# Editorial Histories

## Overview

The Editorial Histories module is MediaScope's novel contribution to computational media analysis. While sentiment scoring and ownership mapping are well-established (Gentzkow & Shapiro 2010; Groseclose & Milyo 2005), **no prior work systematically applies causal inference methods to journalist-level editorial migration data at scale.**

The core insight: when a journalist moves from Publication A to Publication B, it creates a *natural experiment*. By comparing coverage tone before and after the move — at both publications — we can decompose observed bias into institutional and individual components with statistical rigor.

## The Three Natural Experiments

Every journalist migration generates three testable hypotheses:

### 1. Source-Side Effect
**Question:** Does Publication A's coverage change after the journalist leaves?

| Outcome | Interpretation |
|---|---|
| Coverage tone at A unchanged | Institutional bias — the publication drives tone regardless of personnel |
| Coverage tone at A shifts significantly | Individual bias — this journalist was shaping coverage |

### 2. Portable Bias
**Question:** Does the journalist's tone change at Publication B?

| Outcome | Interpretation |
|---|---|
| Journalist's tone unchanged at new outlet | Portable bias — the journalist carries their stance with them |
| Journalist's tone adapts to Publication B's norms | Editorial capture — institutional culture dominates |

### 3. Destination Effect
**Question:** Does Publication B's coverage change after the journalist arrives?

| Outcome | Interpretation |
|---|---|
| Coverage at B unchanged | The journalist adapted to existing culture, or has low influence |
| Coverage at B shifts toward journalist's historical tone | The journalist brought their bias and influenced the publication |

## Methodology

### Difference-in-Differences (DiD)

We adapt the canonical DiD framework (Card & Krueger, 1994) from labor economics to editorial analysis.

**The Standard Model:**

```
Y = β₀ + β₁·Treatment + β₂·Post + β₃·(Treatment × Post) + ε
```

Where:
- `Y` = article tone score
- `Treatment` = 1 for the publication that lost/gained the journalist, 0 for control
- `Post` = 1 for articles after the migration, 0 for articles before
- `β₃` = the **DiD estimator** — the causal effect of the personnel change, net of secular trends

**β₃ is the key number.** It tells us how much the journalist's departure/arrival *caused* a change in coverage tone, after removing trends that would have happened anyway.

### Why DiD Instead of Simple Before/After?

A simple pre/post comparison confounds the journalist's effect with everything else happening in the world. If Meta's coverage became more negative after Karen Hao left MIT Technology Review, was it because she left, or because Meta faced new lawsuits that month?

DiD solves this by comparing the *change* at the affected publication to the *change* at a control publication that didn't experience the personnel shift. If the control also became more negative (because of the lawsuits), that secular trend cancels out, isolating Hao's personal effect.

### Control Group Selection

The control group should be a publication that:
1. Covers the same entities (Meta, Google, etc.)
2. Did NOT experience a significant personnel change in the same window
3. Is exposed to the same news cycle (same industry, same market)

The Guardian is often a useful control because of its stable editorial team (Katharine Viner has been EIC since 2015) and no financial conflicts that would create structural shifts.

### Interrupted Time-Series (ITS) for Leadership Changes

For editorial leadership changes (new EIC, managing editor), we use a segmented regression:

```
Y_t = β₀ + β₁·T + β₂·D_t + β₃·(D_t × T_post) + ε_t
```

Where:
- `T` = time index (months)
- `D_t` = 0 before the leadership change, 1 after
- `T_post` = months since the change (0 before)
- `β₂` = **level shift** — immediate tone change when new leader takes over
- `β₃` = **slope change** — gradual drift in tone under new leadership

**Example:** Katie Drummond became Wired's Global Editorial Director in September 2023. The ITS analysis fits Wired's Meta coverage tone before and after, testing:
- Was there an immediate shift in tone? (β₂)
- Did the monthly trend in tone change? (β₃)
- Are these effects statistically significant?

### Bias Decomposition (Two-Way ANOVA)

For journalists who have worked at ≥2 tracked publications, we decompose total variance in their tone scores:

```
Total_Variance = SS_institutional + SS_individual + SS_interaction
```

Where:
- **SS_institutional** = How much of the variance is explained by which publication they're writing for (the institutional culture effect)
- **SS_individual** = How much is explained by the journalist's deviation from each publication's baseline (their personal stance)
- **SS_interaction** = Synergy between journalist and publication (amplification effects)

**Portable Bias Score** (0 to 1):
- 0.0 = Journalist fully adapts to each publication's norms
- 1.0 = Journalist maintains identical tone regardless of outlet
- Computed as average cross-publication tone similarity using 1 − |Cohen's d|/2

## Usage

### CLI Commands

```bash
# List all tracked journalists and their current outlets
mediascope careers list

# Show a journalist's full career timeline
mediascope careers show "Karen Hao"

# List all detected migration events between tracked publications
mediascope careers migrations

# Show editorial leadership changes at a publication
mediascope careers leadership wired

# Run difference-in-differences analysis for a specific migration
mediascope careers diff "Karen Hao"

# Run full bias decomposition for a journalist
mediascope careers analyze "Karen Hao"
```

### Python API

```python
from mediascope.careers import (
    CareerTracker,
    MigrationAnalyzer,
    LeadershipAnalyzer,
    InfluenceScorer,
)

# Load career data
tracker = CareerTracker()
tracker.load()

# Find migrations between tracked publications
migrations = tracker.find_migrations(from_pub="mit-tech-review")

# Run DiD on a migration
analyzer = MigrationAnalyzer(window_days=180)
result = analyzer.analyze_migration(
    migration=migrations[0],
    source_articles=mit_tech_review_articles,
    dest_articles=atlantic_articles,
    journalist_articles=karen_hao_articles,
    control_articles=guardian_articles,
)
print(f"DiD estimate: {result.did_estimate:.3f} (p={result.did_p_value:.4f})")
print(f"Portable bias: {result.portable_bias_estimate:.3f}")

# Analyze leadership change impact
leadership = LeadershipAnalyzer()
changes = leadership.load_changes()
drummond = [c for c in changes if c.incoming_name == "Katie Drummond"][0]
impact = leadership.analyze_change(drummond, wired_articles, target_entity="Meta")
print(f"Level shift: {impact.level_shift:.3f} (p={impact.level_shift_p:.4f})")

# Decompose a journalist's bias
scorer = InfluenceScorer()
decomp = scorer.decompose(
    journalist_name="Karen Hao",
    articles_by_pub={
        "mit-tech-review": hao_mtr_articles,
        "atlantic": hao_atlantic_articles,
    },
    pub_baselines={"mit-tech-review": -0.15, "atlantic": -0.08},
)
print(f"Institutional: {decomp.institutional_component:.3f}")
print(f"Individual: {decomp.individual_component:.3f}")
print(f"Portable: {decomp.portable_bias_score:.3f}")
```

## Starter Data

MediaScope ships with career data for **97 journalists** across the 5 starter publications plus notable feeder outlets (The Verge, BuzzFeed News, Platformer, Reuters, Recode, WSJ, Bloomberg, The Telegraph, New Scientist, Gizmodo, The Daily Beast, Politico, Consumer Reports, The Information, and 140+ others). 94 of these have multi-publication careers suitable for migration analysis.

### High-Value Migration Events

| Journalist | From | To | When | Why It Matters |
|---|---|---|---|---|
| **Karen Hao** | MIT Tech Review | The Atlantic | 2022 | Adversarial AI reporter crossing outlets — did her viral anti-Meta tone carry over? |
| **Cade Metz** | Wired | NYT | 2017 | AI reporter leaving Condé Nast for Sulzberger — portable bias test |
| **Will Knight** | MIT Tech Review | Wired | 2018 | 13 years at MIT TR → Wired AI beat — deep institutional encoding vs. adaptation |
| **Zoë Schiffer** | The Verge → Platformer | Wired | 2024 | Tech labor reporter with 3 outlets — rich decomposition data |
| **Charlie Warzel** | BuzzFeed → NYT | The Atlantic | 2020 | Anti-Big-Tech stance across three outlets — high portable bias candidate |
| **Mat Honan** | Wired/BuzzFeed | MIT Tech Review (EIC) | 2021 | Became EIC — tests whether a journalist changes an institution from the top |
| **Kara Swisher** | WSJ → Recode | NYT | 2020 | Anti-Big-Tech across every outlet — the ultimate portable bias test case |
| **Mike Isaac** | Wired → Recode | NYT | 2014 | 5-outlet career (Wired→AllThingsD→Forbes→Recode→NYT) — rich decomposition |
| **Kashmir Hill** | Above the Law → Forbes → Fusion → Gizmodo | NYT | 2019 | 5-outlet career covering privacy/surveillance — portable stance test |
| **Katie Drummond** | Bloomberg → Gizmodo → Medium → The Outline → Vice | Wired | 2022 | 7-outlet career ending as Wired editorial director — highest migration count in dataset |
| **Jessica Hamzelou** | New Scientist (13 years) | MIT Tech Review | ~2023 | Longest single-outlet tenure before migration — deep institutional encoding test |
| **Paresh Dave** | Reuters | Wired | ~2023 | Wire service → magazine — tests whether news-wire objectivity survives editorial culture |
| **Johana Bhuiyan** | BuzzFeed → Recode → Politico | Guardian | ~2021 | 5-outlet career across investigative beats — tests stance portability across national contexts |
| **Hibaq Farah** | NYT | Guardian | ~2023 | Reverse Atlantic crossing — US institutional norms meeting UK editorial culture |
| **Kaitlyn Tiffany** | Vox → The Verge | The Atlantic | ~2020 | Digital-native → legacy prestige publication adaptation |
| **Dell Cameron** | The Daily Dot → Vice → Gizmodo | Wired | ~2023 | Investigative security reporter across 4 outlets — consistent adversarial posture test |

### Editorial Leadership Changes

| Publication | Change | When | Key Question |
|---|---|---|---|
| **Wired** | Katie Drummond → Global Editorial Director | Sept 2023 | Did Meta coverage get more adversarial? Most important change — career-long adversarial pipeline (Gizmodo→Vice→Wired) |
| **Wired** | Leah Feiger → first-ever Politics Editor | Nov 2023 | Did Wired structurally shift from tech publication to tech-politics hybrid? |
| **Wired** | Nicholas Thompson → EIC | Feb 2017 | Did political coverage expand? (Thompson later became Atlantic CEO) |
| **Wired** | Gideon Lichfield → EIC | Sept 2020 | Double natural experiment: left MIT TR, arrived at Wired — test both source-side and dest-side effects |
| **NYT** | Joseph Kahn → Executive Editor | June 2022 | Under his leadership, NYT sued OpenAI (Dec 2023). Did AI/Meta coverage shift? |
| **NYT** | Pui-Wing Tam → Technology Editor | Jan 2015 | Built entire NYT tech team — recruited Isaac, Frenkel, Hill, Weise, Grant, Mickle. Institutional architect |
| **NYT** | Zach Seward → Editorial Director of AI | Feb 2024 | First AI editorial role. Pro-AI-for-journalism within guardrails. Built Echo, Stet, Cheat Sheet |
| **The Atlantic** | Nicholas Thompson → CEO | Dec 2020 | Former Wired EIC becoming Atlantic CEO — direct editorial culture bridge between Condé Nast and Emerson Collective |
| **The Atlantic** | Adrienne LaFrance → Executive Editor | May 2019 | Wrote "Facebook is a Doomsday Machine" (2020). Did anti-tech-platforms framing intensify? |
| **MIT Tech Review** | Mat Honan → EIC | Aug 2021 | Double migration: Wired→BuzzFeed→MIT TR. Did AI coverage tone shift under ex-Wired writer? |
| **MIT Tech Review** | Gideon Lichfield → EIC | Dec 2017 | From Quartz/Economist — more investigative direction. Led MIT-Epstein scandal coverage |
| **MIT Tech Review** | Will Douglas Heaven → Senior AI Editor | Jan 2020 | BBC/New Scientist veteran shaping entire AI editorial direction. UK-based |
| **The Guardian** | Katharine Viner → EIC | June 2015 | Control: longest-stable leadership (11+ years). Best baseline for DiD analysis |
| **The Guardian** | OpenAI licensing deal | Feb 2025 | Destroys "pure control case" status — creates direct commercial relationship with Meta's #1 AI competitor |
| **The Guardian** | Samantha Oltman → "Reworked" AI editor | Feb 2026 | 4-month tenure before departure to Bloomberg — tests editorial resilience |

## Limitations

1. **Survivorship bias.** We only track journalists who are notable enough to have verifiable career histories. Beat reporters who leave journalism entirely are invisible.

2. **Confounders.** Journalist moves often coincide with other changes (new ownership, industry events, shifts in public sentiment toward tech). DiD with a control group mitigates but doesn't eliminate this.

3. **Small sample sizes.** Individual journalists produce ~20-50 articles per year. A 180-day pre/post window at a single outlet may yield only 10-25 articles per cell, limiting statistical power.

4. **Beat changes.** A journalist may change beats when switching publications (Karen Hao went from pure AI at MIT TR to broader tech at The Atlantic), confounding tone comparisons.

5. **Freelance periods.** Gaps between staff positions may include freelance work that's hard to track systematically.

6. **Causal identification.** DiD requires the **parallel trends assumption**: treatment and control publications would have followed the same trend absent the journalist's move. This is untestable and may be violated.

7. **Publication baselines.** The institutional component estimate depends on having good publication-wide tone baselines from other journalists' work. For publications with few tracked journalists, this estimate is noisy.

## Academic Novelty

**To our knowledge, no prior work applies difference-in-differences methodology to journalist-level editorial migration data to decompose media bias into institutional and individual components.**

The closest related work:

- **Gentzkow & Shapiro (2010)** decompose newspaper slant into demand-side (reader preferences) and supply-side (owner ideology) components, but treat publications as units, not journalists.
- **Groseclose & Milyo (2005)** measure media bias via think-tank citations, but don't track journalist-level variation.
- **Puglisi & Snyder (2011)** study newspaper coverage of political scandals, finding partisan patterns, but don't exploit journalist migrations as natural experiments.
- **Card & Krueger (1994)** establish the DiD methodology in labor economics (minimum wage and employment), which we adapt for editorial analysis.
- **Martin & Yurukoglu (2017)** study the persuasive effects of media slant on viewers, but from the audience side, not the production side.

MediaScope's Editorial Histories module fills this gap by:
1. Treating journalist migrations as natural experiments (novel application of DiD)
2. Building a reusable career tracking infrastructure that any AI agent can extend
3. Producing decomposition scores that are interpretable, comparable, and auditable
4. Shipping with verified starter data for **97 journalists** across 155+ publications, with 94 having multi-publication careers suitable for migration analysis

## References

1. Card, D. & Krueger, A.B. (1994). "Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania." *American Economic Review*, 84(4), 772-793.
2. Gentzkow, M. & Shapiro, J.M. (2010). "What Drives Media Slant? Evidence from U.S. Daily Newspapers." *Econometrica*, 78(1), 35-71.
3. Groseclose, T. & Milyo, J. (2005). "A Measure of Media Bias." *Quarterly Journal of Economics*, 120(4), 1191-1237.
4. Puglisi, R. & Snyder, J.M. (2011). "Newspaper Coverage of Political Scandals." *Journal of Politics*, 73(3), 931-950.
5. Martin, G.J. & Yurukoglu, A. (2017). "Bias in Cable News: Persuasion and Polarization." *American Economic Review*, 107(9), 2565-2599.
6. Angrist, J.D. & Pischke, J.-S. (2009). *Mostly Harmless Econometrics*. Princeton University Press. [DiD methodology reference]
