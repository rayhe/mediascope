# Reuters: "Big Tech data centers are driving up power bills at America's Rust Belt factories"

**Publication:** Reuters
**Date:** July 7, 2026
**Word count:** ~1,050
**Toolkit version:** MediaScope (91 device types, 513 patterns, 2051 tests)
**Analysis date:** 2026-07-09

---

## Topic Classification

| Topic | Confidence | Matched Keywords |
|-------|-----------|------------------|
| **infrastructure_impact** (primary) | 0.478 | data center, data centers, electricity bills, electricity demand, megawatt, power bills, power-hungry |
| corporate_strategy | 0.440 | data center, data centers, expansion |
| energy_climate | 0.370 | clean energy, electricity bills, natural gas, power generation, power plants, ratepayer, utilities |

**Manual assessment:** Correctly classified. The article's core subject is infrastructure cost impact (data center power demand driving up manufacturer electricity bills), with corporate strategy and energy policy as secondary dimensions. The `infrastructure_impact` bucket captures this well.

---

## Entity Detection

| Entity | Canonical | Cluster | Notes |
|--------|-----------|---------|-------|
| Reuters | Reuters | Media/Publications | Self-byline |
| Meta | Meta | Meta | Named as one of the "tech giants"; declined to comment |
| Amazon | Amazon | Amazon | Named as one of the "tech giants"; no response to comment request |
| Donald Trump / Trump | Donald Trump | Political Figures | Mentioned as U.S. President prioritizing domestic manufacturing |
| White House | White House | US Government | Statement source on ratepayer protection |
| Federal Energy Regulatory Commission / FERC | FERC | Energy Research/Regulatory | Proposing transmission charge rule; declined comment |

**Manual assessment:** Entity detection correctly identifies the major named entities. Notable absences that are *correctly* absent: individual manufacturers (Belden Brick, Plaskolite, Tosoh SMD) are not in the entity cluster registry since they're article-specific subjects, not recurring tracked entities. PJM Interconnection is also not in the registry. This is expected behavior for a toolkit calibrated to media-bias analysis rather than general NER.

---

## Source Extraction

| Source | Type | Affiliation | Expert? | Quotes | Attribution Verb |
|--------|------|-------------|---------|--------|-----------------|
| **Aaron Tinjum** | named | Data Center Coalition | ✓ | 2 | said |
| **Paul Cicio** | named | Industrial Energy Consumers of America | ✓ | 3 | said |
| **Timothy Ling** | named | Plaskolite | ✓ | 3 | said |
| **John Holeman** | named | Tosoh | ✓ | 2 | said |
| **Brad Belden** | named | *(none detected)* | ✓ | 3 | said |
| **Meta** | no_comment | — | — | 1 | — |
| **Reuters** | organizational | Reuters | — | 1 | — |

**Manual assessment:**

✅ **Correct extractions:**
- Aaron Tinjum with affiliation "Data Center Coalition" — correctly extracted via Pattern 0f ("vice president of energy for Data Center Coalition")
- Paul Cicio with affiliation "Industrial Energy Consumers of America" — correctly extracted via Pattern 0f ("president of the trade group Industrial Energy Consumers of America")
- Timothy Ling with affiliation "Plaskolite" — correctly extracted via possessive pattern ("Plaskolite's senior environmental director")
- John Holeman with affiliation "Tosoh" — correctly extracted via possessive pattern ("Tosoh's director of facilities and maintenance")
- Meta as `no_comment` source — correctly detected from "Meta declined to comment"

⚠️ **Known limitation:**
- Brad Belden has no affiliation extracted. He's identified as "company president" with the company name (Belden Brick) appearing only in the article's opening paragraphs, not in the attribution sentence. This would require cross-sentence entity resolution linking "Belden" the surname to "Belden Brick Company" mentioned earlier — a deliberate scope boundary for the current source extraction pipeline.

✅ **False positives eliminated (this iteration):**
Prior to this iteration's fixes, the following false positives were extracted as sources: "Capacity" (from "Capacity charges"), "Energy Consumers" (from "Industrial Energy Consumers of America" partial match), "White House" (from statement attribution), "Synergy Research" (from data citation), "Smart Electric Power" (from the Smart Electric Power Alliance reference). All are now correctly suppressed via `_NAME_STOP_FIRST_WORDS`, `_SINGLE_NAME_ORG_STOPS`, and `_NAME_STOP_NAMES` additions.

---

## Framing Device Detection

| Device Type | Evidence Text | Tier |
|-------------|---------------|------|
| **heritage_nostalgia** | "141-year-old brick manufacturer" | Extended (NEW) |
| **heritage_nostalgia** | "products can be found in iconic" | Extended (NEW) |
| **heritage_nostalgia** | "fifth generation" | Extended (NEW) |
| **pressure_language** | "are pushing Big Tech to" | Core |
| **absence_as_evidence** | "Meta declined to comment" | Extended |
| **refusal_amplification** | "declined to comment" | Core |
| **refusal_amplification** | "did not respond" | Core |
| **defensive_verb_framing** | "was forced to" | Extended |
| **ironic_quotation** | "\"ratepayer protection pledge\"" | Core |
| **expert_consensus_authority** | "said Aaron Tinjum, vice president" | Extended |
| **scale_magnitude** | "1,038% rise" | Core |
| **scale_magnitude** | "7% rise" | Core |
| **expert_consensus_authority** | "said Paul Cicio, president" | Extended |
| **kicker_framing** | "regulators" (final paragraph device) | Structural |

**Manual assessment:**

The toolkit detects 14 framing device instances across 9 distinct types. This is a reasonable density for a 1,050-word article.

**Heritage nostalgia (NEW device type):** All three detections are accurate and represent the article's most distinctive editorial technique. The "141-year-old brick manufacturer" whose products appear in "iconic buildings including the Texas Alamo and Notre Dame University" and whose president is "part of the fifth generation working at the company" — these details aren't neutral context. They build an implicit argument: what data centers are threatening isn't just any factory, but irreplaceable American industrial heritage. A journalistically neutral version might say "a manufacturer in Sugarcreek, Ohio" without the age, the iconic buildings, or the generational continuity.

**Defensive verb framing:** "was forced to take emergency steps" — PJM's actions described as forced rather than voluntary. This could be argued as neutral description (PJM did take the steps under emergency conditions), but "took emergency steps" would be more neutral.

**Ironic quotation:** The scare quotes around "ratepayer protection pledge" are editorial — they signal skepticism about whether the pledge actually protects ratepayers, without the journalist needing to argue the point explicitly.

**False negatives worth noting:**
- The phrase "razor's edge" is quoted speech, so it wouldn't trigger loaded_language (which is correct — it's the source's language, not the journalist's).
- "power-hungry data centers" uses loaded language but it's a compound adjective that could be read as descriptive. The toolkit doesn't flag it, which is arguably correct since "power-hungry" in the context of data centers is closer to literal than metaphorical.

---

## Sentiment Analysis

| Dimension | Score | Notes |
|-----------|-------|-------|
| **Overall tone** | −0.247 | Moderately negative toward Meta |
| **Raw (uncorrected) tone** | +0.610 | VADER reads balanced expert quotes as positive |
| **Framing corrected?** | Yes | Correction applied |
| Emotional language intensity | 0.104 | Low — restrained wire-service register |
| Source authority framing | 1.000 | All named, credentialed sources |
| Agency attribution | −0.600 | Meta framed with low agency (declined to comment) |
| Headline/body alignment | 0.300 | Headline is mildly more negative than body |
| Anonymous source ratio | 0.000 | No anonymous sources |
| Speculative language ratio | 0.087 | Low speculation |
| Comparative framing | 0.000 | No direct competitor comparison |

**Manual assessment:**

The raw VADER tone of +0.610 is a classic VADER failure mode: the article contains extensive quotations from manufacturers and industry advocates using measured, professional language ("We're trying to be as creative as possible," "making us finally grapple with the difficult decisions") that VADER reads as positive. The corrected tone of −0.247 is much closer to the article's actual editorial posture, which is sympathetic to manufacturers and implicitly critical of Big Tech's infrastructure impact.

The −0.600 agency attribution for Meta is appropriate — Meta appears only as a non-responsive entity ("declined to comment") with no substantive voice in the story. Amazon's identical non-response compounds the effect. The article gives manufacturers ~20 direct quotes and Big Tech zero.

**Source balance:** 4 manufacturer/advocate sources (Belden, Ling, Holeman, Cicio) vs. 1 data center industry source (Tinjum) vs. 0 Big Tech company sources. This is a structural imbalance worth noting — the article is told almost entirely from the manufacturer perspective.

---

## Overall Editorial Assessment

**Tone:** Sympathetic to Rust Belt manufacturers, implicitly critical of Big Tech infrastructure expansion. The editorial register is restrained wire-service prose, but the framing consistently positions manufacturers as victims and data centers as disruptors of established American industrial heritage.

**Key framing techniques:**
1. **Heritage nostalgia** anchors the reader's sympathy before any data is presented — you learn about the 141-year-old company, its iconic buildings, and its fifth-generation leadership before seeing a single electricity price.
2. **Source asymmetry** gives manufacturers 4 voices and 11+ direct quotes while Big Tech gets 0 substantive responses. The "declined to comment" / "did not respond" treatment activates refusal_amplification — reasonable for transparency, but structurally ensures the manufacturer narrative goes unchallenged.
3. **Scale magnitude** in the headline data (1,038% capacity price increase, $1,600→$12,000 monthly charge) drives emotional response before context about what capacity charges represent or how they're calculated.

**What the article does well:** Specific, sourced data points (PJM capacity prices, state-level industrial electricity price increases). Named sources with clear affiliations. Includes the data center industry perspective (Tinjum's rebuttal that growth is "making us finally grapple with difficult decisions"). Includes the White House response.

**What the framing obscures:** Whether the manufacturers quoted represent typical cases or outliers. Whether the capacity charge increases are temporary (auction-cycle driven) or structural. What percentage of the PJM capacity price increase is attributable to data centers vs. plant retirements and transmission constraints (the article mentions these factors but doesn't quantify them). The article also omits that many manufacturers themselves benefit from data center proximity through local economic activity.

---

*Analysis generated by MediaScope toolkit. Heritage nostalgia framing device discovered from this article.*
