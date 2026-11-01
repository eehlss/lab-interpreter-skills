# PanelGuard threat model (STRIDE, lightweight)

**Status:** draft v0.1, 1 Nov 2026 (Asia/Riyadh). Owner: Dr. Emeka Patrick Chukwuka. Review: every release or every 6 months.
**Classification of system:** research and decision-support prototype. Not a medical device; not for clinical use.

## 1. System summary

| Item | Value |
|---|---|
| Purpose | Blood-bank / immunohaematology case interpretation copilot with evidence retrieval and sign-off |
| Code | `apps/panelguard` (FastAPI, Python 3.11) |
| Hosting | Google Cloud Run (`panelguard`, us-central1) for demo; local Docker for development |
| Data in | Synthetic cases (`cases/`, `SYN-*` IDs); user-entered case text via `/api/analyze` |
| External calls | LLM provider (OpenAI-compatible endpoint), Tavily search |
| Secrets | LLM / Tavily API keys via environment / Secret Manager |
| Users | Demonstration users; no accounts, no patient records stored |

## 2. Data flow

```
Browser ──HTTPS──▶ Cloud Run (FastAPI: /api/cases, /api/analyze, /api/signoff)
                     ├──▶ LLM API (case text, prompt)         [external processor]
                     └──▶ Tavily search (query terms)          [external processor]
```

Trust boundaries: (1) internet → Cloud Run; (2) Cloud Run → third-party AI/search APIs.

## 3. Assets

1. API keys (LLM, Tavily) - confidentiality, cost.
2. Any text a user pastes into `/api/analyze` - may contain PHI if users ignore guidance.
3. Integrity of interpretations and sign-off records (patient-safety relevance if misused clinically).
4. Availability and cloud spend (free-tier budget).

## 4. Threats and controls

| STRIDE | Threat | Current control | Gap / planned control |
|---|---|---|---|
| S | Anyone can call the API (no auth) | Demo scope, synthetic data | Cloud Run IAM invoker or IAP for non-demo use (approval needed) |
| T | Prompt injection alters interpretation | Deterministic engine + verifier, disclaimer | Keep rule engine authoritative; log model version |
| R | Sign-off not attributable | `/api/signoff` stores reviewer field | Add authenticated identity before any real use |
| I | User pastes real PHI, sent to LLM/search | Disclaimer; synthetic-only policy | **Server-side PHI route guard** (block MRN/DOB/ID/phone shapes before external calls) - proposal |
| I | Secrets leak via repo or logs | `.gitleaks.toml` (default + PHI rules), CI + pre-commit scan | Secret Manager, rotation register |
| D | Cost/DoS via large or repeated requests | Cloud Run max instances | Request size cap + rate limit; `max-instances` 1-2; budget alert - proposal |
| E | Container escape / privilege | Non-root UID 10001 (this change) | Read-only FS on Cloud Run gen2 where possible |
| - | Cross-site use of API | `allow_origins=["*"]` | Restrict CORS to the Cloud Run URL - proposal (needs redeploy approval) |
| - | Vulnerable dependencies | Dependabot, pip-audit in CI | Upgrade starlette/fastapi and python-multipart (known OSV advisories on 1 Nov 2026) |

## 5. Residual risk and conditions of use

Acceptable **only** for synthetic demonstration data. Any use with real patient data requires: DPIA, authentication,
PHI route guard, data processing agreements with AI providers, and a recorded risk acceptance.
