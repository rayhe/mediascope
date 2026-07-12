# NY Post: "New Meta feature lets anyone use your Instagram photos in AI images – here's how to opt out"

**Source:** NY Post (News Corp / Murdoch) | **Date:** July 10, 2026 | **Author:** Not credited (NY Post Tech desk)
**URL:** https://nypost.com/2026/07/10/business/new-meta-feature-lets-anyone-use-your-instagram-photos-in-ai-images-how-to-opt-out/

---

## Summary

Service journalism article (~400 words) structured as a how-to-opt-out guide for Meta's Muse Image AI generator. The article frames Muse Image's default opt-in for public Instagram accounts as a consent violation requiring immediate protective action, walks readers through the opt-out settings, then closes with an unrelated Grok/xAI deepfake scandal section that transfers guilt by proximity. This is the first NY Post article in the MediaScope corpus — News Corp / Murdoch ownership chain, distinct from Condé Nast (Wired), PMC/Penske (The Verge), Scott Trust (Guardian), Sulzberger family (NYT), and Emerson Collective (Atlantic).

## Manual Assessment

**Tone:** Alarmist service journalism (~-0.35 to -0.50). The article's editorial posture is consumer-protective throughout — the headline uses "anyone" (maximal threat scope), "your" (personal address), and the dash construction "– here's how to opt out" which embeds both problem and self-protective response. However, the body text achieves its alarm through neutral-seeming factual statements ("automatically enrolled," "without your knowledge") rather than editorial adjectives, making it harder for lexical sentiment tools to detect.

**Framing strategy:** Three-layer structure:
1. **Consent alarm framing** — The lead and lede repeatedly emphasize automatic enrollment, opt-in defaults, and the ability for "anyone on the internet" to use "your photos" / "your likeness." Six separate consent_alarm device instances establish the core editorial frame: the default is a violation, not a feature.
2. **Service journalism as implicit alarm** — The opt-out walkthrough section positions the reader as a victim needing protection. The very existence of step-by-step instructions implies the default is threatening enough to warrant emergency remediation.
3. **Competitive guilt transfer** — The final "Deepfake controversies" section pivots abruptly from Muse Image to Grok/xAI's "nudify" scandal, creating an inference chain Meta→AI images→Grok→nudify→children→lawsuit without directly accusing Meta of enabling deepfakes. The juxtaposition transfers the scandal's emotional weight.

**Key editorial choices:**
- No byline (NY Post Tech desk) — reduces accountability, presents alarm as institutional voice
- "Meta did not immediately respond" — classic no-comment implication, framing Meta as evasive
- Meta's own marketing quotes ("design a custom event invitation") positioned as ironic counterpoint to privacy alarm
- Competitor scandal section has zero direct connection to Muse Image but occupies 15% of article space

## Toolkit Results (Post-Fix)

### Entities
| Entity | Mentions |
|--------|----------|
| Meta | 22 |
| OpenAI | 2 |
| xAI | 2 |
| Google | 1 |
| X/Twitter | 1 |
| Apple | 1 |

**Primary entity:** Meta ✓ (correct — Instagram mentions cluster to Meta parent)

### Sentiment
| Dimension | Pre-Fix | Post-Fix | Notes |
|-----------|---------|----------|-------|
| raw_tone | +0.6023 | +0.6023 | VADER still inverted — instructional language dominates |
| overall_tone | +0.6023 | +0.6023 | No correction path fires |
| framing_corrected | 0.0 | 0.0 | No correction applied |
| emotional_language_intensity | **0.0** | **1.0** | **FIXED** — 30 new privacy/consent terms added |
| agency_attribution | 0.6667 | 0.6667 | High agency — Meta portrayed as active agent |
| speculative_language_ratio | 0.2066 | 0.2066 | "reportedly" contributes |
| source_authority_framing | 0.600 | 0.600 | Single corporate source |
| comparative_framing | 0.0 | 0.0 | No direct valuation comparison |

**Remaining VADER problem:** raw_tone +0.6023 is wrong for this clearly alarmist article. The failure mode is *instructional service journalism* — the opt-out walkthrough uses neutral procedural language ("tap," "scroll," "open the app") that VADER reads as positive. The alarm is carried by structural framing (consent_alarm devices, guilt transfer) and specific terms that VADER doesn't weigh negatively ("automatically enrolled," "without your knowledge"). This is a new VADER failure category distinct from the sardonic/understatement pattern (Gizmodo) and the balanced debate pattern (MarketWatch): **procedural service journalism where alarm is structural, not lexical.**

### Framing Devices (12 detected — was 3 pre-fix)
| # | Device Type | Evidence |
|---|-------------|----------|
| 1 | consent_alarm | "automatically enrolled" |
| 2 | consent_alarm | "anyone on the internet can use" |
| 3 | consent_alarm | "automatically opts-in" |
| 4 | consent_alarm | "using your likeness" |
| 5 | consent_alarm | "without your knowledge" |
| 6 | delayed_defense | First corporate response at 82% through article: "the company said" |
| 7 | no_comment_implication | "did not immediately respond" |
| 8 | consent_alarm | "automatically opted in" |
| 9 | competitive_guilt_transfer | "facing a class-action lawsuit" |
| 10 | kicker_framing | "lawsuit" |
| 11 | emotional_appeal | "children on social-media platform X" |
| 12 | competitive_guilt_transfer | "threatened to remove" |

**New device types this iteration (3):**
- **consent_alarm** — default-opt-in language framing product defaults as consent violation. 6 instances in one article. Common in privacy service journalism.
- **no_comment_implication** — non-response published as implicit evasiveness, distinct from silence_as_guilt.
- **competitive_guilt_transfer** — competitor scandal juxtaposed to transfer culpability without direct accusation.

### Missing Framing Devices (manual detection only)
| Device Type | Evidence | Why missed |
|-------------|----------|------------|
| headline_framing | "anyone" + "your" + "– here's how to opt out" | No pattern for headline-level threat-scope maximization + personal address |
| service_journalism_alarm | Entire opt-out walkthrough section | No pattern for how-to sections that implicitly position reader as needing defense |

### Sources
| # | Type | Name | Notes |
|---|------|------|-------|
| 1 | no_comment | Meta | "did not immediately respond to The Post's inquiry" |

**Missing sources:**
- Meta blog post (quoted: "design a custom event invitation...") — organizational marketing source
- Meta spokesperson ("the company said") — should be detected as organizational source
- Instagram help page (settings path described) — institutional document source
- Elon Musk / xAI (named in Grok section, not as quoted source)

### Topics
| Topic | Pre-Fix | Post-Fix | Matched Keywords (Post-Fix) |
|-------|---------|----------|------|
| privacy_data | **0.280** | **0.527** | automatically enrolled/opted in/opts-in, deepfake, how to opt out, how to turn off, nudify, opt out, opt-out, privacy, privacy investigation, public accounts, without your knowledge, your likeness |
| ai_generated_content | 0.465 | 0.465 | AI image, AI-generated, deepfake, generated image |
| product_launch | 0.309 | 0.309 | introduced, launched, rolling out |

**Fix:** privacy_data correctly promoted from 3rd (0.28) to 1st (0.527) by adding 11 consent/enrollment alarm terms to the keyword set.

## Toolkit Bugs Fixed This Iteration

### Bug 1: emotional_language_intensity = 0.0 on privacy alarm articles
**Root cause:** EMOTIONAL_LANGUAGE dictionary (941 terms) was heavily skewed toward editorial/opinion vocabulary ("worrying," "unsettling," "predatory") and entirely missing the factual-but-alarming language used in privacy service journalism.
**Fix:** Added 30 new terms across privacy/consent alarm categories: deepfake, deepfakes, deepfake controversy, nudify, nudified, class-action lawsuit, class-action, without your knowledge, without their knowledge, without your consent, without their consent, automatically enrolled, automatically opted in, automatically opts-in, automatically opted-in, auto-enrolled, use your likeness, using your likeness, use your photos, using your photos, privacy investigation, privacy probe, threatened to remove, privately threatened, controversy, controversies, lawsuit, lawsuits, class action, class actions.
**Impact:** emotional_language_intensity: 0.0 → 1.0. Dictionary: 941 → 971 terms.

### Bug 2: privacy_data topic underscored at 0.28
**Root cause:** TOPIC_KEYWORDS["privacy_data"] was missing consent-enrollment terms that appear in service journalism.
**Fix:** Added 11 terms: without your knowledge, without their knowledge, automatically enrolled, automatically opted in, automatically opts-in, your likeness, public accounts, public profiles, deepfake, deepfakes, nudify, how to opt out, how to turn off, privacy investigation, privacy probe.
**Impact:** privacy_data topic: 0.28 → 0.527 (correctly promoted to primary).

### Bug 3: Missing framing device types for privacy service journalism
**Root cause:** No patterns existed for three common editorial techniques in privacy/consent alarm articles.
**Fix:** Added 3 new device types with 4 total regex patterns:
- `consent_alarm` (1 pattern) — default-opt-in / automatic enrollment language
- `no_comment_implication` (1 pattern) — non-response framing
- `competitive_guilt_transfer` (2 patterns) — competitor scandal guilt transfer

**Impact:** Framing device detection: 3 → 12 on this article. Total device types: 98 → 101. Total patterns: 576 → 580.

## Cross-Publication Comparison: Muse Image Coverage

This is the 8th Muse Image article in the corpus. Cross-publication framing comparison:

| Publication | Framing Approach | Device Count | Primary Topic |
|-------------|------------------|-------------|------|
| Gizmodo (Jul 8) | Sardonic test-drive | 8 | product_launch |
| Fast Company (Jul 9) | Recidivism + opt-out guide | 9 | privacy_data |
| Bloomberg (Jul 9) | Financial/competitive | 6 | product_launch |
| **NY Post (Jul 10)** | **Consent alarm + guilt transfer** | **12** | **privacy_data** |
| Fox Business (Jul 10) | Teen safety / regulatory | 7 | privacy_data |
| Devdiscourse (Jul 11) | Wire service discontinuation | 4 | product_launch |
| The Tab (Jul 10) | Backlash aggregate | 5 | privacy_data |

**Observation:** NY Post has the highest framing device density of any Muse Image article, driven entirely by the new consent_alarm type (6 instances). The tabloid register amplifies privacy alarm through structural repetition rather than editorial vocabulary — a pattern VADER systematically misses because consent-violation language is lexically neutral.

## Ownership Chain: News Corp / NY Post

- **NY Post** → News Corp (Rupert Murdoch / Murdoch family trust)
- News Corp also owns: Wall Street Journal, Fox News (via Fox Corporation), HarperCollins, Dow Jones, Barron's, MarketWatch, The Times (UK), The Australian
- **Meta relationship:** News Corp signed a multi-year content licensing deal with Meta (Facebook News) in 2019, reportedly worth ~$10M/year. The deal expired/was not renewed when Meta shut down Facebook News in most markets (2023-2024). Current relationship is neutral-to-adversarial.
- **Competitive dynamics:** News Corp has content licensing deals with Google ($250M+ over 3 years, 2021) and Apple News. No known current Meta revenue relationship.
- **Editorial stance on tech:** Tabloid consumer-protection register. Tech coverage emphasizes personal threat, how-to remediation, and corporate villainy framing. Distinct from Wired's investigative posture and NYT's analytical posture.
