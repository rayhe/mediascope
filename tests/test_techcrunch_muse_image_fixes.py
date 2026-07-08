"""Regression tests for TechCrunch Muse Image privacy pushback article.

Fixes discovered during Jul 8, 2026 Type A iteration:
1. "Muse Video" extracted as a named source (should be filtered as product name)
2. Cambridge Analytica clustered under "Meta" (should be separate cluster)
3. "landmark" detected as loaded_language in literal geographic context
"""

import pytest

from mediascope.analyze.sources import extract_sources
from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices


# ── Source extraction: product name false positives ──────────────────


class TestMuseProductNameSourceFilter:
    """Product names like 'Muse Video' and 'Muse Image' should not be
    extracted as named sources even when they follow an attribution verb."""

    def test_muse_video_not_extracted_as_source(self):
        """'also said Muse Video' should not extract 'Muse Video' as a source."""
        text = (
            'The company also said Muse Video — presumably an AI video '
            'generator — is "already in development." TechCrunch has '
            'reached out to Meta for more information.'
        )
        sources = extract_sources(text)
        source_names = [s.name for s in sources]
        assert "Muse Video" not in source_names, (
            "'Muse Video' is a product name, not a journalistic source"
        )

    def test_muse_image_not_extracted_as_source(self):
        """'said Muse Image' should not extract 'Muse Image' as a source."""
        text = 'Meta on Tuesday unveiled Muse Image, said Muse Image was available for free.'
        sources = extract_sources(text)
        source_names = [s.name for s in sources]
        assert "Muse Image" not in source_names, (
            "'Muse Image' is a product name, not a journalistic source"
        )

    def test_muse_spark_not_extracted_as_source(self):
        """Pre-existing: 'Muse Spark' should also be filtered."""
        text = 'The report said Muse Spark would power the next generation.'
        sources = extract_sources(text)
        source_names = [s.name for s in sources]
        assert "Muse Spark" not in source_names

    def test_real_source_still_extracted(self):
        """Named human sources should still be extracted normally."""
        text = 'Lucas Ropek said the controversy was growing.'
        sources = extract_sources(text)
        source_names = [s.name for s in sources]
        assert "Lucas Ropek" in source_names


# ── Entity clustering: Cambridge Analytica separation ────────────────


class TestCambridgeAnalyticaCluster:
    """Cambridge Analytica should be in its own cluster, not under Meta.
    It's a separate political consulting firm, not a Meta subsidiary."""

    def test_cambridge_analytica_separate_from_meta(self):
        text = (
            "Cambridge Analytica had improperly harvested data from "
            "tens of millions of Facebook users."
        )
        entities = detect_entities(text)
        ca_entities = [e for e in entities if e.entity == "Cambridge Analytica"]
        assert len(ca_entities) > 0, "Cambridge Analytica should be detected"
        for e in ca_entities:
            assert e.cluster != "Meta", (
                f"Cambridge Analytica should not be in Meta cluster, "
                f"got cluster='{e.cluster}'"
            )
            assert e.cluster == "Cambridge Analytica"

    def test_meta_still_detected_separately(self):
        text = (
            "Meta paid a $5 billion fine after Cambridge Analytica "
            "harvested data from Facebook users."
        )
        entities = detect_entities(text)
        meta_entities = [e for e in entities if e.cluster == "Meta"]
        ca_entities = [e for e in entities if e.cluster == "Cambridge Analytica"]
        assert len(meta_entities) > 0, "Meta entities should still be detected"
        assert len(ca_entities) > 0, "Cambridge Analytica should be separate"

    def test_facebook_stays_in_meta_cluster(self):
        """Facebook (the platform) should remain in Meta cluster."""
        text = "Facebook shut down its facial-recognition system in 2021."
        entities = detect_entities(text)
        fb_entities = [e for e in entities if e.entity == "Facebook"]
        assert all(e.cluster == "Meta" for e in fb_entities)


# ── Framing: literal "landmark" suppression ──────────────────────────


class TestLandmarkLiteralSuppression:
    """'landmark' is loaded language when used as a dramatic event modifier
    (e.g. 'landmark ruling') but not when referring to a physical place."""

    def test_historical_landmark_suppressed(self):
        """'historical landmark' is literal geographic usage."""
        text = (
            '"Ask it to mock up an image of you in front of a historical '
            'landmark, cleanly erase a photobomber," the company offers.'
        )
        devices = detect_framing_devices(text)
        landmark_devices = [
            d for d in devices
            if d.device_type == "loaded_language"
            and "landmark" in d.evidence_text.lower()
        ]
        assert len(landmark_devices) == 0, (
            "'historical landmark' is literal usage and should be suppressed"
        )

    def test_landmark_ruling_still_detected(self):
        """'landmark ruling' is loaded language and should be detected."""
        text = "The court issued a landmark ruling against the company."
        devices = detect_framing_devices(text)
        landmark_devices = [
            d for d in devices
            if d.device_type == "loaded_language"
            and "landmark" in d.evidence_text.lower()
        ]
        assert len(landmark_devices) > 0, (
            "'landmark ruling' should still be detected as loaded_language"
        )

    def test_landmark_verdict_still_detected(self):
        """'landmark verdict' is loaded language and should be detected."""
        text = "The jury returned a landmark verdict worth billions."
        devices = detect_framing_devices(text)
        landmark_devices = [
            d for d in devices
            if d.device_type == "loaded_language"
            and "landmark" in d.evidence_text.lower()
        ]
        assert len(landmark_devices) > 0

    def test_famous_landmark_suppressed(self):
        """'famous landmark' is literal geographic usage."""
        text = "Take a photo near a famous landmark in your city."
        devices = detect_framing_devices(text)
        landmark_devices = [
            d for d in devices
            if d.device_type == "loaded_language"
            and "landmark" in d.evidence_text.lower()
        ]
        assert len(landmark_devices) == 0, (
            "'famous landmark' is literal usage and should be suppressed"
        )

    def test_national_landmark_suppressed(self):
        """'national landmark' is literal geographic usage."""
        text = "The app lets you visualize national landmark renovations."
        devices = detect_framing_devices(text)
        landmark_devices = [
            d for d in devices
            if d.device_type == "loaded_language"
            and "landmark" in d.evidence_text.lower()
        ]
        assert len(landmark_devices) == 0
