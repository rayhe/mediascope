# MediaScope Methodology

## Overview

MediaScope employs a multi-layered analytical framework to detect, measure, and report coverage asymmetry in media publications. This document describes the statistical methods, scoring frameworks, and academic foundations underpinning the toolkit.

## 1. Sentiment Analysis Framework

### 1.1 Multi-Model Approach

MediaScope uses three sentiment analysis layers, cross-validated against each other:

| Layer | Model | Purpose | Speed |
|---|---|---|---|
| Baseline | VADER (Hutto & Gilbert, 2014) | Lexicon-based, social media optimized | Fast |
| Secondary | TextBlob (Loria, 2018) | Pattern-based, adjective-focused | Fast |
| Primary | GPT-4o-mini / local LLM | Contextual editorial tone analysis | Slow |

The composite score weights the primary model at 0.5, with VADER and TextBlob each contributing 0.25. When the primary model is unavailable, VADER and TextBlob are weighted equally.

### 1.2 Eight-Dimension Tone Scoring

Beyond simple positive/negative polarity, MediaScope scores articles on eight dimensions designed to capture editorial framing:

| # | Dimension | Range | What It Measures |
|---|---|---|---|
| 1 | **Overall Tone** | -1.0 to +1.0 | Net editorial stance toward the entity |
| 2 | **Emotional Language Intensity** | 0.0 to 1.0 | Ratio of emotionally charged words to neutral language |
| 3 | **Source Authority Framing** | -1.0 to +1.0 | Whether quoted sources are used to undermine (-) or validate (+) the entity |
| 4 | **Agency Attribution** | -1.0 to +1.0 | Whether the entity is framed as passive/victim (-) or active/powerful (+) |
| 5 | **Headline-Body Alignment** | -1.0 to +1.0 | Whether the headline accurately represents the article body |
| 6 | **Anonymous Source Ratio** | 0.0 to 1.0 | Fraction of sources that are unnamed or anonymous |
| 7 | **Speculative Language Ratio** | 0.0 to 1.0 | Frequency of hedging words: "could," "might," "may," "reportedly" |
| 8 | **Comparative Framing** | -1.0 to +1.0 | Whether the entity is compared unfavorably (-) or favorably (+) to peers |

#### Prompt Template (for LLM-based scoring)

```
Analyze the following article for editorial tone toward [{entity}].
Score each dimension from the scale provided. Be precise — a neutral
article should score near 0, not at the extremes.

Article headline: {headline}
Article text: {text}

Score these dimensions:
1. Overall tone toward {entity} (-1.0 to +1.0):
2. Emotional language intensity (0.0 to 1.0):
3. Source authority framing toward {entity} (-1.0 to +1.0):
4. Agency attribution for {entity} (-1.0 to +1.0):
5. Headline-body alignment (-1.0 to +1.0):
6. Anonymous source ratio (0.0 to 1.0):
7. Speculative language ratio (0.0 to 1.0):
8. Comparative framing of {entity} vs peers (-1.0 to +1.0):

Respond with only the 8 numbers, one per line.
```

### 1.3 Academic References

- **VADER**: Hutto, C.J. & Gilbert, E.E. (2014). "VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text." ICWSM.
- **Media Bias Detection**: Spinde, T., et al. (2022). "BABE: A Benchmark for Annotated Media Bias Detection." In Findings of ACL.
- **AI Coverage Sentiment**: Bunz, M. & Braghieri, L. (2021). "The AI Index 2021 Annual Report." Stanford HAI. [finding: Guardian 29% positive AI coverage vs WSJ 49%]
- **Microsoft Research**: Raza, S., et al. (2025). "Media Bias Detector: Automated Detection of Bias in News Articles." CHI 2025.

## 2. Asymmetry Scoring Engine

### 2.1 Core Formula

The Asymmetry Score (AS) quantifies how much more negatively (or positively) a publication covers a target entity compared to its coverage of peer entities:

```
AS = mean(tone_scores_target) - mean(tone_scores_peers)
```

Where:
- `tone_scores_target` = overall tone scores for all articles primarily about the target entity
- `tone_scores_peers` = overall tone scores for all articles primarily about peer entities
- A **negative AS** indicates the target receives more negative coverage than peers
- An AS of 0 indicates equivalent treatment

### 2.2 Statistical Significance Testing

#### Welch's t-test

We use Welch's t-test (not Student's t-test) because we cannot assume equal variance between the target and peer coverage distributions:

```
t = (X̄₁ - X̄₂) / √(s₁²/n₁ + s₂²/n₂)
```

Degrees of freedom estimated via Welch-Satterthwaite equation. Significance threshold: α = 0.05.

#### Cohen's d Effect Size

Raw p-values can be misleading with large sample sizes. Cohen's d provides a standardized measure of practical significance:

```
d = (X̄₁ - X̄₂) / s_pooled

where s_pooled = √((s₁² + s₂²) / 2)
```

Interpretation (Cohen, 1988):
| d | Interpretation |
|---|---|
| < 0.2 | Negligible |
| 0.2–0.5 | Small |
| 0.5–0.8 | Medium |
| > 0.8 | Large |

#### Bootstrap Confidence Intervals

For non-parametric confidence intervals on the asymmetry score:

1. Resample target scores (with replacement) 1,000 times
2. Resample peer scores (with replacement) 1,000 times
3. Calculate AS for each bootstrap sample
4. Report 2.5th and 97.5th percentiles as 95% CI

### 2.3 Confound Controls

#### News Event Severity Normalization

A publication may cover a company more negatively during genuine crises (data breach, layoffs, antitrust action). To control for this:

1. Classify each article by topic bucket (see §3)
2. For each topic, compare the target's coverage to coverage of other companies in the same topic
3. This isolates editorial framing from event severity

Example: If Meta and Google both had layoffs, we compare how Wired covered Meta's layoffs vs Google's layoffs — not Meta's layoffs vs Google's product launches.

#### Volume Normalization

More coverage ≠ more bias. We normalize by:
- Calculating per-article tone scores (not aggregate)
- Reporting article counts alongside asymmetry scores
- Flagging when sample sizes are too small for reliable inference (n < 10)

## 3. Topic Classification

### 3.1 Standardized Topic Buckets

Articles are classified into 10 topic buckets to enable apples-to-apples comparison:

| Topic | Keywords |
|---|---|
| `layoffs` | layoff, fired, cut, reduction, restructuring, workforce, headcount, eliminated |
| `ai_development` | artificial intelligence, AI, machine learning, neural, LLM, language model, training data |
| `privacy_data` | privacy, data, surveillance, tracking, GDPR, consent, collection, user data |
| `antitrust_regulation` | antitrust, monopoly, regulation, FTC, DOJ, market power, dominance, consent decree |
| `child_safety` | children, teens, youth, minor, addiction, mental health, COPPA, age verification |
| `content_moderation` | moderation, misinformation, disinformation, hate speech, policy, removal, censorship |
| `financial_results` | earnings, revenue, profit, stock, market cap, quarterly, fiscal, guidance |
| `product_launch` | launch, release, announce, unveil, new feature, update, rollout, beta |
| `executive_behavior` | CEO, executive, leadership, management, culture, workplace, internal |
| `litigation` | lawsuit, sued, settlement, verdict, court, judge, plaintiff, damages |

Classification uses keyword matching with TF-IDF weighting. An article can match multiple topics; the top 3 by confidence are retained.

## 4. Framing Device Detection

### 4.1 Taxonomy

| Device | Description | Detection Pattern |
|---|---|---|
| **Guilt by Association** | Linking entity to controversial actors/events | Entity + controversial entity in same paragraph |
| **Anonymous Authority** | Using unnamed sources as definitive evidence | "sources say," "people familiar," "according to sources" |
| **Catastrophizing** | Framing outcomes as existential/irreversible | "crisis," "catastrophe," "existential threat," "doomsday" |
| **False Balance** | Presenting fringe views as equivalent to mainstream | "some say... others say" with asymmetric evidence |
| **Selective Omission Signal** | Notable absences detectable in text | "declined to comment" without context, missing competitor comparison |
| **Emotional Appeal** | Using emotional language instead of evidence | "heartbreaking," "chilling," "disturbing," "alarming" |
| **Loaded Language** | Word choices that carry implicit judgment | "admitted," "conceded," "insisted," "claimed" (vs neutral "said") |

### 4.2 Attribution Verb Analysis

The choice of attribution verb signals editorial stance:

| Category | Verbs | Signal |
|---|---|---|
| **Neutral** | said, told, noted, explained, stated, added, commented | Professional reporting |
| **Undermining** | claimed, argued, insisted, maintained, contended | Implies doubt |
| **Concessive** | admitted, conceded, acknowledged | Implies wrongdoing |
| **Adversarial** | warned, blasted, slammed, attacked, fired back | Implies conflict |

## 5. Source Authority Analysis

### 5.1 Source Grading

| Grade | Type | Examples |
|---|---|---|
| **Primary** | Original documents, filings, records | SEC filings, court records, .gov databases, official statements |
| **Secondary** | Professional reporting by credible outlets | Reuters, AP, WSJ, NYT, Bloomberg, FT |
| **Tertiary** | Opinion, analysis, social media | Blogs, Substack, Twitter/X posts, opinion sections |

### 5.2 Anonymous Source Scoring

Anonymous sources are not inherently problematic, but their ratio affects reliability:

| Ratio | Assessment |
|---|---|
| < 20% | Normal — most sources identified |
| 20–40% | Elevated — significant anonymous sourcing |
| 40–60% | High — majority claims rest on anonymous sources |
| > 60% | Extreme — article is substantially unverifiable |

## 6. Quality Control

### 6.1 MediaScope's Own Output Standards

All reports generated by MediaScope must pass internal quality checks:

1. **Citation density**: ≥1 verifiable source per factual claim
2. **AI slop detection**: Zero tolerance for banned phrases (see `quality/standards.py`)
3. **Counterargument**: Every analysis must include the strongest counterargument
4. **Limitations**: Every report must state what it cannot prove
5. **Methodology transparency**: Every report links to this document

### 6.2 Article Quality Scoring

When evaluating articles from target publications, MediaScope applies a quality score based on:
- Source diversity and authority
- Attribution verb neutrality
- Anonymous source ratio
- Speculative language ratio
- Headline-body alignment
- Counterargument presence

## 7. Limitations

### What MediaScope Can Do
- Measure coverage sentiment asymmetry with statistical rigor
- Map ownership and financial conflicts of interest
- Detect framing devices and source authority patterns
- Generate verifiable disclosure statements

### What MediaScope Cannot Do
- **Prove causation.** An asymmetry score correlated with a financial conflict does not prove the conflict caused the bias.
- **Read editorial intent.** We measure outcomes (published text), not motivations.
- **Account for all confounds.** Genuine differences in company behavior (e.g., one company has more scandals) will affect scores.
- **Replace human judgment.** Statistical significance is necessary but not sufficient. Domain expertise is required to interpret results.

### Known Biases in the Tool Itself
- Keyword-based entity detection may miss oblique references
- Sentiment models have known biases toward certain writing styles
- English-language only in current version
- RSS feeds may not capture all articles (paywalled content, newsletters)

## 8. References

1. Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum.
2. Hutto, C.J. & Gilbert, E.E. (2014). "VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text." *ICWSM*.
3. Spinde, T., et al. (2022). "BABE: A Benchmark for Annotated Media Bias Detection." In *Findings of ACL 2022*.
4. Raza, S., et al. (2025). "Media Bias Detector: Automated Detection of Bias in News Articles." *CHI 2025*.
5. Bunz, M. & Braghieri, L. (2021). AI coverage sentiment analysis. Referenced in Stanford HAI AI Index.
6. Welch, B.L. (1947). "The generalization of 'Student's' problem when several different population variances are involved." *Biometrika*, 34(1-2), 28-35.
7. Gentzkow, M. & Shapiro, J.M. (2010). "What Drives Media Slant? Evidence from U.S. Daily Newspapers." *Econometrica*, 78(1), 35-71.
8. Hamborg, F., et al. (2019). "Automated identification of media bias in news articles: an interdisciplinary literature review." *International Journal on Digital Libraries*, 20, 391-415.
