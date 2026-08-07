"""
Kyle Barr (Gizmodo) Cross-Entity Coverage Analysis — The Privacy Gradient Paradox

KEY FINDING: Kyle Barr at Gizmodo (Keleops AG, ZERO financial ties to any tech
company) covers camera-equipped smart glasses across Meta, Samsung, Apple, and
Google — all building functionally identical products. But he applies sharply
different privacy-alarm framing:

  Meta:    -0.65  (apocalyptic: "walking panopticons", "worst company")
  Google:  -0.05  (mild skepticism, one-sentence privacy mention)
  Apple:   -0.10  (sympathetic hero facing impossible choice)
  Samsung: +0.10  (neutral product coverage, positioned as privacy upgrade)

THE PARADOX: All four companies build outward-facing camera glasses. Only Meta
triggers apocalyptic framing. This isolates EDITORIAL CULTURE BIAS as distinct
from FINANCIAL INCENTIVE BIAS.

INTRA-PUBLICATION DIVERGENCE: Raymond Wong (same publication, same beat) applies
equal-opportunity criticism. The Barr-Wong split proves differential framing
operates at the individual journalist level, but the DIRECTION of Barr's
divergence always penalizes Meta and benefits Apple — matching the industry-wide
editorial consensus.

Sources:
- https://gizmodo.com/author/kylebarr (115+ pages of articles)
- https://gizmodo.com/smart-glasses-are-the-one-privacy-nightmare-apple-cant-solve-2000791443
- https://gizmodo.com/apple-is-officially-coming-for-metas-privacy-invading-lunch-with-its-own-smart-glasses-in-late-2027-2000765491
- https://gizmodo.com/heres-samsung-and-googles-rival-to-ray-ban-meta-smart-glasses-2000760595
- Keleops AG ownership (Adweek, Jun 2024)

Created: 2026-08-07
"""
import yaml
import os
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"


def load_gizmodo_profile():
    with open(PROFILES_DIR / "gizmodo.yaml") as f:
        return yaml.safe_load(f)


def load_competitor_research():
    with open(PROFILES_DIR / "competitor-coverage-research.yaml") as f:
        return yaml.safe_load(f)


def get_barr_section():
    profile = load_gizmodo_profile()
    return profile.get("journalist_cross_entity", {}).get("kyle_barr", {})


# ===================================================================
# 1. TestKyleBarrExists — verify profile structure
# ===================================================================
class TestKyleBarrExists:
    """Verify Kyle Barr is documented in the Gizmodo profile."""

    def test_journalist_cross_entity_section_exists(self):
        profile = load_gizmodo_profile()
        assert "journalist_cross_entity" in profile, \
            "gizmodo.yaml must have journalist_cross_entity section"

    def test_kyle_barr_key_exists(self):
        profile = load_gizmodo_profile()
        jce = profile.get("journalist_cross_entity", {})
        assert "kyle_barr" in jce, \
            "journalist_cross_entity must contain kyle_barr"

    def test_barr_role_documented(self):
        barr = get_barr_section()
        assert "role" in barr, "Barr must have role field"
        assert "staff" in barr["role"].lower() or "writer" in barr["role"].lower(), \
            "Barr role should indicate staff writer"

    def test_barr_finding_named(self):
        barr = get_barr_section()
        assert "finding" in barr, "Barr must have a named finding"
        assert "gradient" in barr["finding"].lower() or "paradox" in barr["finding"].lower(), \
            "Finding should reference the Privacy Gradient Paradox"


# ===================================================================
# 2. TestKyleBarrMetaCoverage — Meta tone and framing
# ===================================================================
class TestKyleBarrMetaCoverage:
    """Verify Meta coverage is documented as strongly negative."""

    def test_meta_tone_is_negative(self):
        barr = get_barr_section()
        meta = barr.get("meta", {})
        tone = meta.get("aggregate_tone", 0)
        assert tone <= -0.50, \
            f"Meta aggregate tone should be <= -0.50, got {tone}"

    def test_meta_has_key_language(self):
        barr = get_barr_section()
        meta = barr.get("meta", {})
        lang = meta.get("key_language", [])
        assert len(lang) >= 4, \
            f"Meta should have at least 4 key language examples, got {len(lang)}"

    def test_meta_has_articles(self):
        barr = get_barr_section()
        meta = barr.get("meta", {})
        articles = meta.get("articles", [])
        assert len(articles) >= 2, \
            f"Meta should have at least 2 article examples, got {len(articles)}"

    def test_meta_articles_have_urls(self):
        barr = get_barr_section()
        meta = barr.get("meta", {})
        articles = meta.get("articles", [])
        for art in articles:
            assert "url" in art, f"Article '{art.get('title', '?')}' must have url"
            assert art["url"].startswith("https://gizmodo.com/"), \
                f"Article URL must be on gizmodo.com: {art['url']}"


# ===================================================================
# 3. TestKyleBarrAppleCoverage — Apple sympathetic framing
# ===================================================================
class TestKyleBarrAppleCoverage:
    """Verify Apple coverage is documented as sympathetic."""

    def test_apple_tone_exists(self):
        barr = get_barr_section()
        assert "apple" in barr, "Barr must have apple entity coverage"

    def test_apple_tone_is_near_neutral(self):
        barr = get_barr_section()
        apple = barr.get("apple", {})
        tone = apple.get("aggregate_tone", -999)
        assert -0.25 <= tone <= 0.25, \
            f"Apple tone should be near neutral (-0.25 to +0.25), got {tone}"

    def test_apple_framing_mentions_sympathetic(self):
        barr = get_barr_section()
        apple = barr.get("apple", {})
        label = apple.get("tone_label", "")
        pattern = apple.get("framing_pattern", "")
        combined = (label + " " + pattern).lower()
        assert "sympathetic" in combined or "hero" in combined or "privacy" in combined, \
            "Apple framing should mention sympathetic/hero/privacy positioning"

    def test_apple_has_key_language(self):
        barr = get_barr_section()
        apple = barr.get("apple", {})
        lang = apple.get("key_language", [])
        assert len(lang) >= 2, \
            f"Apple should have at least 2 key language examples, got {len(lang)}"


# ===================================================================
# 4. TestKyleBarrSamsungCoverage — Samsung neutral/positive framing
# ===================================================================
class TestKyleBarrSamsungCoverage:
    """Verify Samsung coverage is documented as neutral-to-positive."""

    def test_samsung_tone_exists(self):
        barr = get_barr_section()
        assert "samsung" in barr, "Barr must have samsung entity coverage"

    def test_samsung_tone_is_neutral_or_positive(self):
        barr = get_barr_section()
        samsung = barr.get("samsung", {})
        tone = samsung.get("aggregate_tone", -999)
        assert tone >= -0.10, \
            f"Samsung tone should be >= -0.10 (neutral/positive), got {tone}"

    def test_samsung_no_alarm_language(self):
        barr = get_barr_section()
        samsung = barr.get("samsung", {})
        pattern = samsung.get("framing_pattern", "").lower()
        alarm_terms = ["nightmare", "panopticon", "surveillance dystopia", "worst company"]
        for term in alarm_terms:
            # Samsung framing should NOT contain alarm language (except when
            # explicitly noting its absence by comparison)
            if term in pattern:
                # Allow if the pattern is describing absence ("no privacy alarm")
                assert "no " + term in pattern or "not " in pattern or "no alarm" in pattern, \
                    f"Samsung framing should not contain alarm language: '{term}'"


# ===================================================================
# 5. TestKyleBarrGoogleCoverage — Google mild skepticism
# ===================================================================
class TestKyleBarrGoogleCoverage:
    """Verify Google coverage is documented as mildly skeptical."""

    def test_google_tone_exists(self):
        barr = get_barr_section()
        assert "google" in barr, "Barr must have google entity coverage"

    def test_google_tone_is_mildly_negative(self):
        barr = get_barr_section()
        google = barr.get("google", {})
        tone = google.get("aggregate_tone", -999)
        assert -0.30 <= tone <= 0.15, \
            f"Google tone should be mildly negative (-0.30 to +0.15), got {tone}"

    def test_google_milder_than_meta(self):
        barr = get_barr_section()
        meta_tone = barr.get("meta", {}).get("aggregate_tone", 0)
        google_tone = barr.get("google", {}).get("aggregate_tone", 0)
        assert google_tone > meta_tone, \
            f"Google tone ({google_tone}) should be less negative than Meta ({meta_tone})"


# ===================================================================
# 6. TestPrivacyGradient — tone ordering and deltas
# ===================================================================
class TestPrivacyGradient:
    """Verify the privacy gradient ordering and deltas."""

    def test_gradient_section_exists(self):
        barr = get_barr_section()
        assert "privacy_gradient" in barr, "Must have privacy_gradient section"

    def test_meta_is_most_negative(self):
        barr = get_barr_section()
        meta = barr.get("meta", {}).get("aggregate_tone", 0)
        apple = barr.get("apple", {}).get("aggregate_tone", 0)
        samsung = barr.get("samsung", {}).get("aggregate_tone", 0)
        google = barr.get("google", {}).get("aggregate_tone", 0)
        assert meta < min(apple, samsung, google), \
            f"Meta ({meta}) should be most negative of all entities"

    def test_meta_apple_delta_at_least_0_4(self):
        barr = get_barr_section()
        gradient = barr.get("privacy_gradient", {})
        delta = gradient.get("meta_apple_delta", 0)
        assert delta >= 0.40, \
            f"Meta-Apple delta should be >= 0.40, got {delta}"

    def test_meta_samsung_delta_at_least_0_5(self):
        barr = get_barr_section()
        gradient = barr.get("privacy_gradient", {})
        delta = gradient.get("meta_samsung_delta", 0)
        assert delta >= 0.50, \
            f"Meta-Samsung delta should be >= 0.50, got {delta}"

    def test_meta_google_delta_at_least_0_4(self):
        barr = get_barr_section()
        gradient = barr.get("privacy_gradient", {})
        delta = gradient.get("meta_google_delta", 0)
        assert delta >= 0.40, \
            f"Meta-Google delta should be >= 0.40, got {delta}"


# ===================================================================
# 7. TestIntraPublicationDivergence — Barr vs Wong comparison
# ===================================================================
class TestIntraPublicationDivergence:
    """Verify the Barr-Wong intra-publication divergence is documented."""

    def test_divergence_section_exists(self):
        barr = get_barr_section()
        assert "intra_publication_divergence" in barr, \
            "Must document intra-publication divergence with Wong"

    def test_wong_comparison_named(self):
        barr = get_barr_section()
        div = barr.get("intra_publication_divergence", {})
        comparison = div.get("comparison", "")
        assert "wong" in comparison.lower(), \
            "Divergence must compare to Raymond Wong"

    def test_barr_more_negative_on_meta_than_wong(self):
        barr = get_barr_section()
        div = barr.get("intra_publication_divergence", {})
        barr_meta = div.get("barr_meta_tone", "")
        wong_meta = div.get("wong_meta_tone", "")
        # Barr should be more negative (apocalyptic vs balanced)
        assert "apocalyptic" in barr_meta.lower() or "-0.6" in barr_meta, \
            f"Barr meta tone should be apocalyptic, got: {barr_meta}"
        assert "balanced" in wong_meta.lower() or "-0.1" in wong_meta, \
            f"Wong meta tone should be balanced, got: {wong_meta}"

    def test_divergence_significance_documented(self):
        barr = get_barr_section()
        div = barr.get("intra_publication_divergence", {})
        sig = div.get("divergence_significance", "")
        assert len(sig) > 100, \
            f"Divergence significance must be substantive (>100 chars), got {len(sig)}"


# ===================================================================
# 8. TestCleanControlSignificance — Gizmodo as clean control
# ===================================================================
class TestCleanControlSignificance:
    """Verify the clean control significance is properly framed."""

    def test_gizmodo_has_zero_financial_ties(self):
        profile = load_gizmodo_profile()
        cr = profile.get("competitor_relationships", {})
        for entity in ["openai", "meta", "anthropic"]:
            if entity in cr:
                tie = cr[entity].get("financial_tie", "")
                assert tie == "none", \
                    f"Gizmodo {entity} financial_tie should be 'none', got '{tie}'"

    def test_finding_summary_mentions_editorial_culture(self):
        barr = get_barr_section()
        summary = barr.get("finding_summary", "")
        assert "editorial culture" in summary.lower() or "cultural" in summary.lower(), \
            "Finding summary must reference editorial culture bias"

    def test_finding_summary_mentions_financial_incentives(self):
        barr = get_barr_section()
        summary = barr.get("finding_summary", "")
        assert "financial" in summary.lower(), \
            "Finding summary must reference financial incentives (to distinguish from)"

    def test_gradient_significance_references_identical_products(self):
        barr = get_barr_section()
        gradient = barr.get("privacy_gradient", {})
        sig = gradient.get("significance", "")
        assert "identical" in sig.lower() or "same" in sig.lower() or "camera" in sig.lower(), \
            "Gradient significance must note products are functionally identical"


# ===================================================================
# 9. TestArticleEvidence — verify article URLs and titles
# ===================================================================
class TestArticleEvidence:
    """Verify article evidence is properly documented."""

    def test_nightmare_article_documented(self):
        barr = get_barr_section()
        articles = barr.get("meta", {}).get("articles", [])
        titles = [a.get("title", "") for a in articles]
        assert any("nightmare" in t.lower() for t in titles), \
            "Must include 'Privacy Nightmare' article"

    def test_privacy_invading_lunch_article_documented(self):
        barr = get_barr_section()
        articles = barr.get("meta", {}).get("articles", [])
        titles = [a.get("title", "") for a in articles]
        assert any("privacy-invading" in t.lower() or "lunch" in t.lower() for t in titles), \
            "Must include 'Privacy-Invading Lunch' article"

    def test_samsung_rival_article_documented(self):
        barr = get_barr_section()
        articles = barr.get("meta", {}).get("articles", [])
        titles = [a.get("title", "") for a in articles]
        assert any("samsung" in t.lower() or "rival" in t.lower() for t in titles), \
            "Must include Samsung/Google Rival article"

    def test_all_articles_have_framing_notes(self):
        barr = get_barr_section()
        articles = barr.get("meta", {}).get("articles", [])
        for art in articles:
            assert "framing_notes" in art, \
                f"Article '{art.get('title', '?')}' must have framing_notes"
            assert len(art["framing_notes"]) >= 50, \
                f"Framing notes for '{art.get('title', '?')}' must be substantive"


# ===================================================================
# 10. TestCrossEntityCompleteness — coverage completeness
# ===================================================================
class TestCrossEntityCompleteness:
    """Verify cross-entity analysis covers all required entities."""

    def test_four_entities_covered(self):
        barr = get_barr_section()
        required = ["meta", "apple", "samsung", "google"]
        for entity in required:
            assert entity in barr, \
                f"Must have {entity} entity coverage"

    def test_each_entity_has_tone(self):
        barr = get_barr_section()
        for entity in ["meta", "apple", "samsung", "google"]:
            section = barr.get(entity, {})
            assert "aggregate_tone" in section, \
                f"{entity} must have aggregate_tone"
            tone = section["aggregate_tone"]
            assert isinstance(tone, (int, float)), \
                f"{entity} tone must be numeric, got {type(tone)}"

    def test_competitor_research_has_barr_finding(self):
        research = load_competitor_research()
        gizmodo = research.get("publications", {}).get("gizmodo", {})
        assert "kyle_barr_privacy_gradient" in gizmodo, \
            "competitor-coverage-research.yaml gizmodo section must have kyle_barr_privacy_gradient"
