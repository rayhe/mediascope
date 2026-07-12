"""
Regression tests for Jul 12, 2026 fixes (Type A deep dive, 15:00 PT).

Two fixes from the iPhone in Canada "EU Says Instagram Is Built to Addict You" analysis:

1. rhetorical_question: tag-question pattern ("...anyone?" / "...right?" / "...no?")
2. executive_behavior topic: suppress false positives from official titles like
   "Executive Vice-President" where "Executive" is a title, not behavior.
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.topics import classify_topic


def _has(devices, device_type):
    return any(d.device_type == device_type for d in devices)


# ─── Rhetorical Question: tag-question pattern ──────────────────────────────


class TestTagQuestionRhetoricalPattern:
    """Tests for tag-question style rhetorical questions ending in 'anyone?', 'right?', etc."""

    def test_dopamine_hits_anyone(self):
        """Original missed case from iPhone in Canada EU DSA article."""
        text = "Endless dopamine hits at 1am anyone?"
        devices = detect_framing_devices(text)
        assert _has(devices, "rhetorical_question"), (
            "'Endless dopamine hits at 1am anyone?' should trigger rhetorical_question"
        )

    def test_sounds_familiar_right(self):
        text = "Algorithmic rabbit holes keeping teens up all night, sounds familiar right?"
        devices = detect_framing_devices(text)
        assert _has(devices, "rhetorical_question"), (
            "Tag question ending in 'right?' should trigger rhetorical_question"
        )

    def test_surprise_no(self):
        text = "Another fine from Brussels, surprise no?"
        devices = detect_framing_devices(text)
        assert _has(devices, "rhetorical_question"), (
            "Tag question ending in 'no?' should trigger rhetorical_question"
        )

    def test_short_fragment_no_match(self):
        """Fragments too short (<10 chars before tag) should not match."""
        text = "Hi anyone?"
        devices = detect_framing_devices(text)
        assert not _has(devices, "rhetorical_question"), (
            "Very short fragment + 'anyone?' should not trigger rhetorical_question"
        )


# ─── Executive Behavior: title suppression ───────────────────────────────────


class TestExecutiveTitleSuppression:
    """Tests that official titles containing 'Executive' don't false-positive on executive_behavior."""

    def test_executive_vp_title_only(self):
        """Original false positive from iPhone in Canada article: Henna Virkkunen's title."""
        text = (
            "Henna Virkkunen, the European Commission's Executive Vice-President "
            "for Tech Sovereignty, announced the findings."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "executive_behavior" not in topic_names, (
            "'Executive Vice-President' as a title should not trigger executive_behavior"
        )

    def test_real_executive_behavior_still_detected(self):
        """Genuine executive behavior should still be detected."""
        text = (
            "CEO Mark Zuckerberg personally ordered the policy change, overriding "
            "concerns from the trust and safety team about the impact on teen users."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "executive_behavior" in topic_names, (
            "Genuine CEO behavior should still trigger executive_behavior"
        )
