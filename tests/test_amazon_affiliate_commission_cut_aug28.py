"""
Test: Amazon Associates Affiliate Commission Cut Aug 28 — Mechanism #367
Iteration #356 — Fri 2026-08-28 20:00 PT — Type C Financial Incentive Mapping

Finding: Amazon quietly restructured Associates program: slashed commissions up to 50% (10%→4-5%), eliminated milestone tiers + YoY bonuses, degraded reporting (tracking-ID 1→4 sales, SKU/ASIN→category-only, revoked premium APIs), 20% cost-cut directive, rollout Asia-Pacific late 2025 → US Mar 9 2026, 7 publishers confirmed to Adweek, deal-site publisher -50% 2026 forecast, Recurrent Ventures CEO quote re Google AI Overviews top funnel + Amazon bottom funnel double squeeze, Amazon statement tiny fraction highly competitive, layoffs thousands early 2026 Associates team among cuts, strategic shift toward creators/influencers more incremental, some publishers exited not strategic, diversification to Walmart/Target/Best Buy/Wayfair/eBay, quote short-term bad medium-term excellent forced diversification overdue. 4th financial channel beyond advertising/AWS/dual-lab-equity. Publications with heavy affiliate ops (NYT/Wirecutter, Condé Nast, Hearst, Vox, Ziff Davis) face amplified dependency.

Sources:
- https://www.adweek.com/media/amazon-associates-affiliate-rate-cuts-publishers/
"""

import unittest
import os
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
NYTIMES_PROFILE = os.path.join(REPO_ROOT, "profiles", "nytimes.yaml")

def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)

def get_mech_367():
    data = load_yaml(COMPETITOR_ENTITIES)
    entities = data.get("entities") or data.get("competitor_entities")
    assert entities is not None, "Missing entities top-level"
    amazon = entities.get("amazon")
    assert amazon is not None, "Missing amazon entity"
    # mechanism keyed as amazon_affiliate_commission_cut_aug28
    mech = amazon.get("amazon_affiliate_commission_cut_aug28")
    assert mech is not None, "Missing mechanism 367 amazon_affiliate_commission_cut_aug28"
    return mech

def get_mech_96():
    data = load_yaml(COMPETITOR_ENTITIES)
    entities = data.get("entities") or data.get("competitor_entities")
    amazon = entities.get("amazon")  # 96 lives under amazon? Actually under litigation? Check top-level scan
    # 96 is under litigation_coverage_analysis nested under some entity - need full scan
    # Search all entities for mechanism_id 96
    for ent_name, ent_data in entities.items():
        if not isinstance(ent_data, dict):
            continue
        for k, v in ent_data.items():
            if isinstance(v, dict) and v.get("mechanism_id") == 96:
                return v
            # also nested one level deeper?
            if isinstance(v, dict):
                for kk, vv in v.items():
                    if isinstance(vv, dict) and vv.get("mechanism_id") == 96:
                        return vv
    raise AssertionError("Missing mechanism 96")

class TestMechanism367Exists(unittest.TestCase):
    def test_mechanism_367_exists(self):
        mech = get_mech_367()
        self.assertEqual(mech["mechanism_id"], 367)
        self.assertEqual(mech["date_analyzed"], "2026-08-28")
        self.assertEqual(mech["iteration"], 356)
        self.assertIn("financial_incentive", mech["type"])

    def test_mechanism_367_has_required_keys(self):
        mech = get_mech_367()
        for key in ["type_c_focus", "overview", "financial_channels", "coverage_prediction", "confounding_factors", "cautious_language", "source_urls"]:
            self.assertIn(key, mech, f"Missing key {key}")

    def test_mechanism_367_source_url_adweek(self):
        mech = get_mech_367()
        urls = mech.get("source_urls", [])
        self.assertTrue(any("adweek.com" in u for u in urls), "Missing Adweek source URL")

    def test_mechanism_367_commission_cut_details(self):
        mech = get_mech_367()
        overview = mech.get("overview", "")
        self.assertIn("50%", overview)
        self.assertIn("Associates", overview)
        fc = mech.get("financial_channels", {})
        self.assertIn("channel_4_affiliate", fc)
        ch4 = fc["channel_4_affiliate"]
        self.assertEqual(ch4["commission_cut_pct"], "up to 50" if isinstance(ch4["commission_cut_pct"], str) else ch4["commission_cut_pct"] in ["up to 50", 50])
        # check reporting degradation preserved
        self.assertIn("reporting_degradation", ch4)

    def test_mechanism_367_no_synthetic_significance_claim(self):
        mech = get_mech_367()
        text = str(mech)
        # Must not claim empirical p-values as fact
        self.assertNotIn("p < 0.05 empirical", text)
        # cautious_language must mention synthetic arrays cannot establish significance OR similar
        cautious = mech.get("cautious_language", "")
        self.assertIn("Synthetic", cautious)
        self.assertIn("cannot", cautious.lower())

class TestMechanism96Correction(unittest.TestCase):
    def test_mech_96_corrected_wired_count_1(self):
        mech = get_mech_96()
        # Should have correction
        self.assertIn("article_count", str(mech))
        wired = mech.get("wired_coverage", {})
        if wired:
            self.assertEqual(wired.get("article_count"), 1, "WIRED count should be corrected to 1, not 0")
        # finding should mention corrected 6 vs 1
        finding = mech.get("finding", "")
        self.assertIn("6", finding)
        self.assertIn("1", finding)

    def test_mech_96_correction_note_present(self):
        mech = get_mech_96()
        # must have date_corrected or correction_note
        has_correction = "date_corrected" in mech or "correction_note" in mech or "correction" in mech
        self.assertTrue(has_correction, "Mechanism 96 must have correction metadata")

class TestNYTimesAffiliateExposure(unittest.TestCase):
    def test_nytimes_has_affiliate_cut(self):
        data = load_yaml(NYTIMES_PROFILE)
        self.assertIn("amazon_affiliate_commission_cuts_2026", data, "NYT profile missing affiliate cut section")

    def test_nytimes_affiliate_source_url(self):
        data = load_yaml(NYTIMES_PROFILE)
        cut = data.get("amazon_affiliate_commission_cuts_2026", {})
        url = cut.get("source_url", "")
        self.assertIn("adweek.com", url)

class TestYamlHealth(unittest.TestCase):
    def test_competitor_entities_yaml_parseable(self):
        data = load_yaml(COMPETITOR_ENTITIES)
        self.assertIsInstance(data, dict)

    def test_no_duplicate_mechanism_ids_367(self):
        data = load_yaml(COMPETITOR_ENTITIES)
        entities = data.get("entities") or data.get("competitor_entities")
        ids = []
        def scan(d):
            if isinstance(d, dict):
                if "mechanism_id" in d:
                    ids.append(d["mechanism_id"])
                for v in d.values():
                    scan(v)
            elif isinstance(d, list):
                for item in d:
                    scan(item)
        scan(entities)
        # 367 should appear exactly once
        self.assertEqual(ids.count(367), 1, f"Mechanism 367 appears {ids.count(367)} times, expected 1")

    def test_source_urls_https(self):
        mech = get_mech_367()
        urls = mech.get("source_urls", [])
        self.assertTrue(len(urls) >= 1)
        for u in urls:
            self.assertTrue(u.startswith("https://"), f"URL must be https: {u}")

