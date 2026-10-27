"""
Blood unit selection and compatibility engine.
Research and decision-support only - not for clinical use.
"""

from typing import Dict, List, Optional
import json
from pathlib import Path
import yaml


class UnitsEngine:
    """Deterministic blood unit selection engine."""
    
    def __init__(self, rules_path: Optional[Path] = None, inventory_path: Optional[Path] = None):
        if rules_path is None:
            rules_path = Path(__file__).parent / "rules.yaml"
        
        if inventory_path is None:
            inventory_path = Path(__file__).parent.parent / "data" / "inventory_synthetic.json"
        
        with open(rules_path) as f:
            self.rules = yaml.safe_load(f)
        
        # Load synthetic inventory
        if inventory_path.exists():
            with open(inventory_path) as f:
                self.inventory = json.load(f)
        else:
            self.inventory = []
    
    def select_compatible_units(
        self,
        patient_abo: str,
        patient_rh: str,
        antibody_specificities: List[str],
        patient_sex: str = 'unknown',
        patient_age: int = 99,
        special_requirements: Optional[List[str]] = None,
        product_type: str = 'rbc',
        max_units: int = 5
    ) -> Dict:
        """
        Select compatible blood units.
        
        Args:
            patient_abo: 'O', 'A', 'B', 'AB'
            patient_rh: 'Pos' or 'Neg'
            antibody_specificities: ['K', 'E', ...]
            patient_sex: 'male'/'female'/'unknown'
            patient_age: int
            special_requirements: ['sickle_cell', 'irradiated', 'cmv_negative', ...]
            product_type: 'rbc', 'plasma', 'platelets'
            max_units: maximum number of units to return
        
        Returns:
            {
                'compatible_units': [...],
                'total_compatible': int,
                'requirements': {...},
                'flags': []
            }
        """
        result = {
            'compatible_units': [],
            'total_compatible': 0,
            'requirements': {},
            'flags': []
        }
        
        # Determine ABO compatibility
        if product_type == 'rbc':
            compatible_abos = self.rules['abo_compatibility']['rbc'].get(patient_abo.upper(), [])
        elif product_type == 'plasma':
            compatible_abos = self.rules['abo_compatibility']['plasma'].get(patient_abo.upper(), [])
        else:  # platelets
            compatible_abos = self.rules['abo_compatibility']['platelets'].get(patient_abo.upper(), [])
        
        # Determine Rh requirement
        rh_requirement = 'Neg' if 'neg' in patient_rh.lower() else 'Pos'
        
        # Special rules for D-negative females under 50
        if 'neg' in patient_rh.lower() and \
           patient_sex.lower() in ['f', 'female'] and \
           patient_age < 50:
            rh_requirement = 'Neg_only'
            result['flags'].append('D-negative female under 50: D-negative units required')
        
        # Build requirements dict
        result['requirements'] = {
            'abo': compatible_abos,
            'rh': rh_requirement,
            'antigen_negative': antibody_specificities,
            'special': special_requirements or []
        }
        
        # Special population matching
        if special_requirements and 'sickle_cell' in special_requirements:
            # Extended Rh/K matching for SCD
            extended_match = ['C', 'c', 'E', 'e', 'K']
            for ag in extended_match:
                if ag not in antibody_specificities:
                    antibody_specificities.append(ag)
            result['flags'].append('Sickle cell disease: extended Rh/K matching applied')
        
        # Filter inventory
        compatible = []
        
        for unit in self.inventory:
            if not self._unit_matches_abo(unit, compatible_abos):
                continue
            
            if not self._unit_matches_rh(unit, rh_requirement):
                continue
            
            if not self._unit_is_antigen_negative(unit, antibody_specificities):
                continue
            
            if not self._unit_meets_special_requirements(unit, special_requirements):
                continue
            
            compatible.append(unit)
        
        result['total_compatible'] = len(compatible)
        result['compatible_units'] = compatible[:max_units]
        
        if result['total_compatible'] == 0:
            result['flags'].append('No compatible units in inventory - contact reference laboratory')
        
        return result
    
    def _unit_matches_abo(self, unit: Dict, compatible_abos: List[str]) -> bool:
        """Check if unit ABO is compatible."""
        unit_abo = unit.get('abo', '').upper()
        return unit_abo in compatible_abos
    
    def _unit_matches_rh(self, unit: Dict, rh_requirement: str) -> bool:
        """Check if unit Rh is compatible."""
        unit_rh = unit.get('rh', '').lower()
        
        if rh_requirement == 'Neg_only':
            return 'neg' in unit_rh
        elif rh_requirement == 'Neg':
            return 'neg' in unit_rh
        else:  # Pos
            return True  # Pos patients can receive Pos or Neg
    
    def _unit_is_antigen_negative(self, unit: Dict, antigens: List[str]) -> bool:
        """Check if unit is negative for all specified antigens."""
        phenotype = unit.get('phenotype', {})
        
        for antigen in antigens:
            # Check if unit has this antigen
            antigen_status = phenotype.get(antigen, '0')
            if antigen_status in ['+', '1', 'pos', 'positive']:
                return False
        
        return True
    
    def _unit_meets_special_requirements(
        self,
        unit: Dict,
        requirements: Optional[List[str]]
    ) -> bool:
        """Check if unit meets special requirements."""
        if not requirements:
            return True
        
        attributes = unit.get('attributes', [])
        
        for req in requirements:
            if req == 'irradiated':
                if 'irradiated' not in attributes:
                    return False
            elif req == 'cmv_negative':
                if 'cmv_negative' not in attributes:
                    return False
            elif req == 'hbs_negative':
                if 'hbs_negative' not in attributes:
                    return False
        
        return True
