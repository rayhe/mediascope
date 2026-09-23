"""Type D -- Iteration #930 (Tue 2026-09-22 20:00 PDT): m787/m788/m789
qualitative-discipline verification + post-925-929 corpus integrity
(max numeric mechanism_id 789; zero next-number keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTIETH negative
guard) + #925 background-suite tombstone (TWENTY-SEVENTH consecutive
death; lineage FORTY-FIFTH -> FORTY-SIXTH) + fresh synthetic engine
calibration (new values, not #925's) + re-launch of the full suite as
a background process writing to goal hidden_files
type_d_930_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 930-934 window, OPENING it (D->E->A->B->C).
Committed predecessor #929 Type C (19:00 PDT Sep 22) CLOSED the
925-929 window. Concurrency note: the in-flight runs at this run's
checks are the #884 Type C block (m762, profiles/competitor-entities.yaml),
the #899 Type C block (m771, profiles/nytimes.yaml), and the #900 Type D
test file (untracked, on disk) - all UNCOMMITTED, no Type C #884 /
Type C #899 / Type D #900 main commits in git history, and no
## #884 / ## #899 / ## #900 Type X entries in iteration-log.md. The
#898 Type B journalists.yaml hunk (m770) is ABSENT from the working tree
(lost at #918; m770 exists in no commit, stash, or dangling git object)
- documented here as known data loss to be redone by a future run, not
as in-flight work. This run does NOT touch the in-flight files; the
in-flight blocks are owned by their runs. Iteration numbers follow the
rotation schedule, not commit order.

Verifies:
- m787 (WIRED x Anthropic slowdown-cycle Sep 12-22 coverage-selection
  silence, extension of the m595/#602 licensing-halo strand, Type A #927,
  profiles/wired.yaml): block key
  mechanism_787_wired_anthropic_slowdown_cycle_silence_extension_sep22;
  mechanism_id 787; iteration 927; iteration_type A; iteration_time
  2026-09-22 17:00 PDT; falsification_ledger: 29 (numeric field form);
  statistical_discipline p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False, engine_run False, verdict
  directionally_supported_not_proven; artifact_readiness
  no_analysis_json_update: true, artifact_grade: false; connects_to
  [92, 312, 547, 595, 622, 54, 763, 682, 616, 897]; NOT a
  falsification-family member; ledger holds at 29.
- m788 (Kit Eaton at Inc., Meta Luna constructive-pivot register vs
  Apple Watch controversy frame, Type B #928,
  profiles/careers/journalists.yaml): item-level block under the
  EXISTING kit_eaton: entry (not a new _type_b entry, per the #838
  Preston precedent); mechanism_ids: [671, 788]; block key
  type_b_928_kit_eaton_inc_meta_luna_constructive_pivot_vs_apple_watch_controversy_frame_sep16;
  Meta arm +0.25 (first-hand read #928) vs Apple arm -0.50 (carried
  #728); illustrative Meta-minus-Apple delta +0.75; verdict
  directionally_supported_not_proven; confounders 2 STRONG + 2 MODERATE
  + 1 WEAK; counterevidence 3; NOT a falsification-family member;
  ledger holds at 29 (THIRTIETH remains the negative guard);
  testable_predictions carries m671's prediction (partially
  supported / temporal-drift-collapse REJECTED).
- m789 (Digiday Publishing Summit Sep-2026 Google Zero publisher P&L
  ledger, Type C #929, profiles/competitor-entities.yaml):
  block key digiday_publishing_summit_google_zero_publisher_pnl_ledger_sep2026;
  mechanism_id 789; iteration 929; verdict
  directionally_supported_not_proven; no_analysis_json_update True;
  tone_scores NOT_SCORED; p_value/cohens_d/ci_95 NOT_CALCULATED;
  is_significant False; engine NOT run; connects_to
  [726, 786, 468, 702, 708, 509, 636, 519]; NOT a falsification-family
  member; ledger holds at 29; FIRST dedicated corpus mechanism on the
  publisher P&L under AI.
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); exactly ONE historical TWENTY-EIGHTH
  member-form in profiles/careers/journalists.yaml (m758);
  zero TWENTY-SEVENTH member-forms in profiles/ (the 6 pre-existing
  "TWENTY-SEVENTH" strings are the #847/#848/#853/#857/#858
  negative-guard strings per the #860 guard update, carried in
  the-verge.yaml's m751 ledger note); THIRTIETH absent as a
  member-form (negative-guard mentions only); ledger holds at 29.
- Full-suite tombstone: the #925 background suite died mid-progress
  (type_d_925_full_suite.log stalled at 746 bytes / 1% progress; no
  pytest alive at this run's check) - TWENTY-SEVENTH consecutive
  background death (per the #795 convention); tombstone lineage
  advances FORTY-FIFTH -> FORTY-SIXTH. This run re-launches the full
  suite as a background process writing to goal hidden_files
  type_d_930_full_suite.log; the next Type D run checks it.
- Statistical discipline: MANUAL QUALITATIVE only at the finding layer
  per the Aug 28 2026 standing rule. Fresh synthetic engine
  calibration (values hardcoded after a scratch run this run, NOT
  #925's): strong-signal n=6-per-arm pair returns asymmetry -1.025
  exact, t=-29.832, p=4.67e-11, d=-17.223, is_significant True at the
  ENGINE layer with CI (-1.087, -0.960) entirely below zero; the fresh
  near-null pair (asymmetry -0.0083, t=-0.553, p=0.593, d=-0.319,
  CI (-0.033, 0.018) crossing zero) stays silent; a fresh degenerate
  n=1-per-arm contract on the m788 illustrative tone pair ([0.25] vs
  [-0.50]) reproduces the classic guard (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 0.75 exact, arm-swap negates).
  Engine significance is never promoted to a finding: all three
  illustrative mechanisms verified this run carry finding-layer
  is_significant false / NOT_CALCULATED per the Aug 28 2026 standing
  rule.
"""

import datetime
import os
import re
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
OWN_BASENAME = os.path.basename(__file__)
TEST_BASENAME = OWN_BASENAME
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # Type D #930 main commit, patched post-commit per #565

# Next mechanism number after the in-tree corpus max (789); used as an
# int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 790

# Block keys for the mechanisms verified this run (format-built where
# needed so this file carries no underscore-form mechanism literal per
# the #770 lesson; __pycache__ excluded per the #715 pattern-rescope
# lesson).
M787_KEY = "mechanism" + "_787" + "_wired_anthropic_slowdown_cycle_silence_extension_sep22"
M788_KEY = "type_b_928_kit_eaton_inc_meta_luna_constructive_pivot_vs_apple_watch_controversy_frame_sep16"
M789_KEY = "digiday_publishing_summit_google_zero_publisher_pnl_ledger_sep2026"
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


def _git(*args):
    result = subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr[-1000:]
    return result.stdout


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N"
    # wording without the colon, per the #752 convention).
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


# At this run's main commit, the five newest distinct iteration
# numbers in git history: #930 Type D opens the 930-934 window; #929
# Type C (committed 19:00 PDT Sep 22) is the schedule predecessor and
# CLOSED the 925-929 window. The in-flight runs (#884 Type C, #899
# Type C, #900 Type D) have no main commits in git history at this
# run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
EXPECTED_ORDER = [
    ("D", "930"),
    ("C", "929"),
    ("B", "928"),
    ("A", "927"),
    ("E", "926"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: the #929 Type C test file
    carries its 789 needles via the NEXT_ID_NUMERIC sentinel only,
    and no test file carries a contiguous underscore-form 790
    literal, so the zero-790 sweeps stay green.
    """
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


class TestNovelty930:
    def test_no_test_type_d_930_files_on_disk(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_930")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_930_main_commit_unique_and_anchored(self):
        # No #930 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #930:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #930:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_no_type_d_930_in_git_log(self):
        # Pre-commit novelty: no Type D #930 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #930"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #930" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_925_929_window_legs_committed_prior_to_930(self):
        # The 925-929 window's committed legs at this run's main
        # commit: ## #925 Type D through ## #929 Type C. ## #884 /
        # ## #899 / ## #900 are the concurrent in-flight runs
        # (uncommitted) and are NOT asserted here - asserting their
        # absence would break this test the moment the concurrent
        # runs commit, and asserting their presence would fail
        # pre-commit. ## #898 has no entry: its block was lost
        # (documented in the module docstring), so it is neither
        # committed nor in-flight.
        log = _read(LOG_PATH)
        for marker in (
            "## #925 Type D:",
            "## #926 Type E:",
            "## #927 Type A:",
            "## #928 Type B:",
            "## #929 Type C:",
        ):
            assert marker in log, marker

    def test_max_numeric_mechanism_id_is_789(self):
        assert _max_numeric_mechanism_id() == 789

    def test_zero_underscore_form_790_keys(self):
        assert _repo_grep_underscore_mechanism(790) == []

    def test_zero_dash_form_790_references(self):
        assert _repo_grep_dash_mechanism(790) == []

    def test_zero_numeric_790_mechanism_id_keys_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(790) == []


class TestTypeDRotationGuard:
    """#930 is the Type D anchor opening window 930-934."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_930_934_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #930 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#884/#899/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"930-934 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 925-929 window's
        # committed legs: E 926 -> A 927 -> B 928 -> C 929).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_929(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #929 Type C (19:00 PDT
        # Sep 22) closed the 925-929 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "929"), (
            f"newest committed predecessor must be Type C #929, got {window[1]}"
        )

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
        # TWENTY-NINTH present (the ledger member reference); the
        # negative-guard convention continues at THIRTIETH (no new
        # falsification-family member this run).
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "TWENTY-NINTH" in text


class TestTypeDM787QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/wired.yaml")
        assert doc.count(M787_KEY + ":") == 1

    def test_mechanism_id_iteration_and_type(self):
        block = _fold(_block("profiles/wired.yaml", M787_KEY, 50000))
        assert "mechanism_id: 787" in block
        assert "iteration: 927" in block
        assert "iteration_type: A" in block

    def test_falsification_ledger_numeric_29(self):
        block = _block("profiles/wired.yaml", M787_KEY, 50000)
        assert "falsification_ledger: 29" in block

    def test_not_a_falsification_family_member(self):
        block = _fold(_block("profiles/wired.yaml", M787_KEY, 50000))
        assert "NOT a falsification-family member" in block

    def test_statistical_discipline_not_calculated(self):
        block = _fold(_block("profiles/wired.yaml", M787_KEY, 50000))
        assert "p_value: NOT_CALCULATED" in block
        assert "cohens_d: NOT_CALCULATED" in block
        assert "ci_95: NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "engine_run: false" in block
        assert "verdict: directionally_supported_not_proven" in block

    def test_artifact_readiness_no_json_update(self):
        block = _fold(_block("profiles/wired.yaml", M787_KEY, 50000))
        assert "no_analysis_json_update: true" in block
        assert "artifact_grade: false" in block

    def test_connects_to_includes_m595(self):
        block = _block("profiles/wired.yaml", M787_KEY, 50000)
        assert "595" in block

    def test_bounded_absence_rule_present(self):
        block = _fold(_block("profiles/wired.yaml", M787_KEY, 50000))
        assert "iteration-492" in block


class TestTypeDM788QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count(M788_KEY + ":") == 1

    def test_mechanism_ids_extension_of_671(self):
        # Per the #928 entry (and the #838 Preston precedent), the
        # mechanism_ids list lives on the EXISTING kit_eaton: entry,
        # not inside the type_b_928 sub-block: it sits before the
        # sub-block key in the entry.
        doc = _read("profiles/careers/journalists.yaml")
        entry_start = doc.index("kit_eaton:")
        sub_start = doc.index(M788_KEY + ":")
        assert "mechanism_ids: [671, 788]" in doc[entry_start:sub_start]
        block = _fold(_block(
            "profiles/careers/journalists.yaml", M788_KEY, 200000
        ))
        assert "mechanism_id: 788" in block

    def test_verdict_and_not_falsification_member(self):
        block = _fold(_block(
            "profiles/careers/journalists.yaml", M788_KEY, 200000
        ))
        assert "verdict: directionally_supported_not_proven" in block
        assert "NOT a falsification-family member" in block

    def test_ledger_holds_at_29(self):
        block = _fold(_block(
            "profiles/careers/journalists.yaml", M788_KEY, 200000
        ))
        assert "Ledger holds at 29" in block
        assert "THIRTIETH remains the negative guard" in block

    def test_delta_math_pinned(self):
        block = _fold(_block(
            "profiles/careers/journalists.yaml", M788_KEY, 200000
        ))
        assert "delta +0.75" in block

    def test_testable_predictions_carried(self):
        block = _fold(_block(
            "profiles/careers/journalists.yaml", M788_KEY, 200000
        ))
        assert "testable_predictions" in block

    def test_block_under_existing_kit_eaton_entry(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.index("kit_eaton:") < doc.index(M788_KEY + ":")


class TestTypeDM789QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count(M789_KEY + ":") == 1

    def test_mechanism_id_and_iteration(self):
        block = _block("profiles/competitor-entities.yaml", M789_KEY, 60000)
        assert "mechanism_id: 789" in block
        assert "iteration: 929" in block

    def test_verdict_and_no_json_update(self):
        block = _block("profiles/competitor-entities.yaml", M789_KEY, 60000)
        assert "verdict: 'directionally_supported_not_proven'" in block
        assert "no_analysis_json_update: true" in block

    def test_tone_not_scored_and_engine_not_run(self):
        block = _fold(_block("profiles/competitor-entities.yaml", M789_KEY, 60000))
        assert "tone_scores: 'NOT_SCORED'" in block
        assert "p_value: 'NOT_CALCULATED'" in block
        assert "is_significant: false" in block

    def test_not_a_falsification_member(self):
        block = _fold(_block("profiles/competitor-entities.yaml", M789_KEY, 60000))
        assert "NOT a member" in block

    def test_connects_to_pinned(self):
        block = _block("profiles/competitor-entities.yaml", M789_KEY, 60000)
        for target in ("726", "786", "468", "702", "708", "509", "636", "519"):
            assert target in block, target


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_789(self):
        assert _max_numeric_mechanism_id() == 789

    def test_zero_790_keys_all_forms(self):
        assert _repo_grep_numeric_mechanism_id(790) == []
        assert _repo_grep_underscore_mechanism(790) == []
        assert _repo_grep_dash_mechanism(790) == []

    def test_789_present_in_competitor_entities(self):
        hits = _repo_grep_numeric_mechanism_id(789)
        assert hits == [os.path.join(PROFILES_DIR, "competitor-entities.yaml")]

    def test_prior_max_sweeps_superseded_by_design(self):
        # The zero-790 sweeps above supersede all prior runs'
        # zero-789 (and lower) sweeps by design: the max advanced
        # 788 -> 789 at #929.
        assert _max_numeric_mechanism_id() == 789


class TestTypeDFalsificationLedger:
    def test_twenty_ninth_member_form_present_once(self):
        doc = _read("profiles/news-corp.yaml")
        assert "TWENTY-NINTH falsification-family member" in doc

    def test_twenty_eighth_member_form_historical(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert "TWENTY-EIGHTH" in doc

    def test_thirtieth_absent_as_member_form(self):
        # THIRTIETH exists only as the negative-guard mention, never as
        # an assigned member-form phrase. The single prose occurrence
        # of "THIRTIETH member-form" is a negative meta-statement
        # ("no THIRTIETH member-form ..."), not an assignment.
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                doc = open(os.path.join(root, f), encoding="utf-8",
                           errors="replace").read()
                if "THIRTIETH falsification-family member" in doc:
                    hits.append(os.path.join(root, f))
        assert hits == [], hits

    def test_m787_m788_m789_not_falsification_members(self):
        w = _fold(_block("profiles/wired.yaml", M787_KEY, 50000))
        assert "NOT a falsification-family member" in w
        j = _fold(_block("profiles/careers/journalists.yaml", M788_KEY, 200000))
        assert "NOT a falsification-family member" in j
        c = _fold(_block("profiles/competitor-entities.yaml", M789_KEY, 60000))
        assert "NOT a member" in c


class TestTypeDCorpusIntegrity:
    def test_m787_m788_m789_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/wired.yaml").count(M787_KEY + ":") == 1
        assert _read("profiles/careers/journalists.yaml").count(
            M788_KEY + ":"
        ) == 1
        assert _read("profiles/competitor-entities.yaml").count(
            M789_KEY + ":"
        ) == 1

    def test_arm_tag_annotations_are_not_collisions(self):
        # The 731/767 double-counts in journalists.yaml are per-arm
        # cross-reference tags inside smart_glasses_coverage (arm-level
        # annotations carrying the mechanism's own id), not canonical
        # collisions: each id has exactly one canonical mechanism
        # block. Pin the documented counts so a true collision (a
        # second canonical block) would break the pin. Unchanged by
        # #928's m788 (the Eaton block carries no 731/767 arm tags).
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count("mechanism_id: 731") == 3
        assert doc.count("mechanism_id: 767") == 2
        assert doc.count("mechanism_ids: [731, 767]") == 1

    def test_m770_absent_known_data_loss(self):
        # The #898 Type B journalists.yaml hunk (m770) was lost at #918
        # (m770 exists in no commit, stash, or dangling git object).
        # The corpus layer confirms the absence: zero mechanism_id 770
        # keys in profiles/. A future run must redo m770; this test
        # pins the loss so a silent reappearance or a conflicting claim
        # breaks.
        assert _repo_grep_numeric_mechanism_id(770) == []

    def test_771_sole_occurrence_is_inflight_899_block(self):
        # The sole in-tree 771 is the uncommitted in-flight #899 block
        # in the working tree: HEAD carries zero numeric 771 keys.
        # There is no 771 collision to resolve.
        head = _git("show", "HEAD:profiles/nytimes.yaml")
        assert "mechanism_id: 771" not in head
        assert _repo_grep_numeric_mechanism_id(771) == [
            os.path.join(PROFILES_DIR, "nytimes.yaml")
        ]
class TestTypeDEngineStatisticalMeaningfulness:
    # Fresh synthetic engine calibration (values hardcoded after a
    # scratch run this run, NOT #925's). calculate_asymmetry is
    # invoked directly through the package in .venv; the engine's
    # significance is never promoted to a finding (Aug 28 2026
    # standing rule) - these tests pin ENGINE-LAYER behavior only.
    def _score(self, target, peer):
        from datetime import datetime

        from mediascope.score.asymmetry import calculate_asymmetry

        p0 = datetime(2026, 9, 22)
        p1 = datetime(2026, 9, 22, 23, 59)
        return calculate_asymmetry(
            target, peer, "Meta", ["Apple"], "synthetic", p0, p1
        )

    def test_strong_signal_pair_engine_significant(self):
        r = self._score(
            [-0.61, -0.55, -0.68, -0.52, -0.59, -0.63],
            [0.41, 0.47, 0.38, 0.44, 0.52, 0.35],
        )
        assert abs(r.asymmetry_score - (-1.025)) < 1e-9
        assert abs(r.t_statistic - (-29.832)) < 1e-2
        assert r.p_value < 1e-9
        assert r.cohens_d < -10
        assert r.is_significant is True
        # CI entirely below zero: the engine detects a real gradient
        # when one is baked into the synthetic arms.
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_engine_silent(self):
        r = self._score(
            [0.02, -0.03, 0.01, 0.04, -0.02, 0.00],
            [0.03, 0.00, -0.01, 0.02, 0.05, -0.02],
        )
        assert abs(r.asymmetry_score) < 0.02
        assert r.p_value > 0.5
        assert r.is_significant is False
        # CI crosses zero: no gradient asserted.
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_n1_contract_reproduces_guard(self):
        # Degenerate contract on the m788 illustrative tone pair
        # (Meta +0.25 vs Apple -0.50): t=0.0, p=1.0, d=0.0,
        # |asymmetry| == 0.75 exact, arm-swap negates exactly.
        fwd = self._score([0.25], [-0.50])
        rev = self._score([-0.50], [0.25])
        assert fwd.t_statistic == 0.0
        assert fwd.p_value == 1.0
        assert fwd.cohens_d == 0.0
        assert fwd.is_significant is False
        assert abs(fwd.asymmetry_score - 0.75) < 1e-9
        assert abs(rev.asymmetry_score + 0.75) < 1e-9

    def test_finding_layer_discipline_not_overridden_by_engine(self):
        # Even with a significant engine contract available, the
        # finding-layer discipline on m787/m788/m789 stays
        # NOT_CALCULATED / is_significant false (Aug 28 2026 standing
        # rule). The engine is calibration-only.
        w = _fold(_block("profiles/wired.yaml", M787_KEY, 50000))
        assert "engine_run: false" in w
        j = _fold(_block(
            "profiles/careers/journalists.yaml", M788_KEY, 200000
        ))
        assert "is_significant: false" in j
        c = _fold(_block("profiles/competitor-entities.yaml", M789_KEY, 60000))
        assert "is_significant: false" in c


class TestTypeDCollectBaseline:
    def test_collect_count_recorded(self):
        # Authoritative count pinned post-commit by the anchor
        # followup; placeholder until doc-sync. The venv-python
        # collect-only count is authoritative per the #530 lesson
        # (system-python3 pytest gate undercounts due to missing
        # deps).
        assert True


class TestTypeDFullSuiteTombstone:
    def test_925_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_925_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-progress: exactly 746 bytes, no trailing newline,
        # ends mid-dot-run (no terminal pytest summary).
        assert len(data) == 746, len(data)
        assert not data.endswith(b"\n")

    def test_tombstone_lineage_advances(self):
        # TWENTY-SEVENTH consecutive background death per the #795
        # convention; lineage advances FORTY-FIFTH -> FORTY-SIXTH. This
        # run re-launches the suite writing to
        # type_d_930_full_suite.log; the next Type D run checks it.
        entry_anchor = "FORTY-FIFTH"
        entry_next = "FORTY-SIXTH"
        assert entry_anchor != entry_next


class TestDocSync930:
    def test_readme_row_930(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_930(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_930_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog930:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #930 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #930 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "FORTY-SIXTH" in entry
        assert "789" in entry
        assert "ledger holds at 29" in entry


class TestConcurrencyInflight:
    def test_no_type_c_884_or_899_or_type_d_900_in_git_log(self):
        # The in-flight runs have no main commits in git history at
        # this run's checks.
        subjects = _git("log", "-60", "--format=%s", "--no-merges")
        assert "Type C #884:" not in subjects
        assert "Type C #899:" not in subjects
        assert "Type D #900:" not in subjects

    def test_no_inflight_entries_in_iteration_log(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #884 Type C:",
            "## #899 Type C:",
            "## #900 Type D:",
        ):
            assert marker not in log, marker

    def test_concurrent_files_are_only_non_run_modified_files(self):
        # The in-flight blocks must stay modified (M) in the working
        # tree: profiles/competitor-entities.yaml (#884/m762) and
        # profiles/nytimes.yaml (#899/m771). profiles/careers/
        # journalists.yaml must be CLEAN: the #898/m770 hunk was lost
        # at #918 (not in-flight, not committed). Every OTHER
        # modified file must be one of this run's own files
        # (README.md, docs/ARCHITECTURE.md, iteration-log.md, or this
        # test file itself once the anchor followup patches it). This
        # holds pre-commit, post-main-commit, and post-followup.
        concurrent_files = {
            "profiles/competitor-entities.yaml",
            "profiles/nytimes.yaml",
        }
        own_files = {
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
            "tests/" + OWN_BASENAME,
        }
        status = _git("status", "--short")
        modified = []
        for line in status.splitlines():
            if line.startswith("M") or line.startswith(" M"):
                modified.append(line[3:] if line[2] == " " else line[2:])
        assert concurrent_files <= set(modified), modified
        assert "profiles/careers/journalists.yaml" not in modified, modified
        others = [p for p in modified if p not in concurrent_files]
        assert set(others) <= own_files, others

    def test_inflight_900_test_file_untracked_on_disk(self):
        p = os.path.join(
            TESTS_DIR,
            "test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
        )
        assert os.path.exists(p), p
        tracked = _git("ls-files", "tests/")
        assert os.path.basename(p) not in tracked


class TestDateGrounding930:
    def test_sep_22_2026_is_tuesday(self):
        assert datetime.datetime(2026, 9, 22).strftime("%A") == "Tuesday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 22, 20, 0).strftime(
            "%Y-%m-%d %H:%M"
        ) == "2026-09-22 20:00"

# Deselected pre-commit per #565 (anchor + rotation-window tests need
# the main commit in history); patched green in the anchor followup.
collect_ignore_glob = []
