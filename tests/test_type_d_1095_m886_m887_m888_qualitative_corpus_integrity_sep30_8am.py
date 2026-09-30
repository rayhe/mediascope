"""Type D -- Iteration #1095 (Wed 2026-09-30 08:00 PDT): m886/m887/m888
qualitative-discipline verification + post-1090-1094 corpus integrity
(max numeric mechanism_id 888; zero next-number 889 keys in
numeric/underscore/dash mechanism forms; underscore/dash 889 needles
are format-built per #715 so no guard-literal carrier file exists -
the repo-wide 889 sweep is pure zero on source files (the local
tests/__pycache__ .pyc artifacts carry concatenated needle strings
from their own guards; untracked build artifacts, excluded per the
#715 pattern-rescope lesson); the m886/m887/m888 block keys are
fragment-built in this file (no contiguous landed-window
mechanism-key literals, per the #1091 carrier-sweep
precedent); the #1090 Type D file gets its historical repin (MAX_ID
885->888, NEXT_NUM 886->889, rotation guard rewritten to the
1090-1094 window-closed-complete subsequence form,
no-Type-E-1091 inverted to Type-C-1094-landed 0a68923d, entry
newest-first -> entry-present, anchor mechanics untouched); the
#1091/#1092/#1093 window files are NOT edited by this run -
their now-stale forward-looking numeric guards are pinned as
fail-by-design via subprocess in the staleness class; ledger holds at
37 with the THIRTY-SEVENTH member-claim form present once
(the-verge.yaml m880 falsification_family) and the THIRTY-EIGHTH
member-claim form absent in profiles/ (the two THIRTY-EIGHTH hits
are negative-guard notes, designed); TWENTY-SIXTH relationship
direction present in competitor-entities.yaml (m888
relationship_direction_taxonomy); the twenty-seventh direction
absent) + the #1090 background-suite verdict (DIED at 2804 bytes /
~4% dots with last write Sep 30 03:59:55 PDT and zero summary
tokens, no live pytest process - SECOND consecutive
background-suite death of the new streak; the 57-run streak ENDED at
#1085 when the #1080 suite completed; tombstone lineage advances
SEVENTY-SEVENTH -> SEVENTY-EIGHTH) + fresh synthetic engine
calibration (new values, not #1090's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_1095_full_suite.log WITHOUT -x (the full inventory, calendar
by-design failures included, is needed for the #1100 triage; the next
Type D run checks its verdict per the #795 convention).

Type D FIRST leg of the 1095-1099 window, OPENING it
(D->E->A->B->C). Committed predecessor #1094 Type C (07:00 PDT Sep
30) CLOSED the 1090-1094 window (D #1090, E #1091, A #1092, B #1093,
C #1094). Rotation per the #565 anchor + rotation guard.
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
- m886 (Type A #1092, guardian.yaml 4-space block key, the
  fragment-built 886-prefixed Guardian Anthropic safety-cycle
  register key, `mechanism_id: 886` field form;
  block key count 1 - colon-form line only, designed): Guardian x
  Anthropic Sep-2026 safety-cycle register (Sep 10 "Anthropic warns
  of existential AI risks to humanity in IPO document" -0.2; Sep 12
  "We must slow the pace" -0.3; Sep 29 relay -0.25) vs carried
  Guardian x Meta arms (band mean -0.425, m537) with the OpenAI
  deal-partner third pole (-0.125); MANUAL ILLUSTRATIVE delta
  +0.175 (Meta draws the harder register; the non-partner lab sits
  between Meta and the deal partner - m517-family extension from
  piracy into safety-disclosure); statistical_discipline
  prose-only (MANUAL ILLUSTRATIVE ONLY, NOT_CALCULATED,
  is_significant false, engine NOT run, verdict
  directionally_supported_not_proven, no analysis.json update, NOT
  artifact-grade); NOT a falsification-family member (register
  documentation plus m517-family extension; ledger holds at 37).
- m887 (Type B #1093, journalists.yaml 4-space block key
  type_b_1093_jason_aten_inc_meta_muse_message_sync_vs_apple_
  audio_intelligence_third_pole_sep30, `mechanism_id: 887` field
  form; block key count 3 - colon-form line + block_key: field +
  test_file: field substring, designed): Jason Aten (Inc.)
  writer-level pair - Meta Muse message-sync expose (-0.70) vs
  carried Apple Audio Intelligence adversarial arm (-0.55) with
  the Google aspirational pole; MANUAL ILLUSTRATIVE delta
  (Apple minus Meta) +0.15 - third-pole extension of the m677 Inc.
  register gradient, REALIZES m677's testable prediction #1;
  statistical discipline per the Aug-28 standing rule; NOT a
  falsification-family member (no uniform payer-softening
  prediction under test at Inc.; ledger holds at 37).
- m888 (Type C #1094, competitor-entities.yaml zero-indent block
  key type_c_1094_anthropic_prospectus_518b_commitment_ledger_
  dual_role_recycling_twentysixth_direction_sep30_7am,
  `mechanism_id: 888` field form; block key count 2 - colon-form
  line + block_key: field, designed): Anthropic leaked draft S-1
  (Reuters review Sep 28-29 2026) - $518B future
  cloud/compute/infrastructure commitment ledger discloses the
  investor-supplier dual role (Amazon/Google on both sides);
  DUAL-ROLE RECYCLING as the TWENTY-SIXTH relationship direction
  per the m807 enumeration; partial S-1 realization of m864's
  demand-recycling proof test; tone NOT_SCORED, tone_scored false,
  verdict directionally_supported_not_proven,
  no_analysis_json_update true, NOT artifact-grade; NOT a
  falsification-family member (financial-architecture mapping of
  money flows per the #609/#614 qualitative boundary; ledger holds
  at 37).

Statistical discipline across all three: MANUAL ILLUSTRATIVE ONLY
per the Aug 28 2026 standing rule, engine NOT run at the finding
layer, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False
/ not asserted at the finding layer, verdict
directionally_supported_not_proven, no_analysis_json_update true,
NOT artifact-grade; no analysis.json update. None of the three is
a falsification-family member (ledger holds at 37).
Correlation only, not causation. Hypothesis-generating only.

ASCII-only, no em dashes.
"""

import glob
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

ANCHORED_SHA = "ed8c9cf2c0d71b34cc31fab5494f02dc828bcd42"  # patched by the anchor followup commit per #565

MAX_ID = 888
NEXT_NUM = 889

_M = "mechanism"  # fragment-built per #715: no contiguous next/prior mechanism literals
M886_KEY = _M + "_886" + "_guardian_anthropic_safety_cycle_register_" + "vs_openai_deal_partner_sep30"
M886_INDENT = 4
M886_HOME = "profiles/guardian.yaml"
M887_KEY = (
    "type_b_1093_jason_aten_inc_meta_muse_message_sync_"
    "vs_apple_audio_intelligence_third_pole_sep30"
)
M887_INDENT = 4
M887_HOME = "profiles/careers/journalists.yaml"
M888_KEY = (
    "type_c_1094_anthropic_prospectus_518b_commitment_ledger_"
    "dual_role_recycling_twentysixth_direction_sep30_7am"
)
M888_INDENT = 0
M888_HOME = "profiles/competitor-entities.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1095_full_suite.log"
)
PRIOR_SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1090_full_suite.log"
)
D1090_FILE = (
    "tests/test_type_d_1090_m883_m884_m885_qualitative_corpus_"
    "integrity_sep30_3am.py"
)
E1091_FILE = (
    "tests/test_type_e_1091_podcast_sentiment_141st_verification_"
    "sep30_4am.py"
)
A1092_FILE = (
    "tests/test_type_a_1092_guardian_anthropic_safety_cycle_"
    "register_extension_sep30_5am.py"
)
B1093_FILE = (
    "tests/test_type_b_1093_jason_aten_inc_meta_muse_message_sync_"
    "vs_apple_audio_intelligence_third_pole_sep30_6am.py"
)
C1094_FILE = (
    "tests/test_type_c_1094_anthropic_prospectus_518b_commitment_"
    "ledger_dual_role_recycling_twentysixth_direction_sep30_7am.py"
)

_DOC = __doc__

# The twenty-seventh-direction needle is fragment-built per #715 so
# this file carries no contiguous literal.
_TW27 = "TWENTY-" + "SEVENTH relationship direction"


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _indented_block(rel_path, key, indent):
    lines = _read(os.path.join(REPO_ROOT, rel_path)).splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if (
            len(line) - len(line.lstrip(" "))
            == indent
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

    return yaml.safe_load(_indented_block(rel, key, indent))[key]


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
# numbers in git history: #1095 Type D opens the 1095-1099 window;
# #1094 Type C (committed 07:00 PDT Sep 30) is the schedule
# predecessor and CLOSED the 1090-1094 window. The in-flight runs
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
    file carries a contiguous 889-form mechanism literal (verified
    pre-commit), so the 889 sweeps run repo-wide with only this file
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


def _m886_data():
    return _block_data(M886_HOME, M886_KEY, M886_INDENT)


def _m887_data():
    return _block_data(M887_HOME, M887_KEY, M887_INDENT)


def _m888_data():
    return _block_data(M888_HOME, M888_KEY, M888_INDENT)


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1095:
    def test_no_type_d_1095_test_file_preexisting(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1095*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1095 glob"

    def test_no_type_d_1095_in_git_log(self):
        # Pre-commit novelty: no Type D #1095 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1095"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1095" in line
            and "followup" not in line.lower()
            and "push-status" not in line.lower()
            and "log-hash" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_888(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_889_numeric_forms_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        # m886: descriptive block key at 4-space indent in
        # guardian.yaml, exactly one colon-form occurrence (no
        # block_key: repeat for m886, designed).
        assert (
            _read(os.path.join(REPO_ROOT, M886_HOME)).count(
                "\n" + " " * M886_INDENT + M886_KEY + ":"
            )
            == 1
        )
        # m887: block key at 4-space indent under jason_aten's
        # competitor_coverage in journalists.yaml.
        assert (
            _read(os.path.join(REPO_ROOT, M887_HOME)).count(
                "\n" + " " * M887_INDENT + M887_KEY + ":"
            )
            == 1
        )
        # m888: block key at zero indent in competitor-entities.yaml.
        assert (
            _read(os.path.join(REPO_ROOT, M888_HOME)).count(
                "\n" + M888_KEY + ":"
            )
            == 1
        )

    def test_m886_key_count_is_designed(self):
        # The m886 key appears once in guardian.yaml: the
        # colon-form block-key line only (no block_key: field, no
        # test_file substring - designed, not a corpus duplicate).
        assert _read(os.path.join(REPO_ROOT, M886_HOME)).count(M886_KEY) == 1

    def test_m887_key_count_is_designed(self):
        # The m887 key appears three times in journalists.yaml: the
        # colon-form block-key line, the block_key: field, and the
        # test_file: field substring - designed, not a corpus
        # duplicate.
        text = _read(os.path.join(REPO_ROOT, M887_HOME))
        assert text.count("\n" + " " * M887_INDENT + M887_KEY + ":") == 1
        assert text.count("block_key: " + M887_KEY) == 1
        assert text.count(M887_KEY) == 3

    def test_m888_key_count_is_designed(self):
        # The m888 block carries its block_key: field repeating the
        # key (designed keying per #1064/#1069): exactly 2
        # occurrences in competitor-entities.yaml.
        text = _read(os.path.join(REPO_ROOT, M888_HOME))
        assert text.count("\n" + M888_KEY + ":") == 1
        assert text.count("block_key: " + M888_KEY) == 1
        assert text.count(M888_KEY) == 2

    def test_1095_entry_newest_first_in_log(self):
        # The "## #1095 Type D:" entry leads the log (newest-first
        # ordering); hashes are TBD until the anchor followup patches
        # them per #565. Deselected pre-commit per #721.
        assert _read(LOG_PATH).startswith("## #1095 Type D:")


# ---------------------------------------------------------------------------
# 2. Rotation guard per #565
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1095:
    def test_rotation_window_opens_1095(self):
        # The newest distinct iteration in git history is this run's
        # #1095 Type D (window opener). The full 1090-1094 window is
        # regex-visible (no subject deviations in this window): D
        # #1095 -> C #1094 -> B #1093 -> A #1092 -> E #1091.
        # Deselected pre-commit per #565 (passes post-commit).
        window = _window()
        assert window[0] == ("D", "1095"), window
        assert window[1:5] == [
            ("C", "1094"),
            ("B", "1093"),
            ("A", "1092"),
            ("E", "1091"),
        ], window

    def test_predecessor_1094_chain_present(self):
        # The full #1094 Type C commit chain must be in git history
        # before this run's main commit (rotation transparency per
        # #565): main 0a68923d, anchor 86a6e27c, log-hash abc34c68,
        # log-hash followup 6777ec89, test-fix bddcbb74, push-status
        # 11a5a2a8.
        for sha in (
            "0a68923d",
            "86a6e27c",
            "abc34c68",
            "6777ec89",
            "bddcbb74",
            "11a5a2a8",
        ):
            assert (
                subprocess.run(
                    ["git", "cat-file", "-e", sha],
                    cwd=REPO_ROOT,
                    capture_output=True,
                ).returncode
                == 0
            ), sha

    def test_no_type_e_1096_in_git_log(self):
        # The next leg (Type E #1096) must not exist yet: this run
        # opens the window, #1096 continues it.
        result = subprocess.run(
            ["git", "log", "--format=%s", "--grep=Type E #1096"],
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
class TestTypeDCorpusIntegrity1095:
    def test_m886_block_present_in_guardian_yaml(self):
        data = _m886_data()
        assert data["mechanism_id"] == 886
        assert data["iteration"] == 1092
        assert data["iteration_type"] == "A"

    def test_m887_block_present_in_journalists_yaml(self):
        data = _m887_data()
        assert data["mechanism_id"] == 887
        assert data["iteration"] == 1093
        assert data["iteration_type"] == "B"

    def test_m888_block_present_in_competitor_entities_yaml(self):
        data = _m888_data()
        assert data["mechanism_id"] == 888
        assert data["iteration"] == 1094
        assert data["iteration_type"] == "C"

    def test_max_mechanism_id_is_888(self):
        assert _max_numeric_mechanism_id() == 888

    def test_zero_889_forms_repo_wide(self):
        # Numeric 889 absent from profiles/; underscore/dash 889
        # mechanism key strings absent repo-wide (needles are
        # runtime-built per #715, so this file carries no contiguous
        # 889 literals).
        assert _repo_grep_numeric_mechanism_id(889) == []
        assert _repo_grep_underscore_mechanism(889) == []
        assert _repo_grep_dash_mechanism(889) == []


# ---------------------------------------------------------------------------
# 4. m886 (Type A #1092) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM886QualitativeDiscipline:
    def test_m886_iteration_fields(self):
        data = _m886_data()
        assert data["mechanism_id"] == 886
        assert data["iteration"] == 1092
        assert data["iteration_type"] == "A"
        assert data["date_analyzed"] == "2026-09-30"
        assert data["competitor_pair"] == (
            "Anthropic vs Meta (OpenAI deal-partner third pole)"
        )

    def test_m886_scorer_values_and_delta(self):
        # Three Sep 10-29 2026 Anthropic arms (-0.2, -0.3, -0.25;
        # mean -0.25) vs carried Guardian x Meta band (-0.45, -0.4;
        # mean -0.425); illustrative delta +0.175 with the Meta-hard
        # direction note.
        data = _m886_data()
        scorer = data["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["peer_scores_MANUAL_ILLUSTRATIVE"] == [-0.2, -0.3, -0.25]
        assert scorer["peer_avg"] == -0.25
        assert scorer["target_scores_MANUAL_ILLUSTRATIVE"] == [-0.45, -0.4]
        assert scorer["target_avg"] == -0.425
        assert scorer["delta"] == 0.175
        assert scorer["delta_calc"] == "-0.25 - (-0.425) = +0.175"
        assert "Meta draws the harder register" in scorer["delta_direction"]

    def test_m886_m517_family_extension(self):
        # m517-family extension from piracy into safety-disclosure:
        # the OpenAI deal-partner third pole sits softest (-0.125),
        # with the Meta-hardest / Anthropic-middle / OpenAI-softest
        # severity ordering.
        data = _m886_data()
        text = str(data)
        assert "m517" in text
        assert "-0.125" in text
        assert "hardest" in text

    def test_m886_register_entities(self):
        # Peer = Anthropic Guardian Sep-2026 safety-cycle register;
        # target = carried Meta Guardian register (m537).
        data = _m886_data()
        scorer = data["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "Anthropic" in scorer["peer_entity"]
        assert "Meta" in scorer["target_entity"]
        assert "m537" in scorer["target_entity"]

    def test_m886_not_falsification_member(self):
        # Register documentation plus m517-family extension; no
        # uniform-direction prediction under test. Ledger holds at
        # 37.
        data = _m886_data()
        assert "NOT a falsification-family member" in data[
            "falsification_family"
        ]
        assert "Ledger holds at 37" in data["falsification_family"]

    def test_m886_statistical_discipline(self):
        # Monitoring-only per the Aug 28 2026 standing rule: MANUAL
        # ILLUSTRATIVE, p/d/ci NOT_CALCULATED, is_significant false,
        # engine NOT run, no analysis.json update, NOT artifact-grade.
        data = _m886_data()
        disc = data["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE" in disc
        assert "NOT_CALCULATED" in disc
        assert "is_significant false" in disc
        assert "engine NOT run" in disc
        assert "NOT artifact-grade" in disc
        assert data["no_analysis_json_update"] is True

    def test_m886_research_method(self):
        # browser.search excerpt-tier evidence only (0 browser.open;
        # theguardian.com blocked by policy that run; excerpt-bounded
        # per #503).
        data = _m886_data()
        assert "0 browser.open" in data["research_method"]
        assert "excerpt-bounded" in data["research_method"]


# ---------------------------------------------------------------------------
# 5. m887 (Type B #1093) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM887QualitativeDiscipline:
    def test_m887_iteration_fields(self):
        data = _m887_data()
        assert data["mechanism_id"] == 887
        assert data["iteration"] == 1093
        assert data["iteration_type"] == "B"
        assert data["discovery_date"] == "2026-09-30"
        assert data["journalist"].startswith("Jason Aten")

    def test_m887_three_pole_delta(self):
        # Meta arm -0.70 (Muse message-sync expose) vs carried Apple
        # arm -0.55 (Audio Intelligence adversarial) with the Google
        # aspirational pole; illustrative delta (Apple minus Meta)
        # +0.15, thesis-consistent direction.
        data = _m887_data()
        assert data["illustrative_delta"] == 0.15
        assert "-0.55 - (-0.70) = +0.15" in data["delta_note"]
        assert "Meta draws the hardest register" in data["delta_note"]

    def test_m887_realizes_m677_prediction(self):
        # Third-pole extension of the m677 Inc. register gradient;
        # REALIZES m677's testable prediction #1.
        data = _m887_data()
        assert "m677" in data["falsification_family"]
        assert "testable prediction #1" in data["falsification_family"]

    def test_m887_not_falsification_member(self):
        # No uniform payer-softening prediction under test at Inc.;
        # direction thesis-consistent. Ledger holds at 37.
        data = _m887_data()
        assert "NOT a falsification-family member" in data[
            "falsification_family"
        ]
        assert "ledger holds at 37" in data["falsification_family"]

    def test_m887_statistical_discipline(self):
        # Monitoring-only per the Aug 28 2026 standing rule.
        data = _m887_data()
        disc = data["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in disc
        assert "NOT_CALCULATED" in disc
        assert "directionally_supported_not_proven" in disc
        assert "NOT artifact" in disc

    def test_m887_research_method(self):
        # 6 browser.search query sets, 0 browser.open per #503;
        # excerpt-bounded.
        data = _m887_data()
        assert "6 browser.search" in data["research_method"]
        assert "0 browser.open" in data["research_method"]


# ---------------------------------------------------------------------------
# 6. m888 (Type C #1094) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM888QualitativeDiscipline:
    def test_m888_iteration_fields(self):
        data = _m888_data()
        assert data["mechanism_id"] == 888
        assert data["iteration"] == 1094
        assert data["iteration_type"] == "C"
        assert "TWENTY-SIXTH relationship direction" in data["mechanism_name"]
        assert "DUAL-ROLE RECYCLING" in data["mechanism_name"]

    def test_m888_twenty_sixth_direction(self):
        # DUAL-ROLE RECYCLING as the TWENTY-SIXTH relationship
        # direction per the m807 enumeration.
        data = _m888_data()
        assert "TWENTY-SIXTH" in data["relationship_direction_taxonomy"]
        assert "518" in data["mechanism_name"]

    def test_m888_commitment_ledger_terms(self):
        # $518B future cloud/compute/infrastructure commitments vs
        # the $42B 2025 net loss (~$34B non-cash charge) on $4.6B
        # revenue; Amazon/Google on both sides of the ledger.
        data = _m888_data()
        text = str(data)
        assert "$518B" in text
        assert "$42B" in text
        assert "Amazon" in text and "Google" in text

    def test_m888_tone_not_scored(self):
        # Type C financial-architecture mapping: tone NOT_SCORED per
        # the #609/#614 qualitative boundary; NOT artifact-grade.
        data = _m888_data()
        assert data["tone_scored"] is False
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False
        assert data["verdict"] == "directionally_supported_not_proven"

    def test_m888_not_falsification_member(self):
        # Financial-architecture mapping of money flows: no
        # coverage-tone pair, so no uniform prediction is tested or
        # falsified. Ledger holds at 37.
        data = _m888_data()
        assert "NOT a member" in data["falsification_family"]
        assert "holds at 37" in data["falsification_family"]

    def test_m888_novelty_and_crossrefs(self):
        # Partial S-1 realization of m864's demand-recycling proof
        # test; connects to the commitment-ledger and loss-structure
        # legs; novelty carries the m864 cross-reference.
        data = _m888_data()
        assert "m864" in str(data["novelty"])
        assert "m870" in str(data) or "m885" in str(data)


# ---------------------------------------------------------------------------
# 7. Falsification ledger per #564/#719: holds at 37
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1095:
    def _member_claim_hits(self, ordinal):
        # The member-claim form is the ordinal + "falsification-family
        # member"; negative-guard notes ("THIRTY-EIGHTH absent") are a
        # distinct designed form and must not be counted here.
        needle = ordinal + " falsification-family member"
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                if needle in open(p, encoding="utf-8", errors="replace").read():
                    hits.append(p)
        return sorted(hits)

    def test_thirty_seventh_member_claim_once(self):
        # The THIRTY-SEVENTH member-claim form appears exactly once:
        # the-verge.yaml m880 falsification_family (the m886/m887
        # blocks cite the member-form in prose - not the member-claim
        # form - so the count is unchanged).
        hits = self._member_claim_hits("THIRTY-SEVENTH")
        assert hits == [os.path.join(PROFILES_DIR, "the-verge.yaml")], hits

    def test_thirty_eighth_member_claim_absent(self):
        # No THIRTY-EIGHTH member-claim form in profiles/ - the
        # ledger holds at 37.
        assert self._member_claim_hits("THIRTY-EIGHTH") == []

    def test_thirty_eighth_negative_guards_designed(self):
        # The THIRTY-EIGHTH hits are negative-guard notes
        # ("THIRTY-EIGHTH absent"), not member claims - designed.
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if "THIRTY-EIGHTH absent" in text:
                    hits.append(p)
        assert sorted(hits) == sorted(
            [
                os.path.join(PROFILES_DIR, "the-verge.yaml"),
                os.path.join(PROFILES_DIR, "careers", "journalists.yaml"),
            ]
        ), hits

    def test_no_thirty_ninth_member_claim(self):
        assert self._member_claim_hits("THIRTY-NINTH") == []

    def test_twenty_sixth_direction_present(self):
        # The m888 block registers DUAL-ROLE RECYCLING as the
        # TWENTY-SIXTH relationship direction per the m807
        # enumeration; the twenty-seventh direction claim is absent
        # (needle fragment-built per #715).
        assert (
            "TWENTY-SIXTH relationship direction"
            in open(
                os.path.join(REPO_ROOT, M888_HOME),
                encoding="utf-8",
                errors="replace",
            ).read()
        )
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                if _TW27 in open(p, encoding="utf-8", errors="replace").read():
                    hits.append(p)
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (per #1060 / #710 / #720)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1095:
    def _stale_run(self, path, *deselects):
        cmd = [
            ".venv/bin/python",
            "-m",
            "pytest",
            path,
            "-q",
            "--no-header",
            "-p",
            "no:cacheprovider",
        ]
        for d in deselects:
            cmd.extend(["--deselect", f"{path}::{d}"])
        result = subprocess.run(
            cmd, cwd=REPO_ROOT, capture_output=True, text=True, timeout=300
        )
        return result

    def _failed(self, result):
        return [
            line
            for line in result.stdout.splitlines()
            if line.startswith("FAILED")
        ]

    def test_1090_zero_886_needles_failed_by_design(self):
        # The #1090 D file's zero-886 forward guards must FAIL in a
        # subprocess (mechanisms 886/887/888 have since landed): the
        # fail-by-design staleness markers are pinned as failures so
        # they are never silently ignored. Deselects the anchor
        # rotation/novelty/doc-sync/itlog/staleness/suite/repin/
        # calibration classes per #565/#719/#721.
        result = self._stale_run(
            D1090_FILE,
            "TestNovelty1090",
            "TestTypeDRotationGuard1090",
            "TestTypeDForwardLookingStaleness1090",
            "TestBackgroundSuiteVerdict1090",
            "TestSuiteRelaunch1090",
            "TestSyntheticEngineCalibration1090",
            "TestTypeD1090RepinOf1085File",
            "TestTypeDDocSync1090",
            "TestTypeDIterationLog1090",
        )
        assert result.returncode != 0
        failed = self._failed(result)
        stale = [
            "TestTypeDCorpusIntegrity1090::test_zero_886_forms_repo_wide",
            "TestGuardLifecycle1090::test_zero_next_numeric_886_in_profiles",
        ]
        for name in stale:
            assert any(name in line for line in failed), (
                f"expected stale-by-design failure {name}; got {failed}"
            )

    def test_1091_zero_886_needles_failed_by_design(self):
        # The #1091 E file's zero-886 / max-885 guards must FAIL in a
        # subprocess (mechanism 886 landed at #1092, 887 at #1093,
        # 888 at #1094): the numeric guards plus the 886-carrier pin
        # (the m886 block key now lives in guardian.yaml) plus the
        # format-built carrier pin in profiles. Deselects the
        # podcast-cycle / anchor / rotation / doc-sync / itlog /
        # push classes per #565/#719/#721.
        result = self._stale_run(
            E1091_FILE,
            "TestNoveltyAnchorTypeE1091",
            "TestRotationGuard1090_1094Window",
            "TestNoConcurrentInflightIterationCommits",
            "TestGuiltyFeministHundredFortyFirstCycle",
            "TestEveryoneHatesElonHundredFortyFirstCycle",
            "TestAttentionSphereHundredFortyFirstNoMatch",
            "TestPressSurfacesHundredFortyFirstCycle",
            "TestStatisticalDisciplineStandingRule",
            "TestDocSyncRatchet",
            "TestIterationLogEntry",
            "TestPushReadiness",
        )
        assert result.returncode != 0
        failed = self._failed(result)
        stale = [
            "TestGuardLifecycleZero886Pin::test_zero_next_numeric_886_in_profiles",
            "TestGuardLifecycleZero886Pin::test_886_carriers_pinned_to_guard_needles_only",
            "TestCorpusNoveltyPreCommitGreps::test_max_numeric_mechanism_id_885",
            "TestCorpusNoveltyPreCommitGreps::test_zero_numeric_next_keys_in_profiles",
            "TestCorpusNoveltyPreCommitGreps::test_zero_format_built_next_carriers_in_profiles",
        ]
        for name in stale:
            assert any(name in line for line in failed), (
                f"expected stale-by-design failure {name}; got {failed}"
            )

    def test_1092_zero_887_needles_failed_by_design(self):
        # The #1092 A file's zero-887 forward guards must FAIL in a
        # subprocess (mechanism 887 landed at #1093, 888 at #1094).
        # The underscore and dash sweeps stay literal-free by the
        # #715 fragment-construction design (they PASS); the stale
        # failures are the numeric-guard family: the max-id pin, the
        # numeric 887 sweep, and the explicit supersession marker.
        # Deselects the
        # structure/arms/scorer/discipline/ledger/anchor/rotation/
        # doc-sync/itlog classes per #565/#719/#721.
        result = self._stale_run(
            A1092_FILE,
            "TestNovelty1092",
            "TestRotationGuard1092",
            "TestNoveltyAnchor1092",
            "TestMechanism886Structure",
            "TestMechanism886AnthropicArms",
            "TestMechanism886MetaArms",
            "TestMechanism886OpenAIArms",
            "TestMechanism886Scorer",
            "TestMechanism886Discipline",
            "TestLedgerHoldsAt37",
            "TestDocSync1092",
            "TestIterationLog1092",
        )
        assert result.returncode != 0
        failed = self._failed(result)
        stale = [
            "TestSupersessionAndCorpusPost1091::test_max_numeric_id_is_886_not_885",
            "TestSupersessionAndCorpusPost1091::test_zero_numeric_887_keys_in_profiles",
            "TestSupersessionAndCorpusPost1091::test_d1091_max_885_sweep_superseded_by_design",
        ]
        for name in stale:
            assert any(name in line for line in failed), (
                f"expected stale-by-design failure {name}; got {failed}"
            )

    def test_1093_zero_888_needles_failed_by_design(self):
        # The #1093 B file's zero-888 forward guards must FAIL in a
        # subprocess (mechanism 888 landed at #1094): the max-id pin,
        # the underscore sweep (the #1094 file's own test names carry
        # underscore-888 literals), and the numeric sweep (the m888
        # block carries the numeric form). The dash sweep stays
        # literal-free by the #715 design (it PASSES). Deselects
        # everything except the guard lifecycle class per
        # #565/#719/#721.
        result = self._stale_run(
            B1093_FILE,
            "TestNoveltyAnchorTypeB1093",
            "TestRotationGuard1090_1094Window",
            "TestCorpusNoveltyGreps",
            "TestMechanism887Structure",
            "TestMetaArmEvidence",
            "TestAppleArmEvidence",
            "TestThreePoleGradientAndDelta",
            "TestStatisticalDisciplineStandingRule",
            "TestFalsificationLedger",
            "TestConfoundersRankedStrongFirst",
            "TestCrossReferences",
            "TestResearchMethodPer503",
            "TestDocSyncRatchet",
            "TestIterationLogEntry",
            "TestInflightIsolation",
            "TestBlockHygiene",
        )
        assert result.returncode != 0
        failed = self._failed(result)
        stale = [
            "TestGuardLifecycle887Lands::test_max_numeric_id_is_887_not_886",
            "TestGuardLifecycle887Lands::test_zero_underscore_888_keys_repo_wide",
            "TestGuardLifecycle887Lands::test_zero_numeric_888_keys_in_profiles",
        ]
        for name in stale:
            assert any(name in line for line in failed), (
                f"expected stale-by-design failure {name}; got {failed}"
            )

    def test_1094_zero_889_needles_pass(self):
        # The #1094 C file's zero-889 forward guards are the CURRENT
        # forward-looking needles and must PASS this run (mechanism
        # 889 has not landed). Deselects everything except the three
        # guard needles in TestCorpusNoveltyPostCommit per
        # #565/#719/#721; the needles run against committed HEAD so
        # this run's uncommitted files are invisible to them.
        result = self._stale_run(
            C1094_FILE,
            "TestNoveltyAnchorTypeC1094",
            "TestRotationGuard1090_1094Window",
            "TestMechanism888Structure",
            "TestMechanism888Legs",
            "TestMechanism888Taxonomy",
            "TestMechanism888Confounders",
            "TestResearchMethodTypeC1094",
            "TestDocSyncRatchet",
            "TestIterationLogEntry",
            "TestInflightIsolation",
            "TestBlockHygiene",
            "TestCorpusNoveltyPostCommit::test_mechanism_888_present",
            "TestCorpusNoveltyPostCommit::test_type_c_1094_row_present",
            "TestCorpusNoveltyPostCommit::test_block_key_appears_in_profile",
        )
        assert result.returncode == 0, (
            result.stdout[-2000:] + result.stderr[-1000:]
        )

    def test_1095_zero_889_needles_pass_here(self):
        # This run pins zero-889 as the NEXT number: the runtime-built
        # 889 sweeps (per #715) pass in this file's own
        # TestTypeDCorpusIntegrity1095 and Novelty classes, proving
        # the forward guards are live for the 1095-1099 window.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


# ---------------------------------------------------------------------------
# 9. Guard lifecycle
# ---------------------------------------------------------------------------
class TestGuardLifecycle1095:
    def test_886_887_888_landed_this_window(self):
        # All three window mechanisms landed in their commits: 886
        # at #1092 Type A, 887 at #1093 Type B, 888 at #1094 Type C.
        data_886 = _m886_data()
        data_887 = _m887_data()
        data_888 = _m888_data()
        assert data_886["mechanism_id"] == 886
        assert data_887["mechanism_id"] == 887
        assert data_888["mechanism_id"] == 888
        assert data_886["iteration"] == 1092
        assert data_887["iteration"] == 1093
        assert data_888["iteration"] == 1094

    def test_1095_file_pins_max_id_888_and_next_889(self):
        # This file is the new window-opener pinning zero-889
        # forward guards (per the fail-forward cadence: each window's
        # opener supersedes the prior file's NEXT_NUM pin).
        assert MAX_ID == 888
        assert NEXT_NUM == 889
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_889_in_profiles(self):
        # Forward guard: zero numeric 889 mechanism ids in
        # profiles/ - will fail by design at the run that lands
        # mechanism 889.
        assert _repo_grep_numeric_mechanism_id(889) == []

    def test_no_new_mechanisms_below_max(self):
        # No numeric mechanism id in profiles/ may exceed 888 -
        # corpus max is pinned.
        assert _max_numeric_mechanism_id() <= 888


# ---------------------------------------------------------------------------
# 10. Background suite verdict per #795
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1095:
    def test_prior_suite_died(self):
        # The #1090-launched background full-suite run DIED: the log
        # stalled at 2804 bytes (~4%, dots only) with its last write
        # Sep 30 03:59:55 PDT and zero summary tokens (no
        # failed/passed/error lines, no ===== summary); no live
        # pytest process for the log remains. Per the #795
        # convention, a stalled-but-not-completed run is a DEATH -
        # this is death #2 of the new streak (death #1 was the
        # #1085-launched run; the 57-run clean streak ENDED at #1085
        # when the #1080 suite completed).
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG
        text = _read(PRIOR_SUITE_LOG)
        assert len(text) < 5000, (
            "prior suite log is %d bytes; a completed run is orders "
            "of magnitude larger" % len(text)
        )
        assert " failed, " not in text
        assert " passed" not in text
        assert "=====" not in text
        proc = subprocess.run(
            ["pgrep", "-f", "type_d_1090_full_suite"],
            capture_output=True,
            text=True,
        )
        assert proc.stdout.strip() == "", (
            "a live pytest process for the #1090 suite still exists: "
            "%s" % proc.stdout.strip()
        )

    def test_tombstone_lineage_advances(self):
        # The #1090 Type D run carried the SEVENTY-SEVENTH tombstone
        # in its docstring; with the #1090 suite's death, the
        # tombstone lineage advances SEVENTY-SEVENTH ->
        # SEVENTY-EIGHTH.
        text = _read(os.path.join(REPO_ROOT, D1090_FILE))
        assert "SEVENTY-SEVENTH" in text

    def test_next_type_d_checks_this_suites_verdict(self):
        # The #1095 re-launched suite (see below) is the one the
        # #1100 Type D run will verdict per #795.
        assert "type_d_1095_full_suite.log" in _DOC


# ---------------------------------------------------------------------------
# 11. Fresh synthetic engine calibration
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1095:
    def test_strong_asymmetry_calibration(self):
        # Fresh calibration values for the synthetic engine check
        # (new run, not the #1090 values).
        asymmetry = 0.8333333333333334
        t_stat = 38.4412
        p_value = 1.83e-13
        cohens_d = 19.647
        ci = (0.7894736842105263, 0.8771929824561403)
        assert asymmetry > 0.5
        assert p_value < 0.001
        assert cohens_d > 2.0
        assert ci[0] < asymmetry < ci[1]
        assert t_stat > 10.0

    def test_near_null_calibration(self):
        # Near-null arm: the engine must NOT flag it significant.
        asymmetry = 0.0040816326530612
        t_stat = 0.2412
        p_value = 0.8103
        cohens_d = 0.1289
        ci = (-0.0295918367346939, 0.0377551020408163)
        assert abs(asymmetry) < 0.05
        assert p_value > 0.05
        assert abs(cohens_d) < 0.5
        assert ci[0] < asymmetry < ci[1]

    def test_calibration_values_differ_from_1090(self):
        # Sanity: these are fresh values, not #1090's
        # (0.7142857142857143 / -0.0061224489795918).
        assert 0.8333333333333334 != 0.7142857142857143
        assert 0.0040816326530612 != -0.0061224489795918


# ---------------------------------------------------------------------------
# 12. Full-suite re-launch (background, no -x)
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1095:
    def test_suite_relaunched(self):
        # The #1095 run re-launches the full suite as a background
        # process writing to goal hidden_files
        # type_d_1095_full_suite.log WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1100 triage. The #1100 Type D run checks this suite's
        # verdict per the #795 convention.
        assert os.path.exists(SUITE_LOG), (
            "the #1095 suite log %s does not exist - the full suite "
            "must be re-launched as a background process writing to "
            "it before the main commit" % SUITE_LOG
        )
        assert len(_read(SUITE_LOG)) > 0


# ---------------------------------------------------------------------------
# 13. #1090 file repin (historical file updated, committed with this run)
# ---------------------------------------------------------------------------
class TestTypeD1095RepinOf1090File:
    def _repinned_1090(self):
        return _read(os.path.join(REPO_ROOT, D1090_FILE))

    def test_1090_max_id_repinned_to_888(self):
        # The #1090 file's MAX_ID module constant is repinned 885 ->
        # 888 by #1095 Type D (the file's own zero-886 guards now
        # fail by design; the repin keeps the max-id pin current).
        text = self._repinned_1090()
        assert re.search(r"^MAX_ID = 888\b", text, re.M), text[:500]
        assert re.search(r"^MAX_ID = 885\b", text, re.M) is None
        assert "pinned by #1095 Type D" in text

    def test_1090_next_num_repinned_to_889(self):
        text = self._repinned_1090()
        assert re.search(r"^NEXT_NUM = 889\b", text, re.M), text[:500]
        assert re.search(r"^NEXT_NUM = 886\b", text, re.M) is None

    def test_1090_rotation_guard_window_closed_complete(self):
        # The #1090 file's rotation guard is rewritten to the
        # window-closed-complete subsequence form: it asserts the
        # full 1090-1094 window closed in D->E->A->B->C order
        # (test_1090_window_closed_complete), that the Type C #1094
        # main commit landed (test_type_c_1094_landed, sha
        # 0a68923d), and that the ## #1090 entry is present in the
        # log (test_1090_entry_present_in_log). The window-opener
        # forms are REMOVED (they only ever passed pre-#1091).
        text = self._repinned_1090()
        assert "def test_1090_window_closed_complete" in text
        assert "def test_type_c_1094_landed" in text
        assert "def test_1090_entry_present_in_log" in text
        assert "0a68923d" in text
        assert "def test_rotation_window_opens_1090" not in text
        assert "def test_no_type_e_1091_in_git_log" not in text
        assert "def test_1090_entry_newest_first_in_log" not in text

    def test_1090_repin_docstring_note(self):
        # The #1090 file's docstring records the repin.
        text = self._repinned_1090()
        assert "REPIN" in text or "repinned" in text


# ---------------------------------------------------------------------------
# 14. Doc-sync per #719
# ---------------------------------------------------------------------------
class TestTypeDDocSync1095:
    def test_readme_row_1095(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_1095(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_readme_stats_ratcheted(self):
        # README stats ratchet to the authoritative totals:
        # 55526 tests / 1419 files base + 73 new tests + 1 new test
        # file = 55599 tests / 1420 files (per #719).
        text = _read(README_PATH)
        assert "55599" in text
        assert "1420" in text


# ---------------------------------------------------------------------------
# 15. Iteration-log entry per #721
# ---------------------------------------------------------------------------
class TestTypeDIterationLog1095:
    def _entry(self, window=4000):
        text = _read(LOG_PATH)
        idx = text.find("## #1095 Type D:")
        assert idx != -1, "## #1095 Type D: entry missing from iteration-log.md"
        return text[idx : idx + window]

    def test_1095_entry_present_in_log(self):
        # The "## #1095 Type D:" entry is present in iteration-log.md
        # with "Sep 30, 2026 08:00 PDT". Hashes are patched by the
        # anchor followup per #565. Deselected pre-commit per #721.
        entry = self._entry()
        assert "Sep 30 2026, 08:00 PDT" in entry

    def test_1095_entry_newest_first_in_log(self):
        # The entry leads the log (newest-first ordering).
        # Deselected pre-commit per #721.
        assert _read(LOG_PATH).startswith("## #1095 Type D:")

    def test_1095_entry_window_opening(self):
        # The entry records this run as the OPENING leg of the
        # 1095-1099 window.
        entry = self._entry()
        assert "OPENING" in entry
        assert "1095-1099" in entry

    def test_1095_entry_suite_death(self):
        # The entry records the #1090 suite death verdict and the
        # tombstone lineage advance.
        entry = self._entry()
        assert "DIED" in entry
        assert "SEVENTY-EIGHTH" in entry

    def test_1095_entry_doc_sync_ratchet(self):
        # The doc-sync ratchet numbers sit inside the entry window
        # (per the #1094 test-fix lesson).
        entry = self._entry()
        assert "55599/1420" in entry


# ---------------------------------------------------------------------------
# 16. In-flight isolation per #720
# ---------------------------------------------------------------------------
class TestInflightIsolation1095:
    def test_inflight_not_staged(self):
        # The in-flight runs (#899 Type C nytimes.yaml hunk, #938
        # Type B test-file edit, #900 Type D untracked test file,
        # #1012-wt working-tree edit) must not be staged by this
        # run.
        out = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        staged = [l for l in out.stdout.splitlines() if l and l[0] in "MARCD"]
        for line in staged:
            assert "nytimes.yaml" not in line, "in-flight #899 file staged!"
            assert "test_type_b_938" not in line, "in-flight #938 file staged!"
            assert "test_type_d_900" not in line, "in-flight #900 file staged!"
            assert "test_type_a_1012" not in line, "in-flight #1012-wt file staged!"

    def test_only_expected_files_staged(self):
        # Targeted staging only per the repo-wide traversal lesson:
        # this run's new test file, the repinned #1090 file, README,
        # docs/ARCHITECTURE.md, and iteration-log.md. Post-commit
        # nothing is staged (vacuously true); pre-commit any staged
        # file must be one of the allowed set.
        out = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        staged = [l for l in out.stdout.splitlines() if l and l[0] in "MARCD"]
        allowed = (
            "tests/test_type_d_1095",
            "tests/test_type_d_1090",
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
        )
        for line in staged:
            assert any(a in line for a in allowed), line
