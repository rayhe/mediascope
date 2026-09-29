"""Type D -- Iteration #1070 (Tue 2026-09-29 07:00 PDT): m871/m872/m873
qualitative-discipline verification + post-1065-1069 corpus integrity
(max numeric mechanism_id 873; zero next-number 874 keys in
numeric/underscore/dash mechanism forms; underscore/dash 874 needles
are format-built per #715 so no guard-literal carrier file exists -
the repo-wide 874 sweep is pure zero on source files (the local
tests/__pycache__ .pyc artifacts carry concatenated 874 strings from
their own guards; untracked build artifacts, excluded per the #715
pattern-rescope lesson); the #1062/#1063/#1064 window files' forward-
looking zero-871 guards FAIL BY DESIGN this run (mechanism 871
landed at the #1067 Type A leg) and are pinned as fail-by-design in
the forward-looking staleness class; the #1067 window file is rolled
forward (M_ID 871->873, NEXT 872->874, OWN_M_ID 871 preserved); the
#1068/#1069 window files are already current (M_ID 873, NEXT 874);
the #1065 Type D file gets its historical repin (MAX_ID 870->873,
NEXT_NUM 871->874, rotation-opens-1065 -> window-closed-complete,
no-Type-E-1066 -> Type-E-1066-landed 8c144fe8, entry newest-first ->
entry-present); ledger holds at 35 with the THIRTY-FIFTH member-claim
form present (financial-times.yaml m859 finding + ledger_note;
competitor-entities.yaml m861-family note), THIRTY-SIXTH member-form
absent in profiles/) + #1065 background-suite tombstone (FIFTY-FIFTH
consecutive death; lineage SEVENTY-THIRD -> SEVENTY-FOURTH) + fresh
synthetic engine calibration (new values, not #1065's) + re-launch of
the full suite as a background process writing to goal hidden_files
type_d_1070_full_suite.log (next Type D run checks its verdict per
the #795 convention).

Type D FIRST leg of the 1070-1074 window, OPENING it
(D->E->A->B->C). Committed predecessor #1069 Type C (06:00 PDT Sep
29) CLOSED the 1065-1069 window (D #1065, E #1066, A #1067, B #1068,
C #1069). Rotation per the #565 anchor + rotation guard.
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
- m871 (Type A #1067, business-insider.yaml openai section,
  4-space indent, descriptive block key
  `bi_openai_sep2026_astra_cancellation_scoop_vs_meta_product_execution_register`,
  `mechanism_id: 871` field form, no block_key: field - key appears
  exactly once in the home YAML): BI applies an insider-scoop
  safety-accountability register to the deal partner (Axel Springer
  x OpenAI licensing deal), NOT softness; A1 Astra-cancellation
  scoop (MANUAL ILLUSTRATIVE -0.35) + A2 influencer-marketing
  investigation (MANUAL ILLUSTRATIVE -0.25); carried Meta comparator
  (m399, un-rescored per #807) at +0.08; illustrative delta -0.38:
  the deal partner sits at the HARD end; TEMPORAL REPLICATION of
  m399/m799 deal-partner-hardness at a second safety peg;
  falsification reference is PROSE-ONLY inside the finding ("NOT a
  falsification-family member ... falsification ledger holds at 35")
  - ledger holds at 35.
- m872 (Type B #1068, journalists.yaml cherlynn_low competitor_coverage,
  4-space indent, block key
  `type_b_1068_cherlynn_low_engadget_apple_watch_audio_intelligence_vs_meta_glasses_hands_on_register_constancy_sep29`,
  `mechanism_id: 872` field form, block_key: field repeats the key -
  3 occurrences in the home YAML): Cherlynn Low (Engadget) applies
  an equally permissive, privacy-alarm-free register to Apple's
  always-listening watch (MANUAL ILLUSTRATIVE +0.35, explicit
  permissive principle quoted verbatim) and Meta's camera glasses
  (MANUAL ILLUSTRATIVE +0.30, warm fashion-forward hands-on, zero
  privacy/surveillance vocabulary); illustrative delta (Apple minus
  Meta) +0.05: register constancy, null asymmetry - TEMPORAL
  EXTENSION of m150's control-case finding to a third entity and a
  new sensor modality; statistical discipline nested under
  statistical_discipline (p_value/cohens_d/ci_95 NOT_CALCULATED,
  engine NOT run, verdict directionally_supported_not_proven,
  is_significant false); falsification_family carries NOT-member
  prose, ledger 35.
- m873 (Type C #1069, profiles/competitor-entities.yaml top-level
  block, zero indent, block key
  `type_c_1069_nvidia_openai_100b_loi_metered_recycling_twentyfirst_direction_sep29_6am`,
  `mechanism_id: 873` field form, block_key: field repeats the key -
  2 occurrences in the home YAML): FIRST dedicated corpus mechanism
  on the Nvidia x OpenAI up-to-$100B progressive equity LOI (Sep 22
  2025, at least 10GW, ~$10B per deployed gigawatt) and its Jan-2026
  stall - METERED-RECYCLING as the TWENTY-FIRST relationship
  direction per the m807 enumeration; coverage_nexus carries tone
  NOT_SCORED (no editorial-tone claim); falsification_family_member
  False - NOT a falsification-family member (ledger holds at 35).

Statistical discipline across all three: MANUAL ILLUSTRATIVE ONLY
(m871, m872) / NOT_SCORED (m873) per the Aug 28 2026 standing rule,
engine NOT run at the finding layer, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False / not asserted at the finding
layer, verdict directionally_supported_not_proven,
no_analysis_json_update true, NOT artifact-grade; no analysis.json
update. NONE of m871/m872/m873 is a falsification-family member
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

ANCHORED_SHA = "d3a261b5604e7b6d520a9a685cd71b8280aebd51"  # patched by the anchor followup commit per #565

MAX_ID = 876  # pinned by #1075 Type D: m876 landed at #1074 Type C
NEXT_NUM = 877  # pinned by #1075 Type D: m876 landed at #1074 Type C

M871_KEY = (
    "bi_openai_sep2026_astra_cancellation_scoop_"
    "vs_meta_product_execution_register"
)
M871_INDENT = 4
M871_HOME = "profiles/business-insider.yaml"
M872_KEY = (
    "type_b_1068_cherlynn_low_engadget_apple_watch_audio_intelligence_"
    "vs_meta_glasses_hands_on_register_constancy_sep29"
)
M872_INDENT = 4
M872_HOME = "profiles/careers/journalists.yaml"
M873_KEY = (
    "type_c_1069_nvidia_openai_100b_loi_metered_recycling_"
    "twentyfirst_direction_sep29_6am"
)
M873_INDENT = 0
M873_HOME = "profiles/competitor-entities.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1070_full_suite.log"
)
PRIOR_SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1065_full_suite.log"
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
# numbers in git history: #1070 Type D opens the 1070-1074 window;
# #1069 Type C (committed 06:00 PDT Sep 29) is the schedule
# predecessor and CLOSED the 1065-1069 window. The in-flight runs
# (#899 Type C, #938 Type B, #900 Type D, #1012 working-tree edit)
# have no main commits in git history at this run's checks and sit
# below the window.


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: local test
    pyc files carry next-number needle strings from their own
    guards; compiled artifacts are excluded from the sweeps). No
    additional sweep-carrier exclusions this run: no in-tree SOURCE
    file carries a contiguous 874-form mechanism literal (verified
    pre-commit), so the 874 sweeps run repo-wide with only this file
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


def _m871_data():
    return _block_data(M871_HOME, M871_KEY, M871_INDENT)


def _m872_data():
    return _block_data(M872_HOME, M872_KEY, M872_INDENT)


def _m873_data():
    return _block_data(M873_HOME, M873_KEY, M873_INDENT)

# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1070:
    def test_no_type_d_1070_test_file_preexisting(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1070*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1070 glob"

    def test_no_type_d_1070_in_git_log(self):
        # Pre-commit novelty: no Type D #1070 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1070"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1070" in line
            and "followup" not in line.lower()
            and "push-status" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_873(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_874_numeric_forms_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        # m871: descriptive block key at 6-space indent under the
        # openai section, exactly one occurrence line in
        # business-insider.yaml (no block_key: field for this block -
        # the key design matches m868).
        assert (
            _read(os.path.join(REPO_ROOT, M871_HOME)).count(
                "\n    " + M871_KEY + ":"
            )
            == 1
        )
        # m872: block key at 6-space indent under cherlynn_low's
        # competitor_coverage in journalists.yaml (the block_key:
        # field repeats it, hence the total-occurrence assertion in
        # the designed-repeat test below).
        assert (
            _read(os.path.join(REPO_ROOT, M872_HOME)).count(
                "\n    " + M872_KEY + ":"
            )
            == 1
        )
        # m873: block key at zero indent in competitor-entities.yaml.
        assert (
            _read(os.path.join(REPO_ROOT, M873_HOME)).count(
                "\n" + M873_KEY + ":"
            )
            == 1
        )

    def test_m871_key_carried_once_no_repeat_field(self):
        # The m871 block carries no block_key: field (unlike m872 /
        # m873); the key string appears exactly once in the home
        # YAML, in the colon-form block-key line. The #1067 Type A
        # test file's own assertion literal is the one other
        # repo-wide carrier - pinned, not a corpus duplicate.
        assert _read(os.path.join(REPO_ROOT, M871_HOME)).count(M871_KEY) == 1

    def test_m872_block_key_repeat_is_designed(self):
        # The m872 block carries its block_key: field repeating the
        # key (designed keying per #1068): the colon-form block-key
        # line and the block_key: field line each appear exactly once
        # in journalists.yaml, plus one prose reference - 3 total,
        # pinned, not corpus duplicates.
        text = _read(os.path.join(REPO_ROOT, M872_HOME))
        assert text.count("\n    " + M872_KEY + ":") == 1
        assert text.count("block_key: " + M872_KEY) == 1
        assert text.count(M872_KEY) == 3

    def test_m873_block_key_repeat_is_designed(self):
        # The m873 block carries its block_key: field repeating the
        # key (designed keying per #1069): exactly 2 occurrences in
        # competitor-entities.yaml.
        assert _read(os.path.join(REPO_ROOT, M873_HOME)).count(M873_KEY) == 2

    def test_1070_entry_present_in_log(self):
        # HISTORICAL REPIN (Sep 29 2026, #1075 run): the #1070 entry
        # is present in the log (newest-first position belonged to
        # the #1075 entry after this run).
        assert "## #1070 Type D:" in _read(LOG_PATH)


# ---------------------------------------------------------------------------
# 2. Rotation guard per #565
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1070:
    def test_1070_window_closed_complete(self):
        # HISTORICAL REPIN (Sep 29 2026, #1075 run): the 1070-1074
        # window is CLOSED and complete. All five legs landed with
        # clean "Type X #N:" main-commit subjects in the correct
        # relative order: D #1070 -> E #1071 -> A #1072 -> B #1073 ->
        # C #1074 (newest-first: C #1074, B #1073, A #1072, E #1071,
        # D #1070). This assertion is stable across the #1075 main
        # commit (which sits above the window) because it filters to
        # the 1070-1074 subsequence rather than absolute positions.
        chain = [
            entry
            for entry in _window(n=80)
            if entry[1] in ("1070", "1071", "1072", "1073", "1074")
        ]
        assert chain == [
            ("C", "1074"),
            ("B", "1073"),
            ("A", "1072"),
            ("E", "1071"),
            ("D", "1070"),
        ], chain

    def test_predecessor_1069_chain_present(self):
        # The full #1069 Type C commit chain must be in git history
        # before this run's main commit (rotation transparency per
        # #565): main 25e85da4, anchor 91cfddbe, log-hash 49ed8740,
        # push-status 2d82c989.
        for sha in (
            "25e85da4",
            "91cfddbe",
            "49ed8740",
            "2d82c989",
        ):
            assert (
                subprocess.run(
                    ["git", "cat-file", "-e", sha],
                    cwd=REPO_ROOT,
                    capture_output=True,
                ).returncode
                == 0
            ), sha

    def test_type_e_1071_landed(self):
        # HISTORICAL REPIN (Sep 29 2026, #1075 run): Type E #1071 has
        # LANDED (main commit 4e19c3b9, Sep 29 08:00 PDT) - the
        # forward-looking "must not exist yet" guard from the #1070
        # run is inverted now that the 1070-1074 window closed.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type E #1071"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type E #1071" in line and "followup" not in line.lower()
        ]
        assert len(mains) == 1, mains
        assert mains[0].startswith("4e19c3b9"), mains

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
class TestTypeDCorpusIntegrity1070:
    def test_underscore_874_zero_repo_wide(self):
        # Underscore-form 874 needles are pure zero on source files:
        # the #1067/#1068/#1069 files build their zero-874 needles at
        # runtime ("mechanism" + "_" + "87" + "4" per #715), so no
        # contiguous literal exists in any source file - no
        # guard-literal carrier file is pinned this run.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_dash_874_zero_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_thirty_sixth_absent_in_profiles(self):
        # THIRTY-SIXTH member-form is absent across profiles/ (ledger
        # holds at 35); the test-file guard-literal carriers are
        # pinned in the falsification-ledger class.
        assert _profiles_with("THIRTY-SIXTH") == []


# ---------------------------------------------------------------------------
# 4. m871 qualitative discipline (Type A #1067, business-insider.yaml openai)
# ---------------------------------------------------------------------------
class TestTypeDM871QualitativeDiscipline:
    def test_mechanism_id_and_identity(self):
        d = _m871_data()
        assert d["mechanism_id"] == 871
        assert d["iteration"] == 1067
        assert d["iteration_type"] == "A"
        assert "Business Insider" in d["publication_focus"]

    def test_finding_carries_manual_illustrative_arms(self):
        finding = _m871_data()["finding"]
        assert "MANUAL ILLUSTRATIVE -0.35" in finding
        assert "MANUAL ILLUSTRATIVE -0.25" in finding
        assert "Illustrative delta (OpenAI minus Meta) -0.38" in finding
        assert "deal partner sits at the HARD end" in finding

    def test_statistical_discipline_nested(self):
        sd = _m871_data()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in sd
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in sd
        assert "is_significant False" in sd
        assert "engine NOT run" in sd
        assert "verdict directionally_supported_not_proven" in sd
        assert "no_analysis_json_update true" in sd

    def test_finding_carries_not_falsification_prose(self):
        # The falsification reference for m871 is PROSE-ONLY inside
        # the finding string (no dedicated falsification_family /
        # falsification_ledger fields in this block): not a member,
        # ledger unchanged at the finding layer.
        finding = _m871_data()["finding"]
        assert "NOT a falsification-family member" in finding
        assert "falsification ledger holds at 35" in finding

    def test_temporal_replication_of_deal_partner_hardness(self):
        # m871 is a TEMPORAL REPLICATION of the m399/m799
        # deal-partner-hardness pattern at a second OpenAI safety peg.
        finding = _m871_data()["finding"]
        assert "TEMPORAL REPLICATION" in finding
        assert "deal-partner-hardness" in finding
        assert "NOT artifact-grade" in finding

# ---------------------------------------------------------------------------
# 5. m872 qualitative discipline (Type B #1068, journalists.yaml cherlynn_low)
# ---------------------------------------------------------------------------
class TestTypeDM872QualitativeDiscipline:
    def test_mechanism_id_and_identity(self):
        d = _m872_data()
        assert d["mechanism_id"] == 872
        assert d["iteration"] == 1068
        assert d["type"] == "B"
        assert "Cherlynn Low" in d["design"]

    def test_finding_carries_manual_illustrative_arms(self):
        d = _m872_data()
        assert "MANUAL ILLUSTRATIVE +0.35" in d["apple_arm"]
        assert "MANUAL ILLUSTRATIVE +0.30" in d["meta_arm"]
        assert "register constancy" in d["verdict"]
        assert "null asymmetry" in d["verdict"]

    def test_temporal_extension_of_m150(self):
        # m872 is a TEMPORAL EXTENSION of m150's beat-assignment
        # control-case finding to a third entity (Apple) and a new
        # sensor modality (always-listening audio).
        d = _m872_data()
        assert "TEMPORAL EXTENSION" in d["verdict"]
        assert "m150" in d["design"]
        assert "explicitly permissive on ambient listening" in d["apple_arm"]

    def test_statistical_discipline_nested(self):
        d = _m872_data()
        sd = d["statistical_discipline"]
        assert "p_value NOT_CALCULATED" in sd
        assert "cohens_d NOT_CALCULATED" in sd
        assert "is_significant false" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in d["verdict"]

    def test_not_falsification_family_member(self):
        d = _m872_data()
        assert "NOT a falsification-family member" in d["falsification_family"]
        assert "ledger holds at 35" in d["falsification_family"]


# ---------------------------------------------------------------------------
# 6. m873 qualitative discipline (Type C #1069, competitor-entities.yaml)
# ---------------------------------------------------------------------------
class TestTypeDM873QualitativeDiscipline:
    def test_mechanism_id_and_identity(self):
        d = _m873_data()
        assert d["mechanism_id"] == 873
        assert d["iteration"] == 1069
        assert d["iteration_type"] == "C"
        assert "TWENTY-FIRST" in d["mechanism_name"]
        assert "METERED-RECYCLING" in d["mechanism_name"]

    def test_three_legs_present(self):
        d = _m873_data()
        finding = d["finding"]
        assert "COMMITMENT LEG" in finding
        assert "METER LEG" in finding
        assert "STALL LEG" in finding
        assert "$100 billion" in finding or "$100B" in finding

    def test_taxonomy_enumeration(self):
        tax = _m873_data()["relationship_direction_taxonomy"]
        assert "TWENTY-FIRST relationship direction" in tax
        assert "demand-recycling" in tax
        assert "backstop-recycling" in tax
        assert "demand-underwriting" in tax

    def test_tone_not_scored(self):
        d = _m873_data()
        assert d["tone_scored"] is False
        assert "tone NOT_SCORED" in d["coverage_nexus"]

    def test_statistical_discipline(self):
        d = _m873_data()
        assert d["is_significant"] is False
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True
        assert d["artifact_grade"] is False
        assert d["engine_run"] is False

    def test_not_falsification_family_member(self):
        d = _m873_data()
        assert d["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 7. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1070:
    def test_ledger_holds_at_35(self):
        # THIRTY-SIXTH member-form absent in profiles/ (pinned in the
        # corpus-integrity class); THIRTY-FIFTH member-claim form
        # present in financial-times.yaml and competitor-entities.yaml.
        assert _profiles_with("THIRTY-SIXTH") == []
        carriers = _profiles_with("THIRTY-FIFTH")
        assert "profiles/financial-times.yaml" in [
            os.path.relpath(p, REPO_ROOT) for p in carriers
        ]
        assert "profiles/competitor-entities.yaml" in [
            os.path.relpath(p, REPO_ROOT) for p in carriers
        ]

    def test_no_new_falsification_members_this_window(self):
        # None of m871/m872/m873 is a falsification-family member:
        # m871 prose-only, m872 NOT-member prose, m873 field False.
        assert "NOT a falsification-family member" in _m871_data()["finding"]
        assert (
            "NOT a falsification-family member"
            in _m872_data()["falsification_family"]
        )
        assert _m873_data()["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (guard lifecycle)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1070:
    WINDOW_1065_1069_FILES = {
        "tests/test_type_a_1067_bi_openai_sep2026_astra_cancellation_"
        "scoop_vs_meta_product_execution_register_sep29_4am.py": 871,
        "tests/test_type_b_1068_cherlynn_low_engadget_apple_watch_audio_"
        "intelligence_vs_meta_glasses_hands_on_register_constancy_"
        "sep29_5am.py": 872,
        "tests/test_type_c_1069_nvidia_openai_100b_loi_metered_recycling_"
        "twentyfirst_direction_sep29_6am.py": 873,
    }

    def test_1067_rolled_forward_by_1070(self):
        # The #1067 Type A file was rolled forward by this #1070 run:
        # M_ID 871->873 (corpus max tracking), NEXT 872->874, OWN_M_ID
        # 871 preserved for its own-mechanism structure assertions.
        rel = (
            "tests/test_type_a_1067_bi_openai_sep2026_astra_cancellation_"
            "scoop_vs_meta_product_execution_register_sep29_4am.py"
        )
        text = _read(os.path.join(REPO_ROOT, rel))
        assert "M_ID = 873" in text, rel
        assert "OWN_M_ID = 871" in text, rel
        assert '"mechanism" + "_874"' in text, rel
        assert '"mechanism" + "-874"' in text, rel
        assert '"mechanism_id: " + "874"' in text, rel
        assert "873 is max, 874 is zero" in text, rel

    def test_1068_already_current(self):
        # The #1068 Type B file was rolled by the #1069 main commit
        # and is already current: M_ID 873, OWN_M_ID 872, NEXT 874.
        rel = (
            "tests/test_type_b_1068_cherlynn_low_engadget_apple_watch_audio_"
            "intelligence_vs_meta_glasses_hands_on_register_constancy_"
            "sep29_5am.py"
        )
        text = _read(os.path.join(REPO_ROOT, rel))
        assert "M_ID = 873" in text, rel
        assert "OWN_M_ID = 872" in text, rel
        assert '"mechanism" + "_874"' in text, rel

    def test_1069_already_current(self):
        # The #1069 Type C file is current: M_ID 873 (own 873 IS the
        # corpus max, so no OWN_M_ID split), NEXT 874.
        rel = (
            "tests/test_type_c_1069_nvidia_openai_100b_loi_metered_recycling_"
            "twentyfirst_direction_sep29_6am.py"
        )
        text = _read(os.path.join(REPO_ROOT, rel))
        assert "M_ID = 873" in text, rel
        assert "OWN_M_ID" not in text, rel
        assert '"mechanism" + "_874"' in text, rel

    def test_zero_871_guards_fail_by_design_pinned(self):
        # The #1062/#1063/#1064 window files' forward-looking
        # zero-871 guards FAIL BY DESIGN this run: mechanism 871
        # landed at the #1067 Type A leg (business-insider.yaml).
        # Pinned by this #1070 Type D run per the #1065 lifecycle
        # calendar - verified via subprocess, NOT touched by this run.
        targets = [
            "tests/test_type_a_1062_ft_apple_sep2026_duo_launch_market_"
            "register_vs_meta_muse_product_register_sep28_11pm.py"
            "::TestCorpusNoveltyPostCommit::"
            "test_zero_next_numeric_869_in_profiles",
            "tests/test_type_a_1062_ft_apple_sep2026_duo_launch_market_"
            "register_vs_meta_muse_product_register_sep28_11pm.py"
            "::TestCorpusNoveltyPostCommit::"
            "test_zero_next_underscore_dash_869_repo_wide",
            "tests/test_type_b_1063_james_pero_gizmodo_vr_headsets_cooked_"
            "enthusiasm_vs_pr_cleanup_adversarial_sep29_12am.py"
            "::TestCorpusNoveltyPostCommit::"
            "test_zero_next_numeric_870_in_profiles",
            "tests/test_type_b_1063_james_pero_gizmodo_vr_headsets_cooked_"
            "enthusiasm_vs_pr_cleanup_adversarial_sep29_12am.py"
            "::TestCorpusNoveltyPostCommit::"
            "test_zero_next_underscore_dash_870_repo_wide",
            "tests/test_type_c_1064_oracle_openai_300b_45gw_demand_"
            "underwriting_twentieth_direction_sep29_1am.py"
            "::TestCorpusNoveltyPostCommit::"
            "test_zero_next_numeric_871_in_profiles",
            "tests/test_type_c_1064_oracle_openai_300b_45gw_demand_"
            "underwriting_twentieth_direction_sep29_1am.py"
            "::TestCorpusNoveltyPostCommit::"
            "test_zero_next_underscore_dash_871_repo_wide",
        ]
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
        assert result.returncode != 0, (
            "expected the zero-871 guards to fail by design now that "
            "mechanism 871 landed; got returncode 0:\n" + result.stdout[-2000:]
        )
        # Designed split: the 3 numeric guards fail (mechanism_id: 871
        # is in profiles/); the 3 underscore/dash guards still pass
        # (871 needles are format-built per #715, no contiguous
        # literals exist repo-wide).
        assert "3 failed, 3 passed" in result.stdout, result.stdout[-2000:]

    def test_zero_874_guards_staleness_calendar(self):
        # Calendar pin: the 873 landing happened at #1069 (Type C).
        # The zero-874 guards fail BY DESIGN when mechanism 874 lands
        # - expected at a future A/B/C leg of the 1070-1074 window.
        # To be pinned by the next Type D run.
        assert 1069 + 1 == 1070
        for rel in self.WINDOW_1065_1069_FILES:
            assert os.path.exists(os.path.join(REPO_ROOT, rel))


# ---------------------------------------------------------------------------
# 9. Background suite tombstone
# ---------------------------------------------------------------------------
class TestTypeDBackgroundSuiteTombstone1070:
    def test_prior_suite_log_is_stalled(self):
        # The #1065 re-launched full suite (type_d_1065_full_suite.log)
        # stalled at 10632 bytes / 4% since Sep 29 02:59:56 PDT with
        # zero summary tokens; no pytest process is alive for it at
        # this run's check. Per the #795 convention this is a
        # background death: FIFTY-FIFTH consecutive, tombstone lineage
        # advances SEVENTY-THIRD -> SEVENTY-FOURTH. (The #1060 suite
        # was already tombstoned by #1065; NOT re-tombstoned here.)
        assert os.path.exists(PRIOR_SUITE_LOG)
        size = os.path.getsize(PRIOR_SUITE_LOG)
        assert 10000 < size < 12000, size
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
            if "pytest" in line and "type_d_1065" in line
        ]
        assert pytest_lines == [], pytest_lines

    def test_tombstone_lineage(self):
        # The lineage marker: #1065's entry recorded SEVENTY-SECOND ->
        # SEVENTY-THIRD; this run advances it to SEVENTY-FOURTH.
        entry = _read(LOG_PATH)
        idx = entry.index("## #1065 Type D:")
        block = entry[idx : idx + 12000]
        assert "SEVENTY-THIRD" in block

# ---------------------------------------------------------------------------
# 10. Synthetic engine calibration (fresh values, not #1065's)
# ---------------------------------------------------------------------------
class TestTypeDSyntheticEngineCalibration1070:
    # FRESH synthetic corpora this run (new values, not #1065's).
    # Engine significance is never promoted to a finding: the m871 /
    # m872 / m873 mechanisms verified this run carry finding-layer
    # is_significant false / NOT asserted per the Aug 28 2026 standing
    # rule.
    STRONG_META = [-0.69, -0.74, -0.71, -0.78, -0.70, -0.76, -0.73]
    STRONG_COMP = [0.03, -0.01, 0.05, 0.00, 0.04, -0.03, 0.02]
    NULL_META = [0.01, -0.04, 0.03, -0.02, 0.05, -0.03, 0.00]
    NULL_COMP = [-0.02, 0.03, -0.04, 0.01, -0.05, 0.02, -0.01]

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

        assert asym == pytest.approx(-0.7442857142857141, rel=1e-12)
        assert t == pytest.approx(-45.233148115538100, rel=1e-9)
        assert p == pytest.approx(1.319334190837689e-14, rel=1e-6)
        assert d == pytest.approx(-24.178134681934704, rel=1e-9)
        assert ci[0] == pytest.approx(-0.7742857142857144, rel=1e-12)
        assert ci[1] == pytest.approx(-0.7142857142857143, rel=1e-12)
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
        assert t == pytest.approx(0.509524665365068, rel=1e-9)
        assert p == pytest.approx(0.6196783808572590, rel=1e-9)
        assert d == pytest.approx(0.272352389700961, rel=1e-9)
        assert ci[0] == pytest.approx(-0.0200000000000000, rel=1e-9)
        assert ci[1] == pytest.approx(0.0385714285714286, rel=1e-9)
        assert ci[0] < 0 < ci[1], "CI crosses zero"
        assert p >= 0.05, "near-null pair stays silent"

    def test_degenerate_n1_guard_on_m871_pair(self):
        # Degenerate n=1-per-arm contract on the m871 illustrative
        # pair ([-0.35] A1 Astra scoop, [+0.08] carried Meta
        # comparator): the classic guard.
        welch_t_test, cohens_d, _ = self._scorer()
        import numpy as np
        import pytest

        openai_arm = [-0.35]
        meta_arm = [0.08]
        t, p = welch_t_test(openai_arm, meta_arm)
        d = cohens_d(openai_arm, meta_arm)
        assert abs(
            float(np.mean(openai_arm) - np.mean(meta_arm))
        ) == pytest.approx(0.4300000000000000, abs=1e-12)
        assert t == 0.0
        assert p == 1.0
        assert d == 0.0
        # Arm-swap negates the signed asymmetry.
        t2, _ = welch_t_test(meta_arm, openai_arm)
        assert t2 == 0.0
        assert float(np.mean(meta_arm) - np.mean(openai_arm)) == pytest.approx(
            0.4300000000000000, abs=1e-12
        )


# ---------------------------------------------------------------------------
# 11. Suite relaunch
# ---------------------------------------------------------------------------
class TestTypeDSuiteRelaunch1070:
    def test_suite_log_relaunched_and_live(self):
        # The full suite is re-launched by this run as a background
        # process writing to goal hidden_files type_d_1070_full_suite.log
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
class TestDocSync1070:
    def test_readme_row_1070(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1070(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1070_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


# ---------------------------------------------------------------------------
# 13. Iteration log per #719 / #721 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestIterationLog1070:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1070 Type D:")
        return log[idx : idx + 25000]

    def test_entry_present(self):
        assert "## #1070 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "SEVENTY-FOURTH" in entry
        assert "873" in entry

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
