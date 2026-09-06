"""Type D #545 (2026-09-05 17:00 PDT): scorer cross-mechanism consistency extended to
#542/#543, standing-rule discipline ratchet, rotation-cycle guard for the
541-544 commit window, 541-545 doc-sync ratchet.

Context: the Aug 28 2026 standing rule says MANUAL ILLUSTRATIVE deltas are NOT
empirical - p_value NOT_CALCULATED, is_significant False in the mechanism YAML,
correlation not causation, no artifact-grade claims. The asymmetry engine
(calculate_asymmetry) still computes t/p/CI on the logged arrays, and its
MEAN-DIFFERENCE arithmetic must reproduce the logged manual delta (engine-drift
detection). The engine's own significance output is computed but deliberately
NOT promoted to a finding for illustrative inputs - this file pins that
separation for the two newest quantitative mechanisms:

- #542 (Type A, BI x Google chase/deficit register vs Anthropic aspirational,
  Sep 5 14:00 PDT): Google [-0.20, +0.05] avg -0.075 vs Anthropic [+0.12]
  avg +0.12, logged delta -0.195 (target entity Google, n=2 vs n=1). This is
  the first engine-checked mechanism whose target entity is a Meta competitor
  rather than Meta itself; the delta sign convention (target-minus-peer,
  negative = target harsher) is unchanged.
- #543 (Type B, Roose Hard Fork late-window matched-episode framing,
  Sep 5 15:00 PDT): Meta/Zuckerberg [-0.50, -0.35] avg -0.425 vs OpenAI
  [+0.10] avg +0.10, logged delta -0.525 (n=2 vs n=1). The Hugging Face
  control (+0.25) is excluded from the delta arithmetic - the logged delta
  equals meta_avg minus openai_avg only.
- #544 (Type C, Vox Media x Microsoft PCM dual-payer, Sep 5 16:00 PDT):
  qualitative - no asymmetry_scorer section is logged (statistical_discipline
  carries tone_scores NOT_SCORED); scorer consistency explicitly does NOT
  apply, mirroring the #539 boundary pinned in #540.
- #541 (Type E, podcast sentiment 31st verification cycle, Sep 5 13:00 PDT):
  monitoring-only, no quantitative mechanism - no scorer extension.

Also: a rotation-cycle guard pins that the 541 E -> 542 A -> 543 B -> 544 C
commit window follows A->B->C->D->E->A adjacency in git-commit order (newest
first), extending #540's 536-539 window guard; and the doc-sync ratchet
extends the README/ARCHITECTURE per-file window to 541-545 with the
authoritative count_stats.py --check gate.

Novelty: zero test_type_d_545 files on disk before this run (glob verified);
no #545 commit title in git log (grep verified); scorer consistency has never
covered #542/#543 (repo grep for 542/543 in scorer-consistency tests returned
only their own mechanism files); the 541-544 rotation window was never
guarded; the 536-540 doc-sync window (from #540) is extended, not duplicated.
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

FILE_545 = "test_type_d_545_scorer_consistency_542_543_rotation_doc_sync_sep05_5pm.py"

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


class TestIteration545Metadata:
    def test_docstring_ids(self):
        assert "Type D #545" in __doc__
        assert "2026-09-05 17:00 PDT" in __doc__

    def test_rotation_c_to_d(self):
        # Previous iteration #544 was Type C (commit 5bc92c1); this run is D.
        assert "C->D" in __doc__.replace(" ", "") or "C -> D" in __doc__ or \
            "rotation" in __doc__.lower()

    def test_filename_convention(self):
        assert os.path.basename(__file__) == FILE_545
        assert FILE_545.startswith("test_type_d_545_")
        assert FILE_545.endswith("_sep05_5pm.py")

    def test_iteration_log_entry_present(self):
        text = LOG.read_text(encoding="utf-8")
        assert re.search(r"^#545 Type D", text, re.MULTILINE), \
            "iteration-log.md missing newest-first #545 Type D heading"


# ---------------------------------------------------------------------------
# Scorer cross-mechanism consistency: engine mean-delta arithmetic reproduces
# the logged MANUAL ILLUSTRATIVE deltas for #542 and #543 (abs tolerance
# 1e-4, per #530 convention); #537/#538/#532/#533 re-locked; #544
# qualitative boundary pinned.
# ---------------------------------------------------------------------------

TARGET_542 = [-0.20, 0.05]
PEER_542 = [0.12]

TARGET_543 = [-0.50, -0.35]
PEER_543 = [0.10]
CONTROL_543 = [0.25]

TARGET_537 = [-0.45, -0.40]
PEER_537 = [-0.15, -0.10]
TARGET_538 = [-0.05, -0.25]
PEER_538 = [-0.05, -0.05, 0.0, -0.15]
TARGET_532 = [-0.30, -0.25]
PEER_532 = [-0.15, -0.25]
TARGET_533 = [-0.35]
PEER_533 = [-0.30]


class TestScorerCrossMechanismConsistency545:
    def test_542_google_vs_anthropic_delta_reproduced(self):
        r = score(TARGET_542, PEER_542, "Google", ["Anthropic"],
                  "business-insider")
        assert r.asymmetry_score == pytest.approx(-0.195, abs=1e-4)

    def test_543_roose_delta_reproduced(self):
        r = score(TARGET_543, PEER_543, "Meta", ["OpenAI"], "nytimes")
        assert r.asymmetry_score == pytest.approx(-0.525, abs=1e-4)

    def test_543_control_excluded_from_delta(self):
        # The Hugging Face control (+0.25) is an open-source falsification
        # control, not a delta input: the logged delta equals meta_avg minus
        # openai_avg with the control excluded.
        r = score(TARGET_543, PEER_543, "Meta", ["OpenAI"], "nytimes")
        assert abs(r.asymmetry_score - (sum(TARGET_543) / 2
                                       - sum(PEER_543) / 1)) < 1e-9
        with_control = calculate_asymmetry(
            target_scores=TARGET_543 + CONTROL_543,
            peer_scores=PEER_543,
            target_entity="Meta",
            peer_entities=["OpenAI"],
            publication_slug="nytimes",
            period_start=PERIOD[0],
            period_end=PERIOD[1],
        )
        assert with_control.asymmetry_score != pytest.approx(-0.525), \
            "control must move the delta - if identical, exclusion untestable"

    def test_542_google_harsher_sign_target_entity_google(self):
        # #542 is the first engine-checked mechanism with a competitor as
        # the target entity; sign convention (target-minus-peer) unchanged.
        r = score(TARGET_542, PEER_542, "Google", ["Anthropic"],
                  "business-insider")
        assert r.target_entity == "Google"
        assert r.asymmetry_score < 0

    def test_537_dual_deal_symmetry_relock(self):
        # The engine DOES compute significance True on the #537 n=2v2
        # well-separated arrays (p~0.0136) - this is engine arithmetic, not
        # a finding. The standing rule keeps the mechanism's own YAML at
        # is_significant False and NOT_CALCULATED; see
        # TestStandingRuleDisciplineRatchet545 for the pinned separation.
        r = score(TARGET_537, PEER_537, "Meta", ["OpenAI"], "guardian")
        assert r.asymmetry_score == pytest.approx(-0.30, abs=1e-4)
        assert r.is_significant is True

    def test_538_metz_symmetry_relock(self):
        r = score(TARGET_538, PEER_538, "Meta", ["OpenAI"], "nytimes")
        assert r.asymmetry_score == pytest.approx(-0.0875, abs=1e-4)
        assert r.is_significant is False

    def test_532_relock(self):
        r = score(TARGET_532, PEER_532, "Meta", ["OpenAI"], "wsj")
        assert r.asymmetry_score == pytest.approx(-0.075, abs=1e-4)
        assert r.is_significant is False

    def test_533_relock(self):
        r = score(TARGET_533, PEER_533, "Meta", ["OpenAI"], "wsj")
        assert r.asymmetry_score == pytest.approx(-0.05, abs=1e-4)
        assert r.is_significant is False

    def test_544_qualitative_no_tone_delta(self):
        # #544 is Type C qualitative mapping: scorer consistency does not
        # apply. The mechanism block must carry NO asymmetry_scorer section
        # and its statistical_discipline must keep tone_scores NOT_SCORED.
        with open(REPO_ROOT / "profiles" / "competitor-entities.yaml") as f:
            entities = yaml.safe_load(f)
        mech = entities["entities"]["openai"][
            "mechanism_544_vox_media_microsoft_pcm_pay_per_use_leg"
        ]
        assert not any(k.startswith("asymmetry_scorer") for k in mech), \
            "qualitative #544 must not log an asymmetry scorer section"
        assert "NOT_SCORED" in str(mech.get("statistical_discipline", "")), \
            "qualitative #544 must keep tone_scores NOT_SCORED"

    def test_all_deltas_share_target_harsher_sign(self):
        for target, peer, entity, peers, slug in [
            (TARGET_532, PEER_532, "Meta", ["OpenAI"], "wsj"),
            (TARGET_533, PEER_533, "Meta", ["OpenAI"], "wsj"),
            (TARGET_537, PEER_537, "Meta", ["OpenAI"], "guardian"),
            (TARGET_538, PEER_538, "Meta", ["OpenAI"], "nytimes"),
            (TARGET_542, PEER_542, "Google", ["Anthropic"],
             "business-insider"),
            (TARGET_543, PEER_543, "Meta", ["OpenAI"], "nytimes"),
        ]:
            r = score(target, peer, entity, peers, slug)
            assert r.asymmetry_score < 0, f"sign flipped for {entity}/{slug}"


# ---------------------------------------------------------------------------
# Standing-rule discipline ratchet: the newest quantitative mechanisms keep
# p_value NOT_CALCULATED and is_significant False in their YAML, even though
# the engine computes t/p/CI on the logged arrays. Logged arrays byte-match
# the engine inputs used in the consistency tests.
# ---------------------------------------------------------------------------

BI = REPO_ROOT / "profiles" / "business-insider.yaml"
JOURNALISTS = REPO_ROOT / "profiles" / "careers" / "journalists.yaml"
MECH_542 = ("mechanism_542_bi_google_chase_register_vs_anthropic_aspirational"
            "_sep05")
MECH_543 = "type_b_543_kevin_roose_hard_fork_late_window_matched_framing"


class TestStandingRuleDisciplineRatchet545:
    def _scorer_542(self):
        with open(BI) as f:
            d = yaml.safe_load(f)
        return d["competitor_relationships"]["google"][MECH_542][
            "asymmetry_scorer_MANUAL_ILLUSTRATIVE"
        ]

    def _mech_543(self):
        with open(JOURNALISTS) as f:
            d = yaml.safe_load(f)
        for j in d["journalists"]:
            if j.get("name") == "Kevin Roose":
                return j["competitor_coverage"][MECH_543]
        raise AssertionError("Kevin Roose profile missing")

    def test_542_scorer_keeps_not_calculated(self):
        s = self._scorer_542()
        assert "NOT_CALCULATED" in str(s["p_value"])
        assert "NOT_CALCULATED" in str(s["cohens_d"])
        assert "NOT_CALCULATED" in str(s["ci"])

    def test_542_scorer_not_significant(self):
        assert self._scorer_542()["is_significant"] is False

    def test_542_logged_arrays_match_engine_inputs(self):
        s = self._scorer_542()
        assert list(s["google_scores"]) == TARGET_542
        assert list(s["anthropic_scores"]) == PEER_542
        assert s["delta"] == pytest.approx(-0.195)

    def test_542_google_vs_meta_delta_logged(self):
        # The secondary Google-vs-Meta comparison (-0.155) is recorded as a
        # logged field, not an engine input - it stays engine-unverified.
        assert self._scorer_542()["google_vs_meta_delta"] == pytest.approx(
            -0.155)

    def test_543_discipline_not_calculated(self):
        disc = self._mech_543()["statistical_discipline"]
        assert "NOT_CALCULATED" in str(disc["p_value"])
        assert "NOT_CALCULATED" in str(disc["cohens_d"])
        assert "NOT_CALCULATED" in str(disc["ci"])

    def test_543_discipline_not_significant(self):
        assert self._mech_543()["statistical_discipline"]["is_significant"] \
            is False

    def test_543_logged_tones_match_engine_inputs(self):
        mt = self._mech_543()["manual_illustrative_tones"]
        assert list(mt["meta"]) == TARGET_543
        assert list(mt["openai"]) == PEER_543
        assert list(mt["huggingface_control"]) == CONTROL_543
        assert mt["delta"] == pytest.approx(-0.525)


# ---------------------------------------------------------------------------
# Rotation-cycle guard: the 541 E -> 542 A -> 543 B -> 544 C window follows
# A->B->C->D->E->A adjacency in git-commit order (newest first).
# Extends #540's 536-539 window guard.
# ---------------------------------------------------------------------------

_CYCLE = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "A"}


class TestRotationCycleGuard545:
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

    def test_541_through_544_types_in_order(self):
        commits = self._recent_type_commits(4)
        assert commits == [(544, "C"), (543, "B"), (542, "A"), (541, "E")], (
            f"expected 544 C / 543 B / 542 A / 541 E newest-first, got "
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

    def test_540_precedes_541_as_d_before_e(self):
        commits = self._recent_type_commits(5)
        assert commits == [(544, "C"), (543, "B"), (542, "A"), (541, "E"),
                           (540, "D")], (
            f"expected 544 C / 543 B / 542 A / 541 E / 540 D newest-first, "
            f"got {commits}"
        )
        assert _CYCLE["D"] == "E", "D must precede E in the cycle"


# ---------------------------------------------------------------------------
# Doc-sync ratchet: per-file README/ARCHITECTURE rows for the 541-545
# window with true counts; authoritative count gate green.
# ---------------------------------------------------------------------------

DOC_SYNC_WINDOW_545 = [
    "test_type_e_541_podcast_sentiment_thirtyfirst_verification_sep05_1pm.py",
    "test_type_a_542_bi_google_chase_register_vs_anthropic_aspirational_sep05_2pm.py",
    "test_type_b_543_kevin_roose_hard_fork_late_window_matched_framing_sep05_3pm.py",
    "test_type_c_544_vox_media_microsoft_pcm_pay_per_use_leg_sep05_4pm.py",
    FILE_545,
]


class TestDocSyncRatchet545:
    """Per-file README/ARCHITECTURE rows exist with true counts (541-545)."""

    def test_readme_row_for_545_with_true_count(self):
        readme = README.read_text()
        pattern = re.compile(
            r"\|\s*`" + re.escape(FILE_545) + r"`\s*\|\s*(\d+)\s*\|"
        )
        m = pattern.search(readme)
        assert m, f"README row missing for {FILE_545}"
        assert int(m.group(1)) == count_def_tests(FILE_545)

    def test_architecture_row_for_545_with_true_count(self):
        arch = ARCHITECTURE.read_text()
        assert FILE_545 in arch, f"ARCHITECTURE row missing for {FILE_545}"
        row = next(line for line in arch.splitlines() if FILE_545 in line)
        assert str(count_def_tests(FILE_545)) in row, (
            f"count mismatch in ARCHITECTURE row for {FILE_545}"
        )

    def test_recent_window_rows_present_in_both_docs(self):
        readme = README.read_text()
        arch = ARCHITECTURE.read_text()
        for fname in DOC_SYNC_WINDOW_545:
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
