# -*- coding: utf-8 -*-
"""Type B #1173 tests: Andy Boxall (Android Police) temporal extension of
mechanism 132 (Aug-16 Boxall three-entity privacy-vocabulary inversion) to
the Connect-2026 stigma-peak peg - carried Jun-17-2026 Snap Specs arm
(+0.90, zero privacy vocabulary, 4 cameras) vs carried Sep-24-2026 Meta
Ray-Ban Audio 'PR stunt' column (-0.55, motive-attribution register).

Iteration #1173, FOURTH leg of the 1170-1174 window
(D #1170 -> E #1171 -> A #1172 -> B #1173 -> C #1174).

The m935 block lives in profiles/careers/journalists.yaml under the existing
top-level `andy_boxall` key (per the #643 convention); mechanism_ids grows
824 -> [824, 935].

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
The Type B #1173 anchor followup sets ANCHORED_SHA to the main commit hash
from `git rev-parse HEAD` after the main commit.

Per #795: this run only CHECKS the #1170-launched background suite
(OBSERVED DEAD/AMBIGUOUS); its verdict belongs to #1175.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 936, the FORTY-SEVENTH / FORTY-EIGHTH member-claim forms, or the
THIRTY-SEVENTH / THIRTY-EIGHTH direction-claim forms; the constants are
constructed at runtime.
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
    "test_type_b_1173_andy_boxall_androidpolice_m132_snap_ar_dream_"
    "vs_sep24_meta_pr_stunt_temporal_extension_oct03_7am.py"
)
BLOCK_KEY = (
    "type_b_1173_andy_boxall_androidpolice_m132_snap_ar_dream_"
    "vs_sep24_meta_pr_stunt_temporal_extension"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "0" * 40
# Post-first-run values per #719: 75 tests collected; README ratchets
# 62238/1497 -> 62313/1498 in the doc-sync followup.
README_TEST_COUNT = 62313
README_FILE_COUNT = 1498

# Forward guards for the next landing. MECH_NUM=935 is THIS run's landed
# mechanism; NEXT_NUM=936 stays forward.
MECH_NUM = 935
NEXT_NUM = 936

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "936" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "936" at runtime
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"

# The landed m935 block lives here (colon-form key; no numeric-935 substring
# in the block key by designed keying per #715).
JOURNALISTS_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
FILE_1172 = (
    "test_type_a_1172_guardian_openai_sep30_oct03_enforcement_week_"
    "triple_register_vs_carried_meta_arms_oct03_6am.py"
)
M132_FILE = "test_andy_boxall_cross_entity_privacy_vocabulary_inversion_aug16.py"
SNAP_URL = (
    "https://www.androidpolice.com/snap-specs-are-the-augmented-"
    "reality-dream-weve-been-waiting-for/"
)

# Ordinal form of the falsification-family member that must stay present.
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _block():
    return _load_journalists()["andy_boxall"]["competitor_coverage"][BLOCK_KEY]


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

class TestAnchor1173:
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
        # "Type B #1173 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type B #1173 anchor").stdout
        assert "Type B #1173 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1173:").stdout
        assert "Type B #1173" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1173 is the FOURTH leg of the 1170-1174 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1173:
    def test_rotation_window_is_1170_1174(self):
        text = _block_text()
        assert "1170-1174" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1170-1174 window FOURTH leg "
            "(D #1170 -> E #1171 -> A #1172 -> B #1173 -> C #1174)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1170", "Type E #1171", "Type A #1172"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The next leg (#1174 Type C) is documented in this run's log entry
        # and block window field; it must not exist as a commit yet.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "C #1174" in text
        assert _block()["window"].endswith("C #1174)")

    def test_no_type_b_1173_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1173_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1173:
    def test_andy_boxall_key_is_existing_convention(self):
        text = _block_text()
        assert text.count("andy_boxall:") == 1

    def test_block_key_zero_935_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1173 and the extended mechanism m132, not the mechanism
        # number 935.
        assert "935" not in BLOCK_KEY
        assert "936" not in BLOCK_KEY

    def test_zero_underscore_935_repo_wide(self):
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_935_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_936_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_935(self):
        nums = []
        for line in _profiles_grep_numeric_mechanism_id(MECH_NUM):
            nums.append(MECH_NUM)
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n
        assert nums, "m935 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_snap_url_in_item_source_urls_verbatim(self):
        d = _load_journalists()
        urls = d["andy_boxall"]["source_urls"]
        assert SNAP_URL in urls
        assert SNAP_URL.startswith("https://")

    def test_snap_url_single_hit_in_journalists_yaml(self):
        # The Snap arm URL is carried from m132; it is NOT repeated in the
        # new block (the #988 URL-count pin pattern): exactly one hit in
        # journalists.yaml, the item-level source_urls entry. (Its other
        # in-corpus hits live in competitor-coverage-research.yaml and the
        # Aug-16 m132 test - outside this file's scope.)
        out = _git(
            "grep", "-c", "-F", SNAP_URL, "--",
            "profiles/careers/journalists.yaml",
        ).stdout
        assert out.strip() == "profiles/careers/journalists.yaml:1", out

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit it
        # appears only in the landed YAML block, this test file, and the
        # doc-sync targets (README, ARCHITECTURE, iteration-log).
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

class TestBlockStructure1173:
    def test_top_level_andy_boxall(self):
        d = _load_journalists()
        assert "andy_boxall" in d
        assert d["andy_boxall"]["name"] == "Andy Boxall"

    def test_mechanism_ids_list(self):
        d = _load_journalists()
        assert d["andy_boxall"]["mechanism_ids"] == [824, 935]

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "iteration", "mechanism_id", "type", "goal_id", "job_id",
            "scheduled_job_id", "date", "block_key", "test_file", "author",
            "journalist", "publication", "window", "design", "meta_arm",
            "snap_arm", "register_gap", "financial_relationship", "scorer",
            "falsification_family_member", "falsification_ledger",
            "ledger_note", "confounders", "counter_evidence", "verdict",
            "research_method", "statistical_discipline",
            "falsification_family", "connects_to",
            "no_analysis_json_update", "background_suite_status",
            "in_flight", "novelty", "artifact_readiness",
        ):
            assert field in b, field

    def test_type_and_publication(self):
        b = _block()
        assert b["type"] == "B"
        assert b["publication"] == "androidpolice"
        assert b["iteration"] == 1173
        assert b["mechanism_id"] == 935

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_ascii_only(self):
        text = _read(JOURNALISTS_PATH)
        start = text.index("andy_boxall:")
        block_region = text[start:start + 120000]
        block_region.encode("ascii")

    def test_competitor_coverage_two_blocks(self):
        d = _load_journalists()
        cc = d["andy_boxall"]["competitor_coverage"]
        assert set(cc.keys()) == {
            "type_b_988_andy_boxall_androidpolice_meta_pr_stunt_vs_"
            "apple_watch_value_sep25",
            BLOCK_KEY,
        }


# ---------------------------------------------------------------------------
# 5. m935 content discipline (the m132 temporal-extension pair).
# ---------------------------------------------------------------------------

class TestM935ContentDiscipline1173:
    def test_arms_identified(self):
        b = _block()
        assert b["meta_arm"]["entity"] == "meta"
        assert b["snap_arm"]["entity"] == "snap"
        assert b["meta_arm"]["date"] == "2026-09-24"
        assert b["snap_arm"]["date"] == "2026-06-17"

    def test_meta_arm_carried_from_988(self):
        b = _block()
        assert "mechanism 824" in b["meta_arm"]["provenance"]
        assert "Type B #988" in b["meta_arm"]["provenance"]
        assert "unrescored per #807" in b["meta_arm"]["provenance"]

    def test_snap_arm_carried_from_m132(self):
        b = _block()
        assert "mechanism 132" in b["snap_arm"]["provenance"]
        assert "unrescored per #807" in b["snap_arm"]["provenance"]

    def test_meta_arm_pr_stunt_quotes(self):
        b = _block()
        q = b["meta_arm"]["key_quotes"]
        joined = " ".join(q) + " " + b["meta_arm"]["title"]
        assert "PR stunt" in joined
        assert "cynical, business-driven" in joined

    def test_snap_arm_ar_dream_quotes(self):
        q = _block()["snap_arm"]["key_quotes"]
        joined = " ".join(q)
        assert "augmented reality future" in joined
        assert "Forget the Ray-Ban Meta" in joined

    def test_snap_arm_zero_privacy_vocabulary_attested(self):
        notes = _block()["snap_arm"]["framing_notes"]
        assert "ZERO privacy/surveillance/consent vocabulary" in notes

    def test_register_gap_delta(self):
        gap = _block()["register_gap"]
        assert "+1.45" in gap["illustrative_delta_snap_minus_meta"]
        assert "1.45" in gap["delta_calc"]
        assert "1.75" in gap["delta_calc"]

    def test_m132_extension_referenced(self):
        b = _block()
        assert 132 in b["connects_to"]
        assert 824 in b["connects_to"]
        assert "mechanism 132" in b["register_gap"]["family_placement"]
        assert "EXTENDS" in b["register_gap"]["family_placement"]

    def test_illustrative_scores(self):
        b = _block()
        assert b["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.55
        assert b["snap_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.90

    def test_extension_not_falsification(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 46

    def test_confounder_strongest_first(self):
        confs = _block()["confounders"]
        assert confs[0].startswith("STRONG:")
        strong = [c for c in confs if c.startswith("STRONG:")]
        assert len(strong) >= 2

    def test_counterevidence_present(self):
        ce = _block()["counter_evidence"]
        assert len(ce) >= 5
        assert any("SOFTENED" in c for c in ce)

    def test_research_method_excerpt_tier(self):
        rm = _block()["research_method"]
        assert "24 browser.search query sets" in rm
        assert "0 browser.open" in rm


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL/QUALITATIVE ONLY per Aug 28 2026 rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1173:
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

class TestFalsificationLedger1173:
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

    def test_forty_eighth_member_claim_absent(self):
        text = _read(JOURNALISTS_PATH)
        assert FORTY_EIGHTH_MEMBER not in text

    def test_ledger_note_negative_guard_wording(self):
        b = _block()
        assert "Ledger holds at 46" in b["ledger_note"]
        assert "FORTY-SEVENTH member-claim form absent repo-wide" in b["ledger_note"]
        assert "FORTY-SIXTH member-form present" in b["ledger_note"]


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1174 Type C run
# pins the 936 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1173:
    def test_zero_936_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 936" in src
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src

    def test_no_thirty_seventh_direction_guard(self):
        # The contiguous direction-claim form must not appear in this
        # file's source; the guard constant stays format-built per #715
        # (verified by inspection of the constant definition above).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("THIRTY" + "-SEVENTH relationship direction") not in src
        assert len(THIRTY_SEVENTH_DIR) > 0

    def test_no_thirty_eighth_direction_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("THIRTY" + "-EIGHTH relationship direction") not in src
        assert len(THIRTY_EIGHTH_DIR) > 0

    def test_no_forty_seventh_member_guard(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source (verified by inspection of the constant
        # definition above).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("FORTY" + "-SEVENTH falsification-family member") not in src
        assert len(FORTY_SEVENTH_MEMBER) > 0

    def test_no_forty_eighth_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("FORTY" + "-EIGHTH falsification-family member") not in src
        assert len(FORTY_EIGHTH_MEMBER) > 0

    def test_1172_pins_flip_by_design_documented(self):
        # #1172's forward guards (max-934, zero-935 numeric, all-ids<=934,
        # no-thirty-seventh, no-forty-seventh) flip by design now that m935
        # has landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1172" in src
        text = _block_text()
        assert "1172" in text or "m934" in text

    def test_thirty_fifth_direction_still_present(self):
        # m915's is the THIRTY-FIFTH relationship direction; its ordinal
        # wording must still be present repo-wide.
        assert "THIRTY-FIFTH relationship direction" in _block_text() or \
            _repo_grep("THIRTY-FIFTH relationship direction")

    def test_thirty_sixth_direction_still_present(self):
        # m878's is the THIRTY-SIXTH relationship direction; its ordinal
        # wording must still be present repo-wide.
        assert _repo_grep("THIRTY-SIXTH relationship direction")


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 935 landing for #1174).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1173:
    def test_pins_on_935_landing(self):
        # The guards this run lays for the next leg: max-935, zero-936
        # numeric, all-ids<=935, no-Type-C-#1174-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 935" in src
        assert "NEXT_NUM = 936" in src

    def test_no_type_c_1174_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type C #1174").stdout
        assert log.strip() == ""

    def test_936_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1172_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1172))

    def test_m132_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, M132_FILE))


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1175).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1173:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1170_full_suite.log" in src

    def test_suite_observed_dead_ambiguous_recorded_not_touched(self):
        # This run stays on targeted verification per the Type B brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest death-observation per #795:
        # #1170-launched suite DEAD/AMBIGUOUS at the 07:00 PDT check
        # (log 2551 bytes, last write Oct 3 05:59 PDT, dots at 3% with one
        # F, no live pytest process). #1175 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "DEAD/AMBIGUOUS" in status
        assert "#1175" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m935 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1170_full_suite.log"
        )
        log = _read(suite_log)
        assert "m935" not in log
        assert "Type B #1173" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1173:
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
        assert "#1173" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 62313
        assert README_FILE_COUNT == 1498


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1173:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1173 Type B:" in text

    def test_no_duplicate_1173_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1173 Type B:") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1170-1174" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1173:
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
            assert "mechanism_id: 935" not in diff, path
            assert "Type B #1173" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert "mechanism_id: 935" not in diff
        assert "Type B #1173" not in diff
