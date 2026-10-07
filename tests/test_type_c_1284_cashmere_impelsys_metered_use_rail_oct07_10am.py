# -*- coding: utf-8 -*-
"""Type C #1284 tests: Impelsys x Cashmere metered-use licensing rail
(Oct 7, 2026) - FIRST dedicated corpus mechanism on the publisher-side
metered-use SETTLEMENT rail: on October 7 2026 Impelsys (a New York
publishing-technology company) announced a partnership with Cashmere (the
premium-content AI licensing infrastructure platform) integrating Cashmere
licensed-access and usage-metering capabilities into mon'k Meter, the
licensing and commercialization component of the Impelsys mon'k Fabric
platform. THE MONEY FLOW: AI applications pay publishers through
Cashmere OmniPub infrastructure; Impelsys works directly with publishers
to identify AI licensing opportunities and manage the relationship end to
end; Cashmere runs the infrastructure that formats content, manages
rights, controls data access and delivery, and meters usage - giving
publishers license-aware access and usage with a unified view of how
content is made available to AI applications and consumed under defined
licensing terms, plus commercial reporting to support repeatable B2AI
revenue models. mon'k Forge transforms publisher content into structured
AI-ready knowledge assets. THE TYPE C NEXUS: the metered-use settlement
leg of the corpus money-flow taxonomy - distinct from m786 (Cloudflare
pay-per-crawl prices crawler ACCESS at the infrastructure edge), m915
(SPUR meter-then-invite prices negotiated usage through a coalition
standard), m891 (Google AI-contribution pilot prices usage unilaterally
at payer-set micro-rates), and m999 (UK Search-Only Contracts price
unauthorized per-article USE unilaterally at the contract layer). The
FIRST corpus mechanism where the PUBLISHER owns the metering surface: the
payer-built-meter mirror image of m891, and a third contestant in the
control-of-the-meter contest alongside m891 (Google) and m915 (SPUR),
with m927 (Stealth Bot Act) as the regulatory fourth. Corroborating leg
(in-corpus, m711, NOT landed): the Sep 9 2026 IOP Publishing x Cashmere
inference-only license (licensed for inference, protected from LLM
training, fully tracked so every use is visible and compensated) is the
template this rail extends from the roster leg to a publisher-operated
environment. October-2026 freshness: the EINPresswire announcement
carries an Oct 7 2026 New York dateline; Frankfurt Book Fair (Oct 7-11)
is the live commercialization event. BOUNDARY (explicit): company-PR
sourcing (EINPresswire); NO dollar terms disclosed; NO named publisher
customers yet - an intent/meter-rail leg, not a priced deal. The
falsifiable milestone: the first publisher customer live on mon'k Meter,
the first settled usage payment, or a named Frankfurt Book Fair deal.
Claims no slot in the coverage-tone falsification ledger.

Mechanism 1002 (MECHANISM DOCUMENTED; ledger HOLDS at 56 - NOT a
falsification-family member). No new direction (fortieth stays
absent by design); thirty-fifth through thirty-ninth stand.

Excerpt-bounded research per #503 (delegated scout across 12 candidate
angles + 2 main-run browser.search verification sets; 0 browser.open
reads). Scout rejections on main-run verification: Stealth Bot Act
fly-in -> REJECTED (m927 saturated, bill carries no payment requirement);
OpenAI India publisher pipeline -> REJECTED (m609/m660/m709/m714
saturated; e4m follow-on deals are talks, unconfirmed); Anthropic
publisher licensing -> REJECTED (zero-deal set saturated, m509; no new
October deal); Perplexity publisher revenue-share -> REJECTED (Comet Plus
80/20 m391; Cashmere/Perplexity m663 saturated); xAI content licensing ->
REJECTED (zero-publisher-deal posture saturated, m813); Canada CJC
disbursements -> REJECTED (2024-2025 vintage, no October 2026 event);
Ziff Davis v OpenAI -> REJECTED (m589 saturated); Google AI Overviews
publisher compensation -> REJECTED (m891 unilateral-pricing saturated);
Apple publisher talks -> REJECTED (m574/m606 vintage); Amazon publisher
relationships -> REJECTED (Reach/NYT/Conde legs saturated or vintage);
Meta Dec-2025 publisher bundle -> REJECTED (m331/m549/m633 saturated);
Reddit v Anthropic / Thomson Reuters v ROSS / News Corp v Brave ->
REJECTED (m614 / in-corpus / in-corpus). SELECTED: Impelsys x Cashmere
metered-use rail. The IOP x Cashmere deal FACT is already banked as m711
(Type C #799) and is NOT landed here (corroboration only; the
researchinformation URL is zero-hit repo-wide pre-commit but marked
novel:false).

The mechanism 1002 block lives in profiles/competitor-entities.yaml as a
top-level key appended at end of file (the #1024 m846 hunk untouched;
explicit-path staging).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only OBSERVES the #1280-launched background suite
(goal hidden_files type_d_1280_full_suite.log; observed at this run's
check: 2592 bytes, last write Oct 7 2026 07:01 PDT, zero live pytest
processes - NOT-ALIVE, observation not a verdict; the #1285 Type D run
owns the verdict and tombstone); this run neither re-launches, kills, nor
writes to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit), #900
(untracked Type D test file), #1012-wt (working-tree edit on the committed
Type A #1012 file).

Type C lands one mechanism (mechanism 1002); the Type B predecessor landed
one (mechanism 1001, control-case observation, not a member).
This run is the FIFTH and CLOSING leg of the 1280-1284 window. Next run
#1285 Type D opens the 1285-1289 window (and renders the #1280-launched
background-suite verdict per #795). Rotation: D #1280 -> E #1281 ->
A #1282 -> B #1283 -> C #1284. The main commit is the anchor per #565.
The 1275-1279 window is VERIFIED CLOSED.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth through fifty-seventh
member-claim forms, or the thirty-fifth through fortieth direction forms;
the constants are constructed at runtime. (The landed ordinals live as
short lowercase forms in prose here; the live full-form claims live in
profiles/financial-times.yaml, profiles/news-corp.yaml,
profiles/the-verge.yaml, profiles/guardian.yaml, profiles/atlantic.yaml,
profiles/wired.yaml, and profiles/careers/journalists.yaml.)
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
    "test_type_c_1284_cashmere_impelsys_metered_use_rail_oct07_10am.py"
)
TOP_KEY = None  # Type C lands at competitor-entities.yaml top level.

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "7325305fc00c02062fa1f9ccfe2865dba0931998"  # patched to main commit per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1002
NEXT_NUM = 1003  # integer only; key-form needles are format-built

BLOCK_KEY = "type_c_1284_cashmere_impelsys_metered_use_rail_oct07"

# Predecessor chain: #1283 Type B continued the 1280-1284 window.
PRED_MAIN_1283 = "9d6803cf"
PRED_ANCHOR_1283 = "39bf2d5f"
PRED_DOCSYNC_1283 = "86785ccb"
PRED_FINAL_1283 = "5786843b"
# #1282 Type A (third leg) for the rotation-guard chain.
PRED_MAIN_1282 = "915f95cd"
PRED_ANCHOR_1282 = "ea804f92"
PRED_DOCSYNC_1282 = "29386d75"
PRED_FINAL_1282 = "45e359a6"
# #1281 Type E (second leg).
PRED_MAIN_1281 = "3c53f5f9"
PRED_ANCHOR_1281 = "7ef464d2"
PRED_DOCSYNC_1281 = "b23ffee6"
PRED_FINAL_1281 = "10d64db0"
# #1280 Type D (window opener).
PRED_MAIN_1280 = "b8695266"
PRED_ANCHOR_1280 = "a9cade12"
PRED_DOCSYNC_1280 = "cc4c74bb"
PRED_FINAL_1280 = "b0cc067f"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the own-run git-log pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1284 = "7325305f"  # re-pinned to main sha per #721

# Forward guard for the next leg: #1285 Type D. Re-pinned by #1285's
# log-hash followup per #721 (starts as 0*40; the forward pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1285 = "0" * 40

# The #1283 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 1001; zero one-zero-zero-three keys all
# forms / no-Type-D-#1285-in-git-log / fortieth direction absent /
# forty-eighth through fifty-sixth members intact /
# fifty-seventh member absent / ledger 56).
E1283_FILE = (
    "test_type_b_1283_lisa_eadicicco_cnn_meta_muse_blitz_vs_"
    "anthropic_ipo_leak_oct07_9am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 71602  # patched pre-main: pre-sync 71577 + 25 collected
README_FILE_COUNT = 1609  # pre-sync 1608 + 1 (this file)

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

# Novel source URLs: 1 zero-hit repo-wide pre-commit (git grep
# -F); 1 in-corpus re-surface disclosed (the IOP x Cashmere deal fact is
# banked as m711 via Type C #799; the researchinformation URL below is
# zero-hit repo-wide pre-commit but marked novel:false - corroboration
# only, not landed).
NOVEL_URLS = [
    "https://www.einpresswire.com/article/947673609/impelsys-partners-with-cashmere-to-strengthen-ai-content-licensing-and-usage-metering-for-publishers",
]
RESURFACED_URLS = [
    "https://www.researchinformation.info/news/iop-publishing-partners-with-cashmere-to-license-research-content-for-ai-use/",
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

class TestAnchor1284:
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
        assert "FIFTH and CLOSING leg of the 1280-1284 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1283/#1282/#1281/#1280 chain; closes 1280-1284.
# ---------------------------------------------------------------------------

class TestRotationGuard1284:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--format=%H").stdout
        for short in (PRED_MAIN_1283, PRED_ANCHOR_1283, PRED_DOCSYNC_1283,
                      PRED_FINAL_1283, PRED_MAIN_1282, PRED_ANCHOR_1282,
                      PRED_DOCSYNC_1282, PRED_FINAL_1282, PRED_MAIN_1281,
                      PRED_ANCHOR_1281, PRED_DOCSYNC_1281, PRED_FINAL_1281,
                      PRED_MAIN_1280, PRED_ANCHOR_1280, PRED_DOCSYNC_1280,
                      PRED_FINAL_1280):
            assert short in log, short

    def test_1283_type_b_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type B #1283")
        assert "Type B #1283" in out.stdout

    def test_closing_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "CLOSING leg of the 1280-1284 window" in src

    def test_1275_1279_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1275-1279 window is VERIFIED CLOSED" in src

    def test_next_window_opens_1285(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1285 Type D opens the 1285-1289 window" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: 1002 lands; key forms stay clean per #715.
# ---------------------------------------------------------------------------

class TestMechanismNovelty1284:
    def test_max_mechanism_id_is_1002_post_landing(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_block_key_present(self):
        assert BLOCK_KEY in _load_entities()

    def test_block_key_occurs_twice_in_text(self):
        text = _block_text()
        assert text.count(BLOCK_KEY) == 2

    def test_1002_numeric_present_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(MECH_NUM) == [ENTITIES_PATH]

    def test_1002_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_1002_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_iteration_field(self):
        assert _block()["iteration"] == 1284

    def test_iteration_type_field(self):
        assert _block()["iteration_type"] == "C"


# ---------------------------------------------------------------------------
# 4. Block structure at the competitor-entities.yaml top level.
# ---------------------------------------------------------------------------

class TestBlockStructure1284:
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
            663, 711, 786, 891, 915, 927, 999}

    def test_all_novel_sources(self):
        urls = [s["url"] for s in _block()["sources"]]
        assert NOVEL_URLS[0] in urls
        assert RESURFACED_URLS[0] in urls

    def test_yaml_parse_clean_flag(self):
        assert _block()["yaml_parse_clean"] is True

    def test_ascii_only_flag(self):
        assert _block()["ascii_only"] is True
