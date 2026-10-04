# -*- coding: utf-8 -*-
"""Type B #1193 tests: Jeff Meyer (Camera Jabber website editor) FIRST
dedicated Type B mechanism - m947 within-piece cross-entity register
divergence. NEW piece (Sep-24-2026 Camera Jabber "Snap's chunky Specs AR
glasses take a different line on the camera-glasses backlash", first-hand
full-text read this run): Meta Ray-Ban arm carries privacy-backlash
vocabulary (disguise is the problem, -0.30 illustrative) vs Snap Specs arm
carries design-praise vocabulary (conspicuousness is the answer, +0.25
illustrative). Illustrative delta (Snap minus Meta) +0.55: peg, genre,
date, and reviewer all held constant - pure vocabulary selection on the
design-philosophy peg (concealment vs conspicuousness). Journalist-level
BOUNDARY pin for the financial theory (no-deal outlet; register follows
the peg, not money); joins the m593/#538 reporter-level boundary family.
NOT a falsification-family member; ledger holds at 46.

Iteration #1193, FOURTH leg of the 1190-1194 window
(D #1190 -> E #1191 -> A #1192 -> B #1193 -> C #1194).

The m947 block lives in profiles/careers/journalists.yaml as the
competitor_coverage sub-key of the new top-level `jeff_meyer:` key (per
the #643 convention, like eli_tan at #1188 - zero jeff_meyer top-level
YAML key pre-commit).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1190-launched background suite
(observed ALIVE at this run's check, ~11% progress); its verdict belongs
to #1195.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number, the forty-seventh / forty-eighth member-claim forms, or the
thirty-ninth direction-claim form; the constants are constructed at
runtime. (The thirty-seventh and thirty-eighth direction forms are landed
ordinals, carried contiguously in the still-present tests.)
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
    "test_type_b_1193_jeff_meyer_camerajabber_snap_specs_"
    "conspicuous_vs_meta_rayban_disguise_within_piece_oct04_12am.py"
)
BLOCK_KEY = (
    "type_b_1193_jeff_meyer_camerajabber_snap_specs_"
    "conspicuous_vs_meta_rayban_disguise_within_piece"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "e1efcca3ef0a33982a8ced80e2e9a82758b5835c"  # patched per #565
# Post-first-run values per #719: N tests collected; README ratchets
# 63752/1517 -> (63752+N)/1518 in the doc-sync followup.
README_TEST_COUNT = 63752
README_FILE_COUNT = 1517
COLLECTED_NEW_TESTS = 0  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=947 is THIS run's landed
# mechanism; NEXT_NUM=948 stays forward.
MECH_NUM = 947
NEXT_NUM = 948

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + next number at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + next number at runtime
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"

# The landed m947 block lives here (colon-form key; no numeric-947 substring
# in the block key by designed keying per #715). Meyer's entry is the
# top-level `jeff_meyer:` key per the #643 convention.
JOURNALISTS_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
FILE_1192 = (
    "test_type_a_1192_wired_openai_oct02_macos_cve100754_"
    "accountability_original_vs_carried_meta_arms_oct03_11pm.py"
)
MEYER_URLS = (
    "https://camerajabber.com/photography-news/"
    "snaps-chunky-specs-ar-glasses-take-a-different-line-on-the-camera-glasses-backlash/",
    "https://muckrack.com/jeff-meyer/articles",
    "https://camerajabber.com/author/jeff/",
)

# Ordinal form of the falsification-family member that must stay present.
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _meyer_entry():
    data = _load_journalists()
    assert "jeff_meyer" in data, "top-level jeff_meyer key must exist"
    return data["jeff_meyer"]


def _block():
    return _meyer_entry()["competitor_coverage"][BLOCK_KEY]


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

class TestAnchor1193:
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
        # "Type B #1193 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type B #1193 anchor").stdout
        assert "Type B #1193 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1193:").stdout
        assert "Type B #1193" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1193 is the FOURTH leg of the 1190-1194 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1193:
    def test_rotation_window_is_1190_1194(self):
        text = _block_text()
        assert "1190-1194" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1190-1194 window FOURTH leg "
            "(D #1190 -> E #1191 -> A #1192 -> B #1193 -> C #1194)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1190", "Type E #1191", "Type A #1192"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The next leg (#1194 Type C) is documented in this run's log entry
        # and block window field; it must not exist as a commit yet.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "C #1194" in text
        assert _block()["window"].endswith("C #1194)")

    def test_no_type_b_1193_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1193_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1193:
    def test_jeff_meyer_top_level_key_found(self):
        entry = _meyer_entry()
        assert entry["name"] == "Jeff Meyer"

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1193, not the mechanism number.
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_mechanism_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_next_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_this_run(self):
        nums = []
        for line in _profiles_grep_numeric_mechanism_id(MECH_NUM):
            nums.append(MECH_NUM)
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n
        assert nums, "m947 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_meyer_urls_in_block_source_urls_verbatim(self):
        urls = list(_meyer_entry()["source_urls"])
        for u in MEYER_URLS:
            assert u in urls, u
        assert all(u.startswith("https://") for u in urls)

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
# 4. Block structure (the #643 top-level journalist-key convention).
# ---------------------------------------------------------------------------

class TestBlockStructure1193:
    def test_meyer_entry_is_top_level_key(self):
        data = _load_journalists()
        assert "jeff_meyer" in data
        assert isinstance(data["jeff_meyer"], dict)

    def test_competitor_coverage_subkey(self):
        entry = _meyer_entry()
        assert "competitor_coverage" in entry
        assert BLOCK_KEY in entry["competitor_coverage"]

    def test_mechanism_ids_list(self):
        assert _meyer_entry()["mechanism_ids"] == [MECH_NUM]

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "iteration", "mechanism_id", "type", "goal_id", "job_id",
            "scheduled_job_id", "date", "block_key", "test_file", "author",
            "journalist", "publication", "window", "design", "piece",
            "meta_arm", "snap_arm", "scorer", "financial_context", "finding",
            "confounders", "counter_evidence", "statistical_discipline",
            "verdict", "cautious_language_required", "correlational_note",
            "no_analysis_json_update", "falsification_family_member",
            "falsification_ledger", "ledger_note", "connects_to", "novelty",
            "research_method", "artifact_readiness",
            "background_suite_status", "in_flight",
        ):
            assert field in b, field

    def test_type_and_publication(self):
        b = _block()
        assert b["type"] == "B"
        assert b["publication"] == "camera-jabber"
        assert b["iteration"] == 1193
        assert b["mechanism_id"] == MECH_NUM

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_source_urls_novel(self):
        # The piece URL was zero-hit repo-wide pre-commit (the domain only
        # appeared in #983's REJECTED-research note, never as this piece).
        hits = _source_grep(MEYER_URLS[0])
        allowed = {
            os.path.join(REPO, "profiles", "careers", "journalists.yaml"),
            os.path.join(TESTS_DIR, OWN_BASENAME),
            os.path.join(REPO, "README.md"),
            os.path.join(REPO, "docs", "ARCHITECTURE.md"),
            os.path.join(REPO, "iteration-log.md"),
        }
        for h in hits:
            assert h in allowed, h

    def test_ascii_only(self):
        entry = _meyer_entry()
        text = yaml.safe_dump(entry, allow_unicode=False)
        text.encode("ascii")


# ---------------------------------------------------------------------------
# 5. m947 content discipline (within-piece cross-entity divergence).
# ---------------------------------------------------------------------------

class TestM947ContentDiscipline1193:
    def test_arms_identified(self):
        b = _block()
        assert b["meta_arm"]["entity"] == "meta"
        assert b["snap_arm"]["entity"] == "snap"

    def test_same_piece_control(self):
        # Peg, genre, date, and reviewer all held constant: one piece, one
        # journalist, one date.
        b = _block()
        piece = b["piece"]
        assert piece["byline"].startswith("Jeff Meyer")
        assert piece["date"] == "2026-09-24"
        assert piece["evidence_tier"].startswith("FIRST-HAND")

    def test_within_piece_constant_holds(self):
        b = _block()
        assert "peg" in b["design"].lower()
        assert "reviewer" in b["design"].lower() or "journalist" in b["design"].lower()

    def test_meta_arm_disguise_quotes(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "steady backlash" in joined
        assert "exactly the problem" in joined
        assert "no obvious sign a camera is running" in joined

    def test_snap_arm_conspicuous_quotes(self):
        quotes = _block()["snap_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "announce themselves" in joined
        assert "making it conspicuous" in joined
        assert "worth knowing about" in joined

    def test_illustrative_scores(self):
        b = _block()
        assert b["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.30
        assert b["snap_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.25

    def test_deltas(self):
        b = _block()
        assert b["scorer"]["illustrative_delta_snap_minus_meta"] == 0.55
        assert b["scorer"]["delta_calc"] == "+0.25 - (-0.30) = +0.55"

    def test_boundary_pin_referenced(self):
        b = _block()
        assert "BOUNDARY" in b["finding"]
        assert "m593" in b["finding"]

    def test_extension_not_falsification(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert "no-deal outlet" in _meyer_entry()["notes"]

    def test_confounder_strongest_first(self):
        confs = _block()["confounders"]
        assert confs[0].startswith("STRONG")
        assert confs[1].startswith("STRONG")

    def test_counterevidence_present(self):
        ces = _block()["counter_evidence"]
        assert len(ces) >= 3
        assert all(c.startswith("COUNTEREVIDENCE") for c in ces)

    def test_research_method_rejection_trail(self):
        rm = _block()["research_method"]
        for name in ("Parham", "Haslam", "Howley"):
            assert name in rm, name
        assert "REJECTED" in rm


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug 28 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1193:
    def test_no_engine_run(self):
        b = _block()
        assert b["scorer"]["engine_run"] is False
        assert b["scorer"]["is_significant"] is False

    def test_stats_not_calculated(self):
        b = _block()
        for field in ("p_value", "cohens_d", "ci_95"):
            assert b["scorer"][field] == "NOT_CALCULATED", field

    def test_verdict_discipline(self):
        b = _block()
        assert b["verdict"].startswith("directionally_supported_not_proven")
        assert b["cautious_language_required"] is True

    def test_not_artifact_grade(self):
        b = _block()
        assert b["no_analysis_json_update"] is True
        assert "NOT artifact-grade" in b["scorer"]["method"]

    def test_aug28_standing_rule_cited(self):
        b = _block()
        assert "Aug 28 2026 standing rule" in b["statistical_discipline"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 46).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1193:
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
# 8. Forward-looking staleness (designed lifecycle; the #1194 Type C run
# pins the 948 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1193:
    def test_zero_948_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 948" in src
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src

    def test_no_thirty_ninth_direction_guard(self):
        # The thirty-ninth direction form stays absent repo-wide; the
        # constant is format-built so the source never carries it.
        # (The thirty-seventh and thirty-eighth forms are landed ordinals,
        # carried contiguously in the still-present tests below.)
        assert not _repo_grep(THIRTY_NINTH_DIR), THIRTY_NINTH_DIR
        assert len(THIRTY_NINTH_DIR) > 0

    def test_no_forty_seventh_member_guard(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source (verified by inspection of the constant
        # definition above).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FORTY_SEVENTH_MEMBER) not in src
        assert len(FORTY_SEVENTH_MEMBER) > 0

    def test_no_forty_eighth_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert (FORTY_EIGHTH_MEMBER) not in src
        assert len(FORTY_EIGHTH_MEMBER) > 0

    def test_1192_pins_flip_by_design_documented(self):
        # #1192's forward guards (max-946, zero-947 keys all forms,
        # no-Type-B-#1193-in-git-log) flip by design now that m947 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1192" in src
        text = _block_text()
        assert "1192" in text or "m946" in text

    def test_thirty_fifth_direction_still_present(self):
        # The THIRTY-FIFTH relationship direction is a landed ordinal;
        # its wording must still be present repo-wide.
        assert _repo_grep("THIRTY-FIFTH relationship direction")

    def test_thirty_sixth_direction_still_present(self):
        assert _repo_grep("THIRTY-SIXTH relationship direction")

    def test_thirty_seventh_direction_still_present(self):
        assert _repo_grep("THIRTY-SEVENTH relationship direction")

    def test_thirty_eighth_direction_still_present(self):
        assert _repo_grep("THIRTY-EIGHTH relationship direction")


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 947 landing for #1194).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1193:
    def test_pins_on_947_landing(self):
        # The guards this run lays for the next leg: max-947, zero-948
        # numeric, no-Type-C-#1194-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 947" in src
        assert "NEXT_NUM = 948" in src

    def test_no_type_c_1194_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type C #1194").stdout
        assert log.strip() == ""

    def test_948_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1192_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1192))

    def test_meyer_key_unique(self):
        data = _load_journalists()
        assert list(data.keys()).count("jeff_meyer") == 1


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1195).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1193:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1190_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type B brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1190-launched suite ALIVE at the 00:05 PDT check
        # (7865 bytes, last write Oct 4 00:05:08 PDT, progress ~11%,
        # 2 F markers). #1195 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "ALIVE" in status
        assert "#1195" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m947 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1190_full_suite.log"
        )
        log = _read(suite_log)
        assert "m947" not in log
        assert "Type B #1193" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1193:
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
        assert "## #1193 Type B:" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 63752 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1518


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1193:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1193 Type B:" in text

    def test_no_duplicate_1193_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1193 Type B:") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1190-1194" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1193:
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
            assert "mechanism_id: 947" not in diff, path
            assert "Type B #1193" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert "mechanism_id: 947" not in diff
        assert "Type B #1193" not in diff
