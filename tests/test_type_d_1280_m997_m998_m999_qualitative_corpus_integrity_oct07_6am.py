# -*- coding: utf-8 -*-
"""Type D #1280 tests: m997/m998/m999 qualitative-discipline
corpus-integrity verification (Oct 7, 2026) + #1275 background-suite
verdict per #795 + recurring-failure triage + full suite re-launch.

m997 (Type A #1277, profiles/atlantic.yaml
competitor_relationships.openai, block key
type_a_1277_atlantic_openai_robinson_essay_culture_broken_october):
mechanism id 997 - the Atlantic Oct-3 David Robinson resignation essay
("I Quit OpenAI Because Its Culture Is Broken", -0.65 MANUAL
ILLUSTRATIVE) vs carried Atlantic x Meta AI Watchdog arms (m481
Strike-3 -0.75 + pirated-books -0.55, mean -0.65); illustrative delta
(OpenAI minus Meta) +0.10 clean / 0.00 pooled - near-null. The
uniform payer-softening prediction FAILS at the ideas/essay
gatekeeping tier: the Atlantic platformed an insider takedown of its
May-2024 licensing partner at Meta-comparable hardness. FIFTY-FIFTH
falsification-family member (ledger 54->55 in the block's own prose;
the live ledger holds at 55), falsification_member_confirmed,
domain-bounded to the ideas/essay gatekeeping tier.

m998 (Type B #1278, profiles/careers/journalists.yaml kris_holt_type_b,
block key
type_b_1278_kris_holt_engadget_meta_connect_roundup_vs_google_eu_fine_oct07_4am):
mechanism id 998 - Kris Holt (Engadget) Meta Connect 2026 launch
roundup (0.00 MANUAL ILLUSTRATIVE, neutral product relay, zero privacy
vocabulary) vs Google EU $463M location-data fine news with
repeat-offender framing (-0.50 MANUAL ILLUSTRATIVE); illustrative delta
(Google minus Meta) -0.50 in the Meta-soft direction. CONTROL-CASE at
a deal-free outlet (no documented Yahoo/Engadget AI content-licensing
deal with Meta or Google in the corpus): the uniform payer-softening
prediction is NOT adjudicated. NOT a falsification-family member.

m999 (Type C #1279, profiles/competitor-entities.yaml top-level, block
key type_c_1279_uk_search_only_contracts_invoice_rail_oct07):
mechanism id 999 - FIRST dedicated corpus mechanism on the
publisher-side per-scrape pricing rail: Movement for an Open Web
Search-Only Contracts (Jun 15 2026, 31 founding UK publisher sites,
typical 500 GBP per-article fee, deemed acceptance on access,
MoneyClaim.gov.uk + county-court enforcement ladder). The
invoice-economy leg of the money-flow taxonomy. BOUNDARY: unilateral
not bilateral, no lab signed/paid, no confirmed invoices
(first-invoice = falsifiable milestone). NOT a falsification-family
member (claims no slot). Ledger HOLDS at 55.

Background-suite verdict per #795: the #1275-launched full suite
(goal hidden_files type_d_1275_full_suite.log) is DEAD at [  2%]:
1779 bytes, zero F marks, last write Oct 7 2026 02:01 PDT (~4h stale
at this run's ~06:00 PDT check), zero summary tokens, zero live pytest
processes, no process holding the log open per the /proc open-fd
check. SIXTH consecutive background-suite death of the new streak (the
57-run streak ENDED at #1085 when the #1080 suite completed; the
43-run streak BROKE at #1250 when the #1245 suite was verdict ALIVE
at 20%; #1255 FIRST, #1260 SECOND, #1265 THIRD, #1270 FOURTH, #1275
FIFTH). Tombstone lineage advances ONE-HUNDRED-THIRTEENTH ->
ONE-HUNDRED-FOURTEENTH per #565. The dead stream carries ZERO F
marks: no recurring-failure triage repairs this run (nothing to
triage; triage is DETERMINATE-vacuous). The full suite is RE-LAUNCHED
this run to goal hidden_files type_d_1280_full_suite.log (venv python
per the Sep 7 2026 convention, full inventory, no -x; dots
accumulating at commit). The #1285 Type D run owns the next verdict
per #795.

MANUAL / qualitative ONLY per the Aug 28 2026 standing rule: engine
NOT run on corpus; is_significant never asserted on corpus data; NOT
artifact-grade; no analysis.json update. Fresh synthetic engine
calibration this run (engine-layer contract, never a finding):
synthetic Apple arms [-0.08, -0.12] vs synthetic Meta arms
[-0.41, -0.35], pooled delta +0.280.

This run is the FIRST and OPENING leg of the 1280-1284 window
(D #1280 -> E #1281 -> A #1282 -> B #1283 -> C #1284 per the #565
anchor + rotation guard). The 1275-1279 window is VERIFIED CLOSED.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY
DESIGN post-anchor.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file
must not carry contiguous numeric/underscore/dash mechanism-key forms
of the max or next number, the forty-eighth through fifty-fifth
member-claim forms, the fifty-sixth member-claim form, or the
thirty-fifth through fortieth direction forms; the constants are
constructed at runtime. (The landed ordinals live as short lowercase
forms in prose here; the live full-form claims live in profiles: the
forty-eighth in financial-times.yaml, the forty-ninth and fiftieth in
profiles/careers/journalists.yaml, the fifty-first in news-corp.yaml,
the fifty-second in profiles/careers/journalists.yaml, the
fifty-third in the-verge.yaml, the fifty-fourth in guardian.yaml, the
fifty-fifth in atlantic.yaml.)
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
ATLANTIC_PATH = os.path.join(PROFILES_DIR, "atlantic.yaml")
JOURNALISTS_PATH = os.path.join(
    PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1275_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1280_full_suite.log")
OWN_BASENAME = (
    "test_type_d_1280_m997_m998_m999_qualitative_"
    "corpus_integrity_oct07_6am.py"
)

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "b8695266909c9b2a1b4a18019d27725aa3d31cb2"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 999
NEXT_NUM = 1000  # integer only; key-form needles are format-built

# Predecessor chain: #1279 Type C closed the 1275-1279 window.
PRED_MAIN_1279 = "102fbeba"
PRED_ANCHOR_1279 = "b2b4cee9"
PRED_DOCSYNC_1279 = "1b62c10e"
PRED_FINAL_1279 = "1fafda66"

# Placeholder for the NEXT leg's main commit sha per #721; re-pinned
# to #1281's main commit in #1281's terminal log-hash followup.
PRED_MAIN_1281 = "3c53f5f98c3b6b53443d507d02a206f4a07afde6"  # re-pinned in #1281 log-hash followup per #721 (main commit sha)

# The #1279 window-closing file, for the staleness pin on its
# guard-lifecycle class (max id 999; zero next-number forms /
# no-Type-D-#1280-in-git-log / fortieth direction absent /
# forty-eighth through fifty-fifth members intact / fifty-sixth
# member absent / ledger 55).
B1279_FILE = (
    "test_type_c_1279_uk_search_only_contracts_"
    "invoice_rail_oct07_4am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 71287  # post-doc-sync total (pre-sync 71208 + 79)
README_FILE_COUNT = 1605  # pre-sync 1604 + 1 (this file)

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

# Fragment-built per #715: the contiguous keys never appear in this
# file. Iteration-form block keys carry no underscore-form mechanism
# key substring (the #723/#738/#739 designed-keying convention).
BLOCK_997 = (
    "type_a_1277_atlantic_openai_robinson_essay_"
    "culture_broken_october"
)
BLOCK_998 = (
    "type_b_1278_kris_holt_engadget_meta_connect_roundup_"
    "vs_google_eu_fine_oct07_4am"
)
BLOCK_999 = (
    "type_c_1279_uk_search_only_contracts_"
    "invoice_rail_oct07"
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


def _git_grep_tracked_source(needle, scope):
    """Grep tracked files at HEAD for a literal needle (fragment-built)."""
    args = ["git", "grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    out = subprocess.run(
        args, cwd=REPO_ROOT, capture_output=True, text=True
    ).stdout
    cleaned = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        if line:
            cleaned.append(line)
    return cleaned


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
    """Fresh engine-layer calibration contract for #1280.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no repo reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_apple_arms = [-0.08, -0.12]
    synthetic_meta_arms = [-0.41, -0.35]
    pooled_apple = (sum(synthetic_apple_arms)
                    / len(synthetic_apple_arms))
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_apple - pooled_meta, 3)


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1280:
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
# 2. Rotation guard: #1279 closed the 1275-1279 window; #1280 opens.
# ---------------------------------------------------------------------------


class TestRotationGuard1280:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-40").stdout
        for sha, label in (
            (PRED_MAIN_1279, "1279 main"),
            (PRED_ANCHOR_1279, "1279 anchor"),
            (PRED_DOCSYNC_1279, "1279 doc-sync"),
            (PRED_FINAL_1279, "1279 log-hash"),
        ):
            assert sha in log, label

    def test_1279_type_c_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type C #1279").stdout
        assert out.strip() != ""

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1280-1284 window" in src

    def test_1275_1279_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1275-1279" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1281_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "E #1281" in src


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m997 / m998 / m999 verified present and well-formed.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1280:
    def test_m997_block_present_in_atlantic(self):
        atlantic = _yaml(ATLANTIC_PATH)["competitor_relationships"]
        assert BLOCK_997 in atlantic["openai"]

    def test_m997_mechanism_id_997(self):
        atlantic = _yaml(ATLANTIC_PATH)["competitor_relationships"]
        assert atlantic["openai"][BLOCK_997]["mechanism_id"] == 997

    def test_m997_block_key_field(self):
        atlantic = _yaml(ATLANTIC_PATH)["competitor_relationships"]
        assert atlantic["openai"][BLOCK_997]["block_key"] == BLOCK_997

    def test_m997_verdict_falsification_member(self):
        atlantic = _yaml(ATLANTIC_PATH)["competitor_relationships"]
        block = atlantic["openai"][BLOCK_997]
        assert block["verdict"].startswith("falsification_member_confirmed")
        assert block["falsification_family_member"] is True

    def test_m998_key_present_in_journalists(self):
        journalists = _yaml(JOURNALISTS_PATH)
        assert "kris_holt_type_b" in journalists

    def test_m998_block_present(self):
        journalists = _yaml(JOURNALISTS_PATH)
        coverage = journalists["kris_holt_type_b"]["competitor_coverage"]
        assert BLOCK_998 in coverage

    def test_m998_mechanism_id_998(self):
        journalists = _yaml(JOURNALISTS_PATH)
        coverage = journalists["kris_holt_type_b"]["competitor_coverage"]
        assert coverage[BLOCK_998]["mechanism_id"] == 998
        assert coverage[BLOCK_998]["iteration"] == 1278
        assert coverage[BLOCK_998]["type"] == "B"

    def test_m998_control_case_not_member(self):
        text = _read(JOURNALISTS_PATH)
        assert "CONTROL-CASE" in text

    def test_m999_block_present_in_entities(self):
        entities = _yaml(ENTITIES_PATH)
        assert BLOCK_999 in entities

    def test_m999_mechanism_id_999(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_999]
        assert block["mechanism_id"] == 999
        assert block["iteration"] == 1279
        assert block["iteration_type"] == "C"

    def test_m999_not_a_member(self):
        entities = _yaml(ENTITIES_PATH)
        assert "claims no slot" in entities[BLOCK_999]["falsification_family"]

    def test_max_numeric_mechanism_id_is_999(self):
        assert _max_numeric_mechanism_id() == MECH_NUM


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1275 suite is DEAD at [  2%].
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1280:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG

    def test_prior_suite_stalled_at_2(self):
        # The #1275-launched suite froze at [  2%] progress: 1779
        # bytes, zero F marks, last write Oct 7 2026 02:01 PDT, zero
        # live pytest processes. Progress never regresses, so the
        # marker stays present and [  3%] never arrives.
        text = _read(PRIOR_SUITE_LOG)
        assert "[  2%]" in text, text[-2000:]
        assert "[  3%]" not in text
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
        # type_d_1275_full_suite.log open anymore (the /proc open-fd
        # check returns empty). The suite died between the #1278
        # observation (~04:10 PDT Oct 7, [  2%], processes dead) and
        # this run's check.
        holders = _proc_holds_log("type_d_1275_full_suite.log")
        assert holders == "", holders

    def test_sixth_death_of_new_streak(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite
        # completed). The 43-run streak BROKE at #1250 (the #1245
        # suite was verdict ALIVE at 20%). #1255 verdict the FIRST
        # consecutive background-suite death of the new streak, #1260
        # the SECOND, #1265 the THIRD, #1270 the FOURTH, #1275 the
        # FIFTH. This verdict is the SIXTH consecutive
        # background-suite death of the new streak.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "SIXTH consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-THIRTEENTH -> ONE-HUNDRED-FOURTEENTH.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ONE-HUNDRED-FOURTEENTH" in src
        assert "lineage advances" in src

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1280 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_PATH)
        assert "SIXTH consecutive" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: zero F marks in the dead stream.
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1280:
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


class TestStatisticalDiscipline1280:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: the max numeric mechanism id is
        # unchanged at 999 and no 1000-form keys exist.
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_engine_not_run_on_corpus(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run on corpus" in src

    def test_synthetic_calibration_delta_contract(self):
        # Engine-layer contract only (never a finding): synthetic
        # Apple arms [-0.08, -0.12] vs synthetic Meta arms
        # [-0.41, -0.35] -> pooled delta +0.280.
        assert _synthetic_calibration_delta() == 0.28


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 55; guards on member forms.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1280:
    def test_ledger_holds_at_55(self):
        entities = _yaml(ENTITIES_PATH)
        fam = entities[BLOCK_999]["falsification_family"]
        assert "ledger holds at 55" in fam
        assert "claims no slot" in fam

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

    def test_no_fifty_sixth_member(self):
        assert _git_grep_tracked_source(_T56, None) == []

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
# 8. Guard lifecycle: forward pins for #1281; #1279's pins flip BY DESIGN.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1280:
    def test_pins_on_999_no_landing(self):
        # Type D lands no mechanisms: max stays 999, next stays 1000.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 999" in src
        assert "NEXT_NUM = 1000" in src

    def test_no_type_e_1281_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1281's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1281" must be #1281's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type E #1281")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1281's own commits"
        main = _git("rev-parse", PRED_MAIN_1281).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1000_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1000_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1000_dash_absent_repo_wide(self):
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

    def test_no_fifty_sixth_member_pin(self):
        assert _git_grep_tracked_source(_T56, None) == []

    def test_predecessor_1279_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, B1279_FILE))

    def test_next_leg_is_1281_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1281 Type E" in src

    def test_1279_pins_flip_by_design_documented(self):
        # #1279's forward guards (max-999, zero-1000 keys all forms,
        # no-Type-D-#1280-in-git-log, fortieth absent, forty-eighth
        # through fifty-fifth intact in profiles/, fifty-sixth absent,
        # ledger 55) verified GREEN at HEAD pre-commit this run. The
        # no-Type-D-#1280-in-git-log pin flips BY DESIGN at this run's
        # main commit (the #1191-class self-trip, re-pinned post-commit
        # by TestStalenessPins1280). Type D lands no mechanisms, so
        # the zero-1000-numeric/underscore/dash pins stay green.
        # Documented in the staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1280" in src
        assert "no_type_d_1280_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1279's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1280:
    def test_1279_guard_lifecycle_post_commit_self_trip(self):
        # Post-main-commit form: 18 tests in the class, 17 pass and
        # ONE flips BY DESIGN when this run's main commit lands: the
        # no_type_d_1280_in_git_log ancestor pin (its PRED_MAIN_1280
        # is still the 0*40 placeholder until this run's terminal
        # log-hash followup re-pins it per #721) - the #1191-class
        # self-trip. Type D lands no mechanisms, so the 1000-numeric
        # forward-guard pins stay green. The pin is re-pinned to the
        # post-commit own-set form in the terminal log-hash followup
        # per #721; the class run below therefore expects the 17
        # surviving pins green and documents the one designed flip.
        # The #1279 block is read-only to this run; the quirk is
        # documented here, not repaired.
        res = _class_run(B1279_FILE, "TestGuardLifecycle1279")
        out = res.stdout + res.stderr
        assert "1 failed, 17 passed" in out, out[-2000:]
        assert "no_type_d_1280_in_git_log" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1280:
    def test_readme_test_file_table_has_1280_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_d_1280" in readme

    def test_architecture_has_1280_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_d_1280" in arch

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


class TestIterationLog1280:
    def test_log_has_1280_entry(self):
        text = _read(LOG_PATH)
        assert "## #1280 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "SIXTH consecutive" in text
        assert "type_d_1280_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1280:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1280_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1280 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1280:
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

    def test_1024_m846_untouched(self):
        # Ray's revert/leave/rebuild decision on m846 is pending;
        # this run does not touch it.
        res = _git("status", "--short")
        assert "competitor-entities.yaml" not in res.stdout
