"""
Reasoning agent: handle complex cases using Ultra model.
Research and decision-support only - not for clinical use.
"""

import json
from typing import Dict, Any
from .llm import NebiusClient


REASONING_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "complex_reasoning",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "complexity_assessment": {"type": "string"},
                "detailed_analysis": {"type": "string"},
                "next_steps": {"type": "string"},
                "differential_diagnosis": {"type": "string"},
                "clinical_significance": {"type": "string"},
                "disclaimer": {"type": "string"}
            },
            "required": [
                "complexity_assessment",
                "detailed_analysis",
                "next_steps",
                "clinical_significance",
                "disclaimer"
            ],
            "additionalProperties": False
        }
    }
}


def reason_complex_case(
    client: NebiusClient,
    engine_result: Dict[str, Any],
    case_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Apply deep reasoning to complex cases using Nemotron Ultra.
    
    Complex cases include:
    - Positive autocontrol
    - Multiple antibody candidates
    - Insufficient cells
    - Positive DAT
    - Special populations
    
    Args:
        client: NebiusClient instance
        engine_result: Results from deterministic engine
        case_data: Original case data
    
    Returns:
        Reasoning dict with detailed analysis
    """
    if not client.is_available():
        # Offline fallback
        return {
            'complexity_assessment': 'Complex case - offline mode active',
            'detailed_analysis': json.dumps(engine_result),
            'next_steps': 'Review engine results. LLM reasoning unavailable in offline mode.',
            'differential_diagnosis': 'N/A - offline',
            'clinical_significance': 'Refer to reference laboratory for complex case review.',
            'disclaimer': 'Research and decision-support only - not for clinical use.'
        }
    
    # Build reasoning prompt
    messages = [
        {
            "role": "system",
            "content": """You are a senior transfusion medicine specialist analyzing a complex antibody case.

CRITICAL RULES:
1. The deterministic engine's results are the SOURCE OF TRUTH. Never contradict them.
2. You provide deep reasoning ABOUT the engine's findings, you do not override them.
3. Explain WHY the case is complex and what additional testing might help.
4. Always include: "Research and decision-support only - not for clinical use."

Your role: explain complexity, suggest next steps, discuss differential diagnosis."""
        },
        {
            "role": "user",
            "content": f"""Analyze this complex antibody panel case.

ENGINE RESULTS (source of truth):
{json.dumps(engine_result, indent=2)}

CASE DATA:
{json.dumps(case_data, indent=2)}

Provide:
- complexity_assessment: why this case is complex
- detailed_analysis: deep reasoning about the findings
- next_steps: what additional testing or consultation is needed
- differential_diagnosis: if multiple antibodies, discuss differentiation
- clinical_significance: transfusion implications
- disclaimer: "Research and decision-support only - not for clinical use."

Return structured JSON."""
        }
    ]
    
    try:
        response = client.call(
            messages=messages,
            model_tier='reason',
            response_format=REASONING_SCHEMA,
            temperature=0.4
        )
        
        if response['offline']:
            return reason_complex_case(client, engine_result, case_data)  # trigger offline fallback
        
        reasoning = json.loads(response['content'])
        return reasoning
    
    except Exception as e:
        print(f"Reasoning failed: {e}")
        return {
            'complexity_assessment': f'Complex case. Reasoning error: {str(e)}',
            'detailed_analysis': json.dumps(engine_result),
            'next_steps': 'Refer to reference laboratory.',
            'differential_diagnosis': 'N/A',
            'clinical_significance': 'Unable to assess - refer to specialist.',
            'disclaimer': 'Research and decision-support only - not for clinical use.'
        }
