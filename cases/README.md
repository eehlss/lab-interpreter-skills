> **Research Purpose Only — synthetic, de-identified data. Not for clinical use.**

# Synthetic case library (skeleton)

This folder will hold **synthetic** test cases for the skill(s) in this repository. It currently contains only this README; **no cases have been generated yet.**

## Location rule

- Cases live in `cases/` at the **repository root**, one subfolder per skill, named by the skill's frontmatter `name`.
- Cases are **not** stored inside skill folders (no `sample-cases/` inside a skill folder), so a skill folder can be copied into `.claude/skills/` without shipping test data.

```
cases/
  README.md                          # this file
  sysmex-xn-cbc-interpreter/         # <- skill `name` (frontmatter), prefix CBC
    CBC-001-<slug>/
  hb-interpreter/                    # prefix HB
  chemistry-hormone-interpreter/     # prefix CH
  transfusion-medicine-interpreter/  # prefix IH (skill folder: immunohaematology-interpreter-skill/)
```

## Index

| Skill (frontmatter `name`) | Skill folder | Case prefix | Cases |
|---|---|---|---|
| `sysmex-xn-cbc-interpreter` | `sysmex-xn-cbc-interpreter-skill/` | `CBC` | none yet |
| `hb-interpreter` | `hb-interpreter-skill/` | `HB` | none yet |
| `chemistry-hormone-interpreter` | `chemistry-hormone-interpreter-skill/` | `CH` | none yet |
| `transfusion-medicine-interpreter` | `immunohaematology-interpreter-skill/` | `IH` | none yet |

## Rules for every case

- Synthetic and de-identified only: invented values, `SYN-` identifiers, fictitious dates (year 2099), no real sample/QC IDs, patient data, institution names, instrument serials or reagent/QC lot numbers.
- Every case file carries the `Research Purpose Only` notice.
- Expected outputs are captured skill output for review and are **not clinically validated**.
- Case IDs are `<PREFIX>-<NNN>` (three digits, never reused); folders are `<ID>-<kebab-slug>`.

## Images for vendor printouts (Sysmex, Bio-Rad, Sebia)

- Image-driven skills may use **generic synthetic images** in place of vendor printouts: drawn or rendered from scratch, with invented values, labelled as a layout approximation, watermarked `SYNTHETIC - RESEARCH PURPOSE ONLY`, and with no EXIF/metadata. Do not use photos or scans of real printouts.
- Real printouts are planned for **later validation** by the repository owner. They are kept strictly separate (next section) and are not part of this public case library.

## `validation-real/` (private, never committed here)

- Real printouts used for validation belong in a separate area named `validation-real/`, kept **outside this public repository** (for example in a private repository or local-only storage).
- **Real printouts must not be committed to a public repository without de-identification and documented consent.** A sample ID, date, instrument serial or lab header can be enough to identify a person or a laboratory.
- `validation-real/` is listed in this repository's `.gitignore` as a safety net only; it does not stop a forced add, and it does not remove anything already committed.
