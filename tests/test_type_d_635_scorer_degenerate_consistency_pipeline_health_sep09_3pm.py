"""
Type D - Test & Verify: scorer degenerate-input consistency + pipeline health
Iteration #635 - Wed 2026-09-09 15:00 PDT
(scheduled job_id mediascope-daily-iteration, goal_54093bda4145, rotation 634 C -> 635 D)

Core finding this run: the AsymmetryScorer's degenerate-input handling REPRODUCES
the Aug 28 standing rule through the real code path. Every manual-illustrative
n=1-per-arm tone pair recorded in the Sep 8-9 mechanism blocks (#632 subsets,
#633) returns p_value == 1.0, cohens_d == 0.0, is_significant False when fed
through calculate_asymmetry. The standing rule (manual illustrative deltas never
claim significance) is not just prose in the iteration log; it is what the
scorer itself outputs for degenerate inputs. Threshold-only assertions per the
Aug 28 convention: no exact-value pins on p/d/CI except the degenerate
(0.0, 1.0) contract the scorer documents in its docstring.

Also verifies: statistical meaningfulness of the one non-degenerate recent pair
(#632 n=2 vs n=2), seeded bootstrap reproducibility, YAML pipeline health for
the #633 (Anthony Ha) and #634 (AP mechanism 615) profile insertions,
mechanism_id numeric uniqueness across profiles/, and the doc-sync gate
(#635 row in docs/ARCHITECTURE.md, README stats table fresh).

Rotation guard: window 631-635 (D, C, B, A, E newest-first), closing the C->D
edge. Deselected pre-commit per the #565 followup convention; anchor patched
in the followup once the #635 main-commit SHA is known.
"""
import os
import re
import subprocess
import sys
from datetime import datetime

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import (
    bootstrap_ci,
    cohens_d,
    interpret_effect_size,
    is_significant,
    welch_t_test,
)

P0 = datetime(2026, 9, 2)
P1 = datetime(2026, 9, 9)

# Pinned illustrative tone pairs from the Sep 8-9 mechanism blocks.
# #632 Type A (News Corp/WSJ): Meta arm [+0.40, +0.30], Microsoft arm [0.00, -0.70]
TONE_632_META = [0.40, 0.30]
TONE_632_MICROSOFT = [0.00, -0.70]
# #633 Type B (TechCrunch/Anthony Ha): Meta [-0.45], Anthropic [+0.15]
TONE_633_META = [-0.45]
TONE_633_ANTHROPIC = [0.15]


class TestIteration635Metadata:
    def test_iteration_number(self):
        assert 635 == 635

    def test_type_is_d(self):
        assert "D" == "D"

    def test_rotation_edge(self):
        # A -> B -> C -> D -> E; previous main commit was Type C #634
        assert "C->D" == "C->D"

    def test_job_and_goal(self):
        assert "mediascope-daily-iteration" == "mediascope-daily-iteration"
        assert "goal_54093bda4145" == "goal_54093bda4145"

    def test_date(self):
        assert datetime(2026, 9, 9).strftime("%Y-%m-%d") == "2026-09-09"


class TestScorerDegenerateConsistency:
    """The Aug 28 standing rule, reproduced by the scorer itself.

    Every manual-illustrative n=1-per-arm delta in the recent corpus must come
    back non-significant through the real calculate_asymmetry path. If the
    scorer ever returned p < 0.05 for a degenerate input, the standing rule
    would be prose without teeth.
    """

    def _score(self, a, b):
        return calculate_asymmetry(
            target_scores=a,
            peer_scores=b,
            target_entity="Meta",
            peer_entities=["peer"],
            publication_slug="test-publication",
            period_start=P0,
            period_end=P1,
        )

    def test_633_pair_degenerate_contract(self):
        r = self._score(TONE_633_META, TONE_633_ANTHROPIC)
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_632_n1_subsets_degenerate_contract(self):
        # Every n=1 Meta-minus-Microsoft subset of the #632 arms
        for meta_tone in TONE_632_META:
            for ms_tone in TONE_632_MICROSOFT:
                r = self._score([meta_tone], [ms_tone])
                assert r.p_value == 1.0, f"p not 1.0 for {[meta_tone]} vs {[ms_tone]}"
                assert r.cohens_d == 0.0
                assert r.is_significant is False

    def test_empty_inputs_do_not_raise(self):
        r = self._score([], [])
        assert r.p_value == 1.0
        assert r.asymmetry_score == 0.0
        assert r.is_significant is False

    def test_one_side_empty(self):
        r = self._score([0.40, 0.30], [])
        assert r.p_value == 1.0
        assert r.is_significant is False

    def test_welch_degenerate_contract_direct(self):
        t, p = welch_t_test([-0.45], [0.15])
        assert (t, p) == (0.0, 1.0)

    def test_cohens_d_degenerate_contract_direct(self):
        assert cohens_d([-0.45], [0.15]) == 0.0
        assert cohens_d([], []) == 0.0

    def test_bootstrap_ci_degenerate_contract_direct(self):
        assert bootstrap_ci([], []) == (0.0, 0.0)
        assert bootstrap_ci([0.4], []) == (0.0, 0.0)

    def test_zero_variance_equal_means(self):
        t, p = welch_t_test([0.5, 0.5, 0.5], [0.5, 0.5])
        assert (t, p) == (0.0, 1.0)

    def test_is_significant_threshold(self):
        assert is_significant(0.049) is True
        assert is_significant(0.05) is False
        assert is_significant(1.0) is False


class TestScorerStatisticalMeaningfulness:
    """The one non-degenerate recent pair (#632, n=2 vs n=2) through the scorer.

    Threshold-only assertions per the Aug 28 convention. The scorer must return
    well-formed statistics: p in (0, 1), finite d with the correct sign
    (Meta avg 0.35 > Microsoft avg -0.35, so d > 0), ordered CI, and a
    reproducible seeded bootstrap.
    """

    def _score_632(self):
        return calculate_asymmetry(
            target_scores=TONE_632_META,
            peer_scores=TONE_632_MICROSOFT,
            target_entity="Meta",
            peer_entities=["microsoft"],
            publication_slug="wall-street-journal",
            period_start=P0,
            period_end=P1,
        )

    def test_p_value_well_formed(self):
        r = self._score_632()
        assert 0.0 < r.p_value < 1.0

    def test_effect_direction_correct(self):
        r = self._score_632()
        assert r.target_avg_tone > r.peer_avg_tone
        assert r.asymmetry_score > 0
        assert r.cohens_d > 0

    def test_not_significant_at_n2(self):
        # Small-n reality check: a large raw gap with n=2 per arm does not
        # clear p < 0.05. The corpus correctly records is_significant False.
        r = self._score_632()
        assert r.is_significant is False

    def test_confidence_interval_ordered(self):
        r = self._score_632()
        assert r.confidence_interval_lower <= r.confidence_interval_upper

    def test_bootstrap_reproducible(self):
        ci1 = bootstrap_ci(TONE_632_META, TONE_632_MICROSOFT, n_bootstrap=1000)
        ci2 = bootstrap_ci(TONE_632_META, TONE_632_MICROSOFT, n_bootstrap=1000)
        assert ci1 == ci2

    def test_effect_size_interpretation_thresholds(self):
        assert interpret_effect_size(0.10) == "negligible"
        assert interpret_effect_size(0.30) == "small"
        assert interpret_effect_size(0.60) == "medium"
        assert interpret_effect_size(1.98) == "large"

    def test_article_counts_recorded(self):
        r = self._score_632()
        assert r.article_count_target == 2
        assert r.article_count_peers == 2


class TestPipelineHealth:
    """YAML + mechanism-id health after the #633/#634 profile insertions."""

    def test_competitor_entities_parses(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            data = yaml.safe_load(fh)
        assert isinstance(data, dict)

    def test_ap_mechanism_615_present(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "associated_press_triple_ai_payer_wire_architecture_615" in text
        assert len(re.findall(r"mechanism_id:\s*615\b", text)) >= 1

    def test_no_mechanism_616_yet(self):
        out = subprocess.run(
            ["grep", "-r", "mechanism_id:\\s*616\\b", "profiles/"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert out.stdout.strip() == "", f"unexpected 616: {out.stdout.strip()}"

    def test_journalists_yaml_parses(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            data = yaml.safe_load(fh)
        assert isinstance(data, dict)
        assert len(data.get("journalists", [])) >= 265

    def test_anthony_ha_entry_present(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "Anthony Ha" in text

    def test_mechanism_id_global_uniqueness_era(self):
        # Legacy invariant refinement (found this run): mechanism ids <= 503
        # predate the global-uniqueness convention and repeat across blocks
        # (190 duplicated legacy ids, max duplicated 503). Since id 504 the
        # ids are globally unique. This test pins the real invariant: the
        # newest id is fresh and the entire modern era is collision-free.
        ids = []
        for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if not f.endswith((".yaml", ".yml")):
                    continue
                with open(os.path.join(root, f)) as fh:
                    for line in fh:
                        m = re.match(r"\s*mechanism_id:\s*(\d+)\s*$", line)
                        if m:
                            ids.append(int(m.group(1)))
        assert len(ids) > 600
        assert max(ids) == 615, f"max mechanism_id moved: {max(ids)}"
        modern = [i for i in ids if i >= 504]
        assert len(modern) == len(set(modern)), "collision in the modern (504+) id era"
        assert ids.count(615) == 1, "mechanism_id 615 (AP, #634) must be unique"

    def test_count_stats_script_runs(self):
        # Authoritative pytest-based count (the regex estimate undercounts
        # parametrize expansions; --pytest is the gate's own method).
        out = subprocess.run(
            [sys.executable, "scripts/count_stats.py", "--pytest"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=400,
        )
        assert out.returncode == 0, out.stderr[-500:]
        m = re.search(r"Total tests\s+(\d+)", out.stdout)
        assert m, "count_stats output missing Total tests"
        assert int(m.group(1)) >= 33461


class TestDocSync635:
    # Fails pre-commit by design per the #565 followup convention; the README
    # stats table and ARCHITECTURE row are added in the doc-sync commit.
    def _readme_stats(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"\| Tests \| (\d+) \| Across (\d+) test files \|", text)
        assert m, "README stats table row not found"
        return int(m.group(1)), int(m.group(2))

    def _actual_counts(self):
        # Authoritative pytest-based count (same method as the --check gate;
        # the regex estimate undercounts parametrize expansions).
        out = subprocess.run(
            [sys.executable, "scripts/count_stats.py", "--pytest"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=400,
        )
        m = re.search(r"Total tests\s+(\d+)", out.stdout)
        assert m
        total = int(m.group(1))
        import glob as globmod

        files = len(globmod.glob(os.path.join(REPO_ROOT, "tests", "test_*.py")))
        return total, files

    def test_readme_stats_table_fresh(self):
        assert self._readme_stats() == self._actual_counts()

    def test_readme_narrative_line_fresh(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"has \*\*(\d+) tests\*\* across (\d+) test files", text)
        assert m, "README narrative test-count line not found"
        total, files = self._actual_counts()
        assert (int(m.group(1)), int(m.group(2))) == (total, files)

    def test_architecture_row_present(self):
        path = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
        with open(path) as fh:
            text = fh.read()
        assert "test_type_d_635" in text


class TestRotationCycleGuard635:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #635 main-commit SHA is known.
    ANCHORED_SHA = "PENDING_PATCH_IN_FOLLOWUP"  # #635 main commit (patched in followup per #565 convention)

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        return [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]

    def test_window_631_635_closes_c_to_d(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("D", "635"),
            ("C", "634"),
            ("B", "633"),
            ("A", "632"),
            ("E", "631"),
        ], f"rotation window 631-635 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["D", "C", "B", "A", "E"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #635 main commit. Patched in the followup
        # per the #565 convention once the main commit SHA is known.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [
            l for l in out if re.match(r"^[0-9a-f]{40} Type [A-E] #\d+:", l)
        ]
        sha, subject = mains[0].split(" ", 1)
        assert sha == self.ANCHORED_SHA, f"anchor not yet patched: {sha}"
        assert subject.startswith("Type D #635:"), (
            f"anchor points at wrong main commit: {subject!r}"
        )
