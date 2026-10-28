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
    
    # Check antibody claims against engine (case-sensitive comparison)
    for antibody in claimed_antibodies:
        # Compare case-sensitively: 'Jka' must match engine's 'Jka', not 'JKA'
        if antibody not in engine_candidates:
            # Check if it was ruled out (also case-sensitive)
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
    
    Handles:
    - Case-sensitive matching (Jka != JKA, keeps c/C, e/E distinct)
    - Sentence-level negation detection ('not ruled out' handled correctly)
    - Long exclusion lists ('exclude anti-C, anti-Fya, ...' all negated)
    - Positive autocontrol context ('to exclude', 'underlying alloantibody' allowed)
    
    Only flag antibodies CLAIMED as identified, like:
    - 'identified anti-Jka' or 'most likely anti-e'
    
    Do NOT flag mentions like:
    - 'anti-E was ruled out' or 'exclude anti-Fya'
    - 'to exclude underlying alloantibodies' (positive autocontrol context)
    """
    import re
    
    # Common antibody names (preserving case: c != C, e != E, k != K, s != S, Jka != JKA)
    common_abs = [
        'D', 'C', 'c', 'E', 'e', 'K', 'k',
        'Fya', 'Fyb', 'Jka', 'Jkb',
        'S', 's', 'M', 'N', 'U',
        'Lea', 'Leb', 'P1',
        'Kpa', 'Kpb', 'Jsa', 'Jsb'
    ]
    
    text = json.dumps(narrative)
    found = set()
    
    # Positive claim patterns (strong identification)
    positive_claim_patterns = [
        'identified', 'identification', 'most likely', 'likely', 'detected', 'confirmed',
        'candidate', 'suspected', 'suggests', 'indicates', 'consistent with',
        'appears to be', 'is present'
    ]
    
    # Negation patterns (sentence-level)
    negation_patterns = [
        'ruled out', 'exclude', 'excluded', 'negative', 'no evidence',
        'not present', 'absent', 'not detected', 'not identified'
    ]
    
    # Split text into sentences for better context
    # Simple sentence split on '.', '!', '?' followed by space or newline
    sentences = re.split(r'[.!?]\s+', text)
    
    for ab in common_abs:
        # Build pattern: match "anti" case-insensitively, but antibody name case-sensitively
        # This allows "Anti-c" or "anti-c" to match 'c', but "Anti-C" only matches 'C'
        # Use (?i) for case-insensitive "anti" part, then turn it off for the antibody
        ab_pattern = f'(?i)anti[-\\s](?-i:{re.escape(ab)})(?![a-z])'
        
        # Search in each sentence for context
        for sentence in sentences:
            # Check if this EXACT antibody is mentioned (case-sensitive for antibody name)
            match = re.search(ab_pattern, sentence)
            if not match:
                continue
            
            # Found exact antibody mention - check LOCAL context (around this match)
            # Use a window around the match to check if THIS antibody is negated
            match_pos = match.start()
            # Wider window: 50 chars before and after
            before_context = sentence[max(0, match_pos - 50):match_pos]
            after_context = sentence[match_pos:min(len(sentence), match_pos + 50)]
            local_context = (before_context + after_context).lower()
            
            # Check for negation in LOCAL context (near this specific antibody)
            has_local_negation = any(neg in local_context for neg in negation_patterns)
            
            # Check for positive claim in LOCAL context
            has_local_positive = any(pos in local_context for pos in positive_claim_patterns)
            
            # Special case: 'not ruled out' means it's a positive claim
            has_not_ruled_out = 'not ruled out' in local_context
            
            # Special case: allow 'to exclude' and 'underlying alloantibody' (positive autocontrol context)
            # These are process mentions, not claims
            is_process_mention = ('to exclude' in local_context or 
                                 'underlying alloantibod' in local_context)
            
            # Decide if this is a claim
            if has_not_ruled_out:
                # 'not ruled out ... likely present' -> claim
                if has_local_positive:
                    found.add(ab)  # Keep original case
                    break
            elif has_local_negation:
                # Negated locally, skip (but check if it's just process mention)
                if not is_process_mention:
                    continue
                # If it's a process mention without a strong claim, skip
                if not has_local_positive:
                    continue
            elif has_local_positive:
                # Positive claim without negation
                found.add(ab)  # Keep original case
                break
    
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
