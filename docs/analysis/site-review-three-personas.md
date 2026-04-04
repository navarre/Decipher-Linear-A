# Site Review: Three Perspectives

## Review Date: April 2026
## Site: https://navarre.github.io/minoan-linear-a/

---

## Persona 1: The Curious Visitor
*"I saw a documentary about Minoan civilization and googled Linear A. I want to know: what is it, can we read it, and why should I care?"*

### What they see:
**Homepage hero — the prayer.** This is excellent. A 3,500-year-old prayer partially translated, with a mysterious red sign blocking the rest. This is the hook that keeps someone scrolling. The three cards below (The Undeciphered Script, What We Know, 3,500 Years of Silence) tell the story in plain language. "The prayer on the stone tables is the closest we've come to hearing their voice" — that's the emotional payoff.

**The map (sites.html)** — beautiful dark-mode SVG with real coastline data. Glowing dots at each site. Click to see what was found there. This is the museum-iPad experience we wanted.

**The document gallery** — they can click on actual tablet drawings and see individual signs. The parchment-background fix makes the images visible.

### What's missing for this persona:
1. **No "What is Linear A?" explainer page.** The homepage dives into findings before explaining basics. A visitor who doesn't know what a syllabogram is will be lost by paragraph 3.
2. **No timeline visualization.** The story of "born at Arkhanes → peak at Haghia Triada → died at 1450 BCE → survived as Eteocretan" should be a visual timeline, not buried in analysis docs.
3. **No images of the ACTUAL artifacts.** We have drawings but no photos of the real objects — the gold ring, the libation tables, the seal stones. A photo of the Arkhanes prism seal with a caption would be more powerful than any amount of text.
4. **No "Where to see Linear A" page.** A visitor who's now fascinated wants to go see these objects. Museum listings with exhibit locations would be high-value content.
5. **The Explore/Research toggle** works but isn't labeled clearly enough. A visitor might not notice it or understand what it does.
6. **The findings section** (Zipf's law, Shannon entropy, Jaccard similarity) is impenetrable for this audience. "Word frequencies follow Zipf's law (exponent 1.103, R²=0.901)" means nothing to a normal person. This should say "We've proven mathematically that this is a real language, not a code or decoration."
7. **No mention of the Phaistos Disc.** Every visitor will ask about it. We should mention it briefly and explain why it's NOT Linear A (probably).

### Grade for this persona: B-
The hook is great, the map is great, the gallery works. But the site still reads like a research project that happens to have a nice front page, not like a resource designed for curious visitors. The gap between the beautiful hero and the dense findings section is jarring.

---

## Persona 2: The Museum Docent / Educator
*"I work at the Heraklion Archaeological Museum (or the British Museum, or any museum with Minoan artifacts). I have a history degree. I can explain the Minoans to visitors, but I've never done original research on Linear A. I want to check whether this site is useful for my work."*

### What they see:
**Credibility markers:** The site cites Salgarella, Younger, Melena, Steele, GORILA, RILA 2025. These are the right names. A docent who knows the field will recognize them immediately.

**The corpus browser (browse.html)** — searchable, filterable. A docent could type in a document ID from their museum's collection and see what we know about it.

**The sign explorer** — visual grid of signs, clickable. Useful for answering visitor questions about "what does this sign mean?"

**The libation formula** — docents at Heraklion are asked about the stone offering tables constantly. Having a clear, citable explanation with "My Lady, Mother of Ida" is immediately useful for tours.

### What's missing for this persona:
1. **No museum integration.** The site doesn't list which artifacts are where. A docent at Chania wants to know "which of these documents are in MY museum?" We should have a museum field on every document record.
2. **No printable/shareable materials.** The ten-findings handout is a good start, but it's a markdown file, not a designed PDF. Docents need something they can actually print and hand to visitors.
3. **No "How to explain Linear A to visitors" guide.** A simple FAQ: "Is it related to Linear B?" "Can we read it?" "What language is it?" "Why hasn't it been deciphered?" — with short, accurate answers a docent can memorize.
4. **The terminology page** exists but is buried. For a docent, this should be more prominent — it's their reference sheet.
5. **No images of objects in museum context.** Our gallery has inscription drawings but no photos showing what the actual tablet/stone vessel/seal looks like as a physical object in a display case.
6. **The old nav problem.** Some pages still have the old `<nav>` element that the sidebar is supposed to hide. If the JS fails to load, the page looks broken.
7. **Attribution is unclear.** "Created by Matt Navarre" with no institutional affiliation. A docent will wonder: is this a university project? A private hobby? A funded research program? The site should be transparent about what it is.

### Grade for this persona: B
The content is solid and the references are right. But the site doesn't actively serve docents — it serves researchers who happen to also be docents. The museum connection is the biggest gap.

---

## Persona 3: The Expert Scholar
*"I'm Dr. [Name], I work on Aegean scripts. Someone sent me this URL. I'll give it 90 seconds before I decide if it's worth my time."*

### What they see in 90 seconds:
**First 5 seconds:** "Linear A Research Project" — OK, another one. The prayer hero is dramatic but scholars are skeptical of dramatic presentations. The *301 in red is a bit flashy. But the transliterations are correct and the Luwian ishassara connection is mainstream scholarship, not fringe. Passes the initial smell test.

**Next 15 seconds:** Scan the three cards. "not Greek, not Semitic, agglutinative language isolate with religious borrowings from Luwian" — this is a defensible position, not a crank decipherment claim. "1,534 inscriptions, 7,574 signs (RILA 2025)" — correct numbers, current source. "1,880 document records" — larger than expected, interesting.

**Next 30 seconds:** Scroll to Key Findings. "Zipf's law (exponent 1.103, R²=0.901)" — real statistics, not hand-waving. "52 words read" with confidence scores — responsible approach. "6-8 case suffixes" — aligns with mainstream analysis.

**Next 40 seconds:** Project Goals. "Incorporate RILA Supplement 2025" — they know about the latest publication. "Review by domain expert (Dr. Salgarella contacted)" — they're trying to get expert review, good. "Decipherment: The Goal" at the bottom with realistic milestones — not claiming to have deciphered it, which is the #1 red flag for crankery.

### What passes the smell test:
- Correct terminology throughout (syllabogram, logogram, libation formula, GORILA)
- Current references (RILA 2025, Salgarella 2022, Younger 2024)
- Confidence scores on everything
- Honest about what's unknown
- No claim of decipherment
- Open source, reproducible data
- Computational approach with real statistics

### What would raise red flags:
1. **"Probable Language Isolate" with a bar chart showing 0.774.** Where does this number come from? What model produced it? A scholar will immediately ask "what's the methodology?" and if they can't find it, they'll assume it's made up. This bar chart needs a source or it should be removed.
2. **"Productive prefix a- dominates 8 of 10 largest word families."** Our own morphological analysis says "no productive prefixes." This contradicts our deeper findings. The homepage hasn't been updated.
3. **"No verb morphology detected in administrative texts."** But we identified u-na-ka-na-si as a verb in the libation formula analysis. Another contradiction.
4. **The old findings section** has stale data that predates the deep analysis. The "near-zero vocabulary overlap between sites (Jaccard 0.000-0.016)" is a specific claim that needs sourcing.
5. **No methodology page.** How was the corpus assembled? How were confidence scores assigned? What were the inclusion/exclusion criteria? A scholar needs to evaluate the methodology before trusting the results.
6. **No bibliography page.** The 36 references we've read are not listed anywhere on the site. This is a basic requirement for any scholarly resource.
7. **No "About" page** explaining who Matt Navarre is, what his background is, and why he's qualified to do this work. This doesn't need to be a CV — it can be honest: "I'm not an academic. I live on Crete. I built this because the data should be open and accessible."
8. **Analysis documents are in the repo but not on the site.** The hypothesis testing, morphology sketch, *301 analysis, libation formula analysis — these are the most impressive work in the project, and they're invisible unless someone browses the GitHub repo.
9. **The site still has some broken pages.** The old signs.html exists alongside sign-explorer.html. Some pages may still have the old nav. This looks unfinished.
10. **"Dr. Salgarella contacted"** — has she actually responded? If not, this claim is aspirational, not factual.

### Grade for this persona: C+
The content passes the smell test — no crankery, correct terminology, current references. But the presentation is uneven: impressive hero, then stale/contradictory findings, then no methodology or bibliography. A scholar would see potential but wouldn't yet trust it enough to cite. The analysis docs in the repo are strong but invisible. The biggest gap: no methodology page and no bibliography.

---

## Summary of Gaps by Priority

### Critical (must fix before Monday):
1. **Fix contradictions on homepage** — "productive prefix a-" vs "no prefixes"; "no verb morphology" vs u-na-ka-na-si
2. **The 0.774 isolate bar chart** — either source it or remove it
3. **Remove or update stale findings** that predate the deep analysis

### High (should fix soon):
4. **Add bibliography page** — list all 36 references, linked to the analysis that uses them
5. **Add methodology/about page** — who we are, how the corpus was built, how confidence scores work
6. **Surface the analysis documents** — hypothesis testing, morphology, *301, libation formula should be HTML pages, not buried markdown files
7. **Add museum listings** — which artifacts are where, with exhibit room numbers
8. **Fix remaining old nav/broken page issues**

### Medium (would improve the experience):
9. **Add "What is Linear A?" explainer** for first-time visitors
10. **Add timeline visualization** — Arkhanes → LA → LB → Eteocretan → today
11. **Add photo references** to actual artifacts (link to museum websites)
12. **Add visitor FAQ** for docents
13. **Clean up the Explore/Research toggle** — make it more obvious
14. **Rewrite findings section** in plain language for Explore mode

### Nice to have:
15. **Printable PDF of ten findings**
16. **Phaistos Disc explainer** (not LA but everyone asks)
17. **"Where to see Linear A" museum guide**
