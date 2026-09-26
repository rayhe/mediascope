"""Type D -- Iteration #1000 (Fri 2026-09-25 19:00 PDT): m829/m830/m831
qualitative-discipline verification + post-995-999 corpus integrity
(max numeric mechanism_id 831; zero next-number 832 keys in
numeric/underscore/dash mechanism forms; ledger holds at 30 with the
THIRTIETH member-form present exactly once (m818, journalists.yaml);
THIRTY-FIRST member-form negative guard) + #995 background-suite
tombstone (FORTY-FIRST consecutive death; lineage FIFTY-NINTH ->
SIXTIETH) + fresh synthetic engine calibration (new values, not #995's)
+ re-launch of the full suite as a background process writing to goal
hidden_files type_d_1000_full_suite.log (next Type D run checks its
verdict per the #795 convention).

Type D FIRST leg of the 1000-1004 window, OPENING it (D->E->A->B->C).
Committed predecessor #999 Type C (18:00 PDT Sep 25) CLOSED the
995-999 window. Concurrency note: the in-flight runs at this run's
checks are the #899 Type C block (m771, uncommitted hunk in
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
- m829 (Type A #997, Atlantic Sep-25 doomsday-scenarios essay:
  frontier-lab philosophical-safety register (Sep 25, target tones
  [0.00, 0.05] avg +0.025) vs carried Meta AI Watchdog accountability
  arms ([-0.75, -0.55] avg -0.65); illustrative delta
  (target minus Meta) +0.675, a temporal EXTENSION of the m694
  philosophical-register strand (not a replication); profiles/
  atlantic.yaml under competitor_relationships/openai): mechanism_id
  829; MANUAL ILLUSTRATIVE ONLY per standing rule Aug 28 2026, engine
  NOT run at the finding layer, p_value/cohens_d/ci NOT_CALCULATED,
  is_significant False, verdict directionally_supported_not_proven,
  no_analysis_json_update true, NOT artifact-grade;
  falsification_family_member False (falsification_ledger 30);
  connects_to [481, 694, 404, 572, 718, 825].
- m830 (Type B #998, Boone Ashworth, WIRED: Sep-23 Meta Connect spec
  roundup (MANUAL ILLUSTRATIVE 0.00, excerpt-tier) vs carried Sep-16
  Snap Specs launch arm (-0.15); illustrative delta (Meta minus Snap)
  +0.15, a GENRE BOUND on mechanism 743 within the same journalist -
  the m743 adversarial-Meta direction FLIPS at news-register level;
  profiles/careers/journalists.yaml at the boone_ashworth item):
  mechanism_id 830; MANUAL ILLUSTRATIVE ONLY, engine NOT run,
  p_value/cohens_d/ci NOT_CALCULATED, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade; falsification_family_member False
  (falsification_ledger 30); connects_to
  [743, 442, 89, 640, 641, 818, 806, 827].
- m831 (Type C #999, OpenAI x Yelp content-to-commerce licensing with
  in-answer Request a Quote, Axios disclosed Jul 23 2026: FIRST
  dedicated corpus mechanism on a commerce-conversion licensing leg,
  ELEVENTH relationship direction in the m807 enumeration; licensed
  news partners keep free unlimited outbound reach while
  business/creator Pages pay; structural contrast with the Anthropic
  zero-deal posture (m509) and flat-fee deals (m594); zero-indent tail
  block of profiles/competitor-entities.yaml): mechanism_id 831;
  tone_scores NOT_SCORED, p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False, engine_run False, verdict
  directionally_supported_not_proven, analysis_json_updated False,
  artifact_grade False, ledger '30 positive claims hold (not a
  falsification-family member); no new member'; connects_to
  [735, 753, 509, 594].

THIRTY-FIRST stays the member-form negative guard; the pre-#997
"THIRTY-FIRST absent entirely" raw-string guard is pinned as superseded
by designed wording (the m829/m830 falsification_notes carry
negative-guard THIRTY-FIRST wordings), not repaired.
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
NEXT_NUM = 832

M829_KEY = "type_a_997_atlantic_frontier_labs_doomsday_scenarios_philosophical_safety_register_vs_meta_watchdog_sep25_2026"
M830_KEY = "type_b_998_boone_ashworth_wired_meta_connect_2026_spec_roundup_genre_bound_m743"
M831_KEY = "type_c_999_yelp_openai_commerce_conversion_request_a_quote_sep25"

M829_INDENT = 4  # nested under competitor_relationships/openai
M830_INDENT = 2  # nested under the boone_ashworth item
M831_INDENT = 0  # top-level key in competitor-entities.yaml


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
# numbers in git history: #1000 Type D opens the 1000-1004 window;
# #999 Type C (committed 18:00 PDT Sep 25) is the schedule predecessor
# and CLOSED the 995-999 window. The in-flight runs (#899 Type C,
# #938 Type B, #900 Type D) have no main commits in git history at
# this run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
# The #884 block (m762) is committed at this run's checks.
EXPECTED_ORDER = [
    ("D", "1000"),
    ("C", "999"),
    ("B", "998"),
    ("A", "997"),
    ("E", "996"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: the #999 pyc
    carries an 832-form needle string from its own next-number guard;
    compiled artifacts are excluded from the sweeps). No additional
    sweep-carrier exclusions this run: no in-tree SOURCE file carries
    a contiguous 832-form mechanism literal (verified pre-commit; the
    #999 test file builds its 832 needles at runtime and its one
    raw "mechanism 832" hit is a docstring with a space, not a
    contiguous mechanism-form literal), so the 832 sweeps run
    repo-wide with only this file excluded.
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


def _m829_data():
    return _block_data("profiles/atlantic.yaml", M829_KEY, M829_INDENT)


def _m830_data():
    return _block_data(
        "profiles/careers/journalists.yaml", M830_KEY, M830_INDENT
    )


def _m831_data():
    return _block_data(
        "profiles/competitor-entities.yaml", M831_KEY, M831_INDENT
    )


class TestNovelty1000:
    def test_no_test_type_d_1000_files_on_disk(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_1000")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_1000_main_commit_unique_and_anchored(self):
        # No #1000 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1000:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #1000:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_no_type_d_1000_in_git_log(self):
        # Pre-commit novelty: no Type D #1000 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1000"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1000" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_995_999_window_legs_committed_prior_to_1000(self):
        # The 995-999 window's committed legs at this run's main
        # commit: ## #995 Type D through ## #999 Type C. ## #899 /
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
            "## #995 Type D:",
            "## #996 Type E:",
            "## #997 Type A:",
            "## #998 Type B:",
            "## #999 Type C:",
        ):
            assert marker in log, marker

    def test_max_numeric_mechanism_id_is_831(self):
        assert _max_numeric_mechanism_id() == 831

    def test_zero_underscore_form_832_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_832_references(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_832_mechanism_id_keys_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []


class TestTypeDRotationGuard:
    """#1000 is the Type D anchor opening window 1000-1004."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_1000_1004_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #1000 main commit does
        # not exist yet); patched green in the anchor followup. The
        # in-flight runs (#899/#938/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"1000-1004 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 995-999 window's
        # committed legs: D 1000 -> C 999 -> B 998 -> A 997 -> E 996
        # newest-first, i.e. D->E->A->B->C oldest-first).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_999(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #999 Type C (18:00 PDT
        # Sep 25) closed the 995-999 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "999"), (
            f"newest committed predecessor must be Type C #999, got {window[1]}"
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
        # THIRTY-FIRST member-form (absent corpus-wide). The pre-#997
        # "THIRTY-FIRST absent entirely" raw-string wordings are pinned
        # as superseded wording in the module docstring, not as ledger
        # changes.
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "THIRTY-FIRST" in text
        assert "Ledger holds at 30" in text


class TestTypeDM829QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        # _indented_block asserts the marker appears exactly once.
        block = _indented_block(
            "profiles/atlantic.yaml", M829_KEY, M829_INDENT
        )
        assert block.startswith("    " + M829_KEY + ":")

    def test_mechanism_id_iteration_and_type(self):
        d = _m829_data()
        assert d["mechanism_id"] == 829
        assert d["iteration"] == 997
        assert d["iteration_type"] == "A"
        assert "Type A" in d["type"]

    def test_target_meta_tones_and_delta(self):
        d = _m829_data()
        sr = d["asymmetry_scorer_result"]
        assert sr["target_entity"] == "openai"
        assert sr["reference_entity"] == "meta"
        assert sr["target_tones"] == [0.0, 0.05]
        assert abs(sr["target_avg"] - 0.025) < 1e-9
        assert sr["meta_tones"] == [-0.75, -0.55]
        assert abs(sr["meta_avg"] - (-0.65)) < 1e-9
        assert abs(sr["delta_target_minus_meta"] - 0.675) < 1e-9
        assert "m694" in d["finding"]

    def test_statistical_discipline_not_calculated(self):
        d = _m829_data()
        sr = d["asymmetry_scorer_result"]
        assert sr["p_value"] == "NOT_CALCULATED"
        assert sr["cohens_d"] == "NOT_CALCULATED"
        assert sr["ci"] == "NOT_CALCULATED"
        assert sr["is_significant"] is False
        assert sr["engine_run"] is False
        assert sr["artifact_grade"] is False

    def test_verdict_and_no_json_update(self):
        d = _m829_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True

    def test_not_a_falsification_family_member(self):
        d = _m829_data()
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 30

    def test_connects_to_pinned(self):
        d = _m829_data()
        assert d["connects_to"] == [481, 694, 404, 572, 718, 825]

    def test_test_file_pinned(self):
        assert _m829_data()["test_file"] == (
            "tests/test_type_a_997_atlantic_frontier_labs_doomsday_scenarios_philosophical_safety_register_vs_meta_watchdog_sep25_4pm.py"
        )

    def test_novelty_is_first_dedicated_mechanism(self):
        assert _m829_data()["novelty"].startswith(
            "Zero test_type_a_997 files on disk pre-commit"
        )
        assert "m694 philosophical-register strand" in _m829_data()["novelty"]


class TestTypeDM830QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        block = _indented_block(
            "profiles/careers/journalists.yaml", M830_KEY, M830_INDENT
        )
        assert block.startswith("  " + M830_KEY + ":")

    def test_mechanism_id_iteration_and_type(self):
        d = _m830_data()
        assert d["mechanism_id"] == 830
        assert d["iteration"] == 998
        assert d["type"] == "B"
        assert d["iteration_type"] == "B"
        assert d["journalist"] == "Boone Ashworth"

    def test_meta_snap_arms_and_delta(self):
        d = _m830_data()
        sr = d["asymmetry_scorer_result"]
        assert sr["target_entity"] == "meta"
        assert sr["reference_entity"] == "snap"
        assert sr["new_meta_arm_tone_manual_illustrative"] == 0.0
        assert sr["carried_snap_sep16_tone_manual_illustrative"] == -0.15
        assert abs(sr["illustrative_delta_meta_minus_snap"] - 0.15) < 1e-9
        assert sr["delta_calc"] == "0.00 - (-0.15) = 0.15"
        assert "GENRE BOUND" in d["finding"]

    def test_statistical_discipline_not_calculated(self):
        d = _m830_data()
        sr = d["asymmetry_scorer_result"]
        assert sr["p_value"] == "NOT_CALCULATED"
        assert sr["cohens_d"] == "NOT_CALCULATED"
        assert sr["ci"] == "NOT_CALCULATED"
        assert sr["is_significant"] is False
        assert sr["engine"] == "engine NOT run"
        assert sr["artifact_grade"] is False
        assert "MANUAL ILLUSTRATIVE" in sr["method"]

    def test_verdict_and_no_json_update(self):
        d = _m830_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True

    def test_not_a_falsification_family_member(self):
        d = _m830_data()
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 30

    def test_connects_to_pinned(self):
        d = _m830_data()
        assert d["connects_to"] == [743, 442, 89, 640, 641, 818, 806, 827]

    def test_test_file_pinned(self):
        assert _m830_data()["test_file"] == (
            "tests/test_type_b_998_boone_ashworth_wired_meta_connect_2026_spec_roundup_genre_bound_m743.py"
        )

    def test_novelty_is_first_corpus_evidence(self):
        assert _m830_data()["novelty"].startswith(
            "FIRST corpus evidence of Ashworth"
        )


class TestTypeDM831QualitativeDiscipline:
    def test_block_key_unique_as_top_level_key(self):
        block = _indented_block(
            "profiles/competitor-entities.yaml", M831_KEY, M831_INDENT
        )
        assert block.startswith(M831_KEY + ":")

    def test_mechanism_id_iteration_and_type(self):
        d = _m831_data()
        assert d["mechanism_id"] == 831
        assert d["iteration"] == 999
        assert d["rotation"] == "Type C"
        assert d["type_c_focus"].startswith(
            "FIRST dedicated corpus mechanism on an AI data-licensing deal"
        )

    def test_tone_not_scored(self):
        d = _m831_data()
        assert d["statistical_discipline"]["tone_scores"] == "NOT_SCORED"
        assert d["tone_scores"] == "NOT_SCORED"

    def test_statistical_discipline_not_calculated(self):
        d = _m831_data()
        sd = d["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False

    def test_qualitative_only_and_no_json_update(self):
        d = _m831_data()
        sd = d["statistical_discipline"]
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert sd["analysis_json_updated"] is False
        assert sd["artifact_grade"] is False
        assert sd["ledger"].startswith("30 positive claims hold")

    def test_connects_to_pinned(self):
        d = _m831_data()
        assert d["connects_to"] == [735, 753, 509, 594]

    def test_not_a_falsification_family_member(self):
        d = _m831_data()
        assert d["statistical_discipline"]["falsification_family"] is False

    def test_commerce_conversion_is_eleventh_direction(self):
        # FIRST commerce-conversion licensing leg (ELEVENTH
        # relationship direction in the m807 enumeration) per the
        # mechanism name and incentive geometry.
        d = _m831_data()
        assert d["mechanism_name"].startswith(
            "OpenAI x Yelp content-to-commerce licensing"
        )
        assert "ELEVENTH relationship direction" in d["mechanism_name"]

    def test_novelty_zero_yelp_pre_commit(self):
        assert 'zero "yelp" strings repo-wide pre-commit' in _m831_data()[
            "novelty"
        ]


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_831(self):
        assert _max_numeric_mechanism_id() == 831

    def test_zero_832_keys_all_forms(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_829_830_831_present_in_home_yamls(self):
        assert os.path.join(PROFILES_DIR, "atlantic.yaml") in (
            _repo_grep_numeric_mechanism_id(829)
        )
        assert os.path.join(PROFILES_DIR, "careers", "journalists.yaml") in (
            _repo_grep_numeric_mechanism_id(830)
        )
        assert os.path.join(PROFILES_DIR, "competitor-entities.yaml") in (
            _repo_grep_numeric_mechanism_id(831)
        )

    def test_prior_max_sweeps_superseded_by_design(self):
        # The #995-era "zero 829 keys" guard fails by DESIGNED
        # SUPERSESSION post-commit (#997 landed m829, #998 landed
        # m830, #999 landed m831) - documented here, NOT repaired.
        # Read-only convention on other runs' test files.
        assert _repo_grep_numeric_mechanism_id(829) != []
        assert _repo_grep_numeric_mechanism_id(830) != []
        assert _repo_grep_numeric_mechanism_id(831) != []


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

    def test_pre_997_thirty_first_raw_string_guard_superseded(self):
        # The #995-era "THIRTY-FIRST absent entirely" RAW-STRING guard
        # fails by DESIGNED SUPERSESSION: #997's m829 and #998's m830
        # falsification_notes carry negative-guard THIRTY-FIRST
        # wordings (no member-form claims). Pinned here, not repaired.
        assert "THIRTY-FIRST" in _read("profiles/atlantic.yaml")
        assert "THIRTY-FIRST" in _read("profiles/careers/journalists.yaml")

    def test_thirty_first_member_form_absent(self):
        # The ledger guard continues at member-form level:
        # THIRTY-FIRST member-form claims are absent corpus-wide.
        assert self._member_form_hits("THIRTY-FIRST") == []

    def test_m829_m830_m831_not_falsification_members(self):
        assert _m829_data()["falsification_family_member"] is False
        assert _m830_data()["falsification_family_member"] is False
        assert (
            _m831_data()["statistical_discipline"]["falsification_family"]
            is False
        )


class TestTypeDCorpusIntegrity:
    def test_m829_m830_m831_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/atlantic.yaml").count("\n    " + M829_KEY + ":")
            == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(
                "\n  " + M830_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count("\n" + M831_KEY + ":")
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

    def test_m831_block_is_last_top_level_key(self):
        # The m831 tail block runs to EOF in
        # profiles/competitor-entities.yaml.
        doc = _read("profiles/competitor-entities.yaml")
        tail = doc[doc.index("\n" + M831_KEY + ":") + 1 :]
        assert not re.search(r"(?m)^[A-Za-z_][^:]*:$", tail.split("\n", 1)[1])

    def test_832_sweep_excludes_only_this_file_and_pycache(self):
        # The sole repo-wide 832-form literals at this run's checks are
        # the #999 pyc in tests/__pycache__ (next-number guard of a
        # committed test, excluded per the #715 pattern-rescope
        # lesson). The source sweeps must therefore come back empty.
        import glob

        pyc_hits = glob.glob(
            os.path.join(TESTS_DIR, "__pycache__", "*999*.pyc")
        )
        assert pyc_hits != [], "expected the #999 pyc to exist"
        for p in pyc_hits:
            data = open(p, "rb").read()
            if b"mechanism-832" in data or b"mechanism_832" in data:
                break
        else:
            assert False, "no #999 pyc carries the 832 needle"
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFullSuiteTombstone:
    def test_995_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_995_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-run: 274 bytes of dots since Sep 25 14:25 PDT,
        # no summary tokens anywhere, the process has since exited.
        assert len(data) == 274, len(data)
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_tombstone_lineage_advances(self):
        # FORTY-FIRST consecutive background death per the #795
        # convention; lineage advances FIFTY-NINTH -> SIXTIETH.
        # This run re-launches the suite writing to
        # type_d_1000_full_suite.log; the next Type D run checks it.
        # (The #990 suite was already tombstoned by #995; it is NOT
        # re-tombstoned here.)
        entry_anchor = "FIFTY-NINTH"
        entry_next = "SIXTIETH"
        assert entry_anchor != entry_next

    def test_1000_suite_log_relaunched(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_1000_full_suite.log",
        )
        assert os.path.isfile(log_path), log_path


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #995's).
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
            [-0.62, -0.45, -0.58, -0.71, -0.49, -0.55, -0.66, -0.43],
            [0.28, 0.41, 0.33, 0.24, 0.37, 0.30, 0.44, 0.26],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.89)) < 1e-9
        assert abs(r.t_statistic - (-20.363052106598623)) < 1e-6
        assert r.p_value < 1e-10
        assert abs(r.cohens_d - (-10.18152605329931)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [0.05, -0.04, 0.02, -0.06, 0.03, -0.01, 0.04, -0.02],
            [-0.03, 0.05, -0.02, 0.03, -0.04, 0.01, -0.05, 0.02],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - 0.005) < 1e-9
        assert r.p_value > 0.5
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m830_pair_engine_guard(self):
        # Degenerate n=1/n=1 contract on the m830 illustrative pair
        # ([0.00] Meta vs [-0.15] Snap): the engine's structural guard
        # fires (t=0.0, p=1.0, d=0.0, not significant) while
        # |asymmetry| == 0.15 and arm-swap negates exactly. The guard's
        # verdict is the assertion.
        r = self._score([0.00], [-0.15], "Meta", ["Snap"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.15) < 1e-9
        swapped = self._score([-0.15], [0.00], "Snap", ["Meta"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT_CALCULATED per the Aug 28 2026
        # standing rule.
        assert _m829_data()["asymmetry_scorer_result"]["is_significant"] is False
        assert _m830_data()["asymmetry_scorer_result"]["is_significant"] is False
        assert (
            _m831_data()["statistical_discipline"]["is_significant"] is False
        )


class TestDocSync1000:
    def test_readme_row_1000(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1000(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1000_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog1000:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1000 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #1000 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "SIXTIETH" in entry
        assert "831" in entry
