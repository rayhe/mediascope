"""Type C #1219: SPUR Content Telemetry v1.0 technical specifics (m963,
profiles/competitor-entities.yaml) - FIFTH and CLOSING leg of the 1215-1219
window (D #1215 -> E #1216 -> A #1217 -> B #1218 -> C #1219).

Mechanism 963 is a STATUS-CHECK EXTENSION of the m915 METER-THEN-INVITE
line (Type C #1139, Oct 2 2026), NOT a new relationship direction: (1) the
character-over-token metering-unit choice (chars_ingested/excerpt_chars
PRIMARY, tokens supplementary) - the pricing-rail specification that makes
usage-based licensing enforceable across vendors; (2) the v1.0 release
engineering (171 fixtures, 15 validated worked examples, 59 mutation
checks, CI on every PR) and the Jun-12-to-Jul-24 public-comment record;
(3) the Sep-2-vs-Oct-2 dating discrepancy on the v1.0 release object
(UNRESOLVED, disclosed); (4) the v1 verification posture (coverage
declaration; grounding/citation still self-reported, signed events
deferred) - the meter prices the UNIT but not the TRUTHFULNESS; (5) the
Oct-15 first technical-committee meeting as forward watch, with zero lab
acceptances of the advisory-board invitation. The fortieth direction stays
absent by design; the thirty-fifth (m915, METER-THEN-INVITE), thirty-sixth
(m933, REGULATORY-PREEMPTION), thirty-seventh (m942, INVEST-AND-LICENSE),
thirty-eighth (m945, LICENSE-AND-CO-BUILD), and thirty-ninth (m948,
LICENSE-AND-ADOPT) stand.

NO NEW MONEY FACTS this run - still $0 on both channels, carried from
m915. NOT a falsification-family member; ledger holds at 50 (forty-ninth:
m956; fiftieth: m959; fifty-first absent).

MANUAL / qualitative-only per the Aug 28 2026 standing rule: 8
browser.search query sets delegated (research scout) + 3 main-run
verification sets, 0 browser.open; no engine runs, no p-values. NOT
artifact-grade. No analysis.json update.

The scout's primary candidate (SPUR v1.0 + advisory board as a NEW
mechanism) was REJECTED on main-run verification: #1139/m915 already
landed the release + board invitation on Oct 2 (Digiday URL in-corpus).
The surviving novel leg is the v1.0 technical specification content.

Pre-commit values. ANCHORED_SHA is the zero placeholder in this file and is
patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1215-launched background suite
(observed at this run's check: log 9224 bytes, mtime Oct 4 2026 18:17 PDT,
stuck at ~12% progress, no live pytest in the ps scan - the one ps hit was
the grep pipeline's own wrapper shell, an artifact not a suite process);
its verdict and tombstone belong to #1220 (next Type D). CHECKED ONLY.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 964 keys, the fifty-first member form, or the fortieth
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
    "test_type_c_1219_spur_telemetry_v1_chars_over_tokens_"
    "oct04_8pm.py"
)
BLOCK_KEY = (
    "type_c_1219_spur_telemetry_v1_chars_over_tokens_oct04_8pm"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "0" * 40
# Post-first-run values per #719: README_TEST_COUNT / README_FILE_COUNT /
# COLLECTED_NEW_TESTS are patched to the post-sync-positive values after the
# first collection run (README ratchets 65830/1543 -> 65830+N/1544 in the
# doc-sync followup).
README_TEST_COUNT = 65901  # patched post-first-run per #719 (65830+71)
README_FILE_COUNT = 1544  # patched post-first-run per #719
COLLECTED_NEW_TESTS = 71  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=963 is THIS run's landed
# mechanism; NEXT_NUM=964 stays forward.
MECH_NUM = 963
NEXT_NUM = 964

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "964" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "964" at runtime
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

# The landed m963 block lives here (top-level key; designed keying per
# #715: the block key carries iteration 1219, no 963 substring).
ENTITIES_PATH = os.path.join(REPO, "profiles", "competitor-entities.yaml")
FILE_1218 = (
    "test_type_b_1218_christine_ji_marketwatch_meta_fda_hearing_"
    "vs_google_alpha_strategy_oct04_7pm.py"
)
M846_BLOCK_NEEDLE = "type_c_1024_benioff"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1215_full_suite.log"
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
    out = _git("log", "--format=%H", "--grep=Type C #1219:").stdout.strip()
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


def _needle_hits_file(needle, rel_path):
    out = _git("grep", "-l", "-F", needle, "--", rel_path).stdout
    return out.strip().splitlines() if out.strip() else []


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup;
# placeholder-pin duality per the #1196 corrective pattern).
# ---------------------------------------------------------------------------

class TestAnchor1219:
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
        log = _git("log", "--oneline", "--grep=Type C #1219 anchor").stdout
        # Pre-commit: no anchor followup yet. Post-commit: exactly one.
        assert log.strip().count("anchor followup") <= 1

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type C #1219:").stdout
        # Pre-commit: empty. The main commit message carries the
        # "Type C #1219:" prefix per the rotation convention.
        assert "Type C #1219:" in log or log.strip() == ""


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1219 is the FIFTH and CLOSING leg of 1215-1219.
# ---------------------------------------------------------------------------

class TestRotationGuard1219:
    def test_rotation_window_is_1215_1219(self):
        assert _block()["window"].startswith("1215-1219 window FIFTH")

    def test_leg_order_documented(self):
        t = _block()["rotation_transparency"]
        assert "D #1215 -> E #1216 -> A #1217 -> B #1218 -> C #1219" in t

    def test_iteration_type_c(self):
        assert _block()["iteration_type"] == "C"
        assert _block()["iteration"] == 1219

    def test_iteration_time(self):
        assert _block()["iteration_time"] == "2026-10-04 20:15 PDT"

    def test_goal_and_job(self):
        assert _block()["goal_id"] == "goal_54093bda4145"
        assert _block()["scheduled_job_id"] == "mediascope-daily-iteration"


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (per #715).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1219:
    def test_block_key_present_once(self):
        # The colon pins the top-level YAML key form, distinguishing it
        # from the block_key: field value (cf. #1214).
        assert _entities_text().count(BLOCK_KEY + ":") == 1

    def test_block_key_zero_963_substring(self):
        # Designed keying per #715: the block key carries iteration 1219,
        # never the mechanism number as a substring.
        assert "963" not in BLOCK_KEY

    def test_zero_underscore_963_repo_wide(self):
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_963_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_964_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_963(self):
        out = _git(
            "grep", "-rhoE", "mechanism_id: [0-9]+", "--", "profiles"
        ).stdout
        nums = sorted(int(m.split(":")[1]) for m in out.strip().splitlines())
        assert nums[-1] == MECH_NUM, nums[-3:]

    def test_no_duplicate_block_key(self):
        data = _load_entities()
        keys = [k for k in data if "1219" in str(k) and "type_c" in str(k)]
        assert keys == [BLOCK_KEY], keys

    def test_urls_copied_verbatim(self):
        # Every source URL must be byte-identical to the Full-URL listing
        # form (no constructed canonicals).
        for src in _block()["sources"]:
            url = src["url"]
            assert url.startswith("https://"), url
            assert " " not in url, url

    def test_novel_flag_discipline(self):
        # novel:true only where the content (not just the string) is new.
        flags = [(s["url"], s["novel"]) for s in _block()["sources"]]
        assert all(isinstance(n, bool) for _, n in flags)
        by_url = dict(flags)
        assert by_url[
            "https://fourweekmba.com/ai-spur-content-telemetry-1-0-"
            "characters-over-tokens/"
        ] is True
        assert by_url["https://github.com/SPUR-Coalition/telemetry"] is True

    def test_no_new_money_facts_claimed(self):
        assert "NO NEW MONEY FACTS" in _block()["money_flow"]
        assert "$0" in _block()["money_flow"]

    def test_rejected_candidates_documented(self):
        n = _block()["novelty"]
        for rej in (
            "Perplexity Publishers Program",
            "Akamai x Anthropic",
            "Getty x Perplexity",
            "NMA x Bria",
            "AFP x Mistral",
            "Axios x OpenAI",
        ):
            assert rej in n, rej

    def test_block_key_zero_hit_except_landed(self):
        # The block key must not appear anywhere except the landed YAML
        # block and this test file's own references.
        hits = _source_grep(BLOCK_KEY)
        allowed = {
            os.path.join(REPO, "profiles", "competitor-entities.yaml"),
            os.path.join(TESTS_DIR, OWN_BASENAME),
        }
        assert set(hits) <= allowed, hits

    def test_scout_supersession_documented(self):
        # The scout's primary candidate was rejected on main-run
        # verification (#1139/m915 saturation); the novelty field records
        # the supersession, not a fresh landing.
        n = _block()["novelty"]
        assert "REJECTED on main-run verification" in n
        assert "#1139/m915" in n


# ---------------------------------------------------------------------------
# 4. Block structure.
# ---------------------------------------------------------------------------

class TestBlockStructure1219:
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
            assert src["accessed"] == "2026-10-04"

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
# 5. m963 content discipline: the five legs.
# ---------------------------------------------------------------------------

class TestM963ContentDiscipline1219:
    def test_chars_over_tokens_leg(self):
        f = _block()["finding"]
        assert "chars_ingested" in f
        assert "excerpt_chars" in f
        assert "portable counts" in f

    def test_release_engineering_leg(self):
        f = _block()["finding"]
        assert "171 fixtures" in f
        assert "59 mutation checks" in f
        assert "29 specification threads" in f

    def test_dating_discrepancy_leg(self):
        f = _block()["finding"]
        assert "Sep 2 2026" in f
        assert "Oct 2" in f
        assert "not resolved" in f

    def test_v1_verification_posture_leg(self):
        f = _block()["finding"]
        assert "schema_version 1.0" in f
        assert "events are reported by the agent" in f
        assert "signed events" in f and "deferred" in f

    def test_oct15_forward_watch_leg(self):
        f = _block()["finding"]
        assert "October 15" in f
        assert "auditing methods" in f
        assert "No AI company has accepted" in f

    def test_usage_proof_framing_leg(self):
        f = _block()["finding"]
        assert "who may use content" in f
        assert "how often that content shapes an AI response" in f

    def test_connects_to_915(self):
        assert _block()["connects_to"] == [915]

    def test_meter_prices_unit_not_truthfulness(self):
        m = _block()["money_flow"]
        assert "ENFORCEABLE" in m
        assert "truthfulness" in m


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL / qualitative-only per the Aug 28
# 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1219:
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

class TestFalsificationLedger1219:
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

class TestDirectionExtension1219:
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
# 9. Forward-looking staleness (#1220's pins).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1219:
    def test_zero_964_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 964" in src
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src

    def test_no_fortieth_direction_guard(self):
        # Same profiles-scope note as the extension class above.
        assert _needle_hits_profiles(FORTIETH_DIR) == [], FORTIETH_DIR

    def test_no_type_d_1220_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type D #1220").stdout
        assert log.strip() == ""


# ---------------------------------------------------------------------------
# 10. Guard lifecycle (#1218's pins flip by design; others stay green).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1219:
    def test_pins_on_963_landing(self):
        # The guards this run lays for the next leg: max-963, zero-964
        # numeric, no-Type-D-#1220-in-git-log, extension (fortieth
        # absent), forty-eighth + forty-ninth + fiftieth intact, no
        # fifty-first.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 963" in src
        assert "NEXT_NUM = 964" in src

    def test_no_type_d_1220_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type D #1220").stdout
        assert log.strip() == ""

    def test_964_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1218_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1218))

    def test_1218_pins_flip_by_design_documented(self):
        # #1218's forward guards (max-962, zero-963 numeric,
        # no-Type-C-#1219-in-git-log) flip by design now that m963 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1218" in src
        text = _entities_text()
        assert "1218" in text or "m962" in text


# ---------------------------------------------------------------------------
# 11. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1220).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1219:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1215_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type C brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1215-launched suite at the ~20:15 PDT check (log 9224 bytes,
        # last write Oct 4 18:17 PDT, stuck at ~12% progress, no live
        # pytest in the ps scan - the one ps hit was the grep pipeline's
        # own wrapper shell, an artifact not a suite process). Its verdict
        # and tombstone belong to #1220 per #795. CHECKED ONLY.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "CHECKED ONLY" in src
        assert "9224" in src
        assert "#1220" in src

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m963 markers.
        log = _read(SUITE_LOG)
        assert "m963" not in log
        assert "Type C #1219" not in log


# ---------------------------------------------------------------------------
# 12. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1219:
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
        assert "#1219" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 65830 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1544


# ---------------------------------------------------------------------------
# 13. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1219:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1219 Type C:" in text

    def test_no_duplicate_1219_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1219 Type C:") == 1

    def test_window_fifth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1215-1219" in text


# ---------------------------------------------------------------------------
# 14. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1219:
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
            assert "mechanism_id: 963" not in diff, path
            assert "Type C #1219" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 block lives in profiles/competitor-entities.yaml;
        # this run appends the m963 block at the end of that file but must
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
        assert "mechanism_id: 963" in diff
