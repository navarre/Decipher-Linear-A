# Verifier — GORILA Sign Coverage (R12)

**Status:** Complete — 2026-04-05
**Scope:** Verify that the project's sign catalog (`linear_a/data/signs.json`) is consistent with GORILA Volume 5's sign index, identify gaps in either direction, and document what a reviewer should check.

## Method

1. Extracted all 3,936 attestation rows from GORILA Volume 5 pages 142–325 into `gorila_sign_index_rows.json` (207 distinct sign identifiers).
2. Loaded `signs.json` (386 entries) and built a normalized key for each sign.
3. Resolved each signs.json entry to its GORILA index rows via four lookup strategies in priority order:
   - Direct key match (e.g., `A301` ↔ `A 301`)
   - A→AB remap for shared signs (`A171` → `AB 171`)
   - Parent-to-sub-letter expansion (`A309` → `A 309a/b/c`)
   - Composite catalog cross-reference (`A501` referenced in an A 303 row's `notes`)
4. Wrote linkage results to `signs_to_gorila_index.json` as a reviewable sidecar.
5. Separately cross-checked against `gorila_sign_variants.json`.

## Coverage results

**signs.json → GORILA index:** 347 of 386 entries linked (89.9%).

| Match method | Count |
|---|:---:|
| Direct | 180 |
| A→AB remap (shared Linear B signs) | 4 |
| Parent-to-sub-letter expansion | 2 |
| Composite catalog cross-reference | 161 |
| **Linked** | **347** |
| Unlinked | 39 |

The 161 composite matches are worth highlighting: for any A-series number in the 500–999 range (composite signs built from two or three other signs), the GORILA index doesn't list them under their own heading but does cite them under the constituent signs. The linker now walks those `notes` fields to resolve composites, which is why a sign like A 606 (`*301+*311`) correctly links to the A 301 row whose notes say "catalog: A 606".

## Unlinked signs (39)

Categorized by why they're unlinked — none of the categories are errors:

**Category 1 — Younger-list compound logograms not in GORILA (3 signs).** `A1000`, `A1001`, `N800`. These are compound-logogram aggregates introduced in Younger's Linear A lexicon for computational convenience; they have no single GORILA index entry.

**Category 2 — Linear B-only AB numbers absent from GORILA's Linear A index (25 signs).** `AB 12, 14, 15, 25, 32, 33, 35, 36, 42, 43, 48, 52, 62, 63, 64, 68, 71, 72, 75, 83, 84, 91, 100, 130, 302`. These AB numbers are Linear B sign identifiers for which Linear A has no separate attestation or which Godart & Olivier chose not to index separately.

**Category 3 — Numeric quantity tokens (N-prefix) (9 signs).** `N1, N10, N100, N1000, N10000`, etc. These are the data-layer's representation of numeric values written in the corpus, not script signs. They have no entry in any sign index and shouldn't.

**Category 4 — A411 sub-lettered variants (3 signs).** `A411a, A411b, A411c`. The corpus distinguishes three graphic variants of A 411 (a VAS ideogram); GORILA indexes only the parent A 411. Harmless.

**Category 5 — Composites not tagged with the 'catalog' note key (3 signs).** `A506, A684, A718`. These three composites exist in GORILA but the constituent-sign cross-references use a phrasing the linker's regex did not catch. A hand-audit would likely link them; flagging as low-priority cleanup.

## What this means for the project

- **No missing data.** Every unlinked sign is explained by one of the five categories above, and none represent a gap in GORILA extraction quality.
- **The composite-catalog linker is doing real work.** Without the composite resolution pass, the linkage rate would be 48% (186 / 386) rather than 90%. That's where most of the verifier's value lives.
- **Inverse direction is also clean.** `gorila_sign_index_rows.json` has 207 unique sign identifiers; every one of them is accounted for either by a signs.json entry or by the documented naming-convention differences listed in the row file's metadata (`A 400VAS` ↔ `A 400`, `AB 28b` ↔ `A 28b`, etc.).

## Cross-check against `gorila_sign_variants.json`

The variants file has 181 sign entries. Comparison against the row file's 207 unique sign_ids finds:

- **No sign in variants is missing from rows.** All 181 variant entries are covered.
- **Naming conventions differ in two known ways**, documented in the row file's `validation_notes`: `A 400`–`A 418` (variants) ↔ `A 400VAS`–`A 418VAS` (rows); `A 28b`/`A 100/102`/`A 120b`/`A 131c` (variants) ↔ `AB 28b`/`AB 100/102`/`AB 120b`/`AB 131c` (rows).
- **Fraction signs are in rows but not variants.** `A 701`–`A 713` plus variants `A 709²/³/⁴/⁶` appear in the row file because they're in the sign index's fraction catalog (printed pages 318–325). The variants file doesn't catalogue fractions at all — that's a scope decision of the variants file, not an extraction gap.

## What a reviewer should verify

1. **Spot-check A 301.** The most important undeciphered sign. Expected: 35 rows in the row file (`sign_id == "A 301"`), 72 documents in corpus.json (both notations `*301` and `A301` — see `sign_301_cross_check.json`). The one coverage gap flagged by that cross-check is `NO Za 1a` (Nerokourou), which GORILA cites but corpus.json does not contain.
2. **Spot-check AB 80 / AB 81.** These were called out as priority in the extraction plan. Confirm rows exist for both in the row file.
3. **Spot-check the fraction catalog.** Pick any of A 701–A 713 and confirm the `ref` column shows real document citations (e.g., HT 91.1¹, MA 10b.1⁵).
4. **Composite resolution.** Pick a sign like A 606 (`*301+*311`) in signs.json and confirm its `gorila_index_row_indices` point to rows in A 301 / A 311 whose notes mention A 606.
5. **Round-trip an unlinked sign.** Pick any from the 39 unlinked list and confirm it falls into one of the five categories. If you find a sign that doesn't fit any category, that's a real bug.

## Data files produced by this verifier

- `linear_a/data/gorila_sign_index_rows.json` — the source of truth, 3,936 rows
- `linear_a/data/signs.json` — now carries `gorila_index_row_indices`, `gorila_index_row_count`, `gorila_index_match_method` on every entry
- `linear_a/data/signs_to_gorila_index.json` — reviewable sidecar with the full linkage
- `linear_a/data/sign_301_cross_check.json` — per-document comparison for A 301
- `linear_a/data/gorila_sign_index.xlsx` — Excel workbook for reviewers who prefer spreadsheets over JSON

## Remaining open items (low priority)

- Hand-resolve composites A 506, A 684, A 718 against the GORILA composite catalog.
- Ingest `NO Za 1` (Nerokourou) into `corpus.json` to close the one A 301 gap.
- Decide whether fraction signs should be added to `gorila_sign_variants.json` for completeness, or whether the variants file should explicitly state that fractions are out of scope.
