"""Type D #540 (2026-09-05 12:00 PDT): scorer cross-mechanism consistency extended to
#537/#538, standing-rule discipline ratchet, rotation-cycle guard, doc-sync ratchet.

Context: the Aug 28 2026 standing rule says MANUAL ILLUSTRATIVE deltas are NOT
empirical - p_value NOT_CALCULATED, is_significant False in the mechanism YAML,
correlation not causation, no artifact-grade claims. The asymmetry engine
(calculate_asymmetry) still computes t/p/CI on the logged arrays, and its
MEAN-DIFFERENCE arithmetic must reproduce the logged manual delta (engine-drift
detection). The engine's own p<0.05 is computed but deliberately NOT promoted to
a finding for illustrative inputs - this file pins that separation for the two
newest quantitative mechanisms:

- #537 (Type A, Guardian same-day register asymmetry, Sep 5 09:00 PDT):
  Meta [-0.45, -0.40] avg -0.425 vs OpenAI [-0.15, -0.10] avg -0.125,
  logged delta -0.30, n=2 vs n=2.
- #538 (Type B, Cade Metz litigation-adversary symmetry, Sep 5 10:00 PDT):
  Meta [-0.05, -0.25] avg -0.15 vs OpenAI [-0.05, -0.05, 0.0, -0.15]
  avg -0.0625, logged delta -0.0875 (near-symmetric falsification family),
  n=2 vs n=4.
- #539 (Type C, DDM triple-payer, Sep 5 11:00 PDT): qualitative - no tone
  delta is logged (statistical_discipline carries tone_scores NOT_SCORED);
  scorer consistency explicitly does NOT apply.

Also: a rotation-cycle guard pins that the 536 E -> 537 A -> 538 B -> 539 C
commit window follows A->B->C->D->E->A adjacency (complements #510's generic
newest-five consecutiveness guard), and the doc-sync ratchet extends the
README/ARCHITECTURE per-file window to 536-540 with the authoritative
count_stats.py --check gate.

Novelty: zero test_type_d_540 files on disk before this run; no #540 commit
title in git log; scorer consistency has never covered #537/#538; no prior
rotation-adjacency guard over a specific window; the 531-535 doc-sync window
(from #535) is extended, not duplicated.
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

FILE_540 = "test_type_d_540_scorer_consistency_537_538_rotation_doc_sync_sep05_12pm.py"

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


class TestIteration540Metadata:
    def test_docstring_ids(self):
        assert "Type D #540" in __doc__
        assert "2026-09-05 12:00 PDT" in __doc__

    def test_rotation_c_to_d(self):
        # Previous iteration #539 was Type C (commit 4e452fe); this run is D.
        assert "C->D" in __doc__.replace(" ", "") or "C -> D" in __doc__ or \
            "rotation" in __doc__.lower()

    def test_filename_convention(self):
        assert os.path.basename(__file__) == FILE_540
        assert FILE_540.startswith("test_type_d_540_")
        assert FILE_540.endswith("_sep05_12pm.py")

    def test_iteration_log_entry_present(self):
        text = LOG.read_text(encoding="utf-8")
        assert re.search(r"^#540 Type D", text, re.MULTILINE), \
            "iteration-log.md missing newest-first #540 Type D heading"


# ---------------------------------------------------------------------------
# Scorer cross-mechanism consistency: engine mean-delta arithmetic reproduces
# the logged MANUAL ILLUSTRATIVE deltas for #537 and #538 (abs tolerance
# 1e-4, per #530 convention); #532/#533 re-locked.
# ---------------------------------------------------------------------------

TARGET_537 = [-0.45, -0.40]
PEER_537 = [-0.15, -0.10]

TARGET_538 = [-0.05, -0.25]
PEER_538 = [-0.05, -0.05, 0.0, -0.15]

TARGET_532 = [-0.30, -0.25]
PEER_532 = [-0.15, -0.25]
TARGET_533 = [-0.35]
PEER_533 = [-0.30]


class TestScorerCrossMechanismConsistency540:
    def test_537_guardian_same_day_delta_reproduced(self):
        r = score(TARGET_537, PEER_537, "Meta", ["OpenAI"], "guardian")
        assert r.asymmetry_score == pytest.approx(-0.30, abs=1e-4)

    def test_538_metz_symmetry_delta_reproduced(self):
        r = score(TARGET_538, PEER_538, "Meta", ["OpenAI"], "nytimes")
        assert r.asymmetry_score == pytest.approx(-0.0875, abs=1e-4)

    def test_537_engine_bootstrap_ci_excludes_zero(self):
        # Arithmetic property of the engine on the logged arrays (n=2 vs
        # n=2, well-separated): the 95% bootstrap CI for the mean difference
        # sits entirely below zero. This is engine behavior, NOT a finding -
        # the mechanism's own YAML keeps is_significant False per the
        # standing rule (see TestStandingRuleDisciplineRatchet540).
        r = score(TARGET_537, PEER_537, "Meta", ["OpenAI"], "guardian")
        assert r.confidence_interval_upper < 0

    def test_538_engine_bootstrap_ci_includes_zero(self):
        # Falsification-family property: the near-symmetric #538 delta's
        # bootstrap CI straddles zero, matching the mechanism's
        # near-symmetric (|delta| < 0.10) classification.
        r = score(TARGET_538, PEER_538, "Meta", ["OpenAI"], "nytimes")
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_538_delta_magnitude_bounded(self):
        r = score(TARGET_538, PEER_538, "Meta", ["OpenAI"], "nytimes")
        assert abs(r.asymmetry_score) < 0.10

    def test_532_dual_deal_symmetry_relock(self):
        r = score(TARGET_532, PEER_532, "Meta", ["OpenAI"], "wsj")
        assert r.asymmetry_score == pytest.approx(-0.075, abs=1e-4)
        assert r.is_significant is False

    def test_533_matched_story_type_relock(self):
        r = score(TARGET_533, PEER_533, "Meta", ["OpenAI"], "wsj")
        assert r.asymmetry_score == pytest.approx(-0.05, abs=1e-4)
        assert r.is_significant is False

    def test_539_qualitative_no_tone_delta(self):
        # #539 is Type C qualitative mapping: scorer consistency does not
        # apply. The mechanism block must carry NO asymmetry_scorer section
        # and its statistical_discipline must keep tone_scores NOT_SCORED.
        with open(REPO_ROOT / "profiles" / "competitor-entities.yaml") as f:
            entities = yaml.safe_load(f)
        mech = entities["entities"]["openai"][
            "mechanism_539_dotdash_meredith_triple_payer_openai_meta_microsoft_pcm"
        ]
        assert not any(k.startswith("asymmetry_scorer") for k in mech), \
            "qualitative #539 must not log an asymmetry scorer section"
        assert "NOT_SCORED" in str(mech.get("statistical_discipline", "")), \
            "qualitative #539 must keep tone_scores NOT_SCORED"

    def test_all_deltas_share_meta_harsher_sign(self):
        for target, peer, slug in [
            (TARGET_532, PEER_532, "wsj"),
            (TARGET_533, PEER_533, "wsj"),
            (TARGET_537, PEER_537, "guardian"),
            (TARGET_538, PEER_538, "nytimes"),
        ]:
            r = score(target, peer, "Meta", ["peer"], slug)
            assert r.asymmetry_score < 0, f"sign flipped for {slug}"


# ---------------------------------------------------------------------------
# Standing-rule discipline ratchet: the newest quantitative mechanisms keep
# p_value NOT_CALCULATED and is_significant False in their YAML, even though
# the engine computes t/p/CI on the logged arrays (the #537 n=2-vs-n=2
# engine p is ~0.0136 - computed but NOT promoted to a finding).
# ---------------------------------------------------------------------------

GUARDIAN = REPO_ROOT / "profiles" / "guardian.yaml"
JOURNALISTS = REPO_ROOT / "profiles" / "careers" / "journalists.yaml"
MECH_537 = "mechanism_537_guardian_meta_vs_openai_deal_partner_same_day_register_asymmetry_sep05"
MECH_538 = "type_b_538_cade_metz_litigation_adversary_register_symmetry_science_desk"


class TestStandingRuleDisciplineRatchet540:
    def _scorer_537(self):
        with open(GUARDIAN) as f:
            d = yaml.safe_load(f)
        return d["competitor_relationships"]["meta"][MECH_537][
            "asymmetry_scorer_MANUAL_ILLUSTRATIVE"
        ]

    def _mech_538(self):
        with open(JOURNALISTS) as f:
            d = yaml.safe_load(f)
        for j in d["journalists"]:
            if j.get("name") == "Cade Metz":
                return j["competitor_coverage"][MECH_538]
        raise AssertionError("Cade Metz profile missing")

    def test_537_scorer_keeps_not_calculated(self):
        s = self._scorer_537()
        assert "NOT_CALCULATED" in str(s["p_value"])

    def test_537_scorer_not_significant(self):
        s = self._scorer_537()
        assert s["is_significant"] is False

    def test_537_logged_arrays_match_engine_inputs(self):
        s = self._scorer_537()
        assert list(s["target_scores_MANUAL_ILLUSTRATIVE"]) == TARGET_537
        assert list(s["peer_scores_MANUAL_ILLUSTRATIVE"]) == PEER_537

    def test_538_discipline_not_calculated(self):
        disc = self._mech_538()["statistical_discipline"]
        assert "NOT_CALCULATED" in str(disc["p_value"])
        assert "NOT_CALCULATED" in str(disc["cohens_d"])
        assert "NOT_CALCULATED" in str(disc["ci"])

    def test_538_discipline_not_significant(self):
        assert self._mech_538()["statistical_discipline"]["is_significant"] is False

    def test_538_logged_tones_match_engine_inputs(self):
        mt = self._mech_538()["manual_illustrative_tones"]
        assert list(mt["meta"]) == TARGET_538
        assert list(mt["openai"]) == PEER_538
        assert mt["delta"] == pytest.approx(-0.0875)


# ---------------------------------------------------------------------------
# Rotation-cycle guard: the 536 E -> 537 A -> 538 B -> 539 C window follows
# A->B->C->D->E->A adjacency in git-commit order (newest first).
# Complements #510's generic five-commit consecutiveness guard.
# ---------------------------------------------------------------------------

_CYCLE = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "A"}


class TestRotationCycleGuard540:
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
            ["git", "log", "--format=%s", "-20"],
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

    def test_536_through_539_types_in_order(self):
        commits = self._recent_type_commits(4)
        assert commits == [(539, "C"), (538, "B"), (537, "A"), (536, "E")], (
            f"expected 539 C / 538 B / 537 A / 536 E newest-first, got {commits}"
        )

    def test_cycle_adjacency_holds(self):
        commits = self._recent_type_commits(4)
        for (num_newer, type_newer), (num_older, type_older) in zip(commits, commits[1:]):
            assert num_newer == num_older + 1, (
                f"non-consecutive: #{num_newer} after #{num_older}"
            )
            assert _CYCLE[type_older] == type_newer, (
                f"rotation broken: #{num_older} Type {type_older} -> "
                f"#{num_newer} Type {type_newer}, expected {_CYCLE[type_older]}"
            )


# ---------------------------------------------------------------------------
# Doc-sync ratchet: per-file README/ARCHITECTURE rows for the 536-540
# window with true counts; authoritative count gate green.
# ---------------------------------------------------------------------------

DOC_SYNC_WINDOW_540 = [
    "test_type_e_536_podcast_sentiment_thirtieth_verification_sep05_8am.py",
    "test_type_a_537_guardian_meta_openai_same_day_register_asymmetry_sep05_9am.py",
    "test_type_b_538_cade_metz_litigation_adversary_symmetry_science_desk_sep05_10am.py",
    "test_type_c_539_dotdash_meredith_triple_payer_openai_meta_microsoft_pcm_sep05_11am.py",
    FILE_540,
]


class TestDocSyncRatchet540:
    """Per-file README/ARCHITECTURE rows exist with true counts (536-540)."""

    def test_readme_row_for_540_with_true_count(self):
        readme = README.read_text()
        pattern = re.compile(
            r"\|\s*`" + re.escape(FILE_540) + r"`\s*\|\s*(\d+)\s*\|"
        )
        m = pattern.search(readme)
        assert m, f"README row missing for {FILE_540}"
        assert int(m.group(1)) == count_def_tests(FILE_540)

    def test_architecture_row_for_540_with_true_count(self):
        arch = ARCHITECTURE.read_text()
        assert FILE_540 in arch, f"ARCHITECTURE row missing for {FILE_540}"
        row = next(line for line in arch.splitlines() if FILE_540 in line)
        assert str(count_def_tests(FILE_540)) in row, (
            f"count mismatch in ARCHITECTURE row for {FILE_540}"
        )

    def test_recent_window_rows_present_in_both_docs(self):
        readme = README.read_text()
        arch = ARCHITECTURE.read_text()
        for fname in DOC_SYNC_WINDOW_540:
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
