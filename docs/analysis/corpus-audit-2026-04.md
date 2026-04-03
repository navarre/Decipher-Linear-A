# Corpus Audit — April 2026

Cross-referencing project data against Younger's Lexicon (updated May 2024), Younger's Updates (updated April 2024), and Salgarella's OCD article (2022).

---

## Sign Catalog

**Our signs.json: 386 signs** (164 syllabograms, 117 logograms, 64 ligatures, 16 other, 14 fractions, 6 compound logograms, 5 numerals)

**Salgarella (OCD 2022): 389 signs** (178 simple, 164 complex/composite, 47 fractional)

**Gap: 3 signs.** The data layer is nearly complete. However:
- Our classification is by function; Salgarella's is by graphic form. We need both axes.
- Our image catalog (315 images in docs/images/signs/) is missing **71 signs** that exist in signs.json — the display layer needs to catch up.
- We have 14 fractions; Salgarella has 47. Our fraction coverage is poor.

### Logogram assignments missing from signs.json:
| Sign | Younger's reading | Our status |
|------|-------------------|------------|
| *327 | AES (bronze) | Present but unlabeled |
| *363 | SO (logogram) | Stub entry, no reading |
| *314 | PU3 | "?314" with no reading |

---

## Glossary

### Critical error found:
**PA-JA-RE is probably NOT Phaistos.** We classify it as a HIGH confidence place name. Younger's Linear B parallel pa-ja-ro (KN As 1519.6) is a masculine personal name. The actual Phaistos spelling is PA-I-TO (confirmed in both LA and LB). Recommend: downgrade PA-JA-RE to MEDIUM as "personal name or place name" and add PA-I-TO as the Phaistos entry.

### Reclassifications needed:
| Word | Our classification | Younger's classification | Action |
|------|-------------------|-------------------------|--------|
| PA-JA-RE | Phaistos (place, HIGH) | cf. pa-ja-ro (personal name in LB) | Downgrade, reclassify |
| A-KA-RU | personal name (MEDIUM) | heading / transaction term | Reclassify |
| KU-NI-SU | emmer wheat (SPECULATIVE) | first name in a list | Reclassify to name |

### Missing from glossary (should be added):
| Word | Meaning | Source |
|------|---------|--------|
| PA-I-TO | Phaistos (place name) | Younger, confirmed in LA and LB |
| DU-PU2-RE | master / lord | Younger, libation formula word |
| I-PI-NA-MA | dedication? (libation formula word 6) | Younger |
| SI-RU-TE | libation formula word 7 | Younger |
| U-NA-KA-NA-SI | verb (libation formula word 5) | Younger |
| DI-DE-RU | personal name (LB parallel di-de-ro) | Younger |
| DA-TA-RE | heading / personal name | Younger |
| TA-JA | possibly = "five" (numeral!) | Younger |
| KI-RI-SI | possible verbal singular of ki-ro | Younger's Updates |
| KI-KI-RA-JA | "the missing ones" (ki-ro derivative) | Schurr 1973 |

### Missing data types:
- No fraction values documented (Younger identifies D = 1/5, J = possibly 1/2)
- No logogram entries (*327 AES bronze, *303 grain)
- No sign value corrections documented (*363 = SO, *314 = PU3)

---

## Corpus Data Quality

### Corrections from Younger's Updates (2007–2024):
These specific tablet reading corrections should be verified against our corpus_structured.json:

| Correction | Date | Details |
|-----------|------|---------|
| HT 30.4-.5 | Jan 2019 | Should be 1 BOS not 4 |
| HT 97, HT 119 | Jan 2019 | Should show *327 AES (bronze) |
| KN Zc 6: NI-TI-NU → NI-JA-NU | Dec 2016 | Typo correction |
| KH Wa 1001g: RO+RO → DA+RO | Nov 2016 | Wrong logogram |
| HT 117.a5 | Jan 2015 | TE-JA-RE and NA-DA-RE order switched |
| HT 26a.1, b.1 | Nov 2010 | 406VAS+KE not 407VAS+A |
| HT 34 | Aug 2010 | Should NOT have SA-VINa |
| HT 23, 24 | Aug 2010 | Should have SI+ME |
| HT 26b.3, 127b.5,6 | Aug 2010 | KI+MU not KU+MU |
| SA-*315 on HT 9, 17, 19, 42 | May 2009 | Should be SA-RO |
| PO Zg → PO Zc | Oct 2014 | Category is "painted" not "graffito" |
| GRA+PA | Oct 2014 | Should be *574 not *577 or *547 |
| KN Wa 40 provenance | Dec 2017 | South-West House not South House |
| HT 115a.1-2 | Mar 2010 | RI-TA-MA-NU-WI not RI-SU-MA- |

**Status:** These corrections have not been audited against our data yet. Assigned to Verifier.

---

## Summary of Actions

### Immediate (Builder):
1. ~~Fix PA-JA-RE classification~~ → needs verification first
2. Add PA-I-TO, DU-PU2-RE, and libation formula words to glossary
3. Update *327, *363, *314 readings in signs.json
4. Add ki-ri-si and ki-ki-ra-ja to ki-ro entry

### Verification needed (Clawdia):
1. Audit all 15 tablet corrections above against corpus_structured.json
2. Verify PA-JA-RE reclassification — check all occurrences in corpus
3. Verify TA-JA = "five" claim
4. Three-way sign count comparison (our data vs Salgarella vs lineara.xyz)
