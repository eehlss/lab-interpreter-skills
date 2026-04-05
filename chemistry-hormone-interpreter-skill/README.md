# Clinical Chemistry & Hormone Panel Interpreter — SKILL.md v2.0

**Developed by:** Echukwuka
**Version:** 2.0 | **Updated:** April 2026
**Instruments:** Siemens Atellica CH (photometry/IMT/EMIT/PETINIA) · Atellica IM (chemiluminescence/acridinium ester) · Roche Cobas (ECLIA) · Compatible with Mindray, Abbott Architect, Beckman AU series
**Standards:** IFCC · CLSI · ISO 15189:2022 · JCAHO NPSG.02.03.01 · CBAHI · SFDA · ESC 2023 · Endocrine Society · IOF · NICE · KDIGO 2022

---

## What's New in Version 2.0

Version 2.0 is a major expansion over v1.0, adding:

- **Thyroid:** Comprehensive TSH algorithm table, pregnancy trimester-specific ranges (T1/T2/T3), reverse T3, TRAb, thyroglobulin, calcitonin, full drug effects table (amiodarone, steroids, heparin, oestrogens, lithium, phenytoin, metformin), NTI (sick euthyroid) differentiation
- **Adrenal:** Full cortisol/ACTH matrix, Cushing's screening algorithm (1mg DST, UFC, midnight salivary cortisol), ARR for hyperaldosteronism, 17-OH progesterone for CAH screening, DHEA-S, aldosterone:renin ratio interpretation
- **Cardiac:** ESC 0h/1h serial troponin algorithm (sex-specific 99th percentiles), NT-proBNP/BNP framework with obesity and CKD confounders, CK-MB index calculation, myoglobin, D-Dimer age-adjusted threshold, Lp(a), ApoB, ApoA1, homocysteine as cardiac risk marker
- **Bone Health:** Complete PTH + Ca decision matrix, Vitamin D staging with dosing protocols, 1,25-OH-Vitamin D, CKD bone disease guidance (alfacalcidol/calcitriol), P1NP and CTX bone turnover markers with osteoporosis monitoring criteria, BSALP, osteocalcin, urine DPD
- **Vitamin B12 & Folate:** Full B12 deficiency interpretation framework (serum B12 + MMA + holotranscobalamin + homocysteine), RBC folate vs serum folate distinction, causes of B12 and folate deficiency, B12 vs folate distinguishing table, treatment protocols (IM hydroxocobalamin, oral cyanocobalamin, folic acid), pernicious anaemia workup (IF-Ab, PCA, gastrin), metformin-B12 monitoring, CRITICAL WARNING against folate-only treatment
- **Reproductive Hormones:** Full cycle-phase reference tables (LH/FSH/E2/progesterone/testosterone/SHBG/prolactin/DHEA-S/AMH/inhibin B), male reference ranges, Free Androgen Index (FAI) calculation, complete reproductive hormone interpretation framework (POI, menopause, PCOS, DOR, hyperprolactinaemia, hypogonadotrophic hypogonadism, anovulation, testicular failure), OCP/HRT effects on gonadotrophin assays, progesterone ovulation confirmation rule
- **Extended Critical Values Table:** 35+ analytes with panic thresholds including Vitamin D toxicity, severe B12 deficiency, PTH, prolactin macroadenoma threshold, homocysteine, ferritin (HLH), ARR
- **Extended Pattern Library:** 20+ multi-analyte syndrome patterns including HLH, cardiorenal syndrome, hypothyroidism with bone effects, NAFLD, PCOS with metabolic syndrome, megaloblastic anaemia, high-turnover bone disease
- **Updated Output Modes:** Dedicated modes for each new organ system

---

## What This Skill Does

This Claude AI skill interprets clinical chemistry and hormone panel results from any automated analyser and produces a full structured clinical report covering:

- **Section 1 — Critical Value Alert:** Immediate flag with notification action for any panic-threshold result
- **Section 2 — Parameter Table:** Every analyte with age/sex-corrected reference ranges and status
- **Section 3 — Organ System Assessment:** 12 subsystems — renal, liver, metabolic, iron, thyroid, adrenal, reproductive/fertility, cardiac, bone, B12/folate, inflammatory, tumour markers
- **Section 4 — Integrated Clinical Narrative:** Syndrome-level assessment combining all abnormalities
- **Section 5 — Differential Diagnosis:** Ranked with supporting evidence; conditions excluded
- **Section 6 — Instrument/QC Assessment:** Interference flags, method limitations, pre-analytical concerns
- **Section 7 — Action Plan:** Tiered — immediate (critical), short-term, further investigations, referrals, QC
- **Section 8 — Brief Conclusion:** 3–5 sentence plain-language summary for report comment or clinician

---

## What You Need Before Starting

### Required
1. Image or typed values from the chemistry/hormone panel
2. Patient **age** and **biological sex**
3. **Clinical context**

### The skill will ask for (if not provided):
- **Menstrual cycle day** — essential for LH, FSH, E2, progesterone, inhibin B (female)
- **Time of blood draw** — cortisol, ACTH, testosterone are diurnal; 08:00–09:00 required
- **Fasting status** — glucose, lipids, triglycerides, insulin, CTX bone marker (all fasting-dependent)
- **Pregnancy status** — transforms virtually all hormone reference ranges
- **Contraceptive/HRT use** — OCP suppresses LH/FSH to near-zero; raises SHBG; alters free androgens
- **Biotin supplementation** >5mg/day — causes false TSH (↓), FT4 (↑), troponin, Vitamin D, folate, B12, PTH, LH, FSH, hCG on streptavidin-based immunoassays
- **Medications** — metformin (→↓B12), PPIs (→↓B12), antiepileptics (→↓folate/↓Vit D), steroids (→↑glucose, ↓cortisol response), antipsychotics (→↑prolactin), amiodarone (→↑T4/↓T3)

---

## How to Install

### Option A — Clone the repository and run in Claude Code (recommended)

1. Clone this repository locally:

```bash
git clone https://github.com/eehlss/lab-interpreter-skills.git
cd lab-interpreter-skills
```

2. Add this skill folder to Claude Code project skills:

```bash
mkdir -p .claude/skills
cp -R chemistry-hormone-interpreter-skill .claude/skills/
```

3. Open Claude Code in the repository and ask, for example:
- "Interpret this chemistry and hormone panel"
- "Thyroid only"
- "Cardiac only"

### Option B — Install for all projects on your local PC

```bash
mkdir -p ~/.claude/skills
cp -R chemistry-hormone-interpreter-skill ~/.claude/skills/
```

### Option C — Claude.ai (Web or Mobile App)

1. Open Claude.ai and sign in.
2. Go to Settings and then Custom Instructions.
3. Open SKILL.md from this folder.
4. Copy the full SKILL.md content into Custom Instructions.
5. Save and start a new chat.

### Option D — Claude API Integration
```python
import anthropic, base64

with open("SKILL.md", "r") as f:
    skill = f.read()

with open("result_image.jpg", "rb") as img:
    image_data = base64.b64encode(img.read()).decode("utf-8")

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    system=skill,
    messages=[{
        "role": "user",
        "content": [
            {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": image_data}},
            {"type": "text", "text": "Interpret this panel. Patient: 38F. Routine screen. Fasting. No medications."}
        ]
    }]
)
print(response.content[0].text)
```

### Option E — n8n Automation (local setup)
Wire HTTP Request node → `https://api.anthropic.com/v1/messages`:
- `system` = SKILL.md content
- `messages[0].content` = base64 image + patient context text
- Output → Email/Slack for delivery to clinical inbox

---

## How to Use

### Basic Usage (Claude.ai)

Upload your result image and type:

```
Interpret this chemistry panel. Patient: 52F. Diabetes follow-up.
Fasting sample at 08:00. On metformin 1g BD for 3 years. 
No other medications. Last B12 not checked.
```

```
Thyroid only. Patient: 35M. Fatigue and weight gain. 
On amiodarone for AF. Sample drawn 09:00.
```

```
Interpret this cardiac panel. Patient: 64F, chest pain 2h ago.
Troponin at 0h and 1h attached. Has CKD Stage 3.
```

```
Bone health assessment. Patient: 58F, postmenopausal.
On alendronate for 2 years. Fasting 08:00 sample.
Also check Vitamin D status.
```

```
Vitamin B12 and folate assessment. Patient: 72M.
On metformin 2g/day for 10 years. Macrocytic anaemia on CBC.
B12, folate, MMA, homocysteine results attached.
```

```
Fertility hormone workup. Patient: 28F. Day 3 of cycle.
Trying to conceive for 18 months. No medications.
```

### Output Modes

| Phrase | Output |
|--------|--------|
| *(default)* | Full 8-section report |
| `"quick summary"` | Critical values + brief conclusion only |
| `"just critical values"` | Section 1 only |
| `"thyroid only"` | Thyroid assessment + algorithm + action |
| `"adrenal only"` | Adrenal/cortisol assessment + action |
| `"fertility"` / `"reproductive"` | Gonadal hormone assessment + action |
| `"cardiac only"` | Cardiac function + serial troponin + action |
| `"bone health"` | PTH/Vit D/Ca/P1NP/CTX + action |
| `"B12 folate"` | B12/folate framework + treatment protocol |
| `"liver only"` | Liver function + R-ratio + action |
| `"kidney only"` | Renal + CKD staging + action |
| `"iron studies"` | Iron panel pattern + differential |
| `"inflammatory"` | CRP/PCT/ESR/IL-6 + sepsis assessment |

---

## Analyte Coverage — Full List

### Chemistry (Atellica CH / Cobas c-series)
**Renal:** Creatinine, eGFR, Urea/BUN, Uric acid, Cystatin C
**Electrolytes:** Na⁺, K⁺, Cl⁻, HCO₃⁻, Ca²⁺, Phosphate, Magnesium
**Liver:** AST, ALT, ALP, GGT, Total/Direct/Indirect Bilirubin, Total Protein, Albumin, Globulin, LDH, Ammonia
**Metabolic:** Fasting/random glucose, HbA1c, Total Cholesterol, HDL, LDL, Non-HDL, Triglycerides, ApoB, ApoA1, Lp(a), Insulin, C-peptide
**Iron:** Serum Iron, TIBC, Transferrin Saturation, Ferritin, Transferrin, sTfR, Hepcidin
**Cardiac enzymes:** CK, CK-MB, CK-MB index, Myoglobin, LDH, D-Dimer, Fibrinogen, Homocysteine
**Inflammatory:** CRP, hs-CRP, ESR, Procalcitonin, IL-6, Lactate

### Immunoassay (Atellica IM / Cobas e-series)
**Thyroid:** TSH (3rd/4th gen), FT4, FT3, Total T4, Total T3, Reverse T3, Anti-TPO, Anti-Tg, TRAb, Thyroglobulin, Calcitonin
**Adrenal:** Cortisol (serum + salivary), ACTH, Aldosterone, Renin, DHEA-S, 17-OH Progesterone, 24h UFC
**Reproductive (Female):** LH, FSH, Estradiol, Progesterone, Prolactin, SHBG, AMH, Inhibin B, DHEA-S, Beta-hCG
**Reproductive (Male):** LH, FSH, Testosterone (total + free), Estradiol, SHBG, Prolactin, Inhibin B
**Cardiac:** hs-Troponin I (sex-specific), hs-Troponin T, NT-proBNP, BNP
**Bone Health:** PTH (intact 1–84), 25-OH Vitamin D, 1,25-(OH)₂ Vitamin D, BSALP, P1NP, CTX, Osteocalcin, Urine DPD
**Haematinics:** Vitamin B12, Serum Folate, RBC/Erythrocyte Folate, Homocysteine, MMA, Holotranscobalamin, IF-Ab, PCA, Gastrin
**Tumour Markers:** PSA, AFP, CEA, CA-125, CA 19-9, CA 15-3, Beta-hCG, Chromogranin A, 5-HIAA

---

## Critical Value System

35+ analytes with panic thresholds, applying JCAHO NPSG.02.03.01 + ISO 15189:2022 standards:
- Direct clinician notification within 60 minutes
- Documentation of time, person notified, value communicated
- Escalation pathway if no contact

New critical thresholds added in v2.0: Vitamin D severe deficiency (<12 nmol/L) and toxicity (>375 nmol/L); B12 severe deficiency with neurological symptoms; PTH severe secondary hyperparathyroidism; prolactin macroadenoma threshold; ferritin (HLH); ARR (Conn's syndrome)

---

## Limitations

- Clinical decision support only — all outputs require validation by a qualified Medical Laboratory Scientist or Clinical Biochemist before patient management decisions
- Hormone interpretation requires cycle day (female) and sample time (cortisol/testosterone) — results without this context are flagged as provisional
- Reference ranges are IFCC/CLSI consensus — laboratory-specific locally validated ranges take precedence
- Biotin >5mg/day causes false results in all streptavidin-based immunoassays; the skill will flag this if suspected
- **CBAHI/SFDA (Saudi Arabia):** All critical value notifications must be documented per accreditation standards; pernicious anaemia and adrenal insufficiency diagnoses require specialist confirmation before treatment
- Serial troponin requires clinical context (chest pain onset time, ECG findings) — the skill will note when this information is absent
- Bone turnover markers (CTX, P1NP) require fasting 08:00 samples — results without this specification will be interpreted with noted uncertainty

---

## Recommended Companion Skills

| Skill | File | Covers |
|-------|------|--------|
| `sysmex-xn-cbc-interpreter` | SKILL.md | Sysmex XN CBC, flags, scattergrams, blood film decisions |
| `hb-interpreter` | SKILL.md | Bio-Rad HPLC + Sebia CZE haemoglobinopathy diagnosis |
| `chemistry-hormone-interpreter` | SKILL.md (v2.0) | Full chemistry + hormone panels, 12 organ systems, critical values |

Use these together for broader lab interpretation coverage across haematology, haemoglobinopathy, and chemistry/endocrinology.

---

## Install All Three Skills in Claude Code (optional)
```bash
git clone https://github.com/eehlss/lab-interpreter-skills.git
cd lab-interpreter-skills
mkdir -p .claude/skills
cp -R sysmex-xn-cbc-interpreter-skill .claude/skills/
cp -R hb-interpreter-skill .claude/skills/
cp -R chemistry-hormone-interpreter-skill .claude/skills/
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | March 2026 | Initial release — renal, liver, iron, metabolic, basic thyroid/adrenal/reproductive, cardiac, bone, inflammatory, tumour markers |
| 2.0 | April 2026 | Major expansion: comprehensive thyroid algorithm + pregnancy ranges + drug effects; full adrenal Cushing's/Addison's framework + ARR + DHEA-S; cardiac with ESC serial troponin algorithm + BNP confounders + Lp(a)/ApoB; bone with P1NP/CTX monitoring + Vitamin D dosing + CKD guidance; complete B12/folate section (MMA/HoloTC/RBC folate/IF-Ab + treatment protocols); full reproductive hormone framework for both sexes + FAI + AMH + inhibin B + OCP effects; 35+ critical values; 20+ syndrome patterns; 14 output modes |

---

*For use in accredited clinical laboratory practice. Results require validation by a qualified Medical Laboratory Scientist.*
