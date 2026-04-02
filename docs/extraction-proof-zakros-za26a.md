# Extraction proof: Zakros pilot (`ZA 26a`)

## Target

I chose a **single-document pilot inside the Zakros subset**: `ZA 26a`.

Why this slice:
- It is small enough to verify carefully by hand.
- It still exposes the full structural chain: site page, document page, eight sign-occurrence pages, four word pages, crop images, and SVG coordinates.
- It includes both a **logogram** and an **unknown sign**, so it tests whether the extraction can preserve mixed evidence without over-normalizing it.

Relevant source pages in the imported snapshot:
- `imported/lineara-website/site/location/Zakros/index.html`
- `imported/lineara-website/site/document/ZA 26a/index.html`
- `imported/lineara-website/site/document/ZA 26a/index-1.html` … `index-8.html`
- `imported/lineara-website/site/document/ZA 26a/index-word-0.html` … `index-word-3.html`

## What was parsed

### 1. Location-level context
From `location/Zakros/index.html`:
- Site label: `Zakros`
- Reported document count at that site: `44`

That matters because this is a genuine site subset, not an isolated page.

### 2. Document-level metadata
From `document/ZA 26a/index.html` I reliably extracted:
- document code: `ZA 26a`
- kind: `Tablet`
- location: `Zakros`
- period: `LM IB`
- dimensions: `4.1 × 2.9 × 0.7 cm`
- external corpus link
- drawing image path
- reported totals: `8 signs / 4 words`

### 3. Sign-occurrence layer
From the main document page I extracted **8 occurrence records** with:
- occurrence number (`#1` … `#8`)
- site-provided role label (`Syllabogram`, `Logogram`)
- sign code when present (`AB41`, `AB04`, `AB07`, `AB21f`, `AB57`, `AB67`)
- display reading when present (`si`, `te`, `di`, `AB21/OVISf`, `ja`, `ki`)
- exact SVG bounding box on the tablet image
- per-occurrence crop image path
- provenance back to source HTML pages

Especially useful here:
- occurrences `3` and `4` repeat the same sign (`AB07` / `di`)
- occurrence `5` is a logogram with site display `AB21/OVISf`
- occurrence `8` is explicitly unknown (`[?]`)

### 4. Sequence / word layer
From `index-word-0.html` to `index-word-3.html` I extracted **4 sequence records**:
- Sequence 1: `si-te` (`AB41-AB04`)
- Sequence 2: `di-di-[` (normalized pattern `AB07-AB07`)
- Sequence 3: `ja-ki[` (`AB57-AB67`)
- Sequence 4: `][?][` (normalized pattern `[?]`)

For each sequence I also extracted the selected-word SVG rectangles and matched them back to occurrence rectangles on `index.html` by exact coordinate equality.

Matched occurrence IDs:
- Sequence 1 → `[1, 2]`
- Sequence 2 → `[3, 4]`
- Sequence 3 → `[6, 7]`
- Sequence 4 → `[8]`

This is a clean proof that the site supports reconstruction of:
- document metadata
- occurrence-level attestations
- word/sequence segmentation
- image-grounded links between pages

## Fields that were reliably extracted

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

### SignOccurrence
Reliable:
- `occurrence_number`
- `role`
- `sign_code` when present
- `display_reading` when present
- `bbox_on_document_image`
- `source_occurrence_page`
- `source_crop_image`
- explicit uncertainty where the site shows `[?]`

### Sequence
Reliable:
- `sequence_number_within_document`
- `display_reading`
- `normalized_pattern`
- `reported_sign_count`
- `selected_word_bboxes`
- derived `matched_occurrence_numbers_by_bbox`
- `source_page`

## Ambiguities and caution points

1. **Unknown final sign**
   - Occurrence `8` is `[?]` on the document page and remains null/unknown in the JSON.
   - The word page still treats it as a one-sign sequence, which is valuable structure even though the sign identity is unresolved.

2. **Bracketed sequence displays are source renderings**
   - Sequence displays such as `di-di-[`, `ja-ki[`, and `][?][` are taken from the site UI.
   - I preserved those literal displays as source evidence and kept the normalized pattern separate.

3. **Logogram display vs. sign code**
   - Occurrence `5` presents site code `AB21f` and display reading `AB21/OVISf`.
   - Those should remain distinct fields; collapsing them would destroy provenance.

4. **Sequence-to-occurrence linkage is derived**
   - The linkage is not printed as plain occurrence IDs on the word pages.
   - I derived it by exact bounding-box equality across pages and marked the method explicitly.

## Why this matters to the project mission

`ZA 26a` shows that the Zakros subset is not merely browseable HTML. It is structured enough to become accountable corpus data with:
- archaeological context
- sign-level evidence
- word segmentation
- image-grounded provenance
- preserved uncertainty

That is exactly what the project needs if the goal is a corpus that can support relational storage and AI-assisted interpretation without blurring source facts and derived links.

## Deliverable produced

Structured extraction file:
- `data/extraction-proofs/zakros-za26a.json`
