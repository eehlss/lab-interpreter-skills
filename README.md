> **Research Purpose Only.** This material is a research and decision-support resource. It is not a validated or approved medical device, and its output must not be the sole basis for any clinical decision; all results require review by a qualified professional.

# Lab Interpreter Skills + PanelGuard

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![CI](https://github.com/eehlss/lab-interpreter-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/eehlss/lab-interpreter-skills/actions/workflows/ci.yml)

Medical laboratory interpretation skills for Claude AI, plus **PanelGuard**: a blood bank copilot built for the [Nebius x NVIDIA Global AI Hackathon](https://nebius-nvidia-ai-hackathon.devpost.com/).

---

## 🩸 PanelGuard: Blood Bank Copilot

**Track:** Best Apps and Agents | **Demo:** https://panelguard-250296213348.us-central1.run.app | **Video:** TBD | **Devpost:** TBD

PanelGuard turns antibody panel workups into reviewed, explained recommendations in under a minute. **Deterministic blood-bank rules make every safety decision.** NVIDIA Nemotron models on Nebius Token Factory read inputs, reason about hard cases, and explain every step.

### Quick Start

**macOS / Linux:**

```bash
git clone https://github.com/eehlss/lab-interpreter-skills.git
cd lab-interpreter-skills
python3 -m venv .venv && source .venv/bin/activate
pip install -r apps/panelguard/requirements.txt
export NEBIUS_API_KEY=<your-key>
export TAVILY_API_KEY=<your-key>
pytest apps/panelguard/tests/ -v
uvicorn app.main:app --app-dir apps/panelguard --host 0.0.0.0 --port 8080
```

**Windows (cmd - single-line commands):**

```cmd
git clone https://github.com/eehlss/lab-interpreter-skills.git && cd lab-interpreter-skills
python -m venv .venv && call .venv\Scripts\activate.bat && pip install -r apps\panelguard\requirements.txt
set NEBIUS_API_KEY=<your-key>
set TAVILY_API_KEY=<your-key>
pytest apps\panelguard\tests\ -v
python -m uvicorn app.main:app --app-dir apps\panelguard --host 127.0.0.1 --port 8080
```

See [full setup documentation](#panelguard-setup) below.

### What Was Added During Hackathon (26 Aug – 30 Oct 2026)

Repository created April 2026 with Claude skills only. Added during submission period:

1. **PanelGuard app** with deterministic engine (ABO, panel, units) + NVIDIA Nemotron integration
2. Tiered routing: Lightning (extract), Super VL (explain), Ultra (complex reasoning)
3. Verifier blocking LLM contradictions, PHI guard, rate caps, human sign-off
4. Synthetic cases, pytest suite, eval harness, GitHub Actions CI
5. MIT LICENSE and Cloud Run deployment config

See [detailed summary](#what-was-significantly-updated) below.

---

## Claude AI Skills (Pre-Hackathon Content)

| Skill | Focus | Interprets |
|-------|-------|------------|
| `sysmex-xn-cbc-interpreter-skill/` | Hematology CBC | Sysmex XN printouts, flags, scattergrams |
| `hb-interpreter-skill/` | Hemoglobinopathy | Bio-Rad HPLC, Sebia CZE |
| `chemistry-hormone-interpreter-skill/` | Chemistry + endocrine | Renal, liver, metabolic, thyroid, adrenal panels |
| `immunohaematology-interpreter-skill/` | Transfusion medicine | Antibody panels, DAT, ABO/Rh, crossmatch |

**Install for Claude Code:**

```bash
mkdir -p .claude/skills
cp -R *-interpreter-skill .claude/skills/
```

---

<a name="panelguard-setup"></a>
## PanelGuard: Full Setup & Architecture

### How We Use NVIDIA Nemotron on Nebius Token Factory

| Model | Role | Cost/1M (in/out) |
|-------|------|------------------|
| `nvidia/Nemotron-3_5-Lightning` | Extraction, verifier | $0.06 / $0.24 |
| `nvidia/Nemotron-3.5-Super-VL` | Explanations | $0.30 / $0.90 |
| `nvidia/Nemotron-3-Ultra-550b-a55b` | Complex reasoning | $1.00 / $3.00 |

**Why tiered?** Most cases cost ~$0.003. Complex cases ~$0.018. Average ~$0.01/case.

**Token Factory advantages:** One OpenAI-compatible endpoint, cached-token pricing, model catalog with prices, playground.

### Architecture

```
UI → FastAPI (PHI guard) → 
  Extract (Lightning) → 
  Engine (deterministic rules) → 
  Explain (Super VL) or Reason (Ultra) → 
  Verifier (blocks contradictions) → 
  Report + Human Sign-Off
```

**Key decisions:** Engine decides (deterministic Python), LLMs explain. Verifier diffs output vs engine. Humans release.

### Services

- **Tavily:** Evidence lookup (antibody name only)
- **LangSmith:** Tracing, evals
- **Cloud Run:** Demo hosting (us-central1, min 0 / max 1)
- **GitHub Actions:** CI (pytest + gitleaks)

### Running Tests

**macOS / Linux:**
```bash
cd apps/panelguard
pytest tests/ -v
```

**Windows (cmd):**
```cmd
cd apps\panelguard && pytest tests\ -v
```

### Running Eval

**macOS / Linux:**
```bash
python eval/run_eval.py --cases cases/transfusion-medicine-interpreter --runs 3 --out eval/RESULTS.md
```

**Windows (cmd):**
```cmd
python eval\run_eval.py --cases cases\transfusion-medicine-interpreter --runs 3 --out eval\RESULTS.md
```

**Gates:** 0 unsafe recommendations, 100% panel status accuracy, ≥90% antibody ID.

### Deploy to Cloud Run

**macOS / Linux:**
```bash
gcloud config set project echukwuka-435611
gcloud secrets create nebius-api-key --replication-policy=automatic
echo -n "<key>" | gcloud secrets versions add nebius-api-key --data-file=-
gcloud secrets create tavily-api-key --replication-policy=automatic
echo -n "<key>" | gcloud secrets versions add tavily-api-key --data-file=-

gcloud run deploy panelguard \
  --source apps/panelguard \
  --region us-central1 \
  --min-instances 0 \
  --max-instances 1 \
  --memory 512Mi \
  --set-secrets NEBIUS_API_KEY=nebius-api-key:latest,TAVILY_API_KEY=tavily-api-key:latest \
  --set-env-vars LIVE_DAILY_CAP=40,MODEL_FAST=nvidia/Nemotron-3_5-Lightning,MODEL_MID=nvidia/Nemotron-3.5-Super-VL,MODEL_REASON=nvidia/Nemotron-3-Ultra-550b-a55b
```

**Windows (cmd - use PowerShell for echo or type keys into file):**
```cmd
gcloud config set project echukwuka-435611
gcloud secrets create nebius-api-key --replication-policy=automatic
echo|set /p="<key>" | gcloud secrets versions add nebius-api-key --data-file=-
gcloud secrets create tavily-api-key --replication-policy=automatic
echo|set /p="<key>" | gcloud secrets versions add tavily-api-key --data-file=-
gcloud run deploy panelguard --source apps\panelguard --region us-central1 --min-instances 0 --max-instances 1 --memory 512Mi --set-secrets NEBIUS_API_KEY=nebius-api-key:latest,TAVILY_API_KEY=tavily-api-key:latest --set-env-vars LIVE_DAILY_CAP=40,MODEL_FAST=nvidia/Nemotron-3_5-Lightning,MODEL_MID=nvidia/Nemotron-3.5-Super-VL,MODEL_REASON=nvidia/Nemotron-3-Ultra-550b-a55b
```

### Repo Layout

```
apps/panelguard/       FastAPI app, engines, agents, UI
cases/                 Synthetic cases (IH-001, IH-008, IH-015, IH-027+)
eval/                  Evaluation harness
.github/workflows/     CI
immunohaematology-interpreter-skill/  Source of clinical rules
LICENSE                MIT (added Oct 2026)
```

### Limitations

- **Research only. Not a medical device.**
- All outputs need review by qualified professional
- Complex cases refer to reference lab
- CBAHI-regulated settings need Biomedical Scientist sign-off

<a name="what-was-significantly-updated"></a>
### What Was Significantly Updated (26 Aug – 30 Oct 2026)

Repo created April 2026 with Markdown skills only. **Added during hackathon:**

1. **PanelGuard app** (`apps/panelguard`): FastAPI with deterministic engine (ABO/Rh compatibility, antibody rule-out/rule-in with dosage + 3+/3- logic, antigen-negative unit selection, DAT)
2. **Nemotron integration**: Tiered routing (Lightning/Super VL/Ultra), JSON schemas, verifier blocking contradictions
3. **Tools**: Tavily (antibody name only), LangSmith, PHI guard, rate caps, human sign-off
4. **Cases**: Synthetic IH cases (partial: IH-001, 008, 015, 027), eval harness, pytest, GitHub Actions
5. **Deployment**: Cloud Run config
6. **License**: MIT added, README rewritten

Earlier (Oct 2026): Clinical example replaced with synthetic data, research notices added.

### License & Contact

MIT License. Copyright (c) 2026 Emeka Patrick Chukwuka / ALAFIAAI. See [LICENSE](./LICENSE).

**Contact:** Dr. Emeka Patrick Chukwuka (ALAFIAAI / EEHLSS)

For clinical cases: consult Consultant Haematologist or Reference Laboratory.

---

*Research, education, and decision support. Not a replacement for human expertise.*
