"""Tests for government_oversight topic bucket and group expert source detection.

Type A deep dive regression tests (Jun 27, 2026 16:00 PT): validates
the new government_oversight topic bucket correctly classifies articles
about national security, export controls, and AI regulation, AND that
group expert sources (named professional collectives like "cybersecurity
experts") are properly detected.
"""

from __future__ import annotations

import pytest

from mediascope.analyze.topics import TOPIC_KEYWORDS, classify_topic
from mediascope.analyze.sources import extract_sources


# ── government_oversight topic bucket ────────────────────────────────

class TestGovernmentOversightTopicDetection:
    """Validate the government_oversight topic bucket."""

    def test_topic_keywords_exist(self):
        """government_oversight should be a registered topic bucket."""
        assert "government_oversight" in TOPIC_KEYWORDS
        assert len(TOPIC_KEYWORDS["government_oversight"]) > 0

    def test_national_security_article(self):
        """Article about national security threats should classify as government_oversight."""
        text = (
            "The federal government declared the AI model a threat to national security "
            "and placed export controls on the new release. Government officials said the "
            "technology could pose risks if exported. The Pentagon is reviewing the decision."
        )
        topics = classify_topic(text, top_n=5)
        topic_names = [t.topic for t in topics]
        assert "government_oversight" in topic_names
        # Should be top topic
        assert topics[0].topic == "government_oversight"

    def test_export_controls_article(self):
        """Article about export controls should classify as government_oversight."""
        text = (
            "New export controls were introduced on advanced AI chips. The sanctions "
            "target Chinese semiconductor firms. The nonproliferation framework draws "
            "on arms control treaties from the Cold War era."
        )
        topics = classify_topic(text, top_n=5)
        topic_names = [t.topic for t in topics]
        assert "government_oversight" in topic_names

    def test_ai_regulation_article(self):
        """Article about AI regulation and governance classifies correctly."""
        text = (
            "Lawmakers are debating new federal legislation on AI regulation. "
            "The bipartisan bill would create an AI governance framework. "
            "Congressional review of AI safety regulation is expected before recess."
        )
        topics = classify_topic(text, top_n=5)
        topic_names = [t.topic for t in topics]
        assert "government_oversight" in topic_names

    def test_military_ai_article(self):
        """Article about military AI should trigger government_oversight."""
        text = (
            "The Pentagon announced new guidelines for military AI systems. "
            "Defense AI contractors must now submit to federal regulation. "
            "Government oversight of defense department AI procurement has increased."
        )
        topics = classify_topic(text, top_n=5)
        topic_names = [t.topic for t in topics]
        assert "government_oversight" in topic_names

    def test_beats_product_launch_on_regulation_article(self):
        """government_oversight should rank higher than product_launch for
        regulation articles that happen to use 'introduced' and 'released'."""
        text = (
            "Anthropic released a new AI model and then the government introduced "
            "export controls. The release was halted after government officials "
            "declared it a risk to national security. Lawmakers responded with "
            "a congressional hearing on AI regulation and nonproliferation."
        )
        topics = classify_topic(text, top_n=5)
        gov_score = next(
            (t.confidence for t in topics if t.topic == "government_oversight"),
            0.0,
        )
        launch_score = next(
            (t.confidence for t in topics if t.topic == "product_launch"),
            0.0,
        )
        assert gov_score > launch_score, (
            f"government_oversight ({gov_score}) should beat "
            f"product_launch ({launch_score}) on a regulation article"
        )

    def test_mittr_anthropic_feud_article(self):
        """The actual MIT TR Anthropic article should classify as government_oversight."""
        import os
        article_path = os.path.join(
            os.path.dirname(__file__), "..",
            "examples", "sample_output",
            "mittr_anthropic_feud_jun2026.txt",
        )
        if not os.path.exists(article_path):
            pytest.skip("Sample article not available")
        text = open(article_path).read()
        topics = classify_topic(text, top_n=5)
        topic_names = [t.topic for t in topics]
        assert "government_oversight" in topic_names
        # Should be the top-ranked topic
        assert topics[0].topic == "government_oversight"


# ── Group expert source detection ────────────────────────────────────

class TestGroupExpertSourceDetection:
    """Validate detection of named collective expert sources."""

    def test_cybersecurity_experts_open_letter(self):
        """'cybersecurity experts have said as much in an open letter' should
        be detected as a group_expert source."""
        text = (
            "Leading cybersecurity experts have said as much in an open letter "
            "to the government, writing that access to the models was helping "
            "researchers prepare defenses."
        )
        sources = extract_sources(text)
        group_sources = [s for s in sources if s.source_type == "group_expert"]
        assert len(group_sources) >= 1, (
            f"Expected group_expert source, got: {[s.source_type for s in sources]}"
        )
        assert group_sources[0].is_expert is True

    def test_ai_researchers_joint_statement(self):
        """'AI researchers argued in a joint statement' should be detected."""
        text = (
            "Leading AI researchers argued in a joint statement that the "
            "technology should be subject to independent review."
        )
        sources = extract_sources(text)
        group_sources = [s for s in sources if s.source_type == "group_expert"]
        assert len(group_sources) >= 1

    def test_security_experts_warned(self):
        """'security experts have warned' should be detected as group_expert."""
        text = (
            "Top security experts have warned that the new policy creates "
            "more vulnerabilities than it prevents."
        )
        sources = extract_sources(text)
        group_sources = [s for s in sources if s.source_type == "group_expert"]
        assert len(group_sources) >= 1
        assert group_sources[0].is_expert is True

    def test_economists_letter_to_congress(self):
        """'economists wrote in a letter to Congress' should be detected."""
        text = (
            "Prominent economics experts wrote in a letter to Congress "
            "that the proposed tariffs would increase consumer prices."
        )
        sources = extract_sources(text)
        group_sources = [s for s in sources if s.source_type == "group_expert"]
        assert len(group_sources) >= 1

    def test_group_expert_not_anonymous(self):
        """Group expert sources should NOT be classified as anonymous."""
        text = (
            "Leading cybersecurity experts have said in an open letter that "
            "the technology poses minimal risk."
        )
        sources = extract_sources(text)
        group_sources = [s for s in sources if s.source_type == "group_expert"]
        assert len(group_sources) >= 1
        for s in group_sources:
            assert s.is_anonymous is False

    def test_petition_by_experts(self):
        """'a petition signed by 200 AI researchers' should be detected."""
        text = (
            "A petition signed by 200 AI researchers called on the "
            "government to reconsider its approach."
        )
        sources = extract_sources(text)
        group_sources = [s for s in sources if s.source_type == "group_expert"]
        assert len(group_sources) >= 1

    def test_privacy_experts_argued(self):
        """'privacy experts argued' should be detected."""
        text = (
            "Independent privacy experts argued that the data collection "
            "practices violated existing consent frameworks."
        )
        sources = extract_sources(text)
        group_sources = [s for s in sources if s.source_type == "group_expert"]
        assert len(group_sources) >= 1

    def test_national_security_analysts(self):
        """'national security analysts warned' should be detected."""
        text = (
            "Senior national security analysts warned that the export "
            "ban could push allies toward Chinese alternatives."
        )
        sources = extract_sources(text)
        group_sources = [s for s in sources if s.source_type == "group_expert"]
        assert len(group_sources) >= 1
        assert group_sources[0].is_expert is True
