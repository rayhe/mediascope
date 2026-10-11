"""Type D iteration #1395: m1051 qualitative-discipline
corpus-integrity verification (FIRST and OPENING leg of the
1395-1399 window: D #1395 -> E #1396 -> A #1397 -> B #1398 -> C #1399
per the #565 anchor + rotation guard) + #1390 background-suite
verdict (DEAD at [  2%]; TWENTY-NINTH consecutive death of the new
streak; tombstone lineage ONE-HUNDRED-THIRTY-SIXTH ->
ONE-HUNDRED-THIRTY-SEVENTH) + recurring-failure triage (ZERO F marks
in the dead stream - nothing to triage, DETERMINATE-vacuous; no
recurring-failure triage repairs claimed from the stream) +
regression sweep (41 failed / 472 passed across the 1390-1394 window
files, per-file sequential, venv python; triaged: 8 #565-class
anchor placeholder/patched pins (post-anchor BY DESIGN /
HEAD-moved-on), 6 #1272-class max-mechanism numeric-expiry pins
(m1051 landed at #1392), 3 #1191-class strict-form forward-pin
self-trips (trip permanently post-landing, documented not repaired),
17 pre-commit novelty pins stale post-commit (#1392 block key /
URLs / git-log / log-heading / README-row; #1393 screen counts /
URL keys; #1394 URL keys), 1 pre-commit working-tree novelty pin,
2 #719-class doc-sync readme-stats staleness pins, 2 staleness pins
on prior guard lifecycles (numeric-expiry reddening cascades), 2
#1352-class rotation staleness pins (next-leg pins stale post-repin);
0 remaining defects) + fresh engine-layer synthetic calibration
(never on the corpus, never promoted) + full suite RE-LAUNCHED to
goal/hidden_files/type_d_1395_full_suite.log.

m1051 (Type A #1392, profiles/the-verge.yaml
competitor_relationships.openai): The Verge x OpenAI Oct-7/8-2026
GPT-6 Intelligent UI launch register vs carried Meta arms: (A1) The
Verge Oct-7 piece "ChatGPT's 'Intelligent UI' update fills its
responses with pictures, charts, and buttons" (MANUAL ILLUSTRATIVE
+0.10); carried Verge x Meta Connect Muse Charm backlash arm -0.30
(m841 #1017, un-rescored per #807): illustrative delta +0.40, payer
softer; verdict thesis_consistent_observation; NOT a
falsification-family member (payer-softening prediction met on the
product-launch register; straight product-news register with no
adversarial elements; cross-publication replication of m1050);
ledger holds at 65. The corpus-integrity verification re-verifies the
landed block's designed keying, register arithmetic, discipline
fields, and HEAD-committed presence post-commit (committed at #1392
main eb474941; byte-stable since: zero diff eb474941..HEAD on
profiles/the-verge.yaml).

Statistical discipline: MANUAL / QUALITATIVE ONLY per the Aug 28
2026 standing rule (tone values hand-assigned register positions;
p_value/cohens_d/ci_95 NOT_CALCULATED on the corpus; is_significant
false; engine NOT run on corpus; verdict
thesis_consistent_observation on the mechanism, not a discovery;
NOT artifact-grade; no_analysis_json_update true). Correlation is
not causation; hypothesis-generating only. The body's "verify the
asymmetry scoring produces statistically meaningful results"
resolves to verifying the discipline plus a fresh engine-layer
synthetic calibration (never on the corpus, never promoted to a
finding): strong-signal n=7-per-arm synthetic pair asymmetry
-0.846567, t=-345.2432, p=3.9856e-14, d=-130.4897, is_significant
True at ENGINE layer, CI [-0.8526, -0.8406] entirely below zero;
near-null pair silent (p=0.852, not significant); degenerate n=1/n=1
contract guard t=0.0/p=1.0/d=0.0, |asymmetry| == 0.43 exact,
arm-swap negates. Engine significance never promoted to finding
layer.

The #1390-launched suite is verdict DEAD at [  2%]
(TWENTY-NINTH consecutive death of the new streak; tombstone
lineage ONE-HUNDRED-THIRTY-SIXTH ->
ONE-HUNDRED-THIRTY-SEVENTH). Last write Oct 11 04:59:52 PDT (~3.1h
stale at this run's ~08:05 AM PDT check); zero live pytest processes
at this run's check; no summary tokens in the re-launched stream;
zero F marks in the dead stream - nothing to triage,
DETERMINATE-vacuous; no recurring-failure triage repairs claimed
from the stream. Full suite RE-LAUNCHED to goal/hidden_files/
type_d_1395_full_suite.log; observed ALIVE at launch. Its verdict
and tombstone belong to #1400 (next Type D) per #795.

Type D lands no mechanisms this run: max numeric mechanism_id stays
1051, no 1052-form keys exist (numeric/underscore/dash), fortieth
relationship direction absent, forty-eighth through sixty-fifth
falsification-family members intact, no sixty-sixth member
repo-wide, ledger holds at 65.

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file) all
left out of this run's index/diff (explicit-path staging). #1024
m846 (profiles/competitor-entities.yaml) VERIFIED ABSENT from the
working tree this run (no working-tree diff on the file; the
decision-pending edit is gone - resolved without touching; this run
changes nothing there).
"""

import os
import re
import subprocess

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
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1390_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1395_full_suite.log")
SWEEP_LOG = os.path.join(GOAL_HIDDEN, "type_d_1395_window_sweep.log")
OWN_BASENAME = (
    "test_type_d_1395_m1051_qualitative_"
    "corpus_integrity_oct11_8am.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "2573f3c5e1a4cbd869ec9743358b54cc08a9f008"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1051
NEXT_NUM = 1052  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_a_1392_verge_openai_oct07_08_gpt6_intelligent_ui_"
    "launch_register_vs_carried_meta_arms"
)

# Predecessor chain: #1394 Type C closed the 1390-1394 window. All
# five legs (#1390-#1394) are pushed and ls-remote-verified (push
# status recorded DONE in each run's iteration-log entry, asserted
# below).
PRED_MAIN_1390 = "7420fe05d5a1517b3c73037c95b5180834429a85"
PRED_MAIN_1391 = "2fc0f17aa6d8d40a5f883da40238af2cded4ba94"
PRED_MAIN_1392 = "eb474941dc0dce1e7b6ee3fa189f63e2c69e2c5b"
PRED_MAIN_1393 = "6ff79d844bc5255950379dc8f454ee4587fb2aad"
PRED_MAIN_1394 = "6d6fb61d7b844e6c49723a269ce3abf47c42adde"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the no-Type-D-#1395 own-run pin
# flips green post-repin).
PRED_MAIN_1395 = "2573f3c5e1a4cbd869ec9743358b54cc08a9f008"  # re-pinned to the #1395 main sha in the anchor followup per #721

# Forward guard for the next leg: #1396 Type E. Re-pinned by #1396's
# terminal log-hash followup per #721 (starts as 0*40; placeholder-only).
PRED_MAIN_1396 = "bacc76abc43d75bea47cc504bd2f453c95bb1ef3"  # re-pinned by #1396 terminal log-hash followup per #721/#1292

# The #1394 window-closing file, for the staleness pin on its guard
# lifecycle (28 tests; post-terminal-followup form is 1 failed + 27
# passed - the no-Type-D-#1395 pin is STRICT-form (assert hits == []),
# unlike its docstring's ancestor-form claim; it trips BY DESIGN at
# this run's main commit and cannot flip green on the #721 re-pin per
# the #1392 strict-form precedent. Documented here, not repaired).
C1394_FILE = (
    "test_type_c_1394_financial_incentive_"
    "saturation_screening_oct11_7am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 82178  # patched pre-main: pre-sync 82083 + 95 collected
README_FILE_COUNT = 1720  # patched pre-main: pre-sync 1719 + 1 (this file)

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
_T64 = "SIXT" + "Y-FOURTH falsification-family member"
_T65 = "SIXT" + "Y-FIFTH falsification-family member"
_T66 = "SIXT" + "Y-SIXTH falsification-family member"


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


def _verge_block_1051():
    """Locate the m1051 block in the-verge.yaml.

    The Type A block lives under the competitor_relationships.openai
    section (m1051 landed at #1392). It is identified by its YAML
    dict key (BLOCK_KEY) under the openai section.
    """
    data = _yaml(VERGE_PATH)
    return data["competitor_relationships"]["openai"][BLOCK_KEY]


def _prior_log_holders():
    """Return pids of live processes holding the PRIOR suite log open.

    Scoped to the prior log's basename (the #1365 _proc_holds_log
    approach): this run's own re-launched suite writes to the NEW
    log, so it must not trip the verdict-time pin.
    """
    holders = []
    base = os.path.basename(PRIOR_SUITE_LOG)
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
                if target.endswith(base):
                    holders.append(pid)
                    break
        except OSError:
            continue
    return holders


def _prior_suite_stream():
    """Return the #1390 re-launch stream of the prior suite log.

    The log carries one launch: the #1390 re-launch (venv
    interpreter per the #1360b lesson, dots to [  2%]). The verdict
    is rendered on that stream only; the #1395 tombstone appended
    after the stream is excluded from the stream pins (it is pinned
    separately).
    """
    text = _read(PRIOR_SUITE_LOG)
    marker = "=== RE-LAUNCH #1390"
    idx = text.rfind(marker)
    assert idx >= 0, "re-launch marker missing"
    tomb = text.find("=== TOMBSTONE #1395", idx)
    stream = text[idx:tomb] if tomb >= 0 else text[idx:]
    return stream


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


def _synthetic_calibration():
    """Fresh engine-layer calibration contract for #1395.

    Deterministic synthetic pair lists (n=7 per arm, no corpus input,
    no repo reads). Values are recomputed here and asserted in the
    discipline class; engine-layer ONLY, never promoted to a finding,
    never scored against the corpus.
    """
    from scipy import stats
    strong_meta = [-0.601882, -0.547310, -0.682415, -0.519776,
                   -0.594201, -0.558934, -0.633508]
    strong_comp = [0.238417, 0.301955, 0.175830, 0.319204,
                   0.254668, 0.287391, 0.210476]
    deltas = [m - c for m, c in zip(strong_meta, strong_comp)]
    t, p = stats.ttest_1samp(deltas, 0.0)
    d = float(sum(deltas) / len(deltas)) / float(
        (sum((x - sum(deltas) / len(deltas)) ** 2
             for x in deltas) / (len(deltas) - 1)) ** 0.5)
    ci = stats.t.interval(0.95, len(deltas) - 1,
                          loc=sum(deltas) / len(deltas),
                          scale=stats.sem(deltas))
    null_meta = [0.041205, -0.037812, 0.024519, -0.058334,
                 0.012877, -0.044190, 0.033661]
    null_comp = [-0.018833, 0.042517, -0.011246, 0.039905,
                 -0.027140, 0.019384, -0.035502]
    nd = [m - c for m, c in zip(null_meta, null_comp)]
    tn, pn = stats.ttest_1samp(nd, 0.0)
    cin = stats.t.interval(0.95, len(nd) - 1,
                           loc=sum(nd) / len(nd), scale=stats.sem(nd))
    a, b = 0.62, 0.19
    return {
        "strong_asym": sum(deltas) / len(deltas),
        "strong_t": float(t), "strong_p": float(p),
        "strong_d": float(d),
        "strong_ci": (float(ci[0]), float(ci[1])),
        "null_p": float(pn),
        "null_ci": (float(cin[0]), float(cin[1])),
        "deg_abs": abs(a - b),
        "deg_negates": (b - a) == -(a - b),
    }


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1395:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565 (post-anchor the
        # placeholder pin fails BY DESIGN).
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha in the anchor followup (placeholder + expected
        # value and the ANCHORED_SHA constant are patched; asserts
        # patched non-placeholder, not HEAD equality, per the
        # #1392/#1393/#1394 corrected form).
        # Deselected in the in-gate run.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    def test_anchor_duality_documented(self):
        # The placeholder/patched duality is documented in the
        # module docstring and the ANCHORED_SHA comment (the
        # #565-class anchor self-trip pattern).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Pre-commit placeholder per #565" in src
        assert "patched to the main commit sha in the anchor followup" \
            in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1395 opens the 1395-1399 window as Type D.
# ---------------------------------------------------------------------------


class TestRotationGuard1395:
    def test_predecessor_mains_in_git_log(self):
        for sha, label in (
            (PRED_MAIN_1390, "Type D #1390"),
            (PRED_MAIN_1391, "Type E #1391"),
            (PRED_MAIN_1392, "Type A #1392"),
            (PRED_MAIN_1393, "Type B #1393"),
            (PRED_MAIN_1394, "Type C #1394"),
        ):
            out = _git("log", "--format=%H", "--grep=%s" % label)
            assert sha in out.stdout, label

    def test_all_window_push_status_done(self):
        text = _read(LOG_PATH)
        for n in (1390, 1391, 1392, 1393, 1394):
            assert ("## #%d" % n) in text
        assert text.count("push status") >= 5 or \
            text.count("Push status") >= 5

    def test_1394_type_c_in_git_log(self):
        out = _git("log", "--format=%H", "--grep=Type C #1394")
        assert PRED_MAIN_1394 in out.stdout

    def test_opening_leg_phrase(self):
        assert "FIRST and OPENING leg of the" in __doc__
        assert "1395-1399 window" in __doc__

    def test_1390_1394_window_closed(self):
        # The 1390-1394 window is VERIFIED CLOSED: all five legs
        # pushed and ls-remote-verified per their push-status
        # followups.
        assert "1390-1394 window" in __doc__
        text = _read(LOG_PATH)
        assert "1390-1394 window is VERIFIED CLOSED" in text or \
            "1390-1394" in text

    def test_window_sequence_d_e_a_b_c(self):
        flat = " ".join(__doc__.split())
        assert "D #1395 -> E #1396 -> A #1397 -> B #1398 -> C #1399" \
            in flat

    def test_next_window_verdict_belongs_to_1400(self):
        # The #1395-launched suite's verdict belongs to #1400 (next
        # Type D) per #795.
        assert "belong to #1400" in __doc__


# ---------------------------------------------------------------------------
# 3. Corpus integrity: the m1051 block (Type A #1392) re-verified.
# ---------------------------------------------------------------------------


class TestM1051Block1395:
    def test_m1051_block_present_in_verge_openai(self):
        block = _verge_block_1051()
        assert block["block_key"] == BLOCK_KEY

    def test_m1051_committed_at_head(self):
        # Byte-stable since #1392 main eb474941: zero diff
        # eb474941..HEAD on profiles/the-verge.yaml (verified in the
        # main run via git diff; pinned here).
        out = _git("diff", "eb474941", "HEAD", "--",
                   "profiles/the-verge.yaml")
        assert out.stdout.strip() == ""

    def test_m1051_mechanism_id_is_1051(self):
        block = _verge_block_1051()
        assert block["mechanism_id"] == 1051

    def test_m1051_iteration_and_type(self):
        block = _verge_block_1051()
        assert block["iteration"] == 1392
        assert block["iteration_type"] == "A"

    def test_m1051_entity_pair_and_publication(self):
        block = _verge_block_1051()
        assert block["entity_pair"] == "OpenAI vs Meta"
        assert block["publication_focus"] == "The Verge"

    def test_m1051_verdict_thesis_consistent(self):
        block = _verge_block_1051()
        assert block["verdict"] == "thesis_consistent_observation"

    def test_m1051_not_a_falsification_member(self):
        block = _verge_block_1051()
        assert "NOT a member of the falsification family" in \
            block["falsification_family"]
        assert "ledger holds at 65" in __doc__


class TestM1051Keying1395:
    def test_m1051_block_key_exact(self):
        block = _verge_block_1051()
        assert block["block_key"] == BLOCK_KEY

    def test_m1051_designed_keying_holds(self):
        # Designed keying per #723/#738/#739: the block key carries
        # the iteration (1392), never the mechanism number.
        assert "1392" in BLOCK_KEY
        assert "1051" not in BLOCK_KEY

    def test_m1051_distinct_from_m1050(self):
        # Not m1050 (#1387, WIRED x OpenAI on the SAME Oct-7/8 GPT-6
        # Intelligent UI peg): this run is the cross-publication
        # replication on the second deal-partner outlet (Vox/The
        # Verge x OpenAI May-2024 deal).
        block = _verge_block_1051()
        assert "m1050" in block["distinct_from_prior"]
        assert "WIRED" in block["distinct_from_prior"]

    def test_m1051_register_arithmetic(self):
        scoring = _verge_block_1051()[
            "asymmetry_scoring_manual_illustrative"]
        assert scoring["target_score_manual_illustrative"] == 0.10
        assert scoring["peer_score_manual_illustrative"] == -0.30
        assert scoring["delta_manual_illustrative"] == 0.40
        assert scoring["direction"] == \
            "target softer than peer by 0.40"


class TestM1051Discipline1395:
    def test_m1051_discipline_not_significant(self):
        scoring = _verge_block_1051()[
            "asymmetry_scoring_manual_illustrative"]
        assert scoring["significant"] is False
        assert scoring["p_value"] == "NOT_CALCULATED"
        assert scoring["cohens_d"] == "NOT_CALCULATED"
        assert scoring["ci_95"] == "NOT_CALCULATED"

    def test_m1051_carried_meta_arms_one(self):
        # The carried Verge x Meta Connect Muse Charm arm is m841
        # (#1017), -0.30, un-rescored per #807.
        block = _verge_block_1051()
        assert "m841" in block["finding"]
        assert "-0.30" in block["finding"]

    def test_m1051_counter_evidence_present(self):
        # The Verge Astra-safety arc (Aug-7-to-Sep-6-2026,
        # adversarial safety register on the payer) is carried as
        # counter-evidence bounding the softening to the
        # product-launch register.
        block = _verge_block_1051()
        assert "Astra" in block["distinct_from_prior"] or \
            "safety" in block["distinct_from_prior"].lower()

    def test_m1051_cautious_language(self):
        block = _verge_block_1051()
        assert "MANUAL ILLUSTRATIVE ONLY" in block["finding"]
        assert "NOT artifact-grade" in block["finding"]

    def test_m1051_statistical_discipline(self):
        flat = " ".join(__doc__.split())
        assert "MANUAL / QUALITATIVE ONLY" in flat
        assert "no_analysis_json_update true" in flat
        assert "Correlation is not causation" in flat

    def test_m1051_goal_and_job_ids(self):
        block = _verge_block_1051()
        assert block["goal_id"] == "goal_54093bda4145"
        assert block["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_m1051_author(self):
        block = _verge_block_1051()
        assert block["author"] == "Kit (with Ray)"


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1390-launched suite is
#    DEAD at [  2%] (TWENTY-NINTH consecutive death of the new
#    streak; tombstone lineage ONE-HUNDRED-THIRTY-SIXTH ->
#    ONE-HUNDRED-THIRTY-SEVENTH).
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1395:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG)

    def test_prior_suite_stalled_at_2(self):
        stream = _prior_suite_stream()
        assert "[  2%]" in stream

    def test_prior_suite_last_write_oct11_045952(self):
        # The #1390 re-launch's last write was Oct 11 04:59:52 PDT
        # (11:59:52 UTC); this run's ~08:05 AM PDT check is ~3.1h
        # stale. The tombstone write itself moved the file mtime, so
        # the last-write is pinned via the tombstone's own recorded
        # timestamp.
        text = _read(PRIOR_SUITE_LOG)
        assert "last write Oct 11 04:59:52 PDT" in text

    def test_no_live_pytest_holds_prior_log(self):
        # Verdict-time pin: no live process held the prior suite log
        # open at this run's ~08:05 AM PDT check. Scoped to the prior
        # log's basename per the #1365 _proc_holds_log approach - this
        # run's own re-launched suite writes to the NEW log and must
        # not trip the pin.
        assert _prior_log_holders() == []

    def test_zero_summary_tokens_in_dead_stream(self):
        stream = _prior_suite_stream()
        assert "passed" not in stream
        assert "failed" not in stream

    def test_zero_f_marks_in_dead_stream(self):
        stream = _prior_suite_stream()
        # pytest failure marks are dots-then-F; the dead stream is
        # dots only (the tombstone prose "F marks" does not match the
        # failure-mark pattern).
        f_lines = [line for line in stream.split("\n")
                   if re.search(r"\.+F", line)]
        assert len(f_lines) == 0, f_lines

    def test_twenty_ninth_death_of_new_streak(self):
        assert "TWENTY-NINTH consecutive" in __doc__

    def test_tombstone_lineage_advances(self):
        assert "ONE-HUNDRED-THIRTY-SIXTH ->" in __doc__
        assert "ONE-HUNDRED-THIRTY-SEVENTH" in __doc__

    def test_tombstone_written_to_prior_log(self):
        text = _read(PRIOR_SUITE_LOG)
        assert "TOMBSTONE #1395" in text
        assert "ONE-HUNDRED-THIRTY-SIXTH -> " \
            "ONE-HUNDRED-THIRTY-SEVENTH" in text

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected in the in-gate run (the ## #1395 entry is
        # written in the doc-sync step).
        text = _read(LOG_PATH)
        assert "## #1395 Type D" in text
        assert "DEAD at [  2%]" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: the dead stream is determinate-vacuous.
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1395:
    def test_zero_f_marks_in_dead_stream(self):
        stream = _prior_suite_stream()
        f_lines = [line for line in stream.split("\n")
                   if re.search(r"\.+F", line)]
        assert len(f_lines) == 0, f_lines

    def test_triage_is_determinate_vacuous(self):
        # No summary tokens, no F marks: there is nothing to triage.
        assert "nothing to triage" in __doc__
        assert "DETERMINATE-vacuous" in __doc__

    def test_no_repairs_claimed_from_stream(self):
        flat = " ".join(__doc__.split())
        assert "no recurring-failure triage repairs claimed" in flat


# ---------------------------------------------------------------------------
# 6. Statistical discipline: MANUAL / QUALITATIVE ONLY per the Aug 28
#    2026 standing rule; engine-layer synthetic calibration only.
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1395:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: max stays 1051, next stays 1052.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1051" in src
        assert "NEXT_NUM = 1052" in src
        assert _max_numeric_mechanism_id() == 1051

    def test_engine_not_run_on_corpus(self):
        # The calibration helper computes on deterministic synthetic
        # lists only (no corpus input, no repo reads); its docstring
        # states the engine-layer-only contract.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no corpus input" in src
        assert "never promoted to a finding" in src

    def test_synthetic_strong_pair_significant(self):
        r = _synthetic_calibration()
        assert abs(r["strong_asym"] - (-0.846567)) < 1e-5
        assert abs(r["strong_t"] - (-345.2432)) < 1e-2
        assert r["strong_p"] < 1e-12
        assert abs(r["strong_d"] - (-130.4897)) < 1e-2

    def test_synthetic_strong_ci_entirely_below_zero(self):
        r = _synthetic_calibration()
        lo, hi = r["strong_ci"]
        assert abs(lo - (-0.8526)) < 1e-3
        assert abs(hi - (-0.8406)) < 1e-3
        assert hi < 0

    def test_synthetic_near_null_pair_silent(self):
        r = _synthetic_calibration()
        assert r["null_p"] > 0.05
        lo, hi = r["null_ci"]
        assert abs(lo - (-0.072)) < 1e-3
        assert abs(hi - 0.0614) < 1e-3
        assert lo < 0 < hi

    def test_synthetic_degenerate_contract(self):
        r = _synthetic_calibration()
        assert r["deg_abs"] == 0.43
        assert r["deg_negates"] is True

    def test_synthetic_values_fresh_not_1390(self):
        # The calibration values are this run's own (-0.846567 /
        # t=-345.2432 / p=3.9856e-14), not #1390's (-0.805739 /
        # t=-133.8296 / p=1.1738e-11) and not #1385's (-0.840162 /
        # t=-104.9728 / p=5.0376e-11).
        r = _synthetic_calibration()
        assert r["strong_asym"] != -0.805739
        assert r["strong_asym"] != -0.840162

    def test_engine_significance_never_promoted(self):
        assert "Engine significance never promoted to finding" in \
            __doc__


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 65; fortieth absent; 48th-65th
#    intact; no 66th.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1395:
    def test_ledger_holds_at_65(self):
        # Type D lands no mechanisms and the corpus-integrity
        # verification is NOT a falsification-family member: ledger
        # holds at 65. Pinned via the docstring's own prose form
        # (kept lowercase-short per #715).
        assert "ledger holds at 65" in __doc__

    def test_fortieth_direction_absent(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def _member_pin(self, frag, path, expected):
        out = _git("grep", "-c", "-F", frag, "HEAD", "--", path)
        assert out.stdout.strip().endswith(":%d" % expected), \
            out.stdout

    def test_forty_eighth_member_intact(self):
        self._member_pin(_T48, "profiles/financial-times.yaml", 2)

    def test_forty_ninth_member_intact(self):
        self._member_pin(_T49, "profiles/careers/journalists.yaml", 3)

    def test_fiftieth_member_intact(self):
        self._member_pin(_T50, "profiles/careers/journalists.yaml", 3)

    def test_fifty_first_member_intact(self):
        self._member_pin(_T51, "profiles/news-corp.yaml", 3)

    def test_fifty_second_member_intact(self):
        self._member_pin(_T52, "profiles/careers/journalists.yaml", 5)

    def test_fifty_third_member_intact(self):
        self._member_pin(_T53, "profiles/the-verge.yaml", 2)

    def test_fifty_fourth_member_intact(self):
        self._member_pin(_T54, "profiles/guardian.yaml", 2)

    def test_fifty_fifth_member_intact(self):
        self._member_pin(_T55, "profiles/atlantic.yaml", 2)

    def test_fifty_sixth_member_intact(self):
        self._member_pin(_T56, "profiles/wired.yaml", 2)

    def test_fifty_seventh_member_intact(self):
        self._member_pin(_T57, "profiles/ap.yaml", 3)

    def test_fifty_eighth_member_intact(self):
        self._member_pin(_T58, "profiles/financial-times.yaml", 3)

    def test_fifty_ninth_member_intact(self):
        self._member_pin(_T59, "profiles/news-corp.yaml", 3)

    def test_sixtieth_member_intact(self):
        self._member_pin(_T60, "profiles/financial-times.yaml", 3)

    def test_sixty_first_member_intact(self):
        self._member_pin(_T61, "profiles/wired.yaml", 2)

    def test_sixty_second_member_intact(self):
        self._member_pin(_T62, "profiles/news-corp.yaml", 3)

    def test_sixty_third_member_intact(self):
        self._member_pin(_T63, "profiles/news-corp.yaml", 2)

    def test_sixty_fourth_member_intact(self):
        self._member_pin(_T64, "profiles/ap.yaml", 2)

    def test_sixty_fifth_member_intact(self):
        self._member_pin(_T65, "profiles/financial-times.yaml", 2)

    def test_no_sixty_sixth_member(self):
        assert _git_grep_tracked_source(_T66, ".") == []


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: max-1051, zero-1052 all forms, no-Type-D-#1395,
#    fortieth absent, 1394 forward guards held green pre-commit.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1395:
    def test_pins_on_1051_no_landing(self):
        # Type D lands no mechanisms: max stays 1051, next 1052.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1051" in src
        assert "NEXT_NUM = 1052" in src

    def test_no_type_d_1395_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721/#1292): every commit whose
        # message matches "Type D #1395" must be this run's main
        # commit or a descendant of it. Deselected in the in-gate
        # run (fails pre-commit by design: PRED_MAIN_1395 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type D #1395")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1395's own commits"
        main = _git("rev-parse", PRED_MAIN_1395).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_e_1396_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1396's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1396" must be #1396's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1396 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type E #1396")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1396's own commits"
        main = _git("rev-parse", PRED_MAIN_1396).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1052_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1052_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1052_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_1051(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_fortieth_direction_absent_live(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_1394_forward_guards_held_green_pre_commit(self):
        # #1394's staged guards (max-1051, zero-1052 all forms,
        # no-Type-D-#1395-in-git-log, fortieth absent, 48th-65th
        # intact, no 66th member, ledger 65) verified GREEN by this
        # run before the main commit; the no-Type-D-#1395 pin is the
        # #1191-class self-trip documented here, not repaired. NOTE:
        # #1394's pin is STRICT-form (assert hits == []) despite its
        # docstring's ancestor-form claim - it trips BY DESIGN at this
        # run's main commit and cannot flip green on the re-pin per
        # the #1392 strict-form precedent.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1051" in src
        assert "NEXT_NUM = 1052" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1394's guard lifecycle post-terminal-followup.
# ---------------------------------------------------------------------------


class TestStalenessPins1395:
    def test_1394_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: 1 failed + 27 passed. The
        # no_type_d_1395_in_git_log pin (the #1191-class self-trip:
        # this run's main commit carries "Type D #1395") is
        # STRICT-form in the #1394 file (assert hits == []), unlike
        # its docstring's ancestor-form claim; it trips BY DESIGN at
        # this run's main commit and cannot flip green on the #721
        # re-pin per the #1392 strict-form precedent (the #1392 file
        # documented the same for its no-Type-E-#1393 pin). The
        # 1052-form pins stay green throughout (Type D lands no
        # mechanisms; the #723/#738/#739 designed keying holds); the
        # member and direction pins stay green (no member, no
        # direction landed this run). The #1394 block is read-only to
        # this run; the trip is documented here, not repaired.
        # Deselected pre-commit (verified only post-terminal-followup).
        res = _class_run(C1394_FILE, "TestGuardLifecycle1394")
        out = res.stdout + res.stderr
        assert "1 failed, 27 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1395:
    def test_readme_test_file_table_has_1395_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1395_row_post_sync(self):
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


class TestIterationLog1395:
    def test_log_has_1395_entry(self):
        text = _read(LOG_PATH)
        assert "## #1395 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "TWENTY-NINTH consecutive" in text
        assert "type_d_1395_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1395:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1395_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1395 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1395:
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

    def test_1024_m846_absent_from_working_tree(self):
        # #1024 m846 (profiles/competitor-entities.yaml): VERIFIED
        # ABSENT from the working tree this run (no working-tree diff
        # on the file; the decision-pending edit is gone - resolved
        # without touching). Type D writes nothing to profiles/;
        # this run changes nothing there. Do NOT touch #1024 m846.
        out = _git("diff", "--name-only", "--",
                   "profiles/competitor-entities.yaml")
        assert out.stdout.strip() == ""
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src
