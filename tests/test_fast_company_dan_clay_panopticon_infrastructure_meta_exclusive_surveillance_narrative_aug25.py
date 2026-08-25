"""
Fast Company Dan Clay Panopticon Infrastructure Meta-Exclusive Surveillance Narrative (Aug 2026)

Mechanism #300: Fast Company Dan Clay uses "panopticon," "creepy," "pervert glasses,"
               "algorithm chow," and "forfeiture of privacy" to frame Meta's smart glasses
               as surveillance infrastructure — while omitting Apple's camera AirPods,
               Google/Samsung Android XR glasses, and Snap Spectacles from the analysis.

CORE FINDING:
Dan Clay's Fast Company article "Meta's creepy smart glasses are part of a much bigger
plan" (Aug 24, 2026) performs a surveillance-infrastructure analysis of camera wearables
that logically applies to any company building camera-equipped face-worn devices with
AI data processing — but applies it exclusively to Meta.

The article deploys 9 alarm-vocabulary terms (creepy, pervert glasses, panopticon,
algorithm chow, forfeiture of privacy, captive to Meta's digital infrastructure,
nonconsensual content, ubiquitous networked cameras, surveillance infrastructure)
with zero positive use cases mentioned (accessibility, translation, navigation,
hands-free communication, live captioning all omitted).

CROSS-ENTITY ASYMMETRY:
- Apple's camera-equipped AirPods (leaked Aug 18, 2026, always-on passive camera mode)
  and N50 smart glasses: NOT MENTIONED
- Google/Samsung Android XR camera glasses (fall 2026 launch): NOT MENTIONED
- Snap Spectacles 5th gen ($2,195, dual cameras): NOT MENTIONED
- Same publication's Apple Vision Pro coverage: protective framing ("impressive privacy
  protections worth calling out," "you don't have to worry")

The "egocentric data" and "contextualized AI" the article frames as sinister are
Apple's exact stated goals for camera AirPods and smart glasses.

Sources:
  Dan Clay, Fast Company (Aug 24, 2026):
    https://www.fastcompany.com/91594615/metas-creepy-smart-glasses-are-part-of-a-much-bigger-plan
  Fast Company (Jun 2024): Can Apple see what you're doing when you wear your Vision Pro?
  9to5Mac / leaked macOS code (Aug 18, 2026): Apple camera-equipped AirPods
  Google I/O 2025 + Samsung: Android XR camera glasses fall 2026
  Snap (2025): Spectacles 5th gen, dual cameras
"""
import os
import yaml
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture(scope='session')
def competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        data = yaml.safe_load(f)
    return data


def _find_mechanism(data, mechanism_id):
    """Search all YAML sections for a mechanism by ID."""
    for section_key in ('aggregate_findings', 'cross_publication_findings', 'publications'):
        section = data.get(section_key, {})
        if isinstance(section, dict):
            for key, value in section.items():
                if isinstance(value, dict) and value.get('mechanism_id') == mechanism_id:
                    return value
                # Check nested findings inside publications
                if isinstance(value, dict):
                    for sub_key, sub_val in value.items():
                        if isinstance(sub_val, dict) and sub_val.get('mechanism_id') == mechanism_id:
                            return sub_val
    return None


@pytest.fixture
def mechanism(competitor_research):
    mech = _find_mechanism(competitor_research, 300)
    if not mech:
        # Direct key lookup as fallback
        pubs = competitor_research.get('publications', {})
        mech = pubs.get(
            'fast_company_dan_clay_panopticon_infrastructure_meta_exclusive_surveillance_narrative', {}
        )
    return mech


# ── Mechanism Structure ──────────────────────────────────────────────────

class TestMechanismStructure:
    """Verify mechanism #300 exists and has required fields."""

    def test_mechanism_exists(self, mechanism):
        assert mechanism, "Mechanism #300 not found in aggregate_findings"

    def test_mechanism_id(self, mechanism):
        assert mechanism.get('mechanism_id') == 300

    def test_mechanism_name(self, mechanism):
        name = mechanism.get('name', '')
        assert 'Panopticon' in name or 'panopticon' in name.lower()
        assert 'Dan Clay' in name

    def test_mechanism_type(self, mechanism):
        assert mechanism.get('type') == 'journalist_cross_entity'

    def test_journalist_is_dan_clay(self, mechanism):
        assert mechanism.get('journalist') == 'Dan Clay'

    def test_publication_is_fast_company(self, mechanism):
        assert 'Fast Company' in mechanism.get('publication', '')

    def test_article_date_aug_2026(self, mechanism):
        assert mechanism.get('article_date') == '2026-08-24'

    def test_has_sources(self, mechanism):
        sources = mechanism.get('sources', [])
        assert len(sources) >= 4, f"Expected at least 4 sources, got {len(sources)}"

    def test_has_confounders(self, mechanism):
        confounders = mechanism.get('confounders', [])
        assert len(confounders) >= 4, f"Expected at least 4 confounders, got {len(confounders)}"

    def test_has_cross_references(self, mechanism):
        xrefs = mechanism.get('cross_references', [])
        assert len(xrefs) >= 2, f"Expected at least 2 cross-references, got {len(xrefs)}"

    def test_has_test_file_reference(self, mechanism):
        tf = mechanism.get('test_file', '')
        assert 'fast_company_dan_clay' in tf
        assert tf.endswith('_aug25.py')


# ── Alarm Vocabulary Analysis ────────────────────────────────────────────

class TestPanopticonVocabularyAnalysis:
    """Verify the alarm vocabulary inventory and its Meta-exclusive direction."""

    def test_alarm_vocabulary_exists(self, mechanism):
        vocab = mechanism.get('meta_alarm_vocabulary', [])
        assert len(vocab) >= 7, f"Expected at least 7 alarm terms, got {len(vocab)}"

    def test_creepy_in_headline(self, mechanism):
        vocab = mechanism.get('meta_alarm_vocabulary', [])
        creepy = [v for v in vocab if v.get('term', '').lower() == 'creepy']
        assert creepy, "Expected 'creepy' in alarm vocabulary"
        assert any('headline' in v.get('location', '') for v in creepy), \
            "'creepy' should appear in headline"

    def test_pervert_glasses_present(self, mechanism):
        vocab = mechanism.get('meta_alarm_vocabulary', [])
        terms = [v.get('term', '').lower() for v in vocab]
        assert any('pervert' in t for t in terms), \
            "Expected 'pervert glasses' stigma label in vocabulary"

    def test_panopticon_metaphor_present(self, mechanism):
        vocab = mechanism.get('meta_alarm_vocabulary', [])
        terms = [v.get('term', '').lower() for v in vocab]
        assert any('panopticon' in t for t in terms), \
            "Expected 'panopticon' metaphor in vocabulary"

    def test_algorithm_chow_present(self, mechanism):
        vocab = mechanism.get('meta_alarm_vocabulary', [])
        terms = [v.get('term', '').lower() for v in vocab]
        assert any('algorithm chow' in t for t in terms), \
            "Expected 'algorithm chow' in vocabulary"

    def test_forfeiture_of_privacy_present(self, mechanism):
        vocab = mechanism.get('meta_alarm_vocabulary', [])
        terms = [v.get('term', '').lower() for v in vocab]
        assert any('forfeiture' in t for t in terms), \
            "Expected 'forfeiture of privacy' in vocabulary"

    def test_meta_alarm_term_count(self, mechanism):
        count = mechanism.get('meta_alarm_term_count', 0)
        assert count >= 7, f"Expected at least 7 Meta alarm terms, got {count}"

    def test_zero_positive_use_cases(self, mechanism):
        pos = mechanism.get('meta_positive_use_cases', -1)
        assert pos == 0, f"Expected 0 positive use cases mentioned, got {pos}"

    def test_positive_use_cases_omitted_listed(self, mechanism):
        omitted = mechanism.get('positive_use_cases_omitted', [])
        assert len(omitted) >= 3, \
            f"Expected at least 3 omitted positive use cases, got {len(omitted)}"
        omitted_lower = [o.lower() for o in omitted]
        assert any('accessibility' in o for o in omitted_lower)
        assert any('translation' in o for o in omitted_lower)


# ── Apple Camera Wearable Omission ───────────────────────────────────────

class TestAppleCameraWearableOmission:
    """Verify the mechanism documents Apple's camera wearable absence from the analysis."""

    def test_entities_compared_includes_apple(self, mechanism):
        entities = mechanism.get('entities_compared', [])
        apple = [e for e in entities if e.get('entity') == 'Apple']
        assert apple, "Expected Apple in entities_compared"

    def test_apple_not_mentioned(self, mechanism):
        entities = mechanism.get('entities_compared', [])
        apple = [e for e in entities if e.get('entity') == 'Apple']
        assert apple
        assert apple[0].get('mentioned') is False, \
            "Apple should be documented as NOT mentioned in the article"

    def test_apple_zero_alarm_terms(self, mechanism):
        entities = mechanism.get('entities_compared', [])
        apple = [e for e in entities if e.get('entity') == 'Apple']
        assert apple
        assert apple[0].get('alarm_terms', -1) == 0

    def test_apple_products_documented(self, mechanism):
        entities = mechanism.get('entities_compared', [])
        apple = [e for e in entities if e.get('entity') == 'Apple']
        assert apple
        product = apple[0].get('product', '').lower()
        assert 'airpods' in product or 'camera' in product, \
            f"Apple product should reference camera AirPods: {product}"

    def test_egocentric_data_equivalence(self, mechanism):
        equiv = mechanism.get('egocentric_data_equivalence', {})
        assert equiv, "Expected egocentric_data_equivalence section"
        assert 'apple' in equiv.get('apple_equivalent', '').lower() or \
               'airpods' in equiv.get('apple_equivalent', '').lower(), \
            "Should document Apple's equivalent use of camera data for AI"

    def test_functional_difference_none(self, mechanism):
        equiv = mechanism.get('egocentric_data_equivalence', {})
        diff = equiv.get('functional_difference', '').lower()
        assert 'none' in diff, \
            f"Functional difference should be 'none', got: {diff}"


# ── Google/Samsung/Snap Omission ─────────────────────────────────────────

class TestCompetitorCameraWearableOmission:
    """Verify the mechanism documents Google/Samsung and Snap omission."""

    def test_google_samsung_in_entities(self, mechanism):
        entities = mechanism.get('entities_compared', [])
        entity_names = [e.get('entity', '').lower() for e in entities]
        assert any('google' in n or 'samsung' in n for n in entity_names), \
            "Expected Google/Samsung in entities_compared"

    def test_google_samsung_not_mentioned(self, mechanism):
        entities = mechanism.get('entities_compared', [])
        gs = [e for e in entities if 'google' in e.get('entity', '').lower()
              or 'samsung' in e.get('entity', '').lower()]
        assert gs
        assert gs[0].get('mentioned') is False

    def test_google_samsung_zero_alarm_terms(self, mechanism):
        entities = mechanism.get('entities_compared', [])
        gs = [e for e in entities if 'google' in e.get('entity', '').lower()
              or 'samsung' in e.get('entity', '').lower()]
        assert gs
        assert gs[0].get('alarm_terms', -1) == 0

    def test_snap_in_entities(self, mechanism):
        entities = mechanism.get('entities_compared', [])
        entity_names = [e.get('entity', '').lower() for e in entities]
        assert any('snap' in n for n in entity_names), \
            "Expected Snap in entities_compared"

    def test_snap_not_mentioned(self, mechanism):
        entities = mechanism.get('entities_compared', [])
        snap = [e for e in entities if 'snap' in e.get('entity', '').lower()]
        assert snap
        assert snap[0].get('mentioned') is False

    def test_meta_is_only_entity_with_alarm_terms(self, mechanism):
        entities = mechanism.get('entities_compared', [])
        for e in entities:
            if e.get('entity') == 'Meta':
                assert e.get('alarm_terms', 0) > 0, "Meta should have alarm terms"
            else:
                assert e.get('alarm_terms', 0) == 0, \
                    f"{e.get('entity')} should have zero alarm terms"


# ── Cross-Entity Framing Differential ────────────────────────────────────

class TestCrossEntityFramingDifferential:
    """Verify Fast Company's differential framing between Meta and Apple wearables."""

    def test_cross_publication_apple_coverage_exists(self, mechanism):
        xpub = mechanism.get('cross_publication_apple_coverage', {})
        assert xpub, "Expected cross_publication_apple_coverage section"

    def test_apple_article_protective_framing(self, mechanism):
        xpub = mechanism.get('cross_publication_apple_coverage', {})
        assert xpub.get('framing') == 'protective', \
            f"Apple article framing should be 'protective', got: {xpub.get('framing')}"

    def test_apple_article_key_phrases(self, mechanism):
        xpub = mechanism.get('cross_publication_apple_coverage', {})
        phrases = xpub.get('key_phrases', [])
        assert len(phrases) >= 1, "Expected protective key phrases"
        phrases_lower = [p.lower() for p in phrases]
        assert any('impressive' in p or 'don\'t have to worry' in p for p in phrases_lower)

    def test_meta_framing_is_surveillance(self, mechanism):
        entities = mechanism.get('entities_compared', [])
        meta = [e for e in entities if e.get('entity') == 'Meta']
        assert meta
        framing = meta[0].get('framing', '').lower()
        assert 'surveillance' in framing, \
            f"Meta framing should include 'surveillance', got: {framing}"

    def test_panopticon_applied_exclusively_to_meta(self, mechanism):
        pan = mechanism.get('panopticon_analysis', {})
        assert pan, "Expected panopticon_analysis section"
        applied_to = pan.get('metaphor_applied_to', '').lower()
        assert 'meta' in applied_to

    def test_panopticon_logical_scope_broader(self, mechanism):
        pan = mechanism.get('panopticon_analysis', {})
        scope = pan.get('logical_scope', '').lower()
        assert 'any' in scope or 'camera' in scope, \
            "Panopticon logical scope should apply to any camera wearable company"

    def test_panopticon_multiple_entities_should_qualify(self, mechanism):
        pan = mechanism.get('panopticon_analysis', {})
        should_qualify = pan.get('entities_that_should_qualify', [])
        assert len(should_qualify) >= 3, \
            f"Expected at least 3 entities that should qualify for panopticon analysis"

    def test_mansueto_ventures_financial_context(self, mechanism):
        mv = mechanism.get('mansueto_ventures_financial_context', {})
        assert mv, "Expected mansueto_ventures_financial_context section"
        assert 'Mansueto' in mv.get('parent_company', '')
        assert mv.get('apple_advertising_dependency') in ('significant', 'high')


# ── Confounders ──────────────────────────────────────────────────────────

class TestConfounders:
    """Verify confounders acknowledge legitimate alternative explanations."""

    def test_has_strong_confounders(self, mechanism):
        confounders = mechanism.get('confounders', [])
        strong = [c for c in confounders if c.get('strength') == 'STRONG']
        assert len(strong) >= 2, \
            f"Expected at least 2 STRONG confounders, got {len(strong)}"

    def test_market_leader_confounder(self, mechanism):
        confounders = mechanism.get('confounders', [])
        descs = [c.get('description', '').lower() for c in confounders]
        assert any('shipping' in d or 'market' in d or 'scale' in d for d in descs), \
            "Should acknowledge Meta is the only company shipping camera glasses at scale"

    def test_privacy_history_confounder(self, mechanism):
        confounders = mechanism.get('confounders', [])
        descs = [c.get('description', '').lower() for c in confounders]
        assert any('cambridge' in d or 'privacy' in d or 'ftc' in d for d in descs), \
            "Should acknowledge Meta's documented privacy controversy history"

    def test_asymmetry_score_moderate(self, mechanism):
        score = mechanism.get('asymmetry_score', 0)
        assert 0.5 <= score <= 0.9, \
            f"Score should reflect strong confounders moderating asymmetry: {score}"


# ── Cross-References ─────────────────────────────────────────────────────

class TestCrossReferences:
    """Verify mechanism links to related mechanisms in the profile."""

    def test_references_mia_sato_mechanism(self, mechanism):
        xrefs = mechanism.get('cross_references', [])
        ids = [x.get('mechanism_id') for x in xrefs]
        assert 213 in ids, "Should reference Mia Sato Verge vocabulary bifurcation (#213)"

    def test_references_katie_couric_mechanism(self, mechanism):
        xrefs = mechanism.get('cross_references', [])
        ids = [x.get('mechanism_id') for x in xrefs]
        assert 297 in ids, "Should reference Katie Couric expert authority mechanism (#297)"

    def test_all_xrefs_have_relationship(self, mechanism):
        xrefs = mechanism.get('cross_references', [])
        for xref in xrefs:
            assert 'relationship' in xref, \
                f"Cross-reference to #{xref.get('mechanism_id')} missing relationship"

    def test_all_xrefs_have_description(self, mechanism):
        xrefs = mechanism.get('cross_references', [])
        for xref in xrefs:
            assert xref.get('description'), \
                f"Cross-reference to #{xref.get('mechanism_id')} missing description"
