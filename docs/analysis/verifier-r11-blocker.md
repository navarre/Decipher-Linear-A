# Verifier R11 — Resolved

## Task
Read GORILA Volume 5 sign plates from `references/gorila/vol5/` and review the sign-plate material.

## Status
**Resolved — 2026-04-05.**

## What changed
The `references/gorila/vol5/` directory is now present in the repo with 524 scanned page images (`EtCret_21-5_1985_001.jpg` through `EtCret_21-5_1985_524.jpg`). The Volume 5 sign index — printed pages 142–325, file pages 194–377 — has been fully transcribed.

## Deliverables produced

- `linear_a/data/gorila_sign_index_rows.json` — 3,936 attestation rows covering 207 distinct sign identifiers, spanning every sign from AB 01 through the fraction catalog A 701–A 713 and the punctuation signs on printed page 325. Each row carries `sign_id`, `sign_name_LB`, `file_page`, `printed_page`, `row_index`, `context_numeric` (with the target sign marked `*like-this*`), `target_sign_position`, `rubrique` (A–J per GORILA's section codes), `ref` (document citation), and `notes`.
- `linear_a/data/gorila_concordances_full.json` — 468 entries linking GORILA inscription ids to museum inventory numbers, dating, and scribal hands (Volume 5 concordance tables).
- `linear_a/data/corpus.json` — enriched with `gorila_ref`, `museum_inventory`, `gorila_dating`, `gorila_scribe`, `gorila_notes` on 632 of 1,880 corpus rows (440 concordance entries applied, expanded to 632 sub-faces).
- `linear_a/data/corpus_enrichment_audit.json` — full audit of matched/unmatched concordance entries, with notes on catalog-difference cases (`HT 42+59` merge, `KH 48`, `KH 89`, `LA Zb 1`, `HT Wb 1/2`, `PH Wc 36`, etc.).
- `linear_a/data/signs.json` — enriched with `gorila_index_row_indices` pointing each sign to its attestation rows; 347 of 386 signs linked (180 direct, 4 via A→AB remap, 2 via sub-letter parent expansion, 161 via composite-catalog cross-reference).
- `linear_a/data/signs_to_gorila_index.json` — sidecar with full sign-to-index linkage and match-method breakdown.
- `docs/sign-concordance.html` — public-facing browser for the index.

## Cross-check against `gorila_sign_variants.json`
Validation comparison found no coverage gaps. All sign identifiers present in the variants file are covered in the index rows. Naming differences are documented in the row-file metadata (`A 400`–`A 418` in variants ↔ `A 400VAS`–`A 418VAS` in rows; `A 28b` / `A 100/102` / `A 120b` / `A 131c` in variants ↔ `AB 28b` / `AB 100/102` / `AB 120b` / `AB 131c` in rows). Fraction signs A 701–A 713 are present in rows but absent from variants — the variants file does not catalogue fractions.

## Historical note
The previous version of this file reported `references/gorila/vol5: No such file or directory` and classified R11 as a source-availability blocker. That report was accurate at the time it was written. A subsequent sync landed the vol5 images; the extraction was then completed in a single overnight pass with periodic checkpoints. The original blocker framing is preserved in the project history via git.

## Downstream work unblocked
- Step 1 (Corpus data layer enrichment) — done, 632 corpus rows now carry `gorila_ref` + `museum_inventory`
- Step 2 (Sign catalog enrichment) — done, 347 of 386 signs linked to their GORILA index rows
- Step 3 (Glossary footnotes) — done, 47 of 52 lexical entries now carry per-document GORILA citations
- Step 4 (Sign *301 doc audit) — done, counts corrected from 48 → 72 documents; 14 distinct *301-bearing words catalogued with attestations
- Step 5 (Libation formula doc audit) — done, stable-core vs variant split documented
- Step 6 (About / Methodology) — done, GORILA integration language added
- Step 7 (Sign Concordance public page) — done, drafted at `docs/sign-concordance.html`

## Verification path for reviewers
```python
import json
d = json.load(open('linear_a/data/gorila_sign_index_rows.json'))
assert d['metadata']['completion_status'] == 'complete'
assert len(d['rows']) == 3936
# spot-check A 301
a301 = [r for r in d['rows'] if r['sign_id'] == 'A 301']
assert len(a301) == 35
```
