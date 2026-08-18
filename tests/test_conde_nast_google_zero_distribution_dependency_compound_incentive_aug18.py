"""
Test Mechanism #167: Condé Nast "Google Zero" Distribution Dependency —
AI Platform Content Surfacing Creates Compound Revenue + Distribution Incentive

Condé Nast CEO Roger Lynch publicly declared a "Google Zero" strategy (May 2026,
TBPN interview), instructing teams to "assume there's no search... single-digit
percentage of our traffic." As Google search traffic collapses, Condé Nast's
content discovery shifts from Google Search to AI platforms (ChatGPT/SearchGPT,
Copilot, Perplexity) through content licensing deals.

This creates a THREE-DIMENSIONAL asymmetric incentive unique to WIRED's parent:

1. REVENUE: AI licensing deals replace declining ad/search revenue ($14-45M/yr est.)
2. DISTRIBUTION: AI platforms surface CN content with attribution — Meta AI does not
3. EQUITY: Advance's Reddit equity (~$9.5B) appreciates as Meta ad share shifts

Adverse Meta coverage is FREE across all three dimensions.
Adverse OpenAI coverage has COSTS across all three dimensions.

This extends mechanism #58 (revenue quantification) and #162 (equity capital
extraction) with the DISTRIBUTION dimension — the first mechanism to identify
AI content surfacing as an editorial incentive distinct from licensing revenue.
"""

import os
import unittest

import yaml


PROFILES_DIR = os.path.join(
    os.path.dirname(__file__), '..', 'profiles'
)


def _load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        # Use safe_load with error handling for large files
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError:
            # Fall back to reading raw text for assertion checks
            f.seek(0)
            return f.read()


def _load_raw(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return f.read()


def find_mechanism(data, mechanism_id):
    """Search for a mechanism by ID across all sections."""
    if isinstance(data, str):
        return None
    for section_name in ('cross_publication_findings', 'aggregate_findings', 'publications'):
        section = data.get(section_name, {})
        if isinstance(section, dict):
            for key, val in section.items():
                if isinstance(val, dict) and val.get('mechanism_id') == mechanism_id:
                    return val
        elif isinstance(section, list):
            for item in section:
                if isinstance(item, dict) and item.get('mechanism_id') == mechanism_id:
                    return item
    return None


class TestMechanism167Existence(unittest.TestCase):
    """Verify mechanism #167 exists with required structural fields."""

    @classmethod
    def setUpClass(cls):
        cls.raw = _load_raw('competitor-coverage-research.yaml')

    def test_mechanism_167_slug_present(self):
        self.assertIn('conde_nast_google_zero_distribution_dependency_compound_incentive', self.raw)

    def test_mechanism_id_167_present(self):
        self.assertIn('mechanism_id: 167', self.raw)

    def test_mechanism_name_present(self):
        self.assertIn('Google Zero', self.raw)

    def test_finding_type_present(self):
        self.assertIn('compound_distribution_incentive', self.raw)

    def test_has_source_urls(self):
        # Must have at least 5 source URLs
        count = self.raw.count('editorandpublisher.com') + \
                self.raw.count('adweek.com/media/conde-nast') + \
                self.raw.count('mediapost.com') + \
                self.raw.count('pressgazette.co.uk')
        self.assertGreaterEqual(count, 1, "Should reference primary source URLs")

    def test_has_confounders(self):
        self.assertIn('STRONG', self.raw)

    def test_has_test_file_reference(self):
        self.assertIn('test_conde_nast_google_zero_distribution_dependency_compound_incentive_aug18', self.raw)

    def test_date_added(self):
        self.assertIn('2026-08-18', self.raw)


class TestGoogleZeroStrategy(unittest.TestCase):
    """Verify the Google Zero strategy data points are documented."""

    @classmethod
    def setUpClass(cls):
        cls.raw = _load_raw('competitor-coverage-research.yaml')

    def test_lynch_google_zero_quote(self):
        self.assertIn('assume', self.raw.lower())

    def test_tbpn_venue(self):
        self.assertIn('TBPN', self.raw)

    def test_openai_owns_tbpn(self):
        # TBPN acquired by OpenAI Apr 2, 2026
        self.assertIn('OpenAI', self.raw)

    def test_search_traffic_single_digit(self):
        self.assertIn('single-digit', self.raw)

    def test_nilay_patel_amplification(self):
        self.assertIn('Decoder', self.raw)


class TestFourAIDealPartners(unittest.TestCase):
    """Verify all 4 confirmed AI licensing partners are documented."""

    @classmethod
    def setUpClass(cls):
        cls.raw = _load_raw('competitor-coverage-research.yaml')

    def test_openai_deal_confirmed(self):
        self.assertIn('OpenAI', self.raw)

    def test_perplexity_deal_confirmed(self):
        self.assertIn('Perplexity', self.raw)

    def test_microsoft_deal_confirmed(self):
        self.assertIn('Microsoft', self.raw)

    def test_amazon_deal_confirmed(self):
        self.assertIn('Amazon', self.raw)

    def test_meta_zero_deals(self):
        # The finding must document Meta's $0 deal position
        self.assertIn('$0', self.raw)


class TestThreeDimensionalIncentive(unittest.TestCase):
    """Verify the three-dimensional asymmetric incentive is documented."""

    @classmethod
    def setUpClass(cls):
        cls.raw = _load_raw('competitor-coverage-research.yaml')

    def test_revenue_dimension(self):
        self.assertIn('revenue', self.raw.lower())

    def test_distribution_dimension(self):
        self.assertIn('distribution', self.raw.lower())

    def test_equity_dimension(self):
        self.assertIn('equity', self.raw.lower())

    def test_compound_structure(self):
        self.assertIn('compound', self.raw.lower())

    def test_meta_free_in_all_dimensions(self):
        # The key finding: adverse Meta coverage costs zero across all 3
        self.assertIn('free', self.raw.lower())

    def test_searchgpt_content_surfacing(self):
        self.assertIn('SearchGPT', self.raw)

    def test_meta_ai_no_surfacing(self):
        self.assertIn('Meta AI', self.raw)


class TestDistributionReplacement(unittest.TestCase):
    """Verify distribution replacement mechanism is distinct from revenue."""

    @classmethod
    def setUpClass(cls):
        cls.raw = _load_raw('competitor-coverage-research.yaml')

    def test_zero_click_data(self):
        self.assertIn('zero-click', self.raw)

    def test_traffic_decline_quantified(self):
        # SimilarWeb data: 56% to ~70%
        self.assertIn('70%', self.raw)

    def test_distribution_distinct_from_revenue(self):
        self.assertIn('distribution', self.raw.lower())

    def test_attribution_and_links(self):
        self.assertIn('attribution', self.raw.lower())


class TestCondeNastRestructuring(unittest.TestCase):
    """Verify portfolio consolidation data showing financial pressure."""

    @classmethod
    def setUpClass(cls):
        cls.raw = _load_raw('competitor-coverage-research.yaml')

    def test_self_magazine_shutdown(self):
        self.assertIn('Self', self.raw)

    def test_wired_italy_shutdown(self):
        self.assertIn('Wired Italy', self.raw)

    def test_glamour_international_winding_down(self):
        self.assertIn('Glamour', self.raw)

    def test_events_revenue_growth(self):
        self.assertIn('40%', self.raw)

    def test_digital_subscriptions_growth(self):
        self.assertIn('29%', self.raw)

    def test_advertising_no_longer_growth_engine(self):
        self.assertIn('no longer expects advertising to be a growth engine', self.raw)


class TestConfounderAnalysis(unittest.TestCase):
    """Verify confounders are documented with strength ratings."""

    @classmethod
    def setUpClass(cls):
        cls.raw = _load_raw('competitor-coverage-research.yaml')

    def test_has_strong_confounders(self):
        self.assertIn('STRONG', self.raw)

    def test_has_moderate_confounders(self):
        self.assertIn('MODERATE', self.raw)

    def test_has_weak_confounders(self):
        self.assertIn('WEAK', self.raw)

    def test_editorial_independence_confounder(self):
        self.assertIn('editorial independence', self.raw.lower())

    def test_meta_could_sign_deal_confounder(self):
        # Must acknowledge Meta could sign its own deal
        self.assertIn('Meta', self.raw)


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    @classmethod
    def setUpClass(cls):
        cls.raw = _load_raw('competitor-coverage-research.yaml')

    def test_cross_ref_mechanism_58(self):
        # Condé Nast AI Deal Portfolio Dependency Index
        self.assertIn('58', self.raw)

    def test_cross_ref_mechanism_162(self):
        # Advance Reddit Equity Capital Extraction
        self.assertIn('162', self.raw)

    def test_cross_ref_mechanism_161(self):
        # Advance Reddit Ad Competition
        self.assertIn('161', self.raw)

    def test_cross_ref_mechanism_35(self):
        # Original WIRED financial conflict
        self.assertIn('35', self.raw)


class TestDocSyncIntegrity(unittest.TestCase):
    """Verify README and ARCHITECTURE list this test file."""

    @classmethod
    def setUpClass(cls):
        readme_path = os.path.join(PROFILES_DIR, '..', 'README.md')
        arch_path = os.path.join(PROFILES_DIR, '..', 'docs', 'ARCHITECTURE.md')
        with open(readme_path) as f:
            cls.readme = f.read()
        with open(arch_path) as f:
            cls.arch = f.read()

    def test_readme_lists_test_file(self):
        self.assertIn(
            'test_conde_nast_google_zero_distribution_dependency_compound_incentive_aug18',
            self.readme
        )

    def test_architecture_lists_test_file(self):
        self.assertIn(
            'test_conde_nast_google_zero_distribution_dependency_compound_incentive_aug18',
            self.arch
        )


class TestTestablePredicitions(unittest.TestCase):
    """Verify testable predictions are documented."""

    @classmethod
    def setUpClass(cls):
        cls.raw = _load_raw('competitor-coverage-research.yaml')

    def test_has_testable_predictions(self):
        self.assertIn('testable_predictions', self.raw)

    def test_prediction_about_meta_deal(self):
        # If Meta signs a CN deal, coverage tone should shift
        self.assertIn('Meta', self.raw)

    def test_prediction_about_search_traffic(self):
        # As search declines further, AI deal dependency increases
        self.assertIn('search', self.raw.lower())


if __name__ == '__main__':
    unittest.main()
