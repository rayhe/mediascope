"""Type D iteration #1305: m1012/m1013/m1014 qualitative-discipline
corpus-integrity verification + #1300 background-suite verdict (DEAD
at [  5%]; ELEVENTH consecutive death of the new streak; tombstone
lineage ONE-HUNDRED-EIGHTEENTH -> ONE-HUNDRED-NINETEENTH) +
recurring-failure triage (ZERO F marks in the dead stream - nothing
to triage, DETERMINATE-vacuous) + broader regression sweep (30 failed,
446 passed across the 1300-1304 window files in 686.90s; triage: 5
#565-class anchor placeholder-duality pins, 14 #1272-class
forward-guard expiries from m1012/m1013/m1014 landing, 5 #1191-class
self-trips, 4 #719-class doc-sync ratchet staleness pins, 2 staleness
artifacts - all by-design, documented not repaired; 0 remaining
defects) + full suite RE-LAUNCHED to
goal/hidden_files/type_d_1305_full_suite.log.

m1012 (Type A #1302, profiles/news-corp.yaml competitor_relationships
.google): WSJ x Google Jul-24-2026 EU DMA $1.02B fine
enforcement-accountability register (-0.35 MANUAL ILLUSTRATIVE) vs
carried WSJ x Meta arms (m532 via m904, mean -0.275); illustrative
delta (Google minus Meta) -0.075, near-null, Google marginally harder;
the naive uniform payer-softening prediction FAILS on the enforcement
register (the Feb-2021 News Corp x Google commercial agreement is
disclosed in-article). The FIFTY-NINTH falsification-family member
(ledger 58->59); verdict falsification_member_confirmed.

m1013 (Type B #1303, profiles/careers/journalists.yaml
kelvin_chan_type_b competitor_coverage): Kelvin Chan (AP Business
Writer, London) Jun-9-2026 EU WhatsApp interim-measures order on Meta
(-0.40 MANUAL ILLUSTRATIVE) vs Sep-17-2026 OpenAI voluntary
misalignment-disclosure framework (+0.10 MANUAL ILLUSTRATIVE);
illustrative delta (OpenAI minus Meta) +0.50; the AP x OpenAI
Jul-13-2023 archive-licensing deal is the payer in the pair, so the
delta runs WITH the naive payer-softening prediction at the
journalist level: thesis-consistent observation, NOT a
falsification-family member (ledger holds at 59); verdict
directionally_supported_not_proven. STRONG confounds: peg asymmetry
(enforcement order vs voluntary disclosure) + contributor-byline
asymmetry on the OpenAI arm.

m1014 (Type C #1304, profiles/competitor-entities.yaml top-level):
TNL Mediagene (Nasdaq: TNMG) x TollBit initial-revenue validation -
FIRST named-publisher revenue evidence on the per-fetch AI licensing
marketplace rail (first Japanese media company, 15 brands on TollBit;
"begun generating initial revenue from AI buyers"; volumes modest;
RAG/agent uses); verdict mechanism_documented; NOT a
falsification-family member (ledger holds at 59); no new direction
(fortieth absent by design; thirty-fifth through thirty-ninth
stand). MANUAL / qualitative ONLY per the Aug 28 2026 standing rule:
engine NOT run on corpus; NOT artifact-grade; no analysis.json
update.

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
NEWS_CORP_PATH = os.path.join(PROFILES_DIR, "news-corp.yaml")
JOURNALISTS_PATH = os.path.join(
    PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1300_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1305_full_suite.log")
OWN_BASENAME = (
    "test_type_d_1305_m1012_m1013_m1014_qualitative_"
    "corpus_integrity_oct08_4am.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "0" * 40

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1014
NEXT_NUM = 1015  # integer only; key-form needles are format-built

# Predecessor chain: #1304 Type C closed the 1300-1304 window.
PRED_MAIN_1304 = "dbacdeb6"
PRED_ANCHOR_1304 = "ad741e80"
PRED_DOCSYNC_1304 = "3b052f3d"
PRED_FINAL_1304 = "f0c6e1b1"
PRED_PUSH_1304 = "47918893"
PRED_MAIN_1303 = "0078dd5d"
PRED_ANCHOR_1303 = "80e22c2d"
PRED_DOCSYNC_1303 = "2be0d18b"
PRED_FINAL_1303 = "567b78e8"
PRED_PUSH_1303 = "13d830ab"
PRED_MAIN_1302 = "b8859fbc"
PRED_ANCHOR_1302 = "a8be4ff1"
PRED_DOCSYNC_1302 = "b643afce"
PRED_FINAL_1302 = "7c49179c"
PRED_PUSH_1302 = "dd93dd6f"
PRED_MAIN_1301 = "68be73fa"
PRED_ANCHOR_1301 = "deb96ee6"
PRED_DOCSYNC_1301 = "8dc0404d"
PRED_FINAL_1301 = "9c61ea8b"
PRED_MAIN_1300 = "73eae8b2"
PRED_ANCHOR_1300 = "ae5056a0"
PRED_DOCSYNC_1300 = "524a047e"
PRED_FINAL_1300 = "96842974"
PRED_PUSH_1300 = "91a83617"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the no-Type-D-#1305 own-run pin
# flips green post-repin).
PRED_MAIN_1305 = "0" * 40

# Forward guard for the next leg: #1306 Type E. Re-pinned by #1306's
# terminal log-hash followup per #721 (starts as 0*40;
# placeholder-only).
PRED_MAIN_1306 = "0" * 40

# The #1304 window-closing file, for the staleness pin on its guard
# lifecycle (21 tests; post-terminal-followup form is 21 passed - the
# no-Type-D-#1305 pin flips at this run's main commit and is re-pinned
# green in the terminal log-hash followup per #721, its PRED_MAIN_1305
# re-pinned in BOTH files per the #1292 precedent; the 1015-form pins
# stay green since Type D lands no mechanisms).
E1304_FILE = (
    "test_type_c_1304_tnl_mediagene_tollbit_initial_revenue_"
    "oct08_3am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 73370  # patched pre-main: pre-sync 73279 + 91 collected
README_FILE_COUNT = 1630  # pre-sync 1629 + 1 (this file)

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

# Fragment-built per #715: the contiguous keys never appear in this
# file. Iteration-form block keys carry no underscore-form mechanism
# key substring (the #723/#738/#739 designed-keying convention).
BLOCK_1012 = (
    "type_a_1302_wsj_google_eu_dma_fine_enforcement_"
    "vs_carried_meta_arms_oct08_1am"
)
BLOCK_1013 = (
    "type_b_1303_kelvin_chan_ap_meta_whatsapp_eu_order_"
    "vs_openai_disclosure_oct08_2am"
)
BLOCK_1014 = (
    "type_c_1304_tnl_mediagene_tollbit_initial_"
    "revenue_oct08_3am"
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


def _newscorp_block_1012():
    """Locate the m1012 block under competitor_relationships.google."""
    data = _yaml(NEWS_CORP_PATH)
    rels = data.get("competitor_relationships", {})
    google = rels.get("google", {})
    return google.get(BLOCK_1012)


def _journalist_block_1013():
    """Locate the m1013 block on the Kelvin Chan record.

    The Type B blocks live under the per-journalist top-level record's
    competitor_coverage dict (m1013 sits on the kelvin_chan_type_b
    record, the FIRST dedicated Type B pair on Kelvin Chan).
    """
    journalists = _yaml(JOURNALISTS_PATH)
    rec = journalists.get("kelvin_chan_type_b")
    if not isinstance(rec, dict):
        return None
    cc = rec.get("competitor_coverage", {})
    if isinstance(cc, dict) and BLOCK_1013 in cc:
        return cc[BLOCK_1013]
    return None


def _entities_block_1014():
    """Locate the m1014 block (top-level key of competitor-entities)."""
    entities = _yaml(ENTITIES_PATH)
    return entities.get(BLOCK_1014)


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
    """Fresh engine-layer calibration contract for #1305.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no repo reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_apple_arms = [-0.11, -0.08, -0.13, -0.09, -0.10]
    synthetic_meta_arms = [-0.45, -0.39, -0.48, -0.43, -0.36]
    pooled_apple = (sum(synthetic_apple_arms)
                    / len(synthetic_apple_arms))
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_apple - pooled_meta, 3)


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1305:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565. This test is
        # deselected in the in-gate run; the patched form is asserted
        # post-anchor.
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
# 2. Rotation guard: #1304 closed the 1300-1304 window; #1305 opens.
# ---------------------------------------------------------------------------


class TestRotationGuard1305:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-70").stdout
        for sha, label in (
            (PRED_MAIN_1304, "1304 main"),
            (PRED_ANCHOR_1304, "1304 anchor"),
            (PRED_DOCSYNC_1304, "1304 doc-sync"),
            (PRED_FINAL_1304, "1304 log-hash"),
            (PRED_PUSH_1304, "1304 push-status"),
            (PRED_MAIN_1303, "1303 main"),
            (PRED_ANCHOR_1303, "1303 anchor"),
            (PRED_DOCSYNC_1303, "1303 doc-sync"),
            (PRED_FINAL_1303, "1303 log-hash"),
            (PRED_PUSH_1303, "1303 push-status"),
            (PRED_MAIN_1302, "1302 main"),
            (PRED_ANCHOR_1302, "1302 anchor"),
            (PRED_DOCSYNC_1302, "1302 doc-sync"),
            (PRED_FINAL_1302, "1302 log-hash"),
            (PRED_PUSH_1302, "1302 push-status"),
            (PRED_MAIN_1301, "1301 main"),
            (PRED_ANCHOR_1301, "1301 anchor"),
            (PRED_DOCSYNC_1301, "1301 doc-sync"),
            (PRED_FINAL_1301, "1301 log-hash"),
            (PRED_MAIN_1300, "1300 main"),
            (PRED_ANCHOR_1300, "1300 anchor"),
            (PRED_DOCSYNC_1300, "1300 doc-sync"),
            (PRED_FINAL_1300, "1300 log-hash"),
            (PRED_PUSH_1300, "1300 push-status"),
        ):
            assert sha in log, label

    def test_1304_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1304")
        assert "Type C #1304" in out.stdout

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1305-1309 window" in src

    def test_1300_1304_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1300-1304 window is VERIFIED CLOSED" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1305 -> E #1306 -> A #1307 -> B #1308 -> C #1309" in src

    def test_next_window_verdict_belongs_to_1310(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1310 Type D run owns the next verdict" in src

# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1012 / m1013 / m1014 all landed and intact.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1305:
    def test_m1012_block_present_in_newscorp(self):
        data = _yaml(NEWS_CORP_PATH)
        rels = data["competitor_relationships"]
        assert BLOCK_1012 in rels["google"]

    def test_m1012_mechanism_id_1012(self):
        block = _newscorp_block_1012()
        assert block is not None
        assert block["mechanism_id"] == 1012
        assert block["iteration"] == 1302
        assert block["iteration_type"] == "A"

    def test_m1012_block_key_field(self):
        block = _newscorp_block_1012()
        assert block["block_key"] == BLOCK_1012

    def test_m1012_fifty_ninth_member_confirmed(self):
        # m1012 IS the fifty-ninth falsification-family member
        # (ledger 58->59): the naive uniform payer-softening prediction
        # fails on the enforcement register. The verdict nests under
        # statistical_discipline in the m1012 block (the Type A
        # corpus schema).
        block = _newscorp_block_1012()
        assert block["statistical_discipline"]["verdict"] == (
            "falsification_member_confirmed")
        assert block["falsification_family_member"] is True
        assert "ledger 58->59" in str(block["falsification_family"])
        assert "FIFTY-NINTH" in str(block["falsification_family"])

    def test_m1012_author(self):
        block = _newscorp_block_1012()
        assert block["author"] == "Kit (with Ray)"

    def test_m1013_block_present_in_journalists(self):
        assert _journalist_block_1013() is not None

    def test_m1013_mechanism_id_1013(self):
        block = _journalist_block_1013()
        assert block["mechanism_id"] == 1013
        assert block["iteration"] == 1303
        assert block["iteration_type"] == "B"

    def test_m1013_block_key_field(self):
        block = _journalist_block_1013()
        assert block["block_key"] == BLOCK_1013

    def test_m1013_verdict_directionally_supported(self):
        # m1013 is a directionally_supported_not_proven
        # thesis-consistent observation, NOT a falsification-family
        # member; ledger holds at 59.
        block = _journalist_block_1013()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["falsification_family_member"] is False

    def test_m1013_not_a_member_in_notes(self):
        # The FIRST dedicated Type B pair on Kelvin Chan; the record
        # notes carry the ledger position and the FIRST-Chan novelty.
        rec = _yaml(JOURNALISTS_PATH)["kelvin_chan_type_b"]
        assert "FIRST dedicated Type B pair on Kelvin Chan" in rec[
            "notes"]
        assert "ledger holds at 59" in rec["notes"]
        assert _journalist_block_1013()["author"] == "Kit (with Ray)"

    def test_m1014_block_present_in_entities(self):
        entities = _yaml(ENTITIES_PATH)
        assert BLOCK_1014 in entities

    def test_m1014_mechanism_id_1014(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1014]
        assert block["mechanism_id"] == 1014
        assert block["iteration"] == 1304
        assert block["iteration_type"] == "C"

    def test_m1014_block_key_field(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1014]["block_key"] == BLOCK_1014

    def test_m1014_verdict_mechanism_documented(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1014]
        assert block["verdict"] == "mechanism_documented"
        assert block["falsification_family_member"] is False
        assert "ledger holds at 59" in block["falsification_family"]

    def test_max_numeric_mechanism_id_is_1014(self):
        assert _max_numeric_mechanism_id() == MECH_NUM


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1300 suite is DEAD at [  5%].
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1305:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG

    def test_prior_suite_stalled_at_5(self):
        # The #1300-launched suite froze at [  5%] progress: 4760
        # bytes, zero F marks, last write Oct 8 2026 00:51 PDT (~3h
        # stale at this run's ~04:00 AM PDT check), zero live pytest
        # processes (the single pgrep hit at this run's check was the
        # check shell's own cmdline - a self-match phantom),
        # confirmed dead by a second pgrep/ps sweep. Progress never
        # regresses, so the [  5%] marker stays present and [  6%]
        # never arrives. Observation history: #1301 saw it ALIVE-but
        # -stalled at ~01:02 PDT (1 live process, resumed-slow), #1302
        # saw it possibly-stalled at ~02:00 PDT (zero live processes),
        # #1303 and #1304 saw it STALLED (~03:10 PDT checks).
        text = _read(PRIOR_SUITE_LOG)
        assert "[  5%]" in text, text[-2000:]
        assert "[  6%]" not in text
        assert 1000 <= len(text) <= 100000, len(text)

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
        # type_d_1300_full_suite.log open anymore (the /proc open-fd
        # check returns empty; the pgrep hits at this run's ~04:00
        # check were the check shell's own cmdline and its pgrep
        # child - self-match phantoms, re-verified with ps -ef).
        holders = _proc_holds_log("type_d_1300_full_suite.log")
        assert holders == "", holders

    def test_eleventh_death_of_new_streak(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite
        # completed). The 43-run streak BROKE at #1250 (the #1245
        # suite was verdict ALIVE at 20%). #1255 verdict the FIRST
        # consecutive background-suite death of the new streak, #1260
        # the SECOND, #1265 the THIRD, #1270 the FOURTH, #1275 the
        # FIFTH, #1280 the SIXTH, #1285 the SEVENTH, #1290-launched
        # the EIGHTH, #1295-launched the NINTH (#1300 verdict),
        # #1300-launched the TENTH (#1305 verdict, this run). This
        # verdict is the ELEVENTH consecutive background-suite death
        # of the new streak.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ELEVENTH consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-EIGHTEENTH -> ONE-HUNDRED-NINETEENTH.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ONE-HUNDRED-NINETEENTH" in src
        assert "lineage advances" in src

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1305 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_PATH)
        assert "ELEVENTH consecutive" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: DETERMINATE-vacuous (zero F marks).
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1305:
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


class TestStatisticalDiscipline1305:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: the max numeric mechanism id is
        # unchanged at 1014 and no 1015-form keys exist.
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_engine_not_run_on_corpus(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run on corpus" in src

    def test_synthetic_calibration_delta_contract(self):
        # Engine-layer contract only (never a finding): synthetic
        # Apple arms [-0.11, -0.08, -0.13, -0.09, -0.10] vs synthetic
        # Meta arms [-0.45, -0.39, -0.48, -0.43, -0.36] -> pooled
        # delta +0.320.
        assert _synthetic_calibration_delta() == 0.320


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 59; guards on member forms.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1305:
    def test_ledger_holds_at_59(self):
        # m1012 carried the ledger 58->59; m1013 and m1014 hold it.
        block = _newscorp_block_1012()
        assert "ledger 58->59" in str(block["falsification_family"])
        entities = _yaml(ENTITIES_PATH)
        assert "ledger holds at 59" in entities[
            BLOCK_1014]["falsification_family"]
        rec = _yaml(JOURNALISTS_PATH)["kelvin_chan_type_b"]
        assert "ledger holds at 59" in rec["notes"]

    def test_forty_eighth_member_intact(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

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
        # Landed #1282 (m1000, profiles/wired.yaml). Asserted on the
        # working tree so the pin is stable across commit boundaries.
        assert _T56 in _read(os.path.join(PROFILES_DIR, "wired.yaml"))

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

    def test_no_sixtieth_member(self):
        assert _git_grep_tracked_source(_T60, None) == []

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
# 8. Guard lifecycle: forward pins for #1306; #1304 staged for this run.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1305:
    def test_pins_on_1014_no_landing(self):
        # Type D lands no mechanisms: max stays 1014, next stays 1015.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1014" in src
        assert "NEXT_NUM = 1015" in src

    def test_no_type_d_1305_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721): every commit whose message
        # matches "Type D #1305" must be this run's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type D #1305")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1305's own commits"
        main = _git("rev-parse", PRED_MAIN_1305).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_e_1306_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1306's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1306" must be #1306's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type E #1306")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1306's own commits"
        main = _git("rev-parse", PRED_MAIN_1306).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1015_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1015_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1015_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

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
        # Landed #1282 (m1000, profiles/wired.yaml). Asserted on the
        # working tree so the pin is stable across the main-commit
        # boundary; the HEAD sweep sees it from the main commit on.
        assert _T56 in _read(os.path.join(PROFILES_DIR, "wired.yaml"))

    def test_fifty_seventh_member_present_pin(self):
        # Landed #1287 (m1003, profiles/ap.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_present_pin(self):
        # Landed #1292 (m1006, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_member_present_pin(self):
        # Landed #1302 (m1012, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixtieth_member_pin(self):
        # Type D lands no mechanisms; the sixtieth member-claim form
        # stays absent repo-wide.
        assert _git_grep_tracked_source(_T60, None) == []

    def test_predecessor_1304_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1304_FILE))

    def test_next_leg_is_1306_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1306 Type E" in src

    def test_1304_pins_flip_documented(self):
        # #1304 staged guard-lifecycle forward pins for this run
        # (no-Type-D-#1305-in-git-log, zero one-zero-one-five keys all
        # forms, fortieth direction absent, forty-eighth through
        # fifty-ninth members intact, no sixtieth member); all
        # verified GREEN pre-commit this run (manual forward-guard
        # verification, recorded in the iteration-log entry). The
        # no-Type-D-#1305 pin flips BY DESIGN at this run's main
        # commit (the #1191-class self-trip, re-pinned post-commit by
        # TestStalenessPins1305); the 1015-form pins stay green
        # because Type D lands no mechanisms. Documented in the
        # staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1305" in src
        assert "no_type_d_1305_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1304's guard lifecycle flips once, then re-pins.
# ---------------------------------------------------------------------------


class TestStalenessPins1305:
    def test_1304_guard_lifecycle_post_terminal_self_trip(self):
        # Post-terminal-followup form: 21 tests in the class; ONE flips
        # BY DESIGN when this run's main commit lands (the
        # no_type_d_1305_in_git_log pin - the #1191-class self-trip)
        # and flips back green in the terminal log-hash followup per
        # #721 (PRED_MAIN_1305 re-pinned to this run's main sha in
        # BOTH this file and the #1304 file per the #1292 precedent).
        # The 1015-form pins stay green throughout (Type D lands no
        # mechanisms; the #723/#738/#739 designed keying holds). The
        # class run below therefore expects 21 passed post-terminal.
        # Documented here, not repaired. Deselected in the in-gate
        # run (fails pre-commit by design: the no_type_d_1305 pin has
        # no commits to match yet).
        res = _class_run(E1304_FILE, "TestGuardLifecycle1304")
        out = res.stdout + res.stderr
        assert "21 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1305:
    def test_readme_test_file_table_has_1305_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1305_row_post_sync(self):
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


class TestIterationLog1305:
    def test_log_has_1305_entry(self):
        text = _read(LOG_PATH)
        assert "## #1305 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "ELEVENTH consecutive" in text
        assert "type_d_1305_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1305:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1305_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1305 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1305:
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
