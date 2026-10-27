"""
Test that all 30 shipped synthetic cases pass PHI guard and analyze end-to-end.
"""

import json
import filecmp
from pathlib import Path
from fastapi.testclient import TestClient
import sys

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.main import app
from app.phi_guard import check_phi_violations

client = TestClient(app)


def get_shipped_cases():
    """Load all 30 shipped cases from repo."""
    cases_dir = Path(__file__).parent.parent.parent.parent / "cases" / "transfusion-medicine-interpreter"
    
    cases = []
    for case_dir in sorted(cases_dir.iterdir()):
        if case_dir.is_dir() and case_dir.name.startswith("IH-"):
            case_file = case_dir / "case.json"
            if case_file.exists():
                with open(case_file) as f:
                    case_data = json.load(f)
                cases.append((case_dir.name, case_data))
    
    return cases


def test_all_shipped_cases_pass_phi_guard():
    """Test that all 30 shipped cases pass PHI guard."""
    cases = get_shipped_cases()
    
    assert len(cases) == 30, f"Expected 30 cases, found {len(cases)}"
    
    for case_id, case_data in cases:
        is_safe, violations = check_phi_violations(case_data)
        
        assert is_safe, f"Case {case_id} failed PHI guard: {violations}"


def test_shipped_cases_analyze_end_to_end():
    """Test that shipped cases can be analyzed via /api/analyze endpoint."""
    cases = get_shipped_cases()
    
    # Test a sample of cases (not all 30 to keep test fast)
    sample_cases = [
        cases[0],   # IH-001 (ABO typing)
        cases[6],   # IH-007 (anti-D)
        cases[12],  # IH-013 (anti-S)
        cases[18],  # IH-019 (warm AIHA)
    ]
    
    for case_id, case_data in sample_cases:
        response = client.post("/api/analyze", json=case_data)
        
        # Should not be rejected by PHI guard
        assert response.status_code != 400 or "PHI_VIOLATION" not in response.text, \
            f"Case {case_id} rejected by PHI guard: {response.text}"
        
        # Should return successful analysis (200) or offline mode (503)
        assert response.status_code in [200, 503], \
            f"Case {case_id} failed with status {response.status_code}: {response.text}"


def test_api_cases_endpoint_lists_presets():
    """Test that /api/cases returns the 30 shipped cases."""
    response = client.get("/api/cases")
    
    assert response.status_code == 200
    
    data = response.json()
    cases = data.get("cases", [])
    
    # Should list 30 cases
    assert len(cases) >= 30, f"Expected at least 30 cases, got {len(cases)}"
    
    # Check first case
    assert any(c["id"].startswith("IH-001") for c in cases), "IH-001 not found in cases list"


def test_case_id_with_ih_prefix_passes_phi_guard():
    """Test that IH- prefixed case_id passes PHI guard."""
    test_case = {
        "case_id": "IH-001",
        "patient_id": "SYN-PAT-001",
        "date": "2099-01-15",
        "patient_abo": "A",
        "patient_rh": "Pos"
    }
    
    is_safe, violations = check_phi_violations(test_case)
    
    assert is_safe, f"IH- prefix should pass PHI guard, got violations: {violations}"


def test_case_id_with_syn_prefix_passes_phi_guard():
    """Test that SYN- prefixed case_id also passes PHI guard."""
    test_case = {
        "case_id": "SYN-CASE-001",
        "patient_id": "SYN-PAT-001",
        "date": "2099-01-15",
        "patient_abo": "A",
        "patient_rh": "Pos"
    }
    
    is_safe, violations = check_phi_violations(test_case)
    
    assert is_safe, f"SYN- prefix should pass PHI guard, got violations: {violations}"


def test_case_id_without_syn_or_ih_fails_phi_guard():
    """Test that case_id without SYN- or IH- prefix fails PHI guard."""
    test_case = {
        "case_id": "REAL-001",
        "patient_id": "SYN-PAT-001",
        "date": "2099-01-15"
    }
    
    is_safe, violations = check_phi_violations(test_case)
    
    assert not is_safe, "Non-synthetic case_id should fail PHI guard"
    assert any("case_id" in v for v in violations), "Should have case_id violation"


def test_vendored_cases_match_repo_cases():
    """Test that vendored cases/ in apps/panelguard match top-level cases/."""
    repo_cases = Path(__file__).parent.parent.parent.parent / "cases" / "transfusion-medicine-interpreter"
    vendored_cases = Path(__file__).parent.parent / "cases" / "transfusion-medicine-interpreter"
    
    # Both should exist
    assert repo_cases.exists(), f"Repo cases not found: {repo_cases}"
    assert vendored_cases.exists(), f"Vendored cases not found: {vendored_cases}"
    
    # Get all case directories
    repo_case_dirs = sorted([d.name for d in repo_cases.iterdir() if d.is_dir() and d.name.startswith("IH-")])
    vendored_case_dirs = sorted([d.name for d in vendored_cases.iterdir() if d.is_dir() and d.name.startswith("IH-")])
    
    # Should have same case directories
    assert repo_case_dirs == vendored_case_dirs, \
        f"Case directories mismatch: repo={len(repo_case_dirs)}, vendored={len(vendored_case_dirs)}"
    
    # Check each case's files are identical
    mismatches = []
    for case_dir_name in repo_case_dirs:
        repo_case_dir = repo_cases / case_dir_name
        vendored_case_dir = vendored_cases / case_dir_name
        
        for filename in ["case.json", "expected.json", "README.md"]:
            repo_file = repo_case_dir / filename
            vendored_file = vendored_case_dir / filename
            
            if repo_file.exists() and vendored_file.exists():
                if not filecmp.cmp(repo_file, vendored_file, shallow=False):
                    mismatches.append(f"{case_dir_name}/{filename}")
            elif repo_file.exists() != vendored_file.exists():
                mismatches.append(f"{case_dir_name}/{filename} (missing in one location)")
    
    assert not mismatches, \
        f"Vendored cases out of sync with repo cases. Mismatches: {mismatches}. " \
        f"Run: cp -r cases/transfusion-medicine-interpreter apps/panelguard/cases/"
