"""
Tests for Mechanism #306: Broadcom XPV $100B Escalation — Apollo Private Credit-
Publisher Compound Incentive

Validates the financial architecture documented in competitor-coverage-research.yaml
and competitor-entities.yaml regarding the Broadcom AI XPV Platform financing
escalation from $35B (June 2026) to potentially $100B (August 20, 2026).

Apollo Global Management simultaneously participates in Anthropic infrastructure
financing ($35B→$100B) AND owns Yahoo publications (TechCrunch, Engadget) that
demonstrably produce softer Anthropic coverage vs Meta (mechanism #305: Rebecca
Bellan vocabulary inversion: Meta -0.20, Anthropic +0.15, same 2-week window).

Cumulative Anthropic financial web exceeds $300B across all instruments: XPV
($35B+$60-100B), pre-IPO credit facility ($10B+), Nexus data center ($15B
Google-guaranteed), Google chip deal ($35B backstop), and total equity ($65B).

Morgan Stanley leads BOTH the $10B+ pre-IPO credit facility AND the IPO
underwriting, with credit facility banks explicitly "jockeying" for IPO roles.

Sources:
- Reuters (Aug 20, 2026): Broadcom seeks $60B+ in AI debt financing
- Reuters (Aug 18, 2026): Pre-IPO credit facility exceeds $10B
- TradingView (Aug 20, 2026): Broadcom eyes up to $100B AI financing deal
- SiliconANGLE (Aug 20, 2026): Broadcom reportedly seeking up to $100B
- Barchart: Broadcom off-balance-sheet financing machine analysis
- Reuters (Jul 30, 2026): $15B Nexus data center deal backed by Google
- The Hindu Business Line: Google backstops $35B chip deal
- TheStreet: Wall Street banks land Anthropic IPO
- PYMNTS: Morgan Stanley and Goldman Sachs land Anthropic IPO
- WSJ: IPO onslaught forcing bankers to pick teams
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
        'broadcom_xpv_100b_escalation_private_credit_publisher_compound_incentive'
    ]


@pytest.fixture(scope='module')
def anthropic(entities):
    return entities['entities']['anthropic']


# =============================================================================
# Class 1: Mechanism Structure
# =============================================================================
class TestMechanismStructure:
    def test_mechanism_id(self, mechanism):
        assert mechanism['mechanism_id'] == 306

    def test_finding_type(self, mechanism):
        assert mechanism['finding_type'] == 'financial_incentive_mapping'

    def test_has_finding_summary(self, mechanism):
        assert len(mechanism['finding_summary']) > 300

    def test_has_asymmetry_score(self, mechanism):
        score = mechanism['asymmetry_score']
        assert 0.0 <= score <= 1.0

    def test_asymmetry_score_high(self, mechanism):
        """Apollo compound incentive is direct — score should be >= 0.85."""
        assert mechanism['asymmetry_score'] >= 0.85

    def test_has_source_urls(self, mechanism):
        assert len(mechanism['source_urls']) >= 8

    def test_all_source_urls_are_valid(self, mechanism):
        for url in mechanism['source_urls']:
            assert url.startswith('http'), f"Invalid URL: {url}"

    def test_has_test_file_reference(self, mechanism):
        assert 'test_file' in mechanism
        assert 'aug25' in mechanism['test_file']

    def test_has_date_added(self, mechanism):
        assert mechanism['date_added'] == '2026-08-25'

    def test_publication_is_cross_publication(self, mechanism):
        assert mechanism['publication'] == 'cross_publication'


# =============================================================================
# Class 2: Broadcom XPV Escalation
# =============================================================================
class TestBroadcomXPVEscalation:
    def test_escalation_from_35b(self, mechanism):
        """Validates the $35B starting point is documented."""
        summary = mechanism['finding_summary']
        assert '$35B' in summary

    def test_escalation_to_100b(self, mechanism):
        """Validates the $100B escalation target."""
        summary = mechanism['finding_summary']
        assert '$100B' in summary or '100B' in summary

    def test_60b_new_debt(self, mechanism):
        """Reuters Aug 20: Broadcom seeking $60B+ in new AI debt financing."""
        summary = mechanism['finding_summary']
        assert '$60B' in summary or '60B' in summary

    def test_participants_apollo(self, mechanism):
        """Apollo Global Management participates in XPV financing."""
        summary = mechanism['finding_summary']
        assert 'Apollo' in summary

    def test_participants_blackstone(self, mechanism):
        """Blackstone participates in XPV financing."""
        summary = mechanism['finding_summary']
        assert 'Blackstone' in summary

    def test_participants_broadcom(self, mechanism):
        """Broadcom leads the XPV platform."""
        summary = mechanism['finding_summary']
        assert 'Broadcom' in summary

    def test_aug_20_date(self, mechanism):
        """Escalation reported August 20, 2026."""
        summary = mechanism['finding_summary']
        assert 'Aug' in summary and '20' in summary

    def test_reuters_aug20_source(self, mechanism):
        """Reuters Aug 20 source for $60B+ expansion."""
        urls = mechanism['source_urls']
        reuters_aug20 = [u for u in urls if 'reuters.com' in u and '2026-08-20' in u]
        assert len(reuters_aug20) >= 1

    def test_entities_xpv_expansion(self, anthropic):
        """competitor-entities.yaml documents the XPV expansion."""
        spv = anthropic['spv_infrastructure_financing']
        assert 'xpv_debt_expansion_aug_2026' in spv


# =============================================================================
# Class 3: Apollo Compound Publisher Incentive
# =============================================================================
class TestApolloCompoundPublisherIncentive:
    def test_apollo_owns_yahoo(self, mechanism):
        """Apollo owns Yahoo (TechCrunch, Engadget)."""
        summary = mechanism['finding_summary']
        assert 'Yahoo' in summary or 'TechCrunch' in summary

    def test_apollo_finances_anthropic(self, mechanism):
        """Apollo simultaneously finances Anthropic infrastructure."""
        summary = mechanism['finding_summary']
        assert 'Apollo' in summary and 'Anthropic' in summary

    def test_compound_incentive_documented(self, mechanism):
        """The compound incentive (finance + own publishers) is documented."""
        summary = mechanism['finding_summary']
        assert 'compound' in summary.lower() or 'simultaneously' in summary.lower()

    def test_cross_reference_to_305(self, mechanism):
        """Must reference mechanism #305 (Rebecca Bellan vocabulary inversion)."""
        refs = [r for r in mechanism['cross_references'] if r['mechanism_id'] == 305]
        assert len(refs) == 1, "Must reference mechanism #305"

    def test_cross_reference_to_111(self, mechanism):
        """Must reference mechanism #111 (Apollo Q2 2026)."""
        refs = [r for r in mechanism['cross_references'] if r['mechanism_id'] == 111]
        assert len(refs) == 1, "Must reference mechanism #111"

    def test_cross_reference_to_302(self, mechanism):
        """Must reference mechanism #302 (credit facility bank multiplication)."""
        refs = [r for r in mechanism['cross_references'] if r['mechanism_id'] == 302]
        assert len(refs) == 1, "Must reference mechanism #302"

    def test_bellan_vocabulary_delta_referenced(self, mechanism):
        """The Rebecca Bellan vocabulary inversion delta should be referenced."""
        summary = mechanism['finding_summary']
        assert 'Bellan' in summary or '-0.20' in summary or 'vocabulary' in summary.lower()

    def test_techcrunch_engadget_named(self, mechanism):
        """Both TechCrunch and Engadget should be named as Apollo-owned publications."""
        summary = mechanism['finding_summary']
        assert 'TechCrunch' in summary and 'Engadget' in summary


# =============================================================================
# Class 4: Cumulative Anthropic Financial Web
# =============================================================================
class TestCumulativeAnthropicFinancialWeb:
    def test_cumulative_exceeds_300b(self, mechanism):
        """Cumulative financial web exceeds $300B."""
        summary = mechanism['finding_summary']
        assert '$300B' in summary or '300B' in summary

    def test_xpv_original_documented(self, mechanism):
        """$35B original XPV documented."""
        summary = mechanism['finding_summary']
        assert '$35B' in summary

    def test_credit_facility_documented(self, mechanism):
        """$10B+ pre-IPO credit facility documented."""
        summary = mechanism['finding_summary']
        assert '$10B' in summary or '10B' in summary

    def test_nexus_data_center_documented(self, mechanism):
        """$15B Nexus data center (Google-guaranteed) documented."""
        summary = mechanism['finding_summary']
        assert '$15B' in summary or 'Nexus' in summary

    def test_google_chip_deal_documented(self, mechanism):
        """$35B Google chip deal backstop documented."""
        summary = mechanism['finding_summary']
        assert 'chip deal' in summary.lower() or 'Google' in summary

    def test_equity_total_documented(self, mechanism):
        """$65B total equity raised documented."""
        summary = mechanism['finding_summary']
        assert '$65B' in summary or '65B' in summary

    def test_entities_cumulative_financial_web(self, anthropic):
        """competitor-entities.yaml has cumulative financial web section."""
        spv = anthropic['spv_infrastructure_financing']
        assert 'cumulative_financial_web_b' in spv

    def test_entities_cumulative_exceeds_300(self, anthropic):
        """Cumulative total exceeds $300B in entities file."""
        spv = anthropic['spv_infrastructure_financing']
        assert spv['cumulative_financial_web_b'] >= 300


# =============================================================================
# Class 5: IPO Underwriter Credit Facility Convergence
# =============================================================================
class TestIPOUnderwriterCreditFacilityConvergence:
    def test_morgan_stanley_dual_role(self, mechanism):
        """Morgan Stanley leads both credit facility and IPO underwriting."""
        summary = mechanism['finding_summary']
        assert 'Morgan Stanley' in summary

    def test_banks_jockeying_for_ipo(self, mechanism):
        """Credit facility banks are explicitly 'jockeying' for IPO roles (Reuters)."""
        summary = mechanism['finding_summary']
        assert 'jockeying' in summary.lower()

    def test_ipo_oct_2026_target(self, mechanism):
        """IPO target is October 2026."""
        summary = mechanism['finding_summary']
        assert 'October' in summary or 'Oct' in summary

    def test_valuation_range_documented(self, mechanism):
        """Valuation range documented ($965B→$2T)."""
        summary = mechanism['finding_summary']
        assert '$965B' in summary or '$2T' in summary

    def test_thestreet_ipo_source(self, mechanism):
        """TheStreet source for IPO underwriter assignments."""
        urls = mechanism['source_urls']
        thestreet = [u for u in urls if 'thestreet.com' in u]
        assert len(thestreet) >= 1

    def test_wsj_banker_teams_source(self, mechanism):
        """WSJ source for banker team selection dynamics."""
        urls = mechanism['source_urls']
        wsj = [u for u in urls if 'wsj.com' in u]
        assert len(wsj) >= 1

    def test_pymnts_ipo_source(self, mechanism):
        """PYMNTS source for Morgan Stanley / Goldman Sachs IPO roles."""
        urls = mechanism['source_urls']
        pymnts = [u for u in urls if 'pymnts.com' in u]
        assert len(pymnts) >= 1

    def test_nexus_reuters_source(self, mechanism):
        """Reuters Jul 30 source for $15B Nexus data center deal."""
        urls = mechanism['source_urls']
        reuters_nexus = [u for u in urls if 'reuters.com' in u and '2026-07-30' in u]
        assert len(reuters_nexus) >= 1


# =============================================================================
# Class 6: Confounders
# =============================================================================
class TestConfounders:
    def test_has_confounders(self, mechanism):
        assert len(mechanism['confounders']) >= 3

    def test_has_strong_confounders(self, mechanism):
        strong = [c for c in mechanism['confounders'] if c['strength'] == 'STRONG']
        assert len(strong) >= 1, "Must have at least 1 STRONG confounder"

    def test_editorial_independence_confounder(self, mechanism):
        """Editorial independence must be acknowledged."""
        confounders = mechanism['confounders']
        editorial = [c for c in confounders if 'editorial' in c['description'].lower()]
        assert len(editorial) >= 1

    def test_multi_hop_confounder(self, mechanism):
        """Multi-hop transmission between PE financing and editorial output."""
        confounders = mechanism['confounders']
        multi_hop = [c for c in confounders if 'multi-hop' in c['description'].lower() or
                     'hop' in c['description'].lower() or
                     'indirect' in c['description'].lower()]
        assert len(multi_hop) >= 1

    def test_competing_incentives_confounder(self, mechanism):
        """Competing incentives must be acknowledged."""
        confounders = mechanism['confounders']
        competing = [c for c in confounders if 'competing' in c['description'].lower() or
                     'diversif' in c['description'].lower() or
                     'counter' in c['description'].lower()]
        assert len(competing) >= 1
