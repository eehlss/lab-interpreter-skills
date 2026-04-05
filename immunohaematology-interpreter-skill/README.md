# Transfusion Medicine & Immunohaematology Interpreter — README

**Skill name:** `transfusion-medicine-interpreter`
**Developed by:** Echukwuka | EEHLSS / MedLabAI-LIS
**Version:** 1.0 | **April 2026**
**Standards:** ISBT · AABB Technical Manual 20th Ed · BCSH/BSH · RCPath · ISO 15189:2022 · CBAHI · CAP Transfusion Medicine Checklist

---

## What This Skill Does

This is a Claude AI skill that interprets immunohaematology results from your blood bank and transfusion laboratory. Upload a photograph or scan of any of the following and receive a structured clinical decision report:

- Antibody identification panels (Bio-Rad ID-DiaPanel, ID-DiaPanel-P, Ortho Surgiscreen, antigrams)
- Crossmatch worksheets (major, minor, immediate spin, AHG phase)
- DAT / Direct Antiglobulin Test (Coombs) results
- IAT / Indirect Antiglobulin Test results
- Blood group typing cards (ABO, Rh, extended phenotyping)
- Antibody titration worksheets

The skill applies a systematic 11-phase framework to produce a structured report covering:

1. Immediate safety alerts (ABO incompatibility, critical alloantibodies)
2. Blood group typing interpretation and discrepancy resolution
3. Antibody screen result
4. Antibody identification panel analysis (rule-out / rule-in logic, dosage effect, statistical significance)
5. DAT result and eluate interpretation
6. Antibody identification conclusion with confidence grading
7. Crossmatch result interpretation
8. Integrated clinical narrative
9. Blood component selection recommendation (RBC, platelets, FFP, cryoprecipitate, factor concentrates)
10. Action plan (immediate, short-term, ongoing monitoring)
11. Brief plain-language clinical conclusion

---

## What Information You Need to Provide

### Always required:
1. **Image(s)** of the panel worksheet(s) — photograph from your phone is fine; ensure the entire panel grid and results column are visible
2. **Patient ABO and Rh(D) type**
3. **Patient age** and **biological sex**
4. **Clinical context** — e.g., "routine pre-transfusion", "obstetric/antenatal", "haemolytic anaemia investigation", "post-transfusion reaction", "sickle cell disease chronic transfusion programme", "myeloma on daratumumab"
5. **Autocontrol result** — this is mandatory and changes the entire interpretation (positive autocontrol = autoantibody or recent transfusion alloantibody)

### The skill will ask you for the following if not provided:
- Transfusion history — number of units, how recent (especially within the last 3 months)
- Obstetric history — gravidity, parity, previous HDFN, RhIG administration
- Phase of testing — IS (immediate spin), 37°C, AHG/IAT, enzyme
- Method used — gel/CAT, tube LISS, PEG, solid phase
- Patient's known red cell phenotype or genotype (if previously typed)
- Medications — especially daratumumab, rituximab, methyldopa, penicillin, cephalosporins, IVIG, RhIG

---

## How to Install

### Option A — Claude.ai Web or Mobile (Easiest — for individuals)

This is the simplest route for a colleague who uses Claude.ai and wants to start immediately.

**Step 1:** Sign in to [claude.ai](https://claude.ai) in your browser or the Claude mobile app.

**Step 2:** Go to **Settings → Custom Instructions** (the equivalent of a system prompt or persistent instruction field — the exact name may vary slightly by interface version).

**Step 3:** Open the `SKILL.md` file from this folder in any text editor — Notepad, VS Code, TextEdit, or even Microsoft Word (view as plain text).

**Step 4:** Copy the **entire contents** of the file and paste into the Custom Instructions field.

**Step 5:** Save. The skill is now active in your Claude.ai account. Every new conversation will have this skill applied automatically. Upload a panel image and ask for interpretation.

> **Character limit note:** The YAML description field at the top of SKILL.md has been specifically trimmed to 923 characters to stay under Claude's 1024-character field limit. Do not expand the description block — all the clinical content is in the body of the file, not the header.

---

### Option B — EEHLSS EVO X2 / Local Skills Folder

For the EEHLSS local Claude environment with a mounted `/mnt/skills/` directory:

**Step 1:** Copy the entire skill folder to the user skills directory:

```bash
cp -r transfusion-medicine-interpreter/ /mnt/skills/user/transfusion-medicine-interpreter/
```

**Step 2:** Verify the files are in place:

```bash
ls /mnt/skills/user/transfusion-medicine-interpreter/
# Should return: SKILL.md  README.md  RESEARCH_DEEP_DIVE.md
```

**Step 3:** Claude will auto-detect the skill from the `<available_skills>` block and trigger it automatically when you upload a panel image or use any of the trigger phrases listed below.

No restart or reloading needed — skills are read at the start of each conversation session.

---

### Option C — Claude API Integration (Developers / MedLabAI-LIS)

For embedding this skill into a custom application or laboratory information system via the Claude API:

**Step 1:** Read `SKILL.md` into a string in your application.

**Step 2:** Pass as the system prompt in your API call alongside the image and patient context:

```python
import anthropic
import base64

# Load skill
with open("SKILL.md", "r") as f:
    skill_content = f.read()

# Load panel image
with open("panel_image.jpg", "rb") as img:
    image_data = base64.b64encode(img.read()).decode("utf-8")

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    system=skill_content,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": image_data
                    }
                },
                {
                    "type": "text",
                    "text": """Interpret this antibody identification panel.
Patient: 45-year-old female. Group A Rh(D) positive.
Clinical context: Chronic transfusion programme, sickle cell disease.
Transfusion history: 22 units, last transfusion 6 weeks ago.
Autocontrol: Negative.
Phase of testing: AHG gel (CAT)."""
                }
            ]
        }
    ]
)

print(response.content[0].text)
```

**Step 3:** For FHIR R4 integration, the skill's structured output maps naturally to:
- `DiagnosticReport` resource for the full compatibility report
- `Observation` resources for individual antigen typing results
- `AllergyIntolerance` (or custom extension) for documented red cell alloantibodies
- `Flag` resource for permanent antibody alert entries in the patient record

---

### Option D — n8n Workflow Automation (EVO X2 Pipeline)

For automated panel interpretation triggered by incoming scanned images:

**Step 1:** Create an **HTTP Request** node in n8n pointing to `https://api.anthropic.com/v1/messages`.

**Step 2:** In the node's body, build the JSON payload:
- `system` = full contents of `SKILL.md` (stored as an n8n credential or variable)
- `messages[0].content` = array with `image` (base64) + `text` (patient context from preceding workflow nodes)
- `model` = `claude-opus-4-6`
- `max_tokens` = 4096

**Step 3:** Wire the output to an Email or Slack node for delivery to the Transfusion Medicine inbox.

**Step 4:** Trigger via:
- Webhook from your scanner/document management system when a new panel scan lands
- File watcher node monitoring a network folder for incoming `.jpg` / `.pdf` panel images
- Scheduled batch processing at end of each working shift

---

## How to Use the Skill — Step by Step

### Basic usage in Claude.ai

1. Open a new Claude conversation.
2. Upload your panel image (photo or scan — portrait orientation works best; ensure full grid is visible).
3. Type your request with patient context:

```
Interpret this antibody identification panel.
Patient: 38-year-old female.
Blood group: O Rh(D) positive.
Clinical context: Antenatal, 16 weeks gestation, G2P1.
Autocontrol: Negative.
Phase tested: AHG gel (ID-DiaPanel).
Previous obstetric history: First baby unaffected.
```

```
What antibody does this panel show?
Patient: 62-year-old male. Group B Rh(D) negative.
Context: Pre-operative crossmatch, elective hip replacement.
Transfusion history: 2 units 8 years ago.
Autocontrol: Negative.
```

```
Interpret my crossmatch results. Patient has known anti-E.
All 6 crossmatched units appear incompatible at AHG phase.
Patient: 28F, Group O Rh(D) positive. On daratumumab for myeloma.
Autocontrol: Positive (IgG 3+).
```

```
Is this DAT significant?
Patient: 3-day-old neonate. Mother is Group A Rh(D) negative with known anti-D titre 1:32.
Cord blood DAT: IgG 2+, C3d negative. Bilirubin rising.
```

---

### Output Modes — Controlling Report Length

Add these phrases to your message to get a shorter, focused output:

| What to type | What you receive |
|-------------|-----------------|
| *(nothing extra — default)* | Full 11-section structured report |
| `"quick interpretation"` | Safety alert + antibody conclusion + blood to give + brief conclusion only |
| `"crossmatch only"` | Crossmatch interpretation + component recommendation |
| `"antibody ID only"` | Sections 3–6: screen, panel analysis, DAT, antibody conclusion |
| `"what blood to give?"` | Component selection + action plan |
| `"DAT interpretation"` | DAT + eluate section only |
| `"obstetric assessment"` | Antenatal antibody + titration assessment + HDFN risk |
| `"SCD transfusion advice"` | Sickle cell transfusion programme guidance |
| `"emergency release"` | Emergency uncrossmatched blood guidance |

---

### Trigger Phrases

The skill activates automatically when you use any of the following alongside an uploaded image or typed results:

- "Interpret this antibody identification panel"
- "What antibody does this panel show?"
- "Interpret my crossmatch result"
- "Is this DAT positive significant?"
- "What blood can I give this patient?"
- "Interpret my ID-DiaPanel results"
- "What does this Surgiscreen show?"
- "Interpret antibody titration"
- "HDFN monitoring"
- "Sickle cell transfusion advice"
- "Patient has warm autoantibody — what blood?"
- "Antenatal antibody found — what do I do?"
- "How do I manage this complex antibody case?"
- "Crossmatch incompatible — what now?"
- "Daratumumab interference — how do I crossmatch?"

---

## Understanding the 11-Section Report

| Section | Contents |
|---------|----------|
| **1. Safety Alert** | Any ABO incompatibility, critical alloantibodies, or urgent actions — always first |
| **2. Blood Group Typing** | Forward and reverse ABO, Rh(D), extended phenotype, discrepancy resolution |
| **3. Antibody Screen** | Screen cell results by phase (IS, 37°C, AHG), autocontrol |
| **4. Panel Analysis** | Cell-by-cell rule-out / rule-in table; dosage effect; statistical significance; enzyme panel if tested |
| **5. DAT & Eluate** | Monospecific DAT (IgG/C3d); eluate specificity; clinical context |
| **6. Antibody Conclusion** | Named antibody(ies); confidence level; clinical significance; mechanism (IgG/IgM/complement) |
| **7. Crossmatch Results** | Unit-by-unit compatibility table; reasons for incompatibility |
| **8. Clinical Narrative** | Integrated synthesis — how all findings relate; overall pattern |
| **9. Component Selection** | What to transfuse: ABO, Rh, antigen-negative requirements, special attributes (irradiated, CMV-negative, phenotypically matched, HbS-negative, washed) |
| **10. Action Plan** | Tiered checklist: immediate → short-term → ongoing → clinician communication → instrument QC |
| **11. Brief Conclusion** | 3–5 sentence plain-language summary for lab report comment or verbal handover |

---

## Clinical Coverage — What the Skill Handles

### Blood Grouping & Discrepancy Resolution
ABO forward and reverse typing, subgroups (A2, A3, Ax, B(A)), Rh(D) typing including weak D and partial D, extended Rh (C, c, E, e) and Kell (K, k), ABO/Rh discrepancies with systematic investigation approach.

### Antibody Screen & Panel Interpretation
Systematic rule-out / rule-in logic for all clinically significant blood group antibodies across: Rh system (D, C, c, E, e, G, Cw, f), Kell system (K, k, Kpa, Kpb, Jsa, Jsb), Duffy system (Fya, Fyb, Fy3), Kidd system (Jka, Jkb, Jk3 — including waning antibody recognition), MNS system (M, N, S, s, U), Lewis (Lea, Leb), P1, high-prevalence antigens (Vel, Lan, Ata, Jr, U), plus multiple alloantibody mixtures. Includes dosage effect recognition, enzyme panel interpretation, and statistical significance calculation.

### DAT / Direct Antiglobulin Test
Polyspecific and monospecific (anti-IgG, anti-C3d, anti-IgA, anti-IgM) interpretation. Eluate interpretation. Full clinical context assessment including: warm AIHA (autoadsorption strategy, alloantibody exclusion), cold agglutinin disease (thermal range, titre significance), paroxysmal cold haemoglobinuria (Donath-Landsteiner), drug-induced immune haemolytic anaemia (hapten, immune complex, NIPA, true autoantibody mechanisms), passenger lymphocyte syndrome post-transplant, daratumumab and other drug interference.

### Crossmatch
Major crossmatch (IS, 37°C, AHG), minor crossmatch, electronic crossmatch eligibility, emergency uncrossmatched blood protocols, incompatible crossmatch management.

### Antibody Titration & HDFN
Serial titration methodology, critical titre thresholds for all HDFN-causing antibodies (anti-D, anti-c, anti-K, anti-E, anti-Fya, anti-Jka, anti-S, anti-M IgG), quantification vs titration (anti-D and anti-c in IU/mL), Kleihauer-Betke / flow cytometry FMH quantification, RhIG dose calculation, antenatal monitoring scheduling.

### Special Populations
Sickle cell disease (extended phenotyping requirements, molecular genotyping strategy, alloimmunisation prevention, hyperhemolysis syndrome recognition), beta-thalassaemia (chronic transfusion extended matching), obstetric patients (RhIG prophylaxis protocols, antenatal antibody monitoring, IUT blood selection), neonates (cord blood testing, crossmatch against maternal serum, exchange transfusion), transplant patients (HSCT chimerism, passenger lymphocyte syndrome, irradiation indications), oncology (daratumumab DTT method, rituximab considerations).

### Blood Component Selection
Full compatibility requirements and clinical thresholds for: red cell concentrates (standard and special attributes), platelets (ABO considerations, HLA matching for refractoriness, RhIG for Rh-incompatible platelets), FFP (ABO compatibility, indications, dose), cryoprecipitate (fibrinogen replacement, FVIII, vWF), factor concentrates (FVIII, FIX, PCC, activated PCC, rFVIIa, fibrinogen concentrate, vWF concentrate, antithrombin, C1-inhibitor).

---

## Important Limitations

This skill provides **clinical decision support** — it is not a replacement for a qualified Biomedical Scientist, Medical Laboratory Scientist, or Transfusion Medicine Physician.

- All outputs must be reviewed and validated by a qualified professional before any transfusion decision is made.
- Complex cases — particularly unresolved antibodies, suspected autoantibody with underlying alloantibody, daratumumab interference in multi-transfused patients, or rare antigen deficiencies — **must be referred to a Transfusion Medicine Reference Laboratory.**
- Results interpreted by this skill are provisional pending laboratory confirmation.
- The skill cannot replace physically performing the serological tests — it interprets results you provide, but those results must come from properly controlled, QC-verified laboratory testing.
- In Saudi Arabia / CBAHI-regulated settings: all compatibility reports require sign-off by a qualified Biomedical Scientist. Use this skill to assist the reporting process, not replace it.

---

## Your Complete EEHLSS Skills Library

| Skill | File | Covers |
|-------|------|--------|
| `sysmex-xn-cbc-interpreter` | SKILL.md | Sysmex XN-Series CBC results, flags, scattergrams, blood film decisions |
| `hb-interpreter` | SKILL.md | Bio-Rad HPLC + Sebia CZE haemoglobinopathy diagnosis |
| `chemistry-hormone-interpreter` | SKILL.md (v2.0) | Chemistry + hormone panels, 12 organ systems, critical values |
| `transfusion-medicine-interpreter` | SKILL.md | Blood bank immunohaematology — all aspects of compatibility testing |

**Deploy all four** for a complete AI-assisted laboratory decision-support suite covering haematology, haemoglobinopathy, biochemistry/endocrinology, and transfusion medicine.

### Install all four skills on EVO X2:
```bash
cp -r sysmex-xn-cbc-interpreter/    /mnt/skills/user/
cp -r hb-interpreter/                /mnt/skills/user/
cp -r chemistry-hormone-interpreter/ /mnt/skills/user/
cp -r transfusion-medicine-interpreter/ /mnt/skills/user/

echo "All 4 EEHLSS skills installed:"
ls /mnt/skills/user/
```

---

## Files in This Folder

| File | Description |
|------|------------|
| `SKILL.md` | The skill itself — 1,138 lines of clinical interpretation logic. Install this into Claude. |
| `README.md` | This file — installation and usage instructions. |
| `RESEARCH_DEEP_DIVE.md` | 533-line academic research document covering current evidence base, 8 identified research gaps, and the EEHLSS implementation roadmap. Not required for clinical use — for research and development reference. |

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | April 2026 | Initial release. Full 11-phase framework. Covers all major blood group systems, DAT/autoantibody workup, crossmatch, antibody titration/HDFN, SCD/thalassaemia/obstetric/neonatal/transplant/oncology special populations, all blood components. Description field trimmed to 923 characters (within 1024-character system limit). |

---

## Contact

Developed and maintained by **Echukwuka** for **EEHLSS / MedLabAI-LIS**.
For clinical queries on complex transfusion cases, consult your Consultant Haematologist, Transfusion Medicine Physician, or National Blood Transfusion Service Reference Laboratory.

---

*EEHLSS / MedLabAI-LIS · eehlss.io · alafiaai.io*
*For use in accredited clinical laboratory practice. All results require validation by a qualified Medical Laboratory Scientist or Transfusion Medicine Physician.*
