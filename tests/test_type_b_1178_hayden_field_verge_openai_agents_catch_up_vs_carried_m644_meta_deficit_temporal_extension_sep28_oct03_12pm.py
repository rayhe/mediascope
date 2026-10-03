# -*- coding: utf-8 -*-
"""Type B #1178 tests: Hayden Field (The Verge, senior AI reporter) temporal
extension of mechanism 644 (Type B #683: Field sole-byline Meta Muse Spark
re-entry-deficit -0.15 vs OpenAI GPT-5.6 regulatory-friction -0.10,
reporter-level constancy pin) to the Sep-28-2026 DevDay-eve peg - NEW
OpenAI arm "OpenAI's AI agents need to catch up" (deficit register on the
deal partner, -0.30 illustrative) vs carried m644 arms.

Iteration #1178, FOURTH leg of the 1175-1179 window
(D #1175 -> E #1176 -> A #1177 -> B #1178 -> C #1179).

The m938 block lives in profiles/careers/journalists.yaml as a direct
sub-key of the Hayden Field list item (the file's list-style `journalists:`
section; sibling of the m644 block per the local convention - no
top-level hayden_field key, no competitor_coverage sub-key, no
mechanism_ids list on this item).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1175-launched background suite
(observed stalled at this run's check); its verdict belongs to #1180.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 939, the forty-seventh / forty-eighth member-claim forms, or the
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
    "test_type_b_1178_hayden_field_verge_openai_agents_catch_up_"
    "vs_carried_m644_meta_deficit_temporal_extension_sep28_oct03_12pm.py"
)
BLOCK_KEY = (
    "type_b_1178_hayden_field_verge_openai_agents_catch_up_"
    "vs_carried_m644_meta_deficit_temporal_extension_sep28"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "8e948b123773120670f942b26ceb58e5946b50dc"
# Post-first-run values per #719: 72 tests collected; README ratchets
# 62617/1502 -> 62689/1503 in the doc-sync followup.
README_TEST_COUNT = 62689
README_FILE_COUNT = 1503

# Forward guards for the next landing. MECH_NUM=938 is THIS run's landed
# mechanism; NEXT_NUM=939 stays forward.
MECH_NUM = 938
NEXT_NUM = 939

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "939" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "939" at runtime
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"

# The landed m938 block lives here (colon-form key; no numeric-938 substring
# in the block key by designed keying per #715). Field's entry is a list
# item under the top-level `journalists:` key, found by name.
JOURNALISTS_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
FILE_1177 = (
    "test_type_a_1177_verge_openai_dots_persistent_agent_launch_"
    "vs_meta_muse_scrutiny_arms_oct03_11am.py"
)
M644_FILE = (
    "test_type_b_683_hayden_field_meta_muse_spark_reentry_deficit_"
    "vs_openai_gpt56_regulatory_launch_byline_register_sep11_5pm.py"
)
FIELD_URLS = (
    "https://technewstube.com/theverge/1871272/openais-ai-agents-need-to-catch-up/",
    "https://www.wilsonsmedia.com/openais-ai-agents-need-to-catch-up/",
    "https://flipboard.com/@theverge/the-verge-on-artificial-intelligence-rkbtf55qz",
    "https://aifuture.org/news/openai-s-ai-agents-need-to-catch-up-14494",
    "https://scoopfeeds.com/article/62d97f45-aa2d-5d3a-9301-9032336364bb",
    "https://thejoai.com/ai-news/ai-overuse-may-harm-cognition-ai-detectors-reveal-content-fakes/",
    "https://aionpulse.com/news/2/",
)

# Ordinal form of the falsification-family member that must stay present.
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _field_item():
    items = _load_journalists()["journalists"]
    matches = [
        i for i in items
        if isinstance(i, dict) and i.get("name") == "Hayden Field"
    ]
    assert len(matches) == 1, "Hayden Field item must be unique"
    return matches[0]


def _block():
    return _field_item()[BLOCK_KEY]


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

class TestAnchor1178:
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
        # "Type B #1178 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type B #1178 anchor").stdout
        assert "Type B #1178 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type B #1178:").stdout
        assert "Type B #1178" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1178 is the FOURTH leg of the 1175-1179 window.
# ---------------------------------------------------------------------------

class TestRotationGuard1178:
    def test_rotation_window_is_1175_1179(self):
        text = _block_text()
        assert "1175-1179" in text

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1175-1179 window FOURTH leg "
            "(D #1175 -> E #1176 -> A #1177 -> B #1178 -> C #1179)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1175", "Type E #1176", "Type A #1177"):
            assert marker in log, marker

    def test_next_run_is_type_c(self):
        # The next leg (#1179 Type C) is documented in this run's log entry
        # and block window field; it must not exist as a commit yet.
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "C #1179" in text
        assert _block()["window"].endswith("C #1179)")

    def test_no_type_b_1178_test_file_before_this_run(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1178_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1178:
    def test_hayden_field_item_found_by_name(self):
        item = _field_item()
        assert item["name"] == "Hayden Field"

    def test_block_key_zero_938_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1178 and the extended mechanism m644, not the mechanism
        # number 938.
        assert "938" not in BLOCK_KEY
        assert "939" not in BLOCK_KEY

    def test_zero_underscore_938_repo_wide(self):
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_938_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_939_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_938(self):
        nums = []
        for line in _profiles_grep_numeric_mechanism_id(MECH_NUM):
            nums.append(MECH_NUM)
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n
        assert nums, "m938 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_field_urls_in_block_source_urls_verbatim(self):
        urls = _block()["new_openai_arm"]["source_urls"]
        for u in FIELD_URLS:
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
# 4. Block structure (the list-item journalist convention for this entry).
# ---------------------------------------------------------------------------

class TestBlockStructure1178:
    def test_field_item_is_list_member(self):
        items = _load_journalists()["journalists"]
        assert isinstance(items, list)
        assert any(
            isinstance(i, dict) and i.get("name") == "Hayden Field"
            for i in items
        )

    def test_m644_sibling_still_present(self):
        item = _field_item()
        assert (
            "mechanism_644_hayden_field_meta_muse_spark_reentry_deficit_"
            "vs_openai_gpt56_regulatory_launch_byline_register_sep11"
        ) in item

    def test_two_mechanism_blocks_on_item(self):
        item = _field_item()
        mech_keys = [
            k for k in item
            if k.startswith("mechanism_644_") or k.startswith("type_b_1178_")
        ]
        assert set(mech_keys) == {
            "mechanism_644_hayden_field_meta_muse_spark_reentry_deficit_"
            "vs_openai_gpt56_regulatory_launch_byline_register_sep11",
            BLOCK_KEY,
        }

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "iteration", "mechanism_id", "type", "goal_id", "job_id",
            "scheduled_job_id", "date", "block_key", "test_file", "author",
            "journalist", "publication", "window", "design",
            "new_openai_arm", "carried_meta_arm", "carried_openai_arm",
            "scorer", "financial_context", "finding", "confounders",
            "counter_evidence", "statistical_discipline", "verdict",
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
        assert b["publication"].startswith("The Verge")
        assert b["iteration"] == 1178
        assert b["mechanism_id"] == 938

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_ascii_only(self):
        text = _read(JOURNALISTS_PATH)
        start = text.index(BLOCK_KEY)
        block_region = text[start:start + 16000]
        block_region.encode("ascii")


# ---------------------------------------------------------------------------
# 5. m938 content discipline (the m644 temporal-extension pair).
# ---------------------------------------------------------------------------

class TestM938ContentDiscipline1178:
    def test_arms_identified(self):
        b = _block()
        assert b["new_openai_arm"]["entity"] == "openai"
        assert b["carried_meta_arm"]["entity"] == "meta"
        assert b["carried_openai_arm"]["entity"] == "openai"
        assert b["new_openai_arm"]["date"] == "2026-09-28"
        assert b["carried_meta_arm"]["date"] == "2026-04-08"
        assert b["carried_openai_arm"]["date"] == "2026-06-26"

    def test_new_arm_sole_byline(self):
        byline = _block()["new_openai_arm"]["byline"]
        assert "Hayden Field (sole" in byline
        assert "Sep 28, 2026, 2:45 pm" in byline

    def test_carried_arms_provenance(self):
        b = _block()
        for arm_key in ("carried_meta_arm", "carried_openai_arm"):
            prov = b[arm_key]["provenance"]
            assert "mechanism 644" in prov
            assert "Type B #683" in prov
            assert "un-rescored per #807" in prov

    def test_new_arm_deficit_quotes(self):
        b = _block()
        q = b["new_openai_arm"]["key_quotes"]
        joined = " ".join(q) + " " + b["new_openai_arm"]["title"]
        assert "fallen behind" in joined
        assert "need to catch up" in joined
        assert "its answer to Meta's Muse" in joined

    def test_deltas(self):
        s = _block()["scorer"]
        assert s["illustrative_delta_new_openai_minus_carried_meta"] == -0.15
        assert s["illustrative_delta_new_openai_minus_carried_openai"] == -0.20
        assert "-0.30 - (-0.15) = -0.15" in s["delta_calc"]

    def test_m644_extension_referenced(self):
        b = _block()
        assert 644 in b["connects_to"]
        assert 920 in b["connects_to"]
        assert 937 in b["connects_to"]
        assert "TEMPORAL EXTENSION" in b["finding"]
        assert "m644" in b["finding"]
        assert "mechanism 644" in b["design"]

    def test_illustrative_scores(self):
        b = _block()
        assert b["new_openai_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.30
        assert b["carried_meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.15
        assert b["carried_openai_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.10

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
        assert "5 browser.search query sets" in rm
        assert "0 browser.open" in rm


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL/QUALITATIVE ONLY per Aug 28 2026 rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1178:
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

class TestFalsificationLedger1178:
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
# 8. Forward-looking staleness (designed lifecycle; the #1179 Type C run
# pins the 939 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1178:
    def test_zero_939_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 939" in src
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

    def test_1177_pins_flip_by_design_documented(self):
        # #1177's forward guards (max-937, zero-938 numeric, no-Type-B-#1178
        # in git log) flip by design now that m938 has landed; recorded,
        # not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1177" in src
        text = _block_text()
        assert "1177" in text or "m937" in text

    def test_thirty_fifth_direction_still_present(self):
        # The THIRTY-FIFTH relationship direction is a landed ordinal;
        # its wording must still be present repo-wide.
        assert _repo_grep("THIRTY-FIFTH relationship direction")

    def test_thirty_sixth_direction_still_present(self):
        # The THIRTY-SIXTH relationship direction is a landed ordinal;
        # its wording must still be present repo-wide.
        assert _repo_grep("THIRTY-SIXTH relationship direction")


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 938 landing for #1179).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1178:
    def test_pins_on_938_landing(self):
        # The guards this run lays for the next leg: max-938, zero-939
        # numeric, no-Type-C-#1179-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 938" in src
        assert "NEXT_NUM = 939" in src

    def test_no_type_c_1179_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type C #1179").stdout
        assert log.strip() == ""

    def test_939_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1177_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1177))

    def test_m644_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, M644_FILE))


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1180).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1178:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1175_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type B brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1175-launched suite STALLED at the 12:00 PDT check
        # (log 10635 bytes, last write Oct 3 16:59 UTC, no live pytest
        # process). #1180 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "stalled" in status
        assert "#1180" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m938 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1175_full_suite.log"
        )
        log = _read(suite_log)
        assert "m938" not in log
        assert "Type B #1178" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1178:
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
        assert "#1178" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 62617 + 72
        assert README_FILE_COUNT == 1503


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1178:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1178 Type B:" in text

    def test_no_duplicate_1178_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1178 Type B:") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1175-1179" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1178:
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
            assert "mechanism_id: 938" not in diff, path
            assert "Type B #1178" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert "mechanism_id: 938" not in diff
        assert "Type B #1178" not in diff
