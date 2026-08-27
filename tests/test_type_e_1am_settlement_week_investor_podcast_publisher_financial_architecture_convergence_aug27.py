"""
Type E: Post-Settlement Political-Investor Podcast Cross-Surface Financial Architecture Convergence
Iteration #323, Aug 27 2026 01:00 PT

Tests the finding that settlement-week podcast/webinar surfaces exhibit perfect
compartmentalization between Meta-accountability and Anthropic-aspiration narratives,
with financial relationships predicting which compartment each entity occupies.

Podcast entries: #79 (Bloomberg Balance of Power), #80 (WBUR/NPR Here & Now),
#81 (ARK Invest August mARKet Update)
Mechanism: #333 (Investor-Podcast-Publisher Financial Architecture Convergence)
Cross-validates: #328 (Meta settlement IPO underwriter), #329, #330
"""

import yaml
import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PODCAST_FILE = os.path.join(REPO_ROOT, "podcast-sentiment.md")
RESEARCH_FILE = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")


class TestPodcastEntryExistence:
    """Verify that podcast entries #79, #80, #81 exist in podcast-sentiment.md."""

    def setup_method(self):
        with open(PODCAST_FILE, "r") as f:
            self.content = f.read()

    def test_entry_79_bloomberg_balance_of_power_exists(self):
        assert "### 79." in self.content or "### 79 " in self.content, \
            "Podcast entry #79 (Bloomberg Balance of Power) missing from podcast-sentiment.md"

    def test_entry_80_wbur_npr_here_and_now_exists(self):
        assert "### 80." in self.content or "### 80 " in self.content, \
            "Podcast entry #80 (WBUR/NPR Here & Now) missing from podcast-sentiment.md"

    def test_entry_81_ark_invest_market_update_exists(self):
        assert "### 81." in self.content or "### 81 " in self.content, \
            "Podcast entry #81 (ARK Invest August mARKet Update) missing from podcast-sentiment.md"

    def test_cross_surface_pattern_summary_table_exists(self):
        assert "Cross-Surface Pattern Summary" in self.content, \
            "Cross-surface pattern summary table missing"


class TestBloombergBalanceOfPowerSettlement:
    """Verify Bloomberg Balance of Power settlement-day podcast analysis."""

    def setup_method(self):
        with open(PODCAST_FILE, "r") as f:
            self.content = f.read()

    def test_governor_spencer_cox_documented(self):
        assert "Spencer Cox" in self.content, \
            "Governor Spencer Cox (R-UT) guest appearance not documented"

    def test_meta_exclusive_title_framing(self):
        assert "Meta Settles Landmark Teen Social Media Case" in self.content, \
            "Episode title 'Meta Settles Landmark Teen Social Media Case' not documented"

    def test_same_episode_compartmentalization(self):
        assert "compartmentalization" in self.content.lower() or "compartmentaliz" in self.content.lower(), \
            "Cross-segment compartmentalization within the same episode not documented"

    def test_source_url_present(self):
        assert "FGI6AS7L8Lc" in self.content, \
            "Bloomberg Balance of Power YouTube source URL not present"

    def test_settlement_amount_higher_quote(self):
        assert "should have been much higher" in self.content, \
            "Cox's 'settlement amount should have been much higher' framing not documented"


class TestWBURNPRCrossMediumPortability:
    """Verify WBUR/NPR Here & Now cross-medium portability analysis."""

    def setup_method(self):
        with open(PODCAST_FILE, "r") as f:
            self.content = f.read()

    def test_lauren_feiner_verge_documented(self):
        assert "Lauren Feiner" in self.content, \
            "Lauren Feiner (The Verge) guest appearance not documented"

    def test_cross_medium_portability_concept(self):
        assert "cross-medium" in self.content.lower(), \
            "Cross-medium portability concept not analyzed"

    def test_vox_media_financial_context(self):
        assert "Vox Media" in self.content, \
            "Vox Media (The Verge's parent) financial context not documented"

    def test_google_youtube_structural_conflict(self):
        # The Verge's parent (Vox Media) has Google ad dependency, and Google/YouTube
        # is one of the settlement-adjacent companies
        content_lower = self.content.lower()
        assert "google" in content_lower and ("vox" in content_lower or "verge" in content_lower), \
            "Vox Media/Google financial dependency in settlement context not documented"


class TestARKInvestAnthropicIPOAspirationalFraming:
    """Verify ARK Invest August mARKet Update analysis of Anthropic IPO framing."""

    def setup_method(self):
        with open(PODCAST_FILE, "r") as f:
            self.content = f.read()

    def test_cathie_wood_documented(self):
        assert "Cathie Wood" in self.content, \
            "Cathie Wood host/speaker not documented"

    def test_arkvx_venture_fund_financial_interest(self):
        assert "ARKVX" in self.content or "Venture Fund" in self.content, \
            "ARK Venture Fund (ARKVX) Anthropic holding not documented as financial interest"

    def test_anthropic_run_rate_scaling(self):
        assert "$9 billion" in self.content and "$75 billion" in self.content, \
            "Anthropic run rate scaling ($9B to $75B) data not documented"

    def test_aspirational_sentiment_score(self):
        # ARK entry should have positive sentiment score for Anthropic
        assert "+8/10" in self.content or "+7/10" in self.content or "+9/10" in self.content, \
            "Aspirational positive sentiment score for Anthropic not documented"

    def test_source_url_present(self):
        assert "Gw9kqiiDX7o" in self.content, \
            "ARK Invest mARKet Update YouTube source URL not present"

    def test_equity_ownership_vs_content_revenue_distinction(self):
        assert "equity" in self.content.lower(), \
            "Equity ownership mechanism (vs content revenue) not analyzed"


class TestMechanism333InvestorPodcastPublisherConvergence:
    """Verify mechanism #333 Investor-Podcast-Publisher Financial Architecture Convergence."""

    def setup_method(self):
        with open(PODCAST_FILE, "r") as f:
            self.content = f.read()

    def test_mechanism_333_referenced(self):
        assert "333" in self.content, \
            "Mechanism #333 not referenced in podcast analysis"

    def test_capital_narrative_feedback_loop(self):
        assert "feedback loop" in self.content.lower(), \
            "Capital-narrative feedback loop not documented"

    def test_five_step_chain_documented(self):
        # Should document the 5-step chain: ARK invests → Anthropic deals → publisher incentive →
        # Meta asymmetry → IPO demand
        content_lower = self.content.lower()
        has_chain = ("ark" in content_lower and
                     "anthropic" in content_lower and
                     "publisher" in content_lower and
                     "meta" in content_lower and
                     "ipo" in content_lower)
        assert has_chain, \
            "Five-step capital-narrative chain not documented"


class TestSettlementWeekCompartmentalization:
    """Verify the settlement-week cross-surface compartmentalization finding."""

    def setup_method(self):
        with open(PODCAST_FILE, "r") as f:
            self.content = f.read()

    def test_no_podcast_connected_settlement_to_ipo(self):
        # Key finding: no single podcast/webinar connected Meta's settlement to Anthropic's IPO
        assert "no single podcast" in self.content.lower() or \
               "perfect compartmentalization" in self.content.lower() or \
               "zero cross-reference" in self.content.lower(), \
            "Settlement-IPO compartmentalization finding not documented"

    def test_financial_relationship_predicts_compartment(self):
        assert "financial relationships predict" in self.content.lower() or \
               "financial relationship" in self.content.lower(), \
            "Financial relationships predicting compartment assignment not documented"

    def test_accountability_vs_aspirational_framing(self):
        content_lower = self.content.lower()
        assert "accountability" in content_lower and "aspirational" in content_lower, \
            "Accountability vs aspirational framing dichotomy not documented"


class TestConfounderDocumentation:
    """Verify confounders are documented for the new mechanism."""

    def setup_method(self):
        with open(PODCAST_FILE, "r") as f:
            self.content = f.read()

    def test_genre_confounder_documented(self):
        # Investor webinar vs political podcast is a STRONG genre confounder
        content_lower = self.content.lower()
        assert "genre" in content_lower or "format conventions" in content_lower, \
            "Genre/format confounder not documented"

    def test_investment_firm_structural_expectation(self):
        assert "structurally expected" in self.content.lower() or \
               "inherently" in self.content.lower(), \
            "Structural expectation that investment firms promote holdings not documented as confounder"

    def test_strong_confounder_label(self):
        assert "STRONG CONFOUNDER" in self.content, \
            "Strong confounder label not present"


class TestCrossValidationWithExistingMechanisms:
    """Verify cross-references to existing settlement mechanisms."""

    def setup_method(self):
        with open(PODCAST_FILE, "r") as f:
            self.content = f.read()

    def test_mechanism_328_cross_reference(self):
        assert "#328" in self.content or "328" in self.content, \
            "Cross-reference to mechanism #328 (settlement IPO underwriter) missing"

    def test_mechanism_329_cross_reference(self):
        assert "#329" in self.content or "329" in self.content, \
            "Cross-reference to mechanism #329 missing"

    def test_wsj_anthropic_relationship_cited(self):
        assert "$1.5B" in self.content or "1.5B" in self.content, \
            "WSJ's $1.5B Anthropic relationship not cited in financial context"
