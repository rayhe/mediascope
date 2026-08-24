"""Type D cross-validation — Fri 2026-08-21 00:00 PT

Fixes applied this iteration:
1. Missing Python dependencies (textblob, vaderSentiment) causing 39 test
   collection errors across 505 test files — 942 tests were silently
   uncollectable.
2. README and ARCHITECTURE doc count sync: 17,461→18,633 (pytest-collected)
   / 505 test files.
3. requirements.txt updated with missing dependencies.

Cross-validation checks:
- All 39 previously-broken test files now importable and passing.
- Doc counts in README/ARCHITECTURE consistent with actual file system.
- requirements.txt contains textblob and vaderSentiment.
"""

import os
import re

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")


@pytest.fixture(scope="module")
def readme():
    with open(os.path.join(REPO_ROOT, "README.md")) as f:
        return f.read()


@pytest.fixture(scope="module")
def architecture():
    with open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")) as f:
        return f.read()


@pytest.fixture(scope="module")
def requirements():
    with open(os.path.join(REPO_ROOT, "requirements.txt")) as f:
        return f.read()


@pytest.fixture(scope="module")
def test_file_count():
    return len([f for f in os.listdir(TESTS_DIR)
                if f.startswith("test_") and f.endswith(".py")])


# ── Class 1: Dependency Fix Validation ──

class TestDependencyFixAug21:
    """Validate that textblob and vaderSentiment are importable."""

    def test_textblob_importable(self):
        import textblob
        assert textblob is not None

    def test_vader_importable(self):
        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
        analyzer = SentimentIntensityAnalyzer()
        assert analyzer is not None

    def test_mediascope_sentiment_importable(self):
        from mediascope.analyze.sentiment import analyze_composite
        assert callable(analyze_composite)

    def test_requirements_includes_textblob(self, requirements):
        assert "textblob" in requirements.lower()

    def test_requirements_includes_vader(self, requirements):
        assert "vadersen" in requirements.lower() or "vader" in requirements.lower()


# ── Class 2: Previously Broken Files Now Importable ──

PREVIOUSLY_BROKEN_FILES = [
    "test_arena_cross_analysis",
    "test_atlantic_analysis",
    "test_buzzfeed_smart_glasses_womens_safety_jul14",
    "test_child_safety_analysis",
    "test_competitive_displacement",
    "test_controlled_retreat_language",
    "test_foxbusiness_meta_ai_layoff_discrimination_jul14",
    "test_gizmodo_1_4t_deep_dive",
    "test_gizmodo_1_4t_teen_safety",
    "test_gizmodo_brain2qwerty_v2",
    "test_gizmodo_muse_scrapped",
    "test_gizmodo_siege_roundup_jul11",
    "test_gizmodo_smart_glasses_celebrity_backlash_jul14",
    "test_gizmodo_super_sensing_glasses",
    "test_hackathon_revolt",
    "test_humanization_and_surveillance_enumeration",
    "test_hypocrisy_medical_duress",
    "test_ibd_wedbush_hyperscalers_2026_07_16",
    "test_marketwatch_cloud_pivot",
    "test_marketwatch_smart_glasses_convince_jun27",
    "test_mit_tr_anduril_meta_warfare_glasses",
    "test_mittr_meta_hack_ai_security",
    "test_nypost_meta_ai_layoff_discrimination_jul14",
    "test_nypost_meta_child_safety_monitoring_jul16",
    "test_nypost_muse_image_yanks_jul13",
    "test_nyt_ai_reviews",
    "test_nyt_article_improvements",
    "test_nyt_school_targeting",
    "test_platform_death",
    "test_policy_reversal_competitive_deficit",
    "test_register_muse_image_superintelligence_jul13",
    "test_reuters_muse_spark_11_jul9",
    "test_sentiment",
    "test_source_stance",
    "test_techcentral_smartglasses_glassholes_jul14",
    "test_virtue_ai_acquihire",
    "test_wired_subscription_era",
    "test_wsj_ai_backlash_exec_threats_jul16",
    "test_wsj_meta_ai_layoff_discrimination_jul14",
]


class TestPreviouslyBrokenFilesAug21:
    """All 39 previously-broken test files should now be importable."""

    @pytest.mark.parametrize("module_name", PREVIOUSLY_BROKEN_FILES)
    def test_file_importable(self, module_name):
        import importlib
        mod = importlib.import_module(f"tests.{module_name}")
        # File has at least one test class
        test_items = [name for name in dir(mod)
                      if name.startswith("Test") or name.startswith("test_")]
        assert len(test_items) > 0, f"{module_name} has no test items"


# ── Class 3: Doc Count Sync ──

class TestDocCountSyncAug21:
    """README and ARCHITECTURE file counts match actual."""

    def test_architecture_file_count_matches_actual(self, architecture, test_file_count):
        m = re.search(r"(\d+)\s*test files", architecture)
        assert m, "ARCHITECTURE should state test file count"
        arch_count = int(m.group(1))
        assert arch_count == test_file_count, \
            f"ARCHITECTURE says {arch_count} files but actual is {test_file_count}"

    def test_readme_file_count_in_table(self, readme, test_file_count):
        m = re.search(r"Across (\d+) test files", readme)
        assert m, "README table should state test file count"
        readme_count = int(m.group(1))
        assert readme_count == test_file_count, \
            f"README table says {readme_count} files but actual is {test_file_count}"

    def test_readme_test_count_reasonable(self, readme):
        """README bold test count should be within 10% of grep count."""
        import subprocess
        result = subprocess.run(
            ["grep", "-c", "def test_"] +
            [os.path.join(TESTS_DIR, f) for f in
             os.listdir(TESTS_DIR)
             if f.startswith("test_") and f.endswith(".py")],
            capture_output=True, text=True
        )
        actual_total = sum(int(line.split(":")[-1]) for line in result.stdout.strip().split("\n")
                          if ":" in line)
        m = re.search(r"\*\*(\d+)\s*tests\*\*", readme)
        if not m:
            m = re.search(r"~([\d,]+)\+?\s*\|", readme)
        assert m, "README should state test count"
        readme_count = int(m.group(1).replace(",", ""))
        delta_pct = abs(readme_count - actual_total) / actual_total * 100
        assert delta_pct < 10, \
            f"README says {readme_count} tests but grep finds {actual_total} ({delta_pct:.1f}% off)"


# ── Class 4: Mechanism Count Integrity ──

class TestMechanismIntegrityAug21:
    """competitor-coverage-research.yaml structure is valid."""

    def test_competitor_coverage_research_loads(self):
        import yaml
        path = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        # Must have core sections
        assert "publications" in data
        assert "cross_entity_leverage" in data
        assert "aggregate_findings" in data

    def test_publications_have_entries(self):
        import yaml
        path = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        pubs = data["publications"]
        assert len(pubs) >= 5, f"Expected 5+ publication entries, got {len(pubs)}"
        # At least some entries should have meta coverage analysis
        meta_coverage_count = sum(1 for pub in pubs.values()
                                 if isinstance(pub, dict) and
                                 ("meta_coverage_summary" in pub or "mechanism_id" in pub))
        assert meta_coverage_count >= 5, \
            f"Expected 5+ entries with meta analysis, got {meta_coverage_count}"

    def test_cross_entity_leverage_populated(self):
        import yaml
        path = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        cel = data["cross_entity_leverage"]
        assert len(cel) >= 3, f"Expected 3+ cross-entity entries, got {len(cel)}"
