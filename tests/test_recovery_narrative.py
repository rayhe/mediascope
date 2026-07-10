"""Tests for recovery_narrative framing detection.

Discovery article: MarketWatch "Meta's stock rebounds as agentic AI coding and
custom chips ease spending fears" (Jul 10, 2026).

Recovery narrative is a three-beat article architecture:
  Beat 1 (Decline): Prior weakness, criticism, stock decline
  Beat 2 (Catalyst): Product launch, positive data, analyst upgrade
  Beat 3 (Recovery projection): Forward-looking analyst projections

Distinct from financial_reassurance (single pivot), bull_bear_structuring
(both sides), investor_advisory (prescribes behavior), and overbuilding_narrative
(frames spending as excessive).
"""

import re
import pytest

# ── Detection patterns for recovery_narrative ──

BEAT_1_DECLINE_PATTERNS = [
    re.compile(r"has\s+long\s+been\s+criticized", re.I),
    re.compile(r"stock\s+(?:was|is)\s+down\s+\d", re.I),
    re.compile(r"(?:insufficient|poor|disappointing)\s+return", re.I),
    re.compile(r"(?:spending|overspending|capex)\s+(?:fears|concerns|worries)", re.I),
    re.compile(r"(?:investors|the market)\s+(?:saw|see|seen)\s+insufficient", re.I),
    re.compile(r"(?:fallen|fell|dropped|tumbled)\s+\d+%?\s+(?:this|last)\s+(?:year|quarter|month)", re.I),
    re.compile(r"(?:strategy|approach)\s+has\s+(?:long\s+)?been\s+(?:criticized|questioned|scrutinized)", re.I),
]

BEAT_2_CATALYST_PATTERNS = [
    re.compile(r"(?:investors?|the market)\s+(?:cheered|welcomed|applauded|embraced)", re.I),
    re.compile(r"(?:getting|received|getting|saw)\s+a\s+boost", re.I),
    re.compile(r"(?:ease|easing|eased|alleviate|alleviating)\s+(?:spending\s+)?(?:fears|concerns|worries)", re.I),
    re.compile(r"getting\s+serious\s+about", re.I),
    re.compile(r"(?:warming\s+up|warmed\s+up)\s+to", re.I),
    re.compile(r"(?:stock|shares)\s+(?:rose|climbed|surged|jumped|rallied|rebounded)\s+\d", re.I),
    re.compile(r"(?:sign|signal|indication)\s+that\s+(?:Meta|the\s+company)\s+is", re.I),
]

BEAT_3_RECOVERY_PATTERNS = [
    re.compile(r"(?:analyst|strategist|researcher)\s+\w+\s+(?:believes?|projects?|estimates?|anticipates?|expects?)", re.I),
    re.compile(r"up\s+to\s+\d+%?\s+(?:lower|higher|more|less)", re.I),
    re.compile(r"(?:high[- ]margin|incremental|additional)\s+(?:revenue|opportunity|growth)", re.I),
    re.compile(r"(?:improve|improving)\s+the\s+(?:cost|revenue)\s+(?:curve|trajectory|outlook)", re.I),
    re.compile(r"(?:larger|greater|bigger)\s+than\s+(?:we|the\s+Street|analysts?)\s+(?:previously\s+)?(?:expected|underwrote|estimated|forecast)", re.I),
    re.compile(r"(?:continue|likely\s+to\s+continue)\s+(?:ramping|building|expanding|growing)", re.I),
]


def detect_recovery_narrative(text: str) -> dict:
    """Detect recovery narrative three-beat structure."""
    beat_1_hits = []
    beat_2_hits = []
    beat_3_hits = []

    for pat in BEAT_1_DECLINE_PATTERNS:
        for m in pat.finditer(text):
            beat_1_hits.append(m.group())

    for pat in BEAT_2_CATALYST_PATTERNS:
        for m in pat.finditer(text):
            beat_2_hits.append(m.group())

    for pat in BEAT_3_RECOVERY_PATTERNS:
        for m in pat.finditer(text):
            beat_3_hits.append(m.group())

    all_three = bool(beat_1_hits) and bool(beat_2_hits) and bool(beat_3_hits)

    return {
        "detected": all_three,
        "beat_1_decline": beat_1_hits,
        "beat_2_catalyst": beat_2_hits,
        "beat_3_recovery": beat_3_hits,
        "confidence": "HIGH" if all_three and len(beat_1_hits) + len(beat_2_hits) + len(beat_3_hits) >= 4 else "MEDIUM" if all_three else "LOW",
    }


# ── Test article: MarketWatch Meta stock rebound (Jul 10, 2026) ──

MARKETWATCH_META_REBOUND = """
Investors are warming up to Meta Platforms' artificial-intelligence strategy
after the company's most recent business updates.

Meta's AI capabilities are getting a boost with Thursday's launch of Muse
Spark 1.1, an agentic coding model comparable to leading industry benchmarks
from OpenAI and Anthropic.

It's seen as a sign that Meta is getting serious about its enterprise coding
offerings. Muse Spark 1.1 is the company's first pay-to-use model, BNP
Paribas analyst Nick Jones wrote in a Thursday note — meaning that it now has
an opportunity to directly monetize its AI products.

Investors cheered the development, with shares of Meta META rising 4.7% on
Thursday.

The company's AI strategy has long been criticized, as investors saw
insufficient return on the billions of dollars that Meta poured into hiring
top researchers for Meta Superintelligence Labs and toward building data
centers.

Earlier this month, reports of Meta's plan to monetize its data-center
capacity through a new Meta Compute division led to mixed analyst reactions.

However, Jones flagged that "the potential cloud offering and fees for access
to its AI model all serve to provide incremental revenue beyond its core
advertising revenue." These developments "demonstrate a clear immediate path
to high return on Meta's AI investments," he added.

Investor sentiment also received a boost from a Reuters report Thursday
suggesting that Meta is moving its proprietary in-house chips, dubbed Iris,
into mass production in September.

The Reuters report also revealed that Meta plans to double its data-center
compute capacity from 7 gigawatts in 2026 to 14 gigawatts in 2027, which
initially led shares of Meta to fall Thursday morning on overspending fears.

Jefferies analyst Brent Thill highlighted in a Wednesday note that Meta is
likely to continue ramping up its AI spending and cloud ambitions.

Deutsche Bank analyst Benjamin Black believes Meta could achieve up to 35%
lower data-center costs in 2027 using a combination of Iris and Nvidia chips.

"MTIA progress should improve the cost curve over time, particularly for
inference and core recommendation workloads," Black wrote in a Thursday note.
"The incremental cost may not be as high as feared, while the incremental
high-margin revenue opportunity may be larger than we — and the Street —
previously underwrote."
"""


class TestRecoveryNarrative:
    """Tests for recovery_narrative framing detection."""

    def test_marketwatch_meta_rebound_detected(self):
        """MarketWatch Meta stock rebound article triggers recovery_narrative."""
        result = detect_recovery_narrative(MARKETWATCH_META_REBOUND)
        assert result["detected"], (
            f"Recovery narrative should be detected. "
            f"Beat 1: {result['beat_1_decline']}, "
            f"Beat 2: {result['beat_2_catalyst']}, "
            f"Beat 3: {result['beat_3_recovery']}"
        )

    def test_beat_1_decline_detected(self):
        """Beat 1 decline patterns fire on criticism/decline language."""
        result = detect_recovery_narrative(MARKETWATCH_META_REBOUND)
        assert len(result["beat_1_decline"]) >= 2, (
            f"Expected 2+ decline hits, got {len(result['beat_1_decline'])}: "
            f"{result['beat_1_decline']}"
        )

    def test_beat_2_catalyst_detected(self):
        """Beat 2 catalyst patterns fire on rebound/cheer language."""
        result = detect_recovery_narrative(MARKETWATCH_META_REBOUND)
        assert len(result["beat_2_catalyst"]) >= 2, (
            f"Expected 2+ catalyst hits, got {len(result['beat_2_catalyst'])}: "
            f"{result['beat_2_catalyst']}"
        )

    def test_beat_3_recovery_detected(self):
        """Beat 3 recovery patterns fire on analyst projections."""
        result = detect_recovery_narrative(MARKETWATCH_META_REBOUND)
        assert len(result["beat_3_recovery"]) >= 2, (
            f"Expected 2+ recovery hits, got {len(result['beat_3_recovery'])}: "
            f"{result['beat_3_recovery']}"
        )

    def test_high_confidence(self):
        """Article with 4+ total beat hits across all 3 beats = HIGH confidence."""
        result = detect_recovery_narrative(MARKETWATCH_META_REBOUND)
        assert result["confidence"] == "HIGH", (
            f"Expected HIGH confidence, got {result['confidence']}"
        )

    def test_neutral_wire_article_not_detected(self):
        """Neutral Reuters wire article should not trigger recovery_narrative."""
        neutral_text = """
        Meta Platforms on Thursday released long-awaited developer access to
        its Muse Spark AI model alongside an upgraded version, pitting it
        directly against the business models of Anthropic and OpenAI in
        charging for use of its AI. The social media giant touted Muse Spark
        1.1 as its most capable model for real-world coding and agentic tasks.
        Meta said the upgraded model can write and debug code, use software
        and external tools, understand text, images and video. Developers in
        the United States can now access Muse Spark in public preview on Meta
        Model API. The access is priced at $1.25 per million input tokens.
        """
        result = detect_recovery_narrative(neutral_text)
        assert not result["detected"], (
            "Neutral wire article should not trigger recovery_narrative"
        )

    def test_negative_only_article_not_detected(self):
        """Article with only decline language and no recovery should not trigger."""
        decline_only = """
        Meta's AI strategy has long been criticized. The stock is down 8.5%
        year-to-date and has fallen from its all-time high. Investors saw
        insufficient return on the billions spent on data centers. Spending
        fears have intensified as capital expenditure guidance rose again.
        The company's Reality Labs division continues to hemorrhage billions.
        """
        result = detect_recovery_narrative(decline_only)
        assert not result["detected"], (
            "Decline-only article should not trigger recovery_narrative — "
            "needs catalyst and recovery beats"
        )


class TestCompetitivePositioningBidirectional:
    """Tests for bidirectional competitive_positioning detection."""

    def test_negative_competitor_elevated(self):
        """Competitor elevated over subject (classic negative variant)."""
        text = "All this may be good news for the upcoming Apple Glasses"
        assert re.search(r"good\s+news\s+for\s+(?:the\s+)?\w+", text, re.I)

    def test_positive_parity_claim(self):
        """Subject elevated to competitor parity (positive variant)."""
        text = "an agentic coding model comparable to leading industry benchmarks from OpenAI and Anthropic"
        match = re.search(r"comparable\s+to\s+(?:leading\s+)?(?:industry\s+)?benchmarks?\s+from", text, re.I)
        assert match, "Parity claim pattern should be detected"

    def test_positive_outperform_claim(self):
        """Subject outperforming competitors (strong positive variant)."""
        text = "Testing results show that the model outperformed Anthropic's Opus 4.8 and OpenAI's GPT-5.5 on four agentic benchmarks"
        match = re.search(r"outperformed?\s+\w+(?:'s)?\s+\w+", text, re.I)
        assert match, "Outperformance claim should be detected"
