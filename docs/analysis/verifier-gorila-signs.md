# Verifier R11 — GORILA Vol. 5 sign plates check

_Date:_ 2026-04-05

## Status

**Blocked by source-image quality / ingest problem.**

The previously missing `references/gorila/vol5/` directory is now present, so R11 is theoretically unblocked. However, the page-image payload currently available in that directory does **not** appear to contain the actual late-volume sign plates needed for extraction.

## What I checked

- Confirmed `references/gorila/vol5/` now exists.
- Confirmed the volume contains **524 JPG files** (`EtCret_21-5_1985_001.jpg` through `EtCret_21-5_1985_524.jpg`).
- Sampled multiple images from the tail end of the volume, where the assignment said the sign plates should normally appear (pages around `500`, `505`, `510`, `515`, `520`, `524`).
- Used vision inspection on those sampled pages.

## Result

All sampled late-volume images appeared to be the **same placeholder/watermark page**, not actual scanned content. The visible content was an online-publication / watermark screen rather than GORILA page art. In other words:

- I could **not** identify any visible sign-plate headings
- I could **not** extract sign numbers or variants
- I could **not** compare GORILA plate forms against `linear_a/data/signs.json`
- I could **not** compare GORILA plate forms against `docs/images/signs/`

## Why this matters

R11 depends on access to the actual "Planches des signes" pages. Right now, the volume directory exists, but the usable source content for those pages does not appear to be present in the current JPG set.

So the state changed from:

- **before:** `vol5/` missing
- **now:** `vol5/` present, but **still not runnable for sign extraction** because the sampled tail pages are placeholders rather than the expected plates

## Minimal conclusion for now

R11 remains **blocked in practice** pending one of the following:

1. a corrected re-export / re-download of vol. 5 page images,
2. direct access to the true sign-plate pages from vol. 5, or
3. a PDF / alternate scan source with readable plate pages.

## Next suggested action

Builder (or ingest pipeline) should verify whether the current `vol5/*.jpg` files are:

- placeholder pages from the source site,
- failed image captures, or
- a protected/publication wrapper rather than the real book pages.

Once real page images are available, I can resume R11 and produce the intended sign comparison file.
