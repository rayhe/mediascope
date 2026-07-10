# Agent Guide

## Overview

MediaScope is designed to be used by AI agents — autonomous systems that can install, configure, and run the toolkit without human intervention. This guide covers integration patterns for any agentic AI framework.

## Installation

```bash
# Standard install
pip install mediascope

# From source (for development)
git clone https://github.com/mediascope/mediascope.git
cd mediascope
pip install -e ".[dev]"

# Download spaCy model
python -m spacy download en_core_web_sm

# Optional: GPU-accelerated transformer models
pip install mediascope[gpu]

# Optional: OpenAI API for editorial tone analysis
pip install mediascope[openai]
```

### Environment Variables

```bash
export MEDIASCOPE_PROFILES_DIR="./profiles"     # Publication profiles directory
export MEDIASCOPE_DB_URL="sqlite:///mediascope.db"  # Database URL
export MEDIASCOPE_OPENAI_KEY="sk-..."           # Optional: OpenAI API key
export MEDIASCOPE_OUTPUT_DIR="./output"          # Report output directory
```

## CLI Commands

Each command is designed for pipeline use — it accepts structured input and produces structured output.

### `mediascope ingest`

Fetches and stores articles from a publication's RSS feeds.

```bash
mediascope ingest --publication wired --since 2025-01-01 --until 2025-06-15
```

**Input**: Publication slug, date range
**Output**: Article count, storage confirmation
**Side effects**: Articles stored in database

### `mediascope analyze`

Runs entity detection, sentiment analysis, and framing detection on stored articles.

```bash
mediascope analyze --publication wired --target Meta --since 2025-01-01
```

**Input**: Publication slug, target entity, date range
**Output**: Analysis results (JSON when `--format json` is used)
**Side effects**: Analysis results stored in database

### `mediascope score`

Calculates asymmetry scores with statistical significance testing.

```bash
mediascope score --publication wired --target Meta --period weekly
```

**Input**: Publication slug, target entity, period
**Output**: Asymmetry scores with p-values and effect sizes

### `mediascope report`

Generates comprehensive reports.

```bash
mediascope report --publication wired --target Meta --format md > report.md
mediascope report --publication wired --target Meta --format html > dashboard.html
mediascope report --publication wired --target Meta --format json > report.json
```

**Formats**: `md` (Markdown), `html` (standalone dashboard), `json` (machine-readable)

### `mediascope disclose`

Generates conflict of interest disclosure statements.

```bash
# Full disclosure
mediascope disclose --publication wired --target Meta --format full

# Social media format (short)
mediascope disclose --publication wired --target Meta --format social

# Machine-readable
mediascope disclose --publication wired --target Meta --format json
```

### `mediascope add-publication`

Creates a new publication profile.

```bash
# Interactive mode
mediascope add-publication --name "Fox News" --slug fox-news --url https://foxnews.com --interactive

# From template
mediascope add-publication --name "Fox News" --slug fox-news --url https://foxnews.com
```

### `mediascope list-publications`

Lists all configured publication profiles.

```bash
mediascope list-publications
```

**Output**: Table of publication names, slugs, conflict counts.

### `mediascope status`

Shows database statistics.

```bash
mediascope status
```

**Output**: Article counts, last ingest dates, analysis coverage.

### `mediascope careers list`

Lists all tracked journalists, their current outlets, roles, publication count, and migration count.

```bash
mediascope careers list
```

**Output**: Table of journalists with career metadata.

### `mediascope careers show`

Shows a journalist's full career timeline with all positions, migrations, and beat changes.

```bash
mediascope careers show "Karen Hao"
```

**Input**: Journalist name (case-insensitive)
**Output**: Career timeline table + detected migration events

### `mediascope careers migrations`

Lists all detected migration events between tracked publications.

```bash
# All migrations
mediascope careers migrations

# Filter by source publication
mediascope careers migrations --from-pub mit-tech-review

# Filter by destination
mediascope careers migrations --to-pub wired
```

**Input**: Optional `--from-pub` and `--to-pub` filters
**Output**: Table of journalist moves with dates, gap days, and type (lateral/promotion/move)

### `mediascope careers leadership`

Shows editorial leadership changes at a publication.

```bash
mediascope careers leadership wired
```

**Input**: Publication slug
**Output**: Table of leadership transitions with dates, positions, incoming/outgoing names

### `mediascope careers diff`

Runs difference-in-differences (DiD) causal analysis on a journalist's migration.

```bash
# Default 180-day window
mediascope careers diff "Karen Hao"

# Custom window, filtered to Meta coverage
mediascope careers diff "Karen Hao" --window 365 --target Meta

# Save results to JSON
mediascope careers diff "Karen Hao" -o results.json
```

**Input**: Journalist name, optional `--window` (days), `--target` (entity filter), `--output` (JSON file)
**Output**: DiD estimate with p-value, source/dest raw changes, journalist tone delta, portable bias estimate, article counts
**Prerequisites**: Articles must be ingested and analysed for the relevant publications

### `mediascope careers analyze`

Runs bias decomposition (two-way ANOVA) for a journalist with multi-publication coverage.

```bash
mediascope careers analyze "Karen Hao"
mediascope careers analyze "Karen Hao" -o decomposition.json
```

**Input**: Journalist name (requires ≥2 publications with ≥5 analysed articles each)
**Output**: Institutional/individual/interaction variance components, portable bias score (0-1), dominant source of bias, confidence metric

## Python API

For agents that prefer direct Python integration over CLI:

```python
from mediascope.config import load_profile, load_all_profiles
from mediascope.ingest.rss import fetch_all_feeds
from mediascope.ingest.scraper import extract_article
from mediascope.analyze.entities import detect_entities, get_primary_entity
from mediascope.analyze.sentiment import analyze_composite
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources, analyze_source_stance
from mediascope.analyze.sentiment import measure_outsourced_intensity
from mediascope.analyze.framing import detect_framing_devices  # power_asymmetry is a framing device type
from mediascope.analyze.topics import classify_topic
from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.byline import build_journalist_profiles
from mediascope.conflicts.ownership import parse_ownership_chain, find_conflicts
from mediascope.conflicts.disclosure import generate_disclosure
from mediascope.quality.standards import check_quality
from mediascope.quality.citations import extract_citations, grade_source
from mediascope.quality.claims import extract_claims, map_claims_to_evidence
from mediascope.report.weekly import generate_weekly_report
from mediascope.storage.db import init_db, store_article
from mediascope.careers.tracker import CareerTracker
from mediascope.careers.migrations import MigrationAnalyzer
from mediascope.careers.editorial_leadership import LeadershipAnalyzer
from mediascope.careers.influence import InfluenceScorer
```

### Full Pipeline Example

```python
from datetime import datetime, timedelta
from mediascope.config import load_profile
from mediascope.ingest.rss import fetch_all_feeds
from mediascope.ingest.scraper import extract_articles
from mediascope.analyze.entities import detect_entities, get_primary_entity
from mediascope.analyze.sentiment import analyze_composite
from mediascope.score.asymmetry import calculate_asymmetry

# 1. Load publication profile
profile = load_profile("wired")

# 2. Fetch recent articles
entries = fetch_all_feeds(profile)
since = datetime.now() - timedelta(days=7)
recent = [e for e in entries if e.published and e.published >= since]

# 3. Extract full article text
articles = extract_articles([e.url for e in recent])

# 4. Analyze each article
analyzed = []
for article in articles:
    entities = detect_entities(article.text)
    primary = get_primary_entity(entities)
    sentiment = analyze_composite(article.text, article.title)
    analyzed.append({
        "title": article.title,
        "url": article.source_url,
        "primary_entity": primary,
        "sentiment": sentiment,
        "entity_mentions": entities,
    })

# 5. Calculate asymmetry
meta_scores = [a["sentiment"].overall_tone for a in analyzed if a["primary_entity"] == "Meta"]
peer_scores = [a["sentiment"].overall_tone for a in analyzed if a["primary_entity"] != "Meta"]

if meta_scores and peer_scores:
    result = calculate_asymmetry(
        target_scores=meta_scores,
        peer_scores=peer_scores,
        target_entity="Meta",
        peer_entities=["Google", "Apple", "Amazon", "Microsoft"],
        publication_slug="wired",
        period_start=since,
        period_end=datetime.now(),
    )
    print(f"Asymmetry Score: {result.asymmetry_score:.3f}")
    print(f"p-value: {result.p_value:.4f}")
    print(f"Significant: {result.is_significant}")
```

## Financial Journalism: Known VADER Inflation

When analyzing financial/investor journalism (Motley Fool, Barron's, MarketWatch, Seeking Alpha, etc.), be aware that VADER systematically inflates scores by 0.3–0.5 points. This is documented in detail in [METHODOLOGY.md §16](METHODOLOGY.md#16-financial-journalism-sentiment-bias).

**Quick diagnostic:** If a financial article scores composite > +0.50 AND has ≥3 adversarial framing devices, trust the framing devices over the sentiment score. The editorial stance is likely more negative than the composite indicates.

**Recommended approach for financial articles:**

1. Run standard `analyze_composite()` + `detect_framing_devices()`
2. Check `classify_topic()` for `financial_results` confidence ≥ 0.4
3. If financial AND composite > 0.50 AND adversarial devices ≥ 3:
   - Report composite score with a caveat about financial genre inflation
   - Weight framing device types (`financial_reassurance`, `competitive_deficit`, `ironic_quotation`, `editorial_deflation`) as the primary editorial stance signal
   - Use `headline_body_alignment` < 0.4 as confirmation of bearish editorial stance

See [`examples/financial_journalism_demo.py`](../examples/financial_journalism_demo.py) for a worked example.

## Function Calling Schema

For AI agents that use function calling (OpenAI, Anthropic, etc.), here are the schemas:

### analyze_publication

```json
{
    "name": "analyze_publication",
    "description": "Analyze a publication's coverage of a target entity for bias and conflicts",
    "parameters": {
        "type": "object",
        "properties": {
            "publication_slug": {
                "type": "string",
                "description": "Publication identifier (e.g., 'wired', 'nytimes')"
            },
            "target_entity": {
                "type": "string",
                "description": "Entity to check for coverage asymmetry (e.g., 'Meta', 'Google')"
            },
            "since": {
                "type": "string",
                "format": "date",
                "description": "Start date for analysis (YYYY-MM-DD)"
            },
            "until": {
                "type": "string",
                "format": "date",
                "description": "End date for analysis (YYYY-MM-DD)"
            }
        },
        "required": ["publication_slug", "target_entity"]
    }
}
```

### generate_disclosure

```json
{
    "name": "generate_disclosure",
    "description": "Generate a conflict of interest disclosure for a publication's coverage",
    "parameters": {
        "type": "object",
        "properties": {
            "publication_slug": {
                "type": "string",
                "description": "Publication identifier"
            },
            "target_entity": {
                "type": "string",
                "description": "Entity covered by the publication"
            },
            "article_url": {
                "type": "string",
                "description": "Optional: specific article URL to disclose conflicts for"
            },
            "format": {
                "type": "string",
                "enum": ["full", "social", "json"],
                "description": "Disclosure format"
            }
        },
        "required": ["publication_slug", "target_entity"]
    }
}
```

### careers_diff

```json
{
    "name": "careers_diff",
    "description": "Run difference-in-differences causal analysis on a journalist's migration between publications",
    "parameters": {
        "type": "object",
        "properties": {
            "journalist_name": {
                "type": "string",
                "description": "Full journalist name (case-insensitive)"
            },
            "window_days": {
                "type": "integer",
                "default": 180,
                "description": "Analysis window in days before/after migration"
            },
            "target_entity": {
                "type": "string",
                "description": "Optional: entity to filter articles by (e.g. 'Meta')"
            }
        },
        "required": ["journalist_name"]
    }
}
```

### careers_analyze

```json
{
    "name": "careers_analyze",
    "description": "Run bias decomposition (two-way ANOVA) for a journalist with multi-publication coverage",
    "parameters": {
        "type": "object",
        "properties": {
            "journalist_name": {
                "type": "string",
                "description": "Full journalist name (case-insensitive). Requires coverage at ≥2 publications."
            }
        },
        "required": ["journalist_name"]
    }
}
```

### careers_list

```json
{
    "name": "careers_list",
    "description": "List all tracked journalists with current outlets, roles, publication count, and migration count"
}
```

### careers_leadership

```json
{
    "name": "careers_leadership",
    "description": "Show editorial leadership changes at a publication — EIC transitions, new editorial roles, managing editor changes",
    "parameters": {
        "type": "object",
        "properties": {
            "publication_slug": {
                "type": "string",
                "description": "Publication identifier (e.g., 'wired', 'nytimes', 'guardian')"
            }
        },
        "required": ["publication_slug"]
    }
}
```

### detect_framing_devices

```json
{
    "name": "detect_framing_devices",
    "description": "Detect editorial framing devices in article text. Returns a list of FramingDevice objects with device_type, evidence_text, and character offsets. Detects 92 device types across three tiers: core (10 pattern-matched), extended (75 from real-article analysis), and structural post-pass (7 heuristic-based).",
    "parameters": {
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "Full article text to scan for framing devices"
            }
        },
        "required": ["text"]
    }
}
```

### classify_topic

```json
{
    "name": "classify_topic",
    "description": "Classify an article into standardized topic buckets using keyword-based matching with confidence scoring. Returns TopicScore objects with topic name, confidence (0.0-1.0), and matched keywords. Articles can match multiple topics; the top 3 by confidence are retained. Confidence uses 60% keyword coverage + 40% density, with length-aware dampening: texts under 500 words receive proportionally reduced density scores to prevent short-text inflation (a 200-word blurb with 1 keyword match won't score the same density as a full article). 29 topic buckets: layoffs, ai_development, privacy_data, antitrust_regulation, child_safety, content_moderation, ai_generated_content, financial_results, product_launch, executive_behavior, litigation, prediction_markets, corporate_strategy, defense_military, labor_market, workplace_culture, government_oversight, infrastructure_impact, worker_ai_displacement, health_tech, cybersecurity, ai_ethics_safety, education, subscription_monetization, energy_climate, hardware_wearables, consumer_protection, content_licensing, financial_markets.",
    "parameters": {
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "Full article text to classify"
            }
        },
        "required": ["text"]
    }
}
```

### check_quality

```json
{
    "name": "check_quality",
    "description": "Run quality standards checks on MediaScope output text. Detects banned AI-slop phrases ('delve', 'tapestry', 'landscape', etc.), excessive em dashes (limit 3), missing counterargument/limitations/methodology sections. Returns a QualityReport with pass/fail, score (0-100), and itemized issues.",
    "parameters": {
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "Text to check against quality standards"
            },
            "metadata": {
                "type": "object",
                "description": "Optional metadata for context-aware checks"
            }
        },
        "required": ["text"]
    }
}
```

### analyze_source_stance

```json
{
    "name": "analyze_source_stance",
    "description": "Analyze the collective stance of sources in an article toward the subject entity. Measures whether sources are deployed adversarially (to undermine) or supportively (to defend). Returns stance_balance from -1.0 (all adversarial) to +1.0 (all supportive).",
    "parameters": {
        "type": "object",
        "properties": {
            "article_text": {
                "type": "string",
                "description": "Full article text. Sources are automatically extracted."
            },
            "target_entity": {
                "type": "string",
                "description": "Optional entity name for context-aware stance detection"
            }
        },
        "required": ["article_text"]
    }
}
```

### measure_outsourced_intensity

```json
{
    "name": "measure_outsourced_intensity",
    "description": "Detect outsourced emotional intensity — the editorial technique of deploying emotional quotes from sources while keeping prose neutral. Returns outsourced_ratio from 0.0 (no outsourcing) to 1.0 (all emotional language in quotes). Located in mediascope.analyze.sentiment, not sources.",
    "parameters": {
        "type": "object",
        "properties": {
            "article_text": {
                "type": "string",
                "description": "Full article text. Splits into quoted vs editorial segments automatically."
            }
        },
        "required": ["article_text"]
    }
}
```

### careers_migrations

```json
{
    "name": "careers_migrations",
    "description": "List all detected journalist migration events between tracked publications",
    "parameters": {
        "type": "object",
        "properties": {
            "from_pub": {
                "type": "string",
                "description": "Filter by source publication slug"
            },
            "to_pub": {
                "type": "string",
                "description": "Filter by destination publication slug"
            }
        }
    }
}
```

### extract_citations

```json
{
    "name": "extract_citations",
    "description": "Extract citations and source attributions from text. Detects URLs, 'according to' attributions, formal citation formats ([1], (Author 2024)), and in-text attributions. Each citation is graded by source authority: primary (SEC filings, court records, .gov), secondary (Reuters, AP, WSJ), or tertiary (blogs, social media, opinion). Returns a list of Citation objects with text, URL, source_type, and domain.",
    "parameters": {
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "Text to extract citations from"
            }
        },
        "required": ["text"]
    }
}
```

### extract_claims

```json
{
    "name": "extract_claims",
    "description": "Identify factual claims in text and classify by evidence type. Scans for statistics (percentages, dollar amounts, multipliers), quotes (attributed statements), citations (URLs, 'according to'), and bare assertions (unsupported factual claims). Each claim gets a confidence score (0.0-1.0) based on evidence strength. Use with map_claims_to_evidence() to get sourced/unsourced ratios.",
    "parameters": {
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "Article or report text to scan for claims"
            }
        },
        "required": ["text"]
    }
}
```

### map_claims_to_evidence

```json
{
    "name": "map_claims_to_evidence",
    "description": "Map extracted claims to their evidence status. Takes the output of extract_claims() and returns a structured summary: sourced claims, unsourced claims, claims grouped by evidence type (statistic, quote, citation, assertion), total count, and sourced_ratio (fraction of claims with verifiable sources). The sourced_ratio is a key quality metric — articles below 0.5 have more unsourced claims than sourced ones.",
    "parameters": {
        "type": "object",
        "properties": {
            "claims": {
                "type": "array",
                "description": "List of Claim objects from extract_claims()"
            }
        },
        "required": ["claims"]
    }
}
```

## Sample Agent Prompts

### For a general-purpose AI agent

```
You have access to MediaScope, a media bias analysis toolkit. When the user
asks about media coverage, bias, or conflicts of interest:

1. Use `mediascope list-publications` to see available profiles
2. Use `mediascope ingest --publication <slug> --since <date>` to fetch articles
3. Use `mediascope analyze --publication <slug> --target <entity>` to analyze
4. Use `mediascope score --publication <slug> --target <entity>` for statistics
5. Use `mediascope disclose --publication <slug> --target <entity>` for disclosures

For journalist-level causal analysis:
6. Use `mediascope careers list` to see tracked journalists
7. Use `mediascope careers migrations` to find personnel changes between publications
8. Use `mediascope careers diff "<name>"` for difference-in-differences analysis
9. Use `mediascope careers analyze "<name>"` for bias decomposition

Always include the methodology link and limitations in your response.
```

### For a research agent

```
You are a media accountability researcher using MediaScope. Your workflow:

1. Identify the publication and target entity
2. Ingest 90 days of articles
3. Run full analysis pipeline (entities, sentiment, framing, source stance)
4. Check quality standards on your output
5. Generate disclosure statements
6. Check if any journalist migrations are relevant (careers diff)
7. Write a report with counterarguments and limitations

Never claim causation from correlation. Always state what you cannot prove.
The DiD careers analysis is the only path to causal claims — and even then,
state the parallel trends assumption and sample size limitations.
```

## Input/Output Formats

### Article Input (JSON)

```json
{
    "title": "Article Title",
    "text": "Full article text...",
    "url": "https://example.com/article",
    "author": "Author Name",
    "published": "2025-06-15T10:00:00Z",
    "publication_slug": "wired"
}
```

### Sentiment Output (JSON)

```json
{
    "overall_tone": -0.342,
    "emotional_language_intensity": 0.45,
    "source_authority_framing": -0.28,
    "agency_attribution": -0.15,
    "headline_body_alignment": 0.72,
    "anonymous_source_ratio": 0.33,
    "speculative_language_ratio": 0.22,
    "comparative_framing": -0.41
}
```

### Asymmetry Output (JSON)

```json
{
    "publication_slug": "wired",
    "target_entity": "Meta",
    "peer_entities": ["Google", "Apple", "Amazon", "Microsoft"],
    "period_start": "2025-01-01",
    "period_end": "2025-06-15",
    "target_avg_tone": -0.342,
    "peer_avg_tone": -0.059,
    "asymmetry_score": -0.283,
    "article_count_target": 47,
    "article_count_peers": 312,
    "t_statistic": -3.847,
    "p_value": 0.00013,
    "cohens_d": 0.71,
    "confidence_interval_lower": -0.427,
    "confidence_interval_upper": -0.139,
    "is_significant": true
}
```

### Source Stance Output (JSON)

```json
{
    "sources": [
        {
            "name": "Sarah Miller",
            "role": "privacy researcher at Stanford",
            "stance": "adversarial",
            "quote_excerpt": "This is reckless disregard for user safety...",
            "attribution_verb": "warned"
        },
        {
            "name": "Meta spokesperson",
            "role": "company representative",
            "stance": "supportive",
            "quote_excerpt": "We take user privacy seriously...",
            "attribution_verb": "said"
        }
    ],
    "stance_balance": -0.33,
    "adversarial_count": 4,
    "supportive_count": 2,
    "neutral_count": 1,
    "outsourced_intensity": {
        "outsourced_ratio": 0.72,
        "editorial_intensity": 0.15,
        "quoted_intensity": 0.54,
        "editorial_word_count": 890,
        "quoted_word_count": 340
    },
    "power_asymmetry": {
        "detected": true,
        "patterns": ["financial_magnitude_near_individual", "fine_per_violation"]
    }
}
```

### DiD Analysis Output (JSON)

```json
{
    "journalist_name": "Karen Hao",
    "migration": {
        "from_publication": "mit-tech-review",
        "to_publication": "atlantic",
        "departure_date": "2022-04",
        "arrival_date": "2022-06"
    },
    "did_estimate": -0.187,
    "did_p_value": 0.023,
    "did_is_significant": true,
    "source_raw_change": -0.092,
    "dest_raw_change": -0.041,
    "journalist_tone_change": -0.033,
    "portable_bias_estimate": 0.82,
    "n_articles_pre": 23,
    "n_articles_post": 18,
    "window_days": 180
}
```

### Disclosure Output (JSON)

```json
{
    "publication": "Wired",
    "publication_slug": "wired",
    "target_entity": "Meta",
    "generated_at": "2025-06-15T10:00:00Z",
    "mediascope_version": "0.1.0",
    "ownership_chain": [
        {"name": "Wired", "entity_type": "publisher"},
        {"name": "Condé Nast", "entity_type": "parent_company"},
        {"name": "Advance Publications", "entity_type": "holding_company"},
        {"name": "Newhouse Family", "entity_type": "family_office"}
    ],
    "conflicts": [
        {
            "type": "investment",
            "severity": 5,
            "description": "Advance Publications holds 65.2% voting power in Reddit (83.5% of Class B shares, ~$7B)...",
            "evidence": "Reddit SEC filing"
        }
    ],
    "methodology_url": "https://github.com/mediascope/mediascope/blob/main/docs/METHODOLOGY.md"
}
```

## Same-Event Comparison Workflow

The most powerful evidence technique in MediaScope is comparing how different publications cover the **same event on the same day**. When the raw facts are held constant, any difference in tone, framing density, source selection, or structural choices is attributable to editorial DNA rather than event severity. This is the media-analysis equivalent of a controlled experiment.

See `METHODOLOGY.md` §13 for the full theoretical framework and `examples/same_event_comparison.py` for a runnable demo.

### Agent Workflow

```
1. Identify a shared event (same press release, court filing, earnings report)

2. Ingest both articles:
   mediascope ingest -p wired --since YYYY-MM-DD
   mediascope ingest -p reuters --since YYYY-MM-DD

3. Analyze both articles against the same target entity:
   mediascope analyze -p wired -t Meta --since YYYY-MM-DD
   mediascope analyze -p reuters -t Meta --since YYYY-MM-DD

4. Compare across seven dimensions:
   - Word count (editorial investment)
   - Tone score (8-dimension sentiment)
   - Framing device count and types (technique fingerprint)
   - Source roster (named vs anonymous, count, affiliations)
   - Source stance balance (adversarial vs supportive)
   - Outsourced intensity (who carries the emotional weight)
   - Structural choices (headline, kicker, paragraph order)

5. Use wire-service baseline:
   Wire tone ≈ event severity
   Magazine tone − wire tone ≈ editorial framing contribution
```

### Python API

```python
from mediascope.analyze.entities import detect_entities, get_primary_entity
from mediascope.analyze.sentiment import analyze_composite, measure_outsourced_intensity
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources, analyze_source_stance

# Analyze both articles through the same pipeline
wire_result = {
    "sentiment": analyze_composite(reuters_text, reuters_headline),
    "framing": detect_framing_devices(reuters_text),
    "stance": analyze_source_stance(
        extract_sources(reuters_text), "Meta", full_text=reuters_text
    ),
    "outsourced": measure_outsourced_intensity(reuters_text),
}
magazine_result = {
    "sentiment": analyze_composite(wired_text, wired_headline),
    "framing": detect_framing_devices(wired_text),
    "stance": analyze_source_stance(
        extract_sources(wired_text), "Meta", full_text=wired_text
    ),
    "outsourced": measure_outsourced_intensity(wired_text),
}

# The gap between wire and magazine isolates editorial contribution
tone_gap = magazine_result["sentiment"].overall_tone - wire_result["sentiment"].overall_tone
framing_gap = len(magazine_result["framing"]) - len(wire_result["framing"])
```

### Function Calling Schema

```json
{
    "name": "compare_same_event",
    "description": "Compare how two publications covered the same event. Runs the full analysis pipeline on both articles and produces a structured comparison across tone, framing, source deployment, and outsourced intensity. Uses wire-service coverage as the neutral baseline.",
    "parameters": {
        "type": "object",
        "properties": {
            "article_a_text": {
                "type": "string",
                "description": "Full text of the first article (typically the magazine/newspaper)"
            },
            "article_a_headline": {
                "type": "string",
                "description": "Headline of the first article"
            },
            "article_a_publication": {
                "type": "string",
                "description": "Publication name or slug for article A"
            },
            "article_b_text": {
                "type": "string",
                "description": "Full text of the second article (typically the wire-service baseline)"
            },
            "article_b_headline": {
                "type": "string",
                "description": "Headline of the second article"
            },
            "article_b_publication": {
                "type": "string",
                "description": "Publication name or slug for article B"
            },
            "target_entity": {
                "type": "string",
                "description": "Entity to focus the comparison on (e.g. 'Meta')"
            },
            "event_description": {
                "type": "string",
                "description": "Brief description of the shared event"
            }
        },
        "required": [
            "article_a_text", "article_a_headline", "article_a_publication",
            "article_b_text", "article_b_headline", "article_b_publication",
            "event_description"
        ]
    }
}
```

### compare_multi_articles (N-Way)

```json
{
    "name": "compare_multi_articles",
    "description": "Compare how N publications covered the same event in an N-way cross-outlet matrix. More powerful than pairwise comparison because it reveals the editorial gradient — the spectrum of editorial responses to identical facts. Uses wire-service coverage as the neutral baseline. Returns comparison across tone, framing density, source deployment, outsourced intensity, and cross-publication import detection.",
    "parameters": {
        "type": "object",
        "properties": {
            "articles": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "text": { "type": "string", "description": "Full article text" },
                        "headline": { "type": "string", "description": "Article headline" },
                        "publication": { "type": "string", "description": "Publication name or slug" }
                    },
                    "required": ["text", "headline", "publication"]
                },
                "minItems": 2,
                "description": "Array of articles from different outlets covering the same event"
            },
            "target_entity": {
                "type": "string",
                "description": "Entity to focus the comparison on (e.g. 'Meta')"
            },
            "event_description": {
                "type": "string",
                "description": "Brief description of the shared event"
            },
            "editorial_modes": {
                "type": "object",
                "description": "Optional: map publication name to editorial mode (wire, financial, tech-editorial, sardonic, etc.) for genre-aware interpretation"
            }
        },
        "required": ["articles", "event_description"]
    }
}
```

See `examples/same_event_comparison.py` for the `compare_multi_articles()` implementation and `examples/sample_output/` for 10+ real N-way comparisons.

## Topic Bucket Quick Reference

The 29 topic buckets enable apples-to-apples asymmetry comparison within a topic. Here is the full reference with adjacency warnings for commonly confused pairs:

| # | Bucket | What It Captures | Confusable With |
|---|--------|------------------|-----------------|
| 1 | `layoffs` | Formal workforce actions: layoffs, firings, severance | `workplace_culture`, `labor_market` |
| 2 | `ai_development` | AI technology: LLMs, training, inference, AI strategy | `ai_ethics_safety`, `ai_generated_content` |
| 3 | `privacy_data` | Data collection, surveillance, tracking, GDPR | `cybersecurity` |
| 4 | `antitrust_regulation` | Competition law, monopoly, FTC/EC, DMA/DSA | `government_oversight` |
| 5 | `child_safety` | Youth protection: CSAM, addiction, teen mental health | `consumer_protection` |
| 6 | `content_moderation` | Platform governance: removal, misinformation, policies | — |
| 7 | `ai_generated_content` | AI output quality: deepfakes, AI slop, generative artifacts | `ai_development` |
| 8 | `financial_results` | Earnings, revenue, stock, analyst ratings | `subscription_monetization` |
| 9 | `product_launch` | Specific product releases and announcements | `corporate_strategy` |
| 10 | `executive_behavior` | CEO statements, leadership decisions, departures | — |
| 11 | `litigation` | Lawsuits, court filings, legal proceedings | `consumer_protection` |
| 12 | `prediction_markets` | Betting platforms, event contracts, wagering | `financial_results` |
| 13 | `corporate_strategy` | M&A, partnerships, pivots, market entry | `product_launch` |
| 14 | `defense_military` | Military applications, defense contracts, dual-use tech | — |
| 15 | `labor_market` | Macro employment, wage dynamics, BLS data | `layoffs`, `worker_ai_displacement` |
| 16 | `workplace_culture` | Internal morale, burnout, culture, RTO policies | `layoffs` |
| 17 | `government_oversight` | Regulatory hearings, government audits, policy reviews | `antitrust_regulation` |
| 18 | `infrastructure_impact` | Data centers, energy/water, NIMBY, environmental footprint | `energy_climate` |
| 19 | `worker_ai_displacement` | Workers training AI that replaces them (recursive) | `labor_market` |
| 20 | `health_tech` | Medical devices, BCIs, clinical AI, health apps | — |
| 21 | `cybersecurity` | Hacking, breaches, exploits, vulnerability disclosure | `privacy_data` |
| 22 | `ai_ethics_safety` | AI alignment, existential risk, algorithmic bias | `ai_development` |
| 23 | `education` | Tech impact on schools, classrooms, students | `child_safety` |
| 24 | `subscription_monetization` | Paywalls, pricing tiers, rate-limiting, monetization | `financial_results` |
| 25 | `energy_climate` | Fossil fuels, carbon emissions, renewables, climate policy | `infrastructure_impact` |
| 26 | `hardware_wearables` | Smart glasses, VR/AR headsets, fitness trackers | `product_launch` |
| 27 | `consumer_protection` | AG enforcement, deceptive practices, UDAP, dark patterns | `litigation`, `child_safety` |
| 28 | `content_licensing` | Publishing fees, neighboring rights, content compensation, news licensing | `antitrust_regulation`, `litigation` |
| 29 | `financial_markets` | Stock price, analyst ratings, price targets, valuations, market-cap, investment thesis | `financial_results` |

**Usage tip:** `financial_results` confidence ≥ 0.4 is the trigger for the VADER inflation warning (see Genre-Aware Analysis). See `examples/topic_classification_demo.py` for a runnable demo.

## Framing-Aware Tone Correction Workflow

VADER and TextBlob systematically misprice editorial tone in investigative journalism. Professional prose uses measured, confident language that lexical sentiment models score as positive — even when the editorial stance is clearly adversarial. MediaScope's tone correction pipeline fixes this through **10 correction paths (A–J)**, each addressing a specific VADER failure mode.

See `METHODOLOGY.md` §9 and `examples/framing_correction_demo.py` for a hands-on walkthrough.

### Correction Paths

The pipeline evaluates 7 paths in priority order — the first match fires:

| Path | Failure Mode | When It Fires | Agent Action |
|---|---|---|---|
| **A** | VADER scores adversarial prose positive | raw ≥ 0, agency < −0.3, ≥3 adversarial devices | Full override — trust corrected score, not raw |
| **B** | VADER understates negative magnitude | raw ∈ (−0.5, 0), agency < −0.3, ≥6 adversarial devices | Magnitude adjustment — corrected score is more negative than raw |
| **C** | Product reviews with embedded anchors | raw > 0.3, agency ≥ 0, ≥2 anchor devices + ≥4 adversarial | Mixed article — corrected score reflects reader takeaway, not word count |
| **D** | Sardonic/mocking contempt | raw ≥ 0.3, agency ≥ 0.3, ≥7 loaded language + ≥8 adversarial | High-contempt override — loaded language is the dominant signal |
| **E** | Military techno-optimism | raw ≥ 0.3, agency < 0, ≥3 MTO devices | Domain-specific fix — aspirational military language misleads VADER |
| **F** | Contradictory review framing | raw ≥ 0.3, agency ∈ [−0.4, 0), emotional intensity ≥ 0.5 | Editorial wrapper overrides product praise — trust corrected score |
| **G** | VADER long-text normalization | ≥10 sentences, compound-sentence divergence > 0.5 | Pre-correction — fixes VADER's alpha=15 distortion before composite |
| **H** | Sarcastic short editorial | raw ≥ 0.3, agency ≥ −0.1, ≥2 editorial_aside + ≥4 adversarial + EI ≥ 0.5 | Sarcastic opinion pieces — editorial_aside density is the dominant signal |
| **I** | Direct consumer critique | raw ≥ 0.3, agency > 0, ≥5 adversarial + ≥2 consumer devices + EI ≥ 0.5 | Moral condemnation of corporate decisions — consumer_ownership/competitive_positioning dominant |
| **J** | Expert-driven structural critique | raw ≥ 0.3, agency ≥ 0, ≥5 adversarial + ≥1 expert_contradiction + ≥2 structural devices + EI ≥ 0.10 | Measured editorial with criticism through expert sources + structural devices (consumer_ownership, loss_leader_framing) rather than vocabulary — VADER fooled by corporate PR quotes |

Only one framing path (A–F, H–J) fires per article. Path G runs independently before the composite is computed.

**Adversarial device types** (27 types trigger Paths A/B): absence_as_evidence, assumed_consensus, catastrophizing, competitive_deficit, competitive_displacement, competitive_positioning, consumer_ownership, editorial_aside, editorial_deflation, emotional_appeal, failure_precedent, guilt_by_association, hypocrisy_frame, isolation_framing, juxtaposition, kicker_framing, loaded_language, military_techno_optimism, power_asymmetry, pressure_language, refusal_amplification, self_referential_investigation, silence_as_guilt, slippery_slope, timeline_implication, expert_contradiction, loss_leader_framing.

**Anchor device types** (3 types trigger Path C): kicker_framing, self_referential_investigation, juxtaposition.

### Key Outputs

The `SentimentResult` preserves both scores for transparency:

```python
result = analyze_composite(text, headline)

# Raw VADER/TextBlob composite (often wrong on investigative prose)
result.raw_tone           # e.g., +0.42

# Corrected score from framing analysis (what the editorial stance actually is)
result.overall_tone       # e.g., -0.35

# Metadata: whether framing correction fired
result.framing_corrected  # True/False
```

### Validated Examples

| Article | VADER Raw | Corrected | Gap | Path | Root Cause |
|---|---|---|---|---|---|
| NYT "Meta AI Employees Miserable" | +0.61 | −0.37 | 0.98 | A | 5 adversarial devices + active-negative agency |
| NYT "US Presses Meta on AI Reviews" | +0.61 | −0.57 | 1.18 | A | Isolation framing + pressure language |
| Wired "Applied AI Soul-Crushing" | +0.30 | −0.72 | 1.02 | A | Loaded language + emotional appeal + outsourced intensity |
| Wired glasses launch review | +0.67 | +0.15 | 0.52 | C | Kicker + self-referential investigation anchored final impression |
| MIT TR Anduril/Meta warfare | +0.64 | −0.10 | 0.74 | E | Military aspirational language ("revolutionize the battlefield") |
| Kotaku Meta Arena gambling | +0.68 | −0.55 | 1.23 | D | Sardonic contempt ("ethically rancid," "AI slop") |
| Gizmodo Meta Fury review | +0.68 | −0.35 | 1.03 | F | Positive product praise drowned out privacy editorial wrapper |

## Genre-Aware Analysis Workflow

Article genre is the strongest predictor of toolkit accuracy. Classify genre before running the full pipeline, and adjust interpretation accordingly. See `METHODOLOGY.md` §18 for the full framework.

### Genre Quick-Classification

Use these signals to identify genre on sight:

| Genre | Key Signals |
|---|---|
| **Wire service** | Reuters/AP byline; <600 words; no editorial voice |
| **Investigative** | >1,500 words; multiple sources; original reporting; institutional publication |
| **Tech editorial** | Magazine-length; product/industry focus; editorial voice |
| **Financial** | Stock tickers; analyst quotes; forward-looking language; disclosure statements |
| **Opinion** | First-person; essay structure; thesis-driven |
| **Academic** | Expert sourcing; policy analysis; research citations |
| **Q&A** | Question-answer format; single interviewee |
| **Sardonic** | <500 words; heavy sarcasm; Gizmodo/AV Club/Kotaku |

### Genre-Adjusted Workflow

```
1. Classify genre (use signals above)

2. If wire service:
   → Trust composite score. Use as same-event baseline.
   → Minimal framing analysis needed.

3. If investigative:
   → ALWAYS run full framing correction.
   → Report BOTH raw and corrected scores.
   → Expect Path A/B to fire.
   → Check for counted-anonymous sources.

4. If financial:
   → FLAG as genre-inflated.
   → Report composite with explicit caveat.
   → Use headline-body alignment as diagnostic.
   → Weight framing devices OVER sentiment score.
   → See METHODOLOGY.md §16 for interim recommendations.

5. If Q&A:
   → Manual annotation required.
   → Source extraction WILL return zero (known limitation).
   → Report framing devices and agency only.

6. If sardonic:
   → Expect severe VADER misscoring.
   → Run Path D/H correction.
   → Normalize framing by word count for comparisons.

7. For all other genres:
   → Run standard pipeline.
   → Note genre-typical devices (see §18.5) when interpreting results.
```

### Cross-Genre Comparison Rules

When comparing articles across genres in same-event analysis:

- **Framing device counts are not directly comparable across genres.** A 7:1 device ratio (Wired vs Reuters) is *genre-typical*, not evidence of extreme bias. Use framing density (devices per 100 words) for cross-genre comparison.
- **Financial VADER inflation dwarfs investigative inflation.** Do not directly compare financial and investigative composite scores without genre correction. Use framing devices and source stance as primary dimensions.
- **Never compare source metrics against Q&A articles.** Q&A genre produces zero extractions by design.
- **Wire-service baseline anchors all comparisons.** Magazine tone − wire tone = editorial framing contribution.

## Integration Patterns

### LangChain

```python
from langchain.tools import StructuredTool
import subprocess
import json

def run_mediascope(command: str) -> str:
    result = subprocess.run(
        f"mediascope {command} --format json",
        shell=True, capture_output=True, text=True
    )
    return result.stdout

mediascope_tool = StructuredTool.from_function(
    func=run_mediascope,
    name="mediascope",
    description="Run MediaScope media bias analysis commands"
)
```

### CrewAI

```python
from crewai import Agent, Task, Crew
from crewai_tools import tool

@tool("MediaScope Analysis")
def mediascope_analyze(publication: str, target: str, since: str = "2025-01-01") -> str:
    """Analyze media coverage asymmetry."""
    import subprocess
    result = subprocess.run(
        ["mediascope", "analyze", "--publication", publication,
         "--target", target, "--since", since, "--format", "json"],
        capture_output=True, text=True
    )
    return result.stdout

researcher = Agent(
    role="Media Accountability Researcher",
    goal="Detect and document media coverage bias",
    tools=[mediascope_analyze],
)
```

### Raw Function Calling (Any Agent)

```python
# MediaScope exposes a simple Python API that any agent can call
import mediascope

# Load profile
profile = mediascope.config.load_profile("wired")

# Run pipeline
articles = mediascope.ingest.rss.fetch_all_feeds(profile)
# ... analyze, score, report
```
