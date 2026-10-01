"""Type D -- Iteration #1120 (Thu 2026-10-01 09:00 PDT): m901/m902/m903
qualitative-discipline verification + post-1115-1119 corpus integrity
(max numeric mechanism_id 903; zero next-number 904 keys in
numeric/underscore/dash mechanism forms - the 904 needles are
format-built per #715 so no guard-literal carrier file exists; the
m901/m902/m903 block keys carry no mechanism-number substring
(designed keying), so they are plain literals; the #1117/#1118/#1119
window files are NOT edited by this run - their now-stale
forward-looking pins are recorded as fail-by-design via subprocess in
the staleness class (#1115's max-900 and zero-901 pins trip on the
landed 901/902/903; #1115's no-thirty-first-direction pin trips on
the landed THIRTY-FIRST direction; #1116's staleness pins flip on
#1115's guard lifecycle; #1115's own forward-looking staleness flips
on the ledger-41 pin; #1119's zero-904 guards and no-thirty-second-
direction guard STAY GREEN; #1119's TestSupersessionPins1119 and
#1118's/#1117's TestSupersessionPins classes STAY GREEN); ledger
holds at 43 with the FORTY-THIRD member-claim form present in
exactly one profiles file (careers/journalists.yaml, m902 block)
and the forty-fourth member-claim form absent profiles-wide (needle
format-built per #715); the THIRTY-FIRST relationship direction is
present in competitor-entities.yaml (m903 GEOGRAPHIC-PORTFOLIO
EXPANSION); the thirty-second relationship-direction claim form is
absent repo-wide (needle format-built per #715)) + the #1115
background-suite verdict (DIED at 1621 bytes / 1461 dots ~2% with
last write Oct 1 11:35:23 UTC and zero summary tokens, no live
pytest process - SEVENTH consecutive background-suite death of the
new streak; the 57-run streak ENDED at #1085 when the #1080 suite
completed; tombstone lineage advances EIGHTY-SECOND -> EIGHTY-
THIRD) + fresh synthetic engine calibration (new values, not
#1115's) + re-launch of the full suite as a background process
writing to goal hidden_files type_d_1120_full_suite.log WITHOUT -x
(the full inventory, calendar by-design failures included, is needed
for the #1125 triage; the next Type D run checks its verdict per
the #795 convention).

Type D FIRST leg of the 1120-1124 window, OPENING it
(D->E->A->B->C). Committed predecessor #1119 Type C (08:00 PDT Oct 1)
CLOSED the 1115-1119 window (D #1115, E #1116, A #1117, B #1118,
C #1119). Rotation per the #565 anchor + rotation guard.
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
rotation schedule, not commit order. Do NOT touch #1024's m846
(FOURTEENTH, exclusionary-diversion): self-flagged
sourcing-constraint violation; Ray's revert/leave/rebuild-from-primary
decision still pending.

Verifies:
- m901 (Type A #1117, financial-times.yaml 4-space block key,
  `mechanism_id: 901` field form; block key count 2 - colon-form
  line + test_file field, designed - no block_key field in the m901
  block): FT x OpenAI Sep-30 FTC agent-safety probe coverage
  (regulatory-enforcement register, -0.35 MANUAL ILLUSTRATIVE)
  vs carried FT x Meta arms (m625 +0.05, m823 +0.20, mean +0.125,
  un-rescored per #807). Illustrative delta (OpenAI minus Meta)
  -0.475: the uniform payer-softening prediction (FT-OpenAI $5-10M/yr
  licensing, Apr 29 2024) FAILS on the enforcement peg; the FT
  routes the regulator's product-safety probe onto the deal partner
  with no delay or softening (relay-attested via runtimewire +
  archynetys, 0 browser.open per #503). FORTY-SECOND
  falsification-family member; ledger 41->42. FIRST
  regulatory-enforcement-register falsification at FT.
- m902 (Type B #1118, journalists.yaml 4-space block key under
  Gerrit De Vynck competitor_coverage, `mechanism_id: 902` field
  form; block key count 3 - colon-form line + block_key field +
  test_file field, designed): De Vynck (WaPo) Sep-26 OpenAI
  federal-websites probe (-0.45 MANUAL ILLUSTRATIVE, beSpacific +
  Muck Rack relay-attested, 0 browser.open per #503) vs carried
  Meta arms (Facebook Papers 2021-10 adversarial_investigation,
  midterms 2025-12 political_power_adversarial, layoffs 2022-11
  stress_narrative - framing labels only, un-rescored per #807).
  The m569 "OpenAI: softer" directional prediction (WaPo x OpenAI
  Apr 22 2025 strategic partnership) FAILS at the journalist level:
  the softening gradient is null (both registers adversarial).
  FORTY-THIRD falsification-family member; ledger 42->43. FIRST
  Washington Post member of the current ordinal falsification line.
- m903 (Type C #1119, competitor-entities.yaml zero-indent block
  key, `mechanism_id: 903` field form; block key count 2 -
  colon-form line + block_key field, designed): Microsoft x Nine
  Entertainment Jul-3-2026 first-APAC news licensing deal
  (Copilot grounding rights across AFR/SMH/Age/Brisbane Times,
  terms undisclosed) - GEOGRAPHIC-PORTFOLIO EXPANSION as the
  THIRTY-FIRST relationship direction (lab opens a new geographic
  market via a first-of-its-kind deal with the region's dominant
  publisher, in the shadow of Australia's News Bargaining
  Incentive; Microsoft NOT subject to the Code or incentive).
  Tone NOT_SCORED per the Aug 28 2026 standing rule. NOT a
  falsification-family member; ledger holds at 43, forty-fourth
  member-claim absent.

All three: MANUAL/QUALITATIVE ONLY, engine NOT run,
no analysis.json update, NOT artifact-grade, verdict
directionally_supported_not_proven. Correlation is not causation;
hypothesis-generating only.
"""

import glob
import os
import re
import subprocess

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
OWN_BASENAME = (
    "test_type_d_1120_m901_m902_m903_qualitative_corpus_"
    "integrity_oct01_9am.py"
)

MAX_ID = 903
NEXT_NUM = 904

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "69728626"

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 58257
README_FILE_COUNT = 1444

# The m901/m902/m903 block keys carry no mechanism-number substring
# (designed keying), so they are plain literals per #715.
M901_KEY = (
    "type_a_1117_ft_openai_ftc_agent_safety_probe_vs_"
    "carried_meta_arms_oct01_6am"
)
M901_INDENT = 4
M901_HOME = "profiles/financial-times.yaml"
M902_KEY = (
    "type_b_1118_gerrit_de_vynck_wapo_openai_federal_websites_"
    "probe_vs_meta_carried_arms_sep2026"
)
M902_INDENT = 4
M902_HOME = "profiles/careers/journalists.yaml"
M903_KEY = (
    "type_c_1119_microsoft_nine_entertainment_first_apac_news_"
    "deal_geographic_portfolio_expansion_thirty_first_"
    "direction_oct01_8am"
)
M903_INDENT = 0
M903_HOME = "profiles/competitor-entities.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1120_full_suite.log"
)
PRIOR_SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1115_full_suite.log"
)
A1117_FILE = (
    "tests/test_type_a_1117_ft_openai_ftc_agent_safety_probe_vs_"
    "carried_meta_arms_oct01_6am.py"
)
B1118_FILE = (
    "tests/test_type_b_1118_gerrit_de_vynck_wapo_openai_"
    "federal_websites_probe_vs_meta_carried_arms_sep2026_7am.py"
)
C1119_FILE = (
    "tests/test_type_c_1119_microsoft_nine_entertainment_"
    "first_apac_news_deal_geographic_portfolio_expansion_"
    "thirty_first_direction_oct01_8am.py"
)
E1116_FILE = (
    "tests/test_type_e_1116_podcast_sentiment_146th_"
    "verification_oct01_5am.py"
)
D1115_FILE = (
    "tests/test_type_d_1115_m898_m899_m900_qualitative_"
    "corpus_integrity_oct01_4am.py"
)

_DOC = __doc__

# The forty-fourth-member and thirty-second-direction needles are
# fragment-built per #715 so this file carries no contiguous literal
# of a forward-guard claim form. The landed FORTY-THIRD member and
# THIRTY-FIRST direction forms are plain literals (already in corpus).
_T43 = "FORTY-THIRD falsification-family member"
_TW31 = "THIRTY-FIRST relationship direction"
_T44 = "FORTY-" + "FOURTH falsification-family member"
_TW32 = "THIRTY-" + "SECOND relationship direction"


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
# numbers in git history: #1120 Type D opens the 1120-1124 window;
# #1119 Type C (committed 08:00 PDT Oct 1) is the schedule
# predecessor and CLOSED the 1115-1119 window. The in-flight runs
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
    file carries a contiguous 904-form mechanism literal (verified
    pre-commit), so the 904 sweeps run repo-wide with only this file
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


def _m901_data():
    return _block_data(M901_HOME, M901_KEY, M901_INDENT)


def _m902_data():
    return _block_data(M902_HOME, M902_KEY, M902_INDENT)


def _m903_data():
    return _block_data(M903_HOME, M903_KEY, M903_INDENT)


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1120:
    def test_no_type_d_1120_test_file_preexisting(self):
        files = glob.glob(
            os.path.join(TESTS_DIR, "test_type_d_1120*.py")
        )
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_no_type_d_1120_in_git_log(self):
        # Pre-commit novelty guard: no commit may already claim this slot.
        # SUPERSEDED BY DESIGN once this run's main commit ("Type D #1120:")
        # lands; post-commit, TestTypeDRotationGuard1120 asserts the anchor
        # and window instead. Deselect this test in post-commit full runs.
        log = _git("log", "--format=%s", "--grep=Type D #1120")
        assert "Type D #1120" not in log

    def test_max_id_is_903(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_904_numeric_forms_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        # m901: colon-form line + test_file field (count 2, designed -
        # no block_key field in the m901 block). m902: colon-form line
        # + block_key field + test_file field (count 3, designed).
        # m903: colon-form line + block_key field (count 2, designed).
        ft = _read(os.path.join(REPO_ROOT, M901_HOME))
        assert ft.count(M901_KEY) == 2, ft.count(M901_KEY)
        jou = _read(os.path.join(REPO_ROOT, M902_HOME))
        assert jou.count(M902_KEY) == 3, jou.count(M902_KEY)
        ent = _read(os.path.join(REPO_ROOT, M903_HOME))
        assert ent.count(M903_KEY) == 2, ent.count(M903_KEY)


# ---------------------------------------------------------------------------
# 2. Rotation guard (2 tests deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1120:
    def test_rotation_window_opens_1120(self):
        # FIRST leg of the 1120-1124 window, OPENING it (per #565:
        # D #1120 -> E #1121 -> A #1122 -> B #1123 -> C #1124).
        # Deselected pre-commit (this run's main commit is not yet
        # in history); passes post-commit.
        w = _window()
        assert w[0] == ("D", "1120"), w
        # Newest-first distinct sequence: D #1120 (this run) opens
        # the window after the closed 1115-1119 window (C #1119,
        # B #1118, A #1117, E #1116).
        assert [t for t, _ in w[:5]] == ["D", "C", "B", "A", "E"], w

    def test_predecessor_1119_chain_present(self):
        # #1119 Type C CLOSED the 1115-1119 window; its main/anchor/
        # log-hash chain must be in history before this run commits.
        log = _git("log", "--format=%H %s")
        assert "5ca5ef2b" in log
        assert "c035336a" in log
        assert "3f792914" in log

    def test_no_type_e_1121_in_git_log(self):
        log = _git("log", "--format=%s", "--grep=Type E #1121")
        assert "Type E #1121" not in log

    def test_anchor_sha_is_real(self):
        # Patched post-main-commit by the anchor followup per #565.
        # Deselected pre-commit (placeholder by design); passes
        # post-patch.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40


# ---------------------------------------------------------------------------
# 2b. Novelty anchor (1 test, deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1120:
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1120
        # commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type D #1120")
        assert "Type D #1120" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1120:
    def test_m901_block_present_in_financial_times_yaml(self):
        data = _m901_data()
        assert data["mechanism_id"] == 901

    def test_m902_block_present_in_journalists_yaml(self):
        data = _m902_data()
        assert data["mechanism_id"] == 902

    def test_m903_block_present_in_competitor_entities_yaml(self):
        data = _m903_data()
        assert data["mechanism_id"] == 903

    def test_max_mechanism_id_is_903(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_904_forms_repo_wide(self):
        # Forward guard: zero numeric/underscore/dash 904 keys -
        # will fail by design at the run that lands mechanism 904.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_m901_key_count_is_designed(self):
        # Colon-form key line + test_file field value: exactly 2,
        # no block_key field, no other carrier.
        text = _read(os.path.join(REPO_ROOT, M901_HOME))
        lines = [
            l
            for l in text.splitlines()
            if M901_KEY in l
        ]
        assert len(lines) == 2, lines
        assert lines[0].strip() == M901_KEY + ":"
        assert "test_file:" in lines[1]

    def test_m902_key_count_is_designed(self):
        # Colon-form key line + block_key field + test_file field:
        # exactly 3, no other carrier.
        text = _read(os.path.join(REPO_ROOT, M902_HOME))
        lines = [
            l
            for l in text.splitlines()
            if M902_KEY in l
        ]
        assert len(lines) == 3, lines
        assert lines[0].strip() == M902_KEY + ":"
        assert "block_key:" in lines[1]
        assert "test_file:" in lines[2]

    def test_m903_key_count_is_designed(self):
        # Colon-form key line + block_key field value: exactly 2,
        # no other carrier.
        text = _read(os.path.join(REPO_ROOT, M903_HOME))
        lines = [
            l
            for l in text.splitlines()
            if M903_KEY in l
        ]
        assert len(lines) == 2, lines
        assert lines[0].strip() == M903_KEY + ":"
        assert "block_key:" in lines[1]


# ---------------------------------------------------------------------------
# 4. m901 qualitative discipline (Type A #1117)
# ---------------------------------------------------------------------------
class TestTypeDM901QualitativeDiscipline:
    def test_m901_run_metadata(self):
        data = _m901_data()
        assert data["mechanism_id"] == 901
        assert data["iteration"] == 1117
        assert data["hour_type"] == "A"
        assert data["date"] == "2026-10-01 06:00 PDT"
        assert "1115-1119" in data["window"]

    def test_m901_falsification_membership(self):
        data = _m901_data()
        assert data["falsification_family_member"] is True
        assert data["falsification_ledger"] == 42
        assert "FORTY-SECOND" in data["ledger_note"]
        assert "41->42" in data["ledger_note"]
        # The negative-guard wording for the next slot is the
        # designed member-claim form, not the claim form itself.
        assert _T43 not in data["ledger_note"]

    def test_m901_openai_arm(self):
        data = _m901_data()
        arm = data["openai_arm"]
        assert arm["tone"] == -0.35
        assert "MANUAL ILLUSTRATIVE" in arm["tone_basis"]
        assert "regulatory-enforcement" in arm["register"]

    def test_m901_carried_meta_arms(self):
        data = _m901_data()
        carried = data["meta_arms_carried"]
        assert carried["meta_mean"] == 0.125
        mechs = [a["mechanism"] for a in carried["arms"]]
        assert mechs == [625, 823]
        for a in carried["arms"]:
            assert "un-rescored per #807" in a["basis"]

    def test_m901_scorer_discipline(self):
        data = _m901_data()
        scorer = data["scorer"]
        assert scorer["openai_tone"] == -0.35
        assert scorer["meta_mean_tone"] == 0.125
        assert scorer["illustrative_delta_openai_minus_meta"] == -0.475
        assert "MANUAL ILLUSTRATIVE ONLY" in scorer["method"]
        assert "engine NOT run" in scorer["method"]

    def test_m901_financial_relationship_fails(self):
        data = _m901_data()
        fin = data["financial_relationship"]
        assert "Apr 29 2024" in fin["deal"]
        assert "softer" in fin["coverage_prediction"]
        assert "FAILS" in fin["result"]

    def test_m901_statistical_discipline(self):
        data = _m901_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        disc = data["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in disc
        assert "NOT_CALCULATED" in disc
        assert "NOT artifact-grade" in disc
        assert "no_analysis_json_update true" in disc

    def test_m901_confounder_and_counterevidence_disclosure(self):
        data = _m901_data()
        assert len(data["confounders"]) >= 4
        assert any("STRONG" in c for c in data["confounders"])
        assert len(data["counter_evidence"]) >= 3

    def test_m901_research_method_and_sources(self):
        data = _m901_data()
        assert "5 browser.search query sets" in data["research_method"]
        assert "0 browser.open" in data["research_method"]
        assert "ASCII-only" in data["research_method"]
        assert len(data["source_urls"]) == 2
        assert data["test_file"].endswith("_oct01_6am.py")
        assert 625 in data["connects_to"] and 898 in data["connects_to"]


# ---------------------------------------------------------------------------
# 5. m902 qualitative discipline (Type B #1118)
# ---------------------------------------------------------------------------
class TestTypeDM902QualitativeDiscipline:
    def test_m902_run_metadata(self):
        data = _m902_data()
        assert data["mechanism_id"] == 902
        assert data["iteration"] == 1118
        assert data["hour_type"] == "B"
        assert data["date"] == "2026-10-01 07:00 PDT"
        assert data["journalist"] == "Gerrit De Vynck"
        assert data["publication"] == "washington-post"
        assert "1115-1119" in data["window"]

    def test_m902_falsification_membership(self):
        data = _m902_data()
        assert data["falsification_family_member"] is True
        assert data["falsification_ledger"] == 43
        assert "FORTY-THIRD" in data["ledger_note"]
        assert "42->43" in data["ledger_note"]
        assert "FIRST Washington Post member" in data["ledger_note"]

    def test_m902_openai_arm(self):
        data = _m902_data()
        arm = data["openai_arm"]
        assert arm["date"] == "2026-09-26"
        assert arm["tone"] == -0.45
        assert "MANUAL ILLUSTRATIVE" in arm["tone_basis"]
        assert "adversarial safety/incident" in arm["register"]

    def test_m902_carried_meta_arms_unrescored(self):
        data = _m902_data()
        assert "un-rescored per #807" in data["meta_arms_carried"]["basis"]
        items = [a["item"] for a in data["meta_arms_carried"]["arms"]]
        assert len(items) == 3
        framings = [a["framing"] for a in data["meta_arms_carried"]["arms"]]
        assert "adversarial_investigation" in framings

    def test_m902_scorer_discipline(self):
        data = _m902_data()
        scorer = data["scorer"]
        assert scorer["openai_tone"] == -0.45
        assert "null gradient" in scorer["illustrative_delta_openai_minus_meta"]
        assert "MANUAL ILLUSTRATIVE ONLY" in scorer["method"]
        assert "engine NOT run" in scorer["method"]
        assert "NOT_CALCULATED" in scorer["method"]

    def test_m902_financial_relationship_fails(self):
        data = _m902_data()
        fin = data["financial_relationship"]
        assert "Apr 22 2025" in fin["deal"]
        assert "softer" in fin["coverage_prediction"]
        assert "FAILS" in fin["result"]

    def test_m902_confounder_and_counterevidence_disclosure(self):
        data = _m902_data()
        assert len(data["confounders"]) >= 4
        assert any("STRONG" in c for c in data["confounders"])
        assert any("MODERATE" in c for c in data["confounders"])
        assert len(data["counterevidence"]) >= 2

    def test_m902_research_method_and_sources(self):
        data = _m902_data()
        assert "5 browser.search query sets" in data["research_method"]
        assert "0 browser.open" in data["research_method"]
        assert len(data["source_urls"]) == 2
        assert "FIRST dedicated Type B mechanism on Gerrit De Vynck" in data[
            "novelty"
        ]
        assert data["verdict"] == "directionally_supported_not_proven"


# ---------------------------------------------------------------------------
# 6. m903 qualitative discipline (Type C #1119)
# ---------------------------------------------------------------------------
class TestTypeDM903QualitativeDiscipline:
    def test_m903_run_metadata(self):
        data = _m903_data()
        assert data["mechanism_id"] == 903
        assert data["iteration"] == 1119
        assert data["iteration_type"] == "C"
        assert data["iteration_time"] == "2026-10-01 08:00 PDT"

    def test_m903_thirty_first_direction_taxonomy(self):
        data = _m903_data()
        assert _TW31 in data["mechanism_name"]
        assert "GEOGRAPHIC-PORTFOLIO EXPANSION" in data[
            "relationship_direction_taxonomy"
        ]
        assert "m900" in data["relationship_direction_taxonomy"]
        assert "Falsifiable" in data["relationship_direction_taxonomy"]

    def test_m903_not_falsification_member(self):
        data = _m903_data()
        assert data["falsification_family_member"] is False
        assert "ledger holds at 43" in data["falsification_family"]

    def test_m903_statistical_discipline(self):
        data = _m903_data()
        assert data["tone_scored"] is False
        assert data["engine_run"] is False
        assert data["is_significant"] is False
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False

    def test_m903_confounder_disclosure(self):
        data = _m903_data()
        confs = data["confounders"]
        assert len(confs) >= 4
        strengths = [c["strength"] for c in confs]
        assert "STRONG" in strengths
        assert "MEDIUM" in strengths
        assert any("counterargument" in c for c in confs)

    def test_m903_sources_and_novelty(self):
        data = _m903_data()
        assert len(data["sources"]) == 5
        assert all(s.get("novel") is True for s in data["sources"])
        assert "FIRST dedicated corpus mechanism" in data["novelty"]
        assert data["connects_to"] == [437, 672, 834, 636]

    def test_m903_yaml_hygiene(self):
        data = _m903_data()
        assert data["yaml_parse_clean"] is True
        assert data["ascii_only"] is True
        assert "terms undisclosed" in data["money_flow"] or "undisclosed" in data[
            "money_flow"
        ].lower()


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 43)
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1120:
    def _profiles_text(self):
        parts = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                parts.append(
                    (
                        os.path.join(root, f),
                        open(
                            os.path.join(root, f),
                            encoding="utf-8",
                            errors="replace",
                        ).read(),
                    )
                )
        return parts

    def test_forty_third_claim_in_exactly_one_profiles_file(self):
        hits = [
            p for p, t in self._profiles_text() if _T43 in t
        ]
        assert len(hits) == 1, hits
        assert hits[0].endswith("careers/journalists.yaml"), hits

    def test_forty_third_claim_count_is_designed(self):
        # The m902 block carries the claim in the ledger_note line
        # and the finding line's self-reference (2 occurrences, 1
        # block - the #1113/#1118 designed pattern).
        text = _read(os.path.join(REPO_ROOT, M902_HOME))
        assert text.count(_T43) == 2, text.count(_T43)

    def test_no_forty_fourth_member_claim_profiles_wide(self):
        # The next falsification slot must be unclaimed profiles-wide
        # (needle format-built per #715; designed negative-guard
        # wordings do not carry the claim form).
        for p, t in self._profiles_text():
            assert _T44 not in t, p

    def test_m901_m902_ledger_sequence_carried(self):
        d901 = _m901_data()
        d902 = _m902_data()
        assert d901["falsification_ledger"] == 42
        assert d902["falsification_ledger"] == 43

    def test_m903_holds_ledger_at_43(self):
        d903 = _m903_data()
        assert d903["falsification_family_member"] is False
        assert "ledger holds at 43" in d903["falsification_family"]


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (subprocess pins on prior window files)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1120:
    def _stale_run(self, path, node=None, *deselects):
        target = path if node is None else "%s::%s" % (path, node)
        cmd = [
            ".venv/bin/python",
            "-m",
            "pytest",
            target,
            "-q",
            "--no-header",
            "-p",
            "no:cacheprovider",
            "-o",
            "addopts=",
        ]
        for d in deselects:
            cmd.extend(["--deselect", "%s::%s" % (path, d)])
        result = subprocess.run(
            cmd, cwd=REPO_ROOT, capture_output=True, text=True, timeout=900
        )
        return result

    def test_1115_guard_lifecycle_stale_by_design(self):
        # #1115's TestGuardLifecycle1115 pinned max 900, zero-901
        # (numeric/underscore/dash), no-thirty-first-direction and
        # no-forty-second-member. The #1117 (901), #1118 (902,
        # FORTY-THIRD) and #1119 (903, THIRTY-FIRST) landings trip
        # the numeric, max, thirty-first and forty-second pins.
        # Designed lifecycle; recorded, not repaired.
        result = self._stale_run(D1115_FILE, "TestGuardLifecycle1115")
        assert result.returncode != 0, result.stdout[-2000:]
        assert "901" in result.stdout or "900" in result.stdout

    def test_1116_staleness_pins_stale_by_design(self):
        # #1116's TestStalenessPins pinned #1115 TestGuardLifecycle1115
        # still PASS and #1114 zero-901 still PASS; both flip at the
        # 901 landing. Designed lifecycle; recorded, not repaired.
        result = self._stale_run(E1116_FILE, "TestStalenessPins")
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1115_forward_looking_staleness_flips_by_design(self):
        # #1115's TestTypeDForwardLookingStaleness1115 pinned
        # test_1113_ledger_41_class_still_green and
        # test_1114_forward_guards_901_still_green: the #1117/#1118
        # landings (FORTY-SECOND/FORTY-THIRD members, mechanism 901)
        # flip both at #1120. Designed lifecycle; recorded, not
        # repaired.
        result = self._stale_run(
            D1115_FILE, "TestTypeDForwardLookingStaleness1115"
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1119_zero_904_forward_guards_still_green(self):
        # #1119's TestForwardGuards1119 pins zero-904
        # (numeric/underscore/dash): 904 unlanded, all green at #1120.
        result = self._stale_run(C1119_FILE, "TestForwardGuards1119")
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1119_supersession_pins_still_green(self):
        # #1119's TestSupersessionPins1119 records the designed
        # end-states of the #1118 zero-903 numeric guard, the #1115
        # no-thirty-first-direction guard and the #1118 forty-fourth
        # absent guard: all pins hold at #1120.
        result = self._stale_run(C1119_FILE, "TestSupersessionPins1119")
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1118_supersession_pins_still_green(self):
        # #1118's TestSupersessionPins1118 records the designed
        # end-states of the #1117 zero-902 numeric guard, the #1117
        # forty-third-absent guard and the #1116 901-numeric guard:
        # all pins hold at #1120.
        result = self._stale_run(B1118_FILE, "TestSupersessionPins1118")
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1117_supersession_pins_still_green(self):
        # #1117's TestSupersessionPins1117 records the designed
        # end-states of the #1116 901-numeric guard, the #1115/#1114
        # 901-numeric guards and the 901 underscore/dash holds:
        # all pins hold at #1120.
        result = self._stale_run(A1117_FILE, "TestSupersessionPins1117")
        assert result.returncode == 0, result.stdout[-2000:]


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this file pins the new max + next number)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1120:
    def test_901_902_903_landed_this_window(self):
        # All three window mechanisms landed in their commits: 901
        # at #1117 Type A, 902 at #1118 Type B, 903 at #1119 Type C.
        data_901 = _m901_data()
        data_902 = _m902_data()
        data_903 = _m903_data()
        assert data_901["mechanism_id"] == 901
        assert data_902["mechanism_id"] == 902
        assert data_903["mechanism_id"] == 903
        assert data_901["iteration"] == 1117
        assert data_902["iteration"] == 1118
        assert data_903["iteration"] == 1119

    def test_1120_file_pins_max_id_903_and_next_904(self):
        # This file is the new window-opener pinning zero-904
        # forward guards (per the fail-forward cadence: each
        # window's opener supersedes the prior file's NEXT_NUM pin).
        assert MAX_ID == 903
        assert NEXT_NUM == 904
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_904_in_profiles(self):
        # Forward guard: zero numeric 904 mechanism ids in
        # profiles/ - will fail by design at the run that lands
        # mechanism 904.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_904_repo_wide(self):
        # Needle format-built per #715: no contiguous 904-form
        # literal may exist in this file.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_904_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_new_mechanisms_below_max(self):
        # No numeric mechanism id in profiles/ may exceed 903 -
        # corpus max is pinned.
        assert _max_numeric_mechanism_id() <= MAX_ID

    def test_no_thirty_second_direction_claim(self):
        # The next direction slot must be unclaimed repo-wide
        # (needle format-built per #715).
        text_parts = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                text_parts.append(
                    open(
                        os.path.join(root, f), encoding="utf-8", errors="replace"
                    ).read()
                )
        assert _TW32 not in "\n".join(text_parts)

    def test_no_forty_fourth_member_claim(self):
        # The next falsification slot must be unclaimed repo-wide
        # (needle format-built per #715).
        text_parts = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                text_parts.append(
                    open(
                        os.path.join(root, f), encoding="utf-8", errors="replace"
                    ).read()
                )
        assert _T44 not in "\n".join(text_parts)


# ---------------------------------------------------------------------------
# 10. Background suite verdict per #795
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1120:
    def _log_stats(self):
        size = os.path.getsize(PRIOR_SUITE_LOG)
        text = _read(PRIOR_SUITE_LOG)
        return size, text.count("."), text.count("F"), text.count("E"), text

    def test_prior_suite_died_seventh_consecutive(self):
        # The #1115-launched background full suite DIED: 1621
        # bytes (1461 dots, ~2% progress), last write Oct 1
        # 11:35:23 UTC, zero summary tokens (no "passed"/"failed"
        # summary, no collected-count token), no live pytest
        # process. Per the #795 convention this is recorded as
        # DIED, not "interrupted": the run produces no usable
        # verdict.
        size, dots, fails, errors, text = self._log_stats()
        assert size == 1621, size
        assert dots == 1461, dots
        assert fails == 0, fails
        assert errors == 0, errors
        assert "passed" not in text
        assert "failed" not in text
        assert " collected " not in text
        assert "no tests ran" not in text

    def test_no_live_pytest_process(self):
        result = subprocess.run(
            ["pgrep", "-f", "pytest.*type_d_1115"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0, (
            "a pytest process for the #1115 suite must not still be "
            "alive when its verdict is recorded"
        )

    def test_tombstone_lineage_advances_to_83rd(self):
        # SEVENTH consecutive background-suite death of the new streak
        # (the 57-run streak ENDED at #1085 when the #1080 suite
        # completed). Tombstone lineage advances EIGHTY-SECOND ->
        # EIGHTY-THIRD; recorded in the #1120 iteration-log entry.
        # Deselected pre-commit (log entry is written in the
        # log-hash step per #721).
        text = _read(LOG_PATH)
        assert "EIGHTY-THIRD" in text


# ---------------------------------------------------------------------------
# 11. Fresh synthetic engine calibration (new values, not #1115's)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1120:
    # Scratch-run values produced at this run (Thu 2026-10-01 ~09:10
    # PDT) via mediascope.score.asymmetry.calculate_asymmetry with
    # its real signature (target_scores, peer_scores,
    # target_entity, peer_entities, publication_slug,
    # period_start, period_end). The finding layer stays MANUAL
    # ILLUSTRATIVE ONLY: the engine is never promoted to findings,
    # and these numbers are NOT a corpus claim.

    def _calculate(self):
        from datetime import datetime

        from mediascope.score.asymmetry import calculate_asymmetry

        def calc(target_scores, peer_scores):
            return calculate_asymmetry(
                target_scores,
                peer_scores,
                "Meta",
                ["Anthropic", "OpenAI"],
                "synthetic-calibration",
                datetime(2026, 10, 1),
                datetime(2026, 10, 1),
            )

        return calc

    def test_strong_effect_is_significant(self):
        calc = self._calculate()
        meta = [-0.58, -0.74, -0.61, -0.69, -0.55, -0.71, -0.63, -0.67]
        comp = [0.12, -0.04, 0.09, 0.02, -0.08, 0.10, -0.03, 0.06]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(-0.6775)
        assert result.t_statistic == pytest.approx(-19.336014443143515)
        assert result.p_value < 1e-10
        assert result.cohens_d == pytest.approx(-9.668007221571758)
        assert result.is_significant is True
        # The strong arm-swap negates the asymmetry exactly.
        swapped = calc(comp, meta)
        assert swapped.asymmetry_score == pytest.approx(
            -result.asymmetry_score
        )

    def test_null_effect_is_not_significant(self):
        calc = self._calculate()
        arm_a = [-0.03, 0.05, -0.02, 0.04, -0.05, 0.01, -0.04, 0.06]
        arm_b = [-0.02, 0.04, -0.04, 0.03, -0.03, 0.05, -0.01, 0.02]
        result = calc(arm_a, arm_b)
        assert result.asymmetry_score == pytest.approx(-0.0025)
        assert result.p_value > 0.86
        assert result.is_significant is False
        lo = result.confidence_interval_lower
        hi = result.confidence_interval_upper
        assert lo < 0 < hi

    def test_degenerate_single_tone_inputs(self):
        # Single-tone arms on the m901 illustrative pair
        # (OpenAI -0.35 vs Meta carried mean +0.125): t 0.0,
        # p 1.0, d 0.0, not significant - the degenerate contract
        # per #638/#643.
        calc = self._calculate()
        result = calc([-0.35], [0.125])
        assert result.asymmetry_score == pytest.approx(-0.475)
        assert result.t_statistic == 0.0
        assert result.p_value == 1.0
        assert result.cohens_d == 0.0
        assert result.is_significant is False

    def test_engine_not_promoted_to_findings(self):
        # Aug 28 2026 standing rule: the finding layer is MANUAL
        # ILLUSTRATIVE ONLY; the engine is never promoted to
        # findings; no analysis.json update for verification runs.
        assert _DOC is not None
        for marker in (
            "MANUAL/QUALITATIVE ONLY",
            "engine NOT run",
            "no analysis.json update",
        ):
            assert marker in _DOC, marker


# ---------------------------------------------------------------------------
# 12. Suite re-launch (this run's background full suite)
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1120:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1120 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1125 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1125)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1120_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 13. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1120:
    def _readme(self):
        return _read(os.path.join(REPO_ROOT, "README.md"))

    def _arch(self):
        return _read(os.path.join(REPO_ROOT, "docs/ARCHITECTURE.md"))

    def test_readme_stats_table_ratchets(self):
        # The stats table carries the new counts (README_TEST_COUNT
        # tests / README_FILE_COUNT files); the constants are patched
        # post-first-run with the true collected count.
        assert str(README_TEST_COUNT) in self._readme()
        assert str(README_FILE_COUNT) in self._readme()

    def test_readme_test_file_table_prepends_this_file(self):
        assert OWN_BASENAME in self._readme()

    def test_architecture_tests_tree_lists_this_file(self):
        assert OWN_BASENAME in self._arch()

    def test_readme_counts_match_constants(self):
        # The README stats row must match the patched constants
        # (post-first-run; pre-commit this fails by design per #719).
        text = self._readme()
        assert ("%d" % README_TEST_COUNT) in text
        assert ("%d" % README_FILE_COUNT) in text


# ---------------------------------------------------------------------------
# 14. Iteration log entry
# ---------------------------------------------------------------------------
class TestTypeDIterationLog1120:
    def test_1120_entry_leads_log(self):
        # The "## #1120 Type D:" entry leads the log (newest-first
        # ordering); hashes are TBD until the log-hash followup
        # registers them per #721. Deselected pre-commit per #721.
        assert _read(LOG_PATH).startswith("## #1120 Type D:")

    def test_1120_entry_names_window_and_predecessors(self):
        text = _read(LOG_PATH)
        entry = text.split("## #1119 Type C:")[0]
        assert "1120-1124" in entry
        assert "3f792914" in entry
        assert "EIGHTY-THIRD" in entry

    def test_1119_entry_present(self):
        # The #1119 entry is present in the log (the #1120 entry
        # prepends above it).
        assert "## #1119 Type C:" in _read(LOG_PATH)


# ---------------------------------------------------------------------------
# 15. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1120:
    def test_no_concurrent_inflight_iteration_commits_staged(self):
        # The in-flight #899/#938/#900/#1012-wt working-tree edits
        # are owned by their runs; this run stages only its own
        # files. (Pre-staging this passes vacuously; it guards the
        # post-staging state before commit.)
        status = _git("status", "--short")
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in (
            "nytimes.yaml",
            "test_type_b_938_",
            "test_type_d_900_",
            "test_type_a_1012_",
        ):
            assert not any(f in l for l in staged), (f, staged)

    def test_this_run_stages_only_own_files(self):
        # This run's staged set is the #1120 test file and the
        # doc-sync files only.
        status = _git("status", "--short")
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        allowed = (
            "test_type_d_1120_",
            "README.md",
            "ARCHITECTURE.md",
            "iteration-log.md",
        )
        for l in staged:
            assert any(a in l for a in allowed), l

    def test_in_flight_files_present_uncommitted(self):
        # The in-flight blocks are present in the working tree as
        # uncommitted changes (owned by their runs): the #899
        # nytimes.yaml hunk, the #938 test-file edit, the untracked
        # #900 test file, and the #1012 working-tree edit.
        status = _git("status", "--short")
        assert " M profiles/nytimes.yaml" in status
        assert " M tests/test_type_b_938_" in status
        assert "?? tests/test_type_d_900_" in status
        assert " M tests/test_type_a_1012_" in status
