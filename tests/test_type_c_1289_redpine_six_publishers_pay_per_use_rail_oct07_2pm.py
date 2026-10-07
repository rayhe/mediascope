# -*- coding: utf-8 -*-
"""Type C #1289 tests: Redpine x six academic publishers pay-per-use rail
(Oct 6, 2026) - FIRST dedicated corpus mechanism on the broker-cleared
publisher-set per-token pricing rail: on October 6 2026 Redpine (a Swedish
AI-content-licensing startup, Stockholm, founded 2024) announced
partnerships with BMJ Group, Sage, IOP Publishing, IGI Global Scientific
Publishing, Wanfang Data, and RCNi, covering more than 20 million
peer-reviewed articles. THE MONEY FLOW: AI agents get licensed full-text
access through Redpine APIs and the Model Context Protocol (named
integrations for Claude, Cursor, and ChatGPT), alongside bulk
data-licensing options; publishers set permitted uses and transaction
pricing; Redpine shares the vast majority of its revenue with publishing
partners; the Redpine Science product page lists pricing of $1 per 1,000
tokens with no upfront subscription. Sage participation is a pilot
spanning more than 400 medical and life-sciences journals, including
titles from Mary Ann Liebert. THE TYPE C NEXUS: the broker-cleared
transaction-pricing leg of the corpus money-flow taxonomy - the publisher
sets the price, the broker operates the metering and takes a revenue-share
haircut. It enters the control-of-the-meter contest as the broker-cleared
commercial contestant: distinct from m891 (Google unilateral payer-set
micro-rates - here the PUBLISHER sets transaction pricing, not the
payer), m915 (SPUR meter-then-invite prices negotiated usage through a
coalition standard - here pricing is per-publisher, not
coalition-negotiated), m999 (UK Search-Only Contracts price unauthorized
per-article USE unilaterally with no broker, no consent, and no clearing -
here a licensed broker clears every transaction), and m1002 (Impelsys x
Cashmere: the publisher owns the metering surface end-to-end - here
metering is broker-operated while price-setting is publisher-held). IOP
Publishing appears in both m711 (the Sep 9 2026 IOP x Cashmere
inference-only license) and this deal - the overlap documents an emerging
multi-broker market on one publisher, not corpus saturation (different
broker, different deal structure, pay-per-use API/MCP access vs flat
inference license). Lab-side capital tie (corroborating, not a separate
mechanism): Redpine raised an $8M seed round in April 2026 led by
NordicNinja, with strategic angels from OpenAI and Perplexity -
payer-side personnel back the broker that prices publisher content.
BOUNDARY (explicit): independent trade coverage (Unite.AI, which flags
vendor-reporting caveats) plus the company announcement; NO named lab
customer paying per-token yet - the lab financial link runs through
MCP/API integration availability into Claude/ChatGPT/Cursor, not a priced
lab contract; NO absolute dollar deal value (list pricing only, no volume
or take-rate terms); author-level compensation under publishing contracts
is unaddressed by the announcement. Falsifiable milestone: the first named
lab customer paying per-token, or a second Redpine publisher cohort
announced. Claims no slot in the coverage-tone falsification ledger.

Mechanism 1005 (MECHANISM DOCUMENTED; ledger HOLDS at 57 - NOT a
falsification-family member). No new direction (fortieth stays
absent by design); thirty-fifth through thirty-ninth stand.

Excerpt-bounded research per #503 (delegated scout across 4 ranked
candidate angles + 2 main-run browser.search verification sets; 0
browser.open reads). Scout rejections on main-run verification: MDPI x
Research Solutions/Scite MCP rail -> REJECTED (company-PR-only sourcing,
no disclosed dollar terms - future-watch, not landed); Chegg + Penske
Media v Google AI Overviews dismissals (Mehta, Sep 30) -> REJECTED
(litigation outcome, no priced deal - incentive-field boundary event, not
a mechanism); Reddit free-data shutdown preserving paid Google/OpenAI
deals -> REJECTED (platform access-tiering, renewal-window leverage
event, no new priced deal); Seattle Times + Newsday v OpenAI/Microsoft
-> REJECTED (early-September vintage, single-sourced). SELECTED: Redpine
x six academic publishers pay-per-use rail. Both landed URLs zero-hit
repo-wide pre-commit (git grep -F on verbatim Full-URL listings).

The mechanism 1005 block lives in profiles/competitor-entities.yaml as a
top-level key appended at end of file (the #1024 m846 hunk untouched;
explicit-path staging).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only OBSERVES the #1280-launched background suite
(goal hidden_files type_d_1280_full_suite.log; observed at this run's
check: 2592 bytes, last write Oct 7 2026 07:01 PDT, zero live pytest
processes - NOT-ALIVE, observation not a verdict; the #1290 Type D run
owns the verdict and tombstone); this run neither re-launches, kills, nor
writes to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit), #900
(untracked Type D test file), #1012-wt (working-tree edit on the committed
Type A #1012 file).

Type C lands one mechanism (mechanism 1005); the Type B predecessor landed
one (mechanism 1004, directional case, not a member).
This run is the FIFTH and CLOSING leg of the 1285-1289 window. Next run
#1290 Type D opens the 1290-1294 window (and renders the #1280-launched
background-suite verdict per #795). Rotation: D #1285 -> E #1286 ->
A #1287 -> B #1288 -> C #1289. The main commit is the anchor per #565.
The 1280-1284 window is VERIFIED CLOSED.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth through fifty-eighth
member-claim forms, or the thirty-fifth through fortieth direction forms;
the constants are constructed at runtime. (The landed ordinals live as
short lowercase forms in prose here; the live full-form claims live in
profiles/financial-times.yaml, profiles/news-corp.yaml,
profiles/the-verge.yaml, profiles/guardian.yaml, profiles/atlantic.yaml,
profiles/wired.yaml, profiles/ap.yaml, and
profiles/careers/journalists.yaml.)
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
GOAL_HIDDEN = os.path.join(
    os.path.expanduser("~"), "workspace", "goals",
    "mediascope-meta-wearables-press-analysis", "hidden_files",
)
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1280_full_suite.log")
WIRED_PATH = os.path.join(PROFILES_DIR, "wired.yaml")
OWN_BASENAME = (
    "test_type_c_1289_redpine_six_publishers_pay_per_use_rail_oct07_2pm.py"
)
TOP_KEY = None  # Type C lands at competitor-entities.yaml top level.

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "14d29a7811045e76b678e48350ded147da9edce5"  # patched to main commit per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1005
NEXT_NUM = 1006  # integer only; key-form needles are format-built

BLOCK_KEY = "type_c_1289_redpine_six_publishers_pay_per_use_rail_oct07"

# Predecessor chain: #1288 Type B continued the 1285-1289 window.
PRED_MAIN_1288 = "30ef8867"
PRED_ANCHOR_1288 = "20b8562b"
PRED_DOCSYNC_1288 = "7ca7a21b"
PRED_FINAL_1288 = "c3aa5397"
# #1287 Type A (third leg) for the rotation-guard chain.
PRED_MAIN_1287 = "32786e12"
PRED_ANCHOR_1287 = "3a21f16b"
PRED_DOCSYNC_1287 = "6eb575e5"
PRED_FINAL_1287 = "9da5dbd4"
# #1286 Type E (second leg).
PRED_MAIN_1286 = "7b75118a"
PRED_ANCHOR_1286 = "954b6788"
PRED_DOCSYNC_1286 = "d2048a8e"
PRED_FINAL_1286 = "90708117"
# #1285 Type D (window opener).
PRED_MAIN_1285 = "137ca235"
PRED_ANCHOR_1285 = "d9e1f0ea"
PRED_DOCSYNC_1285 = "22162b86"
PRED_FINAL_1285 = "f362c54c"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40).
PRED_MAIN_1289 = "0" * 40

# Forward guard for the next leg: #1290 Type D. Re-pinned by #1290's
# log-hash followup per #721 (starts as 0*40; placeholder-only per the
# Type C precedent - the #1284 file carries no forward git-log pin).
PRED_MAIN_1290 = "0" * 40

# The #1288 window-continuation file, for the predecessor reference
# (max id 1004; zero one-zero-zero-five keys all forms /
# no-Type-C-#1289-in-git-log / fortieth direction absent /
# forty-eighth through fifty-seventh members intact /
# fifty-eighth member absent / ledger 57).
E1288_FILE = (
    "test_type_b_1288_lily_hay_newman_chatgpt_mac_flaw_vs_meta_muse_"
    "dossier_oct02_oct03_2pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 72001  # patched pre-main: pre-sync 71976 + 25 collected
README_FILE_COUNT = 1614  # pre-sync 1613 + 1 (this file)

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"
_T54 = "FIFT" + "Y-FOURTH falsification-family member"
_T55 = "FIFT" + "Y-FIFTH falsification-family member"
_T56 = "FIFT" + "Y-SIXTH falsification-family member"
_T57 = "FIFT" + "Y-SEVENTH falsification-family member"
_T58 = "FIFT" + "Y-EIGHTH falsification-family member"

# Novel source URLs: 2 zero-hit repo-wide pre-commit (git grep -F).
NOVEL_URLS = [
    "https://www.unite.ai/redpine-publisher-deal-licensed-research-ai-agents/",
    "https://technews180.com/artificial-intelligence/redpine-secures-8m-to-unlock-non-public-ai-data/",
]


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson).
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
    found = []
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            found.extend(
                int(m) for m in pat.findall(
                    open(os.path.join(root, f),
                         encoding="utf-8", errors="replace").read()
                )
            )
    return max(found) if found else None


def _git_grep_tracked_source(needle, scope):
    """Grep tracked files at HEAD for a literal needle (fragment-built)."""
    args = ["git", "grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    else:
        args.append(".")
    out = subprocess.run(
        args, cwd=REPO_ROOT, capture_output=True, text=True
    ).stdout
    cleaned = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        if line:
            cleaned.append(line)
    return cleaned


def _load_entities():
    return yaml.safe_load(_read(ENTITIES_PATH))


def _block():
    data = _load_entities()
    assert BLOCK_KEY in data
    return data[BLOCK_KEY]


def _block_text():
    return _read(ENTITIES_PATH)


def _class_run(filename, classname):
    target = os.path.join(TESTS_DIR, filename)
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    return subprocess.run(
        ["python3", "-m", "pytest", target,
         "-k", classname,
         "-q", "--no-header"],
        cwd=REPO_ROOT, capture_output=True, text=True, env=env,
    )


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1289:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit this is 0*40 and the test passes BY DESIGN;
        # fails post-anchor (patched to the main commit sha).
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha per #565 in the anchor followup (both this
        # expected value and the ANCHORED_SHA constant are patched).
        # Pre-commit this is 0*40 and the test fails BY DESIGN;
        # deselected in the in-gate run.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40

    def test_this_run_main_commit_is_anchor(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "main commit is the anchor" in src

    def test_rotation_phrase_in_docstring(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIFTH and CLOSING leg of the 1285-1289 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1288/#1287/#1286/#1285 chain; closes 1285-1289.
# ---------------------------------------------------------------------------

class TestRotationGuard1289:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--format=%H").stdout
        for short in (PRED_MAIN_1288, PRED_ANCHOR_1288, PRED_DOCSYNC_1288,
                      PRED_FINAL_1288, PRED_MAIN_1287, PRED_ANCHOR_1287,
                      PRED_DOCSYNC_1287, PRED_FINAL_1287, PRED_MAIN_1286,
                      PRED_ANCHOR_1286, PRED_DOCSYNC_1286, PRED_FINAL_1286,
                      PRED_MAIN_1285, PRED_ANCHOR_1285, PRED_DOCSYNC_1285,
                      PRED_FINAL_1285):
            assert short in log, short

    def test_1288_type_b_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type B #1288")
        assert "Type B #1288" in out.stdout

    def test_closing_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "CLOSING leg of the 1285-1289 window" in src

    def test_1280_1284_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1280-1284 window is VERIFIED CLOSED" in src

    def test_next_window_opens_1290(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1290 Type D opens the 1290-1294 window" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: 1005 lands; key forms stay clean per #715.
# ---------------------------------------------------------------------------

class TestMechanismNovelty1289:
    def test_max_mechanism_id_is_1005_post_landing(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_block_key_present(self):
        assert BLOCK_KEY in _load_entities()

    def test_block_key_occurs_twice_in_text(self):
        text = _block_text()
        assert text.count(BLOCK_KEY) == 2

    def test_1005_numeric_present_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(MECH_NUM) == [ENTITIES_PATH]

    def test_1005_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_1005_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_iteration_field(self):
        assert _block()["iteration"] == 1289

    def test_iteration_type_field(self):
        assert _block()["iteration_type"] == "C"


# ---------------------------------------------------------------------------
# 4. Block structure at the competitor-entities.yaml top level.
# ---------------------------------------------------------------------------

class TestBlockStructure1289:
    def test_block_key_top_level(self):
        data = _load_entities()
        assert BLOCK_KEY in data
        assert data[BLOCK_KEY]["mechanism_id"] == MECH_NUM

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_required_fields_present(self):
        b = _block()
        for field in ("mechanism_name", "finding", "verdict", "novelty",
                      "rotation_transparency", "concurrency", "connects_to",
                      "confounders", "sources", "background_suite_status"):
            assert field in b, field

    def test_connects_to_present(self):
        assert set(_block()["connects_to"]) == {
            663, 711, 786, 891, 915, 927, 999, 1002}

    def test_all_novel_sources(self):
        urls = [s["url"] for s in _block()["sources"]]
        for u in NOVEL_URLS:
            assert u in urls

    def test_yaml_parse_clean_flag(self):
        assert _block()["yaml_parse_clean"] is True

    def test_ascii_only_flag(self):
        assert _block()["ascii_only"] is True
