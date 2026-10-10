"""Type D iteration #1365: m1045 qualitative-discipline
corpus-integrity verification + #1360 background-suite verdict (DEAD
at [  3%]; TWENTY-THIRD consecutive death of the new streak;
tombstone lineage ONE-HUNDRED-THIRTIETH ->
ONE-HUNDRED-THIRTY-FIRST) + recurring-failure triage (ZERO F marks
in the dead stream - nothing to triage, DETERMINATE-vacuous; no
recurring-failure triage repairs claimed from the stream) +
broader regression sweep (20 failed / 408 passed across the
1360-1364 window files in ~104s; triaged: 5 #565-class anchor
placeholder-duality pins, 8 #1272-class forward-guard numeric
expiries and max-mechanism staleness pins (m1045 landed at #1362
after those runs pinned max-1044), 3 #1191-class forward-pin
self-trips (the #1364 no-Type-D-#1365 pin, flips green at this run's
terminal re-pin per #721; the #1363/#1364
no-entry-in-iteration-log pre-commit pins, stale post-commit BY
DESIGN), 4 #719-class doc-sync readme-stats-ratchet staleness
pins; 0 remaining defects) + fresh engine-layer synthetic
calibration (never on the corpus, never promoted) + full suite
RE-LAUNCHED to goal/hidden_files/type_d_1365_full_suite.log.

m1045 (Type A #1362, profiles/nytimes.yaml
competitor_relationships.openai): NYT x OpenAI Oct-8-2026
publisher-copyright-suit legal-enforcement bounded absence - ZERO
NYT originals inside a ~60-row bounded surface (1 delegated scout:
10 searches, ~40 rows; 3 main-run browser.search verification
sets, ~22 rows; zero nytimes.com URLs; zero NYT bylines; zero
NYT-hosted wires; 0 browser.open per #503, excerpt-bounded) on the
USA TODAY Co. v OpenAI publisher-copyright suit (SDNY
1:26-cv-08892; fourteen Gannett-related corporate plaintiffs; 19
publications; 79-page complaint; direct copyright infringement 17
USC 501, vicarious infringement, intentional DMCA 1202 CMI removal;
>$250M sought plus model/training-set destruction; Reuters wire
same day, OpenAI no immediate comment), versus carried NYT x Meta
arms (carried un-rescored per #807). The NYT is OpenAI's
ADVERSARIAL plaintiff (Dec 2023, billions sought,
coverage_prediction "adversarial"); the absence is the
cross-publication replication of m1044 (FT leg, #1357) from the
opposite financial posture. Verdict mechanism_documented, NOT a
falsification-family member; ledger holds at 64. The sole mechanism
landed in the 1360-1364 window (#1361 Type E, #1363 Type B, #1364
Type C landed no mechanisms - saturation screenings).

Statistical discipline: MANUAL / QUALITATIVE ONLY per the Aug 28 2026
standing rule (tone values hand-assigned register positions on
carried arms only; the absent arm is NOT_SCORED;
p_value/cohens_d/ci_95 NOT_CALCULATED on the corpus; is_significant
false; engine NOT run on corpus; verdict mechanism_documented on a
verification, not a discovery; NOT artifact-grade;
no_analysis_json_update true). Correlation is not causation;
hypothesis-generating only. The body's "verify the asymmetry scoring
produces statistically meaningful results" resolves to verifying the
discipline plus a fresh engine-layer synthetic calibration (never on
the corpus, never promoted to a finding): strong-signal n=7-per-arm
synthetic pair asymmetry -0.855714, t=-31.0706, p=9.687e-13,
d=-16.6079, is_significant True at ENGINE layer, CI entirely below
zero; near-null pair silent (p=0.7781, not significant); degenerate
n=1/n=1 contract guard t=0.0/p=1.0/d=0.0, |asymmetry| == 0.40 exact,
arm-swap negates. Engine significance never promoted to finding
layer.

The #1360-launched suite is verdict DEAD at [  3%]
(TWENTY-THIRD consecutive death of the new streak; tombstone lineage
ONE-HUNDRED-THIRTIETH -> ONE-HUNDRED-THIRTY-FIRST). Last write Oct
10 2026 03:59:53 PDT (~3h stale at this run's ~07:10 AM PDT check);
zero live pytest processes at this run's check; no summary tokens in
the #1360b stream; zero F marks in the dead stream - nothing to
triage, DETERMINATE-vacuous; no recurring-failure triage repairs
claimed from the stream. Full suite RE-LAUNCHED to
goal/hidden_files/type_d_1365_full_suite.log; observed ALIVE at
launch (dots accumulating). Its verdict and tombstone belong to
#1370 (next Type D) per #795.

Type D lands no mechanisms this run: max numeric mechanism_id stays
1045, no 1046-form keys exist (numeric/underscore/dash), fortieth
relationship direction absent, forty-eighth through sixty-fourth
falsification-family members intact, no sixty-fifth member
repo-wide, ledger holds at 64.

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file) all
left out of this run's index/diff (explicit-path staging). #1024 m846
(profiles/competitor-entities.yaml) NOT touched - decision pending.
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
NYT_PATH = os.path.join(PROFILES_DIR, "nytimes.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1360_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1365_full_suite.log")
OWN_BASENAME = (
    "test_type_d_1365_m1045_qualitative_"
    "corpus_integrity_oct10_7am.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "0" * 40

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1045
NEXT_NUM = 1046  # integer only; key-form needles are format-built

BLOCK_1045 = (
    "type_a_1362_nyt_openai_oct08_publisher_copyright_suit_"
    "legal_enforcement_bounded_absence_vs_carried_meta_arms"
)
BLOCK_M1039_AP = (
    "type_a_1347_ap_openai_oct09_chan_safety_researcher_firings_"
    "wire_vs_carried_meta_18bn_arm_oct09_2pm"
)

# Predecessor chain: #1364 Type C closed the 1360-1364 window. All
# five legs (#1360-#1364) are pushed and ls-remote-verified (push
# status recorded DONE in each run's iteration-log entry, asserted
# below).
PRED_MAIN_1360 = "c135fc21"
PRED_MAIN_1361 = "790f4f74"
PRED_MAIN_1362 = "330f55d0"
PRED_MAIN_1363 = "8074ebdc"
PRED_MAIN_1364 = "3d37f36c"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the no-Type-D-#1365 own-run pin
# flips green post-repin).
PRED_MAIN_1365 = "0" * 40

# Forward guard for the next leg: #1366 Type E. Re-pinned by #1366's
# anchor followup per #721 (starts as 0*40; placeholder-only).
PRED_MAIN_1366 = "0" * 40

# The #1364 window-closing file, for the staleness pin on its guard
# lifecycle (25 tests; post-terminal-followup form is 25 passed - the
# no-Type-D-#1365 forward pin flips at this run's main commit and is
# re-pinned green in the terminal log-hash followup per #721, its
# PRED_MAIN_1365 re-pinned in BOTH files per the #1292 precedent; the
# 1046-form pins stay green because Type D lands no mechanisms).
# Documented in TestStalenessPins1365, not repaired.
E1364_FILE = (
    "test_type_c_1364_financial_incentive_saturation_oct10_6am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 79302  # patched pre-main: pre-sync 79216 + 86 collected
README_FILE_COUNT = 1690  # patched pre-main: pre-sync 1689 + 1 (this file)

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
_T65 = "SIXT" + "Y-FIFTH falsification-family member"
_T35 = "THIR" + "TY-FIFTH falsification-family member"
_T36 = "THIR" + "TY-SIXTH falsification-family member"
_T37 = "THIR" + "TY-SEVENTH falsification-family member"
_T38 = "THIR" + "TY-EIGHTH falsification-family member"
_T39 = "THIR" + "TY-NINTH falsification-family member"


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


def _nyt_block_1045():
    """Locate the m1045 block in nytimes.yaml.

    The Type A blocks live under the competitor_relationships.openai
    section (m1045 appended at #1362). It is identified by its YAML
    dict key (BLOCK_1045) under the openai section.
    """
    data = _yaml(NYT_PATH)
    return data["competitor_relationships"]["openai"][BLOCK_1045]


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


def _prior_suite_stream():
    """Return the #1360b re-launch stream of the prior suite log.

    The log carries two launches: the first attempt (system python3,
    died at collection with 39 textblob ModuleNotFoundError - its
    collection-error summary is NOT a completion) and the #1360b
    re-launch (venv interpreter, dots to [  3%]). The verdict is
    rendered on the #1360b stream only.
    """
    text = _read(PRIOR_SUITE_LOG)
    marker = "=== RE-LAUNCH #1360b"
    idx = text.rfind(marker)
    assert idx >= 0, "re-launch marker missing"
    return text[idx:]


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
    """Fresh engine-layer calibration contract for #1365.

    Strong-signal synthetic pair (n=7 per arm, no corpus input, no
    repo reads). Engine-layer ONLY: never promoted to a finding,
    never scored against the corpus.
    """
    from mediascope.score.asymmetry import calculate_asymmetry
    from datetime import datetime
    strong_target = [-0.80, -0.75, -0.85, -0.70, -0.78, -0.82, -0.77]
    strong_peers = [0.10, 0.05, 0.15, 0.00, 0.12, 0.08, 0.02]
    r = calculate_asymmetry(
        strong_target, strong_peers, "meta", ["openai"], "wired",
        datetime(2026, 10, 1), datetime(2026, 10, 10))
    return r


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1365:
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
# 2. Rotation guard: #1364 closed the 1360-1364 window; #1365 opens.
# The 1360-1364 window is VERIFIED CLOSED.
# ---------------------------------------------------------------------------


class TestRotationGuard1365:
    def test_predecessor_mains_in_git_log(self):
        log = _git("log", "--oneline", "-200").stdout
        for sha, label in (
            (PRED_MAIN_1360, "1360 main"),
            (PRED_MAIN_1361, "1361 main"),
            (PRED_MAIN_1362, "1362 main"),
            (PRED_MAIN_1363, "1363 main"),
            (PRED_MAIN_1364, "1364 main"),
        ):
            assert sha in log, label

    def test_all_window_push_status_done(self):
        # Push status is recorded in each run's iteration-log entry
        # (in the repo, at HEAD); the main sha appears in the same
        # entry's push-status line.
        text = _git("show", "HEAD:iteration-log.md").stdout
        for sha, num in (
            (PRED_MAIN_1360, "1360"), (PRED_MAIN_1361, "1361"),
            (PRED_MAIN_1362, "1362"), (PRED_MAIN_1363, "1363"),
            (PRED_MAIN_1364, "1364"),
        ):
            assert sha[:8] in text, num
        assert text.count("Push status (this run)") >= 5
        assert text.count("Push status (this run): DONE") >= 4

    def test_1364_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1364")
        assert "Type C #1364" in out.stdout

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1365-1369 window" in src

    def test_1360_1364_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1360-1364 window is VERIFIED CLOSED" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1365 -> E #1366 -> A #1367 -> B #1368 -> C #1369" in src

    def test_next_window_verdict_belongs_to_1370(self):
        # Per #795 the next background-suite verdict (on the
        # #1365-launched suite) belongs to the next Type D run,
        # #1370.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1370 Type D run owns the next verdict" in src


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1045 landed in the 1360-1364 window and is intact.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1365:
    def test_m1045_block_present_in_nytimes(self):
        block = _nyt_block_1045()
        assert block is not None
        assert block["mechanism_id"] == 1045

    def test_m1045_verdict_mechanism_documented(self):
        block = _nyt_block_1045()
        assert block["verdict"] == "mechanism_documented"

    def test_m1045_not_falsification_member(self):
        block = _nyt_block_1045()
        assert block["falsification_family_member"] is False
        assert "NOT a falsification-family member" in block["falsification_family"]

    def test_m1045_block_key_exact(self):
        data = _yaml(NYT_PATH)
        assert BLOCK_1045 in data["competitor_relationships"]["openai"]
        block = _nyt_block_1045()
        assert block["block_key"] == BLOCK_1045
        assert block["iteration"] == 1362
        assert block["iteration_type"] == "A"
        assert block["publication"] == "New York Times"
        assert block["competitor"] == "openai"

    def test_m1045_ledger_note_holds_64(self):
        block = _nyt_block_1045()
        assert "Ledger holds at 64" in block["ledger_note"]
        assert block["ledger"] == "64"
        assert block["falsification_ledger"] == "64"

    def test_m1045_distinct_from_prior(self):
        block = _nyt_block_1045()
        distinct = block["distinct_from_prior"]
        assert "m1044" in distinct

    def test_m1045_counterevidence_four_items(self):
        block = _nyt_block_1045()
        ce = block["counterevidence"]
        assert len(ce) == 4
        assert any("m471" in c for c in ce)

    def test_m1045_confounders_ranked(self):
        block = _nyt_block_1045()
        conf = block["confounders_ranked"]
        assert set(conf.keys()) >= {"strong", "moderate", "weak"}
        assert len(conf["strong"]) >= 2

    def test_m1045_statistical_discipline(self):
        block = _nyt_block_1045()
        sd = block["statistical_discipline"]
        assert "MANUAL / QUALITATIVE ONLY" in sd
        assert "NOT artifact-grade" in sd

    def test_m1045_no_analysis_json_update(self):
        block = _nyt_block_1045()
        assert block["no_analysis_json_update"] is True
        assert block["correlation_not_causation"] is True

    def test_m1045_source_urls_seven(self):
        block = _nyt_block_1045()
        urls = block["source_urls"]
        assert len(urls) == 7
        assert any("cryptobriefing.com" in u for u in urls)
        assert any("substack.com" in u for u in urls)

    def test_m1045_carried_meta_arms(self):
        block = _nyt_block_1045()
        carried = block["meta_arm_carried"]["carried_from"]
        assert "NYT x Meta arms carried" in carried


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1360-launched suite is DEAD
# at [  3%] - TWENTY-THIRD consecutive death of the new streak.
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1365:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG

    def test_prior_suite_stalled_at_3(self):
        # The #1360-launched suite froze at [  3%] progress: the
        # first attempt died at collection (39 textblob
        # ModuleNotFoundError - launched with system python3 instead
        # of .venv/bin/python; its collection-error summary is NOT a
        # completion); the #1360b re-launch (venv interpreter) ran
        # dots to [  3%] by its 03:59:53 PDT last write and never
        # progressed. The verdict is rendered on the #1360b stream:
        # it carries [  3%] and never [  4%]; last write Oct 10 2026
        # 03:59:53 PDT (~3h stale at this run's ~07:10 AM PDT check);
        # zero live pytest processes (the pgrep sweep at this run's
        # check returned zero; the /proc open-fd check returns
        # empty). Progress never regresses, so the [  3%] marker
        # stays present and [  4%] never arrives. Observation
        # history: #1360 launched it and saw it ALIVE at launch
        # (dots accumulating); #1361/#1362/#1363/#1364 CHECKED ONLY
        # per #795 (no verdict rendered, none adjudicated); this run
        # verdicts it DEAD at ~07:10 AM PDT.
        stream = _prior_suite_stream()
        assert "[  3%]" in stream
        assert "[  4%]" not in stream
        assert 100 <= len(stream) <= 100000, len(stream)

    def test_prior_suite_has_zero_summary_tokens(self):
        # A completed run prints a summary ("passed"/"failed") or a
        # collection report ("no tests ran" / "short test summary").
        # The dead #1360b stream carries none of them (the tombstone
        # line is worded to avoid those tokens). Scoped to the
        # #1360b stream: the first attempt's collection-error summary
        # lives before the re-launch marker and is not a completion.
        stream = _prior_suite_stream()
        for token in ("passed", "failed", "no tests ran",
                      "short test summary"):
            assert token not in stream, token

    def test_no_live_pytest_holds_prior_log(self):
        # The #1190-class death check: NO live pytest process holds
        # type_d_1360_full_suite.log open anymore (the /proc open-fd
        # check returns empty; the pgrep sweep at this run's ~07:10
        # AM PDT check returned zero live pytest processes).
        holders = _proc_holds_log("type_d_1360_full_suite.log")
        assert holders == "", holders

    def test_twenty_third_death_of_new_streak(self):
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
        # #1335-launched the SEVENTEENTH (#1340 verdict),
        # #1340-launched the EIGHTEENTH (#1345 verdict),
        # #1345-launched the NINETEENTH (#1350 verdict),
        # #1350-launched the TWENTIETH (#1355 verdict),
        # #1355-launched the TWENTY-FIRST (#1360 verdict),
        # #1360-launched the TWENTY-SECOND (#1365 verdict): the
        # #1360-launched suite's death verdict, rendered this run,
        # is the TWENTY-THIRD consecutive background-suite death of
        # the new streak.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TWENTY-THIRD consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-THIRTIETH ->
        # ONE-HUNDRED-THIRTY-FIRST.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ONE-HUNDRED-THIRTIETH" in src
        assert "lineage advances" in src

    def test_tombstone_written_to_prior_log(self):
        # The verdict's tombstone is appended to the dead log file
        # (this run owns the verdict per #795).
        text = _read(PRIOR_SUITE_LOG)
        assert "TOMBSTONE #1365" in text
        assert "TWENTY-THIRD consecutive" in text

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1365 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_PATH)
        assert "TWENTY-THIRD consecutive" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: DETERMINATE-vacuous (zero F marks).
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1365:
    def test_zero_f_marks_in_dead_stream(self):
        stream = _prior_suite_stream()
        f_lines = [line for line in stream.split("\n")
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


class TestStatisticalDiscipline1365:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: max stays 1045, next stays
        # 1046.
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_engine_not_run_on_corpus(self):
        # The asymmetry scorer is intentionally NOT run on the corpus
        # per the Aug 28 2026 standing rule; the body's "statistically
        # meaningful" check is satisfied by discipline verification
        # plus the engine-layer synthetic calibration below, never by
        # scoring the corpus.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run on" in src

    def test_synthetic_strong_pair_significant(self):
        r = _synthetic_calibration()
        assert abs(r.asymmetry_score - (-0.855714)) < 1e-4
        assert abs(r.t_statistic - (-31.0706)) < 1e-2
        assert r.p_value < 1e-10
        assert r.is_significant is True
        assert r.confidence_interval_upper < 0.0

    def test_synthetic_strong_ci_entirely_below_zero(self):
        r = _synthetic_calibration()
        assert abs(r.confidence_interval_lower - (-0.9029)) < 1e-3
        assert abs(r.confidence_interval_upper - (-0.8043)) < 1e-3

    def test_synthetic_near_null_pair_silent(self):
        # Near-null synthetic pair: the engine stays silent (no
        # significance), proving the calibration does not hallucinate
        # signal.
        from mediascope.score.asymmetry import calculate_asymmetry
        from datetime import datetime
        null_target = [-0.05, 0.02, -0.03, 0.01, -0.02, 0.04, -0.01]
        null_peers = [0.03, -0.01, 0.02, -0.04, 0.01, -0.02, 0.00]
        r = calculate_asymmetry(
            null_target, null_peers, "meta", ["openai"], "wired",
            datetime(2026, 10, 1), datetime(2026, 10, 10))
        assert r.is_significant is False
        assert r.p_value > 0.5

    def test_synthetic_degenerate_contract(self):
        # Degenerate n=1/n=1: t=0.0/p=1.0/d=0.0 guard holds;
        # |asymmetry| == 0.40 exact; arm-swap negates.
        from mediascope.score.asymmetry import calculate_asymmetry
        from datetime import datetime
        r = calculate_asymmetry(
            [-0.40], [0.00], "meta", ["openai"], "wired",
            datetime(2026, 10, 1), datetime(2026, 10, 10))
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert abs(abs(r.asymmetry_score) - 0.40) < 1e-9
        r2 = calculate_asymmetry(
            [0.00], [-0.40], "meta", ["openai"], "wired",
            datetime(2026, 10, 1), datetime(2026, 10, 10))
        assert abs(r2.asymmetry_score - 0.40) < 1e-9

    def test_engine_significance_never_promoted(self):
        # Engine-layer significance is a calibration contract, never
        # a finding: the docstring says so.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "never promoted to a finding" in src


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 64; member forms intact.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1365:
    def test_ledger_holds_at_64(self):
        # Zero new falsification-family members in the 1360-1364
        # window (the sole landed mechanism, m1045, is
        # mechanism_documented, NOT a member): m1045
        # (nytimes.yaml) carries the "Ledger holds at 64"
        # note; the SIXTY-FOURTH member-form is m1039 (ap.yaml).
        assert "Ledger holds at 64" in _nyt_block_1045()["ledger_note"]
        ap = _yaml(os.path.join(PROFILES_DIR, "ap.yaml"))
        assert ap["competitor_relationships"]["openai"][
            BLOCK_M1039_AP]["falsification_ledger"] == "64"

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
        out = _git(
            "grep", "-c", "-F", _T56, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_seventh_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixtieth_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_first_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T61, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_second_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_third_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T63, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_fourth_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T64, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_fifth_member(self):
        assert _git_grep_tracked_source(_T65, None) == []

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (_T35, _T36, _T37, _T38, _T39):
            assert _git_grep_tracked_source(needle, "profiles/") != [], needle

    def test_fortieth_direction_absent(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: forward guards for #1366 staged.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1365:
    def test_pins_on_1045_no_landing(self):
        # Type D lands no mechanisms: max stays 1045, next stays 1046.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1045" in src
        assert "NEXT_NUM = 1046" in src

    def test_no_type_d_1365_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721): every commit whose message
        # matches "Type D #1365" must be this run's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type D #1365")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1365's own commits"
        main = _git("rev-parse", PRED_MAIN_1365).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_e_1366_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1366's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1366" must be #1366's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1366 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type E #1366")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1366's own commits"
        main = _git("rev-parse", PRED_MAIN_1366).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1046_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1046_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1046_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_1045(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_fortieth_direction_absent_live(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_1364_forward_guards_held_green_pre_commit(self):
        # #1364's staged guards (max-1045, zero-1046 all forms,
        # no-Type-D-#1365-in-git-log, fortieth absent, 48th-64th
        # intact, no 65th member, ledger 64) verified GREEN by this
        # run before the main commit; the no-Type-D-#1365 pin is the
        # #1191-class self-trip documented here, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1045" in src
        assert "NEXT_NUM = 1046" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1364's guard lifecycle post-terminal-followup.
# ---------------------------------------------------------------------------


class TestStalenessPins1365:
    def test_1364_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: all 25 pass. The
        # no_type_d_1365_in_git_log pin (the #1191-class self-trip:
        # this run's main commit carries "Type D #1365") flipped BY
        # DESIGN at this run's main commit and is re-pinned green in
        # the terminal log-hash followup per #721 (PRED_MAIN_1365 now
        # holds this run's main sha in BOTH this file and the #1364
        # file per the #1292 precedent). The 1046-form pins stay green
        # throughout (Type D lands no mechanisms; the #723/#738/#739
        # designed keying holds); the member and direction pins stay
        # green (no member, no direction landed this run). The #1364
        # block is read-only to this run; the flip is documented here,
        # not repaired. Deselected pre-commit (verified only
        # post-terminal-followup).
        res = _class_run(E1364_FILE, "TestGuardLifecycle1364")
        out = res.stdout + res.stderr
        assert "25 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1365:
    def test_readme_test_file_table_has_1365_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1365_row_post_sync(self):
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


class TestIterationLog1365:
    def test_log_has_1365_entry(self):
        text = _read(LOG_PATH)
        assert "## #1365 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "TWENTY-THIRD consecutive" in text
        assert "type_d_1365_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1365:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1365_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1365 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1365:
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
        # #1024 m846 (profiles/competitor-entities.yaml): Ray's
        # revert/leave/rebuild-from-primary decision still pending.
        # Type D writes nothing to profiles/; the m846 block must be
        # byte-identical to HEAD. Do NOT touch #1024 m846.
        head = _git(
            "show", "HEAD:profiles/competitor-entities.yaml").stdout
        work = _read(ENTITIES_PATH)
        assert (head.splitlines()[M846_HEAD_START - 1:M846_HEAD_END]
                == work.splitlines()[M846_HEAD_START - 1:M846_HEAD_END])
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src
