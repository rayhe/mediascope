"""Type D #530: count-gate reliability + scorer cross-mechanism verification.

Iteration 530 (Sep 5 2026, 02:00 PDT) - Type D: Test & Verify.

COUNT-GATE FALSE-STALE INCIDENT: this run opened by running
``python3 scripts/count_stats.py --check`` under the system python, which has
no pytest. The script's pytest-collection path failed silently, fell back to
the regex estimate (28382, an undercount of parametrize expansions), and
reported README=28537 as STALE when the README was in fact correct (the
authoritative pytest-collected count is 28537, verified with .venv/bin/python
in 32s). The fix (scripts/count_stats.py): _find_pytest_python() auto-detects
the repo .venv when sys.executable lacks pytest, the collection timeout is
300s, and the fallback warning now states explicitly that the --check verdict
is NOT authoritative. These tests lock that behavior.

SCORER CROSS-MECHANISM CONSISTENCY: iterations #527 and #528 logged
MANUAL ILLUSTRATIVE deltas computed by hand. This run verifies the
calculate_asymmetry engine reproduces both exactly from the same input
scores, so the illustrative arithmetic and the engine agree across all three
quantitative mechanisms (#522 locked in #525, #527 and #528 locked here).
Per the Aug 28 2026 standing rule these remain illustrative, not empirical.

DOC-SYNC REGRESSION: #529 shipped without per-file rows in README.md and
docs/ARCHITECTURE.md, and the #526 ARCHITECTURE row claimed 9 classes for an
8-class file. Both are fixed this run; these tests ratchet them.
"""

import importlib.util
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import pytest

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import bootstrap_ci

REPO_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
README = REPO_ROOT / "README.md"
ARCHITECTURE = REPO_ROOT / "docs" / "ARCHITECTURE.md"
VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"
PERIOD = (datetime(2026, 1, 1), datetime(2026, 8, 31))


def load_count_stats():
    """Import scripts/count_stats.py as a module (it is not a package)."""
    spec = importlib.util.spec_from_file_location(
        "count_stats", SCRIPTS_DIR / "count_stats.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def count_def_tests(test_file):
    """Static def-test count, same definition count_stats.count_tests uses."""
    with open(REPO_ROOT / "tests" / test_file) as f:
        content = f.read()
    return len(re.findall(r"^\s+def test_", content, re.MULTILINE))


def score(target, peer, target_entity, peers, slug):
    return calculate_asymmetry(
        target_scores=list(target),
        peer_scores=list(peer),
        target_entity=target_entity,
        peer_entities=list(peers),
        publication_slug=slug,
        period_start=PERIOD[0],
        period_end=PERIOD[1],
    )


# ---------------------------------------------------------------------------
# Count-gate reliability: the #530 false-STALE incident
# ---------------------------------------------------------------------------


class TestCountGateFalseStaleIncident:
    """The --check gate must not report STALE from the regex estimate."""

    def test_venv_autodetect_returns_existing_python_with_pytest(self):
        cs = load_count_stats()
        python = cs._find_pytest_python()
        assert os.path.isfile(python)
        out = subprocess.run(
            [python, "-c", "import pytest; print('has-pytest')"],
            capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == "has-pytest"

    def test_pytest_count_is_authoritative_and_ge_regex_estimate(self):
        cs = load_count_stats()
        collected = cs.count_tests_pytest()["total_tests"]
        regex_est = cs.count_tests()["total_tests"]
        # Regex estimate undercounts parametrize expansions (documented);
        # the authoritative collection must be at least as large.
        assert collected >= regex_est
        assert collected > 28000  # sanity floor; absolute value drifts by design

    def test_check_green_under_venv_python(self):
        out = subprocess.run(
            [str(VENV_PYTHON), "scripts/count_stats.py", "--check"],
            capture_output=True, text=True, timeout=300, cwd=REPO_ROOT,
        )
        assert out.returncode == 0, out.stderr[-2000:]
        assert "README stats are current" in out.stdout

    def test_fallback_warning_states_not_authoritative(self, monkeypatch, capsys):
        cs = load_count_stats()
        monkeypatch.setattr(cs, "_find_pytest_python", lambda: "/nonexistent/python-xyz")
        result = cs.count_tests_pytest()  # falls back to regex estimate
        assert result["total_tests"] == cs.count_tests()["total_tests"]
        err = capsys.readouterr().err
        assert "NOT authoritative" in err

    def test_readme_test_count_matches_pytest_collection(self):
        cs = load_count_stats()
        collected = cs.count_tests_pytest()["total_tests"]
        readme = README.read_text()
        m = re.search(r"\|\s*Tests\s*\|\s*([\d,]+)", readme)
        assert m, "README Tests row missing"
        assert int(m.group(1).replace(",", "")) == collected

    def test_readme_file_count_matches_glob(self):
        import glob as globmod

        files = globmod.glob(str(REPO_ROOT / "tests" / "test_*.py"))
        readme = README.read_text()
        m = re.search(r"Across\s+(\d+)\s+test files", readme)
        assert m, "README test-files row missing"
        # README header must track the live file count; absolute values drift
        # by design as new test files land, so compare dynamically.
        assert int(m.group(1)) == len(files)


# ---------------------------------------------------------------------------
# Scorer cross-mechanism consistency: engine reproduces manual deltas
# ---------------------------------------------------------------------------

# #527 (WSJ x Microsoft, MANUAL ILLUSTRATIVE): Meta target [-0.45],
# Microsoft peers [-0.15, 0.10, 0.25], logged delta -0.5167, n.s., NOT_CALCULATED
TARGET_527 = [-0.45]
PEER_527 = [-0.15, 0.10, 0.25]

# #528 (WIRED Chokkattu, MANUAL ILLUSTRATIVE): Meta [0.15, -0.65],
# Apple [0.80, 0.75], logged delta -1.025, n=2 vs n=2, n.s.
TARGET_528 = [0.15, -0.65]
PEER_528 = [0.80, 0.75]

# #522 (WSJ x Perplexity, locked in #525): delta -0.125
TARGET_522 = [-0.2, -0.3, -0.4]
PEER_522 = [-0.2, -0.15]


class TestScorerCrossMechanismConsistency:
    """Engine arithmetic agrees with the hand-logged illustrative deltas."""

    def test_527_engine_reproduces_manual_delta(self):
        s = score(TARGET_527, PEER_527, "meta", ["microsoft"], "wsj")
        assert s.asymmetry_score == pytest.approx(-0.5167, abs=1e-4)
        assert s.target_avg_tone == pytest.approx(-0.45, abs=1e-9)
        assert s.peer_avg_tone == pytest.approx(0.0667, abs=1e-4)

    def test_528_engine_reproduces_manual_delta(self):
        s = score(TARGET_528, PEER_528, "meta", ["apple"], "wired")
        assert s.asymmetry_score == pytest.approx(-1.025, abs=1e-9)
        assert s.target_avg_tone == pytest.approx(-0.25, abs=1e-9)
        assert s.peer_avg_tone == pytest.approx(0.775, abs=1e-9)

    def test_522_engine_delta_still_locked(self):
        s = score(TARGET_522, PEER_522, "perplexity", ["openai", "anthropic"], "wsj")
        assert s.asymmetry_score == pytest.approx(-0.125, abs=1e-9)

    def test_all_quantitative_deltas_same_sign(self):
        """All three quantitative mechanisms show Meta covered harsher
        (negative delta). Directional pattern; illustrative, not empirical."""
        deltas = [
            score(TARGET_522, PEER_522, "perplexity", ["openai", "anthropic"], "wsj").asymmetry_score,
            score(TARGET_527, PEER_527, "meta", ["microsoft"], "wsj").asymmetry_score,
            score(TARGET_528, PEER_528, "meta", ["apple"], "wired").asymmetry_score,
        ]
        assert all(d < 0 for d in deltas), deltas
        assert deltas == pytest.approx([-0.125, -0.5167, -1.025], abs=1e-4)

    def test_528_tiny_n_not_significant_but_huge_effect(self):
        """n=2 vs n=2: p=0.2357 n.s. while Cohen's d=-2.5575 is very large.
        Documents the low-power regime the illustrative deltas live in."""
        s = score(TARGET_528, PEER_528, "meta", ["apple"], "wired")
        assert s.is_significant is False
        assert s.p_value == pytest.approx(0.2357, abs=0.005)
        assert s.cohens_d == pytest.approx(-2.5575, abs=0.01)

    def test_bootstrap_deterministic_on_522_data(self):
        lo1, hi1 = bootstrap_ci(TARGET_522, PEER_522)
        lo2, hi2 = bootstrap_ci(TARGET_522, PEER_522)
        assert (lo1, hi1) == (lo2, hi2)
        # Known-answer bounds pinned by #525
        assert (lo1, hi1) == pytest.approx((-0.225, -0.025), abs=1e-9)

    def test_bootstrap_symmetric_null_contains_zero(self):
        symmetric = [-0.5, -0.25, 0.0, 0.25, 0.5]
        lo, hi = bootstrap_ci(symmetric, symmetric)
        assert lo < 0 < hi


# ---------------------------------------------------------------------------
# Doc-sync ratchet: #529 rows present, #526 class count correct
# ---------------------------------------------------------------------------

DOC_SYNC_FILES = {
    "test_type_e_526_podcast_sentiment_twenty_eighth_verification_sep04_10pm.py": 41,
    "test_type_a_527_wsj_microsoft_woo_side_register_sep04_11pm.py": 26,
    "test_type_b_528_julian_chokkattu_apple_flagship_vs_meta_glasses_review_sep05_12am.py": 41,
    "test_type_c_529_google_canada_c18_100m_meta_zero_sep05_1am.py": 21,
    "test_type_d_530_count_gate_and_scorer_verification_sep05_2am.py": 17,
}


class TestDocSyncRatchet:
    """Per-file README/ARCHITECTURE rows must exist and state true counts."""

    def test_readme_rows_exist_with_true_counts(self):
        readme = README.read_text()
        for fname, expected in DOC_SYNC_FILES.items():
            pattern = re.compile(
                r"\|\s*`" + re.escape(fname) + r"`\s*\|\s*(\d+)\s*\|"
            )
            m = pattern.search(readme)
            assert m, f"README row missing for {fname}"
            assert int(m.group(1)) == expected == count_def_tests(fname), fname

    def test_architecture_rows_exist_with_true_counts(self):
        arch = ARCHITECTURE.read_text()
        for fname, expected in DOC_SYNC_FILES.items():
            assert fname in arch, f"ARCHITECTURE row missing for {fname}"
            # claimed count adjacent to the filename in its tree row
            row = next(line for line in arch.splitlines() if fname in line)
            assert str(expected) in row, f"count mismatch in ARCHITECTURE row for {fname}"

    def test_architecture_526_row_states_8_classes(self):
        arch = ARCHITECTURE.read_text()
        row = next(
            line for line in arch.splitlines()
            if "test_type_e_526" in line
        )
        assert "8 classes" in row
        assert "9 classes" not in row

    def test_529_row_notes_bare_functions(self):
        arch = ARCHITECTURE.read_text()
        row = next(
            line for line in arch.splitlines()
            if "test_type_c_529" in line
        )
        assert "21 tests" in row
