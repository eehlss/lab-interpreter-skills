---
name: chemistry-hormone-interpreter
description: >
  Siemens Atellica CH/IM + Roche Cobas Clinical Chemistry & Hormone Interpreter v2.0.
  Trigger for any chemistry or hormone panel result interpretation. Covers renal,
  liver, electrolytes, metabolic, iron, thyroid (TSH/FT3/FT4), adrenal (cortisol/
  ACTH/aldosterone), reproductive & fertility hormones (LH/FSH/E2/progesterone/
  testosterone/prolactin/AMH), cardiac function (hs-troponin/BNP/NT-proBNP/CK/
  CK-MB/myoglobin/D-Dimer), bone health (PTH/Vitamin D/P1NP/CTX/osteocalcin),
  haematinics (vitamin B12/folate/RBC folate/homocysteine/MMA/holotranscobalamin),
  inflammatory markers, lipids, and tumour markers. Critical value flagging →
  parameter table → organ system assessment → differential diagnosis → action plan.
  Always asks for missing age, sex, cycle day, sample time, fasting status.
---

> **Research Purpose Only.** This material is a research and decision-support resource. It is not a validated or approved medical device, and its output must not be the sole basis for any clinical decision; all results require review by a qualified professional.

# Clinical Chemistry & Hormone Panel Interpreter — v2.0
### Siemens Atellica CH/IM · Roche Cobas · Multi-Platform Compatible

**Version:** 2.0 | **Updated:** April 2026
**Standards:** IFCC · CLSI · ISO 15189:2022 · JCAHO NPSG.02.03.01 · CBAHI · SFDA · ESC 2023 · Endocrine Society · IOF · NICE
**Brand:** EEHLSS / MedLabAI-LIS | Crimson #B71C1C · Navy #0D1B4B · Gold #F9A825

---

## PHASE 0 — INTAKE & MANDATORY DATA COLLECTION

Ask for anything missing before interpreting.

**Required:**
1. Image or typed values from the result panel
2. Patient age (years) and biological sex (Male/Female)
3. Clinical context (e.g., "routine screen", "cardiac chest pain", "thyroid symptoms", "infertility", "bone pain", "fatigue", "adrenal disease suspicion")

**Always ask if not provided (hormone-specific):**
- Menstrual cycle day (female) — essential for LH, FSH, E2, progesterone
- Time of blood draw — cortisol/ACTH/testosterone must be 08:00–09:00 for reference range to apply
- Fasting status — glucose, lipids, triglycerides, insulin, cortisol stimulation tests
- Pregnancy status — transforms reference ranges for hormones and many chemistry tests
- Contraceptive/HRT use — suppresses LH/FSH, raises SHBG, alters free androgens
- Biotin supplementation >5mg/day — causes false TSH (↓), FT4 (↑), troponin, vitamin D on streptavidin-based assays
- Current medications — metformin (↓B12), PPIs/H2 blockers (↓B12), antiepileptics (↓folate/↓Vit D), steroids (↑glucose/↓cortisol response), antipsychotics (↑prolactin), statins, ACEi, ARBs, diuretics, amiodarone (↑T4/↓T3)

> **Unit conversions:** Cortisol: nmol/L ÷ 27.6 = µg/dL | Vitamin D: nmol/L ÷ 2.496 = ng/mL | B12: pmol/L × 1.355 = pg/mL | Folate: nmol/L × 0.441 = ng/mL | T4: nmol/L × 0.078 = µg/dL

---

## PHASE 1 — INSTRUMENT TECHNOLOGY PRIMER
*(Apply silently; reference when explaining unexpected results)*

### 1A. Siemens Atellica CH — Chemistry Module

| Technology | Key Analytes | Principle |
|-----------|-------------|-----------|
| Photometry (endpoint/kinetic) | LFTs, glucose, creatinine, urea, uric acid, cholesterol, TG, CK, LDH, ALP, bilirubin | Chromogenic reaction; absorbance at specific λ |
| Turbidimetry / PETINIA | CRP, hs-CRP, immunoglobulins, transferrin, HbA1c (turbidimetric inhibition), RF | Immune complex light scatter |
| IMT (Ion-Selective Electrode) | Na⁺, K⁺, Cl⁻ | Indirect ISE; automated calibration |
| Enzymatic colorimetric | Fe, TIBC, Mg, phosphate, calcium, enzymatic creatinine | Direct enzymatic colour reactions |
| EMIT | TDM (cyclosporin, tacrolimus), drugs of abuse | Competitive homogeneous immunoassay |

### 1B. Siemens Atellica IM — Immunoassay Module

| Sandwich (large molecules) | TSH, LH, FSH, prolactin, insulin, PTH(intact), NT-proBNP, BNP, hs-TnI, AFP, CEA, CA-125, CA19-9, PSA, ferritin, B12, folate |
|---------------------------|---|
| Competitive (small molecules) | FT4, FT3, cortisol, testosterone, estradiol, progesterone, DHEA-S, 25-OH Vit D, ACTH, aldosterone, Total T4, Total T3 |
| Acridinium ester label | All IM assays — photon emission on oxidation; photomultiplier detection |

### 1C. Roche Cobas — ECLIA

- Ruthenium(II) label + streptavidin magnetic microparticles; electrochemical voltage triggers luminescence
- Superior sensitivity: 3rd/4th gen TSH, hs-TnT, 25-OH Vit D, folate, B12, AMH
- Cobas e-series = immunoassay; Cobas c-series = chemistry
- Prozone risk at very high concentrations (beta-hCG in molar pregnancy) — auto-dilution protocols apply

### 1D. Interference Matrix

| Interferent | Analytes Affected | Effect | Action |
|------------|------------------|--------|--------|
| Haemolysis (H) | K⁺, AST, LDH, cortisol (some methods) | K⁺/AST falsely elevated | Reject if H>2+; request fresh sample |
| Lipaemia (L) | Most photometric assays | Turbidity elevates absorbance | Ultracentrifuge; blanking methods |
| Icterus (I) | ALT, AST, albumin, Jaffé creatinine | Bilirubin absorbs at reaction wavelength | Enzymatic creatinine; note if I>2+ |
| Biotin (>5mg/day) | TSH (↓), FT4 (↑), troponin, 25-OH Vit D, folate, B12, PTH, prolactin, LH, FSH, hCG | Streptavidin competition — signals disrupted | 24h washout; repeat |
| Heterophile antibodies (HAMA) | Any sandwich assay: TSH, troponin, PSA, prolactin, BNP | False positive or negative | Dilution series; blocking tubes; alternate platform |
| Macro-prolactin | Prolactin | Spuriously elevated (IgG-PRL complex) | PEG precipitation; <40% recovery = macro-PRL (benign) |
| High B12 interference | Folate (competitive binding assay) | Falsely normal folate if B12 very high | Use RBC folate for definitive stores |

---

## PHASE 2 — REFERENCE RANGES BY ORGAN SYSTEM

### 2A. Renal Function

| Analyte | Male | Female | Units | Critical Low | Critical High |
|---------|------|--------|-------|-------------|--------------|
| Creatinine | 62–106 | 44–80 | µmol/L | <27 | >884 🚨 |
| eGFR (CKD-EPI) | ≥90 = normal | ≥90 = normal | mL/min/1.73m² | — | — |
| Urea | 2.5–7.1 | 2.5–7.1 | mmol/L | — | >35.7 🚨 |
| Uric acid | 202–416 | 143–339 | µmol/L | — | >595 |
| Na⁺ | 136–145 | 136–145 | mmol/L | <120 🚨 | >158 🚨 |
| K⁺ | 3.5–5.1 | 3.5–5.1 | mmol/L | <2.8 🚨 | >6.2 🚨 |
| Cl⁻ | 98–107 | 98–107 | mmol/L | <70 🚨 | >120 🚨 |
| HCO₃⁻ | 22–29 | 22–29 | mmol/L | <10 🚨 | >40 🚨 |
| Phosphate | 0.87–1.45 | 0.87–1.45 | mmol/L | <0.3 🚨 | >2.9 |
| Magnesium | 0.66–1.07 | 0.66–1.07 | mmol/L | <0.4 🚨 | >2.1 🚨 |

**CKD Staging (KDIGO 2022):** G1 ≥90 (normal) · G2 60–89 (mildly reduced) · G3a 45–59 (mildly-moderately reduced — nephrology review) · G3b 30–44 (moderately-severely reduced — nephrology essential) · G4 15–29 (severely reduced — RRT planning) · G5 <15 (kidney failure — dialysis/transplant)

**AKI definition:** Cr rise >26.5 µmol/L in 48h OR >1.5× baseline within 7 days
**Urea:Cr ratio** (both mmol/L): >100 = pre-renal · 50–100 = indeterminate · <50 = intrinsic

### 2B. Liver Function

| Analyte | Male | Female | Units | Critical High |
|---------|------|--------|-------|--------------|
| Total Bilirubin | 3.4–17.1 | 3.4–17.1 | µmol/L | >342 🚨 |
| Direct Bilirubin | 0–5 | 0–5 | µmol/L | >170 🚨 |
| Indirect Bilirubin | 3.4–12 | 3.4–12 | µmol/L | — |
| AST | 10–40 | 10–35 | U/L | >1000 🚨 |
| ALT | 7–56 | 7–45 | U/L | >1000 🚨 |
| ALP | 44–147 | 35–104 | U/L | >1500 |
| GGT | 8–61 | 5–36 | U/L | >300 |
| Total Protein | 60–83 | 60–83 | g/L | <40 🚨 |
| Albumin | 35–52 | 35–52 | g/L | <20 🚨 |
| LDH | 135–225 | 135–214 | U/L | — |
| Ammonia | 9–33 | 9–33 | µmol/L | >55 🚨 |

**Liver Injury Patterns:**

| Pattern | ALT | AST | ALP | GGT | Bilirubin | Cause |
|---------|-----|-----|-----|-----|-----------|-------|
| Hepatocellular | ↑↑↑ | ↑↑↑ | N/↑ | ↑ | Variable | Viral hepatitis, NAFLD, alcohol, drugs, ischaemia |
| Cholestatic | N/↑ | N/↑ | ↑↑↑ | ↑↑↑ | ↑↑ direct | Biliary obstruction, PBC, PSC, drug-induced |
| Mixed | ↑↑ | ↑↑ | ↑↑ | ↑↑ | ↑ | Drug reaction, infiltrative, pregnancy |
| Synthetic failure | N/↓ | N | N/↑ | ↑ | ↑ direct | Cirrhosis, ALF — check INR + albumin urgently |
| Isolated ↑GGT | N | N | N | ↑↑ | N | Alcohol, enzyme induction, fatty liver |
| ↑ALP + normal GGT | N | N | ↑↑ | N | N | Bone origin — check BSALP/P1NP |
| AST:ALT >2:1 | ↑ | ↑↑ | ↑ | ↑↑↑ | Var | Alcoholic hepatitis (de Ritis); also check CK |

**R-ratio:** (ALT÷ALT_ULN) ÷ (ALP÷ALP_ULN) — ≥5=hepatocellular · 2–5=mixed · ≤2=cholestatic
**Synthetic failure markers:** Albumin <28 + Bilirubin >51 + INR >1.5 = decompensated → urgent hepatology referral

### 2C. Glucose, HbA1c & Metabolic Panel

| Analyte | Reference | Units | Critical |
|---------|-----------|-------|---------|
| Fasting glucose | 3.9–5.6 | mmol/L | <2.2 🚨 / >27.8 🚨 |
| Random glucose | <7.8 | mmol/L | <2.2 🚨 / >27.8 🚨 |
| HbA1c | <42 normal; 42–47 prediabetes; ≥48 diabetes | mmol/mol | — |
| HbA1c (%) | <6.0% normal; 6.0–6.4% prediabetes; ≥6.5% diabetes | % | — |
| Insulin (fasting) | 17.8–173 | pmol/L | — |
| C-peptide | 0.37–1.47 | nmol/L | — |
| Total Cholesterol | <5.2 desirable | mmol/L | >13 |
| LDL-C | <3.4 desirable; <2.6 moderate CV risk; <1.8 high CV risk; <1.4 very high | mmol/L | — |
| HDL-C | M:>1.0; F:>1.2 | mmol/L | <0.75 🚨 |
| Triglycerides (fasting) | <1.7 normal; >5.6 very high; >11.3 pancreatitis | mmol/L | >11.3 🚨 |
| Apolipoprotein B (ApoB) | M:<1.0; F:<0.9 optimal | g/L | >1.4 = high atherogenic risk |
| Apolipoprotein A1 | M:1.0–1.6; F:1.0–1.9 | g/L | <0.9 = low HDL capacity |
| Lipoprotein(a) [Lp(a)] | <125 nmol/L (<50 mg/dL) | nmol/L | >125 = high independent CV risk |

**HbA1c Note:** Unreliable in haemolytic anaemia, haemoglobinopathies, recent transfusion, severe IDA. Use fructosamine or plasma glucose average instead. In thalassaemia/HbE: use Bio-Rad HPLC or boronate affinity method.

### 2D. Iron Studies

| Analyte | Male | Female | Units |
|---------|------|--------|-------|
| Serum Iron | 9.0–30.4 | 7.2–25.9 | µmol/L |
| TIBC | 44.8–76.1 | 44.8–76.1 | µmol/L |
| Transferrin Saturation | 20–50% | 15–45% | % |
| Ferritin | 30–300 | 15–200 | µg/L |
| Transferrin | 2.0–3.6 | 2.0–3.6 | g/L |
| sTfR | 2.2–5.0 | 1.9–4.4 | mg/L |

**Iron Pattern Table:** IDA: ↓↓Ferritin + ↓↓Fe + ↑↑TIBC + ↓↓Trf Sat (<16%) | ACD: ↑/N Ferritin + ↓Fe + ↓/N TIBC + low-normal Trf Sat | Haemochromatosis: ↑↑↑Ferritin + ↑↑Fe + ↓TIBC + ↑↑Trf Sat (>45%) | Haemolysis: ↑/N Ferritin + ↑Fe + N TIBC + ↑Trf Sat

### 2E. Thyroid Function Panel — COMPREHENSIVE

| Analyte | Reference | Units | Critical Low | Critical High |
|---------|-----------|-------|-------------|--------------|
| TSH (3rd/4th gen) | 0.27–4.20 | mIU/L | <0.03 🚨 | >100 🚨 |
| Free T4 (FT4) | 12–22 | pmol/L | <6 🚨 | >77 🚨 |
| Free T3 (FT3) | 3.1–6.8 | pmol/L | <2.0 | >20 🚨 |
| Total T4 | 66–181 | nmol/L | — | — |
| Total T3 | 1.3–3.1 | nmol/L | — | — |
| Reverse T3 (rT3) | 0.14–0.54 | nmol/L | — | — |
| Anti-TPO | <34 | IU/mL | — | >500 (significant autoimmune) |
| Anti-thyroglobulin | <115 | IU/mL | — | — |
| TSH receptor Ab (TRAb) | <1.75 | IU/L | — | >10 (active Graves') |
| Thyroglobulin | <10 (euthyroid); <1 post-thyroidectomy | µg/L | — | — |

**TSH Algorithm:**

| TSH | FT4 | FT3 | Interpretation | Action |
|-----|-----|-----|---------------|--------|
| Low | High | High | Primary hyperthyroidism — overt | TRAb; thyroid USS; refer endocrinology |
| Low | Normal | Normal-high | Subclinical hyperthyroidism OR NTI/drugs | Repeat 3m; exclude amiodarone/steroids |
| Low | Low | Low | Central hypothyroidism | MRI pituitary; assess all pituitary axes |
| High | Low | Low | Primary hypothyroidism — overt | Anti-TPO; start levothyroxine |
| High | Normal | Normal | Subclinical hypothyroidism | Anti-TPO; treat if TSH>10 or symptomatic/pregnant |
| Normal | Low | Low | Non-thyroidal illness (NTI) / sick euthyroid | Repeat when clinically recovered |
| Normal | High | High | Thyroid hormone resistance OR assay interference | Biotin check; heterophile Ab test |

**Pregnancy Thyroid Ranges:**

| Trimester | TSH (mIU/L) | FT4 (pmol/L) |
|-----------|------------|-------------|
| 1st (0–12w) | 0.1–2.5 | 12–19 |
| 2nd (13–26w) | 0.2–3.0 | 10–16 |
| 3rd (27–40w) | 0.3–3.5 | 8–14 |

**Drug Effects on TFTs:** Amiodarone: ↑T4 + ↓T3 (inhibits conversion) | Steroids: ↓TSH | Heparin: falsely ↑FT4 (displaces from TBG) | Oestrogens: ↑TBG → ↑Total T4/T3, FT4 normal | Lithium: hypothyroidism risk | Phenytoin: ↓total T4 (displaces TBG) | Metformin: modest ↓TSH

### 2F. Adrenal Function Panel — COMPREHENSIVE

| Analyte | Reference | Units | Critical |
|---------|-----------|-------|---------|
| Cortisol (08:00–09:00) | 171–536 | nmol/L | <83 (adrenal crisis risk) 🚨 |
| Cortisol (16:00–18:00) | 64–327 | nmol/L | — |
| Cortisol (midnight serum) | <138 | nmol/L | >207 = loss of diurnal rhythm |
| Cortisol (midnight salivary) | <5.3 | nmol/L | >5.3 = Cushing's screen positive |
| Post-1mg DST (08:00) | <50 nmol/L = normal suppression | nmol/L | >50 = screen positive for Cushing's |
| Short Synacthen (30 min peak) | >450 nmol/L = adequate | nmol/L | <450 = adrenal insufficiency |
| ACTH (plasma 08:00–09:00) | 7.2–63.3 pg/mL (1.6–13.9 pmol/L) | pg/mL | — |
| Aldosterone (supine) | 100–500 | pmol/L | — |
| Aldosterone (upright) | 100–800 | pmol/L | — |
| Renin (active, supine) | 5.1–46.1 | mU/L | — |
| Aldosterone:Renin Ratio (ARR) | <750 (pmol/L : mU/L) | — | >750 = primary hyperaldosteronism screen positive |
| DHEA-S (F 18–50y) | 1.3–8.4 | µmol/L | — |
| DHEA-S (M 18–50y) | 2.4–11.7 | µmol/L | — |
| 24h Urine Cortisol (UFC) | <166 | nmol/24h | >3× ULN = Cushing's probable |
| 17-OH Progesterone (basal) | F follicular: <6; M:<7.5 | nmol/L | >30 = CAH screen |

**Cortisol/ACTH Interpretation Matrix:**

| Cortisol | ACTH | Interpretation | Confirmation |
|---------|------|---------------|-------------|
| ↓ | ↑↑ | Primary adrenal insufficiency (Addison's) | SST; 21-hydroxylase Ab; adrenal CT |
| ↓ | ↓ or N | Secondary adrenal insufficiency (pituitary) | MRI pituitary; other pituitary hormone axes |
| ↑ | ↓ | ACTH-independent Cushing's (adrenal adenoma/carcinoma) | Adrenal CT/MRI |
| ↑ | ↑ | ACTH-dependent Cushing's (Cushing's disease or ectopic ACTH) | MRI pituitary; CRH test; IPSS |
| Fails to suppress on DST | Variable | Cushing's syndrome screen positive | 48h high-dose DST; UFC; further workup |

**Cushing's Screening Algorithm:** First-line tests (≥2 needed): (1) 1mg overnight DST — cortisol >50 nmol/L = screen positive; (2) 24h UFC >3× ULN; (3) midnight salivary cortisol >5.3 nmol/L. If screen positive → refer endocrinology for second-line testing.

### 2G. Reproductive & Fertility Hormones — COMPREHENSIVE

#### Female Phase-Specific Reference Ranges:

| Analyte | Follicular | Ovulatory | Luteal | Post-Menopause | Units |
|---------|-----------|----------|--------|---------------|-------|
| LH | 2.4–12.6 | 14.0–95.6 | 1.0–11.4 | 7.7–58.5 | IU/L |
| FSH | 3.5–12.5 | 4.7–21.5 | 1.7–7.7 | 25.8–134.8 | IU/L |
| Estradiol (E2) | 46–607 | 315–1828 | 161–774 | <201 | pmol/L |
| Progesterone | <3.2 | Variable | 9.5–76.4 | <3.2 | nmol/L |
| Testosterone | 0.3–1.7 | — | — | 0.1–1.4 | nmol/L |
| SHBG | 32.4–128 | — | — | 17–90 | nmol/L |
| Prolactin | 102–496 | — | — | 102–496 | mIU/L |
| DHEA-S | 1.3–8.4 (18–50y) | — | — | 0.3–3.6 | µmol/L |
| AMH | 1.0–3.5 (25–35y); >1.0 good reserve; 0.5–1.0 low-normal; <0.5 poor | — cycle-independent — | ng/mL |
| Inhibin B | 23–257 (follicular D2–5) | — | — | <17 | pg/mL |
| Free Androgen Index (FAI) | Total testosterone (nmol/L) × 100 ÷ SHBG (nmol/L); Normal female <5 |
| Beta-hCG | <5 | — | — | <5 | IU/L |

#### Male Reference Ranges:

| Analyte | Reference | Units |
|---------|-----------|-------|
| LH | 1.7–8.6 | IU/L |
| FSH | 1.5–12.4 | IU/L |
| Total Testosterone (08:00 sample) | 9.9–27.8 | nmol/L |
| Free Testosterone (calculated) | 0.22–0.64 | nmol/L |
| Estradiol (E2) | <146 | pmol/L |
| SHBG | 16.5–55.9 | nmol/L |
| Prolactin | 86–324 | mIU/L |
| Inhibin B | 80–400 | pg/mL |

**Reproductive Hormone Interpretation Framework:**

| Pattern | Finding | Diagnosis | Action |
|---------|---------|-----------|--------|
| LH ↑↑ + FSH ↑↑ + E2 ↓↓ (F <40y) | High gonadotrophins + low E2 | Premature Ovarian Insufficiency (POI) | Anti-TPO; chromosomes (fragile X); bone DEXA; HRT |
| LH ↑↑ + FSH ↑↑ (F ≥45y) | Menopausal gonadotrophin levels | Menopause | Clinical assessment; DEXA |
| LH:FSH >2:1 + ↑testosterone + FAI >5 + ↓SHBG | Hyperandrogenism + gonadotrophin imbalance | PCOS | Pelvic USS (AFC); insulin/glucose; lipids |
| FSH ↑ + AMH ↓ + Inhibin B ↓ (reproductive age) | Reduced ovarian reserve | DOR | Fertility specialist; AFC on USS |
| PRL >600 mIU/L | Hyperprolactinaemia | Prolactinoma vs drug-induced vs macro-PRL | PEG precipitation first; then MRI pituitary; medication review |
| LH ↓ + FSH ↓ + E2 ↓ (or T ↓ in male) | Hypogonadotrophic hypogonadism | Secondary hypogonadism — pituitary/hypothalamic | MRI pituitary; assess GH/ACTH/TSH; Kallmann if anosmia |
| Progesterone <30 nmol/L (D21 or D[cycle-7]) | Sub-optimal luteal | Anovulation or luteal phase defect | Prolactin; thyroid; PCOS screen; repeat timing |
| Progesterone ≥30 nmol/L (mid-luteal) | Ovulation confirmed | — | Reassure; if conception issues: semen analysis + tubotomy |
| T ↓ (male) + LH ↓ or N | Secondary hypogonadism | Pituitary pathology / haemochromatosis | MRI pituitary; ferritin; iron sat |
| T ↓ (male) + LH ↑ | Primary testicular failure | Klinefelter's or other | Karyotype; testicular USS; semen analysis |
| Estradiol ↑↑ (male) + normal or ↓ T | Oestrogen excess | Obesity (aromatase excess), liver disease, exogenous oestrogen, oestrogen-secreting tumour | LFTs; testicular USS; BMI |

**Ovulation Confirmation:** Mid-luteal progesterone ≥30 nmol/L confirms ovulation. Sample at day (cycle length − 7). For 28-day cycle = Day 21. Borderline 15–30 nmol/L: repeat sample; timing may be off.

**OCP/HRT Effects:** Oestrogen-containing OCP: suppresses LH/FSH (near zero) + raises SHBG. Should be discontinued ≥4–6 weeks before gonadal hormone assessment ideally.

### 2H. Cardiac Function Assessment — COMPREHENSIVE

| Analyte | Male | Female | Units | Critical |
|---------|------|--------|-------|---------|
| hs-Troponin I (Atellica) | <34 | <16 | ng/L | Rising pattern above 99th percentile 🚨 |
| hs-Troponin T (Cobas) | <14 (all) | <14 | ng/L | >52 with rise 🚨 |
| NT-proBNP | <75y: <125; >75y: <450 | same | pg/mL | >900 HF likely; >35,000 🚨 |
| BNP | <100 | <100 | pg/mL | >500 HF likely; >1000 🚨 |
| CK (total) | 40–320 | 25–200 | U/L | >5000 🚨 |
| CK-MB | <25 U/L or <6% of total CK | same | U/L | >25 + rising = myocardial injury |
| Myoglobin | M:28–72; F:25–58 | µg/L | >1000 🚨 (rhabdomyolysis) |
| LDH | 135–225 | 135–214 | U/L | — |
| D-Dimer | <0.5; age-adjusted threshold: age×0.01 µg/mL if >50y | µg/mL FEU | — |
| Fibrinogen | 2.0–4.0 | g/L | <1.0 🚨 (DIC) |
| Homocysteine | <15 | µmol/L | >30 🚨 (very high CV risk; B12/folate deficiency) |
| Lp(a) | <125 nmol/L (<50 mg/dL) | nmol/L | >125 = high independent CV risk |
| ApoB | M:<1.0; F:<0.9 optimal | g/L | >1.4 = elevated atherogenic risk |
| ApoA1 | M:1.0–1.6; F:1.0–1.9 | g/L | <0.9 = low HDL capacity |

**Serial Troponin Interpretation (ESC 0h/1h Algorithm):**
- 0h hs-TnI/T < sex-specific 99th percentile AND 1h delta <5 ng/L (TnT) or <6 ng/L (TnI) → AMI rule-out (high NPV)
- 0h hs-TnI/T very high (>5× 99th percentile) OR 1h delta ≥5 ng/L (TnT) or ≥6 ng/L (TnI) → AMI rule-in 🚨
- Intermediate zone: serial testing at 3h; clinical assessment; ECG; risk stratification
- Stable elevated troponin (no delta) = chronic myocardial injury — CKD, HF, myocarditis, demand ischaemia

**NT-proBNP/BNP Framework:**

| NT-proBNP (pg/mL) | BNP (pg/mL) | Interpretation |
|------------------|------------|----------------|
| <125 (<75y) / <450 (>75y) | <100 | HF unlikely (high NPV) |
| 125–900 | 100–500 | Grey zone → echo + clinical |
| >900 | >500 | HF probable |
| >5000 | >1000 | Severe/decompensated HF |
| >35,000 | — | Critical — notify immediately 🚨 |

**BNP Confounders:** ↑ by: CKD, PE, sepsis, AF, thyrotoxicosis, large pericardial effusion | ↓ by: Obesity (BMI>35 reduces BNP up to 40% — NT-proBNP less affected)

**CK-MB Index:** CK-MB% = (CK-MB ÷ total CK) × 100; >6% = myocardial-specific; <6% = skeletal muscle origin (even if CK-MB absolute value elevated)

### 2I. Bone Health Panel — COMPREHENSIVE

| Analyte | Reference | Units | Critical | Notes |
|---------|-----------|-------|---------|-------|
| Calcium (total) | 2.08–2.65 | mmol/L | <1.5 🚨 / >3.5 🚨 | Correct for albumin: Ca_corr = Ca_meas + 0.02 × (40 − albumin g/L) |
| Ionised Calcium | 1.15–1.32 | mmol/L | <0.8 🚨 / >1.6 🚨 | Gold standard; unaffected by albumin |
| Phosphate | 0.87–1.45 | mmol/L | <0.3 🚨 | Fasting preferred; IV glucose causes false low |
| Magnesium | 0.66–1.07 | mmol/L | <0.4 🚨 / >2.1 🚨 | Hypomagnesaemia causes PTH resistance |
| PTH (intact 1–84) | 1.6–7.2 | pmol/L | >30 (secondary hyperPTH) | Interpret alongside Ca and Vitamin D |
| 25-OH Vitamin D | >75 sufficient; 50–75 insufficient; 25–50 mild deficiency; <25 deficiency; <12 severe 🚨 | nmol/L | CBAHI minimum >50 nmol/L |
| 1,25-(OH)₂ Vitamin D | 43–149 | pmol/L | — | Low in CKD G3+; high in granulomatous disease |
| ALP (total) | M:44–147; F:35–104 | U/L | >1500 | GGT needed to confirm hepatic vs bone origin |
| Bone-specific ALP (BSALP) | M:<22.5; F(pre):<14; F(post):<22.6 | µg/L | — | More specific than total ALP for bone turnover |
| P1NP (N-propeptide type 1 procollagen) | M:20–76; F(pre):19–83; F(post):16–96 | µg/L | — | IOF-preferred bone formation marker |
| CTX (β-C-terminal telopeptide) | M:<0.704; F(pre):<0.573; F(post):<0.704 | µg/L | — | Bone resorption; fasting 08:00 sample essential |
| Osteocalcin | M:12–55; F(pre):11–43; F(post):15–46 | µg/L | — | Bone formation; also reflects Vitamin K status |
| DPD (urine deoxypyridinoline) | F:3.0–7.4; M:4.0–19.0 | nmol/mmol Cr | — | Fasting 2nd void specimen |

**PTH + Calcium Decision Matrix:**

| Ca²⁺ | PTH | Interpretation |
|------|-----|---------------|
| ↑ | ↑ or N-high | Primary hyperparathyroidism — parathyroid adenoma (80%)/hyperplasia/carcinoma |
| ↑ | ↓ | Malignancy (PTHrP), Vitamin D toxicity, sarcoidosis, granulomatous disease |
| N | ↑↑ | Secondary hyperparathyroidism — Vitamin D deficiency, CKD, malabsorption |
| ↓ | ↑↑ secondary → autonomous | Tertiary hyperparathyroidism (CKD long-standing) |
| ↓ | ↓ or low-N | Hypoparathyroidism (post-surgical, autoimmune) |
| ↓ | ↑ but PTH effect impaired | Hypomagnesaemia → PTH resistance — check Mg first |

**Vitamin D Staging Actions:**
- >75 nmol/L: sufficient — maintain dietary intake
- 50–75 nmol/L: insufficient — supplement 1000–2000 IU/day
- 25–50 nmol/L: mild deficiency — supplement 2000–4000 IU/day; recheck in 3 months
- <25 nmol/L: deficiency — supplement 50,000 IU weekly × 8 weeks (loading); then maintenance
- <12 nmol/L: severe deficiency 🚨 — risk of osteomalacia/rickets; high-dose supplementation; notify clinician
- >250 nmol/L: toxicity — discontinue all supplements; hypercalcaemia risk

**CKD + Bone Disease:** CKD G3+: ↓1-α hydroxylation → ↓1,25-OH-D (active form) despite possibly adequate 25-OH-D stores. Supplement 25-OH-D to >75 nmol/L; use alfacalcidol or calcitriol for active form. Monitor Ca²⁺ and PTH 3-monthly.

**Bone Turnover Monitoring (Osteoporosis):**
- P1NP should fall >25% after 3–6 months effective bisphosphonate therapy
- CTX falls rapidly (within 3 months) with bisphosphonate; confirms compliance and response
- High-turnover pattern: ↑P1NP + ↑CTX = Paget's, hyperparathyroidism, hyperthyroidism, multiple myeloma

### 2J. Vitamin B12, Folate & Haematinics — COMPREHENSIVE

| Analyte | Reference | Units | Critical | Notes |
|---------|-----------|-------|---------|-------|
| Vitamin B12 (cobalamin) | 145–569 | pmol/L | <110 probable deficiency 🚨 | Serum B12 may be normal (up to 300 pmol/L) with intracellular deficiency; use MMA/HoloTC to confirm |
| Vitamin B12 (pg/mL) | 197–771 | pg/mL | <150 probable deficiency | pmol/L × 1.355 = pg/mL |
| Serum Folate | >10 | nmol/L | <7 deficiency | Sensitive to last meal — use RBC folate for body stores |
| RBC Folate (erythrocyte) | >340 | nmol/L | <340 deficiency; <230 severe | Reflects 3-month body stores — most clinically reliable |
| Homocysteine (total) | <15 | µmol/L | >30 = very high CV risk + functional deficiency 🚨 | Elevated in B12 def, folate def, CKD, hypothyroidism |
| Methylmalonic acid (MMA) | <0.28 | µmol/L | >0.28 = functional intracellular B12 deficiency | Most specific marker of B12 deficiency |
| Holotranscobalamin (HoloTC) | >35 | pmol/L | <35 = early functional B12 deficiency (active fraction) | Better early marker than total B12 |
| Intrinsic Factor Ab (IF-Ab) | Negative | — | Positive = Pernicious Anaemia (specific ~95%; sensitive ~60%) | |
| Parietal Cell Ab (PCA) | Negative | — | Positive in ~80% PA; also in autoimmune gastritis | Less specific than IF-Ab |
| Gastrin (fasting) | <100 | pg/mL | >300 = PA or Zollinger-Ellison syndrome | Elevated in achlorhydria |

**B12 Deficiency Interpretation Framework:**

| Serum B12 | Homocysteine | MMA | HoloTC | Interpretation |
|-----------|-------------|-----|--------|---------------|
| <110 pmol/L | ↑ | ↑ | <35 | Definite B12 deficiency — treat immediately |
| 110–300 pmol/L | ↑ | ↑ | <35 | Functional B12 deficiency — treat despite borderline serum |
| 110–300 pmol/L | Normal | Normal | >35 | B12 probably adequate — repeat in 3 months |
| >300 pmol/L | Normal | Normal | >35 | B12 sufficient |
| Very high >2000 pmol/L | — | — | — | Investigate: liver disease, MPN, solid tumour |

**Causes of B12 Deficiency:**
- Pernicious anaemia (IF-Ab positive; autoimmune gastric atrophy — most common >50y)
- Strict veganism/vegetarianism
- Malabsorption: gastrectomy, ileal resection, Crohn's, coeliac, bacterial overgrowth, tapeworm
- Medications: metformin (check annually), PPIs long-term, H2 blockers, colchicine
- Nitrous oxide abuse (irreversibly inactivates B12 coenzyme)
- Transcobalamin II deficiency (rare genetic)

**Causes of Folate Deficiency:**
- Poor dietary intake (elderly, alcohol dependency, eating disorders, poverty)
- Increased demand: pregnancy, haemolytic anaemia, exfoliative skin disease, dialysis
- Malabsorption: coeliac disease, IBD, short bowel
- Drugs: methotrexate (DHFR inhibitor), trimethoprim, pyrimethamine, phenytoin, valproate, cholestyramine, sulfasalazine
- Alcoholism (poor intake + impaired hepatic storage + increased urinary loss)

**B12 vs Folate Deficiency — Distinguishing:**

| Feature | B12 Deficiency | Folate Deficiency |
|---------|---------------|------------------|
| Megaloblastic anaemia | Yes | Yes |
| Subacute combined degeneration (neurological) | Yes — unique to B12 | No |
| Serum B12 | ↓ | Normal or ↑ |
| Serum folate | Normal or ↑ | ↓ |
| RBC folate | ↓ (secondary) | ↓ (primary) |
| Homocysteine | ↑ | ↑ |
| MMA | ↑ | Normal |

**⚠️ CRITICAL RULE: NEVER treat megaloblastic anaemia with folate alone until B12 deficiency is excluded.** Folate corrects haematological picture but neurological damage (subacute combined degeneration) continues and may become irreversible. Always check B12 first.

**Treatment Protocols:**
- B12 deficiency (non-dietary): IM hydroxocobalamin 1mg × 3 doses in first week, then 3-monthly maintenance (or daily oral cyanocobalamin 1000 µg if no neurological symptoms and malabsorption excluded)
- B12 deficiency (dietary/vegan): oral cyanocobalamin 50–150 µg daily or 1000 µg weekly
- Folate deficiency: oral folic acid 5 mg daily × 4 months (after B12 excluded)
- Pregnancy: folic acid 400 µg daily preconception to 12 weeks (5 mg if high-risk — previous NTD, coeliac, antiepileptic)

### 2K. Inflammatory Markers

| Analyte | Reference | Units | Critical |
|---------|-----------|-------|---------|
| CRP | <5 | mg/L | >100 (severe inflammation/sepsis) 🚨 |
| hs-CRP | <1.0 low CV risk; 1.0–3.0 intermediate; >3.0 high CV risk | mg/L | — |
| ESR (male) | <15 (<50y); <20 (>50y) | mm/hr | >100 (myeloma, giant cell arteritis, sepsis) |
| ESR (female) | <20 (<50y); <30 (>50y) | mm/hr | >100 |
| Procalcitonin (PCT) | <0.1 normal; 0.1–0.25 monitor; >0.25 bacterial likely; >2 sepsis; >10 septic shock | µg/L | >10 🚨 |
| IL-6 | <7 | pg/mL | >100 (cytokine storm) 🚨 |
| Lactate | 0.5–2.2 | mmol/L | >4 (septic shock) 🚨 |
| Ferritin (inflammatory) | M:30–300; F:15–200 | µg/L | >10,000 (HLH, Still's, MAS) 🚨 |

### 2L. Tumour Markers

| Marker | Reference | Primary Organ | Key Notes |
|--------|-----------|--------------|----------|
| PSA (total) | <4.0 (<50y: <2.5) | Prostate | Also elevated in BPH, prostatitis; PSA density + velocity essential |
| AFP | <7 µg/L | Liver (HCC), testis (NSGCT) | Normal elevation in pregnancy |
| CEA | <3.0 (non-smoker); <5.0 (smoker) | Colorectal, lung, breast | Monitoring, not diagnosis |
| CA-125 | <35 U/mL | Ovary | Elevated in endometriosis, PID, fibroids, ascites |
| CA 19-9 | <37 U/mL | Pancreas, biliary | False positive in cholestasis; absent in Lewis antigen-negative |
| CA 15-3 | <25 U/mL | Breast | Recurrence monitoring |
| Beta-hCG | <5 IU/L | Trophoblastic, testis | Serial doubling in normal pregnancy |
| Calcitonin | M:<11.5; F:<4.6 pg/mL | Medullary thyroid cancer | |
| Chromogranin A | <100 µg/L | NETs, phaeochromocytoma | Falsely elevated with PPI use |
| 5-HIAA (24h urine) | 10–47 µmol/24h | Carcinoid | Avoid tryptophan-rich foods before collection |

---

## PHASE 3 — CRITICAL / PANIC VALUE ALERT SYSTEM

All require direct clinician notification within 60 minutes (ISO 15189:2022 · JCAHO NPSG.02.03.01).

| Analyte | Critical Low | Critical High |
|---------|------------|--------------|
| Sodium | <120 mmol/L | >158 mmol/L |
| Potassium | <2.8 mmol/L | >6.2 mmol/L |
| Calcium (total) | <1.5 mmol/L | >3.5 mmol/L |
| Ionised Ca | <0.8 mmol/L | >1.6 mmol/L |
| Glucose | <2.2 mmol/L | >27.8 mmol/L |
| Magnesium | <0.4 mmol/L | >2.1 mmol/L |
| Phosphate | <0.3 mmol/L | — |
| Bicarbonate | <10 mmol/L | >40 mmol/L |
| Creatinine | — | >884 µmol/L (new) |
| Bilirubin (total) | — | >342 µmol/L |
| Ammonia | — | >55 µmol/L |
| Lactate | — | >10 mmol/L (>4 = septic shock) |
| TSH | <0.03 mIU/L | >100 mIU/L |
| FT4 | <6 pmol/L | >77 pmol/L |
| FT3 | — | >20 pmol/L |
| Cortisol (morning) | <83 nmol/L | — |
| hs-Troponin | — | Rising pattern above 99th percentile 🚨 |
| NT-proBNP | — | >35,000 pg/mL |
| BNP | — | >1000 pg/mL |
| CK | — | >5000 U/L |
| Myoglobin | — | >1000 µg/L |
| Triglycerides | — | >11.3 mmol/L |
| PT/INR | — | >6.0 |
| Fibrinogen | <1.0 g/L | — |
| Vitamin D | <12 nmol/L (severe) | >375 nmol/L (toxicity) |
| Vitamin B12 | <110 pmol/L + neurological sx | >2000 pmol/L (investigate cause) |
| PTH | — | >30 pmol/L (severe secondary) |
| Prolactin | — | >5000 mIU/L (macroadenoma likely) |
| Homocysteine | — | >100 µmol/L (metabolic disorder) |
| Ferritin | — | >10,000 µg/L (HLH/Still's) |
| Aldosterone:Renin Ratio | — | >750 (Conn's screen positive) |

**Critical Value Protocol:**
1. Verify result — confirm no H/I/L interference; repeat if first occurrence
2. Call clinician directly within 60 minutes — no voicemail
3. Document: time of result, time of call, who notified, exact value communicated
4. Escalate if no contact in 30 minutes: ward nurse → on-call doctor → emergency team

---

## PHASE 4 — ORGAN SYSTEM ASSESSMENT ENGINES

### 4A. Renal
Apply CKD stage → electrolyte consequences → AKI vs CKD → pre/renal/post differentiation → CKD-MBD screen (PTH, Vit D, phosphate, BSALP)

### 4B. Liver
R-ratio → injury pattern → de Ritis ratio → synthetic markers (albumin, INR, bilirubin) → Child-Pugh surrogate → aetiology (viral serology, autoimmune, iron studies, Caeruloplasmin, A1AT)

### 4C. Thyroid
Full TSH algorithm table → pregnancy trimester-specific ranges if pregnant → drug effects → NTI exclusion → autoimmune assessment (anti-TPO, TRAb)

### 4D. Adrenal
Cortisol timing critical — state sample time; morning cortisol < 83 = 🚨; ACTH correlation matrix → Cushing's screening algorithm → ARR for hyperaldosteronism; DHEA-S for adrenal androgen excess

### 4E. Reproductive Hormones
Must know cycle day (female) or time of draw (male testosterone). Apply phase-specific ranges. LH:FSH ratio; AMH and inhibin B for ovarian reserve; prolactin: PEG precipitation before MRI if elevated; FAI for hyperandrogenism quantification; progesterone ovulation rule.

### 4F. Cardiac Function
Serial troponin mandatory: apply ESC 0h/1h algorithm. Distinguish acute AMI (rising delta) from chronic myocardial injury (stable elevation). BNP/NT-proBNP: obesity confounds BNP (not NT-proBNP); CKD elevates both. CK-MB index >6% = myocardial. Homocysteine as CV risk marker — check B12/folate. Lp(a) for residual risk assessment.

### 4G. Bone Health
Always albumin-correct calcium. PTH + Ca matrix → diagnosis. Vitamin D staging → supplement protocol. CKD: use active Vit D form. Bone turnover markers P1NP + CTX: fasting 08:00; monitor osteoporosis treatment (P1NP should fall >25% at 3–6 months). Identify high vs low turnover pattern.

### 4H. B12 & Folate
Always measure both together. MMA = most specific for B12 deficiency. HoloTC = earliest functional marker. RBC folate = best for body stores (not serum folate). NEVER treat with folate alone until B12 excluded (neurological damage risk). Metformin users: check B12 annually.

---

## PHASE 5 — INTEGRATED CLINICAL PATTERN RECOGNITION

| Pattern | Syndrome |
|---------|---------|
| ↑Creatinine + ↑K⁺ + ↑Phosphate + ↓Ca²⁺ + ↓HCO₃⁻ + ↑PTH | CKD with secondary hyperparathyroidism |
| ↑Bilirubin (indirect) + ↑LDH + ↓B12 or ↓folate + macrocytosis | Megaloblastic haemolytic anaemia |
| ↑Homocysteine + ↓B12 + ↑MMA | B12 deficiency — treat urgently |
| ↑Homocysteine + ↓RBC folate + normal MMA | Folate deficiency (B12 excluded) |
| ↓Ca²⁺ + ↑PTH + ↓25-OH-Vit D | Vitamin D deficiency with secondary hyperPTH |
| ↑Ca²⁺ + ↓PTH + ↑ALP + clinical malignancy | Malignancy-associated hypercalcaemia |
| ↑Ca²⁺ + ↑PTH + ↓Phosphate | Primary hyperparathyroidism |
| ↑Troponin (rising delta) + ↑NT-proBNP | AMI with cardiac decompensation |
| ↑NT-proBNP stable + ↑creatinine | Cardiorenal syndrome |
| ↑TSH + ↓FT4 + ↑cholesterol + ↑CK + ↑homocysteine | Hypothyroidism |
| ↓TSH + ↑FT4 + ↑ALP + ↑Ca²⁺ + ↑P1NP/CTX | Hyperthyroidism with high bone turnover |
| LH:FSH >2:1 + ↑testosterone + FAI>5 + ↓SHBG + ↑insulin + ↑TG | PCOS with metabolic syndrome |
| LH ↑↑ + FSH ↑↑ + E2 ↓↓ (<40y) | Premature ovarian insufficiency |
| ↓Cortisol + ↑K⁺ + ↓Na⁺ + ↓glucose + ↑ACTH | Addison's disease |
| ↑Cortisol + ↑glucose + ↑Na⁺ + ↓K⁺ + ↓ACTH | Adrenal Cushing's syndrome |
| ↑Prolactin + ↓LH + ↓FSH + ↓E2/T | Hyperprolactinaemia → hypogonadism |
| ↑P1NP + ↑CTX + ↑ALP + ↑Ca²⁺ | High bone turnover — Paget's, mets, hyperPTH |
| ↑Glucose + ↑HbA1c + ↑TG + ↓HDL | Metabolic syndrome / T2DM |
| ↑ALT + ↑AST + ↑TG + ↑glucose + ↑ferritin + ↓ALP:GGT ratio <1 | NAFLD/NASH |
| ↑CRP + ↑PCT + ↑Lactate + ↓Albumin | Sepsis — apply SOFA |
| Very high ferritin (>10,000) + ↑LDH + ↑TG | Haemophagocytic lymphohistiocytosis (HLH) 🚨 |

---

## PHASE 6 — OUTPUT FORMAT: CHEMISTRY & HORMONE REPORT

### 🔬 CLINICAL CHEMISTRY & HORMONE ASSESSMENT REPORT

**Patient:** Age ___ | Sex ___ | Sample ID: ___
**Instrument:** [Atellica CH/IM / Cobas / specify] | **Date:** ___
**Fasting:** [Yes/No/Unknown] | **Sample time:** ___ | **Cycle day (F):** ___
**Clinical context:** ___ | **QC:** ___

---

#### SECTION 1: 🚨 CRITICAL VALUE ALERT *(Always first)*

| Analyte | Result | Threshold | Required Action |
|---------|--------|-----------|----------------|
| [Name] | X | >X / <X | 🚨 CALL CLINICIAN WITHIN 60 MIN — document time, name, value |

*State "No critical values identified" if none.*

---

#### SECTION 2: FULL PARAMETER TABLE

| Analyte | Result | Unit | Reference (Age/Sex) | Status | Note |
|---------|--------|------|--------------------|----|------|
| [Name] | X | unit | range | ✅/⬆️/⬇️/⚠️/🚨 | Brief clinical note |

*✅ Normal · ⬆️ Elevated · ⬇️ Low · ⚠️ Borderline · 🚨 Critical*

---

#### SECTION 3: ORGAN SYSTEM ASSESSMENT *(include only systems with results present)*

**3A. Renal Function:** eGFR stage · electrolyte pattern · AKI vs CKD · CKD-MBD implications
**3B. Liver Function:** R-ratio · injury pattern · de Ritis ratio · synthetic markers · likely aetiology
**3C. Metabolic/Glucose:** Glycaemic status · HbA1c classification · lipid CV risk · HOMA-IR if insulin available
**3D. Iron Studies:** Pattern (IDA/ACD/overload/haemolysis) · CBC integration
**3E. Thyroid (TSH/FT4/FT3/antibodies):** Full algorithm → diagnosis · severity · drug effects considered
**3F. Adrenal (Cortisol/ACTH/Aldosterone/DST):** Timing noted · axis interpretation · Cushing's/Addison's assessment
**3G. Reproductive & Fertility:** Cycle phase noted · LH/FSH/E2/P4/T/PRL/AMH/Inhibin B → diagnosis · FAI
**3H. Cardiac Function:** Serial troponin delta · BNP/NT-proBNP framework · CK-MB index · D-Dimer
**3I. Bone Health (PTH/Vit D/Ca/P1NP/CTX):** PTH-Ca matrix → diagnosis · Vit D staging · turnover markers
**3J. Vitamin B12 & Folate:** B12 framework (serum + MMA + HoloTC) · folate (RBC folate preferred) · homocysteine · B12 vs folate distinction · cause · treatment protocol
**3K. Inflammatory Markers:** CRP/PCT/ESR/IL-6 → severity · bacterial vs viral · sepsis risk
**3L. Tumour Markers:** Clinical context mandatory — never diagnose malignancy on marker alone

---

#### SECTION 4: INTEGRATED CLINICAL NARRATIVE

**Primary Finding:** [Most clinically significant result]
**Secondary Findings:** [Additional abnormalities and their inter-relationships]
**Overall Pattern:** [Syndrome-level: e.g., "CKD G3b with secondary hyperparathyroidism, Vitamin D deficiency, concurrent B12 deficiency from metformin use, and borderline hypothyroidism"]
**Confidence:** High / Moderate / Requires confirmatory testing

---

#### SECTION 5: DIFFERENTIAL DIAGNOSIS

1. [Most likely] — Evidence from results
2. [Second] — Evidence
3. [Third] — Requires [test] to confirm/exclude

**Excluded:** [Condition] — excluded because [specific results]

---

#### SECTION 6: INSTRUMENT / QC / PRE-ANALYTICAL

| Item | Status | Note |
|------|--------|------|
| Serum indices H/I/L | Reported / Normal / Flagged | Action if flagged |
| QC status | Passed / Unknown | |
| Sample timing (hormones) | Appropriate / Unknown | Cortisol: must be 08:00–09:00; testosterone: morning |
| Cycle day (female hormones) | Known / Unknown | Reference ranges cannot be applied without cycle day |
| Biotin interference | Not suspected / Suspected | 24h washout + repeat if suspected |
| Heterophile Ab / Macro-PRL | Not applicable / Check | PEG test if prolactin elevated + asymptomatic |
| Method notes | | Jaffé creatinine, TBG effects on Total T4/T3, HbA1c method limitations |

---

#### SECTION 7: ACTION PLAN

**🚨 IMMEDIATE (critical values — within 60 minutes):**
- [ ] Notify [clinician/dept] of [analyte] = [value]; document per ISO 15189:2022

**SHORT-TERM (within 24–48 hours):**
- [ ] Confirmatory or complementary tests
- [ ] Functional tests (SST, DST, GTT, progesterone D21, etc.)

**FURTHER INVESTIGATIONS:**
- [ ] Imaging: MRI pituitary / adrenal CT / thyroid USS / DEXA / bone scan
- [ ] Specialist referral: Endocrinology / Nephrology / Cardiology / Fertility / Rheumatology / Haematology
- [ ] Molecular/genetic: HFE gene / karyotype / fragile X (POI) / 21-hydroxylase gene (CAH)
- [ ] IF-Ab / PCA for pernicious anaemia; intrinsic factor; Schilling test if available
- [ ] Bone marrow biopsy (B12/folate deficiency with severe haematological findings)

**CLINICIAN COMMUNICATION:**
- [ ] Key messages for requesting doctor
- [ ] Medications to review: metformin → B12 annually; PPIs → B12; antiepileptics → folate/Vit D; OCP → suppress LH/FSH; amiodarone → TFTs 6-monthly
- [ ] Delta check alerts

**INSTRUMENT/QC ACTIONS:**
- [ ] Rerun if interference confirmed
- [ ] Calibration check if systematic shift
- [ ] Biotin: 24h patient washout; repeat all affected immunoassays

---

#### SECTION 8: BRIEF CLINICAL CONCLUSION

> *[3–5 sentence summary: (1) most significant findings, (2) integrated syndrome pattern, (3) key diagnoses to confirm or exclude, (4) single most critical next action.]*

---

## PHASE 7 — QC & MAINTENANCE CHECKS

### Atellica CH

| Issue | Trigger | Action |
|-------|---------|--------|
| H/I/L serum index flagged | Auto-reported | Per SOP: note/reject; fresh sample |
| Jaffé creatinine elevated | Ketoacidosis, cephalosporins | Switch to enzymatic creatinine |
| ALP elevated + GGT normal | Bone pattern | Request BSALP or P1NP |
| HbA1c interference | Haemoglobinopathy present | Use boronate affinity; correlate with plasma glucose |
| IMT (electrolyte) calibration failure | Na/K/Cl flagged * | Run ISE calibrator; service call if persists |
| Westgard rule violation | Levey-Jennings plot | 1-3s: reject; hold patients; investigate |
| Biotin suspected | TSH suppressed + asymptomatic | 24h washout; repeat all affected assays |
| CTX result high | Sample not fasting or not 08:00 | Restate collection instructions; repeat |

### Roche Cobas (ECLIA)

| Issue | Trigger | Action |
|-------|---------|--------|
| Prozone effect | Very high conc → falsely low | Auto-dilution check; manual serial dilution |
| Heterophile Ab | Discordant troponin/TSH/PSA | Blocking tubes; alternate immunoassay method |
| Macro-prolactin | High PRL + asymptomatic | PEG precipitation; <40% recovery = macro-PRL |
| Delta check failure | >50% change in stable analyte | Verify patient ID; repeat before reporting |
| Vitamin D variation | Seasonal; different lots | Use DEQAS-standardised method; note season |
| B12/folate haemolysis | H flag on sample | Reject; haemolysis falsely lowers folate (releases RBC folate into serum) |
| ACTH sample instability | Degradation if delayed >15 min on ice | Centrifuge immediately; freeze at −20°C; never leave at room temperature |

---

## SKILL USAGE NOTES

### Trigger phrases:
"Interpret my chemistry / hormone panel / thyroid / cortisol / ACTH / LH / FSH / fertility hormones / testosterone / prolactin / AMH / cardiac markers / troponin / BNP / bone health / PTH / Vitamin D / P1NP / CTX / vitamin B12 / folate / homocysteine / inflammatory markers / lipids / tumour markers / critical values"

### Mandatory inputs:
1. Image or typed values from panel
2. Patient age and biological sex
3. Clinical context

### Always ask if not provided:
- Menstrual cycle day (female reproductive hormones)
- Time of blood draw (cortisol, ACTH, testosterone, GH)
- Fasting status (glucose, lipids, insulin, cortisol stimulation)
- Pregnancy status
- Biotin supplementation
- Current medications

### Output modes:

| Phrase | Output |
|--------|--------|
| *(default)* | Full 8-section report |
| "quick summary" | Sections 1 + 8 only |
| "just critical values" | Section 1 only |
| "thyroid only" | Section 3E + relevant 2E rows + action |
| "adrenal only" | Section 3F + 2F rows + action |
| "fertility / reproductive" | Section 3G + 2G rows + action |
| "cardiac only" | Section 3H + 2H rows + action |
| "bone health" | Section 3I + 2I rows + action |
| "B12 folate" | Section 3J + 2J rows + treatment protocol |
| "liver only" | Section 3B + 2B rows + action |
| "kidney only" | Section 3A + 2A rows + action |
| "iron studies" | Section 3D + 2D pattern + action |
| "inflammatory markers" | Section 3K + 2K rows + action |

---

*EEHLSS / MedLabAI-LIS | Maintained by Echukwuka | Version 2.0 — April 2026*
*Aligned to: IFCC · CLSI · ISO 15189:2022 · JCAHO NPSG.02.03.01 · CBAHI · SFDA · ESC 2023 · Endocrine Society · IOF · NICE · KDIGO 2022*
*All results require validation by a qualified Medical Laboratory Scientist or Clinical Biochemist.*
*This skill provides clinical decision support only — not a substitute for clinical judgement or face-to-face patient assessment.*
