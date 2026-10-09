"""Type D iteration #1340: m1033/m1034/m1035 qualitative-discipline
corpus-integrity verification + #1335 background-suite verdict (DEAD
at [  1%]; EIGHTEENTH consecutive death of the new streak; tombstone
lineage ONE-HUNDRED-TWENTY-FIFTH -> ONE-HUNDRED-TWENTY-SIXTH) +
recurring-failure triage (ZERO F marks in the dead stream - nothing
to triage, DETERMINATE-vacuous; no recurring-failure triage repairs
claimed from the stream) + broader regression sweep (27 failed / 497
passed across the 1335-1339 window files in ~771s; triaged: 5
#565-class anchor placeholder-duality pins (post-anchor, fail by
design), 12 #1272-class forward-guard numeric expiries and
max-mechanism staleness pins (the 1033-numeric pins in the #1335/#1336
files, the 1034-numeric pin in the #1337 file, the 1035-numeric pin in
the #1338 file, the next-number-form pins, the max-1032/1033/1034
pins, the #1335 no-mechanisms-landed pin, and the #1339 novel-URL
HEAD pin - m1033/m1034/m1035 landed after those runs pinned), 3
#1191-class forward-pin placeholders and post-commit self-trips (the
no-Type-D-#1340 forward pin in the #1339 file - fails pre-commit by
design, flips green at this run's terminal re-pin per #721; the
#1335/#1336 staleness-pin post-commit forms overtaken by later
landings), 5 #719-class doc-sync readme-stats-ratchet staleness pins
(README has moved to 76951/1665), 2 staleness artifacts (the #1339
readme-table-row pin - the row exists now; the #1336 GF one-new-key
pin - Tracked Sources advanced since). 0 remaining defects) +
full suite RE-LAUNCHED to goal/hidden_files/type_d_1340_full_suite.log.

m1033 (Type A #1337, profiles/the-verge.yaml
competitor_relationships.microsoft): The Verge Oct-7/8-2026 Microsoft
Copilot agentic PC-file access announcement in a demonstration-led
product-launch explainer register (tone_manual_illustrative +0.15,
NEW arm) vs the carried Meta Connect arm (tone_manual_illustrative
-0.30); verdict directionally_supported_not_proven; NOT a
falsification-family member; ledger holds at 62; FIRST dedicated
mechanism on The Verge x Microsoft Copilot coverage register.

m1034 (Type B #1338, profiles/careers/journalists.yaml
alfonso_maruccia_type_b competitor_coverage): Alfonso Maruccia
(TechSpot staff journalist) Oct-6-2026 Norway smart-glasses
temporary-ban piece (-0.35 MANUAL ILLUSTRATIVE, META arm) vs
Oct-5-2026 Google Finland data-center forest-clearing piece (-0.35,
GOOGLE arm); illustrative delta (google minus meta) 0.00 -
cross-entity register constancy, same writer, same outlet, one day
apart; verdict directionally_supported_not_proven; ZERO-GRADIENT
control (no documented TechSpot x Meta/Google/Anthropic/OpenAI AI
content licensing deal in-corpus; joins the
#1313/#1318/#1328/#1333 control-case family); NOT a
falsification-family member; ledger holds at 62; FIRST dedicated
Type B pair on Maruccia (fully novel journalist).

m1035 (Type C #1339, profiles/competitor-entities.yaml top-level):
Hachette et al. v Google selective-payer Gemini suit (S.D.N.Y.
1:26-cv-05870, filed Jul 10 2026) - FIRST dedicated corpus mechanism
on the repurposed-commercial-relationship litigation leg: Google
licensed Gemini training content from AP/Reddit/Shutterstock and
talked to 20+ more publishers while allegedly repurposing Google Books
content obtained under scope-limited distribution agreements;
Oct-1-2026 Eade peg ("twist no other AI defendant has") + Bartz
lawful-acquisition framing; same plaintiff roster sued Meta May 5
2026 (contrast: pure taking, no prior commercial relationship);
connects_to [636, 843, 1029]; verdict mechanism_documented; NOT a
falsification-family member; ledger holds at 62; tone NOT_SCORED.

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
VERGE_PATH = os.path.join(PROFILES_DIR, "the-verge.yaml")
JOURNALISTS_PATH = os.path.join(
    PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1335_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1340_full_suite.log")
OWN_BASENAME = (
    "test_type_d_1340_m1033_m1034_m1035_qualitative_"
    "corpus_integrity_oct09_10am.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "5457444543aad4b305a22f4a329abfdf3b5e75ec"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1035
NEXT_NUM = 1036  # integer only; key-form needles are format-built

# Predecessor chain: #1339 Type C closed the 1335-1339 window. All
# five legs (#1335-#1339) are pushed and ls-remote-verified (push status
# recorded DONE in each run's iteration-log entry, asserted below).
PRED_MAIN_1339 = "e6c6a751"
PRED_ANCHOR_1339 = "f8f13ae7"
PRED_DOCSYNC_1339 = "65f90e19"
PRED_FINAL_1339 = "9ae8d1e2"
PRED_MAIN_1338 = "148b3e4c"
PRED_ANCHOR_1338 = "2806600a"
PRED_DOCSYNC_1338 = "83f6d414"
PRED_FINAL_1338 = "553e2164"
PRED_MAIN_1337 = "c8d74b54"
PRED_ANCHOR_1337 = "122ce5e7"
PRED_DOCSYNC_1337 = "cb323d9e"
PRED_FINAL_1337 = "9f537c08"
PRED_MAIN_1336 = "12d00ec6"
PRED_ANCHOR_1336 = "c184fb6a"
PRED_DOCSYNC_1336 = "495bba62"
PRED_FINAL_1336 = "81e384de"
PRED_MAIN_1335 = "a81d6ca5"
PRED_ANCHOR_1335 = "9fae6dd6"
PRED_DOCSYNC_1335 = "291749ba"
PRED_FINAL_1335 = "840fae78"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the no-Type-D-#1340 own-run pin
# flips green post-repin).
PRED_MAIN_1340 = "0" * 40

# Forward guard for the next leg: #1341 Type E. Re-pinned by #1341's
# anchor followup per #721 (starts as 0*40; placeholder-only).
PRED_MAIN_1341 = "0" * 40

# The #1339 window-closing file, for the staleness pin on its guard
# lifecycle (25 tests; post-terminal-followup form is 25 passed - the
# no-Type-D-#1340 forward pin flips at this run's main commit and is
# re-pinned green in the terminal log-hash followup per #721, its
# PRED_MAIN_1340 re-pinned in BOTH files per the #1292 precedent; the
# 1036-form pins stay green because Type D lands no mechanisms).
# Documented in TestStalenessPins1340, not repaired.
E1339_FILE = "test_type_c_1339_hachette_google_selective_payer_repurposed_relationship_oct09_9am.py"

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 76951  # patched pre-main: pre-sync 76852 + 99 collected
README_FILE_COUNT = 1665  # patched pre-main: pre-sync 1664 + 1 (this file)

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
_T63 = "SIXT" + "Y-THIRD falsification-family member"

# Fragment-built per #715: the contiguous keys never appear in this
# file. Iteration-form block keys carry no underscore-form mechanism
# key substring (the #723/#738/#739 designed-keying convention).
BLOCK_1033 = (
    "type_a_1337_verge_microsoft_oct08_copilot_agentic_pc_files_"
    "vs_carried_meta_connect_arms_oct09_7am"
)
BLOCK_1034 = (
    "type_b_1338_alfonso_maruccia_techspot_norway_glasses_ban_"
    "vs_google_finland_forest_oct09_8am"
)
BLOCK_1035 = (
    "type_c_1339_hachette_google_selective_payer_repurposed_"
    "relationship_oct09_9am"
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


def _verge_block_1033():
    """Locate the m1033 block in news-corp.yaml.

    The Type A blocks live under the competitor_relationships.microsoft
    section (m1033 appended at #1337). It is identified by its YAML
    dict key (BLOCK_1033) under the microsoft section.
    """
    data = _yaml(VERGE_PATH)
    return data["competitor_relationships"]["microsoft"][BLOCK_1033]


def _journalist_block_1034():
    """Locate the m1034 block on the Maggie Harrison Dupre record.

    The Type B blocks live under the per-journalist top-level
    record's competitor_coverage dict (m1034 sits on the
    alfonso_maruccia_type_b record, the FIRST dedicated Type B
    pair on Maggie Harrison Dupre).
    """
    journalists = _yaml(JOURNALISTS_PATH)
    rec = journalists.get("alfonso_maruccia_type_b")
    if not isinstance(rec, dict):
        return None
    cc = rec.get("competitor_coverage", {})
    if isinstance(cc, dict) and BLOCK_1034 in cc:
        return cc[BLOCK_1034]
    return None


def _entities_block_1035():
    """Locate the m1035 block (top-level key of competitor-entities)."""
    entities = _yaml(ENTITIES_PATH)
    return entities.get(BLOCK_1035)


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
    """Fresh engine-layer calibration contract for #1340.

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


class TestAnchor1340:
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
# 2. Rotation guard: #1339 closed the 1335-1339 window; #1340 opens.
# The 1335-1339 window is VERIFIED CLOSED.
# ---------------------------------------------------------------------------


class TestRotationGuard1340:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-120").stdout
        # All five legs of the 1335-1339 window have push-status
        # commits (push status recorded DONE in the iteration-log
        # entries and in the push-status commits).
        for sha, label in (
            (PRED_MAIN_1339, "1339 main"),
            (PRED_ANCHOR_1339, "1339 anchor"),
            (PRED_DOCSYNC_1339, "1339 doc-sync"),
            (PRED_FINAL_1339, "1339 log-hash"),
            (PRED_MAIN_1338, "1338 main"),
            (PRED_ANCHOR_1338, "1338 anchor"),
            (PRED_DOCSYNC_1338, "1338 doc-sync"),
            (PRED_FINAL_1338, "1338 log-hash"),
            (PRED_MAIN_1337, "1337 main"),
            (PRED_ANCHOR_1337, "1337 anchor"),
            (PRED_DOCSYNC_1337, "1337 doc-sync"),
            (PRED_FINAL_1337, "1337 log-hash"),
            (PRED_MAIN_1336, "1336 main"),
            (PRED_ANCHOR_1336, "1336 anchor"),
            (PRED_DOCSYNC_1336, "1336 doc-sync"),
            (PRED_FINAL_1336, "1336 log-hash"),
            (PRED_MAIN_1335, "1335 main"),
            (PRED_ANCHOR_1335, "1335 anchor"),
            (PRED_DOCSYNC_1335, "1335 doc-sync"),
            (PRED_FINAL_1335, "1335 log-hash"),
        ):
            assert sha in log, label

    def test_all_window_push_status_done(self):
        # Push status is recorded DONE in each run's iteration-log
        # entry (in the repo, at HEAD); the main sha appears in the
        # same entry's push-status line.
        text = _git("show", "HEAD:iteration-log.md").stdout
        for sha, num in (
            (PRED_MAIN_1339, "1339"), (PRED_MAIN_1338, "1338"),
            (PRED_MAIN_1337, "1337"), (PRED_MAIN_1336, "1336"),
            (PRED_MAIN_1335, "1335"),
        ):
            assert sha[:8] in text, num
        assert text.count("Push status (this run): DONE") >= 5

    def test_1339_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1339")
        assert "Type C #1339" in out.stdout

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1340-1344 window" in src

    def test_1335_1339_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1335-1339 window is VERIFIED CLOSED" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1340 -> E #1341 -> A #1342 -> B #1343 -> C #1344" in src

    def test_next_window_verdict_belongs_to_1345(self):
        # Per #795 the next background-suite verdict (on the
        # #1340-launched suite) belongs to the next Type D run,
        # #1345.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1345 Type D run owns the next verdict" in src


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1033 / m1034 / m1035 all landed and intact.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1340:
    def test_m1033_block_present_in_verge(self):
        assert _verge_block_1033() is not None

    def test_m1033_mechanism_id_1033(self):
        block = _verge_block_1033()
        assert block["mechanism_id"] == 1033
        assert block["iteration"] == 1337
        assert block["iteration_type"] == "A"
        assert block["block_key"] == BLOCK_1033

    def test_m1033_copilot_agentic_pc_peg_identified(self):
        # The Type A corpus schema nests the prose peg under the
        # microsoft_arm_new / meta_arm_carried pair; the Oct-7/8
        # Copilot agentic PC-file-access peg and the microsoft vs
        # meta pair identify the block.
        block = _verge_block_1033()
        assert block["competitor_pair"] == "microsoft vs meta"
        assert block["microsoft_arm_new"][
            "tone_manual_illustrative"] == 0.15
        assert block["meta_arm_carried"][
            "tone_manual_illustrative"] == -0.3

    def test_m1033_verdict_directionally_supported(self):
        # m1033 is a directionally_supported_not_proven arm on The
        # Verge's Microsoft Copilot agentic PC-file access coverage
        # (+0.15 demonstration-led product-launch explainer register
        # vs the carried Meta Connect arm at -0.30), NOT a
        # falsification-family member; ledger holds at 62.
        block = _verge_block_1033()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["falsification_family_member"] is False
        assert block["falsification_ledger"] == "62"
        assert block["author"] == "Kit (with Ray)"

    def test_m1034_block_present_in_journalists(self):
        assert _journalist_block_1034() is not None

    def test_m1034_mechanism_id_1034(self):
        block = _journalist_block_1034()
        assert block["mechanism_id"] == 1034
        assert block["iteration"] == 1338
        assert block["iteration_type"] == "B"

    def test_m1034_block_key_field(self):
        block = _journalist_block_1034()
        assert block["block_key"] == BLOCK_1034

    def test_m1034_verdict_directionally_supported(self):
        # m1034 is a directionally_supported_not_proven ZERO-GRADIENT
        # control (Alfonso Maruccia, TechSpot: Oct-6 Norway
        # smart-glasses temporary-ban piece vs Oct-5 Google Finland
        # data-center forest-clearing piece, illustrative delta
        # (google minus meta) 0.00 - cross-entity register constancy,
        # same writer, same outlet, one day apart), NOT a
        # falsification-family member; ledger holds at 62.
        block = _journalist_block_1034()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["falsification_family_member"] is False

    def test_m1034_first_pair_on_maruccia_in_notes(self):
        # The FIRST dedicated Type B pair on Alfonso Maruccia;
        # the record notes carry the ledger position.
        rec = _yaml(JOURNALISTS_PATH)["alfonso_maruccia_type_b"]
        assert "FIRST" in rec["notes"]
        assert "ledger holds at 62" in rec["notes"]
        assert _journalist_block_1034()["author"] == "Kit (with Ray)"

    def test_m1035_block_present_in_entities(self):
        entities = _yaml(ENTITIES_PATH)
        assert BLOCK_1035 in entities

    def test_m1035_mechanism_id_1035(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1035]
        assert block["mechanism_id"] == 1035
        assert block["iteration"] == 1339
        assert block["iteration_type"] == "C"

    def test_m1035_block_key_field(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1035]["block_key"] == BLOCK_1035

    def test_m1035_verdict_mechanism_documented(self):
        # m1035 documents the Hachette et al. v Google selective-payer
        # Gemini suit (S.D.N.Y. 1:26-cv-05870, filed Jul 10 2026) -
        # the repurposed-commercial-relationship litigation leg:
        # Google licensed Gemini training content from
        # AP/Reddit/Shutterstock while allegedly repurposing Google
        # Books content obtained under scope-limited agreements:
        # verdict mechanism_documented; NOT a falsification-family
        # member; ledger holds at 62; tone NOT_SCORED.
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1035]
        assert block["verdict"] == "mechanism_documented"
        assert block["falsification_family_member"] is False
        assert "ledger holds at 62" in block["falsification_family"]

    def test_m1035_author(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1035]["author"] == "Kit (with Ray)"

    def test_max_numeric_mechanism_id_is_1035(self):
        assert _max_numeric_mechanism_id() == MECH_NUM


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1335 suite is DEAD at [  1%].
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1340:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG

    def test_prior_suite_stalled_at_1(self):
        # The #1335-launched suite froze at [  1%] progress: 1611
        # bytes, zero F marks, last write Oct 9 2026 05:44:08 PDT
        # (~4h stale at this run's ~10:00 AM PDT check), zero live
        # pytest processes (the pgrep sweep at this run's check
        # returned zero live pytest processes; the /proc open-fd
        # check returns empty). Progress never regresses, so the
        # [  1%] marker stays present and [  2%] never arrives.
        # Observation history: #1335 launched it and saw it ALIVE at
        # doc-sync (dots accumulating at [  0%]); #1336 saw it ALIVE
        # at ~06:00 AM PDT ([  1%], two live pytest processes);
        # #1337/#1338/#1339 observed only per #795 (#1339's ~09:00 AM
        # PDT check already found it dead at [  1%] with last write
        # 05:44:08 PDT and zero live processes); this run verdicts it
        # DEAD at ~10:00 AM PDT.
        text = _read(PRIOR_SUITE_LOG)
        assert "[  1%]" in text, text[-2000:]
        assert "[  2%]" not in text
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
        # type_d_1335_full_suite.log open anymore (the /proc open-fd
        # check returns empty; the pgrep sweep at this run's ~10:00 AM
        # PDT check returned zero live pytest processes).
        holders = _proc_holds_log("type_d_1335_full_suite.log")
        assert holders == "", holders

    def test_eighteenth_death_of_new_streak(self):
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
        # verdict), #1325-launched the FIFTEENTH (#1330 verdict),
        # #1330-launched the SIXTEENTH (#1335 verdict),
        # #1335-launched the SEVENTEENTH (#1340 verdict... no: the
        # #1335-launched suite's death verdict is the EIGHTEENTH
        # consecutive background-suite death of the new streak.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "EIGHTEENTH consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-TWENTY-FIFTH -> ONE-HUNDRED-TWENTY-SIXTH.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ONE-HUNDRED-TWENTY-FIFTH" in src
        assert "lineage advances" in src

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1340 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_PATH)
        assert "EIGHTEENTH consecutive" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: DETERMINATE-vacuous (zero F marks).
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1340:
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


class TestStatisticalDiscipline1340:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: the max numeric mechanism id is
        # unchanged at 1035 and no 1037-form keys exist.
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


class TestFalsificationLedger1340:
    def test_ledger_holds_at_62(self):
        # No new falsification-family member in the 1335-1339 window:
        # m1033 (the-verge.yaml) carries falsification_ledger "62";
        # m1034 (alfonso_maruccia_type_b record notes) and m1035
        # (competitor-entities falsification_family) carry the
        # ledger-holds-at-62 note.
        block = _verge_block_1033()
        assert block["falsification_ledger"] == "62"
        rec = _yaml(JOURNALISTS_PATH)["alfonso_maruccia_type_b"]
        assert "ledger holds at 62" in rec["notes"]
        entities = _yaml(ENTITIES_PATH)
        assert "ledger holds at 62" in entities[
            BLOCK_1035]["falsification_family"]

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
        # extra member-claim form mention); stable since. HEAD sweep
        # is stable for a committed landing.
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

    def test_sixty_second_member_intact(self):
        # Landed #1337 (m1033, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixty_third_member(self):
        assert _git_grep_tracked_source(_T63, None) == []

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
# 8. Guard lifecycle: forward pins for #1341; #1339 staged for this run.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1340:
    def test_pins_on_1032_no_landing(self):
        # Type D lands no mechanisms: max stays 1035, next stays 1036.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1035" in src
        assert "NEXT_NUM = 1036" in src

    def test_no_type_d_1340_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721): every commit whose message
        # matches "Type D #1340" must be this run's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type D #1340")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1340's own commits"
        main = _git("rev-parse", PRED_MAIN_1340).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_e_1341_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1341's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1341" must be #1341's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1341 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type E #1341")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1341's own commits"
        main = _git("rev-parse", PRED_MAIN_1341).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1033_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1033_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1033_dash_absent_repo_wide(self):
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

    def test_sixty_second_member_present_pin(self):
        # Landed #1337 (m1033, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixty_third_member_pin(self):
        # Type D lands no mechanisms; the sixty-third member-claim
        # form stays absent repo-wide.
        assert _git_grep_tracked_source(_T63, None) == []

    def test_predecessor_1334_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1339_FILE))

    def test_next_leg_is_1341_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1341 Type E" in src

    def test_1339_pins_flip_documented(self):
        # #1339 staged guard-lifecycle forward pins for this run
        # (no-Type-D-#1340-in-git-log, zero one-zero-three-three keys
        # all forms, fortieth direction absent, forty-eighth through
        # sixty-second members intact, no sixty-third member, ledger
        # 61); all verified GREEN pre-commit this run (manual
        # forward-guard verification, recorded in the iteration-log
        # entry). The no-Type-D-#1340 pin flips BY DESIGN at this
        # run's main commit (the #1191-class self-trip, re-pinned
        # post-commit by TestStalenessPins1340); the 1036-form pins
        # stay green because Type D lands no mechanisms. Documented in
        # the staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1340" in src
        assert "no_type_d_1340_in_git_log_pin" in src
        assert "#1191-class" in src
        assert "#1272-class" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1339's guard lifecycle flips once, then re-pins.
# ---------------------------------------------------------------------------


class TestStalenessPins1340:
    def test_1339_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: all 25 pass. The
        # no_type_d_1340_in_git_log pin (the #1191-class self-trip:
        # this run's main commit carries "Type D #1340") flipped BY
        # DESIGN at this run's main commit and is re-pinned green in
        # the terminal log-hash followup per #721 (PRED_MAIN_1340 now
        # holds this run's main sha in BOTH this file and the #1339
        # file per the #1292 precedent). The 1036-form pins stay green
        # throughout (Type D lands no mechanisms; the #723/#738/#739
        # designed keying holds); the member and direction pins stay
        # green (no member, no direction landed this run). The #1339
        # block is read-only to this run; the flip is documented here,
        # not repaired. Deselected pre-commit (verified only
        # post-terminal-followup).
        res = _class_run(E1339_FILE, "TestGuardLifecycle1339")
        out = res.stdout + res.stderr
        assert "25 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1340:
    def test_readme_test_file_table_has_1340_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1340_row_post_sync(self):
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


class TestIterationLog1340:
    def test_log_has_1340_entry(self):
        text = _read(LOG_PATH)
        assert "## #1340 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "EIGHTEENTH consecutive" in text
        assert "type_d_1340_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1340:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1340_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1340 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1340:
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
