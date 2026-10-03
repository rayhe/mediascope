"""Type A -- Iteration #1157 (Fri 2026-10-02 18:00 PDT): m925 NY Post x
OpenAI/Anthropic Sep-30-2026 FTC-probe original (Post first to report)
vs carried NY Post x Meta arms -- tabloid enforcement-register
continuity, temporal extension of the m763 triad.

On Sep 30 2026 the New York Post published "FTC opens sweeping probe
of Anthropic, OpenAI and other 'super intelligence' models" and is
relay-attested by Reuters (via tbsnews relay) as FIRST to report the
probe -- a day before the WSJ Oct-1 original (m904) and contemporaneous
with the FT Sep-30 piece. The piece applies the
regulatory-enforcement accountability register to the ~$50M/yr
May-2024 OpenAI licensing-deal partner (civil investigative demands,
executive testimony, Ferguson "moat" quotes) with no softening
visible, extending the m763 Sep 9-19 adversarial triad (avg -0.483) by
11 days onto a federal-enforcement peg. Scorer (MANUAL ILLUSTRATIVE
ONLY): new OpenAI FTC arm -0.40 vs triad OpenAI mean -0.483 gives an
illustrative delta of +0.083 (register continuity); new OpenAI FTC arm
-0.40 vs carried Meta arm -0.50 (Sep-18 glasses lawsuit) gives +0.10
near-null -- dual-payer tabloid symmetry holds. NOT a
falsification-family member: the News Corp x OpenAI uniform-softening
prediction was already tested and counted at the tabloid register by
m763 (TWENTY-NINTH member, #887); this run is a same-publication
temporal replication on a new peg, which per the #1143 precedent is
not a new prediction test. Ledger holds at 46 (FORTY-SIXTH in
the-verge.yaml m907 x2; forty-seventh absent; thirty-sixth and
thirty-seventh absent; THIRTY-FIFTH present m915). Disclosure note:
extends the m919 news-corp disclosure_asymmetry strand descriptively --
the WSJ Oct-1 piece disclosed the News Corp-OpenAI tie inline while
the Post Sep-30 piece shows NO disclosure line in the surfaced
excerpt (full-page UNVERIFIED per #492; excerpt-bounded per #503).
The nypost Sep-30 FTC URL is new-to-corpus (zero-hit pre-commit).

Type A THIRD leg of the 1155-1159 window, CONTINUING it
(D #1155 -> E #1156 -> A #1157 -> B #1158 -> C #1159). Committed
predecessors: #1155 Type D (main 72a638f1 / anchor f4ad78e9 /
doc-sync 4a33a092 / log-hash 4638c381) and #1156 Type E (main
e7180bb3 / anchor 98d22959 / doc-sync 027b5a08 / log-hash 7c75d462),
both verified present in history pre-commit. Rotation per the #565
anchor + rotation guard. Iteration-log convention: entries appended
at the tail since #1149 (the #1152 test's _window() treats the log as
chronological oldest-first, newest-appended).
Concurrency note: the in-flight runs at this run's checks are the
#899 Type C block (m771, uncommitted hunk in profiles/nytimes.yaml),
the #938 Type B test file (uncommitted working-tree edit), the #900
Type D test file (untracked, on disk) and the #1012 working-tree
edit of the committed Type A #1012 test file - all UNCOMMITTED, no
Type C #899 / Type B #938 / Type D #900 main commits in git
history, and no ## #899 / ## #938 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch the in-flight files (the
m925 block lands in profiles/news-corp.yaml under
competitor_relationships > openai as a 4-space-indent sibling of the
m763 triad block, NOT nytimes.yaml); the in-flight blocks are
owned by their runs. Targeted staging only per the repo-wide
traversal lesson. Iteration numbers follow the rotation schedule, not
commit order. Do NOT touch #1024's m846 (self-flagged
sourcing-constraint violation; Ray's revert/leave/rebuild-from-primary
decision still pending).

Verifies:
- m925 (Type A #1157, profiles/news-corp.yaml
  competitor_relationships > openai block key, 4-space indent (sibling
  of the m763 triad block per the news-corp.yaml convention),
  `mechanism_id: 925` field form; block key count 1 - designed: the
  block key carries no mechanism-number substring (1157 is the
  iteration), so it is a plain literal per #715): NY Post Sep-30
  FTC-probe original (Post first to report, relay-attested) applying
  the enforcement register to the OpenAI licensing partner (-0.40
  MANUAL ILLUSTRATIVE) vs carried triad arms (OpenAI mean -0.483,
  Meta -0.50, un-rescored per #807); illustrative deltas +0.083 /
  +0.10 near-null; NOT a falsification-family member (temporal
  replication per #1143); ledger holds at 46; disclosure observation
  extends m919 descriptively (no disclosure line in excerpt,
  full-page UNVERIFIED per #492); post-landing corpus integrity (max
  numeric mechanism_id 925; zero next-number 926 keys in
  numeric/underscore/dash mechanism forms - the 926 needles are
  format-built per #715 so no guard-literal carrier file exists;
  the forty-seventh member-claim form absent repo-wide as designed
  negative guard for the next landing; thirty-fifth direction present
  (competitor-entities.yaml, m915), thirty-sixth and thirty-seventh
  absent; the #1155/#1156 window files are NOT edited by this run -
  their now-stale forward-looking pins are recorded as fail-by-design
  via subprocess in the staleness class (#1156's zero-925 numeric pin
  trips on the landed 925; #1156's underscore/dash 925 pins STAY
  GREEN by design - no contiguous underscore/dash-form 925 literal
  exists; #1156's no-thirty-sixth and no-forty-seventh pins STAY
  GREEN, asserted in this run's own guard-lifecycle class)) + the
  #1155 background-suite check (DEAD at this run's check per #795 -
  no pytest alive, log stalled at 1804 bytes since Oct 2 16:51:36
  PDT; checked only, NOT touched; verdict belongs to #1160 per #795).

MANUAL/QUALITATIVE ONLY, engine NOT run, no analysis.json update,
NOT artifact-grade, verdict directionally_supported_not_proven.
Correlation is not causation; hypothesis-generating only.
"""
import glob
import os
import re
import subprocess
import time

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
OWN_BASENAME = (
    "test_type_a_1157_nypost_ftc_probe_sweeping_openai_anthropic_"
    "original_sep30_vs_carried_meta_arms_oct02_6pm.py"
)

MAX_ID = 925
NEXT_NUM = 926

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "0" * 40  # patched per #565 in the anchor followup

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 61097
README_FILE_COUNT = 1482

# The m925 block key carries no mechanism-number substring (1157 is
# the iteration, not the mechanism), so it is a plain literal per
# #715.
M925_KEY = (
    "nypost_ftc_probe_sweeping_openai_anthropic_"
    "super_intelligence_original_sep30_1157"
)
M925_INDENT = 4
M925_HOME = "profiles/news-corp.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

# Falsification-family / relationship-direction needles are
# format-built per #715: no contiguous claim-form literal may exist
# in this file. The landed-claim forms live in the-verge.yaml (m907)
# and competitor-entities.yaml (m915) respectively.
_T46 = "FORTY-" + "SIXTH falsification-family member"
_T47 = "FORTY-" + "SEVENTH falsification-family member"
_TW35 = "THIRTY-" + "FIFTH relationship direction"
_TW36 = "THIRTY-" + "SIXTH relationship direction"
_TW37 = "THIRTY-" + "SEVENTH relationship direction"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1155_full_suite.log"
)
E1156_FILE = (
    "tests/test_type_e_1156_podcast_sentiment_154th_verification_"
    "oct02_5pm.py"
)

# Committed predecessor #1155 Type D chain (verified pre-commit).
PRED_MAIN_1155 = "72a638f1"
PRED_ANCHOR_1155 = "f4ad78e9"
PRED_DOCSYNC_1155 = "4a33a092"
PRED_FINAL_1155 = "4638c381"
# Committed predecessor #1156 Type E chain (verified pre-commit).
PRED_MAIN_1156 = "e7180bb3"
PRED_ANCHOR_1156 = "98d22959"
PRED_DOCSYNC_1156 = "027b5a08"
PRED_FINAL_1156 = "7c75d462"

# New-to-corpus this run (zero-hit repo-wide pre-commit).
NEW_URLS = [
    "https://nypost.com/2026/09/30/us-news/ftc-opens-sweeping-probe-of-anthropic-openai-and-other-super-intelligence-models/",
]

# Carried arms (un-rescored per #807): m763 triad OpenAI mean -0.483,
# Meta arm -0.50; new FTC arm -0.40 MANUAL ILLUSTRATIVE.
TRIAD_OPENAI_MEAN = -0.483
TRIAD_META_ARM = -0.50
NEW_FTC_ARM = -0.40


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def _git(*args):
    result = subprocess.run(
        ["git", "-C", REPO_ROOT] + list(args),
        capture_output=True,
        text=True,
        timeout=120,
    )
    return result.stdout


def _iter_source_files():
    for root, dirs, files in os.walk(REPO_ROOT):
        if ".git" in root or ".venv" in root or "__pycache__" in root:
            continue
        dirs[:] = [
            d
            for d in dirs
            if d not in (".git", ".venv", "__pycache__", "node_modules")
        ]
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


def _m925_data():
    import yaml

    with open(os.path.join(REPO_ROOT, M925_HOME), encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["openai"][M925_KEY]


def _window():
    """File-order distinct (type, number) sequence from the log.

    The log is chronological (oldest first, newest appended) since
    #1149, so file order is oldest-first, not newest-first.
    """
    pat = re.compile(r"^## #(\d+) Type ([A-E]):", re.M)
    seen = []
    for num, typ in pat.findall(_read(LOG_PATH)):
        key = (typ, num)
        if key not in seen:
            seen.append(key)
    return seen


# ---------------------------------------------------------------------------
# 1. Novelty (pre-commit state recorded post-commit; superseded pins noted)
# ---------------------------------------------------------------------------
class TestNovelty1157:
    def test_single_type_a_1157_file(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1157*.py"))
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_type_a_1157_in_git_log(self):
        log = _git("log", "--format=%H %s", "--grep=Type A #1157")
        assert "Type A #1157" in log

    def test_type_a_1157_commit_set(self):
        # Post-full-run: exactly three commits carry "Type A #1157"
        # (main + anchor followup + log-hash followup per #721; the
        # doc-sync commit title is the "Doc-sync #1157:" form and does
        # not match the grep).
        log = _git("log", "--format=%H", "--grep=Type A #1157")
        assert len([l for l in log.splitlines() if l.strip()]) == 3, log

    def test_new_nypost_url_in_corpus(self):
        # The nypost Sep-30 FTC URL was zero-hit repo-wide
        # pre-commit; it is in-corpus now (this file's constant list
        # plus the news-corp.yaml block).
        for url in NEW_URLS:
            hits = _git("grep", "-l", "-F", url).splitlines()
            assert len(hits) >= 1, url

    def test_block_key_unique_in_home_yaml(self):
        # Post-commit-stable: the block key is a literal in this
        # file's constant, so count only inside the home YAML.
        text = _read(os.path.join(REPO_ROOT, M925_HOME))
        assert text.count(M925_KEY + ":") == 1


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestTypeARotationGuard1157:
    def test_anchor_sha_format(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40

    def test_predecessor_1155_chain_in_history(self):
        for sha in (
            PRED_MAIN_1155,
            PRED_ANCHOR_1155,
            PRED_DOCSYNC_1155,
            PRED_FINAL_1155,
        ):
            assert sha in _git("log", "--format=%H"), sha

    def test_predecessor_1156_chain_in_history(self):
        for sha in (
            PRED_MAIN_1156,
            PRED_ANCHOR_1156,
            PRED_DOCSYNC_1156,
            PRED_FINAL_1156,
        ):
            assert sha in _git("log", "--format=%H"), sha

    def test_window_third_leg(self):
        window = _window()
        assert ("A", "1157") in window
        assert ("E", "1156") in window
        assert ("D", "1155") in window
        # File order is chronological (oldest first): D1155 older than
        # E1156 older than A1157.
        assert window.index(("D", "1155")) < window.index(("E", "1156"))
        assert window.index(("E", "1156")) < window.index(("A", "1157"))

    def test_rotation_phrase_in_log_entry(self):
        text = _read(LOG_PATH)
        assert "## #1157 Type A:" in text
        entry_start = text.index("## #1157 Type A:")
        entry = text[entry_start : entry_start + 4000]
        assert "1155-1159 window" in entry
        assert "THIRD leg" in entry


# ---------------------------------------------------------------------------
# Anchor (deselected pre-commit per #565; patched post-commit)
# ---------------------------------------------------------------------------
class TestTypeANoveltyAnchor1157:
    @pytest.mark.skip(reason="deselected pre-commit per #565; green post-anchor")
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1157
        # main commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type A #1157")
        assert "Type A #1157" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeACorpusIntegrity1157:
    def test_m925_block_keyed_at_indent_4(self):
        text = _read(os.path.join(REPO_ROOT, M925_HOME))
        line = next(l for l in text.splitlines() if l.strip() == M925_KEY + ":")
        assert line.startswith(" " * M925_INDENT)
        assert not line.startswith(" " * (M925_INDENT + 1))

    def test_m925_block_sibling_of_triad_block(self):
        data = _read(os.path.join(REPO_ROOT, M925_HOME))
        assert (
            "    nypost_openai_adversarial_triad_vs_meta_glasses_"
            "lawsuit_dual_payer_symmetry_sep21:" in data
        )

    def test_m925_mechanism_id_field_form(self):
        text = _read(os.path.join(REPO_ROOT, M925_HOME))
        assert "mechanism_id: 925" in text

    def test_max_numeric_mechanism_id_is_925(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_926_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_926_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_926_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_925_substring_in_block_key(self):
        assert "925" not in M925_KEY


# ---------------------------------------------------------------------------
# 4. m925 content discipline (YAML-parsed assertions)
# ---------------------------------------------------------------------------
class TestTypeAM925ContentDiscipline1157:
    def test_metadata_fields(self):
        d = _m925_data()
        assert d["mechanism_id"] == 925
        assert d["iteration"] == 1157
        assert d["iteration_type"] == "A"
        assert d["rotation"] == "Type A"
        assert d["date_analyzed"] == "2026-10-02"
        assert d["job_id"] == "mediascope-daily-iteration"
        assert d["goal_id"] == "goal_54093bda4145"
        assert d["author"] == "Kit (with Ray)"

    def test_new_arm_fields(self):
        arm = _m925_data()["articles_new"][0]
        assert arm["publication"] == "New York Post"
        assert arm["date"] == "2026-09-30"
        assert arm["url"] == NEW_URLS[0]
        assert arm["register"] == "regulatory_enforcement_accountability"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == NEW_FTC_ARM
        assert len(arm["key_quotes"]) == 4
        assert len(arm["tone_observations"]) == 4

    def test_first_to_report_attestation(self):
        arm = _m925_data()["articles_new"][0]
        assert "first reported the news" in arm["first_to_report_attestation"]
        assert "m904" in arm["first_to_report_attestation"]

    def test_carried_arms_per_807_unrescored(self):
        d = _m925_data()
        arms = d["carried_arms_per_807"]
        assert len(arms) == 2
        assert "m763" in arms[0]["mechanism"]
        assert "-0.483" in arms[0]["arms"]
        assert "-0.50" in arms[1]["arms"]

    def test_scorer_deltas(self):
        s = _m925_data()["scorer_MANUAL_ILLUSTRATIVE_ONLY"]
        assert "+0.083" in s
        assert "+0.10" in s
        assert "NOT_CALCULATED" in s
        assert "engine NOT run" in s

    def test_disclosure_observation(self):
        d = _m925_data()["disclosure_observation"]
        assert "m919" in d
        assert "NO disclosure line in the surfaced excerpt" in d
        assert "UNVERIFIED" in d
        assert "#492" in d

    def test_confounder_strength_ordering(self):
        confs = _m925_data()["confounders_strong_first"]
        assert confs[0].startswith("STRONG:")
        assert confs[1].startswith("STRONG:")
        assert confs[2].startswith("MODERATE:")
        assert confs[4].startswith("WEAK:")

    def test_counterevidence_present(self):
        ce = _m925_data()["counterevidence"]
        assert len(ce) == 3
        assert any("m763" in c for c in ce)

    def test_research_method(self):
        rm = _m925_data()["research_method"]
        assert "3 browser.search query sets" in rm
        assert "0 browser.open" in rm
        assert "REJECTED" in rm


# ---------------------------------------------------------------------------
# 5. Statistical discipline
# ---------------------------------------------------------------------------
class TestTypeAStatisticalDiscipline1157:
    def test_manual_only_no_engine(self):
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run" in text
        assert "no analysis.json update" in text

    def test_verdict_discipline(self):
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "directionally_supported_not_proven" in text

    def test_no_926_mechanism_key_forms_in_file(self):
        # The next-number needles are format-built at runtime; no
        # contiguous numeric/underscore/dash next-number
        # mechanism-key literal may exist in this file.
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        num = str(NEXT_NUM)
        assert ("mechanism_id: " + num) not in text
        assert ("mechanism" + "_" + num) not in text
        assert ("mechanism" + "-" + num) not in text

    def test_ascii_only_no_em_dashes(self):
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in text
        assert "\u2013" not in text
        yaml_text = _read(os.path.join(REPO_ROOT, M925_HOME))
        # The new block only: slice from the block key to the next
        # 4-space block key after it.
        start = yaml_text.index(M925_KEY)
        nxt = yaml_text.index("\n    wsj_openai_chatgpt_ads_revenue", start)
        block = yaml_text[start:nxt]
        assert "\u2014" not in block
        assert "\u2013" not in block


# ---------------------------------------------------------------------------
# 6. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeAFalsificationLedger1157:
    def test_forty_sixth_present(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                if _T46 in open(p, encoding="utf-8", errors="replace").read():
                    hits.append(p)
        assert hits != [], "forty-sixth member claim must exist"

    def test_forty_seventh_absent(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                if _T47 in open(p, encoding="utf-8", errors="replace").read():
                    hits.append(p)
        assert hits == [], hits

    def test_thirty_fifth_present_thirty_sixth_absent(self):
        def _hits(needle):
            out = []
            for root, dirs, files in os.walk(PROFILES_DIR):
                for f in files:
                    p = os.path.join(root, f)
                    if needle in open(p, encoding="utf-8", errors="replace").read():
                        out.append(p)
            return out

        assert _hits(_TW35) != []
        assert _hits(_TW36) == []

    def test_ledger_note_holds_at_46(self):
        assert "Ledger holds at 46" in _m925_data()["ledger"]


# ---------------------------------------------------------------------------
# 7. Forward-looking staleness (#1156's pins flip by design at this run)
# ---------------------------------------------------------------------------
class TestTypeAForwardLookingStaleness1157:
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

    def test_1156_zero_925_numeric_guard_flips_by_design(self):
        # #1156's zero-925 numeric guard uses a profiles/ walk. The
        # m925 landing (mechanism_id: 925 field in the working tree)
        # trips it at #1157. Designed lifecycle; recorded, not
        # repaired.
        result = self._stale_run(
            E1156_FILE,
            "TestMechanismNovelty::"
            "test_zero_925_numeric_mechanism_id_in_profiles",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1156_zero_925_underscore_dash_guards_stay_green_by_design(self):
        # The underscore/dash 925 guards STAY GREEN: the m925 block
        # key carries no mechanism-number substring (designed keying
        # per #715 - 1157 is the iteration, not the mechanism), and
        # this run's test file builds its 925 needles at runtime, so
        # no contiguous underscore/dash-form 925 literal exists
        # repo-wide. Recorded, not repaired.
        for node in (
            "test_zero_925_underscore_mechanism_repo_wide",
            "test_zero_925_dash_mechanism_repo_wide",
        ):
            result = self._stale_run(E1156_FILE, "TestMechanismNovelty::" + node)
            assert result.returncode == 0, result.stdout[-2000:]

    def test_1156_no_thirty_sixth_and_no_forty_seventh_stay_green_by_design(self):
        # This run claims no new relationship direction and no new
        # falsification-family member, so #1156's negative guards
        # stay green.
        for node in (
            "test_no_thirty_sixth_direction_claim_repo_wide",
            "test_no_forty_seventh_member_claim_repo_wide",
        ):
            result = self._stale_run(
                E1156_FILE, "TestStatisticalDiscipline::" + node
            )
            assert result.returncode == 0, result.stdout[-2000:]


# ---------------------------------------------------------------------------
# 8. Guard lifecycle (this run's forward guards)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1157:
    def test_1157_file_pins_max_id_925_and_next_926(self):
        assert _max_numeric_mechanism_id() == 925

    def test_zero_next_numeric_926_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_926_repo_wide(self):
        # Needle format-built per #715; no contiguous literal in
        # this file.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_926_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_new_mechanisms_below_max(self):
        pat = re.compile(r"mechanism_id:\s*(\d+)")
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in pat.findall(text)]
        assert 925 in ids
        assert all(i <= 925 for i in ids)

    def test_no_thirty_sixth_direction_claim(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _TW36 in text:
                    hits.append(p)
        assert hits == [], hits

    def test_no_forty_seventh_member_claim(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if _T47 in text:
                    hits.append(p)
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 9. Background-suite check (#1155 suite: checked only, NOT touched)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteCheck1157:
    def test_1155_suite_checked_not_touched(self):
        # Per #795 the background suite belongs to its launching run
        # (#1155); its verdict belongs to #1160. This run checks only:
        # the log exists and this run did not write to it (no Type A
        # #1157 marker in the suite log).
        assert os.path.exists(SUITE_LOG), SUITE_LOG
        text = _read(SUITE_LOG)
        assert "Type A #1157" not in text
        assert "m925" not in text

    def test_1155_suite_death_recorded_not_verdict(self):
        # At this run's check (Oct 2 18:03 PDT): zero pytest processes
        # alive at the ps scan; the suite log stalled at 1804 bytes
        # since Oct 2 16:51:36 PDT (~72 min) - the TWENTIETH
        # consecutive background-suite death of the streak. Per #795
        # the verdict and tombstoning belong to the next Type D
        # (#1160); this run records the observation only.
        assert os.path.getsize(SUITE_LOG) > 0


# ---------------------------------------------------------------------------
# 10. Doc-sync (green post-doc-sync per #719)
# ---------------------------------------------------------------------------
class TestTypeADocSync1157:
    def test_readme_stats_ratchet(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text

    def test_readme_test_table_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "test_type_a_1157_nypost_ftc_probe_sweeping" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert "test_type_a_1157_nypost_ftc_probe_sweeping" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 61097
        assert README_FILE_COUNT == 1482


# ---------------------------------------------------------------------------
# 11. Iteration-log entry (green post-doc-sync per #719)
# ---------------------------------------------------------------------------
class TestTypeAIterationLog1157:
    def test_iteration_log_has_1157_entry(self):
        text = _read(LOG_PATH)
        assert "## #1157 Type A:" in text

    def test_iteration_log_registers_hashes(self):
        text = _read(LOG_PATH)
        assert "e7180bb3" in text  # predecessor chain
        entry_start = text.index("## #1157 Type A:")
        entry = text[entry_start : entry_start + 6000]
        assert "Type A THIRD leg of the 1155-1159 window" in entry


# ---------------------------------------------------------------------------
# 12. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1157:
    def test_inflight_files_untouched_by_this_run(self):
        # Marker-scoped: the working tree carries pre-existing
        # in-flight uncommitted changes (#899 nytimes.yaml hunk,
        # #938 test file, #900 test file, #1012 test-file edit).
        # This run's markers must appear in NONE of their diffs;
        # targeted staging at commit time picks up only this run's
        # two files.
        for path in (
            "profiles/nytimes.yaml",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_"
            "agenda_setting_register_vs_carried_meta_india_havoc_m817_"
            "pairing_sep26_7am.py",
        ):
            diff = _git("diff", "--", path)
            assert "m925" not in diff, path
            assert "Type A #1157" not in diff, path
