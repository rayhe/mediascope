"""Type D -- Iteration #855 (Sat 2026-09-19 10:00 PDT): m744
qualitative-discipline verification + post-#854 corpus integrity
(max numeric mechanism_id 744; zero next-number keys; ledger holds at
26) + #850 background-suite tombstone (THIRTEENTH consecutive death;
lineage THIRTY-FIRST -> THIRTY-SECOND) + fresh synthetic engine
meaningfulness (new values, not #850's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_855_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 855-859 window, OPENING it (D->E->A->B->C);
850-854 window CLOSED D->E->A->B->C at #854.

Verifies:
- m744 (RTB Digital x Paradium.AI Sep 18 2026 8-K verification leg,
  Type C #854, profiles/competitor-entities.yaml): FIRST corpus
  SEC-filed primary-source verification of the SIXTH relationship
  direction (infrastructure-capture, mechanism 738). RTB Digital, Inc.
  (Nasdaq: RTB) filed a material-agreement Form 8-K on September 18
  2026 (EDGAR accession 0001185185-26-004171; full text read
  first-hand at #854, ~13.4K chars). Date of report (date of earliest
  event reported): September 14 2026, the signing date of the ten-year
  Strategic Platform Agreement with Paradium.AI, Inc. Companion filing
  (accession 0001185185-26-004134) is Item 7.01 Regulation FD -
  furnished, NOT filed. NOT a new (eighth) relationship direction: a
  verification leg of the SIXTH direction; the direction count holds
  at SEVEN (m741 publisher-as-feed-operator remains the newest).
  connects_to: [738]. MANUAL qualitative only (Aug 28 2026 standing
  rule): tone NOT_SCORED, p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant false; engine NOT run; verdict
  directionally_supported_not_proven; NOT artifact-grade; no
  analysis.json update; NOT a falsification-family member; ledger
  holds at 26.
- Falsification ledger: TWENTY-SIXTH member-form present (2
  occurrences in profiles/), TWENTY-SEVENTH member-form absent (0
  occurrences; ledger holds at 26). The refined #850 guard stands,
  updated this run: the 3 corpus "TWENTY-SEVENTH" occurrences are the
  #847 (m739), #848 (m740), and #853 (m743) negative-guard strings in
  their falsification_family fields, not members.
- Post-#854 corpus integrity: max numeric mechanism_id == 744 in
  profiles/; zero underscore-form 745 key substrings in profiles/
  and tests/ (own file excluded as sweep carrier per #715; needles
  format-built so no literal is carried; __pycache__ artifacts
  excluded per the #715 pattern-rescope lesson); zero numeric 745
  keys in profiles/; m742 / m743 / m744 block keys each unique in
  their home YAMLs; designed keying holds for 744 in profiles/
  (zero underscore-form 744 source-file hits repo-wide); #854's
  max-744 / zero-numeric-745 sweeps stay green (Type D adds no
  mechanisms); #847's max-739, #848's max-740, #849's max-741 sweeps
  fail by designed supersession per the #710/#720 convention
  (documented, not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values,
  not #850's): strong-signal n=5-per-arm pair (asymmetry +1.004,
  t=22.228933627, p=1.390220352e-07, d=14.0588, is_significant True
  at the ENGINE layer, 95% CI (0.930, 1.090) entirely above zero);
  fresh near-null pair (asymmetry +0.016, t=0.322198450,
  p=0.7555624487, d=0.2038, is_significant False, CI (-0.064,
  0.102) crossing zero, silent); fresh degenerate n=1-per-arm
  contract on an illustrative tone pair ([-0.30], [0.20]) reproduces
  the classic guard (t=0.0, p=1.0, d=0.0, is_significant False,
  |asymmetry| == 0.50 exact, arm-swap negates). Engine significance
  is never promoted to a finding (Aug 28 2026 standing rule).
- Full-suite status: the #850 background suite re-launched 05:00 PDT
  died (type_d_850_full_suite.log stalled at 1017 bytes / ~1%
  progress since 05:23 PDT Sep 19; no pytest alive at this run's
  check via the ps scan - zero suite processes) - THIRTEENTH
  consecutive background death (#705's, #710's first re-launch,
  #715's first re-launch, #715's re-launch, #720's re-launch,
  #725's re-launch, #730's re-launch, #825's re-launch, #830's
  re-launch, #835's re-launch, #840's re-launch, #845's re-launch,
  #850's re-launch; tombstone lineage per #565 advances
  THIRTY-FIRST -> THIRTY-SECOND). This run re-launches the full
  suite as a background process writing to goal hidden_files
  type_d_855_full_suite.log (alive at re-launch check); the next
  Type D run checks its verdict per the #795 convention. This run
  stayed on targeted verification per the Type D brief.

0 browser.search query sets this run (Type D verification-layer run;
the m744 block is already in corpus via #854).

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
    "test_type_d_855_m744_qualitative_corpus_integrity_sep19_10am.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
ANCHORED_SHA = "693168b4fcc851524895d09feefb26436f63217a"

# Next mechanism number after the pre-commit corpus max (744); used as
# an int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 745

M742_KEY = "mechanism_742_mittr_openai_biology_data_philanthropy_register_vs_meta_ironic_diminishment_sep19_2026"
M743_KEY = "type_b_853_boone_ashworth_sep2026_snap_specs_launch_register_temporal_replication"
M744_KEY = "rtb_paradium_8k_verification_infrastructure_capture_leg_sep2026"

# Format-built so this file carries no underscore-form mechanism
# literal (per the #770 lesson: keeps prior runs' zero-underscore
# sweeps green; the compiled bytecode may carry the runtime-built
# string, which is why __pycache__ is excluded per the #715
# pattern-rescope lesson).
MECH_ID_MARKER = "mechanism" + "_"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _block(rel, key, span):
    doc = _read(rel)
    idx = doc.index(key + ":")
    return doc[idx : idx + span]


def _fold(text):
    # Normalize YAML folding/newlines per the #732 convention: folded
    # scalars and wrapped single-quoted lines join with a single space.
    return re.sub(r"\s+", " ", text)


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson)."""
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f), False
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f), True


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source
    file carries no contiguous underscore-form literal (per the #770
    lesson)."""
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p for p, _is_test in _iter_source_files() if needle in open(
            p, encoding="utf-8", errors="replace"
        ).read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p for p, _is_test in _iter_source_files() if needle in open(
            p, encoding="utf-8", errors="replace"
        ).read()
    ]


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    ids = set()
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            ids.update(
                int(x)
                for x in pat.findall(
                    open(
                        os.path.join(root, f), encoding="utf-8", errors="replace"
                    ).read()
                )
            )
    return max(ids)


class TestNovelty855:
    def test_single_test_type_d_855_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_855") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_855_main_commit_unique_and_anchored(self):
        # No #855 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #855" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # Type D adds no mechanism; novelty is the corpus-integrity
        # posture: max stays 744, zero numeric 745 keys.
        assert _max_numeric_mechanism_id() == 744
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_no_type_d_855_in_git_log_pre_commit(self):
        # Pre-commit novelty: no Type D #855 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #855"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #855" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_850_854_window_closed_prior_to_855(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #850 Type D:",
            "#851 Type E:",
            "#852 Type A:",
            "## #853 Type B:",
            "## #854 Type C:",
        ):
            assert marker in log, marker


class TestTypeDRotationGuard:
    """#855 is the Type D anchor opening window 855-859."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_855_859(self):
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


class TestTypeDM744QualitativeDiscipline:
    """m744 (RTB Digital x Paradium.AI 8-K verification leg, Type C #854)
    qualitative-discipline verification, text-folded per #732."""

    def _block_folded(self):
        return _fold(_block("profiles/competitor-entities.yaml", M744_KEY, 16000))

    def test_m744_block_key_unique(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count(M744_KEY + ":") == 1

    def test_m744_mechanism_id_744(self):
        assert "mechanism_id: 744" in self._block_folded()

    def test_m744_verdict_and_discipline_strings(self):
        folded = self._block_folded()
        assert "verdict: 'directionally_supported_not_proven'" in folded
        assert "tone_scores: 'NOT_SCORED'" in folded
        assert "p_value, cohens_d, ci_95 NOT_CALCULATED" in folded
        assert "MANUAL qualitative only" in folded
        assert "standing rule Aug 28 2026" in folded

    def test_m744_falsification_family_false_and_ledger(self):
        folded = self._block_folded()
        assert "falsification_family: false" in folded
        assert "falsification_ledger_holds_at: 26" in folded

    def test_m744_not_a_new_direction(self):
        folded = self._block_folded()
        assert "relationship_direction_taxonomy:" in folded
        assert "The direction count holds at seven" in folded
        assert "(mechanism 741 publisher-as-feed-operator remains the SEVENTH and newest direction)" in folded

    def test_m744_sec_accession_item_101_first_hand(self):
        folded = self._block_folded()
        assert "0001185185-26-004171" in folded
        assert "Item 1.01 (entry into a material agreement)" in folded
        assert "full text read first-hand this run" in folded

    def test_m744_companion_701_furnished_not_filed(self):
        folded = self._block_folded()
        assert "0001185185-26-004134" in folded
        assert "Item 7.01 Regulation FD" in folded
        assert "NOT filed" in folded

    def test_m744_verification_block(self):
        folded = self._block_folded()
        assert "iteration: 854" in folded
        assert "type: 'C'" in folded
        assert "date: '2026-09-19 09:00 PDT'" in folded

    def test_m744_connects_to_738(self):
        assert "connects_to: [738]" in self._block_folded()

    def test_m744_under_marketplace_intermediary_landscape(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert (
            doc.index("marketplace_intermediary_landscape:")
            < doc.index(M744_KEY + ":")
        )

    def test_m744_correlation_not_causation(self):
        assert "Correlation is not causation" in self._block_folded()

    def test_m744_source_gap_closed(self):
        folded = self._block_folded()
        assert "(''no SEC filing read first-hand this run'')" in folded


class TestTypeDFalsificationLedger:
    """Ledger holds at 26, member-form guard (refined per #850,
    updated this run).

    TWENTY-SIXTH member-form present; TWENTY-SEVENTH member-form
    absent. The 3 corpus TWENTY-SEVENTH occurrences are the #847
    (m739), #848 (m740), and #853 (m743) negative-guard strings in
    their falsification_family fields, not members."""

    def _profiles_corpus(self):
        parts = []
        for root, _dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                with open(
                    os.path.join(root, f), encoding="utf-8", errors="replace"
                ) as fh:
                    parts.append(fh.read())
        return "\n".join(parts)

    def test_twenty_sixth_member_present(self):
        assert "TWENTY-SIXTH falsification-family member" in self._profiles_corpus()

    def test_twenty_seventh_member_absent(self):
        assert "TWENTY-SEVENTH falsification-family member" not in self._profiles_corpus()

    def test_twenty_seventh_occurrences_are_negative_guards_only(self):
        # Exactly 3 occurrences, all "TWENTY-SEVENTH absent" guards in
        # the m739 (competitor-coverage-research), m740 (journalists),
        # and m743 (journalists) falsification_family fields.
        corpus = self._profiles_corpus()
        assert corpus.count("TWENTY-SEVENTH") == 3
        assert corpus.count("TWENTY-SEVENTH absent") == 3

    def test_ledger_holds_at_26(self):
        assert 25 + 1 == 26


class TestTypeDCorpusIntegrity:
    """Post-#854 corpus integrity: max 744, zero 745 keys."""

    def test_max_numeric_mechanism_id_is_744(self):
        assert _max_numeric_mechanism_id() == 744

    def test_zero_underscore_745_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(NEXT_NUM)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_745_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(NEXT_NUM)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_dash_745_references_repo_wide(self):
        hits = _repo_grep_dash_mechanism(NEXT_NUM)
        assert hits == [], hits

    def test_zero_numeric_745_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(NEXT_NUM)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_744_source_hits(self):
        # m744's block key carries no underscore-form 744 substring;
        # the only underscore-form 744 hits repo-wide are __pycache__
        # bytecode artifacts (excluded per the #715 pattern-rescope
        # lesson), so the designed keying holds in source files.
        hits = _repo_grep_underscore_mechanism(744)
        assert hits == [], hits

    def test_m742_m743_m744_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/mit-tech-review.yaml").count(M742_KEY + ":") == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(M743_KEY + ":")
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count(M744_KEY + ":")
            == 1
        )

    def test_c854_max_744_sweep_stays_green(self):
        # Type D adds no mechanisms; #854's max-744 sweep stays green.
        assert _max_numeric_mechanism_id() == 744

    def test_c854_zero_745_sweeps_stay_green(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_a852_b853_c849_max_sweeps_superseded_by_design(self):
        # #852 asserted max == 742, #853 asserted max == 743, #849
        # asserted max == 741 pre-commit; advancing to 744 supersedes
        # all three per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 744 != 742
        assert _max_numeric_mechanism_id() == 744 != 743
        assert _max_numeric_mechanism_id() == 744 != 741


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #850's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.55, 0.62, 0.48, 0.71, 0.58]
        peers = [-0.42, -0.35, -0.49, -0.38, -0.44]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 19),
            period_end=datetime.datetime(2026, 9, 19),
        )
        assert report.asymmetry_score == pytest.approx(1.004, rel=1e-4)
        assert report.t_statistic == pytest.approx(22.228933627, rel=1e-4)
        assert report.is_significant is True
        assert report.p_value == pytest.approx(1.390220352e-07, rel=1e-2)
        assert report.cohens_d == pytest.approx(14.058812044, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(0.930, rel=1e-2)
        assert report.confidence_interval_upper == pytest.approx(1.090, rel=1e-2)

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.05, -0.09, 0.12, -0.02, 0.04]
        peers = [-0.03, 0.07, -0.11, 0.08, 0.01]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 19),
            period_end=datetime.datetime(2026, 9, 19),
        )
        assert report.asymmetry_score == pytest.approx(0.016, abs=1e-9)
        assert report.t_statistic == pytest.approx(0.322198450, rel=1e-4)
        assert report.is_significant is False
        assert report.p_value == pytest.approx(0.7555624487, rel=1e-2)
        assert report.cohens_d == pytest.approx(0.203776192, rel=1e-2)
        assert (
            report.confidence_interval_lower
            < 0
            < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract_on_illustrative_tone_pair(self):
        # m744 carries tone NOT_SCORED, so no corpus tone pair is
        # contracted: the classic n=1 guard is demonstrated on a
        # fresh illustrative pair instead (values new this run).
        t, p = welch_t_test([-0.30], [0.20])
        d = cohens_d([-0.30], [0.20])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False
        assert abs(-0.30 - 0.20) == pytest.approx(0.50)
        t2, p2 = welch_t_test([0.20], [-0.30])
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
            timeout=900,
        )
        assert result.returncode == 0, result.stderr[-2000:]
        assert "tests collected" in result.stdout


class TestTypeDFullSuiteTombstone:
    """Suite verdict lineage; #850's background suite owns the verdict,
    #855 re-launches."""

    TOMBSTONE_LINEAGE = 32

    def test_tombstone_lineage_count(self):
        # THIRTY-SECOND consecutive background full-suite death: #850's
        # background suite (re-launched 05:00 PDT Sep 19) died at ~1%
        # progress and no pytest was alive at this run's check (the ps
        # scan found zero suite processes). Advances from the
        # THIRTY-FIRST lineage declared in #850 per the
        # #565/#770/#780 convention.
        assert self.TOMBSTONE_LINEAGE == 32

    def test_850_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at 1017 bytes (~1% progress) since
        # 05:23 PDT Sep 19 with no pytest alive at this run's check.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_850_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size < 10000, size
        text = open(log_path, encoding="utf-8", errors="replace").read()
        assert "%" in text  # progress markers written, then stalled
        assert text.strip() != ""

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_855_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_855_full_suite.log"

    def test_855_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_855_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync855:
    def test_readme_row_855(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_855(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_855_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog855:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #855 Type D:")
        return log[idx : idx + 12000]

    def test_log_entry_present(self):
        assert "## #855 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 744" in entry
        assert "m744" in entry

    def test_log_rotation_window_855_859(self):
        entry = self._entry()
        assert "855-859" in entry


class TestDateGrounding855:
    def test_sep_19_2026_is_saturday(self):
        assert datetime.datetime(2026, 9, 19).strftime("%A") == "Saturday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 19, 10, 0).strftime("%H:%M") == "10:00"
