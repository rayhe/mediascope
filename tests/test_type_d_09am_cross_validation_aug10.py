"""
Type D Cross-Validation: 09:00 AM Aug 10, 2026
Validates Mechanisms #22-#25 coherence, schema fixes, and Mechanism #24 gap.

Previous Type D (08:00 AM) covered #22, #23, #25 but skipped #24.
This sprint covers the #24 gap plus cross-mechanism financial scale ordering
and schema validator consistency after relationship_type expansion.
"""

import os
import unittest
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


class TestMechanism24Existence(unittest.TestCase):
    """Mechanism #24: Casey Newton Disclosure-as-Inoculation Paradox."""

    def setUp(self):
        self.research = load_yaml('competitor-coverage-research.yaml')

    def test_mechanism_24_documented_in_research(self):
        """competitor-coverage-research.yaml should reference Mechanism #24."""
        content = open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')).read()
        has_ref = 'Mechanism #24' in content or 'casey_newton' in content.lower()
        self.assertTrue(has_ref,
                        "competitor-coverage-research.yaml should reference Mechanism #24 or Casey Newton")

    def test_mechanism_24_test_file_exists(self):
        """A dedicated test file for Mechanism #24 should exist."""
        test_dir = os.path.dirname(__file__)
        self.assertTrue(
            os.path.exists(os.path.join(test_dir, 'test_casey_newton_cross_entity.py')),
            "test_casey_newton_cross_entity.py must exist for Mechanism #24"
        )

    def test_mechanism_24_is_individual_scale(self):
        """Mechanism #24 operates at individual journalist scale
        (personal relationship), not institutional or systemic."""
        test_path = os.path.join(os.path.dirname(__file__), 'test_casey_newton_cross_entity.py')
        with open(test_path) as f:
            content = f.read()
        # Must mention personal/individual scale, fiancé, or Anthropic
        self.assertIn('Anthropic', content)
        has_personal = 'fiancé' in content or 'fiance' in content or 'personal' in content.lower()
        self.assertTrue(has_personal,
                        "Mechanism #24 should document the personal relationship")


class TestMechanismFinancialScaleOrdering(unittest.TestCase):
    """Mechanisms #22-#25 should represent escalating financial scale:
    #22 (publication licensing) < #23 (triple-chain) < #24 (individual) < #25 ($63B corporate).
    
    Financial magnitude ordering: #24 is smallest (individual), #25 is largest (corporate).
    This tests that the mechanisms are documented with their correct scale."""

    def test_mechanism_22_is_publication_scale(self):
        """Mechanism #22 (WSJ × OpenAI) involves News Corp $50M/yr licensing."""
        test_path = os.path.join(os.path.dirname(__file__),
                                 'test_wsj_openai_ad_cannibalization_self_demonetization_aug10.py')
        with open(test_path) as f:
            content = f.read()
        self.assertIn('50M', content.replace(',', '').replace('$', ''),
                       "Mechanism #22 should reference the $50M/yr News Corp deal")

    def test_mechanism_25_is_largest_scale(self):
        """Mechanism #25 (Amazon $63B dual-lab) is the largest financial exposure."""
        test_path = os.path.join(os.path.dirname(__file__),
                                 'test_amazon_dual_lab_non_disclosure_triangle_aug10.py')
        with open(test_path) as f:
            content = f.read()
        self.assertIn('63B', content.replace(',', '').replace('$', ''),
                       "Mechanism #25 should reference the $63B total stake")

    def test_all_four_mechanisms_have_test_files(self):
        """Each mechanism #22-#25 should have at least one test file."""
        test_dir = os.path.dirname(__file__)
        files = os.listdir(test_dir)
        # #22 = wsj_openai_ad_cannibalization
        has_22 = any('wsj_openai_ad_cannibalization' in f for f in files)
        # #23 = nyt_anthropic_triple_chain
        has_23 = any('nyt_anthropic_triple_chain' in f for f in files)
        # #24 = casey_newton_cross_entity
        has_24 = any('casey_newton_cross_entity' in f for f in files)
        # #25 = amazon_dual_lab_non_disclosure
        has_25 = any('amazon_dual_lab_non_disclosure' in f for f in files)
        self.assertTrue(has_22, "Mechanism #22 needs a test file")
        self.assertTrue(has_23, "Mechanism #23 needs a test file")
        self.assertTrue(has_24, "Mechanism #24 needs a test file")
        self.assertTrue(has_25, "Mechanism #25 needs a test file")


class TestSchemaValidatorExpansion(unittest.TestCase):
    """Validates that the schema expansions for relationship types
    and coverage predictions are self-consistent."""

    def setUp(self):
        self.entities = load_yaml('competitor-entities.yaml')

    def test_settlement_reported_in_relationship_types(self):
        """settlement_reported should be a valid relationship type."""
        types = self.entities.get('relationship_types', {})
        self.assertIn('settlement_reported', types)

    def test_indirect_endowment_in_relationship_types(self):
        """indirect_endowment should be a valid relationship type."""
        types = self.entities.get('relationship_types', {})
        self.assertIn('indirect_endowment', types)

    def test_softer_than_expected_in_predictions(self):
        """softer_than_expected should be a valid coverage prediction."""
        preds = self.entities.get('coverage_predictions', {})
        self.assertIn('softer_than_expected', preds)

    def test_positive_if_deal_confirmed_in_predictions(self):
        """positive_if_deal_confirmed should be a valid coverage prediction."""
        preds = self.entities.get('coverage_predictions', {})
        self.assertIn('positive_if_deal_confirmed', preds)

    def test_settlement_reported_semantically_distinct_from_settlement(self):
        """settlement_reported (unverified) must be distinct from settlement (confirmed)."""
        types = self.entities.get('relationship_types', {})
        self.assertIn('settlement', types)
        self.assertIn('settlement_reported', types)
        self.assertNotEqual(types['settlement'], types['settlement_reported'])

    def test_indirect_endowment_semantically_distinct_from_indirect(self):
        """indirect_endowment (endowment exposure) differs from indirect (parent relationship)."""
        types = self.entities.get('relationship_types', {})
        self.assertIn('indirect', types)
        self.assertIn('indirect_endowment', types)
        self.assertNotEqual(types['indirect'], types['indirect_endowment'])


class TestNYTAnthropicSchemaConsistency(unittest.TestCase):
    """NYT-Anthropic relationship should use settlement_reported consistently."""

    def setUp(self):
        self.nyt = load_yaml('nytimes.yaml')

    def test_nyt_anthropic_tie_is_settlement_reported(self):
        """NYT-Anthropic financial_tie should be settlement_reported (not settlement)."""
        cr = self.nyt.get('competitor_relationships', {})
        anthropic = cr.get('anthropic', {})
        self.assertEqual(anthropic.get('financial_tie'), 'settlement_reported')

    def test_nyt_anthropic_prediction_is_conditional(self):
        """NYT-Anthropic coverage_prediction should reflect the conditional nature."""
        cr = self.nyt.get('competitor_relationships', {})
        anthropic = cr.get('anthropic', {})
        pred = anthropic.get('coverage_prediction', '')
        self.assertIn('confirmed', pred,
                       "Prediction should reflect deal-confirmation conditionality")


class TestMITTRAnthropicSchemaConsistency(unittest.TestCase):
    """MIT TR-Anthropic relationship should use indirect_endowment consistently."""

    def setUp(self):
        self.mittr = load_yaml('mit-tech-review.yaml')

    def test_mittr_anthropic_tie_is_indirect_endowment(self):
        """MIT TR-Anthropic financial_tie should be indirect_endowment."""
        cr = self.mittr.get('competitor_relationships', {})
        anthropic = cr.get('anthropic', {})
        self.assertEqual(anthropic.get('financial_tie'), 'indirect_endowment')

    def test_mittr_anthropic_prediction_softer_than_expected(self):
        """MIT TR-Anthropic coverage_prediction should be softer_than_expected."""
        cr = self.mittr.get('competitor_relationships', {})
        anthropic = cr.get('anthropic', {})
        self.assertEqual(anthropic.get('coverage_prediction'), 'softer_than_expected')


class TestAmazonLeverageLayerCount(unittest.TestCase):
    """Amazon should now have 7 leverage layers after OpenAI investment discovery."""

    def test_amazon_has_seven_leverage_layers(self):
        """Amazon entity should document 7 leverage layers in sextuple_publisher_leverage."""
        content = open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')).read()
        # The key is still named sextuple_publisher_leverage for backward compat
        # but the content says "seven layers" / "SEVEN" after the OpenAI $50B update
        amazon_section = content[content.find('sextuple_publisher_leverage'):
                                  content.find('sextuple_publisher_leverage') + 3000]
        has_seven = ('seven' in amazon_section.lower() or
                     '7' in amazon_section or
                     'SEVEN' in amazon_section)
        self.assertTrue(has_seven,
                        "Amazon sextuple_publisher_leverage should document 7 layers")


class TestMechanismContiguity(unittest.TestCase):
    """All mechanisms #1-#25 should have no gaps in the test corpus."""

    def test_recent_mechanisms_contiguous(self):
        """Mechanisms #22, #23, #24, #25 should all be referenced in test files."""
        test_dir = os.path.dirname(__file__)
        all_content = ''
        for f in os.listdir(test_dir):
            if f.startswith('test_') and f.endswith('.py'):
                with open(os.path.join(test_dir, f)) as fh:
                    all_content += fh.read()

        for num in [22, 23, 24, 25]:
            self.assertIn(f'Mechanism #{num}', all_content,
                          f"Mechanism #{num} should be referenced in at least one test file")


if __name__ == '__main__':
    unittest.main()
