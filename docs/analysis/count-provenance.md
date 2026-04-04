# Count Provenance — April 2026

This note maps the major recurring project numbers to their current source, counting method, and confidence level.

Confidence labels used here:
- **data-verified** — checked directly against project files in this verifier pass
- **pdf-verified** — checked directly against a cited PDF in this verifier pass
- **source-reported** — reported in project prose or assignment text, but not fully re-verified against the underlying source in this pass
- **derived/project-state** — true of the current repo state, but not necessarily a published scholarly count

---

| Number | What it refers to | Source / location | Counting method / taxonomy | Status | Notes |
|---|---|---|---|---|---|
| **1,880** | project corpus document records | `linear_a/data/corpus.json` | current project JSON record count | **data-verified** | This is the unified project corpus size, not the same thing as a published inscription count. |
| **1,534** | RILA 2025 official document count | stated in `docs/analysis/what-we-know.md` | published corpus count | **source-reported** | Not confirmed from the currently available `RILA_Supplement_2025_Index_Only.pdf`, which is only an index/table-of-contents extract. |
| **758** | extracted word forms in computational morphology pass | `linear_a/data/morphological_analysis.json` (`_metadata.total_word_forms_extracted`) | extracted forms from computational morphology workflow | **data-verified** | This is not the same denominator as Younger's full lexicon count used elsewhere. |
| **1,463** | Younger's lexicon word-form total used in project prose | stated in `docs/analysis/what-we-know.md` and related analysis docs | lexicon form count | **source-reported** | Repeated across project analysis prose, but not re-verified directly from the lexicon PDF in this pass. |
| **386** | signs in project structured data layer | `linear_a/data/signs.json` | current project sign-entry count | **data-verified** | Functional/project data inventory. |
| **389** | sign count cited in corpus audit vs Salgarella/OCD-style inventory | `docs/analysis/corpus-audit-2026-04.md` | published sign inventory count | **source-reported** | The audit doc says “Salgarella (OCD 2022): 389 signs”; this was not separately re-confirmed in the PDF pass. |
| **315** | sign types with images in project catalog | current repo state: `docs/images/signs/*.png` | image-file count in docs catalog | **data-verified** | Project display-layer count, not a scholarly inventory count. |
| **178 / 164 / 47** | simple / complex-composite / fractional signs | `references/core/Salgarella_2022_Linear_A_OCD.pdf` | **graphic-form taxonomy** | **pdf-verified** | These are graphic inventory classes, not the same as repo functional categories like syllabogram/logogram/ligature. |
| **48** | A301 occurrences and documents | `linear_a/data/signs.json` entry `A301` | sign-level occurrence/document counts | **data-verified** | Current project data says `occurrences = 48`, `documents = 48`. |
| **52** | glossary entries | `linear_a/data/glossary.json` | current glossary entry count | **data-verified** | Project glossary size. |
| **21** | LA-LB word parallels from latest deep extraction | `docs/analysis/verifier-assignment-round2.md` (Builder note) and `docs/analysis/what-we-know.md` script-language discussion | project extraction / lexicon comparison result | **source-reported** | Round 2 assignment says the deep extraction found 21 parallels; not re-derived independently in this pass. |

---

## Critical distinction: these counts come from different universes

The project currently mixes counts from at least four different universes:

1. **Project corpus record counts**  
   Example: **1,880** in `corpus.json`

2. **Published corpus / inscription counts**  
   Example: **1,534** in RILA-style prose

3. **Computational morphology extraction counts**  
   Example: **758** extracted forms in `morphological_analysis.json`

4. **Lexicon-based form counts**  
   Example: **1,463** word forms in project prose based on Younger

5. **Project functional sign inventory counts**  
   Example: **386** sign entries in `signs.json`

6. **Published graphic sign inventory counts**  
   Example: **178 / 164 / 47** in Salgarella's graphic-form taxonomy

7. **Project display-layer counts**  
   Example: **315** sign images in `docs/images/signs/`

These counts should not be treated as contradictory unless they claim to measure the same thing.

---

## Immediate usage rules

When using these numbers in analysis docs:

- Always label the denominator/source universe explicitly.
- Do **not** compare project functional sign counts directly against published graphic-form sign counts as if they were the same taxonomy.
- Do **not** compare `758` extracted forms directly against `1,463` lexicon forms without explaining the methodological difference.
- Treat `1,534` and `21` as **source-reported** until they are independently re-verified in a dedicated source pass.

---

## Short reference summary

- **Use 1,880** when talking about the current project corpus JSON.
- **Use 1,534** only when explicitly talking about the published RILA-style corpus count, and label it as source-reported unless re-verified.
- **Use 758** for current computational morphology results.
- **Use 1,463** only for Younger's lexicon-based form universe.
- **Use 386** for `signs.json`.
- **Use 178/164/47** only for Salgarella's graphic-form inventory.
- **Use 315** for the current sign-image catalog.
- **Use 48** for A301 occurrence/document counts.
- **Use 52** for the current glossary size.
- **Use 21** for the current Builder-reported LA-LB parallel count unless/until independently re-derived.
