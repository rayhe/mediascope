"""Regression tests for Watermelon/Muse Image/Muse Video entity detection
and BofA/Berkshire Hathaway financial entity detection.

Added 2026-07-07 from Type A deep dive of BofA/Barron's article on
Meta AI capex and Watermelon model codename reveal.
"""

import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices


class TestWatermelonEntityDetection:
    """Watermelon is Meta's next-gen frontier AI model codename (after
    Avocado/Muse Spark), requiring 10x compute."""

    def test_watermelon_detected_as_meta(self):
        text = "Meta's next-gen AI model codenamed Watermelon requires 10x compute."
        entities = detect_entities(text)
        watermelon = [e for e in entities if e.entity == "Watermelon"]
        assert len(watermelon) == 1
        assert watermelon[0].cluster == "Meta"

    def test_watermelon_contextual_match(self):
        """Watermelon should match only with contextual followers to
        avoid false positives with the fruit."""
        text = "I ate a watermelon at the picnic yesterday."
        entities = detect_entities(text)
        watermelon = [e for e in entities if "atermelon" in e.entity.lower()]
        assert len(watermelon) == 0, "Should not match fruit usage"

    def test_watermelon_with_model_context(self):
        text = "Watermelon is expected to cost $10B in training compute."
        entities = detect_entities(text)
        watermelon = [e for e in entities if e.entity == "Watermelon"]
        assert len(watermelon) == 1
        assert watermelon[0].cluster == "Meta"


class TestMuseImageVideoDetection:
    """Muse Image and Muse Video are Meta's generative AI models
    launched July 2026."""

    def test_muse_image_detected_as_meta(self):
        text = "Muse Image is Meta's first image-generation AI model."
        entities = detect_entities(text)
        muse_img = [e for e in entities if e.entity == "Muse Image"]
        assert len(muse_img) == 1
        assert muse_img[0].cluster == "Meta"

    def test_muse_video_detected_as_meta(self):
        text = "Muse Video is in early preview for select creators."
        entities = detect_entities(text)
        muse_vid = [e for e in entities if e.entity == "Muse Video"]
        assert len(muse_vid) == 1
        assert muse_vid[0].cluster == "Meta"

    def test_muse_spark_still_works(self):
        """Ensure existing Muse Spark detection isn't broken."""
        text = "Muse Spark powers the Ray-Ban Meta smart glasses."
        entities = detect_entities(text)
        muse_spark = [e for e in entities if e.entity == "Muse Spark"]
        assert len(muse_spark) == 1
        assert muse_spark[0].cluster == "Meta"


class TestBofAEntityDetection:
    """BofA Securities / BofA should be detected as Financial Services."""

    def test_bofa_securities_detected(self):
        text = "BofA Securities analyst Justin Post raised the capex estimate."
        entities = detect_entities(text)
        bofa = [e for e in entities if "BofA" in e.entity]
        assert len(bofa) >= 1
        assert bofa[0].cluster == "Financial Services"

    def test_bofa_shorthand_detected(self):
        text = "BofA warns that AI spending could spook the market."
        entities = detect_entities(text)
        bofa = [e for e in entities if e.entity == "BofA"]
        assert len(bofa) == 1
        assert bofa[0].cluster == "Financial Services"

    def test_bank_of_america_still_works(self):
        text = "Bank of America raised its price target."
        entities = detect_entities(text)
        boa = [e for e in entities if e.entity == "Bank of America"]
        assert len(boa) == 1
        assert boa[0].cluster == "Financial Services"


class TestBerkshireHathawayDetection:
    """Berkshire Hathaway and Warren Buffett should be Financial Services."""

    def test_berkshire_hathaway_detected(self):
        text = "Berkshire Hathaway sold its remaining Meta shares."
        entities = detect_entities(text)
        bh = [e for e in entities if e.entity == "Berkshire Hathaway"]
        assert len(bh) == 1
        assert bh[0].cluster == "Financial Services"

    def test_warren_buffett_detected(self):
        text = "Warren Buffett warned about AI hype at the annual meeting."
        entities = detect_entities(text)
        wb = [e for e in entities if e.entity == "Warren Buffett"]
        assert len(wb) == 1
        assert wb[0].cluster == "Financial Services"


class TestAnalystAuthorityFraming:
    """The analyst_authority framing device detects named analyst firms
    lending credibility to narrative frames about corporate spending."""

    def test_bofa_warns(self):
        text = "BofA warns that Big Tech AI spending could spook the market."
        devices = detect_framing_devices(text)
        aa = [d for d in devices if d.device_type == "analyst_authority"]
        assert len(aa) >= 1

    def test_analyst_name_pattern(self):
        text = "BofA Securities analyst Justin Post raised the capex estimate."
        devices = detect_framing_devices(text)
        aa = [d for d in devices if d.device_type == "analyst_authority"]
        assert len(aa) >= 1

    def test_according_to_with_negative_framing(self):
        text = (
            "According to Goldman Sachs, the ballooning costs of AI "
            "infrastructure risk unsustainable growth trajectories."
        )
        devices = detect_framing_devices(text)
        aa = [d for d in devices if d.device_type == "analyst_authority"]
        assert len(aa) >= 1

    def test_raised_estimate_with_investor_anxiety(self):
        text = (
            "Morgan Stanley raised its capex estimate to $150 billion, "
            "a figure that could heighten investor anxiety about near-term "
            "returns on AI infrastructure spending."
        )
        devices = detect_framing_devices(text)
        aa = [d for d in devices if d.device_type == "analyst_authority"]
        assert len(aa) >= 1

    def test_no_false_positive_neutral_analyst_mention(self):
        """A neutral analyst mention without negative framing should not
        trigger analyst_authority."""
        text = "Goldman Sachs reported strong quarterly earnings."
        devices = detect_framing_devices(text)
        aa = [d for d in devices if d.device_type == "analyst_authority"]
        assert len(aa) == 0
