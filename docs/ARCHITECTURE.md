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

The toolkit uses a multi-layer correction pipeline with **12 distinct paths (A–L)** that addresses known VADER/TextBlob blind spots when scoring editorial prose:

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
                                 (106 device types, 720 compiled regex)
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
        Path A   Path B    Path C  Path E  Path D  Path F  Path H  Path I  Path J  Path K  Path L
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

Only one framing path (A–F, H–L) fires per article. Path G runs independently before the composite is computed, correcting VADER's input signal. See [METHODOLOGY.md §9.2](METHODOLOGY.md#92-correction-pipeline) for full trigger conditions, blend formulas, and discovery articles.

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
- **106 framing device types** organized in three tiers:
  - **Core (10):** guilt by association, anonymous authority, catastrophizing, false balance, selective omission signal, emotional appeal, loaded language (including workplace coercion/revolt terms), power asymmetry, CEO personalization, litigation framing
  - **Extended (89):** straw man, refusal amplification, juxtaposition (including investment-near-layoffs), timeline implication, military techno-optimism, selective rehabilitation, rhetorical question, ironic quotation, isolation framing, pressure language, self-referential investigation (publication citing its own prior reporting as evidence within adversarial coverage), geopolitical regulatory pressure, sovereignty framing, scale/magnitude framing, corporate reassurance undercut, hypocrisy frame (singling out an entity as the sole holdout among peers, framing inaction as moral failing), sarcastic correction (editorial sarcasm that mockingly concedes a point before retracting it), outsourced intensity (loaded language in legal filings/complaints quoted by neutral editorial prose), precedent analogy (editorial device importing settled villainy from prior crises — opioid, tobacco, asbestos — onto a current subject via era-based comparisons), confession framing (editorial device presenting corporate acknowledgments as forced admissions — "admitted," "conceded," "finally acknowledged" — reframing voluntary statements as reluctant confessions extracted under pressure), latecomer narrative (editorial device framing a company as entering a space after competitors, positioning it as playing catch-up — "exploring partnerships with," "joining the race," "playing catch-up" — rather than innovating independently), regulatory shadow (ambient technique of inserting regulatory/legal context into product or business stories where it is tangential), editorial deflation (editorial technique of building up an ambitious vision then puncturing it with a brief dismissive phrase — "That's the idea, anyway," "or so X claims," "if it ever actually works" — implying failure without explicit argument), denial contradiction (source's direct denial or minimization placed alongside contradicting evidence — "does not exist" near code analysis findings, combative "misleading"/"dishonest" pushback followed by removal evidence, soft "part of a pilot" editorially undercut), analogy/metaphor (explicit comparisons using "like," "akin to," "equivalent of" that import associations from a comparison domain — distinct from analogy_stacking which requires 3+), taxonomy framing (presenting findings using a structured classification system that implies completeness and authority — "broken, buried, or missing" leaves no escape route), failure precedent (invoking a prior failed attempt at the same project type to cast implicit doubt on the current effort — "was set to receive $X ... ultimately cancelled"), worker replacement irony (workers who built/trained the AI that now replaces them), two-tier treatment (contrasting treatment of full-time vs. contractor workers), regulatory favoritism (government oversight framed as picking winners and losers), escalation amplification (intensifying modifiers before threat/concern language), commodification metaphor (language flattening human identity/work into interchangeable modules, tokens, or data), pathologizing metaphor (addiction, disease, or bodily-excess language applied to corporate/institutional behavior — "addicted to," "gorge itself," "high-rollers" — framing strategy as compulsion), anthropomorphization (ascribing human emotions, intentions, cognition, or social roles to AI systems — "happily handed," "the confused bot," "without being taught how to" — converting design flaws into character traits), industry normalization undercut (acknowledging a practice is industry-wide then undercutting it to single out the target — "Other companies also X, but Meta's reliance is especially…"), assumed consensus (presenting a contested or unsupported claim as self-evident common knowledge — "People hate X," "Everyone knows," "Nobody wants" — skipping the burden of proof), editorial aside (breaking journalistic register to address the reader directly with sarcastic or solidarity-building interjections — "brace yourself," "let's be honest," "something tells me"), slippery slope (extrapolating from a specific action to a broader systemic threat via precedent-setting language — "sets an uncomfortable precedent," "If this approach extends," "could end up paying" — common in consumer-tech restriction/DRM coverage), consumer ownership (framing corporate restrictions as violating what consumers "already paid for" — "hardware you've already paid for," "runs entirely on the device" near "subscription/fee" — invoking property-rights intuitions), usage dismissal undercut (corporate minimization of a restriction's impact by citing low average usage — "most users don't use it for three hours" — as reassurance the journalist then challenges), financial reassurance (financial journalism device where negative operational news is immediately reframed as positive market/investor signal — "could soothe concerns," "easing fears," "investors shrugged off" — the journalist's own reassurance, not quoted corporate PR), cross-publication import (importing another outlet's characterization as settled fact — "several reports have depicted," "widely described as," "what critics have called" — laundering contested framing into consensus), competitive positioning (explicitly elevating a competitor over the subject entity — "good news for [competitor]," "buy from a more reputable company," "[competitor] has always/would never" — positioning a rival as the beneficiary of the subject's failure), heritage nostalgia (age, generational continuity, or historical significance establishing emotional stakes — "141-year-old manufacturer," "fifth generation working at the company," "iconic buildings" — creating implicit argument that what is at risk has deep, irreplaceable value), historical legitimation (insertion of temporally distant positive data to structurally dilute fresh negative news — old earnings beats or revenue growth recapped in negative-news articles), marginal endorsement (analyst action of negligible magnitude presented as meaningful bullish signal — price target raises of <1% or rating reiterations framed as substantive conviction), competitive deficit (enumerating multiple named competitors to amplify the subject's failure — "failed to launch a rival to [A]'s X, [B]'s Y, and [C]'s Z" — pile-on effect of being surrounded and outpaced), competitive displacement (framing one entity's action as filling a vacuum left by another's retreat or strategic pivot — "at a time when [Entity] may be reorienting," "filling the void left by" — positions subject as losing ground while competitor capitalizes), policy reversal (framing change of position as flip-flop or U-turn — "reversed course," "backtracked," "walked back" — implying inconsistency rather than evolution), absence as evidence (framing non-action or omission as proof of guilt — "the audit that never happened," "has never disclosed," "failed to act" — converting non-events into indictments), silence as guilt (explicitly treating silence or non-response as confession — "That silence is its own answer," "the lack of denial speaks volumes" — asserting silence proves something), talent hemorrhage (cataloging multiple departures to competitors in sequence — "left for [Company]... recently left... is also leaving" — building cumulative exodus narrative), strategic reversal (company reversing a core strategic position — "a major departure from longtime philosophy," "chosen to abandon," "start from scratch" — framing change as betrayal of principle), scandal comparison (using a notorious fraud/disaster/scandal name as a compact pejorative label — "AI Theranos," "the Enron of AI" — importing moral weight without explicit argument), repeated disruption (headline or body language implying chronic instability — "shakes up... again," "yet another restructuring," "months of tumult" — framing subject as incapable of settling), expert contradiction (named expert source directly contradicting a company's stated rationale — "It's not about X; it's about Y" inversion — the undercut comes from a credentialed third-party, not the journalist), loss-leader framing (editorial description of selling hardware at cost to capture subscription revenue — "sold at cost," "user base grows, subscription service grows revenue" — reframing consumer pricing as strategic capture), editorial dramatization (interpretive glosses rewriting neutral facts in heightened dramatic language — "unexpected reality check," "massive shakeup," "turbulent transition," "did not mince words," "specifically engineered to" — standalone dramatic set-pieces distinct from escalation_amplification's modifier + threat-noun pairs), precedent framing (signaling event significance through historical rarity — "first in N years," "first since YYYY," "unprecedented [action]" — establishes significance through time-span comparison, distinct from scale_magnitude and precedent_analogy), expert consensus authority (trade publication technique of assembling 3+ named credentialed experts who all reinforce the same editorial thesis — creates illusion of independent validation when all sources converge on the journalist's framing — distinct from anonymous_authority and expert_contradiction), prescriptive solutionism (trade publication technique of transforming accountability or controversy stories into management playbooks via prescriptive bullet lists, "actionable steps," or "key takeaways for IT leaders" — normalizes the underlying behavior by implying it is a solvable governance problem rather than a systemic or ethical issue), strategic disclosure (a party in a dispute strategically discloses an opponent's legal demand, internal figure, or unfavorable position to frame it as extreme or unreasonable — the journalist reports the disclosure but the framing originates with the disclosing party, not editorial choice), valuation comparison (comparing a penalty, cost, or liability amount to a company's market capitalization or total valuation to make the figure feel existentially threatening — "compared to the company's market capitalization, which is just above $1.5 trillion"), narrative reframing (editorial technique of explicitly acknowledging an existing narrative then dismissing it as incomplete or simplistic — "That concern is fair. It is also incomplete," "The lazy version says" — allows the author to redirect reader without refuting facts), dismissive qualifier (using pejorative or dismissive adjectives to characterize a viewpoint before presenting it — "an easy worry," "the lazy version," "a convenient narrative" — subtly delegitimizing the opposing view before engaging with it), bull/bear structuring (investor-media genre pattern organizing analysis into explicit "what would support/break the thesis" sections with enumerated signals — creates appearance of balanced analysis while the structural weight and conclusion can tilt one direction), analyst authority (named analyst firms used as authority sources to frame corporate spending decisions — "BofA warns," "according to Goldman Sachs" — distinct from anonymous_authority in that these are named institutions whose credentialing function shapes the narrative), investor advisory (editorial technique where the author adopts an investment-advisor posture, directly warning investors about risks and prescribing behavior — "Investors ignore [X] at their peril," "should start paying attention," "Investors may be making the wrong choice" — distinct from analyst_authority and bull_bear_structuring in that it addresses the reader as investor), default burden privacy (editorial technique of framing a default-on feature with a standard opt-out as inherently violating user consent — "enabled by default," "opt-out," "users may not know," "without consent" — emphasises the burden on users to discover and toggle settings, treating default-on as quasi-deceptive regardless of opt-out accessibility), editorial cross-promotion (all-caps interstitial headline blocks or CTA blocks embedded in article body text, importing linked headline framing into otherwise balanced reporting — creates plausible deniability where neutral prose coexists with adversarial cross-promo blocks), emotion attribution (editorial attribution of emotional states — disappointment, frustration, alarm — to subjects who expressed only factual observations, upgrading neutral statements into emotional reactions — "is disappointed that," "leading investors to fret"), market verdict (market drops or investor behavior framed as authoritative editorial judgment on corporate strategy — "fell X% as/amid concerns," "investors have spoken," "wiping $X in value"), overbuilding narrative (infrastructure investment framed as inherently excessive, unsustainable, or bubble-like — "spending war," "arms race," "overcapacity," "AI bubble," "when will someone blink," "throwing money at"), litigation cascade (stacking of multiple legal fronts — "N states banded," "N,NNN cases pending," "Another N states filed" — building cumulative existential-threat narrative through enumeration of concurrent legal actions), defensive verb framing (loaded attribution verbs editorializing corporate actions — "attempted yet failed," "was forced to," "grudgingly acknowledged," "scrambled to," "has been plagued by" — converting neutral corporate behavior into narratives of struggle, compulsion, or failure through verb choice alone), regulatory risk subordination (regulatory/legal risk acknowledged but architecturally sandwiched between positive market signals — reading experience begins and ends with optimism — genre-normative for IBD/Investopedia/Motley Fool, higher signal in WSJ/NYT/Bloomberg), recovery narrative (three-beat article architecture: decline → catalyst → recovery projection — common in financial/investor media where prior weakness is acknowledged then reframed through positive catalysts and forward analyst projections), grudging concession (positive action or improvement acknowledged but editorially minimized — \"finally,\" \"only after backlash,\" \"it's about time\" — framing legitimate progress as reluctant, forced, or insufficient), ultimatum framing (multi-stage regulatory/legal proceeding compressed into binary \"do X or face Y\" construction — \"change X — or get/face Y,\" \"must [action] or face [consequence],\" \"comply or face fines\" — collapsing procedural complexity into an \"or else\" fork), recidivism framing (entity framed as serial offender through temporal recurrence markers — \"once again caught,\" \"has a long history of violations,\" \"serial violator,\" \"pattern of\" — constructs a habitual-offender narrative distinct from repeated_disruption's organizational-instability focus), reader positioning (second-person concessive constructions that align the reader with the author's editorial stance before evidence is presented — \"you couldn't be blamed,\" \"you'd be forgiven for thinking,\" \"hard to blame anyone,\" \"you'd be right to worry\" — presupposes agreement rather than earning it, distinct from assumed_consensus and editorial_aside), no-comment implication (publishing a subject's non-response as implicit editorial judgment of evasiveness — \"did not immediately respond,\" \"declined to comment\" — distinct from silence_as_guilt which treats absence of action as confession), competitive guilt transfer (linking a product to a competitor's scandal in the same section, creating guilt by proximity — Meta→Grok→nudify→children→lawsuit inference chain without direct accusation), consent alarm (default-opt-in or automatic enrollment language framing product defaults as consent violation — \"automatically enrolled,\" \"without your knowledge,\" \"use your likeness\" — common in privacy service journalism), editorial character attack (journalist inserts their own characterization of a named person's reputation or moral standing as established fact — \"best known for unethical,\" \"he's the guy for that,\" \"has a long history of exploiting\" — distinct from loaded_language targeting individual words and guilt_by_association linking to separate actors), surveillance creep (ambient always-on recording, continuous capture, or incremental expansion of monitoring scope framed as normalizing total information awareness — \"constantly capture audio and visuals,\" \"AI is listening,\" \"record throughout the day\"), market flooding (volume, speed, or scale of product distribution cast as aggressive or overwhelming — \"flooding the market,\" \"into the hands of as many people as possible,\" \"market saturation\"), humanization (emotionally resonant personal details creating sympathy for affected individuals — \"laid off two days before giving birth,\" pregnancy near workplace action, age-specific vulnerability — strategic placement of intimate biographical detail to move reader from policy abstraction to personal identification), surveillance enumeration (multi-item comma-separated lists of monitoring technologies or data types amplifying perceived invasiveness through sheer accumulation — the list length itself is the editorial device, even when each item is factually accurate)
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

Define entity clusters in publication profiles or pass custom clusters to `detect_entities()`. See [ENTITY_REFERENCE.md](ENTITY_REFERENCE.md) for the complete quick-reference card with all 88 clusters, 875 aliases, disambiguation filters, and pipeline interactions, and [METHODOLOGY.md §15](METHODOLOGY.md#15-entity-detection--cluster-reference) for the cluster reference table with analytical categories and growth history.

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
│   └── sample_output/       # 190 annotated real-article analyses (see METHODOLOGY.md §17)
├── tests/                       # 2834 tests across 128 test files (all from real articles)
│   ├── test_accuracy_guide.py   # ACCURACY_GUIDE.md consistency: existence, cross-references, content structure, correction path table, annotated article count sync
│   ├── test_analyst_quote_attribution.py # Analyst/financial quote attribution: firm-level post-attribution suppression, wire cross-citation filtering, genuine scare quote preservation
│   ├── test_asymmetry.py        # Asymmetry score, Welch's t, Cohen's d, bootstrap CI
│   ├── test_atlantic_analysis.py # Atlantic-specific: Emerson Collective conflicts, AI coverage
│   ├── test_avclub_sardonic_framing.py # AV Club sardonic framing: sarcastic_correction sub-patterns, loaded_language ad hominem/industry-as-vice, ironic denial regex
│   ├── test_bofa_capex_watermelon.py # BofA capex/Watermelon model: comma-after-entity lookahead fix, Barron's + Memeburn entity/framing detection, scale_magnitude "nearly double"
│   ├── test_careers.py          # Career loading, migration detection, DiD, leadership ITS
│   ├── test_citations.py       # Citation extraction, source grading, domain classification
│   ├── test_cli_doc_consistency.py # Structural consistency: validates all CLI examples in docs/*.md and README.md use real CLI flags (catches phantom flags) and that documented commands are real
│   ├── test_claims.py          # Claim-to-source mapping, statistic/quote detection
│   ├── test_entities.py        # Entity detection, regex, false-positive exclusion
│   ├── test_glasses_deep_dive.py # Glasses launch fixes: kicker framing, product-name stop-filter, emotional_appeal exclusion
│   ├── test_gizmodo_fury_review.py # Gizmodo Meta Fury contradictory review: entity detection, Path F tone correction, emotional terms
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
│   ├── test_loaded_language_uproar.py # Loaded language detection, workplace coercion terms
│   ├── test_marketwatch_cloud_pivot.py # MarketWatch Meta cloud pivot: financial-defeat EL terms, ironic_quotation attribution suppression (wrote/believes), simple competitive_deficit pattern
│   ├── test_nyt_ai_reviews.py   # Isolation framing, pressure language, VADER correction
│   ├── test_nyt_article_improvements.py  # NYT-specific: agency, coercion, juxtaposition
│   ├── test_nyt_school_targeting.py  # NYT school targeting: education topic, National PTA entity, safety team overrule hypocrisy, role-based adversarial stance
│   ├── test_nypost_muse_image_yanks_jul13.py  # NY Post Muse Image: capitulation verbs, Path C forced-retreat override, policy_reversal adversarial
│   ├── test_platform_death.py   # Platform eulogy detection, tone distinction
│   ├── test_policy_reversal_competitive_deficit.py # Policy reversal and competitive deficit framing device detection, documentary source extraction
│   ├── test_competitive_displacement.py # Competitive displacement framing device (new — fills-vacuum temporal conjunction), entity cluster additions: AI Research Orgs (AI2), HuggingFace, Princeton, plus OpenAI cluster expansions (GPT-2, gpt-oss, Miles Brundage)
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
│   ├── test_sarcastic_correction.py # Sarcastic correction framing: concede-then-retract, standalone sarcasm, false-positive exclusion
│   ├── test_wired_gulag_patterns.py # Wired "gulag" coverage: conscript terms, keystroke surveillance, Scale AI entity, article-context loaded language
│   ├── test_cannes_contractors.py # Wired "Cannes" contractors: Scale AI/Covalen/Character.AI cluster, catastrophizing "death of" fix, Outlook source exclusion, deception/impersonation patterns
│   ├── test_type_d_fixes.py      # Compound publication source extraction (Business Insider, Daily Beast, etc.) and bare confession framing patterns
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
│   ├── test_postpass_activation.py # Structural post-pass framing activation: analogy stacking, speculative framing thresholds
│   ├── test_precedent_analogy.py # Precedent analogy framing: opioid/tobacco/asbestos crisis comparisons, era-based villainy import
│   ├── test_resistance_patterns.py # MIT TR Resistance article patterns: catastrophizing (threat to humanity), alarm/anxiety idioms, intensity/polemical/violence loaded language, poll-based social proof, stalled-dollar and workforce-percentage scale magnitude
│   ├── test_structural_consistency.py # Structural consistency: framing device type registry completeness, total regex pattern count guard (662 patterns), doc count sync guards, test file listing guards, README/ARCHITECTURE total test count header guards (validates pytest-collected count including parametrize expansions), stale voting power purge across all doc files, cross-reference consistency (stale framing taxonomy count purge including parenthetical annotations, README topic bucket count guard), inline topic list validation (ARCHITECTURE.md, AGENT_GUIDE.md, METHODOLOGY.md topic names match code), quality standards banned phrase count and completeness guards, framing.py docstring count and device list completeness validation, ARCHITECTURE.md extended device count label guard, ARCHITECTURE.md device name list completeness (Core + Extended inline lists enumerate all device types from code), ARCHITECTURE.md test_topics bucket count guard, METHODOLOGY.md device table completeness (Extended + Structural tables vs code), METHODOLOGY.md intro tier count guard (106/10/89/7 matches code), METHODOLOGY.md §17 annotated article count and publication count guards (corpus article count and distinct publication count match actual files on disk), adversarial device type list consistency (METHODOLOGY.md + QUALITY_STANDARDS.md + AGENT_GUIDE.md + SENTIMENT_CORRECTION_REFERENCE.md + example demo scripts vs sentiment.py), stale regex pattern count purge (ARCHITECTURE.md + README.md), AGENT_GUIDE.md framing tier count guard (106/10/89/7 matches code), correction path documentation completeness (all 12 paths A-L in METHODOLOGY.md + ARCHITECTURE.md + AGENT_GUIDE.md + README.md + example demos with summary table + introductory path count/range text validated in ARCHITECTURE.md, AGENT_GUIDE.md, and METHODOLOGY.md + financial inflation ref path range), migration count guards (README.md careers_demo + EDITORIAL_HISTORIES.md both match CareerTracker), publication count floor guards (README.md + EDITORIAL_HISTORIES.md), entity cluster consistency (METHODOLOGY.md §15 cluster count matches code, table completeness with no missing/phantom clusters, alias count accuracy), ENTITY_REFERENCE.md consistency (cluster count header, alias count header, cluster completeness, no phantom clusters, custom/auto regex counts, README and ARCHITECTURE cross-references), annotated article count guard (QUALITY_STANDARDS.md vs examples/sample_output/), ARCHITECTURE.md annotated article count guard (file-tree comment vs examples/sample_output/), same-event cluster count guard (QUALITY_STANDARDS.md §10.2 Tier 1 + Tier 2 table rows), example demo adversarial type set completeness (framing_correction_demo.py + sarcastic_editorial_demo.py inline adversarial_types vs code), stale device type count purge (rejects historic device type counts in any doc that don't match the current total, including parenthetical annotations), stale journalist/multi-pub count purge (all EDITORIAL_HISTORIES.md references match current YAML counts), FRAMING_REFERENCE.md extended count consistency (tier legend + Counts by Tier table vs code), SENTIMENT_CORRECTION_REFERENCE.md adversarial count consistency (Part 1 header + Key Input Signals table + adversarial table completeness vs code), stale inline path range purge (no docs/examples files contain interrupted path ranges ending before current max path letter), framing demo docstring path completeness (framing_correction_demo.py docstring lists every correction path A-L)
│   ├── test_arena_cross_analysis.py # Cross-publication analysis: NYT vs Gizmodo on Arena story — tone separation, emotional intensity, ironic quotation filtering, agency detection
│   ├── test_latecomer_regulatory_framing.py # Latecomer narrative and regulatory shadow framing: catch-up/copycat positioning, ambient regulatory context insertion, Arena article integration
│   ├── test_editorial_deflation.py     # Editorial deflation framing: post-buildup dismissal phrases ("That's the idea, anyway"), attribution-as-skepticism, MIT TR Anduril article integration
│   ├── test_editorial_dramatization.py # Editorial dramatization framing: interpretive glosses rewriting neutral facts in dramatic language — "unexpected reality check," "massive shakeup," "turbulent transition," "did not mince words," "specifically engineered to." iPhone in Canada derivative article integration
│   ├── test_memeburn_glasses_deep_dive.py # Memeburn Meta glasses deep dive: open-ended-threat kicker patterns, ubiquitous-camera loaded language, indirect rhetorical question, Gizmodo entity detection
│   ├── test_child_safety_denial.py # Engadget child safety features: denial_contradiction with "no evidence" denials, post-quote combative attribution (said/insisted), replicated/verified evidence counters
│   ├── test_worker_replacement_two_tier.py # WebProNews Meta Dublin contractors: worker_replacement_irony (trained AI that replaced them), two_tier_treatment (contractor vs full-time), geopolitical false positive fix (physical "stood firm"), outsourced_intensity expansion (labor-law expert quotes)
│   ├── test_wired_subscription_era.py # Wired Conversation Focus paywall: consumer_ownership no-adverb "runs on-device", expert_contradiction ("it's not about X; it's about Y"), loss_leader_framing ("sold at cost" + subscription revenue), editorial_aside sarcastic "Guess..." opener, Path J expert-driven structural critique correction
│   ├── test_child_safety_analysis.py # NYT child safety study analysis: new entity clusters (US Congress, Academic/Research, Research Centers, Child Safety Researchers/Legislation, Australia), source extraction fixes (case-sensitive [Aa]n?, expanded _KNOWN_ORGS, direct org attribution), new framing devices (analogy_metaphor, taxonomy_framing), agency attribution sparse-data dampening
│   ├── test_mit_tr_anduril_meta_warfare_glasses.py # MIT TR Anduril/Meta warfare glasses: defense-tech entity detection, failure_precedent (new device), analogy_stacking FP filters (factual similes, recall verb), context-gated Llama entity, selective_rehabilitation, editorial_deflation, sentiment calibration
│   ├── test_multi_outlet_comparison.py # N-way cross-outlet same-event comparison: compare_multi_articles() function validation, 4-way Zuckerberg town hall cross-analysis (Reuters/TechCrunch/Barron's/PYMNTS), cross_publication_import detection, tone matrix generation, QUALITY_STANDARDS Tier 1 update guard
│   ├── test_quote_forward_preference.py # Quote extraction forward-preference fix: _extract_nearby_quote prefers forward quotes over backward, regression test for Ji/Gong misattribution bug in MIT TR AI agent security article
│   ├── test_muse_image_deflation.py # iPhone-in-Canada Muse Image rollout: editorial_deflation (better-late-than-never idiom, I-guess hedge, conditional deflation, trailing minimizer), rhetorical_question (Who's-actually contraction), latecomer_narrative (saving-you-steps-from, competitor listing), integration test for closing-paragraph device cluster
│   ├── test_bloomberg_muse_image_entities.py # Bloomberg Muse Image entity extraction: SpaceXAI→xAI cluster mapping, Anthropic PBC→Anthropic alias, CoreWeave Inc/Alphabet Inc's Google/Oracle Corp corporate suffix extraction
│   ├── test_wsj_ai_spending_sources.py # WSJ AI spending article source extraction: Pattern 0c "Name of Org VERB" (KeyBanc Capital fix), Pattern 0d reverse "VERB Name of Org" (Jefferies fix), Pattern 0e "Org analyst Name VERB" (Bernstein Research affiliation fix), full-text expert detection fallback
│   ├── test_compound_attribution_verbs.py # Compound negative attribution verb detection: contrastive failure/concession/defensive failure multi-word phrases, classification priority over single-word lookup
│   ├── test_litigation_cascade.py # Litigation cascade regression tests: multi-jurisdiction cascade detection, escalation patterns, threshold validation, negative cases
│   ├── test_techcrunch_muse_image_fixes.py # TechCrunch Muse Image privacy article: "Muse Video" product-name source false positive, Cambridge Analytica entity cluster separation, "landmark" literal-usage loaded_language suppression
│   ├── test_ibd_meta_cloud_sources.py # IBD Meta cloud article source extraction regression tests
│   ├── test_ibd_sticker_shock.py # IBD open-source AI article: competitive_deficit framing (acknowledges defeat, catch up to, fill the vacuum), single-surname affiliation full-text fallback, conditional org source filter, D.A. Davidson entity detection
│   ├── test_superintelligence_org_suppression.py # Topic classification: "Superintelligence Labs" proper-noun suppression for ai_ethics_safety, Reuters Muse Image wire false positive fix
│   ├── test_reuters_french_antitrust.py # Reuters French antitrust: "The Information" case-sensitive false positive fix, French media association entities (DVP/APIG/Le Monde/Les Echos), content_licensing topic bucket, acronym org source extraction with appositive clause
│   ├── test_reuters_french_antitrust_jul8.py # Reuters French antitrust publishing fees Jul 8: escalation_amplification framing (trend magnification), precedent_analogy framing (enforcement precedent citing), content_licensing as primary topic, French media entity clustering (DVP/APIG/Le Monde/Les Echos), Alphabet/Google cluster
│   ├── test_reuters_eu_dsa_meta_jul10.py # Reuters EU DSA Meta addictive features Jul 10: entity detection (EU Commission, European Commission cluster), regulatory framing devices, sentiment scoring for wire-service DSA coverage, cross-article comparison
│   ├── test_fastco_meta_glasses_2026_07_10.py # Fast Company Meta AI glasses controversies roundup Jul 10: EFF 3-word org name extraction fix (_KNOWN_ORGS), C-suite title affiliation (CEO/CTO pattern 0b), hyphenated surname dedup (endswith-hyphen check), VADER polarity inversion (raw +0.633 → corrected −0.5217)
│   ├── test_foxbusiness_meta_1_4t_penalty.py # Fox Business Meta $1.4T penalty Jul 7: editorial_cross_promotion framing device (new — all-caps interstitial blocks), reached_out_for_comment no_comment source pattern (new), valuation_comparison detection, litigation/child_safety topic assignment, structural consistency guard (87 pattern-matched device types)
│   ├── test_foxbusiness_muse_image_shutdown.py # Fox Business Muse Image shutdown Jul 11: editorial_cross_promotion regex fix (dollar signs/digits in all-caps callouts), policy_reversal controlled retreat patterns (new — "missed the mark"/"no longer available"), loaded_language "misuse" addition, dollar-sign regression guard
│   ├── test_guardian_cohere_correction.py # Guardian Cohere lawsuit correction Jul 11: factual correction — Guardian News & Media Limited is a NAMED PLAINTIFF in Advance Local Media v. Cohere (SDNY 1:25-cv-01305), contradicting previous "strategic_licensing_over_litigation" classification. Tests: triple_path_ai_strategy reclassification, Cohere MTD denial (McMahon, Nov 13 2025), Observer/Tortoise transfer date (Apr 22 2025), Richard Furness GMG→Tortoise personnel migration, Brittin BBC-Channel 4 partnership, NYT v OpenAI MDL 3143 cross-reference, co-plaintiff verification
│   ├── test_zuckerberg_ai_agents_same_event.py # Reuters vs Barron's same-event comparison on Zuckerberg AI agent admission (Jul 2, 2026 town hall): emotion_attribution framing device (new — editorial attribution of emotional states never expressed by subject), competitive_deficit detection, confession_framing divergence, entity detection (Claude Code, Alexandr Wang, Muse/Spark), topic classification, source extraction (documentary "recording heard by Reuters"), same-event framing divergence analysis
│   ├── test_reuters_rust_belt_jul9.py # Reuters Big Tech data centers Rust Belt factories Jul 9: heritage_nostalgia framing device (new — age/generational continuity establishing emotional stakes), source false positive elimination (Capacity/Energy Consumers/White House/Synergy Research/Smart Electric Power), Pattern 0f affiliation extraction ("president of the trade group Industrial Energy Consumers of America"), environmental domain keyword in affiliation patterns, infrastructure_energy topic assignment
│   ├── test_reuters_scam_ads_securities_jul13.py # Reuters Meta scam ads securities defense Jul 13: power_asymmetry personal-loss savings narrative ("retirement savings"), loaded_language additions ("depressingly", "peculiar"), self_referential_investigation "my [Publication] colleagues" pattern (with source_publication wire-service filter), editorial_dramatization literary-aside undercut ("— while it lasted"), rhetorical_question "Should [entity]... hinge" pattern, entity extraction (Meta cluster with Facebook/Instagram/WhatsApp subsidiaries), sentiment negative lean
│   ├── test_reuters_australia_esafety_child_safety_jul14.py # Reuters Australia eSafety child safety Jul 14: iMessage → Apple cluster (new alias), Google Messages → Google cluster (new alias), Discord cluster (new), Julie Inman Grant → Australia cluster (new alias), multi-entity distribution (7+ clusters, Australia primary), framing: no_comment_implication, regulatory_shadow, scale_magnitude, catastrophizing
│   ├── test_reuters_meta_ai_layoff_discrimination_jul14.py # Reuters Meta AI layoff discrimination Jul 14: District of Columbia entity resolution (not Columbia University), legal-context loaded_language suppression (violating/retaliation as legal terms of art), legal-context absence_as_evidence suppression (plaintiff allegation vs journalistic framing), standalone "slashed" loaded_language verb
│   ├── test_foxbusiness_meta_ai_layoff_discrimination_jul14.py # Fox Business Meta AI layoff discrimination Jul 14: publication self-reference source extraction ("told Fox Business"), legal-context emotional_appeal suppression ("disability" as ADA descriptor), editorial_cross_promotion for embedded all-caps links
│   ├── test_wsj_meta_smartglasses_jul15.py # WSJ Meta smartglasses privacy Jul 15: surveillance_creep (5 patterns), market_flooding (4 patterns), voice-command ironic_quotation suppression, fitness-tracking loaded_language suppression, comma-before-verb source extraction ("Bosworth, said"), title affiliation false positive filter ("Chief Executive"), institutional suffix filter ("Liberties Union, said")
│   ├── test_wsj_meta_ai_layoff_discrimination_jul14.py # WSJ Meta AI layoff discrimination Jul 14: independent expert source extraction (Prof. Hirsch, UNC), corporate spokesperson, lawsuit-as-documentary source, litigation_framing, timeline_implication, entity clustering, source diversity
│   ├── test_reuters_iris_chip_jul9.py # Reuters Meta Iris chip production Jul 9: Sumitomo Electric entity cluster (new), inverted analyst attribution ("Morgan Stanley analysts said"), compound no-comment subject extraction ("Samsung Electronics and Sumitomo Electric did not respond"), "floundered" passive framing term, ai_development + corporate_strategy topic classification
│   ├── test_reuters_muse_spark_11_jul9.py # Reuters Muse Spark 1.1 developer preview Jul 9: pathologizing_metaphor "intervention" false positive suppression (neutral technical context — "less human intervention", "without intervention"), pricing comparison phrases in NEGATIVE_COMPARISON/POSITIVE_COMPARISON ("above openai", "below anthropic", "priced above/below", "cheaper than", "undercuts"), loaded_language competitive dramatization ("heated competition", "AI supremacy", "tech arms race"), competitive_positioning "pitting...against" and "close/narrow the gap"
│   ├── test_recovery_narrative.py # Recovery narrative framing device (#94): three-beat decline→catalyst→recovery structure in financial articles, bidirectional competitive_positioning (positive parity variant), confidence scoring, negative guards for neutral wire articles and decline-only articles; discovered from MarketWatch Meta stock rebound article (Jul 10, 2026)
│   ├── test_register_muse_image_superintelligence_jul13.py # The Register Muse Image "superintelligence" (Jul 13): confession_framing scare-quoted gap, editorial_deflation temporal deflation (long noun phrase gap), recidivism_framing sardonic competence enumeration, ceo_personalization modifier adjectives ("Zuck's latest big bet"), editorial_aside, consent_alarm, loaded_language, policy_reversal, sarcastic_correction
│   ├── test_speculative_quote_suppression.py # Speculative framing quote-context suppression: _find_quoted_spans helper, _is_in_quoted_span helper, editorial prose hedges still fire at 5+ threshold, analyst quotes suppressed (straight + smart quotes), mixed editorial/quoted context, BofA research note style, Motley Fool editorial hedging
│   ├── test_controlled_retreat_language.py # Controlled retreat language detection: policy_reversal subtype for corporate damage-control statements (intent displacement, active listening performance, target-miss euphemism, passive unavailability, control reassurance, useful-tool salvage); discovered from Reuters Meta Muse Image discontinuation (Jul 10, 2026)
│   ├── test_datacenter_framing_jul13.py # WSJ Meta Louisiana data center $50B (Jul 13): escalation_amplification intervening adjective, loaded_language gambling/infrastructure-burden/magnitude patterns, recovery_narrative revitalization idioms
│   ├── test_barrons_splurge_jpmorgan_jul13.py # Barron's Meta AI Splurge JPMorgan Jul 13: pathologizing_metaphor "splurge" variants (6), competitive_deficit "compared with" bridge pattern (7), J.P. Morgan period-variant entity detection (4), Epoch AI entity detection (2)
│   ├── test_barrons_1t_child_safety_backlash_jul10.py # Barron's $1T child safety backlash Jul 10: Roblox entity cluster (3), scale_magnitude N-figure idiom "13-figure penalty" (4), loaded_language "ripe/easy/prime target" (4), investor_advisory (3), catastrophizing (1), pathologizing_metaphor (1), emotional_appeal (1), refusal_amplification (2), 4 xfail known gaps
│   ├── test_foxbusiness_louisiana_datacenter_jul13.py # Fox Business Meta Louisiana datacenter $50B Jul 13: recovery_narrative broadened "reshaping [ProperNoun] Parish" + "transforming [institution]", loaded_language "life-altering", full article regression
│   ├── test_ibd_morgan_stanley_capex_jul13.py # IBD Morgan Stanley CapEx Jul 13: escalation_amplification social/political/consumer/national adjectives (11), market_verdict penalizing/punishing/discounting (8), recovery_narrative proper-noun fix (4), Morgan Stanley + SpaceX entities (3)
│   ├── test_washexaminer_meta_louisiana_50b.py # WashExaminer Meta Louisiana $50B Jul 13: scale_magnitude physical-unit patterns (5), sovereignty_framing American patriotic (3), anonymous_authority singular person fix (2), source extraction corporate title stop-words (2), isolated regression tests (4)
│   ├── test_usatoday_meta_ai_layoff_discrimination_jul15.py # USA Today Meta AI layoff discrimination Jul 15: litigation_framing (1), precedent_framing (1), anthropomorphization (1), entity Meta cluster (3), documented gaps scale_magnitude/escalation/cross_case_citation (3), Workday cross-case reference (3), expert source architecture (2), same-event structural contrasts (4)
│   ├── test_nypost_meta_ai_layoff_discrimination_jul14.py # NY Post Meta AI layoff discrimination Jul 14: bloodbath loaded_language workforce context (2), root_out/weed_out hunting vocabulary (2), ceo_personalization Zuckerberg's Meta (1), trend_bundling/competitive_guilt_transfer capex tail (1), juxtaposition AI spending vs layoffs (1), entity detection Meta/Apple/Zuckerberg (3), Challenger entity xfail ampersand gap (1), negative tone (1), litigation+workplace topics (2)
│   └── fixtures/
├── pyproject.toml
├── requirements.txt
├── iteration-log.md
└── LICENSE
```
