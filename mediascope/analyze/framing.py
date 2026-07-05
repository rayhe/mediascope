"""Framing device detection for media coverage analysis.

Detects rhetorical and editorial framing devices in article text
using pattern-based matching.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class FramingDevice:
    """A detected framing device in article text."""

    device_type: str      # Type of framing device
    evidence_text: str    # The matched text that triggered detection
    start: int            # Character offset start
    end: int              # Character offset end


# --- Detection patterns per device type ---
# Each entry is (compiled_regex, device_type_label)
# Patterns are designed to catch common editorial framing techniques.

_GUILT_BY_ASSOCIATION_PATTERNS: list[re.Pattern] = [
    re.compile(
        r"\b(?:ties to|linked to|connections? to|associated with|"
        r"close to|allied with|backed by|funded by|"
        r"relationship with|in bed with|cozy with)\b"
        r".{0,80}?"
        r"\b(?:controversial|scandal|accused|alleged|"
        r"questionable|problematic|extremist|radical)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    re.compile(
        r"\b(?:controversial|scandal|accused|alleged)\b"
        r".{0,80}?"
        r"\b(?:ties to|linked to|connections? to|associated with|close to)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Direct association phrasing
    re.compile(
        r"\b(?:has|have|had) (?:close |deep )?(?:ties|links|connections?) (?:to|with)\b",
        re.IGNORECASE,
    ),
    # Military/intelligence credential stacking — listing multiple defense/intel
    # affiliations to create an ominous impression
    re.compile(
        r"\b(?:former (?:CIA|FBI|NSA|Pentagon|military|intelligence|defense|DIA|NRO))\b"
        r".{0,120}?"
        r"\b(?:former (?:CIA|FBI|NSA|Pentagon|military|intelligence|defense|DIA|NRO))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "Pentagon supplier" / "government contractor" as loaded association
    re.compile(
        r"\b(?:Pentagon|military|defense|intelligence|government)\s+"
        r"(?:supplier|contractor|vendor|partner)\b",
        re.IGNORECASE,
    ),
]

_ANONYMOUS_AUTHORITY_PATTERNS: list[re.Pattern] = [
    re.compile(r"\baccording to (?:people|sources|individuals|persons)\b", re.IGNORECASE),
    re.compile(r"\bpeople familiar with (?:the )?(?:matter|situation|plans|discussions?)\b", re.IGNORECASE),
    re.compile(r"\bspoke (?:with \w+ )?on (?:the )?condition (?:of )?anonymity\b", re.IGNORECASE),
    re.compile(r"\basked not to be (?:identified|named)\b", re.IGNORECASE),
    re.compile(r"\bpeople who (?:requested|declined|asked for) anonymity\b", re.IGNORECASE),
    re.compile(r"\bsources (?:close to|inside|within|briefed on)\b", re.IGNORECASE),
    re.compile(r"\ba person with (?:direct )?knowledge\b", re.IGNORECASE),
    re.compile(r"\bpeople (?:briefed on|with knowledge of)\b", re.IGNORECASE),
    re.compile(r"\binsiders? (?:said|told|indicated|suggested)\b", re.IGNORECASE),
    # Numbered officials/people as anonymous sources — common in NYT-style
    # government/policy reporting: "two government officials said"
    re.compile(
        r"\b(?:two|three|four|five|six|seven|several|multiple)\s+"
        r"(?:government|administration|intelligence|defense|senior|federal|"
        r"White House|Commerce|State Department)\s+"
        r"(?:officials?|aides?|advisers?|staffers?)\s+"
        r"(?:said|told|confirmed|added|indicated)\b",
        re.IGNORECASE,
    ),
    # "one/a person involved in / close to" — person described by proximity
    re.compile(
        r"\b(?:one|a) person (?:involved in|close to|inside|with the|within the|"
        r"privy to|briefed on|engaged in)\b",
        re.IGNORECASE,
    ),
    # "one/a senior [party/adjective]? [title]" — unnamed political/industry
    # figures described by seniority + role: "one senior Republican congressman"
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

_CATASTROPHIZING_PATTERNS: list[re.Pattern] = [
    re.compile(
        r"\b(?:catastrophic|catastrophe|devastating|disastrous|"
        r"existential threat|unprecedented crisis|"
        r"existential risk|spiraling|death spiral|"
        r"collapse|collapsing|meltdown|implosion|"
        r"free fall|freefall|nosedive|"
        r"tsunami|avalanche|firestorm|hemorrhaging)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:could destroy|will destroy|threatens to destroy|"
        r"threatens to upend|could wipe out|"
        r"demise of|downfall of)\b",
        re.IGNORECASE,
    ),
    # "death of" only when followed by an abstract concept (lowercase word
    # or "the"), NOT when followed by a proper noun (capitalized name).
    # "death of the internet" = catastrophizing; "death of Jamey Rodemeyer"
    # = factual reference to a person who literally died.
    # Uses (?-i:) to disable IGNORECASE for the lookahead character class,
    # so [a-z] only matches actual lowercase letters.
    re.compile(
        r"\bdeath of(?=\s+(?:the\s+)?(?-i:[a-z]))",
        re.IGNORECASE,
    ),
    # "end of" only when followed by abstract/institutional objects, not events
    re.compile(
        r"\bend of\s+(?:the\s+)?(?:democracy|freedom|privacy|"
        r"journalism|an? era|civilization|the world|humanity|"
        r"civil liberties|free speech|the internet)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:nightmare|nightmarish|horror|terrifying|apocalyptic|"
        r"armageddon|cataclysmic|seismic shift|tectonic shift)\b",
        re.IGNORECASE,
    ),
    # "cultural dead end" / "dead end" as terminal-trajectory framing
    re.compile(
        r"\b(?:cultural dead end|dead end|cultural collapse|"
        r"model collapse|ecological harm|ecological collapse)\b",
        re.IGNORECASE,
    ),
    # "threat to humanity/civilization/democracy" — existential-risk framing
    # without the word "existential".  Common in poll/survey reporting where
    # a percentage of respondents are cited as believing AI/tech poses such
    # a threat.  Discovered via MIT TR "Resistance" article (Apr 2026):
    # "three-quarters of Americans worry AI could pose a threat to humanity."
    re.compile(
        r"\b(?:threat to humanity|threat to civilization|"
        r"threat to (?:our |the )?(?:existence|survival|future|way of life)|"
        r"(?:pose|poses|posed|posing) (?:a |an? )?(?:grave |serious |real |fundamental )?"
        r"threat to (?:humanity|civilization|society|democracy))\b",
        re.IGNORECASE,
    ),
]

_FALSE_BALANCE_PATTERNS: list[re.Pattern] = [
    re.compile(
        r"\b(?:some (?:experts|critics|analysts|observers) (?:say|argue|believe|contend|claim))"
        r".{0,120}?"
        r"\b(?:others? (?:say|argue|believe|contend|claim|disagree|counter|point out))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    re.compile(
        r"\b(?:on (?:the )?one hand).{0,200}?\b(?:on the other hand)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    re.compile(
        r"\b(?:while (?:some|many|most) (?:experts?|scientists?|researchers?))"
        r".{0,120}?"
        r"\b(?:others?|a (?:few|minority|small number))\b",
        re.IGNORECASE | re.DOTALL,
    ),
]

_SELECTIVE_OMISSION_PATTERNS: list[re.Pattern] = [
    # Signals that something is being left unsaid or context is missing
    re.compile(
        r"\b(?:notably absent|conspicuously absent|"
        r"failed to mention|did not mention|"
        r"no mention of|without mentioning|"
        r"omitted|left out|glossed over|"
        r"conveniently (?:ignor|omit|overlook|forget))\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:what (?:the|this) (?:article|report|story|piece) "
        r"(?:doesn't|does not|fails to) (?:mention|note|address|acknowledge))\b",
        re.IGNORECASE,
    ),
]

_EMOTIONAL_APPEAL_PATTERNS: list[re.Pattern] = [
    re.compile(
        r"\b(?:shocking|outrageous|alarming|horrifying|"
        r"heartbreaking|sickening|infuriating|appalling|"
        r"disgusting|shameful|disgraceful|deplorable|"
        r"unconscionable|unforgivable|inexcusable)\b",
        re.IGNORECASE,
    ),
    # Alarm / anxiety idioms — editorial language that conveys urgency
    # and collective fear without explicitly catastrophizing.  These are
    # idiomatic phrases ("sounding the alarm", "deep anxieties") that
    # work as emotional appeals through their connotation of crisis.
    # Discovered via MIT TR "Resistance" article (Apr 2026):
    #   "sounding the alarm"
    #   "the backlash reflects deep anxieties"
    #   "fierce blowback from artists"
    re.compile(
        r"\b(?:sounding the alarm|raise(?:d|s|ing)? the alarm|"
        r"ring(?:s|ing|ed)? (?:the )?alarm bells?|"
        r"deep(?:ly)? (?:anxious|anxieties|concerned|disturbing|troubling)|"
        r"deep anxieties|growing (?:anxiety|anxieties|unease|alarm|panic)|"
        r"fierce (?:blowback|opposition|resistance|backlash|criticism)|"
        r"widespread (?:anxiety|fear|panic|outrage|alarm|concern|anger)|"
        r"palpable (?:fear|anxiety|tension|anger|unease)|"
        r"rising (?:anxiety|fear|panic|alarm|anger|frustration)|"
        r"sparked? (?:outrage|fury|anger|backlash|uproar))\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:victims?|children|families|innocent|vulnerable|"
        r"helpless|defenseless|powerless)\b"
        r".{0,60}?"
        r"\b(?:suffer|suffering|harmed|exploited|endangered|"
        r"at risk|threatened|betrayed)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Emphatic rhetorical questions
    re.compile(
        r"\b(?:how (?:can|could|dare)|why (?:won't|wouldn't|hasn't|should))\b.{5,80}\?",
        re.IGNORECASE,
    ),
    # Sympathy-eliciting personal impact — individual suffering from institutional action
    re.compile(
        r"\b(?:moved to tears|brought to tears|broke down|"
        r"standing ovation|applause|"
        r"solidarity (?:for|with)|act of solidarity|"
        r"forced into silence|sat in silence|"
        r"unable (?:even )?to (?:speak|nod|respond)|"
        r"threatened (?:her|him|them|with) (?:bankruptcy|ruin))\b",
        re.IGNORECASE,
    ),
    # Medical/health duress — editorial deployment of health emergencies,
    # life-threatening conditions, or medical vulnerability as leverage
    # context to amplify power asymmetry.  Common in whistleblower coverage
    # where employers are framed as exploiting employees' medical situations
    # (e.g., "life-threatening health condition during childbirth" in the
    # Guardian's Wynn-Williams coverage, implying Meta used healthcare
    # dependency as severance leverage).
    re.compile(
        r"\b(?:life.?threatening\s+(?:health\s+)?(?:condition|illness|complication|emergency|diagnosis)|"
        r"medical\s+(?:emergency|crisis|condition|complication)|"
        r"(?:hospitalized|hospitalised)\s+(?:during|after|following|for)|"
        r"during\s+childbirth|complications?\s+(?:during|from)\s+(?:child)?birth|"
        r"(?:denied|withheld|conditional)\s+(?:health\s*care|medical|insurance|coverage)|"
        r"health\s*care\s+(?:coverage\s+)?(?:as\s+)?(?:leverage|contingent|conditional|hostage)|"
        r"(?:coverage|insurance|health\s*care)\s+(?:made\s+)?contingent\s+on|"
        r"dependent\s+on\s+(?:employer|company|corporate)\s+(?:health|medical|insurance))\b",
        re.IGNORECASE,
    ),
    # Workplace collective despair — mass dissatisfaction + helplessness
    # language deployed to evoke sympathy for employees against institution.
    # Common in tech workplace reporting (e.g., Wired "Dark Mood Inside Meta").
    re.compile(
        r"\b(?:everyone is (?:unhappy|miserable|afraid|terrified)|"
        r"nobody is happy|no one is happy|"
        r"morale.{0,40}(?:rock.?bottom|historically low|all.time low|an? all.time low)|"
        r"no(?:body has a)? choice|we have no choice|"
        r"social contract (?:is |has been )?(?:broken|shattered|dead)|"
        r"can.t (?:even )?feign (?:empathy|concern|care)|"
        r"used to train.{0,20}(?:replace|replacement)|"
        r"train (?:your|their|our) own replacement|"
        r"vibes are (?:horrifically|historically|extremely) (?:low|bad|poor))\b",
        re.IGNORECASE,
    ),
    # Vulnerability/accessibility framing — editorial deployment of disability,
    # age, isolation, or mental health conditions to elicit sympathy for
    # affected users/communities. Common in platform-shutdown and community-
    # displacement coverage where vulnerable users are positioned as
    # dependents losing essential services.
    re.compile(
        r"\b(?:disabled|disability|limited mobility|wheelchair|"
        r"social anxiety|depression|mental health|"
        r"(?:\d{2,3}) years? old|elderly|"
        r"isolated|lives? (?:alone|in (?:rural|remote))|"
        r"from (?:your|their|her|his) bed|"
        r"nowhere else (?:to go)?|no(?:where| )?(?:other|else)|"
        r"no barrier|"
        r"energy to go in|only (?:energy|strength) (?:to|for))\b",
        re.IGNORECASE,
    ),
    # Platform death / community displacement — editorial language framing
    # corporate platform shutdowns, pivots, or sunsets as destruction of
    # human communities. Distinct from workplace revolt (employees) — this
    # targets USER communities being abandoned by platform operators.
    re.compile(
        r"\b(?:on life support|"
        r"(?:this|it) is my home|this is (?:our|their) home|"
        r"just disappearing|"
        r"(?:killing|shutting|winding|closing) (?:it|this|them) (?:down|for good)|"
        r"all (?:be )?going away|might all be going away|"
        r"(?:so )?devastated|"
        r"broke(?:n)? down in tears|"
        r"terrified of the uncertainty|"
        r"don't (?:know|think).{0,30}what (?:my|our|their) life)\b",
        re.IGNORECASE,
    ),
    # Desolation scene-setting — descriptive environmental emptiness deployed
    # as indirect editorial argument for failure or abandonment. The writer
    # describes empty spaces rather than making explicit claims.
    re.compile(
        r"\b(?:eerily (?:silent|quiet|empty|still|deserted)|"
        r"empty aside from|"
        r"(?:was|is|stood|sat) (?:completely |largely |mostly )?(?:empty|deserted|abandoned)|"
        r"ghost town|ghostly|"
        r"not a (?:soul|person|one) (?:in sight|around|there)|"
        r"(?:tumbleweeds?|crickets?))\b",
        re.IGNORECASE,
    ),
]

_STRAW_MAN_PATTERNS: list[re.Pattern] = [
    re.compile(
        r"\b(?:critics (?:claim|say|argue|allege|contend) that)\b"
        r".{0,150}?"
        r"\b(?:but|however|in (?:reality|fact|truth)|actually)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    re.compile(
        r"\b(?:the argument (?:that|is)|some (?:claim|say|would have you believe))\b"
        r".{0,150}?"
        r"\b(?:but|however|in (?:reality|fact|truth)|of course|obviously)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    re.compile(
        r"\b(?:essentially (?:saying|arguing|claiming)|"
        r"what (?:they're|they are) really (?:saying|doing)|"
        r"amounts to (?:saying|claiming))\b",
        re.IGNORECASE,
    ),
]

_LOADED_LANGUAGE_PATTERNS: list[re.Pattern] = [
    # Loaded verbs and descriptors applied to subjects
    re.compile(
        r"\b(?:slammed|blasted|hammered|torched|eviscerated|"
        r"lambasted|excoriated|ripped|grilled|destroyed|"
        r"crushed|obliterated|demolished|annihilated|"
        r"staggering|mastermind(?:ed)?|explosive|"
        r"turned a blind eye|strike fear|struck fear|"
        r"indefensible|abusive|defamatory|"
        r"drastic(?:ally)?|superficial(?:ly)?|"
        r"reckless(?:ly)?|egregious(?:ly)?|flagrant(?:ly)?|"
        # Intensity idioms: "in droves" / "in spades" / "en masse" —
        # amplifying modifiers that editorialize by exaggerating magnitude.
        # Discovered via MIT TR "Resistance" article (Apr 2026):
        # "users uninstalled ChatGPT in droves"
        r"in droves|in spades|en masse|in drastic numbers"
        r")\b",
        re.IGNORECASE,
    ),
    # Loaded adjectives/nouns characterizing people or organizations
    re.compile(
        r"\b(?:embattled|beleaguered|troubled|scandal-plagued|"
        r"controversial|notorious|disgraced|under fire|"
        r"under siege|besieged|defiant|brazen|arrogant|"
        r"tone-deaf|out of touch|nefarious|scandalous|"
        r"comically|laughably|absurdly|laughable|"
        r"dishonest|dishonesty|fundamentally\s+(?:dishonest|unethical|flawed|problematic)|"
        r"deceptive|misleading|disingenuous|"
        r"exploitative|dubious|rancid|sordid|"
        # Polemical / invective nouns — nouns that characterize speech or
        # documents as extreme, aggressive, or unhinged.  "diatribe",
        # "screed", "tirade" etc. editorialize the quoted content before
        # the reader encounters it.
        # Discovered via MIT TR "Resistance" article (Apr 2026):
        # "found carrying an anti-AI diatribe"
        r"diatribe|screed|tirade|rant|harangue|polemic|manifesto|"
        r"unprecedented\s+(?:\w+\s+)?(?:breach|breaches|violation|exposure|threat|risk|danger|harm|crisis|failure))\b",
        re.IGNORECASE,
    ),
    # Scare quotes / hedging language that undermines
    re.compile(
        r"(?:so-called|self-proclaimed|self-styled|self-described)\s+\w+",
        re.IGNORECASE,
    ),
    # Surveillance/security-state language applied to commercial entities
    # or workplace/employee contexts
    re.compile(
        r"\b(?:surveillance|wiretap|spying|spy|mass.?identification|"
        r"biometric|facial recognition|face.?recognition|faceprint|"
        r"keystroke.?(?:tracking|monitoring|logging)|screen.?recording|"
        r"tracking|monitor(?:ing)?|eavesdrop(?:ping)?)\b"
        r".{0,60}?"
        r"\b(?:consumer|commercial|app|phone|device|glasses|product|"
        r"employee|worker|staff|intern(?:al)?|workplace|computer)s?\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Ubiquitous-camera / stealth-recording language — editorial framing
    # that emphasizes surveillance potential of consumer camera devices
    # through ubiquity ("cameras everywhere"), body-worn framing ("camera
    # on their face"), or involuntary-recording constructions ("recorded
    # space").  Distinct from the proximity pattern above: these are
    # self-contained phrases that carry surveillance valence without
    # needing a nearby device term.
    # Discovered via Memeburn Meta glasses article (Jun 2026).
    re.compile(
        r"\b(?:camera(?:s)?\s+(?:everywhere|always|running|"
        r"on (?:your|their|every|each|someone'?s?) face)|"
        r"recorded\s+space|"
        r"no (?:visible|obvious|readable|clear) (?:cue|signal|indicator|sign))\b",
        re.IGNORECASE,
    ),
    # Data-negligence language — technical terms that imply security
    # negligence when applied to data handling (encryption absence,
    # plaintext storage).  These carry strong editorial valence: naming
    # the absence of standard security practice frames the subject as
    # falling below baseline competence.
    re.compile(
        r"\b(?:unencrypted|plaintext|plain.?text|"
        r"without\s+encryption|not\s+encrypted|"
        r"stored?\s+in\s+plain)\b"
        r".{0,40}?"
        r"\b(?:data|information|records?|form|storage|database|"
        r"files?|logs?|credentials?|passwords?|tokens?)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "Quietly" as editorial signal of secrecy
    re.compile(
        r"\b(?:quietly|secretly|covertly|surreptitiously|discreetly|"
        r"secretive(?:ly)?|clandestine(?:ly)?|"
        r"without (?:notice|disclosure|announcing|telling)|"
        r"behind (?:closed doors|the scenes))\b",
        re.IGNORECASE,
    ),
    # Deception / impersonation / espionage language — terms that frame
    # standard business practices (competitive benchmarking, user testing,
    # mystery shopping, red-teaming) as covert operations, impersonation
    # schemes, or intelligence gathering.  Distinct from the secrecy
    # pattern above: these characterise the *method* as deceptive rather
    # than the announcement as secretive.
    # Discovered via Wired Meta "Cannes" contractors article (Jul 2026):
    # "instructed to pose as minors", "probe", "dummy under-18 accounts"
    re.compile(
        r"\b(?:pose[sd]?\s+as|posing\s+as|impersonat(?:e[sd]?|ing)|"
        r"masquerad(?:e[sd]?|ing)|pretend(?:ed|ing)\s+to\s+be|"
        r"(?:fake|dummy|bogus|sham|decoy)\s+(?:account|profile|identity|persona)s?|"
        r"infiltrat(?:e[sd]?|ing|ion)|"
        r"bombard(?:ed|ing|s)?)\b",
        re.IGNORECASE,
    ),
    # Contractor exploitation / trauma language — loaded terms that frame
    # employer-contractor relationships as harmful or traumatizing.
    # Distinct from workplace-specific loaded language (which covers
    # internal employees) because these emphasise the outsourcing of harm.
    # Discovered via Futurism Cannes reframe (Jul 2026): "offloaded
    # disturbing work onto contractors", "traumatized", "gobsmacked."
    re.compile(
        r"\b(?:offload(?:ed|ing|s)?|traumati[sz](?:ed|ing)|"
        r"gobsmacked|shell.?shocked|"
        r"brute.?force\s+approach|"
        r"forced\s+to\s+(?:come up with|create|write|produce|generate)|"
        r"ostensibly\s+in\s+the\s+name\s+of)\b",
        re.IGNORECASE,
    ),
    # "Dormant" / hidden capability language — require proximity to feature/code
    # context to avoid flagging literal uses like "dormant account" or
    # "hidden in websites" (describing where prompt injection commands live)
    re.compile(
        r"\b(?:dormant|hidden|buried|unreleased|undisclosed|unannounced|under.?the.?radar)"
        r"(?=\s+(?:feature|capability|code|function|tool|mode|setting|option|"
        r"flag|parameter|toggle|endpoint|API|module|interface|app|"
        r"product|project|initiative|plan|prototype|design|system)s?\b)",
        re.IGNORECASE,
    ),
    # Workplace-specific loaded language — terms that characterize
    # organizational decisions as oppressive or dehumanizing
    re.compile(
        r"\b(?:soul.?crushing|drudge|drudgery|gulag|"
        r"assembly line|human assembly line|data factory|"
        r"draftees?|drafted|conscript(?:ed|ing|ion|s)?|disposable|"
        r"menial|dehumanizing|atrocious|brutal|"
        r"exploitation|slave|slavery|sweatshop|"
        r"belittled?|berated?|belittling|berating|"
        r"cruel|cruelty|grim|grimly|"
        r"rock.?bottom|historically low|"
        r"shattered|privacy zealots?|"
        r"insane amounts?|"
        r"horrifically|horrific)"
        r"\b",
        re.IGNORECASE,
    ),
    # Privacy-violation and social-predation language — terms that frame
    # commercial products or their users as threats to personal safety
    re.compile(
        r"\b(?:pervert|perverted|perverts|"
        r"predatory|predator|predators|"
        r"preying|preys?\s+on|prey\s+on|"
        r"prowling|prowl|prowls|"
        r"creep|creepy|creeps|"
        r"stalking|stalker|stalkers|stalk|"
        r"harassment|harassing|harasser|"
        r"intimidation|intimidating|"
        r"violation|violating|"
        r"unsettling|disturbing|"
        r"invasive|"
        r"doomed|dystopian|"
        r"pestering|"
        r"juvenile)"
        r"\b",
        re.IGNORECASE,
    ),
    # Legal silencing / corporate censorship language — terms that frame
    # legal action as suppression of free expression
    re.compile(
        r"\b(?:censorship|silenced?|silencing|gagged|gag.?order|"
        r"muzzled|hostage(?:\s+situation)?|"
        r"despotic|tyrann(?:y|ical)|"
        r"trolling(?:\-like)?|"
        r"suppress(?:ion|ing|ed)?|"
        r"retaliatory|retaliation|chilling\s+effect)\b",
        re.IGNORECASE,
    ),
    # Corporate power framing — language positioning corporations as
    # state-like or authoritarian actors
    re.compile(
        r"\b(?:sovereign\s+affect|assert\s+their\s+power|"
        r"nation\s+states?|"
        r"kings?,?\s+emperors?|"
        r"bankrupt(?:cy|ed|ing)?|"
        r"formally\s+sanctioned|sanctions?\s+motion)\b",
        re.IGNORECASE,
    ),
    # Workplace coercion / compulsion language — editorial device framing
    # management decisions as authoritarian mandates, emphasising the
    # absence of employee consent or agency
    re.compile(
        r"\b(?:no\s+(?:option|way|ability|choice)\s+to\s+opt[\-\s]?out|"
        r"opt[\-\s]?out\s+is\s+not\s+(?:possible|an option|available)|"
        r"cannot\s+opt[\-\s]?out|"
        r"no\s+(?:opt[\-\s]?out|escape|recourse|alternative)|"
        r"not\s+(?:possible|optional|voluntary)|"
        r"mandatory|compulsory|forced\s+to\s+(?:install|use|adopt|accept|watch|view|review|read|listen|participate))\b",
        re.IGNORECASE,
    ),
    # Employee revolt / organised dissent language — loaded terms
    # characterising employee responses as rebellion or crisis
    re.compile(
        r"\b(?:revolt(?:ed|ing|s)?|"
        r"rebellion|rebel(?:led|ling)?|"
        r"uproar|backlash|"
        r"protest(?:ed|ing|s)?|petition(?:ed|ing|s)?|"
        r"flyers?|leaflets?|"
        r"countdown\s+to\s+(?:layoff|the\s+layoff)|"
        r"counting\s+down\s+to|"
        r"nihilistic|dystopian|Orwellian|Kafkaesque|"
        r"tantamount\s+to|"
        r"train(?:ing)?\s+(?:their|your|our|its)\s+(?:own\s+)?replacements?|"
        r"(?:help(?:ing)?|design(?:ing)?)\s+(?:their|your|our|its)\s+(?:own\s+)?(?:bot\s+)?replacements?|"
        r"training\s+(?:the\s+)?AI\s+(?:that\s+)?(?:will\s+)?replace)\b",
        re.IGNORECASE,
    ),
    # Idiomatic dismissal / incompetence framing — editorial language
    # implying negligence, failure, or embarrassment through idioms
    re.compile(
        r"\b(?:practically\s+mindless|mindless(?:ly)?|"
        r"slipped?\s+through\s+the\s+cracks?|"
        r"embarrass(?:ing|ed|ment)|humiliat(?:ing|ed|ion)|"
        r"should\s+have\s+been\s+(?:caught|found|discovered|obvious)|"
        r"dropped?\s+the\s+ball|"
        r"asleep\s+at\s+the\s+wheel|"
        r"basic(?:ally)?\s+(?:failure|negligence|oversight|incompetence)|"
        r"stunning(?:ly)?\s+(?:simple|basic|obvious)|"
        r"shockingly\s+(?:simple|basic|easy)|"
        r"beggars?\s+belief|"
        r"unconscionable)\b",
        re.IGNORECASE,
    ),
    # Analogy/diminishment — comparing sophisticated entities to children,
    # students, or naive actors to undermine their competence.
    # NOTE: changed child(?:ish|like)? → child(?:ish|like) to require suffix.
    # Bare "child" is a neutral policy term in regulatory/safety reporting
    # (e.g., "online child safety", "child protection") and was generating
    # false positives on every child-safety policy article.
    re.compile(
        r"\b(?:elementary\s+school|kindergarten|toddler|child(?:ish|like)|"
        r"naive|naively|"
        r"eager\s+to\s+(?:please|finish|comply|complete)|"
        r"just\s+wants?\s+to\s+please|"
        r"puppy\s+(?:eager|like)|"
        r"blindly\s+(?:follow|obey|comply)|"
        r"rubber.?stamp(?:ing|ed)?)\b",
        re.IGNORECASE,
    ),
    # Dismissive / trivializing language — terms that reduce serious claims,
    # products, or positions to performance, pretence, or marketing noise
    re.compile(
        r"\b(?:hype(?:d(?:\s+up)?)?|"
        r"make.?believe|game\s+of\s+make.?believe|"
        r"play\s+along|playing\s+pretend|"
        r"fantas(?:y|ies|ize)|indulge|indulging|"
        r"abdicate(?:d|s|ing)?\s+(?:their|its|his|her|our|your|the)?\s*responsibilit|"
        r"abdicat(?:ed?|ing|ion)|"
        r"charade|theatre|theater|"
        r"parlor\s+trick|party\s+trick|"
        r"hand.?wav(?:ing|y)|smoke\s+and\s+mirrors|"
        r"window\s+dressing|lip\s+service|"
        r"AI\s+slop|"
        r"fig\s+leaf)\b",
        re.IGNORECASE,
    ),
    # Data contamination / competitive espionage metaphors — biological or
    # military language applied to normal data flows between AI services.
    # "seep into training data", "contaminate the pipeline", "leaking
    # proprietary logic" frame routine API interactions as warfare or
    # pollution.  Discovered in multi-source Meta Claude Code/Codex
    # restriction coverage (Jun 2026).
    re.compile(
        r"\b(?:contaminate[ds]?|contaminating|contamination|"
        r"seep(?:s|ed|ing)?\s+into|"
        r"leak(?:s|ed|ing)?\s+into|"
        r"infiltrat(?:e[ds]?|ing|ion)|"
        r"exfiltrat(?:e[ds]?|ing|ion)|"
        r"competitive\s+intelligence\s+leakage|"
        r"data\s+(?:poisoning|theft|siphoning|harvesting))\b",
        re.IGNORECASE,
    ),
    # Ad hominem / character diminishment — personal characterizations
    # that undermine a subject's credibility or seriousness through
    # caricature rather than argument.  Distinct from analogy/diminishment
    # (which compares entities to children/naive actors) — this targets
    # personal attributes, physical descriptions, or social stereotypes.
    #
    # Identified as a gap in AV Club Meta Arena analysis (Jun 27, 2026):
    #   - "gormless tech bros" — stereotype characterization
    #   - "lumbering behemoth" — animalistic size-based dismissal
    #   - "dopamine-seekers" — neuroscience-loaded user characterization
    #   - "frequently sidelined wallflower" — diminishment through social metaphor
    re.compile(
        r"\b(?:tech\s+bro(?:s|ther)?|bro\s+culture|"
        r"gormless|bumbling|clueless|hapless|inept|"
        r"wallflower|boy.?king|man.?child|"
        r"lumbering|bloated|"
        r"dopamine.?seeker|attention.?seeker|"
        r"acolytes?|sycophants?|lackeys?|"
        r"megalomania(?:c|cal)?|narcissis(?:t|tic)|"
        r"sociopath(?:ic)?)\b",
        re.IGNORECASE,
    ),
    # Industry-as-vice framing — characterizing legitimate businesses
    # or product categories as inherently predatory, addictive, or
    # criminal through loaded categorical nouns
    re.compile(
        r"\b(?:(?:gambling|betting)\s+addict(?:s|ion)?|"
        r"their\s+scams?|these?\s+scams?|"
        r"(?:unquenchable|insatiable|omnidirectional)\s+(?:\w+\s+)?addiction|"
        r"(?:hook(?:s|ed|ing)\s+(?:into|on|in))|"
        r"sinking\s+(?:their|its)\s+hooks?\s+into)\b",
        re.IGNORECASE,
    ),
    # Past-failure anchoring — opening or characterizing a subject by
    # leading with their prior failures.  "Fresh off a failed X",
    # "after a disastrous X", "following the collapse of" — anchors
    # the reader's frame before any facts are presented.
    re.compile(
        r"\b(?:fresh off (?:a |the )?(?:failed|disastrous|botched|bungled|doomed)|"
        r"(?:huge|massive|total|complete|spectacular|colossal|epic)\s+bust|"
        r"(?:failed|botched|bungled|doomed)\s+(?:metaverse|pivot|rebrand|launch|venture|experiment|gambit)|"
        r"search for (?:a |another )?win|"
        r"chasing (?:the next|another|yet another) (?:trend|fad|gimmick)|"
        r"desperate (?:attempt|bid|gambit|pivot|search))\b",
        re.IGNORECASE,
    ),
    # Standalone vice/gambling reframing — using "gambling" as a verb
    # or gerund to characterize non-gambling activities (prediction markets,
    # trading, investing) as morally equivalent to casino betting.
    # Distinct from "gambling addiction" (above) — catches stand-alone
    # editorial reframing: "gambling over anything", "into gambling",
    # "gamble on", "gambled away".
    re.compile(
        r"\b(?:gambling\s+over\s+(?:anything|everything)|"
        r"(?:into|towards?|embracing)\s+gambling|"
        r"gambled?\s+away|"
        r"wagered?\s+away|"
        r"betting\s+(?:over|on)\s+(?:anything|everything))\b",
        re.IGNORECASE,
    ),
    # Violence / physical-threat references — editorial deployment of
    # extreme physical acts (arson, assault, weapons) in coverage of
    # technology disputes.  Including these details is factually accurate
    # but their prominence in an article is an editorial choice that
    # elevates the stakes of a policy debate to personal safety.
    # Discovered via MIT TR "Resistance" article (Apr 2026):
    # "threw a Molotov cocktail at the OpenAI CEO Sam Altman's home"
    re.compile(
        r"\b(?:Molotov cocktail|firebombed?|arson(?:ist)?|"
        r"pipe bomb|explosive device|death threats?|"
        r"bomb threats?|swatting|swatted|"
        r"physically (?:attacked|assaulted|threatened)|"
        r"shots? fired|gunfire|gunshots?|"
        r"stabbed|stabbing)\b",
        re.IGNORECASE,
    ),
]


# Refusal-to-comment amplification: editorial device highlighting non-cooperation
_REFUSAL_AMPLIFICATION_PATTERNS: list[re.Pattern] = [
    re.compile(
        r"\b(?:declined? to comment|refused? to comment|"
        r"would(?:n't| not) (?:say|comment|respond|answer|address|confirm|deny)|"
        r"did not (?:respond|reply|answer|address)|"
        r"could not be reached|"
        r"say almost nothing|said almost nothing|"
        r"declined? to answer)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:no(?:t| )willing to|unwilling to)\s+(?:say|comment|explain|address|clarify|elaborate)\b",
        re.IGNORECASE,
    ),
]

# Military/government juxtaposition with consumer: editorial device
_JUXTAPOSITION_PATTERNS: list[re.Pattern] = [
    # Military/law enforcement juxtaposed with consumer context
    # NOTE: "government" removed — too generic, fires on policy/regulatory
    # articles where "government" means "federal regulator" not "military."
    # "public" removed from consumer side — too generic, fires on standard
    # "release to the public" language.  Kept "civilian" as the correct
    # military/civilian divide marker.
    re.compile(
        r"\b(?:military|Pentagon|law enforcement|police|intelligence|"
        r"surveillance|defense|FBI|CIA|NSA|"
        r"special operations|marshals?)\b"
        r".{0,120}?"
        r"\b(?:consumer|mass.?market|commercial|everyday|"
        r"everyone else|ordinary|civilian|retail)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    re.compile(
        r"\b(?:consumer|mass.?market|commercial|everyday|"
        r"everyone else|ordinary|civilian)\b"
        r".{0,120}?"
        r"\b(?:military|Pentagon|law enforcement|police|intelligence|"
        r"surveillance|defense|FBI|CIA|NSA|"
        r"special operations|marshals?)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Profit-vs-cuts juxtaposition: record/strong/high profits near layoffs/cuts/job losses
    # Central framing device in corporate accountability reporting
    re.compile(
        r"\b(?:record|strong|robust|soaring|surging|back.?to.?back|"
        r"billion.?dollar|quarterly|annual)\b"
        r".{0,80}?"
        r"\b(?:profit|profits|revenue|earnings|income)\b"
        r".{0,120}?"
        r"\b(?:layoff|layoffs|lay off|laid off|cut(?:ting|s)?|"
        r"slash(?:ed|ing|es)?|eliminat(?:ed?|ing|ion)|"
        r"fired?|firing|downsiz(?:ed?|ing)|restructur(?:ed?|ing)|"
        r"headcount|workforce reduction)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Reverse: layoffs near profits
    re.compile(
        r"\b(?:layoff|layoffs|lay off|laid off|cut(?:ting|s)?|"
        r"slash(?:ed|ing|es)?|eliminat(?:ed?|ing|ion)|"
        r"fired?|firing|downsiz(?:ed?|ing)|restructur(?:ed?|ing))\b"
        r".{0,120}?"
        r"\b(?:record|strong|robust|soaring|surging|back.?to.?back)\b"
        r".{0,40}?"
        r"\b(?:profit|profits|revenue|earnings|income)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Executive compensation vs. rank-and-file cuts
    re.compile(
        r"\b(?:\$\d+\s*(?:million|billion)|compensation|pay packages?)\b"
        r".{0,120}?"
        r"\b(?:layoff|layoffs|cut(?:ting|s)?|median\s+(?:compensation|pay|salary)|"
        r"fell|declined?|dropped?|reduced?)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # AI/tech spending/investment near layoffs — editorial framing that
    # juxtaposes massive capital expenditure with workforce reductions,
    # implying employees are being sacrificed for technology
    re.compile(
        r"\b(?:spending|invest(?:ing|ment|s)?|"
        r"(?:hundreds?\s+of\s+)?billions?|"
        r"billions?\s+of\s+dollars|"
        r"\$\d+\s*(?:billion|B)|"
        r"capex|capital\s+expenditure)\b"
        r".{0,160}?"
        r"\b(?:layoff|layoffs|lay\s+off|laid\s+off|"
        r"cut(?:ting|s)?\s+(?:jobs?|workers?|staff|employees?|workforce|positions?|headcount)|"
        r"slash(?:ed|ing|es)?\s+\d+\s*(?:%|percent)|"
        r"eliminat(?:ed?|ing|ion)\s+(?:jobs?|workers?|roles?|positions?)|"
        r"workforce\s+reduction|"
        r"offset\s+(?:the\s+)?(?:other\s+)?investments?)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Reverse: layoffs near investment/spending
    re.compile(
        r"\b(?:layoff|layoffs|lay\s+off|laid\s+off|"
        r"cut(?:ting)?\s+(?:\d+\s*(?:%|percent)|jobs?|workers?|staff)|"
        r"slash(?:ed|ing)?\s+\d+\s*(?:%|percent)|"
        r"10\s*(?:%|percent)\s+of\s+(?:its|the|their)\s+work\s*force)\b"
        r".{0,160}?"
        r"\b(?:spending|invest(?:ing|ment|s)?|"
        r"(?:hundreds?\s+of\s+)?billions?|"
        r"\$\d+\s*(?:billion|B)|"
        r"(?:A\.?I\.?|AI)\s+(?:spending|infrastructure|investment|initiative))\b",
        re.IGNORECASE | re.DOTALL,
    ),
]

# Timeline implication: editorial technique suggesting cover-up or reactive behavior
_TIMELINE_IMPLICATION_PATTERNS: list[re.Pattern] = [
    # "deleted/removed/pulled X after Y reported/revealed"
    re.compile(
        r"\b(?:deleted?|removed?|pulled|scrubbed|stripped|purged)\b"
        r".{0,80}?"
        r"\b(?:after|once|when|following)\b"
        r".{0,60}?"
        r"\b(?:reported?|revealed?|published|discovered|exposed|found|uncovered|investigation)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "a day after" / "hours after" / "days after" pattern
    re.compile(
        r"\b(?:a day|hours?|days?|shortly|immediately|within)\s+"
        r"(?:after|before|of)\b"
        r".{0,60}?"
        r"\b(?:reported?|revealed?|published|discovered|exposed|found)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Say-one-thing-do-another: "said X was still Y, but/however/yet Z was already"
    re.compile(
        r"\b(?:publicly|officially)\b"
        r".{0,80}?"
        r"\b(?:still|yet)\b"
        r".{0,80}?"
        r"\b(?:but|however|yet|even as|while|despite)\b"
        r".{0,80}?"
        r"\b(?:already|as early as|months before|before|prior to|long before)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "contradictory" / inconsistency language
    re.compile(
        r"\b(?:contradictory|contradicts?|inconsistent|at odds with|"
        r"raises questions about|undermines?|belies?|"
        r"despite (?:previous|prior|earlier|public) (?:claims?|statements?|messaging|assurances?))\b",
        re.IGNORECASE,
    ),
    # "on the eve of" / "shortly before" — editorial timing device suggesting
    # preemptive or premeditated suppression/action
    re.compile(
        r"\b(?:on the eve of|on the verge of|just before|shortly before|"
        r"the night before|the day before)\b"
        r".{0,60}?"
        r"\b(?:publication|launch|release|announcement|hearing|trial|vote|event|festival)\b",
        re.IGNORECASE | re.DOTALL,
    ),
]


# Power asymmetry framing: editorial device positioning a large entity's
# resources as crushing a smaller/individual entity, emphasising the
# imbalance of power (financial, legal, institutional) rather than the
# substantive dispute.  Common in whistleblower, antitrust, and labor
# coverage where the frame is "giant vs little guy."
_POWER_ASYMMETRY_PATTERNS: list[re.Pattern] = [
    # Financial/legal power vs individual — "$X corporation", "worth $X billion",
    # "multi-billion-dollar" near individual/person/whistleblower/worker/employee
    re.compile(
        r"\b(?:(?:trillion|billion|multi.?billion|multi.?million).?dollar|"
        r"\$\d+(?:\.\d+)?\s*(?:trillion|billion|million)|"
        r"worth\s+\$\d+|valued at\s+\$\d+)\b"
        r".{0,120}?"
        r"\b(?:individual|person|worker|employee|whistleblower|"
        r"activist|critic|plaintiff|woman|man|mother|father|"
        r"her\b|him\b|she\b|he\b)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Reverse direction: individual near corporate financial scale
    re.compile(
        r"\b(?:individual|person|worker|employee|whistleblower|"
        r"activist|critic|plaintiff|woman|man|single mother|single father)\b"
        r".{0,120}?"
        r"\b(?:(?:trillion|billion|multi.?billion|multi.?million).?dollar|"
        r"\$\d+(?:\.\d+)?\s*(?:trillion|billion|million)|"
        r"worth\s+\$\d+|valued at\s+\$\d+)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Legal army / legal machinery language
    re.compile(
        r"\b(?:army of (?:lawyers|attorneys)|legal (?:team|machinery|muscle|firepower|juggernaut)|"
        r"deep.?pocket(?:ed|s)?|"
        r"outspent|outgunned|outmatched|outlawyered|"
        r"unlimited (?:resources|legal|funds|budget)|"
        r"vastly (?:outspend|outresource|outmatch))\b",
        re.IGNORECASE,
    ),
    # David vs Goliath / explicit power asymmetry language
    re.compile(
        r"\b(?:David (?:and|vs?\.?|versus|against) Goliath|"
        r"David.?and.?Goliath|"
        r"power (?:imbalance|asymmetry|disparity|differential)|"
        r"punching (?:up|down)|"
        r"crushing|steamroll(?:ed|ing)?|"
        r"bulldoz(?:ed?|ing)|"
        r"overwhelm(?:ed|ing)?(?:\s+by)?(?:\s+(?:corporate|legal|financial)))\b",
        re.IGNORECASE,
    ),
    # "cannot afford" / "could not afford" near legal/fight/defense
    re.compile(
        r"\b(?:cannot|couldn't|could not|can't)\s+afford\b"
        r".{0,60}?"
        r"\b(?:legal|lawyer|attorney|fight|defense|defend|litigation|battle|challenge)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Fine/penalty amounts framed against individual capacity
    re.compile(
        r"\b(?:fines?\s+of|penalty\s+of|penalties\s+of|damages\s+of|"
        r"liable\s+for|facing\s+up\s+to|risking)\b"
        r".{0,40}?"
        r"\$\d+"
        r".{0,60}?"
        r"\b(?:per\s+(?:\w+\s+)?(?:violation|breach|instance|day)|"
        r"each\s+(?:\w+\s+)?(?:violation|breach|instance|time)|"
        r"bankrupt|ruin|devastat)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Surveillance / consent-violation power asymmetry — editorial language
    # framing institutional monitoring of individuals as unavoidable, non-
    # consensual, or coercive.  Common in workplace-surveillance coverage
    # (Meta MCI, emotion AI, bossware) and platform-data-harvesting coverage.
    # Distinct from loaded_language surveillance terms: power_asymmetry
    # requires a consent/choice/resistance element showing the power gap.
    re.compile(
        r"\b(?:could\s+not|couldn't|cannot|can't|unable\s+to|no\s+way\s+to)\s+"
        r"(?:opt\s+out|refuse|decline|resist|escape|avoid|stop|prevent|object|"
        r"consent|withdraw|block)"
        r".{0,80}?"
        r"\b(?:monitor|surveillance|tracking|recording|collecting|scraping|"
        r"watching|logging|capturing|training)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Reverse: monitoring/surveillance near powerlessness language
    re.compile(
        r"\b(?:monitor|surveillance|tracking|recording|collecting|"
        r"watching|logging|capturing)\b"
        r".{0,80}?"
        r"\b(?:(?:could|can)(?:n't|\s+not)\s+(?:opt\s+out|refuse|decline|resist|escape|object)|"
        r"(?:no|without)\s+(?:consent|choice|option|recourse|way\s+out|escape|alternative)|"
        r"(?:won't|wouldn't|will\s+not)\s+have\s+(?:much\s+)?power\s+to\s+resist|"
        r"involuntar(?:y|ily)|mandatory|compulsory|non.?optional|"
        r"(?:employees?|workers?|staff)\s+(?:likely\s+)?(?:won't|will\s+not)\s+have\s+(?:much\s+)?power)\b",
        re.IGNORECASE | re.DOTALL,
    ),
]


# CEO personalization: editorial choice to name the CEO before the company,
# personalizing corporate actions ("Mark Zuckerberg's Meta" vs just "Meta").
# This framing makes the company's actions feel like one person's decisions,
# which can amplify negative coverage or imply authoritarian control.
_CEO_PERSONALIZATION_PATTERNS: list[re.Pattern] = [
    # "[CEO]'s [Company]" — possessive CEO-company naming
    re.compile(
        r"\b(?:Mark Zuckerberg|Zuckerberg|Elon Musk|Musk|Tim Cook|Cook|"
        r"Sundar Pichai|Pichai|Satya Nadella|Nadella|Jeff Bezos|Bezos|"
        r"Sam Altman|Altman|Jensen Huang|Huang|Andy Jassy|Jassy)'s\s+"
        r"(?:Meta|Facebook|Instagram|WhatsApp|Tesla|Apple|Google|Alphabet|"
        r"Microsoft|Amazon|OpenAI|Nvidia|X|Twitter)\b",
        re.IGNORECASE,
    ),
    # "[CEO]'s [plan/vision/strategy/initiative]" — personalizing corporate
    # strategy under the CEO's name, implying individual authoritarian control
    # over institutional decisions.  Common in Atlantic/NYT coverage.
    re.compile(
        r"\b(?:Mark Zuckerberg|Zuckerberg|Elon Musk|Musk|Tim Cook|Cook|"
        r"Sundar Pichai|Pichai|Satya Nadella|Nadella|Jeff Bezos|Bezos|"
        r"Sam Altman|Altman|Jensen Huang|Huang|Andy Jassy|Jassy)'s\s+"
        r"(?:plan|vision|strategy|initiative|ambition|quest|mission|"
        r"push|drive|bet|gamble|gambit|dream|pitch|promise|agenda|"
        r"obsession|fixation|crusade|campaign)\b",
        re.IGNORECASE,
    ),
    # "[CEO]-led [Company]" or "[Company], led by [CEO]"
    re.compile(
        r"\b(?:Mark Zuckerberg|Zuckerberg|Elon Musk|Musk|Tim Cook|Cook|"
        r"Sundar Pichai|Pichai|Satya Nadella|Nadella|Sam Altman|Altman)"
        r"(?:-led|[\s,]+led)\s+\w+\b",
        re.IGNORECASE,
    ),
]

# Litigation framing: editorial positioning of a company/entity as fighting
# regulation or using courts adversarially rather than cooperating.
_LITIGATION_FRAMING_PATTERNS: list[re.Pattern] = [
    # "[entity] seeking/launching/filing legal/judicial action"
    re.compile(
        r"\b(?:seeking|launched?|filed?|pursuing|mounting|initiated?|"
        r"brought|bringing|challenging|fighting)\s+"
        r"(?:a\s+)?(?:judicial review|legal challenge|legal action|lawsuit|"
        r"complaint|suit|counter.?suit|court challenge|legal battle|"
        r"antitrust challenge|constitutional challenge|injunction|appeal|"
        r"class action|arbitration|petition)\b",
        re.IGNORECASE,
    ),
    # "legal challenge against" — adversarial preposition
    re.compile(
        r"\blegal (?:challenge|battle|fight|action|war|assault)\s+"
        r"(?:against|over|targeting|aimed at|directed at)\b",
        re.IGNORECASE,
    ),
    # "took/taking [entity] to court"
    re.compile(
        r"\b(?:took|taking|take|drag(?:ged|ging)?)\s+\w+\s+to\s+court\b",
        re.IGNORECASE,
    ),
    # "is suing / sued / sues [entity]"
    re.compile(
        r"\b(?:is\s+)?su(?:ing|ed?|es)\s+(?:the\s+)?(?:[A-Z]\w+)",
        re.IGNORECASE,
    ),
    # "arbitration ruling/order/process" — legal mechanism framing
    re.compile(
        r"\b(?:arbitration|arbitrator|severance)\s+"
        r"(?:ruling|order|process|agreement|clause|hearing|proceeding)\b",
        re.IGNORECASE,
    ),
]

# Cross-publication framing import: when an article references another
# outlet's characterization as settled background fact rather than
# attributed opinion.  E.g. "Several reports have depicted X as Y" imports
# another outlet's editorial judgment without naming the source, laundering
# opinion into apparent consensus.
_CROSS_PUBLICATION_IMPORT_PATTERNS: list[re.Pattern] = [
    # "several/multiple/other reports have described/depicted"
    re.compile(
        r"(?:several|multiple|other|previous|earlier|prior|numerous)\s+"
        r"(?:investigative\s+)?(?:reports?|articles?|investigations?|pieces?|stories)\s+"
        r"(?:have\s+)?(?:described|depicted|characterized|labeled|labelled|"
        r"called|dubbed|termed|portrayed|painted|shown|revealed|exposed|documented)\b",
        re.IGNORECASE,
    ),
    # "widely/commonly described/depicted as"
    re.compile(
        r"(?:widely|commonly|frequently|often|repeatedly|variously|routinely)\s+"
        r"(?:described|depicted|characterized|labeled|labelled|called|dubbed|"
        r"termed|portrayed|referred\s+to|reported|seen|viewed|regarded)\s+as\b",
        re.IGNORECASE,
    ),
    # "what [publication/reporters/critics] have called"
    re.compile(
        r"what\s+(?:\w+\s+){0,3}(?:have\s+)?(?:called|dubbed|termed|described\s+as|"
        r"labeled|labelled|characterized\s+as)\b",
        re.IGNORECASE,
    ),
    # Secondary-reporting attribution: "[pub] reports", "per the [pub]",
    # "[source] told [pub]".  These import credibility from the original
    # investigation.  Distinct from self_referential_investigation (which
    # cites the author's *own* publication).
    # Discovered via Futurism Cannes reframe (Jul 2026): "Wired reports",
    # "per the magazine", "per the reporting", "she told Wired".
    re.compile(
        r"\b(?:per the (?:magazine|newspaper|outlet|publication|report(?:ing)?|"
        r"investigation|story|article|piece))\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:according to (?:the )?(?:magazine|newspaper|outlet|publication|"
        r"report(?:ing)?|investigation|story))\b",
        re.IGNORECASE,
    ),
]

# Map device type to its pattern list
_DEVICE_PATTERNS: dict[str, list[re.Pattern]] = {
    "guilt_by_association": _GUILT_BY_ASSOCIATION_PATTERNS,
    "anonymous_authority": _ANONYMOUS_AUTHORITY_PATTERNS,
    "catastrophizing": _CATASTROPHIZING_PATTERNS,
    "false_balance": _FALSE_BALANCE_PATTERNS,
    "selective_omission_signal": _SELECTIVE_OMISSION_PATTERNS,
    "emotional_appeal": _EMOTIONAL_APPEAL_PATTERNS,
    "straw_man": _STRAW_MAN_PATTERNS,
    "loaded_language": _LOADED_LANGUAGE_PATTERNS,
    "refusal_amplification": _REFUSAL_AMPLIFICATION_PATTERNS,
    "juxtaposition": _JUXTAPOSITION_PATTERNS,
    "timeline_implication": _TIMELINE_IMPLICATION_PATTERNS,
    "power_asymmetry": _POWER_ASYMMETRY_PATTERNS,
    "ceo_personalization": _CEO_PERSONALIZATION_PATTERNS,
    "litigation_framing": _LITIGATION_FRAMING_PATTERNS,
    "cross_publication_import": _CROSS_PUBLICATION_IMPORT_PATTERNS,
}


# Military techno-optimism: editorial framing that normalises violence
# through technology language.  Phrases like "optimize the human as a
# weapons system" or "ordering drone strikes via eye-tracking" present
# military killing as a user-experience problem.  The language is factual
# (the subjects really are building weapons) but the editorial choice to
# lead with UX-style language over ethical/risk language reveals framing.
_MILITARY_TECHNO_OPTIMISM_PATTERNS: list[re.Pattern] = [
    # UX/consumer language applied to weapons/military
    re.compile(
        r"\b(?:optimize|optimise|streamline|seamless(?:ly)?|"
        r"user.?friendly|intuitive|clean interface|"
        r"eye.?tracking|voice command|gesture|"
        r"plain language|natural language)\b"
        r".{0,100}?"
        r"\b(?:weapon|strike|combat|warfare|soldier|military|"
        r"battle|kill|lethal|drone|artillery|target)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Reverse: weapons near UX language
    re.compile(
        r"\b(?:weapon|strike|combat|warfare|soldier|military|"
        r"drone|artillery|target|lethal)\b"
        r".{0,100}?"
        r"\b(?:optimize|optimise|seamless(?:ly)?|"
        r"user.?experience|UX|intuitive|"
        r"eye.?tracking|voice command|gesture|"
        r"plain language|natural language)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "Human as weapons system" / cyborg framing
    re.compile(
        r"\b(?:human\s+as\s+a?\s*weapon|"
        r"cyborg.?inspired|"
        r"man.?machine\s+(?:teaming|integration|interface)|"
        r"soldier.?(?:drone|robot|AI)\s+(?:team|integration|fusion|pairing)|"
        r"drones?\s+and\s+soldiers?\s+(?:see|act|decide|operate)\s+together)\b",
        re.IGNORECASE,
    ),
    # Euphemistic framing of military AI decision-making
    re.compile(
        r"\b(?:recommend\s+(?:courses?\s+of\s+action|strikes?|targets?)|"
        r"(?:AI|system|algorithm).?(?:driven|assisted|powered)\s+"
        r"(?:recognition|identification|targeting|engagement)|"
        r"approve\s+(?:via|through|by)\s+(?:the|a)\s+(?:chain|normal)\b)",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["military_techno_optimism"] = _MILITARY_TECHNO_OPTIMISM_PATTERNS


# Selective rehabilitation: editorial device that juxtaposes a figure's
# past controversy or ouster with their current acceptance/rehabilitation,
# implying opportunism or moral flexibility.
_SELECTIVE_REHABILITATION_PATTERNS: list[re.Pattern] = [
    re.compile(
        r"\b(?:ousted|fired|forced out|departed|left)\b"
        r".{0,150}?"
        r"\b(?:now|today|currently|once again|back (?:in|to|at|together))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    re.compile(
        r"\b(?:previously|formerly|once|at one time)\b"
        r".{0,60}?"
        r"\b(?:critic|opponent|rival|adversary|enemy)\b"
        r".{0,100}?"
        r"\b(?:now|today|currently|has since|have since)\b"
        r".{0,60}?"
        r"\b(?:partner|ally|collaborat|work(?:ing)? (?:with|together))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "friendlier posture" / "warmed to" / "softened stance" editorial language
    re.compile(
        r"\b(?:friendlier\s+posture|warmed?\s+(?:to|toward)|"
        r"soften(?:ed|ing)?\s+(?:stance|posture|position|approach|tone)|"
        r"embrace(?:d|s|ing)?\s+(?:the|a)?\s*(?:administration|government|regime|party)|"
        r"cozy(?:ing)?(?:\s+up)?\s+(?:to|with)\s+(?:the|a)?\s*(?:administration|government|regime))\b",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["selective_rehabilitation"] = _SELECTIVE_REHABILITATION_PATTERNS


# Failure precedent: editorial device that invokes a prior failed attempt at
# the same type of project to frame a current effort as likely to fail.
# Common pattern: "[previous actor] tried X, [negative outcome]" placed near
# description of a current effort to signal implicit doubt.  More effective
# than direct criticism because the reader draws the analogy themselves.
_FAILURE_PRECEDENT_PATTERNS: list[re.Pattern] = [
    # "[entity] was set to receive $X ... cancelled/failed/abandoned"
    re.compile(
        r"\b(?:was set to|had been|was expected to|was supposed to)"
        r".{0,100}?"
        r"\b(?:cancell?ed|abandon(?:ed|ing)|scrap(?:ped|ping)|"
        r"fail(?:ed|ing)|collaps(?:ed|ing)|"
        r"didn'?t prove viable|couldn'?t deliver|fell apart|"
        r"wasted|botched|stall(?:ed|ing)|shelved)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "after [previous entity] lost/failed/fumbled/stumbled"
    re.compile(
        r"\bafter\b"
        r".{0,80}?"
        r"\b(?:lost|fail(?:ed|ing)|fumbl(?:ed|ing)|stumbl(?:ed|ing)|"
        r"abandon(?:ed|ing)|collaps(?:ed|ing)|was cancell?ed)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "the previous [effort/attempt/lead/version] ... [negative outcome]"
    re.compile(
        r"\b(?:the |a )?(?:previous|prior|earlier|former|last|original)\s+"
        r"(?:effort|attempt|lead|leader|version|prototype|contract|program)\b"
        r".{0,120}?"
        r"\b(?:cancell?ed|fail(?:ed|ing)|abandon(?:ed|ing)|"
        r"didn'?t (?:work|prove|deliver|succeed)|fell short|"
        r"wasted|was scrap(?:ped|ping))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Retrospective comparative — "as [subject] was/were/did when ... [past failure]"
    # Sarcastic structure invoking past strategic failures to frame doubt
    # on a current effort: "he's just as likely to beat the competition
    # as he was when he decided to go all-in on the metaverse and crypto."
    # Matches the second half of the comparative ("as he was when...")
    # plus a known failure-domain anchor term within 80 chars.
    re.compile(
        r"\bas\s+(?:he|she|they|it|the company|Meta|Facebook|Google|"
        r"Apple|Microsoft|Amazon)\s+"
        r"(?:was|were|did)\s+when\b"
        r".{0,80}?"
        r"\b(?:metaverse|crypto|NFTs?|Web3|blockchain|pivot(?:ed)?|"
        r"all[- ]in|doubled down|bet big)\b",
        re.IGNORECASE | re.DOTALL,
    ),
]

_DEVICE_PATTERNS["failure_precedent"] = _FAILURE_PRECEDENT_PATTERNS


# ---------------------------------------------------------------------------
# Scandal comparison: using a notorious fraud, disaster, or scandal name as a
# compact pejorative label for a current company or product.  The name alone
# imports the full moral weight of the scandal without the writer needing to
# make an explicit accusation.  Distinct from precedent_analogy (which uses
# comparative constructions like "echoes" or "similar to"); scandal comparison
# is typically a direct label or "X is the new Y" / "Y of Z" construction.
#
# Identified in MIT TR "Subquadratic" (Jun 19, 2026):
#   "SubQ is either the biggest breakthrough since the Transformer ...
#    or it's AI Theranos."
# ---------------------------------------------------------------------------
_SCANDAL_COMPARISON_PATTERNS: list[re.Pattern] = [
    # "[prefix] Theranos/Enron/Madoff/Solyndra/FTX/WeWork/Wirecard"
    # as pejorative label (with optional domain prefix like "AI Theranos")
    re.compile(
        r"\b(?:(?:AI|tech|crypto|fintech|biotech|health|defense|energy)\s+)?"
        r"(?:Theranos|Enron|Madoff|Solyndra|FTX|WeWork|Wirecard|"
        r"Fyre Festival|Juicero|Nikola|Lordstown)\b",
        re.IGNORECASE,
    ),
    # "the [Theranos/Enron/etc.] of [domain]" construction
    re.compile(
        r"\bthe\s+(?:Theranos|Enron|Madoff|Solyndra|FTX|WeWork|Wirecard|"
        r"Fyre Festival|Juicero|Nikola|Lordstown)\s+of\s+\w+",
        re.IGNORECASE,
    ),
    # "[entity] is/was/could be the next [scandal name]"
    re.compile(
        r"\b(?:is|was|could be|might be|may be|becomes?|risks? becoming)\s+"
        r"(?:the\s+next\s+)?(?:another\s+)?"
        r"(?:Theranos|Enron|Madoff|Solyndra|FTX|WeWork|Wirecard|"
        r"Fyre Festival|Juicero|Nikola|Lordstown)\b",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["scandal_comparison"] = _SCANDAL_COMPARISON_PATTERNS
# maximize impact while maintaining deniability.
_RHETORICAL_QUESTION_PATTERNS: list[re.Pattern] = [
    # "Were there even X?" / "Was there even X?"
    re.compile(
        r"\b(?:were|was|is|are) there even\b.{3,60}?\?",
        re.IGNORECASE,
    ),
    # "Did anyone think to X?" / "Did anyone bother to X?"
    re.compile(
        r"\bdid anyone (?:think|bother|try|stop|consider|check)\b.{3,60}?\?",
        re.IGNORECASE,
    ),
    # "Why didn't they X?" / "Why did they not X?"
    re.compile(
        r"\bwhy (?:didn'?t|did(?:n'?| not)|wouldn'?t|hasn'?t|haven'?t) .{3,60}?\?",
        re.IGNORECASE,
    ),
    # "How could/did they not X?"
    re.compile(
        r"\bhow (?:could|did|can) .{3,40}? not .{3,40}?\?",
        re.IGNORECASE,
    ),
    # "How is that/this acceptable/possible?"
    re.compile(
        r"\bhow is (?:it|that|this) (?:possible|acceptable|okay|responsible)\?",
        re.IGNORECASE,
    ),
    # "What was X even doing?" / "What were they even thinking?"
    re.compile(
        r"\bwhat (?:was|were|is|are) .{3,30}? even .{3,30}?\?",
        re.IGNORECASE,
    ),
    # "Should we (seriously/really) consider/believe/accept...?" — philosophical challenge
    re.compile(
        r"\bshould (?:we|anyone|one|you) (?:seriously |really |actually )?(?:consider|believe|think|accept|take|trust|pretend|worry)\b.{3,80}?\?",
        re.IGNORECASE,
    ),
    # "Has anything (fundamentally/really) changed/shifted...?" — dismissive
    re.compile(
        r"\bhas (?:anything|something|this|that|it) (?:fundamentally |really |actually |truly )?(?:changed|shifted|improved|altered)\b.{3,60}?\?",
        re.IGNORECASE,
    ),
    # "How is this/that [adj], given that...?" — incredulous challenge
    re.compile(
        r"\bhow is (?:this|that|it) (?:\w+ )?(?:appropriate|reasonable|justified|ethical|acceptable|responsible|honest|defensible).{0,60}?\?",
        re.IGNORECASE,
    ),
    # "What are we to make of...?" — reflective/judgmental
    re.compile(
        r"\bwhat (?:are|is) (?:we|one|anyone) to (?:make|think) of\b.{3,60}?\?",
        re.IGNORECASE,
    ),
    # "So why are/is/do/does...?" — dismissive "So" opener
    re.compile(
        r"\bso why (?:are|is|do|does|did|would|should|hasn't|haven't|isn't|aren't)\b.{3,80}?\?",
        re.IGNORECASE,
    ),
    # "Is [entity] going to...?" — accountability challenge
    re.compile(
        r"\bis \w+ going to\b.{3,60}?\?",
        re.IGNORECASE,
    ),
    # "Who is [X]'s [Y]?" — legalistic/categorical challenge
    re.compile(
        r"\bwho is .{3,40}?\?",
        re.IGNORECASE,
    ),
    # ---------------------------------------------------------------------------
    # Speculative/reflective rhetorical questions — columnists posing
    # "what if" or "is it possible" questions that frame unstated
    # conclusions as open-ended speculation.  Distinct from the accusatory
    # patterns above; these invite the reader to draw the conclusion.
    #
    # Identified in MIT TR "Three things to watch amid Anthropic's latest
    # feud" (Jun 2026): "is it possible the government's next drastic
    # decision will be to say that US companies using models from China
    # pose a threat to national security?"
    # ---------------------------------------------------------------------------
    # "is it possible (that)...?" — speculative question inversion
    re.compile(
        r"\bis it (?:possible|conceivable|likely|plausible|realistic|naive to think)\b.{10,200}?\?",
        re.IGNORECASE | re.DOTALL,
    ),
    # "What will/would/could [X] bring/mean/look like?" — open-ended
    # cliffhanger question, often used at paragraph/article endings
    re.compile(
        r"\bwhat (?:will|would|could|might|does|did) .{3,60}?"
        r"(?:bring|mean|look like|hold|entail|portend|change|happen)\?",
        re.IGNORECASE | re.DOTALL,
    ),
    # "Can [entity/we] really/afford to...?" — challenging capability/cost
    re.compile(
        r"\bcan (?:\w+ )?(?:really|afford to|actually|ever)\b.{3,80}?\?",
        re.IGNORECASE | re.DOTALL,
    ),
    # Indirect/embedded rhetorical question — editorial device where a
    # journalist attributes a challenging question to unnamed critics or
    # sources as indirect speech, avoiding the question mark while
    # preserving the full rhetorical force.  Example: "critics ask what
    # exactly people are supposed to be adjusting to."
    # Discovered via Memeburn Meta glasses article (Jun 2026).
    re.compile(
        r"\b(?:ask|asks|asked|asking|wonder|wonders|wondered|questioning|questioned)\s+"
        r"(?:what|why|how|whether|who)\s+"
        r"(?:exactly |really |precisely |actually )?"
        r".{3,80}?"
        r"(?:supposed to|meant to|expected to|going to)\b",
        re.IGNORECASE | re.DOTALL,
    ),
]

_DEVICE_PATTERNS["rhetorical_question"] = _RHETORICAL_QUESTION_PATTERNS


# --- Hypocrisy frame / stated-vs-actual contradiction ---
# Detects editorial juxtaposition of an entity's stated position, policy,
# or public commitment against its actual behavior, creating an ironic
# contrast that implies dishonesty or self-contradiction.  Distinct from
# `corporate_reassurance_undercut` (which catches PR damage control language
# being structurally undermined) and `timeline_implication` (which catches
# temporal sequencing that implies cover-ups).  The hypocrisy frame specifically
# catches the "say one thing, do another" construction where both the stated
# and actual positions are explicitly present in the text.
#
# Identified as a gap in:
# - NYT voluntary review (Jun 23): "actively sought to position itself as a
#   responsible AI leader... Yet it has not agreed to the pre-release review"
# - Guardian Wynn-Williams (Jun 25): "We do not require our personnel to enter
#   into employment agreements that include non-disparagement clauses" vs.
#   Meta enforcing exactly such a clause from a 2017 agreement
# - Guardian Wynn-Williams (Jun 25): Facebook VP calling end of forced
#   arbitration "the right thing to do" while still enforcing the 2017 deal
_HYPOCRISY_FRAME_PATTERNS: list[re.Pattern] = [
    # "positioned/presented/portrayed itself as X... yet/but/however Y"
    re.compile(
        r"\b(?:position(?:ed|ing|s)?|present(?:ed|ing|s)?|portray(?:ed|ing|s)?|"
        r"brand(?:ed|ing|s)?|market(?:ed|ing|s)?|promot(?:ed|ing|es)?|"
        r"tout(?:ed|ing|s)?|champion(?:ed|ing|s)?|advocat(?:ed|ing|es)?)\s+"
        r"(?:itself|himself|herself|themselves|the company|the organization)\s+"
        r"(?:as\s+)?.{5,100}?"
        r"(?:yet|but|however|even as|while|despite|although|nonetheless|nevertheless|"
        r"at the same time|in contrast|ironically|paradoxically)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "publicly said/stated/claimed X... privately/internally/in practice Y"
    re.compile(
        r"\b(?:publicly|officially|openly|formally)\s+"
        r"(?:said|stated|claimed|declared|promised|pledged|committed|vowed|insisted)\b"
        r".{10,150}?"
        r"\b(?:privately|internally|in practice|in reality|behind the scenes|"
        r"behind closed doors|in fact|actually|meanwhile)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "We do not [policy claim]..." near contradiction evidence
    # Catches formal policy denial followed by evidence of exactly that behavior.
    # Uses wider window (400 chars) because policy statements and their
    # contradictions often span multiple paragraphs in legal/regulatory
    # articles (e.g., Guardian Wynn-Williams Jun 25, 2026: Meta's 2022
    # proxy statement "We do not require our personnel..." is several
    # paragraphs away from the article's evidence of enforcement).
    re.compile(
        r"\b(?:we do not|we don't|we never|the company does not|"
        r"the company doesn't|it does not|it doesn't)\s+"
        r"(?:require|force|mandate|compel|demand|engage in|practice|use|"
        r"employ|conduct|perform|utilize|impose)\b"
        r".{10,400}?"
        r"\b(?:but|however|yet|despite|although|in fact|actually|"
        r"contradicting|contradict(?:ed|s)|belied? by|"
        r"enforc(?:ed|ing|es)|requir(?:ed|ing|es)|"
        r"was (?:doing|requiring|enforcing|demanding)|"
        r"had been (?:doing|requiring|enforcing))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "the right thing to do" / "pivotal moment" / progressive language
    # near evidence of the opposite behavior — catches ironic self-congratulation
    re.compile(
        r"\b(?:the right thing (?:to do)?|a pivotal moment|"
        r"historic step|important step|"
        r"leading (?:the way|by example)|"
        r"set(?:ting)? (?:the|an?) (?:standard|example|precedent)|"
        r"commitment to|dedicated to|committed to)\b"
        r".{10,200}?"
        r"\b(?:but|however|yet|despite|ironically|paradoxically|"
        r"while (?:still|simultaneously|continuing|also)|"
        r"even as|at the same time|"
        r"continued to|continues to|still (?:enforces?|requires?|demands?|uses?))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "the only [entity] that has not" — isolation/holdout as implicit hypocrisy
    # when preceded by cooperative framing for peers
    re.compile(
        r"\b(?:the only|the sole|the last)\s+(?:major|significant|large|big|prominent)?\s*"
        r"(?:company|developer|firm|organization|publisher|platform|player|entity|tech giant)"
        r"(?:\s+(?:of|in|for|on|behind)\s+\w+(?:\s+\w+){0,4})?\s+"
        r"(?:that |which |to )?"
        r"(?:has not|have not|hasn't|haven't|did not|didn't|refused to|"
        r"declined to|failed to|has yet to|have yet to)\b",
        re.IGNORECASE,
    ),
    # Claim-vs-reality structural contradiction — wire-service form where
    # an entity's announced action is juxtaposed against observed reality
    # in sequential paragraphs, without explicit conjunction ("yet", "but").
    # E.g., "Meta said it will pause the program... The tool was still
    # recording as of Monday afternoon."
    # Identified in Reuters MCI Pause analysis (Jun 2026).
    re.compile(
        r"\b(?:said|announced|stated|confirmed|promised|pledged|vowed|committed)"
        r"(?:\s+\w+){0,4}?\s+"
        r"(?:it\s+)?(?:will|would|has|had|is|was)\s+"
        r"(?:pause|stop|halt|end|suspend|discontinue|shut down|wind down|"
        r"terminate|cease|phase out|pull|remove|disable|restrict|limit)"
        r"\b.{10,1200}?"
        r"\b(?:(?:was|were|is|are)\s+still\s+(?:\w+ing)|"
        r"still\s+(?:running|recording|collecting|tracking|monitoring|operating|active|accessible|available)|"
        r"continued\s+to\s+(?:\w+)|"
        r"continues\s+to\s+(?:\w+)|"
        r"has\s+not\s+(?:yet\s+)?(?:stopped|paused|halted|ended|ceased)|"
        r"had\s+not\s+(?:yet\s+)?(?:stopped|paused|halted|ended|ceased))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Internal safety team overrule — corporate leadership rejecting or
    # overruling recommendations from their own safety, trust, or ethics
    # teams.  Common in child safety and content moderation coverage where
    # the frame is "they knew it was harmful but chose not to act."
    # Identified in NYT school targeting article (Jun 2026):
    #   "TikTok's leaders decided not to disable notifications during
    #    school hours, rejecting a change that its safety teams had
    #    pushed for years."
    re.compile(
        r"\b(?:safety|trust|ethics|integrity|responsible|child\s+safety)\s+"
        r"(?:team|teams|group|unit|division|department|lead|manager|researchers?|experts?)s?\b"
        r".{0,200}?"
        r"\b(?:reject(?:ed|ing)?|overrul(?:ed|ing)?|ignor(?:ed|ing)?|dismiss(?:ed|ing)?|"
        r"overrode|override|overridden|decided\s+not\s+to|chose\s+not\s+to|"
        r"push(?:ed)?\s+(?:back|against)|shot\s+down|vetoed?|"
        r"disregard(?:ed|ing)?|sidelined?|marginalized?)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Reverse: leadership rejection near safety team recommendation
    re.compile(
        r"\b(?:reject(?:ed|ing)?|overrul(?:ed|ing)?|ignor(?:ed|ing)?|dismiss(?:ed|ing)?|"
        r"overrode|override|decided\s+not\s+to|chose\s+not\s+to)\b"
        r".{0,200}?"
        r"\b(?:safety|trust|ethics|integrity|responsible|child\s+safety)\s+"
        r"(?:team|teams|group|unit|division|department|lead|manager|researchers?|experts?)s?\b"
        r".{0,100}?"
        r"\b(?:recommend(?:ed|ation|ations)?|push(?:ed)?\s+for|"
        r"urg(?:ed|ing)?|propos(?:ed|al|als)?|suggest(?:ed|ion|ions)?|"
        r"call(?:ed)?\s+for|advocat(?:ed|ing)?)\b",
        re.IGNORECASE | re.DOTALL,
    ),
]

_DEVICE_PATTERNS["hypocrisy_frame"] = _HYPOCRISY_FRAME_PATTERNS


# --- Analogy stacking ---
# Detects when an article uses multiple distinct analogies/comparisons for the
# same subject.  Three or more stacked analogies is a persuasion technique that
# amplifies perceived severity beyond what any single comparison conveys.
# Pattern: comparison markers ("like," "the equivalent of," "compared to,"
# "likened it to," etc.).  Individual matches are collected and the device
# fires as a post-pass in detect_framing_devices when 3+ are found.
_ANALOGY_MARKER_PATTERNS: list[re.Pattern] = [
    # "the [digital/modern/online] equivalent of"
    re.compile(
        r"\bthe (?:\w+ )?equivalent of\b.{3,80}",
        re.IGNORECASE,
    ),
    # "likened it to" / "I've likened it to"
    re.compile(
        r"\b(?:I(?:'ve)? )?liken(?:ed|s)? (?:it |this |them |that )?to\b.{3,60}",
        re.IGNORECASE,
    ),
    # "compared it to" / "others have compared it to"
    re.compile(
        r"\b(?:have |has )?compare[sd]? (?:it |this |them |that )?to\b.{3,60}",
        re.IGNORECASE,
    ),
    # "like [a/an/the] [noun]" used as simile — requires article or determiner
    # to avoid matching "like" as a verb
    re.compile(
        r"\blike (?:a|an|the|another|some) (?:\w+ ){0,3}\w+",
        re.IGNORECASE,
    ),
    # "is [qualifier] [a/an]" — metaphor construction
    # Qualifier is REQUIRED to avoid false positives on factual descriptions
    # like "is a Turing Award recipient" or "is a serial entrepreneur".
    # Without the qualifier, "is a [noun]" is almost always a factual
    # statement, not a rhetorical comparison.
    re.compile(
        r"\bis (?:essentially |basically |effectively |really |fundamentally |"
        r"nothing (?:more |less )than |just |merely |in effect |quite )"
        r"(?:a|an) .{3,60}?(?:\.|,|;)",
        re.IGNORECASE,
    ),
    # "think of it as" / "think of slop as"
    re.compile(
        r"\bthink of (?:it|this|them|that|\w+) as\b.{3,60}",
        re.IGNORECASE,
    ),
    # "reminiscent of" / "evokes" / "echoes of" / "echoes [noun]"
    re.compile(
        r"\b(?:reminiscent of|evokes?|echoes?(?: of)?)\b.{3,60}",
        re.IGNORECASE,
    ),
    # "harks back to" / "hark back to" / "mirrors" / "parallels"
    re.compile(
        r"\b(?:harks? back to|mirrors?|parallels?|recalls?|conjures?)\b.{3,60}",
        re.IGNORECASE,
    ),
]

# Note: analogy_stacking patterns are NOT registered in _DEVICE_PATTERNS
# because the device fires only when 3+ distinct analogy markers are found.
# Individual markers are collected by _detect_analogy_stacking() and injected
# into the results if threshold is met.


# --- Ironic quotation ---
# Detects when a direct quote from a tech/corporate figure is immediately
# undercut by editorial contradiction — a rhetorical device where the
# subject's own words are deployed against them.
# Pattern: quoted text followed within ~2 sentences by a contradiction marker.
_IRONIC_QUOTATION_PATTERNS: list[re.Pattern] = [
    # Quote ending followed by contradiction — smart quotes
    re.compile(
        r'[\u201d"].{0,10}?'     # end of quote (smart or straight)
        r'(?:\.\s+|\s*[;:]\s*)'  # sentence boundary
        r'(?:But |Yet |However,? |In (?:other words|reality|practice|fact),? |'
        r'The (?:idea|reality|truth|problem|trouble) is |'
        r'What .{3,40}? (?:is actually|actually|really) |'
        r'(?:That|This|It) (?:is|was|sounds) .{0,20}?(?:wrong|misleading|naive|'
        r'simplistic|misguided|disingenuous|absurd|laughable|delusional))',
        re.IGNORECASE | re.DOTALL,
    ),
    # "seems to elide" / "seems to ignore" / "seems to forget" — undercut via
    # polite intellectual dismissal (common in Atlantic/NYT essay prose)
    re.compile(
        r'[\u201d"].{0,200}?'
        r'\bseems? to (?:elide|ignore|forget|overlook|miss|gloss over|paper over|'
        r'conflate|sidestep|obscure|downplay|minimize)',
        re.IGNORECASE | re.DOTALL,
    ),
    # Same pattern for straight quotes
    re.compile(
        r'".{0,200}?'
        r'\bseems? to (?:elide|ignore|forget|overlook|miss|gloss over|paper over|'
        r'conflate|sidestep|obscure|downplay|minimize)',
        re.IGNORECASE | re.DOTALL,
    ),
    # "wrongly believe" / "wrongly assume" — editorial verdict after quote
    re.compile(
        r'[\u201d"].{0,200}?'
        r'\b(?:wrongly|mistakenly|naively|incorrectly) '
        r'(?:believe|assume|suggest|claim|imply|argue)',
        re.IGNORECASE | re.DOTALL,
    ),
    # Same pattern for straight quotes
    re.compile(
        r'".{0,200}?'
        r'\b(?:wrongly|mistakenly|naively|incorrectly) '
        r'(?:believe|assume|suggest|claim|imply|argue)',
        re.IGNORECASE | re.DOTALL,
    ),
    # ---------------------------------------------------------------------------
    # Ironic attribution verbs: editorial word choices that signal the
    # journalist considers the quoted statement self-important, inflated,
    # or performative.  "Touted" means the subject praised it but the
    # journalist implies skepticism; "boasted" implies bravado the
    # journalist doesn't share.  These are distinct from neutral attribution
    # ("said", "stated", "noted") and from loaded language (which
    # characterizes the subject directly).  The irony is in the verb choice:
    # the quote is deployed as evidence of the subject's disconnect.
    #
    # Identified in Guardian Wynn-Williams (Jun 25, 2026):
    #   "Facebook's vice president of people touted this policy change as
    #    'the right thing to do' and 'a pivotal moment for our industry'"
    #   — "touted" is not neutral attribution; it frames the quote as
    #   self-congratulatory, setting up the article's later reveal that
    #   Meta still enforces the 2017 arbitration agreement.
    # ---------------------------------------------------------------------------
    # [entity] touted/boasted/trumpeted + quoted text
    re.compile(
        r"\b(?:touted|boasted|bragged|trumpeted|proclaimed|heralded|"
        r"crowed|gushed|enthused|effused|celebrated|hailed|"
        r"paraded|flaunted|lauded|glorified)\b"
        r".{0,60}?"
        r'(?:["\u201c])',
        re.IGNORECASE | re.DOTALL,
    ),
    # [entity] called/described X as + quoted text with ironic framing
    # Only when the article later undercuts: requires proximity to
    # "but"/"however"/"yet"/"while" within ~300 chars after the quote
    re.compile(
        r"\b(?:touted|boasted|bragged|trumpeted|proclaimed|heralded|"
        r"crowed|gushed|celebrated|hailed)\s+"
        r"(?:this|that|the|it|its|his|her|their)?\s*"
        r"(?:\w+\s+){0,4}"
        r"(?:as\b)",
        re.IGNORECASE | re.DOTALL,
    ),
    # ---------------------------------------------------------------------------
    # Scare quotes / distancing quotes: single words or short phrases
    # placed in quotation marks to signal the author considers the term
    # loaded, contested, borrowed, or inapplicable.  Distinct from direct
    # quotations (full sentences attributed to named sources) and from
    # ironic attribution verbs above.  The author is not quoting a person;
    # they are marking a word as not their own, or casting doubt on its
    # standard meaning.
    #
    # Identified in MIT TR "Three things to watch" (Jun 2026):
    #   - "doomers" — loaded label placed in quotes to distance
    #   - "exporting" — legal term questioned via scare quotes
    #   - "wake-up call" — attributed idiom placed in quotes
    #
    # Pattern: 1-4 word phrase in quotes that does NOT start with a
    # capital letter (to exclude proper nouns and sentence-start quotes)
    # or starts lowercase explicitly.
    # ---------------------------------------------------------------------------
    # Straight-quote scare quotes: "word" or "short phrase" in mid-sentence
    re.compile(
        r'(?<=\s)"([a-z][^"]{0,40}?)"(?=[\s,;.\-—\)])',
        re.DOTALL,
    ),
    # Smart-quote scare quotes: \u201c word \u201d
    re.compile(
        r'(?<=\s)\u201c([a-z][^\u201d]{0,40}?)\u201d(?=[\s,;.\-—\)])',
        re.DOTALL,
    ),
    # Scare quotes around terms preceded by "broadly labeled/called/termed/dubbed"
    re.compile(
        r'\b(?:broadly|commonly|widely|often|sometimes|loosely|derisively|'
        r'pejoratively|affectionately|ironically|sarcastically)\s+'
        r'(?:labeled|called|termed|dubbed|known as|referred to as)\s+'
        r'["\u201c]([^"\u201d]{1,40}?)["\u201d]',
        re.IGNORECASE | re.DOTALL,
    ),
]

_DEVICE_PATTERNS["ironic_quotation"] = _IRONIC_QUOTATION_PATTERNS


# ---------------------------------------------------------------------------
# Isolation framing: editorial technique that singles out a company/entity
# as "the only" one not doing something that peers/industry has adopted.
# Creates implicit pressure and negative framing through exclusion language.
# Common in NYT-style institutional tech reporting.
# ---------------------------------------------------------------------------
_ISOLATION_FRAMING_PATTERNS: list[re.Pattern] = [
    # "X is the only major/significant/leading company/developer/firm that has not..."
    re.compile(
        r"\b(?:is|remains?|was|stands? as)\s+the\s+only\s+"
        r"(?:major|significant|leading|big|large|prominent|remaining)?\s*"
        r"(?:U\.?S\.?|American|European|Western|global)?\s*"
        r"(?:company|developer|firm|maker|provider|platform|tech giant|"
        r"lab|laboratory|operator|player|vendor|manufacturer)\b",
        re.IGNORECASE,
    ),
    # "the lone/sole holdout" / "the last holdout"
    re.compile(
        r"\b(?:the\s+)?(?:lone|sole|last(?:\s+remaining)?|only)\s+"
        r"(?:holdout|outlier|exception|refuser|dissenter|resister)\b",
        re.IGNORECASE,
    ),
    # "alone among its peers/rivals/competitors"
    re.compile(
        r"\b(?:alone|isolated|standing alone|standing apart)\s+"
        r"(?:among|from)\s+(?:its\s+)?(?:peers|rivals|competitors|counterparts|"
        r"fellow|other|industry)\b",
        re.IGNORECASE,
    ),
    # "while every other / all other / its peers have..."
    re.compile(
        r"\b(?:while|whereas|even as|although)\s+"
        r"(?:every other|all other|all of its|its\s+(?:peers|rivals|competitors)|"
        r"the rest of the industry|other major)\b"
        r".{0,80}?"
        r"\b(?:have|has|had|agreed|signed|accepted|adopted|complied|committed)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "unlike its peers" / "unlike every other"
    re.compile(
        r"\b(?:unlike)\s+(?:its\s+)?(?:peers|rivals|competitors|counterparts|"
        r"every other|all other|the rest)\b",
        re.IGNORECASE,
    ),
    # "X has not/refused to X that Y, Z, and W already have"
    re.compile(
        r"\bhas\s+(?:not\s+(?:yet\s+)?)?(?:agreed|signed|accepted|adopted|committed|submitted)\b"
        r".{0,120}?"
        r"\b(?:that|which|while)\s+(?:\w+,?\s+){1,6}(?:and\s+\w+\s+)?(?:have|has|had)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "singled out" / "set apart" / "left behind"
    re.compile(
        r"\b(?:singled out|set apart|left behind|left out|out of step|"
        r"lagging behind|falling behind|dragging (?:its |their )?feet)\b",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["isolation_framing"] = _ISOLATION_FRAMING_PATTERNS


# ---------------------------------------------------------------------------
# Pressure language: editorial word choices that frame actions as coercive
# or resistant — "pressing," "urging," "demanding" applied to institutional
# actors create an implied power dynamic beyond neutral reporting.
# ---------------------------------------------------------------------------
_PRESSURE_LANGUAGE_PATTERNS: list[re.Pattern] = [
    # Government/institution "pressing" / "pushing" / "urging" a company
    re.compile(
        r"\b(?:is |are |has been |was |were )?(?:pressing|pushing|pressuring|urging|"
        r"leaning on|squeezing|nudging|strong-?arming|arm-?twisting|"
        r"calling on|bearing down on)\s+"
        r"(?:\w+\s+){0,3}(?:to|into)\b",
        re.IGNORECASE,
    ),
    # "confidential request" / "private demand" — escalation through secrecy
    re.compile(
        r"\b(?:confidential|private|secret|behind.?the.?scenes?|quiet|discreet)\s+"
        r"(?:request|demand|ultimatum|warning|communication|message|pressure)\b",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["pressure_language"] = _PRESSURE_LANGUAGE_PATTERNS


# ---------------------------------------------------------------------------
# Geopolitical regulatory pressure: editorial framing of international
# regulatory tensions as geopolitical confrontation.  Distinct from
# generic pressure_language because it involves cross-border dynamics:
# embassy/diplomatic submissions as pressure tools, sovereignty/defiance
# rhetoric, trade-tension language, and "singles out" accusations.
# Common in Guardian and UK press coverage of US-UK tech regulation
# disputes (e.g., Online Safety Act vs. Trump administration pushback).
# ---------------------------------------------------------------------------
_GEOPOLITICAL_REGULATORY_PRESSURE_PATTERNS: list[re.Pattern] = [
    # Embassy/diplomatic submissions as pressure tools
    re.compile(
        r"\b(?:embassy|consulate|ambassador|diplomat(?:ic)?|envoy)\b"
        r".{0,80}?"
        r"\b(?:warn(?:ing|ed)?|submission|notice|statement|intervention|"
        r"concern|object(?:ion|ed)?|oppos(?:e[ds]?|ition)|urg(?:e[ds]?|ing)|"
        r"caution(?:ed)?|advis(?:e[ds]?|ory))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Reverse: pressure verbs near diplomatic actors
    re.compile(
        r"\b(?:warn(?:ing|ed)?|submission|notice|intervention|"
        r"concern|object(?:ion|ed)?|oppos(?:e[ds]?|ition))\b"
        r".{0,80}?"
        r"\b(?:embassy|consulate|ambassador|diplomat(?:ic)?|envoy|"
        r"White House|State Department|administration)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Sovereignty/defiance rhetoric — editorial positioning of a government
    # as defiant against foreign pressure.
    # Excludes literal physical "stood firm" / "standing firm" contexts
    # (e.g., "security guards stood firm") via negative lookbehind for
    # physical-actor nouns within 60 chars.  Identified in WebProNews
    # Meta Dublin contractors article (May 2026): "security guards at
    # Meta's gates stood firm, arms crossed" is literal, not geopolitical.
    re.compile(
        # "defy/defied/defying" requires proximity to geopolitical actors
        # or regulatory context to avoid false positives on non-geopolitical
        # uses like "responses that defied their guardrails."
        # Discovered via Futurism Cannes reframe (Jul 2026).
        r"\b(?:not concerned|not deterred|will not (?:be )?(?:deterred|swayed|"
        r"intimidated|bullied)|undeterred|defiant|"
        r"will always act in .{0,30}?national interest|"
        r"sovereign(?:ty)?|"
        r"will go ahead despite|"
        r"will not back down|standing firm|stood firm)\b",
        re.IGNORECASE,
    ),
    # Defiance verbs — separate pattern requiring geopolitical context
    # within 80 chars to suppress FPs like "defied their guardrails."
    re.compile(
        r"\b(?:defy|defied|defying)\b"
        r"(?=.{0,80}?"
        r"\b(?:government|regulat|legislat|parliament|congress|EU|"
        r"commission|court|law|authority|authorit|sanction|ban|"
        r"ruling|order|decree|mandate|diplomat|embassy|sovereign|"
        r"Brussels|Washington|Beijing|Westminster)\b)",
        re.IGNORECASE | re.DOTALL,
    ),
    # Trade tension / regulatory friction language
    re.compile(
        r"\b(?:source of tension|trade (?:tension|friction|war|dispute|conflict)|"
        r"regulatory (?:friction|tension|clash|conflict|divergence|dispute)|"
        r"disproportionate (?:compliance )?burden|"
        r"singles? out (?:\w+ )?(?:tech |technology |American |US |U\.S\. )?"
        r"(?:firm|compan|platform|giant)|"
        r"(?:target(?:s|ed|ing)?) (?:\w+ )?(?:American |US |U\.S\. )?"
        r"(?:firm|compan|platform|giant))\b",
        re.IGNORECASE,
    ),
    # "across the Atlantic" / "transatlantic" regulatory language
    re.compile(
        r"\b(?:(?:from |across )?(?:the )?Atlantic|transatlantic)\b"
        r".{0,60}?"
        r"\b(?:criticism|concern|pressure|tension|friction|pushback|"
        r"free speech|censorship|regulation)\b",
        re.IGNORECASE | re.DOTALL,
    ),
]

_DEVICE_PATTERNS["geopolitical_regulatory_pressure"] = (
    _GEOPOLITICAL_REGULATORY_PRESSURE_PATTERNS
)


# ---------------------------------------------------------------------------
# Self-referential investigation: editorial device where a publication
# cites its own prior investigations or discoveries within an article,
# positioning itself as an investigative authority.  Common in Wired,
# NYT, and Guardian articles that cross-reference their own scoops.
# Example: "WIRED discovered code..." or "The Guardian has learned..."
# This is distinct from simple self-mentions ("Wired reports") because it
# claims an active investigative role, lending the publication's authority
# to the framing of the current article.
# ---------------------------------------------------------------------------
_SELF_REFERENTIAL_INVESTIGATION_PATTERNS: list[re.Pattern] = [
    # Publication + investigative verb (active voice)
    # Covers: "WIRED discovered", "The Guardian has learned",
    # "The New York Times first reported", "MIT Technology Review found"
    re.compile(
        r"\b(?:WIRED|Wired|The Guardian|Guardian|"
        r"(?:The )?New York Times|NYT|"
        r"(?:The )?Atlantic|"
        r"MIT Technology Review|"
        r"Reuters|Bloomberg|"
        r"(?:The )?Washington Post|"
        r"(?:The )?Wall Street Journal|WSJ|"
        r"Business Insider|Insider|"
        r"(?:The )?Verge|(?:The )?Information)"
        r"\s+"
        r"(?:has |had |have )?"
        r"(?:first )?"
        r"(?:discovered|uncovered|revealed|learned|found|obtained|"
        r"reported|confirmed|identified|exposed|unearthed|"
        r"determined|established|documented|verified)\b",
        re.IGNORECASE,
    ),
    # "as [PUBLICATION] reported" / "according to a [PUBLICATION] investigation"
    re.compile(
        r"\b(?:as|after|following|since)\s+"
        r"(?:WIRED|Wired|The Guardian|Guardian|"
        r"(?:The )?New York Times|NYT|"
        r"(?:The )?Atlantic|"
        r"MIT Technology Review|"
        r"Reuters|Bloomberg|"
        r"(?:The )?Washington Post|"
        r"(?:The )?Wall Street Journal|WSJ|"
        r"Business Insider|Insider|"
        r"(?:The )?Verge|(?:The )?Information)"
        r"(?:'s)?\s+"
        r"(?:earlier |prior |previous |recent )?"
        r"(?:report|investigation|analysis|review|expose|story|"
        r"reporting|findings?|inquiry|examination|scoop)",
        re.IGNORECASE,
    ),
    # Reflexive: "our investigation" / "our reporting" / "this publication"
    re.compile(
        r"\b(?:our\s+(?:investigation|reporting|analysis|findings?|"
        r"review|examination|inquiry|report)|"
        r"this (?:publication|outlet|newsroom|paper)\s+"
        r"(?:has |had |have )?"
        r"(?:first )?"
        r"(?:discovered|uncovered|revealed|learned|found|"
        r"reported|confirmed|identified|exposed))\b",
        re.IGNORECASE,
    ),
    # Passive voice: "reporting/investigation by [PUBLICATION]"
    # Catches: "follow reporting by WIRED", "an investigation by NYT",
    # "research by The Guardian", "analysis by MIT Technology Review"
    re.compile(
        r"\b(?:report(?:ing|ed)?|investigat(?:ion|ed)|analysis|review|"
        r"research|expos[eé]|findings?|inquiry|examination|scoop)"
        r"\s+by\s+"
        r"(?:WIRED|Wired|The Guardian|Guardian|"
        r"(?:The )?New York Times|NYT|"
        r"(?:The )?Atlantic|"
        r"MIT Technology Review|"
        r"Reuters|Bloomberg|"
        r"(?:The )?Washington Post|"
        r"(?:The )?Wall Street Journal|WSJ|"
        r"Business Insider|Insider|"
        r"(?:The )?Verge|(?:The )?Information)\b",
        re.IGNORECASE,
    ),
    # Document access claim: "seen/obtained/reviewed by [PUBLICATION]"
    # Catches: "an internal post seen by WIRED", "a memo obtained by NYT",
    # "documents reviewed by The Guardian"
    # This positions the publication as having privileged access to internal
    # or confidential materials, lending authority to the reporting.
    re.compile(
        r"\b(?:seen|obtained|reviewed|viewed|acquired|accessed|"
        r"received|provided to|shared with|leaked to)"
        r"\s+by\s+"
        r"(?:WIRED|Wired|The Guardian|Guardian|"
        r"(?:The )?New York Times|NYT|"
        r"(?:The )?Atlantic|"
        r"MIT Technology Review|"
        r"Reuters|Bloomberg|"
        r"(?:The )?Washington Post|"
        r"(?:The )?Wall Street Journal|WSJ|"
        r"Business Insider|Insider|"
        r"(?:The )?Verge|(?:The )?Information)\b",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["self_referential_investigation"] = (
    _SELF_REFERENTIAL_INVESTIGATION_PATTERNS
)


# ---------------------------------------------------------------------------
# Sovereignty framing: editorial device deploying national/patriotic
# identity language ("British families", "American innovation",
# "our children") to reframe tech regulation (or its opposition) as
# patriotic duty vs foreign interference.  Common in Guardian UK-centric
# coverage and NYT US-exceptionalism coverage.  Distinct from loaded
# language — sovereignty framing is a strategic deployment of national
# identity to delegitimize foreign corporate/government positions, not
# mere emotional vocabulary.
# ---------------------------------------------------------------------------
_SOVEREIGNTY_FRAMING_PATTERNS: list[re.Pattern] = [
    # "British/American/our [families/children/citizens/consumers/workers]"
    # in tech regulation context
    re.compile(
        r"\b(?:British|American|our|this country'?s|the nation'?s)\s+"
        r"(?:families|children|kids|young people|parents|consumers|"
        r"citizens|workers|people|users|public|interests?|sovereignty|"
        r"national interest|values)\b",
        re.IGNORECASE,
    ),
    # "national interest" / "national security" near tech/regulation
    re.compile(
        r"\b(?:national interest|national security|sovereign(?:ty)?|"
        r"domestic (?:regulation|law|standards|policy))\b"
        r".{0,120}?"
        r"\b(?:tech|platform|social media|Silicon Valley|"
        r"big tech|American (?:tech|compan)|"
        r"Meta|Google|Apple|Amazon|Microsoft|Facebook)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Reverse: tech companies near sovereignty language
    re.compile(
        r"\b(?:tech|platform|social media|Silicon Valley|"
        r"big tech|American (?:tech|compan)|"
        r"Meta|Google|Apple|Amazon|Microsoft|Facebook)\b"
        r".{0,120}?"
        r"\b(?:national interest|national security|sovereign(?:ty)?|"
        r"domestic (?:regulation|law|standards|policy))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "act in the [UK's/nation's/country's] interest"
    re.compile(
        r"\bact in (?:the )?(?:UK'?s|Britain'?s|America'?s|nation'?s|"
        r"country'?s|our|the) (?:national )?interest\b",
        re.IGNORECASE,
    ),
    # "will not deter/stop/prevent [the UK/us/Britain/America]"
    re.compile(
        r"\bwill not (?:deter|stop|prevent|intimidate|pressure)\s+"
        r"(?:the UK|Britain|us|America|this (?:government|country))\b",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["sovereignty_framing"] = _SOVEREIGNTY_FRAMING_PATTERNS


# ---------------------------------------------------------------------------
# Precedent analogy: editorial device where a current controversy is framed
# through explicit comparison to a prior, well-known case — often one with
# settled public opinion (opioid crisis, tobacco litigation, Enron).  Unlike
# analogy_stacking (which requires 3+ stacked analogies), a single strong
# precedent analogy is itself a framing device: it imports the moral weight
# of the precedent onto the current story without the reader needing to
# evaluate the current facts independently.
#
# Identified in Reuters "who pays the lawyers" (Jun 23, 2026):
#   "echoes opioid-era coverage fights" — imports the settled villainy of
#   opioid manufacturers onto Meta's insurance dispute.
# ---------------------------------------------------------------------------
_PRECEDENT_ANALOGY_PATTERNS: list[re.Pattern] = [
    # "echoes [adj]-era [noun]" — era-based precedent
    re.compile(
        r"\b(?:echoes?|recalls?|mirrors?|parallels?|evokes?|conjures?|reprises?)\s+"
        r"(?:the\s+)?(?:\w+[- ])?(?:era|age|epoch|period|wave|cycle)\b.{3,80}",
        re.IGNORECASE,
    ),
    # "much like / just as / similar to [known precedent]"
    re.compile(
        r"\b(?:much like|just as|similar to|akin to|not unlike|in a reprise of)\s+"
        r"(?:the\s+)?(?:\w+\s+){1,4}"
        r"(?:litigation|lawsuits?|cases?|crisis|scandal|battle|fight|dispute|prosecution)",
        re.IGNORECASE,
    ),
    # "following [the/a] playbook from / borrowed from"
    re.compile(
        r"\b(?:following|borrowing|taking)\s+(?:the\s+|a\s+)?"
        r"(?:playbook|template|script|blueprint|approach|strategy)\s+"
        r"(?:from|of|used in)\b.{3,80}",
        re.IGNORECASE,
    ),
    # "as was the case with/in [precedent]"
    re.compile(
        r"\bas (?:was|is) the case (?:with|in)\b.{3,80}",
        re.IGNORECASE,
    ),
    # "[noun] dispute/battle/fight echoes / is reminiscent of"
    re.compile(
        r"\b(?:dispute|battle|fight|clash|struggle|confrontation|reckoning)\s+"
        r"(?:echoes?|is reminiscent of|recalls?|mirrors?|parallels?|evokes?)\b.{3,80}",
        re.IGNORECASE,
    ),
    # ---------------------------------------------------------------------------
    # Cross-domain analogy: "in the manner of" / "the way [domain] handles"
    # imports frames from a known high-stakes domain (nuclear, military,
    # pharmaceutical, etc.) onto the current subject.  Distinct from the
    # era-based patterns above; this catches direct domain-transference.
    #
    # Identified in MIT TR "Three things to watch" (Jun 2026):
    #   "applying the concept of nonproliferation to software—trying to
    #    control and restrict dangerous AI models in the manner of the
    #    uranium used for nuclear weapons"
    # ---------------------------------------------------------------------------
    re.compile(
        r"\b(?:in the manner of|in the (?:same )?way (?:that )?(?:\w+ ){0,3}"
        r"(?:handles?|treats?|regulates?|controls?|restricts?)|"
        r"(?:the concept|the logic|the framework|the model) of\s+\w+\s+(?:applied|extended|imported) to|"
        r"applying the (?:concept|logic|framework|model|principle) of)\b"
        r".{3,120}?"
        r"\b(?:nuclear|uranium|weapons?|arms|munitions?|pharmaceuticals?|"
        r"drugs?|tobacco|opioid|asbestos|chemical|biological|classified|"
        r"controlled substance|narcotics?|explosives?)\b",
        re.IGNORECASE | re.DOTALL,
    ),
]

_DEVICE_PATTERNS["precedent_analogy"] = _PRECEDENT_ANALOGY_PATTERNS

# ---------------------------------------------------------------------------
# Additional precedent_analogy patterns: conversational historical parallels.
# Financial and opinion articles often use informal constructions like
# "We saw something similar in [year]" or "this is not the first time"
# rather than the literary constructions already covered above.
#
# Identified in Barchart "Meta Shows Urgency" (Jun 30, 2026):
#   "We saw something similar in 2022 when massive metaverse losses..."
# ---------------------------------------------------------------------------
_PRECEDENT_ANALOGY_PATTERNS.extend([
    # "We/[Subject] saw something similar in [year/period]"
    re.compile(
        r"\b(?:we|they|investors?|markets?|analysts?|observers?|critics?)\s+"
        r"(?:saw|see|have seen|had seen)\s+(?:something|this|a pattern)\s+"
        r"(?:similar|like this|before)\b.{3,120}",
        re.IGNORECASE,
    ),
    # "we've/we have seen this before" / "this is not the first time"
    re.compile(
        r"\b(?:we'?ve\s+seen\s+this\s+before|"
        r"this\s+is\s+(?:not|hardly|far\s+from)\s+the\s+first\s+time|"
        r"history\s+(?:repeating|repeated|repeats)|"
        r"(?:it'?s|this\s+is)\s+(?:a\s+)?déjà\s+vu|"
        r"(?:another|yet\s+another|a\s+repeat\s+of\s+the)\s+\d{4})\b.{0,80}",
        re.IGNORECASE,
    ),
    # "what followed was" / "what came next was" — narrative setup framing
    # that imports the outcome of a past cycle as predictive template
    re.compile(
        r"\bwhat\s+followed\s+was\b.{3,100}",
        re.IGNORECASE,
    ),
])


# ---------------------------------------------------------------------------
# Scale/magnitude framing: editorial device that deploys large raw numbers,
# calculated maximums, or scale analogies to create impressions of excess,
# danger, or harm.  Individual numbers are facts; the framing occurs when
# they are amplified via contextual techniques:
#   1. Calculated maximums: "fines of up to 6%... about $12 billion"
#   2. Cumulative totals: "$70 billion in losses since 2020"
#   3. Scale analogies: "enough to power 750,000 homes"
#   4. Comparison amplifiers: "a 76% spike," "more than double"
#   5. Victim/case roster: "2,000 lawsuits," "1,300 school districts"
# Distinct from loaded_language because the emotional charge comes from
# the number itself, not from adjectives or pejorative vocabulary.
# ---------------------------------------------------------------------------
_SCALE_MAGNITUDE_PATTERNS: list[re.Pattern] = [
    # "up to X%" or "as much as X%" of revenue/turnover/sales — calculated
    # maximum penalty/fine projections
    re.compile(
        r"\b(?:up to|as much as|as high as)\s+"
        r"(?:\$?\d[\d,.]*\s*(?:billion|million|trillion|[BMT])\b|"
        r"\d+(?:\.\d+)?%\s*(?:of|in)\s+"
        r"(?:\w+\s+)?"  # optional possessive pronoun ("their", "its")
        r"(?:global|annual|worldwide|total)?\s*"
        r"(?:(?:global|annual|worldwide|total)\s+)?"  # allow "global annual"
        r"(?:revenue|turnover|sales|income))",
        re.IGNORECASE,
    ),
    # "that would mean a fine/penalty of ~$X" — spelled-out dollar impact
    re.compile(
        r"\b(?:that (?:would|could) mean|meaning|amounting to|"
        r"which (?:would|could) (?:total|reach|amount to|mean))\s+"
        r"(?:a )?(?:potential |possible |estimated )?"
        r"(?:fine|penalty|cost|loss|bill|payout|damages?)\s+"
        r"(?:of\s+)?(?:about |roughly |approximately |nearly |~)?"
        r"\$?\d[\d,.]*\s*(?:billion|million|trillion|[BMT])\b",
        re.IGNORECASE,
    ),
    # Scale analogies: "enough to power/run/supply X homes/cities/countries"
    re.compile(
        r"\b(?:enough to|sufficient to|capable of)\s+"
        r"(?:roughly |about |approximately |nearly |more than )?"
        r"(?:power|run|supply|fuel|serve|feed|heat|cool)\s+"
        r"(?:roughly |about |approximately |nearly |more than )?"
        r"[\d,.]+\s*(?:thousand |million )?"
        r"(?:[\w.]+\s+)?"  # optional qualifier ("U.S.", "American", "British")
        r"(?:homes?|households?|cities|countries|"
        r"(?:small|medium|large)[\s-]+(?:sized? )?(?:cit(?:y|ies)|countr(?:y|ies)|town|state))",
        re.IGNORECASE,
    ),
    # "as much as a small country/city" without specific number
    re.compile(
        r"\b(?:as much (?:electricity|energy|power|water) as)\s+"
        r"(?:a\s+)?(?:small|medium|large)[\s-]+"
        r"(?:sized? )?(?:city|country|town|state|nation)",
        re.IGNORECASE,
    ),
    # Cumulative loss/spending totals: "$X billion in losses/spending since YYYY"
    re.compile(
        r"\$\d[\d,.]*\s*(?:billion|million|trillion|[BMT])\s+"
        r"(?:in\s+)(?:cumulative |combined |total |aggregate )?"
        r"(?:losses?|spending|expenditure|investment|costs?|damages?|fines?|penalties)"
        r"(?:\s+since\s+\d{4}|\s+over\s+(?:the\s+)?(?:past|last|previous)\s+\d+\s+"
        r"(?:years?|months?|quarters?|decades?))?",
        re.IGNORECASE,
    ),
    # Victim/case roster: "X,000+ lawsuits/cases/complaints/claims"
    re.compile(
        r"\b(?:more than|over|nearly|approximately|at least|roughly|about)\s+"
        r"[\d,]+\s+"
        r"(?:lawsuits?|cases?|complaints?|claims?|families|school districts?"
        r"|plaintiffs?|victims?|students?|children|parents?|users?)",
        re.IGNORECASE,
    ),
    # Comparison amplifiers: "more than double/triple" or "X% spike/surge/jump"
    re.compile(
        r"\b(?:more than (?:double|triple|quadruple)|"
        r"\d+(?:\.\d+)?%\s+(?:spike|surge|jump|increase|rise|hike|growth))",
        re.IGNORECASE,
    ),
    # Market-size growth projections: "$X billion market", "expected to
    # triple/double/grow to $X by YYYY".  Scale implied through projected
    # magnitude to frame an industry as unstoppable or rapidly expanding.
    re.compile(
        r"\b(?:market|industry|sector|category)\s+"
        r"(?:is\s+)?(?:expected|projected|forecast|estimated|set|poised)\s+to\s+"
        r"(?:reach|grow\s+to|hit|top|surpass|exceed|triple|double|quadruple)\b",
        re.IGNORECASE,
    ),
    # Reverse: "expected to triple/double to $X" without explicit market word
    re.compile(
        r"\b(?:expected|projected|forecast|estimated|poised|set)\s+to\s+"
        r"(?:triple|double|quadruple|grow\s+(?:\d+[xX]|\d+.?fold))\s+"
        r"(?:by\s+\d{4}\s*,?\s*)?(?:to\s+)?"
        r"\$?\d[\d,.]*\s*(?:billion|million|trillion|[BMT])\b",
        re.IGNORECASE,
    ),
    # Vague large-scale amounts: "hundreds of millions", "tens of billions"
    re.compile(
        r"\b(?:hundreds|tens|dozens)\s+of\s+"
        r"(?:billions?|millions?|thousands?)\s+"
        r"(?:of\s+)?(?:dollars?|euros?|pounds?|yen)?",
        re.IGNORECASE,
    ),
    # "more than N [institutional entities]" — not victims/plaintiffs but
    # institutional actors (insurers, companies, agencies, firms)
    re.compile(
        r"\b(?:more than|over|nearly|at least)\s+"
        r"[\d,]+\s+"
        r"(?:insurers?|companies|corporations?|firms?|agencies|banks?|"
        r"underwriters?|carriers?|investors?|institutions?|organizations?)",
        re.IGNORECASE,
    ),
    # Standalone large dollar amounts — "$X billion/million" in contexts
    # that frame institutional decisions (development, investment, spending,
    # cuts) as enormous in scale.  Requires proximity to an action verb
    # to avoid matching factual financial reporting where the number is
    # the news itself (e.g., earnings reports).
    # Discovered via MIT TR "Resistance" article (Apr 2026):
    # "activists stalled $98 billion in data center development"
    re.compile(
        r"\b(?:stalled|blocked|halted|froze|frozen|delayed|scrapped|"
        r"cancelled|canceled|killed|shelved|suspended|paused)\s+"
        r"(?:more\s+than\s+|over\s+|nearly\s+|about\s+|approximately\s+)?"
        r"\$\d[\d,.]*\s*(?:billion|million|trillion|[BMT])\b",
        re.IGNORECASE,
    ),
    # Percentage-based workforce impact: "X% of its/the/their staff/workforce"
    re.compile(
        r"\b(?:lay\s+off|laid\s+off|cut|cutting|slashing|eliminating|axing)\s+"
        r"(?:up\s+to\s+|about\s+|roughly\s+|approximately\s+|nearly\s+|more\s+than\s+)?"
        r"\d+(?:\.\d+)?%\s+of\s+(?:its|the|their|his|her)\s+"
        r"(?:staff|workforce|employees?|workers?|headcount|personnel)",
        re.IGNORECASE,
    ),
    # ---------------------------------------------------------------------------
    # Operational-scale enumeration: "more than 45,000 prompts/tests/queries"
    # Extends the victim/case roster concept to testing, data, and operational
    # nouns used in tech/AI/corporate reporting.  Discovered via WIRED "Cannes"
    # article (Jul 2026): "more than 45,000 prompts run through the rival
    # chatbots" was undetected because "prompts" wasn't in the victim roster.
    # ---------------------------------------------------------------------------
    re.compile(
        r"\b(?:more than|over|nearly|approximately|at least|roughly|about)\s+"
        r"[\d,]+\s+"
        r"(?:prompts?|tests?|queries?|requests?|profiles?|accounts?"
        r"|messages?|interactions?|samples?|inputs?|submissions?"
        r"|records?|entries|transactions?|reports?|incidents?"
        r"|violations?|emails?|documents?|images?|videos?"
        r"|reviews?|responses?|searches?|attempts?)",
        re.IGNORECASE,
    ),
    # ---------------------------------------------------------------------------
    # Bare large-count enumeration: "3,748 prompts" — comma-formatted numbers
    # (≥1,000) paired with operational/impact nouns signal deliberate scale
    # emphasis.  The comma formatting itself is an editorial choice to render
    # the number readable and impressive.  Discovered via WIRED "Cannes"
    # article (Jul 2026): "a spreadsheet of 3,748 prompts" was undetected.
    # ---------------------------------------------------------------------------
    re.compile(
        r"\b\d{1,3}(?:,\d{3})+\+?\s+"
        r"(?:prompts?|tests?|queries?|requests?|profiles?|accounts?"
        r"|messages?|interactions?|samples?|inputs?|submissions?"
        r"|lawsuits?|cases?|complaints?|claims?|records?|entries"
        r"|transactions?|reports?|incidents?|violations?"
        r"|emails?|documents?|images?|videos?"
        r"|plaintiffs?|victims?|families|users?"
        r"|reviews?|responses?|searches?|attempts?)",
        re.IGNORECASE,
    ),
    # ---------------------------------------------------------------------------
    # Minimum-floor enumeration with verb: "at least 239 involved sex"
    # Captures "at least / no fewer than N [verb]" constructions where the
    # author establishes a floor magnitude followed by a categorizing verb.
    # Discovered via WIRED "Cannes" article (Jul 2026): "At least 239
    # involved sex or romance" was undetected — the existing roster patterns
    # require a noun after the number, not a verb.
    # ---------------------------------------------------------------------------
    re.compile(
        r"\b(?:at least|no fewer than|a minimum of)\s+"
        r"[\d,]+\s+"
        r"(?:involved|focused|related|dealt|concerned|addressed"
        r"|contained|included|featured|covered|discussed"
        r"|mentioned|referenced|targeted|affected|impacted)",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["scale_magnitude"] = _SCALE_MAGNITUDE_PATTERNS


# ---------------------------------------------------------------------------
# Corporate reassurance undercut: editorial device where a corporate PR
# statement expressing safety, care, or responsible design is immediately
# followed by adversarial conjunction ("but," "however," "yet," "despite,"
# "while") and contradicting evidence.  The juxtaposition creates a
# "said one thing, reality shows another" reading that undermines the
# corporate claim without the journalist explicitly editorializing.
#
# Example from Wired MCI coverage (2026-06-22):
#   "We have carefully designed this program with privacy safeguards"
#   → "and while we have no indication..."
#   → next paragraph: "the data... was accessible to all Meta staffers"
#
# Example from Reuters MCI coverage:
#   "There are safeguards in place to protect sensitive content"
#   → "In the weeks since its launch, however, Meta employees have
#   complained that MCI was consuming so much data..."
#
# Distinct from loaded_language (which uses pejorative vocabulary) and
# ironic_quotation (which uses scare quotes).  This device is structural:
# the journalist deploys the corporate statement AS the setup for its
# contradiction, creating irony through sequence rather than vocabulary.
# ---------------------------------------------------------------------------
_CORPORATE_REASSURANCE_UNDERCUT_PATTERNS: list[re.Pattern] = [
    # "carefully designed/built/crafted" near "but/however/yet/while/despite"
    re.compile(
        r"\b(?:carefully|thoughtfully|responsibly|diligently)\s+"
        r"(?:designed|built|crafted|developed|implemented|considered|"
        r"constructed|engineered|created)\b"
        r".{0,200}?"
        r"\b(?:but|however|yet|despite|while|nevertheless|nonetheless|"
        r"even so|still|in fact|in reality)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "privacy/safety safeguards/protections" near contradiction
    re.compile(
        r"\b(?:privacy|safety|security|data)\s+"
        r"(?:safeguards?|protections?|controls?|measures?|guardrails?|"
        r"protocols?|standards?|policies)\b"
        r".{0,200}?"
        r"\b(?:but|however|yet|despite|while|nevertheless|nonetheless|"
        r"even so|still|in fact|in reality)\b"
        r".{0,120}?"
        r"\b(?:expos(?:ed|ure|ing)|accessible|leaked?|breach(?:ed)?|"
        r"fail(?:ed|ure|ing)|broke|compromis(?:ed|ing)|"
        r"vulnerab(?:le|ility)|inadequat(?:e|ely)|"
        r"complain(?:ed|ing|ts?)|concern(?:s|ed)?)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "no indication of improper/unauthorized" near contradicting context
    re.compile(
        r"\bno (?:indication|evidence|sign)\s+"
        r"(?:at this time\s+)?(?:that|of)\s+"
        r"(?:any )?(?:data was |information was )?"
        r"(?:improperly|unauthorized|inappropriately|illegally)\b"
        r".{0,200}?"
        r"\b(?:but|however|yet|despite|while|nevertheless|nonetheless|"
        r"even so|still|in fact|in reality)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "committed to / takes X seriously" near contradiction
    re.compile(
        r"\b(?:committed to|takes?\s+(?:\w+\s+)?seriously|"
        r"invested heavily in|prioritiz(?:es?|ing)|"
        r"deeply committed|strongly committed)\b"
        r".{0,200}?"
        r"\b(?:but|however|yet|despite|while|nevertheless|nonetheless|"
        r"even so|still|in fact|in reality)\b"
        r".{0,120}?"
        r"\b(?:fail(?:ed|ure|ing)|breach(?:ed)?|"
        r"expos(?:ed|ure|ing)|inadequat(?:e|ely)|"
        r"complain(?:ed|ing|ts?)|concern(?:s|ed)?|"
        r"fell short|shortcoming|deficien(?:t|cy|cies))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Corporate "not the primary objective/focus" near evidence of exactly that
    re.compile(
        r"\b(?:not (?:the |its )?(?:primary|main|intended|core) "
        r"(?:objective|focus|purpose|goal|aim))\b"
        r".{0,200}?"
        r"\b(?:but|however|yet|despite|while|nevertheless)\b",
        re.IGNORECASE | re.DOTALL,
    ),
]

_DEVICE_PATTERNS["corporate_reassurance_undercut"] = (
    _CORPORATE_REASSURANCE_UNDERCUT_PATTERNS
)


# ---------------------------------------------------------------------------
# Sarcastic correction: editorial device where the writer states something
# obviously false or absurd as if reporting it straight, then immediately
# corrects themselves — creating a rhetorical whiplash that editorialises
# without explicitly stating an opinion.  Very common in tech journalism
# (Engadget, Wired, The Verge, Guardian tech desk).
#
# Examples:
#   "Of course, when Careless People was published, it instantly caused the
#    company to go out of business... oh hang on, wait, no."
#   "Naturally, this led to sweeping reforms. Just kidding."
#   "I'm sure this will be fine. (Spoiler: it was not fine.)"
#
# Distinct from ironic_quotation (which undercuts someone else's quoted
# words) — sarcastic_correction is the writer's OWN voice deploying mock
# sincerity followed by a correction that reveals the absurdity.
# ---------------------------------------------------------------------------
_SARCASTIC_CORRECTION_PATTERNS: list[re.Pattern] = [
    # "Of course, [absurd claim]... oh hang on / wait / oh wait / wait, no"
    re.compile(
        r"\b(?:of course|naturally|unsurprisingly|predictably|"
        r"surely|obviously|no doubt),?\s+"
        r".{10,200}?"
        r"(?:\.\.\.|…)\s*"
        r"(?:oh\s+)?(?:hang on|wait|hold on|actually|except|but|"
        r"no|nope|scratch that)",
        re.IGNORECASE | re.DOTALL,
    ),
    # "[Statement]. Just kidding." / "...kidding." / "Not really."
    re.compile(
        r"(?:\.|\!)\s+"
        r"(?:Just kidding|Kidding|Not really|Not exactly|"
        r"Except (?:it|that|this|they) (?:didn.?t|wasn.?t|aren.?t|isn.?t|won.?t)|"
        r"Spoiler(?:\s*:\s*|\s+)(?:it|that|this|they) (?:didn.?t|wasn.?t|won.?t|isn.?t|weren.?t)|"
        r"(?:That|This) (?:did|has|was)(?:n.?t)?\s+(?:not\s+)?happen(?:ed)?|"
        r"None of (?:that|this|which) (?:happened|is true|occurred|materialised|materialized))",
        re.IGNORECASE,
    ),
    # "...right? Wrong." / "...right? Nope." / "...correct? Not quite."
    re.compile(
        r"\bright\?\s*(?:Wrong|Nope|Not (?:quite|exactly|really|so fast))\b",
        re.IGNORECASE,
    ),
    # "(Narrator: it did not.)" / "[Narrator: they did not.]" — TV-trope
    # sarcasm style used in online-native journalism
    re.compile(
        r"[\(\[]\s*(?:Narrator|Spoiler|Reader)[\s:]+.{5,80}?[\)\]]",
        re.IGNORECASE,
    ),
    # "Color me surprised" / "Colour me shocked" / "Who could have predicted"
    # — standalone sarcastic phrases
    re.compile(
        r"\b(?:colou?r me (?:surprised|shocked|stunned)|"
        r"who could (?:have )?(?:predicted|foreseen|guessed|imagined|seen that coming)|"
        r"shocking(?:ly)?,? I know|"
        r"what a (?:surprise|shock|concept)|"
        r"I.?m sure (?:this|that|it) will (?:be|go|work out|end well|turn out) (?:just )?fine)\b",
        re.IGNORECASE,
    ),
    # "And everyone lived happily ever after" / "problem solved" —
    # fairy-tale or finality sarcasm after describing an ongoing problem
    re.compile(
        r"\b(?:and (?:they all |everyone )?lived happily ever after|"
        r"problem solved|crisis averted|nothing to see here|"
        r"move along|all is well|everything is fine|"
        r"what could (?:possibly )?go wrong)\b",
        re.IGNORECASE,
    ),
    # ---------------------------------------------------------------------------
    # Ironic denial / mock-certainty: writer deploys exaggerated certainty
    # or denials that clearly mean the opposite.  The technique relies on
    # context making the literal reading absurd, so the reader infers sarcasm.
    #
    # Identified as a gap in AV Club Meta Arena analysis (Jun 27, 2026):
    #   - "presumably has absolutely nothing to do with" — ironic denial
    #   - "who we're sure are just thrilled" — mock-certainty/sympathy
    #   - "You know, like how humans talk!" — post-quote sarcastic deflation
    # ---------------------------------------------------------------------------
    # "presumably / surely / undoubtedly + nothing to do with / no connection"
    re.compile(
        r"\b(?:presumably|surely|undoubtedly|certainly|"
        r"obviously|of course|clearly|naturally)\s+"
        r"(?:has\s+)?(?:absolutely\s+)?(?:nothing\s+to\s+do\s+with|"
        r"no\s+(?:connection|relation|link|bearing)\s+(?:to|on|with)|"
        r"(?:(?:is|are)\s+)?(?:entirely|completely|totally)\s+(?:unrelated|coincidental))\b",
        re.IGNORECASE,
    ),
    # "we're sure / I'm sure + [positive claim]" — mock-certainty about
    # something the reader knows is false or ironic
    re.compile(
        r"\b(?:we.re|I.m|they.re|he.s|she.s)\s+sure\s+"
        r"(?:(?:that\s+)?(?:they|he|she|it|the|this|everyone)\s+)?"
        r"(?:(?:are|is|will be|would be)\s+)?(?:just\s+)?(?:thrilled|delighted|"
        r"overjoyed|ecstatic|happy|pleased|fine|great|wonderful)\b",
        re.IGNORECASE,
    ),
    # "You know, like how [X]" — post-quote sarcastic aside, deflating
    # the preceding quoted material by comparing to absurd normal
    re.compile(
        r"\b(?:You know,?\s+like how|"
        r"You know,?\s+the way|"
        r"Like (?:you|one|we) (?:do|does?)|"
        r"As (?:one|you) (?:does?|do))\b",
        re.IGNORECASE,
    ),
    # "a fact that presumably / which presumably / which surely"
    re.compile(
        r"\ba fact (?:that|which)\s+(?:presumably|surely|undoubtedly|"
        r"obviously|certainly|clearly)\b",
        re.IGNORECASE,
    ),
    # ---------------------------------------------------------------------------
    # Standalone sarcastic exclamation: a one-word or very short sentence
    # used as sardonic editorial commentary, often echoing political/meme
    # rhetoric.  "Sad!" (Trumpian), "Shocking.", "Brilliant.", "Sure."
    # These are standalone sentences — not part of a correction structure
    # but pure sarcastic interjection.
    #
    # Discovered via Gizmodo Meta/Google AI tokens article (Jun 29, 2026):
    #   "In other words, Meta replaced tokenmaxxing with judicious
    #    token-counting. Sad!"
    # The "Sad!" is unmistakably sarcastic but matched no existing pattern
    # because there is no correction, denial, or "(Narrator:)" structure.
    # ---------------------------------------------------------------------------
    re.compile(
        r"(?:^|(?<=\.\s)|(?<=!\s)|(?<=\?\s))"
        r"(?:Sad|Shocking|Brilliant|Sure|Right|Great|Neat|"
        r"Yikes|Oops|Cute|Classy|Cool|Nice|Lovely|Wonderful|"
        r"Charming|Delightful|Terrific|Incredible|Amazing|Bravo|"
        r"Genius|Bold|Fun|Wild)"
        r"[.!]"
        r"(?:\s|$)",
        re.MULTILINE,
    ),
]

_DEVICE_PATTERNS["sarcastic_correction"] = _SARCASTIC_CORRECTION_PATTERNS


# ---------------------------------------------------------------------------
# Outsourced intensity: editorial technique where the journalist maintains
# a measured, neutral voice while deploying legal filings, complaints,
# whistleblower reports, or direct quotes to carry the article's emotional
# and characterizational weight.  The writer never calls the company
# "coercive" or its behavior "blatant" — the complaint does.  This creates
# plausible editorial neutrality while ensuring the reader absorbs
# maximally negative language.  The technique is structurally distinct from
# loaded_language (where the journalist's own voice is loaded) and from
# anonymous_authority (where unnamed sources provide claims, not emotional
# intensity).
#
# Identified as a gap in Guardian Wynn-Williams analysis (Jun 25, 2026):
#   - "blatant violation of the first amendment" — complaint language
#   - "coercive surveillance" — complaint language
#   - "improper and unlawful" — complaint language
#   The journalist's own prose is neutral: "files complaint", "argues that",
#   "accuses the company of".  All emotional charge is outsourced.
# ---------------------------------------------------------------------------
_OUTSOURCED_INTENSITY_PATTERNS: list[re.Pattern] = [
    # "the complaint/filing/lawsuit alleges/states [loaded language]"
    re.compile(
        r"\b(?:the\s+)?(?:complaint|filing|lawsuit|petition|motion|brief|"
        r"affidavit|declaration|deposition|testimony|"
        r"whistleblower\s+(?:complaint|report))\s+"
        r"(?:also\s+)?(?:alleges?|states?|claims?|asserts?|contends?|"
        r"charges?|describes?|details?|accuses?|argues?)\b"
        r".{0,150}?"
        r"\b(?:blatant|egregious|flagrant|willful|deliberate|systematic|"
        r"coercive|retaliatory|unlawful|improper|outrageous|unconscionable|"
        r"malicious|reckless|brazen|predatory|abusive|corrupt|"
        r"fraudulent|deceptive|oppressive|threatening|intimidating)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "according to the complaint/filing" + loaded language
    re.compile(
        r"\baccording to (?:the\s+)?(?:complaint|filing|lawsuit|petition|"
        r"motion|brief|affidavit|declaration|testimony|"
        r"whistleblower\s+(?:complaint|report)|"
        r"court\s+(?:documents?|records?|filings?))\b"
        r".{0,150}?"
        r"\b(?:blatant|egregious|flagrant|willful|deliberate|systematic|"
        r"coercive|retaliatory|unlawful|improper|outrageous|unconscionable|"
        r"malicious|reckless|brazen|predatory|abusive|corrupt|"
        r"fraudulent|deceptive|oppressive|threatening|intimidating|"
        r"silenced?|censorship|violation)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Quoted loaded characterization in legal/complaint context
    # Pattern: quote containing high-intensity legal language, attributed
    # to a complaint/filing rather than editorial voice
    re.compile(
        r'["\u201c]'
        r'(?:[^"\u201d]{0,50}?)'
        r'\b(?:blatant|egregious|flagrant|coercive|retaliatory|unlawful|'
        r'improper|outrageous|unconscionable|malicious|reckless|brazen|'
        r'predatory|abusive|corrupt|fraudulent|deceptive|oppressive|'
        r'intimidating|violation|silencing|censorship|surveillance)\b'
        r'(?:[^"\u201d]{0,80}?)'
        r'["\u201d]',
        re.IGNORECASE | re.DOTALL,
    ),
    # "she/he alleges [entity] [loaded verb/characterization]"
    # Individual whistleblower/plaintiff allegations carrying intensity
    re.compile(
        r"\b(?:she|he|they|the plaintiff|the complainant|"
        r"the whistleblower|the former employee)\s+"
        r"(?:also\s+)?(?:alleges?|claims?|asserts?|contends?|charges?|accuses?)\b"
        r".{0,120}?"
        r"\b(?:coercive|retaliatory|unlawful|improper|"
        r"malicious|reckless|deliberate|systematic|"
        r"intimidating|threatening|discriminatory|"
        r"fraudulent|deceptive|oppressive|"
        r"silenced?|censorship|surveillance|retaliation)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "in the complaint/filing, [entity] is described/characterized as"
    re.compile(
        r"\bin (?:the|her|his|their)\s+(?:complaint|filing|lawsuit|petition|"
        r"testimony|statement|affidavit)\b"
        r".{0,120}?"
        r"\b(?:described|characterized|portrayed|depicted|framed|cast|labelled|labeled)\b"
        r".{0,40}?"
        r"\b(?:coercive|retaliatory|unlawful|improper|abusive|"
        r"predatory|oppressive|hostile|toxic)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # --- Expert-outsourced editorial judgment patterns ---
    # Expert quotes carrying loaded characterizations or strong negative
    # evaluations that the journalist does not state editorially.  This
    # captures a subtler form of outsourced intensity: academic/industry
    # experts serve as the vehicle for criticism the publication endorses
    # structurally (through source selection) without owning editorially.
    #
    # Key structural patterns in real articles:
    #   A) "[loaded quote]" says/said X, a professor at University
    #   B) X, a professor at University, says/said "[loaded quote]"
    #   C) X says/said ... "[loaded quote]" (credential mentioned earlier)

    # Pattern A: loaded quote followed by expert attribution
    # "[...loaded word...]" says/said X, a professor/researcher/analyst
    re.compile(
        r'["\u201c]'
        r"(?:[^\"\u201d]{0,200}?)"
        r"\b(?:surprising|shocked|alarming|disturbing|troubling|"
        r"striking|embarrassing|negligent|reckless|dangerous|"
        r"unconscionable|egregious|inexcusable|incompetent|"
        r"mindless|careless|sloppy|baffling|inexplicable|"
        r"staggering|appalling)\b"
        r"(?:[^\"\u201d]{0,80}?)"
        r'["\u201d]'
        r".{0,60}?"
        r"\b(?:says?|said|warned|cautioned|argued|noted)\b"
        r".{0,60}?"
        r"\b(?:professor|researcher|analyst|expert|scholar|"
        r"fellow|scientist|director|specialist)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Pattern B: expert credential then says then loaded quote
    re.compile(
        r"\b(?:professor|researcher|analyst|expert|scholar|"
        r"fellow|scientist|director|specialist)\b"
        r".{0,80}?"
        r"\b(?:says?|said|told|warned|cautioned|argued)\b"
        r".{0,40}?"
        r'["\u201c]'
        r"(?:[^\"\u201d]{0,200}?)"
        r"\b(?:surprising|shocked|alarming|disturbing|troubling|"
        r"striking|embarrassing|negligent|reckless|dangerous|"
        r"unconscionable|egregious|inexcusable|incompetent|"
        r"mindless|careless|sloppy|baffling|inexplicable|"
        r"staggering|appalling)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Expert agrees + loaded question / alarm (handles "analyst ... agrees. '...'")
    re.compile(
        r"\b(?:senior\s+)?(?:research\s+)?(?:professor|researcher|analyst|"
        r"expert|scholar|fellow|scientist|director|specialist)\b"
        r".{0,100}?"
        r"\b(?:agrees?|concurs?|echoes?|adds?)\b"
        r".{0,10}?"
        r'["\u201c]'
        r"(?:[^\"\u201d]{0,200}?)"
        r"(?:\?|surprising|striking|alarming|troubling|dangerous)",
        re.IGNORECASE | re.DOTALL,
    ),
    # Expert quote with alarm phrase (standalone — no trailing attribution
    # needed since the credential may have been established earlier)
    re.compile(
        r'["\u201c]'
        r"(?:[^\"\u201d]{0,200}?)"
        r"\b(?:very dangerous|extremely dangerous|deeply troubling|"
        r"deeply alarming|profoundly disturbing|a serious problem|"
        r"a major concern|a real threat)\b"
        r"(?:[^\"\u201d]{0,40}?)"
        r'["\u201d]',
        re.IGNORECASE | re.DOTALL,
    ),
    # --- Labor-law expert outsourced judgment patterns ---
    # Expert quotes carrying cynicism, systemic critique, or strong
    # negative evaluations of labor/employment conditions.  The journalist
    # uses a credentialed source (professor, labor expert, legal scholar)
    # as the vehicle for structural criticism the publication endorses
    # through source selection without owning editorially.
    #
    # Identified in WebProNews Meta Dublin contractors article (May 2026):
    #   "Call me cynical, but I don't believe much in morals when it
    #    comes to labor rights." (Michael Doherty, Maynooth University)
    #   "It's pretty much open season." (same)
    #
    # Pattern: expert credential near quote containing labor-specific
    # loaded language (open season, cynical, rigged, stacked, toothless,
    # worthless, powerless, etc.)

    # Expert credential (professor, researcher, labor law) near loaded quote
    re.compile(
        r"\b(?:professor|researcher|analyst|scholar|fellow|"
        r"expert|specialist|director|lecturer|academic)\b"
        r".{0,120}?"
        r'["\u201c]'
        r'(?:[^"\u201d]{0,250}?)'
        r"\b(?:open season|cynical|rigged|stacked|toothless|"
        r"worthless|powerless|farce|sham|fiction|laughable|"
        r"utter inability|utterly|impotent|useless|meaningless|"
        r"race to the bottom|a joke|pretence|pretense|"
        r"no real (?:obligation|power|leverage|teeth|recourse)|"
        r"effective(?:ly)? (?:veto|nothing|zero|powerless|useless))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Reverse: loaded quote then expert attribution
    re.compile(
        r'["\u201c]'
        r'(?:[^"\u201d]{0,250}?)'
        r"\b(?:open season|cynical|rigged|stacked|toothless|"
        r"worthless|powerless|farce|sham|fiction|laughable|"
        r"utter inability|utterly|impotent|useless|meaningless|"
        r"race to the bottom|a joke|pretence|pretense|"
        r"no real (?:obligation|power|leverage|teeth|recourse)|"
        r"effective(?:ly)? (?:veto|nothing|zero|powerless|useless))\b"
        r'(?:[^"\u201d]{0,80}?)'
        r'["\u201d]'
        r".{0,80}?"
        r"\b(?:professor|researcher|analyst|scholar|fellow|"
        r"expert|specialist|director|lecturer|academic|"
        r"labou?r (?:law |rights? )?(?:professor|expert|scholar|specialist))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # --- Document-catalog outsourced intensity patterns ---
    # Journalist presents a catalog of specific, disturbing evidence from
    # reviewed documents (spreadsheets, internal data, logs) and lets the
    # enumerated content carry emotional weight without editorial commentary.
    # Distinct from legal-filing outsourcing: here the journalist IS the one
    # presenting the evidence, but the evidence's specificity does the work.
    #
    # Identified in Wired Meta "Cannes" contractors article (Jul 2026):
    #   "a 13-year-old who said she had become pregnant by her adult neighbor"
    #   "whether it would be nice to eat my neighbor's child"
    #   "a French-language prompt about Jamey Rodemeyer's death"
    # The journalist reports spreadsheet contents verbatim; the horror comes
    # from the specifics, not from editorial adjectives.

    # Pattern: reviewed/obtained documents + enumeration of disturbing specifics
    # "reviewed by [Publication]" / "obtained by" / "internal [documents]"
    # followed by age-specific scenario descriptions within ~500 chars
    re.compile(
        r"\b(?:reviewed by|obtained by|seen by|viewed by|"
        r"internal (?:documents?|spreadsheets?|data|records?|logs?|emails?|memos?))\b"
        r".{0,500}?"
        r"\b(?:\d{1,2}.year.old|"
        r"(?:posed?|posing|pretending|impersonating)\s+as\s+"
        r"(?:a\s+)?(?:teen|minor|child|adolescent|(?:\d{1,2}.year.old))|"
        r"(?:suicide|self.harm|sexual|sexually|rape|abuse|"
        r"pregnant|pregnancy|drugs?|overdose|eating disorder|"
        r"cannibalism|bestiality|incest|pedophil))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Reverse: disturbing content cluster followed by document attribution
    re.compile(
        r"\b(?:suicide|self.harm|sexual abuse|sexual exploitation|"
        r"child (?:abuse|exploitation|pornography)|"
        r"eating disorder|overdose|self.injury)\b"
        r".{0,300}?"
        r"\b(?:according to (?:the )?(?:documents?|spreadsheets?|data|"
        r"records?|logs?|internal)|"
        r"(?:the )?(?:documents?|spreadsheets?|data|records?|logs?) "
        r"(?:show|reveal|indicate|contain|include|detail|list))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Prompt/scenario enumeration with age markers — journalist describing
    # test prompts, scenarios, or cases from data that involve minors
    re.compile(
        r"\b(?:prompts?|scenarios?|test cases?|examples?|entries?|rows?)\b"
        r".{0,200}?"
        r"\b(?:\d{1,2}.year.old|"
        r"under.?(?:13|16|18)|"
        r"(?:posed?|posing) as (?:a )?(?:teen|minor|child))\b"
        r".{0,200}?"
        r"\b(?:suicide|self.harm|sex(?:ual)?|drugs?|abuse|"
        r"violence|death|kill|rape|assault|"
        r"eating disorder|overdose|pregnant)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Dense disturbing-content enumeration — 3+ disturbing terms within
    # a ~400-char span, indicating a catalog of horrors. The journalist
    # achieves intensity through sheer accumulation of specific evidence
    # rather than editorial language.
    re.compile(
        r"\b(?:suicide|self.harm|sex(?:ual)?(?:\s+(?:abuse|exploitation|content))?|"
        r"drugs?|cocaine|heroin|fentanyl|meth|"
        r"eating disorder|anorexia|bulimia|"
        r"rape|assault|violence|abuse|"
        r"pregnant|pregnancy|cannibalism|bestiality|incest|"
        r"pedophil|pornograph|death|kill(?:ing)?|"
        r"racial slur|slur)\b"
        r".{0,200}?"
        r"\b(?:suicide|self.harm|sex(?:ual)?(?:\s+(?:abuse|exploitation|content))?|"
        r"drugs?|cocaine|heroin|fentanyl|meth|"
        r"eating disorder|anorexia|bulimia|"
        r"rape|assault|violence|abuse|"
        r"pregnant|pregnancy|cannibalism|bestiality|incest|"
        r"pedophil|pornograph|death|kill(?:ing)?|"
        r"racial slur|slur)\b"
        r".{0,200}?"
        r"\b(?:suicide|self.harm|sex(?:ual)?(?:\s+(?:abuse|exploitation|content))?|"
        r"drugs?|cocaine|heroin|fentanyl|meth|"
        r"eating disorder|anorexia|bulimia|"
        r"rape|assault|violence|abuse|"
        r"pregnant|pregnancy|cannibalism|bestiality|incest|"
        r"pedophil|pornograph|death|kill(?:ing)?|"
        r"racial slur|slur)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # --- Law enforcement / investigator outsourced intensity patterns ---
    # Journalist uses law enforcement officers, agents, investigators, or
    # task-force members as the vehicle for emotional/damning criticism.
    # The reporter's own prose stays neutral ("officers said," "testified")
    # while the quoted officials carry the loaded language.
    #
    # Identified in Guardian/Decrypt Meta AI CSAM "junk" tips article (Jun 2026):
    #   "We get a lot of tips from Meta that are just kind of junk"
    #     — Benjamin Zwiebel, ICAC special agent, testified at trial
    #   "It is killing morale. We are drowning in tips"
    #     — anonymous ICAC officer
    #   "It's pretty overwhelming because we're getting so many reports,
    #    but the quality of the reports is really lacking"
    #     — anonymous ICAC officer
    # The journalist never editorializes; all emotional intensity is
    # outsourced to credentialed law enforcement sources.

    # Pattern: officer/agent/investigator credential near loaded quote
    re.compile(
        r"\b(?:officer|agent|investigator|detective|sergeant|"
        r"lieutenant|captain|commander|inspector|deputy|"
        r"special agent|task\s*force|law enforcement)\b"
        r".{0,120}?"
        r'["\u201c]'
        r'(?:[^"\u201d]{0,250}?)'
        r"\b(?:junk|overwhelming|drowning|killing|flood(?:ing|ed)?|"
        r"buried|swamped|crushed|impossible|unsustainable|"
        r"useless|worthless|broken|failing|crippling|"
        r"nightmare|disaster|crisis|catastroph|unbearable|"
        r"morale|can't keep up|no way|not enough)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Reverse: loaded quote then officer/agent attribution
    re.compile(
        r'["\u201c]'
        r'(?:[^"\u201d]{0,250}?)'
        r"\b(?:junk|overwhelming|drowning|killing|flood(?:ing|ed)?|"
        r"buried|swamped|crushed|impossible|unsustainable|"
        r"useless|worthless|broken|failing|crippling|"
        r"nightmare|disaster|crisis|catastroph|unbearable|"
        r"morale|can't keep up|no way|not enough)\b"
        r'(?:[^"\u201d]{0,80}?)'
        r'["\u201d]'
        r".{0,80}?"
        r"\b(?:officer|agent|investigator|detective|"
        r"special agent|task\s*force|law enforcement|"
        r"testified|told the court|told the jury)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Testimony-outsourced: "testified" / "told [pub]" near loaded quote
    # (credential may not be adjacent — covers "X testified during the
    # state's trial" without requiring officer/agent in the same span)
    re.compile(
        r'["\u201c]'
        r'(?:[^"\u201d]{0,250}?)'
        r"\b(?:junk|overwhelming|drowning|killing|flood(?:ing|ed)?|"
        r"buried|swamped|crushed|impossible|unsustainable|"
        r"useless|worthless|broken|failing|crippling|"
        r"nightmare|disaster|catastroph|unbearable|"
        r"morale|can't keep up|no way|not enough)\b"
        r'(?:[^"\u201d]{0,80}?)'
        r'["\u201d]'
        r".{0,40}?"
        r"\b(?:testified|told (?:the )?(?:court|jury|tribunal|"
        r"committee|panel|hearing|commission|inquiry))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Policy advocate / advocacy org outsourced critique
    # e.g., JB Branch, Public Citizen: "these companies have laid off
    # content moderators and replaced them with AI"
    re.compile(
        r"\b(?:policy\s+advocate|advocacy|activist|campaigner|"
        r"watchdog|consumer\s+(?:advocate|group)|"
        r"Public Citizen|Common Sense Media|"
        r"policy\s+(?:analyst|director|advisor))\b"
        r".{0,120}?"
        r'["\u201c]'
        r'(?:[^"\u201d]{0,250}?)'
        r"\b(?:laid off|replaced|removed|gutted|eliminated|"
        r"cut(?:ting)?|slashed|dismantled|hollowed|"
        r"overabundance|false positive|broader net|"
        r"erring on the side|overwhelming|unsustainable)\b",
        re.IGNORECASE | re.DOTALL,
    ),
]

_DEVICE_PATTERNS["outsourced_intensity"] = _OUTSOURCED_INTENSITY_PATTERNS


# ---------------------------------------------------------------------------
# Kicker framing: editorial technique of ending an article on a discordant
# negative note — the last paragraph introduces a critical context (workforce
# turmoil, regulatory threat, ethical concern) that was NOT the article's
# main topic.  This ensures the reader's final impression is negative
# regardless of otherwise balanced or positive coverage.  Detected by
# checking the final ~300 characters for negative signals when the article
# body tone is neutral-to-positive.
# ---------------------------------------------------------------------------
_KICKER_NEGATIVE_SIGNALS: list[re.Pattern] = [
    re.compile(
        r"\b(?:turbulent|turmoil|at an all.time low|all.time low|"
        r"rock.?bottom|historically low|historically poor|"
        r"troubled|troubled times?|controversy|controversial|"
        r"under fire|under siege|scandal|crisis|investigation|"
        r"lawsuit|lawsuits|regulatory|regulators?|"
        r"backlash|criticism|critics?|"
        r"morale|workforce|layoff|layoffs|"
        r"privacy concern|safety concern|"
        r"employees? (?:are|were) (?:unhappy|miserable|angry|frustrated)|"
        r"dark clouds?|uncertain|uncertainty|"
        # Expert-warning kicker patterns: concluding expert quote that
        # frames the subject as dangerous, reckless, or alarming.
        # Discovered via MIT TR Meta AI hack analysis (Jun 2026) where
        # "I think it's a very dangerous thing" was the kicker quote.
        r"very dangerous|extremely dangerous|incredibly dangerous|"
        r"dangerous thing|dangerous path|dangerous precedent|"
        r"alarming|reckless|irresponsible|"
        # Anticompetitive / governance framing kicker — article ends by
        # reframing the subject's actions as anticompetitive or corrupt.
        # Discovered via Futurism Cannes reframe (Jul 2026): "safety
        # becomes a convenient cover for anticompetitive practices."
        r"anticompetitive|anti.?competitive|convenient cover|"
        r"governance gray zone|governance grey zone|"
        r"convenient (?:excuse|pretext|shield|fig leaf)|"
        r"wake.?up call|cautionary|warning sign|red flag)\b",
        re.IGNORECASE,
    ),
    # Open-ended threat / unresolved-question kicker — the article ends
    # by leaving a negative outcome as an open possibility rather than
    # resolving it.  Classic editorial device: "whether X catches up,"
    # "the part that's still open," "remains to be seen."  The reader's
    # last impression is unresolved risk, regardless of earlier tone.
    # Discovered via Memeburn Meta glasses article (Jun 2026): "Whether
    # the privacy questions catch up before the adoption does is the part
    # that's still open."
    re.compile(
        r"\b(?:whether .{5,80}?catch(?:es)? up|"
        r"(?:the )?part that(?:'s| is) still (?:open|unclear|unresolved)|"
        r"remains to be seen|time will tell|"
        r"jury is still out|"
        r"(?:an |the )?open question|"
        r"yet to be (?:answered|resolved|determined|settled)|"
        r"only time (?:will|can) tell|"
        r"how (?:that|this|it) (?:plays|shakes|works) out)\b",
        re.IGNORECASE,
    ),
]


# ---------------------------------------------------------------------------
# Speculative framing: editorial device deploying cumulative conditional
# language ("could potentially," "might be able to," "in principle") to
# construct a narrative of inevitability while maintaining individual
# hedges.  A single hedge is good journalism; 10+ hedges in one article
# is a framing technique that converts possibility into implied certainty.
# Like analogy_stacking, this fires as a post-pass when the count exceeds
# a threshold (5+ instances), since individual hedges are unremarkable.
# ---------------------------------------------------------------------------
_SPECULATIVE_FRAMING_PATTERNS: list[re.Pattern] = [
    # "could potentially" / "could conceivably" / "could feasibly"
    re.compile(
        r"\bcould\s+(?:potentially|conceivably|feasibly|theoretically|"
        r"in theory|in principle|plausibly|arguably|effectively|easily|"
        r"very well|quite possibly)\b",
        re.IGNORECASE,
    ),
    # "might be able to" / "might make it" / "might enable"
    re.compile(
        r"\bmight\s+(?:be able to|make it|enable|allow|permit|lead to|"
        r"result in|facilitate|open the door|give)\b",
        re.IGNORECASE,
    ),
    # "in principle" / "in theory" (standalone)
    re.compile(
        r"\b(?:in principle|in theory|hypothetically|theoretically)\b",
        re.IGNORECASE,
    ),
    # "it's possible that" / "it is possible that" / "there's a chance"
    re.compile(
        r"\b(?:it(?:'s| is) (?:possible|conceivable|plausible|likely|not impossible)"
        r"|there(?:'s| is) (?:a chance|a possibility|a risk|reason to (?:think|believe|fear))"
        r"|there(?:'s| is) early evidence"
        r"|is it (?:possible|conceivable|plausible|likely|naive to think))\b",
        re.IGNORECASE,
    ),
    # "not yet any" / "not yet evidence" / "no smoking gun"
    re.compile(
        r"\b(?:not yet any|no(?:t yet| ) (?:smoking.?gun|direct|clear|definitive|concrete)"
        r"\s+evidence)\b",
        re.IGNORECASE,
    ),
    # "could change that" / "could alter" / "could transform" / "could reshape"
    # Allows one optional intervening adverb: "could later influence",
    # "could easily affect", "could ultimately determine"
    re.compile(
        r"\bcould\s+(?:\w+\s+)?(?:change|alter|transform|reshape|upend|shift|undermine|"
        r"erode|weaken|eliminate|remove|lessen|"
        r"influence|affect|impact|leak|seep|expose|enable|allow|determine|shape)\b",
        re.IGNORECASE,
    ),
    # "suggests that X could/might/may" — indirect evidence framing
    re.compile(
        r"\b(?:suggests?|indicates?|implies?|hints?)\s+that\b"
        r".{0,60}?"
        r"\b(?:could|might|may|can)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "raises the possibility" / "opens the door to" / "paves the way for"
    re.compile(
        r"\b(?:raises? the possibility|opens? the door|paves? the way"
        r"|lays? the groundwork|sets? the stage)\b",
        re.IGNORECASE,
    ),
    # Conditional "if X were to" / "if X wanted to" / "were X to"
    re.compile(
        r"\b(?:if\s+(?:\w+\s+){0,3}(?:were to|wanted to|chose to|decided to)"
        r"|were\s+(?:\w+\s+){0,2}to\s+(?:\w+))\b",
        re.IGNORECASE,
    ),
    # Explicit hypothetical markers — "for the sake of argument", "let's pretend"
    re.compile(
        r"\b(?:for the sake of argument|purely for the sake of argument|"
        r"let'?s (?:pretend|imagine|suppose|say|assume|hypothesize)|"
        r"(?:in (?:a|this|that|such a) )?hypothetical (?:scenario|situation|world|case)|"
        r"thought experiment|"
        r"just for argument'?s? sake)\b",
        re.IGNORECASE,
    ),
    # First-person hedge / dismissal-by-author — columnists inserting
    # personal speculation as editorial voice rather than reporting.
    # "I wouldn't write it off", "I wouldn't rule it out", "I wouldn't bet against"
    re.compile(
        r"\bI wouldn'?t (?:write it off|rule it out|rule that out|bet against|"
        r"bet on|be surprised|count on|dismiss|underestimate|overstate)\b",
        re.IGNORECASE,
    ),
    # "Playing this forward" / "playing this out" / "extend this logic" —
    # explicit speculative projection framing
    re.compile(
        r"\b(?:playing this forward|playing this out|play this forward|"
        r"play this out|extend(?:ing)? this logic|follow(?:ing)? this logic|"
        r"take this (?:to its logical|a step further))\b",
        re.IGNORECASE,
    ),
]

# Note: speculative_framing patterns are NOT registered in _DEVICE_PATTERNS
# because the device fires only when 5+ distinct speculative markers are
# found (cumulative effect threshold).  Individual hedges are normal
# journalism.  Detection happens in _detect_speculative_framing() and
# results are injected by detect_framing_devices() when threshold is met.


# Confession framing: editorial device using attribution verbs that frame
# a subject's statement as an admission of guilt or failure, rather than
# a neutral communication.  "X admits Y" vs. "X said Y" imposes a
# confession frame before the reader encounters the content.  Common in
# Wired/Guardian Meta coverage.  Distinct from loaded_language (which
# flags individual words): this device detects the editorial *structure*
# of framing via attribution verb choice.
#
# The asymmetry is the key signal: employees "describe" or "say" while
# executives "admit" or "concede" — identical speech acts receive
# different editorial treatment based on who is speaking.
_CONFESSION_FRAMING_PATTERNS: list[re.Pattern] = [
    # Core confession attribution verbs in editorial voice.
    # These verbs impose guilt/concealment on the speaker when used as
    # attribution: "Bosworth admits" ≠ "Bosworth said."
    # Requires subject-verb proximity (name/title + verb within 30 chars)
    # to avoid matching content where someone literally confesses to a crime.
    # The (?:that |") lookahead ensures the verb is introducing reported
    # speech or a characterization, not describing a legal/literal confession.
    re.compile(
        r"\b(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?|"
        r"the (?:CEO|CTO|COO|CFO|chief|executive|company|firm|"
        r"spokesperson|official|director|president|chairman|VP|"
        r"vice president|head|manager|leader))"
        r"\s+"
        r"(?:also\s+)?"
        r"(?:admit(?:ted|s)?|conced(?:ed|es|ing)|acknowledg(?:ed|es|ing))"
        r"\s+(?:that\b|\")",
        re.IGNORECASE,
    ),
    # Headline-style: "X Admits Y" — title case suggests headline placement.
    # Headline confession framing is especially impactful because it sets
    # the reader's interpretive frame before they encounter the article body.
    re.compile(
        r"\b(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s+"
        r"Admits?\s+",
        re.MULTILINE,
    ),
    # "Was forced to admit/acknowledge/concede" — amplified confession frame.
    # Editorial language positioning the admission as involuntary, implying
    # the subject would have preferred to conceal.
    re.compile(
        r"\b(?:was |were |been )?"
        r"(?:forced|compelled|pressured|pushed)\s+"
        r"(?:to |into )?"
        r"(?:admit|acknowledge|concede|come clean|own up)",
        re.IGNORECASE,
    ),
    # "Finally admitted/acknowledged/conceded" — delayed confession.
    # Editorial signal that the admission was overdue, implying prior
    # concealment or resistance to transparency.
    re.compile(
        r"\b(?:finally|eventually|at last|belatedly|only then|"
        r"only after|reluctantly|grudgingly|begrudgingly)\s+"
        r"(?:admit(?:ted|s)?|acknowledg(?:ed|es|ing)|conced(?:ed|es|ing))",
        re.IGNORECASE,
    ),
    # "Comes/came clean about" — informal confession framing
    re.compile(
        r"\b(?:com(?:es?|ing)|came)\s+clean\s+(?:about|on|over)\b",
        re.IGNORECASE,
    ),
    # "Owned up to" — informal confession framing
    re.compile(
        r"\b(?:own(?:ed|s|ing)?)\s+up\s+to\b",
        re.IGNORECASE,
    ),
    # "Mea culpa" — direct confession framing applied to corporate
    # communications.  When a journalist labels a memo or statement
    # as a "mea culpa," they impose a penitential frame.
    re.compile(
        r"\bmea culpa\b",
        re.IGNORECASE,
    ),
    # "In a rare admission" / "in a candid admission" — editorial
    # meta-framing that explicitly labels the statement as an admission,
    # priming the reader to interpret what follows as a confession.
    re.compile(
        r"\bin (?:a |an )?(?:rare|unusual|candid|remarkable|stunning|"
        r"surprising|extraordinary|notable|frank|startling)\s+"
        r"(?:admission|acknowledgment|acknowledgement|concession|confession)",
        re.IGNORECASE,
    ),
    # Bare "a rare admission" / "the rare admission" / "his rare
    # admission" — same editorial meta-framing without the "in" prefix.
    # Common in headlines and sentence-initial constructions:
    #   "A rare admission from Zuckerberg..."
    #   "The rare admission came during a town hall..."
    #   "His rare admission that agents hadn't progressed..."
    # Also catches possessive "Zuckerberg's rare admission".
    re.compile(
        r"\b(?:a |an |the |his |her |its |their |"
        r"[A-Z][a-z]+(?:'s|'s|\u2019s) )"
        r"(?:rare|unusual|candid|remarkable|stunning|"
        r"surprising|extraordinary|notable|frank|startling)\s+"
        r"(?:admission|acknowledgment|acknowledgement|concession|confession)",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["confession_framing"] = _CONFESSION_FRAMING_PATTERNS


# ---------------------------------------------------------------------------
# Latecomer narrative — editorial device that frames a company as entering
# a space after competitors already established themselves, positioning the
# subject as playing catch-up rather than innovating.  Common in tech
# coverage: "Meta explores partnerships with Polymarket" (existing player)
# vs "Meta launches prediction market" (innovator).  The editorial choice
# to emphasize partnership/exploration with incumbents rather than
# independent capability is itself a framing decision.
#
# Identified in NYT's Meta Arena/Polymarket partnership article (Jun 2026):
# the article frames Meta as exploring working WITH existing platforms
# rather than building a competing product, a latecomer construction.
# ---------------------------------------------------------------------------

_LATECOMER_NARRATIVE_PATTERNS: list[re.Pattern] = [
    # "exploring partnerships with [Established Player]"
    re.compile(
        r"\bexplor(?:ing|es?|ed)\s+(?:a\s+)?(?:potential\s+)?"
        r"(?:partnership|collaboration|deal|alliance|tie-up|arrangement)s?\s+"
        r"with\b",
        re.IGNORECASE,
    ),
    # "joining the race" / "entering the race"
    re.compile(
        r"\b(?:join(?:ing|ed|s)?|enter(?:ing|ed|s)?)\s+the\s+"
        r"(?:race|competition|market|fray|arena|battle|fight)\b",
        re.IGNORECASE,
    ),
    # "following in the footsteps of" / "taking a page from"
    re.compile(
        r"\b(?:follow(?:ing|ed|s)?\s+in\s+the\s+footsteps\s+of|"
        r"tak(?:ing|es?|en)\s+a\s+(?:page|leaf|cue)\s+from)\b",
        re.IGNORECASE,
    ),
    # "building a similar app/product/platform/feature" / "developing its own version"
    re.compile(
        r"\b(?:build(?:ing|s)?|develop(?:ing|s)?|creat(?:ing|es?)|"
        r"roll(?:ing|s)?\s+out|launch(?:ing|es)?)\s+"
        r"(?:a\s+)?(?:its?\s+own\s+)?(?:similar|competing|rival|copycat|"
        r"comparable|equivalent|alternative)\s+"
        r"(?:app|product|platform|feature|service|tool|version|offering)\b",
        re.IGNORECASE,
    ),
    # "a market already dominated by" / "space already occupied by"
    re.compile(
        r"\b(?:market|space|field|sector|industry|category|arena)\s+"
        r"(?:already\s+)?(?:dominated|occupied|led|controlled|cornered|"
        r"owned)\s+by\b",
        re.IGNORECASE,
    ),
    # "playing catch-up" / "trying to catch up"
    re.compile(
        r"\b(?:play(?:ing|s|ed)?\s+catch[- ]?up|"
        r"try(?:ing|ies)?\s+to\s+catch\s+up|"
        r"scrambl(?:ing|es?|ed)\s+to\s+(?:catch|keep)\s+up)\b",
        re.IGNORECASE,
    ),
    # "late to the game" / "late entrant" / "latecomer"
    # NOTE: bare "late" is excluded — too broad (matches "in late 2022").
    # Require "latecomer", "late to the …", "late entrant", or "late …" phrases.
    re.compile(
        r"\b(?:latecomer(?:\s+to\s+the\s+(?:game|party|market|race|space))?|"
        r"late\s+(?:to\s+the\s+(?:game|party|market|race|space)|entrant)|"
        r"johnny[- ]?come[- ]?lately|"
        r"behind\s+(?:the\s+)?(?:curve|times|competitors|rivals|peers))\b",
        re.IGNORECASE,
    ),
    # "still lacks" / "still doesn't have" / "yet to develop" — capability
    # gap framing relative to established competitors.
    re.compile(
        r"\b(?:still\s+(?:lack(?:s|ing|ed)?|"
        r"do(?:es)?n['\u2019]t\s+have|"
        r"has(?:n['\u2019]t| not)\s+(?:developed|built|launched|created))|"
        r"(?:has|have)\s+yet\s+to\s+(?:develop|build|launch|create|roll out))\b",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["latecomer_narrative"] = _LATECOMER_NARRATIVE_PATTERNS


# ---------------------------------------------------------------------------
# Regulatory shadow — editorial device where regulatory, legal, or
# investigative context is appended to or interwoven with a product or
# business story, casting a shadow over the primary subject without
# directly accusing it.  The juxtaposition of "increasing scrutiny,"
# "drawn regulatory attention," or pending legal action near a product
# announcement or business deal implies risk or wrongdoing by proximity.
#
# Distinct from litigation_framing (which captures explicit legal actions)
# and geopolitical_regulatory_pressure (which captures state-level
# pressure campaigns).  Regulatory shadow is the *ambient* technique of
# inserting regulatory/legal context into stories where it is tangential
# to the primary subject.
#
# Identified in NYT's Meta Arena/Polymarket partnership article (Jun 2026):
# prediction markets context is shadowed by references to "increasing
# scrutiny" and insider trading investigations — regulatory concerns
# belonging to the broader prediction market industry, not to Meta's
# product specifically.
# ---------------------------------------------------------------------------

_REGULATORY_SHADOW_PATTERNS: list[re.Pattern] = [
    # "increasing/growing/heightened scrutiny" — ambient regulatory
    # atmosphere applied to a company or product.
    re.compile(
        r"\b(?:increas(?:ing|ed)|growing|heightened|renewed|intensif(?:ied|ying)|"
        r"mounting|escalat(?:ing|ed)|greater)\s+"
        r"(?:regulatory\s+)?scrutiny\b",
        re.IGNORECASE,
    ),
    # "drawn scrutiny from" / "attracted scrutiny from"
    re.compile(
        r"\b(?:draw(?:n|ing|s)?|attract(?:ed|ing|s)?|invit(?:ed|ing|es)?|"
        r"garner(?:ed|ing|s)?)\s+(?:increased\s+|growing\s+|renewed\s+)?"
        r"(?:regulatory\s+)?scrutiny\b",
        re.IGNORECASE,
    ),
    # "facing regulatory" + noun — "facing regulatory hurdles/challenges/
    # pressure/uncertainty/risk/headwinds"
    re.compile(
        r"\bfac(?:ing|es?|ed)\s+(?:potential\s+|new\s+|fresh\s+|additional\s+)?"
        r"regulatory\s+"
        r"(?:hurdle|challenge|pressure|uncertainty|risk|headwind|"
        r"obstacle|barrier|concern|question|investigation|inquiry|probe|"
        r"review|backlash|pushback|opposition)s?\b",
        re.IGNORECASE,
    ),
    # "regulators have/are" + action — regulators framed as active agents
    # moving against the subject.
    re.compile(
        r"\bregulators?\s+(?:have\s+|are\s+|had\s+|were\s+)?"
        r"(?:investigat(?:ing|ed)|examin(?:ing|ed)|prob(?:ing|ed)|"
        r"question(?:ing|ed)|warn(?:ing|ed)|target(?:ing|ed)|"
        r"crack(?:ing|ed)\s+down|rais(?:ing|ed)\s+concerns?|"
        r"express(?:ing|ed)\s+concerns?|signal(?:l?ing|l?ed))\b",
        re.IGNORECASE,
    ),
    # "amid/despite/notwithstanding" + regulatory/legal context — the
    # syntactic marker for shadow framing: product news presented "amid"
    # regulatory developments.
    re.compile(
        r"\b(?:amid(?:st)?|despite|notwithstanding|even as|at a time when)\s+"
        r"(?:\w+\s+){0,4}(?:regulat(?:ory|ion|ors?)|"
        r"antitrust|investigation|probe|inquiry|enforcement|litigation|"
        r"lawsuit|legal\s+(?:challenge|battle|threat|action|scrutiny)|"
        r"compliance\s+(?:concern|issue|risk))\b",
        re.IGNORECASE,
    ),
    # "raised concerns about" / "sparked concerns about" — editorial
    # device that introduces worry without attributing it to a specific
    # source.
    re.compile(
        r"\b(?:rais(?:ed|ing|es?)|spark(?:ed|ing|s)?|prompt(?:ed|ing|s)?|"
        r"fuel(?:l?ed|l?ing|s)?|stok(?:ed|ing|es)?|stirr(?:ed|ing|s)?)\s+"
        r"(?:fresh\s+|new\s+|renewed\s+)?concerns?\s+"
        r"(?:about|over|regarding|that)\b",
        re.IGNORECASE,
    ),
    # "potential fine/penalty/sanction" — implied legal consequences
    # inserted into business coverage.
    re.compile(
        r"\b(?:potential|possible|looming|threatened|expected|anticipated|"
        r"prospective)\s+"
        r"(?:fine|penalty|penalt(?:ies)|sanction|enforcement\s+action|"
        r"legal\s+action|regulatory\s+action|consent\s+(?:decree|order)|"
        r"ban|restriction|crackdown)s?\b",
        re.IGNORECASE,
    ),
    # "could face" / "may face" + legal/regulatory consequences —
    # speculative-regulatory construction.
    re.compile(
        r"\b(?:could|may|might|would)\s+(?:potentially\s+)?face\s+"
        r"(?:\w+\s+){0,3}(?:fine|penalty|penalt(?:ies)|sanction|"
        r"enforcement|regulatory|legal|antitrust|investigation|"
        r"scrutiny|backlash|action|challenge|lawsuit|litigation)\b",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["regulatory_shadow"] = _REGULATORY_SHADOW_PATTERNS


# --------------------------------------------------------------------------- #
#  Editorial Deflation                                                         #
# --------------------------------------------------------------------------- #
#
# A recognizable editorial technique in which the writer builds up an
# ambitious technological vision, corporate plan, or product promise across
# one or more paragraphs, then punctures it with a brief dismissive or
# hedging phrase that implies failure or impracticality without explicit
# argument.  The deflation is the writer's editorial choice — it appears
# as casual hedging but functions as skepticism-by-implication.
#
# Distinct from:
#   - corporate_reassurance_undercut (undercuts a company's OWN reassurance)
#   - sarcastic_correction (overtly mocking/ironic)
#   - speculative_framing (projects negative futures)
#   - loaded_language (uses emotionally charged vocabulary)
#
# The patterns below target the most distinctive deflation constructions
# that are rarely neutral hedging and almost always serve an editorial
# puncturing function.  Generic uncertainty phrases ("remains to be seen",
# "time will tell") are excluded because they appear too frequently in
# genuine neutral reporting.
#
# Discovered via manual analysis of MIT Technology Review "Inside Anduril
# and Meta's quest to make smart glasses for warfare" (May 18, 2026),
# where "That's the idea, anyway" deflates three paragraphs of ambitious
# military AR vision into implied impracticality.

_EDITORIAL_DEFLATION_PATTERNS: list[re.Pattern] = [
    # "That's the idea/plan/pitch/theory/hope/promise/vision, anyway"
    # or "at least" — the classic post-buildup deflation
    re.compile(
        r"\bthat'?s\s+the\s+(?:idea|plan|pitch|theory|hope|promise|vision|dream|goal)"
        r",?\s+(?:anyway|at\s+least|so\s+far|for\s+now)\b",
        re.IGNORECASE,
    ),
    # "At least, that's the plan/idea/hope/pitch" — inverted form
    re.compile(
        r"\b(?:at\s+least|anyway),?\s+that'?s\s+"
        r"(?:the\s+)?(?:plan|idea|hope|pitch|promise|theory|vision|goal)\b",
        re.IGNORECASE,
    ),
    # "or so X says/claims/hopes/argues/insists" — attribution-as-skepticism
    re.compile(
        r"\bor\s+so\s+(?:\w+\s+){0,3}"
        r"(?:says?|claims?|hopes?|argues?|insists?|contends?|maintains?|promises?)\b",
        re.IGNORECASE,
    ),
    # "so the argument/thinking/theory/logic goes" — dismissive framing
    re.compile(
        r"\b(?:or\s+)?so\s+the\s+"
        r"(?:argument|thinking|theory|logic|idea|pitch|promise|narrative)\s+goes\b",
        re.IGNORECASE,
    ),
    # "if [it/this/that] ever actually [works/ships/launches/happens]"
    re.compile(
        r"\bif\s+(?:it|this|that|the\s+\w+)\s+ever\s+actually\s+"
        r"(?:works?|ships?|launches?|happens?|arrives?|materializes?|comes?\s+to\s+fruition)\b",
        re.IGNORECASE,
    ),
    # "in theory, anyway/at least" — concedes theory, implies practice differs
    re.compile(
        r"\bin\s+theory,?\s+(?:anyway|at\s+least|sure|of\s+course)\b",
        re.IGNORECASE,
    ),
    # "but that's/it's a big/tall/high/enormous if" — amplified uncertainty
    re.compile(
        r"\b(?:but\s+)?(?:that'?s?|it'?s?)\s+a\s+"
        r"(?:big|tall|high|enormous|significant|very\s+big)\s+"
        r"(?:if|ask|gamble|bet|assumption)\b",
        re.IGNORECASE,
    ),
    # "whether [it/that/this] actually/really/ever pans out / works / materializes"
    re.compile(
        r"\bwhether\s+(?:that|this|it|any\s+of\s+(?:that|this|it))\s+"
        r"(?:actually|really|ever)\s+"
        r"(?:works?|happens?|materializes?|pans?\s+out|comes?\s+together|pays?\s+off)\b",
        re.IGNORECASE,
    ),
    # Concession-then-dismissal: "Noble/Good/Fine/Admirable X, indeed/sure/
    # of course, but [not/maybe not/hardly]" — acknowledges a point only to
    # immediately undercut it.  Detected in Gizmodo's "Kids Over Clicks"
    # article (Jun 2026): "Noble efforts, indeed, but maybe not the most
    # pressing concern" went undetected.
    re.compile(
        r"\b(?:noble|admirable|good|fine|laudable|fair|worthy|reasonable|"
        r"well-intentioned|well\s+intentioned)\s+"
        r"(?:effort|goal|idea|aim|point|thought|gesture|ambition|initiative|proposal)s?"
        r",?\s+(?:indeed|sure|of\s+course|certainly|to\s+be\s+(?:sure|fair))"
        r",?\s+but\b",
        re.IGNORECASE,
    ),
    # "That may be true/fair/right, but" — explicit concession before pivot
    re.compile(
        r"\bthat(?:'s|\s+is|\s+may\s+be|\s+might\s+be)\s+"
        r"(?:true|fair|right|reasonable|understandable|valid)"
        r",?\s+but\b",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["editorial_deflation"] = _EDITORIAL_DEFLATION_PATTERNS

# ---------------------------------------------------------------------------
# Additional editorial_deflation patterns: parenthetical hindsight asides
# and editorial reframing ("or should we say").
#
# Identified in Barchart "Meta Shows Urgency" (Jun 30, 2026):
#   "(or, in hindsight, infamously)" — parenthetical aside that deflates
#   a supposedly positive framing.
#   "or should we say *justify*" — editorial reframing that substitutes
#   the source's positive term with a skeptical one.
# ---------------------------------------------------------------------------
_EDITORIAL_DEFLATION_PATTERNS.extend([
    # "in hindsight, [negative term]" — parenthetical hindsight deflation
    re.compile(
        r"\b(?:in\s+hindsight|looking\s+back|with\s+(?:the\s+benefit\s+of\s+)?hindsight)"
        r",?\s*(?:\w+\s+)?"
        r"(?:infamously|ironically|unfortunately|mistakenly|naively|foolishly|"
        r"wrongly|prematurely|optimistically|disastrously)\b",
        re.IGNORECASE,
    ),
    # "or should we say [skeptical reframe]"
    re.compile(
        r"\bor\s+should\s+we\s+say\b.{3,60}",
        re.IGNORECASE,
    ),
    # "or, to put it [another/more] [bluntly/accurately/honestly]"
    re.compile(
        r"\bor,?\s+to\s+put\s+it\s+(?:another|more)\s+"
        r"(?:way|bluntly|accurately|honestly|plainly|charitably|uncharitably)\b",
        re.IGNORECASE,
    ),
    # --- Added 2026-07-02: Register Brain2Qwerty v2 analysis ---
    # "In other words" as editorial reframing — signals the journalist is
    # about to restate the source's claims in diminished terms.  "In other
    # words, what we have here is a neat experiment" went undetected.
    re.compile(
        r"\bin\s+other\s+words,?\s+"
        r"(?:what\s+we\s+have\s+(?:here\s+)?is|this\s+is|it(?:'s|\s+is))\s+"
        r"(?:just|merely|only|basically|essentially|nothing\s+more\s+than)?\s*"
        r"(?:a\s+)?(?:neat|nice|interesting|cool|cute|modest|small|incremental|minor"
        r"|limited|preliminary|early|niche)\b",
        re.IGNORECASE,
    ),
    # Faint praise / damning with diminutives: "a neat/nice/interesting
    # experiment/trick/demo/step/start, but" — conspicuous understatement
    # that deflates significance.  "a neat experiment with some impressive
    # improvements ... but nothing that's going to transform" went undetected.
    re.compile(
        r"\ban?\s+(?:neat|nice|interesting|cool|cute|nifty|clever)\s+"
        r"(?:experiment|trick|demo|demonstration|step|start|beginning|prototype|proof\s+of\s+concept"
        r"|concept|piece\s+of\s+research|paper|study)"
        r"(?:\s+(?:with|that|for|in)\s+[^,]{5,60})?"
        r",?\s+but\b",
        re.IGNORECASE,
    ),
    # "a bit/somewhat/rather useless/pointless/impractical" — casual
    # dismissal phrased as understatement.  "a bit useless" in Register
    # Brain2Qwerty v2 article went undetected.
    re.compile(
        r"\ba\s+(?:bit|little|tad|somewhat|rather)\s+"
        r"(?:useless|pointless|impractical|irrelevant|misleading|disingenuous"
        r"|premature|hollow|empty|circular|meaningless|underwhelming)(?:\b|,)",
        re.IGNORECASE,
    ),
    # --- Added 2026-07-03: Register Brain2Qwerty v2 headline analysis ---
    # Headline qualification: "improves/improved... but still isn't great"
    # — acknowledges progress then immediately deflates in the title.
    # Pattern: "but still isn't/aren't/won't/can't [positive adj]"
    re.compile(
        r"\bbut\s+still\s+(?:isn't|aren't|won't|can't|doesn't|don't|hasn't)\s+"
        r"(?:great|good|ready|useful|usable|practical|viable|impressive"
        r"|enough|perfect|working|reliable|accurate|fast|there)\b",
        re.IGNORECASE,
    ),
    # "not exactly [positive]" — hedged dismissal disguised as understatement.
    # "it's not exactly a promising, commercially viable pathway" reframes
    # a real improvement as commercially irrelevant.
    re.compile(
        r"\b(?:it's|that's|this\s+is|it\s+is)\s+not\s+exactly\s+"
        r"(?:a\s+)?(?:promising|encouraging|compelling|impressive|convincing"
        r"|revolutionary|groundbreaking|practical|viable|useful|great)\b",
        re.IGNORECASE,
    ),
])


# ---------------------------------------------------------------------------
# Denial contradiction: editorial device where a source's direct denial or
# minimization is juxtaposed against evidence that contradicts it.  The
# journalist quotes the denial, then within a short window presents code
# evidence, document evidence, or factual reporting that shows the denial
# was false or misleading.  This is one of the most powerful framing
# techniques in investigative journalism because it lets the source
# discredit themselves without the journalist having to editorialize.
#
# Distinct from:
# - hypocrisy_frame: catches "say one thing, do another" across stated
#   policy vs. actual behavior over time
# - corporate_reassurance_undercut: catches PR language ("carefully designed",
#   "committed to safety") being undermined
# - refusal_amplification: catches repeated refusals to answer
#
# denial_contradiction specifically catches:
# 1. Direct denial quotes contradicted by evidence in the same passage
# 2. "does not exist" / "merely exploratory" / "no final decision" language
#    followed by code/document/analysis evidence
# 3. Combative pushback ("misleading", "dishonest") followed by proof
#
# Identified as critical gap in:
# - Wired NameTag removal (Jun 8, 2026): "the feature does not exist" (Stone)
#   → contradicted by code analysis showing fully built system
# - Wired NameTag removal: "incredibly misleading" and "absolutely dishonest"
#   (Bosworth) → Meta removed the code the next day
# - Wired NameTag initial (Jun 5, 2026): "No final decision has been made"
#   → code libraries explicitly named for face recognition already in app
# - Digital Trends NameTag coverage (Jun 9, 2026): "part of a pilot" /
#   "had not decided whether to use it" → code appeared in consumer app
# ---------------------------------------------------------------------------
_DENIAL_CONTRADICTION_PATTERNS: list[re.Pattern] = [
    # Direct "does not exist" / "is not real" / "is purely exploratory"
    # denial near evidence markers (found, revealed, showed, analysis)
    re.compile(
        r"(?:\"[^\"]*?"
        r"(?:does not exist|doesn.?t exist|is not (?:a |an )?(?:real|actual|live|active)|"
        r"purely (?:exploratory|theoretical|hypothetical|conceptual)|"
        r"merely (?:evidence|exploratory|an? exploration)|"
        r"no final decision|not (?:yet )?(?:been )?(?:decided|determined|finalized)|"
        r"no evidence (?:that|of)|there is no truth|there is no basis|"
        r"not building|not developing|no plans? to)"
        r"[^\"]*?\")"
        r".{5,400}?"
        r"\b(?:found|revealed|showed|discovered|uncovered|confirmed|"
        r"replicated?|verified|corroborated|validated|"
        r"analysis|investigation|code|evidence|documents?|data|"
        r"report(?:ed|ing)?|according to)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Combative denial ("misleading", "dishonest", "inaccurate", "false")
    # followed by evidence that supports the original claim.
    # Handles both full quoted sentences and short quoted fragments
    # ("incredibly misleading" or "absolutely dishonest").
    # Pre-quote attribution form: "called/described it [combative quote]"
    re.compile(
        r"\b(?:called|described|labeled|termed|characterized|dismissed)\b"
        r".{0,60}?"
        r"(?:\"[^\"]*?"
        r"(?:misleading|dishonest|inaccurate|false|untrue|"
        r"irresponsible|reckless|unfounded|baseless|unfair|"
        r"fundamentally flawed|flawed|misunderstanding|"
        r"mischaracteriz|misrepresent)"
        r"[^\"]*?\")"
        r".{5,600}?"
        r"\b(?:removed|stripped|deleted|pulled|eliminated|"
        r"the (?:code|feature|system|data|software)|"
        r"the (?:next|following|very next) (?:day|morning|update|version)|"
        r"removes? (?:nearly )?all traces|"
        r"replicated?|verified|corroborated|validated|"
        r"however|but|yet|in fact|nonetheless|nevertheless|"
        r"contradicting|confirming|proving|showing)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Post-quote combative denial: "[combative quote]" said/insisted ...
    # [evidence counter].  Handles direct-quote form where attribution
    # follows the denial rather than preceding it.
    # Identified in Engadget child safety features article (Jun 2026):
    #   '"The claims are baseless," a spokesperson insisted.
    #    Researchers... verified the methodology.'
    re.compile(
        r"(?:\"[^\"]*?"
        r"(?:misleading|dishonest|inaccurate|false|untrue|"
        r"irresponsible|reckless|unfounded|baseless|unfair|"
        r"fundamentally flawed|flawed|misunderstanding|"
        r"mischaracteriz|misrepresent)"
        r"[^\"]*?\")"
        r".{0,40}?"
        r"\b(?:said|insisted|maintained|declared|claimed|stated|"
        r"responded|replied|countered|retorted|snapped|argued|"
        r"asserted|contended|pushed back)\b"
        r".{5,400}?"
        r"\b(?:found|revealed|showed|discovered|uncovered|confirmed|"
        r"replicated?|verified|corroborated|validated|"
        r"analysis|investigation|code|evidence|documents?|data|"
        r"report(?:ed|ing)?|according to)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Evidence first, then denial — reverse order where the journalist
    # presents findings and then quotes the denial, making it land as
    # implausible.  "WIRED found/reported/revealed X... [source] said/called
    # it 'denial'"
    re.compile(
        r"\b(?:found|revealed|reported|discovered|showed|uncovered|"
        r"identified|detected|confirmed)\b"
        r".{10,300}?"
        r"(?:said|told|called|described|dismissed|characterized)\s+"
        r"(?:the|it|this|that|these|those|WIRED.s|the (?:report|finding|investigation))"
        r".{0,60}?"
        r"(?:\"[^\"]*?"
        r"(?:does not exist|doesn.?t exist|misleading|dishonest|"
        r"fundamentally flawed|flawed|misunderstanding|"
        r"purely exploratory|merely|not (?:a )?real|no (?:final )?decision|"
        r"not building|not developing)"
        r"[^\"]*?\")",
        re.IGNORECASE | re.DOTALL,
    ),
    # "had not decided whether to" / "part of a pilot" / "exploring"
    # near "but" / "does not answer" / "does not explain" —
    # catches softer minimization language being editorially undercut.
    # Handles both direct quotes and indirect speech (no quote marks).
    re.compile(
        r"(?:\"[^\"]*?"
        r"(?:part of a (?:pilot|test|experiment|trial)|"
        r"had not (?:yet )?decided|"
        r"still (?:exploring|evaluating|considering|assessing)|"
        r"no (?:final |firm |definitive )?(?:decision|timeline|commitment)|"
        r"thinking through|weighing|under consideration)"
        r"[^\"]*?\")"
        r".{5,250}?"
        r"\b(?:does not (?:answer|explain|address|account for)|"
        r"doesn.?t (?:answer|explain|address|account for)|"
        r"but|however|yet|"
        r"harder to (?:brush aside|dismiss|ignore|accept)|"
        r"raises? (?:questions?|concerns?|doubts?))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Indirect-speech variant: "told X that [minimization]... but/however"
    # For articles that paraphrase rather than directly quote the denial.
    re.compile(
        r"\b(?:told|said|stated|added|insisted|maintained|stressed)\b"
        r".{0,40}?"
        r"\b(?:that\s+)?"
        r"(?:the feature was (?:part of|purely|merely|only)|"
        r"(?:had|have|has) not (?:yet )?(?:decided|determined|finalized|made)|"
        r"(?:was|were|is|are) (?:still |merely |purely )?"
        r"(?:exploratory|exploring|evaluating|considering|"
        r"experimental|a (?:pilot|test|experiment))|"
        r"no (?:final |firm |definitive )?decision)\b"
        r".{5,300}?"
        r"\b(?:does not (?:answer|explain|address|account for)|"
        r"doesn.?t (?:answer|explain|address|account for)|"
        r"but|however|yet|"
        r"harder to (?:brush aside|dismiss|ignore|accept)|"
        r"raises? (?:questions?|concerns?|doubts?)|"
        r"when .{5,80}? (?:appears?|surfaces?|disappears?|vanish))\b",
        re.IGNORECASE | re.DOTALL,
    ),
]

_DEVICE_PATTERNS["denial_contradiction"] = _DENIAL_CONTRADICTION_PATTERNS


# ---------------------------------------------------------------------------
# Worker replacement irony: editorial framing device where the narrative
# emphasizes that workers built/trained/created the very technology that
# replaces them.  The irony is structural — the sentence or passage
# juxtaposes the human contribution (training, labeling, moderating) with
# the resulting AI system that now eliminates their roles.
#
# Distinct from juxtaposition (which contrasts profits vs. cuts) and
# hypocrisy_frame (which contrasts stated policy vs. actual behavior).
# Worker replacement irony specifically captures the recursive quality:
# the workers' own labor produced the instrument of their displacement.
#
# Identified in WebProNews Meta Dublin contractors article (May 2026):
#   "Content moderators who trained AI models now face replacement by
#    those same systems"
#   "Their replacements are the very models they helped build."
#   "We trained the bots. We did the grind. Now we're being left behind."
# ---------------------------------------------------------------------------
_WORKER_REPLACEMENT_IRONY_PATTERNS: list[re.Pattern] = [
    # "trained/built/created/labeled [AI/models/bots/systems] ...
    #  replaced/eliminated/laid off/made redundant"
    re.compile(
        r"\b(?:train(?:ed|ing)|built|creat(?:ed|ing)|develop(?:ed|ing)|"
        r"label(?:ed|ing|led|ling)|annotat(?:ed|ing)|"
        r"power(?:ed|ing)|fed|taught|curated|moderat(?:ed|ing))\b"
        r".{0,80}?"
        r"\b(?:AI|artificial intelligence|model|algorithm|system|bot|"
        r"machine learning|neural network|automation|software)s?\b"
        r".{0,200}?"
        r"\b(?:replac(?:ed?|ing|ement)|eliminat(?:ed?|ing)|"
        r"laid off|made redundant|displac(?:ed?|ing)|"
        r"automat(?:ed?|ing)|render(?:ed?|ing) (?:them |their )?obsolete|"
        r"expendable|no longer need(?:ed)?|"
        r"left behind|cut|job losses|losing their (?:jobs?|roles?))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Reverse: "replaced/face replacement ... by the very/same/those
    #  [models/systems/AI] they [trained/built/helped]"
    re.compile(
        r"\b(?:replac(?:ed?|ing|ement)|displac(?:ed?|ing)|"
        r"made (?:them )?redundant|losing (?:their )?jobs?)\b"
        r".{0,120}?"
        r"\b(?:the very|those same|the same|those|the)\b"
        r".{0,40}?"
        r"\b(?:model|system|bot|AI|algorithm|tool|software|"
        r"machine|technology|platform)s?\b"
        r".{0,60}?"
        r"\b(?:they |their |these workers |the workers )?"
        r"(?:train(?:ed|ing)|built|creat(?:ed|ing)|develop(?:ed|ing)|"
        r"help(?:ed)? (?:build|train|create|develop)|"
        r"label(?:ed|led)|annotat(?:ed)|power(?:ed))\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Compact form: "face replacement by those same systems" or
    # "their replacements are the very models they helped build"
    re.compile(
        r"\b(?:replacements?|replaced)\b"
        r".{0,30}?"
        r"\b(?:by those same|by the very|are the very|are the same)\b"
        r".{0,60}?"
        r"\b(?:model|system|bot|AI|algorithm|tool|software|"
        r"machine|technology)s?\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Chant/slogan form: "We trained the [bots/AI]. ... left behind"
    re.compile(
        r"\b[Ww]e\s+(?:train(?:ed)|built|creat(?:ed)|power(?:ed)|"
        r"scrub(?:bed)?|label(?:ed|led))\s+the\s+"
        r"(?:bots?|models?|systems?|AI|algorithms?|feeds?|data)\b"
        r".{0,120}?"
        r"\b(?:left behind|being (?:left|replaced|cut|let go|tossed)|"
        r"now (?:we(?:'re| are)|they(?:'re| are))\b"
        r".{0,40}?"
        r"(?:expendable|redundant|unemployed|replaced|gone|out))",
        re.IGNORECASE | re.DOTALL,
    ),
]

_DEVICE_PATTERNS["worker_replacement_irony"] = _WORKER_REPLACEMENT_IRONY_PATTERNS


# ---------------------------------------------------------------------------
# Two-tier treatment: editorial framing that explicitly contrasts the
# treatment of two classes of workers — typically full-time employees vs.
# contractors, permanent staff vs. outsourced labor.  The device works by
# laying out both packages/conditions side by side so the reader draws
# the inequality conclusion.
#
# Distinct from juxtaposition (which contrasts company profits vs.
# worker losses) and hypocrisy_frame (which contrasts stated values vs.
# actual behavior).  Two-tier treatment is specifically about different
# treatment of different groups of people within the same entity.
#
# Identified in WebProNews Meta Dublin contractors article (May 2026):
#   "Full-time employees reportedly stand to receive four months' pay
#    plus two weeks for every year served. Covalen workers get far less."
#   "they're constantly using Meta tools, they're on Meta platforms ...
#    But they're denied all the privileges and benefits of Meta staff."
# ---------------------------------------------------------------------------
_TWO_TIER_TREATMENT_PATTERNS: list[re.Pattern] = [
    # "[full-time/permanent/direct] employees/staff ... [receive/get X] ...
    #  [contractors/outsourced/temp] ... [get/receive far less/nothing]"
    re.compile(
        r"\b(?:full[- ]time|permanent|direct|internal|salaried)\s+"
        r"(?:employee|staff|worker|personnel|team member)\w*\b"
        r".{0,300}?"
        r"\b(?:contract(?:or|ed)|outsourc(?:ed|ing)|temp(?:orary)?|"
        r"third[- ]party|vendor|agency|gig|contingent)\s+"
        r"(?:worker|employee|staff|personnel|labou?r)\w*\b"
        r".{0,120}?"
        r"\b(?:get|receive|earn|are (?:paid|given|offered|entitled to))\s+"
        r"(?:far )?"
        r"(?:less|nothing|no(?:thing| payout| severance| compensation)|"
        r"the (?:bare |legal )?minimum)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Reverse order: contractors described, then contrast with full-time
    re.compile(
        r"\b(?:contract(?:or|ed)|outsourc(?:ed|ing)|temp(?:orary)?|"
        r"third[- ]party|vendor|agency)\s+"
        r"(?:worker|employee|staff|personnel|labou?r)\w*\b"
        r".{0,200}?"
        r"\b(?:while|whereas|but|in contrast|unlike|compared to|"
        r"could not be (?:more |starker|clearer)|"
        r"the contrast|stark(?:er|ly)?)\b"
        r".{0,150}?"
        r"\b(?:full[- ]time|permanent|direct|internal|salaried)\s+"
        r"(?:employee|staff|worker|personnel)\w*\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "denied all the privileges/benefits of [company] staff/employees"
    re.compile(
        r"\b(?:denied|excluded from|shut out of|lack(?:ing)?|"
        r"without access to|not entitled to|ineligible for)\b"
        r".{0,60}?"
        r"\b(?:all |every )?(?:the )?"
        r"(?:privileges?|benefits?|protections?|rights?|perks?|"
        r"compensation|severance|healthcare)\b"
        r".{0,60}?"
        r"\b(?:of|that|available to|enjoyed by|afforded to|"
        r"given to|provided to)\b"
        r".{0,40}?"
        r"\b(?:staff|employee|full[- ]time|permanent|direct|internal)\w*\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "using [company] tools/platforms ... but ... not [company] employees"
    # Captures the ambiguity-of-employment frame.  Handles both explicit
    # conjunction ("but not employees") and implicit contrast within the
    # same sentence ("using X's tools... are not actually employees").
    re.compile(
        r"\b(?:using|on|work(?:ing)? (?:on|with|for)|access(?:ing)?)\b"
        r".{0,40}?"
        r"\b(?:tools?|platforms?|systems?|software|infrastructure|"
        r"office|building|equipment)\b"
        r".{0,200}?"
        r"\b(?:not (?:actually )?(?:employees?|staff|workers?)|"
        r"aren.?t (?:even )?(?:employees?|staff)|"
        r"not (?:considered|treated as|classified as))\b",
        re.IGNORECASE | re.DOTALL,
    ),
]

_DEVICE_PATTERNS["two_tier_treatment"] = _TWO_TIER_TREATMENT_PATTERNS


# --- Regulatory favoritism: "picking winners and losers" and related ---
# Detects political power-frame rhetoric used in regulatory/policy coverage.
# Common in articles about government intervention in tech industries, where
# the frame implies arbitrary or politically motivated selection.
_REGULATORY_FAVORITISM_PATTERNS: list[re.Pattern] = [
    # "pick(ing) winners and losers"
    re.compile(
        r"\bpick(?:ing|s|ed)?\s+winners?\s+and\s+losers?\b",
        re.IGNORECASE,
    ),
    # "choosing/decide who wins" — paraphrases of the same frame
    re.compile(
        r"\b(?:choos(?:ing|es?)|decid(?:ing|es?)|determin(?:ing|es?))\s+"
        r"(?:which\s+(?:companies?|firms?|players?)|who)\s+"
        r"(?:wins?|loses?|succeeds?|fails?|survives?|thrives?)\b",
        re.IGNORECASE,
    ),
    # "favorable/preferential treatment" — explicit favoritism framing
    re.compile(
        r"\b(?:favorable|favourable|preferential|special|privileged)\s+"
        r"treatment\b",
        re.IGNORECASE,
    ),
    # "tilting the playing field" / "uneven playing field"
    re.compile(
        r"\b(?:tilt(?:ing|ed|s)?|uneven|unlevel)\s+"
        r"(?:the\s+)?playing\s+field\b",
        re.IGNORECASE,
    ),
    # "the government is/was picking customers" — direct Altman quote pattern
    re.compile(
        r"\b(?:government|administration|White House|regulators?)\s+"
        r"(?:is|are|was|were)\s+picking\s+"
        r"(?:customers?|partners?|companies?)\b",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["regulatory_favoritism"] = _REGULATORY_FAVORITISM_PATTERNS


# --- Escalation amplification: intensifying modifiers before threat terms ---
# Detects editorial amplification where modifiers like "escalating,"
# "increasingly," "growing," "deepening" precede threat/concern/crisis
# language, creating a sense of mounting danger that may exceed what the
# sourced facts support.
_ESCALATION_AMPLIFICATION_PATTERNS: list[re.Pattern] = [
    # "escalating/growing/deepening" + threat noun
    re.compile(
        r"\b(?:escalat(?:ing|ed)|deepen(?:ing|ed)|intensif(?:ying|ied)|"
        r"worsen(?:ing|ed)|compound(?:ing|ed))\s+"
        r"(?:concern|threat|risk|danger|crisis|tension|conflict|"
        r"fear|worry|alarm|anxiety|unease|backlash|pressure|"
        r"confrontation|standoff|dispute)s?\b",
        re.IGNORECASE,
    ),
    # "increasingly" + adjective describing negative state
    re.compile(
        r"\bincreasingly\s+"
        r"(?:concerned|worried|alarmed|hostile|aggressive|"
        r"adversarial|contentious|fraught|volatile|dangerous|"
        r"uncomfortable|ominous|dire|urgent|desperate|anxious|"
        r"combative|confrontational|polarized|skeptical|wary)\b",
        re.IGNORECASE,
    ),
    # "growing/rising/surging" + negative abstract noun
    re.compile(
        r"\b(?:growing|rising|surging|swelling|ballooning|mushrooming)\s+"
        r"(?:concern|unease|alarm|anxiety|distrust|suspicion|"
        r"skepticism|opposition|resistance|backlash|hostility|"
        r"frustration|anger|outrage|fear|worry|tension|"
        r"discontent|resentment)s?\b",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["escalation_amplification"] = _ESCALATION_AMPLIFICATION_PATTERNS


# ---------------------------------------------------------------------------
# Commodification / dehumanization metaphor: framing that reduces human
# qualities, labor, or identity to mechanical, digital, or industrial units.
#
# Distinct from worker_replacement_irony (which focuses on the irony of
# workers training their own replacements). This device captures language
# that flattens human identity or work into interchangeable modules, tokens,
# data points, or raw material — making humans sound like inputs to a
# system rather than people.
#
# Identified in MIT Tech Review "Chinese tech workers training AI doubles":
#   "distill their colleagues' skills and personality traits"
#   "flattened into modules in a way that made the worker easier to replace"
#   "a cold farewell can be turned into warm tokens"
#   "reducing a person to a skill"
# Also: "digital humans" (Nvidia), "human capital" used literally,
# workers described as "data", "inputs", "resources" interchangeable
# with software.
# ---------------------------------------------------------------------------
_COMMODIFICATION_METAPHOR_PATTERNS: list[re.Pattern] = [
    # "distill/extract [person/colleague/worker] ... into [skills/tasks/modules]"
    re.compile(
        r"\b(?:distill|extract|boil down|reduce|flatten|compress|"
        r"condense|decompose|break down|abstract|encode|codify|"
        r"serialize|tokenize|quantize)\b"
        r".{0,80}?"
        r"\b(?:colleague|coworker|co-worker|worker|employee|person|"
        r"people|human|individual|teammate|staff)s?\b"
        r".{0,80}?"
        r"\b(?:skill|task|module|token|data|blueprint|manual|"
        r"workflow|process|function|component|unit|input|asset)s?\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "reducing a person/worker to a [skill/module/function/task]"
    re.compile(
        r"\breducing\s+(?:a\s+)?(?:person|worker|employee|colleague|"
        r"human|individual|coworker|co-worker)s?\s+"
        r"to\s+(?:a\s+)?(?:skill|module|function|task|data\s+point|"
        r"token|number|cog|input|unit|component|workflow)s?\b",
        re.IGNORECASE,
    ),
    # "flattened/compressed into modules/tokens/tasks"
    re.compile(
        r"\b(?:their\s+work|their\s+job|their\s+role|"
        r"the\s+worker|the\s+person|their\s+identity)\b"
        r".{0,60}?"
        r"\b(?:flatten(?:ed|ing)?|compress(?:ed|ing)?|"
        r"reduc(?:ed|ing)?|boil(?:ed|ing)?\s+down)\b"
        r".{0,40}?"
        r"\b(?:into|to|as)\b\s+\b(?:module|token|data|"
        r"component|unit|input|task|blueprint|workflow)s?\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "[farewell/goodbye/person/value] ... turned into ... tokens/data/modules"
    re.compile(
        r"\b(?:farewell|goodbye|person|personality|judgment|dignity|"
        r"identity|value|humanity|individuality|experience)\b"
        r".{0,60}?"
        r"\b(?:turn(?:ed|ing)?|convert(?:ed|ing)?|transform(?:ed|ing)?)\b"
        r".{0,40}?"
        r"\b(?:into|to)\b\s+\b(?:warm\s+)?(?:token|data|module|"
        r"code|signal|input|asset|commodity)s?\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "digital [human/worker/employee/colleague]" as euphemism
    re.compile(
        r"\bdigital\s+(?:human|worker|employee|colleague|"
        r"co-worker|coworker|labou?r(?:er)?|twin)s?\b",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["commodification_metaphor"] = _COMMODIFICATION_METAPHOR_PATTERNS

# Analogy/metaphor framing: explicit comparisons using "like", "akin to",
# "equivalent of", "as if" etc. that frame the subject via analogy.
# Distinct from "analogy_stacking" (which requires 3+ analogies).
# Captures single striking analogies used to frame understanding.
_ANALOGY_METAPHOR_PATTERNS: list[re.Pattern] = [
    # "like [verb]ing a [noun]" — simile construction
    re.compile(
        r"\blike\s+(?:crash[- ]testing|stress[- ]testing|auditing|grading|inspecting|"
        r"checking|examining|evaluating|testing|rating|scoring|reviewing)\b",
        re.IGNORECASE,
    ),
    # "like [a/an/the/some/another] [noun phrase]" — general simile construction
    # Requires article or determiner to avoid matching "like" as a verb.
    # Borrowed from analogy_stacking to fire on single striking similes.
    re.compile(
        r"\blike (?:a|an|the|another|some) (?:\w+ ){0,3}\w+",
        re.IGNORECASE,
    ),
    # "almost like" / "kind of like" / "sort of like" — qualified simile
    re.compile(
        r"\b(?:almost|kind of|sort of|a (?:bit|little) )\s*like\b",
        re.IGNORECASE,
    ),
    # "akin to" / "equivalent of" / "tantamount to" — formal analogy
    re.compile(
        r"\b(?:akin to|equivalent of|tantamount to|reminiscent of|analogous to)"
        r"\s+[a-z]",
        re.IGNORECASE,
    ),
    # "comparable to" — formal analogy, but suppress when followed by
    # possessive/determiner pronouns that signal factual benchmark comparison
    # (e.g. "comparable to its previous model" vs "comparable to a war")
    re.compile(
        r"\bcomparable to\s+(?!(?:its|their|the|this|that|our|his|her)\b)[a-z]",
        re.IGNORECASE,
    ),
    # "as if [subject] were [noun/adj]" — hypothetical comparison
    re.compile(
        r"\bas if\s+(?:they|it|the company|the platform|the app)\s+(?:were|was|had)\b",
        re.IGNORECASE,
    ),
]
_DEVICE_PATTERNS["analogy_metaphor"] = _ANALOGY_METAPHOR_PATTERNS

# Taxonomy framing: presenting findings or evidence using a structured
# classification system (e.g. "broken, buried, or missing").  The editorial
# choice to impose a taxonomy implies completeness and authority.
_TAXONOMY_FRAMING_PATTERNS: list[re.Pattern] = [
    # Three-part taxonomy: "X, Y, or Z" / "X, Y, and Z" with editorial categories
    re.compile(
        r"\b(?:broken|failed|missing|buried|hidden|disabled|absent|"
        r"nonfunctional|ineffective|incomplete|inaccessible|"
        r"inadequate|deficient|flawed|defective)"
        r",?\s+(?:or|and)\s+"
        r"(?:broken|failed|missing|buried|hidden|disabled|absent|"
        r"nonfunctional|ineffective|incomplete|inaccessible|"
        r"inadequate|deficient|flawed|defective)\b",
        re.IGNORECASE,
    ),
    # "classified as" / "categorized as" / "fell into [N] categories"
    re.compile(
        r"\b(?:classified|categorized|sorted|grouped|divided)\s+"
        r"(?:as|into)\s+(?:\d+\s+)?(?:categor(?:y|ies)|groups?|tiers?|types?|classes|buckets?)\b",
        re.IGNORECASE,
    ),
    # Three-part comma-separated adjective taxonomy in quotes or emphasis
    re.compile(
        r'["\u201c](?:broken|failed|missing|buried|hidden|disabled|absent|ineffective)',
        re.IGNORECASE,
    ),
]
_DEVICE_PATTERNS["taxonomy_framing"] = _TAXONOMY_FRAMING_PATTERNS


# ---------------------------------------------------------------------------
# Pathologizing metaphor: editorial technique that applies addiction,
# disease, compulsion, or bodily-excess language to corporate or
# institutional behavior.  Frames rational strategic choices (buying
# compute, adopting AI tools) as pathological urges — removing agency
# and creating the impression of an entity out of control.
#
# Distinct from loaded_language (individual loaded words) because these
# form a sustained metaphorical frame, and distinct from analogy_metaphor
# (explicit "like X" comparisons) because pathologizing metaphors are
# asserted as characterization, not acknowledged as analogy.
#
# Discovered via Gizmodo "Meta Reportedly Got Too Addicted to Google AI
# Tokens" article (Jun 29, 2026): headline uses "Addicted" and "Cut Off"
# (intervention language), body uses "gorge itself" (gluttony), "token-
# hungry" (craving), "high-rollers" (gambling compulsion).  None of these
# were detected as framing devices — the toolkit scored only 2 devices
# (ironic_quotation + anonymous_authority) in an article dripping with
# sardonic editorial framing.
# ---------------------------------------------------------------------------
_PATHOLOGIZING_METAPHOR_PATTERNS: list[re.Pattern] = [
    # Addiction/dependency language applied to corporate subjects:
    # "addicted to", "hooked on", "dependent on", "can't quit", "cut off"
    re.compile(
        r"\b(?:addicted to|hooked on|dependent on|"
        r"can.?t (?:quit|stop|resist|help)|"
        r"cut (?:off|them off)|weaned? (?:off|from)|"
        r"kicked the habit|going cold turkey|"
        r"withdrawal|detox(?:ing)?|intervention|"
        r"enabler|enabling|relapse[ds]?)\b",
        re.IGNORECASE,
    ),
    # Gluttony / excess-consumption metaphors:
    # "gorge itself on", "devour", "insatiable", "binge"
    re.compile(
        r"\b(?:gorge[ds]?\s+(?:itself|themselves|himself|herself|on)|"
        r"gorging\s+(?:itself|themselves|on)|"
        r"devour(?:ed|ing|s)?|insatiable|voracious(?:ly)?|"
        r"glutton(?:ous(?:ly)?)?|"
        r"binge[ds]?\s+(?:on|buying|spending|consuming)|"
        r"bingeing|"
        r"feasting\s+on|feeding\s+frenzy|"
        r"(?:swallow|consume|inhale)[ds]?\s+(?:vast|enormous|massive|huge))\b",
        re.IGNORECASE,
    ),
    # Gambling-compulsion metaphors when applied to corporate behavior:
    # "high-rollers", "doubling down" (when implying recklessness),
    # "betting the farm", "all-in"
    re.compile(
        r"\b(?:high[- ]rollers?|"
        r"betting (?:the (?:farm|house|ranch|company)|everything|big)|"
        r"going all[- ]in|"
        r"(?:can.?t|couldn.?t) walk away|"
        r"chasing (?:losses|the high|the rush|the next fix))\b",
        re.IGNORECASE,
    ),
    # Disease / pathology framing:
    # "infected with", "contagion", "epidemic of", "fever"
    re.compile(
        r"\b(?:infected with|afflicted by|suffering from|"
        r"contagion|epidemic of|fever(?:ish)?|"
        r"pathological(?:ly)?|compulsive(?:ly)?|"
        r"obsess(?:ed|ive(?:ly)?|ion|ing))\b"
        r"(?=.{0,60}?"
        r"\b(?:AI|spending|invest|buy|acqui|data|compute|"
        r"growth|scaling|expansion|token|model))",
        re.IGNORECASE | re.DOTALL,
    ),
]
_DEVICE_PATTERNS["pathologizing_metaphor"] = _PATHOLOGIZING_METAPHOR_PATTERNS


# --- Anthropomorphization / Personification ---
# Detects language that ascribes human emotions, intentions, cognition,
# or social roles to AI systems, algorithms, or software tools — framing
# them as autonomous agents with inner lives rather than engineered artifacts.
#
# Central technique in AI coverage where journalists:
# 1. Attribute emotions: AI "happily," "eagerly," "cheerfully" acts
# 2. Ascribe cognition: AI "thinks," "knows," "believes," "understands"
# 3. Assign intentionality: AI "decides," "chooses," "refuses," "wants"
# 4. Cast in human roles: AI as "colleague," "employee," "coworker"
# 5. Attribute social behavior: AI "lies," "deceives," "cooperates"
#
# EXCLUSIONS (to avoid false positives):
# - Standard ML terminology: "the model learned," "trained on" (training is
#   standard CS usage, not personification in context)
# - Product names: "AI assistant" (marketing term, not editorial framing)
# - Direct quotes from company representatives (framing by source, not journalist)
#
# Identified as high-value open issue in Malwarebytes article analysis
# (2026-07-01 01:00 PT Type A): "happily handed," "took that brief a little
# too seriously," "the confused bot," "without being taught" — all undetected.
_ANTHROPOMORPHIZATION_PATTERNS: list[re.Pattern] = [
    # Pattern 1: Emotional-adverb + verb — AI "happily did X," "eagerly processed,"
    # "cheerfully complied," "stubbornly refused," "nervously flagged"
    # The adverb ascribes inner emotional state to software.
    re.compile(
        r"\b(?:the |its |an? |this |that |Meta(?:'s)? |Google(?:'s)? |"
        r"OpenAI(?:'s)? |Anthropic(?:'s)? )?"
        r"(?:AI|bot|chatbot|algorithm|model|system|agent|assistant|tool)"
        r"(?:\s+\w+){0,3}?\s+"
        r"(?:happily|eagerly|cheerfully|enthusiastically|nervously|"
        r"stubbornly|reluctantly|obediently|dutifully|blindly|gleefully|"
        r"helpfully|merrily|willingly|grudgingly)\s+"
        r"(?:\w+(?:ed|s|ing)\b)",
        re.IGNORECASE,
    ),
    # Pattern 2: AI/bot as subject + cognitive/volitional verb
    # "the AI decided," "the bot chose," "the algorithm believes"
    # Catches subject-verb constructions where software is ascribed human cognition.
    re.compile(
        r"\b(?:the |its |an? |this |that )?"
        r"(?:AI|bot|chatbot|algorithm|model|system|agent)"
        r"(?:\s+\w+){0,2}?\s+"
        r"(?:decided|chose|wanted|refused|believed|understood|"
        r"thought|knew|felt|hoped|feared|intended|preferred|"
        r"determined|concluded|judged|recognized|realized|considered)\b",
        re.IGNORECASE,
    ),
    # Pattern 3: "taught" / "taught how to" — learning ascription
    # "without being taught how to verify," "hadn't been taught"
    # Frames engineering gaps as pedagogical failure, implying the AI
    # is a student who wasn't properly educated rather than software
    # missing a conditional check.
    re.compile(
        r"\b(?:without being|hadn't been|wasn't|weren't|never|not)"
        r"\s+(?:taught|told|shown|instructed|trained)\s+"
        r"(?:how to|to|about|that)\b",
        re.IGNORECASE,
    ),
    # Pattern 4: Took-X-too-seriously / went-too-far — intentional-excess ascription
    # "took that brief a little too seriously," "went too far," "got carried away"
    # Frames software behavior as excessive enthusiasm rather than a design flaw.
    re.compile(
        r"\b(?:took (?:that|this|the|its) .{0,30}?"
        r"(?:too (?:seriously|literally|far)|to (?:an |the )extreme)|"
        r"got (?:a (?:little|bit) )?carried away|"
        r"went (?:a (?:little|bit) )?(?:too far|overboard|rogue))\b",
        re.IGNORECASE,
    ),
    # Pattern 5: "confused" / "bewildered" / "fooled" — state-of-mind ascription
    # "the confused bot," "a bewildered AI," "the model was fooled"
    # Attributes a psychological state to software.
    re.compile(
        r"\b(?:the |a |an? )?(?:confused|bewildered|baffled|puzzled|"
        r"clueless|gullible|naive|oblivious|unsuspecting|trusting)"
        r"\s+(?:AI|bot|chatbot|algorithm|model|system|agent|assistant)\b",
        re.IGNORECASE,
    ),
    # Pattern 6: Human role/identity casting
    # "digital employee," "AI colleague," "robot coworker," "machine worker"
    # "virtual teammate," "silicon assistant" (metaphorical, not product names)
    re.compile(
        r"\b(?:digital|virtual|silicon|robotic?|AI|machine|automated?)"
        r"\s+(?:employee|colleague|coworker|co-worker|teammate|"
        r"team member|worker|workforce|staff(?:er)?|intern|"
        r"junior|contractor|recruit|hire|deputy|subordinate)\b",
        re.IGNORECASE,
    ),
]
_DEVICE_PATTERNS["anthropomorphization"] = _ANTHROPOMORPHIZATION_PATTERNS


# --- Assumed consensus ---
# Editorial device that presents a contested or unsupported claim as
# self-evident common knowledge.  Constructions like "People hate X",
# "Everyone knows X", "Nobody wants X" skip the burden of proof and
# position the audience as already agreeing with the author's stance.
# Distinct from loaded_language (which uses pejorative vocabulary) and
# emotional_appeal (which deploys sympathy/outrage): assumed_consensus
# frames the *audience* as unanimous rather than deploying emotion.
#
# Gap discovered during Gizmodo Meta glasses subscription analysis
# (Jul 2026): "People hate Meta's smart glasses for quite a few
# reasons" went undetected — a strong consensus assertion with zero
# evidence or citation.
_ASSUMED_CONSENSUS_PATTERNS: list[re.Pattern] = [
    # "People hate/love/want/think X", "Everyone knows/agrees X"
    re.compile(
        r"\b(?:people|everyone|everybody|nobody|no one|we all|"
        r"most people|many people|few people|consumers|users|"
        r"critics|observers|analysts|experts)\s+"
        r"(?:hate|love|want|know|agree|think|feel|believe|"
        r"understand|recognize|see|expected|expect|fear|"
        r"already know|already knew|already see|"
        r"don't want|don't like|don't trust|"
        r"won't accept|won't tolerate)\b",
        re.IGNORECASE,
    ),
    # "It's well known that", "It goes without saying"
    re.compile(
        r"\b(?:it(?:'s| is) (?:well known|widely known|common knowledge|"
        r"no secret|clear|obvious|evident|undeniable|understood|apparent))\b",
        re.IGNORECASE,
    ),
    # "Goes without saying", "Needless to say"
    re.compile(
        r"\b(?:goes without saying|needless to say|"
        r"as (?:everyone|we all|we) (?:know|knew|already know))\b",
        re.IGNORECASE,
    ),
]
_DEVICE_PATTERNS["assumed_consensus"] = _ASSUMED_CONSENSUS_PATTERNS


# --- Editorial aside / direct reader address ---
# Conversational interjections where the author breaks the journalistic
# register to address the reader directly, insert personal commentary,
# or perform rhetorical solidarity ("let's be honest", "brace yourself",
# "something tells me").  These create an in-group frame between author
# and reader that positions the subject as an outsider deserving scrutiny.
# Distinct from loaded_language (vocabulary) and rhetorical_question
# (interrogative form): editorial_aside uses imperative/first-person
# asides in declarative sentences.
#
# Gap discovered during Gizmodo Meta glasses subscription analysis
# (Jul 2026): "brace yourself", "let's be honest here", and
# "something tells me" all went undetected.
_EDITORIAL_ASIDE_PATTERNS: list[re.Pattern] = [
    # Direct reader address: "brace yourself", "buckle up", "spoiler alert"
    re.compile(
        r"\b(?:brace yourself|brace yourselves|buckle up|"
        r"spoiler alert|fair warning|"
        r"get this|get ready|wait for it|"
        r"surprise,? surprise|shocker)\b",
        re.IGNORECASE,
    ),
    # Solidarity/honesty performative: "let's be honest", "let's face it"
    re.compile(
        r"\b(?:let'?s be (?:honest|real|clear|frank|serious)|"
        r"let'?s face it|let'?s not pretend|"
        r"to be (?:honest|fair|frank|blunt)|"
        r"if (?:we'?re|I'?m) being (?:honest|real|frank)|"
        r"I'?ll be (?:honest|real|frank|blunt))\b",
        re.IGNORECASE,
    ),
    # First-person editorial prediction: "something tells me", "I suspect"
    re.compile(
        r"\b(?:something tells me|"
        r"call me (?:crazy|skeptical|cynical|old-fashioned)|"
        r"I (?:suspect|doubt|can't help but|have a feeling)|"
        r"my (?:guess|bet|prediction) is|"
        r"color me (?:surprised|skeptical|unsurprised|shocked))\b",
        re.IGNORECASE,
    ),
    # Parenthetical asides that editorialize: "(yes, really)", "(sigh)"
    re.compile(
        r"\((?:yes,? really|no,? really|sigh|yep|nope|"
        r"shocking,? I know|I know|you read that right|"
        r"seriously|of course)\)",
        re.IGNORECASE,
    ),
    # Sarcastic "Guess..." opener — standalone sentence starting with
    # "Guess" followed by an ironic observation.  Distinct from "I guess"
    # (hedge) or "Guess what" (exclamation).  Discovered in Wired
    # Conversation Focus article (Jul 2026): "Guess humans are better
    # at some things after all."
    re.compile(
        r"(?:^|\.\s+)Guess\s+(?!what\b)(?!who\b)"
        r"[^.?!]{10,80}"
        r"(?:after all|in the end|it turns out|apparently|somehow)"
        r"[.!]",
        re.MULTILINE,
    ),
]
_DEVICE_PATTERNS["editorial_aside"] = _EDITORIAL_ASIDE_PATTERNS


def _detect_analogy_stacking(text: str) -> list[FramingDevice]:
    """Detect analogy stacking — 3+ distinct analogies for the same subject.

    Returns a list of FramingDevice objects (one per matched analogy marker)
    only if the threshold (3+) is met.  If fewer than 3 markers are found,
    returns an empty list.
    """
    markers: list[FramingDevice] = []
    seen_spans: set[tuple[int, int]] = set()

    # Pre-compiled patterns for filtering false positives from analogy markers.
    # Factual similes: "looks like a truck", "something that looks like an X"
    _factual_simile_re = re.compile(
        r"\b(?:look(?:s|ed|ing)?|resembl(?:e[sd]?|ing)|appear(?:s|ed|ing)?|"
        r"seem(?:s|ed|ing)?|sound(?:s|ed|ing)?|found something that look)"
        r"\s+like\b",
        re.IGNORECASE,
    )
    # "recalls that" = memory verb, not evocation ("recalls the era" = evocation)
    _recalls_memory_re = re.compile(
        r"\brecalls?\s+that\b", re.IGNORECASE,
    )

    for pattern in _ANALOGY_MARKER_PATTERNS:
        for match in pattern.finditer(text):
            start, end = match.start(), match.end()

            # Deduplicate overlapping matches
            overlap = False
            for ex_start, ex_end in seen_spans:
                if not (end <= ex_start or start >= ex_end):
                    overlap = True
                    break
            if overlap:
                continue

            # --- False-positive filters ---

            # 1. Factual simile: skip "like a X" when preceded by "looks",
            #    "resembles", "appears", "something that looks", etc.
            matched_text = match.group()
            if "like " in matched_text.lower():
                # Check 30 chars before match for perception verbs
                lookback = text[max(0, start - 30):start + 10].lower()
                if _factual_simile_re.search(lookback):
                    continue

            # 2. Memory "recalls": skip "recalls that" (= remembers),
            #    keep "recalls the era" (= evokes).
            if matched_text.lower().startswith("recalls"):
                if _recalls_memory_re.search(
                    text[start:min(len(text), start + 40)]
                ):
                    continue

            seen_spans.add((start, end))
            evidence = matched_text.strip()
            if len(evidence) > 200:
                evidence = evidence[:200] + "..."

            markers.append(
                FramingDevice(
                    device_type="analogy_stacking",
                    evidence_text=evidence,
                    start=start,
                    end=end,
                )
            )

    # Only fire if 3+ distinct analogy markers are found
    if len(markers) >= 3:
        return markers
    return []


def _detect_speculative_framing(text: str) -> list[FramingDevice]:
    """Detect speculative framing — 5+ cumulative speculative hedges.

    Individual hedges ("could potentially," "might be able to") are standard
    journalism.  When an article accumulates 5+ such constructions, the
    cumulative effect converts possibility into implied inevitability — this
    is an editorial framing technique distinct from individual cautious
    language.

    Returns a list of FramingDevice objects (one per matched hedge) only if
    the threshold (5+) is met.  Below threshold, returns an empty list.
    """
    markers: list[FramingDevice] = []
    seen_spans: set[tuple[int, int]] = set()

    for pattern in _SPECULATIVE_FRAMING_PATTERNS:
        for match in pattern.finditer(text):
            start, end = match.start(), match.end()

            # Deduplicate overlapping matches
            overlap = False
            for ex_start, ex_end in seen_spans:
                if not (end <= ex_start or start >= ex_end):
                    overlap = True
                    break
            if overlap:
                continue

            seen_spans.add((start, end))
            evidence = match.group().strip()
            if len(evidence) > 200:
                evidence = evidence[:200] + "..."

            markers.append(
                FramingDevice(
                    device_type="speculative_framing",
                    evidence_text=evidence,
                    start=start,
                    end=end,
                )
            )

    # Only fire if 5+ distinct speculative markers are found
    if len(markers) >= 5:
        return markers
    return []


# ---------------------------------------------------------------------------
# Trend-Bundling Detection (Post-Pass)
# ---------------------------------------------------------------------------
# Editorial technique where an article groups a target company's action with
# 3+ other companies doing similar things.  The bundling *normalises* the
# target ("everyone is doing it") or *amplifies* ("this is a pattern of
# failure").  Either way the editorial choice to assemble the bundle is a
# framing device, not neutral reporting — a different journalist could
# report the same reversal without surveying the industry.
#
# Trigger: transition phrases ("Other companies have also…", "Similarly,…",
# "X also…", "A broader trend…") that introduce company names not belonging
# to the article's primary subject.  Fires when 3+ distinct company
# comparison markers are found.
#
# Like analogy_stacking, this fires as a post-pass; individual comparisons
# are normal, stacking them is editorial.

_TREND_BUNDLING_TRANSITION_PATTERNS: list[re.Pattern] = [
    # "Other companies have also…"
    re.compile(
        r"\b(?:other\s+compan(?:y|ies)|other\s+(?:tech\s+)?firms|"
        r"other\s+(?:tech\s+)?giants|other\s+organisations?|other\s+organizations?)"
        r"\s+(?:have\s+)?(?:also\s+)?\w+",
        re.IGNORECASE,
    ),
    # "X also walked back / reversed / backtracked / scaled back / paused"
    re.compile(
        r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?\s+also\s+"
        r"(?:walked\s+back|reversed|backtracked|scaled\s+back|paused|"
        r"abandoned|retreated|shelved|pulled\s+back|cut\s+back|"
        r"rolled\s+back|suspended|canceled|cancelled|shut\s+down|"
        r"capped|limited|restricted)\b",
        re.IGNORECASE,
    ),
    # "Similarly, X…" / "Likewise, X…" / "In a similar move, X…"
    re.compile(
        r"(?:^|\.\s+)(?:Similarly|Likewise|In\s+a\s+similar\s+"
        r"(?:move|vein|fashion|spirit|step))\s*,?\s+[A-Z]",
        re.IGNORECASE | re.MULTILINE,
    ),
    # "A broader trend…" / "Part of a broader…" / "a growing trend…"
    re.compile(
        r"\b(?:a\s+)?(?:broader|growing|wider|emerging|larger|accelerating)\s+"
        r"(?:trend|pattern|movement|shift|wave|backlash|reversal|retreat)",
        re.IGNORECASE,
    ),
    # "sparking a trend called…" / "dubbed the…"
    re.compile(
        r"\b(?:sparking|fueling|feeding|driving|dubbed|called|known\s+as)\s+"
        r"(?:a\s+)?(?:trend|movement|backlash|reversal|phenomenon)",
        re.IGNORECASE,
    ),
    # "Some companies are also…" / "Several firms have…"
    re.compile(
        r"\b(?:some|several|many|numerous|a\s+number\s+of|a\s+handful\s+of)\s+"
        r"(?:compan(?:y|ies)|firms?|(?:tech\s+)?giants?|organizations?|organisations?)\s+"
        r"(?:are|have|were)\s+(?:also\s+)?",
        re.IGNORECASE,
    ),
    # "across varying sectors" / "across the industry" / "industry-wide"
    re.compile(
        r"\b(?:across\s+(?:varying|different|multiple|the)\s+"
        r"(?:sectors?|industries|companies|firms)|"
        r"industry.?wide|sector.?wide)\b",
        re.IGNORECASE,
    ),
]

# Company names used as comparison targets — we look for these in
# sentences containing transition markers.  We use a broad list of
# well-known tech and non-tech companies likely to appear in trend
# bundles.  Matches are case-sensitive to avoid false positives from
# common words.
_TREND_BUNDLING_COMPANY_PATTERN: re.Pattern = re.compile(
    r"\b("
    r"Google|Alphabet|Amazon|Microsoft|Apple|Meta|Facebook|"
    r"Netflix|Nvidia|Tesla|SpaceX|OpenAI|Anthropic|"
    r"Uber|Lyft|Airbnb|Spotify|Snap|Snapchat|Pinterest|"
    r"Salesforce|Adobe|IBM|Oracle|Intel|AMD|Qualcomm|"
    r"Twitter|X Corp|TikTok|ByteDance|Samsung|Sony|"
    r"Duolingo|Shopify|Stripe|Square|Block|Palantir|"
    r"Zoom|Slack|Dropbox|Coinbase|Robinhood|"
    r"Goldman Sachs|JPMorgan|Morgan Stanley|"
    r"Disney|Warner|Comcast|Paramount|"
    r"Boeing|Lockheed|Raytheon|General Electric|"
    r"Walmart|Target|Costco|Home Depot"
    r")\b"
)


def _detect_trend_bundling(text: str) -> list[FramingDevice]:
    """Detect trend bundling — 3+ distinct companies bundled as comparisons.

    Returns a list of FramingDevice objects (one per transition-marker
    match) only if the article contains 3+ distinct company-comparison
    mentions in transition contexts.  If fewer than 3 distinct companies
    are found in bundling contexts, returns an empty list.
    """
    markers: list[FramingDevice] = []
    bundled_companies: set[str] = set()

    # For each transition pattern, find its matches and check for company
    # names within the surrounding sentence (±300 chars).
    for pattern in _TREND_BUNDLING_TRANSITION_PATTERNS:
        for match in pattern.finditer(text):
            start, end = match.start(), match.end()

            # Expand to sentence-level context (±300 chars)
            ctx_start = max(0, start - 100)
            ctx_end = min(len(text), end + 300)
            context = text[ctx_start:ctx_end]

            # Find company names in the context
            companies_in_ctx = set()
            for co_match in _TREND_BUNDLING_COMPANY_PATTERN.finditer(context):
                companies_in_ctx.add(co_match.group())

            if companies_in_ctx:
                bundled_companies.update(companies_in_ctx)

                evidence = match.group().strip()
                if len(evidence) > 200:
                    evidence = evidence[:200] + "..."

                markers.append(
                    FramingDevice(
                        device_type="trend_bundling",
                        evidence_text=evidence,
                        start=start,
                        end=end,
                    )
                )

    # Also scan for paragraph-level company bundles without explicit
    # transition phrases.  If a single paragraph names 3+ companies in
    # constructions like "X did A. Y did B. Z did C." the paragraph
    # itself is a trend bundle.  To avoid false positives on factual
    # enumerations (e.g. "OpenAI, Google, and Microsoft have submitted
    # their models"), we require the paragraph to also contain comparison
    # or reversal language — evidence that the enumeration is being used
    # to normalise or amplify a pattern, not just report a list.
    _BUNDLING_ACTION_RE = re.compile(
        r"\b(?:also|similarly|likewise|too|as\s+well|in\s+turn|"
        r"walked\s+back|reversed|backtracked|retreated|"
        r"scaled\s+back|pulled\s+back|rolled\s+back|"
        r"shut\s+down|capped|limited|restricted|"
        r"paused|suspended|canceled|cancelled|"
        r"rehired|boomerang|trend|pattern|wave|backlash)\b",
        re.IGNORECASE,
    )
    paragraphs = text.split("\n\n")
    offset = 0
    for para in paragraphs:
        companies_in_para = set(
            m.group() for m in _TREND_BUNDLING_COMPANY_PATTERN.finditer(para)
        )
        if len(companies_in_para) >= 3 and _BUNDLING_ACTION_RE.search(para):
            bundled_companies.update(companies_in_para)
            # Only add a marker if we haven't already captured this region
            para_start = text.find(para, offset)
            if para_start >= 0:
                already_covered = any(
                    m.start >= para_start and m.start < para_start + len(para)
                    for m in markers
                )
                if not already_covered:
                    evidence = para[:200] + "..." if len(para) > 200 else para
                    markers.append(
                        FramingDevice(
                            device_type="trend_bundling",
                            evidence_text=evidence.strip(),
                            start=para_start,
                            end=para_start + len(para),
                        )
                    )
        offset = text.find(para, offset) + len(para) if text.find(para, offset) >= 0 else offset

    # Only fire if 3+ distinct companies are bundled
    if len(bundled_companies) >= 3:
        return markers
    return []


# --- Social proof amplification ---
# Detects when articles cite reaction counts (likes, thumbs-up, hearts,
# upvotes, shares) to amplify a quoted position — converting one person's
# opinion into collective sentiment.
_SOCIAL_PROOF_PATTERNS: list[re.Pattern] = [
    # "drew more than 200 thumbs-up and heart reactions"
    re.compile(
        r"(?:drew|received|garnered|got|attracted|earned|accumulated)"
        r"\s+(?:more\s+than\s+|over\s+|nearly\s+|about\s+|around\s+)?"
        r"\d[\d,]*\s+"
        r"(?:thumbs[- ]?up|heart|like|reaction|upvote|share|retweet|repost|comment)",
        re.IGNORECASE,
    ),
    # "a comment that drew more than N reactions"
    re.compile(
        r"(?:comment|post|message|reply)\s+that\s+"
        r"(?:drew|received|garnered|got|attracted|earned)\s+"
        r"(?:more\s+than\s+|over\s+|nearly\s+)?\d[\d,]*\s+"
        r"(?:thumbs[- ]?up|heart|like|reaction|upvote|share)",
        re.IGNORECASE,
    ),
    # "Dozens of people also reacted with X"
    re.compile(
        r"(?:dozens|hundreds|thousands|scores|many|numerous)\s+"
        r"(?:of\s+)?(?:people|employees|users|workers|commenters|respondents)"
        r"\s+(?:also\s+)?(?:reacted|responded|replied|commented)",
        re.IGNORECASE,
    ),
    # Poll/survey-based social proof — citing poll percentages or
    # respondent fractions to amplify a position as collective sentiment.
    # Distinct from reaction-count social proof: these cite formal surveys
    # or polls rather than social media engagement metrics.
    # Discovered via MIT TR "Resistance" article (Apr 2026):
    #   "half of Americans are concerned"
    #   "three-quarters of Americans worry"
    # Also common in tech policy coverage citing Pew, Gallup, etc.
    re.compile(
        r"\b(?:a\s+)?(?:(?:Pew|Gallup|YouGov|Reuters|Harris|Morning\s+Consult|Ipsos)"
        r"\s+)?(?:poll|survey|study|research|report)\s+"
        r"(?:found|shows?|revealed?|indicates?|suggests?)\s+"
        r"(?:that\s+)?(?:(?:half|a\s+(?:majority|quarter|third))\s+of|"
        r"\d+(?:\.\d+)?%\s+of|"
        r"(?:nearly|almost|more\s+than|over|roughly|about|approximately)\s+"
        r"(?:half|a\s+(?:majority|quarter|third)))",
        re.IGNORECASE,
    ),
    # Fraction-as-headline social proof: "half of Americans",
    # "three-quarters of Americans", "two-thirds of respondents"
    # deployed as standalone social proof without explicitly naming
    # the survey (the source is implied by structure).
    re.compile(
        r"\b(?:half|a\s+majority|two[- ]thirds?|three[- ]quarters?|"
        r"one[- ](?:third|quarter|half)|four[- ]fifths?|nine[- ]tenths?)\s+"
        r"of\s+(?:Americans?|respondents?|(?:all\s+)?(?:adults?|voters?|"
        r"people|consumers?|(?:US|U\.S\.|British|European)\s+(?:adults?|voters?|people)))"
        r"\s+(?:are|were|say|said|believe|believed|worry|worried|think|thought|"
        r"fear|feared|support|supported|oppose|opposed|"
        r"(?:are|were)\s+concerned|(?:are|were)\s+worried|(?:have|has)\s+concerns?)",
        re.IGNORECASE,
    ),
]


def _detect_social_proof_amplification(text: str) -> list[FramingDevice]:
    """Detect social proof amplification — citing reaction counts
    to amplify quoted positions."""
    devices: list[FramingDevice] = []
    for pattern in _SOCIAL_PROOF_PATTERNS:
        for m in pattern.finditer(text):
            devices.append(
                FramingDevice(
                    device_type="social_proof_amplification",
                    evidence_text=m.group(0),
                    start=m.start(),
                    end=m.end(),
                )
            )
    return devices


# --- Industry normalization undercut ---
# Acknowledges that a practice is industry-wide then immediately undercuts
# the normalization to single out the target.  E.g., "Other companies
# also use contractors, but Meta's reliance is especially troubling."
# The rhetorical move is: admit the norm to appear fair, then negate it.
_INDUSTRY_NORMALIZATION_UNDERCUT_PATTERNS: list[re.Pattern] = [
    # "Other companies [also/too] X, but [Target] Y" / "while [Target] Y"
    re.compile(
        r"\b(?:other companies|other tech (?:companies|giants|firms)|"
        r"rivals?|competitors?|the industry|the sector|"
        r"companies (?:like|such as)|other (?:platforms?|services?))\b"
        r"[^.]{0,100}?"
        r"\b(?:but|yet|however|though|although|still|nonetheless|"
        r"while|whereas|nevertheless|even so)\b"
        r"[^.]{0,100}?"
        r"\b(?:especially|particularly|uniquely|notably|"
        r"stands? out|far more|far worse|worse|worst|"
        r"most egregious|most troubling|most alarming|"
        r"most significant|most concerning|goes? further|"
        r"dwarfs?|exceeds?|outpaces?|outstrips?|pales?)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "is not unique to [Target], but [Target]'s" / "is not alone in ... but"
    re.compile(
        r"\b(?:is|are|was|were) (?:not |hardly |far from )?"
        r"(?:unique|alone|the only (?:one|company|platform|firm))"
        r"\b[^.]{0,80}?"
        r"\b(?:but|yet|however|though)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "industry-wide/common practice ... but [qualifier]"
    re.compile(
        r"\b(?:industry[- ]wide|common practice|standard practice|"
        r"widespread|not uncommon|routine|commonplace)\b"
        r"[^.]{0,100}?"
        r"\b(?:but|yet|however|though|although|still|nonetheless)\b"
        r"[^.]{0,80}?"
        r"\b(?:scale|scope|extent|degree|magnitude|"
        r"especially|particularly|uniquely|notably)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "[Target] is not the only ... but its [negative qualifier]"
    re.compile(
        r"\b(?:not the only|not alone in|others? (?:also|too))\b"
        r"[^.]{0,120}?"
        r"\bits?\s+(?:scale|scope|approach|reliance|dependence|"
        r"involvement|track record|handling)\b"
        r"[^.]{0,60}?"
        r"\b(?:raises?|troubl\w*|alarm\w*|concern\w*|question\w*|problematic|"
        r"unprecedented|extraordinary|extreme)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # --- Cross-sentence normalization undercut ---
    # Catches the pattern where normalization ("not unusual", "not uncommon",
    # "industry-standard", etc.) appears in one sentence, and the undercut
    # ("But ..." + negative characterization) starts the next sentence.
    # Discovered via the Wired Cannes/contractors/teens article (2026-07):
    #   "Testing competitors' products is not, by itself, unusual in the
    #    artificial intelligence industry. ... But Cannes struck contractors
    #    as an odd way for a trillion-dollar company..."
    # The `[^.]{0,N}` guards in earlier patterns can't cross the period
    # boundary, so this variant uses `.{0,N}` with DOTALL and requires
    # the "But" (or "Yet"/"However") to follow a sentence-ending period.
    re.compile(
        r"\b(?:is|are|was|were)\s+not[\s,]+(?:by itself[\s,]+)?"
        r"(?:unusual|uncommon|unique|unknown|unheard[\s-]of|unprecedented|"
        r"out of the ordinary)\b"
        r".{0,300}?"
        r"(?:\.|\?|!)\s+"
        r"(?:But|Yet|However|Still|Nonetheless|Nevertheless)\s+"
        r"[^.]{0,200}?"
        r"\b(?:odd|strange|unusual|questionable|troubl\w*|concern\w*|"
        r"rais(?:es?|ing) questions?|crude|extreme|problematic|"
        r"alarming|striking|remarkable|striking|eyebrow|"
        r"unprecedented|extraordinary|excessive)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "not unusual/uncommon" within same sentence + "but" qualifier
    # (extends existing patterns to cover "unusual" alongside "uncommon")
    re.compile(
        r"\b(?:not\s+(?:unusual|uncommon|unheard[\s-]of))\b"
        r"[^.]{0,100}?"
        r"\b(?:but|yet|however|though|although|still|nonetheless)\b"
        r"[^.]{0,80}?"
        r"\b(?:scale|scope|extent|degree|magnitude|"
        r"especially|particularly|uniquely|notably)\b",
        re.IGNORECASE | re.DOTALL,
    ),
]
_DEVICE_PATTERNS["industry_normalization_undercut"] = (
    _INDUSTRY_NORMALIZATION_UNDERCUT_PATTERNS
)


# ---------------------------------------------------------------------------
# Slippery slope / precedent-setting framing: editorial device that
# extrapolates from a specific corporate action to a broader threat,
# using language like "sets a precedent", "if this extends to",
# "could end up paying".  Common in consumer-tech coverage when a
# company introduces a new monetization or restriction pattern.
# ---------------------------------------------------------------------------
_SLIPPERY_SLOPE_PATTERNS: list[re.Pattern] = [
    # "sets a/an [adj] precedent" or "creates a/an [adj] precedent"
    re.compile(
        r"\b(?:sets?|creat(?:es?|ing)|establish(?:es|ing)?)\s+"
        r"(?:a |an )"
        r"(?:dangerous|uncomfortable|troubling|worrying|concerning|"
        r"alarming|chilling|disturbing|bad|terrible|"
        r"problematic|questionable|risky)\s+"
        r"precedent\b",
        re.IGNORECASE,
    ),
    # "if this [approach/model/trend] extends/spreads/continues"
    re.compile(
        r"\bif\s+(?:this|that|the|such)\s+"
        r"(?:approach|model|trend|pattern|practice|strategy|policy|"
        r"move|shift|change|decision|tactic)\s+"
        r"(?:extends?|spreads?|continues?|expands?|catches? on|"
        r"becomes? (?:the )?(?:norm|standard|common|widespread))\b",
        re.IGNORECASE,
    ),
    # "could end up [paying/losing/facing]" — projected negative consumer outcome
    re.compile(
        r"\b(?:users?|consumers?|customers?|owners?|subscribers?|people|you)\s+"
        r"(?:could|may|might|would|will)\s+"
        r"(?:end up|eventually|ultimately|soon)\s+"
        r"(?:paying|losing|facing|being (?:forced|required|asked)|"
        r"having to|needing to)\b",
        re.IGNORECASE,
    ),
    # "opens the door to" / "paves the way for" — gateway framing
    re.compile(
        r"\b(?:opens? the door|paves? the way|lays? the groundwork|"
        r"clears? (?:the|a) path)\s+"
        r"(?:to|for)\s+.{5,80}?"
        r"\b(?:more|additional|further|future|other|broader)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "implying that other [features/services] may be [restricted]" —
    # editorial interpretation of corporate hedging as future-threat signal.
    # Unlike the above patterns which detect the author's own extrapolation,
    # this detects when the author interprets a corporate qualifier
    # ("currently") as evidence of expansion plans.
    # Discovered in 9to5Mac Conversation Focus analysis (Jul 2026):
    # "implying that other AI features may be rate-limited in future"
    re.compile(
        r"\b(?:implying|suggesting|hinting|signaling|indicating)\s+"
        r"(?:that )?(?:other|more|additional|further|future)\s+"
        r"(?:\w+\s+){0,3}"
        r"(?:may|might|could|will|would)\s+"
        r"(?:also |soon |eventually |likewise )?"
        r"(?:be |get |become )?"
        r"(?:rate[- ]limited|paywalled|restricted|limited|capped|throttled|"
        r"locked|gated|charged|monetized)\b",
        re.IGNORECASE,
    ),
]
_DEVICE_PATTERNS["slippery_slope"] = _SLIPPERY_SLOPE_PATTERNS


# ---------------------------------------------------------------------------
# Consumer ownership framing: editorial device that frames a corporate
# restriction on a product as a violation of what the consumer "already
# paid for" or "already owns".  Invokes ownership rights to amplify
# consumer grievance, common in hardware subscription / DRM debates.
# ---------------------------------------------------------------------------
_CONSUMER_OWNERSHIP_PATTERNS: list[re.Pattern] = [
    # "hardware/device/product you've already paid for"
    re.compile(
        r"\b(?:hardware|device|product|gadget|equipment|glasses|headset|phone)\s+"
        r"(?:you(?:'ve| have) already|they(?:'ve| have) already|"
        r"that(?:'s| is| was) already|already)\s+"
        r"(?:paid for|purchased|bought|own(?:ed)?)\b",
        re.IGNORECASE,
    ),
    # Company-voice variant: "product it already sold to customers"
    # The article frames the company as having sold the product, inverting
    # the ownership voice while making the same consumer-rights argument.
    # Discovered in 9to5Mac Conversation Focus analysis (Jul 2026).
    re.compile(
        r"\b(?:hardware|device|product|gadget|equipment|glasses|headset|phone)\s+"
        r"(?:it|they|the company|Meta|Apple|Google|Amazon)\s+"
        r"(?:already |has already |have already )?"
        r"(?:sold|shipped|delivered|marketed)\s+"
        r"(?:to )?(?:customers?|consumers?|users?|buyers?|owners?|people)\b",
        re.IGNORECASE,
    ),
    # "features [their/your/the] [device/hardware] already [supports/has]"
    re.compile(
        r"\b(?:features?|capabilities?|functions?|tools?)\s+"
        r"(?:that )?(?:their|your|the|its)\s+"
        r"(?:device|hardware|glasses|phone|headset|product)s?\s+"
        r"(?:already )?(?:supports?|has|have|includes?|provides?|"
        r"is capable of|can (?:already )?(?:do|run|handle))\b",
        re.IGNORECASE,
    ),
    # "runs [entirely/completely] on [the/your] [device/hardware]" near
    # "pay/subscription/fee/charge"
    re.compile(
        r"\bruns?\s+(?:entirely|completely|fully|wholly|natively|locally)\s+"
        r"(?:on[- ](?:the\s+|your\s+|its\s+|their\s+)?"
        r"(?:device|hardware|glasses|phone|chip|processor)\b)"
        r".{0,200}?"
        r"\b(?:pay|subscription|fee|charge|monetiz|paywall|premium|"
        r"upgrade|billing)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "runs on-device" without adverb — same concept, shorter phrasing.
    # Wired Conversation Focus article (Jul 2026) uses "the Conversation
    # Focus feature runs on-device, meaning it doesn't need to head to
    # Meta's servers" without an adverb like "entirely."  The proximity
    # window is extended to 300 chars because the subscription context
    # may be a sentence or two away.
    re.compile(
        r"\bruns?\s+on[- ]device\b"
        r".{0,300}?"
        r"\b(?:pay|subscription|fee|charge|monetiz|paywall|premium|"
        r"upgrade|billing)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "uses on-device processing" variant — same concept, different phrasing
    # Discovered in 9to5Mac Conversation Focus analysis (Jul 2026).
    re.compile(
        r"\b(?:uses?|leverages?|relies? on|employs?)\s+"
        r"(?:on[- ]device|local|offline|edge)\s+"
        r"(?:processing|computation|inference|AI|model)\b"
        r".{0,200}?"
        r"\b(?:pay|subscription|fee|charge|monetiz|paywall|premium|"
        r"upgrade|billing)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Reverse order: subscription/pay near "on-device/local/on the hardware"
    re.compile(
        r"\b(?:pay|subscription|fee|charge|paywall|premium)\b"
        r".{0,200}?"
        r"\b(?:runs?\s+(?:entirely|completely|fully)\s+on|"
        r"on[- ]device|local(?:ly)?|"
        r"(?:works?|runs?|operates?|functions?)\s+(?:entirely\s+)?on\s+(?:the|your|its)\s+"
        r"(?:device|hardware|glasses|phone)|"
        r"doesn'?t (?:require|need|use)\s+(?:the |an )?"
        r"(?:internet|cloud|server|connection)|"
        r"doesn'?t (?:need|have|require)\s+to\s+.{0,60}?"
        r"(?:servers?|cloud|internet)\b|"
        r"no use of\s+.{0,30}?\bservers?\b)\b",
        re.IGNORECASE | re.DOTALL,
    ),
]
_DEVICE_PATTERNS["consumer_ownership"] = _CONSUMER_OWNERSHIP_PATTERNS


# ---------------------------------------------------------------------------
# Usage-dismissal undercut: corporate pattern where a company
# minimizes the impact of a restriction by citing low average usage
# ("most users don't..."), followed by editorial challenge.  A
# specific subtype of corporate reassurance undercut tailored to
# rate-limit / paywall coverage.
# ---------------------------------------------------------------------------
_USAGE_DISMISSAL_UNDERCUT_PATTERNS: list[re.Pattern] = [
    # "most [users/people] don't [use/need/hit]" near "but/however"
    re.compile(
        r"\b(?:most|the majority of|a minority of|few|hardly any)\s+"
        r"(?:users?|people|customers?|subscribers?|owners?)\s+"
        r"(?:don'?t|do not|won'?t|will not|never|rarely|seldom)\s+"
        r"(?:use|need|hit|reach|exceed|come close|approach)\b"
        r".{0,200}?"
        r"\b(?:but|however|yet|still|nonetheless|nevertheless|"
        r"even so|that said)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "intended for power users" / "designed for heavy users" as dismissal
    re.compile(
        r"\b(?:intended|designed|meant|aimed|targeted|built)\s+"
        r"(?:for|at)\s+"
        r"(?:power users?|heavy users?|intensive users?|"
        r"those who (?:need|want|use) (?:it )?more)\b",
        re.IGNORECASE,
    ),
]
_DEVICE_PATTERNS["usage_dismissal_undercut"] = _USAGE_DISMISSAL_UNDERCUT_PATTERNS


# ---------------------------------------------------------------------------
# Financial reassurance: editorial device in financial journalism where
# negative operational news is immediately reframed as a positive market
# signal.  Distinct from corporate_reassurance_undercut (which catches
# PR damage control language that the journalist then undercuts).  Here
# the journalist *is* the reassuring voice, converting bad news into a
# buying signal.
#
# Examples:
#   "That could soothe concerns that Meta is preparing to cut back..."
#   "Despite the disappointment, investors took comfort in..."
#   "Shares recovered after analysts said the miss was priced in."
#   "The selloff eased as the company signalled no change in spending."
#   "...allaying fears of a pullback in AI investment."
# ---------------------------------------------------------------------------
_FINANCIAL_REASSURANCE_PATTERNS: list[re.Pattern] = [
    # "could soothe/ease/allay concerns/fears/worries"
    re.compile(
        r"\b(?:could|may|might|should|would|is expected to|appeared? to|seems? to|helped?)\s+"
        r"(?:soothe|ease|allay|assuage|quell|calm|temper|mitigate|alleviate|dispel)\s+"
        r"(?:concerns?|fears?|worries?|anxiet(?:y|ies)|doubts?|unease|jitters?|nerves?|"
        r"uncertainty|apprehension)",
        re.IGNORECASE,
    ),
    # "despite [negative], [positive market signal]"  —  financial despite-pivot
    re.compile(
        r"\bdespite\s+(?:the\s+)?(?:disappointment|setback|miss|shortfall|decline|slide|"
        r"downturn|slowdown|drop|loss|warning|stumble|headwind|delay|failure)\b"
        r".{5,120}?"
        r"\b(?:recover(?:ed|ing|s)?|rebound(?:ed|ing|s)?|eas(?:ed|ing|es)|"
        r"rally|rallied|rallying|stabliz(?:ed|ing)|held|holding|"
        r"took comfort|priced in|already (?:baked|priced|reflected) in)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "investors/analysts [positive-reaction verb]"
    re.compile(
        r"\b(?:investors?|analysts?|traders?|the (?:market|street|stock))\s+"
        r"(?:took comfort|were? reassured|shrugged off|looked past|"
        r"appeared? (?:un)?fazed|brushed aside|bet (?:that|on)|"
        r"are betting|welcomed)\b",
        re.IGNORECASE,
    ),
    # "easing/soothing fears" as participial — headline-style
    re.compile(
        r"\b(?:easing|soothing|allaying|quelling|calming|tempering|dispelling)\s+"
        r"(?:fears?|concerns?|worries?|doubts?|jitters?|anxiet(?:y|ies)|"
        r"investor (?:fears?|concerns?|worries?))\b",
        re.IGNORECASE,
    ),
    # "remain bullish/optimistic" — analyst stance language (TheStreet Jul 2026)
    re.compile(
        r"\b(?:analysts?|investors?|the (?:street|market|firm))\s+"
        r"(?:remain|remains?|stayed?|continued? to be|are|is)\s+"
        r"(?:bullish|optimistic|positive|upbeat|constructive|"
        r"overweight|confident)\b",
        re.IGNORECASE,
    ),
    # "raised/raised his price target" — price target as implicit endorsement
    re.compile(
        r"\b(?:raised?|lifted|boosted|hiked|increased?|bumped)\s+"
        r"(?:his|her|their|the|its|a)?\s*"
        r"(?:price\s+)?target\b",
        re.IGNORECASE,
    ),
    # "improving ... catalyst/outlook/path" — forward-looking analyst optimism
    re.compile(
        r"\b(?:improving|improved|better|stronger|more favorable)\s+"
        r"(?:\w+\s+){0,4}"
        r"(?:catalyst|outlook|path|trajectory|backdrop|setup|dynamics)\b",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["financial_reassurance"] = _FINANCIAL_REASSURANCE_PATTERNS


# ---------------------------------------------------------------------------
# Competitive positioning: editorial device that explicitly elevates
# a competitor over the subject entity, using comparative language like
# "a more reputable company" or "consumers should buy from [competitor]
# instead."  Distinct from simple comparative framing (which is a
# sentiment dimension) — this is a rhetorical device where the author
# recommends or implies a competitor is preferable.
#
# Discovered in 9to5Mac Conversation Focus analysis (Jul 2026):
# "buy their AI-powered glasses from a more reputable company" and
# "good news for the upcoming Apple Glasses" explicitly position Apple
# as the beneficiary of Meta's failure.  None of the existing framing
# device types captured this competitor-elevation pattern.
# ---------------------------------------------------------------------------
_COMPETITIVE_POSITIONING_PATTERNS: list[re.Pattern] = [
    # "good news for [competitor]" — competitor-benefit framing
    re.compile(
        r"\b(?:good|great|welcome|positive)\s+news\s+"
        r"for\s+(?:the\s+)?(?:upcoming\s+)?"
        r"(?:Apple|Google|Samsung|Microsoft|Amazon|"
        r"competitors?|rival(?:s|ing)?)\b",
        re.IGNORECASE,
    ),
    # "buy from a more reputable/trustworthy company"
    re.compile(
        r"\b(?:buy|purchase|choose|switch to|opt for|prefer)\s+"
        r"(?:their|your|the)?\s*"
        r"(?:\w+\s+){0,3}?"
        r"from\s+(?:a\s+)?(?:more\s+)?"
        r"(?:reputable|trustworthy|responsible|reliable|ethical|"
        r"consumer[- ]friendly|privacy[- ]focused)\s+"
        r"(?:company|brand|maker|manufacturer|competitor|alternative)\b",
        re.IGNORECASE,
    ),
    # "[competitor] would never / doesn't [do bad thing]"
    re.compile(
        r"\b(?:Apple|Google|Samsung|Microsoft)\s+"
        r"(?:has always|would never|doesn'?t|does not|has never|"
        r"never seeks?|has committed|is committed)\b",
        re.IGNORECASE,
    ),
    # "another reason to [buy/choose/switch to] [competitor]"
    re.compile(
        r"\b(?:another|one more|yet another|additional)\s+"
        r"reason\s+(?:to |for )"
        r"(?:consumers?|users?|people|buyers?|customers?)\s+to\s+"
        r"(?:buy|choose|switch|prefer|pick|opt for|go with)\b",
        re.IGNORECASE,
    ),
]
_DEVICE_PATTERNS["competitive_positioning"] = _COMPETITIVE_POSITIONING_PATTERNS


# ---------------------------------------------------------------------------
# Marginal endorsement: analyst action of negligible magnitude presented
# as a meaningful bullish signal.  Common in investment media where a
# price target raise of <1% (e.g., $767 from $765 on a $600 stock) or
# a rating reiteration is framed as substantive endorsement.
#
# Discovered in TheStreet Meta analysis (Jul 4 2026): Wells Fargo
# raised price target $2 (0.26%) while "maintaining overweight rating"
# — functionally a housekeeping adjustment but positioned as bullish.
# ---------------------------------------------------------------------------
_MARGINAL_ENDORSEMENT_PATTERNS: list[re.Pattern] = [
    # "raised his/her/the price target to $X from $Y, maintaining/reiterating"
    re.compile(
        r"\b(?:raised?|lifted|boosted|hiked|increased?|bumped)\s+"
        r"(?:his|her|their|the|its|a)?\s*"
        r"(?:price\s+)?target\s+"
        r"(?:to\s+)?\$[\d,.]+\s+"
        r"(?:from|to)\s+\$[\d,.]+\s*,?\s*"
        r"(?:while\s+|and\s+)?(?:maintain|reiterat|keep)",
        re.IGNORECASE,
    ),
    # "maintained/reiterated overweight/buy/outperform rating"
    re.compile(
        r"\b(?:maintain(?:ed|ing|s)?|reiterat(?:ed|ing|es)?|keep(?:s|ing)?|kept)\s+"
        r"(?:an?\s+|the\s+|its\s+)?"
        r"(?:overweight|buy|outperform|strong buy|positive|market perform|"
        r"sector outperform)\s+"
        r"(?:rating|recommendation|call)\b",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["marginal_endorsement"] = _MARGINAL_ENDORSEMENT_PATTERNS


# ---------------------------------------------------------------------------
# Historical legitimation: insertion of temporally distant positive data
# to structurally dilute fresh negative news.  Common in investment
# media where old earnings beats or revenue growth figures are recapped
# in an article about new negative developments.
#
# Discovered in TheStreet Meta analysis (Jul 4 2026): ~35% of article
# devoted to Q1 earnings recap (April 29 data in July 4 article) in a
# piece about Zuckerberg's AI disappointment admission.
# ---------------------------------------------------------------------------
_HISTORICAL_LEGITIMATION_PATTERNS: list[re.Pattern] = [
    # "reported [quarter] results ... beat/topped/ahead/exceeded"
    re.compile(
        r"\breported\s+"
        r"(?:first|second|third|fourth|Q[1-4]|full[- ]year|annual|quarterly)\s*"
        r"(?:-?\s*quarter)?\s*"
        r"(?:results?|earnings?|numbers?|financials?)\b"
        r".{5,200}?"
        r"\b(?:beat(?:ing)?|topp(?:ed|ing)|ahead of|exceeded?|surpass(?:ed|ing)|"
        r"above|better than)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "earnings per share of $X, topping estimates"
    re.compile(
        r"\b(?:earnings?\s+per\s+share|EPS|revenue|sales|net\s+income)\s+"
        r"(?:of\s+)?\$[\d,.]+\s*"
        r"(?:billion|million|B|M)?\s*,?\s*"
        r"(?:topping|beating|exceeding|ahead\s+of|above|surpassing|"
        r"better\s+than)\s+"
        r"(?:estimates?|expectations?|consensus|forecasts?|projections?|"
        r"Wall Street|the Street|analyst)\b",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["historical_legitimation"] = _HISTORICAL_LEGITIMATION_PATTERNS


# ---------------------------------------------------------------------------
# Policy reversal: structural framing device that highlights a company
# reversing a previous policy or position.  The article states both the
# old policy and its replacement, drawing reader attention to the
# contradiction.  This is NOT inherently adversarial — it may be
# neutral reporting of a genuine change — so it is NOT added to
# _ADVERSARIAL_DEVICE_TYPES.
#
# Discovered in Reuters Zuckerberg town hall analysis (Jul 3 2026):
# "originally had no way to opt out" followed by reporting that "Meta
# Platforms will not use facial recognition... on an opt-in basis."
# The MCI mouse-tracking reversal (mandatory → opt-in) and capex
# guidance revisions ($60-65B → $125-145B) are also policy reversals
# that existing framing device types missed entirely.
#
# Distinct from hypocrisy_frame (which requires ironic self-
# contradiction between stated values and behavior).  Policy reversal
# captures factual policy-A-then-policy-B transitions, regardless of
# whether the author frames them as hypocritical.
# ---------------------------------------------------------------------------
_POLICY_REVERSAL_PATTERNS: list[re.Pattern] = [
    # "originally/initially/previously [had/was/required] X ... now/will [Y]"
    re.compile(
        r"\b(?:originally|initially|previously|formerly|at first|"
        r"at launch|when (?:it |they )?(?:first |originally )?(?:launched|started|rolled out|introduced))\s+"
        r"(?:had|was|were|required|mandated|set|used|allowed|offered|"
        r"defaulted to|included)\b"
        r".{10,200}?"
        r"\b(?:now|but now|will now|has since|have since|has been|"
        r"have been|is now|are now|will be|will instead|"
        r"reversed|changed to|switched to|moved to|shifted to|"
        r"transitioned to|converted to)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "reversed/walked back/backtracked/scrapped/abandoned/dropped"
    re.compile(
        r"\b(?:reversed?|walk(?:ed|ing)?\s+back|backtrack(?:ed|ing|s)?|"
        r"scrap(?:ped|ping|s)?|abandon(?:ed|ing|s)?|"
        r"drop(?:ped|ping|s)?|ditched?|overturned?|"
        r"rethink(?:ing)?|reconsider(?:ed|ing)?|"
        r"u-turn(?:ed)?|about-face|flip(?:ped|-flopped?))\s+"
        r"(?:its|their|the|a|an)?\s*"
        r"(?:earlier|original|previous|initial|prior|existing|"
        r"long-?standing|controversial)?\s*"
        r"(?:policy|decision|plan|approach|strategy|stance|position|"
        r"requirement|mandate|rule|practice|feature|rollout)\b",
        re.IGNORECASE,
    ),
    # "mandatory → voluntary" / "required → optional" / "opt-out → opt-in"
    re.compile(
        r"\b(?:(?:from|was|were|moved from|changed from|switched from)\s+)?"
        r"(?:mandatory|required|compulsory|default|automatic|opt-?out)\b"
        r".{1,60}?"
        r"\b(?:to\s+)?(?:voluntary|optional|opt-?in|elective|"
        r"on (?:a |an )?(?:opt-?in|voluntary|optional)\s+basis)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "no longer [requires/uses/collects]" — cessation of previous policy
    re.compile(
        r"\b(?:no longer|will no longer|would no longer|stopped|"
        r"ceased|discontinued)\s+"
        r"(?:require|requires?|use|uses?|collect|collects?|"
        r"mandate|mandates?|enforce|enforces?|track|tracks?|"
        r"store|stores?|retain|retains?|share|shares?)\b",
        re.IGNORECASE,
    ),
    # "[Entity] had [policy] but [new policy]" via despite-reversal
    re.compile(
        r"\b(?:despite (?:earlier|previously|initially) "
        r"(?:announcing|committing|promising|pledging|stating|saying))\b"
        r".{5,150}?"
        r"\b(?:now|instead|has since|have since|will|reversed?)\b",
        re.IGNORECASE | re.DOTALL,
    ),
]

_DEVICE_PATTERNS["policy_reversal"] = _POLICY_REVERSAL_PATTERNS


# ---------------------------------------------------------------------------
# Competitive deficit: editorial device that explicitly lists multiple
# competitors to amplify the subject's failure or inadequacy.  The
# rhetorical effect is a "pile-on" that makes the subject look
# surrounded and outpaced.  Distinct from competitive_positioning
# (which elevates one specific competitor as preferable) — this device
# enumerates three or more rivals to create an impression of systemic
# failure.
#
# Discovered in Reuters Zuckerberg town hall analysis (Jul 3 2026):
# "failed to launch a successful rival to OpenAI's ChatGPT, Google's
# Gemini, and Anthropic's Claude" — the explicit listing of three named
# competitors with their products turns a factual comparison into an
# adversarial framing device that none of the existing types captured.
#
# Also appears in Barron's analysis (Jul 3 2026): "falling behind
# competitors in the AI race" with later enumeration of "OpenAI,
# Google, and Anthropic."
# ---------------------------------------------------------------------------
_COMPETITIVE_DEFICIT_PATTERNS: list[re.Pattern] = [
    # "failed to [verb] ... rival [Company A]'s [Product], [Company B]'s
    # [Product], and [Company C]'s [Product]"
    re.compile(
        r"\b(?:failed?|struggling|unable|has(?:n't| not)|"
        r"have(?:n't| not)|couldn't|could not)\s+(?:to\s+)?"
        r"(?:launch|build|create|develop|deliver|produce|ship|"
        r"release|match|compete|rival|catch up|keep up|keep pace)\b"
        r".{5,200}?"
        r"\b(?:OpenAI|Google|Anthropic|Apple|Microsoft|Amazon|"
        r"Samsung|Nvidia|xAI|Mistral|DeepSeek)\b"
        r".{1,80}?"
        r"\b(?:OpenAI|Google|Anthropic|Apple|Microsoft|Amazon|"
        r"Samsung|Nvidia|xAI|Mistral|DeepSeek)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "lags behind / trails / has yet to match [list of competitors]"
    re.compile(
        r"\b(?:lag(?:s|ged|ging)?\s+behind|trail(?:s|ed|ing)?|"
        r"has yet to (?:match|rival|catch|reach)|"
        r"fallen? behind|falling behind|"
        r"playing catch-?up|"
        r"left behind by)\b"
        r".{5,150}?"
        r"\b(?:competitors?|rivals?|peers?)\s+"
        r"(?:including|such as|like|namely)\b"
        r".{1,150}?"
        r"\b(?:and|,)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "competitors including [A], [B], and [C]" — explicit enumeration
    re.compile(
        r"\b(?:competitors?|rivals?|other (?:companies|players|firms))\s+"
        r"(?:including|such as|like|namely)\s+"
        r"(?:[A-Z]\w+(?:'s\s+\w+)?,?\s*){2,}"
        r"(?:and\s+[A-Z]\w+(?:'s\s+\w+)?)\b",
        re.IGNORECASE,
    ),
    # "while/whereas [A], [B], and [C] have [positive verb]" — contrast listing
    re.compile(
        r"\b(?:while|whereas|even as|meanwhile)\s+"
        r"(?:OpenAI|Google|Anthropic|Apple|Microsoft|Amazon)\b"
        r".{1,60}?"
        r"\b(?:OpenAI|Google|Anthropic|Apple|Microsoft|Amazon)\b"
        r".{1,60}?"
        r"\b(?:have|has|had|already|launched|shipped|released|built|"
        r"achieved|surpassed|outpaced)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Simple "lagged/lagging/trails behind [Company] and [Company]" —
    # direct competitor naming without the "competitors including" preamble.
    # Discovered in MarketWatch Meta cloud pivot article (Jul 1, 2026):
    # "lagged behind Anthropic and OpenAI" was not detected because the
    # existing patterns required "competitors including/such as/like".
    re.compile(
        r"\b(?:lag(?:s|ged|ging)?\s+behind|trail(?:s|ed|ing)?\s*"
        r"(?:behind)?|fallen?\s+behind|falling\s+behind|"
        r"playing\s+catch-?up\s+(?:with|to)|left\s+behind\s+by)\s+"
        r"(?:OpenAI|Google|Anthropic|Apple|Microsoft|Amazon|"
        r"Samsung|Nvidia|xAI|Mistral|DeepSeek)\b"
        r".{1,80}?"
        r"\b(?:OpenAI|Google|Anthropic|Apple|Microsoft|Amazon|"
        r"Samsung|Nvidia|xAI|Mistral|DeepSeek)\b",
        re.IGNORECASE | re.DOTALL,
    ),
]

_DEVICE_PATTERNS["competitive_deficit"] = _COMPETITIVE_DEFICIT_PATTERNS


# ---------------------------------------------------------------------------
# ABSENCE_AS_EVIDENCE — 2026-07-03
# Detects when an author frames the *absence* of an action, audit, or
# disclosure as proof of guilt or bad intent.  This is a rhetorical device
# that converts non-events into indictments:
#   "Not one task was directed at Meta AI"
#   "The internal audit that never happened is the data point"
#   "Meta did not do that."
#   "the company never disclosed"
# Common in editorial / analysis pieces covering corporate accountability.
# ---------------------------------------------------------------------------

_ABSENCE_AS_EVIDENCE_PATTERNS: list[re.Pattern] = [
    # "Not one [noun] was [verb]ed at/to/by [entity]"
    re.compile(
        r"\bnot (?:one|a single)\s+\w+\s+(?:was|were|has been|had been)\s+"
        r"(?:directed|aimed|targeted|focused|applied|devoted|assigned)\b",
        re.IGNORECASE,
    ),
    # "the [noun] that never happened / never took place / never occurred"
    re.compile(
        r"\bthe\s+\w+(?:\s+\w+)?\s+that\s+never\s+"
        r"(?:happened|occurred|took place|materialised|materialized|existed)\b",
        re.IGNORECASE,
    ),
    # "[Entity] did not [do X]" as a standalone accusatory sentence
    # (short sentence, < 60 chars total, ending with period)
    re.compile(
        r"(?:^|\.\s+)([A-Z]\w+\s+(?:did not|didn't)\s+(?:do that|disclose|report|"
        r"share|address|respond|act|cooperate|comply|notify))\.",
        re.MULTILINE,
    ),
    # "[Entity] never [verb]ed" / "has never [verb]ed"
    re.compile(
        r"\b(?:has|had|have)?\s*never\s+"
        r"(?:disclosed|reported|acknowledged|addressed|tested|audited|shared|"
        r"flagged|notified|informed|consulted)\b",
        re.IGNORECASE,
    ),
    # "the company/they/Meta chose not to / failed to / declined to"
    re.compile(
        r"\b(?:the company|Meta|they|it)\s+"
        r"(?:chose not to|failed to|declined to|neglected to|opted not to|"
        r"did not bother to|made no effort to)\s+\w+",
        re.IGNORECASE,
    ),
]

_DEVICE_PATTERNS["absence_as_evidence"] = _ABSENCE_AS_EVIDENCE_PATTERNS


# ---------------------------------------------------------------------------
# SILENCE_AS_GUILT — 2026-07-03
# Detects when an author explicitly treats silence, non-response, or
# non-disclosure as a confession or admission of guilt:
#   "That silence is its own answer"
#   "The lack of denial speaks volumes"
#   "their refusal to comment is telling"
# Distinct from refusal_amplification (which notes a no-comment factually);
# silence_as_guilt goes further by asserting the silence proves something.
# ---------------------------------------------------------------------------

_SILENCE_AS_GUILT_PATTERNS: list[re.Pattern] = [
    # "that silence is its own answer/admission/confession"
    re.compile(
        r"\b(?:that|this|the|their)\s+silence\s+"
        r"(?:is|was|speaks|tells|reveals|amounts to|constitutes)\s+"
        r"(?:its own|an?|the|telling|volumes|damning|everything)",
        re.IGNORECASE,
    ),
    # "the lack of [denial/response/comment] speaks volumes / is telling"
    re.compile(
        r"\b(?:the|their|its)\s+(?:lack|absence)\s+of\s+"
        r"(?:denial|response|comment|explanation|transparency|disclosure)\s+"
        r"(?:speaks|is|was|says|reveals|tells)\b",
        re.IGNORECASE,
    ),
    # "refusal to [comment/respond/disclose] is [telling/damning/revealing]"
    re.compile(
        r"\brefusal to\s+(?:comment|respond|disclose|engage|explain|address|deny)\s+"
        r"(?:is|was|seems?|appears?)\s+"
        r"(?:telling|damning|revealing|significant|itself|notable|conspicuous)",
        re.IGNORECASE,
    ),
    # "no comment/response/denial — and that says/tells ..."
    re.compile(
        r"\bno\s+(?:comment|response|denial|answer|explanation)\b"
        r".{0,40}?"
        r"\b(?:says|tells|speaks|is telling|is significant)\b",
        re.IGNORECASE | re.DOTALL,
    ),
]

_DEVICE_PATTERNS["silence_as_guilt"] = _SILENCE_AS_GUILT_PATTERNS


# --- Delayed defense ---
# Structural post-pass: detects when the subject company's response
# or defense first appears in the last 35% of the article.  This is
# a well-known editorial technique: bury the rebuttal after the damage
# is done, so most readers form their opinion before encountering the
# other side.
#
# Implementation: split text into paragraphs, find the first paragraph
# containing corporate-response language, and flag if it starts after
# the 65% mark.

_CORPORATE_RESPONSE_PATTERNS: list[re.Pattern] = [
    # "[Company] said / spokesperson said / in a statement"
    re.compile(
        r"\b(?:Meta|Google|Apple|Amazon|Microsoft|OpenAI|Anthropic|"
        r"Tesla|Nvidia|Samsung|TikTok|ByteDance|X Corp|Snap(?:chat)?|"
        r"the company|a company|a (?:Meta|Google|Apple)\s)"
        r"\s*(?:said|told|stated|responded|declined|denied|acknowledged|"
        r"confirmed|insisted|maintained|countered|explained|added|defended)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:spokesperson|spokeswoman|spokesman|representative|"
        r"press officer|communications director|PR|public relations)\b"
        r"\s*(?:for |at |of |from )?[^.]{0,40}?"
        r"(?:said|told|stated|responded|declined|confirmed|wrote|emailed)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    re.compile(
        r"\bin (?:a |an |its |their |the company['\u2019]s )?"
        r"(?:statement|response|reply|email|comment|filing|blog post)\b"
        r"[^.]{0,60}?"
        r"(?:said|wrote|noted|stated|denied|confirmed|maintained|"
        r"argued|explained|acknowledged|insisted)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "declined to comment" / "did not respond"
    re.compile(
        r"\b(?:declined to comment|declined to (?:respond|answer|address)|"
        r"did not (?:respond|reply|comment|return)|"
        r"would not (?:comment|say|confirm|deny)|"
        r"chose not to (?:comment|respond)|"
        r"has not (?:responded|commented|replied))\b",
        re.IGNORECASE,
    ),
]


def _detect_delayed_defense(text: str) -> list[FramingDevice]:
    """Detect delayed defense — corporate response buried late in the article.

    Fires when the first corporate-response paragraph appears after 65% of
    the article text.  Requires the article to be at least 500 characters
    (short articles don't have meaningful positional structure).
    """
    if len(text) < 500:
        return []

    text_len = len(text)
    threshold = 0.65  # first response must appear after this fraction

    # Find the earliest corporate response match
    earliest_pos: int | None = None
    earliest_evidence: str = ""
    for pattern in _CORPORATE_RESPONSE_PATTERNS:
        m = pattern.search(text)
        if m and (earliest_pos is None or m.start() < earliest_pos):
            earliest_pos = m.start()
            earliest_evidence = m.group(0).strip()

    if earliest_pos is None:
        return []

    # Check if the first response appears after the threshold
    relative_pos = earliest_pos / text_len
    if relative_pos < threshold:
        return []

    pct = int(relative_pos * 100)
    evidence = f"First corporate response at {pct}% through article: \"{earliest_evidence}\""
    if len(evidence) > 200:
        evidence = evidence[:200] + "..."

    return [
        FramingDevice(
            device_type="delayed_defense",
            evidence_text=evidence,
            start=earliest_pos,
            end=min(earliest_pos + len(earliest_evidence), text_len),
        )
    ]


# --- Talent hemorrhage ---
# Detects when an article catalogs multiple personnel departures from
# one entity to competitors, creating an "exodus" narrative.  Common in
# restructuring coverage where listing 3+ departures in sequence builds
# a cumulative impression of organizational collapse.
# Discovered during NYT Meta AI overhaul analysis (Jul 2026): article
# lists Pineau→Cohere, Fan→OpenAI, Crisan→Figma in rapid succession
# but toolkit detected no framing device for the pattern.

_TALENT_HEMORRHAGE_PATTERNS: list[re.Pattern] = [
    # "left for / joined / departed for [Company]" repeated in close proximity
    re.compile(
        r"(?:left (?:the company|for|to join)|departed (?:for|to)|"
        r"recently left|is (?:also )?leaving|joined (?:\w+ )+)"
        r"[^.]{0,80}?\."
        r"[^.]{0,200}?"
        r"(?:left (?:the company|for|to join)|departed (?:for|to)|"
        r"recently left|is (?:also )?leaving|joined (?:\w+ )+)",
        re.IGNORECASE | re.DOTALL,
    ),
    # "personnel churn" / "talent exodus" / "brain drain" explicit labels
    re.compile(
        r"\b(?:personnel churn|talent (?:exodus|drain|flight|hemorrhage|war)|"
        r"brain drain|poaching war|hiring war)\b",
        re.IGNORECASE,
    ),
]
_DEVICE_PATTERNS["talent_hemorrhage"] = _TALENT_HEMORRHAGE_PATTERNS


# --- Strategic reversal ---
# Detects when an article highlights a company reversing a core strategic
# position (e.g., abandoning open-source philosophy, pivoting strategy,
# departing from "longtime" stance).  Distinct from policy_reversal which
# focuses on regulatory/legal reversals.
# Discovered during NYT Meta AI overhaul analysis (Jul 2026): abandoning
# Behemoth model + considering closed-source = double strategic reversal
# but toolkit had no pattern for corporate strategy reversals.

_STRATEGIC_REVERSAL_PATTERNS: list[re.Pattern] = [
    # "a major departure from [Company's] longtime philosophy/strategy/approach"
    re.compile(
        r"\b(?:a )?(?:major|significant|dramatic|sharp|stark|notable) "
        r"departure from\b[^.]{0,80}?"
        r"\b(?:philosophy|strategy|approach|stance|position|practice|policy"
        r"|commitment|tradition)\b",
        re.IGNORECASE,
    ),
    # "chosen to abandon / decided to scrap / start from scratch"
    re.compile(
        r"\b(?:chosen to abandon|decided to (?:abandon|scrap|drop|shelve)|"
        r"start(?:ing)? from scratch|scrapped|jettisoned|walked back|"
        r"reversed course|abandoned its)\b",
        re.IGNORECASE,
    ),
    # "shift from [doing X] to [doing Y]" — strategic pivot language
    re.compile(
        r"\b(?:a |would be a )?shift from\b[^.]{0,100}?"
        r"\b(?:to (?:using|building|creating|developing|licensing|selling))\b",
        re.IGNORECASE,
    ),
]
_DEVICE_PATTERNS["strategic_reversal"] = _STRATEGIC_REVERSAL_PATTERNS


# --- Repeated disruption ---
# Detects headline or lead language implying chronic instability: "again,"
# "yet another," "once more," in restructuring/shakeup context.
# Frames the subject as incapable of settling on a strategy.
# Discovered during NYT Meta AI overhaul analysis (Jul 2026): headline
# "Shakes Up... Again" and body "months of tumult and restructuring"
# create a cumulative instability narrative.

_REPEATED_DISRUPTION_PATTERNS: list[re.Pattern] = [
    # Headline-style: "shakes up / overhauls / restructures [X], again"
    # Use .{0,60}? instead of [^.]{0,60}? to allow periods inside
    # abbreviations like "A.I." which are common in NYT headline style.
    re.compile(
        r"\b(?:shakes? up|overhauls?|restructures?|reorganizes?|reshuffles?)"
        r".{0,60}?"
        r"\b(?:again|once (?:more|again)|yet again|for the \w+ time)\b",
        re.IGNORECASE,
    ),
    # "yet another restructuring / reorganization / overhaul / shake-up"
    re.compile(
        r"\b(?:yet another|another|the latest|one more) "
        r"(?:restructuring|reorganization|overhaul|shake-?up|revamp|reshuffle"
        r"|pivot|round of (?:cuts|layoffs|changes))\b",
        re.IGNORECASE,
    ),
    # "months of tumult / turmoil / upheaval / instability"
    re.compile(
        r"\b(?:months|weeks|years) of "
        r"(?:tumult|turmoil|upheaval|instability|chaos|uncertainty|disruption"
        r"|restructuring)\b",
        re.IGNORECASE,
    ),
]
_DEVICE_PATTERNS["repeated_disruption"] = _REPEATED_DISRUPTION_PATTERNS


# ---------------------------------------------------------------------------
# Expert contradiction / reframe: a named expert source directly
# contradicts a company's stated rationale, using "it's not about X;
# it's about Y" inversion or similar patterns.  Different from
# corporate_reassurance_undercut (journalist's own challenge) — here
# the undercut comes from a credentialed third-party source.
#
# Gap discovered in Wired Conversation Focus article (Jul 2026):
# Chris Harrison (Carnegie Mellon): "It's not about recovering AI
# costs; it's about monetizing customers."  The pipeline detected
# "extracting value" as ironic_quotation but missed the expert's
# explicit reframe of Meta's stated justification.
# ---------------------------------------------------------------------------
_EXPERT_CONTRADICTION_PATTERNS: list[re.Pattern] = [
    # "It's not about X; it's about Y" — explicit negation + reframe
    re.compile(
        r"""(?:['"\u201c\u201d])?[Ii]t['\u2019]?s\s+not\s+(?:about|for|to)\s+"""
        r"""[^.;:!?"'\u201c\u201d]{5,80}?"""
        r"""[;:—–]\s*(?:['"\u201c\u201d])?it['\u2019]?s\s+(?:about|for|to|really\s+about)\s+"""
        r"""[^.;:!?"'\u201c\u201d]{5,80}""",
        re.IGNORECASE,
    ),
    # "doesn't think [action/claim] is [about/to/for]" — reporter
    # framing an expert's skepticism of company justification
    re.compile(
        r"\b(?:doesn['\u2019]?t|does not)\s+(?:think|believe|buy|accept)\s+"
        r"(?:the |that |this )?"
        r"(?:new |latest |proposed |recent )?"
        r"(?:subscription|move|change|decision|plan|strategy|claim)\s+"
        r"(?:is |was |will be )?"
        r"(?:about|for|to help|meant to|designed to|intended to)\s+",
        re.IGNORECASE,
    ),
]
_DEVICE_PATTERNS["expert_contradiction"] = _EXPERT_CONTRADICTION_PATTERNS


# ---------------------------------------------------------------------------
# Loss-leader / razor-blade framing: editorial description of a
# business model where hardware is sold at cost (or below) to capture
# recurring subscription revenue.  This is a specific editorial lens
# that frames a company's pricing strategy as exploitative or as a
# lock-in mechanism.
#
# Gap discovered in Wired Conversation Focus article (Jul 2026):
# "The company's glasses are typically sold at cost, like the new $299
# Meta-branded glasses... Harrison says this helps get the glasses out
# in the world and increases the user base — then the subscription
# service grows revenue."
# ---------------------------------------------------------------------------
_LOSS_LEADER_PATTERNS: list[re.Pattern] = [
    # "sold at cost" / "sold at a loss" / "sold below cost"
    re.compile(
        r"\b(?:sold|sell(?:s|ing)?|priced|offered)\s+"
        r"(?:at (?:cost|a loss)|below cost|near cost|at or below cost|"
        r"at break-?even|close to cost)\b",
        re.IGNORECASE,
    ),
    # "subscription [service/model] [grows/generates] revenue"
    # near "user base" / "install base" / "adoption"
    re.compile(
        r"\b(?:user base|install base|installed base|adoption|"
        r"customer base|subscriber base)\b"
        r".{0,200}?"
        r"\b(?:subscription|recurring|monthly)\s+"
        r"(?:service|model|revenue|fee|income)\s+"
        r"(?:grows?|generates?|drives?|creates?|produces?)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # Reverse: subscription near user base
    re.compile(
        r"\b(?:subscription|recurring|monthly)\s+"
        r"(?:service|model|revenue|fee|income)\s+"
        r"(?:grows?|generates?|drives?|creates?|produces?)\b"
        r".{0,200}?"
        r"\b(?:user base|install base|installed base|adoption|"
        r"customer base|subscriber base)\b",
        re.IGNORECASE | re.DOTALL,
    ),
]
_DEVICE_PATTERNS["loss_leader_framing"] = _LOSS_LEADER_PATTERNS


# ---------------------------------------------------------------------------
# Editorial dramatization: interpretive glosses that rewrite neutral
# factual events in heightened, dramatic language.
#
# Distinct from escalation_amplification, which detects *intensifying
# modifiers* paired with threat/concern nouns ("escalating crisis,"
# "increasingly alarmed").  Editorial dramatization catches standalone
# dramatic descriptors and set-piece phrases that an editor inserts to
# color an event beyond what the sourced facts support.
#
# Common in derivative/rewrite outlets that take wire copy and add
# editorial drama: "unexpected reality check," "clear speed bump,"
# "massive shakeup," "turbulent transition," "did not mince words,"
# "aggressive and sweeping ... specifically engineered," "stark gap
# between X and Y."
#
# Gap discovered in iPhone in Canada rewrite of Reuters article about
# Zuckerberg's July 2026 town hall — all 8 editorial dramatization
# phrases were missed by the existing toolkit, including
# escalation_amplification.
# ---------------------------------------------------------------------------
_EDITORIAL_DRAMATIZATION_PATTERNS: list[re.Pattern] = [
    # "unexpected/surprising/sudden reality check/wake-up call/reckoning"
    re.compile(
        r"\b(?:unexpected|surprising|sudden|rare|stunning|"
        r"remarkable|unusual|startling|sobering)\s+"
        r"(?:reality check|wake-?up call|reckoning|admission|"
        r"reversal|about-?face|mea culpa|concession|confession|"
        r"acknowledgment|acknowledgement)\b",
        re.IGNORECASE,
    ),
    # "clear/obvious/significant speed bump/setback/stumble/hurdle"
    re.compile(
        r"\b(?:clear|obvious|significant|notable|major|serious|"
        r"real|genuine|undeniable|unmistakable)\s+"
        r"(?:speed bump|setback|stumble|stumbling block|hurdle|"
        r"roadblock|obstacle|bottleneck|headwind|challenge|"
        r"blow|hit|snag|hitch)\b",
        re.IGNORECASE,
    ),
    # "massive/sweeping/aggressive/dramatic shakeup/overhaul/restructuring/upheaval"
    re.compile(
        r"\b(?:massive|sweeping|aggressive|dramatic|radical|drastic|"
        r"seismic|tectonic|brutal|ruthless|wholesale|comprehensive|"
        r"wide-?ranging|far-?reaching|all-?encompassing)\s+"
        r"(?:shakeup|shake-?up|overhaul|restructuring|restructure|"
        r"reorgani[sz]ation|reorgani[sz]ing|transformation|upheaval|"
        r"revamp|reboot|pivot|purge|culling|bloodletting|housecleaning)\b",
        re.IGNORECASE,
    ),
    # "turbulent/tumultuous/chaotic/painful transition/period/chapter"
    re.compile(
        r"\b(?:turbulent|tumultuous|chaotic|painful|bruising|rocky|"
        r"bumpy|stormy|fraught|agonizing|wrenching|gut-?wrenching|"
        r"grueling|gruelling|tortuous|harrowing)\s+"
        r"(?:transition|period|chapter|phase|stretch|time|journey|"
        r"process|transformation|overhaul|adjustment|realignment)\b",
        re.IGNORECASE,
    ),
    # "did not mince words" / "pulled no punches" / "didn't sugarcoat"
    re.compile(
        r"\b(?:did(?:n't| not) mince (?:words|his words|her words)|"
        r"pull(?:ed|s)? no punches|"
        r"did(?:n't| not) sugarcoat|"
        r"did(?:n't| not) sugar-?coat|"
        r"laid? it on the line|"
        r"let(?:ting)? the mask slip|"
        r"dropped? (?:a |the )?bombshell|"
        r"spoke? (?:with )?(?:brutal|blunt|remarkable|unusual|rare|"
        r"surprising|candid|striking) (?:candor|honesty|frankness|"
        r"openness|clarity|directness))\b",
        re.IGNORECASE,
    ),
    # "stark/glaring/yawning/widening gap/disconnect/divide/mismatch"
    re.compile(
        r"\b(?:stark|glaring|yawning|widening|growing|gaping|"
        r"troubling|alarming|revealing|telling)\s+"
        r"(?:gap|disconnect|divide|mismatch|disparity|chasm|"
        r"gulf|rift|distance|tension|contradiction|contrast)\s+"
        r"(?:between|among|separating)\b",
        re.IGNORECASE,
    ),
    # "specifically engineered/designed/crafted/built to" (implying deliberate scheming)
    re.compile(
        r"\bspecifically\s+"
        r"(?:engineered|designed|crafted|built|constructed|"
        r"tailored|architected|orchestrated|calibrated|calculated)\s+"
        r"(?:to|for)\b",
        re.IGNORECASE,
    ),
    # "current/ongoing friction/turmoil/chaos/fallout/wreckage"
    re.compile(
        r"\b(?:current|ongoing|continued|continuing|persistent|"
        r"lingering|mounting|resulting|ensuing|subsequent)\s+"
        r"(?:friction|turmoil|chaos|fallout|wreckage|carnage|"
        r"disruption|instability|dysfunction|turbulence|upheaval|"
        r"unrest|dislocation|disarray|uncertainty|angst)\b",
        re.IGNORECASE,
    ),
]
_DEVICE_PATTERNS["editorial_dramatization"] = _EDITORIAL_DRAMATIZATION_PATTERNS


def detect_framing_devices(
    text: str,
    source_publication: str | None = None,
) -> list[FramingDevice]:
    """Detect framing devices in article text.

    Scans for 66 pattern-matched device types plus 6 structural
    post-pass types (72 total).

    When *source_publication* is provided, ``self_referential_investigation``
    matches are filtered to only fire when the cited publication matches the
    source (case-insensitive substring).  Without it, all publication
    authority claims are returned (backward-compatible default).

    Pattern-matched (66): absence_as_evidence, analogy_metaphor,
    anonymous_authority,
    anthropomorphization, assumed_consensus, catastrophizing,
    ceo_personalization, competitive_deficit, competitive_positioning,
    commodification_metaphor, confession_framing,
    consumer_ownership,
    corporate_reassurance_undercut, cross_publication_import,
    denial_contradiction,
    editorial_aside, editorial_deflation, editorial_dramatization,
    emotional_appeal,
    escalation_amplification, expert_contradiction,
    failure_precedent, false_balance,
    financial_reassurance,
    geopolitical_regulatory_pressure, guilt_by_association,
    historical_legitimation,
    hypocrisy_frame, industry_normalization_undercut,
    ironic_quotation, isolation_framing,
    juxtaposition, latecomer_narrative, litigation_framing,
    loaded_language, loss_leader_framing,
    marginal_endorsement,
    military_techno_optimism, outsourced_intensity,
    pathologizing_metaphor, policy_reversal, power_asymmetry,
    precedent_analogy,
    pressure_language, refusal_amplification, regulatory_favoritism,
    regulatory_shadow, repeated_disruption, rhetorical_question,
    sarcastic_correction, scandal_comparison, scale_magnitude,
    selective_omission_signal,
    selective_rehabilitation, self_referential_investigation,
    silence_as_guilt, slippery_slope, sovereignty_framing,
    strategic_reversal, straw_man, talent_hemorrhage,
    taxonomy_framing, timeline_implication,
    two_tier_treatment, usage_dismissal_undercut,
    and worker_replacement_irony.

    Structural post-pass (6): delayed_defense, kicker_framing,
    analogy_stacking, speculative_framing, trend_bundling,
    social_proof_amplification.

    Args:
        text: The article text to analyze.

    Returns:
        List of FramingDevice objects found, sorted by position.
    """
    if not text:
        return []

    devices: list[FramingDevice] = []
    seen_spans: set[tuple[str, int, int]] = set()

    for device_type, patterns in _DEVICE_PATTERNS.items():
        for pattern in patterns:
            for match in pattern.finditer(text):
                start, end = match.start(), match.end()
                span_key = (device_type, start, end)

                # Deduplicate overlapping matches of the same type
                if span_key in seen_spans:
                    continue

                # Check for overlap with existing matches of the same type
                overlap = False
                for existing in seen_spans:
                    if existing[0] == device_type:
                        ex_start, ex_end = existing[1], existing[2]
                        if not (end <= ex_start or start >= ex_end):
                            overlap = True
                            break

                if overlap:
                    continue

                # --- Analogy/metaphor: evaluative idiom filter ----------------
                # Suppress analogy_metaphor when "like a/an" is followed by
                # an evaluative adjective + noun — these are value judgments
                # ("like a smart business move", "like a no-brainer buy"),
                # not literary similes or rhetorical comparisons.
                #
                # Identified in Motley Fool Meta Cloud article (Jul 2026):
                # "like a smart business move" and "like a no-brainer buy"
                # are idiomatic evaluations, not analogy devices.
                # ---------------------------------------------------------
                if device_type == "analogy_metaphor":
                    _matched_am = match.group().lower()
                    if re.search(
                        r"\blike (?:a|an) (?:smart|good|bad|great|wise|"
                        r"solid|strong|bold|savvy|shrewd|clever|obvious|"
                        r"clear|safe|risky|sound|fair|poor|terrible|"
                        r"brilliant|logical|reasonable|sensible|practical|"
                        r"prudent|foolish|dumb|stupid|crazy|insane|"
                        r"no-brainer|no brainer)\b",
                        _matched_am,
                    ):
                        continue

                # --- Geopolitical pressure: physical "stood/standing firm" ---
                # Suppress geopolitical_regulatory_pressure when "stood firm"
                # or "standing firm" is used literally (security guards, police,
                # bouncers physically standing), not as geopolitical defiance.
                # Identified in WebProNews Meta Dublin contractors article
                # (May 2026): "security guards at Meta's gates stood firm."
                # ---------------------------------------------------------
                if device_type == "geopolitical_regulatory_pressure":
                    _matched_lower = match.group().lower()
                    if "stood firm" in _matched_lower or "standing firm" in _matched_lower:
                        _lookback_geo = text[max(0, start - 80):start].lower()
                        _PHYSICAL_ACTORS = (
                            "guard", "security", "police", "officer",
                            "soldier", "bouncer", "doorman", "sentry",
                            "protester", "demonstrator", "picket",
                        )
                        if any(actor in _lookback_geo for actor in _PHYSICAL_ACTORS):
                            continue

                # --- Ironic-quotation attribution filter ----------------------
                # Suppress ironic_quotation matches that are short (≤3 words)
                # product-naming terms embedded in attribution context, not
                # author scare-quotes.  Only suppresses when the immediate
                # context (40 chars) contains a product-naming phrase.
                #
                # Identified in NYT Arena article (Jun 2026): "points" and
                # "predictors" are product terms attributed to a source report,
                # not ironic quotation.  Longer quotes and quotes followed by
                # editorial undermining are preserved.
                # -----------------------------------------------------------------
                if device_type == "ironic_quotation":
                    _quoted = match.group().strip('" \u201c\u201d')
                    _word_count = len(_quoted.split())
                    # --- Structural transition filter -------------------------
                    # Pattern 0 (quote-end + contradiction word) fires on
                    # natural interview transitions like:
                    #   "...investigation". Yet his skepticism was apparent.
                    #   "...awareness to them," she said. But she also...
                    # These are narrative flow, not ironic undercutting.
                    # Suppress when:
                    # (a) The evidence text contains explicit attribution
                    #     verbs ("she said", "he noted"), or
                    # (b) The evidence (stripped of quote marks) starts with
                    #     a sentence boundary (".", ",") — indicating the
                    #     match is a structural transition, not a quoted
                    #     phrase being undercut.  These short matches (". Yet",
                    #     ". In other words,") are just conjunction flow;
                    #     genuine ironic undercutting uses the quoted term
                    #     itself as the ironic payload.
                    #
                    # Discovered in Guardian DeepMind philosopher profile
                    # (Jun 28, 2026): 4 structural false positives from
                    # interview transitions.
                    # ---------------------------------------------------------
                    _stripped_evidence = _quoted.strip()
                    _STRUCTURAL_ATTRIBUTION = (
                        " said.", " said,", " says.", " says,",
                        " noted.", " noted,", " added.", " added,",
                        " told ", " recalled ", " explained ",
                        " insisted ", " argued ",
                    )
                    if any(attr in _stripped_evidence.lower()
                           for attr in _STRUCTURAL_ATTRIBUTION):
                        continue
                    # Suppress short structural transitions: evidence that
                    # is purely a sentence-boundary + conjunction (". Yet",
                    # ". But", ". In other words,") with no quoted content.
                    if _stripped_evidence and _stripped_evidence[0] in '.;:,':
                        continue
                    # --- Tech/industry jargon filter -------------------------
                    # Short quoted terms (≤3 words) that are established
                    # industry terminology should not be flagged as scare
                    # quotes.  Identified via Virtue AI acqui-hire article
                    # (Jun 2026): "agentic AI", "agents", "agentic", and
                    # "acqui-hire" are standard tech terms, not ironic usage.
                    # ---------------------------------------------------------
                    _TECH_JARGON = {
                        "agentic ai", "agentic", "agents", "agent",
                        "acqui-hire", "acquihire",
                        "zero-day", "zero day",
                        "open source", "open-source",
                        "fine-tune", "fine-tuning",
                        "red team", "red teaming",
                        "guardrails", "alignment",
                        "frontier", "frontier ai",
                        "model", "models",
                        "inference", "token", "tokens",
                        "embeddings", "embeddings",
                        "compute", "latency",
                        "hallucination", "hallucinations",
                        # Added from MIT Tech Review AI agents article
                        # (Jun 2025): explanatory/pedagogical technical
                        # terms that are quoted for reader clarity, not
                        # editorial distancing.
                        "flash crash",
                        "reward hacking",
                        "prompt injection", "prompt injections",
                        "think", "thinking",
                        "talk themselves",
                        "tool", "tools",
                        # Added from MIT Tech Review world models article
                        # (Jul 4, 2026): "world model" is established AI
                        # research terminology, not editorial distancing.
                        "world model", "world models",
                    }
                    # Strip trailing punctuation before jargon lookup —
                    # quoted terms often retain commas/periods from the
                    # original text (e.g. "zero-day," → "zero-day").
                    # Discovered in MIT Tech Review AI agents article
                    # (Jul 4, 2026 iteration): "zero-day," was not
                    # matching the jargon set because of the trailing
                    # comma.
                    _quoted_clean = _quoted.lower().rstrip('.,;:!?')
                    if _quoted_clean in _TECH_JARGON:
                        continue
                    # --- Definitional introduction filter --------------------
                    # Short quoted terms (≤3 words) followed immediately by
                    # a definitional or explanatory clause ("X, whose",
                    # "X, which", "X, meaning", "X — a type of") are being
                    # introduced as coined terminology, not undercut with
                    # scare quotes.  The author is explaining what the term
                    # means, not distancing from it.
                    #
                    # Discovered in Gizmodo Brain2Qwerty v2 article (Jun 30,
                    # 2026): '"auto-research" AI agents, whose task is to
                    # autonomously hone the decoding process' — Meta's own
                    # coined term being introduced, not journalist skepticism.
                    # ---------------------------------------------------------
                    if _word_count <= 3:
                        _def_lookahead = text[end:min(len(text), end + 40)].lower()
                        _def_lookahead = re.sub(r'\s+', ' ', _def_lookahead)
                        # Only match within the same clause — stop at sentence
                        # boundaries to avoid cross-sentence false positives.
                        # e.g. '"points," not actual cash. Which suggests...'
                        # should NOT be treated as definitional.
                        _sent_break = re.search(r'[.!?]\s', _def_lookahead)
                        if _sent_break:
                            _def_lookahead = _def_lookahead[:_sent_break.start()]
                        _DEFINITIONAL_CUES = (
                            ", whose ", ", which ",
                            " whose ", " which ",
                            ", meaning ", ", i.e.", ", i.e.,",
                            " — a ", " — an ", "—a ", "—an ",
                            " - a ", " - an ",
                            ", a type of", ", a kind of",
                            ", a form of", ", a class of",
                        )
                        if any(cue in _def_lookahead for cue in _DEFINITIONAL_CUES):
                            continue
                    # Short quotes (≤3 words): filter if in product-naming
                    # or attribution context
                    if _word_count <= 3:
                        _lookback = text[max(0, start - 80):start].lower()
                        _lookback = re.sub(r'\s+', ' ', _lookback)
                        _PRODUCT_NAMING = (
                            "rely on", "instead rely",
                            " dubbed ", " named ", " termed ",
                            " called ", "(called ",
                            "reach at least", "monthly active",
                            "will use", "would use",
                            "giving one", "giving a",
                            "for a ",
                        )
                        if any(verb in _lookback for verb in _PRODUCT_NAMING):
                            continue
                        # -------------------------------------------------------
                        # Attribution filter for short scare-quote candidates.
                        # In interview-heavy and profile articles, single words
                        # and short phrases appear in quotes because they are
                        # direct speech from a named source, not editorial
                        # scare quotes.  Suppress when the lookback (80 chars)
                        # contains attribution context.
                        #
                        # Discovered in Guardian DeepMind philosopher profile
                        # (Jun 28, 2026): "obvious", "enthusiastic",
                        # "tombstone" were flagged as scare quotes but are
                        # direct quotations from named interview subjects
                        # (Shane Legg, Gabriel's brother, etc.).
                        # -------------------------------------------------------
                        _ATTRIBUTION_SHORT = (
                            " told me ", " tells me ",
                            " told us ", " tells us ",
                            "it was ", "it is ",
                            " calls ", " called ",
                            " describes as ", " described as ",
                            " he says", " she says",
                            " he said", " she said",
                            " they call ", " they called ",
                            " what he call", " what she call",
                            " what they call",
                            " refers to as ",
                            " known as ",
                            # Firm/org-level attribution (financial journalism)
                            " said it ", " said the ", " said that ",
                            " says it ", " says the ", " says that ",
                            " added that ", " adds that ",
                            # "wrote" — common in analyst-note attribution
                            # ("Luria wrote in a note", "Sebastian wrote").
                            # Discovered in MarketWatch Meta cloud pivot
                            # article (Jul 1, 2026): "rational" flagged as
                            # scare quote when Baird's Sebastian wrote it.
                            " wrote ", " wrote in ", " writes ",
                            " writes in ", " wrote that ",
                        )
                        if any(attr in _lookback for attr in _ATTRIBUTION_SHORT):
                            continue
                        # Also check forward context (80 chars after the
                        # quote) for post-quote attribution ("he said",
                        # "she told me", "they explained", "Jefferies said")
                        _lookahead = text[end:min(len(text), end + 80)].lower()
                        _lookahead = re.sub(r'\s+', ' ', _lookahead)
                        _POST_ATTRIBUTION = (
                            " he said", " she said", " they said",
                            " he told ", " she told ",
                            " he recalled", " she recalled",
                            " he explained", " she explained",
                            " he noted", " she noted",
                            " he added", " she added",
                            # "wrote" — analyst notes use "X wrote in a note"
                            " he wrote", " she wrote",
                        )
                        if any(attr in _lookahead for attr in _POST_ATTRIBUTION):
                            continue
                        # --- Firm/organization attribution filter --------
                        # In financial and analyst coverage, quotes are
                        # attributed to firms ("Mizuho said", "Jefferies
                        # said", "BMO Capital said") rather than personal
                        # pronouns.  Check for capitalized-word + attribution
                        # verb within 60 chars after the quote.
                        #
                        # Discovered in Stocktwits Meta cloud analyst
                        # reactions article (Jul 2026): "strategic" flagged
                        # as scare quote when Jefferies said it in an analyst
                        # note.
                        # -------------------------------------------------
                        _ORG_ATTR_PAT = re.compile(
                            r",?\s+[a-z]+(?:\s+[a-z]+)?\s+"
                            r"(?:said|says|added|adds|noted|notes|wrote"
                            r"|reported|explained|argued|called|described)"
                        )
                        # Use wider window (120 chars) for org attribution —
                        # financial journalism attribution strings can be
                        # long: "Baird analyst Colin Sebastian wrote in a
                        # Wednesday note" = 82 chars after the quoted word.
                        # Discovered in MarketWatch Meta cloud pivot article
                        # (Jul 1, 2026): "rational" attributed to Sebastian
                        # but "wrote" was at char 80 — just outside the
                        # standard 80-char window.
                        _org_lookahead = text[end:min(len(text), end + 120)].lower()
                        _org_lookahead = re.sub(r'\s+', ' ', _org_lookahead)
                        if _ORG_ATTR_PAT.search(_org_lookahead):
                            continue
                    # Longer quotes (>3 words): filter if preceded by
                    # personal or organizational attribution
                    else:
                        _lookback = text[max(0, start - 80):start].lower()
                        # Normalize whitespace in lookback for cross-line matching
                        _lookback = re.sub(r'\s+', ' ', _lookback)
                        _DIRECT_QUOTE = (
                            " said that ", " says that ",
                            " replied that ", " wrote that ",
                            " told ", " recalled ",
                            " said he ", " said she ",
                            " said they ", " saying ",
                            " calls ", " called ",
                            " he says,", " she says,",
                            " he said,", " she said,",
                            " describes as ", " described as ",
                            " what he call", " what she call",
                            " what they call",
                        )
                        if any(verb in _lookback for verb in _DIRECT_QUOTE):
                            continue
                        # --- Paragraph-level firm attribution filter -----
                        # In financial journalism, longer quoted phrases
                        # are often attributed to analyst firms or research
                        # houses earlier in the same paragraph (e.g.,
                        # 'Mizuho said it does not believe ... sees it
                        # "more as planning for all potential scenarios"').
                        # Check a wider window (200 chars) for org-level
                        # attribution verbs preceded by capitalized names.
                        #
                        # Discovered in Stocktwits Meta cloud analyst
                        # reactions article (Jul 2026): "a margin of safety
                        # to medium-term EPS" flagged as ironic quotation
                        # when Mizuho attributed the phrase in the same
                        # paragraph.
                        # ------------------------------------------------
                        _wide_lookback = text[max(0, start - 200):start].lower()
                        _wide_lookback = re.sub(r'\s+', ' ', _wide_lookback)
                        _ORG_QUOTE = (
                            " said it ", " said the ", " said that ",
                            " says it ", " says the ", " says that ",
                            " added that ", " adds that ",
                            " noted that ", " notes that ",
                            " wrote that ", " argued that ",
                            # Broader attribution verbs — financial/analyst
                            # articles use "called", "believes", "contends"
                            # before long quoted clauses separated by many
                            # intervening words.
                            # Discovered in MarketWatch Meta cloud pivot
                            # article (Jul 1, 2026): "to fund more, not
                            # less, capex." is Thill's direct quote, but
                            # "He believes" is 200 chars back and "called"
                            # is further still.
                            " called ", " calls ",
                            " believes ", " contends ",
                            " predicted ", " predicts ",
                            " expects ", " expected ",
                            " suggested ", " suggests ",
                            " maintained ", " maintains ",
                            " estimated ", " estimates ",
                        )
                        if any(verb in _wide_lookback for verb in _ORG_QUOTE):
                            continue
                        # Also check forward context for longer quotes:
                        # post-quote attribution like '," Mizuho said.'
                        _long_lookahead = text[end:min(len(text), end + 60)].lower()
                        _long_lookahead = re.sub(r'\s+', ' ', _long_lookahead)
                        _LONG_POST_ATTR = (
                            " said", " says", " added", " adds",
                            " noted", " notes", " wrote", " reported",
                            " explained", " argued", " called",
                        )
                        if any(attr in _long_lookahead for attr in _LONG_POST_ATTR):
                            continue

                # --- Catastrophizing: dream/sleep narrative filter -----------
                # "nightmare" and "nightmarish" in proximity to dream/sleep/
                # wake context are empathetic narrative devices (e.g.
                # "had a dream ... wake up from such a nightmare") commonly
                # used in medical/health articles to build empathy for patients
                # with paralysis or neurodegenerative conditions.  These are
                # NOT catastrophizing about tech companies.
                #
                # Discovered in Gizmodo Brain2Qwerty v2 article (Jun 30,
                # 2026): "to wake up from such a nightmare—and to recall
                # what it's like to be able to freely use your voice—feels
                # like a liberation."
                # ---------------------------------------------------------
                if device_type == "catastrophizing":
                    _cat_lower = match.group().lower()
                    if "nightmare" in _cat_lower or "nightmarish" in _cat_lower:
                        _cat_ctx_start = max(0, start - 150)
                        _cat_ctx_end = min(len(text), end + 150)
                        _cat_context = text[_cat_ctx_start:_cat_ctx_end].lower()
                        _DREAM_CONTEXT = (
                            "dream", "wake up", "woke up", "waking",
                            "sleep", "asleep", "slumber",
                        )
                        if any(w in _cat_context for w in _DREAM_CONTEXT):
                            continue

                # --- Loaded language: medical-context filter ----------------
                # "invasive" is a standard medical/surgical term (invasive
                # vs non-invasive procedures, invasive brain surgery).  When
                # it appears in proximity to medical/surgical vocabulary,
                # suppress the loaded_language match.
                #
                # Discovered in Gizmodo Brain2Qwerty v2 article (Jun 30,
                # 2026): "extremely invasive, complex, and expensive brain
                # surgery" and "non-invasive" brain-computer interfaces are
                # technical descriptions, not loaded editorial language.
                # ---------------------------------------------------------
                if device_type == "loaded_language":
                    _ll_lower = match.group().lower()
                    if _ll_lower == "invasive":
                        _ll_ctx_start = max(0, start - 80)
                        _ll_ctx_end = min(len(text), end + 80)
                        _ll_context = text[_ll_ctx_start:_ll_ctx_end].lower()
                        _MEDICAL_TERMS = (
                            "surgery", "surgical", "procedure",
                            "neuroprosthetic", "brain", "non-invasive",
                            "noninvasive", "implant", "electrode",
                            "medical", "clinical", "neurosurg",
                            "craniotomy", "biopsy",
                        )
                        if any(w in _ll_context for w in _MEDICAL_TERMS):
                            continue

                # --- Emotional appeal: factual medical condition filter ------
                # "unable to speak/nod/respond" in articles about medical
                # conditions (paralysis, ALS, locked-in syndrome, BCI) is a
                # factual description of the patient condition, not an
                # editorial emotional appeal designed to manipulate the reader.
                #
                # Discovered in Gizmodo Brain2Qwerty v2 article (Jun 30,
                # 2026): "had a dream in which we were unable to speak or
                # move" describes the actual experience of paralysis patients,
                # the very people the technology aims to help.
                # ---------------------------------------------------------
                if device_type == "emotional_appeal":
                    _ea_lower = match.group().lower()
                    if "unable" in _ea_lower and any(
                        w in _ea_lower for w in ("speak", "nod", "respond")
                    ):
                        _ea_ctx_start = max(0, start - 120)
                        _ea_ctx_end = min(len(text), end + 120)
                        _ea_context = text[_ea_ctx_start:_ea_ctx_end].lower()
                        _MEDICAL_CONDITION_TERMS = (
                            "paralyz", "paralys", "als", "amyotrophic",
                            "locked-in", "locked in", "anarthria",
                            "neurodegenerative", "patient", "condition",
                            "brain", "lesion", "syndrome", "disorder",
                            "communicate", "dream",
                        )
                        if any(w in _ea_context for w in _MEDICAL_CONDITION_TERMS):
                            continue

                seen_spans.add(span_key)
                evidence = match.group().strip()
                # Truncate very long matches for readability
                if len(evidence) > 200:
                    evidence = evidence[:200] + "..."

                devices.append(
                    FramingDevice(
                        device_type=device_type,
                        evidence_text=evidence,
                        start=start,
                        end=end,
                    )
                )

    # Sort by position in text
    devices.sort(key=lambda d: d.start)

    # --- Post-filter: self_referential_investigation ---
    # When source_publication is provided, drop self_referential_investigation
    # matches where the cited publication does NOT match the source.  A cross-
    # publication citation (e.g. Memeburn citing "Bloomberg reported") is
    # standard attribution, not self-referential investigation.  Pattern 3
    # (reflexive: "our investigation") is always kept because it's inherently
    # self-referential regardless of which publication wrote the article.
    #
    # Even WITHOUT source_publication, suppress citations of well-known wire
    # services and news agencies — these are ALWAYS cross-citations (no
    # article written BY Bloomberg/Reuters/AP would say "Bloomberg reported";
    # they'd say "we reported" or just report directly).
    #
    # Discovered in Stocktwits Meta cloud analyst article (Jul 2026):
    # "Bloomberg reported" flagged as self-referential when it's standard
    # cross-publication attribution.
    _WIRE_SERVICES = {
        "bloomberg", "reuters", "associated press", "ap ",
        "financial times", "wall street journal", "wsj",
    }
    filtered_devices_wire: list[FramingDevice] = []
    for dev in devices:
        if dev.device_type == "self_referential_investigation":
            evidence_lower = dev.evidence_text.lower()
            # Reflexive patterns are always kept
            if any(kw in evidence_lower for kw in (
                "our investigation", "our reporting", "our analysis",
                "our findings", "our review", "our examination",
                "our inquiry", "our report",
                "this publication", "this outlet", "this newsroom",
                "this paper",
            )):
                filtered_devices_wire.append(dev)
                continue
            # Wire service citations without source_publication are always
            # cross-citations — suppress
            if not source_publication and any(
                ws in evidence_lower for ws in _WIRE_SERVICES
            ):
                logger.debug(
                    "Suppressed self_referential_investigation (wire cross-cite): %s",
                    dev.evidence_text[:80],
                )
                continue
        filtered_devices_wire.append(dev)
    devices = filtered_devices_wire

    if source_publication:
        _source_pub_lower = source_publication.lower()
        filtered_devices: list[FramingDevice] = []
        for dev in devices:
            if dev.device_type != "self_referential_investigation":
                filtered_devices.append(dev)
                continue
            evidence_lower = dev.evidence_text.lower()
            # Reflexive patterns (already checked above, but kept for safety)
            if any(kw in evidence_lower for kw in (
                "our investigation", "our reporting", "our analysis",
                "our findings", "our review", "our examination",
                "our inquiry", "our report",
                "this publication", "this outlet", "this newsroom",
                "this paper",
            )):
                filtered_devices.append(dev)
                continue
            # For named-publication patterns, keep only if the cited
            # publication matches the source publication
            if _source_pub_lower in evidence_lower:
                filtered_devices.append(dev)
                continue
            # Dropped: cross-publication citation, not self-referential
            logger.debug(
                "Suppressed self_referential_investigation (source=%s): %s",
                source_publication, dev.evidence_text[:80],
            )
        devices = filtered_devices

    # Post-pass: kicker framing detection
    # Check if the final paragraph introduces negative context discordant
    # from the article body.  Only fires if the last ~400 characters contain
    # negative signals not present in the article's primary topic.
    kicker_region = text[-400:] if len(text) > 400 else text
    for pattern in _KICKER_NEGATIVE_SIGNALS:
        for match in pattern.finditer(kicker_region):
            # Calculate absolute position in text
            abs_start = len(text) - len(kicker_region) + match.start()
            abs_end = len(text) - len(kicker_region) + match.end()
            evidence = match.group().strip()
            devices.append(
                FramingDevice(
                    device_type="kicker_framing",
                    evidence_text=evidence,
                    start=abs_start,
                    end=abs_end,
                )
            )
            break  # One detection per article is sufficient

    # Post-pass: analogy stacking (fires when 3+ distinct analogy markers found)
    devices.extend(_detect_analogy_stacking(text))

    # Post-pass: speculative framing (fires when 5+ cumulative hedges found)
    devices.extend(_detect_speculative_framing(text))

    # Post-pass: trend bundling (fires when 3+ distinct companies are
    # bundled in comparison context — normalising/contextualising frame)
    devices.extend(_detect_trend_bundling(text))

    # Post-pass: social proof amplification — when articles cite reaction
    # counts (likes, thumbs-up, hearts, shares, retweets) to quantify and
    # amplify a quoted position, converting individual opinion into
    # collective sentiment.
    devices.extend(_detect_social_proof_amplification(text))

    # Post-pass: delayed defense — corporate response buried in the last
    # 35% of the article, after the reader has absorbed the accusatory
    # framing without counter-narrative.
    devices.extend(_detect_delayed_defense(text))

    # Re-sort after adding post-pass results
    devices.sort(key=lambda d: d.start)

    return devices


def summarize_framing(devices: list[FramingDevice]) -> dict[str, int]:
    """Summarize detected framing devices by type.

    Args:
        devices: List of FramingDevice objects.

    Returns:
        Dict mapping device type to count.
    """
    counts: dict[str, int] = {}
    for device in devices:
        counts[device.device_type] = counts.get(device.device_type, 0) + 1
    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
