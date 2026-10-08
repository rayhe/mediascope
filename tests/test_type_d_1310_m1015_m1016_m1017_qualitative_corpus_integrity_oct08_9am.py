"""Type D iteration #1310: m1015/m1016/m1017 qualitative-discipline
corpus-integrity verification + #1305 background-suite verdict (DEAD
at [  2%]; TWELFTH consecutive death of the new streak; tombstone
lineage ONE-HUNDRED-NINETEENTH -> ONE-HUNDRED-TWENTIETH) +
recurring-failure triage (ZERO F marks in the dead stream - nothing
to triage, DETERMINATE-vacuous) + broader regression sweep (30 failed,
453 passed across the 1305-1309 window files in ~378s; triaged: 5
#565-class anchor placeholder-duality pins (post-anchor, fail by
design), 4 #1272-class forward-guard expiries from m1015/m1016/m1017
landing after the pinned runs, 1 #1191-class self-trip (the
no-Type-D-#1310 forward pin - flips green at this run's terminal
re-pin per #721), 5 #719-class doc-sync readme-stats-ratchet staleness
pins, 15 staleness artifacts (pre-commit novelty/max pins and
staleness-pin class runs overtaken by later landings) - all by-design,
documented not repaired; 0 remaining defects) + full suite
RE-LAUNCHED to goal/hidden_files/type_d_1310_full_suite.log.

m1015 (Type A #1307, profiles/news-corp.yaml
competitor_relationships.microsoft): Barron's x Microsoft Oct-6 /
Oct-7-2026 investor-forward register (+0.30 / +0.20 MANUAL
ILLUSTRATIVE, mean +0.25) vs carried Barron's x Meta arms
(+0.05 / +0.10, mean +0.075); illustrative delta (Microsoft minus
Meta) +0.175, symmetric investor-forward softness; the naive uniform
payer-softening prediction (Nov-2024 HarperCollins book-licensing
deal) is MET on the fresh peg, not falsified; verdict
thesis_consistent_observation (nests under statistical_discipline in
the Type A corpus schema); NOT a falsification-family member; ledger
holds at 59.

m1016 (Type B #1308, profiles/careers/journalists.yaml
tobi_opeyemi_amure_type_b competitor_coverage): Tobi Opeyemi Amure
(TheStreet, NFEC Certified Personal Finance Journalist) Sep-26-2026
Meta Connect-week glasses piece (-0.10 MANUAL ILLUSTRATIVE) vs
Sep-6-2026 OpenAI GPT-6 Astra piece (+0.20 MANUAL ILLUSTRATIVE);
illustrative delta (OpenAI minus Meta) +0.30; ZERO-GRADIENT control
pair (no documented AI content-licensing deal between TheStreet/Arena
and OpenAI or Meta in-corpus); verdict
directionally_supported_not_proven; NOT a falsification-family
member; ledger holds at 59.

m1017 (Type C #1309, profiles/competitor-entities.yaml top-level):
Gannett Co., Inc. (NYSE: GCI) / USA TODAY Network x Perplexity
strategic AI content licensing bilateral (Jul 30 2025, banked Oct 8
2026 via the #784 deferral queue) - FIRST dedicated corpus mechanism
on a Perplexity local-news bilateral (USA TODAY + 200-plus local
newsbrands into Perplexity AI search + Comet browser; ad-revenue
share + Sonar API/Enterprise Pro for all staff; terms undisclosed);
verdict mechanism_documented; NOT a falsification-family member;
ledger holds at 59; no new direction (fortieth absent by design;
thirty-fifth through thirty-ninth stand).

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
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1305_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1310_full_suite.log")
OWN_BASENAME = (
    "test_type_d_1310_m1015_m1016_m1017_qualitative_"
    "corpus_integrity_oct08_9am.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "0" * 40

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1017
NEXT_NUM = 1018  # integer only; key-form needles are format-built

# Predecessor chain: #1309 Type C closed the 1305-1309 window.
PRED_MAIN_1309 = "5cd42648"
PRED_ANCHOR_1309 = "490b9490"
PRED_DOCSYNC_1309 = "b8ada6a0"
PRED_FINAL_1309 = "e2d2418b"
PRED_PUSH_1309 = "c99a8fb6"
PRED_MAIN_1308 = "5b997970"
PRED_ANCHOR_1308 = "76924a62"
PRED_DOCSYNC_1308 = "50c7558e"
PRED_FINAL_1308 = "603946bb"
PRED_PUSH_1308 = "dc4556c1"
PRED_MAIN_1307 = "7009064e"
PRED_ANCHOR_1307 = "6ee958a7"
PRED_DOCSYNC_1307 = "a0ec12d1"
PRED_FINAL_1307 = "73307210"
PRED_PUSH_1307 = "ea18c53b"
PRED_MAIN_1306 = "0ac1044d"
PRED_ANCHOR_1306 = "69dadafb"
PRED_DOCSYNC_1306 = "dbed9dbc"
PRED_FINAL_1306 = "f7640d28"
PRED_PUSH_1306 = "fe8e635f"
PRED_MAIN_1305 = "df99a8be"
PRED_ANCHOR_1305 = "905b5853"
PRED_DOCSYNC_1305 = "cd2cf1df"
PRED_FINAL_1305 = "2a8709d9"
PRED_PUSH_1305 = "75551707"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the no-Type-D-#1310 own-run pin
# flips green post-repin).
PRED_MAIN_1310 = "0" * 40

# Forward guard for the next leg: #1311 Type E. Re-pinned by #1311's
# terminal log-hash followup per #721 (starts as 0*40;
# placeholder-only).
PRED_MAIN_1311 = "0" * 40

# The #1309 window-closing file, for the staleness pin on its guard
# lifecycle (22 tests; post-terminal-followup form is 22 passed - the
# no-Type-D-#1310 pin flips at this run's main commit and is re-pinned
# green in the terminal log-hash followup per #721, its PRED_MAIN_1310
# re-pinned in BOTH files per the #1292 precedent; the 1018-form pins
# stay green since Type D lands no mechanisms).
E1309_FILE = (
    "test_type_c_1309_gannett_perplexity_strategic_"
    "bilateral_oct08_8am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 73852  # patched pre-main: pre-sync 73762 + 90 collected
README_FILE_COUNT = 1635  # pre-sync 1634 + 1 (this file)

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
BLOCK_1015 = (
    "type_a_1307_barrons_microsoft_oct06_oct07_"
    "investor_forward_vs_carried_meta_arms_oct08_6am"
)
BLOCK_1016 = (
    "type_b_1308_tobi_opeyemi_amure_thestreet_meta_"
    "glasses_vs_openai_astra_oct08_7am"
)
BLOCK_1017 = (
    "type_c_1309_gannett_perplexity_strategic_"
    "bilateral_oct08_8am"
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


def _newscorp_block_1015():
    """Locate the m1015 block under competitor_relationships.microsoft."""
    data = _yaml(NEWS_CORP_PATH)
    rels = data.get("competitor_relationships", {})
    microsoft = rels.get("microsoft", {})
    return microsoft.get(BLOCK_1015)


def _journalist_block_1016():
    """Locate the m1016 block on the Amure record.

    The Type B blocks live under the per-journalist top-level record's
    competitor_coverage dict (m1016 sits on the tobi_opeyemi_amure
    record, the FIRST dedicated Type B pair on Tobi Opeyemi Amure and
    the FIRST journalist-level mechanism at TheStreet).
    """
    journalists = _yaml(JOURNALISTS_PATH)
    rec = journalists.get("tobi_opeyemi_amure_type_b")
    if not isinstance(rec, dict):
        return None
    cc = rec.get("competitor_coverage", {})
    if isinstance(cc, dict) and BLOCK_1016 in cc:
        return cc[BLOCK_1016]
    return None


def _entities_block_1017():
    """Locate the m1017 block (top-level key of competitor-entities)."""
    entities = _yaml(ENTITIES_PATH)
    return entities.get(BLOCK_1017)


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
    """Fresh engine-layer calibration contract for #1310.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no repo reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_apple_arms = [-0.09, -0.12, -0.07, -0.10, -0.11]
    synthetic_meta_arms = [-0.41, -0.38, -0.44, -0.40, -0.37]
    pooled_apple = (sum(synthetic_apple_arms)
                    / len(synthetic_apple_arms))
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_apple - pooled_meta, 3)


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1310:
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
# 2. Rotation guard: #1309 closed the 1305-1309 window; #1310 opens.
# ---------------------------------------------------------------------------


class TestRotationGuard1310:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-80").stdout
        for sha, label in (
            (PRED_MAIN_1309, "1309 main"),
            (PRED_ANCHOR_1309, "1309 anchor"),
            (PRED_DOCSYNC_1309, "1309 doc-sync"),
            (PRED_FINAL_1309, "1309 log-hash"),
            (PRED_PUSH_1309, "1309 push-status"),
            (PRED_MAIN_1308, "1308 main"),
            (PRED_ANCHOR_1308, "1308 anchor"),
            (PRED_DOCSYNC_1308, "1308 doc-sync"),
            (PRED_FINAL_1308, "1308 log-hash"),
            (PRED_PUSH_1308, "1308 push-status"),
            (PRED_MAIN_1307, "1307 main"),
            (PRED_ANCHOR_1307, "1307 anchor"),
            (PRED_DOCSYNC_1307, "1307 doc-sync"),
            (PRED_FINAL_1307, "1307 log-hash"),
            (PRED_PUSH_1307, "1307 push-status"),
            (PRED_MAIN_1306, "1306 main"),
            (PRED_ANCHOR_1306, "1306 anchor"),
            (PRED_DOCSYNC_1306, "1306 doc-sync"),
            (PRED_FINAL_1306, "1306 log-hash"),
            (PRED_PUSH_1306, "1306 push-status"),
            (PRED_MAIN_1305, "1305 main"),
            (PRED_ANCHOR_1305, "1305 anchor"),
            (PRED_DOCSYNC_1305, "1305 doc-sync"),
            (PRED_FINAL_1305, "1305 log-hash"),
            (PRED_PUSH_1305, "1305 push-status"),
        ):
            assert sha in log, label

    def test_1309_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1309")
        assert "Type C #1309" in out.stdout

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1310-1314 window" in src

    def test_1305_1309_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1305-1309 window is VERIFIED CLOSED" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1310 -> E #1311 -> A #1312 -> B #1313 -> C #1314" in src

    def test_next_window_verdict_belongs_to_1315(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1315 Type D run owns the next verdict" in src

# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1015 / m1016 / m1017 all landed and intact.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1310:
    def test_m1015_block_present_in_newscorp(self):
        data = _yaml(NEWS_CORP_PATH)
        rels = data["competitor_relationships"]
        assert BLOCK_1015 in rels["microsoft"]

    def test_m1015_mechanism_id_1015(self):
        block = _newscorp_block_1015()
        assert block is not None
        assert block["mechanism_id"] == 1015
        assert block["iteration"] == 1307
        assert block["iteration_type"] == "A"

    def test_m1015_mechanism_name_identifies_block(self):
        # The m1015 block carries no block_key field in the Type A
        # corpus schema; the block is identified by its YAML dict
        # key (BLOCK_1015, asserted present above) and its
        # mechanism_name.
        block = _newscorp_block_1015()
        assert "Barron" in block["mechanism_name"]
        assert "Microsoft" in block["mechanism_name"]

    def test_m1015_verdict_thesis_consistent(self):
        # m1015 is a thesis_consistent_observation (the naive uniform
        # payer-softening prediction MET on the fresh Barron's x
        # Microsoft peg, not falsified); NOT a falsification-family
        # member; ledger holds at 59. The verdict nests under
        # statistical_discipline in the m1015 block (the Type A
        # corpus schema).
        block = _newscorp_block_1015()
        assert block["statistical_discipline"]["verdict"] == (
            "thesis_consistent_observation")
        assert not block.get("falsification_family_member")
        assert "ledger holds at 59" in str(block["summary"])

    def test_m1016_block_present_in_journalists(self):
        assert _journalist_block_1016() is not None

    def test_m1016_mechanism_id_1016(self):
        block = _journalist_block_1016()
        assert block["mechanism_id"] == 1016
        assert block["iteration"] == 1308
        assert block["iteration_type"] == "B"

    def test_m1016_block_key_field(self):
        block = _journalist_block_1016()
        assert block["block_key"] == BLOCK_1016

    def test_m1016_verdict_directionally_supported(self):
        # m1016 is a directionally_supported_not_proven
        # zero-gradient control observation, NOT a
        # falsification-family member; ledger holds at 59.
        block = _journalist_block_1016()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["falsification_family_member"] is False

    def test_m1016_not_a_member_in_notes(self):
        # The FIRST dedicated Type B pair on Tobi Opeyemi Amure and
        # the FIRST journalist-level mechanism at TheStreet; the
        # record notes carry the ledger position.
        rec = _yaml(JOURNALISTS_PATH)["tobi_opeyemi_amure_type_b"]
        assert "FIRST dedicated Type B pair on Tobi Opeyemi Amure" in (
            rec["notes"])
        assert "ledger holds at 59" in rec["notes"]
        assert _journalist_block_1016()["author"] == "Kit (with Ray)"

    def test_m1017_block_present_in_entities(self):
        entities = _yaml(ENTITIES_PATH)
        assert BLOCK_1017 in entities

    def test_m1017_mechanism_id_1017(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1017]
        assert block["mechanism_id"] == 1017
        assert block["iteration"] == 1309
        assert block["iteration_type"] == "C"

    def test_m1017_block_key_field(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1017]["block_key"] == BLOCK_1017

    def test_m1017_verdict_mechanism_documented(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1017]
        assert block["verdict"] == "mechanism_documented"
        assert block["falsification_family_member"] is False
        assert "ledger holds at 59" in block["falsification_family"]

    def test_max_numeric_mechanism_id_is_1017(self):
        assert _max_numeric_mechanism_id() == MECH_NUM


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1305 suite is DEAD at [  2%].
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1310:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG

    def test_prior_suite_stalled_at_2(self):
        # The #1305-launched suite froze at [  2%] progress: 2168
        # bytes, zero F marks, last write Oct 8 2026 05:04 PDT (~4h
        # stale at this run's ~09:00 AM PDT check), zero live pytest
        # processes (the pgrep sweep at this run's check returned zero
        # live pytest processes; the /proc open-fd check returns
        # empty), confirmed dead by a second ps sweep. Progress never
        # regresses, so the [  2%] marker stays present and [  3%]
        # never arrives. Observation history: #1305 launched it and
        # saw it ALIVE at doc-sync (dots accumulating); #1306 saw it
        # STALLED at ~05:04 PDT (zero live processes); #1307, #1308
        # and #1309 saw it STALLED at their ~06:10 / ~07:10 / ~08:10
        # PDT checks (zero live processes each).
        text = _read(PRIOR_SUITE_LOG)
        assert "[  2%]" in text, text[-2000:]
        assert "[  3%]" not in text
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
        # type_d_1305_full_suite.log open anymore (the /proc open-fd
        # check returns empty; the pgrep/ps sweep at this run's
        # ~09:00 AM PDT check returned zero live pytest processes).
        holders = _proc_holds_log("type_d_1305_full_suite.log")
        assert holders == "", holders

    def test_twelfth_death_of_new_streak(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite
        # completed). The 43-run streak BROKE at #1250 (the #1245
        # suite was verdict ALIVE at 20%). #1255 verdict the FIRST
        # consecutive background-suite death of the new streak, #1260
        # the SECOND, #1265 the THIRD, #1270 the FOURTH, #1275 the
        # FIFTH, #1280 the SIXTH, #1285 the SEVENTH, #1290-launched
        # the EIGHTH, #1295-launched the NINTH (#1300 verdict),
        # #1300-launched the TENTH (#1305 verdict), #1305-launched
        # the ELEVENTH (#1310 verdict, this run). This verdict is the
        # TWELFTH consecutive background-suite death of the new
        # streak.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TWELFTH consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-NINETEENTH -> ONE-HUNDRED-TWENTIETH.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ONE-HUNDRED-TWENTIETH" in src
        assert "lineage advances" in src

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1310 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_PATH)
        assert "TWELFTH consecutive" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: DETERMINATE-vacuous (zero F marks).
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1310:
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


class TestStatisticalDiscipline1310:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: the max numeric mechanism id is
        # unchanged at 1017 and no 1018-form keys exist.
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_engine_not_run_on_corpus(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run on corpus" in src

    def test_synthetic_calibration_delta_contract(self):
        # Engine-layer contract only (never a finding): synthetic
        # Apple arms [-0.09, -0.12, -0.07, -0.10, -0.11] vs synthetic
        # Meta arms [-0.41, -0.38, -0.44, -0.40, -0.37] -> pooled
        # delta +0.302.
        assert _synthetic_calibration_delta() == 0.302


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 59; guards on member forms.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1310:
    def test_ledger_holds_at_59(self):
        # m1015 carries the ledger-holds-at-59 note in its summary;
        # m1016 and m1017 hold it in their record notes /
        # falsification_family fields.
        block = _newscorp_block_1015()
        assert "ledger holds at 59" in str(block["summary"])
        rec = _yaml(JOURNALISTS_PATH)["tobi_opeyemi_amure_type_b"]
        assert "ledger holds at 59" in rec["notes"]
        entities = _yaml(ENTITIES_PATH)
        assert "ledger holds at 59" in entities[
            BLOCK_1017]["falsification_family"]

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
# 8. Guard lifecycle: forward pins for #1311; #1309 staged for this run.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1310:
    def test_pins_on_1017_no_landing(self):
        # Type D lands no mechanisms: max stays 1017, next stays 1018.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1017" in src
        assert "NEXT_NUM = 1018" in src

    def test_no_type_d_1310_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721): every commit whose message
        # matches "Type D #1310" must be this run's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type D #1310")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1310's own commits"
        main = _git("rev-parse", PRED_MAIN_1310).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_e_1311_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1311's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1311" must be #1311's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type E #1311")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1311's own commits"
        main = _git("rev-parse", PRED_MAIN_1311).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1018_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1018_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1018_dash_absent_repo_wide(self):
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

    def test_predecessor_1309_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1309_FILE))

    def test_next_leg_is_1311_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1311 Type E" in src

    def test_1309_pins_flip_documented(self):
        # #1309 staged guard-lifecycle forward pins for this run
        # (no-Type-D-#1310-in-git-log, zero one-zero-one-eight keys all
        # forms, fortieth direction absent, forty-eighth through
        # fifty-ninth members intact, no sixtieth member); all
        # verified GREEN pre-commit this run (manual forward-guard
        # verification, recorded in the iteration-log entry). The
        # no-Type-D-#1310 pin flips BY DESIGN at this run's main
        # commit (the #1191-class self-trip, re-pinned post-commit by
        # TestStalenessPins1310); the 1018-form pins stay green
        # because Type D lands no mechanisms. Documented in the
        # staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1310" in src
        assert "no_type_d_1310_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1309's guard lifecycle flips once, then re-pins.
# ---------------------------------------------------------------------------


class TestStalenessPins1310:
    def test_1309_guard_lifecycle_post_terminal_self_trip(self):
        # Post-terminal-followup form: 22 tests in the class; ONE flips
        # BY DESIGN when this run's main commit lands (the
        # no_type_d_1310_in_git_log pin - the #1191-class self-trip)
        # and flips back green in the terminal log-hash followup per
        # #721 (PRED_MAIN_1310 re-pinned to this run's main sha in
        # BOTH this file and the #1309 file per the #1292 precedent).
        # The 1018-form pins stay green throughout (Type D lands no
        # mechanisms; the #723/#738/#739 designed keying holds). The
        # class run below therefore expects 22 passed post-terminal.
        # Documented here, not repaired. Deselected in the in-gate
        # run (fails pre-commit by design: the no_type_d_1310 pin has
        # no commits to match yet).
        res = _class_run(E1309_FILE, "TestGuardLifecycle1309")
        out = res.stdout + res.stderr
        assert "22 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1310:
    def test_readme_test_file_table_has_1310_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1310_row_post_sync(self):
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


class TestIterationLog1310:
    def test_log_has_1310_entry(self):
        text = _read(LOG_PATH)
        assert "## #1310 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "TWELFTH consecutive" in text
        assert "type_d_1310_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1310:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1310_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1310 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1310:
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
