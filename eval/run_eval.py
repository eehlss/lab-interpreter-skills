#!/usr/bin/env python3
"""
PanelGuard evaluation harness.
Research and decision-support only - not for clinical use.
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any

# Add parent to path
sys.path.append(str(Path(__file__).parent.parent / "apps" / "panelguard"))

from engine import ABOEngine, PanelEngine, UnitsEngine, DATEngine


def load_cases(cases_dir: Path) -> List[Dict[str, Any]]:
    """Load all IH cases from directory."""
    cases = []
    
    if not cases_dir.exists():
        print(f"Cases directory not found: {cases_dir}")
        return cases
    
    for case_dir in sorted(cases_dir.iterdir()):
        if case_dir.is_dir() and case_dir.name.startswith("IH-"):
            case_file = case_dir / "case.json"
            expected_file = case_dir / "expected.json"
            
            if case_file.exists():
                with open(case_file) as f:
                    case_data = json.load(f)
                
                expected = {}
                if expected_file.exists():
                    with open(expected_file) as f:
                        expected = json.load(f)
                
                cases.append({
                    "case_id": case_dir.name,
                    "case_data": case_data,
                    "expected": expected
                })
    
    return cases


def run_engine_analysis(case_data: Dict[str, Any]) -> Dict[str, Any]:
    """Run deterministic engine on a case."""
    abo_engine = ABOEngine()
    panel_engine = PanelEngine()
    units_engine = UnitsEngine()
    dat_engine = DATEngine()
    
    result = {
        "case_id": case_data.get("case_id", "unknown"),
        "flags": []
    }
    
    # ABO typing
    if "forward_typing" in case_data and "reverse_typing" in case_data:
        blood_type, flags = abo_engine.check_forward_reverse_typing(
            case_data["forward_typing"],
            case_data["reverse_typing"]
        )
        result["blood_type"] = blood_type
        result["abo_flags"] = flags
    
    # Panel analysis
    if "panel_cells" in case_data:
        panel_result = panel_engine.analyze_panel(
            case_data["panel_cells"],
            case_data.get("autocontrol", "0")
        )
        result["panel_analysis"] = panel_result
        
        # Unit selection
        if panel_result["status"] == "ok" and panel_result["candidates"]:
            units_result = units_engine.select_compatible_units(
                patient_abo=case_data.get("patient_abo", "O"),
                patient_rh=case_data.get("patient_rh", "Pos"),
                antibody_specificities=panel_result["candidates"],
                patient_sex=case_data.get("patient_sex", "unknown"),
                patient_age=case_data.get("patient_age", 99),
                special_requirements=case_data.get("special_requirements", []),
                product_type="rbc",
                max_units=5
            )
            result["units"] = units_result
    
    # DAT if available
    if "dat_polyspecific" in case_data:
        dat_result = dat_engine.interpret_dat(
            polyspecific=case_data["dat_polyspecific"],
            monospecific_igg=case_data.get("dat_monospecific_igg"),
            monospecific_c3d=case_data.get("dat_monospecific_c3d"),
            clinical_context=case_data.get("clinical_context")
        )
        result["dat"] = dat_result
    
    return result


def check_safety(result: Dict[str, Any], expected: Dict[str, Any]) -> Dict[str, Any]:
    """Check for unsafe recommendations (critical gate)."""
    safety = {
        "safe": True,
        "violations": []
    }
    
    # Check for ABO-incompatible units
    if "units" in result and "compatible_units" in result["units"]:
        patient_abo = result.get("patient_abo", expected.get("patient_abo", "O"))
        
        for unit in result["units"]["compatible_units"]:
            unit_abo = unit.get("abo", "")
            # Simple check: O patients should only get O
            if patient_abo == "O" and unit_abo != "O":
                safety["safe"] = False
                safety["violations"].append(f"ABO-incompatible unit: {unit['unit_id']} ({unit_abo}) for O patient")
    
    # Check for antigen-positive units when antibody present
    if "panel_analysis" in result and "candidates" in result["panel_analysis"]:
        antibodies = result["panel_analysis"]["candidates"]
        
        if "units" in result and "compatible_units" in result["units"]:
            for unit in result["units"]["compatible_units"]:
                phenotype = unit.get("phenotype", {})
                for antibody in antibodies:
                    if phenotype.get(antibody, "0") in ["+", "1", "pos", "positive"]:
                        safety["safe"] = False
                        safety["violations"].append(
                            f"Unit {unit['unit_id']} is {antibody}-positive but patient has anti-{antibody}"
                        )
    
    return safety


def evaluate_case(case: Dict[str, Any]) -> Dict[str, Any]:
    """Evaluate a single case."""
    case_data = case["case_data"]
    expected = case["expected"]
    
    # Run engine
    result = run_engine_analysis(case_data)
    
    # Check safety (critical)
    safety = check_safety(result, expected)
    
    # Check correctness vs expected
    correctness = {
        "panel_status_match": True,
        "antibody_match": True,
        "refer_match": True
    }
    
    if "expected_panel_status" in expected:
        actual_status = result.get("panel_analysis", {}).get("status", "")
        expected_status = expected["expected_panel_status"]
        correctness["panel_status_match"] = actual_status == expected_status
    
    if "expected_antibodies" in expected:
        actual_abs = set(result.get("panel_analysis", {}).get("candidates", []))
        expected_abs = set(expected["expected_antibodies"])
        correctness["antibody_match"] = actual_abs == expected_abs
    
    return {
        "case_id": case["case_id"],
        "safety": safety,
        "correctness": correctness,
        "result": result
    }


def main():
    parser = argparse.ArgumentParser(description="Run PanelGuard evaluation")
    parser.add_argument("--cases", type=Path, required=True, help="Path to cases directory")
    parser.add_argument("--runs", type=int, default=1, help="Number of runs per case")
    parser.add_argument("--out", type=Path, help="Output results file")
    
    args = parser.parse_args()
    
    # Load cases
    cases = load_cases(args.cases)
    
    if not cases:
        print("No cases found!")
        return 1
    
    print(f"Loaded {len(cases)} cases")
    
    # Run evaluation
    all_results = []
    
    for run in range(args.runs):
        print(f"\n=== Run {run + 1}/{args.runs} ===")
        
        for case in cases:
            print(f"Evaluating {case['case_id']}...", end=" ")
            
            eval_result = evaluate_case(case)
            all_results.append(eval_result)
            
            if not eval_result["safety"]["safe"]:
                print(f"❌ UNSAFE: {eval_result['safety']['violations']}")
            else:
                print("✓")
    
    # Aggregate results
    total_evals = len(all_results)
    unsafe_count = sum(1 for r in all_results if not r["safety"]["safe"])
    panel_status_correct = sum(1 for r in all_results if r["correctness"]["panel_status_match"])
    antibody_correct = sum(1 for r in all_results if r["correctness"]["antibody_match"])
    
    # Summary
    print("\n" + "=" * 60)
    print("EVALUATION SUMMARY")
    print("=" * 60)
    print(f"Total evaluations: {total_evals}")
    print(f"Unsafe recommendations: {unsafe_count} (GATE: must be 0)")
    print(f"Panel status accuracy: {panel_status_correct}/{total_evals} ({100*panel_status_correct/total_evals:.1f}%)")
    print(f"Antibody ID accuracy: {antibody_correct}/{total_evals} ({100*antibody_correct/total_evals:.1f}%)")
    
    # Gate checks
    gates_pass = True
    
    if unsafe_count > 0:
        print("\n❌ CRITICAL: Unsafe recommendations detected - NO GO")
        gates_pass = False
    else:
        print("\n✅ GATE PASS: No unsafe recommendations")
    
    if panel_status_correct == total_evals:
        print("✅ GATE PASS: All panel status checks correct")
    else:
        print(f"⚠️  Panel status: {total_evals - panel_status_correct} mismatches")
    
    # Write results
    if args.out:
        with open(args.out, "w") as f:
            f.write("# PanelGuard Evaluation Results\n\n")
            f.write(f"**Date:** {Path(__file__).stat().st_mtime}\n\n")
            f.write(f"**Cases:** {len(cases)}\n\n")
            f.write(f"**Runs:** {args.runs}\n\n")
            f.write("## Results\n\n")
            f.write(f"- Total evaluations: {total_evals}\n")
            f.write(f"- Unsafe recommendations: **{unsafe_count}** (GATE: must be 0)\n")
            f.write(f"- Panel status accuracy: {panel_status_correct}/{total_evals} ({100*panel_status_correct/total_evals:.1f}%)\n")
            f.write(f"- Antibody ID accuracy: {antibody_correct}/{total_evals} ({100*antibody_correct/total_evals:.1f}%)\n")
            f.write(f"\n**Gates:** {'PASS ✅' if gates_pass else 'FAIL ❌'}\n")
        
        print(f"\nResults written to {args.out}")
    
    return 0 if gates_pass else 1


if __name__ == "__main__":
    sys.exit(main())
