# Linear A site-derived schema draft

Derived from the raw imported website snapshot in `imported/lineara-website/site/` on 2026-04-01.

## Purpose

This draft converts the old website's implicit data model into an explicit schema for the next-generation research site, search layer, and AI interface.

## Design principles

- Keep archaeology, inscription, and media distinct.
- Treat document IDs as first-class identifiers.
- Preserve controlled vocabularies from the imported site where they are already useful.
- Separate evidence from interpretation.
- Support both faceted browse and AI/semantic search.

---

## Core entities

### 1. Document
The primary corpus unit.

Examples:
- `HT 1`
- `HT 154A`
- `ARKH 1a`
- `GO Wc 1a`

Suggested fields:
- `id` — internal stable UUID
- `document_code` — canonical code shown to users (`HT 154A`)
- `document_code_normalized` — machine-safe key
- `title` — optional display title
- `location_id` — foreign key
- `kind_id` — foreign key
- `period_id` — foreign key
- `support_material` — optional (clay, stone, metal, etc.)
- `description` — short neutral summary
- `notes_editorial` — internal curation notes
- `publication_status` — published / fragmentary / uncertain / etc.
- `source_snapshot_path` — path from imported site
- `external_reference_url` — source/reference URL when known

Relationships:
- one `Document` belongs to one `Location` (or uncertain)
- one `Document` belongs to one `Kind` (or uncertain/multiple with priority)
- one `Document` belongs to one `Period` (or uncertain)
- one `Document` has many `Attestations`
- one `Document` has many `ImageAssets`
- one `Document` has many `BibliographicLinks`

---

### 2. Attestation
A sign-level or segment-level occurrence within a document.

Why this exists:
- the imported site explicitly supports `search-attestation.html`
- document folders contain multiple `index-n.html` pages, suggesting sub-document views

Suggested fields:
- `id`
- `document_id`
- `attestation_number` or `attestation_label`
- `sequence_text` — encoded sign sequence as represented in the corpus
- `sequence_normalized` — normalized search form
- `line_label` — if applicable
- `position_label` — if applicable
- `reading_direction` — optional
- `certainty` — certain / uncertain / restored / damaged
- `commentary` — editorial observation
- `source_snapshot_path`

Relationships:
- many attestations belong to one document
- one attestation has many sign-occurrence rows

---

### 3. Sign
Canonical sign inventory entity.

Why this exists:
- imported site includes `sign-list.html`
- sequence/attestation search implies reusable sign inventory

Suggested fields:
- `id`
- `sign_code` — canonical sign label
- `sign_number` — if numeric catalogue applies
- `transliteration` — standard textual representation
- `unicode_or_private_code` — if applicable
- `description`
- `variant_notes`
- `source_system` — GORILA / SigLA / site-native / project-native

Relationships:
- one sign appears in many sign occurrences
- one sign may have many variants

---

### 4. SignOccurrence
Join layer between `Attestation` and `Sign`.

Suggested fields:
- `id`
- `attestation_id`
- `sign_id`
- `ordinal_in_sequence`
- `surface_position`
- `certainty`
- `is_damaged`
- `is_restored`
- `notes`

Purpose:
- supports sequence search
- supports sign-level statistics
- supports image anchoring later

---

### 5. Sequence
Optional reusable abstraction for recurring strings/formulae.

Why this matters:
- imported site includes `search-sequence.html`
- useful for recurring formulae, especially libation formula analysis

Suggested fields:
- `id`
- `sequence_text`
- `sequence_normalized`
- `sequence_type` — formula / lexical / unknown / administrative pattern
- `notes`
- `is_recurring`

Relationships:
- many sequences may be linked to many attestations

---

## Context / facet entities

### 6. Location
Controlled vocabulary from imported site.

Observed values include:
- Arkhanes
- Gournia
- Haghia Triada
- Khania
- Knossos
- Mallia
- Phaistos
- Zakros
- etc.

Suggested fields:
- `id`
- `name`
- `name_normalized`
- `region`
- `latitude`
- `longitude`
- `description`
- `notes`

---

### 7. Kind
Artifact / support type vocabulary.

Observed values include:
- Tablet
- Roundel
- Nodule
- Sealing
- Libation table
- Clay weight
- Pithos
- Jewellery
- Graffiti
- etc.

Suggested fields:
- `id`
- `name`
- `name_normalized`
- `description`
- `broader_category`

---

### 8. Period
Chronological vocabulary.

Observed values include:
- LM I
- LM IA
- LM IB
- LM II
- MM II
- MM III
- MM III-LM IA
- unknown

Suggested fields:
- `id`
- `label`
- `sort_key`
- `date_range_text`
- `notes`

---

## Media / provenance entities

### 9. ImageAsset
The imported site clearly carries document image assets and previews.

Suggested fields:
- `id`
- `document_id`
- `attestation_id` — optional
- `file_path`
- `file_name`
- `mime_type`
- `width`
- `height`
- `caption`
- `source_snapshot_path`
- `license`
- `credit`

---

### 10. BibliographicSource
For scholarly and source attribution.

Suggested fields:
- `id`
- `citation_short`
- `title`
- `author`
- `year`
- `publisher_or_journal`
- `url`
- `source_type` — corpus / article / review / database / web page
- `evidence_class` — core / comparative / fringe / reference only
- `notes`

---

### 11. DocumentBibliography
Join between documents and references.

Suggested fields:
- `id`
- `document_id`
- `bibliographic_source_id`
- `relation_type` — publication / discussion / image source / commentary
- `notes`

---

## Optional research-layer entities

### 12. InterpretationClaim
Useful if the new site distinguishes evidence from hypotheses.

Suggested fields:
- `id`
- `document_id` or `sequence_id`
- `claim_text`
- `claim_type` — reading / linguistic affiliation / formula interpretation / chronology
- `status` — accepted / debated / speculative / fringe
- `source_id`
- `notes`

This is probably smart because the project already contains both strong scholarly material and speculative decipherment material.

---

## Immediate practical mappings from the imported site

### Existing site axis → new schema
- `document/` → `Document`
- `location/` → `Location`
- `kind/` → `Kind`
- `period/` → `Period`
- `search-attestation.html` → `Attestation` + `SignOccurrence`
- `search-sequence.html` → `Sequence`
- `sign-list.html` → `Sign`
- document images / thumbnails → `ImageAsset`

---

## MVP schema recommendation

If building in phases, start with:
- `Document`
- `Location`
- `Kind`
- `Period`
- `ImageAsset`
- `BibliographicSource`

Then add:
- `Attestation`
- `Sign`
- `SignOccurrence`
- `Sequence`

Then later:
- `InterpretationClaim`

---

## Why this matters for the AI-enabled site

This schema supports:
- faceted browse
- exact document lookup
- sign/sequence search
- semantic search over structured entities
- AI answers grounded in corpus data instead of vague chat
- separation of evidence, metadata, and interpretation

That is the right foundation for a serious Linear A research site rather than a pretty wrapper around blobs.
