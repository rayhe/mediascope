"""
Test: Google News AI Pilot Two-Year NDA/No-Sue Deal Structure as Showcase Replacement and Prisoner's Dilemma Neutralizing CMA Opt-Out Remedy
Mechanism #355 — Type C: Financial Incentive Mapping
Iteration Fri 2026-08-28 03:00 PT

Finding: Google's News AI pilot (Dec 10 2025, >200 pubs globally Aug 2026, single-figure millions for Guardian/FT, 2-year term, 90-day exit, NDA/no-sue take-it-or-leave-it) replaces Showcase (2,800 pubs 33 countries, £1M+ UK nationals) with broad AI training/grounding/AI Mode rights. UK CMA world-first ruling Jun 3-4 2026 (SMS Oct 2025, 9-month implementation, compliance reports every 6 months, effective tools, attribution, fine-tuning opt-out, controls not ranking signal) requires opt-out without losing organic ranking. Prisoner's dilemma (divide and rule, no upside to saying no if competitor has deal, already caved, consumer AI win in 2 years, renting peace no product value) explains why Guardian/FT signed despite industry consensus for universal fair payment model. Contractual waiver via private ordering neutralizes regulatory remedy — Press Gazette notes secret deals could make CMA ruling largely irrelevant if most UK publishers sign rights away. 36B UK page views Apr 2026 up 31% YoY > next 24 combined, £21.5B adspend up 7.5% vs £1.1B newsbrands shrink 5%, 90% search share, 1% CTR under AI summaries (Pew), 79% potential traffic loss (Authoritas).

Sources:
- Computer Weekly Jun 4 2026 14:52 CMA ruling (9-month, compliance reports, effective tools, attribution, fine-tuning opt-out, Foxglove Rosa Curling, Authoritas 79%, Pew 1% CTR, Loew blogpost Jun 3 2026)
- Press Gazette Aug 2026 (prisoner dilemma, divide and rule, 36B page views, £21.5B adspend, 2-year single-figure millions Guardian/FT reader revenue, 200 pubs News AI pilot 2,800 Showcase 33 countries, NDA no-sue 90-day exit take-it-or-leave-it renting peace, Kint layoff/legal cost, £1M+ Showcase, Chinnappa 13-year Google, SPUR coalition, access not copyright API)
- Barchart/AP Jun 3 2026 world-first effective tools attribution stronger bargaining
- Register Mar 19 2026 opt-out SMS consultation Jan 2026
- PYMNTS/NY Post Jun 25-26 2026 broad AI training rights Showcase sunset threat
- TechCrunch Dec 10 2025 testing AI overviews
"""

import unittest
import os
import yaml


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
COVERAGE_RESEARCH = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def get_google_mech():
    data = load_yaml(COMPETITOR_ENTITIES)
    # File uses top-level "entities" (not "competitor_entities")
    entities = data.get("entities") or data.get("competitor_entities")
    assert entities is not None, "Missing entities top-level"
    google = entities.get("google")
    assert google is not None, "Missing google entity"
    mech = google.get("google_news_ai_pilot_deal_structure_cma_neutralization")
    assert mech is not None, "Missing mechanism 355"
    return mech


class TestMechanism355Exists(unittest.TestCase):
    def test_google_entity_has_mechanism_355(self):
        mech = get_google_mech()
        self.assertEqual(mech["mechanism_id"], 355)
        self.assertEqual(mech["date_analyzed"], "2026-08-28")
        self.assertIn("Financial Incentive Mapping", mech["type"])

    def test_mechanism_has_required_top_level_keys(self):
        mech = get_google_mech()
        for key in ["financial_structure", "regulatory_remedy", "prisoner_dilemma_collective_action", "neutralization_mechanism", "verification_status", "confounders_and_alternative_explanations", "source_urls"]:
            self.assertIn(key, mech, f"Missing key {key}")


class TestFinancialStructure(unittest.TestCase):
    def test_predecessor_showcase_scale(self):
        mech = get_google_mech()
        fin = mech["financial_structure"]
        self.assertIn("predecessor", fin)
        pred = fin["predecessor"]
        # predecessor may be dict with current_scale or string
        pred_str = str(pred)
        if isinstance(pred, dict):
            pred_str = str(pred.get("current_scale", "")) + str(pred)
        self.assertIn("2,800", pred_str)
        self.assertIn("33", pred_str)

    def test_successor_news_ai_pilot_terms(self):
        mech = get_google_mech()
        fin = mech["financial_structure"]
        self.assertIn("successor", fin)
        succ = fin["successor"]
        succ_str = str(succ)
        # scale
        self.assertIn("200", succ_str)
        # payment range - may be in successor or top-level financial_structure
        combined = str(succ) + str(fin)
        self.assertIn("Single-figure millions", combined)
        self.assertIn("2", combined)  # term 2 years
        self.assertIn("90", combined)  # 90-day exit
        self.assertIn("enhanced content rights", combined.lower())
        self.assertTrue("NDA" in combined or "Non-disclosure" in combined or "no-sue" in combined.lower())

    def test_confidentiality_and_google_framing(self):
        mech = get_google_mech()
        fin = mech["financial_structure"]
        # confidentiality may be in successor or top-level
        combined = str(fin)
        self.assertTrue("Non-disclosure" in combined or "NDA" in combined or "no-sue" in combined.lower())
        self.assertIn("google_official_framing", fin)
        framing = fin["google_official_framing"]
        self.assertIn("As people's news preferences change", framing["quote"])


class TestRegulatoryRemedy(unittest.TestCase):
    def test_cma_world_first_remedy(self):
        mech = get_google_mech()
        reg = mech["regulatory_remedy"]
        self.assertEqual(reg["regulator"], "UK Competition and Markets Authority")
        self.assertIn("Strategic Market Status", reg["designation"])
        self.assertIn("World-first", reg["status"])
        self.assertIn("2026-06-03", reg["ruling_date"])
        reqs = reg["conduct_requirements"]
        self.assertTrue(any("effective tools" in r.lower() for r in reqs))
        self.assertTrue(any("fine-tuning" in r.lower() for r in reqs))
        self.assertTrue(any("attribution" in r.lower() for r in reqs))
        self.assertTrue(any("opt-out" in r.lower() or "opt out" in r.lower() for r in reqs))

    def test_cma_implementation_and_compliance(self):
        mech = get_google_mech()
        reg = mech["regulatory_remedy"]
        # 9 months appears in conduct_requirements
        self.assertIn("9 months", str(reg))
        self.assertIn("google_implementation", reg)
        impl = reg["google_implementation"]
        self.assertIn("2026-06-03", impl["date"])
        self.assertIn("subset", impl["action"].lower())
        self.assertIn("traffic_evidence_cited", reg)
        self.assertIn("79%", str(reg["traffic_evidence_cited"]))

    def test_civil_society_response(self):
        mech = get_google_mech()
        reg = mech["regulatory_remedy"]
        self.assertIn("civil_society_response", reg)
        csr = reg["civil_society_response"]
        self.assertEqual(csr["organization"], "Foxglove")
        self.assertIn("Rosa Curling", csr["spokesperson"])
        self.assertIn("90%", str(csr))
        self.assertIn("own homework", str(csr["concerns"]).lower())


class TestPrisonerDilemma(unittest.TestCase):
    def test_prisoner_dilemma_framing_and_quotes(self):
        mech = get_google_mech()
        pd = mech["prisoner_dilemma_collective_action"]
        self.assertIn("Prisoner's dilemma", pd["frame"])
        quotes = pd.get("industry_quotes", pd.get("industry_source_quotes", {}))
        # Check key quotes present via combined string
        combined = str(quotes).lower()
        self.assertIn("no upside", combined)
        self.assertIn("already caved", combined)
        self.assertIn("consumer ai market", combined)
        self.assertIn("renting peace", combined)

    def test_market_concentration_metrics(self):
        mech = get_google_mech()
        pd = mech["prisoner_dilemma_collective_action"]
        mc = pd["market_concentration"]
        self.assertIn("36", str(mc["google_uk_page_views_apr_2026"]))
        self.assertIn("21.5", str(mc["google_uk_adspend_2025"]))
        self.assertIn("90%", str(mc["google_search_share_uk"]))

    def test_collective_action_failure_and_chinnappa_alternative(self):
        mech = get_google_mech()
        neut = mech["neutralization_mechanism"]
        self.assertIn("alternative_framework", neut)
        alt = neut["alternative_framework"]
        self.assertIn("Madhav Chinnappa", alt["author"])
        self.assertIn("13 years", alt["author"])


class TestNeutralization(unittest.TestCase):
    def test_cma_remedy_neutralized_by_contract(self):
        mech = get_google_mech()
        neut = mech["neutralization_mechanism"]
        self.assertIn("how_cma_remedy_neutralized", neut)
        text = neut["how_cma_remedy_neutralized"]
        self.assertIn("contractually waive", text.lower())
        self.assertIn("Press Gazette", text)
        self.assertIn("largely irrelevant", text.lower())

    def test_fifth_coercion_channel_and_attribution_vs_traffic(self):
        mech = get_google_mech()
        neut = mech["neutralization_mechanism"]
        self.assertIn("fourth_coercion_channel_update", neut)
        self.assertIn("quintuple", neut["fourth_coercion_channel_update"].lower())
        self.assertIn("1%", neut["attribution_vs_traffic"])


class TestVerificationAndConfounders(unittest.TestCase):
    def test_primary_sources_verified(self):
        mech = get_google_mech()
        vs = mech["verification_status"]
        self.assertIn("primary_sources_verified", vs)
        primary = str(vs["primary_sources_verified"])
        self.assertIn("Computer Weekly", primary)
        self.assertIn("Press Gazette", primary)
        self.assertIn("Barchart", primary)

    def test_source_urls_https_and_required_domains(self):
        mech = get_google_mech()
        urls = mech["source_urls"]
        self.assertGreaterEqual(len(urls), 5)
        for url in urls:
            self.assertTrue(url.startswith("https://"), f"URL not HTTPS: {url}")
        self.assertTrue(any("computerweekly.com" in u for u in urls))
        self.assertTrue(any("pressgazette.co.uk" in u for u in urls))
        self.assertTrue(any("barchart.com" in u for u in urls))

    def test_confounders_present_with_strengths(self):
        mech = get_google_mech()
        conf = mech["confounders_and_alternative_explanations"]
        self.assertIn("strong", conf)
        self.assertIn("moderate", conf)
        self.assertIn("weak", conf)
        self.assertGreaterEqual(len(conf["strong"]), 1)
        self.assertTrue(any("reader revenue" in str(c).lower() for c in conf["strong"] + conf["moderate"]))

    def test_speculative_elements_labeled(self):
        mech = get_google_mech()
        vs = mech["verification_status"]
        self.assertIn("speculative_elements_labeled", vs)
        spec = str(vs["speculative_elements_labeled"]).lower()
        self.assertTrue("consumer ai market" in spec or "prediction" in spec)


class TestCoverageResearchEntry(unittest.TestCase):
    def test_coverage_research_has_mechanism_355(self):
        data = load_yaml(COVERAGE_RESEARCH)
        self.assertIn("google_news_ai_pilot_two_year_nda_no_sue_deal_structure_cma_neutralization", data)
        mech = data["google_news_ai_pilot_two_year_nda_no_sue_deal_structure_cma_neutralization"]
        self.assertEqual(mech["mechanism_id"], 355)
        self.assertEqual(mech["date_analyzed"], "2026-08-28")
        self.assertIn("financial_architecture", mech)
        self.assertIn("regulatory_remedy_cma", mech)
        self.assertIn("prisoner_dilemma_collective_action", mech)
        self.assertIn("neutralization_mechanism", mech)

    def test_coverage_research_cross_references(self):
        data = load_yaml(COVERAGE_RESEARCH)
        mech = data["google_news_ai_pilot_two_year_nda_no_sue_deal_structure_cma_neutralization"]
        self.assertIn("cross_references", mech)
        xrefs = [x["mechanism_id"] for x in mech["cross_references"]]
        self.assertIn(88, xrefs)  # Publisher AI Deal Revolt
        self.assertIn(124, xrefs)

    def test_asymmetry_scorer_note_synthetic_disclaimer(self):
        data = load_yaml(COVERAGE_RESEARCH)
        mech = data["google_news_ai_pilot_two_year_nda_no_sue_deal_structure_cma_neutralization"]
        self.assertIn("asymmetry_scorer_note", mech)
        self.assertIn("Synthetic scorer not applicable", mech["asymmetry_scorer_note"])
        self.assertIn("Do NOT claim empirical significance", mech["asymmetry_scorer_note"])


if __name__ == "__main__":
    unittest.main()
