"""Type D iteration #1315: m1018/m1019/m1020 qualitative-discipline
corpus-integrity verification + #1310 background-suite verdict (DEAD
at [  0%]; THIRTEENTH consecutive death of the new streak; tombstone
lineage ONE-HUNDRED-TWENTIETH -> ONE-HUNDRED-TWENTY-FIRST) +
recurring-failure triage (ZERO F marks in the dead stream - nothing
to triage, DETERMINATE-vacuous; no recurring-failure triage repairs
claimed from the stream) + broader regression sweep (1310-1314 window
files; triage recorded in the iteration-log entry) + full suite
RE-LAUNCHED to goal/hidden_files/type_d_1315_full_suite.log.

m1018 (Type A #1312, profiles/competitor-coverage-research.yaml
publications): Politico x OpenAI Decoded-debut marquee CEO platform
(+0.30 MANUAL ILLUSTRATIVE) vs Dahlkamp lobbying expose Meta-as-foil
(+0.05); illustrative delta (OpenAI minus Meta) +0.125 on n=2 vs n=1
(degenerate sample disclosed); scoop channel stays symmetric (m703
continuity); verdict thesis_consistent_observation; NOT a
falsification-family member; ledger holds at 59.

m1019 (Type B #1313, profiles/careers/journalists.yaml
zoe_kleinman_type_b competitor_coverage): Zoe Kleinman (BBC News)
Sep-24-2026 Meta "pervert glasses" camera-free pivot (-0.55 MANUAL
ILLUSTRATIVE, co-bylined Luke Mintz) vs Sep-23-2026 OpenAI Ukraine
cyber-defence gift (+0.25); illustrative delta (OpenAI minus Meta)
+0.80, 1 day apart; ZERO-GRADIENT control (no documented bilateral
BBC x OpenAI/Meta licensing deal in-corpus); verdict
directionally_supported_not_proven; NOT a falsification-family
member; ledger holds at 59.

m1020 (Type C #1314, profiles/competitor-entities.yaml top-level):
Amazon Content Partners in-kind small-publisher program (~mid-Jun
2026 gated preview; AWS WAF bot-traffic control + 1% Associates
uplift + Amazon Publisher Services premium ad inventory + $100/mo AWS
credits with CloudFront; voluntary/fee-free/no-minimums, US-only,
exit-anytime); distinct from the cash Amazon legs (m559 NYT Alexa+
$20-25M/yr, m489/m564 Rufus multi-years); verdict
mechanism_documented; NOT a falsification-family member; ledger holds
at 59; no new direction (fortieth absent by design; thirty-fifth
through thirty-ninth stand).

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
RESEARCH_PATH = os.path.join(
    PROFILES_DIR, "competitor-coverage-research.yaml")
JOURNALISTS_PATH = os.path.join(
    PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1310_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1315_full_suite.log")
OWN_BASENAME = (
    "test_type_d_1315_m1018_m1019_m1020_qualitative_"
    "corpus_integrity_oct08_1pm.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "137d1a952e65889587a464db7d9e96a584078717"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1020
NEXT_NUM = 1021  # integer only; key-form needles are format-built

# Predecessor chain: #1314 Type C closed the 1310-1314 window. #1314
# has no push-status commit (its push status was recorded PENDING in
# the log entry); the other four legs have all five.
PRED_MAIN_1314 = "944d5510"
PRED_ANCHOR_1314 = "1d064d07"
PRED_DOCSYNC_1314 = "efd3bd26"
PRED_FINAL_1314 = "fda5d8c0"
PRED_MAIN_1313 = "fc747c13"
PRED_ANCHOR_1313 = "b65104ac"
PRED_DOCSYNC_1313 = "39aec13d"
PRED_FINAL_1313 = "f8011a00"
PRED_PUSH_1313 = "252ac34b"
PRED_MAIN_1312 = "9e37e42b"
PRED_ANCHOR_1312 = "37e7a7e9"
PRED_DOCSYNC_1312 = "fe67a3bb"
PRED_FINAL_1312 = "ccf522f8"
PRED_PUSH_1312 = "5e67c15a"
PRED_MAIN_1311 = "a9d11a08"
PRED_ANCHOR_1311 = "d12c4a61"
PRED_DOCSYNC_1311 = "b77dad3e"
PRED_FINAL_1311 = "a35c6435"
PRED_PUSH_1311 = "49159cee"
PRED_MAIN_1310 = "84f3c319"
PRED_ANCHOR_1310 = "348e71be"
PRED_DOCSYNC_1310 = "8ef3c029"
PRED_FINAL_1310 = "726bd33f"
PRED_PUSH_1310 = "34e26cae"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the no-Type-D-#1315 own-run pin
# flips green post-repin).
PRED_MAIN_1315 = "137d1a952e65889587a464db7d9e96a584078717"  # re-pinned to main sha per #721

# Forward guard for the next leg: #1316 Type E. Re-pinned by #1316's
# terminal log-hash followup per #721 (starts as 0*40;
# placeholder-only).
PRED_MAIN_1316 = "5d160c6cc9a8d68e863499b4e5fc142845c21060"  # re-pinned by #1316 per #721

# The #1314 window-closing file, for the staleness pin on its guard
# lifecycle (22 tests; post-terminal-followup form is 1 failed / 21
# passed - the no-Type-D-#1315 pin flips at this run's main commit and
# is re-pinned green in the terminal log-hash followup per #721, its
# PRED_MAIN_1315 re-pinned in BOTH files per the #1292 precedent; the
# test_1020_numeric_absent_in_profiles pin stays red permanently BY
# DESIGN, the #1272-class expiry; the 1021-form pins stay green since
# Type D lands no mechanisms).
E1314_FILE = (
    "test_type_c_1314_amazon_content_partners_in_kind_"
    "oct08_12pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 74389  # patched pre-main: pre-sync 74295 + 94 collected
README_FILE_COUNT = 1640  # pre-sync 1639 + 1 (this file)

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
BLOCK_1018 = (
    "type_a_1312_politico_openai_decoded_debut_altman_"
    "marquee_platform_vs_meta_dahlkamp_lobbying_"
    "exposure_oct08_11am"
)
BLOCK_1019 = (
    "type_b_1313_zoe_kleinman_bbc_pervert_glasses_vs_"
    "openai_ukraine_cyber_defence_oct08_12pm"
)
BLOCK_1020 = (
    "type_c_1314_amazon_content_partners_in_kind_"
    "oct08_12pm"
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


def _research_block_1018():
    """Locate the m1018 block under publications in the research file.

    The Type A blocks live directly under the publications top-level
    dict (m1018 sits beside the m703 block it extends). The block
    carries no block_key field in the Type A corpus schema; it is
    identified by its YAML dict key (BLOCK_1018) and its title.
    """
    data = _yaml(RESEARCH_PATH)
    pubs = data.get("publications", {})
    return pubs.get(BLOCK_1018)


def _journalist_block_1019():
    """Locate the m1019 block on the Kleinman record.

    The Type B blocks live under the per-journalist top-level record's
    competitor_coverage dict (m1019 sits on the zoe_kleinman_type_b
    record, the FIRST dedicated Type B pair on Zoe Kleinman and the
    FIRST BBC journalist-level mechanism).
    """
    journalists = _yaml(JOURNALISTS_PATH)
    rec = journalists.get("zoe_kleinman_type_b")
    if not isinstance(rec, dict):
        return None
    cc = rec.get("competitor_coverage", {})
    if isinstance(cc, dict) and BLOCK_1019 in cc:
        return cc[BLOCK_1019]
    return None


def _entities_block_1020():
    """Locate the m1020 block (top-level key of competitor-entities)."""
    entities = _yaml(ENTITIES_PATH)
    return entities.get(BLOCK_1020)


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
    """Fresh engine-layer calibration contract for #1315.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no repo reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_apple_arms = [-0.08, -0.11, -0.06, -0.09, -0.10]
    synthetic_meta_arms = [-0.39, -0.36, -0.42, -0.38, -0.35]
    pooled_apple = (sum(synthetic_apple_arms)
                    / len(synthetic_apple_arms))
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_apple - pooled_meta, 3)


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1315:
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
# 2. Rotation guard: #1314 closed the 1310-1314 window; #1315 opens.
# ---------------------------------------------------------------------------


class TestRotationGuard1315:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-80").stdout
        # #1314 has no push-status commit (its push status was recorded
        # PENDING in the iteration-log entry, asserted separately
        # below); the other four legs contribute all five.
        for sha, label in (
            (PRED_MAIN_1314, "1314 main"),
            (PRED_ANCHOR_1314, "1314 anchor"),
            (PRED_DOCSYNC_1314, "1314 doc-sync"),
            (PRED_FINAL_1314, "1314 log-hash"),
            (PRED_MAIN_1313, "1313 main"),
            (PRED_ANCHOR_1313, "1313 anchor"),
            (PRED_DOCSYNC_1313, "1313 doc-sync"),
            (PRED_FINAL_1313, "1313 log-hash"),
            (PRED_PUSH_1313, "1313 push-status"),
            (PRED_MAIN_1312, "1312 main"),
            (PRED_ANCHOR_1312, "1312 anchor"),
            (PRED_DOCSYNC_1312, "1312 doc-sync"),
            (PRED_FINAL_1312, "1312 log-hash"),
            (PRED_PUSH_1312, "1312 push-status"),
            (PRED_MAIN_1311, "1311 main"),
            (PRED_ANCHOR_1311, "1311 anchor"),
            (PRED_DOCSYNC_1311, "1311 doc-sync"),
            (PRED_FINAL_1311, "1311 log-hash"),
            (PRED_PUSH_1311, "1311 push-status"),
            (PRED_MAIN_1310, "1310 main"),
            (PRED_ANCHOR_1310, "1310 anchor"),
            (PRED_DOCSYNC_1310, "1310 doc-sync"),
            (PRED_FINAL_1310, "1310 log-hash"),
            (PRED_PUSH_1310, "1310 push-status"),
        ):
            assert sha in log, label

    def test_1314_push_status_pending_in_log(self):
        # #1314 recorded its push status as PENDING in the log entry
        # (four commits pushed and ls-remote-verified, no separate
        # push-status commit). This run asserts the record, not a
        # commit.
        text = _read(LOG_PATH)
        assert "Push status (this run): PENDING" in text

    def test_1314_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1314")
        assert "Type C #1314" in out.stdout

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1315-1319 window" in src

    def test_1310_1314_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1310-1314 window is VERIFIED CLOSED" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1315 -> E #1316 -> A #1317 -> B #1318 -> C #1319" in src

    def test_next_window_verdict_belongs_to_1320(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1320 Type D run owns the next verdict" in src


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1018 / m1019 / m1020 all landed and intact.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1315:
    def test_m1018_block_present_in_research(self):
        data = _yaml(RESEARCH_PATH)
        pubs = data["publications"]
        assert BLOCK_1018 in pubs

    def test_m1018_mechanism_id_1018(self):
        block = _research_block_1018()
        assert block is not None
        assert block["mechanism_id"] == 1018
        assert block["iteration"] == 1312
        assert block["iteration_type"] == "A"

    def test_m1018_title_identifies_block(self):
        # The m1018 block carries no block_key field in the Type A
        # corpus schema; the block is identified by its YAML dict
        # key (BLOCK_1018, asserted present above) and its title.
        block = _research_block_1018()
        assert "Politico" in block["title"]
        assert "OpenAI" in block["title"]

    def test_m1018_verdict_thesis_consistent(self):
        # m1018 is a thesis_consistent_observation (the naive uniform
        # payer-softening prediction MET on the Decoded-debut
        # marquee-platform register, not falsified on the scoop
        # channel); NOT a falsification-family member; ledger holds
        # at 59. The verdict is a direct field on the m1018 block
        # (the Type A research schema).
        block = _research_block_1018()
        assert block["verdict"] == "thesis_consistent_observation"
        assert "thesis_consistent_observation" in str(
            block["statistical_discipline"])

    def test_m1018_not_a_member_ledger_59(self):
        block = _research_block_1018()
        ff = str(block["falsification_family"])
        assert "NOT a falsification-family member" in ff
        assert "ledger holds at 59" in ff.lower()

    def test_m1018_author(self):
        block = _research_block_1018()
        assert block["author"] == "Kit (with Ray)"

    def test_m1019_block_present_in_journalists(self):
        assert _journalist_block_1019() is not None

    def test_m1019_mechanism_id_1019(self):
        block = _journalist_block_1019()
        assert block["mechanism_id"] == 1019
        assert block["iteration"] == 1313
        assert block["iteration_type"] == "B"

    def test_m1019_block_key_field(self):
        block = _journalist_block_1019()
        assert block["block_key"] == BLOCK_1019

    def test_m1019_verdict_directionally_supported(self):
        # m1019 is a directionally_supported_not_proven
        # zero-gradient control observation, NOT a
        # falsification-family member; ledger holds at 59.
        block = _journalist_block_1019()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["falsification_family_member"] is False

    def test_m1019_not_a_member_in_notes(self):
        # The FIRST dedicated Type B pair on Zoe Kleinman and the
        # FIRST BBC journalist-level mechanism; the record notes
        # carry the ledger position.
        rec = _yaml(JOURNALISTS_PATH)["zoe_kleinman_type_b"]
        assert "FIRST" in rec["notes"]
        assert "ledger holds at 59" in rec["notes"]
        assert _journalist_block_1019()["author"] == "Kit (with Ray)"

    def test_m1020_block_present_in_entities(self):
        entities = _yaml(ENTITIES_PATH)
        assert BLOCK_1020 in entities

    def test_m1020_mechanism_id_1020(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1020]
        assert block["mechanism_id"] == 1020
        assert block["iteration"] == 1314
        assert block["iteration_type"] == "C"

    def test_m1020_block_key_field(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1020]["block_key"] == BLOCK_1020

    def test_m1020_verdict_mechanism_documented(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1020]
        assert block["verdict"] == "mechanism_documented"
        assert block["falsification_family_member"] is False
        assert "ledger holds at 59" in block["falsification_family"]

    def test_m1020_author(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1020]["author"] == "Kit (with Ray)"

    def test_max_numeric_mechanism_id_is_1020(self):
        assert _max_numeric_mechanism_id() == MECH_NUM


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1310 suite is DEAD at [  0%].
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1315:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG

    def test_prior_suite_stalled_at_0(self):
        # The #1310-launched suite froze at [  0%] progress: 276
        # bytes, zero F marks, last write Oct 8 2026 09:35 PDT (~3.5h
        # stale at this run's ~01:00 PM PDT check), zero live pytest
        # processes (the pgrep/ps sweep at this run's check returned
        # zero live pytest processes; the /proc open-fd check returns
        # empty). Progress never regresses, so the [  0%] marker
        # stays present and [  1%] never arrives. Observation history:
        # #1310 launched it and saw it ALIVE at doc-sync (dots
        # accumulating); #1311 saw it ALIVE at ~10:00 AM PDT (1 live
        # pytest process); #1312 saw it ALIVE at ~11:00 AM PDT (live
        # pytest processes); #1313 saw it ALIVE at ~12:00 PM PDT (1
        # live pytest process); #1314 saw it STALLED at ~12:00 PM PDT
        # (zero live processes).
        text = _read(PRIOR_SUITE_LOG)
        assert "[  0%]" in text, text[-2000:]
        assert "[  1%]" not in text
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
        # type_d_1310_full_suite.log open anymore (the /proc open-fd
        # check returns empty; the pgrep/ps sweep at this run's
        # ~01:00 PM PDT check returned zero live pytest processes).
        holders = _proc_holds_log("type_d_1310_full_suite.log")
        assert holders == "", holders

    def test_thirteenth_death_of_new_streak(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite
        # completed). The 43-run streak BROKE at #1250 (the #1245
        # suite was verdict ALIVE at 20%). #1255 verdict the FIRST
        # consecutive background-suite death of the new streak, #1260
        # the SECOND, #1265 the THIRD, #1270 the FOURTH, #1275 the
        # FIFTH, #1280 the SIXTH, #1285 the SEVENTH, #1290-launched
        # the EIGHTH (#1295 verdict), #1295-launched the NINTH (#1300
        # verdict), #1300-launched the TENTH (#1305 verdict),
        # #1305-launched the ELEVENTH (#1310 verdict), #1310-launched
        # the TWELFTH... no: #1310 verdict the TWELFTH consecutive
        # death. This verdict is the THIRTEENTH consecutive
        # background-suite death of the new streak.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRTEENTH consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-TWENTIETH -> ONE-HUNDRED-TWENTY-FIRST.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ONE-HUNDRED-TWENTY-FIRST" in src
        assert "lineage advances" in src

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1315 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_PATH)
        assert "THIRTEENTH consecutive" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: DETERMINATE-vacuous (zero F marks).
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1315:
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


class TestStatisticalDiscipline1315:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: the max numeric mechanism id is
        # unchanged at 1020 and no 1021-form keys exist.
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_engine_not_run_on_corpus(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run on corpus" in src

    def test_synthetic_calibration_delta_contract(self):
        # Engine-layer contract only (never a finding): synthetic
        # Apple arms [-0.08, -0.11, -0.06, -0.09, -0.10] vs synthetic
        # Meta arms [-0.39, -0.36, -0.42, -0.38, -0.35] -> pooled
        # delta +0.292.
        assert _synthetic_calibration_delta() == 0.292


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 59; guards on member forms.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1315:
    def test_ledger_holds_at_59(self):
        # m1018 carries the ledger-holds-at-59 note in its
        # falsification_family; m1019 and m1020 hold it in their
        # record notes / falsification_family fields.
        block = _research_block_1018()
        assert "ledger holds at 59" in str(
            block["falsification_family"]).lower()
        rec = _yaml(JOURNALISTS_PATH)["zoe_kleinman_type_b"]
        assert "ledger holds at 59" in rec["notes"]
        entities = _yaml(ENTITIES_PATH)
        assert "ledger holds at 59" in entities[
            BLOCK_1020]["falsification_family"]

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
# 8. Guard lifecycle: forward pins for #1316; #1314 staged for this run.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1315:
    def test_pins_on_1020_no_landing(self):
        # Type D lands no mechanisms: max stays 1020, next stays 1021.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1020" in src
        assert "NEXT_NUM = 1021" in src

    def test_no_type_d_1315_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721): every commit whose message
        # matches "Type D #1315" must be this run's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type D #1315")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1315's own commits"
        main = _git("rev-parse", PRED_MAIN_1315).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_e_1316_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1316's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1316" must be #1316's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type E #1316")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1316's own commits"
        main = _git("rev-parse", PRED_MAIN_1316).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1021_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1021_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1021_dash_absent_repo_wide(self):
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

    def test_predecessor_1314_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1314_FILE))

    def test_next_leg_is_1316_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1316 Type E" in src

    def test_1314_pins_flip_documented(self):
        # #1314 staged guard-lifecycle forward pins for this run
        # (no-Type-D-#1315-in-git-log, zero one-zero-two-one keys all
        # forms, fortieth direction absent, forty-eighth through
        # fifty-ninth members intact, no sixtieth member); all
        # verified GREEN pre-commit this run (manual forward-guard
        # verification, recorded in the iteration-log entry). The
        # no-Type-D-#1315 pin flips BY DESIGN at this run's main
        # commit (the #1191-class self-trip, re-pinned post-commit by
        # TestStalenessPins1315); the 1021-form pins stay green
        # because Type D lands no mechanisms. Documented in the
        # staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1315" in src
        assert "no_type_d_1315_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1314's guard lifecycle flips once, then re-pins.
# ---------------------------------------------------------------------------


class TestStalenessPins1315:
    def test_1314_guard_lifecycle_post_terminal_self_trip(self):
        # Post-terminal-followup form: 22 tests in the class, ALL
        # GREEN. The no_type_d_1315_in_git_log pin flips BY DESIGN
        # when this run's main commit lands and is re-pinned green in
        # the terminal log-hash followup per #721 (PRED_MAIN_1315
        # re-pinned to this run's main sha in BOTH this file and the
        # #1314 file per the #1292 precedent). The 1021-form pins stay
        # green throughout (Type D lands no mechanisms; the
        # #723/#738/#739 designed keying holds). (The
        # test_1020_numeric_absent_in_profiles pin that stays red
        # permanently BY DESIGN - the #1272-class expiry - lives in
        # the #1313 file's guard lifecycle, not here.) The class run
        # below therefore expects 22 passed. The #1314 block is
        # read-only to this run; the flips are documented here, not
        # repaired. Deselected in the in-gate run (fails pre-commit
        # by design).
        res = _class_run(E1314_FILE, "TestGuardLifecycle1314")
        out = res.stdout + res.stderr
        assert "22 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1315:
    def test_readme_test_file_table_has_1315_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1315_row_post_sync(self):
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


class TestIterationLog1315:
    def test_log_has_1315_entry(self):
        text = _read(LOG_PATH)
        assert "## #1315 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "THIRTEENTH consecutive" in text
        assert "type_d_1315_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1315:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1315_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1315 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1315:
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
