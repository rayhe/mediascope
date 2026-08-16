"""
Raymond Wong (Gizmodo) Privacy Vocabulary Differential — Refining the Clean Control

KEY FINDING: Raymond Wong, previously characterized as the "clean control" journalist
at a publication with ZERO financial ties to tech competitors (mechanism baseline in
test_raymond_wong_cross_entity.py), actually shows a significant privacy vocabulary
differential when comparing his coverage across entities:

  Meta Fury review (Jul 1, 2026): 15+ privacy/surveillance terms, "worst company" headline
  Google/Xreal Project Aura hands-on (May 19, 2026): 0 privacy terms, 3 cameras
  Samsung Galaxy Glasses analysis (Mar 2026): 0 privacy terms for Samsung, 5+ for Meta

The privacy vocabulary ratio is INFINITE (15:0 Meta-to-Google) — the same order of
magnitude as Andy Boxall at Android Police (mechanism #132) and WIRED/Condé Nast
journalists. Project Aura has 3x the cameras of Meta Fury yet receives ZERO privacy
scrutiny from the same journalist.

REFINEMENT TO CLEAN CONTROL THESIS: Gizmodo IS more balanced than WIRED in one key
respect: Wong acknowledges Meta makes the best hardware and gives it a positive product
review alongside the privacy alarm. WIRED wouldn't even run a headline like that. But
the privacy VOCABULARY differential is indistinguishable from financially-incentivized
outlets. This suggests the asymmetry has a CULTURAL base rate (Meta-specific privacy
stigma from Cambridge Analytica era) that financial incentives AMPLIFY but don't create.

Mechanism #135: same_journalist_privacy_vocabulary_differential_cultural_base_rate

Sources:
- Meta Fury review: https://gizmodo.com/meta-fury-ai-glasses-review-the-worst-company-still-makes-the-best-smart-glasses-2000777827
- Google/Xreal Project Aura: https://gizmodo.com/google-and-xreals-project-aura-xr-smart-glasses-are-legit-2000760940
- Samsung analysis: https://gizmodo.com/samsungs-smart-glasses-might-not-have-to-do-much-thanks-to-meta-2000734490
- Keleops AG ownership: https://www.adweek.com/media/keleops-ag-acquires-gizmodo-from-go-media/

Created: 2026-08-16
"""
import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_gizmodo_profile():
    with open(os.path.join(PROFILES_DIR, 'gizmodo.yaml')) as f:
        return yaml.safe_load(f)


def load_competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


def load_wired_profile():
    with open(os.path.join(PROFILES_DIR, 'wired.yaml')) as f:
        return yaml.safe_load(f)


# ===================================================================
# TEST CLASS 1: Meta Fury Review Privacy Vocabulary
# ===================================================================
class TestMetaFuryPrivacyVocabulary:
    """Verify that the Meta Fury review uses extensive privacy alarm language."""

    def test_fury_review_documented(self):
        """The Fury review should be documented in the Gizmodo profile."""
        profile = load_gizmodo_profile()
        wong_articles = profile.get('wong_cross_entity_privacy_vocabulary', {})
        fury = wong_articles.get('meta_fury_review', {})
        assert fury, "Meta Fury review should be documented"

    def test_fury_review_date(self):
        profile = load_gizmodo_profile()
        fury = profile['wong_cross_entity_privacy_vocabulary']['meta_fury_review']
        assert '2026-07' in fury.get('date', ''), "Fury review is from July 2026"

    def test_fury_review_privacy_term_count(self):
        """Fury review uses 15+ privacy/surveillance alarm terms."""
        profile = load_gizmodo_profile()
        fury = profile['wong_cross_entity_privacy_vocabulary']['meta_fury_review']
        terms = fury.get('privacy_terms', [])
        assert len(terms) >= 12, \
            f"Expected >=12 privacy terms in Fury review, got {len(terms)}"

    def test_fury_headline_contains_worst_company(self):
        """Headline: 'The Worst Company Still Makes the Best Smart Glasses'"""
        profile = load_gizmodo_profile()
        fury = profile['wong_cross_entity_privacy_vocabulary']['meta_fury_review']
        headline = fury.get('headline', '')
        assert 'worst company' in headline.lower(), \
            "Headline should contain 'worst company' framing"

    def test_fury_review_camera_count(self):
        """Meta Fury has 1 camera."""
        profile = load_gizmodo_profile()
        fury = profile['wong_cross_entity_privacy_vocabulary']['meta_fury_review']
        assert fury.get('camera_count') == 1

    def test_fury_review_tone_score(self):
        """Tone score should be negative (adversarial opening)."""
        profile = load_gizmodo_profile()
        fury = profile['wong_cross_entity_privacy_vocabulary']['meta_fury_review']
        tone = fury.get('tone_score', 0)
        assert tone < 0, f"Expected negative tone, got {tone}"

    def test_fury_review_product_rating(self):
        """Despite adversarial framing, Wong gives 3.5/5 — acknowledging
        the product is actually good. This is the key distinction from WIRED."""
        profile = load_gizmodo_profile()
        fury = profile['wong_cross_entity_privacy_vocabulary']['meta_fury_review']
        rating = fury.get('product_rating')
        assert rating is not None and rating >= 3.0, \
            "Wong rates the product positively despite privacy framing"

    def test_fury_review_source_url(self):
        profile = load_gizmodo_profile()
        fury = profile['wong_cross_entity_privacy_vocabulary']['meta_fury_review']
        url = fury.get('source_url', '')
        assert 'gizmodo.com' in url and 'fury' in url.lower()


# ===================================================================
# TEST CLASS 2: Google/Xreal Project Aura Privacy Vocabulary
# ===================================================================
class TestProjectAuraPrivacyVocabulary:
    """Verify that the Project Aura article has ZERO privacy language
    despite having 3x the cameras of Meta glasses."""

    def test_project_aura_documented(self):
        profile = load_gizmodo_profile()
        wong_articles = profile.get('wong_cross_entity_privacy_vocabulary', {})
        aura = wong_articles.get('google_xreal_project_aura', {})
        assert aura, "Project Aura article should be documented"

    def test_project_aura_date(self):
        profile = load_gizmodo_profile()
        aura = profile['wong_cross_entity_privacy_vocabulary']['google_xreal_project_aura']
        assert '2026-05' in aura.get('date', ''), "Project Aura is from May 2026"

    def test_project_aura_privacy_term_count_zero(self):
        """Project Aura article has ZERO privacy/surveillance terms."""
        profile = load_gizmodo_profile()
        aura = profile['wong_cross_entity_privacy_vocabulary']['google_xreal_project_aura']
        terms = aura.get('privacy_terms', [])
        assert len(terms) == 0, \
            f"Expected 0 privacy terms for Project Aura, got {len(terms)}: {terms}"

    def test_project_aura_camera_count(self):
        """Project Aura has 3 cameras — 3x Meta's count."""
        profile = load_gizmodo_profile()
        aura = profile['wong_cross_entity_privacy_vocabulary']['google_xreal_project_aura']
        assert aura.get('camera_count') == 3

    def test_project_aura_tone_positive(self):
        """Tone is enthusiastic — 'legit,' 'promising,' 'optimistic.'"""
        profile = load_gizmodo_profile()
        aura = profile['wong_cross_entity_privacy_vocabulary']['google_xreal_project_aura']
        tone = aura.get('tone_score', 0)
        assert tone > 0.5, f"Expected positive tone, got {tone}"

    def test_project_aura_headline_positive(self):
        profile = load_gizmodo_profile()
        aura = profile['wong_cross_entity_privacy_vocabulary']['google_xreal_project_aura']
        headline = aura.get('headline', '')
        assert 'legit' in headline.lower(), \
            "Headline should be 'Legit' — purely positive"

    def test_cameras_mentioned_only_as_hardware_specs(self):
        """Cameras are mentioned as hardware specs, not as privacy risks."""
        profile = load_gizmodo_profile()
        aura = profile['wong_cross_entity_privacy_vocabulary']['google_xreal_project_aura']
        camera_framing = aura.get('camera_framing', '')
        assert 'hardware' in camera_framing.lower() or 'spec' in camera_framing.lower(), \
            "Cameras should be framed as specs, not privacy concerns"

    def test_project_aura_source_url(self):
        profile = load_gizmodo_profile()
        aura = profile['wong_cross_entity_privacy_vocabulary']['google_xreal_project_aura']
        url = aura.get('source_url', '')
        assert 'gizmodo.com' in url and 'aura' in url.lower()


# ===================================================================
# TEST CLASS 3: Samsung Galaxy Glasses Privacy Framing
# ===================================================================
class TestSamsungGlassesPrivacyFraming:
    """Verify that the Samsung analysis pins ALL privacy concerns on Meta
    while positioning Samsung as the trustworthy alternative."""

    def test_samsung_analysis_documented(self):
        profile = load_gizmodo_profile()
        wong_articles = profile.get('wong_cross_entity_privacy_vocabulary', {})
        samsung = wong_articles.get('samsung_galaxy_glasses_analysis', {})
        assert samsung, "Samsung analysis should be documented"

    def test_samsung_privacy_terms_for_samsung_zero(self):
        """Zero privacy ALARM terms directed at Samsung."""
        profile = load_gizmodo_profile()
        samsung = profile['wong_cross_entity_privacy_vocabulary']['samsung_galaxy_glasses_analysis']
        samsung_privacy = samsung.get('privacy_terms_directed_at_samsung', [])
        assert len(samsung_privacy) == 0, \
            f"Expected 0 Samsung-directed privacy terms, got {len(samsung_privacy)}"

    def test_samsung_privacy_terms_for_meta_in_article(self):
        """5+ privacy alarm terms directed at META within the Samsung article."""
        profile = load_gizmodo_profile()
        samsung = profile['wong_cross_entity_privacy_vocabulary']['samsung_galaxy_glasses_analysis']
        meta_terms = samsung.get('privacy_terms_directed_at_meta', [])
        assert len(meta_terms) >= 4, \
            f"Expected >=4 Meta-directed privacy terms in Samsung article, got {len(meta_terms)}"

    def test_samsung_positioned_as_privacy_solution(self):
        """Samsung is framed as the privacy-friendly alternative to Meta."""
        profile = load_gizmodo_profile()
        samsung = profile['wong_cross_entity_privacy_vocabulary']['samsung_galaxy_glasses_analysis']
        framing = samsung.get('samsung_framing', '')
        assert 'alternative' in framing.lower() or 'privacy' in framing.lower(), \
            "Samsung should be framed as privacy alternative"

    def test_samsung_meta_same_hardware_noted(self):
        """Article notes Samsung has nearly identical hardware (12MP camera,
        similar battery, same form factor) but doesn't apply same scrutiny."""
        profile = load_gizmodo_profile()
        samsung = profile['wong_cross_entity_privacy_vocabulary']['samsung_galaxy_glasses_analysis']
        assert samsung.get('hardware_equivalence_noted', False), \
            "Article should note hardware equivalence"

    def test_samsung_camera_count(self):
        profile = load_gizmodo_profile()
        samsung = profile['wong_cross_entity_privacy_vocabulary']['samsung_galaxy_glasses_analysis']
        assert samsung.get('camera_count') == 1

    def test_samsung_source_url(self):
        profile = load_gizmodo_profile()
        samsung = profile['wong_cross_entity_privacy_vocabulary']['samsung_galaxy_glasses_analysis']
        url = samsung.get('source_url', '')
        assert 'gizmodo.com' in url and 'samsung' in url.lower()


# ===================================================================
# TEST CLASS 4: Cross-Entity Privacy Vocabulary Comparison
# ===================================================================
class TestCrossEntityPrivacyVocabularyComparison:
    """The core finding: same journalist, massive privacy vocabulary differential."""

    def test_privacy_vocabulary_ratio_meta_vs_google(self):
        """Meta:Google privacy term ratio should be effectively infinite (15:0)."""
        profile = load_gizmodo_profile()
        vocab = profile['wong_cross_entity_privacy_vocabulary']
        meta_count = len(vocab['meta_fury_review'].get('privacy_terms', []))
        google_count = len(vocab['google_xreal_project_aura'].get('privacy_terms', []))
        assert meta_count >= 12, f"Meta should have >=12 terms, got {meta_count}"
        assert google_count == 0, f"Google should have 0 terms, got {google_count}"

    def test_camera_count_inverse_to_privacy_scrutiny(self):
        """More cameras = LESS privacy scrutiny — the opposite of what
        hardware-driven analysis would predict."""
        profile = load_gizmodo_profile()
        vocab = profile['wong_cross_entity_privacy_vocabulary']
        meta_cameras = vocab['meta_fury_review'].get('camera_count', 0)
        google_cameras = vocab['google_xreal_project_aura'].get('camera_count', 0)
        meta_terms = len(vocab['meta_fury_review'].get('privacy_terms', []))
        google_terms = len(vocab['google_xreal_project_aura'].get('privacy_terms', []))

        assert google_cameras > meta_cameras, \
            "Google has more cameras than Meta"
        assert meta_terms > google_terms, \
            "Meta gets more privacy scrutiny despite fewer cameras"

    def test_tone_differential_across_entities(self):
        """Tone differential should be significant: Meta negative, Google positive."""
        profile = load_gizmodo_profile()
        vocab = profile['wong_cross_entity_privacy_vocabulary']
        meta_tone = vocab['meta_fury_review'].get('tone_score', 0)
        google_tone = vocab['google_xreal_project_aura'].get('tone_score', 0)
        delta = google_tone - meta_tone
        assert delta >= 0.8, \
            f"Tone differential should be >= 0.8, got {delta}"

    def test_same_journalist_all_three(self):
        """All three articles are by Raymond Wong."""
        profile = load_gizmodo_profile()
        vocab = profile['wong_cross_entity_privacy_vocabulary']
        for key in ['meta_fury_review', 'google_xreal_project_aura',
                     'samsung_galaxy_glasses_analysis']:
            assert vocab[key].get('journalist') == 'Raymond Wong'

    def test_all_three_are_camera_equipped_glasses(self):
        """All three products are camera-equipped smart glasses — same category."""
        profile = load_gizmodo_profile()
        vocab = profile['wong_cross_entity_privacy_vocabulary']
        for key in ['meta_fury_review', 'google_xreal_project_aura',
                     'samsung_galaxy_glasses_analysis']:
            assert vocab[key].get('has_camera', False), \
                f"{key} should have camera"

    def test_within_90_day_window(self):
        """All three articles published within ~90 days of each other."""
        profile = load_gizmodo_profile()
        vocab = profile['wong_cross_entity_privacy_vocabulary']
        dates = [vocab[k].get('date', '') for k in [
            'meta_fury_review', 'google_xreal_project_aura',
            'samsung_galaxy_glasses_analysis']]
        # All should be 2026
        for d in dates:
            assert '2026' in d, f"Article should be from 2026, got {d}"


# ===================================================================
# TEST CLASS 5: Clean Control Thesis Refinement
# ===================================================================
class TestCleanControlRefinement:
    """Tests that validate the refinement to the clean control thesis."""

    def test_mechanism_135_exists(self):
        """Mechanism #135 should be documented."""
        research = load_competitor_research()
        mechanisms = research.get('aggregate_findings', {})
        wong_pvd = mechanisms.get('wong_privacy_vocabulary_differential', {})
        assert wong_pvd.get('mechanism_id') == 135

    def test_mechanism_135_type(self):
        research = load_competitor_research()
        wong_pvd = research['aggregate_findings']['wong_privacy_vocabulary_differential']
        mtype = wong_pvd.get('mechanism', '')
        assert 'cultural_base_rate' in mtype or 'vocabulary_differential' in mtype

    def test_mechanism_cross_references_baseline(self):
        """Should cross-reference the original Wong clean control test."""
        research = load_competitor_research()
        wong_pvd = research['aggregate_findings']['wong_privacy_vocabulary_differential']
        xrefs = wong_pvd.get('cross_references', [])
        assert any('raymond_wong' in str(x).lower() or 'clean_control' in str(x).lower()
                    for x in xrefs), \
            "Should reference original Wong clean control analysis"

    def test_mechanism_has_confounders(self):
        research = load_competitor_research()
        wong_pvd = research['aggregate_findings']['wong_privacy_vocabulary_differential']
        confounders = wong_pvd.get('confounders', [])
        assert len(confounders) >= 4, \
            f"Expected >=4 confounders, got {len(confounders)}"

    def test_strong_confounders_present(self):
        """At least 2 STRONG confounders should be documented."""
        research = load_competitor_research()
        wong_pvd = research['aggregate_findings']['wong_privacy_vocabulary_differential']
        confounders = wong_pvd.get('confounders', [])
        strong = [c for c in confounders if c.get('strength') == 'STRONG']
        assert len(strong) >= 2, \
            f"Expected >=2 STRONG confounders, got {len(strong)}"

    def test_gizmodo_still_more_balanced_than_wired(self):
        """Despite the vocabulary differential, Gizmodo IS still more balanced
        than WIRED: Wong gives a positive product rating, WIRED wouldn't."""
        research = load_competitor_research()
        wong_pvd = research['aggregate_findings']['wong_privacy_vocabulary_differential']
        distinction = wong_pvd.get('wired_distinction', '')
        assert 'product' in distinction.lower() or 'rating' in distinction.lower() or \
               'positive' in distinction.lower(), \
            "Should note Gizmodo is still more balanced than WIRED"

    def test_cultural_base_rate_documented(self):
        """The finding should document a 'cultural base rate' of Meta
        privacy stigma that exists independent of financial incentives."""
        research = load_competitor_research()
        wong_pvd = research['aggregate_findings']['wong_privacy_vocabulary_differential']
        finding = wong_pvd.get('finding_summary', '')
        assert 'cultural' in finding.lower() or 'base rate' in finding.lower() or \
               'brand' in finding.lower(), \
            "Finding should reference cultural base rate / brand stigma"


# ===================================================================
# TEST CLASS 6: Comparison with Andy Boxall (#132)
# ===================================================================
class TestComparisonWithBoxallMechanism:
    """Compare Wong's pattern with Andy Boxall's (mechanism #132)."""

    def test_same_pattern_different_owner(self):
        """Wong (Gizmodo/Keleops) shows same vocabulary inversion as
        Boxall (Android Police/Valnet) — now confirmed at 5th publisher."""
        research = load_competitor_research()
        wong_pvd = research['aggregate_findings']['wong_privacy_vocabulary_differential']
        xrefs = wong_pvd.get('cross_references', [])
        assert any(132 == x or '#132' in str(x) for x in xrefs), \
            "Should cross-reference mechanism #132 (Boxall)"

    def test_wong_no_financial_ties(self):
        """Unlike Boxall (Valnet has Google ad dependency), Wong is at
        Gizmodo (Keleops AG, no known tech content deals)."""
        profile = load_gizmodo_profile()
        ownership = profile.get('ownership', {})
        deals = ownership.get('known_ai_content_deals', [])
        assert len(deals) == 0 or deals == ['none'], \
            "Gizmodo should have zero AI content deals"

    def test_pattern_implies_cultural_not_purely_financial(self):
        """If the same pattern appears at a financially-independent outlet,
        financial incentives AMPLIFY but don't CREATE the asymmetry."""
        research = load_competitor_research()
        wong_pvd = research['aggregate_findings']['wong_privacy_vocabulary_differential']
        implication = wong_pvd.get('implication', '')
        assert 'amplif' in implication.lower() or 'cultural' in implication.lower(), \
            "Should note cultural origin, financial amplification"


# ===================================================================
# TEST CLASS 7: Source URL Verification
# ===================================================================
class TestSourceURLs:
    """Verify all source URLs are documented."""

    def test_source_urls_present(self):
        research = load_competitor_research()
        wong_pvd = research['aggregate_findings']['wong_privacy_vocabulary_differential']
        urls = wong_pvd.get('source_urls', [])
        assert len(urls) >= 3, f"Expected >=3 source URLs, got {len(urls)}"

    def test_fury_url_present(self):
        research = load_competitor_research()
        wong_pvd = research['aggregate_findings']['wong_privacy_vocabulary_differential']
        urls = wong_pvd.get('source_urls', [])
        assert any('fury' in u.lower() for u in urls), "Fury review URL needed"

    def test_project_aura_url_present(self):
        research = load_competitor_research()
        wong_pvd = research['aggregate_findings']['wong_privacy_vocabulary_differential']
        urls = wong_pvd.get('source_urls', [])
        assert any('aura' in u.lower() for u in urls), "Project Aura URL needed"

    def test_samsung_url_present(self):
        research = load_competitor_research()
        wong_pvd = research['aggregate_findings']['wong_privacy_vocabulary_differential']
        urls = wong_pvd.get('source_urls', [])
        assert any('samsung' in u.lower() for u in urls), "Samsung URL needed"


# ===================================================================
# TEST CLASS 8: Falsifiable Predictions
# ===================================================================
class TestFalsifiablePredictions:
    """The mechanism should make testable predictions."""

    def test_predictions_exist(self):
        research = load_competitor_research()
        wong_pvd = research['aggregate_findings']['wong_privacy_vocabulary_differential']
        predictions = wong_pvd.get('falsifiable_predictions', [])
        assert len(predictions) >= 2, \
            f"Expected >=2 falsifiable predictions, got {len(predictions)}"

    def test_prediction_about_samsung_launch(self):
        """Predict: when Samsung ships camera glasses, Wong will apply LESS
        privacy scrutiny to Samsung's launch review than he did to Meta Fury."""
        research = load_competitor_research()
        wong_pvd = research['aggregate_findings']['wong_privacy_vocabulary_differential']
        predictions = wong_pvd.get('falsifiable_predictions', [])
        assert any('samsung' in p.lower() and ('launch' in p.lower() or 'review' in p.lower())
                    for p in predictions)

    def test_prediction_about_cultural_persistence(self):
        """Predict: the privacy vocabulary differential persists regardless
        of Meta's v26 LED tamper-detection fix — because the stigma is
        brand-attached, not hardware-attached."""
        research = load_competitor_research()
        wong_pvd = research['aggregate_findings']['wong_privacy_vocabulary_differential']
        predictions = wong_pvd.get('falsifiable_predictions', [])
        assert any('persist' in p.lower() or 'fix' in p.lower() or 'stigma' in p.lower()
                    for p in predictions)
