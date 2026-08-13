"""
Test Google Display Ads Deprecation — Publisher Revenue Floor Erosion
Through Platform Default Shift (Mechanism #86).

Google retired standalone Display Ads campaigns (May 26, 2026), shifting
GDN from DEFAULT to OPT-IN within Demand Gen. Combined with Performance
Planner Display removal (Mar 9, 2026), Search auto-GDN removal, and AI
Overviews traffic reduction, this creates a four-vector publisher revenue
erosion that strengthens Google's financial leverage over publishers.

Sources:
- PPC Land: https://ppc.land/googles-display-ads-are-dead-here-is-what-replaces-them-in-2026/
- Search Engine Journal: https://www.searchenginejournal.com/google-is-retiring-standalone-display-campaigns-in-favor-of-demand-gen/575889/
- StrategiQ: https://strategiq.co/hub/googles-most-consequential-month-for-paid-search/
- Alphabet Q2 2026 10-Q: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm
- WARC/Madison & Wall: https://medium.com/@anerluzz/the-ad-market-is-growing-faster-than-ever-but-publisher-revenue-is-declining-heres-why-231db78c529a

Added: 2026-08-13 Type C iteration (Financial Incentive Mapping)
"""

import os
import unittest
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


class TestDisplayDeprecationDocumented(unittest.TestCase):
    """Verify display_ads_deprecation section exists in competitor-entities.yaml Google entity."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_yaml("competitor-entities.yaml")
        cls.google = cls.data.get("entities", {}).get("google", {})
        cls.deprecation = cls.google.get("display_ads_deprecation", {})

    def test_google_entity_exists(self):
        self.assertIn("google", self.data.get("entities", {}))

    def test_display_ads_deprecation_section_exists(self):
        self.assertIn("display_ads_deprecation", self.google)

    def test_deprecation_section_is_dict(self):
        self.assertIsInstance(self.deprecation, dict)

    def test_deprecation_has_announcement_date(self):
        self.assertIn("announcement_date", self.deprecation)

    def test_deprecation_has_structural_change(self):
        self.assertIn("structural_change", self.deprecation)

    def test_deprecation_has_publisher_revenue_impact(self):
        self.assertIn("publisher_revenue_impact", self.deprecation)


class TestStructuralChange(unittest.TestCase):
    """Verify announcement_date, migration_tool_start, full_migration_deadline."""

    @classmethod
    def setUpClass(cls):
        data = load_yaml("competitor-entities.yaml")
        cls.deprecation = data.get("entities", {}).get("google", {}).get("display_ads_deprecation", {})

    def test_announcement_date_is_2026_05_26(self):
        self.assertEqual(self.deprecation.get("announcement_date"), "2026-05-26")

    def test_migration_tool_start_is_2026_06_01(self):
        self.assertEqual(self.deprecation.get("migration_tool_start"), "2026-06-01")

    def test_full_migration_deadline_is_2027(self):
        self.assertEqual(self.deprecation.get("full_migration_deadline"), "2027")

    def test_structural_change_mentions_demand_gen(self):
        text = self.deprecation.get("structural_change", "")
        self.assertIn("Demand Gen", text)

    def test_structural_change_mentions_gdn(self):
        text = self.deprecation.get("structural_change", "")
        self.assertIn("GDN", text)

    def test_structural_change_mentions_opt_in(self):
        text = self.deprecation.get("structural_change", "")
        self.assertIn("OPT-IN", text)

    def test_publisher_revenue_impact_mentions_adsense(self):
        text = self.deprecation.get("publisher_revenue_impact", "")
        self.assertIn("AdSense", text)


class TestQuantifiedShift(unittest.TestCase):
    """Verify all network revenue figures (Q2 2025, Q1 2026, Q2 2026), share percentages."""

    @classmethod
    def setUpClass(cls):
        data = load_yaml("competitor-entities.yaml")
        cls.shift = data.get("entities", {}).get("google", {}).get("display_ads_deprecation", {}).get("quantified_shift", {})

    def test_q2_2025_network_b(self):
        self.assertAlmostEqual(self.shift.get("q2_2025_network_b"), 7.354)

    def test_q1_2026_network_b(self):
        self.assertAlmostEqual(self.shift.get("q1_2026_network_b"), 6.97)

    def test_q2_2026_network_b(self):
        self.assertAlmostEqual(self.shift.get("q2_2026_network_b"), 7.303)

    def test_q2_2025_network_share_pct(self):
        self.assertAlmostEqual(self.shift.get("q2_2025_network_share_pct"), 10.3)

    def test_q2_2026_network_share_pct(self):
        self.assertAlmostEqual(self.shift.get("q2_2026_network_share_pct"), 8.9)

    def test_share_decline_pp(self):
        self.assertAlmostEqual(self.shift.get("share_decline_pp"), 1.4)

    def test_implied_quarterly_loss_b(self):
        self.assertAlmostEqual(self.shift.get("implied_quarterly_loss_b"), 1.14)

    def test_implied_quarterly_loss_note_exists(self):
        self.assertIn("implied_quarterly_loss_note", self.shift)

    def test_implied_quarterly_loss_note_mentions_shortfall(self):
        text = self.shift.get("implied_quarterly_loss_note", "")
        self.assertIn("shortfall", text)


class TestSupportingProductDecisions(unittest.TestCase):
    """Verify 3 supporting product decisions documented."""

    @classmethod
    def setUpClass(cls):
        data = load_yaml("competitor-entities.yaml")
        cls.decisions = data.get("entities", {}).get("google", {}).get("display_ads_deprecation", {}).get("supporting_product_decisions", [])

    def test_three_product_decisions_exist(self):
        self.assertEqual(len(self.decisions), 3)

    def test_performance_planner_decision(self):
        actions = [d.get("action", "") for d in self.decisions]
        self.assertTrue(any("Performance Planner" in a for a in actions))

    def test_search_gdn_decision(self):
        actions = [d.get("action", "") for d in self.decisions]
        self.assertTrue(any("GDN" in a for a in actions))

    def test_youtube_video_action_decision(self):
        actions = [d.get("action", "") for d in self.decisions]
        self.assertTrue(any("YouTube" in a or "Video Action" in a for a in actions))

    def test_each_decision_has_date(self):
        for d in self.decisions:
            self.assertIn("date", d, f"Missing date in decision: {d.get('action', 'unknown')}")

    def test_each_decision_has_effect(self):
        for d in self.decisions:
            self.assertIn("effect", d, f"Missing effect in decision: {d.get('action', 'unknown')}")


class TestMechanism86Exists(unittest.TestCase):
    """Verify mechanism #86 in competitor-coverage-research.yaml."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_yaml("competitor-coverage-research.yaml")
        findings = cls.data.get("cross_publication_findings", {})
        if not findings:
            findings = cls.data.get("aggregate_findings", {})
        cls.mechanism = None
        for key, val in findings.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 86:
                cls.mechanism = val
                cls.mechanism_key = key
                break

    def test_mechanism_86_found(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #86 not found in cross_publication_findings")

    def test_mechanism_id_is_86(self):
        self.assertEqual(self.mechanism.get("mechanism_id"), 86)

    def test_mechanism_name_contains_display(self):
        name = self.mechanism.get("mechanism_name", "")
        self.assertIn("Display", name)

    def test_finding_type_is_financial(self):
        self.assertEqual(self.mechanism.get("finding_type"), "financial_incentive_mapping")

    def test_rotation_type_is_c(self):
        self.assertEqual(self.mechanism.get("rotation_type"), "C")

    def test_discovery_date(self):
        self.assertEqual(self.mechanism.get("discovery_date"), "2026-08-13")

    def test_date_added(self):
        self.assertEqual(self.mechanism.get("date_added"), "2026-08-13")

    def test_finding_summary_exists(self):
        self.assertIn("finding_summary", self.mechanism)

    def test_finding_summary_not_empty(self):
        summary = self.mechanism.get("finding_summary", "")
        self.assertTrue(len(summary) > 100, "finding_summary too short")

    def test_test_count_is_76(self):
        self.assertEqual(self.mechanism.get("test_count"), 76)

    def test_test_file_correct(self):
        self.assertEqual(
            self.mechanism.get("test_file"),
            "tests/test_google_display_deprecation_publisher_revenue_floor_erosion_aug13.py",
        )


class TestDistinctions(unittest.TestCase):
    """Verify distinction fields exist and reference correct mechanisms."""

    @classmethod
    def setUpClass(cls):
        data = load_yaml("competitor-coverage-research.yaml")
        findings = data.get("cross_publication_findings", {})
        if not findings:
            findings = data.get("aggregate_findings", {})
        cls.mechanism = None
        for key, val in findings.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 86:
                cls.mechanism = val
                break

    def test_distinction_from_47_exists(self):
        self.assertIn("distinction_from_47", self.mechanism)

    def test_distinction_from_82_exists(self):
        self.assertIn("distinction_from_82", self.mechanism)

    def test_distinction_from_showcase_exists(self):
        self.assertIn("distinction_from_showcase_coercive_cycle", self.mechanism)

    def test_distinction_47_mentions_meta(self):
        text = self.mechanism.get("distinction_from_47", "")
        self.assertIn("Meta", text)

    def test_distinction_82_mentions_spiral(self):
        text = self.mechanism.get("distinction_from_82", "")
        self.assertIn("spiral", text)

    def test_distinction_showcase_mentions_payments(self):
        text = self.mechanism.get("distinction_from_showcase_coercive_cycle", "")
        self.assertIn("PAYMENT", text) or self.assertIn("Showcase", text)


class TestConfoundingFactors(unittest.TestCase):
    """Verify >= 6 confounding factors with STRONG/MODERATE/WEAK ratings."""

    @classmethod
    def setUpClass(cls):
        data = load_yaml("competitor-coverage-research.yaml")
        findings = data.get("cross_publication_findings", {})
        if not findings:
            findings = data.get("aggregate_findings", {})
        cls.mechanism = None
        for key, val in findings.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 86:
                cls.mechanism = val
                break
        cls.factors = cls.mechanism.get("confounding_factors", []) if cls.mechanism else []

    def test_at_least_6_confounding_factors(self):
        self.assertGreaterEqual(len(self.factors), 6)

    def test_each_factor_has_rating(self):
        for f in self.factors:
            self.assertIn("rating", f, f"Missing rating in factor: {f.get('factor', 'unknown')[:50]}")

    def test_each_factor_has_factor_text(self):
        for f in self.factors:
            self.assertIn("factor", f)

    def test_valid_ratings(self):
        valid = {"STRONG", "MODERATE", "WEAK"}
        for f in self.factors:
            self.assertIn(f.get("rating"), valid, f"Invalid rating: {f.get('rating')}")

    def test_has_strong_rating(self):
        ratings = [f.get("rating") for f in self.factors]
        self.assertIn("STRONG", ratings)

    def test_has_moderate_rating(self):
        ratings = [f.get("rating") for f in self.factors]
        self.assertIn("MODERATE", ratings)

    def test_has_weak_rating(self):
        ratings = [f.get("rating") for f in self.factors]
        self.assertIn("WEAK", ratings)


class TestTestablePredictions(unittest.TestCase):
    """Verify >= 4 specific, falsifiable predictions."""

    @classmethod
    def setUpClass(cls):
        data = load_yaml("competitor-coverage-research.yaml")
        findings = data.get("cross_publication_findings", {})
        if not findings:
            findings = data.get("aggregate_findings", {})
        cls.mechanism = None
        for key, val in findings.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 86:
                cls.mechanism = val
                break
        cls.predictions = cls.mechanism.get("testable_predictions", []) if cls.mechanism else []

    def test_at_least_4_predictions(self):
        self.assertGreaterEqual(len(self.predictions), 4)

    def test_prediction_network_revenue_below_7b(self):
        texts = " ".join(self.predictions)
        self.assertIn("$7B", texts)

    def test_prediction_publisher_share_below_8_pct(self):
        texts = " ".join(self.predictions)
        self.assertIn("8%", texts)

    def test_prediction_mentions_adversarial(self):
        texts = " ".join(self.predictions)
        self.assertIn("adversarial", texts)

    def test_prediction_mentions_conde_nast(self):
        texts = " ".join(self.predictions)
        self.assertIn("Cond", texts)


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to mechanisms #82, #47, #76."""

    @classmethod
    def setUpClass(cls):
        data = load_yaml("competitor-coverage-research.yaml")
        findings = data.get("cross_publication_findings", {})
        if not findings:
            findings = data.get("aggregate_findings", {})
        cls.mechanism = None
        for key, val in findings.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 86:
                cls.mechanism = val
                break
        cls.cross_refs = cls.mechanism.get("cross_references", []) if cls.mechanism else []

    def test_at_least_3_cross_references(self):
        self.assertGreaterEqual(len(self.cross_refs), 3)

    def test_cross_ref_mechanism_82(self):
        ids = [cr.get("mechanism_id") for cr in self.cross_refs]
        self.assertIn(82, ids)

    def test_cross_ref_mechanism_47(self):
        ids = [cr.get("mechanism_id") for cr in self.cross_refs]
        self.assertIn(47, ids)

    def test_cross_ref_mechanism_76(self):
        ids = [cr.get("mechanism_id") for cr in self.cross_refs]
        self.assertIn(76, ids)

    def test_each_cross_ref_has_name(self):
        for cr in self.cross_refs:
            self.assertIn("name", cr, f"Missing name for cross_ref mechanism_id {cr.get('mechanism_id')}")

    def test_each_cross_ref_has_connection(self):
        for cr in self.cross_refs:
            self.assertIn("connection", cr, f"Missing connection for cross_ref mechanism_id {cr.get('mechanism_id')}")


class TestSourceUrls(unittest.TestCase):
    """Verify >= 4 source URLs including SEC filing."""

    @classmethod
    def setUpClass(cls):
        data = load_yaml("competitor-coverage-research.yaml")
        findings = data.get("cross_publication_findings", {})
        if not findings:
            findings = data.get("aggregate_findings", {})
        cls.mechanism = None
        for key, val in findings.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 86:
                cls.mechanism = val
                break
        cls.urls = cls.mechanism.get("source_urls", []) if cls.mechanism else []

    def test_at_least_4_source_urls(self):
        self.assertGreaterEqual(len(self.urls), 4)

    def test_sec_filing_url_present(self):
        sec_urls = [u for u in self.urls if "sec.gov" in u]
        self.assertTrue(len(sec_urls) >= 1, "No SEC filing URL found")

    def test_ppc_land_url_present(self):
        ppc_urls = [u for u in self.urls if "ppc.land" in u]
        self.assertTrue(len(ppc_urls) >= 1, "No PPC Land URL found")

    def test_search_engine_journal_url_present(self):
        sej_urls = [u for u in self.urls if "searchenginejournal.com" in u]
        self.assertTrue(len(sej_urls) >= 1, "No SEJ URL found")

    def test_all_urls_are_https(self):
        for u in self.urls:
            self.assertTrue(u.startswith("https://"), f"URL not HTTPS: {u}")


class TestFourVectorErosion(unittest.TestCase):
    """Verify the finding_summary references all 4 vectors."""

    @classmethod
    def setUpClass(cls):
        data = load_yaml("competitor-coverage-research.yaml")
        findings = data.get("cross_publication_findings", {})
        if not findings:
            findings = data.get("aggregate_findings", {})
        cls.mechanism = None
        for key, val in findings.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 86:
                cls.mechanism = val
                break
        cls.summary = cls.mechanism.get("finding_summary", "") if cls.mechanism else ""

    def test_search_traffic_vector(self):
        self.assertIn("search traffic vector", self.summary)

    def test_display_budget_vector(self):
        normalized = self.summary.replace("\n", " ")
        self.assertIn("display budget vector", normalized)

    def test_planning_infrastructure_vector(self):
        self.assertIn("planning infrastructure vector", self.summary)

    def test_search_campaign_vector(self):
        self.assertIn("search campaign vector", self.summary)

    def test_four_vector_label(self):
        self.assertIn("FOUR-VECTOR", self.summary)

    def test_ai_overviews_referenced(self):
        self.assertIn("AI Overviews", self.summary)

    def test_performance_planner_referenced(self):
        self.assertIn("Performance Planner", self.summary)

    def test_demand_gen_referenced(self):
        self.assertIn("Demand Gen", self.summary)


if __name__ == "__main__":
    unittest.main()
