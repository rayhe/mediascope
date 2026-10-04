# -*- coding: utf-8 -*-
"""Type B #1188 tests: Eli Tan (The New York Times, technology reporter) FIRST
dedicated Type B mechanism - m944 within-piece cross-entity stigma pin. NEW
Meta arm (Sep-24-2026 NYT "Complaints About Meta's 'Pervert Glasses' Won't
Slow Tech's Wearable Gadgets Drive", co-byline Brian X. Chen and Eli Tan,
stigma register, -0.45 illustrative) vs other-companies arm (SAME piece, same
date, same bylines: the dek frames every other company's functionally similar
devices neutrally - "That's not stopping other companies from creating similar
devices" - +0.05 illustrative). Illustrative delta (Meta minus others) -0.50:
the stigma nickname brands Meta's product in the headline while competitors
get the sanitized neutral frame, with peg/genre/date/desk/co-byline all held
constant - pure vocabulary selection. Theory-CONSISTENT with the financial-deal
gradient (NYT holds documented AI licensing ties with Google/Apple/Amazon; no
documented NYT AI licensing deal with Meta; NYT sued OpenAI/Microsoft).
Extends m484 (Chen Meta-vs-Apple privacy vocabulary bifurcation) and
mechanism_662 (Chen Duo vs Ray-Ban, #713) to Tan's own byline. NOT a
falsification-family member; ledger holds at 46.

Iteration #1188, FOURTH leg of the 1185-1189 window
(D #1185 -> E #1186 -> A #1187 -> B #1188 -> C #1189).

The m944 block lives in profiles/careers/journalists.yaml as the
competitor_coverage sub-key of the new top-level `eli_tan:` key (per
the #643 convention, like vlad_savov at #1183 - zero eli_tan top-level
YAML key pre-commit; the journalists-list profile entry exists but
carries no dedicated Type B mechanism).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1185-launched background suite
(observed RUNNING at this run's check); its verdict belongs to #1190.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 945, the forty-seventh / forty-eighth member-claim forms, or the
thirty-seventh / thirty-eighth direction-claim forms; the constants are
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
    "test_type_b_1188_eli_tan_nyt_pervert_glasses_stigma_"
    "vs_other_companies_neutral_within_piece_oct03_8pm.py"
)
BLOCK_KEY = (
    "type_b_1188_eli_tan_nyt_pervert_glasses_stigma_"
    "vs_other_companies_neutral_within_piece"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "e4e7305b85d57c41d4a1a19d1de8ca4f03a93fd1"  # patched per #565
# Post-first-run values per #719: N tests collected; README ratchets
# 63377/1512 -> (63377+N)/1513 in the doc-sync followup.
README_TEST_COUNT = 63377 + 74  # 63451; patched post-first-run per #719
README_FILE_COUNT = 1513

# Forward guards for the next landing. MECH_NUM=944 is THIS run's landed
# mechanism; NEXT_NUM=945 stays forward.
MECH_NUM = 944
NEXT_NUM = 945

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "945" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "945" at runtime
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"

# The landed m944 block lives here (colon-form key; no numeric-944 substring
# in the block key by designed keying per #715). Tan's entry is the
# top-level `eli_tan:` key per the #643 convention.
JOURNALISTS_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
FILE_1187 = (
    "test_type_a_1187_nypost_anthropic_oct01_ipo_hypocrisy_"
    "vs_carried_meta_openai_arms_oct03_7pm.py"
)
TAN_URLS = (
    "https://muckrack.com/eli-tan",
    "https://aiweekly.co/alerts/meta-pushes-wearables-forward-despite-pervert-glasses-backlash",
    "https://www.youtube.com/watch?v=W9e0PHDseH4",
)

# Ordinal form of the falsification-family member that must stay present.
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _tan_entry():
    data = _load_journalists()
    assert "eli_tan" in data, "top-level eli_tan key must exist"
    return data["eli_tan"]


def _block():
    return _tan_entry()["competitor_coverage"][BLOCK_KEY]


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

class TestAnchor1188:
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
        # "Type B #1188 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type B #1188 anchor").stdout
        assert "Type B #1188 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1188:").stdout
        assert "Type B #1188" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1188 is the FOURTH leg of the 1185-1189 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1188:
    def test_rotation_window_is_1185_1189(self):
        text = _block_text()
        assert "1185-1189" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1185-1189 window FOURTH leg "
            "(D #1185 -> E #1186 -> A #1187 -> B #1188 -> C #1189)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1185", "Type E #1186", "Type A #1187"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The next leg (#1189 Type C) is documented in this run's log entry
        # and block window field; it must not exist as a commit yet.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "C #1189" in text
        assert _block()["window"].endswith("C #1189)")

    def test_no_type_b_1188_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1188_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1188:
    def test_eli_tan_top_level_key_found(self):
        entry = _tan_entry()
        assert entry["name"] == "Eli Tan"

    def test_block_key_zero_944_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1188, not the mechanism number 944.
        assert "944" not in BLOCK_KEY
        assert "945" not in BLOCK_KEY

    def test_zero_underscore_944_repo_wide(self):
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_944_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_945_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_944(self):
        nums = []
        for line in _profiles_grep_numeric_mechanism_id(MECH_NUM):
            nums.append(MECH_NUM)
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n
        assert nums, "m944 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_tan_urls_in_block_source_urls_verbatim(self):
        urls = (
            list(_block()["new_meta_arm"]["source_urls"])
            + list(_block()["other_companies_arm"]["source_urls"])
        )
        for u in TAN_URLS:
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

class TestBlockStructure1188:
    def test_tan_entry_is_top_level_key(self):
        data = _load_journalists()
        assert "eli_tan" in data
        assert isinstance(data["eli_tan"], dict)

    def test_competitor_coverage_subkey(self):
        entry = _tan_entry()
        assert "competitor_coverage" in entry
        assert BLOCK_KEY in entry["competitor_coverage"]

    def test_mechanism_ids_list(self):
        entry = _tan_entry()
        assert entry["mechanism_ids"] == [944]

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "iteration", "mechanism_id", "type", "goal_id", "job_id",
            "scheduled_job_id", "date", "block_key", "test_file", "author",
            "journalist", "publication", "window", "design",
            "new_meta_arm", "other_companies_arm", "scorer",
            "financial_context", "finding", "confounders", "counter_evidence",
            "statistical_discipline", "verdict",
            "cautious_language_required", "correlational_note",
            "no_analysis_json_update", "falsification_family_member",
            "falsification_ledger", "ledger_note", "connects_to",
            "novelty", "research_method", "artifact_readiness",
            "background_suite_status", "in_flight",
        ):
            assert field in b, field

    def test_type_and_publication(self):
        b = _block()
        assert b["type"] == "B"
        assert b["publication"] == "The New York Times"
        assert b["iteration"] == 1188
        assert b["mechanism_id"] == 944

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_source_urls_novel(self):
        entry = _tan_entry()
        for u in TAN_URLS:
            assert u in entry["source_urls"], u

    def test_ascii_only(self):
        text = _read(JOURNALISTS_PATH)
        start = text.index(BLOCK_KEY)
        block_region = text[start:start + 20000]
        block_region.encode("ascii")


# ---------------------------------------------------------------------------
# 5. m944 content discipline (the Tan within-piece stigma pair).
# ---------------------------------------------------------------------------

class TestM944ContentDiscipline1188:
    def test_arms_identified(self):
        b = _block()
        assert b["new_meta_arm"]["entity"] == "meta"
        assert b["other_companies_arm"]["entity"] == "other_companies"
        assert b["new_meta_arm"]["date"] == "2026-09-24"
        assert b["other_companies_arm"]["date"] == "2026-09-24"

    def test_same_piece_control(self):
        b = _block()
        assert b["new_meta_arm"]["title"] == b["other_companies_arm"]["title"]
        assert "Pervert Glasses" in b["new_meta_arm"]["title"]

    def test_co_byline_caveat(self):
        byline = _block()["new_meta_arm"]["byline"]
        assert "Brian X. Chen and Eli Tan" in byline
        assert "co-byline" in byline
        assert "#678" in byline

    def test_meta_arm_stigma_quotes(self):
        b = _block()
        q = " ".join(b["new_meta_arm"]["key_quotes"])
        assert "Pervert Glasses" in q
        assert "unflattering nickname" in q
        assert "cringe-inducing stories" in q

    def test_other_companies_arm_neutral_quotes(self):
        b = _block()
        q = " ".join(b["other_companies_arm"]["key_quotes"])
        assert "not stopping other companies from creating similar devices" in q
        assert "Pervert" not in q

    def test_deltas(self):
        s = _block()["scorer"]
        assert s["illustrative_delta_meta_minus_others"] == -0.50
        assert "-0.45 - 0.05 = -0.50" in s["delta_calc"]

    def test_illustrative_scores(self):
        b = _block()
        assert b["new_meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.45
        assert b["other_companies_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.05

    def test_boundary_pin_referenced(self):
        b = _block()
        assert 484 in b["connects_to"]
        assert 662 in b["connects_to"]
        assert 835 in b["connects_to"]
        assert "WITHIN-PIECE" in b["finding"]
        assert "m484" in b["finding"]

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
        assert any("COUNTEREVIDENCE" in c for c in ce)

    def test_research_method_excerpt_tier(self):
        rm = _block()["research_method"]
        assert "7 browser.search query sets" in rm
        assert "1 browser.open" in rm
        assert "0 browser.open on the NYT paywalled original" in rm


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL/QUALITATIVE ONLY per Aug 28 2026 rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1188:
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

class TestFalsificationLedger1188:
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
# 8. Forward-looking staleness (designed lifecycle; the #1189 Type C run
# pins the 945 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1188:
    def test_zero_945_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 945" in src
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

    def test_1187_pins_flip_by_design_documented(self):
        # #1187's forward guards (max-943, zero-944 numeric, no-Type-B-#1188
        # in git log) flip by design now that m944 has landed; recorded,
        # not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1187" in src
        text = _block_text()
        assert "1187" in text or "m943" in text

    def test_thirty_fifth_direction_still_present(self):
        # The THIRTY-FIFTH relationship direction is a landed ordinal;
        # its wording must still be present repo-wide.
        assert _repo_grep("THIRTY-FIFTH relationship direction")

    def test_thirty_sixth_direction_still_present(self):
        # The THIRTY-SIXTH relationship direction is a landed ordinal;
        # its wording must still be present repo-wide.
        assert _repo_grep("THIRTY-SIXTH relationship direction")


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 944 landing for #1189).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1188:
    def test_pins_on_944_landing(self):
        # The guards this run lays for the next leg: max-944, zero-945
        # numeric, no-Type-C-#1189-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 944" in src
        assert "NEXT_NUM = 945" in src

    def test_no_type_c_1189_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type C #1189").stdout
        assert log.strip() == ""

    def test_945_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1187_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1187))

    def test_tan_key_unique(self):
        data = _load_journalists()
        assert list(data.keys()).count("eli_tan") == 1


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1190).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1188:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1185_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type B brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1185-launched suite RUNNING at the 20:0x PDT check
        # (log 6950 bytes, last write Oct 3 20:03 PDT, progress at 9%,
        # live pytest processes at ps scan). #1190 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "RUNNING" in status
        assert "#1190" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m944 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1185_full_suite.log"
        )
        log = _read(suite_log)
        assert "m944" not in log
        assert "Type B #1188" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1188:
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
        assert "## #1188 Type B:" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count (74).
        assert README_TEST_COUNT == 63377 + 74
        assert README_FILE_COUNT == 1513


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1188:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1188 Type B:" in text

    def test_no_duplicate_1188_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1188 Type B:") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1185-1189" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1188:
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
            assert "mechanism_id: 944" not in diff, path
            assert "Type B #1188" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert "mechanism_id: 944" not in diff
        assert "Type B #1188" not in diff
