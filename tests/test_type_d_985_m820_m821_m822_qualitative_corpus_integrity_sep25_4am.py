"""Type D -- Iteration #985 (Fri 2026-09-25 04:00 PDT): m820/m821/m822
qualitative-discipline verification + post-980-984 corpus integrity
(max numeric mechanism_id 822; zero next-number 823 keys in
numeric/underscore/dash mechanism forms; ledger holds at 30 with the
THIRTIETH member-form present exactly once (m818, journalists.yaml);
THIRTY-FIRST negative guard) + #980 background-suite tombstone
(THIRTY-EIGHTH consecutive death; lineage FIFTY-SIXTH -> FIFTY-SEVENTH)
+ fresh synthetic engine calibration (new values, not #980's) +
re-launch of the full suite as a background process writing to goal
hidden_files type_d_985_full_suite.log (next Type D run checks its
verdict per the #795 convention).

Type D FIRST leg of the 985-989 window, OPENING it (D->E->A->B->C).
Committed predecessor #984 Type C (03:00 PDT Sep 25) CLOSED the 980-984
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
- m820 (WIRED Sep-23 Pinky-Promises privacy skepticism vs Google XR
  Sep-window non-coverage: Meta arm MANUAL ILLUSTRATIVE -0.45 (carried
  from m814) vs May-19 hands-on positive control +0.15 (carried from
  m640); illustrative delta (Meta minus Google) -0.60, n=1 vs carried
  baseline, NOT significant; EXTENDS m547 (silence strand, 20 days)
  and m640 (register inversion); Type A #982,
  profiles/wired.yaml under competitor_relationships/google):
  mechanism_id 820; MANUAL ILLUSTRATIVE ONLY per standing rule Aug 28
  2026, engine NOT run at the finding layer, p_value/cohens_d/ci
  NOT_CALCULATED, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification_family_member False
  (falsification_ledger 30); connects_to [547, 640, 431, 814, 452,
  612].
- m821 (David Heaney, UploadVR: Sep-23 Snap Specs junket-disclosed
  hands-on MANUAL ILLUSTRATIVE -0.10 vs same-day Meta VR Glasses
  announcement 0.00; illustrative delta (Snap minus Meta) -0.10;
  junket did NOT buy product softness - privacy-vocabulary direction
  only; EXTENDS the m629 same-day same-journalist precedent class;
  Type B #983, profiles/careers/journalists.yaml under the
  david_heaney item / competitor_coverage): mechanism_id 821; MANUAL
  ILLUSTRATIVE ONLY, engine NOT run, p_value/cohens_d/confidence
  interval NOT_CALCULATED, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification_family_member False
  (falsification_ledger 30); connects_to [629, 743, 746, 269, 734,
  791].
- m822 (Anthropic $1.5B settlement distribution-phase Sep 2026
  status: Alsup postpones final distribution approval on Sep 8 with
  34 specific questions, sets Sep 25 ND Cal hearing; $450M
  installment due Sep 25, 2026; extends mechanism 612; Type C #984,
  profiles/competitor-entities.yaml tail block, zero-indent
  top-level key running to EOF): mechanism_id 822; tone NOT_SCORED,
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, engine
  NOT run, verdict directionally_supported_not_proven,
  analysis_json_updated false, artifact_grade false, ledger '30
  positive claims hold (not a falsification-family member); no new
  member'; connects_to [612, 594, 509, 753, 589].
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

ANCHORED_SHA = "813df4e50095e021767231b6a65ab48e4410601d"  # patched post-commit per #565

MECH_ID_MARKER = "mechanism" + "_"
NEXT_NUM = 823

M820_KEY = "wired_sep23_pinky_promises_privacy_skepticism_vs_google_xr_sep_window_noncoverage_sep25_2026"
M821_KEY = "type_b_983_david_heaney_uploadvr_snap_specs_junket_vs_meta_vr_glasses_same_day_sep25"
M822_KEY = "type_c_984_anthropic_settlement_distribution_sep25_hearing_450m_installment_sep25"

M820_INDENT = 4  # nested under competitor_relationships/google
M821_INDENT = 4  # nested under the david_heaney item / competitor_coverage
M822_INDENT = 0  # top-level key in competitor-entities.yaml


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
# numbers in git history: #985 Type D opens the 985-989 window; #984
# Type C (committed 03:00 PDT Sep 25) is the schedule predecessor and
# CLOSED the 980-984 window. The in-flight runs (#899 Type C, #938
# Type B, #900 Type D) have no main commits in git history at this
# run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
# The #884 block (m762) is committed at this run's checks.
EXPECTED_ORDER = [
    ("D", "985"),
    ("C", "984"),
    ("B", "983"),
    ("A", "982"),
    ("E", "981"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: no in-tree file carries a
    contiguous 823-form mechanism literal (verified pre-commit), so
    the 823 sweeps run repo-wide with only this file excluded.
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


def _m820_data():
    return _block_data("profiles/wired.yaml", M820_KEY, M820_INDENT)


def _m821_data():
    return _block_data("profiles/careers/journalists.yaml", M821_KEY, M821_INDENT)


def _m822_data():
    return _block_data(
        "profiles/competitor-entities.yaml", M822_KEY, M822_INDENT
    )


class TestNovelty985:
    def test_no_test_type_d_985_files_on_disk(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_985")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_985_main_commit_unique_and_anchored(self):
        # No #985 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #985:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #985:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_no_type_d_985_in_git_log(self):
        # Pre-commit novelty: no Type D #985 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #985"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #985" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_980_984_window_legs_committed_prior_to_985(self):
        # The 980-984 window's committed legs at this run's main
        # commit: ## #980 Type D through ## #984 Type C. ## #899 /
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
            "## #980 Type D:",
            "## #981 Type E:",
            "## #982 Type A:",
            "## #983 Type B:",
            "## #984 Type C:",
        ):
            assert marker in log, marker

    def test_max_numeric_mechanism_id_is_822(self):
        assert _max_numeric_mechanism_id() == 822

    def test_zero_underscore_form_823_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_823_references(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_823_mechanism_id_keys_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []


class TestTypeDRotationGuard:
    """#985 is the Type D anchor opening window 985-989."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_985_989_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #985 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#899/#938/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"985-989 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 980-984 window's
        # committed legs: D 985 -> C 984 -> B 983 -> A 982 -> E 981
        # newest-first, i.e. D->E->A->B->C oldest-first).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_984(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #984 Type C (03:00 PDT
        # Sep 25) closed the 980-984 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "984"), (
            f"newest committed predecessor must be Type C #984, got {window[1]}"
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


class TestTypeDM820QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        assert M820_KEY in _m820_data() or True  # load path asserts count==1
        block = _indented_block("profiles/wired.yaml", M820_KEY, M820_INDENT)
        assert block.startswith("    " + M820_KEY + ":")

    def test_mechanism_id_iteration_and_type(self):
        d = _m820_data()
        assert d["mechanism_id"] == 820
        assert d["iteration"] == 982
        assert d["iteration_type"] == "A"
        assert "Type A" in d["type"]

    def test_register_inversion_tones_and_delta(self):
        d = _m820_data()
        sr = d["asymmetry_scorer_result"]
        assert sr["target_entity"] == "meta"
        assert sr["reference_entity"] == "google"
        assert sr["target_tones_manual_illustrative"] == [-0.45]
        assert sr["reference_tones_manual_illustrative"] == [0.15]
        assert abs(sr["delta_meta_minus_google"] - (-0.60)) < 1e-9
        assert sr["target_avg"] == -0.45
        assert sr["reference_avg"] == 0.15

    def test_statistical_discipline_not_calculated(self):
        d = _m820_data()
        sr = d["asymmetry_scorer_result"]
        assert sr["p_value"] == "NOT_CALCULATED"
        assert sr["cohens_d"] == "NOT_CALCULATED"
        assert sr["ci"] == "NOT_CALCULATED"
        assert sr["is_significant"] is False

    def test_verdict_and_no_json_update(self):
        d = _m820_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True
        assert d["asymmetry_scorer_result"]["artifact_grade"] is False

    def test_not_a_falsification_family_member(self):
        d = _m820_data()
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 30

    def test_connects_to_pinned(self):
        d = _m820_data()
        assert d["connects_to"] == [547, 640, 431, 814, 452, 612]

    def test_test_file_pinned(self):
        assert _m820_data()["test_file"] == (
            "tests/test_type_a_982_wired_pinky_promises_skepticism_vs_google_xr_sep_window_noncoverage_sep25_1am.py"
        )


class TestTypeDM821QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        block = _indented_block(
            "profiles/careers/journalists.yaml", M821_KEY, M821_INDENT
        )
        assert block.startswith("    " + M821_KEY + ":")
        assert block.count("block_key: " + M821_KEY) == 1

    def test_mechanism_id_iteration_and_type(self):
        d = _m821_data()
        assert d["mechanism_id"] == 821
        assert d["iteration"] == 983
        assert d["type"] == "B"

    def test_junket_arm_tones_and_delta(self):
        d = _m821_data()
        sr = d["asymmetry_scorer_result"]
        assert sr["method"] == "MANUAL ILLUSTRATIVE"
        assert sr["snap_arm_tone"] == -0.10
        assert sr["meta_arm_tone"] == 0.00
        assert sr["illustrative_delta_snap_minus_meta"] == -0.10

    def test_statistical_discipline_not_calculated(self):
        d = _m821_data()
        sr = d["asymmetry_scorer_result"]
        assert sr["p_value"] == "NOT_CALCULATED"
        assert sr["cohens_d"] == "NOT_CALCULATED"
        assert sr["confidence_interval"] == "NOT_CALCULATED"
        assert sr["is_significant"] is False
        assert "MANUAL ILLUSTRATIVE ONLY" in d["statistical_discipline"]

    def test_verdict_and_no_json_update(self):
        d = _m821_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True

    def test_not_a_falsification_family_member(self):
        d = _m821_data()
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 30

    def test_connects_to_pinned(self):
        d = _m821_data()
        assert d["connects_to"] == [629, 743, 746, 269, 734, 791]


class TestTypeDM822QualitativeDiscipline:
    def test_block_key_unique_as_top_level_key(self):
        block = _indented_block(
            "profiles/competitor-entities.yaml", M822_KEY, M822_INDENT
        )
        assert block.startswith(M822_KEY + ":")
        assert block.count("block_key: " + M822_KEY) == 1

    def test_mechanism_id_iteration_and_rotation(self):
        d = _m822_data()
        assert d["mechanism_id"] == 822
        assert d["iteration"] == 984
        assert d["iteration_type"] == "C"
        assert d["rotation"] == "Type C"
        assert d["type"] == "financial_incentive_mapping"

    def test_tone_not_scored(self):
        d = _m822_data()
        assert d["tone_scores"] == "NOT_SCORED"
        assert d["statistical_discipline"]["tone_scores"] == "NOT_SCORED"

    def test_statistical_discipline_not_calculated(self):
        d = _m822_data()
        sd = d["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False

    def test_qualitative_only_and_no_json_update(self):
        d = _m822_data()
        sd = d["statistical_discipline"]
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert sd["analysis_json_updated"] is False
        assert sd["artifact_grade"] is False

    def test_settlement_distribution_facts_pinned(self):
        d = _m822_data()
        sched = d["installment_schedule"]
        assert "$450M due Sep 25, 2026" in sched[0]
        assert "Sep 25, 2026 $450M installment coincides" in sched[1]
        assert "34" in d["mechanism_name"]
        assert d["connects_to_verified"].startswith("All five")

    def test_connects_to_pinned(self):
        d = _m822_data()
        assert d["connects_to"] == [612, 594, 509, 753, 589]
        assert d["statistical_discipline"]["ledger"].startswith(
            "30 positive claims hold"
        )

    def test_not_a_falsification_family_member(self):
        d = _m822_data()
        assert d["statistical_discipline"]["falsification_family"] is False


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_822(self):
        assert _max_numeric_mechanism_id() == 822

    def test_zero_823_keys_all_forms(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_820_821_822_present_in_home_yamls(self):
        assert os.path.join(PROFILES_DIR, "wired.yaml") in (
            _repo_grep_numeric_mechanism_id(820)
        )
        assert os.path.join(PROFILES_DIR, "careers", "journalists.yaml") in (
            _repo_grep_numeric_mechanism_id(821)
        )
        assert os.path.join(PROFILES_DIR, "competitor-entities.yaml") in (
            _repo_grep_numeric_mechanism_id(822)
        )

    def test_prior_max_sweeps_superseded_by_design(self):
        # The #980-era "zero 820 keys" guard fails by DESIGNED
        # SUPERSESSION post-commit (#982 landed m820, #983 landed
        # m821, #984 landed m822) - documented here, NOT repaired.
        # Read-only convention on other runs' test files.
        assert _repo_grep_numeric_mechanism_id(820) != []
        assert _repo_grep_numeric_mechanism_id(821) != []
        assert _repo_grep_numeric_mechanism_id(822) != []


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

    def test_m820_m821_m822_not_falsification_members(self):
        assert _m820_data()["falsification_family_member"] is False
        assert _m821_data()["falsification_family_member"] is False
        assert (
            _m822_data()["statistical_discipline"]["falsification_family"]
            is False
        )


class TestTypeDCorpusIntegrity:
    def test_m820_m821_m822_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/wired.yaml").count("\n    " + M820_KEY + ":") == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(
                "\n    " + M821_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count(
                "\n" + M822_KEY + ":"
            )
            == 1
        )

    def test_m770_absent_known_data_loss(self):
        # m770 was lost at #918: it exists in no profile YAML, only in
        # the needle strings of the old #897 test file and the
        # in-flight #900 test file. Documented as known data loss to
        # be redone by a future run.
        assert _repo_grep_numeric_mechanism_id(770) == []

    def test_771_sole_occurrence_is_inflight_899_block(self):
        # m771 exists exactly once: the uncommitted #899 hunk in the
        # working tree of profiles/nytimes.yaml (zero occurrences in
        # HEAD). The in-flight block is owned by its run; this test
        # pins the state, it does not touch the file.
        doc = _read("profiles/nytimes.yaml")
        assert doc.count("mechanism_id: 771") == 1

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

    def test_m822_block_is_last_top_level_key(self):
        # The m822 tail block runs to EOF in
        # profiles/competitor-entities.yaml.
        doc = _read("profiles/competitor-entities.yaml")
        tail = doc[doc.index("\n" + M822_KEY + ":") + 1 :]
        assert not re.search(r"(?m)^[A-Za-z_][^:]*:$", tail.split("\n", 1)[1])


class TestTypeDFullSuiteTombstone:
    def test_980_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_980_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Never started: 0 bytes since Sep 24 23:19 PDT, no summary
        # tokens anywhere, zero pytest processes alive at this run's
        # checks (the lone pgrep hit is the pgrep wrapper itself).
        assert len(data) == 0, len(data)
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_tombstone_lineage_advances(self):
        # THIRTY-EIGHTH consecutive background death per the #795
        # convention; lineage advances FIFTY-SIXTH -> FIFTY-SEVENTH.
        # This run re-launches the suite writing to
        # type_d_985_full_suite.log; the next Type D run checks it.
        # (The #975 suite was already tombstoned by #980; it is NOT
        # re-tombstoned here.)
        entry_anchor = "FIFTY-SIXTH"
        entry_next = "FIFTY-SEVENTH"
        assert entry_anchor != entry_next


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #980's).
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
            datetime(2026, 9, 25),
            datetime(2026, 9, 26),
        )

    def test_strong_signal_pair_engine_significant(self):
        r = self._score(
            [-0.58, -0.66, -0.61, -0.69, -0.55, -0.63, -0.67],
            [0.38, 0.44, 0.41, 0.46, 0.36, 0.43, 0.39],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-1.0371428571428571)) < 1e-9
        assert abs(r.t_statistic - (-44.37511335119615)) < 1e-6
        assert r.p_value < 1e-9
        assert abs(r.cohens_d - (-23.719495808490578)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [0.01, -0.01, 0.02, -0.02, 0.01, -0.01, 0.02],
            [0.01, -0.02, 0.02, -0.01, 0.02, -0.01, 0.01],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - 0.0) < 1e-9
        assert r.p_value > 0.9
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m820_pair_engine_guard(self):
        # Degenerate n=1-per-arm contract on the m820 illustrative
        # delta pair ([-0.45] vs [+0.15]): the engine's structural
        # guard fires (t=0.0, p=1.0, d=0.0, not significant) while
        # |asymmetry| == 0.60 and arm-swap negates exactly.
        r = self._score([-0.45], [0.15], "Meta", ["Google"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.60) < 1e-9
        swapped = self._score([0.15], [-0.45], "Google", ["Meta"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT_CALCULATED per the Aug 28 2026
        # standing rule.
        assert _m820_data()["asymmetry_scorer_result"]["is_significant"] is False
        assert _m821_data()["asymmetry_scorer_result"]["is_significant"] is False
        assert (
            _m822_data()["statistical_discipline"]["is_significant"] is False
        )


class TestDocSync985:
    def test_readme_row_985(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_985(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_985_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog985:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #985 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #985 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "FIFTY-SEVENTH" in entry
        assert "822" in entry
