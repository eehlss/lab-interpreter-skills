# Security policy

**Research and decision-support only. Not a medical device. Not for clinical use.**
All outputs require review by a qualified professional.

## Supported versions

| Component | Supported |
|---|---|
| `main` branch (PanelGuard in `apps/panelguard`, interpreter skills) | Yes |
| Older branches, tags and forks | No |

## Reporting a vulnerability

Please **do not** open a public issue for security problems.

- Use GitHub private vulnerability reporting: **Security → Report a vulnerability** on this repository, or
- email the maintainer at the address on the GitHub profile with subject `SECURITY: lab-interpreter-skills`.

Include the affected path/endpoint, steps to reproduce and impact. **Never include real patient data** in a report;
use synthetic values (`SYN-...`).

Target response: acknowledgement within 5 working days, triage within 10 working days,
fix or mitigation for high/critical issues within 30 days.

## Data handling rules

- This repository must contain **synthetic data only**. Real printouts, reports, names, MRNs, dates of birth,
  national ID / iqama / NIN numbers or phone numbers must never be committed (`validation-real/` is git-ignored).
- PHI and secret scanning runs in CI and in the pre-commit hook (`gitleaks` with `.gitleaks.toml`, which extends the
  default secret rules with PHI identifier rules).
- API keys (LLM / search providers) are supplied only via environment variables or the cloud secret manager,
  never in code, notebooks, Dockerfiles or CI logs.

## Secure development baseline

- Branch protection on `main` with pull-request review and required status checks.
- GitHub Actions pinned to full commit SHAs; workflow token is `contents: read` by default.
- Dependabot for pip, Docker and GitHub Actions updates.
- CI security job: gitleaks (secrets + PHI), pip-audit (OSV), bandit (SAST) and a CycloneDX SBOM, kept as
  build artifacts for 90 days as audit evidence.
- Container runs as a non-root user (UID 10001).
- Threat model: [`apps/panelguard/docs/threat-model.md`](apps/panelguard/docs/threat-model.md).

## Local setup

```bash
pip install pre-commit
pre-commit install          # runs gitleaks, large-file and private-key checks before each commit
pre-commit run --all-files
```
