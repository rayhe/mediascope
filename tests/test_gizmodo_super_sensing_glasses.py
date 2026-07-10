"""
Tests for Gizmodo 'Meta super-sensing glasses' article (July 9, 2026).

Validates entity detection, framing device detection, source extraction,
topic classification, and loaded-language detection for a first-person
editorial Gizmodo piece covering an FT report about Meta's prototype
always-on recording glasses.

Article: "Meta Is Toying With the Idea of Smart Glasses That Record
Everything, All the Time" — Gizmodo, July 9, 2026.
"""

import pathlib
import pytest
from mediascope.analysis import (
    detect_entities,
    detect_framing_devices,
    extract_sources,
    classify_topics,
    analyze_composite,
)

_ARTICLE = (
    pathlib.Path(__file__).resolve().parent.parent
    / "examples"
    / "sample_output"
    / "gizmodo_meta_super_sensing_glasses_2026_07_09_article.txt"
).read_text()


# ------------------------------------------------------------------
# Entity detection
# ------------------------------------------------------------------
class TestEntities:
    def test_meta_detected(self):
        entities = detect_entities(_ARTICLE)
        names = {str(e).split("entity='")[1].split("'")[0] for e in entities}
        assert "Meta" in names

    def test_financial_times_detected(self):
        entities = detect_entities(_ARTICLE)
        names = {str(e).split("entity='")[1].split("'")[0] for e in entities}
        assert "Financial Times" in names

    def test_mark_zuckerberg_detected(self):
        entities = detect_entities(_ARTICLE)
        names = {str(e).split("entity='")[1].split("'")[0] for e in entities}
        assert "Mark Zuckerberg" in names

    def test_gizmodo_detected(self):
        entities = detect_entities(_ARTICLE)
        names = {str(e).split("entity='")[1].split("'")[0] for e in entities}
        assert "Gizmodo" in names


# ------------------------------------------------------------------
# Source extraction
# ------------------------------------------------------------------
class TestSources:
    def test_financial_times_as_source(self):
        sources = extract_sources(_ARTICLE)
        source_names = [
            str(s).split("name='")[1].split("'")[0]
            for s in sources
        ]
        assert any("Financial Times" in n for n in source_names), (
            f"Financial Times not found in sources: {source_names}"
        )

    def test_meta_spokesperson_source(self):
        sources = extract_sources(_ARTICLE)
        source_names = [
            str(s).split("name='")[1].split("'")[0]
            for s in sources
        ]
        assert any("Meta" in n and "spokesperson" in n.lower()
                    for n in source_names) or any(
            "spokesperson" in str(s).lower() for s in sources
        ), f"Meta spokesperson not found in sources: {source_names}"

    def test_svenska_dagbladet_as_source(self):
        """The article references 'Swedish newspaper Svenska Dagbladet'.
        The 'a report from [descriptor] [Publication]' pattern should catch it."""
        sources = extract_sources(_ARTICLE)
        source_names = [
            str(s).split("name='")[1].split("'")[0]
            for s in sources
        ]
        assert any("Svenska Dagbladet" in n for n in source_names), (
            f"Svenska Dagbladet not found in sources: {source_names}"
        )

    def test_anonymous_sources_detected(self):
        sources = extract_sources(_ARTICLE)
        anon = [s for s in sources if "anonymous" in str(s).lower() or "is_anonymous=True" in str(s)]
        assert len(anon) >= 1, "Should detect 'sources familiar with the matter'"


# ------------------------------------------------------------------
# Framing devices
# ------------------------------------------------------------------
class TestFraming:
    def test_ironic_quotation_every_few_seconds(self):
        """'every few seconds' is placed in quotes to highlight alarm."""
        devices = detect_framing_devices(_ARTICLE)
        types = [str(d).split("device_type='")[1].split("'")[0] for d in devices]
        assert "ironic_quotation" in types

    def test_loaded_language_detected(self):
        devices = detect_framing_devices(_ARTICLE)
        types = [str(d).split("device_type='")[1].split("'")[0] for d in devices]
        assert "loaded_language" in types

    def test_anonymous_authority_detected(self):
        devices = detect_framing_devices(_ARTICLE)
        types = [str(d).split("device_type='")[1].split("'")[0] for d in devices]
        assert "anonymous_authority" in types

    def test_minimum_framing_device_count(self):
        """A critical editorial piece should produce at least 3 framing devices."""
        devices = detect_framing_devices(_ARTICLE)
        assert len(devices) >= 3, (
            f"Expected >= 3 framing devices, got {len(devices)}: "
            f"{[str(d).split('device_type=')[1].split(',')[0] for d in devices]}"
        )


# ------------------------------------------------------------------
# Topic classification
# ------------------------------------------------------------------
class TestTopics:
    def test_hardware_wearables_topic(self):
        topics = classify_topics(_ARTICLE)
        topic_names = [str(t).split("topic='")[1].split("'")[0] for t in topics]
        assert "hardware_wearables" in topic_names

    def test_privacy_data_topic(self):
        topics = classify_topics(_ARTICLE)
        topic_names = [str(t).split("topic='")[1].split("'")[0] for t in topics]
        assert "privacy_data" in topic_names


# ------------------------------------------------------------------
# Loaded language terms
# ------------------------------------------------------------------
class TestLoadedLanguage:
    """Verify newly added emotional language terms are present in the corpus."""

    def test_unsavory_in_emotional_language(self):
        from mediascope.analyze.sentiment import EMOTIONAL_LANGUAGE
        assert "unsavory" in EMOTIONAL_LANGUAGE

    def test_face_computers_in_emotional_language(self):
        from mediascope.analyze.sentiment import EMOTIONAL_LANGUAGE
        assert "face computers" in EMOTIONAL_LANGUAGE

    def test_ick_people_out_in_emotional_language(self):
        from mediascope.analyze.sentiment import EMOTIONAL_LANGUAGE
        assert "ick people out" in EMOTIONAL_LANGUAGE

    def test_problematic_history_in_emotional_language(self):
        from mediascope.analyze.sentiment import EMOTIONAL_LANGUAGE
        assert "problematic history" in EMOTIONAL_LANGUAGE
