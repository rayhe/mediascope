"""Tests for platform death, vulnerability framing, and VR/Metaverse entity detection.

Added as part of the Horizon Worlds Comedy Club deep dive (2026-06-23).
"""

import pytest

from mediascope.analyze.entities import detect_entities, DEFAULT_ENTITY_CLUSTERS
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sentiment import (
    EMOTIONAL_LANGUAGE,
    PASSIVE_FRAMING,
    _measure_emotional_intensity as measure_emotional_intensity,
)


class TestPlatformDeathVocabulary:
    """Test that platform shutdown / community displacement emotional terms are detected."""

    def test_on_life_support_detected(self):
        assert "on life support" in EMOTIONAL_LANGUAGE

    def test_devastated_detected(self):
        assert "devastated" in EMOTIONAL_LANGUAGE

    def test_broke_down_in_tears_detected(self):
        assert "broke down in tears" in EMOTIONAL_LANGUAGE

    def test_eerily_silent_detected(self):
        assert "eerily silent" in EMOTIONAL_LANGUAGE

    def test_terrified_detected(self):
        assert "terrified" in EMOTIONAL_LANGUAGE

    def test_shutdown_passive_framing(self):
        assert "on life support" in PASSIVE_FRAMING

    def test_disappearing_passive_framing(self):
        assert "just disappearing" in PASSIVE_FRAMING

    def test_emotional_intensity_horizon_article(self):
        """An excerpt from the Horizon Worlds article should score non-zero intensity."""
        text = (
            '"When they announced they were killing it for good, I just broke down '
            'in tears," Millsbertc says. "This is my home." The people here are '
            'terrified of the uncertainty. The service is on life support.'
        )
        score = measure_emotional_intensity(text)
        assert score > 0.0, f"Expected non-zero emotional intensity, got {score}"


class TestVulnerabilityAccessibilityVocabulary:
    """Test that disability/elderly/isolation emotional terms are detected."""

    def test_disability_detected(self):
        assert "disability" in EMOTIONAL_LANGUAGE

    def test_disabled_detected(self):
        assert "disabled" in EMOTIONAL_LANGUAGE

    def test_limited_mobility_detected(self):
        assert "limited mobility" in EMOTIONAL_LANGUAGE

    def test_social_anxiety_detected(self):
        assert "social anxiety" in EMOTIONAL_LANGUAGE

    def test_depression_detected(self):
        assert "depression" in EMOTIONAL_LANGUAGE

    def test_mental_health_detected(self):
        assert "mental health" in EMOTIONAL_LANGUAGE


class TestPlatformDeathFramingDevices:
    """Test framing device detection for platform death / community displacement."""

    def test_on_life_support_detected(self):
        text = "Now, the service is on life support."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "emotional_appeal" in types, f"Expected emotional_appeal, got {types}"

    def test_this_is_my_home_detected(self):
        text = '"This is my home," Millsbertc says.'
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "emotional_appeal" in types, f"Expected emotional_appeal, got {types}"

    def test_broke_down_in_tears_detected(self):
        text = "I just broke down in tears."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "emotional_appeal" in types, f"Expected emotional_appeal, got {types}"

    def test_devastated_detected(self):
        text = "That's why people are just so devastated."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "emotional_appeal" in types, f"Expected emotional_appeal, got {types}"

    def test_eerily_silent_detected(self):
        text = "MetDonald's, a world usually filled with children, is eerily silent."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "emotional_appeal" in types, f"Expected emotional_appeal, got {types}"

    def test_empty_aside_from_detected(self):
        text = "a VR church, which is empty aside from one floating profile."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "emotional_appeal" in types, f"Expected emotional_appeal, got {types}"


class TestVulnerabilityFramingDevices:
    """Test vulnerability/accessibility framing detection."""

    def test_disabled_user_detected(self):
        text = "He says he is disabled and comes to Soapstone because these spaces are easier to access with limited mobility."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "emotional_appeal" in types, f"Expected emotional_appeal for disability mention, got {types}"

    def test_age_mention_detected(self):
        text = "Rickii, a Soapstone user who says she is 63 years old and lives in Montana."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "emotional_appeal" in types, f"Expected emotional_appeal for age mention, got {types}"

    def test_mental_health_framing_detected(self):
        text = "You can come here even if you have a disability or social anxiety or depression."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "emotional_appeal" in types, f"Expected emotional_appeal for mental health mention, got {types}"


class TestVRMetaverseEntityCluster:
    """Test VR/Metaverse entity cluster detection."""

    def test_horizon_worlds_detected(self):
        text = "Meta announced it would shut down Horizon Worlds in VR."
        entities = detect_entities(text, DEFAULT_ENTITY_CLUSTERS)
        clusters = {e.cluster for e in entities}
        assert "VR/Metaverse" in clusters, f"Expected VR/Metaverse cluster, got {clusters}"

    def test_metaverse_detected(self):
        text = "The Comedy Club at the End of the Metaverse."
        entities = detect_entities(text, DEFAULT_ENTITY_CLUSTERS)
        vr_entities = [e for e in entities if e.cluster == "VR/Metaverse"]
        assert len(vr_entities) > 0, "Expected metaverse entity detection"

    def test_vrchat_detected(self):
        text = "It's a different culture in VRChat."
        entities = detect_entities(text, DEFAULT_ENTITY_CLUSTERS)
        vr_entities = [e for e in entities if e.cluster == "VR/Metaverse"]
        assert len(vr_entities) > 0, "Expected VRChat entity detection"

    def test_meta_quest_detected(self):
        text = "Meta Quest VR headsets, including the development of Horizon Worlds."
        entities = detect_entities(text, DEFAULT_ENTITY_CLUSTERS)
        vr_entities = [e for e in entities if e.cluster == "VR/Metaverse"]
        assert len(vr_entities) > 0, "Expected Meta Quest entity detection"


class TestIntegrationHorizonWorldsArticle:
    """End-to-end integration tests using an excerpt from the Horizon Worlds article."""

    EXCERPT = (
        'Last week, Meta announced it would shut down Horizon Worlds in VR to focus '
        'on its mobile version. Now, the service is on life support. '
        '"When they announced they were killing it for good, I just broke down in '
        'tears," Millsbertc says. "This is my home." '
        'He says he is disabled and comes to Soapstone because these spaces are '
        'easier to access with limited mobility. '
        'MetDonald\'s, a world usually filled with children, is eerily silent. '
        '"That\'s why people are just so devastated."'
    )

    def test_multiple_framing_devices_detected(self):
        devices = detect_framing_devices(self.EXCERPT)
        types = {d.device_type for d in devices}
        assert "emotional_appeal" in types

    def test_emotional_intensity_meaningful(self):
        score = measure_emotional_intensity(self.EXCERPT)
        assert score > 0.2, f"Expected meaningful intensity, got {score}"

    def test_meta_and_vr_entities_detected(self):
        entities = detect_entities(self.EXCERPT, DEFAULT_ENTITY_CLUSTERS)
        clusters = {e.cluster for e in entities}
        assert "Meta" in clusters, f"Missing Meta cluster from {clusters}"
        assert "VR/Metaverse" in clusters, f"Missing VR/Metaverse cluster from {clusters}"
