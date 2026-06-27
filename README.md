# MediaScope

**Open-source toolkit for tracking editorial bias, ownership conflicts, and coverage asymmetry in media publications.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

---

## The Problem

Media publications have undisclosed financial conflicts of interest that systematically bias their coverage. Parent companies hold investments in competitors, sign licensing deals with some tech companies and not others, and maintain board seats in the companies they cover — all without disclosing these relationships to readers.

**MediaScope** is transparency infrastructure. It gives journalists, researchers, and AI agents the tools to systematically detect, measure, and disclose coverage asymmetry driven by ownership and financial conflicts.

This is not an attack tool. It works equally well pointed at Fox News covering renewable energy, the New York Times covering AI, or Wired covering Meta. The methodology is publication-agnostic and statistically rigorous.

## What It Does

1. **Ingests articles** from any publication via RSS feeds and web scraping
2. **Detects entities** mentioned in coverage (companies, executives, products)
3. **Analyzes sentiment** using an 8-dimension scoring framework (not just positive/negative)
4. **Calculates asymmetry** — is Company X covered more negatively than peers, with statistical significance?
5. **Maps ownership conflicts** — who owns the publication, what are their financial interests?
6. **Tracks litigation funding** — who profits from lawsuits against covered companies?
7. **Generates disclosure statements** — ready-to-post conflict of interest disclosures
8. **Produces reports** — weekly Markdown reports and HTML dashboards
9. **Tracks editorial histories** — journalist migrations between publications as causal signal for bias attribution **(novel contribution — no prior work does this)**
10. **Detects outsourced intensity** — when journalists outsource emotional language to quotes while keeping prose neutral **(new)**
11. **Analyzes source stance** — measures whether sources are deployed adversarially or supportively, beyond just named/anonymous **(new)**
12. **Detects power asymmetry framing** — editorial device positioning institutional power against individual vulnerability **(new)**
13. **Active-negative agency detection** — distinguishes "actively doing harmful things" (tracking, cutting, forcing) from positive active agency (launching, innovating) **(new)**
14. **Framing-aware tone correction** — when VADER scores factual investigative prose as positive but framing devices signal adversarial editorial stance, overrides with framing-derived tone **(new)**
15. **Source extraction stop-word filtering** — prevents false-positive extractions like "After Meta said" → source "After Meta" **(new)**

## ✨ Novel: Editorial Histories

MediaScope's most original contribution is the **Editorial Histories** module. When a journalist moves from Publication A to Publication B, it creates a natural experiment:

- **Does Publication A's coverage change after they leave?** → Institutional vs. individual bias
- **Does the journalist's tone change at Publication B?** → Editorial capture vs. portable bias
- **Does Publication B shift after they arrive?** → Measures the journalist's editorial influence

This is a [difference-in-differences](https://en.wikipedia.org/wiki/Difference_in_differences) approach (Card & Krueger, 1994) applied to media analysis. No prior work applies DiD to journalist-level editorial migration data at scale. See [docs/EDITORIAL_HISTORIES.md](docs/EDITORIAL_HISTORIES.md) for the full methodology.

```bash
# List tracked journalists and their migrations
mediascope careers list
mediascope careers migrations

# Run DiD analysis on a journalist's move
mediascope careers diff "Karen Hao" --window 180

# Decompose a journalist's bias into institutional vs. individual
mediascope careers analyze "Karen Hao"

# Show leadership changes that may have shifted coverage
mediascope careers leadership wired
```

Ships with verified career data for **90 journalists** across 130+ publications, including high-value migrations like Karen Hao (MIT Tech Review → Atlantic), Cade Metz (Wired → NYT), Zoë Schiffer (The Verge → Platformer → Wired), Zeyi Yang (MIT Tech Review → Wired), Melissa Heikkilä (MIT Tech Review → Financial Times), Emily Mullin (MIT Tech Review → Wired), David McCabe (Axios → NYT), Stuart A. Thompson (WSJ → NYT), David Yaffe-Bellany (Bloomberg → NYT), Erin Griffith (Fortune → Wired → NYT), and Hugo Lowell (Guardian → Wired).

## Quick Start

```bash
# Install
pip install mediascope

# Or from source
git clone https://github.com/mediascope/mediascope.git
cd mediascope
pip install -e .

# Download spaCy model
python -m spacy download en_core_web_sm

# List available publication profiles
mediascope list-publications

# Run analysis on Wired's coverage of Meta
mediascope ingest --publication wired --since 2025-01-01
mediascope analyze --publication wired --target Meta
mediascope score --publication wired --target Meta

# Generate a conflict disclosure statement
mediascope disclose --publication wired --target Meta

# Generate a full weekly report
mediascope report --publication wired --target Meta --format md

# Generate an HTML dashboard
mediascope report --publication wired --target Meta --format html
```

## Example Output

### Asymmetry Scores

```
Publication: Wired (wired.com)
Target Entity: Meta
Analysis Period: 2025-01-01 to 2025-06-15
Articles Analyzed: 47 (Meta), 312 (peers)

ASYMMETRY SCORES (negative = more negative coverage of target vs peers)
──────────────────────────────────────────────────────────────────────
Entity          Avg Tone    Articles    Asymmetry    p-value    Effect
──────────────────────────────────────────────────────────────────────
Meta            -0.342      47          —            —          —
Google          -0.098      89          -0.244       0.003**    medium
Apple           +0.051      72          -0.393       <0.001***  large
Amazon          -0.121      56          -0.221       0.008**    medium
Microsoft       -0.067      95          -0.275       0.001**    medium
──────────────────────────────────────────────────────────────────────
Overall Asymmetry: -0.283 (p < 0.001, Cohen's d = 0.71)

** p < 0.01   *** p < 0.001
```

### Conflict Disclosure

```
CONFLICT OF INTEREST DISCLOSURE — Generated by MediaScope v0.1.0

Publication: Wired (wired.com)
Owner: Condé Nast → Advance Publications (Newhouse Family)

FINANCIAL CONFLICTS (5 identified):
1. [SEVERITY 5] Advance Publications holds 33.5% voting power in Reddit,
   a direct Meta competitor, with 2 board seats and ~$2B IPO gain.
2. [SEVERITY 5] Condé Nast has content licensing deals with OpenAI, Amazon,
   and Apple (all Meta competitors). Meta has NO such deal.
3. [SEVERITY 4] Reddit competes directly with Meta for user attention,
   advertiser spend, and community engagement.

METHODOLOGY: Ownership data from SEC filings and corporate disclosures.
Revenue relationships from press releases and industry reporting.
Full methodology: https://github.com/mediascope/mediascope/blob/main/docs/METHODOLOGY.md
```

## Architecture

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│   INGEST    │───▶│   ANALYZE    │───▶│    SCORE    │───▶│    REPORT   │
│             │    │              │    │             │    │              │
│ • RSS feeds │    │ • Entities   │    │ • Asymmetry │    │ • Weekly MD  │
│ • Scraping  │    │ • Sentiment  │    │ • Welch's t │    │ • Dashboard  │
│ • Archives  │    │ • Framing    │    │ • Cohen's d │    │ • Disclosure │
│             │    │ • Sources    │    │ • Bootstrap │    │              │
└─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘
                                                                │
┌─────────────┐    ┌──────────────┐    ┌──────────────┐         │
│  CONFLICTS  │───▶│   QUALITY    │◀───│   CAREERS    │─────────┘
│             │    │              │    │  (novel)     │
│ • Ownership │    │ • Citations  │    │ • Migrations │
│ • Revenue   │    │ • Claims     │    │ • DiD causal │
│ • Litigation│    │ • Standards  │    │ • Bias decomp│
│ • Disclosure│    │ • AI slop    │    │ • Leadership │
└─────────────┘    └──────────────┘    └──────────────┘
```

## Publication Profiles

MediaScope ships with detailed profiles for five publications, chosen to illustrate different conflict patterns:

| Publication | Owner | Conflict Type | Key Conflict |
|---|---|---|---|
| **Wired** | Advance Publications | Financial + Competitive | 33.5% Reddit stake, AI licensing with Meta's competitors |
| **NY Times** | Sulzberger Family | Litigation | Suing OpenAI while building AI internally |
| **The Guardian** | Scott Trust (non-profit) | Partial control | OpenAI + ProRata licensing deals, but no equity in specific competitors. Closest to baseline in the 5-pub set (pre-Feb 2025 coverage cleaner). |
| **The Atlantic** | Emerson Collective (LPJ) | Investment + Licensing + Civic | Owner holds ~$16B Apple stock, $6.5B OpenAI equity exit, co-chairs civic org with Google/Alphabet president and OpenAI CEO |
| **MIT Tech Review** | MIT | Institutional paradox | Parent receives $500M+ from companies it covers |

Add your own with `mediascope add-publication` or copy `profiles/_template.yaml`.

## Agent Integration

MediaScope is designed for use by AI agents. See [docs/AGENT_GUIDE.md](docs/AGENT_GUIDE.md) for:

- Function-calling schemas for each command
- Input/output JSON formats
- Sample agent prompts
- Integration patterns for LangChain, CrewAI, AutoGen, and raw function calling

```python
# Minimal agent integration
from mediascope.config import load_profile
from mediascope.ingest.rss import fetch_all_feeds
from mediascope.analyze.entities import detect_entities
from mediascope.analyze.sentiment import analyze_composite
from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.conflicts.disclosure import generate_disclosure

profile = load_profile("wired")
articles = fetch_all_feeds(profile)
# ... analyze, score, disclose
```

## Quality Standards

MediaScope enforces rigorous quality standards on all generated output:

- **Every factual claim requires a verifiable source.** Primary sources (SEC filings, court records) preferred.
- **No AI slop.** Banned phrase detection catches "delve," "tapestry," "landscape," and 20+ other markers.
- **Strongest counterargument required.** Every analysis must address the best argument against its thesis.
- **Limitations section required.** What the analysis cannot prove, where evidence is circumstantial.
- **Source grading.** Primary > Secondary > Tertiary, with automated classification.

See [docs/QUALITY_STANDARDS.md](docs/QUALITY_STANDARDS.md) for the full standard.

## Methodology

Statistical methodology is documented at academic quality in [docs/METHODOLOGY.md](docs/METHODOLOGY.md), citing:

- Microsoft Research Media Bias Detector (CHI 2025)
- BABE dataset (Spinde et al. 2022)
- Bunz & Braghieri 2021 (AI coverage sentiment analysis)
- Welch's t-test, Cohen's d, bootstrap confidence intervals
- 8-dimension sentiment scoring framework

## Contributing

Contributions welcome. Priority areas:

1. **New publication profiles** — the more publications tracked, the more useful the tool
2. **Improved NER** — better entity detection for non-English publications
3. **Transformer models** — fine-tuned bias detection models
4. **Visualization** — better dashboard charts and graphs
5. **API integrations** — direct feeds from media monitoring services

### Adding a Publication

```bash
# Interactive profile creation
mediascope add-publication --name "Fox News" --slug fox-news --url https://www.foxnews.com --interactive

# Or copy the template
cp profiles/_template.yaml profiles/fox-news.yaml
# Edit with your publication data
```

See [docs/ADDING_PUBLICATIONS.md](docs/ADDING_PUBLICATIONS.md) for detailed instructions.

## Troubleshooting

### Common Issues

**`get_primary_entity()` returns `None` for valid text**

The entity detector uses word-boundary matching, so it won't match entities embedded in compound words or hyphenated terms. If your target entity appears as part of a larger word (e.g., "MetaQuest" without a space), add it as an explicit alias:

```python
from mediascope.analyze.entities import detect_entities
entities = detect_entities(text, clusters={
    "Meta": {"aliases": ["Meta", "MetaQuest", "Meta Quest"], "regex": r"\b(Meta(?:Quest)?)\b"}
})
```

**False positives: "Apple pie" detected as Apple Inc.**

The default clusters for Meta, Apple, Amazon, and Google include negative lookahead patterns to avoid common false positives (e.g., "Apple pie", "Meta tag", "Amazon rainforest"). If you encounter new false positives, add negative lookahead terms to the cluster's `regex`:

```python
# Before: matches "Apple pie"
"Apple": {"aliases": ["Apple"], "regex": r"\bApple\b"}

# After: skips "Apple pie" and similar
"Apple": {
    "aliases": ["Apple"],
    "regex": r"\bApple(?!\s+(?:pie|cider|sauce|tree|juice))\b"
}
```

**Cohen's d is negative — is that a bug?**

No. `cohens_d(a, b)` returns a signed value: `(mean(a) - mean(b)) / pooled_sd`. A negative value means group `a` scores lower than group `b`. Use `abs(cohens_d(...))` when you only care about magnitude, or `interpret_effect_size(d)` which already handles the sign.

**Entity clusters: dict format vs. list format**

`DEFAULT_ENTITY_CLUSTERS` and `detect_entities(clusters=...)` accept two formats:

```python
# Dict format (recommended — supports custom regex)
{"Meta": {"aliases": ["Meta", "Facebook"], "regex": r"\b(Meta|Facebook)\b"}}

# List format (shorthand — auto-generates regex from aliases)
{"Meta": ["Meta", "Facebook"]}
```

Both work in all contexts: direct API calls, YAML profiles, and custom cluster files.

**Tests fail with import errors**

Make sure you've installed the package in development mode:

```bash
cd mediascope
pip install -e ".[dev]"
python -m spacy download en_core_web_sm
```

## Examples

The `examples/` directory contains runnable demos that walk through MediaScope's key capabilities:

| File | What It Demonstrates |
|---|---|
| [`quick_start.py`](examples/quick_start.py) | Minimal workflow: load profile → analyze article → generate disclosure |
| [`full_pipeline.py`](examples/full_pipeline.py) | Complete pipeline: RSS ingest → entity detection → sentiment → framing → asymmetry scoring → report |
| [`same_event_comparison.py`](examples/same_event_comparison.py) | Cross-publication comparison of the same event (wire service vs magazine), isolating editorial framing from event severity |
| [`framing_correction_demo.py`](examples/framing_correction_demo.py) | **NEW:** How MediaScope corrects VADER's positive bias on investigative journalism using framing device signals, active-negative agency detection, and source stance analysis |
| [`agent_integration.py`](examples/agent_integration.py) | Integration patterns for LangChain, CrewAI, and raw function calling |

## Sample Output Gallery

The `examples/sample_output/` directory contains annotated analyses of real articles:

| File | Article | Key Findings |
|---|---|---|
| `atlantic_ai_data_centers_dirty_dystopian_2026_03_*` | Atlantic: "Inside the Dirty, Dystopian World of AI Data Centers" | Tone: -0.40 manual. 12 framing devices (6 loaded_language + 3 scale_metaphor + 2 environmental_justice + 1 dystopian_imagery). 0 anonymous sources. OpenAI partnership disclosed in-text; Emerson Collective/Apple conflicts undisclosed. First Atlantic example — Matteo Wong byline. |
| `atlantic_meta_ai_slop_vibes_2025_10_*` | Atlantic: "A Tool That Crushes Creativity: AI slop is winning" | Tone: -0.72 manual. Charlie Warzel byline. VADER misses negative editorial stance entirely (~+0.30 predicted). Critical for establishing Atlantic anti-AI-product framing patterns and testing Emerson Collective ownership-conflict detection. |
| `atlantic_tool_crushes_creativity_2025_10_*` | Atlantic: "A Tool That Crushes Creativity" (extended analysis) | Sustained cultural critique of AI-generated content. 5+ distinct analogies, extensive loaded language, ironic quotation. Adversarial toward OpenAI and Meta but frames critique as civilizational concern. Warzel 3-publication career (BuzzFeed→NYT→Atlantic) makes him a high-value portable bias candidate. |
| `atlantic_ai_not_conscious_2026_06_*` | Atlantic: "No, Artificial Intelligence Is Not Conscious" | Ted Chiang long-form essay (~4,200 words). 50 Anthropic mentions. **Key entity detection gaps:** Amanda Askell (Anthropic philosopher), AlphaFold, IBM/Deep Blue, Microsoft Word not matched. Tests toolkit on opinion/philosophy genre — no anonymous sources, no traditional framing devices, but sustained adversarial argument through philosophical reasoning rather than journalistic technique. |
| `atlantic_emotion_ai_workplace_surveillance_2026_05_*` | Atlantic: "The Rise of Emotional Surveillance" | Ellen Cushing byline. Emotion AI / affective computing in the workplace. Entities: MorphCast, Aware (Slack integration), HireVue, MetLife, Burger King "Patty". Tests toolkit on science-debunking genre — Paul Ekman / Lisa Feldman Barrett debate. No Meta or Big Tech as primary entity, but relevant for workplace surveillance framing pattern detection. |
| `guardian_meta_whistleblower_hay_festival_2026_06_01_*` | Guardian: Meta silences Facebook whistleblower at Hay Festival | Tone: -0.45 manual/-0.57 toolkit, 20 framing devices (15 loaded_language + 4 emotional_appeal + 1 timeline_implication), 0 anonymous sources, 100% anti-Meta source deployment. First Guardian example — control case for editorial bias without financial conflicts. |
| `guardian_uk_tech_crackdown_us_intervention_2026_06_09_*` | Guardian: UK tech crackdown proceeds despite US intervention | Tone: -0.30 toward Meta. **Sovereignty framing discovery:** "British young people," "British parents and British families," "UK's national interest" — nationalist language reframing corporate regulation as patriotic duty. Led to new `sovereignty_framing` and `geopolitical_regulatory_pressure` device types. 6 pro-regulation sources vs 0 tech company quotes. Kicker positions Meta as sole named corporate litigant. |
| `guardian_meta_wynn_williams_lawsuit_2026_06_25_*` | Guardian: Whistleblower Wynn-Williams sues Meta over 'silence' attempts | Tone: -0.50 manual. Sequel to Hay Festival article. **Toolkit fixes:** litigation_framing expanded (complaint, arbitration, suing patterns: 0→10 detections), power_asymmetry per-violation fines with adjectives ($50K "each purported violation"). Corporate_reassurance_undercut: Meta's "we do not require non-disparagement clauses" vs enforcing exactly that. Ironic quotation: Facebook VP calling end of forced arbitration "the right thing to do" while still enforcing the 2017 deal. 18 new tests. |
| `engadget_meta_wynn_williams_lawsuit_2026_06_26_*` | Engadget: 'Careless People' author accuses Meta of 'punishing' whistleblower | Tone: -0.65 manual. Same lawsuit as Guardian (Jun 25) but markedly more hostile. Editorial sarcasm ("Of course... oh hang on") — led to new `sarcastic_correction` framing device type. ~250 words with 8 loaded-language hits (1 per 30 words, 3× Guardian density). Zero independent sources. Joel Kaplan framed as "mastermind." Cross-publication companion to Guardian analysis. |
| `mit_tr_anduril_meta_smart_glasses_warfare_2026_05_18_*` | MIT TR: Inside Anduril and Meta's Quest to Make Smart Glasses for Warfare | Tone: -0.10 manual/+0.64 toolkit (VADER positive bias persists). 0 anonymous sources, 2 expert sources. Microsoft IVAS $22B failure used as implicit risk frame. Military/weapons vocabulary with editorial restraint — demonstrates the limits of lexical sentiment on defense-tech reporting. First MIT TR example. |
| `mit_tr_llms_mass_surveillance_2026_04_21_*` | MIT TR: How LLMs Could Supercharge Mass Surveillance in the US | Tone: -0.35 manual. Policy analysis / speculative threat assessment. Anchors on Anthropic/DOD dispute; Amodei's "crime against humanity" language is outsourced intensity. Demonstrates measured academic prose that VADER reads as neutral despite adversarial policy framing. |
| `mit_tr_meta_ai_security_hack_2026_06_05_*` | MIT TR: The Meta hack shows there's more to AI security than Mythos | Tone: -0.15 manual. Grace Huckins byline (Rhodes Scholar, Stanford PhD). Security context adjustment test case — domain-specific language inflates emotional intensity. Indirect funding chain: Schmidt award → Google → MIT Intelligence Quest Fund. |
| `wired_meta_nametag_facial_recognition_2026_06_05_*` | Wired: Meta "NameTag" facial recognition investigation | Tone: -0.65, 8+ framing devices, critical VADER positive-bias gap identified |
| `wired_meta_nametag_removal_2026_06_08_*` | Wired: Meta Removes NameTag After Wired's Investigation | Tone: -0.60 manual / -0.32 toolkit (understated). Follow-up to June 5 investigation. Tests headline framing override — "Meta Deletes Face-Recognition System After WIRED Report" scores positive on VADER despite adversarial editorial construction. |
| `wired_meta_rayban_creep_2026_03_23_*` | Wired: The Rise of the Ray-Ban Meta Creep | Long-form (~2,100 words) feature on social consequences of Meta smart glasses. Built on personal testimonials and cultural observation. Heavily slanted through headline word choice, loaded vocabulary, and source selection — but journalistically sound with named sources and verifiable claims. |
| `wired_meta_dark_mood_2026_05_14_*` | Wired: Meta's New Reality: Record High Profits. Record Low Morale | Flagship pre-layoff piece with 4 bylines (Dave, Goode, Levy, Schiffer). "Marshaling the full weight of the publication" editorial decision — rare for workplace morale pieces. Opening salvo of multi-week investigative arc leading to Applied AI and NameTag exposés. |
| `wired_meta_horizon_worlds_comedy_club_2026_03_*` | Wired: The Comedy Club at the End of the Metaverse | Platform eulogy / immersive narrative journalism by Boone Ashworth. Tone: -0.30 (melancholic, not hostile). 0.85 source balance toward community members; Meta gets one boilerplate email quote. Active vs passive framing: Meta "announced," "pulling away" vs users "broke down in tears," "terrified." |
| `wired_meta_applied_ai_revolt_2026_06_13_*` | Wired's "Soul-Crushing Gulag" Meta Applied AI report | Tone: -0.72, 5/7 framing devices detected, 80% anonymous sources, strong emotional appeal + loaded language |
| `wired_meta_applied_ai_2026_06_16_*` | Wired Meta Applied AI follow-up | Continued negative framing with Bosworth admission quotes |
| `wired_meta_bosworth_atrocious_reorg_2026_06_16_*` | Wired: Bosworth's "Atrocious" Reorg | Tone: -0.55 manual. Bosworth's own "atrocious" quote weaponized editorially. Tests ironic quotation framing — executive's candor reframed as damning admission. Self-referential investigation: cites own prior Applied AI reports as evidence. |
| `wired_meta_rank_one_2026_06_15_*` | Wired Meta "Rank One" article | Earlier coverage establishing the pattern |
| `wired_meta_mci_data_exposure_2026_06_22_*` | Wired: Meta Exposed Data Internally From Employee-Tracking Program | Breaking news piece on MCI security incident. Well-sourced factual reporting with embedded editorial choices that amplify institutional failure narrative. "We told you so" structure — positions data exposure as vindication of employee concerns. |
| `wired_vs_reuters_mci_data_exposure_2026_06_22_*` | Cross-publication: Wired vs. Reuters MCI data exposure | Same-day, same-event framing comparison. Wired: 7+ framing devices (loaded headline, vindication narrative, CEO personalization, kicker framing). Reuters: 1 device (mild corporate_reassurance_undercut). Validates new `corporate_reassurance_undercut` device — fires on both with appropriate intensity differentiation. Demonstrates wire-service-as-baseline methodology. |
| `nyt_meta_ai_employees_miserable_2026_05_08_*` | NYT: "Meta's Embrace of A.I. Is Making Its Employees Miserable" | First NYT example. Tone: +0.61 VADER (WRONG) → -0.37 corrected. **5 critical fixes:** active-negative agency detection, workplace coercion/revolt loaded language, investment-near-layoffs juxtaposition, source stop-word filter, framing-corrected headline alignment. Pre/post comparison demonstrates framing correction mechanism. |
| `nyt_meta_prediction_markets_arena_2026_06_23_*` | NYT: Meta "Arena" prediction markets app scoop | Reconstructed from 5 secondary sources (Reuters, NY Post, IBD, Engadget, CNN). Tone: -0.10 manual. Near-neutral business scoop. **Key finding: toolkit blind spot on counted-anonymous source patterns** ("two employees said," "one person familiar") — 100% anonymous sourcing reads as 0%. Cross-publication comparison of same event: Engadget -0.70 vs Reuters +0.05 on same story, same day. |
| `nyt_meta_arena_polymarket_partnership_2026_06_26_*` | NYT: Zuckerberg asks Meta to explore Polymarket/Kalshi partnership | Follow-up to Jun 23 Arena scoop. Reconstructed from Reuters, Seoul Economic Daily, TheStreet, Gizmodo. Tone: -0.05 manual. Near-neutral expansion scoop. **Toolkit improvements:** new Prediction Markets/Fintech entity cluster (Polymarket, Kalshi, Robinhood, CFTC, etc.), Arena/Francis Brennan/Alexandr Wang added to Meta aliases, source extraction `\s+` fix for line-wrapped anonymous patterns ("three employees with knowledge of"). Cross-publication comparison: Gizmodo -0.35 (adversarial framing) vs Reuters +0.05 (neutral wire) on same story. |
| `nyt_meta_ai_voluntary_review_2026_06_23_*` | NYT: U.S. presses Meta on AI reviews | Reconstructed from Reuters + secondary sources. Manual tone: -0.20. **Critical toolkit failure: VADER scored +0.61 (strongly positive)** on a clearly adversarial article using isolation framing ("the only major company that has not") and regulatory pressure language. **4 fixes applied:** isolation_framing + pressure_language added to adversarial device types; count_anonymous_sources excludes no_comment; 14 regulatory passive framing phrases added. Corrected tone: -0.57. 8 new tests (187 total). |
| `wired_meta_glasses_launch_self_branded_2026_06_23_*` | Wired: Meta's new $299 self-branded smart glasses launch | Product review from press event. Manual tone: +0.15, toolkit: +0.67 (overestimates). **7 framing devices:** surveillance-consumer juxtaposition (linking glasses to military facial recognition), kicker framing (ending on workforce morale crisis), loaded language (nefarious, discreetly, comically). All 3 quoted sources are Meta insiders; editorial voice carries ALL negative framing (outsourced ratio: 0.0). **6 toolkit fixes:** false-positive "disabled?"→"disabled" in emotional_appeal, product name stop-filter ("Meta Glasses"), new kicker_framing detection, nefarious/comically loaded language, morale flexible-distance regex. 15 new tests (202 total). |
| `gizmodo_vs_wired_glasses_launch_2026_06_23_*` | Cross-publication: Gizmodo vs Wired Meta glasses launch | Same event (Jun 23), same press Q&A with Bosworth. Gizmodo (James Pero, ~890 words): tone +0.10, 0 framing devices, neutral business-question framing of privacy concerns. Wired (Julian Chokkattu, ~1,200 words): tone -0.15, 10 framing devices (kicker_framing, self_referential_investigation ×2, loaded_language ×4, juxtaposition, emotional_appeal, catastrophizing). Demonstrates editorial DNA: same facts, radically different framing. |
| `reuters_meta_dalton_smith_departure_2026_06_17_*` | Reuters: Meta head of AI for work leaves company | Wire-service baseline — tone: -0.15 (mildly negative from facts, not framing). ~520 words, no individual byline. Introduces novel entities (Emily Dalton Smith, Manus, Metamate, ATA). Comparison with Wired's coverage of same restructuring saga (Applied AI "soul-crushing," Bosworth "atrocious" reorg) provides natural experiment in publication DNA shaping editorial framing. |
| `weekly_report.md` | Synthetic weekly report | Demonstrates full report format with statistical tables |
| `asymmetry_scores.json` | Machine-readable scores | JSON format for programmatic consumption |
| `conflict_disclosure.md` | Disclosure statement | Template for publication-level conflict disclosure |

Each article pair (`*_article.txt` + `*_analysis.md`) shows the full pipeline: raw text → entity detection → 8-dimension sentiment → framing devices → source analysis → conflict disclosure.

## Testing

MediaScope has **518 tests** across 20 test files, each covering a different analytical capability:

| Test File | Tests | What It Covers |
|---|---|---|
| `test_entities.py` | 14 | Entity detection, regex patterns, false-positive exclusion, cluster formats |
| `test_sentiment.py` | 43 | 8-dimension scoring, VADER/TextBlob composite, framing correction pipeline, active-negative agency, headline override, security context adjustment, self-referential investigation detection |
| `test_source_stance.py` | 60 | Source extraction, stance classification, outsourced intensity, power asymmetry, counted anonymous sources, no-comment exclusion, product name stop-filter, kicker framing, isolation/pressure as adversarial devices |
| `test_asymmetry.py` | 22 | Asymmetry score calculation, Welch's t-test, Cohen's d, bootstrap confidence intervals |
| `test_careers.py` | 19 | Career data loading, migration detection, DiD analysis, leadership change analysis, bias decomposition |
| `test_nyt_article_improvements.py` | 28 | NYT-specific article analysis fixes: active-negative agency, workplace coercion language, investment-near-layoffs juxtaposition, source stop-word filter |
| `test_nyt_ai_reviews.py` | 23 | NYT AI voluntary review article: isolation framing, pressure language, regulatory passive framing, VADER positive-bias correction |
| `test_platform_death.py` | 30 | Platform eulogy detection, melancholic vs hostile tone distinction, community source framing |
| `test_quality_standards.py` | 35 | Quality enforcement: banned AI-slop phrase detection (case-sensitive/insensitive), em dash limit enforcement, counterargument/limitations/methodology signal detection, score calculation, pass/fail logic |
| `test_citations.py` | 39 | Citation extraction: URL detection, source grading (primary/secondary/tertiary domain lists), domain extraction, attribution patterns ("according to"), formal citations ([1], (Author 2024)), deduplication, citation report statistics |
| `test_topics.py` | 28 | Topic classification: all 12 standardized topic buckets, confidence scoring (keyword coverage + density), top-N filtering, custom topic injection, multi-topic articles, edge cases |
| `test_claims.py` | 28 | Claim-evidence mapping: statistic detection (percentages, dollar amounts, multipliers), quote detection, citation signal detection, assertion detection, source attribution, claim mapping, unsupported claims ratio, confidence scoring |
| `test_atlantic_analysis.py` | 31 | Atlantic-specific coverage analysis: Emerson Collective ownership conflicts, Apple/OpenAI financial interest detection, AI coverage framing patterns, data center environmental articles |
| `test_loaded_language_uproar.py` | 13 | Loaded language detection edge cases: workplace coercion terms, revolt vocabulary, "uproar" word variants, false-positive exclusion for neutral contexts |
| `test_scale_magnitude.py` | 16 | Scale/magnitude framing: raw number amplification, calculated maximums, cumulative totals, scale analogies, victim roster detection, comparison amplifiers |
| `test_glasses_deep_dive.py` | 17 | Wired glasses launch deep dive fixes: kicker framing (negative final paragraph detection), product-name stop-filter for source extraction ("Meta Glasses"), emotional_appeal false-positive exclusion (question marks), loaded language expansion (nefarious, comically, discreetly) |
| `test_hypocrisy_medical_duress.py` | 16 | Hypocrisy frame detection: "the only company that has not" patterns, medical duress framing, healthcare-as-leverage patterns, prepositional phrase tolerance in entity–negation gaps |
| `test_wynn_williams_fixes.py` | 18 | Guardian Wynn-Williams lawsuit fixes: source extraction false positives (day names "Wednesday", book titles "Careless People"), litigation framing expansion (complaint, suing, arbitration patterns), power_asymmetry per-violation fines with intervening adjectives |
| `test_sarcastic_correction.py` | 15 | Sarcastic correction framing device: concede-then-retract patterns ("Of course... oh wait"), standalone sarcastic constructions ("Who could have predicted"), false-positive exclusion for neutral uses of "of course" and "right" |
| `test_postpass_activation.py` | 23 | Post-pass device activation: analogy_stacking threshold (3+ markers), speculative_framing threshold (5+ hedges), expanded loaded_language patterns (deceptive, misleading, disingenuous, unprecedented+breach/violation), expanded speculative verbs (influence, affect, leak, seep, expose), integration of both post-passes |

```bash
# Run all tests
python3 -m pytest tests/ -v

# Run a specific test file
python3 -m pytest tests/test_source_stance.py -v

# Run tests matching a keyword
python3 -m pytest tests/ -k "kicker" -v

# Run only quality enforcement tests
python3 -m pytest tests/test_quality_standards.py tests/test_citations.py tests/test_claims.py -v

# Run only topic classification tests
python3 -m pytest tests/test_topics.py -v
```

Every article analysis improvement requires at least one regression test before it can be committed. Tests use real article excerpts from the `examples/sample_output/` directory.

## License

MIT License. See [LICENSE](LICENSE).

## Disclaimer

MediaScope is a transparency tool for media accountability research. It is designed to surface undisclosed conflicts of interest and measure coverage asymmetry using statistical methods. It does not make editorial judgments about whether coverage is "right" or "wrong" — it measures whether coverage patterns correlate with financial interests.

Users of this toolkit should:
1. Disclose their own conflicts of interest when publishing results
2. Present findings with appropriate statistical caveats
3. Include the strongest counterargument to their thesis
4. Distinguish between correlation and causation

The existence of a financial conflict does not prove that coverage is biased because of that conflict. MediaScope identifies patterns that warrant disclosure and further investigation.
