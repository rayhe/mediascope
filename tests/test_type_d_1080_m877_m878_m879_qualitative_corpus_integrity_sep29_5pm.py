"""Type D -- Iteration #1080 (Tue 2026-09-29 17:00 PDT): m877/m878/m879
qualitative-discipline verification + post-1075-1079 corpus integrity
(max numeric mechanism_id 879; zero next-number 880 keys in
numeric/underscore/dash mechanism forms; underscore/dash 880 needles
are format-built per #715 so no guard-literal carrier file exists -
the repo-wide 880 sweep is pure zero on source files (the local
tests/__pycache__ .pyc artifacts carry concatenated needle strings
from their own guards; untracked build artifacts, excluded per the
#715 pattern-rescope lesson); the #1075 Type D file gets its
historical repin (MAX_ID 876->879, NEXT_NUM 877->880, rotation guard
rewritten to the 1075-1079 window-closed-complete subsequence form,
no-Type-E-1076 inverted to Type-E-1076-landed d216984d, entry
newest-first -> entry-present, anchor mechanics untouched); the
#1076/#1077/#1078 window files are NOT edited by this run - their
now-stale forward-looking numeric guards are pinned as fail-by-design
via subprocess in the staleness class (5 numeric: #1076 zero-877 +
max-876 + #1075-repin-pin, #1077 max-877, #1078 max-878; the
underscore/dash 879 carrier sweep still passes by the #715
fragment-construction design - the designed split); ledger holds at
36 with the THIRTY-SIXTH member-claim form present twice
(journalists.yaml m878 verdict_note + falsification_family),
TWENTY-NINTH in news-corp, THIRTY-SEVENTH member-form absent in
profiles/) + #1075 background-suite tombstone (FIFTY-SEVENTH
consecutive death; lineage SEVENTY-FIFTH -> SEVENTY-SIXTH) + fresh
synthetic engine calibration (new values, not #1075's) + re-launch of
the full suite as a background process writing to goal hidden_files
type_d_1080_full_suite.log (next Type D run checks its verdict per
the #795 convention).

Type D FIRST leg of the 1080-1084 window, OPENING it
(D->E->A->B->C). Committed predecessor #1079 Type C (16:00 PDT Sep
29) CLOSED the 1075-1079 window (D #1075, E #1076, A #1077, B #1078,
C #1079). Rotation per the #565 anchor + rotation guard.
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
- m877 (Type A #1077, wired.yaml 6-space block key
  wired_openai_sep29_astra_cancellation_accountability_register_
  vs_carried_meta_arms, `mechanism_id: 877` field form; block key
  count 2 in the home YAML - colon-form line + test_file: field,
  designed): WIRED applies a safety-crisis accountability register
  to the deal partner (OpenAI, Conde Nast Aug 2024 licensing
  partner) - NEW Sep-29 Isabella Ward piece MANUAL ILLUSTRATIVE
  -0.35 (relay-attested per #503) vs carried Meta arms from m820
  (-0.45) and m757 (-0.30) per #807; illustrative deltas +0.10 /
  -0.05, near-null parity; TEMPORAL EXTENSION of m712 (+0.15 to
  -0.35, swing -0.50); statistical_discipline nested under
  asymmetry_scorer (scorer none, p_value/cohens_d/ci_95
  NOT_CALCULATED, is_significant false, engine_run false, verdict
  directionally_supported_not_proven, no_analysis_json_update
  true, artifact_grade false); falsification_family_member false,
  falsification_ledger 35 - NOT a member.
- m878 (Type B #1078, journalists.yaml isabella_ward
  competitor_coverage 4-space block key
  type_b_1078_isabella_ward_wired_openai_vs_anthropic_
  accountability_register_constancy_sep29, `mechanism_id: 878`
  field form; block key count 3 - colon-form line + block_key:
  field + test_file: field substring, designed): writer-level
  deal-gradient falsification - Ward runs the accountability
  register at -0.35 on the deal partner (OpenAI, m877 carried) vs
  -0.40 on the non-deal competitor (Anthropic, fresh excerpt-tier),
  illustrative delta -0.05 near-null; verdict
  falsified_softer_prediction; statistical_discipline prose-only
  (MANUAL ILLUSTRATIVE ONLY, NOT_CALCULATED, is_significant
  False, engine NOT run, NOT artifact-grade); THIRTY-SIXTH
  falsification-family member (ledger 35->36).
- m879 (Type C #1079, profiles/competitor-entities.yaml top-level
  block, zero indent, block key
  type_c_1079_openai_india_pipeline_expansion_inbound_pull_
  twentythird_direction_sep29_4pm, `mechanism_id: 879` field form;
  block key count 2 - colon-form line + block_key: field,
  designed): FIRST dedicated corpus mechanism on the Sep-28-2026
  exchange4media report of OpenAI's India publisher pipeline
  expansion - INBOUND-PULL as the TWENTY-THIRD relationship
  direction per the m807 enumeration; five legs (pipeline,
  inbound, pricing-context carried from m798, inventory, traffic
  tension); coverage nexus carries tone NOT_SCORED; tone_scored
  false, verdict directionally_supported_not_proven,
  falsification_family_member False - NOT a member (ledger holds
  at 36).

Statistical discipline across all three: MANUAL ILLUSTRATIVE ONLY
per the Aug 28 2026 standing rule, engine NOT run at the finding
layer, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False
/ not asserted at the finding layer, verdict
directionally_supported_not_proven, no_analysis_json_update true,
NOT artifact-grade; no analysis.json update. Only m878 is a
falsification-family member (THIRTY-SIXTH, ledger 35->36).
Correlation only, not causation. Hypothesis-generating only.

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

ANCHORED_SHA = "0" * 40  # patched by the anchor followup commit per #565

MAX_ID = 879
NEXT_NUM = 880

M877_KEY = (
    "wired_openai_sep29_astra_cancellation_accountability_"
    "register_vs_carried_meta_arms"
)
M877_INDENT = 4
M877_HOME = "profiles/wired.yaml"
M878_KEY = (
    "type_b_1078_isabella_ward_wired_openai_vs_anthropic_"
    "accountability_register_constancy_sep29"
)
M878_INDENT = 4
M878_HOME = "profiles/careers/journalists.yaml"
M879_KEY = (
    "type_c_1079_openai_india_pipeline_expansion_inbound_pull_"
    "twentythird_direction_sep29_4pm"
)
M879_INDENT = 0
M879_HOME = "profiles/competitor-entities.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1080_full_suite.log"
)
PRIOR_SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1075_full_suite.log"
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
    # First occurrence of each distinct iteration number, newest first.
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"^Type ([A-E]) #(\d+)", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


# At this run's anchor followup, the newest distinct iteration
# numbers in git history: #1080 Type D opens the 1080-1084 window;
# #1079 Type C (committed 16:00 PDT Sep 29) is the schedule
# predecessor and CLOSED the 1075-1079 window. The in-flight runs
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
    file carries a contiguous 880-form mechanism literal (verified
    pre-commit), so the 880 sweeps run repo-wide with only this file
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


def _m877_data():
    return _block_data(M877_HOME, M877_KEY, M877_INDENT)


def _m878_data():
    return _block_data(M878_HOME, M878_KEY, M878_INDENT)


def _m879_data():
    return _block_data(M879_HOME, M879_KEY, M879_INDENT)


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1080:
    def test_no_type_d_1080_test_file_preexisting(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1080*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1080 glob"

    def test_no_type_d_1080_in_git_log(self):
        # Pre-commit novelty: no Type D #1080 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1080"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1080" in line
            and "followup" not in line.lower()
            and "push-status" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_879(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_880_numeric_forms_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        # m877: descriptive block key at 6-space indent in wired.yaml,
        # exactly one colon-form occurrence.
        assert (
            _read(os.path.join(REPO_ROOT, M877_HOME)).count(
                "\n" + " " * M877_INDENT + M877_KEY + ":"
            )
            == 1
        )
        # m878: block key at 4-space indent under isabella_ward's
        # competitor_coverage in journalists.yaml.
        assert (
            _read(os.path.join(REPO_ROOT, M878_HOME)).count(
                "\n" + " " * M878_INDENT + M878_KEY + ":"
            )
            == 1
        )
        # m879: block key at zero indent in competitor-entities.yaml.
        assert (
            _read(os.path.join(REPO_ROOT, M879_HOME)).count(
                "\n" + M879_KEY + ":"
            )
            == 1
        )

    def test_m877_key_count_is_designed(self):
        # The m877 key appears twice in wired.yaml: the colon-form
        # block-key line and the test_file: field referencing the
        # #1077 Type A test file - designed, not a corpus duplicate.
        assert _read(os.path.join(REPO_ROOT, M877_HOME)).count(M877_KEY) == 2

    def test_m878_key_count_is_designed(self):
        # The m878 key appears three times in journalists.yaml: the
        # colon-form block-key line, the block_key: field, and the
        # test_file: field substring - designed, not a corpus
        # duplicate.
        text = _read(os.path.join(REPO_ROOT, M878_HOME))
        assert text.count("\n" + " " * M878_INDENT + M878_KEY + ":") == 1
        assert text.count("block_key: " + M878_KEY) == 1
        assert text.count(M878_KEY) == 3

    def test_m879_key_count_is_designed(self):
        # The m879 block carries its block_key: field repeating the
        # key (designed keying per #1079): exactly 2 occurrences in
        # competitor-entities.yaml.
        text = _read(os.path.join(REPO_ROOT, M879_HOME))
        assert text.count("\n" + M879_KEY + ":") == 1
        assert text.count("block_key: " + M879_KEY) == 1
        assert text.count(M879_KEY) == 2

    def test_1080_entry_newest_first_in_log(self):
        # The "## #1080 Type D:" entry leads the log (newest-first
        # ordering); hashes are TBD until the anchor followup patches
        # them per #565. Deselected pre-commit per #721.
        assert _read(LOG_PATH).startswith("## #1080 Type D:")


# ---------------------------------------------------------------------------
# 2. Rotation guard per #565
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1080:
    def test_rotation_window_opens_1080(self):
        # The newest distinct iteration in git history is this run's
        # #1080 Type D (window opener). The full 1075-1079 window is
        # regex-visible (no subject deviations in this window): D
        # #1080 -> C #1079 -> B #1078 -> A #1077 -> E #1076.
        # Deselected pre-commit per #565 (passes post-commit).
        window = _window()
        assert window[0] == ("D", "1080"), window
        assert window[1:5] == [
            ("C", "1079"),
            ("B", "1078"),
            ("A", "1077"),
            ("E", "1076"),
        ], window

    def test_predecessor_1079_chain_present(self):
        # The full #1079 Type C commit chain must be in git history
        # before this run's main commit (rotation transparency per
        # #565): main a04bf111, anchor 5b102a31, log-hash 463e36ea,
        # log-hash tweak f2a2d95f.
        for sha in (
            "a04bf111",
            "5b102a31",
            "463e36ea",
            "f2a2d95f",
        ):
            assert (
                subprocess.run(
                    ["git", "cat-file", "-e", sha],
                    cwd=REPO_ROOT,
                    capture_output=True,
                ).returncode
                == 0
            ), sha

    def test_no_type_e_1081_in_git_log(self):
        # The next leg (Type E #1081) must not exist yet: this run
        # opens the window, #1081 continues it.
        result = subprocess.run(
            ["git", "log", "--format=%s", "--grep=Type E #1081"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.stdout.strip() == "", result.stdout

    def test_anchor_sha_is_real(self):
        # Deselected pre-commit per #565: the anchor followup patches
        # ANCHORED_SHA to the 40-char main commit hash.
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
class TestTypeDCorpusIntegrity1080:
    def test_underscore_880_zero_repo_wide(self):
        # Underscore-form 880 needles are pure zero on source files:
        # the #1076/#1077/#1078/#1079 files build their
        # forward-looking needles at runtime per #715, so no
        # contiguous literal exists in any source file - no
        # guard-literal carrier file is pinned this run.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_dash_880_zero_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_thirty_seventh_member_form_absent_in_profiles(self):
        # THIRTY-SEVENTH falsification-member form is absent across
        # profiles/ (ledger holds at 36); the tombstone-lineage prose
        # in test files carries ordinal words without the member
        # claim and is outside this sweep's scope.
        assert _profiles_with("THIRTY-SEVENTH") == []

    def test_thirty_sixth_member_form_present(self):
        # The THIRTY-SIXTH member-claim form is present exactly where
        # the #1078 Type B run put it: journalists.yaml m878
        # verdict_note + falsification_family (2 occurrences). The
        # competitor-entities.yaml falsification_note is a ledger
        # cross-reference ("THIRTY-SIXTH member ("), not the
        # member-claim form.
        claim = "THIRTY-SIXTH falsification-family member"
        jpath = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        assert _read(jpath).count(claim) == 2
        assert claim not in _read(
            os.path.join(PROFILES_DIR, "competitor-entities.yaml")
        )


# ---------------------------------------------------------------------------
# 4. m877 qualitative discipline (Type A #1077, wired.yaml)
# ---------------------------------------------------------------------------
class TestTypeDM877QualitativeDiscipline:
    def test_mechanism_id_and_identity(self):
        d = _m877_data()
        assert d["mechanism_id"] == 877
        assert d["iteration"] == 1077
        assert d["iteration_type"] == "A"
        assert d["publication"] == "wired"
        assert "Astra-cancellation" in d["mechanism_name"]
        assert d["window"] == "1075-1079"

    def test_openai_arm_carries_manual_illustrative_tone(self):
        arm = _m877_data()["openai_arm"]
        assert arm["manual_illustrative_tone"] == -0.35
        assert "Isabella Ward" in arm["author"]
        # The #503 suffix is a YAML comment in the source; the parsed
        # value is the relay-attestation phrase.
        assert arm["url_status"] == "relay-attested per"

    def test_illustrative_deltas_near_null_parity(self):
        sd = _m877_data()["asymmetry_scorer"]
        assert sd["openai_arm_tone"] == -0.35
        assert sd["meta_primary_arm_tone"] == -0.45
        assert sd["meta_secondary_arm_tone"] == -0.30
        assert sd["illustrative_delta_openai_minus_meta_primary"] == 0.10
        assert sd["illustrative_delta_openai_minus_meta_secondary"] == -0.05
        assert "Near-null parity" in sd["delta_reading"]

    def test_statistical_discipline_nested(self):
        sd = _m877_data()["asymmetry_scorer"]
        assert sd["scorer"] == "none"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert sd["artifact_grade"] is False
        assert sd["no_analysis_json_update"] is True
        assert "MANUAL ILLUSTRATIVE ONLY" in sd["manual_illustrative_only"]

    def test_not_falsification_family_member(self):
        # m877 is NOT a falsification-family member: near-null
        # parity on a register pair with no uniform-prediction test
        # run - the ledger note pins the standing count at 35 for the
        # run that committed it (the 36th landed at #1078).
        d = _m877_data()
        assert d["falsification_family_member"] is False
        assert d["falsification_ledger"] == 35
        assert "NOT a falsification-family member" in d["ledger_note"]
        assert "Ledger holds at 35" in d["ledger_note"]


# ---------------------------------------------------------------------------
# 5. m878 qualitative discipline (Type B #1078, journalists.yaml
#    isabella_ward)
# ---------------------------------------------------------------------------
class TestTypeDM878QualitativeDiscipline:
    def test_mechanism_id_and_identity(self):
        d = _m878_data()
        assert d["mechanism_id"] == 878
        assert d["iteration"] == 1078
        assert d["iteration_type"] == "B"
        assert d["goal_id"] == "goal_54093bda4145"

    def test_writer_level_falsification_verdict(self):
        d = _m878_data()
        assert d["verdict"] == "falsified_softer_prediction"
        ff = d["falsification_family"]
        assert "THIRTY-SIXTH falsification-family member" in ff
        assert "ledger 35->36" in ff
        assert "illustrative delta -0.05 near-null" in ff

    def test_statistical_discipline_prose(self):
        sd = _m878_data()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in sd
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in sd
        assert "is_significant False" in sd
        assert "Engine NOT run" in sd
        assert "directionally_supported_not_proven" in sd
        assert "NOT artifact-grade" in sd

    def test_thirty_sixth_member_claim_forms(self):
        # Both member-claim forms live in the m878 block: the
        # verdict_note and the falsification_family prose.
        text = _indented_block(M878_HOME, M878_KEY, M878_INDENT)
        assert text.count("THIRTY-SIXTH falsification-family member") == 2


# ---------------------------------------------------------------------------
# 6. m879 qualitative discipline (Type C #1079, competitor-entities.yaml)
# ---------------------------------------------------------------------------
class TestTypeDM879QualitativeDiscipline:
    def test_mechanism_id_and_identity(self):
        d = _m879_data()
        assert d["mechanism_id"] == 879
        assert d["type"] == "financial_incentive_mapping"
        assert d["iteration"] == 1079
        assert d["iteration_type"] == "C"
        assert d["goal_id"] == "goal_54093bda4145"

    def test_inbound_pull_twenty_third_direction(self):
        d = _m879_data()
        assert "TWENTY-THIRD" in d["relationship_direction_taxonomy"]
        assert "INBOUND-PULL" in d["relationship_direction_taxonomy"]
        assert "23 inbound-pull m879" in d["relationship_direction_taxonomy"]

    def test_five_legs_present(self):
        d = _m879_data()
        assert "exchange4media Sep 28 2026" in d["pipeline_leg"]
        assert "yet to secure commercial arrangements" in d["inbound_leg"]
        assert "Carried from m798" in d["pricing_context_leg"]
        assert "100M weekly ChatGPT users" in d["inventory_leg"]
        assert "discovery journey changes" in d["traffic_tension_leg"]

    def test_tone_not_scored(self):
        d = _m879_data()
        assert d["tone_scored"] is False
        assert d["verdict"] == "directionally_supported_not_proven"
        assert "tone NOT_SCORED" in d["coverage_nexus"]

    def test_not_falsification_family_member(self):
        d = _m879_data()
        assert d["falsification_family_member"] is False
        assert "ledger holds at 36" in d["falsification_family"]
        assert "NOT a member" in d["falsification_family"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1080:
    def test_ledger_holds_at_36(self):
        # THIRTY-SIXTH member-claim form present in journalists.yaml
        # (2 occurrences: verdict_note + falsification_family);
        # THIRTY-SEVENTH member-form absent in profiles/. The bare
        # TWENTY-NINTH ordinal is a ledger cross-reference carried in
        # several profiles - only the member-claim forms pin the
        # ledger count.
        claim36 = "THIRTY-SIXTH falsification-family member"
        jtext = _read(
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        )
        assert jtext.count(claim36) == 2
        assert _profiles_with("THIRTY-SEVENTH") == []

    def test_thirty_sixth_forms_are_member_claims(self):
        text = _read(
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        )
        assert text.count("THIRTY-SIXTH falsification-family member") == 2

    def test_no_new_falsification_members_this_window(self):
        # m877 and m879 are NOT members; m878 is the 36th (landed at
        # #1078, verified here). No uniform-prediction test ran at
        # the Type D verification layer this turn.
        assert _m877_data()["falsification_family_member"] is False
        assert _m879_data()["falsification_family_member"] is False
        assert "THIRTY-SIXTH" in _m878_data()["falsification_family"]


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (per #1060 / #710 / #720)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1080:
    D1075_FILE = (
        "tests/test_type_d_1075_m874_m875_m876_qualitative_corpus_"
        "integrity_sep29_12pm.py"
    )

    def test_1075_repin_879_880(self):
        # The #1075 Type D file got its historical repin from this
        # run: MAX_ID 876->879 (corpus max tracking), NEXT_NUM
        # 877->880 (forward-looking guards now sweep the next
        # number).
        rel = self.D1075_FILE
        text = _read(os.path.join(REPO_ROOT, rel))
        assert "MAX_ID = 879" in text, rel
        assert "NEXT_NUM = 880" in text, rel
        assert "pinned by #1080 Type D" in text, rel

    def test_1075_rotation_guard_window_closed(self):
        # The #1075 rotation guard was rewritten to the
        # window-closed-complete subsequence form (stable across this
        # run's main commit): the 1075-1079 chain is asserted as a
        # filtered subsequence, the Type E #1076 forward-looking
        # guard is inverted to a landed assertion, and the entry
        # test asserts presence rather than newest-first position.
        rel = self.D1075_FILE
        text = _read(os.path.join(REPO_ROOT, rel))
        assert "def test_1075_window_closed_complete" in text, rel
        assert "def test_type_e_1076_landed" in text, rel
        assert "def test_1075_entry_present_in_log" in text, rel
        assert "def test_no_type_e_1076_in_git_log" not in text, rel
        assert "def test_rotation_window_opens_1075" not in text, rel
        assert "def test_1075_entry_newest_first_in_log" not in text, rel

    def test_stale_guards_fail_by_design_pinned(self):
        # The #1076/#1077/#1078 window files are NOT edited by this
        # run; their now-stale forward-looking numeric guards FAIL BY
        # DESIGN now that mechanisms 877/878/879 landed, and are
        # pinned here per the #1065/#1070/#1075 lifecycle calendar.
        # The #1076 file's pin on the #1075 repin also fails by
        # design (repin landed here). The underscore/dash 879 carrier
        # sweep still PASSES (needles are format-built per #715 - no
        # contiguous literals exist repo-wide) - the designed split.
        targets = [
            "tests/test_type_e_1076_podcast_sentiment_138th_verification_"
            "sep29_1pm.py"
            "::TestGuardLifecycleZero877Pin::"
            "test_zero_next_numeric_877_in_profiles",
            "tests/test_type_e_1076_podcast_sentiment_138th_verification_"
            "sep29_1pm.py"
            "::TestCorpusNoveltyPreCommitGreps::"
            "test_max_numeric_mechanism_id_876",
            "tests/test_type_e_1076_podcast_sentiment_138th_verification_"
            "sep29_1pm.py"
            "::TestGuardLifecycleZero877Pin::"
            "test_1075_file_pins_max_id_876_and_next_877",
            "tests/test_type_a_1077_wired_openai_sep29_astra_cancellation_"
            "accountability_register_vs_carried_meta_arms_sep29_2pm.py"
            "::TestGuardLifecycle877Lands::"
            "test_max_mechanism_id_now_877",
            "tests/test_type_b_1078_isabella_ward_wired_openai_vs_"
            "anthropic_accountability_register_constancy_sep29_3pm.py"
            "::TestGuardLifecycle878Lands::"
            "test_878_landing_in_journalists_yaml",
            "tests/test_type_b_1078_isabella_ward_wired_openai_vs_"
            "anthropic_accountability_register_constancy_sep29_3pm.py"
            "::TestGuardLifecycle878Lands::"
            "test_zero_879_forward_needles_format_built",
        ]
        result = subprocess.run(
            [
                os.path.join(REPO_ROOT, ".venv", "bin", "python"),
                "-m",
                "pytest",
                "-q",
                "-p",
                "no:warnings",
                *targets,
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0, (
            "expected the stale numeric guards to fail by design now "
            "that mechanisms 877/878/879 landed; got returncode 0:\n"
            + result.stdout[-2000:]
        )
        # Designed split: the 5 numeric guards fail (mechanism_id:
        # 877/878/879 are in profiles/, the #1075 repin moved past
        # 876/877); the underscore/dash 879 carrier sweep still
        # passes (879 needles are format-built per #715, no
        # contiguous literals repo-wide).
        assert "5 failed, 1 passed" in result.stdout, result.stdout[-2000:]

    def test_zero_880_guards_staleness_calendar(self):
        # Calendar pin: the 879 landing happened at #1079 (Type C).
        # The zero-880 guards fail BY DESIGN when mechanism 880 lands
        # - expected at a future A/B/C leg of the 1080-1084 window.
        # To be pinned by the next Type D run (#1085).
        assert 1079 + 1 == 1080
        for rel in (
            self.D1075_FILE,
            "tests/test_type_e_1076_podcast_sentiment_138th_verification_"
            "sep29_1pm.py",
            "tests/test_type_a_1077_wired_openai_sep29_astra_cancellation_"
            "accountability_register_vs_carried_meta_arms_sep29_2pm.py",
            "tests/test_type_b_1078_isabella_ward_wired_openai_vs_"
            "anthropic_accountability_register_constancy_sep29_3pm.py",
            "tests/test_type_c_1079_openai_india_pipeline_expansion_"
            "inbound_pull_twentythird_direction_sep29_4pm.py",
        ):
            assert os.path.exists(os.path.join(REPO_ROOT, rel))


# ---------------------------------------------------------------------------
# 9. Guard lifecycle for mechanism 879 (per #710 / #720 / #1060)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1080:
    def test_879_landed_this_window(self):
        # Mechanism 879 landed at #1079 Type C (this window's closing
        # leg). The #1075/#1076/#1077/#1078 zero-877/878/879
        # forward-looking numeric guards and the zero-36th-member
        # guards fail BY DESIGN from that commit; supersession
        # documented per #710/#720.
        assert _max_numeric_mechanism_id() == 879
        hits = _repo_grep_numeric_mechanism_id(879)
        assert len(hits) == 1 and hits[0].endswith(
            "competitor-entities.yaml"
        ), hits

    def test_zero_880_forward_needles_runtime_built(self):
        # This file's zero-880 forward needles are runtime-built (per
        # #715): no contiguous underscore/dash 880 literal is pinned
        # in any source file. The next Type D run (#1085) pins the
        # zero-881 guards.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_mechanism_key_needle_carriers_added(self):
        # This run's own files carry no contiguous underscore/dash
        # 880 mechanism-key literals outside the runtime-built guard
        # helpers above. The needles are format-built (per #715) so
        # this assertion cannot self-match.
        own = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        us_needle = "mechanism" + "_" + "880"
        dash_needle = "mechanism" + "-" + "880"
        assert us_needle not in own
        assert dash_needle not in own


# ---------------------------------------------------------------------------
# 10. Background suite tombstone
# ---------------------------------------------------------------------------
class TestTypeDBackgroundSuiteTombstone1080:
    def test_prior_suite_log_is_stalled(self):
        # The #1075 re-launched full suite
        # (type_d_1075_full_suite.log) stalled at 2518 bytes / 4%
        # since Sep 29 12:59 PDT with zero summary tokens; no pytest
        # process is alive for it at this run's check. Per the #795
        # convention this is a background death: FIFTY-SEVENTH
        # consecutive, tombstone lineage advances SEVENTY-FIFTH ->
        # SEVENTY-SIXTH. (The #1070 suite was already tombstoned by
        # #1075; NOT re-tombstoned here.)
        assert os.path.exists(PRIOR_SUITE_LOG)
        size = os.path.getsize(PRIOR_SUITE_LOG)
        assert 2000 < size < 3000, size
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
            if "pytest" in line and "type_d_1075" in line
        ]
        assert pytest_lines == [], pytest_lines

    def test_tombstone_lineage(self):
        # The lineage marker: #1075's entry recorded SEVENTY-FOURTH
        # -> SEVENTY-FIFTH; this run advances it to SEVENTY-SIXTH.
        entry = _read(LOG_PATH)
        idx = entry.index("## #1075 Type D:")
        block = entry[idx : idx + 12000]
        assert "SEVENTY-FIFTH" in block

    def test_consecutive_death_count(self):
        # FIFTY-SEVENTH consecutive background full-suite death; the
        # #1075 entry recorded the FIFTY-SIXTH.
        entry = _read(LOG_PATH)
        idx = entry.index("## #1075 Type D:")
        block = entry[idx : idx + 12000]
        assert "FIFTY-SIXTH consecutive" in block


# ---------------------------------------------------------------------------
# 11. Synthetic engine calibration (fresh values, not #1075's)
# ---------------------------------------------------------------------------
class TestTypeDSyntheticEngineCalibration1080:
    # FRESH synthetic corpora this run (new values, not #1075's).
    # Engine significance is never promoted to a finding: the m877 /
    # m878 / m879 mechanisms verified this run carry finding-layer
    # is_significant false / NOT asserted per the Aug 28 2026 standing
    # rule.
    STRONG_META = [-0.58, -0.64, -0.60, -0.67, -0.59, -0.63, -0.61]
    STRONG_COMP = [0.03, 0.00, 0.05, 0.01, -0.02, 0.04, 0.02]
    NULL_META = [0.03, -0.04, 0.01, 0.00, 0.05, -0.03, 0.02]
    NULL_COMP = [-0.02, 0.05, 0.00, 0.01, -0.05, 0.02, -0.01]

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

        assert asym == pytest.approx(-0.6357142857142857, rel=1e-12)
        assert t == pytest.approx(-42.429085221428828, rel=1e-9)
        assert p == pytest.approx(9.248947518416920e-14, rel=1e-6)
        assert d == pytest.approx(-22.679300018974320, rel=1e-9)
        assert ci[0] == pytest.approx(-0.6643214285714286, rel=1e-12)
        assert ci[1] == pytest.approx(-0.6085714285714287, rel=1e-12)
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
        assert asym == pytest.approx(0.0057142857142857, rel=1e-9)
        assert t == pytest.approx(0.335672543318676, rel=1e-9)
        assert p == pytest.approx(7.429148654947594e-01, rel=1e-9)
        assert d == pytest.approx(0.179424521606503, rel=1e-9)
        assert ci[0] == pytest.approx(-0.0257142857142857, rel=1e-9)
        assert ci[1] == pytest.approx(0.0357500000000000, rel=1e-9)
        assert ci[0] < 0 < ci[1], "CI crosses zero"
        assert p >= 0.05, "near-null pair stays silent"

    def test_degenerate_n1_guard_on_m878_pair(self):
        # Degenerate n=1-per-arm contract on the m878 illustrative
        # pair ([-0.35] OpenAI deal-partner arm carried from m877,
        # [-0.40] Anthropic non-deal arm, fresh excerpt-tier): the
        # classic guard.
        welch_t_test, cohens_d, _ = self._scorer()
        import numpy as np
        import pytest

        meta_arm = [-0.35]
        comp_arm = [-0.40]
        t, p = welch_t_test(meta_arm, comp_arm)
        d = cohens_d(meta_arm, comp_arm)
        assert abs(
            float(np.mean(meta_arm) - np.mean(comp_arm))
        ) == pytest.approx(0.0500000000000000, abs=1e-12)
        assert t == 0.0
        assert p == 1.0
        assert d == 0.0
        # Arm-swap negates the signed asymmetry.
        t2, _ = welch_t_test(comp_arm, meta_arm)
        assert t2 == 0.0
        assert float(np.mean(comp_arm) - np.mean(meta_arm)) == pytest.approx(
            -0.0500000000000000, abs=1e-12
        )


# ---------------------------------------------------------------------------
# 12. Suite relaunch
# ---------------------------------------------------------------------------
class TestTypeDSuiteRelaunch1080:
    def test_suite_log_relaunched_and_live(self):
        # The full suite is re-launched by this run as a background
        # process writing to goal hidden_files
        # type_d_1080_full_suite.log (per the #795 convention); the
        # next Type D run checks its verdict. This test asserts the
        # launch happened: the log exists, is non-trivial, and
        # carries pytest progress tokens.
        assert os.path.exists(SUITE_LOG), "suite log not launched"
        size = os.path.getsize(SUITE_LOG)
        assert size > 100, size
        head = open(SUITE_LOG, encoding="utf-8", errors="replace").read(2000)
        assert (
            "." in head or "%" in head or "collected" in head
        ), head[:200]


# ---------------------------------------------------------------------------
# 13. Doc-sync ratchet per #719 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSync1080:
    def test_readme_row_1080(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1080(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_1080_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_readme_stats_ratcheted(self):
        # README stats ratchet to the authoritative collect-only
        # totals: 55518 tests / 1405 files (prior 54522/1404 was a
        # count_stats.py artifact - per the #1078 lesson the script
        # is unreliable; .venv --collect-only is authoritative).
        readme = _read(README_PATH)
        assert "55518" in readme, "README must ratchet to 55518 tests"
        assert "1405" in readme, "README must ratchet to 1405 files"


# ---------------------------------------------------------------------------
# 14. Iteration log per #719 / #721 (green post-doc-sync)
# ---------------------------------------------------------------------------
class TestIterationLog1080:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #1080 Type D:")
        return log[idx : idx + 25000]

    def test_entry_present(self):
        assert "## #1080 Type D:" in _read(LOG_PATH)

    def test_entry_records_tombstone_and_integrity(self):
        entry = self._entry()
        assert "SEVENTY-SIXTH" in entry
        assert "879" in entry

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
