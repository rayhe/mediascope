"""Regression tests for scale_magnitude multiplier patterns added Jul 7 2026.

Discovered via Gizmodo "AI Agents Could Make Chatbots Look Like Pocket
Calculators" article: "136.5 times more energy", "153.7 times longer",
and "roughly half of the entire United States" were undetected by
existing scale_magnitude patterns.
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices


class TestMultiplierComparisons:
    """Test N-times-more/higher/longer scale_magnitude patterns."""

    def test_times_more_energy(self):
        text = "AI agents can consume up to 136.5 times more energy per query than generative AI models."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types, f"Expected scale_magnitude, got {types}"

    def test_times_higher(self):
        text = "That figure is about 136.5 times higher than the energy consumed by a generative AI query."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types, f"Expected scale_magnitude, got {types}"

    def test_times_longer(self):
        text = "Agentic AI can take 153.7 times longer than a standard query."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types, f"Expected scale_magnitude, got {types}"

    def test_times_faster(self):
        text = "The new chip is 10 times faster than its predecessor."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types, f"Expected scale_magnitude, got {types}"

    def test_times_worse(self):
        text = "Privacy violations were 3 times worse than initially reported."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types, f"Expected scale_magnitude, got {types}"

    def test_x_notation(self):
        text = "Meta's new model requires 10x more computing power than Muse Spark."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types, f"Expected scale_magnitude, got {types}"


class TestCeilingMultiplier:
    """Test 'up to N times' ceiling multiplier patterns."""

    def test_up_to_times_more(self):
        text = "can consume up to 136.5 times more energy per query"
        devices = detect_framing_devices(text)
        sm_devices = [d for d in devices if d.device_type == "scale_magnitude"]
        # Should match both the ceiling multiplier and the plain multiplier
        assert len(sm_devices) >= 1, f"Expected at least 1 scale_magnitude, got {len(sm_devices)}"

    def test_as_much_as_times(self):
        text = "as much as 50 times greater than normal levels"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types, f"Expected scale_magnitude, got {types}"


class TestNationalScaleComparison:
    """Test national/global scale comparison patterns."""

    def test_half_of_us(self):
        text = "roughly half of the entire United States' current electricity consumption"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types, f"Expected scale_magnitude, got {types}"

    def test_more_than_double_europe(self):
        text = "more than double Europe's annual energy output"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types, f"Expected scale_magnitude, got {types}"

    def test_nearly_half_global(self):
        text = "nearly half of global water supplies"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types, f"Expected scale_magnitude, got {types}"

    def test_roughly_twice_china(self):
        text = "roughly twice China's carbon output"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "scale_magnitude" in types, f"Expected scale_magnitude, got {types}"


class TestGizmodoEnergyArticleFullText:
    """End-to-end test on the Gizmodo AI agents energy article."""

    ARTICLE_TEXT = (
        "Much has been made of the emergence of generative AI and its strain "
        "on the electrical grid due to the energy demand. So just wait until "
        "you see how much energy agentic AI consumes. A new research paper "
        "from the Korea Advanced Institute of Science and Technology set out "
        'to quantify the "hidden costs" of AI agents, and found they can '
        "consume up to 136.5 times more energy per query than generative AI "
        "models.\n\n"
        "As a result, there's a multiplier effect that takes place. "
        "According to the researchers, an AI agent running on a large "
        "language model of the scale of most commercially available AI "
        "models would consume an average of 348.41 watt-hours per "
        "query—about the equivalent of keeping an LED light bulb on for a "
        "full day. That figure, they say, is about 136.5 times higher than "
        "the energy consumed by a generative AI query.\n\n"
        "The paper also examined response latency and found that agentic AI "
        "can take 153.7 times longer than a standard query.\n\n"
        "Researchers also modeled a future in which AI agents generate 13.7 "
        "billion requests per day, roughly the same volume of queries Google "
        "Search currently handles. Without major gains in energy efficiency, "
        "they estimate that would create demand for about 198.9 gigawatts "
        "of power—roughly half of the entire United States' current "
        "electricity consumption."
    )

    def test_detects_all_scale_magnitude_instances(self):
        devices = detect_framing_devices(self.ARTICLE_TEXT)
        sm_devices = [d for d in devices if d.device_type == "scale_magnitude"]
        # Should find: 136.5x more, 136.5x higher, 153.7x longer, half of US
        assert len(sm_devices) >= 4, (
            f"Expected >= 4 scale_magnitude devices, got {len(sm_devices)}: "
            f"{[d.evidence_text[:60] for d in sm_devices]}"
        )

    def test_detects_analogy_metaphor(self):
        devices = detect_framing_devices(self.ARTICLE_TEXT)
        am_devices = [d for d in devices if d.device_type == "analogy_metaphor"]
        assert len(am_devices) >= 1, "Expected 'equivalent of' analogy_metaphor"

    def test_detects_ironic_quotation(self):
        devices = detect_framing_devices(self.ARTICLE_TEXT)
        iq_devices = [d for d in devices if d.device_type == "ironic_quotation"]
        assert len(iq_devices) >= 1, 'Expected "hidden costs" ironic_quotation'
