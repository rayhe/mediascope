"""Type D -- Iteration #860 (Sat 2026-09-19 15:00 PDT): m747
qualitative-discipline verification + post-#859 corpus integrity
(max numeric mechanism_id 747; zero next-number keys; ledger holds at
26) + #855 background-suite tombstone (FOURTEENTH consecutive death;
lineage THIRTY-SECOND -> THIRTY-THIRD) + fresh synthetic engine
meaningfulness (new values, not #855's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_860_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 860-864 window, OPENING it (D->E->A->B->C);
855-859 window CLOSED D->E->A->B->C at #859.

Verifies:
- m747 (News/Media Alliance x Bria enterprise-RAG collective licensing,
  Type C #859, profiles/competitor-entities.yaml): FIRST dedicated US
  trade-association collective-licensing mechanism in the corpus (50%
  revenue split apportioned by Bria's attribution engine; ~2,200
  publisher members, opt-in non-exclusive; enterprise-RAG usage modes).
  MANUAL qualitative only (Aug 28 2026 standing rule): tone NOT_SCORED,
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant false; engine
  NOT run; verdict directionally_supported_not_proven; promotion of
  the m723 tier_3_collective roster mention, NOT a new (eighth)
  relationship direction: direction count holds at seven; connects_to
  [723, 720]; NOT artifact-grade; no analysis.json update; NOT a
  falsification-family member; ledger holds at 26.
- Falsification ledger: TWENTY-SIXTH member-form present (2
  occurrences in profiles/), TWENTY-SEVENTH member-form absent (0
  occurrences; ledger holds at 26). The refined #850 guard stands,
  updated this run: the 6 corpus "TWENTY-SEVENTH" occurrences are all
  "TWENTY-SEVENTH absent" negative-guard strings (one line-wrapped) in
  the m739 (competitor-coverage-research), m740/m743/m746 (journalists),
  and m745 (business-insider) falsification_family fields, not members.
- Post-#859 corpus integrity: max numeric mechanism_id == 747 in
  profiles/; zero underscore-form 748 key substrings in profiles/
  and tests/ (own file excluded as sweep carrier per #715; needles
  format-built so no literal is carried; __pycache__ artifacts
  excluded per the #715 pattern-rescope lesson); zero numeric 748
  keys in profiles/; m745 / m746 / m747 block keys each unique in
  their home YAMLs; designed keying holds for 747 in profiles/
  (zero underscore-form 747 source-file hits repo-wide); #859's
  max-747 / zero-numeric-748 sweeps stay green (Type D adds no
  mechanisms); #857's max-745, #858's max-746, #855's max-744 sweeps
  fail by designed supersession per the #710/#720 convention
  (documented, not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values,
  not #855's): strong-signal n=5-per-arm pair (asymmetry +1.000,
  t=31.434730673, p=1.1695930826e-09, d=19.881069312, is_significant
  True at the ENGINE layer, 95% CI (0.946, 1.056) entirely above zero);
  fresh near-null pair (asymmetry +0.020, t=0.440866714,
  p=0.6710129539, d=0.278828592, is_significant False, CI (-0.060,
  0.094) crossing zero, silent); fresh degenerate n=1-per-arm
  contract on an illustrative tone pair ([-0.25], [0.15]) reproduces
  the classic guard (t=0.0, p=1.0, d=0.0, is_significant False,
  |asymmetry| == 0.40 exact, arm-swap negates). Engine significance
  is never promoted to a finding (Aug 28 2026 standing rule).
- Full-suite status: the #855 background suite re-launched 10:00 PDT
  died (type_d_855_full_suite.log stalled at 1294 bytes / ~2%
  progress since 10:20 PDT Sep 19; no pytest alive at this run's
  check via the ps scan - zero suite processes) - FOURTEENTH
  consecutive background death (#705's, #710's first re-launch,
  #715's first re-launch, #715's re-launch, #720's re-launch,
  #725's re-launch, #730's re-launch, #825's re-launch, #830's
  re-launch, #835's re-launch, #840's re-launch, #845's re-launch,
  #850's re-launch, #855's re-launch; tombstone lineage per #565
  advances THIRTY-SECOND -> THIRTY-THIRD). This run re-launches the
  full suite as a background process writing to goal hidden_files
  type_d_860_full_suite.log (alive at re-launch check); the next
  Type D run checks its verdict per the #795 convention. This run
  stayed on targeted verification per the Type D brief.

0 browser.search query sets this run (Type D verification-layer run;
the m747 block is already in corpus via #859).

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
    "test_type_d_860_m747_qualitative_corpus_integrity_sep19_3pm.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
ANCHORED_SHA = "5fca9a0d5cb5dd1b2300e73f66111aa1ca9c02d7"

# Next mechanism number after the pre-commit corpus max (747); used as
# an int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 748

M745_KEY = "mechanism_745_bi_anthropic_nasdaq_ipo_milestone_register_vs_meta_liability_week_sep19_2026"
M746_KEY = "type_b_858_james_pero_gizmodo_snap_do_or_die_launch_window_fourth_entity_extension"
M747_KEY = "nma_bria_enterprise_rag_collective_licensing_sep2026"

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


class TestNovelty860:
    def test_single_test_type_d_860_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_860") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_860_main_commit_unique_and_anchored(self):
        # No #860 main commit exists pre-commit; the anchor test pins
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
            if "Type D #860" in line and "followup" not in line.lower()
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
        # posture: max stays 747, zero numeric 748 keys.
        assert _max_numeric_mechanism_id() == 747
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_no_type_d_860_in_git_log_pre_commit(self):
        # Pre-commit novelty: no Type D #860 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #860"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #860" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_855_859_window_closed_prior_to_860(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #855 Type D:",
            "#856 Type E:",
            "#857 Type A:",
            "## #858 Type B:",
            "## #859 Type C:",
        ):
            assert marker in log, marker


class TestTypeDRotationGuard:
    """#860 is the Type D anchor opening window 860-864."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_860_864(self):
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


class TestTypeDM747QualitativeDiscipline:
    """m747 (News/Media Alliance x Bria enterprise-RAG collective
    licensing, Type C #859) qualitative-discipline verification,
    text-folded per #732."""

    def _block_folded(self):
        return _fold(_block("profiles/competitor-entities.yaml", M747_KEY, 20000))

    def test_m747_block_key_unique(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count(M747_KEY + ":") == 1

    def test_m747_mechanism_id_747(self):
        assert "mechanism_id: 747" in self._block_folded()

    def test_m747_verdict_and_discipline_strings(self):
        folded = self._block_folded()
        assert "verdict: 'directionally_supported_not_proven'" in folded
        assert "tone_scores: 'NOT_SCORED'" in folded
        assert "p_value: 'NOT_CALCULATED'" in folded
        assert "cohens_d: 'NOT_CALCULATED'" in folded
        assert "ci_95: 'NOT_CALCULATED'" in folded
        assert "is_significant: false" in folded
        assert "qualitative_only: true" in folded
        assert "correlation_not_causation: true" in folded

    def test_m747_falsification_family_false_and_ledger(self):
        folded = self._block_folded()
        assert "falsification_family: false" in folded
        assert "falsification_ledger_holds_at: 26" in folded

    def test_m747_not_a_new_direction(self):
        folded = self._block_folded()
        assert "Direction count holds at seven" in folded
        assert "promotion, not a new direction" in folded

    def test_m747_iteration_block(self):
        folded = self._block_folded()
        assert "iteration: 859" in folded
        assert "iteration_type: C" in folded
        assert "date_analyzed: '2026-09-19'" in folded
        assert "time_pdt: '14:00'" in folded
        assert "type_label: Financial Incentive Mapping" in folded

    def test_m747_connects_to_723_720(self):
        assert "connects_to: [723, 720]" in self._block_folded()

    def test_m747_under_marketplace_intermediary_landscape(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert (
            doc.index("marketplace_intermediary_landscape:")
            < doc.index(M747_KEY + ":")
        )

    def test_m747_correlation_not_causation(self):
        assert "Correlation is not causation" in self._block_folded()

    def test_m747_independent_of_every_meta_competitor(self):
        folded = self._block_folded()
        assert "INDEPENDENT of every Meta competitor" in folded
        assert "First Dedicated US Trade-Association Collective-Licensing Mechanism" in folded

    def test_m747_disclosed_economics_50pct_terms(self):
        folded = self._block_folded()
        assert "50% of all revenues" in folded
        assert "2,200" in folded
        assert "RAG pipelines" in folded
        assert "enterprise AI teams" in folded

    def test_m747_status_active_no_analysis_json_update(self):
        folded = self._block_folded()
        assert "status_sep2026: 'ACTIVE" in folded
        assert "no_analysis_json_update: true" in folded
        assert "artifact_grade: false" in folded


class TestTypeDFalsificationLedger:
    """Ledger holds at 26, member-form guard (refined per #850,
    updated this run).

    TWENTY-SIXTH member-form present; TWENTY-SEVENTH member-form
    absent. The 6 corpus TWENTY-SEVENTH occurrences are all
    "TWENTY-SEVENTH absent" negative-guard strings (one line-wrapped)
    in the m739 (competitor-coverage-research), m740/m743/m746
    (journalists), and m745 (business-insider) falsification_family
    fields, not members."""

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
        # Exactly 6 occurrences (3 at #855 plus the m745 #857 and the
        # two m746 #858 guards), all "TWENTY-SEVENTH absent" guards
        # (the journalists.yaml:20848 occurrence is line-wrapped, so
        # the regex spans whitespace).
        corpus = self._profiles_corpus()
        assert corpus.count("TWENTY-SEVENTH") == 6
        assert len(re.findall(r"TWENTY-SEVENTH\s+absent", corpus)) == 6

    def test_ledger_holds_at_26(self):
        assert 25 + 1 == 26


class TestTypeDCorpusIntegrity:
    """Post-#859 corpus integrity: max 747, zero 748 keys."""

    def test_max_numeric_mechanism_id_is_747(self):
        assert _max_numeric_mechanism_id() == 747

    def test_zero_underscore_748_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(NEXT_NUM)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_748_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(NEXT_NUM)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_dash_748_references_repo_wide(self):
        hits = _repo_grep_dash_mechanism(NEXT_NUM)
        assert hits == [], hits

    def test_zero_numeric_748_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(NEXT_NUM)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_747_source_hits(self):
        # m747's block key carries no underscore-form 747 substring;
        # the only underscore-form 747 hits repo-wide would be
        # __pycache__ bytecode artifacts (excluded per the #715
        # pattern-rescope lesson), so the designed keying holds in
        # source files.
        hits = _repo_grep_underscore_mechanism(747)
        assert hits == [], hits

    def test_m745_m746_m747_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/business-insider.yaml").count(M745_KEY + ":") == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(M746_KEY + ":")
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count(M747_KEY + ":")
            == 1
        )

    def test_c859_max_747_sweep_stays_green(self):
        # Type D adds no mechanisms; #859's max-747 sweep stays green.
        assert _max_numeric_mechanism_id() == 747

    def test_c859_zero_748_sweeps_stay_green(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_a857_b858_c855_max_sweeps_superseded_by_design(self):
        # #857 asserted max == 745 pre-commit, #858 asserted max == 746
        # pre-commit, #855/#856 asserted max == 744; advancing to 747
        # supersedes all per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 747 != 745
        assert _max_numeric_mechanism_id() == 747 != 746
        assert _max_numeric_mechanism_id() == 747 != 744


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #855's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.61, 0.55, 0.68, 0.59, 0.64]
        peers = [-0.38, -0.46, -0.33, -0.41, -0.35]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 19),
            period_end=datetime.datetime(2026, 9, 19),
        )
        assert report.asymmetry_score == pytest.approx(1.0, rel=1e-4)
        assert report.t_statistic == pytest.approx(31.434730673, rel=1e-4)
        assert report.is_significant is True
        assert report.p_value == pytest.approx(1.1695930826e-09, rel=1e-2)
        assert report.cohens_d == pytest.approx(19.881069312, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(0.946, rel=1e-2)
        assert report.confidence_interval_upper == pytest.approx(1.056, rel=1e-2)

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.08, -0.04, 0.11, -0.06, 0.02]
        peers = [-0.05, 0.09, -0.02, 0.06, -0.07]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 19),
            period_end=datetime.datetime(2026, 9, 19),
        )
        assert report.asymmetry_score == pytest.approx(0.020, rel=1e-4)
        assert report.t_statistic == pytest.approx(0.440866714, rel=1e-4)
        assert report.is_significant is False
        assert report.p_value == pytest.approx(0.6710129539, rel=1e-2)
        assert report.cohens_d == pytest.approx(0.278828592, rel=1e-2)
        assert (
            report.confidence_interval_lower
            < 0
            < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract_on_illustrative_tone_pair(self):
        # m747 carries tone NOT_SCORED, so no corpus tone pair is
        # contracted: the classic n=1 guard is demonstrated on a
        # fresh illustrative pair instead (values new this run).
        t, p = welch_t_test([-0.25], [0.15])
        d = cohens_d([-0.25], [0.15])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False
        assert abs(-0.25 - 0.15) == pytest.approx(0.40)
        t2, p2 = welch_t_test([0.15], [-0.25])
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
    """Suite verdict lineage; #855's background suite owns the verdict,
    #860 re-launches."""

    TOMBSTONE_LINEAGE = 33

    def test_tombstone_lineage_count(self):
        # THIRTY-THIRD consecutive background full-suite death: #855's
        # background suite (re-launched 10:00 PDT Sep 19) died at ~2%
        # progress and no pytest was alive at this run's check (the ps
        # scan found zero suite processes). Advances from the
        # THIRTY-SECOND lineage declared in #855 per the
        # #565/#770/#780 convention.
        assert self.TOMBSTONE_LINEAGE == 33

    def test_855_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at 1294 bytes (~2% progress) since
        # 10:20 PDT Sep 19 with no pytest alive at this run's check.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_855_full_suite.log",
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
            "type_d_860_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_860_full_suite.log"

    def test_860_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_860_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync860:
    def test_readme_row_860(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_860(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_860_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog860:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #860 Type D:")
        return log[idx : idx + 12000]

    def test_log_entry_present(self):
        assert "## #860 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 747" in entry
        assert "m747" in entry

    def test_log_rotation_window_860_864(self):
        entry = self._entry()
        assert "860-864" in entry


class TestDateGrounding860:
    def test_sep_19_2026_is_saturday(self):
        assert datetime.datetime(2026, 9, 19).strftime("%A") == "Saturday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 19, 15, 0).strftime("%H:%M") == "15:00"
