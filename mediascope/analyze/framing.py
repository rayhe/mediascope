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
    re.compile(r"\bspoke on (?:the )?condition (?:of )?anonymity\b", re.IGNORECASE),
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
        r"end of|death of|demise of|downfall of)\b",
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
        r"\b(?:quietly|secretly|covertly|surreptitiously|"
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
        r"exploitation|slave|sweatshop)\b",
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
]

# Timeline implication: editorial technique suggesting cover-up or reactive behavior
_TIMELINE_IMPLICATION_PATTERNS: list[re.Pattern] = [
    # "deleted/removed/pulled X after Y reported/revealed"
    re.compile(
        r"\b(?:deleted?|removed?|pulled|scrubbed|stripped|purged)\b"
        r".{0,80}?"
        r"\b(?:after|once|when|following)\b"
        r".{0,60}?"
        r"\b(?:reported?|revealed?|published|discovered|exposed|found|uncovered)\b",
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
}


def detect_framing_devices(text: str) -> list[FramingDevice]:
    """Detect framing devices in article text.

    Scans for patterns associated with 8 types of editorial framing:
    guilt_by_association, anonymous_authority, catastrophizing,
    false_balance, selective_omission_signal, emotional_appeal,
    straw_man, and loaded_language.

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
