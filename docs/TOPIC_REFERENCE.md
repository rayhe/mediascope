# Topic Classification Quick Reference

> A compact lookup card for all 29 topic buckets used by MediaScope's classification system. For the full keyword lists, TF-IDF weighting details, and topic design rationale, see [METHODOLOGY.md §3](METHODOLOGY.md#3-topic-classification).

---

## How to Use This Reference

During article analysis, the topic classification system assigns articles to up to 3 topic buckets using keyword matching with TF-IDF weighting. Topics serve three purposes:

1. **Apples-to-apples asymmetry comparison** — compare coverage of Entity A vs Entity B within the *same* topic
2. **Genre detection** — financial topics trigger VADER inflation warnings (see [METHODOLOGY.md §16](METHODOLOGY.md#16-financial-journalism-vader-inflation))
3. **DiD analysis** — journalist coverage shifts are measured within topic buckets to control for event type

The **Boundary Rules** column below is critical: many topics have adjacent buckets that cover related-but-distinct territory. Misclassification here directly corrupts asymmetry scores.

---

## Category 1: AI & Technology

Topics covering AI technology, its outputs, and its ethical dimensions.

| # | Topic | What It Captures | Boundary Rules |
|---|-------|------------------|----------------|
| 1 | `ai_development` | AI technology creation: LLMs, training, inference, model architecture, AI strategy | NOT output quality (`ai_generated_content`), NOT moral dimensions (`ai_ethics_safety`), NOT commercial releases (`product_launch`) |
| 2 | `ai_generated_content` | AI output quality: deepfakes, generative artifacts, AI slop, model collapse, hallucinations | NOT technology creation (`ai_development`). Focus is on *what AI produces*, not how it's built |
| 3 | `ai_ethics_safety` | AI alignment, existential risk, algorithmic bias, responsible AI, safety research, moral philosophy | NOT technology creation (`ai_development`), NOT regulatory actions (`government_oversight`). Focus is philosophical/moral, not legal |
| 4 | `cybersecurity` | Hacking, security breaches, account takeovers, vulnerability exploits, prompt injection, zero-days | NOT data collection/surveillance (`privacy_data`), NOT policy enforcement (`content_moderation`). Focus is adversarial attacks, not institutional data practices |

---

## Category 2: Business & Finance

Topics covering corporate performance, strategy, and market dynamics.

| # | Topic | What It Captures | Boundary Rules |
|---|-------|------------------|----------------|
| 5 | `financial_results` | Earnings, revenue, profit, quarterly reporting, guidance, fiscal performance | NOT stock price/analyst ratings (`financial_markets`), NOT pricing strategy (`subscription_monetization`). **Genre trigger:** confidence ≥ 0.4 flags VADER inflation risk |
| 6 | `financial_markets` | Stock price movements, analyst ratings, price targets, valuations, market-cap milestones, investment thesis | NOT earnings reporting (`financial_results`), NOT business decisions (`corporate_strategy`). Focus is Wall Street framing |
| 7 | `corporate_strategy` | M&A, partnerships, pivots, market entry decisions, competitive positioning | NOT specific releases (`product_launch`), NOT business decisions reframed as infrastructure (`infrastructure_impact`) |
| 8 | `product_launch` | Specific product releases, feature announcements, launch events, rollouts, betas | NOT strategic decisions (`corporate_strategy`), NOT technology creation (`ai_development`), NOT device hardware (`hardware_wearables`) unless the article focuses on the launch event itself |
| 9 | `subscription_monetization` | Paywalls, subscription pricing, rate-limiting, premium tiers, monetization practices | NOT earnings/stock (`financial_results`), NOT specific releases (`product_launch`). Focus is the *pricing/gating decision*, not the product itself |

---

## Category 3: Regulation & Legal

Topics covering government oversight, legal proceedings, and enforcement.

| # | Topic | What It Captures | Boundary Rules |
|---|-------|------------------|----------------|
| 10 | `antitrust_regulation` | Competition law, monopoly, FTC/EC/DOJ enforcement, DMA/DSA, consent decrees | NOT regulatory hearings without antitrust angle (`government_oversight`), NOT content fees (`content_licensing`), NOT consumer fraud (`consumer_protection`) |
| 11 | `government_oversight` | National security reviews, export controls, AI regulation hearings, Congressional testimony, military AI policy | NOT competition law (`antitrust_regulation`), NOT AI moral philosophy (`ai_ethics_safety`). Focus is government actors exercising oversight |
| 12 | `litigation` | General lawsuits, court filings, legal proceedings, settlements, verdicts, MDL consolidation | NOT consumer fraud enforcement (`consumer_protection`), NOT content licensing disputes (`content_licensing`). Use as default legal bucket when specialized legal topics don't fit |
| 13 | `consumer_protection` | AG enforcement, deceptive practices (UDAP), dark patterns, consumer fraud, state-level consumer lawsuits | NOT general legal (`litigation`), NOT competition law (`antitrust_regulation`), NOT youth-specific harms (`child_safety`). Focus is AG/consumer-rights enforcement |
| 14 | `content_licensing` | Publishing fees, neighboring/related rights, content compensation disputes, news licensing deals, bargaining codes, EU copyright directive | NOT competition law (`antitrust_regulation`), NOT general legal (`litigation`), NOT business decisions (`corporate_strategy`). Focus is publisher-tech platform compensation |

---

## Category 4: Society & Safety

Topics covering social impact, youth protection, and content governance.

| # | Topic | What It Captures | Boundary Rules |
|---|-------|------------------|----------------|
| 15 | `child_safety` | Youth protection: addiction, teen mental health, CSAM, parental controls, COPPA, age verification | NOT consumer fraud (`consumer_protection`), NOT content policy (`content_moderation`), NOT school impact (`education`) |
| 16 | `content_moderation` | Platform governance: content removal, misinformation, disinformation, hate speech, censorship | NOT data collection (`privacy_data`), NOT cybersecurity exploits (`cybersecurity`), NOT youth protection (`child_safety`) |
| 17 | `privacy_data` | Data collection, surveillance, tracking, GDPR, consent, encryption, user data practices | NOT hacking/exploits (`cybersecurity`), NOT content policy (`content_moderation`). Focus is institutional data practices, not adversarial attacks |
| 18 | `education` | Technology's impact on schools, classrooms, students, academic performance, phone bans, Chromebooks | NOT youth protection/harm (`child_safety`), NOT platform governance (`content_moderation`). Focus is the educational setting specifically |

---

## Category 5: Workforce & Labor

Topics covering employment, workplace dynamics, and labor displacement.

| # | Topic | What It Captures | Boundary Rules |
|---|-------|------------------|----------------|
| 19 | `layoffs` | Formal workforce actions: layoffs, firings, headcount cuts, restructuring, severance, reduction in force | NOT internal morale (`workplace_culture`), NOT macro employment trends (`labor_market`), NOT leadership decisions (`executive_behavior`) |
| 20 | `workplace_culture` | Internal organizational dynamics: morale, burnout, attrition, retention, toxic culture, return-to-office | NOT formal workforce actions (`layoffs`), NOT leadership decisions (`executive_behavior`). Focus is lived employee experience |
| 21 | `labor_market` | Macroeconomic employment and wage dynamics: BLS data, labor economists, job displacement, reskilling | NOT specific workforce actions (`layoffs`), NOT company-internal dynamics (`workplace_culture`), NOT recursive self-automation (`worker_ai_displacement`) |
| 22 | `worker_ai_displacement` | Workers whose labor trains/builds AI that replaces them — the recursive irony of self-automation | NOT macro employment trends (`labor_market`), NOT formal layoffs (`layoffs`), NOT internal morale (`workplace_culture`). Focus is the self-automation feedback loop |
| 23 | `executive_behavior` | CEO statements, leadership decisions, executive departures, management culture | NOT internal morale (`workplace_culture`), NOT formal layoffs (`layoffs`). Focus is leadership-level actions and conduct |

---

## Category 6: Infrastructure & Hardware

Topics covering physical technology, energy, and environmental impact.

| # | Topic | What It Captures | Boundary Rules |
|---|-------|------------------|----------------|
| 24 | `infrastructure_impact` | Data center construction, energy/water usage, community opposition (NIMBY), environmental footprint, tax breaks | NOT emissions/climate policy (`energy_climate`), NOT business decisions (`corporate_strategy`). Focus is local physical impact |
| 25 | `energy_climate` | Fossil fuel dependency, carbon emissions, renewable energy transitions, climate policy, utility/ratepayer dynamics | NOT data center construction (`infrastructure_impact`), NOT business decisions (`corporate_strategy`). Focus is energy systems and climate consequences |
| 26 | `hardware_wearables` | Smart glasses, VR/AR headsets, fitness trackers, hearing aids, wearable computing, EMG, neural bands | NOT general releases (`product_launch`), NOT underlying technology (`ai_development`). Focus is the physical device category |
| 27 | `health_tech` | Medical devices, brain-computer interfaces, clinical AI, digital health, FDA approval, clinical trials | NOT general technology (`ai_development`), NOT commercial releases (`product_launch`). Focus is medical/clinical application |

---

## Category 7: Specialized

Topics with narrow but distinct analytical value.

| # | Topic | What It Captures | Boundary Rules |
|---|-------|------------------|----------------|
| 28 | `defense_military` | Military applications, defense contracts, dual-use technology, warfare AI, tactical systems | NOT general government oversight (`government_oversight`). May co-occur with `hardware_wearables` for military AR devices |
| 29 | `prediction_markets` | Betting/wagering platforms, event contracts, CFTC regulation, binary options | NOT earnings/market performance (`financial_results`). Narrow bucket for a specific product category |

---

## Adjacency Map — Commonly Confused Pairs

These topic pairs share surface-level vocabulary but capture distinct editorial framings. Misclassification between them is the #1 source of asymmetry score corruption.

| Pair | Disambiguation Rule | Example |
|------|---------------------|---------|
| `layoffs` ↔ `workplace_culture` | Layoffs = formal actions (cuts, headcount). Culture = lived experience (morale, burnout) | "Meta cut 10,000 jobs" → `layoffs`. "Employees describe soul-crushing environment" → `workplace_culture` |
| `layoffs` ↔ `labor_market` | Layoffs = specific company actions. Labor market = macro trends (BLS, economists) | "Meta fired its AI team" → `layoffs`. "Tech unemployment rose 2.3% in Q2" → `labor_market` |
| `worker_ai_displacement` ↔ `labor_market` | Worker displacement = recursive self-automation. Labor market = macro employment data | "Moderators trained their own replacement" → `worker_ai_displacement`. "AI may eliminate 40% of jobs" → `labor_market` |
| `ai_development` ↔ `ai_ethics_safety` | Development = building technology. Ethics = moral/philosophical dimensions | "Meta released Llama 4" → `ai_development`. "Researchers warn of alignment failure" → `ai_ethics_safety` |
| `ai_development` ↔ `ai_generated_content` | Development = creation. Generated content = output quality | "Training on 15T tokens" → `ai_development`. "AI slop floods Instagram" → `ai_generated_content` |
| `privacy_data` ↔ `cybersecurity` | Privacy = institutional collection/surveillance. Cybersecurity = adversarial attacks | "Meta tracked badge swipes" → `privacy_data`. "Researchers hijacked Meta's AI agent" → `cybersecurity` |
| `child_safety` ↔ `consumer_protection` | Child safety = youth-specific harms. Consumer protection = general AG enforcement | "Teens addicted to Instagram" → `child_safety`. "AGs allege deceptive dark patterns" → `consumer_protection` |
| `litigation` ↔ `consumer_protection` | Litigation = general legal. Consumer protection = deceptive practices/UDAP specifically | "Meta sued over data breach" → `litigation`. "AGs pursue UDAP violations" → `consumer_protection` |
| `antitrust_regulation` ↔ `government_oversight` | Antitrust = competition law. Oversight = regulatory hearings, export controls | "FTC monopoly case" → `antitrust_regulation`. "Senate hearing on AI regulation" → `government_oversight` |
| `financial_results` ↔ `financial_markets` | Results = earnings/revenue reporting. Markets = stock price/analyst ratings/valuation | "Q1 revenue $56B" → `financial_results`. "Analyst raised price target to $800" → `financial_markets` |
| `financial_results` ↔ `subscription_monetization` | Results = earnings/stock. Subscription = pricing/paywall decisions | "Revenue beat by $1B" → `financial_results`. "$7.99/mo paywall drew criticism" → `subscription_monetization` |
| `corporate_strategy` ↔ `product_launch` | Strategy = M&A/partnerships/pivots. Launch = specific product releases | "Meta acquires Virtue AI" → `corporate_strategy`. "Meta launched Ray-Ban Display glasses" → `product_launch` |
| `infrastructure_impact` ↔ `energy_climate` | Infrastructure = local data center impact/NIMBY. Energy = emissions/renewables/climate policy | "2.3 GW data center blocked by NIMBY protests" → `infrastructure_impact`. "Natural gas burns raise CO2 concerns" → `energy_climate` |
| `content_licensing` ↔ `antitrust_regulation` | Content licensing = publisher fees/compensation. Antitrust = competition law/monopoly | "French media demanded content fees" → `content_licensing`. "EC alleges abuse of dominance" → `antitrust_regulation` |
| `content_licensing` ↔ `litigation` | Content licensing = content compensation disputes. Litigation = general legal proceedings | "News publishers seek licensing deal" → `content_licensing`. "Judge dismissed defamation claim" → `litigation` |

---

## Multi-Topic Classification

Articles commonly span 2–3 topics simultaneously. The system retains the top 3 matches by confidence. Common multi-topic patterns:

| Pattern | Example | Topics |
|---------|---------|--------|
| **Regulatory + safety** | FTC action targeting teen features | `antitrust_regulation` + `child_safety` + `consumer_protection` |
| **Legal + financial** | $1.4T penalty disclosure in 10-K filing | `litigation` + `financial_results` + `child_safety` |
| **Tech + ethics** | AI alignment research from Meta's FAIR lab | `ai_development` + `ai_ethics_safety` |
| **Hardware + subscription** | Smart glasses features gated behind paywall | `hardware_wearables` + `subscription_monetization` |
| **Infrastructure + energy** | Data center's fossil fuel consumption | `infrastructure_impact` + `energy_climate` |
| **Labor + displacement** | Contractors trained AI that cut their jobs | `worker_ai_displacement` + `layoffs` |
| **Licensing + litigation** | EU court ruling on publisher content fees | `content_licensing` + `litigation` + `antitrust_regulation` |
| **Military + hardware** | AR glasses adapted for battlefield use | `defense_military` + `hardware_wearables` |

---

## Genre Detection Bridge

Topic classification feeds into MediaScope's genre detection pipeline, which adjusts sentiment scoring:

| Genre | Topic Trigger | Confidence Threshold | Sentiment Effect |
|-------|---------------|---------------------|------------------|
| **Financial** | `financial_results` | ≥ 0.4 | VADER inflation warning — boosterism vocabulary inflates scores 0.3–0.5 points. See [METHODOLOGY.md §16](METHODOLOGY.md#16-financial-journalism-vader-inflation) |
| **Security/technical** | `cybersecurity` | ≥ 0.4 | Domain language ("exploit," "vulnerability," "breach") inflates emotional intensity — dampened to avoid false-positive alarmism |
| **Investment analysis** | `financial_markets` | ≥ 0.4 | Investor-oriented framing (`investor_advisory` device type) uses conditional/aspirational language that VADER may misread |

---

## CLI Reference

```bash
# Classify a single article by text
mediascope analyze --text "Article text here..." --show-topics

# List topics detected in a stored article
mediascope analyze --publication wired --target Meta --since 2026-07-01 --show-topics

# Run asymmetry within a specific topic
mediascope score --publication wired --target Meta --topic child_safety

# Compare topic-level asymmetry across publications
mediascope score --publication wired --target Meta --topic child_safety --compare guardian nytimes
```

---

## References

- **Full keyword lists:** [METHODOLOGY.md §3](METHODOLOGY.md#3-topic-classification) — all 29 buckets with complete keyword sets and TF-IDF weighting details
- **Topic design rationale:** [METHODOLOGY.md §3 Note on topic design](METHODOLOGY.md#3-topic-classification) — why each bucket exists and how boundaries were drawn
- **Genre detection pipeline:** [METHODOLOGY.md §16](METHODOLOGY.md#16-financial-journalism-vader-inflation) — financial genre VADER inflation analysis
- **Topic classification demo:** `examples/topic_classification_demo.py` — runnable demo with 15 real-article snippets and adjacency warnings
- **Same-event comparison clusters:** [QUALITY_STANDARDS.md §10.2](QUALITY_STANDARDS.md) — 13 validated clusters showing topic-controlled cross-publication analysis
