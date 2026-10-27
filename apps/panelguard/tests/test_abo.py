"""
Tests for ABO engine.
Research and decision-support only - not for clinical use.
"""

import pytest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from engine.abo import ABOEngine


def test_forward_reverse_typing_a_pos():
    """Test routine A Pos typing."""
    engine = ABOEngine()
    
    forward = {'anti_a': '4+', 'anti_b': '0', 'anti_d': '4+'}
    reverse = {'a1_cells': '0', 'b_cells': '4+'}
    
    blood_type, flags = engine.check_forward_reverse_typing(forward, reverse)
    
    assert blood_type == 'A Pos'
    assert len(flags) == 0


def test_forward_reverse_typing_o_neg():
    """Test O Neg typing."""
    engine = ABOEngine()
    
    forward = {'anti_a': '0', 'anti_b': '0', 'anti_d': '0'}
    reverse = {'a1_cells': '4+', 'b_cells': '4+'}
    
    blood_type, flags = engine.check_forward_reverse_typing(forward, reverse)
    
    assert blood_type == 'O Neg'
    assert len(flags) == 0


def test_abo_discrepancy():
    """Test ABO discrepancy detection."""
    engine = ABOEngine()
    
    # Forward suggests A, but reverse missing expected B cell reaction
    forward = {'anti_a': '4+', 'anti_b': '0', 'anti_d': '4+'}
    reverse = {'a1_cells': '0', 'b_cells': '0'}  # Should be positive
    
    blood_type, flags = engine.check_forward_reverse_typing(forward, reverse)
    
    assert blood_type is None
    assert len(flags) > 0
    assert 'reverse_b_discrepancy' in flags[0]


def test_rbc_compatibility():
    """Test RBC compatibility rules."""
    engine = ABOEngine()
    
    # O patient can only receive O
    assert engine.check_rbc_compatibility('O', 'O') is True
    assert engine.check_rbc_compatibility('O', 'A') is False
    
    # AB patient can receive any
    assert engine.check_rbc_compatibility('AB', 'O') is True
    assert engine.check_rbc_compatibility('AB', 'A') is True
    assert engine.check_rbc_compatibility('AB', 'B') is True
    assert engine.check_rbc_compatibility('AB', 'AB') is True
    
    # A patient can receive A or O
    assert engine.check_rbc_compatibility('A', 'O') is True
    assert engine.check_rbc_compatibility('A', 'A') is True
    assert engine.check_rbc_compatibility('A', 'B') is False


def test_plasma_compatibility():
    """Test plasma compatibility rules."""
    engine = ABOEngine()
    
    # O plasma can go to anyone
    assert engine.check_plasma_compatibility('O', 'O') is True
    assert engine.check_plasma_compatibility('A', 'O') is False  # A patient gets A or AB plasma
    assert engine.check_plasma_compatibility('A', 'A') is True
    assert engine.check_plasma_compatibility('A', 'AB') is True
    
    # AB patient gets AB plasma only
    assert engine.check_plasma_compatibility('AB', 'AB') is True
    assert engine.check_plasma_compatibility('AB', 'A') is False


def test_rh_requirement_female_under_50():
    """Test D-negative female under 50 requires D-negative."""
    engine = ABOEngine()
    
    requirement = engine.get_rh_requirement(
        patient_rh='Neg',
        patient_sex='female',
        patient_age=28,
        is_partial_d=False
    )
    
    assert requirement == 'Neg_only'


def test_rh_requirement_partial_d():
    """Test partial D treated as D-negative."""
    engine = ABOEngine()
    
    requirement = engine.get_rh_requirement(
        patient_rh='Pos',  # Even if forward types as Pos
        patient_sex='female',
        patient_age=28,
        is_partial_d=True
    )
    
    assert requirement == 'Neg_only'


def test_rh_requirement_male_d_neg():
    """Test D-negative male can receive D-negative (no strict requirement)."""
    engine = ABOEngine()
    
    requirement = engine.get_rh_requirement(
        patient_rh='Neg',
        patient_sex='male',
        patient_age=55,
        is_partial_d=False
    )
    
    assert requirement == 'Neg'


def test_rh_requirement_d_pos():
    """Test D-positive patients can receive D-positive."""
    engine = ABOEngine()
    
    requirement = engine.get_rh_requirement(
        patient_rh='Pos',
        patient_sex='female',
        patient_age=28,
        is_partial_d=False
    )
    
    assert requirement == 'Pos'
