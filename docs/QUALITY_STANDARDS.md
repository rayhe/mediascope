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

1. **Adversarial framing density:** ≥3 devices from the adversarial set (loaded_language, emotional_appeal, guilt_by_association, catastrophizing, power_asymmetry, isolation_framing, pressure_language, timeline_implication, juxtaposition, refusal_amplification, self_referential_investigation, kicker_framing, hypocrisy_frame, military_techno_optimism)
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

This ensures the correction pipeline is validated against real articles, not synthetic examples. All 77 annotated articles in `examples/sample_output/` follow this pattern.
