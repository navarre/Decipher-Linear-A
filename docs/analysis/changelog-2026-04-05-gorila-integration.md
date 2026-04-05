# Changelog — GORILA Integration (2026-04-05)

The full seven-step GORILA Volume 5 integration plan landed today, plus two verifier passes and a data audit. Nothing public-facing has shipped yet — everything below is in the data layer and analysis docs. The `sign-concordance.html` page is new and ready to ship on the next site deploy.

## Summary

| Area | Before | After |
|---|---|---|
| GORILA Volume 5 sign index | Unextracted | 3,936 rows, 207 sign IDs, pages 142–325 complete |
| corpus.json gorila_ref coverage | 0 / 1,880 rows | 632 / 1,880 rows (34%) |
| signs.json linkage to sign index | 0 / 386 | 347 / 386 (90%) |
| glossary.json GORILA footnotes | 0 / 52 entries | 47 / 52 entries (90%) |
| Public sign-concordance page | Did not exist | Drafted at `docs/sign-concordance.html` |
| Sign *301 document count | "48 documents" | **72 documents** (48 logogram + 24 syllabogram) |
| Words containing *301 | "11+" / "14" | **31 distinct words** |
| Libation formula tier counts | ~21/11/4/1 (unreproducible) | 18/4/0/1 (audited against corpus) |
| KN Zf 13 scepter | Tokenized but mis-identified as empty | Confirmed: 19 signs, A301 at position 6 |

## What's new

### Data layer

- **`linear_a/data/gorila_sign_index_rows.json`** — 3,936 attestation rows extracted from GORILA Volume 5, pages 142–325 (file pages 194–377). Covers 207 unique sign identifiers: the full AB series, the A series (A 301–A 371), VAS ideograms (A 400–A 418), fraction catalog (A 701–A 713 including 709² / 709³ / 709⁴ / 709⁶), and punctuation signs. Each row carries `sign_id`, `sign_name_LB`, `file_page`, `printed_page`, `row_index`, `context_numeric` (target marked `*like-this*`), `target_sign_position`, `rubrique` (A–J per GORILA's section codes), `ref`, and `notes`. Cross-checked against `gorila_sign_variants.json` with no coverage gaps.
- **`linear_a/data/gorila_concordances_full.json`** — 468 concordance entries linking inscription ids to museum inventory numbers, dating, and scribal hands (Volume 5 concordance tables, pages 82–113).
- **`linear_a/data/corpus.json`** — enriched in place. Added `gorila_ref`, `museum_inventory`, `gorila_dating`, `gorila_scribe`, `gorila_notes` on 632 of 1,880 corpus rows. Matching used sub-face expansion (one concordance entry can hit multiple corpus rows for recto/verso faces), yielding 440 of 468 concordance entries applied.
- **`linear_a/data/corpus_enrichment_audit.json`** — audit sidecar. 28 concordance entries are unmatched, all for documented reasons (merged documents, catalog-decision differences, or absent from the Younger-derived corpus list). Full list inside.
- **`linear_a/data/signs.json`** — enriched in place. Every entry now carries `gorila_index_row_indices`, `gorila_index_row_count`, and `gorila_index_match_method`. 347 of 386 signs linked (90%).
- **`linear_a/data/signs_to_gorila_index.json`** — reviewable linkage sidecar with method breakdown. 180 direct matches, 4 via A→AB remap, 2 via sub-letter parent expansion, 161 via composite-catalog cross-reference. 39 unlinked signs fall into five documented categories — none are errors.
- **`linear_a/data/glossary.json`** — enriched with `gorila_refs` per entry. 47 of 52 lexical entries now carry per-document GORILA citations; 5 are unenriched because their only attestations are in documents without a matched concordance entry.
- **`linear_a/data/sign_301_cross_check.json`** — per-document comparison of corpus vs. GORILA A 301 index. 72 corpus docs ↔ 35 index rows. 6 of 7 apparent mismatches resolve via sub-face normalization. The one genuine gap: `NO Za 1` (Nerokourou) — cited by GORILA, absent from corpus. Flag for ingestion.
- **`linear_a/data/gorila_sign_index.xlsx`** — six-sheet Excel workbook for reviewers who prefer spreadsheets over JSON: README, All Rows (with auto-filter), Sign Summary (rubrique breakdown per sign), Rubrique Legend, A 301 Detail, Libation Formula.

### Analysis docs

- **`docs/analysis/sign-301.md`** — appended a full audit log. Key corrections: 48→72 documents; 14→31 distinct *301-bearing words; 32 nodules broken down as 29 HT + 3 KH; scepter confirmed in data layer with A 301 at position 6; three "missing" words (`zu-*301-se-de-qi`, `sa-*301-ri`, `te-*301`) confirmed present under the `A301` tokenization. 7-words-plus-variants rollup added explicitly.
- **`docs/analysis/libation-formula.md`** — appended a stable-core vs. variant section. Stable core: `a-ta-i-*301-wa-ja` ×10, `ja-sa-sa-ra-me` ×7, `si-ru-te` ×7, `i-pi-na-ma` ×6, `u-na-ka-na-si` ×4. Eleven variants each with single/double attestation. Tier-structure figures reconciled: the original 21/11/4/1 is not reproducible from current corpus; audited counts are 18/4/0/1. Two new findings: i-da-ma-te is geographically restricted to Arkhanes and never co-occurs with Word 1 in running text; ja-sa-sa-ra-me independently appears 4× without Word 1.
- **`docs/analysis/verifier-gorila-signs.md`** — new R12 verifier deliverable. Documents the sign-catalog linkage method and results, categorizes all 39 unlinked signs, gives reviewers a five-point spot-check protocol.
- **`docs/analysis/verifier-r11-blocker.md`** — rewritten from "Blocker Note" to "Resolved" with full deliverables list, historical note preserving the original blocker framing, and a reviewer verification snippet.

### Public site

- **`docs/sign-concordance.html`** — new page. Client-side browser for the sign index: filter by sign, filter by rubrique, free-text search, pagination at 100 rows. Target-sign position highlighted in the context column. Intro text explicitly frames the page as "sign attestation, not lexeme" and states Linear A has no agreed word count. Added to the research-mode sidebar nav as "Sign Concordance."
- **`docs/about.html`** — GORILA bullet in the Data Sources section rewritten with concrete numbers (3,936 rows, 207 signs, 468 concordance entries, pages 142–325) and linked to the new concordance page. New "Primary-source grounding" bullet added to the Methodology section.
- **`docs/nav.js`** — "Sign Concordance" link added to the research-mode sidebar between "Sign Catalog" and "Sites & Map".

## What did not land

- **Visual verification of the sign-concordance page** against a running site. The page is written and expects `../linear_a/data/gorila_sign_index_rows.json` relative to its location; a browser check would confirm the fetch path is correct.
- **NO Za 1 (Nerokourou) ingestion.** Flagged as the one genuine A 301 coverage gap. Needs a manual add to corpus.json.
- **KN Zf 13 scepter duplicate word fix.** The scepter's 19-sign word is listed twice in its `words[]` array. Minor data-layer bug.
- **Composite resolution cleanup.** Three composite signs (A 506, A 684, A 718) didn't match via the linker's regex. Hand audit would likely close them.
- **Tier-count source tracking.** The original ~21/11/4/1 figures in libation-formula.md came from somewhere; finding and citing their source would let us decide whether to replace or supplement.
- **Git commit.** `.git/index.lock` has been present since an earlier interrupted session. Clear the lock and commit this work when ready.

## Numbers you can cite in public writing

These are the audited, defensible figures as of 2026-04-05:

- GORILA Volume 5 sign index: **3,936 attestation rows** covering **207 sign identifiers** across printed pages 142–325.
- Project corpus: **1,880 documents**, of which **632 carry GORILA volume/page citations** and museum inventory numbers.
- Sign *301: **72 documents** in the corpus (48 logogram + 24 syllabogram). **31 distinct words** contain *301. The canonical libation opening `a-ta-i-*301-wa-ja` is attested **10 times across 7 sanctuary sites** (Ioukhtas, Kophinas, Palaikastro, Syme, Troullos, Tylissos, Vrysinas).
- Libation formula stable core: **5 words** attested ≥4× across multiple sites.
- Sign catalog linkage: **90% of the project's 386 signs** are now linked to their GORILA index attestation rows, with five documented categories of exceptions.
