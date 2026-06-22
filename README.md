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

Ships with verified career data for **17 journalists** across 10+ publications, including high-value migrations like Karen Hao (MIT Tech Review → Atlantic), Cade Metz (Wired → NYT), and Zoë Schiffer (The Verge → Platformer → Wired).

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
| **The Guardian** | Scott Trust (non-profit) | *Control case* | Pure editorial bias, no financial conflicts |
| **The Atlantic** | Emerson Collective (LPJ) | Investment | Owner holds ~$16B in Apple stock (Meta competitor) |
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
