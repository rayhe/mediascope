# Source Analysis Quick Reference

> A compact lookup card for MediaScope's source extraction, stance analysis, outsourced intensity detection, and active-negative agency scoring. For full descriptions, detection patterns, and academic foundations, see [METHODOLOGY.md §5–§8](METHODOLOGY.md#5-source-authority-analysis).

---

## How to Use This Reference

Source analysis is the third pillar of MediaScope's editorial bias detection, alongside [framing devices](FRAMING_REFERENCE.md) and [topic classification](TOPIC_REFERENCE.md). It answers four questions about every article:

1. **Who is quoted?** → Source extraction (14 pattern groups)
2. **How credible are they?** → Source authority grading
3. **Whose side are they on?** → Source stance analysis
4. **Who carries the emotional weight?** → Outsourced intensity measurement

Run `extract_sources()` first, then pipe the results into `analyze_source_stance()` and `measure_outsourced_intensity()`. All three are in `mediascope.analyze.sources` (stance, extraction) and `mediascope.analyze.sentiment` (outsourced intensity).

---

## Part 1: Source Types

Every extracted source is tagged with a `source_type` that determines how it factors into ratio calculations and stance analysis.

| Type | Tag | Counted In Ratios? | Stance-Analyzed? | Example |
|------|-----|---------------------|-------------------|---------|
| **Named person** | `named` | ✅ Named count | ✅ | "Sarah Miller, a privacy researcher at Stanford, warned…" |
| **Anonymous** | `anonymous` | ✅ Anonymous count | ✅ | "sources familiar with the matter said…" |
| **No-comment** | `no_comment` | ❌ Excluded | ❌ | "Meta declined to comment" |
| **Organizational** | `organizational` | ✅ Named count | ✅ | "Meta said in a statement…" |
| **Documentary** | `documentary` | ❌ Excluded | ❌ | "documents obtained by The Guardian…" |
| **Group expert** | `group_expert` | ✅ Named count | ✅ | "cybersecurity experts warned in an open letter…" |
| **Collective research** | `collective_research` | ✅ Named count | ✅ | "the research team wrote…" |
| **Legal party** | `legal_party` | ✅ Named count | ✅ | "the states said they were calculating penalties…" |
| **Publication citation** | `publication_citation` | ✅ Named count | ❌ | "as first reported by Reuters…" |
| **News outlet** | `news_outlet` | ✅ Named count | ❌ | "per Bloomberg…" |

### Why No-Comment and Documentary Sources Are Excluded

**No-comment** signals (e.g., "declined to comment," "did not respond to a request for comment") are editorial markers showing the journalist attempted contact — they are not source attributions and should not inflate ratios.

**Documentary** sources (recordings, leaked documents, court filings) are material artifacts whose provenance matters but whose "stance" is undefined. They inform framing analysis but are excluded from the named/anonymous ratio. A high density of documentary sources typically indicates investigative journalism with primary-source backing.

---

## Part 2: Source Extraction Patterns

MediaScope extracts sources using 14 pattern groups, executed in priority order. Higher-priority patterns add names to a `seen_names` set, preventing lower-priority patterns from re-extracting the same person with less context.

### Named Source Patterns (Patterns 0–5)

| # | Pattern | What It Catches | Example | Priority Notes |
|---|---------|-----------------|---------|----------------|
| **0** | Title + Full Name + Verb | Government officials, chairpersons | "Governor Jeff Landry declared…" | Highest for titled names; prevents truncation to "Governor Jeff" |
| **0b** | Verb + Title + Full Name | Reverse-order titled attribution | '"A game changer," declared Governor Jeff Landry' | Catches post-quote titled attribution |
| **0c** | Name + "of" + Org + Verb | Affiliation via "of" preposition | "Justin Patterson of KeyBanc Capital said…" | Prevents org name being misidentified as person |
| **0d** | Verb + Name + "of" + Org | Reverse of 0c | "…said Justin Patterson of KeyBanc Capital" | Same benefit, reverse word order |
| **0e** | Org + Role + Name + Verb | Org-prefixed role attribution | "Morgan Stanley analyst James Faucette estimated…" | Captures org before general patterns fire |
| **1** | Name + Verb | Standard forward attribution | "Sarah Miller warned…" | Core pattern; most common in journalism |
| **2** | Verb + Name | Reverse attribution | "…said Sarah Miller" | Catches post-quote attributions |
| **2b** | Verb + Title/Role + Name | Verb then titled name | "…told Reuters correspondent Jane Smith" | Captures role context missed by Pattern 2 |
| **3** | "according to" + Name | Indirect attribution | "according to Sarah Miller…" | No verb needed — "according to" is the signal |
| **3a** | "according to" + Descriptor + Name | Titled indirect attribution | "according to privacy researcher Sarah Miller…" | Captures role/title before name |
| **3b-pre** | "per" + Source | Compact indirect attribution | "per Bloomberg…" | Short-form attribution common in financial journalism |
| **3b** | Name + Auxiliary + Verb | Auxiliary verb attribution | "Miller has argued…" | Catches "has said," "had noted," "have warned" |
| **5** | Name + Appositive + Verb | Appositive clause attribution | "Sarah Miller, a Stanford researcher, warned…" | Handles the journalism convention of role in commas |
| **5b** | LastName + Verb | Single-surname attribution | "Miller says…" | For subsequent references after full name established |
| **5c** | Verb + LastName | Reverse single-surname | "…says Miller" | Reverse of 5b |

### Special Source Patterns (Patterns 4, 6–11)

| # | Pattern | Type Tag | What It Catches | Key Signals |
|---|---------|----------|-----------------|-------------|
| **4** | Anonymous sources | `anonymous` | Unnamed sources with various descriptors | "sources say," "people familiar with," counted patterns ("two employees said"), role descriptors ("a policy staffer says"), social media users ("said one X user") |
| **6** | Organizational sources | `organizational` | Companies/entities as speakers | "Meta said," "a Google spokesperson told," self-validating constructions ("analysts with SemiAnalysis estimated") |
| **7** | Group expert sources | `group_expert` | Named collective expert groups | "cybersecurity experts warned in an open letter," "leading AI researchers argued" |
| **8** | Collective research | `collective_research` | Research team attributions | "the team wrote," "researchers explained," "the authors noted" |
| **9** | Documentary sources | `documentary` | Artifacts cited as evidence | "documents obtained by The Guardian," "court records show," "the filing states" |
| **10** | Legal party sources | `legal_party` | Collective legal actors | "the states said," "prosecutors argued," "the attorneys for Meta claimed" |
| **11** | Publication citations | `publication_citation` | Other outlets cited as authority | "The Verge first pointed out," "as first reported by Reuters" |

### No-Comment Detection

Separate from the 14 extraction patterns, no-comment signals are detected and tagged `source_type="no_comment"`:

| Signal | Example |
|--------|---------|
| Declined/refused | "Meta declined to comment" |
| Did not respond | "did not respond to a request for comment" |
| Reached out | "Fox Business reached out to Meta for further comment" |
| Has contacted | "has contacted the company for a statement" |
| Could not be reached | "could not be reached for comment" |

---

## Part 3: Source Authority Grading

All factual claims must cite a source. Sources are graded by reliability:

| Grade | Weight | Type | Examples |
|-------|--------|------|----------|
| **Primary** | 1.0 | Original documents and records | SEC filings, court records, .gov databases, corporate 10-K/10-Q, published research papers, official press releases |
| **Secondary** | 0.8 | Professional reporting by credible outlets | Reuters, AP, WSJ, NYT, Bloomberg, Financial Times |
| **Tertiary** | 0.4 | Opinion, analysis, social media | Blogs, Substack, Twitter/X posts, opinion sections, Wikipedia |

### Anonymous Source Ratio Thresholds

| Ratio | Assessment | Action |
|-------|------------|--------|
| < 20% | Normal | Most sources identified |
| 20–40% | Elevated | Flag; significant anonymous sourcing |
| 40–60% | High | Majority claims rest on anonymous sources |
| > 60% | Extreme | Article is substantially unverifiable |

### Counted Anonymous Sources

A harder pattern to detect: "two employees said," "three people familiar with." These create an illusion of transparency without revealing identity. MediaScope's `extract_sources()` catches them via role-descriptor patterns, reverse-order attribution, and structural heuristics. Discovered via NYT Meta "Arena" article where 100% of sourcing was anonymous via counted patterns but original regex-only counter reported 0%.

---

## Part 4: Source Stance Analysis

### The Question

Source authority (Part 3) answers: "How credible are these sources?" Source *stance* answers a different question: **"Whose side are these sources on?"**

An article can score perfectly on source authority (all named, all expert-credentialed) while deploying every source to undermine the subject entity. This is **adversarial source deployment** — assembling a one-sided roster of critics, each individually credible, to construct a unanimously negative framing.

### Stance Classification

For each extracted source:

1. **Quote content analysis:** Scanned for negative stance terms (harmful, reckless, censorship, exploitation) and positive stance terms (innovative, beneficial, safe, transparent)
2. **Attribution verb weighting:** Adversarial verbs (warned, blasted, accused, fumed) contribute +1 to negative stance
3. **Classification:** Negative > Positive → adversarial. Positive > Negative → supportive. Otherwise → neutral.

### Stance Balance Metric

```
stance_balance = (supportive_count − adversarial_count) / (supportive_count + adversarial_count)
```

| Score | Interpretation |
|-------|---------------|
| −1.0 | All sources positioned against the subject |
| −0.5 | ~75% adversarial |
| 0.0 | Balanced source deployment |
| +0.5 | ~75% supportive |
| +1.0 | All sources validate/defend the subject |

### The Analytical Power Quadrant

The most analytically interesting articles combine authority and stance:

| Authority | Stance | Interpretation | Red Flag? |
|-----------|--------|----------------|-----------|
| High | Balanced | Professional, balanced reporting | ✅ Gold standard |
| High | Adversarial | Credible but one-sided sourcing | ⚠️ Sophisticated editorial bias |
| Low | Adversarial | Anonymous pile-on | 🔴 Low-quality attack |
| Low | Balanced | Poorly sourced but neutral | ⚠️ Lazy reporting |

**The "High authority + Adversarial stance" combination is the hallmark of sophisticated editorial bias** — it looks like rigorous journalism because every source is named and credentialed, but the roster is editorially curated to present only one perspective.

---

## Part 5: Outsourced Intensity

### The Technique

"Outsourced intensity" is the editorial practice of maintaining measured, professional prose in the journalist's own voice while deploying emotionally charged quotes from sources. The byline text reads as neutral; the emotional impact comes entirely from quotes. This provides plausible objectivity while framing coverage adversarially.

**Real example (Guardian, Jun 2026):**
> The strongest language — "censorship," "despotic," "hostage," "asshole" — all comes from quotes, not the journalist.

### Detection Method

Article text is split into **quoted segments** (within quotation marks) and **editorial prose** (everything else). Emotional language intensity is measured independently in each:

```
outsourced_ratio = 1 − (editorial_intensity / quoted_intensity)
```

| Outsourced Ratio | Interpretation |
|-----------------|----------------|
| 0.0 | No outsourcing — editorial prose equally or more emotional |
| 0.3–0.5 | Moderate — quotes carry somewhat more emotion |
| 0.5–0.8 | Significant — emotional impact primarily via source quotes |
| 0.8–1.0 | High — virtually all emotional language is in quotes |

### Combined Signal

When `outsourced_ratio > 0.5` AND `stance_balance < −0.5`, the article uses the most sophisticated form of editorial bias: measured prose that reads as professional journalism, with adversarial framing entirely delegated to a one-sided source roster. This defeats both lexical sentiment analysis (VADER sees neutral prose) and casual reader assessment ("the journalist is just reporting what sources said").

---

## Part 6: Active-Negative Agency Detection

### The Problem

VADER's lexical model cannot distinguish "Meta is tracking users across apps" (negative agency — Meta is the active agent of a harmful action) from "Meta is expanding its user base" (positive agency). Both use active-verb constructions with the entity as subject. The sentiment difference lies in whether the verb implies harm, coercion, or surveillance.

### Active-Negative Verb Categories

| Category | Example Verbs | Typical Context |
|----------|---------------|-----------------|
| **Surveillance** | tracking, monitoring, surveilling, snooping, scraping | Privacy/data coverage |
| **Coercion** | forcing, pressuring, strong-arming, compelling, requiring | Workforce/policy coverage |
| **Exploitation** | exploiting, extracting, harvesting, mining, commodifying | Data/labor coverage |
| **Destruction** | cutting, slashing, gutting, eliminating, laying off | Workforce coverage |
| **Deception** | misleading, deceiving, concealing, obscuring, obfuscating | Regulatory/legal coverage |

### Impact on Tone Correction

Active-negative agency is one of three conditions (alongside adversarial framing density ≥3 and positive raw VADER score) that trigger the framing-aware tone correction pipeline. See [SENTIMENT_CORRECTION_REFERENCE.md](SENTIMENT_CORRECTION_REFERENCE.md) for a quick-reference card covering all 12 correction paths (A–L), or [METHODOLOGY.md §9](METHODOLOGY.md#9-framing-aware-tone-correction) for the full theory.

---

## Part 7: Zero Named Sources Flag

When no named human source can be detected in an article, the quality check emits a `zero_named_sources` warning with a **−12 score penalty**. This catches:

- Articles sourced entirely from unnamed "experts" or "sources say"
- Opinion pieces disguised as reporting (all claims are unsourced assertions)
- Secondary-source repackaging that quotes other publications instead of individuals

### Detection Patterns (4 regex patterns)

| Pattern | Example |
|---------|---------|
| Post-attribution | "…said Sarah Miller" |
| Pre-attribution | "Sarah Miller said/told/noted…" |
| According-to | "according to Sarah Miller…" |
| Title-based | "Sarah Miller, a senior analyst…" |

### Genre Sensitivity

Wire-service factsheets (Reuters, AP) legitimately have zero named sources — they often use organizational attribution ("the company said"). For wire-format articles, this warning is **informational, not a quality failure**. For editorial articles, zero named sources is a significant concern.

---

## Part 8: Common Failure Modes & Edge Cases

### Known Extraction Failures

| Failure | Root Cause | Mitigation | Discovery |
|---------|------------|------------|-----------|
| Q&A format → zero sources | No standard attribution verbs in interview format | Manual annotation required | METHODOLOGY.md §18.4 |
| "Called [Name]" false positive | "a model called Mythos" parsed as "Mythos said" | Naming-construction lookbehind filter | General QA |
| Product names as sources | "Meta Glasses" extracted as source | Product-name stop-filter in `_NAME_STOP_NAMES` | Multiple articles |
| Org name as person | "KeyBanc Capital" → person "Capital" | Pattern 0c (Name of Org Verb) runs before Pattern 1 | WSJ AI spending (Jul 2026) |
| Possessive publications | "told Barron's" → person "Barron" | Possessive-form skip on apostrophe after match end | Barron's articles (Jul 2026) |
| Conditional attribution | "once Meta acknowledges defeat" | Speculative-lookbehind filter (if/when/once/should/could) | IBD article (Jul 2026) |
| Counted anonymous = zero | "two employees said" invisible to simple regex | Dedicated counted-source patterns with number words | NYT Arena article |
| Corporate PR VADER inflation | "heard the feedback," "missed the mark" scores positive | Documented limitation — no current mitigation for ultra-short articles | Reuters Muse Image discontinuation (Jul 2026) |

### Self-Validating Organizational Patterns

Two source extraction patterns are **self-validating** — their syntactic construction inherently indicates an organizational source without requiring membership in `_KNOWN_ORGS`:

1. `"Analysts with/at/from [Org] verb"` → extracts the org name
2. `"[Org] analysts verb"` → extracts the org name

These were added because research/analyst firm names (SemiAnalysis, Erste Group) were invisible when not pre-listed. The self-validating approach handles new firms automatically.

---

## Part 9: CLI Quick Reference

```bash
# Full pipeline: extract → stance → outsourced intensity
mediascope analyze --publication wired --target Meta --since 2026-01-01

# Python API
from mediascope.analyze.sources import extract_sources, analyze_source_stance
from mediascope.analyze.sentiment import measure_outsourced_intensity

sources = extract_sources(article_text)
stance = analyze_source_stance(sources, "Meta", full_text=article_text)
outsourced = measure_outsourced_intensity(article_text)

# Key outputs
print(f"Named: {stance.named_count}, Anonymous: {stance.anonymous_count}")
print(f"Stance balance: {stance.stance_balance:.2f}")  # -1.0 to +1.0
print(f"Outsourced ratio: {outsourced.outsourced_ratio:.2f}")  # 0.0 to 1.0
```

### Function Calling Schema

```json
{
    "name": "extract_sources",
    "description": "Extract all source citations from article text: named persons, anonymous sources, organizations, documentary evidence, legal parties, expert groups, and publication citations.",
    "parameters": {
        "type": "object",
        "properties": {
            "text": { "type": "string", "description": "Full article text" }
        },
        "required": ["text"]
    }
}
```

```json
{
    "name": "analyze_source_stance",
    "description": "Classify each source's stance toward the subject entity (adversarial/supportive/neutral) and compute stance_balance (-1.0 to +1.0).",
    "parameters": {
        "type": "object",
        "properties": {
            "article_text": { "type": "string", "description": "Full article text" },
            "target_entity": { "type": "string", "description": "Entity name for context-aware stance detection" }
        },
        "required": ["article_text"]
    }
}
```

```json
{
    "name": "measure_outsourced_intensity",
    "description": "Measure how much emotional language is outsourced to quoted sources vs. editorial prose. Returns outsourced_ratio from 0.0 (no outsourcing) to 1.0 (all emotion in quotes).",
    "parameters": {
        "type": "object",
        "properties": {
            "article_text": { "type": "string", "description": "Full article text" }
        },
        "required": ["article_text"]
    }
}
```

---

## Part 10: Interaction with Other Subsystems

| Subsystem | How Source Analysis Feeds It |
|-----------|-----------------------------|
| **Framing device detection** | `outsourced_intensity` is both a framing device (§4.1) and a quantitative metric (§7). `expert_contradiction`, `analyst_authority`, and `anonymous_authority` are framing devices whose evidence comes from source extraction. |
| **Tone correction pipeline** | Active-negative agency (Part 6) + adversarial framing density + positive raw VADER → correction Paths A–J fire. Source stance provides the agency signal. |
| **Same-event comparison** | Source roster (named vs. anonymous, count, affiliations), source stance balance, and outsourced intensity ratio are 3 of the 7 comparison dimensions. |
| **Quality standards** | Zero named sources flag (Part 7) is a quality check. `sourced_ratio` from claims-evidence mapping uses source extraction. |
| **Genre-aware analysis** | Wire services have near-zero framing devices and balanced stance; sardonic editorials have extreme outsourced intensity. Genre classification adjusts interpretation thresholds. |

---

*Last updated: 2026-07-11. 14 extraction pattern groups, 10 source types, 4 analysis dimensions. See [METHODOLOGY.md §5–§8](METHODOLOGY.md#5-source-authority-analysis) for the full framework.*
