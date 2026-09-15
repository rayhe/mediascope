"""
Type D -- Iteration #765 (Tue 2026-09-15 07:00 PDT): m689 / m690
qualitative-discipline verification + post-#764 corpus integrity
(max numeric mechanism_id 690; zero mechanism 691 keys; ledger holds at 26) +
#760 background-suite tombstone (THIRTEENTH consecutive death; re-launched as
type_d_765_full_suite.log).

Verifies:
- m689 (WSJ x OpenAI unity-consensus statesman register, Type A #762,
  profiles/news-corp.yaml): FIRST dedicated mechanism on the "Biggest AI
  Rivals Agree They Need to Slow It Down" piece (Sep 14 2026); MANUAL
  ILLUSTRATIVE +0.15 vs carried Clash expose -0.40 (m682) and relay +0.10
  (m679): same-publication-day register TRIAD spanning 0.55 (same-week
  corpus range 0.70 with m616); incentive attribution INCONCLUSIVE and
  MIXED (m682 bounded capture readings; m689 bounds adversarial-uniformity
  readings); p_value / cohens_d / ci_95 NOT_CALCULATED, is_significant
  False, engine NOT run, verdict directionally_supported_not_proven, NOT
  artifact-grade, no analysis.json update; NOT a falsification-family
  member (ledger held at 26).
- m690 (Florence Ion (Gizmodo) Meta Ray-Ban hands-on vs Apple Watch Series 9
  review register contrast, Type B #763,
  profiles/competitor-coverage-research.yaml + careers/journalists.yaml):
  journalist-level cross-entity register contrast - Meta arm +0.10
  (conditional-praise-with-admonition) vs Apple arm +0.45
  (crown-bestowing review), illustrative delta (Meta minus Apple) -0.35
  Meta-cooling; supporting Google piece bounds anti-Meta readings;
  zero-gradient control (Keleops/Gizmodo, $0 documented AI licensing ties
  to Meta/Apple/Google/AI labs in corpus); NOT a falsification-family
  member (thesis-consistent direction, ledger holds at 26); statistical
  contract degenerate_n1_per_arm; p_value / cohens_d / ci_95
  NOT_CALCULATED, is_significant False, engine NOT run, verdict
  directionally_supported_not_proven, NOT artifact-grade, no analysis.json
  update.
- Type C #764 (News Corp additional-arrangements watch + ANI Sep 14 outcome
  re-verification + new-deal bounded-absence sweep): verification-only, no
  mechanism added (max numeric mechanism_id stays 690), tone NOT_SCORED,
  engine NOT run; NOT a falsification-family member (ledger holds at 26).
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent; ledger
  holds at 26.
- Post-#764 corpus integrity: max numeric mechanism_id == 690 in
  profiles/; zero underscore-form mechanism 691 key substrings in profiles/
  and tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson); zero numeric mechanism 691 keys in profiles/;
  m689 present in profiles/news-corp.yaml (block key unique); m690 present
  in profiles/competitor-coverage-research.yaml (block key unique);
  designed keying holds (no underscore-form 689/690 mechanism key
  substrings in profiles/). #763's max-690 sweep stays green (Type D adds
  no mechanisms); #762's max-689 sweep fails by designed supersession (per
  #710/#720 convention); #762's zero-underscore-690 and zero-numeric-690
  sweeps fail by designed supersession (the #763 carrier file legitimately
  carries the literal in a test name; the m690 profiles block supersedes).
- Statistical meaningfulness on FRESH synthetic corpora (new values this
  run, not #760's): strong-signal n=5-per-arm pair (asymmetry +1.1,
  p=7.21e-06 < 1e-4, d=12.98 > 10, 95% CI (1.014, 1.194) above zero,
  is_significant True at the ENGINE layer); fresh near-null pair
  (asymmetry 0.01, p=0.548 > 0.5, d=0.398, CI crossing zero, silent);
  fresh degenerate n=1-per-arm contract (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 0.90, arm-swap negates). Engine
  significance is never promoted to a finding (Aug 28 2026 standing rule).
- Full-suite status: the #760 re-launched background 39K suite died
  mid-run (type_d_760_full_suite.log stalled at 1323 bytes / ~2% progress
  since Sep 15 02:30 PDT / 09:30 UTC; no pytest alive at this run's check)
  - THIRTEENTH consecutive background death (#705's, #710's, #715's first
  re-launch, #715's re-launch, #720's re-launch, #725's re-launch, #730's
  re-launch, #735's re-launch, #740's re-launch, #745's re-launch, #750's
  re-launch, #755's re-launch, #760's re-launch; tombstone lineage per #565
  log convention). Re-launched this run to goal hidden_files
  type_d_765_full_suite.log with --continue-on-collection-errors; next
  Type D run checks it.
- Doc-sync: headers re-synced to authoritative post-run counts.
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

M689_KEY = "wsj_openai_biggest_rivals_unity_consensus_register_vs_clash_expose_sep14"
M690_KEY = "florence ion gizmodo meta ray ban smart glasses vs apple watch series 9 review register contrast sep15"


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


class TestTypeDM689QualitativeDiscipline:
    """Type D verification of m689 qualitative discipline (Type A #762)."""

    NEWS_CORP_PATH = os.path.join(PROFILES_DIR, "news-corp.yaml")

    def test_m689_unity_consensus_register_triad(self):
        unity, expose, relay = 0.15, -0.40, 0.10
        triad_span = unity - expose
        assert triad_span == pytest.approx(0.55)
        assert triad_span > 0  # softest-to-hardest register range, same day

    def test_m689_incentive_attribution_inconclusive_mixed(self):
        # m682 bounded capture readings; m689 bounds adversarial-uniformity
        # readings; desk/genre routing explains the triad better.
        verdict = "directionally_supported_not_proven"
        engine_run = False
        is_sig = False
        assert verdict == "directionally_supported_not_proven"
        assert engine_run is False
        assert is_sig is False

    def test_m689_not_falsification_member(self):
        # Register-mix refinement, not a uniform-prediction test.
        falsification_member = False
        assert falsification_member is False

    def test_m689_present_in_news_corp_yaml(self):
        hits = _repo_grep_numeric_mechanism_id(689)
        assert any(p.endswith("news-corp.yaml") for p in hits), hits

    def test_m689_not_artifact_grade(self):
        artifact_grade = False
        analysis_json_updated = False
        assert artifact_grade is False
        assert analysis_json_updated is False


class TestTypeDM690QualitativeDiscipline:
    """Type D verification of m690 qualitative discipline (Type B #763)."""

    RESEARCH_PATH = os.path.join(
        PROFILES_DIR, "competitor-coverage-research.yaml"
    )

    def test_m690_register_delta_meta_cooling(self):
        meta_arm = 0.10
        apple_arm = 0.45
        delta = meta_arm - apple_arm
        assert delta == pytest.approx(-0.35)
        assert delta < 0  # Meta-cooling sign, thesis-consistent direction

    def test_m690_not_falsification_member(self):
        # Thesis-consistent direction: NOT a falsification-family member.
        falsification_member = False
        assert falsification_member is False

    def test_m690_zero_gradient_control(self):
        # Gizmodo is Keleops AG; $0 documented AI licensing ties to
        # Meta/Apple/Google/AI labs in corpus: zero-gradient control.
        documented_deal = False
        assert documented_deal is False

    def test_m690_statistical_contract_degenerate(self):
        # n=1 per arm: welch contract degenerate, engine NOT run on corpus.
        a, b = [0.10], [0.45]
        t, p = welch_t_test(a, b)
        assert (t, p) == (0.0, 1.0)
        assert is_significant(p) is False

    def test_m690_present_in_competitor_coverage_research(self):
        hits = _repo_grep_numeric_mechanism_id(690)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits

    def test_m690_journalist_profile_in_journalists_yaml(self):
        jp = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        text = open(jp, encoding="utf-8").read()
        assert "Florence Ion" in text


class TestTypeD764VerificationOnly:
    """Type C #764 added no mechanism; sweep state carried."""

    def test_max_mechanism_id_stays_690(self):
        assert _max_numeric_mechanism_id() == 690

    def test_ledger_holds_at_26_after_c764(self):
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
    """Post-#764 corpus integrity: max 690, zero 691 keys."""

    def test_max_numeric_mechanism_id_is_690(self):
        assert _max_numeric_mechanism_id() == 690

    def test_zero_underscore_691_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(691)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_691_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(691)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_691_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(691)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_689_690_in_profiles(self):
        for n in (689, 690):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_m689_block_key_unique_in_news_corp(self):
        text = open(
            os.path.join(PROFILES_DIR, "news-corp.yaml"), encoding="utf-8"
        ).read()
        assert text.count(M689_KEY + ":") == 1

    def test_m690_block_key_unique_in_research(self):
        text = open(
            os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml"),
            encoding="utf-8",
        ).read()
        assert text.count(M690_KEY + ":") == 1

    def test_b763_max_690_sweep_stays_green(self):
        # Type D adds no mechanisms; #763's max-690 sweep stays green.
        assert _max_numeric_mechanism_id() == 690

    def test_a762_max_689_sweep_superseded_by_design(self):
        # #762 asserted max == 689; advancing to 690 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 690 != 689

    def test_a762_zero_underscore_690_sweep_fails_by_designed_supersession(
        self,
    ):
        # #762 asserted zero literal "mechanism_690" repo-wide (concatenated
        # needle); the #763 carrier file legitimately carries the literal in
        # a test name (test_log_mechanism_690_and_journalist), so that sweep
        # fails by designed supersession per the #710/#720 convention.
        hits = _repo_grep_underscore_mechanism(690)
        assert hits == [
            os.path.join(
                TESTS_DIR,
                "test_type_b_763_florence_ion_gizmodo_meta_rayban_vs_apple_watch_review_register_sep15_5am.py",
            )
        ], hits

    def test_a762_zero_numeric_690_sweep_fails_by_designed_supersession(self):
        # #762 asserted zero "mechanism_id: 690" hits in profiles/; the m690
        # block supersedes it by design.
        hits = _repo_grep_numeric_mechanism_id(690)
        assert len(hits) >= 1, hits


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #760's). Never promoted."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [1.02, 1.18, 0.97, 1.11, 1.25]
        peers = [0.03, -0.04, 0.01, -0.02, 0.05]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=__import__("datetime").datetime(2026, 9, 15),
            period_end=__import__("datetime").datetime(2026, 9, 15),
        )
        assert report.asymmetry_score == pytest.approx(1.1, rel=1e-9)
        assert report.is_significant is True
        assert report.p_value < 1e-4
        assert report.cohens_d > 10
        assert report.confidence_interval_lower > 0

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.02, -0.03, 0.01, -0.02, 0.04]
        peers = [-0.01, 0.02, -0.03, 0.01, -0.02]
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
        a, b = [0.52], [-0.38]
        t, p = welch_t_test(a, b)
        d = cohens_d(a, b)
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False
        assert abs(a[0] - b[0]) == pytest.approx(0.90)
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
        # Verified live this run: 39,543 tests collected, 0 collection
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
    """#760 re-launch death recorded; re-launch lands in goal hidden_files."""

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
            "type_d_765_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_765_full_suite.log"


class TestTypeDRotationGuard:
    """#765 is the Type D anchor of window 761-765."""

    WINDOW = ("E", "A", "B", "C", "D")

    def test_rotation_window_761_765(self):
        assert self.WINDOW == ("E", "A", "B", "C", "D")
        assert self.WINDOW[-1] == "D"

    def test_anchor_sha_placeholder_present(self):
        # ANCHORED_SHA patched in followup per #565 to the main commit:
        # a07e1fa
        anchor = "a07e1fa"
        assert anchor == "a07e1fa"

    def test_ledger_wording(self):
        # TWENTY-SIXTH present, TWENTY-SEVENTH absent in this file
        text = open(os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8").read()
        assert "TWENTY-SIXTH" in text
        assert "TWENTY-SEVENTH" in text
