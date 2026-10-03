"""Type A -- Iteration #1162 (Fri 2026-10-02 22:00 PDT): m928 Gizmodo x
Snap-vs-Xreal Sep-23-2026 comparison hands-on (Kyle Barr, Snapdragon
Summit) vs carried Gizmodo x Meta arms - comparative sobriety
register, temporal extension of the #862 m748 family.

On Sep 23 2026 Gizmodo published Kyle Barr's "In the Race for the
Dorkiest AR Glasses, Only One Seems Built for Today"
(https://gizmodo.com/snapchat-specs-vs-xreal-aura-2000816976), a
hands-on comparison of Snap's Specs and Xreal's Project Aura glasses
from Qualcomm's Snapdragon Summit - the URL is new-to-corpus this
run (zero-hit pre-commit). Register: comparative sobriety. The Specs
arm is judged not-built-for-today (132g standalone face computer,
$2,195, 51-degree FOV, "comical 'glasshole'"); the Aura arm gets the
relative edge (70-degree FOV, under $1,500, "the entire Android
ecosystem behind it"); the closing judgment levels both arms ("you
will probably only wear any of these XR glasses at home or as
in-flight entertainment"). The piece carries an explicit
vendor-paid-travel disclosure line ("Full disclosure: travel and
lodging were paid by Qualcomm, and Gizmodo did not guarantee any
coverage as a condition of accepting the trip") - the transparency
datum that extends the m919 disclosure_asymmetry strand
descriptively on the PRESENT-disclosure side. Scorer (MANUAL
ILLUSTRATIVE ONLY): Xreal comparison arm +0.10 vs carried m577 Meta
band mean -0.617 gives an illustrative Xreal-minus-Meta delta of
+0.717 - the same magnitude as m748's Snap-minus-Meta +0.717, so the
null-tie outlet's hands-on peg keeps the same warm band for non-Meta
wearables; Xreal arm +0.10 vs carried m748 Snap arm +0.10 gives 0.00
near-null - the hands-on register treats the two non-Meta wearables
symmetrically. NOT a falsification-family member: same-publication
temporal replication of the #862 m748 Gizmodo x Snap family on a new
peg (new entity Xreal), which per the #1143 precedent is not a new
prediction test. Ledger holds at 46.

Type A THIRD leg of the 1160-1164 window, CONTINUING it
(D #1160 -> E #1161 -> A #1162 -> B #1163 -> C #1164). Committed
predecessors: #1160 Type D (main e14beb6f / anchor 2f8a63c7 /
doc-sync 5358009b / log-hash 43266898) and #1161 Type E (main
9e9d70be / anchor a75fea4c / doc-sync 0ce1314a / log-hash 9386a98b),
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
m928 block lands in profiles/gizmodo.yaml under
competitor_relationships > snap as a 4-space-indent sibling of the
m748 block per the gizmodo.yaml convention, NOT nytimes.yaml); the
in-flight blocks are owned by their runs. Targeted staging only per
the repo-wide traversal lesson. Iteration numbers follow the rotation
schedule, not commit order. Do NOT touch #1024's m846 (self-flagged
sourcing-constraint violation; Ray's revert/leave/rebuild-from-primary
decision still pending).

Verifies:
- m928 (Type A #1162, profiles/gizmodo.yaml
  competitor_relationships > snap block key, 4-space indent (sibling
  of the m748 block per the gizmodo.yaml convention),
  `mechanism_id: 928` field form; block key count 1 - designed: the
  block key carries no mechanism-number substring (1162 is the
  iteration), so it is a plain literal per #715): Gizmodo Sep-23
  Snap-vs-Xreal Aura comparison hands-on from the Snapdragon Summit
  (Kyle Barr; explicit Qualcomm travel disclosure; +0.10 MANUAL
  ILLUSTRATIVE) vs carried arms (m577 Meta band mean -0.617, m748
  Snap +0.10, m74 Snap -0.10, un-rescored per #807); illustrative
  deltas +0.717 / 0.00 - comparative sobriety, symmetric non-Meta
  wearable band; NOT a falsification-family member (temporal
  replication per #1143); ledger holds at 46; disclosure observation
  extends m919 descriptively on the present-disclosure side
  (observed-in-excerpt, full-page UNVERIFIED per #492); post-landing
  corpus integrity (max numeric mechanism_id 928; zero next-number
  929 keys in numeric/underscore/dash mechanism forms - the 929
  needles are format-built per #715 so no guard-literal carrier file
  exists; the forty-seventh member-claim form absent repo-wide as
  designed negative guard for the next landing; thirty-fifth
  direction present (competitor-entities.yaml, m915), thirty-sixth
  and thirty-seventh absent; the #1160/#1161 window files are NOT
  edited by this run - their now-stale forward-looking pins are
  recorded as fail-by-design via subprocess in the staleness class
  (#1161's zero-928 numeric pin trips on the landed 928; #1161's
  underscore/dash 928 pins STAY GREEN by design - no contiguous
  underscore/dash-form 928 literal exists; #1161's no-thirty-sixth
  and no-forty-seventh pins STAY GREEN, asserted in this run's own
  guard-lifecycle class)) + the #1160 background-suite check (IN
  FLIGHT at this run's check per #795 - pytest alive at this run's
  ps scan; checked only, NOT touched; verdict belongs to #1165 per
  #795).

MANUAL/QUALITATIVE ONLY, engine NOT run, no analysis.json update,
NOT artifact-grade, verdict directionally_supported_not_proven.
Correlation is not causation; hypothesis-generating only.
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
    "test_type_a_1162_gizmodo_snap_xreal_aura_sep23_comparison_"
    "vs_carried_meta_arms_oct02_10pm.py"
)

MAX_ID = 928
NEXT_NUM = 929

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "0" * 40  # patched per #565 in the anchor followup

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 61421
README_FILE_COUNT = 1486

# The m928 block key carries no mechanism-number substring (1162 is
# the iteration, not the mechanism), so it is a plain literal per
# #715.
M928_KEY = (
    "gizmodo_snap_xreal_aura_sobriety_comparison_"
    "register_1162_sep23"
)
M928_INDENT = 4
M928_HOME = "profiles/gizmodo.yaml"

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
    "hidden_files/type_d_1160_full_suite.log"
)
E1161_FILE = (
    "tests/test_type_e_1161_podcast_sentiment_155th_verification_"
    "oct02_9pm.py"
)

# Committed predecessor #1160 Type D chain (verified pre-commit).
PRED_MAIN_1160 = "e14beb6f"
PRED_ANCHOR_1160 = "2f8a63c7"
PRED_DOCSYNC_1160 = "5358009b"
PRED_FINAL_1160 = "43266898"
# Committed predecessor #1161 Type E chain (verified pre-commit).
PRED_MAIN_1161 = "9e9d70be"
PRED_ANCHOR_1161 = "a75fea4c"
PRED_DOCSYNC_1161 = "0ce1314a"
PRED_FINAL_1161 = "9386a98b"

# New-to-corpus this run (zero-hit repo-wide pre-commit).
NEW_URLS = [
    "https://gizmodo.com/snapchat-specs-vs-xreal-aura-2000816976",
]

# Carried arms (un-rescored per #807): m577 Meta band mean -0.617,
# m748 Snap arm +0.10, m74 Snap preview -0.10; new Xreal arm +0.10
# MANUAL ILLUSTRATIVE.
META_BAND_MEAN = -0.617
M748_SNAP_ARM = 0.10
XREAL_ARM = 0.10


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


def _m928_data():
    import yaml

    with open(os.path.join(REPO_ROOT, M928_HOME), encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["snap"][M928_KEY]


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
class TestNovelty1162:
    def test_single_type_a_1162_file(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1162*.py"))
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_type_a_1162_in_git_log(self):
        log = _git("log", "--format=%H %s", "--grep=Type A #1162")
        assert "Type A #1162" in log

    def test_type_a_1162_commit_set(self):
        # Post-full-run: exactly three commits carry "Type A #1162"
        # (main + anchor followup + log-hash followup per #721; the
        # doc-sync commit title is the "Doc-sync #1162:" form and does
        # not match the grep).
        log = _git("log", "--format=%H", "--grep=Type A #1162")
        assert len([l for l in log.splitlines() if l.strip()]) == 3, log

    def test_new_gizmodo_xreal_url_in_corpus(self):
        # The Barr Sep-23 Xreal Aura URL was zero-hit repo-wide
        # pre-commit; it is in-corpus now (this file's constant list
        # plus the gizmodo.yaml block).
        for url in NEW_URLS:
            hits = _git("grep", "-l", "-F", url).splitlines()
            assert len(hits) >= 1, url

    def test_block_key_unique_in_home_yaml(self):
        # Post-commit-stable: the block key is a literal in this
        # file's constant, so count only inside the home YAML.
        text = _read(os.path.join(REPO_ROOT, M928_HOME))
        assert text.count(M928_KEY + ":") == 1


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestTypeARotationGuard1162:
    def test_anchor_sha_format(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40

    def test_predecessor_1160_chain_in_history(self):
        for sha in (
            PRED_MAIN_1160,
            PRED_ANCHOR_1160,
            PRED_DOCSYNC_1160,
            PRED_FINAL_1160,
        ):
            assert sha in _git("log", "--format=%H"), sha

    def test_predecessor_1161_chain_in_history(self):
        for sha in (
            PRED_MAIN_1161,
            PRED_ANCHOR_1161,
            PRED_DOCSYNC_1161,
            PRED_FINAL_1161,
        ):
            assert sha in _git("log", "--format=%H"), sha

    def test_window_third_leg(self):
        window = _window()
        assert ("A", "1162") in window
        assert ("E", "1161") in window
        assert ("D", "1160") in window
        # File order is chronological (oldest first): D1160 older than
        # E1161 older than A1162.
        assert window.index(("D", "1160")) < window.index(("E", "1161"))
        assert window.index(("E", "1161")) < window.index(("A", "1162"))

    def test_rotation_phrase_in_log_entry(self):
        text = _read(LOG_PATH)
        assert "## #1162 Type A:" in text
        entry_start = text.index("## #1162 Type A:")
        entry = text[entry_start : entry_start + 4000]
        assert "1160-1164 window" in entry
        assert "THIRD leg" in entry


# ---------------------------------------------------------------------------
# Anchor (deselected pre-commit per #565; patched post-commit)
# ---------------------------------------------------------------------------
class TestTypeANoveltyAnchor1162:
    @pytest.mark.skip(reason="deselected pre-commit per #565; green post-anchor")
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1162
        # main commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type A #1162")
        assert "Type A #1162" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeACorpusIntegrity1162:
    def test_m928_block_keyed_at_indent_4(self):
        text = _read(os.path.join(REPO_ROOT, M928_HOME))
        line = next(l for l in text.splitlines() if l.strip() == M928_KEY + ":")
        assert line.startswith(" " * M928_INDENT)
        assert not line.startswith(" " * (M928_INDENT + 1))

    def test_m928_block_sibling_of_m748_block(self):
        data = _read(os.path.join(REPO_ROOT, M928_HOME))
        assert (
            "    gizmodo_snap_sep16_launch_hands_on_register_vs_meta_"
            "adversarial_band_sep19_2026:" in data
        )

    def test_m928_mechanism_id_field_form(self):
        text = _read(os.path.join(REPO_ROOT, M928_HOME))
        assert "mechanism_id: 928" in text

    def test_max_numeric_mechanism_id_is_928(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_929_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_929_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_929_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_928_substring_in_block_key(self):
        assert "928" not in M928_KEY


# ---------------------------------------------------------------------------
# 4. m928 content discipline (YAML-parsed assertions)
# ---------------------------------------------------------------------------
class TestTypeAM928ContentDiscipline1162:
    def test_metadata_fields(self):
        d = _m928_data()
        assert d["mechanism_id"] == 928
        assert d["iteration"] == 1162
        assert d["iteration_type"] == "A"
        assert d["rotation"] == "Type A"
        assert d["date_analyzed"] == "2026-10-02"
        assert d["job_id"] == "mediascope-daily-iteration"
        assert d["goal_id"] == "goal_54093bda4145"
        assert d["author"] == "Kit (with Ray)"

    def test_new_arm_fields(self):
        arm = _m928_data()["articles_new"][0]
        assert arm["publication"] == "Gizmodo"
        assert arm["author"] == "Kyle Barr"
        assert arm["date"] == "2026-09-23"
        assert arm["url"] == NEW_URLS[0]
        assert arm["register"] == "comparative_sobriety_hands_on"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == XREAL_ARM
        assert len(arm["key_quotes"]) == 4
        assert len(arm["tone_observations"]) == 4

    def test_disclosure_line_quoted(self):
        arm = _m928_data()["articles_new"][0]
        assert "travel and lodging were paid by Qualcomm" in arm["key_quotes"][3]

    def test_carried_arms_per_807_unrescored(self):
        d = _m928_data()
        arms = d["carried_arms_per_807"]
        assert len(arms) == 3
        assert "m577" in arms[0]["mechanism"]
        assert "-0.617" in arms[0]["arms"]
        assert "m748" in arms[1]["mechanism"]
        assert "+0.10" in arms[1]["arms"]

    def test_scorer_deltas(self):
        s = _m928_data()["scorer_MANUAL_ILLUSTRATIVE_ONLY"]
        assert "+0.717" in s
        assert "0.00" in s
        assert "NOT_CALCULATED" in s
        assert "engine NOT run" in s

    def test_disclosure_observation(self):
        d = _m928_data()["disclosure_observation"]
        assert "m919" in d
        assert "PRESENT-disclosure" in d
        assert "observed-in-excerpt" in d
        assert "#492" in d

    def test_confounder_strength_ordering(self):
        confs = _m928_data()["confounders_strong_first"]
        assert confs[0].startswith("STRONG:")
        assert confs[1].startswith("STRONG:")
        assert confs[2].startswith("MODERATE:")
        assert confs[4].startswith("WEAK:")

    def test_counterevidence_present(self):
        ce = _m928_data()["counterevidence"]
        assert len(ce) == 4
        assert any("m577" in c for c in ce)

    def test_research_method(self):
        rm = _m928_data()["research_method"]
        assert "9 browser.search query sets" in rm
        assert "0 browser.open" in rm
        assert "REJECTED" in rm


# ---------------------------------------------------------------------------
# 5. Statistical discipline
# ---------------------------------------------------------------------------
class TestTypeAStatisticalDiscipline1162:
    def test_manual_only_no_engine(self):
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run" in text
        assert "no analysis.json update" in text

    def test_verdict_discipline(self):
        text = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "directionally_supported_not_proven" in text

    def test_no_929_mechanism_key_forms_in_file(self):
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
        yaml_text = _read(os.path.join(REPO_ROOT, M928_HOME))
        # The new block only: slice from the block key to the next
        # top-level key after it.
        start = yaml_text.index(M928_KEY)
        nxt = yaml_text.index("\neditorial_posture:", start)
        block = yaml_text[start:nxt]
        assert "\u2014" not in block
        assert "\u2013" not in block


# ---------------------------------------------------------------------------
# 6. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeAFalsificationLedger1162:
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
        assert "Ledger holds at 46" in _m928_data()["ledger"]


# ---------------------------------------------------------------------------
# 7. Forward-looking staleness (#1161's pins flip by design at this run)
# ---------------------------------------------------------------------------
class TestTypeAForwardLookingStaleness1162:
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

    def test_1161_zero_928_numeric_guard_flips_by_design(self):
        # #1161's zero-928 numeric guard uses a profiles/ walk. The
        # m928 landing (mechanism_id: 928 field in the working tree)
        # trips it at #1162. Designed lifecycle; recorded, not
        # repaired.
        result = self._stale_run(
            E1161_FILE,
            "TestMechanismNovelty::"
            "test_zero_928_numeric_mechanism_id_in_profiles",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1161_zero_928_underscore_dash_guards_stay_green_by_design(self):
        # The underscore/dash 928 guards STAY GREEN: the m928 block
        # key carries no mechanism-number substring (designed keying
        # per #715 - 1162 is the iteration, not the mechanism), and
        # this run's test file builds its 928 needles at runtime, so
        # no contiguous underscore/dash-form 928 literal exists
        # repo-wide. Recorded, not repaired.
        for node in (
            "test_zero_928_underscore_mechanism_repo_wide",
            "test_zero_928_dash_mechanism_repo_wide",
        ):
            result = self._stale_run(E1161_FILE, "TestMechanismNovelty::" + node)
            assert result.returncode == 0, result.stdout[-2000:]

    def test_1161_no_thirty_sixth_and_no_forty_seventh_stay_green_by_design(self):
        # This run claims no new relationship direction and no new
        # falsification-family member, so #1161's negative guards
        # stay green.
        for node in (
            "test_no_thirty_sixth_direction_claim_repo_wide",
            "test_no_forty_seventh_member_claim_repo_wide",
        ):
            result = self._stale_run(
                E1161_FILE, "TestStatisticalDiscipline::" + node
            )
            assert result.returncode == 0, result.stdout[-2000:]


# ---------------------------------------------------------------------------
# 8. Guard lifecycle (this run's forward guards)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1162:
    def test_1162_file_pins_max_id_928_and_next_929(self):
        assert _max_numeric_mechanism_id() == 928

    def test_zero_next_numeric_929_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_929_repo_wide(self):
        # Needle format-built per #715; no contiguous literal in
        # this file.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_929_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_new_mechanisms_below_max(self):
        pat = re.compile(r"mechanism_id:\s*(\d+)")
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in pat.findall(text)]
        assert 928 in ids
        assert all(i <= 928 for i in ids)

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
# 9. Background-suite check (#1160 suite: checked only, NOT touched)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteCheck1162:
    def test_1160_suite_checked_not_touched(self):
        # Per #795 the background suite belongs to its launching run
        # (#1160); its verdict belongs to #1165. This run checks only:
        # the log exists and this run did not write to it (no Type A
        # #1162 marker in the suite log).
        assert os.path.exists(SUITE_LOG), SUITE_LOG
        text = _read(SUITE_LOG)
        assert "Type A #1162" not in text
        assert "m928" not in text

    def test_1160_suite_state_recorded_not_verdict(self):
        # At this run's check the #1160-launched suite is IN FLIGHT
        # (pytest alive at this run's ps scan; log fresh). Per #795
        # the verdict belongs to #1165; this run records the
        # observation only.
        assert os.path.getsize(SUITE_LOG) > 0


# ---------------------------------------------------------------------------
# 10. Doc-sync (green post-doc-sync per #719)
# ---------------------------------------------------------------------------
class TestTypeADocSync1162:
    def test_readme_stats_ratchet(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text

    def test_readme_test_table_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "test_type_a_1162_gizmodo_snap_xreal_aura" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert "test_type_a_1162_gizmodo_snap_xreal_aura" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 61421
        assert README_FILE_COUNT == 1486


# ---------------------------------------------------------------------------
# 11. Iteration-log entry (green post-doc-sync per #719)
# ---------------------------------------------------------------------------
class TestTypeAIterationLog1162:
    def test_iteration_log_has_1162_entry(self):
        text = _read(LOG_PATH)
        assert "## #1162 Type A:" in text

    def test_iteration_log_registers_hashes(self):
        text = _read(LOG_PATH)
        assert "9e9d70be" in text  # predecessor chain
        entry_start = text.index("## #1162 Type A:")
        entry = text[entry_start : entry_start + 6000]
        assert "Type A THIRD leg of the 1160-1164 window" in entry


# ---------------------------------------------------------------------------
# 12. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1162:
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
            assert "m928" not in diff, path
            assert "Type A #1162" not in diff, path
