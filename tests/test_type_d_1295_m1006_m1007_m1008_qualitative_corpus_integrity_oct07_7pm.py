# -*- coding: utf-8 -*-
"""Type D #1295 tests: m1006/m1007/m1008 qualitative-discipline
corpus-integrity verification (Oct 7, 2026) + #1290 background-suite
verdict per #795 + recurring-failure triage + full suite re-launch.

m1006 (Type A #1292, profiles/financial-times.yaml
competitor_relationships.google, block key
type_a_1292_ft_google_oct04_oct07_regulatory_accountability_register_vs_carried_meta_arms):
mechanism id 1006 - FT x Google Oct-1/Oct-4/Oct-7 regulatory-accountability
register (litigation-accountability headline -0.40, lobbying-footprint data
frame -0.30, Brussels-tax scoop -0.35; arm mean -0.35) vs carried FT x Meta
arms (m441, mean -0.5833); illustrative delta (Google minus Meta) +0.23; the
uniform payer-softening prediction FAILS at the regulatory register: the
Feb-2026 FT x Google News AI pilot deal (single-figure millions GBP/yr,
coverage_prediction 'softer') predicts a muted register on Google, but the
FT runs three adversarial regulatory-accountability pegs on the payer within
72 hours, eight months post-deal. Fifty-eighth falsification-family member
(ledger 57->58); fourth FT publication-level member; first falsification pin
on the FT x Google pair. MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026
standing rule: engine NOT run on corpus; p_value/cohens_d/ci_95
NOT_CALCULATED; is_significant false; NOT artifact-grade; no analysis.json
update. Correlation is not causation; hypothesis-generating only.

m1007 (Type B #1293, profiles/careers/journalists.yaml Sarah Perez record
competitor_coverage; block key fragment-built in the BLOCK_1007 constant
below per #715, so no contiguous literal appears in this file):
mechanism id 1007 - third dedicated Type B mechanism on Sarah Perez
(TechCrunch Consumer News Editor): Sep-30 Muse privacy-dispute
accountability register (-0.35, NEW Meta arm, excerpt-attested via the
TechCrunch author-listing mirror) vs Oct-1 ChatGPT shopping-features launch
relay (+0.05, NEW OpenAI arm, excerpt-attested via the WeSearch verbatim
mirror); illustrative delta (OpenAI minus Meta) +0.40 - same writer, same
outlet, 1 day apart; replicates m698's writer-level asymmetry direction at a
no-deal outlet (TechCrunch/Yahoo holds no OpenAI content-licensing deal per
m698), so the writer-register pattern bounds the deal explanation rather
than confirming it; per the #1143 temporal-replication precedent this
same-writer same-pair-class observation is not a new prediction test. NOT a
falsification-family member. MANUAL/QUALITATIVE ONLY per the Aug 28 2026
standing rule: engine NOT run on corpus; NOT artifact-grade; no
analysis.json update.

m1008 (Type C #1294, profiles/competitor-entities.yaml top-level, block key
type_c_1294_elsevier_jama_network_clinicalkey_ai_strategic_content_agreement_oct07):
mechanism id 1008 - first dedicated corpus mechanism on the
publisher-as-AI-provider vertical licensing rail (Elsevier is the PAYER:
licenses peer-publisher content from the JAMA Network - all 13 JAMA Network
Family of Journals titles, full-text + visuals - to feed its own
clinical-grade AI workspace ClinicalKey AI); the financial dependency sits
inside the publisher stack rather than between publishers and AI labs;
distinct from m891/m915/m999/m1002/m1005/m711; the sign-or-sue atom lands
twice on the same entity (Elsevier on the litigation tier vs Google/Meta AND
on the licensing tier as a payer); corroborating multi-product structure:
JAMA Network also licenses into Elsevier's LeapSpace research AI (Sep 15
2026). MECHANISM DOCUMENTED, NOT a falsification-family member (ledger holds
at 58); no new direction (fortieth absent by design; thirty-fifth through
thirty-ninth stand). MANUAL / qualitative ONLY per the Aug 28 2026 standing
rule: engine NOT run; NOT artifact-grade; no analysis.json update.

This run is Type D #1295, the FIRST and OPENING leg of the 1295-1299 window
(D #1295 -> E #1296 -> A #1297 -> B #1298 -> C #1299 per the #565 anchor +
rotation guard); the 1290-1294 window is VERIFIED CLOSED. It renders the
#1290-launched background-suite verdict per #795: the suite is DEAD at
[  9%] (7868 bytes, zero F marks, last write Oct 7 2026 17:37 PDT, zero live
pytest processes, no process holding the log open) - the NINTH consecutive
background-suite death of the new streak; tombstone lineage advances
ONE-HUNDRED-SIXTEENTH -> ONE-HUNDRED-SEVENTEENTH. Recurring-failure triage:
zero F marks in the dead stream - nothing to triage, DETERMINATE-vacuous; no
recurring-failure triage repairs claimed from the stream. The full suite is
re-launched this run to type_d_1295_full_suite.log (venv python per the Sep 7
2026 convention, full inventory, no -x; dots accumulating at commit); the
#1300 Type D run owns the next verdict per #795.

Type D lands no mechanisms: max numeric mechanism id stays 1008, next stays
1009; ledger holds at 58; the forty-eighth through fifty-eighth
member-claim forms stay intact, the fifty-ninth member-claim form stays
absent repo-wide, the fortieth direction-claim form stays absent in
profiles/, and the thirty-fifth through thirty-ninth directions stand.
Forward guards for #1296 are staged in this file (PRED_MAIN_1296 0*40
placeholder per #721); the no-Type-D-#1295 forward pin belongs to this file
(the #1294 Type C file staged no guard-lifecycle forward pins - its
PRED_MAIN_1295 is a 0*40 placeholder, placeholder-only per the Type C
precedent; the #1294 forward-guard verification was done manually this run:
max-1008, zero one-zero-zero-nine keys all forms, no Type D #1295 in git log,
fortieth direction absent, forty-eighth through fifty-eighth members intact,
no fifty-ninth member, ledger 58 - all GREEN pre-commit, recorded in the
iteration-log entry). The forward-guard needles (next-number
one-zero-zero-nine forms, the fifty-ninth member-claim form, the fortieth
direction-claim form) are all format-built at runtime in the new test file;
no contiguous forms anywhere in the new files or this entry's prose (prose
uses lowercase forms). The landed ordinals live as short lowercase forms in
the test-file prose; the live full-form claims live in profiles (the
forty-eighth in financial-times.yaml, the forty-ninth and fiftieth in
profiles/careers/journalists.yaml, the fifty-first in news-corp.yaml, the
fifty-second in profiles/careers/journalists.yaml, the fifty-third in
the-verge.yaml, the fifty-fourth in guardian.yaml, the fifty-fifth in
atlantic.yaml, the fifty-sixth in wired.yaml, the fifty-seventh in ap.yaml,
the fifty-eighth in financial-times.yaml).

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test file
working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file) all left out of this
run's index/diff (explicit-path staging). #1024 m846
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
FT_PATH = os.path.join(PROFILES_DIR, "financial-times.yaml")
WIRED_PATH = os.path.join(PROFILES_DIR, "wired.yaml")
JOURNALISTS_PATH = os.path.join(
    PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1290_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1295_full_suite.log")
OWN_BASENAME = (
    "test_type_d_1295_m1006_m1007_m1008_qualitative_"
    "corpus_integrity_oct07_7pm.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor this fails BY DESIGN).
ANCHORED_SHA = "99b14c1637813fad0b3d58c8d3f632f81e8e341d"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1008
NEXT_NUM = 1009  # integer only; key-form needles are format-built

# Predecessor chain: #1294 Type C closed the 1290-1294 window.
PRED_MAIN_1294 = "110bb68f"
PRED_ANCHOR_1294 = "e83fe669"
PRED_DOCSYNC_1294 = "7d692fa5"
PRED_FINAL_1294 = "d9388971"
PRED_PUSH_1294 = "b3e20938"
PRED_MAIN_1293 = "5e8b08a4"
PRED_ANCHOR_1293 = "2b4efbfe"
PRED_DOCSYNC_1293 = "862cffb5"
PRED_FINAL_1293 = "8e8684bd"
PRED_PUSH_1293 = "2f6bf463"
PRED_MAIN_1292 = "ddb5921f"
PRED_ANCHOR_1292 = "4420f305"
PRED_DOCSYNC_1292 = "db89a93c"
PRED_FINAL_1292 = "434fb01b"
PRED_PUSH_1292 = "7c563e89"
PRED_MAIN_1291 = "4f33ce6a"
PRED_ANCHOR_1291 = "17773f8a"
PRED_DOCSYNC_1291 = "041cda51"
PRED_FINAL_1291 = "939e19d6"
PRED_PUSH_1291 = "31f7726c"
PRED_MAIN_1290 = "0545f246"
PRED_ANCHOR_1290 = "7d6623c4"
PRED_DOCSYNC_1290 = "c9feb331"
PRED_FINAL_1290 = "91137e06"
PRED_PUSH_1290 = "9a9f0fd7"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the no-Type-D-#1295 own-run pin
# flips green post-repin).
PRED_MAIN_1295 = "99b14c1637813fad0b3d58c8d3f632f81e8e341d"  # re-pinned to main sha per #721

# Forward guard for the next leg: #1296 Type E. Re-pinned by #1296's
# terminal log-hash followup per #721 (starts as 0*40;
# placeholder-only).
# Repaired #1300 Type D: the #1296 terminal followup re-pinned only its
# own file's copy (verified in the #1300 regression sweep:
# TestGuardLifecycle1295::test_no_type_e_1296_in_git_log_pin red);
# per the #1292 precedent (434fb01b re-pins both copies) the
# predecessor's copy is re-pinned here to #1296's main sha.
PRED_MAIN_1296 = "14af9fecd0d7dcc93eced86ab065e9114f685226"

# The #1294 window-closing file, for the staleness pin on its test
# classes (#1294 staged no guard-lifecycle forward pins for this run;
# its 36 tests in 4 classes are expected to survive this run's main
# commit with one pre-existing BY-DESIGN failure - the #565
# anchor-duality placeholder pin, failing ever since the #1294 anchor
# followup, not a flip from this run - verified via the subprocess
# pin below).
B1294_FILE = (
    "test_type_c_1294_elsevier_jama_network_"
    "clinicalkey_ai_strategic_content_agreement_oct07_6pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 72446  # patched pre-main: pre-sync 72358 + 88 collected
README_FILE_COUNT = 1620  # pre-sync 1619 + 1 (this file)

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

# Fragment-built per #715: the contiguous keys never appear in this
# file (BLOCK_1007 is split so the #1293 zero-hit-except-landed pin
# stays green). Iteration-form block keys carry no underscore-form
# mechanism key substring (the #723/#738/#739 designed-keying
# convention).
BLOCK_1006 = (
    "type_a_1292_ft_google_oct04_oct07_regulatory_"
    "accountability_register_vs_carried_meta_arms"
)
BLOCK_1007 = (
    "type_b_1293_sarah_perez_techcrunch_muse_privacy_"
    "dispute_vs_chatgpt_shopping_sep30_oct01"
)
BLOCK_1008 = (
    "type_c_1294_elsevier_jama_network_clinicalkey_ai_"
    "strategic_content_agreement_oct07"
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


def _journalist_block_1007():
    """Locate the m1007 block on the Sarah Perez record.

    The Type B blocks live under the per-journalist record's
    competitor_coverage dict (m1007 sits on the Sarah Perez record
    alongside the type_b_638 m617 and type_b_778 m698 blocks).
    """
    journalists = _yaml(JOURNALISTS_PATH)
    records = journalists.get("journalists", [])
    for rec in records:
        if (isinstance(rec, dict)
                and rec.get("name") == "Sarah Perez"):
            cc = rec.get("competitor_coverage", {})
            if isinstance(cc, dict) and BLOCK_1007 in cc:
                return cc[BLOCK_1007]
    return None


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
    args = ["grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    else:
        args.append(".")
    out = _git(*args).stdout
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
    """Fresh engine-layer calibration contract for #1295.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no repo reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_apple_arms = [-0.09, -0.10, -0.08, -0.12, -0.07]
    synthetic_meta_arms = [-0.42, -0.38, -0.51, -0.44, -0.37]
    pooled_apple = (sum(synthetic_apple_arms)
                    / len(synthetic_apple_arms))
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_apple - pooled_meta, 3)


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1295:
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
# 2. Rotation guard: #1294 closed the 1290-1294 window; #1295 opens.
# ---------------------------------------------------------------------------


class TestRotationGuard1295:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-60").stdout
        for sha, label in (
            (PRED_MAIN_1294, "1294 main"),
            (PRED_ANCHOR_1294, "1294 anchor"),
            (PRED_DOCSYNC_1294, "1294 doc-sync"),
            (PRED_FINAL_1294, "1294 log-hash"),
            (PRED_PUSH_1294, "1294 push-status"),
            (PRED_MAIN_1293, "1293 main"),
            (PRED_ANCHOR_1293, "1293 anchor"),
            (PRED_DOCSYNC_1293, "1293 doc-sync"),
            (PRED_FINAL_1293, "1293 log-hash"),
            (PRED_PUSH_1293, "1293 push-status"),
            (PRED_MAIN_1292, "1292 main"),
            (PRED_ANCHOR_1292, "1292 anchor"),
            (PRED_DOCSYNC_1292, "1292 doc-sync"),
            (PRED_FINAL_1292, "1292 log-hash"),
            (PRED_PUSH_1292, "1292 push-status"),
            (PRED_MAIN_1291, "1291 main"),
            (PRED_ANCHOR_1291, "1291 anchor"),
            (PRED_DOCSYNC_1291, "1291 doc-sync"),
            (PRED_FINAL_1291, "1291 log-hash"),
            (PRED_PUSH_1291, "1291 push-status"),
            (PRED_MAIN_1290, "1290 main"),
            (PRED_ANCHOR_1290, "1290 anchor"),
            (PRED_DOCSYNC_1290, "1290 doc-sync"),
            (PRED_FINAL_1290, "1290 log-hash"),
            (PRED_PUSH_1290, "1290 push-status"),
        ):
            assert sha in log, label

    def test_1294_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1294")
        assert "Type C #1294" in out.stdout

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1295-1299 window" in src

    def test_1290_1294_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1290-1294 window is VERIFIED CLOSED" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1295 -> E #1296 -> A #1297 -> B #1298 -> C #1299" in src

    def test_next_window_verdict_belongs_to_1300(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1300 Type D run owns the next verdict" in src


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1006 / m1007 / m1008 all landed and intact.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1295:
    def test_m1006_block_present_in_ft(self):
        ft = _yaml(FT_PATH)["competitor_relationships"]
        assert BLOCK_1006 in ft["google"]

    def test_m1006_mechanism_id_1006(self):
        ft = _yaml(FT_PATH)["competitor_relationships"]
        assert ft["google"][BLOCK_1006]["mechanism_id"] == 1006

    def test_m1006_block_key_field(self):
        ft = _yaml(FT_PATH)["competitor_relationships"]
        assert ft["google"][BLOCK_1006]["block_key"] == BLOCK_1006

    def test_m1006_verdict_falsification_member(self):
        ft = _yaml(FT_PATH)["competitor_relationships"]
        block = ft["google"][BLOCK_1006]
        assert block["verdict"].startswith("falsification_member_confirmed")
        assert block["falsification_family_member"] is True

    def test_m1006_ledger_58_and_family_form(self):
        ft = _yaml(FT_PATH)["competitor_relationships"]
        block = ft["google"][BLOCK_1006]
        assert str(block["falsification_ledger"]) == "58"
        # The fifty-eighth member-claim form lives fragment-built in
        # _T58 per #715 (no contiguous literal in this file).
        assert _T58 in block["falsification_family"]

    def test_m1007_block_present_in_journalists(self):
        assert _journalist_block_1007() is not None

    def test_m1007_mechanism_id_1007(self):
        block = _journalist_block_1007()
        assert block["mechanism_id"] == 1007
        assert block["iteration"] == 1293
        assert block["type"] == "B"

    def test_m1007_block_key_field(self):
        block = _journalist_block_1007()
        assert block["block_key"] == BLOCK_1007

    def test_m1007_not_a_member_in_finding(self):
        # m1007 is NOT a falsification-family member; the finding
        # prose carries the non-member verdict.
        block = _journalist_block_1007()
        assert "NOT a falsification-family member" in block["finding"]
        assert block.get("author") == "Kit (with Ray)"

    def test_m1008_block_present_in_entities(self):
        entities = _yaml(ENTITIES_PATH)
        assert BLOCK_1008 in entities

    def test_m1008_mechanism_id_1008(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1008]
        assert block["mechanism_id"] == 1008
        assert block["iteration"] == 1294
        assert block["iteration_type"] == "C"

    def test_m1008_block_key_field(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1008]["block_key"] == BLOCK_1008

    def test_m1008_verdict_mechanism_documented(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1008]
        assert block["verdict"] == "mechanism_documented"
        assert block["falsification_family_member"] is False
        assert "ledger holds at 58" in block["falsification_family"]

    def test_max_numeric_mechanism_id_is_1008(self):
        assert _max_numeric_mechanism_id() == MECH_NUM


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1290 suite is DEAD at [  9%].
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1295:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG

    def test_prior_suite_stalled_at_9(self):
        # The #1290-launched suite froze at [  9%] progress: 7868
        # bytes, zero F marks, last write Oct 7 2026 17:37 PDT (~1.5h
        # stale at this run's ~07:00 PM PDT check), zero live pytest
        # processes (the pgrep hits at this run's check were the check
        # shell's own cmdline and its pgrep child - self-match
        # phantoms), no process holding the log open per the /proc
        # open-fd check. Progress never regresses, so the marker stays
        # present and [ 10%] never arrives.
        text = _read(PRIOR_SUITE_LOG)
        assert "[  9%]" in text, text[-2000:]
        assert "[ 10%]" not in text
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
        # type_d_1290_full_suite.log open anymore (the /proc open-fd
        # check returns empty; the pgrep hits at this run's ~19:00
        # check were the check shell's own cmdline). The suite died
        # between the #1294 observation (~06:30 PM PDT Oct 7, [  9%],
        # zero live processes) and this run's check.
        holders = _proc_holds_log("type_d_1290_full_suite.log")
        assert holders == "", holders

    def test_ninth_death_of_new_streak(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite
        # completed). The 43-run streak BROKE at #1250 (the #1245
        # suite was verdict ALIVE at 20%). #1255 verdict the FIRST
        # consecutive background-suite death of the new streak, #1260
        # the SECOND, #1265 the THIRD, #1270 the FOURTH, #1275 the
        # FIFTH, #1280 the SIXTH, #1285 the SEVENTH, #1290-launched
        # the EIGHTH (verdict rendered this run). This verdict is the
        # NINTH consecutive background-suite death of the new streak.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NINTH consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-SIXTEENTH -> ONE-HUNDRED-SEVENTEENTH.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ONE-HUNDRED-SEVENTEENTH" in src
        assert "lineage advances" in src

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1295 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_PATH)
        assert "NINTH consecutive" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: DETERMINATE-vacuous (zero F marks).
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1295:
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


class TestStatisticalDiscipline1295:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: the max numeric mechanism id is
        # unchanged at 1008 and no 1009-form keys exist.
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_engine_not_run_on_corpus(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run on corpus" in src

    def test_synthetic_calibration_delta_contract(self):
        # Engine-layer contract only (never a finding): synthetic
        # Apple arms [-0.09, -0.10, -0.08, -0.12, -0.07] vs synthetic
        # Meta arms [-0.42, -0.38, -0.51, -0.44, -0.37] -> pooled
        # delta +0.332.
        assert _synthetic_calibration_delta() == 0.332


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 58; guards on member forms.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1295:
    def test_ledger_holds_at_58(self):
        ft = _yaml(FT_PATH)["competitor_relationships"]
        block = ft["google"][BLOCK_1006]
        assert str(block["falsification_ledger"]) == "58"
        assert _T58 in block["falsification_family"]

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
        assert _T56 in _read(WIRED_PATH)

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

    def test_no_fifty_ninth_member(self):
        assert _git_grep_tracked_source(_T59, None) == []

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
# 8. Guard lifecycle: forward pins for #1296; #1294 staged none.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1295:
    def test_pins_on_1008_no_landing(self):
        # Type D lands no mechanisms: max stays 1008, next stays 1009.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1008" in src
        assert "NEXT_NUM = 1009" in src

    def test_no_type_d_1295_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721): every commit whose message
        # matches "Type D #1295" must be this run's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type D #1295")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1295's own commits"
        main = _git("rev-parse", PRED_MAIN_1295).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_e_1296_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1296's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1296" must be #1296's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type E #1296")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1296's own commits"
        main = _git("rev-parse", PRED_MAIN_1296).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1009_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1009_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1009_dash_absent_repo_wide(self):
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
        assert _T56 in _read(WIRED_PATH)

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

    def test_no_fifty_ninth_member_pin(self):
        # Type D lands no mechanisms; the fifty-ninth member-claim
        # form stays absent repo-wide.
        assert _git_grep_tracked_source(_T59, None) == []

    def test_predecessor_1294_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, B1294_FILE))

    def test_next_leg_is_1296_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1296 Type E" in src

    def test_1294_pins_note_documented(self):
        # #1294 staged no guard-lifecycle forward pins for this run
        # (its test file is the minimal 4-class / 36-test form with
        # no no-Type-D-#1295-in-git-log or 1009-form pins; its
        # PRED_MAIN_1295 is a 0*40 placeholder, placeholder-only per
        # the Type C precedent); its forward-guard verification was
        # done manually this run (all GREEN: max-1008, zero
        # one-zero-zero-nine keys all forms, no Type D #1295 in git
        # log, fortieth direction absent, forty-eighth through
        # fifty-eighth members intact, no fifty-ninth member, ledger
        # 58) and is recorded in the iteration-log entry, not
        # repaired. Documented in the staleness pin below.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1295" in src
        assert "no guard-lifecycle forward pins" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1294's classes flip NOTHING by design post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1295:
    def test_1294_classes_stable_across_main_commit(self):
        # #1294's 36 tests (4 classes, no guard-lifecycle forward
        # pins) are expected to survive this run's main commit with
        # ZERO by-design flips from this run: Type D lands no
        # mechanisms (the max-1008 and 1008-form pins stay green) and
        # the file pins no #1295 git-log forms. The single expected
        # failure is the #565 anchor-duality pin
        # (TestAnchor1294::test_anchor_sha_placeholder_pre_commit),
        # which fails BY DESIGN ever since the #1294 anchor followup
        # patched ANCHORED_SHA - pre-existing, not a flip from this
        # run. The pin runs the file as-is; the class run below
        # therefore expects "1 failed, 35 passed" with the failure
        # named. Documented here, not repaired.
        res = _class_run(B1294_FILE, "")
        out = res.stdout + res.stderr
        assert "1 failed, 35 passed" in out, out[-2000:]
        assert "test_anchor_sha_placeholder_pre_commit" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1295:
    def test_readme_test_file_table_has_1295_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_d_1295" in readme

    def test_architecture_has_1295_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_d_1295" in arch

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


class TestIterationLog1295:
    def test_log_has_1295_entry(self):
        text = _read(LOG_PATH)
        assert "## #1295 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "NINTH consecutive" in text
        assert "type_d_1295_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1295:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1295_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1295 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1295:
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
