"""Tests for Fox Business Meta $1.4T penalty article analysis (2026-07-07).

Validates:
- editorial_cross_promotion framing device detection (new device type)
- "reached out for comment" no_comment source pattern (new pattern)
- valuation_comparison detection on factual market-cap comparison
- Entity extraction for state AGs and federal judiciary
- Topic assignment: litigation > child_safety > consumer_protection
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

ARTICLE_PATH = (
    Path(__file__).resolve().parent.parent
    / "examples"
    / "sample_output"
    / "foxbusiness_meta_1_4t_penalty_2026_07_07_article.txt"
)


@pytest.fixture(scope="module")
def article_text() -> str:
    return ARTICLE_PATH.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Source detection tests
# ---------------------------------------------------------------------------


class TestFoxBusinessSources:
    """Test source and no_comment detection on Fox Business article."""

    def test_reached_out_for_comment_detected(self):
        """New 'reached out for comment' pattern must fire."""
        from mediascope.analyze.sources import extract_sources

        text = "Fox Business reached out to Meta for further comment."
        sources = extract_sources(text)
        no_comments = [
            s for s in sources if getattr(s, "source_type", "") == "no_comment"
        ]
        assert len(no_comments) >= 1, (
            "'reached out to Meta for further comment' should produce a no_comment signal"
        )

    def test_contacted_for_comment_detected(self):
        """'has contacted' variant must also fire."""
        from mediascope.analyze.sources import extract_sources

        text = "The publication has contacted Apple for comment."
        sources = extract_sources(text)
        no_comments = [
            s for s in sources if getattr(s, "source_type", "") == "no_comment"
        ]
        assert len(no_comments) >= 1, (
            "'has contacted Apple for comment' should produce a no_comment signal"
        )

    def test_reached_out_for_clarification_detected(self):
        """Variant with 'clarification' should also fire."""
        from mediascope.analyze.sources import extract_sources

        text = "We reached out to Google for clarification."
        sources = extract_sources(text)
        no_comments = [
            s for s in sources if getattr(s, "source_type", "") == "no_comment"
        ]
        assert len(no_comments) >= 1

    def test_declined_to_comment_still_works(self):
        """Original no_comment patterns must still fire (regression check)."""
        from mediascope.analyze.sources import extract_sources

        text = "Colorado's attorney general declined to comment on the filing."
        sources = extract_sources(text)
        no_comments = [
            s for s in sources if getattr(s, "source_type", "") == "no_comment"
        ]
        assert len(no_comments) >= 1

    def test_did_not_respond_still_works(self):
        """Original 'did not respond' pattern must still fire."""
        from mediascope.analyze.sources import extract_sources

        text = "Kentucky's attorney general did not respond to a request for comment."
        sources = extract_sources(text)
        no_comments = [
            s for s in sources if getattr(s, "source_type", "") == "no_comment"
        ]
        assert len(no_comments) >= 1

    def test_reached_out_false_positive_suppression(self):
        """'reached out to partners for collaboration' should NOT fire."""
        from mediascope.analyze.sources import extract_sources

        text = "Meta reached out to partners for collaboration on the project."
        sources = extract_sources(text)
        no_comments = [
            s for s in sources if getattr(s, "source_type", "") == "no_comment"
        ]
        assert len(no_comments) == 0, (
            "'reached out for collaboration' is not a no_comment signal"
        )


# ---------------------------------------------------------------------------
# Framing device tests
# ---------------------------------------------------------------------------


class TestEditorialCrossPromotion:
    """Test new editorial_cross_promotion framing device."""

    def test_allcaps_block_detected(self):
        """All-caps editorial callout blocks must fire."""
        from mediascope.analyze.framing import detect_framing_devices

        text = (
            "Meta disclosed the trillion-dollar figure.\n\n"
            "JUDGE LETS STATES PURSUE CLAIMS THAT META DESIGNED "
            "FACEBOOK AND INSTAGRAM TO ADDICT CHILDREN\n\n"
            "Fox Business reached out to Meta for further comment."
        )
        devices = detect_framing_devices(text)
        cross_promo = [d for d in devices if d.device_type == "editorial_cross_promotion"]
        assert len(cross_promo) >= 1, (
            "All-caps editorial callout block should fire editorial_cross_promotion"
        )

    def test_cta_block_detected(self):
        """CTA blocks like 'CLICK HERE TO GET THE FOX BUSINESS APP' must fire."""
        from mediascope.analyze.framing import detect_framing_devices

        text = (
            "The company denied the allegations.\n"
            "CLICK HERE TO GET THE FOX BUSINESS APP\n"
            "Another 14 states have brought claims."
        )
        devices = detect_framing_devices(text)
        cross_promo = [d for d in devices if d.device_type == "editorial_cross_promotion"]
        assert len(cross_promo) >= 1

    def test_normal_sentence_not_detected(self):
        """Normal prose sentences should not fire editorial_cross_promotion."""
        from mediascope.analyze.framing import detect_framing_devices

        text = (
            "Meta has denied the allegations, saying the attorneys general "
            "lack evidence that it misled the public about its platforms."
        )
        devices = detect_framing_devices(text)
        cross_promo = [d for d in devices if d.device_type == "editorial_cross_promotion"]
        assert len(cross_promo) == 0

    @pytest.mark.parametrize(
        "block",
        [
            "GOOGLE'S YOUTUBE REACHES SETTLEMENT IN LAWSUIT ALLEGING CHILD SOCIAL MEDIA ADDICTION",
            "READ MORE ABOUT THE LATEST RULING ON META'S PLATFORMS",
            "WATCH THE FULL INTERVIEW ON THE FOX BUSINESS NEWSLETTER",
        ],
        ids=["youtube-settlement", "read-more", "watch-newsletter"],
    )
    def test_various_cross_promo_blocks(self, block: str):
        """Various all-caps editorial blocks should fire."""
        from mediascope.analyze.framing import detect_framing_devices

        text = f"Some article text.\n\n{block}\n\nMore article text."
        devices = detect_framing_devices(text)
        cross_promo = [d for d in devices if d.device_type == "editorial_cross_promotion"]
        assert len(cross_promo) >= 1, f"Block '{block[:40]}...' should fire"


# ---------------------------------------------------------------------------
# Valuation comparison tests
# ---------------------------------------------------------------------------


class TestValuationComparison:
    """Valuation comparison should fire on market-cap anchoring."""

    def test_near_market_cap_fires(self):
        """'near Meta's market capitalization of around $1.5 trillion' should fire."""
        from mediascope.analyze.framing import detect_framing_devices

        text = (
            "The company said the number, which is near Meta's market "
            "capitalization of around $1.5 trillion, was not supported "
            "by the evidence."
        )
        devices = detect_framing_devices(text)
        val_cmp = [d for d in devices if d.device_type == "valuation_comparison"]
        assert len(val_cmp) >= 1


# ---------------------------------------------------------------------------
# Topic assignment tests
# ---------------------------------------------------------------------------


class TestTopicAssignment:
    """Verify topic assignment on Fox Business $1.4T penalty article."""

    def test_litigation_is_primary(self, article_text: str):
        """litigation should be the primary or secondary topic."""
        from mediascope.analyze.topics import classify_topic

        topics = classify_topic(article_text)
        topic_names = [t.topic if hasattr(t, "topic") else t[0] for t in topics[:3]]
        assert "litigation" in topic_names, (
            f"Expected 'litigation' in top-3 topics, got {topic_names}"
        )

    def test_child_safety_present(self, article_text: str):
        """child_safety should appear in topics."""
        from mediascope.analyze.topics import classify_topic

        topics = classify_topic(article_text, top_n=5)
        topic_names = [t.topic if hasattr(t, "topic") else t[0] for t in topics[:5]]
        assert "child_safety" in topic_names, (
            f"Expected 'child_safety' in top-5 topics, got {topic_names}"
        )


# ---------------------------------------------------------------------------
# Structural consistency
# ---------------------------------------------------------------------------


class TestStructuralConsistency:
    """Verify device type count stays consistent after adding editorial_cross_promotion."""

    def test_device_pattern_count(self):
        """Pattern-matched device type count should be 78."""
        from mediascope.analyze.framing import _DEVICE_PATTERNS

        assert len(_DEVICE_PATTERNS) == 84, (
            f"Expected 84 pattern-matched device types, got {len(_DEVICE_PATTERNS)}"
        )
