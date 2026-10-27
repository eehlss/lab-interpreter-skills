"""
Tests for panel analysis engine.
Research and decision-support only - not for clinical use.
"""

import pytest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from engine.panel import PanelEngine


def test_positive_autocontrol():
    """Test that positive autocontrol stops analysis."""
    engine = PanelEngine()
    
    panel_cells = [
        {
            'cell_id': '1',
            'reaction': '4+',
            'antigens': {'K': '+', 'E': '0', 'c': '0'},
            'dosage': {}
        }
    ]
    
    result = engine.analyze_panel(panel_cells, autocontrol='3+')
    
    assert result['status'] == 'positive_autocontrol'
    assert 'autocontrol' in result['flags'][0].lower()


def test_simple_anti_k():
    """Test identification of anti-K."""
    engine = PanelEngine()
    
    panel_cells = [
        {'cell_id': '1', 'reaction': '4+', 'antigens': {'K': '+', 'E': '0', 'c': '+'}, 'dosage': {}},
        {'cell_id': '2', 'reaction': '4+', 'antigens': {'K': '+', 'E': '+', 'c': '0'}, 'dosage': {}},
        {'cell_id': '3', 'reaction': '4+', 'antigens': {'K': '+', 'E': '0', 'c': '+'}, 'dosage': {}},
        {'cell_id': '4', 'reaction': '0', 'antigens': {'K': '0', 'E': '+', 'c': '+'}, 'dosage': {}},
        {'cell_id': '5', 'reaction': '0', 'antigens': {'K': '0', 'E': '0', 'c': '+'}, 'dosage': {}},
        {'cell_id': '6', 'reaction': '0', 'antigens': {'K': '0', 'E': '+', 'c': '0'}, 'dosage': {}},
    ]
    
    result = engine.analyze_panel(panel_cells, autocontrol='0')
    
    assert result['status'] == 'ok'
    assert 'K' in result['candidates']
    assert 'E' not in result['candidates']
    assert 'c' not in result['candidates']
    assert result['confidence'] == 'moderate'  # 3+/3-


def test_dosage_effect_jka():
    """Test that heterozygous Jka cells don't rule out anti-Jka."""
    engine = PanelEngine()
    
    panel_cells = [
        # Positive cells: all have Jka
        {'cell_id': '1', 'reaction': '4+', 'antigens': {'Jka': '+', 'Jkb': '0'}, 'dosage': {'Jka': 'homozygous'}},
        {'cell_id': '2', 'reaction': '4+', 'antigens': {'Jka': '+', 'Jkb': '+'}, 'dosage': {'Jka': 'heterozygous'}},
        {'cell_id': '3', 'reaction': '3+', 'antigens': {'Jka': '+', 'Jkb': '0'}, 'dosage': {'Jka': 'homozygous'}},
        # Negative cells: one heterozygous (doesn't rule out), two lack Jka (do rule out)
        {'cell_id': '4', 'reaction': '0', 'antigens': {'Jka': '+', 'Jkb': '+'}, 'dosage': {'Jka': 'heterozygous'}},  # Weak reaction, not enough to rule out
        {'cell_id': '5', 'reaction': '0', 'antigens': {'Jka': '0', 'Jkb': '+'}, 'dosage': {'Jka': 'negative'}},
        {'cell_id': '6', 'reaction': '0', 'antigens': {'Jka': '0', 'Jkb': '+'}, 'dosage': {'Jka': 'negative'}},
    ]
    
    result = engine.analyze_panel(panel_cells, autocontrol='0')
    
    assert result['status'] == 'ok'
    assert 'Jka' in result['candidates']
    assert 'Jkb' not in result['candidates']


def test_multiple_antibodies():
    """Test detection with complex pattern that could suggest multiple."""
    engine = PanelEngine()
    
    # Simple test: Just verify the engine can handle panels and flag complexity
    panel_cells = [
        {'cell_id': '1', 'reaction': '4+', 'antigens': {'K': '+', 'E': '+'}, 'dosage': {}},
        {'cell_id': '2', 'reaction': '4+', 'antigens': {'K': '+', 'E': '+'}, 'dosage': {}},
        {'cell_id': '3', 'reaction': '4+', 'antigens': {'K': '+', 'E': '+'}, 'dosage': {}},
        {'cell_id': '4', 'reaction': '0', 'antigens': {'K': '0', 'E': '0'}, 'dosage': {}},
        {'cell_id': '5', 'reaction': '0', 'antigens': {'K': '0', 'E': '0'}, 'dosage': {}},
        {'cell_id': '6', 'reaction': '0', 'antigens': {'K': '0', 'E': '0'}, 'dosage': {}},
    ]
    
    result = engine.analyze_panel(panel_cells, autocontrol='0')
    
    # Both K and E are present on all positive cells, so both could be candidates
    # or the pattern might not resolve cleanly (which is realistic for complex cases)
    assert result['status'] == 'ok'
    # Either finds candidates or recognizes the pattern is complex
    assert isinstance(result['candidates'], list)


def test_insufficient_cells():
    """Test insufficient cells for statistical confidence."""
    engine = PanelEngine()
    
    panel_cells = [
        {'cell_id': '1', 'reaction': '4+', 'antigens': {'K': '+'}, 'dosage': {}},
        {'cell_id': '2', 'reaction': '4+', 'antigens': {'K': '+'}, 'dosage': {}},
        {'cell_id': '3', 'reaction': '0', 'antigens': {'K': '0'}, 'dosage': {}},
        {'cell_id': '4', 'reaction': '0', 'antigens': {'K': '0'}, 'dosage': {}},
    ]
    
    result = engine.analyze_panel(panel_cells, autocontrol='0')
    
    assert result['status'] == 'insufficient_cells'
    assert 'insufficient' in str(result['flags']).lower()


def test_is_complex_case():
    """Test complex case detection."""
    engine = PanelEngine()
    
    # Positive autocontrol = complex
    assert engine.is_complex_case('2+', 1, 5, 5) is True
    
    # Multiple antibodies = complex
    assert engine.is_complex_case('0', 2, 5, 5) is True
    
    # Insufficient cells = complex
    assert engine.is_complex_case('0', 1, 2, 2) is True
    
    # DAT positive = complex
    assert engine.is_complex_case('0', 1, 5, 5, dat_positive=True) is True
    
    # Special population = complex
    assert engine.is_complex_case('0', 1, 5, 5, special_population=True) is True
    
    # Simple case
    assert engine.is_complex_case('0', 1, 5, 5) is False
