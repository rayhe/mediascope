# Framing Device Quick Reference

> A compact lookup card for all 83 framing device types detected by MediaScope. For full descriptions, detection patterns, and discovery provenance, see [METHODOLOGY.md §4](METHODOLOGY.md#4-framing-device-detection).

---

## How to Use This Reference

During article analysis, scan the text for trigger keywords and structural patterns listed below. Each device name links to the detailed entry in METHODOLOGY.md. The **tier** column indicates detection method:

- **C** = Core (10 types) — fundamental editorial techniques, pattern-matched
- **E** = Extended (66 types) — discovered from real article analysis, pattern-matched
- **S** = Structural (7 types) — detected via post-pass heuristics over full article structure

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
| 34 | **Competitive Positioning** | E | Competitor explicitly elevated over subject entity | "good news for [competitor]," "buy from a more reputable company" |
| 35 | **Competitive Deficit** | E | Multiple named competitors enumerated to amplify subject's failure | "failed to rival [A]'s X, [B]'s Y, and [C]'s Z" — pile-on effect |
| 36 | **Industry Normalization Undercut** | E | Acknowledges industry-wide practice, then singles out target | "Other companies also X, but [Target] is especially…" |
| 37 | **Latecomer Narrative** | E | Company framed as entering a space after competitors | "joining the race," "playing catch-up," "copycat," "me-too product" |
| 38 | **Refusal Amplification** | E | Entity's non-cooperation emphasized beyond its news value | "declined," "refused," positioned to imply guilt |

---

## Category 5: Analogy, Metaphor & Comparison

Devices that use comparisons, metaphors, or precedents to import external associations.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 39 | **Analogy/Metaphor** | E | Explicit comparisons importing associations from another domain | "like crash-testing a car," "akin to," "equivalent of," "tantamount to" |
| 40 | **Analogy Stacking** | S | 3+ distinct analogies for the same subject amplify perceived severity | Multiple "the equivalent of," "likened it to," "compared it to" markers |
| 41 | **Scandal Comparison** | E | Notorious fraud/scandal name used as compact pejorative label | "AI Theranos," "the Enron of AI," "the next WeWork" |
| 42 | **Precedent Analogy** | E | Current controversy compared to well-known historical case | "echoes opioid-era fights," "much like the [precedent] litigation" |
| 43 | **Failure Precedent** | E | Prior failed attempt at same project type invoked to cast doubt | "was set to receive $X ... ultimately cancelled" |
| 44 | **Pathologizing Metaphor** | E | Corporate behavior cast as addiction, disease, or compulsive gambling | "addicted," "gorge itself," "high-rollers," "withdrawal," "insatiable" |
| 45 | **Commodification Metaphor** | E | Human identity/work flattened into interchangeable modules or tokens | "distill colleagues into skills," "reducing a person to a task" |
| 46 | **Anthropomorphization** | E | Human emotions/intentions ascribed to AI systems | "happily handed," "the confused bot," "without being taught how to" |
| 47 | **Military Techno-Optimism** | E | Violence normalized through technology/UX language | "Optimize the human as a weapons system," "AI-driven targeting" |

---

## Category 6: Denial, Reversal & Contradiction

Devices that frame changes of position, denials, or admissions.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 48 | **Denial Contradiction** | E | Source's denial placed alongside contradicting evidence | "does not exist" near code analysis; "misleading" + removal evidence |
| 49 | **Corporate Reassurance Undercut** | E | Corporate reassurance language immediately undercut by evidence | "carefully designed" + "but/however/yet" + failure evidence |
| 50 | **Usage Dismissal Undercut** | E | Corporate "most users don't" minimization challenged by journalist | "most users don't use X" near "but/however" + ownership argument |
| 51 | **Policy Reversal** | E | Change of position framed as flip-flop or inconsistency | "reversed course," "backtracked," "flip-flopped," "walked back" |
| 52 | **Strategic Reversal** | E | Company reversing a core strategic position | "a major departure from longtime philosophy," "chosen to abandon" |
| 53 | **Selective Rehabilitation** | E | Past controversy juxtaposed with current acceptance to imply opportunism | "Ousted from X... now welcomed at Y," "friendlier posture" |

---

## Category 7: Scale, Significance & Catastrophizing

Devices that amplify the magnitude, significance, or threatening nature of events.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 54 | **Catastrophizing** | C | Outcomes framed as existential or irreversible | "crisis," "catastrophe," "existential threat," "doomsday" |
| 55 | **Scale/Magnitude Framing** | E | Large raw numbers, calculated maximums, or scale analogies for impact | "up to 6% of global revenue," "enough to power 750,000 homes" |
| 56 | **Valuation Comparison** | E | Penalty/cost compared to market cap to imply existential threat | "$1.4 trillion ... market capitalization just above $1.5 trillion" |
| 57 | **Precedent Framing** | E | Event significance signaled through historical rarity | "first [X] in 17 years," "first [X] since YYYY," "unprecedented" |
| 58 | **Slippery Slope** | E | Specific action extrapolated to broader systemic threat | "sets an uncomfortable precedent," "if this approach extends," "opens the door to" |
| 59 | **Speculative Framing** | S | 5+ cumulative speculative hedges convert possibility into implied certainty | "could potentially," "might be able to," "could feasibly" stacked |

---

## Category 8: Regulatory & Legal Framing

Devices that shape how regulatory, legal, and government actions are presented.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 60 | **Litigation Framing** | C | Entity framed as adversarially using courts | "filing/mounting legal challenge," "legal battle against," "took X to court" |
| 61 | **Regulatory Shadow** | E | Regulatory context inserted into product stories where tangential | "increasing scrutiny," "amid antitrust," "could face regulatory" |
| 62 | **Regulatory Favoritism** | E | Government oversight framed as picking winners and losers | "picking winners and losers," "favorable treatment," "tilting the playing field" |
| 63 | **Geopolitical Regulatory Pressure** | E | Regulatory tensions framed as geopolitical confrontation | Embassy/diplomatic submissions, sovereignty/defiance rhetoric |
| 64 | **Strategic Disclosure** | E | Party in dispute discloses opponent's position to frame it as extreme | "Meta said in a recent court filing" — framing originates with disclosing party |
| 83 | **Default Burden Privacy** | E | Default-on feature framed as consent violation by emphasising opt-out burden | "enabled by default," "opt-out," "users may not know," "without consent" |

---

## Category 9: Narrative & Editorial Architecture

Devices that construct or redirect overarching narrative frames.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 65 | **False Balance** | C | Fringe views presented as equivalent to mainstream | "some say... others say" with asymmetric evidence |
| 66 | **Selective Omission Signal** | C | Notable absences detectable in text | "declined to comment" without context, missing competitor comparison |
| 67 | **Straw Man** | E | Entity's position misrepresented to make it easier to attack | Simplified-claim-then-rebut constructions |
| 68 | **Narrative Reframing** | E | Existing narrative acknowledged then dismissed as incomplete | "That concern is fair. It is also incomplete," "The lazy version says" |
| 69 | **Editorial Deflation** | E | Ambitious vision built up across paragraphs, then punctured | "That's the idea, anyway," "or so X claims," "if it ever actually works" |
| 70 | **Prescriptive Solutionism** | E | Accountability story transformed into management playbook | "actionable steps for IT leaders," "executives must balance/evaluate" |
| 82 | **Tempering Coda** | S | Article ends by contextualizing or walking back its own headline-level framing | Final 25% contains explicit moderating language ("likely far higher than," "in context") contradicting headline severity |

---

## Category 10: Personnel & Labor Framing

Devices specific to workforce, employment, and organizational coverage.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 71 | **Worker Replacement Irony** | E | Workers who built/trained the AI now replaced by it | "trained AI models now face replacement by those same systems" |
| 72 | **Two-Tier Treatment** | E | Full-time vs. contractor treatment contrasted side by side | "[employees] receive X... [contractors] get far less" |
| 73 | **Talent Hemorrhage** | E | Multiple departures cataloged in sequence to build exodus narrative | "left for [Company]... recently left... is also leaving" |
| 74 | **Repeated Disruption** | E | Language implying chronic organizational instability | "shakes up... again," "yet another restructuring," "months of tumult" |
| 75 | **Absence as Evidence** | E | Non-action or omission framed as proof of guilt | "the audit that never happened," "has never disclosed," "failed to act" |
| 76 | **Silence as Guilt** | E | Non-response explicitly treated as confession | "That silence is its own answer," "the lack of denial speaks volumes" |

---

## Category 11: Consumer & Product Framing

Devices specific to consumer technology, product reviews, and subscription/pricing coverage.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 77 | **Consumer Ownership** | E | Corporate restriction framed as violating what consumer "already paid for" | "hardware you've already paid for," "runs entirely on the device" + "subscription" |
| 78 | **Loss-Leader Framing** | E | Hardware sold at cost to capture subscription revenue | "sold at cost," "user base grows, subscription service grows revenue" |

---

## Category 12: Financial & Investor Media Framing

Devices specific to financial journalism, earnings coverage, and analyst reporting.

| # | Device | Tier | One-Line Description | Key Triggers |
|---|--------|------|----------------------|-------------|
| 79 | **Financial Reassurance** | E | Negative operational news immediately reframed as positive market signal | "could soothe concerns," "easing fears," "investors shrugged off" |
| 80 | **Historical Legitimation** | E | Temporally distant positive data inserted to dilute fresh negative news | "reported [quarter] results ... beat/topped expectations" in negative-news article |
| 81 | **Marginal Endorsement** | E | Analyst action of negligible magnitude presented as meaningful signal | Price target raise of <1% framed as "analysts remain bullish" |

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
| Extended | 66 | Pattern matching — discovered from real article analysis |
| Structural (post-pass) | 7 | Full-article heuristics (position, accumulation, structure) |
| **Total** | **83** | |

---

*Last updated: 2026-07-08. See [METHODOLOGY.md §4](METHODOLOGY.md#4-framing-device-detection) for full device descriptions, detection patterns, and discovery provenance articles.*
