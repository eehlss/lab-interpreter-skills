"""
Explanation agent: generate natural language explanations using mid-tier model.
Research and decision-support only - not for clinical use.
"""

import json
from typing import Dict, Any
from .llm import NebiusClient


EXPLANATION_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "panel_explanation",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string"},
                "antibody_identification": {"type": "string"},
                "rule_out_explanation": {"type": "string"},
                "unit_selection_rationale": {"type": "string"},
                "safety_notes": {"type": "string"},
                "disclaimer": {"type": "string"}
            },
            "required": [
                "summary",
                "antibody_identification",
                "rule_out_explanation",
                "unit_selection_rationale",
                "safety_notes",
                "disclaimer"
            ],
            "additionalProperties": False
        }
    }
}


def generate_explanation(
    client: NebiusClient,
    engine_result: Dict[str, Any],
    case_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Generate natural language explanation using Super VL (mid tier).
    
    Args:
        client: NebiusClient instance
        engine_result: Results from deterministic engine
        case_data: Original case data
    
    Returns:
        Explanation dict with narrative sections
    """
    if not client.is_available():
        # Offline fallback
        return {
            'summary': 'Offline mode: rules-only analysis available.',
            'antibody_identification': json.dumps(engine_result.get('panel_analysis', {})),
            'rule_out_explanation': f"Ruled out: {', '.join(engine_result.get('panel_analysis', {}).get('ruled_out', []))}",
            'unit_selection_rationale': json.dumps(engine_result.get('units', {})),
            'safety_notes': ', '.join(engine_result.get('flags', [])),
            'disclaimer': 'Research and decision-support only - not for clinical use. All results require review by a qualified professional.'
        }
    
    # Build explanation prompt
    messages = [
        {
            "role": "system",
            "content": """You are an immunohaematology expert explaining antibody panel results.

CRITICAL RULES:
1. You MUST explain the deterministic engine results provided. Never contradict them.
2. You MUST include the exact antibody specificities from the engine's candidates list.
3. You MUST recommend only the units the engine marked as compatible.
4. Always include: "Research and decision-support only - not for clinical use."

Your job is to EXPLAIN what the engine decided, not to make your own decisions."""
        },
        {
            "role": "user",
            "content": f"""Explain this antibody panel analysis.

ENGINE RESULTS (source of truth):
{json.dumps(engine_result, indent=2)}

CASE DATA:
{json.dumps(case_data, indent=2)}

Provide:
- summary: 2-3 sentence overview
- antibody_identification: which antibody(ies), how identified
- rule_out_explanation: how rule-out worked (homozygous cells, 3+/3- rule)
- unit_selection_rationale: why these units are compatible
- safety_notes: any flags or special considerations
- disclaimer: include "Research and decision-support only - not for clinical use."

Return structured JSON."""
        }
    ]
    
    try:
        response = client.call(
            messages=messages,
            model_tier='mid',
            response_format=EXPLANATION_SCHEMA,
            temperature=0.3
        )
        
        if response['offline']:
            return generate_explanation(client, engine_result, case_data)  # recursion triggers offline fallback above
        
        explanation = json.loads(response['content'])
        return explanation
    
    except Exception as e:
        print(f"Explanation generation failed: {e}")
        # Fallback
        return {
            'summary': f'Analysis complete. Error in explanation generation: {str(e)}',
            'antibody_identification': json.dumps(engine_result.get('panel_analysis', {})),
            'rule_out_explanation': f"Ruled out: {', '.join(engine_result.get('panel_analysis', {}).get('ruled_out', []))}",
            'unit_selection_rationale': json.dumps(engine_result.get('units', {})),
            'safety_notes': ', '.join(engine_result.get('flags', [])),
            'disclaimer': 'Research and decision-support only - not for clinical use.'
        }
