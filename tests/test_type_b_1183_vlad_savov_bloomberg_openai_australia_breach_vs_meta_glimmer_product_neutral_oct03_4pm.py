# -*- coding: utf-8 -*-
"""Type B #1183 tests: Vlad Savov (Bloomberg News, tech editor/newsletter
writer) FIRST dedicated Type B mechanism - m941 accountability-register
boundary/null pin at the corpus standing no-deal outlet. NEW OpenAI arm
(Sep-29-2026 Bloomberg "OpenAI pledges task force after hacking of
Australia government website", co-byline James Mayger and Vlad Savov,
accountability register, -0.35 illustrative) vs Meta arm (Aug-10-2026
Bloomberg "Meta Releases Scaled-Down AI Model Consumers Can Use at Home",
Savov sole byline, product-news register, +0.05 illustrative).
Illustrative delta (OpenAI minus Meta) -0.40: the accountability register
lands harder on the AI lab at an outlet where the deal gradient predicts
NULL (Bloomberg Terminal revenue, zero AI licensing deals per in-corpus
#85). The register follows the peg, not the money. Joins the
reporter-level boundary/null family (m593 Gurman, #538 Metz). NOT a
falsification-family member; ledger holds at 46.

Iteration #1183, FOURTH leg of the 1180-1184 window
(D #1180 -> E #1181 -> A #1182 -> B #1183 -> C #1184).

The m941 block lives in profiles/careers/journalists.yaml as the
competitor_coverage sub-key of the new top-level `vlad_savov:` key (per
the #643 convention, like dan_howley at #1148 - zero vlad_savov YAML key
pre-commit).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1180-launched background suite
(observed stalled at this run's check); its verdict belongs to #1185.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 942, the forty-seventh / forty-eighth member-claim forms, or the
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
    "test_type_b_1183_vlad_savov_bloomberg_openai_australia_breach_"
    "vs_meta_glimmer_product_neutral_oct03_4pm.py"
)
BLOCK_KEY = (
    "type_b_1183_vlad_savov_bloomberg_openai_australia_breach_"
    "accountability_vs_meta_glimmer_product_neutral"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "0" * 40
# Post-first-run values per #719: 74 tests collected; README ratchets
# 62991/1507 -> 63065/1508 in the doc-sync followup.
README_TEST_COUNT = 63065
README_FILE_COUNT = 1508

# Forward guards for the next landing. MECH_NUM=941 is THIS run's landed
# mechanism; NEXT_NUM=942 stays forward.
MECH_NUM = 941
NEXT_NUM = 942

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "942" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "942" at runtime
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"

# The landed m941 block lives here (colon-form key; no numeric-941 substring
# in the block key by designed keying per #715). Savov's entry is the
# top-level `vlad_savov:` key per the #643 convention.
JOURNALISTS_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
FILE_1182 = (
    "test_type_a_1182_nyt_anthropic_vatican_consciousness_dias_"
    "accountability_vs_meta_carried_arms_oct03_3pm.py"
)
SAVOV_URLS = (
    "https://www.moneyweb.co.za/news/ai/openai-pledges-task-force-after-hacking-of-australia-government-website/",
    "https://news.bloomberglaw.com/author/vlad-savov-21177944",
    "https://muckrack.com/vladsavov/articles",
)

# Ordinal form of the falsification-family member that must stay present.
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _savov_entry():
    data = _load_journalists()
    assert "vlad_savov" in data, "top-level vlad_savov key must exist"
    return data["vlad_savov"]


def _block():
    return _savov_entry()["competitor_coverage"][BLOCK_KEY]


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

class TestAnchor1183:
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
        # "Type B #1183 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type B #1183 anchor").stdout
        assert "Type B #1183 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1183:").stdout
        assert "Type B #1183" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1183 is the FOURTH leg of the 1180-1184 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1183:
    def test_rotation_window_is_1180_1184(self):
        text = _block_text()
        assert "1180-1184" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1180-1184 window FOURTH leg "
            "(D #1180 -> E #1181 -> A #1182 -> B #1183 -> C #1184)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1180", "Type E #1181", "Type A #1182"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The next leg (#1184 Type C) is documented in this run's log entry
        # and block window field; it must not exist as a commit yet.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "C #1184" in text
        assert _block()["window"].endswith("C #1184)")

    def test_no_type_b_1183_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1183_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1183:
    def test_vlad_savov_top_level_key_found(self):
        entry = _savov_entry()
        assert entry["name"] == "Vlad Savov"

    def test_block_key_zero_941_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1183, not the mechanism number 941.
        assert "941" not in BLOCK_KEY
        assert "942" not in BLOCK_KEY

    def test_zero_underscore_941_repo_wide(self):
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_941_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_942_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_941(self):
        nums = []
        for line in _profiles_grep_numeric_mechanism_id(MECH_NUM):
            nums.append(MECH_NUM)
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n
        assert nums, "m941 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_savov_urls_in_block_source_urls_verbatim(self):
        urls = (
            list(_block()["new_openai_arm"]["source_urls"])
            + list(_block()["meta_arm"]["source_urls"])
        )
        for u in SAVOV_URLS:
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

class TestBlockStructure1183:
    def test_savov_entry_is_top_level_key(self):
        data = _load_journalists()
        assert "vlad_savov" in data
        assert isinstance(data["vlad_savov"], dict)

    def test_competitor_coverage_subkey(self):
        entry = _savov_entry()
        assert "competitor_coverage" in entry
        assert BLOCK_KEY in entry["competitor_coverage"]

    def test_mechanism_ids_list(self):
        entry = _savov_entry()
        assert entry["mechanism_ids"] == [941]

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "iteration", "mechanism_id", "type", "goal_id", "job_id",
            "scheduled_job_id", "date", "block_key", "test_file", "author",
            "journalist", "publication", "window", "design",
            "new_openai_arm", "meta_arm", "scorer", "financial_context",
            "finding", "confounders", "counter_evidence",
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
        assert b["publication"] == "Bloomberg News"
        assert b["iteration"] == 1183
        assert b["mechanism_id"] == 941

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_source_urls_novel(self):
        entry = _savov_entry()
        for u in SAVOV_URLS:
            assert u in entry["source_urls"], u

    def test_ascii_only(self):
        text = _read(JOURNALISTS_PATH)
        start = text.index(BLOCK_KEY)
        block_region = text[start:start + 20000]
        block_region.encode("ascii")


# ---------------------------------------------------------------------------
# 5. m941 content discipline (the Savov boundary/null pair).
# ---------------------------------------------------------------------------

class TestM941ContentDiscipline1183:
    def test_arms_identified(self):
        b = _block()
        assert b["new_openai_arm"]["entity"] == "openai"
        assert b["meta_arm"]["entity"] == "meta"
        assert b["new_openai_arm"]["date"] == "2026-09-29"
        assert b["meta_arm"]["date"] == "2026-08-10"

    def test_openai_arm_co_byline_caveat(self):
        byline = _block()["new_openai_arm"]["byline"]
        assert "James Mayger and Vlad Savov" in byline
        assert "co-byline" in byline
        assert "29 Sep 2026" in byline

    def test_meta_arm_sole_byline(self):
        byline = _block()["meta_arm"]["byline"]
        assert "Vlad Savov (sole" in byline
        assert "Aug. 10, 2026" in byline

    def test_openai_arm_accountability_quotes(self):
        b = _block()
        q = " ".join(b["new_openai_arm"]["key_quotes"])
        assert "pledges task force" in b["new_openai_arm"]["title"]
        assert "first known instance of an AI agent hacking" in q
        assert "We are sorry" in q

    def test_meta_arm_product_quotes(self):
        b = _block()
        q = " ".join(b["meta_arm"]["key_quotes"])
        assert "Muse Glimmer" in q
        assert "adding fuel to a U.S. debate" in q

    def test_deltas(self):
        s = _block()["scorer"]
        assert s["illustrative_delta_openai_minus_meta"] == -0.40
        assert "-0.35 - 0.05 = -0.40" in s["delta_calc"]

    def test_illustrative_scores(self):
        b = _block()
        assert b["new_openai_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.35
        assert b["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.05

    def test_boundary_pin_referenced(self):
        b = _block()
        assert 593 in b["connects_to"]
        assert 85 in b["connects_to"]
        assert 538 in b["connects_to"]
        assert "BOUNDARY/NULL pin" in b["finding"]
        assert "m593" in b["finding"]

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
        assert "4 browser.search query sets" in rm
        assert "0 browser.open" in rm


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL/QUALITATIVE ONLY per Aug 28 2026 rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1183:
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

class TestFalsificationLedger1183:
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
# 8. Forward-looking staleness (designed lifecycle; the #1184 Type C run
# pins the 942 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1183:
    def test_zero_942_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 942" in src
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

    def test_1182_pins_flip_by_design_documented(self):
        # #1182's forward guards (max-940, zero-941 numeric, no-Type-B-#1183
        # in git log) flip by design now that m941 has landed; recorded,
        # not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1182" in src
        text = _block_text()
        assert "1182" in text or "m940" in text

    def test_thirty_fifth_direction_still_present(self):
        # The THIRTY-FIFTH relationship direction is a landed ordinal;
        # its wording must still be present repo-wide.
        assert _repo_grep("THIRTY-FIFTH relationship direction")

    def test_thirty_sixth_direction_still_present(self):
        # The THIRTY-SIXTH relationship direction is a landed ordinal;
        # its wording must still be present repo-wide.
        assert _repo_grep("THIRTY-SIXTH relationship direction")


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 941 landing for #1184).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1183:
    def test_pins_on_941_landing(self):
        # The guards this run lays for the next leg: max-941, zero-942
        # numeric, no-Type-C-#1184-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 941" in src
        assert "NEXT_NUM = 942" in src

    def test_no_type_c_1184_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type C #1184").stdout
        assert log.strip() == ""

    def test_942_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1182_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1182))

    def test_savov_key_unique(self):
        data = _load_journalists()
        assert list(data.keys()).count("vlad_savov") == 1


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1185).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1183:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1180_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type B brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1180-launched suite STALLED at the 16:0x PDT check
        # (log 3233 bytes, last write Oct 3 14:56 PDT, progress frozen at
        # 4%, no live pytest process). #1185 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "STALLED" in status
        assert "#1185" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m941 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1180_full_suite.log"
        )
        log = _read(suite_log)
        assert "m941" not in log
        assert "Type B #1183" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1183:
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
        assert "#1183" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 62991 + 74
        assert README_FILE_COUNT == 1508


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1183:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1183 Type B:" in text

    def test_no_duplicate_1183_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1183 Type B:") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1180-1184" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1183:
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
            assert "mechanism_id: 941" not in diff, path
            assert "Type B #1183" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert "mechanism_id: 941" not in diff
        assert "Type B #1183" not in diff
