"""Tests for grudging_concession framing device (#95).

Discovered from Gizmodo LED tamper article (Jul 8, 2026): positive Meta
privacy action framed through qualifiers that dampen the good news.
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices


def _device_names(text: str) -> set[str]:
    return {d.device_type for d in detect_framing_devices(text)}


class TestGrudgingConcession:
    """grudging_concession detection tests."""

    def test_actually_rolling_out(self):
        """'is now actually rolling out' implies surprise at positive action."""
        text = (
            "Meta is now actually rolling out what it purports to be "
            "tamper-proofing for the privacy LED on its smart glasses."
        )
        names = _device_names(text)
        assert "grudging_concession" in names

    def test_purports_to_be(self):
        """'what it purports to be' deflates a positive claim."""
        text = (
            "The company released what it purports to be a comprehensive "
            "privacy framework for its wearable devices."
        )
        names = _device_names(text)
        assert "grudging_concession" in names

    def test_is_finally_addressing(self):
        """'is finally addressing' implies overdue positive action."""
        text = (
            "After years of complaints, Apple is finally addressing the "
            "battery throttling issue with a software update."
        )
        names = _device_names(text)
        assert "grudging_concession" in names

    def test_it_took_external_pressure(self):
        """'it took [external force] to get [entity] to' pattern."""
        text = (
            "It took a viral investigation by the Wall Street Journal "
            "to get Google to fix the location tracking loophole."
        )
        names = _device_names(text)
        assert "grudging_concession" in names

    def test_credit_where_due_but(self):
        """'credit where it's due, but' pattern."""
        text = (
            "Credit where it's due, but Meta's new privacy dashboard "
            "still doesn't address the core data collection issue."
        )
        names = _device_names(text)
        assert "grudging_concession" in names

    def test_deserves_credit_however(self):
        """'deserves credit, however' pattern."""
        text = (
            "The company deserves some credit for acting quickly, however "
            "the underlying architecture remains unchanged."
        )
        names = _device_names(text)
        assert "grudging_concession" in names

    def test_no_false_positive_neutral_actually(self):
        """'actually' in non-grudging context should not fire."""
        text = (
            "The feature actually works quite well in practice, with "
            "latency under 50ms in our testing."
        )
        names = _device_names(text)
        assert "grudging_concession" not in names

    def test_no_false_positive_plain_purport(self):
        """'purports' in subject position (not 'what it purports to be') should not fire."""
        text = (
            "The study purports significant improvements in accuracy "
            "compared to prior benchmarks."
        )
        names = _device_names(text)
        assert "grudging_concession" not in names

    def test_gizmodo_led_article_verbatim(self):
        """Verbatim excerpt from the discovery article should fire."""
        text = (
            "So, as noticed by the Verge's Victoria Song on Tuesday, "
            "Meta is now actually rolling out what it purports to be "
            "tamper-proofing for the privacy LED on its smart glasses "
            "above and beyond the light sensor safeguard."
        )
        devices = detect_framing_devices(text)
        gc_devices = [d for d in devices if d.device_type == "grudging_concession"]
        # Should fire at least twice: "actually rolling" + "purports to be"
        assert len(gc_devices) >= 2

    def test_only_after_pattern(self):
        """'only after [negative event] did [entity] finally' pattern."""
        text = (
            "Only after a massive data breach exposed millions of records "
            "did Facebook finally implement end-to-end encryption."
        )
        names = _device_names(text)
        assert "grudging_concession" in names
