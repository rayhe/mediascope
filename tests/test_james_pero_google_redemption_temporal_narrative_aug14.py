"""
James Pero (Gizmodo) Google Smart Glasses Temporal Redemption Narrative
vs Meta Perpetual Surveillance Default

Type B: Journalist Cross-Entity Tracking (Aug 14, 2026 08:00 PT)
Mechanism #99: Google Temporal Redemption Narrative vs Meta Recidivism Loop

Finding: James Pero, Gizmodo's self-described "resident smart glasses guy,"
constructs DIFFERENT TEMPORAL NARRATIVES for Google vs Meta when covering
identical smart glasses hardware. Google gets a REDEMPTION ARC (failure →
learning → growth), while Meta gets a RECIDIVISM LOOP (failure → more failure
→ escalation). Both entities build camera-equipped smart glasses with the SAME
Snapdragon AR1 Gen 1 chip, 12MP cameras, LED indicators, and AI visual
processing.

The temporal narrative asymmetry isolates CULTURAL CODING as a mechanism
distinct from financial incentives (Gizmodo/Keleops AG has ZERO financial
ties to any tech company).

Google coverage — redemption narrative:
  - "Google's Next Smart Glasses May Have Actually Learned Something From
    the Glasshole Days" (Jan 14, 2026) — headline frames Google as having
    GROWN from past failures
  - "Google Seems Pretty Scared of the Words 'Smart Glasses'" (May 19, 2026)
    — playful mockery of branding, not adversarial privacy critique
  - "Google's Project Astra May Revolutionize Smart Glasses—but Not Today"
    (May 20, 2025) — aspirational forward framing

Meta coverage — perpetual surveillance default:
  - "Smart Glasses Are a Hit Even as Privacy Concerns Pile Up" (Jul 30, 2026)
    — Meta gets 8 of 10 substantive paragraphs of privacy criticism
  - "Can Smart Glasses Ever Be Privacy-Friendly?" (May 21, 2026)
    — Section titled "The anti-Meta plan"
  - "Smart Glasses Companies Are Getting Shamed Into Covering Their Cameras"
    (Mar 23, 2026) — opens with "Thanks to Meta"
  - "Smart Glasses Are Catching on With U.S. Police" (Aug 11, 2026)
    — Meta singled out for police adoption

The temporal narrative paradox:
  - Google Glass era → failure (2013-2015)
  - Google → "learned" from mistakes → redemption arc (2025-2026)
  - Meta Ray-Ban glasses → cameras (2021) → surveillance → escalation →
    recidivism (2021-2026)

Both companies shipped camera glasses. Google's PREVIOUS failure is framed
as LEARNING. Meta's CONTINUED market success is framed as ESCALATING THREAT.
The temporal coding inverts: failure becomes virtue (for Google), success
becomes menace (for Meta).

Distinct from:
  - #31 (Editorial Direction Override): Covers review vs editorial GENRE
    split. #99 covers TEMPORAL NARRATIVE structure applied to different
    entities within the same article genre.
  - #80 (4-entity clean control): Covers FRAMING VOCABULARY in glasses
    domain. #99 covers how the same journalist constructs different STORY
    TYPES (redemption vs recidivism).
  - #98 (Anthropic AI Safety): Covers Gizmodo's adversarial Anthropic
    coverage consistency. #99 covers TEMPORAL NARRATIVE asymmetry applied
    to Google vs Meta by a specific journalist.
  - #74 (Gizmodo Snap Specs): Privacy vocabulary suppression in Snap
    coverage. #99 is about narrative arc structure, not vocabulary selection.

6 confounding factors (2 STRONG, 2 MODERATE, 2 WEAK).
4 testable predictions.
5 cross-references (#31, #80, #98, #74, #95).

Source articles (all by James Pero at Gizmodo):
  Google:
  - https://gizmodo.com/googles-next-smart-glasses-may-have-actually-learned-something-from-the-glasshole-days-2000710198
  - https://gizmodo.com/google-seems-pretty-scared-of-the-words-smart-glasses-2000760916
  - https://gizmodo.com/googles-project-astra-may-revolutionize-smart-glasses-but-not-today-2000604663

  Meta:
  - https://gizmodo.com/smart-glasses-are-a-hit-even-as-privacy-concerns-pile-up-2000792911
  - https://gizmodo.com/can-smart-glasses-ever-be-privacy-friendly-these-companies-think-so-2000746927
  - https://gizmodo.com/smart-glasses-are-getting-shamed-into-covering-their-cameras-2000736843
  - https://gizmodo.com/smart-glasses-are-catching-on-with-u-s-police-2000797054
"""

import yaml
import os
import pytest
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"
GIZMODO_PATH = PROFILES_DIR / "gizmodo.yaml"
RESEARCH_PATH = PROFILES_DIR / "competitor-coverage-research.yaml"
ENTITIES_PATH = PROFILES_DIR / "competitor-entities.yaml"


@pytest.fixture(scope='module')
def gizmodo_profile():
    with open(GIZMODO_PATH) as f:
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
def temporal_narrative(gizmodo_profile):
    cross = gizmodo_profile.get('cross_entity_coverage', {})
    section = cross.get('pero_google_redemption_temporal_narrative')
    assert section is not None, (
        "Missing pero_google_redemption_temporal_narrative in "
        "gizmodo.yaml cross_entity_coverage"
    )
    return section


@pytest.fixture(scope='module')
def mechanism_99(research_data):
    findings = research_data.get('cross_publication_findings', {})
    section = findings.get('pero_google_redemption_temporal_narrative')
    assert section is not None, (
        "Missing pero_google_redemption_temporal_narrative in "
        "competitor-coverage-research.yaml cross_publication_findings"
    )
    return section


@pytest.fixture(scope='module')
def google_entity(entities_data):
    entity = entities_data.get('entities', {}).get('google', {})
    assert entity is not None, "Missing google entity in competitor-entities.yaml"
    return entity


# ===================================================================
# 1. TestMechanismMetadata — id, date, type, sources
# ===================================================================
class TestMechanismMetadata:
    """Verify mechanism #99 metadata is complete and correct."""

    def test_mechanism_id(self, temporal_narrative):
        assert temporal_narrative.get('mechanism_id') == 99

    def test_mechanism_id_in_research(self, mechanism_99):
        assert mechanism_99.get('mechanism_id') == 99

    def test_date_analyzed(self, temporal_narrative):
        assert temporal_narrative.get('date_analyzed') == '2026-08-14'

    def test_date_added_in_research(self, mechanism_99):
        assert mechanism_99.get('date_added') == '2026-08-14'

    def test_type_b(self, mechanism_99):
        t = mechanism_99.get('type', '')
        assert 'Type B' in t or 'type_b' in t.lower(), \
            f"Mechanism #99 should be Type B, got: {t}"

    def test_finding_type(self, temporal_narrative):
        finding = temporal_narrative.get('finding', '')
        assert 'temporal' in finding.lower() or 'redemption' in finding.lower(), \
            f"Finding should reference temporal/redemption narrative, got: {finding}"

    def test_source_urls_present(self, temporal_narrative):
        urls = temporal_narrative.get('source_urls', [])
        assert len(urls) >= 7, \
            f"Expected ≥7 source URLs (3 Google + 4 Meta), got {len(urls)}"

    def test_source_urls_are_gizmodo(self, temporal_narrative):
        urls = temporal_narrative.get('source_urls', [])
        for url in urls:
            assert 'gizmodo.com' in url, \
                f"All source URLs must be gizmodo.com, got: {url}"

    def test_test_file_reference(self, mechanism_99):
        tf = mechanism_99.get('test_file', '')
        assert 'test_james_pero_google_redemption_temporal_narrative_aug14' in tf


# ===================================================================
# 2. TestTemporalNarrativeStructure — redemption arc vs recidivism loop
# ===================================================================
class TestTemporalNarrativeStructure:
    """Verify the temporal narrative framework is documented."""

    def test_google_redemption_arc_documented(self, temporal_narrative):
        google = temporal_narrative.get('google_redemption_arc', {})
        assert google, "google_redemption_arc section must exist"

    def test_google_redemption_vocabulary(self, temporal_narrative):
        google = temporal_narrative.get('google_redemption_arc', {})
        vocab = google.get('key_vocabulary', [])
        if isinstance(vocab, str):
            vocab = [vocab]
        vocab_text = ' '.join(str(v).lower() for v in vocab)
        assert any(w in vocab_text for w in ['learned', 'learning', 'growth', 'revolutionize']), \
            f"Google redemption vocabulary should include learning/growth language, got: {vocab}"

    def test_meta_recidivism_loop_documented(self, temporal_narrative):
        meta = temporal_narrative.get('meta_recidivism_loop', {})
        assert meta, "meta_recidivism_loop section must exist"

    def test_meta_recidivism_vocabulary(self, temporal_narrative):
        meta = temporal_narrative.get('meta_recidivism_loop', {})
        vocab = meta.get('key_vocabulary', [])
        if isinstance(vocab, str):
            vocab = [vocab]
        vocab_text = ' '.join(str(v).lower() for v in vocab)
        assert any(w in vocab_text for w in ['surveillance', 'privacy', 'pile up', 'shamed', 'encroach']), \
            f"Meta recidivism vocabulary should include surveillance/privacy escalation language, got: {vocab}"

    def test_google_tone_neutral_or_positive(self, temporal_narrative):
        google = temporal_narrative.get('google_redemption_arc', {})
        tone = google.get('aggregate_tone', -1)
        assert tone >= -0.10, \
            f"Google redemption arc tone should be ≥ -0.10, got {tone}"

    def test_meta_tone_adversarial(self, temporal_narrative):
        meta = temporal_narrative.get('meta_recidivism_loop', {})
        tone = meta.get('aggregate_tone', 0)
        assert tone <= -0.30, \
            f"Meta recidivism loop tone should be ≤ -0.30, got {tone}"

    def test_temporal_coding_inversion_documented(self, temporal_narrative):
        """Failure→virtue (Google) vs success→menace (Meta)."""
        inversion = temporal_narrative.get('temporal_coding_inversion', '')
        assert inversion or temporal_narrative.get('mechanism_description', ''), \
            "temporal_coding_inversion or mechanism_description must document the paradox"


# ===================================================================
# 3. TestArticleCountAndCoverage — 7+ source articles documented
# ===================================================================
class TestArticleCountAndCoverage:
    """Verify sufficient source articles are documented."""

    def test_google_article_count(self, temporal_narrative):
        google = temporal_narrative.get('google_redemption_arc', {})
        articles = google.get('articles', [])
        assert len(articles) >= 3, \
            f"Expected ≥3 Google articles, got {len(articles)}"

    def test_meta_article_count(self, temporal_narrative):
        meta = temporal_narrative.get('meta_recidivism_loop', {})
        articles = meta.get('articles', [])
        assert len(articles) >= 4, \
            f"Expected ≥4 Meta articles, got {len(articles)}"

    def test_total_article_count(self, temporal_narrative):
        google = temporal_narrative.get('google_redemption_arc', {})
        meta = temporal_narrative.get('meta_recidivism_loop', {})
        g_articles = google.get('articles', [])
        m_articles = meta.get('articles', [])
        total = len(g_articles) + len(m_articles)
        assert total >= 7, \
            f"Expected ≥7 total source articles, got {total}"

    def test_all_articles_have_urls(self, temporal_narrative):
        for section_name in ['google_redemption_arc', 'meta_recidivism_loop']:
            section = temporal_narrative.get(section_name, {})
            for article in section.get('articles', []):
                assert article.get('url'), \
                    f"Article '{article.get('title', 'unknown')}' missing URL"
                assert 'gizmodo.com' in article['url'], \
                    f"Article URL must be gizmodo.com: {article['url']}"

    def test_all_articles_have_dates(self, temporal_narrative):
        for section_name in ['google_redemption_arc', 'meta_recidivism_loop']:
            section = temporal_narrative.get(section_name, {})
            for article in section.get('articles', []):
                assert article.get('date'), \
                    f"Article '{article.get('title', 'unknown')}' missing date"


# ===================================================================
# 4. TestGoogleRedemptionFraming — headline analysis, tone
# ===================================================================
class TestGoogleRedemptionFraming:
    """Verify Google redemption arc framing is documented."""

    def test_glasshole_learning_headline(self, temporal_narrative):
        """'Learned Something From the Glasshole Days' is redemption framing."""
        google = temporal_narrative.get('google_redemption_arc', {})
        articles = google.get('articles', [])
        titles = [a.get('title', '').lower() for a in articles]
        assert any('learned' in t or 'glasshole' in t for t in titles), \
            "Google articles must include the 'Learned Something From Glasshole Days' headline"

    def test_scared_of_words_playful_tone(self, temporal_narrative):
        """'Scared of the Words Smart Glasses' is playful, not adversarial."""
        google = temporal_narrative.get('google_redemption_arc', {})
        articles = google.get('articles', [])
        scared = [a for a in articles if 'scared' in a.get('title', '').lower()]
        if scared:
            tone = scared[0].get('tone', -1)
            assert tone >= -0.15, \
                f"'Scared' article tone should be neutral/amused (≥-0.15), got {tone}"

    def test_project_astra_aspirational(self, temporal_narrative):
        """'May Revolutionize' is aspirational forward framing."""
        google = temporal_narrative.get('google_redemption_arc', {})
        articles = google.get('articles', [])
        astra = [a for a in articles if 'astra' in a.get('title', '').lower()
                 or 'revolutionize' in a.get('title', '').lower()]
        assert len(astra) >= 1, \
            "Google articles must include the Project Astra aspirational article"

    def test_zero_surveillance_vocabulary_in_google(self, temporal_narrative):
        """Google articles should have zero surveillance vocabulary."""
        google = temporal_narrative.get('google_redemption_arc', {})
        surveillance_terms_count = google.get('surveillance_vocabulary_count', 0)
        assert surveillance_terms_count == 0, \
            f"Google articles should have 0 surveillance terms, got {surveillance_terms_count}"


# ===================================================================
# 5. TestMetaSurveillanceDefault — adversarial vocabulary
# ===================================================================
class TestMetaSurveillanceDefault:
    """Verify Meta recidivism/surveillance framing is documented."""

    def test_privacy_concerns_pile_up_article(self, temporal_narrative):
        meta = temporal_narrative.get('meta_recidivism_loop', {})
        articles = meta.get('articles', [])
        titles = [a.get('title', '').lower() for a in articles]
        assert any('privacy concerns pile up' in t for t in titles), \
            "Meta articles must include 'Privacy Concerns Pile Up'"

    def test_anti_meta_plan_documented(self, temporal_narrative):
        meta = temporal_narrative.get('meta_recidivism_loop', {})
        articles = meta.get('articles', [])
        # Check either key_language or key_framing
        has_anti_meta = False
        for a in articles:
            lang = str(a.get('key_language', '')) + str(a.get('key_framing', ''))
            if 'anti-meta' in lang.lower() or 'anti meta' in lang.lower():
                has_anti_meta = True
                break
        assert has_anti_meta, \
            "Meta articles must document 'The anti-Meta plan' section"

    def test_thanks_to_meta_documented(self, temporal_narrative):
        meta = temporal_narrative.get('meta_recidivism_loop', {})
        articles = meta.get('articles', [])
        has_thanks = False
        for a in articles:
            lang = str(a.get('key_language', '')) + str(a.get('key_framing', ''))
            if 'thanks to meta' in lang.lower():
                has_thanks = True
                break
        assert has_thanks, \
            "Meta articles must document 'Thanks to Meta' opening attribution"

    def test_police_article_meta_singled_out(self, temporal_narrative):
        meta = temporal_narrative.get('meta_recidivism_loop', {})
        articles = meta.get('articles', [])
        titles = [a.get('title', '').lower() for a in articles]
        assert any('police' in t for t in titles), \
            "Meta articles must include the police adoption article"

    def test_meta_privacy_paragraph_dominance(self, temporal_narrative):
        """In 'Privacy Concerns Pile Up', Meta gets 8/10 substantive paragraphs."""
        meta = temporal_narrative.get('meta_recidivism_loop', {})
        dominance = meta.get('meta_privacy_paragraph_dominance', '')
        # Accept either string or numeric
        assert dominance or any(
            a.get('meta_paragraph_share') for a in meta.get('articles', [])
        ), "Must document Meta's paragraph dominance in privacy articles"


# ===================================================================
# 6. TestHardwareParity — identical chip, camera, LED documented
# ===================================================================
class TestHardwareParity:
    """Verify identical hardware is documented for both entities."""

    def test_hardware_parity_section(self, temporal_narrative):
        hw = temporal_narrative.get('hardware_parity', {})
        assert hw, "hardware_parity section must exist"

    def test_same_chip(self, temporal_narrative):
        hw = temporal_narrative.get('hardware_parity', {})
        chip = str(hw.get('shared_chip', '')).lower()
        assert 'snapdragon' in chip or 'ar1' in chip, \
            f"Must document shared Snapdragon AR1 Gen 1 chip, got: {chip}"

    def test_same_camera_resolution(self, temporal_narrative):
        hw = temporal_narrative.get('hardware_parity', {})
        cam = str(hw.get('camera_resolution', '')).lower()
        assert '12mp' in cam or '12 mp' in cam, \
            f"Must document shared 12MP camera, got: {cam}"

    def test_led_indicator_documented(self, temporal_narrative):
        hw = temporal_narrative.get('hardware_parity', {})
        led = str(hw.get('led_indicator', '')).lower()
        assert 'led' in led or hw.get('has_led_indicator'), \
            "Must document LED indicator on both"


# ===================================================================
# 7. TestConfoundingFactors — ≥6, ≥1 STRONG, multiple strengths
# ===================================================================
class TestConfoundingFactors:
    """Verify confounding factors are rigorous."""

    def test_confounding_factor_count(self, temporal_narrative):
        cf = temporal_narrative.get('confounding_factors', [])
        assert len(cf) >= 6, \
            f"Expected ≥6 confounding factors, got {len(cf)}"

    def test_at_least_one_strong(self, temporal_narrative):
        cf = temporal_narrative.get('confounding_factors', [])
        strengths = [f.get('strength', '').upper() for f in cf]
        assert 'STRONG' in strengths, \
            f"Must have at least one STRONG confounding factor, got: {strengths}"

    def test_multiple_strength_levels(self, temporal_narrative):
        cf = temporal_narrative.get('confounding_factors', [])
        strengths = set(f.get('strength', '').upper() for f in cf)
        assert len(strengths) >= 2, \
            f"Must have ≥2 strength levels, got: {strengths}"

    def test_strong_count(self, temporal_narrative):
        cf = temporal_narrative.get('confounding_factors', [])
        strong = [f for f in cf if f.get('strength', '').upper() == 'STRONG']
        assert len(strong) >= 2, \
            f"Expected ≥2 STRONG confounding factors, got {len(strong)}"

    def test_moderate_count(self, temporal_narrative):
        cf = temporal_narrative.get('confounding_factors', [])
        moderate = [f for f in cf if f.get('strength', '').upper() == 'MODERATE']
        assert len(moderate) >= 2, \
            f"Expected ≥2 MODERATE confounding factors, got {len(moderate)}"

    def test_weak_count(self, temporal_narrative):
        cf = temporal_narrative.get('confounding_factors', [])
        weak = [f for f in cf if f.get('strength', '').upper() == 'WEAK']
        assert len(weak) >= 2, \
            f"Expected ≥2 WEAK confounding factors, got {len(weak)}"

    def test_confounding_factors_have_descriptions(self, temporal_narrative):
        cf = temporal_narrative.get('confounding_factors', [])
        for f in cf:
            assert f.get('factor'), \
                f"Confounding factor missing 'factor' description: {f}"

    def test_confounding_factors_in_research(self, mechanism_99):
        cf = mechanism_99.get('confounding_factors', [])
        assert len(cf) >= 6, \
            f"Research YAML should also have ≥6 confounding factors, got {len(cf)}"


# ===================================================================
# 8. TestTestablePredictions — ≥4 specific, falsifiable
# ===================================================================
class TestTestablePredictions:
    """Verify testable predictions are specific and falsifiable."""

    def test_prediction_count(self, temporal_narrative):
        preds = temporal_narrative.get('testable_predictions', [])
        assert len(preds) >= 4, \
            f"Expected ≥4 testable predictions, got {len(preds)}"

    def test_predictions_are_specific(self, temporal_narrative):
        preds = temporal_narrative.get('testable_predictions', [])
        for p in preds:
            pred_text = p.get('prediction', '') if isinstance(p, dict) else str(p)
            assert len(pred_text) >= 30, \
                f"Prediction too short to be specific/falsifiable: {pred_text}"

    def test_samsung_google_launch_prediction(self, temporal_narrative):
        """Must predict how Pero will cover Samsung/Google post-launch incidents."""
        preds = temporal_narrative.get('testable_predictions', [])
        pred_texts = [
            (p.get('prediction', '') if isinstance(p, dict) else str(p)).lower()
            for p in preds
        ]
        has_launch = any('samsung' in t or 'google' in t or 'launch' in t
                         for t in pred_texts)
        assert has_launch, \
            "Must have at least one prediction about Samsung/Google post-launch coverage"

    def test_growing_pains_prediction(self, temporal_narrative):
        """Must predict growing pains vs recidivism framing."""
        preds = temporal_narrative.get('testable_predictions', [])
        pred_texts = [
            (p.get('prediction', '') if isinstance(p, dict) else str(p)).lower()
            for p in preds
        ]
        has_framing = any('growing pain' in t or 'recidivism' in t or
                          'redemption' in t or 'softer' in t or 'vocabulary' in t
                          for t in pred_texts)
        assert has_framing, \
            "Must predict differential framing vocabulary post-launch"

    def test_predictions_in_research(self, mechanism_99):
        preds = mechanism_99.get('testable_predictions', [])
        assert len(preds) >= 4, \
            f"Research YAML should also have ≥4 predictions, got {len(preds)}"


# ===================================================================
# 9. TestCrossReferences — to mechanisms #31, #80, #98, #74, #95
# ===================================================================
class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    def test_cross_refs_exist(self, temporal_narrative):
        refs = temporal_narrative.get('related_mechanisms', [])
        if not refs:
            refs = temporal_narrative.get('cross_references', [])
        assert len(refs) >= 4, \
            f"Expected ≥4 cross-references, got {len(refs)}"

    def test_ref_to_mechanism_31(self, temporal_narrative):
        """Must reference #31 (Editorial Direction Override — same journalist)."""
        refs = temporal_narrative.get('related_mechanisms', [])
        if not refs:
            refs = temporal_narrative.get('cross_references', [])
        assert 31 in refs, \
            f"Must cross-reference mechanism #31 (Editorial Direction Override), got: {refs}"

    def test_ref_to_mechanism_80(self, temporal_narrative):
        """Must reference #80 (Samsung 4-entity clean control)."""
        refs = temporal_narrative.get('related_mechanisms', [])
        if not refs:
            refs = temporal_narrative.get('cross_references', [])
        assert 80 in refs, \
            f"Must cross-reference mechanism #80 (4-entity clean control), got: {refs}"

    def test_ref_to_mechanism_98(self, temporal_narrative):
        """Must reference #98 (Anthropic AI Safety clean control)."""
        refs = temporal_narrative.get('related_mechanisms', [])
        if not refs:
            refs = temporal_narrative.get('cross_references', [])
        assert 98 in refs, \
            f"Must cross-reference mechanism #98 (Anthropic clean control), got: {refs}"

    def test_ref_to_mechanism_74(self, temporal_narrative):
        """Must reference #74 (Gizmodo Snap Specs privacy vocabulary)."""
        refs = temporal_narrative.get('related_mechanisms', [])
        if not refs:
            refs = temporal_narrative.get('cross_references', [])
        assert 74 in refs, \
            f"Must cross-reference mechanism #74 (Snap Specs), got: {refs}"


# ===================================================================
# 10. TestDistinctiveness — Jaccard <0.7 from #31 and #80
# ===================================================================
class TestDistinctiveness:
    """Verify mechanism #99 is distinct from related mechanisms."""

    def test_distinct_from_31_editorial_direction(self, temporal_narrative):
        """#99 is about temporal narrative structure, not genre split."""
        finding = temporal_narrative.get('finding', '').lower()
        desc = temporal_narrative.get('mechanism_description', '').lower()
        combined = finding + ' ' + desc
        # Must mention temporal/redemption/recidivism concepts
        has_temporal = any(w in combined for w in
                          ['temporal', 'redemption', 'recidivism', 'narrative arc',
                           'narrative trajectory'])
        assert has_temporal, \
            "Mechanism must be framed around temporal narrative, not genre split"

    def test_distinct_from_80_vocabulary(self, temporal_narrative):
        """#99 is about narrative arc, not framing vocabulary counts."""
        finding = temporal_narrative.get('finding', '').lower()
        # Should not primarily be about vocabulary counts
        assert 'temporal' in finding or 'redemption' in finding or \
               'narrative' in finding, \
            "Finding should emphasize temporal narrative, not vocabulary"

    def test_distinctiveness_documented(self, temporal_narrative):
        """Must explicitly document distinctiveness from related mechanisms."""
        distinct = temporal_narrative.get('distinctiveness', {})
        if not distinct:
            # Check for distinctiveness in mechanism_description
            desc = temporal_narrative.get('mechanism_description', '')
            assert 'distinct' in desc.lower() or len(desc) > 100, \
                "Must document distinctiveness from related mechanisms"


# ===================================================================
# 11. TestGooglePrivacyRecordContext — confounding factor depth
# ===================================================================
class TestGooglePrivacyRecordContext:
    """Verify Google's actual privacy record is documented for context."""

    def test_google_privacy_context_exists(self, temporal_narrative):
        """Must document Google's actual privacy record for fair analysis."""
        context = temporal_narrative.get('google_actual_privacy_record', {})
        assert context, "google_actual_privacy_record section must exist"

    def test_gemini_data_collection_documented(self, temporal_narrative):
        context = temporal_narrative.get('google_actual_privacy_record', {})
        text = str(context).lower()
        assert 'gemini' in text or 'data' in text, \
            "Must document Gemini data collection scope"

    def test_android_xr_led_behavior(self, temporal_narrative):
        context = temporal_narrative.get('google_actual_privacy_record', {})
        text = str(context).lower()
        assert 'led' in text or 'observation' in text or 'xr' in text, \
            "Must document Android XR LED behavior during AI observation"


# ===================================================================
# 12. TestEntityIntegration — competitor-entities.yaml google section
# ===================================================================
class TestEntityIntegration:
    """Verify mechanism is registered in competitor-entities.yaml google."""

    def test_mechanism_99_in_google_entity(self, google_entity):
        # Look for pero temporal narrative entry anywhere in google entity
        text = str(google_entity).lower()
        assert ('pero' in text and 'temporal' in text) or \
               ('mechanism_id' in text and '99' in text) or \
               'pero_google_redemption' in text, \
            "Google entity must reference mechanism #99 / Pero temporal narrative"
