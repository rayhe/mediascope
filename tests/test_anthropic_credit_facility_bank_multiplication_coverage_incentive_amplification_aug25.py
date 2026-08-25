"""
Tests for Mechanism #302: Anthropic Credit Facility Bank Multiplication —
Coverage Incentive Amplification

Validates the financial architecture documented in competitor-coverage-research.yaml
and competitor-entities.yaml regarding Anthropic's $10B+ pre-IPO revolving credit
facility expanding the number of banks with structural incentive for favorable
Anthropic coverage from 4 lead underwriters to an estimated 12-19 institutions.

Sources:
- Reuters (Aug 18, 2026): Credit facility exceeds $10B target
- Reuters (Aug 17, 2026): ARR tops $65B by end of July
- Reuters (Aug 15, 2026): 2028 revenue projection $190-200B
- Lex Substack (Aug 25, 2026): Bank lending economics analysis
- FinanceFeeds (Aug 21, 2026): End-of-August filing at $2T
- Memeburn (Aug 21, 2026): H1 booked revenue breakdown
- Benzinga/TradingView (Aug 15, 2026): Q2 operating profit
"""
import os
import yaml
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def entities():
    return load_yaml('competitor-entities.yaml')


@pytest.fixture(scope='module')
def mechanism(research):
    return research['cross_publication_findings'][
        'anthropic_credit_facility_bank_multiplication_coverage_incentive_amplification'
    ]


@pytest.fixture(scope='module')
def anthropic(entities):
    return entities['entities']['anthropic']


# =============================================================================
# Class 1: Mechanism Structure
# =============================================================================
class TestMechanismStructure:
    def test_mechanism_id(self, mechanism):
        assert mechanism['mechanism_id'] == 302

    def test_finding_type(self, mechanism):
        assert mechanism['finding_type'] == 'financial_incentive_mapping'

    def test_has_finding_summary(self, mechanism):
        assert len(mechanism['finding_summary']) > 200

    def test_has_asymmetry_score(self, mechanism):
        score = mechanism['asymmetry_score']
        assert 0.0 <= score <= 1.0

    def test_has_source_urls(self, mechanism):
        assert len(mechanism['source_urls']) >= 6

    def test_all_source_urls_are_valid(self, mechanism):
        for url in mechanism['source_urls']:
            assert url.startswith('http'), f"Invalid URL: {url}"

    def test_has_test_file_reference(self, mechanism):
        assert 'test_file' in mechanism
        assert 'aug25' in mechanism['test_file']


# =============================================================================
# Class 2: Credit Facility Financial Architecture
# =============================================================================
class TestCreditFacilityFinancialArchitecture:
    def test_credit_facility_exceeds_10b(self, anthropic):
        ipo = anthropic['ipo_filing']
        assert ipo['pre_ipo_credit_facility_b'] >= 10

    def test_tier_structure_exists(self, anthropic):
        ipo = anthropic['ipo_filing']
        assert 'pre_ipo_credit_facility_tier_structure' in ipo

    def test_tier_1_commitment(self, anthropic):
        tiers = anthropic['ipo_filing']['pre_ipo_credit_facility_tier_structure']
        assert tiers['tier_1_commitment_b'] == 1.25

    def test_tier_2_commitment(self, anthropic):
        tiers = anthropic['ipo_filing']['pre_ipo_credit_facility_tier_structure']
        assert tiers['tier_2_commitment_b'] == 1.0

    def test_tier_3_commitment(self, anthropic):
        tiers = anthropic['ipo_filing']['pre_ipo_credit_facility_tier_structure']
        assert tiers['tier_3_commitment_b_max'] <= 0.75

    def test_implied_bank_count_range(self, anthropic):
        tiers = anthropic['ipo_filing']['pre_ipo_credit_facility_tier_structure']
        assert '8' in tiers['implied_bank_count_range']

    def test_tier_structure_has_sources(self, anthropic):
        tiers = anthropic['ipo_filing']['pre_ipo_credit_facility_tier_structure']
        assert len(tiers['source_urls']) >= 2


# =============================================================================
# Class 3: Revenue Trajectory Validation
# =============================================================================
class TestRevenueTrajectoryValidation:
    def test_arr_jul_2026(self, anthropic):
        assert anthropic['ipo_filing']['arr_jul_2026_b'] == 65

    def test_revenue_2028_projection(self, anthropic):
        proj = anthropic['ipo_filing']['revenue_2028_projection_b']
        assert '190' in str(proj)

    def test_h1_2026_booked_revenue(self, anthropic):
        h1 = anthropic['ipo_filing']['h1_2026_booked_revenue_b']
        assert 15 <= h1 <= 18, f"H1 booked revenue {h1}B outside expected range"

    def test_q2_operating_profit(self, anthropic):
        profit = anthropic['ipo_filing']['q2_2026_estimated_operating_profit_m']
        assert profit > 0, "Q2 should be first profitable quarter"

    def test_revenue_growth_trajectory(self, anthropic):
        """ARR grew from $9B (end 2025) to $65B (Jul 2026) — ~7x in 7 months."""
        ipo = anthropic['ipo_filing']
        arr_end_2025 = 9  # known baseline
        arr_jul_2026 = ipo['arr_jul_2026_b']
        growth_multiple = arr_jul_2026 / arr_end_2025
        assert growth_multiple >= 5, f"Growth multiple {growth_multiple}x below expected 7x"


# =============================================================================
# Class 4: Bank Multiplication Coverage Incentive
# =============================================================================
class TestBankMultiplicationCoverageIncentive:
    def test_lead_underwriter_count(self, anthropic):
        banks = anthropic['ipo_filing']['ipo_banks_reported']
        assert len(banks) >= 4, "Should have at least 4 lead underwriters"

    def test_credit_facility_multiplies_bank_count(self, mechanism):
        """Credit facility implies 8-15+ banks vs 4 lead underwriters — 2-4x multiplication."""
        summary = mechanism['finding_summary']
        assert '8-15' in summary or '12-19' in summary

    def test_lending_is_loss_leader_for_ipo(self, mechanism):
        """$7M lending revenue vs $50M+ IPO fee — 7:1 ratio."""
        summary = mechanism['finding_summary']
        assert '7:1' in summary

    def test_meta_has_zero_ipo_fee_incentive(self, mechanism):
        summary = mechanism['finding_summary']
        assert 'ZERO' in summary or 'zero' in summary.lower()

    def test_mechanism_documents_bank_multiplication(self, mechanism):
        """Core finding: credit facility expands financial entanglement beyond 4 lead banks."""
        summary = mechanism['finding_summary']
        assert 'multiplication' in summary.lower() or 'multiplying' in summary.lower()


# =============================================================================
# Class 5: IPO Filing Timeline
# =============================================================================
class TestIPOFilingTimeline:
    def test_filing_timeline_exists(self, anthropic):
        assert 'ipo_filing_timeline_update' in anthropic['ipo_filing']

    def test_public_filing_target(self, anthropic):
        timeline = anthropic['ipo_filing']['ipo_filing_timeline_update']
        assert 'August' in timeline['public_filing_target']

    def test_valuation_target(self, anthropic):
        timeline = anthropic['ipo_filing']['ipo_filing_timeline_update']
        assert timeline['valuation_target_t'] >= 2

    def test_s1_disclosure_significance(self, anthropic):
        """S-1 will be first public disclosure of publisher deal financials."""
        timeline = anthropic['ipo_filing']['ipo_filing_timeline_update']
        assert 'publisher' in timeline.get('valuation_range_note', '').lower() or \
               'S-1' in timeline.get('valuation_range_note', '')


# =============================================================================
# Class 6: Confounders
# =============================================================================
class TestConfounders:
    def test_has_confounders(self, mechanism):
        assert len(mechanism['confounders']) >= 4

    def test_has_strong_confounders(self, mechanism):
        strong = [c for c in mechanism['confounders'] if c['strength'] == 'STRONG']
        assert len(strong) >= 2, "Must have at least 2 STRONG confounders for intellectual honesty"

    def test_editorial_independence_confounder(self, mechanism):
        strong = [c for c in mechanism['confounders'] if c['strength'] == 'STRONG']
        editorial = [c for c in strong if 'editorial' in c['description'].lower()]
        assert len(editorial) >= 1

    def test_multi_hop_transmission_confounder(self, mechanism):
        strong = [c for c in mechanism['confounders'] if c['strength'] == 'STRONG']
        multi_hop = [c for c in strong if 'multi-hop' in c['description'].lower() or
                     'transmission' in c['description'].lower()]
        assert len(multi_hop) >= 1

    def test_temporal_precedent_confounder(self, mechanism):
        moderate = [c for c in mechanism['confounders'] if c['strength'] == 'MODERATE']
        temporal = [c for c in moderate if 'temporal' in c['description'].lower() or
                    'predate' in c['description'].lower()]
        assert len(temporal) >= 1


# =============================================================================
# Class 7: Cross-References
# =============================================================================
class TestCrossReferences:
    def test_has_cross_references(self, mechanism):
        assert len(mechanism['cross_references']) >= 3

    def test_references_mechanism_35(self, mechanism):
        refs = [r for r in mechanism['cross_references'] if r['mechanism_id'] == 35]
        assert len(refs) == 1, "Must reference mechanism #35 (pre-IPO underwriter convergence)"

    def test_references_mechanism_21(self, mechanism):
        refs = [r for r in mechanism['cross_references'] if r['mechanism_id'] == 21]
        assert len(refs) == 1, "Must reference mechanism #21 (research laundering)"

    def test_references_mechanism_294(self, mechanism):
        refs = [r for r in mechanism['cross_references'] if r['mechanism_id'] == 294]
        assert len(refs) == 1, "Must reference mechanism #294 (CN post-search dependency)"


# =============================================================================
# Class 8: Source Verification
# =============================================================================
class TestSourceVerification:
    def test_reuters_credit_facility_source(self, mechanism):
        urls = mechanism['source_urls']
        reuters_cf = [u for u in urls if 'reuters.com' in u and 'credit-facility' in u]
        assert len(reuters_cf) >= 1

    def test_reuters_revenue_source(self, mechanism):
        urls = mechanism['source_urls']
        reuters_rev = [u for u in urls if 'reuters.com' in u and 'revenue' in u]
        assert len(reuters_rev) >= 1

    def test_lex_substack_economics_source(self, mechanism):
        urls = mechanism['source_urls']
        lex = [u for u in urls if 'lex.substack.com' in u]
        assert len(lex) >= 1

    def test_entities_credit_facility_source(self, anthropic):
        source = anthropic['ipo_filing']['pre_ipo_credit_facility_source']
        assert 'reuters.com' in source

    def test_revenue_2028_source(self, anthropic):
        source = anthropic['ipo_filing']['revenue_2028_projection_source']
        assert 'reuters.com' in source
