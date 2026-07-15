# Sentiment Correction Quick Reference

> A compact lookup card for all 12 tone correction paths (A–L) used by MediaScope's framing-aware sentiment pipeline. For the full scoring framework, VADER limitations, and academic foundations, see [METHODOLOGY.md §1](METHODOLOGY.md#1-sentiment-analysis-framework) and [QUALITY_STANDARDS.md §7](QUALITY_STANDARDS.md#7-automated-scoring-accuracy).

---

## How to Use This Reference

VADER + TextBlob produce a raw composite tone score for every article. This raw score is unreliable for investigative and editorial journalism because professional prose uses measured, active language that lexical models read as positive — even when the editorial stance is clearly adversarial. The correction pipeline fixes this by detecting structural framing signals that reveal the true editorial stance.

Each correction path fires when a specific combination of conditions is met. **Paths are evaluated in order (A → B → C → E → D → F → H → K → I → J)**; the first match wins. Path G operates earlier in the pipeline (during raw VADER computation) and is always active for long texts.

### When Correction Fires

All paths except G and B require `raw_tone >= 0.3` (VADER got the direction wrong or severely understated). Path B handles the case where VADER got the direction right but underestimated magnitude. Path G corrects a VADER normalization artifact independent of framing.

### Key Input Signals

| Signal | Source | Range | What It Measures |
|---|---|---|---|
| `raw_tone` | VADER + TextBlob composite | −1.0 to +1.0 | Lexical sentiment (often wrong for editorial prose) |
| `adversarial_count` | Sum of 32 adversarial device types | 0–∞ | How many editorial devices signal adversarial stance |
| `agency` | Agency attribution scorer | −1.0 to +1.0 | Whether subject is passive/victim (−) or active/powerful (+) |
| `emotional_intensity` (EI) | Emotional language ratio | 0.0 to 1.0 | Density of emotionally charged vocabulary |
| `loaded_count` | `loaded_language` framing count | 0–∞ | Raw contemptuous word choice density |
| `aside_count` | `editorial_aside` framing count | 0–∞ | Register-breaking sarcastic interjections |
| `sc_count` | `sarcastic_correction` framing count | 0–∞ | Ironic negation and mock-certainty devices |
| `anchor_count` | Kicker + self-referential + juxtaposition | 0–∞ | Devices that shift the reader's final impression |

---

## Part 1: The 32 Adversarial Device Types

These are the framing devices counted toward `adversarial_count`. When ≥3 fire alongside negative agency, the correction pipeline activates. Full descriptions in [FRAMING_REFERENCE.md](FRAMING_REFERENCE.md).

| # | Device | Discovery Provenance |
|---|--------|---------------------|
| 1 | `loaded_language` | Core — baseline |
| 2 | `timeline_implication` | Core — baseline |
| 3 | `guilt_by_association` | Core — baseline |
| 4 | `juxtaposition` | Core — baseline |
| 5 | `refusal_amplification` | Core — baseline |
| 6 | `emotional_appeal` | Core — baseline |
| 7 | `catastrophizing` | Core — baseline |
| 8 | `power_asymmetry` | Core — baseline |
| 9 | `isolation_framing` | NYT voluntary-review article (Jun 2026) |
| 10 | `pressure_language` | NYT voluntary-review article (Jun 2026) |
| 11 | `failure_precedent` | Register Brain2Qwerty v2 (Jun 30, 2026) |
| 12 | `editorial_deflation` | Register Brain2Qwerty v2 (Jun 30, 2026) |
| 13 | `self_referential_investigation` | Wired glasses launch review (Jun 23, 2026) |
| 14 | `kicker_framing` | Wired glasses launch review (Jun 23, 2026) |
| 15 | `hypocrisy_frame` | Guardian Wynn-Williams (Jun 25, 2026) |
| 16 | `military_techno_optimism` | MIT TR Anduril/Meta warfare glasses (May 18, 2026) |
| 17 | `assumed_consensus` | Gizmodo glasses subscription (Jul 2026) |
| 18 | `editorial_aside` | Gizmodo glasses subscription (Jul 2026) |
| 19 | `competitive_positioning` | 9to5Mac Conversation Focus (Jul 2026) |
| 20 | `consumer_ownership` | Android Authority Conversation Focus (Jul 2026) |
| 21 | `slippery_slope` | Android Authority Conversation Focus (Jul 2026) |
| 22 | `competitive_deficit` | Reuters Zuckerberg town hall (Jul 3, 2026) |
| 23 | `absence_as_evidence` | Newzlet Meta/Cannes editorial (Jul 3, 2026) |
| 24 | `silence_as_guilt` | Newzlet Meta/Cannes editorial (Jul 3, 2026) |
| 25 | `expert_contradiction` | Wired Conversation Focus paywall (Jul 2026) |
| 26 | `loss_leader_framing` | Wired Conversation Focus paywall (Jul 2026) |
| 27 | `competitive_displacement` | MIT TR open-weight models (Jul 9, 2026) |
| 28 | `recidivism_framing` | Fast Company Muse Image opt-out (Jul 9, 2026) |
| 29 | `sarcastic_correction` | AV Club Muse Image remix (Jul 2026) |
| 30 | `consent_alarm` | Gizmodo Muse Image scrapped article (Jul 11, 2026) |
| 31 | `precedent_analogy` | Reuters insurance-defense article (Jun 2026) |
| 32 | `policy_reversal` | NY Post Muse Image article (Jul 2026) |

### Anchor Device Types (subset)

Three devices form the "anchor" set used by Path C. These shift the reader's *final impression* regardless of the article's overall tone:

| Device | Why It Anchors |
|---|---|
| `kicker_framing` | Last paragraph overrides the reader's memory of earlier content |
| `self_referential_investigation` | Links product to publication's prior adversarial reporting |
| `juxtaposition` | Pairs positive product with negative context (e.g., consumer glasses ↔ military surveillance) |

---

## Part 2: Correction Paths

### Path A — Full Adversarial Override

**Problem:** VADER scores investigative/adversarial articles positive because measured, confident prose uses active verbs and factual language that lexical models read as positive.

**When it fires:**
| Condition | Threshold | Rationale |
|---|---|---|
| `raw_tone` | ≥ 0 | VADER got the direction wrong |
| `adversarial_count` | ≥ 3 | Structural framing confirms adversarial stance |
| `agency` | < −0.3 | Subject framed as passive/under scrutiny |

**Correction formula:**
```
base = agency
amplified = base × (0.6 + 0.4 × EI)
density_factor = min(adversarial_count / 8, 1.0)
framing_tone = amplified × (0.7 + 0.3 × density_factor)
corrected = 0.10 × raw_tone + 0.90 × framing_tone
```

**Blend:** 90% framing / 10% raw — strongest correction. Clamped to [−1.0, 0.0].

**Validated on:**
| Article | VADER Raw | Corrected | Manual | Gap Closed |
|---|---|---|---|---|
| NYT "Meta AI Employees Miserable" | +0.61 | −0.37 | −0.37 | 100% |
| NYT "US Presses Meta on AI Reviews" | +0.61 | −0.57 | −0.57 | 100% |
| MIT TR "Meta AI Hack" | +0.65 | −0.43 | −0.43 | 100% |
| Wired "Applied AI Soul-Crushing" | +0.30 | −0.72 | −0.72 | 100% |

#### Path A Variant: Forced-Retreat Override (Jul 14, 2026)

**Problem:** Path A's agency threshold (`agency < −0.3`) blocks correction on "corporate capitulation" articles where the subject is grammatically active — *they* yanked, reversed, scrapped — but editorially the frame is humiliation: the company was *forced* to back down. VADER scores the active-voice retreat language as neutral-to-positive, and the positive agency reading prevents Path A from firing.

**Discovery article:** NY Post "Meta yanks controversial AI image tool after privacy backlash" (Jul 13, 2026) — VADER raw +0.30, agency +0.33, 11 adversarial devices (7 loaded_language, 4 consent_alarm, 4 policy_reversal). Path A was blocked by agency > −0.3. Manual estimate: −0.45.

**When the override activates:**
| Condition | Threshold | Rationale |
|---|---|---|
| `policy_reversal` | ≥ 1 | Article frames a corporate reversal/retreat |
| `consent_alarm` **OR** `loaded_language` | ≥ 2 **OR** ≥ 5 | Privacy-violation or contempt framing accompanies the reversal |

When both conditions are met, the **forced-retreat flag** is set, and:
1. **Path A's agency threshold is waived** — the correction fires even with positive agency
2. **Emotional intensity replaces agency as the base tone driver** — because grammatical agency is unreliable in capitulation narratives (the subject's active voice doesn't map to editorial valence)
3. **A dampening factor (0.5×) is applied** — capitulation narratives are moderately negative, not as extreme as passive-agency investigative pieces

**Correction formula (forced-retreat variant of Path A):**
```
base = −0.5 × EI                           # EI 1.0 → base −0.5
amplified = base × (0.6 + 0.4 × EI)
density_factor = min(adversarial_count / 8, 1.0)
framing_tone = amplified × (0.7 + 0.3 × density_factor)
corrected = 0.10 × raw_tone + 0.90 × framing_tone
```

**Why dampened?** Without dampening, the standard Path A formula would produce −0.65 to −0.80 for tabloid capitulation pieces, which overcorrects. The subject *did* take action (even if forced), and the editorial stance is "they got caught and backed down" (moderately negative), not "they're under secret investigation" (strongly negative). The 0.5× factor on EI keeps corrections in the −0.30 to −0.50 range, which matches manual estimates for this genre.

**Complementary fix:** Capitulation verbs (`yanked`, `scrapped`, `axed`, `backtracked`, `walked back`, `backed down`, `reversed course`, `caved`, `capitulated`, `pulled the plug`, `shelved`) were added to `ACTIVE_NEGATIVE_FRAMING` to flip agency from positive to negative. This means future capitulation articles may fire standard Path A *without* the override when enough capitulation verbs appear. The override is a safety net for articles where the agency fix alone doesn't push below −0.3.

**Validated on:**
| Article | VADER Raw | Agency (pre/post fix) | Corrected | Manual | Gap Closed |
|---|---|---|---|---|---|
| NY Post "Meta yanks Muse Image" (Jul 13) | +0.30 | +0.33 / −0.20 | −0.43 | −0.45 | 96% |

---

### Path B — Amplification (Understated Negative)

**Problem:** VADER gets the direction right (negative) but understates the magnitude. Framing signals indicate the article is more adversarial than the lexical score reflects.

**When it fires:**
| Condition | Threshold | Rationale |
|---|---|---|
| `raw_tone` | < 0 and > −0.5 | Mildly negative — direction right, magnitude wrong |
| `adversarial_count` | ≥ 6 | Higher bar than Path A (direction is already right) |
| `agency` | < −0.3 | Subject framed passively |

**Three refinements at high EI:**

1. **Dynamic blend (EI > 0.6):** `raw_weight` slides from 0.50 to 0.15 — more trust in framing estimate as emotional content density rises.
2. **EI amplification (EI > 0.7):** Framing-derived tone amplified by `(1 + (EI − 0.7) × 0.5)` because visceral content (child exploitation, self-harm) can't be captured by word-level sentiment.
3. **Density boost (EI > 0.6 AND adversarial_count ≥ 12):** Additional `(1 + (count − 8) / 12)` amplification for deeply investigative pieces with overwhelming framing density.

**Blend:** 50% raw / 50% framing baseline, sliding to 15% raw / 85% framing at extreme EI.

**Validated on:**
| Article | VADER Raw | Corrected | Manual | Gap Closed |
|---|---|---|---|---|
| Wired Cannes contractors | −0.16 | −0.44 | −0.45 | 96% |

---

### Path C — Embedded Adversarial Anchor

**Problem:** Product reviews where the subject has positive agency (actively launching products) but anchor devices shift the reader's final impression negative. VADER scores the surface-level positive content; the reader walks away remembering the kicker.

**When it fires:**
| Condition | Threshold | Rationale |
|---|---|---|
| `raw_tone` | > 0.3 | Strongly positive VADER reading |
| `anchor_count` | ≥ 2 | At least 2 anchor devices (kicker, self-referential, juxtaposition) |
| `adversarial_count` | ≥ 4 | Overall adversarial framing present |
| `agency` | ≥ 0 | Positive agency (product review context) |

**Correction formula:**
```
anchor_target = 0.15
corrected = 0.55 × raw_tone + 0.45 × anchor_target
```

**Blend:** 55% raw / 45% toward +0.15 (neutral-to-slight-positive). Clamped to [−0.2, raw_tone]. The article IS partly positive — the correction nudges toward reality, not a full adversarial override.

**Validated on:**
| Article | VADER Raw | Corrected | Manual |
|---|---|---|---|
| Wired glasses launch review (Jun 23) | +0.67 | ~+0.38 | +0.15 |

---

### Path D — Sardonic/Mocking Framing

**Problem:** Article describes someone actively pursuing something but frames the pursuit as foolish, futile, or contemptible. VADER reads active positive words literally ("looking to start," "booming") while missing editorial contempt conveyed through raw contemptuous word choice.

**Key distinguishing signal:** `loaded_language` dominance — in sardonic pieces, loaded language typically accounts for >70% of all adversarial devices. The writer uses raw contemptuous vocabulary, not structural devices.

**When it fires:**
| Condition | Threshold | Rationale |
|---|---|---|
| `raw_tone` | ≥ 0.3 | VADER fooled by active language |
| `agency` | ≥ 0.3 | Positive agency (contrast with Path A's negative agency) |
| `loaded_count` | ≥ 7 | Very high loaded language density |
| `adversarial_count` | ≥ 8 | Overall adversarial count |

**Correction formula:**
```
density_factor = min(adversarial_count / 10, 1.0)
sardonic_tone = −(0.40 + 0.25 × density_factor)
corrected = 0.10 × raw_tone + 0.90 × sardonic_tone
```

**Blend:** 90% sardonic tone / 10% raw. Clamped to [−1.0, 0.0].

**Validated on:**
| Article | VADER Raw | Corrected | Manual |
|---|---|---|---|
| Kotaku Meta Arena (Jun 28) | +0.68 | −0.55 | −0.55 to −0.65 |

---

### Path E — Military Techno-Optimism Inflation

**Problem:** Military/defense articles where aspirational language ("revolutionize the battlefield," "transform warfare") inflates VADER's reading. Editorial stance is critical, but subjects ARE actively building things — the inflation comes from the content domain (warfare, weapons), not passive framing.

**When it fires:**
| Condition | Threshold | Rationale |
|---|---|---|
| `raw_tone` | ≥ 0.3 | VADER inflated by aspirational language |
| `military_techno_optimism count` | ≥ 3 | Domain-specific inflation devices |
| `agency` | < 0 | Any negative agency (relaxed from Path A's −0.3) |

**Correction formula:**
```
base = agency
amplified = base × (0.5 + 0.5 × EI)
density_factor = min(mto_count / 6, 1.0)
framing_tone = amplified × (0.6 + 0.4 × density_factor)
corrected = 0.30 × raw_tone + 0.70 × framing_tone
```

**Blend:** 70% framing / 30% raw — lighter than Path A because these are not purely adversarial pieces. Clamped to [−0.5, +0.2].

**Validated on:**
| Article | VADER Raw | Corrected | Manual |
|---|---|---|---|
| MIT TR Anduril/Meta warfare glasses (May 18) | +0.64 | ~−0.10 | −0.10 |

---

### Path F — Contradictory Review Framing

**Problem:** Product reviews where the reviewer gives a positive product assessment but wraps it in negative editorial context about privacy, ethics, or corporate behavior. Positive product language outnumbers negative editorial passages by word count, so VADER reads overall positive.

**When it fires:**
| Condition | Threshold | Rationale |
|---|---|---|
| `raw_tone` | ≥ 0.3 | VADER inflated by product praise |
| `adversarial_count` | ≥ 4 | Editorial wrapper is adversarial |
| `EI` | ≥ 0.5 | Privacy/ethics loaded language present |
| `agency` | −0.4 to 0.0 | Mixed agency — building good products AND acting badly |
| `rhetorical_question ≥ 1` OR `loaded_count ≥ 3` | — | Kicker question or heavy loaded language |

**Correction formula:**
```
density_factor = min(adversarial_count / 8, 1.0)
review_tone = −(0.25 + 0.15 × density_factor + 0.10 × EI)
corrected = 0.20 × raw_tone + 0.80 × review_tone
```

**Blend:** 80% framing / 20% raw. Clamped to [−0.6, 0.0].

**Validated on:**
| Article | VADER Raw | Corrected | Manual |
|---|---|---|---|
| Gizmodo Meta Fury review (Jun 29) | +0.68 | ~−0.35 | −0.35 |

---

### Path G — VADER Long-Text Normalization Fix

**Problem:** VADER's compound score is normalized via `sum / sqrt(sum² + alpha)` where `alpha=15`, tuned for tweet-length texts. For long articles (10+ sentences), this normalization amplifies small biases — a few business words like "risk," "pressure," "problem" in otherwise neutral context can push compound to −0.85 when sentence-level sentiment is balanced.

**When it fires:**
| Condition | Threshold | Rationale |
|---|---|---|
| Sentence count | ≥ 10 | Long enough for normalization distortion |
| Divergence (compound vs sentence mean) | > 0.5 | Full-text and sentence-level disagree substantially |
| Compound magnitude | > 0.5 | Strong full-text signal |
| Direction disagrees | Opposite signs OR sentence mean ≈ 0 | VADER's direction appears wrong |

**Correction formula:**
```
vader_compound = 0.70 × sentence_mean + 0.30 × vader_compound
```

**Blend:** 70% sentence-level / 30% full-text. This operates at the VADER stage *before* the composite score and framing correction, so it affects the input to all subsequent paths.

**Note:** Unlike all other paths, Path G does not require framing signal — it corrects a statistical artifact in VADER itself. It always runs for qualifying articles regardless of adversarial device count or agency.

---

### Path H — Sarcastic Short Editorial

**Problem:** Short opinion pieces (~<500 words) where the editorial voice is sarcastic/dismissive but the subject has neutral agency (the company IS doing things, just doing them badly). VADER reads active language as positive while missing the sarcastic register.

**Key distinguishing signals:** `editorial_aside` devices (direct reader address: "brace yourself," "let's be honest"), `assumed_consensus` ("People hate"), and high EI from consumer-frustration vocabulary.

**When it fires:**
| Condition | Threshold | Rationale |
|---|---|---|
| `raw_tone` | ≥ 0.3 | VADER fooled by active language |
| `aside_count` | ≥ 2 | At least 2 editorial asides (sarcastic register) |
| `adversarial_count` | ≥ 4 | Modest adversarial threshold |
| `EI` | ≥ 0.5 | Consumer-frustration vocabulary |
| `agency` | ≥ −0.1 | Neutral to slightly positive (contrast: Path A requires < −0.3) |

**Correction formula:**
```
sarcasm_density = min((aside_count + consensus_count) / 5, 1.0)
target_tone = −(0.30 + 0.20 × sarcasm_density + 0.10 × EI)
corrected = 0.15 × raw_tone + 0.85 × target_tone
```

**Blend:** 85% target / 15% raw. Clamped to [−0.7, 0.0].

**Validated on:**
| Article | VADER Raw | Corrected | Manual |
|---|---|---|---|
| Gizmodo Meta glasses subscription (Jul 2026) | +0.65 | ~−0.40 | −0.40 |

---

### Path I — Direct Consumer Critique with Positive Agency

**Problem:** Short opinion pieces where the author directly condemns a corporate decision using strong moral/consumer-rights language ("unacceptable," "no possible justification") but the company is the active agent (agency > 0). VADER scores positive because embedded product-description blockquotes dominate the lexical signal.

**Key distinguishing signals:** High EI (consumer-rights vocabulary), strong negative comparative framing (competitor elevated), and multiple consumer-adversarial framing devices (`consumer_ownership`, `competitive_positioning`, `slippery_slope`).

**When it fires:**
| Condition | Threshold | Rationale |
|---|---|---|
| `raw_tone` | ≥ 0.3 | VADER inflated by product blockquotes |
| `adversarial_count` | ≥ 5 | Overall adversarial density |
| `EI` | ≥ 0.5 | Consumer-rights vocabulary present |
| `consumer_device_count` | ≥ 2 | At least 2 of: consumer_ownership, competitive_positioning, slippery_slope, usage_dismissal_undercut |
| `agency` | > 0 | Company is the active agent |

**Correction formula:**
```
base_target = −(0.25 + 0.15 × EI)
if competitive_positioning ≥ 1: base_target −= 0.10
corrected = 0.20 × raw_tone + 0.80 × target_tone
```

**Blend:** 80% target / 20% raw. Clamped to [−0.6, 0.0].

**Contrast with other paths:**
- **vs Path H:** No editorial asides or register-breaking — criticism is direct, not sarcastic
- **vs Path A:** Agency is positive, not negative
- **vs Path C:** No kicker or self-referential investigation — criticism is in the body, not the anchor

**Validated on:**
| Article | VADER Raw | Corrected | Manual |
|---|---|---|---|
| 9to5Mac Conversation Focus paywall (Jul 2026) | +0.67 | ~−0.40 | −0.40 |

---

### Path J — Expert-Driven Structural Critique

**Problem:** Measured editorial where criticism is embedded through expert sources contradicting corporate rationale + structural devices (consumer_ownership, loss_leader_framing) rather than through emotional vocabulary. Both VADER and EI read these as positive because the *words* are measured — the criticism is structural.

**Key distinguishing signals:** `expert_contradiction` (credentialed source directly disputes company), `consumer_ownership` / `loss_leader_framing` (structural devices), moderate EI (0.10–0.50), and positive agency.

**When it fires:**
| Condition | Threshold | Rationale |
|---|---|---|
| `raw_tone` | ≥ 0.3 | VADER fooled by corporate PR quotes |
| `adversarial_count` | ≥ 5 | Overall adversarial density |
| `EI` | ≥ 0.10 | Low floor — structure is the signal, not vocabulary |
| `expert_contradiction_count` | ≥ 1 | At least one named expert directly contradicts company |
| `structural_device_count` | ≥ 2 | At least 2 of: consumer_ownership, competitive_positioning, loss_leader_framing, slippery_slope, usage_dismissal_undercut |
| `agency` | ≥ 0 | Neutral or positive agency |

**Correction formula:**
```
base_target = −(0.15 + 0.10 × EI)
if loss_leader_framing ≥ 1: base_target −= 0.05
if expert_contradiction ≥ 2: base_target −= 0.05
corrected = 0.30 × raw_tone + 0.70 × target_tone
```

**Blend:** 70% target / 30% raw — lightest of the editorial-override paths because the criticism is measured and structural, not visceral. Clamped to [−0.45, 0.0].

**Contrast with other paths:**
- **vs Path I:** EI is moderate, not high — criticism comes through expert sources, not vocabulary
- **vs Path D:** No sarcastic_correction or loaded_language dominance — tone is journalistic
- **vs Path A:** Agency is positive, not negative

**Validated on:**
| Article | VADER Raw | Corrected | Manual |
|---|---|---|---|
| Wired Conversation Focus paywall (Jul 2026) | +0.69 | ~−0.20 | −0.20 |

---

### Path K — Sarcastic Rejection Editorial

**Problem:** Satirical or vulgar short pieces where contempt is conveyed through `sarcastic_correction` devices (ironic negation, mock-certainty, sarcastic farewell) rather than structural adversarial framing. VADER reads profanity and active language as emotionally positive ("fuck yeah" → positive sentiment) while completely missing ironic context.

**When it fires:**
| Condition | Threshold | Rationale |
|---|---|---|
| `raw_tone` | ≥ 0.3 | VADER fooled by profanity and active language |
| `sarcastic_correction count` | ≥ 2 | At least 2 sarcastic_correction devices |
| `EI` | ≥ 0.7 | High emotional intensity from contemptuous vocabulary |

**Correction formula:**
```
sc_density = min(sc_count / 4, 1.0)
target_tone = −(0.35 + 0.20 × sc_density + 0.10 × EI)
corrected = 0.10 × raw_tone + 0.90 × target_tone
```

**Blend:** 90% target / 10% raw — strong correction because these articles are unambiguously negative. Target clamped to [−0.7, −0.2], final clamped to [−0.7, 0.0].

**Contrast with other paths:**
- **vs Path D:** Does not require massive loaded_language count — fires on sarcastic register regardless of loaded language density
- **vs Path H:** Requires sarcastic_correction devices, not editorial_aside — different register mechanism

**Validated on:**
| Article | VADER Raw | Corrected | Manual |
|---|---|---|---|
| AV Club Muse Image remix (Jul 2026) | +0.65 | ~−0.48 | −0.48 |

---

### Path L — Quote-Inflated Body with Negative Headline

**Problem:** Short editorial pieces where VADER scores the body positive because embedded quotes (corporate blog posts, PR statements, formal union statements) dominate the lexical signal, but the headline and editorial framing clearly position the article as critical. The headline VADER is strongly negative while the body VADER is positive.

**When it fires:**
| Condition | Threshold | Rationale |
|---|---|---|
| `raw_tone` | ≥ 0.3 | VADER inflated by quote material |
| `headline_body_alignment` | ≤ -0.5 | Strong headline-body divergence |
| `adversarial_count` | ≥ 4 | Substantial adversarial framing |
| distinct adversarial types | ≥ 3 | Breadth of adversarial framing |

**Correction formula:** Corrects toward mild negative range (-0.05 to -0.50), using adversarial density and headline-body divergence to calibrate severity.

**Contrast with other paths:**
- **vs Path A:** Path A requires adversarial ≥ 6 and agency < -0.3. Path L uses headline-body divergence as compensating evidence at lower adversarial threshold.
- **vs Path C:** Path C requires anchor devices ≥ 2 and positive agency. Path L has no anchor requirement — it's driven by headline-body mismatch.

**Validated on:**
| Article | VADER Raw | Corrected | Manual |
|---|---|---|---|
| Gizmodo Muse Image scrapped (Jul 2026) | +0.63 | ~−0.13 | −0.13 |

---

## Part 3: Path Selection Flowchart

```
Article arrives with raw_tone, agency, adversarial_count, EI, framing_summary
│
├─ [Path G runs first, during VADER computation]
│  Long text (≥10 sentences) + divergent compound vs sentence mean?
│  → Blend VADER compound toward sentence mean (0.70/0.30)
│
├─ raw_tone ≥ 0 AND adversarial ≥ 3 AND agency < −0.3?
│  → Path A: Full adversarial override (90/10)
│
├─ raw_tone < 0 AND > −0.5 AND adversarial ≥ 6 AND agency < −0.3?
│  → Path B: Amplification (50/50 → 15/85 at high EI)
│
├─ raw_tone > 0.3 AND anchor ≥ 2 AND adversarial ≥ 4 AND agency ≥ 0?
│  → Path C: Embedded anchor (55/45 toward +0.15)
│
├─ raw_tone ≥ 0.3 AND mto ≥ 3 AND agency < 0?
│  → Path E: Military techno-optimism (30/70)
│
├─ raw_tone ≥ 0.3 AND agency ≥ 0.3 AND loaded ≥ 7 AND adversarial ≥ 8?
│  → Path D: Sardonic/mocking (10/90)
│
├─ raw_tone ≥ 0.3 AND adversarial ≥ 4 AND EI ≥ 0.5 AND −0.4 ≤ agency < 0
│  AND (rhetorical_question ≥ 1 OR loaded ≥ 3)?
│  → Path F: Contradictory review (20/80)
│
├─ raw_tone ≥ 0.3 AND aside ≥ 2 AND adversarial ≥ 4 AND EI ≥ 0.5
│  AND agency ≥ −0.1?
│  → Path H: Sarcastic short editorial (15/85)
│
├─ raw_tone ≥ 0.3 AND sc ≥ 2 AND EI ≥ 0.7?
│  → Path K: Sarcastic rejection (10/90)
│
├─ raw_tone ≥ 0.3 AND headline_body ≤ -0.5 AND adversarial ≥ 4
│  AND ≥ 3 distinct adversarial types?
│  → Path L: Quote-inflated body + negative headline (mild negative)
│
├─ raw_tone ≥ 0.3 AND adversarial ≥ 5 AND EI ≥ 0.5 AND consumer_devices ≥ 2
│  AND agency > 0?
│  → Path I: Direct consumer critique (20/80)
│
├─ raw_tone ≥ 0.3 AND adversarial ≥ 5 AND EI ≥ 0.10 AND expert_contradiction ≥ 1
│  AND structural_devices ≥ 2 AND agency ≥ 0?
│  → Path J: Expert-driven structural (30/70)
│
└─ No path matches → return raw_tone uncorrected
```

---

## Part 4: Correction Strength Summary

Sorted from strongest to lightest blend:

| Path | Blend (framing/raw) | Target Range | Typical Gap Closed | When To Use |
|---|---|---|---|---|
| **A** | 90/10 | [−1.0, 0.0] | 0.98–1.18 | Classic adversarial: VADER positive, framing negative, agency passive |
| **D** | 90/10 | [−1.0, 0.0] | ~1.20 | Sardonic: loaded language dominance, positive agency, contempt |
| **K** | 90/10 | [−0.7, 0.0] | ~1.13 | Sarcastic rejection: ironic devices, profanity-as-positive |
| **H** | 85/15 | [−0.7, 0.0] | ~1.05 | Sarcastic short: editorial asides, neutral agency |
| **B** | 50/50 → 85/15 | dynamic | ~0.29 | Amplification: direction right, magnitude understated |
| **F** | 80/20 | [−0.6, 0.0] | ~1.03 | Contradictory review: positive product + negative editorial wrapper |
| **I** | 80/20 | [−0.6, 0.0] | ~1.07 | Consumer critique: moral condemnation, positive agency |
| **E** | 70/30 | [−0.5, +0.2] | ~0.74 | Military: aspirational warfare language inflates VADER |
| **J** | 70/30 | [−0.45, 0.0] | ~0.89 | Expert structural: measured criticism via expert contradiction |
| **G** | 70/30 (VADER stage) | n/a | varies | Long-text normalization: fixes VADER statistical artifact |
| **C** | 45/55 (toward +0.15) | [−0.2, raw] | ~0.29 | Anchor: product review with negative kicker/investigation |

---

## Part 5: Adding a New Correction Path

When a new article analysis reveals a VADER failure mode not covered by existing paths:

1. **Document the failure:** Record the article, raw VADER score, manual assessment, and the specific gap.
2. **Identify the distinguishing signals:** What combination of framing devices, agency, and EI uniquely identifies this failure mode? The new path MUST NOT overlap with existing paths' conditions.
3. **Determine the blend strength:** How certain is the framing signal? Strong certainty → 90/10. Mixed signals → 70/30 or 80/20. Partially positive → lighter blend.
4. **Set appropriate clamps:** What's the reasonable range for the corrected score? Never clamp to exactly −1.0 unless the article is genuinely propaganda-level.
5. **Place in evaluation order:** Paths are evaluated top-to-bottom. More specific conditions should come before more general ones to prevent shadowing.
6. **Write regression tests:** At least one test per new path, validating the specific article that discovered it.
7. **Update this reference:** Add the new path to Parts 2, 3, and 4.
8. **Update counts:** Run `python3 scripts/count_stats.py --check` and update README.md, METHODOLOGY.md, AGENT_GUIDE.md, and QUALITY_STANDARDS.md with the new path count.

### Naming Convention

Paths are lettered alphabetically by discovery order, not by evaluation order. The current sequence (A, B, C, D, E, F, G, H, I, J, K) reflects the chronological order in which VADER failure modes were discovered during real article analysis. The next path would be **L**.

### Proposed Path M — Structural Irony

A candidate path for macro-level article organization that creates negative framing invisible at the sentence level. Currently tracked in [FRAMING_REFERENCE.md § Proposed Additions](FRAMING_REFERENCE.md#proposed-additions-pending-validation) pending validation across ≥3 articles from ≥2 publications. Key challenge: the distinguishing signal is in section ordering and narrative structure, not in vocabulary, making it harder to detect with existing pattern-based methods.

---

## Part 6: Known Limitations

Documented VADER failure modes where no correction path currently fires. These are not bugs — they represent gaps in the pipeline's coverage that may become future correction paths when sufficient validation examples exist.

### Procedural Service Journalism

**Discovered:** NY Post Muse Image opt-out article (Jul 10, 2026)

**Problem:** VADER raw_tone scores procedural "how-to" service journalism as positive (+0.60 or higher) even when the article's editorial stance is clearly alarmist. The alarm comes from structural framing devices (`consent_alarm`, `competitive_guilt_transfer`, `no_comment_implication`) rather than adversarial vocabulary.

**Why no path fires:** Service journalism uses instructional language ("Here's how to turn it off," "Follow these steps") that VADER reads as positive. The article lacks adversarial editorial vocabulary — no `loaded_language`, no `editorial_aside`, no sarcastic register breaks. Agency is often near-neutral (the company is active, the user is given instructions). Emotional intensity may be moderate. This combination falls outside every existing path's trigger conditions:

| Path | Why It Doesn't Fire |
|---|---|
| A | `agency` is not strongly negative (article focuses on user action, not company scrutiny) |
| B | `raw_tone` is positive, not mildly negative |
| D | No `loaded_language` density, no sarcastic register |
| H | No `editorial_aside` devices |
| I | May lack `consumer_ownership` devices |
| K | No `sarcastic_correction` devices |

**Distinguishing signal:** High `consent_alarm` count (≥3) + instructional/procedural prose structure + positive VADER raw tone. The alarm is *structural* — the article's very existence as a "how to protect yourself" guide implies the default is dangerous, without any sentence explicitly saying so.

**Current workaround:** Manual annotation. When encountering procedural service journalism with high consent_alarm density but positive VADER raw_tone, note the gap in the analysis and report both scores with the caveat that VADER is systematically inflated for this genre.

**Path to resolution:** Requires ≥3 validated examples from ≥2 publications to establish the pattern. Candidate correction would key on `consent_alarm ≥ 3` + procedural prose markers (step-by-step instructions, imperative verbs like "go to Settings," "tap," "toggle off") + `raw_tone ≥ 0.3`.
