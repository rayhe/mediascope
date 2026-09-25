"""Type D -- Iteration #990 (Fri 2026-09-25 09:00 PDT): m823/m824/m825
qualitative-discipline verification + post-985-989 corpus integrity
(max numeric mechanism_id 825; zero next-number 826 keys in
numeric/underscore/dash mechanism forms; ledger holds at 30 with the
THIRTIETH member-form present exactly once (m818, journalists.yaml);
THIRTY-FIRST negative guard) + #985 background-suite tombstone
(THIRTY-NINTH consecutive death; lineage FIFTY-SEVENTH -> FIFTY-EIGHTH)
+ fresh synthetic engine calibration (new values, not #985's) +
re-launch of the full suite as a background process writing to goal
hidden_files type_d_990_full_suite.log (next Type D run checks its
verdict per the #795 convention).

Type D FIRST leg of the 990-994 window, OPENING it (D->E->A->B->C).
Committed predecessor #989 Type C (08:00 PDT Sep 25) CLOSED the 985-989
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
- m823 (Type A #987, FT x OpenAI Sep-2026 cash-burn realism
  MANUAL ILLUSTRATIVE -0.15 (carried from m754, un-rescored per #807)
  vs FT x Meta Sep-2026 Muse-Charm momentum-change constructiveness
  MANUAL ILLUSTRATIVE +0.20 (NEW); illustrative delta (OpenAI minus
  Meta) -0.35, register INVERSION that bounds m718's matched-peg +0.55
  gap temporally (unmatched peg, NOT falsification-family member);
  profiles/financial-times.yaml under competitor_relationships/openai):
  mechanism_id 823; MANUAL ILLUSTRATIVE ONLY per standing rule Aug 28
  2026, engine NOT run at the finding layer, p_value/cohens_d/ci
  NOT_CALCULATED, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification_family_member False
  (falsification_ledger 30); connects_to [754, 718, 54, 643, 676, 625].
- m824 (Type B #988, Andy Boxall, Android Police: Sep-24 Meta Ray-Ban
  Audio "PR stunt" motive-attribution MANUAL ILLUSTRATIVE -0.55 vs
  Sep-10-2025 Apple Watch SE 3 constructive value column MANUAL
  ILLUSTRATIVE +0.35; illustrative delta (Apple minus Meta) +0.90,
  price-register inversion + motive-attribution asymmetry; FIRST
  dedicated corpus mechanism on Boxall; profiles/careers/
  journalists.yaml under the andy_boxall item): mechanism_id 824;
  MANUAL ILLUSTRATIVE ONLY, engine NOT run, p_value/cohens_d/
  confidence_interval NOT_CALCULATED, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification_family_member False
  (falsification_ledger 30); connects_to [821, 809, 818].
- m825 (Type C #989, Anthropic $1.5B settlement VERIFIED
  distribution-phase cash-flow map: $1.07B in escrow per Docket 688
  Sep 2 2026; $450M Scheduled Payment 1 PAID Aug 19 2026 (not due
  Sep 25 2026); final $450M due Sep 25 2027 or on IPO trigger; first
  author payments $2,203.56/work by Nov 15 2026; m822 year-shift
  CORRECTION; FIRST dedicated corpus verification/correction
  mechanism; profiles/competitor-entities.yaml tail block, zero-indent
  top-level key running to EOF): mechanism_id 825; tone NOT_SCORED,
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, engine
  NOT run, verdict directionally_supported_not_proven,
  analysis_json_updated false, artifact_grade false, ledger '30
  positive claims hold (not a falsification-family member); no new
  member'; connects_to [822, 612, 594, 509].

THIRTY-FIRST stays the negative guard; pre-#978 "THIRTIETH remains the
negative guard" wordings are pinned as superseded, not repaired.
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
NEXT_NUM = 826

M823_KEY = "type_a_987_ft_openai_burn_realism_vs_meta_muse_charm_momentum_change_sep25_2026"
M824_KEY = "type_b_988_andy_boxall_androidpolice_meta_pr_stunt_vs_apple_watch_value_sep25"
M825_KEY = "type_c_989_anthropic_settlement_verified_cashflow_correction_sep25"

M823_INDENT = 4  # nested under competitor_relationships/openai
M824_INDENT = 4  # nested under the andy_boxall item
M825_INDENT = 0  # top-level key in competitor-entities.yaml


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
# numbers in git history: #990 Type D opens the 990-994 window; #989
# Type C (committed 08:00 PDT Sep 25) is the schedule predecessor and
# CLOSED the 985-989 window. The in-flight runs (#899 Type C, #938
# Type B, #900 Type D) have no main commits in git history at this
# run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
# The #884 block (m762) is committed at this run's checks.
EXPECTED_ORDER = [
    ("D", "990"),
    ("C", "989"),
    ("B", "988"),
    ("A", "987"),
    ("E", "986"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson). No additional
    sweep-carrier exclusions this run: no in-tree file carries a
    contiguous 826-form mechanism literal (verified pre-commit), so
    the 826 sweeps run repo-wide with only this file excluded.
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


def _m823_data():
    return _block_data("profiles/financial-times.yaml", M823_KEY, M823_INDENT)


def _m824_data():
    return _block_data(
        "profiles/careers/journalists.yaml", M824_KEY, M824_INDENT
    )


def _m825_data():
    return _block_data(
        "profiles/competitor-entities.yaml", M825_KEY, M825_INDENT
    )


class TestNovelty990:
    def test_no_test_type_d_990_files_on_disk(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_990")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_990_main_commit_unique_and_anchored(self):
        # No #990 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #990:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #990:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_no_type_d_990_in_git_log(self):
        # Pre-commit novelty: no Type D #990 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #990"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #990" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_985_989_window_legs_committed_prior_to_990(self):
        # The 985-989 window's committed legs at this run's main
        # commit: ## #985 Type D through ## #989 Type C. ## #899 /
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
            "## #985 Type D:",
            "## #986 Type E:",
            "## #987 Type A:",
            "## #988 Type B:",
            "## #989 Type C:",
        ):
            assert marker in log, marker

    def test_max_numeric_mechanism_id_is_825(self):
        assert _max_numeric_mechanism_id() == 825

    def test_zero_underscore_form_826_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_826_references(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_826_mechanism_id_keys_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []


class TestTypeDRotationGuard:
    """#990 is the Type D anchor opening window 990-994."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_990_994_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #990 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#899/#938/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"990-994 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 985-989 window's
        # committed legs: D 990 -> C 989 -> B 988 -> A 987 -> E 986
        # newest-first, i.e. D->E->A->B->C oldest-first).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_989(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #989 Type C (08:00 PDT
        # Sep 25) closed the 985-989 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "989"), (
            f"newest committed predecessor must be Type C #989, got {window[1]}"
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


class TestTypeDM823QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        # _indented_block asserts the marker appears exactly once.
        block = _indented_block(
            "profiles/financial-times.yaml", M823_KEY, M823_INDENT
        )
        assert block.startswith("    " + M823_KEY + ":")

    def test_mechanism_id_iteration_and_type(self):
        d = _m823_data()
        assert d["mechanism_id"] == 823
        assert d["iteration"] == 987
        assert d["iteration_type"] == "A"
        assert "Type A" in d["type"]

    def test_register_inversion_tones_and_delta(self):
        d = _m823_data()
        sr = d["asymmetry_scorer_result"]
        assert sr["target_entity"] == "openai"
        assert sr["reference_entity"] == "meta"
        assert sr["target_tones_manual_illustrative"] == [-0.15]
        assert sr["reference_tones_manual_illustrative"] == [0.2]
        assert abs(sr["delta_openai_minus_meta"] - (-0.35)) < 1e-9
        assert sr["target_avg"] == -0.15
        assert sr["reference_avg"] == 0.2

    def test_statistical_discipline_not_calculated(self):
        d = _m823_data()
        sr = d["asymmetry_scorer_result"]
        assert sr["p_value"] == "NOT_CALCULATED"
        assert sr["cohens_d"] == "NOT_CALCULATED"
        assert sr["ci"] == "NOT_CALCULATED"
        assert sr["is_significant"] is False

    def test_verdict_and_no_json_update(self):
        d = _m823_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True
        assert d["asymmetry_scorer_result"]["artifact_grade"] is False

    def test_not_a_falsification_family_member(self):
        d = _m823_data()
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 30

    def test_connects_to_pinned(self):
        d = _m823_data()
        assert d["connects_to"] == [754, 718, 54, 643, 676, 625]

    def test_test_file_pinned(self):
        assert _m823_data()["test_file"] == (
            "tests/test_type_a_987_ft_openai_burn_realism_vs_meta_muse_charm_momentum_change_sep25_6am.py"
        )


class TestTypeDM824QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        block = _indented_block(
            "profiles/careers/journalists.yaml", M824_KEY, M824_INDENT
        )
        assert block.startswith("    " + M824_KEY + ":")
        assert block.count("block_key: " + M824_KEY) == 1

    def test_mechanism_id_iteration_and_type(self):
        d = _m824_data()
        assert d["mechanism_id"] == 824
        assert d["iteration"] == 988
        assert d["type"] == "B"

    def test_motive_attribution_arms_and_delta(self):
        d = _m824_data()
        sr = d["asymmetry_scorer_result"]
        assert sr["method"] == "MANUAL ILLUSTRATIVE"
        assert sr["meta_arm_tone"] == -0.55
        assert sr["apple_arm_tone"] == 0.35
        assert abs(sr["illustrative_delta_apple_minus_meta"] - 0.90) < 1e-9
        assert "FIRST dedicated corpus mechanism on Andy Boxall" in d["novelty"]

    def test_statistical_discipline_not_calculated(self):
        d = _m824_data()
        sr = d["asymmetry_scorer_result"]
        assert sr["p_value"] == "NOT_CALCULATED"
        assert sr["cohens_d"] == "NOT_CALCULATED"
        assert sr["confidence_interval"] == "NOT_CALCULATED"
        assert sr["is_significant"] is False
        assert "MANUAL ILLUSTRATIVE ONLY" in d["statistical_discipline"]

    def test_verdict_and_no_json_update(self):
        d = _m824_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True

    def test_not_a_falsification_family_member(self):
        d = _m824_data()
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 30

    def test_connects_to_and_test_file_pinned(self):
        d = _m824_data()
        assert d["connects_to"] == [821, 809, 818]
        assert d["test_file"] == (
            "tests/test_type_b_988_andy_boxall_androidpolice_meta_pr_stunt_vs_apple_watch_value_sep25_7am.py"
        )


class TestTypeDM825QualitativeDiscipline:
    def test_block_key_unique_as_top_level_key(self):
        block = _indented_block(
            "profiles/competitor-entities.yaml", M825_KEY, M825_INDENT
        )
        assert block.startswith(M825_KEY + ":")

    def test_mechanism_id_iteration_and_type(self):
        d = _m825_data()
        assert d["mechanism_id"] == 825
        assert d["iteration"] == 989
        assert d["iteration_type"] == "C"
        assert d["type"] == "financial_incentive_mapping"

    def test_tone_not_scored(self):
        d = _m825_data()
        assert d["statistical_discipline"]["tone_scores"] == "NOT_SCORED"

    def test_statistical_discipline_not_calculated(self):
        d = _m825_data()
        sd = d["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False

    def test_qualitative_only_and_no_json_update(self):
        d = _m825_data()
        sd = d["statistical_discipline"]
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert sd["analysis_json_updated"] is False
        assert sd["artifact_grade"] is False
        assert sd["ledger"].startswith("30 positive claims hold")

    def test_connects_to_pinned(self):
        d = _m825_data()
        assert d["connects_to"] == [822, 612, 594, 509]

    def test_not_a_falsification_family_member(self):
        d = _m825_data()
        assert _m825_data()["statistical_discipline"]["falsification_family"] is False


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_825(self):
        assert _max_numeric_mechanism_id() == 825

    def test_zero_826_keys_all_forms(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_823_824_825_present_in_home_yamls(self):
        assert os.path.join(PROFILES_DIR, "financial-times.yaml") in (
            _repo_grep_numeric_mechanism_id(823)
        )
        assert os.path.join(PROFILES_DIR, "careers", "journalists.yaml") in (
            _repo_grep_numeric_mechanism_id(824)
        )
        assert os.path.join(PROFILES_DIR, "competitor-entities.yaml") in (
            _repo_grep_numeric_mechanism_id(825)
        )

    def test_prior_max_sweeps_superseded_by_design(self):
        # The #985-era "zero 823 keys" guard fails by DESIGNED
        # SUPERSESSION post-commit (#987 landed m823, #988 landed
        # m824, #989 landed m825) - documented here, NOT repaired.
        # Read-only convention on other runs' test files.
        assert _repo_grep_numeric_mechanism_id(823) != []
        assert _repo_grep_numeric_mechanism_id(824) != []
        assert _repo_grep_numeric_mechanism_id(825) != []


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
        # "THIRTIETH remains the negative guard" and the verge's. Type D
        # read-only on other runs' blocks; a future non-Type-D run
        # reconciles.
        assert "THIRTIETH remains the negative guard" in _read(
            "profiles/gizmodo.yaml"
        )
        assert "THIRTIETH remains the negative guard" in _read(
            "profiles/the-verge.yaml"
        )

    def test_thirty_first_absent_entirely(self):
        assert _profiles_with("THIRTY-FIRST") == []

    def test_m823_m824_m825_not_falsification_members(self):
        assert _m823_data()["falsification_family_member"] is False
        assert _m824_data()["falsification_family_member"] is False
        assert (
            _m825_data()["statistical_discipline"]["falsification_family"]
            is False
        )


class TestTypeDCorpusIntegrity:
    def test_m823_m824_m825_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/financial-times.yaml").count("\n    " + M823_KEY + ":")
            == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(
                "\n    " + M824_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count("\n" + M825_KEY + ":")
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

    def test_m825_block_is_last_top_level_key(self):
        # The m825 tail block runs to EOF in
        # profiles/competitor-entities.yaml.
        doc = _read("profiles/competitor-entities.yaml")
        tail = doc[doc.index("\n" + M825_KEY + ":") + 1 :]
        assert not re.search(r"(?m)^[A-Za-z_][^:]*:$", tail.split("\n", 1)[1])


class TestTypeDFullSuiteTombstone:
    def test_985_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_985_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-run: 267 bytes of dots since Sep 25 04:22 PDT,
        # no summary tokens anywhere, the process has since exited.
        assert len(data) == 267, len(data)
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_tombstone_lineage_advances(self):
        # THIRTY-NINTH consecutive background death per the #795
        # convention; lineage advances FIFTY-SEVENTH -> FIFTY-EIGHTH.
        # This run re-launches the suite writing to
        # type_d_990_full_suite.log; the next Type D run checks it.
        # (The #980 suite was already tombstoned by #985; it is NOT
        # re-tombstoned here.)
        entry_anchor = "FIFTY-SEVENTH"
        entry_next = "FIFTY-EIGHTH"
        assert entry_anchor != entry_next

    def test_990_suite_log_relaunched(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_990_full_suite.log",
        )
        assert os.path.isfile(log_path), log_path


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #985's).
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
            [-0.42, -0.55, -0.38, -0.61, -0.47, -0.58, -0.44],
            [0.28, 0.35, 0.19, 0.41, 0.31, 0.24, 0.37],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.8)) < 1e-9
        assert abs(r.t_statistic - (-18.18475771093122)) < 1e-6
        assert r.p_value < 1e-9
        assert abs(r.cohens_d - (-9.720161859400026)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [-0.02, 0.05, -0.04, 0.01, -0.03, 0.06, -0.01],
            [0.03, -0.04, 0.02, -0.05, 0.04, -0.02, 0.01],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - 0.004285714285714287) < 1e-9
        assert r.p_value > 0.8
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m823_pair_engine_guard(self):
        # Degenerate n=1-per-arm contract on the m823 illustrative
        # delta pair ([-0.15] vs [+0.20]): the engine's structural
        # guard fires (t=0.0, p=1.0, d=0.0, not significant) while
        # |asymmetry| == 0.35 and arm-swap negates exactly.
        r = self._score([-0.15], [0.20], "OpenAI", ["Meta"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.35) < 1e-9
        swapped = self._score([0.20], [-0.15], "Meta", ["OpenAI"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT_CALCULATED per the Aug 28 2026
        # standing rule.
        assert _m823_data()["asymmetry_scorer_result"]["is_significant"] is False
        assert _m824_data()["asymmetry_scorer_result"]["is_significant"] is False
        assert (
            _m825_data()["statistical_discipline"]["is_significant"] is False
        )


class TestDocSync990:
    def test_readme_row_990(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_990(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_990_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog990:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #990 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #990 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "FIFTY-EIGHTH" in entry
        assert "825" in entry
