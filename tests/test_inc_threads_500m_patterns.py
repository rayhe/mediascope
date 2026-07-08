"""Regression tests for patterns added during Inc.com Threads 500M analysis.

Article: "Mark Zuckerberg's New Social Network Just Crossed 500 Million Users
—and Put X on Notice" (Georgia Fearn, Inc.com, Jul 7 2026).

Patterns added:
- scale_magnitude: user-base milestone pattern ("crossed X million users")
- competitive_positioning: 3 headline-level patterns ("put X on notice",
  "leaves X behind", "overtakes X")

Provenance: Type A article deep dive, mediascope iteration Jul 8 2026 10:00 PT.
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices


def _types(text: str) -> set[str]:
    """Return set of device_type strings detected in *text*."""
    return {f.device_type for f in detect_framing_devices(text)}


# ---------------------------------------------------------------------------
# scale_magnitude: user-base milestone pattern
# ---------------------------------------------------------------------------
class TestScaleMagnitudeMilestonePattern:
    """The milestone pattern matches user-count crossings like '500 million
    monthly active users', which the existing scale_magnitude patterns missed
    because they focused on dollar amounts and multipliers."""

    @pytest.mark.parametrize(
        "text",
        [
            "Threads just crossed 500 million monthly active users",
            "The platform crossed 500M users last week",
            "WhatsApp surpassed 2 billion users in 2020",
            "It reached 100 million subscribers within weeks",
            "ChatGPT hit 200 million monthly active users",
            "The service topped 1 billion downloads in Q3",
            "Signal passed 40 million users after the WhatsApp exodus",
            "exceeded 3.2 billion registered accounts",
            "TikTok broke through 1.5 billion MAU last quarter",
        ],
    )
    def test_milestone_matches(self, text):
        assert "scale_magnitude" in _types(text), (
            f"Expected scale_magnitude for: {text!r}"
        )

    @pytest.mark.parametrize(
        "text",
        [
            "The company crossed the street to the new office",
            "Users reached out for customer support",
            "She passed the phone to her colleague",
        ],
    )
    def test_milestone_non_matches(self, text):
        assert "scale_magnitude" not in _types(text), (
            f"False positive scale_magnitude for: {text!r}"
        )


# ---------------------------------------------------------------------------
# competitive_positioning: "put X on notice" headline pattern
# ---------------------------------------------------------------------------
class TestCompetitivePositioningPutOnNotice:
    """Headline-level competitive framing: 'put X on notice'."""

    @pytest.mark.parametrize(
        "text",
        [
            "Put X on Notice",
            "Threads puts Twitter on notice",
            "The launch is putting rivals on notice",
        ],
    )
    def test_put_on_notice_matches(self, text):
        assert "competitive_positioning" in _types(text), (
            f"Expected competitive_positioning for: {text!r}"
        )


# ---------------------------------------------------------------------------
# competitive_positioning: "leaves X behind" pattern
# ---------------------------------------------------------------------------
class TestCompetitivePositioningLeavesBehind:
    """Competitive framing: 'leaves X behind / in the dust'."""

    @pytest.mark.parametrize(
        "text",
        [
            "Threads leaves X behind in the race for users",
            "The update left competitors in the dust",
            "Meta leaves Snap eating dust",
        ],
    )
    def test_leaves_behind_matches(self, text):
        assert "competitive_positioning" in _types(text), (
            f"Expected competitive_positioning for: {text!r}"
        )


# ---------------------------------------------------------------------------
# competitive_positioning: "overtakes/eclipses/dethrones" pattern
# ---------------------------------------------------------------------------
class TestCompetitivePositioningOvertakes:
    """Competitive framing: 'overtakes/eclipses/dethrones [rival]'."""

    @pytest.mark.parametrize(
        "text",
        [
            "Threads overtakes X in daily downloads",
            "Meta eclipses rival TikTok in ad revenue",
            "The newcomer dethrones Google in search satisfaction",
        ],
    )
    def test_overtakes_matches(self, text):
        assert "competitive_positioning" in _types(text), (
            f"Expected competitive_positioning for: {text!r}"
        )


# ---------------------------------------------------------------------------
# Integration: full Inc.com headline
# ---------------------------------------------------------------------------
class TestIncHeadlineIntegration:
    """The Inc.com headline should trigger both scale_magnitude (500 Million
    Users) and competitive_positioning (Put X on Notice)."""

    HEADLINE = (
        "Mark Zuckerberg's New Social Network Just Crossed 500 Million "
        "Users—and Put X on Notice"
    )

    def test_headline_triggers_scale_magnitude(self):
        assert "scale_magnitude" in _types(self.HEADLINE)

    def test_headline_triggers_competitive_positioning(self):
        assert "competitive_positioning" in _types(self.HEADLINE)
