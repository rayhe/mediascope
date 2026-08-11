"""
Chokkattu / WIRED Compound Competitor Wearables Silence — Type B Journalist Cross-Entity (Aug 11, 2026)

Mechanism #42: Compound Competitor Coverage Selection Silence

KEY FINDING: WIRED's wearables beat, anchored by Reviews Editor Julian Chokkattu,
published 3+ Meta smart glasses articles in the Jun-Jul 2026 window but ZERO
standalone articles about EITHER of the two biggest competitor wearable launches:

  1. Snap Specs consumer launch ($2,195, Jun 16, 2026 at AWE)
     - 4 cameras (2 RGB + 2 IR), hand tracking, standalone AR, electrochromic lenses
     - Covered by: TechCrunch, Reuters, Gizmodo, Engadget, Fast Company, MacRumors,
       Android Authority, Android Police, Dezeen, Road to VR, USA Today, Wareable,
       Tom's Guide, Slashdot (citing Verge)
     - WIRED standalone article count: 0

  2. Samsung Galaxy Glasses (Galaxy Unpacked, Jul 22, 2026)
     - 12MP camera, Snapdragon AR1, Google Gemini AI, ~50g
     - Covered by: 20+ publications (Mechanism #39)
     - WIRED standalone article count: 0

Meanwhile WIRED published multiple standalone Meta glasses articles in the same
window: Chokkattu's Jun 23 Starfire/Adventurer/Fury launch article, his Jul 2
subscription pricing analysis, and his Business Wars podcast episodes (Jun 3-11).

This extends Mechanism #39 (Samsung Coverage Selection Gap) from an isolated
incident to a SYSTEMATIC PATTERN: WIRED's wearables beat covers Meta glasses
extensively while publishing zero standalone articles on the two largest
competitor wearable launches in the same season.

PRIVACY FRAMING ASYMMETRY — The Camera Count Paradox:
  - Snap Specs: 4 cameras (2 RGB front + 2 IR hand tracking) -> ZERO privacy/
    surveillance framing from any publication, including WIRED
  - Samsung Galaxy Glasses: 12MP camera, Google Gemini cloud -> ZERO surveillance
    framing from any publication
  - Meta Ray-Ban: 1 camera (12MP) -> "mass surveillance," "I'm a Creep,"
    "nefarious," "discreetly" (WIRED's own vocabulary)

When WIRED DOES cover competitors, it applies technical feature language.
When it covers Meta, the same camera hardware triggers surveillance vocabulary.
But for Snap Specs, coverage doesn't exist at WIRED at all — the silence
itself prevents any framing comparison.

LEGITIMATE EDITORIAL FACTORS (5 documented):
  1. Editorial bandwidth: WIRED may have deprioritized one event for another
  2. Snap Specs not yet shipping: announcement-only vs product-in-hand
  3. Beat assignment: Chokkattu may focus on products he can review hands-on
  4. Platform relevance: Snap Specs target developers, not WIRED's reader demo
  5. Snap is smaller market cap / less culturally relevant than Meta/Samsung

None of these explain why WIRED skipped BOTH launches while covering multiple
Meta glasses articles, nor why every other major tech publication covered them.

Sources:
  - TechCrunch Snap Specs: https://techcrunch.com/2026/06/16/snap-finally-debuts-its-long-awaited-ar-glasses-specs-and-oof-they-arent-cheap/
  - Reuters Snap Specs: https://www.reuters.com/technology/snap-bets-life-beyond-smartphones-with-2195-specs-augmented-reality-glasses-2026-06-16/
  - Gizmodo Snap Specs roast: https://gizmodo.com/snaps-ar-glasses-arent-even-out-yet-and-theyre-already-getting-roasted-to-death-2000773124
  - Gizmodo Snap Specs preorder: https://gizmodo.com/apple-vision-pro-isnt-the-only-future-of-ar-specs-wearable-computer-built-into-see-through-glasses-are-now-up-for-pre-order-2000779916
  - Fast Company Snap Specs: https://www.fastcompany.com/91559773/snap-specs-2026-ar-glasses-evan-spiegel
  - Engadget AWE live blog: https://www.engadget.com/2194982/awe-xr-2026-snap-live-blog/
  - Snap Specs BusinessWire: https://www.businesswire.com/news/home/20260612154498/en/Snap-Inc.-Debuts-SPECS-Augmented-Reality-Glasses-to-Make-Computing-More-Human
  - Android Authority Snap Specs: https://www.androidauthority.com/snap-specs-ar-glasses-3677759/
  - MacRumors Snap Specs: https://www.macrumors.com/2026/06/16/snap-specs-ar-glasses/
  - Samsung Newsroom (Mechanism #39 source): https://news.samsung.com/us/samsung-galaxy-ecosystem-everyday-eyewear
  - Cross-ref Mechanism #39: test_chokkattu_samsung_coverage_selection_gap_aug11.py
  - Cross-ref Mechanism #30: test_chokkattu_temporal_framing_oscillation_aug10.py

Created: 2026-08-11
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
REPO_ROOT = os.path.join(os.path.dirname(__file__), '..')


def load_yaml(name):
    with open(os.path.join(PROFILES_DIR, name)) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def wired():
    return load_yaml('wired.yaml')


@pytest.fixture(scope='module')
def entities():
    return load_yaml('competitor-entities.yaml')


@pytest.fixture(scope='module')
def research():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def compound_silence(wired):
    section = wired.get('chokkattu_compound_competitor_silence')
    assert section is not None, (
        "wired.yaml must have chokkattu_compound_competitor_silence section"
    )
    return section


# == Class 1: Section Structure ==


class TestSectionStructure:
    """Verify the compound silence section exists with required fields."""

    def test_section_exists(self, wired):
        assert 'chokkattu_compound_competitor_silence' in wired

    def test_has_mechanism_id(self, compound_silence):
        assert compound_silence.get('mechanism_id') == 42

    def test_has_mechanism_name(self, compound_silence):
        name = compound_silence.get('mechanism_name', '')
        assert 'compound' in name.lower() or 'silence' in name.lower()

    def test_has_finding_summary(self, compound_silence):
        summary = compound_silence.get('finding_summary', '')
        assert len(summary) > 50

    def test_has_finding_type(self, compound_silence):
        assert compound_silence.get('finding_type') == 'coverage_selection_silence'

    def test_has_analysis_date(self, compound_silence):
        assert '2026-08-11' in str(compound_silence.get('analysis_date', ''))


# == Class 2: Snap Specs Event Documentation ==


class TestSnapSpecsEvent:
    """Validate Snap Specs launch event data."""

    def test_snap_specs_section_exists(self, compound_silence):
        assert 'snap_specs_launch' in compound_silence

    def test_snap_specs_date(self, compound_silence):
        snap = compound_silence['snap_specs_launch']
        assert snap.get('date') == '2026-06-16'

    def test_snap_specs_price(self, compound_silence):
        snap = compound_silence['snap_specs_launch']
        assert snap.get('price_usd') == 2195

    def test_snap_specs_venue(self, compound_silence):
        snap = compound_silence['snap_specs_launch']
        venue = str(snap.get('venue', '')).lower()
        assert 'awe' in venue or 'augmented world expo' in venue

    def test_snap_specs_camera_count(self, compound_silence):
        snap = compound_silence['snap_specs_launch']
        assert snap.get('camera_count') == 4

    def test_snap_specs_camera_types(self, compound_silence):
        snap = compound_silence['snap_specs_launch']
        types = snap.get('camera_types', [])
        assert len(types) >= 2  # RGB + IR at minimum

    def test_snap_specs_standalone(self, compound_silence):
        snap = compound_silence['snap_specs_launch']
        assert snap.get('standalone') is True

    def test_snap_specs_wired_article_count(self, compound_silence):
        snap = compound_silence['snap_specs_launch']
        assert snap.get('wired_standalone_articles') == 0

    def test_snap_specs_other_pubs_covered(self, compound_silence):
        snap = compound_silence['snap_specs_launch']
        pubs = snap.get('publications_that_covered', [])
        assert len(pubs) >= 8, f"Expected 8+ pubs, got {len(pubs)}"


# == Class 3: Samsung Galaxy Glasses Cross-Reference ==


class TestSamsungCrossRef:
    """Cross-validate Samsung data matches Mechanism #39."""

    def test_samsung_section_exists(self, compound_silence):
        assert 'samsung_galaxy_glasses' in compound_silence

    def test_samsung_date(self, compound_silence):
        samsung = compound_silence['samsung_galaxy_glasses']
        assert samsung.get('date') == '2026-07-22'

    def test_samsung_wired_coverage_zero(self, compound_silence):
        samsung = compound_silence['samsung_galaxy_glasses']
        assert samsung.get('wired_standalone_articles') == 0

    def test_samsung_cross_ref_mechanism_39(self, compound_silence):
        samsung = compound_silence['samsung_galaxy_glasses']
        refs = samsung.get('cross_references', [])
        assert any('39' in str(r) for r in refs), (
            "Samsung section must cross-reference Mechanism #39"
        )


# == Class 4: Meta Glasses Coverage in Same Window ==


class TestMetaCoverageInWindow:
    """Verify documented Meta coverage for contrast."""

    def test_meta_coverage_section_exists(self, compound_silence):
        assert 'meta_coverage_same_window' in compound_silence

    def test_meta_article_count(self, compound_silence):
        meta = compound_silence['meta_coverage_same_window']
        count = meta.get('standalone_article_count', 0)
        assert count >= 3, f"Expected 3+ Meta articles, got {count}"

    def test_meta_articles_have_dates(self, compound_silence):
        meta = compound_silence['meta_coverage_same_window']
        articles = meta.get('articles', [])
        for article in articles:
            assert 'date' in article, f"Article missing date: {article}"

    def test_meta_articles_have_author(self, compound_silence):
        meta = compound_silence['meta_coverage_same_window']
        articles = meta.get('articles', [])
        chokkattu_articles = [a for a in articles if 'Chokkattu' in str(a.get('author', ''))]
        assert len(chokkattu_articles) >= 2, "Need 2+ Chokkattu Meta articles"


# == Class 5: Camera Count Privacy Paradox ==


class TestCameraCountPrivacyParadox:
    """Validate the camera count vs privacy framing asymmetry."""

    def test_privacy_paradox_section_exists(self, compound_silence):
        assert 'camera_privacy_paradox' in compound_silence

    def test_snap_camera_count_documented(self, compound_silence):
        paradox = compound_silence['camera_privacy_paradox']
        snap = paradox.get('snap_specs', {})
        assert snap.get('camera_count') == 4

    def test_meta_camera_count_documented(self, compound_silence):
        paradox = compound_silence['camera_privacy_paradox']
        meta = paradox.get('meta_ray_ban', {})
        assert meta.get('camera_count') == 1

    def test_snap_surveillance_language_count(self, compound_silence):
        paradox = compound_silence['camera_privacy_paradox']
        snap = paradox.get('snap_specs', {})
        assert snap.get('surveillance_language_instances') == 0

    def test_meta_surveillance_language_present(self, compound_silence):
        paradox = compound_silence['camera_privacy_paradox']
        meta = paradox.get('meta_ray_ban', {})
        lang = meta.get('surveillance_language_examples', [])
        assert len(lang) >= 3, f"Expected 3+ surveillance language examples for Meta"

    def test_samsung_surveillance_language_zero(self, compound_silence):
        paradox = compound_silence['camera_privacy_paradox']
        samsung = paradox.get('samsung_galaxy_glasses', {})
        assert samsung.get('surveillance_language_instances') == 0


# == Class 6: Compound Pattern Validation ==


class TestCompoundPattern:
    """Validate this is a pattern, not isolated incident."""

    def test_two_missed_events(self, compound_silence):
        """Must document at least 2 missed competitor events."""
        missed = compound_silence.get('missed_competitor_events', [])
        assert len(missed) >= 2, f"Expected 2+ missed events, got {len(missed)}"

    def test_pattern_is_systematic(self, compound_silence):
        """Pattern must be labeled systematic, not isolated."""
        pattern = compound_silence.get('pattern_type', '')
        assert 'systematic' in pattern.lower() or 'compound' in pattern.lower()

    def test_window_documented(self, compound_silence):
        """Must specify the time window for comparison."""
        window = compound_silence.get('comparison_window', {})
        assert 'start' in window and 'end' in window

    def test_window_covers_both_events(self, compound_silence):
        window = compound_silence.get('comparison_window', {})
        start = str(window.get('start', ''))
        end = str(window.get('end', ''))
        assert start <= '2026-06-16', "Window must start before Snap launch"
        assert end >= '2026-07-22', "Window must extend through Samsung launch"


# == Class 7: Legitimate Confounding Factors ==


class TestConfoundingFactors:
    """Verify legitimate editorial factors are documented."""

    def test_factors_section_exists(self, compound_silence):
        assert 'legitimate_factors' in compound_silence

    def test_at_least_four_factors(self, compound_silence):
        factors = compound_silence.get('legitimate_factors', [])
        assert len(factors) >= 4, f"Need 4+ factors, got {len(factors)}"

    def test_bandwidth_factor(self, compound_silence):
        factors = compound_silence.get('legitimate_factors', [])
        factor_text = ' '.join(str(f) for f in factors).lower()
        assert 'bandwidth' in factor_text or 'capacity' in factor_text

    def test_shipping_status_factor(self, compound_silence):
        factors = compound_silence.get('legitimate_factors', [])
        factor_text = ' '.join(str(f) for f in factors).lower()
        assert 'shipping' in factor_text or 'hands-on' in factor_text or 'available' in factor_text


# == Class 8: Cross-Mechanism Validation ==


class TestCrossMechanismValidation:
    """Verify cross-references to related mechanisms."""

    def test_references_mechanism_39(self, compound_silence):
        refs = compound_silence.get('cross_references', [])
        ref_text = ' '.join(str(r) for r in refs)
        assert '39' in ref_text, "Must cross-reference Mechanism #39 (Samsung gap)"

    def test_references_mechanism_30(self, compound_silence):
        refs = compound_silence.get('cross_references', [])
        ref_text = ' '.join(str(r) for r in refs)
        assert '30' in ref_text, "Must cross-reference Mechanism #30 (temporal oscillation)"

    def test_test_file_for_mechanism_39_exists(self):
        path = os.path.join(REPO_ROOT, 'tests',
                            'test_chokkattu_samsung_coverage_selection_gap_aug11.py')
        assert os.path.exists(path), "Mechanism #39 test file must exist"

    def test_test_file_for_mechanism_30_exists(self):
        path = os.path.join(REPO_ROOT, 'tests',
                            'test_chokkattu_temporal_framing_oscillation_aug10.py')
        assert os.path.exists(path), "Mechanism #30 test file must exist"


# == Class 9: Competitor Entity Snap Data ==


class TestCompetitorEntitySnapData:
    """Verify Snap entity data in competitor-entities.yaml."""

    def test_snap_entity_exists(self, entities):
        ents = entities.get('entities', {})
        assert 'snap' in ents, "Snap must be in competitor-entities.yaml"

    def test_snap_has_specs_section(self, entities):
        snap = entities['entities'].get('snap', {})
        hw = snap.get('hardware_devices', {})
        assert 'specs_consumer' in hw or 'specs' in hw or any(
            'spec' in str(k).lower() for k in hw.keys()
        ), f"Snap must have a Specs hardware section, found: {list(hw.keys())}"


# == Class 10: Statistical Summary ==


class TestStatisticalSummary:
    """Validate the statistical comparison."""

    def test_summary_section_exists(self, compound_silence):
        assert 'statistical_summary' in compound_silence

    def test_wired_meta_vs_competitor_ratio(self, compound_silence):
        stats = compound_silence['statistical_summary']
        meta_count = stats.get('wired_meta_glasses_articles', 0)
        competitor_count = stats.get('wired_competitor_glasses_articles', 0)
        assert meta_count >= 3, f"Expected 3+ Meta articles, got {meta_count}"
        assert competitor_count == 0, f"Expected 0 competitor articles, got {competitor_count}"

    def test_other_pubs_covered_both(self, compound_silence):
        stats = compound_silence['statistical_summary']
        snap_pubs = stats.get('pubs_covering_snap_specs', 0)
        samsung_pubs = stats.get('pubs_covering_samsung_glasses', 0)
        assert snap_pubs >= 8
        assert samsung_pubs >= 10
