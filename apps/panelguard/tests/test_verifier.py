"""
Tests for LLM output verifier.
Research and decision-support only - not for clinical use.
"""

import pytest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from agents.verify import verify_llm_output, _extract_antibody_mentions
from agents.llm import NebiusClient


def test_verifier_accepts_correct_output():
    """Test verifier accepts output matching engine."""
    client = NebiusClient()  # Offline is fine for this test
    
    llm_narrative = {
        'summary': 'Analysis complete. K antibody confirmed.',
        'antibody_identification': 'Antibody K confirmed by rule-out methodology',
        'rule_out_explanation': 'Other antigens were ruled out based on non-reactive cells',
        'unit_selection_rationale': 'Compatible units are K-negative. Unit SYN-RBC-002 recommended.',
        'safety_notes': 'Standard precautions',
        'disclaimer': 'Research and decision-support only - not for clinical use'
    }
    
    engine_result = {
        'panel_analysis': {
            'candidates': ['K'],
            'ruled_out': []
        },
        'units': {
            'compatible_units': [
                {'unit_id': 'SYN-RBC-002'}
            ]
        },
        'flags': []
    }
    
    result = verify_llm_output(client, llm_narrative, engine_result)
    
    # Should pass: narrative mentions K (in candidates), SYN-RBC-002 (in compatible), has disclaimer
    # If it fails, check what violations were found
    if not result['verified']:
        print("Violations:", result['violations'])
    
    assert result['verified'] is True
    assert len(result['violations']) == 0


def test_verifier_blocks_contradictory_antibody():
    """Test verifier blocks antibody not in engine candidates."""
    client = NebiusClient()
    
    llm_narrative = {
        'summary': 'Anti-E identified',  # Wrong!
        'antibody_identification': 'Anti-E confirmed',
        'rule_out_explanation': 'K ruled out',
        'unit_selection_rationale': 'Units recommended',
        'safety_notes': 'None',
        'disclaimer': 'Research and decision-support only - not for clinical use'
    }
    
    engine_result = {
        'panel_analysis': {
            'candidates': ['K'],  # Engine says K, not E
            'ruled_out': ['E', 'c']
        },
        'units': {
            'compatible_units': [
                {'unit_id': 'SYN-RBC-002'}
            ]
        },
        'flags': []
    }
    
    result = verify_llm_output(client, llm_narrative, engine_result)
    
    assert result['verified'] is False
    assert len(result['violations']) > 0
    assert any('E' in v for v in result['violations'])


def test_verifier_blocks_incompatible_unit():
    """Test verifier blocks unit not in engine compatible list."""
    client = NebiusClient()
    
    llm_narrative = {
        'summary': 'Anti-K identified',
        'antibody_identification': 'Anti-K',
        'rule_out_explanation': 'E ruled out',
        'unit_selection_rationale': 'SYN-RBC-999 recommended',  # Not in engine list
        'safety_notes': 'None',
        'disclaimer': 'Research and decision-support only - not for clinical use'
    }
    
    engine_result = {
        'panel_analysis': {
            'candidates': ['K'],
            'ruled_out': ['E']
        },
        'units': {
            'compatible_units': [
                {'unit_id': 'SYN-RBC-002'}
            ]
        },
        'flags': []
    }
    
    result = verify_llm_output(client, llm_narrative, engine_result)
    
    assert result['verified'] is False
    assert any('SYN-RBC-999' in v for v in result['violations'])


def test_verifier_requires_disclaimer():
    """Test verifier requires disclaimer."""
    client = NebiusClient()
    
    llm_narrative = {
        'summary': 'Anti-K identified',
        'antibody_identification': 'Anti-K',
        'rule_out_explanation': 'E ruled out',
        'unit_selection_rationale': 'Units OK',
        'safety_notes': 'None',
        'disclaimer': ''  # Missing required text
    }
    
    engine_result = {
        'panel_analysis': {
            'candidates': ['K'],
            'ruled_out': ['E']
        },
        'units': {
            'compatible_units': []
        },
        'flags': []
    }
    
    result = verify_llm_output(client, llm_narrative, engine_result)
    
    assert result['verified'] is False
    assert any('disclaimer' in v.lower() for v in result['violations'])


def test_extract_antibody_mentions():
    """Test antibody name extraction."""
    narrative = {
        'text': 'Anti-K and anti-E identified. anti-c ruled out.'
    }
    
    mentions = _extract_antibody_mentions(narrative)
    
    assert 'K' in mentions
    assert 'E' in mentions
    assert 'c' in mentions


def test_verifier_blocked_output_has_engine_report():
    """Test that blocked output includes engine-only report."""
    client = NebiusClient()
    
    llm_narrative = {
        'summary': 'Wrong antibody',
        'antibody_identification': 'Anti-E',  # Wrong
        'disclaimer': 'Research and decision-support only - not for clinical use'
    }
    
    engine_result = {
        'panel_analysis': {
            'candidates': ['K'],
            'ruled_out': ['E']
        },
        'units': {
            'compatible_units': []
        },
        'flags': []
    }
    
    result = verify_llm_output(client, llm_narrative, engine_result)
    
    assert result['verified'] is False
    assert 'safe_narrative' in result
    assert result['safe_narrative']['blocked'] is True
    assert 'engine_only_report' in result['safe_narrative']
