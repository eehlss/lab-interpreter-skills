"""
ABO/Rh blood group typing and compatibility engine.
Research and decision-support only - not for clinical use.
"""

from typing import Dict, List, Optional, Tuple
import yaml
from pathlib import Path


class ABOEngine:
    """Deterministic ABO and Rh compatibility engine."""
    
    def __init__(self, rules_path: Optional[Path] = None):
        if rules_path is None:
            rules_path = Path(__file__).parent / "rules.yaml"
        
        with open(rules_path) as f:
            self.rules = yaml.safe_load(f)
    
    def check_forward_reverse_typing(
        self,
        forward: Dict[str, str],
        reverse: Dict[str, str]
    ) -> Tuple[Optional[str], List[str]]:
        """
        Check ABO typing consistency.
        
        Args:
            forward: {'anti_a': '4+', 'anti_b': '0', 'anti_d': '4+'}
            reverse: {'a1_cells': '0', 'b_cells': '4+'}
        
        Returns:
            (blood_type, discrepancy_flags)
        """
        flags = []
        
        # Parse forward typing
        anti_a = self._parse_reaction(forward.get('anti_a', '0'))
        anti_b = self._parse_reaction(forward.get('anti_b', '0'))
        anti_d = self._parse_reaction(forward.get('anti_d', '0'))
        
        # Parse reverse typing
        a1_cells = self._parse_reaction(reverse.get('a1_cells', '0'))
        b_cells = self._parse_reaction(reverse.get('b_cells', '0'))
        
        # Determine expected ABO
        if anti_a and anti_b:
            expected_forward = 'AB'
            expected_a1 = False
            expected_b = False
        elif anti_a:
            expected_forward = 'A'
            expected_a1 = False
            expected_b = True
        elif anti_b:
            expected_forward = 'B'
            expected_a1 = True
            expected_b = False
        else:
            expected_forward = 'O'
            expected_a1 = True
            expected_b = True
        
        # Check for discrepancies
        if a1_cells != expected_a1:
            flags.append(f"reverse_a1_discrepancy: expected {'positive' if expected_a1 else 'negative'}, got {'positive' if a1_cells else 'negative'}")
        
        if b_cells != expected_b:
            flags.append(f"reverse_b_discrepancy: expected {'positive' if expected_b else 'negative'}, got {'positive' if b_cells else 'negative'}")
        
        # Determine Rh
        rh = 'Pos' if anti_d else 'Neg'
        
        # Return type or None if discrepancy
        if flags:
            return None, flags
        
        return f"{expected_forward} {rh}", flags
    
    def check_rbc_compatibility(
        self,
        patient_abo: str,
        donor_abo: str
    ) -> bool:
        """
        Check if donor RBC unit is compatible with patient.
        
        Args:
            patient_abo: 'O', 'A', 'B', or 'AB'
            donor_abo: 'O', 'A', 'B', or 'AB'
        
        Returns:
            True if compatible, False otherwise
        """
        patient_abo = patient_abo.upper().strip()
        donor_abo = donor_abo.upper().strip()
        
        compatible = self.rules['abo_compatibility']['rbc'].get(patient_abo, [])
        return donor_abo in compatible
    
    def check_plasma_compatibility(
        self,
        patient_abo: str,
        donor_abo: str
    ) -> bool:
        """Check if donor plasma is compatible with patient."""
        patient_abo = patient_abo.upper().strip()
        donor_abo = donor_abo.upper().strip()
        
        compatible = self.rules['abo_compatibility']['plasma'].get(patient_abo, [])
        return donor_abo in compatible
    
    def check_platelet_compatibility(
        self,
        patient_abo: str,
        donor_abo: str
    ) -> bool:
        """Check if donor platelets are compatible with patient."""
        patient_abo = patient_abo.upper().strip()
        donor_abo = donor_abo.upper().strip()
        
        compatible = self.rules['abo_compatibility']['platelets'].get(patient_abo, [])
        return donor_abo in compatible
    
    def get_rh_requirement(
        self,
        patient_rh: str,
        patient_sex: str,
        patient_age: int,
        is_partial_d: bool = False
    ) -> str:
        """
        Determine Rh requirement for patient.
        
        Returns:
            'Pos', 'Neg', or 'Neg_only'
        """
        # Normalize Rh
        patient_rh = patient_rh.lower()
        is_d_negative = 'neg' in patient_rh or patient_rh == 'd-'
        
        # Partial D always treated as D-negative
        if is_partial_d:
            is_d_negative = True
        
        if not is_d_negative:
            return 'Pos'
        
        # D-negative patient
        # Females under 50 must receive D-negative
        if patient_sex.lower() in ['f', 'female'] and patient_age < 50:
            return 'Neg_only'
        
        return 'Neg'
    
    def _parse_reaction(self, reaction: str) -> bool:
        """Parse gel reaction grade to boolean."""
        reaction = str(reaction).strip().lower()
        
        # Negative reactions
        if reaction in ['0', 'neg', 'negative', '-', '']:
            return False
        
        # Positive reactions
        if any(x in reaction for x in ['1+', '2+', '3+', '4+', 'w+', '+', 'pos', 'mf']):
            return True
        
        return False
    
    def get_compatible_rbc_types(self, patient_abo: str) -> List[str]:
        """Get list of compatible RBC ABO types for patient."""
        patient_abo = patient_abo.upper().strip()
        return self.rules['abo_compatibility']['rbc'].get(patient_abo, [])
    
    def get_compatible_plasma_types(self, patient_abo: str) -> List[str]:
        """Get list of compatible plasma ABO types for patient."""
        patient_abo = patient_abo.upper().strip()
        return self.rules['abo_compatibility']['plasma'].get(patient_abo, [])
