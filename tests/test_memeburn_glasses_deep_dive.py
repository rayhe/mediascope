"""Tests for framing gaps found during Memeburn Meta Glasses article deep dive.

These tests cover toolkit improvements discovered in the 2026-06-28 23:00 PT
Hour Type A iteration — manual analysis of the Memeburn article
"Meta Is Betting We'll Stop Noticing the Cameras" (Jun 27, 2026).

Improvements:
1. Kicker patterns: open-ended threat / unresolved-question constructions
2. Loaded language: ubiquitous-camera / stealth-recording patterns
3. Rhetorical question: indirect/embedded question via attributed speech
4. Entity: Gizmodo added to Media/Publications cluster
"""

import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mediascope.analyze.framing import detect_framing_devices, FramingDevice
from mediascope.analyze.entities import detect_entities, get_entity_distribution


# ===================================================================
# Kicker Framing: Open-Ended Threat Constructions
# ===================================================================

class TestKickerOpenEndedThreat:
    """Kicker framing should detect articles ending with unresolved threats."""

    def test_whether_catches_up(self):
        """'Whether X catches up before Y' is a kicker device."""
        # Pad with 500+ chars of neutral content so the kicker region check works
        neutral = "The product launched at a competitive price point. " * 12
        kicker = "Whether the privacy questions catch up before the adoption does is the part that's still open."
        text = neutral + kicker
        devices = detect_framing_devices(text)
        kicker_devices = [d for d in devices if d.device_type == "kicker_framing"]
        assert len(kicker_devices) >= 1, (
            f"Expected kicker_framing for 'whether...catches up', got: "
            f"{[d.device_type for d in devices]}"
        )

    def test_remains_to_be_seen(self):
        """'Remains to be seen' is a kicker device."""
        neutral = "The new features were well received by analysts. " * 12
        kicker = "Whether that momentum can last remains to be seen."
        text = neutral + kicker
        devices = detect_framing_devices(text)
        kicker_devices = [d for d in devices if d.device_type == "kicker_framing"]
        assert len(kicker_devices) >= 1

    def test_time_will_tell(self):
        """'Time will tell' is a kicker device."""
        neutral = "Revenue exceeded expectations for the third quarter. " * 12
        kicker = "Only time will tell if the strategy survives contact with regulators."
        text = neutral + kicker
        devices = detect_framing_devices(text)
        kicker_devices = [d for d in devices if d.device_type == "kicker_framing"]
        assert len(kicker_devices) >= 1

    def test_part_thats_still_open(self):
        """'The part that's still open' is a kicker device."""
        neutral = "The company reported strong earnings growth. " * 12
        kicker = "How regulators respond is the part that's still open."
        text = neutral + kicker
        devices = detect_framing_devices(text)
        kicker_devices = [d for d in devices if d.device_type == "kicker_framing"]
        assert len(kicker_devices) >= 1

    def test_yet_to_be_resolved(self):
        """'Yet to be resolved' is a kicker device."""
        neutral = "The merger was approved by both boards unanimously. " * 12
        kicker = "The antitrust concerns are yet to be resolved."
        text = neutral + kicker
        devices = detect_framing_devices(text)
        kicker_devices = [d for d in devices if d.device_type == "kicker_framing"]
        assert len(kicker_devices) >= 1

    def test_open_question(self):
        """'An open question' is a kicker device."""
        neutral = "The platform expanded to twelve new markets this quarter. " * 12
        kicker = "Whether users trust the company with their data is an open question."
        text = neutral + kicker
        devices = detect_framing_devices(text)
        kicker_devices = [d for d in devices if d.device_type == "kicker_framing"]
        assert len(kicker_devices) >= 1


# ===================================================================
# Loaded Language: Ubiquitous-Camera / Stealth-Recording Patterns
# ===================================================================

class TestUbiquitousCameraFraming:
    """Surveillance-flavored language about consumer cameras should fire loaded_language."""

    def test_camera_on_their_face(self):
        """'Camera on their face' triggers loaded_language."""
        text = "They want millions of people to put a camera on their face every day."
        devices = detect_framing_devices(text)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert any("camera on their face" in d.evidence_text.lower() for d in loaded), (
            f"Expected loaded_language for 'camera on their face', got: "
            f"{[(d.device_type, d.evidence_text) for d in devices]}"
        )

    def test_cameras_everywhere(self):
        """'Cameras everywhere' triggers loaded_language."""
        text = "The heading read: Cameras Everywhere, All The Time."
        devices = detect_framing_devices(text)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert any("cameras everywhere" in d.evidence_text.lower() for d in loaded)

    def test_recorded_space(self):
        """'Recorded space' triggers loaded_language."""
        text = "Conversations can happen inside a recorded space without consent."
        devices = detect_framing_devices(text)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert any("recorded space" in d.evidence_text.lower() for d in loaded)

    def test_no_visible_cue(self):
        """'No visible cue' triggers loaded_language."""
        text = "With smart glasses, there's no visible cue to trigger that awareness."
        devices = detect_framing_devices(text)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert any("no visible cue" in d.evidence_text.lower() for d in loaded)

    def test_camera_on_your_face(self):
        """'Camera on your face' triggers loaded_language."""
        text = "When you strap a camera on your face and walk into a café, things change."
        devices = detect_framing_devices(text)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert any("camera on your face" in d.evidence_text.lower() for d in loaded)

    def test_no_obvious_signal(self):
        """'No obvious signal' triggers loaded_language."""
        text = "There is no obvious signal that a device is recording."
        devices = detect_framing_devices(text)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert any("no obvious signal" in d.evidence_text.lower() for d in loaded)

    def test_cameras_always(self):
        """'Cameras always running' triggers loaded_language."""
        text = "The concern is cameras always running on consumer hardware."
        devices = detect_framing_devices(text)
        loaded = [d for d in devices if d.device_type == "loaded_language"]
        assert any("cameras always" in d.evidence_text.lower() for d in loaded)


# ===================================================================
# Rhetorical Question: Indirect/Embedded Pattern
# ===================================================================

class TestIndirectRhetoricalQuestion:
    """Attributed rhetorical questions in indirect speech should be detected."""

    def test_critics_ask_what_exactly(self):
        """'Critics ask what exactly people are supposed to' is rhetorical_question."""
        text = ("When Bosworth talks about society adjusting, critics point to that "
                "gap and ask what exactly people are supposed to be adjusting to.")
        devices = detect_framing_devices(text)
        rq = [d for d in devices if d.device_type == "rhetorical_question"]
        assert len(rq) >= 1, (
            f"Expected rhetorical_question for indirect 'ask what exactly...supposed to', "
            f"got: {[(d.device_type, d.evidence_text) for d in devices]}"
        )

    def test_observers_wonder_how(self):
        """'Observers wonder how users are expected to' is rhetorical_question."""
        text = "Industry observers wonder how users are expected to protect themselves."
        devices = detect_framing_devices(text)
        rq = [d for d in devices if d.device_type == "rhetorical_question"]
        assert len(rq) >= 1

    def test_asked_why_meant_to(self):
        """'They asked why regulators were meant to' is rhetorical_question."""
        text = "Privacy groups asked why regulators were meant to trust the LED indicator."
        devices = detect_framing_devices(text)
        rq = [d for d in devices if d.device_type == "rhetorical_question"]
        assert len(rq) >= 1

    def test_no_false_positive_plain_ask(self):
        """Plain 'asked what' without challenge language should NOT trigger."""
        text = "She asked what the new features would cost."
        devices = detect_framing_devices(text)
        rq = [d for d in devices if d.device_type == "rhetorical_question"]
        assert len(rq) == 0, (
            f"False positive: plain 'asked what' without 'supposed to' etc. should not fire, "
            f"got: {[(d.device_type, d.evidence_text) for d in rq]}"
        )


# ===================================================================
# Entity: Gizmodo Detection
# ===================================================================

class TestGizmodoEntity:
    """Gizmodo should be detected in the Media/Publications cluster."""

    def test_gizmodo_detected(self):
        """Gizmodo mention is detected and clustered under Media/Publications."""
        text = "Gizmodo reports the frame is surprisingly light given what's inside."
        entities = detect_entities(text)
        gizmodo = [e for e in entities if e.canonical_name == "Gizmodo"]
        assert len(gizmodo) == 1, f"Expected 1 Gizmodo entity, got {len(gizmodo)}"
        assert gizmodo[0].cluster == "Media/Publications"

    def test_gizmodo_in_distribution(self):
        """Gizmodo appears in entity distribution under Media/Publications."""
        text = "According to Gizmodo, the product ships next week."
        dist = get_entity_distribution(detect_entities(text))
        assert "Media/Publications" in dist
        assert dist["Media/Publications"] >= 1


# ===================================================================
# Full Article Regression: Memeburn Meta Glasses
# ===================================================================

class TestMemburnFullArticle:
    """Regression: full Memeburn article should produce expected framing counts."""

    @pytest.fixture
    def article_text(self):
        article_path = os.path.join(
            os.path.dirname(__file__), "..",
            "examples", "sample_output",
            "memeburn_meta_glasses_cameras_2026_06_27_article.txt",
        )
        if not os.path.exists(article_path):
            pytest.skip("Memeburn article text not available")
        return open(article_path).read()

    def test_minimum_framing_device_count(self, article_text):
        """Full article should produce at least 8 framing devices."""
        devices = detect_framing_devices(article_text)
        assert len(devices) >= 8, (
            f"Expected >= 8 framing devices, got {len(devices)}: "
            f"{[(d.device_type, d.evidence_text[:40]) for d in devices]}"
        )

    def test_device_type_coverage(self, article_text):
        """Full article should detect at least 4 distinct device types."""
        from mediascope.analyze.framing import summarize_framing
        devices = detect_framing_devices(article_text)
        summary = summarize_framing(devices)
        assert len(summary) >= 4, (
            f"Expected >= 4 distinct device types, got {len(summary)}: {summary}"
        )

    def test_kicker_detected(self, article_text):
        """Kicker framing must fire for the 'whether...catches up' ending."""
        devices = detect_framing_devices(article_text)
        kicker = [d for d in devices if d.device_type == "kicker_framing"]
        assert len(kicker) >= 1

    def test_rhetorical_question_detected(self, article_text):
        """Indirect rhetorical question must fire for 'ask what exactly'."""
        devices = detect_framing_devices(article_text)
        rq = [d for d in devices if d.device_type == "rhetorical_question"]
        assert len(rq) >= 1

    def test_entity_count(self, article_text):
        """Full article should detect at least 19 entity mentions."""
        entities = detect_entities(article_text)
        assert len(entities) >= 19, f"Expected >= 19 entities, got {len(entities)}"

    def test_gizmodo_entity_detected(self, article_text):
        """Gizmodo should be detected in the article entity list."""
        entities = detect_entities(article_text)
        gizmodo = [e for e in entities if e.canonical_name == "Gizmodo"]
        assert len(gizmodo) == 1
