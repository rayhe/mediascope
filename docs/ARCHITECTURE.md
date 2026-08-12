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

The toolkit uses a multi-layer correction pipeline with **13 distinct paths (A–N)** that addresses known VADER/TextBlob blind spots when scoring editorial prose:

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
                                 (113 device types, 782 compiled regex)
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
           ┌────────┬──────────┬────┼────┬──────────┬──────────┐
           ▼        ▼          ▼    ▼    ▼          ▼          ▼
        Path A   Path B    Path C  Path E  Path D  Path F  Path H  Path I  Path J  Path K  Path L  Path N
        Full     Amplify   Anchor  Mil.   Sardonic Contra- Sarcastic Consumer Expert Sarcastic Quote-
        correct  understat embed   techno mocking  dictory editorial critique struct. rejection inflated
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
| **I** | Direct consumer critique with positive agency | raw ≥ 0.3, agency > 0, ≥5 adv. + ≥2 consumer devices, EI ≥ 0.5 | 20% raw / 80% target |
| **J** | Expert-driven structural critique | raw ≥ 0.3, agency ≥ 0, ≥5 adv. + ≥1 expert_contradiction, EI ≥ 0.10 | 30% raw / 70% target |
| **K** | Sarcastic rejection editorial | raw ≥ 0.3, ≥2 sarcastic_correction, EI ≥ 0.7 | 10% raw / 90% target |
| **L** | Quote-inflated body + negative headline | raw ≥ 0.3, headline_body ≤ -0.5, adversarial ≥ 4, ≥3 distinct types | Mild negative (-0.05 to -0.50) |

Only one framing path (A–F, H–N) fires per article. Path G runs independently before the composite is computed, correcting VADER's input signal. See [METHODOLOGY.md §9.2](METHODOLOGY.md#92-correction-pipeline) for full trigger conditions, blend formulas, and discovery articles.

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
- **113 framing device types** organized in three tiers:
  - **Core (10):** guilt by association, anonymous authority, catastrophizing, false balance, selective omission signal, emotional appeal, loaded language (including workplace coercion/revolt terms), power asymmetry, CEO personalization, litigation framing
  - **Extended (96):** straw man, refusal amplification, juxtaposition (including investment-near-layoffs), timeline implication, military techno-optimism, selective rehabilitation, rhetorical question, ironic quotation, isolation framing, pressure language, self-referential investigation (publication citing its own prior reporting as evidence within adversarial coverage), geopolitical regulatory pressure, sovereignty framing, scale/magnitude framing, corporate reassurance undercut, hypocrisy frame (singling out an entity as the sole holdout among peers, framing inaction as moral failing), sarcastic correction (editorial sarcasm that mockingly concedes a point before retracting it), outsourced intensity (loaded language in legal filings/complaints quoted by neutral editorial prose), precedent analogy (editorial device importing settled villainy from prior crises — opioid, tobacco, asbestos — onto a current subject via era-based comparisons), confession framing (editorial device presenting corporate acknowledgments as forced admissions — "admitted," "conceded," "finally acknowledged" — reframing voluntary statements as reluctant confessions extracted under pressure), latecomer narrative (editorial device framing a company as entering a space after competitors, positioning it as playing catch-up — "exploring partnerships with," "joining the race," "playing catch-up" — rather than innovating independently), regulatory shadow (ambient technique of inserting regulatory/legal context into product or business stories where it is tangential), editorial deflation (editorial technique of building up an ambitious vision then puncturing it with a brief dismissive phrase — "That's the idea, anyway," "or so X claims," "if it ever actually works" — implying failure without explicit argument), denial contradiction (source's direct denial or minimization placed alongside contradicting evidence — "does not exist" near code analysis findings, combative "misleading"/"dishonest" pushback followed by removal evidence, soft "part of a pilot" editorially undercut), analogy/metaphor (explicit comparisons using "like," "akin to," "equivalent of" that import associations from a comparison domain — distinct from analogy_stacking which requires 3+), taxonomy framing (presenting findings using a structured classification system that implies completeness and authority — "broken, buried, or missing" leaves no escape route), failure precedent (invoking a prior failed attempt at the same project type to cast implicit doubt on the current effort — "was set to receive $X ... ultimately cancelled"), worker replacement irony (workers who built/trained the AI that now replaces them), two-tier treatment (contrasting treatment of full-time vs. contractor workers), regulatory favoritism (government oversight framed as picking winners and losers), escalation amplification (intensifying modifiers before threat/concern language), commodification metaphor (language flattening human identity/work into interchangeable modules, tokens, or data), pathologizing metaphor (addiction, disease, or bodily-excess language applied to corporate/institutional behavior — "addicted to," "gorge itself," "high-rollers" — framing strategy as compulsion), anthropomorphization (ascribing human emotions, intentions, cognition, or social roles to AI systems — "happily handed," "the confused bot," "without being taught how to" — converting design flaws into character traits), industry normalization undercut (acknowledging a practice is industry-wide then undercutting it to single out the target — "Other companies also X, but Meta's reliance is especially…"), assumed consensus (presenting a contested or unsupported claim as self-evident common knowledge — "People hate X," "Everyone knows," "Nobody wants" — skipping the burden of proof), editorial aside (breaking journalistic register to address the reader directly with sarcastic or solidarity-building interjections — "brace yourself," "let's be honest," "something tells me"), slippery slope (extrapolating from a specific action to a broader systemic threat via precedent-setting language — "sets an uncomfortable precedent," "If this approach extends," "could end up paying" — common in consumer-tech restriction/DRM coverage), consumer ownership (framing corporate restrictions as violating what consumers "already paid for" — "hardware you've already paid for," "runs entirely on the device" near "subscription/fee" — invoking property-rights intuitions), usage dismissal undercut (corporate minimization of a restriction's impact by citing low average usage — "most users don't use it for three hours" — as reassurance the journalist then challenges), financial reassurance (financial journalism device where negative operational news is immediately reframed as positive market/investor signal — "could soothe concerns," "easing fears," "investors shrugged off" — the journalist's own reassurance, not quoted corporate PR), cross-publication import (importing another outlet's characterization as settled fact — "several reports have depicted," "widely described as," "what critics have called" — laundering contested framing into consensus), competitive positioning (explicitly elevating a competitor over the subject entity — "good news for [competitor]," "buy from a more reputable company," "[competitor] has always/would never" — positioning a rival as the beneficiary of the subject's failure), heritage nostalgia (age, generational continuity, or historical significance establishing emotional stakes — "141-year-old manufacturer," "fifth generation working at the company," "iconic buildings" — creating implicit argument that what is at risk has deep, irreplaceable value), historical legitimation (insertion of temporally distant positive data to structurally dilute fresh negative news — old earnings beats or revenue growth recapped in negative-news articles), marginal endorsement (analyst action of negligible magnitude presented as meaningful bullish signal — price target raises of <1% or rating reiterations framed as substantive conviction), competitive deficit (enumerating multiple named competitors to amplify the subject's failure — "failed to launch a rival to [A]'s X, [B]'s Y, and [C]'s Z" — pile-on effect of being surrounded and outpaced), competitive displacement (framing one entity's action as filling a vacuum left by another's retreat or strategic pivot — "at a time when [Entity] may be reorienting," "filling the void left by" — positions subject as losing ground while competitor capitalizes), policy reversal (framing change of position as flip-flop or U-turn — "reversed course," "backtracked," "walked back" — implying inconsistency rather than evolution), absence as evidence (framing non-action or omission as proof of guilt — "the audit that never happened," "has never disclosed," "failed to act" — converting non-events into indictments), silence as guilt (explicitly treating silence or non-response as confession — "That silence is its own answer," "the lack of denial speaks volumes" — asserting silence proves something), talent hemorrhage (cataloging multiple departures to competitors in sequence — "left for [Company]... recently left... is also leaving" — building cumulative exodus narrative), strategic reversal (company reversing a core strategic position — "a major departure from longtime philosophy," "chosen to abandon," "start from scratch" — framing change as betrayal of principle), scandal comparison (using a notorious fraud/disaster/scandal name as a compact pejorative label — "AI Theranos," "the Enron of AI" — importing moral weight without explicit argument), repeated disruption (headline or body language implying chronic instability — "shakes up... again," "yet another restructuring," "months of tumult" — framing subject as incapable of settling), expert contradiction (named expert source directly contradicting a company's stated rationale — "It's not about X; it's about Y" inversion — the undercut comes from a credentialed third-party, not the journalist), loss-leader framing (editorial description of selling hardware at cost to capture subscription revenue — "sold at cost," "user base grows, subscription service grows revenue" — reframing consumer pricing as strategic capture), editorial dramatization (interpretive glosses rewriting neutral facts in heightened dramatic language — "unexpected reality check," "massive shakeup," "turbulent transition," "did not mince words," "specifically engineered to" — standalone dramatic set-pieces distinct from escalation_amplification's modifier + threat-noun pairs), precedent framing (signaling event significance through historical rarity — "first in N years," "first since YYYY," "unprecedented [action]" — establishes significance through time-span comparison, distinct from scale_magnitude and precedent_analogy), expert consensus authority (trade publication technique of assembling 3+ named credentialed experts who all reinforce the same editorial thesis — creates illusion of independent validation when all sources converge on the journalist's framing — distinct from anonymous_authority and expert_contradiction), prescriptive solutionism (trade publication technique of transforming accountability or controversy stories into management playbooks via prescriptive bullet lists, "actionable steps," or "key takeaways for IT leaders" — normalizes the underlying behavior by implying it is a solvable governance problem rather than a systemic or ethical issue), strategic disclosure (a party in a dispute strategically discloses an opponent's legal demand, internal figure, or unfavorable position to frame it as extreme or unreasonable — the journalist reports the disclosure but the framing originates with the disclosing party, not editorial choice), valuation comparison (comparing a penalty, cost, or liability amount to a company's market capitalization or total valuation to make the figure feel existentially threatening — "compared to the company's market capitalization, which is just above $1.5 trillion"), narrative reframing (editorial technique of explicitly acknowledging an existing narrative then dismissing it as incomplete or simplistic — "That concern is fair. It is also incomplete," "The lazy version says" — allows the author to redirect reader without refuting facts), dismissive qualifier (using pejorative or dismissive adjectives to characterize a viewpoint before presenting it — "an easy worry," "the lazy version," "a convenient narrative" — subtly delegitimizing the opposing view before engaging with it), bull/bear structuring (investor-media genre pattern organizing analysis into explicit "what would support/break the thesis" sections with enumerated signals — creates appearance of balanced analysis while the structural weight and conclusion can tilt one direction), analyst authority (named analyst firms used as authority sources to frame corporate spending decisions — "BofA warns," "according to Goldman Sachs" — distinct from anonymous_authority in that these are named institutions whose credentialing function shapes the narrative), investor advisory (editorial technique where the author adopts an investment-advisor posture, directly warning investors about risks and prescribing behavior — "Investors ignore [X] at their peril," "should start paying attention," "Investors may be making the wrong choice" — distinct from analyst_authority and bull_bear_structuring in that it addresses the reader as investor), default burden privacy (editorial technique of framing a default-on feature with a standard opt-out as inherently violating user consent — "enabled by default," "opt-out," "users may not know," "without consent" — emphasises the burden on users to discover and toggle settings, treating default-on as quasi-deceptive regardless of opt-out accessibility), editorial cross-promotion (all-caps interstitial headline blocks or CTA blocks embedded in article body text, importing linked headline framing into otherwise balanced reporting — creates plausible deniability where neutral prose coexists with adversarial cross-promo blocks), emotion attribution (editorial attribution of emotional states — disappointment, frustration, alarm — to subjects who expressed only factual observations, upgrading neutral statements into emotional reactions — "is disappointed that," "leading investors to fret"), market verdict (market drops or investor behavior framed as authoritative editorial judgment on corporate strategy — "fell X% as/amid concerns," "investors have spoken," "wiping $X in value"), overbuilding narrative (infrastructure investment framed as inherently excessive, unsustainable, or bubble-like — "spending war," "arms race," "overcapacity," "AI bubble," "when will someone blink," "throwing money at"), litigation cascade (stacking of multiple legal fronts — "N states banded," "N,NNN cases pending," "Another N states filed" — building cumulative existential-threat narrative through enumeration of concurrent legal actions), defensive verb framing (loaded attribution verbs editorializing corporate actions — "attempted yet failed," "was forced to," "grudgingly acknowledged," "scrambled to," "has been plagued by" — converting neutral corporate behavior into narratives of struggle, compulsion, or failure through verb choice alone), regulatory risk subordination (regulatory/legal risk acknowledged but architecturally sandwiched between positive market signals — reading experience begins and ends with optimism — genre-normative for IBD/Investopedia/Motley Fool, higher signal in WSJ/NYT/Bloomberg), recovery narrative (three-beat article architecture: decline → catalyst → recovery projection — common in financial/investor media where prior weakness is acknowledged then reframed through positive catalysts and forward analyst projections), grudging concession (positive action or improvement acknowledged but editorially minimized — \"finally,\" \"only after backlash,\" \"it's about time\" — framing legitimate progress as reluctant, forced, or insufficient), ultimatum framing (multi-stage regulatory/legal proceeding compressed into binary \"do X or face Y\" construction — \"change X — or get/face Y,\" \"must [action] or face [consequence],\" \"comply or face fines\" — collapsing procedural complexity into an \"or else\" fork), recidivism framing (entity framed as serial offender through temporal recurrence markers — \"once again caught,\" \"has a long history of violations,\" \"serial violator,\" \"pattern of\" — constructs a habitual-offender narrative distinct from repeated_disruption's organizational-instability focus), reader positioning (second-person concessive constructions that align the reader with the author's editorial stance before evidence is presented — \"you couldn't be blamed,\" \"you'd be forgiven for thinking,\" \"hard to blame anyone,\" \"you'd be right to worry\" — presupposes agreement rather than earning it, distinct from assumed_consensus and editorial_aside), no-comment implication (publishing a subject's non-response as implicit editorial judgment of evasiveness — \"did not immediately respond,\" \"declined to comment\" — distinct from silence_as_guilt which treats absence of action as confession), competitive guilt transfer (linking a product to a competitor's scandal in the same section, creating guilt by proximity — Meta→Grok→nudify→children→lawsuit inference chain without direct accusation), consent alarm (default-opt-in or automatic enrollment language framing product defaults as consent violation — \"automatically enrolled,\" \"without your knowledge,\" \"use your likeness\" — common in privacy service journalism), editorial character attack (journalist inserts their own characterization of a named person's reputation or moral standing as established fact — \"best known for unethical,\" \"he's the guy for that,\" \"has a long history of exploiting\" — distinct from loaded_language targeting individual words and guilt_by_association linking to separate actors), surveillance creep (ambient always-on recording, continuous capture, or incremental expansion of monitoring scope framed as normalizing total information awareness — \"constantly capture audio and visuals,\" \"AI is listening,\" \"record throughout the day\"), market flooding (volume, speed, or scale of product distribution cast as aggressive or overwhelming — \"flooding the market,\" \"into the hands of as many people as possible,\" \"market saturation\"), humanization (emotionally resonant personal details creating sympathy for affected individuals — \"laid off two days before giving birth,\" pregnancy near workplace action, age-specific vulnerability — strategic placement of intimate biographical detail to move reader from policy abstraction to personal identification), surveillance enumeration (multi-item comma-separated lists of monitoring technologies or data types amplifying perceived invasiveness through sheer accumulation — the list length itself is the editorial device, even when each item is factually accurate), glasshole revival (revival of "glasshole" pejorative from 2013 Google Glass era to frame current smart glasses products — invokes historical social stigma as predictive of current rejection), walking camera (framing that reduces smart glasses wearers to ambulatory surveillance devices — "walking surveillance camera," "camera on your face," "turns every wearer into a surveillance device" — dehumanizes wearers by equating them with the device's camera), chilling effect (self-censorship or avoidance behavior by product users/owners due to social stigma — "too scared to wear them in public," "fold them up," "not a good idea to have those" — captures internalized behavioral response where stigma becomes self-reinforcing), success paradox (headline/lede acknowledges positive commercial news then pivots via "even as"/"despite" to negative narrative dominating the word count — "a hit even as concerns pile up," "popular despite prickly climate," "growth doesn't mean a tipping point isn't coming" — uses genuine positive data as Trojan horse for negative framing), safeguard inadequacy (introduces a technical or policy safeguard then systematically undermines it as insufficient — "privacy light but people might not see it," "growing market for disabling indicators," "option to opt out no longer available"), platform self-incrimination (highlights violations, circumvention services, or evidence against the company's own policies found on the company's own platforms/marketplace — "advertised on Meta's own platforms," "trended on Meta's own Threads app for the wrong reasons" — frames distribution channel as ironic self-undermining), category contamination (one company's reputational damage contaminates an entire product category, forcing competitors to delay, redesign, or explicitly distance themselves — "[Company A]'s reputation directly influences [Company B]'s timeline," "poisoned the well," "wants none of it" — converts company-specific failures into category-level stigma)
  - **Structural post-pass (7):** kicker framing (checks final ~400 chars for discordant negative note), analogy stacking (fires when 3+ distinct analogy markers found), speculative framing (fires when 5+ cumulative speculative hedges found — individual hedges are normal journalism; stacked hedges convert possibility into implied certainty), trend bundling (fires when 3+ distinct companies are bundled as comparisons — editorial technique of normalising or amplifying a target company's action by assembling an industry-wide pattern), social proof amplification (detects when articles cite reaction counts — likes, thumbs-up, hearts — to convert individual opinion into collective sentiment), delayed defense (first corporate response appears after 65% of article text — the rebuttal is buried after the accusatory framing), tempering coda (article's final 25% contextualizes or walks back its own headline-level framing — common in tabloid journalism where dramatic headlines drive clicks but the final paragraphs provide a hedging anchor)
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
- **Documentary source detection**: Identifies cited artifacts — recordings, leaked documents, court filings, internal memos, regulatory orders — as `source_type="documentary"`, distinguishing them from named and anonymous human sources for accurate authority scoring and source-type breakdowns

### `topics.py`
- TF-IDF weighted keyword classification into 29 topic buckets
- Multi-label (top 3 by confidence retained)
- Topics: layoffs, ai_development, privacy_data, antitrust_regulation, child_safety, content_moderation, ai_generated_content, financial_results, product_launch, executive_behavior, litigation, prediction_markets, corporate_strategy, defense_military, labor_market, workplace_culture, government_oversight, infrastructure_impact, worker_ai_displacement, health_tech, cybersecurity, ai_ethics_safety, education, subscription_monetization, energy_climate, hardware_wearables, consumer_protection, content_licensing, financial_markets

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

Define entity clusters in publication profiles or pass custom clusters to `detect_entities()`. See [ENTITY_REFERENCE.md](ENTITY_REFERENCE.md) for the complete quick-reference card with all 94 clusters, 898 aliases, disambiguation filters, and pipeline interactions, and [METHODOLOGY.md §15](METHODOLOGY.md#15-entity-detection--cluster-reference) for the cluster reference table with analytical categories and growth history.

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

## Known Limitations & Open Research Questions

> For a practical guide to working around these limitations — including when to trust raw vs. corrected scores, a decision tree, and genre-specific accuracy benchmarks — see [ACCURACY_GUIDE.md](ACCURACY_GUIDE.md).

### Sentiment Correction Gaps

Two documented failure classes lack correction paths:

1. **Financial journalism inflation (unaddressed):** Investment recommendation vocabulary (e.g., "strong buy," "bonanza," "attractive valuation") inflates VADER scores by +0.3–0.5 regardless of editorial stance. A future correction path would use headline sentiment as an anchor combined with framing device density. See [METHODOLOGY.md §16](METHODOLOGY.md#16-financial-journalism-sentiment-bias) for full analysis and design constraints.

2. **Procedural service journalism (partially addressed):** VADER misscores privacy alarm articles where the negative tone is structural (consent_alarm devices, guilt transfer sections) rather than lexical. No standard correction path fires because the article lacks adversarial editorial vocabulary — the alarm comes from framing, not word choice. Discovered via NY Post Muse Image opt-out article (Jul 10, 2026). **Partial fix (Jul 14, 2026):** The forced-retreat override (Path A variant) now handles the subset of service journalism where `policy_reversal + consent_alarm` co-occur, by waiving the agency threshold so Path A can fire even with positive agency. Articles with consent_alarm *without* policy_reversal remain uncorrected. See [ACCURACY_GUIDE.md](ACCURACY_GUIDE.md) and [SENTIMENT_CORRECTION_REFERENCE.md](SENTIMENT_CORRECTION_REFERENCE.md#path-a-variant-forced-retreat-override-jul-14-2026) for details.

### Source Extraction

- **LinkedIn as a data source:** Career data enrichment from LinkedIn is blocked by Chrome App-Bound Encryption, limiting automated profile expansion. Career entries must be manually researched from public sources (conference bios, author pages, press releases).
- **Freelance/concurrent roles:** The migration detector uses gap analysis to distinguish genuine job changes from concurrent freelance roles, but short-duration freelance stints (< 3 months) between permanent positions can be miscounted as migrations.

### Genre as Confounding Variable (Open — Identified Jul 13, 2026)

Same-event cross-publication analysis of the Meta Hyperion Louisiana datacenter expansion (6 outlets, same day) revealed that **article genre predicts framing more reliably than publication identity**. The two news-genre articles (Fox Business, WSJ) both included community impact voices; the three investor-analysis articles (Barron's, IBD, MarketWatch) all omitted community voices and led with analyst framing; the Washington Examiner added a patriotic sovereignty frame absent from the other five. See `examples/sample_output/cross_pub_meta_louisiana_datacenter_6way_2026_07_13.md` for full evidence.

**Implication for asymmetry scoring:** When comparing publications, an apparent asymmetry between Publication A and Publication B may actually reflect genre-mix differences (e.g., A publishes more investor-angled coverage, B publishes more news reports). The asymmetry score would attribute to editorial bias what is actually a genre composition effect.

**Proposed solution:** Add `genre` as a confounding variable in asymmetry calculations. Minimum genre categories: `news_report`, `investor_analysis`, `opinion_editorial`, `investigative`, `service_journalism`. This would enable within-genre comparisons that better isolate genuine editorial asymmetry from genre effects. Not yet implemented — requires genre classification as a pre-analysis step.

### Competitor Sentiment Augmentation (Open — Requested Jul 12, 2026)

The current asymmetry scoring compares a target entity's sentiment against peers, but does not weight competitor mentions within target articles. When an article about Meta favorably mentions Google or Apple, that favorable competitor mention currently counts only toward the competitor's entity sentiment — it does not register as an implicit negative signal *within* the Meta article. A future enhancement would compute intra-article competitor sentiment differentials.

### Scope

- The toolkit currently tracks **6 publications** with full ownership profiles. Adding publications requires manual research into ownership chains, revenue relationships, and litigation connections (see [ADDING_PUBLICATIONS.md](ADDING_PUBLICATIONS.md)).
- Entity clusters (88) are optimized for the tech/media/finance domain. Analysis of other verticals (e.g., pharmaceutical, energy, defense) would require domain-specific cluster expansion.
- The DiD analysis for journalist migrations requires a minimum of 5 articles per publication per journalist — low-output contributors cannot be analyzed even when their career path is well-documented.

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
│   ├── the-verge.yaml
│   └── careers/
│       ├── journalists.yaml
│       └── editorial_changes.yaml
├── docs/
│   ├── METHODOLOGY.md
│   ├── EDITORIAL_HISTORIES.md
│   ├── AGENT_GUIDE.md
│   ├── ADDING_PUBLICATIONS.md
│   ├── QUALITY_STANDARDS.md
│   ├── FRAMING_REFERENCE.md
│   ├── TOPIC_REFERENCE.md
│   ├── ENTITY_REFERENCE.md
│   ├── SOURCE_ANALYSIS_REFERENCE.md
│   ├── SENTIMENT_CORRECTION_REFERENCE.md
│   └── ARCHITECTURE.md      # (this file)
├── examples/
│   ├── quick_start.py
│   ├── full_pipeline.py
│   ├── same_event_comparison.py
│   ├── conflict_disclosure_demo.py
│   ├── framing_correction_demo.py
│   ├── topic_classification_demo.py
│   ├── agent_integration.py
│   └── sample_output/       # 206 annotated real-article analyses (see METHODOLOGY.md §17)
├── tests/                       # 10078 tests across 315 test files (all from real articles)
│   ├── test_accuracy_guide.py   # ACCURACY_GUIDE.md consistency: existence, cross-references, content structure, correction path table, annotated article count sync
│   ├── test_advance_dual_asset_monetization_aug8.py  # Advance Publications dual-asset AI monetization: Reddit Q2 2026 earnings + Condé Nast strategic pivot + Sam Altman Reddit conflict
│   ├── test_advance_total_ai_financial_exposure_index_aug11.py  # Advance Publications Total AI Financial Exposure Index: Q2 2026 Reddit earnings quantification + litigation pipeline + Condé Nast editorial cost-reduction + composite exposure index
│   ├── test_analyst_quote_attribution.py # Analyst/financial quote attribution: firm-level post-attribution suppression, wire cross-citation filtering, genuine scare quote preservation
│   ├── test_asymmetry.py        # Asymmetry score, Welch's t, Cohen's d, bootstrap CI
│   ├── test_atlantic_analysis.py # Atlantic-specific: Emerson Collective conflicts, AI coverage
│   ├── test_atlantic_apple_openai_silence_aug6.py # Atlantic × Apple v. OpenAI: 27-day editorial silence, five-way financial conflict, omission bias
│   ├── test_avclub_sardonic_framing.py # AV Club sardonic framing: sarcastic_correction sub-patterns, loaded_language ad hominem/industry-as-vice, ironic denial regex
│   ├── test_bofa_capex_watermelon.py # BofA capex/Watermelon model: comma-after-entity lookahead fix, Barron's + Memeburn entity/framing detection, scale_magnitude "nearly double"
│   ├── test_careers.py          # Career loading, migration detection, DiD, leadership ITS
│   ├── test_citations.py       # Citation extraction, source grading, domain classification
│   ├── test_cli_doc_consistency.py # Structural consistency: validates all CLI examples in docs/*.md and README.md use real CLI flags (catches phantom flags) and that documented commands are real
│   ├── test_claims.py          # Claim-to-source mapping, statistic/quote detection
│   ├── test_entities.py        # Entity detection, regex, false-positive exclusion
│   ├── test_financial_relationships.py  # Financial relationship data integrity, asymmetry hypothesis
│   ├── test_financial_incentive_mapping_aug5.py  # Perplexity hypocrisy arc, Anthropic absence, Google coercive structure, updated aggregate counts
│   ├── test_glasses_deep_dive.py # Glasses launch fixes: kicker framing, product-name stop-filter, emotional_appeal exclusion
│   ├── test_gizmodo_openai_rogue_ai_framing_paradox_aug7.py # Gizmodo × OpenAI vs Meta rogue AI framing paradox (Aug 7): CLEAN CONTROL — Gizmodo (Keleops AG, zero financial ties) covers OpenAI's ACTUAL rogue AI hack (Hugging Face production breach, 4 accounts compromised, infrastructure rebuilt) with procedural tone (-0.25) while covering Meta's SPECULATIVE glasses privacy (unconfirmed facial recognition, zero affected users) with apocalyptic framing (-0.75). 0.50 tone delta = cultural baseline of editorial asymmetry. 10 classes, 39 tests: severity comparison, headline framing, in-article language, advocacy citation asymmetry, company voice, clean control verification, causal factors (narrative templates, source framing, company identity), tone scoring, cross-reference, source citations
│   ├── test_nilay_patel_cross_entity.py # Nilay Patel (Verge EIC) cross-entity (Aug 7): EIC Delegation Paradox (mechanism #6) — Patel personally interviews competitor CEOs (Pichai annually at I/O, Suleyman, Ronan Farrow/OpenAI) with strategic "big ideas" framing but DELEGATES all Meta CEO interviews to deputy Heath who applies adversarial-investigative framing. Meta -0.45, Google -0.15, OpenAI -0.30, Microsoft +0.05, Apple -0.10. Publisher solidarity context: Patel raised Condé Nast "assume zero search traffic" in Pichai interview, Meta's "overestimate the value" dismissal of publishers reinforces delegation pattern. 11 classes, 32 tests
│   ├── test_gizmodo_fury_review.py # Gizmodo Meta Fury contradictory review: entity detection, Path F tone correction, emotional terms
│   ├── test_gizmodo_glasses_harassment_ban_jul23.py # Gizmodo glasses harassment Instagram ban (Jul 23): 15 framing devices (7 types), 5 new patterns: escalation_amplification "reached entirely new heights" (peak-escalation phrase), escalation_amplification "fever pitch", recidivism_framing sardonic "[Entity]'s always been good at" chronic behavior, recidivism_framing predictive "We can expect more mixed messaging", editorial_aside parenthetical "meanwhile" contrast. Control-case convergence: Swiss-owned Gizmodo produces identical framing to WIRED (zero Condé Nast connection)
│   ├── test_gizmodo_brain2qwerty_v2.py # Context-aware false-positive suppression: dream/sleep catastrophizing, medical loaded language, factual medical emotional appeal, definitional ironic quotation
│   ├── test_gizmodo_meta_1_4t_penalty.py # Gizmodo $1.4T penalty: source extraction patterns (filing_as_source, legal_party, per-source)
│   ├── test_ap_appeals_deep_dive.py # AP Meta appeals verdict deep dive: hook infinitive (loaded_language), legal woes editorialization, shielded-from metaphor, kicker/trend_bundling integration
│   ├── test_gizmodo_1_4t_deep_dive.py # Gizmodo $1.4T existential threat deep dive: headline scale_magnitude, loaded_language gaps (exploiting, hooked), litigation cascade, sentiment
│   ├── test_gizmodo_1_4t_consumer_protection.py # Gizmodo $1.4T consumer protection: consumer_protection topic classification, valuation_comparison framing device, strategic_disclosure with curly quotes, entity extraction for AGs and legal actors
│   ├── test_gizmodo_1_4t_teen_safety.py # Gizmodo $1.4T teen safety existential threat: litigation_cascade (new — multi-front legal stacking), defensive_verb_framing (new — loaded attribution verbs), zero named human sources, sentiment intensity 1.0, entity detection for state AG coalitions
│   ├── test_gizmodo_super_sensing_glasses.py # Gizmodo super-sensing glasses editorial: entity detection (Meta, FT, Zuckerberg), source extraction (Svenska Dagbladet via pub-cite pattern, anonymous sources), ironic_quotation/loaded_language/anonymous_authority framing, privacy_data + hardware_wearables topics, new emotional language terms (ick people out, face computers, unsavory, problematic history)
│   ├── test_gizmodo_zuckerberg_underclass.py # Gizmodo Muse Spark 1.1 "permanent underclass" editorial: analogy_metaphor gap fix (would-be-like-calling pattern for damning analogies), loaded_language expansion (ignominious, disingenuous, hubris), gerund simile pattern, Anthropic entity cluster validation, scale_magnitude for $1.4T reference
│   ├── test_gizmodo_siege_roundup_jul11.py # Gizmodo "Meta Under Siege" roundup: sarcastic_correction gap fix ("somehow...supposed to" pattern), recidivism_framing gap fix (predictive legal scrutiny patterns), 12 framing devices (loaded_language, emotional_appeal, regulatory_shadow, geopolitical_regulatory_pressure, sovereignty_framing, catastrophizing, pathologizing_metaphor, refusal_amplification, no_comment_implication, sarcastic_correction, recidivism_framing), entity detection (Meta, EU Regulatory, Gizmodo, Financial Times, 404 Media, Patentlyze, Horizon Worlds), sentiment correction (raw 0.42→corrected -0.19)
│   ├── test_kotaku_muse_image_editorial_attack.py # Kotaku Meta Muse Image removed article (Jul 11): editorial_character_attack device type (new — journalist's own character judgment as fact), 9 new loaded_language terms (encroachment, regurgitated, cloak and daggery, cause for alarm/worry, unsavory, unnerving, curtly, quell suspicions), policy_reversal, Meta/Instagram/SAG-AFTRA entity detection
│   ├── test_gizmodo_muse_scrapped.py # Gizmodo Muse Image scrapped article (Jul 11): SAG-AFTRA corporate_spokesperson reclassification (hyphenated org regex), blog post documentary source, Reuters pub citation ("according to [Pub]"), consent_alarm ("pulled face data by default"), temporal compression in policy_reversal ("three days in operation", "made it to Friday"), sarcastic_correction ("world record" opener), precedent_analogy coined-term ("The Ghibli Meme Effect"), Path L sentiment correction (quote-inflated body + negative headline: raw +0.63→corrected -0.13)
│   ├── test_gizmodo_smart_glasses_celebrity_backlash_jul14.py # Gizmodo smart glasses celebrity backlash (Jul 14): entity detection (Meta cluster with Ray-Ban Meta/Instagram/Starfire, Apple, Google, Samsung, Kylie Jenner Celebrity/Influencer cluster, Wired), loaded_language framing ("backlash", "blasted"), failure_precedent framing (Google Glass "tried, and failed" temporal setup), source extraction Ray-Ban hyphen false-positive regression (Pattern 5c compound-word fix), Lorde source detection
│   ├── test_gizmodo_layoff_discrimination_jul15.py # Gizmodo Meta AI layoff discrimination (Jul 15): Metamate entity detection (Meta cluster), humanization framing fixes ("away from" preposition, "selected" termination verb), full-article integration (≥9 framing devices, surveillance_enumeration), pregnancy-near-harm pattern expansion
│   ├── test_investor_framing.py # Investor-media framing patterns and ticker entity detection: narrative_reframing, dismissive_qualifier, bull_bear_structuring device types; NVDA/Rubin/Blackwell ticker/platform entity detection; integration tests against Motley Fool Meta compute article
│   ├── test_market_overbuilding_framing.py # market_verdict and overbuilding_narrative framing devices (Category 12: Financial & Investor Media Framing), plus speculative_framing pattern expansions (may be [verb]ing, would [adverb] [verb], could be [past participle]); discovered from WSJ AI Spending article (Jul 8, 2026)
│   ├── test_watermelon_bofa_entities.py # Watermelon/Muse Image/Muse Video Meta entity detection, BofA/Berkshire Hathaway financial entity detection, and analyst_authority framing device regression tests; discovered from Barron's BofA AI spending article (Jul 7, 2026)
│   ├── test_memeburn_chip_selloff.py # MemeBurn chip sell-off article analysis and regression tests
│   ├── test_loaded_language_jul7.py # Loaded language wordlist expansion: exploit/exploiting/exploited, hooked (addiction metaphor)
│   ├── test_strategic_disclosure.py # Strategic disclosure framing: party-originated legal demands, court filing figures, opponent positioning
│   ├── test_hypocrisy_medical_duress.py # Hypocrisy frame detection, medical duress framing, healthcare-as-leverage patterns
│   ├── test_humanization_and_surveillance_enumeration.py # humanization + surveillance_enumeration framing devices, censored profanity emotional_appeal extension
│   ├── test_inc_muse_image_backlash_jul14.py # Inc.com Muse Image backlash patterns (Jul 14 2026): confession_framing post-quote attribution, cross_publication_import named publication reference, policy_reversal temporal urgency qualifiers, loaded_language death/termination metaphors, full article integration test (13+ devices)
│   ├── test_inc_threads_500m_patterns.py # Inc.com Threads 500M patterns: scale_magnitude milestone detection (user-count crossings), competitive_positioning headline patterns (put on notice, leaves behind, overtakes/eclipses/dethrones), full headline integration (Jul 8 2026)
│   ├── test_iphoneincanada_eu_dsa_regressions.py # iPhone in Canada EU DSA article regressions: tag-question rhetorical_question pattern ("...anyone?"), executive_behavior title suppression for "Executive Vice-President" (Jul 12 2026)
│   ├── test_james_pero_cross_entity.py # James Pero (Gizmodo) cross-entity: Editorial Direction Override (Mechanism #31) — self-described "resident smart glasses guy" with hands-on ALL brands. Meta product reviews balanced-positive (tone +0.10, Neural Band "groundbreaking", affiliate links), editorial pieces adversarial (tone -0.40, "The anti-Meta plan", competitors as privacy heroes). Samsung/Google identical 12MP camera glasses ZERO surveillance framing; Apple "privacy champion". Genre split delta 0.50 isolates editorial direction from personal bias. 10 classes, 41 tests
│   ├── test_joanna_stern_cross_entity.py # Joanna Stern cross-entity: WSJ (12 years) → independent "New Things" + NBC News — Meta Ray-Ban tone +0.35 to -0.65 (1.00-point swing), reverse Heikkilä pattern, strongest natural experiment for financial-structure effects (Aug 7 2026)
│   ├── test_loaded_language_uproar.py # Loaded language detection, workplace coercion terms
│   ├── test_marketwatch_cloud_pivot.py # MarketWatch Meta cloud pivot: financial-defeat EL terms, ironic_quotation attribution suppression (wrote/believes), simple competitive_deficit pattern
│   ├── test_nyt_ai_reviews.py   # Isolation framing, pressure language, VADER correction
│   ├── test_nyt_amazon_february_simultaneous_paradox.py  # NYT × Amazon Feb 2026: NameTag exposé vs Ring Familiar Faces business framing
│   ├── test_nyt_article_improvements.py  # NYT-specific: agency, coercion, juxtaposition
│   ├── test_nyt_project_giraffe_xai_absence.py # NYT-OpenAI Project Giraffe discovery obstruction, xAI publisher absence, Snowflake Cortex marketplace
│   ├── test_nyt_school_targeting.py  # NYT school targeting: education topic, National PTA entity, safety team overrule hypocrisy, role-based adversarial stance
│   ├── test_nypost_muse_image_yanks_jul13.py  # NY Post Muse Image: capitulation verbs, Path C forced-retreat override, policy_reversal adversarial
│   ├── test_platform_death.py   # Platform eulogy detection, tone distinction
│   ├── test_pmc_deal_fragmentation_paradox_aug7.py # PMC Deal Fragmentation Paradox: Vox Media split orphaned 3 AI licensing deals (OpenAI, Microsoft PCM, ProRata AI), PMC v. Google antitrust (6 Sherman Act claims), perverse incentive direction predicts adversarial Google + softer OpenAI — opposite of observed Meta-focused hostility
│   ├── test_policy_reversal_competitive_deficit.py # Policy reversal and competitive deficit framing device detection, documentary source extraction
│   ├── test_competitive_displacement.py # Competitive displacement framing device (new — fills-vacuum temporal conjunction), entity cluster additions: AI Research Orgs (AI2), HuggingFace, Princeton, plus OpenAI cluster expansions (GPT-2, gpt-oss, Miles Brundage)
│   ├── test_competitor_coverage.py # Competitor entity definitions, publication competitor_relationships validation, financial asymmetry patterns, source URL verification
│   ├── test_privacy_affiliation_fixes.py # Privacy/data topic MCI keyword expansion, source affiliation case-sensitivity
│   ├── test_quality_standards.py # Quality enforcement: banned phrases, em dashes, scoring, zero-named-sources detection
│   ├── test_scale_magnitude.py  # Scale/magnitude framing, raw number amplification
│   ├── test_multiplier_scale_magnitude.py # Multiplier scale/magnitude: N× comparisons, ceiling multipliers, national/global scale analogies
│   ├── test_sentiment.py        # 8-dim scoring, framing correction, self-referential detection
│   ├── test_source_stance.py    # Source extraction, stance, outsourced intensity, kicker framing
│   ├── test_source_extraction_fixes.py # Pattern 3 case fix, Pattern 5c verb-before-surname, attribution verb expansion
│   ├── test_possessive_affiliation.py # Possessive affiliation extraction: "Org's Person Name" pattern, cross-contamination prevention
│   ├── test_topics.py           # Topic classification, all 29 buckets, confidence scoring, density normalization
│   ├── test_wynn_williams_fixes.py # Litigation framing, source extraction false positives, power asymmetry
│   ├── test_virtue_ai_acquihire.py # Virtue AI entities, FAIR, BIS/CAISI, tech-jargon ironic_quotation filter
│   ├── test_victoria_song_cross_entity.py # Victoria Song (Verge) cross-entity coverage: balanced Meta/Apple lens, lane comparison vs WIRED
│   ├── test_will_douglas_heaven_cross_entity.py # Will Douglas Heaven (MIT TR) cross-entity: source access hierarchy, failure framing double standard (Galactica vs Mariner vs OpenAI reward hacking), MIT financial correlation, Heikkilä migration
│   ├── test_will_knight_cross_entity.py # Will Knight (WIRED) cross-entity AI coverage: 7+ OpenAI / 5+ DeepMind / 3+ Anthropic / ZERO Meta articles, talent framing asymmetry, executive access gaps, three-layer WIRED exclusion
│   ├── test_wired_google_glasses_framing_paradox_aug6.py # WIRED smart glasses framing paradox: Google/Samsung Android XR gets product-review framing while functionally identical Meta Ray-Ban gets investigative-surveillance framing, advertising dependency paradox
│   ├── test_zoe_schiffer_cross_entity.py # Zoë Schiffer (WIRED Director) cross-entity: talent war framing asymmetry, OpenAI insider access, Meta adversarial framing, executive profile gap, departure framing divergence
│   ├── test_kashmir_hill_cross_entity.py # Kashmir Hill (NYT) cross-entity: privacy beat concentrated on Meta (Name Tag investigation) while Ring facial recognition (deployed, FTC settlement), Google Android XR, Apple Vision Pro receive zero Hill coverage — beat assignment effect amplified by NYT-Amazon $20-25M deal
│   ├── test_kevin_roose_cross_entity.py # Kevin Roose (NYT → Independent) cross-entity: TRIPLE professional identity capture (AGI Chronicles book, Sydney/Bing career, post-NYT AI media venture), CEO access asymmetry, headline personalization, AI interaction correlation mechanism
│   ├── test_kyle_barr_cross_entity.py # Kyle Barr (Gizmodo) cross-entity: Privacy Gradient Paradox — identical camera glasses, Meta (-0.65 apocalyptic) vs Apple (-0.10 sympathetic) vs Samsung (+0.10 neutral) vs Google (-0.05 mild). Intra-publication Barr/Wong divergence isolates individual editorial culture from institutional incentives. Clean control: ZERO financial ties. 10 classes, 38 tests
│   ├── test_revenue_dependency_ratios.py # Revenue Dependency Concentration Index: normalizes AI deal values by total annual revenue — inverse proportionality paradox, margin amplification effect, disclosure paradox, 9 publications with verified revenue sources
│   ├── test_sean_hollister_cross_entity.py # Sean Hollister (Verge senior editor) cross-entity: Apple recusal asymmetry, pre/post-recusal coverage shift, consumer harm lane gap, 3-entity coverage pattern, structural vs personal ethics
│   ├── test_sam_schechner_cross_entity.py # Sam Schechner (WSJ Paris) cross-entity: Mechanism #9 topic-dependent register shift, same journalist 3 registers across Meta/Anthropic/OpenAI, co-authorship control, EU regulation baseline, podcast escalation
│   ├── test_sheera_frenkel_cross_entity.py # Sheera Frenkel (NYT) cross-entity: Mechanism #9 Book Deal Narrative Capture, seven-figure "An Ugly Truth" undisclosed financial conflict, sympathy-adversarial inversion (Meta -0.55 vs Anthropic -0.05), refusal framing inversion, Anthropic redemption arc (12+ articles), government scare quote asymmetry, beat migration register preservation
│   ├── test_steven_levy_cross_entity.py # Steven Levy (WIRED Editor at Large) cross-entity: headline diagnostic asymmetry (Meta institutional-pathology vs Google neutral-enterprise vs competitor personality-driven), access-book trajectory divergence (post-Google warm, post-Facebook adversarial), CEO-platforming asymmetry, Advance/Reddit financial correlation, whistleblower amplification asymmetry
│   ├── test_anthropic_ipo_investor_publisher_triangle_aug9.py # Anthropic IPO Investor-Advertiser-Publisher Triangle: ZERO direct deals but NOT financially neutral — Amazon ($13B+, $76B/yr ads) and Google ($3B+, $81.6B/yr ads) are investors AND publishers' biggest ad partners — indirect incentive triangle, corrects "financially neutral" claim, coverage predictions
│   ├── test_anthropic_meta_cloud_deal_coverage_selection_aug11.py # Mechanism #38: Anthropic-Meta $10B cloud deal (Jul 17 2026) coverage selection — NYT/Reuters/Bloomberg/CNN covered; WIRED/The Verge had NO standalone articles found. Anthropic's non-Meta deals (SpaceX, CoreWeave, Fluidstack) were covered by these same publications. Adversarial tone + no Meta deal correlates with omission. WSJ (balanced) covered. 8 classes, 60 tests
│   ├── test_chokkattu_samsung_coverage_selection_gap_aug11.py # Mechanism #39: Chokkattu Samsung Coverage Selection Gap — 3+ Meta articles in Jun-Jul 2026, zero Samsung Galaxy Glasses articles despite identical hardware (Snapdragon AR1 Gen 1, 12MP camera, AI, LED anti-tamper). Extends #30 from framing to selection asymmetry. 8 classes, 41 tests
│   ├── test_chokkattu_wired_compound_competitor_silence_aug11.py # Mechanism #42: Compound Competitor Wearables Coverage Selection Silence — Chokkattu published 3+ Meta glasses articles Jun-Jul 2026 but ZERO standalone Snap Specs ($2,195, 4 cameras, Jun 16 AWE, 14+ pubs covered) AND zero Samsung Galaxy Glasses (Jul 22, 20+ pubs covered). Camera Count Paradox: Snap 4× Meta's cameras, zero surveillance framing. Extends #39 to systematic compound silence. 10 classes, 46 tests
│   ├── test_dual_client_litigation_entanglement_index_aug11.py # Mechanism #43: Dual-Client Litigation Financial Entanglement Index — Apple v. OpenAI trade secret lawsuit (Jul 10 2026) first active litigation between two entities jointly funding same publisher clients via Apple News+ and OpenAI content licensing. Five dual-client pubs (Condé Nast, News Corp, Vox Media, Atlantic, Hearst). WSJ factual-relay; WIRED/Verge/Atlantic no confirmed standalone articles. Meta loaded language 3.7× higher. Meta zero deals either channel. 9 classes, 69 tests
│   ├── test_type_d_2pm_cross_validation_aug9.py  # Cross-validation Aug 9: Ryan Mac beat capture ↔ rogue AI experiment, eMarketer ↔ publisher financial models, NYT dual mechanism (Mac+Frenkel), cross-publication lane assignment (WIRED+Verge), Levy ↔ Google I/O, eMarketer ↔ cross-pressure materiality, cumulative integrity. 7 classes, 35 tests
│   ├── test_type_d_6pm_cross_validation_aug9.py  # Cross-validation Aug 9 15-17h sprint: Barrett Crisis/Makeover ↔ Condé Nast Opacity, Wong Camera Paradox ↔ Barrett cross-pub convergence, financial amplification (Gizmodo 0.50 baseline vs WIRED 1.0), revenue materiality tone gradient, parity acknowledgment gradient, cumulative sprint integrity. 6 classes, 29 tests
│   ├── test_gizmodo_google_io_2026_camera_paradox_aug9.py # Gizmodo × Google I/O 2026 Camera Acknowledgment Paradox: Wong's 6 Google camera-glasses articles (zero privacy headlines) vs 3+ Meta articles (privacy/surveillance dominant), explicit camera parity acknowledged, decomposed into legitimate (incidents, data practices, market maturity) and editorial (headline gap, Google Glass amnesia, source ecosystem) factors. 8 classes, 35 tests
│   ├── test_brian_barrett_cross_entity.py  # Brian Barrett (WIRED Executive Editor, News): Crisis/Makeover Headline Paradox — May 21 2026 headline applies "crisis" to Meta and "makeover" to Google in SAME headline for SAME underlying dynamics. 100% crisis language for Meta, 100% neutral/positive for competitors. Structural editorial direction. Mechanism #14. 8 classes, 36 tests
│   ├── test_casey_newton_cross_entity.py   # Casey Newton (Platformer/Hard Fork): Disclosure-as-Inoculation Paradox — fiancé at Anthropic, best-in-class disclosure but self-regulated. Meta accountability framing vs Anthropic admiration framing. Claude Code personal adoption → positive columns. Aug 2026 independence transition removes last institutional check. Mechanism #24. 8 classes, 27 tests
│   ├── test_amazon_dual_lab_non_disclosure_triangle_aug10.py  # Type C: Amazon-Bezos $63B Dual-Lab Non-Disclosure Triangle — Mechanism #25. Amazon $50B OpenAI (Feb 2026) + $13B Anthropic = $63B largest dual-lab investment (3.5x Microsoft). PROFILE CORRECTION: "Amazon invests in Anthropic only" was factually wrong. Bezos owns WaPo; WaPo has OpenAI content deal. Washingtonian (Jun 23 2026) documented systematic non-disclosure on editorial pages. OpenAI $138B AWS deal undisclosed. Dual S-1 IPO exposure. Meta zero IPO stake. 8 classes, 26 tests
│   ├── test_google_q2_2026_meta_coverage_asymmetry_aug8.py # Google vs Meta Q2 2026 earnings coverage asymmetry: Alphabet Q2 earnings ($119.8B/+24%, $81.6B ads, $44.9B capex, -$5.9B FCF), 5 framing patterns (capex narrative inversion, net income quality erasure, FCF double standard, growth rate suppression, headline register asymmetry), financial incentive prediction 100%
│   ├── test_safe_target_coefficient_aug8.py # Type C Safe Target Coefficient quantification: binary Meta-deal predictor (9/9 accuracy), competitor deal gradient (r≈0.52), per-publisher asymmetry scores + meta_avg_tone, News Corp symmetric control, Gizmodo zero-deal control, safe target delta range
│   ├── test_samsung_equivalence_paradox_aug7.py # Samsung Equivalence Paradox: Samsung Intelligent Eyewear functionally identical to Meta Ray-Ban (12MP camera, mics, AI, LED indicator, ~50g, no display) yet receives product-review framing while Meta gets adversarial framing; Iberville Parish school ban names Meta glasses only despite identical Samsung hardware
│   ├── test_apple_google_gemini_publisher_chain_aug7.py # Apple-Google $1B/yr Gemini deal creates publisher content bypass chain: Apple negotiated with Condé Nast/NBC/IAC ($50M, Dec 2023) but signed no deals; instead paid Google for Gemini model trained on publisher content (Hachette/Cengage lawsuit confirms), bypassing direct publisher licensing entirely
│   ├── test_verge_anthropic_rogue_ai_comparison.py # The Verge Anthropic/OpenAI/Meta three-tier coverage: "Accidentally" Paradox, rogue AI safety comparison, pay→soft/neutral→factual/threaten→adversarial, reporter lane extension to Anthropic
│   ├── test_raymond_wong_cross_entity.py # Gizmodo Raymond Wong cross-entity: Clean Control Paradox (no-deals publication balanced), Maxwell Zeff migration (Gizmodo→WIRED), three-tier model validation, aggregate control evidence
│   ├── test_ryan_mac_cross_entity.py  # Ryan Mac (NYT Tech Accountability) cross-entity: BEAT CAPTURE — hired for "all manner of tech companies" but covers exclusively Meta + Musk. Three mechanisms: sourcing lock-in, book-deal incentive (Character Limit parallels Frenkel's An Ugly Truth), institutional assignment. OpenAI sole article = NYT's own lawsuit (institutional advocacy). Coverage gap: Google 0, Apple 0, Amazon 0, Anthropic 0. Personal adversarial dynamic with Musk (Twitter suspension, Maye Musk racial attack). 7 classes, 47 tests
│   ├── test_reddit_ai_editorial_loop_advance_aug9.py  # Reddit AI Data Licensing → Advance/WIRED Circular Editorial Incentive: WIRED "must pay" coverage strengthens Reddit licensing position ($60M/yr Google, ~$70M/yr OpenAI, $550M projected), Advance 23.3% equity ($6.82B). Reddit Q2 2026 $372.4M rev +61% YoY. Google non-renewal risk. Perplexity MTD denied. SRMG Q2 stabilization. 8 classes, 35 tests
│   ├── test_openai_ad_revenue_emarketer_counter_forecast_aug9.py  # OpenAI Ad Revenue eMarketer Counter-Forecast: US chatbot ad market <$1B 2026, $5.41B 2030 vs OpenAI $100B target (18x overshoot, 90% miss). Revised financial incentive model: content licensing remains material, Google leverage increases, deal dependency > ad dependency. AI ad spend 80%+ alongside-AI-content (Google). 8 classes, 34 tests
│   ├── test_charlie_warzel_cross_entity.py # Charlie Warzel (Atlantic) cross-entity: career-defining adversarial Meta beat, OpenAI executive access asymmetry, Apple coverage absence, vocabulary/investigation/financial incentive correlation
│   ├── test_chokkattu_ashworth_cross_entity.py # Chokkattu & Ashworth (WIRED Gear desk) cross-entity: "Creep Paradox" — Meta glasses get 'creep'/'surveillance' framing, Snap (4 cameras) and Google (cameras + Gemini) get none; dual-channel influence via Business Wars podcast; Condé Nast financial correlation
│   ├── test_chokkattu_temporal_framing_oscillation_aug10.py # Chokkattu (WIRED) genre-determined framing direction: same-journalist temporal oscillation — adversarial in podcast, balanced in product article, adversarial in editorial analysis within 30-day window; cross-publication convergence with Gizmodo Mechanism #31
│   ├── test_parmy_olson_cross_entity.py # Parmy Olson (Bloomberg Opinion) cross-entity: CEO personalization asymmetry — 87.5% Meta headlines personalize to "Zuckerberg" vs 0% for OpenAI/Anthropic; loaded language asymmetry ("bait," "slop," "failure club" for Meta vs analytical framing for competitors); professional identity capture mechanism via "Supremacy" book — new asymmetry type distinct from financial incentives
│   ├── test_mark_gurman_cross_entity.py # Mark Gurman (Bloomberg) cross-entity: Access Dependency — Beat Reporter Competitive Narration (Mechanism #11). Apple wearables aspirational (+0.30) vs Meta wearables competitive-obstacle (−0.25). Key patterns: first-person strategic narration, developmental framing asymmetry, delay-as-refinement vs delay-as-failure, talent narrative directionality. Access dependency mechanism, not financial — distinct from Olson #9
│   ├── test_apple_openai_litigation_cross_pressure_aug9.py # Apple-OpenAI litigation publisher cross-pressure (Jul-Aug 2026). 6 dual-tie publications mapped. Anthropic settlement date fix (Jun→Jul 20) + expanded detail (482K works, $3.1K/work, payments Aug 10). WSJ balanced, TechCrunch Apple-sympathetic, Reuters neutral control
│   ├── test_christopher_mims_cross_entity.py # Mims (WSJ) cross-entity: TONE INVERSION — constructive Meta (+0.3) vs skeptical OpenAI (-0.3), validates balanced control; WSJ systematic disclosure (only pub that discloses financial ties)
│   ├── test_dan_milmo_cross_entity.py    # Milmo (Guardian) cross-entity: "BIG TOBACCO" framing asymmetry — Meta gets loaded metaphor, OpenAI rogue agent gets factual relay. Gap ~0.20. Editorial leadership role means institutional direction.
│   ├── test_david_pierce_cross_entity.py # Pierce (Verge) cross-entity: INSTITUTIONAL FRAMING IMMUNITY — 5-publication career proves adversarial Meta framing is editorially imposed, not reporter-driven. Balanced Meta tone across WIRED/WSJ/Verge contexts.
│   ├── test_paresh_dave_cross_entity.py # Dave (WIRED) cross-entity: EMOTIONAL REGISTER ASYMMETRY (Mechanism #8) — Meta coverage uses "gulag"/"piece of shit" in headlines (tone -0.51), OpenAI uses "quietly scrapped" (tone -0.07), Google gets "paid off" (tone +0.08). Source pipeline + headline escalation institution-driven, not reporter-driven.
│   ├── test_wired_apple_lane_assignment.py # WIRED Apple vs Meta wearables lane assignment: Camera Count Paradox, editorial desk assignment by manufacturer identity, financial alignment
│   ├── test_wired_amazon_surveillance_parity_paradox_aug8.py # WIRED × Amazon Surveillance Parity Paradox: Meta dormant NameTag code (never activated) gets multi-part investigation while Amazon's FTC Ring/Alexa settlements, active Familiar Faces lawsuit, and Bee wearable get editorial silence — despite two Condé Nast-Amazon licensing deals. 8 classes, 38 tests
│   ├── test_wsj_anthropic_deception_framing_triangle_aug8.py # WSJ Rogue AI Deception Triangle: Three articles, three companies (OpenAI/Anthropic/Meta), three registers (adventure/capability-admiration/adversarial). Only Meta named in headline. Disclosure asymmetry: OpenAI deal disclosed in favorable article, Anthropic/Meta deals omitted in adverse. Beat assignment predetermines frame. 7 classes, 45 tests
│   ├── test_wsj_rogue_ai_severity_framing_inversion_aug8.py # WSJ Rogue AI Severity-Framing Inversion: Equal ~$50M/yr deals with OpenAI and Meta, inverted framing — OpenAI MORE severe gets "Jurassic Park" adventure, Meta LESS severe gets "drumbeat" adversarial. Barron's counterpoint, cross-publication triangulation. 7 classes, 45 tests
│   ├── test_wsj_openai_ad_cannibalization_self_demonetization_aug10.py # WSJ × OpenAI Ad Cannibalization — Content Licensee Self-Demonetization Paradox (Mechanism #22): 6-step financial chain from $50M/yr content licensing to ad cannibalization, Paywall Penalty 0% citation data, investigative depth gap not tone gap. 11 classes, 62 tests
│   ├── test_wsj_anthropic_meta_business_viability_framing_aug10.py # WSJ × Anthropic vs Meta — Business Viability Framing Asymmetry with Settlement-Incentive Bias (Mechanism #26): deficit/follower language for profitable Meta vs celebration/hero for unprofitable Anthropic. Settlement incentive, embedded follower framing, missing critical analysis. 8 classes, 46 tests
│   ├── test_google_spv_guarantee_anthropic_showcase_chain_aug10.py # Type C: Google Quintuple Anthropic Exposure + $35B SPV Guarantee + Showcase Publisher Dependency Chain (Mechanism #28). Google as payment guarantor on $35B off-balance-sheet SPV + Showcase dependency chain to 700+ publishers. 8 classes, 32 tests
│   ├── test_nyt_anthropic_triple_chain_incentive_aug10.py # NYT × Anthropic Triple-Chain Financial Incentive Structure (Mechanism #23): Three independent pathways — direct settlement (UNVERIFIED), Amazon indirect chain ($53.4B Q2 gain), litigation halo (NYT v. OpenAI). Kevin Roose 0.60 tone delta, rogue AI coverage gap. 7 classes, 27 tests
│   ├── test_wired_apple_openai_silence_aug7.py # WIRED 28-day silence on Apple v. OpenAI trade secret lawsuit, cross-pub comparison, financial amplification evidence
│   ├── test_nyt_cade_metz_cross_entity.py # Cade Metz (NYT) cross-entity AI coverage: OpenAI/Anthropic technology-progress framing vs Meta adversarial beat reporter assignment
│   ├── test_mike_isaac_cross_entity.py # Mike Isaac (NYT) cross-entity coverage post-beat expansion: consistent framing across Meta/Anthropic/SpaceX, Eli Tan succession, institutional lane assignment
│   ├── test_meta_deal_landscape.py # Meta AI deal landscape: 13 partners, excluded publishers, WIRED/Verge Microsoft+Perplexity relationships, deal-coverage correlation validation
│   ├── test_meta_inverse_leverage_q2_2026_aug8.py # Meta Q2 2026 earnings, Anthropic $10B compute deal, Inverse Financial Leverage Paradox (1 mechanism vs competitors 4-7)
│   ├── test_beat_assignment_correlation.py # Cross-publication beat/lane assignment → coverage asymmetry correlation: WIRED desk, NYT reporter, Verge institutional split; financial deal-coverage prediction; asymmetry scorer statistical validity
│   ├── test_ft_openai_meta_dual_standard.py # FT OpenAI vs Meta cross-entity framing: always-on device dual standard (Ive device aspirational vs Meta glasses surveillance), spending framing asymmetry, systematic non-disclosure of FT-OpenAI $5-10M/yr deal, reporter assignment (Murphy=Meta), financial incentive → coverage tone correlation
│   ├── test_ft_anthropic_meta_capital_raise_framing_asymmetry_aug11.py # FT Capital-Raise Framing Asymmetry (Mechanism #54): Anthropic aspirational vs Meta desperation framing for identical capital-raising activity. 7 confounding factors, ecosystem-level bias. 10 classes, 40 tests
│   ├── test_ft_openai_guardrails_partner_validation_aug8.py # FT × OpenAI Mechanism #10: investigative target selection as partner validation — May 25 guardrails investigation tested Meta Llama/Google Gemma, validated proprietary (OpenAI/Anthropic) as safer, undisclosed FT-OpenAI deal, proprietary falsification by GPT-5.6 Sol Hugging Face hack
│   ├── test_ft_openai_hardware_privacy_double_standard_aug9.py # FT × OpenAI Mechanism #18: Hardware Privacy Framing Inversion — identical always-on sensing tech (camera, mic, contextual memory) framed as "iPhone of AI" for OpenAI io device vs "surveillance infrastructure" for Meta glasses; FT-OpenAI $5-10M/yr deal, no FT-Meta deal; extends Dual-Lens Paradox (Mechanism #7)
│   ├── test_jeff_horwitz_cross_entity.py # Reuters × Jeff Horwitz Mechanism #19: Triple-Deal Narrative Lock-In — investigative journalist applies maximum-depth techniques (internal documents, undercover experiments, whistleblower cultivation) exclusively to Meta while covering competitors with surface-level wire-service reporting; compounding incentives from book deal (Broken Code, Doubleday), movie deal (The Social Reckoning, Sony/Columbia, Aaron Sorkin, Oct 2026 release), and Pulitzer Prize for Beat Reporting (May 2026)
│   ├── test_ft_google_coverage_asymmetry.py # FT Google vs Meta coverage asymmetry: Google (News AI pilot deal) gets neutral business framing, Meta (no deal) gets surveillance framing. Smart glasses double standard, reporter assignment, regulatory vs coverage split, capex framing delta 0.45
│   ├── test_hannah_murphy_cross_entity.py # Hannah Murphy (FT) cross-entity coverage: same reporter applies different editorial standards to Meta vs Snap for same product category (AR glasses), surveillance language 6:0 Meta:Snap, three-publication lane assignment comparison (WIRED desk / NYT reporter / FT within-reporter), Murphy covers Meta+Snap+TikTok+X+Pinterest but reserves adversarial framing for Meta
│   ├── test_madhumita_murgia_cross_entity.py # Madhumita Murgia (FT AI Editor) cross-entity: Dual-Lens Paradox (Mechanism #7) — covers every major AI company (OpenAI 4, Anthropic 9, Google 4, xAI) with innovation framing, Meta exclusively routed to Murphy (platform desk) with surveillance framing. FT-OpenAI deal (Apr 2024) written by Murgia with no disclosure. AI Labs podcast: Murgia hosts all episodes EXCEPT Meta (Murphy/Criddle, "Zuckerberg's $100bn gamble"). Former Wired UK senior editor
│   ├── test_melissa_heikkila_cross_entity.py # Melissa Heikkilä (FT AI Correspondent) cross-entity: MIT Technology Review → FT career migration (independent → 3 AI deals), Google VP interview access (constructive framing), OpenAI 5+ institutional articles (neutral-constructive), ZERO dedicated Meta articles (peripheral/risk only), Anthropic aspirational framing despite no FT deal, "State of AI" newsletter reverse editorial pipeline MIT TR ↔ FT, coverage volume tracks financial relationships, asymmetry score 0.87. 8 classes, 28 tests
│   ├── test_microsoft_septuple_leverage_aug7.py # Microsoft septuple publisher leverage: SEVEN financial mechanisms (OpenAI axis $13B/27%, Anthropic $5B/$3.2B Q4 gain, PCM marketplace, Copilot Daily, MSN/Start, Bing 1B MAU, Azure $100B+), dual AI lab paradox (most-deals + zero-deals simultaneously), FY26 Q4 $90B/$331.8B, 5/7 profiled pubs have MSFT-adjacent revenue, Meta has ONE mechanism. 14 classes, 61 tests
│   ├── test_type_c_snowflake_marketplace_intermediary_aug7.py # Snowflake Cortex marketplace intermediary: three-tier publisher monetization architecture (bilateral→marketplace→collective), Snowflake as first neutral marketplace (17 publishers, six-figure deals, zero revenue cut), xAI litigation landscape (CSAM/deepfake lawsuits, zero publisher copyright), marketplace concentration risk (Meta absent from all marketplace tiers). 8 classes, 35 tests
│   ├── test_lauren_goode_cross_entity.py # Lauren Goode (WIRED) cross-entity: Apple Vision Pro (12 cameras) emotional empathy / Snap Spectacles playful positive / Meta Ray-Ban clinical→avoidance. Beat shift to AI semiconductors (Nvidia/AMD/Intel/Arm) coincides with Meta glasses becoming WIRED target. Executive access asymmetry (all major chip CEOs + Anthropic vs ZERO Meta). Google I/O 2026 playful zero-surveillance. Score 0.87
│   ├── test_cross_platform_financial_incentives.py # Cross-platform financial incentive matrix: 18 competitor revenue streams (OpenAI, Amazon Rufus/Alexa+, Google News AI pilot, Microsoft PCM, Perplexity, ProRata) across 7/8 MediaScope publications vs 0 Meta deals, aggregate incentive gradient, per-publisher deal breakdowns with source URLs, Google pilot coercive Showcase sunset, Gizmodo clean control
│   ├── test_aggregate_incentive_matrix.py # Aggregate incentive matrix structural integrity: 8-publication matrix field validation, deal count consistency between matrix and excluded_publishers, platform distribution analysis, control group (News Corp balanced/Gizmodo independent) predictions, excluded_publishers schema migration to structured dict format with source_url verification
│   ├── test_news_corp_balanced_control.py # News Corp balanced control verification: WSJ Meta coverage tone (-0.15 vs WIRED -0.85), WSJ OpenAI critical coverage despite deal (-0.40), financial disclosure analysis (WSJ only publication disclosing deals), tone delta quantification, aggregate disclosure finding validation
│   ├── test_news_corp_triple_revenue_aug7.py # News Corp Triple-Revenue Architecture: ONLY publisher receiving AI revenue from three major AI companies simultaneously (OpenAI deal, Meta deal, Anthropic settlement via HarperCollins $1.5B Bartz v. Anthropic). Q4 FY2026 record quarter ($2.34B rev +11%, adj EPS $0.35 vs $0.21 consensus, net income +167%), full year FY2026 ($9B rev, 18% EBITDA margin, $811M FCF +42%, $643M buyback). Brave countersuit (filed 2026-07-22, N.D. Cal.). Thomson: Meta deal "part of the business," Anthropic settlement benefits "in coming months." Woo-and-sue strategy validation. 6 classes, 37 tests
│   ├── test_google_ad_dependency_paradox.py # Google advertising revenue dependency paradox: publishers' SDNY antitrust filings reveal simultaneous Google litigation AND AdX revenue dependency; advertising_dependency relationship type; Vox Media/Atlantic/Advance Publications AdX admissions; Atlantic dual Apple financial link (ownership + News+ platform revenue); financial vector count validation
│   ├── test_google_showcase_coercive_cycle_aug8.py # Google five-year coercive dependency cycle: three-stage model (Showcase dependency creation → AI Overviews traffic destruction → forced News AI pilot rights extraction), contract clauses (secrecy NDAs, anti-litigation, broad IP rights), anti-coordination mechanism, Australia termination, former exec admissions (Chinnappa/Blecher), profiled publication exposure (Guardian/Der Spiegel/El País), Meta zero-coercion contrast (5 vs 0 mechanisms), dependency metrics, coverage paradox. 10 classes, 50 tests
│   ├── test_google_news_ai_prisoner_dilemma_aug11.py # Google News AI Prisoner's Dilemma — CMA Regulatory Arbitrage (Mechanism #50): 200+ publications in News AI pilot, prisoner's dilemma dynamics, CMA opt-out ruling neutralized, Guardian/FT earning "single figure millions" GBP, UK market dominance (36B page views > next 24 combined), deal terms (2-year, NDA, no-sue), Meta zero coercion contrast, 5 confounding factors, 4 testable predictions. 10 classes, 51 tests
│   ├── test_sarcastic_correction.py # Sarcastic correction framing: concede-then-retract, standalone sarcasm, false-positive exclusion
│   ├── test_wired_gulag_patterns.py # Wired "gulag" coverage: conscript terms, keystroke surveillance, Scale AI entity, article-context loaded language
│   ├── test_cannes_contractors.py # Wired "Cannes" contractors: Scale AI/Covalen/Character.AI cluster, catastrophizing "death of" fix, Outlook source exclusion, deception/impersonation patterns
│   ├── test_type_d_fixes.py      # Compound publication source extraction (Business Insider, Daily Beast, etc.) and bare confession framing patterns
│   ├── test_type_d_pattern_fixes_aug5.py # 4 promoted xfails: scale_magnitude $NNN million, plural loaded_language targets, investor_advisory parenthetical tolerance, no_comment_implication contractions, cross-pattern regression
│   ├── test_type_d_deal_count_cascade_aug6.py # Post-Snowflake/xAI cascade validation: deal count consistency (19), xAI entity integration, Snowflake Cortex, Project Giraffe, stale count guards
│   ├── test_type_d_cross_validation_aug6.py # Type D cross-validation suite Aug 6: structural consistency across profiles, entity definitions, financial relationship data, citation URL reachability, cross-profile score validation
│   ├── test_type_d_10am_cross_validation_aug6.py # Type D 10 AM cross-validation: Guardian partial independence, Alex Heath Access Paradox, Advance-Reddit-Perplexity triangle, asymmetry gap ordering, five-mechanism taxonomy
│   ├── test_type_d_7pm_cross_validation_aug6.py # Type D 7 PM cross-validation: MS-OpenAI axis cross-file, Milmo tones cross-file, Atlantic silence, Amazon layers, leverage completeness, source URL consistency
│   ├── test_type_d_midnight_cross_validation_aug7.py # Type D midnight cross-validation: Revenue Dependency Concentration Index arithmetic, deal summation, inverse proportionality ranking, margin amplification, disclosure paradox, revenue plausibility, cross-file consistency, Gizmodo clean control, News Corp balanced symmetry
│   ├── test_type_d_cross_validation_aug7_04am.py # Type D 04:00 cross-validation: Apple-OpenAI 5-phase expansion, Apple-Google Gemini deal integrity, publisher content bypass chain, Apple-Google-Publisher triangle consistency, Samsung equivalence, cross-platform summary, incentive matrix arithmetic, source URL validation
│   ├── test_type_d_cross_validation_aug7_06am.py # Type D 06:00 cross-validation: NYT-Amazon February Simultaneous Paradox (NameTag vs Ring), Samsung Equivalence Paradox entity consistency, PMC Deal Fragmentation financial sums, cross-iteration source URL validation
│   ├── test_type_d_3pm_cross_validation_aug7.py # Type D 15:00 cross-validation: financial amplification model ordering, three-tier marketplace taxonomy, Snowflake entity, Meta isolation claim, metric scale consistency, FT Heikkilä career migration, research cross-references
│   ├── test_nyt_google_traffic_cannibalization_paradox_aug8.py # Type A: NYT × Google Q2 2026 traffic cannibalization paradox — CEO Levien explicitly blamed Google for traffic declines (stock -13%, worst since 2012), yet investigative resources target Meta (zero deal) not Google ($100M+ ad dependency). Oumi study paradox, beat assignment mechanism, attacker-vs-threat inverse relationship
│   ├── test_type_d_11pm_cross_validation_aug7.py # Type D 23:00 end-of-day: entity set evolution (8→11), hardcoded count regression scan, News Corp triple-revenue, WIRED Apple-OpenAI silence, Parmy Olson identity capture, Samsung equivalence + school ban, financial amplification ordering, RDC adversarial zero-Meta invariant, test infrastructure health (217 files, 5994 tests), source URL coverage
│   ├── test_atlantic_wong_cross_entity_framing_aug8.py # Type A 04:00 Aug 8: Matteo Wong three-tier framing hierarchy (Meta -0.45, OpenAI -0.05, Anthropic +0.20), language markers, headline personalization rates, financial relationship correlation, Apple v. OpenAI silence at 29 days, mechanism analysis (adversarial incentive model), confounding factors. 10 classes, 36 tests
│   ├── test_type_d_02am_cross_validation_aug9.py # Type D 02:00 Aug 9 cross-validation: Apple-OpenAI cross-pressure ↔ publication profile consistency, cross-pressure model internal coherence, Anthropic settlement date correction verification, Gurman Mechanism #11 uniqueness, source URL integrity, README/ARCHITECTURE count sync, financial data coherence. 7 classes, 30 tests
│   ├── test_type_d_07am_cross_validation_aug9.py # Type D 07:00 Aug 9 cross-validation: News Corp Factiva dual-role ↔ Anthropic IPO triangle cross-consistency, triple revenue coherence, Anthropic marketplace absence, Microsoft deepest entanglement, Meta isolation claim, Factiva source count coherence, Amazon dual-presence, infrastructure count sync (7296→7322). 7 classes, 26 tests
│   ├── test_nyt_rogue_ai_coverage_natural_experiment_aug9.py # Type A 10:00 Aug 9: NYT × Rogue AI Coverage Natural Experiment — Summer 2026. 3 companies disclosed equivalent rogue agent incidents; NYT gave standalone article to OpenAI (litigation target) only. Anthropic (reported settlement partner, 3 companies breached) and Meta (no deal) got no standalone coverage found. Kevin Roose framing inversion: Mythos platformed as responsible → Mythos published malware to PyPI. 7 classes, 48 tests
│   ├── test_verge_snap_specs_meta_glasses_framing_aug9.py # Type A 08:00 Aug 9: The Verge × Snap Specs vs Meta glasses — camera capability parity, framing divergence. Snap (cameras + OpenAI/Gemini) gets product-review, Meta (camera + Meta AI) gets surveillance/harassment. Financial: OpenAI pays PMC, Meta does not. PIF divested Meta. 7 classes, 57 tests
│   ├── test_wired_google_io_2026_glasses_framing_aug9.py # Type A 03:00 Aug 9 competitor coverage: WIRED Google I/O 2026 smart glasses — Lane Assignment Extends to Google. Live blog framing analysis, AI photo manipulation asymmetry, Google Glass precedent reversal, Chokkattu dual standard, Condé Nast financial correlation. 7 classes, 40 tests
│   ├── test_type_d_03am_cross_validation_aug8.py # Type D 03:00 Aug 8 cross-validation: Google Showcase coercive cycle 3-stage model integrity, Kevin Roose triple identity capture in NYT profile, NYT Google traffic cannibalization paradox financial relationship, cross-iteration consistency (leverage hierarchy MSFT>GOOG>META, Roose departure+financial pressure alignment), entity/test-file count stability (222 files, 6168 tests), source URL integrity, financial amplification model direction. 8 classes, 35 tests
│   ├── test_type_d_07am_cross_validation_aug8.py # Type D 07:00 Aug 8 cross-validation: publications key integrity (no cross-publication findings pollution), cross_publication_findings schema completeness, HTTPS enforcement across all profiles, YAML top-level structure validation, test file count integrity. 5 classes, 21 tests
│   ├── test_type_d_11am_cross_validation_aug8.py # Type D 11:00 Aug 8 cross-validation: 3 bug fixes (showcase section isolation, Atlantic silence day count resilience, Amazon marketplace source_urls key), Meta Q2 2026 inverse leverage validation, Aug 8 file integrity, entity set stability, HTTPS regression. 8 classes, 27 tests
│   ├── test_publisher_ai_revenue_matrix_aug8.py # Publisher AI Revenue Asymmetry Matrix (Aug 8, 15:00 PT Type C): 10 publications mapped with verified deal values, coverage tone, financial direction, disclosure practice. 100% correlation between financial incentive direction and Meta coverage tone — News Corp (ONLY pub with Meta deal) balanced (-0.15), all others adversarial (-0.45 to -0.85). News Corp Q4 FY2026 deep dive: $2.34B rev +11%, $0.35 adj EPS beat $0.21, Thomson praises Meta+OpenAI as "principled" partners. Anthropic $1.5B settlement (Bartz v. Anthropic) HarperCollins share. Cross-validates entity profiles and news-corp.yaml. 11 classes, 71 tests
│   ├── test_publisher_ai_revenue_opacity_index.py # Publisher AI Revenue Opacity Index (Aug 8, 14:00 PT Type C): cross-publisher financial disclosure analysis — 3-tier transparency model (black-box, bundled, transparent) vs coverage adversariality. Digiday Q1 2026, News Corp Q4 FY2026 earnings, NYT Q2 2026 derived revenue. Inverse correlation: opacity predicts adversarial Meta coverage. 10 classes, 69 tests
│   ├── test_type_d_4pm_cross_validation_aug8.py # Type D 16:00 Aug 8 cross-validation: 4 structural fixes (missing test file listing, stale test counts), Paresh Dave Mechanism #8 institution-driven alignment with opacity model, Revenue Matrix News Corp balanced tone, Condé Nast/Advance Tier 1, Aug 8 cumulative integrity (15 files), entity count stability. 7 classes, 61 tests
│   ├── test_type_d_10pm_cross_validation_aug8.py # Type D 22:00 Aug 8 end-of-day cross-validation: Google Q2 vs Meta Q2 earnings asymmetry + OpenAI publisher displacement architecture + Anthropic zero-deal paradox + financial incentive prediction coherence + stale stats fix (framing 779→782, tests 6947→7075). 9 classes, 36 tests
│   ├── test_type_d_10pm_cross_validation_aug7.py # Type D 22:00 day-end cross-validation: News Corp triple-revenue consistency, WIRED Apple-OpenAI silence, 4 asymmetry mechanisms (licensing, advertising, marketplace, professional identity capture), entity set stability (11 entities), settlement_revenue type validation, metric scale integrity, source URL presence, cumulative day integrity
│   ├── test_type_d_8pm_cross_validation_aug6.py # Type D 8 PM cross-validation: OpenAI/Apple entity escalation phases 4-5, Atlantic silence source_urls schema, Milmo profile↔research consistency, Amazon sextuple entity↔research, evening iteration coverage
│   ├── test_type_d_2pm_cross_validation_aug6.py # Type D 2 PM cross-validation: sensor-count paradox, WSJ balanced control, Google coercion-Condé Nast consistency, NYT Q2 earnings, Mims tone inversion, WSJ disclosure uniqueness, MIT TR governance
│   ├── test_type_d_aug6_cross_validation.py # Type D cross-validation (Aug 6 09:00): asymmetry gap ordering, five-mechanism taxonomy, Guardian partial independence, Advance-Reddit-Perplexity triangle, statistical direction consistency
│   ├── test_type_c_financial_landscape_aug6.py # Apple-OpenAI partnership collapse (3 phases), Google publisher class-action, UK CMA AI Overviews opt-out, Reddit deal instability, cross-platform coercion updates
│   ├── test_type_c_advance_reddit_perplexity_triangle_aug6.py # Advance-Reddit-Perplexity Triangle conflict, $550M/yr deal renewal projections, Jul 31 DMCA ruling, Reddit ad cannibalization, Amazon vs Microsoft marketplace evolution
│   ├── test_type_c_google_ad_dependency_aug6.py # Google advertising dependency coercion (quadruple structure), Alphabet Q2 2026 Network revenue ($7.3B, -0.7% YoY), NYT Q2 2026 earnings (stock -13%), Condé Nast Google traffic collapse, Advertising Dependency Paradox
│   ├── test_type_c_microsoft_openai_axis_aug6.py # Microsoft-OpenAI Financial Axis (27% ownership, 20% revenue share, $250B Azure), circular revenue flow, publisher dual exposure, Conde Nast revenue pivot (Lynch: advertising not growth engine), editorial independence paradox
│   ├── test_type_c_amazon_sextuple_leverage_aug6.py # Amazon 6-layer publisher leverage (AWS, advertising, AI licensing, Kindle, Bezos/WaPo, Anthropic $53.4B gain), double-play conflict, leverage count comparison, coverage asymmetry
│   ├── test_verge_openai_coverage_asymmetry.py # Verge × OpenAI: four-lane reporter system, io device paradox, bilateral financial flow, selective disclosure
│   ├── test_type_d_relationship_types.py # New financial relationship types validation: advertising_dependency and adversarial_litigation weights, asymmetry scorer classification, competitor-entities.yaml definitions, Verge/Atlantic Google adversarial_litigation profiles, AdX dependency admissions
│   ├── test_disclosure_audit.py # Cross-publication financial disclosure audit: WSJ unique disclosure practice (Meta + OpenAI partnerships), WIRED/FT/Atlantic non-disclosure patterns, symmetric vs asymmetric deal correlation with coverage tone, aggregate 17:0 competitor-to-Meta deal ratio validation
│   ├── test_narrative_coherence.py # End-to-end evidentiary chain validation: financial asymmetry (17:0 ratio), coverage asymmetry (4+ publications), lane assignment mechanisms (3 types), journalist cross-entity patterns (4+ reporters), control groups (News Corp balanced, Gizmodo independent), camera count paradox, source documentation, systemic non-disclosure
│   ├── test_jul7_regressions.py  # Jul 7 regressions: disclosure+PublicationProfile compat, regex backtracking, investments coercion
│   ├── test_jul8_regressions.py  # Jul 8 regressions: "mounting" escalation, auxiliary confession verbs, "largest ever" precedent
│   ├── test_confession_framing.py # Confession framing: "admitted," "conceded," voluntary-to-forced-admission reframing, false-positive exclusion
│   ├── test_delayed_defense_and_normalization.py # Delayed defense (corporate response buried late in article), industry normalization undercut (acknowledging then singling out), headline boost strength for child_safety topic
│   ├── test_government_oversight_topic.py # government_oversight topic bucket: national security, export controls, AI regulation, group_expert source detection
│   ├── test_grudging_concession.py # Grudging concession framing device (#95): positive action editorially minimized via "finally," "only after backlash," "it's about time" — framing legitimate progress as reluctant, forced, or insufficient; discovered from Gizmodo LED tamper article (Jul 8, 2026); negative guards for neutral reporting
│   ├── test_ultimatum_framing.py # Ultimatum framing device (#96): multi-stage regulatory/legal proceeding compressed into binary "do X or face Y" construction; discovered from NY Post EU DSA headline (Jul 10, 2026); cross-publication comparison (Reuters softer variant, CNN/WSJ non-matches); 6 negative guards
│   ├── test_recidivism_framing.py # Recidivism framing device (#97): entity framed as serial offender through temporal recurrence markers — "once again caught," "has a long history of violations," "serial violator," "pattern of" — distinct from repeated_disruption; 20 positive tests, 5 negative guards
│   ├── test_jun27_regression.py # Regression tests for Jun 27 fixes across multiple analysis modules
│   ├── test_hackathon_revolt.py # Wired hackathon revolt: entity, sentiment, framing, topic tests
│   ├── test_law_enforcement_outsourced.py # Law enforcement outsourced intensity: ICAC officer/agent/investigator loaded quotes, testimony-outsourced patterns, policy advocate/watchdog critique, entity detection for ICAC/Public Citizen/Report Act/CyberTipline
│   ├── test_mittr_anthropic_feud.py # MIT Tech Review Anthropic feud article: entity detection, framing, topic classification
│   ├── test_mittr_meta_hack_ai_security.py # MIT TR Meta hack AI security: Bo Li/Dawn Song/Sanmi Koyejo academic entity fix, case-sensitive Nature guard, education analogy suppression, AI agent security topics
│   ├── test_mittr_openai_open_weight_meta_pivot.py # MIT TR OpenAI open-weight models: entity clusters (OpenAI/Meta/Academic/Chinese AI/HuggingFace/AI Research Orgs), competitive_displacement framing, analogy_metaphor false-positive regression guard
│   ├── test_postpass_activation.py # Structural post-pass framing activation: analogy stacking, speculative framing thresholds
│   ├── test_precedent_analogy.py # Precedent analogy framing: opioid/tobacco/asbestos crisis comparisons, era-based villainy import
│   ├── test_resistance_patterns.py # MIT TR Resistance article patterns: catastrophizing (threat to humanity), alarm/anxiety idioms, intensity/polemical/violence loaded language, poll-based social proof, stalled-dollar and workforce-percentage scale magnitude
│   ├── test_structural_consistency.py # Structural consistency: framing device type registry completeness, total regex pattern count guard (721 patterns), doc count sync guards, test file listing guards, README/ARCHITECTURE total test count header guards (validates pytest-collected count including parametrize expansions), stale voting power purge across all doc files, cross-reference consistency (stale framing taxonomy count purge including parenthetical annotations, README topic bucket count guard), inline topic list validation (ARCHITECTURE.md, AGENT_GUIDE.md, METHODOLOGY.md topic names match code), quality standards banned phrase count and completeness guards, framing.py docstring count and device list completeness validation, ARCHITECTURE.md extended device count label guard, ARCHITECTURE.md device name list completeness (Core + Extended inline lists enumerate all device types from code), ARCHITECTURE.md test_topics bucket count guard, METHODOLOGY.md device table completeness (Extended + Structural tables vs code), METHODOLOGY.md intro tier count guard (113/10/96/7 matches code), METHODOLOGY.md §17 annotated article count and publication count guards (corpus article count and distinct publication count match actual files on disk), adversarial device type list consistency (METHODOLOGY.md + QUALITY_STANDARDS.md + AGENT_GUIDE.md + SENTIMENT_CORRECTION_REFERENCE.md + example demo scripts vs sentiment.py), stale regex pattern count purge (ARCHITECTURE.md + README.md), AGENT_GUIDE.md framing tier count guard (113/10/96/7 matches code), correction path documentation completeness (all 13 paths A-N in METHODOLOGY.md + ARCHITECTURE.md + AGENT_GUIDE.md + README.md + example demos with summary table + introductory path count/range text validated in ARCHITECTURE.md, AGENT_GUIDE.md, and METHODOLOGY.md + financial inflation ref path range), migration count guards (README.md careers_demo + EDITORIAL_HISTORIES.md both match CareerTracker), publication count floor guards (README.md + EDITORIAL_HISTORIES.md), entity cluster consistency (METHODOLOGY.md §15 cluster count matches code, table completeness with no missing/phantom clusters, alias count accuracy), ENTITY_REFERENCE.md consistency (cluster count header, alias count header, cluster completeness, no phantom clusters, custom/auto regex counts, README and ARCHITECTURE cross-references), annotated article count guard (QUALITY_STANDARDS.md vs examples/sample_output/), ARCHITECTURE.md annotated article count guard (file-tree comment vs examples/sample_output/), same-event cluster count guard (QUALITY_STANDARDS.md §10.2 Tier 1 + Tier 2 table rows), example demo adversarial type set completeness (framing_correction_demo.py + sarcastic_editorial_demo.py inline adversarial_types vs code), stale device type count purge (rejects historic device type counts in any doc that don't match the current total, including parenthetical annotations), stale journalist/multi-pub count purge (all EDITORIAL_HISTORIES.md references match current YAML counts), FRAMING_REFERENCE.md extended count consistency (tier legend + Counts by Tier table vs code), SENTIMENT_CORRECTION_REFERENCE.md adversarial count consistency (Part 1 header + Key Input Signals table + adversarial table completeness vs code), stale inline path range purge (no docs/examples files contain interrupted path ranges ending before current max path letter), framing demo docstring path completeness (framing_correction_demo.py docstring lists every correction path A-L)
│   ├── test_arena_cross_analysis.py # Cross-publication analysis: NYT vs Gizmodo on Arena story — tone separation, emotional intensity, ironic quotation filtering, agency detection
│   ├── test_latecomer_regulatory_framing.py # Latecomer narrative and regulatory shadow framing: catch-up/copycat positioning, ambient regulatory context insertion, Arena article integration
│   ├── test_editorial_deflation.py     # Editorial deflation framing: post-buildup dismissal phrases ("That's the idea, anyway"), attribution-as-skepticism, MIT TR Anduril article integration
│   ├── test_editorial_dramatization.py # Editorial dramatization framing: interpretive glosses rewriting neutral facts in dramatic language — "unexpected reality check," "massive shakeup," "turbulent transition," "did not mince words," "specifically engineered to." iPhone in Canada derivative article integration
│   ├── test_memeburn_glasses_deep_dive.py # Memeburn Meta glasses deep dive: open-ended-threat kicker patterns, ubiquitous-camera loaded language, indirect rhetorical question, Gizmodo entity detection
│   ├── test_child_safety_denial.py # Engadget child safety features: denial_contradiction with "no evidence" denials, post-quote combative attribution (said/insisted), replicated/verified evidence counters
│   ├── test_chilling_effect.py # Chilling effect social stigma framing: self-censorship patterns (too scared/afraid/embarrassed), avoidance behavior (fold up, put away), reconsidering purchase, social labeling (you're a predator), inappropriate-to-wear framing, PetaPixel Jul 14 full-text integration test
│   ├── test_worker_replacement_two_tier.py # WebProNews Meta Dublin contractors: worker_replacement_irony (trained AI that replaced them), two_tier_treatment (contractor vs full-time), geopolitical false positive fix (physical "stood firm"), outsourced_intensity expansion (labor-law expert quotes)
│   ├── test_wired_subscription_era.py # Wired Conversation Focus paywall: consumer_ownership no-adverb "runs on-device", expert_contradiction ("it's not about X; it's about Y"), loss_leader_framing ("sold at cost" + subscription revenue), editorial_aside sarcastic "Guess..." opener, Path J expert-driven structural critique correction
│   ├── test_child_safety_analysis.py # NYT child safety study analysis: new entity clusters (US Congress, Academic/Research, Research Centers, Child Safety Researchers/Legislation, Australia), source extraction fixes (case-sensitive [Aa]n?, expanded _KNOWN_ORGS, direct org attribution), new framing devices (analogy_metaphor, taxonomy_framing), agency attribution sparse-data dampening
│   ├── test_child_safety_litigation_financial_ecosystem_aug9.py # Children's safety litigation coverage financial ecosystem (Mechanism #17 — "Settle-and-Silence"): Meta disproportionate litigation coverage vs Google/YouTube KGM bellwether (70/30 split), NM $942M Meta-only ruling, Oakland $1.4T Meta-only trial, Google $200M+ cumulative settlements, MDL 3047 counsel, publisher incentive alignment, profile cross-validation
│   ├── test_type_d_10pm_cross_validation_aug9.py # Type D cross-validation (Aug 9, 22:00 PT): Sprint 19:00-21:00 mechanisms #15-#17, numbering integrity, financial direction consistency, zero-deal paradox convergence, Watchdog↔Settle-and-Silence complementarity, asymmetry scale analysis, fixed stale test counts 7922→8036
│   ├── test_type_d_04am_cross_validation_aug10.py # Type D cross-validation (Aug 10, 04:00 PT): Sprint 01:00-03:00 mechanisms #19-#21, mechanism 18-21 contiguous sequence, financial incentive scale escalation (individual→institutional→systemic), disclosure gap consistency, Meta-negative convergence through independent causal chains, causal chain non-overlap, legitimate factors discipline, Watchdog Paradox taxonomy (#16 vs #20), asymmetry score reasonability. 8 classes, 30 tests
│   ├── test_type_d_08am_cross_validation_aug10.py # Type D cross-validation (Aug 10, 08:00 PT): Mechanisms #22-#25 cross-validation, mechanism ID uniqueness, HTTPS URL consistency fixes, Amazon 6→7 layer sync, cross_publication_findings metadata completeness, infrastructure count sync. 8 classes, 23 tests
│   ├── test_type_d_09am_cross_validation_aug10.py # Type D cross-validation (Aug 10, 09:00 PT): Schema validator fixes (5→0), Mechanism #24 gap, relationship_type/coverage_prediction expansion, NYT/MITTR Anthropic consistency, Amazon 7-layer, Mechanisms #22-#25 contiguity. 8 classes, 18 tests
│   ├── test_type_d_1pm_cross_validation_aug10.py # Type D cross-validation (Aug 10, 13:00 PT): Mechanism #26-#28 cross-validation, mechanism_id consistency fixes (#23/#24/#26), test_count fix (#28 27→32), README/ARCHITECTURE count drift fix (8480→8625, 280→281), schema integrity. 8 classes, 43 tests
│   ├── test_type_d_6pm_cross_validation_aug10.py # Type D cross-validation (Aug 10, 18:00 PT): Mechanisms #30-#32 — fixed mechanism_id collision (Georgia Wells #30→#32), genre hypothesis convergence, positive control isolation, three ownership structures, contiguity #29-#32, causal chain non-overlap. 8 classes, 36 tests
│   ├── test_type_d_11pm_cross_validation_aug10.py # Type D end-of-day cross-validation (Aug 10, 23:00 PT): Mechanisms #33-#36 — mechanism_id uniqueness/contiguity, facial recognition parity, rogue AI #34↔#29 coherence, Advance aggregate, pre-IPO convergence three chains, infrastructure sync (9005/291). 8 classes, 25 tests
│   ├── test_type_d_01am_cross_validation_aug11.py # Type D cross-validation (Aug 11, 01:00 PT): parametrize counter fix (variable refs + single quotes, 8920→9107), missing mechanism_id catalog (#18/#20/#21/#22/#25), Mechanism #37 integrity, distinction_from cross-refs, new entry schema. 8 classes, 57 tests
│   ├── test_type_d_05am_cross_validation_aug11.py # Type D cross-validation (Aug 11, 05:00 PT): Full mechanism ID coverage (24 IDs, 17-40), mechanisms #38-#40 integrity, test_file existence, count sync (9292/297), 01am fix verified, no ID collisions, coverage selection legitimate factors. 9 classes, 55 tests
│   ├── test_openai_meta_facial_recognition_parity_aug10.py # Mechanism #33: Cross-Publication Facial Recognition Privacy Parity Test — OpenAI PLANNED facial recognition (always-on, cameras+mics) gets aspirational framing vs Meta DORMANT NameTag code gets alarm/investigative coverage. Financial relationships predict framing direction. 8 classes, 60 tests
│   ├── test_wired_rogue_ai_coverage_volume_asymmetry_aug10.py # Mechanism #34: WIRED Institutional Rogue AI Coverage Volume Asymmetry — Summer of Rogue AI natural experiment, 3:0 article ratio (OpenAI+Anthropic vs Meta) despite Meta least severe. Extends Will Knight + Guardian Mechanism #29. 9 classes, 42 tests
│   ├── test_advance_conde_nast_aggregate_ai_dependency_aug10.py # Mechanism #35: Advance/Condé Nast Aggregate AI Revenue Dependency — The Omni-Deal Publisher. 6 AI revenue channels across 5 companies (OpenAI, Microsoft, Amazon, Perplexity, Reddit/Google, Apple News+), Meta excluded from all. ~$7.2B total exposure. 8 classes, ~35 tests
│   ├── test_pre_ipo_owner_investor_publisher_convergence_aug10.py # Mechanism #36: Pre-IPO Owner-Investor-Publisher Convergence. 3 Anthropic investor→media owner chains (Bezos/Amazon→WashPost, Benioff/Salesforce→Time, HarperCollins/News Corp→settlement). 3-hop vs 1-hop disclosure asymmetry. Pre-IPO amplification. 9 classes, ~51 tests
│   ├── test_open_weight_policy_coverage_selection_asymmetry_aug11.py # Mechanism #37: Open-Weight Policy Coverage Selection Asymmetry. Trump WH exempt open-weight from safety testing (Aug 4). WIRED/Verge covered rogue AI but skipped Meta-favorable exemption. WSJ (balanced deals) covered both. Coverage rate: OpenAI-only 0/2, no-deal 4/4, balanced 1/1. 12 classes, 46 def tests (55 parametrized)
│   ├── test_mit_tr_anduril_meta_warfare_glasses.py # MIT TR Anduril/Meta warfare glasses: defense-tech entity detection, failure_precedent (new device), analogy_stacking FP filters (factual similes, recall verb), context-gated Llama entity, selective_rehabilitation, editorial_deflation, sentiment calibration
│   ├── test_mit_tr_anthropic_preipo_product_validation_aug9.py # MIT TR × Anthropic pre-IPO product validation asymmetry (Mechanism #15): fascinated/validating Anthropic framing (J-space, Claude Science, Code with Claude, 10 Breakthroughs) vs failure/warfare/dismissive Meta framing, max headline valence gap (1.0), competence-benchmark device, indirect endowment financial chain, pre-IPO amplification timeline
│   ├── test_mit_tr_apple_governance_conflict_aug6.py # MIT TR × Apple governance-level conflict analysis: Bergeron MIT Corporation election, CSAIL Alliance membership, Apple privacy-positive vs Meta adversarial tone asymmetry, sensor-count paradox (Vision Pro 30+ praised vs Meta 4 surveilled), non-disclosure, three-tier influence hierarchy, profile cross-validation
│   ├── test_mit_tr_apple_wwdc_2026_pcc_omission_aug11.py # MIT TR × Apple WWDC 2026 PCC-to-Google-Cloud coverage omission (Mechanism #41): WWDC 2024 favorable baseline, WWDC 2026 PCC shift omission, Meta-Anduril warfare contrast, Apple 3 camera wearables privacy silence, Bergeron governance timing, 5 confounding factors, mechanism registration, cross-mechanism validation. 9 classes, 41 tests
│   ├── test_multi_outlet_comparison.py # N-way cross-outlet same-event comparison: compare_multi_articles() function validation, 4-way Zuckerberg town hall cross-analysis (Reuters/TechCrunch/Barron's/PYMNTS), cross_publication_import detection, tone matrix generation, QUALITY_STANDARDS Tier 1 update guard
│   ├── test_quote_forward_preference.py # Quote extraction forward-preference fix: _extract_nearby_quote prefers forward quotes over backward, regression test for Ji/Gong misattribution bug in MIT TR AI agent security article
│   ├── test_muse_image_deflation.py # iPhone-in-Canada Muse Image rollout: editorial_deflation (better-late-than-never idiom, I-guess hedge, conditional deflation, trailing minimizer), rhetorical_question (Who's-actually contraction), latecomer_narrative (saving-you-steps-from, competitor listing), integration test for closing-paragraph device cluster
│   ├── test_bloomberg_muse_image_entities.py # Bloomberg Muse Image entity extraction: SpaceXAI→xAI cluster mapping, Anthropic PBC→Anthropic alias, CoreWeave Inc/Alphabet Inc's Google/Oracle Corp corporate suffix extraction
│   ├── test_wsj_ai_spending_sources.py # WSJ AI spending article source extraction: Pattern 0c "Name of Org VERB" (KeyBanc Capital fix), Pattern 0d reverse "VERB Name of Org" (Jefferies fix), Pattern 0e "Org analyst Name VERB" (Bernstein Research affiliation fix), full-text expert detection fallback
│   ├── test_compound_attribution_verbs.py # Compound negative attribution verb detection: contrastive failure/concession/defensive failure multi-word phrases, classification priority over single-word lookup
│   ├── test_litigation_cascade.py # Litigation cascade regression tests: multi-jurisdiction cascade detection, escalation patterns, threshold validation, negative cases
│   ├── test_litigation_framing_pronoun_guard.py # litigation_framing pronoun guard: colloquial "sue me/him/us/them" suppression via negative lookahead, genuine named-entity litigation preserved, mixed-context edge cases
│   ├── test_techcrunch_muse_image_fixes.py # TechCrunch Muse Image privacy article: "Muse Video" product-name source false positive, Cambridge Analytica entity cluster separation, "landmark" literal-usage loaded_language suppression
│   ├── test_ibd_meta_cloud_sources.py # IBD Meta cloud article source extraction regression tests
│   ├── test_ibd_sticker_shock.py # IBD open-source AI article: competitive_deficit framing (acknowledges defeat, catch up to, fill the vacuum), single-surname affiliation full-text fallback, conditional org source filter, D.A. Davidson entity detection
│   ├── test_superintelligence_org_suppression.py # Topic classification: "Superintelligence Labs" proper-noun suppression for ai_ethics_safety, Reuters Muse Image wire false positive fix
│   ├── test_success_paradox.py   # success_paradox framing: "hit even as concerns pile up," "popular despite prickly climate," "nearly doubled but backlash," "growth doesn't mean tipping point" — positive commercial data used as Trojan horse for negative framing. Gizmodo EssilorLuxottica Q2 article (Jul 30, 2026)
│   ├── test_safeguard_inadequacy.py # safeguard_inadequacy framing (#111): introduces privacy safeguard (LED, opt-out, deletion) then systematically undermines as insufficient — "privacy light but people might not see it," "growing market for disabling indicators," "option no longer available," "services to alter glasses," "no real opt-out," "security theater." 9to5Google (Jul 7), Northeastern (Jun 22), LiveMint, Laptop Mag
│   ├── test_reuters_french_antitrust.py # Reuters French antitrust: "The Information" case-sensitive false positive fix, French media association entities (DVP/APIG/Le Monde/Les Echos), content_licensing topic bucket, acronym org source extraction with appositive clause
│   ├── test_reuters_french_antitrust_jul8.py # Reuters French antitrust publishing fees Jul 8: escalation_amplification framing (trend magnification), precedent_analogy framing (enforcement precedent citing), content_licensing as primary topic, French media entity clustering (DVP/APIG/Le Monde/Les Echos), Alphabet/Google cluster
│   ├── test_reuters_eu_dsa_meta_jul10.py # Reuters EU DSA Meta addictive features Jul 10: entity detection (EU Commission, European Commission cluster), regulatory framing devices, sentiment scoring for wire-service DSA coverage, cross-article comparison
│   ├── test_fastco_meta_glasses_2026_07_10.py # Fast Company Meta AI glasses controversies roundup Jul 10: EFF 3-word org name extraction fix (_KNOWN_ORGS), C-suite title affiliation (CEO/CTO pattern 0b), hyphenated surname dedup (endswith-hyphen check), VADER polarity inversion (raw +0.633 → corrected −0.5217)
│   ├── test_foxbusiness_meta_1_4t_penalty.py # Fox Business Meta $1.4T penalty Jul 7: editorial_cross_promotion framing device (new — all-caps interstitial blocks), reached_out_for_comment no_comment source pattern (new), valuation_comparison detection, litigation/child_safety topic assignment, structural consistency guard (87 pattern-matched device types)
│   ├── test_foxbusiness_muse_image_shutdown.py # Fox Business Muse Image shutdown Jul 11: editorial_cross_promotion regex fix (dollar signs/digits in all-caps callouts), policy_reversal controlled retreat patterns (new — "missed the mark"/"no longer available"), loaded_language "misuse" addition, dollar-sign regression guard
│   ├── test_guardian_cohere_correction.py # Guardian Cohere lawsuit correction Jul 11: factual correction — Guardian News & Media Limited is a NAMED PLAINTIFF in Advance Local Media v. Cohere (SDNY 1:25-cv-01305), contradicting previous "strategic_licensing_over_litigation" classification. Tests: triple_path_ai_strategy reclassification, Cohere MTD denial (McMahon, Nov 13 2025), Observer/Tortoise transfer date (Apr 22 2025), Richard Furness GMG→Tortoise personnel migration, Brittin BBC-Channel 4 partnership, NYT v OpenAI MDL 3143 cross-reference, co-plaintiff verification
│   ├── test_guardian_cross_entity_aug6.py # Guardian cross-entity deep dive Aug 6: Stargate UK FOI investigation (adversarial OpenAI coverage despite deal), rogue agent "going rogue" framing, Brittin revolving door, ProRata/Meta Llama paradox, partial independence model, balanced_to_adversarial tone reclassification, cross-publication asymmetry comparison
│   ├── test_adi_robertson_cross_entity.py # Type B 05:00 Aug 8: Adi Robertson (The Verge) Comfort/Discomfort Paradox — Meta products receive deficit framing (Quest Pro 2/5 "irredeemably bad") while competitors with equal limitations get improvement framing (ML2 "sharp and vibrant" same year). Privacy Conditional Pattern: privacy-conditional language applied exclusively to Meta despite Apple VP having 12 cameras. Institutional amplification post-Heath departure. PMC acquisition context. Cross-desk consistency with Chokkattu/Ashworth Creep Paradox. 9 classes, 34 tests
│   ├── test_alex_heath_cross_entity.py # Alex Heath (The Verge Deputy Editor) cross-entity: Access Paradox — same Decoder CEO interview format for Meta (Zuckerberg) and OpenAI (Nick Turley, Bret Taylor) but adversarial investigative lens only for Meta; deputy editor weight amplifies asymmetry; beat separation (Hayden Field=OpenAI, Heath=Meta); four-lane system Meta-specific; financial correlation (PMC-OpenAI deal, no Meta deal); io device paradox; Snap Spectacles constructive framing; selective disclosure; Command Line newsletter; mechanism #5
│   ├── test_zuckerberg_ai_agents_same_event.py # Reuters vs Barron's same-event comparison on Zuckerberg AI agent admission (Jul 2, 2026 town hall): emotion_attribution framing device (new — editorial attribution of emotional states never expressed by subject), competitive_deficit detection, confession_framing divergence, entity detection (Claude Code, Alexandr Wang, Muse/Spark), topic classification, source extraction (documentary "recording heard by Reuters"), same-event framing divergence analysis
│   ├── test_reuters_rust_belt_jul9.py # Reuters Big Tech data centers Rust Belt factories Jul 9: heritage_nostalgia framing device (new — age/generational continuity establishing emotional stakes), source false positive elimination (Capacity/Energy Consumers/White House/Synergy Research/Smart Electric Power), Pattern 0f affiliation extraction ("president of the trade group Industrial Energy Consumers of America"), environmental domain keyword in affiliation patterns, infrastructure_energy topic assignment
│   ├── test_reuters_scam_ads_securities_jul13.py # Reuters Meta scam ads securities defense Jul 13: power_asymmetry personal-loss savings narrative ("retirement savings"), loaded_language additions ("depressingly", "peculiar"), self_referential_investigation "my [Publication] colleagues" pattern (with source_publication wire-service filter), editorial_dramatization literary-aside undercut ("— while it lasted"), rhetorical_question "Should [entity]... hinge" pattern, entity extraction (Meta cluster with Facebook/Instagram/WhatsApp subsidiaries), sentiment negative lean
│   ├── test_reuters_australia_esafety_child_safety_jul14.py # Reuters Australia eSafety child safety Jul 14: iMessage → Apple cluster (new alias), Google Messages → Google cluster (new alias), Discord cluster (new), Julie Inman Grant → Australia cluster (new alias), multi-entity distribution (7+ clusters, Australia primary), framing: no_comment_implication, regulatory_shadow, scale_magnitude, catastrophizing
│   ├── test_reuters_meta_ai_layoff_discrimination_jul14.py # Reuters Meta AI layoff discrimination Jul 14: District of Columbia entity resolution (not Columbia University), legal-context loaded_language suppression (violating/retaliation as legal terms of art), legal-context absence_as_evidence suppression (plaintiff allegation vs journalistic framing), standalone "slashed" loaded_language verb
│   ├── test_foxbusiness_meta_ai_layoff_discrimination_jul14.py # Fox Business Meta AI layoff discrimination Jul 14: publication self-reference source extraction ("told Fox Business"), legal-context emotional_appeal suppression ("disability" as ADA descriptor), editorial_cross_promotion for embedded all-caps links
│   ├── test_wsj_meta_smartglasses_jul15.py # WSJ Meta smartglasses privacy Jul 15: surveillance_creep (5 patterns), market_flooding (4 patterns), voice-command ironic_quotation suppression, fitness-tracking loaded_language suppression, comma-before-verb source extraction ("Bosworth, said"), title affiliation false positive filter ("Chief Executive"), institutional suffix filter ("Liberties Union, said")
│   ├── test_wsj_ai_backlash_exec_threats_jul16.py # WSJ AI backlash exec threats Jul 16: multi-entity extraction (Anthropic, OpenAI, Meta, Palantir), escalation_amplification, no_comment_implication, trend_bundling, tone correction gap (reported-violence), xfail: ceo_personalization, scale_magnitude, humanization
│   ├── test_wsj_meta_ai_layoff_discrimination_jul14.py # WSJ Meta AI layoff discrimination Jul 14: independent expert source extraction (Prof. Hirsch, UNC), corporate spokesperson, lawsuit-as-documentary source, litigation_framing, timeline_implication, entity clustering, source diversity
│   ├── test_wsj_essilorluxottica_q2_smartglasses_boom_2026_07_28.py # WSJ EssilorLuxottica Q2 smartglasses Jul 28: inverted success_paradox ("Slows Despite Boom"), editorial_deflation deceleration framing, grudging_concession uncertainty injection, scale_magnitude, cross-pub comparison with Reuters
│   ├── test_reuters_iris_chip_jul9.py # Reuters Meta Iris chip production Jul 9: Sumitomo Electric entity cluster (new), inverted analyst attribution ("Morgan Stanley analysts said"), compound no-comment subject extraction ("Samsung Electronics and Sumitomo Electric did not respond"), "floundered" passive framing term, ai_development + corporate_strategy topic classification
│   ├── test_reuters_muse_spark_11_jul9.py # Reuters Muse Spark 1.1 developer preview Jul 9: pathologizing_metaphor "intervention" false positive suppression (neutral technical context — "less human intervention", "without intervention"), pricing comparison phrases in NEGATIVE_COMPARISON/POSITIVE_COMPARISON ("above openai", "below anthropic", "priced above/below", "cheaper than", "undercuts"), loaded_language competitive dramatization ("heated competition", "AI supremacy", "tech arms race"), competitive_positioning "pitting...against" and "close/narrow the gap"
│   ├── test_recovery_narrative.py # Recovery narrative framing device (#94): three-beat decline→catalyst→recovery structure in financial articles, bidirectional competitive_positioning (positive parity variant), confidence scoring, negative guards for neutral wire articles and decline-only articles; discovered from MarketWatch Meta stock rebound article (Jul 10, 2026)
│   ├── test_register_muse_image_superintelligence_jul13.py # The Register Muse Image "superintelligence" (Jul 13): confession_framing scare-quoted gap, editorial_deflation temporal deflation (long noun phrase gap), recidivism_framing sardonic competence enumeration, ceo_personalization modifier adjectives ("Zuck's latest big bet"), editorial_aside, consent_alarm, loaded_language, policy_reversal, sarcastic_correction
│   ├── test_speculative_quote_suppression.py # Speculative framing quote-context suppression: _find_quoted_spans helper, _is_in_quoted_span helper, editorial prose hedges still fire at 5+ threshold, analyst quotes suppressed (straight + smart quotes), mixed editorial/quoted context, BofA research note style, Motley Fool editorial hedging
│   ├── test_controlled_retreat_language.py # Controlled retreat language detection: policy_reversal subtype for corporate damage-control statements (intent displacement, active listening performance, target-miss euphemism, passive unavailability, control reassurance, useful-tool salvage); discovered from Reuters Meta Muse Image discontinuation (Jul 10, 2026)
│   ├── test_datacenter_framing_jul13.py # WSJ Meta Louisiana data center $50B (Jul 13): escalation_amplification intervening adjective, loaded_language gambling/infrastructure-burden/magnitude patterns, recovery_narrative revitalization idioms
│   ├── test_barrons_splurge_jpmorgan_jul13.py # Barron's Meta AI Splurge JPMorgan Jul 13: pathologizing_metaphor "splurge" variants (6), competitive_deficit "compared with" bridge pattern (7), J.P. Morgan period-variant entity detection (4), Epoch AI entity detection (2)
│   ├── test_barrons_1t_child_safety_backlash_jul10.py # Barron's $1T child safety backlash Jul 10: Roblox entity cluster (3), scale_magnitude N-figure idiom "13-figure penalty" (4), loaded_language "ripe/easy/prime target" (4), investor_advisory (3), catastrophizing (1), pathologizing_metaphor (1), emotional_appeal (1), refusal_amplification (2), 4 xfail known gaps
│   ├── test_buzzfeed_smart_glasses_womens_safety_jul14.py # BuzzFeed smart glasses women's safety Jul 14: Meta/Facebook cluster, GDPR EU Regulatory, 13 framing device types, Refuge affiliation cross-paragraph bleed bug, VADER polarity inversion (+0.64 for manual −0.55), 11 xfail known gaps
│   ├── test_marketwatch_smart_glasses_convince_jun27.py # MarketWatch smart glasses market skepticism Jun 27: CRITICAL VADER +0.65 vs manual −0.20 (largest polarity inversion in corpus), professional skepticism genre, all 3 sources unanimously skeptical, 8 xfail, candidate Path O
│   ├── test_foxbusiness_louisiana_datacenter_jul13.py # Fox Business Meta Louisiana datacenter $50B Jul 13: recovery_narrative broadened "reshaping [ProperNoun] Parish" + "transforming [institution]", loaded_language "life-altering", full article regression
│   ├── test_ibd_morgan_stanley_capex_jul13.py # IBD Morgan Stanley CapEx Jul 13: escalation_amplification social/political/consumer/national adjectives (11), market_verdict penalizing/punishing/discounting (8), recovery_narrative proper-noun fix (4), Morgan Stanley + SpaceX entities (3)
│   ├── test_ibd_wedbush_hyperscalers_2026_07_16.py # IBD Wedbush hyperscalers Jul 16: Reddit/eBay entity clusters (2), Trainium3 Amazon cluster (1), "the [Org] analyst" corporate spokesperson fix (1), analyst-preference competitive_positioning framing (4 patterns), full-article integration
│   ├── test_washexaminer_meta_louisiana_50b.py # WashExaminer Meta Louisiana $50B Jul 13: scale_magnitude physical-unit patterns (5), sovereignty_framing American patriotic (3), anonymous_authority singular person fix (2), source extraction corporate title stop-words (2), isolated regression tests (4)
│   ├── test_usatoday_meta_ai_layoff_discrimination_jul15.py # USA Today Meta AI layoff discrimination Jul 15: litigation_framing (1), precedent_framing (1), anthropomorphization (1), entity Meta cluster (3), documented gaps scale_magnitude/escalation/cross_case_citation (3), Workday cross-case reference (3), expert source architecture (2), same-event structural contrasts (4)
│   ├── test_nypost_meta_ai_layoff_discrimination_jul14.py # NY Post Meta AI layoff discrimination Jul 14: bloodbath loaded_language workforce context (2), root_out/weed_out hunting vocabulary (2), ceo_personalization Zuckerberg's Meta (1), trend_bundling/competitive_guilt_transfer capex tail (1), juxtaposition AI spending vs layoffs (1), entity detection Meta/Apple/Zuckerberg (3), Challenger entity xfail ampersand gap (1), negative tone (1), litigation+workplace topics (2)
│   ├── test_analyticsinsight_meta_ai_layoff_discrimination_jul15.py # Analytics Insight Meta AI layoff discrimination Jul 15: hypocrisy_frame precedent-in-legal-context suppression (1), entity detection Meta cluster (1), sentiment legal article tone (1)
│   ├── test_techcentral_smartglasses_glassholes_jul14.py # TechCentral smart glasses privacy editorial Jul 14: negated loaded_language suppression "not a gimmick" (5), editorial conclusion ironic_quotation suppression (3), source extraction false positive suppression Name Tag/Balance/Name (3), entity detection Warby Parker/Be My Eyes/BBC (8), sentiment opinion editorial (4), framing device accuracy (8)
│   ├── test_nypost_meta_child_safety_monitoring_jul16.py # NY Post Meta child-safety chatbot monitoring (Jul 16): outsourced_intensity protective-context guard (crisis helpline, parental alerts), Path N sentiment correction (positive-action negative-domain VADER inflation: raw -0.541→corrected -0.08)
│   ├── test_meghan_bobrowsky_cross_entity.py # Meghan Bobrowsky (WSJ) cross-entity: Balanced-Control Beat Assignment Model — dedicated Meta beat reporter at ONLY pub with symmetric financial ties ($50M Meta + $50M OpenAI). Tone: −0.15 vs Hill −0.80 (0.65 gap) / Goode −0.85 (0.70 gap) — largest single-journalist delta. WSJ beat structure (Bobrowsky→Meta, Jin→OpenAI, McMillan→Cybersecurity, Mims→Columnist). Beat assignment neutral; asymmetry from financial environment. 9 classes, 36 tests
│   ├── test_bobrowsky_smart_glasses_entity_targeting_aug11.py # Mechanism #49 — Bobrowsky Smart Glasses Privacy Entity-Targeting Concentration (Type B, Aug 11 15:00 PT): same pub, same topic, same 3-week window. Bobrowsky deep Meta glasses privacy investigation (Jul 14) vs Samsung Galaxy Glasses IDENTICAL hardware (Jul 22, same Snapdragon AR1 Gen 1, 12MP camera, LED, Google Gemini AI) — ZERO Samsung privacy investigations. Mims balanced all-companies column (Jun 26) isolates beat assignment as structural mechanism. News Corp balanced deals rule out financial driver. 6 confounding factors + testable prediction. 9 classes, 36 tests
│   ├── test_apple_news_platform_leverage_aug7.py # Apple News+ platform leverage — Lifeline Paradox: Apple has FIVE financial mechanisms (News+ 50% rev share $12.99/mo 400+ titles 125M MAU, App Store 15-30% tax, Apple One dilution, 2.5B-device distribution monopoly, $1B/yr AI bypass via Google Gemini). THIRD most entangled after Microsoft (7) and Amazon (6). Completes hierarchy: MSFT(7)>AMZN(6)>AAPL(5)>GOOG(4)>META(1). Profiled pub exposure: Condé Nast 16 titles, Atlantic "most valuable syndication partner", WSJ participant, FT only non-participant. Q3 FY26 $30.7B Services +12% YoY. 9 classes, 37 tests
│   ├── test_openai_publisher_financial_displacement_aug8.py # OpenAI publisher financial displacement architecture: ad business launch Jan 2026, $100M ARR pilot in 6 weeks, $2.5B projected 2026 → $100B 2030, Chris Lehane dual role (ads+TBPN). TBPN acquired Apr 2 2026 (11 people, 70K daily viewers, $30M/yr). Publisher deals 20+ covering 160+ outlets, $300-400M/yr total, News Corp largest $250M/5yr. Ad rev exceeds deal spending 6-8× in 2026. OpenAI S-1 filed Jun 8 2026 $852B val. Anthropic S-1 filed Jun 1 2026 $965B val ZERO publisher deals — validates zero-deal model. Dual-IPO $1.8T+ combined, transparency inflection. 9 classes, 66 tests
│   ├── test_news_corp_factiva_marketplace_dual_role_aug9.py # Type C: News Corp Factiva AI Marketplace Dual-Role — Factiva sells AI licensing rights to 8,100+ sources (>25% of Factiva), making News Corp dual role: publisher + marketplace operator. WSJ self-disclosure. 4 marketplace operators conflict ranking (MS PCM highest, Amazon high, Factiva medium, Snowflake lowest). Q4 FY2026 cross-validation. 8 classes, 41 tests
│   ├── test_publisher_ai_revenue_materiality_aug9.py # Type C: Publisher AI Revenue Materiality Index — SEC-filed AI licensing revenue from Q1-Q2 2026 earnings. News Corp Q4 FY2026 ($2.34B +11%, $230M NI +167%), People Inc Q2 ($436.7M, Meta deal primary licensing driver), USA Today Co Q1 ($33.75M other digital +125.6%), NYT Q1 ($45.2M affiliate/licensing — AI commingled), Wiley Q2 (~$100M cumulative AI training). Condé Nast Opacity Paradox: 4 competitor deals, zero disclosed terms, -0.85 Meta tone, zero SEC obligation. 9 classes, 64 tests
│   ├── test_cecilia_kang_cross_entity.py        # Type B: Cecilia Kang (NYT) cross-entity — Mechanism #9B (Parallel Beat Reinforcement). Co-author of 'An Ugly Truth' with Frenkel, shares seven-figure book deal. Regulatory/policy beat (DC) vs Frenkel's cybersecurity (SF) creates dual-beat adversarial pipeline. Meta -0.50, Google -0.05, OpenAI +0.05. 5 patterns: dual-beat pipeline, headline naming asymmetry, regulatory circularity, partnership-enforcement toggle, thesis lock-in. 7 classes, 46 tests
│   ├── test_guardian_google_sid_governance_capture_aug10.py  # Type A: Guardian × Google — Mechanism #17 (SID Governance Capture Privacy Scrutiny Inversion). Brittin (Google EMEA 18yrs) → Guardian SID → BBC DG. Compound dependency: advertising + AI pilot + revolving door vs Meta $0. Android XR glasses feature parity with Ray-Ban, no equivalent scrutiny. 8 classes, 46 tests
│   ├── test_guardian_rogue_ai_volume_asymmetry_aug10.py  # Type A: Guardian × OpenAI — Mechanism #29 (Rogue AI Coverage Volume & Temperature Asymmetry). Same-event natural experiment: OpenAI/Anthropic/Meta all disclosed Irregular containment breaches Jul–Aug 2026. Milmo published 4 standalone OpenAI rogue AI articles, 0 Meta despite identical disclosure. Big tobacco framing for Meta child safety vs factual relay for OpenAI rogue AI. Coverage aligns with OpenAI deal (Feb 2025) and absent Meta deal. 8 classes, 30 tests
│   ├── test_georgia_wells_cross_entity.py  # Type B: Georgia Wells (WSJ) — Mechanism #30 (Disclosure-Correlated Editorial Independence). Dual-beat reporter covers OpenAI adversarially (AG investigation, rogue AI) despite News Corp $250M+ deal; Meta with neutral business register. Positive control: WSJ disclosure correlates with balanced coverage vs undisclosed-relationship pubs. 7 classes, 27 tests
│   ├── test_alex_reisner_cross_entity.py         # Type B: Alex Reisner (The Atlantic) cross-entity — Mechanism #16 (Training Data Investigative Target Gradient). Atlantic AI Watchdog investigates pirated training data, but employer has OpenAI content deal (May 2024). Books3 and LibGen coverage: Meta foregrounded in every headline/subhead, OpenAI absent or backgrounded with denial accepted at face value. ~90% narrative allocation to Meta despite both companies using same pirated libraries. Music investigation company-neutral (Suno target) = control case. Watchdog Paradox: investigates piracy at publication that licenses content to a pirate. 8 classes, 49 tests
│   ├── test_kate_clark_cross_entity.py            # Type B: Kate Clark (WSJ startup/VC desk) cross-entity — Mechanism #27 (Startup Desk vs. Corporate Desk Narrative Segregation). Clark covers Anthropic with hero-arc templates (+0.45 tone) while Bobrowsky covers Meta with accountability templates (-0.15 tone). 0.60-point gap within same publication from desk/genre assignment, not financial incentive. Distinct from Mechanism #26. 8 classes, 38 tests
│   ├── test_kate_knibbs_cross_entity.py           # Type B: Kate Knibbs (WIRED) cross-entity — Mechanism #20 (Dual Watchdog Paradox). Industry's definitive AI copyright record-keeper (tracker cited in federal court NDCA, CA Assembly AB 412, academic papers) works for Condé Nast which SELLS training data to OpenAI/Amazon/Microsoft/Apple. $0 Meta, $0 Google. Meta headline prominence in shared lawsuits (Books3), dismissive product reviews, accusatory data coverage. OpenAI secondary in shared cases. Two-layer paradox: Condé Nast → OpenAI + Advance → Reddit (65.2% voting) → OpenAI/Alphabet. Record-keeper role = outsized discourse influence. 8 classes, 29 tests
│   ├── test_ipo_underwriter_research_laundering_aug10.py  # Type C: IPO Underwriter Research Laundering Pipeline — Mechanism #21. GS+MS lead BOTH Anthropic+OpenAI IPOs (unprecedented), research divisions produce AI reports cited as independent analysis. Bank stocks fell 4-5% on OpenAI delay news. Meta zero IPO fees. Reddit Q2 data licensing verified. Anthropic secondary $1.2T. 8 classes, 42 tests
│   ├── test_type_d_09am_cross_validation_aug11.py # Type D cross-validation (Aug 11, 09:00 PT): Mechanisms #42/#43 cross_publication_findings placement, publications section clean (no mechanism_ids), snap entity in competitor-entities.yaml, 05am stale assertion prevention (>= not ==), structural count sync. 9 classes, 26 tests
│   ├── test_type_d_5pm_cross_validation_aug11.py # Type D cross-validation (Aug 11, 17:00 PT): FT unification, mechanisms 42-50 required fields, no duplicate mechanism IDs, Heikkilä cross-entity canonical key, publications count 9, Aug 11 mechanisms have test files. 21 tests
│   ├── test_type_d_8pm_cross_validation_aug11.py # Type D cross-validation (Aug 11, 20:00 PT): Mechanism #41 relocation, date_added completeness #51-53, full ID coverage 17-53, no mechanism IDs in publications, README/ARCHITECTURE sync, previous fixes regression check. 27 tests
│   ├── test_wired_apple_pcc_privacy_pivot_coverage_asymmetry_aug11.py # Mechanism #44: WIRED Apple PCC-to-Google-Cloud Privacy Pivot Coverage Selection Asymmetry. 11-day window (Jun 4-15 2026), 3+ NameTag investigations vs ZERO Apple PCC-to-Google-Cloud coverage. Makeover framing on Uncanny Valley podcast Jun 11. Financial prediction: Condé Nast Apple Intelligence negotiations (~$50M) + Apple News+ (16 titles); Meta $0. 8 legitimate factors. 9 classes, 43 tests
│   ├── test_wired_openai_ad_coverage_selection_gap_aug11.py # Mechanism #48: WIRED OpenAI ChatGPT Ad Business Coverage Selection Gap. ZERO standalone WIRED articles covering OpenAI ChatGPT ad business launch (Jan-Aug 2026) while 20+ other outlets covered extensively. $100M annualized in 6 weeks, conversation data targeting, former Meta execs (Simo/Dugan), user backlash (+132% uninstalls, Claude 11x surge). Condé Nast OpenAI deal predicts gap; Meta $0 deals. 7 legitimate factors. 10 classes, 53 tests
│   ├── test_wired_copyright_piracy_framing_parity_aug11.py # Mechanism #51: WIRED Copyright Piracy Framing Parity — Anthropic vs Meta. Both pirated books from LibGen; Judge Alsup ruled identically (training = fair use, piracy ≠ fair use). Meta gets morally-loaded piracy/theft framing, Anthropic gets market-focused settlement framing. Condé Nast $0 Meta deal, $5-10M/yr OpenAI deal, Amazon deal (Anthropic's $53.4B investor). Financial exclusion predicts moral framing. 8 classes, 26 tests
│   ├── test_hayden_field_ai_beat_concentration_aug11.py # Mechanism #52: Hayden Field AI Beat Concentration at The Verge. Senior AI reporter (Jun 2025) with mandate covering 6 AI companies equally; actual portfolio ~15+ OpenAI/Anthropic vs ~2-3 Meta AI articles. Aspiration framing for Anthropic, follower/deficit framing for Meta. THIRD instance of AI beat concentration pattern (Metz/NYT, Knight/WIRED). PMC has OpenAI deal + Azure enterprise agreement, no Meta deal. 10 classes, 48 tests
│   ├── test_openai_triple_layer_journalism_funding_aug11.py # Mechanism #53: OpenAI Triple-Layer Journalism Funding Architecture. THREE simultaneous financial channels: Layer 1 content licensing (20+ publishers, 160+ outlets), Layer 2 salary funding (Axios 4→13 cities, Lenfest $10M 5 newsrooms), Layer 3 philanthropic grants (AJP $10M+$8M credits, 50+ nonprofits, 38 states). No tech co has all three levels. Meta mirror: ended $105M News Tab (2022), killed Bulletin (2023), zero post-2022. 7 factors, 4 predictions. 10 classes, 65 tests
│   ├── test_ashworth_wwdc_pcc_privacy_framing_aug11.py # Mechanism #45: Boone Ashworth (WIRED) journalist-level privacy framing asymmetry — same reporter uses "mass surveillance" for Meta glasses (Business Wars podcast Jun 3 & 10) and "AI partnership" for Apple PCC-to-Google-Cloud (WWDC roundup Jun 8) in same 8-day window; 0.95 tone delta; extends Mechanism #44 from publication to individual journalist level. 10 classes, 46 tests
│   ├── test_pre_ipo_underwriter_client_publisher_convergence_aug11.py # Mechanism #46: Pre-IPO Underwriter-Client-Publisher Financial Convergence — Goldman Sachs, Morgan Stanley, JPMorgan Chase simultaneously (1) lead Anthropic ~$1T IPO (Oct 2026), (2) enterprise Claude customers (GS: embedded engineers, JPM: 230K employees), (3) major financial publication advertisers. SEC terminated GRAS Dec 2025 (10 months pre-IPO), replacing prescriptive structural mandates with principles-based FINRA Rule 2241. SpaceX fee precedent: $500M total, ~$100M per lead bank. Meta IPO 2012 = zero current underwriter entanglement. 12 classes, 44 tests
│   ├── test_meta_ad_competitor_structural_antagonism_aug11.py # Mechanism #47: Meta Ad Revenue Competitor Structural Antagonism Index — Meta projected $243.46B 2026 ad revenue (surpassing Google for first time). Meta is ONLY entity among 7 profiled that is pure ad competitor with zero publisher revenue. Structural antagonism matrix, Condé Nast CEO "no longer expects advertising to be a growth engine", publisher ad decline. 9 classes, 52 tests
│   ├── test_privacy_innovation_attribution_inversion_aug11.py # Mechanism #55: Privacy Innovation Attribution Inversion — cross-journalist framing of Meta's industry-first camera-disable feature (Jul 7 2026, "No other kind of camera has done this") vs Samsung Galaxy Glasses privacy toggle (Jul 22, neutral) vs Apple smart glasses delay (Jul 26, aspirational). Same privacy concern, inverted framing by company. Ben Schoon (9to5Google "privacy nightmare"), Chandra Steele (Android Police "but women's safety"), Digital Trends ("creep's weapon"), PetaPixel (reactive), Gizmodo/Barr (Samsung neutral), WebProNews (Apple "reckoning"), Fast Company ("The Problem"). 6 confounders, 3 testable predictions. 9 classes, 56 tests
│   └── fixtures/
├── pyproject.toml
├── requirements.txt
├── iteration-log.md
└── LICENSE
```
