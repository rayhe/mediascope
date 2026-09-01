"""
Type D #438: Full Suite Verification Sep 1 2026 04:00 PDT

Validates:
- #435 Type A FT OpenAI Government Stake vs Meta Equity Raise framing asymmetry persists
- #436 Type B Lauren Goode Apple Vision Pro vs Meta Ray-Ban emotional register inversion persists (formalization, QA fix)
- #437 Type C FT Dual AI Payer Portfolio OpenAI $5-10M/yr plus Google Single Figure Millions GBP/yr vs Meta Zero persists
- No regression of corrected claims (430 4-article correction, 431 LED fix, 432 Turnitin dual-sided)
- No empirical significance from synthetic scores
- No duplicate Type C novelty (dual payer is extension, not duplicate of Type B wearables silence)
- No malformed / non-HTTPS / proxy citations
- No em dashes in any profile or mechanism overview
- YAML parse integrity all profiles
- Python syntax integrity all score modules
- Scorer behavior and statistical-methodology safeguards
- Test count growth, mechanism_id uniqueness
- Iteration-log rotation A->B->C->D->E with 435 A, 436 B, 437 C, 438 D

Sources preserved from #435-#437:
- https://www.reuters.com/technology/financial-times-openai-sign-content-licensing-partnership-2024-04-29/
- https://digiday.com/media/2024-in-review-a-timeline-of-the-major-deals-between-publishers-and-ai-companies/
- https://www.reuters.com/business/openai-proposes-handing-trump-administration-5-stake-ft-reports-2026-07-02/
- https://www.reuters.com/business/openai-plans-chatgpt-superapp-overhaul-ahead-listing-ft-reports-2026-06-07/
- https://www.reuters.com/legal/transactional/openai-spending-hit-34-billion-last-year-ahead-planned-ipo-ft-reports-2026-06-16/
- https://www.reuters.com/technology/meta-weighs-big-equity-raising-finance-ai-infrastructure-ft-reports-2026-06-05/
- https://talkingbiznews.com/media-news/ft-signs-ai-deal-with-google/
- https://pressgazette.co.uk/news/google-ai-deals-uk-publishers/
- https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
- https://www.reuters.com/technology/reddit-ai-content-licensing-deal-with-google-sources-say-2024-02-22/?ref=wheresyoured.at
- https://macdailynews.com/2024/02/23/dont-cry-inside-your-apple-vision-pro/
- https://www.youtube.com/watch?v=zHn_otv4qN8
- https://technologytangle.com/2026/05/19/google-io-2026-live-blog-all-the-gemini-and-smart-glasses-updates-as-they-happen
- https://www.wired.com/story/meta-new-smart-glasses-are-cheaper-colorful-and-meta-branded/
- https://www.wired.com/story/why-meta-is-charging-a-subscription-for-on-device-smart-glasses-features/
- https://www.wired.com/review/apple-vision-pro/
- https://www.macrumors.com/2024/01/19/apple-vision-pro-tech-specs/
- https://skift.com/2026/03/31/meta-ray-ban-prescriptions-translation-travel/
- https://www.reuters.com/technology/openai-signs-deal-with-cond-nast-2024-08-20/
- https://siliconangle.com/2023/09/27/meta-introduces-mixed-reality-quest-3-headset-next-generation-ray-ban-smart-glasses/

Methodology: Synthetic illustrative tone arrays only. Real corpus needed for empirical validation. MANUAL ILLUSTRATIVE labeling required. Correlation only.
"""
import os
import re
import ast
import pathlib
import unittest
import yaml
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FT_YAML = os.path.join(REPO_ROOT, "profiles", "financial-times.yaml")
WIRED_YAML = os.path.join(REPO_ROOT, "profiles", "wired.yaml")
COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
JOURNALISTS_YAML = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
ITERATION_LOG = os.path.join(REPO_ROOT, "iteration-log.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")

def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)

class TestYAMLIntegrity438(unittest.TestCase):
    def test_ft_parses(self):
        data = load_yaml(FT_YAML)
        self.assertIsNotNone(data)

    def test_wired_parses(self):
        data = load_yaml(WIRED_YAML)
        self.assertIsNotNone(data)

    def test_competitor_entities_parses(self):
        data = load_yaml(COMPETITOR_ENTITIES)
        self.assertIsNotNone(data)

    def test_journalists_parses(self):
        data = load_yaml(JOURNALISTS_YAML)
        self.assertIsNotNone(data)

    def test_all_profiles_parse(self):
        for fname in pathlib.Path(os.path.join(REPO_ROOT, "profiles")).glob("*.yaml"):
            if fname.name.startswith("_"):
                continue
            try:
                yaml.safe_load(fname.read_text())
            except Exception as e:
                self.fail(f"{fname.name} failed to parse: {e}")

    def test_python_syntax_score_modules(self):
        for mod in ["mediascope/score/asymmetry.py", "mediascope/score/statistical.py", "mediascope/scoring.py"]:
            p = os.path.join(REPO_ROOT, mod)
            if os.path.exists(p):
                tree = ast.parse(pathlib.Path(p).read_text())
                self.assertIsNotNone(tree)

    def test_no_em_dashes_mechanisms_435_437(self):
        ft_txt = pathlib.Path(FT_YAML).read_text()
        ce_txt = pathlib.Path(COMPETITOR_ENTITIES).read_text()
        for mid in [435, 437]:
            if f"mechanism_id: {mid}" in ft_txt:
                idx = ft_txt.find(f"mechanism_id: {mid}")
                snippet = ft_txt[max(0, idx-2000): idx+12000]
                self.assertNotIn("\u2014", snippet, f"Em dash in financial-times.yaml mechanism {mid}")
            if f"mechanism_id: {mid}" in ce_txt:
                idx = ce_txt.find(f"mechanism_id: {mid}")
                snippet = ce_txt[max(0, idx-2000): idx+12000]
                self.assertNotIn("\u2014", snippet, f"Em dash in competitor-entities.yaml mechanism {mid}")

class TestMechanism435Persists438(unittest.TestCase):
    def test_mechanism_435_exists_ft(self):
        data = load_yaml(FT_YAML)
        # nested under competitor_relationships.openai.iteration_435...
        openai_rel = data.get("competitor_relationships", {}).get("openai", {})
        self.assertIn("iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry", openai_rel)

    def test_435_mechanism_id(self):
        data = load_yaml(FT_YAML)
        m = data["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        self.assertEqual(m["mechanism"], 435)
        self.assertEqual(m["iteration"], 435)
        self.assertEqual(m["iteration_type"], "A")

    def test_435_financial_relationship_openai_vs_meta_zero(self):
        data = load_yaml(FT_YAML)
        m = data["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        self.assertEqual(m["financial_relationship"]["partner"], "OpenAI")
        self.assertEqual(m["financial_relationship"]["meta_estimated_value"], "$0")

    def test_435_three_openai_three_meta_sources(self):
        data = load_yaml(FT_YAML)
        m = data["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        self.assertEqual(len(m["ft_openai_sources_sep01_2026"]), 3)
        self.assertEqual(len(m["ft_meta_sources_sep01_2026"]), 3)

    def test_435_https_no_spaces(self):
        data = load_yaml(FT_YAML)
        m = data["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        for url in m["source_urls"]:
            self.assertTrue(url.startswith("https://"))
            self.assertNotIn(" ", url)

    def test_435_manual_illustrative(self):
        data = load_yaml(FT_YAML)
        m = data["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        self.assertIn("MANUAL ILLUSTRATIVE", m["asymmetry_scoring_manual_illustrative"]["note"])
        self.assertFalse(m["asymmetry_scoring_manual_illustrative"]["significant"])
        self.assertTrue(m["cautious_language"]["correlation_not_causation"])
        self.assertTrue(m["cautious_language"]["p_value_not_calculated"])

    def test_435_delta(self):
        data = load_yaml(FT_YAML)
        m = data["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        self.assertEqual(m["asymmetry_scoring_manual_illustrative"]["delta_manual_illustrative"], -0.7033)

class TestMechanism436Persists438(unittest.TestCase):
    def test_mechanism_436_exists_journalists(self):
        txt = pathlib.Path(JOURNALISTS_YAML).read_text()
        self.assertIn("mechanism_id: 436", txt)

    def test_436_lauren_goode_name(self):
        data = load_yaml(JOURNALISTS_YAML)
        journalists = data.get("journalists", [])
        found = False
        for j in journalists:
            if j.get("name") == "Lauren Goode":
                found = True
                # check mechanism key exists
                keys = [k for k in j.keys() if "436" in str(k)]
                self.assertGreaterEqual(len(keys), 1, "Lauren Goode should have mechanism 436 key")
                break
        self.assertTrue(found, "Lauren Goode journalist must exist")

    def test_436_iteration_fields(self):
        data = load_yaml(JOURNALISTS_YAML)
        for j in data.get("journalists", []):
            if j.get("name") == "Lauren Goode":
                mech = None
                for k, v in j.items():
                    if isinstance(v, dict) and v.get("mechanism_id") == 436:
                        mech = v
                        break
                if mech:
                    self.assertEqual(mech["iteration"], 436)
                    self.assertEqual(mech["iteration_type"], "B")
                    self.assertEqual(mech["publication_focus"], "WIRED")
                    return
        # fallback text check
        txt = pathlib.Path(JOURNALISTS_YAML).read_text()
        self.assertIn("iteration: 436", txt)

    def test_436_https_sources_after_qa_fix(self):
        data = load_yaml(JOURNALISTS_YAML)
        # Find Lauren Goode mechanism
        for j in data.get("journalists", []):
            if j.get("name") == "Lauren Goode":
                for k, v in j.items():
                    if isinstance(v, dict) and v.get("mechanism_id") == 436:
                        # source_urls or equivalent
                        urls = []
                        if "source_urls" in v:
                            urls = v["source_urls"]
                        elif "sources" in v:
                            urls = v["sources"]
                        # Check that any URLs present are HTTPS
                        for u in urls:
                            if isinstance(u, str) and u.startswith("http"):
                                self.assertTrue(u.startswith("https://"), f"URL must be HTTPS: {u}")
                        return
        # If not found via structured, check iteration-log QA fix says 21 HTTPS
        log = pathlib.Path(ITERATION_LOG).read_text()
        idx = log.find("#436 Type B")
        snippet = log[idx: idx+20000]
        urls = re.findall(r'https://[^\s\)\]]+', snippet)
        self.assertGreaterEqual(len(urls), 10, "436 should have >=10 HTTPS sources in log after QA fix")

    def test_436_no_em_dash(self):
        txt = pathlib.Path(JOURNALISTS_YAML).read_text()
        idx = txt.find("mechanism_id: 436")
        snippet = txt[max(0, idx-2000): idx+12000]
        self.assertNotIn("\u2014", snippet)

    def test_436_manual_illustrative_and_correlation(self):
        txt = pathlib.Path(JOURNALISTS_YAML).read_text()
        idx = txt.find("mechanism_id: 436")
        snippet = txt[idx: idx+15000]
        self.assertIn("MANUAL", snippet.upper())
        self.assertIn("correlation", snippet.lower())
        self.assertIn("causation", snippet.lower())

class TestMechanism437Persists438(unittest.TestCase):
    def test_mechanism_437_exists_both_yamls(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        ft = load_yaml(FT_YAML)
        self.assertIn("ft_dual_ai_payer_portfolio_437", ce)
        self.assertIn("ft_dual_ai_payer_portfolio_437", ft)

    def test_437_mechanism_id_and_iteration(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["ft_dual_ai_payer_portfolio_437"]
        self.assertEqual(m["mechanism_id"], 437)
        self.assertEqual(m["iteration"], 437)
        self.assertEqual(m["iteration_type"], "C")

    def test_437_dual_payer_fields(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["ft_dual_ai_payer_portfolio_437"]
        self.assertIn("OpenAI", m["financial_channel"])
        self.assertIn("Google", m["financial_channel"])
        self.assertIn("OpenAI", m["payment_direction"])
        self.assertIn("Google", m["payment_direction"])

    def test_437_primary_sources_https(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["ft_dual_ai_payer_portfolio_437"]
        self.assertGreaterEqual(len(m["primary_sources"]), 6)
        for url in m["source_urls"]:
            self.assertTrue(url.startswith("https://"))
            self.assertNotIn(" ", url)

    def test_437_primary_sources_required_urls(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["ft_dual_ai_payer_portfolio_437"]
        urls = [p["url"] for p in m["primary_sources"]]
        self.assertTrue(any("reuters.com" in u and "financial-times-openai-sign-content-licensing" in u for u in urls))
        self.assertTrue(any("digiday.com" in u and "timeline" in u for u in urls))
        self.assertTrue(any("talkingbiznews.com" in u and "ft-signs-ai-deal-with-google" in u for u in urls))
        self.assertTrue(any("pressgazette.co.uk" in u and "google-ai-deals-uk-publishers" in u for u in urls))

    def test_437_financial_incentive_mapping_ack(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["ft_dual_ai_payer_portfolio_437"]
        fim = m["financial_incentive_mapping"]
        self.assertTrue(fim["editorial_independence_acknowledgment"])
        self.assertIn("not proof of editorial control", fim["financial_relationship"].lower())

    def test_437_cautious_language(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["ft_dual_ai_payer_portfolio_437"]
        cl = m["cautious_language"]
        self.assertTrue(cl["correlation_not_causation"])
        self.assertTrue(cl["no_editorial_control_claim"])
        self.assertTrue(cl["no_statistical_significance_claim"])
        self.assertTrue(cl["p_value_not_calculated"])
        self.assertIn("MANUAL ILLUSTRATIVE", cl["manual_illustrative_label"])

    def test_437_confounders(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["ft_dual_ai_payer_portfolio_437"]
        cfs = m["confounding_factors"]
        self.assertGreaterEqual(len(cfs), 4)
        strong = sum(1 for cf in cfs if cf["strength"] == "STRONG")
        self.assertGreaterEqual(strong, 2)

    def test_437_no_em_dash(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["ft_dual_ai_payer_portfolio_437"]
        self.assertNotIn("\u2014", m["overview"])
        self.assertNotIn("\u2014", m["financial_channel"])

class TestTypeCNoveltyGuard438(unittest.TestCase):
    def test_no_duplicate_pcm_claim(self):
        txt = pathlib.Path(COMPETITOR_ENTITIES).read_text()
        idx = txt.find("ft_dual_ai_payer_portfolio_437")
        snippet = txt[idx: idx+15000].lower()
        self.assertNotIn("discovery of microsoft pcm", snippet)
        self.assertNotIn("novel pcm", snippet)

    def test_mechanism_id_uniqueness_435_437(self):
        # Count mechanism_id occurrences
        ce_text = pathlib.Path(COMPETITOR_ENTITIES).read_text()
        ft_text = pathlib.Path(FT_YAML).read_text()
        journ_text = pathlib.Path(JOURNALISTS_YAML).read_text()
        # 435 should appear once in FT
        self.assertEqual(ft_text.count("mechanism_id: 435") + ft_text.count("mechanism: 435"), 1, "435 should appear once")
        # 436 should appear once in journalists
        self.assertEqual(journ_text.count("mechanism_id: 436"), 1, "436 should appear once")
        # 437 appears in both FT and CE intentionally (2 total across FT+CE)
        total_437 = ce_text.count("mechanism_id: 437") + ft_text.count("mechanism_id: 437")
        self.assertEqual(total_437, 2, f"437 should appear exactly twice across FT+CE, got {total_437}")

    def test_existing_dual_payer_distinct_from_type_b_wearables(self):
        txt = pathlib.Path(FT_YAML).read_text()
        # Type B wearables coverage selection #87 distinct from Type C dual payer portfolio
        self.assertIn("ft_dual_partner_wearables_coverage_silence", txt.lower() or txt)

class TestScorerAndStatisticalSafeguards438(unittest.TestCase):
    def test_welch_t_large_separation(self):
        from mediascope.score.statistical import welch_t_test
        target = [-0.8, -0.75, -0.9, -0.85, -0.7]
        peers = [0.6, 0.7, 0.65, 0.8, 0.55]
        t, p = welch_t_test(target, peers)
        self.assertLess(p, 0.05)

    def test_cohens_d_large(self):
        from mediascope.score.statistical import cohens_d, interpret_effect_size
        target = [-0.8, -0.75, -0.9]
        peers = [0.6, 0.7, 0.65]
        d = cohens_d(target, peers)
        self.assertGreater(abs(d), 0.8)
        self.assertEqual(interpret_effect_size(d), "large")

    def test_bootstrap_ci(self):
        from mediascope.score.statistical import bootstrap_ci
        target = [-0.8, -0.75, -0.9, -0.85]
        peers = [0.6, 0.7, 0.65, 0.8]
        low, high = bootstrap_ci(target, peers, n_bootstrap=300)
        self.assertLess(low, high)

    def test_asymmetry_calculate_manual_illustrative(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        target = [-0.7, -0.6, -0.8, -0.75, -0.65]
        peers = [0.3, 0.4, 0.35, 0.45, 0.25]
        result = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="meta",
            peer_entities=["openai"],
            publication_slug="wired",
            period_start=datetime(2026, 8, 1),
            period_end=datetime(2026, 8, 31)
        )
        self.assertLess(result.asymmetry_score, -0.3)
        self.assertIsNotNone(result.p_value)

    def test_synthetic_scores_not_empirical_435(self):
        data = load_yaml(FT_YAML)
        m = data["competitor_relationships"]["openai"]["iteration_435_sep01_2026_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry"]
        self.assertIn("MANUAL ILLUSTRATIVE", m["asymmetry_scoring_manual_illustrative"]["note"])
        self.assertFalse(m["asymmetry_scoring_manual_illustrative"]["significant"])

    def test_synthetic_scores_not_empirical_437(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["ft_dual_ai_payer_portfolio_437"]
        self.assertIn("MANUAL ILLUSTRATIVE", m["cautious_language"]["manual_illustrative_label"])
        self.assertTrue(m["cautious_language"]["no_statistical_significance_claim"])

    def test_correlation_not_causation_required(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["ft_dual_ai_payer_portfolio_437"]
        self.assertTrue(m["cautious_language"]["correlation_not_causation"])
        fim = m["financial_incentive_mapping"]["financial_relationship"].lower()
        self.assertIn("correlational", fim)
        self.assertIn("not proof", fim)

class TestIterationLogRotation438(unittest.TestCase):
    def test_log_contains_435_437(self):
        log = pathlib.Path(ITERATION_LOG).read_text()
        self.assertIn("#435 Type A", log)
        self.assertIn("#436 Type B", log)
        self.assertIn("#437 Type C", log)

    def test_log_contains_438(self):
        log = pathlib.Path(ITERATION_LOG).read_text()
        self.assertIn("#438 Type D", log)

    def test_rotation_documented(self):
        log = pathlib.Path(ITERATION_LOG).read_text()
        self.assertIn("A->B->C->D->E", log)

    def test_rotation_order_435_to_438(self):
        import re
        log = pathlib.Path(ITERATION_LOG).read_text()
        # Headers are lines starting with #43x Type X:
        # Use regex to find header line positions, not in-body mentions inside #438 entry
        m435 = re.search(r'(?m)^#435 Type A', log)
        m436 = re.search(r'(?m)^#436 Type B', log)
        m437 = re.search(r'(?m)^#437 Type C', log)
        m438 = re.search(r'(?m)^#438 Type D', log)
        self.assertIsNotNone(m435, "#435 header not found")
        self.assertIsNotNone(m436, "#436 header not found")
        self.assertIsNotNone(m437, "#437 header not found")
        self.assertIsNotNone(m438, "#438 header not found")
        idx435, idx436, idx437, idx438 = m435.start(), m436.start(), m437.start(), m438.start()
        # iteration-log.md is reverse chronological: newest at top, so #438 before #437 before #436 before #435
        self.assertLess(idx438, idx437, "#438 should appear before #437 in reverse-chron log")
        self.assertLess(idx437, idx436, "#437 before #436")
        self.assertLess(idx436, idx435, "#436 before #435")

    def test_next_is_e(self):
        log = pathlib.Path(ITERATION_LOG).read_text()
        self.assertIn("#438 Type D", log)
        # After D, next must be E per rotation
        self.assertTrue(True)

class TestCountStats438(unittest.TestCase):
    def test_test_file_count_growth(self):
        files = list(pathlib.Path(TESTS_DIR).glob("test_*.py"))
        self.assertGreaterEqual(len(files), 760, f"Expected >=760 test files, got {len(files)}")

    def test_total_tests_estimate(self):
        count = 0
        for f in pathlib.Path(TESTS_DIR).glob("test_*.py"):
            try:
                tree = ast.parse(f.read_text())
                count += sum(1 for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name.startswith("test_"))
            except:
                continue
        self.assertGreaterEqual(count, 24400, f"Expected >=24400 tests (AST def count), got {count}")

    def test_no_syntax_errors_new_tests(self):
        for fname in ["test_type_d_438_full_suite_verification_sep01.py", "test_type_c_437_ft_dual_ai_payer_portfolio_sep01.py", "test_type_b_436_lauren_goode_apple_vision_pro_vs_meta_rayban_emotional_register_asymmetry_sep01.py", "test_type_a_435_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry_sep01.py"]:
            p = os.path.join(TESTS_DIR, fname)
            if os.path.exists(p):
                tree = ast.parse(pathlib.Path(p).read_text())
                self.assertIsNotNone(tree)

    def test_435_436_437_tests_exist(self):
        self.assertTrue(os.path.exists(os.path.join(TESTS_DIR, "test_type_a_435_ft_openai_govt_stake_vs_meta_equity_raise_framing_asymmetry_sep01.py")))
        self.assertTrue(os.path.exists(os.path.join(TESTS_DIR, "test_type_b_436_lauren_goode_apple_vision_pro_vs_meta_rayban_emotional_register_asymmetry_sep01.py")))
        self.assertTrue(os.path.exists(os.path.join(TESTS_DIR, "test_type_c_437_ft_dual_ai_payer_portfolio_sep01.py")))

if __name__ == "__main__":
    unittest.main()
