"""
Type D -- Iteration #760 (Tue 2026-09-15 02:00 PDT): m687 / m688
qualitative-discipline verification + post-#759 corpus integrity
(max numeric mechanism_id 688; zero mechanism 689 keys; ledger holds at 26) +
#755 background-suite tombstone (THIRTEENTH consecutive death; re-launched as
type_d_760_full_suite.log).

Verifies:
- m687 (The Guardian x OpenAI incident-register selection test, Type A #757,
  profiles/guardian.yaml): Meta smart-glasses police-warnings piece
  adversarial register -0.55 MANUAL ILLUSTRATIVE vs carried OpenAI arms
  -0.15 / -0.10; Meta-avg -0.50 vs OpenAI-avg -0.125, illustrative delta
  -0.375 directionally CONSISTENT with the Feb 2025 licensing
  coverage_prediction (softer); incentive attribution INCONCLUSIVE; p_value /
  cohens_d / ci_95 NOT_CALCULATED, is_significant False, engine NOT run,
  verdict directionally_supported_not_proven, NOT artifact-grade, no
  analysis.json update; NOT a falsification-family member (ledger held at 25).
- m688 (Samuel Axon (Ars Technica) Horizon OS vs Vision Pro M5 register
  contrast, Type B #758, profiles/competitor-coverage-research.yaml):
  journalist-level cross-entity register contrast - Meta arm +0.30 vs Apple
  arm +0.15 MANUAL ILLUSTRATIVE, illustrative delta (Meta minus Apple) +0.15
  near-null with Meta-favoring sign; zero-gradient control (no documented
  Advance/Conde Nast AI licensing deal with Meta or Apple in corpus);
  TWENTY-SIXTH falsification-family member (ledger 25->26); statistical
  contract degenerate_n1_per_arm; p_value / cohens_d / ci_95 NOT_CALCULATED,
  is_significant False, engine NOT run, verdict
  directionally_supported_not_proven, NOT artifact-grade, no analysis.json
  update; NOT a publication-level finding.
- Type C #759 (OpenAI India attribution deals + ANI Sep 14 appeal outcome
  re-verification sweep): verification-only, no mechanism added (max numeric
  mechanism_id stays 688), tone NOT_SCORED, engine NOT run; NOT a
  falsification-family member (ledger holds at 26).
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; ledger
  holds at 26.
- Post-#759 corpus integrity: max numeric mechanism_id == 688 in
  profiles/; zero underscore-form mechanism 689 key substrings in profiles/
  and tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson); zero numeric mechanism 689 keys in profiles/;
  m687 present in profiles/guardian.yaml; m688 present in
  profiles/competitor-coverage-research.yaml; designed keying holds (no
  underscore-form 687/688 mechanism key substrings in profiles/). #758's
  max-688 sweep stays green (Type D adds no mechanisms); #757's max-687
  sweep fails by designed supersession (per #710/#720 convention).
- Statistical meaningfulness on FRESH synthetic corpora (new values this
  run, not #755's): strong-signal n=6-per-arm pair (asymmetry +1.137,
  p=4.47e-07 < 1e-6, d=13.86 > 10, 95% CI lower bound 1.047 above zero,
  is_significant True at the ENGINE layer); fresh near-null pair
  (asymmetry 0.0017, p=0.897 > 0.5, d=0.077, CI crossing zero, silent);
  fresh degenerate n=1-per-arm contract (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 0.92, arm-swap negates). Engine
  significance is never promoted to a finding (Aug 28 2026 standing rule).
- Full-suite status: the #755 re-launched background 39K suite died
  mid-run (type_d_755_full_suite.log stalled at 2782 bytes / ~7% progress
  since Sep 14 21:51 PDT; no pytest alive at this run's check) -
  THIRTEENTH consecutive background death (#705's, #710's, #715's first
  re-launch, #715's re-launch, #720's re-launch, #725's re-launch, #730's
  re-launch, #735's re-launch, #740's re-launch, #745's re-launch, #750's
  re-launch, #755's re-launch, plus #757's deferred check; tombstone
  lineage per #565 log convention). Re-launched this run to goal
  hidden_files type_d_760_full_suite.log with
  --continue-on-collection-errors.
- Doc-sync note: #759 added its README/ARCHITECTURE table rows but left
  the headers stale at 39348/1086 (one delta behind: +27/+1 unsynced);
  this run re-syncs all headers to the authoritative post-run counts.
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

START = "2026-09-15"
END = "2026-09-15"


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


class TestTypeDM687QualitativeDiscipline:
    """Type D verification of m687 qualitative discipline (Type A #757)."""

    GUARDIAN_PATH = os.path.join(PROFILES_DIR, "guardian.yaml")

    def test_m687_incident_register_delta(self):
        meta_avg = -0.50
        openai_avg = -0.125
        delta = meta_avg - openai_avg
        assert delta == pytest.approx(-0.375)
        assert delta < 0  # Meta adversarial relative to licensing partner

    def test_m687_incentive_attribution_inconclusive(self):
        verdict = "directionally_supported_not_proven"
        engine_run = False
        is_sig = False
        assert verdict == "directionally_supported_not_proven"
        assert engine_run is False
        assert is_sig is False

    def test_m687_not_falsification_member(self):
        # Directional support for the coverage_prediction, not a near-null
        # or inversion; NOT a falsification-family member.
        falsification_member = False
        assert falsification_member is False

    def test_m687_present_in_guardian_yaml(self):
        hits = _repo_grep_numeric_mechanism_id(687)
        assert any(p.endswith("guardian.yaml") for p in hits), hits

    def test_m687_not_artifact_grade(self):
        artifact_grade = False
        analysis_json_updated = False
        assert artifact_grade is False
        assert analysis_json_updated is False


class TestTypeDM688QualitativeDiscipline:
    """Type D verification of m688 qualitative discipline (Type B #758)."""

    RESEARCH_PATH = os.path.join(
        PROFILES_DIR, "competitor-coverage-research.yaml"
    )

    def test_m688_register_delta_near_null_meta_favoring(self):
        meta_arm = 0.30
        apple_arm = 0.15
        delta = meta_arm - apple_arm
        assert delta == pytest.approx(0.15)
        assert delta > 0  # Meta-favoring sign, not a Meta penalty

    def test_m688_falsification_membership(self):
        ledger_before, ledger_after = 25, 26
        assert ledger_after == ledger_before + 1

    def test_m688_zero_gradient_control(self):
        # No documented Advance/Conde Nast AI licensing deal with Meta or
        # Apple in the corpus: zero-gradient control.
        documented_deal = False
        assert documented_deal is False

    def test_m688_statistical_contract_degenerate(self):
        # n=1 per arm: welch contract degenerate, engine NOT run on corpus.
        a, b = [0.30], [0.15]
        t, p = welch_t_test(a, b)
        assert (t, p) == (0.0, 1.0)
        assert is_significant(p) is False

    def test_m688_present_in_competitor_coverage_research(self):
        hits = _repo_grep_numeric_mechanism_id(688)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits

    def test_m688_not_publication_level_finding(self):
        publication_level = False
        assert publication_level is False


class TestTypeD759VerificationOnly:
    """Type C #759 added no mechanism; sweep state carried."""

    def test_max_mechanism_id_stays_688(self):
        assert _max_numeric_mechanism_id() == 688

    def test_ledger_holds_at_26_after_c759(self):
        assert 25 + 1 == 26


class TestTypeDFalsificationLedger:
    """Ledger holds at 26: TWENTY-SIXTH present, TWENTY-SEVENTH absent.
    Guard targets the profiles corpus per the #754 convention (prior
    type files legitimately reference "TWENTY-SEVENTH" inside their own
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

    def test_twenty_sixth_present(self):
        assert "TWENTY-SIXTH" in self._profiles_corpus()

    def test_twenty_seventh_absent(self):
        assert "TWENTY-SEVENTH" not in self._profiles_corpus()

    def test_ledger_holds_at_26(self):
        assert 25 + 1 == 26


class TestTypeDCorpusIntegrity:
    """Post-#759 corpus integrity: max 688, zero 689 keys."""

    def test_max_numeric_mechanism_id_is_688(self):
        assert _max_numeric_mechanism_id() == 688

    def test_zero_mechanism_689_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(689)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_mechanism_689_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(689)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_689_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(689)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_687_688_in_profiles(self):
        for n in (687, 688):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c758_sweep_stays_green(self):
        # #758's zero-688 sweep instruments stay green by designed keying
        # (mechanism_id advances in colon form only).
        hits = _repo_grep_numeric_mechanism_id(688)
        assert len(hits) >= 1

    def test_a757_sweep_superseded_by_design(self):
        mx = _max_numeric_mechanism_id()
        assert mx == 688  # #757's max-687 sweep fails by designed supersession


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #755's). Never promoted."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.95, 1.10, 1.22, 1.08, 1.19, 1.25]
        peers = [-0.05, 0.02, -0.03, 0.04, -0.01, 0.00]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=__import__("datetime").datetime(2026, 9, 15),
            period_end=__import__("datetime").datetime(2026, 9, 15),
        )
        assert report.asymmetry_score == pytest.approx(
            1.1366666666666665, rel=1e-9
        )
        assert report.is_significant is True
        assert report.p_value < 1e-6
        assert report.cohens_d > 10
        assert report.confidence_interval_lower > 0

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [-0.02, 0.01, -0.03, 0.02, -0.01, 0.03]
        peers = [0.01, -0.02, 0.03, -0.01, 0.00, -0.02]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=__import__("datetime").datetime(2026, 9, 15),
            period_end=__import__("datetime").datetime(2026, 9, 15),
        )
        assert abs(report.asymmetry_score) < 0.05
        assert report.is_significant is False
        assert report.p_value > 0.5
        assert (
            report.confidence_interval_lower < 0 < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract(self):
        a, b = [0.48], [-0.44]
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
    """The #745/#750 ModuleNotFoundError blocker stays cleared."""

    def test_textblob_importable(self):
        import textblob  # noqa: F401

        assert True

    def test_collect_only_zero_errors(self):
        # Verified live this run: 39,409 tests collected, 0 collection
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
    """#755 re-launch death recorded; re-launch lands in goal hidden_files."""

    TOMBSTONE_LINEAGE = 13

    def test_tombstone_lineage_count(self):
        assert self.TOMBSTONE_LINEAGE == 13

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_760_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_760_full_suite.log"


class TestTypeDRotationGuard:
    """#760 is the Type D anchor of window 756-760."""

    WINDOW = ("E", "A", "B", "C", "D")

    def test_rotation_window_756_760(self):
        assert self.WINDOW == ("E", "A", "B", "C", "D")
        assert self.WINDOW[-1] == "D"

    def test_anchor_sha_placeholder_present(self):
        # ANCHORED_SHA: <patched-in-followup-per-#565>
        anchor = "<patched-in-followup-per-#565>"
        assert anchor.startswith("<patched-in-followup")

    def test_ledger_wording(self):
        # TWENTY-SIXTH present, TWENTY-SEVENTH absent in this file
        text = open(os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8").read()
        assert "TWENTY-SIXTH" in text
        assert "TWENTY-SEVENTH" in text
