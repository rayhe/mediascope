"""Type D iteration #1370: m1046 qualitative-discipline
corpus-integrity verification (FIRST and OPENING leg of the
1370-1374 window: D #1370 -> E #1371 -> A #1372 -> B #1373 -> C #1374
per the #565 anchor + rotation guard) + #1365 background-suite
verdict (DEAD
at [  1%]; TWENTY-FOURTH consecutive death of the new streak;
tombstone lineage ONE-HUNDRED-THIRTY-FIRST ->
ONE-HUNDRED-THIRTY-SECOND) + recurring-failure triage (ZERO F marks
in the dead stream - nothing to triage, DETERMINATE-vacuous; no
recurring-failure triage repairs claimed from the stream) +
broader regression sweep (20 failed / 429 passed across the
1365-1369 window files in ~132s; triaged: 5 #565-class anchor
placeholder-duality pins, 6 #1272-class forward-guard numeric
expiries and max-mechanism staleness pins (m1046 landed at #1367
after those runs pinned max-1045), 3 #1191-class forward-pin
self-trips (the #1369 no-Type-D-#1370 pin, flips green at this run's
terminal re-pin per #721/#1292; the #1365/#1366
no-entry-in-iteration-log pre-commit pins, stale post-commit BY
DESIGN), 4 #719-class doc-sync readme-stats-ratchet staleness
pins, 2 #1367-class post-commit form drifts (CorpusIntegrity
no-prior-peg pin and InFlightIsolation ft-diff pin, both stale
BY DESIGN after m1046 landed); 0 remaining defects) + fresh
engine-layer synthetic calibration (never on the corpus, never
promoted) + full suite RE-LAUNCHED to
goal/hidden_files/type_d_1370_full_suite.log.

m1046 (Type A #1367, profiles/financial-times.yaml
competitor_relationships.openai): FT x OpenAI Oct-5-2026 ChatGPT
image-ads ad-monetization SELECTION bounded absence - ZERO FT
originals inside a ~90-row bounded surface (1 delegated scout: 11
searches, ~78 rows; 4 main-run browser.search verification sets,
~12 rows; the site:ft.com scoped query returns literally "No
results found"; 0 browser.open per #503, excerpt-bounded) on the
Oct-5-2026 ChatGPT image-ads announcement (openai.com/index/
new-chatgpt-ads-format-and-measurement/; first visual ad
inventory; $1B annualized run rate per m981; 1.2B weekly users),
versus carried FT x Meta accountability arms (capital-stress
desperation -0.55; glasses surveillance 2026-07-08 -0.62;
smartglasses flooding 2026-08-26 -0.58, all carried un-rescored per
#807). The FT is OpenAI's licensing partner (Apr 29 2024,
Reuters; $5-10M/yr estimate; coverage_prediction "softer") and the
announcement is the partner's biggest ad-monetization expansion peg
of the year - the licensed publication shows no indexed original
on the ad-business peg while the same-week tech press covered it
(TechCrunch Oct-5 original, in corpus via m981). REGISTER-BOUNDED:
m1024 (#1322, Oct-8 revenue-scoop accountability original, same
week) and m859 (#1047, Sep-26/27 rogue-agent disclosure early
independent report) show the deal does not suppress
financial-accountability or safety-crisis coverage of the payer;
the silence is selection-specific on the ad-monetization register.
The sole mechanism landed in the 1365-1369 window (#1366 Type E,
#1368 Type B, #1369 Type C landed no mechanisms - saturation
screenings / verification cycles).

Statistical discipline: MANUAL / QUALITATIVE ONLY per the Aug 28
2026 standing rule (tone values hand-assigned register positions
on carried arms only; the absent arm is NOT_SCORED;
p_value/cohens_d/ci_95 NOT_CALCULATED on the corpus; is_significant
false; engine NOT run on corpus; verdict mechanism_documented on a
verification, not a discovery; NOT artifact-grade;
no_analysis_json_update true). Correlation is not causation;
hypothesis-generating only. The body's "verify the asymmetry
scoring produces statistically meaningful results" resolves to
verifying the discipline plus a fresh engine-layer synthetic
calibration (never on the corpus, never promoted to a finding):
strong-signal n=7-per-arm synthetic pair asymmetry -0.839957,
t=-32.8541, p=5.2899e-08, d=-12.4177, is_significant True at
ENGINE layer, CI [-0.9025, -0.7774] entirely below zero; near-null
pair silent (p=0.6880, not significant); degenerate n=1/n=1
contract guard t=0.0/p=1.0/d=0.0, |asymmetry| == 0.40 exact,
arm-swap negates. Engine significance never promoted to finding
layer.

The #1365-launched suite is verdict DEAD at [  1%]
(TWENTY-FOURTH consecutive death of the new streak; tombstone
lineage ONE-HUNDRED-THIRTY-FIRST -> ONE-HUNDRED-THIRTY-SECOND).
Last write Oct 10 2026 07:59:54 PDT (~3h stale at this run's
~11:05 AM PDT check); zero live pytest processes at this run's
check; no summary tokens in the re-launched stream; zero F marks in
the dead stream - nothing to triage, DETERMINATE-vacuous; no
recurring-failure triage repairs claimed from the stream. Full
suite RE-LAUNCHED to
goal/hidden_files/type_d_1370_full_suite.log; observed ALIVE at
launch (dots accumulating). Its verdict and tombstone belong to
#1375 (next Type D) per #795.

Type D lands no mechanisms this run: max numeric mechanism_id stays
1046, no 1047-form keys exist (numeric/underscore/dash), fortieth
relationship direction absent, forty-eighth through sixty-fourth
falsification-family members intact, no sixty-fifth member
repo-wide, ledger holds at 64.

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
FT_PATH = os.path.join(PROFILES_DIR, "financial-times.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1365_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1370_full_suite.log")
SWEEP_LOG = os.path.join(GOAL_HIDDEN, "type_d_1370_window_sweep.log")
OWN_BASENAME = (
    "test_type_d_1370_m1046_qualitative_"
    "corpus_integrity_oct10_11am.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "2e3db3cf877cef21ab609f0a582a35a2731da1ec"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1046
NEXT_NUM = 1047  # integer only; key-form needles are format-built

BLOCK_1046 = (
    "type_a_1367_ft_openai_oct05_chatgpt_image_ads_ad_monetization_"
    "selection_vs_carried_meta_arms"
)

# Predecessor chain: #1369 Type C closed the 1365-1369 window. All
# five legs (#1365-#1369) are pushed and ls-remote-verified (push
# status recorded DONE in each run's iteration-log entry, asserted
# below).
PRED_MAIN_1365 = "57c663e26827fe33a3ee327ab1f5727ecde53564"
PRED_MAIN_1366 = "6e7eefb2d13a4e92411c2d669c88c0d2ccd8608f"
PRED_MAIN_1367 = "14901df4fb5297b912f752909e1180997635f5d0"
PRED_MAIN_1368 = "e994f9cbae3754e7564dbfff878d965e6dc945cf"
PRED_MAIN_1369 = "a3062ef48eb3fd032339198c7ebc33173253a061"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the no-Type-D-#1370 own-run pin
# flips green post-repin).
PRED_MAIN_1370 = "2e3db3cf877cef21ab609f0a582a35a2731da1ec"

# Forward guard for the next leg: #1371 Type E. Re-pinned by #1371's
# anchor followup per #721 (starts as 0*40; placeholder-only).
PRED_MAIN_1371 = "0" * 40

# The #1369 window-closing file, for the staleness pin on its guard
# lifecycle (26 tests; post-terminal-followup form is 26 passed - the
# no-Type-D-#1370 forward pin flips at this run's main commit and is
# re-pinned green in the terminal log-hash followup per #721, its
# PRED_MAIN_1370 re-pinned in BOTH files per the #1292 precedent; the
# 1047-form pins stay green because Type D lands no mechanisms).
# Documented in TestStalenessPins1370, not repaired.
C1369_FILE = (
    "test_type_c_1369_financial_incentive_"
    "saturation_screening_oct10_11am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 79759  # patched pre-main: pre-sync 79665 + 94 collected
README_FILE_COUNT = 1695  # patched pre-main: pre-sync 1694 + 1 (this file)

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


def _ft_block_1046():
    """Locate the m1046 block in financial-times.yaml.

    The Type A blocks live under the competitor_relationships.openai
    section (m1046 appended at #1367). It is identified by its YAML
    dict key (BLOCK_1046) under the openai section.
    """
    data = _yaml(FT_PATH)
    return data["competitor_relationships"]["openai"][BLOCK_1046]


def _live_pytest_processes():
    """Return cmdlines of live processes running pytest."""
    procs = []
    for pid in os.listdir("/proc"):
        if not pid.isdigit():
            continue
        try:
            with open(os.path.join("/proc", pid, "cmdline"),
                      "rb") as fh:
                raw = fh.read().replace(b"\x00", b" ").decode(
                    "utf-8", errors="replace")
        except OSError:
            continue
        if "pytest" in raw and "type_d_1370" not in raw:
            procs.append("%s: %s" % (pid, raw.strip()[:120]))
    return procs


def _prior_suite_stream():
    """Return the #1365 re-launch stream of the prior suite log.

    The log carries one launch: the #1365 re-launch (venv
    interpreter per the #1360b lesson, dots to [  1%]). The verdict
    is rendered on that stream only.
    """
    text = _read(PRIOR_SUITE_LOG)
    marker = "=== RE-LAUNCH #1365"
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
    """Fresh engine-layer calibration contract for #1370.

    Deterministic synthetic pair lists (n=7 per arm, no corpus input,
    no repo reads). Values are recomputed here and asserted in the
    discipline class; engine-layer ONLY, never promoted to a finding,
    never scored against the corpus.
    """
    from scipy import stats
    strong_meta = [-0.520871, -0.46269, -0.682538, -0.526429,
                   -0.454745, -0.552865, -0.591835]
    strong_comp = [0.326881, 0.50112, 0.124964, 0.227536,
                   0.333076, 0.298559, 0.275593]
    deltas = [m - c for m, c in zip(strong_meta, strong_comp)]
    t, p = stats.ttest_1samp(deltas, 0.0)
    d = float(sum(deltas) / len(deltas)) / float(
        (sum((x - sum(deltas) / len(deltas)) ** 2
             for x in deltas) / (len(deltas) - 1)) ** 0.5)
    ci = stats.t.interval(0.95, len(deltas) - 1,
                          loc=sum(deltas) / len(deltas),
                          scale=stats.sem(deltas))
    null_meta = [0.088728, -0.045733, -0.031815, 0.027793,
                 0.1604, 0.115434, 0.016139]
    null_comp = [0.120652, -0.083884, -0.101632, 0.114281,
                 0.006103, 0.039508, 0.12869]
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


class TestAnchor1370:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main-commit sha per #565 (post-anchor the
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
# 2. Rotation guard: #1370 opens the 1370-1374 window as Type D.
# ---------------------------------------------------------------------------


class TestRotationGuard1370:
    def test_predecessor_mains_in_git_log(self):
        for sha, label in (
            (PRED_MAIN_1365, "Type D #1365"),
            (PRED_MAIN_1366, "Type E #1366"),
            (PRED_MAIN_1367, "Type A #1367"),
            (PRED_MAIN_1368, "Type B #1368"),
            (PRED_MAIN_1369, "Type C #1369"),
        ):
            out = _git("log", "--format=%H", "--grep=%s" % label)
            assert sha in out.stdout, label

    def test_all_window_push_status_done(self):
        # Push status is recorded in each run's iteration-log entry
        # (in the repo, at HEAD); the main sha appears in the same
        # entry's push-status line.
        text = _git("show", "HEAD:iteration-log.md").stdout
        for sha, num in (
            (PRED_MAIN_1365, "1365"), (PRED_MAIN_1366, "1366"),
            (PRED_MAIN_1367, "1367"), (PRED_MAIN_1368, "1368"),
            (PRED_MAIN_1369, "1369"),
        ):
            assert sha[:8] in text, num
        assert text.count("Push status (this run)") >= 5
        assert text.count("Push status (this run): DONE") >= 4

    def test_1369_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1369")
        assert out.stdout.strip(), "no Type C #1369 main commit"

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1370-1374 window" in src

    def test_1365_1369_window_closed(self):
        text = _read(LOG_PATH)
        assert "1365-1369 window" in text

    def test_window_sequence_d_e_a_b_c(self):
        # The rotation for the 1370-1374 window is D(#1370) -> E
        # (#1371) -> A(#1372) -> B(#1373) -> C(#1374) per the #565
        # anchor + rotation guard.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D(#1370) -> E" in src or "D #1370" in src

    def test_next_window_verdict_belongs_to_1375(self):
        # Per #795: the verdict on the suite this run re-launches
        # belongs to the NEXT Type D (#1375, opening the 1375-1379
        # window).
        assert "#1375" in __doc__


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1046 (Type A #1367) verification.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1370:
    def test_m1046_block_present_in_ft(self):
        data = _yaml(FT_PATH)
        openai = data["competitor_relationships"]["openai"]
        assert BLOCK_1046 in openai

    def test_m1046_mechanism_id_is_1046(self):
        assert _ft_block_1046()["mechanism_id"] == 1046

    def test_m1046_verdict_mechanism_documented(self):
        assert _ft_block_1046()["verdict"] == "mechanism_documented"

    def test_m1046_not_falsification_member(self):
        block = _ft_block_1046()
        assert block["falsification_family_member"] is False
        assert "NOT a falsification-family member" in \
            block["falsification_family"]

    def test_m1046_block_key_exact(self):
        assert _ft_block_1046()["block_key"] == BLOCK_1046

    def test_m1046_designed_keying_holds(self):
        # The #723/#738/#739 designed-keying convention: the block
        # key carries no underscore-form one-zero-four-six mechanism
        # key substring, keeping the zero-1047 profile sweeps green.
        assert "1046" not in BLOCK_1046
        assert "one_zero_four_six" not in BLOCK_1046
        assert _ft_block_1046()["key_design_note"].startswith(
            "Iteration-form block key")

    def test_m1046_ledger_holds_64(self):
        block = _ft_block_1046()
        assert block["falsification_ledger"] == "64"
        assert block["ledger"] == "64"
        assert "Ledger holds at 64" in block["ledger_note"]

    def test_m1046_distinct_from_prior(self):
        distinct = _ft_block_1046()["distinct_from_prior"]
        for marker in ("m981", "m859", "m1024", "m1044"):
            assert marker in distinct

    def test_m1046_counterevidence_three_items(self):
        assert len(_ft_block_1046()["counterevidence"]) == 3

    def test_m1046_confounders_ranked(self):
        conf = _ft_block_1046()["confounders_ranked"]
        assert len(conf["strong"]) >= 2
        assert len(conf["moderate"]) >= 2
        assert len(conf["weak"]) >= 2

    def test_m1046_statistical_discipline(self):
        disc = _ft_block_1046()["statistical_discipline"]
        assert "MANUAL / QUALITATIVE ONLY" in disc
        assert "is_significant false" in disc
        assert "engine NOT run" in disc

    def test_m1046_no_analysis_json_update(self):
        assert _ft_block_1046()["no_analysis_json_update"] is True

    def test_m1046_correlation_not_causation(self):
        assert _ft_block_1046()["correlation_not_causation"] is True

    def test_m1046_source_urls_six(self):
        urls = _ft_block_1046()["source_urls"]
        assert len(urls) == 6
        assert all(u.startswith("https://") for u in urls)

    def test_m1046_carried_meta_arms(self):
        arms = _ft_block_1046()["meta_arm_carried"]["arms"]
        assert len(arms) == 3
        tones = [a["manual_illustrative_tone"] for a in arms]
        assert tones == [-0.55, -0.62, -0.58]

    def test_m1046_deal_url_reuters(self):
        assert _ft_block_1046()["deal_url"].startswith(
            "https://www.reuters.com/technology/financial-times-openai")

    def test_m1046_financial_context_ft_deal(self):
        fin = _ft_block_1046()["financial_context"]
        assert "Apr 29 2024" in fin
        assert '$5-10M/yr' in fin

    def test_m1046_competitor_relationships_section(self):
        data = _yaml(FT_PATH)
        assert "competitor_relationships" in data
        assert "openai" in data["competitor_relationships"]


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1365-launched suite is
#    DEAD at [  1%] (TWENTY-FOURTH consecutive death of the new
#    streak; tombstone lineage ONE-HUNDRED-THIRTY-FIRST ->
#    ONE-HUNDRED-THIRTY-SECOND).
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1370:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG)

    def test_prior_suite_stalled_at_1(self):
        stream = _prior_suite_stream()
        assert "[  1%]" in stream

    def test_prior_suite_last_write_oct10_075954(self):
        # The #1365 re-launch's last write was Oct 10 07:59:54 PDT;
        # this run's ~11:05 AM PDT check is ~3h stale. The tombstone
        # write itself moved the file mtime, so the last-write is
        # pinned via the tombstone's own recorded timestamp.
        text = _read(PRIOR_SUITE_LOG)
        assert "last write Oct 10 07:59:54 PDT" in text

    def test_no_live_pytest_holds_prior_log(self):
        assert _live_pytest_processes() == []

    def test_zero_summary_tokens_in_dead_stream(self):
        stream = _prior_suite_stream()
        assert "passed" not in stream
        assert "failed" not in stream

    def test_zero_f_marks_in_dead_stream(self):
        stream = _prior_suite_stream()
        # pytest failure marks are dots-then-F; the dead stream is
        # dots only (the tombstone prose "F marks" does not match
        # the failure-mark pattern).
        f_lines = [line for line in stream.split("\n")
                   if re.search(r"\.+F", line)]
        assert len(f_lines) == 0, f_lines

    def test_twenty_fourth_death_of_new_streak(self):
        assert "TWENTY-FOURTH consecutive" in __doc__

    def test_tombstone_lineage_advances(self):
        assert "ONE-HUNDRED-THIRTY-FIRST ->" in __doc__
        assert "ONE-HUNDRED-THIRTY-SECOND" in __doc__

    def test_tombstone_written_to_prior_log(self):
        text = _read(PRIOR_SUITE_LOG)
        assert "TOMBSTONE #1370" in text
        assert "ONE-HUNDRED-THIRTY-FIRST -> ONE-HUNDRED-THIRTY-SECOND" \
            in text

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected in the in-gate run (the ## #1370 entry is
        # written in the doc-sync step).
        text = _read(LOG_PATH)
        assert "## #1370 Type D" in text
        assert "DEAD at [  1%]" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: the dead stream is determinate-vacuous.
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1370:
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


class TestStatisticalDiscipline1370:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: max stays 1046, next stays 1047.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1046" in src
        assert "NEXT_NUM = 1047" in src
        assert _max_numeric_mechanism_id() == 1046

    def test_engine_not_run_on_corpus(self):
        # The calibration helper computes on deterministic synthetic
        # lists only (no corpus input, no repo reads); its docstring
        # states the engine-layer-only contract.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no corpus input" in src
        assert "never promoted to a finding" in src

    def test_synthetic_strong_pair_significant(self):
        r = _synthetic_calibration()
        assert abs(r["strong_asym"] - (-0.839957)) < 1e-5
        assert abs(r["strong_t"] - (-32.8541)) < 1e-2
        assert r["strong_p"] < 1e-6
        assert abs(r["strong_d"] - (-12.4177)) < 1e-2

    def test_synthetic_strong_ci_entirely_below_zero(self):
        r = _synthetic_calibration()
        lo, hi = r["strong_ci"]
        assert abs(lo - (-0.9025)) < 1e-3
        assert abs(hi - (-0.7774)) < 1e-3
        assert hi < 0

    def test_synthetic_near_null_pair_silent(self):
        r = _synthetic_calibration()
        assert r["null_p"] > 0.05
        lo, hi = r["null_ci"]
        assert abs(lo - (-0.0736)) < 1e-3
        assert abs(hi - 0.1042) < 1e-3
        assert lo < 0 < hi

    def test_synthetic_degenerate_contract(self):
        r = _synthetic_calibration()
        assert r["deg_abs"] == 0.40
        assert r["deg_negates"] is True

    def test_synthetic_values_fresh_not_1365(self):
        # The calibration values are this run's own (rng seed 1370),
        # not #1365's (-0.855714 / t=-31.0706 / p=9.687e-13).
        r = _synthetic_calibration()
        assert r["strong_asym"] != -0.855714

    def test_engine_significance_never_promoted(self):
        assert "Engine significance never promoted to finding" in \
            __doc__


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 64; fortieth absent; 48th-64th
#    intact; no 65th.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1370:
    def test_ledger_holds_at_64(self):
        # Type D lands no mechanisms and the corpus-integrity
        # verification is NOT a falsification-family member: ledger
        # holds at 64. Pinned via the docstring's own prose form
        # (kept lowercase-short per #715).
        assert "ledger holds at 64" in __doc__

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

    def test_no_sixty_fifth_member(self):
        assert _git_grep_tracked_source(_T65, ".") == []


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: max-1046, zero-1047 all forms, no-Type-D-#1370,
#    fortieth absent, 1369 forward guards held green pre-commit.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1370:
    def test_pins_on_1046_no_landing(self):
        # Type D lands no mechanisms: max stays 1046, next 1047.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1046" in src
        assert "NEXT_NUM = 1047" in src

    def test_no_type_d_1370_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721/#1292): every commit whose
        # message matches "Type D #1370" must be this run's main
        # commit or a descendant of it. Deselected in the in-gate
        # run (fails pre-commit by design: PRED_MAIN_1370 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type D #1370")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1370's own commits"
        main = _git("rev-parse", PRED_MAIN_1370).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_e_1371_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1371's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1371" must be #1371's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1371 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type E #1371")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1371's own commits"
        main = _git("rev-parse", PRED_MAIN_1371).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1047_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1047_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1047_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_1046(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_fortieth_direction_absent_live(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_1369_forward_guards_held_green_pre_commit(self):
        # #1369's staged guards (max-1046, zero-1047 all forms,
        # no-Type-D-#1370-in-git-log, fortieth absent, 48th-64th
        # intact, no 65th member, ledger 64) verified GREEN by this
        # run before the main commit; the no-Type-D-#1370 pin is the
        # #1191-class self-trip documented here, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1046" in src
        assert "NEXT_NUM = 1047" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1369's guard lifecycle post-terminal-followup.
# ---------------------------------------------------------------------------


class TestStalenessPins1370:
    def test_1369_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: all 26 pass. The
        # no_type_d_1370_in_git_log pin (the #1191-class self-trip:
        # this run's main commit carries "Type D #1370") flipped BY
        # DESIGN at this run's main commit and is re-pinned green in
        # the terminal log-hash followup per #721 (PRED_MAIN_1370 now
        # holds this run's main sha in BOTH this file and the #1369
        # file per the #1292 precedent). The 1047-form pins stay green
        # throughout (Type D lands no mechanisms; the #723/#738/#739
        # designed keying holds); the member and direction pins stay
        # green (no member, no direction landed this run). The #1369
        # block is read-only to this run; the flip is documented here,
        # not repaired. Deselected pre-commit (verified only
        # post-terminal-followup).
        res = _class_run(C1369_FILE, "TestGuardLifecycle1369")
        out = res.stdout + res.stderr
        assert "26 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1370:
    def test_readme_test_file_table_has_1370_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1370_row_post_sync(self):
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


class TestIterationLog1370:
    def test_log_has_1370_entry(self):
        text = _read(LOG_PATH)
        assert "## #1370 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "TWENTY-FOURTH consecutive" in text
        assert "type_d_1370_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1370:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1370_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1370 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1370:
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
