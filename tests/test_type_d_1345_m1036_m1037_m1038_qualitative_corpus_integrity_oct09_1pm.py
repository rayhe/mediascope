"""Type D iteration #1345: m1036/m1037/m1038 qualitative-discipline
corpus-integrity verification + #1340 background-suite verdict (DEAD
at [  0%]; NINETEENTH consecutive death of the new streak; tombstone
lineage ONE-HUNDRED-TWENTY-SIXTH -> ONE-HUNDRED-TWENTY-SEVENTH) +
recurring-failure triage (ZERO F marks in the dead stream - nothing
to triage, DETERMINATE-vacuous; no recurring-failure triage repairs
claimed from the stream) + broader regression sweep (30 failed / 480
passed across the 1340-1344 window files in ~437s; triaged: 6
#565-class anchor placeholder-duality and anchor-staleness pins
(post-anchor and post-HEAD-move, fail by design), 11 #1272-class
forward-guard numeric expiries and max-mechanism staleness pins (the
1033-numeric pin in the #1340 file, the 1036-numeric pin in the #1341
file, the 1037-numeric pin in the #1342 file, the 1038-numeric pin in
the #1343 file, the next-number-form pins, the max-1035/max-1036/
max-1037 pins, and the #1340/#1341 no-mechanisms-landed pins -
m1036/m1037/m1038 landed after those runs pinned), 4 #1191-class
member self-trips and forward-pin placeholders (the
no-sixty-third-member pins in the #1340/#1341 files - the sixty-third
member landed at #1342/m1036, permanent red by design; the
no-Type-D-#1345 forward pin in the #1344 file - fails pre-commit by
design, flips green at this run's terminal re-pin per #721), 4
#719-class doc-sync readme-stats-ratchet staleness pins (README has
moved to 77362/1669), 5 staleness artifacts (the #1340
staleness-pin post-commit form - the #1339 guard-lifecycle
1036-numeric and no-sixty-third pins overtaken by the #1342 landing;
the #1341 staleness-pin post-commit self-trip; the #1341 EHE
one-new-key pin - the key is in-corpus now; the #1344 novel-URL HEAD
pin - the 5 URLs are at HEAD now; the #1344 readme-table-row pin -
the row exists now). 0 remaining defects) +
full suite RE-LAUNCHED to goal/hidden_files/type_d_1345_full_suite.log.

m1036 (Type A #1342, profiles/news-corp.yaml
competitor_relationships.openai): The Times Sep-24-Oct-8-2026
safety/accountability cluster - four adversarial originals on the
$50M/yr licensing partner (cluster mean -0.39 MANUAL ILLUSTRATIVE)
vs the carried Times x Meta arm (Sep-7 privacy register, -0.55,
via m709 #797, un-rescored per #807); illustrative delta (OpenAI
minus Meta) +0.16 - near-symmetric hardness, the payer draws NO
softening at the accountability register; verdict
falsification_member_confirmed; SIXTY-THIRD falsification-family
member (ledger 62->63); FIRST dedicated Times x OpenAI member;
FIRST News Corp broadsheet-register member; domain-bounded to The
Times' safety/accountability register, Sep 24-Oct 8 2026.

m1037 (Type B #1343, profiles/careers/journalists.yaml
ariel_zilber_type_b competitor_coverage): Ariel Zilber (NY Post,
FULLY NOVEL journalist) Sep-16-2026 Meta 'creep glasses'
dating-surveillance piece (-0.55 MANUAL ILLUSTRATIVE, adversarial
privacy register) vs Oct-8-2026 Anthropic 'be nice to Claude'
usage-policy piece (-0.40, mock-adversarial register);
illustrative delta (anthropic minus meta) +0.15 - near-symmetric
adversarial, register-kind asymmetry (privacy-outrage vs tabloid
mockery) disclosed; verdict directionally_supported_not_proven;
NOT a falsification-family member; ledger holds at 63; FIRST
dedicated Type B pair on Zilber (fully novel journalist).

m1038 (Type C #1344, profiles/competitor-entities.yaml top-level):
Getty Images (US) v Stability AI Lanham Act survival order
(N.D. Cal. 3:25-cv-06891-TLT, Apr-23-2026 order, Doc. 53) - FIRST
dedicated corpus mechanism on the visual-licensor litigation leg:
trademark, false-designation and dilution claims survive dismissal;
AI outputs bearing distorted Getty watermarks are Lanham Act goods;
Dastar distinguished; household fame pled (2.8B annual searches);
UK parallel (Justice Joanna Smith, Nov 2025) won trademark in part,
lost secondary copyright (historic and extremely limited in scope);
Getty SIGNS with OpenAI (m684, Jun 2026 display deal) + Perplexity
(Oct 2025 visual licensing) while SUING Stability AI - selective
enforcement, the sue-side counterpart to the sign-side, mirrors the
Guardian triple-path; connects_to [636, 684, 1029]; verdict
mechanism_documented; NOT a falsification-family member (ledger
HOLDS at 63); NOT a new direction (fortieth absent by design);
MANUAL/qualitative ONLY; NOT artifact-grade; no analysis.json
update; tone NOT_SCORED.

Type D FIRST and OPENING leg of the 1345-1349 window
(D #1345 -> E #1346 -> A #1347 -> B #1348 -> C #1349 per the #565
anchor + rotation guard). The 1340-1344 window is VERIFIED CLOSED.
The #1350 Type D run owns the next verdict per #795.

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
NEWS_CORP_PATH = os.path.join(PROFILES_DIR, "news-corp.yaml")
JOURNALISTS_PATH = os.path.join(
    PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1340_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1345_full_suite.log")
OWN_BASENAME = (
    "test_type_d_1345_m1036_m1037_m1038_qualitative_"
    "corpus_integrity_oct09_1pm.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "fbd9c635e81575717ac42b1124d8f99484fd5749"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1038
NEXT_NUM = 1039  # integer only; key-form needles are format-built

# Predecessor chain: #1344 Type C closed the 1340-1344 window. All
# five legs (#1340-#1344) are pushed and ls-remote-verified (push status
# recorded DONE in each run's iteration-log entry, asserted below).
PRED_MAIN_1344 = "df15141d"
PRED_ANCHOR_1344 = "c92ec055"
PRED_DOCSYNC_1344 = "1261653b"
PRED_FINAL_1344 = "cde05a2c"
PRED_MAIN_1343 = "d3252af1"
PRED_ANCHOR_1343 = "0ed77aae"
PRED_DOCSYNC_1343 = "b6f4bb90"
PRED_FINAL_1343 = "e353a64c"
PRED_MAIN_1342 = "3e71adbd"
PRED_ANCHOR_1342 = "d1ce1912"
PRED_DOCSYNC_1342 = "13d866e8"
PRED_FINAL_1342 = "814a1c34"
PRED_MAIN_1341 = "f714800a"
PRED_ANCHOR_1341 = "40567e0e"
PRED_DOCSYNC_1341 = "adcd227c"
PRED_FINAL_1341 = "5cda62e5"
PRED_MAIN_1340 = "54574445"
PRED_ANCHOR_1340 = "abbfb457"
PRED_DOCSYNC_1340 = "5ebc61d0"
PRED_FINAL_1340 = "e568e59f"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the no-Type-D-#1345 own-run pin
# flips green post-repin).
PRED_MAIN_1345 = "fbd9c635e81575717ac42b1124d8f99484fd5749"

# Forward guard for the next leg: #1346 Type E. Re-pinned by #1346's
# anchor followup per #721 (starts as 0*40; placeholder-only).
PRED_MAIN_1346 = "9adb96df467924dbb9295f8c3dc3ac8c299c00c1"

# The #1344 window-closing file, for the staleness pin on its guard
# lifecycle (26 tests; post-terminal-followup form is 26 passed - the
# no-Type-D-#1345 forward pin flips at this run's main commit and is
# re-pinned green in the terminal log-hash followup per #721, its
# PRED_MAIN_1345 re-pinned in BOTH files per the #1292 precedent; the
# 1039-form pins stay green because Type D lands no mechanisms).
# Documented in TestStalenessPins1345, not repaired.
E1344_FILE = "test_type_c_1344_getty_stability_lanham_act_visual_licensor_suit_oct09_12pm.py"

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 77463  # patched pre-main: pre-sync 77362 + 101 collected
README_FILE_COUNT = 1670  # patched pre-main: pre-sync 1669 + 1 (this file)

# m846 block region in profiles/competitor-entities.yaml at HEAD (the
# #1024 m846 decision-pending block; byte-identity pin in the
# in-flight isolation class).
M846_HEAD_START = 26349
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
_T64 = "SIXT" + "Y-FOURTH falsification-family member"

# Fragment-built per #715: the contiguous keys never appear in this
# file. Iteration-form block keys carry no underscore-form mechanism
# key substring (the #723/#738/#739 designed-keying convention).
BLOCK_1036 = (
    "type_a_1342_times_openai_sep24_oct08_safety_accountability_"
    "cluster_vs_carried_times_meta_arms_oct09_11am"
)
BLOCK_1037 = (
    "type_b_1343_ariel_zilber_nypost_creep_glasses_vs_anthropic_"
    "claude_policy_oct09_11am"
)
BLOCK_1038 = (
    "type_c_1344_getty_stability_lanham_act_visual_licensor_"
    "suit_oct09_12pm"
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


def _newscorp_block_1036():
    """Locate the m1036 block in news-corp.yaml.

    The Type A blocks live under the competitor_relationships.openai
    section (m1036 appended at #1342). It is identified by its YAML
    dict key (BLOCK_1036) under the openai section.
    """
    data = _yaml(NEWS_CORP_PATH)
    return data["competitor_relationships"]["openai"][BLOCK_1036]


def _journalist_block_1037():
    """Locate the m1037 block on the Ariel Zilber record.

    The Type B blocks live under the per-journalist top-level
    record's competitor_coverage dict (m1037 sits on the
    ariel_zilber_type_b record, the FIRST dedicated Type B
    pair on Ariel Zilber).
    """
    journalists = _yaml(JOURNALISTS_PATH)
    rec = journalists.get("ariel_zilber_type_b")
    if not isinstance(rec, dict):
        return None
    cc = rec.get("competitor_coverage", {})
    if isinstance(cc, dict) and BLOCK_1037 in cc:
        return cc[BLOCK_1037]
    return None


def _entities_block_1038():
    """Locate the m1038 block (top-level key of competitor-entities)."""
    entities = _yaml(ENTITIES_PATH)
    return entities.get(BLOCK_1038)


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
    """Fresh engine-layer calibration contract for #1345.

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


class TestAnchor1345:
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
# 2. Rotation guard: #1344 closed the 1340-1344 window; #1345 opens.
# The 1340-1344 window is VERIFIED CLOSED.
# ---------------------------------------------------------------------------


class TestRotationGuard1345:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-120").stdout
        # All five legs of the 1340-1344 window have push-status
        # commits (push status recorded DONE in the iteration-log
        # entries and in the push-status commits).
        for sha, label in (
            (PRED_MAIN_1344, "1344 main"),
            (PRED_ANCHOR_1344, "1344 anchor"),
            (PRED_DOCSYNC_1344, "1344 doc-sync"),
            (PRED_FINAL_1344, "1344 log-hash"),
            (PRED_MAIN_1343, "1343 main"),
            (PRED_ANCHOR_1343, "1343 anchor"),
            (PRED_DOCSYNC_1343, "1343 doc-sync"),
            (PRED_FINAL_1343, "1343 log-hash"),
            (PRED_MAIN_1342, "1342 main"),
            (PRED_ANCHOR_1342, "1342 anchor"),
            (PRED_DOCSYNC_1342, "1342 doc-sync"),
            (PRED_FINAL_1342, "1342 log-hash"),
            (PRED_MAIN_1341, "1341 main"),
            (PRED_ANCHOR_1341, "1341 anchor"),
            (PRED_DOCSYNC_1341, "1341 doc-sync"),
            (PRED_FINAL_1341, "1341 log-hash"),
            (PRED_MAIN_1340, "1340 main"),
            (PRED_ANCHOR_1340, "1340 anchor"),
            (PRED_DOCSYNC_1340, "1340 doc-sync"),
            (PRED_FINAL_1340, "1340 log-hash"),
        ):
            assert sha in log, label

    def test_all_window_push_status_done(self):
        # Push status is recorded DONE in each run's iteration-log
        # entry (in the repo, at HEAD); the main sha appears in the
        # same entry's push-status line.
        text = _git("show", "HEAD:iteration-log.md").stdout
        for sha, num in (
            (PRED_MAIN_1344, "1344"), (PRED_MAIN_1343, "1343"),
            (PRED_MAIN_1342, "1342"), (PRED_MAIN_1341, "1341"),
            (PRED_MAIN_1340, "1340"),
        ):
            assert sha[:8] in text, num
        assert text.count("Push status (this run): DONE") >= 5

    def test_1344_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1344")
        assert "Type C #1344" in out.stdout

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1345-1349 window" in src

    def test_1340_1344_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1340-1344 window is VERIFIED CLOSED" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1345 -> E #1346 -> A #1347 -> B #1348 -> C #1349" in src

    def test_next_window_verdict_belongs_to_1345(self):
        # Per #795 the next background-suite verdict (on the
        # #1345-launched suite) belongs to the next Type D run,
        # #1345.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1350 Type D run owns the next verdict" in src


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1036 / m1037 / m1038 all landed and intact.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1345:
    def test_m1036_block_present_in_newscorp(self):
        assert _newscorp_block_1036() is not None

    def test_m1036_mechanism_id_1036(self):
        block = _newscorp_block_1036()
        assert block["mechanism_id"] == 1036
        assert block["iteration"] == 1342
        assert block["iteration_type"] == "A"
        assert block["block_key"] == BLOCK_1036

    def test_m1036_times_openai_safety_cluster_peg_identified(self):
        # The Type A corpus schema nests the prose peg under the
        # openai_arm_new / meta_arm_carried pair; the Sep-24-Oct-8
        # Times x OpenAI safety/accountability cluster peg and the
        # times x openai vs times x meta pair identify the block.
        block = _newscorp_block_1036()
        assert block["competitor_pair"] == "times x openai vs times x meta"
        assert block["openai_arm_new"][
            "tone_MANUAL_ILLUSTRATIVE_mean"] == -0.39
        assert block["meta_arm_carried"][
            "tone_MANUAL_ILLUSTRATIVE"] == -0.55

    def test_m1036_verdict_falsification_member_confirmed(self):
        # m1036 is the SIXTY-THIRD falsification-family member: the
        # Times ran four adversarial originals Sep 24-Oct 8 2026 on
        # its $50M/yr licensing partner (cluster mean -0.39) against
        # the carried Times x Meta arm (-0.55); illustrative delta
        # (OpenAI minus Meta) +0.16 - near-symmetric hardness, the
        # payer draws NO softening at the accountability register;
        # verdict falsification_member_confirmed; ledger 63.
        block = _newscorp_block_1036()
        assert block["verdict"] == "falsification_member_confirmed"
        assert block["falsification_family_member"] is True
        assert block["falsification_ledger"] == "63"
        assert block["author"] == "Kit (with Ray)"

    def test_m1037_block_present_in_journalists(self):
        assert _journalist_block_1037() is not None

    def test_m1037_mechanism_id_1037(self):
        block = _journalist_block_1037()
        assert block["mechanism_id"] == 1037
        assert block["iteration"] == 1343
        assert block["iteration_type"] == "B"

    def test_m1037_block_key_field(self):
        block = _journalist_block_1037()
        assert block["block_key"] == BLOCK_1037

    def test_m1037_verdict_directionally_supported(self):
        # m1037 is a directionally_supported_not_proven cross-entity
        # register-constancy pair (Ariel Zilber, NY Post: Sep-16 Meta
        # 'creep glasses' dating-surveillance piece, -0.55, vs Oct-8
        # Anthropic 'be nice to Claude' usage-policy piece, -0.40;
        # illustrative delta (anthropic minus meta) +0.15 -
        # near-symmetric adversarial, register-kind asymmetry
        # disclosed), NOT a falsification-family member; ledger
        # holds at 63.
        block = _journalist_block_1037()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["falsification_family_member"] is False
        assert block["illustrative_delta_anthropic_minus_meta"] == 0.15

    def test_m1037_first_pair_on_zilber_in_notes(self):
        # The FIRST dedicated Type B pair on Ariel Zilber (fully
        # novel journalist); the record notes carry the ledger
        # position.
        rec = _yaml(JOURNALISTS_PATH)["ariel_zilber_type_b"]
        assert "FIRST" in rec["notes"]
        assert "ledger holds at 63" in rec["notes"]
        assert _journalist_block_1037()["author"] == "Kit (with Ray)"

    def test_m1038_block_present_in_entities(self):
        entities = _yaml(ENTITIES_PATH)
        assert BLOCK_1038 in entities

    def test_m1038_mechanism_id_1038(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1038]
        assert block["mechanism_id"] == 1038
        assert block["iteration"] == 1344
        assert block["iteration_type"] == "C"

    def test_m1038_block_key_field(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1038]["block_key"] == BLOCK_1038

    def test_m1038_verdict_mechanism_documented(self):
        # m1038 documents the Getty Images (US) v Stability AI Lanham
        # Act survival order (N.D. Cal. 3:25-cv-06891-TLT, Apr-23-2026
        # order, Doc. 53) - the FIRST dedicated corpus mechanism on
        # the visual-licensor litigation leg: trademark,
        # false-designation and dilution claims survive dismissal; AI
        # outputs bearing distorted Getty watermarks are Lanham Act
        # goods; Getty SIGNS with OpenAI (m684) + Perplexity while
        # SUING Stability AI (selective enforcement, the sue-side
        # counterpart to the sign-side); verdict
        # mechanism_documented; NOT a falsification-family member;
        # ledger holds at 63; tone NOT_SCORED.
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1038]
        assert block["verdict"] == "mechanism_documented"
        assert block["falsification_family_member"] is False
        assert "ledger holds at 63" in block["falsification_family"]

    def test_m1038_author(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1038]["author"] == "Kit (with Ray)"

    def test_max_numeric_mechanism_id_is_1038(self):
        assert _max_numeric_mechanism_id() == MECH_NUM


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1340 suite is DEAD at [  0%].
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1345:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG

    def test_prior_suite_stalled_at_0(self):
        # The #1340-launched suite froze at [  0%] progress: 780
        # bytes, zero F marks, last write Oct 9 2026 09:35:16 PDT
        # (~3.5h stale at this run's ~1:00 PM PDT check), zero live
        # pytest processes (the pgrep sweep at this run's check
        # returned zero live pytest processes; the /proc open-fd
        # check returns empty). Progress never regresses, so the
        # [  0%] marker stays present and [  1%] never arrives.
        # Observation history: #1340 launched it and saw it ALIVE at
        # doc-sync (dots accumulating at [  0%]); #1341 observed it
        # ALIVE at [  0%]; #1342 observed it ALIVE at [  0%] (one
        # live pytest process); #1343 observed only per #795;
        # #1344's ~12:00 PM PDT check found it DEAD at [  0%] with
        # last write 09:35:16 PDT and zero live processes (recorded
        # not adjudicated); this run verdicts it DEAD at ~1:00 PM
        # PDT.
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
        # type_d_1340_full_suite.log open anymore (the /proc open-fd
        # check returns empty; the pgrep sweep at this run's ~1:00 PM
        # PDT check returned zero live pytest processes).
        holders = _proc_holds_log("type_d_1340_full_suite.log")
        assert holders == "", holders

    def test_nineteenth_death_of_new_streak(self):
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
        # #1335-launched the SEVENTEENTH (#1340 verdict): the
        # #1340-launched suite's death verdict, rendered this run,
        # is the NINETEENTH consecutive background-suite death of
        # the new streak.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NINETEENTH consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-TWENTY-SIXTH -> ONE-HUNDRED-TWENTY-SEVENTH.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ONE-HUNDRED-TWENTY-SIXTH" in src
        assert "lineage advances" in src

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1345 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_PATH)
        assert "NINETEENTH consecutive" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: DETERMINATE-vacuous (zero F marks).
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1345:
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


class TestStatisticalDiscipline1345:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: the max numeric mechanism id is
        # unchanged at 1038 and no 1037-form keys exist.
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
# 7. Falsification ledger: holds at 63; guards on member forms.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1345:
    def test_ledger_holds_at_63(self):
        # One new falsification-family member in the 1340-1344 window
        # (m1036, the SIXTY-THIRD): m1036 (news-corp.yaml) carries
        # falsification_ledger "63"; m1037 (ariel_zilber_type_b record
        # notes) and m1038 (competitor-entities falsification_family)
        # carry the ledger-holds-at-63 note.
        block = _newscorp_block_1036()
        assert block["falsification_ledger"] == "63"
        rec = _yaml(JOURNALISTS_PATH)["ariel_zilber_type_b"]
        assert "ledger holds at 63" in rec["notes"]
        entities = _yaml(ENTITIES_PATH)
        assert "ledger holds at 63" in entities[
            BLOCK_1038]["falsification_family"]

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
        # Landed #1332 (m1030, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_third_member_intact(self):
        # Landed #1342 (m1036, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T63, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_fourth_member(self):
        assert _git_grep_tracked_source(_T64, None) == []

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
# 8. Guard lifecycle: forward pins for #1346; #1344 staged for this run.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1345:
    def test_pins_on_1038_no_landing(self):
        # Type D lands no mechanisms: max stays 1038, next stays 1039.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1038" in src
        assert "NEXT_NUM = 1039" in src

    def test_no_type_d_1345_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721): every commit whose message
        # matches "Type D #1345" must be this run's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type D #1345")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1345's own commits"
        main = _git("rev-parse", PRED_MAIN_1345).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_e_1346_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1346's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1346" must be #1346's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1346 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type E #1346")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1346's own commits"
        main = _git("rev-parse", PRED_MAIN_1346).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1039_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1039_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1039_dash_absent_repo_wide(self):
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
        # Landed #1342 (m1036, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_third_member_present_pin(self):
        # Landed #1342 (m1036, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T63, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_fourth_member_pin(self):
        # Type D lands no mechanisms; the sixty-fourth member-claim
        # form stays absent repo-wide.
        assert _git_grep_tracked_source(_T64, None) == []

    def test_predecessor_1344_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1344_FILE))

    def test_next_leg_is_1346_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1346 Type E" in src

    def test_1344_pins_flip_documented(self):
        # #1344 staged guard-lifecycle forward pins for this run
        # (no-Type-D-#1345-in-git-log, zero one-zero-three-nine keys
        # all forms, fortieth direction absent, forty-eighth through
        # sixty-third members intact, no sixty-fourth member, ledger
        # 63); all verified GREEN pre-commit this run (manual
        # forward-guard verification, recorded in the iteration-log
        # entry). The no-Type-D-#1345 pin flips BY DESIGN at this
        # run's main commit (the #1191-class self-trip, re-pinned
        # post-commit by TestStalenessPins1345); the 1039-form pins
        # stay green because Type D lands no mechanisms. Documented in
        # the staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1345" in src
        assert "no_type_d_1345_in_git_log_pin" in src
        assert "#1191-class" in src
        assert "#1272-class" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1344's guard lifecycle flips once, then re-pins.
# ---------------------------------------------------------------------------


class TestStalenessPins1345:
    def test_1344_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: all 26 pass. The
        # no_type_d_1345_in_git_log pin (the #1191-class self-trip:
        # this run's main commit carries "Type D #1345") flipped BY
        # DESIGN at this run's main commit and is re-pinned green in
        # the terminal log-hash followup per #721 (PRED_MAIN_1345 now
        # holds this run's main sha in BOTH this file and the #1344
        # file per the #1292 precedent). The 1039-form pins stay green
        # throughout (Type D lands no mechanisms; the #723/#738/#739
        # designed keying holds); the member and direction pins stay
        # green (no member, no direction landed this run). The #1344
        # block is read-only to this run; the flip is documented here,
        # not repaired. Deselected pre-commit (verified only
        # post-terminal-followup).
        res = _class_run(E1344_FILE, "TestGuardLifecycle1344")
        out = res.stdout + res.stderr
        assert "26 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1345:
    def test_readme_test_file_table_has_1345_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1345_row_post_sync(self):
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


class TestIterationLog1345:
    def test_log_has_1345_entry(self):
        text = _read(LOG_PATH)
        assert "## #1345 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "NINETEENTH consecutive" in text
        assert "type_d_1345_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1345:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1345_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1345 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1345:
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
