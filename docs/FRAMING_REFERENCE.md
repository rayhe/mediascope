# Framing Device Quick Reference

> A compact lookup card for all 102 framing device types detected by MediaScope. For full descriptions, detection patterns, and discovery provenance, see [METHODOLOGY.md §4](METHODOLOGY.md#4-framing-device-detection).

---

## How to Use This Reference

During article analysis, scan the text for trigger keywords and structural patterns listed below. Each device name links to the detailed entry in METHODOLOGY.md. The **tier** column indicates detection method:

- **C** = Core (10 types) — fundamental editorial techniques, pattern-matched
- **E** = Extended (85 types) — discovered from real article analysis, pattern-matched
- **S** = Structural (7 types) — detected via post-pass heuristics over full article structure

> **Note on device numbering:** Devices are numbered by discovery order (1–102), not by category. When new devices are discovered during article analysis, they receive the next sequential number. The reference organizes them by thematic category for readability, so device numbers within a category are not contiguous.

---

## Category 1: Attribution & Source Manipulation

Devices that shape how sources, experts, and quotes are deployed.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 1 | **Anonymous Authority** | C | Unnamed sources presented as definitive evidence | "sources say," "people familiar," "according to sources" |
| 2 | **Ironic Quotation** | E | Source's own words quoted then immediately undercut | Quote + "But," "Yet," "In reality," verdict like "wrongly believe" |
| 3 | **Outsourced Intensity** | E | Emotional language in legal filings/complaints quoted by neutral editorial prose | "the complaint alleges [loaded term]," quoted legal characterizations |
| 4 | **Expert Contradiction** | E | Named expert directly contradicts company's stated rationale | "It's not about X; it's about Y" inversion from credentialed source |
| 5 | **Expert Consensus Authority** | E | 3+ named experts all reinforce the same editorial thesis | "said [Name], [title] at [Company]" ×3+, all converging |
| 6 | **Cross-Publication Import** | E | Another outlet's characterization imported as settled fact | "several reports have depicted," "widely described as" |
| 7 | **Self-Referential Investigation** | E | Publication cites its own prior reporting as evidence | "a WIRED investigation found," "as WIRED previously reported" |
| 8 | **Analyst Authority** | E | Named analyst firms used as authority sources | "BofA warns," "according to Goldman Sachs," "[Firm] estimates" |
| 9 | **Social Proof Amplification** | S | Reaction counts cited to convert opinion into collective sentiment | "received X likes," "went viral with X comments" |
| 99 | **No-Comment Implication** | E | Non-response published as implicit evasiveness | "did not immediately respond," "declined to comment," "could not be reached for comment" |

---

## Category 2: Language & Tone Manipulation

Devices that use word choice, register shifts, and rhetorical techniques to color coverage.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 10 | **Loaded Language** | C | Word choices carrying implicit judgment | "admitted," "conceded," "insisted," "claimed"; workplace coercion terms |
| 11 | **Emotional Appeal** | C | Emotional language substituted for evidence | "heartbreaking," "chilling," "disturbing," "alarming" |
| 12 | **Sarcastic Correction** | E | Editorial sarcasm mockingly concedes then retracts | "Of course... oh hang on," "Just kidding," "Spoiler: it didn't" |
| 13 | **Editorial Aside** | E | Breaks journalistic register for direct reader address | "brace yourself," "let's be honest," "something tells me," "(yes, really)" |
| 14 | **Editorial Dramatization** | E | Neutral facts rewritten in heightened dramatic language | "unexpected reality check," "massive shakeup," "did not mince words" |
| 15 | **Escalation Amplification** | E | Intensifying modifiers before threat/concern language | "escalating concerns," "increasingly hostile," "growing alarm" |
| 16 | **Dismissive Qualifier** | E | Pejorative adjective characterizes viewpoint before presenting it | "the lazy version says," "an easy worry," "a convenient narrative" |
| 17 | **Assumed Consensus** | E | Contested claim presented as self-evident common knowledge | "People hate X," "Everyone knows," "Nobody wants," "Needless to say" |
| 18 | **Rhetorical Question** | E | Questions implying negligence without directly asserting it | "Were there even guardrails?" "Did anyone think to...?" |
| 19 | **Confession Framing** | E | Attribution verbs frame statements as admissions of guilt | "[Person] admits/concedes/acknowledged," "forced to admit," "mea culpa" |
| 20 | **Pressure Language** | E | Word choices framing actions as coercive | "pressing," "pushing," "strong-arming," "private demand" |
| 21 | **Sovereignty Framing** | E | National/patriotic identity language to delegitimize foreign positions | "British families," "our children," "national interest/security" |
| 98 | **Reader Positioning** | E | Second-person concessive constructions presupposing reader agreement | "you couldn't be blamed," "you'd be forgiven for thinking," "hard to blame anyone," "you'd be right to worry" |

---

## Category 3: Structural & Positional Framing

Devices that use article structure, sequencing, and placement for editorial effect.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 22 | **Kicker Framing** | S | Article ends on discordant negative note unrelated to main topic | Final ~400 chars contain negative signals when body is neutral-to-positive |
| 23 | **Delayed Defense** | S | Corporate rebuttal buried after 65% of article text | First response pattern appears in last 35% of article |
| 24 | **Juxtaposition** | E | Contrasting facts placed side-by-side for editorial effect | Investment figures adjacent to layoffs; surveillance tech near consumer language |
| 25 | **Timeline Implication** | E | Temporal sequencing used to imply causation | "After X happened, Y occurred" (when X did not cause Y) |
| 26 | **Taxonomy Framing** | E | Structured classification system implying completeness | "broken, buried, or missing" — named categories leaving no escape route |
| 27 | **Trend Bundling** | S | Target company's action grouped with 3+ peers to normalize or amplify | "Other companies have also…," "Similarly, X…" with 3+ companies |
| 28 | **Bull/Bear Structuring** | E | Analysis organized into explicit bull/bear sections | "What Would Support/Break the Thesis?" — may tilt via word count/position |

---

## Category 4: Entity & Power Framing

Devices that frame entities, companies, or individuals through power dynamics, comparisons, or personalization.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 29 | **Power Asymmetry** | C | Institutional power framed against individual vulnerability | Dollar amounts near individuals, "army of lawyers," David vs Goliath |
| 30 | **CEO Personalization** | C | Company's institutional actions attributed to CEO personally | "Zuckerberg's Meta," "Musk's Tesla," CEO-led constructions |
| 31 | **Guilt by Association** | C | Entity linked to controversial actors/events | Entity + controversial entity in same paragraph |
| 32 | **Isolation Framing** | E | Entity singled out as "the only" one not doing something | "The only major company that has not," "unlike its peers" |
| 33 | **Hypocrisy Frame** | E | Entity singled out as sole holdout, framing inaction as moral failing | "uniquely among its peers," "alone in refusing" |
| 34 | **Competitive Positioning** | E | Competitor elevated over subject entity (negative), OR subject elevated to competitor parity (positive) | **Neg:** "good news for [competitor]," "buy from a more reputable company." **Pos:** "comparable to leading industry benchmarks from," "on par with" |
| 35 | **Competitive Deficit** | E | Multiple named competitors enumerated to amplify subject's failure | "failed to rival [A]'s X, [B]'s Y, and [C]'s Z" — pile-on effect |
| 36 | **Competitive Displacement** | E | Entity A fills vacuum left by Entity B's retreat/pivot | "at a time when X is reorienting," "filling the void left by" |
| 37 | **Industry Normalization Undercut** | E | Acknowledges industry-wide practice, then singles out target | "Other companies also X, but [Target] is especially…" |
| 38 | **Latecomer Narrative** | E | Company framed as entering a space after competitors | "joining the race," "playing catch-up," "copycat," "me-too product" |
| 39 | **Refusal Amplification** | E | Entity's non-cooperation emphasized beyond its news value | "declined," "refused," positioned to imply guilt |
| 97 | **Recidivism Framing** | E | Entity framed as serial offender through temporal recurrence markers | "once again," "yet again," "continues to," "not for the first time," "has a history of" |
| 100 | **Competitive Guilt Transfer** | E | Competitor scandal juxtaposed to transfer culpability | "facing a class-action lawsuit," "threatened to remove from App Store" |

---

## Category 5: Analogy, Metaphor & Comparison

Devices that use comparisons, metaphors, or precedents to import external associations.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 40 | **Analogy/Metaphor** | E | Explicit comparisons importing associations from another domain | "like crash-testing a car," "akin to," "equivalent of," "tantamount to" |
| 41 | **Analogy Stacking** | S | 3+ distinct analogies for the same subject amplify perceived severity | Multiple "the equivalent of," "likened it to," "compared it to" markers |
| 42 | **Scandal Comparison** | E | Notorious fraud/scandal name used as compact pejorative label | "AI Theranos," "the Enron of AI," "the next WeWork" |
| 43 | **Precedent Analogy** | E | Current controversy compared to well-known historical case | "echoes opioid-era fights," "much like the [precedent] litigation" |
| 44 | **Failure Precedent** | E | Prior failed attempt at same project type invoked to cast doubt | "was set to receive $X ... ultimately cancelled" |
| 45 | **Pathologizing Metaphor** | E | Corporate behavior cast as addiction, disease, or compulsive gambling | "addicted," "gorge itself," "high-rollers," "withdrawal," "insatiable" |
| 46 | **Commodification Metaphor** | E | Human identity/work flattened into interchangeable modules or tokens | "distill colleagues into skills," "reducing a person to a task" |
| 47 | **Anthropomorphization** | E | Human emotions/intentions ascribed to AI systems | "happily handed," "the confused bot," "without being taught how to" |
| 48 | **Military Techno-Optimism** | E | Violence normalized through technology/UX language | "Optimize the human as a weapons system," "AI-driven targeting" |

---

## Category 6: Denial, Reversal & Contradiction

Devices that frame changes of position, denials, or admissions.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 49 | **Denial Contradiction** | E | Source's denial placed alongside contradicting evidence | "does not exist" near code analysis; "misleading" + removal evidence |
| 50 | **Corporate Reassurance Undercut** | E | Corporate reassurance language immediately undercut by evidence | "carefully designed" + "but/however/yet" + failure evidence |
| 51 | **Usage Dismissal Undercut** | E | Corporate "most users don't" minimization challenged by journalist | "most users don't use X" near "but/however" + ownership argument |
| 52 | **Policy Reversal** | E | Change of position framed as flip-flop or inconsistency. Subtype: **Controlled Retreat Language** — corporate statement uses intent displacement, active listening, target-miss euphemism, and passive unavailability to minimize failure signals. **Correction pipeline role:** co-occurrence with `consent_alarm` (≥2) or `loaded_language` (≥5) triggers the forced-retreat override, waiving Path A's agency threshold for capitulation narratives (see [SENTIMENT_CORRECTION_REFERENCE.md](SENTIMENT_CORRECTION_REFERENCE.md#path-a-variant-forced-retreat-override-jul-14-2026)) | "reversed course," "backtracked," "flip-flopped," "walked back"; **controlled retreat:** "missed the mark," "heard the feedback," "no longer available," "Our intent was" |
| 53 | **Strategic Reversal** | E | Company reversing a core strategic position | "a major departure from longtime philosophy," "chosen to abandon" |
| 54 | **Selective Rehabilitation** | E | Past controversy juxtaposed with current acceptance to imply opportunism | "Ousted from X... now welcomed at Y," "friendlier posture" |

---

## Category 7: Scale, Significance & Catastrophizing

Devices that amplify the magnitude, significance, or threatening nature of events.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 55 | **Catastrophizing** | C | Outcomes framed as existential or irreversible | "crisis," "catastrophe," "existential threat," "doomsday" |
| 56 | **Scale/Magnitude Framing** | E | Large raw numbers, calculated maximums, or scale analogies for impact | "up to 6% of global revenue," "enough to power 750,000 homes" |
| 57 | **Valuation Comparison** | E | Penalty/cost compared to market cap to imply existential threat | "$1.4 trillion ... market capitalization just above $1.5 trillion" |
| 58 | **Precedent Framing** | E | Event significance signaled through historical rarity | "first [X] in 17 years," "first [X] since YYYY," "unprecedented" |
| 59 | **Slippery Slope** | E | Specific action extrapolated to broader systemic threat | "sets an uncomfortable precedent," "if this approach extends," "opens the door to" |
| 60 | **Speculative Framing** | S | 5+ cumulative speculative hedges convert possibility into implied certainty | "could potentially," "might be able to," "could feasibly" stacked |

---

## Category 8: Regulatory & Legal Framing

Devices that shape how regulatory, legal, and government actions are presented.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 61 | **Litigation Framing** | C | Entity framed as adversarially using courts | "filing/mounting legal challenge," "legal battle against," "took X to court" |
| 62 | **Regulatory Shadow** | E | Regulatory context inserted into product stories where tangential | "increasing scrutiny," "amid antitrust," "could face regulatory" |
| 63 | **Regulatory Favoritism** | E | Government oversight framed as picking winners and losers | "picking winners and losers," "favorable treatment," "tilting the playing field" |
| 64 | **Geopolitical Regulatory Pressure** | E | Regulatory tensions framed as geopolitical confrontation | Embassy/diplomatic submissions, sovereignty/defiance rhetoric |
| 65 | **Strategic Disclosure** | E | Party in dispute discloses opponent's position to frame it as extreme | "Meta said in a recent court filing" — framing originates with disclosing party |
| 66 | **Default Burden Privacy** | E | Default-on feature framed as consent violation by emphasising opt-out burden | "enabled by default," "opt-out," "users may not know," "without consent" |
| 101 | **Consent Alarm** | E | Default opt-in / automatic enrollment framed as consent violation | "automatically enrolled," "without your knowledge," "use your likeness" |
| 102 | **Editorial Character Attack** | E | Journalist inserts their own characterization of a named person's reputation or moral standing as established fact, rather than attributing the claim to a source | "best known for unethical use of," "he's *the guy* for that," "has a long history of exploiting" |
| 67 | **Editorial Cross-Promotion** | E | All-caps interstitial headline blocks importing linked headline framing into otherwise balanced reporting | All-caps blocks 5+ words; "CLICK HERE TO GET THE FOX BUSINESS APP"; imports adversarial linked headlines |
| 68 | **Emotion Attribution** | E | Editorial attribution of emotional states never expressed by the subject — upgrading factual observations into disappointment, frustration, or alarm | "[Name] is disappointed that"; "leading investors to fret"; "[Name] is alarmed by" |
| 69 | **Litigation Cascade** | E | Stacking multiple legal proceedings, case counts, plaintiff numbers to create avalanche effect | "N states have banded/sued"; "more than N,NNN cases pending"; "Another N states also brought claims" |
| 70 | **Defensive Verb Framing** | E | Loaded attribution verbs framing subject as reactive or embattled | "attempted yet failed to"; "was forced/compelled to"; "grudgingly acknowledged"; "scrambled/struggled to"; "has been plagued by" |

---

## Category 9: Narrative & Editorial Architecture

Devices that construct or redirect overarching narrative frames.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 71 | **False Balance** | C | Fringe views presented as equivalent to mainstream | "some say... others say" with asymmetric evidence |
| 72 | **Selective Omission Signal** | C | Notable absences detectable in text | "declined to comment" without context, missing competitor comparison |
| 73 | **Straw Man** | E | Entity's position misrepresented to make it easier to attack | Simplified-claim-then-rebut constructions |
| 74 | **Narrative Reframing** | E | Existing narrative acknowledged then dismissed as incomplete | "That concern is fair. It is also incomplete," "The lazy version says" |
| 75 | **Editorial Deflation** | E | Ambitious vision built up across paragraphs, then punctured | "That's the idea, anyway," "or so X claims," "if it ever actually works" |
| 76 | **Prescriptive Solutionism** | E | Accountability story transformed into management playbook | "actionable steps for IT leaders," "executives must balance/evaluate" |
| 77 | **Tempering Coda** | S | Article ends by contextualizing or walking back its own headline-level framing | Final 25% contains explicit moderating language ("likely far higher than," "in context") contradicting headline severity |

---

## Category 10: Personnel & Labor Framing

Devices specific to workforce, employment, and organizational coverage.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 78 | **Worker Replacement Irony** | E | Workers who built/trained the AI now replaced by it | "trained AI models now face replacement by those same systems" |
| 79 | **Two-Tier Treatment** | E | Full-time vs. contractor treatment contrasted side by side | "[employees] receive X... [contractors] get far less" |
| 80 | **Talent Hemorrhage** | E | Multiple departures cataloged in sequence to build exodus narrative | "left for [Company]... recently left... is also leaving" |
| 81 | **Repeated Disruption** | E | Language implying chronic organizational instability | "shakes up... again," "yet another restructuring," "months of tumult" |
| 82 | **Absence as Evidence** | E | Non-action or omission framed as proof of guilt | "the audit that never happened," "has never disclosed," "failed to act" |
| 83 | **Silence as Guilt** | E | Non-response explicitly treated as confession | "That silence is its own answer," "the lack of denial speaks volumes" |

---

## Category 11: Consumer & Product Framing

Devices specific to consumer technology, product reviews, and subscription/pricing coverage.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 84 | **Consumer Ownership** | E | Corporate restriction framed as violating what consumer "already paid for" | "hardware you've already paid for," "runs entirely on the device" + "subscription" |
| 85 | **Loss-Leader Framing** | E | Hardware sold at cost to capture subscription revenue | "sold at cost," "user base grows, subscription service grows revenue" |

---

## Category 12: Financial & Investor Media Framing

Devices specific to financial journalism, earnings coverage, and analyst reporting.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 86 | **Financial Reassurance** | E | Negative operational news immediately reframed as positive market signal | "could soothe concerns," "easing fears," "investors shrugged off" |
| 87 | **Historical Legitimation** | E | Temporally distant positive data inserted to dilute fresh negative news | "reported [quarter] results ... beat/topped expectations" in negative-news article |
| 88 | **Marginal Endorsement** | E | Analyst action of negligible magnitude presented as meaningful signal | Price target raise of <1% framed as "analysts remain bullish" |
| 89 | **Market Verdict** | E | Market drops/investor behavior framed as editorial judgment on strategy | "fell X% as/amid concerns," "investors have spoken," "wiping $X in value" |
| 90 | **Overbuilding Narrative** | E | Infrastructure spending framed as excess, bubble, or unsustainable arms race | "spending war," "arms race," "overcapacity," "bubble," "when will someone blink" |
| 91 | **Heritage Nostalgia** | E | Age, generational continuity, or historical significance establishing emotional stakes for disruption | "141-year-old brick manufacturer," "fifth generation working at the company," "iconic buildings," "family-owned since 1892" |
| 92 | **Investor Advisory** | E | Author adopts investment-advisor posture, directly warning investors about risks and prescribing behavior. Two variants: *prescriptive* (Barron's — "investors ignore at their peril") and *observational* (IBD/Investopedia — "despite [risk], stock rallied") | "Investors ignore [X] at their peril," "should start paying attention," "Investors may be making the wrong choice," "it's time for investors to," "despite [regulatory action], [stock] rallied" |
| 93 | **Regulatory Risk Subordination** | E | Regulatory/legal risk acknowledged but architecturally sandwiched between positive market signals so reading experience begins and ends with optimism. Genre-normative for IBD/Investopedia/Motley Fool; higher signal in WSJ/NYT/Bloomberg | "Despite [regulatory/legal action], [stock positive]," article opens with stock performance before regulatory news, regulatory content >70% through article, "shrugging off [regulatory] headwinds" |
| 94 | **Recovery Narrative** | E | Three-beat article architecture: (1) prior decline/criticism, (2) catalyst event, (3) forward recovery projection via analyst quotes. Converts neutral news into "turning point" narrative. Genre-normative for MarketWatch/Barron's/Motley Fool | **Beat 1:** "has long been criticized," "stock was down X%." **Beat 2:** "investors cheered," "ease spending fears." **Beat 3:** forward-looking analyst projections, "up to N% lower costs" |

> **Devices #95–96** are in their own categories below: [Category 13: Concession & Acknowledgment Framing](#category-13-concession--acknowledgment-framing) and [Category 14: Procedural Compression](#category-14-procedural-compression).

---

## Category 13: Concession & Acknowledgment Framing

Devices that shape how positive developments or admissions are presented.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 95 | **Grudging Concession** | E | Positive development framed through qualifiers and historical failure context that ensure the good news reads as reactive or insufficient. Author acknowledges genuine improvement while dampening it via credit displacement, deflating qualifiers, or surprise markers | "is now *actually* rolling out," "what it purports to be," "is finally addressing," "it took [external pressure] to get [entity] to," "credit where it's due, but" |

---

## Category 14: Procedural Compression

Devices that collapse multi-step processes into simplified binary constructions.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 96 | **Ultimatum Framing** | E | Multi-stage regulatory or legal proceeding (investigation → findings → response → decision → fine) compressed into a binary "do X or face Y" construction. Collapses procedural complexity into an "or else" fork. Distinct from regulatory_shadow (ambient fear), pressure_language (coercive verbs), and scale_magnitude (number amplification) | "change/fix X — or get/face Y," "must [action] or face [consequence]," "comply or face fines/penalties," "either [action] or [consequence]" |

---

## External Influence Vectors

These are not framing devices in the formal taxonomy but are tracked as editorial influence mechanisms documented in [METHODOLOGY.md §19](METHODOLOGY.md#19-external-editorial-influence-vectors-fellowship-programs):

| Vector | Description | Key Example |
|---|---|---|
| **Fellowship Programs** | Externally funded fellows placed at tracked publications | Tarbell Center for AI Journalism — fellows at The Verge, MIT Tech Review |

---

## Attribution Verb Quick Reference

| Category | Verbs | Signal |
|---|---|---|
| **Neutral** | said, told, noted, explained, stated, added, commented | Professional reporting |
| **Undermining** | claimed, argued, insisted, maintained, contended | Implies doubt |
| **Concessive** | admitted, conceded, acknowledged | Implies wrongdoing |
| **Adversarial** | warned, blasted, slammed, attacked, fired back | Implies conflict |

---

## Counts by Tier

| Tier | Count | Detection Method |
|---|---|---|
| Core | 10 | Pattern matching — fundamental editorial techniques |
| Extended | 85 | Pattern matching — discovered from real article analysis |
| Structural (post-pass) | 7 | Full-article heuristics (position, accumulation, structure) |
| **Total** | **102** | |

---

*Last updated: 2026-07-14. See [METHODOLOGY.md §4](METHODOLOGY.md#4-framing-device-detection) for full device descriptions, detection patterns, and discovery provenance articles.*

---

## Proposed Additions (Pending Validation)

Candidate framing devices discovered during analysis but not yet formally added. Each requires **≥3 independent real-article examples** demonstrating the pattern before promotion to the taxonomy.

| Candidate | Category | Description | Discovery Provenance | Examples Found | Status |
|-----------|----------|-------------|---------------------|----------------|--------|
| **Ironic Consolidation** | Narrative & Editorial Architecture | Bundling multiple independent negative narratives into a single article, connecting them with ironic thematic links to amplify perceived systemic failure. Distinct from `trend_bundling` (which groups similar actions by peers) — ironic consolidation groups *disparate* failures of a *single* entity. | Gizmodo siege roundup (Jul 2026) | 1 | Needs 2+ more |

### Proposed Correction Paths

| Candidate | Problem | Distinguishing Signal | Discovery Provenance | Status |
|-----------|---------|----------------------|---------------------|--------|
| **Path M — Structural Irony** | Macro-level article organization creates negative framing invisible at sentence level. VADER and even individual framing devices read each paragraph as neutral, but the *sequence* and *juxtaposition* of sections constructs an editorial argument. | Low adversarial_count + low EI + neutral agency, but manual assessment is clearly negative. Signal is in section ordering, not vocabulary. | Gizmodo siege roundup (Jul 2026) | Needs validation articles |

> **Note:** Path L (quote-inflated body with negative headline) is already implemented. This candidate uses the next available letter.

### Promotion Criteria

1. **≥3 independent articles** from ≥2 different publications demonstrating the pattern
2. **Distinguishable from existing devices** — must not overlap with conditions of any existing device type
3. **Measurable impact on scoring** — must cause a demonstrable gap between raw and manual assessment
4. **Regression tests** — at least one test per new device/path validating the discovery article
