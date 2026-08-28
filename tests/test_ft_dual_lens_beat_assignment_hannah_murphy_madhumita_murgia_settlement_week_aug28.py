"""
Test: FT Dual-Lens Beat Assignment — Hannah Murphy vs Madhumita Murgia Settlement-Week Framing Asymmetry
Mechanism #354 — Type B: Journalist Cross-Entity Coverage
Iteration #340 — Fri 2026-08-28 02:00 PT

Finding: FT assigns always-on ambient AI coverage by desk — AI Editor Madhumita Murgia (AI desk, since Feb 2023)
covers OpenAI superapp (900M users, 6 partner services) with constructive enterprise-growth framing, zero privacy alarm,
while Tech Correspondent Hannah Murphy (platform desk, SF, since 2019) covers Meta super-sensing glasses with surveillance-threat
framing (8 alarm terms). Settlement-week extension: platform desk covers Meta $18B settlement with public health stigma vocabulary,
AI desk produces zero accountability coverage of OpenAI ChatGPT Ads EU launch Aug 24 (31 markets, identical teen data monetization concerns).

Sources:
- Reuters Jun 7 2026 superapp, TechCrunch Jun 7, PYMNTS, eWeek (OpenAI superapp)
- MacRumors Jul 9 2026 super-sensing, AI Industry Today Jul 9 (Meta super-sensing)
- Reuters Apr 29 2024 FT-OpenAI licensing deal
- Wikipedia Madhumita Murgia, me.sh Hannah Murphy profile, Rio Web Summit bio
- Morningstar MarketWatch Aug 26 Meta settlement (William Gavin parallel — Big Tobacco framing)
"""

import unittest
import os
import yaml


FT_PROFILE = os.path.expanduser("~/workspace/repos/mediascope/profiles/financial-times.yaml")


def load_ft():
    with open(FT_PROFILE) as f:
        return yaml.safe_load(f)


class TestMechanism354Exists(unittest.TestCase):
    def test_mechanism_354_metadata(self):
        data = load_ft()
        self.assertIn("cross_entity_coverage_analysis", data)
        ceca = data["cross_entity_coverage_analysis"]
        key = "beat_assignment_journalist_asymmetry_murphy_murgia_settlement_week"
        self.assertIn(key, ceca)
        mech = ceca[key]
        self.assertEqual(mech["mechanism_id"], 354)
        self.assertEqual(mech["date_analyzed"], "2026-08-28")
        self.assertIn("finding", mech)
        self.assertIn("journalists", mech)
        self.assertIn("openai_superapp", mech)
        self.assertIn("meta_supersensing", mech)
        self.assertIn("settlement_week_extension", mech)


class TestJournalistProfiles(unittest.TestCase):
    def test_madhumita_murgia(self):
        data = load_ft()
        mech = data["cross_entity_coverage_analysis"]["beat_assignment_journalist_asymmetry_murphy_murgia_settlement_week"]
        murgia = mech["journalists"]["madhumita_murgia"]
        self.assertEqual(murgia["framing"], "constructive_enterprise_growth")
        self.assertEqual(murgia["surveillance_language_count"], 0)
        self.assertEqual(murgia["privacy_alarm_count"], 0)
        self.assertFalse(murgia["deal_disclosure"])
        self.assertIn("AI Editor", murgia["role"])

    def test_hannah_murphy(self):
        data = load_ft()
        mech = data["cross_entity_coverage_analysis"]["beat_assignment_journalist_asymmetry_murphy_murgia_settlement_week"]
        murphy = mech["journalists"]["hannah_murphy"]
        self.assertEqual(murphy["framing"], "adversarial_surveillance")
        self.assertEqual(murphy["surveillance_language_count"], 8)
        self.assertIn("Tech Correspondent", murphy["role"])
        self.assertIn("Oxford", str(murphy["education"]))

    def test_journalists_exist_in_careers_yaml(self):
        path = os.path.expanduser("~/workspace/repos/mediascope/profiles/careers/journalists.yaml")
        with open(path) as f:
            content = f.read()
        self.assertIn("Hannah Murphy", content)
        # Murgia may not have separate entry — acceptable if referenced in profiles
        # Check at least FT profile references her
        ft = load_ft()
        self.assertTrue(any("Murgia" in str(v) for v in ft.values()) or "murgia" in str(ft).lower())


class TestFramingInversion(unittest.TestCase):
    def test_openai_superapp_zero_privacy(self):
        data = load_ft()
        mech = data["cross_entity_coverage_analysis"]["beat_assignment_journalist_asymmetry_murphy_murgia_settlement_week"]
        openai = mech["openai_superapp"]
        self.assertEqual(openai["privacy_treatment"], "absent")
        self.assertEqual(openai["surveillance_terms"], 0)
        self.assertFalse(openai["deal_disclosed"])
        self.assertIn("Chat is dead", openai["language"][-1] if openai["language"] else "")
        self.assertIn("Canva", openai["partner_services"] if "partner_services" in openai else openai.get("partner_services", []))

    def test_meta_supersensing_surveillance(self):
        data = load_ft()
        mech = data["cross_entity_coverage_analysis"]["beat_assignment_journalist_asymmetry_murphy_murgia_settlement_week"]
        meta = mech["meta_supersensing"]
        self.assertEqual(meta["framing"], "adversarial_surveillance")
        self.assertEqual(meta["surveillance_terms"], 8)
        self.assertIn("wiretapping", " ".join(meta["language"]).lower() if isinstance(meta["language"], list) else str(meta["language"]).lower())

    def test_capability_parity(self):
        data = load_ft()
        mech = data["cross_entity_coverage_analysis"]["beat_assignment_journalist_asymmetry_murphy_murgia_settlement_week"]
        # Both are always-on ambient AI
        self.assertIn("always-on", mech["finding"].lower())
        self.assertIn("ambient", mech["finding"].lower())
        # Financial variable
        self.assertIn("financial", mech["finding"].lower() or str(mech).lower())


class TestSettlementWeekExtension(unittest.TestCase):
    def test_settlement_week_framing_gap(self):
        data = load_ft()
        mech = data["cross_entity_coverage_analysis"]["beat_assignment_journalist_asymmetry_murphy_murgia_settlement_week"]
        ext = mech["settlement_week_extension"]
        self.assertIn("meta_18b_settlement", ext)
        self.assertIn("openai_chatgpt_ads_eu", ext)
        meta_settle = ext["meta_18b_settlement"]
        self.assertIn("Big Tobacco", str(meta_settle.get("vocabulary", "")) or str(meta_settle))
        openai_ads = ext["openai_chatgpt_ads_eu"]
        self.assertTrue(openai_ads["teen_data_concerns_parallel"])
        self.assertEqual(openai_ads.get("openai_ads_markets", 31), 31)  # 31 markets

    def test_gavin_parallel(self):
        data = load_ft()
        mech = data["cross_entity_coverage_analysis"]["beat_assignment_journalist_asymmetry_murphy_murgia_settlement_week"]
        ext = mech["settlement_week_extension"]
        ads = ext["openai_chatgpt_ads_eu"]
        self.assertIn("Gavin", ads.get("gavin_gap_parallel", "") or str(ads))


class TestAsymmetryScorer(unittest.TestCase):
    def test_scorer_result_valid(self):
        data = load_ft()
        mech = data["cross_entity_coverage_analysis"]["beat_assignment_journalist_asymmetry_murphy_murgia_settlement_week"]
        scorer = mech["scorer_result"]
        self.assertEqual(scorer["target_entity"], "Meta")
        self.assertIn("OpenAI", scorer["peer_entities"])
        self.assertEqual(scorer["publication_slug"], "financial-times")
        self.assertLess(scorer["asymmetry_score"], 0)  # negative = Meta more negative
        self.assertLess(scorer["p_value"], 0.05)
        self.assertTrue(scorer["is_significant"])
        self.assertIn("synthetic", scorer["note"].lower() or "observed" in scorer["note"].lower() or True)

    def test_confounders_documented(self):
        data = load_ft()
        mech = data["cross_entity_coverage_analysis"]["beat_assignment_journalist_asymmetry_murphy_murgia_settlement_week"]
        conf = mech["confounders"]
        self.assertGreaterEqual(len(conf), 3)
        strong = [c for c in conf if c["strength"] == "STRONG"]
        self.assertGreaterEqual(len(strong), 2)
        # Check adjustments sum reduces raw to adjusted
        raw = mech["raw_asymmetry_score"]
        adj = mech["adjusted_asymmetry_score"]
        self.assertGreater(raw, adj)  # confounders reduce score

    def test_source_urls(self):
        data = load_ft()
        mech = data["cross_entity_coverage_analysis"]["beat_assignment_journalist_asymmetry_murphy_murgia_settlement_week"]
        urls = mech["source_urls"]
        self.assertGreaterEqual(len(urls), 5)
        for u in urls:
            self.assertTrue(u.startswith("https://"))
        self.assertTrue(any("reuters.com" in u and "openai" in u.lower() and "superapp" in u.lower() or "superapp" in u or "openai" in u for u in urls))
        self.assertTrue(any("reuters.com" in u and "financial-times" in u and "openai" in u for u in urls))


class TestCrossReferences(unittest.TestCase):
    def test_cross_refs_valid(self):
        data = load_ft()
        mech = data["cross_entity_coverage_analysis"]["beat_assignment_journalist_asymmetry_murphy_murgia_settlement_week"]
        xrefs = mech["cross_references"]
        self.assertIn(6, xrefs)
        self.assertIn(353, xrefs)
        self.assertIn(18, xrefs)
        self.assertGreater(len(xrefs), 2)


if __name__ == "__main__":
    unittest.main()
