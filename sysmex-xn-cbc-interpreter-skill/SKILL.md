---
name: sysmex-xn-cbc-interpreter
description: >
  Sysmex XN-Series (XN-1000/XN-3100/XN-9000) CBC Result Interpreter and Troubleshooter.
  Trigger when a user uploads an image of a Sysmex XN-Series CBC printout and asks for
  interpretation, flagging assessment, blood film review decisions, QC/calibration
  evaluation, or a clinical conclusion with next action plan. Also trigger for:
  "interpret my CBC result", "is a blood film needed?", "check my Sysmex flags",
  "assess my hematology result", "troubleshoot my analyzer result", or when the user
  uploads any Sysmex XN scattergram/printout image and provides age/gender.
  Outputs a structured clinical assessment: parameter review → flag analysis →
  scattergram interpretation → blood film decision → instrument QC check → 
  EEHLSS-branded conclusion + action plan.
---

# Sysmex XN-Series CBC Result Interpreter & Troubleshooter

**Version:** 1.0 | **Platform:** Sysmex XN-1000 / XN-3100 / XN-9000  
**Standards:** ICSH 2014, CLSI H20-A2, BSH 2009 Blood Film Guidelines, ISO 15189:2022  
**Brand:** EEHLSS / MedLabAI-LIS | Colors: Crimson #B71C1C · Navy #0D1B4B · Gold #F9A825

---

## PHASE 0 — INTAKE & CONTEXT COLLECTION

Before interpreting, collect:

1. **Image of the result** — Sysmex XN printout (photograph or scan)
2. **Patient age** (years) and **biological sex** (Male/Female)
3. **Clinical context** (if available) — e.g., "post-chemo", "HIV-positive", "pregnant",  
   "malaria-endemic region", "routine screening", "known sickle cell"
4. **QC status** (if known) — "QC passed today", "QC not done", "QC out of range"
5. **Sample handling notes** (if available) — delay to analysis, storage temp, EDTA tube condition

If age and sex are not provided, **ask before proceeding.** These are mandatory for reference range application.

---

## PHASE 1 — INSTRUMENT TECHNOLOGY PRIMER  
*(Apply silently; reference only when explaining an unexpected result)*

### Detection Channels on XN-Series

| Channel | Method | What It Measures |
|---------|--------|-----------------|
| **RBC/PLT (Impedance)** | Sheath-flow DC detection | RBC count, MCV (→HCT), PLT-I (impedance platelets) |
| **HGB** | SLS-hemoglobin photometry at 555 nm | Hemoglobin concentration |
| **WNR** | Fluorescence flow cytometry (FSC + SFL) | Total WBC, BASO%, NRBC%; separates NRBC from WBC using acidic reagent |
| **WDF** | Fluorescence flow cytometry (FSC + SSC + SFL) | 5-part WBC differential: NEUT, LYMPH, MONO, EO, BASO, IG%; flagging for blasts/abnormal lymphocytes |
| **RET** | Fluorescence flow cytometry (633 nm laser) | Reticulocyte %, RET-He (reticulocyte hemoglobin), IRF (immature reticulocyte fraction), LFR/MFR/HFR |
| **PLT-F** | Fluorescence flow cytometry | Fluorescent platelet count (reference for very low PLT); IPF (immature platelet fraction) |
| **WPC** (reflex) | Fluorescence flow cytometry (Fluorocell WPC dye) | Blast detection; abnormal lymphocyte confirmation after WDF flag |

### Key Physics Principles
- **FSC (Forward Scatter)** = cell volume/size
- **SSC (Side Scatter)** = cell internal complexity (nucleus, granules)
- **SFL (Side Fluorescence)** = nucleic acid content (RNA/DNA) — labelled by proprietary fluorescent dye
- Lysis reagent perforates membranes while preserving cell structure → dye penetrates → fluorescence proportional to RNA/DNA content
- WNR uses more acidic, lower-osmolarity reagent than WDF → erythrocytes lyse completely; basophils resist lysis
- RBC/PLT channel uses **impedance only** — cell size = voltage pulse magnitude

### Why Scattergram Morphology Matters
- Normal cluster positions and tight groupings = reliable differential
- Dispersed, shifted, or fused clusters = suspect interference, sample degradation, or pathological cells
- **WDF scattergram axes:** SSC (y) vs SFL (x) — NEUT (upper right), LYMPH (lower left), MONO (middle), EO (upper left area), BASO/IG (variable positions)
- **WNR scattergram axes:** SFL (y) vs FSC (x) — WBC cluster upper right; NRBC cluster lower left; BASO cluster upper left
- **RET scattergram:** FSC (y) vs SFL (x) — reticulocytes show elevated SFL relative to mature RBC

---

## PHASE 2 — REFERENCE RANGES BY AGE & SEX

Apply the correct reference range before flagging as abnormal or normal.

### Adult Reference Ranges (18–65 years)

| Parameter | Adult Male | Adult Female | Units |
|-----------|-----------|--------------|-------|
| WBC | 4.0–10.0 | 4.0–10.0 | ×10³/µL |
| RBC | 4.5–5.9 | 3.8–5.2 | ×10⁶/µL |
| HGB | 13.5–17.5 | 12.0–16.0 | g/dL |
| HCT | 40–52 | 36–48 | % |
| MCV | 80–100 | 80–100 | fL |
| MCH | 27–33 | 27–33 | pg |
| MCHC | 32–36 | 32–36 | g/dL |
| PLT | 150–400 | 150–400 | ×10³/µL |
| RDW-CV | 11.5–14.5 | 11.5–14.5 | % |
| RDW-SD | 37–54 | 37–54 | fL |
| NEUT% | 45–75 | 45–75 | % |
| LYMPH% | 20–45 | 20–45 | % |
| MONO% | 2–10 | 2–10 | % |
| EO% | 1–6 | 1–6 | % |
| BASO% | 0–1 | 0–1 | % |
| IG% | <2 | <2 | % |
| NEUT# | 1.8–7.7 | 1.8–7.7 | ×10³/µL |
| LYMPH# | 1.0–4.5 | 1.0–4.5 | ×10³/µL |
| MONO# | 0.2–1.0 | 0.2–1.0 | ×10³/µL |
| EO# | 0.02–0.5 | 0.02–0.5 | ×10³/µL |
| BASO# | 0.0–0.1 | 0.0–0.1 | ×10³/µL |
| NRBC# | 0 | 0 | ×10³/µL |
| RET% | 0.5–2.0 | 0.5–2.0 | % |
| IRF | 3–17 | 3–17 | % |
| RET-He | 28–36 | 28–36 | pg |
| MPV | 7.5–12.5 | 7.5–12.5 | fL |
| PDW | 9–17 | 9–17 | fL |
| PCT | 0.15–0.40 | 0.15–0.40 | % |
| P-LCR | 15–35 | 15–35 | % |

### Paediatric Adjustments (flag these for attention)

| Age Group | WBC ×10³/µL | HGB g/dL | RBC ×10⁶/µL | PLT ×10³/µL |
|-----------|------------|---------|------------|------------|
| Neonate (0–7d) | 9–30 | 13.5–21.5 | 3.9–6.3 | 150–400 |
| Infant (1–12m) | 6–17.5 | 9.5–14.0 | 3.0–5.4 | 200–550 |
| Child (1–6y) | 5–15.5 | 11.0–14.0 | 3.7–5.3 | 150–450 |
| Child (6–12y) | 4.5–13.5 | 11.5–15.5 | 3.9–5.3 | 150–450 |
| Adolescent (12–18y) | 4.5–13.0 | M:13–17 / F:12–16 | M:4.5–5.9 / F:4.1–5.3 | 150–400 |

### Special Populations (apply as modifier)
- **Pregnancy:** Lower HGB threshold acceptable (≥10 g/dL in 2nd/3rd trimester); physiological leukocytosis up to 12×10³/µL; thrombocytopenia threshold raised concern at <100
- **African/West African populations:** Benign ethnic neutropenia — NEUT# as low as 1.0 may be physiological; evaluate in clinical context before labeling neutropenic
- **Post-chemotherapy:** Absolute NEUT count critical; threshold for neutropenic fever ≤0.5×10³/µL (severe <0.1)

---

## PHASE 3 — SYSTEMATIC PARAMETER INTERPRETATION

For each result image, parse and evaluate ALL parameters in this order:

### 3A. RBC Line (Erythrocyte Assessment)

**Step 1: Classify anemia or polycythemia**
- Low HGB/RBC → Anemia. Then classify by MCV:
  - MCV <80 fL → **Microcytic** (Iron deficiency, thalassemia, sideroblastic, lead toxicity)
  - MCV 80–100 fL → **Normocytic** (Acute blood loss, hemolysis, chronic disease, aplastic anemia, early mixed deficiency)
  - MCV >100 fL → **Macrocytic** (B12/folate deficiency, liver disease, hypothyroidism, alcohol, drugs — hydroxyurea, methotrexate)
- High HGB/HCT/RBC → Polycythemia
  - Relative (dehydration) vs. Absolute (primary PV vs. secondary causes — hypoxia, EPO)

**Step 2: RDW interpretation**
- Elevated RDW-CV (>14.5%) with low MCV → Iron deficiency favored over thalassemia trait (thalassemia trait has normal/low RDW)
- Elevated RDW with normal MCV → mixed deficiency (iron + B12/folate), or early iron deficiency, or hemolysis
- Elevated RDW with high MCV → B12/folate deficiency, liver disease

**Step 3: MCH/MCHC interpretation**
- Low MCH + low MCHC → Hypochromia → Iron deficiency, thalassemia
- High MCHC (>36 g/dL) → **Suspect: hemolysis, spherocytosis, cold agglutinins**; ALSO a QC alert (see Phase 5)
- MCHC >37 → Strong indicator for blood film + repeat; possible instrument interference (cold agglutinin, lipemia, hemolysis)

**Step 4: RBC histogram shape** (from printout)
- Single symmetric peak: normal
- Right shift (tall peak shifted right): macrocytosis
- Left shift: microcytosis
- Broad peak: anisocytosis (elevated RDW)
- Bimodal (two peaks): dimorphic picture — mixed iron deficiency + B12/folate, or post-transfusion, or treatment response

**Key MCH/MCHC Interference Table:**

| Finding | Possible Cause | Action |
|---------|---------------|--------|
| MCHC >37 g/dL | Hemolysis, cold agglutinin, lipemia, HbS/C | Blood film + spin plasma |
| MCH very low + MCHC low | IDA, thalassemia | Film + ferritin/serum iron |
| Low RBC + high MCV | B12/folate deficiency | Film + B12/folate assay |
| High RBC + low MCV | Thalassemia trait | HPLC/electrophoresis |

---

### 3B. WBC Line (Leukocyte Assessment)

**Step 1: Total WBC**
- <4.0 × 10³/µL → **Leukopenia** (investigate differential, drug history, viral infection, BM pathology)
- 4–10 → Normal
- 10–30 → **Leukocytosis** (infection, inflammation, steroid use, physiological stress, CML spectrum)
- >30 → **Significant leukocytosis** — consider CML, leukemoid reaction, leukemia
- >100 → **Hyperleukocytosis** — URGENT; consider blast crisis, CML, leukemia; WBC clumping/clogging artifacts possible

**Step 2: Differential assessment**

| Cell | High = | Low = |
|------|--------|-------|
| NEUT | Bacterial infection, steroids, CML, G-CSF, stress, burns | Aplasia, viral infection, immune-mediated, ethnic neutropenia, drug toxicity |
| LYMPH | Viral infection (EBV, CMV, COVID), CLL, ALL, pertussis | HIV/AIDS, steroids, immunosuppression, post-radiation |
| MONO | Chronic infection (TB, malaria, leishmania), monocytic leukemia, IBD | Rare; bone marrow suppression |
| EO | Parasitosis, allergy, eosinophilic leukemia, hypereosinophilic syndrome, drug reaction | Not clinically significant when low |
| BASO | CML (hallmark), reactive conditions, basophilic leukemia | Not clinically significant when low |
| IG (immature granulocytes) | Sepsis (early left shift), leukemoid reaction, CML, post-G-CSF | Baseline 0 expected |

**Step 3: NRBC assessment**
- Any NRBC# >0 in adults = **ABNORMAL** (physiological only in neonates)
- Causes: severe hemolytic anemia, thalassemia major, sickle cell crisis, myelophthisic anemia, blast crisis, severe hypoxia
- NRBCs artificially inflate WBC on some older analyzers — XN-Series corrects WBC for NRBCs automatically; check WBC-N vs WBC-D

**Step 4: IG% (immature granulocytes)**
- IG% 2–5%: Monitor, correlate with clinical picture
- IG% >5%: Significant left shift — blood film mandatory
- IG% >10%: Consider CML or sepsis; urgent clinical review

---

### 3C. PLT Line (Platelet Assessment)

**Step 1: PLT count**
- <150 → Thrombocytopenia
  - 100–150: Mild; monitor
  - 50–100: Moderate; bleeding risk with trauma
  - 20–50: Significant risk; spontaneous bleeding possible
  - <20: Critical; spontaneous CNS/GI bleeding risk → URGENT CLINICAL ACTION
- >400 → Thrombocytosis
  - Reactive (infection, iron deficiency, post-splenectomy, inflammation) vs. primary (ET, CML)

**Step 2: PLT morphology indices**
- High MPV (>12.5 fL) + low PLT: Increased platelet production (ITP, hypersplenism, myeloproliferative) OR large platelet artifacts
- Low MPV (<7.5 fL) + low PLT: Aplastic anemia, chemotherapy suppression
- High PDW: Platelet anisocytosis → myeloproliferative disease, ITP
- High P-LCR: Large platelet fraction elevated → ITP, essential thrombocythemia
- High PCT (proportional to PLT × MPV): Elevated in thrombocytosis; very low in aplasia

**Step 3: PLT histogram**
- Right-shifted or broad peak: Large platelets (may include microerythrocytes, cell fragments)
- Peak cut off at right: Suspect microerythrocytes or RBC fragments counted as PLT → blood film required
- PLT-F vs PLT-I discordance (if available): PLT-F is more accurate at very low counts (<50×10³/µL) and when microparticles are present

**PLT Interference Table:**

| Finding | Suspect | Action |
|---------|---------|--------|
| PLT histogram peak cut right edge | Micro-RBC, schistocytes, RBC fragments | Blood film — urgent if PLT <50 |
| High MPV + PLT "normal" | Giant platelets (May-Hegglin, GPIb deficiency) | Blood film |
| PLT-I >> PLT-F | Platelet clumping | Rerun citrate tube; blood film |
| PLT very low + normal MPV | Aplasia vs. pseudothrombocytopenia | Citrate tube recount; blood film |

---

### 3D. Reticulocyte Assessment (RET Channel)

| Parameter | Low Indicates | High Indicates |
|-----------|--------------|----------------|
| RET% | Hypoproliferative anemia (IDA, aplasia, B12/folate early, renal disease) | Hemolysis, blood loss, treatment response (iron/B12) |
| IRF (immature reticulocyte fraction) | Low marrow output | Active erythropoiesis (post-treatment, hemolysis, blood loss) |
| RET-He | Iron-deficient erythropoiesis (<28 pg = functional iron deficiency even if stores normal) | Normal or iron replete |
| LFR/MFR/HFR | LFR = mature reticulocytes; HFR = youngest, RNA-richest reticulocytes | High HFR = active marrow response |

**RET-He Clinical Decision Tool:**
- RET-He <25 pg → Definitive functional iron deficiency → Iron supplementation
- RET-He 25–28 pg → Borderline → Ferritin + TSAT
- RET-He >28 pg + low RET% → Hypoproliferative; not iron-deficient

---

## PHASE 4 — FLAG INTERPRETATION ENGINE

### 4A. WBC Flags (WDF/WNR Channel)

| Flag | Triggered By | Clinical Meaning | Action |
|------|-------------|-----------------|--------|
| **Blasts?** | WDF cluster in blast zone | Possible leukemia, blast crisis | URGENT: Blood film + immediate clinician alert |
| **Abnormal Lympho/Blasts?** | WDF abnormal lymph zone + WPC | CLL, viral lymphocytosis, ALL, NHL | Blood film mandatory; oncology referral if confirmed |
| **Atypical Lympho?** | WDF upper lymph area | Reactive lymphocytes (EBV, CMV, viral infections) | Blood film; clinical correlation |
| **Left Shift?** | IG% elevated; immature NEUT in WDF | Sepsis, leukemoid reaction, CML | Blood film; clinical urgency depends on IG% level |
| **IG Present** | IG% >defined threshold | Left shift, CML, recovery | Blood film |
| **NRBC Present** | NRBC% >2% (user-defined) | Hemolysis, thalassemia, BM infiltration | Blood film; clinical review |
| **WBC Abn Scattergram** | Abnormal cluster pattern in WNR or WDF | Pathological cells, reagent failure, cold agglutinin | Verify scattergrams; blood film; check reagents if no pathology |
| **Diff WNR/WDF** | WBC-N vs WBC-D discordance >15% | NRBC interference, immature cells, cold agglutinin in WNR | Use WBC-D; verify WNR scattergram; blood film |
| **iRBC?** | RBC inclusions causing fluorescent signal in WNR | Malaria (Plasmodium spp.), Babesia, inclusions | IMMEDIATE: Thick/thin blood film for malaria parasites |
| **Low SFL WDF clusters** | Unstable Hb variants (Hb Mizuho, met-Hb) | Hemoglobinopathy | Blood film + Hb electrophoresis/HPLC |

### 4B. RBC Flags

| Flag | Triggered By | Clinical Meaning | Action |
|------|-------------|-----------------|--------|
| **Anisocytosis** | RDW elevated | Mixed cell sizes | Film; investigate cause |
| **Microcytosis** | MCV <80 fL | IDA, thalassemia, lead | Film + ferritin/iron studies |
| **Macrocytosis** | MCV >100 fL | B12/folate, liver, drugs | Film + B12/folate |
| **Hypochromia** | Low MCH/MCHC | IDA, thalassemia | Film + iron studies |
| **Fragments?** | Abnormal PLT histogram + low PLT | MAHA, TTP, DIC, HUS | URGENT blood film; ADAMTS13 if TTP suspected |
| **Turbidity/HGB Interference** | HGB elevated vs. expected from RBC/HCT | Lipemia, hemolysis, icterus | Spin sample; visual check; dilution correction |
| **MCHC >37** | Mathematical from HGB/HCT | Cold agglutinin, lipemia, hemolysis | Spin; warm sample; blood film |

### 4C. PLT Flags

| Flag | Triggered By | Clinical Meaning | Action |
|------|-------------|-----------------|--------|
| **Thrombocytopenia** | PLT <150 | See Phase 3C | Blood film to confirm; citrate tube if clumping suspected |
| **Giant PLT?** | Large events in PLT histogram | GPIb deficiency, MYH9-related disorder, ITP | Blood film; evaluate platelet morphology |
| **PLT Clumps?** | Satellite platelet events | EDTA-induced pseudothrombocytopenia | Rerun in citrate tube; blood film |
| **Abn PLT Distribution** | Abnormal histogram shape | Fragments counted as PLT, giant PLT, schistocytes | Blood film; clinical correlation |

### 4D. Scattergram Interpretation Rules

**WDF Scattergram (SSC vs SFL):**
- Tight NEUT cluster = normal; dispersed/shifted upper right = toxic granulation, reactive change
- Lymph cluster elevated SFL = reactive lymphocytes (viral)
- Blurred NEUT-MONO boundary = immature monocytes, monocytosis
- Extra cluster between NEUT and LYMPH = IG/blast population → BLOOD FILM
- Low SFL entire scattergram = abnormal Hb, reagent issue

**WNR Scattergram (SFL vs FSC):**
- WBC main cluster = upper right (normal)
- NRBC cloud = lower left area (small, dim fluorescence)
- Extra cloud between NRBC and WBC = immature erythroid precursors, blasts
- BASO cluster = upper left (large, high FSC)

**RET Scattergram (FSC vs SFL):**
- Dense cloud lower left = mature RBC
- Upper right scatter = reticulocytes (high RNA → high SFL)
- Very dense upper cloud = high reticulocyte activity (hemolysis/treatment response)
- Sparse scatter = hypoproliferative; check RET-He

---

## PHASE 5 — INSTRUMENT QC & MAINTENANCE ASSESSMENT

### 5A. QC Assessment Triggers

Suspect instrument issue (not patient pathology) when:

| Observation | Likely Instrument Issue | Action |
|-------------|------------------------|--------|
| MCHC consistently >37 g/dL across multiple samples | Cold agglutinin OR reagent problem OR calibration drift | Run QC; check reagent expiry; warm samples to 37°C; recalibrate |
| All parameters uniformly shifted from baseline | Calibration drift | Run IQC at all 3 levels; if fail → recalibrate with XN CAL |
| WBC normal but differential has systematic shift | WDF channel reagent exhaustion or reagent contamination | Check reagent levels; prime WDF reagent; rerun QC |
| PLT very low with no clinical correlation | PLT histogram cut-off artifact or clogged aperture | Check PLT-F vs PLT-I; check for clumping; clean aperture |
| HGB unexpectedly high vs. RBC/HCT | Lipemia, hemolysis, HbCO, turbid sample | Spin and visually inspect plasma; correct if needed |
| CV% >3% on WBC repeat | Precision problem | Run precision study; check sheath flow; call service |
| Carryover flags on sequential samples | High WBC or PLT previous sample causing carryover | Check carryover test result; increase wash cycles |
| Background count elevated | Contaminated sheath fluid or reagents | Run background check; replace reagents; decontaminate |
| [----] dashes on results | Analysis failure, insufficient volume, clog | Check sample volume; unclog; rerun |
| Scattergram clusters missing | Reagent exhaustion, reagent error, lysis failure | Check reagent levels; prime; replace; rerun |

### 5B. Daily QC Checklist (Remind user if QC not mentioned)

```
□ Run XN CHECK Level 1, 2, 3 before patient samples
□ Review Levey-Jennings charts — apply Westgard rules (1-2s warning; 1-3s reject; 2-2s reject; R-4s reject; 4-1s reject; 10x trend reject)
□ Check background count (WBC <0.2; RBC <0.02; PLT <10 acceptable)
□ Verify reagent levels (CELLPACK, STROMATOLYSER, FLUOROCELL, SULFOLYSER)
□ Check reagent expiry dates
□ Confirm temperature of analyser room (18–28°C optimal)
□ Verify sample: K₂EDTA tube, no clot, well-mixed, analyzed within 4–6 hours (RDW/MCV drift after 6h; MCHC after 8h)
```

### 5C. Calibration Trigger Criteria

Recalibrate when:
- QC mean shifts >2 SD from established mean on any parameter
- Bias exceeds CLSI EP9 allowable error for: WBC (>15%), RBC (>2.5%), HGB (>2%), HCT (>3%), PLT (>9%)
- After reagent lot change
- After major maintenance (aperture replacement, flow cell cleaning)
- When QC values show trend >5 consecutive points in same direction (Westgard)
- After power failure or instrument relocation

**Calibration Parameters Requiring XN CAL:** WBC, RBC, HGB, HCT, PLT, RET, RET-He  
**PLT-F requires XN CAL PF separately**

### 5D. Reagent Interference Table

| Preanalytical Condition | Parameters Affected | Correction |
|------------------------|--------------------|-----------| 
| Lipemia | HGB (falsely high), MCHC (falsely high) | Saline replacement method; dilution |
| Hemolysis in tube | HGB (high), RBC (low), PLT (low), MCHC (high) | Fresh sample; document; correct clinically |
| Icterus (bilirubin) | HGB (high at >100 µmol/L) | Correct with blank |
| Cold agglutinin | MCV (high), MCHC (high), RBC (falsely low), HCT (low) | Warm sample to 37°C for 15 min; rerun |
| EDTA-induced pseudothrombocytopenia | PLT (falsely low) | Rerun in sodium citrate tube; blood film |
| WBC clumping | WBC may be low; clog possible | Blood film; citrate rerun; gentle mixing |
| Delayed analysis (>6h RT) | MCV (increased), MCHC (decreased), MPV (increased), PLT-F drift | Note on report; fresh sample recommended |
| Malaria/parasite | WBC falsely elevated (WNR), iRBC? flag | iRBC? flag assessment; thick/thin film STAT |

---

## PHASE 6 — BLOOD FILM DECISION ENGINE

Apply the ICSH 2014 / BSH criteria for blood film review decisions.

### MANDATORY Blood Film (DO NOT DELAY):

- [ ] Blasts? flag present
- [ ] Abnormal lympho/blasts? flag present  
- [ ] iRBC? flag (malaria/parasite suspected — STAT thick film)
- [ ] WBC >30 or <2 × 10³/µL
- [ ] HGB <7 g/dL (severe anemia requiring morphology)
- [ ] PLT <50 × 10³/µL (critically low — confirm and morphology)
- [ ] NRBC >5% or NRBC# >1 × 10³/µL
- [ ] IG% >10%
- [ ] MCHC >37 g/dL (exclude cold agglutinin, spherocytes, artifact)
- [ ] Fragments? flag (TTP/DIC/MAHA screen)
- [ ] WBC Abn Scattergram with clinical concern

### RECOMMENDED Blood Film (within same session):

- [ ] WBC 10–30 × 10³/µL with clinical concern (unexplained leukocytosis)
- [ ] Atypical Lympho? flag
- [ ] IG% 2–10%
- [ ] RDW-CV >18% (marked anisocytosis)
- [ ] PLT 50–100 × 10³/µL
- [ ] PLT >600 × 10³/µL (thrombocytosis — reactive vs. primary?)
- [ ] New significant anemia (HGB drop >2 g/dL from previous)
- [ ] Abnormal PLT histogram (peak cut off right edge)
- [ ] Monocyte count >1.5 × 10³/µL (CMML exclusion)
- [ ] Macrocytosis MCV >110 fL
- [ ] Known hemoglobinopathy with acute change

### BLOOD FILM NOT REQUIRED (routine, confirm clinically):

- All parameters within reference range for age/sex
- No morphological flags
- QC in range
- Clinical context is routine screening

### Blood Film Report Expectations

When sending for film, specify these morphological targets in the film request note:

**RBC morphology:** Hypochromia, microcytes, macrocytes, target cells, sickle cells, spherocytes, elliptocytes, schistocytes, tear-drop cells, Howell-Jolly bodies, basophilic stippling, polychromasia, rouleaux

**WBC morphology:** Left shift (bands, metamyelocytes), toxic granulation, Döhle bodies, hypersegmented neutrophils, blasts, abnormal/reactive lymphocytes, monocyte morphology

**PLT morphology:** Giant platelets, platelet clumps, satellite platelets, megakaryocyte fragments

---

## PHASE 7 — CLINICAL CONCLUSION & ACTION PLAN FORMAT

After completing Phases 2–6, output the following structured report:

---

### 🔬 CBC ASSESSMENT REPORT — [Date/Sample ID]

**Patient:** Age ___ | Sex ___ | Clinical Context: ___  
**Instrument:** Sysmex XN-3100 | Module: ___  
**Sample Collected:** ___ | Analyzed: ___

---

#### SECTION 1: PARAMETER SUMMARY TABLE

| Parameter | Result | Reference Range | Status | Clinical Significance |
|-----------|--------|----------------|--------|----------------------|
| WBC | X.XX | 4.0–10.0 | ⬆️/✅/⬇️ | Brief note |
| [continue all parameters] | | | | |

*Status icons: ✅ Normal | ⬆️ High | ⬇️ Low | ⚠️ Borderline | 🚨 Critical*

---

#### SECTION 2: FLAG ANALYSIS

| Flag | Category | Interpretation | Urgency |
|------|----------|---------------|---------|
| [flag name] | WBC/RBC/PLT | [Clinical meaning] | URGENT / Routine / Monitor |

---

#### SECTION 3: SCATTERGRAM INTERPRETATION

**WDF:** [Describe cluster positions, any aberrant clusters, quality of separation]  
**WNR:** [NRBC presence, WBC cluster quality, BASO position]  
**RET:** [Reticulocyte cloud density, SFL distribution, evidence of active erythropoiesis]  
**RBC Histogram:** [Peak shape, position, bimodal features]  
**PLT Histogram:** [Peak shape, cutoff concerns]

---

#### SECTION 4: CLINICAL INTERPRETATION

**Primary Finding:** [e.g., Microcytic hypochromic anemia with thrombocytosis]  
**Differential Diagnosis (top 3):**
1. [Most likely] — supported by [parameters]
2. [Second possibility] — supported by [parameters]
3. [Third possibility] — needs exclusion by [test]

**Correlating Parameters:** [How parameters together support the interpretation]

---

#### SECTION 5: INSTRUMENT QC ASSESSMENT

| QC Item | Status | Action Needed |
|---------|--------|---------------|
| Daily IQC | Passed/Failed/Unknown | [Action] |
| Reagent levels | OK/Unknown | [Check if unknown] |
| Calibration currency | Current/Unknown | [Action] |
| Preanalytical issues | None/Suspected | [Detail] |
| Instrument maintenance | Up to date/Unknown | [Action] |

**Instrument Conclusion:** [e.g., "Results appear analytically reliable — no instrument flags present and QC described as passing. Proceed with clinical interpretation." OR "MCHC >37 g/dL — exclude cold agglutinin/lipemia before validating result."]

---

#### SECTION 6: BLOOD FILM DECISION

**Decision:** [MANDATORY NOW / RECOMMENDED / NOT REQUIRED]  
**Rationale:** [Which flags/parameters drove this decision]  
**Morphological Targets:** [List what to look for on the film]  
**Urgency:** [STAT (<2 hours) / Routine (same session) / Next session]

---

#### SECTION 7: ACTION PLAN

**IMMEDIATE (within 1 hour):**
- [ ] [Action item e.g., "Prepare STAT blood film — iRBC? flag present, exclude malaria"]

**SHORT-TERM (within same working day):**
- [ ] [Action item e.g., "Repeat PLT in citrate tube — clumping suspected"]
- [ ] [Action item e.g., "Request serum ferritin, TSAT — microcytic anemia with normal RDW"]

**FURTHER INVESTIGATIONS:**
- [ ] [Lab tests to request e.g., B12/folate, HPLC, reticulocyte count if not done, Coombs test]
- [ ] [Imaging or clinical if needed e.g., "Refer for hepatosplenomegaly assessment — monocytosis + splenomegaly pattern"]

**CLINICIAN NOTIFICATION:**
- [ ] [e.g., "CRITICAL VALUE: PLT 18 × 10³/µL — Notify clinician immediately per laboratory critical value policy"]

**INSTRUMENT ACTIONS:**
- [ ] [e.g., "Run QC all 3 levels before next patient batch — QC status unconfirmed"]
- [ ] [e.g., "Check reagent expiry — FLUOROCELL RET due for replacement"]

---

#### SECTION 8: BRIEF CONCLUSION

> *[2–3 sentence plain-language summary suitable for laboratory report comment or verbal communication to clinician. Example: "This CBC shows moderate microcytic hypochromic anemia with thrombocytosis and a normal WBC differential, most consistent with iron deficiency anemia in a 35-year-old female. No instrument flags detected. A blood film is recommended to assess hypochromia and microcytosis degree, and serum ferritin with iron studies should be requested to confirm diagnosis. Results are analytically reliable — QC status should be confirmed."]*

---

## PHASE 8 — WORKED EXAMPLE (APPLIED TO SAMPLE IMAGE)

**This section demonstrates how to apply the skill to a real result — use as template.**

**Patient context from uploaded image:**
- Sample: SYN-CBC-0001 | Date: 2099/01/01 | Instrument: Sysmex XN-3100 (SYNTHETIC — no real instrument or serial number)
- No age/sex provided in image → **Must request from user before full interpretation**

**Parameter Extract from image:**
- WBC: 17.10 ×10³/µL | RBC: 5.09 ×10⁶/µL | HGB: 15.3 g/dL | HCT: 44.3%
- MCV: 87.0 fL | MCH: 30.1 pg | MCHC: 34.5 g/dL | PLT: 519 ×10³/µL
- NEUT: 8.15/47.7% | LYMPH: 4.33/25.3% | MONO: 1.70/9.9% | EO: 2.10/12.3%
- BASO: 0.82/4.8% | IG: 2.04/11.9% | NRBC: 1.03 ×10³/µL (6.0%)
- RET: 1.16% | IRF: 24.6% | RET-He: 26.1 pg
- LFR: 75.4% | MFR: 21.0% | HFR: 3.6%

**Preliminary interpretation (age/sex unknown — for demonstration):**

*WBC elevation (17.10):* Leukocytosis. Differential shows relative neutrophilia, eosinophilia (12.3% = 2.10 ×10³/µL — elevated), basophilia (4.8% = 0.82 ×10³/µL — elevated), and **IG 11.9% (2.04 ×10³/µL — significantly elevated)**. Combined picture of eosinophilia + basophilia + elevated IG strongly suggests a **myeloproliferative disorder, particularly CML** — requires urgent blood film and BCR-ABL1 molecular testing.

*NRBC: 1.03 ×10³/µL (6.0%):* Significant NRBC — **blood film mandatory**. In context of possible CML, NRBCs may represent leukoerythroblastic reaction.

*RBC/HGB/HCT:* Within reference range (assuming adult). MCHC 34.5 — normal.

*PLT: 519 ×10³/µL:* Thrombocytosis. Reactive or primary (essential thrombocythemia vs. CML thrombocytosis).

*RET-He: 26.1 pg:* Below 28 pg → Indicates **functional iron deficiency** — possible concurrent iron-deficient erythropoiesis despite normal HGB. Consider ferritin.

*IRF: 24.6%:* Elevated — indicates active erythropoiesis with young reticulocytes being released, consistent with increased marrow output.

**Blood Film Decision:** MANDATORY — STAT  
**Targets:** Blasts, myeloid left shift, tear-drop cells, NRBC morphology, eosinophil morphology, basophil count, platelet morphology, any hypersegmented or dysplastic forms

**Immediate Action:**  
1. 🚨 STAT blood film — blast/myeloproliferative screen  
2. Notify clinician — pattern consistent with possible CML or myeloproliferative neoplasm  
3. Request: BCR-ABL1 FISH/PCR, bone marrow referral if not known diagnosis  
4. Request serum ferritin (RET-He 26.1 pg)  
5. Confirm QC was run today; if uncertain, run before reporting

---

## SKILL USAGE NOTES

### Trigger phrases that activate this skill:
- "Interpret this CBC result"
- "Is a blood film needed for this result?"
- "Check my Sysmex flags"
- "Assess my hematology result"
- "Troubleshoot my analyzer output"
- "What does this CBC mean for a [age] year old [male/female]?"
- Any uploaded image of a Sysmex XN printout (identifiable by scattergram layout, parameter format, or "XN series sysmex" header)

### Mandatory inputs:
1. Image of CBC result (uploaded photograph or scan)
2. Patient age (years)
3. Patient biological sex

### Optional but valuable:
- Clinical context/diagnosis
- Previous CBC for comparison
- QC status of the day
- Time from collection to analysis

### Output mode:
Default = Full report (Phases 2–8)  
If user asks "quick summary" = Section 8 only (Brief Conclusion) + Action Plan  
If user asks "just flags" = Section 2 (Flag Analysis) + Section 6 (Blood Film Decision) only  
If user asks "is my instrument working?" = Section 5 (QC Assessment) only

---

*EEHLSS / MedLabAI-LIS | Skill maintained by Echukwuka | Aligned to ICSH 2014, CLSI H20-A2, BSH 2009, ISO 15189:2022*  
*For use in clinical laboratory practice — results must be validated by a qualified Medical Laboratory Scientist*
