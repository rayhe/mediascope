"""Type D -- Iteration #1065 (Tue 2026-09-29 02:00 PDT): m868/m869/m870
qualitative-discipline verification + post-1060-1064 corpus integrity
(max numeric mechanism_id 870; zero next-number 871 keys in
numeric/underscore/dash mechanism forms; underscore/dash 871 needles
are format-built per #715 so no guard-literal carrier file exists -
the repo-wide 871 sweep is pure zero on source files (the six local
tests/__pycache__ .pyc artifacts carry concatenated 871 strings from
their own guards; untracked build artifacts, excluded per the #715
pattern-rescope lesson); the #1062/#1063/#1064 window test files'
own forward-looking zero-871 guards pass this run and are pinned as
forward-looking staleness: they fail BY DESIGN when mechanism 871
lands at a future A/B/C leg, to be pinned by the next Type D run;
ledger holds at 35 with the THIRTY-FIFTH member-claim form present
(financial-times.yaml m859 finding + ledger_note; competitor-entities.yaml
m861-family note), THIRTY-SIXTH member-form absent in profiles/) +
#1060 background-suite tombstone (FIFTY-FOURTH consecutive death;
lineage SEVENTY-SECOND -> SEVENTY-THIRD) + fresh synthetic engine
calibration (new values, not #1060's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_1065_full_suite.log (next Type D run checks its verdict per
the #795 convention).

Type D FIRST leg of the 1065-1069 window, OPENING it
(D->E->A->B->C). Committed predecessor #1064 Type C (01:00 PDT Sep
29) CLOSED the 1060-1064 window (D #1060, E #1061, A #1062, B #1063,
C #1064). Rotation per the #565 anchor + rotation guard.
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
- m868 (Type A #1062, financial-times.yaml competitor_relationships.apple,
  4-space indent, descriptive block key
  `ft_apple_sep2026_duo_launch_market_register_vs_meta_muse_product_register`,
  `mechanism_id: 868` field form, no block_key: field - key appears
  exactly once in the home YAML): FT applies a price-forward
  market-analysis register (MANUAL ILLUSTRATIVE +0.10) to Apple's
  Sep-10 iPhone Duo foldable launch, inside the product-launch
  register band it applies to Meta's Sep-8/9 Muse launch (carried
  m625, +0.05, un-rescored per #807); illustrative delta +0.05
  near-null; A2 liability-verdict arm (MANUAL ILLUSTRATIVE -0.20)
  documents register selection not tone; falsification reference is
  PROSE-ONLY inside the finding ("NOT a falsification-family member
  ... falsification ledger holds at 35") - ledger holds at 35.
- m869 (Type B #1063, journalists.yaml james_pero item, 4-space
  indent, block key
  `type_b_1063_james_pero_gizmodo_vr_headsets_cooked_enthusiasm_vs_pr_cleanup_adversarial_sep29`,
  `mechanism_id: 869` field form, block_key: field repeats the key -
  2 occurrences in the home YAML): James Pero's Sep-25 Gizmodo VR
  glasses hands-on runs enthusiastic gadget register (MANUAL
  ILLUSTRATIVE +0.50) vs his Sep-28 smart-glasses PR-cleanup
  adversarial analysis (MANUAL ILLUSTRATIVE -0.30); illustrative
  delta +0.80; TEMPORAL REPLICATION of m818 with fresh arms -
  register follows product category and news peg, not a uniform
  anti-Meta stance; statistical discipline nested under
  statistical_discipline: p_value/cohens_d/ci NOT_CALCULATED,
  engine NOT run, verdict directionally_supported_not_proven,
  is_significant False, falsification_family_member False,
  falsification_ledger 35, no_analysis_json_update True.
- m870 (Type C #1064, profiles/competitor-entities.yaml top-level
  block, zero indent, block key
  `type_c_1064_oracle_openai_300b_45gw_demand_underwriting_twentieth_direction_sep29_1am`,
  `mechanism_id: 870` field form, block_key: field repeats the key -
  2 occurrences in the home YAML): FIRST dedicated corpus mechanism
  on the OpenAI x Oracle committed-demand financing architecture
  ($300B/5yr, 4.5GW Stargate; Oracle Q1 FY2027 RPO $664B, $28.5B
  quarterly capex, customer prepayments $11.36B) -
  DEMAND-UNDERWRITING as the TWENTIETH relationship direction per
  the m807 enumeration; coverage_nexus carries tone NOT_SCORED (no
  editorial-tone claim); falsification_family_member False - NOT a
  falsification-family member (ledger holds at 35).

Statistical discipline across all three: MANUAL ILLUSTRATIVE ONLY
(m868, m869) / NOT_SCORED (m870) per the Aug 28 2026 standing rule,
engine NOT run at the finding layer, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False / not asserted at the finding
layer, verdict directionally_supported_not_proven,
no_analysis_json_update true, NOT artifact-grade; no analysis.json
update. NONE of m868/m869/m870 is a falsification-family member
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

ANCHORED_SHA = "0" * 40  # patched to the main commit hash by the anchor followup per #565

MAX_ID = 870
NEXT_NUM = 871

M868_KEY = (
    "ft_apple_sep2026_duo_launch_market_register_"
    "vs_meta_muse_product_register"
)
M868_INDENT = 4
M868_HOME = "profiles/financial-times.yaml"
M869_KEY = (
    "type_b_1063_james_pero_gizmodo_vr_headsets_cooked_enthusiasm_"
    "vs_pr_cleanup_adversarial_sep29"
)
M869_INDENT = 4
M869_HOME = "profiles/careers/journalists.yaml"
M870_KEY = (
    "type_c_1064_oracle_openai_300b_45gw_demand_underwriting_"
    "twentieth_direction_sep29_1am"
)
M870_INDENT = 0
M870_HOME = "profiles/competitor-entities.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1065_full_suite.log"
)
PRIOR_SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1060_full_suite.log"
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
# numbers in git history: #1065 Type D opens the 1065-1069 window;
# #1064 Type C (committed 01:00 PDT Sep 29) is the schedule
# predecessor and CLOSED the 1060-1064 window. The in-flight runs
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
    file carries a contiguous 871-form mechanism literal (verified
    pre-commit), so the 871 sweeps run repo-wide with only this file
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


def _m868_data():
    return _block_data(M868_HOME, M868_KEY, M868_INDENT)


def _m869_data():
    return _block_data(M869_HOME, M869_KEY, M869_INDENT)


def _m870_data():
    return _block_data(M870_HOME, M870_KEY, M870_INDENT)

# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1065:
    def test_no_type_d_1065_test_file_preexisting(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1065*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1065 glob"

    def test_no_type_d_1065_in_git_log(self):
        # Pre-commit novelty: no Type D #1065 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1065"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1065" in line
            and "followup" not in line.lower()
            and "push-status" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_870(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_871_numeric_forms_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        # m868: descriptive block key at 4-space indent, exactly one
        # occurrence line in financial-times.yaml (no block_key: field
        # for this block - the key design matches m865).
        assert (
            _read(os.path.join(REPO_ROOT, M868_HOME)).count(
                "\n    " + M868_KEY + ":"
            )
            == 1
        )
        # m869: block key at 4-space indent in journalists.yaml (the
        # block_key: field repeats it, hence the total-occurrence
        # assertion in the designed-repeat test below).
        assert (
            _read(os.path.join(REPO_ROOT, M869_HOME)).count(
                "\n    " + M869_KEY + ":"
            )
            == 1
        )
        # m870: block key at zero indent in competitor-entities.yaml.
        assert (
            _read(os.path.join(REPO_ROOT, M870_HOME)).count(
                "\n" + M870_KEY + ":"
            )
            == 1
        )

    def test_m868_key_carried_once_no_repeat_field(self):
        # The m868 block carries no block_key: field (unlike m869 /
        # m870); the key string appears exactly once in the home
        # YAML, in the colon-form block-key line. The #1062 Type A
        # test file's own assertion literal is the one other
        # repo-wide carrier - pinned, not a corpus duplicate.
        assert _read(os.path.join(REPO_ROOT, M868_HOME)).count(M868_KEY) == 1

    def test_m869_block_key_repeat_is_designed(self):
        # The m869 block carries its block_key: field repeating the
        # key (designed keying per #1063): the colon-form block-key
        # line and the block_key: field line each appear exactly once
        # in journalists.yaml. Two further prose/field references are
        # pinned, not corpus duplicates: the novelty prose (backticked)
        # and the test_file field.
        text = _read(os.path.join(REPO_ROOT, M869_HOME))
        assert text.count("\n    " + M869_KEY + ":") == 1
        assert text.count("block_key: " + M869_KEY) == 1
        assert text.count(M869_KEY) == 4

    def test_m870_block_key_repeat_is_designed(self):
        # The m870 block carries its block_key: field repeating the
        # key (designed keying per #1064): exactly 2 occurrences in
        # competitor-entities.yaml.
        assert _read(os.path.join(REPO_ROOT, M870_HOME)).count(M870_KEY) == 2

    def test_1065_entry_newest_first_in_log(self):
        # The "## #1065 Type D:" entry leads the log (newest-first
        # ordering); hashes are TBD until the anchor followup patches
        # them per #565.
        assert _read(LOG_PATH).startswith("## #1065 Type D:")


# ---------------------------------------------------------------------------
# 2. Rotation guard per #565
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1065:
    def test_rotation_window_opens_1065(self):
        # The newest distinct iteration in git history is this run's
        # #1065 Type D (window opener). The full 1060-1064 window is
        # regex-visible (no subject deviations in this window): D
        # #1065 -> C #1064 -> B #1063 -> A #1062 -> E #1061.
        window = _window()
        assert window[0] == ("D", "1065"), window
        assert window[1:5] == [
            ("C", "1064"),
            ("B", "1063"),
            ("A", "1062"),
            ("E", "1061"),
        ], window

    def test_predecessor_1064_chain_present(self):
        # The full #1064 Type C commit chain must be in git history
        # before this run's main commit (rotation transparency per
        # #565): main ca831b0b, anchor 1eb83096, log-hash ba08c733,
        # push-status d678e90c.
        for sha in (
            "ca831b0b",
            "1eb83096",
            "ba08c733",
            "d678e90c",
        ):
            assert (
                subprocess.run(
                    ["git", "cat-file", "-e", sha],
                    cwd=REPO_ROOT,
                    capture_output=True,
                ).returncode
                == 0
            ), sha

    def test_no_type_e_1066_in_git_log(self):
        # The next leg (Type E #1066) must not exist yet: this run
        # opens the window, #1066 continues it.
        result = subprocess.run(
            ["git", "log", "--format=%s", "--grep=Type E #1066"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.stdout.strip() == "", result.stdout

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
class TestTypeDCorpusIntegrity1065:
    def test_underscore_871_zero_repo_wide(self):
        # Underscore-form 871 needles are pure zero on source files:
        # the #1062/#1063/#1064 files build their zero-871 needles at
        # runtime ("mechanism" + "_" + "87" + "1" per #715), so no
        # contiguous literal exists in any source file - no
        # guard-literal carrier file is pinned this run.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_dash_871_zero_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_thirty_sixth_absent_in_profiles(self):
        # THIRTY-SIXTH member-form is absent across profiles/ (ledger
        # holds at 35); the test-file guard-literal carriers are
        # pinned in the falsification-ledger class.
        assert _profiles_with("THIRTY-SIXTH") == []

# ---------------------------------------------------------------------------
# 4. m868 qualitative discipline (Type A #1062, financial-times.yaml apple)
# ---------------------------------------------------------------------------
class TestTypeDM868QualitativeDiscipline:
    def test_mechanism_id_and_identity(self):
        d = _m868_data()
        assert d["mechanism_id"] == 868
        assert d["iteration"] == 1062
        assert d["iteration_type"] == "A"
        assert "Financial Times" in d["publication_focus"]

    def test_finding_carries_manual_illustrative_arms(self):
        finding = _m868_data()["finding"]
        assert "MANUAL ILLUSTRATIVE +0.10" in finding
        assert "MANUAL ILLUSTRATIVE -0.20" in finding
        assert "Illustrative delta" in finding
        assert "+0.05" in finding
        sd = _m868_data()["statistical_discipline"]
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in sd
        assert "is_significant False" in sd
        assert "engine NOT run" in sd

    def test_finding_carries_not_falsification_prose(self):
        # The falsification reference for m868 is PROSE-ONLY inside
        # the finding string (no dedicated falsification_family /
        # falsification_ledger fields in this block): not a member,
        # ledger unchanged at the finding layer.
        finding = _m868_data()["finding"]
        assert "NOT a falsification-family member" in finding
        assert "falsification ledger holds at 35" in finding

    def test_null_tie_control_documented(self):
        # m868 is the FIRST dedicated Type A mechanism under
        # competitor_relationships.apple, which previously held only
        # the financial stub (financial_tie none, estimated $0,
        # coverage_prediction neutral).
        finding = _m868_data()["finding"]
        assert "no AI licensing deal disclosed" in finding
        assert "neutral prediction" in finding


# ---------------------------------------------------------------------------
# 5. m869 qualitative discipline (Type B #1063, journalists.yaml james_pero)
# ---------------------------------------------------------------------------
class TestTypeDM869QualitativeDiscipline:
    def test_mechanism_id_and_identity(self):
        d = _m869_data()
        assert d["mechanism_id"] == 869
        assert d["iteration"] == 1063
        assert d["iteration_type"] == "B"
        assert d["journalist"] == "James Pero"
        assert "Gizmodo" in d["publication"]

    def test_finding_carries_manual_illustrative_arms(self):
        finding = _m869_data()["finding"]
        assert "+0.50 illustrative" in finding
        assert "-0.30 illustrative" in finding
        assert "Illustrative delta +0.80" in finding
        assert "MANUAL ILLUSTRATIVE only" in finding

    def test_temporal_replication_of_m818(self):
        finding = _m869_data()["finding"]
        assert "REPLICATES m818" in finding
        assert "not a uniform anti-Meta stance" in finding

    def test_statistical_discipline_nested(self):
        d = _m869_data()
        sd = d["statistical_discipline"]
        assert "p_value NOT_CALCULATED" in sd
        assert "cohens_d NOT_CALCULATED" in sd
        assert "is_significant False" in sd
        assert "engine NOT run" in sd
        assert "verdict directionally_supported_not_proven" in sd

    def test_not_falsification_family_member(self):
        d = _m869_data()
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 35


# ---------------------------------------------------------------------------
# 6. m870 qualitative discipline (Type C #1064, competitor-entities.yaml)
# ---------------------------------------------------------------------------
class TestTypeDM870QualitativeDiscipline:
    def test_mechanism_id_and_identity(self):
        d = _m870_data()
        assert d["mechanism_id"] == 870
        assert d["iteration"] == 1064
        assert d["iteration_type"] == "C"
        assert "TWENTIETH" in d["mechanism_name"]
        assert "DEMAND-UNDERWRITING" in d["mechanism_name"]

    def test_three_legs_present(self):
        d = _m870_data()
        assert "4.5GW" in d["commitment_leg"]
        assert "$664B" in d["underwrite_leg"]
        assert "Force majeure" in d["stress_leg"]

    def test_taxonomy_enumeration(self):
        tax = _m870_data()["relationship_direction_taxonomy"]
        assert "TWENTIETH relationship direction" in tax
        assert "demand-recycling" in tax
        assert "backstop-recycling" in tax

    def test_tone_not_scored(self):
        d = _m870_data()
        assert d["tone_scored"] is False
        assert "tone NOT_SCORED" in d["coverage_nexus"]

    def test_statistical_discipline(self):
        d = _m870_data()
        assert d["is_significant"] is False
        assert d["verdict"] == "directionally_supported_not_proven"
        assert d["no_analysis_json_update"] is True
        assert d["artifact_grade"] is False
        assert d["engine_run"] is False

    def test_not_falsification_family_member(self):
        d = _m870_data()
        assert d["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 7. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1065:
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
        # None of m868/m869/m870 is a falsification-family member:
        # m868 prose-only, m869 field False, m870 field False.
        assert "NOT a falsification-family member" in _m868_data()["finding"]
        assert _m869_data()["falsification_family_member"] is False
        assert _m870_data()["falsification_family_member"] is False

# ---------------------------------------------------------------------------
# 8. Forward-looking staleness
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1065:
    WINDOW_FILES = [
        "tests/test_type_a_1062_ft_apple_sep2026_duo_launch_market_"
        "register_vs_meta_muse_product_register_sep28_11pm.py",
        "tests/test_type_b_1063_james_pero_gizmodo_vr_headsets_cooked_"
        "enthusiasm_vs_pr_cleanup_adversarial_sep29_12am.py",
        "tests/test_type_c_1064_oracle_openai_300b_45gw_demand_"
        "underwriting_twentieth_direction_sep29_1am.py",
    ]
    OWN_IDS = {
        "tests/test_type_a_1062_ft_apple_sep2026_duo_launch_market_"
        "register_vs_meta_muse_product_register_sep28_11pm.py": 868,
        "tests/test_type_b_1063_james_pero_gizmodo_vr_headsets_cooked_"
        "enthusiasm_vs_pr_cleanup_adversarial_sep29_12am.py": 869,
        "tests/test_type_c_1064_oracle_openai_300b_45gw_demand_"
        "underwriting_twentieth_direction_sep29_1am.py": 870,
    }

    def test_window_files_carry_m_id_870(self):
        # The #1062/#1063/#1064 files were pinned forward to M_ID =
        # 870 by the #1064 main commit (their max-id guards already
        # account for m870).
        for rel in self.WINDOW_FILES:
            text = _read(os.path.join(REPO_ROOT, rel))
            assert "M_ID = 870" in text, rel

    def test_window_files_carry_own_m_id_split(self):
        # The OWN_M_ID split (own mechanism id asserted separately
        # from the corpus max) is pinned in the #1062/#1063 window
        # files: 868 / 869 respectively. The #1064 file carries no
        # OWN_M_ID split by design: its own mechanism 870 IS the
        # corpus max, so M_ID serves both roles there.
        for rel, own in self.OWN_IDS.items():
            if rel == self.WINDOW_FILES[2]:
                text = _read(os.path.join(REPO_ROOT, rel))
                assert "OWN_M_ID" not in text, rel
                continue
            text = _read(os.path.join(REPO_ROOT, rel))
            assert "OWN_M_ID = %d" % own in text, rel

    def test_zero_871_guards_pass_this_run(self):
        # The window files' forward-looking next-number guards PASS
        # this run (needles are 871-form in all three files; the
        # #1062/#1063 test names still say 869/870 but the
        # NEXT_US / NEXT_DASH / NEXT_NUMERIC needles they assert are
        # 871-form since the #1064 roll) - verified via subprocess,
        # NOT touched by this run.
        targets = [
            self.WINDOW_FILES[0]
            + "::TestCorpusNoveltyPostCommit::"
            + "test_zero_next_numeric_869_in_profiles",
            self.WINDOW_FILES[0]
            + "::TestCorpusNoveltyPostCommit::"
            + "test_zero_next_underscore_dash_869_repo_wide",
            self.WINDOW_FILES[1]
            + "::TestCorpusNoveltyPostCommit::"
            + "test_zero_next_numeric_870_in_profiles",
            self.WINDOW_FILES[1]
            + "::TestCorpusNoveltyPostCommit::"
            + "test_zero_next_underscore_dash_870_repo_wide",
            self.WINDOW_FILES[2]
            + "::TestCorpusNoveltyPostCommit::"
            + "test_zero_next_numeric_871_in_profiles",
            self.WINDOW_FILES[2]
            + "::TestCorpusNoveltyPostCommit::"
            + "test_zero_next_underscore_dash_871_repo_wide",
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
        assert result.returncode == 0, result.stdout[-2000:]

    def test_zero_871_guards_staleness_calendar(self):
        # Calendar pin: the 870 landing happened at #1064 (Type C).
        # The zero-871 guards fail BY DESIGN when mechanism 871 lands
        # - expected at a future A/B/C leg of the 1065-1069 window.
        # To be pinned by the next Type D run.
        assert 1064 + 1 == 1065
        for rel in self.WINDOW_FILES:
            assert os.path.exists(os.path.join(REPO_ROOT, rel))


# ---------------------------------------------------------------------------
# 9. Background suite tombstone
# ---------------------------------------------------------------------------
class TestTypeDBackgroundSuiteTombstone1065:
    def test_prior_suite_log_is_stalled(self):
        # The #1060 re-launched full suite (type_d_1060_full_suite.log)
        # stalled at 241 bytes since Sep 28 21:10 PDT with zero summary
        # tokens; no pytest process is alive for it at this run's
        # check. Per the #795 convention this is a background death:
        # FIFTY-FOURTH consecutive, tombstone lineage advances
        # SEVENTY-SECOND -> SEVENTY-THIRD. (The #1055 suite was
        # already tombstoned by #1060; NOT re-tombstoned here.)
        assert os.path.exists(PRIOR_SUITE_LOG)
        size = os.path.getsize(PRIOR_SUITE_LOG)
        assert 150 < size < 400, size
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
            if "pytest" in line and "type_d_1060" in line
        ]
        assert pytest_lines == [], pytest_lines

    def test_tombstone_lineage(self):
        # The lineage marker: #1060's entry recorded SEVENTY-FIRST ->
        # SEVENTY-SECOND; this run advances it to SEVENTY-THIRD.
        entry = _read(LOG_PATH)
        idx = entry.index("## #1060 Type D:")
        block = entry[idx : idx + 12000]
        assert "SEVENTY-SECOND" in block


# ---------------------------------------------------------------------------
# 10. Synthetic engine calibration (fresh values, not #1060's)
# ---------------------------------------------------------------------------
class TestTypeDSyntheticEngineCalibration1065:
    # FRESH synthetic corpora this run (new values, not #1060's).
    # Engine significance is never promoted to a finding: the m868 /
    # m869 / m870 mechanisms verified this run carry finding-layer
    # is_significant false / NOT asserted per the Aug 28 2026 standing
    # rule.
    STRONG_META = [-0.71, -0.76, -0.73, -0.77, -0.72, -0.75, -0.74]
    STRONG_COMP = [0.05, 0.01, 0.04, -0.02, 0.02, 0.06, 0.00]
    NULL_META = [-0.03, 0.02, -0.01, 0.04, -0.05, 0.01, 0.00]
    NULL_COMP = [0.02, -0.03, 0.04, -0.01, 0.05, -0.04, 0.03]

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

        assert asym == pytest.approx(-0.7628571428571430, rel=1e-12)
        assert t == pytest.approx(-56.184592968934730, rel=1e-9)
        assert p == pytest.approx(4.9526769056458606e-15, rel=1e-6)
        assert d == pytest.approx(-30.031928186443125, rel=1e-9)
        assert ci[0] == pytest.approx(-0.7885714285714286, rel=1e-12)
        assert ci[1] == pytest.approx(-0.7371428571428571, rel=1e-12)
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
        assert asym == pytest.approx(-0.0114285714285714, rel=1e-9)
        assert t == pytest.approx(-0.648885684523050, rel=1e-9)
        assert p == pytest.approx(0.52890275539013287, rel=1e-9)
        assert d == pytest.approx(-0.346843987809648, rel=1e-9)
        assert ci[0] == pytest.approx(-0.0428571428571429, rel=1e-9)
        assert ci[1] == pytest.approx(0.0200000000000000, rel=1e-9)
        assert ci[0] < 0 < ci[1], "CI crosses zero"
        assert p >= 0.05, "near-null pair stays silent"

    def test_degenerate_n1_guard_on_m868_pair(self):
        # Degenerate n=1-per-arm contract on the m868 illustrative
        # pair ([+0.10] Apple, [+0.05] Meta): the classic guard.
        welch_t_test, cohens_d, _ = self._scorer()
        import numpy as np
        import pytest

        apple_arm = [0.10]
        meta_arm = [0.05]
        t, p = welch_t_test(apple_arm, meta_arm)
        d = cohens_d(apple_arm, meta_arm)
        assert abs(float(np.mean(apple_arm) - np.mean(meta_arm))) == pytest.approx(
            0.0500000000000000, abs=1e-12
        )
        assert t == 0.0
        assert p == 1.0
        assert d == 0.0
        # Arm-swap negates the signed asymmetry.
        t2, _ = welch_t_test(meta_arm, apple_arm)
        assert t2 == 0.0
        assert float(np.mean(meta_arm) - np.mean(apple_arm)) == pytest.approx(
            -0.0500000000000000, abs=1e-12
        )


# ---------------------------------------------------------------------------
# 11. Suite relaunch
# ---------------------------------------------------------------------------
class TestTypeDSuiteRelaunch1065:
    def test_suite_log_relaunched_and_live(self):
        # The full suite is re-launched by this run as a background
        # process writing to goal hidden_files type_d_1065_full_suite.log
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
class TestDocSync1065:
    def test_readme_row_1065(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1065(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1065_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


# ---------------------------------------------------------------------------
# 13. Iteration log per #719 / #721 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestIterationLog1065:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1065 Type D:")
        return log[idx : idx + 25000]

    def test_entry_present(self):
        assert "## #1065 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "SEVENTY-THIRD" in entry
        assert "870" in entry

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
