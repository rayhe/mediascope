"""Tests for privacy_data topic keyword expansion and source affiliation
case-sensitivity fixes (2026-07-02 Type A iteration).

Covers:
1. privacy_data topic detection with MCI/employee-surveillance language
2. Source affiliation extraction with capitalized titles
"""

import pytest
from mediascope.analyze.topics import classify_topic
from mediascope.analyze.sources import _extract_affiliation, extract_sources


# ---------------------------------------------------------------------------
# Privacy/Data Topic Keyword Expansion
# ---------------------------------------------------------------------------

class TestPrivacyDataTopicExpansion:
    """Verify the privacy_data topic fires on employee surveillance
    and consent-related language that was previously undetected."""

    def test_opt_in_opt_out_triggers_privacy(self):
        text = (
            "If the company turns the program back on once the review is "
            "completed, it will be on an opt-in basis. When Meta first "
            "installed the program, Bosworth told them there was no way "
            "to opt out."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "privacy_data" in topic_names

    def test_sensitive_data_employee_data_triggers_privacy(self):
        text = (
            "Meta paused the program while investigating the exposure of "
            "sensitive data. A review of a recent data security incident "
            "indicated that no employee data was included in AI training."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "privacy_data" in topic_names

    def test_mouse_tracking_digital_activity_triggers_privacy(self):
        text = (
            "The company's controversial mouse-tracking software tracks "
            "employee mouse movements and digital activity for AI training."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "privacy_data" in topic_names

    def test_keystroke_screen_scraping_triggers_privacy(self):
        text = (
            "One engineer wrote a widely shared internal note saying having "
            "their laptop screen scraped for training data without consent "
            "felt like an invasion of privacy. The keystroke data was also "
            "collected without clear disclosure."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "privacy_data" in topic_names

    def test_combined_mci_article_has_privacy_as_top_topic(self):
        """The Reuters July 2 town hall article should have privacy_data
        as a top-3 topic after keyword expansion."""
        text = (
            "Meta Chief Executive Mark Zuckerberg told an internal town hall "
            "that AI agent development had not accelerated. Meta is projected "
            "to spend $145 billion on AI infrastructure. Meta's chief "
            "technology officer said a review of a recent data security "
            "incident with the company's controversial mouse-tracking software "
            "indicated that no employee data was included in AI training. "
            "Meta paused the program, which tracks employee mouse movements "
            "and digital activity for AI training, while investigating the "
            "exposure of sensitive data. If the company turns the program "
            "back on, it will be on an opt-in basis. Bosworth told them "
            "there was no way to opt out."
        )
        topics = classify_topic(text)
        topic_names = [t.topic for t in topics]
        assert "privacy_data" in topic_names
        # Should be top-ranked since the MCI content dominates
        assert topics[0].topic == "privacy_data"


# ---------------------------------------------------------------------------
# Source Affiliation Case Sensitivity
# ---------------------------------------------------------------------------

class TestAffiliationCaseSensitivity:
    """Verify affiliation extraction handles capitalized titles in
    article text (Chief, Vice President, Technology, etc.)."""

    def test_meta_chief_executive_capitalized(self):
        context = "Meta Chief Executive Mark Zuckerberg told an internal town hall"
        assert _extract_affiliation(context) == "Meta"

    def test_meta_chief_technology_officer_capitalized(self):
        context = "Meta's Chief Technology Officer Andrew Bosworth said"
        assert _extract_affiliation(context) == "Meta"

    def test_meta_chief_technology_officer_lowercase(self):
        context = "Meta's chief technology officer, Andrew Bosworth, said"
        assert _extract_affiliation(context) == "Meta"

    def test_google_vice_president_capitalized(self):
        context = "Google's Vice President of Engineering Jane Smith told reporters"
        assert _extract_affiliation(context) == "Google"

    def test_apple_senior_director_capitalized(self):
        context = "Apple's Senior Director of Product Management John Doe said"
        assert _extract_affiliation(context) == "Apple"

    def test_amazon_chief_financial_officer_mixed_case(self):
        context = "Amazon's Chief Financial Officer Brian Olsavsky said"
        assert _extract_affiliation(context) == "Amazon"

    def test_pattern_0_possessive_with_department_layer(self):
        """Pattern 0 now includes the department layer (technology,
        financial, etc.) between title prefix and role word."""
        context = "Meta's chief technology officer said the program would change"
        assert _extract_affiliation(context) == "Meta"

    def test_pattern_0b_non_possessive_capitalized(self):
        """Pattern 0b handles non-possessive org + capitalized title."""
        context = "Meta Chief Technology Officer Andrew Bosworth said"
        assert _extract_affiliation(context) == "Meta"

    def test_extract_sources_zuckerberg_affiliation(self):
        """Full pipeline: Zuckerberg should get affiliation='Meta'."""
        text = (
            "Meta Chief Executive Mark Zuckerberg told an internal town hall "
            "on Thursday that AI agent development over the last four months "
            'had not "accelerated in the way we expected."'
        )
        sources = extract_sources(text)
        zuck_sources = [s for s in sources if "Zuckerberg" in s.name]
        assert len(zuck_sources) >= 1
        assert zuck_sources[0].affiliation == "Meta"
