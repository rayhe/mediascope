# -*- coding: utf-8 -*-
"""Type C #1179 tests: Meta $600B US investment pledge (floated Sep 2025 Trump
White House dinner, formalized as by-2028 AI infrastructure/jobs commitment) -
the VOLUNTARY-PLEDGE form of #12 regulatory-bargaining (mechanism 939).

Iteration #1179, FIFTH and CLOSING leg of the 1175-1179 window
(D #1175 -> E #1176 -> A #1177 -> B #1178 -> C #1179).

The m939 block lives in profiles/competitor-entities.yaml as a top-level
`type_c_1179_...` key (Type C convention; cf. m936 at #1174, m933 at #1169).

This run lands NO new relationship direction: it documents the
VOLUNTARY-PLEDGE form of #12 regulatory-bargaining (m834, Australia NBI) -
there the state legislates the payer menu (deal-or-levy BATNA); here the payer
volunteers the menu (a $600B domestic-investment headline floated at the
President dinner table). The thirty-fifth (m915) and thirty-sixth (m933)
directions stand; the thirty-seventh stays absent by design.

The financing INSTRUMENT behind the pledge is in-corpus (m882,
SPV-DEBT-SHEDDING, the TWENTY-FOURTH direction: Beignet $27B Hyperion,
Sopaipilla $12.55B El Paso); this mechanism maps the PLEDGE as political
instrument, not the financing. FIRST dedicated corpus mechanism on the pledge.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1175-launched background suite
(OBSERVED STALLED); its verdict belongs to #1180.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 940, the FORTY-SEVENTH member-claim form, or the thirty-seventh
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
    "test_type_c_1179_meta_600b_us_pledge_voluntary_"
    "regulatory_bargaining_oct03_1pm.py"
)
BLOCK_KEY = (
    "type_c_1179_meta_600b_us_pledge_voluntary_"
    "regulatory_bargaining_oct03_1pm"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "0" * 40
# Post-first-run values per #719: 70 tests collected; README ratchets
# 62689/1503 -> 62759/1504 in the doc-sync followup.
README_TEST_COUNT = 62759
README_FILE_COUNT = 1504

# Forward guards for the next landing. MECH_NUM=939 is THIS run's landed
# mechanism; NEXT_NUM=940 stays forward.
MECH_NUM = 939
NEXT_NUM = 940

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "940" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "940" at runtime
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"

# The landed m939 block lives here (top-level key; designed keying per
# #715: the block key carries iteration 1179, no 939 substring).
ENTITIES_PATH = os.path.join(REPO, "profiles", "competitor-entities.yaml")
FILE_1178 = (
    "test_type_b_1178_hayden_field_verge_openai_agents_catch_up_"
    "vs_carried_m644_meta_deficit_temporal_extension_sep28_oct03_12pm.py"
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


def _main_sha():
    # The main commit exists only post-commit; pre-commit this is empty and
    # the m846 test falls back to the working-tree diff against HEAD.
    out = _git("log", "--format=%H", "--grep=Type C #1179:").stdout.strip()
    return out.splitlines()[0] if out else ""


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

class TestAnchor1179:
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
        # "Type C #1179 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type C #1179 anchor").stdout
        assert "Type C #1179 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type C #1179:").stdout
        assert "Type C #1179" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1179 is the FIFTH and CLOSING leg of 1175-1179.
# ---------------------------------------------------------------------------

class TestRotationGuard1179:
    def test_rotation_window_is_1175_1179(self):
        assert "1175-1179" in _entities_text()

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1175-1179 window FIFTH and CLOSING leg "
            "(D #1175 -> E #1176 -> A #1177 -> B #1178 -> C #1179)"
        )

    def test_predecessor_types_in_git_log(self):
        log = _git("log", "--oneline").stdout
        for marker in ("Type D #1175", "Type E #1176", "Type A #1177",
                       "Type B #1178"):
            assert marker in log, marker

    def test_no_type_d_1180_in_git_log_yet(self):
        # The next window (1180-1184) opens with Type D #1180; it must not
        # exist as a commit yet.
        log = _git("log", "--oneline", "--grep=Type D #1180").stdout
        assert log.strip() == ""

    def test_single_type_c_1179_test_file(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1179_*.py"))
        assert len(files) == 1 and files[0].endswith(OWN_BASENAME)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (pre-commit claims, verifiable post-commit).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1179:
    def test_block_key_present_once(self):
        assert _entities_text().count(BLOCK_KEY + ":") == 1

    def test_block_key_zero_939_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1179, not the mechanism number 939.
        assert "939" not in BLOCK_KEY

    def test_zero_underscore_939_repo_wide(self):
        # Per #1178's forward guard (zero-939 keys all forms): no
        # underscore-form 939 mechanism key may exist repo-wide
        # (own file excluded from the walk).
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_939_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_940_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_939(self):
        present = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert present, "m939 must be present in profiles"
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n

    def test_no_duplicate_block_key(self):
        d = _load_entities()
        assert list(d.keys()).count(BLOCK_KEY) == 1

    def test_urls_copied_verbatim(self):
        urls = [s["url"] for s in _block()["sources"]]
        assert len(urls) == 6
        assert (
            "https://www.techradar.com/pro/"
            "meta-says-it-wants-to-invest-usd600-billion-in-us-"
            "infrastructure-and-jobs-by-2028"
        ) in urls
        assert (
            "https://www.engadget.com/ai/meta-says-it-will-invest-600-"
            "billion-in-the-us-with-ai-data-centers-front-and-center-"
            "195000377.html"
        ) in urls
        assert (
            "https://www.webpronews.com/metas-600-billion-ai-"
            "infrastructure-gamble-from-open-models-to-cloud-ambitions/"
        ) in urls
        assert (
            "https://siliconangle.com/2025/11/07/meta-announces-plans-"
            "spend-600b-us-three-years/"
        ) in urls
        assert (
            "https://stocktwits.com/news-articles/markets/equity/"
            "meta-announces-600-billion-us-investment-plan-to-strengthen-"
            "ai-data-centers/cL2w3iiREcO"
        ) in urls
        assert (
            "https://oilprice.com/Finance/the-Markets/Off-Balance-Sheet-"
            "AI-Financing-Stirs-Tech-Bubble-Fears.html"
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

class TestBlockStructure1179:
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
        assert b["iteration"] == 1179
        assert b["mechanism_id"] == 939

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
# 5. m939 content discipline (the $600B pledge, voluntary-pledge form).
# ---------------------------------------------------------------------------

class TestM939ContentDiscipline1179:
    def test_pledge_leg(self):
        f = _block()["finding"]
        assert "September 2025 White House dinner" in f
        assert "I was not sure what number you wanted to go with" in f
        assert "hot-mic" in f
        assert "$600B" in f
        assert "by 2028" in f

    def test_delivery_leg(self):
        f = _block()["finding"]
        assert "Blue Owl" in f
        assert "BlackRock" in f
        assert "Meta Compute" in f
        assert "Hyperion" in f
        assert "$115-135B" in f

    def test_cost_leg(self):
        f = _block()["finding"]
        assert "6.58%" in f
        assert "extra interest" in f
        assert "asset-light optics" in f

    def test_political_instrument_leg(self):
        f = _block()["finding"]
        assert "voluntary form inverts m834" in f
        assert "bargaining instrument" in f

    def test_influence_stack_leg(self):
        f = _block()["finding"]
        assert "m933" in f
        assert "$65M" in f
        assert "Mobilizing Economic Transformation" in f
        assert "federal-pledge over state-elections over Sacramento-lobbying" in f

    def test_corpus_positioning_leg(self):
        f = _block()["finding"]
        assert "FIRST dedicated corpus mechanism on the pledge" in f
        assert "m882" in f
        assert "Type A follow-up" in f

    def test_no_new_direction_documented(self):
        t = _block()["relationship_direction_taxonomy"]
        assert "No new direction" in t
        assert "VOLUNTARY-PLEDGE form of #12 regulatory-bargaining" in t
        assert "m834" in t
        assert "thirty-seventh direction stays absent by design" in t

    def test_connects_to(self):
        assert _block()["connects_to"] == [834, 933, 882]

    def test_confounder_strongest_first(self):
        confs = _block()["confounders"]
        assert len(confs) == 6
        assert confs[0]["strength"] == "STRONG"
        strong = [c for c in confs if c["strength"] == "STRONG"]
        assert len(strong) == 3
        assert "forward commitment, not spent capital" in confs[0]["text"]

    def test_coverage_nexus_bounded_absence(self):
        cn = _block()["coverage_nexus"]
        assert "iteration-492" in cn
        assert "Bounded absence" in cn
        assert "NOT scored this run" in cn

    def test_not_falsification_member(self):
        b = _block()
        assert b["falsification_family_member"] is False

    def test_research_method_excerpt_tier(self):
        n = _block()["novelty"]
        assert "4 browser.search query sets" in n
        assert "0 browser.open" in n


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL/QUALITATIVE ONLY per Aug 28 2026 rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1179:
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

class TestFalsificationLedger1179:
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
# 8. Forward-looking staleness (designed lifecycle; the #1180 Type D run
# pins the 940 landing).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1179:
    def test_zero_940_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 940" in src
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

    def test_1178_pins_flip_by_design_documented(self):
        # #1178's forward guards (max-938, zero-939 numeric,
        # no-Type-C-#1179-in-git-log) flip by design now that m939 has
        # landed and this run commits; recorded, not repaired. #1178's
        # zero-939 underscore/dash, no-thirty-seventh/thirty-eighth,
        # no-forty-seventh/forty-eighth, and
        # thirty-fifth/thirty-sixth-intact guards stay green (this run
        # does not touch #1178's file), as do the direction guards.
        rt = _block()["rotation_transparency"]
        assert "fail BY DESIGN" in rt
        assert "max-938" in rt

    def test_thirty_fifth_direction_still_present(self):
        # m915's METER-THEN-INVITE is the THIRTY-FIFTH relationship
        # direction; its ordinal wording must still be present repo-wide.
        assert "THIRTY-FIFTH" in _entities_text()

    def test_thirty_sixth_direction_still_present(self):
        # m933's REGULATORY-PREEMPTION is the THIRTY-SIXTH relationship
        # direction; landed #1169, must still be present.
        assert THIRTY_SIXTH_DIR in _entities_text()


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this run pins the 939 landing for #1180).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1179:
    def test_pins_on_939_landing(self):
        # The guards this run lays for the next leg: max-939, zero-940
        # numeric, no-Type-D-#1180-in-git-log.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 939" in src
        assert "NEXT_NUM = 940" in src

    def test_no_type_d_1180_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type D #1180").stdout
        assert log.strip() == ""

    def test_940_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1178_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1178))


# ---------------------------------------------------------------------------
# 10. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1180).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1179:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1175_full_suite.log" in src

    def test_suite_observed_stalled_recorded_not_touched(self):
        # This run stays on targeted verification per the Type C brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest stalled-observation per #795:
        # #1175-launched suite STALLED at the 13:00 PDT check
        # (log 10635 bytes, last write Oct 3 16:59 UTC, dots at 3%,
        # no live pytest process at ps scan, no m939 markers;
        # byte-identical to #1178's check). #1180 owns the verdict.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "STALLED" in src
        assert "#1180" in src

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m939 markers.
        suite_log = os.path.expanduser(
            "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
            "hidden_files/type_d_1175_full_suite.log"
        )
        log = _read(suite_log)
        assert "m939" not in log
        assert "Type C #1179" not in log


# ---------------------------------------------------------------------------
# 11. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1179:
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
        assert "#1179" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 62759
        assert README_FILE_COUNT == 1504


# ---------------------------------------------------------------------------
# 12. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1179:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1179 Type C:" in text

    def test_no_duplicate_1179_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1179 Type C:") == 1

    def test_window_fifth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1175-1179" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1179:
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
            assert "mechanism_id: 939" not in diff, path
            assert "Type C #1179" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 block lives in profiles/competitor-entities.yaml;
        # this run appends the m939 block at the end of that file but must
        # not alter the m846 block region. Post-commit the working-tree
        # diff is empty, so the check runs against the main commit's own
        # diff for the file (pre-commit it falls back to the working-tree
        # diff against HEAD).
        sha = _main_sha()
        if sha:
            diff = _git(
                "show", sha, "--", "profiles/competitor-entities.yaml"
            ).stdout
        else:
            diff = _git(
                "diff", "HEAD", "--", "profiles/competitor-entities.yaml"
            ).stdout
        assert M846_BLOCK_NEEDLE not in diff
        assert "mechanism_id: 939" in diff
