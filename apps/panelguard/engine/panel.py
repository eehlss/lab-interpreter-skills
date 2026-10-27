"""
Antibody panel rule-out and identification engine.
Research and decision-support only - not for clinical use.
"""

from typing import Dict, List, Optional, Set, Tuple
import yaml
from pathlib import Path


class PanelEngine:
    """Deterministic antibody panel interpretation engine."""
    
    def __init__(self, rules_path: Optional[Path] = None):
        if rules_path is None:
            rules_path = Path(__file__).parent / "rules.yaml"
        
        with open(rules_path) as f:
            self.rules = yaml.safe_load(f)
        
        self.dosage_antigens = set(self.rules['dosage_antigens'])
    
    def analyze_panel(
        self,
        panel_cells: List[Dict],
        autocontrol: str
    ) -> Dict:
        """
        Analyze antibody panel and identify antibody specificities.
        
        Args:
            panel_cells: List of cell reactions, e.g.:
                [{
                    'cell_id': '1',
                    'reaction': '4+',
                    'antigens': {'D': '+', 'C': '+', 'E': '0', 'c': '0', 'e': '+', 
                                'K': '0', 'Fya': '+', 'Fyb': '0', 'Jka': '+', 'Jkb': '0'},
                    'dosage': {'C': 'homozygous', 'Fya': 'heterozygous', 'Jka': 'homozygous'}
                }, ...]
            autocontrol: '0', '1+', '2+', etc.
        
        Returns:
            {
                'status': 'ok' | 'positive_autocontrol' | 'insufficient_cells',
                'ruled_out': ['E', 'c', 'K', ...],
                'candidates': ['D', 'Fya', ...],
                'confidence': 'high' | 'moderate' | 'low',
                'positive_cells': 5,
                'negative_cells': 6,
                'flags': []
            }
        """
        result = {
            'status': 'ok',
            'ruled_out': [],
            'candidates': [],
            'confidence': 'low',
            'positive_cells': 0,
            'negative_cells': 0,
            'flags': []
        }
        
        # Check autocontrol first
        if self._is_positive(autocontrol):
            result['status'] = 'positive_autocontrol'
            result['flags'].append('Positive autocontrol - route to DAT workup')
            return result
        
        # Initialize tracking
        all_antigens = self._get_all_antigens(panel_cells)
        ruled_out = set()
        
        # Rule-out phase
        for cell in panel_cells:
            cell_reaction = cell.get('reaction', '0')
            
            if not self._is_positive(cell_reaction):
                # Negative cell: rule out antigens present on this cell
                antigens = cell.get('antigens', {})
                dosage = cell.get('dosage', {})
                
                for antigen, presence in antigens.items():
                    if self._is_antigen_positive(presence):
                        # For dosage antigens, only homozygous cells can rule out
                        if antigen in self.dosage_antigens:
                            if dosage.get(antigen) == 'homozygous':
                                ruled_out.add(antigen)
                        else:
                            ruled_out.add(antigen)
        
        result['ruled_out'] = sorted(list(ruled_out))
        
        # Find candidates (not ruled out)
        candidates = all_antigens - ruled_out
        
        # For each candidate, verify all positive cells have the antigen
        verified_candidates = set()
        
        for antigen in candidates:
            all_pos_cells_have_it = True
            all_neg_cells_lack_it = True
            pos_count = 0
            neg_count = 0
            
            for cell in panel_cells:
                cell_reaction = cell.get('reaction', '0')
                antigen_presence = cell.get('antigens', {}).get(antigen, '0')
                has_antigen = self._is_antigen_positive(antigen_presence)
                
                if self._is_positive(cell_reaction):
                    pos_count += 1
                    if not has_antigen:
                        all_pos_cells_have_it = False
                else:
                    neg_count += 1
                    if has_antigen:
                        # For dosage antigens, check if it's homozygous
                        if antigen in self.dosage_antigens:
                            dosage = cell.get('dosage', {})
                            if dosage.get(antigen) == 'homozygous':
                                all_neg_cells_lack_it = False
                        else:
                            all_neg_cells_lack_it = False
            
            if all_pos_cells_have_it:
                verified_candidates.add(antigen)
                
                # Check confidence based on 3+/3- or 5+/5- rule
                if pos_count >= self.rules['rule_of_three']['high_confidence_pos'] and \
                   neg_count >= self.rules['rule_of_three']['high_confidence_neg']:
                    result['confidence'] = 'high'
                elif pos_count >= self.rules['rule_of_three']['min_positive'] and \
                     neg_count >= self.rules['rule_of_three']['min_negative']:
                    if result['confidence'] != 'high':
                        result['confidence'] = 'moderate'
        
        result['candidates'] = sorted(list(verified_candidates))
        result['positive_cells'] = sum(1 for c in panel_cells if self._is_positive(c.get('reaction', '0')))
        result['negative_cells'] = sum(1 for c in panel_cells if not self._is_positive(c.get('reaction', '0')))
        
        # Check for insufficient cells
        if result['candidates']:
            min_pos = self.rules['rule_of_three']['min_positive']
            min_neg = self.rules['rule_of_three']['min_negative']
            
            if result['positive_cells'] < min_pos or result['negative_cells'] < min_neg:
                result['status'] = 'insufficient_cells'
                result['flags'].append(f'Insufficient cells for statistical confidence (need {min_pos}+/{min_neg}-)')
        
        # Check for multiple antibodies
        if len(result['candidates']) > 1:
            result['flags'].append('Multiple antibody candidates - possible mixture')
        
        # If no candidates found but panel is reactive
        if not result['candidates'] and result['positive_cells'] > 0:
            result['flags'].append('High-prevalence antibody pattern - refer to reference laboratory')
        
        return result
    
    def _get_all_antigens(self, panel_cells: List[Dict]) -> Set[str]:
        """Extract all antigens present in panel."""
        antigens = set()
        for cell in panel_cells:
            antigens.update(cell.get('antigens', {}).keys())
        return antigens
    
    def _is_positive(self, reaction: str) -> bool:
        """Parse gel reaction grade to boolean."""
        reaction = str(reaction).strip().lower()
        
        if reaction in ['0', 'neg', 'negative', '-', '']:
            return False
        
        if any(x in reaction for x in ['1+', '2+', '3+', '4+', 'w+', '+', 'pos', 'mf']):
            return True
        
        return False
    
    def _is_antigen_positive(self, presence: str) -> bool:
        """Check if antigen is present on cell."""
        presence = str(presence).strip()
        return presence in ['+', '1', 'pos', 'positive']
    
    def is_complex_case(
        self,
        autocontrol: str,
        num_candidates: int,
        positive_cells: int,
        negative_cells: int,
        dat_positive: bool = False,
        special_population: bool = False
    ) -> bool:
        """
        Determine if case should be routed to hard tier (Ultra model).
        
        Complexity triggers from rules:
        - positive_autocontrol
        - multiple_antibodies (>1 candidate)
        - insufficient_cells
        - positive_dat
        - special_population
        """
        if self._is_positive(autocontrol):
            return True
        
        if num_candidates > 1:
            return True
        
        min_pos = self.rules['rule_of_three']['min_positive']
        min_neg = self.rules['rule_of_three']['min_negative']
        
        if positive_cells < min_pos or negative_cells < min_neg:
            return True
        
        if dat_positive:
            return True
        
        if special_population:
            return True
        
        return False
