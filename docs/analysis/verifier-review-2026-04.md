# Verifier Review — April 2026

**Verifier:** Clawdia / Bot B  
**Status:** Draft completed after repo/data verification pass  
**Scope covered in this pass:** project analysis docs + structured data in `linear_a/data/`  
**Not fully completed in this pass:** systematic source-PDF re-verification of every published claim

---

## 1. Confirmed claims

These claims are supported by the project data as checked directly in this pass.

### Corpus / data-layer claims confirmed
- `linear_a/data/corpus.json` contains **1,880 document records**.
- `linear_a/data/signs.json` contains **386 sign entries**.
- `linear_a/data/signs.json` entry `A301` shows **48 occurrences on 48 documents**.
- `linear_a/data/morphological_analysis.json` metadata reports:
  - **758** extracted word forms
  - **210** suffixed words
  - **27.7%** suffixed
  - **8** suffixes in the suffix inventory
- `morphological_analysis.json` also explicitly reports:
  - **27** stacking patterns
  - **34** reduplicated forms
  - **15** identified compounds
  - **51** paradigm stems

### High-confidence methodological confirmations
- The repo is using **multiple taxonomic layers** for signs. The data-layer categories are functional (`syllabogram`, `logogram`, `ligature`, `fraction`, etc.), while some prose claims cite a graphic inventory scheme (`simple`, `complex/composite`, `fractional`). These are not interchangeable counts.
- The sign *301 discussion is grounded in real structured data: the project does indeed have a strong corpus basis for saying that *301 is frequent and important.
- There is already substantial analysis output in `docs/analysis/`; this is not an empty repo or a hallucinated workstream.

### Directly confirmed sign-category breakdown from `signs.json`
- **164** syllabogram
- **117** logogram
- **64** ligature
- **16** other
- **14** fraction
- **6** compound_logogram
- **5** numeral

---

## 2. Corrections needed

These are places where the current analysis set is internally inconsistent, overstated, or mixing incompatible measures.

### C1. Mixed corpus-size baselines are not labeled clearly enough
Different docs refer to different totals without explaining the shift in denominator:
- `corpus.json` = **1,880 document records**
- RILA-style prose claim = **1,534 documents**
- `morphological_analysis.json` = **758 extracted forms**
- several prose docs refer to **1,463 word forms**

These may all be legitimate in their own contexts, but the current docs often read as if they are talking about the same universe of evidence. They are not.

**Required fix:** every quantitative section should explicitly label its denominator and source, e.g.:
- "1,880 project corpus document records"
- "1,534 inscriptions in RILA 2025"
- "758 extracted forms in computational morphology pass"
- "1,463 lexicon forms in Younger's lexicon counting scheme"

### C2. Sign inventory counts are being compared across incompatible taxonomies
The repo data supports:
- 164 syllabogram / 117 logogram / 64 ligature / 14 fraction / etc.

The prose also cites:
- 178 simple / 164 complex-composite / 47 fractional

Those are not direct confirmations of each other. One is a **functional categorization in the repo**, the other appears to be a **graphic inventory scheme from published scholarship**.

**Required fix:** stop presenting them as if they were directly commensurable. They should be explicitly framed as different classification systems.

### C3. Morphology counts differ across documents
`morphological_analysis.json` summary gives suffix counts:
- -JA 39
- -TE 36
- -NA 33
- -RA 33
- -SE 22
- -NE 21
- -RO 16
- -ME 10

But prose docs sometimes state noticeably different frequencies (for example 42/39/38/34 etc. in one place, and much larger counts in another where a different total is implied).

**Required fix:** each morphology doc must declare whether it is counting:
- extracted forms from the computational JSON,
- lexicon forms,
- token occurrences,
- or something else.

Right now the reader cannot tell whether the discrepancy is a bug, a dataset difference, or a methodological choice.

### C4. The project currently overstates some claims as verified when they remain source-dependent
Examples:
- exact published sign counts attributed to Salgarella
- exact published RILA figures
- strong statements about Steele's percentage
- confident restatements of specific publication claims about chronology and object interpretation

These may prove correct, but in this pass they were **not yet all re-verified against the PDFs**.

**Required fix:** mark such claims as one of:
- "verified against project data"
- "reported from published source; PDF reconfirmation pending"
- "interpretive hypothesis"

### C5. Some prose conclusions outrun the demonstrated evidence
Examples include language-family statements written too definitively, especially where the evidence presented is typological rather than lexical.

The strongest demonstrated result from the repo is that the language is **compatible with a suffixing/agglutinative analysis**. That is not the same as having securely established deeper genealogical conclusions.

---

## 3. Overclaiming

These are not necessarily false, but they are too strong relative to the evidence demonstrated in the repo pass.

### O1. "Unknown agglutinative language isolate" is stronger than the evidence currently warrants
"Unknown agglutinative language" is supportable as a working description. "Isolate" goes further and implies comparative exclusion that has not been fully demonstrated here.

**Better wording:**
> "An as-yet unidentified language with strong suffixing/agglutinative tendencies remains the best working description on current evidence."

### O2. "Greek" and "Semitic" rejection is sometimes phrased more strongly than the actual analysis supports
The anti-Greek and anti-Semitic arguments may well be directionally right, but some formulations sound like full disproof when they are really cumulative typological objections.

**Better wording:**
> "The current morphological profile is difficult to reconcile with Greek or Semitic as full-language explanations."

### O3. Hurrian comparisons are useful, but some prose moves too quickly from typological resemblance to explanatory weight
The repo analysis supports saying Hurrian is a **typological comparison point**. It does not by itself secure a genetic or historical relationship.

### O4. Substrate-word arguments are currently suggestive, not closed
The `substrate-words.md` file contains stimulating ideas, but several chains are still inferential. These should be labeled as **proposals under evaluation**, not as settled survivals.

### O5. Sign *301 phonological claims remain hypothetical
The data strongly shows *301 is important and structurally unusual. It does **not** yet prove a specific phoneme class.

**Better wording:**
> "A non-Linear-B-equivalent value remains plausible; finer phonological assignment is still hypothetical."

---

## 4. New findings from this verifier pass

### N1. The biggest immediate issue is not lack of work — it is lack of denominator discipline
The project already contains real quantitative work. The main verifier problem is that the writeups mix:
- document counts
- lexicon form counts
- extracted-form counts
- sign-function counts
- published graphic-inventory counts

without always labeling which universe is being used.

This makes good work look less reliable than it actually is.

### N2. The morphology JSON is a stronger anchor than several prose summaries
For claims about:
- suffix inventory
- total extracted forms
- percent suffixed
- stacking patterns
- reduplication count

`linear_a/data/morphological_analysis.json` should be treated as the current computational reference point unless and until a revised analysis replaces it.

### N3. The A301 work is one of the project’s strongest quantitative lanes
Unlike some of the broader language-history conclusions, the *301 lane already has clear data support:
- structured sign entry
- occurrence count
- document count
- cross-document analytical attention

That means *301 is a good candidate for a tighter, evidence-first paper or benchmark writeup.

### N4. The current analysis set contains multiple excellent "working hypotheses" that should be reframed as staged confidence levels
The project would improve immediately if each claim were labeled:
- **Data-verified**
- **Source-reported**
- **Interpretive**
- **Speculative**

Right now many interpretive claims are written in the voice of verification.

---

## 5. New hypothesis

### H1. A large share of the project’s apparent disagreement is methodological, not substantive
**Hypothesis:** several current contradictions in the analysis corpus arise because different documents are measuring different things rather than because one of them is simply wrong.

Examples:
- 758 vs 1,463 word-form counts
- 386 functional sign entries vs 178/164/47 graphic inventory counts
- differing suffix-frequency tables

**Testable prediction:** if the project adds a one-page "count provenance" table that maps every major number to its source and counting method, a large fraction of the current internal friction will disappear without changing the underlying analysis.

This is not a hypothesis about Minoan itself; it is a hypothesis about the project’s current research architecture. It is highly testable and worth fixing immediately.

---

## 6. Open questions

These remain unresolved after this verifier pass.

1. **Published-source verification backlog**  
   Which headline numbers have been rechecked directly against the cited PDFs, and which are still inherited from prior notes?

2. **Word-form denominator problem**  
   What exactly explains the gap between the 758 extracted forms and the 1,463 lexicon forms repeatedly cited in prose?

3. **Sign-taxonomy bridge**  
   Can the project create a crosswalk table between functional sign categories in `signs.json` and published graphic inventory categories?

4. **A301 role split**  
   Can the project quantify more rigorously how often *301 behaves like a logogram versus a syllabogram by context and document type?

5. **Confidence labeling**  
   Which current conclusions should be downgraded from asserted findings to working hypotheses pending PDF-level verification?

---

## Recommended next actions

1. Add a short `count-provenance.md` documenting all major project numbers and their denominators.
2. Revise `what-we-know.md` so every number is explicitly tagged by source universe.
3. Normalize morphology reporting to one declared counting method.
4. Create a sign-taxonomy crosswalk note: functional vs graphic classes.
5. Keep developing the *301 lane, because it is one of the strongest data-supported parts of the project.
6. Only after the above, do a targeted PDF verification pass on the most public-facing claims.

---

## Bottom line

There is real work here. The repo already contains substantial quantitative and interpretive analysis. The immediate problem is **not** that the analysis is empty or fake; it is that the project currently mixes counting systems and confidence levels too loosely. Tightening that will make the strongest parts of the research stand up much better.
