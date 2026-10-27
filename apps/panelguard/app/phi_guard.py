"""
PHI guard: reject input that looks like real patient data.
Research and decision-support only - not for clinical use.
"""

import re
from typing import Dict, List, Tuple
from datetime import datetime


def check_phi_violations(input_data: Dict) -> Tuple[bool, List[str]]:
    """
    Check if input contains PHI-like data.
    
    Returns:
        (is_safe, violations)
    """
    violations = []
    
    # Convert to string for pattern checking
    input_str = str(input_data)
    
    # Check for non-2099 dates (real dates)
    date_patterns = [
        r'\b(19|20)\d{2}[/-](0[1-9]|1[0-2])[/-](0[1-9]|[12]\d|3[01])\b',  # YYYY-MM-DD
        r'\b(0[1-9]|1[0-2])[/-](0[1-9]|[12]\d|3[01])[/-](19|20)\d{2}\b',  # MM-DD-YYYY
        r'\b(0[1-9]|[12]\d|3[01])[/-](0[1-9]|1[0-2])[/-](19|20)\d{2}\b',  # DD-MM-YYYY
    ]
    
    current_year = datetime.now().year
    
    for pattern in date_patterns:
        matches = re.findall(pattern, input_str)
        for match in matches:
            # Extract year
            year_match = re.search(r'(19|20)\d{2}', str(match))
            if year_match:
                year = int(year_match.group())
                if year != 2099 and year <= current_year:
                    violations.append(f'Real date detected: use synthetic dates in year 2099 only')
                    break
    
    # Check for MRN-like patterns (not SYN-)
    mrn_patterns = [
        r'\b(?!SYN-)[A-Z]{2,4}-?\d{6,10}\b',  # MRN-1234567
        r'\b(?!SYN-)[A-Z]\d{8,10}\b',  # A12345678
    ]
    
    for pattern in mrn_patterns:
        if re.search(pattern, input_str):
            violations.append('Identifier pattern detected: use SYN- prefixed IDs only')
            break
    
    # Check for name-like patterns (capitalized words that look like names)
    # Must not be common medical terms
    excluded_terms = [
        'ABO', 'RH', 'DAT', 'IAT', 'IgG', 'C3d',
        'Anti', 'Cell', 'Panel', 'Screen',
        'Positive', 'Negative', 'Patient',
        'Male', 'Female', 'Antibody', 'Antigen',
        'RBC', 'SYN'
    ]
    
    # Look for sequences of 2+ capitalized words (potential names)
    name_pattern = r'\b[A-Z][a-z]{2,}\s+[A-Z][a-z]{2,}\b'
    name_matches = re.findall(name_pattern, input_str)
    
    for match in name_matches:
        # Check if any word is in excluded medical terms
        words = match.split()
        if not any(word in excluded_terms for word in words):
            # Potential name
            violations.append('Name-like pattern detected: use synthetic identifiers only')
            break
    
    # Check for national ID patterns (country-specific)
    # Saudi ID: 1xxxxxxxxx (10 digits starting with 1 or 2)
    if re.search(r'\b[12]\d{9}\b', input_str):
        violations.append('National ID pattern detected: use synthetic data only')
    
    # Check that any IDs present start with SYN- or IH- (shipped synthetic cases)
    id_fields = ['patient_id', 'sample_id', 'unit_id']
    
    for field in id_fields:
        if field in input_data:
            value = str(input_data[field])
            if not value.startswith('SYN-'):
                violations.append(f'{field} must start with SYN- prefix')
    
    # case_id can be SYN- or IH- (shipped synthetic cases use IH- prefix)
    if 'case_id' in input_data:
        value = str(input_data['case_id'])
        if not (value.startswith('SYN-') or value.startswith('IH-')):
            violations.append(f'case_id must start with SYN- or IH- prefix')
    
    is_safe = len(violations) == 0
    
    return is_safe, violations
