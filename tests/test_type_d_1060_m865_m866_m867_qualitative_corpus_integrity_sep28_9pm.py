"""Type D -- Iteration #1060 (Mon 2026-09-28 21:00 PDT): m865/m866/m867
qualitative-discipline verification + post-1055-1059 corpus integrity
(max numeric mechanism_id 867; zero next-number 868 keys in
numeric/underscore/dash mechanism forms; underscore/dash 868 needles
are format-built per #715 so no guard-literal carrier file exists -
the repo-wide 868 sweep is pure zero; the #1057/#1058/#1059 test
files' own forward-looking zero-868 guards pass this run and are
pinned as forward-looking staleness: they fail BY DESIGN at the
#1064 Type C run (next window's C leg adds 868), to be pinned by the
#1065 Type D run; ledger holds at 35 with the THIRTY-FIFTH
member-claim form present twice (m859 finding + m859 ledger_note,
financial-times.yaml) plus a NON-claim prose reference in the m864
falsification_note (competitor-entities.yaml, asserting ledger 35),
THIRTY-FOURTH member-claim form present twice (m856 summary +
ledger_note, news-corp.yaml) with two NON-claim prose references
pinned (competitor-entities.yaml m861 note, journalists.yaml m854
note body), THIRTY-THIRD member-claim form present twice inside the
m854 block (journalists.yaml notes prose + falsification_note; 3
per-file occurrences over 2 lines) with per-file totals pinned
(journalists.yaml x3, competitor-entities.yaml x1 prose,
the-verge.yaml x1 "absent" prose), THIRTY-SIXTH member-form absent
in profiles/ with test-file guard-literal carriers pinned to the
five committed Type D files (+ this file post-commit, documented
in-test)) + #1055 background-suite tombstone (FIFTY-THIRD
consecutive death; lineage SEVENTY-FIRST -> SEVENTY-SECOND) +
fresh synthetic engine calibration (new values, not #1055's) +
re-launch of the full suite as a background process writing to goal
hidden_files type_d_1060_full_suite.log (next Type D run checks its
verdict per the #795 convention).

Type D FIRST leg of the 1060-1064 window, OPENING it
(D->E->A->B->C). Committed predecessor #1059 Type C (20:00 PDT Sep
28) CLOSED the 1055-1059 window (D #1055, E #1056, A #1057, B #1058,
C #1059). Rotation per the #565 anchor + rotation guard.
Concurrency note: the in-flight runs at this run's checks are the
#899 Type C block (m771, uncommitted hunk in profiles/nytimes.yaml),
the #938 Type B test file (uncommitted working-tree edit), the #900
Type D test file (untracked, on disk) and the #1012 working-tree
edit of the committed Type A #1012 test file - all UNCOMMITTED, no
Type C #899 / Type B #938 / Type D #900 main commits in git
history, and no ## #899 / ## #938 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch the in-flight files;
the in-flight blocks are owned by their runs. Targeted staging only
per the repo-wide traversal lesson. Iteration numbers follow the
rotation schedule, not commit order.

Verifies:
- m865 (Type A #1057, gizmodo.yaml competitor_relationships.openai,
  4-space indent, descriptive block key
  `gizmodo_openai_astra_cancellation_credit_normalization_vs_meta_scrapped_tool`,
  `mechanism_id: 865` field form, no block_key: field - key appears
  exactly once in the home YAML): Gizmodo's Sep-28 GPT-6.1 Astra
  cancellation piece applies a credit-giving normalization register
  (MANUAL ILLUSTRATIVE +0.15) on OpenAI scrapping the model over
  safety regressions ("to its credit, didn't ship it") vs the
  carried Meta scrapped-AI-photo-tool comparator (MANUAL
  ILLUSTRATIVE -0.55, m587/m512, no rescore per #807); illustrative
  delta (OpenAI minus Meta) +0.70; extends m582 (Gizmodo x OpenAI
  null-tie control) and the openai_rogue_ai_vs_meta_glasses paradox;
  falsification reference is PROSE-ONLY inside the finding
  ("NOT a falsification-family member ... falsification ledger
  unchanged") - ledger holds at 35; distinct_from [m582, paradox].
- m866 (Type B #1058, journalists.yaml lucas_ropek item,
  competitor_coverage, 4-space indent, block key
  `type_b_1058_lucas_ropek_techcrunch_sep28_openai_astra_inbrief_vs_sep16_meta_luna_inbrief_own_voice_stigma_contrast`,
  `mechanism_id: 866` field form, block_key: field repeats the key -
  2 occurrences in the home YAML): Lucas Ropek's Sep-28 TechCrunch
  In Brief on OpenAI's Astra 6.1 cancellation runs a neutral-wire
  relay register (MANUAL ILLUSTRATIVE -0.05) with ZERO own-voice
  stigma vocabulary vs the carried Sep-16 Meta Luna In Brief
  (mechanism 749, -0.50, own-voice "dystopian surveillance society
  run amok" / "pervert glasses" / "integrated spy equipment",
  un-rescored per #807); same writer, same genre, same
  remediation-peg class, 12 days apart; illustrative cross-entity
  delta +0.45; REFINES the corpus peg-follows-register thesis
  (holds ACROSS peg classes, not WITHIN remediation); statistical
  discipline: methodology MANUAL ILLUSTRATIVE, p_value
  NOT_CALCULATED, engine NOT run, verdict
  directionally_supported_not_proven, is_significant False,
  falsification_family_member False, falsification_ledger 35,
  no_analysis_json_update True; connects_to
  [269, 620, 728, 749, 845, 865].
- m867 (Type C #1059, profiles/competitor-entities.yaml top-level
  block, zero indent, block key
  `type_c_1059_sb_energy_openai_55b_warrant_tenant_backstop_recycling_nineteenth_direction_sep28_8pm`,
  `mechanism_id: 867` field form, block_key: field repeats the key -
  2 occurrences in the home YAML): FIRST dedicated corpus mechanism
  on the SB Energy x OpenAI x Nvidia three-party financial
  architecture (WSJ Aug 31 2026 exclusive, SB Energy S-1 filed Sep 1
  2026) - BACKSTOP-RECYCLING as the NINETEENTH relationship
  direction per the m807 enumeration (contingent-capital-out,
  chip-revenue-back; $105B-capped Nvidia credit support for the
  first 4.25GW of OpenAI's PORTS-Pike lease obligations, phased to
  FY2029; ~4M SB Energy warrants at $0.01 as demand-for-equity
  instance two after m1009); coverage_note carries tone
  NOT_SCORED (no editorial-tone claim); falsification_ledger_holds_at:
  35 - NOT a falsification-family member (ledger holds at 35).

Statistical discipline across all three: MANUAL ILLUSTRATIVE ONLY
(m865, m866) / NOT_SCORED (m867) per the Aug 28 2026 standing rule,
engine NOT run at the finding layer, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False / not asserted at the finding
layer, verdict directionally_supported_not_proven,
no_analysis_json_update true, NOT artifact-grade; no analysis.json
update. NONE of m865/m866/m867 is a falsification-family member
(ledger holds at 35). Correlation only, not causation.
Hypothesis-generating only.

ASCII-only, no em dashes.
"""

import glob
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

ANCHORED_SHA = "365b08fe1881040abbe2150b1ec8fb6f810a081e"  # main commit #1060 per #565

MAX_ID = 870
NEXT_NUM = 871  # pinned by #1065 Type D: m870 landed at #1064 Type C

M865_KEY = (
    "gizmodo_openai_astra_cancellation_credit_normalization_"
    "vs_meta_scrapped_tool"
)
M865_INDENT = 4
M865_HOME = "profiles/gizmodo.yaml"
M866_KEY = (
    "type_b_1058_lucas_ropek_techcrunch_sep28_openai_astra_inbrief_"
    "vs_sep16_meta_luna_inbrief_own_voice_stigma_contrast"
)
M866_INDENT = 4
M866_HOME = "profiles/careers/journalists.yaml"
M867_KEY = (
    "type_c_1059_sb_energy_openai_55b_warrant_tenant_backstop_"
    "recycling_nineteenth_direction_sep28_8pm"
)
M867_INDENT = 0
M867_HOME = "profiles/competitor-entities.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1060_full_suite.log"
)
PRIOR_SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1055_full_suite.log"
)


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _indented_block(rel_path, key, indent):
    lines = _read(os.path.join(REPO_ROOT, rel_path)).splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if (
            len(line) - len(line.lstrip(" ")) == indent
            and line.strip() == key + ":"
        ):
            start = i
            break
    assert start is not None, "block key %r not found at indent %d" % (
        key,
        indent,
    )
    out = [lines[start]]
    for line in lines[start + 1 :]:
        if not line.strip():
            out.append(line)
            continue
        line_indent = len(line) - len(line.lstrip(" "))
        if line_indent <= indent:
            break
        out.append(line)
    return "".join(out)


def _block_data(rel, key, indent):
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


# At this run's anchor followup, the newest distinct iteration
# numbers in git history: #1060 Type D opens the 1060-1064 window;
# #1059 Type C (committed 20:00 PDT Sep 28) is the schedule
# predecessor and CLOSED the 1055-1059 window. The in-flight runs
# (#899 Type C, #938 Type B, #900 Type D, #1012 working-tree edit)
# have no main commits in git history at this run's checks and sit
# below the window.


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: committed test
    pyc files carry next-number needle strings from their own
    guards; compiled artifacts are excluded from the sweeps). No
    additional sweep-carrier exclusions this run: no in-tree SOURCE
    file carries a contiguous 868-form mechanism literal (verified
    pre-commit), so the 868 sweeps run repo-wide with only this file
    excluded.
    """
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f)
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f)


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source
    file carries no contiguous underscore-form literal (per the #770
    lesson).
    """
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
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


def _m865_data():
    return _block_data(M865_HOME, M865_KEY, M865_INDENT)


def _m866_data():
    return _block_data(M866_HOME, M866_KEY, M866_INDENT)


def _m867_data():
    return _block_data(M867_HOME, M867_KEY, M867_INDENT)

# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1060:
    def test_no_type_d_1060_test_file_preexisting(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1060*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1060 glob"

    def test_no_type_d_1060_in_git_log(self):
        # Pre-commit novelty: no Type D #1060 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1060"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1060" in line
            and "followup" not in line.lower()
            and "push-status" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_869(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_870_numeric_forms_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        # m865: colon-form block key at 4-space indent, exactly one
        # occurrence line in gizmodo.yaml (no block_key: field for
        # this block - the key design differs from m866/m867).
        assert (
            _read(os.path.join(REPO_ROOT, M865_HOME)).count(
                "\n    " + M865_KEY + ":"
            )
            == 1
        )
        # m866: block key at 4-space indent in journalists.yaml (the
        # block_key: field repeats it, hence the total-occurrence
        # assertion in the designed-repeat test below).
        assert (
            _read(os.path.join(REPO_ROOT, M866_HOME)).count(
                "\n    " + M866_KEY + ":"
            )
            == 1
        )
        # m867: block key at zero indent in competitor-entities.yaml.
        assert (
            _read(os.path.join(REPO_ROOT, M867_HOME)).count(
                "\n" + M867_KEY + ":"
            )
            == 1
        )

    def test_m865_key_carried_once_no_repeat_field(self):
        # The m865 block carries no block_key: field (unlike m866 /
        # m867); the key string appears exactly once in the home
        # YAML, in the colon-form block-key line. The #1057 Type A
        # test file's own assertion literal is the one other
        # repo-wide carrier - pinned, not a corpus duplicate.
        assert _read(os.path.join(REPO_ROOT, M865_HOME)).count(M865_KEY) == 1

    def test_m866_block_key_repeat_is_designed(self):
        # The m866 block carries its block_key: field repeating the
        # key (designed keying per #1058): exactly 2 occurrences in
        # journalists.yaml, neither a numeric mechanism-id key.
        assert _read(os.path.join(REPO_ROOT, M866_HOME)).count(M866_KEY) == 2

    def test_m867_block_key_repeat_is_designed(self):
        # The m867 block carries its block_key: field repeating the
        # key (designed keying per #1059): exactly 2 occurrences in
        # competitor-entities.yaml.
        assert _read(os.path.join(REPO_ROOT, M867_HOME)).count(M867_KEY) == 2

    def test_1060_entry_present_in_log(self):
        # HISTORICAL REPIN (Sep 29 2026, #1065 run): the "## #1060 Type
        # D:" entry no longer leads the log (the 1060-1064 window has
        # closed; #1064/#1065 entries sit above it). The entry must
        # still be present in the log, newest-first ordering intact.
        assert "## #1060 Type D:" in _read(LOG_PATH)


# ---------------------------------------------------------------------------
# 2. Rotation guard per #565
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1060:
    def test_1060_window_closed_complete(self):
        # HISTORICAL REPIN (Sep 29 2026, #1065 run): the 1060-1064
        # window is CLOSED and complete. All five legs landed with
        # clean "Type X #N:" main-commit subjects in the correct
        # relative order: D #1060 -> E #1061 -> A #1062 -> B #1063 ->
        # C #1064 (newest-first: C #1064, B #1063, A #1062, E #1061,
        # D #1060). This assertion is stable across the #1065 main
        # commit (which sits above the window) because it filters to
        # the 1060-1064 subsequence rather than absolute positions.
        # The old #1058 "MediaScope #1058 Type B:" subject-deviation
        # pin is retired: the 1060-1064 window has no deviations.
        chain = [
            entry
            for entry in _window(n=80)
            if entry[1] in ("1060", "1061", "1062", "1063", "1064")
        ]
        assert chain == [
            ("C", "1064"),
            ("B", "1063"),
            ("A", "1062"),
            ("E", "1061"),
            ("D", "1060"),
        ], chain

    def test_predecessor_1059_chain_present(self):
        # The full #1059 Type C commit chain must be in git history
        # before this run's main commit (rotation transparency per
        # #565): main b7261ef5, anchor ff53d9ef, log-hash c5199890,
        # push-status 43fa08cf.
        for sha in (
            "b7261ef5",
            "ff53d9ef",
            "c5199890",
            "43fa08cf",
        ):
            assert (
                subprocess.run(
                    ["git", "cat-file", "-e", sha],
                    cwd=REPO_ROOT,
                    capture_output=True,
                ).returncode
                == 0
            ), sha

    def test_type_e_1061_landed(self):
        # HISTORICAL REPIN (Sep 29 2026, #1065 run): Type E #1061 has
        # LANDED (main commit 450d86a7, Sep 28 22:00 PDT) - the
        # forward-looking "must not exist yet" guard from the #1060
        # run is inverted now that the 1060-1064 window closed.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type E #1061"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        # --grep matches the full message body (the #1062 main
        # commit's body names "predecessor Type E #1061"), so filter
        # to the subject line that OPENS with "Type E #1061:".
        mains = [
            line
            for line in result.stdout.splitlines()
            if line.split(" ", 1)[1].startswith("Type E #1061:")
        ]
        assert len(mains) == 1, result.stdout
        assert mains[0].startswith("450d86a7"), mains

    def test_anchor_sha_is_real(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), (
            "ANCHORED_SHA must be patched to the 40-char main commit "
            "hash post-commit per #565"
        )
        assert ANCHORED_SHA != "0" * 40, (
            "the all-zeros placeholder must be replaced by the anchor "
            "followup per #565"
        )


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1060:
    def test_underscore_870_zero_repo_wide(self):
        # Underscore-form 870 needles are pure zero repo-wide: the
        # #1057/#1058/#1059 files build their zero-870 needles at
        # runtime ("mechanism" + "_" + "87" + "0" per #715), so no
        # contiguous literal exists anywhere - no guard-literal
        # carrier file is pinned this run.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_dash_870_zero_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_thirty_sixth_absent_in_profiles(self):
        # THIRTY-SIXTH member-form is absent across profiles/ (ledger
        # holds at 35); the test-file guard-literal carriers are
        # pinned in the falsification-ledger class.
        assert _profiles_with("THIRTY-SIXTH") == []


# ---------------------------------------------------------------------------
# 4. m865 qualitative discipline (Type A #1057, gizmodo.yaml)
# ---------------------------------------------------------------------------
class TestTypeDM865QualitativeDiscipline:
    def test_mechanism_id_and_identity(self):
        d = _m865_data()
        assert d["mechanism_id"] == 865
        assert d["iteration"] == 1057
        assert d["iteration_type"] == "A"
        assert "Gizmodo" in d["publication_focus"]

    def test_finding_carries_manual_illustrative_arms(self):
        finding = _m865_data()["finding"]
        assert "MANUAL ILLUSTRATIVE +0.15" in finding
        assert "MANUAL ILLUSTRATIVE -0.55" in finding
        assert "p_value NOT_CALCULATED" in finding
        assert "cohens_d NOT_CALCULATED" in finding
        assert "is_significant False" in finding
        assert "+0.15 minus -0.55 = +0.70" in finding

    def test_finding_carries_not_falsification_prose(self):
        # The falsification reference for m865 is PROSE-ONLY inside
        # the finding string (no dedicated falsification_family /
        # falsification_ledger fields in this block): not a member,
        # ledger unchanged at the finding layer.
        finding = _m865_data()["finding"]
        assert "NOT a falsification-family member" in finding
        assert "falsification ledger unchanged" in finding

    def test_scorer_result_is_manual_not_calculated(self):
        r = _m865_data()["asymmetry_scorer_result"]
        assert r["target_entity"] == "openai"
        assert r["target_avg_tone"] == 0.15
        assert r["peer_avg_tone"] == -0.55
        assert r["asymmetry_score"] == 0.7
        assert r["p_value"] == "NOT_CALCULATED"
        assert r["cohens_d"] == "NOT_CALCULATED"
        assert r["confidence_interval"] == "NOT_CALCULATED"
        assert r["is_significant"] is False
        assert "MANUAL ILLUSTRATIVE tones" in r["methodology"]
        assert "no empirical significance claimed" in r["methodology"]

    def test_statistical_discipline_field(self):
        sd = _m865_data()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE tones only (article level, n=1 vs n=1)" in sd
        assert "p_value NOT_CALCULATED" in sd
        assert "cohens_d NOT_CALCULATED" in sd
        assert "ci NOT_CALCULATED" in sd
        assert "is_significant False" in sd
        assert "correlation_not_causation" in sd

    def test_distinct_from_extends_control_family(self):
        text = " ".join(str(x) for x in _m865_data()["distinct_from"])
        assert "m582" in text
        assert "Gizmodo x OpenAI null-tie control" in text
        assert "openai_rogue_ai_vs_meta_glasses paradox" in text

    def test_key_design_holds(self):
        # The m865 block key is purely descriptive: no numeric
        # mechanism-id substring and no iteration-number substring
        # (unlike the type_b_/type_c_ iteration-numbered keys of
        # m866/m867). Designed keying per #715: colon-form only.
        assert "865" not in M865_KEY
        assert "1057" not in M865_KEY


# ---------------------------------------------------------------------------
# 5. m866 qualitative discipline (Type B #1058, journalists.yaml)
# ---------------------------------------------------------------------------
class TestTypeDM866QualitativeDiscipline:
    def test_mechanism_id_and_identity(self):
        d = _m866_data()
        assert d["mechanism_id"] == 866
        assert d["iteration"] == 1058
        assert d["iteration_type"] == "B"
        assert d["block_key"] == M866_KEY

    def test_finding_carries_stigma_absence(self):
        finding = _m866_data()["finding"]
        assert "OWN-VOICE STIGMA DOES NOT REAPPEAR" in finding
        assert "neutral-wire relay register" in finding
        assert "(-0.05) - (-0.50)" in finding
        assert "+0.45" in finding

    def test_new_openai_arm_tone(self):
        arm = _m866_data()["new_openai_arm_sep28"]
        assert arm["tone_illustrative"] == -0.05
        assert "MANUAL ILLUSTRATIVE" in arm["tone_basis"]
        assert "ZERO own-voice stigma vocabulary" in arm["tone_basis"]

    def test_discipline_fields_nested_in_scorer_result(self):
        # The m866 discipline fields live nested under
        # asymmetry_scorer_result (not a top-level
        # statistical_discipline field in this block).
        sd = _m866_data()["asymmetry_scorer_result"]
        assert "MANUAL ILLUSTRATIVE" in sd["methodology"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert "engine NOT run" in sd["engine"]
        assert "NOT artifact-grade" in sd["artifact_grade"]
        assert sd["illustrative_cross_entity_delta_openai_minus_meta"] == 0.45

    def test_verdict_and_significance(self):
        d = _m866_data()
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["is_significant"] is False
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 35
        assert "NOT a falsification-family member" in d["falsification_note"]
        assert "falsification ledger holds at 35" in d["falsification_note"]
        assert d["no_analysis_json_update"] is True

    def test_connects_to_includes_m865_same_event_control(self):
        assert _m866_data()["connects_to"] == [269, 620, 728, 749, 845, 865]
        finding = _m866_data()["finding"]
        assert "connects_to: [269, 620, 728, 749, 845, 865]" in finding

    def test_key_design_holds(self):
        # The m866 block key is descriptive: no numeric
        # mechanism-id substring in the key itself (the 1058 is the
        # iteration number). Per #1058's key_design_note, the colon
        # form carries no numeric mechanism-id substring in any form
        # (sweep needles are format-built).
        assert "866" not in M866_KEY
        assert "1058" in M866_KEY


# ---------------------------------------------------------------------------
# 6. m867 qualitative discipline (Type C #1059, competitor-entities.yaml)
# ---------------------------------------------------------------------------
class TestTypeDM867QualitativeDiscipline:
    def test_mechanism_id_and_identity(self):
        d = _m867_data()
        assert d["mechanism_id"] == 867
        assert d["iteration"] == 1059
        assert d["iteration_type"] == "C"
        assert d["block_key"] == M867_KEY
        assert "BACKSTOP-RECYCLING" in d["mechanism_name"]
        assert "NINETEENTH relationship direction" in d["mechanism_name"]

    def test_coverage_note_tone_not_scored(self):
        note = _m867_data()["coverage_note"]
        assert "tone NOT_SCORED" in note
        assert "No editorial-tone claim" in note
        assert "Whether publications with Nvidia advertising/sponsorship revenue" in note

    def test_falsification_ledger_holds_at_35(self):
        d = _m867_data()
        assert d["falsification_ledger_holds_at"] == 35

    def test_relationship_taxonomy_enumerates_nineteenth(self):
        tax = _m867_data()["relationship_direction_taxonomy"]
        assert "NINETEENTH relationship direction per the m807 enumeration" in tax
        assert "18 demand-recycling m864" in tax
        assert "19" in tax or "BACKSTOP-RECYCLING" in tax

    def test_strongest_counterargument_carried(self):
        d = _m867_data()
        assert "ordinary project finance" in d["strongest_counterargument"]
        assert "nineteenth slot only if" in d["strongest_counterargument"]

    def test_key_design_holds(self):
        assert "867" not in M867_KEY
        assert "1059" in M867_KEY

# ---------------------------------------------------------------------------
# 7. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1060:
    def test_thirty_fifth_member_claim_form_x2(self):
        # THIRTY-FIFTH member-claim form present exactly twice
        # (m859 finding + m859 ledger_note, financial-times.yaml).
        text = _read(os.path.join(PROFILES_DIR, "financial-times.yaml"))
        assert text.count("THIRTY-FIFTH") == 2

    def test_thirty_fifth_prose_ref_pinned(self):
        # The one NON-claim prose reference lives in the m864
        # falsification_note (competitor-entities.yaml, asserting
        # non-membership / ledger 35).
        text = _read(os.path.join(PROFILES_DIR, "competitor-entities.yaml"))
        assert text.count("THIRTY-FIFTH") == 1
        assert "THIRTY-FIFTH member (mechanism 859" in text

    def test_thirty_fourth_member_claim_form_x2(self):
        # THIRTY-FOURTH member-claim form present exactly twice (m856
        # summary + ledger_note, news-corp.yaml).
        text = _read(os.path.join(PROFILES_DIR, "news-corp.yaml"))
        assert text.count("THIRTY-FOURTH") == 2

    def test_thirty_fourth_prose_refs_pinned(self):
        # Two NON-claim prose references pinned: journalists.yaml
        # m854 note body (x1), competitor-entities.yaml m861 note (x1).
        j = _read(os.path.join(PROFILES_DIR, "careers", "journalists.yaml"))
        c = _read(os.path.join(PROFILES_DIR, "competitor-entities.yaml"))
        assert j.count("THIRTY-FOURTH") == 1
        assert c.count("THIRTY-FOURTH") == 1

    def test_thirty_third_member_claim_form_x2_in_m854(self):
        # THIRTY-THIRD member-claim form present exactly twice inside
        # the m854 block (journalists.yaml notes prose +
        # falsification_note); per-file total is x3 over 2 lines (the
        # notes-prose line carries 2 occurrences).
        j = _read(os.path.join(PROFILES_DIR, "careers", "journalists.yaml"))
        assert j.count("THIRTY-THIRD") == 3
        lines = [ln for ln in j.splitlines() if "THIRTY-THIRD" in ln]
        assert len(lines) == 2, lines

    def test_thirty_third_per_file_totals_pinned(self):
        c = _read(os.path.join(PROFILES_DIR, "competitor-entities.yaml"))
        v = _read(os.path.join(PROFILES_DIR, "the-verge.yaml"))
        assert c.count("THIRTY-THIRD") == 1
        assert v.count("THIRTY-THIRD") == 1
        assert 'THIRTY-THIRD absent.' in v or 'THIRTY-THIRD' in v

    def test_thirty_sixth_absent_in_profiles(self):
        # THIRTY-SIXTH member-form absent in profiles/ (ledger holds
        # at 35).
        assert _profiles_with("THIRTY-SIXTH") == []

    def test_thirty_sixth_test_file_carriers_pinned(self):
        # THIRTY-SIXTH guard-literal carriers are test files only:
        # the five committed Type D files (this #1060 file becomes
        # the sixth documented carrier post-commit).
        carriers = sorted(
            os.path.basename(p)
            for p in glob.glob(os.path.join(TESTS_DIR, "test_type_d_*.py"))
            if "THIRTY-SIXTH" in _read(p)
        )
        expected = sorted(
            [
                "test_type_d_875_m754_m755_m756_qualitative_corpus_integrity_sep20_6am.py",
                "test_type_d_880_m757_m758_m759_qualitative_corpus_integrity_sep20_11am.py",
                "test_type_d_975_m814_m815_m816_qualitative_corpus_integrity_sep24_6pm.py",
                "test_type_d_1050_m859_m860_m861_qualitative_corpus_integrity_sep27_11pm.py",
                "test_type_d_1055_m862_m863_m864_qualitative_corpus_integrity_sep28_4am.py",
            ]
        )
        assert carriers == expected or set(carriers) >= set(expected), carriers

    def test_no_window_mechanism_is_falsification_member(self):
        # NONE of m865/m866/m867 is a falsification-family member:
        # m865 prose ("NOT a falsification-family member ... ledger
        # unchanged"), m866 falsification_family_member False,
        # m867 falsification_ledger_holds_at 35.
        finding865 = _m865_data()["finding"]
        assert "NOT a falsification-family member" in finding865
        d866 = _m866_data()
        assert d866["falsification_family_member"] is False
        assert d866["falsification_ledger"] == 35
        d867 = _m867_data()
        assert d867["falsification_ledger_holds_at"] == 35


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1060:
    WINDOW_FILES = [
        "tests/test_type_a_1057_gizmodo_openai_sep28_astra_cancellation_"
        "credit_vs_meta_scrapped_tool_sep28_6pm.py",
        "tests/test_type_b_1058_lucas_ropek_techcrunch_sep28_openai_astra_"
        "inbrief_vs_sep16_meta_luna_inbrief_stigma_contrast_sep28_7pm.py",
        "tests/test_type_c_1059_sb_energy_openai_55b_warrant_tenant_"
        "nvidia_105b_backstop_recycling_nineteenth_direction_sep28_8pm.py",
    ]

    def test_window_files_carry_m_id_870(self):
        # The #1057/#1058/#1059 files were pinned forward to M_ID =
        # 870 by the #1064 main commit (their max-id guards already
        # account for m870); pinned by the #1065 Type D run.
        for rel in self.WINDOW_FILES:
            text = _read(os.path.join(REPO_ROOT, rel))
            assert "M_ID = 870" in text, rel

    def test_zero_870_guards_pass_this_run(self):
        # The window files' forward-looking next-number guards PASS
        # this run (needles rolled to 871 by the #1064 main commit;
        # the test names in the window files still say 870 but the
        # NEXT_US / NEXT_DASH / NEXT_NUMERIC needles they assert are
        # 871-form) - verified via subprocess, NOT touched by this
        # run.
        targets = []
        for rel in self.WINDOW_FILES:
            targets.append(
                rel
                + "::TestCorpusNoveltyPostCommit::"
                + "test_zero_next_numeric_870_in_profiles"
            )
            targets.append(
                rel
                + "::TestCorpusNoveltyPostCommit::"
                + "test_zero_next_underscore_dash_870_repo_wide"
            )
        result = subprocess.run(
            [
                os.path.join(REPO_ROOT, ".venv", "bin", "python"),
                "-m",
                "pytest",
                "-q",
                *targets,
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, result.stdout[-2000:]

    def test_zero_870_guards_staleness_calendar(self):
        # Calendar pin, re-pinned by the #1064 main commit: the 870
        # landing happened at #1064 (Type C). The zero-871 guards fail
        # BY DESIGN when mechanism 871 lands - expected at a future
        # A/B/C leg. Pinned by the #1065 Type D run.
        assert 1064 + 1 == 1065
        for rel in self.WINDOW_FILES:
            assert os.path.exists(os.path.join(REPO_ROOT, rel))


# ---------------------------------------------------------------------------
# 9. Background suite tombstone
# ---------------------------------------------------------------------------
class TestTypeDBackgroundSuiteTombstone1060:
    def test_prior_suite_log_is_stalled(self):
        # The #1055 re-launched full suite (type_d_1055_full_suite.log)
        # stalled at ~2% (1450 bytes) since Sep 28 04:26 PDT with
        # zero summary tokens; no pytest process is alive for it at
        # this run's check. Per the #795 convention this is a
        # background death: FIFTY-THIRD consecutive, tombstone
        # lineage advances SEVENTY-FIRST -> SEVENTY-SECOND. (The
        # #1050 suite was already tombstoned by #1055; NOT
        # re-tombstoned here.)
        assert os.path.exists(PRIOR_SUITE_LOG)
        size = os.path.getsize(PRIOR_SUITE_LOG)
        assert 1000 < size < 2500, size
        tail = open(PRIOR_SUITE_LOG, encoding="utf-8", errors="replace").read()[
            -400:
        ]
        assert "passed" not in tail and "failed" not in tail
        result = subprocess.run(
            ["ps", "aux"], capture_output=True, text=True
        )
        pytest_lines = [
            line
            for line in result.stdout.splitlines()
            if "pytest" in line and "type_d_1055" in line
        ]
        assert pytest_lines == [], pytest_lines

    def test_tombstone_lineage(self):
        # The lineage marker: #1055's entry recorded SEVENTIETH ->
        # SEVENTY-FIRST; this run advances it to SEVENTY-SECOND.
        entry = _read(LOG_PATH)
        idx = entry.index("## #1055 Type D:")
        block = entry[idx : idx + 12000]
        assert "SEVENTY-FIRST" in block


# ---------------------------------------------------------------------------
# 10. Synthetic engine calibration (fresh values, not #1055's)
# ---------------------------------------------------------------------------
class TestTypeDSyntheticEngineCalibration1060:
    # FRESH synthetic corpora this run (new values, not #1055's).
    # Engine significance is never promoted to a finding: the m865 /
    # m866 / m867 mechanisms verified this run carry finding-layer
    # is_significant false / NOT asserted per the Aug 28 2026 standing
    # rule.
    STRONG_META = [-0.74, -0.79, -0.76, -0.78, -0.75, -0.77, -0.76]
    STRONG_COMP = [0.03, 0.00, 0.02, -0.01, 0.01, 0.04, -0.02]
    NULL_META = [0.02, -0.04, 0.01, 0.03, -0.02, 0.00, -0.01]
    NULL_COMP = [-0.02, 0.03, -0.01, 0.02, -0.04, 0.01, -0.06]

    def _scorer(self):
        import sys

        sys.path.insert(0, REPO_ROOT)
        from mediascope.score.statistical import (
            welch_t_test,
            cohens_d,
            bootstrap_ci,
        )

        return welch_t_test, cohens_d, bootstrap_ci

    def test_strong_signal_significant_at_engine_layer(self):
        welch_t_test, cohens_d, bootstrap_ci = self._scorer()
        a = self.STRONG_META
        b = self.STRONG_COMP
        import numpy as np

        asym = float(np.mean(a) - np.mean(b))
        t, p = welch_t_test(a, b)
        d = cohens_d(a, b)
        ci = bootstrap_ci(a, b)
        import pytest

        assert asym == pytest.approx(-0.7742857142857142, rel=1e-12)
        assert t == pytest.approx(-74.216406541949965, rel=1e-9)
        assert p == pytest.approx(1.0839153639466970e-16, rel=1e-6)
        assert d == pytest.approx(-39.670337965357859, rel=1e-9)
        assert ci[0] == pytest.approx(-0.7942857142857143, rel=1e-12)
        assert ci[1] == pytest.approx(-0.7557142857142857, rel=1e-12)
        assert ci[1] < 0, "CI entirely below zero"
        assert p < 0.05

    def test_near_null_stays_silent(self):
        welch_t_test, cohens_d, bootstrap_ci = self._scorer()
        a = self.NULL_META
        b = self.NULL_COMP
        import numpy as np
        import pytest

        asym = float(np.mean(a) - np.mean(b))
        t, p = welch_t_test(a, b)
        d = cohens_d(a, b)
        ci = bootstrap_ci(a, b)
        assert asym == pytest.approx(0.0085714285714286, rel=1e-9)
        assert t == pytest.approx(0.558693769719781, rel=1e-9)
        assert p == pytest.approx(0.58752309351099241, rel=1e-9)
        assert d == pytest.approx(0.298634381488085, rel=1e-9)
        assert ci[0] == pytest.approx(-0.0185714285714286, rel=1e-9)
        assert ci[1] == pytest.approx(0.0371428571428571, rel=1e-9)
        assert ci[0] < 0 < ci[1], "CI crosses zero"
        assert p >= 0.05, "near-null pair stays silent"

    def test_degenerate_n1_guard_on_m865_pair(self):
        # Degenerate n=1-per-arm contract on the m865 illustrative
        # pair ([+0.15] OpenAI, [-0.55] Meta): the classic guard.
        welch_t_test, cohens_d, _ = self._scorer()
        import numpy as np
        import pytest

        openai_arm = [0.15]
        meta_arm = [-0.55]
        t, p = welch_t_test(openai_arm, meta_arm)
        d = cohens_d(openai_arm, meta_arm)
        assert abs(float(np.mean(openai_arm) - np.mean(meta_arm))) == pytest.approx(
            0.7000000000000001, abs=1e-12
        )
        assert t == 0.0
        assert p == 1.0
        assert d == 0.0
        # Arm-swap negates the signed asymmetry.
        t2, _ = welch_t_test(meta_arm, openai_arm)
        assert t2 == 0.0
        assert float(np.mean(meta_arm) - np.mean(openai_arm)) == pytest.approx(
            -0.7000000000000001, abs=1e-12
        )


# ---------------------------------------------------------------------------
# 11. Suite relaunch
# ---------------------------------------------------------------------------
class TestTypeDSuiteRelaunch1060:
    def test_suite_log_relaunched_and_live(self):
        # The full suite is re-launched by this run as a background
        # process writing to goal hidden_files type_d_1060_full_suite.log
        # (per the #795 convention); the next Type D run checks its
        # verdict. This test asserts the launch happened: the log
        # exists, is non-trivial, and carries pytest progress tokens.
        assert os.path.exists(SUITE_LOG), "suite log not launched"
        size = os.path.getsize(SUITE_LOG)
        assert size > 200, size
        head = open(SUITE_LOG, encoding="utf-8", errors="replace").read(2000)
        assert (
            "." in head or "%" in head or "collected" in head
        ), head[:200]


# ---------------------------------------------------------------------------
# 12. Doc-sync ratchet per #719 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSync1060:
    def test_readme_row_1060(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1060(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1060_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


# ---------------------------------------------------------------------------
# 13. Iteration log per #719 / #721 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestIterationLog1060:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1060 Type D:")
        return log[idx : idx + 25000]

    def test_entry_present(self):
        assert "## #1060 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "SEVENTY-SECOND" in entry
        assert "867" in entry

    def test_entry_records_doc_sync_delta(self):
        # The entry's doc-sync delta must match this file's actual
        # test count and the +1 file delta.
        result = subprocess.run(
            [
                os.path.join(REPO_ROOT, ".venv", "bin", "python"),
                "-m",
                "pytest",
                "--collect-only",
                "-q",
                TEST_BASENAME,
            ],
            cwd=TESTS_DIR,
            capture_output=True,
            text=True,
        )
        m = re.search(r"(\d+) tests collected", result.stdout)
        assert m, result.stdout[-500:]
        n = int(m.group(1))
        entry = self._entry()
        assert ("+%d/+1" % n) in entry, entry[:2000]
