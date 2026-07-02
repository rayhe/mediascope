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

Ships with verified career data for **117 journalists** across 170+ publications, including high-value migrations like Karen Hao (MIT Tech Review → Atlantic), Cade Metz (Wired → NYT), Zoë Schiffer (The Verge → Platformer → Wired), Zeyi Yang (MIT Tech Review → Wired), Melissa Heikkilä (MIT Tech Review → Financial Times), Emily Mullin (MIT Tech Review → Wired), David McCabe (Axios → NYT), Stuart A. Thompson (WSJ → NYT), David Yaffe-Bellany (Bloomberg → NYT), Erin Griffith (Fortune → Wired → NYT), Hugo Lowell (Guardian → Wired), Tom Simonite (MIT Tech Review → Wired → Washington Post), Noah Shachtman (Wired ↔ Daily Beast ↔ Rolling Stone ↔ Wired), Morgan Meaker (Telegraph → Wired → Bloomberg), Paris Martineau (The Outline → Wired → The Information → Consumer Reports), Eli Tan (CoinDesk → Washington Post → NYT), Nellie Bowles (Guardian → Vice News → NYT → The Free Press), Reece Rogers (Insider → Wired, service writer baseline), Danny Yadron (WSJ → Guardian → Stanford Law), Steve Lohr (NYT lifer, ~47 years — foreign correspondent → business editor → technology reporter, pure institutional framing baseline), Maxwell Zeff (Bloomberg → Gizmodo → TechCrunch → Wired — fastest four-outlet pipeline, ChatGPT-era generational contrast), and Brian X. Chen (Macworld → Wired → NYT — Wirecutter co-founder, 14+ year NYT lifer, "Tech Fix" column pivot from product reviews to societal critique, Gruber contradiction test for institutional framing drift), Isabella Ward (Bloomberg → Wired — MSci Physics, quantum computing specialist, London rebuild hire alongside deputy editor Rosie Swash), Louise Matsakis (Mashable → Motherboard/VICE → Wired → Rest of World → NBC News → Semafor → Wired — rare boomerang journalist, China/e-commerce specialist, now senior business editor shaping Big Tech coverage framing), Chris Stokel-Walker (freelance across Guardian, Wired, NYT, MIT Tech Review — highest cross-publication coverage of any tracked journalist, key DiD test case), Maddy Varner (ProPublica → The Markup → FTC → Wired — Gerald Loeb Award winner for "Monetizing Hate" Facebook ad investigation, FTC technologist in residence providing regulatory insider perspective, now investigating Meta scam ad lawsuits at Wired), Kate Taylor (Forbes → Entrepreneur → Business Insider → Columbia MBA → Wired — Emmy-nominated investigative journalist whose exposés became HBO documentaries, now covering AI's impact on employment), and Julian Chokkattu (TechCrunch → Star-Ledger → Digital Trends → Wired — 7+ year Wired veteran, Senior Editor for Gear, primary hardware reviewer for Meta products including smart glasses).

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
1. [SEVERITY 5] Advance Publications holds 65.2% voting power in Reddit
   (83.5% of Class B shares, 10 votes/share), a direct Meta competitor,
   with 2 board seats and ~$7B stake value.
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
| **Wired** | Advance Publications | Financial + Competitive | 65.2% Reddit voting power (83.5% Class B), AI licensing with Meta's competitors |
| **NY Times** | Sulzberger Family | Litigation | Suing OpenAI while building AI internally |
| **The Guardian** | Scott Trust (non-profit) | Partial control | OpenAI + ProRata licensing deals, but no equity in specific competitors. Closest to baseline in the 5-pub set (pre-Feb 2025 coverage cleaner). |
| **The Atlantic** | Emerson Collective (LPJ) | Investment + Licensing + Civic | Owner holds ~$16B Apple stock, $6.5B OpenAI equity exit, co-chairs civic org with Google/Alphabet president and OpenAI CEO |
| **MIT Tech Review** | MIT | Institutional paradox | Parent receives $500M+ from companies it covers; operates DoD's largest FFRDC ($12.2B Lincoln Lab contract, $1.36B/yr); DAF-MIT AI Accelerator transfers AI to military |

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
- **No AI slop.** Banned phrase detection catches "delve," "tapestry," "landscape," and 22 other markers (25 total).
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
| [`careers_demo.py`](examples/careers_demo.py) | **NEW:** Editorial Histories module: career timelines for 115 journalists, 290 auto-detected migrations, DiD natural experiment setup, and notable career pipelines |
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
| `fastco_meta_wynn_williams_lawsuit_2026_06_26_*` | Fast Company: Meta faces lawsuit by 'Careless People' author and whistleblower | Tone: -0.60 manual / -0.71 toolkit. Third analysis of same Wynn-Williams v. Meta lawsuit — completes first 3-outlet controlled comparison on identical source material. Middle-ground "reportorial-sympathetic" register between Guardian's legalism and Engadget's sarcasm. 13 framing devices (6 loaded_language, 5 litigation_framing, 1 ironic_quotation, 1 kicker_framing). Outsourced intensity: closing complaint quote is emotional climax. Meta response depersonalized (no named spokesperson). **Bug discovered:** `EMOTIONAL_LANGUAGE` missing legal/whistleblower terms → `quoted_intensity=0.0` false negative. 18 terms added, 14 pre-existing duplicates cleaned. |
| `mit_tr_anduril_meta_smart_glasses_warfare_2026_05_18_*` | MIT TR: Inside Anduril and Meta's Quest to Make Smart Glasses for Warfare | Tone: -0.10 manual/+0.64 toolkit (VADER positive bias persists). 0 anonymous sources, 2 expert sources. Microsoft IVAS $22B failure used as implicit risk frame. Military/weapons vocabulary with editorial restraint — demonstrates the limits of lexical sentiment on defense-tech reporting. First MIT TR example. |
| `mit_tr_llms_mass_surveillance_2026_04_21_*` | MIT TR: How LLMs Could Supercharge Mass Surveillance in the US | Tone: -0.35 manual. Policy analysis / speculative threat assessment. Anchors on Anthropic/DOD dispute; Amodei's "crime against humanity" language is outsourced intensity. Demonstrates measured academic prose that VADER reads as neutral despite adversarial policy framing. |
| `mit_tr_meta_ai_security_hack_2026_06_05_*` | MIT TR: The Meta hack shows there's more to AI security than Mythos | Tone: -0.15 manual. Grace Huckins byline (Rhodes Scholar, Stanford PhD). Security context adjustment test case — domain-specific language inflates emotional intensity. Indirect funding chain: Schmidt award → Google → MIT Intelligence Quest Fund. |
| `mit_tr_ai_memory_privacy_frontier_2026_01_*` | MIT TR: What AI "remembers" about you is privacy's next frontier | Tone: -0.25 manual (cautionary, constructive). CDT policy op-ed by Miranda Bogen & Ruchika Joshi. Industry-wide critique — Meta mentioned once alongside 4 peers. Tests toolkit on policy/prescriptive genre: no anonymous sources, no adversarial framing, structured recommendation format. Scare-quote anthropomorphism challenge in headline. |
| `wired_meta_nametag_facial_recognition_2026_06_05_*` | Wired: Meta "NameTag" facial recognition investigation | Tone: -0.65, 8+ framing devices, critical VADER positive-bias gap identified |
| `wired_meta_nametag_removal_2026_06_08_*` | Wired: Meta Removes NameTag After Wired's Investigation | Tone: -0.60 manual / -0.32 toolkit (understated). Follow-up to June 5 investigation. Tests headline framing override — "Meta Deletes Face-Recognition System After WIRED Report" scores positive on VADER despite adversarial editorial construction. Identified `denial_contradiction` gap (now resolved — 3 instances detected). |
| `digitaltrends_meta_nametag_removal_2026_06_09_*` | Digital Trends: Meta denied face scanning tech, then silently wiped the evidence | Cross-outlet comparison against Wired's NameTag coverage. Secondary-report dynamics: DT lacks original evidence, compensates with hotter headline ("silently wiped the evidence") and historical precedent (2021 face-recognition shutdown). 1 `denial_contradiction` (indirect-speech Pattern 4) vs Wired's 3. Framing density: 1 per 54 words (moderate) vs Wired's 1 per 34 words. First cross-outlet validation of `denial_contradiction` device type. |
| `wired_meta_rayban_creep_2026_03_23_*` | Wired: The Rise of the Ray-Ban Meta Creep | Long-form (~2,100 words) feature on social consequences of Meta smart glasses. Built on personal testimonials and cultural observation. Heavily slanted through headline word choice, loaded vocabulary, and source selection — but journalistically sound with named sources and verifiable claims. |
| `wired_meta_dark_mood_2026_05_14_*` | Wired: Meta's New Reality: Record High Profits. Record Low Morale | Flagship pre-layoff piece with 4 bylines (Dave, Goode, Levy, Schiffer). "Marshaling the full weight of the publication" editorial decision — rare for workplace morale pieces. Opening salvo of multi-week investigative arc leading to Applied AI and NameTag exposés. |
| `wired_meta_horizon_worlds_comedy_club_2026_03_*` | Wired: The Comedy Club at the End of the Metaverse | Platform eulogy / immersive narrative journalism by Boone Ashworth. Tone: -0.30 (melancholic, not hostile). 0.85 source balance toward community members; Meta gets one boilerplate email quote. Active vs passive framing: Meta "announced," "pulling away" vs users "broke down in tears," "terrified." |
| `wired_meta_applied_ai_revolt_2026_06_13_*` | Wired's "Soul-Crushing Gulag" Meta Applied AI report | Tone: -0.72, 5/7 framing devices detected, 80% anonymous sources, strong emotional appeal + loaded language |
| `wired_meta_ai_gulag_engineer_revolt_2026_06_*` | Wired: Meta AI "Gulag" — 6,500 engineers conscripted into data labeling | Reconstructed from 7 secondary sources (Wired paywalled). Tone: -0.65 manual. 14 framing devices (loaded_language ×6, emotional_appeal ×3, scale_magnitude ×2, juxtaposition, self_referential_investigation, kicker_framing). 80% anonymous sourcing. Military conscription vocabulary ("gulag," "conscripted," "forced labor"). **Toolkit fixes:** Scale AI entity added to Meta cluster, conscript terms added to workplace loaded language, keystroke/screen-recording added to surveillance patterns. 17 new tests. |
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
| `reuters_meta_mci_pause_2026_06_22_*` | Reuters: Meta to pause internal mouse-tracking tech | Wire-service breaking news (~400 words). Tone: -0.15 manual. Entity cluster audit: Meta/MCI/Tracy Clayton correctly aggregated, 12 cluster mentions. Includes rare Reuters correction ("'documentation showed' not 'document said'"). Paired with Wired MCI data exposure for wire-vs-magazine same-event comparison. |
| `reuters_meta_insurance_defense_2026_06_23_*` | Reuters: In Meta's social media litigation, who pays the lawyers? | Alison Frankel legal analysis column. **12 framing devices** detected, dominated by `precedent_analogy` ("echoes opioid-era coverage fights") and 6× `scale_magnitude`. Led to new Insurance/Litigation Finance entity cluster (Hartford, Chubb, Flashlight Capital, Innsworth Capital, Burford Capital) and Legal/Judicial cluster (Section 230, DSA, bellwether, MDL). First legal-column genre example. |
| `mit_tr_lecun_ami_labs_contrarian_2026_01_22_*` | MIT TR: Yann LeCun's New Venture Is a Contrarian Bet Against LLMs | Q&A interview format — tests toolkit on conversational genre. Tone: +0.15 manual vs +0.65 toolkit (VADER positive bias on Q&A prose). **Critical gap:** zero sources detected because Q&A format bypasses standard attribution patterns. Source authority 1.0 manual (Turing Award recipient) vs 0.0 toolkit. Demonstrates genre-specific blind spots requiring Q&A-aware source extraction. |
| `mit_tr_meta_ai_hack_agent_security_2026_06_05_*` | MIT TR: The Meta hack shows there's more to AI security (deep dive) | Expanded analysis of the Meta AI customer support agent vulnerability. **13 framing devices**, 7× loaded_language, 2× rhetorical_question. **Largest framing correction in corpus:** raw +0.65 → corrected -0.43 (1.09-point swing). 4/4 named experts criticize Meta; zero defending voices. Expert-loaded adversarial structure with surface-level neutral prose. Grace Huckins byline (Rhodes Scholar, Stanford PhD). |
| `mit_tr_ai_agents_not_coworkers_2026_06_29_*` | MIT TR: AI agents are not your "coworkers" | The Algorithm newsletter op-ed. Tone: +0.635 VADER (misleading — editorially negative). 9 framing devices (4× ironic_quotation, 3× analogy_stacking, 1× emotional_appeal, 1× rhetorical_question). **Key finding: outsourced_intensity false negative.** Acemoglu quote ("losing proposition," "replace humans") scored 0.0 — `EMOTIONAL_LANGUAGE` was missing AI labor/displacement terms. **33 terms added.** Fixed: quoted_intensity 0→1.0, outsourced_ratio 0→0.653. Meta conspicuously absent despite being major AI agent deployer. One-sided expert sourcing: 2/2 critics, 0/2 defenders. |
| `mittr_anthropic_feud_jun2026*` | MIT TR: Three things to watch amid Anthropic's feud with the US government | Annotation (not full analysis format). Entity detection stress test: Fable, Mythos, Zhipu, Chinese AI cluster. Scare quotes ("doomers," "exporting," "wake-up call"), speculative rhetorical questions, cross-domain precedent analogy (nuclear nonproliferation). See `test_mittr_anthropic_feud.py` for 25 regression tests. |
| `avclub_meta_arena_gambling_2026_06_27_*` | AV Club: Mark Zuckerberg thinks Meta isn't doing enough to cater to gambling addicts | Cross-publication stress test for sardonic tone detection on entertainment press. Sarcastic correction (ironic denial, mock-certainty), loaded language (character diminishment "tech bros," industry-as-vice "gambling addiction"). Tests toolkit generalization beyond prestige-press framing techniques to pop-culture editorial voice. See also `test_avclub_sardonic_framing.py`. |
| `fastco_meta_ai_draft_reversal_2026_06_25_*` | Fast Company: Meta reverses decision to reassign employees to AI training roles | Follow-up to Wired "soul-crushing gulag" coverage. **Key discovery:** led to `trend_bundling` framing device (#34). Article assembles 4+ companies' separate decisions (Duolingo, Amazon, Uber, Microsoft) into an industry-wide pattern. Also: ironic quotation ("drafted" in scare quotes ×3), self-referential investigation ("shared with Fast Company from sources close to the company"). |
| `gizmodo_meta_arena_worst_instincts_2026_06_24_*` | Gizmodo: Meta's new prediction-market app | Companion to AV Club and NYT Arena coverage for planned cross-publication comparison of same-event sardonic vs. neutral framing. |
| `gizmodo_meta_google_ai_tokens_addiction_2026_06_29_*` | Gizmodo: "Meta Reportedly Got Too Addicted to Google AI Tokens and Had to Be Cut Off" | **Discovered `pathologizing_metaphor` device type.** ~320-word sardonic report on Google rate-limiting Meta's Gemini API consumption. Sustained addiction/gluttony/gambling metaphorical frame: "gorge itself," "cut off," "high-rollers." 6 framing devices (3× pathologizing_metaphor, sarcastic_correction, ironic_quotation, anonymous_authority). 80% anonymous sourcing. Emotional intensity jumped from 0.29 → 0.71 after pathologizing vocabulary added. |
| `gizmodo_project2029_kids_over_clicks_2026_06_29_*` | Gizmodo: "Democrats Want to Do Their Own Project 2025. First Up: Kicking Kids Offline" | Tests **topic displacement** — article nominally covers child safety policy but spends ~40% on unrelated political commentary (Trump, Iran, Kushner). Sardonic/dismissive editorial tone. Editorial deflation: "Noble efforts, indeed, but maybe not the most pressing concern." Credibility undermining via tangent chain. |
| `guardian_deepmind_philosopher_gabriel_2026_06_*` | Guardian: "The philosopher inside Google DeepMind" | ~7,500-word long-form profile of Iason Gabriel, DeepMind's in-house political philosopher. Tests toolkit on **character-driven feature genre**: no adversarial framing, sympathetic tone, extensive named-source quoting. **Significant entity detection gaps:** 15+ named individuals (Demis Hassabis, Shane Legg, Nick Bostrom, Timnit Gebru, etc.) not captured because entity extractor is tuned for organizational clusters, not individual profiles. |
| `malwarebytes_meta_ai_support_bot_hack_2026_06_*` | Malwarebytes: Meta's AI support bot happily handed Instagram accounts to hackers | **Discovered `anthropomorphization` device type.** Cybersecurity vendor blog. Bot consistently personified: "took that brief a little too seriously," "happily handed," "confused bot," "without being taught how to verify." Converts missing identity-verification check into character flaw in a naive agent. Clean source attribution (0 anonymous sources). |
| `memeburn_meta_qualcomm_dragonfly_c1000_2026_06_29_*` | Memeburn: Meta's Qualcomm Dragonfly C1000 deal | **Positive/neutral baseline.** Uncritically positive tech-business reporting on Meta's multi-vendor AI infrastructure strategy. No adversarial framing, no editorial sarcasm. Useful control case for establishing what non-adversarial coverage looks like in the corpus. |
| `mit_tr_ai_bubble_meta_spending_2025_12_15_*` | MIT TR: "What even is the AI bubble?" | CEO roundtable format — interviews Altman, Zuckerberg, Pichai, Hassabis, Amodei, Bezos. Tests entity detection on multi-company articles with dense CEO mentions. OpenAI assigned as primary entity (17 mentions) despite Meta being in blast radius. Exposes need for **mention-role classifier** distinguishing subject vs. reference mentions. |
| `mit_tr_ai_jobs_hysteria_reality_check_2026_05_28_*` | MIT TR: "A reality check on the AI jobs hysteria" | **Contrarian-to-prevailing-narrative test.** David Rotman systematically dismantles AI job-loss panic using BLS data and Stanford research. Meta mentioned once in passing. VADER scored −0.99 (extreme negative) on factual economic analysis — **Path G long-text normalization** failure case. Tests toolkit on data-heavy, expert-sourced academic journalism. |
| `mit_tr_data_centers_nimby_2026_01_14_*` | MIT TR: "Data Centers Are Amazing. Everyone Hates Them." | **Essay/opinion format test.** No quoted sources, first-person voice, extended analogy structure (Silicon Valley tech bus protests). Meta mentioned once. Pervasive sardonic/ironic register that VADER scores as neutral. Cross-publication comparison with Atlantic's data center piece (different angle: NIMBYism politics vs. immersive reportage). |
| `mit_tr_deepmind_multi_agent_safety_2026_06_11_*` | MIT TR: Google DeepMind multi-agent safety research | **Non-Meta baseline from tracked publication.** Will Douglas Heaven byline. Responsible tech journalism: source-heavy, expert-focused, balanced. Provides contrast material against adversarial coverage patterns. Tests toolkit on AI safety coverage from Google/DeepMind perspective. |
| `mit_tr_resistance_ai_backlash_2026_04_21_*` | MIT TR: AI resistance and backlash | Tests catastrophizing ("threat to humanity"), alarm/anxiety idioms, intensity/polemical language, poll-based social proof amplification, stalled-dollar and workforce-percentage scale magnitude patterns. See `test_resistance_patterns.py`. |
| `mit_tr_chinese_workers_ai_doubles_2026_04_*` | MIT TR: Chinese tech workers and AI doubles | Tests `commodification_metaphor` device — language flattening human identity into modules/tokens: "distill their colleagues' skills," "flattened into modules," "a cold farewell can be turned into warm tokens." |
| `multi_source_meta_claude_codex_restriction_2026_06_29_*` | Multi-source: Meta restricts Claude Code & Codex | Composite text assembled from The Decoder, CoinDesk, FourWeekMBA, Bloomberg Tax, AI Weekly. 51 entity mentions across 8 clusters. Tests toolkit on **multi-source reconstructed articles** where original (The Information) is paywalled. |
| `nyt_child_safety_features_broken_2026_06_29_*` | NYT: Child safety features found "Broken, Buried, or Missing" | **Discovered `taxonomy_framing` and `analogy_metaphor` device types.** New entity clusters: US Congress, Academic/Research, Research Centers, Child Safety Researchers/Legislation. Source extraction fixes (case-sensitive patterns, expanded known orgs). Agency attribution sparse-data dampening. 21 framing devices detected. See `test_child_safety_analysis.py`. |
| `register_meta_brain2qwerty_2026_06_30_*` | The Register: Meta Brain2Qwerty non-surgical BCI | **First `health_tech` topic classification.** Sardonic British register: "still isn't great," loaded verbs ("admit," "claims"). Retrospective comparative `failure_precedent` pattern: "as likely to beat the competition as he was when he decided to go all-in on the metaverse." Added "Zuck" to Meta aliases and collective research source attribution pattern. |
| `reuters_boe_agentic_ai_regulation_2026_06_30_*` | Reuters: Bank of England's Breeden signals rules for agentic AI | **Regulatory genre test.** Entity extraction sparse (primary actors are persons + central bank, not tech companies). Exposes gap in `government_oversight` topic keywords for central bank / prudential regulation vocabulary ("prudential," "macroprudential," "circuit breakers"). |
| `reuters_google_limits_meta_gemini_2026_06_28_*` | Reuters: Google limits Meta's use of Gemini AI models | Wire-service repackaging of Financial Times original. ~270 words. All entities correctly detected and clustered. Companion to Gizmodo version of same story — demonstrates wire-service-as-baseline vs. sardonic-editorial framing of identical facts. |
| `reuters_meta_child_addiction_29states_dismiss_2026_06_30_*` | Reuters: Meta loses bid to dismiss 29 states' child addiction claims | Wire-service legal/institutional coverage. Judge Yvonne Gonzalez Rogers denies Meta's motion to dismiss in MDL 3047. 6 framing devices in ~420 words. Entity detection gap for judges, courts, and government officials (design limitation). |
| `stocktwits_meta_virtue_ai_acquihire_2026_06_25_*` | StockTwits: Meta acqui-hires Virtue AI team | Tests entity detection for AI safety startup ecosystem: Virtue AI, Bo Li, Dawn Song, Sanmi Koyejo, FAIR, BIS, CAISI. Ironic quotation tech-jargon filter. See `test_virtue_ai_acquihire.py`. |
| `techtimes_meta_applied_ai_gulag_2026_06_17_*` | TechTimes: Meta Applied AI "gulag" (secondary source) | Secondary-source repackaging of Wired's original investigation. Tests how editorial framing attenuates or amplifies when stories are repackaged across outlets. |
| `kotaku_meta_arena_polymarket_rival_2026_06_28_*` | Kotaku: Meta "Arena" Polymarket rival | Sardonic gaming-press coverage of Meta's prediction market app. Tests sardonic tone detection calibration — editorial contempt via word choice rather than structural framing. Path D sardonic correction trigger. |
| `barchart_meta_investor_urgency_ai_capex_2026_06_30_*` | Barchart: "Meta Shows Urgency as Investors Get Exasperated" | **Financial opinion genre test.** Author discloses META/NVDA positions (standard in financial writing, not yet tracked by toolkit). 14 framing devices including editorial_deflation, precedent_analogy, catastrophizing ("tsunami" of depreciation). Emotional intensity jumped from 0.05 → 0.40 after financial metaphor vocabulary added. |
| `weekly_report.md` | Synthetic weekly report | Demonstrates full report format with statistical tables |
| `asymmetry_scores.json` | Machine-readable scores | JSON format for programmatic consumption |
| `conflict_disclosure.md` | Disclosure statement | Template for publication-level conflict disclosure |

Each article pair (`*_article.txt` + `*_analysis.md`) shows the full pipeline: raw text → entity detection → 8-dimension sentiment → framing devices → source analysis → conflict disclosure.

## Testing

MediaScope has **1171 tests** across 44 test files, each covering a different analytical capability:

| Test File | Tests | What It Covers |
|---|---|---|
| `test_entities.py` | 18 | Entity detection, regex patterns, false-positive exclusion, cluster formats |
| `test_sentiment.py` | 46 | 8-dimension scoring, VADER/TextBlob composite, framing correction pipeline, active-negative agency, headline override, security context adjustment, self-referential investigation detection |
| `test_source_stance.py` | 60 | Source extraction, stance classification, outsourced intensity, power asymmetry, counted anonymous sources, no-comment exclusion, product name stop-filter, kicker framing, isolation/pressure as adversarial devices |
| `test_source_extraction_fixes.py` | 26 | Pattern 3 case-insensitivity fix, Pattern 5c verb-before-surname, attribution verb expansion (thinks/believes/considers/cautions), "called" naming-context filter, geographic/org false positives |
| `test_asymmetry.py` | 22 | Asymmetry score calculation, Welch's t-test, Cohen's d, bootstrap confidence intervals |
| `test_careers.py` | 21 | Career data loading, migration detection, DiD analysis, leadership change analysis, bias decomposition |
| `test_nyt_article_improvements.py` | 28 | NYT-specific article analysis fixes: active-negative agency, workplace coercion language, investment-near-layoffs juxtaposition, source stop-word filter |
| `test_nyt_ai_reviews.py` | 33 | NYT AI voluntary review article: isolation framing, pressure language, regulatory passive framing, VADER positive-bias correction, regulatory favoritism, escalation amplification, entity euphemisms |
| `test_nyt_school_targeting.py` | 29 | NYT school targeting article: education topic, National PTA/Cornell entity detection, safety team overrule hypocrisy frame, role-based adversarial stance for plaintiff attorneys, ironic quotation, scale/magnitude |
| `test_platform_death.py` | 30 | Platform eulogy detection, melancholic vs hostile tone distinction, community source framing |
| `test_quality_standards.py` | 41 | Quality enforcement: banned AI-slop phrase detection (25 phrases, case-sensitive/insensitive), em dash limit enforcement, counterargument/limitations/methodology signal detection, score calculation, pass/fail logic |
| `test_citations.py` | 39 | Citation extraction: URL detection, source grading (primary/secondary/tertiary domain lists), domain extraction, attribution patterns ("according to"), formal citations ([1], (Author 2024)), deduplication, citation report statistics |
| `test_topics.py` | 35 | Topic classification: all 23 standardized topic buckets, confidence scoring (keyword coverage + density), top-N filtering, custom topic injection, multi-topic articles, child_safety addiction/harm framing, ai_ethics_safety alignment/philosopher, edge cases |
| `test_claims.py` | 28 | Claim-evidence mapping: statistic detection (percentages, dollar amounts, multipliers), quote detection, citation signal detection, assertion detection, source attribution, claim mapping, unsupported claims ratio, confidence scoring |
| `test_atlantic_analysis.py` | 31 | Atlantic-specific coverage analysis: Emerson Collective ownership conflicts, Apple/OpenAI financial interest detection, AI coverage framing patterns, data center environmental articles |
| `test_loaded_language_uproar.py` | 13 | Loaded language detection edge cases: workplace coercion terms, revolt vocabulary, "uproar" word variants, false-positive exclusion for neutral contexts |
| `test_scale_magnitude.py` | 16 | Scale/magnitude framing: raw number amplification, calculated maximums, cumulative totals, scale analogies, victim roster detection, comparison amplifiers |
| `test_glasses_deep_dive.py` | 17 | Wired glasses launch deep dive fixes: kicker framing (negative final paragraph detection), product-name stop-filter for source extraction ("Meta Glasses"), emotional_appeal false-positive exclusion (question marks), loaded language expansion (nefarious, comically, discreetly) |
| `test_gizmodo_fury_review.py` | 19 | Gizmodo Meta Fury contradictory review: entity detection (Fury, Adventurer, Starfire, Garmin, Llama 4), Path F framing correction for mixed product reviews, emotional terms (ickiness, glassholism, privacy minefield, spying, paranoid) |
| `test_hypocrisy_medical_duress.py` | 16 | Hypocrisy frame detection: "the only company that has not" patterns, medical duress framing, healthcare-as-leverage patterns, prepositional phrase tolerance in entity–negation gaps |
| `test_wynn_williams_fixes.py` | 18 | Guardian Wynn-Williams lawsuit fixes: source extraction false positives (day names "Wednesday", book titles "Careless People"), litigation framing expansion (complaint, suing, arbitration patterns), power_asymmetry per-violation fines with intervening adjectives |
| `test_virtue_ai_acquihire.py` | 14 | Virtue AI acqui-hire entity detection (Virtue AI, Bo Li, Dawn Song, Sanmi Koyejo, FAIR, BIS, CAISI, Howard Lutnick), ironic_quotation tech-jargon filter, emotional language additions |
| `test_sarcastic_correction.py` | 15 | Sarcastic correction framing device: concede-then-retract patterns ("Of course... oh wait"), standalone sarcastic constructions ("Who could have predicted"), false-positive exclusion for neutral uses of "of course" and "right" |
| `test_wired_gulag_patterns.py` | 17 | Wired "gulag" engineer revolt coverage: conscript/conscription workplace loaded language, keystroke/screen-recording surveillance detection, Scale AI entity detection, full article-context loaded language density |
| `test_cannes_contractors.py` | 32 | Wired "Cannes" contractors story: Scale AI/Covalen/Character.AI AI-Infrastructure clustering, catastrophizing "death of" proper-noun exclusion, Outlook software-product source exclusion, deception/impersonation loaded_language patterns, Business Insider/Daily Beast source fragment leak prevention, headline-aware topic boosting, cross-sentence industry_normalization_undercut detection |
| `test_postpass_activation.py` | 26 | Post-pass device activation: analogy_stacking threshold (3+ markers), speculative_framing threshold (5+ hedges), expanded loaded_language patterns, analogy_stacking false-positive regression (factual "is a" constructions vs qualified metaphors) |
| `test_jun27_regression.py` | 6 | Jun 27 regression tests: topic "fine" ambiguity (fine-tuned ≠ litigation), source extraction stop words ("Any"/"All" not person names), fined still matches litigation |
| `test_hackathon_revolt.py` | 13 | Wired hackathon employee revolt: Ime Archibong entity detection, workplace-discontent emotional terms, social_proof_amplification framing device, AI hackathon topic classification, composite sentiment on internal-morale articles |
| `test_structural_consistency.py` | 68 | Structural consistency guards: framing device type count (51 total = 45 pattern-matched + 6 structural), total regex pattern count (310 patterns across all pattern-matched types), `precedent_analogy` exists, `__main__.py` entry point works, doc counts match across METHODOLOGY.md/ARCHITECTURE.md/AGENT_GUIDE.md/CLI/README (framing types, banned phrases, Advance/Reddit voting power, topic bucket counts), test file listing completeness (every test file on disk appears in ARCHITECTURE.md and README.md, no phantoms, header count matches), README/ARCHITECTURE total test count header guards (validates pytest-collected count including parametrize expansions), stale voting power purge guards across all doc files, cross-reference consistency guards (no stale framing taxonomy count references in any doc, README test descriptions reference correct topic bucket and framing device counts), inline topic list validation (ARCHITECTURE.md, AGENT_GUIDE.md, METHODOLOGY.md topic names match code), quality standards banned phrase count and completeness guards, framing.py docstring count validation (pattern-matched and total counts match code), METHODOLOGY.md device table completeness (Extended and Structural tables contain all code device types), adversarial device type list consistency (METHODOLOGY.md, QUALITY_STANDARDS.md, and AGENT_GUIDE.md enumerate all 14 adversarial types from sentiment.py), ARCHITECTURE.md test_topics bucket count guard, ARCHITECTURE.md device name list completeness (Core and Extended inline lists enumerate all device types from code), AGENT_GUIDE.md framing tier count guard (49/10/34/5 matches code), correction path documentation completeness (all 7 sentiment correction paths A-G documented in METHODOLOGY.md, ARCHITECTURE.md, and AGENT_GUIDE.md with summary table), journalist count consistency (YAML journalist count matches README.md, EDITORIAL_HISTORIES.md, and careers_demo.py; multi-pub count matches docs; CareerTracker loads all journalists without error) |
| `test_mittr_anthropic_feud.py` | 25 | MIT TR "Three things to watch amid Anthropic's feud" article deep dive: entity detection (Fable, Mythos, Zhipu, Chinese AI cluster), scare quotes (doomers, exporting, wake-up call), speculative rhetorical questions (is it possible...?), cliffhanger questions (What will X bring?), loaded language (drastic, superficial), cross-domain precedent analogy (nuclear nonproliferation), speculative framing threshold, sovereignty framing, pattern unit tests |
| `test_government_oversight_topic.py` | 15 | government_oversight topic bucket (national security, export controls, AI regulation, military AI, beats product_launch on regulation articles, MIT TR Anthropic feud article), group_expert source detection (cybersecurity experts open letter, AI researchers joint statement, petition signed by experts, not anonymous) |
| `test_confession_framing.py` | 31 | Confession framing (#33): "admitted," "conceded," "finally acknowledged," "was forced to admit" reframing corporate statements as confessions. Cross-publication patterns (Guardian, NYT, Atlantic, MIT TR). False-positive exclusion for legal/judicial confessions, direct-quote self-description. Attribution asymmetry detection. |
| `test_delayed_defense_and_normalization.py` | 27 | Delayed defense (corporate response buried after 65% of article, including 'defended' verb), industry normalization undercut, headline boost strength, outsourced intensity document-catalog variant (reviewed documents with disturbing enumerated content), expanded child_safety keywords (suicide, self-harm, eating disorders, cyberbullying). |
| `test_precedent_analogy.py` | 22 | Precedent analogy framing: opioid/tobacco/asbestos crisis import via "echoes of," "much like," "following the playbook" patterns. Insurance entity detection (Hartford, Chubb, Flashlight Capital). Legal entity detection (Section 230, DSA, bellwether). Scale/magnitude expansions ("hundreds of millions," "tens of billions"). Analogy marker boundary fixes. |
| `test_resistance_patterns.py` | 35 | MIT TR Resistance article patterns: catastrophizing (threat to humanity), alarm/anxiety idioms, intensity/polemical/violence loaded language, poll-based social proof amplification, stalled-dollar and workforce-percentage scale magnitude. |
| `test_avclub_sardonic_framing.py` | 34 | AV Club sardonic framing stress test: ironic quotation (scare quotes around "predictions," "points," "content"), sarcastic correction (ironic denial "presumably has absolutely nothing to do with," mock-certainty "we're sure are just thrilled," post-quote deflation "You know, like how humans talk!"), loaded language (ad hominem "tech bros"/"gormless"/"lumbering," industry-as-vice "gambling addiction"/"sinking their hooks into"), cross-publication sardonic tone detection. |
| `test_arena_cross_analysis.py` | 18 | Cross-publication analysis: NYT vs Gizmodo on Arena prediction markets story — tone separation between neutral business scoop and adversarial entertainment coverage, emotional intensity scoring, ironic quotation filtering, agency detection on same-event coverage. |
| `test_latecomer_regulatory_framing.py` | 33 | Latecomer narrative (#36) and regulatory shadow (#37) framing devices: "exploring partnerships with," "joining the race," "playing catch-up," "market already dominated by" (latecomer narrative); "increasing scrutiny," "drawn scrutiny from," "amid antitrust," "could face regulatory," "raised concerns about" (regulatory shadow). Integration test on Arena article excerpt triggers both devices. False-positive exclusion for neutral partnerships and compliance language. |
| `test_editorial_deflation.py` | 33 | Editorial deflation framing device (#38): post-buildup dismissal phrases that puncture ambitious visions — "That's the idea, anyway," "or so X claims/hopes," "so the argument goes," "if it ever actually works," "in theory, anyway," "but that's a big if," "whether that actually pans out." Concession-then-dismissal variants: "Noble efforts, indeed, but," "That may be true, but." Integration test on MIT TR Anduril/Meta article excerpt. Negative cases exclude neutral hedging ("remains to be seen," "time will tell," standalone "in theory") and factual plan statements. |
| `test_memeburn_glasses_deep_dive.py` | 25 | Memeburn Meta glasses deep dive: open-ended-threat kicker patterns ("whether X catches up," "remains to be seen," "time will tell"), ubiquitous-camera loaded language ("camera on their face," "cameras everywhere," "recorded space," "no visible cue"), indirect/embedded rhetorical question ("critics ask what exactly...supposed to"), Gizmodo entity detection, full-article regression. |
| `test_child_safety_denial.py` | 6 | Engadget child safety features: denial_contradiction with "no evidence" denials, post-quote combative attribution (said/insisted vs called/described), replicated/verified as evidence counter-keywords, "misunderstanding" soft-denial patterns. |
| `test_worker_replacement_two_tier.py` | 16 | WebProNews Meta Dublin contractors: worker_replacement_irony patterns (forward/reverse/compact/chant forms, negative cases for generic layoffs and generic AI adoption), two_tier_treatment (denied privileges, full-time vs contractor severance, not-even-employees, negative case), geopolitical false positive fix (security guards/police "stood firm" suppressed, government still fires), outsourced_intensity expansion (labor-law expert "open season"/"cynical"/"utter inability"). |
| `test_child_safety_analysis.py` | 16 | NYT child safety study: new entity clusters (US Congress, Academic/Research, Research Centers, Child Safety Researchers/Legislation, Australia), source extraction fixes (case-sensitive [Aa]n?, expanded _KNOWN_ORGS, direct org attribution), new framing devices (analogy_metaphor, taxonomy_framing), agency attribution sparse-data dampening. |
| `test_mit_tr_anduril_meta_warfare_glasses.py` | 30 | MIT TR Anduril/Meta warfare glasses: defense-tech entity detection (Anduril, EagleEye, SBMC), failure_precedent framing device (new — Microsoft $22B cancelled contract), analogy_stacking false-positive filters (factual similes, memory-verb "recalls that"), context-gated Llama entity alias (case-sensitive with model/AI/LLM lookahead), selective_rehabilitation (Palmer Luckey), editorial_deflation ("That's the idea, anyway"), sentiment calibration for neutral-skeptical military reporting |

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
