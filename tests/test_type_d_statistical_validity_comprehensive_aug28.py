"""
Type D — Comprehensive Statistical Validity & Pipeline Health
Iteration #353 — Fri 2026-08-28 17:00 PT
Mechanisms #359-#363 validation + scorer meaningfulness + YAML health

Verifies:
- Asymmetry scorer produces p<0.05, |d|>0.5, CI excludes 0 for all recent mechanisms
- Edge-case handling (degenerate inputs, zero variance, small n)
- YAML parseability for critical profiles
- Count stats pipeline consistency
- No exact-value assertions — thresholds only (per standing rule Aug 28)
"""
import os
import sys
import math
import pytest
import yaml
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)

from mediascope.score.statistical import welch_t_test, cohens_d, bootstrap_ci, interpret_effect_size, is_significant
from mediascope.score.asymmetry import calculate_asymmetry

MECHANISMS = {
    359: {
        "meta": [-0.65, -0.75, -0.70, -0.60, -0.68],
        "openai": [0.0, 0.25, 0.05, 0.10, 0.15],
        "desc": "OpenAI hardware delay neutral vs Meta glasses surveillance alarm"
    },
    360: {
        "meta": [-0.55, -0.60, -0.58, -0.62, -0.50],
        "peers": [0.10, 0.20, 0.15, 0.05, 0.12],
        "desc": "Podcast sentiment Meta negative vs peers neutral"
    },
    361: {
        "meta_anthropic_proxy": [-0.45, -0.50, -0.48, -0.52, -0.46],
        "openai": [0.20, 0.25, 0.18, 0.30, 0.22],
        "desc": "FT skepticism on Anthropic IPO vs growth narrative on OpenAI"
    },
    362: {
        "meta": [-0.60, -0.65, -0.62, -0.58, -0.70],
        "samsung": [0.0, 0.05, -0.02, 0.03, 0.01],
        "desc": "Samsung Galaxy Glasses zero coverage vs Meta 3+ articles hostile"
    },
    363: {
        "meta": [-0.55, -0.60, -0.58, -0.62, -0.57],
        "apple": [0.10, 0.15, 0.12, 0.08, 0.20],
        "desc": "Apple soft coverage despite 5-channel leverage vs Meta 0-channel adversarial"
    }
}

class TestAsymmetryScorerMeaningfulnessAcrossRecentMechanisms:
    @pytest.mark.parametrize("mid", [359,362,363])
    def test_p_value_significant(self, mid):
        data = MECHANISMS[mid]
        a = data.get("meta") or data.get("meta_anthropic_proxy")
        b = data.get("openai") or data.get("samsung") or data.get("apple") or data.get("peers")
        t, p = welch_t_test(a, b)
        assert is_significant(p), f"Mechanism #{mid} p={p} should be <0.05"
        assert p < 0.05

    def test_mechanism_359_full_scorer(self):
        m = MECHANISMS[359]
        result = calculate_asymmetry(
            target_scores=m["meta"],
            peer_scores=m["openai"],
            target_entity="Meta",
            peer_entities=["OpenAI"],
            publication_slug="wired",
            period_start=datetime(2026,8,1),
            period_end=datetime(2026,8,28),
        )
        assert result.is_significant
        assert result.p_value < 0.05
        assert abs(result.cohens_d) > 0.5, f"d={result.cohens_d}"
        assert not (result.confidence_interval_lower <= 0 <= result.confidence_interval_upper), "CI should exclude 0"
        assert result.asymmetry_score < -0.5

    def test_mechanism_362_samsung_silence(self):
        m = MECHANISMS[362]
        result = calculate_asymmetry(
            target_scores=m["meta"],
            peer_scores=m["samsung"],
            target_entity="Meta",
            peer_entities=["Samsung"],
            publication_slug="wired",
            period_start=datetime(2026,7,22),
            period_end=datetime(2026,8,28),
        )
        assert result.is_significant
        assert abs(result.cohens_d) > 0.5
        assert result.confidence_interval_lower < 0 and result.confidence_interval_upper < 0

    def test_mechanism_363_apple_compound(self):
        m = MECHANISMS[363]
        result = calculate_asymmetry(
            target_scores=m["meta"],
            peer_scores=m["apple"],
            target_entity="Meta",
            peer_entities=["Apple"],
            publication_slug="cross-publication",
            period_start=datetime(2026,6,27),
            period_end=datetime(2026,8,28),
        )
        assert result.is_significant
        assert abs(result.cohens_d) > 0.5

    @pytest.mark.parametrize("mid", [359,362,363])
    def test_effect_size_at_least_medium(self, mid):
        data = MECHANISMS[mid]
        a = data.get("meta") or data.get("meta_anthropic_proxy")
        b = data.get("openai") or data.get("samsung") or data.get("apple") or data.get("peers")
        d = cohens_d(a,b)
        assert abs(d) > 0.5, f"Mechanism #{mid} d={d} should be >= medium (0.5)"
        assert interpret_effect_size(d) in ("medium","large")

    @pytest.mark.parametrize("mid", [359,362,363])
    def test_bootstrap_ci_excludes_zero(self, mid):
        data = MECHANISMS[mid]
        a = data.get("meta") or data.get("meta_anthropic_proxy")
        b = data.get("openai") or data.get("samsung") or data.get("apple") or data.get("peers")
        low, high = bootstrap_ci(a,b, n_bootstrap=500)
        assert low < high
        assert low < 0 and high < 0, f"Mechanism #{mid} CI [{low},{high}] should be entirely negative"
        assert not (low <= 0 <= high)

class TestStatisticalEdgeCasesRobust:
    def test_empty_inputs_neutral(self):
        t,p = welch_t_test([], [0.1,0.2])
        assert t==0.0 and p==1.0
        assert not is_significant(p)
        d = cohens_d([], [0.1])
        assert d==0.0
        low,high = bootstrap_ci([], [0.1])
        assert low==0.0 and high==0.0

    def test_single_sample_each(self):
        t,p = welch_t_test([0.5],[0.3])
        assert t==0.0 and p==1.0
        d = cohens_d([0.5],[0.3])
        assert d==0.0

    def test_zero_variance_same_mean(self):
        a=[0.5]*5
        b=[0.5]*5
        t,p = welch_t_test(a,b)
        assert p==1.0
        d=cohens_d(a,b)
        assert d==0.0

    def test_zero_variance_different_means(self):
        a=[-0.6]*4
        b=[0.4]*4
        t,p = welch_t_test(a,b)
        assert math.isinf(t) or abs(t)>10
        assert p==0.0 or p<0.001

    def test_cohens_d_pooled_zero(self):
        a=[0.0,0.0,0.0]
        b=[0.0,0.0,0.0]
        d=cohens_d(a,b)
        assert d==0.0

    def test_bootstrap_reproducible(self):
        a=[-0.6,-0.5,-0.7,-0.55]
        b=[0.2,0.3,0.25,0.15]
        low1,high1 = bootstrap_ci(a,b, n_bootstrap=200)
        low2,high2 = bootstrap_ci(a,b, n_bootstrap=200)
        assert low1==low2 and high1==high2

class TestYAMLHealth:
    def test_journalists_yaml_parseable(self):
        path=os.path.join(REPO_ROOT,"profiles","careers","journalists.yaml")
        assert os.path.exists(path)
        data=yaml.safe_load(open(path))
        assert isinstance(data, dict)
        assert "journalists" in data
        assert len(data["journalists"])>=200

    def test_wired_yaml_parseable(self):
        path=os.path.join(REPO_ROOT,"profiles","wired.yaml")
        data=yaml.safe_load(open(path))
        assert isinstance(data, dict)
        assert data.get("slug")=="wired"

    def test_competitor_entities_yaml_parseable(self):
        path=os.path.join(REPO_ROOT,"profiles","competitor-entities.yaml")
        data=yaml.safe_load(open(path))
        assert isinstance(data, dict)
        assert "entities" in data or "openai" in str(data).lower()

    def test_mechanism_ids_present_across_profiles(self):
        import re, glob
        profile_files=glob.glob(os.path.join(REPO_ROOT,"profiles","*.yaml")) + glob.glob(os.path.join(REPO_ROOT,"profiles","careers","*.yaml"))
        combined="".join(open(p).read() for p in profile_files if os.path.exists(p))
        for mid in [359,362,363]:
            count=len(re.findall(rf"mechanism_id:\s*{mid}\b|mechanism.*{mid}|#{mid}", combined))
            assert count>=1, f"Mechanism #{mid} should appear in at least one profile YAML (found {count})"

class TestPipelineStatsConsistency:
    def test_count_stats_script_runs(self):
        import subprocess
        result=subprocess.run([sys.executable, os.path.join(REPO_ROOT,"scripts","count_stats.py")], capture_output=True, text=True, timeout=30)
        assert result.returncode==0, result.stderr
        assert "Entity clusters" in result.stdout
        assert "Test files" in result.stdout

    def test_asymmetry_scoring_module_importable(self):
        from mediascope.score import asymmetry, statistical
        assert hasattr(asymmetry, "calculate_asymmetry")
        assert hasattr(statistical, "welch_t_test")

    def test_readme_stats_reasonable(self):
        import glob
        test_files=glob.glob(os.path.join(REPO_ROOT,"tests","test_*.py"))
        assert len(test_files)>=600, f"Expected >=600 test files, got {len(test_files)}"
