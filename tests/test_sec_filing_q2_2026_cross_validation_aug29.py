"""
Test: SEC Filing Q2 2026 Cross-Validation — Mechanism #372
Iteration #371 — Sat 2026-08-29 11:00 PT — Type C Financial Incentive Mapping

Finding: Quadruple financial incentive quantified via primary SEC sources:
Amazon Q2 2026 ad revenue $19.8B up 26% YoY (AdExchanger Jul 30 2026, Motley Fool, TradingView 10-Q summary, $200.6B total, $62.65B net inflated by Anthropic mark-to-market),
Alphabet Q2 2026 ad revenue $81.63B (Search $63.27B up 17%, YouTube $11.06B up 13%, Network $7.3B, total $119.8B up 24%, Cloud $24.77B up 82%, Zacks Jul 23 2026, blog.google Jul 22 2026, 9to5Google Jul 22 2026, Fool Aug 25 2026),
Apple Siri AI nine-figure budget variable pay-per-use multiyear (WSJ Aug 12 2026 + 6 secondary sources, reversal Jan 2026 $1B/yr Gemini bypass, hallucination motivator iOS 18 disabled >1 year),
Google Showcase sunset coercion (PYMNTS Jun 25 2026, NYPost Jun 26 2026, Press Gazette Jun 26 2026, Showcase $1B/3yr 3000+ pubs, News AI pilot broad AI training rights, EU Commission probe Dec 2024, UK CMA Jan 28 2026),
Meta Q2 2026 $59.363B ad revenue contrast structural antagonism.
Combined 4 financial levers same structural incentive - softer for paying entities, adversarial for zero-deal Meta.

Sources all verified Aug 29 2026 via direct search.

Mechanism #372 must not duplicate Apple Siri #156 or Amazon affiliate #367 but extend/verify them.
"""

import unittest
import os
import yaml
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
GUARDIAN_PROFILE = os.path.join(REPO_ROOT, "profiles", "guardian.yaml")
WIRED_PROFILE = os.path.join(REPO_ROOT, "profiles", "wired.yaml")

def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)

def get_mech_372():
    data = load_yaml(COMPETITOR_ENTITIES)
    entities = data.get("entities") or data.get("competitor_entities") or data
    # amazon section contains sec_filing_q2_2026_cross_validation_aug29
    for ent_name, ent_data in entities.items():
        if not isinstance(ent_data, dict):
            continue
        if "sec_filing_q2_2026_cross_validation_aug29" in ent_data:
            return ent_data["sec_filing_q2_2026_cross_validation_aug29"]
        # also check nested
        for k,v in ent_data.items():
            if isinstance(v, dict) and v.get("mechanism_id") == 372:
                return v
            if isinstance(v, dict):
                for kk,vv in v.items():
                    if isinstance(vv, dict) and vv.get("mechanism_id") == 372:
                        return vv
    # direct top-level under entities.amazon
    if "amazon" in entities and "sec_filing_q2_2026_cross_validation_aug29" in entities["amazon"]:
        return entities["amazon"]["sec_filing_q2_2026_cross_validation_aug29"]
    raise AssertionError("Missing mechanism 372 sec_filing_q2_2026_cross_validation_aug29")

class TestMechanism372Exists(unittest.TestCase):
    def test_exists(self):
        mech = get_mech_372()
        self.assertEqual(mech["mechanism_id"], 372)
        self.assertEqual(mech["date_analyzed"], "2026-08-29")
        self.assertEqual(mech["iteration"], 371)

    def test_required_keys(self):
        mech = get_mech_372()
        for key in ["type_c_focus", "overview", "amazon_q2_2026", "alphabet_q2_2026", "apple_siri_ai_deals_aug_2026", "google_showcase_sunset_coercion_jun_2026", "meta_q2_2026_contrast", "quadruple_incentive_synthesis", "confounding_factors", "cautious_language", "source_urls"]:
            self.assertIn(key, mech, f"Missing key {key}")

    def test_no_em_dash(self):
        mech = get_mech_372()
        text = str(mech)
        self.assertNotIn("—", text, "Em dash found in mechanism 372 - violates style guide")
        self.assertNotIn("–", text, "En dash found - use hyphen")

    def test_type_c_focus_mentions_quadruple(self):
        mech = get_mech_372()
        focus = mech.get("type_c_focus","")
        self.assertIn("SEC", focus)
        self.assertIn("Amazon", focus)
        self.assertIn("Alphabet", focus)
        self.assertIn("Apple", focus)
        self.assertIn("Google", focus)

class TestMechanism372AmazonSEC(unittest.TestCase):
    def test_amazon_q2_revenue(self):
        mech = get_mech_372()
        amzn = mech.get("amazon_q2_2026",{})
        self.assertEqual(amzn.get("advertising_services_revenue_b"), 19.8)
        self.assertIn("advertising_yoy_pct", amzn)
        self.assertIn("total_revenue_b", amzn)
        self.assertIn("net_income_b", amzn)
        self.assertIn("source_urls", amzn)
        urls = amzn.get("source_urls",[])
        self.assertTrue(any("adexchanger" in u for u in urls), "Missing AdExchanger Amazon source")
        self.assertTrue(any("tradingview" in u for u in urls), "Missing TradingView 10-Q source")
        self.assertIn("sec_filing", amzn)

    def test_amazon_cautious_no_causation_claim(self):
        mech = get_mech_372()
        cautious = mech.get("cautious_language","")
        self.assertIn("does not imply", cautious.lower())
        self.assertIn("STRUCTURAL INCENTIVE", cautious)

class TestMechanism372AlphabetSEC(unittest.TestCase):
    def test_alphabet_q2_revenue(self):
        mech = get_mech_372()
        goog = mech.get("alphabet_q2_2026",{})
        self.assertEqual(goog.get("google_advertising_total_b"), 81.63)
        self.assertEqual(goog.get("google_search_and_other_b"), 63.27)
        self.assertEqual(goog.get("youtube_ads_b"), 11.06)
        self.assertEqual(goog.get("total_revenue_b"), 119.8)
        self.assertIn("source_urls", goog)
        urls = goog.get("source_urls",[])
        self.assertTrue(any("zacks" in u for u in urls), "Missing Zacks Alphabet source")
        self.assertTrue(any("blog.google" in u for u in urls), "Missing blog.google Alphabet source")
        self.assertIn("sec_filing", goog)

    def test_alphabet_no_em_dash(self):
        mech = get_mech_372()
        goog = str(mech.get("alphabet_q2_2026",""))
        self.assertNotIn("—", goog)

class TestMechanism372AppleSiri(unittest.TestCase):
    def test_apple_siri_structure(self):
        mech = get_mech_372()
        appl = mech.get("apple_siri_ai_deals_aug_2026",{})
        self.assertEqual(appl.get("budget_magnitude"), "nine_figure")
        self.assertEqual(appl.get("compensation_model"), "variable_pay_per_use")
        self.assertEqual(appl.get("deal_duration"), "multiyear")
        self.assertIn("source_urls", appl)
        urls = appl.get("source_urls",[])
        self.assertTrue(any("wsj.com" in u for u in urls), "Missing WSJ primary Apple source")
        self.assertTrue(any("macrumors" in u for u in urls), "Missing MacRumors Apple source")
        self.assertTrue(any("9to5mac" in u for u in urls), "Missing 9to5Mac Apple source")
        self.assertTrue(len(urls) >= 6, f"Need at least 6 Apple sources for verification, got {len(urls)}")

    def test_apple_reversal_timeline(self):
        mech = get_mech_372()
        appl = mech.get("apple_siri_ai_deals_aug_2026",{})
        self.assertIn("reversal_timeline", appl)
        rt = appl["reversal_timeline"]
        self.assertIn("phase_1_approach", rt)
        self.assertIn("phase_2_bypass", rt)
        self.assertIn("phase_3_return", rt)

    def test_apple_no_duplicate_of_156_claim(self):
        # Ensure mechanism 372 verifies rather than duplicates 156
        mech = get_mech_372()
        xrefs = mech.get("cross_references",[])
        self.assertTrue(any(r.get("mechanism_id")==156 for r in xrefs), "Should cross-ref mechanism 156")

class TestMechanism372GoogleShowcase(unittest.TestCase):
    def test_showcase_structure(self):
        mech = get_mech_372()
        goog = mech.get("google_showcase_sunset_coercion_jun_2026",{})
        self.assertIn("showcase", goog)
        sc = goog["showcase"]
        self.assertEqual(sc.get("total_commitment_b"), 1)
        self.assertEqual(sc.get("publications_count"), 3000)
        self.assertIn("news_ai_pilot", goog)
        self.assertIn("regulatory_context", goog)
        self.assertIn("source_urls", goog)
        urls = goog.get("source_urls",[])
        self.assertTrue(any("pymnts" in u for u in urls), "Missing PYMNTS Showcase source")
        self.assertTrue(any("nypost" in u for u in urls), "Missing NYPost Showcase source")
        self.assertTrue(any("pressgazette" in u for u in urls), "Missing Press Gazette Showcase source")

    def test_showcase_cautious(self):
        mech = get_mech_372()
        goog = mech.get("google_showcase_sunset_coercion_jun_2026",{})
        overview = goog.get("overview","")
        self.assertIn("Showcase", overview)
        self.assertIn("AI training", overview or str(goog))

class TestMechanism372MetaContrast(unittest.TestCase):
    def test_meta_contrast(self):
        mech = get_mech_372()
        meta = mech.get("meta_q2_2026_contrast",{})
        self.assertIn("advertising_revenue_b", meta)
        self.assertEqual(meta["advertising_revenue_b"], 59.363)
        self.assertIn("structural_antagonism", meta)
        self.assertIn("source_urls", meta)

class TestMechanism372QuadrupleSynthesis(unittest.TestCase):
    def test_synthesis(self):
        mech = get_mech_372()
        synth = mech.get("quadruple_incentive_synthesis",{})
        self.assertEqual(synth.get("incentive_channels"), 4)
        self.assertIn("prediction", synth)
        self.assertIn("asymmetry_quantification", synth)
        self.assertIn("methodology_note", synth)
        # Must mention illustrative synthetic
        meth = synth.get("methodology_note","")
        self.assertIn("Illustrative synthetic", meth)
        self.assertIn("source URL", meth)

    def test_prediction_mentions_wired(self):
        mech = get_mech_372()
        synth = mech.get("quadruple_incentive_synthesis",{})
        pred = synth.get("prediction","")
        self.assertIn("WIRED", pred)

    def test_no_causal_claim(self):
        mech = get_mech_372()
        synth = mech.get("quadruple_incentive_synthesis",{})
        cautious = mech.get("cautious_language","")
        combined = synth.get("prediction","") + " " + cautious
        # Should not claim proof of editorial influence
        self.assertNotIn("proves editorial", combined.lower())
        self.assertIn("not proof of editorial influence", combined.lower())  # fixed: negated form is expected cautious language

class TestMechanism372CrossReferences(unittest.TestCase):
    def test_cross_refs(self):
        mech = get_mech_372()
        xrefs = mech.get("cross_references",[])
        ids = [r.get("mechanism_id") for r in xrefs]
        for required_id in [367, 355, 156]:
            self.assertIn(required_id, ids, f"Missing cross-ref {required_id}")

class TestMechanism372Confounding(unittest.TestCase):
    def test_confounding_present(self):
        mech = get_mech_372()
        conf = mech.get("confounding_factors",[])
        self.assertGreaterEqual(len(conf), 4)
        strengths = [c.get("strength") for c in conf]
        self.assertIn("STRONG", strengths)
        self.assertIn("MODERATE", strengths)

    def test_confounding_predictive_nature(self):
        mech = get_mech_372()
        conf = str(mech.get("confounding_factors",""))
        self.assertIn("PREDICTIVE", conf or "predictive", "Should note predictive nature of Apple deals not yet signed")

class TestMechanism372SourceURLs(unittest.TestCase):
    def test_all_urls_present(self):
        mech = get_mech_372()
        urls = mech.get("source_urls",[])
        self.assertGreaterEqual(len(urls), 15, f"Need at least 15 source URLs for quadruple verification, got {len(urls)}")
        # Check each category present
        url_str = " ".join(urls)
        self.assertIn("adexchanger", url_str)
        self.assertIn("zacks", url_str)
        self.assertIn("wsj.com", url_str)
        self.assertIn("pymnts", url_str)

    def test_no_placeholder_urls(self):
        mech = get_mech_372()
        urls = mech.get("source_urls",[])
        for u in urls:
            self.assertTrue(u.startswith("https://"), f"URL should start with https:// got {u}")
            self.assertNotIn("example.com", u)
            self.assertNotIn("placeholder", u.lower())

class TestGuardianSECUpdate(unittest.TestCase):
    def test_guardian_google_updated(self):
        data = load_yaml(GUARDIAN_PROFILE)
        rels = data.get("revenue_relationships",[])
        google_rels = [r for r in rels if "Google" in r.get("partner","") and r.get("relationship_type")=="advertising"]
        self.assertTrue(len(google_rels)>0, "Missing Guardian Google advertising relationship")
        google = google_rels[0]
        self.assertIn("$81.63B", str(google.get("estimated_value","")) or str(google.get("description","")) or str(google))
        self.assertIn("source_urls", google)

class TestWiredSECUpdate(unittest.TestCase):
    def test_wired_amazon_updated(self):
        data = load_yaml(WIRED_PROFILE)
        rels = data.get("revenue_relationships",[])
        amazon_rels = [r for r in rels if "Amazon" in r.get("partner","")]
        self.assertTrue(len(amazon_rels)>0, "Missing WIRED Amazon relationship")
        amazon = amazon_rels[0]
        self.assertIn("$19.8B", str(amazon.get("estimated_value","")) or str(amazon.get("description","")))

if __name__ == "__main__":
    unittest.main()
