"""Tests for delayed_defense and industry_normalization_undercut framing devices,
and improved headline boost for child_safety topic classification.

Added in Type A iteration (2026-07-01) after analysis of the Wired Cannes
contractors/teens article surfaced these gaps.
"""

import pytest
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.topics import classify_topic


# ---- Delayed Defense ----

class TestDelayedDefense:
    """Corporate response buried late in an article should trigger delayed_defense."""

    def test_response_at_80_percent(self):
        """Meta spokesperson response at 80% through the article -> fires."""
        # Build an article where the first 80% is accusations, last 20% has response
        accusation = "The contractors were asked to perform disturbing tasks. " * 40
        response = "A Meta spokesperson said the company follows all applicable guidelines."
        text = accusation + response
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "delayed_defense" in types, \
            "Response at 80% should trigger delayed_defense"

    def test_response_at_30_percent(self):
        """Response early in the article (30%) -> should NOT fire."""
        intro = "The investigation revealed troubling practices. " * 10
        response = "A Meta spokesperson said the company has strict safety measures. "
        body = "More details emerged about the project scope. " * 30
        text = intro + response + body
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "delayed_defense" not in types, \
            "Response at 30% should NOT trigger delayed_defense"

    def test_declined_to_comment_late(self):
        """'declined to comment' at the end of the article -> fires."""
        body = "Workers described unsafe conditions and long hours without breaks. " * 40
        kicker = "Meta declined to comment on the specific allegations."
        text = body + kicker
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "delayed_defense" in types, \
            "'Declined to comment' at the end should trigger delayed_defense"

    def test_short_article_no_fire(self):
        """Articles under 500 chars should not trigger (no meaningful structure)."""
        text = "Bad things happened. Meta said it was fine."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "delayed_defense" not in types, \
            "Short articles should not trigger delayed_defense"

    def test_spokesperson_pattern(self):
        """Spokesperson response late in article -> fires."""
        body = "The AI system processed millions of harmful prompts. " * 40
        response = "A spokesperson for Meta told WIRED that the program has been discontinued."
        text = body + response
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "delayed_defense" in types

    def test_in_a_statement_late(self):
        """'In a statement, the company said...' late in article -> fires."""
        body = "The investigation uncovered systematic violations of safety protocols. " * 40
        response = "In a statement, the company said it takes worker safety seriously."
        text = body + response
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "delayed_defense" in types

    def test_no_response_at_all_no_fire(self):
        """Article with no corporate response at all -> does NOT fire."""
        text = "Workers described terrible conditions. " * 30
        text += "The investigation continued for months. " * 10
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "delayed_defense" not in types, \
            "No corporate response should not trigger delayed_defense"


# ---- Industry Normalization Undercut ----

class TestIndustryNormalizationUndercut:
    """Acknowledging industry-wide practice then singling out the target."""

    def test_other_companies_but_especially(self):
        text = (
            "Other companies also rely on contractors for content moderation, "
            "but Meta's reliance is especially troubling given the scale of its operations."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "industry_normalization_undercut" in types

    def test_not_unique_but(self):
        text = (
            "The practice is not unique to Meta, but the company's approach "
            "has drawn particular scrutiny from regulators."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "industry_normalization_undercut" in types

    def test_industry_wide_but_scale(self):
        text = (
            "Content moderation outsourcing is an industry-wide practice, "
            "but the scale at Meta dwarfs competitors."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "industry_normalization_undercut" in types

    def test_pure_normalization_no_undercut(self):
        """Simple industry comparison without undercutting -> should NOT fire."""
        text = (
            "Other companies like Google and Apple also use contractors "
            "for similar quality assurance tasks."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "industry_normalization_undercut" not in types, \
            "Pure normalization without undercut should not fire"

    def test_others_also_but_far_worse(self):
        text = (
            "Other tech giants also employ low-paid contractors, "
            "yet Meta's conditions are far worse than its peers."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "industry_normalization_undercut" in types

    def test_not_alone_but_approach(self):
        text = (
            "Meta is not alone in using AI to moderate content, but its approach "
            "raises more concerns than any rival's."
        )
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "industry_normalization_undercut" in types


# ---- Headline Boost (child_safety) ----

class TestHeadlineBoostStrength:
    """Headline boost at 2.0x should lift child_safety above ai_development
    when the headline contains child-safety signals."""

    def test_teens_headline_outranks_ai_body(self):
        """Body dominated by AI keywords, headline has 'teens' ->
        child_safety should rank above ai_development."""
        body = (
            "The artificial intelligence project used machine learning models "
            "and large language models to benchmark competitor chatbots. "
            "The AI system processed millions of prompts using neural networks "
            "and generative AI infrastructure. The AI agent framework used "
            "deep learning for training data analysis and inference. "
            "Contractors posed as teens on rival platforms to test safety."
        )
        headline = "Meta Contractors Posed as Teens to Test Rival AI Chatbots"

        result = classify_topic(body, headline=headline)
        topic_ranks = {ts.topic: i for i, ts in enumerate(result)}

        assert "child_safety" in topic_ranks, "child_safety should be in top topics"
        if "ai_development" in topic_ranks:
            assert topic_ranks["child_safety"] < topic_ranks["ai_development"], \
                f"child_safety (rank {topic_ranks['child_safety']}) should rank above " \
                f"ai_development (rank {topic_ranks['ai_development']}) with headline boost"

    def test_children_headline_boost(self):
        """Headline with 'children' should boost child_safety."""
        body = (
            "The new AI model was trained on vast datasets. The company "
            "invested heavily in computing capacity and AI infrastructure. "
            "Some children were exposed to inappropriate content online."
        )
        headline = "New Report Reveals Dangers to Children on Social Platforms"

        result = classify_topic(body, headline=headline)
        topics = [ts.topic for ts in result]
        assert topics[0] == "child_safety", \
            f"child_safety should be #1 with children in headline, got {topics[0]}"

    def test_posed_as_teens_keyword(self):
        """New compound keyword 'posed as teens' should match child_safety."""
        body = "Contractors posed as teens on rival platforms to test chatbot safety."
        result = classify_topic(body)
        topics = [ts.topic for ts in result]
        assert "child_safety" in topics, \
            "'posed as teens' should trigger child_safety topic"
