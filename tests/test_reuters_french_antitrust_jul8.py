"""Tests for Reuters French antitrust vs Meta article (Jul 8, 2026).

Type A deep dive — validates:
1. content_licensing topic classification (new topic, added Jul 8)
2. antitrust_regulation as secondary topic
3. escalation_amplification: "a growing number between" (new pattern)
4. precedent_analogy: "resulting in large fines... particularly Google" (new pattern)
5. expert_consensus_authority: Benoit Coeure, president
6. Entity detection: Meta, DVP, APIG, France's competition authority, Google
7. Source extraction: Benoit Coeure (named), Meta (org), DVP (org)
8. French Media Associations entity cluster (DVP, APIG, Le Monde, Les Echos)
9. EU Regulatory entity cluster (France's competition authority)
"""

import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources
from mediascope.analyze.topics import classify_topic


# --- Article text ---
ARTICLE = (
    "French antitrust watchdog orders Meta to resume talks with media "
    "groups over publishing fees\n\n"
    "France's competition authority on Wednesday ordered Meta Platforms "
    "to put forward a payment plan and resume talks with French media "
    "groups that are seeking a year of unpaid fees for the use of their "
    "content online.\n\n"
    "The case is one of a growing number between publishers and tech "
    "companies over the use of content published on social media or used "
    "for AI training that have triggered litigation.\n\n"
    "Lodged by French media associations DVP and APIG, the French "
    "complaint alleged that Meta attempted to impose its own method for "
    "calculating fees for the re-use of published content on its "
    "services, while refusing to provide the information needed for them "
    "to evaluate the remuneration.\n\n"
    "The authority said Meta likely abused its dominant position, and it "
    "ordered the Facebook owner to put forward details of its payment "
    "plan within 15 days.\n\n"
    "In a statement, Meta said it disagreed with the competition "
    "authority's decisions but would engage with the process.\n\n"
    '"We remain committed to reaching a fair deal with DVP and APIG and '
    "we hope these decisions will mean the publishers now engage in good "
    'faith," it said in an emailed statement.\n\n'
    "Media rights group DVP, which includes the newspapers Le Monde and "
    "Les Echos, said it was satisfied with the decision and welcomed the "
    "renewed talks.\n\n"
    "WHAT ARE 'NEIGHBOURING RIGHTS'?\n\n"
    'At the heart of the dispute are "neighbouring rights," which in the '
    "European Union allow print media to seek payment for the digital use "
    "of their content.\n\n"
    "France has sought to strictly enforce the EU rules, resulting in "
    "large fines in recent years for tech companies, particularly "
    "Alphabet's Google.\n\n"
    "The competition authority said it did not set a provisional amount "
    "for the unpaid fees owed by Meta in this case, as it said it did "
    "not want to alter the negotiation with a figure determined by the "
    "authority.\n\n"
    '"Setting a specific amount risked creating a focal point for the '
    "negotiation \u2014 something we wanted to avoid,\" said Benoit Coeure, "
    "president of the antitrust authority.\n\n"
    "A previous agreement between Meta and press associations DVP and "
    "APIG expired in 2024 and the two sides have since failed to agree "
    "on the amount due, meaning the French media have received no "
    "payment since 2025.\n\n"
    "That has caused financial harm to DVP and APIG members, said the "
    "authority, despite their news content continuing to be distributed "
    "on Meta's services."
)

HEADLINE = (
    "French antitrust watchdog orders Meta to resume talks with media "
    "groups over publishing fees"
)


# ── Topic classification ─────────────────────────────────────────────


class TestTopicClassification:
    """Validate topic detection for French antitrust content licensing."""

    def test_content_licensing_is_top_topic(self):
        topics = classify_topic(ARTICLE, headline=HEADLINE)
        top = max(topics, key=lambda t: t.confidence)
        assert top.topic == "content_licensing"

    def test_content_licensing_high_confidence(self):
        topics = classify_topic(ARTICLE, headline=HEADLINE)
        cl = next(t for t in topics if t.topic == "content_licensing")
        assert cl.confidence >= 0.8

    def test_antitrust_regulation_secondary(self):
        topics = classify_topic(ARTICLE, headline=HEADLINE)
        topic_names = [t.topic for t in topics]
        assert "antitrust_regulation" in topic_names

    def test_litigation_detected(self):
        topics = classify_topic(ARTICLE, headline=HEADLINE)
        topic_names = [t.topic for t in topics]
        assert "litigation" in topic_names


# ── Framing devices ──────────────────────────────────────────────────


class TestFramingDevices:
    """Validate framing detection improvements from this article."""

    def test_escalation_amplification_growing_number(self):
        """'a growing number between' triggers escalation_amplification."""
        devices = detect_framing_devices(ARTICLE)
        types = [d.device_type for d in devices]
        assert "escalation_amplification" in types

    def test_escalation_amplification_evidence(self):
        devices = detect_framing_devices(ARTICLE)
        ea = [d for d in devices if d.device_type == "escalation_amplification"]
        assert any("growing number" in d.evidence_text for d in ea)

    def test_precedent_analogy_enforcement(self):
        """'resulting in large fines... particularly Google' fires."""
        devices = detect_framing_devices(ARTICLE)
        types = [d.device_type for d in devices]
        assert "precedent_analogy" in types

    def test_precedent_analogy_evidence(self):
        devices = detect_framing_devices(ARTICLE)
        pa = [d for d in devices if d.device_type == "precedent_analogy"]
        assert any("resulting in large fines" in d.evidence_text for d in pa)

    def test_expert_consensus_authority(self):
        """Benoit Coeure quote fires expert_consensus_authority."""
        devices = detect_framing_devices(ARTICLE)
        types = [d.device_type for d in devices]
        assert "expert_consensus_authority" in types

    def test_total_device_count(self):
        """Article should have exactly 3 framing devices."""
        devices = detect_framing_devices(ARTICLE)
        assert len(devices) == 3


# ── Escalation amplification pattern variants ────────────────────────


class TestEscalationAmplificationVariants:
    """Regression tests for the new 'growing number' pattern variants."""

    @pytest.mark.parametrize("phrase,expected", [
        ("a growing number of lawsuits", True),
        ("the mounting wave of complaints", True),
        ("an increasing number of regulators", True),
        ("a rising tide of litigation", True),
        ("an ever-growing list of agencies", True),
        ("a growing number between publishers and tech companies", True),
        ("an expanding chorus of critics", True),
        ("a swelling body of evidence", True),
        # Should NOT match:
        ("the number is growing", False),  # inverted word order
        ("a small number of cases", False),  # not escalation modifier
    ])
    def test_trend_magnification(self, phrase, expected):
        devices = detect_framing_devices(phrase)
        types = [d.device_type for d in devices]
        if expected:
            assert "escalation_amplification" in types, (
                f"Expected escalation_amplification for: {phrase!r}"
            )
        else:
            assert "escalation_amplification" not in types, (
                f"Unexpected escalation_amplification for: {phrase!r}"
            )


# ── Precedent analogy enforcement pattern variants ───────────────────


class TestPrecedentAnalogyEnforcement:
    """Regression tests for enforcement precedent pattern."""

    @pytest.mark.parametrize("phrase,expected", [
        (
            "resulting in large fines for tech companies, "
            "particularly Alphabet's Google",
            True,
        ),
        (
            "leading to hefty penalties in recent years, "
            "especially Microsoft",
            True,
        ),
        (
            "triggering sanctions against other firms, "
            "notably Amazon",
            True,
        ),
        (
            "resulting in record fines for social media platforms, "
            "including Meta",
            True,
        ),
        # Should NOT match:
        ("resulting in a fair outcome for everyone", False),
        ("the fine was particularly large", False),
    ])
    def test_enforcement_precedent(self, phrase, expected):
        devices = detect_framing_devices(phrase)
        types = [d.device_type for d in devices]
        if expected:
            assert "precedent_analogy" in types, (
                f"Expected precedent_analogy for: {phrase!r}"
            )
        else:
            assert "precedent_analogy" not in types, (
                f"Unexpected precedent_analogy for: {phrase!r}"
            )


# ── Entity detection ─────────────────────────────────────────────────


class TestEntityDetection:
    """Validate entity clusters for this article."""

    def test_meta_detected(self):
        entities = detect_entities(ARTICLE)
        names = [e.canonical_name for e in entities]
        assert "Meta" in names

    def test_dvp_in_french_media_cluster(self):
        entities = detect_entities(ARTICLE)
        dvp = [e for e in entities if e.entity == "DVP"]
        assert dvp
        assert dvp[0].cluster == "French Media Associations"

    def test_apig_in_french_media_cluster(self):
        entities = detect_entities(ARTICLE)
        apig = [e for e in entities if e.entity == "APIG"]
        assert apig
        assert apig[0].cluster == "French Media Associations"

    def test_le_monde_in_french_media_cluster(self):
        entities = detect_entities(ARTICLE)
        lm = [e for e in entities if e.entity == "Le Monde"]
        assert lm
        assert lm[0].cluster == "French Media Associations"

    def test_france_competition_authority_in_eu_regulatory(self):
        entities = detect_entities(ARTICLE)
        fca = [e for e in entities
               if "competition authority" in e.entity.lower()]
        assert fca
        assert fca[0].cluster == "EU Regulatory"

    def test_google_detected(self):
        entities = detect_entities(ARTICLE)
        names = [e.canonical_name for e in entities]
        assert "Google" in names

    def test_alphabet_in_google_cluster(self):
        entities = detect_entities(ARTICLE)
        alpha = [e for e in entities if e.entity == "Alphabet"]
        assert alpha
        assert alpha[0].cluster == "Google"


# ── Source extraction ────────────────────────────────────────────────


class TestSourceExtraction:
    """Validate source detection for this wire article."""

    def test_benoit_coeure_named_source(self):
        sources = extract_sources(ARTICLE)
        named = [s for s in sources if s.source_type == "named"]
        names = [s.name for s in named]
        assert "Benoit Coeure" in names

    def test_meta_organizational_source(self):
        sources = extract_sources(ARTICLE)
        org = [s for s in sources if s.source_type == "organizational"]
        names = [s.name for s in org]
        assert "Meta" in names

    def test_dvp_organizational_source(self):
        sources = extract_sources(ARTICLE)
        org = [s for s in sources if s.source_type == "organizational"]
        names = [s.name for s in org]
        assert "DVP" in names

    def test_at_least_one_named_source(self):
        """Wire article should pass zero-named-sources check."""
        sources = extract_sources(ARTICLE)
        named = [s for s in sources if s.source_type == "named"]
        assert len(named) >= 1
