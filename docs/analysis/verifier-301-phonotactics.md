# Verifier R4 — Phonotactic Constraints on *301

## Task
Determine what can precede and follow *301 in the currently attested word inventory, and use that to constrain claims about its phonotactic behavior.

## Sources used in this pass
- `docs/analysis/sign-301.md`
- `linear_a/data/morphological_analysis.json`

## Important note on evidence quality
The strongest usable word inventory for this task in the current repo is the curated list in `sign-301.md`. The morphological JSON only surfaced a small subset of *301-containing strings. So this pass treats `sign-301.md` as the working word list and makes no claim that the list is exhaustive beyond what the current repo surfaces.

## Word list used
The following forms containing *301 were available in current repo materials:

1. `a-ta-i-*301-wa-ja`
2. `a-ta-i-*301-wa-e`
3. `a-ta-i-*301-de-ka`
4. `ja-ta-i-*301-u-ja`
5. `ta-na-i-*301-ti`
6. `ta-na-i-*301-u-ti-nu`
7. `a-*301-ki-ta-a`
8. `zu-*301-se-de-qi-*118`
9. `sa-*301-ri`
10. `na-tu-*301-ne`
11. `te-*301`
12. `a-re-ne-si-di-*301-pi-ke-pa-ja-ta-ri-se-te-ri-mu-a-ja-ku`

## Immediate positional finding
### *301 position in word
- **word-initial:** 0
- **word-medial:** 11
- **word-final:** 1 (`te-*301`)

So the current evidence strongly favors *301 as a **medial sign**, with one attested final use and no attested initial use in the currently surfaced forms.

## Preceding syllables
| Preceding syllable | Count | Attested forms |
|---|---:|---|
| `I` | 6 | `a-ta-i-*301-wa-ja`, `a-ta-i-*301-wa-e`, `a-ta-i-*301-de-ka`, `ja-ta-i-*301-u-ja`, `ta-na-i-*301-ti`, `ta-na-i-*301-u-ti-nu` |
| `A` | 1 | `a-*301-ki-ta-a` |
| `ZU` | 1 | `zu-*301-se-de-qi-*118` |
| `SA` | 1 | `sa-*301-ri` |
| `TU` | 1 | `na-tu-*301-ne` |
| `TE` | 1 | `te-*301` |
| `DI` | 1 | `a-re-ne-si-di-*301-pi-ke-pa-ja-ta-ri-se-te-ri-mu-a-ja-ku` |

### Interpretation
The standout pattern is that *301 most often follows **I** (6/12 forms), especially in the libation-formula family. That does **not** prove a phonological rule by itself, because the formula family may overweight one local morphological template. But it does show that **I + *301** is the strongest attested sequence in the currently surfaced data.

## Following syllables
| Following syllable | Count | Attested forms |
|---|---:|---|
| `WA` | 2 | `a-ta-i-*301-wa-ja`, `a-ta-i-*301-wa-e` |
| `U` | 2 | `ja-ta-i-*301-u-ja`, `ta-na-i-*301-u-ti-nu` |
| `DE` | 1 | `a-ta-i-*301-de-ka` |
| `TI` | 1 | `ta-na-i-*301-ti` |
| `KI` | 1 | `a-*301-ki-ta-a` |
| `SE` | 1 | `zu-*301-se-de-qi-*118` |
| `RI` | 1 | `sa-*301-ri` |
| `NE` | 1 | `na-tu-*301-ne` |
| `PI` | 1 | `a-re-ne-si-di-*301-pi-ke-pa-ja-ta-ri-se-te-ri-mu-a-ja-ku` |
| final position | 1 | `te-*301` |

### Interpretation
The following environment is more dispersed than the preceding environment. No single follower dominates the way `I` dominates in the preceding position. That suggests *301 may be more constrained by what comes **before** it than what comes after it — though the sample is small.

## Distributional summary
### Clear current observations
1. **No initial examples** in the current surfaced word list.
2. **Almost always medial** in the current surfaced forms.
3. **One final example**: `te-*301`.
4. The most frequent immediate left context is **I**.
5. Right contexts are varied: `WA`, `U`, `DE`, `TI`, `KI`, `SE`, `RI`, `NE`, `PI`.

## What this does and does not suggest about phoneme type
### What it supports
The data support a **distributional constraint claim**, not a full phonetic identification:
- *301 is not randomly distributed in the current surfaced forms.
- It appears readily after vowels (`A`, `I`) and also after syllables ending in vowels (`ZU`, `SA`, `TU`, `TE`, `DI`).
- This is compatible with *301 representing a syllabic value or consonant-vowel sign that fits smoothly into normal Linear A word structure.

### What it does NOT prove
The current data do **not** by themselves prove that *301 is:
- a pharyngeal
- a laryngeal
- an ejective
- a special classifier
- or any other specific phoneme class

The present sample is too small and too formula-heavy to support a strong phonetic claim.

## Best current verifier conclusion
The strongest defensible statement from current repo evidence is:

> In the currently surfaced *301 word inventory, *301 is overwhelmingly medial, never initial, and most often follows `I`, especially in formulaic sequences. Its right-side environments are more varied than its left-side environments. This supports the view that *301 occupies a regular syllabic slot in words, but does not by itself identify the phoneme it represents.

## Implications for the main project
This finding slightly strengthens the project's **distribution-first** approach and weakens any wording that jumps too quickly from occurrence patterns to a specific phonetic proposal. The best immediate value of *301 analysis is structural/distributional, not yet phonetic certainty.

## Next useful extensions
1. Re-check the full corpus directly for any additional *301 word contexts beyond the current curated list.
2. Compare *301 distribution against other rare A-series signs with no Linear B equivalent.
3. If GORILA or full inscription transcriptions become available, test whether the non-initial / mostly-medial profile still holds.
