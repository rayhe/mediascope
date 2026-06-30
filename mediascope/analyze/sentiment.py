"""Multi-model sentiment analysis for media coverage asymmetry detection.

Provides VADER and TextBlob baselines plus a composite analyzer that
calculates 8 sentiment dimensions for nuanced coverage analysis.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

logger = logging.getLogger(__name__)

# Singleton VADER analyzer
_vader = SentimentIntensityAnalyzer()

# --- Anonymous source patterns ---
ANONYMOUS_SOURCE_PATTERNS: list[re.Pattern] = [
    re.compile(r"\baccording to (?:people|sources|individuals|persons)\b", re.IGNORECASE),
    re.compile(r"\bpeople familiar with\b", re.IGNORECASE),
    re.compile(r"\bspoke (?:with \w+ )?on (?:the )?condition (?:of )?(?:anonymity)?\b", re.IGNORECASE),
    re.compile(r"\basked not to be identified\b", re.IGNORECASE),
    re.compile(r"\bpeople who requested anonymity\b", re.IGNORECASE),
    re.compile(r"\ba person with (?:direct )?knowledge\b", re.IGNORECASE),
    re.compile(r"\bsources (?:said|told|indicated|suggested|confirmed|added)\b", re.IGNORECASE),
    re.compile(r"\bpeople (?:said|told|indicated|suggested|confirmed|added)\b", re.IGNORECASE),
    re.compile(r"\baccording to (?:two|three|four|five|several|multiple) people\b", re.IGNORECASE),
    re.compile(r"\bsomeone (?:close to|briefed on|with knowledge)\b", re.IGNORECASE),
    re.compile(r"\binsiders?\b", re.IGNORECASE),
    re.compile(r"\ba (?:former|current) (?:employee|executive|official) who\b", re.IGNORECASE),
    # Publication-as-source patterns (journalist withholding their own source)
    re.compile(r"\b\w+ has learned\b", re.IGNORECASE),
    re.compile(r"\bobtained by \w+\b", re.IGNORECASE),
    re.compile(r"\breviewed by \w+\b", re.IGNORECASE),
    re.compile(r"\ba source (?:with knowledge|close|familiar|briefed|told|said|confirmed)\b", re.IGNORECASE),
    re.compile(r"\bmultiple sources (?:confirm|said|told)\b", re.IGNORECASE),
    # Unnamed/unidentified descriptor patterns — catch anonymous sources described
    # by role rather than by the standard "spoke on condition of anonymity" phrases
    re.compile(r"\ban? unnamed (?:worker|employee|executive|official|source|person|staffer|engineer)\b", re.IGNORECASE),
    re.compile(r"\ban? (?:second|third|fourth|another) (?:worker|employee|source|person|engineer)\b", re.IGNORECASE),
    re.compile(r"\b(?:one|another|a) (?:worker|employee|engineer|staffer) (?:said|told|called|described|complained)\b", re.IGNORECASE),
    re.compile(r"\ban? (?:worker|employee|engineer|staffer) (?:was quoted|was reported)\b", re.IGNORECASE),
    re.compile(r"\b(?:some|several|multiple|many|other) (?:workers|employees|engineers|staffers|people) (?:said|told|described|complained|called)\b", re.IGNORECASE),
    # Publication-investigative patterns
    re.compile(r"\b\w+ (?:found|reported|revealed) (?:widespread|significant|extensive|growing)\b", re.IGNORECASE),
    # UK-style passive institutional attribution — common in Guardian/UK press.
    # "it is understood that ministers are mindful" positions an institutional
    # claim as background knowledge without naming any source at all.
    re.compile(r"\bit is understood (?:that )?\b", re.IGNORECASE),
    re.compile(r"\bit is believed (?:that )?\b", re.IGNORECASE),
    re.compile(r"\bit is thought (?:that )?\b", re.IGNORECASE),
    re.compile(r"\bit has emerged (?:that )?\b", re.IGNORECASE),
    # Numbered officials/people as anonymous sources — very common in NYT-style
    # government and policy reporting: "two government officials said",
    # "four people familiar with", "three administration officials confirmed"
    re.compile(r"\b(?:two|three|four|five|six|seven|several|multiple) (?:government|administration|intelligence|defense|senior|federal|White House|Commerce|State Department) (?:officials?|aides?|advisers?|staffers?) (?:said|told|confirmed|added|indicated)\b", re.IGNORECASE),
    # "one/a person involved in / close to / inside / with the" — person described
    # by proximity/involvement rather than by "knowledge of"
    re.compile(r"\b(?:one|a) person (?:involved in|close to|inside|with the|within the|privy to|briefed on|engaged in) (?:the )?(?:process|matter|talks?|discussions?|negotiations?|deliberations?|effort|planning)\b", re.IGNORECASE),
    # "one/a senior [party/adjective]? [title]" — unnamed political/industry
    # figures described by seniority + role: "one senior Republican congressman",
    # "a senior Meta executive", "one prominent industry analyst".
    re.compile(
        r"\b(?:one|a)\s+(?:senior|prominent|high-ranking|top|leading|key)\s+"
        r"(?:Republican|Democrat|Democratic|Labour|Conservative|Tory|"
        r"White House|Pentagon|administration|government|industry|tech|"
        r"Meta|Google|Apple|Amazon|Microsoft|intelligence|military|"
        r"congressional|Senate|House)?\s*"
        r"(?:congressman|congresswoman|senator|lawmaker|legislator|"
        r"official|executive|adviser|advisor|aide|diplomat|analyst|"
        r"figure|member|source|insider|person)\b",
        re.IGNORECASE,
    ),
]

# Named source patterns — look for "Name said", "said Name", "according to Name"
NAMED_SOURCE_PATTERNS: list[re.Pattern] = [
    # "Name said" / "Name told" — capitalized name followed by attribution verb
    # Includes both past and present tense forms (see sources.py for rationale)
    re.compile(
        r"\b([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+)\s+"
        r"(?:said|says|told|tells|stated|states|noted|notes|explained|explains|"
        r"argued|argues|claimed|claims|insisted|insists|warned|warns|added|adds|"
        r"commented|comments|confirmed|confirms|acknowledged|acknowledges|"
        r"revealed|reveals|described|describes|agreed|agrees)\b"
    ),
    # "said Name" — attribution verb followed by capitalized name
    re.compile(
        r"\b(?:said|says|told|tells|stated|states|noted|notes|explained|explains|"
        r"argued|argues|claimed|claims|insisted|insists|warned|warns|added|adds|"
        r"commented|comments|confirmed|confirms|acknowledged|acknowledges|"
        r"revealed|reveals|described|describes|agreed|agrees)\s+"
        r"([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+)\b"
    ),
    # "according to Name"
    re.compile(
        r"\baccording to ([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+)\b"
    ),
    # "Name, who/the CEO/a spokesperson" — name with title
    re.compile(
        r"\b([A-Z][a-z]+ (?:[A-Z]\. )?[A-Z][a-z]+),\s+"
        r"(?:who|the|a|an|chief|CEO|president|director|spokesperson|head)\b"
    ),
]

# Speculative language indicators
SPECULATIVE_PHRASES: list[str] = [
    "could", "might", "may", "reportedly", "allegedly", "apparently",
    "is expected to", "is said to", "is believed to", "is thought to",
    "is rumored to", "is likely to", "is unlikely to",
    "sources say", "some say", "it is unclear", "remains to be seen",
    "raises questions", "raises concerns", "it appears",
    "seems to", "appeared to", "suggesting that", "suggesting",
    "potentially", "possibly", "perhaps", "probably",
]

# Emotional / loaded language indicators
EMOTIONAL_LANGUAGE: list[str] = [
    "shocking", "outrageous", "alarming", "devastating", "horrifying",
    "explosive", "bombshell", "stunning", "jaw-dropping", "terrifying",
    "unprecedented", "catastrophic", "disastrous", "scandalous",
    "shameful", "disgraceful", "appalling", "egregious", "reckless",
    "sinister", "insidious", "toxic", "predatory", "ruthless",
    "brazen", "defiant", "embattled", "beleaguered", "under fire",
    "under siege", "slammed", "blasted", "hammered", "crushed",
    "destroyed", "eviscerated", "torched", "ripped", "grilled",
    "excoriated", "lambasted",
    # Workplace/organizational emotional terms
    "soul-crushing", "soul crushing", "brutal", "atrocious",
    "drudge", "drudgery", "gulag", "hell", "humiliation",
    "disposable", "demoralized", "demoralizing", "disgruntled",
    "fury", "furious", "revolt", "rage", "nightmare",
    "horror", "excruciating", "hellish", "grueling",
    # Workplace morale/dysfunction emotional terms — needed for corporate
    # reporting on layoffs, restructuring, and internal dissent
    "horrifically", "grim", "grimly", "cruel", "cruelty",
    "belittled", "belittling", "berated", "berating",
    "shattered", "shattering", "zealots", "zealotry",
    "insane", "rock-bottom", "rock bottom",
    "anger", "angry", "angst", "fearful", "frustrating",
    "frustrated", "frustration", "unhappy", "unhappiness",
    "miserable", "misery", "despair", "despairing", "morale",
    "plummeted", "plunging", "collapsed", "collapse",
    "feign empathy", "dark mood", "historically low",
    "severed", "broken", "eroded", "erosion",
    "widespread dissatisfaction", "widespread discontent",
    "recruiting crisis", "talent exodus", "brain drain",
    # Workplace revolt / dissent emotional terms
    "revolted", "rebellion", "rebel",
    "callous", "callousness", "antisocial",
    "nihilistic", "nihilism", "dystopian", "Orwellian",
    "downright ugly", "ugly truth",
    "train your own replacement", "training their replacements",
    "Big Beautiful Layoff",
    # Privacy/surveillance emotional terms
    "surveillance", "biometric surveillance", "mass identification",
    "faceprints", "faceprint", "vacuum up", "weaponized",
    "stalkers", "stalking", "abusers", "covert filming",
    "vile", "vile behavior", "invasive",
    # Legal/censorship/power-abuse emotional terms
    "censorship", "silenced", "silencing", "silence", "gagged", "gag order",
    "muzzled", "hostage", "hostage situation",
    "despotic", "tyranny", "tyrannical", "oppressive", "oppression",
    "trolling", "intimidate", "intimidation", "bankrupt", "bankruptcy",
    "sanctioned", "sanctions motion", "punitive", "punishing",
    "chilling", "chilling effect", "suppress", "suppression",
    "retaliation", "retaliatory", "retaliating", "stifle", "stifled",
    # Legal/whistleblower coverage emotional terms — coercion, fear, and
    # character-attack language frequently deployed in articles about
    # corporate silencing of critics, NDAs, and whistleblower disputes.
    # Gap discovered during Fast Company Wynn-Williams analysis (Jun 2026):
    # outsourced_intensity returned 0.0 because quoted text containing
    # "strike fear," "abusive," "greed," "unlawful" had no matching terms.
    "abusive", "abuse", "fear", "greed", "greedy",
    "unlawful", "strike fear", "struck fear",
    "coercive", "coercion", "duress",
    "defamatory", "disparaging", "indefensible",
    "riddled",
    # Military/defense/weapons emotional terms — needed for coverage of
    # military-tech partnerships, defense contracts, and armed systems
    # where the language of violence reads as factual to VADER but carries
    # strong editorial weight in a consumer-tech publication context
    "drone strike", "drone strikes", "ordering drone strikes",
    "weapons system", "weapons systems", "weapon system",
    "cyborg", "cyborg-inspired",
    "lethal", "lethal force", "lethal autonomous",
    "kill chain", "kill box",
    "escalation", "major escalation",
    "shockwaves", "shockwave", "sent shockwaves",
    "tumultuous", "crackdown", "upheaval",
    "fortify", "fortified", "fortifying",
    "massive new risks", "massive risks",
    "imperfect AI", "imperfect AI systems",
    "ousted", "ousting",
    "information overload",
    "money pit",
    "colossal",
    "wasted",
    # Consumer privacy / wearable-tech emotional terms — needed for
    # coverage of smart glasses, facial recognition, and surveillance tech
    # where editorial language deploys pejorative labels and predatory
    # framing that VADER reads as neutral
    "creep", "creepy", "creepier", "creepiest", "creeps",
    "pervert", "perverted", "perversion", "pervert glasses",
    "prowling", "prowl",
    "infested", "infestation",
    "violation", "violated", "violating",
    "unsettling", "unsettled",
    "contemptuous", "contempt",
    "harassment", "harassing", "harassed", "harass",
    "sexist", "sexism",
    "disturbing", "disturbed", "disturbingly",
    "off-putting",
    "pestering", "pester",
    "corny",
    "stealth mode",
    "bystander", "bystanders",
    "authoritarian",
    "trolls", "troll",
    "backlash",
    "inconspicuous",
    # Platform death / community displacement emotional terms — needed for
    # coverage of platform shutdowns where editorial language frames corporate
    # decisions as community destruction or abandonment
    "devastated", "devastation",
    "on life support", "life support",
    "eerily silent", "eerily", "eerie",
    "abandoned", "abandoning", "abandonment",
    "displaced", "displacement",
    "shutdown whiplash", "whiplash",
    "killed", "killing",
    "broke down in tears", "broke down",
    "going away", "disappearing",
    "terrified",
    "anxious", "anxiety",
    "reluctance", "reluctant",
    "hesitant",
    # Cultural criticism / AI slop emotional terms — needed for coverage
    # of AI-generated content flooding, synthetic media critique, and
    # cultural erosion framing where editorial deploys visceral language
    # that VADER reads as neutral
    "narcotic", "narcotic effect",
    "stupefying", "stupefied",
    "soulless", "soul-less",
    "nightmarish",
    "meaninglessness", "meaningless",
    "disorientation", "disorienting",
    "recursive", "recursiveness",
    "corrosive", "corroding", "erode",
    "pervasive",
    "polluted", "pollution", "polluting",
    "degrade", "degraded", "degrading",
    "slop", "sloppy",
    "unsatisfying", "wholly unsatisfying",
    "contextless",
    "never-ending",
    "frictionless", "frictionlessness",
    # Vulnerability / accessibility emotional terms — disability, elderly,
    # isolation, and mental health framing deployed to create sympathy
    "disability", "disabled",
    "limited mobility", "mobility",
    "social anxiety", "depression",
    "nowhere else", "no barrier",
    "mental health",
    "from your bed", "in your pajamas",
    # Cybersecurity / data-breach emotional terms — needed for security
    # reporting which uses domain-specific loaded language that reads as
    # neutral to VADER but carries strong negative editorial framing
    "hack", "hacked", "hacking", "hacker", "hackers",
    "breach", "breached", "breaches",
    "exploit", "exploited", "exploits", "exploiting",
    "vulnerability", "vulnerabilities", "vulnerable",
    "steal", "stolen", "stealing", "stole",
    "attack", "attackers", "attacked", "attacking",
    "hijack", "hijacked", "hijacking",
    "compromised", "compromise",
    "malicious", "malware",
    "embarrassing", "embarrassment",
    "negligent", "negligence",
    "recklessness",
    # Gambling/addiction/exploitation emotional terms — needed for coverage
    # of prediction markets, platform addiction, and exploitation framing
    # where editorial prose links corporate products to addictive behaviour.
    # Detected in Gizmodo "Worst Instincts" Arena article (Jun 2026):
    # 0.159 emotional intensity vs manual 0.90 — toolkit was missing these.
    "addicted", "addictive", "addiction", "addictions",
    "gambling", "gamble", "gambler", "gamblers",
    "dopamine", "dopamine hit",
    "worst instincts", "worst impulses",
    "pathetic",
    "plague",
    "notorious", "notoriously",
    "knockoff", "knockoffs", "clone", "clones",
    "horniness",
    "destroying",
    "destructive", "destructive behaviors",
    "cash in on", "cashing in on",
    "bread and butter",
    "pitted people against",
    "scraped",
    # Corporate character-attack emotional terms — op-ed/essay framing that
    # builds a character indictment through accumulated pejorative language
    "dumb fucks", "dumb f*cks",
    "liable", "found liable",
    "unwitting", "unwitting users",
    "worst of people",
    # Workplace discontent / internal morale — moderate emotional language
    # frequently used in employee dissent articles and leaked internal comms.
    # Lower intensity than sensationalist terms but cumulatively shapes tone.
    "disappointing", "disappointed",
    "discouraged", "disbelief", "skeptical", "skepticism",
    "sarcastic", "pushback", "unimpressed",
    "chaotic", "overburdened", "distress",
    "preoccupied", "tone-deaf", "performative",
    # Infrastructure / community-impact emotional terms — needed for
    # coverage of data centers, resource extraction, environmental harm,
    # and tech-industry impact on communities. Gap discovered during MIT TR
    # "Data centers are amazing. Everyone hates them." analysis (Jan 2026).
    "incensed", "infuriates", "infuriated", "infuriating",
    "eyesore", "eyesores",
    "came gunning for", "gunning for",
    "powerless", "powerlessness",
    "gentrification", "gentrified", "gentrifying",
    "dirty",
    "shrouded in secrecy", "shrouded",
    "skyrocketing", "skyrocketed",
    "noisy", "constant hum",
    "NIMBY",
    "California billionaires",
    # Political rhetoric / dismissive language — pejorative labels and
    # loaded idioms common in political-tech intersection coverage where
    # policy proposals are framed through partisan lens.  Gap discovered
    # in Gizmodo "Kids Over Clicks" / Project 2029 article (Jun 2026):
    # "hucksters", "robbed blind", "carved up" all went undetected.
    "hucksters", "huckster",
    "robbed blind", "robbing blind",
    "carved up", "carving up",
    "grifter", "grifters", "grift",
    "con man", "con men", "con artist",
    "shakedown",
    "racket", "racketeer",
    "swindler", "swindled",
    "charlatans", "charlatan",
    "snake oil", "snake-oil",
    "peddling", "peddle",
    "duped", "duping",
    "bamboozled",
    "fleeced", "fleecing",
    "looted", "looting",
    "plundered", "plundering",
    # AI labor/displacement emotional terms — needed for coverage of AI
    # agents, automation, and workforce disruption where editorial and
    # quoted language deploys displacement anxiety, delegitimizing labels,
    # and doom framing that reads as measured academic critique but carries
    # strong emotional load.  Gap discovered during MIT TR "AI agents are
    # not your coworkers" analysis (Jun 2026): outsourced_intensity returned
    # 0.0 for Acemoglu quote containing "losing proposition," "replace
    # humans" because these terms had no match.
    "losing proposition", "losing propositions",
    "replace humans", "replacing humans",
    "replace workers", "replacing workers",
    "replace employees", "replacing employees",
    "unrealistic expectations",
    "dump blame", "dumping blame", "offload blame",
    "offload accountability", "offloading accountability",
    "hot air",
    "overhyped", "overhype", "over-hyped",
    "branding exercise",
    "job displacement",
    "automating away", "automated away",
    "deskilling", "deskilled",
    "devaluing", "devalue", "devalued",
    "commodify", "commodified", "commodifying",
    "expendable",
    "obsolete", "obsolescence",
]

# Passive/victim vs. active/powerful framing indicators
PASSIVE_FRAMING: list[str] = [
    "was forced to", "had to", "was compelled", "was pressured",
    "faces criticism", "faces backlash", "under scrutiny",
    "was hit by", "was plagued by", "was rocked by",
    "struggled", "stumbled", "faltered", "fumbled",
    "failed to", "refused to", "declined to comment",
    "came under fire", "was accused of", "was blamed for",
    "would say almost nothing", "would not say",
    "declined to answer", "declined to respond",
    "quietly built", "quietly removed", "quietly deleted",
    "secretly", "covertly", "surreptitiously", "discreetly",
    # Workplace/organizational passive framing
    "felt they had to", "had little choice", "had little real choice",
    "felt coerced", "were drafted", "were reassigned",
    "dropped to levels", "morale dropped", "anxiety has lingered",
    "dissatisfaction", "frustration", "unrest",
    # Legal silencing / corporate power framing
    "forced to sit in silence", "unable to speak", "unable even to nod",
    "forced into silence", "sat in silence", "sit in silence",
    "threatened with bankruptcy", "threatened her",
    "on the eve of publication", "fines of",
    "formally sanctioned", "legal order", "legal restrictions",
    "mounting legal restrictions", "legal action",
    "emergency legal order", "emergency arbitration",
    "arbitration order", "sanctions motion",
    # Regulatory non-cooperation / compliance holdout framing — common in
    # government-pressure articles where the subject is positioned as the
    # sole non-cooperator.  Detected in NYT voluntary-review article where
    # "has not agreed to" and "holdout" were unmatched by any framing list.
    "has not agreed to", "has not agreed",
    "has not reached an agreement", "has not reached agreement",
    "has not signed", "has not signed an agreement",
    "has not accepted", "has not submitted",
    "holdout", "lone holdout",
    "has not complied", "has not cooperated",
    "has not committed", "has not joined",
    "is pressing", "pressing it to",
    # Workplace coercion / compulsion passive framing
    "no option to opt-out", "no option to opt out",
    "there is no option", "there is no opt-out",
    "cannot opt out", "cannot opt-out",
    "opt-out is not possible", "no way to opt out",
    "opting out is not possible",
    # Tech responsibility / security failure framing — common in
    # cybersecurity and product safety reporting where the subject is
    # framed as negligently passive
    "slipped through", "fell through the cracks",
    "should have been", "could have been prevented",
    "did not respond", "has not commented",
    "did not respond to a request",
    "were there even", "raises questions",
    "tricked", "was tricked", "can be tricked",
    "did not mention", "has not addressed",
    # Platform death / corporate abandonment passive framing — editorial
    # language positioning users as victims of corporate platform shutdowns,
    # pivots, or community abandonments
    "on life support", "just disappearing", "going away",
    "shutting down", "shut down", "pulling away",
    "killing it", "killed it",
    "slowing down", "winding down",
    "no more new", "no longer be able",
    "nowhere else to go", "nowhere else",
    "not sure where", "aren't sure what comes next",
    "terrified of the uncertainty",
]

ACTIVE_FRAMING: list[str] = [
    "announced", "launched", "unveiled", "pioneered", "led",
    "spearheaded", "championed", "drove", "transformed",
    "innovated", "invested", "expanded", "committed to",
    "doubled down on", "accelerated", "delivered",
    "outperformed", "exceeded expectations", "set a record",
    # CEO directive verbs — active positive agency where a leader
    # is proactively directing strategy.  Detected in NYT Arena
    # article (Jun 2026): "urged his lieutenants", "dispatched a
    # small team" scored 0.0 agency vs manual +0.50.
    "urged", "dispatched", "directed", "instructed",
    "rallied", "mobilized", "greenlit", "fast-tracked",
]

# Active-NEGATIVE framing: the subject is the agent, but the actions are
# harmful, coercive, or destructive.  These are NOT "passive/victim" framing
# (the subject isn't being *done to*); the subject is *doing* things that
# the editorial presents as harmful.  Counting these as positive-agency
# inflates the score on articles about corporate actions like layoffs,
# surveillance, forced adoption, etc.
ACTIVE_NEGATIVE_FRAMING: list[str] = [
    "tracking", "tracked", "surveilling", "monitoring",
    "laying off", "laid off", "slashing", "slashed", "cutting jobs",
    "cutting staff", "cutting workers", "eliminating jobs",
    "eliminating positions", "firing", "downsizing",
    "forcing", "forced", "mandating", "mandated",
    "requiring", "required employees", "compelling",
    "harvesting", "capturing", "extracting",
    "pushing employees", "pressuring employees",
    "factoring their use",
]

# Comparative framing indicators
NEGATIVE_COMPARISON: list[str] = [
    "lags behind", "falls short", "trails", "unlike",
    "while competitors", "compared unfavorably", "worse than",
    "less than", "behind", "failed where", "losing to",
    "outpaced by", "overshadowed by",
]

POSITIVE_COMPARISON: list[str] = [
    "leads", "ahead of", "outperforms", "surpasses",
    "dominates", "eclipses", "outshines", "beats",
    "better than", "exceeds", "tops",
    # NOTE: "more than" REMOVED (2026-06-23) — it false-positives on
    # quantitative phrases like "more than 50 million phones" which are
    # not comparative framing.  Detected in WIRED NameTag deep dive:
    # "more than 50 million phones" scored as positive comparison.
]


@dataclass
class SentimentResult:
    """Multi-dimensional sentiment analysis result.

    Eight dimensions capture different aspects of media framing
    beyond simple positive/negative sentiment.  When adversarial
    framing is strong enough to override VADER/TextBlob polarity,
    ``framing_corrected`` is set to ``True`` and ``raw_tone``
    preserves the uncorrected composite for comparison.
    """

    overall_tone: float = 0.0                  # -1.0 to 1.0
    emotional_language_intensity: float = 0.0  # 0.0 to 1.0
    source_authority_framing: float = 0.0      # -1.0 to 1.0
    agency_attribution: float = 0.0            # -1.0 to 1.0
    headline_body_alignment: float = 0.0       # -1.0 to 1.0
    anonymous_source_ratio: float = 0.0        # 0.0 to 1.0
    speculative_language_ratio: float = 0.0    # 0.0 to 1.0
    comparative_framing: float = 0.0           # -1.0 to 1.0
    # Framing-correction metadata
    framing_corrected: bool = False            # True when framing override fired
    raw_tone: float = 0.0                      # uncorrected VADER+TextBlob blend


def analyze_vader(text: str) -> dict:
    """Run VADER sentiment analysis on text.

    Args:
        text: Text to analyze.

    Returns:
        Dict with keys: neg, neu, pos, compound (-1 to 1).
    """
    if not text:
        return {"neg": 0.0, "neu": 1.0, "pos": 0.0, "compound": 0.0}
    return _vader.polarity_scores(text)


def analyze_textblob(text: str) -> dict:
    """Run TextBlob sentiment analysis on text.

    Args:
        text: Text to analyze.

    Returns:
        Dict with keys: polarity (-1 to 1), subjectivity (0 to 1).
    """
    if not text:
        return {"polarity": 0.0, "subjectivity": 0.0}
    blob = TextBlob(text)
    return {
        "polarity": blob.sentiment.polarity,
        "subjectivity": blob.sentiment.subjectivity,
    }


def count_anonymous_sources(text: str) -> tuple[int, int]:
    """Count anonymous and total source attributions in text.

    Delegates to the comprehensive ``extract_sources()`` in the sources
    module, which uses role-descriptor patterns, reverse-order attribution,
    and other structural heuristics that catch far more anonymous sources
    than simple regex patterns (e.g. "a policy staffer says", "the
    Instagram employee says").

    Falls back to the legacy regex-based counter if the sources module
    import fails (e.g. during isolated unit testing).

    Args:
        text: Article text to analyze.

    Returns:
        Tuple of (anonymous_source_count, total_source_count).
    """
    try:
        from mediascope.analyze.sources import extract_sources
        sources = extract_sources(text)
        # Exclude no_comment signals (e.g. "did not respond to a request
        # for comment") — these are editorial signals, not source attributions,
        # and should not inflate named/anonymous counts.
        sources = [s for s in sources if getattr(s, "source_type", "named") != "no_comment"]
        anonymous_count = sum(1 for s in sources if s.is_anonymous)
        total = len(sources)
        return anonymous_count, total
    except ImportError:
        pass

    # Legacy fallback: regex-based counting
    anonymous_count = 0
    for pattern in ANONYMOUS_SOURCE_PATTERNS:
        anonymous_count += len(pattern.findall(text))

    named_count = 0
    for pattern in NAMED_SOURCE_PATTERNS:
        named_count += len(pattern.findall(text))

    total = anonymous_count + named_count
    return anonymous_count, total


def measure_speculative_language(text: str) -> float:
    """Measure the ratio of speculative language in text.

    Args:
        text: Article text to analyze.

    Returns:
        Float between 0.0 and 1.0 representing the density of
        speculative phrases relative to text length.
    """
    if not text:
        return 0.0

    text_lower = text.lower()
    word_count = max(len(text.split()), 1)
    spec_count = 0

    for phrase in SPECULATIVE_PHRASES:
        # Count occurrences of each phrase
        escaped = re.escape(phrase)
        matches = re.findall(rf"\b{escaped}\b", text_lower)
        spec_count += len(matches)

    # Normalize: speculative phrases per 100 words, capped at 1.0
    ratio = min(spec_count / (word_count / 50), 1.0)
    return round(ratio, 4)


# Technical/domain vocabulary that should be downweighted when the article
# context is clearly about that domain (e.g. a cybersecurity article using
# "hack", "exploit", "vulnerability" as neutral technical terms).
_SECURITY_TECHNICAL_TERMS: set[str] = {
    "hack", "hacked", "hacking", "hacker", "hackers",
    "attack", "attacks", "attacked", "attacker", "attackers",
    "exploit", "exploits", "exploited",
    "vulnerability", "vulnerabilities", "vulnerable",
    "hijack", "hijacked", "hijacking",
    "breach", "breached", "breaches",
    "malware", "phishing", "spyware", "ransomware",
    "threat", "threats",
}

# Signals that an article is primarily about cybersecurity/security topics
_SECURITY_CONTEXT_SIGNALS: set[str] = {
    "cybersecurity", "red-teaming", "red teaming", "prompt injection",
    "guardrails", "agent security", "ai security", "ai agent",
    "account recovery", "account takeover", "credential",
    "two-factor authentication", "multi-factor authentication",
}


def _is_security_context(text_lower: str) -> bool:
    """Detect whether article is primarily about cybersecurity topics.

    When True, standard security vocabulary (hack, attack, exploit, etc.)
    should be downweighted in emotional intensity scoring because these
    terms are neutral technical language in this domain.
    """
    signal_count = sum(
        1 for term in _SECURITY_CONTEXT_SIGNALS
        if term in text_lower
    )
    return signal_count >= 2


def _measure_emotional_intensity(text: str) -> float:
    """Measure emotional/loaded language intensity.

    Returns a 0.0–1.0 score based on density of emotional terms.
    Domain-aware: in cybersecurity articles, standard security vocabulary
    (hack, attack, exploit, vulnerability) is downweighted because these
    are neutral technical terms, not emotional language.
    """
    if not text:
        return 0.0

    text_lower = text.lower()
    word_count = max(len(text.split()), 1)
    emotional_count = 0
    is_security = _is_security_context(text_lower)

    for term in EMOTIONAL_LANGUAGE:
        escaped = re.escape(term)
        matches = re.findall(rf"\b{escaped}\b", text_lower)
        match_count = len(matches)
        if match_count > 0:
            # Downweight security technical terms in security-context articles
            if is_security and term.lower() in _SECURITY_TECHNICAL_TERMS:
                match_count = match_count * 0.15  # 85% discount
            emotional_count += match_count

    # Normalize: scale so 2.5 emotional terms per 100 words = 1.0
    # (previous threshold of 1/100 was far too sensitive — any article
    # with standard descriptive language maxed out immediately)
    intensity = min(emotional_count / (word_count / 100) / 2.5, 1.0)
    return round(intensity, 4)


def _measure_agency(text: str) -> float:
    """Measure agency attribution framing.

    Returns -1.0 (passive/victim OR active-negative) to 1.0 (active/powerful/positive).
    Active-negative framing (the subject is the agent but performs harmful
    actions) counts as negative agency because the editorial effect is
    the same as passive framing: the subject is positioned unfavourably.
    """
    if not text:
        return 0.0

    text_lower = text.lower()
    passive_count = 0
    active_count = 0
    active_neg_count = 0

    for phrase in PASSIVE_FRAMING:
        escaped = re.escape(phrase)
        passive_count += len(re.findall(rf"\b{escaped}\b", text_lower))

    for phrase in ACTIVE_FRAMING:
        escaped = re.escape(phrase)
        active_count += len(re.findall(rf"\b{escaped}\b", text_lower))

    for phrase in ACTIVE_NEGATIVE_FRAMING:
        escaped = re.escape(phrase)
        active_neg_count += len(re.findall(rf"\b{escaped}\b", text_lower))

    # Active-negative counts against the subject (like passive framing)
    negative_total = passive_count + active_neg_count
    total = negative_total + active_count
    if total == 0:
        return 0.0

    # Scale from -1 (all passive/active-negative) to +1 (all active-positive)
    score = (active_count - negative_total) / total
    return round(score, 4)


def _measure_source_authority(text: str) -> float:
    """Measure how sources are used to frame the subject.

    Returns -1.0 (sources used to undermine) to 1.0 (sources validate).
    Based on ratio of named vs anonymous sources and attribution verb tone.
    """
    anon_count, total_count = count_anonymous_sources(text)

    if total_count == 0:
        return 0.0

    # More named sources = higher authority framing
    # More anonymous sources = lower authority framing
    named_count = total_count - anon_count
    score = (named_count - anon_count) / total_count
    return round(score, 4)


def _measure_headline_alignment(headline: str, body: str) -> float:
    """Measure how well the headline represents the article body.

    Compares sentiment direction between headline and body.
    Returns -1.0 (contradictory) to 1.0 (aligned).

    Fix (Jun 22, 2026): previous version returned negative scores when
    both headline and body were negative but at different magnitudes
    due to VADER assigning opposite signs to headline-length vs body-
    length text.  Now uses a sign-aware check with a neutral zone
    (|compound| < 0.05 treated as zero) to avoid sign-flip artifacts.

    Fix (Jun 23, 2026): VADER assigns positive scores to editorially
    negative headlines containing technical/neutral vocabulary
    (e.g., "Meta Deletes Face-Recognition System From Smart Glasses App
    After WIRED Report" → compound +0.40 due to "Smart").  When a
    headline contains loaded framing signals (face-recognition, surveillance,
    biometric, quietly, secretly, deleted, removed, stripped, scrubbed)
    near tech-company/product context, override VADER's positive score
    and treat the headline as editorially negative.
    """
    if not headline or not body:
        return 0.0

    headline_vader = analyze_vader(headline)
    body_vader = analyze_vader(body)

    h_compound = headline_vader["compound"]
    b_compound = body_vader["compound"]

    # --- Headline framing override ---
    # When VADER reads a headline as positive but it contains loaded
    # editorial signals (surveillance tech, deletions, removals, quiet
    # actions, after-report framing), the editorial direction is negative.
    # Override h_compound to a synthetic negative value.
    if h_compound > 0.05:
        headline_lower = headline.lower()
        _HEADLINE_NEGATIVE_SIGNALS = [
            "face-recognition", "face recognition", "facial recognition",
            "surveillance", "biometric", "faceprint", "tracking",
            "quietly", "secretly", "covertly", "surreptitiously",
            "deletes", "deleted", "removes", "removed", "strips",
            "stripped", "scrubbed", "purged", "pulled",
            "after report", "after investigation", "after wired",
            "after nyt", "after times", "after guardian",
            "under fire", "under siege", "under scrutiny",
            "backlash", "controversy", "scandal",
            "pauses", "paused", "halts", "halted", "suspends",
            # Government pressure / regulatory compliance language —
            # editorially negative headlines where "presses", "demands",
            # "concerns rise" are adversarial despite VADER scoring them
            # as neutral/positive.  Detected in NYT voluntary review
            # (Jun 23): "U.S. Presses Meta" scored +0.60 by VADER.
            "presses", "pressed", "pressing",
            "demands", "demanded",
            "concerns rise", "concerns mount", "concerns grow",
            "raises concerns", "raises questions",
            "warns", "warned", "warning",
            "threatens", "threatened",
            "holdout", "lone holdout",
            "only company", "the only",
        ]
        signal_count = sum(
            1 for sig in _HEADLINE_NEGATIVE_SIGNALS
            if sig in headline_lower
        )
        if signal_count >= 2:
            # Strong editorial signal: treat as negative
            h_compound = -0.3 * signal_count  # scale with signal density
            h_compound = max(-0.9, h_compound)

    # Treat very small magnitudes as neutral to prevent sign-flip artifacts
    h_sign = 0 if abs(h_compound) < 0.05 else (1 if h_compound > 0 else -1)
    b_sign = 0 if abs(b_compound) < 0.05 else (1 if b_compound > 0 else -1)

    # Both neutral
    if h_sign == 0 and b_sign == 0:
        return 0.0

    # One is neutral, the other has a direction — weak alignment
    if h_sign == 0 or b_sign == 0:
        return 0.3

    # Same direction — alignment score based on magnitude similarity
    if h_sign == b_sign:
        mag_min = min(abs(h_compound), abs(b_compound))
        mag_max = max(abs(h_compound), abs(b_compound))
        if mag_max == 0:
            return 0.0
        magnitude_ratio = mag_min / mag_max

        # Penalise if headline is much more extreme than body (clickbait)
        if abs(h_compound) > abs(b_compound) * 2:
            return round(magnitude_ratio * 0.5, 4)
        return round(magnitude_ratio, 4)

    # Opposite directions — misalignment (but cap at -0.8 to avoid
    # overly harsh scores from VADER noise)
    diff = abs(h_compound - b_compound)
    return round(-min(diff, 0.8), 4)


def _measure_comparative_framing(text: str) -> float:
    """Measure how the subject is compared to peers.

    Returns -1.0 (unfavorable comparisons) to 1.0 (favorable).
    """
    if not text:
        return 0.0

    text_lower = text.lower()
    neg_count = 0
    pos_count = 0

    for phrase in NEGATIVE_COMPARISON:
        escaped = re.escape(phrase)
        neg_count += len(re.findall(rf"\b{escaped}\b", text_lower))

    for phrase in POSITIVE_COMPARISON:
        escaped = re.escape(phrase)
        pos_count += len(re.findall(rf"\b{escaped}\b", text_lower))

    total = neg_count + pos_count
    if total == 0:
        return 0.0

    score = (pos_count - neg_count) / total
    return round(score, 4)


# --- Adversarial framing device types ---
# These device types signal the editorial is positioned *against* the subject.
# Used by _compute_framing_correction to detect VADER-unreliable articles.
_ADVERSARIAL_DEVICE_TYPES: set[str] = {
    "loaded_language",
    "timeline_implication",
    "guilt_by_association",
    "juxtaposition",
    "refusal_amplification",
    "emotional_appeal",
    "catastrophizing",
    "power_asymmetry",
    # Isolation and pressure framing are adversarial: "Meta is the ONLY
    # major company that has not..." and "pressing Meta to..." position
    # the subject as a non-cooperator under authority pressure.  Detected
    # in NYT voluntary-review article where toolkit scored +0.61 on an
    # editorially adversarial piece because these were excluded.
    "isolation_framing",
    "pressure_language",
    # Self-referential investigation positions the publication as
    # investigative authority, anchoring credibility to prior adversarial
    # reporting.  Detected in Wired glasses launch review (Jun 23) where
    # "WIRED discovered code" references the NameTag facial recognition
    # investigation, embedding surveillance framing into a product review.
    "self_referential_investigation",
    # Kicker framing ends the article on a discordant negative note,
    # overriding the reader's impression regardless of the article's
    # overall positive content.  Critical for product reviews that end
    # on workforce morale or privacy concerns.
    "kicker_framing",
    # Hypocrisy frame juxtaposes an entity's stated position, policy,
    # or public commitment against its actual behavior, creating ironic
    # self-contradiction.  Detected in Guardian Wynn-Williams (Jun 25):
    # "We do not require non-disparagement clauses" vs enforcing one;
    # and NYT voluntary review (Jun 23): "positioned itself as responsible"
    # yet being the only holdout.
    "hypocrisy_frame",
    # Military techno-optimism frames defense/surveillance technology in
    # aspirational language ("revolutionize," "transform the battlefield")
    # that VADER reads as strongly positive even when editorial stance is
    # critical or the subject matter is intrinsically adversarial (weapons,
    # warfare, mass surveillance).  Detected in MIT TR Anduril/Meta smart
    # glasses warfare article where VADER scored +0.64 vs manual -0.10.
    "military_techno_optimism",
}

# Anchor device types that create negative reader takeaway even when
# the subject has positive agency (e.g. product reviews where the
# company is actively launching things).  These devices change what
# the reader *remembers* — kickers anchor the final impression, and
# self-referential investigation links the product to prior adversarial
# reporting by the same publication.
_ANCHOR_DEVICE_TYPES: set[str] = {
    "kicker_framing",
    "self_referential_investigation",
    "juxtaposition",
}

# Minimum thresholds for framing correction activation
_FRAMING_MIN_ADVERSARIAL_DEVICES = 3  # at least 3 adversarial framing devices
_FRAMING_MAX_AGENCY = -0.3            # agency must be negative (passive/adversarial)


# --- Outsourced intensity detection ---
# Quote extraction patterns for splitting quoted vs editorial text.
_QUOTE_PATTERNS: list[re.Pattern] = [
    re.compile(r'\u201c([^\u201d]+)\u201d'),  # smart double quotes
    re.compile(r'"([^"]+)"'),                  # straight double quotes
    re.compile(r"\u2018([^\u2019]+)\u2019"),   # smart single quotes (long-form)
]


def measure_outsourced_intensity(text: str) -> dict:
    """Measure outsourced emotional intensity — the editorial technique of
    deploying emotional quotes from sources while keeping prose measured.

    Returns a dict with:
    - ``quoted_intensity``: emotional language density in quoted text (0–1)
    - ``editorial_intensity``: emotional language density in non-quoted text (0–1)
    - ``outsourced_ratio``: how much more emotional quoted text is vs editorial.
      0.0 = no outsourcing (equal or editorial is more emotional).
      1.0 = all emotional language is in quotes, none in editorial prose.
    - ``quoted_word_count``: total words in quoted segments.
    - ``editorial_word_count``: total words in editorial (non-quoted) segments.

    Journalists who maintain neutral prose while deploying quotes like
    "this is censorship", "soul-crushing", "despotic" achieve high
    outsourced_ratio scores — the emotional punch is real but the
    journalist's byline text reads as measured and professional.
    """
    if not text:
        return {
            "quoted_intensity": 0.0,
            "editorial_intensity": 0.0,
            "outsourced_ratio": 0.0,
            "quoted_word_count": 0,
            "editorial_word_count": 0,
        }

    # Extract all quoted segments
    quoted_segments: list[str] = []
    quote_spans: list[tuple[int, int]] = []

    for pattern in _QUOTE_PATTERNS:
        for m in pattern.finditer(text):
            content = m.group(1).strip()
            if len(content.split()) >= 3:  # Skip very short quotes (titles, etc.)
                quoted_segments.append(content)
                quote_spans.append((m.start(), m.end()))

    # Build editorial text by removing quoted spans
    if quote_spans:
        # Sort spans and merge overlapping
        quote_spans.sort()
        editorial_parts: list[str] = []
        prev_end = 0
        for start, end in quote_spans:
            if start > prev_end:
                editorial_parts.append(text[prev_end:start])
            prev_end = max(prev_end, end)
        if prev_end < len(text):
            editorial_parts.append(text[prev_end:])
        editorial_text = " ".join(editorial_parts)
    else:
        editorial_text = text

    quoted_text = " ".join(quoted_segments)

    # Measure emotional intensity in each segment
    quoted_intensity = _measure_emotional_intensity(quoted_text) if quoted_text else 0.0
    editorial_intensity = _measure_emotional_intensity(editorial_text) if editorial_text else 0.0

    quoted_word_count = len(quoted_text.split()) if quoted_text else 0
    editorial_word_count = len(editorial_text.split()) if editorial_text else 0

    # Compute outsourced ratio:
    # If quoted text is more emotional than editorial, the journalist is
    # "outsourcing" emotional impact to sources.
    if quoted_intensity <= editorial_intensity or quoted_intensity == 0:
        outsourced_ratio = 0.0
    else:
        # How much of the emotional differential is outsourced
        # 1.0 when editorial_intensity = 0 and quoted_intensity > 0
        outsourced_ratio = 1.0 - (editorial_intensity / quoted_intensity)
        outsourced_ratio = round(max(0.0, min(1.0, outsourced_ratio)), 4)

    return {
        "quoted_intensity": round(quoted_intensity, 4),
        "editorial_intensity": round(editorial_intensity, 4),
        "outsourced_ratio": outsourced_ratio,
        "quoted_word_count": quoted_word_count,
        "editorial_word_count": editorial_word_count,
    }


def _compute_framing_correction(
    raw_tone: float,
    agency: float,
    emotional_intensity: float,
    framing_summary: dict[str, int],
) -> tuple[float, bool]:
    """Compute a framing-aware tone correction.

    VADER and TextBlob assign positive polarity to factual, measured
    investigative prose even when the editorial stance is clearly
    adversarial (loaded_language, timeline_implication, passive agency).
    This function detects that situation and returns a corrected tone
    derived primarily from the framing signals rather than the lexical
    polarity scores.

    The correction fires ONLY when:
    1. The raw VADER+TextBlob composite is non-negative (VADER got it wrong)
    2. At least ``_FRAMING_MIN_ADVERSARIAL_DEVICES`` adversarial framing
       devices are detected
    3. Agency attribution is below ``_FRAMING_MAX_AGENCY`` (subject is
       framed passively / as target of scrutiny)

    When the raw composite is already negative, VADER got the direction
    right.  However, if the framing signal is strong (many adversarial
    devices + strongly negative agency), the raw score may understate the
    true negativity.  In that case, a lighter *amplification* blend
    nudges the score toward the framing estimate without fully overriding.

    Returns:
        (corrected_tone, was_corrected) — the tone and whether the
        correction was activated.
    """
    adversarial_count = sum(
        framing_summary.get(dt, 0) for dt in _ADVERSARIAL_DEVICE_TYPES
    )

    # --- Path A: Full correction (raw non-negative, VADER got it wrong) ---
    if (
        raw_tone >= 0
        and adversarial_count >= _FRAMING_MIN_ADVERSARIAL_DEVICES
        and agency < _FRAMING_MAX_AGENCY
    ):
        # Compute framing-derived tone estimate
        base = agency
        amplified = base * (0.6 + 0.4 * emotional_intensity)
        density_factor = min(adversarial_count / 8.0, 1.0)
        framing_tone = amplified * (0.7 + 0.3 * density_factor)
        framing_tone = max(-1.0, min(0.0, framing_tone))
        corrected = 0.10 * raw_tone + 0.90 * framing_tone
        corrected = max(-1.0, min(1.0, round(corrected, 4)))
        return corrected, True

    # --- Path B: Amplification (raw negative but understated) ---
    # When VADER gets direction right but framing signals indicate
    # the article is more adversarial than the lexical score reflects.
    # Uses a lighter blend (50/50) to nudge toward framing estimate
    # without fully overriding the lexical signal.
    _AMPLIFICATION_MIN_DEVICES = 6  # higher threshold than full correction
    if (
        raw_tone < 0
        and raw_tone > -0.5  # only amplify mildly-negative scores
        and adversarial_count >= _AMPLIFICATION_MIN_DEVICES
        and agency < _FRAMING_MAX_AGENCY
    ):
        base = agency
        amplified = base * (0.6 + 0.4 * emotional_intensity)
        density_factor = min(adversarial_count / 8.0, 1.0)
        framing_tone = amplified * (0.7 + 0.3 * density_factor)
        framing_tone = max(-1.0, min(0.0, framing_tone))
        # Lighter blend: 50% raw, 50% framing estimate
        corrected = 0.50 * raw_tone + 0.50 * framing_tone
        corrected = max(-1.0, min(1.0, round(corrected, 4)))
        return corrected, True

    # --- No correction needed ---
    # --- Path C: Embedded adversarial anchor ---
    # Product review articles where the subject has positive agency
    # (actively launching products, designing things) but specific
    # "anchor" devices shift the reader's final impression negative.
    # Kicker framing + self-referential investigation + juxtaposition
    # create a "Trojan horse" effect: the article looks positive on
    # the surface but anchors the reader's takeaway negatively.
    #
    # Example: Wired glasses launch review (Jun 23, 2026) — agency
    # +0.67, raw tone +0.67, but the kicker ("morale at an all-time
    # low"), self-referential investigation ("WIRED discovered code
    # suggesting facial recognition"), and juxtaposition ("consumer
    # smart glasses...surveillance tools for the US military") anchor
    # the reader's final impression at ~+0.15 (neutral-to-slight-positive).
    #
    # Lighter blend than Path A: 60% raw, 40% toward neutral, because
    # the article IS partly positive — the correction nudges toward
    # the manual assessment, not a full adversarial override.
    anchor_count = sum(
        framing_summary.get(dt, 0) for dt in _ANCHOR_DEVICE_TYPES
    )
    if (
        raw_tone > 0.3        # strongly positive raw score
        and anchor_count >= 2  # at least 2 anchor devices
        and adversarial_count >= 4  # overall framing is adversarial-heavy
        and agency >= 0        # positive agency (product review context)
    ):
        # Nudge toward neutral: blend raw score toward 0.15
        # (typical manual assessment for product reviews with embedded
        # adversarial anchors — not negative, just much less positive)
        anchor_target = 0.15
        corrected = 0.55 * raw_tone + 0.45 * anchor_target
        corrected = max(-0.2, min(raw_tone, round(corrected, 4)))
        return corrected, True

    # --- Path E: Military techno-optimism inflation ---
    # Articles about military/defense technology where aspirational language
    # ("revolutionize the battlefield", "transform warfare", "enhanced
    # capabilities") inflates VADER's reading.  The editorial stance is
    # often critical or skeptical, but VADER reads the aspirational claims
    # as genuine positive sentiment.  Unlike Path A, agency is not strongly
    # negative because the subjects ARE actively building things — the
    # inflation comes from the *content domain* (warfare, weapons), not
    # from passive framing.
    #
    # Discovered in MIT TR Anduril/Meta smart glasses warfare article
    # (May 18, 2026) where VADER scored +0.64 vs manual assessment of
    # -0.10.  Agency was -0.2 (below Path A's -0.3 threshold).
    #
    # Relaxed agency threshold: any negative agency suffices.  The key
    # signal is ≥3 military_techno_optimism devices, which specifically
    # indicate VADER-inflating aspirational military language.
    _MTO_MIN_DEVICES = 3
    mto_count = framing_summary.get("military_techno_optimism", 0)
    if (
        raw_tone >= 0.3
        and mto_count >= _MTO_MIN_DEVICES
        and agency < 0  # any negative agency (relaxed from -0.3)
    ):
        # Blend toward the agency-derived estimate, lighter than Path A
        # (70/30 vs 90/10) because these are not pure adversarial pieces.
        base = agency
        amplified = base * (0.5 + 0.5 * emotional_intensity)
        density_factor = min(mto_count / 6.0, 1.0)
        framing_tone = amplified * (0.6 + 0.4 * density_factor)
        framing_tone = max(-0.5, min(0.0, framing_tone))
        corrected = 0.30 * raw_tone + 0.70 * framing_tone
        corrected = max(-0.5, min(0.2, round(corrected, 4)))
        return corrected, True

    # --- Path D: Sardonic/mocking framing ---
    # Active agency + overwhelmingly negative loaded language = article
    # describes someone actively pursuing something but frames the pursuit
    # as foolish, futile, or contemptible.  VADER reads active positive
    # words literally ("looking to start," "booming," "interesting") while
    # missing the editorial contempt conveyed entirely through loaded
    # language ("ethically rancid," "failed metaverse," "search for a
    # win," "AI slop").
    #
    # Key distinguishing signal: loaded_language dominance.  In sardonic
    # pieces, loaded_language typically accounts for >70% of all adversarial
    # devices — the writer isn't using structural framing (juxtaposition,
    # kicker, isolation) but raw contemptuous word choice.
    #
    # Discovered in Kotaku Meta Arena article (Jun 28, 2026) where VADER
    # scored +0.68 on a manually-assessed -0.55 to -0.65 piece.
    _SARDONIC_MIN_LOADED = 7    # very high loaded language count
    _SARDONIC_MIN_ADVERSARIAL = 8  # overall adversarial count
    loaded_count = framing_summary.get("loaded_language", 0)
    if (
        raw_tone >= 0.3
        and agency >= 0.3          # positive agency (contrast to Path A)
        and loaded_count >= _SARDONIC_MIN_LOADED
        and adversarial_count >= _SARDONIC_MIN_ADVERSARIAL
    ):
        density_factor = min(adversarial_count / 10.0, 1.0)
        sardonic_tone = -(0.40 + 0.25 * density_factor)
        corrected = 0.10 * raw_tone + 0.90 * sardonic_tone
        corrected = max(-1.0, min(0.0, round(corrected, 4)))
        return corrected, True

    return raw_tone, False


def _measure_source_authority_v2(text: str) -> float:
    """Improved source authority that considers attribution verb stance.

    Version 1 (``_measure_source_authority``) only measured named-vs-
    anonymous ratio.  This version also penalises heavy use of loaded
    attribution verbs (``claimed``, ``insisted``, ``admitted``), which
    signal that sources are deployed to *undermine* rather than validate
    the subject — even when all sources are named.

    Returns:
        -1.0 (sources deployed to undermine) to +1.0 (sources validate).
    """
    from mediascope.analyze.sources import (
        extract_sources,
        NEUTRAL_VERBS,
        LOADED_VERBS,
    )

    sources = extract_sources(text)
    if not sources:
        return 0.0

    anon_count = sum(1 for s in sources if s.is_anonymous)
    named_count = len(sources) - anon_count

    # Named/anonymous component (existing logic)
    identity_score = (named_count - anon_count) / len(sources)

    # Attribution verb stance component
    neutral_count = 0
    loaded_count = 0
    for s in sources:
        v = s.attribution_verb.lower().strip() if s.attribution_verb else ""
        if v in NEUTRAL_VERBS:
            neutral_count += 1
        elif v in LOADED_VERBS:
            loaded_count += 1

    verb_total = neutral_count + loaded_count
    verb_score = 0.0
    if verb_total > 0:
        verb_score = (neutral_count - loaded_count) / verb_total

    # Blend: identity 60%, verb stance 40%
    blended = 0.6 * identity_score + 0.4 * verb_score
    return round(max(-1.0, min(1.0, blended)), 4)


def analyze_composite(text: str, headline: str = "") -> SentimentResult:
    """Run composite multi-dimensional sentiment analysis.

    Combines VADER, TextBlob, and custom dimension analyzers to produce
    an 8-dimension SentimentResult.  When adversarial framing is detected
    and VADER produces a misleading positive score, a framing-aware
    correction overrides the raw composite (see
    ``_compute_framing_correction``).

    Args:
        text: Full article text.
        headline: Article headline (optional, used for alignment check).

    Returns:
        SentimentResult with all 8 dimensions calculated.
    """
    if not text:
        return SentimentResult()

    # Import framing detection lazily to avoid circular imports
    from mediascope.analyze.framing import detect_framing_devices, summarize_framing

    # 1. Overall tone: blend VADER compound and TextBlob polarity
    vader = analyze_vader(text)
    tb = analyze_textblob(text)
    raw_tone = round(0.6 * vader["compound"] + 0.4 * tb["polarity"], 4)
    raw_tone = max(-1.0, min(1.0, raw_tone))

    # 2. Emotional language intensity
    emotional_intensity = _measure_emotional_intensity(text)

    # 3. Source authority framing (v2: includes attribution verb stance)
    source_authority = _measure_source_authority_v2(text)

    # 4. Agency attribution
    agency = _measure_agency(text)

    # 5. Headline-body alignment (use framing-aware check)
    alignment = _measure_headline_alignment(headline, text)

    # 6. Anonymous source ratio
    anon_count, total_sources = count_anonymous_sources(text)
    anon_ratio = round(anon_count / total_sources, 4) if total_sources > 0 else 0.0

    # 7. Speculative language ratio
    spec_ratio = measure_speculative_language(text)

    # 8. Comparative framing
    comparative = _measure_comparative_framing(text)

    # --- Framing-aware tone correction ---
    # When VADER reads factual investigative prose as positive but framing
    # signals are clearly adversarial, override with framing-derived tone.
    devices = detect_framing_devices(text)
    framing_summary = summarize_framing(devices)

    overall_tone, framing_corrected = _compute_framing_correction(
        raw_tone=raw_tone,
        agency=agency,
        emotional_intensity=emotional_intensity,
        framing_summary=framing_summary,
    )

    # When framing correction fired, the body's true direction is negative
    # even though VADER scored it positive.  Recalculate alignment against
    # the corrected direction so that a negative headline + corrected-negative
    # body reads as aligned rather than contradictory.
    if framing_corrected and headline:
        headline_vader = analyze_vader(headline)
        h_compound = headline_vader["compound"]
        # If headline is also negative (or neutral), alignment is positive
        if h_compound <= 0.05:
            # Both headline and (corrected) body are negative — good alignment
            # Scale by how negative the headline is (stronger = more aligned)
            alignment = round(min(abs(h_compound) * 2.0, 0.9), 4) if h_compound < -0.05 else 0.3

    return SentimentResult(
        overall_tone=overall_tone,
        emotional_language_intensity=emotional_intensity,
        source_authority_framing=source_authority,
        agency_attribution=agency,
        headline_body_alignment=alignment,
        anonymous_source_ratio=anon_ratio,
        speculative_language_ratio=spec_ratio,
        comparative_framing=comparative,
        framing_corrected=framing_corrected,
        raw_tone=raw_tone,
    )
