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

1. **Adversarial framing density:** ≥3 devices from the adversarial set (loaded_language, emotional_appeal, guilt_by_association, catastrophizing, power_asymmetry, isolation_framing, pressure_language, timeline_implication, juxtaposition, refusal_amplification, self_referential_investigation, kicker_framing, hypocrisy_frame, military_techno_optimism, assumed_consensus, editorial_aside, failure_precedent, editorial_deflation)
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

This ensures the correction pipeline is validated against real articles, not synthetic examples. All 83 annotated articles in `examples/sample_output/` follow this pattern.

## 8. Emotional Language Validation

### 8.1 The Term Lexicon

MediaScope maintains a curated lexicon of **735 emotional language terms** used for emotional intensity scoring (§1.2, dimension 2), outsourced intensity measurement (§7), and framing device detection. Unlike VADER's fixed sentiment lexicon, this list is continuously expanded from real article analysis — every article deep dive that reveals missing terms results in additions with regression tests.

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

Emotional intensity is the ratio of emotional language hits to total word count. Because the lexicon started at ~500 terms and has grown to 735, scores on older analyses may differ from current runs. The `SentimentResult` includes the raw hit count and word count so the density can be recomputed.

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

The `examples/sample_output/` directory contains three validated same-event comparisons:

| Event | Articles | Tone Gap | Framing Gap |
|---|---|---|---|
| MCI data exposure (Jun 22) | Wired (−0.60) vs Reuters (−0.10) | 0.50 | 7 vs 1 |
| Glasses launch (Jun 23) | Wired (−0.15) vs Gizmodo (+0.10) | 0.25 | 10 vs 0 |
| Arena prediction markets (Jun 23) | Reuters (+0.05) vs Engadget (−0.70) | 0.75 | — |

These demonstrate that identical facts can produce 0.25–0.75 point tone gaps and 6–10x framing device differentials across publications, making the editorial framing contribution directly observable.
