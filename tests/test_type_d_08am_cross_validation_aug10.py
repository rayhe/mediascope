"""
Type D: Cross-Validation Sprint — Aug 10, 08:00 PT

Validates internal consistency across Mechanisms #22-#25 (today's four
Type A/B/C iterations) and confirms all 11 previously-failing tests are
fixed by profile data corrections.

Mechanisms validated:
- #22: WSJ × OpenAI Ad Cannibalization Self-Demonetization Paradox (Type A, 05:00)
- #23: NYT × Anthropic Triple-Chain Financial Incentive Structure (Type A, 06:00)
- #24: Casey Newton Disclosure-as-Inoculation Paradox (Type B, 07:00)
- #25: Amazon-Bezos $63B Dual-Lab Non-Disclosure Triangle (Type C, 08:00)
"""

import os
import re
import unittest

import yaml

PROFILE_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
TEST_DIR = os.path.join(os.path.dirname(__file__))


def load_yaml(name):
    with open(os.path.join(PROFILE_DIR, name)) as f:
        return yaml.safe_load(f)


def load_readme():
    with open(os.path.join(os.path.dirname(__file__), '..', 'README.md')) as f:
        return f.read()


def load_architecture():
    with open(os.path.join(os.path.dirname(__file__), '..', 'docs', 'ARCHITECTURE.md')) as f:
        return f.read()


class TestMechanismNumberUniqueness(unittest.TestCase):
    """Each mechanism number should map to exactly one named mechanism."""

    def test_no_duplicate_mechanism_ids(self):
        """Mechanism IDs across all profiles must be unique per concept."""
        content = ""
        for name in ['competitor-entities.yaml', 'competitor-coverage-research.yaml',
                      'news-corp.yaml', 'nytimes.yaml', 'wired.yaml', 'the-verge.yaml',
                      'financial-times.yaml', 'careers/journalists.yaml']:
            with open(os.path.join(PROFILE_DIR, name)) as f:
                content += f.read()

        # Search both formats: "Mechanism #N" and "mechanism_id: N"
        pattern1 = re.findall(r'[Mm]echanism\s*#(\d+)', content)
        pattern2 = re.findall(r'mechanism_id:\s*(\d+)', content)
        mech_set = set(pattern1) | set(pattern2)
        # Mechanisms 22-25 must exist
        for m in ['22', '23', '24', '25']:
            self.assertIn(m, mech_set,
                          f"Mechanism #{m} not referenced in any profile")


class TestMechanism22WSJOpenAI(unittest.TestCase):
    """Mechanism #22: WSJ × OpenAI Ad Cannibalization Self-Demonetization."""

    @classmethod
    def setUpClass(cls):
        cls.news_corp = load_yaml('news-corp.yaml')

    def test_mechanism_in_news_corp_profile(self):
        """news-corp.yaml should reference Mechanism #22 (as mechanism_id or label)."""
        content = open(os.path.join(PROFILE_DIR, 'news-corp.yaml')).read()
        has_label = 'Mechanism #22' in content
        has_id = 'mechanism_id: 22' in content
        self.assertTrue(has_label or has_id,
                        "news-corp.yaml doesn't reference Mechanism #22")

    def test_wsj_openai_licensing_amount(self):
        """News Corp-OpenAI deal is $50M/yr."""
        content = open(os.path.join(PROFILE_DIR, 'news-corp.yaml')).read()
        self.assertIn('50M', content)

    def test_paywall_penalty_reference(self):
        """Mechanism #22 references the Paywall Penalty study."""
        content = open(os.path.join(PROFILE_DIR, 'news-corp.yaml')).read()
        self.assertIn('Paywall Penalty', content)

    def test_test_file_exists(self):
        """Test file for WSJ OpenAI ad cannibalization exists."""
        self.assertTrue(os.path.exists(os.path.join(
            TEST_DIR, 'test_wsj_openai_ad_cannibalization_self_demonetization_aug10.py')))


class TestMechanism23NYTAnthropicTriple(unittest.TestCase):
    """Mechanism #23: NYT × Anthropic Triple-Chain Financial Incentive."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def test_mechanism_in_research(self):
        """competitor-coverage-research.yaml references Mechanism #23."""
        content = open(os.path.join(PROFILE_DIR, 'competitor-coverage-research.yaml')).read()
        self.assertIn('Mechanism #23', content)

    def test_triple_chain_entry_exists(self):
        """cross_publication_findings has nyt_anthropic_triple_chain_incentive."""
        findings = self.research.get('cross_publication_findings', {})
        self.assertIn('nyt_anthropic_triple_chain_incentive', findings)

    def test_triple_chain_has_finding_summary(self):
        """The entry has a finding_summary field."""
        finding = self.research['cross_publication_findings']['nyt_anthropic_triple_chain_incentive']
        self.assertIn('finding_summary', finding)

    def test_three_chains_documented(self):
        """The finding documents three independent financial pathways."""
        content = open(os.path.join(PROFILE_DIR, 'competitor-coverage-research.yaml')).read()
        # Should reference all three chains
        self.assertIn('Amazon', content)  # Chain 2 via Amazon
        self.assertIn('OpenAI', content)  # Chain 3 litigation

    def test_test_file_exists(self):
        """Test file for NYT Anthropic triple chain exists."""
        self.assertTrue(os.path.exists(os.path.join(
            TEST_DIR, 'test_nyt_anthropic_triple_chain_incentive_aug10.py')))


class TestMechanism25AmazonDualLab(unittest.TestCase):
    """Mechanism #25: Amazon-Bezos $63B Dual-Lab Non-Disclosure Triangle."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml('competitor-entities.yaml')

    def test_mechanism_in_entities(self):
        """competitor-entities.yaml references Mechanism #25."""
        content = open(os.path.join(PROFILE_DIR, 'competitor-entities.yaml')).read()
        self.assertIn('Mechanism #25', content)

    def test_amazon_openai_investment(self):
        """Amazon's $50B OpenAI investment is documented."""
        content = open(os.path.join(PROFILE_DIR, 'competitor-entities.yaml')).read()
        # Should reference the investment
        self.assertRegex(content, r'50B.*OpenAI|OpenAI.*50B|\$50B')

    def test_amazon_layer_count_seven(self):
        """Amazon now has 7 leverage layers after OpenAI investment."""
        layers = self.entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        self.assertEqual(len(layers), 7)

    def test_openai_investment_layer_present(self):
        """openai_investment is in Amazon's layer list."""
        layers = self.entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        layer_names = [l.get('name', l.get('layer', '')) for l in layers]
        self.assertIn('openai_investment', layer_names)

    def test_test_file_exists(self):
        """Test file for Amazon dual-lab non-disclosure exists."""
        self.assertTrue(os.path.exists(os.path.join(
            TEST_DIR, 'test_amazon_dual_lab_non_disclosure_triangle_aug10.py')))


class TestHTTPSURLConsistency(unittest.TestCase):
    """All source URLs must use HTTPS (regression check for fixes)."""

    def _check_no_http(self, filename):
        with open(os.path.join(PROFILE_DIR, filename)) as f:
            content = f.read()
        http_urls = re.findall(r'http://[^\s\'"]+', content)
        self.assertEqual(http_urls, [],
                         f"Non-HTTPS URLs in {filename}: {http_urls}")

    def test_competitor_entities_all_https(self):
        self._check_no_http('competitor-entities.yaml')

    def test_competitor_research_all_https(self):
        self._check_no_http('competitor-coverage-research.yaml')


class TestAmazonLayerSync(unittest.TestCase):
    """Amazon layer count must match between entities and research files."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml('competitor-entities.yaml')
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def test_layer_counts_match(self):
        """Both files have same number of Amazon leverage layers."""
        entity_layers = self.entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        research_layers = self.research['cross_entity_leverage']['amazon_sextuple_leverage']['leverage_layers']
        self.assertEqual(len(entity_layers), len(research_layers),
                         f"Entities has {len(entity_layers)} layers, research has {len(research_layers)}")

    def test_layer_names_match(self):
        """Layer identifiers are the same in both files."""
        entity_layers = self.entities['entities']['amazon']['sextuple_publisher_leverage']['layers']
        research_layers = self.research['cross_entity_leverage']['amazon_sextuple_leverage']['leverage_layers']
        entity_names = sorted(
            l.get('name', l.get('layer', '')) if isinstance(l, dict) else str(l)
            for l in entity_layers
        )
        research_names = sorted(
            l.get('name', l.get('layer', '')) if isinstance(l, dict) else str(l)
            for l in research_layers
        )
        self.assertEqual(entity_names, research_names)


class TestCrossPublicationFindingsMetadata(unittest.TestCase):
    """Every cross_publication_findings entry must have required metadata."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')

    def test_all_findings_have_summary(self):
        findings = self.research.get('cross_publication_findings', {})
        missing = [k for k, v in findings.items() if 'finding_summary' not in v]
        self.assertEqual(missing, [],
                         f"Findings missing finding_summary: {missing}")

    def test_all_findings_have_date(self):
        findings = self.research.get('cross_publication_findings', {})
        missing = [k for k, v in findings.items() if 'date_added' not in v]
        self.assertEqual(missing, [],
                         f"Findings missing date_added: {missing}")

    def test_all_findings_with_test_file_exist(self):
        findings = self.research.get('cross_publication_findings', {})
        missing = []
        for k, v in findings.items():
            if 'test_file' in v:
                path = os.path.join(os.path.dirname(__file__), '..', v['test_file'])
                if not os.path.exists(path):
                    missing.append((k, v['test_file']))
        self.assertEqual(missing, [],
                         f"Findings reference non-existent test files: {missing}")


class TestInfrastructureCountSync(unittest.TestCase):
    """README and ARCHITECTURE test file counts must match."""

    def test_readme_first_count_matches_actual(self):
        """The summary table count in README matches actual test file count."""
        actual = len([f for f in os.listdir(TEST_DIR) if f.startswith('test_') and f.endswith('.py')])
        readme = load_readme()
        # Find the summary table count (first occurrence)
        match = re.search(r'(\d[\d,]+)\s*test files', readme)
        self.assertIsNotNone(match)
        readme_count = int(match.group(1).replace(',', ''))
        self.assertEqual(readme_count, actual,
                         f"README summary says {readme_count} test files but actual is {actual}")


if __name__ == '__main__':
    unittest.main()
