---
name: hb-interpreter
description: >
  Bio-Rad VARIANT II HPLC + Sebia Capillarys CZE Hemoglobinopathy Interpreter.
  Trigger when a user uploads an image of a Bio-Rad VARIANT II HPLC chromatogram
  (V2_BThal or HbA1c program), a Sebia Capillarys capillary electrophoresis pattern,
  or both together. Also trigger for: "interpret my Hb electrophoresis", "what does
  this HPLC show", "interpret my hemoglobin result", "is this thalassemia or iron
  deficiency", "assess my HbA2/HbF", or any request to correlate hemoglobin fractions
  with CBC indices for differential diagnosis. Outputs: technology interpretation →
  fraction analysis → CBC integration → differential diagnosis → condition classification
  (thalassemia, hemoglobin variant, IDA, ACD, sideroblastic) → confidence scoring →
  action plan. Asks for missing CBC data before completing diagnosis.
---

> **Research Purpose Only.** This material is a research and decision-support resource. It is not a validated or approved medical device, and its output must not be the sole basis for any clinical decision; all results require review by a qualified professional.

# Hemoglobinopathy Full-Spectrum Interpreter
### Bio-Rad VARIANT II HPLC + Sebia Capillarys 3 OCTA CZE

**Version:** 1.0 | **Instruments:** Bio-Rad VARIANT II (V2_BThal / V2_HbA1c) · Sebia Capillarys 2/3 OCTA  
**Standards:** ICSH · TIF (Thalassaemia International Federation) · BSH · WHO · ACMG  
**Brand:** EEHLSS / MedLabAI-LIS | Crimson #B71C1C · Navy #0D1B4B · Gold #F9A825

---

## PHASE 0 — INTAKE & MANDATORY DATA COLLECTION

Before interpreting, collect the following. If any item is missing, **ask the user before proceeding.** Do not generate a diagnosis without at least items 1–4.

### Required (ask if not provided):
1. **Image(s)** — Bio-Rad HPLC printout and/or Sebia CZE electrophoretogram (upload as photo/scan)
2. **Patient age** (years)
3. **Patient biological sex** (Male / Female)
4. **CBC indices** — request ALL of the following if not provided:
   - Hemoglobin (HGB) — g/dL or g/L (specify units)
   - RBC count — ×10⁶/µL
   - HCT/PCV — % or ratio
   - MCV — fL
   - MCH — pg
   - MCHC — g/dL or g/L
   - RDW-CV or RDW-SD — %
   - WBC and differential (if available)
   - PLT count

### Optional but strongly recommended:
- Serum ferritin (µg/L) and/or serum iron / TIBC / transferrin saturation
- Clinical context (ethnicity, family history of hemoglobinopathy, transfusion history, symptoms, current medications, pregnancy status)
- Previous Hb HPLC or electrophoresis results for comparison
- Reticulocyte count / RET-He (if available from Sysmex XN)
- Sickling test result (if done)
- Family studies (parents tested?)

> **Important:** HGB in g/L must be converted to g/dL (÷10) for reference range tables. Always confirm units.

---

## PHASE 1 — INSTRUMENT TECHNOLOGY PRIMER

*(Applied silently during interpretation; reference when explaining an unexpected result)*

### 1A. Bio-Rad VARIANT II HPLC — Principle

**Technology:** Cation-exchange High Performance Liquid Chromatography (CE-HPLC)  
**Program used:** V2_BThal (Beta-Thalassemia Short Program) — 6-minute run  
**Detection:** Absorbance at 415 nm (Soret band of hemoglobin); background correction at 690 nm

**How it works:**
1. Whole EDTA blood is automatically diluted and injected (~5 µL) onto an analytical ion-exchange cartridge
2. Two pumps deliver a programmed buffer gradient of increasing ionic strength and changing pH (Bis-Tris buffer system)
3. Hemoglobin fractions bind to the negatively charged cartridge surface; more positively charged Hb fractions elute later (higher retention times)
4. As ionic strength increases, Hb fractions are displaced in order of their ionic affinity: least ionically bound → elutes first (low RT); most bound → elutes last (high RT)
5. Each fraction is detected as an absorbance peak plotted against time (chromatogram)
6. Software integrates peak areas and calculates % of total area; assigns peaks to predefined windows based on expected retention times

**Bio-Rad V2_BThal Retention Time Windows:**

| Window / Peak Name | Retention Time (min) | Normal Hb Expected | Common Abnormal Hb in Window |
|-------------------|---------------------|-------------------|-------------------------------|
| Unknown (pre-integration) | <1.00 | — | Hb Bart's (γ4), Hb H (β4), bilirubin artefact, acetylated HbF |
| F (HbF) | ~1.10 | <2% adults | ↑ in β-thal, HPFH, δβ-thal, stress erythropoiesis |
| Unknown | ~1.21 | — | Various minor peaks; inspect chromatogram |
| P2 | ~1.33 | <4% | Post-translational HbA0 modification; degradation product |
| P3 | ~1.71 | <4% | Modified HbA0; also seen with HbH/Bart's; α-thal marker |
| Ao (HbA) | ~2.43 | 95–98% adults | Low in all hemoglobin disorders |
| A2 (HbA2) | ~3.65 | 2.0–3.3% | ↑β-thal trait (>3.5%); ↓IDA; co-elutes with HbE, HbC (false ↑) |
| S-window | ~4.41 | 0% | HbS; also Hb D-Punjab, Hb G-Coushata (same window, different RT) |
| C-window | ~5.10 | 0% | HbC; also Hb O-Arab, Hb E (HbE usually earlier in HPLC — see note) |
| D-window | ~4.05–4.30 | 0% | Hb D-Punjab, Hb G-Coushatta |

**Critical HPLC Interpretation Rules:**
- HPLC provides **presumptive** identification only — confirmation by alternative method (CZE, acid/alkaline electrophoresis, molecular) required for definitive diagnosis
- **HbE co-elutes with HbA2** on Bio-Rad Variant II V2_BThal program → apparent HbA2 >10% is virtually never true thalassemia; suspect HbE
- **Hb D-Punjab co-elutes with HbS** in S-window but sickling test is negative → differentiate by RT and CZE
- **Hb Lepore co-elutes with HbA2** on Bio-Rad; RT ~3.46 min; suspected when apparent HbA2 >5% with normal Hb electrophoresis
- Falsely **low HbA2** can occur with iron deficiency anemia — always interpret HbA2 in context of iron stores
- P3 peak elevation at RT ~1.71 min can suggest **alpha thalassemia trait**; normal range ~2–4%
- Hb Bart's (γ4) appears as a very early peak <1 min — may be missed if not looked for on chromatogram visual
- Total area <1,000,000 or >2,000,000 — consider dilution error or high-count sample; check calibration

**A2 Calibrated vs. Area %:**
- The *Calibrated Area %* is the quality-controlled reportable value for HbA2/HbF
- The *Area %* is the raw calculated % — used for peaks without calibration
- Values marked with `*` = outside expected ranges (instrument flag — not necessarily pathological; interpret in context)

---

### 1B. Sebia Capillarys 3 OCTA — Principle

**Technology:** Capillary Zone Electrophoresis (CZE) in free solution  
**Detection:** Direct absorbance at 415 nm

**How it works:**
1. Erythrocytes are lysed with Sebia haemolysing buffer; haemolysate injected into silica capillaries (25–100 µm internal diameter)
2. High voltage applied (~10–15 kV) in alkaline buffer
3. Hemoglobin molecules migrate through the capillary based on their electrophoretic mobility (charge-to-size ratio) in an alkaline pH environment
4. Electroosmotic flow (EOF) carries all Hb molecules toward the detector; migration speed differences between variants create separation
5. Each fraction is detected as a peak at 415 nm; position on x-axis (migration position in arbitrary units 0–300 or time) determines zone assignment
6. **Zone Z9 = HbA** — instrument standardizes HbA position as anchor point for zone assignment
7. Zones Z1–Z15 numbered from right (fastest migrating, most anionic = Z1) to left (slowest migrating, most cationic = Z15)

**Sebia CZE Zone Map (Capillarys 2/3):**

| Zone | Position | Normal Hb / Common Variants |
|------|----------|------------------------------|
| Z1 | Far right | HbA2', Hb Hope, fast variants |
| Z2 | | Rare variants |
| Z3 | | Rare variants |
| Z4 | | Hb J Baltimore, Hb J Oxford |
| Z5 | | **HbS** (diagnostic position) |
| Z6 | | Hb D-Punjab, Hb G variants (co-migrate with S in HPLC but separable here) |
| Z7 | | Hb Lepore (β/δ fusion), Hb G-Philadelphia |
| Z8 | | HbF (fetal hemoglobin) |
| Z(A) = Z9 | Centre | **HbA** (anchor zone) — always the largest peak in normal adult |
| Z10 / Z(A) area | | HbA (shaded/filled peak) |
| Z(F) | | HbF (when elevated) |
| Z(D) | | HbD-Punjab zone |
| Z(S) | | HbS zone |
| Z(E) | | HbE zone (unlike HPLC, CZE separates HbE from HbA2) |
| Z(A2) | ~position 235–245 | **HbA2** (separated from HbE and HbC on CZE) |
| Z(C) | Far left | **HbC** — "Hb C or Hb variant" label |
| Z14, Z15 | Leftmost | Slow variants; Hb H suspected if wide fraction 0.3–32% in Z15; Hb Bart's in Z12 |

**Critical CZE Interpretation Rules:**
- CZE **separates HbE from HbA2** (unlike HPLC) — major diagnostic advantage
- CZE **separates HbD from HbS** — major diagnostic advantage
- HbA2 values on CZE are systematically ~0.3–0.5% **higher** than HPLC; use method-specific reference ranges
- HbA2 reference range on CZE (Sebia Capillarys): **1.6–3.1%** (not 2.0–3.5% as used for HPLC)
- Hb C and HbA2 may overlap in Z(C)/Z(A2) boundary — when co-elution occurs, reported as "Hb C or Hb variant"
- HbA2 >10% on CZE: almost certainly co-migration of Hb Lepore or HbE — exclude with HPLC correlation
- Hb Bart's appears in Z12; Hb H appears in Z15 (wide fraction — flagged as "Hb H suspected")
- Absence of HbA on CZE (no Z9 peak) = major abnormality — requires HbA identification by mixing control experiment

---

## PHASE 2 — REFERENCE RANGES FOR HEMOGLOBIN FRACTIONS

### Adults (>18 years)

| Fraction | HPLC (Bio-Rad V2_BThal) | CZE (Sebia Capillarys) | Significance if Outside Range |
|---------|------------------------|----------------------|-------------------------------|
| HbA | 95.0–97.5% | 95.0–98.0% | Low in all hemoglobin disorders |
| HbA2 | 2.0–3.3% | 1.6–3.1% (note higher CZE values) | >3.5% HPLC / >3.2% CZE → β-thal trait |
| HbF | <2.0% | <2.0% | >2% → HPFH, δβ-thal, β-thal; stress erythropoiesis |
| HbS | 0% | 0% | Present → sickle cell trait (35–45%) or disease (>80%) |
| HbC | 0% | 0% | Present → HbC trait (~40%) or disease |
| HbE | 0% | 0% | Present → HbE trait, disease, or HbEβ-thal |
| HbD-Punjab | 0% | 0% | Present → HbD trait; S-window HPLC — distinguish by CZE/sickling |
| HbH | 0% | 0% | Present → α-thalassemia (Hb H disease: 3-gene deletion) |
| Hb Bart's | 0% | 0% | Present → α-thalassemia; Hb Bart's hydrops fetalis (4-gene del) |

### HbA2 Interpretation Rules (CRITICAL)

**Elevated HbA2 (>3.5% HPLC / >3.2% CZE) — Rule Out List:**

| HbA2 Value (HPLC) | Likely Diagnosis | Supporting CBC | Action |
|------------------|-----------------|---------------|--------|
| 3.5–7.0% | β-thalassemia trait | MCV <75, MCH <27, normal/low RBC, low Hb | Confirm by CZE; family study |
| 3.5–7.0% | β-thal trait + iron deficiency | MCV low, ferritin low | Treat IDA first, recheck HbA2 |
| >10% on HPLC | HbE co-elution | MCV low-normal, target cells on film | CZE mandatory to separate |
| >10% on CZE | Hb Lepore or HbE co-migration | — | HPLC correlation; molecular |
| 5–8% | Possible HbC/HbO-Arab co-migration with A2 | — | C-window check; CZE |
| 5–8% | Hb Lepore trait | Microcytic; Lepore RT ~3.46 min | CZE/electrophoresis |

**Low HbA2 (<2.0% HPLC / <1.6% CZE) — Rule Out List:**

| Scenario | Likely Cause |
|---------|--------------|
| Low HbA2 + microcytic hypochromic anemia | Iron deficiency — IDA suppresses HbA2 production; treat IDA and retest |
| Low HbA2 + microcytosis + normal iron | δ-thalassemia; Hb H disease |
| Low HbA2 + normal CBC | Normal variant; some ethnic groups; sideroblastic anemia |

---

## PHASE 3 — CBC INTEGRATION ENGINE

### 3A. Red Cell Index Analysis for Hemoglobinopathy Screen

**Step 1: Classify anemia if present**
- HGB <12 g/dL (F) / <13.5 g/dL (M) = anemia → classify by MCV
- MCV <80 fL → Microcytic → work up below
- MCV 80–100 fL → Normocytic → consider hemolytic, aplastic, chronic disease
- MCV >100 fL → Macrocytic → B12/folate; liver disease; unlikely pure hemoglobinopathy

**Step 2: Microcytic Anemia Differential — Discriminant Indices**

Apply these indices to distinguish the major causes of microcytic anemia:

| Index | Formula | β-thal Trait | IDA | ACD | Sideroblastic |
|-------|---------|-------------|-----|-----|--------------|
| **Mentzer Index** | MCV ÷ RBC | <13 → thal | >13 → IDA | Variable | Variable |
| **England & Fraser** | MCV − RBC − (5×HGB) − 3.4 | <0 → thal | >0 → IDA | — | — |
| **Green & King (GK) Index** | MCV² × RDW ÷ (HGB × 100) | <65 → thal | >65 → IDA | — | — |
| **RBC Morphology Index (RDWI)** | MCV × RDW ÷ RBC | <220 → thal | >220 → IDA | — | — |
| **Shine & Lal** | MCV² × MCH ÷ 100 | <1530 → thal | >1530 → IDA | — | — |

> These indices are **screening tools only** — none has 100% sensitivity/specificity. Always combine with Hb studies and iron parameters.

**Step 3: Typical CBC Profiles by Condition**

| Parameter | β-thal Trait | α-thal Trait (1–2 gene del) | IDA | ACD | Sideroblastic | HbE Trait | HbS Trait |
|-----------|-------------|----------------------------|-----|-----|--------------|-----------|-----------|
| HGB | Mildly low or N | Mildly low or N | Low | Low-mod | Low | N or slightly low | Usually N |
| MCV | Low (<75 fL) | Low-normal (70–80) | Low | N-low | Low-normal | Low (60–75 fL) | N |
| MCH | Low | Low-normal | Low | N-low | Low | Low | N |
| MCHC | N-low | N | Low | N | Variable | N-low | N |
| RDW | N or mildly ↑ | N | Markedly ↑ | N | ↑ (dimorphic) | N | N |
| RBC count | N or ↑ | N or ↑ | ↓ | ↓ | ↓ | N | N |
| Ferritin | N | N | ↓↓ | ↑ or N | ↑ or N | N | N |
| Serum Iron | N | N | ↓↓ | ↓ | ↑ or N | N | N |
| TIBC | N | N | ↑↑ | ↓ or N | N | N | N |
| Trf Sat | N | N | <15% | <20% | ↑ or N | N | N |
| HbA2 | >3.5% | N or low | Low-N | N-low | N | High (co-elutes on HPLC) | N |
| HbF | N or ↑1–5% | N | N | N | N | N | N |

### 3B. Discriminating IDA from β-Thalassemia Trait — Key Points

This is the most clinically important differential at the CBC level. Both present with microcytic hypochromic picture.

**Favours IDA over β-thalassemia trait:**
- RDW markedly elevated (>16%) — thalassemia trait usually has normal/near-normal RDW
- Mentzer Index >13
- Ferritin <12 µg/L (definitive iron deficiency)
- TIBC elevated (>70 µmol/L / >390 µg/dL)
- History: menorrhagia, inadequate dietary intake, GI blood loss, rapid growth, pregnancy
- HbA2 low or borderline (IDA suppresses HbA2 — can mask β-thalassemia trait)
- Response to iron therapy (improvement in MCV and HGB)

**Favours β-thalassemia trait over IDA:**
- RBC count elevated or high-normal despite low MCV/HGB
- RDW normal or only mildly elevated
- Mentzer Index <13
- HbA2 >3.5% on HPLC
- Normal or elevated ferritin
- Normal or low TIBC
- Family history of thalassemia; ethnicity (Mediterranean, Middle Eastern, South/Southeast Asian, West African)
- No response to iron therapy

**Compound β-thal trait + IDA (IMPORTANT):**
- IDA can **falsely lower HbA2** to normal range, masking β-thalassemia trait
- If CBC strongly suggests thalassemia morphology but HbA2 is borderline (3.0–3.5%), treat IDA first, then repeat Hb studies
- RDW markedly elevated + microcytosis + normal/borderline HbA2 + low ferritin = treat IDA and retest

### 3C. ACD (Anemia of Chronic Disease / Inflammation) Recognition

| Feature | Finding in ACD |
|---------|---------------|
| HGB | Mild-moderate reduction (90–120 g/L / 9–12 g/dL) |
| MCV | Normal or mildly low (normocytic or mildly microcytic) |
| RDW | Usually normal |
| Ferritin | Normal or ELEVATED (ferritin is acute phase reactant) |
| Serum iron | Low |
| TIBC | Low or normal (unlike IDA where TIBC is high) |
| Transferrin saturation | Low |
| Hepcidin | Elevated (not routinely measured but underlying mechanism) |
| Reticulocyte | Inappropriately low for degree of anemia |
| Clinical context | Active chronic illness: infection (TB, HIV, malaria), autoimmune disease, cancer, CKD |

**ACD vs IDA (when TIBC not available):**
- Ferritin <30 µg/L → IDA likely even in inflammation
- Ferritin 30–100 µg/L with clinical inflammation → ACD + possible concurrent IDA
- Ferritin >100 µg/L + low serum iron + normal/high TIBC → Pure ACD

### 3D. Sideroblastic Anemia Recognition

| Feature | Sideroblastic Anemia |
|---------|---------------------|
| CBC | Microcytic or normocytic anemia; often dimorphic RBC population on film |
| RDW | Elevated (dimorphic) |
| MCV | Variable (can be low, normal, or high in congenital form) |
| Serum iron | Elevated or normal |
| Ferritin | Elevated |
| TIBC | Normal or low |
| Transferrin saturation | Elevated |
| Hb studies | Usually normal HbA2/HbF; no hemoglobin variant |
| Film | Hypochromic microcytes + normochromic cells = dimorphic; Pappenheimer bodies |
| Bone marrow | Ring sideroblasts on Prussian blue stain (>15% = WHO criteria for refractory anemia with ring sideroblasts) |
| Causes | Congenital (X-linked ALAS2 mutation); acquired: alcohol, lead, drugs (isoniazid, chloramphenicol, pyrazinamide), MDS |
| Key clue | High ferritin/serum iron + microcytic/dimorphic anemia + normal Hb fractions |

---

## PHASE 4 — COMBINED HPLC + CZE INTERPRETATION ALGORITHM

### When both results available (same patient), apply this cross-platform logic:

**Step 1: Do the HbA2 values agree (after method adjustment)?**
- CZE HbA2 runs ~0.3–0.5% higher than HPLC
- If HPLC HbA2 = 3.6% and CZE HbA2 = 4.0% → concordant elevation → β-thalassemia trait confirmed
- If HPLC HbA2 >10% but CZE HbA2 = 4% → HPLC showing HbE co-elution → HbE + separate HbA2 4%

**Step 2: Does CZE identify a variant that HPLC placed in a shared window?**
- HPLC S-window + CZE Z5 → HbS confirmed
- HPLC S-window + CZE Z6 → Hb D-Punjab (not HbS; sickling test negative)
- HPLC C-window + CZE Z(C) → HbC confirmed
- HPLC C-window + CZE Z(E) → HbE confirmed (now separated from HbA2)
- "Hb C or Hb variant" on CZE Z(C) → correlate with HPLC C-window RT; if RT ~4.91 min → HbO-Arab; if ~5.18 min → HbC

**Step 3: Quantitative comparison of HbA percentage**
- Major discordance in HbA% between HPLC and CZE (>5% difference) = suspect undetected variant or analysis error
- Low HbA on both = significant Hb disorder present

**Step 4: HbF assessment**
- HbF elevated on both HPLC and CZE → concordant finding; interpret clinically
- HbF elevated on HPLC only → check for acetylated HbF peaks or post-translational modification

---

## PHASE 5 — CONDITION-SPECIFIC DIAGNOSIS ENGINE

### 5A. β-Thalassemia Spectrum

| Genotype | HbA2 | HbF | HbA | HbS/C/E | CBC | Diagnosis |
|----------|------|-----|-----|---------|-----|-----------|
| β-thal trait (β/β+) | >3.5% (HPLC) | N or ↑1–5% | ↓ slightly | 0% | Microcytic, normal RBC count | β-thalassemia carrier — does NOT cause significant clinical disease |
| β-thal intermedia | >3.5–5% | 20–40% | ↓↓ | 0% | Moderate anemia, microcytic | Significant disease; transfusion-independent mostly |
| β-thalassemia major (β0/β0) | Unmeasurable | 80–100% | 0% | 0% | Severe anemia; transfusion dependent | Cooley's anemia |
| δβ-thal trait | Low/normal A2 | ↑ (5–20%) | ↓ | 0% | Microcytic | δβ-thalassemia; A2 not elevated |
| HPFH | Low A2 | ↑↑ (15–30% het) | ↓ but less so | 0% | Normal or mild anemia | Hereditary persistence of HbF — often benign |

### 5B. α-Thalassemia Spectrum

| Genotype | HbA2 | HbF | HbA | Hb Bart's / HbH | CBC | Diagnosis |
|----------|------|-----|-----|----------------|-----|-----------|
| Silent carrier (--/αα) | N | N | N | 0–1% Bart's neonatal | Normal | Asymptomatic; may pass on to child |
| α-thal trait (--/αα or -α/-α) | Low-N | N | N | 0% adults | Mild microcytosis, normal Hb | α-thalassemia trait |
| Hb H disease (--/-α) | Low | N | ↓ | HbH 5–30% | Moderate microcytic anemia | Significant hemolysis; splenomegaly |
| Hb Bart's hydrops (-α/--) neonatal | — | — | 0% | Bart's >80% | Hydrops fetalis | Incompatible with life without intervention |
| P3 elevation on HPLC | Low-N | N | N | 0% | Mild microcytosis | **Suggestive of α-thalassemia** — α-globin gene analysis recommended |

### 5C. Structural Hemoglobin Variants

| Variant | HPLC Findings | CZE Findings | CBC Typical | Clinical |
|---------|--------------|-------------|-------------|---------|
| HbS trait | S-window 35–45%, HbA 55–60% | Z5 ~35–45% | Normal usually | Asymptomatic; sickling under extreme hypoxia |
| HbSS (sickle cell disease) | S-window >80%, HbA 0%, HbF variable | Z5 >80%, no HbA | Low HGB, high MCV (hemolysis), high bilirubin | Vaso-occlusive crises, hemolytic anemia, multi-organ |
| HbSβ-thalassemia | HbS 60–80%, HbA 0–20%, HbA2 >3.5% | S in Z5, elevated A2 | Microcytic anemia | Variable severity by β0 or β+ mutation |
| HbC trait | C-window 35–45%, HbA 55–60% | Z(C) ~35–45% | Normal CBC | Asymptomatic |
| HbCC disease | C-window >90%, HbA 0% | Z(C) dominant | Mild anemia, microcytic | Mild hemolytic anemia; splenomegaly |
| HbE trait | HPLC: apparent HbA2 ~25–30% (HbE+A2 co-elution), HbA 65–75% | CZE: HbE in Z(E) ~25–30%, HbA2 separate ~2–3% | Mild microcytosis; MCV 65–80 fL | Asymptomatic |
| HbEβ-thalassemia | HPLC: HbE+HbA2 co-elution, HbF elevated, HbA low | CZE: HbE >50%, HbF elevated, HbA low | Significant microcytic anemia | Clinically variable; can mimic β-thal major |
| HbD-Punjab | S-window on HPLC, ~35–45%, HbA 55–60% | Z6 (NOT Z5) — differentiates from HbS | Normal or mild | Sickling test NEGATIVE — key distinction from HbS |
| HbH disease | P3 elevation, possible pre-integration Hb H peak | Z15 wide fraction ("Hb H suspected") | Moderate anemia, microcytic | Hemolytic; Heinz bodies on film; splenomegaly |

---

## PHASE 6 — OUTPUT FORMAT: HEMOGLOBINOPATHY REPORT

Use this structured format for every interpretation:

---

### 🧬 HEMOGLOBINOPATHY ASSESSMENT REPORT

**Patient:** Age ___ | Sex ___ | Sample ID: ___  
**Instruments:** [Bio-Rad VARIANT II HPLC V2_BThal] + [Sebia Capillarys CZE] | Date: ___  
**Clinical Context:** ___

---

#### SECTION 1: HEMOGLOBIN FRACTION SUMMARY TABLE

| Fraction | HPLC Result | HPLC Reference | CZE Result | CZE Reference | Status | Notes |
|---------|------------|---------------|-----------|--------------|--------|-------|
| HbA | X% | 95–97.5% | X% | 95–98% | ✅/⚠️/🚨 | |
| HbA2 | X% | 2.0–3.3% | X% | 1.6–3.1% | | |
| HbF | X% | <2% | X% | <2% | | |
| HbS / variant | X% | 0% | X% | 0% | | |
| Unknown peaks | Describe RT + % | — | Zone + % | — | | |

---

#### SECTION 2: CBC INTEGRATION TABLE

| Parameter | Result | Reference (Age/Sex) | Status | Interpretation |
|-----------|--------|---------------------|--------|---------------|
| HGB | X g/dL | X–X | ✅/⬇️/🚨 | |
| RBC | X ×10⁶/µL | X–X | | |
| HCT | X% | X–X | | |
| MCV | X fL | 80–100 | | |
| MCH | X pg | 27–33 | | |
| MCHC | X g/dL | 32–36 | | |
| RDW-CV | X% | 11.5–14.5 | | |

**Discriminant Index Results:**

| Index | Calculated Value | Cut-off | Interpretation |
|-------|-----------------|---------|----------------|
| Mentzer Index (MCV÷RBC) | X | <13=thal; >13=IDA | |
| England & Fraser | X | <0=thal; >0=IDA | |
| Green & King | X | <65=thal; >65=IDA | |
| Shine & Lal | X | <1530=thal; >1530=IDA | |
| RDWI | X | <220=thal; >220=IDA | |

**Overall Index Consensus:** [e.g., "4 of 5 indices favour β-thalassemia trait"]

---

#### SECTION 3: CHROMATOGRAM / ELECTROPHORETOGRAM INTERPRETATION

**HPLC Chromatogram:**
- Baseline: [stable/unstable/note if artefacts present]
- HbA peak (RT ~2.43 min): [height, shape, normal/reduced]
- HbA2 peak (RT ~3.65 min): [% calibrated, any flags, shape]
- HbF peak (RT ~1.10 min): [% area, normal/elevated]
- P2/P3 peaks: [present/elevated — significance]
- S/C/D window peaks: [present or absent; if present: RT, area%, shape]
- Unknown peaks: [RT, area%, morphology — broad/narrow/sharp]
- Pre-integration peaks (<1 min): [present or absent — Hb Bart's/HbH alert]
- Total area: [acceptable/outside range — calibration concern if outside 1,000,000–2,000,000]

**CZE Electrophoretogram:**
- HbA zone (Z9): [dominant/reduced/absent]
- HbA2 zone Z(A2): [%, normal/elevated — note CZE reference 1.6–3.1%]
- HbF zone Z(F)/Z8: [%, normal/elevated]
- Variant peaks: [zone assigned, % — e.g., "peak in Z(C) at 27.9% — Hb C or Hb variant"]
- "Hb C or Hb variant" label: [present + %]
- Z15 (Hb H suspected): [present/absent]
- Z12 (Hb Bart's): [present/absent]
- Baseline and peak quality: [clean/artefacts present]

---

#### SECTION 4: DIFFERENTIAL DIAGNOSIS

**Primary diagnosis:** [Most likely condition with evidence]  
**Confidence level:** High / Moderate / Low  
**Evidence supporting:**
- HPLC findings:
- CZE findings:
- CBC indices and discriminant indices:
- Clinical context:

**Alternative diagnoses to exclude:**
1. [Condition] — excluded/still possible because [reason]
2. [Condition] — requires [test] to exclude
3. [Condition] — less likely because [reason]

**Conditions EXCLUDED by these results:**
- [List conditions ruled out and rationale]

---

#### SECTION 5: IRON STUDIES ASSESSMENT

*(Complete only when iron data available; otherwise note as pending)*

| Parameter | Result | Reference | Status | Interpretation |
|-----------|--------|-----------|--------|---------------|
| Serum Ferritin | X µg/L | M:30–300 / F:15–200 | | |
| Serum Iron | X µmol/L | M:11–29 / F:7–27 | | |
| TIBC | X µmol/L | 45–75 | | |
| Transferrin Sat | X% | M:20–50% / F:15–45% | | |
| RET-He (if available) | X pg | >28 | | |

**Iron Status Conclusion:** [Iron replete / Iron deficient / ACD pattern / Iron overload / Indeterminate — pending ferritin]

**Impact on Hb Study Interpretation:** [e.g., "Iron deficiency may be suppressing HbA2; β-thalassemia trait cannot be excluded — treat IDA and retest Hb studies in 3 months"]

---

#### SECTION 6: FINAL INTEGRATED DIAGNOSIS

**Primary Diagnosis:** [e.g., "β-Thalassemia Trait with concurrent Iron Deficiency Anemia"]  
**Genotype/Phenotype confidence:** [Definitive / Probable / Possible / Requires confirmation]  
**Pathophysiology summary:** [2–3 sentences explaining the condition in clinical terms]

---

#### SECTION 7: ACTION PLAN

**IMMEDIATE (within 48 hours):**
- [ ] [e.g., "Confirm HbC vs Hb O-Arab: perform sickling test and correlate HPLC C-window RT (HbC RT ~5.18 vs HbO-Arab RT ~4.91)"]
- [ ] [e.g., "CRITICAL: Hb H disease suspected — arrange haematology referral and blood film for Heinz bodies"]

**SHORT-TERM (within 2 weeks):**
- [ ] [e.g., "Request serum ferritin and TIBC — IDA masking HbA2 elevation possible"]
- [ ] [e.g., "Repeat Hb HPLC after 3 months of iron therapy to re-evaluate HbA2"]
- [ ] [e.g., "Blood film: look for target cells, microcytes, hypochromia, pencil cells, Pappenheimer bodies"]
- [ ] [e.g., "Sickling test if HbS not excluded"]

**CONFIRMATORY TESTING:**
- [ ] [Molecular testing for specific mutations — indication and gene targets]
- [ ] [α-globin gene analysis — if α-thalassemia suspected (P3 elevation, low MCV, normal HbA2)]
- [ ] [β-globin gene analysis — specify if required for genotyping compound heterozygotes]
- [ ] [Acid gel electrophoresis — if CZE equivocal for HbS vs HbD distinction]
- [ ] [Family studies — parents/siblings should be tested if pathogenic variant confirmed]

**CLINICAL REFERRAL:**
- [ ] [Haematology referral — indications and urgency]
- [ ] [Genetic counselling — if carrier state confirmed, especially if reproductive age]
- [ ] [Haematology-Obstetrics referral — if pregnant or planning pregnancy]
- [ ] [Paediatric haematology — if child or neonatal result]

**INSTRUMENT/QC ACTIONS:**
- [ ] [e.g., "Run HPLC calibrator; A2 calibrated result marked * — verify calibration is current"]
- [ ] [e.g., "Check Bio-Rad cartridge lot number — retention times drifting if P3 at unusual RT"]
- [ ] [e.g., "Confirm CZE control result within range before reporting"]

---

#### SECTION 8: BRIEF CLINICAL CONCLUSION

> *[3–4 sentence plain-language summary suitable for lab report comment or clinician communication. Should state: (1) what was found, (2) what condition it most likely represents, (3) key clinical implication, (4) most important next step.]*

---

## PHASE 7 — QC AND INSTRUMENT MAINTENANCE CHECKS

### Bio-Rad VARIANT II HPLC QC Assessment

| Issue | Indicator | Action |
|-------|-----------|--------|
| Retention time drift | Known variants eluting outside expected windows | Recalibrate; check column temperature; replace cartridge |
| HbA2 marked `*` | Calibrated value flagged by software | Verify calibration with Bio-Rad CDM calibrator; repeat run |
| Total area <1,000,000 | Under-dilution or weak haemolysate | Check sample concentration; repeat |
| Total area >2,000,000 | Over-dilution error or very high Hb count | Repeat with correct dilution |
| Unstable baseline | Reagent contamination; air bubbles; pump issue | Prime system; check buffers; call service if persists |
| P2/P3 spuriously elevated | Sample degradation; old sample | Request fresh sample; verify tube age (run within 5 days) |
| HbA2 falsely low | Iron deficiency; HbD Punjab co-elution | Request ferritin; correlate |
| HbA2 apparently high (>10%) | HbE co-elution — not true HbA2 elevation | Confirm with CZE which separates HbE from HbA2 |
| Pre-integration peak visible | Hb Bart's or Hb H — clinically significant | Flag and report; urgent haematology review |

### Sebia Capillarys CZE QC Assessment

| Issue | Indicator | Action |
|-------|-----------|--------|
| HbA zone (Z9) absent | No anchor for zone assignment — results unreliable | Perform 1:1 mixing with normal control; repeat |
| HbA2 and HbC not separating | Overlap at Z(A2)/Z(C) boundary | Report as combined %; note limitation; HPLC correlation |
| Hb H suspected (Z15 wide fraction) | Width >10 points, 0.3–32% | Clinically significant — report with comment |
| Hb Bart's (Z12 fitted) | Wide fraction with elevated % | Significant — neonatal screening concern |
| Controls out of range | Both normal and pathological controls must pass | Do not report patient results; troubleshoot system |
| Capillary-to-capillary variation | Results differ significantly between capillaries on same run | Flag; recalibrate; system maintenance |

---

## PHASE 8 — ETHNICITY/GEOGRAPHY CONTEXT ADJUSTMENTS

*(Apply silently when ethnicity/geography is provided)*

| Population | Common Variants to Consider | Priority Tests |
|-----------|---------------------------|----------------|
| West African (Nigeria, Ghana, etc.) | HbS (high frequency), HbC, β-thal, α-thal, HbSC compound | Sickling test; family history |
| North/East African | HbS, β-thal, HbC | Same as West African |
| Middle Eastern (Saudi Arabia, Gulf, Iran) | β-thalassemia trait, α-thal, HbD-Punjab, HbS, HbC | HbA2 elevation key; α-globin analysis |
| Mediterranean (Greece, Italy, Sardinia) | β-thalassemia (high frequency), α-thal, HbE | HbA2 elevation; family studies |
| South/Southeast Asian | HbE (very common), β-thal, α-thal, HbH disease | CZE critical — separates HbE from HbA2 |
| South Asian (India, Pakistan) | β-thal, α-thal, HbE, HbD-Punjab, HbS | Full panel + molecular |
| Northern European | β-thal rare; Hb variants uncommon | Standard workup; low pretest probability |

> For Saudi Arabia (patient location in this system): **β-thalassemia trait, Hb Lepore, HbD-Punjab, and HbS/HbC variants** are all relevant. CBAHI guidelines require confirmation of all hemoglobinopathy diagnoses before issuing report. SFDA-registered reagents must be used.

---

## SKILL USAGE NOTES

### Mandatory inputs to begin diagnosis:
1. Image of HPLC printout and/or CZE electrophoretogram
2. Patient age (years)
3. Patient biological sex
4. CBC indices: HGB, RBC, HCT, MCV, MCH, MCHC, RDW

### Additional inputs for complete diagnosis:
- Serum ferritin (essential for IDA/thalassemia distinction)
- Clinical context and ethnicity
- Both HPLC and CZE when available (cross-platform confirms variants)

### Output modes:
- Default = Full 8-section report (Phases 2–7)
- "Quick summary" = Section 8 (Brief Conclusion) + Section 7 (Action Plan) only
- "Just Hb fractions" = Sections 1 + 3 only
- "Iron status only" = Section 5 only
- "QC check" = Phase 7 only

### Trigger phrases:
- "Interpret my Hb electrophoresis"
- "Interpret this HPLC result"
- "Is this thalassemia or iron deficiency?"
- "Assess my hemoglobin fractions"
- "Interpret my Sebia result"
- Any upload of Bio-Rad or Sebia printout image

---

*EEHLSS / MedLabAI-LIS | Maintained by Echukwuka | Aligned to TIF, BSH, ICSH, ACMG, ISO 15189:2022, CBAHI*  
*All results require validation by a qualified Medical Laboratory Scientist. Molecular confirmation required for definitive hemoglobinopathy diagnosis.*
