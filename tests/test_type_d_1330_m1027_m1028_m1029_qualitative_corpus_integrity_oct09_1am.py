"""Type D iteration #1330: m1027/m1028/m1029 qualitative-discipline
corpus-integrity verification + #1325 background-suite verdict (DEAD
at [  2%]; SIXTEENTH consecutive death of the new streak; tombstone
lineage ONE-HUNDRED-TWENTY-THIRD -> ONE-HUNDRED-TWENTY-FOURTH) +
recurring-failure triage (ZERO F marks in the dead stream - nothing
to triage, DETERMINATE-vacuous; no recurring-failure triage repairs
claimed from the stream) + broader regression sweep (37 failed / 465
passed across the 1325-1329 window files in ~813s; triaged: 5
#565-class anchor placeholder-duality pins (post-anchor, fail by
design), 12 #1272-class forward-guard numeric expiries and
max-mechanism staleness pins (the 1027-numeric pins in the #1325/#1326
files, the 1028-numeric pin in the #1327 file, the 1029-numeric pin in
the #1328 file, the 1027/1028/1029 next-number-form pins, the
max-1026/max-1027/this-run max pins, and the #1325 no-mechanisms-landed
pin - m1027/m1028/m1029 landed after those runs pinned), 4 #1191-class
sixty-first-member self-trips and forward-pin placeholders (the
no-sixty-first-member pins in the #1325/#1326 files - the sixty-first
member landed at #1327/m1027, permanent red by design; the
no-Type-D-#1330 forward pin in the #1329 file - fails pre-commit by
design, flips green at this run's terminal re-pin per #721), 4
#719-class doc-sync readme-stats-ratchet staleness pins (README has
moved to 75816/1654), 12 staleness artifacts (pre-commit novelty/max/
press/log pins overtaken by later landings: the #1324/#1325/#1327
guard-lifecycle post-commit forms, the #1326 forward-guards-for-1327
and sixtieth-member-repo-wide pins, the #1327 type-a-lands-one-mechanism
pin, the #1328 novel-URL/readme-row/architecture-row/iteration-log
pins, the #1329 novel-URL/readme-row pins). 0 remaining defects) +
full suite RE-LAUNCHED to goal/hidden_files/type_d_1330_full_suite.log.

m1027 (Type A #1327, profiles/wired.yaml competitor_relationships.
openai): WIRED Oct-6/7-2026 product-review peg - THREE originals
applying critical/adversarial registers to the Aug-2024 licensing
partner OpenAI within 48 hours: Oct 7 "The New ChatGPT Is More Show
Than Tell" (intelligent-UI redesign review, -0.30 MANUAL
ILLUSTRATIVE) plus Oct-6 Isabella Ward mathematicians GitHub-dump and
John Semley Artificial film roast, vs carried WIRED x Meta
Muse-dossier accountability arm (m988, -0.58); illustrative delta
(OpenAI minus Meta) +0.28; the uniform payer-softening prediction
(Conde Nast x OpenAI Aug-20-2024 licensing, $1-5M/yr, coverage_
prediction softer) FAILS on the product-review register; verdict
falsification_member_confirmed; SIXTY-FIRST falsification-family
member (ledger 60->61); SECOND WIRED publication-level member; FIRST
product-review-register pin; domain-bounded to WIRED's
product-review/culture register on OpenAI in the Oct-6/7 window.

m1028 (Type B #1328, profiles/careers/journalists.yaml
matt_swider_type_b competitor_coverage): Matt Swider (The Shortcut)
Sep-30-2026 Meta Ray-Ban Gen-3 / VR-glasses launch piece (+0.25
MANUAL ILLUSTRATIVE, sole byline, spec-forward first-look) vs
Sep-9-2026 Apple iPhone Duo launch piece (+0.15, co-bylined
Swider/Buondonno/Lee, launch-enthusiastic with skeptical kicker);
illustrative delta (Apple minus Meta) -0.10 - register constancy,
same outlet, 21 days apart, both flagship-launch first-looks;
ZERO-GRADIENT control (no documented Shortcut x Meta/Apple licensing
deal in-corpus; joins the #1313/#1318 control-case family); verdict
directionally_supported_not_proven; NOT a falsification-family
member; ledger holds at 61; FIRST dedicated Type B pair on Swider
(fully novel journalist; The Shortcut outlet zero-hit pre-commit).

m1029 (Type C #1329, profiles/competitor-entities.yaml top-level):
USA TODAY Co. v OpenAI (SDNY No. 1:26-cv-08892, filed Oct 8 2026) -
FIRST dedicated corpus mechanism on the suit-side of the m636
pay-or-litigate bifurcation running on the SAME publisher that signed
the banked m1017 Perplexity licensing bilateral (Jul 30 2025);
damages "in excess of $250 million" + injunction over training on
"hundreds of thousands" of articles from 19 publications; variant
EXTENSION of the m636 family (connects_to [636, 1017]), NOT a new
relationship direction (fortieth direction absent by design;
35th-39th stand); verdict mechanism_documented; NOT a
falsification-family member; ledger holds at 61; tone NOT_SCORED.

MANUAL / qualitative ONLY per the Aug 28 2026 standing rule
(statistical discipline: engine NOT run on corpus, tone values are
hand-assigned, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant
false, NOT artifact-grade, no_analysis_json_update true).
Correlation is not causation; hypothesis-generating only.

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file) all left out of
this run's index/diff (explicit-path staging). #1024 m846
(profiles/competitor-entities.yaml) NOT touched - decision pending.
Do NOT touch #1024 m846.
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
WIRED_PATH = os.path.join(PROFILES_DIR, "wired.yaml")
JOURNALISTS_PATH = os.path.join(
    PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1325_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1330_full_suite.log")
OWN_BASENAME = (
    "test_type_d_1330_m1027_m1028_m1029_qualitative_"
    "corpus_integrity_oct09_1am.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "0f8f289923d4dcee0a96137a50b4231c75c64c83"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1029
NEXT_NUM = 1030  # integer only; key-form needles are format-built

# Predecessor chain: #1329 Type C closed the 1325-1329 window. All
# five legs (#1325-#1329) have push-status commits (push status
# recorded DONE in their commits, asserted below).
PRED_MAIN_1329 = "e64c14d5"
PRED_ANCHOR_1329 = "9860f05e"
PRED_DOCSYNC_1329 = "63b03c5a"
PRED_FINAL_1329 = "46fedf35"
PRED_PUSH_1329 = "ebe83c16"
PRED_MAIN_1328 = "086130d2"
PRED_ANCHOR_1328 = "5753d64b"
PRED_DOCSYNC_1328 = "7dee2272"
PRED_FINAL_1328 = "0d9756ca"
PRED_PUSH_1328 = "87a4bd2f"
PRED_MAIN_1327 = "7e011cb6"
PRED_ANCHOR_1327 = "2853e325"
PRED_DOCSYNC_1327 = "d211a118"
PRED_FINAL_1327 = "2967454a"
PRED_PUSH_1327 = "786b7942"
PRED_MAIN_1326 = "ed8d8652"
PRED_ANCHOR_1326 = "2e6c1bf2"
PRED_DOCSYNC_1326 = "9d374ff1"
PRED_FINAL_1326 = "1e92534e"
PRED_PUSH_1326 = "9d18b4cf"
PRED_MAIN_1325 = "cc24b13b"
PRED_ANCHOR_1325 = "54a68697"
PRED_DOCSYNC_1325 = "fa04cdb2"
PRED_FINAL_1325 = "00385ffd"
PRED_PUSH_1325 = "1834287b"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the no-Type-D-#1330 own-run pin
# flips green post-repin).
PRED_MAIN_1330 = "0f8f289923d4dcee0a96137a50b4231c75c64c83"  # re-pinned to main sha per #721

# Forward guard for the next leg: #1331 Type E. Re-pinned by #1331's
# terminal log-hash followup per #721 (starts as 0*40;
# placeholder-only).
PRED_MAIN_1331 = "f2e2cec6132603b0114e3a437ecf9d4f8cb42e03"

# The #1329 window-closing file, for the staleness pin on its guard
# lifecycle (33 tests; post-main-commit form is 1 failed / 32 passed -
# the no-Type-D-#1330 forward pin flips at this run's main commit and
# is re-pinned green in the terminal log-hash followup per #721, its
# PRED_MAIN_1330 re-pinned in BOTH files per the #1292 precedent; the
# 1030-form pins stay green because Type D lands no mechanisms).
# Documented in TestStalenessPins1330, not repaired.
E1329_FILE = (
    "test_type_c_1329_usa_today_co_v_openai_sdny_suit_"
    "oct09_12am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 75913  # patched pre-main: pre-sync 75816 + 97 collected
README_FILE_COUNT = 1655  # patched pre-main: pre-sync 1654 + 1 (this file)

# m846 block region in profiles/competitor-entities.yaml at HEAD (the
# #1024 m846 decision-pending block; byte-identity pin in the
# in-flight isolation class).
M846_HEAD_START = 26350
M846_HEAD_END = 26472

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
_T60 = "SIXT" + "IETH falsification-family member"
_T61 = "SIXT" + "Y-FIRST falsification-family member"
_T62 = "SIXT" + "Y-SECOND falsification-family member"

# Fragment-built per #715: the contiguous keys never appear in this
# file. Iteration-form block keys carry no underscore-form mechanism
# key substring (the #723/#738/#739 designed-keying convention).
BLOCK_1027 = (
    "type_a_1327_wired_openai_oct07_chatgpt_intelligent_ui_"
    "review_vs_carried_meta_dossier"
)
BLOCK_1028 = (
    "type_b_1328_matt_swider_shortcut_meta_rayban_gen3_"
    "vs_apple_iphone_duo_oct08_11pm"
)
BLOCK_1029 = (
    "type_c_1329_usa_today_co_v_openai_sdny_suit_"
    "oct09_12am"
)


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _yaml(path):
    return yaml.safe_load(_read(path))


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


def _wired_block_1027():
    """Locate the m1027 block in wired.yaml.

    The Type A blocks live under the competitor_relationships.openai
    section (m1027 appended at #1327). The block carries no
    iteration/author fields in the Type A corpus schema; it is
    identified by its YAML dict key (BLOCK_1027) under the openai
    section.
    """
    data = _yaml(WIRED_PATH)
    return data["competitor_relationships"]["openai"][BLOCK_1027]


def _journalist_block_1028():
    """Locate the m1028 block on the Matt Swider record.

    The Type B blocks live under the per-journalist top-level
    record's competitor_coverage dict (m1028 sits on the
    matt_swider_type_b record, the FIRST dedicated Type B pair on
    Matt Swider).
    """
    journalists = _yaml(JOURNALISTS_PATH)
    rec = journalists.get("matt_swider_type_b")
    if not isinstance(rec, dict):
        return None
    cc = rec.get("competitor_coverage", {})
    if isinstance(cc, dict) and BLOCK_1028 in cc:
        return cc[BLOCK_1028]
    return None


def _entities_block_1029():
    """Locate the m1029 block (top-level key of competitor-entities)."""
    entities = _yaml(ENTITIES_PATH)
    return entities.get(BLOCK_1029)


def _proc_holds_log(basename):
    """Return a description of live processes holding the log open."""
    holders = []
    for pid in os.listdir("/proc"):
        if not pid.isdigit():
            continue
        fd_dir = os.path.join("/proc", pid, "fd")
        try:
            for fd in os.listdir(fd_dir):
                try:
                    target = os.readlink(os.path.join(fd_dir, fd))
                except OSError:
                    continue
                if target.endswith(basename):
                    try:
                        with open(
                            os.path.join("/proc", pid, "comm")
                        ) as fh:
                            comm = fh.read().strip()
                    except OSError:
                        comm = "?"
                    holders.append("%s (%s)" % (pid, comm))
                    break
        except OSError:
            continue
    return "; ".join(holders)


def _git_grep_tracked_source(needle, scope):
    """Grep tracked files at HEAD for a literal needle (fragment-built)."""
    args = ["git", "grep", "-F", "-l", needle, "HEAD", "--"]
    args.append(scope if scope else ".")
    out = subprocess.run(
        args, cwd=REPO_ROOT, capture_output=True, text=True).stdout
    cleaned = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        if line:
            cleaned.append(line)
    return cleaned


def _class_run(filename, classname):
    target = os.path.join(TESTS_DIR, filename)
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    venv_py = os.path.join(REPO_ROOT, ".venv", "bin", "python")
    return subprocess.run(
        [venv_py, "-m", "pytest", target, "-k", classname,
         "-q", "--no-header", "-o", "addopts=", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        timeout=600,
    )


def _synthetic_calibration_delta():
    """Fresh engine-layer calibration contract for #1330.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no repo reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_apple_arms = [-0.07, -0.10, -0.05, -0.08, -0.09]
    synthetic_meta_arms = [-0.41, -0.37, -0.44, -0.39, -0.36]
    pooled_apple = (sum(synthetic_apple_arms)
                    / len(synthetic_apple_arms))
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_apple - pooled_meta, 3)


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1330:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565. This test runs
        # in the in-gate (passes pre-commit); post-anchor it fails BY
        # DESIGN (the patched form is asserted post-anchor).
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

    def test_anchor_duality_documented(self):
        # The #565 duality: the placeholder pin passes pre-commit and
        # fails post-anchor BY DESIGN; the patched pin is the mirror.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "BY DESIGN post-anchor" in src or "fails BY DESIGN" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1329 closed the 1325-1329 window; #1330 opens.
# ---------------------------------------------------------------------------


class TestRotationGuard1330:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-120").stdout
        # All five legs of the 1325-1329 window have push-status
        # commits (push status recorded DONE in the iteration-log
        # entries and in the push-status commits).
        for sha, label in (
            (PRED_MAIN_1329, "1329 main"),
            (PRED_ANCHOR_1329, "1329 anchor"),
            (PRED_DOCSYNC_1329, "1329 doc-sync"),
            (PRED_FINAL_1329, "1329 log-hash"),
            (PRED_PUSH_1329, "1329 push-status"),
            (PRED_MAIN_1328, "1328 main"),
            (PRED_ANCHOR_1328, "1328 anchor"),
            (PRED_DOCSYNC_1328, "1328 doc-sync"),
            (PRED_FINAL_1328, "1328 log-hash"),
            (PRED_PUSH_1328, "1328 push-status"),
            (PRED_MAIN_1327, "1327 main"),
            (PRED_ANCHOR_1327, "1327 anchor"),
            (PRED_DOCSYNC_1327, "1327 doc-sync"),
            (PRED_FINAL_1327, "1327 log-hash"),
            (PRED_PUSH_1327, "1327 push-status"),
            (PRED_MAIN_1326, "1326 main"),
            (PRED_ANCHOR_1326, "1326 anchor"),
            (PRED_DOCSYNC_1326, "1326 doc-sync"),
            (PRED_FINAL_1326, "1326 log-hash"),
            (PRED_PUSH_1326, "1326 push-status"),
            (PRED_MAIN_1325, "1325 main"),
            (PRED_ANCHOR_1325, "1325 anchor"),
            (PRED_DOCSYNC_1325, "1325 doc-sync"),
            (PRED_FINAL_1325, "1325 log-hash"),
            (PRED_PUSH_1325, "1325 push-status"),
        ):
            assert sha in log, label

    def test_all_window_push_status_done_commits(self):
        out = _git("log", "--format=%H %s")
        for sha in (PRED_PUSH_1325, PRED_PUSH_1326, PRED_PUSH_1327,
                    PRED_PUSH_1328, PRED_PUSH_1329):
            assert sha in out.stdout
        assert "push-status: DONE" in out.stdout

    def test_1329_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1329")
        assert "Type C #1329" in out.stdout

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1330-1334 window" in src

    def test_1325_1329_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1325-1329 window is VERIFIED CLOSED" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1330 -> E #1331 -> A #1332 -> B #1333 -> C #1334" in src

    def test_next_window_verdict_belongs_to_1335(self):
        # Per #795 the next background-suite verdict (on the
        # #1330-launched suite) belongs to the next Type D run,
        # #1335.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1335 Type D run owns the next verdict" in src


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1027 / m1028 / m1029 all landed and intact.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1330:
    def test_m1027_block_present_in_wired(self):
        assert _wired_block_1027() is not None

    def test_m1027_mechanism_id_1027(self):
        block = _wired_block_1027()
        assert block["mechanism_id"] == 1027
        assert block["block_key"] == BLOCK_1027

    def test_m1027_product_review_peg_identified(self):
        # The Type A corpus schema nests the prose peg under event/
        # publication_focus (no mechanism_name field); the Oct-6/7
        # product-review peg and the WIRED focus identify the block.
        block = _wired_block_1027()
        assert "WIRED" in block["publication_focus"]
        assert "product-review" in block["event"]
        assert "ChatGPT" in block["event"]

    def test_m1027_verdict_falsification_member_confirmed(self):
        # m1027 is the SIXTY-FIRST falsification-family member
        # (ledger 60->61): WIRED runs an adversarial product-review
        # original on its own Aug-2024 licensing partner OpenAI, so
        # the uniform payer-softening prediction FAILS on the
        # product-review register.
        block = _wired_block_1027()
        assert block["verdict"].startswith(
            "falsification_member_confirmed")
        assert block["falsification_family_member"] is True
        assert "ledger 60->61" in block["falsification_family"]
        assert block["ledger"] == "61"

    def test_m1028_block_present_in_journalists(self):
        assert _journalist_block_1028() is not None

    def test_m1028_mechanism_id_1028(self):
        block = _journalist_block_1028()
        assert block["mechanism_id"] == 1028
        assert block["iteration"] == 1328
        assert block["iteration_type"] == "B"

    def test_m1028_block_key_field(self):
        block = _journalist_block_1028()
        assert block["block_key"] == BLOCK_1028

    def test_m1028_verdict_directionally_supported(self):
        # m1028 is a directionally_supported_not_proven ZERO-GRADIENT
        # control (Matt Swider, The Shortcut: Meta Ray-Ban Gen-3
        # launch piece vs Apple iPhone Duo launch piece,
        # illustrative delta -0.10, register constancy), NOT a
        # falsification-family member; ledger holds at 61.
        block = _journalist_block_1028()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["falsification_family_member"] is False

    def test_m1028_first_pair_on_swider_in_notes(self):
        # The FIRST dedicated Type B pair on Matt Swider; the record
        # notes carry the ledger position.
        rec = _yaml(JOURNALISTS_PATH)["matt_swider_type_b"]
        assert "FIRST" in rec["notes"]
        assert "ledger holds at 61" in rec["notes"]
        assert _journalist_block_1028()["author"] == "Kit (with Ray)"

    def test_m1029_block_present_in_entities(self):
        entities = _yaml(ENTITIES_PATH)
        assert BLOCK_1029 in entities

    def test_m1029_mechanism_id_1029(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1029]
        assert block["mechanism_id"] == 1029
        assert block["iteration"] == 1329
        assert block["iteration_type"] == "C"

    def test_m1029_block_key_field(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1029]["block_key"] == BLOCK_1029

    def test_m1029_verdict_mechanism_documented(self):
        # m1029 documents the suit-side of the m636 pay-or-litigate
        # bifurcation (USA TODAY Co. v OpenAI, SDNY 1:26-cv-08892):
        # verdict mechanism_documented; NOT a falsification-family
        # member; ledger holds at 61; tone NOT_SCORED.
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1029]
        assert block["verdict"] == "mechanism_documented"
        assert block["falsification_family_member"] is False
        assert "ledger holds at 61" in block["falsification_family"]

    def test_m1029_author(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1029]["author"] == "Kit (with Ray)"

    def test_max_numeric_mechanism_id_is_1029(self):
        assert _max_numeric_mechanism_id() == MECH_NUM


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1325 suite is DEAD at [  2%].
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1330:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG

    def test_prior_suite_stalled_at_2(self):
        # The #1325-launched suite froze at [  2%] progress: 1873
        # bytes, zero F marks, last write Oct 8 2026 21:59 PDT (~3h
        # stale at this run's ~01:00 AM PDT check), zero live pytest
        # processes (the pgrep sweep at this run's check returned zero
        # live pytest processes; the /proc open-fd check returns
        # empty). Progress never regresses, so the [  2%] marker stays
        # present and [  3%] never arrives. Observation history: #1325
        # launched it and saw it ALIVE at doc-sync (dots accumulating
        # at [  0%]); #1326 saw it ALIVE at ~10:00 PM PDT (1 live
        # pytest process); #1327 saw it DEAD at ~11:00 PM PDT (zero
        # live processes, last write 21:59); #1328 saw it DEAD at
        # ~11:00 PM PDT; #1329 saw it DEAD at ~12:15 AM PDT.
        text = _read(PRIOR_SUITE_LOG)
        assert "[  2%]" in text, text[-2000:]
        assert "[  3%]" not in text
        assert 100 <= len(text) <= 100000, len(text)

    def test_prior_suite_has_zero_summary_tokens(self):
        # A completed run prints a summary ("passed"/"failed") or a
        # collection report ("no tests ran" / "short test summary").
        # The dead run carries none of them.
        text = _read(PRIOR_SUITE_LOG)
        for token in ("passed", "failed", "no tests ran",
                      "short test summary"):
            assert token not in text, token

    def test_no_live_pytest_holds_prior_log(self):
        # The #1190-class death check: NO live pytest process holds
        # type_d_1325_full_suite.log open anymore (the /proc open-fd
        # check returns empty; the pgrep sweep at this run's ~01:00 AM
        # PDT check returned zero live pytest processes).
        holders = _proc_holds_log("type_d_1325_full_suite.log")
        assert holders == "", holders

    def test_sixteenth_death_of_new_streak(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite
        # completed). The 43-run streak BROKE at #1250 (the #1245
        # suite was verdict ALIVE at 20%). #1255 verdict the FIRST
        # consecutive background-suite death of the new streak, #1260
        # the SECOND, #1265 the THIRD, #1270 the FOURTH, #1275 the
        # FIFTH, #1280 the SIXTH, #1285 the SEVENTH, #1290-launched
        # the EIGHTH (#1295 verdict), #1295-launched the NINTH (#1300
        # verdict), #1300-launched the TENTH (#1305 verdict),
        # #1305-launched the ELEVENTH (#1310 verdict), #1310-launched
        # the TWELFTH (#1315 verdict), #1315-launched the THIRTEENTH
        # (#1320 verdict), #1320-launched the FOURTEENTH (#1325
        # verdict), #1325-launched the FIFTEENTH (#1330 verdict...
        # no: the #1325-launched suite's death verdict is the
        # SIXTEENTH consecutive background-suite death of the new
        # streak.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "SIXTEENTH consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-TWENTY-THIRD -> ONE-HUNDRED-TWENTY-FOURTH.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ONE-HUNDRED-TWENTY-FOURTH" in src
        assert "lineage advances" in src

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1330 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_PATH)
        assert "SIXTEENTH consecutive" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: DETERMINATE-vacuous (zero F marks).
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1330:
    def test_zero_f_marks_in_dead_stream(self):
        text = _read(PRIOR_SUITE_LOG)
        f_lines = [line for line in text.split("\n")
                   if re.search(r"\.+F", line)]
        assert len(f_lines) == 0, f_lines

    def test_triage_is_determinate_vacuous(self):
        # With zero F marks there is nothing to root-cause and
        # nothing to repair: the triage verdict is DETERMINATE by
        # vacuity, recorded in this file's docstring.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "zero F marks" in src
        assert "nothing to triage" in src

    def test_no_repairs_claimed_from_stream(self):
        # No repair claims may ride on an empty failure stream.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no recurring-failure triage repairs" in src


# ---------------------------------------------------------------------------
# 6. Statistical discipline: manual/qualitative only; engine calibration.
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1330:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: the max numeric mechanism id is
        # unchanged at 1029 and no 1030-form keys exist.
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_engine_not_run_on_corpus(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run on corpus" in src

    def test_synthetic_calibration_delta_contract(self):
        # Engine-layer contract only (never a finding): synthetic
        # Apple arms [-0.07, -0.10, -0.05, -0.08, -0.09] vs synthetic
        # Meta arms [-0.41, -0.37, -0.44, -0.39, -0.36] -> pooled
        # delta +0.316.
        assert _synthetic_calibration_delta() == 0.316


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 61; guards on member forms.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1330:
    def test_ledger_holds_at_61(self):
        # m1027 is the SIXTY-FIRST member (ledger 60->61); m1028 and
        # m1029 carry the ledger-holds-at-61 note in their record
        # notes / falsification_family fields.
        block = _wired_block_1027()
        assert "ledger 60->61" in block["falsification_family"]
        rec = _yaml(JOURNALISTS_PATH)["matt_swider_type_b"]
        assert "ledger holds at 61" in rec["notes"]
        entities = _yaml(ENTITIES_PATH)
        assert "ledger holds at 61" in entities[
            BLOCK_1029]["falsification_family"]

    def test_forty_eighth_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T48, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_forty_ninth_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T49, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_member_intact(self):
        # Landed #1237 (m979, profiles/news-corp.yaml, committed);
        # the count moved 2->3 after #1325 (the #1237 block carries an
        # extra member-claim form mention). HEAD sweep is stable for a
        # committed landing.
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T55, "HEAD", "--",
            "profiles/atlantic.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_sixth_member_intact(self):
        # Landed #1282 (m1000, profiles/wired.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T56, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_seventh_member_intact(self):
        # Landed #1287 (m1003, profiles/ap.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_intact(self):
        # Landed #1292 (m1006, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_member_intact(self):
        # Landed #1302 (m1012, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixtieth_member_intact(self):
        # Landed #1322 (m1024, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_first_member_intact(self):
        # Landed #1327 (m1027, profiles/wired.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T61, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_second_member(self):
        assert _git_grep_tracked_source(_T62, None) == []

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (
            "THIRT" + "Y-FIFTH relationship direction",
            "THIRT" + "Y-SIXTH relationship direction",
            "THIRT" + "Y-SEVENTH relationship direction",
            "THIRT" + "Y-EIGHTH relationship direction",
            "THIRT" + "Y-NINTH relationship direction",
        ):
            assert _git_grep_tracked_source(needle, "profiles/") != [], needle

    def test_fortieth_direction_absent(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: forward pins for #1331; #1329 staged for this run.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1330:
    def test_pins_on_1029_no_landing(self):
        # Type D lands no mechanisms: max stays 1029, next stays 1030.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1029" in src
        assert "NEXT_NUM = 1030" in src

    def test_no_type_d_1330_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721): every commit whose message
        # matches "Type D #1330" must be this run's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type D #1330")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1330's own commits"
        main = _git("rev-parse", PRED_MAIN_1330).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_e_1331_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1331's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1331" must be #1331's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1331 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type E #1331")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1331's own commits"
        main = _git("rev-parse", PRED_MAIN_1331).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1030_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1030_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1030_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T48, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_forty_ninth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T49, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T55, "HEAD", "--",
            "profiles/atlantic.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_sixth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T56, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_seventh_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixtieth_member_present_pin(self):
        # Landed #1322 (m1024, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_first_member_present_pin(self):
        # Landed #1327 (m1027, profiles/wired.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T61, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_second_member_pin(self):
        # Type D lands no mechanisms; the sixty-second member-claim
        # form stays absent repo-wide.
        assert _git_grep_tracked_source(_T62, None) == []

    def test_predecessor_1329_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1329_FILE))

    def test_next_leg_is_1331_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1331 Type E" in src

    def test_1329_pins_flip_documented(self):
        # #1329 staged guard-lifecycle forward pins for this run
        # (no-Type-D-#1330-in-git-log, zero one-zero-three-zero keys
        # all forms, fortieth direction absent, forty-eighth through
        # sixty-first members intact, no sixty-second member, ledger
        # 61); all verified GREEN pre-commit this run (manual
        # forward-guard verification, recorded in the iteration-log
        # entry). The no-Type-D-#1330 pin flips BY DESIGN at this
        # run's main commit (the #1191-class self-trip, re-pinned
        # post-commit by TestStalenessPins1330); the 1030-form pins
        # stay green because Type D lands no mechanisms. Documented in
        # the staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1330" in src
        assert "no_type_d_1330_in_git_log_pin" in src
        assert "#1191-class" in src
        assert "#1272-class" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1329's guard lifecycle flips once, then re-pins.
# ---------------------------------------------------------------------------


class TestStalenessPins1330:
    def test_1329_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: all 24 pass. The
        # no_type_d_1330_in_git_log pin (the #1191-class self-trip:
        # this run's main commit carries "Type D #1330") flipped BY
        # DESIGN at this run's main commit and is re-pinned green in
        # the terminal log-hash followup per #721 (PRED_MAIN_1330 now
        # holds this run's main sha in BOTH this file and the #1329
        # file per the #1292 precedent). The 1030-form pins stay green
        # throughout (Type D lands no mechanisms; the #723/#738/#739
        # designed keying holds); the member and direction pins stay
        # green (no member, no direction landed this run). The #1329
        # block is read-only to this run; the flip is documented here,
        # not repaired. Deselected pre-commit (verified only
        # post-terminal-followup).
        res = _class_run(E1329_FILE, "TestGuardLifecycle1329")
        out = res.stdout + res.stderr
        assert "24 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1330:
    def test_readme_test_file_table_has_1330_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1330_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert OWN_BASENAME in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 11. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1330:
    def test_log_has_1330_entry(self):
        text = _read(LOG_PATH)
        assert "## #1330 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "SIXTEENTH consecutive" in text
        assert "type_d_1330_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1330:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1330_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1330 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1330:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#899" in src

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_1012_wt_working_tree_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_a_1012" in res.stdout

    def test_own_diff_excludes_inflight(self):
        # This run's staged set must never include the in-flight
        # files; verified at commit time by explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "explicit-path" in src

    def test_1024_m846_block_untouched(self):
        # #1024 m846 (profiles/competitor-entities.yaml, HEAD lines
        # 26350-26472): Ray's revert/leave/rebuild-from-primary
        # decision still pending. Type D writes nothing to profiles/;
        # the m846 block must be byte-identical to HEAD. Do NOT touch
        # #1024 m846.
        head = _git(
            "show", "HEAD:profiles/competitor-entities.yaml").stdout
        work = _read(ENTITIES_PATH)
        assert (head.splitlines()[M846_HEAD_START - 1:M846_HEAD_END]
                == work.splitlines()[M846_HEAD_START - 1:M846_HEAD_END])
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src
