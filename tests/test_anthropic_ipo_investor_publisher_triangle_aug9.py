"""
Test: Anthropic IPO Investor-Advertiser-Publisher Triangle

Type C: Financial Incentive Mapping — Aug 9, 2026 06:00 PT

Key finding: Anthropic has ZERO direct publisher content licensing deals, but
is NOT financially neutral to publishers. Amazon ($13B+ invested, $76B/yr TTM
ad revenue) and Google ($3B+ invested, $81.6B/yr ad revenue) are both
Anthropic's largest investors AND publishers' two largest advertising/cloud
revenue partners. This creates an INDIRECT coverage incentive triangle where
publishers covering Anthropic favorably boost the asset value of their own
biggest financial partners — a structural incentive invisible to traditional
conflict-of-interest disclosure.

Sources:
- Amazon Q2 2026 earnings: $53.4B Anthropic paper gain, $76B TTM ad revenue
- Alphabet 14% Anthropic stake, up to $40B committed, $200B cloud commitment
- News Corp Q4 FY2026 (Aug 5): Triple AI revenue (OpenAI + Meta + Anthropic settlement)
- Motley Fool investor analysis of Amazon/Alphabet Anthropic stakes
- Adweek: Amazon TTM ad revenue $76B (Aug 2026)
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_publication_profile(slug):
    path = os.path.join(PROFILES_DIR, f'{slug}.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


# ============================================================
# Class 1: Triangle Structure Exists and Is Complete
# ============================================================
class TestTriangleStructure:
    """Verify the investor_advertiser_publisher_triangle section exists
    with all required sub-sections in the Anthropic entity."""

    def test_triangle_section_exists(self):
        data = load_competitor_entities()
        ant = data['entities']['anthropic']
        assert 'investor_advertiser_publisher_triangle' in ant

    def test_triangle_has_overview(self):
        data = load_competitor_entities()
        tri = data['entities']['anthropic']['investor_advertiser_publisher_triangle']
        assert 'overview' in tri
        assert len(tri['overview']) > 200

    def test_triangle_has_amazon_leg(self):
        data = load_competitor_entities()
        tri = data['entities']['anthropic']['investor_advertiser_publisher_triangle']
        assert 'amazon_leg' in tri

    def test_triangle_has_google_leg(self):
        data = load_competitor_entities()
        tri = data['entities']['anthropic']['investor_advertiser_publisher_triangle']
        assert 'google_leg' in tri

    def test_triangle_has_dynamics(self):
        data = load_competitor_entities()
        tri = data['entities']['anthropic']['investor_advertiser_publisher_triangle']
        assert 'triangle_dynamics' in tri
        assert len(tri['triangle_dynamics']) >= 4

    def test_triangle_has_source_urls(self):
        data = load_competitor_entities()
        tri = data['entities']['anthropic']['investor_advertiser_publisher_triangle']
        assert 'source_urls' in tri
        assert len(tri['source_urls']) >= 4


# ============================================================
# Class 2: Amazon Leg Financial Data
# ============================================================
class TestAmazonLeg:
    """Verify Amazon's dual role as Anthropic investor AND publisher advertiser."""

    def test_amazon_invested_total(self):
        data = load_competitor_entities()
        leg = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['amazon_leg']
        assert leg['invested_total_b'] >= 13

    def test_amazon_additional_committed(self):
        data = load_competitor_entities()
        leg = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['amazon_leg']
        assert leg['additional_committed_b'] >= 20

    def test_amazon_stake_value(self):
        data = load_competitor_entities()
        leg = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['amazon_leg']
        assert leg['stake_value_estimated_b'] >= 100  # conservatively >$100B

    def test_amazon_q2_paper_gain(self):
        data = load_competitor_entities()
        leg = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['amazon_leg']
        assert leg['q2_2026_paper_gain_b'] == 53.4

    def test_amazon_publisher_ad_revenue(self):
        data = load_competitor_entities()
        leg = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['amazon_leg']
        assert leg['publisher_ad_revenue_ttm_b'] >= 70  # $76B TTM

    def test_amazon_paper_gain_exceeds_operating_income(self):
        """Amazon's Anthropic paper gain ($53.4B) exceeded its entire Q2 operating income."""
        data = load_competitor_entities()
        leg = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['amazon_leg']
        assert 'materiality' in leg
        assert '53.4' in leg['materiality']
        assert '27.5' in leg['materiality']

    def test_amazon_publisher_mechanism_mentions_key_partners(self):
        data = load_competitor_entities()
        leg = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['amazon_leg']
        mechanism = leg['publisher_mechanism']
        # Should mention specific publisher partners
        for partner in ['BuzzFeed', 'Hearst', 'Ziff Davis']:
            assert partner in mechanism

    def test_amazon_cloud_mechanism_mentions_publishers(self):
        data = load_competitor_entities()
        leg = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['amazon_leg']
        assert 'cloud_mechanism' in leg
        assert 'AWS' in leg['cloud_mechanism']


# ============================================================
# Class 3: Google Leg Financial Data
# ============================================================
class TestGoogleLeg:
    """Verify Google's dual role as Anthropic investor AND publisher advertiser."""

    def test_google_invested_total(self):
        data = load_competitor_entities()
        leg = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['google_leg']
        assert leg['invested_total_b'] >= 3

    def test_google_additional_committed(self):
        data = load_competitor_entities()
        leg = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['google_leg']
        assert leg['additional_committed_b'] >= 30

    def test_google_max_stake(self):
        data = load_competitor_entities()
        leg = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['google_leg']
        assert leg['max_stake_pct'] == 15

    def test_google_cloud_commitment_from_anthropic(self):
        data = load_competitor_entities()
        leg = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['google_leg']
        assert leg['cloud_commitment_from_anthropic_b'] >= 200

    def test_google_publisher_ad_revenue(self):
        data = load_competitor_entities()
        leg = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['google_leg']
        assert leg['publisher_ad_revenue_annual_b'] >= 80

    def test_google_publisher_mechanism_mentions_ad_stack(self):
        data = load_competitor_entities()
        leg = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['google_leg']
        mechanism = leg['publisher_mechanism']
        for component in ['Ad Manager', 'AdSense', 'Showcase']:
            assert component in mechanism

    def test_google_materiality_describes_chain(self):
        data = load_competitor_entities()
        leg = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['google_leg']
        assert 'materiality' in leg
        # Should describe the financial chain
        assert 'Cloud' in leg['materiality']


# ============================================================
# Class 4: Triangle Dynamics (Coverage Predictions)
# ============================================================
class TestTriangleDynamics:
    """Verify the coverage prediction model based on the triangle structure."""

    def test_pre_ipo_coverage_pressure(self):
        data = load_competitor_entities()
        dynamics = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['triangle_dynamics']
        names = [d['name'] for d in dynamics]
        assert 'pre_ipo_coverage_pressure' in names

    def test_settlement_revenue_adds_direct_layer(self):
        data = load_competitor_entities()
        dynamics = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['triangle_dynamics']
        names = [d['name'] for d in dynamics]
        assert 'settlement_revenue_adds_direct_layer' in names

    def test_zero_deal_paradox_explained(self):
        data = load_competitor_entities()
        dynamics = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['triangle_dynamics']
        names = [d['name'] for d in dynamics]
        assert 'zero_deal_paradox_explained' in names

    def test_coverage_prediction_exists(self):
        data = load_competitor_entities()
        dynamics = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['triangle_dynamics']
        names = [d['name'] for d in dynamics]
        assert 'coverage_prediction' in names

    def test_coverage_prediction_names_clean_controls(self):
        """Clean controls (Reuters, Gizmodo) should be identified."""
        data = load_competitor_entities()
        dynamics = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['triangle_dynamics']
        pred = [d for d in dynamics if d['name'] == 'coverage_prediction'][0]
        assert 'Reuters' in pred['detail']
        assert 'Gizmodo' in pred['detail']

    def test_coverage_prediction_names_most_exposed(self):
        """Most exposed publications should be identified."""
        data = load_competitor_entities()
        dynamics = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['triangle_dynamics']
        pred = [d for d in dynamics if d['name'] == 'coverage_prediction'][0]
        assert 'WIRED' in pred['detail'] or 'Condé Nast' in pred['detail']

    def test_settlement_dynamics_mentions_news_corp_triple(self):
        """News Corp receiving from all three AI companies should be noted."""
        data = load_competitor_entities()
        dynamics = data['entities']['anthropic']['investor_advertiser_publisher_triangle']['triangle_dynamics']
        settlement = [d for d in dynamics if d['name'] == 'settlement_revenue_adds_direct_layer'][0]
        assert 'News Corp' in settlement['detail'] or 'Thomson' in settlement['detail']
        assert 'THREE' in settlement['detail'] or 'three' in settlement['detail']


# ============================================================
# Class 5: Corrected "Financially Neutral" Claim
# ============================================================
class TestCorrectedNeutralityClaim:
    """The old claim that Anthropic is 'financially neutral' to all profiled
    publishers has been corrected to note the indirect relationship."""

    def test_old_claim_removed(self):
        """The unqualified 'financially neutral' claim should no longer exist."""
        data = load_competitor_entities()
        note = data['entities']['anthropic']['publisher_deals_note']
        # Should NOT say "financially neutral" without qualification
        assert 'financially neutral' not in note.lower() or 'not financially' in note.lower()

    def test_new_claim_references_triangle(self):
        """The publisher_deals_note should reference the triangle section."""
        data = load_competitor_entities()
        note = data['entities']['anthropic']['publisher_deals_note']
        assert 'investor_advertiser_publisher_triangle' in note or 'indirect' in note.lower()

    def test_no_direct_deals_still_stated(self):
        """The note should still accurately state zero DIRECT deals."""
        data = load_competitor_entities()
        note = data['entities']['anthropic']['publisher_deals_note']
        assert 'DIRECT' in note or 'direct' in note


# ============================================================
# Class 6: Cross-Validation with Amazon Entity
# ============================================================
class TestAmazonEntityCrossValidation:
    """Verify Amazon entity data is consistent with the triangle analysis."""

    def test_amazon_anthropic_investment_matches(self):
        data = load_competitor_entities()
        amazon = data['entities']['amazon']
        # Check sextuple leverage anthropic_investment layer
        anthropic_layer = None
        for layer in amazon.get('sextuple_publisher_leverage', {}).get('layers', []):
            if layer.get('name') == 'anthropic_investment':
                anthropic_layer = layer
                break
        assert anthropic_layer is not None
        assert anthropic_layer.get('anthropic_total_invested_b', 0) >= 13

    def test_amazon_q2_2026_ad_revenue_consistent(self):
        data = load_competitor_entities()
        amazon = data['entities']['amazon']
        q2 = amazon.get('q2_2026_earnings', {})
        assert q2.get('advertising_ttm_b', 0) >= 70  # $76B TTM

    def test_amazon_q2_2026_anthropic_gain_consistent(self):
        data = load_competitor_entities()
        amazon = data['entities']['amazon']
        q2 = amazon.get('q2_2026_earnings', {})
        assert q2.get('anthropic_gain_b', 0) == 53.4


# ============================================================
# Class 7: Meta Contrast (Structural Asymmetry)
# ============================================================
class TestMetaContrast:
    """The triangle reveals why Anthropic (zero deals) gets softer treatment
    than Meta (direct deals) — indirect incentives through investors."""

    def test_overview_mentions_meta_contrast(self):
        data = load_competitor_entities()
        tri = data['entities']['anthropic']['investor_advertiser_publisher_triangle']
        assert 'Meta' in tri['overview']

    def test_meta_has_no_investor_triangle(self):
        """Meta has no strategic investor whose advertising revenue flows to publishers."""
        data = load_competitor_entities()
        tri = data['entities']['anthropic']['investor_advertiser_publisher_triangle']
        overview = tri['overview']
        assert 'Meta has no strategic investor' in overview or 'no strategic investor' in overview

    def test_meta_relationship_is_direct(self):
        """Meta's publisher relationship is direct (licensing), not indirect."""
        data = load_competitor_entities()
        tri = data['entities']['anthropic']['investor_advertiser_publisher_triangle']
        overview = tri['overview']
        assert 'DIRECT' in overview or 'direct' in overview

    def test_triangle_makes_indirect_invisible(self):
        """The triangle's indirect nature makes it invisible to traditional disclosure."""
        data = load_competitor_entities()
        tri = data['entities']['anthropic']['investor_advertiser_publisher_triangle']
        overview = tri['overview']
        assert 'invisible' in overview.lower() or 'two-hop' in overview.lower() or 'disclosure' in overview.lower()


# ============================================================
# Class 8: Combined Revenue Scale
# ============================================================
class TestCombinedRevenueScale:
    """The combined Google+Amazon publisher revenue dwarfs any direct deal."""

    def test_combined_revenue_documented(self):
        """Google ($81.6B) + Amazon ($76B) = ~$157B annual publisher-touching revenue."""
        data = load_competitor_entities()
        tri = data['entities']['anthropic']['investor_advertiser_publisher_triangle']
        dynamics = tri['triangle_dynamics']
        paradox = [d for d in dynamics if d['name'] == 'zero_deal_paradox_explained'][0]
        # Should mention the combined scale
        assert '157' in paradox['detail'] or 'billion' in paradox['detail'].lower()

    def test_combined_equity_stake_documented(self):
        """Amazon (~$200B) + Google (~$135B) = ~$335B combined Anthropic equity."""
        data = load_competitor_entities()
        tri = data['entities']['anthropic']['investor_advertiser_publisher_triangle']
        dynamics = tri['triangle_dynamics']
        paradox = [d for d in dynamics if d['name'] == 'zero_deal_paradox_explained'][0]
        assert '335' in paradox['detail'] or 'equity' in paradox['detail'].lower()
