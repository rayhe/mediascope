"""
Type C: Financial Incentive Mapping — Safe Target Coefficient Quantification
Date: 2026-08-08 18:00 PT

KEY FINDING: The binary presence/absence of a Meta financial relationship predicts
coverage direction with 100% accuracy across all 9 profiled publishers. 8/8 publishers
with zero Meta deals produce adversarial Meta coverage. The ONE publisher with a Meta
deal (News Corp, $50M/yr) produces balanced coverage.

Within the zero-Meta-deal group, competitor deal count shows weak positive correlation
with asymmetry score (r ≈ 0.52), but the binary predictor is far more powerful.

SAFE TARGET COEFFICIENT FRAMEWORK:
- Binary predictor: meta_deal = 0 → adversarial (100% accuracy)
- Gradient predictor: competitor_deals × direction (r ≈ 0.52)
- Controls: Gizmodo (zero deals, still adversarial = editorial culture baseline)
            News Corp (symmetric deals, balanced = financial symmetry control)

Sources:
- Digiday Q1 AI licensing revenue: https://digiday.com/media/media-briefing-publishers-cautiously-count-ai-licensing-as-notable-revenue-amid-programmatic-strain-in-q1-earnings/
- USA Today AI deals revenue: https://digiday.com/media/usa-today-co-s-ai-licensing-deals-drive-notable-revenue-in-q1-despite-pressure-on-traffic-and-programmatic/
- Digiday 2025 AI deal timeline: https://digiday.com/media/a-timeline-of-the-major-deals-between-publishers-and-ai-tech-companies-in-2025/
- FT-OpenAI deal: https://www.reuters.com/technology/financial-times-openai-sign-content-licensing-partnership-2024-04-29/?utm
- Meta publisher deals (Dec 2025): https://www.reuters.com/business/meta-strikes-multiple-ai-deals-with-news-publishers-axios-reports-2025-12-05/
- News Corp-Meta deal ($50M/yr): https://www.wsj.com/business/media/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year-d4fbf244
"""

import pytest
import yaml
import os


PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture(scope="module")
def competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def matrix(competitor_entities):
    return competitor_entities['meta_ai_deals']['aggregate_incentive_matrix']


@pytest.fixture(scope="module")
def publications(matrix):
    return matrix['publications']


@pytest.fixture(scope="module")
def safe_target(matrix):
    return matrix['safe_target_quantification']


# =====================================================================
# CLASS 1: Publication Data Completeness
# =====================================================================

class TestPublicationDataCompleteness:
    """Every publication in the matrix must have asymmetry_score and meta_avg_tone."""

    def test_publication_count(self, publications):
        """Matrix must contain exactly 8 profiled publications."""
        assert len(publications) == 8

    def test_all_have_asymmetry_score(self, publications):
        """Every publication must have a numeric asymmetry_score."""
        for pub in publications:
            assert 'asymmetry_score' in pub, f"{pub['name']} missing asymmetry_score"
            assert isinstance(pub['asymmetry_score'], (int, float)), \
                f"{pub['name']} asymmetry_score must be numeric"

    def test_all_have_meta_avg_tone(self, publications):
        """Every publication must have a numeric meta_avg_tone."""
        for pub in publications:
            assert 'meta_avg_tone' in pub, f"{pub['name']} missing meta_avg_tone"
            assert isinstance(pub['meta_avg_tone'], (int, float)), \
                f"{pub['name']} meta_avg_tone must be numeric"

    def test_all_have_asymmetry_source(self, publications):
        """Every publication must cite the source of its asymmetry score."""
        for pub in publications:
            assert 'asymmetry_source' in pub, f"{pub['name']} missing asymmetry_source"
            assert len(pub['asymmetry_source']) > 20, \
                f"{pub['name']} asymmetry_source too short to be meaningful"

    def test_asymmetry_scores_in_valid_range(self, publications):
        """Asymmetry scores must be between 0 and 1."""
        for pub in publications:
            score = pub['asymmetry_score']
            assert 0 <= score <= 1, \
                f"{pub['name']} asymmetry_score {score} outside [0, 1]"

    def test_meta_avg_tone_in_valid_range(self, publications):
        """Meta average tone must be between -1 and +1."""
        for pub in publications:
            tone = pub['meta_avg_tone']
            assert -1 <= tone <= 1, \
                f"{pub['name']} meta_avg_tone {tone} outside [-1, +1]"

    def test_all_meta_tones_negative(self, publications):
        """All profiled publications must have negative Meta tone (adversarial)."""
        for pub in publications:
            assert pub['meta_avg_tone'] < 0, \
                f"{pub['name']} meta_avg_tone {pub['meta_avg_tone']} is not negative"


# =====================================================================
# CLASS 2: Binary Predictor Validation
# =====================================================================

class TestBinaryPredictor:
    """The meta_deal presence/absence must predict coverage direction."""

    def test_binary_predictor_section_exists(self, safe_target):
        assert 'binary_predictor' in safe_target

    def test_meta_deal_absent_all_adversarial(self, publications):
        """All publications with meta_deals=0 must have adversarial_meta_coverage=true."""
        zero_meta = [p for p in publications if p['meta_deals'] == 0]
        assert len(zero_meta) == 8
        for pub in zero_meta:
            assert pub['adversarial_meta_coverage'] is True, \
                f"{pub['name']} has zero Meta deals but not adversarial"

    def test_prediction_accuracy_100_percent(self, safe_target):
        """Binary predictor must claim 9/9 accuracy."""
        bp = safe_target['binary_predictor']
        assert '9/9' in bp['prediction_accuracy']
        assert '100%' in bp['prediction_accuracy']

    def test_meta_deal_present_publisher_is_news_corp(self, safe_target):
        """Only News Corp should be in the meta_deal_present group."""
        present = safe_target['binary_predictor']['meta_deal_present']
        assert 'News Corp' in present['publishers']
        assert len(present['publishers']) == 1

    def test_meta_deal_absent_count(self, safe_target):
        """8 publishers in the meta_deal_absent group."""
        absent = safe_target['binary_predictor']['meta_deal_absent']
        assert len(absent['publishers']) == 8

    def test_mean_asymmetry_calculated(self, safe_target):
        """Mean asymmetry for meta_deal_absent group must be documented."""
        absent = safe_target['binary_predictor']['meta_deal_absent']
        assert 'mean_asymmetry' in absent
        assert 0.6 <= absent['mean_asymmetry'] <= 0.8

    def test_mean_asymmetry_matches_data(self, publications, safe_target):
        """Mean asymmetry must match actual publication data."""
        scores = [p['asymmetry_score'] for p in publications]
        actual_mean = sum(scores) / len(scores)
        claimed_mean = safe_target['binary_predictor']['meta_deal_absent']['mean_asymmetry']
        assert abs(actual_mean - claimed_mean) < 0.05, \
            f"Claimed mean {claimed_mean} vs actual {actual_mean:.2f}"


# =====================================================================
# CLASS 3: Competitor Deal Gradient
# =====================================================================

class TestCompetitorDealGradient:
    """Validate the competitor_deals × asymmetry correlation."""

    def test_gradient_section_exists(self, safe_target):
        assert 'competitor_deal_gradient' in safe_target

    def test_data_points_count(self, safe_target):
        """Gradient must include all 8 publications."""
        dp = safe_target['competitor_deal_gradient']['data_points']
        assert len(dp) == 8

    def test_pearson_r_documented(self, safe_target):
        """Pearson correlation coefficient must be documented."""
        r = safe_target['competitor_deal_gradient']['pearson_r']
        assert isinstance(r, (int, float))
        assert 0 < r < 1  # positive but not perfect

    def test_pearson_r_moderate(self, safe_target):
        """Correlation should be moderate (0.3-0.7), not strong."""
        r = safe_target['competitor_deal_gradient']['pearson_r']
        assert 0.3 <= r <= 0.7, \
            f"Pearson r={r} outside moderate range; binary predictor should be stronger"

    def test_data_points_match_publications(self, publications, safe_target):
        """Gradient data points must match publication data exactly."""
        dp = safe_target['competitor_deal_gradient']['data_points']
        dp_dict = {d['publisher']: d for d in dp}
        # Map full names to gradient short names
        name_map = {
            'WIRED (Condé Nast)': 'WIRED',
            'The Verge (Vox Media)': 'The Verge',
            'The Atlantic (Emerson Collective)': 'The Atlantic',
            'NYT': 'NYT',
            'Financial Times (Nikkei)': 'FT',
            'The Guardian': 'The Guardian',
            'MIT Technology Review': 'MIT TR',
            'Gizmodo (Keleops AG)': 'Gizmodo',
        }
        for pub in publications:
            short_name = name_map.get(pub['name'], pub['name'].split(' (')[0])
            assert short_name in dp_dict, f"{short_name} missing from gradient data"
            assert dp_dict[short_name]['competitor_deals'] == pub['competitor_deals']
            assert abs(dp_dict[short_name]['asymmetry'] - pub['asymmetry_score']) < 0.01

    def test_wired_highest_deals(self, safe_target):
        """WIRED (5 deals) must have the highest competitor deal count."""
        dp = safe_target['competitor_deal_gradient']['data_points']
        max_deals = max(d['competitor_deals'] for d in dp)
        wired = [d for d in dp if d['publisher'] == 'WIRED'][0]
        assert wired['competitor_deals'] == max_deals

    def test_gizmodo_lowest_deals(self, safe_target):
        """Gizmodo (0 deals) must have the lowest competitor deal count."""
        dp = safe_target['competitor_deal_gradient']['data_points']
        gizmodo = [d for d in dp if d['publisher'] == 'Gizmodo'][0]
        assert gizmodo['competitor_deals'] == 0

    def test_ft_is_asymmetry_outlier(self, safe_target):
        """FT must have the highest asymmetry despite having only 3 deals."""
        dp = safe_target['competitor_deal_gradient']['data_points']
        ft = [d for d in dp if d['publisher'] == 'FT'][0]
        max_asym = max(d['asymmetry'] for d in dp)
        assert ft['asymmetry'] == max_asym, \
            "FT should be the highest-asymmetry publication"
        assert ft['competitor_deals'] < 5, \
            "FT is an outlier because it has fewer deals than WIRED but higher asymmetry"


# =====================================================================
# CLASS 4: Control Group Analysis
# =====================================================================

class TestControlGroups:
    """Validate the two control groups (News Corp symmetric, Gizmodo zero-deal)."""

    def test_control_section_exists(self, safe_target):
        assert 'control_group_analysis' in safe_target

    def test_news_corp_symmetric_control(self, safe_target):
        """News Corp must be documented as symmetric control."""
        nc = safe_target['control_group_analysis']['news_corp_symmetric_control']
        assert nc['meta_deals'] == 1
        assert nc['openai_deals'] == 1
        assert nc['topic_dependent'] is True

    def test_news_corp_asymmetry_topic_dependent(self, safe_target):
        """News Corp asymmetry must be labeled topic-dependent, not systematic."""
        nc = safe_target['control_group_analysis']['news_corp_symmetric_control']
        assert nc['topic_dependent'] is True
        assert 'Mechanism #9' in nc['finding']

    def test_gizmodo_zero_deal_control(self, safe_target):
        """Gizmodo must be documented as zero-deal control."""
        gz = safe_target['control_group_analysis']['gizmodo_zero_deal_control']
        assert gz['meta_deals'] == 0
        assert gz['competitor_deals'] == 0
        assert gz['asymmetry'] == 0.55

    def test_gizmodo_lowest_asymmetry(self, safe_target):
        """Gizmodo (zero deals) must have the lowest asymmetry score."""
        gz = safe_target['control_group_analysis']['gizmodo_zero_deal_control']
        dp = safe_target['competitor_deal_gradient']['data_points']
        min_asym = min(d['asymmetry'] for d in dp)
        assert gz['asymmetry'] == min_asym

    def test_safe_target_delta_documented(self, safe_target):
        """Safe target delta (premium) range must be documented."""
        delta = safe_target['control_group_analysis']['safe_target_delta']
        assert 'description' in delta
        assert '0.25' in delta['description']  # Gizmodo baseline
        assert 'WIRED' in delta['description']  # highest premium


# =====================================================================
# CLASS 5: Source URL Completeness
# =====================================================================

class TestSourceUrls:
    """All claims must be backed by source URLs."""

    def test_safe_target_has_sources(self, safe_target):
        """Safe target quantification must have source URLs."""
        assert 'source_urls' in safe_target
        assert len(safe_target['source_urls']) >= 4

    def test_source_urls_are_valid_format(self, safe_target):
        """All source URLs must be valid HTTP(S) URLs."""
        for url in safe_target['source_urls']:
            assert url.startswith('http'), f"Invalid URL: {url}"

    def test_digiday_q1_source_present(self, safe_target):
        """Must cite Digiday Q1 AI licensing revenue report."""
        urls = safe_target['source_urls']
        assert any('digiday.com' in u and 'q1' in u.lower() for u in urls), \
            "Missing Digiday Q1 AI licensing source"

    def test_meta_deals_reuters_source(self, safe_target):
        """Must cite Reuters Meta publisher deals report."""
        urls = safe_target['source_urls']
        assert any('reuters.com' in u and 'meta' in u for u in urls), \
            "Missing Reuters Meta deals source"

    def test_news_corp_meta_deal_source(self, safe_target):
        """Must cite WSJ News Corp-Meta $50M/yr deal."""
        urls = safe_target['source_urls']
        assert any('wsj.com' in u and 'news-corp' in u for u in urls), \
            "Missing WSJ News Corp-Meta deal source"


# =====================================================================
# CLASS 6: Cross-Validation With Profile Data
# =====================================================================

class TestCrossValidation:
    """Cross-validate matrix data against individual publisher profiles."""

    def test_wired_asymmetry_matches_profile(self, publications):
        """WIRED asymmetry must match Schiffer cross-entity score."""
        wired = [p for p in publications if 'WIRED' in p['name']][0]
        assert wired['asymmetry_score'] == 0.82
        assert 'Schiffer' in wired['asymmetry_source']

    def test_wired_meta_tone_matches_profile(self, publications):
        """WIRED meta_avg_tone must match Paresh Dave cross-entity data."""
        wired = [p for p in publications if 'WIRED' in p['name']][0]
        assert wired['meta_avg_tone'] == -0.51

    def test_ft_asymmetry_matches_profile(self, publications):
        """FT asymmetry must match Murgia cross-entity score."""
        ft = [p for p in publications if 'Financial Times' in p['name']][0]
        assert ft['asymmetry_score'] == 0.87
        assert 'Murgia' in ft['asymmetry_source']

    def test_mit_tr_lowest_asymmetry_among_deal_holders(self, publications):
        """MIT TR (1 deal) must have lowest asymmetry among publications with deals."""
        deal_pubs = [p for p in publications if p['competitor_deals'] > 0]
        mit = [p for p in publications if 'MIT' in p['name']][0]
        min_score = min(p['asymmetry_score'] for p in deal_pubs)
        assert mit['asymmetry_score'] == min_score

    def test_nyt_harshest_meta_tone(self, publications):
        """NYT must have the harshest meta_avg_tone (Kashmir Hill effect)."""
        nyt = [p for p in publications if p['name'] == 'NYT'][0]
        min_tone = min(p['meta_avg_tone'] for p in publications)
        assert nyt['meta_avg_tone'] == min_tone

    def test_verge_patel_delegation_paradox(self, publications):
        """Verge asymmetry source must reference EIC delegation (Mechanism #6)."""
        verge = [p for p in publications if 'Verge' in p['name']][0]
        assert 'Mechanism #6' in verge['asymmetry_source']

    def test_atlantic_warzel_referenced(self, publications):
        """Atlantic asymmetry source must reference Charlie Warzel."""
        atlantic = [p for p in publications if 'Atlantic' in p['name']][0]
        assert 'Warzel' in atlantic['asymmetry_source']

    def test_guardian_reader_funded_model(self, publications):
        """Guardian asymmetry source must reference reader-funded model."""
        guardian = [p for p in publications if 'Guardian' in p['name']][0]
        assert 'reader-funded' in guardian['asymmetry_source']


# =====================================================================
# CLASS 7: Asymmetry Ordering Consistency
# =====================================================================

class TestAsymmetryOrdering:
    """Validate that asymmetry scores follow expected financial-structure ordering."""

    def test_ft_highest_asymmetry(self, publications):
        """FT must have the highest asymmetry score (Nikkei ownership + OpenAI deal)."""
        ft = [p for p in publications if 'Financial Times' in p['name']][0]
        assert ft['asymmetry_score'] == max(p['asymmetry_score'] for p in publications)

    def test_gizmodo_lowest_asymmetry(self, publications):
        """Gizmodo (zero deals) must have the lowest asymmetry."""
        gz = [p for p in publications if 'Gizmodo' in p['name']][0]
        assert gz['asymmetry_score'] == min(p['asymmetry_score'] for p in publications)

    def test_wired_top_three(self, publications):
        """WIRED (5 deals) must be in top 3 asymmetry scores."""
        sorted_pubs = sorted(publications, key=lambda p: p['asymmetry_score'], reverse=True)
        top_names = [p['name'] for p in sorted_pubs[:3]]
        assert any('WIRED' in n for n in top_names)

    def test_nyt_top_three(self, publications):
        """NYT must be in top 3 asymmetry scores (Kashmir Hill + Amazon deals)."""
        sorted_pubs = sorted(publications, key=lambda p: p['asymmetry_score'], reverse=True)
        top_names = [p['name'] for p in sorted_pubs[:3]]
        assert 'NYT' in top_names

    def test_tone_asymmetry_correlation_direction(self, publications):
        """More negative meta_avg_tone should weakly correlate with higher asymmetry."""
        # Lower tone (more negative) generally = higher asymmetry
        # Not a perfect correlation (FT has -0.55 tone but 0.87 asymmetry)
        # but the bottom (Gizmodo: -0.30, 0.55) and top (FT: -0.55, 0.87) should align
        gz = [p for p in publications if 'Gizmodo' in p['name']][0]
        ft = [p for p in publications if 'Financial Times' in p['name']][0]
        assert gz['meta_avg_tone'] > ft['meta_avg_tone']  # Gizmodo less negative
        assert gz['asymmetry_score'] < ft['asymmetry_score']  # Gizmodo less asymmetric
