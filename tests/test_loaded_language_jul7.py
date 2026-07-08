"""Tests for framing device improvements from Gizmodo $1.4T article.

Discovered in MediaScope Type A iteration 2026-07-07 13:00 PT.
Tests: whopping, plagued (standalone), watershed/landmark/seismic, eye-watering.
"""

from mediascope.analyze.framing import detect_framing_devices


class TestNewLoadedLanguageTerms:
    """Test loaded_language additions from Jul 7 2026 iteration."""

    def test_whopping(self):
        text = "The company faced a whopping $1.4 trillion penalty."
        frames = detect_framing_devices(text)
        loaded = [f for f in frames if f.device_type == "loaded_language"]
        evidence = " ".join(f.evidence_text for f in loaded).lower()
        assert "whopping" in evidence

    def test_plagued_standalone(self):
        text = "Meta has been plagued by teen safety controversies."
        frames = detect_framing_devices(text)
        loaded = [f for f in frames if f.device_type == "loaded_language"]
        evidence = " ".join(f.evidence_text for f in loaded).lower()
        assert "plagued" in evidence

    def test_scandal_plagued_still_works(self):
        text = "The scandal-plagued executive resigned."
        frames = detect_framing_devices(text)
        loaded = [f for f in frames if f.device_type == "loaded_language"]
        evidence = " ".join(f.evidence_text for f in loaded).lower()
        assert "scandal-plagued" in evidence or "plagued" in evidence

    def test_watershed(self):
        text = "Legal experts called it a watershed verdict."
        frames = detect_framing_devices(text)
        loaded = [f for f in frames if f.device_type == "loaded_language"]
        evidence = " ".join(f.evidence_text for f in loaded).lower()
        assert "watershed" in evidence

    def test_landmark(self):
        text = "The landmark ruling set new precedent for the industry."
        frames = detect_framing_devices(text)
        loaded = [f for f in frames if f.device_type == "loaded_language"]
        evidence = " ".join(f.evidence_text for f in loaded).lower()
        assert "landmark" in evidence

    def test_seismic(self):
        text = "The decision sent seismic shockwaves through Silicon Valley."
        frames = detect_framing_devices(text)
        loaded = [f for f in frames if f.device_type == "loaded_language"]
        evidence = " ".join(f.evidence_text for f in loaded).lower()
        assert "seismic" in evidence

    def test_jaw_dropping(self):
        text = "The jaw-dropping penalty exceeded all expectations."
        frames = detect_framing_devices(text)
        loaded = [f for f in frames if f.device_type == "loaded_language"]
        evidence = " ".join(f.evidence_text for f in loaded).lower()
        assert "jaw-dropping" in evidence

    def test_eye_watering(self):
        text = "An eye-watering sum that dwarfs previous fines."
        frames = detect_framing_devices(text)
        loaded = [f for f in frames if f.device_type == "loaded_language"]
        evidence = " ".join(f.evidence_text for f in loaded).lower()
        assert "eye-watering" in evidence

    def test_sweeping(self):
        text = "Regulators announced sweeping new restrictions on the platform."
        frames = detect_framing_devices(text)
        loaded = [f for f in frames if f.device_type == "loaded_language"]
        evidence = " ".join(f.evidence_text for f in loaded).lower()
        assert "sweeping" in evidence
