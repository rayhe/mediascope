"""Regression tests for Reuters Meta scam ads / securities defense article (Jul 13, 2026).

Article: "Meta presses new defense tactic in cases over scam ads promoting stocks"
(Reuters Legal, July 13, 2026).

Covers:
- Framing: power_asymmetry on personal-loss savings narrative ("retirement savings"),
  loaded_language on "depressingly" and "peculiar(ly)",
  self_referential_investigation on "my Reuters colleagues",
  editorial_dramatization on literary-aside undercut ("— while it lasted"),
  rhetorical_question on "Should Meta's potential liability hinge..."
- Entity extraction: Meta cluster (Meta, Facebook, Instagram, WhatsApp)
- Sentiment: loaded language detection for "depressingly", "peculiar"
"""

import pytest
from pathlib import Path

ARTICLE_PATH = Path(__file__).parent.parent / (
    "examples/sample_output/"
    "reuters_meta_scam_ads_securities_defense_2026_07_13_article.txt"
)

ARTICLE_TEXT = ARTICLE_PATH.read_text() if ARTICLE_PATH.exists() else ""


# ---------------------------------------------------------------------------
# Framing device detection — new patterns added in this iteration
# ---------------------------------------------------------------------------


class TestFramingNewPatterns:
    """Framing devices that required pattern additions for this article."""

    @pytest.fixture(autouse=True)
    def _detect(self):
        from mediascope.analyze.framing import detect_framing_devices
        # source_publication required for self_referential_investigation
        # to survive the wire-service cross-citation filter
        self.devices = detect_framing_devices(
            ARTICLE_TEXT, source_publication="Reuters"
        )
        self.types = {d.device_type for d in self.devices}
        self.by_type = {}
        for d in self.devices:
            self.by_type.setdefault(d.device_type, []).append(d)

    def test_power_asymmetry_retirement_savings(self):
        """Personal-loss savings narrative: 'retirement savings' triggers power_asymmetry."""
        assert "power_asymmetry" in self.types
        texts = [d.evidence_text.lower() for d in self.by_type["power_asymmetry"]]
        assert any("retirement" in t or "savings" in t for t in texts)

    def test_loaded_language_depressingly(self):
        """Editorial judgment adverb 'depressingly' detected as loaded_language."""
        assert "loaded_language" in self.types
        texts = [d.evidence_text.lower() for d in self.by_type["loaded_language"]]
        assert any("depressingly" in t for t in texts)

    def test_loaded_language_peculiar(self):
        """'peculiar' detected as loaded_language."""
        texts = [d.evidence_text.lower() for d in self.by_type["loaded_language"]]
        assert any("peculiar" in t for t in texts)

    def test_self_referential_investigation(self):
        """'my Reuters colleagues' triggers self_referential_investigation."""
        assert "self_referential_investigation" in self.types
        texts = [d.evidence_text.lower() for d in self.by_type["self_referential_investigation"]]
        assert any("colleagues" in t or "reuters" in t for t in texts)

    def test_editorial_dramatization_while_it_lasted(self):
        """Literary aside '— while it lasted' triggers editorial_dramatization."""
        assert "editorial_dramatization" in self.types
        texts = [d.evidence_text.lower() for d in self.by_type["editorial_dramatization"]]
        assert any("while it lasted" in t for t in texts)

    def test_rhetorical_question_should_meta(self):
        """'Should Meta's potential liability hinge...' triggers rhetorical_question."""
        assert "rhetorical_question" in self.types
        texts = [d.evidence_text.lower() for d in self.by_type["rhetorical_question"]]
        assert any("hinge" in t or "should" in t for t in texts)


# ---------------------------------------------------------------------------
# Framing device detection — pre-existing patterns
# ---------------------------------------------------------------------------


class TestFramingExistingPatterns:
    """Framing devices that pre-existing patterns should catch."""

    @pytest.fixture(autouse=True)
    def _detect(self):
        from mediascope.analyze.framing import detect_framing_devices
        self.devices = detect_framing_devices(ARTICLE_TEXT)
        self.types = {d.device_type for d in self.devices}

    def test_refusal_amplification(self):
        assert "refusal_amplification" in self.types

    def test_no_comment_implication(self):
        assert "no_comment_implication" in self.types

    def test_scale_magnitude(self):
        assert "scale_magnitude" in self.types

    def test_kicker_framing(self):
        assert "kicker_framing" in self.types


# ---------------------------------------------------------------------------
# Entity extraction
# ---------------------------------------------------------------------------


class TestEntityExtraction:
    """Entity detection for Reuters scam ads article."""

    @pytest.fixture(autouse=True)
    def _detect(self):
        from mediascope.analyze.entities import detect_entities
        self.entities = detect_entities(ARTICLE_TEXT)
        self.clusters = {e.cluster for e in self.entities}
        self.canonical_names = {e.canonical_name for e in self.entities}

    def test_meta_detected(self):
        assert "Meta" in self.clusters

    def test_facebook_canonical(self):
        assert "Facebook" in self.canonical_names

    def test_instagram_canonical(self):
        assert "Instagram" in self.canonical_names

    def test_whatsapp_canonical(self):
        assert "WhatsApp" in self.canonical_names

    def test_meta_cluster_has_subsidiaries(self):
        """Meta cluster should contain Facebook, Instagram, WhatsApp."""
        meta_entities = [e for e in self.entities if e.cluster == "Meta"]
        meta_canonical = {e.canonical_name for e in meta_entities}
        for sub in ("Facebook", "Instagram", "WhatsApp"):
            assert sub in meta_canonical, f"{sub} not in Meta cluster"


# ---------------------------------------------------------------------------
# Sentiment
# ---------------------------------------------------------------------------


class TestSentiment:
    """Sentiment analysis on the article text."""

    @pytest.fixture(autouse=True)
    def _analyze(self):
        from mediascope.analyze.sentiment import analyze_composite
        self.result = analyze_composite(
            ARTICLE_TEXT,
            headline="Meta presses new defense tactic in cases over scam ads promoting stocks",
        )

    def test_loaded_language_detected(self):
        """Article should have high emotional language intensity."""
        assert self.result.emotional_language_intensity > 0.0

    def test_negative_lean(self):
        """Article leans negative given victim narrative and loaded language."""
        assert self.result.overall_tone < 0.0
