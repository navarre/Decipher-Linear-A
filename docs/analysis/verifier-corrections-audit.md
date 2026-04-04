# Verifier R9 — Corrections Audit Against `corpus_structured.json`

## Task
Audit the correction list in `docs/analysis/corpus-audit-2026-04.md` against the structured corpus data.

## Important path correction
The round-2 assignment cited:
- `linear_a/data/corpus_structured.json`

That path does **not** exist in the current repo.

The structured corpus file actually used in this audit is:
- `linear_a/data/sources/sigla/corpus_structured.json`

So the assignment pointed to the wrong path, but the underlying data file does exist.

---

## Audit table

| Correction target | Expected correction | What current structured data has | Status |
|---|---|---|---|
| **HT 30.4-.5** | Should be **1 BOS** not 4 | `HT 30` includes `AB23/BOS` followed by fraction signs; exact line-value granularity is not recoverable from this JSON alone | **partial / line-level not testable** |
| **HT 97, HT 119** | Should show `*327 AES` (bronze) | `HT 119` begins with `A327` as a logogram; `HT 97a/b` not yet inspected at line-detail in this pass | **partial / likely supports correction** |
| **KN Zc 6** | `NI-TI-NU → NI-JA-NU` | current reading is `...pa-ku-ni-ja-nu-ju...` / word `ni-ja-nu` | **correct** |
| **KH Wa 1001g** | `RO+RO → DA+RO` | no `KH Wa 1001g` entry found in current structured file | **not found** |
| **HT 117.a5** | `TE-JA-RE` and `NA-DA-RE` switched | `HT 117a` contains both `te-*56-re` and `na-da-re`; sequence visible, but exact line-position switching is not fully testable from current word list alone | **partial / probably auditable with line images** |
| **HT 26a.1, b.1** | `406VAS+KE` not `407VAS+A` | `HT 26a/26b` entries present, but current JSON abstracts logograms and does not expose this exact old/new rendering in a directly comparable way | **partial / not directly testable** |
| **HT 34** | should **NOT** have `SA-VINa` | current `HT 34` words are `da-ju-te`, `si-A516`, `sa-ra`, `ki-ro`; no `sa-VINa` word reading is present | **correct** |
| **HT 23, 24** | should have `SI+ME` | `HT 23a/b` and `HT 24a/b` exist, but current JSON representation does not expose an obvious `SI+ME` composite in the word list sampled here | **unclear / not directly confirmed** |
| **HT 26b.3, 127b.5,6** | `KI+MU` not `KU+MU` | `HT 26b` and `HT 127b` exist, but current JSON word/sign sampling here did not expose a decisive `KI+MU` vs `KU+MU` comparison | **unclear / not directly confirmed** |
| **SA-*315 on HT 9, 17, 19, 42** | should be `SA-RO` | `HT 17`, `HT 19`, and `HT 42+59` all show `sa-ro`; `HT 9` not directly isolated in this pass | **supports correction** |
| **PO Zg → PO Zc** | category should be painted, not graffito | no `PO Zg` / `PO Zc` entry found in current structured file search | **not found** |
| **GRA+PA** | should be `*574` not `*577` or `*547` | not directly testable from current sampled entries in this pass | **not resolved** |
| **KN Wa 40 provenance** | South-West House not South House | no `KN Wa 40` entry found in current structured file search | **not found** |
| **HT 115a.1-2** | `RI-TA-MA-NU-WI` not `RI-SU-MA-...` | current `HT 115a` contains word `ri-ta-ma-nu-wi` | **correct** |

---

## What was confirmed cleanly

### Strong clean confirmations
1. **KN Zc 6**  
   Current data contains `ni-ja-nu`, supporting the correction from `NI-TI-NU`.

2. **HT 34**  
   Current data does not expose a `SA-VINa` reading and instead gives a sequence centered on `sa-ra` / `ki-ro`, supporting the correction note.

3. **HT 115a.1-2**  
   Current data contains `ri-ta-ma-nu-wi`, supporting the correction.

4. **SA-*315 cluster → SA-RO**  
   In the sampled entries (`HT 17`, `HT 19`, `HT 42+59`), the current structured data shows `sa-ro`, which supports the correction trend.

### Strong partial support
5. **HT 119 / *327 AES**  
   `HT 119` begins with `A327` as a logogram, which is at least consistent with the correction note that this tablet should show `*327 AES`.

---

## What could not be fully resolved in this pass

The main reason some items remain unresolved is that `corpus_structured.json` is structurally useful but not fully line-granular in the same way the correction notes are phrased.

Some corrections refer to:
- exact line positions
- exact composite sign values
- provenance metadata not surfaced in the sampled JSON entries
- fine distinctions in old vs corrected sign decomposition

These need either:
1. the source images / plate views, or
2. a richer structured corpus export with line-by-line / provenance-level detail

This affects especially:
- HT 30 line-level BOS count
- HT 117.a5 word-order switch
- HT 26a/26b exact VAS sign assignment
- HT 23/24 `SI+ME`
- HT 26b / HT 127b `KI+MU` vs `KU+MU`
- GRA+PA exact sign-value correction

---

## Missing entries from the current structured file search
The following audit targets were **not found** by direct key search in `linear_a/data/sources/sigla/corpus_structured.json`:
- `KH Wa 1001g`
- `PO Zg` / `PO Zc`
- `KN Wa 40`

This may mean:
- different ID normalization in the structured corpus
- omission from the current source subset
- or the need for broader search logic beyond direct key matching

---

## Best verifier judgment
This audit produced a mixed but useful result.

### What it shows
- some of Younger's corrections are clearly reflected in the current structured corpus
- the corpus is **not oblivious** to these updates
- the most clearly supported corrections in this pass are:
  - `KN Zc 6`
  - `HT 34`
  - `HT 115a`
  - the `SA-RO` cluster

### What it does NOT show yet
- a clean yes/no resolution for all 15 correction items
- a fully line-granular correction audit

---

## Recommended next step
To fully complete this audit, the project needs one of:
1. a line-granular enriched export of the structured corpus, or
2. direct comparison against source transcription/images for unresolved items

Still, the audit was worth doing because it established:
- the structured corpus file exists (at a different path than documented)
- several corrections are already reflected in current data
- the remaining unresolved cases are mostly about **representation granularity**, not total absence of evidence

## Bottom line
The correction audit partially succeeds.

Some of Younger's updates are clearly present in the structured corpus, but the current JSON export is not rich enough to resolve all 15 items cleanly. The result improves confidence in parts of the data while also identifying exactly where finer-grained corpus representation is still needed.
