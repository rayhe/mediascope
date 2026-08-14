"""
Gizmodo Equitable Adversarial Coverage of OpenAI Hardware Litigation —
Clean Control Cross-Entity Validation

Type A: Competitor Coverage Deep Dive (Aug 14, 2026 05:00 PT)
Mechanism #96: Gizmodo OpenAI Hardware Litigation Clean Control Coverage Validation

Finding: Gizmodo (Keleops AG, zero financial ties to any tech company) produced 5+
standalone articles covering OpenAI's hardware device and the Apple vs OpenAI
trade-secret lawsuit (Jul 10 - Aug 6, 2026), applying consistent skepticism and
adversarial framing. WIRED (Condé Nast, OpenAI content deal since Aug 2024) produced
zero identifiable standalone wired.com articles covering the Apple vs OpenAI
trade-secret lawsuit over the same period, despite this being one of the biggest
tech legal stories of 2026 (400+ poached employees, systematic hardware IP theft
allegations, supplier fraud claims, preliminary injunction filed).

This extends Gizmodo's clean-control pattern from hardware/privacy (mechanism #80)
into the litigation/ethics domain. Gizmodo covers BOTH Meta (tone -0.75) AND OpenAI
(tone ~-0.35) adversarially, confirming equitable editorial standards. WIRED's
absence from covering OpenAI's actual legal scandal while actively covering Meta
(Ashworth "Is It Possible to Make Smart Glasses That Aren't Creepy?" Aug 2) confirms
financial relationship predicts coverage selectivity.

Distinct from:
- #80 (Gizmodo 4-entity clean control): Hardware/privacy vocabulary comparison
- #84 (WIRED OpenAI hardware FR investigation gap): Privacy investigation gap
- #96 (this): LITIGATION/ETHICS coverage gap — WIRED's absence from covering
  OpenAI's actual legal scandal while actively covering Meta

6 confounding factors (2 STRONG, 2 MODERATE, 2 WEAK).
4 testable predictions.
5 cross-references (#80, #84, #48, #58, #82).
"""

import yaml
import os
import pytest

PROFILE_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
GIZMODO_PATH = os.path.join(PROFILE_DIR, 'gizmodo.yaml')
WIRED_PATH = os.path.join(PROFILE_DIR, 'wired.yaml')
RESEARCH_PATH = os.path.join(PROFILE_DIR, 'competitor-coverage-research.yaml')
ENTITIES_PATH = os.path.join(PROFILE_DIR, 'competitor-entities.yaml')


@pytest.fixture(scope='module')
def gizmodo_profile():
    with open(GIZMODO_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def wired_profile():
    with open(WIRED_PATH) as f:
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
def gizmodo_openai_litigation(gizmodo_profile):
    cross = gizmodo_profile.get('cross_entity_coverage', {})
    section = cross.get('openai_hardware_litigation_coverage')
    assert section is not None, (
        "Missing openai_hardware_litigation_coverage in gizmodo.yaml cross_entity_coverage"
    )
    return section


@pytest.fixture(scope='module')
def wired_lawsuit_gap(wired_profile):
    cea = wired_profile.get('cross_entity_coverage_analysis', {})
    rogue = cea.get('rogue_ai_coverage_volume_asymmetry', {})
    section = rogue.get('apple_openai_lawsuit_coverage_gap')
    assert section is not None, (
        "Missing apple_openai_lawsuit_coverage_gap in wired.yaml "
        "cross_entity_coverage_analysis.rogue_ai_coverage_volume_asymmetry"
    )
    return section


@pytest.fixture(scope='module')
def mechanism_96(research_data):
    findings = research_data.get('cross_publication_findings', {})
    section = findings.get('gizmodo_openai_litigation_clean_control_coverage_validation')
    assert section is not None, (
        "Missing gizmodo_openai_litigation_clean_control_coverage_validation in "
        "competitor-coverage-research.yaml cross_publication_findings"
    )
    return section


# -- Class 1: Gizmodo OpenAI Article Count and Structure -----------------------


class TestGizmodoOpenAIArticleCount:
    """Verify Gizmodo produced 5+ standalone OpenAI hardware/litigation articles."""

    def test_section_exists(self, gizmodo_openai_litigation):
        assert gizmodo_openai_litigation is not None

    def test_mechanism_id(self, gizmodo_openai_litigation):
        assert gizmodo_openai_litigation.get('mechanism_id') == 96

    def test_minimum_article_count(self, gizmodo_openai_litigation):
        articles = gizmodo_openai_litigation.get('articles', [])
        assert len(articles) >= 5, f"Expected >= 5 articles, got {len(articles)}"

    def test_articles_span_feb_to_aug_2026(self, gizmodo_openai_litigation):
        articles = gizmodo_openai_litigation.get('articles', [])
        dates = [a.get('date', '') for a in articles]
        has_early = any('2026-02' in d for d in dates)
        has_late = any('2026-08' in d or '2026-07' in d for d in dates)
        assert has_early, "Expected at least one article from Feb 2026"
        assert has_late, "Expected at least one article from Jul or Aug 2026"

    def test_all_articles_have_urls(self, gizmodo_openai_litigation):
        articles = gizmodo_openai_litigation.get('articles', [])
        for a in articles:
            url = a.get('url', '')
            assert url.startswith('https://gizmodo.com/'), (
                f"Invalid or missing URL for article: {a.get('title', 'unknown')}"
            )

    def test_all_articles_have_titles(self, gizmodo_openai_litigation):
        articles = gizmodo_openai_litigation.get('articles', [])
        for a in articles:
            assert len(a.get('title', '')) > 10, (
                f"Missing or too-short title: {a.get('title', '')}"
            )

    def test_smart_speaker_article_present(self, gizmodo_openai_litigation):
        """The 'no one asked for' smart speaker article should be present."""
        articles = gizmodo_openai_litigation.get('articles', [])
        titles = [a.get('title', '').lower() for a in articles]
        assert any('smart speaker' in t or 'no one asked' in t for t in titles)

    def test_apple_lawsuit_day_of_article(self, gizmodo_openai_litigation):
        """Gizmodo covered the Apple lawsuit day-of (Jul 10)."""
        articles = gizmodo_openai_litigation.get('articles', [])
        has_jul10 = any(
            '2026-07-10' in a.get('date', '') and 'lawsuit' in a.get('title', '').lower()
            for a in articles
        )
        assert has_jul10, "Missing day-of Apple lawsuit coverage (Jul 10, 2026)"


# -- Class 2: Gizmodo OpenAI Tone Verification ---------------------------------


class TestGizmodoOpenAITone:
    """Verify Gizmodo's OpenAI coverage tone is adversarial/skeptical (~-0.35)."""

    def test_openai_tone_negative(self, gizmodo_openai_litigation):
        tone = gizmodo_openai_litigation.get('aggregate_tone', 0)
        assert tone < 0, f"Expected negative tone, got {tone}"

    def test_openai_tone_range(self, gizmodo_openai_litigation):
        tone = gizmodo_openai_litigation.get('aggregate_tone', 0)
        assert -0.55 <= tone <= -0.15, (
            f"OpenAI tone {tone} outside expected range [-0.55, -0.15]"
        )

    def test_articles_contain_skeptical_language(self, gizmodo_openai_litigation):
        articles = gizmodo_openai_litigation.get('articles', [])
        all_language = ' '.join(
            a.get('key_language', '') for a in articles
        ).lower()
        skeptical_markers = [
            'no one asked', 'zero points', 'inane', 'shame',
            'trying to shame', 'run out of ideas'
        ]
        found = [m for m in skeptical_markers if m in all_language]
        assert len(found) >= 2, (
            f"Expected >= 2 skeptical language markers, found: {found}"
        )


# -- Class 3: Gizmodo Cross-Entity Comparison (OpenAI vs Meta) ----------------


class TestGizmodoEquitableCoverage:
    """Verify Gizmodo covers BOTH Meta and OpenAI with adversarial framing."""

    def test_meta_tone_recorded(self, gizmodo_openai_litigation):
        comparison = gizmodo_openai_litigation.get('cross_entity_comparison', {})
        meta_tone = comparison.get('meta_tone', 0)
        assert meta_tone <= -0.60, f"Meta tone {meta_tone} should be <= -0.60"

    def test_openai_tone_recorded(self, gizmodo_openai_litigation):
        comparison = gizmodo_openai_litigation.get('cross_entity_comparison', {})
        openai_tone = comparison.get('openai_tone', 0)
        assert openai_tone < 0, f"OpenAI tone {openai_tone} should be negative"

    def test_both_entities_adversarial(self, gizmodo_openai_litigation):
        comparison = gizmodo_openai_litigation.get('cross_entity_comparison', {})
        meta_tone = comparison.get('meta_tone', 0)
        openai_tone = comparison.get('openai_tone', 0)
        assert meta_tone < 0 and openai_tone < 0, (
            "Both entities should receive adversarial (negative) framing at Gizmodo"
        )

    def test_meta_more_adversarial_than_openai(self, gizmodo_openai_litigation):
        """Meta receives MORE adversarial coverage, but both are negative."""
        comparison = gizmodo_openai_litigation.get('cross_entity_comparison', {})
        meta_tone = comparison.get('meta_tone', 0)
        openai_tone = comparison.get('openai_tone', 0)
        assert meta_tone < openai_tone, (
            f"Meta tone ({meta_tone}) should be more adversarial than OpenAI ({openai_tone})"
        )

    def test_equitable_finding_documented(self, gizmodo_openai_litigation):
        comparison = gizmodo_openai_litigation.get('cross_entity_comparison', {})
        finding = comparison.get('equitable_finding', '')
        assert 'equitable' in finding.lower() or 'both' in finding.lower()


# -- Class 4: WIRED Apple-OpenAI Lawsuit Coverage Gap -------------------------


class TestWIREDLawsuitCoverageGap:
    """Verify WIRED produced zero standalone wired.com articles on Apple vs OpenAI lawsuit."""

    def test_wired_gap_section_exists(self, wired_lawsuit_gap):
        assert wired_lawsuit_gap is not None

    def test_wired_standalone_article_count_zero(self, wired_lawsuit_gap):
        count = wired_lawsuit_gap.get('standalone_wired_articles', -1)
        assert count == 0, f"Expected 0 standalone WIRED articles, got {count}"

    def test_wired_gap_date_range(self, wired_lawsuit_gap):
        start = wired_lawsuit_gap.get('observation_start', '')
        end = wired_lawsuit_gap.get('observation_end', '')
        assert '2026-07-10' in start
        assert '2026-08-14' in end or '2026-08' in end

    def test_paresh_dave_podcast_documented(self, wired_lawsuit_gap):
        """Paresh Dave discussed the lawsuit on Marketplace, NOT a WIRED article."""
        podcast = wired_lawsuit_gap.get('paresh_dave_marketplace_appearance', {})
        assert podcast.get('is_wired_article') is False

    def test_wired_meta_coverage_during_same_period(self, wired_lawsuit_gap):
        """WIRED published adversarial Meta coverage in the same window."""
        meta = wired_lawsuit_gap.get('concurrent_meta_coverage', {})
        assert meta.get('article_count', 0) >= 1

    def test_ashworth_meta_article_documented(self, wired_lawsuit_gap):
        """Boone Ashworth's 'Is It Possible to Make Smart Glasses That Aren't Creepy?' (Aug 2)."""
        meta = wired_lawsuit_gap.get('concurrent_meta_coverage', {})
        examples = meta.get('examples', [])
        titles = [e.get('title', '').lower() for e in examples]
        assert any('creepy' in t or 'ashworth' in str(e.get('author', '')).lower()
                    for e in examples for t in [e.get('title', '').lower()])


# -- Class 5: WIRED-Gizmodo Coverage Gap Quantification -----------------------


class TestWIREDGizmodoCoverageGap:
    """Quantify the coverage gap between WIRED (0 articles) and Gizmodo (5+ articles)."""

    def test_gizmodo_count_at_least_5(self, mechanism_96):
        giz = mechanism_96.get('gizmodo_article_count', 0)
        assert giz >= 5, f"Gizmodo count {giz} < 5"

    def test_wired_count_zero(self, mechanism_96):
        wired = mechanism_96.get('wired_lawsuit_article_count', 0)
        assert wired == 0, f"WIRED count {wired} should be 0"

    def test_coverage_gap_documented(self, mechanism_96):
        gap = mechanism_96.get('coverage_gap', '')
        assert gap or mechanism_96.get('finding_summary', '')

    def test_other_outlets_covered(self, mechanism_96):
        """10+ other outlets covered the lawsuit — WIRED's silence is anomalous."""
        others = mechanism_96.get('other_outlets_covering_lawsuit', [])
        assert len(others) >= 5, f"Expected >= 5 other outlets, got {len(others)}"


# -- Class 6: Financial Relationship Prediction --------------------------------


class TestFinancialRelationshipPrediction:
    """Verify financial relationship predicts coverage selectivity."""

    def test_wired_openai_deal_documented(self, mechanism_96):
        financial = mechanism_96.get('financial_relationships', {})
        wired_openai = financial.get('wired_openai_deal', '')
        assert 'condé nast' in wired_openai.lower() or 'conde nast' in wired_openai.lower() or \
               'content deal' in wired_openai.lower() or '2024' in wired_openai

    def test_gizmodo_zero_financial_ties(self, mechanism_96):
        financial = mechanism_96.get('financial_relationships', {})
        gizmodo_ties = financial.get('gizmodo_financial_ties', '')
        assert 'none' in gizmodo_ties.lower() or 'zero' in gizmodo_ties.lower()

    def test_financial_predicts_coverage(self, mechanism_96):
        financial = mechanism_96.get('financial_relationships', {})
        prediction = financial.get('coverage_prediction', '')
        assert len(prediction) > 20, "Financial coverage prediction should be documented"

    def test_gizmodo_owner_documented(self, mechanism_96):
        financial = mechanism_96.get('financial_relationships', {})
        owner = financial.get('gizmodo_owner', '')
        assert 'keleops' in owner.lower()


# -- Class 7: Confounding Factors (6, STRONG/MODERATE/WEAK) --------------------


class TestConfoundingFactors:
    """Verify 6 confounding factors with proper strength labels."""

    def test_six_confounding_factors(self, mechanism_96):
        factors = mechanism_96.get('confounding_factors', [])
        assert len(factors) >= 6, f"Expected >= 6 confounding factors, got {len(factors)}"

    def test_factors_have_strength_labels(self, mechanism_96):
        factors = mechanism_96.get('confounding_factors', [])
        for f in factors:
            strength = f.get('strength', '')
            assert strength in ('STRONG', 'MODERATE', 'WEAK'), (
                f"Factor missing valid strength label: {f.get('factor', '')[:60]}"
            )

    def test_two_strong_factors(self, mechanism_96):
        factors = mechanism_96.get('confounding_factors', [])
        strong = [f for f in factors if f.get('strength') == 'STRONG']
        assert len(strong) == 2, f"Expected 2 STRONG factors, got {len(strong)}"

    def test_two_moderate_factors(self, mechanism_96):
        factors = mechanism_96.get('confounding_factors', [])
        moderate = [f for f in factors if f.get('strength') == 'MODERATE']
        assert len(moderate) == 2, f"Expected 2 MODERATE factors, got {len(moderate)}"

    def test_two_weak_factors(self, mechanism_96):
        factors = mechanism_96.get('confounding_factors', [])
        weak = [f for f in factors if f.get('strength') == 'WEAK']
        assert len(weak) == 2, f"Expected 2 WEAK factors, got {len(weak)}"

    def test_beat_assignment_confound_present(self, mechanism_96):
        factors = mechanism_96.get('confounding_factors', [])
        text = ' '.join(f.get('factor', '') for f in factors).lower()
        assert 'beat' in text or 'reporter' in text or 'assignment' in text

    def test_editorial_bandwidth_confound_present(self, mechanism_96):
        factors = mechanism_96.get('confounding_factors', [])
        text = ' '.join(f.get('factor', '') for f in factors).lower()
        assert 'bandwidth' in text or 'busy' in text or 'timing' in text


# -- Class 8: Testable Predictions (4) ----------------------------------------


class TestTestablePredictions:
    """Verify 4 specific, falsifiable testable predictions."""

    def test_four_predictions(self, mechanism_96):
        preds = mechanism_96.get('testable_predictions', [])
        assert len(preds) >= 4, f"Expected >= 4 predictions, got {len(preds)}"

    def test_hardware_device_announcement_prediction(self, mechanism_96):
        """When OpenAI announces hardware device, WIRED will cover product but not IP provenance."""
        preds = mechanism_96.get('testable_predictions', [])
        text = ' '.join(p if isinstance(p, str) else p.get('prediction', '') for p in preds).lower()
        assert 'hardware' in text and ('provenance' in text or 'trade' in text or 'investigate' in text)

    def test_gizmodo_volume_prediction(self, mechanism_96):
        """Gizmodo will produce more adversarial OpenAI hardware coverage than WIRED."""
        preds = mechanism_96.get('testable_predictions', [])
        text = ' '.join(p if isinstance(p, str) else p.get('prediction', '') for p in preds).lower()
        assert 'gizmodo' in text and ('volume' in text or 'more' in text or 'adversarial' in text)

    def test_discovery_revelations_prediction(self, mechanism_96):
        """If discovery reveals damaging info, deal-holding publications will lag Gizmodo."""
        preds = mechanism_96.get('testable_predictions', [])
        text = ' '.join(p if isinstance(p, str) else p.get('prediction', '') for p in preds).lower()
        assert 'discovery' in text or 'lag' in text or 'speed' in text

    def test_wired_review_framing_prediction(self, mechanism_96):
        """WIRED's first OpenAI hardware review will use neutral/aspirational framing."""
        preds = mechanism_96.get('testable_predictions', [])
        text = ' '.join(p if isinstance(p, str) else p.get('prediction', '') for p in preds).lower()
        assert 'review' in text or 'aspirational' in text or 'neutral' in text


# -- Class 9: Mechanism Distinctiveness from #80, #84, #48 ---------------------


class TestMechanismDistinctiveness:
    """Verify mechanism #96 is distinct from related mechanisms."""

    def test_distinct_from_mechanism_80(self, mechanism_96):
        """#80 covers hardware/privacy vocabulary; #96 covers litigation/ethics coverage gap."""
        summary = mechanism_96.get('finding_summary', '')
        assert 'litigation' in summary.lower() or 'ethics' in summary.lower() or \
               'lawsuit' in summary.lower()

    def test_distinct_from_mechanism_84(self, mechanism_96):
        """#84 covers FR investigation gap; #96 covers trade-secret lawsuit coverage gap."""
        summary = mechanism_96.get('finding_summary', '')
        assert 'trade' in summary.lower() or 'apple' in summary.lower() or \
               'lawsuit' in summary.lower()

    def test_domain_is_litigation_ethics(self, mechanism_96):
        domain = mechanism_96.get('domain', '')
        assert 'litigation' in domain.lower() or 'ethics' in domain.lower()

    def test_mechanism_96_in_research(self, mechanism_96):
        assert mechanism_96.get('mechanism_id') == 96


# -- Class 10: Cross-References -----------------------------------------------


class TestCrossReferences:
    """Verify cross-references to #80, #84, #48, #58, #82."""

    def test_references_mechanism_80(self, mechanism_96):
        refs = mechanism_96.get('cross_references', [])
        ref_text = str(refs).lower()
        assert '#80' in ref_text or '80' in str([
            r.get('mechanism_id', '') for r in refs if isinstance(r, dict)
        ])

    def test_references_mechanism_84(self, mechanism_96):
        refs = mechanism_96.get('cross_references', [])
        ref_text = str(refs).lower()
        assert '#84' in ref_text or '84' in str([
            r.get('mechanism_id', '') for r in refs if isinstance(r, dict)
        ])

    def test_references_mechanism_48(self, mechanism_96):
        refs = mechanism_96.get('cross_references', [])
        ref_text = str(refs).lower()
        assert '#48' in ref_text or '48' in str([
            r.get('mechanism_id', '') for r in refs if isinstance(r, dict)
        ])

    def test_references_mechanism_58(self, mechanism_96):
        refs = mechanism_96.get('cross_references', [])
        ref_text = str(refs).lower()
        assert '#58' in ref_text or '58' in str([
            r.get('mechanism_id', '') for r in refs if isinstance(r, dict)
        ])

    def test_references_mechanism_82(self, mechanism_96):
        refs = mechanism_96.get('cross_references', [])
        ref_text = str(refs).lower()
        assert '#82' in ref_text or '82' in str([
            r.get('mechanism_id', '') for r in refs if isinstance(r, dict)
        ])


# -- Class 11: Source URLs Verification ----------------------------------------


class TestSourceURLs:
    """Verify source URLs are present and properly formatted."""

    def test_source_urls_present(self, mechanism_96):
        urls = mechanism_96.get('source_urls', [])
        assert len(urls) >= 5, f"Expected >= 5 source URLs, got {len(urls)}"

    def test_gizmodo_urls_present(self, mechanism_96):
        urls = mechanism_96.get('source_urls', [])
        gizmodo_urls = [u for u in urls if 'gizmodo.com' in u]
        assert len(gizmodo_urls) >= 4, f"Expected >= 4 Gizmodo URLs, got {len(gizmodo_urls)}"

    def test_all_urls_valid_format(self, mechanism_96):
        urls = mechanism_96.get('source_urls', [])
        for url in urls:
            assert url.startswith('https://'), f"URL must start with https://: {url}"

    def test_openai_litigation_coverage_in_entities(self, entities_data):
        """Verify OpenAI entity in competitor-entities.yaml has litigation coverage analysis."""
        openai = entities_data.get('entities', {}).get('openai', {})
        litigation = openai.get('apple_partnership_collapse', {})
        coverage_analysis = openai.get('litigation_coverage_analysis', {})
        assert litigation or coverage_analysis, (
            "OpenAI entity should have apple_partnership_collapse or litigation_coverage_analysis"
        )

    def test_mechanism_96_test_file(self, mechanism_96):
        tf = mechanism_96.get('test_file', '')
        assert 'gizmodo_openai_litigation_clean_control_coverage_validation_aug14' in tf
