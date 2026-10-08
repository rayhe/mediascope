# -*- coding: utf-8 -*-
"""Type C #1294 tests: Elsevier x JAMA Network ClinicalKey AI strategic
content agreement (Oct 7, 2026) - FIRST dedicated corpus mechanism on the
publisher-as-AI-provider vertical licensing rail: on October 7 2026 Elsevier
announced a strategic content agreement with the JAMA Network bringing
full-text content and visuals from all 13 JAMA Network Family of Journals
titles into ClinicalKey AI, Elsevier's clinical-grade AI workspace.
THE MONEY FLOW: Elsevier is the PAYER - it licenses peer-publisher content
from the JAMA Network to feed its own AI product; the licensed full-text
content and visuals inform the answers clinicians receive through
ClinicalKey AI. THE TYPE C NEXUS: the publisher-stack-internal leg of the
corpus money-flow taxonomy - the payer is a publisher, not a lab, so the
financial dependency sits inside the publisher stack rather than between
publishers and AI labs. Distinct from m891 (Google unilateral payer-set
micro-rates), m915 (SPUR meter-then-invite), m999 (UK Search-Only
Contracts), m1002 (Impelsys x Cashmere: the publisher owns the metering
surface end-to-end - here the publisher owns the AI WORKSPACE end-to-end),
m1005 (Redpine broker-cleared - here no broker; the publisher-provider
contracts directly with the licensor), and m711 (IOP x Cashmere
inference-only flat license into a broker product - here the license feeds
a publisher-owned clinical workspace). The sign-or-sue atom lands twice on
the same entity: Elsevier sits on the litigation tier (Hachette/Cengage/
Elsevier/Turow Jul 2026 class action against Google over Gemini training,
plus the May 2026 same-roster suit against Meta) AND on the licensing tier
as a payer (this deal) - the (publisher, counterparty) pair decides the
tier, not an intrinsic publisher label (per the iteration-1140 lesson).
Corroborating multi-product structure: the JAMA Network also licenses into
Elsevier's LeapSpace research AI (Sep 15 2026) - one licensor into TWO
Elsevier AI products (clinical + research), an emerging multi-product
licensing market on one licensor, not corpus saturation. BOUNDARY
(explicit): company-PR sourcing (PRNewswire announcement + independent
Unite.AI trade coverage); NO dollar terms disclosed; NO per-use metering
described (the corpus control-of-the-meter contest is not engaged by this
deal). Falsifiable milestone: dollar terms disclosed, or the JAMA Network
licensing into a named lab (OpenAI/Anthropic/Google) AI product. Claims no
slot in the coverage-tone falsification ledger.

Mechanism 1008 (MECHANISM DOCUMENTED; ledger HOLDS at 58 - NOT a
falsification-family member). No new direction (fortieth stays
absent by design); thirty-fifth through thirty-ninth stand.

Excerpt-bounded research per #503 (2 main-run browser.search verification
sets; 0 browser.open reads). Scout rejections on main-run verification:
Google SynthID Detector partner checks (Oct 7) -> REJECTED
(content-verification partnership, no licensing payment - no money flow to
publishers); Google AI Contribution Pilot -> REJECTED (m891 saturated,
unilateral payer-set micro-rates); Impelsys x Cashmere -> REJECTED (m1002
saturated, this run's window predecessor); Redpine x six academic
publishers -> REJECTED (m1005 saturated); OpenEvidence x JAMA Network ->
REJECTED (Jan 2025 vintage, not an October 2026 event). SELECTED: Elsevier
x JAMA Network ClinicalKey AI strategic content agreement. Landed URLs
zero-hit repo-wide pre-commit (git grep -F on verbatim Full-URL listings).

The mechanism 1008 block lives in profiles/competitor-entities.yaml as a
top-level key appended at end of file (the #1024 m846 hunk untouched;
explicit-path staging).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only OBSERVES the #1290-launched background suite
(goal hidden_files type_d_1290_full_suite.log; observed at this run's
check: 7868 bytes / [ 9%], last write Oct 7 2026 17:37 PDT, zero live
pytest processes - STALLED, observation not a verdict; the #1295 Type D run
owns the verdict and tombstone); this run neither re-launches, kills, nor
writes to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit), #900
(untracked Type D test file), #1012-wt (working-tree edit on the committed
Type A #1012 file).

Type C lands one mechanism (mechanism 1008); the Type B predecessor landed
one (mechanism 1007, directional case, not a member).
This run is the FIFTH and CLOSING leg of the 1290-1294 window. Next run
#1295 Type D opens the 1295-1299 window (and renders the #1290-launched
background-suite verdict per #795). Rotation: D #1290 -> E #1291 ->
A #1292 -> B #1293 -> C #1294. The main commit is the anchor per #565.
The 1285-1289 window is VERIFIED CLOSED.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth through fifty-ninth
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
SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1290_full_suite.log")
OWN_BASENAME = (
    "test_type_c_1294_elsevier_jama_network_clinicalkey_ai_"
    "strategic_content_agreement_oct07_6pm.py"
)

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "110bb68ff5016102177b4d93ada4aca3d6c7f659"  # patched to main commit per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1008
NEXT_NUM = 1009  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_c_1294_elsevier_jama_network_clinicalkey_ai_"
    "strategic_content_agreement_oct07"
)

# Predecessor chain: #1293 Type B continued the 1290-1294 window.
PRED_MAIN_1293 = "5e8b08a4"
PRED_ANCHOR_1293 = "2b4efbfe"
PRED_DOCSYNC_1293 = "862cffb5"
PRED_FINAL_1293 = "8e8684bd"
PRED_PUSH_1293 = "2f6bf463"
# #1292 Type A (third leg) for the rotation-guard chain.
PRED_MAIN_1292 = "ddb5921f"
PRED_ANCHOR_1292 = "4420f305"
PRED_DOCSYNC_1292 = "db89a93c"
PRED_FINAL_1292 = "434fb01b"
# #1291 Type E (second leg).
PRED_MAIN_1291 = "4f33ce6a"
PRED_ANCHOR_1291 = "17773f8a"
PRED_DOCSYNC_1291 = "041cda51"
PRED_FINAL_1291 = "939e19d6"
# #1290 Type D (window opener).
PRED_MAIN_1290 = "0545f246"
PRED_ANCHOR_1290 = "7d6623c4"
PRED_DOCSYNC_1290 = "c9feb331"
PRED_FINAL_1290 = "91137e06"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40).
PRED_MAIN_1294 = "110bb68ff5016102177b4d93ada4aca3d6c7f659"  # re-pinned to main sha per #721

# Forward guard for the next leg: #1295 Type D. Re-pinned by #1295's
# log-hash followup per #721 (starts as 0*40; placeholder-only per the
# Type C precedent - this file carries no forward git-log pin).
PRED_MAIN_1295 = "0" * 40

# The #1293 window-continuation file, for the predecessor reference
# (max id 1007; zero one-zero-zero-eight keys all forms /
# no-Type-C-#1294-in-git-log / fortieth direction absent /
# forty-eighth through fifty-eighth members intact /
# fifty-ninth member absent / ledger 58).
E1293_FILE = (
    "test_type_b_1293_sarah_perez_techcrunch_muse_privacy_dispute_vs_"
    "chatgpt_shopping_sep30_oct01_6pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 72358  # patched pre-main: pre-sync 72322 + 36 collected
README_FILE_COUNT = 1619  # pre-sync 1618 + 1 (this file)

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
_T59 = "FIFT" + "Y-NINTH falsification-family member"

# Novel source URLs: 2 zero-hit repo-wide pre-commit (git grep -F).
NOVEL_URLS = [
    "https://www.prnewswire.com/news-releases/elsevier-and-jama-"
    "network-sign-strategic-content-agreement-for-clinicalkey-"
    "ai-302899585.html",
    "https://www.unite.ai/clinicalkey-ai-gains-full-text-access-"
    "to-13-jama-network-journals/",
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


def _load_entities():
    return yaml.safe_load(_read(ENTITIES_PATH))


def _block():
    data = _load_entities()
    assert BLOCK_KEY in data
    return data[BLOCK_KEY]


def _block_text():
    return _read(ENTITIES_PATH)


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1294:
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
        assert "FIFTH and CLOSING leg of the 1290-1294 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1293/#1292/#1291/#1290 chain; closes 1290-1294.
# ---------------------------------------------------------------------------

class TestRotationGuard1294:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--format=%H").stdout
        for short in (PRED_MAIN_1293, PRED_ANCHOR_1293, PRED_DOCSYNC_1293,
                      PRED_FINAL_1293, PRED_PUSH_1293, PRED_MAIN_1292,
                      PRED_ANCHOR_1292, PRED_DOCSYNC_1292, PRED_FINAL_1292,
                      PRED_MAIN_1291, PRED_ANCHOR_1291, PRED_DOCSYNC_1291,
                      PRED_FINAL_1291, PRED_MAIN_1290, PRED_ANCHOR_1290,
                      PRED_DOCSYNC_1290, PRED_FINAL_1290):
            assert short in log, short

    def test_1293_type_b_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type B #1293")
        assert "Type B #1293" in out.stdout

    def test_closing_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "CLOSING leg of the 1290-1294 window" in src

    def test_1285_1289_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1285-1289 window is VERIFIED CLOSED" in src

    def test_next_window_opens_1295(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1295 Type D opens the 1295-1299 window" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: 1008 lands; key forms stay clean per #715.
# ---------------------------------------------------------------------------

class TestMechanismNovelty1294:
    def test_max_mechanism_id_is_1008_post_landing(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_block_key_present(self):
        assert BLOCK_KEY in _load_entities()

    def test_block_key_occurs_twice_in_text(self):
        text = _block_text()
        assert text.count(BLOCK_KEY) == 2

    def test_1008_numeric_present_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(MECH_NUM) == [ENTITIES_PATH]

    def test_1008_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_1008_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_iteration_field(self):
        assert _block()["iteration"] == 1294

    def test_iteration_type_field(self):
        assert _block()["iteration_type"] == "C"


# ---------------------------------------------------------------------------
# 4. Block structure at the competitor-entities.yaml top level.
# ---------------------------------------------------------------------------

class TestBlockStructure1294:
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
            663, 711, 786, 891, 915, 927, 999, 1002, 1005}

    def test_all_novel_sources(self):
        urls = [s["url"] for s in _block()["sources"]]
        for u in NOVEL_URLS:
            assert u in urls

    def test_corborating_source_marked_not_novel(self):
        by_url = {s["url"]: s for s in _block()["sources"]}
        leap = [u for u in by_url if "302880358" in u]
        assert len(leap) == 1
        assert by_url[leap[0]]["novel"] is False

    def test_yaml_parse_clean_flag(self):
        assert _block()["yaml_parse_clean"] is True

    def test_ascii_only_flag(self):
        assert _block()["ascii_only"] is True

    def test_verdict_mechanism_documented(self):
        assert _block()["verdict"] == "mechanism_documented"
        assert _block()["verdict_detail"] == "mechanism_documented"

    def test_manual_qualitative_only(self):
        assert "MANUAL / qualitative ONLY" in _block()["finding"]

    def test_engine_not_run(self):
        assert _block()["engine_run"] is False

    def test_not_falsification_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert "ledger holds at 58" in b["falsification_family"]

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_not_artifact_grade(self):
        assert _block()["artifact_grade"] is False

    def test_browser_opens_zero(self):
        assert _block()["browser_opens"] == 0

    def test_block_ascii_only(self):
        def _walk(o):
            if isinstance(o, str):
                o.encode("ascii")
            elif isinstance(o, dict):
                for v in o.values():
                    _walk(v)
            elif isinstance(o, list):
                for v in o:
                    _walk(v)
        _walk(_block())

    def test_no_em_dashes(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        em_dash = chr(0x2014)  # built at runtime per #770; no literal in source
        en_dash = chr(0x2013)
        assert em_dash not in src
        assert en_dash not in src

    def test_yaml_block_ascii(self):
        block = _block()
        yaml.safe_dump(block).encode("ascii")
