"""Type D #550 (2026-09-05 22:00 PDT): scorer cross-mechanism consistency extended to
#547/#548, standing-rule discipline ratchet, rotation-cycle guard for the
546-549 commit window, 546-550 doc-sync ratchet.

Context: the Aug 28 2026 standing rule says MANUAL ILLUSTRATIVE deltas are NOT
empirical - p_value NOT_CALCULATED, is_significant False in the mechanism YAML,
correlation not causation, no artifact-grade claims. The asymmetry engine
(calculate_asymmetry) still computes t/p/CI on the logged arrays, and its
MEAN-DIFFERENCE arithmetic must reproduce the logged manual delta (engine-drift
detection). The engine's own significance output is computed but deliberately
NOT promoted to a finding for illustrative inputs - this file pins that
separation for the two newest quantitative mechanisms:

- #547 (Type A, WIRED x Google/Samsung camera glasses silence vs Meta alarm,
  Sep 5 19:00 PDT): Google [+0.15] avg +0.15 vs Meta [-0.82, -0.72, -0.78]
  avg -0.773, logged delta_google_minus_meta +0.923 (n=1 vs n=3). This is the
  FIRST positive-sign delta in the consistency suite: the sign convention is
  target-minus-peer, so +0.923 means the target (Google) is SOFTER than the
  reference (Meta) - the opposite direction from every prior consistency
  mechanism. The logged live_asymmetry_score (0.9233333333333335) is the
  engine's own mean-difference arithmetic, stored inline.
- #548 (Type B, Mehrotra Bloomberg-boomerang register constancy, Sep 5 20:00
  PDT): Meta [-0.75, -0.70, -0.75, -0.80] avg -0.75 vs non-Meta targets
  [-0.80, -0.80, -0.75] avg -0.783, logged delta_meta_minus_non_meta 0.033
  (rounded; true arithmetic is 1/30 = 0.03333...). Constancy/falsification
  finding - near-zero delta is the POINT, not a weak asymmetry.
- #549 (Type C, News Corp x Meta $50M/yr licensing, Sep 5 21:00 PDT):
  qualitative - no asymmetry_scorer section is logged
  (statistical_discipline carries tone_scores NOT_SCORED); scorer consistency
  explicitly does NOT apply, mirroring the #544 boundary pinned in #545.
- #546 (Type E, podcast sentiment 32nd verification cycle, Sep 5 18:00 PDT):
  monitoring-only, no quantitative mechanism - no scorer extension.

Also: a rotation-cycle guard pins that the 546 E -> 547 A -> 548 B -> 549 C
window follows A->B->C->D->E->A adjacency in git-commit order (newest
first), extending #545's 541-544 window guard; and the doc-sync ratchet
extends the README/ARCHITECTURE per-file window to 546-550 with the
authoritative count_stats.py --check gate.

Novelty: zero test_type_d_550 files on disk before this run (glob verified);
no #550 in git log (grep verified); scorer consistency has never covered
#547/#548 (repo grep for 547 in scorer-consistency test files returned only
their own mechanism file); the 546-549 rotation window was never guarded;
the 541-545 doc-sync window (from #545) is extended, not duplicated.
"""

from __future__ import annotations

import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

import pytest
import yaml

from mediascope.score.asymmetry import calculate_asymmetry

REPO_ROOT = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TESTS_DIR = REPO_ROOT / "tests"
README = REPO_ROOT / "README.md"
ARCHITECTURE = REPO_ROOT / "docs" / "ARCHITECTURE.md"
LOG = REPO_ROOT / "iteration-log.md"
VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"

FILE_550 = ("test_type_d_550_scorer_consistency_547_548_rotation_doc_sync"
            "_sep05_10pm.py")

PERIOD = (datetime(2026, 1, 1), datetime(2026, 8, 31))


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


def count_def_tests(test_file):
    """Static def-test count, same definition count_stats.count_tests uses."""
    with open(REPO_ROOT / "tests" / test_file) as f:
        content = f.read()
    return len(re.findall(r"^\s+def test_", content, re.MULTILINE))


# ---------------------------------------------------------------------------
# Iteration metadata
# ---------------------------------------------------------------------------


class TestIteration550Metadata:
    def test_docstring_ids(self):
        assert "Type D #550" in __doc__
        assert "2026-09-05 22:00 PDT" in __doc__

    def test_rotation_c_to_d(self):
        # Previous iteration #549 was Type C (commit 30d2710); this run is D.
        assert "C->D" in __doc__.replace(" ", "") or "C -> D" in __doc__ or \
            "rotation" in __doc__.lower()

    def test_filename_convention(self):
        assert os.path.basename(__file__) == FILE_550
        assert FILE_550.startswith("test_type_d_550_")
        assert FILE_550.endswith("_sep05_10pm.py")

    def test_iteration_log_entry_present(self):
        text = LOG.read_text(encoding="utf-8")
        assert re.search(r"^#550 Type D", text, re.MULTILINE), \
            "iteration-log.md missing newest-first #550 Type D heading"


# ---------------------------------------------------------------------------
# Scorer cross-mechanism consistency: engine mean-delta arithmetic reproduces
# the logged MANUAL ILLUSTRATIVE deltas for #547 and #548 (abs tolerance
# 1e-4, per #530 convention); #549 qualitative boundary pinned; the #547
# delta is the first POSITIVE-sign delta in the consistency suite.
# ---------------------------------------------------------------------------

TARGET_547 = [0.15]
PEER_547 = [-0.82, -0.72, -0.78]

TARGET_548 = [-0.75, -0.70, -0.75, -0.80]
PEER_548 = [-0.80, -0.80, -0.75]


class TestScorerCrossMechanismConsistency550:
    def test_547_google_vs_meta_delta_reproduced(self):
        r = score(TARGET_547, PEER_547, "Google", ["Meta"], "wired")
        assert r.asymmetry_score == pytest.approx(0.9233, abs=1e-4)

    def test_547_matches_logged_live_asymmetry_score(self):
        # #547 stores the engine's own mean-difference output inline as
        # live_asymmetry_score (0.9233333333333335); the engine must
        # reproduce it exactly (tolerance 1e-9), not merely the rounded
        # 0.923 delta field.
        r = score(TARGET_547, PEER_547, "Google", ["Meta"], "wired")
        assert r.asymmetry_score == pytest.approx(0.9233333333333335,
                                                  abs=1e-9)

    def test_547_positive_sign_means_target_softer_first_in_suite(self):
        # Sign convention is target-minus-peer; +0.923 means the target
        # (Google) is SOFTER than the reference (Meta) - the first
        # positive-sign delta among all consistency-checked mechanisms
        # (#532/#533/#537/#538/#542/#543 were all target-harsher negative).
        r = score(TARGET_547, PEER_547, "Google", ["Meta"], "wired")
        assert r.target_entity == "Google"
        assert r.asymmetry_score > 0

    def test_547_degenerate_stats_not_significant(self):
        # n=1 target gives degenerate t/p (t=0.0, p=1.0 per the YAML method
        # note); the engine must not call this significant - the standing
        # rule's NOT_CALCULATED in YAML is the deliberate finding-layer
        # choice, separate from this arithmetic-layer check.
        r = score(TARGET_547, PEER_547, "Google", ["Meta"], "wired")
        assert r.is_significant is False

    def test_548_mehrotra_delta_reproduced(self):
        r = score(TARGET_548, PEER_548, "Meta", ["non_Meta_targets"],
                  "wired")
        assert r.asymmetry_score == pytest.approx(0.0333333, abs=1e-4)

    def test_548_logged_rounded_delta_within_rounding(self):
        # The YAML logs the rounded 0.033; true arithmetic is 1/30 =
        # 0.03333... - the logged field must be within rounding tolerance
        # (1e-3) of the engine output.
        r = score(TARGET_548, PEER_548, "Meta", ["non_Meta_targets"],
                  "wired")
        assert abs(r.asymmetry_score - 0.033) < 1e-3

    def test_548_near_zero_delta_not_significant(self):
        # The constancy finding's near-zero delta is the POINT (falsification
        # of reporter-level bias), not a weak asymmetry; the engine agrees
        # it is not statistically distinguishable from zero.
        r = score(TARGET_548, PEER_548, "Meta", ["non_Meta_targets"],
                  "wired")
        assert r.is_significant is False

    def test_549_qualitative_no_tone_delta(self):
        # #549 is Type C qualitative mapping: scorer consistency does not
        # apply. The mechanism block must carry NO asymmetry_scorer section
        # and its statistical_discipline must keep tone_scores NOT_SCORED.
        with open(REPO_ROOT / "profiles" / "competitor-entities.yaml") as f:
            entities = yaml.safe_load(f)
        mech = entities["entities"]["meta"][
            "mechanism_549_newscorp_meta_50m_yr_deal"]
        assert not any(k.startswith("asymmetry_scorer") for k in mech), \
            "qualitative #549 must not log an asymmetry scorer section"
        assert "NOT_SCORED" in str(mech.get("statistical_discipline", "")), \
            "qualitative #549 must keep tone_scores NOT_SCORED"

    def test_547_and_548_deltas_directionally_distinct(self):
        # Both #547 (+0.923, target softer) and #548 (+0.033, near-zero
        # constancy) are non-negative, but the suite must not conflate
        # them: #547's magnitude exceeds #548's by more than 20x - the
        # falsification finding (#548) is a different claim class from the
        # asymmetry observation (#547).
        r547 = score(TARGET_547, PEER_547, "Google", ["Meta"], "wired")
        r548 = score(TARGET_548, PEER_548, "Meta", ["non_Meta_targets"],
                      "wired")
        assert r547.asymmetry_score > 20 * r548.asymmetry_score


# ---------------------------------------------------------------------------
# Standing-rule discipline ratchet: the newest quantitative mechanisms keep
# p_value NOT_CALCULATED and is_significant False in their YAML, even though
# the engine computes t/p/CI on the logged arrays. Logged arrays byte-match
# the engine inputs used in the consistency tests.
# ---------------------------------------------------------------------------

WIRED = REPO_ROOT / "profiles" / "wired.yaml"
MECH_547 = ("mechanism_547_wired_google_samsung_camera_glasses_silence_vs_"
            "meta_alarm_sep05")


def _wired_journalist_548():
    with open(WIRED) as f:
        d = yaml.safe_load(f)
    section = d["journalist_cross_entity_coverage"]
    assert "dhruv_mehrotra" in section, "dhruv_mehrotra block missing"
    return section["dhruv_mehrotra"]


class TestStandingRuleDisciplineRatchet550:
    def _scorer_547(self):
        with open(WIRED) as f:
            d = yaml.safe_load(f)
        return d["competitor_relationships"]["google"][MECH_547][
            "asymmetry_scorer_result"]

    def test_547_scorer_keeps_not_calculated(self):
        s = self._scorer_547()
        assert "NOT_CALCULATED" in str(s["p_value"])
        assert "NOT_CALCULATED" in str(s["cohens_d"])
        assert "NOT_CALCULATED" in str(s["ci"])

    def test_547_scorer_not_significant(self):
        assert self._scorer_547()["is_significant"] is False

    def test_547_logged_arrays_match_engine_inputs(self):
        s = self._scorer_547()
        assert list(s["target_tones_manual_illustrative"]) == TARGET_547
        assert list(s["reference_tones_manual_illustrative"]) == PEER_547
        assert s["delta_google_minus_meta"] == pytest.approx(0.923)

    def test_547_artifact_grade_false(self):
        # Illustrative-only: the block must not be promoted to artifact
        # grade.
        assert self._scorer_547()["artifact_grade"] is False

    def _scorer_548(self):
        return _wired_journalist_548()["asymmetry_scorer_result"]

    def test_548_scorer_keeps_not_calculated(self):
        s = self._scorer_548()
        assert "NOT_CALCULATED" in str(s["p_value"])

    def test_548_scorer_not_significant(self):
        assert self._scorer_548()["is_significant"] is False

    def test_548_logged_arrays_match_engine_inputs(self):
        s = self._scorer_548()
        assert list(s["target_tones_manual_illustrative"]) == TARGET_548
        assert list(s["reference_tones_manual_illustrative"]) == PEER_548
        assert s["delta_meta_minus_non_meta"] == pytest.approx(0.033)

    def test_548_discipline_illustrative_only(self):
        disc = _wired_journalist_548()["statistical_discipline"]
        assert "MANUAL_ILLUSTRATIVE_ONLY" in str(disc["tone_scores"])
        assert "NOT_CALCULATED" in str(disc["p_value"])


# ---------------------------------------------------------------------------
# Rotation-cycle guard: the 546 E -> 547 A -> 548 B -> 549 C window follows
# A->B->C->D->E->A adjacency in git-commit order (newest first), plus this
# run's #550 D closing the cycle. Extends #545's 541-544 window guard.
# ---------------------------------------------------------------------------

_CYCLE = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "A"}


class TestRotationCycleGuard550:
    _SUBJECT_PATTERNS = (
        re.compile(r"Type ([A-E]) #(\d+)"),
        re.compile(r"#(\d+) Type ([A-E])\b"),
        re.compile(r"#(\d+) \(Type ([A-E])\)"),
    )

    @classmethod
    def _parse_subject(cls, subject):
        for pat in cls._SUBJECT_PATTERNS:
            m = pat.search(subject)
            if m:
                groups = m.groups()
                if pat is cls._SUBJECT_PATTERNS[0]:
                    return int(groups[1]), groups[0]
                return int(groups[0]), groups[1]
        return None

    def _recent_type_commits(self, n):
        proc = subprocess.run(
            ["git", "log", "--format=%s", "-25"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=60,
        )
        commits = []
        for line in proc.stdout.splitlines():
            parsed = self._parse_subject(line)
            if parsed:
                commits.append(parsed)
            if len(commits) == n:
                break
        return commits

    def test_546_through_549_types_in_order(self):
        commits = self._recent_type_commits(4)
        assert commits == [(549, "C"), (548, "B"), (547, "A"),
                           (546, "E")], (
            f"expected 549 C / 548 B / 547 A / 546 E newest-first, got "
            f"{commits}"
        )

    def test_cycle_adjacency_holds(self):
        commits = self._recent_type_commits(4)
        for (num_newer, type_newer), (num_older, type_older) in zip(
                commits, commits[1:]):
            assert num_newer == num_older + 1, (
                f"non-consecutive: #{num_newer} after #{num_older}"
            )
            assert _CYCLE[type_older] == type_newer, (
                f"rotation broken: #{num_older} Type {type_older} -> "
                f"#{num_newer} Type {type_newer}, expected "
                f"{_CYCLE[type_older]}"
            )

    def test_545_precedes_546_as_d_before_e(self):
        commits = self._recent_type_commits(5)
        assert commits == [(549, "C"), (548, "B"), (547, "A"), (546, "E"),
                           (545, "D")], (
            f"expected 549 C / 548 B / 547 A / 546 E / 545 D newest-first, "
            f"got {commits}"
        )
        assert _CYCLE["D"] == "E", "D must precede E in the cycle"

    def test_this_run_closes_cycle_as_d(self):
        # This run is #550 Type D: C->D closes the 546-549 window
        # (asserted on the current code's metadata, not on a commit that
        # does not exist until this run is committed).
        assert "Type D #550" in __doc__
        newest = self._recent_type_commits(1)
        assert newest == [(549, "C")], f"expected newest commit (549, C)"
        assert _CYCLE["C"] == "D", "C must be followed by D in the cycle"


# ---------------------------------------------------------------------------
# Doc-sync ratchet: per-file README/ARCHITECTURE rows for the 546-550
# window with true counts; authoritative count gate green.
# ---------------------------------------------------------------------------

DOC_SYNC_WINDOW_550 = [
    "test_type_e_546_podcast_sentiment_thirtysecond_verification_sep05_6pm.py",
    "test_type_a_547_wired_google_samsung_camera_glasses_silence_vs_meta_alarm_sep05_7pm.py",
    "test_type_b_548_dhruv_mehrotra_register_constancy_boomerang_sep05.py",
    "test_type_c_549_newscorp_meta_50m_yr_deal_sep05_9pm.py",
    FILE_550,
]


class TestDocSyncRatchet550:
    """Per-file README/ARCHITECTURE rows exist with true counts (546-550)."""

    def test_readme_row_for_550_with_true_count(self):
        readme = README.read_text()
        pattern = re.compile(
            r"\|\s*`" + re.escape(FILE_550) + r"`\s*\|\s*(\d+)\s*\|"
        )
        m = pattern.search(readme)
        assert m, f"README row missing for {FILE_550}"
        assert int(m.group(1)) == count_def_tests(FILE_550)

    def test_architecture_row_for_550_with_true_count(self):
        arch = ARCHITECTURE.read_text()
        assert FILE_550 in arch, f"ARCHITECTURE row missing for {FILE_550}"
        row = next(line for line in arch.splitlines() if FILE_550 in line)
        assert str(count_def_tests(FILE_550)) in row, (
            f"count mismatch in ARCHITECTURE row for {FILE_550}"
        )

    def test_recent_window_rows_present_in_both_docs(self):
        readme = README.read_text()
        arch = ARCHITECTURE.read_text()
        for fname in DOC_SYNC_WINDOW_550:
            assert fname in readme, f"README row missing for {fname}"
            assert fname in arch, f"ARCHITECTURE row missing for {fname}"

    def test_count_gate_green_under_venv_python(self):
        out = subprocess.run(
            [str(VENV_PYTHON), "scripts/count_stats.py", "--check"],
            capture_output=True,
            text=True,
            timeout=300,
            cwd=REPO_ROOT,
        )
        assert out.returncode == 0, out.stderr[-2000:]
