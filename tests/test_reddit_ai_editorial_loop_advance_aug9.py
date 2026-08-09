"""
Reddit AI Data Licensing → Advance/WIRED Circular Editorial Incentive Loop
Type C: Financial Incentive Mapping
Created: 2026-08-09 12:00 PT

Key finding: WIRED's editorial coverage of AI content licensing creates
market conditions that increase the value of Advance Publications' ~$6.82B
Reddit equity stake. Reddit's AI data licensing deals ($60M/yr Google,
~$70M/yr OpenAI, projected $550M/yr at renewal) are the fastest-growing
revenue driver for Advance's single largest equity holding.

The circular incentive: WIRED amplifies "AI companies must pay for content"
→ this narrative strengthens Reddit's negotiating position on AI data deals
→ higher Reddit AI revenue → higher RDDT stock → higher Advance equity value
→ Advance profits while WIRED never discloses the connection.

Additionally: SRMG (PIF → SRMG → PMC → The Verge) reported Q2 2026 showing
financial recovery (revenue +15.8% YoY, net profit +77.7%), stabilizing the
sovereign ownership chain.

Sources:
- Reddit Q2 2026 earnings: https://www.techtimes.com/articles/322357/20260730/reddit-revenue-soars-past-estimates-flags-google-search-traffic-choppy.htm
- Reddit-Google deal non-renewal risk: https://stocktwits.com/news-articles/markets/equity/this-analyst-believes-reddit-not-renewing-google-ai-content-deal-would-be-a-step-backward/cZZm8iGR7Dl
- Wells Fargo $550M/yr projection: https://www.barrons.com/articles/buy-reddit-stock-price-pick-eef67fe8
- Reddit-Perplexity lawsuit survives MTD: https://www.reuters.com/legal/litigation/perplexity-ai-loses-bid-toss-reddit-lawsuit-over-data-scraping-2026-07-31/
- Reddit stock recovery: https://robinhood.com/us/en/stocks/rddt/
- SRMG Q2 2026 Saudi Exchange filing
"""

import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
WIRED_PROFILE = os.path.join(PROFILES_DIR, 'wired.yaml')
ENTITIES_PROFILE = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
VERGE_PROFILE = os.path.join(PROFILES_DIR, 'the-verge.yaml')
RESEARCH_PROFILE = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')


def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestRedditStockRecovery:
    """Verify Reddit stock recovery data (Aug 1-7, 2026) is captured."""

    def test_wired_profile_has_stock_recovery_section(self):
        """WIRED profile contains Reddit stock recovery data."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        assert reddit_entry is not None
        recovery = reddit_entry.get('stock_recovery_aug_2026', '')
        assert '161.70' in recovery or '161' in recovery

    def test_recovery_from_crash_low(self):
        """Recovery from Jul 31 crash low of ~$140 is documented."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        assert reddit_entry is not None
        recovery = reddit_entry.get('stock_recovery_aug_2026', '')
        assert '140' in recovery

    def test_advance_stake_value_updated(self):
        """Advance stake value is recalculated at recovery price."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        assert reddit_entry is not None
        recovery = reddit_entry.get('stock_recovery_aug_2026', '')
        assert '6.82B' in recovery or '6.8' in recovery

    def test_margin_loan_status_updated(self):
        """Margin loan status reflects recovery above offering floor."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        assert reddit_entry is not None
        recovery = reddit_entry.get('stock_recovery_aug_2026', '')
        assert 'margin' in recovery.lower() or 'offering' in recovery.lower()

    def test_entities_has_stock_recovery(self):
        """Competitor entities file also tracks Reddit stock recovery."""
        entities = load_yaml(ENTITIES_PROFILE)
        google = entities.get('entities', {}).get('google', {})
        reddit_recovery = google.get('reddit_stock_recovery_aug_2026', None)
        assert reddit_recovery is not None
        assert '161' in reddit_recovery.get('detail', '')

    def test_ytd_performance_captured(self):
        """YTD performance decline is documented."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        assert reddit_entry is not None
        recovery = reddit_entry.get('stock_recovery_aug_2026', '')
        assert '-33' in recovery or 'YTD' in recovery


class TestRedditAIEditorialLoop:
    """Verify the circular editorial incentive loop is documented."""

    def test_loop_section_exists(self):
        """The editorial loop section exists in WIRED profile."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        assert reddit_entry is not None
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', None)
        assert loop is not None

    def test_loop_finding_describes_circular_incentive(self):
        """The finding describes the circular nature of the incentive."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        finding = loop.get('finding', '')
        assert 'circular' in finding.lower() or 'CIRCULAR' in finding

    def test_loop_mechanism_has_numbered_steps(self):
        """The mechanism section outlines a multi-step chain."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        mechanism = loop.get('mechanism', '')
        # Should have at least 5 numbered steps
        assert '5.' in mechanism or '5)' in mechanism

    def test_loop_mechanism_references_google_deal(self):
        """Mechanism references Reddit-Google $60M/yr deal."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        mechanism = loop.get('mechanism', '')
        assert '60M' in mechanism or '$60' in mechanism

    def test_loop_mechanism_references_openai_deal(self):
        """Mechanism references Reddit-OpenAI ~$70M/yr deal."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        mechanism = loop.get('mechanism', '')
        assert '70M' in mechanism or 'OpenAI' in mechanism

    def test_loop_references_wells_fargo_projection(self):
        """Loop references Wells Fargo $550M/yr renewal projection."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        mechanism = loop.get('mechanism', '')
        assert '550M' in mechanism or '550' in mechanism

    def test_loop_references_advance_stake_percentage(self):
        """Loop references Advance's 23.3% economic stake."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        mechanism = loop.get('mechanism', '')
        assert '23.3%' in mechanism or '23.3' in mechanism


class TestMetaAsymmetryInLoop:
    """Verify the Meta asymmetry dimension of the editorial loop."""

    def test_meta_asymmetry_section_exists(self):
        """Meta asymmetry within the loop is documented."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        assert 'meta_asymmetry' in loop

    def test_meta_has_no_reddit_deal(self):
        """Meta's absence from Reddit data licensing is documented."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        asymmetry = loop.get('meta_asymmetry', '')
        assert 'no' in asymmetry.lower() and 'Reddit' in asymmetry

    def test_meta_has_no_conde_nast_deal(self):
        """Meta's absence from Condé Nast licensing is also noted."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        asymmetry = loop.get('meta_asymmetry', '')
        assert 'Condé Nast' in asymmetry or 'Conde Nast' in asymmetry


class TestQuantifiedConflict:
    """Verify the quantified conflict analysis."""

    def test_quantified_section_exists(self):
        """Quantified conflict section exists."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        assert 'quantified_conflict' in loop

    def test_licensing_growth_value_to_advance(self):
        """AI licensing growth valued at ~$1.1B for Advance's stake."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        quantified = loop.get('quantified_conflict', '')
        assert '1.1B' in quantified or 'billion' in quantified.lower()

    def test_reddit_vs_conde_nast_deal_size_comparison(self):
        """Reddit AI licensing pathway compared to Condé Nast's OpenAI deal."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        quantified = loop.get('quantified_conflict', '')
        assert '20-50x' in quantified or 'dwarfs' in quantified

    def test_jul_22_stock_drop_quantified(self):
        """Jul 22 stock drop (Google deal non-renewal report) quantified."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        quantified = loop.get('quantified_conflict', '')
        assert '600M' in quantified or 'Jul 22' in quantified


class TestPerplexityDimension:
    """Verify the Perplexity dual-litigation dimension."""

    def test_perplexity_section_exists(self):
        """Perplexity dimension of the loop is documented."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        assert 'perplexity_dimension' in loop

    def test_both_plaintiffs_identified(self):
        """Both Reddit and Condé Nast identified as Advance-controlled plaintiffs."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        perplexity = loop.get('perplexity_dimension', '')
        assert 'Reddit' in perplexity and 'Condé Nast' in perplexity or 'Conde Nast' in perplexity

    def test_advance_controls_both(self):
        """Advance's control of both plaintiffs is explicit."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        perplexity = loop.get('perplexity_dimension', '')
        assert 'Advance' in perplexity

    def test_150m_damages_mentioned(self):
        """Reddit's $150M damages claim is referenced."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        perplexity = loop.get('perplexity_dimension', '')
        assert '150M' in perplexity or '$150' in perplexity


class TestSRMGQ2Recovery:
    """Verify SRMG Q2 2026 financial recovery data."""

    def test_srmg_section_exists_in_loop(self):
        """SRMG Q2 update exists in the editorial loop section."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        assert 'srmg_q2_2026_update' in loop

    def test_srmg_revenue_growth(self):
        """SRMG Q2 revenue growth (+15.8% YoY) is documented."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        srmg = loop.get('srmg_q2_2026_update', '')
        assert '15.8%' in srmg or '653' in srmg

    def test_srmg_profit_turnaround(self):
        """SRMG sequential profit turnaround is documented (Q4 loss → Q1 → Q2 profit)."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        srmg = loop.get('srmg_q2_2026_update', '')
        assert '71.2' in srmg or '77.7%' in srmg

    def test_srmg_ownership_chain_implication(self):
        """SRMG recovery's implication for PMC ownership chain is noted."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        srmg = loop.get('srmg_q2_2026_update', '')
        assert 'PMC' in srmg or 'Verge' in srmg

    def test_entities_has_srmg_q2(self):
        """Competitor entities also tracks SRMG Q2 2026."""
        entities = load_yaml(ENTITIES_PROFILE)
        google = entities.get('entities', {}).get('google', {})
        srmg_q2 = google.get('srmg_q2_2026_results', None)
        assert srmg_q2 is not None
        detail = srmg_q2.get('detail', '')
        assert '653' in detail or '15.8%' in detail


class TestSourceCitations:
    """Verify all source citations exist."""

    def test_loop_has_source_urls(self):
        """The editorial loop section has source URLs."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        sources = loop.get('source_urls', [])
        assert len(sources) >= 3

    def test_sources_include_techtimes(self):
        """Sources include TechTimes Reddit Q2 coverage."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        sources = loop.get('source_urls', [])
        assert any('techtimes' in s for s in sources)

    def test_sources_include_reuters_perplexity(self):
        """Sources include Reuters Perplexity ruling."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        sources = loop.get('source_urls', [])
        assert any('reuters' in s for s in sources)


class TestCrossFileConsistency:
    """Verify consistency between WIRED profile and competitor-entities.yaml."""

    def test_advance_stake_percentage_consistent(self):
        """Advance's 23.3% stake is consistent across files."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        mechanism = loop.get('mechanism', '')
        # Entities file references same percentage
        entities = load_yaml(ENTITIES_PROFILE)
        google = entities.get('entities', {}).get('google', {})
        renewal = google.get('reddit_deal_renewal_projections', {})
        renewal_detail = renewal.get('detail', '')
        assert '23.3%' in mechanism
        assert '23.3%' in renewal_detail

    def test_wells_fargo_projection_consistent(self):
        """Wells Fargo $550M/yr projection is consistent across files."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        mechanism = loop.get('mechanism', '')
        entities = load_yaml(ENTITIES_PROFILE)
        google = entities.get('entities', {}).get('google', {})
        renewal = google.get('reddit_deal_renewal_projections', {})
        renewal_detail = renewal.get('detail', '')
        assert '550M' in mechanism
        assert '550M' in renewal_detail

    def test_google_deal_amount_consistent(self):
        """Reddit-Google $60M/yr deal amount consistent across files."""
        profile = load_yaml(WIRED_PROFILE)
        investments = profile.get('advance_investments', [])
        reddit_entry = next((e for e in investments if 'Reddit' in str(e.get('entity', ''))), None)
        loop = reddit_entry.get('reddit_ai_data_licensing_editorial_loop', {})
        mechanism = loop.get('mechanism', '')
        entities = load_yaml(ENTITIES_PROFILE)
        google = entities.get('entities', {}).get('google', {})
        instability = google.get('reddit_deal_instability', {})
        instability_detail = instability.get('detail', '')
        assert '60M' in mechanism
        assert '60M' in instability_detail
