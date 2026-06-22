# Architecture

## System Overview

MediaScope is a modular Python toolkit organized into six functional layers:

```
┌──────────────────────────────────────────────────────────────────────┐
│                        CLI / Agent Interface                        │
│                     mediascope/cli.py                                │
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
```

## Data Flow

```
RSS Feeds ──→ Article Text ──→ Entity Detection ──→ Sentiment Analysis
                                      │                     │
                                      ▼                     ▼
                              Topic Classification   Framing Detection
                                      │                     │
                                      └──────┬──────────────┘
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

## Configuration

All configuration flows through `config.py`:

- **Publication profiles**: YAML files in `profiles/` directory
- **Global config**: Environment variables or `mediascope.yaml` in working directory
- **Database**: SQLite (default) or PostgreSQL via `MEDIASCOPE_DB_URL`

## Storage

MediaScope uses SQLAlchemy with the following tables:

| Table | Purpose |
|---|---|
| `articles` | Ingested article text and metadata |
| `entity_mentions` | Detected entity mentions per article |
| `sentiment_scores` | 8-dimension sentiment scores per article |
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
