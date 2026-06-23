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
from mediascope.analyze.sources import extract_sources, analyze_source_stance, measure_outsourced_intensity, detect_power_asymmetry
from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.byline import build_journalist_profiles
from mediascope.conflicts.ownership import parse_ownership_chain, find_conflicts
from mediascope.conflicts.disclosure import generate_disclosure
from mediascope.quality.standards import check_quality
from mediascope.quality.citations import extract_citations, grade_source
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
            "description": "Advance Publications holds 33.5% voting power in Reddit...",
            "evidence": "Reddit SEC filing"
        }
    ],
    "methodology_url": "https://github.com/mediascope/mediascope/blob/main/docs/METHODOLOGY.md"
}
```

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
