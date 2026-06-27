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
