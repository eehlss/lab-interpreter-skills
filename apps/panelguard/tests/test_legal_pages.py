"""
Tests for legal pages and security headers.
Research and decision-support only - not for clinical use.
"""

import pytest
from pathlib import Path
import sys
from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).parent.parent))

from app.main import app

client = TestClient(app)


def test_privacy_page_returns_200():
    """Test that /privacy returns 200 OK."""
    response = client.get("/privacy")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"


def test_terms_page_returns_200():
    """Test that /terms returns 200 OK."""
    response = client.get("/terms")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"


def test_refund_page_returns_200():
    """Test that /refund returns 200 OK."""
    response = client.get("/refund")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"


def test_privacy_contains_draft_banner():
    """Test that privacy page contains the DRAFT banner."""
    response = client.get("/privacy")
    content = response.text
    assert "DRAFT" in content
    assert "PENDING LEGAL REVIEW" in content


def test_terms_contains_draft_banner():
    """Test that terms page contains the DRAFT banner."""
    response = client.get("/terms")
    content = response.text
    assert "DRAFT" in content
    assert "PENDING LEGAL REVIEW" in content


def test_refund_contains_draft_banner():
    """Test that refund page contains the DRAFT banner."""
    response = client.get("/refund")
    content = response.text
    assert "DRAFT" in content
    assert "PENDING LEGAL REVIEW" in content


def test_privacy_contains_research_disclaimer():
    """Test that privacy page contains research use disclaimer."""
    response = client.get("/privacy")
    content = response.text
    assert "RESEARCH AND DECISION-SUPPORT ONLY" in content or "research and decision-support" in content.lower()
    assert "Not a medical device" in content or "not a medical device" in content.lower()


def test_terms_contains_research_disclaimer():
    """Test that terms page contains research use disclaimer."""
    response = client.get("/terms")
    content = response.text
    assert "RESEARCH AND DECISION-SUPPORT ONLY" in content or "research and decision-support" in content.lower()
    assert "Not a medical device" in content or "not a medical device" in content.lower()


def test_refund_contains_research_disclaimer():
    """Test that refund page contains research use disclaimer."""
    response = client.get("/refund")
    content = response.text
    assert "RESEARCH AND DECISION-SUPPORT ONLY" in content or "research and decision-support" in content.lower()
    assert "Not a medical device" in content or "not a medical device" in content.lower()


def test_security_header_hsts():
    """Test that HSTS header is present."""
    response = client.get("/")
    assert "strict-transport-security" in response.headers
    assert "max-age=31536000" in response.headers["strict-transport-security"]


def test_security_header_x_content_type_options():
    """Test that X-Content-Type-Options header is present."""
    response = client.get("/")
    assert "x-content-type-options" in response.headers
    assert response.headers["x-content-type-options"] == "nosniff"


def test_security_header_x_frame_options():
    """Test that X-Frame-Options header is present."""
    response = client.get("/")
    assert "x-frame-options" in response.headers
    assert response.headers["x-frame-options"] == "DENY"


def test_security_header_referrer_policy():
    """Test that Referrer-Policy header is present."""
    response = client.get("/")
    assert "referrer-policy" in response.headers
    assert response.headers["referrer-policy"] == "strict-origin-when-cross-origin"


def test_security_headers_on_privacy_page():
    """Test that security headers are present on privacy page."""
    response = client.get("/privacy")
    assert "strict-transport-security" in response.headers
    assert "x-content-type-options" in response.headers
    assert "x-frame-options" in response.headers
    assert "referrer-policy" in response.headers


def test_security_headers_on_terms_page():
    """Test that security headers are present on terms page."""
    response = client.get("/terms")
    assert "strict-transport-security" in response.headers
    assert "x-content-type-options" in response.headers
    assert "x-frame-options" in response.headers
    assert "referrer-policy" in response.headers


def test_security_headers_on_refund_page():
    """Test that security headers are present on refund page."""
    response = client.get("/refund")
    assert "strict-transport-security" in response.headers
    assert "x-content-type-options" in response.headers
    assert "x-frame-options" in response.headers
    assert "referrer-policy" in response.headers


def test_security_headers_on_api_health():
    """Test that security headers are present on API endpoints."""
    response = client.get("/health")
    assert "strict-transport-security" in response.headers
    assert "x-content-type-options" in response.headers
    assert "x-frame-options" in response.headers
    assert "referrer-policy" in response.headers


def test_privacy_contains_contact_placeholder():
    """Test that privacy page contains contact email placeholder."""
    response = client.get("/privacy")
    content = response.text
    assert "[CONTACT EMAIL]" in content


def test_terms_contains_contact_placeholder():
    """Test that terms page contains contact email placeholder."""
    response = client.get("/terms")
    content = response.text
    assert "[CONTACT EMAIL]" in content


def test_refund_contains_contact_placeholder():
    """Test that refund page contains contact email placeholder."""
    response = client.get("/refund")
    content = response.text
    assert "[CONTACT EMAIL]" in content


def test_terms_contains_jurisdiction_placeholder():
    """Test that terms page contains jurisdiction placeholder."""
    response = client.get("/terms")
    content = response.text
    assert "[JURISDICTION]" in content
