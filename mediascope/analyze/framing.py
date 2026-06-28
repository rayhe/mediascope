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
        r"free fall|freefall|nosedive)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:could destroy|will destroy|threatens to destroy|"
        r"threatens to upend|could wipe out|"
        r"death of|demise of|downfall of)\b",
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
        r"cataclysmic|seismic shift|tectonic shift)\b",
        re.IGNORECASE,
    ),
    # "cultural dead end" / "dead end" as terminal-trajectory framing
    re.compile(
        r"\b(?:cultural dead end|dead end|cultural collapse|"
        r"model collapse|ecological harm|ecological collapse)\b",
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
        r"staggering|mastermind(?:ed)?|"
        r"turned a blind eye|strike fear|struck fear|"
        r"indefensible|abusive|defamatory|"
        r"drastic(?:ally)?|superficial(?:ly)?|"
        r"reckless(?:ly)?|egregious(?:ly)?|flagrant(?:ly)?"
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
        r"without (?:notice|disclosure|announcing|telling)|"
        r"behind (?:closed doors|the scenes))\b",
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
        r"mandatory|compulsory|forced\s+to\s+(?:install|use|adopt|accept))\b",
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
        r"fig\s+leaf)\b",
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
        r"each\s+(?:\w+\s+)?(?:violation|breach|instance)|"
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


# Rhetorical question framing: questions that imply negligence, incompetence,
# or failure without directly asserting it.  "Were there even guardrails?"
# is more devastating than "there were no guardrails" because it positions
# the audience to draw the negative conclusion themselves.  Common in
# accountability journalism where sources use interrogative form to
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
    # as defiant against foreign pressure
    re.compile(
        r"\b(?:not concerned|not deterred|will not (?:be )?(?:deterred|swayed|"
        r"intimidated|bullied)|undeterred|defiant|defy|defied|defying|"
        r"will always act in .{0,30}?national interest|"
        r"sovereign(?:ty)?|"
        r"will go ahead despite|"
        r"will not back down|standing firm|stood firm)\b",
        re.IGNORECASE,
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
        r"wake.?up call|cautionary|warning sign|red flag)\b",
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
]

_DEVICE_PATTERNS["confession_framing"] = _CONFESSION_FRAMING_PATTERNS


def _detect_analogy_stacking(text: str) -> list[FramingDevice]:
    """Detect analogy stacking — 3+ distinct analogies for the same subject.

    Returns a list of FramingDevice objects (one per matched analogy marker)
    only if the threshold (3+) is met.  If fewer than 3 markers are found,
    returns an empty list.
    """
    markers: list[FramingDevice] = []
    seen_spans: set[tuple[int, int]] = set()

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

            seen_spans.add((start, end))
            evidence = match.group().strip()
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


def detect_framing_devices(text: str) -> list[FramingDevice]:
    """Detect framing devices in article text.

    Scans for 30 pattern-matched device types plus 4 structural
    post-pass types (34 total).

    Pattern-matched (30): guilt_by_association, anonymous_authority,
    catastrophizing, false_balance, selective_omission_signal,
    emotional_appeal, straw_man, loaded_language, refusal_amplification,
    juxtaposition, timeline_implication, power_asymmetry,
    military_techno_optimism, selective_rehabilitation,
    rhetorical_question, ironic_quotation, isolation_framing,
    pressure_language, geopolitical_regulatory_pressure,
    self_referential_investigation, sovereignty_framing,
    scale_magnitude, ceo_personalization, litigation_framing,
    corporate_reassurance_undercut, sarcastic_correction,
    hypocrisy_frame, outsourced_intensity, confession_framing,
    and precedent_analogy.

    Structural post-pass (4): kicker_framing, analogy_stacking,
    speculative_framing, trend_bundling.

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
                    }
                    if _quoted.lower() in _TECH_JARGON:
                        continue
                    # Short quotes (≤3 words): filter if in product-naming context
                    if _word_count <= 3:
                        _lookback = text[max(0, start - 60):start].lower()
                        _PRODUCT_NAMING = (
                            "rely on", "instead rely",
                            " dubbed ", " named ", " termed ",
                            "reach at least", "monthly active",
                            "will use", "would use",
                            "giving one", "giving a",
                            "for a ",
                        )
                        if any(verb in _lookback for verb in _PRODUCT_NAMING):
                            continue
                    # Longer quotes (>3 words): filter if preceded by
                    # personal attribution ("X said that he/she had")
                    else:
                        _lookback = text[max(0, start - 60):start].lower()
                        # Normalize whitespace in lookback for cross-line matching
                        _lookback = re.sub(r'\s+', ' ', _lookback)
                        _DIRECT_QUOTE = (
                            " said that ", " says that ",
                            " replied that ", " wrote that ",
                            " told ", " recalled ",
                            " said he ", " said she ",
                            " said they ", " saying ",
                        )
                        if any(verb in _lookback for verb in _DIRECT_QUOTE):
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
