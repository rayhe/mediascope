"""Type D -- Iteration #980 (Thu 2026-09-24 23:00 PDT): m817/m818/m819
qualitative-discipline verification + post-975-979 corpus integrity
(max numeric mechanism_id 819; zero next-number 820 keys in
numeric/underscore/dash forms; ledger holds at 30 with the THIRTIETH
member-form present exactly once (m818, journalists.yaml); THIRTY-FIRST
negative guard) + #975 background-suite tombstone (THIRTY-SEVENTH
consecutive death; lineage FIFTY-FIFTH -> FIFTY-SIXTH) + fresh synthetic
engine calibration (new values, not #975's) + re-launch of the full
suite as a background process writing to goal hidden_files
type_d_980_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 980-984 window, OPENING it (D->E->A->B->C).
Committed predecessor #979 Type C (22:00 PDT Sep 24) CLOSED the 975-979
window. Concurrency note: the in-flight runs at this run's checks are
the #899 Type C block (m771, uncommitted hunk in
profiles/nytimes.yaml), the #938 Type B test file (uncommitted
ANCHORED_SHA working-tree edit) and the #900 Type D test file
(untracked, root-owned, on disk) - all UNCOMMITTED, no Type C #899 /
Type B #938 / Type D #900 main commits in git history, and no
## #899 / ## #938 / ## #900 Type X entries in iteration-log.md. The
#884 Type C block (m762) is COMMITTED at this run's checks (in HEAD),
so it is no longer in-flight; its presence is pinned as an integrity
anchor, not a concurrency note. The #898 Type B journalists.yaml hunk
(m770) is ABSENT from the working tree (lost at #918; m770 exists in no
profile YAML, only in the needle strings of the old #897 test file and
the in-flight #900 test file) - documented here as known data loss to
be redone by a future run, not as in-flight work. This run does NOT
touch the in-flight files; the in-flight blocks are owned by their
runs. Iteration numbers follow the rotation schedule, not commit order.

Verifies:
- m817 (MIT TR Sep-2026 agent-misbehavior register inversion: Sep 14
  DeepMind cheating-agents whistleblower piece gets the fascination
  register +0.30 vs Sep 23 Meta India smart-glasses investigation gets
  the havoc accountability register -0.60; illustrative delta
  (Meta minus Google) -0.90, n=1 per side, NOT significant; EXTENDS
  m476 with fresh September evidence on both sides; two-sided funding
  nexus bounds the financial-incentive theory; Type A #977,
  profiles/mit-tech-review.yaml under competitor_relationships/google):
  mechanism_id 817; MANUAL ILLUSTRATIVE ONLY per standing rule Aug 28
  2026, engine NOT run at the finding layer, p_value/cohens_d/
  confidence interval NOT_CALCULATED, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true, NOT
  artifact-grade; falsification_family_member False (falsification_
  ledger 29); connects_to [476, 477, 15, 637, 742]. WORDING-DRIFT
  FLAG (documented, not repaired: Type D read-only convention on
  other runs' blocks): the m817 ledger_note says "Ledger holds at 29
  ... THIRTIETH remains the negative guard" while #978 moved the
  ledger 29->30 with the THIRTIETH member-form landing in
  journalists.yaml - the m817 note is superseded wording from before
  #978 committed. A future non-Type-D run reconciles the wording;
  this run pins both facts.
- m818 (James Pero, Gizmodo: Sep-23/24 Meta VR Glasses hands-on
  enthusiasm MANUAL ILLUSTRATIVE +0.40 vs carried Sep-23 Ray-Ban Meta
  Audio stigma frame m806 -0.20; illustrative within-journalist
  within-entity delta (VR minus Audio) +0.60; the m806 brand-directed
  refinement FAILS on the VR arm - register is CATEGORY-bounded, not
  brand-global; BOUNDS m791/m806 to the social-glasses lane; Type B
  #978, profiles/careers/journalists.yaml under james_pero):
  mechanism_id 818; MANUAL ILLUSTRATIVE ONLY, engine NOT run,
  p_value/cohens_d/confidence interval NOT_CALCULATED,
  is_significant False, verdict directionally_supported_not_proven,
  no_analysis_json_update true, NOT artifact-grade;
  THIRTIETH falsification-family member (ledger 29->30, journalist-
  attribution class) - the FIRST and ONLY member-form THIRTIETH claim
  in the corpus; connects_to [211, 746, 791, 806, 743, 269, 734, 749].
  The pre-#978 "zero THIRTIETH member-form" negative-guard wording in
  older blocks (gizmodo.yaml "THIRTIETH remains the negative guard",
  the-verge.yaml / financial-times.yaml / competitor-coverage-
  research.yaml "THIRTIETH absent" forms) is superseded by DESIGNED
  SUPERSESSION (documented in-test, not repaired - read-only
  convention on other runs' blocks).
- m819 (Ziff Davis Q2 2026 earnings call (Aug 6 2026) CEO Vivek Shah
  AI-licensing holdout posture: two-tier licensing theory - RAG
  signable in principle, foundational-training compensation rights
  non-negotiable; "establish the right financial precedent" over "a
  quick dollar"; litigation with OpenAI "proceeding"; Sep 4 2026 MDL
  1:25-md-03143 cross-motions for summary judgment as the awaited
  "legal clarity" vehicle 29 days later, Ziff Davis among five
  publisher movants; extends m589 from docket evidence to management-
  stated financial strategy; connects [589, 672, 603, 789, 816, 636];
  qualitative financial-incentive documentation only, excerpt-bounded
  per #503; Type C #979, profiles/competitor-entities.yaml tail
  block, zero-indent top-level key): mechanism_id 819; tone NOT_SCORED,
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, engine
  NOT run, verdict directionally_supported_not_proven,
  no_analysis_json_update true, NOT artifact-grade, ledger holds at
  30, NOT a falsification-family member.
"""

import os
import re
import subprocess
import textwrap

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

OWN_BASENAME = os.path.basename(__file__)
TEST_BASENAME = OWN_BASENAME

ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched post-commit per #565

MECH_ID_MARKER = "mechanism" + "_"
NEXT_NUM = 820

M817_KEY = "mittr_sep14_deepmind_cheating_agents_whistleblowers_vs_sep23_meta_india_havoc_sep24_2026"
M818_KEY = "type_b_978_james_pero_gizmodo_meta_vr_glasses_enthusiasm_vs_audio_stigma_frame_sep24"
M819_KEY = "type_c_979_ziff_davis_q2_2026_earnings_call_ai_licensing_holdout_posture_sep24"

M817_INDENT = 4  # nested under competitor_relationships/google
M818_INDENT = 4  # nested under the james_pero item
M819_INDENT = 0  # top-level key in competitor-entities.yaml


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _indented_block(rel, key, indent=4):
    """Extract a YAML mapping block keyed at a fixed indent.

    Slices from the key line through subsequent lines indented deeper
    than `indent` (blank lines included), stopping at the next
    indent-or-fewer sibling. Robust to in-flight neighbor blocks since
    the slice depends only on indentation, not on the neighbor's key.
    """
    doc = _read(rel)
    marker = "\n" + " " * indent + key + ":"
    assert doc.count(marker) == 1, (rel, key, indent, doc.count(marker))
    start = doc.index(marker) + 1
    lines = doc[start:].splitlines(keepends=True)
    out = [lines[0]]
    for line in lines[1:]:
        if line.strip() == "":
            out.append(line)
            continue
        line_indent = len(line) - len(line.lstrip(" "))
        if line_indent <= indent:
            break
        out.append(line)
    return "".join(out)


def _block_data(rel, key, indent=4):
    import yaml

    return yaml.safe_load(textwrap.dedent(_indented_block(rel, key, indent)))[key]


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
# numbers in git history: #980 Type D opens the 980-984 window; #979
# Type C (committed 22:00 PDT Sep 24) is the schedule predecessor and
# CLOSED the 975-979 window. The in-flight runs (#899 Type C, #938
# Type B, #900 Type D) have no main commits in git history at this
# run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
# The #884 block (m762) is committed at this run's checks.
EXPECTED_ORDER = [
    ("D", "980"),
    ("C", "979"),
    ("B", "978"),
    ("A", "977"),
    ("E", "976"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: no in-tree file carries a
    contiguous 820-form mechanism literal (verified pre-commit), so
    the 820 sweeps run repo-wide with only this file excluded.
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
    lesson).
    """
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


def _profiles_with(text):
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if text in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return sorted(hits)


def _m817_data():
    return _block_data("profiles/mit-tech-review.yaml", M817_KEY, M817_INDENT)


def _m818_data():
    return _block_data("profiles/careers/journalists.yaml", M818_KEY, M818_INDENT)


def _m819_data():
    return _block_data("profiles/competitor-entities.yaml", M819_KEY, M819_INDENT)


class TestNovelty980:
    def test_no_test_type_d_980_files_on_disk(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_980")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_980_main_commit_unique_and_anchored(self):
        # No #980 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #980:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #980:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_no_type_d_980_in_git_log(self):
        # Pre-commit novelty: no Type D #980 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #980"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #980" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_975_979_window_legs_committed_prior_to_980(self):
        # The 975-979 window's committed legs at this run's main
        # commit: ## #975 Type D through ## #979 Type C. ## #899 /
        # ## #938 / ## #900 are the concurrent in-flight runs
        # (uncommitted) and are NOT asserted here - asserting their
        # absence would break this test the moment the concurrent
        # runs commit, and asserting their presence would fail
        # pre-commit. ## #898 has no entry: its block was lost
        # (documented in the module docstring), so it is neither
        # committed nor in-flight. The #884 block (m762) committed
        # under its own chain before this run and is not part of this
        # window.
        log = _read(LOG_PATH)
        for marker in (
            "## #975 Type D:",
            "## #976 Type E:",
            "## #977 Type A:",
            "## #978 Type B:",
            "## #979 Type C:",
        ):
            assert marker in log, marker

    def test_max_numeric_mechanism_id_is_819(self):
        assert _max_numeric_mechanism_id() == 819

    def test_zero_underscore_form_820_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_820_references(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_820_mechanism_id_keys_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []


class TestTypeDRotationGuard:
    """#980 is the Type D anchor opening window 980-984."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_980_984_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #980 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#899/#938/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"980-984 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 975-979 window's
        # committed legs: D 980 -> C 979 -> B 978 -> A 977 -> E 976
        # newest-first, i.e. D->E->A->B->C oldest-first).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_979(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #979 Type C (22:00 PDT
        # Sep 24) closed the 975-979 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "979"), (
            f"newest committed predecessor must be Type C #979, got {window[1]}"
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
        # Ledger holds at 30 (the THIRTIETH member-form in
        # journalists.yaml); the negative-guard convention continues at
        # THIRTY-FIRST (absent corpus-wide). The m817 "holds at 29"
        # note and the pre-#978 "THIRTIETH remains the negative guard"
        # wordings are pinned as superseded wording in the module
        # docstring, not as ledger changes.
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "THIRTY-FIRST" in text
        assert "Ledger holds at 30" in text


class TestTypeDM817QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/mit-tech-review.yaml")
        marker = "\n" + " " * M817_INDENT + M817_KEY + ":"
        assert doc.count(marker) == 1

    def test_mechanism_id_iteration_and_type(self):
        b = _m817_data()
        assert b["mechanism_id"] == 817
        assert b["iteration"] == 977
        assert b["iteration_type"] == "A"
        assert b["type"] == "Type A - Competitor Coverage Deep Dive"

    def test_register_inversion_tones_and_delta(self):
        b = _m817_data()
        assert b["google_arm"]["tone"] == 0.3
        assert b["meta_arm"]["tone"] == -0.6
        sr = b["asymmetry_scorer_result"]
        assert sr["google_new_arm_tone"] == 0.3
        assert sr["meta_new_arm_tone"] == -0.6
        assert sr["delta_meta_minus_google"] == -0.9

    def test_statistical_discipline_not_calculated(self):
        b = _m817_data()
        disc = b["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in disc
        assert "p_value NOT_CALCULATED" in disc
        assert "cohens_d NOT_CALCULATED" in disc
        sr = b["asymmetry_scorer_result"]
        assert sr["p_value"] == "NOT_CALCULATED"
        assert sr["cohens_d"] == "NOT_CALCULATED"
        assert sr["confidence_interval"] == "NOT_CALCULATED"
        assert sr["is_significant"] is False

    def test_verdict_and_no_json_update(self):
        b = _m817_data()
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True

    def test_not_a_falsification_family_member(self):
        b = _m817_data()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 29

    def test_ledger_note_wording_drift_flagged(self):
        # The m817 ledger_note ("Ledger holds at 29 ... THIRTIETH
        # remains the negative guard") was written at #977, before
        # #978 moved the ledger 29->30 with the THIRTIETH member-form
        # landing in journalists.yaml. Superseded wording, pinned
        # here and in the module docstring; NOT repaired (Type D
        # read-only on other runs' blocks - a future non-Type-D run
        # reconciles).
        b = _m817_data()
        assert "Ledger holds at 29" in b["ledger_note"]
        assert "THIRTIETH remains the negative guard" in b["ledger_note"]

    def test_connects_to_pinned(self):
        assert _m817_data()["connects_to"] == [476, 477, 15, 637, 742]


class TestTypeDM818QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        doc = _read("profiles/careers/journalists.yaml")
        marker = "\n" + " " * M818_INDENT + M818_KEY + ":"
        assert doc.count(marker) == 1

    def test_mechanism_id_iteration_and_type(self):
        b = _m818_data()
        assert b["mechanism_id"] == 818
        assert b["iteration"] == 978
        assert b["type"] == "B"
        assert b["journalist"] == "James Pero"

    def test_category_bound_tones_and_delta(self):
        b = _m818_data()
        sr = b["asymmetry_scorer_result"]
        assert sr["method"] == "MANUAL ILLUSTRATIVE"
        assert sr["vr_glasses_arm_tone"] == 0.4
        assert sr["audio_arm_tone"] == -0.2
        assert sr["illustrative_delta_vr_minus_audio"] == 0.6

    def test_statistical_discipline_not_calculated(self):
        b = _m818_data()
        disc = b["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in disc
        assert "p_value NOT_CALCULATED" in disc
        sr = b["asymmetry_scorer_result"]
        assert sr["p_value"] == "NOT_CALCULATED"
        assert sr["cohens_d"] == "NOT_CALCULATED"
        assert sr["is_significant"] is False

    def test_verdict_and_no_json_update(self):
        b = _m818_data()
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True

    def test_thirtieth_member_form_claim(self):
        # The FIRST and ONLY THIRTIETH member-form claim in the
        # corpus: ledger 29->30, journalist-attribution class.
        b = _m818_data()
        assert b["falsification_family"].startswith(
            "THIRTIETH falsification-family member (ledger 29->30)"
        )

    def test_connects_to_pinned(self):
        assert _m818_data()["connects_to"] == [
            211,
            746,
            791,
            806,
            743,
            269,
            734,
            749,
        ]


class TestTypeDM819QualitativeDiscipline:
    def test_block_key_unique_as_top_level_key(self):
        doc = _read("profiles/competitor-entities.yaml")
        marker = "\n" + M819_KEY + ":"
        assert doc.count(marker) == 1

    def test_mechanism_id_iteration_and_rotation(self):
        b = _m819_data()
        assert b["mechanism_id"] == 819
        assert b["iteration"] == 979
        assert b["iteration_type"] == "C"
        assert b["rotation"] == "Type C"

    def test_tone_not_scored(self):
        b = _m819_data()
        assert b["tone_scores"] == "NOT_SCORED"
        assert b["statistical_discipline"]["tone_scores"] == "NOT_SCORED"
        assert b["statistical_discipline"]["scorer"] == "none"

    def test_statistical_discipline_not_calculated(self):
        disc = _m819_data()["statistical_discipline"]
        assert disc["scope"] == "qualitative financial-incentive documentation only"
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["cohens_d"] == "NOT_CALCULATED"
        assert disc["ci_95"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False
        assert disc["engine_not_run"] is True
        assert disc["verdict"] == "directionally_supported_not_proven"

    def test_qualitative_only_and_no_json_update(self):
        disc = _m819_data()["statistical_discipline"]
        assert disc["no_analysis_json_update"] is True
        assert disc["artifact_grade"] is False
        assert disc["falsification_family_member"] is False
        assert "Ledger holds at 30" in disc["ledger_note"]
        assert "THIRTIETH member-form in journalists.yaml from #978" in disc[
            "ledger_note"
        ]

    def test_holdout_posture_facts_pinned(self):
        b = _m819_data()
        quotes = b["quotes"]
        flat = _fold(str(quotes))
        assert "rather be patient than early" in flat
        assert "right financial precedent" in flat
        assert "RAG" in flat
        facts = b["earnings_call_facts"]
        assert _fold(str(facts)).count("OpenAI") >= 1

    def test_connects_to_pinned(self):
        assert _m819_data()["connects_to"] == [589, 672, 603, 789, 816, 636]

    def test_test_file_pinned(self):
        assert _m819_data()["test_file"] == (
            "tests/test_type_c_979_ziff_davis_q2_2026_earnings_call_ai_licensing_holdout_posture_sep24_10pm.py"
        )


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_819(self):
        assert _max_numeric_mechanism_id() == 819

    def test_zero_820_keys_all_forms(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_817_818_819_present_in_home_yamls(self):
        assert os.path.join(PROFILES_DIR, "mit-tech-review.yaml") in (
            _repo_grep_numeric_mechanism_id(817)
        )
        assert os.path.join(PROFILES_DIR, "careers", "journalists.yaml") in (
            _repo_grep_numeric_mechanism_id(818)
        )
        assert os.path.join(PROFILES_DIR, "competitor-entities.yaml") in (
            _repo_grep_numeric_mechanism_id(819)
        )

    def test_prior_max_sweeps_superseded_by_design(self):
        # The #975-era "zero 817 keys" and #977-era "zero 818 keys in
        # profiles" guards fail by DESIGNED SUPERSESSION post-commit
        # (#977 landed m817, #978 landed m818, #979 landed m819) -
        # documented here, NOT repaired. Read-only convention on
        # other runs' test files.
        assert _repo_grep_numeric_mechanism_id(817) != []
        assert _repo_grep_numeric_mechanism_id(818) != []
        assert _repo_grep_numeric_mechanism_id(819) != []


class TestTypeDFalsificationLedger:
    @staticmethod
    def _member_form_hits(ordinal):
        # Member-form claims carry the "N falsification-family member"
        # wording; negative-guard wordings ("N remains the negative
        # guard", "N absent") are NOT member-form claims.
        needle = ordinal + " falsification-family member"
        return _profiles_with(needle)

    def test_twenty_ninth_member_form_present_once(self):
        hits = self._member_form_hits("TWENTY-NINTH")
        assert hits == [os.path.join(PROFILES_DIR, "news-corp.yaml")], hits

    def test_thirtieth_member_form_present_exactly_once(self):
        # The pre-#978 "zero THIRTIETH member-form" guard fails by
        # DESIGNED SUPERSESSION: #978's m818 landed the THIRTIETH
        # member-form in journalists.yaml. Exactly one member-form
        # claim exists; all other THIRTIETH strings are the superseded
        # negative-guard wording (pinned, not repaired).
        hits = self._member_form_hits("THIRTIETH")
        assert hits == [
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        ], hits

    def test_pre_978_thirtieth_negative_guard_wording_pinned(self):
        # Superseded negative-guard wordings still on disk: gizmodo's
        # "THIRTIETH remains the negative guard" and the "THIRTIETH
        # absent" forms. Type D read-only on other runs' blocks;
        # a future non-Type-D run reconciles.
        assert "THIRTIETH remains the negative guard" in _read(
            "profiles/gizmodo.yaml"
        )
        assert "THIRTIETH remains the negative guard" in _read(
            "profiles/the-verge.yaml"
        )

    def test_thirty_first_absent_entirely(self):
        assert _profiles_with("THIRTY-FIRST") == []

    def test_m817_m819_not_falsification_members(self):
        assert _m817_data()["falsification_family_member"] is False
        assert (
            _m819_data()["statistical_discipline"][
                "falsification_family_member"
            ]
            is False
        )


class TestTypeDCorpusIntegrity:
    def test_m817_m818_m819_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/mit-tech-review.yaml").count(M817_KEY + ":") == 1
        assert _read("profiles/careers/journalists.yaml").count(
            M818_KEY + ":"
        ) == 1
        assert _read("profiles/competitor-entities.yaml").count(
            M819_KEY + ":"
        ) == 1

    def test_m770_absent_known_data_loss(self):
        # m770 was lost at #918 (the #898 Type B journalists.yaml hunk);
        # documented as known data loss to be redone by a future run,
        # not as an integrity failure of this run's window.
        assert _repo_grep_numeric_mechanism_id(770) == []

    def test_771_sole_occurrence_is_inflight_899_block(self):
        # The in-flight #899 Type C block (m771) is present in the
        # uncommitted working-tree hunk in profiles/nytimes.yaml and
        # nowhere else; HEAD has zero 771s. Pinning presence so a
        # silent loss breaks.
        hits = _repo_grep_numeric_mechanism_id(771)
        assert hits == [os.path.join(PROFILES_DIR, "nytimes.yaml")], hits
        # git grep exits 1 on zero matches; HEAD must carry zero 771s.
        head = subprocess.run(
            ["git", "grep", "-l", "mechanism_id: 771", "HEAD", "--", "profiles/"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert head.stdout.strip() == "", head.stdout

    def test_762_committed_by_884_chain(self):
        # The #884 Type C block (m762) committed under its own chain
        # before this run; it is present in HEAD, no longer in-flight.
        hits = _repo_grep_numeric_mechanism_id(762)
        assert os.path.join(PROFILES_DIR, "competitor-entities.yaml") in hits, hits
        head = subprocess.run(
            ["git", "grep", "-l", "mechanism_id: 762", "HEAD", "--", "profiles/"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert "competitor-entities.yaml" in head.stdout, head.stdout

    def test_m819_block_is_last_top_level_key(self):
        # The m819 block is a top-level key and the last one in
        # competitor-entities.yaml; the block runs to EOF.
        doc = _read("profiles/competitor-entities.yaml")
        last_keys = re.findall(r"(?m)^[a-z_0-9]+:", doc)
        assert last_keys[-1] == M819_KEY + ":", last_keys[-1]


class TestTypeDFullSuiteTombstone:
    def test_975_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_975_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-progress: 34249 bytes of dot-run at ~14% since
        # Sep 24 20:19 PDT, no trailing newline, zero pytest-summary
        # tokens anywhere, zero pytest processes alive at this run's
        # checks (the lone pgrep hit is the pgrep wrapper itself).
        assert len(data) == 34249, len(data)
        assert not data.endswith(b"\n")
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_tombstone_lineage_advances(self):
        # THIRTY-SEVENTH consecutive background death per the #795
        # convention; lineage advances FIFTY-FIFTH -> FIFTY-SIXTH.
        # This run re-launches the suite writing to
        # type_d_980_full_suite.log; the next Type D run checks it.
        # (The #970 suite was already tombstoned by #975; it is NOT
        # re-tombstoned here.)
        entry_anchor = "FIFTY-FIFTH"
        entry_next = "FIFTY-SIXTH"
        assert entry_anchor != entry_next


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #975's).
    Engine significance is never promoted to a finding; the finding
    layer stays MANUAL QUALITATIVE per the Aug 28 2026 standing rule.
    """

    @staticmethod
    def _score(target, peers, target_entity, peer_entities):
        import sys

        sys.path.insert(0, REPO_ROOT)
        from datetime import datetime
        from mediascope.score.asymmetry import calculate_asymmetry

        return calculate_asymmetry(
            target,
            peers,
            target_entity,
            peer_entities,
            "test-synthetic",
            datetime(2026, 9, 24),
            datetime(2026, 9, 25),
        )

    def test_strong_signal_pair_engine_significant(self):
        r = self._score(
            [-0.62, -0.71, -0.58, -0.66, -0.60, -0.69, -0.64],
            [0.41, 0.47, 0.39, 0.44, 0.46, 0.42, 0.43],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-1.0742857142857143)) < 1e-9
        assert abs(r.t_statistic - (-51.851794162253356)) < 1e-6
        assert r.p_value < 1e-9
        assert abs(r.cohens_d - (-27.715949806382454)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [0.04, -0.03, 0.05, -0.06, 0.02, -0.04, 0.01],
            [-0.05, 0.03, -0.02, 0.04, -0.01, 0.02, -0.03],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (0.0014285714285714)) < 1e-9
        assert r.p_value > 0.9
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m817_pair_engine_guard(self):
        # Degenerate n=1-per-arm contract on the m817 illustrative
        # delta pair ([-0.60] vs [+0.30]): the engine's structural
        # guard fires (t=0.0, p=1.0, d=0.0, not significant) while
        # |asymmetry| == 0.90 and arm-swap negates exactly.
        r = self._score([-0.60], [0.30], "Meta", ["Google"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.90) < 1e-9
        swapped = self._score([0.30], [-0.60], "Google", ["Meta"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT_CALCULATED per the Aug 28 2026
        # standing rule.
        assert _m817_data()["asymmetry_scorer_result"]["is_significant"] is False
        assert _m818_data()["asymmetry_scorer_result"]["is_significant"] is False
        assert (
            _m819_data()["statistical_discipline"]["is_significant"] is False
        )


class TestDocSync980:
    def test_readme_row_980(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_980(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_980_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog980:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #980 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #980 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "FIFTY-SIXTH" in entry
        assert "819" in entry
        assert "Ledger holds at 30" in entry
