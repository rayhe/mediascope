# Accuracy Guide

> A practical reference for understanding MediaScope's accuracy characteristics, known failure modes, and how to interpret results correctly. For the correction pipeline mechanics, see [SENTIMENT_CORRECTION_REFERENCE.md](SENTIMENT_CORRECTION_REFERENCE.md). For the scoring framework, see [METHODOLOGY.md §1](METHODOLOGY.md#1-sentiment-analysis-framework).

---

## How to Use This Guide

MediaScope is a detection toolkit, not an oracle. Every automated score is a hypothesis that must be validated against the article's actual editorial posture. This guide tells you:

1. **Where the toolkit is reliable** — genres, article types, and conditions where raw or corrected scores match manual assessment
2. **Where it fails predictably** — specific failure modes with recognizable signatures
3. **What to do about failures** — practical decision tree for interpreting results

The goal is not perfect automation. It is *reliable flagging* — surfacing articles that warrant deeper analysis and providing structured evidence (framing devices, source stance, agency attribution) that holds up even when the headline sentiment number is wrong.

---

## Part 1: The #1 Accuracy Problem — VADER Polarity Inversion

### What It Is

VADER (Valence Aware Dictionary and sEntiment Reasoner) reads individual words and short phrases, not editorial intent. Professional journalism uses measured, confident, active language — "major step forward," "unprecedented scale," "innovative approach" — that VADER scores as positive *regardless of whether the article approves or condemns the subject*.

This creates **polarity inversion**: VADER assigns a positive raw score to an article whose editorial stance is clearly negative. Of the 176 manually annotated articles in MediaScope's corpus, **at least 20 exhibit documented polarity inversion** where VADER's raw score is positive (+0.30 to +0.99) but the true editorial tone is negative (−0.20 to −0.72).

### Why It Happens

Three linguistic patterns cause the vast majority of inversions:

| Pattern | Example | VADER Reads | Editorial Intent |
|---|---|---|---|
| **Aspirational vocabulary in critical context** | "a major step forward" in an article arguing the step is insufficient | Positive (+0.5) | Ironic/dismissive |
| **Corporate PR quotes treated as article tone** | "We take safety seriously" followed by evidence they don't | Positive (quote content) | Undermining (quote deployed adversarially) |
| **Profanity as mock-enthusiasm** | "fuck yeah, they're scraping your photos" | Positive (+0.99) | Contemptuous sarcasm |

### Correction Coverage

MediaScope's 12 correction paths (A–L) address polarity inversion in specific, recognizable article structures:

| Path | Addresses | Validated Examples | Coverage |
|---|---|---|---|
| **Path A** | Adversarial prose with negative agency | 13 articles | Broadest — catches most investigative journalism |
| **Path B** | VADER understates negative magnitude | 1 article | Rare — fires when VADER direction is correct but too mild |
| **Path C** | Product reviews with embedded anchors | 1 article | Narrow — requires specific anchor devices (kicker + self-ref) |
| **Path D** | Sardonic contempt with loaded vocabulary | 4 articles | Sardonic outlets (Gizmodo, Kotaku, AV Club) |
| **Path E** | Military techno-optimism | 3 articles | Domain-specific — aspirational military language |
| **Path F** | Contradictory review framing | 3 articles | Product praise embedded in critical editorial wrapper |
| **Path H** | Sarcastic short editorial | 3 articles | Editorial asides + emotional intensity |
| **Path I** | Direct consumer critique | 2 articles | Moral condemnation of corporate decisions |
| **Path J** | Expert-driven structural critique | 2 articles | Expert contradictions + structural devices |
| **Path K** | Sarcastic rejection | 4 articles | Ironic negation and mock-certainty |
| **Path L** | Quote-inflated body with negative headline | 5 articles | Quoted material inflates VADER body score |

**What's not covered (known gaps):**

| Failure Mode | Why No Path Fires | Workaround |
|---|---|---|
| **"Facts-speak-for-themselves" irony** | No adversarial vocabulary, no sarcastic devices — irony is purely structural (juxtaposing damning facts without editorial comment) | Manual annotation required. Flag when framing device count is low but source stance is heavily adversarial |
| **Financial journalism inflation** | Investment vocabulary ("strong buy," "attractive valuation") inflates by +0.3–0.5 | Trust framing devices over sentiment score. See [METHODOLOGY.md §16](METHODOLOGY.md#16-financial-journalism-sentiment-bias) |
| **Procedural service journalism** | Negative tone is structural (consent_alarm, guilt transfer) rather than lexical | Flag articles with ≥2 consent_alarm + low adversarial count |
| **Q&A format** | Source extraction returns zero; question-answer structure breaks all detection | Manual annotation required. Report framing devices and agency only |

---

## Part 2: Genre-Specific Accuracy

Article genre is the strongest predictor of toolkit accuracy. The table below summarizes expected accuracy by genre, based on validated examples in `examples/sample_output/`.

| Genre | Raw Score Accuracy | Corrected Score Accuracy | Primary Failure Mode | Recommended Workflow |
|---|---|---|---|---|
| **Wire service** (Reuters, AP) | ✅ High | N/A (correction rarely fires) | None — VADER works well on factual wire prose | Trust raw composite. Use as same-event baseline |
| **Investigative journalism** | ❌ Low (systematic false-positive) | ✅ High (Path A/B) | Polarity inversion — measured professional prose scores positive | Always run correction. Report both raw and corrected |
| **Tech editorial** | ⚠️ Mixed | ✅ High (Path C/F/J) | Product praise mixed with critical editorial wrapper | Run correction. Check headline-body alignment |
| **Sardonic** (Gizmodo, AV Club, Kotaku) | ❌ Very low | ✅ High (Path D/H/K) | Profanity, sarcasm, and irony all score positive in VADER | Always run correction. Expect Path D/H/K |
| **Financial/investor** | ❌ Low (systematic inflation) | ⚠️ Partial (no dedicated path yet) | Investment vocabulary inflates by +0.3–0.5 | Flag as genre-inflated. Weight framing devices over score |
| **Opinion/essay** | ⚠️ Mixed | ⚠️ Mixed | First-person voice with genuine emotional vocabulary | Check agency attribution — opinion pieces have high legitimate agency |
| **Q&A** | ❌ Not applicable | ❌ Not applicable | Format breaks source extraction entirely | Manual annotation. Report framing + agency only |

### Accuracy by the Numbers

From the 176 annotated articles:

- **32 articles** (18%) required framing correction — correction paths fired and improved accuracy
- **20 articles** (11%) had documented VADER polarity inversion — raw score wrong direction
- **~144 articles** (82%) had acceptable raw scores — correction was either unnecessary or did not fire
- **Path A** is the workhorse — covers 13 of the 32 corrected articles (41% of corrections)
- **Typical correction magnitude:** 0.50–1.20 points (raw → corrected gap)
- **Largest documented correction:** 1.23 points (Kotaku Meta Arena gambling: raw +0.68 → corrected −0.55, Path D)

---

## Part 3: When to Trust Each Score

### Decision Tree

```
1. What genre is the article?
   │
   ├─ Wire service (Reuters, AP) ──→ Trust raw_tone. Done.
   │
   ├─ Q&A ──→ Do NOT trust sentiment. Report framing + agency only.
   │
   ├─ Financial (Motley Fool, Barron's, MarketWatch, etc.)
   │   └─→ Flag as genre-inflated. If composite > +0.50 AND ≥3
   │       adversarial devices, trust framing devices over score.
   │
   └─ All other genres ──→ Continue to step 2.

2. Did framing correction fire? (result.framing_corrected == True)
   │
   ├─ Yes ──→ Trust result.overall_tone (corrected score).
   │          Report both raw and corrected with the correction path.
   │
   └─ No ──→ Continue to step 3.

3. Is raw_tone ≥ +0.30?
   │
   ├─ Yes ──→ Check for uncovered failure modes:
   │   │
   │   ├─ ≥3 adversarial framing devices? ──→ LIKELY POLARITY INVERSION.
   │   │   Report raw score with explicit caveat. Investigate manually.
   │   │
   │   ├─ Source stance < −0.30? ──→ Sources deployed adversarially
   │   │   despite positive vocabulary. Flag for manual review.
   │   │
   │   └─ Neither? ──→ Raw score may be correct. The article
   │       may genuinely have positive editorial tone.
   │
   └─ No ──→ Trust raw_tone. VADER is generally accurate for
             genuinely negative or neutral articles.
```

### Key Principle: Framing Devices as Ground Truth

When sentiment scores and framing device analysis disagree, **trust the framing devices**. This is the core design principle of MediaScope's accuracy model:

- Sentiment scores are **lexical** — they read individual words and miss context
- Framing devices are **structural** — they detect editorial techniques that reveal intent
- Source stance is **relational** — it measures whether sources are deployed to undermine or defend

A positive sentiment score with 8 adversarial framing devices is a false positive. A negative sentiment score with 0 adversarial framing devices may be a false negative (or a genuinely neutral article with measured language). The framing layer is the tiebreaker.

---

## Part 4: Common Misinterpretation Patterns

### Mistake 1: Treating raw_tone as editorial stance

**Wrong:** "This article has a tone of +0.65 toward Meta, indicating positive coverage."

**Right:** "The raw lexical score is +0.65, but 7 adversarial framing devices (loaded_language ×3, power_asymmetry ×2, editorial_deflation ×1, kicker_framing ×1) and negative agency (−0.35) indicate adversarial editorial stance. Path A correction yields −0.37."

### Mistake 2: Comparing scores across genres

**Wrong:** "Wired scores −0.35 on this article while Reuters scores +0.12 on the same event — a 0.47 gap indicating Wired bias."

**Right:** "Wired and Reuters cover this event in different editorial modes. Reuters uses wire genre (factual, ~600 words, no editorial voice); Wired uses investigative genre (1,800 words, multiple sources, editorial framing). The 0.47 tone gap is **expected** between these genres. To isolate editorial bias, compare framing device density (devices per 100 words): Wired has 3.2 devices/100w vs. a wire baseline of 0.5 devices/100w — the 2.7 excess per 100 words is the editorial framing contribution."

### Mistake 3: Ignoring sample size

**Wrong:** "Meta's asymmetry score is −0.45 (p < 0.01), proving systematic bias."

**Right:** "Meta's asymmetry score is −0.45 with 12 target articles and 48 peer articles over 30 days. The p-value (0.008) indicates statistical significance at α=0.01, but the sample size is modest and confidence interval is wide (−0.62 to −0.28). Effect size (Cohen's d = 0.71) is medium-large. This is suggestive of systematic asymmetry but would benefit from a larger article window."

### Mistake 4: Assuming correction = bias

**Wrong:** "Path A fired on 5 out of 8 Wired articles about Meta, proving Wired is adversarial."

**Right:** "Path A corrected VADER's false-positive scores on 5 investigative articles. This means VADER was wrong about the tone, not that the articles were biased. Whether the corrected scores reveal bias depends on the asymmetry calculation: compare Meta's corrected scores against Wired's coverage of peer companies in the same period and genre."

---

## Part 5: Accuracy Validation Checklist

When analyzing a new article, run this checklist to assess result quality:

| # | Check | Pass Condition | If Fail |
|---|---|---|---|
| 1 | Genre classification | Article genre identified | Cannot interpret scores without genre context |
| 2 | Entity detection | Primary entity correctly identified | Wrong entity → wrong asymmetry bucket |
| 3 | Framing device count | ≥1 device detected (for articles >500 words) | Zero devices on long articles may indicate regex gaps |
| 4 | Source extraction | ≥1 source extracted (except Q&A genre) | Zero sources = source extraction failure or opinion piece |
| 5 | Headline-body alignment | Score direction matches manual reading | Misaligned HBA can prevent Path L from firing |
| 6 | Correction path | If raw > +0.30 and ≥3 adversarial devices, correction fires | No correction = potential uncovered failure mode |
| 7 | Agency direction | Agency sign matches article framing | Wrong agency → wrong correction path selection |

### Post-Analysis Validation

After generating results, spot-check these against the article text:

1. **Read the kicker** (last 2 paragraphs). Does it align with the overall_tone direction?
2. **Count adversarial devices manually**. Are the detected devices real (not false-positive regex hits)?
3. **Check the top 3 entity mentions**. Are they the right entities, or did alias collision produce false matches?
4. **Read quoted sources**. Does the stance_balance match your reading of whether sources support or undermine the subject?

---

## Part 6: Reporting Results Responsibly

### Required Context

Every MediaScope result shared with stakeholders should include:

1. **The raw AND corrected score** (when correction fired), with the correction path named
2. **The genre classification** of the article
3. **The framing device count** and top adversarial devices
4. **The article count and time period** for asymmetry scores
5. **The counterargument** — what would explain this result WITHOUT bias? (See [QUALITY_STANDARDS.md §3](QUALITY_STANDARDS.md#3-analytical-rigor))
6. **The limitations** — sample size, genre confounds, time period, correction coverage

### What Not to Report

- Raw sentiment scores as standalone evidence of bias
- Cross-genre comparisons without normalization
- Asymmetry scores with fewer than 10 target articles
- Correction paths firing as evidence of bias (they're evidence of VADER limitations)
- Source stance from Q&A-format articles

---

## Appendix: Accuracy by Correction Path

Detailed accuracy characteristics of each correction path, based on validated examples:

| Path | Precision | Recall | Notes |
|---|---|---|---|
| **Path A** | High — rarely fires incorrectly | Medium — misses articles with neutral/positive agency despite adversarial intent | Agency < −0.3 threshold is conservative. Articles with positive active agency (e.g., "Meta launches…") and adversarial framing won't trigger Path A |
| **Path B** | High | Low — very narrow trigger conditions | Fires only when VADER direction is correct but magnitude insufficient |
| **Path C** | High | Low — requires specific anchor device combination | Only fires with ≥2 anchor devices (kicker + self-ref + juxtaposition) |
| **Path D** | High | Medium — vocabulary threshold (loaded ≥ 7) excludes subtle sardonic pieces | Works well for Kotaku/AV Club; may miss sophisticated satire |
| **Path E** | High | High within military domain | Domain-specific; irrelevant outside defense/military coverage |
| **Path F** | High | Medium | Catches product-review wrappers; may miss feature-comparison articles |
| **Path H** | High | Medium — requires editorial_aside ≥ 2 | Sarcastic pieces without explicit reader-directed asides won't trigger |
| **Path I** | High | Medium | Consumer moral-condemnation articles; relatively new, fewer validated examples |
| **Path J** | High | Medium | Expert-contradiction-driven criticism; requires structural devices |
| **Path K** | High | Medium — requires sarcastic_correction ≥ 2 + EI ≥ 0.7 | Catches ironic mock-enthusiasm; misses dry irony without sarcastic markers |
| **Path L** | Medium-High | Medium — requires HBA ≤ −0.5 | Headline-body alignment must be strongly negative; marginal HBA scores miss |

**Overall system accuracy estimate:**
- **With correction:** ~85–90% of articles get scores within ±0.15 of manual assessment
- **Without correction (raw only):** ~65–70% — the 30–35% failure rate is concentrated in investigative and sardonic genres
- **On wire service articles:** ~95%+ — VADER is well-suited to factual, neutral prose
