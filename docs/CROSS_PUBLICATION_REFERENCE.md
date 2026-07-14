# Cross-Publication Comparison Quick Reference

> A compact lookup card for MediaScope's same-event cross-publication comparison methodology — the most powerful evidence technique for isolating editorial framing bias. For the full theoretical framework, see [METHODOLOGY.md §13](METHODOLOGY.md#13-cross-publication-same-event-comparison). For quality standards, see [QUALITY_STANDARDS.md §10](QUALITY_STANDARDS.md#10-cross-publication-same-event-comparisons).

---

## How to Use This Reference

Cross-publication comparison holds raw facts constant by analyzing how multiple outlets cover **the same event on the same day**. When the underlying event is identical, any difference in tone, framing density, source selection, or structural choices is attributable to **editorial DNA** rather than event severity. This is the media-analysis equivalent of a controlled experiment.

### Why This Matters

A critic can always argue that a publication's negative aggregate asymmetry score reflects genuine corporate wrongdoing. Same-event comparison neutralizes that argument: when two outlets cover an identical court filing, press release, or product launch and produce a 0.50-point tone gap with a 6× framing device differential, the editorial framing contribution is directly observable and cannot be explained by event severity.

### When to Use It

| Scenario | Use Same-Event Comparison? | Notes |
|---|---|---|
| Aggregate asymmetry score shows bias | ✅ Yes — confirmatory | Same-event data rules out "they just cover worse events" |
| Journalist migrated between outlets | ✅ Yes — complementary | Combine with DiD analysis for causal attribution |
| New framing device discovered | ✅ Yes — calibration | Check if device appears in wire baseline (if so, it's genre-normative, not adversarial) |
| Single article analysis | ❌ No | Single articles need the standard pipeline, not comparison |
| Longitudinal coverage arc | ✅ Yes — escalation | Track framing escalation over days/weeks on same root event |

---

## Part 1: Comparison Types

MediaScope supports three comparison architectures, each with increasing analytical power.

### 1.1 Pairwise Comparison (A vs B)

The simplest case: two outlets covering the same event.

| Strengths | Limitations |
|---|---|
| Establishes that editorial framing exists | Cannot distinguish which outlet is the outlier |
| Easy to construct from any shared event | Direction is ambiguous without a neutral baseline |
| Good for initial hypothesis generation | May reflect genre differences rather than editorial bias |

**When to use:** Initial exploration, when only two outlets covered the event, or when the pair spans different editorial modes (e.g., wire vs. investigative).

### 1.2 N-Way Comparison (3+ outlets)

Three or more outlets covering the same event reveal the **spectrum** of editorial responses.

| Strengths | Limitations |
|---|---|
| Shows gradient, not just gap | Harder to find events covered by 3+ outlets |
| Identifies which outlet is the outlier | Genre mixing requires explicit acknowledgment |
| Reveals cross-publication import patterns | More complex presentation (comparison matrix) |
| Isolates framing contribution per outlet | Timing differences may explain some variation |

**When to use:** Major events (product launches, court rulings, earnings reports) where multiple outlets publish same-day coverage. Always prefer N-way over pairwise when possible.

**Requirements:**
1. Minimum 3 outlets
2. Include at least one wire service (neutral baseline)
3. Include different editorial modes (see Part 3)
4. Present results in a seven-dimension comparison matrix

### 1.3 Longitudinal Cluster (same event over time)

Tracks how editorial framing escalates, compounds, or decays across multiple articles about the same root event over days or weeks.

| Strengths | Limitations |
|---|---|
| Reveals framing escalation vs. decay | Confounded by new facts emerging over time |
| Detects cross-publication import propagation | Harder to control for — later articles have more context |
| Shows when editorial language first appears | Requires careful timeline tracking |

**When to use:** Ongoing stories (reorganizations, lawsuits, regulatory proceedings) where coverage evolves. Track when loaded language first appears vs. when it becomes consensus.

---

## Part 2: The Seven-Dimension Comparison Matrix

Every cross-publication comparison must report these seven dimensions. Partial comparisons (tone-only) are insufficient per [QUALITY_STANDARDS.md §10.1](QUALITY_STANDARDS.md#10-cross-publication-same-event-comparisons).

| # | Dimension | What to Measure | What It Reveals |
|---|---|---|---|
| 1 | **Word count** | Total article length | Editorial investment — longer = more resources allocated |
| 2 | **Tone score** | 8-dimension composite (raw and corrected) | Raw editorial stance; corrected score accounts for genre VADER bias |
| 3 | **Framing device count** | Total devices from the 102-type taxonomy | Framing density — how many editorial techniques are deployed |
| 4 | **Framing device types** | Which specific devices appear | Editorial technique fingerprint — reveals preferred persuasion patterns |
| 5 | **Source roster** | Named vs. anonymous count + affiliations | Who the journalist chose to quote; who was excluded |
| 6 | **Source stance balance** | Adversarial vs. supportive vs. neutral ratio | Whether sources are deployed one-directionally or balanced |
| 7 | **Structural choices** | Headline framing, kicker, paragraph ordering, delayed defense | How information is architecturally arranged to shape interpretation |

### Supplementary Dimensions (recommended for investigative comparisons)

| Dimension | What to Measure | When to Include |
|---|---|---|
| Outsourced intensity ratio | Editorial vs. quoted emotional intensity | When one outlet appears neutral but quotes do the heavy lifting |
| Power asymmetry patterns | Dollar-magnitude framing, David vs. Goliath | When coverage involves corporate vs. individual dynamics |
| Cross-publication import | Borrowed characterizations from other outlets | In N-way and longitudinal comparisons |

---

## Part 3: Editorial Mode Taxonomy

Different publication types have genre-normative framing behaviors. A wire service using 0 framing devices is normal; a magazine using 0 would be unusual. Understanding editorial mode baselines prevents misattributing genre conventions as editorial bias.

| Mode | Examples | Baseline Tone | Baseline Framing | VADER Reliability | Analytical Role |
|---|---|---|---|---|---|
| **Wire service** | Reuters, AP | ±0.10 (neutral) | 0–2 devices | ★★★★★ High | **Neutral baseline** — anchors the "true" event severity |
| **Financial analysis** | Barron's, IBD, Investopedia, MarketWatch | +0.20 to +0.50 (VADER-inflated) | 3–6 devices (bull/bear, analyst authority, recovery narrative) | ★☆☆☆☆ Very Low | Investor-oriented; VADER inflated by 0.3–0.5 points |
| **Tech editorial** | TechCrunch, Engadget, Gizmodo | −0.10 to −0.30 | 3–8 devices | ★★☆☆☆ Low | Industry-narrative; editorial voice present but moderate |
| **Investigative magazine** | Wired, Atlantic | −0.30 to −0.65 | 7–18 devices | ★☆☆☆☆ Very Low | Long-form; maximum framing density; self-referential |
| **General newspaper** | NYT, Guardian, WSJ | −0.10 to −0.25 | 2–6 devices | ★★★☆☆ Moderate | Institutional accountability posture |
| **Sardonic entertainment** | AV Club, Kotaku | −0.30 to −0.60 (manual) / +0.30 (VADER) | 4–8 devices (sarcastic correction, editorial aside) | ★☆☆☆☆ Very Low | VADER completely fails on sarcasm |
| **Tabloid** | NY Post, Daily Mail | −0.20 to −0.40 | 5–10 devices (ultimatum framing, tempering coda) | ★★☆☆☆ Low | Dramatic headlines + hedging body |

### Mode Diversity Requirement

The analytical value of N-way comparisons comes from **mode diversity**. A comparison of three tech blogs reveals less than wire + financial + tech-editorial covering the same event, because mode diversity isolates the framing contribution of each outlet's editorial culture.

**Minimum recommended:** Include at least 2 different editorial modes. **Ideal:** 3+ modes including a wire service baseline.

---

## Part 4: Wire-Service Baseline Method

Wire services (Reuters, AP) are the analytical anchor. Their editorial mandate is factual neutrality — no commentary, minimal framing, rapid dissemination.

### How to Use the Baseline

```
Wire-service tone    ≈ event severity (neutral reading of the facts)
Magazine tone        − wire-service tone ≈ editorial framing contribution
Framing differential = magazine devices − wire devices ≈ editorial technique density
```

### Validated Baseline Behavior

Across all 13 validated comparison clusters where a wire service is included:

| Property | Validated Range | Notes |
|---|---|---|
| Wire tone | ±0.10 | Anchors at neutral in 100% of clusters |
| Wire framing devices | 0–2 | Minimal editorial technique |
| Wire source extraction | High accuracy | Clean attribution structure |
| Wire outsourced intensity | Low (≤0.20) | Journalist carries minimal emotional weight |

### Example Calculation

```
Event:     EU DSA "Addictive Design" ruling (Jul 10, 2026)
Reuters:   tone = −0.28, framing devices = 2
CNN:       tone = −0.40, framing devices = 4
WSJ:       tone = −0.27, framing devices = 3

CNN editorial contribution:  −0.40 − (−0.28) = −0.12 (moderate editorial darkening)
WSJ editorial contribution:  −0.27 − (−0.28) = +0.01 (near-neutral, wire-aligned)
```

### When No Wire Baseline Is Available

If no wire service covered the event, use the **most neutral outlet** as a proxy baseline and note the limitation explicitly. Financial outlets are poor proxies (VADER inflation). General newspapers (NYT, WSJ news section) are better proxies than magazines or entertainment outlets.

---

## Part 5: Validated Comparison Clusters

The corpus includes **13 same-event comparison clusters** across two tiers:

### Tier 1: Dedicated Cross-Analysis Files (7 clusters, 24+ articles)

| Event | Publications Compared | Tone Gap | Framing Gap | Key Finding |
|---|---|---|---|---|
| MCI data exposure (Jun 22) | Wired (−0.60) vs Reuters (−0.10) | 0.50 | 7 vs 1 | Vindication narrative + CEO personalization + kicker; Reuters factual |
| Glasses launch (Jun 23) | Wired (−0.15) vs Gizmodo (+0.10) | 0.25 | 10 vs 0 | Surveillance-consumer juxtaposition × self-referential investigation; Gizmodo product-first |
| Zuckerberg town hall (Jul 2–4) | Reuters / TechCrunch / Barron's / PYMNTS / TheStreet | 1.23 | 4–11 per outlet | Widest tone range; VADER TheStreet gap of 1.13 (worst corpus failure) |
| $1.4T youth safety penalty (Jul 7) | Reuters / Gizmodo / NY Post | 0.73 | 2 vs 7 vs 10 | Tabloid tempering coda discovery; NY Post hedges its own dramatic framing |
| Muse Image launch (Jul 7–8) | Reuters / Bloomberg / TechCrunch / TechLusive / iPhone in Canada | 0.35 | 0–18 per outlet | TechCrunch 18 devices on same product Reuters covered with 0 |
| Zuckerberg AI agents (Jul 2) | Reuters vs Barron's | ~0.14 | confession_framing vs emotion_attribution | Same Zuckerberg quotes → different attribution verbs |
| EU DSA addictive design (Jul 10) | WSJ / Reuters / CNN (+IBD / Investopedia expansion) | 0.13 (core) | Headline gradient | Regulatory content migrates from 5% (wire lede) to 81% (investment caveat) |

### Tier 2: Same-Event Article Clusters (6 clusters, ~18 articles)

| Event | Outlets | Tone Range | Key Signal |
|---|---|---|---|
| Wynn-Williams lawsuit (Jun 25–26) | Guardian / Engadget / Fast Company | 0.21 | Legalistic → editorial sarcasm gradient |
| Brain2Qwerty research (Jun 30) | Gizmodo / Register | 1.00 | Same paper, opposite editorial stances; worst VADER gap |
| Child safety features (Jun 29) | NYT / Engadget | ~0.30 | Institutional reporting vs tech-press accountability |
| Arena prediction markets (Jun 23–28) | NYT (×2) / Gizmodo / AV Club / Kotaku | wide | Escalating editorial hostility over time |
| Gemini compute limits (Jun 28–Jul 1) | Reuters / Memeburn | ~0.40 | Wire vs blog framing |
| Applied AI reorg (Jun 13–17) | Wired (×4) / TechTimes | variable | Longitudinal escalation + "gulag" cross-pub import |

### Tier 1 + Louisiana Datacenter (Jul 13)

| Event | Publications Compared | Key Signal |
|---|---|---|
| Meta Hyperion $50B Louisiana datacenter | WSJ / Fox Business / Barron's / IBD / MarketWatch / Wash. Examiner | 6-way genre gradient; identical facts produce 0.70+ point spread across financial/news/political modes |

### Statistical Summary

| Metric | Range | Notes |
|---|---|---|
| Tone gaps | 0.13–1.23 | Widest in multi-genre comparisons |
| Framing differentials | 1:1 to 18:0 | TechCrunch Muse Image is the most extreme |
| Wire baseline anchor | ±0.10 in 100% of clusters | Validates Reuters/AP as neutral reference |
| Genre-controlled spread | Up to 0.70 points | Same facts, different editorial modes |

---

## Part 6: Cross-Publication Import Detection

N-way and longitudinal comparisons revealed a framing device invisible in single-article analysis: **cross-publication import** (framing device #6).

### Definition

One outlet imports another outlet's loaded characterization as settled fact, laundering editorial framing through consensus attribution. The borrowed language appears as common knowledge rather than a single outlet's editorial choice.

### Detection Patterns

| Pattern | Example | Signal |
|---|---|---|
| Vague collective attribution | "several reports have depicted..." | "Reports" conceals that one outlet coined the phrase |
| Consensus-laundering adverbs | "widely described as..." | "Widely" implies broad agreement that may not exist |
| Indirect import | "what critics/reporters have called..." | Converts one journalist's editorial choice into collective characterization |

### Validated Propagation Example

The "gulag" characterization of Meta's Applied AI reorg:

| Date | Outlet | Usage | Type |
|---|---|---|---|
| Jun 16 | Wired | "soul-crushing gulag" (original) | Editorial coinage |
| Jun 17 | TechTimes | "gulag" imported from Wired | Cross-publication import (24h propagation) |
| Jul 2 | TechCrunch | "Several reports have depicted the overhaul as a soul-crushing gulag" | Consensus laundering (16-day propagation) |

### Analytical Significance

Cross-publication import matters because it converts one outlet's editorial framing into perceived industry consensus. Once "imported," the characterization no longer carries its original editorial weight — it becomes "what everyone says." Tracking propagation timelines reveals which outlets originate loaded framing vs. which amplify it.

---

## Part 7: Agent Workflow

### Step-by-Step Same-Event Comparison

```
1. IDENTIFY shared event
   └─ Same press release, court filing, earnings report, product launch
   └─ Same day (or within 48h for rolling events)

2. COLLECT articles from 2+ outlets (prefer 3+ with wire baseline)
   └─ Search each outlet's coverage of the event
   └─ Verify all articles reference the same underlying facts

3. RUN full MediaScope pipeline on EACH article independently
   └─ Entity detection
   └─ 8-dimension sentiment (raw + corrected)
   └─ Framing device detection (102 types)
   └─ Source extraction + stance analysis
   └─ Outsourced intensity measurement
   └─ Topic classification

4. BUILD seven-dimension comparison matrix
   └─ One row per outlet
   └─ All seven dimensions (see Part 2)

5. CALCULATE editorial framing contribution
   └─ Wire tone = event severity baseline
   └─ (Outlet tone − wire tone) = editorial contribution
   └─ (Outlet devices − wire devices) = technique density

6. IDENTIFY publication-specific framing fingerprints
   └─ Which devices are unique to each outlet?
   └─ Does one outlet use self-referential investigation?
   └─ Is there cross-publication import?

7. DOCUMENT limitations
   └─ Genre differences
   └─ Timing differences
   └─ Byline variation
   └─ Selection bias
```

### Python API Example

```python
from mediascope.analyze.entities import detect_entities, get_primary_entity
from mediascope.analyze.sentiment import analyze_composite, measure_outsourced_intensity
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources, analyze_source_stance
from mediascope.analyze.topics import classify_topic

def compare_articles(articles: list[dict]) -> dict:
    """
    Compare multiple articles covering the same event.

    Each article dict has keys: 'title', 'text', 'url', 'publication', 'date'.
    Returns comparison matrix with seven dimensions per outlet.
    """
    results = []
    for article in articles:
        entities = detect_entities(article['text'])
        sentiment = analyze_composite(article['text'], article['title'])
        framing = detect_framing_devices(article['text'])
        sources = extract_sources(article['text'])
        stance = analyze_source_stance(article['text'])
        outsourced = measure_outsourced_intensity(article['text'])
        topics = classify_topic(article['text'])

        results.append({
            'publication': article['publication'],
            'word_count': len(article['text'].split()),
            'tone_raw': sentiment.raw_overall_tone,
            'tone_corrected': sentiment.overall_tone,
            'correction_path': sentiment.correction_path,
            'framing_count': len(framing),
            'framing_types': [d.device_type for d in framing],
            'sources_named': sum(1 for s in sources if s.source_type == 'named'),
            'sources_anonymous': sum(1 for s in sources if s.source_type == 'anonymous'),
            'stance_balance': stance.stance_balance,
            'outsourced_ratio': outsourced.outsourced_ratio,
            'topics': [t.topic for t in topics],
        })

    # Calculate editorial contributions if wire baseline exists
    wire = next((r for r in results
                 if r['publication'].lower() in ('reuters', 'ap', 'associated press')), None)
    if wire:
        for r in results:
            r['editorial_contribution'] = r['tone_corrected'] - wire['tone_corrected']
            r['technique_density'] = r['framing_count'] - wire['framing_count']

    return {
        'event': articles[0].get('event', 'Unknown'),
        'outlets': len(results),
        'has_wire_baseline': wire is not None,
        'results': results,
    }
```

---

## Part 8: Common Pitfalls

| Pitfall | Why It Happens | How to Avoid |
|---|---|---|
| **Comparing genres as if equivalent** | Wire service vs. magazine framing density is expected to differ | Always note genre in limitations; use genre baselines from Part 3 |
| **Ignoring VADER inflation in financial articles** | Financial vocabulary inflates VADER by 0.3–0.5 | Use corrected tone scores; weight framing devices over raw sentiment |
| **Treating timing differences as framing** | Later articles may have more sources or context | Note publication timestamps; exclude articles published 48h+ apart unless longitudinal |
| **Claiming causation from comparison** | Same-event comparison shows *that* framing differs, not *why* | Combine with DiD careers analysis for causal claims |
| **Missing cross-publication import** | Requires having analyzed the source article first | Build event timelines; check which outlet first used key characterizations |
| **Single-pair without baseline** | Two editorial outlets may both be biased in the same direction | Include a wire service; without one, state limitation explicitly |
| **Conflating editorial aside with bias** | Some genres (entertainment, opinion) use editorial voice normatively | Flag genre; Gizmodo's editorial aside is genre-typical, Wired's self-referential investigation is not |

---

## Part 9: Relationship to Other Analysis Methods

| Method | What It Shows | Complementarity |
|---|---|---|
| **Aggregate asymmetry score** | *That* coverage is systematically asymmetric | Same-event comparison *confirms* it's editorial, not event-driven |
| **Framing device detection** | *How* editorial techniques are deployed | Same-event comparison shows *which outlets* deploy which techniques on identical facts |
| **Source stance analysis** | *Who* is quoted and how they're deployed | Same-event comparison reveals source selection differences when the source pool is identical |
| **DiD journalist migration** | *Why* bias exists (institutional vs. individual) | Same-event comparison provides the outcome variable; DiD provides the causal mechanism |
| **Genre-aware analysis** | *Expected* framing by publication type | Genre baselines calibrate same-event comparison against normative behavior |

---

*For the full theoretical framework, see [METHODOLOGY.md §13](METHODOLOGY.md#13-cross-publication-same-event-comparison). For quality standards, see [QUALITY_STANDARDS.md §10](QUALITY_STANDARDS.md#10-cross-publication-same-event-comparisons). For runnable code, see [`examples/same_event_comparison.py`](../examples/same_event_comparison.py).*
