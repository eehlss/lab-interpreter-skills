> **Research Purpose Only.** This material is a research and decision-support resource. It is not a validated or approved medical device, and its output must not be the sole basis for any clinical decision; all results require review by a qualified professional.

# Lab Interpreter Skills + PanelGuard

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![CI](https://github.com/eehlss/lab-interpreter-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/eehlss/lab-interpreter-skills/actions/workflows/ci.yml)

Medical laboratory interpretation skills for Claude AI, plus **PanelGuard**: a blood bank copilot built for the [Nebius x NVIDIA Global AI Hackathon](https://nebius-nvidia-ai-hackathon.devpost.com/).

---

## 🩸 PanelGuard: Blood Bank Copilot

**Track:** Best Apps and Agents  
**Demo:** TBD (deploy to Cloud Run after submission)  
**Video:** TBD  
**Devpost:** TBD

PanelGuard turns antibody panel workups into reviewed, explained recommendations in under a minute. **Deterministic blood-bank rules make every safety decision.** NVIDIA Nemotron models on Nebius Token Factory read inputs, reason about hard cases, and explain every step. A qualified scientist always signs off.

### How We Use NVIDIA Nemotron on Nebius Token Factory

| Model | Role | Use Case | Cost per 1M tokens (in/out) |
|-------|------|----------|------------------------------|
| **nvidia/Nemotron-3_5-Lightning** | Fast tier | Input extraction, verifier language checks | $0.06 / $0.24 |
| **nvidia/Nemotron-3.5-Super-VL** | Mid tier | Routine explanations, panel photo reading | $0.30 / $0.90 |
| **nvidia/Nemotron-3-Ultra-550b-a55b** | Reasoning tier | Complex cases: multiple antibodies, positive autocontrol, insufficient cells, positive DAT, special populations | $1.00 / $3.00 |

**Why tiered routing?** Most cases are routine. Lightning and Super VL handle them quickly and cheaply (~$0.003/case). Only complex cases need Ultra's deep reasoning (~$0.018/case). This keeps average cost around $0.01/case while maintaining safety.

**Token Factory advantages:**
- One OpenAI-compatible endpoint (`https://api.tokenfactory.nebius.com/v1/`) for three model sizes
- Cached-token pricing (50-80% discount on repeated prompt prefixes)
- Public machine-readable model catalog with pricing
- Playground for prompt testing before integration
- Hosted in eu-north1 (Lightning), us-north1 (Super VL), us-central1 (Ultra)

### Other Services

- **Tavily:** Evidence lookup for rare antibodies (sends antibody name only, never patient data). Cache per antibody to protect credits.
- **LangSmith:** Tracing all LLM calls, eval datasets, experiment comparison (screenshots in video/README).
- **Google Cloud Run:** Demo hosting (us-central1, min 0 / max 1 instances, free tier covers demo traffic).
- **GitHub Actions:** CI with pytest and gitleaks.

### Architecture & Safety Design

```
Scientist (UI) → FastAPI (PHI guard + rate cap) → 
  1. Extract (Lightning or Super VL if photo) →
  2. Deterministic Engine (ABO/Rh, rule-out, 3+/3-, units) ← SOURCE OF TRUTH →
  3. Router (simple → Super VL explain | complex → Ultra reason) →
  4. Verifier (diffs LLM vs engine, blocks contradictions) →
  5. Report + Sign-Off (human reviewer required)
```

**Key design decisions:**

1. **Engine decides, LLMs explain.** ABO/Rh compatibility, antibody rule-out/rule-in, 3+/3- confidence, and antigen-negative unit selection are deterministic Python functions with unit tests. The LLM gets the engine's output as fixed input and must explain it, not recompute it.

2. **Verifier blocks unsafe output.** After generation, a structured diff checks: every antibody specificity the LLM names must be in the engine's candidates list; every unit it recommends must be in the engine's compatible list; it must not contradict safety alerts; the disclaimer must be present. Any mismatch hides the LLM text and shows the engine-only report with a "verifier blocked narrative" badge.

3. **Tiered by cost.** Lightning handles extraction and verifier checks ($0.06/$0.24 per M tokens). Super VL handles routine explanations and panel photos ($0.30/$0.90). Ultra runs only when the router marks a case complex ($1/$3): positive autocontrol, more than one candidate specificity, fewer than 3+/3- cells, DAT positive, or special population.

4. **JSON schemas for all outputs.** Every LLM call uses Token Factory's `response_format` with a JSON schema. If the output doesn't validate, retry once, then fallback to engine-only.

5. **Model IDs from environment variables** with sensible defaults that aren't being retired. If a model is deprecated, the fix is a config change, not a code change.

6. **Synthetic data only.** A PHI guard rejects input that looks like a name, an MRN or national ID, or a real date (anything not in year 2099). The UI lists only `SYN-` cases. Tavily receives only the antibody specificity.

7. **A human releases.** The "Release units" button stays disabled until a reviewer ticks "Reviewed by a qualified scientist" and types initials. The demo logs the sign-off and issues nothing.

8. **Credit protection.** The 30 preset cases are served from cached, pre-computed traces showing the original model and timestamp (no credit). Live LLM calls are capped per IP and per day. When the cap is reached, the app falls back to engine-only.

### Quick Start

**Windows (cmd):**

```cmd
git clone https://github.com/eehlss/lab-interpreter-skills.git
cd lab-interpreter-skills
python -m venv .venv
call .venv\Scripts\activate.bat
pip install -r apps\panelguard\requirements.txt
set NEBIUS_API_KEY=<your-key-here>
set TAVILY_API_KEY=<your-key-here>
python -m pytest apps\panelguard\tests -q
python -m uvicorn app.main:app --app-dir apps\panelguard --host 127.0.0.1 --port 8080
```

Then open `http://127.0.0.1:8080`.

**macOS / Linux (bash/zsh):**

```bash
git clone https://github.com/eehlss/lab-interpreter-skills.git
cd lab-interpreter-skills
python3 -m venv .venv
source .venv/bin/activate
pip install -r apps/panelguard/requirements.txt
export NEBIUS_API_KEY=<your-key-here>
export TAVILY_API_KEY=<your-key-here>
python -m pytest apps/panelguard/tests -q
uvicorn app.main:app --app-dir apps/panelguard --host 0.0.0.0 --port 8080
```

**Docker:**

```bash
cd apps/panelguard
docker build -t panelguard .
docker run -p 8080:8080 -e NEBIUS_API_KEY=<key> -e TAVILY_API_KEY=<key> panelguard
```

**Offline mode:** If `NEBIUS_API_KEY` is not set, the app runs rules-only (no LLM explanations). The deterministic engine still works.

### Running Tests and Eval

```bash
# Unit tests
cd apps/panelguard
pytest tests/ -v

# Evaluation harness
cd ../..
python eval/run_eval.py --cases cases/transfusion-medicine-interpreter --runs 3 --out eval/RESULTS.md
```

**Gates:**
- Unsafe recommendations (ABO-incompatible or antigen-positive units): must be 0
- Panel status accuracy: 100% target
- Antibody ID accuracy: ≥90% target (27/30 on majority-of-3)
- Verifier fault injection: 10/10 catch rate

### Deploy to Google Cloud Run (Owner Only)

```bash
gcloud config set project echukwuka-435611
gcloud secrets create nebius-api-key --replication-policy=automatic
echo -n "<your-key>" | gcloud secrets versions add nebius-api-key --data-file=-
gcloud secrets create tavily-api-key --replication-policy=automatic
echo -n "<your-key>" | gcloud secrets versions add tavily-api-key --data-file=-

gcloud run deploy panelguard \
  --source apps/panelguard \
  --region us-central1 \
  --min-instances 0 \
  --max-instances 1 \
  --memory 512Mi \
  --cpu 1 \
  --concurrency 20 \
  --set-secrets NEBIUS_API_KEY=nebius-api-key:latest,TAVILY_API_KEY=tavily-api-key:latest \
  --set-env-vars LIVE_DAILY_CAP=40,MODEL_FAST=nvidia/Nemotron-3_5-Lightning,MODEL_MID=nvidia/Nemotron-3.5-Super-VL,MODEL_REASON=nvidia/Nemotron-3-Ultra-550b-a55b
```

### Repo Layout

```
lab-interpreter-skills/
├── LICENSE                          MIT License (added Oct 2026 for hackathon)
├── README.md                        This file
├── apps/panelguard/                 PanelGuard application (NEW)
│   ├── engine/                      Deterministic rules engines (ABO, panel, units, DAT)
│   ├── agents/                      LLM client, extract, explain, reason, verify, Tavily
│   ├── app/                         FastAPI server + PHI guard
│   ├── ui/                          Single-page web UI
│   ├── data/                        Synthetic blood unit inventory
│   ├── tests/                       pytest suite
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── cases/                           Synthetic case library (NEW)
│   └── transfusion-medicine-interpreter/
│       ├── IH-001-abo-a-pos-routine/    case.json + expected.json + README.md
│       ├── IH-008-anti-k-single/
│       ├── IH-015-anti-e-plus-anti-c/
│       └── IH-027-positive-autocontrol/
├── eval/                            Evaluation harness (NEW)
│   ├── run_eval.py
│   └── RESULTS.md
├── .github/workflows/ci.yml         GitHub Actions CI (NEW)
├── immunohaematology-interpreter-skill/  Original Claude skill (source of clinical rules)
│   ├── SKILL.md
│   └── README.md
└── (other skills: sysmex-xn-cbc, hb, chemistry-hormone...)
```

### Limitations

- **Research and decision-support only.** Not a medical device. Not for clinical use.
- All outputs require review by a qualified professional (Biomedical Scientist, Medical Laboratory Scientist, or Transfusion Medicine Physician).
- Complex cases (unresolved antibodies, suspected autoantibody with underlying alloantibody, daratumumab interference in multi-transfused patients, rare antigen deficiencies) **must be referred to a Transfusion Medicine Reference Laboratory.**
- Results are interpretations of data you provide. Those data must come from properly controlled, QC-verified laboratory testing.
- In Saudi Arabia / CBAHI-regulated settings: all compatibility reports require sign-off by a qualified Biomedical Scientist.

### What Was Significantly Updated During the Hackathon Submission Period

The repository was created 5 April 2026 and previously contained only Markdown prompt files ("skills") for Claude Code: **no runnable code, no tests, no license, no cases.** The Nebius x NVIDIA Global AI Hackathon submission period opened 26 August 2026.

**During the submission period (26 Aug to 30 Oct 2026), the following were added:**

1. **PanelGuard application** (`apps/panelguard`): FastAPI app with a deterministic immunohaematology engine (ABO/Rh compatibility, antibody rule-out/rule-in with dosage and 3+/3- logic, antigen-negative unit selection, DAT interpretation).

2. **NVIDIA Nemotron integration** via Nebius Token Factory with tiered routing (Lightning for extraction, Super VL for explanation, Ultra for complex reasoning), JSON-schema structured outputs, and a verifier that blocks any LLM narrative contradicting the deterministic engine results.

3. **Tavily evidence tool** (antibody name only, cached), LangSmith tracing, PHI guard rejecting identifier-like input, rate caps, and human sign-off workflow.

4. **Synthetic case library** (IH-001 to IH-004, IH-008, IH-015, IH-027 at time of initial submission; owner to complete remaining cases), evaluation harness with pass/fail gates, unit tests (pytest), and GitHub Actions CI (tests + gitleaks).

5. **Public demo** deployment configuration for Google Cloud Run (us-central1, min 0 / max 1 instances).

6. **Open-source license** (MIT) and this rewritten README with PanelGuard at the top.

Earlier in the period (October 2026), the clinical example in `immunohaematology-interpreter-skill/SKILL.md` was replaced with a synthetic, de-identified one, and research-only notices were added throughout all skill files.

### License

MIT License. Copyright (c) 2026 Emeka Patrick Chukwuka / ALAFIAAI. See [LICENSE](./LICENSE).

### Contact

Developed and maintained by **Dr. Emeka Patrick Chukwuka** (ALAFIAAI / EEHLSS).

For complex transfusion cases in clinical practice, consult your Consultant Haematologist, Transfusion Medicine Physician, or National Blood Transfusion Service Reference Laboratory.

---

## Claude AI Skills (Original Repository Content)

This repository also bundles four clinical laboratory interpretation skills designed for Claude-based workflows (the original content, pre-dating PanelGuard).

Each skill subfolder contains:
- `SKILL.md`: the actual skill logic and behavior
- `README.md`: detailed domain-specific guidance and examples

| Subfolder | Skill Focus | What It Interprets | Typical Output |
|---|---|---|---|
| `sysmex-xn-cbc-interpreter-skill/` | Hematology CBC interpretation | Sysmex XN-series CBC printouts, flags, scattergrams/histograms | CBC parameter analysis, flag interpretation, blood film decision, QC checks, action plan |
| `hb-interpreter-skill/` | Hemoglobinopathy interpretation | Bio-Rad HPLC and Sebia CZE hemoglobin fraction studies + CBC context | Hb fraction analysis, CBC discriminant indices, thalassemia/variant differential, confirmatory plan |
| `chemistry-hormone-interpreter-skill/` | Clinical chemistry and endocrine interpretation | Chemistry panels (renal/liver/metabolic/iron/cardiac/inflammatory) and hormone panels (thyroid/adrenal/reproductive/bone/B12-folate) | Critical-value triage, organ-system interpretation, differential diagnosis, integrated action plan |
| `immunohaematology-interpreter-skill/` | Transfusion medicine and blood bank support | Antibody screens/panels, DAT/IAT, ABO/Rh typing, crossmatch workups | Antibody identification workflow, compatibility guidance, blood product recommendation, transfusion safety actions |

### How To Use These Skills In Claude Code

Claude Code can load skills from a `.claude/skills/` directory. The important file is `SKILL.md` inside each skill folder.

**Option A: Install Per Project (recommended)**

```bash
git clone https://github.com/eehlss/lab-interpreter-skills.git
cd lab-interpreter-skills
mkdir -p .claude/skills
cp -R sysmex-xn-cbc-interpreter-skill .claude/skills/
cp -R hb-interpreter-skill .claude/skills/
cp -R chemistry-hormone-interpreter-skill .claude/skills/
cp -R immunohaematology-interpreter-skill .claude/skills/
```

Then open Claude Code in the repository root.

**Option B: Install Globally**

```bash
mkdir -p ~/.claude/skills
cp -R sysmex-xn-cbc-interpreter-skill ~/.claude/skills/
cp -R hb-interpreter-skill ~/.claude/skills/
cp -R chemistry-hormone-interpreter-skill ~/.claude/skills/
cp -R immunohaematology-interpreter-skill ~/.claude/skills/
```

Skills installed globally are available across all Claude Code projects on your machine.

---

*For use in research, education, and clinical decision support under appropriate supervision. Not a replacement for human expertise.*
