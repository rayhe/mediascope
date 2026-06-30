# MIT Technology Review: Chinese tech workers are starting to train their AI doubles — and pushing back

**Publication:** MIT Technology Review
**Date:** April 20, 2026
**Author:** MIT Technology Review staff (byline not specified in accessible version)
**Topic:** Worker AI displacement / workplace culture
**Word count:** ~1,000
**URL:** https://www.technologyreview.com/2026/04/20/1136149/chinese-tech-workers-ai-colleagues/

---

## Manual Analysis

### Summary

Feature-length piece exploring the Colleague Skill GitHub project — a tool that "distills" coworkers' skills and personality traits into AI agent workflows — and the backlash it generated among Chinese tech workers. The article balances reporting on the viral tool (created as a spoof by Tianyi Zhou at Shanghai AI Laboratory) with worker reactions ranging from existential discomfort (Amber Li) to organized resistance (Koki Xu's "anti-distillation" tool). An academic source (Hancheng Cao, Emory University) provides the corporate rationalization perspective.

### Tone Assessment

**Manual tone: -0.10 to 0.00 (neutral with sympathetic-to-workers lean)**

The article is not adversarial toward any specific company (no Meta, no Google, no named corporate villain). Its editorial sympathy lies clearly with the workers, expressed through:
- Word choices: "soul-searching," "alienating," "uncanny and uncomfortable," "bleak humor," "value is being cheapened"
- Structural emphasis: the corporate perspective gets one paragraph (Hancheng Cao), while worker resistance gets three paragraphs (anonymous engineer, Koki Xu, Amber Li's closing)
- The closing quote — "I feel that my value is being cheapened, and I don't know what to do about it" — is a classic kicker that leaves the reader with the workers' existential anxiety, not the corporate efficiency argument

This is not a neutral article. It is sympathetically framed toward labor. But it is not hostile to any named entity — it treats the phenomenon itself as the subject, not a corporation.

### Entities Mentioned

| Entity | Role in Article | Sentiment Toward |
|--------|----------------|-----------------|
| Colleague Skill (GitHub) | Central subject | Presented as provocative/concerning |
| OpenClaw | Background (AI agent platform) | Neutral mention |
| Claude Code | Background (AI agent tool) | Neutral mention |
| Lark / DingTalk | Background (workplace apps) | Neutral mention |
| Shanghai AI Laboratory | Employer of creator | Neutral mention |
| Southern Metropolis Daily | Source credit | Neutral |
| Emory University | Employer of academic source | Neutral |
| GitHub | Platform mention | Neutral |
| Rednote | Social media platform | Neutral |

**Note:** No Meta, Google, Apple, or other tracked company appears in this article. It is not a company-coverage piece — it covers a labor/technology phenomenon.

### Sources

| Source | Type | Affiliation | Stance |
|--------|------|-------------|--------|
| Tianyi Zhou | Named | Shanghai AI Laboratory, Colleague Skill creator | Neutral (declined further comment) |
| Amber Li, 27 | Named | Tech worker, Shanghai | Sympathetic to workers (used tool, found it "uncanny") |
| Hancheng Cao | Named | Asst. Prof., Emory University | Corporate rationalization ("firms gain richer data on employee know-how") |
| Anonymous software engineer | Anonymous | Unnamed company | Anti-commodification ("felt reductive," "flattened into modules") |
| Koki Xu, 26 | Named | AI product manager, Beijing | Anti-distillation advocate, worker resistance |
| Anonymous Rednote user | Anonymous (social media) | Not applicable | Bleak humor ("a cold farewell can be turned into warm tokens") |

**Source balance:** 4 worker-sympathetic sources vs. 1 corporate-perspective source vs. 1 neutral (creator). Heavily weighted toward worker perspective. Academic source (Cao) is the only voice offering the corporate argument, and his quote is immediately followed by "To employees, though, making agents or even blueprints for them can feel strange and alienating" — a editorial pivot back to the worker frame.

### Framing Devices (Manual)

| Device | Count | Evidence |
|--------|-------|---------|
| **commodification_metaphor** | 5+ | "distill their colleagues' skills and personality traits," "flattened into modules in a way that made the worker easier to replace," "a cold farewell can be turned into warm tokens," "reducing a person to a skill," "digital" coworker concept |
| **worker_replacement_irony** | 2 | Headline: "train their AI doubles—and pushing back." Body: workers training AI on their own workflows, implicitly building their replacements |
| **pressure_language** | 1-2 | "bosses in China have been pushing tech workers to experiment," "being instructed by their bosses to train AI agents to replace them" |
| **loaded_language** | 2-3 | "soul-searching," "alienation, disempowerment," "value is being cheapened" — labor solidarity vocabulary |
| **kicker_framing** | 1 | Final quote: "I feel that my value is being cheapened, and I don't know what to do about it" — leaves reader with workers' unresolved anxiety |

**Not present:** ironic_quotation (quotes around "distill," "coworker," and "anti-distillation" are explanatory scare quotes for introducing technical/novel terms, not editorial undermining of sources' claims)

---

## Toolkit Analysis

### Topics

| Topic | Confidence | Matched Keywords |
|-------|-----------|-----------------|
| **worker_ai_displacement** | 0.595 | alienating, alienation, anti-distillation, automate themselves, countermeasures, disempowerment, easier to replace, flattened into modules, replace them, replacing coworkers, sabotage, value is being cheapened |
| **workplace_culture** | 0.457 | employees, layoffs, workers, workplace |
| **ai_development** | 0.322 | AI agent, AI agents, artificial intelligence |

**Assessment: ✅ Excellent.** `worker_ai_displacement` correctly identified as primary topic. This article is exactly the kind of content the new topic bucket was designed for. 12 keyword matches with high relevance. The `workplace_culture` secondary topic is reasonable (the article does discuss workplace dynamics).

### Sentiment

| Dimension | Score | Assessment |
|-----------|-------|-----------|
| overall_tone | +0.624 | ❌ **Too positive.** Manual: ~0.0. Article has neutral reportorial tone but clear sympathetic framing toward workers. |
| emotional_language_intensity | 0.000 | ❌ **Should be ~0.3-0.4.** "Soul-searching," "alienation," "disempowerment," "uncanny and uncomfortable," "bleak humor," "cheapened" are all emotionally loaded. |
| source_authority_framing | 0.600 | ⚠️ Reasonable — mix of named workers and one academic. |
| agency_attribution | 1.000 | ⚠️ High — possibly not calibrated for labor articles where the "agents" are both AI tools and human actors. |
| anonymous_source_ratio | 0.000 | ❌ **Should be >0.** Article has one explicitly anonymous source ("who spoke with MIT Technology Review anonymously because of concerns about job security"). |
| speculative_language_ratio | 0.201 | ✅ Reasonable — article does use hedging ("could become a norm," "largely because they remain unreliable"). |
| comparative_framing | -1.000 | ⚠️ Default/absence value — no comparative framing detected (correct). |
| raw_tone → framing_corrected | 0.624 → False | ❌ No framing correction applied despite 10 detected framing devices. |

**Key sentiment gaps:**
1. **VADER positive bias on feature-style articles.** VADER compound = 0.995 (extremely positive), driven by the neutral/professional reporting language. VADER doesn't register the underlying concern conveyed through word choice and structure.
2. **Emotional intensity detector missing labor/dignity vocabulary.** Terms like "alienation," "disempowerment," "soul-searching," "cheapened," "bleak humor" are emotionally loaded but apparently not in the emotional_language word lists.
3. **Anonymous source detection failure.** The explicit anonymity clause ("who spoke... anonymously because of concerns about job security") was not detected, possibly because the source is introduced with "One software engineer" (count + occupation) rather than the standard "a person familiar" pattern.

### Framing Devices

| Device | Toolkit Count | Manual Count | Assessment |
|--------|-------------|-------------|-----------|
| commodification_metaphor | 5 | 5+ | ✅ **Excellent.** All 5 are true positives. This is the source article for the pattern. |
| ironic_quotation | 3 | 0 | ❌ **3 false positives.** Triggered by scare quotes around "distill," "coworker," and "anti-distillation" — these are explanatory/technical quotes introducing novel terms, not editorial undermining of sources. |
| pressure_language | 1 | 1-2 | ✅ "pushing tech workers to" correctly detected. |
| worker_replacement_irony | 1 | 2 | ⚠️ Caught one instance but missed the structural irony in the headline and the broader framing of workers building their own replacements. |
| loaded_language | 0 | 2-3 | ❌ **Missed.** "Soul-searching," "alienation, disempowerment," "value is being cheapened" should register. |
| kicker_framing | 0 | 1 | ❌ **Missed.** The closing quote is a textbook kicker leaving the reader with unresolved worker anxiety. Should be within the ~400 char check range. |

**Ironic quotation false positive analysis:** The `ironic_quotation` pattern detects quoted words/phrases followed or preceded by editorial undermining. But for this article, the quotes serve a different function — introducing technical neologisms ("distill" as a metaphor for skills extraction, "coworker" as a sarcastic self-label for AI, "anti-distillation" as a coined term). The pattern needs a distinction between:
- **Editorial ironic quotation:** Quote + "But/Yet/In reality" or verdict → undermining
- **Technical scare quotes:** Quote introducing a new/unfamiliar term → neutral

### Source Extraction

| Toolkit Found | Assessment |
|---------------|-----------|
| Colleague Skill (named) | ❌ **False positive** — this is a software tool, not a human source |
| Hancheng Cao (named) | ✅ Correct |
| She (named) | ❌ **Extraction failure** — should be "Koki Xu" (pronoun extracted instead of name) |
| Colleague (named) | ❌ **False positive** — not a source, just a word |

| Missing Sources | Type |
|----------------|------|
| Amber Li | Named — quoted multiple times |
| Tianyi Zhou | Named — quoted via Southern Metropolis Daily |
| Koki Xu | Named — quoted directly, multiple paragraphs |
| Anonymous software engineer | Anonymous — explicitly anonymous |

**Source extraction has 4 false positives/errors and 4 missed sources out of 6 actual sources.** The extractor is likely tuned for Western article formats with "X said/told/says" patterns and struggling with this article's structure, which introduces sources with context before attribution (e.g., "Amber Li, 27, a tech worker in Shanghai, used it to...").

---

## Toolkit Gaps Identified

### Priority 1: Emotional Intensity Vocabulary

The emotional_language_intensity detector does not include labor/dignity vocabulary:
- **Missing terms:** alienation, disempowerment, soul-searching, cheapened, dehumanizing, uncanny, bleak, existential, reductive, unsettling
- **Impact:** Articles about worker displacement will score 0.0 on emotional intensity despite being heavily emotionally framed
- **Recommendation:** Add a "labor_dignity" cluster to the emotional intensity word list

### Priority 2: Anonymous Source Detection Pattern

The anonymous source detection misses "One [occupation], who spoke with [publication] anonymously because of [reason]" — a legitimate anonymous source pattern that uses a count word + job title instead of the standard "a person familiar with" construction.

### Priority 3: Ironic Quotation False Positive Suppression

The ironic_quotation detector needs a heuristic to suppress matches where:
- The quoted term appears only once in the article (introducing it)
- No editorial "But/Yet/however/in reality" follows within ~30 words
- The quote is a technical/novel term not previously used in unquoted form

### Priority 4: Source Extraction for Non-Western Article Formats

Source extraction misses names introduced through contextual description before attribution verb. Pattern: "Name, age, a [occupation] in [location], [action verb]... 'quote' Name says." Both "Amber Li, 27, a tech worker in Shanghai" and "Koki Xu, 26, an AI product manager in Beijing" were missed.

### Priority 5: VADER Positive Bias on Feature Articles

VADER consistently scores feature-length articles as positive (compound = 0.995) because neutral reportorial prose has slightly positive language. This article is clearly concerned/sympathetic, not positive. Consider a genre-aware correction that dampens VADER's positive bias when:
- Topic is `worker_ai_displacement` or `workplace_culture`
- Multiple `commodification_metaphor` or `loaded_language` devices are present
- The kicker is negative in tone

---

## Cross-Publication Value

This article has no direct comparison to other publications covering the same event (Colleague Skill was primarily covered in Chinese-language media). However, it serves as a critical test case for the `worker_ai_displacement` topic bucket and `commodification_metaphor` framing device, and exposes significant gaps in sentiment scoring for labor/dignity articles that are sympathetically framed without being overtly adversarial.

**Analytical significance for DiD research:** This article was written by MIT Technology Review staff, not a named journalist, which limits its utility for individual journalist framing analysis. However, the institutional framing — sympathetic to workers, skeptical of corporate automation, structurally weighted toward resistance narratives — provides a baseline for MIT TR's editorial posture on labor displacement topics.
