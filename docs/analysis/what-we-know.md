# What We Know About Minoan Linear A
## A Synthesis of Current Knowledge — April 2026

*This document synthesizes findings from 36 reference papers, the unified corpus (1,880 documents), Younger's Lexicon (1,463 word forms), and computational analysis.*

---

## The Script

Linear A is the writing system of Minoan Crete, used approximately **1800–1450 BCE**. It is a **logo-syllabary**: a combination of phonetic signs representing syllables (syllabograms) and picture-signs representing whole words or concepts (logograms/ideograms).

### Sign Inventory
- **178 simple signs** (independent graphic units) — Salgarella 2022
- **164 complex/composite signs** (ligatures of two or more simple signs) — Linear A only
- **47 fractional signs** (unique to Linear A, not found in Linear B)
- **~315 sign types with images** in this project's catalog
- **386 signs** in the structured data layer

A core group of ~90 simple signs is shared across all sites and with Linear B. Signs prefixed with "A" (e.g., A301, A363) are specific to Linear A with no Linear B equivalent — strong evidence that the Minoan language had **phonemes not present in Greek**.

### Script Origins
The script evolved from **Cretan Hieroglyphic** (CHS), a pictographic writing system used primarily in northern Crete. Manning (2009) identifies four transformation techniques:
1. **Reduction** to a single element of the CHS sign
2. **Sectioning** along the vertical axis
3. **Stick-figure simplification**
4. **Icon-on-stick composition**

Manning speculatively maps 53 CHS signs to their Linear A equivalents, of which 13 are confirmed by the CHIC corpus editors and 23 are well-supported.

The **"Arkhanes script"** (~15 seal stones, EM III/MM IA, ~2000 BCE) may be the common ancestor of both CHS and Linear A. Crucially, one sign group on these earliest seal stones reads **A-SA-SA-RA** — the same sequence found in the later libation formula. This suggests the ritual vocabulary may predate either script (Schoep 1999).

### Geographic and Temporal Distribution
- **Proto-Palatial (1900–1700 BCE):** Linear A and Cretan Hieroglyphic coexist. LA is dominant in southern/central Crete (Mesara plain: Phaistos, Haghia Triada). CHS is dominant in northern/eastern Crete (Knossos, Malia, Petras).
- **Neo-Palatial (1700–1450 BCE):** Linear A becomes the island-wide standard. CHS disappears.
- **~1450 BCE:** Linear A disappears. Linear B (writing Greek) replaces it, initially at Knossos only.
- **~1350 BCE:** Latest known Linear A inscription — a painted figurine from Poros Herakleiou.

Linear A has been found on **Crete** (dominant), **Thera** (Santorini), **Kea**, **Melos**, **Samothrace**, **Kythera**, **mainland Greece** (Mycenae, possibly Tiryns), **Miletos** (Anatolia), and possibly **Tel Lachish** and **Tel Haror** (Levant).

---

## The Corpus

### Scale
- **1,534 documents** with **7,574 signs** — RILA 2025 (the official count)
- **1,880 document records** in this project's unified corpus (merged from SigLA + lineara.xyz + hand-curated)
- **107 new documents** in the RILA Supplement 2025 (not yet fully incorporated)
- **773 documents** with images in our gallery

### Document Types
| Type | Count | Function |
|------|-------|----------|
| Tablets | ~489 | Administrative records: commodity lists, personnel, assessments |
| Nodules | ~913 | Clay lumps sealed around strings — authentication markers |
| Roundels | ~192 | Clay discs with seal impressions — receipts |
| Stone vessels | ~62 | Ritual libation tables — carry the libation formula |
| Clay vessels | ~63 | Scratched/painted marks on pottery |
| Metal objects | ~23 | Bronze/gold votive objects |
| Lames (bars) | ~18 | Thin clay bars for brief records |
| Other | ~120 | Graffiti, labels, miscellaneous |

~90% of documents are administrative. ~10% are ritual or other.

### Key Sites
| Site | Documents | Specialty |
|------|-----------|-----------|
| Haghia Triada (HT) | 373 | Largest administrative archive. Most of what we know about Minoan bookkeeping. |
| Khania (KH) | 213 | Second largest. Western Crete. Proves island-wide administration. |
| Phaistos (PH) | 63 | Major palace near HT. |
| Zakros (ZA) | 44 | Easternmost palace. Archive sealed by destruction ~1450 BCE. |
| Knossos (KN) | 31 | Largest palace. Mostly Linear B, but some LA survives. |
| Mallia (MA) | 20 | North coast palace. |
| Arkhanes (ARKH) | 10 | South of Knossos. Palatial and funerary contexts. |

**Missing from our corpus** (identified via RILA 2025 index): Petras (major administrative site), Iouktas (key ritual site with libation tables), Palaikastro, Thera, Samothrace, Poros Herakleiou, Mokhlos, Skoteino, Kalo Khoraphi.

---

## What We Can Read

### Secure Knowledge (arithmetic verification)

**ku-ro** = "total" (36 occurrences, HIGH confidence). Appears at the end of commodity lists. The number following ku-ro matches the arithmetic sum of preceding entries in **77% of tablets**. This is the single most securely identified word in Linear A.

**ki-ro** = "deficit / owed" (17 occurrences, HIGH confidence). Always appears after ku-ro with a smaller value. Represents the shortfall between expected and actual amounts.

**po-to-ku-ro** = "grand total" (3 occurrences, HIGH confidence). Compound of po-to + ku-ro. Sums multiple ku-ro subtotals on complex tablets.

**The numeral system** is well understood: vertical strokes = units, horizontal bars = tens, circles = hundreds. Matches Linear B exactly.

### The Accounting System

Minoan administration used an **assessment-based redistribution** system:
1. **Heading** (sa-ra₂, da-me, ka-pa, etc.) declares the transaction type
2. **Names + commodity + amount** — individual assessed entries
3. **ku-ro + total** — arithmetic sum
4. **ki-ro + deficit** — what is still owed
5. **po-to-ku-ro + grand total** — sum across sections

Commodities tracked: **GRA** (grain/barley), **VIN** (wine), **OLE** (oil), **FIC** (figs), **OLIV** (olives), **TELA** (textiles), **BOS** (cattle), **OVIS** (sheep), **CAP** (goats), **SUS** (pigs), *327 **AES** (bronze).

### The Libation Formula

The most studied multi-word phrase in Linear A, found on **stone offering vessels** across multiple sites. Standard form:

> **a-ta-i-*301-wa-ja** · u-na-ka-na-si · i-pi-na-ma · si-ru-te · **ja-sa-sa-ra-me** · u-na-ru-ka-na-ti · **i-da-ma-te**

Key terms:
- **ja-sa-sa-ra-me** — most likely Luwian *ishassara* + possessive *-me* = "My Lady" (a deity epithet). The Luwian connection is phonologically precise and morphologically transparent.
- **i-da-ma-te** — "Mother of Ida" or "Mother Ida" (i-da = Mt. Ida + ma-te = mother)
- **a-ta-i-*301-wa-ja** — the opening dedicatory phrase. Contains sign *301 (undeciphered). Manning speculatively identifies *301 = CHS #046 "engraving tool" with value 'phra'.
- **Sign *301** appears in 15+ word contexts beyond the formula (personal names, nodules), confirming it is a regular syllabogram for a phoneme Greek lacks.

The sequence **A-SA-SA-RA** appears on seal stones from ~2000 BCE (Arkhanes script), suggesting the ritual vocabulary **predates Linear A itself** and may have motivated the invention of writing on Crete (Schoep 1999).

### The Glossary

52 entries with confidence scores:
- **8 HIGH confidence** (arithmetic verification): ku-ro, ki-ro, po-to-ku-ro, sa-ra, da-me, pa-i-to (Phaistos), ku-do-ni (Kydonia), su-ki-ri-ta (Sybrita)
- **37 MEDIUM confidence** (distributional evidence): personal names, place names, transaction terms
- **5 LOW / 2 SPECULATIVE**: contested identifications

**Known corrections needed** (from Younger's Updates):
- PA-JA-RE is probably a personal name, not Phaistos (LB parallel is masculine name)
- PA-I-TO should be added as the Phaistos entry
- A-KA-RU should be reclassified as transaction heading, not personal name
- DU-PU₂-RE ("master/lord"), TA-JA (possibly "five"), and libation formula words need to be added

---

## The Morphology: What Kind of Language?

### Suffix System (6-8 productive suffixes)
| Suffix | Frequency | Function | Example |
|--------|-----------|----------|---------|
| -ja | 85 (5.8%) | Adjectival/ethnic; **marks persons** | pa-se-ja, sa-ra₂ |
| -ra | 59 (4.0%) | Nominal; **marks things** | ki-ki-ra-ja vs ku-ku-da-ra |
| -ro | 34 (2.3%) | Nominal (totals, administrative) | ku-ro, ki-ro |
| -na | 68 (4.6%) | Genitive/agentive | ki-re-ta-na |
| -te | 63 (4.3%) | Dative/locative case | a-di-ki-te, ta-na-te |
| -se | 42 (2.9%) | Instrumental/ablative? | pi-ta-ka-se |
| -ne | 42 (2.9%) | Dative plural? | da-ku-se-ne |
| -me | 8 | Possessive "my" | ja-sa-sa-ra-me |

### Key Grammatical Discovery: -ja (persons) vs -ra (things)
Schurr (1973) demonstrated that **-ja marks person-related derivations** while **-ra marks thing-related derivations**:
- ki-ro "deficit" → ki-ki-ra-**ja** "the missing **people**" (HT 85b)
- ku-da "allocation deficit" → ku-ku-da-**ra** "the missing **things**" (HT 117a)
- sa-ro → sa-ra₂ (= sa-ra-**ja**) "assessed **persons**"

### Suffix Chaining (Agglutination)
Linear A words can stack 4-5 suffixes:
- KI-TA → KI-TA-NA-SI-JA-SE (root + genitive + ? + adjectival + instrumental)
- DA-KU → DA-KU-SE-NE → DA-KU-SE-NE-TI
- U-NA → U-NA-KA → U-NA-KA-NA → U-NA-KA-NA-SI

This **progressive suffix stacking without stem modification** is the hallmark of agglutinative morphology.

### Reduplication = Plural
- ki-ro (singular: deficit) → **ki-ki**-ra-ja (plural: the missing ones)
- ku-da (singular) → **ku-ku**-da-ra (plural)
- sa-ra → sa-ra-ra (with additional -ra)
- qa-qa-ru, qa-qa-da (reduplicated forms in the lexicon)

---

## Testing the Language Hypotheses

### Can any be disproved?

**Semitic: SUBSTANTIALLY RULED OUT**
- No productive prefixation (Semitic requires verb prefixes ya-, ta-, a-)
- No root-and-pattern morphology (Semitic trilateral roots with vowel alternation)
- Case suffixes are CV-syllables, not single-vowel Akkadian markers
- Suffix chaining is fundamentally non-Semitic

**Greek: ACTIVELY CONTRADICTED**
- Morphology is agglutinative (suffix chains 4-5 deep), not fusional like Greek
- 6-8 case suffixes exceed Greek's 5 cases
- No articles found (Greek's diagnostic feature)
- No productive bare -o nominative
- Core administrative vocabulary has 0-2 Greek etymologies out of ~10 terms
- ja-sa-sa-ra-me = Luwian, not Greek
- LA has signs with no LB equivalent (*301, *188) → non-Greek phonemes

**Hurrian: MORPHOLOGICALLY PLAUSIBLE, LEXICALLY UNSUPPORTED**
- Agglutinative suffix chaining: matches ✅
- No prefixes: matches ✅
- 6-8 case suffixes: matches Hurrian's 8-9 ✅
- But: ku-ro, ki-ro, sa-ra have NO Hurrian cognates ❌
- The d/t dental distinction in the sign grid contradicts Hurrian phonology (which doesn't distinguish them) ⚠️
- Libation formula: Luwian reading more parsimonious than Hurrian prayer reading ❌

**Unknown Agglutinative Language: MOST PARSIMONIOUS**
- Morphology: agglutinative with suffix chaining ✅
- Vocabulary: no matches to any proposed source language ✅
- Luwian religious borrowings: explains ja-sa-sa-ra-me without requiring the whole language to be Luwian ✅
- Substrate place names surviving into Greek: expected ✅

### The Script-Language Disconnect

A critical finding: **70% of Linear B signs have Linear A antecedents** (Steele), but **less than 1% of Linear A words have Linear B parallels** (11 out of ~1,463 word forms in Younger's Lexicon). The scripts are genetically related but the languages are not. This is exactly what we'd expect if Linear B was adapted from Linear A to write a completely different language (Greek), just as the Latin alphabet was adapted for Turkish, Finnish, Vietnamese, and other unrelated languages.

The 11 words with LB parallels are mostly **personal names and place names** — exactly the category of words that survives across language changes (substrate vocabulary).

### The Emerging Picture

The Minoan language is most likely an **unknown agglutinative language** — possibly related to Hurrian-Urartian at a deep level, possibly an isolate — with **Anatolian/Luwian loanwords in its religious register**. It has a suffix-based case system, no prefixes, reduplication for plural, and a person/thing distinction in derivational morphology. Its phonological system included sounds not present in Greek (evidenced by signs like *301 with no Linear B equivalent).

---

## What Would Change This

1. **A bilingual inscription** — Linear A + any known language would be decisive
2. **The RILA Supplement's 107 new documents** — larger corpus enables deeper statistical analysis
3. **New archaeological discoveries** — particularly at ritual sites; a longer text; a bilingual
4. **Computational cross-script analysis** — AI-powered visual similarity across writing systems
5. **The Eteocretan inscriptions** — Archaic-period texts in Greek alphabet that may preserve the Minoan language; if connected to Linear A, could provide the key

---

## References

### Core Scholarly Sources
- Salgarella, E. "Linear A" — Oxford Classical Dictionary (2022)
- Salgarella, E. & Castellan, S. "SigLA" — Grapholinguistics in the 21st Century (2021)
- Younger, J.G. *Linear A Lexicon* (2008–2024)
- Younger, J.G. *Linear A: Updates* (2007–2024)
- Melena, J.L. "Mycenaean Writing" — Companion to Linear B (2014)
- Steele, P.M. "Other Pre-alphabetic Scripts" (~2018)
- Manning, M.B. "Genesis of Linear A" (2009)
- Schurr, D. "Linear A KI.KI.RA.JA" — Kadmos 12 (1973)
- Schoep, I. "Origins of Writing and Administration on Crete" — Oxford J. Archaeology (1999)
- Bennet, J. "Now You See It; Now You Don't!" (2008)
- Montecchi, B. "Linear A Banqueting Lists?" — Kadmos 51 (2012)
- Van Soesbergen, P.G. *The Decipherment of Minoan Linear A*, Vols. I–II (2022)
- Del Freo, M. & Zurbach, J. *RILA Supplément 1* (2025) — index only

### This Project
- Unified corpus: 1,880 documents from SigLA + lineara.xyz + hand-curated
- Sign catalog: 386 signs in data, 315 with images
- Glossary: 52 entries with confidence scores
- 14 reproducible benchmarks
- Document gallery: 773 documents with 5,715 images
- Interactive site map with real GeoJSON coastline data
