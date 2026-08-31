"""
Test: Google News AI Pilot Two-Year Payment for Permanent Model Weights - Training Data Persistence Beyond 90-Day Exit
Mechanism #412 — Type C: Financial Incentive Mapping
Iteration Sun 2026-08-31 02:00 PT

Finding: Primary-source triangulation of coercive share-or-lose framing (PYMNTS Jun 25 2026 headline Google Tells News Publishers to Share Content for AI Training or Lose Fees, NY Post Jun 26 2026 Google Looks to Bleed Publishers With New AI Partnerships That Would Cull Their Content, AndroidHeadlines Jul 2026 death of classic license, The Information Jun 2026 broad rights via PYMNTS) with Showcase sunset threat. Google pays single-figure millions GBP 1-9M per year for 2 years (Guardian, FT, Press Gazette Aug 2026 understanding, total GBP 2-18M MANUAL ILLUSTRATIVE) for enhanced content rights including broad AI training, grounding, AI Mode rights, but 90-day exit does not require model unlearning or training data deletion, so payment temporary while model weights improvement permanent. Showcase temporary display rights for temporary payment revocable vs News AI pilot permanent training rights for temporary payment irrevocable. Training data persistence beyond contract term creates financial asymmetry. Contrasts with CMA world-first remedy Jun 3-4 2026 requiring effective opt-out tools, fine-tuning opt-out, attribution, 9-month implementation, compliance reports every 6 months, controls not ranking signal. Private contract waives CMA-granted opt-out rights. Industry prediction in two years Google could completely win consumer AI market then does not have to pay publishers anything aligns with 2-year term enabling training extraction before dominance.

Sources:
- Computer Weekly Jun 4 2026 14:52 CMA ruling (9-month, compliance reports, effective tools, attribution, fine-tuning opt-out, Foxglove Rosa Curling, Authoritas 79%, Pew 1% CTR, Loew blogpost Jun 3 2026, subset UK media global rollout, controls not ranking signal)
- Press Gazette Aug 2026 (prisoner dilemma, divide and rule, 36B UK page views up 31% YoY greater than next 24 combined, GBP 21.5B adspend up 7.5% vs GBP 1.1B newsbrands shrink about 5%, 2-year deals, single-figure millions Guardian/FT reader revenue, 200 pubs News AI pilot 2,800 Showcase 33 countries, NDA no-sue 90-day exit take-it-or-leave-it renting peace, Kint layoff/legal cost, GBP 1M+ Showcase, Chinnappa 13-year Google Reuters Institute, SPUR coalition, access not copyright API)
- Barchart/AP Jun 3 2026 world-first effective tools attribution stronger bargaining
- Register Mar 19 2026 opt-out SMS consultation Jan 2026
- PYMNTS Jun 25 2026 broad AI training rights demand, Showcase sunset threat, Google spokesperson news preferences change statement
- NY Post Jun 26 2026 bleed publishers broad rights Kint game dominance
- TechCrunch Dec 10 2025 testing AI-powered article overviews on select publications Google News pages
- AndroidHeadlines Jul 2026 death of classic license via PYMNTS citation
"""

import unittest
import os
import yaml
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
COVERAGE_RESEARCH = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def get_google_mech():
    data = load_yaml(COMPETITOR_ENTITIES)
    entities = data.get("entities") or data.get("competitor_entities")
    assert entities is not None, "Missing entities top-level"
    google = entities.get("google")
    assert google is not None, "Missing google entity"
    mech = google.get("google_news_ai_pilot_permanent_weights_temporary_payment_412")
    assert mech is not None, "Missing mechanism 412 in competitor-entities.yaml under google.google_news_ai_pilot_permanent_weights_temporary_payment_412"
    return mech


def get_research_mech():
    data = load_yaml(COVERAGE_RESEARCH)
    assert "google_news_ai_pilot_permanent_weights_temporary_payment_412" in data, "Missing mechanism 412 in competitor-coverage-research.yaml"
    return data["google_news_ai_pilot_permanent_weights_temporary_payment_412"]


class TestMechanism412Exists(unittest.TestCase):
    def test_google_entity_has_mechanism_412(self):
        mech = get_google_mech()
        self.assertEqual(mech["mechanism_id"], 412)
        self.assertEqual(mech["date_analyzed"], "2026-08-31")
        self.assertIn("Financial Incentive Mapping", mech["type"])
        self.assertEqual(mech["iteration"], "412 - Sun 2026-08-31 02:00 PT")

    def test_research_entry_exists(self):
        mech = get_research_mech()
        self.assertEqual(mech["mechanism_id"], 412)
        self.assertIn("Permanent Model Weights", mech["title"])


class TestRequiredKeys(unittest.TestCase):
    def test_top_level_keys(self):
        mech = get_google_mech()
        for key in ["financial_architecture", "training_data_persistence_mechanism", "regulatory_remedy_cma_world_first", "prisoner_dilemma_collective_action", "quintuple_coercion_update", "confounders_and_alternative_explanations", "verification_status", "source_urls", "mediascope_relevance"]:
            self.assertIn(key, mech, f"Missing key {key} in mechanism 412")

    def test_source_urls_present(self):
        mech = get_google_mech()
        urls = mech.get("source_urls", [])
        self.assertGreaterEqual(len(urls), 5, "Every factual claim needs source URLs - expect at least 5 URLs")
        # Check specific required sources
        combined = " ".join(urls)
        self.assertIn("pymnts.com", combined, "PYMNTS Jun 25 2026 source required")
        self.assertIn("nypost.com", combined, "NY Post Jun 26 2026 source required")
        self.assertIn("pressgazette.co.uk", combined, "Press Gazette Aug 2026 source required")
        self.assertIn("computerweekly.com", combined, "Computer Weekly Jun 4 2026 source required")
        self.assertIn("androidheadlines.com", combined, "AndroidHeadlines Jul 2026 source required")


class TestFinancialStructure(unittest.TestCase):
    def test_predecessor_showcase(self):
        mech = get_google_mech()
        fin = mech["financial_architecture"]
        pred = fin["predecessor_showcase"]
        pred_str = str(pred)
        self.assertIn("2,800", pred_str)
        self.assertIn("33", pred_str)
        self.assertIn("temporary", pred_str.lower())

    def test_successor_payment_and_term(self):
        mech = get_google_mech()
        fin = mech["financial_architecture"]
        succ = fin["successor_news_ai_pilot"]
        succ_str = str(succ)
        self.assertIn("200", succ_str)
        self.assertIn("Single-figure millions", succ_str)
        self.assertIn("2", succ_str)  # term 2 years
        self.assertIn("90", succ_str)  # 90-day exit
        # total GBP 2-18M MANUAL ILLUSTRATIVE must be present
        combined = str(fin)
        self.assertIn("GBP 2-18M", combined)
        self.assertIn("MANUAL ILLUSTRATIVE", combined)

    def test_rights_type_permanent_vs_temporary(self):
        mech = get_google_mech()
        fin = mech["financial_architecture"]
        succ = fin["successor_news_ai_pilot"]
        self.assertIn("permanent", str(succ["rights_type"]).lower())
        self.assertIn("temporary", str(fin["predecessor_showcase"]["rights_type"]).lower())
        self.assertIn("value_exchange", str(fin["predecessor_showcase"]).lower())
        self.assertIn("value_exchange", str(succ).lower())


class TestTrainingPersistence(unittest.TestCase):
    def test_exit_does_not_claw_back(self):
        mech = get_google_mech()
        persist = mech["training_data_persistence_mechanism"]
        self.assertIn("90 days", str(persist["exit_clause_text"]))
        self.assertIn("none reported", str(persist["model_unlearning_requirement"]).lower())
        self.assertIn("fine-tuning", str(persist["fine_tuning_opt_out_vs_signed_deal"]).lower())

    def test_temporary_vs_permanent_asymmetry(self):
        mech = get_google_mech()
        persist = mech["training_data_persistence_mechanism"]
        asym = persist["temporary_vs_permanent_asymmetry"]
        self.assertIn("temporary", asym["showcase"].lower())
        self.assertIn("revocable", asym["showcase"].lower())
        self.assertIn("permanent", asym["news_ai_pilot"].lower())
        self.assertIn("irrevocable", asym["news_ai_pilot"].lower())
        self.assertIn("GBP 2-18M", asym["financial_asymmetry"])

    def test_industry_prediction_alignment(self):
        mech = get_google_mech()
        persist = mech["training_data_persistence_mechanism"]
        self.assertIn("two years", persist["industry_prediction"].lower())
        self.assertIn("completely won", persist["industry_prediction"].lower())


class TestCoerciveFramingTriangulation(unittest.TestCase):
    def test_headlines(self):
        mech = get_google_mech()
        fin = mech["financial_architecture"]
        succ = fin["successor_news_ai_pilot"]
        tri = fin["coercive_framing_triangulation"]
        self.assertIn("Share Content for AI Training or Lose Fees", tri["pymnts_headline"])
        self.assertIn("Bleed Publishers", tri["nypost_headline"])
        self.assertIn("death of the classic license", tri["androidheadlines"].lower())
        self.assertIn("Broad rights", tri["information_via_pymnts"])

    def test_google_official_framing(self):
        mech = get_google_mech()
        tri = mech["financial_architecture"]["coercive_framing_triangulation"]
        self.assertIn("As people's news preferences change", tri["google_official_framing"]["quote"])
        self.assertIn("2,800", tri["google_official_framing"]["quote"])


class TestNoEmDashes(unittest.TestCase):
    def test_no_em_dashes_or_en_dashes(self):
        mech = get_google_mech()
        mech_str = str(mech)
        # Em dash U+2014 and en dash U+2013 are banned per project requirement
        self.assertNotIn("\u2014", mech_str, "Em dash U+2014 found - use hyphen - per project requirement")
        self.assertNotIn("\u2013", mech_str, "En dash U+2013 found - use hyphen - per project requirement")

    def test_no_em_dashes_in_research(self):
        mech = get_research_mech()
        mech_str = str(mech)
        self.assertNotIn("\u2014", mech_str)
        self.assertNotIn("\u2013", mech_str)


class TestFinancialRelationshipsCorrelational(unittest.TestCase):
    def test_correlational_not_causal(self):
        mech = get_google_mech()
        conf = mech["confounders_and_alternative_explanations"]
        conf_str = str(conf).lower()
        self.assertIn("editorial independence", conf_str)
        self.assertIn("correlational not causal", conf_str)
        # Must acknowledge no documented editorial directive
        self.assertIn("no documented editorial directive", conf_str)

    def test_acknowledges_alternative_explanations(self):
        mech = get_google_mech()
        conf = mech["confounders_and_alternative_explanations"]
        self.assertIn("strong", conf)
        self.assertIn("moderate", conf)
        self.assertIn("weak", conf)
        # At least 3 strong confounders
        self.assertGreaterEqual(len(conf["strong"]), 3)


class TestManualIllustrativeLabeling(unittest.TestCase):
    def test_manual_illustrative_labeled(self):
        mech = get_google_mech()
        mech_str = str(mech)
        # Total GBP 2-18M is MANUAL ILLUSTRATIVE - must be labeled as such everywhere it appears
        if "GBP 2-18M" in mech_str:
            self.assertIn("MANUAL ILLUSTRATIVE", mech_str, "Synthetic GBP 2-18M range must be labeled MANUAL ILLUSTRATIVE per project requirement")
        # No p-values, Cohen's d, confidence intervals claimed for tiny samples
        self.assertNotIn("p-value", mech_str.lower())
        self.assertNotIn("p value", mech_str.lower())
        # Cohen's d may be mentioned in scorer note as required method for future validation - allow mention but not claimed as calculated
        # Check we do NOT claim empirical significance from synthetic scores
        self.assertIn("Do NOT claim empirical significance from synthetic scores", mech_str)

    def test_synthetic_scorer_note(self):
        mech = get_google_mech()
        note = mech.get("asymmetry_scorer_note", "")
        self.assertIn("Synthetic scorer not applicable", note)
        self.assertIn("MANUAL ILLUSTRATIVE", note)
        self.assertIn("Welch's t-test", note)
        self.assertIn("Cohen's d", note)


class TestMechanismUniqueness(unittest.TestCase):
    def test_mechanism_id_unique(self):
        data = load_yaml(COMPETITOR_ENTITIES)
        entities = data.get("entities") or data.get("competitor_entities")
        google = entities.get("google")
        # Count mechanism_id 412 occurrences in google entity
        count_412 = 0
        for k, v in google.items():
            if isinstance(v, dict) and v.get("mechanism_id") == 412:
                count_412 += 1
        self.assertEqual(count_412, 1, "mechanism_id 412 should appear exactly once in google entity")

    def test_mechanism_355_still_exists(self):
        data = load_yaml(COMPETITOR_ENTITIES)
        entities = data.get("entities") or data.get("competitor_entities")
        google = entities.get("google")
        self.assertIn("google_news_ai_pilot_deal_structure_cma_neutralization", google)
        self.assertEqual(google["google_news_ai_pilot_deal_structure_cma_neutralization"]["mechanism_id"], 355)


class TestQuintupleCoercion(unittest.TestCase):
    def test_five_channels(self):
        mech = get_google_mech()
        quin = mech["quintuple_coercion_update"]
        self.assertIn("channel_a_advertising", quin)
        self.assertIn("channel_b_traffic", quin)
        self.assertIn("channel_c_showcase_leverage", quin)
        self.assertIn("channel_d_pilot_exclusion", quin)
        self.assertIn("channel_e_contract_waiver_persistence", quin)
        self.assertIn("meta_contrast", quin)
        self.assertIn("zero", quin["meta_contrast"].lower())


class TestCrossReferences(unittest.TestCase):
    def test_cross_references_in_research(self):
        mech = get_research_mech()
        self.assertIn("cross_references", mech)
        cross_ids = [c["mechanism_id"] for c in mech["cross_references"]]
        self.assertIn(355, cross_ids, "Mechanism 412 should cross-reference 355 as extension")
        self.assertIn(88, cross_ids)


class TestSourceURLsValid(unittest.TestCase):
    def test_all_urls_https(self):
        mech = get_google_mech()
        urls = mech["source_urls"]
        for url in urls:
            self.assertTrue(url.startswith("https://"), f"URL must be https: {url}")

    def test_no_duplicate_urls(self):
        mech = get_google_mech()
        urls = mech["source_urls"]
        self.assertEqual(len(urls), len(set(urls)), "Duplicate source URLs found")


if __name__ == "__main__":
    unittest.main()
