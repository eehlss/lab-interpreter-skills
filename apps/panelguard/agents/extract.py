"""
Extraction agent: parse case inputs using fast-tier model.
Research and decision-support only - not for clinical use.
"""

import json
from typing import Dict, Any
from .llm import NebiusClient


EXTRACTION_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "case_extraction",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "patient_abo": {"type": "string"},
                "patient_rh": {"type": "string"},
                "patient_age": {"type": "integer"},
                "patient_sex": {"type": "string"},
                "autocontrol": {"type": "string"},
                "panel_cells": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "cell_id": {"type": "string"},
                            "reaction": {"type": "string"},
                            "antigens": {"type": "object"},
                            "dosage": {"type": "object"}
                        },
                        "required": ["cell_id", "reaction", "antigens"],
                        "additionalProperties": False
                    }
                },
                "clinical_context": {"type": "string"}
            },
            "required": ["patient_abo", "patient_rh", "autocontrol", "panel_cells"],
            "additionalProperties": False
        }
    }
}


def extract_case_data(client: NebiusClient, case_input: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract structured data from case input using Lightning (fast tier).
    
    Args:
        client: NebiusClient instance
        case_input: Raw case input dict
    
    Returns:
        Extracted structured data or original input if extraction fails
    """
    # If already structured, return as-is
    if 'panel_cells' in case_input and isinstance(case_input['panel_cells'], list):
        return case_input
    
    # If offline, return input as-is
    if not client.is_available():
        return case_input
    
    # Build extraction prompt
    messages = [
        {
            "role": "system",
            "content": """You are an immunohaematology data extractor. Extract structured panel data from the input.
Research and decision-support only - not for clinical use.

Extract:
- patient_abo: 'O', 'A', 'B', or 'AB'
- patient_rh: 'Pos' or 'Neg'
- patient_age: integer
- patient_sex: 'male', 'female', or 'unknown'
- autocontrol: reaction grade ('0', '1+', '2+', '3+', '4+')
- panel_cells: array of cells with cell_id, reaction, antigens, dosage
- clinical_context: brief context string

Return only the JSON, no commentary."""
        },
        {
            "role": "user",
            "content": f"Extract from this case:\n\n{json.dumps(case_input, indent=2)}"
        }
    ]
    
    try:
        response = client.call(
            messages=messages,
            model_tier='fast',
            response_format=EXTRACTION_SCHEMA,
            temperature=0.1
        )
        
        if response['offline']:
            return case_input
        
        extracted = json.loads(response['content'])
        return extracted
    
    except Exception as e:
        print(f"Extraction failed: {e}")
        return case_input
