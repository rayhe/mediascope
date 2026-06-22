# Adding Publication Profiles

## Overview

MediaScope uses YAML profiles to describe publications. Each profile contains the publication's ownership structure, revenue relationships, editorial leadership, key journalists, known conflicts of interest, and entity detection patterns.

## Quick Start

### Option 1: Interactive CLI

```bash
mediascope add-publication \
    --name "Fox News" \
    --slug fox-news \
    --url https://www.foxnews.com \
    --interactive
```

This walks you through each section of the profile.

### Option 2: Copy Template

```bash
cp profiles/_template.yaml profiles/your-publication.yaml
```

Edit the YAML file with your publication's data.

## Profile Structure

### Required Fields

| Field | Description | Example |
|---|---|---|
| `name` | Full publication name | "Wired" |
| `slug` | URL-safe identifier | "wired" |
| `url` | Homepage URL | "https://www.wired.com" |
| `rss_feeds` | At least one RSS feed | See below |
| `ownership_chain` | At least the publisher | See below |

### RSS Feeds

```yaml
rss_feeds:
  - url: "https://example.com/feed/rss"
    category: "main"
  - url: "https://example.com/feed/technology"
    category: "technology"
  - url: "https://example.com/feed/business"
    category: "business"
```

**Finding RSS feeds**: Most publications expose RSS at `/feed`, `/rss`, or `/feed/rss`. Check the page source for `<link rel="alternate" type="application/rss+xml">` tags.

### Ownership Chain

List entities from the publication up to the ultimate parent:

```yaml
ownership_chain:
  - name: "Publication Name"
    entity_type: "publisher"
    description: "Brief description"
  - name: "Parent Company"
    entity_type: "parent_company"
    description: "Brief description"
    investments:
      - entity: "Company X"
        stake: "33.5%"
        competitive_with: ["Meta", "Google"]
```

Entity types: `publisher`, `parent_company`, `holding_company`, `family_office`, `individual`

### Revenue Relationships

```yaml
revenue_relationships:
  - partner: "OpenAI"
    relationship_type: "licensing"
    estimated_value: "undisclosed"
    description: "Content licensing deal for AI training"
    date_established: "2024"
    source_url: "https://..."
```

Relationship types: `licensing`, `advertising`, `partnership`, `investment`, `institutional_funding`, `litigation`, `none`

**Important**: If the publication has NO relationship with the target entity, include that as:

```yaml
  - partner: "Meta"
    relationship_type: "none"
    estimated_value: "$0"
    description: "No revenue relationship exists."
```

### Target Entity Clusters

Define how to recognize mentions of companies in articles:

```yaml
target_entities:
  "Meta":
    aliases: ["Meta Platforms", "Facebook", "Instagram", "WhatsApp"]
    regex: "\\b(Meta(?! tag| data)|Facebook|Instagram|WhatsApp)\\b"
```

**Tips**:
- Include subsidiary names, product names, and executive names
- Use negative lookahead to avoid false positives (e.g., `Meta(?! tag)` avoids matching "meta tag")
- Word boundaries (`\b`) prevent partial matches

## Research Guide

### Finding Ownership Data

1. **SEC filings**: Search [EDGAR](https://www.sec.gov/cgi-bin/browse-edgar) for parent company 10-K/10-Q filings
2. **Wikipedia**: Usually has accurate ownership chains (verify against SEC)
3. **Columbia Journalism Review** [Who Owns What](https://www.cjr.org/resources/): Database of media ownership
4. **OpenCorporates**: Corporate registration records
5. **Crunchbase**: Investment and funding data

### Finding Revenue Relationships

1. **Press releases**: Company newsrooms announce partnerships
2. **SEC filings**: Material relationships disclosed in 10-K risk factors
3. **Industry reporting**: Nieman Lab, Digiday, Press Gazette cover media deals
4. **AI crawler policies**: Check robots.txt — if a publication allows a specific AI crawler, they likely have a deal

### Finding Bias Ratings

1. **Ad Fontes Media**: [adfontesmedia.com](https://adfontesmedia.com/) — reliability and bias scores
2. **AllSides**: [allsides.com](https://allsides.com/) — left/center/right ratings
3. **Media Bias/Fact Check**: [mediabiasfactcheck.com](https://mediabiasfactcheck.com/) — detailed ratings

## Validation

After creating a profile, validate it:

```bash
mediascope list-publications  # Should show your new profile
mediascope ingest --publication your-slug --since 2025-01-01  # Test feed ingestion
```

## Contributing Profiles

When submitting a profile for inclusion in the main repository:

1. All facts must have sources (URLs preferred)
2. Ownership chains must be verified against SEC filings or corporate records
3. Revenue relationships must be sourced from press releases or credible reporting
4. Editorial stance descriptions must cite specific published statements
5. Bias ratings must cite the rating organization
6. The profile must include at least one RSS feed that resolves

Submit profiles via pull request to the `profiles/` directory.
