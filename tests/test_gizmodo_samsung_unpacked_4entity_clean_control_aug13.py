"""
Gizmodo Samsung Galaxy Unpacked — 4-Entity Clean Control Privacy Vocabulary Comparison

Type A: Competitor Coverage Deep Dive (Aug 13, 2026 06:00 PT)
Mechanism #80: 4-Entity Clean Control Privacy Vocabulary Comparison

Extends Mechanism #74 (Snap Specs) to Samsung, completing a 4-entity comparison at
Gizmodo -- the only publication in the MediaScope dataset with ZERO financial ties to
any tech company (owned by Keleops AG, Luxembourg).

All four entities make camera-equipped smart glasses with functionally identical
privacy-relevant hardware (cameras, AI processing, LED indicators):

| Entity   | Tone  | Surveillance Vocab | Key Framing                                     |
|----------|-------|--------------------|------------------------------------------------|
| Meta     | -0.75 | 5+ instances       | "You're Being Watched," "surveillance state"    |
| Google   | +0.4  | 0 instances        | "Legit," aspirational product review            |
| Snap     | -0.10 | 0 instances        | "cameras that enable spatial experiences"        |
| Samsung  | +0.2  | 0 instances        | "very light," build quality, ecosystem           |

Samsung's glasses use the SAME Snapdragon AR1 Gen 1 chip as Meta's, have a 12MP camera
(same as Meta), LED anti-tamper privacy indicator (same as Meta), and Google Gemini AI
visual processing. The hardware is functionally identical for privacy purposes.

Since Gizmodo has zero financial ties to ANY entity, this 4-entity comparison isolates
CULTURAL NARRATIVE CODING as the primary mechanism (~70% of asymmetry), with financial
incentives at other publications as an amplifier (~30%).

6 confounding factors (2 STRONG, 2 MODERATE, 2 WEAK).
4 testable predictions.
5 cross-references (#74, #6, #76, #77, Google I/O Camera Paradox).
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


@pytest.fixture(scope='module')
def gizmodo_profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research_data():
    with open(RESEARCH_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def samsung_section(gizmodo_profile):
    cross = gizmodo_profile.get('cross_entity_coverage', {})
    section = cross.get('samsung', {}).get('samsung_unpacked_4entity_clean_control')
    assert section is not None, (
        "Missing samsung.samsung_unpacked_4entity_clean_control in gizmodo.yaml cross_entity_coverage"
    )
    return section


@pytest.fixture(scope='module')
def mechanism_80(research_data):
    findings = research_data.get('aggregate_findings', {})
    section = findings.get('gizmodo_samsung_unpacked_4entity_clean_control')
    assert section is not None, (
        "Missing gizmodo_samsung_unpacked_4entity_clean_control in "
        "competitor-coverage-research.yaml aggregate_findings"
    )
    return section


# -- Class 1: Section Structure ------------------------------------------------


class TestSectionStructure:
    """Verify the Samsung Unpacked 4-entity section has all required fields."""

    def test_section_exists(self, samsung_section):
        assert samsung_section is not None

    def test_has_mechanism_id(self, samsung_section):
        assert samsung_section.get('mechanism_id') == 80

    def test_has_date_analyzed(self, samsung_section):
        assert '2026-08-13' in samsung_section.get('date_analyzed', '')

    def test_has_finding_summary(self, samsung_section):
        summary = samsung_section.get('finding_summary', '')
        assert len(summary) > 100

    def test_has_finding_title(self, samsung_section):
        title = samsung_section.get('finding', '')
        assert '4-entity' in title.lower() or '4 entity' in title.lower() or 'clean control' in title.lower()

    def test_has_confounding_factors(self, samsung_section):
        factors = samsung_section.get('confounding_factors', [])
        assert len(factors) >= 6

    def test_has_testable_predictions(self, samsung_section):
        preds = samsung_section.get('testable_predictions', [])
        assert len(preds) >= 4


# -- Class 2: Samsung Articles ------------------------------------------------


class TestSamsungArticles:
    """Verify 4 Samsung articles are documented with correct metadata."""

    def test_samsung_articles_exist(self, samsung_section):
        articles = samsung_section.get('samsung_articles', [])
        assert len(articles) >= 4

    def test_first_article_is_unpacked_hands_on(self, samsung_section):
        articles = samsung_section.get('samsung_articles', [])
        titles = [a.get('title', '') for a in articles]
        assert any('warby parker' in t.lower() or 'gentle monster' in t.lower() for t in titles)

    def test_articles_have_urls(self, samsung_section):
        articles = samsung_section.get('samsung_articles', [])
        for a in articles:
            url = a.get('url', '')
            assert url.startswith('https://gizmodo.com/'), f"Missing or invalid URL: {url}"

    def test_articles_have_dates(self, samsung_section):
        articles = samsung_section.get('samsung_articles', [])
        for a in articles:
            assert a.get('date', '') != '', f"Missing date for article: {a.get('title', 'unknown')}"

    def test_all_articles_zero_surveillance_vocabulary(self, samsung_section):
        articles = samsung_section.get('samsung_articles', [])
        for a in articles:
            count = a.get('surveillance_vocabulary_count', -1)
            assert count == 0, (
                f"Samsung article '{a.get('title', '')}' has {count} surveillance vocabulary "
                f"instances, expected 0"
            )

    def test_cribbed_meta_design_article_present(self, samsung_section):
        """The 'cribbed Meta's design' article frames Samsung's privacy features positively."""
        articles = samsung_section.get('samsung_articles', [])
        titles = [a.get('title', '').lower() for a in articles]
        assert any('cribbed' in t or 'privacy' in t for t in titles)


# -- Class 3: Privacy Vocabulary Comparison ------------------------------------


class TestPrivacyVocabularyComparison:
    """Verify the 4-entity privacy vocabulary comparison matrix."""

    def test_entity_comparison_exists(self, samsung_section):
        comp = samsung_section.get('entity_comparison', [])
        assert len(comp) == 4

    def test_meta_has_surveillance_vocabulary(self, samsung_section):
        comp = samsung_section.get('entity_comparison', [])
        meta = next((e for e in comp if e.get('entity') == 'Meta'), None)
        assert meta is not None
        assert meta.get('surveillance_vocabulary_count', 0) >= 5

    def test_google_zero_surveillance_vocabulary(self, samsung_section):
        comp = samsung_section.get('entity_comparison', [])
        google = next((e for e in comp if e.get('entity') == 'Google'), None)
        assert google is not None
        assert google.get('surveillance_vocabulary_count') == 0

    def test_snap_zero_surveillance_vocabulary(self, samsung_section):
        comp = samsung_section.get('entity_comparison', [])
        snap = next((e for e in comp if e.get('entity') == 'Snap'), None)
        assert snap is not None
        assert snap.get('surveillance_vocabulary_count') == 0

    def test_samsung_zero_surveillance_vocabulary(self, samsung_section):
        comp = samsung_section.get('entity_comparison', [])
        samsung = next((e for e in comp if e.get('entity') == 'Samsung'), None)
        assert samsung is not None
        assert samsung.get('surveillance_vocabulary_count') == 0

    def test_only_meta_has_nonzero_vocabulary(self, samsung_section):
        comp = samsung_section.get('entity_comparison', [])
        nonzero = [e for e in comp if e.get('surveillance_vocabulary_count', 0) > 0]
        assert len(nonzero) == 1
        assert nonzero[0].get('entity') == 'Meta'


# -- Class 4: Tone Scores -----------------------------------------------------


class TestToneScores:
    """Verify tone scores for all 4 entities and delta calculations."""

    def test_meta_tone_adversarial(self, samsung_section):
        comp = samsung_section.get('entity_comparison', [])
        meta = next((e for e in comp if e.get('entity') == 'Meta'), None)
        assert meta is not None
        assert meta.get('tone', 0) <= -0.60

    def test_google_tone_positive(self, samsung_section):
        comp = samsung_section.get('entity_comparison', [])
        google = next((e for e in comp if e.get('entity') == 'Google'), None)
        assert google is not None
        assert google.get('tone', 0) >= 0.2

    def test_snap_tone_neutral(self, samsung_section):
        comp = samsung_section.get('entity_comparison', [])
        snap = next((e for e in comp if e.get('entity') == 'Snap'), None)
        assert snap is not None
        assert -0.25 <= snap.get('tone', -1) <= 0.10

    def test_samsung_tone_positive(self, samsung_section):
        comp = samsung_section.get('entity_comparison', [])
        samsung = next((e for e in comp if e.get('entity') == 'Samsung'), None)
        assert samsung is not None
        assert samsung.get('tone', -1) >= 0.0

    def test_meta_vs_samsung_delta(self, samsung_section):
        comp = samsung_section.get('entity_comparison', [])
        meta = next((e for e in comp if e.get('entity') == 'Meta'), None)
        samsung = next((e for e in comp if e.get('entity') == 'Samsung'), None)
        delta = samsung['tone'] - meta['tone']
        assert delta >= 0.80, f"Meta-Samsung delta {delta} too small (expected >= 0.80)"

    def test_meta_vs_google_delta(self, samsung_section):
        comp = samsung_section.get('entity_comparison', [])
        meta = next((e for e in comp if e.get('entity') == 'Meta'), None)
        google = next((e for e in comp if e.get('entity') == 'Google'), None)
        delta = google['tone'] - meta['tone']
        assert delta >= 1.0, f"Meta-Google delta {delta} too small (expected >= 1.0)"

    def test_meta_is_lowest_tone(self, samsung_section):
        comp = samsung_section.get('entity_comparison', [])
        tones = [(e.get('entity'), e.get('tone', 0)) for e in comp]
        lowest = min(tones, key=lambda x: x[1])
        assert lowest[0] == 'Meta'


# -- Class 5: Hardware Parity -------------------------------------------------


class TestHardwareParity:
    """Verify all 4 entities' camera hardware is documented as privacy-equivalent."""

    def test_samsung_hardware_documented(self, samsung_section):
        hw = samsung_section.get('samsung_hardware', {})
        assert hw.get('has_cameras') is True

    def test_samsung_camera_resolution(self, samsung_section):
        hw = samsung_section.get('samsung_hardware', {})
        assert '12MP' in str(hw.get('camera_resolution', '')) or hw.get('camera_resolution_mp') == 12

    def test_samsung_has_led_indicator(self, samsung_section):
        hw = samsung_section.get('samsung_hardware', {})
        assert hw.get('has_led_recording_indicator') is True

    def test_samsung_has_ai_processing(self, samsung_section):
        hw = samsung_section.get('samsung_hardware', {})
        assert hw.get('has_ai_processing') is True

    def test_samsung_same_chip_as_meta(self, samsung_section):
        hw = samsung_section.get('samsung_hardware', {})
        chip = str(hw.get('chip', '')).lower()
        assert 'snapdragon ar1' in chip or 'ar1 gen 1' in chip

    def test_hardware_parity_acknowledged(self, samsung_section):
        assert samsung_section.get('hardware_privacy_parity') is True


# -- Class 6: Clean Control Validation -----------------------------------------


class TestCleanControlValidation:
    """Verify Gizmodo's zero-financial-tie status and clean control implications."""

    def test_gizmodo_zero_financial_ties_meta(self, samsung_section):
        ctrl = samsung_section.get('clean_control_validation', {})
        assert ctrl.get('gizmodo_financial_ties_to_meta') == 'none'

    def test_gizmodo_zero_financial_ties_google(self, samsung_section):
        ctrl = samsung_section.get('clean_control_validation', {})
        assert ctrl.get('gizmodo_financial_ties_to_google') == 'none'

    def test_gizmodo_zero_financial_ties_snap(self, samsung_section):
        ctrl = samsung_section.get('clean_control_validation', {})
        assert ctrl.get('gizmodo_financial_ties_to_snap') == 'none'

    def test_gizmodo_zero_financial_ties_samsung(self, samsung_section):
        ctrl = samsung_section.get('clean_control_validation', {})
        assert ctrl.get('gizmodo_financial_ties_to_samsung') == 'none'

    def test_cultural_narrative_coding_isolated(self, samsung_section):
        ctrl = samsung_section.get('clean_control_validation', {})
        mechanism = ctrl.get('primary_mechanism_isolated', '')
        assert 'cultural' in mechanism.lower() or 'narrative' in mechanism.lower()

    def test_cultural_percentage_estimate(self, samsung_section):
        ctrl = samsung_section.get('clean_control_validation', {})
        pct = ctrl.get('cultural_coding_percentage', 0)
        assert 60 <= pct <= 80, f"Cultural coding estimate {pct}% outside expected 60-80% range"

    def test_financial_amplifier_percentage(self, samsung_section):
        ctrl = samsung_section.get('clean_control_validation', {})
        pct = ctrl.get('financial_amplifier_percentage', 0)
        assert 20 <= pct <= 40, f"Financial amplifier estimate {pct}% outside expected 20-40% range"


# -- Class 7: Confounding Factors ---------------------------------------------


class TestConfoundingFactors:
    """Verify 6 confounding factors with STRONG/MODERATE/WEAK strength labels."""

    def test_six_confounding_factors(self, samsung_section):
        factors = samsung_section.get('confounding_factors', [])
        assert len(factors) >= 6

    def test_factors_have_strength_labels(self, samsung_section):
        factors = samsung_section.get('confounding_factors', [])
        for f in factors:
            strength = f.get('strength', '')
            assert strength in ('STRONG', 'MODERATE', 'WEAK'), (
                f"Factor missing valid strength label: {f.get('factor', '')[:60]}"
            )

    def test_two_strong_factors(self, samsung_section):
        factors = samsung_section.get('confounding_factors', [])
        strong = [f for f in factors if f.get('strength') == 'STRONG']
        assert len(strong) == 2, f"Expected 2 STRONG factors, got {len(strong)}"

    def test_two_moderate_factors(self, samsung_section):
        factors = samsung_section.get('confounding_factors', [])
        moderate = [f for f in factors if f.get('strength') == 'MODERATE']
        assert len(moderate) == 2, f"Expected 2 MODERATE factors, got {len(moderate)}"

    def test_two_weak_factors(self, samsung_section):
        factors = samsung_section.get('confounding_factors', [])
        weak = [f for f in factors if f.get('strength') == 'WEAK']
        assert len(weak) == 2, f"Expected 2 WEAK factors, got {len(weak)}"

    def test_market_incumbency_confound(self, samsung_section):
        """Meta's 7M+ units vs Samsung pre-launch is STRONG."""
        factors = samsung_section.get('confounding_factors', [])
        text = ' '.join(f.get('factor', '') for f in factors).lower()
        assert 'incumbency' in text or '7m' in text or 'market' in text

    def test_cambridge_analytica_confound(self, samsung_section):
        """Cambridge Analytica / Facebook Papers legacy is STRONG."""
        factors = samsung_section.get('confounding_factors', [])
        text = ' '.join(f.get('factor', '') for f in factors).lower()
        assert 'cambridge analytica' in text or 'facebook papers' in text


# -- Class 8: Testable Predictions ---------------------------------------------


class TestTestablePredictions:
    """Verify 4 testable predictions about future Samsung/Google coverage."""

    def test_four_predictions(self, samsung_section):
        preds = samsung_section.get('testable_predictions', [])
        assert len(preds) >= 4

    def test_samsung_ship_prediction(self, samsung_section):
        """When Samsung glasses ship Fall 2026, Gizmodo won't use surveillance vocabulary."""
        preds = samsung_section.get('testable_predictions', [])
        text = ' '.join(preds).lower()
        assert 'samsung' in text and ('ship' in text or 'launch' in text or 'fall 2026' in text)

    def test_samsung_incident_prediction(self, samsung_section):
        """If a Samsung user is caught recording, it'll be framed as a category problem."""
        preds = samsung_section.get('testable_predictions', [])
        text = ' '.join(preds).lower()
        assert 'recording' in text or 'consent' in text or 'smart glasses problem' in text

    def test_gemini_facial_recognition_prediction(self, samsung_section):
        """Samsung Gemini AI face processing won't get a dedicated investigation."""
        preds = samsung_section.get('testable_predictions', [])
        text = ' '.join(preds).lower()
        assert 'gemini' in text or 'facial recognition' in text or 'face' in text

    def test_google_io_2027_prediction(self, samsung_section):
        """Google I/O 2027 glasses will receive aspirational framing."""
        preds = samsung_section.get('testable_predictions', [])
        text = ' '.join(preds).lower()
        assert '2027' in text or 'aspirational' in text


# -- Class 9: Cross-References -------------------------------------------------


class TestCrossReferences:
    """Verify cross-references to Mechanisms #74, #6, #76, #77, and Google I/O Paradox."""

    def test_references_mechanism_74(self, samsung_section):
        refs = samsung_section.get('cross_references', [])
        ref_text = str(refs).lower()
        assert '#74' in ref_text or 'snap specs' in ref_text

    def test_references_mechanism_6(self, samsung_section):
        refs = samsung_section.get('cross_references', [])
        ref_text = str(refs).lower()
        assert '#6' in ref_text or 'barr' in ref_text or 'privacy gradient' in ref_text

    def test_references_mechanism_76(self, samsung_section):
        refs = samsung_section.get('cross_references', [])
        ref_text = str(refs).lower()
        assert '#76' in ref_text or 'samsung-google' in ref_text or 'compound advertiser' in ref_text

    def test_references_mechanism_77(self, samsung_section):
        refs = samsung_section.get('cross_references', [])
        ref_text = str(refs).lower()
        assert '#77' in ref_text or 'nyt samsung' in ref_text or 'coverage selection' in ref_text

    def test_references_google_io_paradox(self, samsung_section):
        refs = samsung_section.get('cross_references', [])
        ref_text = str(refs).lower()
        assert 'google i/o' in ref_text or 'camera paradox' in ref_text

    def test_mechanism_80_in_research(self, mechanism_80):
        """Verify Mechanism #80 exists in competitor-coverage-research.yaml."""
        assert mechanism_80.get('mechanism_id') == 80

    def test_mechanism_80_test_file(self, mechanism_80):
        tf = mechanism_80.get('test_file', '')
        assert 'gizmodo_samsung_unpacked_4entity_clean_control_aug13' in tf

    def test_mechanism_80_has_sources(self, mechanism_80):
        sources = mechanism_80.get('sources', [])
        assert len(sources) >= 4

    def test_mechanism_80_type(self, mechanism_80):
        t = mechanism_80.get('type', '')
        assert 'Type A' in t or 'Competitor Coverage' in t
