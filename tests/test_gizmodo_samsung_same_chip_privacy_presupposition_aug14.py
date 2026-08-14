"""
Test Mechanism #95: Gizmodo Same-Journalist Same-Chip Samsung Privacy Presupposition —
Clean Control Entity-Specific Coverage Selectivity

Type A: Competitor Coverage Deep Dive (Aug 14, 2026 04:00 PT)

KEY FINDING: Raymond Wong at Gizmodo — the dataset's clean control publication
(zero financial ties to any tech company, owned by Keleops AG) — demonstrates
entity-specific privacy vocabulary selectivity when covering Samsung Galaxy
Glasses vs Meta Ray-Ban glasses, despite IDENTICAL hardware.

Samsung Galaxy Glasses use the SAME Snapdragon AR1 Gen 1 chip as Meta Ray-Ban,
the same 12MP camera resolution, the same LED indicator, the same form factor.
Wong explicitly acknowledges the hardware parity in his Apr 28 2026 article
("Leak Suggests Samsung Cribbed Meta's Smart Glasses Design") but adds
"except maybe not violate your privacy as easily" — presupposing Samsung as
privacy-superior WITHOUT evidence. No Samsung privacy investigation exists;
the product hadn't shipped.

Within-article asymmetry (Jul 30, 2026): Meta gets 5 substantive privacy-scandal
paragraphs; Samsung gets 1 sentence as positive market entry. Same journalist,
same article.

Samsung coverage:
  Apr 28: "except maybe not violate your privacy as easily" — presupposition, no evidence
  Jul 22: Samsung hands-on, 1 paragraph on privacy, Samsung exec knife analogy accepted
  Jul 30: Within-article asymmetry — Meta = 5 privacy paragraphs, Samsung = 1 growth sentence

Meta coverage (same journalist, same period):
  Mar 2026: "You're Being Watched, Too" — adversarial headline, surveillance vocabulary
  Jun 14: "Can Smart Glasses Ever Be Privacy-Friendly?" — Meta = problem, alternatives = solutions
  Jul 30: same article — Meta paragraphs use surveillance, pile up, deafening language

HARDWARE PARITY:
  Samsung: Snapdragon AR1 Gen 1, 12MP camera, LED indicator
  Meta:    Snapdragon AR1 Gen 1, 12MP camera, LED indicator
  SAME CHIP. SAME CAMERA. SAME PRIVACY PROFILE.

SIGNIFICANCE: Since Gizmodo has ZERO financial ties to Samsung, Google, Meta,
or any tech company, this establishes that Samsung-favorable privacy framing
operates at the CULTURAL level. Financial relationships at WIRED, FT, and NYT
AMPLIFY this pre-existing cultural coding but did not create it. This extends
#74 (Snap Specs niche $2,195) to Samsung (mass-market $299-$499), establishing
robustness across competitor categories.

Sources:
  Samsung articles:
  - https://gizmodo.com/leak-suggests-samsung-cribbed-metas-smart-glasses-design-2000751362
  - https://gizmodo.com/samsung-let-me-touch-its-warby-parker-x-gentle-monster-smart-glasses-but-not-wear-them-2000788835
  - https://gizmodo.com/smart-glasses-are-a-hit-even-as-privacy-concerns-pile-up-2000792911
  Meta articles (same journalist):
  - https://gizmodo.com/dear-meta-smart-glasses-wearers-youre-being-watched-too-2000740207
  - https://gizmodo.com/can-smart-glasses-ever-be-privacy-friendly-these-companies-think-so-2000771803
  - https://gizmodo.com/smart-glasses-are-a-hit-even-as-privacy-concerns-pile-up-2000792911
"""

import yaml
import os
import pytest

PROFILE_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'gizmodo.yaml'
)

RESEARCH_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
)

ENTITIES_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'competitor-entities.yaml'
)


@pytest.fixture(scope='module')
def gizmodo_profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research_data():
    with open(RESEARCH_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def entities_data():
    with open(ENTITIES_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def same_chip_section(gizmodo_profile):
    cross = gizmodo_profile.get('cross_entity_coverage', {})
    samsung_sec = cross.get('samsung', {})
    section = samsung_sec.get('gizmodo_same_chip_privacy_presupposition')
    assert section is not None, (
        "Missing samsung.gizmodo_same_chip_privacy_presupposition in gizmodo.yaml cross_entity_coverage"
    )
    return section


@pytest.fixture(scope='module')
def mechanism_95(research_data):
    cpf = research_data.get('cross_publication_findings', {})
    section = cpf.get('gizmodo_samsung_same_chip_privacy_presupposition')
    assert section is not None, (
        "Missing gizmodo_samsung_same_chip_privacy_presupposition in "
        "competitor-coverage-research.yaml cross_publication_findings"
    )
    return section


@pytest.fixture(scope='module')
def entities_samsung(entities_data):
    entities = entities_data.get('entities', {})
    samsung = entities.get('samsung', {})
    section = samsung.get('gizmodo_same_chip_privacy_presupposition')
    assert section is not None, (
        "Missing entities.samsung.gizmodo_same_chip_privacy_presupposition in competitor-entities.yaml"
    )
    return section


# ── Class 1: Hardware Parity ────────────────────────────────────────


class TestHardwareParity:
    """Verify identical hardware specs are documented for both products."""

    def test_samsung_chip(self, same_chip_section):
        hw = same_chip_section.get('samsung_hardware', {})
        assert 'AR1 Gen 1' in hw.get('chip', '')

    def test_meta_chip(self, same_chip_section):
        hw = same_chip_section.get('meta_hardware', {})
        assert 'AR1 Gen 1' in hw.get('chip', '')

    def test_same_chip(self, same_chip_section):
        samsung_hw = same_chip_section.get('samsung_hardware', {})
        meta_hw = same_chip_section.get('meta_hardware', {})
        assert samsung_hw.get('chip') == meta_hw.get('chip')

    def test_samsung_camera_resolution(self, same_chip_section):
        hw = same_chip_section.get('samsung_hardware', {})
        assert hw.get('camera_resolution_mp') == 12

    def test_meta_camera_resolution(self, same_chip_section):
        hw = same_chip_section.get('meta_hardware', {})
        assert hw.get('camera_resolution_mp') == 12

    def test_same_camera_resolution(self, same_chip_section):
        samsung_hw = same_chip_section.get('samsung_hardware', {})
        meta_hw = same_chip_section.get('meta_hardware', {})
        assert samsung_hw.get('camera_resolution_mp') == meta_hw.get('camera_resolution_mp')

    def test_samsung_led_indicator(self, same_chip_section):
        hw = same_chip_section.get('samsung_hardware', {})
        assert hw.get('has_led_recording_indicator') is True

    def test_meta_led_indicator(self, same_chip_section):
        hw = same_chip_section.get('meta_hardware', {})
        assert hw.get('has_led_recording_indicator') is True

    def test_hardware_privacy_parity(self, same_chip_section):
        assert same_chip_section.get('hardware_privacy_parity') is True


# ── Class 2: Surveillance Vocabulary Asymmetry ──────────────────────


class TestSurveillanceVocabularyAsymmetry:
    """Samsung articles have 0 surveillance words; Meta articles have many."""

    def test_samsung_articles_exist(self, same_chip_section):
        articles = same_chip_section.get('samsung_articles', [])
        assert len(articles) >= 3

    def test_all_samsung_articles_zero_surveillance(self, same_chip_section):
        articles = same_chip_section.get('samsung_articles', [])
        for art in articles:
            assert art.get('surveillance_vocabulary_count', -1) == 0, (
                f"Samsung article '{art.get('title', '?')}' has non-zero surveillance vocabulary"
            )

    def test_meta_articles_exist(self, same_chip_section):
        articles = same_chip_section.get('meta_articles', [])
        assert len(articles) >= 2

    def test_meta_articles_have_surveillance_vocabulary(self, same_chip_section):
        articles = same_chip_section.get('meta_articles', [])
        total = sum(art.get('surveillance_vocabulary_count', 0) for art in articles)
        assert total >= 3, "Meta articles should have at least 3 total surveillance vocabulary instances"

    def test_samsung_aggregate_surveillance_zero(self, same_chip_section):
        articles = same_chip_section.get('samsung_articles', [])
        total = sum(art.get('surveillance_vocabulary_count', 0) for art in articles)
        assert total == 0


# ── Class 3: Within-Article Entity Delta ────────────────────────────


class TestWithinArticleEntityDelta:
    """Jul 30 article: Meta gets 5 privacy paragraphs, Samsung gets 1 sentence."""

    def test_within_article_section_exists(self, same_chip_section):
        within = same_chip_section.get('within_article_asymmetry', {})
        assert within, "Missing within_article_asymmetry section"

    def test_within_article_date(self, same_chip_section):
        within = same_chip_section.get('within_article_asymmetry', {})
        assert '2026-07-30' in within.get('date', '')

    def test_within_article_url(self, same_chip_section):
        within = same_chip_section.get('within_article_asymmetry', {})
        url = within.get('url', '')
        assert 'gizmodo.com' in url
        assert 'pile-up' in url or 'privacy-concerns' in url or '2000792911' in url

    def test_meta_privacy_paragraphs(self, same_chip_section):
        within = same_chip_section.get('within_article_asymmetry', {})
        assert within.get('meta_privacy_paragraphs', 0) >= 5

    def test_samsung_mention_type(self, same_chip_section):
        within = same_chip_section.get('within_article_asymmetry', {})
        samsung_type = within.get('samsung_mention_type', '')
        assert 'positive' in samsung_type.lower() or 'growth' in samsung_type.lower() or 'sentence' in samsung_type.lower()

    def test_within_article_entity_tone_delta(self, same_chip_section):
        within = same_chip_section.get('within_article_asymmetry', {})
        delta = within.get('entity_tone_delta', 0)
        assert delta >= 0.50, f"Within-article entity tone delta {delta} should be >= 0.50"

    def test_meta_tone_adversarial(self, same_chip_section):
        within = same_chip_section.get('within_article_asymmetry', {})
        assert within.get('meta_tone', 0) <= -0.50

    def test_samsung_tone_neutral(self, same_chip_section):
        within = same_chip_section.get('within_article_asymmetry', {})
        assert within.get('samsung_tone', -1) >= -0.10


# ── Class 4: Pre-Emptive Privacy Pass ──────────────────────────────


class TestPreEmptivePrivacyPass:
    """Apr 28 'except maybe not violate your privacy as easily' — editorial presupposition."""

    def test_presupposition_section_exists(self, same_chip_section):
        section = same_chip_section.get('pre_emptive_privacy_pass', {})
        assert section, "Missing pre_emptive_privacy_pass section"

    def test_presupposition_date(self, same_chip_section):
        section = same_chip_section.get('pre_emptive_privacy_pass', {})
        assert '2026-04-28' in section.get('date', '') or '2026-04-27' in section.get('date', '')

    def test_presupposition_quote(self, same_chip_section):
        section = same_chip_section.get('pre_emptive_privacy_pass', {})
        quote = section.get('editorial_quote', '')
        assert 'except maybe not violate your privacy' in quote.lower() or 'privacy as easily' in quote.lower()

    def test_presupposition_type(self, same_chip_section):
        section = same_chip_section.get('pre_emptive_privacy_pass', {})
        ptype = section.get('presupposition_type', '')
        assert 'editorial' in ptype.lower() or 'assumption' in ptype.lower() or 'presupposition' in ptype.lower()

    def test_evidence_basis_none(self, same_chip_section):
        section = same_chip_section.get('pre_emptive_privacy_pass', {})
        evidence = section.get('evidence_basis', '')
        assert 'none' in evidence.lower() or 'no evidence' in evidence.lower() or 'unsubstantiated' in evidence.lower()


# ── Class 5: Journalist Consistency ─────────────────────────────────


class TestJournalistConsistency:
    """Same journalist (Raymond Wong), different treatment by entity."""

    def test_journalist_name(self, same_chip_section):
        assert same_chip_section.get('journalist') == 'Raymond Wong'

    def test_same_journalist_both_entities(self, same_chip_section):
        samsung_arts = same_chip_section.get('samsung_articles', [])
        meta_arts = same_chip_section.get('meta_articles', [])
        samsung_authors = {art.get('author', '') for art in samsung_arts}
        meta_authors = {art.get('author', '') for art in meta_arts}
        assert 'Raymond Wong' in samsung_authors
        assert 'Raymond Wong' in meta_authors

    def test_samsung_aggregate_tone(self, same_chip_section):
        tone = same_chip_section.get('samsung_aggregate_tone', 1)
        # Neutral to slightly negative — NOT adversarial
        assert tone >= -0.15

    def test_meta_aggregate_tone(self, same_chip_section):
        tone = same_chip_section.get('meta_aggregate_tone', 0)
        # Adversarial
        assert tone <= -0.40

    def test_tone_delta_significant(self, same_chip_section):
        samsung_tone = same_chip_section.get('samsung_aggregate_tone', 0)
        meta_tone = same_chip_section.get('meta_aggregate_tone', 0)
        delta = samsung_tone - meta_tone
        assert delta >= 0.30, f"Tone delta {delta} should be >= 0.30"


# ── Class 6: Samsung Exec Framing Adoption ─────────────────────────


class TestSamsungExecFramingAdoption:
    """Journalist accepts Samsung executive's knife analogy without pushback."""

    def test_exec_framing_section_exists(self, same_chip_section):
        section = same_chip_section.get('samsung_exec_framing_adoption', {})
        assert section, "Missing samsung_exec_framing_adoption section"

    def test_exec_analogy_documented(self, same_chip_section):
        section = same_chip_section.get('samsung_exec_framing_adoption', {})
        analogy = section.get('executive_analogy', '')
        assert 'knife' in analogy.lower()

    def test_journalist_pushback(self, same_chip_section):
        section = same_chip_section.get('samsung_exec_framing_adoption', {})
        pushback = section.get('journalist_pushback', '')
        assert pushback.lower() in ('none', 'zero', 'no pushback', 'absent')

    def test_article_url(self, same_chip_section):
        section = same_chip_section.get('samsung_exec_framing_adoption', {})
        url = section.get('article_url', '')
        assert 'gizmodo.com' in url


# ── Class 7: Confounding Factors ────────────────────────────────────


class TestConfoundingFactors:
    """Verify >=5 confounding factors with >=1 STRONG and >=2 strength levels."""

    def test_at_least_five_confounds(self, same_chip_section):
        factors = same_chip_section.get('confounding_factors', [])
        assert len(factors) >= 5

    def test_at_least_one_strong(self, same_chip_section):
        factors = same_chip_section.get('confounding_factors', [])
        strong_count = sum(1 for f in factors if f.get('strength', '').upper() == 'STRONG')
        assert strong_count >= 1

    def test_at_least_two_strength_levels(self, same_chip_section):
        factors = same_chip_section.get('confounding_factors', [])
        levels = {f.get('strength', '').upper() for f in factors}
        assert len(levels) >= 2, f"Only {levels} strength levels found, need >=2"

    def test_pre_launch_confound(self, same_chip_section):
        factors = same_chip_section.get('confounding_factors', [])
        factor_text = ' '.join(f.get('factor', '') for f in factors).lower()
        assert 'pre-launch' in factor_text or 'not shipped' in factor_text or 'hadn\'t shipped' in factor_text or 'deployed' in factor_text

    def test_cambridge_analytica_confound(self, same_chip_section):
        factors = same_chip_section.get('confounding_factors', [])
        factor_text = ' '.join(f.get('factor', '') for f in factors).lower()
        assert 'cambridge analytica' in factor_text or 'privacy scandal' in factor_text or 'documented history' in factor_text

    def test_installed_base_confound(self, same_chip_section):
        factors = same_chip_section.get('confounding_factors', [])
        factor_text = ' '.join(f.get('factor', '') for f in factors).lower()
        assert 'installed base' in factor_text or '7m' in factor_text or 'million' in factor_text


# ── Class 8: Testable Predictions ───────────────────────────────────


class TestTestablePredictions:
    """Verify >=4 testable predictions."""

    def test_at_least_four_predictions(self, same_chip_section):
        preds = same_chip_section.get('testable_predictions', [])
        assert len(preds) >= 4

    def test_predictions_are_specific(self, same_chip_section):
        preds = same_chip_section.get('testable_predictions', [])
        for pred in preds:
            pred_text = pred if isinstance(pred, str) else pred.get('prediction', '')
            assert len(pred_text) > 30, f"Prediction too short: {pred_text}"

    def test_shipping_prediction(self, same_chip_section):
        """Should predict behavior when Samsung glasses actually ship."""
        preds = same_chip_section.get('testable_predictions', [])
        pred_text = ' '.join(
            p if isinstance(p, str) else p.get('prediction', '') for p in preds
        ).lower()
        assert 'ship' in pred_text or 'launch' in pred_text or 'fall 2026' in pred_text

    def test_gemini_vision_prediction(self, same_chip_section):
        """Should predict framing of Gemini camera vision features."""
        preds = same_chip_section.get('testable_predictions', [])
        pred_text = ' '.join(
            p if isinstance(p, str) else p.get('prediction', '') for p in preds
        ).lower()
        assert 'gemini' in pred_text or 'ai' in pred_text or 'vision' in pred_text


# ── Class 9: Clean Control Significance ─────────────────────────────


class TestCleanControlSignificance:
    """Extends #74 from niche Snap to mass-market Samsung at clean control pub."""

    def test_mechanism_id_95(self, same_chip_section):
        assert same_chip_section.get('mechanism_id') == 95

    def test_gizmodo_zero_financial_ties(self, same_chip_section):
        sig = same_chip_section.get('clean_control_significance', {})
        assert sig.get('gizmodo_financial_ties_to_samsung') in ('none', 'zero', None) or \
            'none' in str(sig.get('gizmodo_financial_ties_to_samsung', '')).lower()

    def test_gizmodo_zero_financial_ties_to_meta(self, same_chip_section):
        sig = same_chip_section.get('clean_control_significance', {})
        assert sig.get('gizmodo_financial_ties_to_meta') in ('none', 'zero', None) or \
            'none' in str(sig.get('gizmodo_financial_ties_to_meta', '')).lower()

    def test_extends_mechanism_74(self, same_chip_section):
        sig = same_chip_section.get('clean_control_significance', {})
        related = sig.get('extends_mechanism', [])
        if isinstance(related, list):
            assert 74 in related
        else:
            assert related == 74

    def test_extends_from_niche_to_mass_market(self, same_chip_section):
        sig = same_chip_section.get('clean_control_significance', {})
        desc = sig.get('extension_description', '')
        assert 'mass' in desc.lower() or 'market' in desc.lower() or '$299' in desc or 'direct competitor' in desc.lower()

    def test_cultural_level_mechanism(self, same_chip_section):
        sig = same_chip_section.get('clean_control_significance', {})
        mechanism = sig.get('mechanism_isolated', '')
        assert 'cultural' in mechanism.lower()

    def test_cross_references(self, same_chip_section):
        refs = same_chip_section.get('cross_references', [])
        ref_ids = []
        for r in refs:
            if isinstance(r, dict):
                ref_ids.append(r.get('mechanism_id', 0))
            elif isinstance(r, int):
                ref_ids.append(r)
            elif isinstance(r, str):
                # Extract numbers from strings like "#74 — ..."
                import re
                nums = re.findall(r'#(\d+)', r)
                ref_ids.extend(int(n) for n in nums)
        assert 74 in ref_ids, "Must cross-reference mechanism #74 (Snap Specs)"
        assert 31 in ref_ids or 89 in ref_ids or 93 in ref_ids, \
            "Must cross-reference at least one of #31, #89, or #93"

    def test_has_finding_summary(self, same_chip_section):
        summary = same_chip_section.get('finding_summary', '')
        assert len(summary) >= 100

    def test_has_date_analyzed(self, same_chip_section):
        assert '2026-08-14' in same_chip_section.get('date_analyzed', '')

    def test_has_source_urls(self, same_chip_section):
        urls = same_chip_section.get('source_urls', [])
        assert len(urls) >= 6, f"Need >= 6 source URLs (3 Samsung + 3 Meta), got {len(urls)}"


# ── Class 10: Mechanism #95 in Research File ────────────────────────


class TestMechanism95InResearch:
    """Verify mechanism documented in competitor-coverage-research.yaml."""

    def test_mechanism_id(self, mechanism_95):
        assert mechanism_95.get('mechanism_id') == 95

    def test_publication(self, mechanism_95):
        pub = mechanism_95.get('publication', '')
        assert 'Gizmodo' in pub

    def test_journalist(self, mechanism_95):
        assert mechanism_95.get('journalist') == 'Raymond Wong'

    def test_finding_summary_length(self, mechanism_95):
        summary = mechanism_95.get('finding_summary', '')
        assert len(summary) >= 100

    def test_has_source_urls(self, mechanism_95):
        urls = mechanism_95.get('source_urls', [])
        assert len(urls) >= 6

    def test_has_test_file(self, mechanism_95):
        tf = mechanism_95.get('test_file', '')
        assert 'gizmodo_samsung_same_chip_privacy_presupposition_aug14' in tf

    def test_has_confounding_factors(self, mechanism_95):
        factors = mechanism_95.get('confounding_factors', [])
        assert len(factors) >= 5

    def test_has_testable_predictions(self, mechanism_95):
        preds = mechanism_95.get('testable_predictions', [])
        assert len(preds) >= 4

    def test_cross_references(self, mechanism_95):
        refs = mechanism_95.get('cross_references', [])
        assert len(refs) >= 3

    def test_date_added(self, mechanism_95):
        assert '2026-08-14' in mechanism_95.get('date_added', '')


# ── Class 11: Competitor Entities Registration ──────────────────────


class TestCompetitorEntitiesRegistration:
    """Verify mechanism registered in competitor-entities.yaml under samsung."""

    def test_mechanism_id_in_entities(self, entities_samsung):
        assert entities_samsung.get('mechanism_id') == 95

    def test_has_source_urls(self, entities_samsung):
        urls = entities_samsung.get('source_urls', [])
        assert len(urls) >= 3

    def test_has_related_mechanisms(self, entities_samsung):
        related = entities_samsung.get('related_mechanisms', [])
        assert len(related) >= 3
        assert 74 in related
