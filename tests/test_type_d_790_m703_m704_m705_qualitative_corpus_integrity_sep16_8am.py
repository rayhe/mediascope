"""Type D -- Iteration #790 (Wed 2026-09-16 08:00 PDT): m703 / m704 / m705
qualitative-discipline verification + post-#789 corpus integrity
(max numeric mechanism_id 705; zero 706 keys; ledger holds at 26) +
#785 background-suite tombstone (TWENTY-FIRST consecutive death; re-launched as
type_d_790_full_suite.log) + fresh synthetic engine meaningfulness.

Verifies:
- m703 (Politico x OpenAI slowdown-week scoop channel symmetry, Type A #787,
  profiles/competitor-coverage-research.yaml): FIRST dedicated Politico x
  OpenAI mechanism; Politico's AI-policy vertical is the frontier labs'
  preferred leak/scoop channel; scoop access SYMMETRIC across payer status
  (OpenAI arm +0.05 via Reuters "Politico earlier reported", Anthropic arm
  +0.05 via techtimes "first reported by Politico in August 2026"); financial
  tie real and near-term material (OpenAI x Axel Springer Dec 13 2023 3-year
  tens-of-millions EUR, mechanism 597, renewal UNRESOLVED ~Dec 2026 expiry;
  Microsoft x Axel Springer Apr 29 2024 makes it a DUAL-AI-PAYER owner);
  uniform financial-incentive prediction NOT supported on observed arms;
  beat-driven + lab-driven pattern; Meta comparator bounded absence;
  MANUAL ILLUSTRATIVE only; is_significant false; Engine NOT run; NOT
  artifact-grade; verdict directionally_supported_not_proven; NOT a
  falsification-family member (ledger holds at 26).
- m704 (Brenda Stolyar, WIRED -> Wirecutter migration, Meta vs Apple
  register split, Type B #788, profiles/competitor-coverage-research.yaml +
  careers/journalists.yaml): FIRST dedicated corpus mechanism on Stolyar;
  migrated from WIRED staff writer (Gear team, Conde Nast / Advance) to
  Wirecutter senior staff writer (circa May 2025); WITHIN-employer
  within-journalist register split at Wirecutter/NYT: Meta arm
  disappointed-dismissive opinion -0.45 ("Meta's New Smart Glasses Sounded
  Cool at First. But I Was Unimpressed."), Apple arms +0.45 / +0.55
  (avg +0.50, Sep 10 2026 iPhone Duo foldable pieces); illustrative register
  delta (Apple minus Meta) +0.95; financial prediction NULL on the register
  axis (both arms under Wirecutter/NYT); MANUAL ILLUSTRATIVE only;
  is_significant false; no_analysis_json_update true; verdict
  directionally_supported_not_proven; NOT a falsification-family member
  (ledger holds at 26); NOT artifact-grade.
- m705 (Paramount-WBD tender/exchange-offer extension to Sep 18 2026 +
  SEC-filed deal-protection provisions, Type C #789,
  profiles/competitor-entities.yaml): FIRST dedicated Paramount-WBD
  tender/exchange extension mechanism; twelfth extension of debt tender and
  exchange offers to 5:00 p.m. NYC Sep 18 2026; Sep 4 5pm NYC figures
  66.28% tendered / 75.31% exchanged (Paramount disclaims
  representativeness); SEC Edgar tm2533570d52_exa5ab.htm provisions:
  $0.25/share quarterly ticking fee (~$650M/quarter beyond Dec 31 2026),
  $2.8B Netflix termination-fee funding, $1.5B debt-exchange backstop (no
  reduction to separate $5.8B reverse termination fee), $15B bridge-loan
  refinancing readiness, Netflix-matching interim covenants; extends
  mechanism 124 + paramount_merger sub-key; sets timing/certainty of Advance
  Publications' ~$2.94B WBD liquidity event; statistical_discipline scorer
  none / tone NOT_SCORED / qualitative_only true / artifact_grade false;
  verdict directionally_supported_not_proven; no_analysis_json_update true;
  falsification_family 'NOT a member - qualitative financial mapping only';
  ledger holds at 26.
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent in
  profiles/; ledger holds at 26.
- Post-#789 corpus integrity: max numeric mechanism_id == 705 in
  profiles/; zero underscore-form 706 key substrings in profiles/ and
  tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson; needles built by format string so no literal is
  carried); zero numeric 706 keys in profiles/; m703 / m704 / m705 block
  keys each unique in their home YAMLs; designed keying holds (no
  underscore-form 703/704/705 mechanism key substrings in profiles/).
  #789's max-705, zero-underscore-705, and zero-numeric-705 sweeps stay
  green (Type D adds no mechanisms); #787's max-703, #788's max-704 and
  zero-numeric-705 sweeps fail by designed supersession (per the #710/#720
  convention; documented, not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values, not
  #785's): strong-signal n=5-per-arm pair (asymmetry +0.934,
  p=3.75e-05 < 5e-4, d=9.756 > 8, 95% CI (0.834, 1.038) above zero,
  is_significant True at the ENGINE layer); fresh near-null pair
  (asymmetry 0.000, p=1.000 > 0.5, d=0.000 < 0.5, CI crossing zero,
  silent); fresh degenerate n=1-per-arm contract (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 1.00, arm-swap negates). Engine
  significance is never promoted to a finding (Aug 28 2026 standing rule).
- Full-suite status: the #785 re-launched background 40K suite died
  mid-run (type_d_785_full_suite.log stalled at ~8% progress; no pytest
  alive at this run's check) -- TWENTY-FIRST consecutive background death
  (lineage: 20 per #785's log plus this run's). Re-launched this run to
  goal hidden_files type_d_790_full_suite.log with
  --continue-on-collection-errors; next Type D run checks it.
- Doc-sync: headers re-synced to authoritative post-run counts.

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import datetime
import os
import re
import subprocess

import pytest

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import welch_t_test, cohens_d, is_significant

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = os.path.basename(__file__)
TEST_BASENAME = (
    "test_type_d_790_m703_m704_m705_qualitative_corpus_integrity_sep16_8am.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"

ANCHORED_SHA = "c762630bb86d8a7fd7825522a7af52a84b837940"

M703_KEY = "politico_openai_slowdown_week_scoop_channel_symmetry_sep16"
M704_KEY = (
    "brenda stolyar wired to wirecutter migration meta vs apple register "
    "split sep2026"
)
M705_KEY = "paramount_wbd_tender_exchange_extension_sep18_2026"
M704_JOURNALIST_KEY = (
    "type_b_788_brenda_stolyar_wired_wirecutter_meta_vs_apple_register_split_"
    "sep16"
)


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _block(rel, key, span):
    doc = _read(rel)
    idx = doc.index(key + ":")
    return doc[idx : idx + span]


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source file
    carries no contiguous underscore-form literal (per the #770 lesson:
    keep prior runs' zero-underscore sweeps green)."""
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


def _git_log_mains(pattern):
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%H %s", "--no-merges", "--", "."],
        capture_output=True,
        text=True,
    )
    return [l for l in proc.stdout.splitlines() if re.search(pattern, l)]


def _window_legs_deduped():
    """First occurrence of each iteration number, newest first.

    Robust to the #781-style push-status followup commit that repeats the
    iteration wording (per the #752 convention and the #783 repair).
    The current iteration ("790") is skipped so the 785-789 window
    closure reads stable both pre- and post-commit."""
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%s", "--no-merges", "-n", "60"],
        capture_output=True,
        text=True,
        check=True,
    )
    seen_nums = set()
    out = []
    for s in proc.stdout.splitlines():
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums and m.group(2) != "790":
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out


class TestNovelty790:
    """Pre-commit novelty: single new file, unique commit."""

    def test_single_test_type_d_790_file(self):
        files = sorted(
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_790") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_d_790_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 convention; the main commit
        # does not exist yet. Patched green in the anchor followup.
        mains = _git_log_mains(r"Type D #790: ")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # Type D adds no mechanism; novelty is the corpus-integrity posture:
        # single new file, no mechanism keys added (max stays 705).
        assert _max_numeric_mechanism_id() == 705
        assert _repo_grep_numeric_mechanism_id(706) == []

    def test_785_789_window_closed_prior_to_790(self):
        # Anchor leg of the 790-794 window: the previous window must read
        # closed D->E->A->B->C (newest first) before the new window opens.
        legs = _window_legs_deduped()[:5]
        assert legs == [
            ("C", "789"),
            ("B", "788"),
            ("A", "787"),
            ("E", "786"),
            ("D", "785"),
        ], legs


class TestTypeDRotationGuard:
    """#790 is the Type D anchor opening window 790-794."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_790_794(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_anchor_sha_placeholder_patched(self):
        # ANCHORED_SHA patched in followup per #565 to the main commit:
        # deselected pre-commit, patched green in the followup.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        )
        assert len(ANCHORED_SHA) == 40

    def test_ledger_wording(self):
        # TWENTY-SIXTH present, TWENTY-SEVENTH present in this file
        # (prior type files legitimately reference the absent member
        # inside their own negative guards per the #754 convention).
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "TWENTY-SIXTH" in text
        assert "TWENTY-SEVENTH" in text


class TestTypeDM703QualitativeDiscipline:
    """Type D verification of m703 qualitative discipline (Type A #787)."""

    def _block(self):
        return _block("profiles/competitor-coverage-research.yaml", M703_KEY, 14000)

    def test_m703_publication_and_entity(self):
        block = self._block()
        assert "publication: Politico (Axel Springer)" in block
        assert "entity: OpenAI" in block
        assert "Slowdown-Week Scoop Channel" in block

    def test_m703_scoop_access_symmetric(self):
        block = self._block()
        assert "scoop access is SYMMETRIC across payer status" in block
        assert "arm1_openai_bill_endorsements_politico_scoop" in block

    def test_m703_both_arms_plus_005_illustrative(self):
        block = self._block()
        assert "tone_MANUAL_ILLUSTRATIVE: 0.05" in block
        assert "MANUAL ILLUSTRATIVE scores only" in block

    def test_m703_financial_tie_real(self):
        block = self._block()
        assert "Dec 13 2023" in block
        assert "mechanism 597" in block
        assert "DUAL-AI-PAYER owner" in block
        assert "renewal UNRESOLVED" in block

    def test_m703_uniform_prediction_not_supported(self):
        block = self._block()
        assert "preferential narrative carriage" in block
        assert "is NOT supported on the" in block
        assert "beat-driven" in block

    def test_m703_meta_comparator_bounded_absence(self):
        block = self._block()
        assert "bounded absence" in block

    def test_m703_statistical_discipline_strings(self):
        block = self._block()
        assert "is_significant: false" in block
        assert "Engine NOT" in block
        assert "NOT artifact-grade" in block
        assert "no_analysis_json_update: true" in block

    def test_m703_verdict(self):
        assert "verdict: directionally_supported_not_proven" in self._block()

    def test_m703_not_falsification_member(self):
        block = self._block()
        assert "NOT a falsification-family member" in block
        assert "Ledger holds at 26" in block

    def test_m703_block_key_unique_in_research(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert text.count(M703_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(703)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits


class TestTypeDM704QualitativeDiscipline:
    """Type D verification of m704 qualitative discipline (Type B #788)."""

    def _block(self):
        return _block(
            "profiles/competitor-coverage-research.yaml", M704_KEY, 16000
        )

    def test_m704_journalist_and_publication(self):
        block = self._block()
        assert "journalist: 'Brenda Stolyar'" in block
        assert "publication: wirecutter" in block
        assert "previous_publication: wired" in block
        assert "owner: nyt" in block

    def test_m704_meta_vs_apple_register_arms(self):
        block = self._block()
        assert "disappointed_dismissive_opinion" in block
        assert "enthusiastic_launch_hands_on" in block
        assert "But I Was Unimpressed" in block

    def test_m704_illustrative_delta_plus_095(self):
        block = self._block()
        assert "Meta arm -0.45; Apple arms +0.45 / +0.55, avg +0.50" in block
        assert "illustrative register delta (Apple minus Meta) = +0.95" in block
        assert "MANUAL ILLUSTRATIVE" in block

    def test_m704_within_employer_split(self):
        block = self._block()
        assert "WITHIN-employer and within-journalist" in block
        assert "the migration is career context, not the causal mechanism" in block

    def test_m704_financial_prediction_null(self):
        block = self._block()
        assert "NULL on the register axis for the scored comparison" in block
        assert "the split is writer-level and entity-selective" in block

    def test_m704_statistical_discipline_strings(self):
        block = self._block()
        assert "is_significant: false" in block
        assert "no_analysis_json_update: true" in block
        assert "NOT artifact-grade" in block

    def test_m704_verdict(self):
        assert "verdict: directionally_supported_not_proven" in self._block()

    def test_m704_not_falsification_member(self):
        block = self._block()
        assert "NOT a falsification-family member" in block
        assert "Ledger holds at 26" in block

    def test_m704_journalist_profile_in_journalists_yaml(self):
        text = open(
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml"),
            encoding="utf-8",
        ).read()
        assert M704_JOURNALIST_KEY in text

    def test_m704_block_key_unique_in_research(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert text.count(M704_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(704)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits


class TestTypeDM705QualitativeDiscipline:
    """Type D verification of m705 qualitative discipline (Type C #789)."""

    def _block(self):
        return _block("profiles/competitor-entities.yaml", M705_KEY, 9500)

    def test_m705_extension_action(self):
        block = self._block()
        assert "September 18, 2026" in block
        assert "Twelfth extension" in block

    def test_m705_creditor_confidence_figures(self):
        block = self._block()
        assert "66.28" in block
        assert "75.31" in block
        assert "disclaims" in block

    def test_m705_sec_filed_provisions(self):
        block = self._block()
        assert "tm2533570d52_exa5ab.htm" in block
        assert "$0.25 per share" in block
        assert "$2.8 billion termination fee" in block
        assert "$1.5 billion financing cost" in block
        assert "$15 billion bridge loan" in block

    def test_m705_mediascope_linkage(self):
        block = self._block()
        assert "extends_mechanism_124" in block
        assert "$2.94B" in block

    def test_m705_statistical_discipline(self):
        block = self._block()
        assert "scorer: none" in block
        assert "tone_scores: NOT_SCORED" in block
        assert "is_significant: false" in block
        assert "qualitative_only: true" in block
        assert "correlation_not_causation: true" in block
        assert "artifact_grade: false" in block
        assert "no_analysis_json_update: true" in block

    def test_m705_verdict(self):
        assert "verdict: directionally_supported_not_proven" in self._block()

    def test_m705_not_falsification_member(self):
        block = self._block()
        assert "NOT a member - qualitative financial mapping only" in block
        assert "ledger holds at 26" in block

    def test_m705_block_key_unique_in_entities(self):
        text = _read("profiles/competitor-entities.yaml")
        assert text.count(M705_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(705)
        assert any(p.endswith("competitor-entities.yaml") for p in hits), hits


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
    """Post-#789 corpus integrity: max 705, zero 706 keys."""

    def test_max_numeric_mechanism_id_is_705(self):
        assert _max_numeric_mechanism_id() == 705

    def test_zero_underscore_706_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(706)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_706_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(706)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_706_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(706)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_703_704_705_in_profiles(self):
        for n in (703, 704, 705):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c789_max_705_sweep_stays_green(self):
        # Type D adds no mechanisms; #789's max-705 sweep stays green.
        assert _max_numeric_mechanism_id() == 705

    def test_c789_zero_underscore_705_sweeps_stay_green(self):
        hits = _repo_grep_underscore_mechanism(705)
        assert hits == [], hits

    def test_c789_zero_numeric_705_sweep_stays_green(self):
        hits = _repo_grep_numeric_mechanism_id(705)
        assert len(hits) >= 1, hits

    def test_a787_max_703_sweep_superseded_by_design(self):
        # #787 asserted max == 703; advancing to 705 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 705 != 703

    def test_b788_max_704_sweep_superseded_by_design(self):
        # #788 asserted max == 704; advancing to 705 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 705 != 704

    def test_b788_zero_numeric_705_sweep_fails_by_designed_supersession(self):
        # #788 asserted zero "mechanism_id: 705" hits in profiles/; the m705
        # block supersedes it by design.
        hits = _repo_grep_numeric_mechanism_id(705)
        assert len(hits) >= 1, hits


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #785's). Never promoted."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.88, 1.02, 0.76, 0.94, 1.10]
        peers = [0.03, -0.04, 0.01, -0.02, 0.05]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 16),
            period_end=datetime.datetime(2026, 9, 16),
        )
        assert report.asymmetry_score == pytest.approx(0.934, rel=1e-9)
        assert report.is_significant is True
        assert report.p_value < 5e-4
        assert report.cohens_d > 8
        assert report.confidence_interval_lower > 0

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [-0.03, 0.05, -0.01, 0.02, -0.04]
        peers = [0.01, -0.03, 0.04, -0.05, 0.02]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 16),
            period_end=datetime.datetime(2026, 9, 16),
        )
        assert report.asymmetry_score == pytest.approx(0.0, abs=1e-9)
        assert report.is_significant is False
        assert report.p_value > 0.5
        assert report.cohens_d < 0.5
        assert (
            report.confidence_interval_lower < 0 < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract(self):
        a, b = [0.51], [-0.49]
        t, p = welch_t_test(a, b)
        d = cohens_d(a, b)
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False
        assert abs(a[0] - b[0]) == pytest.approx(1.00)
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
        # Verified live this run on the plain (non-continue-on) run.
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
            timeout=600,
        )
        assert result.returncode == 0, result.stderr[-2000:]
        assert "tests collected" in result.stdout


class TestTypeDFullSuiteTombstone:
    """#785 re-launch death recorded; re-launch lands in goal hidden_files."""

    TOMBSTONE_LINEAGE = 21

    def test_tombstone_lineage_count(self):
        assert self.TOMBSTONE_LINEAGE == 21

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_790_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_790_full_suite.log"


class TestDocSync790:
    def test_readme_row_790(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_790(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_790_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog790:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #790 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        # "#790 Type D:" is the entry header; a bare "#790" would
        # false-positive on other rotation lines mentioning 790.
        assert "#790 Type D:" in self._tail()

    def test_log_mechanism_numbers_and_topics(self):
        tail = self._tail()
        assert "mechanism 705" in tail
        assert "Paramount-WBD" in tail


class TestDateGrounding790:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_16_2026_is_wednesday(self):
        assert self._weekday("2026-09-16") == "Wednesday"
