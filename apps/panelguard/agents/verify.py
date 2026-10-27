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
    
    # Extract mentioned antibodies from narrative
    mentioned_antibodies = _extract_antibody_mentions(llm_narrative)
    
    # Check antibody mentions against engine
    for antibody in mentioned_antibodies:
        if antibody not in engine_candidates:
            if antibody in engine_ruled_out:
                violations.append(f'Antibody {antibody} was ruled out by engine but mentioned as candidate')
            else:
                violations.append(f'Antibody {antibody} not in engine candidate list')
    
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


def _extract_antibody_mentions(narrative: Dict[str, Any]) -> Set[str]:
    """Extract antibody names from narrative text - only anti-X pattern."""
    # Common antibody names
    common_abs = [
        'D', 'C', 'c', 'E', 'e', 'K', 'k',
        'Fya', 'Fyb', 'Jka', 'Jkb',
        'S', 's', 'M', 'N', 'U',
        'Lea', 'Leb', 'P1',
        'Kpa', 'Kpb', 'Jsa', 'Jsb'
    ]
    
    text = json.dumps(narrative)
    found = set()
    
    for ab in common_abs:
        # Only match "anti-X" or "Anti-X" patterns to be precise
        patterns = [
            f'anti-{ab}',
            f'Anti-{ab}',
            f'anti {ab}',
            f'Anti {ab}'
        ]
        
        if any(pattern in text for pattern in patterns):
            found.add(ab)
    
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
