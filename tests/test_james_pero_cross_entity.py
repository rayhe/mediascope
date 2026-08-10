"""
James Pero (Gizmodo) Cross-Entity Coverage Analysis — Editorial Direction Override

TYPE B: Journalist Cross-Entity Tracking (Aug 10, 2026 16:00 PT)
Mechanism #31: Editorial Direction Override

KEY FINDING: James Pero is Gizmodo's self-described "resident smart glasses guy"
(his words, from the Antizuck app review) with hands-on access to ALL brands:
Meta, Samsung/Google, Apple, Even Realities, Brilliant Labs, INMO, Everysight.
His PRODUCT REVIEWS of Meta are balanced-to-positive — he calls the Neural Band
"groundbreaking," links to Amazon/Best Buy, and says "These are the smart glasses
that anyone interested in the form factor has been waiting for."

BUT his EDITORIAL/ANALYSIS pieces use the standard anti-Meta framing:
- "Can Smart Glasses Ever Be Privacy-Friendly?" (May 21, 2026) interviews ONLY
  Meta competitors (Even Realities, Brilliant Labs) and the EFF, positioning them
  as privacy heroes against Meta as the implied villain
- Section titled "The anti-Meta plan"
- Google/Samsung (building identical camera glasses) get ONE sentence of caveat:
  "Google doesn't have the best track record for respecting user privacy, either"
- Apple is positioned as a privacy champion: "has often made privacy the core of
  its products"

The SPLIT between review-Pero (balanced on Meta) and editorial-Pero (anti-Meta)
suggests EDITORIAL DIRECTION rather than PERSONAL BIAS. This is distinct from:
- Kyle Barr's Privacy Gradient Paradox (personal differential framing)
- Lauren Goode's Lane Assignment (beat segregation)
- Paresh Dave's Emotional Register Asymmetry (vocabulary escalation)

Pero's case isolates the editorial layer: same journalist, same publication,
same topic, but the GENRE (review vs editorial) determines the framing direction.

Sources:
- "Can Smart Glasses Ever Be Privacy-Friendly?" (May 21, 2026) — By James Pero
  https://gizmodo.com/can-smart-glasses-ever-be-privacy-friendly-these-companies-think-so-2000746927
- "We Need to Talk About Smart Glasses" (Oct 2025) — By James Pero
  https://gizmodo.com/we-need-to-talk-about-smart-glasses-2000661487
- "Smart Glasses Are Forcing Wearables to Get Very Weird" (Sep 2025) — By James Pero
  https://gizmodo.com/smart-glasses-are-forcing-wearables-to-get-very-weird-2000674309
- "The Viral 'Antizuck' App" (Aug 5, 2026) — By James Pero
  https://gizmodo.com/the-viral-smart-glasses-sniffing-app-is-informative-but-anticlimactic-2000794504
- "Meta's New AI Smart Glasses Drop Ray-Ban Branding" (Jun 24, 2026) — By James Pero
  https://gizmodo.com/metas-new-smart-glasses-drop-ray-ban-branding-and-add-kylie-jenner-2000775546
- Google I/O 2026 Live Blog — co-authored with Raymond Wong, Kyle Barr
  https://gizmodo.com/live-updates-from-google-io-2026-2000757469
- "The World's First Eye-Tracking Smart Glasses" (Apr 2026) — By James Pero
  https://gizmodo.com/the-worlds-first-eye-tracking-smart-glasses-are-intriguing-and-unpolished-2000743475
"""

import yaml
import os
import pytest
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"


def load_gizmodo_profile():
    with open(PROFILES_DIR / "gizmodo.yaml") as f:
        return yaml.safe_load(f)


def load_competitor_research():
    with open(PROFILES_DIR / "competitor-coverage-research.yaml") as f:
        return yaml.safe_load(f)


def get_pero_section():
    profile = load_gizmodo_profile()
    return profile.get("journalist_cross_entity", {}).get("james_pero", {})


# ===================================================================
# 1. TestJamesPeroPeroExists — verify profile structure
# ===================================================================
class TestJamesPeroExists:
    """Verify James Pero is documented in the Gizmodo profile."""

    def test_james_pero_key_exists(self):
        profile = load_gizmodo_profile()
        jce = profile.get("journalist_cross_entity", {})
        assert "james_pero" in jce, \
            "journalist_cross_entity must contain james_pero"

    def test_pero_role_documented(self):
        pero = get_pero_section()
        assert "role" in pero, "Pero must have role field"

    def test_pero_self_identification(self):
        """Pero self-identifies as 'Gizmodo's resident smart glasses guy'."""
        pero = get_pero_section()
        assert "self_identification" in pero, \
            "Pero must document his self-identification as smart glasses specialist"
        assert "resident" in pero["self_identification"].lower() or \
               "smart glasses" in pero["self_identification"].lower(), \
            "Self-identification should reference 'resident smart glasses guy'"

    def test_pero_finding_named(self):
        pero = get_pero_section()
        assert "finding" in pero, "Pero must have a named finding"
        assert "editorial" in pero["finding"].lower() or \
               "override" in pero["finding"].lower() or \
               "direction" in pero["finding"].lower(), \
            "Finding should reference Editorial Direction Override"

    def test_pero_mechanism_id(self):
        pero = get_pero_section()
        assert pero.get("mechanism_id") == 31, \
            f"Mechanism ID should be 31, got {pero.get('mechanism_id')}"


# ===================================================================
# 2. TestPeroMetaProductReviews — balanced-to-positive in reviews
# ===================================================================
class TestPeroMetaProductReviews:
    """Product reviews of Meta hardware show balanced-to-positive framing."""

    def test_meta_review_tone_is_not_adversarial(self):
        pero = get_pero_section()
        reviews = pero.get("meta_product_reviews", {})
        tone = reviews.get("aggregate_tone", -999)
        assert tone >= -0.15, \
            f"Meta product review tone should be >= -0.15 (balanced/positive), got {tone}"

    def test_meta_reviews_have_positive_language(self):
        pero = get_pero_section()
        reviews = pero.get("meta_product_reviews", {})
        positive = reviews.get("positive_language", [])
        assert len(positive) >= 3, \
            f"Meta reviews should have at least 3 positive language examples, got {len(positive)}"

    def test_neural_band_positive_framing(self):
        """Pero called Meta's Neural Band 'groundbreaking'."""
        pero = get_pero_section()
        reviews = pero.get("meta_product_reviews", {})
        positive = reviews.get("positive_language", [])
        has_neural_band = any(
            "neural band" in p.lower() or "groundbreaking" in p.lower()
            for p in positive
        )
        assert has_neural_band, \
            "Must document positive framing of Meta's Neural Band"

    def test_meta_reviews_have_affiliate_links(self):
        """Pero includes Amazon/Best Buy affiliate links in Meta reviews —
        not something you do for products you frame as privacy villains."""
        pero = get_pero_section()
        reviews = pero.get("meta_product_reviews", {})
        assert reviews.get("includes_affiliate_links", False), \
            "Meta product reviews include Amazon/Best Buy affiliate links"

    def test_meta_review_articles_documented(self):
        pero = get_pero_section()
        reviews = pero.get("meta_product_reviews", {})
        articles = reviews.get("articles", [])
        assert len(articles) >= 3, \
            f"Should document at least 3 Meta product review articles, got {len(articles)}"


# ===================================================================
# 3. TestPeroMetaEditorialFraming — adversarial in editorial pieces
# ===================================================================
class TestPeroMetaEditorialFraming:
    """Editorial/analysis pieces about Meta use adversarial framing."""

    def test_editorial_section_exists(self):
        pero = get_pero_section()
        assert "meta_editorial_pieces" in pero, \
            "Must document Meta editorial/analysis pieces separately from reviews"

    def test_editorial_tone_is_negative(self):
        pero = get_pero_section()
        editorial = pero.get("meta_editorial_pieces", {})
        tone = editorial.get("aggregate_tone", 0)
        assert tone <= -0.30, \
            f"Meta editorial tone should be <= -0.30, got {tone}"

    def test_privacy_friendly_article_documented(self):
        """'Can Smart Glasses Ever Be Privacy-Friendly?' is the key editorial piece."""
        pero = get_pero_section()
        editorial = pero.get("meta_editorial_pieces", {})
        articles = editorial.get("articles", [])
        privacy_articles = [a for a in articles
                           if "privacy" in a.get("title", "").lower()]
        assert len(privacy_articles) >= 1, \
            "Must document the 'Can Smart Glasses Be Privacy-Friendly?' piece"

    def test_anti_meta_plan_section_documented(self):
        """The article has a section literally titled 'The anti-Meta plan'."""
        pero = get_pero_section()
        editorial = pero.get("meta_editorial_pieces", {})
        framing = editorial.get("key_framing_elements", [])
        has_anti_meta = any(
            "anti-meta" in f.lower() or "anti meta" in f.lower()
            for f in framing
        )
        assert has_anti_meta, \
            "Must document the 'The anti-Meta plan' section header"

    def test_source_selection_asymmetry(self):
        """Editorial pieces interview Meta COMPETITORS as privacy heroes, not Meta."""
        pero = get_pero_section()
        editorial = pero.get("meta_editorial_pieces", {})
        sources = editorial.get("source_selection", {})
        competitor_sources = sources.get("competitor_sources", 0)
        meta_sources = sources.get("meta_sources", 0)
        assert competitor_sources > meta_sources, \
            f"Competitor sources ({competitor_sources}) should exceed " \
            f"Meta sources ({meta_sources}) — editorial interviews competitors as heroes"


# ===================================================================
# 4. TestPeroGoogleCoverage — minimal privacy scrutiny
# ===================================================================
class TestPeroGoogleCoverage:
    """Google smart glasses coverage receives minimal privacy scrutiny."""

    def test_google_section_exists(self):
        pero = get_pero_section()
        assert "google_coverage" in pero, \
            "Must document Google smart glasses coverage"

    def test_google_privacy_caveat_is_minimal(self):
        """Google gets ONE sentence of privacy caveat in the 1,500+ word piece."""
        pero = get_pero_section()
        google = pero.get("google_coverage", {})
        caveat = google.get("privacy_caveat_depth", "")
        assert "one_sentence" in caveat.lower() or "minimal" in caveat.lower(), \
            "Google privacy caveat should be documented as minimal/one-sentence"

    def test_google_not_framed_as_villain(self):
        pero = get_pero_section()
        google = pero.get("google_coverage", {})
        tone = google.get("aggregate_tone", -999)
        assert tone >= -0.15, \
            f"Google coverage tone should be >= -0.15 (not villainized), got {tone}"

    def test_google_io_liveblog_neutral(self):
        """I/O live blog coverage is factual and neutral."""
        pero = get_pero_section()
        google = pero.get("google_coverage", {})
        liveblog_tone = google.get("io_liveblog_tone", "")
        assert "neutral" in liveblog_tone.lower() or "descriptive" in liveblog_tone.lower(), \
            "Google I/O live blog coverage should be neutral/descriptive"


# ===================================================================
# 5. TestPeroAppleCoverage — positioned as privacy champion
# ===================================================================
class TestPeroAppleCoverage:
    """Apple is positioned as inherently privacy-positive despite planning camera glasses."""

    def test_apple_section_exists(self):
        pero = get_pero_section()
        assert "apple_coverage" in pero, \
            "Must document Apple smart glasses coverage"

    def test_apple_privacy_framing_is_positive(self):
        """Apple 'has often made privacy the core of its products' per Pero's framing."""
        pero = get_pero_section()
        apple = pero.get("apple_coverage", {})
        assert apple.get("privacy_framing", "") in [
            "positive", "privacy_champion", "inherent_trust"
        ], "Apple should be documented as receiving privacy-positive framing"

    def test_apple_camera_glasses_not_scrutinized(self):
        """Apple is building camera glasses — same hardware — but gets no privacy alarm."""
        pero = get_pero_section()
        apple = pero.get("apple_coverage", {})
        assert not apple.get("receives_surveillance_framing", True), \
            "Apple camera glasses should NOT receive surveillance framing"


# ===================================================================
# 6. TestPeroCompetitorFraming — competitors as privacy heroes
# ===================================================================
class TestPeroCompetitorFraming:
    """Meta competitors are systematically framed as privacy-forward alternatives."""

    def test_even_realities_as_hero(self):
        pero = get_pero_section()
        competitors = pero.get("competitor_hero_framing", {})
        assert "even_realities" in competitors, \
            "Even Realities must be documented as hero-framed"
        er = competitors["even_realities"]
        assert er.get("framing_role") in ["privacy_hero", "anti_meta_alternative"], \
            "Even Realities should be framed as privacy hero"

    def test_brilliant_labs_as_hero(self):
        pero = get_pero_section()
        competitors = pero.get("competitor_hero_framing", {})
        assert "brilliant_labs" in competitors, \
            "Brilliant Labs must be documented as hero-framed"

    def test_competitor_quotes_are_aspirational(self):
        """Competitor CEO quotes are aspirational/philosophical, not interrogative."""
        pero = get_pero_section()
        competitors = pero.get("competitor_hero_framing", {})
        for name, data in competitors.items():
            quote_tone = data.get("quote_framing", "")
            assert "aspirational" in quote_tone.lower() or \
                   "philosophical" in quote_tone.lower() or \
                   "sympathetic" in quote_tone.lower(), \
                f"{name} competitor quotes should be aspirational/philosophical, " \
                f"got: {quote_tone}"


# ===================================================================
# 7. TestPeroGenreSplit — the key mechanism
# ===================================================================
class TestPeroGenreSplit:
    """The genre split (review vs editorial) is the distinguishing mechanism."""

    def test_genre_split_documented(self):
        pero = get_pero_section()
        assert "genre_split" in pero, \
            "Must document the review-vs-editorial genre split mechanism"

    def test_review_genre_is_balanced(self):
        pero = get_pero_section()
        split = pero.get("genre_split", {})
        review_tone = split.get("product_review_meta_tone", -999)
        assert review_tone >= -0.15, \
            f"Product review Meta tone should be >= -0.15, got {review_tone}"

    def test_editorial_genre_is_adversarial(self):
        pero = get_pero_section()
        split = pero.get("genre_split", {})
        editorial_tone = split.get("editorial_meta_tone", 0)
        assert editorial_tone <= -0.30, \
            f"Editorial Meta tone should be <= -0.30, got {editorial_tone}"

    def test_tone_delta_between_genres(self):
        """The delta between review-Pero and editorial-Pero on Meta."""
        pero = get_pero_section()
        split = pero.get("genre_split", {})
        delta = split.get("meta_tone_delta", 0)
        assert delta >= 0.25, \
            f"Genre tone delta should be >= 0.25, got {delta}"

    def test_editorial_direction_hypothesis(self):
        """The split suggests editorial direction, not personal bias."""
        pero = get_pero_section()
        split = pero.get("genre_split", {})
        hypothesis = split.get("mechanism_hypothesis", "")
        assert "editorial" in hypothesis.lower() or "direction" in hypothesis.lower(), \
            "Genre split should support editorial direction hypothesis"


# ===================================================================
# 8. TestPeroHardwareParadox — identical hardware, different framing
# ===================================================================
class TestPeroHardwareParadox:
    """All companies build identical camera glasses but only Meta gets privacy alarm."""

    def test_hardware_equivalence_documented(self):
        pero = get_pero_section()
        assert "hardware_equivalence" in pero, \
            "Must document that all companies build identical camera hardware"

    @pytest.mark.parametrize("company", [
        "meta", "samsung_google", "apple", "snap"
    ])
    def test_all_companies_have_cameras(self, company):
        pero = get_pero_section()
        hw = pero.get("hardware_equivalence", {})
        entry = hw.get(company, {})
        assert entry.get("has_camera", False), \
            f"{company} should be documented as having cameras in smart glasses"

    def test_only_meta_gets_surveillance_framing(self):
        pero = get_pero_section()
        hw = pero.get("hardware_equivalence", {})
        surveillance_framed = [
            company for company, data in hw.items()
            if data.get("receives_surveillance_framing", False)
        ]
        assert surveillance_framed == ["meta"], \
            f"Only Meta should receive surveillance framing, got: {surveillance_framed}"

    def test_samsung_google_data_pipeline_not_scrutinized(self):
        """Samsung sends data through Google Gemini — world's largest ad company —
        but this gets NO privacy scrutiny in Pero's editorial pieces."""
        pero = get_pero_section()
        hw = pero.get("hardware_equivalence", {})
        sg = hw.get("samsung_google", {})
        assert not sg.get("receives_data_pipeline_scrutiny", True), \
            "Samsung/Google's Gemini data pipeline should be documented as " \
            "NOT receiving privacy scrutiny"


# ===================================================================
# 9. TestPeroInCompetitorResearch — mechanism entry in research yaml
# ===================================================================
class TestPeroInCompetitorResearch:
    """Mechanism #31 should be in competitor-coverage-research.yaml."""

    def test_mechanism_31_exists(self):
        research = load_competitor_research()
        mechanisms = research.get("aggregate_findings", {})
        pero_key = [k for k in mechanisms
                   if "pero" in k.lower() or "editorial_direction" in k.lower()]
        assert len(pero_key) >= 1, \
            "competitor-coverage-research.yaml must have a james_pero or " \
            "editorial_direction mechanism entry"

    def test_mechanism_id_is_31(self):
        research = load_competitor_research()
        mechanisms = research.get("aggregate_findings", {})
        for key, data in mechanisms.items():
            if "pero" in key.lower() or "editorial_direction" in key.lower():
                assert data.get("mechanism_id") == 31, \
                    f"Mechanism ID should be 31, got {data.get('mechanism_id')}"
                return
        pytest.fail("Could not find James Pero mechanism entry")


# ===================================================================
# 10. TestPeroLegitimateFactors — document legitimate explanations
# ===================================================================
class TestPeroLegitimateFactors:
    """Document legitimate factors that could explain differential framing."""

    def test_legitimate_factors_documented(self):
        pero = get_pero_section()
        factors = pero.get("legitimate_factors", [])
        assert len(factors) >= 4, \
            f"Should document at least 4 legitimate factors, got {len(factors)}"

    def test_meta_market_share_acknowledged(self):
        """Meta's 69% market share makes it the natural focus of scrutiny."""
        pero = get_pero_section()
        factors = pero.get("legitimate_factors", [])
        has_market_share = any("market share" in f.lower() or "market leader" in f.lower()
                              for f in factors)
        assert has_market_share, \
            "Must acknowledge Meta's dominant market share as a legitimate factor"

    def test_meta_privacy_incidents_acknowledged(self):
        """Meta has had genuine privacy incidents (Kenya contractors, etc.)."""
        pero = get_pero_section()
        factors = pero.get("legitimate_factors", [])
        has_incidents = any("incident" in f.lower() or "contractor" in f.lower()
                           or "kenya" in f.lower()
                           for f in factors)
        assert has_incidents, \
            "Must acknowledge Meta's actual privacy incidents as legitimate factor"

    def test_editorial_assignment_acknowledged(self):
        """Editors assign stories with specific angles — that's normal journalism."""
        pero = get_pero_section()
        factors = pero.get("legitimate_factors", [])
        has_assignment = any("assignment" in f.lower() or "editorial" in f.lower()
                            for f in factors)
        assert has_assignment, \
            "Must acknowledge editorial story assignment as legitimate factor"

    def test_genre_conventions_acknowledged(self):
        """Reviews and analysis pieces have different genre conventions."""
        pero = get_pero_section()
        factors = pero.get("legitimate_factors", [])
        has_genre = any("genre" in f.lower() or "convention" in f.lower()
                        for f in factors)
        assert has_genre, \
            "Must acknowledge genre conventions as legitimate factor"
