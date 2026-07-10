# Quality Standards

## Overview

MediaScope enforces rigorous quality standards on all generated output. These standards ensure that media accountability research meets the same bar it holds other publications to. You cannot credibly critique journalism quality while producing low-quality analysis.

## 1. Citation Requirements

### Source Hierarchy

All factual claims must cite a source. Sources are graded by reliability:

| Grade | Type | Examples | Weight |
|---|---|---|---|
| **Primary** | Original documents and records | SEC filings, court records, .gov databases, corporate 10-K/10-Q, published research papers, official press releases | 1.0 |
| **Secondary** | Professional reporting by credible outlets | Reuters, AP, WSJ, NYT, Bloomberg, Financial Times, court reporting | 0.8 |
| **Tertiary** | Opinion, analysis, social media | Blogs, Substack, Twitter/X posts, opinion sections, Wikipedia | 0.4 |

### Citation Density

- **Minimum**: 1 verifiable source per factual claim
- **Target**: 70%+ of citations should be primary or secondary sources
- **Tertiary-only claims**: Must be flagged as "unverified" or "opinion-sourced"

### Verification

- URLs must resolve (HEAD request returns 2xx or 3xx)
- Archived URLs (web.archive.org) are acceptable
- "According to" attributions must name a specific source, not "experts say"
- Statistical claims must cite the original dataset or study, not a summary of it

## 2. Anti-Slop Standards

### Banned Phrases

The following 25 phrases are markers of AI-generated filler content and must not appear in MediaScope output. Organized by category:

**Filler nouns and verbs** (case-insensitive):
```
delve, tapestry, landscape, game-changer, paradigm shift, synergy,
leverage (as verb), ecosystem (metaphorical), deep dive,
unpack (metaphorical), robust, holistic
```

**Sentence-starter throat-clearing** (case-sensitive — only the capitalized form is banned):
```
Moreover, Furthermore, In conclusion,
It's worth noting, It bears mentioning
```

**Cliché connective phrases** (case-insensitive):
```
at the end of the day, moving forward, circle back,
in today's digital age, it is important to note,
needless to say, it goes without saying, without further ado
```

### Structural Markers

- **Em dash limit**: Maximum 3 per article. Overuse of em dashes is an AI writing signature.
- **Paragraph length**: No paragraph should be a single sentence unless it's a transition.
- **List abuse**: Bullet lists are for data, not for padding word count.
- **Throat-clearing**: First paragraphs must contain substance, not setup.

### Tone Markers

- No sycophantic openers ("Great question!", "Absolutely!")
- No hedge-stacking ("It could potentially perhaps be argued that...")
- No false enthusiasm about mundane findings
- No passive-aggressive "nuance" signaling

## 3. Analytical Rigor

### Counterargument Requirement

Every analysis MUST include the strongest counterargument to its own thesis. This is non-negotiable.

**Example**: If claiming Wired's coverage of Meta is biased by Advance Publications' Reddit investment, the counterargument section must address:
- "Wired covers ALL Big Tech critically, not just Meta"
- "Meta's genuine controversies (child safety, misinformation) warrant negative coverage"
- "Editorial independence from business interests is standard at major publications"
- "Correlation between ownership interests and coverage tone does not prove causation"

### Limitations Section

Every report MUST include a Limitations section that honestly states:
- What the analysis cannot prove
- Where evidence is circumstantial vs. direct
- What confounding factors exist
- What data was unavailable
- How sample size affects confidence

### Methodology Transparency

Every report MUST link to the full methodology documentation and state:
- Which sentiment models were used
- What time period was analyzed
- How many articles were included
- Statistical significance levels and effect sizes

## 4. Conflict of Interest Disclosure

### User Self-Disclosure

Anyone using MediaScope to publish findings MUST disclose their own conflicts of interest:

- Employment at any company covered in the analysis
- Financial interest in any company covered
- Personal relationships with journalists or editors analyzed
- Funding sources for the research
- Any prior public statements about the publication being analyzed

### Template

```
RESEARCHER CONFLICT DISCLOSURE
This analysis was conducted using MediaScope v{version}.
The researcher discloses the following potential conflicts:
- [Employment/financial interest/personal relationship]
- [Funding source]
- [Prior public statements]
```

## 5. Scoring Calibration

### Metacritic-Calibrated Scale

When scoring article quality or bias severity:

| Score | Meaning |
|---|---|
| 90-100 | Exceptional — virtually never warranted |
| 80-89 | Excellent — well-sourced, fair, comprehensive |
| 70-79 | Good — solid journalism with minor issues |
| 60-69 | Mixed — notable gaps in sourcing or framing |
| 50-59 | Below average — significant issues |
| 40-49 | Poor — unreliable or heavily biased |
| Below 40 | Failing — propaganda or misinformation territory |

100 is effectively unreachable. No grade inflation. A 72 is a compliment.

### Severity Scale for Conflicts

| Level | Meaning | Example |
|---|---|---|
| 1 | Minimal | Shared industry event sponsorship |
| 2 | Minor | Indirect competitive relationship |
| 3 | Moderate | Revenue dependency on covered entity's competitor |
| 4 | Significant | Major investment in direct competitor |
| 5 | Critical | Controlling stake in competitor + revenue deals with other competitors |

## 6. Enforcement

MediaScope's `quality/standards.py` module automatically checks output against these standards. A quality check returns:

- **PASS**: All requirements met
- **WARN**: Minor issues that should be addressed
- **FAIL**: Critical issues that must be fixed before publication

Reports that FAIL quality checks should not be published without manual review and correction.

### 6.1 Zero Named Sources Flag

When no named human source can be detected in an article (via attribution patterns like "said [Name]," "[Name] told/noted/explained," or "according to [Name]"), the quality check emits a `zero_named_sources` warning with a −12 score penalty. This flag catches:

- Articles sourced entirely from unnamed "experts," "people familiar," or "sources say" attributions
- Opinion pieces disguised as reporting (all claims are unsourced assertions)
- Secondary-source repackaging that quotes other publications instead of named individuals

**Detection patterns** (4 regex patterns):
1. Post-attribution: `said [First] [Last]`
2. Pre-attribution: `[First] [Last] said/told/noted/explained/added`
3. According-to: `according to [First] [Last]`
4. Title-based: `[First] [Last], [article] [title-word]` (e.g., "Jane Smith, a senior analyst")

**Genre sensitivity:** Wire-service factsheets (Reuters, AP) legitimately have zero named sources — they often use organizational attribution ("the company said"). For wire-format articles, this warning is informational, not a quality failure. For editorial articles, zero named sources is a significant concern because it means all claims are either unsourced or attributed to anonymous entities.

**Discovery:** TechLusive Meta Muse Image privacy article (Jul 8, 2026) — zero named human sources, all claims attributed to vague "experts" or unsourced editorial assertions.

## 7. Automated Scoring Accuracy

### The VADER Positive-Bias Problem

VADER and TextBlob — the toolkit's fast baseline sentiment models — systematically misprice editorial tone in investigative and adversarial journalism. Professional prose uses measured, confident language that lexical sentiment models score as positive, even when the editorial stance is clearly adversarial. This is not a bug in VADER; it is a fundamental limitation of lexical sentiment analysis applied to professional-grade prose.

**Validated failure cases:**

| Article | VADER Raw | Corrected | Gap | Root Cause |
|---|---|---|---|---|
| NYT "Meta AI Employees Miserable" | +0.61 | −0.37 | 0.98 | Active-negative agency + workplace coercion language |
| NYT "US Presses Meta on AI Reviews" | +0.61 | −0.57 | 1.18 | Isolation framing + regulatory pressure language |
| MIT TR "Meta AI Hack" | +0.65 | −0.43 | 1.08 | Expert-loaded adversarial sourcing with neutral prose |
| Wired "Applied AI Soul-Crushing" | +0.30 | −0.72 | 1.02 | Loaded language + emotional appeal + outsourced intensity |

These gaps demonstrate that **raw VADER scores on investigative journalism are unreliable** and should never be presented without framing correction.

### Tone Correction Pipeline

MediaScope's framing-aware correction fires when three conditions are all met:

1. **Adversarial framing density:** ≥3 devices from the adversarial set (loaded_language, emotional_appeal, guilt_by_association, catastrophizing, power_asymmetry, isolation_framing, pressure_language, timeline_implication, juxtaposition, refusal_amplification, self_referential_investigation, kicker_framing, hypocrisy_frame, military_techno_optimism, assumed_consensus, editorial_aside, failure_precedent, editorial_deflation, competitive_positioning, consumer_ownership, slippery_slope, competitive_deficit, competitive_displacement, absence_as_evidence, silence_as_guilt, expert_contradiction, loss_leader_framing)
2. **Negative agency signal:** Active-negative agency (tracking, cutting, forcing) or passive victim framing
3. **Positive raw VADER score:** The uncorrected composite score misleadingly reads as positive

When all three fire, the corrected `overall_tone` is derived from structural framing signals rather than VADER's lexical analysis. Both raw and corrected scores are preserved in the `SentimentResult` for transparency — the consumer can inspect when and why correction was applied.

### Known Scoring Limitations

| Limitation | Impact | Mitigation |
|---|---|---|
| **Q&A format** | Zero source extraction; VADER positive bias on conversational prose | Manual annotation required for interview-format articles |
| **Legal/judicial context** | "Admitted" and "conceded" used neutrally in court proceedings score as confession framing | Confession framing false-positive exclusion for legal contexts |
| **Security/hacking articles** | Domain-specific vocabulary ("exploit," "breach," "attack") inflates emotional intensity | Security context adjustment reduces intensity scores |
| **Wire-service vs. magazine genre** | Different genre conventions (length, framing density) affect comparisons | Use same-event comparison methodology to control for genre |
| **Counted anonymous sources** | "Two employees said" reads as zero anonymous sources to simple regex | `count_anonymous_sources()` delegates to comprehensive `extract_sources()` |
| **Product-name entities** | "Meta Glasses" extracted as a source name | Product-name stop-filter in source extraction |

### Scoring Calibration Validation

Every article analysis that introduces a toolkit correction must include:

1. **Manual tone assessment** — human-assigned tone score with brief justification
2. **Pre-correction toolkit score** — what VADER/TextBlob produced raw
3. **Post-correction toolkit score** — what the framing pipeline corrected to
4. **Gap analysis** — why the gap exists and which specific framing devices or detection failures caused it
5. **Regression tests** — at least one test per correction to prevent future regressions

This ensures the correction pipeline is validated against real articles, not synthetic examples. All 146 annotated articles in `examples/sample_output/` follow this pattern.

## 8. Emotional Language Validation

### 8.1 The Term Lexicon

MediaScope maintains a curated lexicon of **853 emotional language terms** used for emotional intensity scoring (§1.2, dimension 2), outsourced intensity measurement (§7), and framing device detection. Unlike VADER's fixed sentiment lexicon, this list is continuously expanded from real article analysis — every article deep dive that reveals missing terms results in additions with regression tests.

### 8.2 Term Categories

Terms are organized into domain-specific categories, each added because a specific article analysis exposed a blind spot:

| Category | Example Terms | Discovery Article |
|---|---|---|
| **General emotional** | alarming, devastating, heartbreaking, disturbing, chilling | Initial toolkit baseline |
| **Workplace morale/dysfunction** | soul-crushing, nihilistic, demoralized, attrition, burnout, toxic | Wired "Applied AI Gulag" (Jun 2026) |
| **Workplace revolt/dissent** | revolt, uprising, mutiny, walkout, backlash, uproar | Wired hackathon coverage (Jun 2026) |
| **Labor dignity/displacement** | alienation, dehumanizing, commodification, expendable, disposable | MIT TR Chinese workers article (Apr 2026) |
| **Privacy/surveillance** | invasive, creepy, snooping, stalking, spying, Big Brother | Wired NameTag coverage (Jun 2026) |
| **Legal/censorship/power-abuse** | censorship, despotic, hostage, coercive, retaliatory | Guardian whistleblower article (Jun 2026) |
| **Legal/whistleblower** | abusive, greed, unlawful, strike fear, punishing | Guardian Wynn-Williams lawsuit (Jun 2026) |
| **Military/defense/weapons** | lethal, warfighter, kill chain, battlefield, weapons system | MIT TR Anduril/Meta article (May 2026) |
| **Consumer privacy/wearable-tech** | creep, nefarious, glasshole, surveillance capitalism | Wired Ray-Ban Meta coverage (Mar-Jun 2026) |
| **Product review visceral** | ickiness, glassholism, privacy minefield, paranoid | Gizmodo Fury review (Jun 2026) |
| **Financial/market metaphor** | tsunami, hemorrhaging, bloodbath, cratering, free-fall | Barchart investor urgency article (Jun 2026) |
| **Child safety** | predatory, grooming, addiction, self-harm, cyberbullying | NYT child safety studies (Jun 2026) |
| **Pathologizing** | addicted, gorge, insatiable, voracious, glutton, contagion | Gizmodo AI tokens article (Jun 2026) |
| **AI agent/anthropomorphization** | happily, eagerly, confused, bewildered, naive | Malwarebytes AI bot article (Jun 2026) |

### 8.3 Maintenance Standards

Every addition to the emotional language lexicon must meet these standards:

1. **Real-article origin.** Every term was added because a specific article analysis showed the toolkit under-scoring emotional intensity. The discovery article is cited in a code comment.
2. **Deduplication.** Before adding terms, check for case-insensitive duplicates. A cleanup pass removed 14 pre-existing duplicates in Jun 2026.
3. **False-positive awareness.** Terms that have common non-emotional uses (e.g., "invasive" in medical/surgical context, "catastrophe" in dream/sleep narrative) should be flagged for context-aware detection. Some terms have special handling via `_is_negated_or_medical_context()`.
4. **Regression tests.** Every batch of term additions requires at least one test verifying the expected emotional intensity change on the discovery article.

### 8.4 Impact on Scoring

Emotional intensity is the ratio of emotional language hits to total word count. Because the lexicon started at ~500 terms and has grown to 853, scores on older analyses may differ from current runs. The `SentimentResult` includes the raw hit count and word count so the density can be recomputed.

**Common patterns by score range:**

| Intensity | Typical Genre |
|---|---|
| 0.00–0.10 | Wire-service reporting (Reuters, AP) |
| 0.10–0.25 | Investigative journalism with measured prose |
| 0.25–0.45 | Feature journalism with editorial voice |
| 0.45–0.65 | Opinion/commentary or heavily framed investigative piece |
| 0.65+ | Sardonic/polemic editorial (Gizmodo, Kotaku style) |

## 9. Claims-Evidence Mapping

### 9.1 Purpose

MediaScope's claims extraction system (`quality/claims.py`) identifies factual assertions in text and classifies them by evidence strength. This serves two purposes:

1. **Quality enforcement on MediaScope's own output** — reports with a `sourced_ratio` below 0.5 have more unsourced claims than sourced ones, which fails the quality bar.
2. **Article analysis** — measuring how well a publication sources its factual claims reveals differences in journalistic rigor.

### 9.2 Claim Types

| Type | Detection Pattern | Confidence | Example |
|---|---|---|---|
| **Statistic** | Percentages, dollar amounts, multipliers, large numbers | 0.80–0.90 | "65.2% voting power," "$7B stake value" |
| **Quote** | Attributed statements in quotation marks | 0.85–0.95 | '"We take privacy seriously," the spokesperson said' |
| **Citation** | URLs, "according to," formal reference patterns | 0.90–0.95 | "According to SEC filings..." |
| **Assertion** | Bare factual claims without evidence | 0.50–0.70 | "The deal creates a conflict of interest" |

### 9.3 Source Attribution

A claim is classified as "sourced" when it includes an attribution signal:

- **Explicit source:** "According to SEC filings," "per the 10-K," "Reuters reports"
- **Inline citation:** URL, `[1]`, `(Author 2024)` format
- **Quote attribution:** Named or described source + attribution verb

Claims without attribution are classified as "unsourced" — bare assertions or statistics presented as background fact.

### 9.4 API Output

```python
from mediascope.quality.claims import extract_claims, map_claims_to_evidence

claims = extract_claims(article_text)
mapping = map_claims_to_evidence(claims)

# mapping keys:
# 'sourced'       — list of Claim objects with verifiable sources
# 'unsourced'     — list of Claim objects without attribution
# 'by_type'       — claims grouped by evidence_type (statistic, quote, citation, assertion)
# 'total'         — total claim count
# 'sourced_ratio' — fraction with verifiable sources (key quality metric)
```

### 9.5 Quality Thresholds

| Sourced Ratio | Assessment | Action |
|---|---|---|
| ≥ 0.70 | Good | Publish |
| 0.50–0.69 | Acceptable | Review unsourced claims |
| 0.30–0.49 | Below standard | Must add sources or remove unsupported claims |
| < 0.30 | Failing | Do not publish |

## 10. Same-Event Comparison Standards

### 10.1 Article Pair Requirements

When performing cross-publication same-event comparisons (the most powerful evidence for editorial framing bias), the following quality standards apply:

1. **Same event, same day.** Both articles must cover the same underlying event (press release, court filing, earnings report, product launch). Multi-day coverage is acceptable only if the event is discrete (a single ruling, a single announcement).

2. **Wire-service baseline.** At least one article in the pair should be from a wire service (Reuters, AP) to establish the "neutral" event-severity reading. Wire-service tone approximates the factual baseline; `magazine_tone − wire_tone ≈ editorial_framing_contribution`.

3. **Full pipeline on both.** Both articles must be run through the complete MediaScope pipeline: entity detection, 8-dimension sentiment, framing device detection, source extraction + stance analysis, outsourced intensity measurement. Partial comparisons (tone-only) are insufficient.

4. **Seven-dimension comparison matrix.** Report all seven dimensions:
   - Word count (editorial investment)
   - Tone score (8-dimension sentiment)
   - Framing device count and types (technique fingerprint)
   - Source roster (named vs. anonymous, count, affiliations)
   - Source stance balance (adversarial vs. supportive)
   - Outsourced intensity ratio
   - Structural choices (headline, kicker, paragraph ordering)

5. **Genre acknowledgment.** Note genre differences (wire service writes breaking news; magazines write features) in the limitations section. Some framing differences reflect genre conventions, not editorial bias.

### 10.2 Validated Comparisons in the Corpus

The `examples/sample_output/` directory contains validated same-event comparisons across 13 distinct event clusters, ranging from 2-article pairs to 5-article multi-outlet analyses:

#### Tier 1: Explicit Cross-Analysis Files

These comparisons have dedicated cross-analysis documents with side-by-side metric tables:

| Event | Articles | Tone Gap | Framing Gap | File |
|---|---|---|---|---|
| MCI data exposure (Jun 22) | Wired (−0.60) vs Reuters (−0.10) | 0.50 | 7 vs 1 | `wired_vs_reuters_mci_data_exposure_2026_06_22_cross_analysis.md` |
| Glasses launch (Jun 23) | Wired (−0.15) vs Gizmodo (+0.10) | 0.25 | 10 vs 0 | `gizmodo_vs_wired_glasses_launch_2026_06_23_analysis.md` |
| Zuckerberg town hall (Jul 2–4) | Reuters (−0.06) vs TechCrunch (−0.05) vs Barron's (−0.20) vs PYMNTS (+0.60) vs TheStreet (−0.15 manual, +0.98 VADER) | 1.23 | 6 vs 6 vs 4 vs 6 vs 11 | `town_hall_4way_cross_analysis_2026_07_02.md`, `thestreet_meta_ai_warning_earnings_2026_07_04_analysis.md` |
| $1.4T youth safety penalty (Jul 7) | Reuters (neutral wire) vs Gizmodo (−0.65, 7 devices) vs NY Post (−0.40, 10 devices incl. tempering_coda) | 0.73 | 2 vs 7 vs 10 | `cross_pub_meta_1_4t_penalty_reuters_gizmodo_nypost_2026_07_07.md` |
| Muse Image launch (Jul 7–8) | Reuters (0.00) vs Bloomberg (−0.05) vs TechCrunch (−0.35) vs TechLusive (−0.25) vs iPhone in Canada (−0.05) | 0.35 | 0 vs 5 vs 18 vs 8 vs 4 | `cross_pub_muse_image_5way_2026_07_07.md` |
| Zuckerberg AI agents (Jul 2) | Reuters (wire) vs Barron's (editorial) | ~0.14 | confession_framing vs emotion_attribution | `reuters_vs_barrons_zuckerberg_ai_agents_2026_07_02_cross_analysis.md` |
| EU DSA addictive design (Jul 10) | WSJ (−0.27) vs Reuters (−0.28) vs CNN (−0.40) | 0.13 | failure_attribution headline gradient; WSJ most assertive, CNN most hedged | `cross_pub_eu_dsa_addictive_design_wsj_reuters_cnn_2026_07_10.md` |

#### Tier 2: Same-Event Article Clusters

These share a common underlying event and can be compared via their individual analysis files:

| Event | Outlets | Tone Range | Notes |
|---|---|---|---|
| Wynn-Williams lawsuit (Jun 25–26) | Guardian (−0.50), Engadget (−0.65), Fast Company (−0.71) | 0.21 | Legalistic → editorial sarcasm gradient across 3 outlets |
| Brain2Qwerty research (Jun 30) | Gizmodo (+0.65), Register (+0.60 raw / −0.35 manual) | 1.00 | VADER positive-bias failure case — same paper, opposite editorial stances |
| Child safety features study (Jun 29) | NYT (−0.05), Engadget (moderate-negative) | ~0.30 | Institutional reporting vs tech-press accountability framing |
| Arena / prediction markets (Jun 23–28) | NYT (2 articles), Gizmodo, AV Club, Kotaku | wide | 5 articles, same product, escalating editorial hostility over time |
| Gemini compute limits (Jun 28–Jul 1) | Reuters (neutral wire), Memeburn (tech blog) | ~0.40 | Wire vs blog framing of Google restricting Meta's Gemini access |
| Applied AI reorg (Jun 13–17) | Wired (4 articles), TechTimes | variable | Longitudinal cluster — same event arc covered repeatedly with escalating loaded language |

#### Statistical Summary

Across all validated comparison clusters:
- **Tone gaps** range from 0.21 (Wynn-Williams lawsuit, all outlets editorially negative) to 1.00 (Brain2Qwerty, genuinely opposite editorial stances on same research paper)
- **Framing device differentials** range from 1:1 (both outlets use similar techniques) to 10:0 (one outlet deploys extensive framing, the other stays neutral)
- **Wire-service baseline** (Reuters/AP) anchors at ±0.10 in 100% of comparison clusters where included, validating its use as a neutral reference
- **Genre-controlled comparisons** (wire vs magazine vs blog vs financial) produce the cleanest signal — same facts, different editorial modes

### 10.3 N-Way Cross-Outlet Comparisons

Single-pair comparisons (A vs B) establish that editorial framing exists. **N-way comparisons** (3+ outlets covering the same event) are more powerful because they reveal the *spectrum* of editorial responses and isolate the framing contribution of each outlet's editorial mode.

#### Requirements

1. **Minimum 3 outlets.** Two outlets can show a gap; three or more can show a gradient and identify which outlet is the outlier.

2. **Include at least one wire service.** The wire baseline anchors the neutral reading. Without it, the comparison shows relative differences between editorial outlets but cannot establish the absolute framing contribution of each.

3. **Include different editorial modes.** The analytical value of N-way comparisons comes from mode diversity. A comparison of three tech blogs covering the same event reveals less than wire + financial + tech-editorial covering it. Validated editorial modes:
   - **Wire service** (Reuters, AP): neutral attribution, minimal framing
   - **Financial analysis** (Barron's, Barchart): investor-oriented, stock-price anchored
   - **Tech editorial** (TechCrunch, Engadget, Gizmodo): industry-narrative, editorial voice
   - **Investigative magazine** (Wired, Atlantic): long-form, maximum framing density
   - **General newspaper** (NYT, Guardian): institutional accountability posture

4. **Present results in a comparison matrix.** The seven-dimension comparison (§10.1, point 4) should be presented in a single table with one row per outlet, enabling visual inspection of the gradient.

#### Discovery: Cross-Publication Import

N-way comparisons revealed a framing device invisible in single-pair analysis: **cross-publication import**. This occurs when a later article references an earlier outlet's loaded characterization as settled fact, laundering editorial framing through consensus attribution.

**Validated example:** TechCrunch (Jul 2, 2026) wrote "Several reports have depicted the overhaul as a soul-crushing gulag" — importing Wired's editorially loaded "gulag" characterization as consensus rather than attributing it to a single outlet's editorial choice. This framing device is detectable only when the analyst has already analyzed the source article (Wired, Jun 16) and recognizes the borrowed language.

**Detection patterns** (`cross_publication_import` framing device type):
- "several/multiple/other reports have described/depicted..." (vague collective attribution)
- "widely/commonly described/depicted as..." (consensus-laundering adverbs)
- "what [publication/reporters/critics] have called..." (indirect import)

Cross-publication import is distinct from `self_referential_investigation` (same publication citing its own prior reporting) and `anonymous_authority` (unnamed individual sources).

### 10.4 Longitudinal Same-Event Clusters

Some events generate coverage over days or weeks, not a single news cycle. These **longitudinal clusters** expose how editorial framing escalates, compounds, or decays over time — a dimension invisible in single-day comparisons.

#### Requirements

1. **Same underlying event.** All articles must trace to the same root event (reorganization, lawsuit filing, product launch), not merely the same topic.
2. **Timeline tracking.** Note publication date for each article and track when new editorial language first appears vs. when it becomes consensus.
3. **Framing escalation detection.** Compare framing device density across the timeline. If loaded language increases in later articles without new factual developments, the escalation is editorial, not event-driven.
4. **Cross-outlet framing propagation.** Track when characterizations coined by one outlet appear in later articles by other outlets (cross-publication import). This distinguishes viral editorial framing from independent editorial judgment.

#### Validated Example: Applied AI Reorg (Jun 13–17, 2026)

| Date | Outlet | Key Language | New? |
|---|---|---|---|
| Jun 13 | Wired | "employee revolt," "hackathon" framing | First use |
| Jun 16 | Wired | "soul-crushing," "gulag" | Escalation |
| Jun 16 | Wired | "atrocious" (Bosworth quote, headline-promoted) | Selective quotation |
| Jun 17 | TechTimes | "gulag" imported from Wired | Cross-pub import |

The "gulag" characterization, originated by Wired on Jun 16, propagated to TechTimes within 24 hours and to TechCrunch within 16 days (Jul 2) — demonstrating how editorial framing originating at one outlet becomes industry consensus through repetition and cross-publication import.
