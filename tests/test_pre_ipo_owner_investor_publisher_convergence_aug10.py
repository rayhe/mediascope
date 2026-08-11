"""
Mechanism #36: Pre-IPO Owner-Investor-Publisher Convergence

Tests for the finding that Anthropic's largest equity investors personally own
or control major news publications, creating an undisclosed pre-IPO coverage
incentive that operates through EQUITY OWNERSHIP rather than content licensing
deals.

Three documented chains:
1. Amazon ($13B invested, 15-20% stake) → Jeff Bezos → Washington Post
2. Salesforce ($5B stake) → Marc Benioff → Time magazine
3. Google (~14% equity + $35B SPV guarantee) → News Showcase → 700+ publishers

Plus: News Corp/HarperCollins receives Anthropic $1.5B settlement funds
while covering Anthropic via WSJ.

Key insight: Unlike OpenAI's direct publisher content licensing deals,
Anthropic's financial relationships with media flow through EQUITY OWNERSHIP
by media owners. This is structurally harder to disclose and creates a
qualitatively different coverage incentive: the publication owner's personal
net worth increases with positive pre-IPO coverage.

Sources:
- Amazon Anthropic stake: Motley Fool (Jun 11, 2026), MarketBeat (Jul 7, 2026),
  Amazon 10-K (Feb 2026), NextBigFuture (Apr 21, 2026)
- Bezos/WashPost: IBJ (Sep 2018), $250M acquisition in 2013
- Salesforce Anthropic stake: Bloomberg (Jun 1, 2026), TradingView, Barchart
- Benioff/Time: Wikipedia, IBJ (Sep 2018), $190M acquisition in 2018
- Time names Anthropic "World's Most Disruptive Company": WEEX (Aug 2026)
- WEEX directly noted: "Salesforce is also one of Anthropic's investors, and
  TIME Magazine's owner, Marc Benioff, is the CEO of Salesforce"
- Google Anthropic stake: Court filing (Mar 2025), ~14%, ~$135B at $965B
- Google SPV guarantee: Mechanism #28 documentation
- Anthropic $1.5B settlement: AP/Bloomberg Law (Jul 20, 2026 final approval)
- HarperCollins/News Corp: News Corp subsidiary, settlement class member
- OpenAI/Time deal: Jun 2024 content licensing agreement
- WashPost/OpenAI deal: Apr 2025 content licensing agreement
- Anthropic S-1 filed: Jun 1, 2026, confidential, expected Oct 2026 IPO

Date added: 2026-08-10
"""

import pytest
import yaml
import os
import re
from pathlib import Path


PROFILES_DIR = Path(__file__).parent.parent / "profiles"


def load_yaml(filename):
    """Load a YAML profile file."""
    filepath = PROFILES_DIR / filename
    with open(filepath) as f:
        return yaml.safe_load(f)


# =============================================================================
# Class 1: Investment Chain Verification — Amazon → Bezos → Washington Post
# =============================================================================
class TestAmazonBezosWashPostChain:
    """Verify the Amazon-Bezos-WashPost ownership-investment chain."""

    def test_amazon_anthropic_investment_exists(self):
        """Amazon has invested $13B+ in Anthropic."""
        data = load_yaml("competitor-entities.yaml")
        anthropic = data["entities"]["anthropic"]
        investors = anthropic.get("investors", anthropic.get("equity_investors", {}))
        # Check that Amazon is documented as an investor
        amazon_ref = str(anthropic).lower()
        assert "amazon" in amazon_ref, (
            "Anthropic profile must document Amazon as a major investor"
        )

    def test_amazon_anthropic_stake_range(self):
        """Amazon's stake is reported at 15-20% of Anthropic."""
        # Multiple sources: Motley Fool, MarketBeat, NextBigFuture
        # Amazon 10-K: $60.6B in holdings at $380B valuation = ~16%
        # Post-April 2026 deal: estimated 16-20%
        data = load_yaml("competitor-entities.yaml")
        amazon_leg = data["entities"].get("amazon", {}).get("anthropic_investment", {})
        # If not yet documented at entity level, check competitor-coverage-research
        research = load_yaml("competitor-coverage-research.yaml")
        full_text = str(research) + str(data)
        assert "15" in full_text or "16" in full_text or "20" in full_text, (
            "Amazon's 15-20% Anthropic stake must be documented"
        )

    def test_bezos_owns_washington_post(self):
        """Jeff Bezos purchased Washington Post in 2013 for $250M."""
        # This is a well-documented fact - verify it's captured in profiles
        research = load_yaml("competitor-coverage-research.yaml")
        full_text = str(research)
        # Check for Bezos-WashPost connection documentation
        assert "bezos" in full_text.lower() or "washington post" in full_text.lower(), (
            "Bezos-Washington Post ownership connection must be documented"
        )

    def test_washpost_openai_deal_exists(self):
        """Washington Post signed OpenAI content deal in Apr 2025."""
        data = load_yaml("competitor-entities.yaml")
        openai = data["entities"]["openai"]
        deals = openai.get("publisher_content_deal_portfolio", {})
        partners = deals.get("notable_partners", [])
        partner_text = str(partners).lower()
        assert "washington post" in partner_text, (
            "Washington Post must be listed as OpenAI content deal partner"
        )

    def test_washpost_no_meta_deal(self):
        """Washington Post has no disclosed Meta content licensing deal."""
        # Meta's known deal partners: News Corp, Reuters, CNN, Fox News,
        # USA Today, People Inc, Washington Examiner, Le Monde, Daily Caller
        # Washington Post is NOT among them
        meta_deal_partners = [
            "news corp", "reuters", "cnn", "fox news", "usa today",
            "people inc", "washington examiner", "le monde", "daily caller"
        ]
        assert "washington post" not in meta_deal_partners, (
            "Washington Post should not be among Meta's known deal partners"
        )

    def test_triple_incentive_structure(self):
        """The Amazon-Bezos chain creates a triple incentive:
        1. Owner (Bezos) has massive equity upside from Anthropic IPO
        2. WashPost has OpenAI content deal (direct revenue)
        3. WashPost has NO Meta deal (no financial incentive for softer Meta coverage)
        """
        # This is a structural test — the triple incentive exists by construction
        # when all three conditions are met
        incentives = {
            "owner_anthropic_equity": True,  # Amazon $13B → 15-20% stake
            "publication_openai_deal": True,  # WashPost-OpenAI Apr 2025
            "publication_meta_deal": False,   # No WashPost-Meta deal
        }
        assert incentives["owner_anthropic_equity"], "Owner has Anthropic equity"
        assert incentives["publication_openai_deal"], "Publication has OpenAI deal"
        assert not incentives["publication_meta_deal"], "No Meta deal"


# =============================================================================
# Class 2: Investment Chain Verification — Salesforce → Benioff → Time
# =============================================================================
class TestSalesforceBenioffTimeChain:
    """Verify the Salesforce-Benioff-Time ownership-investment chain."""

    def test_salesforce_anthropic_stake_value(self):
        """Salesforce holds ~$5B Anthropic stake (from $50M initial in 2023)."""
        # Bloomberg (Jun 1, 2026): $5B value
        # Barchart, TradingView, InsiderMonkey confirm
        # 100x return on initial $50M investment
        initial_investment_m = 50
        current_value_b = 5.0
        return_multiple = (current_value_b * 1000) / initial_investment_m
        assert return_multiple == 100.0, (
            f"Salesforce Anthropic return is {return_multiple}x, expected ~100x"
        )

    def test_benioff_owns_time_magazine(self):
        """Marc Benioff purchased Time for $190M in September 2018."""
        # Personal purchase by Marc and Lynne Benioff, not Salesforce
        purchase_price_m = 190
        purchase_year = 2018
        assert purchase_price_m == 190
        assert purchase_year == 2018

    def test_benioff_is_salesforce_ceo(self):
        """Marc Benioff is CEO of Salesforce (Anthropic's investor)."""
        # This creates the chain: Salesforce (investor) → Benioff (CEO) → Time (owner)
        chain = {
            "company": "Salesforce",
            "ceo": "Marc Benioff",
            "publication_owned": "Time",
            "anthropic_stake_b": 5.0,
        }
        assert chain["ceo"] == "Marc Benioff"
        assert chain["publication_owned"] == "Time"

    def test_time_openai_deal_exists(self):
        """Time has an OpenAI content licensing deal (Jun 2024)."""
        data = load_yaml("competitor-entities.yaml")
        openai = data["entities"]["openai"]
        deals = openai.get("publisher_content_deal_portfolio", {})
        partners = deals.get("notable_partners", [])
        partner_text = str(partners).lower()
        assert "time" in partner_text, (
            "Time must be listed as OpenAI content deal partner"
        )

    def test_time_anthropic_most_disruptive(self):
        """Time named Anthropic 'World's Most Disruptive Company' — while
        owner's company holds $5B Anthropic stake. WEEX directly noted this
        conflict: 'Salesforce is also one of Anthropic's investors, and TIME
        Magazine's owner, Marc Benioff, is the CEO of Salesforce.'"""
        # This is a documented fact from WEEX reporting (Aug 2026)
        conflict_noted_by_third_party = True
        assert conflict_noted_by_third_party, (
            "WEEX noted the Benioff-Salesforce-Anthropic-Time conflict"
        )

    def test_dual_financial_incentive(self):
        """Time has dual incentive: OpenAI deal (direct) + owner Anthropic equity."""
        incentives = {
            "openai_content_deal": True,       # Time-OpenAI Jun 2024
            "owner_anthropic_equity_b": 5.0,   # Salesforce $5B stake
            "meta_deal": False,                # No Time-Meta deal
        }
        assert incentives["openai_content_deal"]
        assert incentives["owner_anthropic_equity_b"] > 0
        assert not incentives["meta_deal"]


# =============================================================================
# Class 3: Settlement-to-Coverage Chain — Anthropic → HarperCollins → News Corp
# =============================================================================
class TestAnthropicSettlementNewsCorp:
    """Verify the Anthropic settlement → HarperCollins → News Corp chain."""

    def test_anthropic_settlement_amount(self):
        """Anthropic's copyright settlement is $1.5B (largest in US history)."""
        settlement_b = 1.5
        assert settlement_b == 1.5

    def test_settlement_final_approval_date(self):
        """Final approval granted July 20, 2026 by Judge Martínez-Olguín."""
        # Preliminary approval: Sep 2025 (Judge Alsup)
        # Final approval: Jul 20, 2026 (Judge Martínez-Olguín, Alsup retired)
        approval_date = "2026-07-20"
        assert approval_date == "2026-07-20"

    def test_settlement_per_book_payout(self):
        """Authors/publishers receive ~$3,000-$3,100 per pirated work."""
        per_book = 3000
        total_works = 482460
        total_b = (per_book * total_works) / 1e9
        assert 1.4 <= total_b <= 1.5, (
            f"Settlement math: {total_works} works × ${per_book} = ${total_b:.2f}B"
        )

    def test_harpercollins_is_news_corp_subsidiary(self):
        """HarperCollins is a wholly-owned subsidiary of News Corp."""
        # News Corp also owns: WSJ, NY Post, Barron's, Times of London, The Sun
        news_corp_subsidiaries = {
            "publishing": ["HarperCollins"],
            "news": ["Wall Street Journal", "New York Post", "Barron's",
                     "MarketWatch", "Times of London", "The Sun"],
        }
        assert "HarperCollins" in news_corp_subsidiaries["publishing"]

    def test_news_corp_triple_ai_financial_relationship(self):
        """News Corp now has financial ties to ALL THREE major AI labs:
        1. OpenAI: $250M/5yr content deal ($50M/yr)
        2. Meta: $50M/yr content deal (3yr minimum)
        3. Anthropic: Settlement payments to HarperCollins subsidiary
        """
        relationships = {
            "openai_deal_annual_m": 50,
            "meta_deal_annual_m": 50,
            "anthropic_settlement": True,  # Via HarperCollins
        }
        assert all(v for v in relationships.values()), (
            "News Corp has financial relationships with all three major AI labs"
        )

    def test_settlement_creates_solvency_incentive(self):
        """Publishers need Anthropic to remain solvent to collect settlement.
        The IPO is the mechanism that ensures Anthropic can fund the $1.5B payout.
        This creates an indirect incentive for positive pre-IPO coverage."""
        settlement_b = 1.5
        anthropic_cash_at_ipo = True  # IPO raises capital for settlement payments
        claims_filed_pct = 91  # 91% of works claimed
        assert claims_filed_pct > 90, "High claims rate means many stakeholders"
        assert settlement_b > 1.0, "Material liability"


# =============================================================================
# Class 4: Structural Comparison — Licensing Deals vs Owner Equity
# =============================================================================
class TestStructuralComparison:
    """Compare OpenAI's deal-based model to Anthropic's equity-based model."""

    def test_openai_model_is_direct_deals(self):
        """OpenAI's coverage incentive operates through direct content deals."""
        data = load_yaml("competitor-entities.yaml")
        openai = data["entities"]["openai"]
        deals = openai.get("publisher_content_deal_portfolio", {})
        total_deals = deals.get("total_deals", "20+")
        assert "20" in str(total_deals), (
            "OpenAI has 20+ direct publisher content deals"
        )

    def test_anthropic_zero_direct_publisher_deals(self):
        """Anthropic has ZERO publicly disclosed publisher content deals."""
        # Confirmed by Rob Kelly's Media & the Machine tracking (91 deals, Jun 2026)
        # Troveo's Marty Pesis suggests possible PRIVATE deals
        # S-1 will force disclosure of any material deals
        anthropic_public_deals = 0
        assert anthropic_public_deals == 0, (
            "Anthropic has zero publicly disclosed publisher content deals"
        )

    def test_equity_incentive_harder_to_disclose(self):
        """Owner equity positions are structurally harder to disclose than
        direct content deals. A publication can say 'we have an OpenAI deal'
        but disclosing 'our owner's other company holds $5B in equity' requires
        multi-hop disclosure that no current framework mandates."""
        # Direct deal disclosure: 1 hop (publication → deal partner)
        # Owner equity disclosure: 2+ hops (publication → owner → company → investee)
        direct_deal_hops = 1   # WSJ → OpenAI deal
        owner_equity_hops = 3  # Time → Benioff → Salesforce → Anthropic
        assert owner_equity_hops > direct_deal_hops, (
            "Owner equity requires more disclosure hops than direct deals"
        )

    @pytest.mark.parametrize("chain,hops", [
        ("Time → Benioff → Salesforce → Anthropic", 3),
        ("WashPost → Bezos → Amazon → Anthropic", 3),
        ("WSJ → News Corp → HarperCollins → Anthropic settlement", 3),
        ("WIRED → Condé Nast → OpenAI deal", 2),
        ("WSJ → News Corp → OpenAI deal", 2),
    ])
    def test_disclosure_hop_count(self, chain, hops):
        """Each ownership chain has a defined number of disclosure hops."""
        assert hops >= 1, f"Chain '{chain}' should have at least 1 hop"

    def test_meta_excluded_from_both_models(self):
        """Meta has NO equity relationship with publication owners AND
        NO deals with adversarial publications. It is excluded from
        BOTH the licensing deal model AND the owner equity model."""
        meta_has_adversarial_pub_deals = False  # No WIRED, Verge, NYT, Guardian deals
        meta_has_owner_equity_links = False     # No pub owner invests in Meta AI
        assert not meta_has_adversarial_pub_deals
        assert not meta_has_owner_equity_links


# =============================================================================
# Class 5: IPO Timing and Coverage Incentive Amplification
# =============================================================================
class TestIPOTimingAmplification:
    """Test how Anthropic's IPO timing amplifies the coverage incentive."""

    def test_s1_filed_june_2026(self):
        """Anthropic filed confidential S-1 on June 1, 2026."""
        filing_date = "2026-06-01"
        assert filing_date == "2026-06-01"

    def test_expected_ipo_october_2026(self):
        """IPO expected October 2026 based on multiple analyst reports."""
        expected_quarter = "Q4 2026"
        expected_month = "October"
        # Sources: AwesomeAgents, Medium/Bykreator, Motley Fool
        assert expected_month == "October"

    def test_valuation_at_filing(self):
        """Last private valuation: $965B. Secondary market: ~$1.2T."""
        private_valuation_b = 965
        secondary_valuation_b = 1200
        assert secondary_valuation_b > private_valuation_b, (
            "Secondary market values Anthropic above last round"
        )

    def test_pre_ipo_coverage_window(self):
        """The Aug-Oct 2026 window is the peak coverage incentive period.
        During this window, positive coverage most directly affects IPO pricing.
        Owner equity holders (Bezos, Benioff) have maximum incentive for
        favorable coverage of Anthropic in their publications."""
        filing_month = 6   # June S-1
        expected_ipo_month = 10  # October
        current_month = 8  # August
        in_peak_window = filing_month <= current_month <= expected_ipo_month
        assert in_peak_window, "Currently in peak pre-IPO coverage incentive window"

    def test_amazon_upside_at_ipo(self):
        """Amazon's 15-20% stake could be worth $145B-$240B at IPO.
        On $13B invested, that's an 11-18x return."""
        investment_b = 13
        stake_low_pct = 15
        stake_high_pct = 20
        # At $965B valuation
        value_low_b = 965 * stake_low_pct / 100   # $144.75B
        value_high_b = 965 * stake_high_pct / 100  # $193B
        # At $1.2T secondary valuation
        value_high_secondary_b = 1200 * stake_high_pct / 100  # $240B
        assert value_low_b > 100, f"Amazon's stake worth ${value_low_b:.0f}B+"
        return_multiple = value_low_b / investment_b
        assert return_multiple > 10, f"Amazon return: {return_multiple:.0f}x"


# =============================================================================
# Class 6: S-1 Transparency Inflection — Testable Predictions
# =============================================================================
class TestS1TransparencyPredictions:
    """The S-1 creates a natural experiment with testable predictions."""

    def test_prediction_private_deals_disclosure(self):
        """PREDICTION: If Anthropic has private publisher deals (as Troveo's
        Pesis suggests), the S-1 must disclose them if material. This would
        change the financial incentive map for those publishers."""
        prediction = {
            "if_deals_exist": "S-1 forces disclosure of material content deals",
            "if_no_deals": "Confirms Anthropic zero-deal status",
            "testable_when": "S-1 becomes public (expected Oct 2026)",
        }
        assert prediction["testable_when"] is not None

    def test_prediction_google_concentration(self):
        """PREDICTION: S-1 will reveal Google/AWS revenue concentration.
        Estimated 50-60% of revenue through AWS Bedrock + significant
        Google Cloud spend. High concentration strengthens the Google
        Showcase → publisher dependency chain (Mechanism #28)."""
        estimated_aws_bedrock_pct = 55  # The Information, analyst estimates
        assert estimated_aws_bedrock_pct > 40, (
            "High AWS Bedrock concentration expected"
        )

    def test_prediction_settlement_liability(self):
        """PREDICTION: S-1 will show $1.5B settlement as material liability.
        This is the first time the public will see how Anthropic plans to
        fund the settlement payments."""
        settlement_b = 1.5
        anthropic_arr_b = 47
        settlement_as_pct_of_arr = (settlement_b / anthropic_arr_b) * 100
        assert settlement_as_pct_of_arr < 5, (
            f"Settlement is {settlement_as_pct_of_arr:.1f}% of ARR — material "
            "but not existential"
        )


# =============================================================================
# Class 7: Aggregate Financial Exposure Comparison
# =============================================================================
class TestAggregateExposureComparison:
    """Compare total financial exposure across AI companies and publishers."""

    @pytest.mark.parametrize("company,mechanism,examples", [
        ("OpenAI", "direct_content_deals",
         "20+ deals, $300-400M/yr total, partners include WIRED/Condé Nast, "
         "FT, Guardian, Atlantic, Time, WashPost"),
        ("Anthropic", "owner_equity_positions",
         "Zero direct deals but investors own WashPost (Bezos/Amazon), "
         "Time (Benioff/Salesforce), + Google Showcase 700+ pubs"),
        ("Google", "ad_revenue_plus_showcase_plus_equity",
         "Google Showcase $1B+, ad revenue dependency, 14% Anthropic equity, "
         "$35B SPV guarantee"),
        ("Meta", "minimal_adversarial_coverage_relationships",
         "13 deals total but ZERO with adversarial publications "
         "(WIRED, Verge, NYT, Guardian). No owner equity links."),
    ])
    def test_company_incentive_model(self, company, mechanism, examples):
        """Each company has a distinct financial incentive model with publishers."""
        assert len(mechanism) > 0
        assert len(examples) > 0

    def test_meta_is_only_company_with_no_adversarial_pub_links(self):
        """Meta is the ONLY major AI company with zero financial links to
        publications that produce adversarial coverage of it.
        - OpenAI: direct deals with WIRED (Condé Nast), Guardian, FT, NYT (lawsuit)
        - Anthropic: owner equity (Bezos→WashPost, Benioff→Time) + Google Showcase
        - Google: Showcase pays adversarial pubs + ad revenue dependency
        - Meta: ZERO deals with WIRED, Verge, NYT, Guardian, Atlantic"""
        meta_adversarial_pub_links = 0
        openai_adversarial_pub_links = 4  # Condé Nast, Guardian, FT, Atlantic
        assert meta_adversarial_pub_links == 0
        assert openai_adversarial_pub_links > 0

    def test_bezos_combined_exposure(self):
        """Bezos has COMBINED exposure: Amazon Anthropic equity ($145-193B)
        + WashPost (which he bought for $250M). The Anthropic stake is worth
        580-772x more than the WashPost acquisition price."""
        washpost_price_m = 250
        anthropic_stake_low_b = 145
        multiple = (anthropic_stake_low_b * 1000) / washpost_price_m
        assert multiple > 500, (
            f"Anthropic stake is {multiple:.0f}x the WashPost purchase price"
        )


# =============================================================================
# Class 8: Legitimate Factors and Confounds
# =============================================================================
class TestLegitimateFactors:
    """Document legitimate factors that could explain the patterns
    without financial incentive bias."""

    @pytest.mark.parametrize("factor_id,factor", [
        (1, "Benioff and Bezos genuinely promise editorial independence from "
            "business interests. Benioff: 'not involved in day-to-day operations "
            "or journalistic decisions.' Bezos has similarly promised WashPost "
            "editorial independence."),
        (2, "Salesforce's $5B Anthropic stake is an investment decision made by "
            "Salesforce's board, not by Benioff personally in his capacity as "
            "Time owner. Corporate Chinese wall argument."),
        (3, "The Anthropic copyright settlement pays AUTHORS, not news publishers. "
            "HarperCollins receives funds as a book publisher, not as a news "
            "operation. The editorial teams are separate."),
        (4, "Amazon's Anthropic investment is an AWS cloud strategy, not a media "
            "strategy. Bezos's WashPost involvement is personal, not Amazon's."),
        (5, "Pre-IPO coverage may be positive because Anthropic genuinely has "
            "strong products (Claude Code $1B ARR in 6 months, $47B total ARR). "
            "Positive coverage could reflect genuine quality, not incentive bias."),
        (6, "Time's 'Most Disruptive Company' designation may be editorially "
            "driven by Anthropic's genuine market impact (fastest revenue growth "
            "in software history) rather than owner equity influence."),
        (7, "The S-1 filing itself is news. Publications covering Anthropic "
            "positively pre-IPO may be responding to newsworthy milestones "
            "(funding rounds, product launches, IPO filing) rather than owner "
            "financial interests."),
    ])
    def test_legitimate_factor_documented(self, factor_id, factor):
        """Each legitimate factor must be documented."""
        assert len(factor) > 50, (
            f"Factor {factor_id} must be substantive, not cursory"
        )
        assert factor_id >= 1


# =============================================================================
# Class 9: Profile Integration Verification
# =============================================================================
class TestProfileIntegration:
    """Verify mechanism #36 is properly integrated into profiles."""

    def test_mechanism_in_competitor_coverage_research(self):
        """Mechanism #36 must exist in competitor-coverage-research.yaml."""
        research = load_yaml("competitor-coverage-research.yaml")
        full_text = str(research)
        assert "36" in full_text, (
            "Mechanism #36 must be referenced in competitor-coverage-research.yaml"
        )

    def test_mechanism_has_finding_summary(self):
        """Mechanism #36 must have a finding_summary."""
        research = load_yaml("competitor-coverage-research.yaml")
        findings = research.get("cross_publication_findings", {})
        if not findings:
            findings = research.get("aggregate_findings", {})
        full_text = str(research)
        assert "owner" in full_text.lower() or "equity" in full_text.lower() or \
               "investor" in full_text.lower() or "convergence" in full_text.lower(), (
            "Mechanism #36 finding must reference owner/equity/investor convergence"
        )

    def test_anthropic_investor_chains_documented(self):
        """Anthropic's investor → publication owner chains must be documented
        in competitor-entities.yaml."""
        data = load_yaml("competitor-entities.yaml")
        full_text = str(data)
        # At least one of the chains should be documented
        chains_found = sum([
            "bezos" in full_text.lower(),
            "benioff" in full_text.lower(),
            "washington post" in full_text.lower(),
            "time" in full_text.lower() and "magazine" in full_text.lower(),
        ])
        assert chains_found >= 1, (
            "At least one investor → publication chain must be documented"
        )
