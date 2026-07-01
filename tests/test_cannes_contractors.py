"""Tests for patterns added during Wired Meta Cannes Contractors analysis.

Verifies:
1. Scale AI clustered under 'AI Infrastructure' (not 'Meta')
2. Covalen and Character.AI also in 'AI Infrastructure'
3. 'death of [proper noun]' does NOT trigger catastrophizing
4. 'death of [abstract concept]' DOES trigger catastrophizing
5. 'Outlook' as software product does NOT get extracted as source
6. 'posed as' / 'posing as' / 'impersonating' detected as loaded_language
7. 'dummy accounts' / 'fake accounts' / 'bogus accounts' detected as loaded_language
"""

import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources


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
