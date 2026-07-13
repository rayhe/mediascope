"""Tests for Gizmodo Muse Image Scrapped article (Jul 11, 2026) analysis gaps.

Validates fixes for:
1. SAG-AFTRA spokesperson classified as corporate_spokesperson (not anonymous)
2. Blog post as documentary source
3. Reuters as publication citation
4. Consent alarm for "pulled face data... by default"
5. Temporal compression patterns in policy_reversal
6. Sarcastic "world record" opener in sarcastic_correction
7. Coined-term precedent analogy ("The Ghibli Meme Effect")
8. Path L sentiment correction (quote-inflated body + negative headline)
"""

import pytest

from mediascope.analyze.sources import extract_sources
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sentiment import analyze_composite


ARTICLE_PATH = "examples/sample_output/gizmodo_meta_muse_image_scrapped_2026_07_11_article.txt"


@pytest.fixture(scope="module")
def article_text():
    with open(ARTICLE_PATH) as f:
        return f.read()


@pytest.fixture(scope="module")
def article_body(article_text):
    return "\n".join(article_text.split("\n")[5:])


@pytest.fixture(scope="module")
def article_headline(article_text):
    return article_text.split("\n")[0]


# --- Source extraction tests ---

class TestSourceExtraction:
    def test_sag_aftra_spokesperson_is_corporate(self, article_body):
        """SAG-AFTRA spokesperson should be corporate_spokesperson, not anonymous."""
        sources = extract_sources(article_body)
        sag_sources = [s for s in sources if "sag-aftra" in s.name.lower()]
        assert len(sag_sources) >= 1, "SAG-AFTRA spokesperson not detected"
        for s in sag_sources:
            assert s.source_type == "corporate_spokesperson"
            assert not s.is_anonymous
            assert s.affiliation == "SAG-AFTRA"

    def test_blog_post_is_documentary(self, article_body):
        """Meta's blog post should be detected as a documentary source."""
        sources = extract_sources(article_body)
        doc_sources = [s for s in sources if s.source_type == "documentary"]
        assert len(doc_sources) >= 1, "Blog post documentary source not detected"
        blog_sources = [s for s in doc_sources if "blog" in s.name.lower()]
        assert len(blog_sources) >= 1, "Blog post not in documentary sources"

    def test_reuters_is_publication_citation(self, article_body):
        """Reuters should be detected as a publication citation."""
        sources = extract_sources(article_body)
        reuters_sources = [s for s in sources if "reuters" in s.name.lower()]
        assert len(reuters_sources) >= 1, "Reuters not detected"
        assert reuters_sources[0].source_type == "publication_citation"

    def test_no_anonymous_sources(self, article_body):
        """No sources in this article should be classified as anonymous."""
        sources = extract_sources(article_body)
        anon = [s for s in sources if s.is_anonymous]
        assert len(anon) == 0, f"Unexpected anonymous sources: {[s.name for s in anon]}"


# --- Framing detection tests ---

class TestFramingDetection:
    def test_sarcastic_world_record(self, article_body):
        """Sarcastic 'world record' opener should detect sarcastic_correction."""
        devices = detect_framing_devices(article_body)
        sc = [d for d in devices if d.device_type == "sarcastic_correction"]
        assert len(sc) >= 1, "Sarcastic 'world record' opener not detected"
        assert any("world record" in d.evidence_text.lower() for d in sc)

    def test_consent_alarm_by_default(self, article_body):
        """'pulled face data... by default' should trigger consent_alarm."""
        devices = detect_framing_devices(article_body)
        ca = [d for d in devices if d.device_type == "consent_alarm"]
        assert len(ca) >= 1, "Consent alarm not detected"
        assert any("by default" in d.evidence_text.lower() for d in ca)

    def test_temporal_compression_three_days(self, article_body):
        """'three days in operation' should trigger policy_reversal."""
        devices = detect_framing_devices(article_body)
        pr = [d for d in devices if d.device_type == "policy_reversal"]
        temporal = [d for d in pr if "three days" in d.evidence_text.lower()
                    or "made it to friday" in d.evidence_text.lower()]
        assert len(temporal) >= 1, "Temporal compression not detected in policy_reversal"

    def test_ghibli_meme_effect_precedent(self, article_body):
        """'The Ghibli Meme Effect' should trigger precedent_analogy."""
        devices = detect_framing_devices(article_body)
        pa = [d for d in devices if d.device_type == "precedent_analogy"]
        assert len(pa) >= 1, "Precedent analogy not detected"
        assert any("ghibli" in d.evidence_text.lower() for d in pa)

    def test_minimum_device_count(self, article_body):
        """Article should have at least 7 framing devices after fixes."""
        devices = detect_framing_devices(article_body)
        assert len(devices) >= 7, f"Only {len(devices)} devices detected"


# --- Sentiment correction tests ---

class TestSentimentCorrection:
    def test_framing_corrected(self, article_body, article_headline):
        """Sentiment should be framing-corrected (Path L: quote inflation)."""
        result = analyze_composite(article_body, headline=article_headline)
        assert result.framing_corrected, "Framing correction did not fire"

    def test_corrected_tone_negative(self, article_body, article_headline):
        """Corrected tone should be negative (article is critical of Meta)."""
        result = analyze_composite(article_body, headline=article_headline)
        assert result.overall_tone < 0, f"Expected negative, got {result.overall_tone}"

    def test_raw_tone_positive(self, article_body, article_headline):
        """Raw VADER tone should still be positive (quote inflation)."""
        result = analyze_composite(article_body, headline=article_headline)
        assert result.raw_tone > 0.3, f"Expected positive raw, got {result.raw_tone}"


# --- Standalone pattern tests (not article-dependent) ---

class TestHyphenatedOrgSpokesperson:
    """Corporate spokesperson regex should handle hyphenated org names."""

    @pytest.mark.parametrize("text,expected_org", [
        ("a SAG-AFTRA spokesperson said the deal was bad", "SAG-AFTRA"),
        ("A WGA spokesman told reporters", "WGA"),
    ])
    def test_hyphenated_org_spokesperson(self, text, expected_org):
        sources = extract_sources(text)
        corp = [s for s in sources if s.source_type == "corporate_spokesperson"]
        assert len(corp) >= 1, f"No corporate_spokesperson found for {expected_org}"
        assert corp[0].affiliation == expected_org


class TestDirectPublicationCitation:
    """'According to [Publication]' should be detected."""

    @pytest.mark.parametrize("text,pub", [
        ("According to Reuters, the company confirmed the deal.", "Reuters"),
        ("According to Bloomberg, profits rose sharply.", "Bloomberg"),
    ])
    def test_according_to_publication(self, text, pub):
        sources = extract_sources(text)
        pubs = [s for s in sources if s.source_type == "publication_citation"]
        assert len(pubs) >= 1, f"Publication citation for {pub} not detected"
        assert any(pub.lower() in s.name.lower() for s in pubs)


class TestCoinedTermPrecedentAnalogy:
    """Coined-term pattern analogies should trigger precedent_analogy."""

    @pytest.mark.parametrize("text", [
        'perhaps you could call it "The Ghibli Meme Effect"',
        'what I call "The Streisand Effect on Steroids"',
        "the Cobra Effect in regulation",
        "the Facebook Playbook has become standard",
    ])
    def test_coined_term_analogy(self, text):
        devices = detect_framing_devices(text)
        pa = [d for d in devices if d.device_type == "precedent_analogy"]
        assert len(pa) >= 1, f"Coined-term analogy not detected in: {text!r}"


class TestTemporalCompressionPatterns:
    """Temporal compression patterns should trigger policy_reversal."""

    @pytest.mark.parametrize("text", [
        "It made it to Friday—a little over three days in operation",
        "The feature lasted until Monday before being pulled",
        "only two days live before it was scrapped",
        "barely 48 hours old before being yanked",
    ])
    def test_temporal_compression(self, text):
        devices = detect_framing_devices(text)
        pr = [d for d in devices if d.device_type == "policy_reversal"]
        assert len(pr) >= 1, f"Temporal compression not detected in: {text!r}"
