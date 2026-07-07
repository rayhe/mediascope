# MIT Technology Review: "AI could keep us dependent on natural gas for decades to come"

## Article Metadata
- **Publication:** MIT Technology Review
- **Series:** "Power Hungry" (investigative series on AI's energy footprint)
- **Subject:** Meta's planned 2.3-GW natural gas power complex in Richland Parish, Louisiana
- **Date:** May 2026
- **Word count:** ~3,400
- **Article file:** `mit_tr_meta_louisiana_natural_gas_2026_05_article.txt`

---

## Toolkit vs Manual Assessment

### 1. Entity Detection

| Cluster | Toolkit (pre-fix) | Toolkit (post-fix) | Manual Assessment |
|---|---|---|---|
| Meta | 16 | 16 | ✅ Accurate — Meta is the primary subject |
| Energy/Utilities | 0 | 18 | ✅ Fixed — Entergy (~15 mentions) was entirely invisible |
| Energy Research/Regulatory | 0 | 11 | ✅ Fixed — EPRI, EIA, LPSC, Rhodium Group now detected |
| Environmental Advocacy | 0 | 5 | ✅ Fixed — Alliance for Affordable Energy, SELC detected |
| Academic/Research | 8 | 8 | ✅ Accurate — Harvard Law, UC San Diego, Carnegie Mellon |
| US Congress | 3 | 3 | ✅ Accurate — Sheldon Whitehouse references |
| Google | 1 | 1 | ✅ Accurate — brief Google comparison mention |
| Chinese AI | 1 | 1 | ⚠️ Marginal — single mention context |

**Gap analysis:** Before adding the Energy/Utilities, Energy Research/Regulatory, and Environmental Advocacy clusters, the toolkit missed 34 entity mentions (51% of all entities in the article). This was the single largest detection gap found in any article to date. The article's primary tension — Big Tech vs energy utilities and environmental groups — was invisible to the toolkit. The fix elevated Entergy to second-most-mentioned entity, correctly reflecting the article's structure.

**Remaining gap:** None significant. The toolkit now captures all major entities.

### 2. Topic Classification

| Topic | Toolkit (pre-fix) | Toolkit (post-fix) | Manual Assessment |
|---|---|---|---|
| energy_climate | N/A | 1.0000 (36 kw) | ✅ Correct — this is fundamentally an energy/climate article |
| infrastructure_impact | 0.5111 | 0.5111 (10 kw) | ✅ Accurate secondary topic (data center construction) |
| corporate_strategy | 0.4400 | 0.4400 (3 kw) | ✅ Accurate tertiary topic (Meta's strategic energy plans) |
| product_launch | 0.0696 | 0.0696 | ⚠️ Marginal — no product launches in this article |
| ai_development | 0.0403 | 0.0403 | ⚠️ Marginal — AI mentioned as driver but not the topic |

**Gap analysis:** Without the `energy_climate` topic, the toolkit classified this as primarily an infrastructure article. While infrastructure is a valid secondary topic, the article's core argument — that AI-driven natural gas dependency locks in decades of fossil fuel use — is fundamentally about energy policy and climate consequences. The `infrastructure_impact` topic only captures the "building stuff" dimension, not the "burning stuff" dimension.

**Design note:** `energy_climate` and `infrastructure_impact` are complementary, not overlapping. An article about a data center's water usage or community opposition is `infrastructure_impact`. An article about a data center's carbon footprint and fossil fuel lock-in is `energy_climate`. This article is both, correctly scoring high on both topics.

### 3. Sentiment Analysis

| Dimension | Toolkit (pre-fix) | Toolkit (post-fix) | Manual Assessment |
|---|---|---|---|
| overall_tone | 0.6427 | 0.6427 | ⚠️ Slightly high — article has more critical framing than neutral |
| agency_attribution | 0.0000 | 0.7778 | ✅ Fixed — Meta has strong agency (planning, building, choosing) |
| speculative_language | 0.3659 | 0.3659 | ✅ Accurate — "could keep us," future projections throughout |
| headline_body_alignment | 0.3613 | 0.3613 | ⚠️ Low alignment is a genuine finding — headline makes a broad claim about "keeping us dependent," body is more nuanced about specific Louisiana dynamics |
| emotional_intensity | 0.082 | 0.082 | ✅ Accurate — measured, investigative tone |

**Agency fix root cause:** The `_measure_agency` function counted active verbs ("announced," "committed to") and active-negative verbs ("forcing," "requiring"), and when they balanced, agency scored 0.0. The fix added ~20 infrastructure/investment active verbs ("plans to build," "aims to," "will fund," etc.) that are unambiguously agentic. Post-fix score of 0.7778 correctly reflects Meta as the primary agent in the article — the company chose Louisiana, negotiated with Entergy, planned the facility, etc.

**Remaining gap:** `overall_tone` at 0.6427 (moderately negative) may be slightly generous. The article systematically frames natural gas dependency as a problem, uses "lock-in" language, and leads with environmental/ratepayer harm. A manual assessment would score this closer to 0.55-0.60.

### 4. Source Extraction

| Source | Toolkit (pre-fix) | Toolkit (post-fix) | Manual Assessment |
|---|---|---|---|
| David Victor | ✅ Named | ✅ Named | UC San Diego energy policy expert |
| Greg Buppert | ✅ Named | ✅ Named | Southern Environmental Law Center attorney |
| David Porter | ✅ Named | ✅ Named | EPRI VP of integrated grid |
| Costa Samaras | ✅ Named | ✅ Named | Carnegie Mellon, Scott Institute for Energy Innovation |
| Paul Arbaje | ✅ Named | ✅ Named | Meta spokesperson |
| Logan Burke | ✅ Named | ✅ Named | Alliance for Affordable Energy executive director |
| Rhodium Group | ✅ Named | ✅ Named | Research org, cited via report |
| Tyler Norris | "Norris" only | "Norris" only | ⚠️ Single-name — Pattern 5b captured surname from "Norris says" |
| Governor Jeff Landry | "Governor Jeff" | ✅ "Governor Jeff Landry" | ✅ Fixed — titled pattern now captures full name |
| Entergy | Not detected | ✅ Organizational | ✅ Fixed — "Entergy acknowledged" correctly tagged |
| Meta | Not detected | ✅ Organizational | ✅ Fixed — "Meta said in a statement" correctly tagged |
| **FALSE POSITIVES** |
| "Law School" | ❌ False positive | ✅ Filtered | Was: "Harvard Law School" → truncated to "Law School" |
| "Governor Jeff" | ❌ Truncated | ✅ Now "Governor Jeff Landry" | Was: title treated as first name |
| "Affordable Energy" | ❌ Partial org | ✅ Filtered | Was: "Alliance for Affordable Energy" → truncated |
| "the energy source" | ❌ False anonymous | ✅ Filtered | Was: "said the energy source was" matched anonymous pattern |
| "School" | ❌ False single-name | ✅ Filtered | Was: "School argued" at sentence start |

**Fixes applied:**
1. Added `Governor`, `Senator`, `Representative`, etc. to `_NAME_STOP_FIRST_WORDS` — prevents titles from matching as first names
2. Added Pattern 0/0b for titled sources — `[Title] [First] [Last]` captures full three-word names
3. Added `Law School`, `Affordable Energy`, `Concerned Scientists` to `_NAME_STOP_NAMES` — filters partial org names
4. Added non-journalistic "source" filter — `energy source`, `data source`, `power source`, etc. rejected from anonymous detection
5. Added `School`, `University`, `College`, etc. to `_SINGLE_NAME_ORG_STOPS` — prevents institutional nouns from matching as sources
6. Added `Entergy`, `Duke Energy`, `Dominion`, `Eversource` to `_SINGLE_NAME_ORG_STOPS` and `entergy` etc. to `_KNOWN_ORGS` — enables organizational source detection

**Remaining gaps:**
- Tyler Norris appears only as "Norris" — the full name "Tyler Norris" appears earlier in the text without a direct attribution verb nearby. Pattern 5b (single-name) captured the surname. This is cosmetic, not a coverage gap.
- Senator Sheldon Whitehouse is mentioned in context of "a letter from Senator Sheldon Whitehouse" — no attribution verb attached. He's referenced as a source of a document, not as someone who "said" or "told." This is an edge case where the current verb-based extraction model doesn't capture document-attributed sources.

### 5. Framing Devices

Not analyzed in this iteration — `detect_framing_devices()` API needs investigation of its actual signature and return format. Deferred to a future Type D (toolkit quality) iteration.

---

## Summary of Code Changes

### New Entity Clusters (entities.py)
- `Energy/Utilities` — 15+ aliases for major US utilities (Entergy, Duke Energy, Southern Company, etc.)
- `Energy Research/Regulatory` — 12+ aliases for energy research and regulatory bodies (EPRI, EIA, LPSC, FERC, etc.)
- `Environmental Advocacy` — 10+ aliases for environmental organizations (Alliance for Affordable Energy, SELC, Sierra Club, etc.)

### New Topic (topics.py)
- `energy_climate` — ~50 keywords covering fossil fuels, carbon emissions, renewables, climate policy, ratepayer dynamics

### Agency Fix (sentiment.py)
- Added ~20 infrastructure/investment active verbs to `ACTIVE_FRAMING` list in `_measure_agency`

### Source Extraction Fixes (sources.py)
- Added Pattern 0/0b: Titled source extraction (`Governor Jeff Landry`, `Senator Sheldon Whitehouse`)
- Added title words to `_NAME_STOP_FIRST_WORDS`: Governor, Senator, Representative, etc.
- Added partial org names to `_NAME_STOP_NAMES`: Law School, Affordable Energy, Concerned Scientists, etc.
- Added non-journalistic "source" filter: energy source, data source, power source, etc.
- Added institutional nouns to `_SINGLE_NAME_ORG_STOPS`: School, University, College, etc.
- Added energy companies to `_SINGLE_NAME_ORG_STOPS` and `_KNOWN_ORGS`: Entergy, Duke Energy, etc.

### Documentation Updates
- METHODOLOGY.md: Updated to 26 topic buckets, 69 entity clusters, added `energy_climate` topic definition, added Energy & Environment cluster category to §15.3, updated §15.4 growth history
- ARCHITECTURE.md: Updated topic bucket count
- AGENT_GUIDE.md: Updated topic list with energy_climate
- test_structural_consistency.py: Updated expected counts (25→26 topics, updated entity cluster assertions)
