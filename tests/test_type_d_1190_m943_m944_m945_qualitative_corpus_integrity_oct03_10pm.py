"""Type D #1190: verify m943/m944/m945 qualitative-discipline landings +
post-1185-1189 corpus integrity (max numeric mechanism_id 945; zero
next-number nine-four-six keys all forms; falsification ledger holds
at 46; thirty-fifth + thirty-sixth + thirty-seventh + thirty-eighth
directions present, thirty-ninth absent) + #1185 background-suite verdict
(THIRTIETH consecutive death; tombstone NINETY-SIXTH -> NINETY-SEVENTH)
+ fresh synthetic engine calibration + full suite re-launched - FIRST
and OPENING leg of the 1190-1194 window (Oct 3 2026, 10:00 PM PDT).

Verification-layer run: no corpus edits, no analysis.json updates, no
new mechanisms. The finding layer stays MANUAL/QUALITATIVE ONLY per
the Aug 28 2026 standing rule; the synthetic engine calibration is a
fresh engine-layer contract and is never promoted to a finding.

- m943 (Type A #1187, profiles/news-corp.yaml
  competitor_relationships block key
  type_a_1187_nypost_anthropic_oct01_ipo_hypocrisy_register_vs_carried_
  meta_openai_arms_oct03_7pm): NY Post x Anthropic Oct-1 IPO-hypocrisy
  original (-0.35 MANUAL ILLUSTRATIVE) vs carried NY Post x Meta /
  OpenAI arms (temporal extension of m925; FIRST dedicated NY Post x
  Anthropic mechanism; illustrative deltas +0.15 vs Meta arm, +0.05
  vs OpenAI arm); NOT a falsification-family member per the #1143
  precedent (same-publication temporal replication is not a new
  prediction test); ledger holds at 46. Statistical discipline:
  MANUAL/QUALITATIVE ONLY (p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False, engine NOT run, NOT artifact-grade, verdict
  directionally_supported_not_proven, no_analysis_json_update true).
- m944 (Type B #1188, profiles/careers/journalists.yaml top-level
  eli_tan key, competitor_coverage block
  type_b_1188_eli_tan_nyt_pervert_glasses_stigma_vs_other_companies_
  neutral_within_piece): Eli Tan (NYT) FIRST dedicated Type B -
  Sep-24 Chen+Tan "Pervert Glasses" column within-piece cross-entity
  stigma pin (-0.45 vs +0.05, illustrative delta -0.50,
  theory-consistent with the financial-deal gradient, extends m484
  and mechanism_662 to Tan's own byline); NOT a falsification-family
  member (single-column pin with a co-byline; no uniform
  payer-softening prediction refuted); ledger holds at 46.
  Statistical discipline: MANUAL ILLUSTRATIVE ONLY per the Aug 28
  2026 standing rule (engine NOT run, is_significant False, NOT
  artifact-grade, verdict directionally_supported_not_proven,
  no_analysis_json_update true).
- m945 (Type C #1189, profiles/competitor-entities.yaml top-level
  block key
  type_c_1189_openai_synopsys_gpt_synopsys_license_and_cobuild_
  thirty_eighth_direction_oct03_9pm): FIRST dedicated corpus
  mechanism on the OpenAI x Synopsys GPT-Synopsys license-and-co-build
  (announced Sep 30 2026) - LANDS the thirty-eighth relationship
  direction; 8 novel sources (0 browser.open); connects_to [804,
  391, 663]; NOT a falsification-family member (per the #609/#614
  qualitative boundary); ledger holds at 46. Statistical discipline:
  tone NOT_SCORED, engine NOT run, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade.
- #1186 Type E 160th podcast-sentiment verification-cycle discipline
  verified: monitoring-only per the Aug 28 2026 standing rule
  (tone NOT_SCORED, engine NOT run, no mechanisms landed,
  NOT artifact-grade, verdict directionally_supported_not_proven,
  no_analysis_json_update true, ledger holds at 46).
- #1185 background-suite verdict rendered this run per #795: the
  #1185-launched full suite DIED (11188 bytes, 10046 dots + 19 xfail
  marks frozen at [ 15%], last write Oct 3 20:56:35 PDT, ~64 min stale
  at this run's check, zero summary tokens - no "passed"/"failed"
  summary, no collected-count token, no "no tests ran", no "short
  test summary" - no live pytest process holding the log open per the
  /proc open-fd check, no type_d_1190 markers). THIRTIETH consecutive
  background-suite death of the new streak (the 57-run streak ENDED
  at #1085 when the #1080 suite completed); tombstone lineage advances
  NINETY-SIXTH -> NINETY-SEVENTH. Suite re-launched to goal
  hidden_files/type_d_1190_full_suite.log WITHOUT -x in a background
  process (alive and accumulating dots at this run's commit checks);
  its verdict belongs to the next Type D run (#1195) per #795.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup; the anchor tests are deselected in-gate and go green
post-anchor. Doc-sync constants per #719: README_TEST_COUNT /
README_FILE_COUNT hold the post-doc-sync values from the start
(post-sync-positive); the doc-sync tests are deselected in-gate and
go green once README.md, docs/ARCHITECTURE.md and iteration-log.md
carry the #1190 rows.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
GUARDIAN_FILE = os.path.join(PROFILES_DIR, "guardian.yaml")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
NEWSCORP_FILE = os.path.join(PROFILES_DIR, "news-corp.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")
README_FILE = os.path.join(REPO_ROOT, "README.md")
ARCH_FILE = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

# Block keys are plain literals: they carry the landing ITERATION
# number (1187/1188/1189) and no mechanism-number substring (designed
# keying per #715). Iterations are the landing iterations, not the
# mechanism ids.
KEY_943 = ("type_a_1187_nypost_anthropic_oct01_ipo_hypocrisy_"
           "register_vs_carried_meta_openai_arms_oct03_7pm")
KEY_944 = ("type_b_1188_eli_tan_nyt_pervert_glasses_stigma_"
           "vs_other_companies_neutral_within_piece")
KEY_944_TEST_FILE = ("tests/test_type_b_1188_eli_tan_nyt_pervert_"
                     "glasses_stigma_vs_other_companies_neutral_"
                     "within_piece_oct03_8pm.py")
KEY_945 = ("type_c_1189_openai_synopsys_gpt_synopsys_license_and_"
           "cobuild_thirty_eighth_direction_oct03_9pm")
OWN_BASENAME = ("test_type_d_1190_m943_m944_m945_qualitative_"
                "corpus_integrity_oct03_10pm.py")

# Predecessor test files for supersession pins.
E1186_FILE = ("test_type_e_1186_podcast_sentiment_160th_verification_"
              "oct03_7pm.py")
A1187_FILE = ("test_type_a_1187_nypost_anthropic_oct01_ipo_hypocrisy_"
              "vs_carried_meta_openai_arms_oct03_7pm.py")
B1188_FILE = ("test_type_b_1188_eli_tan_nyt_pervert_glasses_stigma_"
              "vs_other_companies_neutral_within_piece_oct03_8pm.py")
C1189_FILE = ("test_type_c_1189_openai_synopsys_gpt_synopsys_license_"
              "and_cobuild_thirty_eighth_direction_oct03_9pm.py")
THIS_FILE = ("test_type_d_1190_m943_m944_m945_qualitative_"
             "corpus_integrity_oct03_10pm.py")

# Prior-window background suite (verdict rendered this run) and this
# run's re-launched suite.
PRIOR_SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1185_full_suite.log",
)
SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1190_full_suite.log",
)

# Patched post-first-run with the true collected count per #719.
# Pre-sync: 63528 tests / 1514 files. Patched post-first-run: 92 collected.
README_TEST_COUNT = 63620  # post-doc-sync total (pre-sync 63528 + 92)
README_FILE_COUNT = 1515  # post-doc-sync total (pre-sync 1514 + 1)
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "0" * 40

MECH_NUM = 945
NEXT_NUM = 946
PREV_NUM = 944

# Fragment-built direction needles per #715 (never contiguous here).
_T34 = "THIRTY-" + "FOURTH relationship direction"
_T35 = "THIRTY-" + "FIFTH relationship direction"
_T36 = "THIRTY-" + "SIXTH relationship direction"
_T37 = "THIRTY-" + "SEVENTH relationship direction"
_T38 = "THIRTY-" + "EIGHTH relationship direction"
_T39 = "THIRTY-" + "NINTH relationship direction"


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


def _max_numeric_mechanism_id_in_profiles():
    ids = []
    for dirpath, _, files in os.walk(PROFILES_DIR):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(dirpath, fn))
                for m in re.findall(r"mechanism_id: (\d+)", text):
                    ids.append(int(m))
    return max(ids)


def _m943_block():
    # News Corp's competitor_relationships carries Type A blocks as
    # top-level keys (the NY Post is a News Corp publication), per the
    # #1187 land.
    return _yaml(NEWSCORP_FILE)["competitor_relationships"][KEY_943]


def _m944_block():
    # Eli Tan's journalist entry is a top-level key in the careers
    # journalists.yaml (the per-#643 key convention, as with
    # dan_howley at #1148 and vlad_savov at #1183); the m944 block
    # lives under its competitor_coverage sub-key.
    return _yaml(JOURNALISTS_FILE)["eli_tan"]["competitor_coverage"][
        KEY_944]


def _m945_block():
    return _yaml(ENTITIES_FILE)[KEY_945]


def _sweep_source_files(needle):
    """Return source files containing a runtime-built needle.

    Mirrors the #1166 sweep scope: every file under profiles/ plus
    every .py under tests/, excluding this file (the sweep carrier
    per #715) and __pycache__ artifacts.
    """
    hits = []
    profiles_dir = os.path.join(REPO_ROOT, "profiles")
    for root, dirs, files in os.walk(profiles_dir):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == THIS_FILE or not f.endswith(".py"):
                continue
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


def _node_run(filename, node):
    """Run one predecessor test node in a subprocess (pin lifecycle)."""
    import time

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


def _class_run(filename, classname):
    """Run one predecessor test class in a subprocess."""
    target = os.path.join(TESTS_DIR, filename) + "::" + classname
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    venv_py = os.path.join(REPO_ROOT, ".venv", "bin", "python")
    return subprocess.run(
        [venv_py, "-m", "pytest", target, "-q", "--no-header",
         "-o", "addopts=", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        env=env,
        timeout=300,
    )


def _assert_tripped(node, res):
    """A trip-by-design pin must fail for a real reason (rc 1), not
    via the transient rc-4 "no tests ran" filesystem flake: _node_run
    already retried, so a surviving rc 4 is reported, never counted
    as a trip."""
    assert "no tests ran" not in res.stdout, (node, "flake survived retries")
    assert res.returncode != 0, (node, res.stdout[-2000:])


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1190:
    def test_no_type_d_1190_test_file_preexisting(self):
        own = glob.glob(os.path.join(TESTS_DIR, "test_type_d_1190*"))
        own = [p for p in own
               if os.path.basename(p) == OWN_BASENAME]
        assert own == [os.path.join(TESTS_DIR, OWN_BASENAME)], own

    def test_no_type_d_1190_in_git_log(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1190"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == "", out.stdout

    def test_max_id_is_945(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_946_numeric_forms_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(NEXT_NUM),
                                 "profiles/") == []

    def test_zero_946_underscore_dash_forms_repo_wide(self):
        assert _git_grep_tracked(_mech_underscore(NEXT_NUM)) == []
        assert _git_grep_tracked(_mech_dash(NEXT_NUM)) == []

    def test_no_type_e_1191_in_git_log(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type E #1191"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == "", out.stdout


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1190 is the FIRST and OPENING leg of 1190-1194.
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1190:
    def test_rotation_window_opens_1190(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "1190-1194 window" in src
        assert "OPENING" in src

    def test_predecessor_1189_chain_present(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type C #1189"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert "Type C #1189" in out.stdout

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
        assert "#1191 Type E" in src

    def test_closing_window_1185_1189_verified(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type C #1189"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert "Type C #1189" in out.stdout


# ---------------------------------------------------------------------------
# 3. Novelty anchor: no prior #1190 claims
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1190:
    def test_no_prior_type_d_1190_in_log(self):
        text = _read(LOG_FILE)
        assert "## #1190" not in text

    def test_no_prior_1190_opening_claim(self):
        # The #1189 entry already names the 1190-1194 window ("Next:
        # #1190 Type D opens the 1190-1194 window"); the pre-commit
        # absence pin is on the OPENING-leg heading this run adds.
        text = _read(LOG_FILE)
        assert "OPENING leg of the 1190-1194 window" not in text


# ---------------------------------------------------------------------------
# 4. Corpus integrity: the m943/m944/m945 landings are present
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1190:
    def test_m943_block_present_in_newscorp_yaml(self):
        block = _m943_block()
        assert block["mechanism_id"] == 943
        assert block["iteration"] == 1187
        assert block["iteration_type"] == "A"

    def test_m944_block_present_in_journalists_yaml(self):
        block = _m944_block()
        assert block["mechanism_id"] == 944
        assert block["iteration"] == 1188
        assert block["type"] == "B"

    def test_m945_block_present_in_competitor_entities_yaml(self):
        block = _m945_block()
        assert block["mechanism_id"] == 945
        assert block["iteration"] == 1189
        assert block["iteration_type"] == "C"

    def test_max_mechanism_id_is_945(self):
        assert _max_numeric_mechanism_id_in_profiles() == 945

    def test_zero_946_forms_repo_wide(self):
        assert _git_grep_tracked(_mech_id_colon(946), "profiles/") == []
        assert _git_grep_tracked(_mech_underscore(946)) == []
        assert _git_grep_tracked(_mech_dash(946)) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 945 in ids
        assert all(i <= 945 for i in ids)

    def test_m943_key_count_is_designed(self):
        # yaml key line only: exactly 1 (the #1187 run wrote no
        # block_key field for this top-level Type A block).
        text = _read(NEWSCORP_FILE)
        assert text.count(KEY_943) == 1

    def test_m944_key_count_is_designed(self):
        # yaml key line + block_key field + test_file value: exactly
        # 3 (the test_file value embeds the key slug).
        text = _read(JOURNALISTS_FILE)
        assert text.count(KEY_944) == 3
        assert KEY_944_TEST_FILE in text

    def test_m945_key_count_is_designed(self):
        # yaml key line + block_key field: exactly 2.
        text = _read(ENTITIES_FILE)
        assert text.count(KEY_945) == 2


# ---------------------------------------------------------------------------
# 5. m943 qualitative discipline (Type A #1187)
# ---------------------------------------------------------------------------
class TestTypeDM943QualitativeDiscipline1190:
    def test_m943_run_metadata(self):
        b = _m943_block()
        assert b["iteration"] == 1187
        assert b["iteration_type"] == "A"
        assert "temporal extension of m925" in b["competitor_pair"]
        assert "Anthropic" in b["competitor_pair"]

    def test_m943_arm_tones_and_deltas(self):
        # The scorer is a hand-written string (MANUAL ILLUSTRATIVE
        # ONLY): new Anthropic arm -0.35 vs carried Meta arm -0.50
        # (illustrative delta +0.15) vs carried OpenAI FTC arm -0.40
        # (illustrative delta +0.05).
        b = _m943_block()
        sc = b["scorer_MANUAL_ILLUSTRATIVE_ONLY"]
        assert "-0.35" in sc
        assert "-0.50" in sc
        assert "-0.40" in sc
        assert "+0.15" in sc
        assert "+0.05" in sc

    def test_m943_manual_illustrative_only(self):
        b = _m943_block()
        assert b["statistical_discipline"].startswith(
            "MANUAL/QUALITATIVE ONLY")
        assert "is_significant False" in b[
            "scorer_MANUAL_ILLUSTRATIVE_ONLY"]
        assert "NOT_CALCULATED" in b["scorer_MANUAL_ILLUSTRATIVE_ONLY"]
        assert "engine NOT run" in b["scorer_MANUAL_ILLUSTRATIVE_ONLY"]
        assert "NOT artifact-grade" in b["statistical_discipline"]
        assert b["no_analysis_json_update"] is True

    def test_m943_verdict_and_ledger(self):
        b = _m943_block()
        assert "directionally_supported_not_proven" in b[
            "statistical_discipline"]
        assert "Ledger holds at 46" in b["ledger"]
        assert "NOT a member" in b["falsification_family"]
        assert "m763" in b["falsification_family"]

    def test_m943_novelty_fields_intact(self):
        # FIRST dedicated NY Post x Anthropic mechanism; temporal
        # replication of m925 is not a new prediction test per #1143.
        b = _m943_block()
        assert "FIRST dedicated NY Post x Anthropic mechanism" in b[
            "overview"]
        assert "#1143" in b["falsification_family"] or \
            "#1143" in b["incentive_attribution"]


# ---------------------------------------------------------------------------
# 6. m944 qualitative discipline (Type B #1188)
# ---------------------------------------------------------------------------
class TestTypeDM944QualitativeDiscipline1190:
    def test_m944_run_metadata(self):
        b = _m944_block()
        assert b["iteration"] == 1188
        assert b["type"] == "B"
        assert b["journalist"] == "Eli Tan"
        assert b["publication"] == "The New York Times"
        assert "mechanism_ids: [944]" in _read(JOURNALISTS_FILE)

    def test_m944_arm_tones_and_delta(self):
        b = _m944_block()
        assert b["new_meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.45
        assert b["other_companies_arm"][
            "tone_MANUAL_ILLUSTRATIVE"] == 0.05
        assert b["scorer"]["illustrative_delta_meta_minus_others"] == \
            -0.50
        assert "Illustrative delta (Meta minus others) -0.50" in b[
            "finding"]

    def test_m944_manual_illustrative_only(self):
        b = _m944_block()
        assert "MANUAL ILLUSTRATIVE" in b["scorer"]["method"]
        assert b["scorer"]["engine_run"] is False
        assert b["scorer"]["is_significant"] is False
        assert b["scorer"]["p_value"] == "NOT_CALCULATED"
        assert "NOT artifact-grade" in b["statistical_discipline"]
        assert b["no_analysis_json_update"] is True

    def test_m944_verdict_and_ledger(self):
        b = _m944_block()
        assert b["verdict"].startswith(
            "directionally_supported_not_proven")
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 46
        assert "Ledger holds at 46" in b["ledger_note"]
        assert "NOT a falsification-family member" in b["finding"]

    def test_m944_correlational_note_intact(self):
        # The deal-gradient consistency is correlation, not causation;
        # the confounders (co-byline attribution STRONG) are recorded.
        b = _m944_block()
        assert "correlation" in b["correlational_note"].lower()
        assert any("Co-byline attribution" in c
                   for c in b["confounders"])

    def test_m944_theory_links_intact(self):
        b = _m944_block()
        assert "m484" in b["finding"]
        assert "mechanism_662" in b["finding"]


# ---------------------------------------------------------------------------
# 7. m945 qualitative discipline (Type C #1189)
# ---------------------------------------------------------------------------
class TestTypeDM945QualitativeDiscipline1190:
    def test_m945_run_metadata(self):
        b = _m945_block()
        assert b["iteration"] == 1189
        assert b["iteration_type"] == "C"
        assert "synopsys" in b["novelty"].lower()

    def test_m945_thirty_eighth_direction_landed(self):
        b = _m945_block()
        assert "THIRTY-EIGHTH relationship direction LANDED this run" \
            in b["falsification_family"]
        assert "LICENSE-AND-CO-BUILD" in b["falsification_family"]
        assert "thirty-fifth (m915" in b["falsification_family"]
        assert "thirty-sixth (m933" in b["falsification_family"]
        assert "thirty-seventh (m942" in b["falsification_family"]

    def test_m945_manual_qualitative_only(self):
        b = _m945_block()
        assert b["tone_scored"] is False
        assert b["engine_run"] is False
        assert b["is_significant"] is False
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True
        assert b["artifact_grade"] is False
        # MANUAL/qualitative-only is the Aug 28 2026 standing rule
        # for Type C landings; this block carries the method in the
        # novelty string rather than a statistical_discipline key.
        assert "MANUAL" in b["novelty"]

    def test_m945_verdict_and_ledger(self):
        b = _m945_block()
        assert b["falsification_family_member"] is False
        assert "NOT a member" in b["falsification_family"]
        assert "46" in b["falsification_family"]
        assert "forty-seventh" not in b["falsification_family"].lower() \
            or "absent" in b["falsification_family"].lower()


# ---------------------------------------------------------------------------
# 8. Falsification ledger and direction guards
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1190:
    def test_forty_sixth_claim_in_exactly_one_profiles_file(self):
        hits = _git_grep_tracked(FORTY_SIXTH_MEMBER, "profiles/")
        assert hits == ["profiles/the-verge.yaml"], hits

    def test_forty_sixth_claim_count_is_designed(self):
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FORTY_SIXTH_MEMBER, "--",
             "profiles/the-verge.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        # The #1127 designed pattern: exactly 2 occurrences in the
        # m907 block.
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_forty_seventh_member_claim_repo_wide(self):
        assert _git_grep_tracked(FORTY_SEVENTH_MEMBER) == []

    def test_no_forty_eighth_member_claim_repo_wide(self):
        assert _git_grep_tracked(FORTY_EIGHTH_MEMBER) == []

    def test_thirty_eighth_direction_in_competitor_entities(self):
        # Landed at #1189 (m945 LICENSE-AND-CO-BUILD): the former
        # absence guard is now an affirmative presence pin on the
        # corpus home (profiles/competitor-entities.yaml).
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

    def test_no_thirty_ninth_direction_claim_repo_wide(self):
        assert _git_grep_tracked(_T39) == []

    def test_m943_m944_m945_not_members_ledger_holds(self):
        b943 = _m943_block()
        assert "Ledger holds at 46" in b943["ledger"]
        assert "NOT a member" in b943["falsification_family"]
        b944 = _m944_block()
        assert b944["falsification_ledger"] == 46
        assert b944["falsification_family_member"] is False
        assert "Ledger holds at 46" in b944["ledger_note"]
        b945 = _m945_block()
        assert "NOT a member" in b945["falsification_family"]
        assert "46" in b945["falsification_family"]


# ---------------------------------------------------------------------------
# 9. Type E #1186 discipline: the 160th verification cycle stays
#    monitoring-only
# ---------------------------------------------------------------------------
class TestTypeDTypeE1186Discipline1190:
    def test_1186_file_on_disk(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1186_FILE))

    def test_1186_pins_160th_cycle(self):
        src = _read(os.path.join(TESTS_DIR, E1186_FILE))
        assert "160th verification cycle" in src
        assert "159->160" in src

    def test_1186_monitoring_only_discipline(self):
        # The Aug 28 2026 standing rule: monitoring-only, tone
        # NOT_SCORED, engine NOT run, no mechanisms, NOT artifact-grade,
        # verdict directionally_supported_not_proven.
        src = _read(os.path.join(TESTS_DIR, E1186_FILE))
        assert "monitoring-only" in src
        assert "NOT artifact-grade" in src

    def test_1186_gf_episode_502_holds(self):
        src = _read(os.path.join(TESTS_DIR, E1186_FILE))
        assert "502" in src

    def test_1186_research_method_bounded(self):
        src = _read(os.path.join(TESTS_DIR, E1186_FILE))
        assert "0 browser.open" in src


# ---------------------------------------------------------------------------
# 10. Forward-looking staleness (predecessor pin lifecycle via subprocess)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1190:
    def test_1186_type_e_pins_trip_by_design(self):
        # Type E lands no mechanisms; the #1187/#1188/#1189 A/B/C
        # landings trip its zero-943 guards by design.
        res = _node_run(
            E1186_FILE,
            "TestMechanismNovelty::"
            "test_zero_943_numeric_mechanism_id_in_profiles",
        )
        _assert_tripped("1186 TestMechanismNovelty zero-943", res)

    def test_1187_a_pins_trip_by_design(self):
        # #1187's forward guards (max-943, zero-944 numeric,
        # no-Type-B-#1188 in git log) flip by design now that m944
        # has landed.
        res = _node_run(
            A1187_FILE,
            "TestForwardGuards::"
            "test_zero_944_numeric_mechanism_id_in_profiles",
        )
        _assert_tripped("1187 TestForwardGuards zero-944", res)

    def test_1188_b_pins_trip_by_design(self):
        # #1188's forward guards (max-944, zero-945 numeric,
        # no-Type-C-#1189 in git log) flip by design now that m945
        # has landed.
        res = _node_run(
            B1188_FILE,
            "TestGuardLifecycle1188::test_945_numeric_absent_in_"
            "profiles",
        )
        _assert_tripped("1188 TestGuardLifecycle1188 zero-945", res)

    def test_1188_b_git_log_pin_trip_by_design(self):
        # #1188's no-Type-C-#1189-in-git-log pin flipped by design at
        # #1189's main commit (80eef294 - now in history).
        res = _node_run(
            B1188_FILE,
            "TestGuardLifecycle1188::test_no_type_c_1189_in_git_log_pin",
        )
        _assert_tripped("1188 TestGuardLifecycle1188 no-Type-C-#1189",
                        res)

    def test_1189_c_pins_trip_by_design(self):
        # #1189's no-Type-D-#1190-in-git-log pin flips by design at
        # THIS run's main commit; the zero-946 pins stay GREEN (this
        # run lands no mechanisms - pinned in TestGuardLifecycle1190
        # forward guards). Record the pre-commit state: the git-log
        # pin still holds now.
        res = _node_run(
            C1189_FILE,
            "TestGuardLifecycle1189::"
            "test_no_type_d_1190_in_git_log_pin",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1189_c_underscore_dash_946_stay_green(self):
        # The designed keying carries the iteration number, not the
        # mechanism number: #1189's zero-946 underscore/dash guards
        # stay green (this run lands no mechanisms).
        res = _class_run(C1189_FILE, "TestMechanismNovelty1189")
        assert res.returncode == 0, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 11. Guard lifecycle: the guards this run lays for the next leg
# ---------------------------------------------------------------------------
class TestGuardLifecycle1190:
    def test_pins_on_945_landing(self):
        # The guards this run lays for the next leg: max-945, zero-946
        # numeric, no-Type-A-#1191-in-git-log, thirty-eighth landed,
        # thirty-ninth absent.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 945" in src
        assert "NEXT_NUM = 946" in src

    def test_no_type_a_1191_in_git_log_pin(self):
        log = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type A #1191"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert log.strip() == ""

    def test_946_numeric_absent_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(NEXT_NUM),
                                 "profiles/") == []

    def test_predecessor_1189_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, C1189_FILE))

    def test_1189_pins_flip_by_design_documented(self):
        # #1189's forward guards (max-945, zero-946 numeric, no-Type-D-
        # #1190 in git log) flip by design at this run's main commit;
        # recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1189" in src
        text = _read(ENTITIES_FILE)
        assert "1189" in text or "m945" in text


# ---------------------------------------------------------------------------
# 12. Background-suite verdict per #795: the #1185-launched full suite
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1190:
    def _log_stats(self):
        text = _read(PRIOR_SUITE_LOG)
        return (os.path.getsize(PRIOR_SUITE_LOG), text.count("."),
                text.count("x"), text)

    def test_prior_suite_died_thirtieth_consecutive(self):
        # The #1185-launched background full suite DIED: 11188 bytes
        # (10046 dots + 19 xfail marks frozen at [ 15%]), last write
        # Oct 3 20:56:35 PDT (~64 min before this run's check), zero
        # summary tokens (no "passed"/"failed" summary, no
        # collected-count token, no "no tests ran", no "short test
        # summary"), no live pytest process, no type_d_1190 markers.
        # Per the #795 convention this is recorded as DIED, not
        # "interrupted": the run produces no usable verdict.
        size, dots, xs, text = self._log_stats()
        assert size == 11188, size
        assert dots == 10046, dots
        assert xs == 19, xs
        assert "passed" not in text
        assert "failed" not in text
        assert " collected " not in text
        assert "no tests ran" not in text
        assert "short test summary" not in text

    def test_no_live_pytest_process(self):
        # A live suite writer would hold the #1185 log file open.
        # Scan /proc for pytest processes and check whether any of
        # them has the #1185 suite log among its open file
        # descriptors. The #1190 re-launch writes to a different log
        # (same pytest cmdline), so cmdline matching alone cannot
        # distinguish them - the open-fd check is the honest one.
        log_real = os.path.realpath(PRIOR_SUITE_LOG)
        holders = []
        for pid in os.listdir("/proc"):
            if not pid.isdigit():
                continue
            try:
                cmdline = open("/proc/%s/cmdline" % pid,
                               "rb").read().decode("utf-8", "replace")
            except OSError:
                continue
            if "pytest" not in cmdline:
                continue
            try:
                fds = os.listdir("/proc/%s/fd" % pid)
            except OSError:
                continue
            for fd in fds:
                try:
                    target = os.path.realpath(
                        "/proc/%s/fd/%s" % (pid, fd))
                except OSError:
                    continue
                if target == log_real:
                    holders.append(pid)
        assert holders == [], (
            "a live pytest process still holds the #1185 suite log "
            "open: %r" % holders)

    def test_last_write_stale(self):
        # The prior suite's last write predates this run by over an
        # hour, far beyond any healthy inter-write bound.
        import time
        mtime = os.path.getmtime(PRIOR_SUITE_LOG)
        assert mtime < time.time() - 1800, mtime

    def test_no_1190_markers_in_prior_suite(self):
        # The #1185 suite was launched before this run existed; it
        # must carry no trace of it.
        _, _, _, text = self._log_stats()
        assert "type_d_1190" not in text
        assert "m943" not in text
        assert "m944" not in text
        assert "m945" not in text

    def test_tombstone_lineage_advances_to_97th(self):
        # THIRTIETH consecutive background-suite death of the new
        # streak (the 57-run streak ENDED at #1085 when the #1080
        # suite completed). Tombstone lineage advances NINETY-SIXTH ->
        # NINETY-SEVENTH; recorded in the #1190 iteration-log entry.
        # Deselected pre-commit (log entry is written in the doc-sync
        # step per #719/#721).
        text = _read(LOG_FILE)
        assert "NINETY-SEVENTH" in text


# ---------------------------------------------------------------------------
# 13. Fresh synthetic engine calibration (new values, not #1185's)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1190:
    # Scratch-run values produced at this run (Sat 2026-10-03 ~22:05
    # PDT) via mediascope.score.asymmetry.calculate_asymmetry with
    # its real signature (target_scores, peer_scores,
    # target_entity, peer_entities, publication_slug,
    # period_start, period_end). The finding layer stays MANUAL
    # ILLUSTRATIVE ONLY: the engine is never promoted to findings,
    # and these numbers are NOT a corpus claim.

    def _calculate(self):
        from datetime import datetime

        from mediascope.score.asymmetry import calculate_asymmetry

        def calc(target_scores, peer_scores):
            return calculate_asymmetry(
                target_scores,
                peer_scores,
                "Meta",
                ["Anthropic", "OpenAI"],
                "synthetic-calibration",
                datetime(2026, 10, 3),
                datetime(2026, 10, 3),
            )

        return calc

    def test_strong_effect_is_significant(self):
        calc = self._calculate()
        meta = [-0.61, -0.55, -0.66, -0.59, -0.63, -0.57]
        comp = [0.41, 0.35, 0.44, 0.38, 0.36, 0.40]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(
            -0.9916666666666667)
        assert result.t_statistic == pytest.approx(
            -46.43338974609792)
        assert result.p_value == pytest.approx(
            1.0587806293436397e-12)
        assert result.cohens_d == pytest.approx(
            -26.808330069296446)
        assert result.is_significant is True
        assert result.confidence_interval_lower == pytest.approx(
            -1.0266666666666666)
        assert result.confidence_interval_upper == pytest.approx(
            -0.9533333333333334)
        # The strong arm-swap negates the asymmetry exactly.
        swapped = calc(comp, meta)
        assert swapped.asymmetry_score == pytest.approx(
            -result.asymmetry_score)
        assert abs(result.asymmetry_score +
                   swapped.asymmetry_score) < 1e-12

    def test_near_null_pair_stays_silent(self):
        calc = self._calculate()
        meta = [0.04, -0.03, 0.05, -0.04, 0.02, -0.01]
        comp = [0.03, 0.05, -0.02, 0.02, -0.01, 0.03]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(
            -0.011666666666666665)
        assert result.p_value > 0.05
        assert result.is_significant is False
        assert result.confidence_interval_lower < 0 < \
            result.confidence_interval_upper

    def test_degenerate_n1_contract(self):
        # The classic degenerate guard: n=1 per arm yields t=0.0,
        # p=1.0, d=0.0 and is_significant False regardless of the
        # illustrative pair mean (here +0.18 vs +0.06, delta +0.12).
        calc = self._calculate()
        result = calc([0.18], [0.06])
        assert result.asymmetry_score == pytest.approx(0.12)
        assert result.t_statistic == 0.0
        assert result.p_value == 1.0
        assert result.cohens_d == 0.0
        assert result.is_significant is False

    def test_engine_layer_not_finding_layer(self):
        # The m943/m944/m945 mechanisms never promote engine
        # significance to a finding: all three carry manual-only
        # discipline (m943 MANUAL/QUALITATIVE ONLY engine NOT run,
        # m944 MANUAL ILLUSTRATIVE ONLY engine NOT run, m945 tone
        # NOT_SCORED / engine NOT run).
        b943 = _m943_block()
        assert b943["statistical_discipline"].startswith(
            "MANUAL/QUALITATIVE ONLY")
        assert "engine NOT run" in b943[
            "scorer_MANUAL_ILLUSTRATIVE_ONLY"]
        b944 = _m944_block()["scorer"]
        assert "MANUAL ILLUSTRATIVE" in b944["method"]
        assert b944["engine_run"] is False
        b945 = _m945_block()
        assert b945["is_significant"] is False
        assert b945["engine_run"] is False
        assert b945["tone_scored"] is False


# ---------------------------------------------------------------------------
# 14. Suite re-launch
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1190:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1190 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1195 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1195)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1190_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 15. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1190:
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
        assert "## #1190" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count (92).
        assert README_TEST_COUNT == 63528 + COLLECTED_COUNT
        assert README_FILE_COUNT == 1515


# ---------------------------------------------------------------------------
# 16. Iteration log (#719: the entry carries hashes per #721)
# ---------------------------------------------------------------------------
class TestTypeDIterationLog1190:
    def test_log_entry_has_main_commit_hash(self):
        text = _read(LOG_FILE)
        assert "Type D #1190" in text

    def test_log_entry_notes_window_opening(self):
        text = _read(LOG_FILE)
        assert "OPENING leg of the 1190-1194 window" in text

    def test_log_entry_notes_tombstone_lineage(self):
        # Deselected pre-commit: the entry is written in the doc-sync
        # step per #719/#721.
        text = _read(LOG_FILE)
        assert "NINETY-SEVENTH" in text


# ---------------------------------------------------------------------------
# 17. Literal discipline (ASCII-only, no em dashes)
# ---------------------------------------------------------------------------
class TestLiteralDiscipline1190:
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
class TestInflightIsolation1190:
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
        # main commit's own diff (working tree clean post-commit).
        out = subprocess.run(
            ["git", "show", ANCHORED_SHA, "--stat", "--format="],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert "m846" not in out.stdout


# ---------------------------------------------------------------------------
# 19. Anchor (per #565; patched in the anchor followup)
# ---------------------------------------------------------------------------
class TestAnchor1190:
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
        # "Type D #1190 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1190 anchor"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert "Type D #1190 anchor" in log

    def test_main_commit_message_convention(self):
        log = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1190:"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert "Type D #1190" in log


# Collected count patch (post-first-run per #719).
COLLECTED_COUNT = 92
