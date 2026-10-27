"""
Tests for unit selection engine.
Research and decision-support only - not for clinical use.
"""

import pytest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from engine.units import UnitsEngine


def test_select_k_negative_units():
    """Test selection of K-negative units for anti-K."""
    engine = UnitsEngine()
    
    result = engine.select_compatible_units(
        patient_abo='O',
        patient_rh='Pos',
        antibody_specificities=['K'],
        patient_sex='male',
        patient_age=55
    )
    
    assert result['total_compatible'] > 0
    
    # All returned units must be K-negative
    for unit in result['compatible_units']:
        k_status = unit['phenotype'].get('K', '0')
        assert k_status in ['0', 'neg', 'negative']


def test_d_negative_female_under_50():
    """Test D-negative female under 50 gets D-negative only."""
    engine = UnitsEngine()
    
    result = engine.select_compatible_units(
        patient_abo='O',
        patient_rh='Neg',
        antibody_specificities=[],
        patient_sex='female',
        patient_age=28
    )
    
    assert 'D-negative female under 50' in str(result['flags'])
    
    # All units must be D-negative
    for unit in result['compatible_units']:
        rh = unit['rh'].lower()
        assert 'neg' in rh


def test_multiple_antibodies():
    """Test selection with multiple antibody specificities."""
    engine = UnitsEngine()
    
    result = engine.select_compatible_units(
        patient_abo='A',
        patient_rh='Pos',
        antibody_specificities=['K', 'E', 'Fya'],
        patient_sex='male',
        patient_age=45
    )
    
    # All returned units must be K-, E-, Fya-negative
    for unit in result['compatible_units']:
        assert unit['phenotype'].get('K', '0') in ['0', 'neg']
        assert unit['phenotype'].get('E', '0') in ['0', 'neg']
        assert unit['phenotype'].get('Fya', '0') in ['0', 'neg']


def test_sickle_cell_extended_matching():
    """Test extended Rh/K matching for sickle cell disease."""
    engine = UnitsEngine()
    
    result = engine.select_compatible_units(
        patient_abo='O',
        patient_rh='Pos',
        antibody_specificities=[],
        patient_sex='female',
        patient_age=25,
        special_requirements=['sickle_cell']
    )
    
    assert 'sickle cell' in str(result['flags']).lower()
    
    # Extended antigens should be in requirements
    extended = result['requirements']['antigen_negative']
    assert 'C' in extended or 'E' in extended or 'K' in extended


def test_no_compatible_units():
    """Test when no compatible units exist."""
    engine = UnitsEngine()
    
    # Request impossible combination
    result = engine.select_compatible_units(
        patient_abo='AB',
        patient_rh='Neg',
        antibody_specificities=['D', 'C', 'E', 'c', 'e', 'K', 'k', 'Fya', 'Fyb', 'Jka', 'Jkb'],
        patient_sex='female',
        patient_age=30
    )
    
    assert result['total_compatible'] == 0
    assert 'no compatible units' in str(result['flags']).lower()


def test_abo_compatibility():
    """Test ABO compatibility in unit selection."""
    engine = UnitsEngine()
    
    # O patient gets O only
    result = engine.select_compatible_units(
        patient_abo='O',
        patient_rh='Pos',
        antibody_specificities=[],
        patient_sex='male',
        patient_age=50
    )
    
    for unit in result['compatible_units']:
        assert unit['abo'] == 'O'
    
    # AB patient can get any ABO
    result = engine.select_compatible_units(
        patient_abo='AB',
        patient_rh='Pos',
        antibody_specificities=[],
        patient_sex='male',
        patient_age=50
    )
    
    # Should have units of various ABO types
    abos = set(u['abo'] for u in result['compatible_units'])
    assert len(abos) > 1  # Multiple ABO types available
