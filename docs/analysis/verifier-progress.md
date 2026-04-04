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
