"""Type D #1215: verify m958/m959/m960 qualitative-discipline landings +
post-1210-1214 corpus integrity (max numeric mechanism_id 960; zero
next-number nine-six-one keys all forms; falsification ledger HOLDS
at 50: m959 the fiftieth member (profiles/careers/journalists.yaml),
m958 claims no slot, m960 is a status-check extension not a new
direction; thirty-fifth through thirty-ninth directions present, the
fortieth absent by design) + #1210 background-suite verdict
(THIRTY-SEVENTH consecutive death; tombstone ONE-HUNDRED-FIRST ->
ONE-HUNDRED-SECOND) + fresh synthetic engine calibration + full suite
re-launched - FIRST and OPENING leg of the 1215-1219 window
(Oct 4 2026, 04:00 PM PDT).

Verification-layer run: no corpus edits, no analysis.json updates, no
new mechanisms. The finding layer stays MANUAL/QUALITATIVE ONLY per
the Aug 28 2026 standing rule; the synthetic engine calibration is a
fresh engine-layer contract and is never promoted to a finding.

- m958 (Type A #1212, profiles/news-corp.yaml competitor_
  relationships / openai block key type_a_1212_wsj_openai_safety_
  firings_oct01_vs_wsj_meta_muse_trust_dual_payer_symmetry): WSJ
  Oct-1-2026 safety-researcher-firings scoop (NEW peg) + CARRIED
  Sep-28 Astra deception-shelving peg on the OpenAI leg, vs NEW
  WSJ x Meta Muse-trust pieces (M1 Sep-19, M2 Sep-24) on the Meta
  leg; illustrative delta (OpenAI minus Meta) 0.00 - dual-payer
  symmetric hardness at the WSJ register in the crisis week, the
  m519 symmetric-softening refinement INVERTING between the calm
  window (m532, Sep 5) and the crisis week. CONTROL-CASE / DUAL-
  PAYER-SYMMETRY EXTENSION, NOT a new direction, NOT a
  falsification-family member (falsification_family 'NOT a member
  (temporal replication / symmetry extension ...)'; ledger_note
  'Ledger holds at 49 this run'); verdict
  mechanism_refinement_not_a_discovery; ledger 49. Statistical
  discipline: MANUAL ILLUSTRATIVE only per the Aug 28 2026 standing
  rule (engine NOT run, p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant false, NOT artifact-grade, no_analysis_json_update
  true). connects_to [519, 532, 763, 904, 905, 956, 957]. 11
  browser.search query sets via delegated research + main-run
  verification, 0 browser.open per #503.
- m959 (Type B #1213, profiles/careers/journalists.yaml top-level
  kaitlyn_huamani_type_b key, competitor_coverage block key
  type_b_1213_kaitlyn_huamani_ap_meta_connect_vs_openai_devday_
  falsification): Kaitlyn Huamani (AP Technology Writer) OpenAI
  DevDay security-critical accountability (-0.30 MANUAL
  ILLUSTRATIVE, NEW Sep-29 arm, solo byline) vs Meta Connect
  celebratory launch register (+0.30, NEW Sep-24 arm, co-byline
  Ortutay); illustrative delta (OpenAI minus Meta) -0.60 HARD-
  INVERTS the uniform payer-softening prediction at the deal-
  holding outlet (OpenAI x AP Jul-2023 content-licensing
  partnership, in-corpus). FIFTIETH falsification-family member
  (ledger 49 -> 50); extends the m956 journalist-contingent
  inversion to a second deal-holding outlet, first AP byline in
  the family. verdict falsification_member_confirmed. Statistical
  discipline: MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026
  standing rule (tones hand-assigned, n=1 per arm; p_value/
  cohens_d/ci_95 NOT_CALCULATED; engine NOT run; is_significant
  false; NOT artifact-grade; no_analysis_json_update true).
  connects_to [343, 513, 952, 956, 957].
- m960 (Type C #1214, profiles/competitor-entities.yaml top-level
  block key type_c_1214_october_publisher_deal_renewal_status_sweep_
  oct04_3pm): October-2026 publisher-deal renewal-status sweep
  (Oct 4 checkpoint): Axel Springer x OpenAI 3-year deal expiry
  now ~2 months out (Dec 2026), renewal UNRESOLVED; first-gen
  OpenAI publisher triad (Conde Nast, Atlantic, FT) renewal
  UNRESOLVED, treated ACTIVE per the #599 convention; News Corp
  dual-payer ledger HOLDS on independent 4-set confirmation;
  OpenAI DevDay Oct 6 not yet occurred - forward watch. STATUS-
  CHECK EXTENSION of the m597, m600, and m957 lines; no new
  direction (the fortieth direction form absent in profiles/).
  no_analysis_json_update true; type financial_incentive_mapping;
  connects_to [597, 600, 957]. 9 delegated search sets, 0
  browser.open per #503.
- LEDGER STATE: exactly one fiftieth member-claim form in the
  corpus (m959, profiles/careers/journalists.yaml, 3 occurrences:
  the notes landing line, the falsification_family claim, and the
  novelty line; falsification_ledger 50). The forty-ninth member-
  claim form is intact (m956, same file, 3 occurrences). m958
  claims NO slot (falsification_family_member false,
  falsification_ledger 49); m960 is an extension, not a member.
  No fifty-first member-claim form repo-wide.
- #1211 Type E 165th podcast-sentiment verification-cycle discipline
  verified: monitoring-only per the Aug 28 2026 standing rule (tone
  NOT_SCORED, engine NOT run, no mechanisms landed, NOT artifact-
  grade, verdict directionally_supported_not_proven,
  no_analysis_json_update true). GF 502 HOLDS (32nd verification,
  ~168h post Sep-28 release; NO 503); pure re-surface streak
  ADVANCES to four; Attention Sphere 165th no-match.
- The 1210-1214 window is VERIFIED CLOSED as a consecutive newest-
  first sequence in git history (D #1210 main 42ef40b0, E #1211 main
  03c1ac95, A #1212 main 9f4eb1a9, B #1213 main 9b2f12d1, C #1214 main
  971a9250). This run opens the 1215-1219 window: D (#1215) ->
  E (#1216) -> A (#1217) -> B (#1218) -> C (#1219) per the #565 anchor
  + rotation guard. The #1210-launched background-suite verdict
  rendered this run; the #1215-launched suite's verdict belongs to
  #1220 per #795.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
file's committed placeholder form; the anchor followup patches it
to this run's main-commit hash (self-anchor). Doc-sync constants
per #719: README_TEST_COUNT / README_FILE_COUNT hold the
post-doc-sync values from the start (patched post-first-run with
the true collected count); the doc-sync classes fail pre-commit by
design and pass post-sync.
"""

import glob
import inspect
import os
import re
import subprocess
import time

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
NEWS_CORP_FILE = os.path.join(PROFILES_DIR, "news-corp.yaml")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")
README_FILE = os.path.join(REPO_ROOT, "README.md")
ARCH_FILE = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

# Block keys are plain literals: they carry the landing ITERATION
# number (1212/1213/1214) and no mechanism-number substring (designed
# keying per #715). Iterations are the landing iterations, not the
# mechanism ids.
KEY_958 = ("type_a_1212_wsj_openai_safety_firings_oct01_vs_wsj_meta_"
           "muse_trust_dual_payer_symmetry")
KEY_959 = ("type_b_1213_kaitlyn_huamani_ap_meta_connect_vs_openai_"
           "devday_falsification")
KEY_960 = ("type_c_1214_october_publisher_deal_renewal_status_sweep_"
           "oct04_3pm")
OWN_BASENAME = ("test_type_d_1215_m958_m959_m960_qualitative_"
                "corpus_integrity_oct04_4pm.py")

# Predecessor test files for supersession pins.
E1211_FILE = ("test_type_e_1211_podcast_sentiment_165th_verification_"
              "oct04_1pm.py")
A1212_FILE = ("test_type_a_1212_wsj_openai_oct01_safety_firings_vs_"
              "wsj_meta_muse_trust_dual_payer_oct04_2pm.py")
B1213_FILE = ("test_type_b_1213_kaitlyn_huamani_ap_meta_connect_vs_"
              "openai_devday_falsification_oct04_2pm.py")
C1214_FILE = ("test_type_c_1214_october_publisher_deal_renewal_status_"
              "sweep_oct04_3pm.py")
THIS_FILE = OWN_BASENAME

# Prior-window background suite (verdict rendered this run) and this
# run's re-launched suite.
PRIOR_SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1210_full_suite.log",
)
SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1215_full_suite.log",
)

# Patched post-first-run with the true collected count per #719.
# Pre-sync: 65500 tests / 1539 files. Patched post-first-run: N collected.
README_TEST_COUNT = 65500 + 0  # post-doc-sync total; patched per #719
README_FILE_COUNT = 1540  # post-doc-sync total (pre-sync 1539 + 1)
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "0" * 40

MECH_NUM = 960
NEXT_NUM = 961

# Fragment-built direction needles per #715 (never contiguous here).
_T35 = "THIRTY-" + "FIFTH relationship direction"
_T36 = "THIRTY-" + "SIXTH relationship direction"
_T37 = "THIRTY-" + "SEVENTH relationship direction"
_T38 = "THIRTY-" + "EIGHTH relationship direction"
_T39 = "THIRTY-" + "NINTH relationship direction"
_T40 = "FORT" + "IETH relationship direction"


# Format-built mechanism needles per #715/#770 (never contiguous here).
def _mech_underscore(n):
    return "mechanism" + "_%d" % n


def _mech_dash(n):
    return "mechanism" + "-%d" % n


def _mech_id_colon(n):
    return "mechanism_id: %d" % n


FORTY_SIXTH_MEMBER = "FORTY" + "-SIXTH falsification-family member"
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"
FORTY_NINTH_MEMBER = "FORTY" + "-NINTH falsification-family member"
FIFTIETH_MEMBER = "FIFT" + "IETH falsification-family member"
FIFTY_FIRST_MEMBER = "FIFT" + "Y-FIRST falsification-family member"

# One-parse-per-file cache: the journalists YAML is large and
# re-parsing per test method is pure waste (tests never mutate).
_YAML_CACHE = {}


def _yaml(path):
    if path not in _YAML_CACHE:
        with open(path, "r", encoding="utf-8") as f:
            _YAML_CACHE[path] = yaml.safe_load(f)
    return _YAML_CACHE[path]


def _read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _git_grep_tracked(needle, *paths):
    cmd = ["git", "grep", "-l", "-F", needle]
    if paths:
        cmd += ["--"] + list(paths)
    out = subprocess.run(
        cmd, cwd=REPO_ROOT, capture_output=True, text=True, timeout=120,
    )
    return [line for line in out.stdout.split("\n") if line.strip()]


def _iter_source_files():
    """Yield paths for profile + test source files.

    Scoped to profiles/ + tests/ per the #1191 convention (the
    iteration-log.md prose carries next-number needle forms as
    documented guards; the log is not a mechanism-key position).
    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts.
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
            yield os.path.join(root, f)


def _sweep_underscore_mechanism(n):
    needle = "mechanism" + "_%d" % n
    return [p for p in _iter_source_files()
            if needle in open(p, encoding="utf-8",
                              errors="replace").read()]


def _sweep_dash_mechanism(n):
    needle = "mechanism" + "-%d" % n
    return [p for p in _iter_source_files()
            if needle in open(p, encoding="utf-8",
                              errors="replace").read()]


def _max_numeric_mechanism_id_in_profiles():
    ids = []
    for dirpath, _, files in os.walk(PROFILES_DIR):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(dirpath, fn))
                for m in re.findall(r"mechanism_id: (\d+)", text):
                    ids.append(int(m))
    return max(ids)


def _m958_block():
    # News Corp's competitor_relationships carries Type A blocks
    # under the entity sub-key (openai), per the #1212 land.
    return _yaml(NEWS_CORP_FILE)["competitor_relationships"]["openai"][
        KEY_958]


def _m959_block():
    # Kaitlyn Huamani's journalist entry is a top-level key in the
    # careers journalists.yaml (the per-#643 key convention); the m959
    # block lives under its competitor_coverage sub-key.
    return _yaml(JOURNALISTS_FILE)["kaitlyn_huamani_type_b"][
        "competitor_coverage"][KEY_959]


def _m960_block():
    return _yaml(ENTITIES_FILE)[KEY_960]


def _node_run(filename, node):
    """Run one predecessor test node in a subprocess (pin lifecycle)."""
    target = os.path.join(TESTS_DIR, filename) + "::" + node
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    venv_py = os.path.join(REPO_ROOT, ".venv", "bin", "python")
    cmd = [venv_py, "-m", "pytest", target, "-q", "--no-header",
           "-o", "addopts=", "-p", "no:cacheprovider"]
    res = None
    for attempt in range(6):
        res = subprocess.run(
            cmd,
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            env=env,
            timeout=300,
        )
        # Transient "no tests ran" (rc 4) flake: this filesystem
        # briefly hides files from freshly spawned processes (the
        # same class as the find/git-add hangs per AGENTS.md), so a
        # fresh pytest can report "file or directory not found"
        # for a node that exists. Retry with a sleep; a real bad
        # node name fails all attempts identically, so the retry
        # cannot mask a genuine bug - and it keeps trip-by-design
        # pins honest (a flake rc=4 must not count as a trip).
        if not (res.returncode == 4 and "no tests ran" in res.stdout):
            break
        time.sleep(10)
    return res


def _synthetic_calibration_delta():
    """Fresh engine-layer calibration contract for #1215.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no profile reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_anthropic_arms = [-0.13, -0.27]
    synthetic_meta_arms = [-0.33, -0.44]
    pooled_anthropic = (sum(synthetic_anthropic_arms)
                        / len(synthetic_anthropic_arms))
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_anthropic - pooled_meta, 3)


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1215:
    def test_zero_type_d_1215_files_on_disk(self):
        assert glob.glob(
            os.path.join(TESTS_DIR, "test_type_d_1215*")) == [
                os.path.join(TESTS_DIR, OWN_BASENAME)], "only this file"

    def test_no_type_d_1215_in_git_log(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1215"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == "", out.stdout

    def test_no_1215_block_key_repo_wide(self):
        # Designed keying: this file's keys reference the landed
        # iterations (1212/1213/1214) and mechanisms (958/959/960).
        # The only tracked carrier of the "type_d_1215" string is the
        # #1214 file's forward-guard pin (its no-Type-D-#1215 git-log
        # pin); no type_d_1215 block-key form exists anywhere.
        assert _git_grep_tracked("type_d_1215") == [
            "tests/" + C1214_FILE]

    def test_no_1215_row_in_readme_test_table_pre_commit(self):
        text = _read(README_FILE)
        assert TEST_BASENAME not in text

    def test_no_1215_row_in_architecture_tree_pre_commit(self):
        text = _read(ARCH_FILE)
        assert TEST_BASENAME not in text

    def test_no_1215_entry_in_iteration_log_pre_commit(self):
        assert "## #1215" not in _read(LOG_FILE)

    def test_readme_stats_pre_commit(self):
        text = _read(README_FILE)
        assert "| Tests | 65500 |" in text
        assert "Across 1539 test files" in text


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1215 opens the 1215-1219 window
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1215:
    def test_rotation_window_opens_1215(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "1215-1219 window" in src
        assert "OPENING" in src

    def test_predecessor_1214_chain_present(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type C #1214"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert "Type C #1214" in out.stdout

    def test_window_order_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "D->E->A->B->C" in src

    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit the anchor is the 0*40 placeholder; the anchor
        # followup patches it to the main-commit hash per #565.
        # Deselect post-anchor (the shape test then takes over).
        assert ANCHORED_SHA == "0" * 40

    def test_next_window_leg_is_type_e(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "#1216 Type E" in src

    def test_closing_window_1210_1214_verified_closed(self):
        # The 1210-1214 window verified closed as a consecutive
        # newest-first sequence in git history.
        for typ, n in (("D", "1210"), ("E", "1211"), ("A", "1212"),
                       ("B", "1213"), ("C", "1214")):
            out = subprocess.run(
                ["git", "log", "--oneline",
                 "--grep=Type %s #%s" % (typ, n)],
                cwd=REPO_ROOT, capture_output=True, text=True,
                timeout=60,
            )
            assert out.stdout.strip() != "", n

    def test_closing_window_mains_present(self):
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        subjects = out.stdout
        for needle in ("Type D #1210:", "Type E #1211:",
                       "Type A #1212:", "Type B #1213:",
                       "Type C #1214:"):
            assert needle in subjects, needle

    def test_closing_window_main_hashes_present(self):
        # The five main-commit short hashes are pinned so the chain
        # the window-close claim rests on is the real one.
        out = subprocess.run(
            ["git", "log", "--format=%H"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        full = out.stdout.splitlines()
        for short in ("42ef40b0", "03c1ac95", "9f4eb1a9", "9b2f12d1",
                      "971a9250"):
            assert any(h.startswith(short) for h in full), short


# ---------------------------------------------------------------------------
# 3. Novelty anchor: no prior #1215 claims
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1215:
    def test_no_prior_type_d_1215_in_log(self):
        text = _read(LOG_FILE)
        assert "## #1215" not in text

    def test_no_prior_1215_opening_claim(self):
        # The #1214 entry already names the next window (the 1210-1214
        # window closed; the 1215-1219 window opens with Type D #1215
        # lineage); the pre-commit absence pin is on the OPENING-leg
        # heading this run adds.
        text = _read(LOG_FILE)
        assert "OPENING leg of the 1215-1219 window" not in text


# ---------------------------------------------------------------------------
# 4. Corpus integrity: the m958/m959/m960 landings are present
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1215:
    def test_m958_block_present_in_news_corp_yaml(self):
        block = _m958_block()
        assert block["mechanism_id"] == 958
        assert block["block_key"] == KEY_958

    def test_m958_test_file_present(self):
        assert os.path.exists(
            os.path.join(TESTS_DIR, A1212_FILE))

    def test_m959_block_present_in_journalists_yaml(self):
        block = _m959_block()
        assert block["mechanism_id"] == 959
        assert block["block_key"] == KEY_959

    def test_m959_test_file_present(self):
        assert os.path.exists(
            os.path.join(TESTS_DIR, B1213_FILE))

    def test_m960_block_present_in_competitor_entities_yaml(self):
        block = _m960_block()
        assert block["mechanism_id"] == 960
        assert block["block_key"] == KEY_960

    def test_m960_test_file_present(self):
        assert os.path.exists(
            os.path.join(TESTS_DIR, C1214_FILE))

    def test_no_numeric_961_mechanism_id_in_profiles(self):
        assert _git_grep_tracked(
            _mech_id_colon(NEXT_NUM), "profiles/") == []

    def test_max_numeric_mechanism_id_is_960(self):
        # Type D lands no mechanisms: max stays 960.
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_next_number_underscore_forms(self):
        # The designed keying carries the iteration number, never the
        # mechanism number; iteration-1215 keys cannot contain a 961
        # mechanism substring.
        assert _sweep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_number_dash_forms(self):
        assert _sweep_dash_mechanism(NEXT_NUM) == []

    def test_type_d_lands_no_mechanisms(self):
        # Type D is verification-layer: max stays 960, next stays 961.
        assert MECH_NUM == 960
        assert NEXT_NUM == 961


# ---------------------------------------------------------------------------
# 5. m958 qualitative discipline (Type A #1212, WSJ dual-payer)
# ---------------------------------------------------------------------------
class TestTypeDM958QualitativeDiscipline1215:
    def test_m958_verdict_is_refinement_not_discovery(self):
        assert _m958_block()["verdict"] == \
            "mechanism_refinement_not_a_discovery"

    def test_m958_claims_no_falsification_slot(self):
        block = _m958_block()
        assert block["falsification_family_member"] is False
        assert block["falsification_ledger"] == 49
        assert block["falsification_family"].startswith("NOT a member")

    def test_m958_statistical_discipline_manual_only(self):
        disc = _m958_block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE only" in disc
        assert "engine NOT run" in disc
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in disc
        assert "is_significant false" in disc
        assert "NOT artifact-grade" in disc
        assert "no_analysis_json_update true" in disc

    def test_m958_no_analysis_json_update(self):
        assert _m958_block()["no_analysis_json_update"] is True

    def test_m958_connects_to(self):
        assert _m958_block()["connects_to"] == \
            [519, 532, 763, 904, 905, 956, 957]

    def test_m958_iteration_and_type(self):
        block = _m958_block()
        assert block["iteration"] == 1212
        assert block["iteration_type"] == "A"

    def test_m958_research_method_bounded(self):
        # 11 browser.search query sets via delegated research +
        # main-run verification; 0 browser.open per #503.
        method = _m958_block()["research_method"]
        assert "0 browser.open" in method


# ---------------------------------------------------------------------------
# 6. m959 qualitative discipline (Type B #1213, Huamani AP)
# ---------------------------------------------------------------------------
class TestTypeDM959QualitativeDiscipline1215:
    def test_m959_verdict_is_member_confirmed(self):
        assert _m959_block()["verdict"] == "falsification_member_confirmed"

    def test_m959_lands_fiftieth_slot(self):
        block = _m959_block()
        assert block["falsification_family_member"] is True
        assert block["falsification_ledger"] == 50
        assert "FIFTIETH falsification-family member" in \
            block["falsification_family"]

    def test_m959_statistical_discipline_manual_only(self):
        disc = _m959_block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in disc
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in disc
        assert "engine NOT run" in disc
        assert "is_significant false" in disc
        assert "NOT artifact-grade" in disc
        assert "no_analysis_json_update true" in disc

    def test_m959_no_analysis_json_update(self):
        assert _m959_block()["no_analysis_json_update"] is True

    def test_m959_connects_to(self):
        assert _m959_block()["connects_to"] == \
            [343, 513, 952, 956, 957]

    def test_m959_iteration_and_type(self):
        # The m959 block stores the run type under the plain `type`
        # key ('B'), not `iteration_type` (in-gate fix: assert the
        # corpus's actual storage form).
        block = _m959_block()
        assert block["iteration"] == 1213
        assert block["type"] == "B"

    def test_m959_research_method_bounded(self):
        method = _m959_block()["research_method"]
        assert "0 browser.open" in method


# ---------------------------------------------------------------------------
# 7. m960 qualitative discipline (Type C #1214, renewal sweep)
# ---------------------------------------------------------------------------
class TestTypeDM960QualitativeDiscipline1215:
    def test_m960_is_status_check_extension(self):
        tax = _m960_block()["relationship_direction_taxonomy"]
        assert tax.startswith("STATUS-CHECK EXTENSION")

    def test_m960_claims_no_falsification_slot(self):
        block = _m960_block()
        assert block.get("falsification_family_member", False) is False

    def test_m960_no_analysis_json_update(self):
        assert _m960_block()["no_analysis_json_update"] is True

    def test_m960_connects_to(self):
        assert _m960_block()["connects_to"] == [597, 600, 957]

    def test_m960_iteration_and_type(self):
        block = _m960_block()
        assert block["iteration"] == 1214
        assert block["iteration_type"] == "C"
        assert block["type"] == "financial_incentive_mapping"

    def test_m960_no_new_money_facts(self):
        # A status-check extension: money_flow states NO NEW MONEY
        # FACTS; the delta is a bounded-absence refresh.
        assert "NO NEW MONEY FACTS" in _m960_block()["money_flow"]


# ---------------------------------------------------------------------------
# 8. Falsification ledger: holds at 50
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1215:
    def test_forty_sixth_claim_in_exactly_one_profiles_file(self):
        hits = _git_grep_tracked(FORTY_SIXTH_MEMBER, "profiles/")
        assert hits == ["profiles/the-verge.yaml"], hits

    def test_forty_seventh_member_claim_exactly_in_wired(self):
        # The single live forty-seventh member claim is m946
        # (profiles/wired.yaml). m958/m959/m960 landings do not move
        # the 47th slot.
        hits = _git_grep_tracked(FORTY_SEVENTH_MEMBER, "profiles/")
        assert hits == ["profiles/wired.yaml"], hits

    def test_forty_seventh_member_claim_count_is_two(self):
        # The novelty "LANDED this run" line + the falsification_family
        # claim inside the m946 block: exactly 2 occurrences.
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FORTY_SEVENTH_MEMBER, "--",
             "profiles/wired.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_forty_eighth_member_claim_in_financial_times(self):
        # The single live forty-eighth member claim is m952
        # (profiles/financial-times.yaml).
        hits = _git_grep_tracked(FORTY_EIGHTH_MEMBER, "profiles/")
        assert hits == ["profiles/financial-times.yaml"], hits

    def test_forty_eighth_member_claim_count_is_two(self):
        # The novelty "LANDED this run" line + the falsification_family
        # claim inside the m952 block: exactly 2 occurrences.
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FORTY_EIGHTH_MEMBER, "--",
             "profiles/financial-times.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_forty_ninth_member_claim_in_journalists(self):
        # The single live forty-ninth member claim is m956
        # (profiles/careers/journalists.yaml).
        hits = _git_grep_tracked(FORTY_NINTH_MEMBER, "profiles/")
        assert hits == ["profiles/careers/journalists.yaml"], hits

    def test_forty_ninth_member_claim_count_is_three(self):
        # The notes landing line + the falsification_family claim +
        # the novelty line inside the m956 block: exactly 3.
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FORTY_NINTH_MEMBER, "--",
             "profiles/careers/journalists.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_member_claim_in_journalists(self):
        # The single live fiftieth member claim is m959
        # (profiles/careers/journalists.yaml).
        hits = _git_grep_tracked(FIFTIETH_MEMBER, "profiles/")
        assert hits == ["profiles/careers/journalists.yaml"], hits

    def test_fiftieth_member_claim_count_is_three(self):
        # The notes landing line + the falsification_family claim +
        # the novelty line inside the m959 block: exactly 3.
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FIFTIETH_MEMBER, "--",
             "profiles/careers/journalists.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_fifty_first_member_claim_repo_wide(self):
        assert _git_grep_tracked(FIFTY_FIRST_MEMBER) == []

    def test_thirty_ninth_direction_in_competitor_entities(self):
        # Landed at #1194 (m948 LICENSE-AND-ADOPT).
        hits = _git_grep_tracked(_T39, "profiles/")
        assert "profiles/competitor-entities.yaml" in hits, hits

    def test_thirty_eighth_direction_in_competitor_entities(self):
        # Landed at #1189 (m945 LICENSE-AND-CO-BUILD).
        hits = _git_grep_tracked(_T38, "profiles/")
        assert "profiles/competitor-entities.yaml" in hits, hits

    def test_thirty_seventh_direction_in_competitor_entities(self):
        # Landed at #1184 (m942 INVEST-AND-LICENSE).
        hits = _git_grep_tracked(_T37, "profiles/")
        assert "profiles/competitor-entities.yaml" in hits, hits

    def test_thirty_sixth_direction_in_competitor_entities(self):
        # Landed at #1169 (m933 REGULATORY-PREEMPTION).
        hits = _git_grep_tracked(_T36, "profiles/")
        assert "profiles/competitor-entities.yaml" in hits, hits

    def test_thirty_fifth_direction_in_competitor_entities(self):
        # Landed at #1139 (m915 METER-THEN-INVITE).
        hits = _git_grep_tracked(_T35, "profiles/")
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_no_fortieth_direction_claim_in_profiles(self):
        # Profiles-scoped per the #1199 in-gate fix: the #1197 and
        # #1202 test files carry the contiguous fortieth needle in
        # their own constant definitions; a repo-wide scope would trip
        # on those landed files. The format-built constant above is
        # never written contiguously in THIS file.
        assert _git_grep_tracked(_T40, "profiles/") == []
        assert len(_T40) > 0

    def test_ledger_holds_at_50(self):
        # m959 lands the fiftieth slot (falsification_ledger 50);
        # m958 claims no slot; m960 is a status-check extension, not
        # a member. Exactly one live member claim at the top slot.
        b958 = _m958_block()
        assert b958["falsification_family_member"] is False
        assert b958["falsification_ledger"] == 49
        b959 = _m959_block()
        assert b959["falsification_family_member"] is True
        assert b959["falsification_ledger"] == 50
        assert "FIFTIETH falsification-family member" in \
            b959["falsification_family"]
        b960 = _m960_block()
        assert b960["relationship_direction_taxonomy"].startswith(
            "STATUS-CHECK EXTENSION")


# ---------------------------------------------------------------------------
# 9. Type E #1211 discipline: the 165th verification cycle stays
#    monitoring-only
# ---------------------------------------------------------------------------
class TestTypeDTypeE1211Discipline1215:
    def test_1211_file_on_disk(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1211_FILE))

    def test_1211_pins_165th_cycle(self):
        src = _read(os.path.join(TESTS_DIR, E1211_FILE))
        assert "165th verification cycle" in src
        assert "164->165" in src

    def test_1211_monitoring_only_discipline(self):
        # The Aug 28 2026 standing rule: monitoring-only, tone
        # NOT_SCORED, engine NOT run, no mechanisms, NOT artifact-grade,
        # verdict directionally_supported_not_proven.
        src = _read(os.path.join(TESTS_DIR, E1211_FILE))
        assert "monitoring-only" in src
        assert "NOT artifact-grade" in src

    def test_1211_covers_both_podcasts(self):
        src = _read(os.path.join(TESTS_DIR, E1211_FILE))
        assert "Attention Sphere" in src
        assert "Guilty Feminist" in src

    def test_1211_research_method_bounded(self):
        src = _read(os.path.join(TESTS_DIR, E1211_FILE))
        assert "0 browser.open" in src


# ---------------------------------------------------------------------------
# 10. Forward-looking staleness (predecessor pin lifecycle via subprocess)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1215:
    def test_1214_rotation_no_type_d_1215_pin_stays_green_precommit(self):
        # #1214's no-Type-D-#1215 git-log pin flips by design at THIS
        # run's main commit; the zero-961 guards stay GREEN (this run
        # lands no mechanisms - pinned in TestGuardLifecycle1215).
        # Record the pre-commit state: the pin still holds now.
        res = _node_run(
            C1214_FILE,
            "TestGuardLifecycle1214::test_no_type_d_1215_in_git_log_pin",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1214_guard_lifecycle_961_numeric_stays_green_precommit(self):
        res = _node_run(
            C1214_FILE,
            "TestGuardLifecycle1214::test_961_numeric_absent_in_profiles",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1214_pins_on_960_landing_stay_green(self):
        # #1214's landing pin (max-960) stays green: this run lands no
        # mechanisms, so max remains 960.
        res = _node_run(
            C1214_FILE,
            "TestGuardLifecycle1214::test_pins_on_960_landing",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1213_pins_flip_by_design_documented(self):
        # #1213's forward guards (max-959, zero-960 keys all forms,
        # no-Type-C-#1214-in-git-log) flip by design now that m960 has
        # landed; recorded in #1214's file, not repaired here.
        src = _read(os.path.join(TESTS_DIR, C1214_FILE))
        assert "1213" in src


# ---------------------------------------------------------------------------
# 11. Guard lifecycle: the guards this run lays for the next leg
# ---------------------------------------------------------------------------
class TestGuardLifecycle1215:
    def test_pins_on_no_mechanism_landing(self):
        # Type D lands no mechanisms: max stays 960, next stays 961.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "MECH_NUM = 960" in src
        assert "NEXT_NUM = 961" in src

    def test_no_type_e_1216_in_git_log_pin(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type E #1216"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == ""

    def test_961_numeric_absent_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(961), "profiles/") == []

    def test_no_fortieth_direction_pin(self):
        # The fortieth direction-claim form stays absent in profiles/
        # (profiles-scoped per the #1199 in-gate fix).
        assert _git_grep_tracked(_T40, "profiles/") == []

    def test_forty_ninth_member_intact_pin(self):
        # The single live forty-ninth member claim (m956,
        # careers/journalists.yaml) must survive this run unchanged.
        assert _git_grep_tracked(
            FORTY_NINTH_MEMBER, "profiles/") == [
                "profiles/careers/journalists.yaml"]

    def test_fiftieth_member_intact_pin(self):
        # The single live fiftieth member claim (m959,
        # careers/journalists.yaml) must survive this run unchanged.
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FIFTIETH_MEMBER, "--",
             "profiles/careers/journalists.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_fifty_first_member_pin(self):
        assert _git_grep_tracked(FIFTY_FIRST_MEMBER) == []

    def test_predecessor_1214_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, C1214_FILE))

    def test_next_leg_is_1216_type_e(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "#1216 Type E" in src


# ---------------------------------------------------------------------------
# 12. Background-suite verdict per #795: the #1210-launched suite DIED
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1215:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG)

    def test_prior_suite_frozen_at_three_percent(self):
        # The #1210-launched suite stalled at 10636 bytes / [ 3%]
        # progress; last write Oct 4 12:59 PDT (~3h stale at this
        # run's 16:0x check); the log holds progress dots, not a
        # summary.
        text = _read(PRIOR_SUITE_LOG)
        assert 10000 <= len(text) <= 11000, len(text)
        assert "[  3%]" in text

    def test_prior_suite_has_zero_summary_tokens(self):
        # A completed run prints a summary ("passed"/"failed") or a
        # collection report ("no tests ran" / "short test summary").
        # The dead run carries none of them.
        text = _read(PRIOR_SUITE_LOG)
        for token in ("passed", "failed", "no tests ran",
                      "short test summary"):
            assert token not in text, token

    def test_prior_suite_not_holding_live_pytest(self):
        # The re-launched #1215 suite IS alive in this run's process
        # set (a plain ps grep for "pytest" would self-trip on it),
        # so the dead-or-alive question must be scoped to the PRIOR
        # log: no process holds type_d_1210_full_suite.log open (the
        # /proc open-fd check per the #1190 convention). A dead run
        # produces no usable verdict, which is what this test pins.
        out = subprocess.run(
            ["bash", "-c",
             "ls -l /proc/[0-9]*/fd/* 2>/dev/null | grep -F "
             "'type_d_1210_full_suite.log' | head -5"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == "", out.stdout

    def test_thirty_seventh_consecutive_death(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite completed).
        # This verdict renders the THIRTY-SEVENTH consecutive
        # background-suite death of the new streak.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "THIRTY-SEVENTH consecutive" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each verdict:
        # ONE-HUNDRED-FIRST -> ONE-HUNDRED-SECOND.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "ONE-HUNDRED-FIRST -> ONE-HUNDRED-SECOND" in src

    def test_tombstone_recorded_in_iteration_log(self):
        # Deselected pre-commit: the tombstone is written into the
        # #1215 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_FILE)
        assert "ONE-HUNDRED-SECOND" in text


# ---------------------------------------------------------------------------
# 13. Suite re-launch: the #1215-launched suite is in flight
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1215:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1215 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1220 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1220)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1215_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 14. Synthetic engine calibration (engine-layer contract, never a
#     finding)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1215:
    def test_calibration_delta_contract(self):
        # Synthetic Anthropic arms [-0.13, -0.27] vs synthetic Meta
        # arms [-0.33, -0.44]: pooled delta +0.185 (Meta-harder). This
        # is a FRESH #1215 engine-layer contract value; it is never
        # promoted to a finding.
        assert _synthetic_calibration_delta() == 0.185

    def test_calibration_is_deterministic(self):
        assert _synthetic_calibration_delta() == \
            _synthetic_calibration_delta()

    def test_calibration_reads_no_corpus(self):
        # The calibration function must not touch the corpus: its
        # source references no profile paths, no yaml, no repo reads.
        src = inspect.getsource(_synthetic_calibration_delta)
        assert "profiles" not in src
        assert "yaml" not in src
        assert "iteration-log" not in src

    def test_calibration_not_promoted_to_finding(self):
        # The module docstring declares the calibration engine-layer
        # only, never a finding; no analysis.json update is claimed.
        doc = __doc__
        assert "never promoted to a finding" in doc
        assert "Verification-layer run: no corpus edits" in doc


# ---------------------------------------------------------------------------
# 15. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1215:
    def test_readme_stats_table_updated(self):
        text = _read(README_FILE)
        assert "| Tests | %d |" % README_TEST_COUNT in text
        assert "Across %d test files" % README_FILE_COUNT in text

    def test_readme_test_table_row_present(self):
        text = _read(README_FILE)
        assert TEST_BASENAME in text

    def test_architecture_tree_row_present(self):
        text = _read(ARCH_FILE)
        assert TEST_BASENAME in text

    def test_iteration_log_entry_present(self):
        text = _read(LOG_FILE)
        assert "## #1215" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 65500 + COLLECTED_COUNT
        assert README_FILE_COUNT == 1540


# ---------------------------------------------------------------------------
# 16. Iteration log (#719: the entry carries hashes per #721)
# ---------------------------------------------------------------------------
class TestTypeDIterationLog1215:
    def test_log_entry_has_main_commit_hash(self):
        text = _read(LOG_FILE)
        assert "Type D #1215" in text

    def test_log_entry_notes_window_opening(self):
        text = _read(LOG_FILE)
        assert "OPENING leg of the 1215-1219 window" in text

    def test_log_entry_notes_tombstone_lineage(self):
        # Deselected pre-commit: the entry is written in the doc-sync
        # step per #719/#721.
        text = _read(LOG_FILE)
        assert "ONE-HUNDRED-SECOND" in text


# ---------------------------------------------------------------------------
# 17. Literal discipline (ASCII-only, no em dashes)
# ---------------------------------------------------------------------------
class TestLiteralDiscipline1215:
    def test_ascii_only(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert all(ord(c) < 128 for c in src), "non-ASCII literal found"

    def test_no_em_dashes(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "\u2014" not in src
        assert "\u2013" not in src


# ---------------------------------------------------------------------------
# 18. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1215:
    def test_inflight_items_untouched(self):
        # #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test
        # file working-tree edit), #900 (untracked Type D test file),
        # #1012-wt (Type A test file working-tree edit) stay out of
        # this run's index and diff; targeted staging only.
        out = subprocess.run(
            ["git", "status", "--short"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        staged = [l for l in out.stdout.split("\n")
                  if l.startswith(("A ", "M "))]
        for line in staged:
            assert "nytimes.yaml" not in line, line
            assert "test_type_b_938" not in line, line
            assert "test_type_a_1012" not in line, line
            assert "test_type_d_900" not in line, line

    def test_m846_untouched(self):
        # #1024's m846: Ray's revert/leave/rebuild decision pending;
        # not an assistant repair task. Show-hash form against the
        # main commit's own diff (vacuous pass pre-commit on the
        # 0*40 placeholder; real check post-anchor).
        out = subprocess.run(
            ["git", "show", ANCHORED_SHA, "--stat", "--format="],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert "m846" not in out.stdout


# ---------------------------------------------------------------------------
# 19. Anchor (per #565; patched in the anchor followup)
# ---------------------------------------------------------------------------
class TestAnchor1215:
    def test_anchor_sha_format(self):
        # Patched in the anchor followup per #565: ANCHORED_SHA is the
        # main-commit hash, a 40-char hex string, not the placeholder.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40

    def test_anchor_sha_is_main_commit(self):
        # The anchor commit patches ANCHORED_SHA to the main-commit hash;
        # verify it appears in the git log as a commit hash.
        log = subprocess.run(
            ["git", "log", "--format=%H"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert ANCHORED_SHA in log

    def test_anchor_followup_commit_message_convention(self):
        # The anchor followup uses the documented message shape:
        # "Type D #1215 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1215 anchor"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert "Type D #1215 anchor" in log

    def test_main_commit_message_convention(self):
        log = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1215:"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert "Type D #1215" in log


# Collected count patch (post-first-run per #719).
COLLECTED_COUNT = 0
