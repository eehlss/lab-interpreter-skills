> **Research Purpose Only.** This material is a research and decision-support resource. It is not a validated or approved medical device, and its output must not be the sole basis for any clinical decision; all results require review by a qualified professional.

# Hemoglobinopathy Full-Spectrum Interpreter — SKILL.md

**Developed by:** Echukwuka  
**Version:** 1.0 | **Last Updated:** April 2026  
**Instruments Covered:** Bio-Rad VARIANT II HPLC (V2_BThal) · Sebia Capillarys 2/3 OCTA (CZE)  
**Standards:** TIF · BSH · ICSH · ACMG · WHO · ISO 15189:2022 · CBAHI

---

## What This Skill Does

This Claude AI skill interprets hemoglobin studies from two complementary platforms — the **Bio-Rad VARIANT II HPLC** and the **Sebia Capillarys capillary zone electrophoresis (CZE)** — and integrates results with CBC indices to produce a full-spectrum hemoglobinopathy assessment.

Upload a photograph or scan of either or both result printouts, provide the patient's age, sex, and CBC values, and the skill generates:

- A hemoglobin fraction breakdown with platform-specific reference ranges
- Cross-platform correlation (HPLC vs. CZE — identifying variants each platform may miss)
- CBC integration with all five standard microcytic anemia discriminant indices (Mentzer, England & Fraser, Green & King, Shine & Lal, RDWI)
- Differential diagnosis across: β-thalassemia, α-thalassemia, HbS/C/E/D variants, compound heterozygotes, iron deficiency anemia (IDA), anemia of chronic disease (ACD), and sideroblastic anemia
- Iron studies assessment and its impact on Hb fraction interpretation
- A tiered action plan covering confirmatory testing, molecular analysis, family studies, clinical referral, and instrument QC
- A plain-language brief conclusion suitable for a lab report comment

---

## What You Need Before You Start

### Required for every session
1. Image of the Bio-Rad HPLC printout **and/or** Sebia CZE electrophoretogram (clear photo or scan)
2. Patient **age** in years
3. Patient **biological sex** (Male / Female)
4. CBC indices — the following are all required for discriminant index calculation:
   - Hemoglobin (HGB) — specify g/dL or g/L
   - RBC count (×10⁶/µL)
   - HCT / PCV (% or ratio)
   - MCV (fL)
   - MCH (pg)
   - MCHC (g/dL or g/L)
   - RDW-CV or RDW-SD (%)

> If any of the above are missing, the skill will ask for them before proceeding. Discriminant indices cannot be calculated without the full RBC panel.

### Strongly recommended (for complete diagnosis)
- Serum ferritin and/or serum iron / TIBC / transferrin saturation
- Ethnicity or geographic origin of patient (affects variant pretest probability)
- Clinical context (symptoms, known diagnoses, current medications, transfusion history)
- Pregnancy status (if applicable)
- Previous Hb studies for comparison
- Reticulocyte count / RET-He (if available from Sysmex XN)
- Sickling test result

> **Unit note:** HGB in g/L must be converted to g/dL (divide by 10) to apply reference ranges. The skill will handle the conversion if you specify the units.

---

## How to Install This Skill on Your Own System

### Option A — Clone the repository and run in Claude Code (recommended)

**Step 1:** Clone this repository locally:

```bash
git clone https://github.com/eehlss/lab-interpreter-skills.git
cd lab-interpreter-skills
```

**Step 2:** Add this skill folder to Claude Code project skills:

```bash
mkdir -p .claude/skills
cp -R hb-interpreter-skill .claude/skills/
```

**Step 3:** Open Claude Code in the repository and ask, for example:

- "Interpret this Hb HPLC result"
- "Interpret this Sebia CZE pattern"
- "Is this thalassemia or iron deficiency?"

### Option B — Install for all projects on your local PC

```bash
mkdir -p ~/.claude/skills
cp -R hb-interpreter-skill ~/.claude/skills/
```

### Option C — Claude.ai (Web or Mobile App)

1. Open Claude.ai and sign in.
2. Go to Settings and then Custom Instructions.
3. Open SKILL.md from this folder.
4. Copy the full SKILL.md content into Custom Instructions.
5. Save and start a new chat.

### Option D — Claude API Integration (Developer)

**Step 1:** Read `SKILL.md` into a string in your application.

**Step 2:** Pass as system prompt with the patient's CBC data and image as user message:

```python
import anthropic, base64

with open("SKILL.md", "r") as f:
    skill = f.read()

with open("hplc_result.jpg", "rb") as img:
    image_data = base64.b64encode(img.read()).decode("utf-8")

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    system=skill,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {"type": "base64", "media_type": "image/jpeg", "data": image_data}
            },
            {
                "type": "text",
                "text": """Interpret this Hb HPLC result.
Patient: 38-year-old female.
CBC: HGB 9.8 g/dL, RBC 4.32, HCT 0.28, MCV 64.9, MCH 22.6, MCHC 34.8 g/dL, RDW 23.6%.
Clinical context: Al-Ahsa Health Cluster, Saudi Arabia. Routine investigation."""
            }
        ]
    }]
)
print(response.content[0].text)
```

---

### Option E — n8n Workflow Automation (local setup)

**Step 1:** Create an HTTP Request node → `https://api.anthropic.com/v1/messages`

**Step 2:** Build JSON payload:
- `system` = contents of `SKILL.md`
- `messages[0].content` = array with base64 image + CBC text
- Pass patient context as text node from preceding workflow step

**Step 3:** Wire output to Email/Slack node for delivery to clinical inbox.

**Step 4:** Trigger via webhook or folder watch on incoming Hb result scans.

---

## How to Use the Skill — Step by Step

### Basic Usage (Claude.ai)

1. Open a new Claude conversation.
2. Upload your HPLC printout and/or CZE electrophoretogram image.
3. Type your request including patient data:

```
Interpret this Hb HPLC result.
Patient: 38-year-old female.
CBC: HGB 9.8 g/dL, RBC 4.32, HCT 0.28, MCV 64.9, MCH 22.6, MCHC 34.8 g/dL, RDW 23.6%.
No ferritin available. Location: Saudi Arabia.
```

```
Interpret both these results (HPLC and CZE from same patient).
Patient: 25-year-old male.
CBC: HGB 11.2 g/dL, RBC 5.8, HCT 0.35, MCV 61, MCH 19, MCHC 31, RDW 16%.
Ferritin: 45 µg/L. Ethnicity: West African.
```

```
Is this thalassemia or iron deficiency? Patient: 22-year-old female, 16 weeks pregnant.
CBC: Hb 98 g/L, RBC 4.1, MCV 72, MCH 24, MCHC 330, RDW 18%.
Ferritin 8 µg/L.
```

4. Claude applies the full 8-section framework and returns a structured report.

---

### Output Modes

Add these phrases to control report length:

| Phrase | Output |
|--------|--------|
| *(nothing — default)* | Full 8-section report |
| `"quick summary"` | Brief conclusion + action plan only |
| `"just Hb fractions"` | Fraction table + chromatogram description only |
| `"iron status only"` | Section 5 (iron assessment) only |
| `"QC check"` | Instrument QC assessment only |
| `"discriminant indices only"` | CBC section with index calculations only |

---

### Trigger Phrases

The skill activates on:
- "Interpret my Hb electrophoresis" / "Interpret this HPLC"
- "Is this thalassemia or iron deficiency?"
- "Assess my hemoglobin fractions"
- "What does this Bio-Rad result show?"
- "Interpret this Sebia result"
- "Analyze this hemoglobinopathy workup"
- Any upload of a Bio-Rad VARIANT II or Sebia Capillarys printout image

---

## Understanding the Report — Section Guide

| Section | Contents |
|---------|----------|
| **1. Hb Fraction Summary** | All fractions from HPLC and/or CZE vs. method-specific reference ranges |
| **2. CBC Integration** | Full RBC parameter table + 5 discriminant indices calculated + consensus |
| **3. Chromatogram/Electrophoretogram** | Peak-by-peak description of HPLC chromatogram and CZE electrophoretogram |
| **4. Differential Diagnosis** | Primary diagnosis, confidence level, alternative diagnoses, conditions excluded |
| **5. Iron Studies Assessment** | Interpretation of ferritin/iron/TIBC/transferrin saturation and impact on Hb study validity |
| **6. Final Integrated Diagnosis** | Definitive/probable diagnosis with genotype/phenotype confidence |
| **7. Action Plan** | Tiered: immediate → short-term → confirmatory → referral → QC actions |
| **8. Brief Conclusion** | 3–4 sentence summary for lab report comment or clinician communication |

---

## Conditions Covered

### Thalassemia Syndromes
- β-thalassemia trait (carrier), intermedia, major (Cooley's anemia)
- α-thalassemia: silent carrier, trait (1–2 gene deletion), Hb H disease (3-gene deletion), Hb Bart's hydrops
- δβ-thalassemia, Hb Lepore
- Hereditary Persistence of Fetal Hemoglobin (HPFH)

### Structural Hemoglobin Variants
- HbS (sickle cell trait and disease), HbSS, HbSC, HbSβ-thalassemia
- HbC (trait, CC disease), HbE (trait, EE disease, HbEβ-thalassemia)
- HbD-Punjab, Hb G-Philadelphia, Hb J family
- HbO-Arab, Hb Lepore, HbH
- Unknown peaks — cross-platform RT and zone analysis for tentative identification

### Microcytic Anemia Differential
- Iron Deficiency Anemia (IDA)
- Anemia of Chronic Disease / Inflammation (ACD)
- Sideroblastic Anemia (congenital and acquired)
- Combined IDA + β-thalassemia trait (important — IDA suppresses HbA2)

---

## Limitations

**This skill is a clinical decision support tool.**

- All outputs must be reviewed and validated by a qualified Medical Laboratory Scientist before use in patient management.
- HPLC and CZE provide **presumptive identification** of Hb variants. Molecular confirmation (α-globin and/or β-globin gene sequencing) is required for definitive diagnosis, especially before genetic counselling.
- HbA2 on HPLC can be **falsely lowered by iron deficiency** — never exclude β-thalassemia trait based on a borderline HbA2 without first excluding IDA.
- In Saudi Arabia and CBAHI-regulated settings: **a definitive diagnosis of hemoglobinopathy must be confirmed by molecular testing** before issuing a carrier report for premarital or prenatal counselling purposes.
- CZE HbA2 reference ranges are **different from HPLC** — the skill applies the correct range per method (CZE: 1.6–3.1%; HPLC: 2.0–3.3%).
- HbE co-elutes with HbA2 on Bio-Rad Variant II HPLC — apparent HbA2 >10% should trigger CZE correlation.
- This skill does not cover HbA1c interpretation or HbA1c interference by variants.

---

## Sharing With Colleagues

Share the entire `hb-interpreter-skill/` folder containing:
- `SKILL.md` — the interpretation framework
- `README.md` — this file

Recommended colleague workflow:
1. Clone `https://github.com/eehlss/lab-interpreter-skills.git`.
2. From the repo root, copy the skill into `.claude/skills/`.
3. Open Claude Code and run interpretation prompts with patient context.

**Minimum access:** Claude.ai Free account (Option A above). For regular clinical use, Claude.ai Pro is recommended.

---

## Frequently Asked Questions

**Q: I only have the HPLC result — can I still use this skill?**  
Yes. The skill works with HPLC alone, CZE alone, or both together. If only one platform is available, the skill will note which confirmatory steps require the other method.

**Q: My patient's ferritin is unavailable — will I still get a diagnosis?**  
Yes, but the diagnosis will be flagged as provisional in the iron-dependent aspects. The skill will recommend ferritin as a priority action and will explain which conclusions may change once iron status is known.

**Q: The image of my HPLC printout is partially cut off — will it still work?**  
The skill can work from partial images, but accuracy improves with full visibility of the numerical table and chromatogram. If the HbA2 calibrated value and chromatogram peak area table are visible, that is the minimum for a useful interpretation.

**Q: The patient had a recent blood transfusion — does that affect the result?**  
Yes — significantly. Post-transfusion samples will show donor HbA mixing with patient Hb, masking variant fractions and falsely elevating HbA. State transfusion history in your message and the skill will flag this as a major pre-analytical confound.

**Q: Can this skill be used for neonatal screening results?**  
Partially. HbF reference ranges, Hb Bart's thresholds, and the significance of trace HbA in neonates differ from adult interpretation. The skill will note when neonatal-specific interpretation limits apply and recommend specialist review.

**Q: What is the difference between this skill and the Sysmex XN CBC interpreter skill?**  
The Sysmex XN skill interprets automated CBC results (blood count, differential, reticulocytes, flags, scattergrams). This skill interprets hemoglobin fractionation studies (HPLC and electrophoresis). They are complementary — the CBC indices from the Sysmex XN skill can be directly pasted into this skill for a complete integrated hemoglobinopathy workup.

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | April 2026 | Initial release. Covers Bio-Rad V2_BThal HPLC + Sebia Capillarys 2/3 CZE. Full thalassemia/variant spectrum + IDA/ACD/sideroblastic differential. 5 discriminant indices. CBAHI/SFDA context included. |

---

## Contact

Developed and maintained by **Echukwuka**.  
Clinical queries → consult a Consultant Haematologist or Clinical Geneticist for complex or critical cases.

---

*For use in accredited clinical laboratory practice. Results require validation by a qualified Medical Laboratory Scientist.*
