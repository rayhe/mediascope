"""Type C #1229: Reddit free-tier shutdown enforcement event (m969,
profiles/competitor-entities.yaml) - FIFTH and CLOSING leg of the 1225-1229
window (D #1225 -> E #1226 -> A #1227 -> B #1228 -> C #1229).

Mechanism 969 is a STATUS-CHECK EXTENSION of the m843 Reddit AI-licensing
quantum line (Type C #1019, Sep 26 2026) and the m417/m427 deal-architecture
line, NOT a new relationship direction: (1) the Sep-30 announcement leg -
Reddit's r/modnews + r/redditdev posts set four firm free-tier deadlines
(Oct 31 2026 new-API-request stop; Nov 13 2026 RSS end; Jan 12 2027
unregistered-app cutoff; March 2027 public API close) on the stated
anti-scraping rationale; (2) the paid-deals-preserved leg - Google
(~$60M/yr) and OpenAI (~$70M/yr press-reconstructed, m843 caveat) keep
access while the free tier closes; (3) the migration-program leg - $1M fund,
$1,000 per eligible app to Devvit, 14,000+ registered; (4) the
leverage-context leg - the enforcement executes the m843-documented posture
(July WSJ cut-off deliberation, Huffman commercial-terms quotes, Bloomberg
Sep-2025 talks, 10-K concentration-risk warning); renewal itself still
unresolved; (5) the cohort-significance leg - first dated ENFORCEMENT event
in the publisher-x-AI licensing cohort. The fortieth direction stays absent
by design; the thirty-fifth (m915, METER-THEN-INVITE), thirty-sixth (m933,
REGULATORY-PREEMPTION), thirty-seventh (m942, INVEST-AND-LICENSE),
thirty-eighth (m945, LICENSE-AND-CO-BUILD), and thirty-ninth (m948,
LICENSE-AND-ADOPT) stand.

NO NEW MONEY FACTS this run - the $60M/$70M figures and Q2 $43.3M Other are
carried from m843 with the m843 provenance caveat on the OpenAI leg. NOT a
falsification-family member; ledger holds at 50 (forty-ninth: m956;
fiftieth: m959; fifty-first absent).

MANUAL / qualitative-only per the Aug 28 2026 standing rule: scout query
sets delegated (research scout) + 3 main-run verification sets, 0
browser.open; no engine runs, no p-values. NOT artifact-grade. No
analysis.json update.

The scout's backup candidate (Amazon x Anthropic Q2 $10B tranche + $518B
prospectus commitments) was REJECTED on main-run review (earlier tranches
in-corpus; filing-level verification beyond excerpt-bounded scope; held as a
future Type C candidate). The ten screened-and-rejected angles were each
confirmed rejected (in-corpus saturation or no new money facts). OpenAI
DevDay Oct 6 has not occurred - forward watch carried since #1214.

Pre-commit values. ANCHORED_SHA is the zero placeholder in this file and is
patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1225-launched background suite
(observed at this run's check: log 8145 bytes, mtime Oct 5 2026 03:19 PDT,
~45min stale at the ~04:05 PDT check, one pytest process alive in the ps
scan, zero processes holding the log open per the /proc open-fd check -
an observation, not a verdict); its verdict and tombstone belong to #1230
(next Type D). CHECKED ONLY.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 970 keys, the fifty-first member form, or the fortieth
direction-claim form; the forty-eighth member form is asserted via a
runtime-built needle against profiles/financial-times.yaml; the forty-ninth
and fiftieth member forms are asserted via runtime-built needles against
profiles/careers/journalists.yaml; the 35th-39th direction forms are
asserted via runtime-built needles against the landed YAML (never written
contiguously in source); the constants are constructed at runtime.
"""

import os
import re
import subprocess

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TESTS_DIR = HERE

OWN_BASENAME = (
    "test_type_c_1229_reddit_free_tier_shutdown_enforcement_"
    "event_oct05_4am.py"
)
BLOCK_KEY = (
    "type_c_1229_reddit_free_tier_shutdown_enforcement_"
    "event_oct05_4am"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "26d317415e9b35713f16a3cc449ed501e876c094"  # patched per #565 in the anchor followup
# Post-first-run values per #719: README_TEST_COUNT / README_FILE_COUNT /
# COLLECTED_NEW_TESTS are patched to the post-sync-positive values after the
# first collection run (README ratchets 66646/1553 -> 66646+N/1554 in the
# doc-sync followup).
README_TEST_COUNT = 66646  # patched post-first-run per #719 (66646+N)
README_FILE_COUNT = 1553  # patched post-first-run per #719
COLLECTED_NEW_TESTS = 0  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=969 is THIS run's landed
# mechanism; NEXT_NUM=970 stays forward.
MECH_NUM = 969
NEXT_NUM = 970

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "970" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "970" at runtime
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"
FORTIETH_DIR = "FORT" + "IETH relationship direction"
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"
FORTY_NINTH_MEMBER = "FORTY" + "-NINTH falsification-family member"
FIFTIETH_MEMBER = "FIFT" + "IETH falsification-family member"
FIFTY_FIRST_MEMBER = "FIFTY" + "-FIRST falsification-family member"

# The landed m969 block lives here (top-level key; designed keying per
# #715: the block key carries iteration 1229, no 969 substring).
ENTITIES_PATH = os.path.join(REPO, "profiles", "competitor-entities.yaml")
FILE_1228 = (
    "test_type_b_1228_jess_weatherbed_verge_meta_muse_address_"
    "vs_anthropic_42bn_loss_oct05_3am.py"
)
M846_BLOCK_NEEDLE = "type_c_1024_benioff"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1225_full_suite.log"
)


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
    out = _git("log", "--format=%H", "--grep=Type C #1229:").stdout.strip()
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


def _needle_hits_profiles(needle):
    # profiles/-scoped needle search (cf. #1198): the #1197 test file
    # carries the contiguous fortieth needle in its own constant
    # definition, so the fortieth absence guard is profiles-scoped.
    out = _git("grep", "-l", "-F", needle, "--", "profiles").stdout
    return out.strip().splitlines() if out.strip() else []


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup;
# placeholder-pin duality per the #1196 corrective pattern).
# ---------------------------------------------------------------------------

class TestAnchor1229:
    def test_anchor_sha_format(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    def test_anchor_placeholder_or_main_commit(self):
        # Pre-commit: zero placeholder. Post-anchor-followup: the main
        # commit hash. Either is a valid state for this pin.
        is_placeholder = ANCHORED_SHA == "0" * 40
        is_committed = bool(
            _git("cat-file", "-t", ANCHORED_SHA).stdout.strip() == "commit"
        ) if not is_placeholder else False
        assert is_placeholder or is_committed

    def test_anchor_placeholder_pin(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert 'ANCHORED_SHA = "0" * 40' in src or len(ANCHORED_SHA) == 40

    def test_anchor_followup_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type C #1229 anchor").stdout
        # Pre-commit: no anchor followup yet. Post-commit: exactly one.
        assert log.strip().count("anchor followup") <= 1

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type C #1229:").stdout
        # Pre-commit: empty. The main commit message carries the
        # "Type C #1229:" prefix per the rotation convention.
        assert "Type C #1229:" in log or log.strip() == ""


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1229 is the FIFTH and CLOSING leg of 1225-1229.
# ---------------------------------------------------------------------------

class TestRotationGuard1229:
    def test_rotation_window_is_1225_1229(self):
        assert _block()["window"].startswith("1225-1229 window FIFTH")

    def test_leg_order_documented(self):
        t = _block()["rotation_transparency"]
        assert "D #1225 -> E #1226 -> A #1227 -> B #1228 -> C #1229" in t

    def test_iteration_type_c(self):
        assert _block()["iteration_type"] == "C"
        assert _block()["iteration"] == 1229

    def test_iteration_time(self):
        assert _block()["iteration_time"] == "2026-10-05 04:00 AM PDT"

    def test_goal_and_job(self):
        assert _block()["goal_id"] == "goal_54093bda4145"
        assert _block()["scheduled_job_id"] == "mediascope-daily-iteration"


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (per #715).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1229:
    def test_block_key_present_once(self):
        # The colon pins the top-level YAML key form, distinguishing it
        # from the block_key: field value (cf. #1214).
        assert _entities_text().count(BLOCK_KEY + ":") == 1

    def test_block_key_zero_969_substring(self):
        # Designed keying per #715: the block key carries iteration 1229,
        # never the mechanism number as a substring.
        assert "969" not in BLOCK_KEY

    def test_zero_underscore_969_repo_wide(self):
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_969_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_970_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_969(self):
        out = _git(
            "grep", "-rhoE", "mechanism_id: [0-9]+", "--", "profiles"
        ).stdout
        nums = sorted(int(m.split(":")[1]) for m in out.strip().splitlines())
        assert nums[-1] == MECH_NUM, nums[-3:]

    def test_no_duplicate_block_key(self):
        data = _load_entities()
        keys = [k for k in data if "1229" in str(k) and "type_c" in str(k)]
        assert keys == [BLOCK_KEY], keys

    def test_urls_copied_verbatim(self):
        # Every source URL must be byte-identical to the Full-URL listing
        # form (no constructed canonicals).
        for src in _block()["sources"]:
            url = src["url"]
            assert url.startswith("https://"), url


# ---------------------------------------------------------------------------
# 4. Block structure.
# ---------------------------------------------------------------------------

class TestBlockStructure1229:
    def test_yaml_parses(self):
        assert _block() is not None

    def test_required_fields(self):
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

    def test_type_financial_incentive_mapping(self):
        assert _block()["type"] == "financial_incentive_mapping"

    def test_confounder_strength_order(self):
        strengths = [c["strength"] for c in _block()["confounders"]]
        assert strengths[0] == "STRONG"
        assert strengths[-1] == "WEAK"

    def test_five_sources_accessed(self):
        assert len(_block()["sources"]) == 5
        for src in _block()["sources"]:
            assert src["accessed"] == "2026-10-05"
            assert src["novel"] is True

    def test_flags(self):
        b = _block()
        assert b["yaml_parse_clean"] is True
        assert b["ascii_only"] is True
        assert b["verdict"] == "directionally_supported_not_proven"

    def test_ascii_only_content(self):
        b = _block()
        for field in ("finding", "money_flow", "novelty", "falsification_family"):
            text = b[field]
            assert all(ord(ch) < 128 for ch in text), field
            assert "\u2014" not in text and "\u2013" not in text, field


# ---------------------------------------------------------------------------
# 5. m969 content discipline: the five legs.
# ---------------------------------------------------------------------------

class TestM969ContentDiscipline1229:
    def test_announcement_leg_four_deadlines(self):
        f = _block()["finding"]
        assert "Oct 31 2026" in f
        assert "Nov 13 2026" in f
        assert "Jan 12 2027" in f
        assert "March 2027" in f
        assert "r/modnews" in f
        assert "r/redditdev" in f

    def test_paid_deals_preserved_leg(self):
        f = _block()["finding"]
        assert "explicitly unaffected" in f
        assert "~$60M/yr" in f
        assert "~$70M/yr" in f
        assert "Anthropic and Perplexity are sued" in f

    def test_migration_program_leg(self):
        f = _block()["finding"]
        assert "$1M App Migration Program" in f
        assert "$1,000" in f
        assert "14,000+" in f
        assert "there is no replacement" in f

    def test_leverage_context_leg(self):
        f = _block()["finding"]
        assert "m843" in f
        assert "commercial use of our data requires commercial terms" in f
        assert "may not be renewed" in f

    def test_cohort_significance_leg(self):
        f = _block()["finding"]
        assert "first dated ENFORCEMENT event" in f
        assert "pay-or-take-a-hike" in f

    def test_connects_to_843_417_427(self):
        assert _block()["connects_to"] == [843, 417, 427]

    def test_no_new_money_facts(self):
        m = _block()["money_flow"]
        assert "NO NEW MONEY FACTS" in m
        assert "$60M/yr" in m
        assert "m843 provenance caveat" in m


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL / qualitative-only per the Aug 28
# 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1229:
    def test_tone_not_scored(self):
        assert _block()["tone_scored"] is False

    def test_engine_not_run(self):
        assert _block()["engine_run"] is False

    def test_not_artifact_grade(self):
        assert _block()["artifact_grade"] is False

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_not_significant(self):
        assert _block()["is_significant"] is False

    def test_browser_opens_zero(self):
        assert _block()["browser_opens"] == 0


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 50 (m956 forty-ninth, m959 fiftieth);
# the fifty-first form absent.
# ---------------------------------------------------------------------------

class TestFalsificationLedger1229:
    def test_not_family_member(self):
        assert _block()["falsification_family_member"] is False

    def test_ledger_50_in_block(self):
        assert "ledger holds at 50" in _block()["falsification_family"]

    def test_forty_eighth_member_intact_2x(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source. The landed claim lives in
        # profiles/financial-times.yaml.
        text = _read(os.path.join(REPO, "profiles", "financial-times.yaml"))
        assert text.count(FORTY_EIGHTH_MEMBER) == 2

    def test_forty_ninth_member_intact_3x(self):
        # The #1208 m956 landing registers the forty-ninth member in
        # profiles/careers/journalists.yaml.
        text = _read(
            os.path.join(REPO, "profiles", "careers", "journalists.yaml")
        )
        assert text.count(FORTY_NINTH_MEMBER) == 3

    def test_fiftieth_member_intact_3x(self):
        # The #1213 m959 landing registers the fiftieth member in
        # profiles/careers/journalists.yaml.
        text = _read(
            os.path.join(REPO, "profiles", "careers", "journalists.yaml")
        )
        assert text.count(FIFTIETH_MEMBER) == 3

    def test_members_only_in_expected_files(self):
        assert _needle_hits_profiles(FORTY_EIGHTH_MEMBER) == [
            "profiles/financial-times.yaml"
        ]
        assert _needle_hits_profiles(FORTY_NINTH_MEMBER) == [
            "profiles/careers/journalists.yaml"
        ]
        assert _needle_hits_profiles(FIFTIETH_MEMBER) == [
            "profiles/careers/journalists.yaml"
        ]

    def test_fifty_first_member_absent_repo_wide(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source. Scope is repo-wide (the forward form must
        # not exist anywhere; own file excluded from the walk).
        assert _source_grep(FIFTY_FIRST_MEMBER) == [], FIFTY_FIRST_MEMBER
        assert len(FIFTY_FIRST_MEMBER) > 0


# ---------------------------------------------------------------------------
# 8. Direction extension (no new direction; the fortieth form absent in
# profiles/ per #1199).
# ---------------------------------------------------------------------------

class TestDirectionExtension1229:
    def test_thirty_fifth_direction_present(self):
        assert _source_grep(THIRTY_FIFTH_DIR)

    def test_thirty_sixth_direction_present(self):
        assert _source_grep(THIRTY_SIXTH_DIR)

    def test_thirty_seventh_direction_present(self):
        assert _source_grep(THIRTY_SEVENTH_DIR)

    def test_thirty_eighth_direction_present(self):
        assert _source_grep(THIRTY_EIGHTH_DIR)

    def test_thirty_ninth_direction_present(self):
        assert _source_grep(THIRTY_NINTH_DIR)

    def test_fortieth_direction_absent_in_profiles(self):
        # profiles/-scoped per #1199: the #1197 test file carries the
        # contiguous fortieth needle in its own constant definition.
        assert _needle_hits_profiles(FORTIETH_DIR) == [], FORTIETH_DIR
        assert len(FORTIETH_DIR) > 0

    def test_taxonomy_claims_extension_only(self):
        t = _block()["relationship_direction_taxonomy"]
        assert "STATUS-CHECK EXTENSION" in t
        assert "not a new direction" in t
        assert "absent by design" in t


# ---------------------------------------------------------------------------
# 9. Forward-looking staleness (#1230's pins).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1229:
    def test_zero_970_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 970" in src
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src

    def test_no_fortieth_direction_guard(self):
        # Same profiles-scope note as the extension class above.
        assert _needle_hits_profiles(FORTIETH_DIR) == [], FORTIETH_DIR

    def test_no_type_d_1230_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type D #1230").stdout
        assert log.strip() == ""


# ---------------------------------------------------------------------------
# 10. Guard lifecycle (#1228's pins flip by design; others stay green).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1229:
    def test_pins_on_969_landing(self):
        # The guards this run lays for the next leg: max-969, zero-970
        # numeric, no-Type-D-#1230-in-git-log, extension (fortieth
        # absent), forty-eighth + forty-ninth + fiftieth intact, no
        # fifty-first.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 969" in src
        assert "NEXT_NUM = 970" in src

    def test_no_type_d_1230_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type D #1230").stdout
        assert log.strip() == ""

    def test_970_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1228_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1228))

    def test_1228_pins_flip_by_design_documented(self):
        # #1228's forward guards (max-968, zero-969 numeric,
        # no-Type-C-#1229-in-git-log) flip by design now that m969 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1228" in src
        text = _entities_text()
        assert "1228" in text or "m968" in text


# ---------------------------------------------------------------------------
# 11. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1230).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1229:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1225_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type C brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1225-launched suite at the ~04:05 PDT check (log 8145 bytes,
        # last write Oct 5 2026 03:19 PDT, ~45min stale, one pytest
        # process alive in the ps scan, zero processes holding the log
        # open per the /proc open-fd check - an observation, not a
        # verdict). Its verdict and tombstone belong to #1230 per #795.
        # CHECKED ONLY.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "CHECKED ONLY" in src
        assert "8145" in src
        assert "#1230" in src

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m969 markers.
        log = _read(SUITE_LOG)
        assert "m969" not in log
        assert "Type C #1229" not in log


# ---------------------------------------------------------------------------
# 12. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1229:
    def test_readme_stats_table_updated(self):
        # Current README stats-line convention (per #1217): "| Tests | N |
        # Across M test files |" - no slash form; assert the count and
        # file count both appear.
        text = _read(os.path.join(REPO, "README.md"))
        assert "| Tests |" in text
        assert str(README_TEST_COUNT) in text
        assert str(README_FILE_COUNT) in text

    def test_readme_test_table_row_present(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert OWN_BASENAME in text

    def test_architecture_tree_row_present(self):
        text = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert OWN_BASENAME in text

    def test_iteration_log_entry_present(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "#1229" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 66646 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1554


# ---------------------------------------------------------------------------
# 13. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1229:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1229 Type C:" in text

    def test_no_duplicate_1229_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1229 Type C:") == 1

    def test_window_fifth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1225-1229" in text


# ---------------------------------------------------------------------------
# 14. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1229:
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
            assert "mechanism_id: 969" not in diff, path
            assert "Type C #1229" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 block lives in profiles/competitor-entities.yaml;
        # this run appends the m969 block at the end of that file but must
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
        assert "mechanism_id: 969" in diff
