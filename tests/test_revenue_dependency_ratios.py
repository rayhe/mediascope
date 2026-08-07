"""
Tests for Revenue Dependency Concentration Index (Type C iteration, Aug 6 2026).

Validates the financial incentive normalization model that calculates
competitor AI deal values as a percentage of total publication revenue.

KEY FINDING — INVERSE PROPORTIONALITY PARADOX:
The publications with the SMALLEST revenues face the HIGHEST proportional
incentive pressure from AI deals, but because they are private and their
deals are undisclosed, the incentive gradient is invisible.

Source URLs:
- NYT 10-K (FY2025): https://stockanalysis.com/stocks/nyt/revenue/
- FT revenue: https://www.amediaoperator.com/news/financial-times-annual-report-2024-revenue/
- Guardian annual report: https://tomorrowspublisher.today/the-guardian-halves-losses-and-hits-record-275m-revenue/
- Vox Media (Adweek): https://www.adweek.com/media/vox-media-roll-up-unwinds/
- Condé Nast (RocketReach): https://rocketreach.co/conde-nast-profile_b5f542b3f42d3402
- MIT TR Form 990: ProPublica Nonprofit Explorer, FY2024
- News Corp FY2025: https://newscorp.com/2025/08/05/news-corp-reports-fourth-quarter-and-full-year-results-for-fiscal-2025/
- News Corp Meta deal: https://www.wsj.com/business/media/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year-d4fbf244
- OpenAI deals tracker: https://llmpulse.ai/blog/openai-publisher-deals/
- Press Gazette tracker: https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture(scope="module")
def entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def rdc(entities):
    """Revenue Dependency Concentration section."""
    assert 'revenue_dependency_concentration' in entities, (
        "competitor-entities.yaml missing revenue_dependency_concentration section"
    )
    return entities['revenue_dependency_concentration']


@pytest.fixture(scope="module")
def publications(rdc):
    pubs = rdc.get('publications', [])
    assert len(pubs) >= 9, f"Expected >= 9 publications, got {len(pubs)}"
    return pubs


def _find_pub(publications, fragment):
    """Find a publication by name fragment."""
    for p in publications:
        if fragment.lower() in p['name'].lower():
            return p
    pytest.fail(f"Publication containing '{fragment}' not found")


# ===================================================================
# 1. Structure and Schema Validation
# ===================================================================

class TestRDCStructure:
    """Validate structure of revenue dependency concentration section."""

    def test_methodology_exists(self, rdc):
        assert 'methodology' in rdc
        assert 'dependency' in rdc['methodology'].lower()

    def test_source_urls_exist(self, rdc):
        assert 'source_urls' in rdc
        urls = rdc['source_urls']
        assert len(urls) >= 5, f"Expected >= 5 source URLs, got {len(urls)}"

    def test_key_findings_exist(self, rdc):
        assert 'key_findings' in rdc
        kf = rdc['key_findings']
        assert 'inverse_proportionality_paradox' in kf
        assert 'margin_amplification_effect' in kf
        assert 'disclosure_paradox' in kf

    def test_nine_publications(self, publications):
        assert len(publications) >= 9

    def test_all_expected_publications_present(self, publications):
        expected = [
            "MIT", "Guardian", "Vox", "Financial Times",
            "Condé Nast", "New York Times", "Atlantic",
            "Gizmodo", "News Corp"
        ]
        names = [p['name'] for p in publications]
        for frag in expected:
            assert any(frag in n for n in names), (
                f"Missing publication containing '{frag}'"
            )


class TestPublicationSchema:
    """Each publication must have required fields."""

    REQUIRED_FIELDS = [
        'name', 'total_revenue', 'competitor_deals',
        'meta_deals', 'adversarial_meta_coverage'
    ]

    def test_all_publications_have_required_fields(self, publications):
        for pub in publications:
            for field in self.REQUIRED_FIELDS:
                assert field in pub, (
                    f"{pub['name']} missing required field '{field}'"
                )

    def test_revenue_usd_present_when_known(self, publications):
        """Publications with known revenue must have total_revenue_usd."""
        for pub in publications:
            if pub['total_revenue'] and pub['total_revenue'] != 'unknown':
                assert 'total_revenue_usd' in pub, (
                    f"{pub['name']} has total_revenue but no total_revenue_usd"
                )

    def test_revenue_source_present(self, publications):
        """Each publication should cite its revenue source."""
        for pub in publications:
            if pub.get('total_revenue_usd') is not None:
                assert 'revenue_source' in pub, (
                    f"{pub['name']} has revenue but no revenue_source"
                )


# ===================================================================
# 2. Revenue Data Verification
# ===================================================================

class TestRevenueData:
    """Verify revenue figures match known public data."""

    def test_nyt_revenue_matches_10k(self, publications):
        """NYT FY2025 revenue should be ~$2.82B (per 10-K)."""
        nyt = _find_pub(publications, "New York Times")
        rev = nyt['total_revenue_usd']
        assert 2_700_000_000 <= rev <= 3_000_000_000, (
            f"NYT revenue {rev} outside expected range $2.7-3.0B"
        )

    def test_nyt_is_public(self, publications):
        nyt = _find_pub(publications, "New York Times")
        assert nyt.get('is_public') is True

    def test_news_corp_revenue_matches_10k(self, publications):
        """News Corp FY2025 revenue should be ~$8.45B."""
        nc = _find_pub(publications, "News Corp")
        rev = nc['total_revenue_usd']
        assert 8_000_000_000 <= rev <= 9_000_000_000, (
            f"News Corp revenue {rev} outside expected range $8-9B"
        )

    def test_news_corp_is_public(self, publications):
        nc = _find_pub(publications, "News Corp")
        assert nc.get('is_public') is True

    def test_guardian_revenue_approx_350m(self, publications):
        """Guardian FY2024-25 revenue ~£275M (~$350M)."""
        g = _find_pub(publications, "Guardian")
        rev = g['total_revenue_usd']
        assert 300_000_000 <= rev <= 400_000_000, (
            f"Guardian revenue {rev} outside expected range $300-400M"
        )

    def test_ft_revenue_approx_726m(self, publications):
        """FT 2024 global revenue ~£540M (~$726M)."""
        ft = _find_pub(publications, "Financial Times")
        rev = ft['total_revenue_usd']
        assert 650_000_000 <= rev <= 800_000_000, (
            f"FT revenue {rev} outside expected range $650-800M"
        )

    def test_mit_tr_revenue_from_990(self, publications):
        """MIT TR FY2024 revenue $22.3M (Form 990)."""
        mit = _find_pub(publications, "MIT")
        rev = mit['total_revenue_usd']
        assert 20_000_000 <= rev <= 25_000_000, (
            f"MIT TR revenue {rev} outside expected range $20-25M"
        )

    def test_mit_tr_is_smallest(self, publications):
        """MIT TR should have the smallest revenue of any publication."""
        mit = _find_pub(publications, "MIT")
        for pub in publications:
            if pub.get('total_revenue_usd') is not None and pub['name'] != mit['name']:
                assert pub['total_revenue_usd'] > mit['total_revenue_usd'], (
                    f"{pub['name']} ({pub['total_revenue_usd']}) should be "
                    f"larger than MIT TR ({mit['total_revenue_usd']})"
                )


# ===================================================================
# 3. Dependency Ratio Calculations
# ===================================================================

class TestDependencyRatios:
    """Validate dependency ratio calculations are consistent."""

    def test_nyt_dependency_ratio(self, publications):
        """NYT ratio: $22.5M / $2.82B ≈ 0.8%."""
        nyt = _find_pub(publications, "New York Times")
        ratio = nyt.get('dependency_ratio_floor', nyt.get('dependency_ratio_known'))
        assert 0.005 <= ratio <= 0.015, (
            f"NYT dependency ratio {ratio} outside expected range 0.5-1.5%"
        )

    def test_guardian_dependency_ratio(self, publications):
        """Guardian floor ratio: ~$7M / $350M ≈ 2.0%."""
        g = _find_pub(publications, "Guardian")
        ratio = g['dependency_ratio_floor']
        assert 0.01 <= ratio <= 0.04, (
            f"Guardian dependency ratio {ratio} outside expected range 1-4%"
        )

    def test_news_corp_has_meta_deal_ratio(self, publications):
        """News Corp should have a Meta dependency ratio (balanced control)."""
        nc = _find_pub(publications, "News Corp")
        assert 'dependency_ratio_meta' in nc or 'dependency_ratio_meta_pct' in nc, (
            "News Corp missing Meta dependency ratio"
        )

    def test_news_corp_balanced_ratios(self, publications):
        """News Corp competitor and Meta ratios should be approximately equal."""
        nc = _find_pub(publications, "News Corp")
        comp = nc.get('dependency_ratio_competitor', 0)
        meta = nc.get('dependency_ratio_meta', 0)
        assert abs(comp - meta) < 0.005, (
            f"News Corp ratios not balanced: competitor={comp}, meta={meta}"
        )

    def test_all_adversarial_pubs_zero_meta_deals(self, publications):
        """All adversarial publications should have 0 Meta deals."""
        for pub in publications:
            if pub.get('adversarial_meta_coverage'):
                meta = pub.get('meta_deals')
                assert meta == 0 or meta == [] or meta is None, (
                    f"{pub['name']} marked adversarial but has meta_deals: {meta}"
                )

    def test_ratios_are_internally_consistent(self, publications):
        """Floor deal value / revenue should match stated ratio."""
        for pub in publications:
            rev = pub.get('total_revenue_usd')
            floor_val = pub.get('floor_competitor_deal_value_usd')
            stated_ratio = pub.get('dependency_ratio_floor')
            if rev and floor_val and stated_ratio and rev > 0:
                calculated = floor_val / rev
                assert abs(calculated - stated_ratio) < 0.005, (
                    f"{pub['name']}: stated ratio {stated_ratio} but "
                    f"calculated {floor_val}/{rev} = {calculated:.4f}"
                )


# ===================================================================
# 4. Inverse Proportionality Paradox
# ===================================================================

class TestInverseProportionalityParadox:
    """Validate the key finding: smaller publications face higher ratios."""

    def test_atlantic_higher_ratio_than_nyt(self, publications):
        """The Atlantic (smaller) should have higher ratio than NYT (larger)."""
        atl = _find_pub(publications, "Atlantic")
        nyt = _find_pub(publications, "New York Times")
        atl_r = atl.get('dependency_ratio_floor', 0)
        nyt_r = nyt.get('dependency_ratio_floor', nyt.get('dependency_ratio_known', 0))
        assert atl_r > nyt_r, (
            f"Atlantic ratio ({atl_r}) should exceed NYT ratio ({nyt_r})"
        )

    def test_guardian_higher_ratio_than_nyt(self, publications):
        g = _find_pub(publications, "Guardian")
        nyt = _find_pub(publications, "New York Times")
        g_r = g['dependency_ratio_floor']
        nyt_r = nyt.get('dependency_ratio_floor', nyt.get('dependency_ratio_known', 0))
        assert g_r > nyt_r

    def test_adversarial_mean_exceeds_control(self, publications):
        """Mean adversarial dependency ratio should exceed control ratio."""
        adversarial_ratios = []
        control_ratio = None
        for pub in publications:
            if pub.get('balanced_coverage'):
                # News Corp uses dependency_ratio_competitor (not floor/known)
                control_ratio = pub.get('dependency_ratio_competitor')
                continue
            ratio = pub.get('dependency_ratio_floor',
                           pub.get('dependency_ratio_known'))
            if ratio is None:
                continue
            if pub.get('adversarial_meta_coverage'):
                adversarial_ratios.append(ratio)
        assert adversarial_ratios, "No adversarial ratios found"
        assert control_ratio is not None, "No control ratio found"
        mean_adv = sum(adversarial_ratios) / len(adversarial_ratios)
        assert mean_adv > control_ratio, (
            f"Mean adversarial ratio ({mean_adv:.4f}) should exceed "
            f"control ratio ({control_ratio:.4f})"
        )

    def test_ranking_order(self, rdc):
        """The ranking in key_findings should list publications in descending ratio order."""
        ranking = rdc['key_findings']['inverse_proportionality_paradox']['ranking_by_dependency_floor']
        # Extract numeric ratios from strings like "0.9% (floor)"
        import re
        ratios = []
        for entry in ranking:
            match = re.search(r'([\d.]+)%', entry['ratio'])
            if match:
                ratios.append(float(match.group(1)))
        # Should be roughly descending (Atlantic 4.4% > Guardian 2.0% > ... > News Corp 0.6%)
        # Allow for ties
        for i in range(len(ratios) - 1):
            assert ratios[i] >= ratios[i + 1] - 0.1, (
                f"Ranking not descending at position {i}: "
                f"{ratios[i]} should be >= {ratios[i+1]}"
            )


# ===================================================================
# 5. Margin Amplification Effect
# ===================================================================

class TestMarginAmplification:
    """Validate that margin-normalized ratios amplify the incentive signal."""

    def test_ft_margin_amplification(self, rdc):
        """FT's deals should represent >15% of operating profit."""
        examples = rdc['key_findings']['margin_amplification_effect']['examples']
        ft_ex = [e for e in examples if 'Financial Times' in e['publication']]
        assert ft_ex, "FT not in margin amplification examples"
        ratio_str = ft_ex[0]['ratio_vs_profit']
        ratio = float(ratio_str.rstrip('%'))
        assert ratio >= 15, f"FT margin ratio {ratio}% should be >= 15%"

    def test_guardian_loss_offset(self, rdc):
        """Guardian's deals should offset >15% of operating loss."""
        examples = rdc['key_findings']['margin_amplification_effect']['examples']
        guard_ex = [e for e in examples if 'Guardian' in e['publication']]
        assert guard_ex, "Guardian not in margin amplification examples"
        ratio_str = guard_ex[0]['ratio_vs_loss']
        ratio = float(ratio_str.rstrip('%'))
        assert ratio >= 15, f"Guardian loss offset {ratio}% should be >= 15%"

    def test_nyt_least_affected(self, rdc):
        """NYT should have the lowest margin impact ratio."""
        examples = rdc['key_findings']['margin_amplification_effect']['examples']
        nyt_ex = [e for e in examples if 'NYT' in e['publication']]
        assert nyt_ex, "NYT not in margin amplification examples"
        ratio_str = nyt_ex[0]['ratio_vs_profit']
        ratio = float(ratio_str.rstrip('%'))
        assert ratio < 10, f"NYT margin ratio {ratio}% should be < 10%"


# ===================================================================
# 6. Disclosure Paradox
# ===================================================================

class TestDisclosureParadox:
    """Validate the disclosure paradox finding."""

    def test_disclosure_paradox_exists(self, rdc):
        dp = rdc['key_findings']['disclosure_paradox']
        assert 'control_validation' in dp
        assert 'mims' in dp['control_validation'].lower() or \
               'wsj' in dp['control_validation'].lower()

    def test_news_corp_is_balanced_control(self, publications):
        nc = _find_pub(publications, "News Corp")
        assert nc.get('balanced_coverage') is True
        assert nc.get('adversarial_meta_coverage') is False


# ===================================================================
# 7. Deal Data Consistency with Existing Profiles
# ===================================================================

class TestCrossFileConsistency:
    """Verify RDC data matches existing profile data."""

    def test_nyt_amazon_deal_matches_profile(self, publications):
        """NYT Amazon deal value should match nytimes.yaml revenue_relationships."""
        nyt = _find_pub(publications, "New York Times")
        deals = nyt['competitor_deals']
        amazon_deals = [d for d in deals if 'amazon' in d['partner'].lower()]
        assert amazon_deals, "NYT missing Amazon deal"
        # Check it references $20-25M
        deal = amazon_deals[0]
        val = deal.get('value', deal.get('value_midpoint_usd', ''))
        assert '20' in str(val) or 22500000 == deal.get('value_midpoint_usd'), (
            f"NYT Amazon deal value doesn't match expected $20-25M"
        )

    def test_news_corp_openai_deal_50m(self, publications):
        """News Corp OpenAI deal should be $50M/yr."""
        nc = _find_pub(publications, "News Corp")
        deals = nc['competitor_deals']
        openai_deals = [d for d in deals if 'openai' in d['partner'].lower()]
        assert openai_deals, "News Corp missing OpenAI deal"
        deal = openai_deals[0]
        assert deal.get('value_annual_usd') == 50000000

    def test_news_corp_meta_deal_50m(self, publications):
        """News Corp Meta deal should be up to $50M/yr."""
        nc = _find_pub(publications, "News Corp")
        meta_deals = nc['meta_deals']
        assert isinstance(meta_deals, list) and len(meta_deals) >= 1, (
            "News Corp should have at least 1 Meta deal"
        )
        deal = meta_deals[0]
        assert deal.get('value_annual_usd') == 50000000

    def test_excluded_publishers_deal_counts_match(self, entities, publications):
        """Deal counts in RDC should match excluded_publishers counts."""
        excluded = entities['meta_ai_deals']['excluded_publishers']
        # Build mapping from distinctive name fragments to RDC publications
        exc_to_rdc = {
            "Condé Nast": "Condé Nast",
            "Vox Media": "Vox Media",
            "Atlantic": "Atlantic",
            "New York Times": "New York Times",
            "Financial Times": "Financial Times",
            "Guardian": "Guardian",
            "MIT": "MIT",
            "Gizmodo": "Gizmodo",
        }
        for exc_pub in excluded:
            exc_name = exc_pub['name']
            exc_count = exc_pub['deal_count']
            # Find matching RDC publication using distinctive fragment
            matched = False
            for frag, rdc_frag in exc_to_rdc.items():
                if frag in exc_name:
                    for rdc_pub in publications:
                        if rdc_frag in rdc_pub['name']:
                            rdc_deals = rdc_pub.get('competitor_deals', [])
                            rdc_count = len(rdc_deals)
                            assert rdc_count == exc_count, (
                                f"{exc_name}: excluded_publishers has {exc_count} deals "
                                f"but RDC has {rdc_count} deals"
                            )
                            matched = True
                            break
                    break
            assert matched, f"No RDC match found for excluded publisher: {exc_name}"


# ===================================================================
# 8. Statistical Validation
# ===================================================================

class TestStatisticalClaims:
    """Validate statistical claims in the analysis."""

    def test_nineteen_total_competitor_deals(self, publications):
        """Total competitor deals across all adversarial pubs should be 19."""
        total = 0
        for pub in publications:
            if pub.get('adversarial_meta_coverage'):
                total += len(pub.get('competitor_deals', []))
        assert total == 19, (
            f"Total adversarial competitor deals should be 19, got {total}"
        )

    def test_zero_total_meta_deals_adversarial(self, publications):
        """Total Meta deals across adversarial pubs should be 0."""
        for pub in publications:
            if pub.get('adversarial_meta_coverage'):
                meta = pub['meta_deals']
                assert meta == 0 or meta == [] or meta is None, (
                    f"{pub['name']}: adversarial pub has Meta deal"
                )

    def test_news_corp_revenue_dwarfs_mit_tr(self, publications):
        """News Corp revenue should be >300x MIT TR revenue."""
        nc = _find_pub(publications, "News Corp")
        mit = _find_pub(publications, "MIT")
        ratio = nc['total_revenue_usd'] / mit['total_revenue_usd']
        assert ratio > 300, (
            f"News Corp/MIT TR revenue ratio {ratio:.0f}x should be > 300x"
        )
