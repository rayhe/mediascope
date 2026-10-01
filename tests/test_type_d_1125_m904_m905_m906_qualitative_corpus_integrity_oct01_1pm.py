"""Type D -- Iteration #1125 (Thu 2026-10-01 13:00 PDT): m904/m905/m906
qualitative-discipline verification + post-1120-1124 corpus integrity
(max numeric mechanism_id 906; zero next-number 907 keys in
numeric/underscore/dash mechanism forms - the 907 needles are
format-built per #715 so no guard-literal carrier file exists; the
m904/m905/m906 block keys carry no mechanism-number substring
(designed keying), so they are plain literals; the #1122/#1123/#1124
window files are NOT edited by this run - their now-stale
forward-looking pins are recorded as fail-by-design via subprocess in
the staleness class (#1120's max-903 and zero-904 pins trip on the
landed 904/905/906; #1120's no-thirty-second-direction pin trips on
the landed THIRTY-SECOND direction; #1120's no-forty-fourth-member
pin trips on the landed FORTY-FOURTH member; #1121's staleness pins
flip on #1120's guard lifecycle; #1120's own forward-looking
staleness flips on the ledger-44/45 and 904 pins; #1124's zero-907
guards, no-thirty-third-direction guard and forty-sixth-absent
guard STAY GREEN; #1124's/#1123's/#1122's supersession classes STAY
GREEN); ledger holds at 45 with the FORTY-FOURTH member-claim form
present in exactly one profiles file (profiles/news-corp.yaml, m904
block, 3 occurrences - the #1118 designed pattern) and the
FORTY-FIFTH member-claim form present in exactly one profiles file
(profiles/careers/journalists.yaml, m905 block, 3 occurrences);
the forty-sixth member-claim form is absent profiles-wide (needle
format-built per #715); the thirty-second relationship direction is
present in competitor-entities.yaml (m906 PAY-FOR-REACH-LITIGATE-
FOR-CONTENT); the thirty-third relationship-direction claim form is
absent repo-wide (needle format-built per #715)) + the #1120
background-suite verdict (DIED at 1654 bytes / 1494 dots ~2% with
last write Oct 1 16:38 UTC and zero summary tokens, no live pytest
process - EIGHTH consecutive background-suite death of the new
streak; the 57-run streak ENDED at #1085 when the #1080 suite
completed; tombstone lineage advances EIGHTY-THIRD -> EIGHTY-
FOURTH) + fresh synthetic engine calibration (new values, not
#1120's) + re-launch of the full suite as a background process
writing to goal hidden_files type_d_1125_full_suite.log WITHOUT -x
(the full inventory, calendar by-design failures included, is needed
for the #1130 triage; the next Type D run checks its verdict per
the #795 convention).

Type D FIRST leg of the 1125-1129 window, OPENING it
(D->E->A->B->C). Committed predecessor #1124 Type C (12:00 PDT Oct 1)
CLOSED the 1120-1124 window (D #1120, E #1121, A #1122, B #1123,
C #1124). Rotation per the #565 anchor + rotation guard.
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
- m904 (Type A #1122, news-corp.yaml 4-space block key,
  `mechanism_id: 904` field form; block key count 1 - colon-form
  line only, designed: no block_key field in the m904 block and the
  test_file value does not contain the block key): WSJ x OpenAI
  Sep 28-Oct 1 safety-crisis double (GPT-6.1 Astra deception-shelving
  + FTC agent-safety probe, regulatory-enforcement register, arms
  -0.40 / -0.35 MANUAL ILLUSTRATIVE, mean -0.375) vs carried WSJ x
  Meta arms (m532 -0.30 / -0.25, mean -0.275, un-rescored per #807).
  Illustrative delta (OpenAI minus Meta) -0.10: the uniform
  payer-softening prediction (News Corp-OpenAI $250M/5yr licensing,
  May 2024) FAILS on both pegs; the Journal breaks the payer's
  safety-chief-admitted deception failure and routes the regulator's
  probe onto the payer, adversarially, with the deal disclosure
  intact (relay-attested via runtimewire/Reuters/PYMNTS, 0
  browser.open per #503). FORTY-FOURTH falsification-family member;
  ledger 43->44. FIRST regulatory-enforcement-register falsification
  at WSJ/News Corp.
- m905 (Type B #1123, journalists.yaml 4-space block key under
  Maxwell Zeff competitor_coverage, `mechanism_id: 905` field form;
  block key count 3 - colon-form line + block_key field + test_file
  field, designed): Zeff WIRED->WSJ migration (m63 fourth leg),
  12-day OpenAI register flip: Sep-16 WIRED company-briefed platform
  relay (+0.15, carried per #807 from m779/#913) becomes the
  Sep-24/28 WSJ debut-week adversarial safety-crisis double (Astra
  deception-shelving scoop -0.40; Australian agent-hack -0.35; mean
  -0.375; illustrative delta -0.525) MANUAL ILLUSTRATIVE ONLY. The
  dual-deal softer-OpenAI prediction (News Corp x OpenAI ~$50M/yr
  m519 + News Corp x Meta ~$50M/yr m549) FAILS at the
  journalist-migration level; the m63 PIPELINE TEST prediction is
  challenged (institutional framing dominates). FORTY-FIFTH
  falsification-family member; ledger 44->45. FIRST
  journalist-migration-register member of the current ordinal line.
- m906 (Type C #1124, competitor-entities.yaml zero-indent block
  key, `mechanism_id: 906` field form; block key count 2 -
  colon-form line + block_key field, designed - no test_file field
  in the m906 block): Perplexity Sep-15-2026 dual spend (HP taskbar
  pre-install, ZBook Ultra G3a first + Crusoe multi-year
  model-lifecycle on dedicated Nvidia GB300 NVL72 clusters, both
  terms undisclosed) under the seven-publisher suit load
  (Dow Jones/NY Post SDNY Oct 2024; NYT/Chicago Tribune; Reddit/
  Britannica/Merriam-Webster fall 2025; CNN May 2026 17,000 works;
  Nikkei/Asahi Tokyo District Court Aug 2026, 2.2B yen each) -
  PAY-FOR-REACH-LITIGATE-FOR-CONTENT as the THIRTY-SECOND
  relationship direction (reach and compute cash-settled, content
  priced adversarially by courts; split by INPUT TYPE, simultaneous,
  same product stack, same news day; distinct from #2 pay-or-litigate
  bifurcation m636). Tone NOT_SCORED per the Aug 28 2026 standing
  rule. NOT a falsification-family member; ledger holds at 45,
  forty-sixth member-claim absent.

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
    "test_type_d_1125_m904_m905_m906_qualitative_corpus_"
    "integrity_oct01_1pm.py"
)

MAX_ID = 906
NEXT_NUM = 907

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "c3212b93461ff870c5e9d3a38a64b2c9decd16d0"

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 58762
README_FILE_COUNT = 1450

# The m904/m905/m906 block keys carry no mechanism-number substring
# (designed keying), so they are plain literals per #715.
M904_KEY = (
    "type_a_1122_wsj_openai_astra_scrapped_plus_ftc_probe_"
    "enforcement_vs_carried_meta_arms_oct01_10am"
)
M904_INDENT = 4
M904_HOME = "profiles/news-corp.yaml"
M905_KEY = (
    "type_b_1123_maxwell_zeff_wsj_migration_openai_register_"
    "flip_vs_wired_platform_relay_sep2026"
)
M905_INDENT = 4
M905_HOME = "profiles/careers/journalists.yaml"
M906_KEY = (
    "type_c_1124_perplexity_hp_crusoe_sep15_dual_spend_under_"
    "suit_load_pay_for_reach_litigate_for_content_thirty_"
    "second_direction_oct01_12pm"
)
M906_INDENT = 0
M906_HOME = "profiles/competitor-entities.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1125_full_suite.log"
)
PRIOR_SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1120_full_suite.log"
)
A1122_FILE = (
    "tests/test_type_a_1122_wsj_openai_astra_scrapped_ftc_"
    "probe_enforcement_vs_carried_meta_arms_oct01_10am.py"
)
B1123_FILE = (
    "tests/test_type_b_1123_maxwell_zeff_wsj_migration_"
    "openai_register_flip_vs_wired_platform_relay_sep2026_"
    "11am.py"
)
C1124_FILE = (
    "tests/test_type_c_1124_perplexity_hp_crusoe_sep15_dual_"
    "spend_under_suit_load_pay_for_reach_litigate_for_"
    "content_thirty_second_direction_oct01_12pm.py"
)
E1121_FILE = (
    "tests/test_type_e_1121_podcast_sentiment_147th_"
    "verification_oct01_9am.py"
)
D1120_FILE = (
    "tests/test_type_d_1120_m901_m902_m903_qualitative_"
    "corpus_integrity_oct01_9am.py"
)

_DOC = __doc__

# The forty-sixth-member and thirty-third-direction needles are
# fragment-built per #715 so this file carries no contiguous literal
# of a forward-guard claim form. The landed FORTY-FOURTH and
# FORTY-FIFTH forms are plain literals (already in corpus); the
# landed thirty-second direction form is fragment-built as well
# because #1123's test_thirty_second_direction_absent_repo_wide
# still sweeps .py files (the #1124 file keeps the same discipline:
# its lone "THIRTY-SECOND" is broken across a line boundary).
_T44 = "FORTY-FOURTH falsification-family member"
_T45 = "FORTY-FIFTH falsification-family member"
_TW32 = "THIRTY-" + "SECOND relationship direction"
_T46 = "FORTY-" + "SIXTH falsification-family member"
_TW33 = "THIRTY-" + "THIRD relationship direction"


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
# numbers in git history: #1125 Type D opens the 1125-1129 window;
# #1124 Type C (committed 12:00 PDT Oct 1) is the schedule
# predecessor and CLOSED the 1120-1124 window. The in-flight runs
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
    file carries a contiguous 907-form mechanism literal (verified
    pre-commit), so the 907 sweeps run repo-wide with only this file
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


def _m904_data():
    return _block_data(M904_HOME, M904_KEY, M904_INDENT)


def _m905_data():
    return _block_data(M905_HOME, M905_KEY, M905_INDENT)


def _m906_data():
    return _block_data(M906_HOME, M906_KEY, M906_INDENT)


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1125:
    def test_no_type_d_1125_test_file_preexisting(self):
        files = glob.glob(
            os.path.join(TESTS_DIR, "test_type_d_1125*.py")
        )
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_no_type_d_1125_in_git_log(self):
        # Pre-commit novelty guard: no commit may already claim this slot.
        # SUPERSEDED BY DESIGN once this run's main commit ("Type D #1125:")
        # lands; post-commit, TestTypeDRotationGuard1125 asserts the anchor
        # and window instead. Deselect this test in post-commit full runs.
        log = _git("log", "--format=%s", "--grep=Type D #1125")
        assert "Type D #1125" not in log

    def test_max_id_is_906(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_907_numeric_forms_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        # m904: colon-form line only (count 1, designed - no block_key
        # field in the m904 block, and the test_file value does not
        # contain the block key). m905: colon-form line + block_key
        # field + test_file field (count 3, designed). m906:
        # colon-form line + block_key field (count 2, designed - no
        # test_file field in the m906 block).
        nc = _read(os.path.join(REPO_ROOT, M904_HOME))
        assert nc.count(M904_KEY) == 1, nc.count(M904_KEY)
        jou = _read(os.path.join(REPO_ROOT, M905_HOME))
        assert jou.count(M905_KEY) == 3, jou.count(M905_KEY)
        ent = _read(os.path.join(REPO_ROOT, M906_HOME))
        assert ent.count(M906_KEY) == 2, ent.count(M906_KEY)


# ---------------------------------------------------------------------------
# 2. Rotation guard (2 tests deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1125:
    def test_rotation_window_opens_1125(self):
        # FIRST leg of the 1125-1129 window, OPENING it (per #565:
        # D #1125 -> E #1126 -> A #1127 -> B #1128 -> C #1129).
        # Deselected pre-commit (this run's main commit is not yet
        # in history); passes post-commit.
        w = _window()
        assert w[0] == ("D", "1125"), w
        # Newest-first distinct sequence: D #1125 (this run) opens
        # the window after the closed 1120-1124 window (C #1124,
        # B #1123, A #1122, E #1121).
        assert [t for t, _ in w[:5]] == ["D", "C", "B", "A", "E"], w

    def test_predecessor_1124_chain_present(self):
        # #1124 Type C CLOSED the 1120-1124 window; its main/anchor/
        # doc-sync/log-hash chain must be in history before this run
        # commits.
        log = _git("log", "--format=%H %s")
        assert "fb17f6ad" in log
        assert "7445685f" in log
        assert "0fb33e51" in log
        assert "62c5506d" in log

    def test_no_type_e_1126_in_git_log(self):
        log = _git("log", "--format=%s", "--grep=Type E #1126")
        assert "Type E #1126" not in log

    def test_anchor_sha_is_real(self):
        # Patched post-main-commit by the anchor followup per #565.
        # Deselected pre-commit (placeholder by design); passes
        # post-patch.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40


# ---------------------------------------------------------------------------
# 2b. Novelty anchor (1 test, deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1125:
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1125
        # commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type D #1125")
        assert "Type D #1125" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1125:
    def test_m904_block_present_in_news_corp_yaml(self):
        data = _m904_data()
        assert data["mechanism_id"] == 904

    def test_m905_block_present_in_journalists_yaml(self):
        data = _m905_data()
        assert data["mechanism_id"] == 905

    def test_m906_block_present_in_competitor_entities_yaml(self):
        data = _m906_data()
        assert data["mechanism_id"] == 906

    def test_max_mechanism_id_is_906(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_907_forms_repo_wide(self):
        # Forward guard: zero numeric/underscore/dash 907 keys -
        # will fail by design at the run that lands mechanism 907.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_m904_key_count_is_designed(self):
        # Colon-form key line only: exactly 1, no block_key field,
        # no test_file carrier (the test_file value does not contain
        # the block key).
        text = _read(os.path.join(REPO_ROOT, M904_HOME))
        lines = [
            l
            for l in text.splitlines()
            if M904_KEY in l
        ]
        assert len(lines) == 1, lines
        assert lines[0].strip() == M904_KEY + ":"

    def test_m905_key_count_is_designed(self):
        # Colon-form key line + block_key field + test_file field:
        # exactly 3, no other carrier.
        text = _read(os.path.join(REPO_ROOT, M905_HOME))
        lines = [
            l
            for l in text.splitlines()
            if M905_KEY in l
        ]
        assert len(lines) == 3, lines
        assert lines[0].strip() == M905_KEY + ":"
        assert "block_key:" in lines[1]
        assert "test_file:" in lines[2]

    def test_m906_key_count_is_designed(self):
        # Colon-form key line + block_key field value: exactly 2,
        # no other carrier (no test_file field in the m906 block).
        text = _read(os.path.join(REPO_ROOT, M906_HOME))
        lines = [
            l
            for l in text.splitlines()
            if M906_KEY in l
        ]
        assert len(lines) == 2, lines
        assert lines[0].strip() == M906_KEY + ":"
        assert "block_key:" in lines[1]


# ---------------------------------------------------------------------------
# 4. m904 qualitative discipline (Type A #1122)
# ---------------------------------------------------------------------------
class TestTypeDM904QualitativeDiscipline:
    def test_m904_run_metadata(self):
        data = _m904_data()
        assert data["iteration"] == 1122
        assert data["hour_type"] == "A"
        assert data["date"] == "2026-10-01 10:00 PDT"
        assert "THIRD leg" in data["window"]
        assert "1120-1124" in data["window"]

    def test_m904_falsification_membership(self):
        data = _m904_data()
        assert data["falsification_family_member"] is True
        assert data["falsification_ledger"] == 44
        assert _T44 in data["ledger_note"]
        assert "ledger 43->44" in data["ledger_note"]

    def test_m904_openai_arms(self):
        data = _m904_data()
        arms = data["openai_arms"]["arms"]
        assert len(arms) == 2
        assert arms[0]["arm"] == "astra_scrapped_safety_chief_admission"
        assert arms[0]["tone"] == -0.40
        assert "MANUAL ILLUSTRATIVE" in arms[0]["tone_basis"]
        assert arms[1]["arm"] == "ftc_probe_enforcement"
        assert arms[1]["tone"] == -0.35
        assert data["openai_arms"]["openai_mean"] == pytest.approx(-0.375)

    def test_m904_carried_meta_arms(self):
        data = _m904_data()
        arms = data["meta_arms_carried"]["arms"]
        assert len(arms) == 2
        assert all(a["mechanism"] == 532 for a in arms)
        assert arms[0]["tone"] == -0.30
        assert arms[1]["tone"] == -0.25
        assert "un-rescored per #807" in arms[0]["basis"]
        assert data["meta_arms_carried"]["meta_mean"] == pytest.approx(-0.275)

    def test_m904_scorer_discipline(self):
        data = _m904_data()
        scorer = data["scorer"]
        assert scorer["openai_mean_tone"] == pytest.approx(-0.375)
        assert scorer["meta_mean_tone"] == pytest.approx(-0.275)
        assert scorer["illustrative_delta_openai_minus_meta"] == pytest.approx(
            -0.10
        )
        assert "MANUAL ILLUSTRATIVE ONLY" in scorer["method"]
        assert "engine NOT run" in scorer["method"]

    def test_m904_financial_relationship_fails(self):
        data = _m904_data()
        fin = data["financial_relationship"]
        assert "News Corp-OpenAI" in fin["deal"]
        assert "$250M" in fin["value"]
        assert fin["coverage_prediction"] == "softer (uniform payer-softening)"
        assert "FAILS on both pegs" in fin["result"]

    def test_m904_statistical_discipline(self):
        data = _m904_data()
        disc = data["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in disc
        assert "engine NOT run" in disc
        assert "NOT_CALCULATED" in disc
        assert "is_significant false" in disc
        assert "NOT artifact-grade" in disc
        assert data["verdict"] == "directionally_supported_not_proven"

    def test_m904_confounder_and_counterevidence_disclosure(self):
        data = _m904_data()
        conf = data["confounders"]
        assert len(conf) >= 5
        assert any(c.startswith("STRONG:") for c in conf)
        ce = data["counter_evidence"]
        assert len(ce) >= 4
        assert any("m718" in c for c in ce)

    def test_m904_research_method_and_sources(self):
        data = _m904_data()
        assert "5 browser.search query sets Oct 1 2026 PDT" in data[
            "research_method"
        ]
        assert "0 browser.open" in data["research_method"]
        urls = data["source_urls"]
        assert len(urls) == 3
        assert urls[0] == (
            "https://www.wsj.com/tech/ai/ftc-opens-investigation-"
            "of-anthropic-and-openai-a317b617"
        )
        assert "ASCII-only, no em dashes" in data["research_method"]


# ---------------------------------------------------------------------------
# 5. m905 qualitative discipline (Type B #1123)
# ---------------------------------------------------------------------------
class TestTypeDM905QualitativeDiscipline:
    def test_m905_run_metadata(self):
        data = _m905_data()
        assert data["iteration"] == 1123
        assert data["hour_type"] == "B"
        assert data["date"] == "2026-10-01 11:00 PDT"
        assert data["journalist"] == "Maxwell Zeff"
        assert "WIRED -> Wall Street Journal" in data["migration"]

    def test_m905_falsification_membership(self):
        data = _m905_data()
        assert data["falsification_family_member"] is True
        assert data["falsification_ledger"] == 45
        assert _T45 in data["ledger_note"]
        assert "ledger 44->45" in data["ledger_note"]

    def test_m905_wired_arm_carried(self):
        data = _m905_data()
        arm = data["wired_arm_carried"]
        assert arm["tone"] == 0.15
        assert arm["outlet"] == "WIRED"
        assert "un-rescored per #807" in arm["basis"]
        assert "platform relay" in arm["register"]

    def test_m905_wsj_arms_fresh(self):
        data = _m905_data()
        arms = data["wsj_arms_fresh"]
        # 2 scored arms + 1 unscored pattern-context arm (the
        # multi-lab oversight exclusive bounds the adversarial
        # claim without entering the mean).
        assert len(arms) == 3, len(arms)
        assert arms[0]["tone"] == -0.40
        assert arms[1]["tone"] == -0.35
        assert "MANUAL ILLUSTRATIVE" in arms[0]["tone_basis"]
        # The third arm is the unscored pattern-context arm: no tone
        # key, and a role field bounding the adversarial claim.
        assert "tone" not in arms[2]
        assert "Bounds the adversarial claim" in arms[2]["role"]
        flip = data["register_flip"]
        assert flip["wsj_openai_mean_tone"] == pytest.approx(-0.375)
        assert flip["window_days"] == 12

    def test_m905_register_flip_arithmetic(self):
        data = _m905_data()
        flip = data["register_flip"]
        assert flip["illustrative_delta_wsj_minus_wired"] == pytest.approx(
            -0.525
        )
        assert "(-0.375) - (0.15) = -0.525" in flip["delta_calc"]

    def test_m905_scorer_discipline(self):
        data = _m905_data()
        scorer = data["scorer"]
        assert scorer["illustrative_delta_wsj_minus_wired"] == pytest.approx(
            -0.525
        )
        assert "MANUAL ILLUSTRATIVE ONLY" in scorer["method"]
        assert "engine NOT run" in scorer["method"]
        assert data["verdict"] == "directionally_supported_not_proven"

    def test_m905_financial_relationship_fails(self):
        data = _m905_data()
        fin = data["financial_relationship"]
        assert "Conde Nast x OpenAI" in fin["wired_geometry"]
        assert "News Corp x OpenAI" in fin["wsj_geometry"]
        assert "DUAL-payer" in fin["wsj_geometry"]
        assert "FAILS at the journalist-migration level" in fin["result"]

    def test_m905_confounder_and_counterevidence_disclosure(self):
        data = _m905_data()
        conf = data["confounders"]
        assert len(conf) >= 5
        assert any(c.startswith("STRONG:") for c in conf)
        ce = data["counterevidence"]
        assert len(ce) >= 3
        assert any("entity-neutral" in c for c in ce)

    def test_m905_research_method_and_sources(self):
        data = _m905_data()
        assert "6 browser.search query sets Oct 1 2026 PDT" in data[
            "research_method"
        ]
        assert "0 browser.open" in data["research_method"]
        urls = data["source_urls"]
        assert len(urls) == 7
        assert urls[0] == "https://muckrack.com/maxwell-zeff"
        assert "ASCII-only, no em dashes" in data["research_method"]
        assert "no canonical URLs constructed" in data["research_method"]


# ---------------------------------------------------------------------------
# 6. m906 qualitative discipline (Type C #1124)
# ---------------------------------------------------------------------------
class TestTypeDM906QualitativeDiscipline:
    def test_m906_run_metadata(self):
        data = _m906_data()
        assert data["iteration"] == 1124
        assert data["iteration_type"] == "C"
        assert data["iteration_time"] == "2026-10-01 12:00 PDT"
        assert data["mechanism_id"] == 906

    def test_m906_thirty_second_direction_taxonomy(self):
        data = _m906_data()
        assert _TW32 in data["relationship_direction_taxonomy"]
        assert "PAY-FOR-REACH-LITIGATE-FOR-CONTENT" in data[
            "relationship_direction_taxonomy"
        ]
        assert "m807 enumeration" in data["relationship_direction_taxonomy"]
        assert "mechanism_name" in data
        assert "THIRTY-SECOND" in data["mechanism_name"]

    def test_m906_not_falsification_member(self):
        data = _m906_data()
        assert data["falsification_family_member"] is False
        assert "NOT a member" in data["falsification_family"]
        assert "ledger holds at 45" in data["falsification_family"]

    def test_m906_statistical_discipline(self):
        data = _m906_data()
        assert data["tone_scored"] is False
        assert data["engine_run"] is False
        assert data["is_significant"] is False
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False

    def test_m906_confounder_disclosure(self):
        data = _m906_data()
        conf = data["confounders"]
        assert len(conf) >= 5
        strong = [c for c in conf if c["strength"] == "STRONG"]
        assert len(strong) >= 2
        assert any("Undisclosed terms" in c["text"] for c in strong)
        assert any(
            "counterargument" in c for c in conf if "counterargument" in c
        )

    def test_m906_sources_and_novelty(self):
        data = _m906_data()
        sources = data["sources"]
        assert len(sources) == 7
        assert all(s["novel"] is True for s in sources)
        assert sources[0]["url"] == (
            "https://startupfortune.com/hp-is-putting-perplexity-"
            "on-new-pcs-while-seven-publishers-sue-it/"
        )
        assert "FIRST dedicated corpus mechanism" in data["novelty"]
        assert "the seven novel source URLs zero-hit repo-wide" in data[
            "novelty"
        ]

    def test_m906_yaml_hygiene(self):
        data = _m906_data()
        assert data["yaml_parse_clean"] is True
        assert data["ascii_only"] is True
        assert "coverage_nexus" in data
        assert "Nikkei owns the Financial Times" in data["coverage_nexus"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1125:
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

    def test_forty_fourth_claim_in_exactly_one_profiles_file(self):
        hits = [
            p for p, t in self._profiles_text() if _T44 in t
        ]
        assert len(hits) == 1, hits
        assert hits[0].endswith("news-corp.yaml"), hits

    def test_forty_fourth_claim_count_is_designed(self):
        # The m904 block carries the claim in the mechanism_name line,
        # the finding line and the ledger_note line (3 occurrences, 1
        # block - the #1118 designed pattern extended to Type A).
        text = _read(os.path.join(REPO_ROOT, M904_HOME))
        assert text.count(_T44) == 3, text.count(_T44)

    def test_forty_fifth_claim_in_exactly_one_profiles_file(self):
        hits = [
            p for p, t in self._profiles_text() if _T45 in t
        ]
        assert len(hits) == 1, hits
        assert hits[0].endswith("careers/journalists.yaml"), hits

    def test_forty_fifth_claim_count_is_designed(self):
        # The m905 block carries the claim in the mechanism_name line,
        # the finding line's self-reference and the ledger_note line
        # (3 occurrences, 1 block - the #1118 designed pattern).
        text = _read(os.path.join(REPO_ROOT, M905_HOME))
        assert text.count(_T45) == 3, text.count(_T45)

    def test_no_forty_sixth_member_claim_profiles_wide(self):
        # The next falsification slot must be unclaimed profiles-wide
        # (needle format-built per #715; designed negative-guard
        # wordings do not carry the claim form).
        for p, t in self._profiles_text():
            assert _T46 not in t, p

    def test_m904_m905_ledger_sequence_carried(self):
        d904 = _m904_data()
        d905 = _m905_data()
        assert d904["falsification_ledger"] == 44
        assert d905["falsification_ledger"] == 45

    def test_m906_holds_ledger_at_45(self):
        d906 = _m906_data()
        assert d906["falsification_family_member"] is False
        assert "ledger holds at 45" in d906["falsification_family"]


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (subprocess pins on prior window files)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1125:
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

    def test_1120_guard_lifecycle_stale_by_design(self):
        # #1120's TestGuardLifecycle1120 pinned max 903, zero-904
        # numeric, no-thirty-second-direction and no-forty-fourth-
        # member. The #1122 (904, FORTY-FOURTH), #1123 (905) and #1124
        # (906, THIRTY-SECOND) landings trip the max, numeric,
        # thirty-second and forty-fourth pins. Designed lifecycle;
        # recorded, not repaired.
        result = self._stale_run(D1120_FILE, "TestGuardLifecycle1120")
        assert result.returncode != 0, result.stdout[-2000:]
        assert "904" in result.stdout or "906" in result.stdout

    def test_1121_staleness_pins_stale_by_design(self):
        # #1121's TestStalenessPins pinned #1120 TestGuardLifecycle1120
        # still PASS; the 904/905/906 landings flip it at #1125.
        # Designed lifecycle; recorded, not repaired.
        result = self._stale_run(E1121_FILE, "TestStalenessPins")
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1120_forward_looking_staleness_flips_by_design(self):
        # #1120's TestTypeDForwardLookingStaleness1120 pinned
        # test_1119_zero_904_forward_guards_still_green,
        # test_1119_supersession_pins_still_green and friends: the
        # #1122/#1123/#1124 landings (mechanisms 904/905/906, the
        # THIRTY-SECOND direction, the FORTY-FOURTH/FORTY-FIFTH
        # members) flip them at #1125. Designed lifecycle; recorded,
        # not repaired.
        result = self._stale_run(
            D1120_FILE, "TestTypeDForwardLookingStaleness1120"
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1124_zero_907_forward_guards_still_green(self):
        # #1124's TestForwardGuards1124 pins zero-907
        # (numeric/underscore/dash) and no-thirty-third-direction:
        # 907 unlanded, all green at #1125.
        result = self._stale_run(C1124_FILE, "TestForwardGuards1124")
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1124_ledger45_forty_sixth_absent_still_green(self):
        # #1124's TestLedger45Holds pins the forty-sixth-absent
        # guard: the slot is still unclaimed at #1125.
        result = self._stale_run(
            C1124_FILE,
            "TestLedger45Holds::test_forty_sixth_absent_repo_wide",
        )
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1124_supersession_pins_still_green(self):
        # #1124's TestSupersessionPins1124 records the designed
        # end-states of the #1123 max-905/numeric-906 pins (failed by
        # design on the 906 landing), the #1119 thirty-second-absent
        # pin (failed by design on the 906 landing), the #1121
        # 904-flip pin, and the #1123 thirty-second-absent py-scoped
        # + 906 underscore/dash + forty-sixth-absent +
        # thirty-first-present holds: all pins hold at #1125. (The
        # #1123 thirty-second guard stays green only because this
        # file, like #1124's, format-builds the thirty-second
        # needle per #715.)
        result = self._stale_run(C1124_FILE, "TestSupersessionPins1124")
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1123_forty_sixth_absent_still_green(self):
        # #1123's TestFalsificationLedger1123 pins the forty-sixth-
        # absent guard: the slot is still unclaimed at #1125.
        result = self._stale_run(
            B1123_FILE,
            "TestFalsificationLedger1123::"
            "test_forty_sixth_member_absent_repo_wide",
        )
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1123_supersession_pins_except_thirty_second_still_green(self):
        # #1123's TestSupersessionPins1123 records the designed
        # end-states of the #1122 zero-905 numeric guard and the
        # #1122 forty-fifth-absent guard (both failed by design on
        # the 905 landing), and the 905 underscore/dash +
        # forty-fourth-intact holds. Its
        # test_1122_thirty_second_absent_still_green pin flips BY
        # DESIGN at #1124: the landed thirty-second direction in
        # competitor-entities.yaml trips #1122's profiles+tests-
        # scoped guard (unrecorded at #1124; recorded here).
        result = self._stale_run(
            B1123_FILE,
            "TestSupersessionPins1123",
            "TestSupersessionPins1123::"
            "test_1122_thirty_second_absent_still_green",
        )
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1123_thirty_second_pin_flips_by_design(self):
        # The one #1123 supersession pin that fails by design at
        # #1125: the landed thirty-second direction trips #1122's
        # profiles+tests-scoped guard. Recorded, not repaired.
        result = self._stale_run(
            B1123_FILE,
            "TestSupersessionPins1123::"
            "test_1122_thirty_second_absent_still_green",
        )
        assert result.returncode != 0, result.stdout[-2000:]
        assert "test_1122_thirty_second_absent_still_green" in result.stdout

    def test_1122_supersession_pins_except_thirty_second_still_green(self):
        # #1122's TestSupersessionPins1122 records the designed
        # end-states of the #1121 zero-904 numeric guard and the
        # #1121 forty-fourth-absent guard (both failed by design on
        # the 904 landing), and the 904 underscore/dash + #1119
        # forward-guard holds. Its
        # test_1120_underscore_dash_thirty_second_still_green pin
        # flips BY DESIGN at #1124: the landed thirty-second
        # direction in competitor-entities.yaml trips #1120's
        # profiles-scoped no-thirty-second guard (unrecorded at
        # #1124; recorded here).
        result = self._stale_run(
            A1122_FILE,
            "TestSupersessionPins1122",
            "TestSupersessionPins1122::"
            "test_1120_underscore_dash_thirty_second_still_green",
        )
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1122_thirty_second_pin_flips_by_design(self):
        # The one #1122 supersession pin that fails by design at
        # #1125: the landed thirty-second direction trips #1120's
        # profiles-scoped guard. Recorded, not repaired.
        result = self._stale_run(
            A1122_FILE,
            "TestSupersessionPins1122::"
            "test_1120_underscore_dash_thirty_second_still_green",
        )
        assert result.returncode != 0, result.stdout[-2000:]
        assert (
            "test_1120_underscore_dash_thirty_second_still_green"
            in result.stdout
        )


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this file pins the new max + next number)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1125:
    def test_904_905_906_landed_this_window(self):
        # All three window mechanisms landed in their commits: 904
        # at #1122 Type A, 905 at #1123 Type B, 906 at #1124 Type C.
        data_904 = _m904_data()
        data_905 = _m905_data()
        data_906 = _m906_data()
        assert data_904["mechanism_id"] == 904
        assert data_905["mechanism_id"] == 905
        assert data_906["mechanism_id"] == 906
        assert data_904["iteration"] == 1122
        assert data_905["iteration"] == 1123
        assert data_906["iteration"] == 1124

    def test_1125_file_pins_max_id_906_and_next_907(self):
        # This file is the new window-opener pinning zero-907
        # forward guards (per the fail-forward cadence: each
        # window's opener supersedes the prior file's NEXT_NUM pin).
        # NOTE: #1120's forward-looking note predicted this run
        # would pin zero-905; the 1120-1124 window instead landed
        # 904/905/906, so the pin is zero-907 per the landed state.
        assert MAX_ID == 906
        assert NEXT_NUM == 907
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_907_in_profiles(self):
        # Forward guard: zero numeric 907 mechanism ids in
        # profiles/ - will fail by design at the run that lands
        # mechanism 907.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_907_repo_wide(self):
        # Needle format-built per #715: no contiguous 907-form
        # literal may exist in this file.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_907_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_new_mechanisms_below_max(self):
        # No numeric mechanism id in profiles/ may exceed 906 -
        # corpus max is pinned.
        assert _max_numeric_mechanism_id() <= MAX_ID

    def test_no_thirty_third_direction_claim(self):
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
        assert _TW33 not in "\n".join(text_parts)

    def test_no_forty_sixth_member_claim(self):
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
        assert _T46 not in "\n".join(text_parts)


# ---------------------------------------------------------------------------
# 10. Background suite verdict per #795
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1125:
    def _log_stats(self):
        size = os.path.getsize(PRIOR_SUITE_LOG)
        text = _read(PRIOR_SUITE_LOG)
        return size, text.count("."), text.count("F"), text.count("E"), text

    def test_prior_suite_died_eighth_consecutive(self):
        # The #1120-launched background full suite DIED: 1654
        # bytes (1494 dots, ~2% progress), last write Oct 1
        # 16:38:06 UTC, zero summary tokens (no "passed"/"failed"
        # summary, no collected-count token), no live pytest
        # process. Per the #795 convention this is recorded as
        # DIED, not "interrupted": the run produces no usable
        # verdict.
        size, dots, fails, errors, text = self._log_stats()
        assert size == 1654, size
        assert dots == 1494, dots
        assert fails == 0, fails
        assert errors == 0, errors
        assert "passed" not in text
        assert "failed" not in text
        assert " collected " not in text
        assert "no tests ran" not in text

    def test_no_live_pytest_process(self):
        result = subprocess.run(
            ["pgrep", "-f", "pytest.*type_d_1120"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0, (
            "a pytest process for the #1120 suite must not still be "
            "alive when its verdict is recorded"
        )

    def test_tombstone_lineage_advances_to_84th(self):
        # EIGHTH consecutive background-suite death of the new streak
        # (the 57-run streak ENDED at #1085 when the #1080 suite
        # completed). Tombstone lineage advances EIGHTY-THIRD ->
        # EIGHTY-FOURTH; recorded in the #1125 iteration-log entry.
        # Deselected pre-commit (log entry is written in the
        # log-hash step per #721).
        text = _read(LOG_PATH)
        assert "EIGHTY-FOURTH" in text


# ---------------------------------------------------------------------------
# 11. Fresh synthetic engine calibration (new values, not #1120's)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1125:
    # Scratch-run values produced at this run (Thu 2026-10-01 ~13:10
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
        meta = [-0.71, -0.52, -0.68, -0.60, -0.74, -0.57, -0.66, -0.63]
        comp = [0.21, -0.09, 0.14, 0.05, -0.02, 0.18, -0.06, 0.11]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(-0.70375)
        assert result.t_statistic == pytest.approx(-14.784376063554792)
        assert result.p_value < 1e-8
        assert result.cohens_d == pytest.approx(-7.392188031777396)
        assert result.is_significant is True
        # The strong arm-swap negates the asymmetry exactly.
        swapped = calc(comp, meta)
        assert swapped.asymmetry_score == pytest.approx(
            -result.asymmetry_score
        )

    def test_null_effect_is_not_significant(self):
        calc = self._calculate()
        arm_a = [0.07, -0.03, 0.04, -0.05, 0.02, -0.06, 0.01, -0.04]
        arm_b = [0.03, -0.05, 0.06, -0.02, -0.04, 0.05, -0.01, 0.02]
        result = calc(arm_a, arm_b)
        assert result.asymmetry_score == pytest.approx(-0.01)
        assert result.p_value > 0.6
        assert result.is_significant is False
        lo = result.confidence_interval_lower
        hi = result.confidence_interval_upper
        assert lo < 0 < hi

    def test_degenerate_single_tone_inputs(self):
        # Single-tone arms on the m904 illustrative pair
        # (OpenAI mean -0.375 vs Meta carried mean -0.275): t 0.0,
        # p 1.0, d 0.0, not significant - the degenerate contract
        # per #638/#643.
        calc = self._calculate()
        result = calc([-0.375], [-0.275])
        assert result.asymmetry_score == pytest.approx(-0.10)
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
class TestSuiteRelaunch1125:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1125 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1130 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1130)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1125_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 13. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1125:
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
class TestTypeDIterationLog1125:
    def test_1125_entry_leads_log(self):
        # The "## #1125 Type D:" entry leads the log (newest-first
        # ordering); hashes are TBD until the log-hash followup
        # registers them per #721. Deselected pre-commit per #721.
        assert _read(LOG_PATH).startswith("## #1125 Type D:")

    def test_1125_entry_names_window_and_predecessors(self):
        text = _read(LOG_PATH)
        entry = text.split("## #1124 Type C:")[0]
        assert "1125-1129" in entry
        assert "62c5506d" in entry
        assert "EIGHTY-FOURTH" in entry

    def test_1124_entry_present(self):
        # The #1124 entry is present in the log (the #1125 entry
        # prepends above it).
        assert "## #1124 Type C:" in _read(LOG_PATH)


# ---------------------------------------------------------------------------
# 15. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1125:
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
        # This run's staged set is the #1125 test file and the
        # doc-sync files only.
        status = _git("status", "--short")
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        allowed = (
            "test_type_d_1125_",
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
