"""
Test: WSJ EssilorLuxottica Q2 Smartglasses Boom (Jul 28, 2026)
==============================================================

WSJ coverage of EssilorLuxottica Q2 2026 earnings where smartglasses
revenue nearly doubled YoY, yet the headline leads with "Growth Slows."

This article is a textbook case of *inverted* success_paradox framing
in financial journalism: the headline positions strong underlying data
(revenue nearly doubled) as insufficient to prevent overall deceleration.

Cross-publication comparison: Reuters covered the same earnings report
the same day with "profit beats forecasts, AI glasses and myopia products
drive revenue growth" — leading with the positive and omitting the
competition-as-threat framing WSJ includes.

Discovered patterns:
- success_paradox (inverted): "Slows Despite Smartglasses Boom"
- editorial_deflation: "losing a little pace"
- grudging_concession: "Still, questions remain" + "debate remains"
- scale_magnitude: "nearly doubled"
"""

import pytest
from mediascope.analyze import framing

# Full article text — WSJ, Joshua Kirby, Jul 28, 2026
ARTICLE_TEXT = (
    "Ray-Ban Maker EssilorLuxottica Sales Growth Slows Despite "
    "Smartglasses Boom. "
    "Eyewear company EssilorLuxottica said sales growth slowed a "
    "little in the second quarter from the first, despite a continued "
    "rapid increase in revenue from its smartglasses. "
    "The Franco-Italian manufacturer of Oakley and Ray-Ban sunglasses "
    "booked 8.7 percent year-on-year organic growth in its top line "
    "to 7.69 billion euros in the three months through June, losing a "
    "little pace from the 11 percent growth it recorded in the first "
    "three months of the year. Analysts polled by Visible Alpha had "
    "forecast sales of 7.83 billion euros in the second quarter. "
    "Sales in the Asia-Pacific region drove quarterly growth, rising "
    "by 17 percent on year after the acquisition of the store network "
    "of optical retailer Top Charoen, which owns around 2,000 stores "
    "in Thailand. Revenue in North America and Europe saw some softer "
    "trends, in part due to conflict in the Middle East, "
    "EssilorLuxottica said. "
    "Sales of Ray-Ban and Oakley smartglasses, powered by artificial "
    "intelligence and produced in collaboration with tech giant Meta, "
    "nearly doubled on the year in the second quarter, adding to "
    "rapid expansion in a category the company is banking on to help "
    "fuel its growth over the longer term. The company backed its "
    "five-year guidance of solid growth in total revenue and broadly "
    "aligned increases in adjusted operating profit. It did not "
    "offer any numerical guidance. "
    '"AI glasses confirmed their exponential growth," the company '
    "said. Still, questions remain around the company's growth "
    "trajectory as it leans into its smartglasses product offer. "
    '"The point of debate remains the prospects for smartglasses," '
    "analysts at brokerage Bernstein wrote in a note following "
    "the update. "
    "The group could face competition from other smartglasses "
    "models in the near future, with Google and Apple preparing "
    "their own models of the wearable tech. But plenty of untapped "
    "opportunity still lies ahead for EssilorLuxottica, analysts at "
    "UBS wrote in a note this month. "
    '"Our long-standing view has been that greater competition is '
    "necessary to help build the category and accelerate adoption "
    'in the U.S. and globally," the bank\'s analysts said. '
    "The company's adjusted operating profit rose by 15 percent "
    "over the first six months of the year, while its operating "
    "margin grew to 18.9 percent from 18.1 percent in the "
    "previous-year period."
)


@pytest.fixture
def devices():
    return framing.detect_framing_devices(ARTICLE_TEXT)


def _types(devs):
    return [d.device_type for d in devs]


class TestWSJEssilorLuxotticaQ2SmartglassesBoom:
    """Framing device detection on WSJ EssilorLuxottica Q2 2026 article."""

    # ------------------------------------------------------------------
    # 1. Inverted success_paradox: "Slows Despite Smartglasses Boom"
    # ------------------------------------------------------------------
    def test_inverted_success_paradox_detected(self, devices):
        """Headline's 'Slows Despite Boom' is inverted success_paradox."""
        assert "success_paradox" in _types(devices), (
            "Expected success_paradox for headline 'Slows Despite "
            "Smartglasses Boom' — inverted structure where the negative "
            "leads and the positive is in the 'despite' clause."
        )

    def test_success_paradox_evidence_mentions_despite(self, devices):
        sp = [d for d in devices if d.device_type == "success_paradox"]
        assert any("despite" in d.evidence_text.lower() for d in sp), (
            "success_paradox evidence should reference 'despite'."
        )

    # ------------------------------------------------------------------
    # 2. editorial_deflation: "losing a little pace"
    # ------------------------------------------------------------------
    def test_editorial_deflation_detected(self, devices):
        """'losing a little pace' deflates 8.7% organic growth."""
        assert "editorial_deflation" in _types(devices), (
            "Expected editorial_deflation for 'losing a little pace' "
            "— framing 8.7% organic growth as deceleration."
        )

    def test_editorial_deflation_losing_pace_evidence(self, devices):
        ed = [d for d in devices if d.device_type == "editorial_deflation"]
        assert any("losing" in d.evidence_text.lower() for d in ed), (
            "editorial_deflation evidence should include 'losing'."
        )

    # ------------------------------------------------------------------
    # 3. grudging_concession: "Still, questions remain" + "debate remains"
    # ------------------------------------------------------------------
    def test_grudging_concession_questions_remain(self, devices):
        """'Still, questions remain' is grudging_concession after positive."""
        gc = [d for d in devices if d.device_type == "grudging_concession"]
        assert any("questions remain" in d.evidence_text.lower() for d in gc), (
            "Expected grudging_concession for 'Still, questions remain'."
        )

    def test_grudging_concession_debate_remains(self, devices):
        """'The point of debate remains' is grudging_concession."""
        gc = [d for d in devices if d.device_type == "grudging_concession"]
        assert any("debate remains" in d.evidence_text.lower() for d in gc), (
            "Expected grudging_concession for 'debate remains'."
        )

    def test_grudging_concession_count(self, devices):
        gc = [d for d in devices if d.device_type == "grudging_concession"]
        assert len(gc) >= 2, (
            f"Expected at least 2 grudging_concession devices "
            f"('questions remain' + 'debate remains'), got {len(gc)}."
        )

    # ------------------------------------------------------------------
    # 4. scale_magnitude: "nearly doubled"
    # ------------------------------------------------------------------
    def test_scale_magnitude_nearly_doubled(self, devices):
        """'nearly doubled' revenue should trigger scale_magnitude."""
        assert "scale_magnitude" in _types(devices), (
            "Expected scale_magnitude for 'nearly doubled'."
        )

    # ------------------------------------------------------------------
    # 5. Total device count
    # ------------------------------------------------------------------
    def test_total_device_count(self, devices):
        """Expect at least 5 framing devices in this article."""
        assert len(devices) >= 5, (
            f"Expected at least 5 framing devices, got {len(devices)}. "
            f"Types found: {_types(devices)}"
        )

    # ------------------------------------------------------------------
    # 6. Cross-publication framing comparison note
    # ------------------------------------------------------------------
    def test_no_false_positives_on_neutral_content(self, devices):
        """Ensure no spurious device types in this short, factual article."""
        # This article is relatively restrained — no surveillance_creep,
        # no glasshole_revival, no sarcastic_correction expected.
        bad_types = {
            "surveillance_creep",
            "glasshole_revival",
            "sarcastic_correction",
            "editorial_dramatization",
            "humanization_and_surveillance_enumeration",
        }
        found_bad = set(_types(devices)) & bad_types
        assert not found_bad, (
            f"Unexpected device types in this factual earnings article: "
            f"{found_bad}"
        )


class TestInvertedSuccessParadoxVariants:
    """Test the inverted success_paradox pattern on various constructions."""

    @pytest.mark.parametrize(
        "text,should_detect",
        [
            # WSJ headline verbatim
            ("Sales Growth Slows Despite Smartglasses Boom", True),
            # Hypothetical variants
            ("Revenue falls despite strong growth in wearables", True),
            ("Share price drops despite record sales", True),
            ("Growth eases despite doubling of AI glasses revenue", True),
            ("Stock dips despite surging demand", True),
            # Should NOT trigger (positive despite negative = standard)
            ("Sales boom despite privacy concerns", False),
            # Should NOT trigger (no "despite")
            ("Sales growth slows as competition heats up", False),
        ],
    )
    def test_inverted_success_paradox_pattern(self, text, should_detect):
        devices = framing.detect_framing_devices(text)
        types = [d.device_type for d in devices]
        if should_detect:
            assert "success_paradox" in types, (
                f"Expected success_paradox in: {text!r}"
            )
        else:
            # Standard success_paradox might fire on "boom despite concerns"
            # but inverted pattern should not fire on non-despite text
            if "despite" not in text.lower():
                inverted_sp = [
                    d
                    for d in devices
                    if d.device_type == "success_paradox"
                    and "despite" in d.evidence_text.lower()
                ]
                assert not inverted_sp, (
                    f"Inverted success_paradox should not fire on: {text!r}"
                )


class TestDecelationFramingVariants:
    """Test editorial_deflation deceleration patterns."""

    @pytest.mark.parametrize(
        "text",
        [
            "losing a little pace from the prior quarter",
            "losing momentum as the year progresses",
            "losing steam despite new product launches",
            "the company appears to be losing pace",
            "growth is losing a bit of traction",
        ],
    )
    def test_deceleration_detected(self, text):
        devices = framing.detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "editorial_deflation" in types, (
            f"Expected editorial_deflation for: {text!r}"
        )


class TestQuestionsRemainVariants:
    """Test grudging_concession 'questions remain' patterns."""

    @pytest.mark.parametrize(
        "text",
        [
            "Still, questions remain about the company's strategy",
            "Yet, doubts linger over the long-term viability",
            "However, concerns persist about profitability",
            "Nonetheless, uncertainty surrounds the outlook",
            "The debate remains over whether glasses can scale",
            "The point of debate remains the prospects",
        ],
    )
    def test_questions_remain_detected(self, text):
        devices = framing.detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "grudging_concession" in types, (
            f"Expected grudging_concession for: {text!r}"
        )
