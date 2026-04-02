# Extraction proof: Haghia Triada pilot (`HT 24a`)

## Target

I chose a **single-document pilot inside the Haghia Triada subset**: `HT 24a`.

Why this slice:
- It is small enough to verify carefully by hand.
- It still exposes multiple site layers at once: a location page, a document page, per-sign pages, per-sequence pages, crop images, and SVG coordinates.
- That makes it a good proof that the old site can be **converted into structured corpus data**, not merely screen-scraped for browsing.

Relevant source pages in the imported snapshot:
- `inbox/lineara website/location/Haghia Triada/index.html`
- `inbox/lineara website/document/HT 24a/index.html`
- `inbox/lineara website/document/HT 24a/index-1.html` … `index-20.html`
- `inbox/lineara website/document/HT 24a/index-word-0.html` … `index-word-2.html`

## What was parsed

### 1. Location-level context
From `location/Haghia Triada/index.html`:
- Site label: `Haghia Triada`
- Reported document count at that site: `372`

This matters because it shows the `HT 24a` extraction is not an isolated curiosity; it sits inside a larger, enumerable site subset.

### 2. Document-level metadata
From `document/HT 24a/index.html` I reliably extracted:
- document code: `HT 24a`
- kind: `Tablet`
- location: `Haghia Triada`
- period: `LM IB`
- dimensions: `5.9 × 7.9 × 0.9 cm`
- external corpus link
- drawing image path
- reported totals: `20 signs / 3 words`

### 3. Sign-occurrence layer
From the main document page I extracted **20 occurrence records** with:
- occurrence number (`#1` … `#20`)
- site-provided role label (`Syllabogram`, `Logogram`, `Fraction`, `Erasure (Unknown?)`)
- sign code when present (examples: `AB81`, `AB56`, `A546`, `A707`)
- display reading when present (examples: `ku`, `ri`, `ja`, `A546`)
- exact SVG bounding box on the tablet image
- per-occurrence crop image path
- provenance back to source HTML pages

This is the strongest extraction proof in the set: the old site is already encoding **object-level attestation rows** and their positions on an image.

### 4. Sequence / word layer
From `index-word-0.html` to `index-word-2.html` I extracted **3 sequence records**:
- Sequence 1: `ku-*56-ri-ja` (`AB81-AB56-AB53-AB57`)
- Sequence 2: `pa-sa-ri-ja` (`AB03-AB31-AB53-AB57`)
- Sequence 3: `ru-i-ko` (`AB26-AB28-AB70`)

For each sequence I also extracted the selected-word SVG rectangles and matched them back to occurrence rectangles on `index.html` by exact coordinate equality.

Matched occurrence IDs:
- Sequence 1 → occurrences `[1, 2, 3, 4]`
- Sequence 2 → occurrences `[11, 12, 13, 14]`
- Sequence 3 → occurrences `[16, 18, 19]`

This cross-page coordinate match is important because it proves the site has enough internal structure to reconstruct links between:
- document
- sign occurrence
- sequence/word
- image region

## Fields that were reliably extracted

Mapped to the schema draft concepts where possible.

### Document
Reliable:
- `document_code`
- `kind`
- `location`
- `period`
- `dimensions_cm`
- `corpus_url`
- `drawing_image`
- `reported_sign_count`
- `reported_word_count`
- `source_page`

Why these matter:
- They support faceted browse and filtering.
- They give the stable top-level corpus unit for search and AI retrieval.
- They preserve archaeological context instead of flattening everything into raw sign strings.

### SignOccurrence
Reliable:
- `occurrence_number`
- `role`
- `sign_code` when present
- `display_reading` when present
- `bbox_on_document_image`
- `source_occurrence_page`
- `source_crop_image`

Why these matter:
- This is the bridge between inscription content and visual evidence.
- It enables sign-frequency work, image-grounded review, and future annotation layers.
- It supports a accountable data model rather than a vague AI-only representation.

### Sequence
Reliable:
- `sequence_number_within_document`
- `normalized_pattern`
- `display_reading`
- `reported_sign_count`
- `selected_word_bboxes`
- derived `matched_occurrence_numbers_by_bbox`
- `source_page`

Why these matter:
- Sequences are exactly the kind of recurring unit that make semantic search, pattern search, and hypothesis testing useful.
- They are the cleanest bridge from legacy browse pages to modern corpus querying.

## Ambiguities and caution points

I did **not** treat the following as certain beyond what the site explicitly shows:

1. **Erasures / unknowns**
   - Occurrences `7`, `10`, and `17` are labeled `[?]` with role `Erasure (Unknown?)`.
   - These should remain null/uncertain in structured data.

2. **Sequence coverage vs. total sign count**
   - The document reports `20 signs / 3 words`.
   - The visible word pages account for 11 sign positions if taken literally, or 10/11 cleanly matched occurrences depending on whether one counts surrounding non-word signs and erasures.
   - So the site distinguishes between total sign occurrences and word-level sequence groupings; they are related but not identical.

3. **Role labels are source assertions**
   - Labels such as `Logogram`, `Syllabogram`, and `Fraction` were extracted from the site.
   - I preserved them as evidence from the snapshot, not as independently verified epigraphic claims.

4. **Sequence-to-occurrence linkage is derived**
   - The sequence pages do not spell out occurrence IDs in plain text.
   - I linked them by exact SVG rectangle equality across pages.
   - That is a strong inference, but it should still be marked as a derived relation with method provenance.

## Why this matters to the project mission

The important result is not just that `HT 24a` can be read. It is that the legacy site already contains a **recoverable corpus ontology**:
- `Location` → `Document` → `SignOccurrence` / `Sequence`
- plus image assets and external corpus provenance

That is exactly the sort of structure needed for:
- accountable corpus storage
- Structured records with clean relationships
- hybrid browse + query interfaces
- AI assistance grounded in explicit evidence instead of hallucinated summaries

In other words: the site is not merely a pile of HTML pages. It is a latent database wearing a website costume.

## Additional parsing work needed to scale

To scale this from one document to the whole site, I would do the following:

1. **Generalize the extractor over all document folders**
   - parse `document/*/index.html`
   - parse all `index-N.html` and `index-word-N.html`
   - normalize URL-decoding and special characters in document IDs

2. **Build controlled-vocabulary tables from the facet directories**
   - `location/`
   - `kind/`
   - `period/`

3. **Separate evidence from derivation explicitly**
   - store source-extracted fields as first-order evidence
   - store bbox-based sequence membership as a derived relation with method notes

4. **Handle edge cases**
   - erasures and uncertain signs
   - documents with more complex layouts
   - variant role labels
   - non-word signs, fractions, and logograms that may not participate in word pages cleanly

5. **Add validation passes**
   - compare reported sign counts against extracted occurrences
   - compare reported word counts against extracted sequence pages
   - flag mismatches for manual review

## Deliverable produced

Structured extraction file:
- `data/extraction-proofs/haghia-triada-ht24a.json`

That JSON is the practical proof: this subset has already been mapped into schema-shaped structured data with provenance and explicit uncertainty handling.
