> **Research Purpose Only.** This material is a research and decision-support resource. It is not a validated or approved medical device, and its output must not be the sole basis for any clinical decision; all results require review by a qualified professional.

# Lab Interpreter Skills

This repository bundles four clinical laboratory interpretation skills designed for Claude-based workflows.

Each subfolder contains:
- `SKILL.md`: the actual skill logic and behavior
- `README.md`: detailed domain-specific guidance and examples

## Subfolder Structure Summary

| Subfolder | Skill Focus | What It Interprets | Typical Output |
|---|---|---|---|
| `sysmex-xn-cbc-interpreter-skill/` | Hematology CBC interpretation | Sysmex XN-series CBC printouts, flags, scattergrams/histograms | CBC parameter analysis, flag interpretation, blood film decision, QC checks, action plan |
| `hb-interpreter-skill/` | Hemoglobinopathy interpretation | Bio-Rad HPLC and Sebia CZE hemoglobin fraction studies + CBC context | Hb fraction analysis, CBC discriminant indices, thalassemia/variant differential, confirmatory plan |
| `chemistry-hormone-interpreter-skill/` | Clinical chemistry and endocrine interpretation | Chemistry panels (renal/liver/metabolic/iron/cardiac/inflammatory) and hormone panels (thyroid/adrenal/reproductive/bone/B12-folate) | Critical-value triage, organ-system interpretation, differential diagnosis, integrated action plan |
| `immunohaematology-interpreter-skill/` | Transfusion medicine and blood bank support | Antibody screens/panels, DAT/IAT, ABO/Rh typing, crossmatch workups | Antibody identification workflow, compatibility guidance, blood product recommendation, transfusion safety actions |

## Detailed Summary by Subfolder

### 1) `sysmex-xn-cbc-interpreter-skill/`
- Domain: Routine and complex CBC interpretation from Sysmex XN analyzers.
- Strengths: Interprets WBC/RBC/PLT flags, channel/scattergram patterns, and blood film escalation needs.
- Inputs usually needed: Result image, patient age, biological sex, clinical context.
- Best for: Fast triage of abnormal CBCs and standardized analyzer troubleshooting.

### 2) `hb-interpreter-skill/`
- Domain: Hemoglobinopathy and microcytic anemia differentiation.
- Strengths: Correlates Bio-Rad HPLC and Sebia CZE findings with RBC indices and discriminant formulas.
- Inputs usually needed: HPLC/CZE report image, age, sex, complete CBC indices (plus iron studies when available).
- Best for: Distinguishing beta-thal trait, alpha-thal patterns, Hb variants, and iron deficiency overlap.

### 3) `chemistry-hormone-interpreter-skill/`
- Domain: Broad chemistry plus hormone interpretation framework.
- Strengths: Multi-system interpretation (renal, liver, metabolic, cardiac, endocrine, fertility, bone, inflammation, haematinics), critical-value handling, and clinical prioritization.
- Inputs usually needed: Chemistry/hormone values or image, age, sex, context (and cycle day/time/fasting for hormone relevance).
- Best for: Comprehensive biochemistry interpretation with high-structure reporting.

### 4) `immunohaematology-interpreter-skill/`
- Domain: Blood bank and transfusion medicine decision support.
- Strengths: Antibody screen/panel reasoning, DAT/IAT interpretation, ABO/Rh discrepancy pathways, crossmatch and compatible unit selection.
- Inputs usually needed: Panel/crossmatch image, ABO/Rh type, age/sex, clinical/transfusion history, autocontrol.
- Best for: Complex pre-transfusion workups and immunohematology safety workflows.

## How To Use These Skills In Claude Code

Claude Code can load skills from a `.claude/skills/` directory. The important file is `SKILL.md` inside each skill folder.

### Option A: Install Per Project (recommended)

From this repository root:

```bash
mkdir -p .claude/skills
cp -R sysmex-xn-cbc-interpreter-skill .claude/skills/
cp -R hb-interpreter-skill .claude/skills/
cp -R chemistry-hormone-interpreter-skill .claude/skills/
cp -R immunohaematology-interpreter-skill .claude/skills/
```

After this, open Claude Code in this project and prompt naturally, for example:
- "Interpret this Sysmex XN CBC printout"
- "Interpret this Hb HPLC/CZE result"
- "Interpret this chemistry and hormone panel"
- "Interpret this antibody panel and crossmatch"

### Option B: Install For Your User (all projects on your PC)

If your Claude Code setup supports a user-level `.claude/skills/` location, copy the same four folders there once, then reuse everywhere.

macOS/Linux example:

```bash
mkdir -p ~/.claude/skills
cp -R sysmex-xn-cbc-interpreter-skill ~/.claude/skills/
cp -R hb-interpreter-skill ~/.claude/skills/
cp -R chemistry-hormone-interpreter-skill ~/.claude/skills/
cp -R immunohaematology-interpreter-skill ~/.claude/skills/
```

Windows PowerShell example:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse -Force .\sysmex-xn-cbc-interpreter-skill "$HOME\.claude\skills\"
Copy-Item -Recurse -Force .\hb-interpreter-skill "$HOME\.claude\skills\"
Copy-Item -Recurse -Force .\chemistry-hormone-interpreter-skill "$HOME\.claude\skills\"
Copy-Item -Recurse -Force .\immunohaematology-interpreter-skill "$HOME\.claude\skills\"
```

## Running Locally On Any PC With Claude Code Installed

1. Install Claude Code and complete sign-in/authentication.
2. Clone or copy this repository to the PC.
3. Place skill folders in either project `.claude/skills/` or user `~/.claude/skills/`.
4. Start Claude Code from the repository (or any project if using user-level install).
5. Provide:
   - a clear lab result image or typed values
   - required patient context (age/sex and domain-specific metadata)
6. Use targeted prompts to trigger the relevant skill.

## Recommended Prompt Templates

- CBC:
  - "Interpret this Sysmex XN CBC. Patient: 42M. Context: fatigue. QC passed today."
- Hemoglobinopathy:
  - "Interpret this HPLC/CZE result and correlate with CBC for thalassemia vs IDA."
- Chemistry/Hormone:
  - "Interpret this chemistry and hormone panel. Patient: 33F, fasting, sample at 08:30, cycle day 3."
- Immunohaematology:
  - "Interpret this antibody panel and suggest compatible blood products. Autocontrol is negative."

## Safety Note

These skills are clinical decision-support aids, not a replacement for licensed clinical judgment. Final interpretation and patient-management decisions must be validated by qualified laboratory and clinical professionals.
