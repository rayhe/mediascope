"""
Mechanism #161: Advance Publications Reddit-Meta Advertising Direct Competition
Structural Incentive Chain (Aug 18, 2026)

Type C: Financial Incentive Mapping

DISCOVERY: Advance Publications — parent of Condé Nast (WIRED, Vogue, GQ, Vanity Fair,
The New Yorker) — holds 65.2% voting control and 83.5% of Class B stock in Reddit, which
EXPLICITLY competes with Meta for advertising revenue. Reddit launched Max Campaigns at
CES 2026 as a direct competitor to Meta Advantage+ and Google Performance Max. Meta
launched Forum (May 2026), a standalone Reddit-rival app built from Facebook Groups.

This creates a STRUCTURAL COMPETITIVE INCENTIVE: adversarial WIRED coverage of Meta
potentially steers advertiser attention away from Meta and toward competitors including
Reddit. The financial benefit flows to Advance through its Reddit stake (~$6-8B).

KEY EVIDENCE:
1. Reddit Max Campaigns launched Jan 6, 2026 (CES) — "Reddit's most direct push to
   compete with giants like Google and Meta for performance ad dollars" (Adweek)
2. Reddit Q1 2026: advertising revenue +74% YoY, active advertiser count +75% YoY
3. Reddit COO Jen Wong named Meta explicitly as competitor (Reuters Q4 2025 earnings)
4. Reuters (Feb 5, 2026): "Reddit is ratcheting up competition with Meta by rolling out
   AI-powered Max campaigns"
5. Meta launched Forum (May 21-22, 2026) — standalone Reddit-rival app
6. Reddit Q1 2026 revenue: $663.4M (+69.1% YoY), 94% from advertising
7. Advance voting control: 65.2% (up from 62.0% in 2025, concentrated via insider sells)
8. Former Condé Nast CEO Robert Sauerberg is Reddit Board Vice Chairperson

ADVANCE PUBLICATIONS DUAL-SURFACE COMPETITION:
- Surface 1 (Advertising): Reddit competes directly with Meta for ad dollars
- Surface 2 (Community): Meta Forum competes directly with Reddit for user engagement
Both competition surfaces create Advance financial incentive for adverse Meta coverage.

CONFOUNDERS:
1. (STRONG) Editorial independence — WIRED journalists may operate independently of
   Advance corporate interests. No documented editorial directive linking Reddit competition
   to WIRED coverage decisions.
2. (STRONG) Advertiser switching is complex — negative coverage of one platform doesn't
   automatically redirect budgets to Reddit.
3. (MODERATE) Meta's ad revenue ($233B) dwarfs Reddit's ($2.6B TTM) — Reddit's competitive
   impact on Meta is marginal in absolute terms.
4. (MODERATE) WIRED's adversarial Meta coverage predates Reddit Max Campaigns (Jan 2026),
   so the pattern isn't caused by this specific product launch.
5. (WEAK) Other publications without Reddit ownership also cover Meta adversarially,
   suggesting industry-wide dynamics beyond Advance-specific incentives.

CROSS-REFERENCES:
- Mechanism #1 (Advance-Reddit aggregate AI dependency)
- Mechanism #11 (ad competitor structural antagonism)
- Mechanism #69 (Reddit deal renewal projections — $550M/yr)
- Mechanism #159 (OpenAI companion vs Meta surveillance vocabulary bifurcation)

Source URLs:
- https://adweek.com/media/reddit-max-campaign-media-buying-ces/
- https://www.reuters.com/business/media-telecom/reddit-forecasts-revenue-above-estimates-ai-fuels-ad-sales-2026-02-05/
- https://www.reuters.com/business/media-telecom/reddit-expects-revenue-above-estimates-ai-tools-fuel-ad-growth-2026-04-30/
- https://techcrunch.com/2026/05/22/meta-quietly-launches-a-new-reddit-like-app-called-forum/
- https://www.zacks.com/stock/news/2938157/rddt-vs-meta-which-digital-advertising-stock-has-an-edge-right-now
- https://www.barrons.com/articles/buy-reddit-stock-price-pick-eef67fe8
"""

import unittest
import yaml
import os


def load_competitor_coverage_research():
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_wired_profile():
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'wired.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


class TestMechanismExists(unittest.TestCase):
    """Verify mechanism #161 exists with required structural fields."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage_research()
        cls.mechanism = cls.data.get('aggregate_findings', {}).get(
            'advance_reddit_meta_ad_competition_structural_incentive', {}
        )

    def test_mechanism_exists(self):
        self.assertTrue(self.mechanism, "Mechanism entry must exist")

    def test_mechanism_id(self):
        self.assertEqual(self.mechanism.get('mechanism_id'), 161)

    def test_has_finding_summary(self):
        self.assertIn('finding_summary', self.mechanism)
        self.assertGreater(len(self.mechanism['finding_summary']), 100)

    def test_has_source_urls(self):
        urls = self.mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 4)

    def test_has_confounding_factors(self):
        cfs = self.mechanism.get('confounding_factors', [])
        self.assertGreaterEqual(len(cfs), 4)
        strong = sum(1 for c in cfs if c.get('strength') == 'STRONG')
        self.assertGreaterEqual(strong, 2, "Must have at least 2 STRONG confounders")

    def test_has_cross_references(self):
        refs = self.mechanism.get('cross_references', [])
        self.assertGreaterEqual(len(refs), 3)

    def test_has_test_file(self):
        self.assertIn('test_file', self.mechanism)
        self.assertIn('advance_reddit_meta_ad_competition', self.mechanism['test_file'])

    def test_publication(self):
        self.assertIn('WIRED', self.mechanism.get('publication', ''))

    def test_key_finding(self):
        self.assertIn('key_finding', self.mechanism)
        kf = self.mechanism['key_finding'].lower()
        self.assertTrue('reddit' in kf or 'ad' in kf or 'competition' in kf)


class TestRedditMaxCampaigns(unittest.TestCase):
    """Verify Reddit Max Campaigns competitive data."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage_research()
        cls.mechanism = cls.data.get('aggregate_findings', {}).get(
            'advance_reddit_meta_ad_competition_structural_incentive', {}
        )

    def test_max_campaigns_launch_date(self):
        rd = self.mechanism.get('reddit_max_campaigns', {})
        self.assertIn('2026-01', rd.get('launch_date', ''))

    def test_max_campaigns_competitors_named(self):
        rd = self.mechanism.get('reddit_max_campaigns', {})
        comps = rd.get('direct_competitors', [])
        self.assertIn('Meta Advantage+', comps)
        self.assertIn('Google Performance Max', comps)

    def test_max_campaigns_source(self):
        rd = self.mechanism.get('reddit_max_campaigns', {})
        self.assertTrue(any('adweek' in u for u in rd.get('source_urls', [])))

    def test_reuters_ratcheting_quote(self):
        rd = self.mechanism.get('reddit_max_campaigns', {})
        self.assertIn('ratcheting', rd.get('reuters_characterization', '').lower())

    def test_alpha_advertiser_count(self):
        rd = self.mechanism.get('reddit_max_campaigns', {})
        self.assertGreaterEqual(rd.get('alpha_advertisers', 0), 600)


class TestRedditFinancials(unittest.TestCase):
    """Verify Reddit Q1 2026 financial data."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage_research()
        cls.mechanism = cls.data.get('aggregate_findings', {}).get(
            'advance_reddit_meta_ad_competition_structural_incentive', {}
        )

    def test_q1_2026_revenue(self):
        fin = self.mechanism.get('reddit_financials', {})
        self.assertAlmostEqual(fin.get('q1_2026_revenue_m', 0), 663.4, delta=5)

    def test_q1_2026_ad_revenue_growth_yoy(self):
        fin = self.mechanism.get('reddit_financials', {})
        self.assertGreaterEqual(fin.get('q1_2026_ad_revenue_growth_yoy_pct', 0), 70)

    def test_ad_revenue_share(self):
        fin = self.mechanism.get('reddit_financials', {})
        self.assertGreaterEqual(fin.get('ad_revenue_share_pct', 0), 90)

    def test_active_advertiser_growth(self):
        fin = self.mechanism.get('reddit_financials', {})
        self.assertGreaterEqual(fin.get('active_advertiser_growth_yoy_pct', 0), 70)

    def test_q2_2026_guidance(self):
        fin = self.mechanism.get('reddit_financials', {})
        guidance = fin.get('q2_2026_guidance_m', '')
        self.assertIn('715', str(guidance))


class TestMetaForumCompetition(unittest.TestCase):
    """Verify Meta Forum as Reddit-competitive product."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage_research()
        cls.mechanism = cls.data.get('aggregate_findings', {}).get(
            'advance_reddit_meta_ad_competition_structural_incentive', {}
        )

    def test_forum_launch_date(self):
        forum = self.mechanism.get('meta_forum', {})
        self.assertIn('2026-05', forum.get('launch_date', ''))

    def test_forum_is_reddit_competitor(self):
        forum = self.mechanism.get('meta_forum', {})
        self.assertTrue(forum.get('positioned_as_reddit_rival', False))

    def test_forum_sources(self):
        forum = self.mechanism.get('meta_forum', {})
        urls = forum.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 2)

    def test_forum_features_overlap(self):
        forum = self.mechanism.get('meta_forum', {})
        features = forum.get('reddit_overlap_features', [])
        self.assertGreaterEqual(len(features), 3)


class TestAdvanceOwnershipStake(unittest.TestCase):
    """Verify Advance Publications ownership data."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage_research()
        cls.mechanism = cls.data.get('aggregate_findings', {}).get(
            'advance_reddit_meta_ad_competition_structural_incentive', {}
        )

    def test_advance_voting_control(self):
        ownership = self.mechanism.get('advance_ownership', {})
        self.assertGreaterEqual(ownership.get('voting_control_pct', 0), 60)

    def test_advance_class_b_pct(self):
        ownership = self.mechanism.get('advance_ownership', {})
        self.assertGreaterEqual(ownership.get('class_b_ownership_pct', 0), 80)

    def test_sauerberg_governance_pipeline(self):
        ownership = self.mechanism.get('advance_ownership', {})
        self.assertIn('Sauerberg', str(ownership.get('governance_pipeline', '')))

    def test_advance_stake_value(self):
        ownership = self.mechanism.get('advance_ownership', {})
        self.assertGreaterEqual(ownership.get('stake_value_b', 0), 4)


class TestDualSurfaceCompetition(unittest.TestCase):
    """Verify the dual-surface competition framework."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage_research()
        cls.mechanism = cls.data.get('aggregate_findings', {}).get(
            'advance_reddit_meta_ad_competition_structural_incentive', {}
        )

    def test_has_dual_surface(self):
        ds = self.mechanism.get('dual_surface_competition', {})
        self.assertIn('advertising', ds)
        self.assertIn('community', ds)

    def test_advertising_surface(self):
        ds = self.mechanism.get('dual_surface_competition', {})
        ad = ds.get('advertising', {})
        self.assertIn('Reddit', ad.get('aggressor', ''))
        self.assertIn('Meta', ad.get('defender', ''))

    def test_community_surface(self):
        ds = self.mechanism.get('dual_surface_competition', {})
        comm = ds.get('community', {})
        self.assertIn('Meta', comm.get('aggressor', ''))
        self.assertIn('Reddit', comm.get('defender', ''))


class TestMediaScopeRelevance(unittest.TestCase):
    """Verify the MediaScope relevance analysis."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage_research()
        cls.mechanism = cls.data.get('aggregate_findings', {}).get(
            'advance_reddit_meta_ad_competition_structural_incentive', {}
        )

    def test_mediascope_relevance_exists(self):
        self.assertIn('mediascope_relevance', self.mechanism)

    def test_relevance_mentions_coverage_incentive(self):
        rel = self.mechanism.get('mediascope_relevance', '')
        self.assertTrue('coverage' in rel.lower() or 'adversarial' in rel.lower())

    def test_has_testable_predictions(self):
        preds = self.mechanism.get('testable_predictions', [])
        self.assertGreaterEqual(len(preds), 3)

    def test_meta_has_zero_advance_financial_relationship(self):
        rel = self.mechanism.get('mediascope_relevance', '')
        self.assertTrue('zero' in rel.lower() or 'no' in rel.lower())


class TestConfounders(unittest.TestCase):
    """Verify confounder analysis quality."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage_research()
        cls.mechanism = cls.data.get('aggregate_findings', {}).get(
            'advance_reddit_meta_ad_competition_structural_incentive', {}
        )

    def test_confounder_count(self):
        cfs = self.mechanism.get('confounding_factors', [])
        self.assertEqual(len(cfs), 5)

    def test_each_confounder_has_strength(self):
        cfs = self.mechanism.get('confounding_factors', [])
        for cf in cfs:
            self.assertIn(cf.get('strength', ''), ['STRONG', 'MODERATE', 'WEAK'])

    def test_each_confounder_has_description(self):
        cfs = self.mechanism.get('confounding_factors', [])
        for cf in cfs:
            self.assertIn('description', cf)
            self.assertGreater(len(cf['description']), 20)

    def test_editorial_independence_is_strong(self):
        cfs = self.mechanism.get('confounding_factors', [])
        editorial_cfs = [c for c in cfs if 'editorial' in c.get('description', '').lower()]
        self.assertGreater(len(editorial_cfs), 0)
        self.assertEqual(editorial_cfs[0]['strength'], 'STRONG')


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage_research()
        cls.mechanism = cls.data.get('aggregate_findings', {}).get(
            'advance_reddit_meta_ad_competition_structural_incentive', {}
        )

    def test_cross_ref_count(self):
        refs = self.mechanism.get('cross_references', [])
        self.assertGreaterEqual(len(refs), 3)

    def test_cross_ref_has_mechanism_ids(self):
        refs = self.mechanism.get('cross_references', [])
        for ref in refs:
            self.assertIn('mechanism_id', ref)
            self.assertIsInstance(ref['mechanism_id'], int)

    def test_ad_antagonism_cross_ref(self):
        refs = self.mechanism.get('cross_references', [])
        ids = [r['mechanism_id'] for r in refs]
        self.assertIn(11, ids, "Must cross-reference mechanism #11 (ad competitor structural antagonism)")


class TestDocSync(unittest.TestCase):
    """Verify documentation consistency."""

    def test_test_file_listed_in_architecture(self):
        arch_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'ARCHITECTURE.md')
        with open(arch_path) as f:
            arch = f.read()
        self.assertIn('advance_reddit_meta_ad_competition', arch)

    def test_mechanism_listed_in_readme(self):
        readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
        with open(readme_path) as f:
            readme = f.read()
        self.assertIn('advance_reddit_meta_ad_competition', readme)


if __name__ == '__main__':
    unittest.main()
