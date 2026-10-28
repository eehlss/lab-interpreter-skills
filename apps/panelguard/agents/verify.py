"""
Verifier agent: check LLM output against engine results.
Research and decision-support only - not for clinical use.
"""

import json
from typing import Dict, Any, List, Set
from .llm import NebiusClient


def verify_llm_output(
    client: NebiusClient,
    llm_narrative: Dict[str, Any],
    engine_result: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Verify that LLM narrative does not contradict engine results.
    
    Checks:
    1. All antibody specificities mentioned must be in engine's candidates
    2. All units recommended must be in engine's compatible list
    3. Safety disclaimer must be present
    4. No contradictions of engine safety flags
    
    Args:
        client: NebiusClient instance
        llm_narrative: Explanation or reasoning output from LLM
        engine_result: Deterministic engine results
    
    Returns:
        {
            'verified': bool,
            'violations': [],
            'safe_narrative': dict (original or blocked)
        }
    """
    violations = []
    
    # Extract engine truth
    engine_candidates = set(engine_result.get('panel_analysis', {}).get('candidates', []))
    engine_ruled_out = set(engine_result.get('panel_analysis', {}).get('ruled_out', []))
    engine_compatible_units = [u['unit_id'] for u in engine_result.get('units', {}).get('compatible_units', [])]
    
    # Check disclaimer presence
    narrative_text = json.dumps(llm_narrative).lower()
    if 'research and decision-support only' not in narrative_text:
        violations.append('Missing required disclaimer')
    
    # Extract mentioned antibodies and their context from narrative
    claimed_antibodies = _extract_claimed_antibodies(llm_narrative)
    
    # Check antibody claims against engine (only block false claims, not mentions)
    for antibody in claimed_antibodies:
        if antibody not in engine_candidates:
            if antibody in engine_ruled_out:
                violations.append(f'Antibody {antibody} was ruled out by engine but claimed as candidate/identified')
            else:
                violations.append(f'Antibody {antibody} not in engine candidate list but claimed as identified')
    
    # Check unit recommendations
    mentioned_units = _extract_unit_mentions(llm_narrative)
    
    for unit in mentioned_units:
        if unit not in engine_compatible_units:
            violations.append(f'Unit {unit} not in engine compatible list')
    
    # Check for contradictions of engine flags
    engine_flags = engine_result.get('flags', [])
    
    if 'positive_autocontrol' in str(engine_flags).lower():
        if 'proceed' in narrative_text or 'transfuse' in narrative_text:
            violations.append('Narrative suggests proceeding despite positive autocontrol')
    
    # Build result
    if violations:
        # Block the narrative
        result = {
            'verified': False,
            'violations': violations,
            'safe_narrative': {
                'blocked': True,
                'reason': 'LLM output contradicted deterministic engine results',
                'violations': violations,
                'engine_only_report': _generate_engine_only_report(engine_result)
            }
        }
    else:
        result = {
            'verified': True,
            'violations': [],
            'safe_narrative': llm_narrative
        }
    
    return result


def _extract_claimed_antibodies(narrative: Dict[str, Any]) -> Set[str]:
    """
    Extract antibodies that are CLAIMED as identified or candidates.
    Ignore mentions of ruled-out or negative antibodies.
    
    Only flag antibodies mentioned in positive contexts like:
    - 'identified anti-X'
    - 'likely anti-X'
    - 'anti-X is present'
    - 'candidate anti-X'
    
    Do NOT flag mentions like:
    - 'anti-X was ruled out'
    - 'no evidence of anti-X'
    - 'anti-X is negative'
    """
    import re
    
    # Common antibody names
    common_abs = [
        'D', 'C', 'c', 'E', 'e', 'K', 'k',
        'Fya', 'Fyb', 'Jka', 'Jkb',
        'S', 's', 'M', 'N', 'U',
        'Lea', 'Leb', 'P1',
        'Kpa', 'Kpb', 'Jsa', 'Jsb'
    ]
    
    text = json.dumps(narrative).lower()
    found = set()
    
    # Positive claim patterns (case-insensitive)
    positive_patterns = [
        'identified', 'likely', 'present', 'detected', 'confirmed',
        'candidate', 'suspected', 'suggests', 'indicates', 'consistent with'
    ]
    
    # Negative patterns to exclude
    negative_patterns = [
        'ruled out', 'excluded', 'negative', 'no evidence', 'not present',
        'absent', 'unlikely', 'not detected', 'no anti-'
    ]
    
    # To avoid duplicate matches for K/k, C/c, E/e, track patterns already matched
    matched_patterns = set()
    
    for ab in common_abs:
        # Convert to lowercase for pattern matching
        ab_lower = ab.lower()
        
        # Skip if we already processed this pattern (e.g., both 'K' and 'k' map to 'k')
        if ab_lower in matched_patterns:
            continue
        
        # Pattern: anti- or anti followed by antibody name, not followed by another letter
        ab_pattern = f'\\banti[-\\s]{ab_lower}\\b'
        
        for match in re.finditer(ab_pattern, text):
            # Check immediate context (within 25 chars) for explicit negative phrases
            # This is enough for "anti-X detected" or "anti-X ruled out" but avoids
            # false negatives from unrelated mentions later in the text
            match_pos = match.start()
            before_context = text[max(0, match_pos - 25):match_pos]
            after_context = text[match_pos:min(len(text), match_pos + 25)]
            context = before_context + after_context
            
            # ONLY skip if explicitly negative (ruled out, negative, excluded, etc.)
            # Otherwise, assume it's a claim (safer for verification)
            is_explicit_negative = any(neg in context for neg in negative_patterns)
            
            if not is_explicit_negative:
                # Add uppercase version (normalize to avoid K/k duplication)
                found.add(ab.upper())
                matched_patterns.add(ab_lower)
                break  # Found this antibody pattern, move to next
    
    return found


def _extract_unit_mentions(narrative: Dict[str, Any]) -> Set[str]:
    """Extract unit IDs from narrative text."""
    text = json.dumps(narrative)
    found = set()
    
    # Look for SYN-RBC-XXX pattern
    import re
    matches = re.findall(r'SYN-RBC-\d+', text)
    found.update(matches)
    
    return found


def _generate_engine_only_report(engine_result: Dict[str, Any]) -> Dict[str, Any]:
    """Generate rules-only report when LLM is blocked."""
    panel = engine_result.get('panel_analysis', {})
    units = engine_result.get('units', {})
    
    report = {
        'summary': 'Deterministic rules engine analysis (LLM narrative was blocked due to safety verification failure)',
        'status': panel.get('status', 'unknown'),
        'ruled_out': panel.get('ruled_out', []),
        'candidates': panel.get('candidates', []),
        'confidence': panel.get('confidence', 'unknown'),
        'compatible_units': [u['unit_id'] for u in units.get('compatible_units', [])],
        'flags': engine_result.get('flags', []),
        'disclaimer': 'Research and decision-support only - not for clinical use. All results require review by a qualified professional.'
    }
    
    return report
