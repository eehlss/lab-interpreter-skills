"""
Direct Antiglobulin Test (DAT) interpretation engine.
Research and decision-support only - not for clinical use.
"""

from typing import Dict, List, Optional


class DATEngine:
    """DAT/DCT interpretation engine."""
    
    def interpret_dat(
        self,
        polyspecific: str,
        monospecific_igg: Optional[str] = None,
        monospecific_c3d: Optional[str] = None,
        clinical_context: Optional[str] = None
    ) -> Dict:
        """
        Interpret DAT results.
        
        Args:
            polyspecific: '0', '1+', '2+', '3+', '4+'
            monospecific_igg: Optional monospecific anti-IgG result
            monospecific_c3d: Optional monospecific anti-C3d result
            clinical_context: Optional clinical context (e.g., 'hemolytic_anemia', 'daratumumab')
        
        Returns:
            {
                'positive': bool,
                'pattern': str,
                'interpretation': str,
                'workup_path': str,
                'flags': []
            }
        """
        result = {
            'positive': False,
            'pattern': 'negative',
            'interpretation': '',
            'workup_path': '',
            'flags': []
        }
        
        # Parse polyspecific
        poly_positive = self._is_positive(polyspecific)
        
        if not poly_positive:
            result['positive'] = False
            result['pattern'] = 'negative'
            result['interpretation'] = 'Negative DAT'
            return result
        
        result['positive'] = True
        
        # If monospecific not provided, can't determine pattern
        if monospecific_igg is None and monospecific_c3d is None:
            result['pattern'] = 'positive_poly_only'
            result['interpretation'] = 'Positive polyspecific DAT - perform monospecific testing'
            result['flags'].append('Monospecific testing required')
            return result
        
        # Parse monospecific
        igg_positive = self._is_positive(monospecific_igg) if monospecific_igg else False
        c3d_positive = self._is_positive(monospecific_c3d) if monospecific_c3d else False
        
        # Determine pattern
        if igg_positive and c3d_positive:
            result['pattern'] = 'IgG+C3d'
            result['interpretation'] = 'Positive for both IgG and C3d'
            result['workup_path'] = 'warm_aiha_or_mixed'
        elif igg_positive:
            result['pattern'] = 'IgG_only'
            result['interpretation'] = 'Positive for IgG only'
            result['workup_path'] = 'warm_aiha'
            result['flags'].append('Warm autoantibody workup: perform autoadsorption and eluate')
        elif c3d_positive:
            result['pattern'] = 'C3d_only'
            result['interpretation'] = 'Positive for C3d only'
            result['workup_path'] = 'cold_agglutinin_disease'
            result['flags'].append('Cold agglutinin disease: test thermal range and titre')
        
        # Check for daratumumab
        if clinical_context and 'daratumumab' in clinical_context.lower():
            result['flags'].append('Daratumumab interference: use DTT-treated cells for antibody detection')
        
        return result
    
    def _is_positive(self, reaction: Optional[str]) -> bool:
        """Parse reaction grade to boolean."""
        if reaction is None:
            return False
        
        reaction = str(reaction).strip().lower()
        
        if reaction in ['0', 'neg', 'negative', '-', '']:
            return False
        
        if any(x in reaction for x in ['1+', '2+', '3+', '4+', 'w+', '+', 'pos']):
            return True
        
        return False
