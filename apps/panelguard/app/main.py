"""
PanelGuard FastAPI application.
Research and decision-support only - not for clinical use.
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Import engines and agents
import sys
sys.path.append(str(Path(__file__).parent.parent))

from engine import ABOEngine, PanelEngine, UnitsEngine, DATEngine
from agents import NebiusClient, extract_case_data, generate_explanation, reason_complex_case, verify_llm_output, lookup_antibody_evidence
from app.phi_guard import check_phi_violations

# Initialize FastAPI
app = FastAPI(
    title="PanelGuard",
    description="Blood Bank Copilot - Research and decision-support only",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize engines
abo_engine = ABOEngine()
panel_engine = PanelEngine()
units_engine = UnitsEngine()
dat_engine = DATEngine()

# Initialize LLM client
llm_client = NebiusClient()

# Rate limiting (simple in-memory)
request_counts = {}
LIVE_DAILY_CAP = int(os.getenv('LIVE_DAILY_CAP', '40'))


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "llm_available": llm_client.is_available(),
        "models": {
            "fast": llm_client.model_fast,
            "mid": llm_client.model_mid,
            "reason": llm_client.model_reason
        },
        "disclaimer": "Research and decision-support only - not for clinical use"
    }


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve main UI."""
    ui_path = Path(__file__).parent.parent / "ui" / "index.html"
    if ui_path.exists():
        return ui_path.read_text()
    return "<h1>PanelGuard</h1><p>UI not found</p>"


@app.get("/api/cases")
async def list_cases():
    """List available preset cases."""
    # Try /app/cases (Docker) first, then fall back to repo structure
    cases_dir = Path("/app/cases/transfusion-medicine-interpreter")
    if not cases_dir.exists():
        cases_dir = Path(__file__).parent.parent.parent.parent / "cases" / "transfusion-medicine-interpreter"
    
    if not cases_dir.exists():
        return {"cases": []}
    
    cases = []
    for case_dir in sorted(cases_dir.iterdir()):
        if case_dir.is_dir() and case_dir.name.startswith("IH-"):
            case_file = case_dir / "case.json"
            if case_file.exists():
                cases.append({
                    "id": case_dir.name,
                    "name": case_dir.name.replace("-", " ").title()
                })
    
    return {"cases": cases}


@app.post("/api/analyze")
async def analyze_case(request: Request):
    """
    Analyze an antibody panel case.
    
    Flow:
    1. PHI guard
    2. Extract data (fast tier)
    3. Engine analysis (deterministic)
    4. Route to explanation (mid tier) or reasoning (Ultra)
    5. Verify LLM output
    6. Optional Tavily lookup
    7. Return combined result
    """
    try:
        case_input = await request.json()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON: {str(e)}")
    
    # PHI guard
    is_safe, violations = check_phi_violations(case_input)
    if not is_safe:
        return JSONResponse(
            status_code=403,
            content={
                "error": "PHI_VIOLATION",
                "message": "Input appears to contain real patient data",
                "violations": violations,
                "disclaimer": "Only synthetic data (SYN- IDs, year 2099 dates) is permitted"
            }
        )
    
    # Rate limiting (basic)
    client_ip = request.client.host
    today = str(Path(__file__).stat().st_mtime)[:10]  # Simple day key
    rate_key = f"{client_ip}:{today}"
    
    if rate_key not in request_counts:
        request_counts[rate_key] = 0
    
    if request_counts[rate_key] >= LIVE_DAILY_CAP:
        return JSONResponse(
            status_code=429,
            content={
                "error": "RATE_LIMIT",
                "message": f"Daily cap of {LIVE_DAILY_CAP} requests reached. Rules-only analysis available.",
                "disclaimer": "Research and decision-support only - not for clinical use"
            }
        )
    
    request_counts[rate_key] += 1
    
    # Extract data
    case_data = extract_case_data(llm_client, case_input)
    
    # Run deterministic engines
    result = {
        "disclaimer": "Research and decision-support only - not for clinical use. All results require review by a qualified professional.",
        "case_id": case_data.get('case_id', 'unknown'),
        "flags": []
    }
    
    # ABO typing if available
    if 'forward_typing' in case_data and 'reverse_typing' in case_data:
        blood_type, flags = abo_engine.check_forward_reverse_typing(
            case_data['forward_typing'],
            case_data['reverse_typing']
        )
        result['blood_type'] = blood_type
        result['abo_flags'] = flags
        result['flags'].extend(flags)
    
    # Panel analysis
    if 'panel_cells' in case_data:
        panel_result = panel_engine.analyze_panel(
            case_data['panel_cells'],
            case_data.get('autocontrol', '0')
        )
        result['panel_analysis'] = panel_result
        result['flags'].extend(panel_result.get('flags', []))
        
        # Unit selection
        if panel_result['status'] == 'ok' and panel_result['candidates']:
            units_result = units_engine.select_compatible_units(
                patient_abo=case_data.get('patient_abo', 'O'),
                patient_rh=case_data.get('patient_rh', 'Pos'),
                antibody_specificities=panel_result['candidates'],
                patient_sex=case_data.get('patient_sex', 'unknown'),
                patient_age=case_data.get('patient_age', 99),
                special_requirements=case_data.get('special_requirements', []),
                product_type='rbc',
                max_units=5
            )
            result['units'] = units_result
            result['flags'].extend(units_result.get('flags', []))
    
    # DAT if available
    if 'dat_polyspecific' in case_data:
        dat_result = dat_engine.interpret_dat(
            polyspecific=case_data['dat_polyspecific'],
            monospecific_igg=case_data.get('dat_monospecific_igg'),
            monospecific_c3d=case_data.get('dat_monospecific_c3d'),
            clinical_context=case_data.get('clinical_context')
        )
        result['dat'] = dat_result
        if dat_result['positive']:
            result['flags'].extend(dat_result.get('flags', []))
    
    # Determine complexity
    is_complex = False
    if 'panel_analysis' in result:
        is_complex = panel_engine.is_complex_case(
            autocontrol=case_data.get('autocontrol', '0'),
            num_candidates=len(result['panel_analysis'].get('candidates', [])),
            positive_cells=result['panel_analysis'].get('positive_cells', 0),
            negative_cells=result['panel_analysis'].get('negative_cells', 0),
            dat_positive=result.get('dat', {}).get('positive', False),
            special_population='sickle_cell' in case_data.get('special_requirements', [])
        )
    
    # LLM layer
    if llm_client.is_available():
        if is_complex:
            # Use Ultra for reasoning
            llm_output = reason_complex_case(llm_client, result, case_data)
            result['reasoning'] = llm_output
            result['model_tier'] = 'Ultra'
        else:
            # Use mid tier for explanation
            llm_output = generate_explanation(llm_client, result, case_data)
            result['explanation'] = llm_output
            result['model_tier'] = 'mid'
        
        # Verify LLM output
        verification = verify_llm_output(llm_client, llm_output, result)
        result['verified'] = verification['verified']
        
        if not verification['verified']:
            result['narrative_blocked'] = True
            result['violations'] = verification['violations']
            result['safe_output'] = verification['safe_narrative']
    else:
        result['model_tier'] = 'offline'
        result['message'] = 'Rules-only analysis (LLM unavailable)'
    
    # Tavily evidence lookup
    if result.get('panel_analysis', {}).get('candidates'):
        evidence = {}
        for antibody in result['panel_analysis']['candidates']:
            evidence[antibody] = lookup_antibody_evidence(antibody)
        result['evidence'] = evidence
    
    return result


@app.post("/api/signoff")
async def signoff(request: Request):
    """
    Record reviewer sign-off.
    
    In production, this would log the sign-off.
    For the demo, it just acknowledges.
    """
    try:
        data = await request.json()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON: {str(e)}")
    
    case_id = data.get('case_id')
    reviewer_initials = data.get('reviewer_initials')
    
    if not case_id or not reviewer_initials:
        raise HTTPException(status_code=400, detail="case_id and reviewer_initials required")
    
    # In production: log to audit trail
    # For demo: acknowledge only
    
    return {
        "status": "acknowledged",
        "case_id": case_id,
        "reviewer": reviewer_initials,
        "message": "Sign-off recorded (demo mode - no units released)",
        "disclaimer": "Research and decision-support only - not for clinical use"
    }


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port)
