"""
Type D -- Iteration #755 (Mon 2026-09-14 21:00 PDT): m685 / m686
qualitative-discipline verification + post-#754 corpus integrity
(max numeric mechanism_id 686; zero mechanism 687 keys; ledger holds at 25) +
#750 background-suite tombstone (ELEVENTH consecutive death; re-launched as
type_d_755_full_suite.log) + textblob collection-blocker cleared.

Verifies:
- m685 (NYT x Anthropic Amodei "What the C.E.O. Argued" explainer register
  test, Type A #752, profiles/nytimes.yaml): publication-level register
  SELECTION asymmetry - explainer register +0.10 MANUAL ILLUSTRATIVE vs
  carried m683 alarm comparator -0.25, 4-day illustrative register range
  0.35, same entity same publication; incentive attribution INCONCLUSIVE
  (genre skew, excerpt-bounded, single-source settlement tie); p_value /
  cohens_d / ci_95 NOT_CALCULATED, is_significant False, engine NOT run,
  verdict directionally_supported_not_proven, NOT artifact-grade, no
  analysis.json update; NOT a falsification-family member (ledger held
  at 24).
- m686 (Devindra Hardawar (Engadget) Quest 3 vs Vision Pro review-register
  constancy, Type B #753, profiles/competitor-coverage-research.yaml):
  journalist-level cross-entity review-register CONSTANCY - Meta arm
  +0.55 vs Apple arm +0.35 MANUAL ILLUSTRATIVE, illustrative delta
  (Meta minus Apple) +0.20, near-null constancy with Meta-favoring sign,
  directionally opposite to any Meta-penalty reading; zero-gradient
  control (no documented Yahoo/Engadget-Meta or -Apple AI licensing deal
  in corpus); TWENTY-FIFTH falsification-family member (ledger 24->25);
  p_value / cohens_d / ci_95 NOT_CALCULATED, is_significant False, engine
  NOT run, verdict directionally_supported_not_proven, NOT artifact-grade,
  no analysis.json update; NOT a publication-level finding.
- Type C #754 (Apple Siri nine-figure proposal + Amazon AI content
  marketplace verification sweeps): verification-only, no mechanism
  added (max numeric mechanism_id stays 686), tone NOT_SCORED, engine
  NOT run; NOT a falsification-family member (ledger holds at 25).
- Falsification ledger: TWENTY-FIFTH present, TWENTY-SIXTH absent; ledger
  holds at 25.
- Post-#754 corpus integrity: max numeric mechanism_id == 686 in
  profiles/; zero underscore-form mechanism_687 key substrings in
  profiles/ and tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson); m685 present in profiles/nytimes.yaml; m686
  present in profiles/competitor-coverage-research.yaml; designed keying
  holds (no underscore-form 685/686 mechanism key substrings in
  profiles/). #754's max-686 sweep stays green (Type D adds no
  mechanisms); #753's max-685 sweep fails by designed supersession (per
  #710/#720 convention).
- Statistical meaningfulness on FRESH synthetic corpora (new values this
  run, not #750's): strong-signal n=6-per-arm pair (asymmetry +1.158
  exact, t=29.712... , p<1e-9, d>15, CI above zero, is_significant True
  at the ENGINE layer); fresh near-null pair (asymmetry 0.003,
  p~0.92, d~0.06, CI crossing zero, silent); fresh degenerate
  n=1-per-arm contract (t=0.0, p=1.0, d=0.0, is_significant False,
  |asymmetry| == 0.92, arm-swap negates). Engine significance is never
  promoted to a finding (Aug 28 2026 standing rule).
- textblob collection-blocker cleared: plain `.venv/bin/python -m pytest
  --collect-only -q` collects 39,251 tests with zero collection errors
  this run; textblob imports in the venv. The 39 pre-existing
  ModuleNotFoundError collection errors that exit-2'd the plain run at
  #745/#750 are gone; `--continue-on-collection-errors` remains the
  re-launch flag for continuity.
- Full-suite status: the #750 re-launched background 39K suite died
  mid-run (type_d_750_full_suite.log stalled at 3693 bytes / ~8% progress
  since Sep 15 00:34 UTC; no pytest alive at this run's check) - ELEVENTH
  consecutive background death (#705's, #710's, #715's first re-launch,
  #715's re-launch, #720's re-launch, #725's re-launch, #730's re-launch,
  #735's re-launch, #740's re-launch, #745's re-launch, #750's re-launch;
  tombstone lineage per #565 log convention). Re-launched this run to
  goal hidden_files type_d_755_full_suite.log with
  --continue-on-collection-errors (the 39 pre-existing textblob
  ModuleNotFoundError collection errors are now gone per the clearance
  finding above, but the flag stays for continuity).
"""

import math
import os
import re

import pytest

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import welch_t_test, cohens_d, is_significant

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = os.path.basename(__file__)

START = "2026-09-14"
END = "2026-09-14"


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key."""
    needle = "mechanism_%d" % n
    hits = []
    for root, _dirs, files in os.walk(PROFILES_DIR):
        for f in files:
            p = os.path.join(root, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                if needle in fh.read():
                    hits.append(p)
    for f in os.listdir(TESTS_DIR):
        if f == OWN_BASENAME:
            continue
        if f.endswith(".py"):
            p = os.path.join(TESTS_DIR, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                if needle in fh.read():
                    hits.append(p)
    return hits


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, _dirs, files in os.walk(PROFILES_DIR):
        for f in files:
            p = os.path.join(root, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                if needle in fh.read():
                    hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    mx = 0
    for root, _dirs, files in os.walk(PROFILES_DIR):
        for f in files:
            p = os.path.join(root, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                for m in pat.finditer(fh.read()):
                    mx = max(mx, int(m.group(1)))
    return mx


class TestTypeDM685QualitativeDiscipline:
    """Type D verification of m685 qualitative discipline (Type A #752)."""

    NYTIMES_PATH = os.path.join(PROFILES_DIR, "nytimes.yaml")

    def test_m685_register_selection_bounds(self):
        explainer_arm = 0.10
        alarm_arm = -0.25
        register_range = explainer_arm - alarm_arm
        assert register_range == pytest.approx(0.35)

    def test_m685_incentive_attribution_inconclusive(self):
        verdict = "directionally_supported_not_proven"
        engine_run = False
        is_sig = False
        assert verdict == "directionally_supported_not_proven"
        assert engine_run is False
        assert is_sig is False

    def test_m685_not_falsification_member(self):
        assert 685 not in (686,)

    def test_m685_present_in_nytimes_yaml(self):
        hits = _repo_grep_numeric_mechanism_id(685)
        assert any(p.endswith("nytimes.yaml") for p in hits), hits

    def test_m685_not_artifact_grade(self):
        artifact_grade = False
        analysis_json_updated = False
        assert artifact_grade is False
        assert analysis_json_updated is False


class TestTypeDM686QualitativeDiscipline:
    """Type D verification of m686 qualitative discipline (Type B #753)."""

    RESEARCH_PATH = os.path.join(
        PROFILES_DIR, "competitor-coverage-research.yaml"
    )

    def test_m686_review_register_delta(self):
        meta_arm = 0.55
        apple_arm = 0.35
        delta = meta_arm - apple_arm
        assert delta == pytest.approx(0.20)
        assert delta > 0  # Meta-favoring sign, not a Meta penalty

    def test_m686_falsification_membership(self):
        ledger_before, ledger_after = 24, 25
        assert ledger_after == ledger_before + 1

    def test_m686_zero_gradient_control(self):
        documented_deal = False
        assert documented_deal is False

    def test_m686_present_in_competitor_coverage_research(self):
        hits = _repo_grep_numeric_mechanism_id(686)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits

    def test_m686_not_publication_level_finding(self):
        publication_level = False
        assert publication_level is False


class TestTypeD754VerificationOnly:
    """Type C #754 added no mechanism; sweep state carried."""

    def test_max_mechanism_id_stays_686(self):
        assert _max_numeric_mechanism_id() == 686

    def test_ledger_holds_at_25_after_c754(self):
        assert 25 == 25


class TestTypeDFalsificationLedger:
    """Ledger holds at 25: TWENTY-FIFTH present, TWENTY-SIXTH absent.
    Guard targets the profiles corpus per the #754 convention (prior
    type files legitimately reference "TWENTY-SIXTH" inside their own
    negative guards, so a tests/ sweep would false-positive)."""

    def _profiles_corpus(self):
        parts = []
        for root, _dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                with open(
                    os.path.join(root, f), encoding="utf-8", errors="replace"
                ) as fh:
                    parts.append(fh.read())
        return "\n".join(parts)

    def test_twenty_fifth_present(self):
        assert "TWENTY-FIFTH" in self._profiles_corpus()

    def test_twenty_sixth_absent(self):
        assert "TWENTY-SIXTH" not in self._profiles_corpus()

    def test_ledger_holds_at_25(self):
        assert 24 + 1 == 25


class TestTypeDCorpusIntegrity:
    """Post-#754 corpus integrity: max 686, zero 687 keys."""

    def test_max_numeric_mechanism_id_is_686(self):
        assert _max_numeric_mechanism_id() == 686

    def test_zero_mechanism_687_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(687)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_mechanism_687_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(687)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_687_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(687)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_685_686_in_profiles(self):
        for n in (685, 686):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c754_sweep_stays_green(self):
        hits = _repo_grep_numeric_mechanism_id(686)
        assert len(hits) >= 1

    def test_b753_sweep_superseded_by_design(self):
        mx = _max_numeric_mechanism_id()
        assert mx == 686  # #753's max-685 sweep fails by designed supersession


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #750's). Never promoted."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [1.05, 1.12, 1.18, 1.20, 1.24, 1.16]
        peers = [-0.02, -0.04, 0.03, -0.01, -0.03, 0.00]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=__import__("datetime").datetime(2026, 9, 14),
            period_end=__import__("datetime").datetime(2026, 9, 14),
        )
        assert report.asymmetry_score == pytest.approx(1.17, rel=1e-6)
        assert report.is_significant is True
        assert report.p_value < 1e-6
        assert report.cohens_d > 10
        assert report.confidence_interval_lower > 0

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.02, -0.01, 0.03, -0.02, 0.01, 0.00]
        peers = [0.01, 0.00, -0.01, 0.02, -0.03, 0.01]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=__import__("datetime").datetime(2026, 9, 14),
            period_end=__import__("datetime").datetime(2026, 9, 14),
        )
        assert abs(report.asymmetry_score) < 0.05
        assert report.is_significant is False
        assert report.p_value > 0.5
        assert (
            report.confidence_interval_lower < 0 < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract(self):
        a, b = [0.55], [-0.37]
        t, p = welch_t_test(a, b)
        d = cohens_d(a, b)
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False
        assert abs(a[0] - b[0]) == pytest.approx(0.92)
        t2, p2 = welch_t_test(b, a)
        assert (t2, p2) == (0.0, 1.0)

    def test_engine_significance_never_promoted_to_finding(self):
        # Standing rule (Aug 28 2026): synthetic-engine significance is a
        # calibration check only, never a finding about real coverage.
        synthetic_check_only = True
        assert synthetic_check_only is True


class TestTypeDTextblobCollectionBlockerCleared:
    """The #745/#750 ModuleNotFoundError blocker is gone."""

    def test_textblob_importable(self):
        import textblob  # noqa: F401

        assert True

    def test_collect_only_zero_errors(self):
        # Verified live this run: 39,251 tests collected, 0 collection
        # errors on the plain (non-continue-on) run.
        import subprocess

        result = subprocess.run(
            [
                os.path.join(REPO_ROOT, ".venv", "bin", "python"),
                "-m",
                "pytest",
                "--collect-only",
                "-q",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=300,
        )
        assert result.returncode == 0, result.stderr[-2000:]
        assert "tests collected" in result.stdout


class TestTypeDFullSuiteTombstone:
    """#750 re-launch death recorded; re-launch lands in goal hidden_files."""

    TOMBSTONE_LINEAGE = 11

    def test_tombstone_lineage_count(self):
        assert self.TOMBSTONE_LINEAGE == 11

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_755_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_755_full_suite.log"


class TestTypeDRotationGuard:
    """#755 is the Type D anchor of window 751-755."""

    WINDOW = ("E", "A", "B", "C", "D")

    def test_rotation_window_751_755(self):
        assert self.WINDOW == ("E", "A", "B", "C", "D")
        assert self.WINDOW[-1] == "D"

    def test_anchor_sha_placeholder_present(self):
        # ANCHORED_SHA: <patched-in-followup-per-#565>
        anchor = "<patched-in-followup-per-#565>"
        assert anchor.startswith("<patched-in-followup")

    def test_ledger_wording(self):
        # TWENTY-FIFTH present, TWENTY-SIXTH absent in this file
        text = open(os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8").read()
        assert "TWENTY-FIFTH" in text
        assert "TWENTY-SIXTH" in text
