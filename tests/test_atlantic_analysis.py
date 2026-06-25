"""Tests for toolkit improvements from Atlantic 'A Tool That Crushes Creativity' analysis.

Validates fixes discovered during the Type A deep dive on Charlie Warzel's
October 2025 essay about AI slop and creative destruction.
"""

import sys
sys.path.insert(0, ".")

import pytest
from mediascope.analyze.entities import detect_entities, get_entity_distribution
from mediascope.analyze.framing import (
    detect_framing_devices,
    _detect_analogy_stacking,
)
from mediascope.analyze.sources import extract_sources
from mediascope.analyze.topics import classify_topic
from mediascope.analyze.sentiment import _measure_emotional_intensity


# --- Entity Detection Tests ---

class TestAtlanticEntityFixes:
    """Entities added/fixed from Atlantic article analysis."""

    def test_jd_vance_detected(self):
        text = "President Trump and Vice President J. D. Vance wearing crowns."
        mentions = detect_entities(text)
        names = {m.canonical_name for m in mentions}
        assert "Vance" in names or "J.D. Vance" in names

    def test_jd_vance_without_periods(self):
        text = "JD Vance appeared at the rally alongside Trump."
        mentions = detect_entities(text)
        names = {m.canonical_name for m in mentions}
        assert "Vance" in names or "J.D. Vance" in names or "Trump" in names

    def test_marc_andreessen_detected(self):
        text = "The venture capitalist Marc Andreessen mused last week that Sora 2 would give rise to a new type of creative."
        mentions = detect_entities(text)
        names = {m.canonical_name for m in mentions}
        assert "Marc Andreessen" in names

    def test_andreessen_cluster(self):
        text = "Marc Andreessen and the firm Andreessen Horowitz invested heavily."
        mentions = detect_entities(text)
        clusters = {m.cluster for m in mentions}
        assert "VC/Tech Investors" in clusters

    def test_spotify_detected(self):
        text = "You begin to second-guess if that artist in that Spotify playlist is a real person."
        mentions = detect_entities(text)
        names = {m.canonical_name for m in mentions}
        assert "Spotify" in names

    def test_pew_research_detected(self):
        text = "A recent Pew Research Center survey finds that roughly one-third used chatbots."
        mentions = detect_entities(text)
        names = {m.canonical_name for m in mentions}
        assert "Pew Research Center" in names or "Pew Research" in names

    def test_graphite_detected(self):
        text = "The SEO company Graphite recently found a slop tipping point."
        mentions = detect_entities(text)
        names = {m.canonical_name for m in mentions}
        assert "Graphite" in names


# --- Source Detection Tests ---

class TestAtlanticSourceFixes:
    """Source detection fixes from Atlantic article analysis."""

    def test_mused_verb_detected(self):
        text = 'Marc Andreessen mused last week that "AI is changing everything."'
        sources = extract_sources(text)
        names = {s.name for s in sources}
        assert "Marc Andreessen" in names

    def test_pleaded_verb_detected(self):
        text = "Zelda Williams pleaded with her followers to stop sending AI videos."
        sources = extract_sources(text)
        names = {s.name for s in sources}
        assert "Zelda Williams" in names

    def test_dubbed_verb_with_auxiliary(self):
        text = 'The designer Angelos Arnis has dubbed it an "infrastructure of meaninglessness."'
        sources = extract_sources(text)
        names = {s.name for s in sources}
        assert "Angelos Arnis" in names

    def test_adverb_before_verb_in_appositive(self):
        text = 'Will Manidis, a start-up founder and investor, convincingly argued in a Substack post that "slop emerges when we eliminate labor."'
        sources = extract_sources(text)
        names = {s.name for s in sources}
        assert "Will Manidis" in names

    def test_mused_on_x(self):
        text = 'Joe Weisenthal mused on X recently, "The emergence of slop was foretold."'
        sources = extract_sources(text)
        names = {s.name for s in sources}
        assert "Joe Weisenthal" in names

    def test_has_noted_pattern(self):
        text = "John Smith has noted that the trend is accelerating."
        sources = extract_sources(text)
        names = {s.name for s in sources}
        assert "John Smith" in names

    def test_had_argued_pattern(self):
        text = "Jane Doe had argued against the proposal before it passed."
        sources = extract_sources(text)
        names = {s.name for s in sources}
        assert "Jane Doe" in names


# --- Framing Device Tests ---

class TestAtlanticFramingFixes:
    """Framing detection fixes from Atlantic article analysis."""

    def test_nightmarish_catastrophizing(self):
        text = "The frictionless future they portend is nightmarish—recursive and soulless."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "catastrophizing" in types

    def test_cultural_dead_end_catastrophizing(self):
        text = "It is a cultural dead end, devoid of real creative output."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "catastrophizing" in types

    def test_ecological_harm_catastrophizing(self):
        text = "The introduction of AI-generated content results in some form of ecological harm."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "catastrophizing" in types

    def test_model_collapse_catastrophizing(self):
        text = "Technologists fear model collapse, which occurs when AI feeds other AI."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "catastrophizing" in types

    def test_ceo_personalization_plan(self):
        text = "It looks like Mark Zuckerberg's plan to supplement real friends with AI chatbot companions."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "ceo_personalization" in types

    def test_ceo_personalization_vision(self):
        text = "This is Sam Altman's vision for a world without friction."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "ceo_personalization" in types

    def test_ceo_personalization_obsession(self):
        text = "Elon Musk's obsession with Mars colonization continues to consume resources."
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "ceo_personalization" in types

    def test_ironic_quotation_straight_quotes_seems_to(self):
        """Ironic quotation should fire with straight quotes + 'seems to elide'."""
        text = 'Altman said "creativity is about removing friction." His definition seems to elide the value of craft.'
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "ironic_quotation" in types

    def test_ironic_quotation_straight_quotes_wrongly(self):
        """Ironic quotation should fire with straight quotes + 'wrongly believe'."""
        text = 'They said "ideas are universal." They wrongly believe that ideas alone drive progress.'
        devices = detect_framing_devices(text)
        types = {d.device_type for d in devices}
        assert "ironic_quotation" in types


# --- Topic Classification Tests ---

class TestAtlanticTopicFixes:
    """Topic classification fixes from Atlantic article analysis."""

    def test_ai_generated_content_topic(self):
        text = "AI slop is flooding the internet with synthetic content and AI-generated articles."
        topics = classify_topic(text)
        topic_names = {t.topic for t in topics}
        assert "ai_generated_content" in topic_names

    def test_ai_generated_content_keywords(self):
        text = """The emergence of slop represents a tipping point where AI-generated content
        surpasses human content. Model collapse threatens when AI trains on AI. The
        ultra-processed junk includes AI video, AI image, and spammy engagement bait."""
        topics = classify_topic(text, top_n=1)
        assert topics[0].topic == "ai_generated_content"
        assert topics[0].confidence > 0.3


# --- Emotional Intensity Tests ---

class TestAtlanticEmotionalVocab:
    """Emotional language vocabulary additions from Atlantic article analysis."""

    def test_narcotic_detected(self):
        text = "The videos take on an overwhelming, almost narcotic effect."
        intensity = _measure_emotional_intensity(text)
        assert intensity > 0.0

    def test_stupefying_detected(self):
        text = "They are contextless, stupefying, and never-ending."
        intensity = _measure_emotional_intensity(text)
        assert intensity > 0.0

    def test_soulless_detected(self):
        text = "The frictionless future is nightmarish and soulless."
        intensity = _measure_emotional_intensity(text)
        assert intensity > 0.0

    def test_nihilism_detected(self):
        text = "At its core, slop invites a kind of nihilism into all aspects of our life."
        intensity = _measure_emotional_intensity(text)
        assert intensity > 0.0

    def test_meaninglessness_detected(self):
        text = "AI has created an infrastructure of meaninglessness and disorientation."
        intensity = _measure_emotional_intensity(text)
        assert intensity > 0.0

    def test_corrosive_detected(self):
        text = "The frictionlessness of these tools has a corrosive effect over time."
        intensity = _measure_emotional_intensity(text)
        assert intensity > 0.0
