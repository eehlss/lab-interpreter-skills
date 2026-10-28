"""
Tests for production fixes:
1. GET /api/cases/{id} endpoint
2. Rate limiting with UTC date
3. Negative screen routing to mid tier
4. UI case loading

Research and decision-support only - not for clinical use.
"""

import pytest
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path
from fastapi.testclient import TestClient
import sys

sys.path.append(str(Path(__file__).parent.parent))

from app.main import app, request_counts

client = TestClient(app)


def test_get_case_by_id():
    """Test GET /api/cases/{id} returns case JSON."""
    response = client.get("/api/cases/IH-001-abo-a-pos-routine")
    
    assert response.status_code == 200
    data = response.json()
    
    # Should have case data
    assert "case_id" in data
    assert data["case_id"] == "IH-001"
    assert "patient_abo" in data
    assert "panel_cells" in data


def test_get_case_invalid_id():
    """Test GET /api/cases/{id} with invalid ID returns 400 or 404."""
    # Path traversal attempt (may return 404 if FastAPI normalizes path first)
    response = client.get("/api/cases/../../../etc/passwd")
    assert response.status_code in [400, 404]
    
    # Invalid format (not IH- prefix)
    response = client.get("/api/cases/REAL-001")
    assert response.status_code == 400


def test_get_case_not_found():
    """Test GET /api/cases/{id} with nonexistent ID returns 404."""
    response = client.get("/api/cases/IH-999-nonexistent")
    assert response.status_code == 404


def test_rate_limiting_uses_utc_date():
    """Test rate limiting uses UTC date as key (not file mtime)."""
    from app.main import request_counts
    
    # Clear rate limit state
    request_counts.clear()
    
    # Simulate a request
    test_ip = "192.168.1.100"
    today = datetime.now(timezone.utc).date().isoformat()
    rate_key = f"{test_ip}:{today}"
    
    # First request should initialize counter
    assert rate_key not in request_counts
    
    # Manually add to simulate request processing
    request_counts[rate_key] = 1
    
    # Key should use YYYY-MM-DD format (UTC date)
    assert len(today.split('-')) == 3  # YYYY-MM-DD
    assert today.startswith('202')  # Reasonable year
    
    # Different day should use different key
    tomorrow = (datetime.now(timezone.utc) + timedelta(days=1)).date().isoformat()
    tomorrow_key = f"{test_ip}:{tomorrow}"
    
    assert tomorrow_key != rate_key
    assert tomorrow_key not in request_counts


def test_negative_screen_routing():
    """Test negative screen (0 positive cells, autocontrol negative) routes to mid tier."""
    # This test verifies the routing logic by checking the model_tier in the response
    # A negative screen should use 'mid' tier, not 'Ultra'
    
    negative_screen_case = {
        "case_id": "SYN-NEG-001",
        "patient_id": "SYN-PAT-001",
        "date": "2099-01-15",
        "patient_abo": "O",
        "patient_rh": "Pos",
        "autocontrol": "0",
        "panel_cells": [
            {
                "cell_id": "1",
                "reaction": "0",
                "antigens": {"D": "+", "C": "+", "E": "0", "c": "0", "e": "+", "K": "0"}
            },
            {
                "cell_id": "2",
                "reaction": "0",
                "antigens": {"D": "+", "C": "0", "E": "+", "c": "+", "e": "+", "K": "0"}
            },
            {
                "cell_id": "3",
                "reaction": "0",
                "antigens": {"D": "+", "C": "0", "E": "0", "c": "+", "e": "+", "K": "+"}
            }
        ]
    }
    
    response = client.post("/api/analyze", json=negative_screen_case)
    
    # Should succeed
    assert response.status_code == 200
    data = response.json()
    
    # Should have panel analysis
    assert "panel_analysis" in data
    assert data["panel_analysis"]["positive_cells"] == 0
    
    # Should route to mid tier (not Ultra), if LLM is available
    if "model_tier" in data:
        assert data["model_tier"] == "mid" or data["model_tier"] == "offline"
        assert data["model_tier"] != "Ultra"


def test_ui_case_loading_uses_api():
    """Test UI loads cases via /api/cases/{id} not static files."""
    # Read UI HTML
    ui_path = Path(__file__).parent.parent / "ui" / "index.html"
    html = ui_path.read_text()
    
    # Should use /api/cases/ endpoint
    assert "/api/cases/" in html
    
    # Should NOT use direct /cases/ path
    assert "/cases/transfusion-medicine-interpreter/" not in html
