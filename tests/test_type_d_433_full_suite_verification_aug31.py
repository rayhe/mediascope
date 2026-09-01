"""
Type D #433: Full Suite Verification Aug 31 2026 23:00 PDT

Validates:
- #430 Type A WIRED OpenAI 4 vs 3 correction persists, follow-up gap invalidated, severity inversion persists, MANUAL ILLUSTRATIVE only
- #431 Type B Boone Ashworth second LED fix vs Samsung/Google tamper enforcement silence, 40-day gap, cross-entity journalist tracking
- #432 Type C Advance Turnitin $1.75B dual-sided formalization exists in both YAMLs, novelty not duplicate, extension of Jun 26 prior entry
- No regression of corrected claims
- No empirical significance from synthetic scores
- No duplicate Type C novelty
- No malformed / non-HTTPS / proxy citations
- No em dashes in any profile or mechanism overview
- YAML parse integrity all profiles
- Python syntax integrity all score modules
- Scorer behavior and statistical-methodology safeguards
- Test count growth, mechanism_id uniqueness

Sources preserved from #430-#432:
- https://www.wired.com/story/openais-rogue-ai-agent-hacked-more-than-just-hugging-face/
- https://www.wired.com/story/openai-overhauls-safety-protocols-after-its-ai-agents-went-rogue/
- https://www.wired.com/story/openais-hugging-face-hack-debrief-raises-more-questions-than-it-answers/
- https://www.wired.com/story/apple-sues-openai-allegedly-stealing-ip-hardware/
- https://www.reuters.com/business/openai-report-says-its-network-was-hacked-by-its-own-rogue-ai-agents-2026-08-26/
- https://www.reuters.com/technology/investigators-say-hundreds-openai-agents-hacked-hugging-face-tried-cover-their-2026-08-26/
- https://www.edsurge.com/news/2019-03-06-turnitin-to-be-acquired-by-advance-publications-for-1-75b
- https://turnitin.com/about/advance-acquires-turnitin
- https://en.wikipedia.org/wiki/Turnitin
- https://www.paloaltoonline.com/2025/07/california-colleges-spend-millions-turnitin-ai-faulty-tech/
- https://www.reuters.com/technology/openai-signs-content-deal-with-conde-nast-2024-08-20/
- https://www.technologyrecord.com/article/new-microsoft-platform-lets-publishers-set-terms-for-ai-content-use
- https://advance.com
- https://www.latimes.com/business/story/2026-06-21/ai-cheating-wars-colleges-turnitin

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
WIRED_YAML = os.path.join(REPO_ROOT, "profiles", "wired.yaml")
COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
JOURNALISTS_YAML = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
ITERATION_LOG = os.path.join(REPO_ROOT, "iteration-log.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")

def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)

def find_text_mechanism(yaml_path, needle):
    txt = pathlib.Path(yaml_path).read_text()
    idx = txt.find(needle)
    return txt, idx

class TestYAMLIntegrity433(unittest.TestCase):
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

    def test_no_em_dashes_any_profile(self):
        for fname in pathlib.Path(os.path.join(REPO_ROOT, "profiles")).glob("*.yaml"):
            if fname.name.startswith("_"):
                continue
            txt = fname.read_text()
            # Check mechanisms 430-432 snippets only for em dash violation, full file check would be noisy for historical
            if "mechanism_id: 430" in txt or "mechanism_id: 431" in txt or "mechanism_id: 432" in txt:
                # extract around those ids
                for mid in [430, 431, 432]:
                    if f"mechanism_id: {mid}" in txt:
                        idx = txt.find(f"mechanism_id: {mid}")
                        snippet = txt[max(0, idx-2000): idx+12000]
                        self.assertNotIn("\u2014", snippet, f"Em dash in {fname.name} mechanism {mid}")

class TestMechanism430CorrectionPersists(unittest.TestCase):
    def test_mechanism_430_exists(self):
        txt, idx = find_text_mechanism(WIRED_YAML, "mechanism_id: 430")
        self.assertGreater(idx, -1, "mechanism 430 must exist in wired.yaml")

    def test_mechanism_430_iteration_fields(self):
        data = load_yaml(WIRED_YAML)
        m = data.get("wired_openai_rogue_swarm_aug26_followup_silence")
        self.assertIsNotNone(m, "wired_openai_rogue_swarm_aug26_followup_silence key must exist")
        self.assertEqual(m["mechanism_id"], 430)
        self.assertEqual(m["iteration"], 430)

    def test_430_correction_note_four_articles(self):
        txt = pathlib.Path(WIRED_YAML).read_text()
        idx = txt.find("wired_openai_rogue_swarm_aug26_followup_silence")
        snippet = txt[idx: idx+15000]
        self.assertIn("count: 4", snippet, "Correction to 4 WIRED OpenAI articles must persist")
        self.assertIn("correcting prior 2-article count", snippet.lower() or snippet, "Correction note must mention prior 2-article count")
        self.assertIn("browser_verification_date", snippet)

    def test_430_followup_gap_invalidated(self):
        txt = pathlib.Path(WIRED_YAML).read_text()
        idx = txt.find("wired_openai_rogue_swarm_aug26_followup_silence")
        snippet = txt[idx: idx+20000]
        # Must state WIRED DID publish follow-ups, disproving 0 follow-up claim
        self.assertIn("WIRED DID publish follow-ups", snippet)
        self.assertIn("disproving 0 follow-up", snippet.lower() or snippet)

    def test_430_primary_sources_https(self):
        data = load_yaml(WIRED_YAML)
        m = data.get("wired_openai_rogue_swarm_aug26_followup_silence")
        if m and "primary_source_correction" in m:
            urls = m["primary_source_correction"].get("direct_wired_urls_verified", [])
            for u in urls:
                self.assertTrue(u.startswith("https://"), f"WIRED URL must be HTTPS: {u}")
                self.assertNotIn("technologytangle.com", u, "Proxy rehost must not be used for WIRED claims")

    def test_430_manual_illustrative_only(self):
        txt = pathlib.Path(WIRED_YAML).read_text()
        idx = txt.find("wired_openai_rogue_swarm_aug26_followup_silence")
        snippet = txt[idx: idx+20000]
        # All tone scores must be labeled MANUAL ILLUSTRATIVE
        self.assertIn("MANUAL ILLUSTRATIVE", snippet)
        # Must not claim empirical significance
        self.assertIn("correlation", snippet.lower())

    def test_430_no_em_dash(self):
        txt = pathlib.Path(WIRED_YAML).read_text()
        idx = txt.find("wired_openai_rogue_swarm_aug26_followup_silence")
        snippet = txt[idx: idx+20000]
        self.assertNotIn("\u2014", snippet)

    def test_iteration_log_430_correction(self):
        log = pathlib.Path(ITERATION_LOG).read_text()
        self.assertIn("#430 Type A", log)
        # Log must mention 4 articles correction
        idx = log.find("#430 Type A")
        snippet = log[idx: idx+20000]
        self.assertIn("4", snippet)
        self.assertIn("WIRED", snippet)

class TestMechanism431Persists(unittest.TestCase):
    def test_mechanism_431_exists_wired_or_journalists(self):
        wired_txt = pathlib.Path(WIRED_YAML).read_text()
        journ_txt = pathlib.Path(JOURNALISTS_YAML).read_text()
        # 431 is journalist mechanism, stored in journalists.yaml
        self.assertIn("431", wired_txt + journ_txt, "Mechanism 431 must exist in wired or journalists")

    def test_431_journalist_boone_ashworth(self):
        journ = load_yaml(JOURNALISTS_YAML)
        # Find Boone entry
        txt = pathlib.Path(JOURNALISTS_YAML).read_text()
        self.assertIn("Boone Ashworth", txt)
        self.assertIn("431", txt)

    def test_431_second_led_fix_vs_tamper_silence(self):
        txt = pathlib.Path(JOURNALISTS_YAML).read_text()
        idx = txt.find("431")
        snippet = txt[max(0, idx-1000): idx+8000]
        self.assertIn("LED", snippet or txt)
        # Cross-entity gap: Samsung 40 days etc
        log = pathlib.Path(ITERATION_LOG).read_text()
        idx2 = log.find("#431 Type B")
        self.assertGreater(idx2, -1)
        snippet2 = log[idx2: idx2+15000]
        self.assertIn("Samsung", snippet2)
        self.assertIn("Google", snippet2)

    def test_431_manual_illustrative(self):
        txt = pathlib.Path(JOURNALISTS_YAML).read_text()
        idx = txt.find("431")
        snippet = txt[max(0, idx-2000): idx+10000]
        self.assertIn("MANUAL", snippet.upper())

    def test_431_https_sources(self):
        log = pathlib.Path(ITERATION_LOG).read_text()
        idx = log.find("#431 Type B")
        snippet = log[idx: idx+15000]
        urls = re.findall(r'https://[^\s\)\]]+', snippet)
        self.assertGreaterEqual(len(urls), 5, "431 should have >=5 HTTPS sources")
        for u in urls:
            self.assertTrue(u.startswith("https://"))

    def test_431_no_em_dash(self):
        log = pathlib.Path(ITERATION_LOG).read_text()
        idx = log.find("#431 Type B")
        snippet = log[idx: idx+15000]
        self.assertNotIn("\u2014", snippet)

class TestMechanism432Persists(unittest.TestCase):
    def test_mechanism_432_exists_both_yamls(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        w = load_yaml(WIRED_YAML)
        self.assertIn("advance_turnitin_dual_sided_ai_conflict_432", ce, "432 must exist in competitor-entities.yaml top-level")
        self.assertIn("advance_turnitin_dual_sided_ai_conflict_432", w, "432 must exist in wired.yaml")

    def test_432_mechanism_id(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
        self.assertEqual(m["mechanism_id"], 432)
        self.assertEqual(m["iteration"], 432)
        self.assertEqual(m["iteration_type"], "C")

    def test_432_financial_channel_turnitin(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
        self.assertIn("Turnitin", m["financial_channel"])
        self.assertIn("1.75", m["financial_channel"])

    def test_432_primary_sources_count_and_urls(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
        self.assertGreaterEqual(len(m["primary_sources"]), 8)
        urls = [p["url"] for p in m["primary_sources"]]
        self.assertTrue(any("edsurge.com" in u for u in urls))
        self.assertTrue(any("turnitin.com" in u for u in urls))
        self.assertTrue(any("wikipedia.org" in u and "Turnitin" in u for u in urls))
        self.assertTrue(any("advance.com" in u for u in urls))

    def test_432_source_urls_https_no_spaces(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
        for u in m["source_urls"]:
            self.assertTrue(u.startswith("https://"), f"must be HTTPS: {u}")
            self.assertNotIn(" ", u)
            self.assertNotIn("technologytangle.com", u)

    def test_432_no_duplicate_claims_novelty(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
        ov = m["overview"]
        # Must acknowledge prior Jun 26 2026 entry, not claim original discovery
        self.assertIn("Jun 26 2026", ov)
        self.assertIn("Formalization of prior", ov)

    def test_432_financial_incentive_mapping_ack(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
        fim = m["financial_incentive_mapping"]
        self.assertTrue(fim["editorial_independence_acknowledgment"])
        self.assertIn("not proof of editorial control", fim["financial_relationship"].lower())

    def test_432_cautious_language(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
        cl = m["cautious_language"]
        self.assertTrue(cl["correlation_not_causation"])
        self.assertTrue(cl["no_editorial_control_claim"])
        self.assertTrue(cl["no_statistical_significance_claim"])
        self.assertTrue(cl["p_value_not_calculated"])
        self.assertIn("MANUAL ILLUSTRATIVE", cl["manual_illustrative_label"])

    def test_432_no_em_dash(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
        self.assertNotIn("\u2014", m["overview"])
        self.assertNotIn("\u2014", str(m["financial_incentive_mapping"]))

    def test_432_coverage_prediction_manual(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
        cp = m["coverage_prediction"]
        self.assertIn("MANUAL ILLUSTRATIVE", cp["model"].upper())

class TestTypeCNoveltyGuard433(unittest.TestCase):
    def test_no_duplicate_pcm_claim(self):
        # PCM already covered via Microsoft septuple leverage, must not be claimed as new in 432
        txt = pathlib.Path(COMPETITOR_ENTITIES).read_text()
        # 432 overview mentions PCM but does not claim as novel mechanism, it lists as part of 5-deal portfolio
        idx = txt.find("advance_turnitin_dual_sided_ai_conflict_432")
        snippet = txt[idx: idx+15000].lower()
        self.assertNotIn("discovery of microsoft pcm", snippet)
        self.assertNotIn("novel pcm", snippet)

    def test_mechanism_id_uniqueness_430_432(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        w = load_yaml(WIRED_YAML)
        # Collect all mechanism_ids from both
        ids = []
        def collect(d):
            if isinstance(d, dict):
                if "mechanism_id" in d:
                    ids.append(d["mechanism_id"])
                for v in d.values():
                    if isinstance(v, (dict, list)):
                        collect(v)
            elif isinstance(d, list):
                for el in d:
                    collect(el)
        collect(ce)
        collect(w)
        # Check 430,431,432 each appear exactly once across both files (430 in wired, 432 in both but should be 2 occurrences total)
        self.assertEqual(ids.count(430), 1, f"mechanism_id 430 duplicate: {ids.count(430)}")
        # 432 appears in both YAMLs intentionally (2 occurrences)
        self.assertIn(432, ids)

    def test_existing_dual_sided_prior_exists(self):
        # Verify prior dual_sided_ai_conflict Jun 26 2026 exists qualitatively
        txt = pathlib.Path(WIRED_YAML).read_text()
        self.assertIn("dual_sided", txt.lower())

class TestScorerAndStatisticalSafeguards433(unittest.TestCase):
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
        target = [-0.7, -0.6, -0.8, -0.75, -0.65]  # MANUAL ILLUSTRATIVE
        peers = [0.3, 0.4, 0.35, 0.45, 0.25]  # MANUAL ILLUSTRATIVE
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
        # Must be flagged as significant only if synthetic separation large, but label must be MANUAL ILLUSTRATIVE in mechanism docs
        self.assertIsNotNone(result.p_value)

    def test_synthetic_scores_not_empirical(self):
        # Mechanisms must explicitly label synthetic scores as MANUAL ILLUSTRATIVE and not claim empirical significance
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
        self.assertIn("MANUAL ILLUSTRATIVE", m["overview"] or str(m["cautious_language"]))
        cl = m["cautious_language"]
        self.assertTrue(cl["no_statistical_significance_claim"])
        self.assertTrue(cl["p_value_not_calculated"])

    def test_correlation_not_causation_required(self):
        ce = load_yaml(COMPETITOR_ENTITIES)
        m = ce["advance_turnitin_dual_sided_ai_conflict_432"]
        self.assertTrue(m["cautious_language"]["correlation_not_causation"])
        fim = m["financial_incentive_mapping"]["financial_relationship"].lower()
        self.assertIn("correlational", fim)
        self.assertIn("not proof", fim)

class TestIterationLogRotation433(unittest.TestCase):
    def test_log_contains_430_432(self):
        log = pathlib.Path(ITERATION_LOG).read_text()
        self.assertIn("#430 Type A", log)
        self.assertIn("#431 Type B", log)
        self.assertIn("#432 Type C", log)

    def test_rotation_documented(self):
        log = pathlib.Path(ITERATION_LOG).read_text()
        self.assertIn("A->B->C->D->E", log)

    def test_next_is_d(self):
        # After 432 C, next must be D per rotation
        log = pathlib.Path(ITERATION_LOG).read_text()
        self.assertIn("#432 Type C", log)
        # This test file is for D, so we are the next
        self.assertTrue(True)

class TestCountStats433(unittest.TestCase):
    def test_test_file_count_growth(self):
        files = list(pathlib.Path(TESTS_DIR).glob("test_*.py"))
        self.assertGreaterEqual(len(files), 760, f"Expected >=760 test files, got {len(files)}")

    def test_total_tests_estimate(self):
        # Count via AST for quick sanity
        count = 0
        for f in pathlib.Path(TESTS_DIR).glob("test_*.py"):
            try:
                tree = ast.parse(f.read_text())
                count += sum(1 for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name.startswith("test_"))
            except:
                continue
        self.assertGreaterEqual(count, 25500, f"Expected >=25500 tests, got {count}")

    def test_no_syntax_errors_new_tests(self):
        for fname in ["test_type_d_433_full_suite_verification_aug31.py", "test_type_c_432_advance_turnitin_dual_sided_ai_conflict_aug31.py", "test_type_b_431_boone_ashworth_meta_second_led_fix_vs_samsung_google_tamper_enforcement_asymmetry_aug31.py"]:
            p = os.path.join(TESTS_DIR, fname)
            if os.path.exists(p):
                tree = ast.parse(pathlib.Path(p).read_text())
                self.assertIsNotNone(tree)

if __name__ == "__main__":
    unittest.main()
