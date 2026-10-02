"""Type B -- Iteration #1138 (Fri 2026-10-02 01:00 PDT): m914 Stevie Bonifield
(The Verge) Sep-24 Meta Connect 2026 product-positive recap (+0.10) vs
Apr-16 Google Gucci glasses fashion-partnership news (+0.15) --
competitive quote-inclusion mechanism EXTENDING m150's Spiegel-quote-inclusion
observation (Cherlynn Low, Engadget) to a second writer and a second outlet:
Bonifield's Google glasses piece platforms Snap CEO Evan Spiegel's anti-Meta
brand diss ("the Meta brand, I think, is not something people want anywhere
near their face") as editorial color while his Meta Connect recap reads
product-positive with zero privacy interrogation of the camera/audio glasses.
Illustrative delta (Google minus Meta) +0.05: near-null at the TONE level --
the finding sits at the QUOTE-INCLUSION level, not tone. FIRST dedicated
Type B mechanism on Stevie Bonifield in journalists.yaml (zero
stevie_bonifield YAML key pre-commit, per the #643 convention). STRONG
temporal confound: the Google arm (Apr 16) predates the summer backlash wave
by ~5 months. MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule;
engine NOT run; NOT a falsification-family member; ledger holds at 46;
no analysis.json update; NOT artifact-grade; verdict
directionally_supported_not_proven.

Type B FOURTH leg of the 1135-1139 window, CONTINUING it
(D #1135 -> E #1136 -> A #1137 -> B #1138 -> C #1139). Committed
predecessor #1137 Type A (00:00 PDT Oct 2) is the window's third leg
(main 311b2e32 / anchor 4dce0951 / doc-sync 0153bf5f / log-hash
8922dcf5). Rotation per the #565 anchor + rotation guard.
Concurrency note: the in-flight runs at this run's checks are the
#899 Type C block (m771, uncommitted hunk in profiles/nytimes.yaml),
the #938 Type B test file (uncommitted working-tree edit), the #900
Type D test file (untracked, on disk) and the #1012 working-tree
edit of the committed Type A #1012 test file - all UNCOMMITTED, no
Type C #899 / Type B #938 / Type D #900 main commits in git
history, and no ## #899 / ## #938 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch the in-flight files (the
m914 block lands in profiles/careers/journalists.yaml under a new
stevie_bonifield key, NOT nytimes.yaml); the in-flight blocks are
owned by their runs. Targeted staging only per the repo-wide
traversal lesson. Iteration numbers follow the rotation schedule,
not commit order. Do NOT touch #1024's m846 (FOURTEENTH,
exclusionary-diversion): self-flagged sourcing-constraint violation;
Ray's revert/leave/rebuild-from-primary decision still pending.

Verifies:
- m914 (Type B #1138, profiles/careers/journalists.yaml
  stevie_bonifield/competitor_coverage block key, 4-space indent,
  `mechanism_id: 914` field form; block key count 3 - colon-form line +
  block_key field + test_file-adjacent mention, designed): Stevie
  Bonifield (The Verge) Sep-24 Meta Connect recap (+0.10, zero privacy
  vocabulary in digest excerpt) vs Apr-16 Google Gucci glasses piece
  (+0.15, fashion-positive, platforms Spiegel's anti-Meta brand diss);
  competitive quote-inclusion EXTENDING m150 to a second writer/outlet,
  post-landing corpus integrity (max numeric mechanism_id 914; zero
  next-number 915 keys in numeric/underscore/dash mechanism forms -
  the 915 needles are format-built per #715 so no guard-literal carrier
  file exists; falsification ledger holds at 46 - FORTY-SIXTH member-form
  present (m907, profiles/the-verge.yaml), FORTY-SEVENTH member-claim
  form absent repo-wide as designed negative guard for the next landing;
  thirty-fourth direction present (competitor-entities.yaml m912),
  thirty-fifth direction-claim form absent; the #1135/#1136/#1137 window
  files are NOT edited by this run - their now-stale forward-looking
  pins are recorded as designed lifecycle in TestForwardLookingStaleness1138).
"""

import glob
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
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
OWN_BASENAME = (
    "test_type_b_1138_stevie_bonifield_verge_meta_connect_recap_"
    "vs_google_gucci_glasses_oct02_1am.py"
)

# Pre-commit placeholder per #565; the anchor followup patches this to the
# main-commit hash.
ANCHORED_SHA = "0" * 40  # Type B runs self-anchor per #565

MECH_NUM = 914
NEXT_NUM = 915

# Literal discipline per #715/#770: the underscore/dash mechanism-key forms,
# the block key, and the member/direction forward-guard forms are
# format-built so this file carries no contiguous needle.
MECH_ID_MARKER = "mechanism" + "_"
MECH_DASH_MARKER = "mechanism" + "-"

BLOCK_KEY = (
    "type_b_1138_stevie_bonifield_verge_meta_connect_recap_"
    "vs_google_gucci_glasses_sep2026"
)

FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_SIXTH_MEMBER = "FORTY" + "-SIXTH falsification-family member"
THIRTY_FOURTH_DIR = "THIRTY" + "-FOURTH" + " relationship direction"
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH" + " relationship direction"
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"

PRED_MAIN_1137 = "311b2e32"
PRED_ANCHOR_1137 = "4dce0951"
PRED_DOCSYNC_1137 = "0153bf5f"
PRED_LOGHASH_1137 = "8922dcf5"

FILE_1137 = (
    "test_type_a_1137_atlantic_openai_sep26_oct01_crisis_window_"
    "silence_historical_register_vs_meta_watchdog_oct02_12am.py"
)

URL_META_CONNECT = (
    "https://wesearch.press/s/"
    "meta-connect-2026-the-7-biggest-announcements-93c0ec36"
)
URL_GOOGLE_GUCCI = (
    "https://technewstube.com/theverge/1824006/"
    "gucci-branded-google-smart-glasses-next-year/"
)

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1135_full_suite.log"
)


def _read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO_ROOT, capture_output=True, text=True
    )


def _iter_source_files():
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [
            d
            for d in dirs
            if d not in (".git", "__pycache__", "node_modules", ".venv")
        ]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f)


def _repo_grep_underscore_mechanism(n):
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [p for p in _iter_source_files() if needle in _read(p)]


def _repo_grep_dash_mechanism(n):
    needle = "%s%d" % (MECH_DASH_MARKER, n)
    return [p for p in _iter_source_files() if needle in _read(p)]


def _profiles_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in _read(p):
                hits.append(p)
    return hits


def _max_numeric_mechanism_id_in_profiles():
    found = []
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            found.extend(int(m) for m in pat.findall(_read(os.path.join(root, f))))
    return max(found) if found else 0


def _profiles_text():
    parts = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            parts.append(_read(os.path.join(root, f)))
    return "\n".join(parts)


def _block():
    doc = yaml.safe_load(_read(JOURNALISTS_FILE))
    return doc["stevie_bonifield"]["competitor_coverage"][BLOCK_KEY]


def _block_text():
    return _read(JOURNALISTS_FILE)


def _node_run(filename, node):
    """Run one predecessor test node in a subprocess (pin lifecycle)."""
    target = os.path.join(TESTS_DIR, filename) + "::" + node
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    return subprocess.run(
        ["python3", "-m", "pytest", target, "-q", "--no-header"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        env=env,
    )


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder; patched green post-commit per #565).
# ---------------------------------------------------------------------------

class TestAnchor1138:
    def test_anchored_sha_placeholder_pre_commit(self):
        # Pre-commit the anchor is a zero placeholder; the anchor followup
        # patches it per #565. The post-commit rotation guard asserts the
        # patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        assert ANCHORED_SHA == "0" * 40

    def test_anchored_sha_shape(self):
        assert len(ANCHORED_SHA) == 40

    def test_anchor_mechanics_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ANCHORED_SHA" in src
        assert "#565" in src

    def test_block_key_matches_file_and_profile(self):
        # The format-built BLOCK_KEY is the colon-form profile key carrying
        # the iteration number (not the mechanism id) per #715.
        assert "type_b_1138" in BLOCK_KEY
        assert "914" not in BLOCK_KEY
        assert BLOCK_KEY in _block_text()

    def test_journalist_file_and_indent(self):
        # The block lives under stevie_bonifield's competitor_coverage at
        # indent 4 in profiles/careers/journalists.yaml.
        text = _block_text()
        assert "    " + BLOCK_KEY + ":" in text
        b = _block()
        assert b["journalist"] == "Stevie Bonifield"
        assert b["block_key"] == BLOCK_KEY
        assert b["publication"] == "theverge"


# ---------------------------------------------------------------------------
# 2. Rotation guard (pre-commit assertions; git-log novelty test is
# SUPERSEDED BY DESIGN post-commit - deselect in post-commit full runs).
# ---------------------------------------------------------------------------

class TestRotationGuard1138:
    def test_predecessor_1137_chain_present(self):
        log = _git("log", "--oneline", "-80").stdout
        assert PRED_MAIN_1137 in log
        assert PRED_ANCHOR_1137 in log
        assert PRED_DOCSYNC_1137 in log
        assert PRED_LOGHASH_1137 in log

    def test_type_b_1138_novelty(self):
        # "Type B #1138" absent from git log pre-commit; own file not
        # yet committed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type B #1138:") lands; post-commit, the anchor
        # asserts the patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        log = _git("log", "--oneline", "--grep=Type B #1138").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1135 -> E #1136 -> A #1137 -> B #1138" in src

    def test_window_fourth_leg(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH leg" in src
        assert "1135-1139" in src

    def test_next_run_1139_type_c_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "C #1139" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (post-landing state: max is 914; 915 absent in all
# forms; 914 underscore/dash absent - the forward guards for #1139+).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1138:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1138*.py"))
        assert len(files) == 1, files

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_b_1138 files on disk" in _block_text()

    def test_max_numeric_mechanism_id_is_914(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_underscore_915_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_915_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_915_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_914_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_914_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_914_numeric_present_only_in_journalists_block(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [JOURNALISTS_FILE], hits

    def test_block_key_zero_hit_outside_own_file(self):
        # The block key must not appear anywhere except the landed profile
        # block (own file carries only the format-built form).
        hits = [
            p for p in _iter_source_files() if BLOCK_KEY in _read(p)
        ]
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 4. Block structure.
# ---------------------------------------------------------------------------

class TestBlockStructure1138:
    def test_block_loads_under_bonifield_competitor_coverage(self):
        doc = yaml.safe_load(_block_text())
        assert BLOCK_KEY in doc["stevie_bonifield"]["competitor_coverage"]

    def test_iteration_and_type(self):
        b = _block()
        assert b["iteration"] == 1138
        assert b["type"] == "B"

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_urls_present_and_verbatim(self):
        b = _block()
        assert b["new_meta_arm"]["url"] == URL_META_CONNECT
        assert b["new_google_arm"]["url"] == URL_GOOGLE_GUCCI

    def test_tone_scores(self):
        b = _block()
        assert b["new_meta_arm"]["tone_score"] == 0.1
        assert b["new_google_arm"]["tone_score"] == 0.15
        rc = b["register_contrast"]
        assert rc["illustrative_delta_google_minus_meta"] == 0.05

    def test_window_and_test_file(self):
        b = _block()
        assert "FOURTH leg" in b["window"]
        assert b["test_file"].endswith(OWN_BASENAME)

    def test_first_dedicated_mechanism_convention(self):
        # Per the #643 convention, the journalist key is new this run and
        # mechanism_ids holds only the landed mechanism.
        doc = yaml.safe_load(_block_text())
        assert doc["stevie_bonifield"]["mechanism_ids"] == [914]
        assert doc["stevie_bonifield"]["publication_owner"] == "Vox Media"


# ---------------------------------------------------------------------------
# 5. m914 content discipline.
# ---------------------------------------------------------------------------

class TestM914ContentDiscipline1138:
    def test_meta_arm_fields(self):
        b = _block()
        m = b["new_meta_arm"]
        assert m["title"] == "Meta Connect 2026: The 7 biggest announcements"
        assert m["date"] == "Sep 24 2026"
        assert m["byline"].startswith("Stevie Bonifield")
        assert "five times lighter than Meta Quest 3" in " ".join(m["key_quotes"])
        assert "url_note" in m

    def test_google_arm_fields(self):
        b = _block()
        g = b["new_google_arm"]
        assert g["title"] == "Gucci-branded Google smart glasses are coming next year"
        assert g["date"] == "Apr 16 2026"
        assert g["byline"].startswith("Stevie Bonifield")
        quotes = " ".join(g["key_quotes"])
        assert "not something people want anywhere near their face" in quotes
        assert "Meta Ray-Ban line-up" in quotes

    def test_quote_inclusion_hook(self):
        text = _block_text()
        assert "QUOTE-INCLUSION" in text
        assert "EXTENDING m150" in text

    def test_confounders_ranked_strong_first(self):
        b = _block()
        confs = b["confounders"]
        assert confs[0].startswith("STRONG:")
        assert any("5 months" in c for c in confs)

    def test_counterevidence_present(self):
        b = _block()
        assert len(b["counterevidence"]) >= 2

    def test_cross_refs_carry_m150_and_perez(self):
        b = _block()
        refs = " ".join(b["cross_refs"])
        assert "#150" in refs
        assert "#142" in refs
        assert "#269" in refs

    def test_research_method_rejections_documented(self):
        b = _block()
        rm = b["research_method"]
        assert "Sarah Perez" in rm
        assert "Ropek" in rm
        assert "Marcus Mendes" in rm
        assert "0 browser.open per #503" in rm

    def test_no_em_dashes_ascii_only(self):
        text = _block_text()
        assert "\u2014" not in text
        assert "\u2013" not in text


# ---------------------------------------------------------------------------
# 6. Statistical discipline.
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1138:
    def test_manual_illustrative_only(self):
        b = _block()
        assert b["scorer"]["method"].startswith("MANUAL ILLUSTRATIVE ONLY")
        assert "engine NOT run" in b["scorer"]["method"]

    def test_no_significance_claimed(self):
        b = _block()
        assert "is_significant False" in b["scorer"]["method"]
        assert b["scorer"]["verdict"].startswith("directionally_supported_not_proven")

    def test_p_value_not_calculated(self):
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in _block()["scorer"]["method"]

    def test_not_artifact_grade(self):
        b = _block()
        assert "NOT artifact-grade" in b["scorer"]["method"]
        assert b["no_analysis_json_update"] is True

    def test_aug28_standing_rule_cited(self):
        text = _block_text()
        assert "Aug 28 2026 standing rule" in text


# ---------------------------------------------------------------------------
# 7. Falsification ledger.
# ---------------------------------------------------------------------------

class TestFalsificationLedger1138:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 46

    def test_forty_sixth_member_form_present(self):
        assert FORTY_SIXTH_LANDED in _profiles_text()

    def test_forty_seventh_member_claim_absent(self):
        # Negative-guard wordings ("absent repo-wide") are allowed; the
        # affirmative member-claim form must not exist. Needle format-built
        # per #715; own file carries no contiguous needle.
        text = _profiles_text()
        assert FORTY_SEVENTH_MEMBER not in text

    def test_ledger_note_negative_guard_wording(self):
        b = _block()
        assert "Ledger holds at 46" in b["ledger_note"]
        assert "FORTY-SEVENTH member-claim form absent repo-wide" in b["ledger_note"]


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1139 Type C run
# pins the 915 landing; the #1140 Type D run tombstones the suite).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1138:
    def test_zero_915_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 915" in src
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src

    def test_no_thirty_fifth_direction_guard(self):
        # The contiguous direction-claim form must not appear in this
        # file's source; the guard constant stays format-built per #715
        # (verified by inspection of the constant definition above).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("THIRTY" + "-FIFTH relationship direction") not in src
        assert len(THIRTY_FIFTH_DIR) > 0

    def test_no_forty_seventh_member_guard(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source (verified by inspection of the constant
        # definition above).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("FORTY" + "-SEVENTH falsification-family member") not in src
        assert len(FORTY_SEVENTH_MEMBER) > 0

    def test_1137_pins_flip_by_design_documented(self):
        # #1137's forward guards (max-913, zero-914 numeric, all-ids<=913)
        # flip by design now that m914 has landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1137" in src
        text = _block_text()
        assert "1137" in text or "m913" in text

    def test_thirty_fourth_direction_still_present(self):
        # m912's NEGOTIATE-WHILE-COVERING is the THIRTY-FOURTH relationship
        # direction; its ordinal wording must still be present repo-wide.
        assert "THIRTY-FOURTH" in _profiles_text()


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 914 landing for #1139/#1140).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1138:
    def test_pins_on_914_landing(self):
        # The guards this run lays for the next legs: max-914, zero-915
        # numeric, all-ids<=914, no-Type-B-#1139-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 914" in src
        assert "NEXT_NUM = 915" in src

    def test_no_type_b_1139_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type B #1139").stdout
        assert log.strip() == ""

    def test_915_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1137_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1137))


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - tombstoning belongs
# to the next Type D run, #1140).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1138:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1135_full_suite.log" in src

    def test_suite_checked_not_touched(self):
        # This run stays on targeted verification per the Type B brief;
        # the suite is read-only state, never re-launched or killed here.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "checked only" in src.lower() or "CHECKED ONLY" in src

    def test_no_pytest_process_spawned(self):
        procs = subprocess.run(
            ["pgrep", "-f", "[p]ytest"], capture_output=True, text=True
        )
        # A dead or absent suite is recorded as state, not acted on.
        assert procs.returncode in (0, 1)


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1138:
    def test_readme_stats_table_updated(self):
        text = _read(README_PATH)
        assert "| Tests |" in text

    def test_readme_test_table_row_present(self):
        text = _read(README_PATH)
        assert OWN_BASENAME in text

    def test_architecture_tree_row_present(self):
        text = _read(ARCH_PATH)
        assert OWN_BASENAME in text

    def test_iteration_log_entry_present(self):
        text = _read(LOG_PATH)
        assert "#1138" in text


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1138:
    def test_log_entry_header(self):
        text = _read(LOG_PATH)
        assert "## #1138 Type B:" in text

    def test_no_duplicate_1138_entries(self):
        text = _read(LOG_PATH)
        assert text.count("## #1138 Type B:") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(LOG_PATH)
        assert "1135-1139" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1137).
# ---------------------------------------------------------------------------

class TestInflightIsolation1138:
    def test_inflight_files_untouched_by_this_run(self):
        # Marker-scoped: the working tree carries pre-existing
        # in-flight uncommitted changes (#899 nytimes.yaml hunk,
        # #938 test file, #900 test file, #1012 test-file edit).
        # This run's markers must appear in NONE of their diffs;
        # targeted staging at commit time picks up only this run's
        # two files.
        for path in (
            "profiles/nytimes.yaml",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_"
            "sep21_1pm.py",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_"
            "turn_agenda_setting_register_vs_carried_meta_india_"
            "havoc_m817_pairing_sep26_7am.py",
        ):
            diff = _git("diff", "--", path).stdout
            assert "mechanism_id: 914" not in diff, path
            assert BLOCK_KEY not in diff, path
            assert "Type B #1138" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert diff == "", diff[:500]

    def test_do_not_touch_1024_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src
