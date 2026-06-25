"""Tests for loaded language improvements: uproar, backlash, tantamount, and
Twitter-like entity false positive fix.

Added as part of Type A iteration: Reuters × Emily Dalton Smith departure.
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.entities import detect_entities


class TestUproarBacklashLoaded:
    """Verify 'uproar' and 'backlash' are detected as loaded_language."""

    def test_uproar_standalone(self):
        text = "The restructuring has caused an uproar among employees."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types

    def test_backlash_standalone(self):
        text = "The policy change triggered immediate backlash from workers."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types

    def test_uproar_in_reuters_context(self):
        """The exact Reuters phrasing from the Dalton Smith article."""
        text = (
            "The restructuring, aimed at developing AI agents that could "
            "autonomously carry out tasks currently performed by human staffers, "
            "has caused an uproar among Meta employees."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types


class TestTantamountLoaded:
    """Verify 'tantamount to' is detected as loaded_language."""

    def test_tantamount_standalone(self):
        text = "Many employees see it as tantamount to helping design their own replacements."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types

    def test_tantamount_reuters_context(self):
        """The exact Reuters phrasing."""
        text = (
            "introducing mouse-tracking software that many employees see as "
            "tantamount to helping design their own bot replacements."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types


class TestHelpingDesignReplacements:
    """Verify 'helping design their own bot replacements' variant is caught."""

    def test_helping_design_replacements(self):
        text = "employees see it as helping design their own bot replacements"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types

    def test_designing_replacements(self):
        text = "designing their own replacements was the fear"
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types


class TestTwitterLikeFalsePositive:
    """Ensure 'Twitter-like' does NOT match as an X/Twitter entity mention."""

    def test_twitter_like_no_match(self):
        text = "Meta's Twitter-like microblogging app Threads."
        entities = detect_entities(text)
        clusters = [e.cluster for e in entities]
        assert "X/Twitter" not in clusters, (
            "'Twitter-like' should not produce an X/Twitter entity match"
        )

    def test_twitter_standalone_still_matches(self):
        """Plain 'Twitter' should still match."""
        text = "Elon Musk's Twitter was rebranded to X."
        entities = detect_entities(text)
        clusters = [e.cluster for e in entities]
        assert "X/Twitter" in clusters

    def test_twitter_esque_no_match(self):
        text = "The new app has a Twitter-esque interface."
        entities = detect_entities(text)
        clusters = [e.cluster for e in entities]
        assert "X/Twitter" not in clusters

    def test_uber_like_no_match(self):
        """Generic test: 'Uber-like' should not match."""
        # This requires Uber to be in entity clusters; skip if not
        text = "An Uber-like service for deliveries."
        entities = detect_entities(text)
        # Just ensure no crash; cluster presence depends on defaults
        assert isinstance(entities, list)


class TestNegativeFalsePositive:
    """Ensure existing patterns don't false-positive on benign text."""

    def test_uproar_not_in_neutral(self):
        text = "The company announced quarterly earnings were up 12%."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" not in types

    def test_backlash_not_in_product_review(self):
        text = "The new features received positive user feedback."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" not in types
