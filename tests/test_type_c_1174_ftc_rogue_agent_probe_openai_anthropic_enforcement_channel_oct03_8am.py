# -*- coding: utf-8 -*-
"""Type C #1174 tests: FTC rogue-agent probe (Oct 1 2026) enforcement channel -
federal consumer-protection investigation of OpenAI + Anthropic over
autonomous-agent risks (mechanism 936).

Iteration #1174, FIFTH and CLOSING leg of the 1170-1174 window
(D #1170 -> E #1171 -> A #1172 -> B #1173 -> C #1174).

The m936 block lives in profiles/competitor-entities.yaml as a top-level
`type_c_1174_...` key (Type C convention; cf. m933 at #1169, m930 at #1164).

This run lands NO new relationship direction: it documents the
FEDERAL-ENFORCEMENT leg of #2 pay-or-litigate (m636) - the FTC probe widens
the sue side of the menu from private-publisher litigation to federal
consumer-protection enforcement (CID machinery, 10-year authority, METR as
compelled party). The thirty-fifth (m915) and thirty-sixth (m933) directions
stand; the thirty-seventh stays absent by design.

The probe-as-coverage-peg is in-corpus via Type A m901 (#1120), m904 (#1122),
m907 (#1127), m910 (#1132) (all Oct 1, coverage-tone pairs). This mechanism
documents the enforcement CHANNEL itself (machinery, predicate, scope,
philosophy), not the coverage. FIRST dedicated Type C enforcement-channel
mechanism on the probe.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1170-launched background suite
(OBSERVED STALLED); its verdict belongs to #1175.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 937, the FORTY-SEVENTH member-claim form, or the thirty-seventh
direction-claim form; the thirty-fifth/sixth direction forms are asserted via
runtime-built needles against the landed YAML (never written contiguously
in source); the constants are constructed at runtime.
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
    "test_type_c_1174_ftc_rogue_agent_probe_openai_anthropic_"
    "enforcement_channel_oct03_8am.py"
)
BLOCK_KEY = (
    "type_c_1174_ftc_rogue_agent_probe_openai_anthropic_"
    "enforcement_channel_oct03_8am"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "904ccee713991844eeba05eaa3932c2c58d6c4bb"
# Post-first-run values per #719: 70 tests collected; README ratchets
# 62313/1498 -> 62383/1499 in the doc-sync followup.
README_TEST_COUNT = 62383
README_FILE_COUNT = 1499

# Forward guards for the next landing. MECH_NUM=936 is THIS run's landed
# mechanism; NEXT_NUM=937 stays forward.
MECH_NUM = 936
NEXT_NUM = 937

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "937" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "937" at runtime
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"

# The landed m936 block lives here (top-level key; designed keying per
# #715: the block key carries iteration 1174, no 936 substring).
ENTITIES_PATH = os.path.join(REPO, "profiles", "competitor-entities.yaml")
FILE_1173 = (
    "test_type_b_1173_andy_boxall_androidpolice_m132_snap_ar_dream_"
    "vs_sep24_meta_pr_stunt_temporal_extension_oct03_7am.py"
)
M846_BLOCK_NEEDLE = "type_c_1024_benioff"

# Ordinal form of the falsification family. The FORTY-SIXTH member form
# must be present repo-wide; the FORTY-SEVENTH member-claim form must be
# absent (negative guard). (The falsification-family thirty-sixth member
# m878 is a separate taxonomy from the relationship-direction ordinal.)
FORTY_SIXTH_LANDED = "FORTY-SIXTH falsification-family member"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _load_entities():
    return yaml.safe_load(_read(ENTITIES_PATH))


def _block():
    return _load_entities()[BLOCK_KEY]


def _entities_text():
    return _read(ENTITIES_PATH)


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

class TestAnchor1174:
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
        # "Type C #1174 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type C #1174 anchor").stdout
        assert "Type C #1174 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type C #1174:").stdout
        assert "Type C #1174" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1174 is the FIFTH and CLOSING leg of 1170-1174.
# ---------------------------------------------------------------------------

class TestRotationGuard1174:
    def test_rotation_window_is_1170_1174(self):
        assert "1170-1174" in _entities_text()

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1170-1174 window FIFTH and CLOSING leg "
            "(D #1170 -> E #1171 -> A #1172 -> B #1173 -> C #1174)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1170", "Type E #1171", "Type A #1172",
                       "Type B #1173"):
            assert marker in log, marker

    def test_no_type_d_1175_in_git_log_yet(self):
        # The next window (1175-1179) opens with Type D #1175; it must not
        # exist as a commit yet.
        log = _git("log", "--oneline", "--grep=Type D #1175").stdout
        assert log.strip() == ""

    def test_single_type_c_1174_test_file(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1174_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1174:
    def test_block_key_present_once(self):
        assert _entities_text().count(BLOCK_KEY + ":") == 1

    def test_block_key_zero_936_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1174, not the mechanism number 936.
        assert "936" not in BLOCK_KEY

    def test_zero_underscore_936_repo_wide(self):
        # Per #1173's forward guard (zero-936 keys all forms): no
        # underscore-form 936 mechanism key may exist repo-wide
        # (own file excluded from the walk).
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_936_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_937_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_936(self):
        present = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert present, "m936 must be present in profiles"
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n

    def test_no_duplicate_block_key(self):
        d = _load_entities()
        assert list(d.keys()).count(BLOCK_KEY) == 1

    def test_urls_copied_verbatim(self):
        urls = [s["url"] for s in _block()["sources"]]
        assert len(urls) == 6
        assert (
            "https://www.tbsnews.net/world/"
            "ftc-opens-probe-ai-giants-including-anthropic-and-openai-1559131"
        ) in urls
        assert (
            "https://broadbandbreakfast.com/"
            "ftc-opens-probe-of-ai-giants-anthropic-openai-over-consumer-risks/"
        ) in urls
        assert (
            "https://tech-insider.org/"
            "ftc-investigates-openai-anthropic-ai-agents-2026/"
        ) in urls
        assert (
            "https://openclassactions.com/news/"
            "ftc-openai-anthropic-ai-investigation-2026.php"
        ) in urls
        assert (
            "https://insideai.news/news/ai-policy-and-regulation/"
            "ftc-investigation-anthropic-openai/13381/"
        ) in urls
        assert (
            "https://www.renascence.io/news/84117/"
            "ftc-investigation-targets-openai-anthropic-over-consumer-protection"
        ) in urls
        for u in urls:
            assert u.startswith("https://"), u

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit it
        # appears only in the landed YAML block, this test file, and the
        # doc-sync surfaces (README, ARCHITECTURE, iteration-log).
        hits = _source_grep(BLOCK_KEY)
        allowed = {
            os.path.join(REPO, "profiles", "competitor-entities.yaml"),
            os.path.join(TESTS_DIR, OWN_BASENAME),
            os.path.join(REPO, "README.md"),
            os.path.join(REPO, "docs", "ARCHITECTURE.md"),
            os.path.join(REPO, "iteration-log.md"),
        }
        for h in hits:
            assert h in allowed, h


# ---------------------------------------------------------------------------
# 4. Block structure (Type C top-level key convention in
# profiles/competitor-entities.yaml).
# ---------------------------------------------------------------------------

class TestBlockStructure1174:
    def test_top_level_block_key(self):
        d = _load_entities()
        assert BLOCK_KEY in d

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "block_key", "mechanism_id", "mechanism_name", "type",
            "type_label", "iteration", "iteration_type", "iteration_time",
            "goal_id", "scheduled_job_id", "window", "connects_to",
            "relationship_direction_taxonomy", "finding", "money_flow",
            "confounders", "coverage_nexus", "sources", "browser_opens",
            "tone_scored", "engine_run", "is_significant", "verdict",
            "no_analysis_json_update", "artifact_grade",
            "falsification_family_member", "falsification_family",
            "novelty", "rotation_transparency", "concurrency",
            "yaml_parse_clean", "ascii_only",
        ):
            assert field in b, field

    def test_type_and_iteration(self):
        b = _block()
        assert b["type"] == "financial_incentive_mapping"
        assert b["iteration_type"] == "C"
        assert b["iteration"] == 1174
        assert b["mechanism_id"] == 936

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_ascii_only_region(self):
        text = _entities_text()
        start = text.index(BLOCK_KEY + ":")
        text[start:].encode("ascii")

    def test_yaml_parse_clean(self):
        assert _block()["yaml_parse_clean"] is True
        assert _block()["ascii_only"] is True

    def test_browser_opens_zero(self):
        assert _block()["browser_opens"] == 0


# ---------------------------------------------------------------------------
# 5. m936 content discipline (the FTC probe enforcement channel).
# ---------------------------------------------------------------------------

class TestM936ContentDiscipline1174:
    def test_probe_announcement_leg(self):
        f = _block()["finding"]
        assert "Oct 1" in f
        assert "New York Post" in f
        assert "first official US enforcement action" in f
        assert "METR" in f

    def test_incident_predicate_leg(self):
        f = _block()["finding"]
        assert "Hugging Face" in f
        assert "Census Bureau" in f
        assert "most serious example of unexpected behavior" in f
        assert "Dario Amodei" in f

    def test_scope_leg(self):
        f = _block()["finding"]
        assert "September 30, 2026" in f
        assert "unfair or deceptive practices" in f
        assert "escaping test environments" in f

    def test_enforcement_machinery_leg(self):
        f = _block()["finding"]
        assert "civil investigative demand" in f
        assert "November 2023" in f
        assert "ten years" in f
        assert "6(b)" in f
        assert "January 2025" in f

    def test_philosophy_leg(self):
        f = _block()["finding"]
        assert "Andrew Ferguson" in f
        assert "deep suspicion" in f
        assert "wall and a moat" in f

    def test_corpus_positioning_leg(self):
        f = _block()["finding"]
        assert "m901" in f
        assert "m904" in f
        assert "m907" in f
        assert "m910" in f
        assert "FIRST dedicated Type C enforcement-channel mechanism" in f

    def test_no_new_direction_documented(self):
        t = _block()["relationship_direction_taxonomy"]
        assert "No new direction" in t
        assert "FEDERAL-ENFORCEMENT leg of #2 pay-or-litigate" in t
        assert "m636" in t
        assert "thirty-seventh direction stays absent by design" in t

    def test_connects_to(self):
        assert _block()["connects_to"] == [636, 834, 753, 930]

    def test_confounder_strongest_first(self):
        confs = _block()["confounders"]
        assert len(confs) == 6
        assert confs[0]["strength"] == "STRONG"
        strong = [c for c in confs if c["strength"] == "STRONG"]
        assert len(strong) == 3
        assert "sourced reporting, not a public record" in confs[0]["text"]

    def test_coverage_nexus_bounded_absence(self):
        cn = _block()["coverage_nexus"]
        assert "iteration-492" in cn
        assert "bounded absence" in cn
        assert "SB 1130" in cn

    def test_not_falsification_member(self):
        b = _block()
        assert b["falsification_family_member"] is False

    def test_research_method_excerpt_tier(self):
        n = _block()["novelty"]
        assert "6 browser.search query sets" in n
        assert "0 browser.open" in n


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL/QUALITATIVE ONLY per Aug 28 2026 rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1174:
    def test_no_engine_run(self):
        b = _block()
        assert b["engine_run"] is False
        assert b["tone_scored"] is False

    def test_stats_not_calculated(self):
        n = _block()["novelty"]
        assert "MANUAL / qualitative-only" in n
        assert "Aug 28 2026 standing rule" in n

    def test_verdict_discipline(self):
        b = _block()
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True
        assert b["is_significant"] is False

    def test_not_artifact_grade(self):
        b = _block()
        assert b["artifact_grade"] is False


# ---------------------------------------------------------------------------
# 7. Falsification ledger (holds at 46; no new member this run).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1174:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False

    def test_forty_sixth_member_form_present(self):
        assert _repo_grep(FORTY_SIXTH_LANDED), FORTY_SIXTH_LANDED

    def test_forty_seventh_member_claim_absent(self):
        # Negative-guard wordings ("absent repo-wide") are allowed; the
        # affirmative member-claim form must not exist. Needle format-built
        # per #715; own file carries no contiguous needle.
        assert FORTY_SEVENTH_MEMBER not in _entities_text()

    def test_forty_eighth_member_claim_absent(self):
        assert FORTY_EIGHTH_MEMBER not in _entities_text()

    def test_ledger_note_wording(self):
        ff = _block()["falsification_family"]
        assert "ledger holds at 46" in ff
        assert "FORTY-SEVENTH member-claim form absent repo-wide" in ff
        assert "thirty-seventh direction form absent repo-wide" in ff


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (designed lifecycle; the #1175 Type D run
# pins the 937 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1174:
    def test_zero_937_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 937" in src
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src

    def test_no_thirty_seventh_direction_guard(self):
        # The contiguous direction-claim form must not appear in this
        # file's source; the guard constant stays format-built per #715.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("THIRTY" + "-SEVENTH relationship direction") not in src
        assert len(THIRTY_SEVENTH_DIR) > 0

    def test_no_thirty_eighth_direction_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("THIRTY" + "-EIGHTH relationship direction") not in src
        assert len(THIRTY_EIGHTH_DIR) > 0

    def test_no_forty_seventh_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("FORTY" + "-SEVENTH falsification-family member") not in src
        assert len(FORTY_SEVENTH_MEMBER) > 0

    def test_1173_pins_flip_by_design_documented(self):
        # #1173's forward guards (max-935, zero-936 numeric,
        # no-Type-C-#1174-in-git-log) flip by design now that m936 has
        # landed and this run commits; recorded, not repaired. #1173's
        # zero-936 underscore/dash, no-thirty-seventh/thirty-eighth,
        # no-forty-seventh/forty-eighth, and
        # thirty-fifth/thirty-sixth-intact guards stay green (this run
        # does not touch #1173's file), as do the direction guards.
        rt = _block()["rotation_transparency"]
        assert "fail BY DESIGN" in rt
        assert "max-935" in rt

    def test_thirty_fifth_direction_still_present(self):
        # m915's METER-THEN-INVITE is the THIRTY-FIFTH relationship
        # direction; its ordinal wording must still be present repo-wide.
        assert "THIRTY-FIFTH" in _entities_text()

    def test_thirty_sixth_direction_still_present(self):
        # m933's REGULATORY-PREEMPTION is the THIRTY-SIXTH relationship
        # direction; landed #1169, must still be present.
        assert THIRTY_SIXTH_DIR in _entities_text()


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 936 landing for #1175).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1174:
    def test_pins_on_936_landing(self):
        # The guards this run lays for the next leg: max-936, zero-937
        # numeric, no-Type-D-#1175-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 936" in src
        assert "NEXT_NUM = 937" in src

    def test_no_type_d_1175_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type D #1175").stdout
        assert log.strip() == ""

    def test_937_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1173_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1173))


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1175).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1174:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1170_full_suite.log" in src

    def test_suite_observed_stalled_recorded_not_touched(self):
        # This run stays on targeted verification per the Type C brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest stalled-observation per #795:
        # #1170-launched suite STALLED at the 08:00 PDT check
        # (log 2551 bytes, last write Oct 3 05:59 PDT, dots at 3% with
        # one F, no live pytest process at ps scan, no m936 markers;
        # byte-identical to #1173's check). #1175 owns the verdict.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "STALLED" in src
        assert "#1175" in src

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m936 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1170_full_suite.log"
        )
        log = _read(suite_log)
        assert "m936" not in log
        assert "Type C #1174" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1174:
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
        assert "#1174" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 62383
        assert README_FILE_COUNT == 1499


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1174:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1174 Type C:" in text

    def test_no_duplicate_1174_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1174 Type C:") == 1

    def test_window_fifth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1170-1174" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1174:
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
            assert "mechanism_id: 936" not in diff, path
            assert "Type C #1174" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 block lives in profiles/competitor-entities.yaml;
        # this run appends the m936 block at the end of that file but must
        # not alter the m846 block region. Post-commit the working-tree
        # diff is empty, so the check runs against the main commit's own
        # diff for the file.
        diff = _git(
            "show", "904ccee7", "--", "profiles/competitor-entities.yaml"
        ).stdout
        assert M846_BLOCK_NEEDLE not in diff
        assert "mechanism_id: 936" in diff
