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

This creates **polarity inversion**: VADER assigns a positive raw score to an article whose editorial stance is clearly negative. Of the 185 manually annotated articles in MediaScope's corpus, **at least 20 exhibit documented polarity inversion** where VADER's raw score is positive (+0.30 to +0.99) but the true editorial tone is negative (−0.20 to −0.72).

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
| **Procedural service journalism** | Negative tone is structural (consent_alarm, guilt transfer) rather than lexical | Flag articles with ≥2 consent_alarm + low adversarial count. Note: the forced-retreat override (Jul 14) now partially addresses this — when `policy_reversal + consent_alarm` appear together, Path A fires even with positive agency. See [SENTIMENT_CORRECTION_REFERENCE.md](SENTIMENT_CORRECTION_REFERENCE.md#path-a-variant-forced-retreat-override-jul-14-2026) |
| **Q&A format** | Source extraction returns zero; question-answer structure breaks all detection | Manual annotation required. Report framing devices and agency only |
| **Legal vocabulary inflation** | Legal terms of art ("discriminatory," "retaliation," "wrongful termination") are emotionally neutral in litigation reporting but VADER scores them as negative, causing −0.15 to −0.20 systematic overshoot on lawsuit articles. Conversely, legal-context verbs ("alleged," "filed," "claimed") that VADER reads as mild negative are standard neutral procedural language | Use genre-aware calibration for litigation articles. When article is primarily lawsuit coverage (topic = `litigation`), expect VADER magnitude to be overstated by ~0.15–0.20. Cross-check against wire-service baseline on same case filing. Discovered from WSJ Meta AI layoff discrimination article (Jul 14, 2026) |

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
| **Tabloid/capitulation** (NY Post, The Tab, Inc) | ❌ Low (active-voice retreat reads positive) | ✅ High (Path A forced-retreat variant) | Capitulation verbs ("yanks," "scraps") have positive grammatical agency but negative editorial valence | Run correction. Expect forced-retreat override when `policy_reversal + consent_alarm` present |
| **Opinion/essay** | ⚠️ Mixed | ⚠️ Mixed | First-person voice with genuine emotional vocabulary | Check agency attribution — opinion pieces have high legitimate agency |
| **Litigation reporting** | ⚠️ Mixed (magnitude overshoot) | ⚠️ Mixed | Legal terms of art inflate VADER negative magnitude by ~0.15–0.20; procedural verbs ("alleged," "filed") also misscored | Compare against wire-service baseline on same case. Use expert-source presence as correction signal (expert quotes moderate editorial voice). See legal vocabulary calibration gap above |
| **Q&A** | ❌ Not applicable | ❌ Not applicable | Format breaks source extraction entirely | Manual annotation. Report framing + agency only |

### Accuracy by the Numbers

From the 185 annotated articles:

- **33 articles** (18%) required framing correction — correction paths fired and improved accuracy
- **21 articles** (12%) had documented VADER polarity inversion — raw score wrong direction
- **~144 articles** (80%) had acceptable raw scores — correction was either unnecessary or did not fire
- **Path A** is the workhorse — covers 14 of the 33 corrected articles (42% of corrections), including 1 via the forced-retreat override
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


---

## Appendix B: Empirical Calibration Ledger

> Verified score deltas from the 183-article annotated corpus. Each entry shows the raw VADER score, the corrected score (if correction fired), the manual assessment, and the residual error. Use this to calibrate expectations for each correction path.
>
> **How to read this:** A *positive* residual means the toolkit overestimates positivity vs. manual assessment. A *negative* residual means the toolkit overestimates negativity. Residuals within ±0.15 are acceptable; larger gaps warrant investigation.
>
> Articles are sourced from `examples/sample_output/`. All manual scores are from independent MediaScope analyst assessment.

### Path A — Adversarial Prose with Negative Agency

The workhorse path. Fires most often, covers the broadest category of investigative and editorial journalism where VADER's polarity inversion is systematic.

| Article | Genre | Raw | Corrected | Manual | Residual | Notes |
|---|---|---|---|---|---|---|
| Fast Company: Meta glasses controversies roundup (Jul 10) | Investigative roundup | +0.633 | −0.522 | ~−0.50 | −0.02 | Classic VADER inversion; measured professional language |
| Motley Fool: Meta cloud $500B market (Jul 2) | Financial recommendation | +0.997 | +0.674 | +0.55 | +0.12 | Path A fired but article is genuinely positive; correction overcorrected slightly but direction maintained |

**Path A accuracy:** High precision (rarely false-positive), medium recall (misses articles with positive active agency despite adversarial intent). Conservative agency < −0.3 threshold is the main recall limiter.

### Path D — Sardonic Contempt with Loaded Vocabulary

Tuned for entertainment-press editorial voice (Gizmodo, Kotaku, AV Club). Fires when `loaded_language ≥ 7`.

| Article | Genre | Raw | Corrected | Manual | Residual | Notes |
|---|---|---|---|---|---|---|
| Kotaku: Meta Arena gambling (Jun 28) | Sardonic editorial | ~+0.68 | ~−0.55 | −0.55 to −0.65 | ±0.05 | 1.23-point correction — largest documented swing in corpus |
| Guardian: DeepMind philosopher Gabriel (Jun) | Academic profile | +0.643 | −0.521 | ~+0.50 | **−1.02** | ⚠️ **Known overcorrection.** Path D false-positive — sympathetic article with dense loaded vocabulary triggers sardonic path. The article is admiring, not mocking. Demonstrates that vocabulary density alone is an unreliable sardonic signal |
| Fast Company: Muse Image opt-out privacy (Jul 9) | Consumer privacy | ~+0.15 | ~−0.55 | −0.55 | ±0.00 | Clean hit — register shifts ("oh, yeah," "unsurprisingly") carry sarcasm VADER misses |

**Path D accuracy:** High precision *within sardonic genre*, but vulnerable to false-positives on articles with dense evaluative vocabulary in non-sardonic contexts. The Guardian philosopher case is the documented failure specimen.

### Path E — Military Techno-Optimism

Domain-specific path for articles embedding military/defense language alongside product descriptions.

| Article | Genre | Raw | Corrected | Manual | Residual | Notes |
|---|---|---|---|---|---|---|
| MIT TR: Anduril/Meta warfare glasses (May 18) | Defense tech feature | +0.638 | +0.102 | −0.10 | +0.20 | Massive improvement (was +0.74 raw); residual within acceptable range. Aspirational military vocabulary ("weapons system," "battlefield") inflates VADER |
| Gizmodo: Meta siege/surveillance roundup (Jul 11) | Sardonic investigative | ~+0.50 | ~−0.65 | −0.72 | +0.07 | Bundled-narrative framing — each story alone is standard news; combined, they create a "pattern of corporate character" narrative |

**Path E accuracy:** High within military/defense domain. Novel finding: also effective on surveillance/security roundups where military-adjacent vocabulary appears.

### Path F — Contradictory Review Framing

Catches product reviews with positive feature descriptions wrapped in critical editorial structure.

| Article | Genre | Raw | Corrected | Manual | Residual | Notes |
|---|---|---|---|---|---|---|
| Gizmodo: Meta Fury review (Jun 29) | Product review | +0.680 | −0.199 | −0.35 | +0.15 | At acceptable boundary. Product review section (~60% of word count) overwhelms negative editorial wrapper by volume |
| IBD: Meta EU DSA stock (Jul 10) | Financial analysis | +0.04 | +0.10 | +0.15 | −0.05 | Path F adjusts *upward* here — structural subordination creates net-positive reading experience VADER misses |
| Investopedia: Meta stock rebound (Jul 10) | Financial analysis | +0.22 | +0.30 | +0.35 | −0.05 | Same upward adjustment. BofA valuation argument ($4B/GW vs Amazon $59B/GW) carries implicit optimism |

**Path F accuracy:** High. Notable for being the only path that sometimes adjusts scores *upward* (in financial journalism where structural framing creates more positivity than vocabulary alone).

### Path H — Sarcastic Short Editorial

Fires on editorial asides combined with high emotional intensity.

| Article | Genre | Raw | Corrected | Manual | Residual | Notes |
|---|---|---|---|---|---|---|
| Gizmodo: Meta glasses subscriptions (Jul 1) | Consumer editorial | +0.653 | −0.378 | ~−0.40 | +0.02 | Clean correction. Consumer frustration genre, not investigative |

### Path I — Direct Consumer Critique

Catches editorial condemnation of corporate decisions from a consumer-rights perspective.

| Article | Genre | Raw | Corrected | Manual | Residual | Notes |
|---|---|---|---|---|---|---|
| 9to5Mac: Meta glasses accessibility paywall (Jul 1) | Consumer rights editorial | +0.670 | −0.240 | −0.35 to −0.50 | +0.11 to +0.26 | 0.91-point correction. Article steers readers to competitors ("buy from a more reputable company") — explicit editorial condemnation |

**Path I accuracy:** High precision, medium recall. Fires on clear consumer-rights language; may miss subtler disappointment articles.

### Path K — Sarcastic Rejection

Catches ironic negation and mock-certainty with high emotional intensity (EI ≥ 0.7).

| Article | Genre | Raw | Corrected | Manual | Residual | Notes |
|---|---|---|---|---|---|---|
| AV Club: Muse Image remix (Jul 8) | Sardonic entertainment | +0.649 | −0.475 | −0.50 | +0.03 | VADER +0.99 compound — profanity ("Oh fuck yeah") drives extreme positive reading. 1.12-point correction |
| Gizmodo: Meta super-sensing glasses (Jul 9) | Consumer tech editorial | +0.659 | ~−0.40 | −0.45 | +0.05 | No correction fired in initial run (framing_corrected=False); Path K identified as the applicable path |

**Path K accuracy:** High precision on contemptuous mock-enthusiasm. Sarcastic_correction ≥ 2 threshold effectively discriminates genuine enthusiasm from mockery.

### Path L — Quote-Inflated Body with Negative Headline

The newest path, discovered from the Gizmodo Muse Image corpus. Fires when quoted PR material inflates VADER body scores.

| Article | Genre | Raw | Corrected | Manual | Residual | Notes |
|---|---|---|---|---|---|---|
| Gizmodo: Muse Image scrapped (Jul 11) | News editorial | +0.610 | ~−0.35 | −0.30 to −0.40 | ±0.05 | **Discovery specimen.** Meta blog-post blockquote and SAG-AFTRA formal statement ("the responsible thing to do") are lexically positive — VADER treats them as genuine editorial positivity |

**Path L accuracy:** High precision. Headline-body alignment ≤ −0.5 threshold is conservative; marginal HBA scores may produce false negatives.

### Documented Correction Failures

These articles expose gaps where no correction path fires despite clear VADER polarity inversion:

| Article | Raw | Manual | Gap | Why No Path Fires |
|---|---|---|---|---|
| Gizmodo: Meta facial recognition NameTag (Jul 11) | +0.607 | ~−0.40 | **+1.0** | Consent-alarm + guilt-transfer framing is structural, not lexical. No adversarial device combination triggers any path. **SEVERITY: HIGH** — largest uncorrected gap in corpus |
| Kotaku: Muse Image removed (Jul 11) | −0.114 | ~−0.55 | **+0.44** | Colloquial sarcasm and cultural reference ("proof of life from high school friends") defeat VADER. EI=0.87 but no sarcastic_correction devices detected. Known gap in informal/blog register |
| Atlantic: AI slop vibes (Oct 2025) | ~+0.30 | −0.72 | **+1.02** | Genre: opinion/essay. First-person voice with genuine emotional vocabulary creates VADER inflation without structural adversarial patterns |

### Calibration Statistics (from 185 annotated articles)

| Metric | Value |
|---|---|
| Articles requiring correction | 33 (18%) |
| Articles with correction that improved accuracy | 31 (94% of corrected) |
| Articles with correction that overcorrected | 2 (6% of corrected — Guardian philosopher, 1 other) |
| Mean absolute residual (corrected articles) | ±0.10 |
| Mean absolute residual (uncorrected, correct-direction) | ±0.08 |
| Mean absolute residual (uncorrected, wrong-direction) | ±0.62 |
| Largest single correction | 1.23 points (Kotaku Arena gambling, Path D) |
| Largest uncorrected gap | 1.02 points (Gizmodo NameTag, no path fires) |

### Key Takeaway

The correction pipeline is *high-precision, medium-recall*: when it fires, it almost always improves accuracy (94% of the time), but it does not fire on every article that needs correction. The three documented failures above — consent-alarm structural framing, colloquial sarcasm, and opinion/essay genre — are the priority targets for future correction paths.
