# Verifier R3 — RILA 2025 Extraction

## Task
Extract all data possible from `references/core/RILA_Supplement_2025_Index_Only.pdf` and produce:
- `linear_a/data/rila_2025_concordances.json`
- a verifier note documenting what was and was not recoverable

## Result
**Partial extraction completed.**

The available PDF artifact is **not** a full concordance dump. It appears to contain front matter / table-of-contents material, plus visible listings for the doubtful-inscription section, but **not** the full concordance pages needed for a complete extraction.

## Evidence / method
### File checked
- `references/core/RILA_Supplement_2025_Index_Only.pdf`
- SHA1: `5ddddc024314a7638f4b34078f5fcd3f167d3cd4`

### Tooling reality
The round-2 assignment suggested using `pdftotext`, but in this environment:
- `pdftotext` = **not installed**
- `pdfinfo` = **not installed**

So I used the available PDF analysis path instead.

## What was extractable
### 1. Structural site/type skeleton
The PDF makes visible the supplement's section structure by document type and site, including:
- Tablets
- Nodules / roundels / miscellaneous W-documents
- Stone-vessel inscriptions (Za)
- Incised clay-vessel inscriptions (Zb)
- Painted clay-vessel inscriptions (Zc)
- Metal-support inscriptions (Zf)
- Miscellaneous supports (Zg)

These sections include site groupings and page references. I converted that into the partial JSON structure.

### 2. Doubtful-inscription IDs
The visible doubtful-inscription section provides explicit IDs:
- `D 1` through `D 18`
- with `D 10` shown bracketed as `<D 10>`

These were extracted with site names and page references into the JSON.

## What was NOT extractable
The following could **not** be extracted from the available PDF because the needed pages are not present in the artifact:
- complete **Concordance générale**
- complete **Concordance typologique**
- complete **Concordance géographique**
- complete **Concordance muséographique**
- full normal supplement document IDs beyond the visible doubtful-inscription section
- museum holdings mapping for the supplement corpus

## Deliverable status
### `linear_a/data/rila_2025_concordances.json`
Status: **written**

Contents:
- partial structural extraction
- type groups
- site groups
- visible doubtful-inscription IDs
- explicit note that the extraction is partial
- list of missing concordance components

## Interpretation
This task cannot honestly be called "complete RILA concordance extraction" from the currently available file.

What is now true:
- we do have a useful **structural skeleton** of the supplement by type/site
- we do have visible **D-series doubtful inscription IDs**
- we do **not** have the full concordance data required by the assignment

## Next requirement for full completion
To finish R3 completely, the project needs one of:
1. the full supplement PDF including the concordance pages, or
2. the specific concordance pages (xxvi–xliii), or
3. another text/image source containing those pages

Until then, the JSON should be treated as a **partial extraction only**.
