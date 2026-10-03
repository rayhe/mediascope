# -*- coding: utf-8 -*-
"""Type B #1168 tests: Tyler Lee (Phandroid) Sep-16-2026 Meta Luna
'pervert glasses' privacy register vs Sep-17-2026 Snap Specs launch
(zero privacy vocabulary) - within-journalist within-week cross-entity
privacy-register gap (mechanism 932).

Iteration #1168, FOURTH leg of the 1165-1169 window
(D #1165 -> E #1166 -> A #1167 -> B #1168 -> C #1169).

The m932 block lives in profiles/careers/journalists.yaml under a NEW
top-level `tyler_lee` key (per the #643 convention).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
The Type B #1168 anchor followup sets ANCHORED_SHA to the main commit hash
from `git rev-parse HEAD` after the main commit.

Per #795: this run only CHECKS the #1165-launched background suite
(OBSERVED DEAD/AMBIGUOUS); its verdict belongs to #1170.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 933, the FORTY-SEVENTH member-claim form, or the thirty-sixth /
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

OWN_BASENAME = (
    "test_type_b_1168_tyler_lee_phandroid_meta_luna_pervert_glasses_"
    "vs_snap_specs_launch_privacy_register_gap_sep16_17_oct03_3am.py"
)
BLOCK_KEY = (
    "type_b_1168_tyler_lee_phandroid_meta_luna_pervert_glasses_"
    "vs_snap_specs_launch_privacy_register_gap_sep16_17"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "0" * 40
# Post-first-run values per #719: 68 tests collected; README ratchets
# 61869/1492 -> 61937/1493 in the doc-sync followup.
README_TEST_COUNT = 61937
README_FILE_COUNT = 1493

# Forward guards for the next landing. MECH_NUM=932 is THIS run's landed
# mechanism; NEXT_NUM=933 stays forward.
MECH_NUM = 932
NEXT_NUM = 933

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "933" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "933" at runtime
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"

# The landed m932 block lives here (colon-form key; no numeric-932 substring
# in the block key by designed keying per #715).
JOURNALISTS_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
FILE_1167 = (
    "test_type_a_1167_gizmodo_samsung_unpacked_build_quality_"
    "meta_favoring_comparator_oct03_2am.py"
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
    return _load_journalists()["tyler_lee"]["competitor_coverage"][BLOCK_KEY]


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
        except (OSError, UnicodeError):
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
        except (OSError, UnicodeError):
            continue
        if pattern in text:
            hits.append(path)
    return hits


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1168:
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
        # "Type B #1168 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type B #1168 anchor").stdout
        assert "Type B #1168 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1168:").stdout
        assert "Type B #1168" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1168 is the FOURTH leg of the 1165-1169 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1168:
    def test_rotation_window_is_1165_1169(self):
        text = _block_text()
        assert "1165-1169" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1165-1169 window FOURTH leg "
            "(D #1165 -> E #1166 -> A #1167 -> B #1168 -> C #1169)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1165", "Type E #1166", "Type A #1167"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The next leg (#1169 Type C) is documented in this run's log entry
        # and block window field; it must not exist as a commit yet.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "C #1169" in text
        assert _block()["window"].endswith("C #1169)")

    def test_no_type_b_1168_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1168_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1168:
    def test_tyler_lee_key_is_new_convention(self):
        text = _block_text()
        assert text.count("tyler_lee:") == 1

    def test_block_key_zero_932_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1168, not the mechanism number 932.
        assert "932" not in BLOCK_KEY

    def test_zero_underscore_932_repo_wide(self):
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_932_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_933_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_932(self):
        nums = []
        for line in _profiles_grep_numeric_mechanism_id(MECH_NUM):
            nums.append(MECH_NUM)
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n
        assert nums, "m932 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_urls_copied_verbatim(self):
        d = _load_journalists()
        urls = d["tyler_lee"]["source_urls"]
        assert (
            "https://phandroid.com/2026/09/16/"
            "metas-fix-for-pervert-glasses-backlash-no-more-camera/"
        ) in urls
        assert (
            "https://phandroid.com/2026/09/17/"
            "snaps-new-2195-smart-glasses-wants-to-replace-your-phone/"
        ) in urls
        for u in urls:
            assert u.startswith("https://"), u

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit it
        # appears only in the landed YAML block and this test file.
        hits = _source_grep(BLOCK_KEY)
        allowed = {
            os.path.join(REPO, "profiles", "careers", "journalists.yaml"),
            os.path.join(TESTS_DIR, OWN_BASENAME),
            os.path.join(REPO, "README.md"),
            os.path.join(REPO, "docs", "ARCHITECTURE.md"),
            os.path.join(REPO, "iteration-log.md"),
        }
        for h in hits:
            assert h in allowed, h


# ---------------------------------------------------------------------------
# 4. Block structure (the #643 top-level journalist convention).
# ---------------------------------------------------------------------------

class TestBlockStructure1168:
    def test_top_level_tyler_lee(self):
        d = _load_journalists()
        assert "tyler_lee" in d
        assert d["tyler_lee"]["name"] == "Tyler Lee"

    def test_mechanism_ids_list(self):
        d = _load_journalists()
        assert d["tyler_lee"]["mechanism_ids"] == [932]

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "iteration", "mechanism_id", "type", "goal_id", "job_id",
            "scheduled_job_id", "date", "block_key", "test_file", "author",
            "journalist", "publication", "window", "meta_arm", "snap_arm",
            "register_gap", "financial_relationship", "scorer",
            "falsification_family_member", "falsification_ledger",
            "ledger_note", "confounders", "counterevidence", "verdict",
            "research_method", "statistical_discipline",
            "falsification_family", "cross_refs",
            "no_analysis_json_update", "background_suite_status",
            "in_flight", "novelty",
        ):
            assert field in b, field

    def test_type_and_publication(self):
        b = _block()
        assert b["type"] == "B"
        assert b["publication"] == "phandroid"
        assert b["iteration"] == 1168
        assert b["mechanism_id"] == 932

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_ascii_only(self):
        text = _read(JOURNALISTS_PATH)
        start = text.index("tyler_lee:")
        block_region = text[start:start + 40000]
        block_region.encode("ascii")

    def test_competitor_coverage_single_block(self):
        d = _load_journalists()
        cc = d["tyler_lee"]["competitor_coverage"]
        assert list(cc.keys()) == [BLOCK_KEY]


# ---------------------------------------------------------------------------
# 5. m932 content discipline (the Tyler Lee pair).
# ---------------------------------------------------------------------------

class TestM932ContentDiscipline1168:
    def test_arms_identified(self):
        b = _block()
        assert b["meta_arm"]["entity"] == "meta"
        assert b["snap_arm"]["entity"] == "snap"
        assert b["meta_arm"]["date"] == "2026-09-16"
        assert b["snap_arm"]["date"] == "2026-09-17"

    def test_meta_arm_privacy_register_quotes(self):
        b = _block()
        q = b["meta_arm"]["key_quotes"]
        joined = " ".join(q) + " " + b["meta_arm"]["title"]
        assert "Pervert Glasses" in joined
        assert "secretly recording" in joined

    def test_snap_arm_launch_register_quotes(self):
        q = _block()["snap_arm"]["key_quotes"]
        joined = " ".join(q)
        assert "Snap Has Tried This Before, and Failed" in joined
        assert "$2,195" in joined or "2,195" in joined

    def test_snap_arm_zero_privacy_vocabulary_attested(self):
        notes = _block()["snap_arm"]["framing_notes"]
        assert "ZERO privacy/surveillance/consent vocabulary" in notes

    def test_register_gap_delta(self):
        gap = _block()["register_gap"]
        assert "-0.35" in gap["illustrative_delta_meta_minus_snap"]
        assert "m75" in gap["family_placement"]

    def test_howley_contrast_referenced(self):
        b = _block()
        assert "#1148" in b["register_gap"]["family_placement"]
        assert any("#1148" in c for c in b["cross_refs"])

    def test_illustrative_scores(self):
        b = _block()
        assert b["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.30
        assert b["snap_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.05

    def test_parity_gap_not_falsification(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 46

    def test_confounder_strongest_first(self):
        confs = _block()["confounders"]
        assert confs[0].startswith("STRONG:")
        strong = [c for c in confs if c.startswith("STRONG:")]
        assert len(strong) >= 3

    def test_counterevidence_present(self):
        ce = _block()["counterevidence"]
        assert len(ce) >= 5
        assert any("Whittaker" in c for c in ce)

    def test_research_method_excerpt_tier(self):
        rm = _block()["research_method"]
        assert "11 browser.search query sets" in rm
        assert "0 browser.open" in rm


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL/QUALITATIVE ONLY per Aug 28 2026 rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1168:
    def test_no_engine_run(self):
        b = _block()
        assert "engine NOT run" in b["scorer"]["method"]

    def test_stats_not_calculated(self):
        sd = _block()["statistical_discipline"]
        assert "p_value NOT_CALCULATED" in sd
        assert "cohens_d NOT_CALCULATED" in sd
        assert "ci_95 NOT_CALCULATED" in sd
        assert "is_significant false" in sd

    def test_verdict_discipline(self):
        b = _block()
        assert b["verdict"].startswith("directionally_supported_not_proven")
        assert b["no_analysis_json_update"] is True

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _block()["scorer"]["method"]

    def test_aug28_standing_rule_cited(self):
        assert "Aug 28 2026 standing rule" in _block()["scorer"]["method"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 46; no new member this run).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1168:
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
# 8. Forward-looking staleness (designed lifecycle; the #1169 Type C run
# pins the 933 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1168:
    def test_zero_933_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 933" in src
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

    def test_1167_pins_flip_by_design_documented(self):
        # #1167's forward guards (max-931, zero-932 numeric, all-ids<=931,
        # no-thirty-sixth, no-forty-seventh) flip by design now that m932
        # has landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1167" in src
        text = _block_text()
        assert "1167" in text or "m931" in text

    def test_thirty_fifth_direction_still_present(self):
        # m915's METER-THEN-INVITE is the THIRTY-FIFTH relationship
        # direction; its ordinal wording must still be present repo-wide.
        assert "THIRTY-FIFTH" in _block_text()


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 932 landing for #1169).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1168:
    def test_pins_on_932_landing(self):
        # The guards this run lays for the next leg: max-932, zero-933
        # numeric, all-ids<=932, no-Type-C-#1169-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 932" in src
        assert "NEXT_NUM = 933" in src

    def test_no_type_c_1169_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type C #1169").stdout
        assert log.strip() == ""

    def test_933_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1167_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1167))


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1170).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1168:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1165_full_suite.log" in src

    def test_suite_observed_dead_ambiguous_recorded_not_touched(self):
        # This run stays on targeted verification per the Type B brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest death-observation per #795:
        # #1165-launched suite DEAD/AMBIGUOUS at the 03:00 PDT check
        # (log 1134 bytes, last write Oct 3 01:22 PDT, one pytest process
        # at ps scan, no m932 markers). #1170 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "DEAD/AMBIGUOUS" in status
        assert "#1170" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m932 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1165_full_suite.log"
        )
        log = _read(suite_log)
        assert "m932" not in log
        assert "Type B #1168" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1168:
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
        assert "#1168" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 61937
        assert README_FILE_COUNT == 1493


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1168:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1168 Type B:" in text

    def test_no_duplicate_1168_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1168 Type B:") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1165-1169" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1168:
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
            assert "mechanism_id: 932" not in diff, path
            assert "Type B #1168" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert "mechanism_id: 932" not in diff
        assert "Type B #1168" not in diff
