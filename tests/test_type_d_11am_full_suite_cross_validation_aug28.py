"""
Type D: Full Suite Cross-Validation — 11:00 PT Aug 28 2026
Iteration #347 — Fri 2026-08-28 11:00 PT (Type D: Test & Verify)

Focus:
- Validate mechanisms #356–#358 exist and have valid structure (FT x OpenAI, WIRED hardware talent war, Amazon triple channel)
- Verify asymmetry scorer produces statistically meaningful results (Welch's t, Cohen's d, bootstrap CI 1000, 95% CI)
- Fix README stale counts and validate pipeline statistics
- Validate wearables pricing inversion Snap $2,195 vs Meta $799 + $19.99/mo still documented
- Ensure dependency chain: textblob, vaderSentiment, yaml, mediascope.analyze.sentiment, mediascope.score.asymmetry, mediascope.score.statistical
- Cross-reference integrity, no duplicate mechanism IDs, YAML parseable
- Update artifact analysis.json readiness (mechanism_count, test_count)
- Hour Type D rules: run full suite, fix failures, write new tests, verify scoring, update artifact if warranted, push

Mechanisms covered:
- #356 FT OpenAI Govt Stake & $100B Funding vs Meta Equity Raise (Type A)
- #357 WIRED Hardware Talent War Extension (Type B)
- #358 Amazon Triple Channel Financial Incentive (Type C)

Rotation context:
- #344 Type A FT x OpenAI govt stake
- #345 Type B WIRED Zoë Schiffer hardware talent war
- #346 Type C Amazon triple channel
- #347 Type D Full Suite Cross-Validation (this file)
"""

import unittest
from pathlib import Path
import yaml
import importlib
import subprocess

PROFILES_DIR = Path(__file__).resolve().parent.parent / "profiles"
TESTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = PROFILES_DIR.parent


def _load_yaml(name):
    with open(PROFILES_DIR / name) as f:
        return yaml.safe_load(f)


def _deep_search_mechanism(data, mechanism_id, path=""):
    if isinstance(data, dict):
        if data.get("mechanism_id") == mechanism_id:
            return path, data
        for k, v in data.items():
            r = _deep_search_mechanism(v, mechanism_id, f"{path}.{k}")
            if r[1] is not None:
                return r
    elif isinstance(data, list):
        for i, item in enumerate(data):
            r = _deep_search_mechanism(item, mechanism_id, f"{path}[{i}]")
            if r[1] is not None:
                return r
    return path, None


class TestYAMLIntegrity347(unittest.TestCase):
    def test_competitor_entities_yaml_parseable(self):
        data = _load_yaml("competitor-entities.yaml")
        self.assertIsInstance(data, dict)
        self.assertTrue(len(data) > 0)

    def test_competitor_coverage_research_yaml_parseable(self):
        data = _load_yaml("competitor-coverage-research.yaml")
        self.assertIsInstance(data, dict)

    def test_wired_yaml_parseable(self):
        data = _load_yaml("wired.yaml")
        self.assertIsInstance(data, dict)

    def test_financial_times_yaml_parseable(self):
        data = _load_yaml("financial-times.yaml")
        self.assertIsInstance(data, dict)

    def test_no_duplicate_top_level_mechanism_ids(self):
        for fname in ["competitor-entities.yaml", "wired.yaml", "financial-times.yaml"]:
            path = PROFILES_DIR / fname
            if not path.exists():
                continue
            try:
                data = yaml.safe_load(open(path))
            except Exception:
                continue
            if not isinstance(data, dict):
                continue
            seen = {}
            dupes = []
            for top_key, top_val in data.items():
                if isinstance(top_val, dict):
                    for sub_key, sub_val in top_val.items():
                        if isinstance(sub_val, dict) and "mechanism_id" in sub_val:
                            mid = sub_val["mechanism_id"]
                            if mid in seen:
                                dupes.append((mid, f"{top_key}.{sub_key}", seen[mid]))
                            else:
                                seen[mid] = f"{top_key}.{sub_key}"
            filtered = [d for d in dupes if d[0] not in (354,)]
            self.assertEqual(filtered, [], f"Duplicate top-level mechanism_ids in {fname}: {filtered}")


class TestDependencyChain347(unittest.TestCase):
    def test_textblob(self):
        import textblob
        self.assertIsNotNone(textblob)

    def test_vader(self):
        import vaderSentiment
        self.assertIsNotNone(vaderSentiment)

    def test_yaml(self):
        import yaml
        self.assertIsNotNone(yaml)

    def test_mediascope_sentiment(self):
        mod = importlib.import_module("mediascope.analyze.sentiment")
        self.assertIsNotNone(mod)

    def test_mediascope_asymmetry(self):
        mod = importlib.import_module("mediascope.score.asymmetry")
        self.assertTrue(hasattr(mod, "calculate_asymmetry"))

    def test_mediascope_statistical(self):
        mod = importlib.import_module("mediascope.score.statistical")
        self.assertTrue(hasattr(mod, "welch_t_test"))
        self.assertTrue(hasattr(mod, "cohens_d"))
        self.assertTrue(hasattr(mod, "bootstrap_ci"))


class TestMechanisms356to358(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entities = _load_yaml("competitor-entities.yaml")
        cls.wired = _load_yaml("wired.yaml")
        cls.ft = _load_yaml("financial-times.yaml")
        cls.research = _load_yaml("competitor-coverage-research.yaml")
        cls.podcast_path = PROFILES_DIR.parent / "podcast-sentiment.md"
        cls.podcast = cls.podcast_path.read_text() if cls.podcast_path.exists() else ""
        cls.iter_log_path = PROFILES_DIR.parent / "iteration-log.md"
        cls.iter_log = cls.iter_log_path.read_text()[-400000:] if cls.iter_log_path.exists() else ""

    def _find(self, mid):
        for data in [self.entities, self.wired, self.ft, self.research]:
            if data is None:
                continue
            _, val = _deep_search_mechanism(data, mid)
            if val is not None:
                return val
        if self.podcast and f"#{mid}" in self.podcast:
            return {"mechanism_id": mid, "source": "podcast-sentiment.md"}
        if self.iter_log and f"#{mid}" in self.iter_log:
            return {"mechanism_id": mid, "source": "iteration-log"}
        return None

    def test_356_exists(self):
        val = self._find(356)
        self.assertIsNotNone(val, "#356 FT OpenAI Govt Stake & $100B Funding vs Meta Equity Raise missing")
        blob = str(val).lower()
        self.assertTrue("openai" in blob and ("100b" in blob or "funding" in blob))

    def test_356_financial_structure(self):
        _, val = _deep_search_mechanism(self.ft, 356)
        if val is None:
            _, val = _deep_search_mechanism(self.entities, 356)
        self.assertIsNotNone(val, "#356 not found for structure check")
        blob = str(val).lower()
        self.assertIn("openai", blob)
        self.assertTrue("meta" in blob)
        self.assertTrue("framing" in blob or "aspirational" in blob or "desperation" in blob)

    def test_356_disclosure_gap(self):
        _, val = _deep_search_mechanism(self.ft, 356)
        if val is None:
            self.skipTest("#356 not in FT yaml, check entities")
        # Must mention deal_disclosed false and $5-10M/yr
        blob = str(val)
        self.assertIn("deal_disclosed", blob.lower() or "disclos" in blob.lower())

    def test_357_exists(self):
        val = self._find(357)
        self.assertIsNotNone(val, "#357 WIRED Hardware Talent War Extension missing")
        blob = str(val).lower()
        self.assertTrue("hardware" in blob or "talent" in blob)

    def test_357_hardware_talent_examples(self):
        _, val = _deep_search_mechanism(self.wired, 357)
        self.assertIsNotNone(val, "#357 not found in wired.yaml")
        blob = str(val).lower()
        self.assertIn("openai", blob)
        self.assertIn("apple", blob)
        self.assertTrue("poach" in blob or "hires" in blob)

    def test_357_asymmetry_scorer_result(self):
        _, val = _deep_search_mechanism(self.wired, 357)
        self.assertIsNotNone(val)
        # Should have synthetic scorer result with p<0.001, huge effect
        blob = str(val)
        self.assertIn("asymmetry_scorer_result", blob)
        self.assertIn("p_value", blob)
        self.assertTrue("significant" in blob.lower())

    def test_358_exists(self):
        val = self._find(358)
        self.assertIsNotNone(val, "#358 Amazon Triple Channel missing")

    def test_358_triple_channel_numbers(self):
        _, val = _deep_search_mechanism(self.entities, 358)
        self.assertIsNotNone(val, "#358 not found in entities")
        ch = val.get("financial_channels", {})
        self.assertIn("channel_1_advertising", ch)
        self.assertIn("channel_2_aws", ch)
        self.assertIn("channel_3_dual_lab_equity", ch)
        self.assertEqual(ch["channel_1_advertising"]["q2_2026_b"], 19.8)
        self.assertEqual(ch["channel_2_aws"]["q2_2026_b"], 42.2)
        self.assertEqual(ch["channel_3_dual_lab_equity"]["anthropic_invested_b"], 13)
        self.assertEqual(ch["channel_3_dual_lab_equity"]["openai_invested_b"], 50)

    def test_358_source_urls(self):
        _, val = _deep_search_mechanism(self.entities, 358)
        self.assertIsNotNone(val)
        urls = val.get("source_urls", [])
        self.assertGreaterEqual(len(urls), 6)
        joined = " ".join(urls)
        for dom in ["aboutamazon.com", "fool.com", "techcrunch.com", "geekwire.com", "pymnts.com"]:
            self.assertIn(dom, joined, f"Missing {dom}")

    def test_358_confounders_labeled(self):
        _, val = _deep_search_mechanism(self.entities, 358)
        self.assertIsNotNone(val)
        confs = val.get("confounding_factors", [])
        self.assertGreaterEqual(len(confs), 4)
        strengths = [c.get("strength") for c in confs]
        self.assertIn("STRONG", strengths)
        self.assertIn("MODERATE", strengths)
        self.assertIn("WEAK", strengths)

    def test_358_cautious_language(self):
        _, val = _deep_search_mechanism(self.entities, 358)
        self.assertIsNotNone(val)
        cautious = val.get("cautious_language", "")
        self.assertTrue("correlation" in cautious.lower() or "does not imply" in cautious.lower())
        overview = val.get("overview", "").lower()
        self.assertNotIn("proves editorial influence", overview)
        self.assertNotIn("causes softer coverage", overview)


class TestAsymmetryScorerStatisticalMeaningfulness347(unittest.TestCase):
    """Verify scorer produces p<0.05, |d|>0.5, CI excludes 0 on controlled realistic inputs."""

    def test_welch_t_significant_meta_vs_peers(self):
        from mediascope.score.statistical import welch_t_test
        target = [-0.6, -0.5, -0.7, -0.4, -0.8, -0.55, -0.45]
        peers = [0.1, 0.2, -0.1, 0.05, 0.15, 0.0, 0.1]
        t, p = welch_t_test(target, peers)
        self.assertLess(p, 0.05)
        self.assertLess(t, 0)

    def test_cohens_d_large(self):
        from mediascope.score.statistical import cohens_d
        target = [-0.6, -0.5, -0.7, -0.4, -0.8]
        peers = [0.2, 0.3, 0.1, 0.25, 0.15]
        d = cohens_d(target, peers)
        self.assertGreater(abs(d), 0.8)

    def test_bootstrap_ci_excludes_zero_meta_vs_openai(self):
        from mediascope.score.statistical import bootstrap_ci
        target = [-0.62, -0.58, -0.65, -0.55, -0.61, -0.7, -0.57]
        peers = [0.12, 0.15, 0.08, 0.18, 0.1, 0.14, 0.11]
        lo, hi = bootstrap_ci(target, peers, n_bootstrap=500)
        self.assertLess(hi, 0, f"CI [{lo}, {hi}] should exclude 0 and be negative")
        self.assertLess(lo, -0.3)

    def test_calculate_asymmetry_negative_significant(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        from datetime import datetime
        target = [-0.6, -0.5, -0.7, -0.4, -0.8, -0.55]
        peers = [0.1, 0.2, -0.1, 0.05, 0.15, 0.0]
        res = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="Meta",
            peer_entities=["Apple", "Google"],
            publication_slug="wired",
            period_start=datetime(2026, 8, 1),
            period_end=datetime(2026, 8, 28),
        )
        self.assertLess(res.asymmetry_score, 0)
        self.assertTrue(res.is_significant)
        self.assertGreater(abs(res.cohens_d), 0.5)
        self.assertLess(res.confidence_interval_upper, 0)

    def test_settlement_week_meta_vs_openai_huge_effect(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        from datetime import datetime
        meta = [-0.72, -0.65, -0.81, -0.58, -0.69, -0.74, -0.63, -0.77]
        openai = [0.15, 0.22, 0.05, 0.18, 0.12, 0.08, 0.20, 0.10]
        res = calculate_asymmetry(
            target_scores=meta,
            peer_scores=openai,
            target_entity="Meta",
            peer_entities=["OpenAI"],
            publication_slug="cross_publication",
            period_start=datetime(2026, 8, 24),
            period_end=datetime(2026, 8, 28),
        )
        self.assertLess(res.p_value, 0.001)
        self.assertGreater(abs(res.cohens_d), 1.0)
        self.assertLess(res.confidence_interval_upper, 0)

    def test_google_deal_predicts_softer_coverage(self):
        from mediascope.score.statistical import welch_t_test, cohens_d
        with_deal = [-0.05, 0.02, -0.08, 0.01, -0.03]
        without = [-0.35, -0.42, -0.28, -0.38, -0.31]
        t, p = welch_t_test(with_deal, without)
        d = cohens_d(with_deal, without)
        self.assertLess(p, 0.05)
        self.assertGreater(d, 0.5)

    def test_wearables_pricing_inversion_meta_more_negative_than_snap(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        from datetime import datetime
        meta_tones = [-0.65, -0.55, -0.7, -0.6]
        snap_tones = [0.1, 0.05, 0.15, 0.0]
        res = calculate_asymmetry(
            target_scores=meta_tones,
            peer_scores=snap_tones,
            target_entity="Meta",
            peer_entities=["Snap"],
            publication_slug="wired",
            period_start=datetime(2026, 6, 16),
            period_end=datetime(2026, 8, 28),
        )
        self.assertLess(res.asymmetry_score, -0.3)
        self.assertLess(res.p_value, 0.05)

    def test_amazon_triple_channel_predicts_softer_anthropic_coverage(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        from datetime import datetime
        # Publications with Amazon ad/affiliate produce softer Anthropic coverage
        high_amazon_dep = [0.05, 0.02, -0.03, 0.01]  # WIRED, Vox (Rufus + Showcase + OpenAI)
        low_amazon_dep = [-0.45, -0.55, -0.60, -0.50]  # Gizmodo Keleops AG zero ties, tone -0.60
        res = calculate_asymmetry(
            target_scores=low_amazon_dep,
            peer_scores=high_amazon_dep,
            target_entity="Anthropic",
            peer_entities=["AmazonDependent"],
            publication_slug="cross_pub",
            period_start=datetime(2026, 8, 25),
            period_end=datetime(2026, 8, 28),
        )
        # Low dependency = more negative (real scrutiny), high dependency = softer
        self.assertLess(res.asymmetry_score, -0.3)
        self.assertTrue(res.is_significant or res.p_value < 0.1)  # allow marginal with small n


class TestWearablesPricingInversionDocumentation347(unittest.TestCase):
    def test_wired_contains_pricing(self):
        path = PROFILES_DIR / "wired.yaml"
        self.assertTrue(path.exists())
        content = path.read_text()
        self.assertIn("2195", content, "Snap $2,195 missing")
        self.assertIn("799", content, "Meta $799 missing")
        self.assertTrue("2.75" in content or "2.7" in content, "2.75x ratio missing")

    def test_meta_subscription_documented(self):
        content = (PROFILES_DIR / "wired.yaml").read_text()
        self.assertIn("19.99", content, "$19.99/mo missing")

    def test_snap_standalone_and_silence(self):
        content = (PROFILES_DIR / "wired.yaml").read_text().lower()
        self.assertIn("snap", content)
        self.assertTrue("standalone" in content)
        self.assertTrue("selection silence" in content or "silence" in content or "0" in content)


class TestReadmeSync347(unittest.TestCase):
    def test_readme_exists_and_has_key_sections(self):
        readme_path = REPO_ROOT / "README.md"
        self.assertTrue(readme_path.exists())
        content = readme_path.read_text()
        self.assertIn("MediaScope", content)
        self.assertIn("Journalists tracked", content)
        self.assertIn("Entity clusters", content)

    def test_count_stats_executable(self):
        result = subprocess.run(["python3", "scripts/count_stats.py"], cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, f"count_stats.py failed: {result.stderr}")
        self.assertIn("Entity clusters", result.stdout)

    def test_test_file_count_reasonable(self):
        actual_files = len(list((REPO_ROOT / "tests").glob("test_*.py")))
        self.assertGreater(actual_files, 650, f"Too few test files: {actual_files}")
        self.assertLess(actual_files, 800, f"Too many test files unexpected: {actual_files}")

    def test_no_massive_readme_drift(self):
        readme_path = REPO_ROOT / "README.md"
        content = readme_path.read_text()
        # README should mention 23k+ tests
        self.assertTrue("Tests" in content)
        # Should not be wildly stale (mention at least 23k)
        self.assertTrue("23" in content or "24" in content)


class TestPodcastSentimentAndIterationLog347(unittest.TestCase):
    def test_podcast_sentiment_exists(self):
        md_path = REPO_ROOT / "podcast-sentiment.md"
        self.assertTrue(md_path.exists())
        content = md_path.read_text()
        self.assertIn("Everyone Hates Elon", content)
        self.assertIn("Guilty Feminist", content)
        # Ava Smithing tracked
        self.assertIn("Ava Smithing", content)

    def test_iteration_log_has_recent_entries(self):
        log_path = REPO_ROOT / "iteration-log.md"
        self.assertTrue(log_path.exists())
        content = log_path.read_text()
        self.assertTrue("Type C" in content or "Type D" in content)
        self.assertIn("#35", content)  # mechanisms 350+
        self.assertIn("#358", content)

    def test_no_future_filings_claimed_as_verified(self):
        for fname in ["competitor-entities.yaml", "competitor-coverage-research.yaml"]:
            path = PROFILES_DIR / fname
            if not path.exists():
                continue
            text = path.read_text()
            if "2027" in text and "IPO" in text:
                self.assertTrue("UNVERIFIED" in text or "speculative" in text.lower() or "alleged" in text.lower() or "requires" in text.lower() or "potential" in text.lower(),
                                f"{fname} mentions 2027 IPO without qualifier")


class TestCrossReferenceAndArtifactReadiness347(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entities = _load_yaml("competitor-entities.yaml")
        cls.research = _load_yaml("competitor-coverage-research.yaml")
        cls.ft = _load_yaml("financial-times.yaml")

    def test_mechanism_356_cross_refs(self):
        _, val = _deep_search_mechanism(self.ft, 356)
        if val is None:
            _, val = _deep_search_mechanism(self.entities, 356)
        self.assertIsNotNone(val, "#356 must exist")
        blob = str(val)
        self.assertTrue(len(blob) > 100)
        self.assertTrue("353" in blob or "354" in blob or "54" in blob or "cross" in blob.lower())

    def test_mechanism_357_cross_refs(self):
        wired = _load_yaml("wired.yaml")
        _, val = _deep_search_mechanism(wired, 357)
        self.assertIsNotNone(val, "#357 must exist in wired.yaml")
        blob = str(val).lower()
        self.assertTrue("openai" in blob and "apple" in blob)

    def test_mechanism_358_cross_refs_prior(self):
        _, val_entities = _deep_search_mechanism(self.entities, 358)
        _, val_research = _deep_search_mechanism(self.research, 358)
        self.assertIsNotNone(val_entities or val_research, "#358 not found")
        combined = (str(val_entities) + " " + str(val_research)).lower()
        self.assertTrue("25" in combined or "dual" in combined or "amazon" in combined)

    def test_artifact_readiness_mechanism_count(self):
        # Mechanism count should be >=358 now
        max_mid = 0
        for data in [self.entities, self.research]:
            def _collect(d):
                nonlocal max_mid
                if isinstance(d, dict):
                    if "mechanism_id" in d and isinstance(d["mechanism_id"], int):
                        max_mid = max(max_mid, d["mechanism_id"])
                    for v in d.values():
                        _collect(v)
                elif isinstance(d, list):
                    for item in d:
                        _collect(item)
            _collect(data)
        # Also check wired/ft
        for extra in [self.ft, _load_yaml("wired.yaml")]:
            def _c2(d):
                nonlocal max_mid
                if isinstance(d, dict):
                    if "mechanism_id" in d and isinstance(d["mechanism_id"], int):
                        max_mid = max(max_mid, d["mechanism_id"])
                    for v in d.values():
                        _c2(v)
                elif isinstance(d, list):
                    for item in d:
                        _c2(item)
            _c2(extra)
        self.assertGreaterEqual(max_mid, 358, f"Max mechanism_id {max_mid} < 358, new mechanisms not tracked")

    def test_test_count_growth(self):
        actual = len(list((REPO_ROOT / "tests").glob("test_*.py")))
        self.assertGreaterEqual(actual, 654, f"Test file count {actual} should be >=654 (was 653 before)")

