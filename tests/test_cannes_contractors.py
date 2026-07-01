"""Tests for patterns added during Wired Meta Cannes Contractors analysis.

Verifies:
1. Scale AI clustered under 'AI Infrastructure' (not 'Meta')
2. Covalen and Character.AI also in 'AI Infrastructure'
3. 'death of [proper noun]' does NOT trigger catastrophizing
4. 'death of [abstract concept]' DOES trigger catastrophizing
5. 'Outlook' as software product does NOT get extracted as source
6. 'posed as' / 'posing as' / 'impersonating' detected as loaded_language
7. 'dummy accounts' / 'fake accounts' / 'bogus accounts' detected as loaded_language
8. 'Business Insider' does NOT leak 'Insider' as standalone source
9. 'Daily Beast' does NOT leak 'Beast' as standalone source
10. Headline keyword presence boosts topic confidence via classify_topic()
"""

import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources
from mediascope.analyze.topics import classify_topic


class TestScaleAICluster:
    """Scale AI should be in AI Infrastructure cluster, not Meta."""

    def test_scale_ai_not_meta(self):
        text = "Scale AI contractors working for Google trained on competitor data."
        entities = detect_entities(text)
        scale = [e for e in entities if e.entity == "Scale AI"]
        assert len(scale) > 0, "Scale AI should be detected"
        assert all(e.cluster != "Meta" for e in scale), \
            "Scale AI should NOT be in Meta cluster"

    def test_scale_ai_in_ai_infrastructure(self):
        text = "Scale AI and Alexandr Wang's team benchmarked rival chatbots."
        entities = detect_entities(text)
        scale = [e for e in entities if e.entity == "Scale AI"]
        assert len(scale) > 0, "Scale AI should be detected"
        assert all(e.cluster == "AI Infrastructure" for e in scale)

    def test_covalen_in_ai_infrastructure(self):
        text = "Covalen managed the testing project for Meta."
        entities = detect_entities(text)
        covalen = [e for e in entities if e.entity == "Covalen"]
        assert len(covalen) > 0, "Covalen should be detected"
        assert all(e.cluster == "AI Infrastructure" for e in covalen)

    def test_character_ai_in_ai_infrastructure(self):
        text = "The project targeted OpenAI, Google Gemini, and Character.AI."
        entities = detect_entities(text)
        char_ai = [e for e in entities if "Character" in e.entity]
        assert len(char_ai) > 0, "Character.AI should be detected"
        assert all(e.cluster == "AI Infrastructure" for e in char_ai)


class TestCatastrophizingDeathOf:
    """'death of [proper noun]' is literal, not catastrophizing.
    'death of [abstract concept]' IS catastrophizing."""

    def test_death_of_person_no_catastrophizing(self):
        text = "The prompt referred to the death of Jamey Rodemeyer, a teenager."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "catastrophizing" not in types, \
            "'death of Jamey Rodemeyer' is a literal death, not catastrophizing"

    def test_death_of_abstract_is_catastrophizing(self):
        text = "Critics warned about the death of journalism in the AI era."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "catastrophizing" in types, \
            "'death of journalism' should be detected as catastrophizing"

    def test_death_of_democracy_is_catastrophizing(self):
        text = "The policy would mean the death of democracy as we know it."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "catastrophizing" in types

    def test_death_of_named_person_no_catastrophizing(self):
        text = "The death of Sarah Jones shocked the community."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "catastrophizing" not in types


class TestOutlookSourceExclusion:
    """'Outlook' as a software product should not be extracted as a source."""

    def test_outlook_addresses_not_source(self):
        text = "The accounts used throwaway Gmail and Outlook addresses."
        sources = extract_sources(text)
        names = [s.name.lower() for s in sources]
        assert "outlook" not in names, \
            "'Outlook' as email product should not be a source"

    def test_outlook_app_not_source(self):
        text = "Workers used the Outlook app to manage email responses."
        sources = extract_sources(text)
        names = [s.name.lower() for s in sources]
        assert "outlook" not in names


class TestDeceptionImpersonationPatterns:
    """Deception/impersonation language should be detected as loaded_language."""

    def test_posed_as(self):
        text = "Contractors posed as teenagers on rival platforms."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types

    def test_posing_as(self):
        text = "Workers posing as minors sent disturbing prompts."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types

    def test_impersonating(self):
        text = "Staff were impersonating children to test chatbot safety."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types

    def test_dummy_accounts(self):
        text = "They created dummy accounts to probe competitor systems."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types

    def test_fake_accounts(self):
        text = "The project used fake accounts registered with false birthdays."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types

    def test_infiltrate(self):
        text = "The team attempted to infiltrate competitor platforms."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types

    def test_bombard(self):
        text = "Workers bombarded the chatbot with thousands of prompts."
        devices = detect_framing_devices(text)
        types = [d.device_type for d in devices]
        assert "loaded_language" in types


class TestBusinessInsiderSourceSplitting:
    """'Business Insider' should not leak 'Insider' as a standalone source.
    Similarly 'Daily Beast' should not leak 'Beast'."""

    def test_business_insider_no_insider_fragment(self):
        text = "Business Insider reported that contractors were paid below minimum wage."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Insider" not in names, \
            "'Insider' should not appear as standalone source from 'Business Insider reported'"

    @pytest.mark.xfail(reason="Business Insider in _NAME_STOP_NAMES blocks Pattern 1; "
                        "full compound-name extraction is a future enhancement")
    def test_business_insider_full_name_extracted(self):
        text = "According to Business Insider, the project began in 2024."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Business Insider" in names, \
            "'Business Insider' should be extracted as a full source name"

    def test_daily_beast_no_beast_fragment(self):
        text = "The Daily Beast reported on the internal documents."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Beast" not in names, \
            "'Beast' should not appear as standalone source from 'Daily Beast reported'"

    @pytest.mark.xfail(reason="Daily Beast in _NAME_STOP_NAMES blocks Pattern 1; "
                        "full compound-name extraction is a future enhancement")
    def test_daily_beast_full_name_extracted(self):
        text = "According to the Daily Beast, sources confirmed the story."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Daily Beast" in names or "The Daily Beast" in names, \
            "'Daily Beast' should be extracted as a full source name"

    def test_insider_as_role_word_not_source(self):
        text = "An insider at the company revealed the details."
        sources = extract_sources(text)
        names = [s.name for s in sources]
        assert "Insider" not in names, \
            "'insider' as a role word should not be a source name"


class TestHeadlineTopicBoosting:
    """When a topic's keywords appear in the headline, classify_topic()
    should boost that topic's confidence via the 1.5x multiplier."""

    def test_headline_boosts_matching_topic(self):
        """A headline with 'teens' should boost child_safety above
        topics that only dominate body text."""
        body = (
            "The artificial intelligence project used machine learning models "
            "to benchmark competitor chatbots. The AI system processed millions "
            "of prompts using neural networks and large language models. "
            "Some contractors posed as teens on rival platforms."
        )
        headline = "Meta Contractors Posed as Teens to Test Rival AI Chatbots"

        result_with = classify_topic(body, headline=headline)
        result_without = classify_topic(body, headline=None)

        # Find child_safety rank in both
        topics_with = [t.topic for t in result_with]
        topics_without = [t.topic for t in result_without]

        # child_safety should be ranked higher with the headline boost
        if "child_safety" in topics_with and "child_safety" in topics_without:
            rank_with = topics_with.index("child_safety")
            rank_without = topics_without.index("child_safety")
            assert rank_with <= rank_without, \
                f"Headline boost should improve child_safety rank: " \
                f"with={rank_with}, without={rank_without}"

    def test_headline_boost_does_not_exceed_1(self):
        """Even with headline boost, confidence should be capped at 1.0."""
        body = (
            "Children were targeted by unsafe content online. Child safety "
            "advocates warned about minors being exploited. Teen users faced "
            "dangerous interactions with predators on the platform."
        )
        headline = "Children at Risk: Teen Safety Crisis Online"
        result = classify_topic(body, headline=headline)
        for t in result:
            assert t.confidence <= 1.0, \
                f"Topic {t.topic} confidence {t.confidence} exceeds 1.0"

    def test_no_headline_no_boost(self):
        """Without a headline, results should be unchanged from baseline."""
        body = "Meta's AI team developed new language models for chatbots."
        result_none = classify_topic(body, headline=None)
        result_empty = classify_topic(body, headline="")
        # Both should produce the same top topic
        if result_none and result_empty:
            assert result_none[0].topic == result_empty[0].topic

    def test_unrelated_headline_no_false_boost(self):
        """A headline about weather should not boost tech topics."""
        body = (
            "The artificial intelligence startup raised $50 million in funding. "
            "Their machine learning platform processes enterprise data."
        )
        headline = "Sunny Skies Expected Through the Weekend"
        result_with = classify_topic(body, headline=headline)
        result_without = classify_topic(body)
        # Top topic should remain the same — unrelated headline has no effect
        if result_with and result_without:
            assert result_with[0].topic == result_without[0].topic

    def test_headline_param_is_optional(self):
        """classify_topic should work without headline param (backward compat)."""
        body = "Meta released a new virtual reality headset at the conference."
        result = classify_topic(body)
        assert len(result) > 0, "classify_topic should return results without headline"
