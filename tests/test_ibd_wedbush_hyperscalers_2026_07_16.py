"""Tests for IBD Wedbush hyperscalers article analysis (Jul 16, 2026).

Validates entity, source, and framing detection against the IBD article
"AI Internet Hyperscalers: Why Wedbush Prefers Google And Amazon To Meta".

Key regression coverage:
- Reddit/RDDT and eBay/EBAY entity extraction (added Jul 16, 2026)
- Trainium3 as Amazon cluster product (added Jul 16, 2026)
- "the [Org] analyst" corporate spokesperson vs anonymous source fix
- Analyst preference competitive positioning framing patterns
"""
import pathlib
import pytest

from mediascope.analysis import (
    analyze_text,
    detect_entities,
    detect_framing_devices,
    extract_sources,
    classify_topics,
)

_ARTICLE_PATH = (
    pathlib.Path(__file__).resolve().parents[1]
    / "examples"
    / "sample_output"
    / "ibd_wedbush_hyperscalers_meta_neutral_2026_07_16_article.txt"
)

_TITLE = "AI Internet Hyperscalers: Why Wedbush Prefers Google And Amazon To Meta"


@pytest.fixture(scope="module")
def article_text() -> str:
    return _ARTICLE_PATH.read_text()


# ---------------------------------------------------------------------------
# Entity detection
# ---------------------------------------------------------------------------

class TestEntities:
    """Entity cluster coverage for the IBD Wedbush article."""

    @pytest.fixture(scope="class")
    def entities(self, article_text):
        return detect_entities(article_text)

    @pytest.fixture(scope="class")
    def canonical_names(self, entities):
        return {e.canonical_name for e in entities}

    @pytest.fixture(scope="class")
    def entity_texts(self, entities):
        return {e.entity for e in entities}

    def test_core_companies_detected(self, canonical_names):
        """Meta, Google/Alphabet, Amazon, Wedbush must all be detected."""
        for expected in ("Meta", "Alphabet", "Amazon", "Wedbush", "Google"):
            assert expected in canonical_names, f"Missing entity: {expected}"

    def test_reddit_detected(self, canonical_names, entity_texts):
        """Reddit/RDDT entity extraction (added Jul 16 2026)."""
        assert "Reddit" in canonical_names or "Reddit" in entity_texts

    def test_rddt_ticker_detected(self, entity_texts):
        """RDDT stock ticker detected as entity."""
        assert "RDDT" in entity_texts

    def test_ebay_detected(self, canonical_names, entity_texts):
        """eBay entity extraction (added Jul 16 2026)."""
        assert "eBay" in canonical_names or "eBay" in entity_texts

    def test_ebay_ticker_detected(self, entity_texts):
        """EBAY stock ticker detected as entity."""
        assert "EBAY" in entity_texts

    def test_trainium3_detected(self, entity_texts):
        """Trainium3 detected as Amazon cluster product (added Jul 16 2026)."""
        assert "Trainium3" in entity_texts

    def test_mark_zuckerberg_detected(self, canonical_names):
        """Mark Zuckerberg mentioned at article end."""
        assert "Mark Zuckerberg" in canonical_names

    def test_uber_detected(self, canonical_names):
        """Uber Technologies mentioned as a rated stock."""
        assert "Uber" in canonical_names

    def test_muse_spark_detected(self, canonical_names):
        """Muse Spark mentioned as an early-stage Meta AI product."""
        assert "Muse Spark" in canonical_names

    def test_youtube_android_detected(self, canonical_names):
        """YouTube and Android mentioned as Google distribution products."""
        assert "YouTube" in canonical_names
        assert "Android" in canonical_names


# ---------------------------------------------------------------------------
# Source extraction
# ---------------------------------------------------------------------------

class TestSources:
    """Source attribution correctness for the IBD Wedbush article."""

    @pytest.fixture(scope="class")
    def sources(self, article_text):
        return extract_sources(article_text)

    def test_arounian_named_expert(self, sources):
        """Ygal Arounian should be a named, expert source."""
        arounian = [s for s in sources if "Arounian" in s.name]
        assert len(arounian) >= 1, "Arounian not found in sources"
        src = arounian[0]
        assert not src.is_anonymous
        assert src.is_expert
        assert src.source_type == "named"

    def test_wedbush_analyst_not_anonymous(self, sources):
        """'the Wedbush analyst' is a corporate spokesperson, NOT anonymous.

        Bug discovered Jul 16 2026: the prior corporate spokesperson regex
        only matched spokesperson/representative roles, not analyst/director/etc.
        "the Wedbush analyst" = Arounian (named earlier in article).
        """
        wedbush_analyst = [s for s in sources if "Wedbush analyst" in s.name]
        assert len(wedbush_analyst) >= 1, "'the Wedbush analyst' not found"
        src = wedbush_analyst[0]
        assert not src.is_anonymous, (
            f"'the Wedbush analyst' should NOT be anonymous, got type={src.source_type}"
        )
        assert src.source_type == "corporate_spokesperson"
        assert src.affiliation == "Wedbush"

    def test_no_truly_anonymous_sources(self, sources):
        """This article has zero anonymous sources — all named or org-attributed."""
        anon = [s for s in sources if s.is_anonymous]
        assert len(anon) == 0, f"Unexpected anonymous sources: {[s.name for s in anon]}"


# ---------------------------------------------------------------------------
# Framing devices
# ---------------------------------------------------------------------------

class TestFraming:
    """Framing device detection for the IBD Wedbush article."""

    @pytest.fixture(scope="class")
    def devices(self, article_text):
        return detect_framing_devices(article_text)

    @pytest.fixture(scope="class")
    def device_types(self, devices):
        return [d.device_type for d in devices]

    def test_competitive_positioning_detected(self, device_types):
        """Analyst preference language should trigger competitive_positioning.

        Added Jul 16 2026: "Prefers Google And Amazon To Meta", "better picks
        in that race", "remain on the sidelines", "more cautious on".
        """
        assert "competitive_positioning" in device_types

    def test_multiple_competitive_positioning(self, devices):
        """At least 2 competitive positioning instances should be found."""
        cp = [d for d in devices if d.device_type == "competitive_positioning"]
        assert len(cp) >= 2, f"Expected >=2 competitive_positioning, got {len(cp)}"

    def test_scale_magnitude_detected(self, device_types):
        """'hundreds of billions' should trigger scale_magnitude."""
        assert "scale_magnitude" in device_types

    def test_analyst_authority_detected(self, device_types):
        """'Wedbush analyst Ygal Arounian' should trigger analyst_authority."""
        assert "analyst_authority" in device_types

    def test_no_litigation_false_positive(self, device_types):
        """Financial analyst article should NOT trigger litigation framing."""
        for dt in device_types:
            assert "litigation" not in dt, f"Unexpected litigation device: {dt}"


# ---------------------------------------------------------------------------
# Full analysis integration
# ---------------------------------------------------------------------------

class TestFullAnalysis:
    """Integration test for analyze_text on the IBD article."""

    @pytest.fixture(scope="class")
    def result(self, article_text):
        return analyze_text(article_text, title=_TITLE, target_entity="Meta")

    def test_primary_entity_is_meta(self, result):
        assert result["primary_entity"] == "Meta"

    def test_sentiment_positive_raw(self, result):
        """VADER scores this positive (0.65) due to financial vocabulary.

        This is a known limitation (§16 ACCURACY_GUIDE.md): financial genre
        words like 'outperform', 'rally', 'upside' inflate VADER tone.
        Documenting expected behavior, not asserting correctness.
        """
        assert result["sentiment"]["overall_tone"] > 0.4

    def test_topics_include_financial(self, result):
        """Primary topic should be financial_markets or financial_results."""
        topic_names = [t["topic"] for t in result["topics"]]
        assert any(t.startswith("financial") for t in topic_names)
