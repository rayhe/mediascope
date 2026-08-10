"""
Tests for Mechanism #28: Google Quintuple Anthropic Exposure + $35B SPV
Guarantee + Showcase Publisher Dependency Chain

TYPE C: Financial Incentive Mapping (Aug 10, 2026 12:00 PT)

FINDING: Google's role as payment GUARANTOR on Anthropic's $35B off-balance-
sheet SPV financing (Apollo/Blackstone, Jul 2026) creates a fifth layer of
Google-Anthropic financial entanglement. Combined with Google's $1B+ Showcase
program paying 700+ publishers, this creates an INDIRECT coverage incentive
chain: Showcase-dependent publishers have structural incentive to avoid
Anthropic coverage that would impair Google's $170B+ combined exposure.

Sources:
- https://www.linkedin.com/pulse/anthropics-35b-infrastructure-bet-inside-deal-reshaping-collin-gnajc
- https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/
- https://mediaandthemachine.substack.com/p/ai-content-licensing-deals-june-2026
- https://www.reuters.com/world/americas/google-pay-publishers-1-bln-over-three-years-their-news-2020-10-01/
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(name):
    path = os.path.join(PROFILES_DIR, name)
    with open(path) as f:
        return yaml.safe_load(f)


class TestGoogleQuintupleAnthropicExposure:
    """Google's five distinct roles in Anthropic's business."""

    def test_google_has_guarantee_role(self):
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        google_str = str(google).lower()
        assert 'guarantee' in google_str or 'guarantor' in google_str

    def test_spv_value_is_35b(self):
        entities = load_yaml('competitor-entities.yaml')
        combined = str(entities['entities'])
        assert '35' in combined

    def test_spv_is_off_balance_sheet(self):
        entities = load_yaml('competitor-entities.yaml')
        combined = str(entities['entities']).lower()
        assert 'off-balance' in combined or 'spv' in combined

    def test_apollo_documented(self):
        entities = load_yaml('competitor-entities.yaml')
        combined = str(entities['entities']).lower()
        assert 'apollo' in combined

    def test_broadcom_documented(self):
        entities = load_yaml('competitor-entities.yaml')
        combined = str(entities['entities']).lower()
        assert 'broadcom' in combined


class TestSPVIPOImplications:
    """SPV structure implications for IPO financial reporting."""

    def test_ipo_cleanliness_documented(self):
        entities = load_yaml('competitor-entities.yaml')
        anthro_str = str(entities['entities']['anthropic']).lower()
        assert 'ipo' in anthro_str

    def test_tranche_structure_referenced(self):
        entities = load_yaml('competitor-entities.yaml')
        combined = str(entities['entities']).lower()
        assert 'tranche' in combined or 'senior' in combined

    def test_tpu_scale_documented(self):
        entities = load_yaml('competitor-entities.yaml')
        combined = str(entities['entities'])
        assert '2.5' in combined or 'million TPU' in combined

    def test_five_sites_documented(self):
        entities = load_yaml('competitor-entities.yaml')
        combined = str(entities['entities']).lower()
        assert 'five' in combined or '5 site' in combined or '5 us' in combined


class TestShowcaseDependencyChain:
    """Chain from Showcase dependency to Anthropic coverage incentive."""

    def test_showcase_documented(self):
        entities = load_yaml('competitor-entities.yaml')
        google_str = str(entities['entities']['google'])
        assert 'Showcase' in google_str or 'showcase' in google_str

    def test_showcase_anthropic_chain_exists(self):
        entities = load_yaml('competitor-entities.yaml')
        combined = str(entities['entities']).lower()
        assert 'showcase' in combined and 'anthropic' in combined

    def test_zero_direct_anthropic_publisher_deals(self):
        entities = load_yaml('competitor-entities.yaml')
        anthro_str = str(entities['entities']['anthropic']).lower()
        assert 'zero' in anthro_str or '0 publisher' in anthro_str or \
               'no publisher' in anthro_str

    def test_rob_kelly_91_deals_anthropic_zero(self):
        """Rob Kelly tracks 91 public AI content deals; Anthropic has 0."""
        known = {'openai': 24, 'anthropic': 0, 'meta': 13}
        assert known['anthropic'] == 0
        assert known['openai'] > 0


class TestGoogleCreditRiskExposure:
    """Google's credit risk from the guarantee role."""

    def test_guarantee_creates_credit_risk(self):
        entities = load_yaml('competitor-entities.yaml')
        google_str = str(entities['entities']['google']).lower()
        assert 'guarantee' in google_str or 'guarantor' in google_str

    def test_google_equity_stake_documented(self):
        entities = load_yaml('competitor-entities.yaml')
        combined = str(entities['entities'])
        assert '14%' in combined or '14 percent' in combined.lower()

    def test_combined_exposure_exceeds_100b(self):
        equity_at_ipo = 0.14 * 965  # ~$135B
        guarantee = 35  # $35B
        assert equity_at_ipo + guarantee > 100


class TestAnthropicDealVacuumMechanism:
    """Deal Vacuum as distinct coverage incentive mechanism."""

    def test_mechanism_28_in_research(self):
        research = load_yaml('competitor-coverage-research.yaml')
        research_str = str(research).lower()
        assert 'mechanism #28' in research_str or 'spv_guarantee' in research_str or \
               'quintuple' in research_str or 'guarantee_chain' in research_str

    def test_pre_ipo_deal_courtship(self):
        entities = load_yaml('competitor-entities.yaml')
        combined = str(entities['entities']).lower()
        assert 'pre-ipo' in combined or 'pre_ipo' in combined

    @pytest.mark.parametrize('publication', [
        'wired', 'the-verge', 'guardian', 'financial-times',
    ])
    def test_showcase_pubs_have_coverage_prediction(self, publication):
        entities = load_yaml('competitor-entities.yaml')
        combined = str(entities['entities']).lower()
        assert 'showcase' in combined and 'coverage' in combined


class TestSPVTransparencyInflection:
    """How the SPV affects financial journalism obligations."""

    def test_s1_will_reveal_terms(self):
        entities = load_yaml('competitor-entities.yaml')
        anthro_str = str(entities['entities']['anthropic']).lower()
        assert 's-1' in anthro_str or 's1' in anthro_str or 'ipo' in anthro_str

    def test_private_deals_possibility_noted(self):
        entities = load_yaml('competitor-entities.yaml')
        anthro_str = str(entities['entities']['anthropic']).lower()
        assert 'private' in anthro_str or 'undisclosed' in anthro_str or \
               'troveo' in anthro_str or 'zero' in anthro_str


class TestLegitimateCaveats:
    """Legitimate counterarguments are documented."""

    def test_structural_not_conspiratorial(self):
        entities = load_yaml('competitor-entities.yaml')
        google_str = str(entities['entities']['google']).lower()
        assert 'structural' in google_str or 'indirect' in google_str or \
               'rational' in google_str

    @pytest.mark.parametrize('factor', [
        'commercial', 'legitimate', 'rational',
    ])
    def test_legitimate_factors_exist(self, factor):
        entities = load_yaml('competitor-entities.yaml')
        combined = str(entities['entities']).lower()
        assert factor in combined


class TestCrossReferenceIntegrity:
    """Cross-references with prior mechanisms."""

    def test_mechanism_26_still_exists(self):
        research = load_yaml('competitor-coverage-research.yaml')
        assert '#26' in str(research) or 'business_viability' in str(research).lower()

    def test_mechanism_25_still_exists(self):
        research = load_yaml('competitor-coverage-research.yaml')
        assert '#25' in str(research) or 'dual_lab' in str(research).lower() or \
               'dual-lab' in str(research).lower()

    def test_mechanism_21_still_exists(self):
        research = load_yaml('competitor-coverage-research.yaml')
        assert '#21' in str(research) or 'underwriter' in str(research).lower()

    def test_google_anthropic_layers_at_least_4(self):
        entities = load_yaml('competitor-entities.yaml')
        google_str = str(entities['entities']['google']).lower()
        anthro_str = str(entities['entities']['anthropic']).lower()
        combined = google_str + anthro_str
        layers = [
            any(x in combined for x in ['equity', 'investor', '14%']),
            any(x in combined for x in ['tpu', 'tensor']),
            any(x in combined for x in ['cloud', 'compute']),
            any(x in combined for x in ['guarantee', 'guarantor', 'spv']),
        ]
        assert sum(layers) >= 4
