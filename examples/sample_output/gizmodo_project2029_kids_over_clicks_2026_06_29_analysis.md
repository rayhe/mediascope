# Gizmodo: "Democrats Want to Do Their Own Project 2025. First Up: Kicking Kids Offline"

**Source:** Gizmodo
**Date:** 2026-06-29
**URL:** https://gizmodo.com/democrats-want-to-do-their-own-project-2025-first-up-kicking-kids-offline-2000779191
**Subject:** Project 2029's "Kids Over Clicks" policy proposal / children's online safety legislation / social media regulation

## Manual Analysis

### Entity Extraction
- **Project 2029** — small liberal policy group (primary subject, consistently framed as minor/misguided)
- **Meta** — implied target of child safety regulation (mentioned indirectly via "social media," "surveillance advertising business model," "Facebook"; not named directly)
- **Cory Booker** — Democratic senator, supporter of proposal (framed as inconsistent centrist)
- **Jonathan Haidt** — *The Anxious Generation* author (mentioned neutrally as supporter)
- **KIDS Act** — legislation context (same day as House vote, not mentioned in article)
- **Trump/Kushner** — political context (extensive tangent occupying ~25% of article)
- **Fox News** — cited for polling data

### Tone & Framing Assessment
**Overall tone:** Sardonic / dismissive-editorial
**Stance on child safety legislation:** Skeptical — frames it as politically misguided rather than addressing the policy substance

### Key Framing Techniques

1. **Topic displacement / political reframing** — The article nominally covers a tech policy proposal but spends ~40% of its text on unrelated political commentary (Trump, Iran bombing, Kushner's equity deals). The child safety policy becomes a vehicle for criticizing Democratic Party strategy, not for analyzing tech regulation.

2. **Editorial deflation (concession-then-dismissal):**
   - "Noble efforts, indeed, but maybe not the most pressing concern" — classic build-up-then-puncture, conceding the proposal's merit only to dismiss it relative to other priorities.

3. **Credibility undermining via tangent chain:**
   - Booker supports proposal → Booker voted for Trump nominees → Charles Kushner ambassador → Jared Kushner → Iran negotiations → sovereign wealth fund solicitation. This guilt-by-association chain spans 3 paragraphs and has zero relevance to child safety policy.

4. **Size minimization as delegitimization:**
   - "the small liberal group" — size modifier used to pre-shrink the proposal's significance before examining it
   - "a relatively small political group" — repeated in closing

5. **Ironic quotation marks:**
   - "additive apps" — quotes the proposal's terminology without endorsing it
   - "cosplaying as licensed professionals" — quotes with implicit amusement
   - "not a silver bullet" — quotes the concession to amplify it

6. **Loaded language (political register):**
   - "hucksters" — pejorative for political officials
   - "carved up" / "robbed blind" — hyperbolic characterizations
   - "carved up and robbed blind" — compound loaded phrasing
   - "talks a big game" — dismissive idiom applied to Booker

7. **Outsourced intensity:**
   - "A dismantling of the surveillance advertising business model that profits off targeting vulnerable teens" — author quotes the proposal's most inflammatory language verbatim, letting it read as extreme without taking editorial ownership

8. **Effectiveness pre-emption:**
   - "wouldn't even achieve its stated goals, given the existence of VPNs" — VPN argument presented as dispositive when it's actually debated (the article notes the proposal itself addresses this comparison to fake IDs)

### What's NOT in the article
- No mention of the KIDS Act House vote that happened THE SAME DAY (267-117, bipartisan)
- No engagement with the NYU/Northeastern/Heat Initiative study showing 50-73% failure rates for child safety features (published same weekend)
- No industry perspective from Meta, Snap, or TikTok
- No comparison to Australian implementation data beyond one BMJ stat
- No cost-benefit analysis of the proposal itself

## Toolkit Analysis (automated)

### Framing Devices Detected (9)
| Device | Evidence | Assessment |
|--------|----------|------------|
| ironic_quotation | "additive apps" | ✅ Correct |
| ironic_quotation | "cosplaying as licensed professionals" | ✅ Correct |
| confession_framing | "The group acknowledges that" | ⚠️ Borderline — this is straightforward reporting of the proposal's own caveat |
| ironic_quotation | "not a silver bullet" | ✅ Correct |
| loaded_language | "predators" | ⚠️ False positive — "child predators" is standard terminology, not loaded in this regulatory context |
| outsourced_intensity | "A dismantling of the surveillance advertising..." | ✅ Correct — excellent catch |
| editorial_deflation | "Noble efforts, indeed, but" | ✅ Correct (NEW — pattern added this iteration) |
| geopolitical_regulatory_pressure | "sovereign" | ❌ False positive — refers to sovereign wealth funds in a political tangent, not tech regulatory pressure |
| sovereignty_framing | "American public" | ❌ False positive — standard phrase in political commentary |

### Manual-vs-Toolkit Gap Analysis

**Detected correctly (5/9):** ironic_quotation ×3, outsourced_intensity, editorial_deflation
**Borderline (2/9):** confession_framing, loaded_language ("predators")
**False positives (2/9):** geopolitical_regulatory_pressure, sovereignty_framing

**Major gaps — NOT detected:**
1. **Topic displacement / political reframing** — ~40% of article is political commentary unrelated to the nominal tech policy subject. No device type exists for this pattern.
2. **Credibility undermining via tangent chain** — The Booker→Kushner→Iran chain is a powerful rhetorical move with no matching device.
3. **Political loaded language** — "hucksters", "carved up", "robbed blind", "talks a big game" not detected as loaded_language. (FIXED: added 22 political rhetoric terms to EMOTIONAL_LANGUAGE this iteration.)
4. **Size minimization** — "the small liberal group" uses size as a delegitimization modifier; no pattern exists.

### Improvements Made This Iteration

1. **editorial_deflation**: Added concession-then-dismissal patterns:
   - `"Noble/Admirable/Good/Fine X, indeed/sure/of course, but"` — catches the "Noble efforts, indeed, but" construction
   - `"That may be true/fair/right, but"` — catches explicit concession pivots
   - 8 new tests in TestConcessionThenDismissal class

2. **EMOTIONAL_LANGUAGE (loaded_language)**: Added 32 political rhetoric terms:
   - `hucksters`, `huckster`, `robbed blind`, `robbing blind`, `carved up`, `carving up`
   - `grifter`, `grifters`, `grift`, `con man`, `con men`, `con artist`
   - `shakedown`, `racket`, `racketeer`, `swindler`, `swindled`
   - `charlatans`, `charlatan`, `snake oil`, `snake-oil`
   - `peddling`, `peddle`, `duped`, `duping`, `bamboozled`
   - `fleeced`, `fleecing`, `looted`, `looting`, `plundered`, `plundering`

### Remaining Toolkit Gaps (future work)
- **Topic displacement detection** — would require measuring topic coherence across paragraphs
- **Association chain analysis** — detecting guilt-by-association rhetorical constructions
- **Size/significance minimization** — "small group", "tiny startup", "niche" as delegitimization modifiers
- **geopolitical_regulatory_pressure false positive** — "sovereign" in non-regulatory context triggers incorrectly

## Context Notes

This article is notable for how it handles the child safety regulation topic. Published the same day as the KIDS Act House vote (267-117), it ignores the legislative milestone entirely and instead uses the smaller Project 2029 proposal as a vehicle for criticizing Democratic Party political strategy. The substantive policy questions (do child safety features work? what would effective regulation look like?) are never engaged.

This creates a framing asymmetry worth tracking: when the same-day legislative context would strengthen the article's subject (bipartisan support, parallel Senate action), omitting that context is itself a framing choice. The toolkit has no mechanism to detect significant omissions.

### Sources
- Gizmodo article: https://gizmodo.com/democrats-want-to-do-their-own-project-2025-first-up-kicking-kids-offline-2000779191
- Same-day context: Reuters, "US House passes youth online safety legislation" (2026-06-29)
- Same-day context: USA Today, "House passes bill to protect kids online" (2026-06-29)
