"""
Mechanism #208: Condé Nast CRO Career Migration → Snap Personnel Financial Incentive Architecture

Type: Financial Incentive Mapping — Personnel-Level Career Migration
Discovery Date: 2026-08-21
Iteration: #215

CORE DISCOVERY: Elizabeth Herbst-Brady, Condé Nast's Chief Revenue Officer (since Sep 2024),
previously held two senior roles at Snap Inc.: Head of Global Strategic Partnerships and Head
of East Coast Ad Sales. Full career: MAGNA Global → 20th Television → Starcom Worldwide →
Universal Television → Fox → Verizon → Snap Inc. → Viacom → Yahoo! (CRO + GM, Yahoo DSP) →
Condé Nast (CRO, Sep 2024).

As CRO she controls ALL revenue diversification: advertising, events (+40% in 2025),
subscriptions (+10%), commerce (+13%), and AI licensing deals (OpenAI, Perplexity, Amazon,
Apple Siri AI, Microsoft Copilot). Reports directly to CEO Roger Lynch.

PERSONNEL-LEVEL ASYMMETRY: The executive controlling WIRED parent revenue strategy has deep
Snap career history. Meta has ZERO personnel or financial ties to Condé Nast. When Snap
launches consumer Spectacles (Sep 16, 2026, $2,195, Los Angeles), the CRO's career
relationship creates asymmetric coverage incentives.

AI DEAL EVANGELIST: Thread Podcast (2026): "AI didn't kill premium media — it made it more
valuable." YouTube/Strike Social interview (Jul 2026): "Purposeful Large Language Model
Licensing" as commercial strategy.

SOURCES:
- https://www.adweek.com/morning-media-newsfeed/conde-nast-names-elizabeth-herbst-brady-chief-revenue-officer/
- http://archive.advertisingweek.com/events/ny/2023/speakers/?id=20599
- https://www.buzzsprout.com/1976572/episodes/18632585-ai-didn-t-kill-premium-media-it-made-it-more-valuable-elizabeth-herbst-brady-cro-of-conde-nast
- https://www.youtube.com/watch?v=PMxv1g-wKKE
- https://www.adweek.com/media/conde-nast-events-revenue-2026/
- https://mediabrief.com/conde-nast-names-elizabeth-herbst-brady-as-cro/
- https://www.gilderlehrman.org/about/elizabeth-herbst-brady

Cross-references: #8, #43, #133, #199
"""

import unittest
import yaml
import os


def load_wired_profile():
    """Load WIRED publication profile."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'wired.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    """Load competitor entities YAML."""
    path = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-entities.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestHerbstBradyCareerDataExists(unittest.TestCase):
    """Class 1: Verify Herbst-Brady career data exists in wired.yaml."""

    def setUp(self):
        self.profile = load_wired_profile()
        self.mechanism = self.profile.get('cro_career_migration_snap_link', {})

    def test_mechanism_section_exists(self):
        """Mechanism #208 section exists in wired.yaml."""
        self.assertIn('cro_career_migration_snap_link', self.profile)

    def test_mechanism_id_is_208(self):
        """Mechanism ID is 208."""
        self.assertEqual(self.mechanism['mechanism_id'], 208)

    def test_career_path_exists(self):
        """Career path list exists."""
        self.assertIn('career_path', self.mechanism)
        self.assertIsInstance(self.mechanism['career_path'], list)

    def test_career_path_has_10_employers(self):
        """Career path includes all 10 employer entries."""
        self.assertEqual(len(self.mechanism['career_path']), 10)

    def test_snap_in_career_path(self):
        """Snap Inc. appears in career path."""
        employers = [entry.get('employer', '') for entry in self.mechanism['career_path']]
        self.assertIn('Snap Inc.', employers)

    def test_snap_roles_documented(self):
        """Snap career entry has both roles documented."""
        snap_entry = None
        for entry in self.mechanism['career_path']:
            if entry.get('employer') == 'Snap Inc.':
                snap_entry = entry
                break
        self.assertIsNotNone(snap_entry, "Snap Inc. not found in career path")
        roles = snap_entry.get('roles', [])
        self.assertIn('Head of Global Strategic Partnerships', roles)
        self.assertIn('Head of East Coast Ad Sales', roles)

    def test_conde_nast_cro_role(self):
        """Condé Nast entry has CRO title and start date."""
        cn_entry = None
        for entry in self.mechanism['career_path']:
            if entry.get('employer') == 'Condé Nast':
                cn_entry = entry
                break
        self.assertIsNotNone(cn_entry, "Condé Nast not found in career path")
        self.assertEqual(cn_entry['role'], 'Chief Revenue Officer')
        self.assertEqual(cn_entry['start_date'], '2024-09')


class TestSnapSpecsLaunchData(unittest.TestCase):
    """Class 2: Verify Snap entity has Specs Sep 16 launch data in competitor-entities.yaml."""

    def setUp(self):
        data = load_competitor_entities()
        self.snap = data.get('entities', {}).get('snap', data.get('snap', {}))
        self.specs = self.snap.get('hardware_devices', {}).get('specs_consumer', {})

    def test_snap_entity_exists(self):
        """Snap entity exists in competitor-entities.yaml."""
        self.assertTrue(len(self.snap) > 0, "Snap entity not found")

    def test_consumer_launch_event_date(self):
        """Specs consumer launch event date is Sep 16, 2026."""
        self.assertEqual(self.specs.get('consumer_launch_event_date'), '2026-09-16')

    def test_consumer_launch_location(self):
        """Specs consumer launch location is Los Angeles."""
        self.assertEqual(self.specs.get('consumer_launch_location'), 'Los Angeles')

    def test_specs_price(self):
        """Specs price is $2,195."""
        self.assertEqual(self.specs.get('price_usd'), 2195)

    def test_mass_market_target(self):
        """Mass market target is end of the decade."""
        self.assertEqual(self.specs.get('mass_market_target'), 'end of the decade')


class TestMechanism208Exists(unittest.TestCase):
    """Class 3: Verify mechanism #208 entry exists in wired.yaml with required fields."""

    def setUp(self):
        self.profile = load_wired_profile()
        self.mechanism = self.profile.get('cro_career_migration_snap_link', {})

    def test_date_added(self):
        """Date added is 2026-08-21."""
        self.assertEqual(self.mechanism['date_added'], '2026-08-21')

    def test_overview_exists(self):
        """Overview is a non-empty string."""
        self.assertIsInstance(self.mechanism['overview'], str)
        self.assertGreater(len(self.mechanism['overview']), 100)

    def test_asymmetry_score(self):
        """Asymmetry score is 0.72."""
        self.assertAlmostEqual(self.mechanism['asymmetry_score'], 0.72, places=2)

    def test_finding_summary_exists(self):
        """Finding summary exists and is non-empty."""
        self.assertIn('finding_summary', self.mechanism)
        self.assertGreater(len(self.mechanism['finding_summary']), 50)

    def test_source_urls_exist(self):
        """Source URLs list exists with at least 5 entries."""
        urls = self.mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 5)

    def test_confounding_factors_exist(self):
        """Confounding factors list exists with entries."""
        factors = self.mechanism.get('confounding_factors', [])
        self.assertGreaterEqual(len(factors), 4)

    def test_testable_predictions_exist(self):
        """Testable predictions list exists with entries."""
        predictions = self.mechanism.get('testable_predictions', [])
        self.assertGreaterEqual(len(predictions), 2)

    def test_test_file_reference(self):
        """Test file reference points to this test file."""
        self.assertIn('test_conde_nast_cro_career_migration_snap_personnel_financial_architecture_aug21',
                      self.mechanism.get('test_file', ''))


class TestMetaZeroPersonnelLinks(unittest.TestCase):
    """Class 4: Verify Meta has zero personnel career-migration links to Condé Nast."""

    def setUp(self):
        self.profile = load_wired_profile()
        self.mechanism = self.profile.get('cro_career_migration_snap_link', {})

    def test_meta_contrast_documented(self):
        """Meta contrast section exists documenting zero personnel ties."""
        contrast = self.mechanism.get('meta_contrast', '')
        self.assertIn('ZERO', contrast)

    def test_meta_zero_personnel_ties(self):
        """Meta contrast explicitly states zero personnel career-migration links."""
        contrast = self.mechanism.get('meta_contrast', '')
        self.assertIn('personnel career-migration links', contrast.lower()
                      if contrast else '')

    def test_meta_zero_financial_partnership(self):
        """Meta contrast explicitly states no financial partnership."""
        contrast = self.mechanism.get('meta_contrast', '')
        self.assertIn('No financial partnership', contrast)

    def test_meta_most_adversarial_coverage(self):
        """Meta contrast notes most adversarial coverage."""
        contrast = self.mechanism.get('meta_contrast', '')
        self.assertIn('adversarial', contrast.lower() if contrast else '')


class TestCareerMigrationAsymmetry(unittest.TestCase):
    """Class 5: Verify the asymmetry (Snap has career link + financial ties; Meta has neither)."""

    def setUp(self):
        self.profile = load_wired_profile()
        self.mechanism = self.profile.get('cro_career_migration_snap_link', {})
        data = load_competitor_entities()
        self.snap = data.get('entities', {}).get('snap', data.get('snap', {}))

    def test_snap_has_career_link(self):
        """Snap has a documented career migration link through Herbst-Brady."""
        career_path = self.mechanism.get('career_path', [])
        snap_employers = [e for e in career_path if e.get('employer') == 'Snap Inc.']
        self.assertEqual(len(snap_employers), 1)

    def test_snap_has_financial_ties(self):
        """Snap has documented publisher financial relationships."""
        pub_rel = self.snap.get('publisher_financial_relationships', {})
        self.assertGreater(len(pub_rel), 0)

    def test_snap_has_perplexity_chain(self):
        """Snap has Perplexity financial chain to Condé Nast."""
        perplexity = self.snap.get('ai_partnerships', {}).get('perplexity', {})
        self.assertIn('perplexity_publisher_chain', perplexity)
        chain = perplexity.get('perplexity_publisher_chain', '')
        self.assertIn('Condé Nast', chain)

    def test_cross_references_include_key_mechanisms(self):
        """Cross-references include mechanisms #8, #43, #133, #199."""
        xrefs = self.mechanism.get('cross_references', [])
        for expected in [8, 43, 133, 199]:
            self.assertIn(expected, xrefs,
                          f"Expected mechanism #{expected} in cross-references")

    def test_snap_natural_experiment_documented(self):
        """Snap Specs consumer launch documented as natural experiment."""
        experiment = self.mechanism.get('snap_natural_experiment', {})
        self.assertEqual(experiment.get('date'), '2026-09-16')
        self.assertEqual(experiment.get('price_usd'), 2195)


class TestAIDealEvangelistStatements(unittest.TestCase):
    """Class 6: Verify Herbst-Brady's AI deal evangelist statements are documented."""

    def setUp(self):
        self.profile = load_wired_profile()
        self.mechanism = self.profile.get('cro_career_migration_snap_link', {})
        self.statements = self.mechanism.get('ai_deal_evangelist_statements', [])

    def test_statements_list_exists(self):
        """AI deal evangelist statements list exists."""
        self.assertIsInstance(self.statements, list)
        self.assertGreaterEqual(len(self.statements), 2)

    def test_thread_podcast_statement(self):
        """Thread Podcast statement documented with quote and URL."""
        thread_entries = [s for s in self.statements if 'Thread Podcast' in s.get('source', '')]
        self.assertEqual(len(thread_entries), 1)
        entry = thread_entries[0]
        self.assertIn("AI didn't kill premium media", entry.get('quote', ''))
        self.assertIn('buzzsprout.com', entry.get('url', ''))

    def test_youtube_strike_social_statement(self):
        """YouTube/Strike Social statement documented with description and URL."""
        yt_entries = [s for s in self.statements
                      if 'YouTube' in s.get('source', '') or 'Strike Social' in s.get('source', '')]
        self.assertEqual(len(yt_entries), 1)
        entry = yt_entries[0]
        self.assertIn('Purposeful Large Language Model Licensing', entry.get('description', ''))
        self.assertIn('youtube.com', entry.get('url', ''))

    def test_overview_mentions_ai_deals(self):
        """Overview mentions AI licensing deals that Herbst-Brady controls."""
        overview = self.mechanism.get('overview', '')
        for deal_partner in ['OpenAI', 'Perplexity', 'Amazon', 'Apple']:
            self.assertIn(deal_partner, overview,
                          f"Expected {deal_partner} in overview")


if __name__ == '__main__':
    unittest.main()
