# MediaScope Methodology

## Overview

MediaScope employs a multi-layered analytical framework to detect, measure, and report coverage asymmetry in media publications. This document describes the statistical methods, scoring frameworks, and academic foundations underpinning the toolkit.

## 1. Sentiment Analysis Framework

### 1.1 Multi-Model Approach

MediaScope uses three sentiment analysis layers, cross-validated against each other:

| Layer | Model | Purpose | Speed |
|---|---|---|---|
| Baseline | VADER (Hutto & Gilbert, 2014) | Lexicon-based, social media optimized | Fast |
| Secondary | TextBlob (Loria, 2018) | Pattern-based, adjective-focused | Fast |
| Primary | GPT-4o-mini / local LLM | Contextual editorial tone analysis | Slow |

The composite score weights the primary model at 0.5, with VADER and TextBlob each contributing 0.25. When the primary model is unavailable, VADER and TextBlob are weighted equally.

### 1.2 Eight-Dimension Tone Scoring

Beyond simple positive/negative polarity, MediaScope scores articles on eight dimensions designed to capture editorial framing:

| # | Dimension | Range | What It Measures |
|---|---|---|---|
| 1 | **Overall Tone** | -1.0 to +1.0 | Net editorial stance toward the entity |
| 2 | **Emotional Language Intensity** | 0.0 to 1.0 | Ratio of emotionally charged words to neutral language |
| 3 | **Source Authority Framing** | -1.0 to +1.0 | Whether quoted sources are used to undermine (-) or validate (+) the entity |
| 4 | **Agency Attribution** | -1.0 to +1.0 | Whether the entity is framed as passive/victim (-) or active/powerful (+) |
| 5 | **Headline-Body Alignment** | -1.0 to +1.0 | Whether the headline accurately represents the article body |
| 6 | **Anonymous Source Ratio** | 0.0 to 1.0 | Fraction of sources that are unnamed or anonymous |
| 7 | **Speculative Language Ratio** | 0.0 to 1.0 | Frequency of hedging words: "could," "might," "may," "reportedly" |
| 8 | **Comparative Framing** | -1.0 to +1.0 | Whether the entity is compared unfavorably (-) or favorably (+) to peers |

#### Prompt Template (for LLM-based scoring)

```
Analyze the following article for editorial tone toward [{entity}].
Score each dimension from the scale provided. Be precise — a neutral
article should score near 0, not at the extremes.

Article headline: {headline}
Article text: {text}

Score these dimensions:
1. Overall tone toward {entity} (-1.0 to +1.0):
2. Emotional language intensity (0.0 to 1.0):
3. Source authority framing toward {entity} (-1.0 to +1.0):
4. Agency attribution for {entity} (-1.0 to +1.0):
5. Headline-body alignment (-1.0 to +1.0):
6. Anonymous source ratio (0.0 to 1.0):
7. Speculative language ratio (0.0 to 1.0):
8. Comparative framing of {entity} vs peers (-1.0 to +1.0):

Respond with only the 8 numbers, one per line.
```

### 1.3 Academic References

- **VADER**: Hutto, C.J. & Gilbert, E.E. (2014). "VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text." ICWSM.
- **Media Bias Detection**: Spinde, T., et al. (2022). "BABE: A Benchmark for Annotated Media Bias Detection." In Findings of ACL.
- **AI Coverage Sentiment**: Bunz, M. & Braghieri, L. (2021). "The AI Index 2021 Annual Report." Stanford HAI. [finding: Guardian 29% positive AI coverage vs WSJ 49%]
- **Microsoft Research**: Raza, S., et al. (2025). "Media Bias Detector: Automated Detection of Bias in News Articles." CHI 2025.

## 2. Asymmetry Scoring Engine

### 2.1 Core Formula

The Asymmetry Score (AS) quantifies how much more negatively (or positively) a publication covers a target entity compared to its coverage of peer entities:

```
AS = mean(tone_scores_target) - mean(tone_scores_peers)
```

Where:
- `tone_scores_target` = overall tone scores for all articles primarily about the target entity
- `tone_scores_peers` = overall tone scores for all articles primarily about peer entities
- A **negative AS** indicates the target receives more negative coverage than peers
- An AS of 0 indicates equivalent treatment

### 2.2 Statistical Significance Testing

#### Welch's t-test

We use Welch's t-test (not Student's t-test) because we cannot assume equal variance between the target and peer coverage distributions:

```
t = (X̄₁ - X̄₂) / √(s₁²/n₁ + s₂²/n₂)
```

Degrees of freedom estimated via Welch-Satterthwaite equation. Significance threshold: α = 0.05.

#### Cohen's d Effect Size

Raw p-values can be misleading with large sample sizes. Cohen's d provides a standardized measure of practical significance:

```
d = (X̄₁ - X̄₂) / s_pooled

where s_pooled = √((s₁² + s₂²) / 2)
```

Interpretation (Cohen, 1988):
| d | Interpretation |
|---|---|
| < 0.2 | Negligible |
| 0.2–0.5 | Small |
| 0.5–0.8 | Medium |
| > 0.8 | Large |

#### Bootstrap Confidence Intervals

For non-parametric confidence intervals on the asymmetry score:

1. Resample target scores (with replacement) 1,000 times
2. Resample peer scores (with replacement) 1,000 times
3. Calculate AS for each bootstrap sample
4. Report 2.5th and 97.5th percentiles as 95% CI

### 2.3 Confound Controls

#### News Event Severity Normalization

A publication may cover a company more negatively during genuine crises (data breach, layoffs, antitrust action). To control for this:

1. Classify each article by topic bucket (see §3)
2. For each topic, compare the target's coverage to coverage of other companies in the same topic
3. This isolates editorial framing from event severity

Example: If Meta and Google both had layoffs, we compare how Wired covered Meta's layoffs vs Google's layoffs — not Meta's layoffs vs Google's product launches.

#### Volume Normalization

More coverage ≠ more bias. We normalize by:
- Calculating per-article tone scores (not aggregate)
- Reporting article counts alongside asymmetry scores
- Flagging when sample sizes are too small for reliable inference (n < 10)

## 3. Topic Classification

### 3.1 Standardized Topic Buckets

Articles are classified into 25 topic buckets to enable apples-to-apples comparison:

| Topic | Keywords |
|---|---|
| `layoffs` | layoff, fired, cut, reduction, restructuring, workforce, headcount, eliminated |
| `ai_development` | artificial intelligence, AI, machine learning, neural, LLM, language model, training data |
| `privacy_data` | privacy, data, surveillance, tracking, GDPR, consent, collection, user data |
| `antitrust_regulation` | antitrust, monopoly, regulation, FTC, DOJ, market power, dominance, consent decree |
| `child_safety` | children, teens, youth, minor, addiction, mental health, COPPA, age verification |
| `content_moderation` | moderation, misinformation, disinformation, hate speech, policy, removal, censorship |
| `ai_generated_content` | slop, AI slop, synthetic content, AI-generated, generative AI content, deepfake, AI art, model collapse, engagement bait, hallucination |
| `financial_results` | earnings, revenue, profit, stock, market cap, quarterly, fiscal, guidance |
| `product_launch` | launch, release, announce, unveil, new feature, update, rollout, beta |
| `executive_behavior` | CEO, executive, leadership, management, culture, workplace, internal |
| `litigation` | lawsuit, sued, settlement, verdict, court, judge, plaintiff, damages |
| `prediction_markets` | prediction market, Polymarket, Kalshi, betting, gambling, wagering, event contract, CFTC, binary option |
| `corporate_strategy` | acquisition, merger, M&A, partnership, diversification, pivot, market entry, rival, competitive, spin-off |
| `workplace_culture` | morale, employee morale, burnout, attrition, retention, toxic culture, internal revolt, soul-crushing, return to office, disgruntled |
| `government_oversight` | national security, export controls, classified, embargo, sanctions, nonproliferation, Pentagon, policymakers, lawmakers, AI regulation, military AI |
| `defense_military` | military, defense contractor, warfare, combat, Army, Pentagon, DoD, drone, weapons system, IVAS, Anduril, Palantir, Special Operations, tactical AI |
| `infrastructure_impact` | data center, hyperscale, power grid, electricity demand, power bills, NIMBY, rezoning, environmental impact, community opposition, tax breaks, megawatt, cooling system |
| `labor_market` | labor market, employment growth, unemployment, job market, workforce, BLS, Bureau of Labor Statistics, wage growth, labor economist, job displacement, reskilling, career model, labor transition |
| `worker_ai_displacement` | automate themselves, train their replacement, replace workers, worker dignity, alienation, dehumanizing, AI double, AI clones, sabotage, countermeasures, worker resistance, self-automation, flattened into modules, digital labor, AI replacement, replaced by AI |
| `health_tech` | brain-computer interface, BCI, neural interface, neural implant, neuroprosthetic, neurotech, EEG, MEG, fMRI, paralysis, paralyzed, prosthetic, medical device, FDA approval, clinical trial, digital health, telehealth, medtech, genomics, gene therapy, CRISPR, surgical robot, drug discovery, medical AI, noninvasive |
| `cybersecurity` | cybersecurity, cyber attack, hacker, hackers, hacking, data breach, security breach, security vulnerability, zero-day, account takeover, phishing, social engineering, password reset, ransomware, malware, exploit, MFA, multi-factor authentication, 2FA, security researcher, security patch, emergency patch, confused deputy, privilege escalation, defaced, identity theft, CISA, NIST, infosec |
| `ai_ethics_safety` | AI ethics, AI safety, AI alignment, alignment problem, misalignment, existential risk, AGI safety, responsible AI, ethical AI, AI governance, algorithmic bias, algorithmic fairness, AI accountability, AI transparency, superintelligence, AI philosopher, AI ethicist, reward hacking, specification gaming, alignment research, safety research, moral philosophy, technology ethics, machine ethics |
| `education` | school, schools, classroom, classrooms, teacher, teachers, student, students, academic, academic performance, education, educational, learning, school district, school districts, school hours, school day, campus, smartphone ban, phone ban, Chromebook, Chromebooks, PTA, parent-teacher, K-12, elementary school, middle school, high school |
| `subscription_monetization` | subscription, subscriptions, subscribe, subscribing, paywall, paywalls, paywalled, paywalling, rate limit, rate limits, rate-limited, rate limited, rate limiting, rate-limiting, premium tier, premium subscription, premium plan, free tier, freemium, free plan, monthly fee, monthly bill, monthly charge, monthly subscription, annual subscription, pricing tier, pricing tiers, pricing plan, pay-to-play, pay to play, pay to use, monetize, monetization, monetizing, in-app purchase, in-app purchases, microtransaction, microtransactions, recurring charge, recurring fee, upsell, upselling, upsold, subscription fatigue, subscription creep, locked behind, gated behind, behind a paywall, unlock, unlocking |
| `hardware_wearables` | smart glasses, AR glasses, augmented reality glasses, wearable, wearables, wearable device, VR headset, VR headsets, mixed reality headset, Ray-Ban, Ray-Ban Meta, Oakley Meta, Quest, Meta Quest, Apple Vision Pro, heads-up display, HUD, earbuds, smart earbuds, smart watch, smartwatch, fitness tracker, fitness band, hearing aid, hearing aids, hearing assistance, neural band, EMG, brain-computer interface, haptic, haptics, gesture control, eye tracking, gaze tracking, spatial computing, spatial audio |

Classification uses keyword matching with TF-IDF weighting. An article can match multiple topics; the top 3 by confidence are retained.

**Note on topic design:** The 25 buckets are designed for apples-to-apples comparison within a topic across companies. The `ai_generated_content` topic captures coverage of AI output quality and generative AI byproducts, distinct from `ai_development` (technology creation). The `ai_ethics_safety` topic captures coverage of AI alignment, AI safety research, existential risk, algorithmic bias, responsible AI, and the philosophical/moral dimensions of AI development, distinct from `ai_development` (technology creation) and `government_oversight` (regulatory actions). The `workplace_culture` topic captures internal organizational dynamics (morale, burnout, culture), distinct from `layoffs` (formal workforce actions) and `executive_behavior` (leadership decisions). The `labor_market` topic captures macroeconomic employment and wage dynamics (BLS data, labor economists, job displacement), distinct from `workplace_culture` (company-internal dynamics) and `layoffs` (specific workforce actions). The `worker_ai_displacement` topic captures coverage of workers whose labor directly trains, builds, or enables the AI systems that replace them — the recursive irony of self-automation — distinct from `labor_market` (macro employment trends), `layoffs` (formal workforce actions), and `workplace_culture` (internal morale). The `prediction_markets` topic captures coverage of betting/wagering platforms and event contracts, distinct from `financial_results` (earnings/market performance). The `corporate_strategy` topic captures M&A, partnerships, and market entry decisions, distinct from `product_launch` (specific releases). The `infrastructure_impact` topic captures coverage of data center construction, energy/water usage, community opposition (NIMBY), and environmental consequences of tech infrastructure, distinct from `corporate_strategy` (business decisions) and `ai_development` (technology itself). The `health_tech` topic captures coverage of medical technology, brain-computer interfaces, clinical devices, and health-focused AI, distinct from `ai_development` (general technology) and `product_launch` (commercial releases). The `cybersecurity` topic captures coverage of hacking, security breaches, account takeovers, and vulnerability exploits, distinct from `privacy_data` (collection/surveillance) and `content_moderation` (policy enforcement). The `education` topic captures coverage of technology's impact on schools, classrooms, students, and academic performance, distinct from `child_safety` (child protection/harm) and `content_moderation` (platform governance). The `subscription_monetization` topic captures coverage of product paywalling, subscription pricing, rate-limiting, and monetization practices, distinct from `financial_results` (earnings/market performance) and `product_launch` (specific releases). The `hardware_wearables` topic captures coverage of smart glasses, VR/AR headsets, fitness trackers, hearing aids, and other wearable computing devices, distinct from `product_launch` (general releases) and `ai_development` (underlying technology).

## 4. Framing Device Detection

### 4.1 Taxonomy

MediaScope detects 53 framing device types, organized into three tiers: core devices (10 pattern-matched types covering fundamental editorial techniques), extended devices (37 added from real-article analysis), and structural devices (6 detected via post-pass heuristics rather than simple pattern matching).

#### Core Devices

| Device | Description | Detection Pattern |
|---|---|---|
| **Guilt by Association** | Linking entity to controversial actors/events | Entity + controversial entity in same paragraph |
| **Anonymous Authority** | Using unnamed sources as definitive evidence | "sources say," "people familiar," "according to sources" |
| **Catastrophizing** | Framing outcomes as existential/irreversible | "crisis," "catastrophe," "existential threat," "doomsday" |
| **False Balance** | Presenting fringe views as equivalent to mainstream | "some say... others say" with asymmetric evidence |
| **Selective Omission Signal** | Notable absences detectable in text | "declined to comment" without context, missing competitor comparison |
| **Emotional Appeal** | Using emotional language instead of evidence | "heartbreaking," "chilling," "disturbing," "alarming" |
| **Loaded Language** | Word choices that carry implicit judgment | "admitted," "conceded," "insisted," "claimed" (vs neutral "said"); also workplace coercion language ("no opt-out," "revolt," "training their own replacements") |
| **Power Asymmetry** | Framing institutional/financial power against individual vulnerability | Dollar-magnitude near individual, "army of lawyers," David vs Goliath language, fine-per-violation-could-bankrupt patterns |
| **CEO Personalization** | Attributing a company's institutional actions to its CEO personally, implying one-person authoritarian control | Possessive constructions ("Zuckerberg's Meta," "Musk's Tesla"), CEO-led constructions ("Zuckerberg-led Meta"). Makes corporate decisions feel like personal edicts, amplifying negative framing. |
| **Litigation Framing** | Positioning an entity as adversarially using courts rather than cooperating with regulators or peers | "Seeking/filing/mounting legal challenge," "legal battle against," "took X to court." Distinct from neutral legal reporting — frames litigation as aggression rather than legitimate dispute resolution. |

#### Extended Devices

These were added through systematic analysis of real articles from the five tracked publications. Each addresses a framing technique not captured by the core devices.

| Device | Description | Detection Pattern | Discovered From |
|---|---|---|---|
| **Straw Man** | Misrepresenting an entity's position to make it easier to attack | Simplified-claim-then-rebut constructions | General pattern |
| **Refusal Amplification** | Emphasizing an entity's refusal/non-cooperation beyond its news value | "declined," "refused," "would not say," positioned to imply guilt | General pattern |
| **Juxtaposition** | Placing contrasting facts side-by-side for editorial effect | Investment/spending figures adjacent to layoffs/harm; surveillance tech near consumer product language | NYT Meta AI employees article; Wired glasses launch |
| **Timeline Implication** | Using temporal sequencing to imply causation | "After X happened, Y occurred" (when X did not cause Y) | Guardian whistleblower article |
| **Military Techno-Optimism** | Editorial framing that normalizes violence through technology language | "Optimize the human as a weapons system," "AI-driven targeting," UX language for weapons | MIT TR Anduril/Meta glasses article |
| **Selective Rehabilitation** | Juxtaposing a figure's past controversy with current acceptance to imply opportunism | "Ousted from X... now welcomed at Y," "friendlier posture," "softened stance" | General pattern |
| **Rhetorical Question** | Questions that imply negligence without directly asserting it | "Were there even guardrails?" "Did anyone think to...?" "Why didn't they...?" | General pattern |
| **Ironic Quotation** | Deploying a source's own words, then immediately undercutting them editorially | Quote followed by "But," "Yet," "In reality," or verdict like "wrongly believe" | Atlantic AI slop article |
| **Isolation Framing** | Singling out a company as "the only" one not doing what peers have done | "The only major company that has not," "unlike its peers," "singled out," "out of step" | NYT AI voluntary review article |
| **Pressure Language** | Editorial word choices that frame actions as coercive | "Pressing," "pushing," "strong-arming," "confidential request," "private demand" | NYT AI voluntary review article |
| **Self-Referential Investigation** | Publication citing its own prior reporting as evidence within adversarial coverage, creating a closed feedback loop | "reporting by WIRED," "a WIRED investigation found," "as WIRED previously reported," "WIRED has learned" patterns with 5+ tracked publication names | Wired Meta coverage pattern — publication becomes both investigator and source authority |
| **Geopolitical Regulatory Pressure** | Framing international regulatory tensions as geopolitical confrontation, using diplomatic/sovereignty language | Embassy/diplomatic submissions as pressure tools, sovereignty/defiance rhetoric ("will not be deterred"), transatlantic tension language, "singles out American tech" patterns | Guardian UK tech crackdown article — framing US-UK regulatory disputes as international confrontation rather than policy debate |
| **Sovereignty Framing** | Deploying national/patriotic identity language to delegitimize foreign corporate or government positions | "British families," "American innovation," "our children" in tech regulation context; "national interest/security" near tech entities; "act in the UK's national interest" | Guardian UK tech crackdown article — distinct from loaded_language because it strategically invokes national identity rather than just emotional vocabulary |
| **Scale/Magnitude Framing** | Deploying large raw numbers, calculated maximums, scale analogies, or victim/case rosters to create impressions of excess, danger, or harm beyond what a neutral factual reference would convey | "up to 6% of global revenue," "enough to power 750,000 homes," "$70 billion in losses since 2020," "more than 2,000 lawsuits," "76% spike" — calculated maximums, cumulative totals, scale analogies, victim rosters, comparison amplifiers | Cross-article pattern — Atlantic data centers, NYT/Reuters child-safety litigation, EU DSA coverage. Distinct from loaded_language because the emotional charge comes from the number itself, not from adjectives or pejorative vocabulary |
| **Corporate Reassurance Undercut** | Quoting a corporate entity's reassurance or responsibility language and immediately undercutting it with contradicting evidence or adversarial conjunctions | "carefully designed with privacy safeguards" + "but/however/yet" + failure evidence; "no indication of improper" + contradiction; "committed to / takes seriously" + contradiction + exposure/failure | Wired/Reuters MCI data exposure coverage — Meta's corporate communications reframed as hollow through editorial juxtaposition of reassurance language with reported failures |
| **Hypocrisy Frame** | Singling out an entity as the sole holdout that has not done what all peers have, framing inaction as hypocrisy or defiance rather than legitimate disagreement | "the only major company/developer that has not," "uniquely among its peers," "alone in refusing" — entity isolation + negation patterns with optional prepositional phrases between entity noun and negation clause | NYT AI voluntary review article — framing Meta as uniquely defiant among tech companies. Distinct from isolation_framing because hypocrisy_frame specifically implies moral failing (not just being different), and from pressure_language because the frame comes from peer comparison rather than institutional demands |
| **Sarcastic Correction** | Editorial sarcasm that mockingly concedes a positive outcome before immediately retracting it, weaponizing irony to undermine a company's position | "Of course... oh hang on/wait/no," "Just kidding," "Spoiler: it didn't," "...right? Wrong/Nope," "(Narrator: it did not.)," "Color me surprised," "Who could have predicted," "What could possibly go wrong," "Nothing to see here" — concede-then-retract and standalone sarcastic constructions | Engadget Meta/Wynn-Williams lawsuit article — explicit editorial sarcasm mocking Meta's market resilience after whistleblower book. Distinct from ironic_quotation (which undercuts *sources'* words) because sarcastic_correction is pure editorial voice deploying rhetorical sarcasm without quoting anyone |
| **Outsourced Intensity** | Loaded emotional language appearing in legal filings, complaint text, or whistleblower allegations quoted by the journalist, while the journalist's own prose remains neutral — outsourcing the emotional charge to authoritative documents | "the complaint alleges [loaded term]," "according to the filing... blatant/egregious/coercive," quoted legal language containing high-intensity characterizations, plaintiff/whistleblower allegations carrying emotional weight | Guardian Wynn-Williams lawsuit article (Jun 25, 2026) — all loaded language ("blatant violation," "coercive surveillance," "improper and unlawful") came from the complaint, not the journalist. Distinct from loaded_language (editorial voice) and anonymous_authority (unnamed sources). See also §7 for the separate quantitative outsourced intensity ratio measure |
| **Pathologizing Metaphor** | Sustained metaphorical framing that casts corporate or institutional behavior as addiction, disease, gluttony, or compulsive gambling — importing clinical/pathological associations onto business decisions | Addiction/dependency language ("addicted," "hooked," "dependent," "withdrawal," "cut off"), gluttony/excess consumption ("gorge," "voracious," "insatiable," "feeding frenzy," "glutton"), gambling compulsion ("high-rollers," "doubling down," "betting the house"), disease/pathology ("infected," "contagion," "metastasized," "toxic") | Gizmodo Meta/Google AI tokens article (Jun 29, 2026) — "gorge itself on," "addicted," "token-hungry," "high-rollers," "cut off" — sustained addiction/gluttony metaphorical frame casting Meta's API consumption as pathological behavior rather than a business scaling decision. Distinct from loaded_language (individual word choices) and analogy_metaphor (single explicit comparisons) because pathologizing_metaphor is a sustained framing strategy that maps an entire clinical/pathological domain onto business activity |
| **Precedent Analogy** | Explicit comparison of a current controversy to a well-known historical case — importing the settled moral weight of the precedent onto the new situation, allowing readers to reach conclusions without independently evaluating the current facts | "echoes [adj]-era fights," "much like the [precedent] litigation," "following the playbook from [precedent]," "akin to [precedent]," "as was the case with [precedent]," "dispute mirrors/parallels [precedent]" | Reuters Meta insurance defense article (Jun 23, 2026) — "echoes opioid-era coverage fights" imports the settled villainy of opioid manufacturers onto Meta's insurance dispute, framing social media addiction as morally equivalent to the opioid crisis without requiring the reader to evaluate that equivalence |
| **Confession Framing** | Using attribution verbs that frame a subject's statement as an admission of guilt or failure rather than neutral communication — "admits" vs. "said" imposes a confession frame before the reader encounters the content | "[Person/Title] admits/admitted/concedes/acknowledged that," "was forced to admit/acknowledge/concede," "finally/grudgingly admitted," "came clean about," "mea culpa," "in a rare/stunning admission/concession" | Wired "Meta CTO Andrew Bosworth Admits the Company's AI Reorg Was 'Atrocious'" (Jun 16, 2026) — headline frames a proactive internal memo as a forced confession. The attribution verb asymmetry (employees "describe" while executives "admit") is a systematic editorial stance technique documented in §4.2 |
| **Latecomer Narrative** | Editorial framing positioning a company as entering a space after competitors, implying it is playing catch-up rather than innovating independently — converts a strategic decision into a story of being behind | "exploring partnerships with," "joining the race," "playing catch-up," "market already dominated by," "following in the footsteps of," "late to the game," "copycat," "me-too product" | NYT Arena/Polymarket article (Jun 26, 2026) — framing Meta's prediction market exploration as catch-up to Polymarket and Kalshi, positioning partnership-seeking as an admission of inability to build independently. Distinct from straw_man (not misrepresenting a position) and juxtaposition (not side-by-side fact contrast) |
| **Regulatory Shadow** | Ambient editorial technique of inserting regulatory or legal context into product or business stories where it is tangential, casting a shadow over the primary subject without direct accusation | "increasing scrutiny," "drawn scrutiny from," "amid antitrust," "could face regulatory," "raised concerns about," "amid growing regulatory pressure," "watchdogs are watching," "under the eye of regulators" | NYT Arena article (Jun 26, 2026) — prediction market "scrutiny" and insider trading investigations inserted into a product story about Meta's Arena app, where the regulatory context applies to the prediction market industry broadly, not to Meta specifically. Distinct from litigation_framing (explicit legal actions) and geopolitical_regulatory_pressure (state-level pressure campaigns) |
| **Editorial Deflation** | Editorial technique of building up an ambitious technological vision or corporate plan across multiple paragraphs, then puncturing it with a brief dismissive or hedging phrase that implies failure without explicit argument — the deflation is the writer's editorial choice, appearing as casual hedging but functioning as skepticism-by-implication | "That's the idea, anyway," "or so X claims/hopes," "so the argument goes," "if it ever actually works/ships," "in theory, anyway," "but that's a big if," "whether that actually pans out" | MIT TR Anduril/Meta smart glasses article (May 18, 2026) — three paragraphs build up Anduril's ambitious cyborg-inspired AR battlefield vision (eye tracking, voice commands, drone control), then "That's the idea, anyway" deflates the entire vision into implied impracticality. Distinct from corporate_reassurance_undercut (undercuts company's OWN reassurance), sarcastic_correction (overtly mocking), and speculative_framing (projects negative futures) |
| **Denial Contradiction** | A source's direct denial or minimization is presented alongside evidence that contradicts it, making the denial land as implausible. The journalist places the denial and the contradiction in proximity so the reader can draw the conclusion without the journalist explicitly calling the source a liar | "does not exist" / "no final decision" / "purely exploratory" / "no evidence that" near evidence markers (found, revealed, code, analysis); combative pushback ("misleading," "dishonest," "baseless") near removal/contradiction evidence — both pre-quote ("called it baseless") and post-quote ("baseless," insisted) forms; soft minimization ("part of a pilot," "had not decided") editorially undercut by "does not answer/explain" or "but/however"; indirect-speech variant for articles that paraphrase rather than directly quote | Wired NameTag removal (Jun 8, 2026) — Meta spokesperson's "does not exist" denial contradicted by code analysis; Bosworth's "incredibly misleading" and "absolutely dishonest" followed by Meta removing the code the next day; Digital Trends (Jun 9, 2026) indirect-speech "part of a pilot" near editorial undercut; Engadget child safety (Jun 2026) — "no evidence" / "baseless" denials near verified/replicated evidence. Distinct from hypocrisy_frame (say one thing, do another over time), corporate_reassurance_undercut (PR language undermined), and refusal_amplification (repeated refusals to answer) |
| **Worker Replacement Irony** | Editorial framing that emphasizes the recursive quality of AI-driven displacement: workers who built, trained, or labeled the technology now find themselves replaced by it. The irony is structural — the sentence or passage juxtaposes the human contribution with the resulting system that eliminates their roles, making the workers' own labor the instrument of their displacement | "trained/built/created/labeled [AI/models/bots/systems]" near "replaced/eliminated/laid off/made redundant"; reverse form "replacement by those same/the very [models/systems] they [trained/built]"; chant/slogan form "We trained the bots... left behind" | WebProNews Meta Dublin contractors (May 2026) — "Content moderators who trained AI models now face replacement by those same systems"; "Their replacements are the very models they helped build"; worker chants "We trained the bots. We did the grind. Now we're being left behind." Distinct from juxtaposition (profits vs. cuts), hypocrisy_frame (stated policy vs. actual behavior) |
| **Two-Tier Treatment** | Editorial framing that explicitly contrasts the treatment of two classes of workers — typically full-time employees vs. contractors, permanent staff vs. outsourced labor — by laying out both packages/conditions side by side so the reader draws the inequality conclusion | "[full-time/permanent] employees... [receive X]... [contractors/outsourced] workers... [get far less/nothing]"; "denied all the privileges/benefits of [company] staff"; "using [company] tools/platforms... but... not [company] employees" | WebProNews Meta Dublin contractors (May 2026) — "Full-time employees reportedly stand to receive four months' pay plus two weeks for every year served. Covalen workers get far less"; "They're constantly using Meta tools, they're on Meta platforms... But they're denied all the privileges and benefits of Meta staff." Distinct from juxtaposition (profits vs. cuts), worker_replacement_irony (built the tech that replaced them) |

| **Regulatory Favoritism** | Frames government oversight as politically motivated selection of industry winners, implying arbitrary or self-interested intervention rather than neutral regulation | "picking winners and losers"; "favorable/preferential treatment"; "tilting the playing field"; "government is picking customers/partners" | NYT Meta AI government review holdout (Jun 2026) — "Critics have raised concerns that the emerging framework allows the government to pick winners and losers in the AI industry"; Sam Altman: "I don't like the idea of the government picking the customers" |
| **Escalation Amplification** | Intensifying modifiers ("escalating," "increasingly," "growing," "deepening") preceding threat/concern language, creating editorial momentum beyond what sourced facts support | "escalating [concerns/threats/tensions]"; "increasingly [concerned/hostile/wary]"; "growing [alarm/suspicion/backlash/frustration]" | NYT Meta AI government review holdout (Jun 2026) — "escalating national security concerns about the power of frontier AI systems" |
| **Commodification Metaphor** | Language that flattens human identity, work, or relationships into interchangeable modules, tokens, data points, or raw material — making humans sound like inputs to a system rather than people. Distinct from worker_replacement_irony (which emphasizes the recursive irony of building one's own replacement) because commodification_metaphor focuses on the dehumanizing language itself | "distill/extract/flatten [colleagues/workers] into [skills/modules/tokens]"; "reducing a person to a [skill/task]"; "a cold farewell can be turned into warm tokens"; "digital [human/worker/employee]" | MIT Tech Review Chinese tech workers article (Apr 2026) — "distill their colleagues' skills and personality traits," "flattened into modules in a way that made the worker easier to replace," "a cold farewell can be turned into warm tokens." Also: Nvidia "digital humans," corporate "digital twin" euphemisms |
| **Analogy/Metaphor** | Explicit comparisons using "like", "akin to", "equivalent of" etc. that frame the subject through analogy. The editorial choice of analogy imports associations from the comparison domain. Distinct from analogy_stacking (which requires 3+ analogies) and commodification_metaphor (which specifically dehumanizes) | "like crash-testing a car"; "akin to grading homework"; "as if the platform were a public utility"; "tantamount to" | NYT child safety study (Jun 2026) — "like crash-testing" frames platform safety in automotive regulatory language. Imports expectations of mandatory testing and manufacturer liability |
| **Anthropomorphization** | Ascribing human emotions, intentions, cognition, or social roles to AI systems, algorithms, or software tools — framing engineered artifacts as autonomous agents with inner lives, converting design flaws into character traits and engineering gaps into pedagogical failures | Emotional-adverb ascription ("happily handed," "eagerly processed"), cognitive/volitional verbs ("the AI decided," "the bot chose"), learning/teaching ascription ("without being taught how to"), intentional-excess ("took that brief too seriously," "got carried away"), state-of-mind ("the confused bot," "a bewildered AI"), human role-casting ("digital employee," "AI colleague," "virtual teammate") | Malwarebytes Meta AI support bot article (Jun 2026) — "happily handed Instagram accounts to hackers," "took that brief a little too seriously," "the confused bot," "without being taught how to verify" — sustained personification casts a missing identity-verification check as a character flaw in a naive agent rather than an engineering omission. Distinct from commodification_metaphor (which dehumanizes people) and pathologizing_metaphor (which maps clinical domains onto institutions) |
| **Taxonomy Framing** | Presenting findings using a structured classification system that implies completeness and authority. The editorial choice to organize evidence into named categories ("broken, buried, or missing") creates a framework that constrains interpretation | "broken, buried, or missing"; "classified as [N] categories"; three-part comma-separated adjective taxonomy | NYT child safety study (Jun 2026) — "broken, buried, or missing" taxonomy covers all failure modes, implying comprehensive evaluation and leaving no escape route for the subject |
| **Failure Precedent** | Editorial device that invokes a prior failed attempt at the same type of project to frame a current effort as likely to fail. More effective than direct criticism because the reader draws the analogy themselves. The predecessor's failure casts implicit doubt on the current effort without the journalist stating it | "was set to receive $X ... ultimately cancelled"; "after [entity] lost/failed/fumbled"; "the previous [effort] ... didn't prove viable" | MIT Tech Review Anduril/Meta warfare glasses (May 2026) — Microsoft "was set to receive a $22 billion production contract that was ultimately cancelled when the glasses didn't prove viable," placed directly before describing Anduril's prototype timeline |
| **Industry Normalization Undercut** | Acknowledges that a practice is industry-wide ("other companies also…"), then immediately undercuts the normalization to single out the target ("but Meta's reliance is especially…"). The rhetorical move concedes fairness while negating it in the same breath, making the singling-out appear more objective because the writer "acknowledged" the broader context first | "Other companies also X, but [Target] is especially/far worse/uniquely"; "is not unique to [Target], but"; "industry-wide practice, but the scale at [Target]" | Wired Meta Cannes contractors/teens article (Jul 2026) — practice acknowledged as industry-wide before pivoting to single out Meta's scale and approach as distinctly problematic |
| **Assumed Consensus** | Presents a contested or unsupported claim as self-evident common knowledge, skipping the burden of proof. Constructions like "People hate X", "Everyone knows X", "Nobody wants X" position the audience as already agreeing with the author's stance before any evidence is offered | "People hate/love/want"; "Everyone knows/agrees"; "Nobody wants/trusts"; "It's well known that"; "Goes without saying"; "Needless to say" | Gizmodo Meta glasses subscription article (Jul 2026) — "People hate Meta's smart glasses for quite a few reasons" presents consumer hatred as self-evident fact with zero citation or evidence. Distinct from loaded_language (pejorative vocabulary) and emotional_appeal (sympathy/outrage deployment) |
| **Editorial Aside** | Breaking journalistic register to address the reader directly with sarcastic or solidarity-building interjections that create an in-group frame between author and reader, positioning the subject as an outsider deserving scrutiny | "brace yourself"; "buckle up"; "spoiler alert"; "let's be honest"; "let's face it"; "something tells me"; "call me skeptical"; "(yes, really)"; "(sigh)" | Gizmodo Meta glasses subscription article (Jul 2026) — "brace yourself" and "something tells me" break the journalistic register to editorialize via direct reader address. Distinct from loaded_language (vocabulary choice) and rhetorical_question (interrogative form) |

#### Structural Devices (Post-Pass)

These devices are detected through structural analysis of the article rather than simple pattern matching, and are injected in a post-processing pass.

| Device | Description | Detection Method |
|---|---|---|
| **Kicker Framing** | Ending an article on a discordant negative note unrelated to the article's main topic | Scans the final ~400 characters for negative signals (morale crisis, regulatory threat, ethical concern) when the body tone is neutral-to-positive. Ensures the reader's final impression is negative regardless of otherwise balanced coverage. |
| **Analogy Stacking** | Using 3+ distinct analogies/comparisons for the same subject to amplify perceived severity | Collects analogy markers ("the equivalent of," "likened it to," "compared it to," "like a/an") across the full text. Fires only when 3+ distinct markers are found. Individual analogies are not framing; stacking them is a persuasion technique. |
| **Speculative Framing** | Deploying cumulative conditional language to construct a narrative of inevitability while maintaining individual hedges | Collects speculative hedges ("could potentially," "might be able to," "in principle," "could feasibly," "could conceivably") across the full text. Fires only when 5+ distinct speculative markers are found. A single hedge is good journalism; 10+ hedges in one article is a framing technique that converts possibility into implied certainty. |
| **Trend Bundling** | Grouping a target company's action with 3+ other companies doing similar things to normalise or amplify the narrative | Scans for transition phrases ("Other companies have also…," "Similarly, X…," "X also walked back…") and paragraph-level company bundles. Fires only when 3+ distinct companies are mentioned in comparison/bundling contexts. Individual comparisons are normal reporting; stacking them is an editorial framing technique that imports an industry-wide pattern onto a single company's story. Discovered from Fast Company Meta AI draft reversal article (2026-06-25). |
| **Social Proof Amplification** | Citing reaction counts (likes, thumbs-up, hearts, upvotes) to convert an individual opinion into collective sentiment, lending democratic authority to editorial framing | Detects patterns like "received X likes/upvotes," "garnered X reactions," "thousands liked/shared/retweeted," "went viral with X comments." Fires when numeric reaction counts are cited to amplify the perceived weight of a statement or sentiment. Individual quotes are opinions; citing their virality is a framing technique that manufactures consensus. |
| **Delayed Defense** | The target company's first response or rebuttal appears in the last 35% of the article, after the reader has absorbed the accusatory framing without counter-narrative. Burying the defense is a well-known editorial technique: most readers form their opinion before reaching the other side | Finds the earliest corporate-response pattern (company/spokesperson said, in a statement, declined to comment) and checks if it appears after the 65% mark of the article text. Requires minimum 500 characters (short articles lack meaningful positional structure). |

### 4.2 Attribution Verb Analysis

The choice of attribution verb signals editorial stance:

| Category | Verbs | Signal |
|---|---|---|
| **Neutral** | said, told, noted, explained, stated, added, commented | Professional reporting |
| **Undermining** | claimed, argued, insisted, maintained, contended | Implies doubt |
| **Concessive** | admitted, conceded, acknowledged | Implies wrongdoing |
| **Adversarial** | warned, blasted, slammed, attacked, fired back | Implies conflict |

## 5. Source Authority Analysis

### 5.1 Source Grading

| Grade | Type | Examples |
|---|---|---|
| **Primary** | Original documents, filings, records | SEC filings, court records, .gov databases, official statements |
| **Secondary** | Professional reporting by credible outlets | Reuters, AP, WSJ, NYT, Bloomberg, FT |
| **Tertiary** | Opinion, analysis, social media | Blogs, Substack, Twitter/X posts, opinion sections |

### 5.2 Anonymous Source Scoring

Anonymous sources are not inherently problematic, but their ratio affects reliability:

| Ratio | Assessment |
|---|---|
| < 20% | Normal — most sources identified |
| 20–40% | Elevated — significant anonymous sourcing |
| 40–60% | High — majority claims rest on anonymous sources |
| > 60% | Extreme — article is substantially unverifiable |

#### Counted Anonymous Source Patterns

Standard anonymous-source detection catches phrases like "sources say" and "people familiar with the matter." A harder pattern to detect is **counted anonymous sourcing**: phrases like "two employees said," "three people familiar with," "one person close to." These are anonymous sources disguised as specificity — the count creates an illusion of transparency without revealing identity.

MediaScope's `count_anonymous_sources()` delegates to the comprehensive `extract_sources()` function, which uses role-descriptor patterns, reverse-order attribution, and structural heuristics to catch counted anonymous patterns. This addresses a blind spot discovered in the NYT Meta "Arena" prediction markets article, where 100% of sourcing was anonymous via counted patterns but the original regex-only counter reported 0%.

#### No-Comment Signal Exclusion

"Declined to comment" and similar no-comment signals (e.g., "did not respond to a request for comment," "could not be reached for comment") are tagged as `source_type="no_comment"` and **excluded** from both anonymous and named source counts. These are editorial signals — they communicate that the journalist attempted to contact the entity — but they are not source attributions and should not inflate the anonymous source ratio.

## 6. Source Stance Analysis

### 6.1 Beyond Authority: Who Sources Are Deployed Against

Source authority analysis (§5) answers: "How credible are these sources?"  Source *stance* analysis answers a different question: "Whose side are these sources on?"

An article can score perfectly on source authority (all named, all expert-credentialed, all with direct quotes) while deploying every single source to undermine the subject entity.  This is the editorial technique of adversarial source deployment — assembling a one-sided roster of critics, whistleblowers, and advocacy organizations, each individually credible, to construct a unanimously negative framing.

### 6.2 Stance Classification

For each extracted source, stance is determined by:

1. **Quote content analysis:** The source's quoted text is scanned for negative stance terms (harmful, reckless, censorship, exploitation, etc.) and positive stance terms (innovative, beneficial, safe, transparent, etc.).

2. **Attribution verb weighting:** Adversarial verbs (warned, blasted, accused, fumed, threatened) contribute +1 to the negative stance count, further distinguishing editorial intent.

3. **Classification:** If negative indicators > positive indicators → adversarial.  If positive > negative → supportive.  Otherwise → neutral.

### 6.3 Stance Balance Metric

```
stance_balance = (supportive_count − adversarial_count) / (supportive_count + adversarial_count)
```

| Score | Interpretation |
|---|---|
| −1.0 | All sources positioned against the subject |
| −0.5 | ~75% adversarial |
| 0.0 | Balanced source deployment |
| +0.5 | ~75% supportive |
| +1.0 | All sources validate/defend the subject |

**Note:** A stance_balance of −1.0 is not inherently bad journalism — it could reflect a genuine consensus among experts.  But combined with undisclosed financial conflicts (e.g., the publication's parent owns a competitor of the subject), it becomes evidence of *editorial selection bias*: the journalist chose only sources that support the preferred frame.

### 6.4 Interaction with Authority Score

The most analytically interesting articles score HIGH on source authority AND LOW (negative) on stance balance:

| Authority | Stance | Interpretation |
|---|---|---|
| High | Balanced | Professional, balanced reporting |
| High | Adversarial | Credible but one-sided sourcing |
| Low | Adversarial | Anonymous pile-on |
| Low | Balanced | Poorly sourced but neutral |

The "High authority + Adversarial stance" combination is the hallmark of sophisticated editorial bias — it looks like rigorous journalism because every source is named and credentialed, but the roster is editorially curated to present only one perspective.

## 7. Outsourced Intensity Detection

### 7.1 The Technique

"Outsourced intensity" is the editorial practice of maintaining measured, professional prose in the journalist's own voice while deploying emotionally charged quotes from sources.  The byline text reads as neutral reporting; the emotional impact comes entirely from the quotes.  This lets the journalist (and publication) maintain plausible objectivity while framing coverage adversarially.

**Note:** Outsourced intensity is analyzed in two complementary ways in MediaScope:
1. **As a framing device** (§4.1, Extended Devices): pattern-based detection of specific instances where legal filings, complaints, or whistleblower allegations carry loaded emotional language while the journalist's prose remains neutral. This detects individual occurrences and contributes to framing device counts.
2. **As a quantitative metric** (this section): a ratio measuring the overall balance of emotional language between quoted segments and editorial prose across the full article. This provides a continuous score from 0.0 to 1.0.

Both are valuable: the framing device flags specific outsourcing patterns as evidence, while the ratio quantifies the technique's overall prevalence in an article.

Example from a real article (Guardian, Jun 1 2026):
> The strongest language — "censorship", "despotic", "hostage", "asshole" — all comes from quotes, not the journalist.

### 7.2 Detection Method

MediaScope splits article text into **quoted segments** (text within quotation marks) and **editorial prose** (everything else), then measures emotional language intensity in each:

```
outsourced_ratio = 1 − (editorial_intensity / quoted_intensity)
```

Where `editorial_intensity` and `quoted_intensity` are the standard emotional language density scores (§1.2, dimension 2) applied to each text segment independently.

| Outsourced Ratio | Interpretation |
|---|---|
| 0.0 | No outsourcing — editorial prose is equally or more emotional than quotes |
| 0.3–0.5 | Moderate — some emotional language in both, but quotes carry more |
| 0.5–0.8 | Significant — emotional impact primarily via source quotes |
| 0.8–1.0 | High — virtually all emotional language is in quotes; editorial prose is measured |

### 7.3 Analytical Value

High outsourced intensity is a *red flag* for editorial bias detection because:

1. It defeats lexical sentiment analysis: VADER and TextBlob score the overall text as neutral/positive because the journalist's prose *is* neutral
2. It provides plausible deniability: the journalist can claim to be "just reporting what sources said"
3. It correlates with adversarial source stance: publications that outsource intensity typically also deploy one-sided sources

**Combined signal:** When `outsourced_ratio > 0.5` AND `stance_balance < −0.5`, the article is using the most sophisticated form of editorial bias — credible-looking, measured prose that reads as professional journalism, with the adversarial framing entirely delegated to a one-sided source roster.

## 8. Active-Negative Agency Detection

### 8.1 The Problem

Standard agency attribution (§1.2, dimension 4) distinguishes between entities framed as active/powerful (+1.0) and passive/victim (−1.0). But this misses a critical distinction: **active agency can be negative**. "Meta is tracking users" and "Meta is launching a product" both frame Meta as active, but the editorial valence is opposite. VADER scores both as moderately positive because they use confident, active-voice construction.

### 8.2 Active-Negative Verb Categories

MediaScope maintains a list of verbs and phrases that signal active agency with negative editorial valence:

| Category | Examples |
|---|---|
| **Surveillance/extraction** | "tracking," "surveilling," "monitoring," "harvesting," "capturing," "extracting" |
| **Workforce harm** | "laying off," "slashing," "cutting jobs," "cutting staff," "eliminating positions," "downsizing" |
| **Coercion** | "forcing," "mandating," "compelling," "requiring," "pushing employees," "pressuring employees" |

When these phrases are detected, the agency attribution score is adjusted downward — the entity is active, but the activity is framed as harmful.

### 8.3 Impact on Tone Correction

Active-negative agency feeds into the framing-aware tone correction pipeline (§9). When an article has multiple active-negative agency indicators AND adversarial framing devices, the combination signals editorial stance more reliably than VADER's lexical analysis.

## 9. Framing-Aware Tone Correction

### 9.1 The VADER Positive-Bias Problem

VADER (§1.1) systematically misprices editorial tone in investigative journalism. Professional prose uses measured, confident language that VADER scores as positive. An article stating "Meta is the only major company that has not agreed to voluntary AI safety reviews" scores positive on VADER because the sentence structure is declarative and the vocabulary is neutral. But the editorial stance is clearly adversarial — the framing isolates Meta from peers.

This is not a VADER bug; it is a fundamental limitation of lexical sentiment analysis applied to professional prose. TextBlob has the same blind spot.

### 9.2 Correction Pipeline

MediaScope implements **8 distinct correction paths** (A–H), each addressing a specific VADER/TextBlob failure mode discovered through real article analysis. The paths are evaluated in priority order; the first match fires and returns the corrected score.

The `SentimentResult` preserves both `raw_overall_tone` (uncorrected) and `overall_tone` (corrected) with metadata documenting when and why correction fired.

#### Path A: Full Correction (VADER Got Direction Wrong)

**The primary path.** Fires when VADER scores investigative/adversarial journalism as positive because the prose is lexically measured.

| Trigger | Threshold |
|---|---|
| Raw composite tone | ≥ 0.0 (non-negative) |
| Adversarial framing devices | ≥ 3 (from the adversarial device type set (loaded_language, emotional_appeal, guilt_by_association, catastrophizing, power_asymmetry, isolation_framing, pressure_language, timeline_implication, juxtaposition, refusal_amplification, self_referential_investigation, kicker_framing, hypocrisy_frame, military_techno_optimism, assumed_consensus, editorial_aside)) |
| Agency attribution | < −0.3 (passive/target of scrutiny) |

**Blend:** 10% raw + 90% framing-derived estimate. The framing estimate is computed from agency, emotional intensity, and adversarial device density.

**Discovery article:** NYT "Meta AI Government Review Holdout" (Jun 23, 2026) — VADER scored +0.61 on a piece that framed Meta as the sole holdout among peers refusing voluntary AI safety reviews.

#### Path B: Amplification (VADER Got Direction Right but Understated)

When VADER correctly identifies negative tone but the magnitude is too mild relative to the adversarial framing signal.

| Trigger | Threshold |
|---|---|
| Raw composite tone | < 0.0 and > −0.5 (mildly negative) |
| Adversarial framing devices | ≥ 6 (higher threshold than Path A) |
| Agency attribution | < −0.3 |

**Blend:** 50% raw + 50% framing-derived estimate. Lighter than Path A because VADER got the direction right — only nudging the magnitude.

**Rationale:** A mildly negative VADER score (e.g., −0.12) on a piece with 8 adversarial framing devices and agency of −0.6 understates the editorial stance. Path B amplifies to match the structural signal.

#### Path C: Embedded Adversarial Anchor

Product review articles where the subject has positive agency (actively launching products) but specific anchor devices shift the reader's final impression negative.

| Trigger | Threshold |
|---|---|
| Raw composite tone | > 0.3 (strongly positive) |
| Anchor devices (kicker, self-referential investigation, juxtaposition) | ≥ 2 |
| Overall adversarial count | ≥ 4 |
| Agency attribution | ≥ 0.0 (positive — product review context) |

**Blend:** 55% raw + 45% toward anchor target (0.15). The article IS partly positive, so the correction nudges toward the reader's likely takeaway rather than fully overriding.

**Discovery article:** Wired glasses launch review (Jun 23, 2026) — agency +0.67, raw tone +0.67, but the kicker ("morale at an all-time low"), self-referential investigation ("WIRED discovered code suggesting facial recognition"), and juxtaposition ("consumer smart glasses… surveillance tools for the US military") anchored the reader's final impression at approximately +0.15.

#### Path D: Sardonic/Mocking Framing

Articles where editorial contempt is conveyed through raw word choice rather than structural framing. The subject has positive active agency (someone actively pursuing something) but the pursuit is framed as foolish, futile, or contemptible.

| Trigger | Threshold |
|---|---|
| Raw composite tone | ≥ 0.3 |
| Agency attribution | ≥ 0.3 (positive — key contrast to Path A) |
| Loaded language count | ≥ 7 |
| Overall adversarial count | ≥ 8 |

**Blend:** 10% raw + 90% sardonic-derived estimate. Heavy override because VADER is maximally misled — positive agency words ("looking to start," "booming") combine with positive sentence structure to produce inflated scores while the editorial stance is unambiguously contemptuous.

**Discovery article:** Kotaku Meta Arena article (Jun 28, 2026) — VADER scored +0.68 on a piece manually assessed at −0.55 to −0.65. Loaded language ("ethically rancid," "failed metaverse," "AI slop") accounted for >70% of adversarial devices — the contempt was purely lexical, not structural.

#### Path E: Military Techno-Optimism Inflation

Articles about military/defense technology where aspirational language inflates VADER's reading. Unlike Path A, agency is not strongly negative because the subjects ARE actively building things — the inflation comes from the content domain (warfare, weapons), not from passive framing.

| Trigger | Threshold |
|---|---|
| Raw composite tone | ≥ 0.3 |
| `military_techno_optimism` devices | ≥ 3 |
| Agency attribution | < 0.0 (any negative — relaxed from −0.3) |

**Blend:** 30% raw + 70% framing-derived estimate. Lighter than Path A because these are not pure adversarial pieces — the articles may include genuine technological achievements alongside critical editorial framing.

**Discovery article:** MIT Tech Review Anduril/Meta smart glasses warfare article (May 18, 2026) — VADER scored +0.64 vs manual assessment of −0.10. Agency was −0.2 (too weak for Path A's −0.3 threshold). "Revolutionize the battlefield," "enhanced capabilities" inflated VADER's reading.

#### Path F: Contradictory Review Framing

Product reviews where the reviewer gives a positive assessment (VADER reads product-praise language as strongly positive) but wraps it in negative editorial context about privacy, ethics, or corporate behavior. Positive product language outnumbers negative editorial passages by sheer word count, drowning out the editorial stance.

| Trigger | Threshold |
|---|---|
| Raw composite tone | ≥ 0.3 |
| Overall adversarial count | ≥ 4 |
| Emotional intensity | ≥ 0.5 |
| Agency attribution | −0.4 ≤ agency < 0.0 (mixed: not fully passive) |
| Rhetorical questions OR loaded language | ≥ 1 RQ or ≥ 3 loaded language |

**Blend:** 20% raw + 80% review-derived estimate. The editorial wrapper is the dominant signal — the product praise is genuine but the article's *editorial position* is negative.

**Discovery article:** Gizmodo Meta Fury review (Jun 29, 2026) — VADER scored +0.68 on a manually assessed −0.35 article. Positive product review language dominated the word count, drowning out the negative privacy/ethics editorial wrapper. Rhetorical question in the kicker undermined the positive assessment.

#### Path H: Sarcastic Short Editorial

Short opinion pieces (typically <500 words) where the editorial voice is sarcastic/dismissive but VADER reads neutral-agency active language as positive. The sarcastic register — direct reader address, assumed consensus, editorial asides — is invisible to lexical sentiment.

| Trigger | Threshold |
|---|---|
| Raw tone | ≥ 0.3 (VADER inflated positive) |
| Editorial aside devices | ≥ 2 |
| Adversarial device count | ≥ 4 |
| Emotional language intensity | ≥ 0.5 |
| Agency attribution | ≥ −0.1 (neutral to slightly positive) |

**Blend:** 15% raw + 85% target. Target tone = −(0.30 + 0.20 × sarcasm_density + 0.10 × emotional_intensity), where sarcasm_density = min((editorial_aside_count + assumed_consensus_count) / 5.0, 1.0). Clamped to [−0.7, 0.0].

**Key distinction from Path D (sardonic/mocking):** Path D requires high loaded_language count (≥7) and strongly positive agency (≥0.3) — the subject is actively pursuing something framed as foolish. Path H fires on shorter articles with fewer total devices but concentrated sarcastic indicators (editorial_aside, assumed_consensus) and neutral agency (the subject is doing things, but the editorial register signals disapproval through sarcasm rather than loaded vocabulary).

**Discovery article:** Gizmodo Meta glasses subscription article (Jul 1, 2026) — VADER scored +0.65 on a clearly negative article with "People hate" (assumed consensus), "brace yourself", "let's be honest", "something tells me" (editorial asides), and "hate", "grievances", "slapping", "paywall" (emotional language). Agency = 0.0.

#### Path G: VADER Long-Text Normalization

Not a framing correction — this fixes a fundamental VADER math problem. VADER's compound score uses `sum / sqrt(sum² + alpha)` where `alpha=15`, tuned for tweet-length texts. For long articles (10+ sentences), this normalization amplifies small biases.

| Trigger | Threshold |
|---|---|
| Article length | ≥ 10 sentences |
| Full-text compound | \|compound\| > 0.5 (strong signal) |
| Sentence-level mean | \|mean\| < 0.05 (near-zero) or opposite sign from compound |
| Divergence | \|compound − sentence_mean\| > 0.5 |

**Blend:** 70% sentence-level mean + 30% full-text compound.

**Key constraint:** Only fires when VADER's *direction* is wrong (compound and sentence-level mean disagree on sign, or sentence-level is near zero). When both agree on direction, VADER's reading is preserved even if it exaggerates magnitude.

**Mechanism:** Business-neutral vocabulary like "risk," "pressure," "problem" in otherwise neutral context can push full-text compound to −0.85 when the actual sentence-level sentiment is balanced around 0. The sentence-level mean, immune to the alpha normalization, provides the corrective signal.

#### Path Evaluation Order and Priority

The paths are evaluated in code order: **A → B → C → E → D → F → H**. Path G runs independently in the `analyze_composite` function before the framing correction pipeline, as it corrects VADER's input signal rather than overriding the composite output.

**Only one framing path fires per article.** If Path A matches, Paths B–H are never evaluated. This prevents over-correction and ensures the strongest applicable correction takes precedence.

#### Summary Table

| Path | Failure Mode | Raw Tone | Agency | Key Signal | Blend |
|---|---|---|---|---|---|
| **A** | VADER wrong direction | ≥ 0.0 | < −0.3 | ≥3 adversarial devices | 10/90 (raw/framing) |
| **B** | VADER understated | (−0.5, 0.0) | < −0.3 | ≥6 adversarial devices | 50/50 |
| **C** | Anchor devices | > 0.3 | ≥ 0.0 | ≥2 anchor + ≥4 adversarial | 55/45 (raw/target) |
| **D** | Sardonic contempt | ≥ 0.3 | ≥ 0.3 | ≥7 loaded + ≥8 adversarial | 10/90 (raw/sardonic) |
| **E** | Military optimism | ≥ 0.3 | < 0.0 | ≥3 MTO devices | 30/70 (raw/framing) |
| **F** | Contradictory review | ≥ 0.3 | [−0.4, 0.0) | ≥4 adversarial + ≥0.5 EI | 20/80 (raw/review) |
| **G** | Long-text normalization | any | any | divergence > 0.5, ≥10 sentences | 30/70 (compound/sentence) |
| **H** | Sarcastic editorial | ≥ 0.3 | ≥ −0.1 | ≥2 editorial_aside + ≥4 adversarial + ≥0.5 EI | 15/85 (raw/target) |

### 9.3 Headline Framing Override

A secondary correction addresses headline-body alignment (§1.2, dimension 5). When VADER reads a headline as positive but it contains loaded editorial signals (surveillance terms, deletion/removal language, "after report"/"after investigation" constructions, "under fire"/"backlash"), the headline compound score is overridden to negative. This prevents headlines like "Meta Deletes Face-Recognition System After WIRED Report" from scoring as positive.

### 9.4 Security Context Adjustment

Technical security/hacking articles use domain-specific language ("exploit," "vulnerability," "breach," "attack") that inflates emotional intensity scores. When an article matches security topic patterns, the emotional intensity scorer reduces its score to avoid false-positive alarmism signals.

## 10. Quality Control

### 10.1 MediaScope's Own Output Standards

All reports generated by MediaScope must pass internal quality checks:

1. **Citation density**: ≥1 verifiable source per factual claim
2. **AI slop detection**: Zero tolerance for banned phrases (see `quality/standards.py`)
3. **Counterargument**: Every analysis must include the strongest counterargument
4. **Limitations**: Every report must state what it cannot prove
5. **Methodology transparency**: Every report links to this document

### 10.2 Article Quality Scoring

When evaluating articles from target publications, MediaScope applies a quality score based on:
- Source diversity and authority
- Attribution verb neutrality
- Anonymous source ratio
- Speculative language ratio
- Headline-body alignment
- Counterargument presence

## 11. Limitations

### What MediaScope Can Do
- Measure coverage sentiment asymmetry with statistical rigor
- Map ownership and financial conflicts of interest
- Detect framing devices and source authority patterns
- Generate verifiable disclosure statements

### What MediaScope Cannot Do
- **Prove causation.** An asymmetry score correlated with a financial conflict does not prove the conflict caused the bias.
- **Read editorial intent.** We measure outcomes (published text), not motivations.
- **Account for all confounds.** Genuine differences in company behavior (e.g., one company has more scandals) will affect scores.
- **Replace human judgment.** Statistical significance is necessary but not sufficient. Domain expertise is required to interpret results.

### Known Biases in the Tool Itself
- Keyword-based entity detection may miss oblique references
- Sentiment models have known biases toward certain writing styles
- English-language only in current version
- RSS feeds may not capture all articles (paywalled content, newsletters)

## 12. References

1. Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum.
2. Hutto, C.J. & Gilbert, E.E. (2014). "VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text." *ICWSM*.
3. Spinde, T., et al. (2022). "BABE: A Benchmark for Annotated Media Bias Detection." In *Findings of ACL 2022*.
4. Raza, S., et al. (2025). "Media Bias Detector: Automated Detection of Bias in News Articles." *CHI 2025*.
5. Bunz, M. & Braghieri, L. (2021). AI coverage sentiment analysis. Referenced in Stanford HAI AI Index.
6. Welch, B.L. (1947). "The generalization of 'Student's' problem when several different population variances are involved." *Biometrika*, 34(1-2), 28-35.
7. Gentzkow, M. & Shapiro, J.M. (2010). "What Drives Media Slant? Evidence from U.S. Daily Newspapers." *Econometrica*, 78(1), 35-71.
8. Hamborg, F., et al. (2019). "Automated identification of media bias in news articles: an interdisciplinary literature review." *International Journal on Digital Libraries*, 20, 391-415.

---

## 13. Cross-Publication Same-Event Comparison

### 13.1 The Method

The most powerful evidence for editorial framing bias comes from comparing how different publications cover **the same event on the same day**. When two journalists attend the same press conference, read the same press release, or report on the same court filing, the raw facts are held constant — any difference in tone, framing device density, source selection, or structural choices is attributable to editorial DNA rather than event severity.

This is the media analysis equivalent of a controlled experiment: the "treatment" is the publication's editorial culture and financial incentive structure, and the "outcome" is the framing of identical facts.

### 13.2 Comparison Dimensions

For each same-event pair, MediaScope compares:

| Dimension | What to Measure | Why It Matters |
|---|---|---|
| **Word count** | Total article length | Editorial investment — longer = more resources allocated |
| **Tone score** | 8-dimension sentiment (§1) | Raw editorial stance toward the entity |
| **Framing device count** | Total devices from the 53-type taxonomy (§4) | Framing density — how many editorial techniques are deployed |
| **Framing device types** | Which specific devices appear | Editorial technique fingerprint — reveals preferred persuasion patterns |
| **Source roster** | Named vs anonymous, count, affiliations | Who the journalist chose to quote |
| **Source stance balance** | Adversarial vs supportive vs neutral (§6) | Whether sources are deployed one-directionally |
| **Outsourced intensity** | Editorial prose intensity vs quoted intensity (§7) | Who carries the emotional weight — journalist or sources |
| **Structural choices** | Headline framing, kicker, paragraph ordering | How information is architecturally arranged |

### 13.3 Wire-Service Baseline

Wire services (Reuters, AP) serve as the analytical baseline. Their editorial mandate is factual neutrality — no commentary, minimal framing, rapid dissemination. When a wire service and a magazine cover the same event:

- **Wire-service tone ≈ event severity.** If Reuters scores an event at −0.15, that's approximately the "neutral" reading of the facts.
- **Magazine tone − wire-service tone ≈ editorial framing contribution.** If Wired scores the same event at −0.65, the −0.50 gap is attributable to editorial choices, not the facts themselves.
- **Framing device differential.** Reuters typically deploys 0-1 framing devices on a given story. If Wired deploys 7+ on the same story, those 6+ additional devices are editorial signal.

### 13.4 Validated Examples

MediaScope's sample output gallery includes three same-event comparisons that demonstrate the method:

| Event | Publications | Tone Gap | Framing Gap | Key Finding |
|---|---|---|---|---|
| MCI data exposure (Jun 22, 2026) | Wired (−0.60) vs Reuters (−0.10) | −0.50 | 7 vs 1 | Wired: vindication narrative, CEO personalization, kicker framing. Reuters: factual, one mild corporate reassurance undercut. Same facts, radically different framing density. |
| Meta glasses launch (Jun 23, 2026) | Wired (−0.15) vs Gizmodo (+0.10) | −0.25 | 10 vs 0 | Wired: surveillance-consumer juxtaposition, self-referential investigation ×2, kicker framing (unrelated morale crisis). Gizmodo: neutral product-first structure, privacy raised as business question not moral failing. Same press event, same Bosworth Q&A. |
| Meta "Arena" prediction markets (Jun 23, 2026) | Reuters (+0.05) vs Engadget (−0.70) | −0.75 | — | Same-day scoop: Reuters treated as neutral business news, Engadget deployed heavy adversarial framing. Demonstrates how publication DNA transforms identical news items. |

### 13.5 Analytical Value

Same-event comparisons are more persuasive than aggregate asymmetry scores because they control for the most important confound: **event severity**. A critic can always argue that a publication's negative aggregate tone reflects genuine corporate wrongdoing. But when two publications cover the identical event with a 0.50-point tone gap and a 6x framing device differential, the editorial framing contribution is directly observable.

These comparisons also reveal **publication-specific framing fingerprints**. Wired's characteristic patterns include:
- Self-referential investigation (citing its own prior exposés as evidence)
- Kicker framing (ending product reviews with unrelated workforce morale crises)
- Surveillance-consumer juxtaposition (linking consumer products to military applications)

These patterns are invisible in aggregate scores but become unmistakable in side-by-side comparison.

### 13.6 Limitations

- **Selection bias in article pairs.** Not every event gets covered by multiple publications, and the events that do (major launches, scandals) may not be representative.
- **Genre differences.** Wire services write breaking news; magazines write features. Some framing differences reflect genre conventions, not editorial bias.
- **Timing.** Same-day coverage may differ because one outlet had more time (later publication) or more access (exclusive sources).
- **Byline variation.** Different journalists within the same publication may cover the same event differently. The comparison measures publication-level editorial culture but may conflate it with individual journalist style.

---

## 14. Causal Identification Through Journalist Migration Analysis

*This section documents MediaScope's novel methodological contribution. For the full treatment, see [EDITORIAL_HISTORIES.md](EDITORIAL_HISTORIES.md).*

### 14.1 The Problem of Causal Attribution

Standard sentiment asymmetry analysis (§§1-3) measures *that* coverage is asymmetric, but cannot identify *why*. An asymmetry score tells us Wired covers Meta 0.28 points more negatively than peers — it cannot distinguish:

- **Institutional bias** — Advance Publications' 65.2% Reddit voting power creates financial incentive for anti-Meta coverage, and editorial culture enforces it regardless of who writes
- **Individual bias** — specific journalists carry adversarial stances toward certain companies
- **Interaction effects** — certain journalist × publication pairings amplify bias beyond what either would produce alone

MediaScope's Editorial Histories module provides causal identification by exploiting journalist migrations as natural experiments.

### 14.2 Difference-in-Differences (DiD) Framework

We adapt the canonical DiD estimator from labor economics (Card & Krueger, 1994):

**Setup:** Journalist J departs Publication A at time *t* for Publication B.

**Treatment group:** Publication A (experienced the personnel change)
**Control group:** Publication C (no personnel change in the same window)

**Model:**
```
Y_ij = β₀ + β₁·Treatment_i + β₂·Post_j + β₃·(Treatment_i × Post_j) + ε_ij
```

| Parameter | Interpretation |
|---|---|
| β₀ | Baseline tone at control publication, pre-migration |
| β₁ | Structural difference between treatment and control pubs |
| β₂ | Secular trend in coverage tone (e.g., from news events) |
| **β₃** | **The causal effect of the journalist's departure on coverage tone** |

**Key assumption: Parallel trends.** In the absence of the journalist's departure, Publication A and Publication C would have followed the same tone trajectory. This is untestable but can be assessed visually by checking pre-migration trend similarity.

**Standard errors** are computed from the OLS DiD regression with Huber-White robust variance estimation.

### 14.3 Portable Bias Score

For journalists who have worked at ≥2 tracked publications, we measure how much of their coverage tone is *portable* (carried from outlet to outlet) versus *adaptive* (shaped by each outlet's culture):

```
Portable_Bias = 1 − |Cohen's d(tone_pub_A, tone_pub_B)| / 2
```

| Score | Interpretation |
|---|---|
| 0.0 | Fully adaptive — tone matches each publication's norms |
| 0.5 | Mixed — some portable, some adaptive |
| 1.0 | Fully portable — identical tone regardless of outlet |

Example: If Kara Swisher's average tone toward Meta is −0.45 at Recode, −0.42 at NYT, and −0.40 at WSJ, while the publication baselines are −0.10, −0.15, and +0.05 respectively, her portable bias score would be high (she carries her stance everywhere).

### 14.4 Bias Decomposition (Two-Way ANOVA)

For journalists with multi-publication coverage, total tone variance is decomposed:

```
SS_total = SS_institutional + SS_individual + SS_interaction

Institutional = SS_pub_baseline / SS_total
Individual = SS_journalist_deviation / SS_total
Interaction = SS_residual / SS_total
```

Where:
- SS_pub_baseline = Σ nⱼ × (publication_baseline_j − grand_mean)²
- SS_journalist_deviation = Σ nⱼ × (journalist_mean_at_j − publication_baseline_j)²
- SS_residual = SS_total − SS_pub − SS_journalist

### 14.5 Interrupted Time-Series for Leadership Changes

Editorial leadership changes (new EIC, managing editor) are analysed with segmented regression:

```
Y_t = β₀ + β₁·T + β₂·D_t + β₃·(D_t × T_post) + ε_t
```

| Parameter | Interpretation |
|---|---|
| β₁ | Pre-change monthly trend |
| **β₂** | **Immediate level shift when new leader takes over** |
| **β₃** | **Change in monthly trend under new leadership** |
| β₁ + β₃ | Post-change monthly trend |

### 14.6 Academic Novelty

To our knowledge, **no prior work applies difference-in-differences methodology to journalist-level editorial migration data** to decompose media bias into institutional and individual components. The closest related literature:

| Paper | What They Did | How We Extend |
|---|---|---|
| Gentzkow & Shapiro (2010) | Decomposed newspaper slant into demand/supply components | We decompose at journalist level, not publication level |
| Groseclose & Milyo (2005) | Measured bias via think-tank citation patterns | We use NLP tone scoring instead of manual citation coding |
| Puglisi & Snyder (2011) | Studied partisan coverage of political scandals | We exploit personnel changes as natural experiments |
| Card & Krueger (1994) | Established DiD for minimum wage/employment | We adapt their framework from labor economics to media analysis |

### 14.7 Additional References

9. Card, D. & Krueger, A.B. (1994). "Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania." *American Economic Review*, 84(4), 772-793.
10. Groseclose, T. & Milyo, J. (2005). "A Measure of Media Bias." *Quarterly Journal of Economics*, 120(4), 1191-1237.
11. Puglisi, R. & Snyder, J.M. (2011). "Newspaper Coverage of Political Scandals." *Journal of Politics*, 73(3), 931-950.
12. Martin, G.J. & Yurukoglu, A. (2017). "Bias in Cable News: Persuasion and Polarization." *American Economic Review*, 107(9), 2565-2599.
13. Angrist, J.D. & Pischke, J.-S. (2009). *Mostly Harmless Econometrics*. Princeton University Press.
