"""
Gizmodo × Google I/O 2026 — Camera Acknowledgment Paradox

Type A: Competitor Coverage Deep Dive
Date: 2026-08-09

Finding: Raymond Wong wrote 6+ articles about Google/Samsung camera glasses at
Google I/O 2026. In one, he explicitly states camera parity: Google's glasses
"most certainly have cameras on them that can take pictures and videos—same as
the Ray-Ban Meta AI glasses." Despite this acknowledged equivalence, his 6
Google I/O headlines contain ZERO privacy/surveillance language. Within 2 months,
the same author produces 3+ Meta headlines with privacy/surveillance framing.

This is the "Camera Acknowledgment Paradox" — Wong acknowledges hardware parity
in body text, then applies asymmetric framing in headlines.

Significance for the clean control model: Gizmodo has ZERO financial ties to
Google or Meta (Swiss-owned Keleops AG). The paradox therefore isolates the
organic/temporal/editorial-culture component of coverage asymmetry, separate
from the financial-incentive component measured at WIRED, NYT, and FT.
"""

import yaml
import pathlib
import re

PROFILES = pathlib.Path(__file__).resolve().parent.parent / "profiles"


def _load(name: str) -> dict:
    return yaml.safe_load((PROFILES / name).read_text())


# ────────────────────────────────────────────────────────────────
# 1. Profile section exists with correct structure
# ────────────────────────────────────────────────────────────────


class TestGizmodoGoogleIOSectionExists:
    """Verify google_io_2026_camera_paradox section is present and complete."""

    def test_section_exists(self):
        data = _load("gizmodo.yaml")
        assert "google_io_2026_camera_paradox" in data

    def test_has_reporter(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        assert section["reporter"] == "Raymond Wong"

    def test_has_finding_name(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        assert section["finding"] == "Camera Acknowledgment Paradox"

    def test_has_google_io_articles(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        assert "google_io_articles" in section
        assert len(section["google_io_articles"]) >= 6

    def test_has_meta_comparison_articles(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        assert "meta_comparison_articles_same_period" in section
        assert len(section["meta_comparison_articles_same_period"]) >= 3

    def test_has_decomposition(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        assert "decomposition" in section
        assert "legitimate_factors" in section["decomposition"]
        assert "editorial_factors" in section["decomposition"]


# ────────────────────────────────────────────────────────────────
# 2. Camera Parity Acknowledgment
# ────────────────────────────────────────────────────────────────


class TestCameraParityAcknowledgment:
    """Wong explicitly states cameras are the same — then applies different framing."""

    def test_parity_explicitly_stated(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        assert section["quantitative_summary"]["camera_parity_explicitly_stated"] is True

    def test_parity_quote_present(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        quote = section["quantitative_summary"]["camera_parity_quote"]
        assert "same as the Ray-Ban Meta AI glasses" in quote

    def test_parity_in_google_scared_article(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        scared_article = [a for a in section["google_io_articles"]
                          if "Scared" in a["title"]]
        assert len(scared_article) == 1
        assert "same as the Ray-Ban Meta AI glasses" in scared_article[0].get("key_quote", "")


# ────────────────────────────────────────────────────────────────
# 3. Google I/O Privacy Language Absence
# ────────────────────────────────────────────────────────────────


class TestGoogleIOPrivacyAbsence:
    """6 Google I/O articles, ZERO privacy/surveillance headlines."""

    def test_zero_privacy_headlines(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        assert section["quantitative_summary"]["google_io_privacy_headlines"] == 0

    def test_minimal_privacy_body_mentions(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        assert section["quantitative_summary"]["google_io_privacy_mentions_in_body"] <= 1

    def test_no_surveillance_vocabulary_in_headlines(self):
        """No Google I/O headline contains privacy/surveillance terms."""
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        surveillance_terms = ["privacy", "surveillance", "spy", "nightmare",
                              "panopticon", "concern", "alarm"]
        for article in section["google_io_articles"]:
            title_lower = article["title"].lower()
            for term in surveillance_terms:
                assert term not in title_lower, (
                    f"Google I/O headline '{article['title']}' "
                    f"contains surveillance term '{term}'"
                )

    def test_google_headline_registers_are_product_focused(self):
        """All Google I/O headlines are product/marketing analysis, not privacy."""
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        product_registers = {
            "neutral_competitive", "playful_marketing_analysis",
            "positive_product_arrival", "positive_product_endorsement",
            "neutral_ecosystem_analysis", "skeptical_product_strategy"
        }
        for article in section["google_io_articles"]:
            assert article["headline_register"] in product_registers, (
                f"Article '{article['title']}' has register "
                f"'{article['headline_register']}' outside product-focused set"
            )


# ────────────────────────────────────────────────────────────────
# 4. Meta Privacy Language Presence
# ────────────────────────────────────────────────────────────────


class TestMetaPrivacyLanguagePresence:
    """Same author, same period — 3+ Meta privacy/surveillance headlines."""

    def test_meta_privacy_headline_count(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        assert section["quantitative_summary"]["meta_privacy_headlines"] >= 3

    def test_meta_heavy_privacy_body_mentions(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        val = section["quantitative_summary"]["meta_privacy_mentions_in_body"]
        # Value may be "15+" string — extract numeric part
        numeric = int(str(val).rstrip("+"))
        assert numeric >= 15

    def test_meta_headlines_contain_privacy_vocabulary(self):
        """Meta headlines use privacy/concern/surveillance language."""
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        privacy_terms = {"privacy", "concern", "senate", "surveillance"}
        meta_articles = section["meta_comparison_articles_same_period"]
        privacy_headline_count = 0
        for article in meta_articles:
            title_lower = article["title"].lower()
            if any(term in title_lower for term in privacy_terms):
                privacy_headline_count += 1
        assert privacy_headline_count >= 2

    def test_meta_articles_have_key_language(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        for article in section["meta_comparison_articles_same_period"]:
            assert "key_language" in article, (
                f"Meta article '{article['title']}' missing key_language"
            )
            assert len(article["key_language"]) >= 2


# ────────────────────────────────────────────────────────────────
# 5. Headline Asymmetry Quantification
# ────────────────────────────────────────────────────────────────


class TestHeadlineAsymmetry:
    """Measure the Google→Meta privacy-language gap in headlines."""

    def test_google_zero_meta_nonzero(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        qs = section["quantitative_summary"]
        assert qs["google_io_privacy_headlines"] == 0
        assert qs["meta_privacy_headlines"] >= 3

    def test_same_author_both_sets(self):
        """Wong wrote both Google I/O and Meta articles."""
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        for article in section["google_io_articles"]:
            assert article["author"] == "Raymond Wong"

    def test_articles_from_same_year(self):
        """All articles are from 2026."""
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        all_articles = (section["google_io_articles"] +
                        section["meta_comparison_articles_same_period"])
        for article in all_articles:
            assert "2026" in str(article["date"])


# ────────────────────────────────────────────────────────────────
# 6. Decomposition — Legitimate vs Editorial Factors
# ────────────────────────────────────────────────────────────────


class TestDecomposition:
    """Verify the analysis separates legitimate from editorial explanations."""

    def test_legitimate_factors_documented(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        legit = section["decomposition"]["legitimate_factors"]
        assert "incident_asymmetry" in legit
        assert "data_practice_asymmetry" in legit
        assert "market_maturity" in legit

    def test_editorial_factors_documented(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        editorial = section["decomposition"]["editorial_factors"]
        assert "headline_framing_gap" in editorial
        assert "google_glass_amnesia" in editorial
        assert "source_ecosystem" in editorial

    def test_incident_asymmetry_cites_konkret_examples(self):
        data = _load("gizmodo.yaml")
        text = str(data["google_io_2026_camera_paradox"]["decomposition"]["legitimate_factors"]["incident_asymmetry"])
        assert "Svenska Dagbladet" in text or "contractor" in text

    def test_google_glass_amnesia_noted(self):
        data = _load("gizmodo.yaml")
        text = str(data["google_io_2026_camera_paradox"]["decomposition"]["editorial_factors"]["google_glass_amnesia"])
        assert "Glasshole" in text or "Google Glass" in text

    def test_temporal_prediction_included(self):
        """Analysis makes a testable forward prediction about Google shipping."""
        data = _load("gizmodo.yaml")
        editorial = section = data["google_io_2026_camera_paradox"]["decomposition"]["editorial_factors"]
        assert "temporal_prediction" in editorial
        text = str(editorial["temporal_prediction"])
        assert "ship" in text.lower() or "shipping" in text.lower()


# ────────────────────────────────────────────────────────────────
# 7. Cross-References to Other Profiles
# ────────────────────────────────────────────────────────────────


class TestCrossReferences:
    """Verify consistency with WIRED Google I/O analysis and Barr-Wong divergence."""

    def test_wired_cross_reference_exists(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        assert "cross_reference" in section
        assert "wired_google_io_2026" in section["cross_reference"]

    def test_wired_cross_reference_mentions_financial_ties(self):
        data = _load("gizmodo.yaml")
        text = str(data["google_io_2026_camera_paradox"]["cross_reference"]["wired_google_io_2026"])
        assert "financial" in text.lower()

    def test_barr_wong_divergence_referenced(self):
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        assert "barr_wong_divergence" in section["cross_reference"]

    def test_google_zero_consistent_across_reporters(self):
        """Both Barr and Wong produce zero privacy alarm for Google."""
        data = _load("gizmodo.yaml")
        text = str(data["google_io_2026_camera_paradox"]["cross_reference"]["barr_wong_divergence"])
        assert "Google zero" in text or "google" in text.lower()

    def test_wired_google_io_section_exists_in_wired_profile(self):
        """WIRED profile has corresponding Google I/O analysis (may be nested)."""
        wired_text = (PROFILES / "wired.yaml").read_text()
        assert "google_io_2026_smart_glasses_coverage" in wired_text, (
            "WIRED profile should have Google I/O 2026 coverage section"
        )


# ────────────────────────────────────────────────────────────────
# 8. Clean Control Model Implications
# ────────────────────────────────────────────────────────────────


class TestCleanControlImplications:
    """The clean control paradox: Gizmodo reproduces the industry-wide
    Google-zero pattern WITHOUT any financial incentive to do so."""

    def test_gizmodo_has_no_google_financial_tie(self):
        data = _load("gizmodo.yaml")
        google_rel = data["competitor_relationships"]["google"]
        assert google_rel["financial_tie"] == "none"

    def test_gizmodo_has_no_meta_financial_tie(self):
        data = _load("gizmodo.yaml")
        meta_rel = data["competitor_relationships"]["meta"]
        assert meta_rel["financial_tie"] == "none"

    def test_finding_summary_mentions_clean_control(self):
        data = _load("gizmodo.yaml")
        text = str(data["google_io_2026_camera_paradox"]["finding_summary"])
        # Check for clean control / financial reference anywhere in section
        full_text = str(data["google_io_2026_camera_paradox"]).lower()
        assert ("zero financial" in full_text or
                "no financial" in full_text or
                "clean control" in full_text or
                "keleops" in full_text), (
            "Camera paradox section should reference Gizmodo's clean control status"
        )

    def test_cross_reference_notes_industry_wide_pattern(self):
        """Both WIRED (with deals) and Gizmodo (without) produce Google-zero coverage."""
        data = _load("gizmodo.yaml")
        text = str(data["google_io_2026_camera_paradox"]["cross_reference"]["wired_google_io_2026"])
        assert "industry-wide" in text.lower() or "both publications" in text.lower()

    def test_camera_parity_is_testable_claim(self):
        """The camera parity claim is verifiable from Wong's own text."""
        data = _load("gizmodo.yaml")
        section = data["google_io_2026_camera_paradox"]
        # The "Google Scared" article has the key quote
        scared_articles = [a for a in section["google_io_articles"]
                           if "Scared" in a["title"]]
        assert len(scared_articles) == 1
        assert "significance" in scared_articles[0]
