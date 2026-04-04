# Verifier R6 — Cross-Site Dialect Variation

## Task
Test whether Linear A shows cross-site vocabulary differences, site-exclusive words, and possible dialect or register variation.

## Sources used in this pass
- `linear_a/data/glossary.json`
- project site-distribution notes already embedded in the glossary entries

## Evidence note
This is a first-pass dialect-variation study based on the current 52-word glossary, not a full token-by-token corpus reconstruction from Younger's Lexicon. It is therefore strongest for **known frequent words with site metadata**, and weaker for total-vocabulary claims.

## 1. Top glossary words and site spread
Ignoring pure suffix entries (`-ro`, `-ra`, `-na`, etc.), the highest-frequency lexical items in the current glossary show the following site patterns:

| Word | Freq | Class | Sites |
|---|---:|---|---|
| `ku-ro` | 36 | administrative | Haghia Triada, Phaistos, Zakros |
| `sa-ra` | 20 | administrative | Haghia Triada only |
| `ki-ro` | 17 | administrative | Haghia Triada only |
| `i-ra` | 16 | name | Haghia Triada only |
| `a-du` | 12 | name | Haghia Triada, Khania, Tylissos |
| `si-ka` | 10 | name | Haghia Triada only |
| `da-ka` | 10 | name | Haghia Triada only |
| `ku-*56-nu` | 8 | name | Haghia Triada, Phaistos |
| `ma-di` | 7 | name | Haghia Triada, Phaistos |
| `sa-ru` | 6 | name | Haghia Triada only |
| `pa-se-ja` | 5 | name | Haghia Triada only |
| `ku-pa` | 5 | name | Haghia Triada, Khania, Zakros |
| `ka-pa` | 5 | administrative | Haghia Triada only |
| `ka-ku-pa` | 5 | name | Haghia Triada only |
| `di-na-u` | 5 | name | Haghia Triada only |
| `da-re` | 5 | name | Haghia Triada only |

## 2. Immediate pattern: Haghia Triada dominates the lexical picture
The clearest result from the glossary is that **Haghia Triada (HT)** dominates the known lexical inventory.

This produces two effects:
1. many words are HT-only simply because HT provides by far the densest administrative dataset
2. any dialect claim must be careful not to confuse **archive size** with **regional language difference**

## 3. Site-exclusive words
### Strongest current site-exclusive signals
The following glossary entries are currently HT-only:
- `sa-ra`
- `ki-ro`
- `ka-pa`
- `je-di`
- `po-to-ku-ro`
- `da-me`
- `sa-ro`
- plus many names (`i-ra`, `si-ka`, `da-ka`, `sa-ru`, etc.)

The single strongest non-HT site-exclusive signal in the current glossary is:
- `ku-do-ni` — **Khania only**

But `ku-do-ni` is a place name, so it is not strong evidence of dialect by itself.

## 4. HT vs KH comparison
### Haghia Triada (HT)
HT has the richest and most specialized administrative vocabulary in the current glossary:
- `ku-ro`
- `ki-ro`
- `sa-ra`
- `po-to-ku-ro`
- `da-me`
- `ka-pa`
- `je-di`
- `sa-ro`

This suggests HT is not just lexically richer because of volume; it also preserves a particularly dense **administrative register**.

### Khania (KH)
KH appears in the glossary primarily with:
- `a-du`
- `ku-pa`
- `ku-do-ni`

Compared with HT, Khania currently shows **fewer specialized administrative terms** in the project glossary and relatively more dependence on names / toponyms in the known-word layer.

### First-pass interpretation
The current evidence suggests a stronger difference in **archive function and register** than in clearly demonstrable spoken dialect.

HT looks like the center where the best-understood accounting vocabulary clusters.
KH looks lexically thinner in the current glossary, though that may partly reflect extraction bias and corpus imbalance.

## 5. Cross-site words vs local words
### Broadly distributed words
Some words clearly travel across sites:
- `ku-ro` — HT / PH / ZA
- `a-du` — HT / KH / TY
- `ku-pa` — HT / KH / ZA
- `ku-*56-nu` — HT / PH
- `ma-di` — HT / PH

These are the better candidates for island-wide or supra-local vocabulary.

### Localized words
Words currently restricted to one archive, especially HT, may reflect:
- local administrative habits
- local institutions
- archive-specific jargon
- or true dialect variation

Current evidence is not yet enough to distinguish those cleanly.

## 6. The libation formula and regional variation
The glossary includes ritual-only entries:
- `a-ta-i-*301-wa-ja`
- `ja-sa-sa-ra-me`
- `i-da-ma-te`
- `a-di-ki-te`

These are labeled to **ritual sites** rather than one archive center. That already suggests an important contrast:
- administrative vocabulary is archive-localized, especially at HT
- ritual vocabulary is more geographically distributed across sanctuary contexts

This is compatible with the idea that ritual language was more standardized across Crete, while administrative wording may have varied more by center.

## 7. Best current verifier conclusion
The strongest defensible first-pass conclusion is:

> The current glossary suggests strong **cross-site register variation**, especially between the dense administrative vocabulary of Haghia Triada and the thinner known-word profiles of other sites such as Khania. There are many site-exclusive words, but because Haghia Triada dominates the lexical evidence, these should not yet be treated as pure dialect markers. At present, the evidence more strongly supports **archive-specific administrative vocabulary differences** than a securely demonstrated spoken dialect split.

## 8. What looks most promising
### Strongest current findings
1. **HT is lexically distinctive** in the administrative register.
2. **KH does not yet show the same dense specialized admin vocabulary** in the glossary.
3. **Ritual vocabulary appears more cross-site / supra-local** than admin vocabulary.
4. Some words (`ku-ro`, `a-du`, `ku-pa`) appear broad enough to represent shared inter-site vocabulary.

## 9. What would strengthen this task next
A stronger R6 would require:
1. extracting the true top 20 corpus words from the full lexicon/corpus rather than just the glossary
2. comparing suffix distributions by site directly from `morphological_analysis.json` or corpus token lists
3. isolating libation-formula variants by sanctuary/site to test regional ritual wording more precisely

## Bottom line
There is evidence for **site-based lexical differentiation**, but the safest current interpretation is not “we have proven separate dialects.” The better first-pass claim is:
- **administrative vocabulary varies strongly by archive center**
- **ritual vocabulary is more standardized across sites**
- **true dialect claims remain plausible but not yet proven from the current glossary-level evidence alone**
