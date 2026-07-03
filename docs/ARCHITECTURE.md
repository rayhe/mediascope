# Architecture

## System Overview

MediaScope is a modular Python toolkit organized into seven functional layers, plus a dedicated Editorial Histories subsystem for causal bias attribution:

```
┌──────────────────────────────────────────────────────────────────────┐
│                        CLI / Agent Interface                        │
│                     mediascope/cli.py                                │
│                                                                      │
│   Commands: ingest, analyze, score, report, disclose,               │
│             add-publication, list-publications, status               │
│   Subgroups: careers (list, show, migrations, leadership, diff,     │
│              analyze)                                                │
└──────────────┬───────────────────────────────────────┬───────────────┘
               │                                       │
┌──────────────▼───────────────┐     ┌─────────────────▼──────────────┐
│         INGEST               │     │          CONFLICTS             │
│                              │     │                                │
│  rss.py      → RSS feeds     │     │  ownership.py  → chain mapper  │
│  scraper.py  → full text     │     │  revenue.py    → revenue links │
│  archive.py  → Wayback       │     │  litigation.py → funding nets  │
│                              │     │  disclosure.py → disclosures   │
└──────────────┬───────────────┘     └────────────────────────────────┘
               │
┌──────────────▼───────────────┐
│         ANALYZE              │
│                              │
│  entities.py  → NER + regex  │
│  topics.py    → topic class  │
│  sentiment.py → 8-dim score  │
│  framing.py   → device detect│
│  sources.py   → source auth  │
│               + stance       │
│               + outsourced   │
│                 intensity    │
│               + power asym   │
└──────────────┬───────────────┘
               │
┌──────────────▼───────────────┐     ┌────────────────────────────────┐
│          SCORE               │     │          QUALITY               │
│                              │     │                                │
│  asymmetry.py → AS formula   │     │  standards.py → slop detect    │
│  byline.py    → journalist   │     │  citations.py → source verify  │
│  statistical.py → tests      │     │  claims.py    → claim mapping  │
└──────────────┬───────────────┘     └────────────────────────────────┘
               │
┌──────────────▼───────────────┐     ┌────────────────────────────────┐
│          REPORT              │     │          STORAGE               │
│                              │     │                                │
│  weekly.py    → MD reports   │     │  models.py → SQLAlchemy models │
│  dashboard.py → HTML dash    │     │  db.py     → CRUD operations   │
│  disclosure.py → re-export   │     │                                │
└──────────────────────────────┘     └────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│              CAREERS — Editorial Histories (Novel)                   │
│                                                                      │
│  models.py              → Data models (JournalistProfile, Migration, │
│                            CareerEvent, LeadershipChange)            │
│  tracker.py             → Career data loader + journalist lookup     │
│  migrations.py          → DiD analysis on journalist moves           │
│  editorial_leadership.py→ ITS analysis on leadership changes         │
│  influence.py           → Bias decomposition (two-way ANOVA),        │
│                            portable bias scoring                     │
└──────────────────────────────────────────────────────────────────────┘
```

## Data Flow

### Primary Analysis Pipeline

```
RSS Feeds ──→ Article Text ──→ Entity Detection ──→ Sentiment Analysis
                                      │                     │
                                      ▼                     ▼
                              Topic Classification   Framing Detection
                                      │                     │
                                      └──────┬──────────────┘
                                             │
                                             ▼
                                    ┌─────────────────┐
                                    │ Source Analysis  │
                                    │  • Authority     │
                                    │  • Stance        │
                                    │  • Outsourced    │
                                    │    intensity     │
                                    │  • Power asymm   │
                                    └────────┬────────┘
                                             │
                                             ▼
                                    Asymmetry Scoring
                                    (Welch's t-test)
                                             │
                                    ┌────────┴────────┐
                                    ▼                  ▼
                              Weekly Report      Disclosure
                              (MD/HTML/JSON)     Statement
```

### Sentiment Correction Pipeline

The toolkit uses a multi-layer correction pipeline with **8 distinct paths (A–H)** that addresses known VADER/TextBlob blind spots when scoring editorial prose:

```
Raw Text
  │
  ├── VADER baseline score ──────┐
  │   │                          │
  │   └── Path G: Long-text      │    (fixes VADER math before
  │       normalization          │     composite is computed)
  │                              │
  ├── TextBlob baseline score ───┤
  │                              ├──→ Composite raw score
  └── (Optional) LLM score ─────┘          │
                                           ▼
                                 Framing Device Detection
                                 (53 device types, 320 patterns)
                                           │
                                           ▼
                                 Active-Negative Agency Check
                                 ("tracking," "cutting," "forcing"
                                  vs. "launching," "innovating")
                                           │
                                           ▼
                                 Framing Correction Router
                                 (first matching path fires)
                                    │
           ┌────────┬──────────┬────┼────┬──────────┐
           ▼        ▼          ▼    ▼    ▼          ▼
        Path A   Path B    Path C  Path E  Path D  Path F  Path H
        Full     Amplify   Anchor  Mil.   Sardonic Contra- Sarcastic
        correct  understat embed   techno mocking  dictory editorial
                                   optim          review
                                           │
                                           ▼
                                 Corrected Composite Score
```

Each path addresses a specific VADER failure mode discovered through real article analysis:

| Path | Failure Mode | Key Trigger | Blend Ratio |
|---|---|---|---|
| **A** | VADER wrong direction on adversarial prose | raw ≥ 0, agency < −0.3, ≥3 adv. devices | 10% raw / 90% framing |
| **B** | VADER understates negative magnitude | raw ∈ (−0.5, 0), agency < −0.3, ≥6 adv. | 50% raw / 50% framing |
| **C** | Anchor devices in product reviews | raw > 0.3, agency ≥ 0, ≥2 anchors | 55% raw / 45% target |
| **D** | Sardonic contempt via loaded language | raw ≥ 0.3, agency ≥ 0.3, ≥7 loaded | 10% raw / 90% sardonic |
| **E** | Military aspirational language inflation | raw ≥ 0.3, agency < 0, ≥3 MTO devices | 30% raw / 70% framing |
| **F** | Positive product reviews with negative editorial wrapper | raw ≥ 0.3, agency ∈ [−0.4, 0), EI ≥ 0.5 | 20% raw / 80% review |
| **G** | VADER long-text alpha normalization distortion | ≥10 sentences, divergence > 0.5 | 30% compound / 70% sentence |
| **H** | Sarcastic short editorial tone | raw ≥ 0.3, agency ≥ −0.1, ≥2 editorial_aside, EI ≥ 0.5 | 15% raw / 85% target |

Only one framing path (A–F, H) fires per article. Path G runs independently before the composite is computed, correcting VADER's input signal. See [METHODOLOGY.md §9.2](METHODOLOGY.md#92-correction-pipeline) for full trigger conditions, blend formulas, and discovery articles.

### Editorial Histories Pipeline (Causal Analysis)

```
Journalist YAML ──→ Career Tracker ──→ Migration Detection
                                              │
                              ┌────────────────┼────────────────┐
                              ▼                ▼                ▼
                      Source-Side DiD    Portable Bias    Dest-Side DiD
                      (did Publication   (did journalist   (did Publication
                       A change after    carry tone to     B change after
                       journalist left?) new outlet?)      journalist arrived?)
                              │                │                │
                              └────────┬───────┘                │
                                       ▼                        ▼
                              Bias Decomposition         Leadership ITS
                              (Two-Way ANOVA:            (Interrupted
                               institutional vs.          Time-Series for
                               individual vs.             EIC/ME changes)
                               interaction)
```

## Analyze Layer — Module Detail

### `entities.py`
- Regex-based entity detection with word-boundary matching
- Configurable entity clusters (dict format with custom regex, or list shorthand)
- Negative lookahead patterns to avoid false positives (e.g., "Apple pie", "Meta tag")
- `get_primary_entity()` returns the dominant entity in an article

### `sentiment.py`
- Three-layer sentiment: VADER (0.25), TextBlob (0.25), optional LLM (0.5)
- Eight-dimension scoring: overall tone, emotional intensity, source authority, agency attribution, headline-body alignment, anonymous source ratio, speculative language ratio, comparative framing
- **Active-negative agency detection**: Distinguishes "tracking users" (harmful active) from "launching products" (positive active), feeding into tone correction
- **Framing-aware tone correction**: When VADER scores prose as positive but framing devices and agency signals are adversarial, the corrected score reflects the editorial stance. The `SentimentResult` includes both `raw_overall_tone` and `overall_tone` (corrected) plus metadata fields documenting when and why correction fired
- **Security context adjustment**: Technical security/hacking articles use domain-specific language that inflates emotional intensity; the scorer reduces intensity for articles matching security topic patterns

### `framing.py`
- **53 framing device types** organized in three tiers:
  - **Core (10):** guilt by association, anonymous authority, catastrophizing, false balance, selective omission signal, emotional appeal, loaded language (including workplace coercion/revolt terms), power asymmetry, CEO personalization, litigation framing
  - **Extended (37):** straw man, refusal amplification, juxtaposition (including investment-near-layoffs), timeline implication, military techno-optimism, selective rehabilitation, rhetorical question, ironic quotation, isolation framing, pressure language, self-referential investigation (publication citing its own prior reporting as evidence within adversarial coverage), geopolitical regulatory pressure, sovereignty framing, scale/magnitude framing, corporate reassurance undercut, hypocrisy frame (singling out an entity as the sole holdout among peers, framing inaction as moral failing), sarcastic correction (editorial sarcasm that mockingly concedes a point before retracting it), outsourced intensity (loaded language in legal filings/complaints quoted by neutral editorial prose), precedent analogy (editorial device importing settled villainy from prior crises — opioid, tobacco, asbestos — onto a current subject via era-based comparisons), confession framing (editorial device presenting corporate acknowledgments as forced admissions — "admitted," "conceded," "finally acknowledged" — reframing voluntary statements as reluctant confessions extracted under pressure), latecomer narrative (editorial device framing a company as entering a space after competitors, positioning it as playing catch-up — "exploring partnerships with," "joining the race," "playing catch-up" — rather than innovating independently), regulatory shadow (ambient technique of inserting regulatory/legal context into product or business stories where it is tangential), editorial deflation (editorial technique of building up an ambitious vision then puncturing it with a brief dismissive phrase — "That's the idea, anyway," "or so X claims," "if it ever actually works" — implying failure without explicit argument), denial contradiction (source's direct denial or minimization placed alongside contradicting evidence — "does not exist" near code analysis findings, combative "misleading"/"dishonest" pushback followed by removal evidence, soft "part of a pilot" editorially undercut), analogy/metaphor (explicit comparisons using "like," "akin to," "equivalent of" that import associations from a comparison domain — distinct from analogy_stacking which requires 3+), taxonomy framing (presenting findings using a structured classification system that implies completeness and authority — "broken, buried, or missing" leaves no escape route), failure precedent (invoking a prior failed attempt at the same project type to cast implicit doubt on the current effort — "was set to receive $X ... ultimately cancelled"), worker replacement irony (workers who built/trained the AI that now replaces them), two-tier treatment (contrasting treatment of full-time vs. contractor workers), regulatory favoritism (government oversight framed as picking winners and losers), escalation amplification (intensifying modifiers before threat/concern language), commodification metaphor (language flattening human identity/work into interchangeable modules, tokens, or data), pathologizing metaphor (addiction, disease, or bodily-excess language applied to corporate/institutional behavior — "addicted to," "gorge itself," "high-rollers" — framing strategy as compulsion), anthropomorphization (ascribing human emotions, intentions, cognition, or social roles to AI systems — "happily handed," "the confused bot," "without being taught how to" — converting design flaws into character traits), industry normalization undercut (acknowledging a practice is industry-wide then undercutting it to single out the target — "Other companies also X, but Meta's reliance is especially…"), assumed consensus (presenting a contested or unsupported claim as self-evident common knowledge — "People hate X," "Everyone knows," "Nobody wants" — skipping the burden of proof), editorial aside (breaking journalistic register to address the reader directly with sarcastic or solidarity-building interjections — "brace yourself," "let's be honest," "something tells me")
  - **Structural post-pass (6):** kicker framing (checks final ~400 chars for discordant negative note), analogy stacking (fires when 3+ distinct analogy markers found), speculative framing (fires when 5+ cumulative speculative hedges found — individual hedges are normal journalism; stacked hedges convert possibility into implied certainty), trend bundling (fires when 3+ distinct companies are bundled as comparisons — editorial technique of normalising or amplifying a target company's action by assembling an industry-wide pattern), social proof amplification (detects when articles cite reaction counts — likes, thumbs-up, hearts — to convert individual opinion into collective sentiment), delayed defense (first corporate response appears after 65% of article text — the rebuttal is buried after the accusatory framing)
- Attribution verb analysis: neutral ("said"), undermining ("claimed"), concessive ("admitted"), adversarial ("warned")
- **Workplace coercion/revolt language detection**: Terms like "no opt-out," "revolt," "nihilistic," "training their own replacements" detected as loaded language specific to labor/workplace framing
- **Investment-near-layoffs juxtaposition detection**: Pattern where large spending figures ($X billion) appear near workforce cuts, an editorial device implying corporate indifference

### `sources.py`
- **Source extraction**: Named and anonymous source detection with stop-word filtering (prevents false extractions like "After Meta said" → source "After Meta")
- **Appositive source extraction**: Handles "Name, Title at Company, said" patterns
- **Counted anonymous source detection**: Identifies "two employees said," "three people familiar with" patterns that standard regex misses — anonymous sources disguised as specificity
- **No-comment signal tagging**: "Declined to comment," "did not respond to a request for comment" tagged as `source_type="no_comment"` and excluded from source counts — these are editorial signals, not source attributions
- **Source authority grading**: Primary (SEC, court records) > Secondary (Reuters, AP) > Tertiary (blogs, social media)
- **Source stance analysis**: Classifies each source as adversarial, supportive, or neutral based on quote content + attribution verbs. Computes `stance_balance` from −1.0 (all adversarial) to +1.0 (all supportive)
- **Outsourced intensity detection**: Splits text into quoted vs. editorial prose, measures emotional intensity in each. High outsourced ratio (>0.5) means the journalist delegates emotional impact to sources while maintaining measured prose — a sophisticated editorial technique that defeats lexical sentiment analysis
- **Power asymmetry framing detection**: Dollar-magnitude near individual vulnerability, "army of lawyers" language, David vs Goliath constructions, fine-per-violation-could-bankrupt patterns

### `topics.py`
- TF-IDF weighted keyword classification into 25 topic buckets
- Multi-label (top 3 by confidence retained)
- Topics: layoffs, ai_development, privacy_data, antitrust_regulation, child_safety, content_moderation, ai_generated_content, financial_results, product_launch, executive_behavior, litigation, prediction_markets, corporate_strategy, defense_military, labor_market, workplace_culture, government_oversight, infrastructure_impact, worker_ai_displacement, health_tech, cybersecurity, ai_ethics_safety, education, subscription_monetization, hardware_wearables

## Careers Layer — Module Detail

### `models.py`
Data classes for the Editorial Histories subsystem:
- `CareerEvent`: A single position (publication, role, beat, dates, notes)
- `JournalistProfile`: Full career with events, computed properties (current outlet, migrations, publications worked at, career span)
- `Migration`: Movement between two publications with gap analysis and type classification (lateral, promotion, move)
- `LeadershipChange`: Editorial leadership transition at a publication (position, incoming/outgoing, date, notes)

### `tracker.py`
- Loads career data from `profiles/careers/journalists.yaml`
- Case-insensitive journalist lookup
- Migration detection: scans career events for consecutive positions at different tracked publications
- Filters by source/destination publication

### `migrations.py` — `MigrationAnalyzer`
- Implements the DiD framework from Card & Krueger (1994) adapted for editorial analysis
- Configurable analysis window (default 180 days before/after)
- Computes: DiD estimate, p-value, source-side raw change, destination-side raw change, journalist tone change, portable bias estimate
- Huber-White robust standard errors

### `editorial_leadership.py` — `LeadershipAnalyzer`
- Loads leadership changes from `profiles/careers/editorial_changes.yaml`
- Interrupted Time-Series (segmented regression): level shift (β₂) and slope change (β₃) when a new editor takes over
- Tests statistical significance of both immediate and gradual effects

### `influence.py` — `InfluenceScorer`
- Two-way ANOVA bias decomposition: SS_institutional + SS_individual + SS_interaction
- Portable Bias Score (0-1): 1 − |Cohen's d|/2 across publications
- Requires ≥2 publications with ≥5 articles each
- Confidence metric based on data volume

## Configuration

All configuration flows through `config.py`:

- **Publication profiles**: YAML files in `profiles/` directory
- **Career data**: YAML files in `profiles/careers/` directory
  - `journalists.yaml` — journalist career histories
  - `editorial_changes.yaml` — leadership transitions
- **Global config**: Environment variables or `mediascope.yaml` in working directory
- **Database**: SQLite (default) or PostgreSQL via `MEDIASCOPE_DB_URL`

## Storage

MediaScope uses SQLAlchemy with the following tables:

| Table | Purpose |
|---|---|
| `articles` | Ingested article text and metadata |
| `entity_mentions` | Detected entity mentions per article |
| `sentiment_scores` | 8-dimension sentiment scores per article (raw + corrected) |
| `framing_results` | Detected framing devices per article |
| `source_analyses` | Source authority, stance, and outsourced intensity per article |
| `asymmetry_results` | Calculated asymmetry scores per period |
| `conflict_records` | Mapped conflicts of interest |

Default storage is SQLite (`mediascope.db` in working directory). For production use, point `MEDIASCOPE_DB_URL` to PostgreSQL.

## Extension Points

### Custom Entity Clusters

Define entity clusters in publication profiles or pass custom clusters to `detect_entities()`:

```python
custom_clusters = {
    "Exxon": {
        "aliases": ["ExxonMobil", "Exxon Mobil", "XOM"],
        "regex": r"\b(Exxon|ExxonMobil|XOM)\b"
    }
}
entities = detect_entities(text, clusters=custom_clusters)
```

### Custom Sentiment Models

The sentiment pipeline is model-agnostic. Add new models by implementing the `SentimentResult` interface:

```python
def my_custom_model(text: str, headline: str = "") -> SentimentResult:
    # Your model here
    return SentimentResult(
        overall_tone=score,
        # ... other dimensions
    )
```

### Custom Quality Rules

Add banned phrases or quality rules in `quality/standards.py`:

```python
from mediascope.quality.standards import BANNED_PHRASES
BANNED_PHRASES.extend(["my_custom_banned_phrase"])
```

### Custom Framing Devices

Extend the framing detection by adding new device patterns. The framing detector uses regex patterns and keyword lists, so new devices can be added without changing the core logic.

### Custom Source Stance Terms

The source stance classifier uses configurable lists of negative and positive stance terms plus adversarial attribution verbs. Add domain-specific terms for specialized coverage areas (e.g., environmental, financial, defense).

## Dependencies

### Required
- Python 3.10+
- click, pyyaml, feedparser, newspaper3k, requests, beautifulsoup4
- spacy (with en_core_web_sm model)
- textblob, vaderSentiment
- scipy, numpy, pandas
- jinja2, rich
- sqlalchemy

### Optional
- transformers + torch (GPU-accelerated sentiment analysis)
- openai (GPT-4o-mini editorial tone analysis)

## File Layout

```
mediascope/
├── mediascope/
│   ├── __init__.py
│   ├── cli.py              # Click CLI with commands + careers subgroup
│   ├── config.py            # Profile loading, env vars, paths, global config
│   ├── profiles.py          # Profile re-exports + validation (CLI shim)
│   ├── analysis.py          # ArticleAnalyzer orchestrator (CLI shim)
│   ├── scoring.py           # AsymmetryScorer orchestrator (CLI shim)
│   ├── reports.py           # ReportGenerator orchestrator (CLI shim)
│   ├── disclosure.py        # DisclosureGenerator orchestrator (CLI shim)
│   ├── db.py                # MediaScopeDB re-export (CLI shim)
│   ├── analyze/
│   │   ├── entities.py      # Entity detection + clustering
│   │   ├── sentiment.py     # 8-dim scoring + framing correction
│   │   ├── framing.py       # Framing device detection
│   │   ├── sources.py       # Source authority, stance, outsourced intensity
│   │   └── topics.py        # Topic classification
│   ├── careers/
│   │   ├── models.py        # CareerEvent, JournalistProfile, Migration, etc.
│   │   ├── tracker.py       # Career data loading + lookup
│   │   ├── migrations.py    # DiD analysis
│   │   ├── editorial_leadership.py  # ITS analysis
│   │   └── influence.py     # Bias decomposition + portable bias
│   ├── conflicts/
│   │   ├── ownership.py     # Ownership chain parsing
│   │   ├── revenue.py       # Revenue relationship mapping
│   │   ├── litigation.py    # Litigation funding network
│   │   └── disclosure.py    # Disclosure statement generation
│   ├── ingest/
│   │   ├── rss.py           # RSS feed fetching
│   │   ├── scraper.py       # Full-text extraction
│   │   └── archive.py       # Wayback Machine integration
│   ├── quality/
│   │   ├── standards.py     # AI slop detection, banned phrases
│   │   ├── citations.py     # Citation density + source grading
│   │   └── claims.py        # Claim-to-source mapping
│   ├── report/
│   │   ├── weekly.py        # Markdown report generation
│   │   ├── dashboard.py     # HTML dashboard generation
│   │   └── disclosure.py    # Disclosure re-export
│   ├── score/
│   │   ├── asymmetry.py     # Asymmetry Score formula
│   │   ├── byline.py        # Per-journalist profiling
│   │   └── statistical.py   # Welch's t, Cohen's d, bootstrap CI
│   └── storage/
│       ├── models.py        # SQLAlchemy table definitions
│       └── db.py            # CRUD operations
├── profiles/
│   ├── _template.yaml
│   ├── wired.yaml
│   ├── nytimes.yaml
│   ├── guardian.yaml
│   ├── atlantic.yaml
│   ├── mit-tech-review.yaml
│   └── careers/
│       ├── journalists.yaml
│       └── editorial_changes.yaml
├── docs/
│   ├── METHODOLOGY.md
│   ├── EDITORIAL_HISTORIES.md
│   ├── AGENT_GUIDE.md
│   ├── ADDING_PUBLICATIONS.md
│   ├── QUALITY_STANDARDS.md
│   └── ARCHITECTURE.md      # (this file)
├── examples/
│   ├── quick_start.py
│   ├── full_pipeline.py
│   ├── same_event_comparison.py
│   ├── framing_correction_demo.py
│   ├── agent_integration.py
│   └── sample_output/       # Annotated real-article analyses
├── tests/                       # 1207 tests across 46 test files (all from real articles)
│   ├── test_analyst_quote_attribution.py # Analyst/financial quote attribution: firm-level post-attribution suppression, wire cross-citation filtering, genuine scare quote preservation
│   ├── test_asymmetry.py        # Asymmetry score, Welch's t, Cohen's d, bootstrap CI
│   ├── test_atlantic_analysis.py # Atlantic-specific: Emerson Collective conflicts, AI coverage
│   ├── test_avclub_sardonic_framing.py # AV Club sardonic framing: sarcastic_correction sub-patterns, loaded_language ad hominem/industry-as-vice, ironic denial regex
│   ├── test_careers.py          # Career loading, migration detection, DiD, leadership ITS
│   ├── test_citations.py       # Citation extraction, source grading, domain classification
│   ├── test_claims.py          # Claim-to-source mapping, statistic/quote detection
│   ├── test_entities.py        # Entity detection, regex, false-positive exclusion
│   ├── test_glasses_deep_dive.py # Glasses launch fixes: kicker framing, product-name stop-filter, emotional_appeal exclusion
│   ├── test_gizmodo_fury_review.py # Gizmodo Meta Fury contradictory review: entity detection, Path F tone correction, emotional terms
│   ├── test_hypocrisy_medical_duress.py # Hypocrisy frame detection, medical duress framing, healthcare-as-leverage patterns
│   ├── test_loaded_language_uproar.py # Loaded language detection, workplace coercion terms
│   ├── test_nyt_ai_reviews.py   # Isolation framing, pressure language, VADER correction
│   ├── test_nyt_article_improvements.py  # NYT-specific: agency, coercion, juxtaposition
│   ├── test_nyt_school_targeting.py  # NYT school targeting: education topic, National PTA entity, safety team overrule hypocrisy, role-based adversarial stance
│   ├── test_platform_death.py   # Platform eulogy detection, tone distinction
│   ├── test_privacy_affiliation_fixes.py # Privacy/data topic MCI keyword expansion, source affiliation case-sensitivity
│   ├── test_quality_standards.py # Quality enforcement: banned phrases, em dashes, scoring
│   ├── test_scale_magnitude.py  # Scale/magnitude framing, raw number amplification
│   ├── test_sentiment.py        # 8-dim scoring, framing correction, self-referential detection
│   ├── test_source_stance.py    # Source extraction, stance, outsourced intensity, kicker framing
│   ├── test_source_extraction_fixes.py # Pattern 3 case fix, Pattern 5c verb-before-surname, attribution verb expansion
│   ├── test_topics.py           # Topic classification, all 25 buckets, confidence scoring
│   ├── test_wynn_williams_fixes.py # Litigation framing, source extraction false positives, power asymmetry
│   ├── test_virtue_ai_acquihire.py # Virtue AI entities, FAIR, BIS/CAISI, tech-jargon ironic_quotation filter
│   ├── test_sarcastic_correction.py # Sarcastic correction framing: concede-then-retract, standalone sarcasm, false-positive exclusion
│   ├── test_wired_gulag_patterns.py # Wired "gulag" coverage: conscript terms, keystroke surveillance, Scale AI entity, article-context loaded language
│   ├── test_cannes_contractors.py # Wired "Cannes" contractors: Scale AI/Covalen/Character.AI cluster, catastrophizing "death of" fix, Outlook source exclusion, deception/impersonation patterns
│   ├── test_confession_framing.py # Confession framing: "admitted," "conceded," voluntary-to-forced-admission reframing, false-positive exclusion
│   ├── test_delayed_defense_and_normalization.py # Delayed defense (corporate response buried late in article), industry normalization undercut (acknowledging then singling out), headline boost strength for child_safety topic
│   ├── test_government_oversight_topic.py # government_oversight topic bucket: national security, export controls, AI regulation, group_expert source detection
│   ├── test_jun27_regression.py # Regression tests for Jun 27 fixes across multiple analysis modules
│   ├── test_hackathon_revolt.py # Wired hackathon revolt: entity, sentiment, framing, topic tests
│   ├── test_mittr_anthropic_feud.py # MIT Tech Review Anthropic feud article: entity detection, framing, topic classification
│   ├── test_postpass_activation.py # Structural post-pass framing activation: analogy stacking, speculative framing thresholds
│   ├── test_precedent_analogy.py # Precedent analogy framing: opioid/tobacco/asbestos crisis comparisons, era-based villainy import
│   ├── test_resistance_patterns.py # MIT TR Resistance article patterns: catastrophizing (threat to humanity), alarm/anxiety idioms, intensity/polemical/violence loaded language, poll-based social proof, stalled-dollar and workforce-percentage scale magnitude
│   ├── test_structural_consistency.py # Structural consistency: framing device type registry completeness, total regex pattern count guard (320 patterns), doc count sync guards, test file listing guards, README/ARCHITECTURE total test count header guards (validates pytest-collected count including parametrize expansions), stale voting power purge across all doc files, cross-reference consistency (stale framing taxonomy count purge, README topic bucket count guard), inline topic list validation (ARCHITECTURE.md, AGENT_GUIDE.md, METHODOLOGY.md topic names match code), quality standards banned phrase count and completeness guards, framing.py docstring count and device list completeness validation, ARCHITECTURE.md extended device count label guard, ARCHITECTURE.md device name list completeness (Core + Extended inline lists enumerate all device types from code), ARCHITECTURE.md test_topics bucket count guard, METHODOLOGY.md device table completeness (Extended + Structural tables vs code), adversarial device type list consistency (METHODOLOGY.md + QUALITY_STANDARDS.md + AGENT_GUIDE.md vs sentiment.py), stale regex pattern count purge (ARCHITECTURE.md + README.md), AGENT_GUIDE.md framing tier count guard (53/10/37/6 matches code), correction path documentation completeness (all 8 paths A-H in METHODOLOGY.md + ARCHITECTURE.md + AGENT_GUIDE.md with summary table), migration count and publication count floor guards (README.md + EDITORIAL_HISTORIES.md)
│   ├── test_arena_cross_analysis.py # Cross-publication analysis: NYT vs Gizmodo on Arena story — tone separation, emotional intensity, ironic quotation filtering, agency detection
│   ├── test_latecomer_regulatory_framing.py # Latecomer narrative and regulatory shadow framing: catch-up/copycat positioning, ambient regulatory context insertion, Arena article integration
│   ├── test_editorial_deflation.py     # Editorial deflation framing: post-buildup dismissal phrases ("That's the idea, anyway"), attribution-as-skepticism, MIT TR Anduril article integration
│   ├── test_memeburn_glasses_deep_dive.py # Memeburn Meta glasses deep dive: open-ended-threat kicker patterns, ubiquitous-camera loaded language, indirect rhetorical question, Gizmodo entity detection
│   ├── test_child_safety_denial.py # Engadget child safety features: denial_contradiction with "no evidence" denials, post-quote combative attribution (said/insisted), replicated/verified evidence counters
│   ├── test_worker_replacement_two_tier.py # WebProNews Meta Dublin contractors: worker_replacement_irony (trained AI that replaced them), two_tier_treatment (contractor vs full-time), geopolitical false positive fix (physical "stood firm"), outsourced_intensity expansion (labor-law expert quotes)
│   ├── test_child_safety_analysis.py # NYT child safety study analysis: new entity clusters (US Congress, Academic/Research, Research Centers, Child Safety Researchers/Legislation, Australia), source extraction fixes (case-sensitive [Aa]n?, expanded _KNOWN_ORGS, direct org attribution), new framing devices (analogy_metaphor, taxonomy_framing), agency attribution sparse-data dampening
│   ├── test_mit_tr_anduril_meta_warfare_glasses.py # MIT TR Anduril/Meta warfare glasses: defense-tech entity detection, failure_precedent (new device), analogy_stacking FP filters (factual similes, recall verb), context-gated Llama entity, selective_rehabilitation, editorial_deflation, sentiment calibration
│   └── fixtures/
├── pyproject.toml
├── requirements.txt
├── iteration-log.md
└── LICENSE
```
