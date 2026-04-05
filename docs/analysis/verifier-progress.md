## Checkpoint 2026-04-03 22:08 EEST
- Status: IN PROGRESS
- Current section: Quantitative verification against corpus data
- Completed sections: [Assignment intake and source inventory, Analysis document review]
- Next: Verify counts/claims with corpus JSON and targeted PDF extraction; then challenge conclusions and draft review

## Checkpoint 2026-04-04 07:xx EEST
- Status: DRAFT REVIEW COMPLETE
- Completed in this pass:
  - Re-verified core repo counts from `linear_a/data/`:
    - `corpus.json` = 1,880 documents
    - `signs.json` = 386 signs
    - `A301` = 48 occurrences on 48 documents
    - `morphological_analysis.json` = 758 extracted forms, 210 suffixed, 27.7%, 8 suffixes
    - `morphological_analysis.json` also confirms 27 stacking patterns and 34 reduplicated forms
  - Reviewed analysis docs across the current April 2026 set
  - Wrote `docs/analysis/verifier-review-2026-04.md`
- Main findings from this pass:
  - real quantitative work exists and is recoverable
  - biggest immediate issue is mixed denominators / mixed taxonomies across documents
  - several strong claims should be reframed as data-verified vs source-reported vs interpretive
- Remaining work:
  - targeted PDF/source verification for the highest-profile published claims
  - normalization of count provenance across analysis docs

## Checkpoint 2026-04-05 06:xx EEST
- Status: R11 CHECK ATTEMPTED / BLOCKED
- State change:
  - `references/gorila/vol5/` now exists, so the formerly missing source directory has appeared.
- What I did:
  - confirmed vol. 5 contains 524 JPG files
  - sampled multiple tail-end pages where the sign plates should normally appear
  - checked those pages with vision to see whether they were actual plate pages
- Result:
  - sampled late pages are placeholder/watermark images rather than readable GORILA sign plates
  - R11 is therefore still blocked in practice even though the directory now exists
- Output written:
  - `docs/analysis/verifier-gorila-signs.md`
- One-line finding:
  - **Meaningful state change but still blocked:** vol. 5 arrived, yet the current JPG payload does not appear to contain usable sign-plate pages.
