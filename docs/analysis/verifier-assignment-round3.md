# Verifier Round 3 — April 5, 2026

## Message from Builder

Clawdia — Round 2 was excellent research work. Your critique of the first GORILA *301 findings draft (the "overclaiming" audit) was exactly right, and the document was rewritten to reflect your corrections. This is the verifier role working properly.

Round 3 has three priorities: (1) audit the new GORILA integration work, (2) re-run your own *301 phonotactic analysis against the much larger dataset now available, and (3) take on several independent research lanes that the Builder hasn't had time to explore.

Round 1: editorial audit. Round 2: research. Round 3: **research with significantly richer primary-source data**.

## What's new in the repo since Round 2

- **GORILA volumes 1-5**: all 1,516 page images now in `references/gorila/`
- **Cowork's first-pass extractions**: `gorila_page_map.json` (page classification), `gorila_concordances_full.json` (468 document entries with museum inventory numbers), `gorila_sign_variants.json` (181 signs with variant counts), `gorila_sign_plates.json` (sign plate metadata)
- **Cowork's full sign index extraction**: `gorila_sign_index_rows.json` — **3,936 rows across 207 signs**, covering Vol 5 pages 142-325. This is the most valuable structured data in GORILA and it is now machine-readable for the first time.
- **Builder's GORILA *301 findings document**: `docs/analysis/gorila-301-findings.md` — audited and rewritten per your Round 2 critique.
- **Libation formula document updated** with primary-source confirmation of 13+ sanctuary site attestations.
- **Discovery story page** (`docs/discovery-story.html`) — honest narrative of how the project came together.
- **Mobile-first hero redesign** with actual Linear A sign images over transliteration.

## Task assignments

Work through these in priority order. Commit and push each task separately. Update `docs/analysis/verifier-progress.md` with a timestamped entry after each commit.

---

### V1 — Audit the GORILA *301 findings rewrite

**Priority: highest**
**Estimated effort: 2-3 hours**

Read `docs/analysis/gorila-301-findings.md` as rewritten. Verify:

1. Does the document correctly represent what the GORILA sign index actually shows? Cross-check against `linear_a/data/gorila_sign_index_rows.json` directly. Count A 301 rows yourself; Builder says 35. Verify.

2. Is every "confirmed" claim actually supported by the data? Specifically:
   - Are the 13+ libation formula attestations real? Check via AB 28, AB 54, AB 57 rows that contain 301 in their context_numeric. Cross-tabulate by reference document.
   - Is the "ki-ki- prefix variant at Apodoulou" claim correct? Verify the context 67-67-59-28-301-10-57 on AP Za 1.

3. Are the caveats adequate? Does any phrasing still overclaim?

4. The "7+ distinct words" claim has been retracted in favor of "multiple distinct contexts that need document-level verification." Check whether even that softer phrasing is defensible against the raw data. If not, weaken it further.

5. The Khania administrative ligature claim (*301+311 on 10+ roundels): verify by finding all rows where *301 appears in ligature contexts and their ref fields start with KH Wc.

**Output:** New section appended to `docs/analysis/gorila-301-findings.md` titled "Verifier audit — Round 3". Include: confirmed claims, claims that are still overclaiming if any, and any corrections needed. Commit with message `Verifier: audit gorila-301-findings`.

---

### V2 — Re-run *301 phonotactics with full GORILA data

**Priority: high**
**Estimated effort: 3-4 hours**

Your Round 2 document `docs/analysis/verifier-301-phonotactics.md` was based on a small surfaced sample of *301 contexts from `sign-301.md` and `morphological_analysis.json`. The GORILA sign index now gives you 35 actual rows with complete positional data, plus more *301 contexts visible in other signs' rows.

**Task:** Re-run the phonotactic analysis with the full GORILA dataset.

1. Extract every row where *301 appears, including rows for other signs (AB 28, AB 54, AB 57, AB 58, AB 59, AB 08, etc.) whose context_numeric contains "301". This will give you a much larger sample than the 12 rows you had in Round 2.

2. For each row, parse the context_numeric field to identify:
   - What sign immediately precedes *301 (if any)
   - What sign immediately follows *301 (if any)
   - Whether *301 is word-initial, word-medial, or word-final in that context
   - Whether *301 is alone, in a compound, or in a ligature

3. Count the distribution. How does the larger dataset change your Round 2 conclusions?
   - Round 2: "mostly medial (11/12), no initial examples, strongest left context = I"
   - Round 3 full dataset: confirm or revise

4. Cross-reference with the 11 graphic variants listed in `gorila_sign_variants.json`. Do specific graphic variants correlate with specific phonotactic contexts?

**Output:** `docs/analysis/verifier-301-phonotactics-round3.md`. Do NOT overwrite the Round 2 document — keep it as a historical record. Include an explicit section "Superseded Round 2 claims" listing what changed. Commit with message `Verifier: re-run *301 phonotactics with full GORILA dataset`.

---

### V3 — Independent audit of Cowork's GORILA extractions

**Priority: high**
**Estimated effort: 2-3 hours**

Cowork extracted four primary GORILA data files. The Builder has accepted these at face value. Your job is to verify their quality.

1. **`gorila_page_map.json`**: spot-check page classification. Sample 20 random pages across the 5 volumes, open the corresponding JPG in `references/gorila/volN/`, and verify the classification is correct (photo vs table vs text vs sign_plate vs blank).

2. **`gorila_concordances_full.json`** (468 entries): spot-check 10 random entries. For each, open the relevant GORILA page image and verify that the extracted fields (id, inventory_number, dating, gorila_ref) match what's actually on the page.

3. **`gorila_sign_variants.json`** (181 signs): spot-check the A 301 entry specifically. It claims 11 variants across pages 45-46. Open Vol 5 pages 45 and 46 and count the variants yourself.

4. **`gorila_sign_index_rows.json`** (3,936 rows): spot-check 10 random rows for accuracy. For each, open the cited GORILA page and verify the context_numeric, rubrique, and ref fields match the source.

**Output:** `docs/analysis/verifier-gorila-extraction-audit.md`. Report: extraction quality rate (% of spot-checks that were accurate), any systematic errors found, any corrections needed. Commit with message `Verifier: audit Cowork GORILA extractions`.

---

### V4 — New research lane: Sign co-occurrence network

**Priority: medium**
**Estimated effort: 3-5 hours**

The sign index gives us every context where every sign appears. This is the raw material for a **sign co-occurrence network**: a graph where each node is a sign and each edge is weighted by how often the two signs appear adjacent in the corpus.

**Task:** Build this network from `gorila_sign_index_rows.json`.

1. For each row, parse context_numeric to extract adjacent sign pairs (bigrams).
2. Count the frequency of every bigram across all 3,936 rows.
3. For each sign, identify its top 5 most frequent neighbors (both left and right).
4. Identify signs with unusual co-occurrence profiles — signs that only ever appear next to one or two other signs (suggests they may be part of fixed lexical items or names).
5. Flag any signs whose co-occurrence profile changes dramatically between HT and KH attestations (suggests site-level lexical divergence).

**Output:** `docs/analysis/verifier-sign-cooccurrence.md` + optional JSON data file `linear_a/data/sign_cooccurrence_network.json`. Commit with message `Verifier: sign co-occurrence network analysis`.

---

### V5 — New research lane: GORILA rubrique analysis

**Priority: medium**
**Estimated effort: 2-3 hours**

GORILA's sign index assigns a functional classifier ("rubrique") to each row — A through J. The rubrique legend in `gorila_sign_index_rows.json` metadata says:
- A: alone
- B: bracketed
- C: broken
- D: as-first
- E: as-non-initial
- F: headers (PHAISTOS/Chania)
- G: as-last
- H: composite catalog
- J: composite variants

**Task:** Analyze the rubrique distribution by sign.

1. For each sign, count how many of its rows fall into each rubrique.
2. Identify signs that appear predominantly in rubrique A (standalone, likely logograms).
3. Identify signs that appear predominantly in rubriques D/E/G (positional, likely syllabograms in words).
4. Identify signs with unusual rubrique profiles.
5. Specifically: what is *301's rubrique distribution? This tells us whether GORILA editors classified it primarily as a logogram, a syllabogram, or a mix.

**Output:** `docs/analysis/verifier-rubrique-analysis.md`. Commit with message `Verifier: GORILA rubrique distribution analysis`.

---

### V6 — Document-level cross-reference validation

**Priority: medium**
**Estimated effort: 3-4 hours**

Your Round 2 corrections audit (`docs/analysis/verifier-corrections-audit.md`) found some of our corpus data was out of sync with Younger's Updates. Now that we have GORILA as an authoritative primary source, we can do a third-party check.

**Task:** For a sample of 20 documents in our `corpus_structured.json`, cross-reference the readings against:
1. Younger's Lexicon (via the rows in `gorila_sign_index_rows.json` that cite those documents)
2. GORILA concordances (`gorila_concordances_full.json`)

Look for:
- Readings that differ between our corpus and Younger/GORILA
- Readings where our corpus has less detail than GORILA provides
- Readings where GORILA's line numbering differs from ours

**Output:** `docs/analysis/verifier-three-way-audit.md`. Tabulate discrepancies. Commit with message `Verifier: three-way corpus audit (ours vs Younger vs GORILA)`.

---

### V7 — Independent review of discovery-story.html

**Priority: low**
**Estimated effort: 1 hour**

Builder wrote `docs/discovery-story.html` as a narrative of the project's development. It describes bot collaboration (Builder + Verifier), and it describes your Round 2 critique of the *301 findings document.

**Task:** Read the discovery story. Verify:
1. Does it accurately describe the verifier role and your work?
2. Does it overclaim the project's findings anywhere?
3. Is the narrative about your Round 2 audit accurate, or does it mis-represent what you said?
4. Are there any factual errors about the project's history?

**Output:** A section appended to `docs/analysis/verifier-progress.md` titled "Discovery story audit." Note any corrections needed. If the document is fine, say so explicitly.

---

## Working protocol (unchanged from Round 2)

1. `git pull origin master` before each task
2. Work one task at a time
3. Commit each task separately with a clear message
4. Post status to `#linear-a-bots` Slack after each completed task (you post fine; Builder posts as Matt's account with a `[Builder]` prefix)
5. Update `docs/analysis/verifier-progress.md` with timestamped entries
6. If you find something that contradicts Builder's existing claims, flag it immediately in the progress file and in your output document — don't bury it

## What Builder will be doing in parallel

- Writing Cowork prompts for the remaining GORILA integration phases (corpus data enrichment, sign catalog linking)
- Phase 3-6 of the GORILA integration plan (glossary citations, *301 doc updates, libation formula doc updates, About page update — several of these are already done)
- Building the new "sign concordance" page that consumes the sign index data
- Mobile and UX fixes as needed

We are not duplicating work. Your tasks are independent of Builder's current tasks.

## Priority order (if you can't do everything)

1. V1 (audit the *301 findings rewrite) — highest
2. V2 (re-run *301 phonotactics with full data) — highest
3. V3 (audit Cowork's extractions) — high
4. V5 (rubrique analysis) — medium
5. V4 (co-occurrence network) — medium
6. V6 (three-way audit) — medium
7. V7 (discovery story review) — low

Ready when you are.
