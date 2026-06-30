"""Tests for MIT TR 'Three things to watch amid Anthropic's latest feud'
article analysis improvements.

Type A deep dive (Jun 27, 2026 15:00 PT): validates new/improved patterns
for rhetorical questions, scare quotes, loaded language, speculative
framing, and cross-domain precedent analogy — all identified as gaps
in manual vs toolkit comparison on this MIT Technology Review piece.
"""

from __future__ import annotations

import re

import pytest

from mediascope.analyze.entities import detect_entities, DEFAULT_ENTITY_CLUSTERS
from mediascope.analyze.framing import detect_framing_devices

# --- Article text (MIT TR "The Algorithm" newsletter, Jun 2026) ---
from pathlib import Path as _Path
_ARTICLE_FILE = _Path(__file__).parent.parent / "examples" / "sample_output" / "mittr_anthropic_feud_jun2026.txt"
ARTICLE_TEXT = _ARTICLE_FILE.read_text() if _ARTICLE_FILE.exists() else ""

# Inline fallback for CI without sample file
_ARTICLE_INLINE = """Three things to watch amid Anthropic's latest feud with the government

For those of you enjoying your summer unaware of Anthropic's latest feud with the US government, here's a recap: In April the company said it had built an AI model called Mythos that was so good at working with code it could pose a global cybersecurity threat.

People worried about catastrophic effects of AI—broadly labeled "doomers"—have said for years that the technology poses a threat to humanity. And the result so far looks less like a safety plan than like a superficial reaction.

There's plenty to dissect about what happened in those few days that led to such drastic action from the government, and it's notable that Amazon CEO Andy Jassy was the one who told government officials that Fable would be dangerous (Amazon is both invested in Anthropic and building its own competing AI models). It's also possible this will be a short-lived ban from the government that doesn't survive legal scrutiny (it's not clear that Anthropic's offering access to Fable really counts as "exporting" it, for example).

The French politician Bruno Retailleau described it as a "wake-up call" that should motivate Europe to build more AI.

It's possible that companies, including those in the US and Europe, will decide that working with Chinese models is just easier, as the skyrocketing of shares in the Chinese startup Zhipu suggests. Playing this forward, is it possible the government's next drastic decision will be to say that US companies using models from China pose a threat to national security? I wouldn't write it off.

Such is the risk of applying the concept of nonproliferation to software—trying to control and restrict dangerous AI models in the manner of the uranium used for nuclear weapons.

Right now, the biggest players shaping how AI gets used are the companies and the White House. But with every drastic action from the White House, the pressure for regulations rises.

When President Trump took office, he threw out the restrictive rulebook for how to make AI safe and promised to get out of the way of tech companies. The White House has now called the most valuable AI startup a risk to national security once in the spring, and again in summer. What will fall bring?
"""

TEXT = ARTICLE_TEXT or _ARTICLE_INLINE


# ============================================================
# Entity detection
# ============================================================

class TestEntityDetection:
    """Validate entity cluster coverage on this article."""

    def _entities(self):
        return detect_entities(TEXT, DEFAULT_ENTITY_CLUSTERS)

    def _clusters(self):
        clusters = {}
        for e in self._entities():
            clusters.setdefault(e.cluster, set()).add(e.entity)
        return clusters

    def test_anthropic_cluster_includes_fable(self):
        """Fable (Anthropic model) should be detected."""
        clusters = self._clusters()
        assert "Anthropic" in clusters
        assert "Fable" in clusters["Anthropic"]

    def test_anthropic_cluster_includes_mythos(self):
        """Mythos (Anthropic model) should be detected."""
        clusters = self._clusters()
        assert "Mythos" in clusters["Anthropic"]

    def test_amazon_cluster_includes_jassy(self):
        """Andy Jassy should be detected as Amazon entity."""
        clusters = self._clusters()
        assert "Amazon" in clusters
        assert "Andy Jassy" in clusters["Amazon"]

    def test_chinese_ai_cluster_includes_zhipu(self):
        """Zhipu should be detected as Chinese AI entity."""
        clusters = self._clusters()
        assert "Chinese AI" in clusters
        assert "Zhipu" in clusters["Chinese AI"]

    def test_us_government_cluster(self):
        """White House and Pentagon should be US Government."""
        clusters = self._clusters()
        assert "US Government" in clusters
        assert "White House" in clusters["US Government"]


# ============================================================
# Framing device detection
# ============================================================

class TestFramingDeviceDetection:
    """Validate framing device detection improvements."""

    def _devices(self):
        return detect_framing_devices(TEXT)

    def _device_types(self):
        types = {}
        for d in self._devices():
            types.setdefault(d.device_type, []).append(d.evidence_text)
        return types

    # --- Scare quotes / distancing quotes ---

    def test_scare_quote_doomers(self):
        """'doomers' in quotes should trigger ironic_quotation."""
        types = self._device_types()
        assert "ironic_quotation" in types
        assert any("doomers" in ev for ev in types["ironic_quotation"])

    def test_scare_quote_exporting(self):
        """'exporting' in quotes should trigger ironic_quotation."""
        types = self._device_types()
        assert any("exporting" in ev for ev in types["ironic_quotation"])

    def test_scare_quote_wake_up_call(self):
        """'wake-up call' in quotes should trigger ironic_quotation."""
        types = self._device_types()
        assert any("wake-up call" in ev for ev in types["ironic_quotation"])

    # --- Rhetorical questions ---

    def test_speculative_rhetorical_question(self):
        """'is it possible...?' should trigger rhetorical_question."""
        types = self._device_types()
        assert "rhetorical_question" in types
        assert any("is it possible" in ev.lower() for ev in types["rhetorical_question"])

    def test_cliffhanger_rhetorical_question(self):
        """'What will fall bring?' should trigger rhetorical_question."""
        types = self._device_types()
        assert any("What will fall bring" in ev for ev in types["rhetorical_question"])

    # --- Loaded language ---

    def test_loaded_language_drastic(self):
        """'drastic' should trigger loaded_language."""
        types = self._device_types()
        assert "loaded_language" in types
        assert any("drastic" in ev.lower() for ev in types["loaded_language"])

    def test_loaded_language_superficial(self):
        """'superficial' should trigger loaded_language."""
        types = self._device_types()
        assert any("superficial" in ev.lower() for ev in types["loaded_language"])

    # --- Speculative framing ---

    def test_speculative_framing_fires(self):
        """Article has enough speculative markers for speculative_framing."""
        types = self._device_types()
        assert "speculative_framing" in types
        assert len(types["speculative_framing"]) >= 3

    # --- Precedent analogy ---

    def test_nuclear_nonproliferation_analogy(self):
        """Nuclear nonproliferation analogy should trigger precedent_analogy."""
        types = self._device_types()
        assert "precedent_analogy" in types
        assert any("nonproliferation" in ev for ev in types["precedent_analogy"])

    # --- Sovereignty framing ---

    def test_sovereignty_framing(self):
        """National security framing should trigger sovereignty_framing."""
        types = self._device_types()
        assert "sovereignty_framing" in types

    # --- Overall device count ---

    def test_minimum_device_type_count(self):
        """Article should trigger at least 6 distinct device types."""
        types = self._device_types()
        assert len(types) >= 6, (
            f"Expected ≥6 device types, got {len(types)}: {list(types.keys())}"
        )


# ============================================================
# Pattern-level unit tests for new patterns
# ============================================================

class TestNewPatternUnits:
    """Unit tests for newly added pattern constructions."""

    def test_is_it_possible_question(self):
        """'is it possible X?' should match rhetorical_question."""
        text = "is it possible that the government will ban all open-source AI?"
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "rhetorical_question" in types

    def test_what_will_bring_question(self):
        """'What will X bring?' should match rhetorical_question."""
        text = "What will the next quarter bring?"
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "rhetorical_question" in types

    def test_can_really_question(self):
        """'Can X really Y?' should match rhetorical_question."""
        text = "Can regulators really keep up with AI development?"
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "rhetorical_question" in types

    def test_scare_quote_lowercase(self):
        """Single lowercase word in quotes should match ironic_quotation."""
        text = 'The so-called "safety" measures were widely mocked.'
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "ironic_quotation" in types

    def test_broadly_labeled_scare_quote(self):
        """'broadly labeled X' pattern should match ironic_quotation."""
        text = 'Critics broadly labeled "alarmists" pushed back against the plan.'
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "ironic_quotation" in types

    def test_drastic_loaded_language(self):
        """'drastic' should match loaded_language."""
        text = "The drastic measures taken by regulators shocked the industry."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "loaded_language" in types

    def test_in_the_manner_of_precedent(self):
        """'in the manner of [domain]' should match precedent_analogy."""
        text = "They sought to control algorithms in the manner of the controlled substances used in pharmaceuticals."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "precedent_analogy" in types

    def test_playing_this_forward_speculative(self):
        """'Playing this forward' should count toward speculative_framing markers."""
        # This tests at the marker level, not device-fire level (needs 5+ markers)
        from mediascope.analyze.framing import _SPECULATIVE_FRAMING_PATTERNS
        text = "Playing this forward, the implications are enormous."
        matched = False
        for p in _SPECULATIVE_FRAMING_PATTERNS:
            if p.search(text):
                matched = True
                break
        assert matched, "'Playing this forward' should match a speculative pattern"

    def test_i_wouldnt_write_it_off_speculative(self):
        """'I wouldn't write it off' should match speculative_framing pattern."""
        from mediascope.analyze.framing import _SPECULATIVE_FRAMING_PATTERNS
        text = "I wouldn't write it off as impossible."
        matched = False
        for p in _SPECULATIVE_FRAMING_PATTERNS:
            if p.search(text):
                matched = True
                break
        assert matched, "'I wouldn't write it off' should match a speculative pattern"
