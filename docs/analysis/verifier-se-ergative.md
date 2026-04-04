# Verifier R1 — Testing the -SE Suffix as Ergative Marker

## Task
Test whether Linear A `-SE` behaves like a Hurrian-style ergative marker by extracting `-SE` forms and checking whether they appear in agent positions rather than patient/object/commodity positions.

## Sources used in this pass
- `references/core/Younger_2024_Linear_A_Lexicon.pdf` (via fallback PDF extraction)
- `linear_a/data/morphological_analysis.json`
- `docs/analysis/morphology.md`

## Tooling / evidence note
The assignment recommended `pdftotext`, but it is **not installed** in this environment. So this pass relies on:
- the structured suffix inventory in `morphological_analysis.json`
- the available PDF extraction path for Younger's lexicon

This means the result is a **real research pass**, but still a first pass rather than a final exhaustive corpus-position analysis.

## 1. -SE forms recovered

### From `morphological_analysis.json`
The current computational morphology file reports **22** `-SE` forms:

- `A-NA-NU-SI-JA-SE`
- `A-SA-SU-MA-I-SE`
- `A-SE`
- `DI-DI-KA-SE`
- `DI-KI-SE`
- `DU-RE-ZA-SE`
- `I-SE`
- `JA-PA-RA-JA-SE`
- `KI-TA-NA-SI-JA-SE`
- `MA-KA-I-SE`
- `MI-ZA-SE`
- `NU-SE`
- `O-TA-NI-ZA-SE`
- `PA-SE`
- `PI-TA-KA-SE`
- `RA-TI-SE`
- `RE-DI-SE`
- `RU-MA-TA-SE`
- `SO-KE-MA-SE`
- `TU-MI-TI-ZA-SE`
- `U-TA-I-SE`
- `ZA-SE`

### From Younger's Lexicon extraction
The lexicon extraction yielded a usable set of clean or near-clean final `-SE` forms (with one or two fragmentary cases):

- `A-SE`
- `DI-DI-KA-SE`
- `DU-RE-ZA-SE`
- `JA-PA-RA-JA-SE`
- `KI-TA-NA-SI-JA-SE`
- `A-NA-NU-SI-JA-SE[`
- `MA-KA-I-SE`
- `MI-ZA-SE`
- `O-TA-NI-ZA-SE`
- `PA-SE`
- `PI-TA-KA-SE`
- `RE-DI-SE`
- `RU-MA-TA-SE`
- `SO-KE-MA-SE`
- `TU-MI-TI-ZA-SE`
- `•-RA-KI-•-SE`

Additional repo-only candidates from the morphology JSON that did not surface as clearly in the fallback lexicon pass include:
- `DI-KI-SE`
- `I-SE`
- `NU-SE`
- `RA-TI-SE`
- `U-TA-I-SE`
- `ZA-SE`

## 2. Context types recoverable from the lexicon pass

The lexicon extraction provided context notes for many forms. These do **not** yet amount to full syntactic analysis, but they are enough to classify the immediate attestation type.

### A. Clear or likely names in lists
These are especially important because names in lists do **not automatically behave like ergative subjects**.

- `A-SE` — name / first name / word
- `DU-RE-ZA-SE` — name in list
- `JA-PA-RA-JA-SE` — name?
- `MA-KA-I-SE` — name in list
- `O-TA-NI-ZA-SE` — name in list
- `PA-SE` — first/second name in two-name list
- `RE-DI-SE` — name in list
- `RU-MA-TA-SE` — name in list
- `SO-KE-MA-SE` — name in list
- `TU-MI-TI-ZA-SE` — name in list
- `•-RA-KI-•-SE` — name?

### B. Headings / administrative word-like contexts
- `DI-DI-KA-SE` — heading, first word, possibly verbal
- `PI-TA-KA-SE` — heading, name?

### C. Derived/ethnic-looking forms
- `KI-TA-NA-SI-JA-SE` — described as a word formed from a hypothetical place name
- `A-NA-NU-SI-JA-SE[` — similarly described as a place-name derivative

### D. Unclear / not enough context in this pass
- `MI-ZA-SE` — cited but context not clearly specified in the extracted note
- repo-only forms like `DI-KI-SE`, `I-SE`, `NU-SE`, `RA-TI-SE`, `U-TA-I-SE`, `ZA-SE` need deeper context lookup

## 3. Preliminary distributional conclusion

### What we would expect if -SE were a strong ergative marker
If `-SE` functioned primarily as a Hurrian-style ergative marker, we would expect many `-SE` words to appear in contexts that look like:
- the acting entity in a transitive event
- clear agent positions
- recurring syntactic roles distinct from commodities or patient roles

### What the current evidence actually shows
The current first-pass evidence does **not** show a clean agent-only distribution.

Instead, many `-SE` forms are attested as:
- **names in lists**
- **headings**
- **derived forms that may be adjectival/ethnic**
- **unclear administrative words**

That does **not** rule out an instrumental/case function in some subset of forms, but it **does** weaken the strongest version of the claim that `-SE` is straightforwardly an ergative marker parallel to Hurrian `-s(e)`.

## 4. Best current verifier judgment

### Conservative conclusion
The current repo evidence supports this weaker statement:

> `-SE` is a productive Linear A suffix that appears on a mixed set of forms, including many names/list entries, some headings, and some derived-looking forms. The presently surfaced evidence does not justify treating `-SE` as a cleanly demonstrated ergative marker.

### What remains plausible
- `-SE` could still have an **instrumental**, **relational**, or **case-like** function in some forms.
- The Hurrian comparison remains typologically interesting.
- But the current evidence base is too mixed to say: **“LA -SE = Hurrian ergative”** with confidence.

## 5. Count summary (current first pass)

### Recoverable context categories from the lexicon extraction
Approximate first-pass classification of clearly surfaced final `-SE` forms:

- **names / likely personal names:** about 10–11
- **headings / possible administrative operators:** 2
- **place-derived / ethnic-looking words:** 2
- **unclear in this pass:** several remaining forms

This balance is not what we would hope to see if `-SE` were already demonstrated as a strong agent-case marker.

## 6. What would be needed to strengthen the claim
A stronger test would require:
1. direct lookup of each cited tablet in corpus/transcription context
2. determining whether the `-SE` form stands in actor position, commodity position, heading position, or list position
3. comparing those roles across all `-SE` attestations

That is the next-step corpus-context version of this task.

## Bottom line
The first-pass evidence does **not** support a strong claim that `-SE` has already been shown to function as an ergative marker. It remains a live hypothesis, but the currently surfaced attestations are too mixed — especially because so many are names in lists or administrative headings rather than clearly recoverable transitive-agent contexts.
