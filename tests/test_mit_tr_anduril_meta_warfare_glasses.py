"""Tests for MIT Technology Review: Inside Anduril and Meta's quest to make
smart glasses for warfare (James O'Donnell, 2026-05-18).

Article deep dive: defense-tech entity detection, failure_precedent framing
device (new), analogy_stacking false-positive filtering, context-gated Llama
entity alias, source affiliation, and sentiment calibration for neutral-
skeptical military technology reporting.
"""

import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sentiment import analyze_composite
from mediascope.analyze.sources import extract_sources
from mediascope.analyze.topics import classify_topic

# ---------------------------------------------------------------------------
# Fixture: article text
# ---------------------------------------------------------------------------

_ARTICLE_PATH = (
    "examples/sample_output/"
    "mit_tech_review_anduril_meta_smart_glasses_warfare_2026_05_18_article.txt"
)


@pytest.fixture(scope="module")
def article_text():
    import pathlib
    root = pathlib.Path(__file__).resolve().parent.parent
    with open(root / _ARTICLE_PATH) as f:
        text = f.read()
    lines = text.split("\n")
    body_start = next(i for i, l in enumerate(lines) if l.strip() == "") + 1
    return "\n".join(lines[body_start:])


@pytest.fixture(scope="module")
def article_title():
    import pathlib
    root = pathlib.Path(__file__).resolve().parent.parent
    with open(root / _ARTICLE_PATH) as f:
        first_line = f.readline()
    return first_line.replace("Title: ", "").strip()


# ========================================================================
# Entity detection
# ========================================================================

class TestEntityDetection:

    def test_defense_tech_cluster_dominant(self, article_text):
        """Defense Tech should be the most-mentioned cluster."""
        from collections import Counter
        mentions = detect_entities(article_text)
        counts = Counter(em.cluster for em in mentions)
        assert counts.most_common(1)[0][0] == "Defense Tech"

    def test_anduril_detected(self, article_text):
        mentions = detect_entities(article_text)
        anduril = [em for em in mentions if em.entity == "Anduril"]
        assert len(anduril) >= 3, "Anduril should appear multiple times"

    def test_meta_cluster_detected(self, article_text):
        from collections import Counter
        mentions = detect_entities(article_text)
        meta_count = sum(1 for em in mentions if em.cluster == "Meta")
        assert meta_count >= 5, f"Meta cluster should have 5+ mentions, got {meta_count}"

    def test_facebook_under_meta_cluster(self, article_text):
        mentions = detect_entities(article_text)
        fb = [em for em in mentions if em.entity == "Facebook"]
        assert fb, "Facebook should be detected"
        assert all(em.cluster == "Meta" for em in fb)

    def test_microsoft_detected(self, article_text):
        mentions = detect_entities(article_text)
        ms = [em for em in mentions if em.cluster == "Microsoft"]
        assert ms, "Microsoft should be detected (HoloLens context)"

    def test_pentagon_army_us_government(self, article_text):
        mentions = detect_entities(article_text)
        gov = [em for em in mentions if em.cluster == "US Government"]
        assert len(gov) >= 5, f"US Government cluster should have 5+ mentions, got {len(gov)}"

    def test_rand_detected(self, article_text):
        mentions = detect_entities(article_text)
        rand = [em for em in mentions if em.entity == "RAND"]
        assert rand, "RAND (think tank) should be detected"

    def test_trump_political_figures(self, article_text):
        mentions = detect_entities(article_text)
        trump = [em for em in mentions if "Trump" in em.entity]
        assert trump, "Trump should be detected"
        assert all(em.cluster == "Political Figures" for em in trump)


# ========================================================================
# Context-gated Llama entity (regression test for fix)
# ========================================================================

class TestLlamaEntityContextGate:

    def test_llama_model_context_detected(self):
        """'Llama model' should be detected as Meta entity."""
        mentions = detect_entities("The Llama model outperforms competitors.")
        llama = [em for em in mentions if em.entity == "Llama"]
        assert llama, "Llama should be detected with 'model' context"
        assert llama[0].cluster == "Meta"

    def test_llama_animal_not_detected(self):
        """Lowercase 'llama' (animal) should not be detected."""
        mentions = detect_entities("They saw a llama in the field.")
        llama = [em for em in mentions if "lama" in em.entity.lower()]
        assert not llama, "Animal 'llama' should not match Meta cluster"

    def test_meta_possessive_llama_detected(self):
        """'Meta's Llama' should detect both Meta and Llama."""
        mentions = detect_entities("Meta's Llama is used for translation.")
        entities = {em.entity for em in mentions}
        assert "Meta" in entities, "Meta should be detected"
        assert "Llama" in entities, "Llama should be detected after 'Meta's'"


# ========================================================================
# Framing devices
# ========================================================================

class TestFramingDevices:

    def test_military_techno_optimism_detected(self, article_text):
        devices = detect_framing_devices(article_text)
        mto = [d for d in devices if d.device_type == "military_techno_optimism"]
        assert len(mto) >= 3, (
            f"Expected 3+ military_techno_optimism, got {len(mto)}"
        )

    def test_failure_precedent_detected(self, article_text):
        """failure_precedent (new device) should detect Microsoft contract cancellation."""
        devices = detect_framing_devices(article_text)
        fp = [d for d in devices if d.device_type == "failure_precedent"]
        assert len(fp) >= 1, "failure_precedent should detect at least 1 instance"
        # At least one should reference the cancelled contract
        evidence = " ".join(d.evidence_text for d in fp)
        assert "cancel" in evidence.lower(), (
            "failure_precedent should reference cancelled contract"
        )

    def test_analogy_stacking_not_false_positive(self, article_text):
        """analogy_stacking should NOT fire — all similes are factual examples."""
        devices = detect_framing_devices(article_text)
        stacking = [d for d in devices if d.device_type == "analogy_stacking"]
        assert len(stacking) == 0, (
            f"analogy_stacking should be 0 (false positive filter), got {len(stacking)}: "
            f"{[d.evidence_text[:60] for d in stacking]}"
        )

    def test_editorial_deflation_detected(self, article_text):
        """'That's the idea, anyway' is editorial deflation."""
        devices = detect_framing_devices(article_text)
        defl = [d for d in devices if d.device_type == "editorial_deflation"]
        assert defl, "Should detect 'That's the idea, anyway' as editorial_deflation"

    def test_selective_rehabilitation_detected(self, article_text):
        """Palmer Luckey's Facebook ouster/Trump support → rehabilitation."""
        devices = detect_framing_devices(article_text)
        rehab = [d for d in devices if d.device_type == "selective_rehabilitation"]
        assert rehab, "Should detect Palmer Luckey rehabilitation narrative"

    def test_ironic_quotation_detected(self, article_text):
        """'the human as a weapons system' should trigger ironic_quotation."""
        devices = detect_framing_devices(article_text)
        ironic = [d for d in devices if d.device_type == "ironic_quotation"]
        assert ironic, "Should detect 'the human as a weapons system' as ironic_quotation"


# ========================================================================
# failure_precedent unit tests
# ========================================================================

class TestFailurePrecedentPatterns:

    def test_cancelled_contract_pattern(self):
        text = ("Microsoft was set to receive a $22 billion production contract "
                "that was ultimately cancelled when the glasses didn't prove viable.")
        devices = detect_framing_devices(text)
        fp = [d for d in devices if d.device_type == "failure_precedent"]
        assert fp, "Should detect 'set to receive ... cancelled'"

    def test_after_entity_lost(self):
        text = "after Microsoft lost the contract, Anduril stepped in."
        devices = detect_framing_devices(text)
        fp = [d for d in devices if d.device_type == "failure_precedent"]
        assert fp, "Should detect 'after X lost'"

    def test_previous_effort_failed(self):
        text = "The previous attempt by Apple didn't prove viable."
        devices = detect_framing_devices(text)
        fp = [d for d in devices if d.device_type == "failure_precedent"]
        assert fp, "Should detect 'previous attempt ... didn't prove viable'"


# ========================================================================
# analogy_stacking false-positive filters (regression tests)
# ========================================================================

class TestAnalogySackingFalsePositives:

    def test_factual_simile_not_analogy(self):
        """'like a truck' in factual identification context is not stacking."""
        text = (
            "The system identifies a target like a truck. Then it classifies "
            "another target like an artillery unit. Finally it recommends action."
        )
        devices = detect_framing_devices(text)
        stacking = [d for d in devices if d.device_type == "analogy_stacking"]
        assert len(stacking) == 0, (
            f"Factual similes should not trigger analogy_stacking: "
            f"{[d.evidence_text[:60] for d in stacking]}"
        )

    def test_recalls_that_not_evocation(self):
        """'recalls that' (memory verb) should not count as evocation."""
        text = (
            "Wong recalls that as a platoon commander, they used a system "
            "like a handheld radio. The platoon also carried gear like a "
            "standard-issue backpack."
        )
        devices = detect_framing_devices(text)
        stacking = [d for d in devices if d.device_type == "analogy_stacking"]
        assert len(stacking) == 0, "Memory verb 'recalls that' should be filtered"


# ========================================================================
# Sentiment
# ========================================================================

class TestSentiment:

    def test_overall_tone_near_neutral(self, article_text, article_title):
        """Article is neutral-to-slightly-skeptical; tone should be near 0."""
        sentiment = analyze_composite(article_text, headline=article_title)
        assert -0.3 <= sentiment.overall_tone <= 0.3, (
            f"Expected near-neutral tone, got {sentiment.overall_tone}"
        )

    def test_framing_corrected(self, article_text, article_title):
        """Framing correction should engage — military_techno_optimism devices
        should push raw VADER positive tone down."""
        sentiment = analyze_composite(article_text, headline=article_title)
        assert sentiment.framing_corrected, "Framing correction should be active"

    def test_source_authority_high(self, article_text, article_title):
        """Named RAND analyst = high source authority."""
        sentiment = analyze_composite(article_text, headline=article_title)
        assert sentiment.source_authority_framing >= 0.5


# ========================================================================
# Sources
# ========================================================================

class TestSources:

    def test_wong_detected(self, article_text):
        sources = extract_sources(article_text)
        names = [s.name for s in sources]
        assert any("Wong" in n for n in names), (
            f"Jonathan Wong (RAND analyst) should be detected. Got: {names}"
        )

    def test_barnett_detected(self, article_text):
        sources = extract_sources(article_text)
        names = [s.name for s in sources]
        assert any("Barnett" in n for n in names), (
            f"Quay Barnett should be detected. Got: {names}"
        )

    def test_no_anonymous_sources(self, article_text):
        """Article uses named sources — no anonymous ones expected."""
        sources = extract_sources(article_text)
        anon = [s for s in sources if s.is_anonymous]
        assert len(anon) == 0, f"Unexpected anonymous sources: {anon}"


# ========================================================================
# Topics
# ========================================================================

class TestTopics:

    def test_defense_military_primary_topic(self, article_text):
        topics = classify_topic(article_text)
        assert topics[0].topic == "defense_military", (
            f"Primary topic should be defense_military, got {topics[0].topic}"
        )

    def test_ai_development_secondary(self, article_text):
        topics = classify_topic(article_text)
        topic_names = [t.topic for t in topics]
        assert "ai_development" in topic_names, (
            "ai_development should be in topic list"
        )
