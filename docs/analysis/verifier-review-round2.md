# Verifier Review — Round 2

**Verifier:** Clawdia / Bot B  
**Date:** April 2026  
**Scope:** Round 2 research tasks completed so far: C-FIX, R3, R4, R1, R6, R7, R10  
**Not yet completed in this round:** R9 corrections audit, R11 GORILA sign-plate review

---

## Executive summary

Round 2 produced real research results, not just editorial criticism.

The strongest overall picture now is:
- the project's best-supported lane remains the ***301 distributional / structural problem**
- the **administrative core vocabulary still resists Greek, Hurrian, and Semitic reduction**
- **Anatolian/Luwian contact is real**, but appears concentrated in ritual / elite vocabulary rather than the accounting core
- **cross-site differences exist**, but current evidence more strongly supports **archive/register variation** than securely proven spoken dialect splits
- the `-SE` suffix is **not yet demonstrated** as a clean ergative marker
- the strongest Greek steelman still fails to overturn the present conclusion that the core Linear A language is unlikely to be Greek

In short:
> Round 2 strengthens the project's core caution. The language behind Linear A still looks like a non-Greek, non-Semitic, suffixing language with selective Anatolian contact and significant internal structural regularity — but not yet one that can be securely assigned to a known family.

---

## 1. What was completed in Round 2

### Completed deliverables
- `docs/analysis/count-provenance.md`
- `linear_a/data/rila_2025_concordances.json`
- `docs/analysis/verifier-rila-extraction.md`
- `docs/analysis/verifier-301-phonotactics.md`
- `docs/analysis/verifier-se-ergative.md`
- `docs/analysis/verifier-dialect-variation.md`
- `docs/analysis/verifier-luwian-contact.md`
- `docs/analysis/verifier-greek-steelman.md`

### Upstream commits
- `1a0744d` — count provenance table
- `23bfb2f` — partial RILA extraction
- `bd9bd91` — *301 phonotactics
- `532e881` — -SE ergative test
- `743cbbd` — Luwian contact beyond formula
- `8fd89c3` — cross-site dialect variation
- `559ee64` — Greek steelman

---

## 2. Major findings from the completed tasks

## 2.1 C-FIX — Count provenance was a real research prerequisite, not just housekeeping

The count-provenance table confirmed that the project had been mixing different universes of evidence:
- project corpus size
- published inscription counts
- morphology extraction counts
- lexicon counts
- functional sign inventory counts
- graphic-form sign inventory counts

### What this changed
This was not a cosmetic fix. It changed how later verifier work had to be interpreted.

It is now much clearer that:
- **1,880** ≠ **1,534**
- **758** ≠ **1,463**
- **386** ≠ **178/164/47**
- **315** is a display-layer count, not a full sign-inventory claim

This matters because it prevents false contradiction and false confirmation.

---

## 2.2 R3 — The available RILA 2025 source is genuinely partial

The local PDF artifact (`RILA_Supplement_2025_Index_Only.pdf`) is only a **4-page front-matter / table-of-contents artifact**, not the full concordance section.

### What was still recovered
A partial structural extraction was possible:
- type-group skeleton
- site-group skeleton
- visible doubtful-inscription IDs `D1–D18`

### What this means
The project should stop speaking as if the full 2025 supplement concordances were already locally extractable. They are not.

This was a useful negative result:
> the bottleneck here is source completeness, not analytical laziness.

---

## 2.3 R4 — *301 remains the strongest quantitative lane

The verifier *301 phonotactic pass found:
- no initial examples in the currently surfaced forms
- **11/12 medial** positions
- **1/12 final** position
- strongest left context = **I**
- right contexts more varied than left contexts

### What survives from that
The best-supported current *301 claim is structural/distributional:
- *301 is not randomly placed
- it occupies a regular word-internal slot
- it is heavily patterned, especially in formulaic material

### What does NOT survive
The current evidence still does **not** justify a confident phoneme-class claim such as:
- pharyngeal
- laryngeal
- ejective
- special classifier sign

### Bottom line
The *301 lane is publication-worthy **as a distributional problem**, not yet as a phonetic solution.

---

## 2.4 R1 — `-SE` is weaker as an ergative argument than previously implied

The verifier pass on `-SE` found that many `-SE` forms appear as:
- names in lists
- headings / administrative contexts
- derived-looking forms
- unclear contexts not obviously agentive

### What survives
It is still possible that `-SE` has:
- case-like behavior
- instrumental/relational behavior
- some role-specific function in a subset of forms

### What weakened
The strongest version of the claim —
> "Linear A -SE behaves like a Hurrian-style ergative marker"
— is **not currently demonstrated**.

### Bottom line
`-SE` remains interesting, but it is no longer a clean flagship argument for a Hurrian-style grammar.

---

## 2.5 R6 — Site differences are real, but they look more like archive/register effects than clean dialect splits

From the current glossary-level pass:
- `ku-ro` is cross-site
- `ki-ro` is HT-only in current known distribution
- `sa-ra` is HT-only in current known distribution
- `ku-do-ni` is KH-only but is a place name
- HT preserves the densest specialized administrative vocabulary

### What survives
There is real site-based lexical differentiation.

### What weakened
The easiest reading would be:
> "we have proven dialects"

That is too strong.

### Better reading
Current evidence more strongly supports:
- **archive-specific administrative vocabulary concentration**
- especially at **Haghia Triada**
- versus thinner or different lexical profiles elsewhere

### Bottom line
The evidence is stronger for **register / archive differentiation** than for securely demonstrated spoken dialects.

---

## 2.6 R7 — Anatolian/Luwian contact appears selective, not total

The verifier pass confirmed the strongest contact case remains:
- `ja-sa-sa-ra-me`

The larger pattern now looks like this:
- Anatolian/Luwian contact is strongest in **ritual / elite vocabulary**
- not in the **administrative core vocabulary**

### What survives
This strengthens the project's contact model.

### What weakened
It weakens any tendency to slide toward:
- "Linear A is basically Anatolian"
- "the administrative language is Luwianized"

### Better conclusion
The better model is:
- a distinct local language
- with selective prestige borrowing / cult contact / elite interaction with the Anatolian sphere

---

## 2.7 R10 — Greek remains worth adversarial testing, but not as the best current explanation

The Greek steelman found the strongest Greek-side arguments are:
- script continuity with Linear B
- toponym continuity
- some LA-LB overlap
- orthographic caution against over-fast rejection

### What survives
The anti-Greek case should not be phrased lazily.
Orthographic mismatch alone is not enough.
Proper names and toponyms remain real testing ground.

### What weakened
Even after steelmanning Greek as hard as possible, the overall Greek hypothesis still falls short because:
- morphology remains a bad fit
- most strong anchors are not convincingly Greek
- place-name continuity is weaker evidence than full-language continuity

### Bottom line
Greek remains a useful adversarial test, but not the leading explanation of the corpus.

---

## 3. What now looks stronger than it did before

After Round 2, the following claims look stronger:

### S1. The project's structural work is stronger than some of its headline wording
The data-driven lanes are often better than the prose that summarizes them.

### S2. *301 is still the best deep-dive lane
It is quantitatively anchored, constrained, and genuinely unresolved.

### S3. The language still looks more suffixing/agglutinative than fusional/root-and-pattern
Nothing in Round 2 weakened the broad structural case against simple Greek or Semitic identification.

### S4. The contact picture is becoming clearer
The current best contact model is selective Anatolian/Luwian influence in prestige/ritual vocabulary, not full language identity.

---

## 4. What now looks weaker than it did before

### W1. Strong `-SE = ergative` claims
Too strong on current evidence.

### W2. Easy dialect claims
Too strong on current glossary-level evidence.

### W3. Broad statements that Greek is "fully disproved"
The better phrasing is that Greek remains a weak explanation after adversarial testing, not that it is intellectually unworthy of testing.

### W4. Any implication that the full 2025 RILA supplement was locally extractable
It was not.

---

## 5. What remains open

1. **Exact family placement**  
   Still unresolved.

2. **True role of `-SE`**  
   Still unresolved.

3. **Phonetic value of *301**  
   Still unresolved.

4. **Extent of real dialect variation**  
   Still unresolved; archive effects are currently the stronger explanation.

5. **Administrative borrowings from Anatolian?**  
   Still unresolved; current evidence suggests no strong case yet.

6. **What the incomplete RILA supplement would add if obtained in full**  
   Still unresolved.

---

## 6. New falsifiable hypothesis

## Hypothesis H1 — The sharpest distinctions in the current Linear A corpus are driven more by **register specialization** than by **spoken dialect divergence**

### Why this is new/useful
The completed verifier tasks together point toward a specific pattern:
- HT has dense specialized administrative vocabulary
- ritual formula language is distributed differently across sites
- contact vocabulary clusters in ritual/elite domains
- site-exclusive words often sit inside specific archive functions rather than obviously phonological dialect clusters

This suggests a stronger hypothesis than simply "there were dialects":

> The main linguistic partition visible in the current corpus is between **administrative register** and **ritual register**, with site differences largely mediated by archive function rather than by sharply divergent spoken dialects.

### Why this is falsifiable
This can be tested.

### Predictions
If the hypothesis is correct:
1. words that appear site-exclusive in one archive should cluster by **document type / register** more than by purely geographic separation
2. ritual formula vocabulary should show broader cross-site stability than narrow administrative jargon
3. suffix distributions should differ more strongly by **text type** than by site alone
4. the strongest contact vocabulary (e.g. Anatolian/Luwian-linked terms) should cluster in ritual/elite contexts, not in ordinary accounting terms

### What would support it
- text-type clustering of key words and suffixes
- repeated cross-site ritual forms with stable morphology
- archive-local administrative lexicons that do not produce clean phonological dialect bundles

### What would weaken or refute it
- strong site-based phonological or morphological splits that persist across all text types
- clear evidence that the same register behaves differently by site in systematic, language-level ways
- widespread site-exclusive non-administrative core vocabulary that cannot be explained by archive function

### Why this matters
This hypothesis changes the project's center of gravity.
It says the most useful next analytic question may not be:
> "Which family is Minoan?"

but rather:
> "How many linguistic layers are we actually looking at — ritual language, archive language, place-name layer, personal-name layer, and contact vocabulary — and which of those are being mistaken for one another?"

That is testable and high-value.

---

## 7. Recommended next steps

### Immediate next research task
**R9 corrections audit**

Why:
- direct credibility gain
- improves confidence in downstream analysis
- cleaner and more bounded than speculative extension

### Parallel project-planning task
Create a **website restructuring brief**, not a full rewrite yet.

Why:
- the verifier results now justify clearer audience lanes and confidence labels
- but site implementation should follow verified synthesis, not race ahead of it

### Research priority after that
If source readiness allows, revisit:
- full corpus context for `-SE`
- text-type clustering for the new register-vs-dialect hypothesis
- better *301 contextual corpus extraction

---

## Bottom line

Round 2 materially improved the project.

The best-supported current picture is:
- Linear A still looks like a **non-Greek, non-Semitic, strongly suffixing language**
- Anatolian/Luwian contact is **real but selective**
- *301 remains the strongest deep research lane
- `-SE` and dialect claims both require more caution than some earlier prose implied
- the next high-value move is to tighten corpus reliability and separate **register effects** from **true language-variation effects**

The project is strongest when it speaks in that voice: ambitious, evidence-driven, and careful about what has and has not yet been shown.
