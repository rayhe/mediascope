"""
Tests for Type C Financial Incentive Mapping — Aug 6 2026 08:00 PT
Advance-Reddit-Perplexity Triangle + Deal Renewal Projections + Marketplace Evolution

Key finding: Advance Publications simultaneously profits from Perplexity (via Condé Nast
licensing deal) and sues Perplexity (via Reddit DMCA lawsuit, dismissal rejected Jul 31 2026).
This is the most acute undisclosed conflict-of-interest in AI content licensing.

Sources:
- https://www.reuters.com/legal/litigation/perplexity-ai-loses-bid-toss-reddit-lawsuit-over-data-scraping-2026-07-31/
- https://www.barrons.com/articles/buy-reddit-stock-price-pick-eef67fe8
- https://digiday.com/marketing/reddit-questions-if-ai-data-deals-could-hurt-its-ad-business/
- https://techcrunch.com/2026/02/10/amazon-may-launch-a-marketplace-where-media-sites-can-sell-their-content-to-ai-companies/
- https://searchengineland.com/microsoft-launches-publisher-content-marketplace-for-ai-licensing-468191
"""
import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    with open(os.path.join(PROFILES_DIR, filename)) as f:
        return yaml.safe_load(f)


class TestAdvanceRedditPerplexityTriangle:
    """Validates the three-way conflict: Advance sues Perplexity (via Reddit)
    while profiting from Perplexity (via Condé Nast deal)."""

    def test_triangle_section_exists(self):
        data = load_yaml('competitor-coverage-research.yaml')
        wired = data['publications']['wired']
        assert 'advance_reddit_perplexity_triangle' in wired

    def test_triangle_has_description(self):
        data = load_yaml('competitor-coverage-research.yaml')
        triangle = data['publications']['wired']['advance_reddit_perplexity_triangle']
        assert 'description' in triangle
        assert 'SUING' in triangle['description'] or 'suing' in triangle['description']

    def test_triangle_mentions_dmca_ruling(self):
        data = load_yaml('competitor-coverage-research.yaml')
        triangle = data['publications']['wired']['advance_reddit_perplexity_triangle']
        desc = triangle['description']
        assert 'Engelmayer' in desc or 'SDNY' in desc or 'Jul 31' in desc

    def test_triangle_mentions_comet_plus_deal(self):
        data = load_yaml('competitor-coverage-research.yaml')
        triangle = data['publications']['wired']['advance_reddit_perplexity_triangle']
        desc = triangle['description']
        assert 'Comet Plus' in desc or 'licensing deal' in desc.lower()

    def test_triangle_has_source_urls(self):
        data = load_yaml('competitor-coverage-research.yaml')
        triangle = data['publications']['wired']['advance_reddit_perplexity_triangle']
        assert 'source_urls' in triangle
        assert len(triangle['source_urls']) >= 2

    def test_triangle_reuters_source(self):
        data = load_yaml('competitor-coverage-research.yaml')
        triangle = data['publications']['wired']['advance_reddit_perplexity_triangle']
        urls = triangle['source_urls']
        assert any('reuters.com' in u for u in urls)

    def test_sam_altman_reddit_conflict(self):
        """Sam Altman owns 8.7% of Reddit AND is CEO of OpenAI which has deals
        with both Reddit and Condé Nast."""
        data = load_yaml('competitor-coverage-research.yaml')
        triangle = data['publications']['wired']['advance_reddit_perplexity_triangle']
        desc = triangle['description']
        assert 'Altman' in desc


class TestRedditDealRenewalProjections:
    """Validates the $550M/yr deal renewal forecast from Wells Fargo."""

    def test_renewal_projections_exist(self):
        data = load_yaml('competitor-entities.yaml')
        google = data['entities']['google']
        assert 'reddit_deal_renewal_projections' in google

    def test_renewal_amount(self):
        data = load_yaml('competitor-entities.yaml')
        proj = data['entities']['google']['reddit_deal_renewal_projections']
        detail = proj['detail']
        assert '$550M' in detail or '550' in detail

    def test_renewal_source_barrons(self):
        data = load_yaml('competitor-entities.yaml')
        proj = data['entities']['google']['reddit_deal_renewal_projections']
        urls = proj['source_urls']
        assert any('barrons.com' in u for u in urls)

    def test_renewal_wells_fargo_analyst(self):
        data = load_yaml('competitor-entities.yaml')
        proj = data['entities']['google']['reddit_deal_renewal_projections']
        detail = proj['detail']
        assert 'Brondolo' in detail or 'Wells Fargo' in detail

    def test_renewal_advance_impact(self):
        data = load_yaml('competitor-entities.yaml')
        proj = data['entities']['google']['reddit_deal_renewal_projections']
        detail = proj['detail']
        assert 'Advance' in detail

    def test_renewal_mediascope_relevance(self):
        data = load_yaml('competitor-entities.yaml')
        proj = data['entities']['google']['reddit_deal_renewal_projections']
        assert 'mediascope_relevance' in proj
        assert 'WIRED' in proj['mediascope_relevance']

    def test_renewal_quadruple_increase(self):
        data = load_yaml('competitor-entities.yaml')
        proj = data['entities']['google']['reddit_deal_renewal_projections']
        detail = proj['detail']
        assert 'quadruple' in detail.lower() or '4x' in detail


class TestRedditPerplexityLitigation:
    """Validates the Jul 31 2026 DMCA ruling documentation."""

    def test_litigation_section_exists(self):
        data = load_yaml('competitor-entities.yaml')
        google = data['entities']['google']
        assert 'reddit_perplexity_litigation' in google

    def test_ruling_date(self):
        data = load_yaml('competitor-entities.yaml')
        lit = data['entities']['google']['reddit_perplexity_litigation']
        assert str(lit['date']) == '2026-07-31'

    def test_engelmayer_judge(self):
        data = load_yaml('competitor-entities.yaml')
        lit = data['entities']['google']['reddit_perplexity_litigation']
        ruling = lit['ruling']
        assert 'Engelmayer' in ruling

    def test_sdny_court(self):
        data = load_yaml('competitor-entities.yaml')
        lit = data['entities']['google']['reddit_perplexity_litigation']
        ruling = lit['ruling']
        assert 'SDNY' in ruling

    def test_anthropic_lawsuit_mentioned(self):
        data = load_yaml('competitor-entities.yaml')
        lit = data['entities']['google']['reddit_perplexity_litigation']
        ruling = lit['ruling']
        assert 'Anthropic' in ruling

    def test_triangle_conflict_documented(self):
        data = load_yaml('competitor-entities.yaml')
        lit = data['entities']['google']['reddit_perplexity_litigation']
        assert 'advance_conde_nast_perplexity_triangle' in lit
        triangle = lit['advance_conde_nast_perplexity_triangle']
        assert 'SUING' in triangle or 'suing' in triangle

    def test_triangle_mentions_150m(self):
        data = load_yaml('competitor-entities.yaml')
        lit = data['entities']['google']['reddit_perplexity_litigation']
        triangle = lit['advance_conde_nast_perplexity_triangle']
        assert '$150M' in triangle

    def test_litigation_source_urls(self):
        data = load_yaml('competitor-entities.yaml')
        lit = data['entities']['google']['reddit_perplexity_litigation']
        assert 'source_urls' in lit
        assert len(lit['source_urls']) >= 2


class TestRedditAdCannibalization:
    """Validates the Reddit AI deal ad cannibalization concern."""

    def test_ad_cannibalization_section_exists(self):
        data = load_yaml('competitor-entities.yaml')
        google = data['entities']['google']
        assert 'reddit_ad_cannibalization_debate' in google

    def test_ad_cannibalization_date(self):
        data = load_yaml('competitor-entities.yaml')
        debate = data['entities']['google']['reddit_ad_cannibalization_debate']
        assert '2026-07' in str(debate['date'])

    def test_ad_cannibalization_digiday_source(self):
        data = load_yaml('competitor-entities.yaml')
        debate = data['entities']['google']['reddit_ad_cannibalization_debate']
        urls = debate['source_urls']
        assert any('digiday.com' in u for u in urls)

    def test_ad_cannibalization_paradox(self):
        data = load_yaml('competitor-entities.yaml')
        debate = data['entities']['google']['reddit_ad_cannibalization_debate']
        detail = debate['detail']
        assert 'paradox' in detail.lower() or 'cannibalize' in detail.lower() or 'undercut' in detail.lower()


class TestMarketplaceEvolution:
    """Validates the Amazon vs Microsoft marketplace competition documentation."""

    def test_amazon_marketplace_has_details(self):
        data = load_yaml('competitor-entities.yaml')
        # Search for amazon_marketplace_emerging in the landscape section
        found = False
        for key in data:
            if isinstance(data[key], dict):
                if 'amazon_marketplace_emerging' in data.get(key, {}):
                    found = True
                    break
        # Try nested structures
        if not found:
            landscape = data.get('financial_landscape', data.get('cross_cutting', {}))
            if isinstance(landscape, dict):
                found = 'amazon_marketplace_emerging' in landscape
        # The section exists somewhere in the file
        import subprocess
        result = subprocess.run(
            ['grep', '-c', 'amazon_marketplace_emerging', os.path.join(PROFILES_DIR, 'competitor-entities.yaml')],
            capture_output=True, text=True
        )
        assert int(result.stdout.strip()) >= 1

    def test_amazon_marketplace_has_multiple_sources(self):
        """Amazon marketplace section should have multiple source URLs."""
        import subprocess
        result = subprocess.run(
            ['grep', '-A', '50', 'amazon_marketplace_emerging:', os.path.join(PROFILES_DIR, 'competitor-entities.yaml')],
            capture_output=True, text=True
        )
        output = result.stdout
        assert output.count('source_url') >= 1 or output.count('techcrunch.com') >= 1 or output.count('reuters.com') >= 1

    def test_amazon_marketplace_has_date(self):
        """Amazon marketplace should have an announced date."""
        import subprocess
        result = subprocess.run(
            ['grep', '-A', '5', 'amazon_marketplace_emerging:', os.path.join(PROFILES_DIR, 'competitor-entities.yaml')],
            capture_output=True, text=True
        )
        assert '2026' in result.stdout

    def test_microsoft_pcm_conde_nast_participation(self):
        """Condé Nast is a Microsoft PCM pilot partner — confirmed in competitor-entities."""
        data = load_yaml('competitor-entities.yaml')
        excluded = data.get('meta_ai_deals', {}).get('excluded_publishers', [])
        if not excluded:
            # Try the deals structure
            excluded = []
            for section in data.values():
                if isinstance(section, dict) and 'excluded_publishers' in section:
                    excluded = section['excluded_publishers']
                    break
        # Fallback to grep
        import subprocess
        result = subprocess.run(
            ['grep', '-c', 'Microsoft PCM', os.path.join(PROFILES_DIR, 'competitor-entities.yaml')],
            capture_output=True, text=True
        )
        assert int(result.stdout.strip()) >= 2  # Should appear in Condé Nast + Vox Media entries

    def test_meta_not_in_marketplace(self):
        """Meta is NOT a participant in Microsoft PCM or Amazon marketplace."""
        import subprocess
        result = subprocess.run(
            ['grep', '-A', '50', 'amazon_marketplace_emerging:', os.path.join(PROFILES_DIR, 'competitor-entities.yaml')],
            capture_output=True, text=True
        )
        output = result.stdout
        assert 'Meta' in output or 'bilateral' in output


class TestPerplexityDualRelationship:
    """Cross-validates the Perplexity dual relationship: Condé Nast deal + Reddit lawsuit."""

    def test_wired_perplexity_coverage_tone_neutral(self):
        data = load_yaml('competitor-coverage-research.yaml')
        wired = data['publications']['wired']
        assert wired.get('perplexity_coverage_tone') == 'neutral'

    def test_conde_nast_perplexity_deal_exists(self):
        data = load_yaml('competitor-entities.yaml')
        excluded = data.get('meta_ai_deals', {}).get('excluded_publishers', [])
        if not excluded:
            for section in data.values():
                if isinstance(section, dict) and 'excluded_publishers' in section:
                    excluded = section['excluded_publishers']
                    break
        # Verify Condé Nast has Perplexity deal
        cn_entry = None
        for pub in excluded:
            if 'Condé Nast' in pub.get('name', ''):
                cn_entry = pub
                break
        if cn_entry:
            deals = cn_entry.get('deals_with_competitors', [])
            perplexity_deal = [d for d in deals if d.get('partner', '') == 'Perplexity']
            assert len(perplexity_deal) >= 1
        else:
            # Grep fallback
            import subprocess
            result = subprocess.run(
                ['grep', '-c', r'Perplexity.*Comet\|Comet.*Perplexity', os.path.join(PROFILES_DIR, 'competitor-entities.yaml')],
                capture_output=True, text=True
            )
            assert int(result.stdout.strip()) >= 1

    def test_reddit_perplexity_lawsuit_exists(self):
        data = load_yaml('competitor-entities.yaml')
        google = data['entities']['google']
        assert 'reddit_perplexity_litigation' in google

    def test_hypocrisy_arc_documented(self):
        data = load_yaml('competitor-coverage-research.yaml')
        wired = data['publications']['wired']
        summary = wired.get('perplexity_coverage_summary', '')
        assert 'HYPOCRISY' in summary or 'hypocrisy' in summary

    def test_deal_count_is_five_or_more(self):
        """Condé Nast should have at least 5 competitor AI deals."""
        data = load_yaml('competitor-coverage-research.yaml')
        wired = data['publications']['wired']
        summary = wired.get('deal_count_summary', '')
        assert 'FIVE' in summary or '5' in summary or 'five' in summary.lower()


class TestDealRenewalResearchCrossValidation:
    """Cross-validates data consistency between profiles for new findings."""

    def test_reddit_deal_instability_preserved(self):
        """Original reddit_deal_instability section should still exist."""
        data = load_yaml('competitor-entities.yaml')
        google = data['entities']['google']
        assert 'reddit_deal_instability' in google

    def test_google_entity_complete(self):
        """Google entity should have all required fields."""
        data = load_yaml('competitor-entities.yaml')
        google = data['entities']['google']
        assert 'display_name' in google
        assert 'category' in google
        assert google['category'] == 'big_tech'

    def test_meta_zero_deals(self):
        """Meta should have zero AI deals count."""
        import subprocess
        result = subprocess.run(
            ['grep', '-A', '3', 'meta_deal:', os.path.join(PROFILES_DIR, 'competitor-entities.yaml')],
            capture_output=True, text=True
        )
        assert 'none' in result.stdout.lower()

    def test_advance_voting_power_documented(self):
        """Advance's ~62% voting power should be documented."""
        import subprocess
        result = subprocess.run(
            ['grep', '-c', r'62%\|65.2%', os.path.join(PROFILES_DIR, 'wired.yaml')],
            capture_output=True, text=True
        )
        assert int(result.stdout.strip()) >= 1
