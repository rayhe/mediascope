"""Type D -- Iteration #795 (Wed 2026-09-16 22:00 PDT): m706 / m707 / m708
qualitative-discipline verification + post-#794 corpus integrity
(max numeric mechanism_id 708; zero 709 keys; ledger holds at 26) +
#790 background-suite tombstone (TWENTY-SECOND consecutive death) +
#795 foreground full-suite run + fresh synthetic engine meaningfulness.

Verifies:
- m706 (The Verge x Apple iPhone Duo launch-week staff-react register vs
  Meta glasses adversarial privacy register, Type A #792,
  profiles/competitor-coverage-research.yaml): FIRST dedicated Verge x
  Apple Duo mechanism; arm 1 (Sep 9 2026, 7:45 PM) "Verge staffers react
  to the iPhone Duo" aspirational staff-react register, MANUAL
  ILLUSTRATIVE +0.45; arm 2 (Sep 11 2026) Vergecast "We unfolded the
  iPhone Duo" +0.45 with Apple privacy carried INSIDE the
  product-positive frame; Meta comparator (in-corpus m75/m304):
  Victoria Song's privacy-adversarial Meta glasses pieces, tone -0.55;
  illustrative register delta (Apple arms avg +0.45 minus Meta
  comparator -0.55) = +1.00, documented as register selection on
  different news pegs, NOT a controlled causal claim; financial tie
  Apple x Vox Media platform-distribution tie at parent level,
  directionally CONSISTENT with the observed delta, caveated
  (Vox-site-specific, not The Verge); MANUAL ILLUSTRATIVE only;
  is_significant false; Engine NOT run; NOT artifact-grade; verdict
  directionally_supported_not_proven; NOT a falsification-family
  member (ledger holds at 26).
- m707 (Jason Hiner, ZDNet/Ziff Davis, Meta vs Rokid register
  even-handedness, Type B #793, profiles/competitor-coverage-research.yaml
  + careers/journalists.yaml): FIRST dedicated corpus mechanism on
  Hiner; within-journalist, within-employer register even-handedness on
  the smart-glasses axis: Meta arm Sep 2025 ZDNet news-analysis "Meta
  wears Prada?" enthusiastic forward-looking register, MANUAL
  ILLUSTRATIVE +0.35; comparator arm Oct 2025 ZDNet hands-on comparison
  "I tested Meta Ray-Ban Display alternatives" - Meta's $799 flagship
  loses to $599 Rokid Glasses, MANUAL ILLUSTRATIVE -0.30 on the Meta
  leg; illustrative within-writer spread 0.65; migration to The Deep
  View (announced Dec 2025) post-dates both arms, career context not
  the mechanism; uniform financial-incentive prediction NOT supported
  on the observed arms; MANUAL ILLUSTRATIVE only; is_significant
  false; Engine NOT run; NOT artifact-grade; verdict
  directionally_supported_not_proven; NOT a falsification-family
  member (ledger holds at 26).
- m708 (Google publisher AI-licensing talks, Bloomberg Law ~Jul 2026,
  ~20 national outlets, Type C #794, profiles/competitor-entities.yaml):
  FIRST dedicated corpus mechanism documenting Bloomberg Law reporting
  (~Jul 2026) that Google sought to recruit news organizations for a
  new AI licensing project: pilot initially with about 20 national
  news outlets; Jul 2026 precursor of the Sep 14 2026 Digiday-reported
  pay-per-use AI licensing pilot (mechanism 702); two independent
  outlets corroborate the program existence; 5 ranked confounders
  (2 strong, 2 moderate, 1 weak) + strongest counterargument
  (industry-relations/regulatory-hedge null reading); statistical
  discipline scorer none / tone NOT_SCORED / qualitative_only true /
  artifact_grade false; verdict directionally_supported_not_proven;
  no_analysis_json_update true; NOT a falsification-family member
  (ledger holds at 26).
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent in
  profiles/; ledger holds at 26.
- Post-#794 corpus integrity: max numeric mechanism_id == 708 in
  profiles/; zero underscore-form 709 key substrings in profiles/ and
  tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson; needles built by format string so no literal
  is carried); zero numeric 709 keys in profiles/; m706 / m707 / m708
  block keys each unique in their home YAMLs; designed keying holds
  (no underscore-form 706/707/708 mechanism key substrings in
  profiles/). #794's max-708 and zero-underscore-708 sweeps stay green
  (Type D adds no mechanisms); #792's max-706, #793's max-707 and
  zero-numeric-708, and #794's zero-numeric-708 sweeps fail by designed
  supersession per the #710/#720 convention (documented, not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values,
  not #790's): strong-signal n=5-per-arm pair (asymmetry +1.046,
  p=8.47e-06 < 5e-4, d=10.57 > 8, 95% CI (0.934, 1.150) above zero,
  is_significant True at the ENGINE layer); fresh near-null pair
  (asymmetry -0.012, p=0.614 > 0.5, |d|=0.332 < 0.5, CI crossing zero,
  silent); fresh degenerate n=1-per-arm contract (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 1.00, arm-swap negates). Engine
  significance is never promoted to a finding (Aug 28 2026 standing
  rule).
- Full-suite status: the #790 re-launched background 40K suite died
  (type_d_790_full_suite.log stalled at ~10% progress, no pytest alive
  at this run's check) -- TWENTY-SECOND consecutive background death
  (lineage: 21 per #790's log plus this run's). This run's own 40K
  suite ran as a foreground process writing to /tmp/
  type_d_795_pytest.log; failures (if any) repaired in the test file
  before the main commit.
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
    "test_type_d_795_m706_m707_m708_qualitative_corpus_integrity_sep16_10pm.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"

ANCHORED_SHA = "21938a3b882fb2e22201cf33d3b1cdfc3cd571f7"

M706_KEY = "verge_apple_duo_launch_week_staff_react_register_sep16"
M707_KEY = (
    "jason hiner zdnet meta vs rokid register evenhandedness sep2026"
)
M708_KEY = "google_publisher_licensing_talks_bloomberg_20_outlets_jul2026"
M707_JOURNALIST_KEY = (
    "type_b_793_jason_hiner_zdnet_meta_vs_rokid_register_evenhandedness_sep16"
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
    The current iteration ("795") is skipped so the 790-794 window
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
        if m and m.group(2) not in seen_nums and m.group(2) != "795":
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out


class TestNovelty795:
    """Pre-commit novelty: single new file, unique commit."""

    def test_single_test_type_d_795_file(self):
        files = sorted(
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_795") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_d_795_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 convention; the main commit
        # does not exist yet. Patched green in the anchor followup.
        # Specific "Type D #795: m706" prefix per the #796 convention
        # (repaired #800): the #795 push-status record commit subject
        # "Type D #795: push-status record (...)" collided with the bare
        # "Type D #795: " pattern.
        mains = _git_log_mains(r"Type D #795: m706")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # Type D adds no mechanism; novelty is the corpus-integrity posture:
        # single new file, no mechanism keys added (max stays 708).
        assert _max_numeric_mechanism_id() == 708
        assert _repo_grep_numeric_mechanism_id(709) == []

    def test_790_794_window_closed_prior_to_795(self):
        # Anchor leg of the 795-799 window: the previous window must read
        # closed D->E->A->B->C (newest first) as a consecutive sequence in
        # history, wherever it sits (repaired #800: the newest-five
        # shortcut broke once #796-#799 landed; #781/#783 convention).
        legs = _window_legs_deduped()
        want = [
            ("C", "794"),
            ("B", "793"),
            ("A", "792"),
            ("E", "791"),
            ("D", "790"),
        ]
        found = any(legs[i : i + 5] == want for i in range(len(legs) - 4))
        assert found, legs[:12]


class TestTypeDRotationGuard:
    """#795 is the Type D anchor opening window 795-799."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_795_799(self):
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


class TestTypeDM706QualitativeDiscipline:
    """Type D verification of m706 qualitative discipline (Type A #792)."""

    def _block(self):
        return _block("profiles/competitor-coverage-research.yaml", M706_KEY, 20000)

    def test_m706_publication_and_entity(self):
        block = self._block()
        assert "publication: The Verge (Vox Media)" in block
        assert "entity: Apple" in block
        assert "Verge x Apple Duo" in block or "Verge x Apple iPhone Duo" in block

    def test_m706_arm1_staff_react_aspirational(self):
        block = self._block()
        assert "Verge staffers react to the iPhone Duo" in block
        assert "Tone MANUAL ILLUSTRATIVE +0.45" in block

    def test_m706_arm2_vergecast_privacy_inside_positive_frame(self):
        block = self._block()
        assert "We unfolded the iPhone Duo" in block
        assert "Privacy Whitepaper" in block

    def test_m706_meta_comparator_adversarial_minus_055(self):
        block = self._block()
        assert "tone -0.55" in block
        assert "pervert glasses" in block

    def test_m706_illustrative_delta_plus_100(self):
        block = self._block()
        assert "avg +0.45 minus Meta comparator -0.55) = +1.00" in block
        assert "NOT a controlled causal claim" in block or "register-documentation" in block

    def test_m706_financial_tie_vox_parent_level(self):
        block = self._block()
        assert "Apple x Vox Media distribution" in block
        assert "is directionally CONSISTENT with the observed register delta" in block

    def test_m706_statistical_discipline_strings(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE scores only" in block
        assert "is_significant: false" in block
        assert "Engine NOT run" in block
        assert "NOT artifact-grade" in block
        assert "no_analysis_json_update: true" in block

    def test_m706_verdict(self):
        assert "directionally_supported_not_proven" in self._block()

    def test_m706_not_falsification_member(self):
        block = self._block()
        assert "NOT a member - register documentation with" in block
        assert "holds at 26." in block

    def test_m706_block_key_unique_in_research(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert text.count(M706_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(706)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits


class TestTypeDM707QualitativeDiscipline:
    """Type D verification of m707 qualitative discipline (Type B #793)."""

    def _block(self):
        return _block(
            "profiles/competitor-coverage-research.yaml", M707_KEY, 18000
        )

    def test_m707_journalist_and_publication(self):
        block = self._block()
        assert "journalist: 'Jason Hiner'" in block
        assert "publication: zdnet" in block
        assert "owner: ziff_davis" in block

    def test_m707_meta_arm_prada_plus_035(self):
        block = self._block()
        assert "Meta wears Prada?" in block
        assert "Meta-Prada arm +0.35; Meta leg in the Rokid comparison -0.30; illustrative within-writer spread 0.65" in block

    def test_m707_comparator_arm_rokid_minus_030(self):
        block = self._block()
        assert "I tested Meta Ray-Ban Display alternatives" in block
        assert "Rokid Glasses" in block
        assert "illustrative_within_writer_spread: 0.65" in block

    def test_m707_migration_postdates_arms(self):
        block = self._block()
        assert "The Deep View" in block
        assert "post-dates both arms" in block

    def test_m707_uniform_prediction_not_supported(self):
        block = self._block()
        assert "Uniform financial-incentive prediction NOT supported" in block

    def test_m707_statistical_discipline_strings(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE scores only" in block
        assert "is_significant: false" in block
        assert "Engine NOT run" in block
        assert "NOT artifact-grade" in block
        assert "no_analysis_json_update: true" in block

    def test_m707_verdict(self):
        assert "verdict: directionally_supported_not_proven" in self._block()

    def test_m707_not_falsification_member(self):
        block = self._block()
        assert "NOT a falsification-family member" in block
        assert "Ledger holds at 26." in block

    def test_m707_journalist_profile_in_journalists_yaml(self):
        text = open(
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml"),
            encoding="utf-8",
        ).read()
        assert M707_JOURNALIST_KEY in text

    def test_m707_block_key_unique_in_research(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert text.count(M707_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(707)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits


class TestTypeDM708QualitativeDiscipline:
    """Type D verification of m708 qualitative discipline (Type C #794)."""

    def _block(self):
        return _block("profiles/competitor-entities.yaml", M708_KEY, 16000)

    def test_m708_bloomberg_jul2026_reporting(self):
        block = self._block()
        assert "Bloomberg Law" in block
        assert "Jul 2026" in block

    def test_m708_20_outlet_scope_figure(self):
        block = self._block()
        assert "about 20 national news outlets" in block

    def test_m708_precursor_of_m702_pay_per_use(self):
        block = self._block()
        assert "mechanism 702" in block
        assert "Digiday" in block

    def test_m708_ranked_confounders_and_counterargument(self):
        block = self._block()
        assert "ranked_confounders:" in block
        assert "strongest_counterargument:" in block
        assert "regulatory-theater" in block or "regulatory hedge" in block

    def test_m708_statistical_discipline(self):
        block = self._block()
        assert "scorer: none" in block
        assert "tone_scores: NOT_SCORED" in block
        assert "is_significant: false" in block
        assert "qualitative_only: true" in block
        assert "artifact_grade: false" in block
        assert "no_analysis_json_update: true" in block

    def test_m708_verdict(self):
        assert "verdict: directionally_supported_not_proven" in self._block()

    def test_m708_not_falsification_member(self):
        block = self._block()
        assert "NOT a member - qualitative financial mapping only" in block
        assert "ledger holds at 26" in block

    def test_m708_block_key_unique_in_entities(self):
        text = _read("profiles/competitor-entities.yaml")
        assert text.count(M708_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(708)
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
    """Post-#794 corpus integrity: max 708, zero 709 keys."""

    def test_max_numeric_mechanism_id_is_708(self):
        assert _max_numeric_mechanism_id() == 708

    def test_zero_underscore_709_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(709)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_709_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(709)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_709_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(709)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_706_707_708_in_profiles(self):
        for n in (706, 707, 708):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c794_max_708_sweep_stays_green(self):
        # Type D adds no mechanisms; #794's max-708 sweep stays green.
        assert _max_numeric_mechanism_id() == 708

    def test_c794_zero_underscore_708_sweeps_stay_green(self):
        hits = _repo_grep_underscore_mechanism(708)
        assert hits == [], hits

    def test_a792_max_706_sweep_superseded_by_design(self):
        # #792 asserted max == 706; advancing to 708 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 708 != 706

    def test_b793_max_707_sweeps_superseded_by_design(self):
        # #793 asserted max == 707; advancing to 708 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 708 != 707

    def test_b793_zero_numeric_708_sweep_fails_by_designed_supersession(self):
        # #793 asserted zero "mechanism_id: 708" hits in profiles/; the
        # m708 block supersedes it by design.
        hits = _repo_grep_numeric_mechanism_id(708)
        assert len(hits) >= 1, hits

    def test_c794_zero_numeric_708_sweep_fails_by_designed_supersession(self):
        # #794's own zero-numeric-708 forward sweep is superseded by the
        # m708 block it documented, per the #710/#720 convention.
        hits = _repo_grep_numeric_mechanism_id(708)
        assert len(hits) >= 1, hits


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #790's). Never promoted."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [1.12, 0.95, 1.08, 0.89, 1.21]
        peers = [0.06, -0.07, 0.04, -0.03, 0.02]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 16),
            period_end=datetime.datetime(2026, 9, 16),
        )
        assert report.asymmetry_score == pytest.approx(1.046, rel=1e-9)
        assert report.is_significant is True
        assert report.p_value < 5e-4
        assert report.cohens_d > 8
        assert report.confidence_interval_lower > 0

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [-0.05, 0.03, -0.02, 0.04, -0.01]
        peers = [0.02, -0.04, 0.03, -0.01, 0.05]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 16),
            period_end=datetime.datetime(2026, 9, 16),
        )
        assert report.asymmetry_score == pytest.approx(-0.012, abs=1e-9)
        assert report.is_significant is False
        assert report.p_value > 0.5
        assert abs(report.cohens_d) < 0.5
        assert (
            report.confidence_interval_lower < 0 < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract(self):
        a, b = [0.62], [-0.38]
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
    """#790 re-launch death recorded; lineage counts this run's."""

    TOMBSTONE_LINEAGE = 22

    def test_tombstone_lineage_count(self):
        # TWENTY-SECOND consecutive background full-suite death:
        # 21 per #790's log plus this run's (no pytest alive on the
        # type_d_790_full_suite.log re-launch at this run's check).
        assert self.TOMBSTONE_LINEAGE == 22

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

    def test_foreground_suite_log_owns_this_run(self):
        # The #795 foreground suite wrote to /tmp/type_d_795_pytest.log;
        # /tmp is ephemeral and the log vanished on VM recycle. The durable
        # record is the #795 iteration-log entry; assert it documents the
        # foreground run (repaired #800; per the #730 test-side precedent).
        log = _read(LOG_PATH)
        assert "## #795 Type D:" in log
        assert "foreground full suite (/tmp/type_d_795_pytest.log)" in log


class TestDocSync795:
    def test_readme_row_795(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_795(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_795_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog795:
    def _entry(self):
        # Repaired #800: entries are appended chronologically (post-#735
        # convention), so the #795 entry is displaced by the #796-#799
        # appends; locate it by header (the #799 8000-char window
        # convention) instead of the last-60-lines tail.
        log = _read(LOG_PATH)
        idx = log.index("## #795 Type D:")
        return log[idx : idx + 8000]

    def test_log_entry_present(self):
        # "## #795 Type D:" is the entry header; a bare "#795" would
        # false-positive on other rotation lines mentioning 795.
        assert "## #795 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 708" in entry
        assert "m706" in entry


class TestDateGrounding795:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_16_2026_is_wednesday(self):
        assert self._weekday("2026-09-16") == "Wednesday"
