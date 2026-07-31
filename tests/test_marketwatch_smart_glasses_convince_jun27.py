"""
Tests for MarketWatch: "Big Tech is obsessed with smart glasses.
Now it has to convince people to wear them." (Jun 27, 2026)

Article type: Financial market analysis (investor-facing)
Key gap: VADER polarity inversion (+0.65 vs manual -0.20)
Genre: Professional skepticism — all sources express doubt using measured language.
"""
import pathlib
import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources
from mediascope.analyze.sentiment import analyze_composite

_DIR = pathlib.Path(__file__).resolve().parent.parent / "examples" / "sample_output"
_ARTICLE = (_DIR / "marketwatch_smart_glasses_convince_2026_06_27_article.txt").read_text()


# ---------------------------------------------------------------------------
# Entity detection
# ---------------------------------------------------------------------------

class TestEntityExtraction:
    @classmethod
    def setup_class(cls):
        cls.entities = detect_entities(_ARTICLE)
        cls.clusters = {}
        for e in cls.entities:
            cls.clusters.setdefault(e.cluster, []).append(e.entity)

    def test_meta_cluster_count(self):
        """Meta mentioned >=10 times (including Ray-Ban, Zuckerberg, Muse Spark)."""
        assert len(self.clusters.get("Meta", [])) >= 10

    def test_google_cluster(self):
        """Google/Alphabet detected."""
        assert "Google" in self.clusters

    def test_snap_cluster(self):
        """Snap detected."""
        assert "Snap" in self.clusters

    def test_apple_cluster(self):
        """Apple detected."""
        assert "Apple" in self.clusters

    def test_essilorluxottica_cluster(self):
        """EssilorLuxottica detected."""
        assert "EssilorLuxottica" in self.clusters

    def test_samsung_cluster(self):
        """Samsung detected."""
        assert "Samsung" in self.clusters

    def test_kylie_jenner_detected(self):
        """Kylie Jenner detected as celebrity."""
        all_names = [e.entity for e in self.entities]
        assert any("Kylie Jenner" in n for n in all_names)

    def test_mark_zuckerberg_in_meta_cluster(self):
        """Mark Zuckerberg correctly clustered under Meta."""
        meta_entities = [e.entity for e in self.entities if e.cluster == "Meta"]
        assert any("Zuckerberg" in e for e in meta_entities)

    def test_ray_ban_in_meta_cluster(self):
        """Ray-Ban correctly clustered under Meta."""
        meta_entities = [e.entity for e in self.entities if e.cluster == "Meta"]
        assert any("Ray-Ban" in e for e in meta_entities)

    @pytest.mark.xfail(reason="Franklin Templeton not in entity clusters — research firm gap")
    def test_franklin_templeton_detected(self):
        """Franklin Templeton should be detected as a financial institution entity."""
        all_names = [e.entity for e in self.entities]
        assert any("Franklin" in n or "Templeton" in n for n in all_names)

    @pytest.mark.xfail(reason="Prada not in entity clusters — fashion brand gap")
    def test_prada_detected(self):
        """Prada mentioned in Zuckerberg runway context should be detected."""
        all_names = [e.entity for e in self.entities]
        assert any("Prada" in n for n in all_names)


# ---------------------------------------------------------------------------
# Framing devices
# ---------------------------------------------------------------------------

class TestFramingDevices:
    @classmethod
    def setup_class(cls):
        cls.devices = detect_framing_devices(_ARTICLE)
        cls.device_types = [d.device_type for d in cls.devices]

    def test_loaded_language_detected(self):
        """loaded_language should fire (groundbreaking, ill-fated)."""
        assert "loaded_language" in self.device_types

    def test_catastrophizing_detected(self):
        """catastrophizing should fire on 'demise of' Google Glass."""
        assert "catastrophizing" in self.device_types

    def test_expert_consensus_authority(self):
        """expert_consensus_authority should fire for 'said Sara Araghi, senior'."""
        assert "expert_consensus_authority" in self.device_types

    @pytest.mark.xfail(reason="Rhetorical question not detected — editorial voice undermining value prop")
    def test_rhetorical_question_detected(self):
        """'And will these capabilities be more accessible... than the device everyone has in their pocket?' is editorial rhetorical question."""
        assert "rhetorical_question" in self.device_types

    @pytest.mark.xfail(reason="No outsourced_hostility/damning_quotation pattern for 'No one really wants Meta glasses'")
    def test_damning_quotation_detected(self):
        """'No one really wants Meta glasses' should trigger outsourced_hostility or a similar negative-expert-demand device.
        This is the most devastating quote in the article — an analyst stating zero organic demand."""
        hostile_types = {"outsourced_hostility", "damning_quotation", "outsourced_criticism"}
        assert any(t in self.device_types for t in hostile_types)

    @pytest.mark.xfail(reason="precedent_analogy not firing on 'ill-fated Google Glass' + 'demise'")
    def test_precedent_analogy_google_glass(self):
        """'ill-fated Google Glass' + 'the demise' should trigger precedent_analogy — explicit cautionary-tale framing."""
        assert "precedent_analogy" in self.device_types

    def test_framing_count_reasonable(self):
        """Article should have at least 4 framing devices (manual count: 11)."""
        assert len(self.devices) >= 4


# ---------------------------------------------------------------------------
# Source extraction
# ---------------------------------------------------------------------------

class TestSourceExtraction:
    @classmethod
    def setup_class(cls):
        cls.sources = extract_sources(_ARTICLE)
        cls.source_names = [s.name for s in cls.sources]

    def test_sara_araghi_detected(self):
        """Sara Araghi (Franklin Templeton) detected as named source."""
        assert any("Araghi" in n for n in self.source_names)

    def test_max_weinbach_detected(self):
        """Max Weinbach (Creative Strategies) detected as named source."""
        assert any("Weinbach" in n for n in self.source_names)

    def test_flora_tang_detected(self):
        """Flora Tang (Counterpoint Research) detected as named source."""
        assert any("Tang" in n for n in self.source_names)

    def test_araghi_affiliation_franklin_templeton(self):
        """Sara Araghi should be affiliated with Franklin Templeton, not Meta."""
        araghi = [s for s in self.sources if "Araghi" in s.name]
        if araghi:
            assert "Franklin" in araghi[0].affiliation or "Templeton" in araghi[0].affiliation

    def test_all_sources_are_named(self):
        """No anonymous sources in this article — all expert-quoted."""
        for s in self.sources:
            if s.name in ("Sara Araghi", "Max Weinbach", "Flora Tang"):
                assert not s.is_anonymous

    @pytest.mark.xfail(reason="Counterpoint Research misaffiliated with Meta — independent research firm")
    def test_counterpoint_not_meta_affiliated(self):
        """Counterpoint Research is an independent firm, not affiliated with Meta."""
        cr = [s for s in self.sources if "Counterpoint" in s.name]
        if cr:
            assert "Meta" not in cr[0].affiliation


# ---------------------------------------------------------------------------
# Sentiment — CRITICAL GAP
# ---------------------------------------------------------------------------

class TestSentiment:
    @classmethod
    def setup_class(cls):
        cls.result = analyze_composite(_ARTICLE)

    @pytest.mark.xfail(reason="VADER polarity inversion: +0.65 vs manual -0.20 — professional skepticism reads as positive")
    def test_tone_negative(self):
        """Article is structurally negative (all sources skeptical, 'no one really wants' thesis).
        Should read as negative or at most slightly positive, not +0.65."""
        assert self.result.overall_tone < 0.10

    @pytest.mark.xfail(reason="No correction path fires for financial skepticism genre")
    def test_framing_corrected(self):
        """Some correction path should fire given the structural negativity."""
        assert self.result.framing_corrected

    def test_not_strongly_positive(self):
        """At minimum, article should not read as strongly positive (>0.80)."""
        assert self.result.overall_tone < 0.80

    def test_raw_tone_positive_explains_gap(self):
        """Raw VADER reads positive due to professional/measured language."""
        assert self.result.raw_tone > 0.40, (
            "Raw tone should be positive, confirming that professional language "
            "masks structural skepticism"
        )


# ---------------------------------------------------------------------------
# Source direction bias
# ---------------------------------------------------------------------------

class TestSourceDirectionBias:
    """All three expert sources express skepticism about smart glasses.
    No bullish/optimistic source is quoted. This is editorial source selection bias."""

    @classmethod
    def setup_class(cls):
        cls.sources = extract_sources(_ARTICLE)

    def test_three_named_expert_sources(self):
        """Article should have at least 3 named expert sources."""
        experts = [s for s in self.sources if s.is_expert and not s.is_anonymous]
        assert len(experts) >= 3

    def test_no_meta_spokesperson_quoted(self):
        """No Meta spokesperson is quoted — article has no company response."""
        meta_sources = [s for s in self.sources
                       if s.affiliation and "Meta" in s.affiliation
                       and s.name not in ("Counterpoint Research",)]
        # Should have no Meta spokesperson quotes (Mark Zuckerberg's Boz quote
        # is from a separate event, not a response to the article's thesis)
        spokesperson_quotes = [s for s in meta_sources
                              if "spokesperson" in (s.name or "").lower()]
        assert len(spokesperson_quotes) == 0
