# Reuters: Meta Alberta Data Center — Toolkit Analysis
**Date:** 2026-07-08  
**Iteration:** Type A (Article Deep Dive)  
**Article:** "Meta to build C$13 billion Alberta data center, its first in Canada"  
**Genre:** Wire service (Reuters)

---

## 1. Entity Detection

### Toolkit Output (9 mentions)
| Cluster | Canonical | Matched Text | Position |
|---------|-----------|--------------|----------|
| Meta | Meta Platforms | "Meta Platforms" | 0-14 |
| Meta | Meta | "Meta" | 737-741 |
| Meta | Meta | "Meta" | 1110-1114 |
| Meta | Meta | "Meta" | 1344-1348 |
| Meta | Meta | "Meta" | 1600-1604 |
| Microsoft | Microsoft | "Microsoft" | 1606-1615 |
| Google | Alphabet | "Alphabet" | 1617-1625 |
| Amazon | Amazon | "Amazon" | 1630-1636 |
| Meta | Meta | "Meta" | 1804-1808 |

### Manual Analysis — Missed Entities
| Entity | Type | Mentions | Notes |
|--------|------|----------|-------|
| Pembina Pipeline Corp | Energy company | 5 | "Pembina Pipeline Corp", "Pembina" ×4 |
| Danielle Smith | Politician | 1 | Alberta Premier |
| Francois-Philippe Champagne | Politician | 2 | Canada industry minister + "Champagne" |
| Sturgeon County | Geographic | 1 | Data center location |
| Alberta | Geographic/political | 5+ | Province, repeated throughout |
| Canada | Geographic/political | 5+ | Country-level entity |
| Greenlight Electricity Centre | Project/facility | 1 | Pembina's power project |
| Big Tech | Aggregate entity | 1 | Industry collective reference |

### Gap Assessment
The entity detector covers tracked tech companies well but has **zero coverage** for:
- Energy/pipeline companies (Pembina is the co-equal actor in this deal)
- Canadian political figures (both are direct sources)
- Geographic entities (Alberta is the story's central location)

**Impact:** Entity-count-based framing analysis would see this as a "Meta story with brief competitor mentions" when it's actually a "Meta + Pembina + Alberta government" three-party deal. Entity coverage needs expansion beyond tech companies for infrastructure/energy crossover reporting.

---

## 2. Topic Classification

### Toolkit Output
| Topic | Confidence | Keywords |
|-------|-----------|----------|
| corporate_strategy | 0.6752 | data center, data centers, investment |
| infrastructure_impact | 0.6619 | data center, data centers, gigawatt |
| energy_climate | 0.3305 | carbon emissions, clean electricity, emissions, natural gas |

### Manual Assessment
**Accurate.** The primary topic is corporate infrastructure investment (corporate_strategy), with strong secondary energy/climate angle. The `energy_climate` confidence (0.33) slightly underweights the environmental tension — the final paragraph is the editorial counterpoint — but the ranking is correct. Wire-service energy reporting typically blends corporate + infrastructure + environment, and all three are captured.

---

## 3. Framing Devices

### Toolkit Output (6 devices, post-fix)
| Type | Evidence |
|------|----------|
| scale_magnitude | $13 billion |
| scale_magnitude | $9.17 billion |
| ironic_quotation | touted its clean electricity supply as |
| scale_magnitude | electricity equivalent to more than 800,000 homes |
| scale_magnitude | almost five times the national |
| tempering_coda | Tempering coda in final 25%: 2 moderating phrases found |

### Pre-Fix Output (3 devices)
Only the first 3 were detected. The last 3 were added by this iteration's fixes.

### Manual Analysis — Remaining Gaps
| Framing Device | Evidence | Why Missed |
|----------------|----------|------------|
| scale_magnitude | "1 gigawatt of power" | No pattern for raw energy unit milestones |
| scale_magnitude | "150 million cubic feet per day" | No pattern for volumetric quantities |
| scale_magnitude | "2,500 acres" | No pattern for acreage/land area |
| scale_magnitude | "1 billion cubic feet per day" | Same volumetric gap |
| urgency_frame | "racing to lock down power sources" | Competitive urgency language |
| scale_magnitude | "1,500 construction jobs and over 400 permanent roles" | Job creation numbers |
| milestone_enumeration | "company's 33rd globally" | Ordinal milestone (not caught) |

**Assessment:** The remaining gaps are mostly raw-number-plus-unit constructions without contextual framing verbs. These are low-priority — detecting every large number would create noise. The highest-value misses are "racing to lock down" (urgency framing) and the ordinal milestone "33rd globally."

---

## 4. Source Extraction

### Toolkit Output (5 sources)
| Name | Type | Verb | Quote Count |
|------|------|------|-------------|
| Meta Platforms | named | said | 1 |
| Danielle Smith | named | said | 1 |
| Philippe Champagne | named (expert) | said | 2 |
| Pembina | named | said | 2 |
| Meta | organizational | said | 1 |

### Issues Found
1. **Name truncation:** "Philippe Champagne" should be "Francois-Philippe Champagne" — the hyphenated first name is being split, and only the second part captured. The source extractor's name regex likely truncates at the hyphen or treats "Francois-Philippe" as a title.
2. **Quote bleed:** Danielle Smith's quote text includes a paragraph break — extends from her statement into the next paragraph about Canada's government.
3. **Missing data source:** "according to Canadian government data" — this is a document/data source, not a person, but it should be captured as an institutional source.
4. **Duplicate Meta:** "Meta Platforms" (named) and "Meta" (organizational) are the same entity counted twice.

### Positive Notes
- Correctly identified all human speakers
- Correctly marked Champagne as `is_expert: True`
- Zero anonymous sources correctly detected
- Attribution verb ("said") correctly identified throughout

---

## 5. Composite Sentiment

### Toolkit Output
| Metric | Value | Assessment |
|--------|-------|------------|
| overall_tone | 0.6135 | Slightly positive — ✅ correct for investment announcement wire |
| agency_attribution | 1.0 | Meta has clear agency — ✅ correct |
| anonymous_source_ratio | 0.0 | No anonymous sources — ✅ correct |
| emotional_language_intensity | 0.0 | Wire-service style, no emotional language — ✅ correct |
| speculative_language_ratio | 0.0 | No speculation — ✅ correct |
| headline_body_alignment | 0.3 | Seems low — both discuss Meta/Alberta/data center |
| comparative_framing | 0.0 | Should flag "five times the national average" — ❌ missed |
| source_authority_framing | 1.0 | All sources are authoritative — ✅ correct |
| framing_corrected | False | No framing correction applied — ✅ appropriate |

### Issues
- `headline_body_alignment` at 0.3 is suspiciously low for a wire article where the headline directly summarizes the body.
- `comparative_framing` at 0.0 misses "almost five times the national average" — the framing module now catches this, but the sentiment module doesn't read from the framing output.

---

## 6. Fixes Applied This Iteration

### Fix 1: Scale equivalence pattern (framing.py)
**Gap:** "electricity equivalent to more than 800,000 homes" — analogy pattern required "enough to power/run/supply" but wire service used "equivalent to."
**Fix:** Added new regex pattern matching `electricity/energy/power equivalent/equal/comparable to ... homes/households/cities`.
**Lines:** ~2267-2282

### Fix 2: Spelled-out multiplier pattern (framing.py)
**Gap:** "almost five times the national average" — numeric multiplier pattern required `\d[\d,.]*` but "five" is spelled out per AP style.
**Fix:** Added pattern matching English word-numbers (two through hundred) + "times" + comparison targets (national, global, average, more, higher, etc.).
**Lines:** ~2460-2479

### Fix 3: Tempering coda environmental counterpoint (framing.py)
**Gap:** Final paragraph walks back the positive investment narrative with environmental cost data, but the tempering coda detector only matched financial moderation phrases.
**Fix:** Added 3 new moderating phrase patterns: "which means/meaning that" (consequence construction), "far more carbon/emissions" (environmental cost), and "however/nonetheless/nevertheless" (hedging conjunctions).
**Lines:** ~6130-6145

### Test Results
- 175 existing tests pass (scale_magnitude: 29, multiplier: 6, sentiment: 42, entities: 63, topics: 18, sources: 17)
- No regressions

---

## 7. Article Characteristics (for corpus metadata)

| Property | Value |
|----------|-------|
| Publication | Reuters |
| Genre | Wire service |
| Word count | ~380 |
| Paragraph count | 13 |
| Named sources | 4 (Meta Platforms, Danielle Smith, Francois-Philippe Champagne, Pembina) |
| Anonymous sources | 0 |
| Dollar figures | 2 (C$13B, US$9.17B) |
| Structural devices | Tempering coda (environmental counterpoint in final ¶) |
| Primary entity | Meta |
| Sector crossover | Tech → Energy → Government |
| Unique for corpus | First Canadian political figure article; first energy company as co-equal actor; first natural-gas infrastructure framing |
