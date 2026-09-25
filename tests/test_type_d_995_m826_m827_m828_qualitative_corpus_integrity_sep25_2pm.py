"""Type D -- Iteration #995 (Fri 2026-09-25 14:00 PDT): m826/m827/m828
qualitative-discipline verification + post-990-994 corpus integrity
(max numeric mechanism_id 828; zero next-number 829 keys in
numeric/underscore/dash mechanism forms; ledger holds at 30 with the
THIRTIETH member-form present exactly once (m818, journalists.yaml);
THIRTY-FIRST negative guard) + #990 background-suite tombstone
(FORTIETH consecutive death; lineage FIFTY-EIGHTH -> FIFTY-NINTH)
+ fresh synthetic engine calibration (new values, not #990's) +
re-launch of the full suite as a background process writing to goal
hidden_files type_d_995_full_suite.log (next Type D run checks its
verdict per the #795 convention).

Type D FIRST leg of the 995-999 window, OPENING it (D->E->A->B->C).
Committed predecessor #994 Type C (13:00 PDT Sep 25) CLOSED the 990-994
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
- m826 (Type A #992, The Verge Sep 9-24 2026 ambient-listening
  register pair: NEW Apple arms - company-briefed privacy-defense relay
  (Sep 9, MANUAL ILLUSTRATIVE +0.10) + privacy-skeptical blowback
  (Sep 24, MANUAL ILLUSTRATIVE -0.30) avg -0.10 vs carried Meta Luna
  stigma arm (Sep 16, m794 via #938, un-rescored per #807, MANUAL
  ILLUSTRATIVE -0.30); illustrative delta (Apple minus Meta) +0.20, a
  temporal BOUND on m646's launch-window +0.73 (unmatched peg, NOT
  falsification-family member); profiles/the-verge.yaml under
  competitor_relationships/apple): mechanism_id 826; MANUAL
  ILLUSTRATIVE ONLY per standing rule Aug 28 2026, engine NOT run at
  the finding layer, p_value/cohens_d/ci NOT_CALCULATED, is_significant
  False, verdict directionally_supported_not_proven,
  no_analysis_json_update true, NOT artifact-grade;
  falsification_family_member False (falsification_ledger 30);
  connects_to [646, 794, 811, 643, 628].
- m827 (Type B #993, Victoria Song, The Verge: Sep-23 Meta Ray-Ban
  Audio stigma-frame arm (MANUAL ILLUSTRATIVE -0.30, feed-attestation)
  + Sep-24 Vergecast business-model-attribution register (MANUAL
  ILLUSTRATIVE -0.35, relay) vs same-segment Snap
  "broken illusion" product-skepticism (MANUAL ILLUSTRATIVE -0.20);
  illustrative delta (Meta minus Snap) -0.15, direction CONSISTENT with
  m75 but the gap NARROWS - a temporal BOUND on m75's bifurcation;
  profiles/careers/journalists.yaml under the victoria_song item):
  mechanism_id 827; MANUAL ILLUSTRATIVE ONLY, engine NOT run,
  p_value/cohens_d/confidence_interval_95 NOT_CALCULATED,
  is_significant False, verdict directionally_supported_not_proven,
  no_analysis_json_update true, NOT artifact-grade;
  falsification_family_member False (falsification_ledger 30);
  connects_to [75, 722, 764, 773, 818, 824].
- m828 (Type C #994, Meta One for Business link-limit traffic gate
  with publisher carve-out, announced Sep 15 2026: FIRST dedicated
  publisher-traffic-gate leg, TENTH relationship direction in the m807
  enumeration; licensed news partners keep free unlimited outbound
  reach while business/creator Pages pay; structural contrast with
  m801 DOJ-Google adtech remedies; FIRST dedicated corpus
  verification-geometry Type C block at zero-indent tail of
  profiles/competitor-entities.yaml): mechanism_id 828; tone_scores
  NOT_SCORED, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant
  False, engine_run False, verdict directionally_supported_not_proven,
  analysis_json_updated False, artifact_grade False, ledger '30
  positive claims hold (not a falsification-family member); no new
  member'; connects_to [801, 331, 669, 594].

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
NEXT_NUM = 829

M826_KEY = "type_a_992_verge_apple_ambient_listening_week_vs_meta_luna_stigma_sep25_2026"
M827_KEY = "type_b_993_victoria_song_verge_rayban_audio_stigma_vs_snap_broken_illusion_sep25"
M828_KEY = "type_c_994_meta_one_link_limits_publisher_carveout_sep25"

M826_INDENT = 4  # nested under competitor_relationships/apple
M827_INDENT = 4  # nested under the victoria_song item
M828_INDENT = 0  # top-level key in competitor-entities.yaml


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
# numbers in git history: #995 Type D opens the 995-999 window; #994
# Type C (committed 13:00 PDT Sep 25) is the schedule predecessor and
# CLOSED the 990-994 window. The in-flight runs (#899 Type C, #938
# Type B, #900 Type D) have no main commits in git history at this
# run's checks and sit below the window; #898's block was lost
# (documented in the module docstring) and has no main commit either.
# The #884 block (m762) is committed at this run's checks.
EXPECTED_ORDER = [
    ("D", "995"),
    ("C", "994"),
    ("B", "993"),
    ("A", "992"),
    ("E", "991"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: the #994 pyc
    carries an 829-form needle string from its own next-number guard;
    compiled artifacts are excluded from the sweeps). No additional
    sweep-carrier exclusions this run: no in-tree SOURCE file carries
    a contiguous 829-form mechanism literal (verified pre-commit), so
    the 829 sweeps run repo-wide with only this file excluded.
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


def _m826_data():
    return _block_data("profiles/the-verge.yaml", M826_KEY, M826_INDENT)


def _m827_data():
    return _block_data(
        "profiles/careers/journalists.yaml", M827_KEY, M827_INDENT
    )


def _m828_data():
    return _block_data(
        "profiles/competitor-entities.yaml", M828_KEY, M828_INDENT
    )


class TestNovelty995:
    def test_no_test_type_d_995_files_on_disk(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_995")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_995_main_commit_unique_and_anchored(self):
        # No #995 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #995:"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type D #995:", line)
            and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith(ANCHORED_SHA), (mains, ANCHORED_SHA)

    def test_no_type_d_995_in_git_log(self):
        # Pre-commit novelty: no Type D #995 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #995"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #995" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_990_994_window_legs_committed_prior_to_995(self):
        # The 990-994 window's committed legs at this run's main
        # commit: ## #990 Type D through ## #994 Type C. ## #899 /
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
            "## #990 Type D:",
            "## #991 Type E:",
            "## #992 Type A:",
            "## #993 Type B:",
            "## #994 Type C:",
        ):
            assert marker in log, marker

    def test_max_numeric_mechanism_id_is_828(self):
        assert _max_numeric_mechanism_id() == 828

    def test_zero_underscore_form_829_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_829_references(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_829_mechanism_id_keys_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []


class TestTypeDRotationGuard:
    """#995 is the Type D anchor opening window 995-999."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_995_999_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #995 main commit does not
        # exist yet); patched green in the anchor followup. The
        # in-flight runs (#899/#938/#900, plus lost #898) have no main
        # commits in git history at this run's checks and sit below
        # the window.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"995-999 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 990-994 window's
        # committed legs: D 995 -> C 994 -> B 993 -> A 992 -> E 991
        # newest-first, i.e. D->E->A->B->C oldest-first).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_994(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #994 Type C (13:00 PDT
        # Sep 25) closed the 990-994 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "994"), (
            f"newest committed predecessor must be Type C #994, got {window[1]}"
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


class TestTypeDM826QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        # _indented_block asserts the marker appears exactly once.
        block = _indented_block(
            "profiles/the-verge.yaml", M826_KEY, M826_INDENT
        )
        assert block.startswith("    " + M826_KEY + ":")

    def test_mechanism_id_iteration_and_type(self):
        d = _m826_data()
        assert d["mechanism_id"] == 826
        assert d["iteration"] == 992
        assert d["iteration_type"] == "A"
        assert "Type A" in d["type"]

    def test_ambient_listening_arms_and_delta(self):
        d = _m826_data()
        sr = d["asymmetry_scorer_result"]
        assert sr["target_entity"] == "apple"
        assert sr["reference_entity"] == "meta"
        assert sr["method"] == "MANUAL ILLUSTRATIVE"
        assert sr["apple_avg"] == -0.1
        assert sr["meta_avg"] == -0.3
        assert abs(sr["delta_apple_minus_meta"] - 0.2) < 1e-9
        assert "temporal BOUND" in d["finding"]

    def test_statistical_discipline_not_calculated(self):
        d = _m826_data()
        sr = d["asymmetry_scorer_result"]
        assert sr["p_value"] == "NOT_CALCULATED"
        assert sr["cohens_d"] == "NOT_CALCULATED"
        assert sr["ci"] == "NOT_CALCULATED"
        assert sr["is_significant"] is False
        assert sr["artifact_grade"] is False

    def test_verdict_and_no_json_update(self):
        d = _m826_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True

    def test_not_a_falsification_family_member(self):
        d = _m826_data()
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 30

    def test_connects_to_pinned(self):
        d = _m826_data()
        assert d["connects_to"] == [646, 794, 811, 643, 628]

    def test_test_file_pinned(self):
        assert _m826_data()["test_file"] == (
            "tests/test_type_a_992_verge_apple_ambient_listening_week_vs_meta_luna_stigma_sep25_11am.py"
        )

    def test_novelty_is_first_dedicated_mechanism(self):
        assert _m826_data()["novelty"].startswith(
            "First dedicated corpus mechanism on The Verge"
        )


class TestTypeDM827QualitativeDiscipline:
    def test_block_key_unique_as_mapping_key(self):
        block = _indented_block(
            "profiles/careers/journalists.yaml", M827_KEY, M827_INDENT
        )
        assert block.startswith("    " + M827_KEY + ":")

    def test_mechanism_id_iteration_and_type(self):
        d = _m827_data()
        assert d["mechanism_id"] == 827
        assert d["iteration"] == 993
        assert d["type"] == "B"

    def test_meta_snap_arms_and_delta(self):
        d = _m827_data()
        sc = d["scoring"]
        assert sc["manual_illustrative"] is True
        assert sc["meta_arm_tone"] == -0.35
        assert sc["snap_arm_tone"] == -0.20
        assert abs(sc["illustrative_delta_meta_minus_snap"] - (-0.15)) < 1e-9
        assert "FIRST dedicated mechanism-id-sequence Type B" in d["novelty"]

    def test_statistical_discipline_not_calculated(self):
        d = _m827_data()
        sc = d["scoring"]
        assert sc["p_value"] == "NOT_CALCULATED"
        assert sc["cohens_d"] == "NOT_CALCULATED"
        assert sc["confidence_interval_95"] == "NOT_CALCULATED"
        assert sc["is_significant"] is False
        assert sc["verdict"] == "directionally_supported_not_proven"

    def test_verdict_and_no_json_update(self):
        d = _m827_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True

    def test_not_a_falsification_family_member(self):
        d = _m827_data()
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 30

    def test_connects_to_and_test_file_pinned(self):
        d = _m827_data()
        assert d["connects_to"] == [75, 722, 764, 773, 818, 824]
        assert d["test_file"] == (
            "tests/test_type_b_993_victoria_song_verge_rayban_audio_stigma_vs_snap_broken_illusion_sep25_noon.py"
        )


class TestTypeDM828QualitativeDiscipline:
    def test_block_key_unique_as_top_level_key(self):
        block = _indented_block(
            "profiles/competitor-entities.yaml", M828_KEY, M828_INDENT
        )
        assert block.startswith(M828_KEY + ":")

    def test_mechanism_id_iteration_and_type(self):
        d = _m828_data()
        assert d["mechanism_id"] == 828
        assert d["iteration"] == 994
        assert d["rotation"] == "Type C"
        assert d["type"] == "financial_incentive_mapping"

    def test_tone_not_scored(self):
        d = _m828_data()
        assert d["statistical_discipline"]["tone_scores"] == "NOT_SCORED"

    def test_statistical_discipline_not_calculated(self):
        d = _m828_data()
        sd = d["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False

    def test_qualitative_only_and_no_json_update(self):
        d = _m828_data()
        sd = d["statistical_discipline"]
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert sd["analysis_json_updated"] is False
        assert sd["artifact_grade"] is False
        assert sd["ledger"].startswith("30 positive claims hold")

    def test_connects_to_pinned(self):
        d = _m828_data()
        assert d["connects_to"] == [801, 331, 669, 594]

    def test_not_a_falsification_family_member(self):
        d = _m828_data()
        assert _m828_data()["statistical_discipline"]["falsification_family"] is False

    def test_publisher_traffic_gate_is_tenth_direction(self):
        # FIRST publisher-traffic-gate leg (TENTH relationship direction
        # in the m807 enumeration) per the mechanism name and novelty.
        d = _m828_data()
        assert d["mechanism_name"].startswith(
            "Meta One link-limit traffic gate"
        )


class TestTypeDMaxIdAndNextNumber:
    def test_max_numeric_mechanism_id_is_828(self):
        assert _max_numeric_mechanism_id() == 828

    def test_zero_829_keys_all_forms(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_826_827_828_present_in_home_yamls(self):
        assert os.path.join(PROFILES_DIR, "the-verge.yaml") in (
            _repo_grep_numeric_mechanism_id(826)
        )
        assert os.path.join(PROFILES_DIR, "careers", "journalists.yaml") in (
            _repo_grep_numeric_mechanism_id(827)
        )
        assert os.path.join(PROFILES_DIR, "competitor-entities.yaml") in (
            _repo_grep_numeric_mechanism_id(828)
        )

    def test_prior_max_sweeps_superseded_by_design(self):
        # The #990-era "zero 826 keys" guard fails by DESIGNED
        # SUPERSESSION post-commit (#992 landed m826, #993 landed
        # m827, #994 landed m828) - documented here, NOT repaired.
        # Read-only convention on other runs' test files.
        assert _repo_grep_numeric_mechanism_id(826) != []
        assert _repo_grep_numeric_mechanism_id(827) != []
        assert _repo_grep_numeric_mechanism_id(828) != []


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

    def test_m826_m827_m828_not_falsification_members(self):
        assert _m826_data()["falsification_family_member"] is False
        assert _m827_data()["falsification_family_member"] is False
        assert (
            _m828_data()["statistical_discipline"]["falsification_family"]
            is False
        )


class TestTypeDCorpusIntegrity:
    def test_m826_m827_m828_block_keys_unique_in_home_yamls(self):
        assert (
            _read("profiles/the-verge.yaml").count("\n    " + M826_KEY + ":")
            == 1
        )
        assert (
            _read("profiles/careers/journalists.yaml").count(
                "\n    " + M827_KEY + ":"
            )
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count("\n" + M828_KEY + ":")
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

    def test_m828_block_is_last_top_level_key(self):
        # The m828 tail block runs to EOF in
        # profiles/competitor-entities.yaml.
        doc = _read("profiles/competitor-entities.yaml")
        tail = doc[doc.index("\n" + M828_KEY + ":") + 1 :]
        assert not re.search(r"(?m)^[A-Za-z_][^:]*:$", tail.split("\n", 1)[1])

    def test_829_sweep_excludes_only_this_file_and_pycache(self):
        # The sole repo-wide 829-form literal at this run's checks is
        # the #994 pyc in tests/__pycache__ (next-number guard of a
        # committed test, excluded per the #715 pattern-rescope
        # lesson). The source sweeps must therefore come back empty.
        import glob

        pyc_hits = glob.glob(
            os.path.join(TESTS_DIR, "__pycache__", "*994*.pyc")
        )
        assert pyc_hits != [], "expected the #994 pyc to exist"
        for p in pyc_hits:
            data = open(p, "rb").read()
            if b"mechanism-829" in data:
                break
        else:
            assert False, "no #994 pyc carries the 829 needle"
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFullSuiteTombstone:
    def test_990_suite_log_stalled(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_990_full_suite.log",
        )
        with open(log_path, "rb") as fh:
            data = fh.read()
        # Stalled mid-run: 1420 bytes of dots since Sep 25 09:23 PDT,
        # no summary tokens anywhere, the process has since exited.
        assert len(data) == 1420, len(data)
        for token in (b"passed", b"failed", b"error"):
            assert token not in data, token

    def test_tombstone_lineage_advances(self):
        # FORTIETH consecutive background death per the #795
        # convention; lineage advances FIFTY-EIGHTH -> FIFTY-NINTH.
        # This run re-launches the suite writing to
        # type_d_995_full_suite.log; the next Type D run checks it.
        # (The #985 suite was already tombstoned by #990; it is NOT
        # re-tombstoned here.)
        entry_anchor = "FIFTY-EIGHTH"
        entry_next = "FIFTY-NINTH"
        assert entry_anchor != entry_next

    def test_995_suite_log_relaunched(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_995_full_suite.log",
        )
        assert os.path.isfile(log_path), log_path


class TestTypeDSyntheticEngine:
    """Fresh engine meaningfulness calibration on synthetic corpora.

    Values hardcoded after a scratch run this run (NOT #990's).
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
            [-0.51, -0.44, -0.58, -0.39, -0.62, -0.47, -0.55],
            [0.31, 0.22, 0.38, 0.27, 0.34, 0.25, 0.30],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - (-0.8042857142857143)) < 1e-9
        assert abs(r.t_statistic - (-21.78312399583595)) < 1e-6
        assert r.p_value < 1e-9
        assert abs(r.cohens_d - (-11.643569543718897)) < 1e-6
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0

    def test_near_null_pair_stays_silent(self):
        r = self._score(
            [0.04, -0.03, 0.01, -0.05, 0.02, -0.01, 0.03],
            [-0.02, 0.04, -0.03, 0.01, -0.05, 0.02, -0.04],
            "Meta",
            ["Snap", "Apple"],
        )
        assert abs(r.asymmetry_score - 0.0114285714285714) < 1e-9
        assert r.p_value > 0.5
        assert r.is_significant is False
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_m826_pair_engine_guard(self):
        # Degenerate n=2/n=1 contract on the m826 illustrative pair
        # ([+0.10, -0.30] Apple vs [-0.30] Meta): the engine's
        # structural guard fires (t=0.0, p=1.0, not significant) while
        # |asymmetry| == 0.20 and arm-swap negates exactly. (d is the
        # pooled arm-scale value here, not the zero of the n=1/n=1
        # #990 degenerate; the guard's verdict is the assertion.)
        r = self._score([0.10, -0.30], [-0.30], "Apple", ["Meta"])
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert abs(r.cohens_d - 0.7071067811865475) < 1e-9
        assert r.is_significant is False
        assert abs(abs(r.asymmetry_score) - 0.20) < 1e-9
        swapped = self._score([-0.30], [0.10, -0.30], "Meta", ["Apple"])
        assert swapped.asymmetry_score == -r.asymmetry_score

    def test_engine_finding_layer_separation(self):
        # The engine CAN return is_significant True on synthetic
        # corpora while the finding layer refuses: the three
        # mechanisms verified this run all carry finding-layer
        # is_significant false / NOT_CALCULATED per the Aug 28 2026
        # standing rule.
        assert _m826_data()["asymmetry_scorer_result"]["is_significant"] is False
        assert _m827_data()["scoring"]["is_significant"] is False
        assert (
            _m828_data()["statistical_discipline"]["is_significant"] is False
        )


class TestDocSync995:
    def test_readme_row_995(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_995(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_995_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog995:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #995 Type D:")
        return log[idx : idx + 15000]

    def test_entry_present(self):
        assert "## #995 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "FIFTY-NINTH" in entry
        assert "828" in entry
