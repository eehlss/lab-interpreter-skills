"""
Regression tests for verifier bugs found in production.
Tests built from realistic IH-012 and IH-027 narratives.
"""

import pytest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from agents.verify import verify_llm_output, _extract_claimed_antibodies
from agents.llm import NebiusClient


def test_case_sensitive_matching_jka():
    """
    Bug: Uppercasing 'Jka' to 'JKA' breaks comparison with engine's 'Jka'.
    Fix: Keep case-sensitive matching.
    """
    client = NebiusClient()
    
    # Realistic narrative from IH-012 (anti-Jka with dosage, C co-segregates)
    llm_narrative = {
        'summary': 'Panel analysis reveals anti-Jka with dosage effect and likely anti-C.',
        'antibody_identification': 'Anti-Jka identified (homozygous cells 4+, heterozygous 2+). Anti-C co-segregates.',
        'explanation': 'The pattern suggests anti-Jka with dosage effect. C also appears as a candidate.',
        'disclaimer': 'Research and decision-support only - not for clinical use'
    }
    
    engine_result = {
        'panel_analysis': {
            'candidates': ['C', 'Jka'],  # Engine uses exact case
            'ruled_out': []
        },
        'units': {
            'compatible_units': []
        },
        'flags': []
    }
    
    result = verify_llm_output(client, llm_narrative, engine_result)
    
    # Should pass: 'Jka' in narrative matches engine's 'Jka'
    assert result['verified'] is True, f"Failed with violations: {result.get('violations')}"


def test_keep_c_and_C_distinct():
    """
    Bug: Uppercasing merges c/C, e/E, k/K, s/S.
    Fix: Keep them distinct (c != C).
    """
    # Narrative mentions anti-c (lowercase)
    narrative_c = {
        'text': 'Anti-c identified based on panel reactivity.'
    }
    
    claims_c = _extract_claimed_antibodies(narrative_c)
    
    # Should extract 'c' not 'C'
    assert 'c' in claims_c
    assert 'C' not in claims_c
    
    # Narrative mentions anti-C (uppercase)
    narrative_C = {
        'text': 'Anti-C identified based on panel reactivity.'
    }
    
    claims_C = _extract_claimed_antibodies(narrative_C)
    
    # Should extract 'C' not 'c'
    assert 'C' in claims_C
    assert 'c' not in claims_C


def test_not_ruled_out_with_likely_present():
    """
    Bug: 25-char window treats 'Anti-K was not ruled out ... likely present' as negation.
    Fix: Sentence-level detection, handle 'not ruled out' correctly.
    """
    narrative = {
        'text': 'Anti-K was not ruled out and appears likely present based on the reaction pattern.'
    }
    
    claims = _extract_claimed_antibodies(narrative)
    
    # Should extract K (not ruled out + likely present = claim)
    assert 'K' in claims, f"Should extract K from 'not ruled out ... likely present', got {claims}"


def test_long_exclusion_list():
    """
    Bug: 25-char window might not catch all antigens in 'exclude anti-C, anti-Fya, ...'
    Fix: Sentence-level negation detection handles long lists.
    """
    narrative = {
        'text': 'The pattern allows us to exclude anti-C, anti-E, anti-Fya, anti-Fyb, and anti-Jkb based on negative cells.'
    }
    
    claims = _extract_claimed_antibodies(narrative)
    
    # Should NOT extract any of these (all in exclusion list)
    assert 'C' not in claims
    assert 'E' not in claims
    assert 'Fya' not in claims
    assert 'Fyb' not in claims
    assert 'Jkb' not in claims


def test_positive_autocontrol_to_exclude():
    """
    Bug: 'to exclude underlying alloantibodies' was blocked for positive autocontrol cases.
    Fix: Allow 'to exclude' and 'underlying alloantibody' in positive autocontrol context.
    """
    # Realistic narrative from IH-027 (positive autocontrol, warm AIHA)
    narrative = {
        'summary': 'Positive autocontrol and panreactivity suggest warm autoimmune hemolytic anemia.',
        'explanation': 'The positive autocontrol indicates autoantibody. Further testing needed to exclude underlying alloantibodies.',
        'workup': 'Perform DAT to characterize the autoantibody. May need adsorption studies to exclude alloantibodies.',
        'disclaimer': 'Research and decision-support only - not for clinical use'
    }
    
    claims = _extract_claimed_antibodies(narrative)
    
    # Should NOT extract anything (no specific antibody claims, just process mentions)
    assert len(claims) == 0, f"Should not extract antibodies from 'to exclude' context, got {claims}"


def test_positive_autocontrol_still_blocks_named_claims():
    """
    Even with positive autocontrol, still block named antibody claims like 'most likely anti-e'.
    """
    client = NebiusClient()
    
    # Narrative claims anti-e despite positive autocontrol
    llm_narrative = {
        'summary': 'Positive autocontrol but pattern suggests most likely anti-e.',
        'antibody_identification': 'Anti-e appears most likely despite autocontrol.',
        'disclaimer': 'Research and decision-support only - not for clinical use'
    }
    
    engine_result = {
        'panel_analysis': {
            'candidates': [],  # Engine says no candidates (positive autocontrol)
            'ruled_out': []
        },
        'units': {
            'compatible_units': []
        },
        'flags': ['positive_autocontrol']
    }
    
    result = verify_llm_output(client, llm_narrative, engine_result)
    
    # Should block: LLM claims anti-e but engine has no candidates
    assert result['verified'] is False
    assert any('e' in v for v in result['violations'])


def test_unit_recommendations_still_blocked():
    """
    Verify that invalid unit recommendations are still blocked.
    """
    client = NebiusClient()
    
    llm_narrative = {
        'summary': 'Anti-K identified',
        'antibody_identification': 'Anti-K',
        'unit_selection': 'Recommend unit SYN-RBC-999',
        'disclaimer': 'Research and decision-support only - not for clinical use'
    }
    
    engine_result = {
        'panel_analysis': {
            'candidates': ['K'],
            'ruled_out': []
        },
        'units': {
            'compatible_units': [
                {'unit_id': 'SYN-RBC-001'}  # Not 999
            ]
        },
        'flags': []
    }
    
    result = verify_llm_output(client, llm_narrative, engine_result)
    
    # Should block: unit SYN-RBC-999 not in compatible list
    assert result['verified'] is False
    assert any('SYN-RBC-999' in v for v in result['violations'])


def test_realistic_ih012_narrative():
    """
    Full realistic narrative from IH-012 analysis.
    Should pass with C and Jka correctly extracted.
    """
    client = NebiusClient()
    
    llm_narrative = {
        'summary': 'Antibody panel interpretation reveals anti-Jka with dosage effect. Anti-C co-segregates.',
        'panel_analysis': {
            'positive_cells': 3,
            'negative_cells': 3,
            'pattern': 'Anti-Jka shows characteristic dosage: homozygous cells (1, 5) react 4+, heterozygous cell (3) reacts 2+.',
            'candidates': ['Jka', 'C']
        },
        'antibody_identification': 'Anti-Jka identified with dosage effect. Anti-C also appears as a candidate due to co-segregation.',
        'clinical_significance': 'Anti-Jka can cause severe delayed hemolytic transfusion reactions. Further testing recommended to distinguish C from Jka.',
        'unit_selection': 'Select Jka-negative units. C antigen status should be determined.',
        'disclaimer': 'Research and decision-support only - not for clinical use. All results require review by a qualified professional.'
    }
    
    engine_result = {
        'panel_analysis': {
            'candidates': ['C', 'Jka'],
            'ruled_out': ['E', 'K', 'e']
        },
        'units': {
            'compatible_units': []
        },
        'flags': []
    }
    
    result = verify_llm_output(client, llm_narrative, engine_result)
    
    # Should pass: narrative correctly identifies C and Jka
    assert result['verified'] is True, f"IH-012 narrative failed with violations: {result.get('violations')}"
