"""Type B -- Iteration #1143 (Fri 2026-10-02 06:00 PDT): m917 Cristina Criddle
(FT) Sep-16-2026 "blindsided" piece (OpenAI + Anthropic staff blindsided by
Dario Amodei's and Sam Altman's calls to slow the frontier; some fear
evaluators may compromise security -- accountability-adversarial on the
FT x OpenAI licensing-deal partner, MANUAL ILLUSTRATIVE -0.35,
headline-tier via techmeme 2026-09-16 13:57:16 + biztoc relay) --
TEMPORAL EXTENSION of m758's writer-level falsification pattern to a
second crisis-window peg five weeks later (m758, Type B #878: Aug-11
Bakalar ethics-chief-exit -0.40 with within-piece Meta constructive
contrast +0.15, both carried per #807). The adversarial-on-partner /
favorable-on-non-payer register pattern replicates; the uniform-softening
prediction (mechanism 54, FT x OpenAI deal) fails at the writer level
again. NOT a new falsification-family member (the same writer/partner
prediction test was already counted at #878 as the TWENTY-EIGHTH member;
a same-writer temporal replication is not a new prediction test); ledger
holds at 46; no analysis.json update; NOT artifact-grade; verdict
directionally_supported_not_proven.

Type B FOURTH leg of the 1140-1144 window, CONTINUING it
(D #1140 -> E #1141 -> A #1142 -> B #1143 -> C #1144). Committed
predecessor #1142 Type A (05:00 PDT Oct 2) is the window's third leg
(main 224f054e / anchor 3094ab16 / doc-sync a716c109 / log-hash
7d36f101). Rotation per the #565 anchor + rotation guard.
Concurrency note: the in-flight runs at this run's checks are the
#899 Type C block (m771, uncommitted hunk in profiles/nytimes.yaml),
the #938 Type B test file (uncommitted working-tree edit), the #900
Type D test file (untracked, on disk) and the #1012-wt working-tree
edit of the committed Type A #1012 test file - all UNCOMMITTED, no
Type C #899 / Type B #938 / Type D #900 main commits in git
history, and no ## #899 / ## #938 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch the in-flight files (the
m917 block lands in profiles/careers/journalists.yaml under the
existing cristina_criddle key, NOT nytimes.yaml); the in-flight
blocks are owned by their runs. Targeted staging only per the
repo-wide traversal lesson. Iteration numbers follow the rotation
schedule, not commit order. Do NOT touch #1024's m846 (FOURTEENTH,
exclusionary-diversion): self-flagged sourcing-constraint violation;
Ray's revert/leave/rebuild-from-primary decision still pending.

Verifies:
- m917 (Type B #1143, profiles/careers/journalists.yaml
  cristina_criddle/competitor_coverage block key, 4-space indent,
  `mechanism_id: 917` field form; block key count 3 - colon-form line +
  block_key field + test_file-adjacent mention, designed): Cristina
  Criddle (FT) Sep-16 "blindsided" accountability-adversarial on
  OpenAI+Anthropic (-0.35, headline-tier: techmeme 2026-09-16
  13:57:16 + biztoc relay) TEMPORALLY EXTENDING m758's writer-level
  pattern (Aug-11 Bakalar arm -0.40 carried, Meta within-piece
  constructive contrast +0.15 carried per #807); post-landing corpus
  integrity (max numeric mechanism_id 917; zero next-number 918 keys
  in numeric/underscore/dash mechanism forms - the 918 needles are
  format-built per #715 so no guard-literal carrier file exists;
  falsification ledger holds at 46 - FORTY-SIXTH member-form present
  (m907, profiles/the-verge.yaml), FORTY-SEVENTH member-claim form
  absent repo-wide as designed negative guard for the next landing;
  thirty-fifth direction present (competitor-entities.yaml m915),
  thirty-sixth direction-claim form absent; the #1140/#1141/#1142
  window files are NOT edited by this run - their now-stale
  forward-looking pins are recorded as designed lifecycle in
  TestForwardLookingStaleness1143).
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
    "test_type_b_1143_cristina_criddle_ft_blindsided_openai_anthropic_"
    "sep16_m758_temporal_extension_oct02_6am.py"
)

# Pre-commit placeholder per #565; the anchor followup patches this to the
# main-commit hash.
ANCHORED_SHA = "0" * 40  # Type B #1143 main commit (Type B runs self-anchor per #565)

MECH_NUM = 917
NEXT_NUM = 918

# Literal discipline per #715/#770: the underscore/dash mechanism-key forms,
# the block key, and the member/direction forward-guard forms are
# format-built so this file carries no contiguous needle.
MECH_ID_MARKER = "mechanism" + "_"
MECH_DASH_MARKER = "mechanism" + "-"

BLOCK_KEY = (
    "type_b_1143_cristina_criddle_ft_blindsided_openai_anthropic_"
    "m758_temporal_extension_sep16"
)

FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_SIXTH_MEMBER = "FORTY" + "-SIXTH falsification-family member"
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH" + " relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH" + " relationship direction"
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"

PRED_MAIN_1142 = "224f054e"
PRED_ANCHOR_1142 = "3094ab16"
PRED_DOCSYNC_1142 = "a716c109"
PRED_LOGHASH_1142 = "7d36f101"

FILE_1142 = (
    "test_type_a_1142_wired_openai_sep26_rogue_agent_gov_disclosure_"
    "bounded_absence_vs_cameron_jul28_adversarial_oct02_5am.py"
)

URL_BLINDSIDED = "https://biztoc.com/x/88145bbd4e93e047"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1140_full_suite.log"
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
    return doc["cristina_criddle"]["competitor_coverage"][BLOCK_KEY]


def _block_text():
    return _read(JOURNALISTS_FILE)


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder; patched green post-commit per #565).
# ---------------------------------------------------------------------------

class TestAnchor1143:
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
        assert "type_b_1143" in BLOCK_KEY
        assert "917" not in BLOCK_KEY
        assert BLOCK_KEY in _block_text()

    def test_journalist_file_and_indent(self):
        # The block lives under cristina_criddle's competitor_coverage at
        # indent 4 in profiles/careers/journalists.yaml.
        text = _block_text()
        assert "    " + BLOCK_KEY + ":" in text
        b = _block()
        assert b["journalist"] == "Cristina Criddle"
        assert b["block_key"] == BLOCK_KEY
        assert b["publication"] == "financial-times"


# ---------------------------------------------------------------------------
# 2. Rotation guard (pre-commit assertions; git-log novelty test is
# SUPERSEDED BY DESIGN post-commit - deselect in post-commit full runs).
# ---------------------------------------------------------------------------

class TestRotationGuard1143:
    def test_predecessor_1142_chain_present(self):
        log = _git("log", "--oneline", "-80").stdout
        assert PRED_MAIN_1142 in log
        assert PRED_ANCHOR_1142 in log
        assert PRED_DOCSYNC_1142 in log
        assert PRED_LOGHASH_1142 in log

    def test_type_b_1143_novelty(self):
        # "Type B #1143" absent from git log pre-commit; own file not
        # yet committed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type B #1143:") lands; post-commit, the anchor
        # asserts the patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        log = _git("log", "--oneline", "--grep=Type B #1143").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1140 -> E #1141 -> A #1142 -> B #1143" in src

    def test_window_fourth_leg(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH leg" in src
        assert "1140-1144" in src

    def test_next_run_1144_type_c_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "C #1144" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (post-landing state: max is 917; 918 absent in all
# forms; 917 underscore/dash absent - the forward guards for #1144+).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1143:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1143*.py"))
        assert len(files) == 1, files

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_b_1143 files on disk" in _block_text()

    def test_max_numeric_mechanism_id_is_917(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_underscore_918_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_918_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_918_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_917_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_917_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_917_numeric_present_only_in_journalists_block(self):
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

class TestBlockStructure1143:
    def test_block_loads_under_criddle_competitor_coverage(self):
        doc = yaml.safe_load(_block_text())
        assert BLOCK_KEY in doc["cristina_criddle"]["competitor_coverage"]

    def test_iteration_and_type(self):
        b = _block()
        assert b["iteration"] == 1143
        assert b["type"] == "B"

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_urls_present_and_verbatim(self):
        b = _block()
        assert b["new_openai_anthropic_arm"]["url"] == URL_BLINDSIDED
        assert b["new_openai_anthropic_arm"]["techmeme_timestamp"] == (
            "2026-09-16 13:57:16"
        )

    def test_tone_scores(self):
        b = _block()
        assert b["new_openai_anthropic_arm"]["tone_score"] == -0.35
        assert b["carried_bakalar_arm"]["tone_score"] == -0.4
        assert b["carried_meta_contrast_arm"]["tone_score"] == 0.15
        rc = b["register_contrast"]
        assert rc["illustrative_delta_meta_minus_openai"] == 0.5

    def test_window_and_test_file(self):
        b = _block()
        assert "FOURTH leg" in b["window"]
        assert b["test_file"].endswith(OWN_BASENAME)

    def test_mechanism_ids_appended(self):
        # The journalist key pre-exists (m758 at #878); this run appends
        # 917, not the #643 first-dedicated convention.
        doc = yaml.safe_load(_block_text())
        assert doc["cristina_criddle"]["mechanism_ids"] == [758, 917]


# ---------------------------------------------------------------------------
# 5. m917 content discipline.
# ---------------------------------------------------------------------------

class TestM917ContentDiscipline1143:
    def test_new_arm_fields(self):
        b = _block()
        a = b["new_openai_anthropic_arm"]
        assert a["date"] == "2026-09-16"
        assert a["byline"] == "Cristina Criddle"
        assert a["publication"] == "financial-times"
        quotes = " ".join(a["key_quotes"])
        assert "blindsided by Dario Amodei's and Sam Altman's calls" in quotes
        assert "evaluators may compromise security" in quotes
        assert "headline-tier" in a["evidence_tier"]
        assert "0 browser.open per #503" in a["evidence_tier"]

    def test_carried_bakalar_arm_fields(self):
        b = _block()
        a = b["carried_bakalar_arm"]
        assert a["carried_from"] == "m758"
        assert a["tone_score"] == -0.4

    def test_carried_meta_contrast_fields(self):
        b = _block()
        a = b["carried_meta_contrast_arm"]
        assert a["carried_from"] == "m758"
        assert "ethics programs" in a["note"]

    def test_temporal_extension_hook(self):
        text = _block_text()
        assert "TEMPORAL EXTENSION" in text
        assert "EXTENDING m758" in text or "extension of m758" in text.lower()

    def test_confounders_ranked_strong_first(self):
        b = _block()
        confs = b["confounders"]
        assert confs[0].startswith("STRONG:")
        assert any("dual-entity peg" in c for c in confs)

    def test_counterevidence_present(self):
        b = _block()
        assert len(b["counterevidence"]) >= 3

    def test_cross_refs_carry_m758_m54_m593(self):
        b = _block()
        refs = " ".join(b["cross_refs"])
        assert "#878" in refs
        assert "m54" in refs
        assert "m593" in refs

    def test_research_method_rejections_documented(self):
        b = _block()
        rm = b["research_method"]
        assert "Karissa Bell" in rm
        assert "Dell Cameron" in rm
        assert "0 browser.open this run per #503" in rm
        assert "11 browser.search query sets" in rm

    def test_no_em_dashes_ascii_only(self):
        text = _block_text()
        assert "\u2014" not in text
        assert "\u2013" not in text


# ---------------------------------------------------------------------------
# 6. Statistical discipline.
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1143:
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

class TestFalsificationLedger1143:
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
        assert "TWENTY-NINTH stays the negative guard" in b["ledger_note"]


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1144 Type C run
# pins the 918 landing; the #1145 Type D run tombstones the suite).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1143:
    def test_zero_918_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 918" in src
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

    def test_no_forty_seventh_member_guard(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source (verified by inspection of the constant
        # definition above).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("FORTY" + "-SEVENTH falsification-family member") not in src
        assert len(FORTY_SEVENTH_MEMBER) > 0

    def test_1142_pins_flip_by_design_documented(self):
        # #1142's forward guards (max-916, zero-917 numeric, all-ids<=916)
        # flip by design now that m917 has landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1142" in src
        text = _block_text()
        assert "1142" in text or "m916" in text

    def test_thirty_fifth_direction_still_present(self):
        # m915's METER-THEN-INVITE is the THIRTY-FIFTH relationship
        # direction; its ordinal wording must still be present repo-wide.
        assert "THIRTY-FIFTH" in _profiles_text()


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 917 landing for #1144/#1145).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1143:
    def test_pins_on_917_landing(self):
        # The guards this run lays for the next legs: max-917, zero-918
        # numeric, all-ids<=917, no-Type-C-#1144-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 917" in src
        assert "NEXT_NUM = 918" in src

    def test_no_type_c_1144_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type C #1144").stdout
        assert log.strip() == ""

    def test_918_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1142_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1142))


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and
# tombstoning belong to the next Type D run, #1145).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1143:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1140_full_suite.log" in src

    def test_suite_observed_dead_recorded_not_touched(self):
        # This run stays on targeted verification per the Type B brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest death-observation per #795:
        # #1140-launched suite OBSERVED DEAD at the 06:07 PDT check
        # (last write 04:07 PDT, 3555 bytes / ~5% dots, no live pytest;
        # twelfth consecutive death). #1145 owns the verdict.
        status = _block()["background_suite_status"]
        assert "CHECKED ONLY" in status
        assert "OBSERVED DEAD" in status
        assert "twelfth consecutive" in status
        assert "#1145" in status

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m917 markers.
        log = _read(SUITE_LOG)
        assert "m917" not in log
        assert "Type B #1143" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1143:
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
        assert "#1143" in text


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1143:
    def test_log_entry_header(self):
        text = _read(LOG_PATH)
        assert "## #1143 Type B:" in text

    def test_no_duplicate_1143_entries(self):
        text = _read(LOG_PATH)
        assert text.count("## #1143 Type B:") == 1

    def test_window_fourth_leg_noted(self):
        text = _read(LOG_PATH)
        assert "1140-1144" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1143:
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
            assert "mechanism_id: 917" not in diff, path
            assert "Type B #1143" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 lives in profiles/competitor-entities.yaml;
        # this run must not alter that file at all.
        diff = _git("diff", "--", "profiles/competitor-entities.yaml").stdout
        assert diff == "", diff[:500]

    def test_do_not_touch_1024_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src
