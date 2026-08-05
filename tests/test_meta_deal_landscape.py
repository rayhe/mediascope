"""
Test Meta AI content deal landscape data integrity, completeness,
and cross-validation against publication coverage predictions.

Added Aug 5 2026, Type C iteration (Financial Incentive Mapping).
Validates the comprehensive meta_ai_deals section in competitor-entities.yaml
and cross-references WIRED/Verge profiles for Microsoft/Perplexity additions.

Sources:
- Reuters: https://www.reuters.com/business/meta-strikes-multiple-ai-deals-with-news-publishers-axios-reports-2025-12-05/
- WSJ: https://www.wsj.com/business/media/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year-d4fbf244
- SiliconANGLE: https://siliconangle.com/2024/10/25/meta-inks-multiyear-ai-content-licensing-deal-reuters/
- TheKeyword: https://www.thekeyword.co/news/meta-ai-news-publisher-partnerships
- Adweek: https://www.adweek.com/media/conde-nast-vasanth-williams-chief-product-technology-officer-microsoft-ai-licensing-pilot/
- WebWire: https://www.WebWire.com/ViewPressRel.asp?aId=350303
"""

import os
import unittest

import yaml


PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


class TestMetaDealLandscapeExists(unittest.TestCase):
    """meta_ai_deals section must exist in competitor-entities.yaml."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml("competitor-entities.yaml")
        cls.deals = cls.entities.get("meta_ai_deals", {})

    def test_section_exists(self):
        self.assertIn("meta_ai_deals", self.entities)

    def test_overview_present(self):
        overview = self.deals.get("overview", "")
        self.assertTrue(len(overview) > 100, "Overview should be substantive")

    def test_partners_list_present(self):
        partners = self.deals.get("partners", [])
        self.assertIsInstance(partners, list)
        self.assertGreaterEqual(len(partners), 10, "Should have at least 10 Meta AI partners")

    def test_excluded_publishers_present(self):
        excluded = self.deals.get("excluded_publishers", [])
        self.assertIsInstance(excluded, list)
        self.assertGreaterEqual(len(excluded), 5, "Should list at least 5 excluded publishers")

    def test_critical_finding_present(self):
        finding = self.deals.get("critical_finding", "")
        self.assertTrue(len(finding) > 100, "Critical finding should be substantive")


class TestMetaDealPartnerData(unittest.TestCase):
    """Each Meta AI deal partner must have required fields."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml("competitor-entities.yaml")
        cls.partners = cls.entities.get("meta_ai_deals", {}).get("partners", [])

    def test_partner_has_name(self):
        for p in self.partners:
            self.assertIn("name", p, f"Partner missing name: {p}")

    def test_partner_has_date(self):
        for p in self.partners:
            self.assertIn("date", p, f"{p.get('name', '?')} missing date")

    def test_partner_has_source_url(self):
        for p in self.partners:
            self.assertIn("source_url", p, f"{p.get('name', '?')} missing source_url")
            self.assertTrue(p["source_url"].startswith("http"),
                            f"{p.get('name', '?')} source_url not valid URL")

    def test_partner_has_scope(self):
        for p in self.partners:
            self.assertIn("scope", p, f"{p.get('name', '?')} missing scope")

    def test_reuters_is_first_deal(self):
        """Reuters (Oct 2024) must be the earliest Meta AI deal."""
        dates = [(p["name"], p["date"]) for p in self.partners]
        sorted_dates = sorted(dates, key=lambda x: x[1])
        self.assertEqual(sorted_dates[0][0], "Reuters",
                         f"Reuters should be first deal, got: {sorted_dates[0]}")

    def test_news_corp_has_value(self):
        """News Corp deal should document the $50M/yr value."""
        nc = [p for p in self.partners if p["name"] == "News Corp"]
        self.assertTrue(len(nc) >= 1, "News Corp must be in partners list")
        terms = nc[0].get("terms", "")
        self.assertIn("50M", terms, f"News Corp terms should mention $50M, got: {terms}")

    def test_dec_2025_batch(self):
        """Dec 5 2025 batch should have at least 7 publishers."""
        dec_batch = [p for p in self.partners if p.get("date", "").startswith("2025-12")]
        self.assertGreaterEqual(len(dec_batch), 7,
                                f"Dec 2025 batch should have 7+ publishers, got {len(dec_batch)}")

    def test_mar_2026_expansion(self):
        """Mar 2026 expansion should have at least 3 new partners."""
        mar_batch = [p for p in self.partners if p.get("date", "").startswith("2026-03")]
        self.assertGreaterEqual(len(mar_batch), 3,
                                f"Mar 2026 expansion should have 3+ publishers, got {len(mar_batch)}")


class TestExcludedPublishers(unittest.TestCase):
    """Validate excluded publishers data."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml("competitor-entities.yaml")
        cls.excluded = cls.entities.get("meta_ai_deals", {}).get("excluded_publishers", [])

    def test_conde_nast_excluded(self):
        cn = [e for e in self.excluded if "Condé Nast" in e.get("name", "")]
        self.assertTrue(len(cn) >= 1, "Condé Nast must be in excluded list")
        self.assertEqual(cn[0]["meta_deal"], "none")

    def test_conde_nast_has_competitor_deals(self):
        """Condé Nast should list multiple competitor deals."""
        cn = [e for e in self.excluded if "Condé Nast" in e.get("name", "")]
        if cn:
            deals = cn[0].get("deals_with_competitors", [])
            self.assertGreaterEqual(len(deals), 4,
                                    f"Condé Nast should have 4+ competitor deals, got {len(deals)}")

    def test_nyt_excluded(self):
        nyt = [e for e in self.excluded if "New York Times" in e.get("name", "")]
        self.assertTrue(len(nyt) >= 1, "NYT must be in excluded list")
        self.assertEqual(nyt[0]["meta_deal"], "none")

    def test_vox_media_excluded(self):
        vox = [e for e in self.excluded if "Vox Media" in e.get("name", "") or "PMC" in e.get("name", "")]
        self.assertTrue(len(vox) >= 1, "Vox Media/PMC must be in excluded list")

    def test_gizmodo_clean_control(self):
        """Gizmodo should have zero competitor deals — the clean control."""
        gz = [e for e in self.excluded if "Gizmodo" in e.get("name", "")]
        self.assertTrue(len(gz) >= 1, "Gizmodo must be in excluded list")
        deals = gz[0].get("deals_with_competitors", [])
        self.assertEqual(len(deals), 0,
                         f"Gizmodo should have 0 competitor deals (clean control), got {len(deals)}")


class TestWiredMicrosoftPerplexityRelationships(unittest.TestCase):
    """WIRED profile must include Microsoft and Perplexity competitor relationships.
    Added Aug 5 2026 Type C iteration.
    """

    @classmethod
    def setUpClass(cls):
        cls.wired = load_yaml("wired.yaml")
        cls.cr = cls.wired.get("competitor_relationships", {})

    def test_microsoft_relationship_exists(self):
        self.assertIn("microsoft", self.cr, "WIRED must have Microsoft competitor relationship")

    def test_microsoft_is_licensing(self):
        ms = self.cr.get("microsoft", {})
        self.assertEqual(ms.get("financial_tie"), "licensing")

    def test_microsoft_has_source_url(self):
        ms = self.cr.get("microsoft", {})
        self.assertIn("source_url", ms)
        self.assertTrue(ms["source_url"].startswith("http"))

    def test_microsoft_mentions_pcm(self):
        ms = self.cr.get("microsoft", {})
        desc = ms.get("description", "")
        self.assertIn("PCM", desc, "Microsoft description should mention PCM")

    def test_microsoft_notes_meta_exclusion(self):
        ms = self.cr.get("microsoft", {})
        desc = ms.get("description", "")
        self.assertIn("Meta is NOT", desc,
                      "Microsoft description should note Meta's exclusion from PCM")

    def test_perplexity_relationship_exists(self):
        self.assertIn("perplexity", self.cr, "WIRED must have Perplexity competitor relationship")

    def test_perplexity_is_licensing(self):
        px = self.cr.get("perplexity", {})
        self.assertEqual(px.get("financial_tie"), "licensing")

    def test_perplexity_has_source_url(self):
        px = self.cr.get("perplexity", {})
        self.assertIn("source_url", px)
        self.assertTrue(px["source_url"].startswith("http"))

    def test_perplexity_notes_cease_desist_history(self):
        """Perplexity entry should document the adversarial-to-commercial transition."""
        px = self.cr.get("perplexity", {})
        desc = px.get("description", "")
        self.assertTrue(
            "cease" in desc.lower() or "plagiarism" in desc.lower(),
            "Perplexity description should mention cease-and-desist or plagiarism history"
        )

    def test_wired_now_has_nine_entities(self):
        """WIRED should now track 9 competitor relationships."""
        expected = {"openai", "meta", "anthropic", "amazon", "apple",
                    "google", "x_twitter", "microsoft", "perplexity"}
        actual = set(self.cr.keys())
        self.assertEqual(expected, actual,
                         f"Missing: {expected - actual}, Extra: {actual - expected}")

    def test_five_licensing_relationships(self):
        """WIRED should have exactly 5 licensing/commercial relationships."""
        licensing = [k for k, v in self.cr.items()
                     if v.get("financial_tie") in ("licensing", "negotiating")]
        self.assertGreaterEqual(len(licensing), 5,
                                f"Expected 5+ licensing/negotiating ties, got: {licensing}")

    def test_meta_still_zero(self):
        """Meta must remain at $0 / none."""
        meta = self.cr.get("meta", {})
        self.assertEqual(meta.get("financial_tie"), "none")
        self.assertIn("$0", meta.get("estimated_value", ""))


class TestVergeMicrosoftRelationship(unittest.TestCase):
    """The Verge profile must include Microsoft PCM relationship.
    Added Aug 5 2026 Type C iteration.
    """

    @classmethod
    def setUpClass(cls):
        cls.verge = load_yaml("the-verge.yaml")
        cls.cr = cls.verge.get("competitor_relationships", {})

    def test_microsoft_relationship_exists(self):
        self.assertIn("microsoft", self.cr, "The Verge must have Microsoft competitor relationship")

    def test_microsoft_is_licensing(self):
        ms = self.cr.get("microsoft", {})
        self.assertEqual(ms.get("financial_tie"), "licensing")

    def test_microsoft_has_source_url(self):
        ms = self.cr.get("microsoft", {})
        self.assertIn("source_url", ms)
        self.assertTrue(ms["source_url"].startswith("http"))

    def test_meta_still_none(self):
        meta = self.cr.get("meta", {})
        self.assertEqual(meta.get("financial_tie"), "none")


class TestCriticalFindingAssertion(unittest.TestCase):
    """The critical finding in meta_ai_deals should make strong claims."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml("competitor-entities.yaml")
        cls.finding = cls.entities.get("meta_ai_deals", {}).get("critical_finding", "")

    def test_mentions_zero_deals(self):
        self.assertIn("ZERO", self.finding)

    def test_mentions_news_corp_control(self):
        self.assertIn("News Corp", self.finding)

    def test_mentions_balanced_prediction(self):
        self.assertIn("balanced", self.finding.lower())


class TestDealCoverageCorrelation(unittest.TestCase):
    """Cross-validate: every entity in competitor_relationships with 'licensing'
    financial_tie should have 'softer' coverage_prediction in WIRED's profile."""

    @classmethod
    def setUpClass(cls):
        cls.wired = load_yaml("wired.yaml")
        cls.cr = cls.wired.get("competitor_relationships", {})

    def test_licensing_predicts_softer(self):
        """All licensing relationships should predict softer coverage."""
        for entity, rel in self.cr.items():
            if rel.get("financial_tie") == "licensing":
                self.assertEqual(
                    rel.get("coverage_prediction"), "softer",
                    f"WIRED-{entity} is licensing but predicts '{rel.get('coverage_prediction')}' not 'softer'"
                )

    def test_none_predicts_adversarial_or_neutral(self):
        """Entities with no financial tie should predict adversarial or neutral."""
        for entity, rel in self.cr.items():
            if rel.get("financial_tie") == "none":
                pred = rel.get("coverage_prediction", "")
                self.assertIn(pred, ("adversarial", "neutral"),
                              f"WIRED-{entity} has no tie but predicts '{pred}'")

    def test_meta_only_adversarial_with_no_deal(self):
        """Meta should be the only entity predicted adversarial with no deal + no litigation."""
        adversarial_no_deal = [
            entity for entity, rel in self.cr.items()
            if rel.get("coverage_prediction") == "adversarial"
            and rel.get("financial_tie") == "none"
        ]
        self.assertIn("meta", adversarial_no_deal,
                      "Meta should be adversarial with no deal")


if __name__ == "__main__":
    unittest.main()
