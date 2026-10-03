---
name: transfusion-medicine-interpreter
description: >
  Transfusion Medicine & Immunohaematology Decision Support. Trigger when a user
  uploads antibody ID panel results (ID-DiaPanel, Surgiscreen, antigram), crossmatch
  worksheets, DAT/DCT, IAT/ICT, or blood group typing cards. Covers: ABO/Rh grouping
  and discrepancy resolution; antibody screening and identification (single and multiple
  alloantibodies); DAT/IAT interpretation; autoantibody management (warm AIHA, cold
  agglutinin disease, PCH, DIIHA); crossmatch interpretation (IS, AHG, electronic);
  extended phenotyping and genotyping strategy; antibody titration and HDFN monitoring;
  special populations (sickle cell, thalassaemia, pregnancy, neonates, transplant,
  oncology, daratumumab interference); transfusion component selection (RBC, platelets,
  FFP, cryoprecipitate, factor concentrates, IUT); compatibility reporting and clinician
  guidance. Asks for patient history, clinical context, testing phase, and prior results.
---

# Transfusion Medicine & Immunohaematology Interpreter
### Comprehensive Blood Bank Decision Support — All Component Types

**Version:** 1.0 | **April 2026**
**Standards:** ISBT · AABB Technical Manual (20th Ed) · BCSH/BSH · FACT · CAP · CBAHI · ISO 15189:2022 · NICE · RCPath
**Brand:** EEHLSS / MedLabAI-LIS | Crimson #B71C1C · Navy #0D1B4B · Gold #F9A825

---

## PHASE 0 — INTAKE & MANDATORY DATA COLLECTION

Before interpreting, collect the following. **Ask for any missing items before proceeding.**

### Required for every case:
1. **Image(s)** of the panel worksheet(s) — antibody ID panel, screen cells, crossmatch, DAT card
2. **Patient age** and **biological sex**
3. **ABO and Rh(D) type** (forward and reverse typing results if available)
4. **Clinical context** — e.g., "routine pre-transfusion", "obstetric/antenatal", "haemolytic anaemia investigation", "post-transfusion reaction", "sickle cell disease chronic transfusion", "haematological malignancy", "transplant workup", "emergency trauma"
5. **Transfusion history** — number of units, timing (especially within last 3 months), product types
6. **Obstetric history** — gravidity, parity, previous HDFN, RhIG administration dates and doses
7. **Medications** — especially daratumumab, rituximab, methyldopa, penicillin, cephalosporins, IVIG, RhIG

### Ask if not provided (test-specific):
- **Phase of testing performed** — IS (immediate spin), RT (room temperature), 37°C, AHG/IAT, enzyme
- **Autocontrol result** — mandatory for all panels; positive autocontrol changes interpretation entirely
- **Method** — gel/column agglutination technology (CAT), solid phase, tube (LISS, PEG, albumin)
- **Patient's own phenotype** — especially Rh (C/c/E/e/D), Kell (K/k), Duffy (Fya/Fyb), Kidd (Jka/Jkb), MNS (M/N/S/s)
- **Previous antibody identification history** — does patient have a known antibody on file?
- **Recent transfusion** — within last 3 months? If yes: mixed-field possible; adsorption studies may be needed
- **DAT result on patient's cells** — IgG, C3d, or both?
- **Eluate results** (if DAT positive) — what does eluate react with?

> **CRITICAL RULE:** A positive autocontrol changes every interpretation. Always establish autocontrol status first.

---

## PHASE 1 — INSTRUMENT & TECHNOLOGY PRIMER

### 1A. Gel/Column Agglutination Technology (CAT) — Bio-Rad ID-DiaPanel, ID-DiaPanel-P

**Principle:**
1. Patient serum/plasma + reagent red cells are incubated in micro-tubes containing gel matrix (Sephadex) with anti-human globulin (AHG) pre-embedded for IAT cards, or neutral gel for IS/RT tests
2. After incubation, tube is centrifuged at controlled speed and time
3. Agglutinated RBCs (bound by antibody + AHG) cannot penetrate the gel → trapped at top = **positive**
4. Non-agglutinated RBCs pellet through gel to bottom = **negative**

**Reaction Grading (CAT):**

| Grade | Appearance | Meaning |
|-------|-----------|---------|
| 4+ | Complete solid red agglutinate at top of gel, no cells at bottom | Strongest positive — high-titre or high-avidity antibody |
| 3+ | Large agglutinate at top, some cells at bottom | Strong positive |
| 2+ | Agglutinate in upper half of gel | Moderate positive |
| 1+ | Agglutinate dispersed throughout gel | Weak positive |
| W+ / ± | Faint agglutinate, mostly cells at bottom | Very weak — clinically significant? Investigate |
| 0 | All cells pelleted at bottom | Negative |
| MF | Mixed field — two populations | Recent transfusion, chimerism, or weak variant expression |

**ID-DiaPanel (standard 11-cell panel):** Tests serum/plasma for antibodies against a comprehensive antigen profile. Each of the 11 reagent cells (from Group O donors) is selected to express specific antigens, including homozygous (double-dose) cells for Rh, MNS, Duffy, Kidd to detect dosage effect. Covers: D, C, E, c, e, f, Cw, K, k, Kpa, Kpb, Jsa, Jsb, Fya, Fyb, Jka, Jkb, Lea, Leb, P1, M, N, S, s, Lua, Lub, Xga.

**ID-DiaPanel-P (extended panel):** Additional cells for resolution of complex antibodies, complement activation studies, and mixed antibody workups.

**Reading Key:**
- `+` = positive agglutination at test phase
- `0` = negative
- `nt` = not tested (antigen not expressed or destroyed by enzyme)
- `/` = weak positive (also written as `w+`)
- `MF` = mixed field

### 1B. Surgiscreen / Antigram (Ortho Clinical Diagnostics, 3-cell screen)
- 3 Group O reagent cells: R1wR1 (Cell 1), R2R2 (Cell 2), rr (Cell 3)
- Designed to detect most clinically significant alloantibodies at IS and AHG phases
- A positive screen triggers antibody identification panel
- Can be used as crossmatch check for screen-positive patients

### 1C. Tube Testing (LISS, PEG, Albumin, Enzyme)
- IS (immediate spin): detects IgM antibodies (ABO, cold reactive) — room temperature
- 37°C saline: rarely used alone; some warm IgM antibodies detected
- AHG (indirect antiglobulin test): detects IgG and complement-binding antibodies — clinically significant
- LISS (low ionic strength solution): enhances IgG antibody uptake; 10–15 min incubation at 37°C
- PEG (polyethylene glycol): most sensitive enhancement medium; removes water → concentrates antibodies; can detect very weak antibodies; may cause false positives — requires strict protocol
- Enzyme (ficin, papain, bromelain): cleaves sialic acid → enhances some antibodies (Rh, Kidd), destroys others (Duffy, MNS, Xga); Kell unaffected

**Enzyme Effects on Blood Group Antigens:**

| Enhanced by Enzyme | Destroyed by Enzyme | Unaffected |
|-------------------|--------------------|-----------| 
| Rh (D,C,c,E,e), Kidd (Jka, Jkb), Lewis (Lea, Leb), P1, I | Duffy (Fya, Fyb), MNS (M, N, S, s), Xga | Kell (K, k), Lutheran, ABO, Diego |

---

## PHASE 2 — ABO & RH BLOOD GROUPING ENGINE

### 2A. ABO Typing Interpretation

**Forward (Cell) Grouping** — antibodies against patient cells:

| Anti-A | Anti-B | Anti-A,B | Interpretation |
|--------|--------|---------|----------------|
| + | 0 | + | Group A |
| 0 | + | + | Group B |
| + | + | + | Group AB |
| 0 | 0 | 0 | Group O |

**Reverse (Serum) Grouping** — patient serum vs A1 and B cells:

| A1 cells | B cells | Expected group |
|---------|--------|----------------|
| 0 | + | Group A |
| + | 0 | Group B |
| 0 | 0 | Group AB |
| + | + | Group O |

**ABO Discrepancy — Forward/Reverse Mismatch:**

| Discrepancy Type | Common Causes | Approach |
|-----------------|--------------|---------|
| Weak/missing forward reaction | Subgroup (A2, A3, Ax), disease (leukaemia), hypogammaglobulinaemia | Lectin testing, saliva inhibition, adsorption/elution, molecular |
| Extra forward reaction | B(A) phenotype, bacterial contamination, polyagglutinable RBCs | Warm wash; retest; check reverse |
| Weak/missing reverse reaction | Neonates (maternal antibodies only), immunosuppression, hypogammaglobulinaemia, elderly, bone marrow transplant | Clinical history; cold vs warm incubation |
| Extra cells in reverse | Unexpected cold alloantibody (anti-M, anti-P1, anti-Lea, anti-I), warm autoantibody | Check autocontrol; test at 37°C only; enzyme panel |
| Polyagglutination | T-polyagglutinable, bacterial enzyme-altered RBCs | Use monoclonal antibodies (not polyclonal sera which contain anti-T) |

### 2B. Rh(D) Typing

**Routine D Typing:**
- Strong D (most common): clear agglutination with anti-D IgM monoclonal
- Weak D: requires IAT phase to detect (formerly called Du)
- Partial D: has all or most D epitopes missing; may form anti-D; treat as D-negative for transfusion purposes
- DEL (D-elution only): very weak D detectable only by adsorption-elution; common in East Asians

**D-Negative Confirmation:** Two different anti-D IgM monoclonal reagents at IS phase; if both negative → test by IAT (weak D test); document result clearly.

**Clinical Decision Rules for D typing:**
- Patients: If weak D test positive → treat as D-positive (cannot form immune anti-D)
- Donors: Test by IAT; if positive → label as D-positive (protect D-negative recipients)
- Obstetric patients: If initial typing ambiguous → treat as D-negative and give RhIG; confirm by molecular D genotyping
- Partial D patients: Treat as D-negative; can form immune anti-D; give D-negative blood; may need RhIG

**Extended Rh Typing:** Type for C, c, E, e in addition to D. Essential for:
- Patients with known anti-Rh antibodies
- Chronic transfusion patients (sickle cell, thalassaemia)
- Patients likely to require long-term transfusion support
- All females of childbearing potential with alloantibodies

### 2C. Rh(D) Negative Patients — Special Management

| Scenario | Action |
|---------|--------|
| Non-sensitised Rh(D)-negative female <50y | ALWAYS give Rh(D)-negative blood and platelets |
| Non-sensitised Rh(D)-negative male or post-menopausal female | Strongly prefer D-negative; use D-positive only if shortage |
| Known immune anti-D present | ALWAYS give Rh(D)-negative blood |
| Rh(D)-negative patient given D-positive platelets inadvertently | Consider RhIG (1500 IU covers ~30 mL RBCs) |
| Emergency: no D-negative available | Use D-positive with RhIG cover if patient is non-sensitised |

---

## PHASE 3 — ANTIBODY SCREEN & PANEL INTERPRETATION ENGINE

### 3A. Step-by-Step Panel Interpretation Protocol

**STEP 1: Check the autocontrol**
- **Negative autocontrol** → antibody is most likely alloantibody (patient's serum reacting with foreign antigens)
- **Positive autocontrol** → STOP. Autoantibody, recent transfusion with alloantibody on circulating donor cells, drug effect, or autoimmune condition. Proceed to autoantibody workup (Phase 5)

**STEP 2: Identify positive cells**
- List all cells showing any reaction (grade ≥ W+)
- Note the strength of reaction — dosage effect? (stronger with homozygous cells)
- Record phase of reaction: IS only, 37°C, AHG only, or all phases

**STEP 3: Rule OUT antibodies**
- To rule OUT an antibody: the patient's serum must NOT react with a cell that is POSITIVE for that antigen
- Use homozygous cells for definitive rule-out of dosage-sensitive antibodies: C, c, E, e, M, N, S, s, Fya, Fyb, Jka, Jkb
- Cannot rule out if only heterozygous cells are tested (weak dosage antibody may be missed)
- **Rule of three:** Ideally rule out using ≥3 cells that are antigen-positive and non-reactive

**STEP 4: Rule IN antibodies**
- The antibody target antigen must be POSITIVE on all cells that react with patient serum
- AND must be NEGATIVE on all non-reactive cells
- Dosage pattern: stronger reaction with homozygous (double-dose) cells vs heterozygous (single-dose) → suggests dosage-sensitive antibody (common in: Rh, MNS, Duffy, Kidd)

**STEP 5: Confirm specificity**
- Pattern must fit one antibody (or known mixture)
- All reactive cells must share the antigen
- All non-reactive cells must lack the antigen
- Discrepancies require: enzyme panel, additional cells, adsorption/elution, or molecular workup

**STEP 6: Confirm patient's red cell phenotype**
- Patient must lack the antigen targeted by any identified alloantibody
- If patient is antigen-positive → cannot be a simple alloantibody to that antigen; reconsider
- Exception: autoantibody (patient IS antigen-positive and autoantibody forms against self-antigen)

**STEP 7: Check for multiple antibodies**
- If single specificity doesn't explain all reactions → test additional cells, enzyme panel
- Common combinations: anti-E + anti-c; anti-K + anti-E; anti-Jka + anti-E; anti-D + anti-C (or anti-G)
- Probability statistics: calculate probability that reaction pattern fits proposed specificity (Fisher's exact test or p-value <0.05 for clinical significance)

**Statistical Probability (rule of thumb):**
- 3 concordant positive cells + 3 concordant negative cells → p ≈ 0.05 (minimum acceptable)
- 5 concordant positive + 5 concordant negative cells → p < 0.01 (confident)
- More cells = higher confidence; essential for rare antibodies

### 3B. Antigen Matrix — Key Reference

**Rh System:** D, C, c, E, e, f(ce), Cw, Cx, V, VS, G
- Clinically significant: ALL. IgG, reacts at AHG phase. Dosage effect (especially C, c, E, e)
- HLA association: None; purely blood group
- HDFN: Severe (anti-D, anti-c most common); anti-E, anti-C moderate
- HTR: Delayed and acute; all Rh antibodies clinically significant

**Kell System:** K (K1), k (K2), Kpa, Kpb, Jsa, Jsb, Ku, Kx
- K most immunogenic antigen after D; IgG, AHG phase; no dosage effect
- Anti-K: causes severe HDFN (erythroid progenitor suppression, not just haemolysis); titer not reliable for HDFN severity
- Anti-k: rare (k is high-prevalence antigen — 99.8% k-positive); clinically significant
- NOT enhanced by enzyme

**Duffy System:** Fya, Fyb, Fy3, Fy4, Fy5
- IgG; dosage effect present; DESTROYED by ficin/papain — important diagnostic tool
- Duffy-null (Fy(a-b-)): Common in sub-Saharan Africans (malaria resistance); forms anti-Fy3 if immunised
- HDFN: Anti-Fya mild-moderate; Anti-Fyb rare

**Kidd System:** Jka, Jkb, Jk3
- IgG; dosage effect; ENHANCED by enzyme
- Anti-Jka/Jkb notorious for: (1) dosage effect → may appear weak, (2) waning antibody → can become undetectable then cause DELAYED haemolytic TR (DHTR)
- Kidd-null (Jk[a-b-]): very rare; anti-Jk3 causes severe HTR; common in Polynesians/Finns
- Complement-fixing: can cause acute HTR and DHTR

**MNS System:** M, N, S, s, U, Mia
- Anti-M, Anti-N: usually IgM, reacts IS/RT; clinically insignificant usually; DESTROYED by enzyme; rarely causes HDFN or HTR
- Anti-M warm-reactive IgG: rare but clinically significant — test at 37°C only and assess carefully
- Anti-S, Anti-s: IgG; AHG phase; clinically significant HTR and HDFN; dosage effect
- Anti-U: rare; all U-negative blood required; common in African patients; high-prevalence antigen
- Anti-Mia: common in East/Southeast Asian populations; enzyme-sensitive

**Lewis System:** Lea, Leb
- IgM (mostly); reacts IS/RT; NOT clinically significant — do not cause HDFN (IgM doesn't cross placenta), rarely cause HTR
- Lewis antigens are adsorbed from plasma onto RBCs (not intrinsic)
- Exception: rare IgG Lewis antibodies — test thermal range; if only reactive at IS/RT → benign
- Lewis-negative phenotype common in pregnancy (Leb secretion changes); reverts postpartum

**P1/Pk/P System:** P1, P, Pk, P1PK, GLOB
- Anti-P1: IgM; IS/RT; clinically insignificant; enhanced by cold; can titrate highly
- Anti-P (formerly anti-Tja or anti-PP1Pk): high-prevalence; rare; can cause severe HTR and recurrent miscarriage
- Donath-Landsteiner antibody (anti-P): biphasic IgG; binds at cold, lyses at 37°C; paroxysmal cold haemoglobinuria (PCH)

**I/i System:** I, i
- Anti-I: very common cold autoantibody; benign; associated with cold agglutinin disease (CAD)
- Anti-i: associated with infectious mononucleosis (EBV), less common than anti-I

**Complement-Activating Antibodies (highest HTR risk):**
- Anti-Jka, anti-Jkb (Kidd): intravascular haemolysis
- Anti-A, anti-B: most severe (incompatible ABO: fatal acute HTR)
- Anti-Lea, anti-Leb (in IgG form, rare): complement-activating
- Anti-PP1Pk: intravascular haemolysis

### 3C. Clinically Significant vs Insignificant Antibody Classification

**Clinically Significant (must provide antigen-negative blood):**
- All Rh antibodies (D, C, c, E, e, G, Cw when warm-reactive)
- Kell system (K, k, Kpa, Kpb, Jsa, Jsb)
- Duffy system (Fya, Fyb)
- Kidd system (Jka, Jkb, Jk3) — ** even if titre low or undetectable**
- MNS: Anti-S, Anti-s, Anti-U
- Anti-M (if warm-reactive IgG or clinically relevant in pregnancy)
- Anti-Dia (Diego), Anti-Dib
- Anti-Vel (high-prevalence)
- Anti-Lan, Anti-Ata, Anti-Jr (high-prevalence)

**Usually Clinically Insignificant (compatible blood can be given if antigen-negative unavailable):**
- Anti-M (cold-reactive IgM only, not reactive at 37°C)
- Anti-N (IgM, cold-reactive)
- Anti-P1 (IgM, cold-reactive)
- Anti-Lea, Anti-Leb (IgM, cold-reactive) — note: rarely IgG Lewis causes HTR
- Anti-A1 (in A2 patients)
- Anti-HI (cold-reactive)
- Anti-I (cold autoantibody, low titre, <4°C maximum)
- Xga (not associated with significant HTR or HDFN)

**Borderline / Phase-Dependent:**
- Anti-Cw: usually insignificant; test thermal range; if only IS/RT → probably ignore; if AHG-reactive → provide Cw-negative
- Anti-Ch, Anti-Rg: high-prevalence antigens on C4; neutralisable by plasma; very rarely cause transfusion reactions

---

## PHASE 4 — DAT / DIRECT COOMBS TEST INTERPRETATION

### 4A. DAT Interpretation Algorithm

**Step 1: Perform DAT with polyspecific AHG**
- Positive polyspecific → proceed to monospecific

**Step 2: Monospecific testing**

| Anti-IgG | Anti-C3d | Interpretation |
|---------|--------|---------------|
| + | 0 | IgG coating only → warm AIHA (most common), alloantibody on recently transfused donor cells, drug-induced (certain mechanisms) |
| 0 | + | Complement (C3d) only → Cold agglutinin disease (CAD), DIIHA (complement-only mechanism), PCH (transiently) |
| + | + | Both IgG and C3d → Warm AIHA with complement activation, mixed AIHA, DIIHA (drug-dependent Ab), alloantibody + complement |
| 0 | 0 | Negative polyspecific DAT → Normal; but DAT-negative AIHA exists (<200 IgG/RBC — below detection threshold) |

**Step 3: Eluate study** (when DAT positive)
- Perform elution (heat, acid, chloroform, or digitonin-acid method)
- Test eluate against a panel of RBCs
- **Eluate reacts with all panel cells** → panagglutinin = warm autoantibody
- **Eluate reacts with specific antigen-positive cells** → specificity identified (alloantibody on donor cells in recently transfused patient, or autoantibody with specificity)
- **Eluate non-reactive (negative)** → drug-dependent antibody (e.g., cephalosporin non-immunological protein adsorption), hypergammaglobulinaemia, low-prevalence antigen antibody

### 4B. Clinical Context of DAT Results

| DAT Pattern | Clinical Scenario | Action |
|------------|-------------------|--------|
| IgG positive, eluate panreactive | Warm AIHA | Haematology referral; prednisolone; transfuse if life-threatening; adsorb serum for hidden alloantibodies |
| IgG positive, eluate shows specific Rh (e.g., anti-e) | Autoantibody with Rh relative specificity | Provide e-negative blood if possible; alloantibody exclusion critical |
| C3d only, cold autoagglutination at RT | Cold agglutinin disease (CAD) | Warm blood; blood warmer; keep patient warm; treat underlying cause |
| IgG + C3d, biphasic haemolysis | Paroxysmal cold haemoglobinuria (PCH) | Donath-Landsteiner test; usually post-viral in children; supportive care |
| IgG positive, recent transfusion, eluate shows specific antibody | Delayed haemolytic transfusion reaction (DHTR) | Identify antibody; provide antigen-negative blood |
| IgG positive in neonate | HDFN | Cord DAT; eluate to identify maternal antibody; treat neonatal jaundice |
| IgG positive, patient on daratumumab | Drug interference | Plasma neutralisation with DTT-treated reagent cells; treat CD38 using special method |
| IgG positive, patient on methyldopa | Drug-induced AIHA | Warm AIHA pattern; stop drug if possible; may persist for months post-discontinuation |
| IgG positive, patient on cephalosporin/penicillin | Drug adsorption mechanism | Non-haemolytic usually; eluate shows drug-antibody; stop drug |

### 4C. Quantitative DAT — When Standard Test Fails

**Indications for enhanced/quantitative DAT:**
- Clinical evidence of immune haemolysis but routine DAT negative
- Very weak DAT (W+) — is this meaningful?
- Suspicion of IgA or IgM warm autoantibody (rare but occur)

**Methods:**
- **Flow cytometry DAT:** Detects as few as 50–100 IgG molecules/RBC (vs 200–500 by tube/gel)
- **ELISA DAT:** Quantitative; research setting
- **Mitogen-stimulated DAT (MS-DAT):** Detects autoantibody production by stimulated lymphocytes; used in DAT-negative AIHA diagnosis
- **Monospecific anti-IgA, anti-IgM:** Test if IgG and C3d both negative but AIHA suspected

---

## PHASE 5 — AUTOANTIBODY IDENTIFICATION & MANAGEMENT

### 5A. Warm Autoantibody Workup

**When suspected:** Positive DAT (IgG ± C3d) + panreactive serum + panreactive eluate

**Step 1: Autoadsorption** (if patient has NOT been transfused in last 3 months)
- Absorb patient serum with patient's own RBCs (pre-treat RBCs with enzyme or ZZAP reagent to remove bound antibody)
- Run adsorbed serum on antibody ID panel
- Alloantibodies will NOT be adsorbed (remain in serum); autoantibodies WILL be adsorbed (removed)
- Any residual reactivity = underlying alloantibody — identify and provide antigen-negative blood

**Step 2: Allogeneic adsorption** (if patient HAS been transfused in last 3 months — autoadsorption unreliable)
- Use 2–3 sets of phenotypically different cells selected to present: R1R1, R2R2, rr (or equivalent Rh phenotypes)
- Each set absorbs different alloantibodies while the autoantibody is adsorbed by all
- After adsorption, test each adsorbed serum on identification panel
- RABBIT ERYTHROCYTE STROMA (REST) optional for non-specific adsorption

**Step 3: Specificity assessment of the autoantibody itself**
- Test unadsorbed eluate/serum against panels at various phases
- Relative specificity (e.g., "anti-e-like" preference) — common in warm AIHA
- Clinically useful if specificity found: provide e-negative (or corresponding antigen-negative) blood

**Step 4: Decision for transfusion in warm AIHA**
- Perform full alloantibody screen on adsorbed serum
- Provide blood matching patient's own Rh/Kell phenotype at minimum
- Extended matching (Rh + Kell + Kidd + Duffy + MNS) recommended for chronically transfused patients
- Transfuse if clinically necessary — DO NOT withhold blood for an incompatible crossmatch alone in life-threatening warm AIHA
- Document: "Least incompatible blood selected; patient has warm autoantibody; alloantibodies excluded by adsorption"

### 5B. Cold Autoantibody — Cold Agglutinin Disease (CAD)

**Characteristics:**
- IgM cold agglutinin; reacts at 0–4°C maximally; thermal range extends to 30°C or higher in pathological CAD
- DAT: C3d positive; IgG negative (IgM dissociates during wash, C3d remains)
- Causes: Idiopathic (often clonal B-cell disorder), Mycoplasma pneumoniae (anti-I), EBV (anti-i), B-cell lymphoma
- Clinical: acrocyanosis, Raynaud's, haemolytic anaemia when cold, livedo reticularis

**Serological identification:**
- High-titre cold agglutinin in serum (>1:64 at 4°C = significant; >1:512 = pathological CAD)
- Broad thermal range (agglutination at 30–37°C) = clinically dangerous
- Specificity: anti-I (most common), anti-i, anti-H (rare)

**Transfusion management:**
- All blood MUST be warmed via approved blood warmer before and during transfusion
- Keep patient warm; avoid cold exposure
- Crossmatch must be performed at 37°C ONLY (warm LISS/PEG method)
- Wash cells at 37°C to eliminate cold agglutinin interference
- DAT will show C3d; ignore any IS/RT agglutination (artefactual)
- Treatment: Rituximab ± bendamustine; sutimlimab (anti-C1s); avoid cold triggers

### 5C. Paroxysmal Cold Haemoglobinuria (PCH)

- Biphasic IgG Donath-Landsteiner antibody; binds at cold (anti-P specificity), fixes complement, lyses at 37°C
- DAT: C3d positive; IgG may be weakly positive or negative
- Donath-Landsteiner test: incubate serum + normal RBCs at 4°C then 37°C → haemolysis = positive
- Clinical: haemoglobinuria, acute haemolysis, often post-viral in children; self-limiting
- Transfusion: Use pre-warmed blood; blood warmer; P-negative blood ideal but rarely available and not usually necessary; supportive management

### 5D. Drug-Induced Immune Haemolytic Anaemia (DIIHA)

**Mechanisms:**

| Mechanism | Drug Examples | DAT | Eluate | Action |
|----------|--------------|-----|--------|--------|
| Drug adsorption (hapten) | High-dose IV Penicillin, Cephalosporins (some) | IgG +; may be strong | Reacts with drug-coated cells ONLY | Stop drug; haemolysis resolves |
| Immune complex (ternary complex) | Quinine, quinidine, cephalosporins, NSAIDs, many others | C3d ± IgG; variable | Negative or reacts only with drug present | Stop drug; acute severe haemolysis possible |
| Non-immunological protein adsorption (NIPA) | Cephalosporins, oxaliplatin | IgG +; non-haemolytic | Negative (no antibody — protein adsorption) | No haemolysis; clinically insignificant |
| True autoantibody induction | Methyldopa (alpha-methyldopa), fludarabine, procainamide | IgG + (warm AIHA pattern) | Panreactive (mimics warm AIHA) | Stop drug; steroid if severe; months to resolve |
| Daratumumab (anti-CD38) | Daratumumab (multiple myeloma) | ALL DATs positive; panreactive serum | Difficult to interpret | Use DTT-treated RBCs (destroys CD38) for phenotyping; FLOWcytometry; use reagent cells treated with DTT |

### 5E. Autoantibody Interference — Finding Hidden Alloantibodies

**Problem:** Warm autoantibody causes panagglutination, masking underlying alloantibodies that could cause acute haemolytic transfusion reactions.

**Strategy:**
1. Autoadsorption (non-transfused) or allogeneic adsorption (recently transfused)
2. ZZAP treatment of patient cells (removes bound antibody and prepares cells for autoadsorption)
3. PEG-enhanced adsorption (more efficient antibody removal)
4. Adsorb with R1R1, R2R2, and rr cells (or equivalent Rh combinations) to detect Rh, Kell, Duffy, Kidd alloantibodies
5. Test adsorbed sera on panels — any residual specificity = alloantibody
6. Molecular RBC genotyping: provides patient's own antigen profile without serological interference — send to reference laboratory

---

## PHASE 6 — CROSSMATCH INTERPRETATION

### 6A. Crossmatch Types

**Major Crossmatch** (most important): Patient serum/plasma + Donor RBCs
- Detects antibodies in patient that react with donor cells
- Phases: IS (ABO check) → 37°C → AHG (definitive compatibility check)
- Compatible = no agglutination at AHG phase
- Incompatible at AHG = clinically significant antibody against donor — DO NOT TRANSFUSE

**Minor Crossmatch** (donor serum + patient RBCs):
- Now rarely performed routinely (all donor plasma tested for antibodies)
- Still required for: plasma-containing components (FFP, platelets) in some labs; neonatal exchange transfusion
- Positive minor: donor has antibody against patient's antigens

**Electronic Crossmatch (E-XM):**
- Computer/LIS-based matching of patient and donor ABO/Rh groups
- Only valid if: ≥2 concordant ABO typings on file, antibody screen NEGATIVE (current sample ≤3 days old), no historical clinically significant alloantibodies
- NOT appropriate for: positive antibody screen, known alloantibodies, positive DAT, emergency situations

**Immediate Spin (IS) Crossmatch:**
- ABO incompatibility check only
- Much faster; acceptable if antibody screen negative and no prior alloantibodies
- Does NOT replace AHG crossmatch if alloantibodies known or screen positive

### 6B. Crossmatch Result Interpretation

| Crossmatch Result | Interpretation | Action |
|------------------|----------------|--------|
| Compatible IS + AHG | Serologically compatible | Issue blood; monitor patient |
| Incompatible IS only | ABO incompatibility OR cold agglutinin | Check ABO type again urgently; never issue ABO-incompatible blood |
| Incompatible AHG | Alloantibody to donor antigen | Identify antibody; select antigen-negative donors; re-crossmatch |
| Incompatible in all donors | Panreactive antibody (autoantibody likely) | DAT; warm AIHA workup; adsorption studies |
| Incompatible with some donors | Specific alloantibody likely | Panel to confirm specificity; select antigen-negative |
| Mixed field at AHG | Recent transfusion, weak antibody, mixed chimerism | Document; clinical correlation; repeat if clinically significant |

### 6C. Emergency Transfusion — Uncrossmatched Blood

| Scenario | Product to Issue | Notes |
|---------|----------------|-------|
| Life-threatening emergency, no sample | Group O Rh(D)-negative RBCs | Universal donor; minimise use |
| ABO type known, no crossmatch complete | ABO- and Rh-compatible RBCs | Issue with "emergency release" documentation |
| Crossmatch in progress, immediate need | ABO/Rh-compatible (IS crossmatch only) | Document; complete AHG crossmatch on parallel sample |
| Known alloantibody, emergency | Antigen-negative ABO/Rh-compatible | Contact reference lab; alert Blood Centre |

**Rule:** NEVER withhold blood in a life-threatening emergency due to serological incompatibility alone. Document fully and notify consultant haematologist/transfusion medicine specialist.

---

## PHASE 7 — ANTIBODY TITRATION

### 7A. Titration Principles

- Titration quantifies antibody strength by serial doubling dilutions (1:1, 1:2, 1:4, 1:8 ... 1:4096)
- The TITRE = highest dilution showing definite (1+) agglutination at the relevant phase (usually AHG)
- The SCORE = numerical total using graded reactions to allow more sensitive comparison
- Always test current and previous sample IN PARALLEL for accurate trend assessment (freeze prior samples at -20°C)
- Method: LISS-IAT recommended (most sensitive, most reproducible); same method must be used for serial comparisons

### 7B. Critical Antibody Titres — HDFN Monitoring

| Antibody | Critical Titre | Action at Critical Titre |
|---------|---------------|--------------------------|
| Anti-D | ≥16 (some centres ≥32) | MCA Doppler monitoring every 1–2 weeks; refer to Fetal Medicine Unit |
| Anti-c | ≥16 | As for anti-D; anti-c causes late-onset anaemia |
| Anti-K | ANY titre | All anti-K pregnancies require Doppler monitoring regardless of titre (suppresses erythropoiesis rather than haemolysis) |
| Anti-E | ≥16 | MCA Doppler; consider paternal typing |
| Anti-Fya | ≥32 | MCA Doppler monitoring |
| Anti-Jka | ≥8 (low threshold due to waning) | MCA Doppler; Kidd antibodies notorious for causing DHTR |
| Anti-S, Anti-s | ≥32 | MCA Doppler |
| Anti-M (IgG) | ≥16 | MCA Doppler; rare IgG anti-M can cause severe HDFN |

**Quantification vs Titration:**
- Anti-D and anti-c: Use QUANTIFICATION (IU/mL using national reference standard) rather than titration where available
  - Anti-D <4 IU/mL → Low risk; monitor monthly
  - Anti-D 4–15 IU/mL → Moderate risk; fortnightly MCA Doppler
  - Anti-D >15 IU/mL → High risk; weekly MCA Doppler; consider cordocentesis
  - Anti-D >100 IU/mL → Very severe; immediate fetal medicine referral
- Anti-c: critical level >7.5 IU/mL

---

## PHASE 8 — SPECIAL CLINICAL POPULATIONS

### 8A. Sickle Cell Disease (SCD) — Chronic Transfusion Programme

**Pre-transfusion phenotyping requirements:**
- Full Rh phenotype: D, C, c, E, e, G (to prevent anti-C, anti-E, anti-c, anti-e formation)
- Kell: K (avoid K-positive blood)
- At minimum: Rh + K matched (most effective in preventing new alloantibodies)
- Extended: Rh + Kell + Duffy (Fya) + Kidd (Jka) + MNS (S) recommended by AABB/BSH

**Alloimmunisation rates in SCD:**
- 30–50% in chronically transfused SCD patients (vs 2–6% general population)
- High frequency due to: mismatch between donor (predominantly Caucasian) and recipient (predominantly African) antigen profiles
- Variant Rh antigens (RhCe, Rh32, Rh variant) common in African patients → serological typing unreliable → molecular genotyping essential

**Molecular RBC Genotyping in SCD:**
- BioArray/BeadChip (Immucor): types for 35+ blood group antigens simultaneously
- Critical for: patients with multiple alloantibodies, post-transfusion patients (mixed populations), identifying variant Rh
- Enables extended phenotype matching programme
- Result must be interpreted alongside serological results

**SCD Transfusion Types:**
- Simple transfusion: chronic anaemia, pre-operative; target Hb 10 g/dL, HbS <30–40%
- Exchange transfusion: acute stroke, ACS, priapism, multi-organ failure; reduces HbS to <30%
- Automated red cell exchange (erythrocytapheresis): preferred for exchange; reduces iron loading
- Iron overload monitoring: serum ferritin ≥1000 ng/mL indicates overload; liver MRI (T2*) definitive
- Chelation: required when ferritin persistently >1000 µg/L

### 8B. Thalassaemia — Chronic Transfusion Programme

**Requirements:**
- Extended phenotype: Rh (D, C, c, E, e) + Kell (K, k) + MNS (S, s) + Duffy (Fya, Fyb) + Kidd (Jka, Jkb)
- Leucodepleted blood mandatory
- Pre-storage leucodepletion reduces febrile reactions and HLA alloimmunisation
- Target Hb pre-transfusion: 9.5–10.5 g/dL; post-transfusion: 13–14.5 g/dL
- Iron chelation essential: transfusion iron burden ~200 mg/unit

**Alloimmunisation in thalassaemia:**
- Rate 5–30% in regularly transfused patients
- Most common: anti-E, anti-c, anti-K, anti-Jka
- Extended matching significantly reduces new alloantibody formation
- Once alloimmunised: finding compatible blood increasingly difficult — early molecular genotyping essential

### 8C. Obstetric / Antenatal Patients

**First trimester (booking visit):**
- ABO and Rh(D) type ALL pregnant women
- Antibody screen ALL pregnant women
- If positive screen → identify antibody; assess HDFN risk; repeat screen each trimester

**Rh(D)-negative mothers — RhIG prophylaxis:**
- 28 weeks gestation: routine antenatal anti-D prophylaxis (RAADP) — 1500 IU or 1000 IU × 2 doses
- After delivery: if baby Rh(D)-positive → 500–1500 IU RhIG within 72h (Kleihauer-Betke test for large FMH)
- Sensitising events requiring additional RhIG: miscarriage, ectopic pregnancy, amniocentesis, CVS, antepartum haemorrhage, ECV
- NB: RhIG passive anti-D should not be confused with immune anti-D — perform titre at 28 weeks and compare to previous

**Kleihauer-Betke (KBT) / Flow Cytometry FMH quantification:**
- Indicates volume of fetal cells in maternal circulation after potential FMH
- Calculate dose: Volume FMH (mL) ÷ 500 mL = vials of 500 IU RhIG (plus 1 extra)
- Flow cytometry more sensitive and reproducible than KBT (especially in ABO-compatible FMH)
- Required: after any delivery, trauma, or sensitising event in Rh-negative mothers

**Antibody monitoring in pregnancy:**
- All clinically significant antibodies: repeat titre every 4 weeks until 28 weeks; 2-weekly after 28 weeks
- Critical titres (see Phase 7B): refer to Fetal Medicine Unit
- MCA Doppler measurement of Peak Systolic Velocity (PSV) > 1.5 MoM = fetal anaemia requiring intrauterine transfusion (IUT)

**Intrauterine Transfusion (IUT) blood selection:**
- Group O Rh(D)-negative (unless mother's ABO known and anti-A/B absent)
- CMV seronegative OR leucodepleted
- Irradiated (to prevent transfusion-associated graft-versus-host disease, TA-GvHD)
- Antigen-negative for all maternal antibodies
- Less than 5–7 days old
- Crossmatch compatible with maternal serum
- Haematocrit 0.75–0.85 (to limit volume)

### 8D. Neonatal Transfusion

**Neonatal crossmatch rules:**
- Crossmatch against MATERNAL serum (not neonatal) — maternal antibodies are the clinical risk
- Use maternal sample if available; if not, cord blood or neonatal sample
- Group O Rh-negative is safest for emergency neonatal transfusion
- Crossmatch-compatible with maternal antibodies until 4 months of age (or until maternal antibodies no longer detectable)

**Neonatal HDFN management:**
- Cord blood: ABO/Rh type, DAT, bilirubin, haemoglobin
- Positive cord DAT: identify antibody by eluate; monitor bilirubin carefully (phototherapy threshold)
- Exchange transfusion criteria: bilirubin approaching exchange level on nomogram; severe anaemia; hydrops
- Exchange blood: same volume calculation (2× blood volume = 160–200 mL/kg)

**Neonatal/Infant transfusion thresholds:**
- Age <24h, Hb <12 g/dL with symptoms → transfuse
- Age 1–7 days, Hb <10 g/dL on ventilator → transfuse
- Age >7 days, Hb <7 g/dL stable → transfuse

### 8E. Transplant Patients

**Solid organ transplant — blood group considerations:**
- ABO compatibility: critical for kidney, heart, liver (ABO-incompatible solid organ transplant protocols exist in some centres; require special management)
- Haematopoietic stem cell transplant (HSCT): recipient may develop donor's blood group over time
- Recipient's own antibodies persist for months → crossmatch against DONOR cells post-transplant
- Passenger lymphocyte syndrome (PLS): donor B-lymphocytes produce antibodies against recipient RBC antigens → DAT positive; ABO/Rh haemolysis (especially minor ABO-mismatched transplants)
- CMV matching: CMV-seronegative recipients require CMV-negative or leucodepleted products

**Irradiated blood products — when mandatory:**
- All patients post-allogeneic HSCT (lifetime)
- All patients post-autologous HSCT (6–12 months)
- Patients receiving purine analogue chemotherapy (fludarabine, cladribine, deoxycoformycin) — lifetime
- Congenital immunodeficiency
- Intrauterine transfusion and transfusion of premature neonates
- HLA-selected/platelets from first-degree relatives
- Aplastic anaemia patients (some protocols)

### 8F. Oncology / Haematological Malignancy

**Daratumumab (anti-CD38) interference:**
- Daratumumab binds CD38 on RBCs → panagglutination; positive DAT; interferes with ALL crossmatches and antibody screens
- Management:
  1. Type and antibody screen BEFORE starting daratumumab (pre-treatment sample archived)
  2. Use DTT (dithiothreitol)-treated reagent RBCs (destroys CD38; eliminates daratumumab reactivity)
  3. May still have residual Kell system interference (DTT also denatures Kell antigens — provide Kell-typed blood or check with genotyping)
  4. Genotype patient (molecular) for extended phenotype

**Rituximab:**
- Anti-CD20 used in B-cell disorders; AIHA can develop or worsen post-rituximab
- May suppress new alloantibody formation (reduces risk) but can also unmask auto-reactivity
- DAT monitoring monthly during treatment

**ITP (Immune Thrombocytopenic Purpura) — platelet refractoriness:**
- Anti-HPA (human platelet antigen) antibodies: most common HPA-1a alloimmunisation
- ABO-compatible platelets preferred
- HLA-matched platelets for alloimmunised patients (HLA antibody-mediated refractoriness)
- Crossmatch-compatible platelets (Colnect or solid-phase RBC adherence test)
- 1h post-transfusion count increment (CCI) < 7.5 × 10⁹/L = platelet refractoriness

---

## PHASE 9 — BLOOD COMPONENT TRANSFUSION GUIDANCE

### 9A. Red Cell Transfusion (Packed RBCs / PRBC)

**Standard compatibility requirements:**
1. ABO and Rh(D) compatible
2. Antibody screen negative (or alloantibodies identified and antigen-negative blood selected)
3. Crossmatch compatible (major crossmatch at AHG phase, or electronic if qualified)
4. Leucodepleted (universal in UK; recommended in all settings — reduces febrile reactions, HLA alloimmunisation, CMV transmission, immunomodulation)

**Thresholds for RBC transfusion (NICE 2015 / BSH 2016):**
- Hb <7 g/dL (symptomatic) → transfuse (1 unit at a time; reassess after each)
- Hb 7–8 g/dL + symptoms (palpitations, breathlessness, orthostatic hypotension) → consider transfusing
- Hb 8–10 g/dL post-cardiac surgery, ACS, or symptomatic anaemia → consider
- Target post-transfusion Hb: typically 8–10 g/dL; NOT maximum possible
- Pre-operative: correct anaemia with haematinics if time allows; avoid peri-operative transfusion

**Volume:** 1 adult unit ≈ raises Hb by 1 g/dL; Paediatric: 10–15 mL/kg raises Hb by 2–3 g/dL

**Special attributes:**

| Attribute | When Needed | Indication |
|-----------|-----------|-----------|
| Leucodepleted | Universal (UK); standard | CMV risk reduction; febrile reactions; HLA alloimmunisation |
| CMV-seronegative | CMV-negative seronegative immunocompromised | Prevent primary CMV; leucodepletion is equivalent in most settings |
| Irradiated | See 8E above | Prevent TA-GvHD |
| Washed | IgA-deficient patients; severe allergic reactions; neonatal/IUT | Remove plasma proteins |
| HbS-negative | IUT; SCD; neonates | Avoid sickling in stored units |
| Phenotypically matched | SCD, thalassaemia, patients with multiple alloantibodies | Prevent further alloimmunisation |
| Freshest available | Exchange transfusion; neonates; IUT | Reduces potassium load |

### 9B. Platelet Transfusion

**ABO compatibility:**
- Use ABO-compatible platelets where possible (plasma contains anti-A/anti-B)
- ABO-compatible preferred (better survival); ABO-incompatible acceptable if no compatible available
- Rh(D)-compatible preferred (platelets may contain trace RBCs); if Rh(D)-positive given to Rh(D)-negative: consider RhIG (adult female premenopausal: 1500 IU covers 4 weeks of regular platelet transfusions with Rh(D)-positive apheresis platelets)

**Thresholds:**
- Prophylactic (haematology, no active bleeding): Plt <10 × 10⁹/L
- Prophylactic (fever, antibiotics, rapid count fall): Plt <20 × 10⁹/L
- Invasive procedures (LP, liver biopsy, CVC insertion): Plt >50 × 10⁹/L
- Major surgery, CNS surgery, ophthalmology: Plt >80–100 × 10⁹/L
- Active bleeding (trauma/surgical): Plt >50 × 10⁹/L (target >100 for CNS bleeding)
- DIC: correct underlying cause; transfuse Plt <50

**Volume:** 1 adult therapeutic pool ≈ raises Plt by 20–40 × 10⁹/L
**Special:** Irradiation when required (same indications as RBC); HLA-matched for alloimmunised patients

### 9C. Fresh Frozen Plasma (FFP)

**Indications:**
- Active haemorrhage + PT/APTT >1.5× normal
- Massive haemorrhage (use in ratio with RBC — 1:1 or 1:1:1 FFP:Plt:RBC)
- TTP (plasma exchange, not simple transfusion)
- Reversal of warfarin (if PCC not available and urgent)
- Rare coagulation factor deficiencies where factor concentrate not available
- DIC with bleeding

**ABO compatibility required** (major consideration: patient may have anti-A or anti-B; FFP of wrong ABO group can cause haemolysis in small patients)
- Best: ABO-identical
- Acceptable: ABO-compatible (Group A FFP to Group O patient: avoid; Group AB FFP: universal donor for FFP)
- Rh(D) matching: not required for FFP (no RBCs)

**Dose:** 10–15 mL/kg; raises individual factors by ~10–20%

### 9D. Cryoprecipitate

**Contains:** Fibrinogen (150–300 mg/unit), Factor VIII (80–120 IU/unit), vWF (100–200 IU/unit), Factor XIII, fibronectin

**Indications:**
- Fibrinogen <1.0–1.5 g/L with active bleeding (or prophylactically if <0.5 g/L)
- DIC with haemorrhage (fibrinogen replacement)
- Von Willebrand disease when DDAVP ineffective and vWF concentrate not available
- Haemophilia A (if Factor VIII concentrate unavailable — emergency only)
- Factor XIII deficiency
- Massive haemorrhage protocol (included in 1:1:1:1 ratio some protocols)

**ABO compatibility:** Preferred but not mandatory (small volume of plasma)
**Dose:** 10 units (pooled cryoprecipitate pool) raises fibrinogen by ~1 g/L in 70 kg adult

### 9E. Factor Concentrates

| Concentrate | Clinical Use |
|------------|-------------|
| Factor VIII (recombinant/plasma-derived) | Haemophilia A; also used in some vWD types |
| Factor IX (recombinant/plasma-derived) | Haemophilia B (Christmas disease) |
| Prothrombin Complex Concentrate (PCC) | Warfarin reversal; factor II, VII, IX, X deficiency |
| Activated PCC (FEIBA) | Haemophilia with inhibitors |
| rFVIIa (NovoSeven) | Haemophilia with inhibitors; refractory trauma haemorrhage (off-label) |
| Fibrinogen concentrate | Fibrinogen deficiency/hypofibrinogenaemia; replacing cryoprecipitate in some protocols |
| vWF concentrate (Haemate-P, Wilate) | Von Willebrand disease; haemophilia A with high-titre inhibitors (some protocols) |
| Anti-thrombin (AT) concentrate | AT deficiency; HIT; DIC management |
| Protein C concentrate | Protein C deficiency; severe sepsis (historical) |
| C1-Inhibitor concentrate | Hereditary angioedema |

---

## PHASE 10 — OUTPUT FORMAT: IMMUNOHAEMATOLOGY REPORT

### 🔬 IMMUNOHAEMATOLOGY ASSESSMENT REPORT

**Patient:** Age ___ | Sex ___ | Sample ID: ___
**Date:** ___ | **Method:** [Gel CAT / Tube LISS / PEG / Enzyme / Solid Phase]
**ABO/Rh Group:** ___
**Clinical Context:** ___
**Transfusion/Obstetric History:** ___
**Medications:** ___

---

#### SECTION 1: 🚨 IMMEDIATE SAFETY ALERT

*(Always completed first)*

| Issue | Result | Risk | Action Required |
|-------|--------|------|----------------|
| ABO incompatibility | [result] | FATAL | 🚨 STOP — DO NOT ISSUE LABELLED UNIT |
| Critical alloantibody (Jka — waning pattern) | [result] | Severe DHTR | 🚨 Antigen-negative blood mandatory |
| Positive DAT + active haemolysis | [result] | Ongoing haemolysis | 🚨 Haematology urgent referral |
| Anti-D in Rh-negative pregnant woman | [result] | HDFN risk | 🚨 Fetal Medicine referral |

*State "No immediate safety alerts" if none.*

---

#### SECTION 2: BLOOD GROUP TYPING

| Test | Result | Interpretation |
|------|--------|---------------|
| Forward ABO (cell group) | Anti-A: __ Anti-B: __ | Group ___ |
| Reverse ABO (serum group) | A1 cells: __ B cells: __ | Confirms Group ___ |
| Rh(D) typing | IS: __ / IAT: __ | D-positive / D-negative / Weak D / Partial D |
| Extended Rh phenotype | C:__ c:__ E:__ e:__ | Rh phenotype: ___ |
| Kell | K:__ k:__ | K-positive/negative |
| ABO/Rh Concordant? | Yes / No — discrepancy noted | [Detail discrepancy and action] |

---

#### SECTION 3: ANTIBODY SCREEN RESULT

| Phase | Screen Cell 1 | Screen Cell 2 | Screen Cell 3 | Autocontrol | Overall |
|-------|-------------|-------------|-------------|-------------|---------|
| IS | | | | | |
| 37°C | | | | | |
| AHG | | | | | |

**Screen Interpretation:** Positive / Negative / Equivocal
**Autocontrol:** Negative (alloantibody) / Positive (proceed to DAT/autoantibody workup)

---

#### SECTION 4: ANTIBODY IDENTIFICATION PANEL ANALYSIS

**Panel used:** [ID-DiaPanel lot ____ / Surgiscreen lot ____ / Other]
**Phase(s) tested:** IS / 37°C / AHG / Enzyme

| Cell | Rh phenotype | Key antigens expressed | Result | Phase |
|------|-------------|----------------------|--------|-------|
| 1 | | | | |
| [continue for all cells] | | | | |
| Autocontrol | — | — | | |

**Rule-out table:**

| Antibody | Rule-out cells (antigen+, unreacted) | Ruled Out? | Notes |
|---------|-------------------------------------|-----------|-------|
| Anti-D | | Yes/No | |
| Anti-C | | | |
| [continue for all antigens] | | | |

**Rule-in evidence:**

| Proposed Antibody | Reactive cells (antigen+) | Non-reactive cells (antigen-) | Pattern consistent? |
|------------------|--------------------------|------------------------------|---------------------|
| Anti-___ | Cells __ , __ | Cells __ , __ | Yes / No |

**Statistical significance:** p = __ (Fisher's exact or equivalent)
**Dosage effect noted:** Yes / No — [specify if stronger with homozygous cells]
**Enzyme panel results:** [if performed]

---

#### SECTION 5: DAT RESULT & ELUATE

| DAT — Polyspecific | Anti-IgG | Anti-C3d | Anti-IgA (if tested) | Anti-IgM (if tested) |
|-------------------|---------|--------|---------------------|---------------------|
| [Grade] | [Grade] | [Grade] | [Grade] | [Grade] |

**Eluate:** [if performed]
- Eluate vs panel: [all cells reactive / specific cells reactive / non-reactive]
- Eluate specificity: [Panagglutinin (warm AIHA) / Anti-___ / Non-reactive]

---

#### SECTION 6: ANTIBODY IDENTIFICATION CONCLUSION

**Identified Antibody(ies):** Anti-___ [confidence: high / probable / possible]
**Clinical Significance:** Clinically significant / Insignificant / Uncertain
**Mechanism:** IgG (IAT) / IgM (IS) / Complement-activating / Mixed
**Dosage:** Demonstrated / Not demonstrated
**Enzyme enhancement/destruction:** Enhanced / Destroyed / Unaffected by enzyme
**Autoantibody component:** Present / Absent / Suspected
**Hidden alloantibody exclusion:** [list methods used — adsorption etc. and conclusion]

---

#### SECTION 7: CROSSMATCH RESULTS

| Donor Unit | ABO/Rh | IS | 37°C | AHG | Interpretation |
|-----------|--------|-----|------|-----|---------------|
| [Unit ID] | | | | | Compatible / Incompatible |

**Crossmatch Interpretation:** Compatible / Incompatible
**Reason for incompatibility:** [if applicable]
**Recommended action:** [Issue / Do not issue / Repeat / Reference lab]

---

#### SECTION 8: INTEGRATED CLINICAL INTERPRETATION

**Primary serological finding:** [e.g., "Anti-E + Anti-c identified; IgG; AHG phase; dosage effect present"]
**Clinical significance:** [Impact on transfusion, pregnancy, future testing]
**Patient phenotype concordance:** [Patient confirmed E-negative, c-negative — consistent with antibody formation]
**Special situation assessment:** [SCD / thalassaemia / obstetric / autoimmune]

---

#### SECTION 9: COMPONENT SELECTION RECOMMENDATION

| Component | Requirements | Compatibility |
|-----------|-------------|--------------|
| Red cells | ABO group __ ; Rh __ ; E-negative; c-negative; Leucodepleted | Crossmatch-compatible |
| Platelets (if required) | ABO-compatible; Rh(D) considerations | |
| FFP (if required) | ABO group __ | |
| Special attributes | [Irradiated / CMV-negative / HbS-negative / Phenotypically matched] | |

**Antigen-negative prevalence (to guide stock planning):**
- E-negative: ~71% of donors
- c-negative: ~80% of donors
- E-negative AND c-negative: ~55% of donors
- (Adjust for local donor pool demographics)

---

#### SECTION 10: ACTION PLAN

**IMMEDIATE:**
- [ ] [Critical safety action — ABO check / do not issue / emergency notification]

**SHORT-TERM (within 24–48h):**
- [ ] [Confirm antibody with additional cells / enzyme panel / reference lab]
- [ ] [Extended phenotype patient's RBCs]
- [ ] [Notify patient's haematologist / obstetrician / primary team]

**ONGOING MANAGEMENT:**
- [ ] [Add permanent antibody alert to patient record — blood bank sticker / wristband / electronic flag]
- [ ] [Antibody card issued to patient]
- [ ] [Titration schedule if obstetric patient]
- [ ] [Molecular genotyping referral — if extended matching required]
- [ ] [Reference laboratory referral — if unresolved or high complexity]

**CLINICIAN GUIDANCE:**
- [ ] [Inform clinician of compatibility status]
- [ ] [Estimated time to find compatible blood]
- [ ] [Alternative strategies if compatible blood unavailable]

---

#### SECTION 11: BRIEF CLINICAL CONCLUSION

> *[3–5 sentence plain-language summary: what was found, its clinical significance, what blood to give, most important immediate action.]*

---

## PHASE 11 — IMAGE-SPECIFIC INTERPRETATION: UPLOADED PANELS

### Analysis of Images 1, 2, 3, 4 (Patient Case Example — *Synthetic, de-identified*)

> *Synthetic, de-identified example.* Panel lot numbers and dates below are invented placeholders (year 2099) and do not correspond to any real reagent lot, patient, sample or laboratory run. The serological reasoning is unchanged.

**Image 1 (Bio-Rad ID-DiaPanel — Panel A):**
Lot: SYN-LOT-A-0001 (synthetic) | Date: 2099.01.01 (synthetic) | Method: Gel CAT (IAT)

Panel Results:
| Cell | Rh | Result (IAT) | Notes |
|------|-----|-------------|-------|
| 1 | CCC\*D.ee (R₁ᵂR₁) | +1 | |
| 2 | CCD.ee (R₁R₁) | +2 | Donor note: Co(b+)\* |
| 3 | ccD.EE (R₂R₂) | +3 | |
| 4 | Ccddee (r'r) | +4 | |
| 5 | ccddEe (r"r) | 0 | |
| 6 | ccddee (rr) | +2 | |
| 7 | ccddee (rr) | 0 | |
| 8 | ccD.ee (R₀r) | +1 | |
| 9 | ccddee (rr) | +2 | HLA+\* |
| 10 | ccddee (rr) | +3 | |
| 11 | ccddee (rr) | 0 | |

**Image 2 (Ortho Surgiscreen — 3-cell screen):**
| Cell | Rh | Result |
|------|-----|-------|
| 1 | R₁ᵂR₁ | +2 |
| 2 | R₂R₂ | +2 |
| 3 | rr | 0 |

**Image 3 (Bio-Rad ID-DiaPanel — Panel B, different lot):**
Lot: SYN-LOT-B-0002 (synthetic) | Date: 2099.01.29 (synthetic) | Autocontrol: 0

| Cell | Rh | Result (IAT) | Notes |
|------|-----|-------------|-------|
| 1 | CCC\*D.ee | 0 | |
| 2 | CCD.ee | 0 | |
| 3 | ccD.EE | 0 | |
| 4 | Ccddee (r'r) | +2 | |
| 5 | ccddEe (r"r) | 0 | HLA+\* |
| 6 | ccddee (rr) | 0 | |
| 7 | ccddee (rr) | 0 | |
| 8 | ccD.ee (R₀r) | 0 | |
| 9 | ccddee (rr) | 0 | |
| 10 | ccddee (rr) | 0 | |
| 11 | ccddee (rr) | +2 | |

**Image 4 (ID-DiaPanel-P — Empty template):** Reference worksheet only (no patient results entered)

---

### INTERPRETATION OF PATIENT CASE (Images 1–3):

**Step 1 — Autocontrol:** Image 3 shows A.C = 0 (negative). This is critical — confirms the antibody is most likely an ALLOANTIBODY, not an autoantibody. Proceed with alloantibody identification.

**Step 2 — Surgiscreen (Image 2):**
- Cell 1 (R₁ᵂR₁): +2 — This cell expresses D, C, Cw. Not e-negative; not c-negative.
- Cell 2 (R₂R₂): +2 — This cell expresses D, c, E. Notably c-positive and E-positive.
- Cell 3 (rr): 0 — Negative. This cell is D-negative, c-positive, e-positive, no C, no E.
- Pattern: Reacting with R₁R₁ (+2) AND R₂R₂ (+2), NOT with rr (0)
- Cells 1 and 2 share: D (in both). But also: Cell 1 has C/no E; Cell 2 has E/no C. Both have D.
- This is consistent with anti-D, or a combination. However, the rr cell is c-positive and negative — rules out anti-c. Need full panel to clarify.

**Step 3 — Panel A (Image 1) Analysis:**

Reactive cells: 1 (+1), 2 (+2), 3 (+3), 4 (+4), 6 (+2), 8 (+1), 9 (+2), 10 (+3)
Non-reactive cells: 5 (0), 7 (0), 11 (0)

Looking for common antigen on cells 1,2,3,4,6,8,9,10 but NOT on 5,7,11:

- Cell 5 (ccddEe): has no D, has E, has c — negative
- Cell 7 (ccddee): no D, no E, has c — negative
- Cell 11 (ccddee): no D, no E, has c — negative

Looking at D: Cells 1,2,3,8 are D-positive (all reactive). Cell 4 is D-negative (r'r = Ccddee) but is +4 — most reactive cell. Cell 6 is rr (ccddee) D-negative but +2. Cells 9,10 are rr (ccddee) D-negative but +2,+3. So D cannot be the sole target — D-negative cells ARE reactive.

Looking at C: Cell 1 (CCC\*D.ee) has C — reactive. Cell 4 (Ccddee) has C — very reactive (+4). Cell 8 (ccD.ee) has NO C — reactive (+1). So C cannot be sole target.

Reconsidering: What's common to all REACTIVE cells (1,2,3,4,6,8,9,10) and ABSENT from all NEGATIVE cells (5,7,11)?

Cell 4 = Ccddee = has C, c, d (no D), no E — reaction +4
Cell 5 = ccddEe = has c, E, no C, no D — NEGATIVE
Cell 6 = ccddee = has c, no E, no C, no D — +2
Cell 7 = ccddee = rr — NEGATIVE
Cell 11 = ccddee = rr — NEGATIVE

Cells 6,7,11 are all ccddee (rr) — same phenotype! Yet 6 = +2, 7 = 0, 11 = 0. This suggests a SECOND ANTIBODY or additional antigen involved, OR HLA antibody (Cell 9 flagged HLA+).

Checking Cell 9 (rr with HLA+): +2. Cell 6 (rr): +2. Cell 7 (rr): 0. Cell 11 (rr): 0.

The additional differentiation between rr cells must be in non-Rh antigens. Looking at MNS, Duffy, Kidd columns across rr cells (6,7,9,10,11):

Cell 6: ccddee, rr — has specific Kell, MNS, Duffy, Kidd antigens (from panel design). Reactive.
Cell 7: ccddee, rr — different antigen combination. Non-reactive.
Cell 9: ccddee, rr — HLA+ flag; different non-Rh antigens. Reactive.
Cell 10: ccddee, rr — reactive +3.
Cell 11: ccddee, rr — non-reactive.

This pattern among the rr cells is crucial. The overall picture most likely represents:

**Panel A Preliminary Conclusion: MULTIPLE ANTIBODIES — likely anti-C + another antibody**

Anti-C evidence:
- Cell 4 (Ccddee, r'r) = +4 strongest reaction — homozygous for C (double dose C)
- Cell 1 (CCC\*D.ee) = +1 — C-positive
- Cell 2 (CCD.ee) = +2 — C-positive
- Cell 3 (ccD.EE) = +3 — *** c-positive, no C — this contradicts anti-C alone ***

So anti-C cannot be sole antibody either, as Cell 3 (ccD.EE — C-NEGATIVE) is reactive +3.

**Revised analysis — antibody directed at antigen(s) present on:**
- Cell 3 (ccD.EE) +3: has D, E, c
- Cell 4 (Ccddee r'r) +4: has C, c (no D, no E) — most reactive

What is shared between Cell 3 and Cell 4 that is absent from Cell 5 (ccddEe, negative) and Cell 11 (ccddee, negative)?

Cell 3 has: D, c, E (no C)
Cell 4 has: C, c (no D, no E)
Cell 5 has: c, E (no D, no C) — NEGATIVE
Cell 11 has: c (no D, no C, no E) — NEGATIVE

Shared between 3 and 4 but NOT 5: D (present in 3, absent in both 4 and 5 — no), C (in 4, not in 3)...

Actually the strongest clue: Cell 4 is maximally reactive (+4) and is Ccddee. Among reactive cells, the variation in strength (1,2,3,4,2,1,2,3) correlates with antigen expression. Most reactive = Cell 4 (Ccddee = homozygous C, homozygous c). This is the c homozygous double-dose expression (cc).

**Panel B (Image 3) — key verification:**
Cell 4 (Ccddee, r'r) = +2 only on Panel B
Cells 1,2,3 (D-positive) = ALL ZERO on Panel B
Cells 5–11 (except 4 and 11) = all ZERO

Panel B Cell 4 = +2 (C+, c+, no D, no E)
Panel B Cell 11 = +2 (rr, ccddee)

Between the two panels: Panel A shows broad reactivity; Panel B shows only Cells 4 and 11 reactive.

The reconciliation: Panel A was likely tested with a DIFFERENT serum (possibly before treatment or at a higher titre), OR Panel A shows multiple specificities and Panel B performed at a different time shows only residual weaker antibody.

**Most probable final interpretation:**

Given:
- Negative autocontrol on Panel B
- Surgiscreen: R₁R₁ +2, R₂R₂ +2, rr 0
- Panel A broad reactivity across D-positive AND some D-negative cells with C
- Panel B: only Cell 4 (r'r = Ccddee) and Cell 11 (rr) reactive

The most consistent identification is:

**Anti-C** — explains Cell 4 reactivity (C-homozygous = strongest reaction), Cell 1 (C+), Cell 2 (C+) on Panel A, and positive Surgiscreen cells 1 and 2 (both C+)

**PLUS an additional antibody to explain Cell 3 (ccD.EE, C-negative) being +3 and rr cell reactivity** — most likely **anti-E** (Cell 3 is EE homozygous, would give strong reaction) or anti-Rh antigen.

Panel B supports: Panel B Cell 4 (Cc) = +2, Cell 11 (rr ccddee — need antigen table) = +2. If Cell 11 has E+ antigen (from panel design) = anti-E may persist at lower titre.

**Working antibody identification: Anti-C + Anti-E (most probable)**
- Both are clinically significant IgG Rh alloantibodies
- Consistent with previous Rh sensitisation (transfusion or pregnancy)
- Patient is likely phenotype: D+/C-/E-/c+/e+ or variant

**Blood requirements:**
- C-negative AND E-negative
- ABO and Rh(D) compatible
- Leucodepleted
- Crossmatch compatible at AHG phase
- C-negative E-negative blood available in ~55% of donors

**Clinical urgency:** Proceed with reference laboratory confirmation. Provide patient with antibody alert card. All future transfusions must be C-negative and E-negative.

**HLA antibody note (Cells 5, 9 flagged):** These are informational flags indicating donor cells with known HLA antigens that may cause false reactions in patients with HLA antibodies. Do not interpret HLA flags as alloantibody confirmation. However, consider requesting leucodepleted blood to reduce HLA alloimmunisation risk going forward.

---

## SKILL USAGE NOTES

### Trigger phrases:
"Interpret this antibody identification panel", "What antibody does this panel show?", "Interpret my crossmatch result", "Is this DAT positive significant?", "What blood can I give this patient?", "Interpret my ID-DiaPanel results", "What does this Surgiscreen show?", "Interpret antibody titration", "HDFN monitoring", "Sickle cell transfusion advice", "Patient has warm autoantibody — what blood?", "Antenatal antibody found", "How do I manage this complex antibody case?", "Crossmatch incompatible — what now?"

### Mandatory inputs:
1. Panel image(s) or typed results
2. Patient ABO/Rh type
3. Patient age and sex
4. Clinical context
5. Autocontrol result (CRITICAL)

### Always ask if not provided:
- Transfusion history (within last 3 months)
- Obstetric history
- Medications (especially daratumumab)
- Phase of testing performed
- Patient's known phenotype/genotype

### Output modes:
| Phrase | Output |
|--------|--------|
| Default | Full 11-section report |
| "quick interpretation" | Sections 1 + 6 + 9 + 11 |
| "crossmatch only" | Section 7 |
| "antibody ID only" | Sections 3–6 |
| "what blood to give?" | Sections 9 + 10 action |
| "DAT interpretation" | Section 5 only |
| "obstetric assessment" | Sections 8C + Phase 7 titration |
| "SCD transfusion advice" | Section 8A + 9A |

---

*EEHLSS / MedLabAI-LIS | Maintained by Echukwuka | Version 1.0 — April 2026*
*Aligned to: ISBT · AABB Technical Manual 20th Ed · BCSH/BSH Transfusion Guidelines · RCPath · ISO 15189:2022 · CBAHI · CAP Transfusion Medicine Checklist*
*All interpretations require validation by a qualified Biomedical Scientist, Medical Laboratory Scientist, or Transfusion Medicine Physician.*
*This skill provides expert decision support only — complex cases must be referred to a Transfusion Medicine specialist or Reference Laboratory.*
