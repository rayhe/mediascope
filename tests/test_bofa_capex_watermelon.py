"""Regression tests for BofA/Barron's capex article + Memeburn Meta Compute analysis.

Tests entity detection, framing analysis, and comma-after-entity lookahead fix.

Source: Barron's "The AI Bill Keeps Growing as Alphabet, Amazon, and Meta Spending
Is Set to Go Through the Roof" (Mackenzie Tatananni, Jul 7, 2026)
and Memeburn "Meta AI Cloud Push Triggers the Biggest Chip Stocks Selloff"
(~Jul 2, 2026).
"""

import pytest
from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices

# === Full article text excerpts ===

BARRONS_BOFA_EXCERPT = (
    "As concerns over heavy artificial-intelligence spending weigh on the "
    "market, new projections from BofA Securities are bound to heighten investor "
    "anxiety rather than soothe it. On Tuesday, the firm raised its capital "
    "spending estimates for three of the largest hyperscalers: Alphabet, Amazon, "
    "and Meta Platforms. Meta's spending outlook received a similar bump, as BofA "
    "hiked its estimate for the current year to $145 billion from $130 billion "
    "and increased its 2027 forecast to $185 billion from $157 billion. The "
    "massive scale of these AI and infrastructure investments has quickly "
    "outpaced what the companies can afford using their regular operating cash "
    "flow. As BofA Securities noted Tuesday, rising memory costs could cause "
    "spending to escalate. The firm cited DRAM spot pricing that suggests a 40% "
    "jump since last quarter. The arrival of new, power-hungry AI models could "
    "also drive up infrastructure costs. The firm highlighted recent commentary "
    "from Meta indicating that its next-generation AI model, Watermelon, "
    "requires 10 times more computing power than Muse Spark, the frontier model "
    "it released in April. BofA's calculations suggest that the cost of building "
    "1 gigawatt of AI data-center capacity could range anywhere from $25 billion "
    "to $45 billion. By 2030, BofA expects Amazon, Alphabet, and Meta to have "
    "58.1, 32.4, and 22.8 gigawatts of installed capacity, respectively."
)

MEMEBURN_EXCERPT = (
    "On July 1, Bloomberg reported that Meta is developing a cloud infrastructure "
    "business to sell access to AI computing power and models. The internal "
    "project called Meta Compute is led by Meta's head of infrastructure, "
    "Santosh Janardhan, and Superintelligence Labs leader Daniel Gross. CEO Mark "
    "Zuckerberg first hinted at the idea during Meta's May shareholder meeting. "
    "Meta's 2026 capital expenditure guidance now sits at $125 to $145 billion, "
    "nearly double what it spent in 2025. As of Q1, the company has committed "
    "$182.9 billion in total AI infrastructure spending. Here's the part most "
    "coverage misses. Meta's own AI products, Llama, Meta AI, Muse Spark, "
    "haven't generated standalone revenue anywhere close to justifying that "
    "spend. Neocloud companies CoreWeave and Nebius fell 10.8% and 12.4%, "
    "respectively. OpenAI's Jalapeño chip, co-developed with Broadcom, targets "
    "another 50% cost reduction when it ships in late 2026. BofA's Bubble Risk "
    "Indicator for semiconductors hit 0.91 in late June, where 1.0 represents "
    "extreme bubble conditions. Chinese hedge funds have called global AI stocks "
    "a super bubble."
)


# === Entity detection tests ===


class TestBarronsEntities:
    """Entity detection on the BofA/Barron's article excerpt."""

    def test_watermelon_comma_lookahead(self):
        """Watermelon followed by comma-requires must be detected (bug fix)."""
        entities = detect_entities(BARRONS_BOFA_EXCERPT)
        names = {e.entity for e in entities}
        assert "Watermelon" in names, (
            "Watermelon not detected in comma-after-entity context "
            "'Watermelon, requires'"
        )

    def test_watermelon_cluster(self):
        """Watermelon must cluster under Meta."""
        entities = detect_entities(BARRONS_BOFA_EXCERPT)
        watermelons = [e for e in entities if e.entity == "Watermelon"]
        assert watermelons, "Watermelon not found"
        assert watermelons[0].cluster == "Meta"

    def test_muse_spark_detected(self):
        entities = detect_entities(BARRONS_BOFA_EXCERPT)
        names = {e.entity for e in entities}
        assert "Muse Spark" in names

    def test_bofa_detected(self):
        entities = detect_entities(BARRONS_BOFA_EXCERPT)
        names = {e.entity for e in entities}
        assert "BofA Securities" in names or "BofA" in names

    def test_hyperscaler_entities(self):
        """All three hyperscalers (Alphabet, Amazon, Meta) must be detected."""
        entities = detect_entities(BARRONS_BOFA_EXCERPT)
        names = {e.entity for e in entities}
        assert "Alphabet" in names or "Google" in names
        assert "Amazon" in names
        assert "Meta Platforms" in names or "Meta" in names


class TestMemburnEntities:
    """Entity detection on the Memeburn Meta Compute article."""

    def test_meta_compute_detected(self):
        entities = detect_entities(MEMEBURN_EXCERPT)
        names = {e.entity for e in entities}
        assert "Meta Compute" in names

    def test_leadership_detected(self):
        entities = detect_entities(MEMEBURN_EXCERPT)
        names = {e.entity for e in entities}
        assert "Santosh Janardhan" in names
        assert "Daniel Gross" in names
        assert "Mark Zuckerberg" in names

    def test_neocloud_entities(self):
        entities = detect_entities(MEMEBURN_EXCERPT)
        names = {e.entity for e in entities}
        assert "CoreWeave" in names
        assert "Nebius" in names

    def test_openai_jalapeno(self):
        entities = detect_entities(MEMEBURN_EXCERPT)
        names = {e.entity for e in entities}
        assert "OpenAI" in names
        assert "Jalapeño" in names
        assert "Broadcom" in names

    def test_muse_spark_and_meta_ai(self):
        entities = detect_entities(MEMEBURN_EXCERPT)
        names = {e.entity for e in entities}
        assert "Muse Spark" in names
        assert "Meta AI" in names


# === Framing device tests ===


class TestBarronsFraming:
    """Framing analysis on the BofA/Barron's article."""

    def test_scale_magnitude_10x(self):
        """'10 times more computing power' is scale_magnitude."""
        devices = detect_framing_devices(BARRONS_BOFA_EXCERPT)
        scale_devices = [d for d in devices if d.device_type == "scale_magnitude"]
        assert any("10 times" in d.evidence_text for d in scale_devices), (
            "scale_magnitude not detected for '10 times more'"
        )

    def test_loaded_language_or_trend(self):
        """Article should trigger at least one framing device."""
        devices = detect_framing_devices(BARRONS_BOFA_EXCERPT)
        assert len(devices) >= 1


class TestMemburnFraming:
    """Framing analysis on the Memeburn article."""

    def test_nearly_double_scale(self):
        """'nearly double what it spent' must now trigger scale_magnitude."""
        devices = detect_framing_devices(MEMEBURN_EXCERPT)
        scale_devices = [d for d in devices if d.device_type == "scale_magnitude"]
        nearly_double = [
            d for d in scale_devices if "nearly double" in d.evidence_text.lower()
        ]
        assert nearly_double, (
            "scale_magnitude not detected for 'nearly double' — "
            "this was a known gap fixed in this iteration"
        )

    def test_loaded_language_bubble(self):
        """'super bubble' must be detected as loaded_language."""
        devices = detect_framing_devices(MEMEBURN_EXCERPT)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert any("bubble" in d.evidence_text.lower() for d in loaded)

    def test_percentage_decline_framing(self):
        """Stock percentage drops (10.8%, 12.4%, 50%) should trigger framing."""
        devices = detect_framing_devices(MEMEBURN_EXCERPT)
        scale_devices = [d for d in devices if d.device_type == "scale_magnitude"]
        # At least one percentage framing should fire
        assert len(scale_devices) >= 1


# === Comma-after-entity lookahead regression ===


class TestCommaLookaheadFix:
    """Regression tests for the comma-after-entity lookahead bug.

    Before the fix, entities with context-sensitive lookaheads (Watermelon,
    Fury, Arena, FAIR) would not match when followed by a comma before the
    disambiguating word. E.g. 'Watermelon, requires' failed because the
    lookahead expected \\s+ but got a comma.
    """

    @pytest.mark.parametrize(
        "text,expected",
        [
            # Watermelon
            (
                "Meta's AI model, Watermelon, requires 10x compute",
                "Watermelon",
            ),
            ("Watermelon requires massive compute", "Watermelon"),
            ("The Watermelon model launches next year", "Watermelon"),
            # Fury
            ("Meta Fury, the smart glasses, cost $499", "Meta Fury"),
            ("Fury is the successor to Ray-Ban Meta", "Fury"),
        ],
    )
    def test_comma_lookahead(self, text, expected):
        entities = detect_entities(text)
        names = {e.entity for e in entities}
        assert expected in names, (
            f"Expected '{expected}' in entities from: '{text}'\n"
            f"Got: {names}"
        )
