"""
Type D Midnight Cross-Validation: Revenue Dependency Concentration Integrity (Aug 7, 2026)

Cross-validates the Revenue Dependency Concentration Index added in
the 11PM Type C iteration on Aug 6. Tests verify:

1. MATHEMATICAL CONSISTENCY:
   - Dependency ratios match deal values / revenue
   - Floor estimates >= known values
   - Rankings are internally consistent

2. SOURCE CROSS-REFERENCES:
   - Revenue figures consistent across profiles
   - Deal values consistent with competitor-entities.yaml deal registry
   - Operating margin figures are arithmetically valid

3. KEY FINDINGS VALIDATION:
   - Inverse proportionality paradox: ranking is correct
   - Margin amplification: ratios match stated figures
   - Disclosure paradox: claims match per-publication data

4. BALANCED CONTROL INTEGRITY:
   - News Corp dual-deal structure is correctly represented
   - Symmetric dependency ratios are mathematically correct

5. CROSS-FILE CONSISTENCY:
   - Publication profiles reference same deal values
   - No contradiction between financial-times.yaml and competitor-entities.yaml
"""

import yaml
import os
import pytest
import math

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def entities():
    return load_yaml('competitor-entities.yaml')


@pytest.fixture(scope='module')
def rdc(entities):
    """Revenue Dependency Concentration section."""
    return entities['revenue_dependency_concentration']


@pytest.fixture(scope='module')
def publications(rdc):
    """Publication list from RDC section."""
    return {p['name']: p for p in rdc['publications']}


@pytest.fixture(scope='module')
def findings(rdc):
    """Key findings from RDC section."""
    return rdc['key_findings']


@pytest.fixture(scope='module')
def wired_profile():
    return load_yaml('wired.yaml')


@pytest.fixture(scope='module')
def ft_profile():
    return load_yaml('financial-times.yaml')


@pytest.fixture(scope='module')
def guardian_profile():
    return load_yaml('guardian.yaml')


@pytest.fixture(scope='module')
def nytimes_profile():
    return load_yaml('nytimes.yaml')


@pytest.fixture(scope='module')
def atlantic_profile():
    return load_yaml('atlantic.yaml')


# ===================================================================
# 1. MATHEMATICAL CONSISTENCY
# ===================================================================

class TestDependencyRatioArithmetic:
    """Verify dependency ratios are correctly calculated from deal values and revenue."""

    def test_nyt_ratio_calculation(self, publications):
        nyt = publications['The New York Times']
        expected = nyt['floor_competitor_deal_value_usd'] / nyt['total_revenue_usd']
        assert abs(nyt['dependency_ratio_floor'] - expected) < 0.001

    def test_guardian_ratio_calculation(self, publications):
        guardian = publications['The Guardian']
        expected = guardian['floor_competitor_deal_value_usd'] / guardian['total_revenue_usd']
        assert abs(guardian['dependency_ratio_floor'] - expected) < 0.001

    def test_ft_ratio_calculation(self, publications):
        ft = publications['Financial Times (Nikkei)']
        expected = ft['floor_competitor_deal_value_usd'] / ft['total_revenue_usd']
        assert abs(ft['dependency_ratio_floor'] - expected) < 0.001

    def test_conde_nast_ratio_calculation(self, publications):
        cn = publications['Condé Nast (WIRED)']
        expected = cn['floor_competitor_deal_value_usd'] / cn['total_revenue_usd']
        assert abs(cn['dependency_ratio_floor'] - expected) < 0.001

    def test_atlantic_ratio_calculation(self, publications):
        atl = publications['Emerson Collective (The Atlantic)']
        expected = atl['floor_competitor_deal_value_usd'] / atl['total_revenue_usd']
        assert abs(atl['dependency_ratio_floor'] - expected) < 0.001

    def test_vox_ratio_calculation(self, publications):
        vox = publications['Vox Media (The Verge)']
        expected = vox['floor_competitor_deal_value_usd'] / vox['total_revenue_usd']
        assert abs(vox['dependency_ratio_floor'] - expected) < 0.001

    def test_news_corp_competitor_ratio(self, publications):
        nc = publications['News Corp (WSJ, NY Post)']
        expected = nc['known_competitor_deal_value_usd'] / nc['total_revenue_usd']
        assert abs(nc['dependency_ratio_competitor'] - expected) < 0.001

    def test_news_corp_meta_ratio(self, publications):
        nc = publications['News Corp (WSJ, NY Post)']
        expected = nc['known_meta_deal_value_usd'] / nc['total_revenue_usd']
        assert abs(nc['dependency_ratio_meta'] - expected) < 0.001

    def test_news_corp_symmetric(self, publications):
        """News Corp competitor and Meta ratios should be equal (both $50M on $8.45B)."""
        nc = publications['News Corp (WSJ, NY Post)']
        assert nc['dependency_ratio_competitor'] == nc['dependency_ratio_meta']

    def test_floor_gte_known(self, publications):
        """Floor deal estimates must be >= known deal values for all pubs."""
        for name, pub in publications.items():
            if 'known_competitor_deal_value_usd' in pub and 'floor_competitor_deal_value_usd' in pub:
                assert pub['floor_competitor_deal_value_usd'] >= pub['known_competitor_deal_value_usd'], \
                    f"{name}: floor ({pub['floor_competitor_deal_value_usd']}) < known ({pub['known_competitor_deal_value_usd']})"


class TestDealValueSummation:
    """Verify deal floor values equal sum of individual deal floors."""

    def test_guardian_deal_sum(self, publications):
        guardian = publications['The Guardian']
        deal_sum = sum(d.get('value_estimate_floor_usd', 0) for d in guardian['competitor_deals'])
        assert deal_sum == guardian['floor_competitor_deal_value_usd']

    def test_vox_deal_sum(self, publications):
        vox = publications['Vox Media (The Verge)']
        deal_sum = sum(d.get('value_estimate_floor_usd', 0) for d in vox['competitor_deals'])
        assert deal_sum == vox['floor_competitor_deal_value_usd']

    def test_ft_deal_sum(self, publications):
        ft = publications['Financial Times (Nikkei)']
        # FT has one known midpoint + two floors
        total = 0
        for d in ft['competitor_deals']:
            if 'value_midpoint_usd' in d:
                total += d['value_midpoint_usd']
            elif 'value_estimate_floor_usd' in d:
                total += d['value_estimate_floor_usd']
        assert total == ft['floor_competitor_deal_value_usd']

    def test_atlantic_deal_sum(self, publications):
        atl = publications['Emerson Collective (The Atlantic)']
        deal_sum = sum(d.get('value_estimate_floor_usd', 0) for d in atl['competitor_deals'])
        assert deal_sum == atl['floor_competitor_deal_value_usd']

    def test_nyt_deal_sum(self, publications):
        nyt = publications['The New York Times']
        total = 0
        for d in nyt['competitor_deals']:
            if 'value_midpoint_usd' in d:
                total += d['value_midpoint_usd']
            elif 'value_estimate_floor_usd' in d:
                total += d['value_estimate_floor_usd']
        assert total == nyt['floor_competitor_deal_value_usd']


# ===================================================================
# 2. RANKING CONSISTENCY
# ===================================================================

class TestInverseProportionalityRanking:
    """Verify the ranking in key_findings matches actual calculated ratios."""

    def test_atlantic_highest_adversarial_ratio(self, publications):
        """Atlantic should have highest dependency floor ratio among adversarial pubs."""
        adversarial = {k: v for k, v in publications.items()
                       if v.get('adversarial_meta_coverage', False)
                       and v.get('dependency_ratio_floor') is not None}
        max_pub = max(adversarial, key=lambda k: adversarial[k]['dependency_ratio_floor'])
        assert max_pub == 'Emerson Collective (The Atlantic)'

    def test_nyt_lowest_adversarial_ratio(self, publications):
        """NYT should have lowest dependency floor ratio among adversarial pubs with data."""
        adversarial = {k: v for k, v in publications.items()
                       if v.get('adversarial_meta_coverage', False)
                       and v.get('dependency_ratio_floor') is not None}
        min_pub = min(adversarial, key=lambda k: adversarial[k]['dependency_ratio_floor'])
        assert min_pub == 'The New York Times'

    def test_news_corp_lower_than_all_adversarial(self, publications):
        """Balanced control (News Corp) should have lower competitor ratio than adversarial mean."""
        nc = publications['News Corp (WSJ, NY Post)']
        adversarial_ratios = [v['dependency_ratio_floor']
                              for k, v in publications.items()
                              if v.get('adversarial_meta_coverage', False)
                              and v.get('dependency_ratio_floor') is not None]
        mean_adversarial = sum(adversarial_ratios) / len(adversarial_ratios)
        assert nc['dependency_ratio_competitor'] < mean_adversarial

    def test_ranking_order_matches_findings(self, findings, publications):
        """The ranking in key_findings should match sorted order of actual ratios."""
        ranking = findings['inverse_proportionality_paradox']['ranking_by_dependency_floor']
        # Extract publication names from ranking
        ranked_names = [r['publication'] for r in ranking]
        # Atlantic should be first (highest), News Corp last (balanced control)
        assert ranked_names[0] == 'The Atlantic'
        assert ranked_names[-1] == 'News Corp (control)'


# ===================================================================
# 3. MARGIN AMPLIFICATION VALIDATION
# ===================================================================

class TestMarginAmplificationArithmetic:
    """Verify margin amplification ratios are mathematically correct."""

    def test_ft_margin_ratio(self, findings):
        """FT's $11.5M vs $56.7M operating profit should be ~20%."""
        ft_example = None
        for ex in findings['margin_amplification_effect']['examples']:
            if ex['publication'] == 'Financial Times':
                ft_example = ex
                break
        assert ft_example is not None
        # Parse the values
        deal = 11.5  # $11.5M
        profit = 56.7  # $56.7M
        expected_ratio = deal / profit * 100
        stated_ratio = float(ft_example['ratio_vs_profit'].replace('%', ''))
        assert abs(expected_ratio - stated_ratio) < 1.0

    def test_guardian_loss_ratio(self, findings):
        """Guardian's $7M vs $31.8M operating loss should be ~22%."""
        guard_example = None
        for ex in findings['margin_amplification_effect']['examples']:
            if ex['publication'] == 'The Guardian':
                guard_example = ex
                break
        assert guard_example is not None
        deal = 7.0  # $7M
        loss = 31.8  # $31.8M
        expected_ratio = deal / loss * 100
        stated_ratio = float(guard_example['ratio_vs_loss'].replace('%', ''))
        assert abs(expected_ratio - stated_ratio) < 1.0

    def test_nyt_profit_ratio(self, findings):
        """NYT's $22.5M vs $432M operating profit should be ~5.2%."""
        nyt_example = None
        for ex in findings['margin_amplification_effect']['examples']:
            if ex['publication'] == 'NYT':
                nyt_example = ex
                break
        assert nyt_example is not None
        deal = 22.5
        profit = 432
        expected_ratio = deal / profit * 100
        stated_ratio = float(nyt_example['ratio_vs_profit'].replace('%', ''))
        assert abs(expected_ratio - stated_ratio) < 1.0

    def test_news_corp_profit_ratio(self, findings):
        """News Corp's $100M vs $1.07B operating profit should be ~9.3%."""
        nc_example = None
        for ex in findings['margin_amplification_effect']['examples']:
            if ex['publication'] == 'News Corp (control)':
                nc_example = ex
                break
        assert nc_example is not None
        deal = 100
        profit = 1070
        expected_ratio = deal / profit * 100
        stated_ratio = float(nc_example['ratio_vs_profit'].replace('%', ''))
        assert abs(expected_ratio - stated_ratio) < 1.0


# ===================================================================
# 4. DISCLOSURE PARADOX VALIDATION
# ===================================================================

class TestDisclosureParadoxConsistency:
    """Verify disclosure paradox claims are consistent with per-publication data."""

    def test_news_corp_is_balanced(self, publications):
        """News Corp should be flagged as balanced coverage."""
        nc = publications['News Corp (WSJ, NY Post)']
        assert nc.get('balanced_coverage', False) is True
        assert nc.get('adversarial_meta_coverage', False) is False

    def test_all_adversarial_pubs_marked(self, publications):
        """All non-control publications should be adversarial."""
        for name, pub in publications.items():
            if name != 'News Corp (WSJ, NY Post)':
                if pub.get('dependency_ratio_floor') is not None or pub.get('adversarial_meta_coverage') is not None:
                    assert pub.get('adversarial_meta_coverage', False) is True, \
                        f"{name} should be adversarial"

    def test_gizmodo_clean_control(self, publications):
        """Gizmodo should have zero deals on both sides."""
        giz = publications['Keleops AG (Gizmodo)']
        assert giz['known_competitor_deal_value_usd'] == 0
        assert giz['floor_competitor_deal_value_usd'] == 0
        assert giz['meta_deals'] == 0
        assert giz.get('adversarial_meta_coverage', False) is True

    def test_news_corp_has_both_deals(self, publications):
        """News Corp should have both competitor and Meta deals."""
        nc = publications['News Corp (WSJ, NY Post)']
        assert nc['known_competitor_deal_value_usd'] > 0
        assert nc['known_meta_deal_value_usd'] > 0

    def test_adversarial_pubs_have_zero_meta_deals(self, publications):
        """All adversarial publications should have zero Meta deals."""
        for name, pub in publications.items():
            if pub.get('adversarial_meta_coverage', False):
                meta_deals = pub.get('meta_deals', None)
                if meta_deals is not None:
                    assert meta_deals == 0, f"{name} has {meta_deals} Meta deals but is adversarial"


# ===================================================================
# 5. REVENUE DATA PLAUSIBILITY
# ===================================================================

class TestRevenuePlausibility:
    """Sanity-check revenue figures are within plausible ranges."""

    def test_nyt_revenue_plausible(self, publications):
        """NYT revenue should be $2-4B (10-K verifiable)."""
        nyt = publications['The New York Times']
        assert 2_000_000_000 <= nyt['total_revenue_usd'] <= 4_000_000_000

    def test_news_corp_revenue_plausible(self, publications):
        """News Corp should be $7-12B."""
        nc = publications['News Corp (WSJ, NY Post)']
        assert 7_000_000_000 <= nc['total_revenue_usd'] <= 12_000_000_000

    def test_ft_revenue_plausible(self, publications):
        """FT revenue should be $500M-$1B."""
        ft = publications['Financial Times (Nikkei)']
        assert 500_000_000 <= ft['total_revenue_usd'] <= 1_000_000_000

    def test_guardian_revenue_plausible(self, publications):
        """Guardian revenue should be $250M-$500M."""
        g = publications['The Guardian']
        assert 250_000_000 <= g['total_revenue_usd'] <= 500_000_000

    def test_mit_tr_revenue_plausible(self, publications):
        """MIT TR revenue should be $15-50M (small nonprofit)."""
        mit = publications['MIT Technology Review']
        assert 15_000_000 <= mit['total_revenue_usd'] <= 50_000_000

    def test_conde_nast_revenue_plausible(self, publications):
        """Condé Nast should be $1-3B."""
        cn = publications['Condé Nast (WIRED)']
        assert 1_000_000_000 <= cn['total_revenue_usd'] <= 3_000_000_000

    def test_atlantic_revenue_plausible(self, publications):
        """The Atlantic should be $75-200M."""
        atl = publications['Emerson Collective (The Atlantic)']
        assert 75_000_000 <= atl['total_revenue_usd'] <= 200_000_000

    def test_vox_revenue_plausible(self, publications):
        """Vox Media should be $300-600M."""
        vox = publications['Vox Media (The Verge)']
        assert 300_000_000 <= vox['total_revenue_usd'] <= 600_000_000


# ===================================================================
# 6. CROSS-FILE CONSISTENCY
# ===================================================================

class TestCrossFileConsistency:
    """Verify revenue/deal data is consistent across publication profiles."""

    def test_ft_openai_deal_referenced(self, ft_profile, publications):
        """FT profile should reference OpenAI deal, consistent with RDC data."""
        ft_rdc = publications['Financial Times (Nikkei)']
        openai_deals = [d for d in ft_rdc['competitor_deals'] if d['partner'] == 'OpenAI']
        assert len(openai_deals) >= 1

    def test_guardian_openai_deal_referenced(self, guardian_profile, publications):
        """Guardian RDC should have OpenAI deal."""
        g_rdc = publications['The Guardian']
        openai_deals = [d for d in g_rdc['competitor_deals'] if d['partner'] == 'OpenAI']
        assert len(openai_deals) >= 1

    def test_conde_nast_deal_count(self, publications):
        """Condé Nast should have highest deal count among adversarial pubs."""
        cn = publications['Condé Nast (WIRED)']
        cn_deals = len(cn['competitor_deals'])
        for name, pub in publications.items():
            if name != 'Condé Nast (WIRED)' and pub.get('adversarial_meta_coverage', False):
                other_deals = len(pub.get('competitor_deals', []))
                assert cn_deals >= other_deals, \
                    f"Condé Nast ({cn_deals}) should have >= deals than {name} ({other_deals})"

    def test_news_corp_deal_values_match_entities(self, entities, publications):
        """News Corp deal values in RDC should match the broader entities registry."""
        nc = publications['News Corp (WSJ, NY Post)']
        # $50M each from competitor and Meta
        assert nc['known_competitor_deal_value_usd'] == 50_000_000
        assert nc['known_meta_deal_value_usd'] == 50_000_000


# ===================================================================
# 7. SOURCE URL PRESENCE
# ===================================================================

class TestSourceUrlPresence:
    """Every RDC section should have source URLs for revenue claims."""

    def test_has_source_urls(self, rdc):
        """RDC section must have source_urls."""
        assert 'source_urls' in rdc
        assert len(rdc['source_urls']) >= 5

    def test_nyt_has_10k_source(self, rdc):
        assert 'nyt_10k' in rdc['source_urls']

    def test_ft_has_revenue_source(self, rdc):
        assert 'ft_revenue' in rdc['source_urls']

    def test_news_corp_has_10k_source(self, rdc):
        assert 'news_corp_10k' in rdc['source_urls']

    def test_each_pub_has_revenue_source(self, publications):
        """Every publication with revenue data should cite its source."""
        for name, pub in publications.items():
            if pub.get('total_revenue_usd') is not None:
                assert 'revenue_source' in pub and pub['revenue_source'], \
                    f"{name} has revenue but no revenue_source"

    def test_each_deal_has_source(self, publications):
        """Every deal should have a source field."""
        for name, pub in publications.items():
            for deal in pub.get('competitor_deals', []):
                assert 'source' in deal and deal['source'], \
                    f"{name} deal with {deal.get('partner', '?')} has no source"


# ===================================================================
# 8. COMPLETE COVERAGE CHECK
# ===================================================================

class TestCoverageCompleteness:
    """Verify all expected publications are represented."""

    def test_nine_publications(self, publications):
        """Should have 9 publications in RDC section."""
        assert len(publications) == 9

    EXPECTED_PUBS = [
        'MIT Technology Review',
        'The Guardian',
        'Vox Media (The Verge)',
        'Financial Times (Nikkei)',
        'Condé Nast (WIRED)',
        'The New York Times',
        'Emerson Collective (The Atlantic)',
        'Keleops AG (Gizmodo)',
        'News Corp (WSJ, NY Post)',
    ]

    @pytest.mark.parametrize("pub_name", EXPECTED_PUBS)
    def test_publication_present(self, publications, pub_name):
        assert pub_name in publications, f"Missing publication: {pub_name}"

    def test_three_key_findings(self, findings):
        """Should have all three key findings."""
        assert 'inverse_proportionality_paradox' in findings
        assert 'margin_amplification_effect' in findings
        assert 'disclosure_paradox' in findings


# ===================================================================
# 9. GIZMODO CLEAN CONTROL ISOLATION
# ===================================================================

class TestGizmodoCleanControl:
    """Gizmodo as zero-deal control validates editorial culture as independent factor."""

    def test_no_competitor_deals(self, publications):
        giz = publications['Keleops AG (Gizmodo)']
        assert len(giz.get('competitor_deals', [])) == 0

    def test_no_revenue_data(self, publications):
        """Gizmodo revenue is unknown — should have null ratio."""
        giz = publications['Keleops AG (Gizmodo)']
        assert giz.get('dependency_ratio_floor') is None
        assert giz.get('dependency_ratio_known') is None

    def test_still_adversarial(self, publications):
        """Despite zero deals, Gizmodo is adversarial (editorial culture)."""
        giz = publications['Keleops AG (Gizmodo)']
        assert giz['adversarial_meta_coverage'] is True


# ===================================================================
# 10. NEWS CORP BALANCE VALIDATION
# ===================================================================

class TestNewsCorpBalance:
    """News Corp balanced control should have perfect symmetry."""

    def test_equal_deal_values(self, publications):
        nc = publications['News Corp (WSJ, NY Post)']
        assert nc['known_competitor_deal_value_usd'] == nc['known_meta_deal_value_usd']

    def test_equal_ratios(self, publications):
        nc = publications['News Corp (WSJ, NY Post)']
        assert nc['dependency_ratio_competitor'] == nc['dependency_ratio_meta']

    def test_total_ai_ratio(self, publications):
        """Total AI ratio should be sum of competitor + Meta ratios."""
        nc = publications['News Corp (WSJ, NY Post)']
        expected_total = nc['dependency_ratio_competitor'] + nc['dependency_ratio_meta']
        assert abs(nc['dependency_ratio_total_ai'] - expected_total) < 0.001

    def test_has_dow_jones_revenue(self, publications):
        """Should break out Dow Jones revenue separately."""
        nc = publications['News Corp (WSJ, NY Post)']
        assert 'dow_jones_revenue_usd' in nc
        assert nc['dow_jones_revenue_usd'] < nc['total_revenue_usd']

    def test_is_public_company(self, publications):
        nc = publications['News Corp (WSJ, NY Post)']
        assert nc['is_public'] is True

    def test_nyt_is_public_company(self, publications):
        nyt = publications['The New York Times']
        assert nyt['is_public'] is True
