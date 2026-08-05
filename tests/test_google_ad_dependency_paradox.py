"""
Test the Google Advertising Revenue Dependency Paradox.

Publishers' own SDNY antitrust lawsuit filings (Jan 2026) reveal they are
simultaneously suing Google for ad revenue suppression AND admitting complete
dependency on Google's ad exchange for financial survival.

Sources:
- Digiday running list: http://digiday.com/media/a-running-list-of-publisher-lawsuits-targeting-googles-ad-tech-practices/
- Vox Media complaint: https://ppc.land/content/files/2026/01/1768500307197.pdf
- Bloomberg Tax: https://news.bloombergtax.com/esg/googles-ad-tech-litigation-defense-grows-as-publishers-pile-on
- Apple News+ / Atlantic: https://digiday.com/media/media-briefing-publishers-see-apple-news-as-a-stable-revenue-stream-amid-volatile-referral-traffic/

Added: 2026-08-05 Type C iteration (Financial Incentive Mapping)
"""

import os
import unittest

import yaml


PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


class TestAdvertisingDependencyType(unittest.TestCase):
    """Validate the new advertising_dependency relationship type."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml("competitor-entities.yaml")

    def test_advertising_dependency_type_defined(self):
        """advertising_dependency must be a valid relationship type."""
        types = self.entities.get("relationship_types", {})
        self.assertIn("advertising_dependency", types)

    def test_advertising_dependency_description(self):
        """advertising_dependency must have a meaningful description."""
        types = self.entities.get("relationship_types", {})
        desc = types.get("advertising_dependency", "")
        self.assertIn("dependent", desc.lower())


class TestPublisherAdxDependencyAdmissions(unittest.TestCase):
    """Validate that publisher lawsuit self-admissions about Google AdX
    dependency are documented in the aggregate findings."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml("competitor-coverage-research.yaml")
        cls.findings = cls.research.get("aggregate_findings", {}).get("key_evidence", [])

    def test_google_ad_dependency_finding_exists(self):
        """Aggregate findings must include the Google ad dependency paradox."""
        found = any("dependency" in f.get("finding", "").lower() or
                     "ad revenue dependency" in f.get("finding", "").lower()
                     for f in self.findings)
        self.assertTrue(found, "No Google ad dependency paradox finding")

    def test_finding_mentions_vox_media(self):
        """Dependency finding must reference Vox Media's admission."""
        dep = [f for f in self.findings
               if "dependency" in f.get("finding", "").lower()]
        text = str(dep)
        self.assertIn("Vox Media", text)

    def test_finding_mentions_atlantic(self):
        """Dependency finding must reference The Atlantic's admission."""
        dep = [f for f in self.findings
               if "dependency" in f.get("finding", "").lower()]
        text = str(dep)
        self.assertIn("Atlantic", text)

    def test_finding_mentions_advance_publications(self):
        """Dependency finding must reference Advance Publications' admission."""
        dep = [f for f in self.findings
               if "dependency" in f.get("finding", "").lower()]
        text = str(dep)
        self.assertIn("Advance", text)

    def test_finding_has_source_urls(self):
        """Dependency finding must have source URLs."""
        dep = [f for f in self.findings
               if "dependency" in f.get("finding", "").lower()]
        self.assertTrue(len(dep) > 0, "No dependency finding found")
        urls = dep[0].get("source_urls", [])
        self.assertTrue(len(urls) >= 2, f"Need at least 2 source URLs, got {len(urls)}")

    def test_three_layer_relationship_documented(self):
        """Finding must document the triple-layer Google relationship."""
        dep = [f for f in self.findings
               if "dependency" in f.get("finding", "").lower()]
        text = str(dep)
        # Must mention all three layers
        self.assertTrue("litigation" in text.lower() or "suing" in text.lower(),
                        "Must mention litigation layer")
        self.assertTrue("dependency" in text.lower() or "dependent" in text.lower(),
                        "Must mention dependency layer")
        self.assertTrue("coercive" in text.lower() or "coercion" in text.lower(),
                        "Must mention coercive layer")


class TestVergeGoogleRelationshipUpdated(unittest.TestCase):
    """The Verge's Google relationship should reflect dual lawsuit + dependency."""

    @classmethod
    def setUpClass(cls):
        cls.verge = load_yaml("the-verge.yaml")

    def test_google_is_adversarial_litigation(self):
        """The Verge-Google should be adversarial_litigation."""
        cr = self.verge.get("competitor_relationships", {})
        google = cr.get("google", {})
        self.assertEqual(google.get("financial_tie"), "adversarial_litigation")

    def test_google_mentions_both_lawsuits(self):
        """Description should mention both AI Overviews and adtech lawsuits."""
        cr = self.verge.get("competitor_relationships", {})
        google = cr.get("google", {})
        desc = google.get("description", "")
        self.assertIn("AI Overviews", desc)
        self.assertIn("adtech", desc.lower())

    def test_google_mentions_revenue_dependency(self):
        """Description should include Vox Media's revenue dependency admission."""
        cr = self.verge.get("competitor_relationships", {})
        google = cr.get("google", {})
        desc = google.get("description", "")
        self.assertTrue(
            "well over half" in desc or "half of its revenue" in desc.lower(),
            "Should mention Vox Media's admission about digital ad revenue share"
        )

    def test_google_has_adtech_source_url(self):
        """Must have source URL for adtech lawsuit."""
        cr = self.verge.get("competitor_relationships", {})
        google = cr.get("google", {})
        # Either in source_url or adtech_lawsuit_source
        has_adtech_url = (
            "adtech_lawsuit_source" in google or
            "digiday" in google.get("source_url", "").lower()
        )
        self.assertTrue(has_adtech_url, "Missing adtech lawsuit source URL")


class TestAtlanticGoogleRelationshipUpdated(unittest.TestCase):
    """The Atlantic's Google relationship should reflect adtech lawsuit."""

    @classmethod
    def setUpClass(cls):
        cls.atlantic = load_yaml("atlantic.yaml")

    def test_google_is_adversarial_litigation(self):
        """Atlantic-Google should be adversarial_litigation."""
        cr = self.atlantic.get("competitor_relationships", {})
        google = cr.get("google", {})
        self.assertEqual(google.get("financial_tie"), "adversarial_litigation")

    def test_google_mentions_adx_dependency(self):
        """Description should include Atlantic's AdX dependency admission."""
        cr = self.atlantic.get("competitor_relationships", {})
        google = cr.get("google", {})
        desc = google.get("description", "")
        self.assertTrue(
            "cannot forgo" in desc or "AdX" in desc,
            "Should mention Atlantic's admission about Google AdX dependency"
        )

    def test_google_has_source_url(self):
        """Must have source URL."""
        cr = self.atlantic.get("competitor_relationships", {})
        google = cr.get("google", {})
        self.assertIn("source_url", google)
        self.assertTrue(google["source_url"].startswith("http"))


class TestAtlanticAppleNewsPlus(unittest.TestCase):
    """The Atlantic's Apple relationship now includes Apple News+ revenue."""

    @classmethod
    def setUpClass(cls):
        cls.atlantic = load_yaml("atlantic.yaml")
        cls.research = load_yaml("competitor-coverage-research.yaml")

    def test_apple_estimated_value_includes_news_plus(self):
        """Apple estimated value should mention Apple News+."""
        cr = self.atlantic.get("competitor_relationships", {})
        apple = cr.get("apple", {})
        value = apple.get("estimated_value", "")
        self.assertIn("News+", value,
                      f"Apple value should mention News+, got: {value}")

    def test_apple_description_dual_relationship(self):
        """Apple description should document both ownership and platform revenue."""
        cr = self.atlantic.get("competitor_relationships", {})
        apple = cr.get("apple", {})
        desc = apple.get("description", "")
        self.assertIn("DUAL", desc.upper(),
                      "Should mention dual relationship")
        self.assertIn("syndication", desc.lower(),
                      "Should mention most valuable syndication partner")

    def test_apple_has_news_plus_source(self):
        """Apple relationship must have Apple News+ source URL."""
        cr = self.atlantic.get("competitor_relationships", {})
        apple = cr.get("apple", {})
        has_news_source = "apple_news_source" in apple
        self.assertTrue(has_news_source, "Missing apple_news_source URL")

    def test_research_atlantic_apple_mentions_news_plus(self):
        """Competitor coverage research for Atlantic should mention Apple News+."""
        pubs = self.research.get("publications", {})
        atlantic = pubs.get("atlantic", {})
        summary = atlantic.get("apple_coverage_summary", "")
        self.assertIn("syndication partner", summary.lower(),
                      "Research should mention most valuable syndication partner")

    def test_research_atlantic_has_news_plus_source(self):
        """Research file must have apple_news_plus_source."""
        pubs = self.research.get("publications", {})
        atlantic = pubs.get("atlantic", {})
        self.assertIn("apple_news_plus_source", atlantic,
                      "Research should have apple_news_plus_source")

    def test_research_atlantic_asymmetry_mentions_dual(self):
        """Atlantic asymmetry verdict should mention dual Apple financial link."""
        pubs = self.research.get("publications", {})
        atlantic = pubs.get("atlantic", {})
        verdict = atlantic.get("asymmetry_verdict", "")
        self.assertTrue(
            "second" in verdict.lower() or "dual" in verdict.lower() or
            "News+" in verdict,
            "Asymmetry verdict should mention second/dual Apple relationship"
        )


class TestAtlanticFinancialVectorCount(unittest.TestCase):
    """The Atlantic now has 5 unique financial vectors vs 0 for Meta."""

    @classmethod
    def setUpClass(cls):
        cls.atlantic = load_yaml("atlantic.yaml")

    def test_meta_still_zero(self):
        """Atlantic-Meta should still be 'none' / $0."""
        cr = self.atlantic.get("competitor_relationships", {})
        meta = cr.get("meta", {})
        self.assertEqual(meta.get("financial_tie"), "none")
        self.assertEqual(meta.get("estimated_value"), "$0")

    def test_at_least_three_non_meta_relationships(self):
        """Atlantic should have at least 3 non-Meta financial relationships."""
        cr = self.atlantic.get("competitor_relationships", {})
        non_none = sum(1 for entity, rel in cr.items()
                       if isinstance(rel, dict) and
                       rel.get("financial_tie") not in ("none", None) and
                       entity != "meta")
        self.assertGreaterEqual(non_none, 3,
                                f"Expected at least 3 non-Meta relationships, got {non_none}")


class TestUpdatedTimestamp(unittest.TestCase):
    """Research file should have updated timestamp."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml("competitor-coverage-research.yaml")

    def test_last_updated_is_aug_5_noon(self):
        """Last updated should be Aug 5, 2026 noon."""
        ts = self.research.get("aggregate_findings", {}).get("last_updated", "")
        self.assertIn("2026-08-05", ts)
        self.assertIn("12:00", ts)


if __name__ == "__main__":
    unittest.main()
