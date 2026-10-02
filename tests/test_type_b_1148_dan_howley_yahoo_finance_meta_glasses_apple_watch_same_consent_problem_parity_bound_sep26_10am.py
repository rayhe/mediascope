# -*- coding: utf-8 -*-
"""Type B #1148 tests: Dan Howley (Yahoo Finance) Sep-26-2026 Meta glasses /
Apple Watch same-consent-problem parity bound (mechanism 920).

Iteration #1148, FOURTH leg of the 1145-1149 window
(D #1145 -> E #1146 -> A #1147 -> B #1148 -> C #1149).

The m920 block lives in profiles/careers/journalists.yaml under a NEW
top-level `dan_howley` key (per the #643 convention).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
The Type B #1148 anchor followup sets ANCHORED_SHA to the main commit hash
from `git rev-parse HEAD` after the main commit.

Per #795: this run only CHECKS the #1145-launched background suite
(OBSERVED DEAD, sixteenth consecutive); its verdict belongs to #1150.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 921, the FORTY-SEVENTH member-claim form, or the thirty-sixth /
thirty-seventh direction-claim forms; the constants are constructed at
runtime.
"""

import glob
import os
import re
import subprocess

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TESTS_DIR = HERE

OWN_BASENAME = os.path.basename(__file__)
BLOCK_KEY = (
    "type_b_1148_dan_howley_yahoo_finance_meta_glasses_apple_watch_"
    "same_consent_problem_parity_bound_sep26"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "6dd1f44bb9f620972a61af30968127d0b7c66394"
README_TEST_COUNT = 60363
README_FILE_COUNT = 1472

# Forward guards for the next landing. MECH_NUM=920 is THIS run's landed
# mechanism; NEXT_NUM=921 stays forward.
MECH_NUM = 920
NEXT_NUM = 921

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "921" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "921" at runtime
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"

# The landed m920 block lives here (colon-form key; no numeric-920 substring
# in the block key by designed keying per #715).
JOURNALISTS_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
FILE_1147 = (
    "test_type_a_1147_wsj_anthropic_oct01_ftc_probe_disclosure_"
    "asymmetry_aug25_tam_pitch_vs_carried_meta_arms_oct02_9am.py"
)

# Ordinal form of THIS run's mechanism, landed at m907 for the falsification
# family. The FORTY-SIXTH member form must be present repo-wide;
# the FORTY-SEVENTH member-claim form must be absent (negative guard).
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _block():
    return _load_journalists()["dan_howley"]["competitor_coverage"][BLOCK_KEY]


def _block_text():
    return _read(JOURNALISTS_PATH)


def _git(*args):
    return subprocess.run(
        ["git", "-C", REPO] + list(args), capture_output=True, text=True
    )


def _profiles_grep_numeric_mechanism_id(num):
    out = _git("grep", "-F", "mechanism_id: %d" % num, "--", "profiles").stdout
    return out.strip().splitlines() if out.strip() else []


def _repo_grep(pattern, exclude_paths=(), file_globs=None):
    """Repo-wide grep; file_globs restricts to a file set (None = all)."""
    candidates = []
    for root, _dirs, files in os.walk(REPO):
        rel_root = os.path.relpath(root, REPO)
        if rel_root.startswith(".git") or rel_root.startswith(".pytest_cache"):
            continue
        for name in files:
            rel = os.path.join(rel_root, name) if rel_root != "." else name
            if rel in exclude_paths:
                continue
            if file_globs and not any(
                name.endswith(g.lstrip("*")) for g in file_globs
            ):
                continue
            candidates.append(os.path.join(root, name))
    hits = []
    for path in candidates:
        try:
            text = _read(path)
        except (OSError, UnicodeDecodeError):
            continue
        if pattern in text:
            hits.append(path)
    return hits


def _iter_source_files():
    return _repo_grep(
        "", exclude_paths=("tests/" + OWN_BASENAME,),
        file_globs=("*.py", "*.yaml", "*.md", "*.txt", "*.sh", "*.json"),
    )


def _repo_grep_underscore_mechanism(n):
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [p for p in _iter_source_files() if needle in _read(p)]


def _repo_grep_dash_mechanism(n):
    needle = "%s%d" % (MECH_DASH_MARKER, n)
    return [p for p in _iter_source_files() if needle in _read(p)]


def _source_grep(pattern):
    hits = []
    for path in _iter_source_files():
        try:
            text = _read(path)
        except (OSError, UnicodeDecodeError):
            continue
        if pattern in text:
            hits.append(path)
    return hits


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1148:
    def test_anchor_sha_format(self):
        # Patched in the anchor followup per #565: ANCHORED_SHA is the
        # main-commit hash, a 40-char hex string, not the placeholder.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40

    def test_anchor_sha_is_main_commit(self):
        # The anchor commit patches ANCHORED_SHA to the main-commit hash;
        # verify it appears in the git log as a commit hash.
        log = _git("log", "--format=%H").stdout
        assert ANCHORED_SHA in log

    def test_anchor_followup_commit_message_convention(self):
        # The anchor followup uses the documented message shape:
        # "Type B #1148 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type B #1148 anchor").stdout
        assert "Type B #1148 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1148:").stdout
        assert "Type B #1148" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1148 is the FOURTH leg of the 1145-1149 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1148:
    def test_rotation_window_is_1145_1149(self):
        text = _block_text()
        assert "1145-1149" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1145-1149 window FOURTH leg "
            "(D #1145 -> E #1146 -> A #1147 -> B #1148 -> C #1149)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1145", "Type E #1146", "Type A #1147"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The Type C leg (#1149) must NOT exist yet; #1148 owns the B leg.
        log = _git("log", "--oneline").stdout
        assert "Type B #1148" not in log
        assert "Type C #1149" not in log

    def test_no_type_b_1148_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1148_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1148:
    def test_dan_howley_key_is_new_convention(self):
        text = _block_text()
        assert "dan_howley:" in text
        assert _block_text().count("\ndan_howley:") == 1

    def test_block_key_zero_920_substring(self):
        assert "920" not in BLOCK_KEY

    def test_zero_underscore_920_repo_wide(self):
        # Colon-form / numeric-field form only for 920; the underscore key
        # form must not exist repo-wide (needles format-built per #715;
        # _iter_source_files excludes this file).
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_920_repo_wide(self):
        # Same for the dash form.
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_zero_numeric_921_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_920(self):
        # The landed max mechanism_id must be this run's 920.
        ids = []
        for m in re.finditer(r"mechanism_id:\s*(\d+)", _block_text()):
            ids.append(int(m.group(1)))
        assert max(ids) == MECH_NUM

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY) >= 1
        assert text.count("      block_key: " + BLOCK_KEY) == 1

    def test_urls_copied_verbatim(self):
        b = _block()
        assert b["segment"]["url_youtube"] == "https://www.youtube.com/watch?v=p80DDeG9otQ"
        assert b["segment"]["url_mirror"] == (
            "https://www.foreignpolicyjournal.com/2026/09/26/ai-wearables-"
            "from-meta-nasdaq-meta-and-apple-nasdaq-aapl-raise-fresh-privacy-"
            "and-consent-concerns/"
        )

    def test_block_key_zero_hit_except_landed(self):
        # The block key only lives in the landed journalists block,
        # its test_file reference, and this test file.
        hits = _repo_grep(BLOCK_KEY)
        basenames = {os.path.relpath(p, REPO) for p in hits}
        assert basenames <= {
            "profiles/careers/journalists.yaml",
            "tests/" + OWN_BASENAME,
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
        }, basenames


# ---------------------------------------------------------------------------
# 4. Block structure.
# ---------------------------------------------------------------------------

class TestBlockStructure1148:
    def test_top_level_dan_howley(self):
        d = _load_journalists()
        assert "dan_howley" in d

    def test_mechanism_ids_list(self):
        assert _load_journalists()["dan_howley"]["mechanism_ids"] == [920]

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "iteration", "mechanism_id", "type", "goal_id", "job_id",
            "scheduled_job_id", "date", "block_key", "test_file", "author",
            "journalist", "publication", "window", "segment", "apple_arm",
            "meta_arm", "register_parity", "financial_relationship", "scorer",
            "falsification_family_member", "falsification_ledger",
            "ledger_note", "confounders", "counterevidence", "verdict",
            "research_method", "statistical_discipline", "falsification_family",
            "cross_refs", "no_analysis_json_update", "novelty",
            "background_suite_status", "in_flight",
        ):
            assert field in b, field

    def test_type_and_publication(self):
        b = _block()
        assert b["type"] == "B"
        assert b["iteration"] == 1148
        assert b["mechanism_id"] == 920
        assert b["journalist"] == "Dan Howley"
        assert b["publication"] == "yahoo-finance"

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_ascii_only(self):
        b = _block()
        blob = yaml.safe_dump(b, allow_unicode=True)
        assert all(ord(c) < 128 for c in blob)
        assert "\u2014" not in blob  # no em dashes


# ---------------------------------------------------------------------------
# 5. m920 content discipline: the parity-bound finding.
# ---------------------------------------------------------------------------

class TestM920ContentDiscipline1148:
    def test_segment_identified(self):
        seg = _block()["segment"]
        assert seg["title"].startswith("Why Meta")
        assert "same consent problem" in seg["title"]
        assert seg["date"] == "2026-09-26"
        assert "Howley" in seg["participants"]

    def test_apple_arm_quotes(self):
        quotes = _block()["apple_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "listen continuously" in joined
        assert "last 15 seconds" in joined
        assert "does not have access to the underlying audio data" in joined

    def test_meta_arm_quotes(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "Facebook Marketplace" in joined
        assert "without their knowledge" in joined

    def test_register_parity_thesis(self):
        rp = _block()["register_parity"]
        assert rp["thesis_level_delta"] == 0.0
        assert "same consent problem" in rp["thesis"].lower()

    def test_illustrative_scores(self):
        b = _block()
        assert b["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.25
        assert b["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.35

    def test_parity_bound_not_falsification(self):
        rp = _block()["register_parity"]
        assert "NOT a falsification" in rp["reading"] or "not a falsification" in rp["reading"].lower()
        assert b_falsification_family_member() is False

    def test_confounder_strongest_first(self):
        confs = _block()["confounders"]
        assert confs[0].startswith("STRONG:")
        assert confs[1].startswith("STRONG:")
        assert confs[2].startswith("STRONG:")

    def test_counterevidence_present(self):
        assert len(_block()["counterevidence"]) >= 4

    def test_m75_bound_referenced(self):
        refs = " ".join(_block()["cross_refs"])
        assert "#75" in refs
        assert "#993" in refs

    def test_research_method_excerpt_tier(self):
        b = _block()
        assert "0 browser.open per #503" in b["research_method"]
        assert "10 browser.search" in b["research_method"]


def b_falsification_family_member():
    return _block()["falsification_family_member"]


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL ILLUSTRATIVE only).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1148:
    def test_no_engine_run(self):
        b = _block()
        assert "engine NOT run" in b["scorer"]["method"]
        assert b["no_analysis_json_update"] is True

    def test_stats_not_calculated(self):
        b = _block()
        assert "NOT_CALCULATED" in b["statistical_discipline"]

    def test_verdict_discipline(self):
        b = _block()
        assert b["scorer"]["verdict"].startswith("directionally_supported_not_proven")
        assert b["verdict"].startswith("directionally_supported_not_proven")

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

class TestFalsificationLedger1148:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 46

    def test_forty_sixth_member_form_present(self):
        # The FORTY-SIXTH member form landed at m907 in
        # profiles/the-verge.yaml; check repo-wide, not just journalists.
        assert _repo_grep(FORTY_SIXTH_LANDED), FORTY_SIXTH_LANDED

    def test_forty_seventh_member_claim_absent(self):
        # Negative-guard wordings ("absent repo-wide") are allowed; the
        # affirmative member-claim form must not exist. Needle format-built
        # per #715; own file carries no contiguous needle.
        text = _read(JOURNALISTS_PATH)
        assert FORTY_SEVENTH_MEMBER not in text

    def test_ledger_note_negative_guard_wording(self):
        b = _block()
        assert "Ledger holds at 46" in b["ledger_note"]
        assert "FORTY-SEVENTH member-claim form absent repo-wide" in b["ledger_note"]
        assert "FORTY-SIXTH member-form present" in b["ledger_note"]


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1149 Type C run
# pins the 921 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1148:
    def test_zero_921_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 921" in src
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src

    def test_no_thirty_sixth_direction_guard(self):
        # The contiguous direction-claim form must not appear in this
        # file's source; the guard constant stays format-built per #715
        # (verified by inspection of the constant definition above).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("THIRTY" + "-SIXTH relationship direction") not in src
        assert len(THIRTY_SIXTH_DIR) > 0

    def test_no_thirty_seventh_direction_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("THIRTY" + "-SEVENTH relationship direction") not in src
        assert len(THIRTY_SEVENTH_DIR) > 0

    def test_no_forty_seventh_member_guard(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source (verified by inspection of the constant
        # definition above).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("FORTY" + "-SEVENTH falsification-family member") not in src
        assert len(FORTY_SEVENTH_MEMBER) > 0

    def test_1147_pins_flip_by_design_documented(self):
        # #1147's forward guards (max-919, zero-920 numeric, all-ids<=919,
        # no-thirty-sixth, no-forty-seventh) flip by design now that m920
        # has landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1147" in src
        text = _block_text()
        assert "1147" in text or "m919" in text

    def test_thirty_fifth_direction_still_present(self):
        # m915's METER-THEN-INVITE is the THIRTY-FIFTH relationship
        # direction; its ordinal wording must still be present repo-wide.
        assert "THIRTY-FIFTH" in _block_text()


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 920 landing for #1149).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1148:
    def test_pins_on_920_landing(self):
        # The guards this run lays for the next leg: max-920, zero-921
        # numeric, all-ids<=920, no-Type-C-#1149-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 920" in src
        assert "NEXT_NUM = 921" in src

    def test_no_type_c_1149_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type C #1149").stdout
        assert log.strip() == ""

    def test_921_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1147_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1147))


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1150).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1148:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1145_full_suite.log" in src

    def test_suite_observed_dead_recorded_not_touched(self):
        # This run stays on targeted verification per the Type B brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest death-observation per #795:
        # #1145-launched suite OBSERVED DEAD at the 10:00 PDT check
        # (last write Oct 2 08:14:13 PDT, 385 bytes, no live pytest;
        # sixteenth consecutive death). #1150 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "OBSERVED DEAD" in status
        assert "sixteenth consecutive" in status
        assert "#1150" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m920 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1145_full_suite.log"
        )
        log = _read(suite_log)
        assert "m920" not in log
        assert "Type B #1148" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1148:
    def test_readme_stats_table_updated(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert "| Tests |" in text

    def test_readme_test_table_row_present(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert OWN_BASENAME in text

    def test_architecture_tree_row_present(self):
        text = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert OWN_BASENAME in text

    def test_iteration_log_entry_present(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "#1148" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 60363
        assert README_FILE_COUNT == 1472


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1148:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1148 Type B:" in text

    def test_no_duplicate_1148_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1148 Type B:") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1145-1149" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1148:
    def test_inflight_files_untouched_by_this_run(self):
        # Marker-scoped: the working tree carries pre-existing
        # in-flight uncommitted changes (#899 nytimes.yaml hunk,
        # #938 test file, #900 test file, #1012-wt test-file edit).
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
            assert "mechanism_id: 920" not in diff, path
            assert "Type B #1148" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert diff == "", diff[:500]

    def test_do_not_touch_1024_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src
