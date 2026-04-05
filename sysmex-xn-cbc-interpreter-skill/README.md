# Sysmex XN-Series CBC Interpreter & Troubleshooter — SKILL.md

**Developed by:** Echukwuka | EEHLSS / MedLabAI-LIS  
**Version:** 1.0 | **Last Updated:** April 2026  
**Compatible Instruments:** Sysmex XN-1000 · XN-3100 · XN-9000 (all XN-Series modules)  
**Standards Referenced:** ICSH 2014 · CLSI H20-A2 · BSH 2009 · ISO 15189:2022

---

## What This Skill Does

This is a Claude AI skill that turns a photograph or scan of a Sysmex XN-Series CBC printout into a structured clinical assessment. You upload the result image, provide the patient's age and sex, and Claude applies the full 8-phase framework to produce:

- A parameter-by-parameter review with age/sex-corrected reference ranges
- Interpretation of all instrument flags (WBC, RBC, PLT, and scattergram)
- A scattergram pattern analysis (WDF, WNR, RET, RBC histogram, PLT histogram)
- A blood film decision — mandatory, recommended, or not required — with specific morphological targets
- An instrument QC and calibration assessment
- A tiered action plan (immediate, same-day, further investigations, clinician notification)
- A plain-language brief conclusion suitable for a lab report comment or verbal handover

It is designed for use by Medical Laboratory Scientists, Haematology Technologists, and Laboratory Managers working with Sysmex XN-Series instruments in clinical, hospital, or reference laboratory settings.

---

## What You Need Before You Start

### Required for every session
1. A clear photograph or scan of the Sysmex XN printout (the paper result sheet showing parameters, scattergrams, and histograms)
2. The patient's **age in years**
3. The patient's **biological sex** (Male / Female)

### Helpful but optional
- Clinical context (e.g., "known sickle cell", "post-chemotherapy", "HIV-positive", "routine antenatal screen", "malaria-endemic region")
- Previous CBC result for the same patient (for trend comparison)
- QC status for that working day ("QC passed", "QC not done", "Level 2 out of range")
- Time elapsed between blood collection and analysis

> If age and sex are not provided, the skill will ask for them before proceeding. Reference ranges cannot be applied without these two inputs.

---

## How to Install This Skill on Your Own System

This skill is designed for use with **Claude.ai** (the web or mobile app) via the Skills/Custom Instructions system, or with any Claude API-based system that supports skill/prompt injection.

### Option A — Claude.ai (Web or Mobile App)

This is the simplest route for individual users and colleagues who use Claude.ai directly.

**Step 1:** Open Claude.ai in your browser or the Claude mobile app and sign in.

**Step 2:** Go to **Settings → Custom Instructions** (or the equivalent "System Prompt" or "Memories" panel depending on your interface version).

**Step 3:** Open the `SKILL.md` file from this folder in any text editor (Notepad, VS Code, TextEdit, etc.).

**Step 4:** Copy the **entire contents** of `SKILL.md` and paste it into the Custom Instructions field.

**Step 5:** Save. Claude will now apply this skill automatically whenever you upload a Sysmex XN result image and ask for an interpretation.

> Note: If your Custom Instructions field has a character limit, paste from `## PHASE 2` onwards (skipping the YAML front-matter header) — this preserves all the clinical logic. The header is only needed for systems that read metadata from the YAML block.

---

### Option B — Claude.ai Skills Folder (EEHLSS / MedLabAI-LIS Local Setup)

If you are running a local or server-based Claude environment with a `/mnt/skills/` directory (as used in the EEHLSS EVO X2 setup):

**Step 1:** Copy the entire `sysmex-xn-cbc-interpreter/` folder to your skills directory:

```bash
cp -r sysmex-xn-cbc-interpreter/ /mnt/skills/user/sysmex-xn-cbc-interpreter/
```

**Step 2:** Verify the file is in place:

```bash
ls /mnt/skills/user/sysmex-xn-cbc-interpreter/
# Should return: SKILL.md  README.md
```

**Step 3:** Claude will now auto-detect this skill from the `<available_skills>` list and trigger it when you upload a Sysmex XN printout image and use any of the trigger phrases listed below.

No restart or reloading is required — skills are read at the start of each conversation.

---

### Option C — Claude API Integration (Developers / LIS Developers)

If you are integrating this skill into a custom application (e.g., embedding CBC interpretation into MedLabAI-LIS or a laboratory workflow tool via the Claude API):

**Step 1:** Read the full contents of `SKILL.md` into a string in your application code.

**Step 2:** Pass the skill content as part of the system prompt in your API call:

```python
import anthropic

with open("SKILL.md", "r") as f:
    skill_content = f.read()

system_prompt = f"""
You are a clinical hematology assistant for a medical laboratory.
Apply the following skill framework for every CBC result analysis request.

{skill_content}
"""

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    system=system_prompt,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": "<base64_encoded_image>"
                    }
                },
                {
                    "type": "text",
                    "text": "Please interpret this CBC result. Patient: 35-year-old female. Clinical context: routine antenatal screening. QC passed this morning."
                }
            ]
        }
    ]
)
print(message.content[0].text)
```

**Step 3:** For FHIR R4 integration, the output `Section 7: Action Plan` maps naturally to a `DiagnosticReport` resource. The brief conclusion maps to `DiagnosticReport.conclusion`. Parameter values map to `Observation` resources.

---

### Option D — n8n Workflow Automation (EEHLSS EVO X2 / Local Inference)

If you are running automated CBC interpretation via n8n on your EVO X2:

**Step 1:** Create an n8n **HTTP Request** node pointing to your Claude API endpoint (`https://api.anthropic.com/v1/messages`).

**Step 2:** In the node's body, build a JSON payload where:
- `system` = contents of `SKILL.md` (read from file or stored as n8n credential/variable)
- `messages[0].content` = array containing the image (base64) and the patient context text

**Step 3:** Wire the output to an n8n **Email** or **Slack** node to deliver the report to your work inbox or team channel.

**Step 4:** Use a **Webhook** or **File Watch** trigger to fire the workflow automatically when a new CBC result image lands in a watched folder.

---

## How to Use the Skill — Step by Step

### Basic Usage (Claude.ai Web or Mobile)

1. Open a new conversation with Claude.
2. Upload your Sysmex XN CBC printout image (photo from your phone works well — ensure the parameters, scattergrams, and histograms are all visible and in focus).
3. Type your request. Examples:

```
Interpret this CBC result. Patient is a 28-year-old female. 
Routine screening. QC passed this morning.
```

```
Assess this Sysmex result for a 6-year-old male child. 
Clinical concern: pallor and fatigue. No QC information available.
```

```
Is a blood film needed for this result? Patient: 52-year-old male, known CLL, post-chemotherapy.
```

```
Check my Sysmex flags and tell me if my instrument needs QC attention.
Patient: 45-year-old female. QC Level 2 was borderline this morning.
```

4. Claude will apply the 8-phase framework and return a structured report.

---

### Output Modes — Controlling Report Length

You can control how much detail you receive by adding a mode instruction to your request:

| What you type | What you get |
|---------------|-------------|
| *(nothing extra — default)* | Full 8-section report |
| `"quick summary"` | Brief conclusion + action plan only |
| `"just flags"` | Flag analysis + blood film decision only |
| `"is my instrument working?"` | QC and calibration assessment only |
| `"interpret the scattergrams"` | Scattergram section only |

**Example:**
```
Quick summary only. Patient: 67-year-old male. Known CML on imatinib.
```

---

### Trigger Phrases

The skill activates automatically when you use any of these phrases alongside an uploaded image:

- "Interpret this CBC result"
- "Is a blood film needed for this result?"
- "Check my Sysmex flags"
- "Assess my hematology result"
- "Troubleshoot my analyzer output"
- "What does this CBC mean for a [age]-year-old [male/female]?"
- "Run a CBC assessment"
- "Analyze this Sysmex printout"

---

## Understanding the Output — Section Guide

The full report has 8 sections:

| Section | What It Contains |
|---------|----------------|
| **1. Parameter Summary Table** | All CBC values with reference range, status icon (✅⬆️⬇️⚠️🚨), and brief clinical note |
| **2. Flag Analysis** | Each instrument flag decoded — what triggered it, what it means, urgency level |
| **3. Scattergram Interpretation** | WDF, WNR, RET, RBC histogram, and PLT histogram pattern descriptions |
| **4. Clinical Interpretation** | Primary finding, top 3 differential diagnoses with supporting parameters |
| **5. Instrument QC Assessment** | Daily QC status, reagent concerns, calibration currency, preanalytical issues |
| **6. Blood Film Decision** | Mandatory / Recommended / Not Required + morphological targets + urgency |
| **7. Action Plan** | Tiered checklist: Immediate → Same-day → Further investigations → Clinician notification → Instrument actions |
| **8. Brief Conclusion** | 2–3 sentence plain-language summary for lab report comment or clinical handover |

---

## Clinical Scope — What This Skill Covers

### Analyte Coverage
All parameters reported by the Sysmex XN-Series in whole blood mode:
- Full CBC: WBC, RBC, HGB, HCT, MCV, MCH, MCHC, RDW-SD, RDW-CV, PLT, MPV, PDW, P-LCR, PCT
- 5-part WBC differential: NEUT, LYMPH, MONO, EO, BASO (% and absolute)
- Extended parameters: NRBC, IG (immature granulocytes)
- Reticulocyte panel: RET%, IRF, RET-He, LFR, MFR, HFR
- Platelet extended: PLT-F (fluorescent), IPF (if available)

### Flag Library
All XN-Series flags are covered including:
- WBC flags: Blasts?, Abnormal Lympho/Blasts?, Atypical Lympho?, Left Shift?, IG Present, NRBC Present, WBC Abn Scattergram, Diff WNR/WDF, iRBC?, Low SFL clusters
- RBC flags: Anisocytosis, Microcytosis, Macrocytosis, Hypochromia, Fragments?, MCHC >37, Turbidity/HGB interference
- PLT flags: Thrombocytopenia, Giant PLT?, PLT Clumps?, Abn PLT Distribution

### Reference Range Populations
- Adults (18–65 years), male and female
- Paediatric tiers: Neonates, Infants, Children (1–6y, 6–12y), Adolescents
- Special populations: Pregnancy, West African/African benign ethnic neutropenia, post-chemotherapy

### QC Framework
Applies Westgard multi-rules to QC interpretation (1-2s warning, 1-3s reject, 2-2s reject, R-4s reject, 4-1s reject, 10x trend). Identifies reagent interference (lipemia, cold agglutinin, EDTA pseudothrombocytopenia, hemolysis, delayed samples) and calibration trigger conditions per CLSI EP9 allowable error specifications.

---

## Important Limitations

**This skill is a clinical decision support tool, not a diagnostic replacement.**

- All outputs must be reviewed and validated by a qualified Medical Laboratory Scientist (MLS) or equivalent registered professional before being used in patient care decisions.
- The skill does not have access to the patient's clinical history, medication records, previous results, or electronic health record unless you explicitly provide that context in your message.
- Reference ranges used are general consensus ranges from WHO, ICSH, and BSH guidelines. Your laboratory's locally validated reference ranges should take precedence where they differ.
- In malaria-endemic regions (including Nigeria, other West/Central African countries, and parts of the Middle East), the `iRBC?` flag should always be treated as a malaria screen trigger — thick and thin blood films are mandatory regardless of clinical probability.
- This skill does not replace mandatory quality control procedures. If QC has not been performed, run QC before reporting patient results regardless of what the skill assessment suggests.
- The skill is aligned with ISO 15189:2022 principles for medical laboratory quality but does not constitute an accreditation document or audit record.

---

## Sharing With Colleagues

### What to share
Share the entire `sysmex-xn-cbc-interpreter/` folder, which contains:
- `SKILL.md` — the skill itself (the clinical brain)
- `README.md` — this file (instructions)

### How colleagues can install it
Direct colleagues to **Option A** above (Claude.ai Custom Instructions) as the easiest route — it requires no technical setup, just a Claude.ai account and copy-paste.

For laboratory networks or shared systems, **Option B** (skills folder) or **Option C** (API integration) are appropriate.

### Minimum Claude access required
- A **Claude.ai Free** account is sufficient for occasional use (with message limits)
- **Claude.ai Pro** is recommended for regular clinical use — higher message limits and priority access
- **Claude API** access is required for Option C (developer integration) and Option D (n8n automation)

### Attribution
If you adapt or extend this skill for your own laboratory, please retain the attribution line at the bottom of `SKILL.md`:

> *EEHLSS / MedLabAI-LIS | Skill maintained by Echukwuka | Aligned to ICSH 2014, CLSI H20-A2, BSH 2009, ISO 15189:2022*

---

## Frequently Asked Questions

**Q: Can I use this with instruments other than the Sysmex XN-Series?**  
A: The flag names, scattergram descriptions, and channel logic are specific to XN-Series instruments (XN-1000, XN-3100, XN-9000, XN-10, XN-20). Parameters like IG, NRBC, IRF, RET-He, and IPF may not be present on older Sysmex models (e.g., XE-2100, XT-1800) or non-Sysmex platforms. A separate skill would be needed for those instruments.

**Q: The image I have is low resolution or partially cut off — will it still work?**  
A: Claude can read partially visible printouts, but accuracy improves significantly when the full parameter list, at least two scattergrams (WDF and WNR), and the RBC/PLT histograms are visible. If only the numeric parameters are visible (no scattergrams), the skill will still complete Sections 1, 2, 4, 5, 7, and 8 but will note that scattergram interpretation (Section 3) is unavailable.

**Q: Can I upload a screenshot from the Sysmex IPU software instead of a paper printout?**  
A: Yes. Digital screenshots from the Sysmex IPU screen are ideal and often provide better image quality than photographs of paper printouts.

**Q: What if my laboratory uses different reference ranges?**  
A: State your laboratory's reference ranges in your message when uploading the result (e.g., "Our lab uses HGB normal range 11.5–16.5 for adult females"). The skill will use your stated ranges instead of the built-in consensus ranges.

**Q: Can this help with body fluid CBC analysis?**  
A: The current version (1.0) covers whole blood mode only. Body fluid mode (peritoneal, pleural, synovial fluid analysis) is not included in this version.

**Q: What languages is this available in?**  
A: The skill is written in English. Claude itself can respond in other languages — if you write your request in French, Arabic, Yoruba, Igbo, or another language, Claude will respond in that language while applying the English skill logic internally.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | April 2026 | Initial release. Covers whole blood mode, all XN-Series parameters, full flag library, QC framework, blood film decision engine, 8-section output format. |

---

## Contact & Feedback

Developed and maintained by **Echukwuka** for **EEHLSS / MedLabAI-LIS**.  
Feedback, flag additions, or reference range corrections can be submitted to the EEHLSS development team.

For clinical queries about specific patient results, this tool provides decision support only — consult a Consultant Haematologist or senior MLS for complex or critical cases.

---

*EEHLSS / MedLabAI-LIS · eehlss.io · alafiaai.io*  
*For use in accredited clinical laboratory practice. Results must be validated by a qualified Medical Laboratory Scientist.*
