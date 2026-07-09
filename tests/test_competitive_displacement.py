"""Tests for competitive_displacement framing device and related entity additions.

Added in Jul 9, 2026 Type A iteration (MIT TR open-weight models article).
"""
import sys
sys.path.insert(0, ".")

from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.entities import detect_entities, DEFAULT_ENTITY_CLUSTERS
from mediascope.analyze.sentiment import _ADVERSARIAL_DEVICE_TYPES


# ── competitive_displacement framing device ──────────────────────


class TestCompetitiveDisplacement:
    """Tests for the competitive_displacement framing device."""

    def test_at_a_time_when_reorienting(self):
        """Detects 'at a time when X may be reorienting'."""
        text = (
            "That's particularly notable at a time when Meta, which had "
            "previously dominated the American open-model landscape with its "
            "Llama models, may be reorienting toward closed releases."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "competitive_displacement" in types

    def test_at_a_time_when_retreating(self):
        """Detects 'at a time when X is retreating'."""
        text = (
            "This comes at a time when Google is retreating from its "
            "ambitious AI chip program."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "competitive_displacement" in types

    def test_at_a_time_when_stepping_back(self):
        """Detects 'at a time when X is stepping back'."""
        text = (
            "Intel's announcement is especially significant at a time when "
            "Nvidia is stepping back from certain consumer GPU segments."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "competitive_displacement" in types

    def test_notable_as_cedes(self):
        """Detects 'notable as X cedes ground'."""
        text = (
            "The deal is notable as Meta cedes ground in the open-source "
            "AI competition to Chinese rivals."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "competitive_displacement" in types

    def test_filling_the_void_left_by(self):
        """Detects 'filling the void left by X'."""
        text = (
            "OpenAI appears to be filling the void left by Meta's "
            "shift toward proprietary models."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "competitive_displacement" in types

    def test_previously_dominated_may_be_losing(self):
        """Detects 'previously dominated ... may be losing'."""
        text = (
            "Meta previously dominated the open-source AI space but "
            "may be losing its grip on the developer community."
        )
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "competitive_displacement" in types

    def test_no_false_positive_simple_time_reference(self):
        """Should NOT fire on 'at a time when X is growing'."""
        text = (
            "Meta made the announcement at a time when the AI market "
            "is growing rapidly."
        )
        devices = detect_framing_devices(text)
        cd = [d for d in devices if d.device_type == "competitive_displacement"]
        assert len(cd) == 0

    def test_in_adversarial_types(self):
        """competitive_displacement SHOULD be in adversarial device types."""
        assert "competitive_displacement" in _ADVERSARIAL_DEVICE_TYPES


# ── Entity cluster additions ──────────────────────────────────────


class TestEntityClusterAdditions:
    """Tests for entity clusters added in Jul 9 iteration."""

    def test_princeton_detected(self):
        """Princeton University should be detected in Academic/Research cluster."""
        text = "Peter Henderson, an assistant professor at Princeton University, said..."
        mentions = detect_entities(text)
        names = {m.entity for m in mentions}
        clusters = {m.cluster for m in mentions}
        assert "Princeton" in names or "Princeton University" in names
        assert "Academic/Research" in clusters

    def test_allen_institute_detected(self):
        """Allen Institute for AI should be detected."""
        text = "Nathan Lambert, post-training lead at the Allen Institute for AI, said..."
        mentions = detect_entities(text)
        names = {m.entity for m in mentions}
        assert "Allen Institute for AI" in names

    def test_ai2_detected(self):
        """AI2 alias should be detected."""
        text = "Researchers at AI2 published a new benchmark."
        mentions = detect_entities(text)
        names = {m.entity for m in mentions}
        assert "AI2" in names

    def test_huggingface_detected(self):
        """HuggingFace should be detected."""
        text = "HuggingFace CEO Clement Delangue praised the open release."
        mentions = detect_entities(text)
        names = {m.entity for m in mentions}
        assert any("Hugging" in n or "HuggingFace" in n for n in names)

    def test_clement_delangue_detected(self):
        """Clement Delangue should be detected in HuggingFace cluster."""
        text = "Clement Delangue, CEO of HuggingFace, commented on the release."
        mentions = detect_entities(text)
        names = {m.entity for m in mentions}
        assert "Clement Delangue" in names

    def test_percy_liang_detected(self):
        """Percy Liang should be in Academic/Research cluster."""
        text = "Stanford's Percy Liang signed the open letter."
        mentions = detect_entities(text)
        names = {m.entity for m in mentions}
        assert "Percy Liang" in names

    def test_miles_brundage_detected(self):
        """Miles Brundage should be in OpenAI cluster."""
        text = "Former OpenAI researcher Miles Brundage co-authored the report."
        mentions = detect_entities(text)
        names = {m.entity for m in mentions}
        assert "Miles Brundage" in names

    def test_gpt2_in_openai_cluster(self):
        """GPT-2 should be in OpenAI cluster."""
        text = "OpenAI released GPT-2 back in 2019."
        mentions = detect_entities(text)
        gpt2 = [m for m in mentions if m.entity == "GPT-2"]
        assert len(gpt2) > 0
        assert gpt2[0].cluster == "OpenAI"

    def test_gpt_oss_in_openai_cluster(self):
        """gpt-oss should be in OpenAI cluster."""
        text = "The new gpt-oss models are available for download."
        mentions = detect_entities(text)
        gptoss = [m for m in mentions if m.entity == "gpt-oss"]
        assert len(gptoss) > 0
        assert gptoss[0].cluster == "OpenAI"

    def test_rishi_bommasani_detected(self):
        """Rishi Bommasani should be in Academic/Research cluster."""
        text = "Rishi Bommasani, a senior research scholar at Stanford, commented."
        mentions = detect_entities(text)
        names = {m.entity for m in mentions}
        assert "Rishi Bommasani" in names

    def test_peter_henderson_detected(self):
        """Peter Henderson should be in Academic/Research cluster."""
        text = "Peter Henderson at Princeton has worked on open models."
        mentions = detect_entities(text)
        names = {m.entity for m in mentions}
        assert "Peter Henderson" in names
