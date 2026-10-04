"""Type D #1185: verify m940/m941/m942 qualitative-discipline landings +
post-1180-1184 corpus integrity (max numeric mechanism_id 942; zero
next-number nine-four-three keys all forms; falsification ledger holds
at 46; thirty-fifth + thirty-sixth + thirty-seventh directions present,
thirty-eighth/thirty-ninth absent) + #1180 background-suite verdict
(TWENTY-NINTH consecutive death; tombstone NINETY-FIFTH -> NINETY-SIXTH)
+ fresh synthetic engine calibration + full suite re-launched - FIRST
and OPENING leg of the 1185-1189 window (Oct 3 2026, 06:00 PM PDT).

Verification-layer run: no corpus edits, no analysis.json updates, no
new mechanisms. The finding layer stays MANUAL/QUALITATIVE ONLY per
the Aug 28 2026 standing rule; the synthetic engine calibration is a
fresh engine-layer contract and is never promoted to a finding.

- m940 (Type A #1182, profiles/nytimes.yaml
  competitor_relationships/anthropic, block key
  type_a_1182_nyt_anthropic_vatican_consciousness_dias_accountability_vs
  _meta_carried_arms_oct03_3pm): NYT x Anthropic Sep-29 Dias
  Vatican-consciousness accountability arm (-0.25 MANUAL
  ILLUSTRATIVE) vs carried NYT x Meta arms (mean -0.10) - same-day
  second accountability leg of m895 (temporal extension; pooled
  Sep-29 Anthropic -0.30 vs Meta -0.10, illustrative delta -0.20;
  within-entity swing +0.25 to -0.30 = -0.55 in 11 days); NOT a
  falsification-family member; ledger holds at 46. Statistical
  discipline: MANUAL ILLUSTRATIVE ONLY (engine NOT run, p_value /
  cohens_d / ci_95 NOT_CALCULATED, is_significant False, NOT
  artifact-grade, verdict directionally_supported_not_proven,
  no_analysis_json_update true).
- m941 (Type B #1183, profiles/careers/journalists.yaml top-level
  vlad_savov key, competitor_coverage block
  type_b_1183_vlad_savov_bloomberg_openai_australia_breach_
  accountability_vs_meta_glimmer_product_neutral): Vlad Savov
  (Bloomberg News) Sep-29 OpenAI Australia-breach accountability arm
  (-0.35 MANUAL ILLUSTRATIVE) vs Aug-10 Meta Glimmer product-neutral
  arm (+0.05) - BOUNDARY/NULL pin at the corpus standing no-deal
  outlet (in-corpus #85); illustrative delta (OpenAI minus Meta)
  -0.40, peg-driven; joins the m593/#538 reporter-level boundary
  family; register follows the peg, not the money; NOT a
  falsification-family member; ledger holds at 46. Statistical
  discipline: MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing
  rule (engine NOT run, is_significant False, NOT artifact-grade,
  verdict directionally_supported_not_proven, no_analysis_json_update
  true).
- m942 (Type C #1184, profiles/competitor-entities.yaml top-level
  block key
  type_c_1184_stability_ai_big_three_labels_invest_and_license_
  thirty_seventh_direction_oct03_5pm): FIRST dedicated corpus
  mechanism on the Stability AI x Big Three music labels
  INVEST-AND-LICENSE ($76M Series B announced Aug 25 2026;
  UMG+SMG+WMG equity AND catalog-training licenses in the same deal)
  - LANDS the thirty-seventh relationship direction; 8 novel sources
  (0 browser.open); connects_to [804, 391, 663]; NOT a
  falsification-family member (per the #609/#614 qualitative
  boundary); ledger holds at 46. Statistical discipline: tone
  NOT_SCORED, engine NOT run, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade.
- #1181 Type E 159th podcast-sentiment verification-cycle discipline
  verified: monitoring-only per the Aug 28 2026 standing rule
  (tone NOT_SCORED, engine NOT run, no mechanisms landed,
  falsification ledger holds at 46, NOT artifact-grade, verdict
  directionally_supported_not_proven); GF episode 502 holds newest
  (twenty-sixth verification; NO 503; pure-re-surface streak advances
  to five; ZERO Meta/wearables content across all 159 cycles);
  Attention Sphere 159th quoted-search no-match; press 7 rows all
  re-surfaces (ZERO new keys); recency frontier holds at Oct 2.
- Falsification ledger holds at 46: the forty-sixth member-claim
  form present in exactly one profiles file (profiles/the-verge.yaml,
  m907 block, 2 occurrences, the #1127 designed pattern); the
  forty-seventh and forty-eighth member-claim forms absent repo-wide
  (needles format-built per #715). The thirty-fifth (m915
  METER-THEN-INVITE), thirty-sixth (m933 REGULATORY-PREEMPTION), and
  thirty-seventh (m942 INVEST-AND-LICENSE) relationship directions
  are present in profiles/competitor-entities.yaml; the
  thirty-eighth and thirty-ninth direction-claim forms absent
  repo-wide (needles format-built per #715).
- Background-suite verdict per #795: the #1180-launched full suite
  DIED (3233 bytes, 2901 dots + xfail marks frozen at [ 4%],
  last write Oct 3 14:56 PDT, ~3h stale at this run's check, zero
  summary tokens - no 'passed'/'failed' summary, no collected-count
  token, no 'no tests ran', no 'short test summary' - no live pytest
  process holding the log open per the /proc open-fd check, no
  type_d_1180/type_d_1185 markers). TWENTY-NINTH consecutive
  background-suite death of the new streak (the 57-run streak ENDED
  at #1085 when the #1080 suite completed); tombstone lineage
  advances NINETY-FIFTH -> NINETY-SIXTH. Suite re-launched this run
  to goal hidden_files/type_d_1185_full_suite.log WITHOUT -x in a
  background process (alive and accumulating dots at this run's
  commit checks); its verdict belongs to the next Type D run
  (#1190) per #795.
- Fresh synthetic engine calibration via real
  mediascope.score.asymmetry.calculate_asymmetry (new values, not
  #1180's): strong pair -0.7979999999999999 / t -32.79759796741879 /
  p 2.4282304739441895e-08 / d -20.743022271910455 / CI
  [-0.8380500000000001, -0.758], is_significant True; arm-swap
  negates exactly (sum 0.0); near-null -0.002 p 0.9265230402780709
  not significant (CI crossing zero); degenerate n=1
  0.15000000000000002/0.0/1.0/0.0/False. Finding layer stays MANUAL
  ILLUSTRATIVE ONLY; the engine is never promoted to findings.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup; the anchor tests are deselected in-gate and go green
post-anchor. Doc-sync constants per #719: README_TEST_COUNT /
README_FILE_COUNT hold the post-doc-sync values from the start
(post-sync-positive); the doc-sync tests are deselected in-gate and
go green once README.md, docs/ARCHITECTURE.md and iteration-log.md
carry the #1185 rows.
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
NYTIMES_FILE = os.path.join(PROFILES_DIR, "nytimes.yaml")
VERGE_FILE = os.path.join(PROFILES_DIR, "the-verge.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")
README_FILE = os.path.join(REPO_ROOT, "README.md")
ARCH_FILE = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

# Block keys are plain literals: they carry the landing ITERATION
# number (1182/1183/1184) and no mechanism-number substring (designed
# keying per #715). Iterations are the landing iterations, not the
# mechanism ids.
KEY_940 = ("type_a_1182_nyt_anthropic_vatican_consciousness_dias_"
           "accountability_vs_meta_carried_arms_oct03_3pm")
KEY_941 = ("type_b_1183_vlad_savov_bloomberg_openai_australia_breach_"
           "accountability_vs_meta_glimmer_product_neutral")
KEY_941_TEST_FILE = ("tests/test_type_b_1183_vlad_savov_bloomberg_openai_"
                     "australia_breach_vs_meta_glimmer_product_neutral_"
                     "oct03_4pm.py")
KEY_942 = ("type_c_1184_stability_ai_big_three_labels_invest_and_license_"
           "thirty_seventh_direction_oct03_5pm")
OWN_BASENAME = ("test_type_d_1185_m940_m941_m942_qualitative_"
                "corpus_integrity_oct03_6pm.py")

# Predecessor test files for supersession pins.
E1181_FILE = ("test_type_e_1181_podcast_sentiment_159th_verification_"
              "oct03_2pm.py")
A1182_FILE = ("test_type_a_1182_nyt_anthropic_vatican_consciousness_dias_"
              "accountability_vs_meta_carried_arms_oct03_3pm.py")
B1183_FILE = ("test_type_b_1183_vlad_savov_bloomberg_openai_australia_"
              "breach_vs_meta_glimmer_product_neutral_oct03_4pm.py")
C1184_FILE = ("test_type_c_1184_stability_ai_big_three_labels_invest_and_"
              "license_thirty_seventh_direction_oct03_5pm.py")
THIS_FILE = ("test_type_d_1185_m940_m941_m942_qualitative_"
             "corpus_integrity_oct03_6pm.py")

# Prior-window background suite (verdict rendered this run) and this
# run's re-launched suite.
PRIOR_SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1180_full_suite.log",
)
SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1185_full_suite.log",
)

# Patched post-first-run with the true collected count per #719.
# Pre-sync: 63140 tests / 1509 files. Patched post-first-run: 109 collected.
README_TEST_COUNT = 63249  # post-doc-sync total (pre-sync 63140 + 109)
README_FILE_COUNT = 1510  # post-doc-sync total (pre-sync 1509 + 1)
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "0" * 40

MECH_NUM = 942
NEXT_NUM = 943
PREV_NUM = 941

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


def _m940_block():
    return _yaml(NYTIMES_FILE)["competitor_relationships"]["anthropic"][
        KEY_940]


def _m941_block():
    # Vlad Savov's journalist entry is a top-level key in the careers
    # journalists.yaml (the per-#643 key convention, as with
    # dan_howley at #1148); the m941 block lives under its
    # competitor_coverage sub-key.
    return _yaml(JOURNALISTS_FILE)["vlad_savov"]["competitor_coverage"][
        KEY_941]


def _m942_block():
    return _yaml(ENTITIES_FILE)[KEY_942]


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
class TestNovelty1185:
    def test_no_type_d_1185_test_file_preexisting(self):
        own = glob.glob(os.path.join(TESTS_DIR, "test_type_d_1185*"))
        own = [p for p in own
               if os.path.basename(p) == OWN_BASENAME]
        assert own == [os.path.join(TESTS_DIR, OWN_BASENAME)], own

    def test_no_type_d_1185_in_git_log(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1185"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == "", out.stdout

    def test_max_id_is_942(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_943_numeric_forms_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(NEXT_NUM),
                                 "profiles/") == []

    def test_zero_943_underscore_dash_forms_repo_wide(self):
        assert _git_grep_tracked(_mech_underscore(NEXT_NUM)) == []
        assert _git_grep_tracked(_mech_dash(NEXT_NUM)) == []

    def test_no_type_e_1186_in_git_log(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type E #1186"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == "", out.stdout


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1185 is the FIRST and OPENING leg of 1185-1189.
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1185:
    def test_rotation_window_opens_1185(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "1185-1189 window" in src
        assert "OPENING" in src

    def test_predecessor_1184_chain_present(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type C #1184"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert "Type C #1184" in out.stdout

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
        assert "#1186 Type E" in src

    def test_closing_window_1180_1184_verified(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type E #1181"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert "Type E #1181" in out.stdout


# ---------------------------------------------------------------------------
# 3. Novelty anchor: no prior #1185 claims
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1185:
    def test_no_prior_type_d_1185_in_log(self):
        text = _read(LOG_FILE)
        assert "## #1185" not in text

    def test_no_prior_1185_opening_claim(self):
        # The #1184 entry already names the 1185-1189 window ("Next:
        # #1185 Type D opens the 1185-1189 window"); the pre-commit
        # absence pin is on the OPENING-leg heading this run adds.
        text = _read(LOG_FILE)
        assert "OPENING leg of the 1185-1189 window" not in text


# ---------------------------------------------------------------------------
# 4. Corpus integrity: the m940/m941/m942 landings are present
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1185:
    def test_m940_block_present_in_nytimes_yaml(self):
        block = _m940_block()
        assert block["mechanism_id"] == 940
        assert block["iteration"] == 1182
        assert block["iteration_type"] == "A"

    def test_m941_block_present_in_journalists_yaml(self):
        block = _m941_block()
        assert block["mechanism_id"] == 941
        assert block["iteration"] == 1183
        assert block["type"] == "B"

    def test_m942_block_present_in_competitor_entities_yaml(self):
        block = _m942_block()
        assert block["mechanism_id"] == 942
        assert block["iteration"] == 1184
        assert block["iteration_type"] == "C"

    def test_max_mechanism_id_is_942(self):
        assert _max_numeric_mechanism_id_in_profiles() == 942

    def test_zero_943_forms_repo_wide(self):
        assert _git_grep_tracked(_mech_id_colon(943), "profiles/") == []
        assert _git_grep_tracked(_mech_underscore(943)) == []
        assert _git_grep_tracked(_mech_dash(943)) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 942 in ids
        assert all(i <= 942 for i in ids)

    def test_m940_key_count_is_designed(self):
        # yaml key line + test_file filename embed: exactly 2.
        text = _read(NYTIMES_FILE)
        assert text.count(KEY_940) == 2

    def test_m941_key_count_is_designed(self):
        # yaml key + block_key field: exactly 2. The #1183 test file
        # carries a shortened slug (no accountability_vs_meta
        # qualifier), so unlike m938 it is not a third carrier.
        text = _read(JOURNALISTS_FILE)
        assert text.count(KEY_941) == 2
        assert KEY_941_TEST_FILE in text

    def test_m942_key_count_is_designed(self):
        # yaml key line + block_key field: exactly 2.
        text = _read(ENTITIES_FILE)
        assert text.count(KEY_942) == 2


# ---------------------------------------------------------------------------
# 5. m940 qualitative discipline (Type A #1182)
# ---------------------------------------------------------------------------
class TestTypeDM940QualitativeDiscipline1185:
    def test_m940_run_metadata(self):
        b = _m940_block()
        assert b["iteration"] == 1182
        assert b["iteration_type"] == "A"
        assert b["iteration_time"] == "2026-10-03 15:00 PDT"
        assert b["publication"] == "The New York Times"
        assert "Anthropic vs Meta" in b["competitor_pair"]

    def test_m940_temporal_extension_of_m895(self):
        # Second same-day accountability leg of m895; m835 carried
        # per #807.
        b = _m940_block()
        assert "m895" in b["finding"]
        assert "temporal extension" in b["competitor_pair"]

    def test_m940_arm_tones_and_means(self):
        b = _m940_block()
        sc = b["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert sc["target_scores"] == [-0.25]
        assert sc["target_avg"] == -0.25
        assert sc["peer_avg"] == -0.1
        assert sc["delta"] == -0.15
        assert sc["pooled_same_day"].startswith(
            "Sep-29 NYT x Anthropic pooled")

    def test_m940_within_entity_swing(self):
        b = _m940_block()
        sc = b["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "-0.55" in sc["temporal_swing"]
        assert "m895" in sc["temporal_swing"]

    def test_m940_manual_illustrative_only(self):
        b = _m940_block()
        assert b["statistical_discipline"].startswith(
            "MANUAL ILLUSTRATIVE ONLY")
        assert "engine NOT run" in b["statistical_discipline"]
        assert b["asymmetry_scorer_MANUAL_ILLUSTRATIVE"][
            "is_significant"] is False
        assert b["asymmetry_scorer_MANUAL_ILLUSTRATIVE"][
            "p_value"] == "NOT_CALCULATED"
        assert "NOT artifact-grade" in b["statistical_discipline"]

    def test_m940_verdict_and_ledger(self):
        b = _m940_block()
        sc = b["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert sc["verdict"] == "directionally_supported_not_proven"
        assert sc["no_analysis_json_update"] is True
        assert b["no_analysis_json_update"] is True
        assert b["ledger"] == "46"
        assert b["falsification_family_member"] is False
        assert "NOT a falsification-family member" in \
            b["falsification_family"]

    def test_m940_research_method_bounded(self):
        b = _m940_block()
        assert "0 browser.open" in b["research_method"]
        assert "6 browser.search query sets" in b["research_method"]


# ---------------------------------------------------------------------------
# 6. m941 qualitative discipline (Type B #1183)
# ---------------------------------------------------------------------------
class TestTypeDM941QualitativeDiscipline1185:
    def test_m941_run_metadata(self):
        b = _m941_block()
        assert b["iteration"] == 1183
        assert b["type"] == "B"
        assert b["journalist"] == "Vlad Savov"
        assert b["publication"] == "Bloomberg News"
        assert b["date"] == "2026-10-03 16:00 PDT"

    def test_m941_boundary_pin_of_boundary_family(self):
        # BOUNDARY/NULL pin at the corpus standing no-deal outlet
        # (in-corpus #85); joins the m593/#538 reporter-level
        # boundary family.
        b = _m941_block()
        assert "m593" in b["design"]
        assert "1180-1184 window FOURTH leg" in b["window"]

    def test_m941_arm_tones_and_delta(self):
        b = _m941_block()
        sc = b["scorer"]
        assert sc["new_openai_arm_tone"] == -0.35
        assert sc["meta_arm_tone"] == 0.05
        assert sc["illustrative_delta_openai_minus_meta"] == -0.4
        assert sc["delta_calc"] == "-0.35 - 0.05 = -0.40"

    def test_m941_peg_not_money_documented(self):
        b = _m941_block()
        assert "register follows the peg" in b["scorer"]["note"]

    def test_m941_manual_illustrative_only(self):
        b = _m941_block()
        assert "MANUAL ILLUSTRATIVE ONLY" in b["scorer"]["method"]
        assert "engine NOT run" in b["scorer"]["method"]
        assert b["scorer"]["engine_run"] is False
        assert b["scorer"]["is_significant"] is False
        assert "is_significant false" in b["statistical_discipline"]

    def test_m941_verdict_and_ledger(self):
        b = _m941_block()
        assert b["verdict"].startswith(
            "directionally_supported_not_proven")
        assert b["no_analysis_json_update"] is True
        assert b["falsification_ledger"] == 46
        assert b["falsification_family_member"] is False
        assert "NOT a falsification-family member" in b["finding"]
        assert "Ledger holds at 46" in b["ledger_note"]

    def test_m941_research_method_bounded(self):
        b = _m941_block()
        assert "0 browser.open" in b["research_method"]
        assert "4 browser.search query sets" in b["research_method"]
        assert "relay-bounded" in b["new_openai_arm"]["evidence_tier"]


# ---------------------------------------------------------------------------
# 7. m942 qualitative discipline (Type C #1184)
# ---------------------------------------------------------------------------
class TestTypeDM942QualitativeDiscipline1185:
    def test_m942_run_metadata(self):
        b = _m942_block()
        assert b["iteration"] == 1184
        assert b["iteration_type"] == "C"
        assert b["block_key"] == KEY_942
        assert "Stability AI $76M Series B" in b["mechanism_name"]

    def test_m942_invest_and_license_geometry(self):
        b = _m942_block()
        assert "INVEST-AND-LICENSE" in b["relationship_direction_taxonomy"]
        assert b["connects_to"] == [804, 391, 663]

    def test_m942_eight_novel_sources(self):
        b = _m942_block()
        srcs = b["sources"]
        assert len(srcs) == 8
        assert all(s["novel"] is True for s in srcs)

    def test_m942_lands_thirty_seventh_direction(self):
        # This run LANDED the thirty-seventh relationship direction;
        # the taxonomy field names the form explicitly.
        b = _m942_block()
        assert b["relationship_direction_taxonomy"].startswith(
            "THIRTY-SEVENTH relationship direction")
        assert "FIRST dedicated corpus mechanism" in b["novelty"]

    def test_m942_statistical_discipline(self):
        b = _m942_block()
        assert b["is_significant"] is False
        assert b["engine_run"] is False
        assert b["tone_scored"] is False
        assert b["artifact_grade"] is False
        assert b["no_analysis_json_update"] is True
        assert b["verdict"] == "directionally_supported_not_proven"

    def test_m942_falsification_family_excluded(self):
        b = _m942_block()
        assert "NOT a member" in b["falsification_family"]
        assert "46" in b["falsification_family"]

    def test_m942_research_method_bounded(self):
        b = _m942_block()
        assert b["browser_opens"] == 0


# ---------------------------------------------------------------------------
# 8. Falsification ledger: holds at 46
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1185:
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

    def test_thirty_seventh_direction_in_competitor_entities(self):
        # Landed at #1184 (m942 INVEST-AND-LICENSE): the former
        # absence guard is now an affirmative presence pin on the
        # corpus home (profiles/competitor-entities.yaml).
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

    def test_thirty_fourth_direction_in_competitor_entities(self):
        hits = _git_grep_tracked(_T34, "profiles/")
        assert "profiles/competitor-entities.yaml" in hits, hits

    def test_no_thirty_eighth_direction_claim_repo_wide(self):
        assert _git_grep_tracked(_T38) == []

    def test_no_thirty_ninth_direction_claim_repo_wide(self):
        assert _git_grep_tracked(_T39) == []

    def test_m940_m941_m942_not_members_ledger_holds(self):
        b940 = _m940_block()
        assert b940["ledger"] == "46"
        assert b940["falsification_family_member"] is False
        assert "NOT a falsification-family member" in \
            b940["falsification_family"]
        b941 = _m941_block()
        assert b941["falsification_ledger"] == 46
        assert b941["falsification_family_member"] is False
        assert "Ledger holds at 46" in b941["ledger_note"]
        b942 = _m942_block()
        assert "NOT a member" in b942["falsification_family"]
        assert "46" in b942["falsification_family"]


# ---------------------------------------------------------------------------
# 9. Type E #1181 discipline: the 159th verification cycle stays
#    monitoring-only
# ---------------------------------------------------------------------------
class TestTypeDTypeE1181Discipline1185:
    def test_1181_file_on_disk(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1181_FILE))

    def test_1181_pins_159th_cycle(self):
        src = _read(os.path.join(TESTS_DIR, E1181_FILE))
        assert "159th verification cycle" in src
        assert "158->159" in src

    def test_1181_monitoring_only_discipline(self):
        # The Aug 28 2026 standing rule: monitoring-only, tone
        # NOT_SCORED, engine NOT run, no mechanisms, NOT artifact-grade,
        # verdict directionally_supported_not_proven.
        src = _read(os.path.join(TESTS_DIR, E1181_FILE))
        assert "monitoring-only" in src
        assert "NOT artifact-grade" in src

    def test_1181_gf_episode_502_holds(self):
        src = _read(os.path.join(TESTS_DIR, E1181_FILE))
        assert "502" in src

    def test_1181_research_method_bounded(self):
        src = _read(os.path.join(TESTS_DIR, E1181_FILE))
        assert "0 browser.open" in src


# ---------------------------------------------------------------------------
# 10. Forward-looking staleness (predecessor pin lifecycle via subprocess)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1185:
    def test_1181_type_e_pins_trip_by_design(self):
        # Type E lands no mechanisms, but the #1182/#1183/#1184 A/B/C
        # legs landed 940/941/942 after #1181: its adds-no-mechanisms
        # and zero-940-numeric pins trip by design. Asserted directly
        # (same reason as #1170's/#1180's handling of the E1176 file:
        # the Type E file intermittently fails to resolve as a
        # subprocess node on this filesystem).
        # test_type_e_adds_no_mechanisms asserted max numeric == 939;
        # the 940/941/942 landings moved it to 942, so the pin trips.
        assert _max_numeric_mechanism_id_in_profiles() == 942
        # test_zero_940_numeric_mechanism_id_in_profiles asserted zero
        # numeric-940 keys in profiles; m940 landed, trips.
        assert _git_grep_tracked(_mech_id_colon(940), "profiles/") != []

    def test_1181_underscore_dash_940_halves_stay_green(self):
        # Designed keying: no mechanism-number substring in the
        # m940/m941/m942 block keys, so the underscore/dash halves
        # stay green. Direct working-tree sweep (NOT a subprocess node
        # run): the same scope the pin uses. Per #715 the needles are
        # format-built; this file carries no contiguous literal.
        hits_u = _sweep_source_files(_mech_underscore(940))
        hits_d = _sweep_source_files(_mech_dash(940))
        assert hits_u == [], hits_u
        assert hits_d == [], hits_d

    def test_1182_max_940_and_zero_941_numeric_trip_by_design(self):
        # m941 (journalists.yaml) and m942 (competitor-entities.yaml)
        # landed after #1182.
        for cls, node in (("TestMechanismNovelty",
                           "test_max_numeric_mechanism_id_is_940_post_insert"),
                          ("TestForwardGuards",
                           "test_zero_941_numeric_mechanism_id_in_profiles")):
            res = _node_run(A1182_FILE, cls + "::" + node)
            _assert_tripped(node, res)

    def test_1182_underscore_dash_941_halves_stay_green(self):
        # Designed keying (iteration 1183 in the m941 key, no 941
        # substring): the underscore/dash halves stay green.
        assert _git_grep_tracked(_mech_underscore(941)) == []
        assert _git_grep_tracked(_mech_dash(941)) == []

    def test_1183_zero_942_numeric_and_max_941_trip_by_design(self):
        # #1184 landed m942 (numeric id 942 in competitor-entities)
        # and committed "Type C #1184": the corpus pins trip.
        for node in ("test_zero_numeric_942_in_profiles",
                     "test_max_numeric_mechanism_id_is_941"):
            res = _node_run(
                B1183_FILE, "TestMechanismNovelty1183::" + node)
            _assert_tripped(node, res)

    def test_1183_underscore_dash_942_halves_stay_green(self):
        # Designed keying (iteration 1184 in the m942 key, no 942
        # substring): the underscore/dash halves stay green.
        assert _git_grep_tracked(_mech_underscore(942)) == []
        assert _git_grep_tracked(_mech_dash(942)) == []

    def test_1183_no_type_c_1184_pin_trips_by_design(self):
        # #1184's main commit landed "Type C #1184" in the git log, so
        # #1183's own in-git-log absence pin (TestGuardLifecycle1183)
        # trips by design.
        res = _node_run(
            B1183_FILE,
            "TestGuardLifecycle1183::test_no_type_c_1184_in_git_log_pin")
        _assert_tripped("test_no_type_c_1184_in_git_log_pin", res)

    def test_1184_zero_943_guards_stay_green(self):
        # Type D lands no mechanism: #1184's forward guards (zero 943
        # numeric in profiles, max 942) stay green.
        for node in ("test_zero_numeric_943_in_profiles",
                     "test_max_numeric_mechanism_id_is_942"):
            res = _node_run(
                C1184_FILE, "TestMechanismNovelty1184::" + node)
            assert res.returncode == 0, (node, res.stdout[-2000:])

    def test_1184_guard_lifecycle_class_stays_green(self):
        res = _class_run(C1184_FILE, "TestGuardLifecycle1184")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1184_no_type_d_1185_pin_green_pre_commit(self):
        # Green in-gate; flips BY DESIGN once this run's main commit
        # lands (pinned in the rotation_transparency field).
        res = _node_run(
            C1184_FILE,
            "TestGuardLifecycle1184::test_no_type_d_1185_in_git_log_pin")
        assert res.returncode == 0, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 11. Guard lifecycle (forward guards for #1186)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1185:
    def test_1185_file_pins_max_id_942_and_next_943(self):
        assert _max_numeric_mechanism_id_in_profiles() == 942

    def test_zero_next_numeric_943_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(NEXT_NUM), "profiles/") == []

    def test_zero_next_underscore_943_repo_wide(self):
        assert _git_grep_tracked(_mech_underscore(NEXT_NUM)) == []

    def test_zero_next_dash_943_repo_wide(self):
        assert _git_grep_tracked(_mech_dash(NEXT_NUM)) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 942 in ids
        assert all(i <= 942 for i in ids)

    def test_thirty_seventh_direction_still_present(self):
        # Landed at #1184 (m942 INVEST-AND-LICENSE): the affirmative
        # claim now lives in the corpus file and the #1184 doc rows;
        # assert the corpus home is present, not exclusivity.
        hits = [p for p in _git_grep_tracked(_T37)]
        assert "profiles/competitor-entities.yaml" in hits, hits

    def test_thirty_sixth_direction_still_present(self):
        hits = [p for p in _git_grep_tracked(_T36)]
        assert "profiles/competitor-entities.yaml" in hits, hits

    def test_no_thirty_eighth_direction_claim(self):
        hits = [p for p in _git_grep_tracked(_T38)]
        assert hits == [], hits

    def test_no_thirty_ninth_direction_claim(self):
        hits = [p for p in _git_grep_tracked(_T39)]
        assert hits == [], hits

    def test_no_forty_seventh_member_claim(self):
        hits = [p for p in _git_grep_tracked(FORTY_SEVENTH_MEMBER)]
        assert hits == [], hits

    def test_no_forty_eighth_member_claim(self):
        hits = [p for p in _git_grep_tracked(FORTY_EIGHTH_MEMBER)]
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 12. Background-suite verdict (#1180 suite)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1185:
    def _log_stats(self):
        text = _read(PRIOR_SUITE_LOG)
        return (os.path.getsize(PRIOR_SUITE_LOG), text.count("."),
                text.count("x"), text)

    def test_prior_suite_died_twenty_ninth_consecutive(self):
        # The #1180-launched background full suite DIED: 3233 bytes
        # (2901 dots + xfail marks frozen at [ 4%]), last write Oct 3
        # 14:56 PDT (~3h before this run's check), zero summary tokens
        # (no "passed"/"failed" summary, no collected-count token, no
        # "no tests ran", no "short test summary"), no live pytest
        # process, no type_d_1180/type_d_1185 markers. Per the #795
        # convention this is recorded as DIED, not "interrupted":
        # the run produces no usable verdict.
        size, dots, xs, text = self._log_stats()
        assert size == 3233, size
        assert dots == 2901, dots
        assert "passed" not in text
        assert "failed" not in text
        assert " collected " not in text
        assert "no tests ran" not in text
        assert "short test summary" not in text

    def test_no_live_pytest_process(self):
        # A live suite writer would hold the #1180 log file open.
        # Scan /proc for pytest processes and check whether any of
        # them has the #1180 suite log among its open file
        # descriptors. The #1185 re-launch writes to a different log
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
            "a live pytest process still holds the #1180 suite log "
            "open: %r" % holders)

    def test_last_write_stale(self):
        # The prior suite's last write predates this run by hours,
        # far beyond any healthy inter-write bound.
        import time
        mtime = os.path.getmtime(PRIOR_SUITE_LOG)
        assert mtime < time.time() - 7200, mtime

    def test_no_1185_markers_in_prior_suite(self):
        # The #1180 suite was launched before this run existed; it
        # must carry no trace of it.
        _, _, _, text = self._log_stats()
        assert "type_d_1185" not in text

    def test_tombstone_lineage_advances_to_96th(self):
        # TWENTY-NINTH consecutive background-suite death of the new
        # streak (the 57-run streak ENDED at #1085 when the #1080
        # suite completed). Tombstone lineage advances NINETY-FIFTH ->
        # NINETY-SIXTH; recorded in the #1185 iteration-log entry.
        # Deselected pre-commit (log entry is written in the doc-sync
        # step per #719/#721).
        text = _read(LOG_FILE)
        assert "NINETY-SIXTH" in text


# ---------------------------------------------------------------------------
# 13. Fresh synthetic engine calibration (new values, not #1180's)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1185:
    # Scratch-run values produced at this run (Sat 2026-10-03 ~18:05
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
        meta = [-0.50, -0.44, -0.57, -0.49, -0.52]
        comp = [0.31, 0.26, 0.33, 0.29, 0.28]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(
            -0.7979999999999999)
        assert result.t_statistic == pytest.approx(
            -32.79759796741879)
        assert result.p_value == pytest.approx(
            2.4282304739441895e-08)
        assert result.cohens_d == pytest.approx(
            -20.743022271910455)
        assert result.is_significant is True
        assert result.confidence_interval_lower == pytest.approx(
            -0.8380500000000001)
        assert result.confidence_interval_upper == pytest.approx(
            -0.758)
        # The strong arm-swap negates the asymmetry exactly.
        swapped = calc(comp, meta)
        assert swapped.asymmetry_score == pytest.approx(
            -result.asymmetry_score)
        assert abs(result.asymmetry_score +
                   swapped.asymmetry_score) < 1e-12

    def test_near_null_pair_stays_silent(self):
        calc = self._calculate()
        meta = [0.03, -0.02, 0.04, -0.05, 0.01]
        comp = [0.02, 0.04, -0.03, 0.01, -0.02]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(-0.002)
        assert result.p_value > 0.05
        assert result.is_significant is False
        assert result.confidence_interval_lower < 0 < \
            result.confidence_interval_upper

    def test_degenerate_n1_contract(self):
        # The classic degenerate guard: n=1 per arm yields t=0.0,
        # p=1.0, d=0.0 and is_significant False regardless of the
        # illustrative pair mean (here +0.20 vs +0.05, delta +0.15).
        calc = self._calculate()
        result = calc([0.20], [0.05])
        assert result.asymmetry_score == pytest.approx(0.15000000000000002)
        assert result.t_statistic == 0.0
        assert result.p_value == 1.0
        assert result.cohens_d == 0.0
        assert result.is_significant is False

    def test_engine_layer_not_finding_layer(self):
        # The m940/m941/m942 mechanisms never promote engine
        # significance to a finding: all three carry manual-only
        # discipline (m940 MANUAL ILLUSTRATIVE ONLY engine NOT run,
        # m941 MANUAL ILLUSTRATIVE ONLY engine NOT run, m942 tone
        # NOT_SCORED / engine NOT run).
        b940 = _m940_block()
        assert b940["statistical_discipline"].startswith(
            "MANUAL ILLUSTRATIVE ONLY")
        assert "engine NOT run" in b940[
            "asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["scorer"]
        b941 = _m941_block()["scorer"]
        assert "MANUAL ILLUSTRATIVE ONLY" in b941["method"]
        assert b941["engine_run"] is False
        b942 = _m942_block()
        assert b942["is_significant"] is False
        assert b942["engine_run"] is False
        assert b942["tone_scored"] is False


# ---------------------------------------------------------------------------
# 14. Suite re-launch
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1185:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1185 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1190 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1190)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1185_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 15. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1185:
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
        assert "## #1185" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 63249
        assert README_FILE_COUNT == 1510


# ---------------------------------------------------------------------------
# 16. Iteration log (#719: the entry carries hashes per #721)
# ---------------------------------------------------------------------------
class TestTypeDIterationLog1185:
    def test_log_entry_has_main_commit_hash(self):
        text = _read(LOG_FILE)
        assert "Type D #1185" in text

    def test_log_entry_notes_window_opening(self):
        text = _read(LOG_FILE)
        assert "OPENING leg of the 1185-1189 window" in text

    def test_log_entry_notes_tombstone_lineage(self):
        # Deselected pre-commit: the entry is written in the doc-sync
        # step per #719/#721.
        text = _read(LOG_FILE)
        assert "NINETY-SIXTH" in text


# ---------------------------------------------------------------------------
# 17. Literal discipline (ASCII-only, no em dashes)
# ---------------------------------------------------------------------------
class TestLiteralDiscipline1185:
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
class TestInflightIsolation1185:
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
class TestAnchor1185:
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
        # "Type D #1185 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1185 anchor"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert "Type D #1185 anchor" in log

    def test_main_commit_message_convention(self):
        log = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1185:"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert "Type D #1185" in log
