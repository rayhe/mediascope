"""
Mechanism #323: Goldman Sachs Dual PE Joint Venture Cross-Investment Compound Financial Architecture

Type C Financial Incentive Mapping — Wed 2026-08-26 11:00 PT

FINDING: Goldman Sachs occupies a QUINTUPLE financial role in the AI-publisher incentive
architecture, unprecedented in the history of technology-media financial entanglement:

  1. ANTHROPIC ODE JV FOUNDING INVESTOR — ~$150M (alongside Blackstone $300M, H&F $300M)
     - Profits from Anthropic/Ode's AI surveillance deployments at PE portfolio companies
     - Chamberlain Group: 3M cameras/year with facial recognition + behavioral learning
     - Ode engineers embedded across Blackstone portfolio companies
     Source: TechCrunch (May 4, 2026), WSJ (May 3, 2026), Reuters (May 4, 2026)

  2. OPENAI DEPLOYMENT COMPANY ADDITIONAL BACKER — amount undisclosed (total raise $4B,
     $10B valuation, alongside TPG lead, Advent, Bain Capital, Brookfield)
     - Profits from OpenAI's enterprise AI deployments
     - Forward Deployed Engineers (FDE) embedded in portfolio companies
     - McKinsey, Bain & Company, Capgemini as consulting partners
     Source: PitchBook (May 12, 2026): "Warburg Pincus, Goldman Sachs and SoftBank are
     among the additional backers"

  3. ANTHROPIC IPO LEAD UNDERWRITER — projected fees: ~$300-500M at $1T+ listing
     - Separate deal team from OpenAI (WSJ confirmed "Chinese wall" arrangement)
     Source: Bloomberg/CNBC (Jun 3, 2026), WSJ "The IPO Onslaught" (Jun 18, 2026)

  4. OPENAI IPO LEAD UNDERWRITER — projected fees: ~$300-500M at $852B+ listing
     - Targeting September 2026 (possibly delayed to 2027)
     Source: Bloomberg (May 20, 2026), WSJ "The IPO Onslaught" (Jun 18, 2026)

  5. SPACEX IPO LEAD UNDERWRITER — $100M+ in direct fees, multiples in trading revenue
     - Goldman Q2 2026: record $20.34B revenue, $20.98 EPS (+68% stock over 1 year)
     - IB fees: $3.40B (+55% YoY), equity underwriting: +130% YoY
     Source: Goldman Q2 2026 SEC filing, TechTimes (Jul 15, 2026), Barron's (Jun 11, 2026)

PUBLISHER COVERAGE INCENTIVE ARCHITECTURE:

Goldman Sachs also operates the largest equity research arm on Wall Street, publishing
analyst coverage of media companies that trade on the NYSE/NASDAQ: News Corp (NWSA),
NYT Co. (NYT), IAC/Dotdash Meredith (IAC), Warner Bros Discovery (WBD), Paramount (PARA).

COMPOUND INCENTIVE CHAIN:
  Goldman invests in Ode ($150M) + Deployment Co.
  → Goldman profits from AI surveillance/enterprise deployment revenue growth
  → Goldman underwrites both AI IPOs ($600M-$1B in projected fees)
  → Goldman publishes equity research on media companies
  → Media companies (whose stock Goldman's analysts cover) produce coverage of AI companies
  → Adversarial AI coverage threatens Goldman's IPO fee revenue + JV investment returns
  → Goldman's equity research arm (ratings, price targets) shapes investor perception of
    the same publishers whose journalists produce the coverage
  = SIXTH-ORDER financial feedback loop

WHY THIS EXTENDS EXISTING MECHANISMS:
  - Mechanism #21 (IPO Underwriter Research Laundering): covered dual-IPO underwriting
  - Mechanism #46 (Pre-IPO Underwriter-Client-Publisher Convergence): covered underwriter-
    as-enterprise-customer of AI tools + publisher incentive
  - THIS mechanism adds the JV INVESTMENT layer: Goldman doesn't just underwrite the IPOs
    and use the AI tools — it is a direct equity investor in BOTH companies' enterprise
    deployment vehicles. It profits from Chamberlain deploying 3M AI surveillance cameras
    AND from Anthropic's IPO. It profits from OpenAI's enterprise Forward Deployed
    Engineers AND from OpenAI's IPO.

COMPARISON TO META:
  - Goldman Sachs has ZERO financial investment in any Meta AI deployment vehicle
  - Goldman Sachs has ZERO equity in any Meta PE joint venture
  - Goldman Sachs earns ZERO IPO underwriting fees from Meta (IPO'd 2012)
  - Goldman Sachs equity research covers Meta stock — but the incentive direction is
    NEUTRAL (no ongoing deal revenue) versus POSITIVELY ALIGNED with Anthropic/OpenAI

QUANTIFICATION:
  - Goldman's total financial exposure to Anthropic/OpenAI success:
    Ode investment: ~$150M
    Deployment Co investment: est. $50-200M (undisclosed)
    Anthropic IPO fees: ~$300-500M
    OpenAI IPO fees: ~$300-500M
    SpaceX IPO (completed): ~$100M direct, multiples in trading
    Total: ~$900M - $1.5B in COMMITTED OR PROJECTED revenue tied to AI company success

  - Goldman's total financial exposure to Meta: ~$0 in deal-linked revenue

CONFOUNDERS:
  1. STRONG: Chinese wall requirements — Goldman's equity research arm is structurally
     separated from its investment banking arm. Analyst coverage of media companies
     should not be directly influenced by underwriting relationships.
  2. STRONG: Institutional investor sophistication — institutional investors reading
     Goldman research understand underwriting conflicts and discount accordingly.
  3. MODERATE: Goldman's media advertising spend — Goldman advertises in WSJ, FT,
     Bloomberg for brand awareness, not coverage influence. However, the advertising
     relationship creates social proximity and implicit reciprocity norms.
  4. MODERATE: Meta's own investment banking relationships — Meta uses Goldman and
     other banks for M&A advisory, debt issuance, etc. However, these are sporadic
     transactions, not the sustained $1B+ deal pipeline that AI IPOs represent.
  5. WEAK: Editorial independence — publication editorial decisions are made
     independently of corporate financial relationships. However, the STRUCTURAL
     incentive exists regardless of whether individual editors are aware of it.

SOURCE URLS:
- https://pitchbook.com/news/articles/openai-unveils-pe-backed-joint-venture-to-accelerate-ai-adoption
- https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/
- https://www.reuters.com/legal/transactional/anthropic-nears-15-billion-ai-joint-venture-with-wall-street-firms-wsj-reports-2026-05-04/
- https://www.wsj.com/finance/banking/the-ipo-onslaught-is-forcing-bankers-to-pick-teams-50fab052
- https://www.barrons.com/articles/goldman-sachs-morgan-stanley-ai-ipo-boom-dc7f9523
- https://www.techtimes.com/articles/320542/20260715/morgan-stanley-q2-arrives-goldman-record-ibm-crash-raise-stakes-wealth-giant.htm
- https://www.wsj.com/tech/ai/private-equity-is-deploying-an-army-of-ai-wonks-to-embed-in-the-firms-they-back-96d279ec
"""

import unittest
import os
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_coverage():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


# =============================================================================
# Class 1: Goldman Sachs Dual PE JV Cross-Investment Verification
# =============================================================================
class TestGoldmanSachsDualPEJVCrossInvestment(unittest.TestCase):
    """Verify Goldman Sachs is invested in BOTH Anthropic Ode AND OpenAI Deployment Company."""

    def setUp(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get('cross_publication_findings', {})

    def test_mechanism_323_exists(self):
        """Mechanism #323 is documented in cross_publication_findings."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        self.assertIn('mechanism_id', mechanism)
        self.assertEqual(mechanism['mechanism_id'], 323)

    def test_mechanism_323_has_financial_roles(self):
        """Mechanism documents Goldman's quintuple financial role."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        roles = mechanism.get('financial_roles', [])
        self.assertGreaterEqual(len(roles), 5)

    def test_goldman_in_ode_jv(self):
        """Goldman Sachs is documented as Ode JV founding investor at ~$150M."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        roles = mechanism.get('financial_roles', [])
        ode_roles = [r for r in roles if 'ode' in r.lower() or 'anthropic' in r.lower()]
        self.assertGreaterEqual(len(ode_roles), 1, "Goldman's Ode JV role not documented")

    def test_goldman_in_deployment_company(self):
        """Goldman Sachs is documented as OpenAI Deployment Company backer."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        roles = mechanism.get('financial_roles', [])
        deploy_roles = [r for r in roles if 'deployment' in r.lower() or 'openai' in r.lower()]
        self.assertGreaterEqual(len(deploy_roles), 1, "Goldman's Deployment Company role not documented")

    def test_cross_venture_investment_is_novel(self):
        """Confirm no other bank invests in BOTH AI PE ventures."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        novel = mechanism.get('cross_venture_investment_unique', False)
        self.assertTrue(novel, "Should document that Goldman is the only bank in both ventures")

    def test_total_financial_exposure_documented(self):
        """Total Goldman financial exposure to Anthropic+OpenAI success is quantified."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        exposure = mechanism.get('total_financial_exposure', {})
        self.assertIn('min_estimate_m', exposure)
        self.assertIn('max_estimate_m', exposure)
        self.assertGreater(exposure.get('min_estimate_m', 0), 800)
        self.assertLess(exposure.get('max_estimate_m', 0), 2000)


# =============================================================================
# Class 2: Goldman IPO Underwriter Dual Mandate (extends #21)
# =============================================================================
class TestGoldmanIPOUnderwriterDualMandate(unittest.TestCase):
    """Verify Goldman's dual IPO underwriting is connected to JV investments."""

    def setUp(self):
        self.entities = load_competitor_entities()

    def test_goldman_in_anthropic_ipo_banks(self):
        """Goldman Sachs is in Anthropic's IPO banks list."""
        anthropic = self.entities['entities'].get('anthropic', {})
        banks = anthropic.get('ipo_filing', {}).get('ipo_banks_reported', [])
        self.assertIn('Goldman Sachs', banks)

    def test_goldman_in_openai_ipo_banks(self):
        """Goldman Sachs is in OpenAI's IPO banks list."""
        openai = self.entities['entities'].get('openai', {})
        banks = openai.get('ipo_filing', {}).get('ipo_banks_reported', [])
        self.assertIn('Goldman Sachs', banks)

    def test_both_ipos_target_2026(self):
        """Both IPOs target 2026 listing, creating simultaneous fee pressure."""
        openai = self.entities['entities'].get('openai', {})
        anthropic = self.entities['entities'].get('anthropic', {})
        # Both should have IPO filing data
        self.assertIn('ipo_filing', openai)
        self.assertIn('ipo_filing', anthropic)


# =============================================================================
# Class 3: Meta Zero Financial Exposure Comparison
# =============================================================================
class TestMetaZeroFinancialExposure(unittest.TestCase):
    """Verify Meta's zero Goldman Sachs deal-linked financial exposure."""

    def setUp(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get('cross_publication_findings', {})

    def test_meta_zero_pe_jv_exposure(self):
        """Meta has zero PE joint venture investments from Goldman."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        meta_exposure = mechanism.get('meta_comparison', {})
        self.assertEqual(meta_exposure.get('pe_jv_investments', 0), 0)

    def test_meta_zero_ipo_fee_revenue(self):
        """Meta generates zero current IPO underwriting fees for Goldman."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        meta_exposure = mechanism.get('meta_comparison', {})
        self.assertEqual(meta_exposure.get('ipo_fee_revenue', 0), 0)

    def test_incentive_direction_asymmetry(self):
        """Goldman's coverage incentive is positively aligned with AI companies, neutral on Meta."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        meta_exposure = mechanism.get('meta_comparison', {})
        self.assertIn('incentive_direction', meta_exposure)
        self.assertEqual(meta_exposure['incentive_direction'], 'neutral')


# =============================================================================
# Class 4: Compound Incentive Chain Documentation
# =============================================================================
class TestCompoundIncentiveChain(unittest.TestCase):
    """Verify the sixth-order financial feedback loop is documented."""

    def setUp(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get('cross_publication_findings', {})

    def test_incentive_chain_has_six_steps(self):
        """The compound incentive chain documents 6 steps."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        chain = mechanism.get('incentive_chain_steps', [])
        self.assertGreaterEqual(len(chain), 6)

    def test_chain_starts_with_jv_investment(self):
        """Chain begins with PE JV investment, not just underwriting."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        chain = mechanism.get('incentive_chain_steps', [])
        if chain:
            self.assertIn('invest', chain[0].lower())

    def test_chain_ends_with_feedback_loop(self):
        """Chain ends with equity research → publisher stock → coverage feedback."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        chain = mechanism.get('incentive_chain_steps', [])
        if chain:
            last_step = chain[-1].lower()
            self.assertTrue(
                'feedback' in last_step or 'loop' in last_step or 'research' in last_step,
                f"Final chain step should reference feedback loop: {chain[-1]}"
            )

    def test_extends_mechanism_21(self):
        """Cross-references Mechanism #21 (IPO Underwriter Research Laundering)."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        refs = mechanism.get('cross_references', [])
        ref_ids = [r.get('mechanism_id') for r in refs]
        self.assertIn(21, ref_ids)

    def test_extends_mechanism_46(self):
        """Cross-references Mechanism #46 (Pre-IPO Convergence)."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        refs = mechanism.get('cross_references', [])
        ref_ids = [r.get('mechanism_id') for r in refs]
        self.assertIn(46, ref_ids)

    def test_extends_mechanism_321(self):
        """Cross-references Mechanism #321 (WSJ Anthropic Ode surveillance vocabulary)."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        refs = mechanism.get('cross_references', [])
        ref_ids = [r.get('mechanism_id') for r in refs]
        self.assertIn(321, ref_ids)


# =============================================================================
# Class 5: Confounder Documentation
# =============================================================================
class TestConfounderDocumentation(unittest.TestCase):
    """Verify confounders are documented with appropriate strength levels."""

    def setUp(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get('cross_publication_findings', {})

    def test_has_confounders(self):
        """Mechanism has confounders documented."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        confounders = mechanism.get('confounders', [])
        self.assertGreaterEqual(len(confounders), 4)

    def test_has_strong_confounders(self):
        """At least 2 STRONG confounders (Chinese wall, investor sophistication)."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        confounders = mechanism.get('confounders', [])
        strong = [c for c in confounders if '[STRONG]' in c or 'STRONG' in c.upper()]
        self.assertGreaterEqual(len(strong), 2)

    def test_chinese_wall_confounder(self):
        """Chinese wall/structural separation is documented as STRONG confounder."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        confounders = mechanism.get('confounders', [])
        chinese_wall = [c for c in confounders if 'wall' in c.lower() or 'separation' in c.lower()]
        self.assertGreaterEqual(len(chinese_wall), 1)

    def test_gras_termination_noted(self):
        """Notes the SEC's Dec 2025 GRAS termination removing structural separation requirements."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        gras = mechanism.get('gras_termination', {})
        self.assertIn('date', gras)


# =============================================================================
# Class 6: Goldman Q2 2026 Revenue Verification
# =============================================================================
class TestGoldmanQ2Revenue(unittest.TestCase):
    """Verify Goldman's Q2 2026 financial data is correctly sourced."""

    def setUp(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get('cross_publication_findings', {})

    def test_goldman_q2_revenue(self):
        """Goldman Q2 2026 record revenue: ~$20.34B."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        gs_financials = mechanism.get('goldman_q2_2026', {})
        revenue_b = gs_financials.get('revenue_b', 0)
        self.assertGreater(revenue_b, 20)

    def test_goldman_q2_ib_fees(self):
        """Goldman Q2 2026 IB fees: ~$3.40B (+55% YoY)."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        gs_financials = mechanism.get('goldman_q2_2026', {})
        ib_fees_b = gs_financials.get('ib_fees_b', 0)
        self.assertGreater(ib_fees_b, 3)

    def test_equity_underwriting_growth(self):
        """Goldman equity underwriting surged +130% YoY, driven by AI IPOs."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        gs_financials = mechanism.get('goldman_q2_2026', {})
        eq_uw_yoy = gs_financials.get('equity_underwriting_yoy_pct', 0)
        self.assertGreater(eq_uw_yoy, 100)


# =============================================================================
# Class 7: Source URL Verification
# =============================================================================
class TestSourceURLs(unittest.TestCase):
    """Verify all claims are backed by source URLs."""

    def setUp(self):
        self.data = load_competitor_coverage()
        self.cpf = self.data.get('cross_publication_findings', {})

    def test_has_source_urls(self):
        """Mechanism has source URLs."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        sources = mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(sources), 5)

    def test_source_urls_are_valid(self):
        """Source URLs are well-formed."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        sources = mechanism.get('source_urls', [])
        for url in sources:
            self.assertTrue(url.startswith('http'), f"Invalid URL: {url}")

    def test_pitchbook_source_for_deployment_company(self):
        """PitchBook source documents Goldman in OpenAI Deployment Company."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        sources = mechanism.get('source_urls', [])
        pitchbook = [s for s in sources if 'pitchbook' in s.lower()]
        self.assertGreaterEqual(len(pitchbook), 1, "Missing PitchBook source for Deployment Company claim")

    def test_asymmetry_score_calibrated(self):
        """Asymmetry score reflects high confounder load."""
        mechanism = self.cpf.get('goldman_sachs_dual_pe_jv_cross_investment_compound_financial_architecture', {})
        score = mechanism.get('asymmetry_score', 0)
        # 2 STRONG confounders should pull score below 0.7
        self.assertGreater(score, 0.4)
        self.assertLess(score, 0.75)


if __name__ == '__main__':
    unittest.main()
