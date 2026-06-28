# Adding Publication Profiles

## Overview

MediaScope uses YAML profiles to describe publications. Each profile contains the publication's ownership structure, revenue relationships, editorial leadership, key journalists, known conflicts of interest, litigation connections, AI crawl policies, bias ratings, and entity detection patterns.

A complete profile enables the full analysis pipeline: entity detection → sentiment scoring → framing detection → asymmetry calculation → conflict disclosure. A minimal profile (name, slug, URL, one RSS feed, and ownership chain) is enough to start ingesting and analyzing articles, but conflict disclosure and cross-publication comparisons improve with each additional section.

This guide covers every profile section, how to research the data, and how to add career data for journalist-level causal analysis.

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

## Profile Structure — Complete Reference

### Required Fields

| Field | Type | Description | Example |
|---|---|---|---|
| `name` | string | Full publication name | `"Wired"` |
| `slug` | string | URL-safe identifier (lowercase, hyphens only) | `"wired"` |
| `url` | string | Homepage URL | `"https://www.wired.com"` |
| `rss_feeds` | list | At least one RSS feed entry | See below |
| `ownership_chain` | list | At least the publisher entity | See below |

### Optional Fields (recommended for full analysis)

| Field | Type | Purpose |
|---|---|---|
| `revenue_relationships` | list | Revenue links to entities covered |
| `editorial_leadership` | list | Current editorial leaders |
| `key_journalists` | list | Journalists covering the target beat |
| `known_conflicts` | list | Pre-identified conflicts of interest |
| `litigation_connections` | list | Litigation funding connections |
| `ai_crawl_policy` | object | Which AI crawlers the publication allows |
| `bias_ratings` | object | Third-party bias ratings |
| `target_entities` | object | Entity detection clusters |
| `internal_ai_tools` | object | Publication's own AI usage |
| `editorial_stance` | object | Documented editorial positions |

---

## Section-by-Section Guide

### 1. RSS Feeds

```yaml
rss_feeds:
  - url: "https://example.com/feed/rss"
    category: "main"
  - url: "https://example.com/feed/technology"
    category: "technology"
  - url: "https://example.com/feed/business"
    category: "business"
```

**Finding RSS feeds:**

1. Check `<publication_url>/feed`, `/rss`, `/feed/rss`, `/feed.xml`
2. View page source and search for `<link rel="alternate" type="application/rss+xml">`
3. Try `<publication_url>/sitemap.xml` — often lists section feeds
4. Google: `site:example.com inurl:feed OR inurl:rss`

**Category labels** are freeform but use these conventions: `main`, `technology`, `business`, `politics`, `science`, `security`, `culture`, `opinion`.

**Tip:** Include section-specific feeds (not just the main feed) to get better topic distribution. Wired's profile includes 6 feeds across business, gear, science, security, and politics.

### 2. Ownership Chain

List entities from the publication up to the ultimate parent/beneficial owner:

```yaml
ownership_chain:
  - name: "Publication Name"
    entity_type: "publisher"
    description: >
      Brief description with key facts: founding date, acquisition history,
      current structure. Include hard numbers when available.
    source_url: "https://..."

  - name: "Parent Company"
    entity_type: "parent_company"
    description: >
      Revenue figures, recent restructuring, key leadership.
      Cite FY figures from SEC filings or Companies House where possible.
    source_url: "https://..."
    investments:
      - entity: "Company X"
        stake: "65.2%"
        competitive_with: ["Meta", "Google"]
        source_url: "https://..."

  - name: "Holding Company"
    entity_type: "holding_company"
    description: >
      Ultimate parent. Board composition, portfolio companies,
      family/trust structure if privately held.
    source_url: "https://..."

  - name: "Individual/Family/Trust"
    entity_type: "family_office"
    description: >
      Beneficial owners. Net worth, other holdings, political affiliations
      or known positions that could influence editorial direction.
    source_url: "https://..."
```

**Entity types:** `publisher`, `parent_company`, `operating_subsidiary`, `holding_company`, `family_office`, `individual`, `trust`, `foundation`

**Key principle:** Follow the money upward. Each entity should document what it owns, who controls it, and any investments that compete with entities the publication covers.

**Research sources:**

| Source | What You'll Find | URL |
|---|---|---|
| SEC EDGAR | 10-K, 10-Q, proxy statements, Schedule 13G/A filings | `sec.gov/cgi-bin/browse-edgar` |
| Companies House (UK) | UK subsidiary financials, director filings | `find-and-update.company-information.service.gov.uk` |
| OpenCorporates | Corporate registration records worldwide | `opencorporates.com` |
| CJR Who Owns What | Media ownership database | `cjr.org/resources/` |
| Wikipedia | Usually accurate ownership chains (verify against SEC) | |
| Crunchbase | Investment and funding data | `crunchbase.com` |

**Example from Wired profile** — Advance Publications' Reddit stake:
```yaml
  - name: "Advance Publications, Inc."
    entity_type: "holding_company"
    description: >
      Private media holding company. Wholly owned by the Newhouse family.
    investments:
      - entity: "Reddit"
        stake: "65.2% total voting power"
        shares: "42,191,092 Class B + 16,182 Class A (83.5% of Class B, 10 votes/share)"
        competitive_with: ["Meta", "Google", "X/Twitter"]
        board_seats: 2
        stake_value: "~$7B"
        source_url: "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=advance+magazine"
```

### 3. Revenue Relationships

Document every revenue link between the publication (or its parent) and entities it covers. **Crucially, also document the absence of a relationship** when that absence is analytically significant:

```yaml
revenue_relationships:
  # Active relationship
  - partner: "OpenAI"
    relationship_type: "ai_licensing"
    estimated_value: "undisclosed"
    description: "Content licensing deal for AI training data"
    date_established: "2024-07"
    source_url: "https://..."
    notes: "Announced via press release"

  # Compound relationship (multiple revenue streams)
  - partner: "Amazon"
    relationship_type: "ai_licensing + affiliate_revenue (COMPOUND)"
    estimated_value: "$70-125M+/year (combined)"
    description: >
      Wirecutter affiliate revenue ($50-100M+/yr estimated from
      FY2025 affiliate segment) + Amazon Rufus AI licensing deal
      ($20-25M/yr, started May 2025).
    date_established: "2016 (Wirecutter), 2025 (AI deal)"
    source_url:
      - "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=nytimes"
      - "https://www.adweek.com/media/amazon-affiliate-commission-cuts-2026/"

  # Absence of relationship (analytically important)
  - partner: "Meta"
    relationship_type: "none"
    estimated_value: "$0"
    description: >
      No revenue relationship exists between Condé Nast/Advance Publications
      and Meta. This is significant because Condé Nast has licensing deals
      with OpenAI, Amazon, and Apple — all Meta competitors.
    notes: "Asymmetric deal pattern — competitors pay, Meta doesn't"
```

**Relationship types:** `licensing`, `ai_licensing`, `advertising`, `partnership`, `investment`, `institutional_funding`, `affiliate_revenue`, `subscription_bundle`, `litigation`, `none`

**How to find revenue relationships:**

1. **Press releases:** Check the publication's and partner's newsrooms for partnership announcements
2. **SEC filings:** Material relationships are disclosed in 10-K risk factors and related-party notes
3. **Industry reporting:** Nieman Lab, Digiday, Press Gazette, Adweek cover media deals
4. **AI crawler policies:** Check `robots.txt` — if a publication allows a specific AI crawler (e.g., `GPTBot`, `CCBot`), they likely have a licensing deal
5. **Affiliate programs:** Check if the publication links to Amazon, uses affiliate tags (e.g., `?tag=` parameters)

### 4. Editorial Leadership

```yaml
editorial_leadership:
  - name: "Katie Drummond"
    title: "Global Editorial Director"
    since: "2023-09"
    editorial_stance: >
      Explicitly adversarial: "If you do wrong, I want the world to know."
      Created Wired's first politics team (Nov 2023). Freedom of the Press
      Foundation board member (2024). Launched 'Story Zero' newsroom ethos.
    source_url: "https://www.nytimes.com/2023/09/11/business/media/wired-katie-drummond.html"

  - name: "Leah Feiger"
    title: "Politics Editor"
    since: "2023-11"
    editorial_stance: "First-ever dedicated politics editor at Wired"
    notes: "Signals structural shift from pure tech to tech-politics hybrid"
```

**Key fields:**
- `name` (required): Full name
- `title` (required): Editorial title
- `since`: When they started (YYYY-MM format)
- `editorial_stance`: Any documented editorial positions, public statements, or editorial mission declarations. Quote directly where possible.
- `source_url`: Link to announcement or profile
- `notes`: Analytical context

**Why this matters:** Editorial leadership changes are analyzed by the `LeadershipAnalyzer` using interrupted time-series regression. A new EIC can shift a publication's entire tone — documenting their stance provides context for interpreting the statistical signal.

### 5. Key Journalists

```yaml
key_journalists:
  - name: "Lauren Goode"
    beat: "consumer technology, Meta/Apple coverage"
    known_patterns: >
      Covers Meta products (Ray-Ban glasses, Quest) and Apple comparisons.
      Pre-Wired career at The Verge (2012-2018). Podcast host (Have a Nice Future).

  - name: "David Gilbert"
    beat: "misinformation, content moderation, platform accountability"
    known_patterns: >
      Previously at VICE News. Bylined on major Meta misinformation stories.
      Focus on Global South content moderation failures.
```

**Key fields:**
- `name` (required): Full name as it appears in bylines
- `beat` (required): Topic areas they cover
- `known_patterns`: Observed coverage tendencies, source preferences, narrative frames. Be specific and cite evidence.

**Tip:** Start with the 3-5 journalists who most frequently cover your target entity. Check byline archives on the publication's site. For deeper journalist tracking (career history, migrations, bias decomposition), add them to `profiles/careers/journalists.yaml` (see [Adding Career Data](#adding-career-data) below).

### 6. Known Conflicts of Interest

```yaml
known_conflicts:
  - name: "reddit_stake"
    type: "investment"
    severity: 5
    description: >
      Advance Publications holds 65.2% total voting power in Reddit via 42.2M
      Class B shares (83.5% of Class B, 10 votes/share) plus 16K Class A shares,
      worth ~$7B. Reddit competes directly with Meta for user attention,
      advertiser spend, and community engagement. 2 board seats.
    evidence: "Reddit 2026 Proxy Statement, Schedule 13G filed Nov 14, 2024"
    source_url: "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=reddit"
    entities_affected: ["Meta", "Google", "X/Twitter"]

  - name: "ai_licensing_asymmetry"
    type: "revenue"
    severity: 5
    description: >
      Condé Nast has content licensing deals with OpenAI, Amazon (Rufus),
      and Apple — all Meta competitors. Meta has NO such deal. Creates a
      financial incentive to frame AI competitors favorably.
    evidence: "Press releases, Adweek reporting"
    source_url: "https://..."
    entities_affected: ["Meta"]

  - name: "no_meta_counterweight"
    type: "structural"
    severity: 4
    description: >
      No revenue relationship with Meta exists to counterbalance the
      competitor relationships. Meta has no financial lever to influence
      coverage, while competitors collectively pay millions.
    evidence: "Absence confirmed — no press release, no filing, no crawler policy"
```

**Conflict types:** `investment`, `revenue`, `board_seat`, `competitive`, `litigation`, `structural`, `personnel`, `institutional_funding`

**Severity scale:**

| Level | Meaning | Example |
|---|---|---|
| 1 | Minimal | Shared industry event sponsorship |
| 2 | Minor | Indirect competitive relationship, passive equity stake |
| 3 | Moderate | Revenue dependency on a covered entity's competitor |
| 4 | Significant | Major investment in a direct competitor, compound revenue |
| 5 | Critical | Controlling stake in competitor + revenue deals with other competitors |

**Key principle:** Every conflict MUST have verifiable evidence. Cite SEC filings, court records, or credible industry reporting. Speculation without evidence is not a conflict — it's a hypothesis.

### 7. Litigation Connections

```yaml
litigation_connections:
  - type: "funder"
    name: "Flashlight Capital"
    description: >
      Funds the Social Media Victims Law Center (SMVLC), lead counsel
      in Meta bellwether trial. Litigation funding is undisclosed.
    case_reference: "MDL 3047"
    source_url: "https://..."

  - type: "plaintiff"
    name: "Innsworth Capital (Elliott Management)"
    description: >
      Elliott Management ($35B AUM) funding £2.7B UK Facebook antitrust
      via Innsworth Capital vehicle.
    case_reference: "UK Competition Appeal Tribunal"
    source_url: "https://..."
```

**Connection types:** `funder`, `plaintiff`, `connected_party`, `law_firm`, `expert_witness`

**Research sources:**

| Source | What You'll Find |
|---|---|
| PACER | US federal court filings — party lists, funding disclosures |
| UK Competition Appeal Tribunal | UK antitrust filings |
| State AG websites | State-level investigations and settlements |
| Litigation funder registries | Many jurisdictions now require funder disclosure |

### 8. AI Crawl Policy

```yaml
ai_crawl_policy:
  blocks_gptbot: false
  blocks_ccbot: false
  blocks_google_extended: true
  blocks_anthropic: true
  blocks_meta: true
  allows_specific: ["GPTBot"]
  notes: >
    Allows GPTBot (OpenAI) suggesting a licensing deal.
    Blocks Google-Extended and Anthropic. Check robots.txt
    at the publication URL for current status.
```

**How to check:** Fetch `https://<publication_url>/robots.txt` and look for `User-agent: GPTBot`, `CCBot`, `Google-Extended`, `anthropic-ai`, `Meta-ExternalFetcher`.

**Analytical value:** A publication that blocks all AI crawlers *except* one likely has a licensing deal with that company. This is circumstantial evidence of a revenue relationship.

### 9. Bias Ratings

```yaml
bias_ratings:
  ad_fontes:
    reliability: 37.13        # 0-64 scale; 40+ = "good reliability"
    bias: -7.19               # -42 (far left) to +42 (far right)
    source_url: "https://adfontesmedia.com/wired-bias-and-reliability/"
  allsides: "Lean Left"       # Left, Lean Left, Center, Lean Right, Right
  mbfc:
    rating: "Left-Center Bias"
    factual_reporting: "High"
    source_url: "https://mediabiasfactcheck.com/wired/"
```

**Sources:**

| Rater | URL | Scale |
|---|---|---|
| Ad Fontes Media | `adfontesmedia.com` | Reliability 0-64, Bias -42 to +42 |
| AllSides | `allsides.com` | 5-point Left to Right |
| Media Bias/Fact Check | `mediabiasfactcheck.com` | Detailed multi-dimensional ratings |

**Context:** These ratings provide an independent baseline for comparison. Ad Fontes reliability below 40 is below their "good" threshold — analytically significant for publications claiming editorial rigor.

### 10. Target Entity Clusters

Define how to recognize company mentions in articles. Two formats are supported:

**Dict format (recommended)** — explicit aliases and optional custom regex:

```yaml
target_entities:
  "Meta":
    aliases: ["Meta Platforms", "Facebook", "Instagram", "WhatsApp", "Mark Zuckerberg"]
    regex: "\\b(Meta(?!\\s+(?:tag|data|analysis|description|key|charset))\\b|Facebook|Instagram|WhatsApp|Zuckerberg)"
  "Apple":
    aliases: ["Apple Inc", "iPhone", "Tim Cook", "John Ternus"]
    regex: "\\b(Apple(?!\\s+(?:pie|cider|sauce|tree|juice|Watch))\\b|iPhone|iPad|Tim\\s+Cook|John\\s+Ternus)"
```

**List format (shorthand)** — auto-generates word-boundary regex from aliases:

```yaml
target_entities:
  "Meta":
    - "Meta Platforms"
    - "Facebook"
    - "Instagram"
```

The dict format is preferred for entities with common false positives (Apple, Meta, Amazon) because the `regex` field lets you add negative lookahead patterns.

**Tips:**
- Include subsidiary names, product names, and executive names
- Use negative lookahead `(?!\s+(?:word1|word2))` to avoid false positives
- Word boundaries `\b` prevent partial matches
- Test with a few real articles to catch edge cases

### 11. Internal AI Tools (optional)

If the publication uses AI internally, document it — this creates the "hypocrisy index" when a publication criticizes AI while using it:

```yaml
internal_ai_tools:
  uses_ai_for_journalism: true
  tools:
    - name: "Echo"
      purpose: "Editorial assistant for drafting, research, and summarization"
      source_url: "https://..."
    - name: "Stet"
      purpose: "Copy-editing and style enforcement"
    - name: "Cheat Sheet"
      purpose: "Article summarization for internal briefings"
  editorial_director_of_ai:
    name: "Zach Seward"
    since: "2024-02"
    stance: "Pro-AI-for-journalism within guardrails"
    source_url: "https://..."
  notes: >
    Paradox: NYT sued OpenAI (Dec 2023) while simultaneously building
    internal AI tools and hiring an editorial AI director.
```

### 12. Editorial Stance (optional)

Document the publication's stated editorial positions:

```yaml
editorial_stance:
  self_described: "Technology and culture magazine"
  notable_positions:
    - topic: "AI regulation"
      stance: "Strongly pro-regulation"
      evidence: "Multiple editorial board pieces calling for AI moratorium"
    - topic: "Meta/Facebook"
      stance: "Adversarial"
      evidence: "Katie Drummond: 'If you do wrong, I want the world to know'"
  editorial_mission:
    text: "Story Zero newsroom ethos — every story starts from zero assumptions"
    source_url: "https://..."
```

---

## Adding Career Data

Career data enables MediaScope's novel contribution: causal bias attribution through journalist migration analysis (see [EDITORIAL_HISTORIES.md](EDITORIAL_HISTORIES.md)). Two YAML files hold this data:

### `profiles/careers/journalists.yaml`

Each journalist has a name, optional notes, and a chronological list of career events:

```yaml
journalists:
  - name: "Karen Hao"
    notes: >
      Key migration: MIT Tech Review → Atlantic. Known for adversarial AI
      coverage. Her viral 'How Facebook got addicted to spreading
      misinformation' (2021) set the template for anti-Meta AI reporting.
    career:
      - publication: "mit-tech-review"     # Must match a profile slug
        event_type: "hired"                 # hired, promoted, departed, beat_change
        role: "staff_writer"                # staff_writer, senior_writer, correspondent, editor, etc.
        beat: "AI"
        start: "2018-01"                    # YYYY-MM or YYYY-MM-DD
        end: "2022-05"                      # Omit if still active
        source_url: "https://www.technologyreview.com/author/karen-hao/"
        notes: "AI reporter. Wrote viral anti-Meta AI piece (Mar 2021)."

      - publication: "atlantic"
        event_type: "hired"
        role: "staff_writer"
        beat: "AI, technology"
        start: "2022-06"
        source_url: "https://www.theatlantic.com/author/karen-hao/"
        notes: "Continued AI ethics/harms focus."
```

**Career event fields:**

| Field | Required | Description |
|---|---|---|
| `publication` | Yes | Profile slug (must match an existing profile) |
| `event_type` | Yes | `hired`, `promoted`, `departed`, `beat_change`, `freelance` |
| `role` | Yes | Position title: `staff_writer`, `senior_writer`, `correspondent`, `editor`, `senior_editor`, `deputy_editor`, `eic`, `columnist` |
| `beat` | Recommended | Topic areas covered |
| `start` | Yes | Start date (YYYY-MM or YYYY-MM-DD) |
| `end` | No | End date (omit if still active at this publication) |
| `source_url` | Recommended | Verification link (LinkedIn, staff page, byline archive) |
| `notes` | No | Analytical context, notable work, patterns |

**Publication slugs for tracked publications:** `wired`, `nytimes`, `guardian`, `atlantic`, `mit-tech-review`

**For publications not in the 5-publication set:** Use the slug you would assign them (e.g., `the-verge`, `buzzfeed-news`, `platformer`, `reuters`). The CareerTracker only detects migrations between *tracked* publications, but career events at non-tracked outlets still provide context for portable bias scoring.

**Who to add (priority order):**

1. **Cross-publication migrants** — journalists who have worked at ≥2 of the 5 tracked publications (highest analytical value)
2. **Multi-outlet journalists** — reporters with 3+ total outlets, even if only 1 is tracked (useful for portable bias estimation)
3. **Beat leads** — the primary reporter(s) covering your target entity at each publication
4. **Recent hires** — journalists who joined in the last 2 years (most likely to create detectable tone shifts)

### `profiles/careers/editorial_changes.yaml`

Leadership transitions, organized by publication slug:

```yaml
editorial_changes:
  wired:
    - position: "eic"                    # eic, editorial_director, managing_editor, etc.
      outgoing: "Nicholas Thompson"      # Who left
      incoming: "Gideon Lichfield"       # Who arrived
      date: "2020-09"                    # YYYY-MM
      source_url: "https://..."
      notes: >
        Thompson left for The Atlantic. Lichfield came from MIT Technology
        Review. Double natural experiment: tests source-side AND dest-side.

    - position: "politics_editor"
      incoming: "Leah Feiger"
      date: "2023-11"
      notes: "First-ever politics editor — structural shift, not a replacement"
```

**Leadership change fields:**

| Field | Required | Description |
|---|---|---|
| `position` | Yes | `eic`, `editorial_director`, `managing_editor`, `deputy_editor`, `politics_editor`, `tech_editor`, `ai_editor`, `investigations_editor` |
| `outgoing` | No | Name of predecessor (omit for new positions) |
| `incoming` | Yes | Name of new leader |
| `date` | Yes | YYYY-MM |
| `source_url` | Recommended | Announcement article |
| `notes` | No | Context: why this matters, prior career, editorial stance |

**Why this matters:** The `LeadershipAnalyzer` uses interrupted time-series regression to detect tone shifts correlated with leadership changes. The `notes` field provides hypothesis context — if a new EIC came from an adversarial outlet, a subsequent tone shift is more interpretable.

---

## Research Workflow

When building a new publication profile, follow this order:

### Step 1: Basic Structure (30 min)

1. Create the profile file from the template
2. Fill in `name`, `slug`, `url`
3. Find RSS feeds (check page source, `/feed`, `/rss`)
4. Set up basic `target_entities` clusters

### Step 2: Ownership Chain (1-2 hours)

1. Start with Wikipedia for the high-level chain
2. Verify against SEC filings (10-K, proxy statements) for public companies
3. Check Companies House for UK subsidiaries
4. For private companies, check CJR's "Who Owns What" database
5. Document every entity from publisher to ultimate beneficial owner
6. Look for investments that compete with your target entity

### Step 3: Revenue Relationships (1-2 hours)

1. Search for press releases about content deals, licensing, partnerships
2. Check `robots.txt` for AI crawler permissions
3. Look at SEC filings for "material relationships" disclosures
4. Check Nieman Lab, Digiday, Press Gazette for industry reporting
5. Document the *absence* of a relationship with your target entity if relevant

### Step 4: Editorial Context (1 hour)

1. Identify current editorial leadership (masthead page, LinkedIn)
2. Find their public statements about editorial direction
3. List 3-5 key journalists covering your target beat
4. Check Ad Fontes, AllSides, MBFC for third-party bias ratings

### Step 5: Conflicts & Litigation (1-2 hours)

1. Cross-reference ownership investments against entities covered
2. Check PACER for litigation involving entities covered
3. Search for litigation funding connections
4. Assign severity scores (1-5) with evidence

### Step 6: Career Data (30 min per journalist)

1. Find LinkedIn profiles, staff pages, byline archives
2. Build chronological career timelines in `journalists.yaml`
3. Document any editorial leadership changes in `editorial_changes.yaml`
4. Verify dates against multiple sources

---

## Validation

### Basic Validation

```bash
# Check profile loads without errors
mediascope list-publications

# Test feed ingestion
mediascope ingest --publication your-slug --since 2025-01-01

# Test entity detection on a few articles
mediascope analyze --publication your-slug --target "Your Target" --since 2025-01-01
```

### YAML Validity

```bash
# Check YAML syntax
python3 -c "import yaml; yaml.safe_load(open('profiles/your-publication.yaml'))"

# Check careers YAML
python3 -c "import yaml; yaml.safe_load(open('profiles/careers/journalists.yaml'))"
```

### Profile Completeness Checklist

- [ ] Name, slug, and URL are set
- [ ] At least one RSS feed resolves (test with `curl`)
- [ ] Ownership chain reaches the ultimate beneficial owner
- [ ] All ownership facts cite a source URL
- [ ] Revenue relationships include both active deals AND documented absences
- [ ] Known conflicts have severity ratings and evidence
- [ ] Target entity clusters include negative lookahead for false positives
- [ ] Bias ratings cite the rating organization
- [ ] Editorial leadership includes current EIC or equivalent
- [ ] At least 3 key journalists are documented with beats

### Quality Standards

When submitting a profile for inclusion in the main repository:

1. **All facts must have sources** — URLs to SEC filings, press releases, or credible reporting
2. **Ownership chains must be verified** against SEC filings or corporate registries, not just Wikipedia
3. **Revenue relationships must be sourced** from press releases, SEC filings, or industry reporting
4. **Editorial stance descriptions must cite** specific published statements, not inferences
5. **Bias ratings must cite** the rating organization with a link
6. **The profile must include at least one RSS feed** that resolves and returns articles
7. **Severity scores must be justified** — a severity 5 conflict should be as significant as "controlling stake in a direct competitor"
8. **YAML must parse cleanly** — test with `yaml.safe_load()` before committing

---

## Examples

### Minimal Profile

A bare-minimum profile for starting article ingestion:

```yaml
name: "Fox News"
slug: "fox-news"
url: "https://www.foxnews.com"

rss_feeds:
  - url: "https://moxie.foxnews.com/google-publisher/latest.xml"
    category: "main"

ownership_chain:
  - name: "Fox News Media"
    entity_type: "publisher"
    description: "Cable/digital news network, part of Fox Corporation"
  - name: "Fox Corporation"
    entity_type: "parent_company"
    description: "Publicly traded (FOXA/FOX). Spun off from 21st Century Fox in 2019."
  - name: "Murdoch Family Trust"
    entity_type: "family_office"
    description: "Rupert Murdoch controls Fox Corp via family trust voting shares."
```

### Complete Profile

See `profiles/wired.yaml` for a fully-documented profile with all sections populated, including 5-deep ownership chain, 8 revenue relationships, 17 known conflicts, litigation connections, AI crawl policy, bias ratings, and editorial leadership.

---

## Frequently Asked Questions

**Q: Can I add a publication that's behind a paywall?**

Yes. RSS feeds usually include at least headlines and summaries, which is enough for entity detection and basic sentiment. For full-text analysis, you'll need a subscription or to use the Wayback Machine (`archive.py`) for older articles.

**Q: What if the ownership chain is opaque (private company, no SEC filings)?**

Document what you can find. Companies House (UK), OpenCorporates, Crunchbase, and CJR's database are all useful for private companies. State "ownership structure not fully disclosed" in the profile notes and cite what sources you checked.

**Q: How do I handle publications with complex corporate structures (e.g., multiple subsidiaries)?**

Add intermediate entities to the `ownership_chain` with `entity_type: "operating_subsidiary"`. See the Wired profile, which includes a "Condé Nast (UK subsidiary)" entry with Companies House financials separate from the global parent.

**Q: My target entity name has common false positives (like "Apple"). What do I do?**

Use the dict format for `target_entities` with a custom regex that includes negative lookahead:

```yaml
target_entities:
  "Apple":
    aliases: ["Apple Inc", "iPhone", "iPad"]
    regex: "\\b(Apple(?!\\s+(?:pie|cider|sauce|tree|juice|Watch|TV\\+))\\b|iPhone|iPad)"
```

Test with a few real articles and add terms to the exclusion list as needed.

**Q: Should I include journalists who no longer work at the publication?**

Yes, in `profiles/careers/journalists.yaml`. Former journalists with known departure dates are essential for DiD migration analysis. Set their `end` date and the CareerTracker will detect the migration automatically.
