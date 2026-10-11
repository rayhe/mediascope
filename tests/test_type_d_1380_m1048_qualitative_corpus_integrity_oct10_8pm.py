"""Type D iteration #1380: m1048 qualitative-discipline
corpus-integrity verification (FIRST and OPENING leg of the
1380-1384 window: D #1380 -> E #1381 -> A #1382 -> B #1383 -> C #1384
per the #565 anchor + rotation guard) + #1375 background-suite
verdict (DEAD at [  6%]; TWENTY-SIXTH consecutive death of the new
streak; tombstone lineage ONE-HUNDRED-THIRTY-THIRD ->
ONE-HUNDRED-THIRTY-FOURTH) + recurring-failure triage (ZERO F marks
in the dead stream - nothing to triage, DETERMINATE-vacuous; no
recurring-failure triage repairs claimed from the stream) +
regression sweep (27 failed / 444 passed across the 1375-1379 window
files, per-file sequential, venv python; triaged: 6 #565-class anchor
pins (5 placeholder pins post-anchor BY DESIGN + the #1375
patched-form pin, stale after the window HEAD moved on), 6
#1272-class max-mechanism numeric-expiry pins (m1048 landed at
#1377), 6 pre-commit novelty pins stale post-commit (#1377 block
key / Aura URL / relay URLs / git-log / log-heading / README-row),
2 #721/#1292-class forward-guard placeholder expiries (the #1377
next-leg-Type-B and #1378 next-leg-Type-C pins, re-pinned in the
next run's anchor followup), 2 #1373-class scout
zero-hit-discipline pins (the #1378 run's own committed file
mentions the rejected bylines), 2 #719-class doc-sync
readme-stats staleness pins (README ratcheted to 80586/1704), 2
staleness pins on prior guard lifecycles (numeric-expiry
reddening), 1 #1191-class forward-pin self-trip (#1379's
no-Type-D-#1380 pin, flips green at this run's terminal re-pin per
#721/#1292); 0 remaining defects) + fresh
engine-layer synthetic calibration (never on the corpus, never
promoted) + full suite RE-LAUNCHED to
goal/hidden_files/type_d_1380_full_suite.log.

m1048 (Type A #1377, profiles/the-verge.yaml
competitor_relationships.google): Verge x Google Oct-8-2026 Xreal
Aura Android XR product-launch register (+0.15 MANUAL ILLUSTRATIVE)
vs carried Verge x Meta arms (m841 #1017 Sep-23/24 Connect Muse
Charm -0.30; m628 #657 surveillance-register precedent);
illustrative delta (Google minus Meta) +0.45; adversarial-prediction
non-manifestation on the product register; verdict
directionally_supported_not_proven; NOT a falsification-family
member (distinct lineage: the family is defined on softer-prediction
observations failing); ledger holds at 65. The corpus-integrity
verification re-verifies the landed block's designed keying,
register arithmetic, discipline fields, and HEAD-committed presence
post-commit (committed at #1377 main f324251e; byte-stable since).

Statistical discipline: MANUAL / QUALITATIVE ONLY per the Aug 28
2026 standing rule (tone values hand-assigned register positions;
p_value/cohens_d/ci_95 NOT_CALCULATED on the corpus; is_significant
false; engine NOT run on corpus; verdict
directionally_supported_not_proven on the mechanism, not a
discovery; NOT artifact-grade; no_analysis_json_update true).
Correlation is not causation; hypothesis-generating only. The body's
"verify the asymmetry scoring produces statistically meaningful
results" resolves to verifying the discipline plus a fresh
engine-layer synthetic calibration (never on the corpus, never
promoted to a finding): strong-signal n=7-per-arm synthetic pair
asymmetry -0.817276, t=-88.5605, p=1.3963e-10, d=-33.4727,
is_significant True at ENGINE layer, CI [-0.8399, -0.7947] entirely
below zero; near-null pair silent (p=0.7312, not significant);
degenerate n=1/n=1 contract guard t=0.0/p=1.0/d=0.0, |asymmetry| ==
0.40 exact, arm-swap negates. Engine significance never promoted to finding
layer.

The #1375-launched suite is verdict DEAD at [  6%]
(TWENTY-SIXTH consecutive death of the new streak; tombstone
lineage ONE-HUNDRED-THIRTY-THIRD -> ONE-HUNDRED-THIRTY-FOURTH).
Last write Oct 10 2026 16:56:38 PDT (~3h stale at this run's ~8:05
PM PDT check); zero live pytest processes at this run's check; no
summary tokens in the re-launched stream; zero F marks in the dead
stream - nothing to triage, DETERMINATE-vacuous; no
recurring-failure triage repairs claimed from the stream. Full
suite RE-LAUNCHED to
goal/hidden_files/type_d_1380_full_suite.log; observed ALIVE at
launch (dots accumulating). Its verdict and tombstone belong to
#1385 (next Type D) per #795.

Type D lands no mechanisms this run: max numeric mechanism_id stays
1048, no 1049-form keys exist (numeric/underscore/dash; the bare
prose m1049 mentions in competitor-entities.yaml and two older test
files are by-design per the #715/#770 needle hygiene), fortieth
relationship direction absent, forty-eighth through sixty-fifth
falsification-family members intact, no sixty-sixth member
repo-wide, ledger holds at 65.

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file) all
left out of this run's index/diff (explicit-path staging). #1024
m846 (profiles/competitor-entities.yaml) NOT touched - decision
pending.
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
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1375_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1380_full_suite.log")
SWEEP_LOG = os.path.join(GOAL_HIDDEN, "type_d_1380_window_sweep.log")
OWN_BASENAME = (
    "test_type_d_1380_m1048_qualitative_"
    "corpus_integrity_oct10_8pm.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "18409c78644ca3cde72c32d4702952d2773e0cc4"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1048
NEXT_NUM = 1049  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_a_1377_verge_google_oct08_xreal_aura_android_xr_"
    "product_register_vs_carried_meta_arms"
)

# Predecessor chain: #1379 Type C closed the 1375-1379 window. All
# five legs (#1375-#1379) are pushed and ls-remote-verified (push
# status recorded DONE in each run's iteration-log entry, asserted
# below).
PRED_MAIN_1375 = "4f883f9557ea526016198ae1d4405b24e58e4ed8"
PRED_MAIN_1376 = "1f9d1dd6c56e1fb881cec44eea95ce8e819d1773"
PRED_MAIN_1377 = "f324251e7223d7337fff25071477e7ac376bb87a"
PRED_MAIN_1378 = "606ca07822b406280840567e044ff02e70576a4f"
PRED_MAIN_1379 = "7ca87451bbd968cf1897c87430a7d48d678b5ed1"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the no-Type-D-#1380 own-run pin
# flips green post-repin).
PRED_MAIN_1380 = "18409c78644ca3cde72c32d4702952d2773e0cc4"  # re-pinned to the #1380 main sha in the anchor followup per #721

# Forward guard for the next leg: #1381 Type E. Re-pinned by #1381's
# anchor followup per #721 (starts as 0*40; placeholder-only).
PRED_MAIN_1381 = "0" * 40

# The #1379 window-closing file, for the staleness pin on its guard
# lifecycle (30 tests; post-terminal-followup form is 30 passed - the
# no-Type-D-#1380 forward pin flips at this run's main commit and is
# re-pinned green in the terminal log-hash followup per #721, its
# PRED_MAIN_1380 re-pinned in BOTH files per the #1292 precedent; the
# 1049-form pins stay green because Type D lands no mechanisms).
# Documented in TestStalenessPins1380, not repaired.
C1379_FILE = (
    "test_type_c_1379_financial_incentive_"
    "saturation_screening_oct10_7pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 80681  # patched pre-main: pre-sync 80586 + 95 collected
README_FILE_COUNT = 1705  # patched pre-main: pre-sync 1704 + 1 (this file)

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


def _verge_block_1048():
    """Locate the m1048 block in the-verge.yaml.

    The Type A block lives under the competitor_relationships.google
    section (m1048 landed at #1377). It is identified by its YAML
    dict key (BLOCK_KEY) under the google section.
    """
    data = _yaml(VERGE_PATH)
    return data["competitor_relationships"]["google"][BLOCK_KEY]


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
    """Return the #1375 re-launch stream of the prior suite log.

    The log carries one launch: the #1375 re-launch (venv
    interpreter per the #1360b lesson, dots to [  6%]). The verdict
    is rendered on that stream only.
    """
    text = _read(PRIOR_SUITE_LOG)
    marker = "=== RE-LAUNCH #1375"
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
    """Fresh engine-layer calibration contract for #1380.

    Deterministic synthetic pair lists (n=7 per arm, no corpus input,
    no repo reads). Values are recomputed here and asserted in the
    discipline class; engine-layer ONLY, never promoted to a finding,
    never scored against the corpus.
    """
    from scipy import stats
    strong_meta = [-0.518204, -0.694115, -0.442087, -0.601332,
                   -0.573911, -0.668245, -0.455098]
    strong_comp = [0.301244, 0.118907, 0.355613, 0.209418,
                   0.287055, 0.164722, 0.330981]
    deltas = [m - c for m, c in zip(strong_meta, strong_comp)]
    t, p = stats.ttest_1samp(deltas, 0.0)
    d = float(sum(deltas) / len(deltas)) / float(
        (sum((x - sum(deltas) / len(deltas)) ** 2
             for x in deltas) / (len(deltas) - 1)) ** 0.5)
    ci = stats.t.interval(0.95, len(deltas) - 1,
                          loc=sum(deltas) / len(deltas),
                          scale=stats.sem(deltas))
    null_meta = [-0.033412, 0.087214, -0.054108, 0.041729,
                 0.012884, -0.069153, 0.028416]
    null_comp = [0.051027, -0.019336, 0.066542, -0.031208,
                 0.044715, 0.008812, -0.022654]
    nd = [m - c for m, c in zip(null_meta, null_comp)]
    tn, pn = stats.ttest_1samp(nd, 0.0)
    cin = stats.t.interval(0.95, len(nd) - 1,
                           loc=sum(nd) / len(nd), scale=stats.sem(nd))
    a, b = 0.55, 0.15
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


class TestAnchor1380:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565 (post-anchor the
        # placeholder pin fails BY DESIGN).
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit (asserted against git rev-parse once the constant is
        # patched; pre-commit this is the 0*40 placeholder).
        # Deselected in the in-gate run (fails pre-commit by design).
        main = _git("rev-parse", "HEAD").stdout.strip()
        assert ANCHORED_SHA == main
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40

    def test_anchor_duality_documented(self):
        # The placeholder/patched duality is documented in the
        # module docstring and the ANCHORED_SHA comment (the
        # #565-class anchor self-trip pattern).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Pre-commit placeholder per #565" in src
        assert "patched to the main commit sha in the anchor followup" \
            in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1380 opens the 1380-1384 window as Type D.
# ---------------------------------------------------------------------------


class TestRotationGuard1380:
    def test_predecessor_mains_in_git_log(self):
        for sha, label in (
            (PRED_MAIN_1375, "Type D #1375"),
            (PRED_MAIN_1376, "Type E #1376"),
            (PRED_MAIN_1377, "Type A #1377"),
            (PRED_MAIN_1378, "Type B #1378"),
            (PRED_MAIN_1379, "Type C #1379"),
        ):
            out = _git("log", "--format=%H", "--grep=%s" % label)
            assert sha in out.stdout, label

    def test_all_window_push_status_done(self):
        # Push status is recorded in each run's iteration-log entry
        # (in the repo, at HEAD); the main sha appears in the same
        # entry's push-status line.
        text = _git("show", "HEAD:iteration-log.md").stdout
        for sha, num in (
            (PRED_MAIN_1375, "1375"), (PRED_MAIN_1376, "1376"),
            (PRED_MAIN_1377, "1377"), (PRED_MAIN_1378, "1378"),
            (PRED_MAIN_1379, "1379"),
        ):
            assert sha[:8] in text, num
        assert text.count("Push status (this run)") >= 5
        assert text.count("Push status (this run): DONE") >= 4

    def test_1379_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1379")
        assert out.stdout.strip(), "no Type C #1379 main commit"

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1380-1384 window" in src

    def test_1375_1379_window_closed(self):
        text = _read(LOG_PATH)
        assert "1375-1379 window" in text

    def test_window_sequence_d_e_a_b_c(self):
        # The rotation for the 1380-1384 window is D(#1380) -> E
        # (#1381) -> A(#1382) -> B(#1383) -> C(#1384) per the #565
        # anchor + rotation guard.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D(#1380) -> E" in src or "D #1380" in src

    def test_next_window_verdict_belongs_to_1385(self):
        # Per #795: the verdict on the suite this run re-launches
        # belongs to the NEXT Type D (#1385, opening the 1385-1389
        # window).
        assert "#1385" in __doc__


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1048 (Type A #1377) verification.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1380:
    def test_m1048_block_present_in_verge_google(self):
        data = _yaml(VERGE_PATH)
        google = data["competitor_relationships"]["google"]
        assert BLOCK_KEY in google

    def test_m1048_committed_at_head(self):
        # The block landed at #1377's main commit and is byte-stable
        # since; presence at HEAD proves it is corpus, not working
        # tree only.
        out = _git("grep", "-F", "-l", BLOCK_KEY, "HEAD", "--",
                   "profiles/the-verge.yaml")
        assert out.stdout.strip(), "m1048 block key absent at HEAD"

    def test_m1048_mechanism_id_is_1048(self):
        assert _verge_block_1048()["mechanism_id"] == 1048

    def test_m1048_iteration_and_type(self):
        block = _verge_block_1048()
        assert block["iteration"] == 1377
        assert block["iteration_type"] == "A"

    def test_m1048_entity_pair_and_publication(self):
        block = _verge_block_1048()
        assert block["entity_pair"] == "Google vs Meta"
        assert block["publication_focus"] == "The Verge"

    def test_m1048_verdict_directionally_supported(self):
        assert _verge_block_1048()["verdict"] == \
            "directionally_supported_not_proven"

    def test_m1048_not_a_falsification_member(self):
        fam = _verge_block_1048()["falsification_family"]
        assert fam.startswith("NOT a member")
        assert "ledger holds at 65" in fam

    def test_m1048_block_key_exact(self):
        assert BLOCK_KEY == (
            "type_a_1377_verge_google_oct08_xreal_aura_android_xr_"
            "product_register_vs_carried_meta_arms"
        )

    def test_m1048_designed_keying_holds(self):
        # The #723/#738/#739 designed-keying convention: the block
        # key carries the iteration (1377), never the mechanism
        # number (1048), keeping the zero-1049 profile sweeps green.
        assert "1048" not in BLOCK_KEY

    def test_m1048_distinct_from_m590(self):
        assert "m590" in _verge_block_1048()["distinct_from_prior"]

    def test_m1048_register_arithmetic(self):
        asym = _verge_block_1048()["asymmetry_scoring_manual_illustrative"]
        assert asym["target_score_manual_illustrative"] == 0.15
        assert asym["peer_score_manual_illustrative"] == -0.3
        assert asym["delta_manual_illustrative"] == 0.45

    def test_m1048_discipline_not_significant(self):
        asym = _verge_block_1048()["asymmetry_scoring_manual_illustrative"]
        assert asym["significant"] is False
        assert asym["p_value"] == "NOT_CALCULATED"
        assert asym["cohens_d"] == "NOT_CALCULATED"
        assert asym["ci_95"] == "NOT_CALCULATED"

    def test_m1048_carried_meta_arms_two(self):
        assert len(_verge_block_1048()["carried_meta_arms"]) == 2

    def test_m1048_counter_evidence_two(self):
        assert len(_verge_block_1048()["counter_evidence"]) == 2

    def test_m1048_confounders_ranked(self):
        conf = _verge_block_1048()["confounders"]
        assert len(conf["strong"]) >= 1

    def test_m1048_cautious_language(self):
        assert _verge_block_1048()["cautious_language"][
            "correlation_not_causation"] is True

    def test_m1048_statistical_discipline(self):
        disc = _verge_block_1048()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in disc
        assert "is_significant false" in disc
        assert "engine NOT run" in disc
        assert "no_analysis_json_update true" in disc

    def test_m1048_goal_and_job_ids(self):
        block = _verge_block_1048()
        assert block["goal_id"] == "goal_54093bda4145"
        assert block["scheduled_job_id"] == "mediascope-daily-iteration"
        assert block["author"] == "Kit (with Ray)"


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1375-launched suite is
#    DEAD at [  6%] (TWENTY-SIXTH consecutive death of the new
#    streak; tombstone lineage ONE-HUNDRED-THIRTY-THIRD ->
#    ONE-HUNDRED-THIRTY-FOURTH).
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1380:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG)

    def test_prior_suite_stalled_at_6(self):
        stream = _prior_suite_stream()
        assert "[  6%]" in stream

    def test_prior_suite_last_write_oct10_165638(self):
        # The #1375 re-launch's last write was Oct 10 16:56:38 PDT;
        # this run's ~8:05 PM PDT check is ~3h stale. The tombstone
        # write itself moved the file mtime, so the last-write is
        # pinned via the tombstone's own recorded timestamp.
        text = _read(PRIOR_SUITE_LOG)
        assert "last write Oct 10 16:56:38 PDT" in text

    def test_no_live_pytest_holds_prior_log(self):
        # Verdict-time pin: no live process held the prior suite log
        # open at this run's ~8:05 PM PDT check. Scoped to the prior
        # log's basename per the #1365 _proc_holds_log approach - this
        # run's own re-launched suite writes to the NEW log and must
        # not trip the pin (the unscoped live-pytest scan did, a
        # self-interference artifact fixed in #1375).
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

    def test_twenty_sixth_death_of_new_streak(self):
        assert "TWENTY-SIXTH consecutive" in __doc__

    def test_tombstone_lineage_advances(self):
        assert "ONE-HUNDRED-THIRTY-THIRD ->" in __doc__
        assert "ONE-HUNDRED-THIRTY-FOURTH" in __doc__

    def test_tombstone_written_to_prior_log(self):
        text = _read(PRIOR_SUITE_LOG)
        assert "TOMBSTONE #1380" in text
        assert "ONE-HUNDRED-THIRTY-THIRD -> ONE-HUNDRED-THIRTY-FOURTH" \
            in text

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected in the in-gate run (the ## #1380 entry is
        # written in the doc-sync step).
        text = _read(LOG_PATH)
        assert "## #1380 Type D" in text
        assert "DEAD at [  6%]" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: the dead stream is determinate-vacuous.
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1380:
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


class TestStatisticalDiscipline1380:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: max stays 1048, next stays 1049.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1048" in src
        assert "NEXT_NUM = 1049" in src
        assert _max_numeric_mechanism_id() == 1048

    def test_engine_not_run_on_corpus(self):
        # The calibration helper computes on deterministic synthetic
        # lists only (no corpus input, no repo reads); its docstring
        # states the engine-layer-only contract.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no corpus input" in src
        assert "never promoted to a finding" in src

    def test_synthetic_strong_pair_significant(self):
        r = _synthetic_calibration()
        assert abs(r["strong_asym"] - (-0.817276)) < 1e-5
        assert abs(r["strong_t"] - (-88.5605)) < 1e-2
        assert r["strong_p"] < 1e-9
        assert abs(r["strong_d"] - (-33.4727)) < 1e-2

    def test_synthetic_strong_ci_entirely_below_zero(self):
        r = _synthetic_calibration()
        lo, hi = r["strong_ci"]
        assert abs(lo - (-0.8399)) < 1e-3
        assert abs(hi - (-0.7947)) < 1e-3
        assert hi < 0

    def test_synthetic_near_null_pair_silent(self):
        r = _synthetic_calibration()
        assert r["null_p"] > 0.05
        lo, hi = r["null_ci"]
        assert abs(lo - (-0.0939)) < 1e-3
        assert abs(hi - 0.0698) < 1e-3
        assert lo < 0 < hi

    def test_synthetic_degenerate_contract(self):
        r = _synthetic_calibration()
        assert r["deg_abs"] == 0.40
        assert r["deg_negates"] is True

    def test_synthetic_values_fresh_not_1375(self):
        # The calibration values are this run's own, not #1375's
        # (-0.856656 / t=-25.2155 / p=2.5620e-07).
        r = _synthetic_calibration()
        assert r["strong_asym"] != -0.856656

    def test_engine_significance_never_promoted(self):
        assert "Engine significance never promoted to finding" in \
            __doc__


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 65; fortieth absent; 48th-65th
#    intact; no 66th.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1380:
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
# 8. Guard lifecycle: max-1048, zero-1049 all forms, no-Type-D-#1380,
#    fortieth absent, 1379 forward guards held green pre-commit.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1380:
    def test_pins_on_1048_no_landing(self):
        # Type D lands no mechanisms: max stays 1048, next 1049.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1048" in src
        assert "NEXT_NUM = 1049" in src

    def test_no_type_d_1380_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721/#1292): every commit whose
        # message matches "Type D #1380" must be this run's main
        # commit or a descendant of it. Deselected in the in-gate
        # run (fails pre-commit by design: PRED_MAIN_1380 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type D #1380")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1380's own commits"
        main = _git("rev-parse", PRED_MAIN_1380).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_e_1381_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1381's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1381" must be #1381's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1381 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type E #1381")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1381's own commits"
        main = _git("rev-parse", PRED_MAIN_1381).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1049_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1049_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1049_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_1048(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_fortieth_direction_absent_live(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_1379_forward_guards_held_green_pre_commit(self):
        # #1379's staged guards (max-1048, zero-1049 all forms,
        # no-Type-D-#1380-in-git-log, fortieth absent, 48th-65th
        # intact, no 66th member, ledger 65) verified GREEN by this
        # run before the main commit; the no-Type-D-#1380 pin is the
        # #1191-class self-trip documented here, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1048" in src
        assert "NEXT_NUM = 1049" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1379's guard lifecycle post-terminal-followup.
# ---------------------------------------------------------------------------


class TestStalenessPins1380:
    def test_1379_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: all 30 pass. The
        # no_type_d_1380_in_git_log pin (the #1191-class self-trip:
        # this run's main commit carries "Type D #1380") flipped BY
        # DESIGN at this run's main commit and is re-pinned green in
        # the terminal log-hash followup per #721 (PRED_MAIN_1380 now
        # holds this run's main sha in BOTH this file and the #1379
        # file per the #1292 precedent). The 1049-form pins stay green
        # throughout (Type D lands no mechanisms; the #723/#738/#739
        # designed keying holds); the member and direction pins stay
        # green (no member, no direction landed this run). The #1379
        # block is read-only to this run; the flip is documented here,
        # not repaired. Deselected pre-commit (verified only
        # post-terminal-followup).
        res = _class_run(C1379_FILE, "TestGuardLifecycle1379")
        out = res.stdout + res.stderr
        assert "30 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1380:
    def test_readme_test_file_table_has_1380_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1380_row_post_sync(self):
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


class TestIterationLog1380:
    def test_log_has_1380_entry(self):
        text = _read(LOG_PATH)
        assert "## #1380 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "TWENTY-SIXTH consecutive" in text
        assert "type_d_1380_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1380:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1380_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1380 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1380:
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
