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
        r"\b(?:nightmare|horror|terrifying|apocalyptic|"
        r"cataclysmic|seismic shift|tectonic shift)\b",
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
    # Workplace collective despair — mass dissatisfaction + helplessness
    # language deployed to evoke sympathy for employees against institution.
    # Common in tech workplace reporting (e.g., Wired "Dark Mood Inside Meta").
    re.compile(
        r"\b(?:everyone is (?:unhappy|miserable|afraid|terrified)|"
        r"nobody is happy|no one is happy|"
        r"morale (?:is |has |at )(?:rock.?bottom|historically low|all.time low|an? low)|"
        r"no(?:body has a)? choice|we have no choice|"
        r"social contract (?:is |has been )?(?:broken|shattered|dead)|"
        r"can.t (?:even )?feign (?:empathy|concern|care)|"
        r"used to train.{0,20}(?:replace|replacement)|"
        r"train (?:your|their|our) own replacement|"
        r"vibes are (?:horrifically|historically|extremely) (?:low|bad|poor))\b",
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
        r"crushed|obliterated|demolished|annihilated)\b",
        re.IGNORECASE,
    ),
    # Loaded adjectives/nouns characterizing people or organizations
    re.compile(
        r"\b(?:embattled|beleaguered|troubled|scandal-plagued|"
        r"controversial|notorious|disgraced|under fire|"
        r"under siege|besieged|defiant|brazen|arrogant|"
        r"tone-deaf|out of touch)\b",
        re.IGNORECASE,
    ),
    # Scare quotes / hedging language that undermines
    re.compile(
        r"(?:so-called|self-proclaimed|self-styled|self-described)\s+\w+",
        re.IGNORECASE,
    ),
    # Surveillance/security-state language applied to commercial entities
    re.compile(
        r"\b(?:surveillance|wiretap|spying|spy|mass.?identification|"
        r"biometric|facial recognition|face.?recognition|faceprint|"
        r"tracking|monitor(?:ing)?|eavesdrop(?:ping)?)\b"
        r".{0,60}?"
        r"\b(?:consumer|commercial|app|phone|device|glasses|product)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    # "Quietly" as editorial signal of secrecy
    re.compile(
        r"\b(?:quietly|secretly|covertly|surreptitiously|discreetly|"
        r"without (?:notice|disclosure|announcing|telling)|"
        r"behind (?:closed doors|the scenes))\b",
        re.IGNORECASE,
    ),
    # "Dormant" / hidden capability language
    re.compile(
        r"\b(?:dormant|hidden|buried|unreleased|inactive|"
        r"undisclosed|unannounced|under.?the.?radar)\b",
        re.IGNORECASE,
    ),
    # Workplace-specific loaded language — terms that characterize
    # organizational decisions as oppressive or dehumanizing
    re.compile(
        r"\b(?:soul.?crushing|drudge|drudgery|gulag|"
        r"assembly line|human assembly line|data factory|"
        r"draftees?|drafted|disposable|"
        r"menial|dehumanizing|atrocious|brutal|"
        r"exploitation|slave|sweatshop|"
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
        r"protest(?:ed|ing|s)?|petition(?:ed|ing|s)?|"
        r"flyers?|leaflets?|"
        r"countdown\s+to\s+(?:layoff|the\s+layoff)|"
        r"counting\s+down\s+to|"
        r"nihilistic|dystopian|Orwellian|Kafkaesque|"
        r"train(?:ing)?\s+(?:their|your|our|its)\s+(?:own\s+)?replacements?|"
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
    # students, or naive actors to undermine their competence
    re.compile(
        r"\b(?:elementary\s+school|kindergarten|toddler|child(?:ish|like)?|"
        r"naive|naively|"
        r"eager\s+to\s+(?:please|finish|comply|complete)|"
        r"just\s+wants?\s+to\s+please|"
        r"puppy\s+(?:eager|like)|"
        r"blindly\s+(?:follow|obey|comply)|"
        r"rubber.?stamp(?:ing|ed)?)\b",
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
    re.compile(
        r"\b(?:military|Pentagon|law enforcement|police|intelligence|"
        r"surveillance|defense|government|FBI|CIA|NSA|"
        r"special operations|marshals?)\b"
        r".{0,120}?"
        r"\b(?:consumer|mass.?market|commercial|everyday|"
        r"everyone else|ordinary|public|civilian|retail)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    re.compile(
        r"\b(?:consumer|mass.?market|commercial|everyday|"
        r"everyone else|ordinary|public|civilian)\b"
        r".{0,120}?"
        r"\b(?:military|Pentagon|law enforcement|police|intelligence|"
        r"surveillance|defense|government|FBI|CIA|NSA|"
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
        r"\b(?:per\s+(?:violation|breach|instance|day)|"
        r"each\s+(?:violation|breach|instance)|"
        r"bankrupt|ruin|devastat)\b",
        re.IGNORECASE | re.DOTALL,
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
]

_DEVICE_PATTERNS["rhetorical_question"] = _RHETORICAL_QUESTION_PATTERNS


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
    # "is [essentially/basically] [a/an]" — metaphor construction
    re.compile(
        r"\bis (?:essentially |basically |effectively )?(?:a|an) .{3,60}?(?:\.|,|;)",
        re.IGNORECASE,
    ),
    # "think of it as" / "think of slop as"
    re.compile(
        r"\bthink of (?:it|this|them|that|\w+) as\b.{3,60}",
        re.IGNORECASE,
    ),
    # "reminiscent of" / "evokes" / "echoes of"
    re.compile(
        r"\b(?:reminiscent of|evokes?|echoes? of)\b.{3,60}",
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
        r'[\u201d"].{0,10}?'     # end of quote
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
    # "wrongly believe" / "wrongly assume" — editorial verdict after quote
    re.compile(
        r'[\u201d"].{0,200}?'
        r'\b(?:wrongly|mistakenly|naively|incorrectly) '
        r'(?:believe|assume|suggest|claim|imply|argue)',
        re.IGNORECASE | re.DOTALL,
    ),
]

_DEVICE_PATTERNS["ironic_quotation"] = _IRONIC_QUOTATION_PATTERNS


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


def detect_framing_devices(text: str) -> list[FramingDevice]:
    """Detect framing devices in article text.

    Scans for patterns associated with 17 types of editorial framing:
    guilt_by_association, anonymous_authority, catastrophizing,
    false_balance, selective_omission_signal, emotional_appeal,
    straw_man, loaded_language, refusal_amplification,
    juxtaposition, timeline_implication, power_asymmetry,
    military_techno_optimism, selective_rehabilitation,
    rhetorical_question, ironic_quotation, and analogy_stacking.

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
