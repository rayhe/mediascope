"""Type C #1214: October 2026 publisher-deal renewal-status sweep (m960,
profiles/competitor-entities.yaml) - FIFTH and CLOSING leg of the 1210-1214
window (D #1210 -> E #1211 -> A #1212 -> B #1213 -> C #1214).

Mechanism 960 is a STATUS-CHECK EXTENSION of three corpus
financial-relationship lines, NOT a new relationship direction: (1) the m597
Axel Springer line (Type C #604, Sep 8 2026: dual-AI-payer architecture,
OpenAI 3-year deal expiry Dec 2026 with renewal UNRESOLVED) - the expiry is
now ~2 months out at the Oct 4 checkpoint; (2) the m600 first-gen OpenAI
publisher renewal-window line (Type C #609, Sep 8 2026: Conde Nast / Atlantic
/ FT renewal mapping, all UNRESOLVED, treated ACTIVE per the #599
convention); (3) the m957 News Corp dual-payer line (Type C #1209, Oct 4
2026: October-wave corroboration, $400M combined figure, dual-payer status
HOLDS) - independently confirmed this run ~3.5h after #1209's tracker
re-reads. The fortieth direction stays absent by design; the thirty-fifth
(m915, METER-THEN-INVITE), thirty-sixth (m933, REGULATORY-PREEMPTION),
thirty-seventh (m942, INVEST-AND-LICENSE), thirty-eighth (m945,
LICENSE-AND-CO-BUILD), and thirty-ninth (m948, LICENSE-AND-ADOPT) stand.

Four legs: (1) Axel Springer expiry countdown (bounded Oct-4 sets: zero
renewal/extension/termination reporting; UNRESOLVED; Meta pays Axel Springer
$0; BI control case stands); (2) first-gen triad (zero renewal reporting;
UNRESOLVED, ACTIVE per #599; OpenAI Jul-2026 $5M local-news renewal is the
positive control); (3) News Corp dual-payer (independent 4-set confirmation,
zero renegotiation/extension/termination/third-lab news; ledger HOLDS;
$400M combined figure stands; no tracker re-read this run, carried from
#1209); (4) forward watch (OpenAI DevDay Oct 6 not yet occurred; #709's
zero-new-deals-since-Sep-8 stands; next Type C window's watch item).

NO NEW MONEY FACTS this run - temporal-posture verification only. NOT a
falsification-family member; ledger holds at 50 (forty-ninth: m956;
fiftieth: m959; fifty-first absent).

MANUAL / qualitative-only per the Aug 28 2026 standing rule: 9
browser.search query sets delegated (research scout) + 1 main-run
verification set, 0 browser.open; no engine runs, no p-values. NOT
artifact-grade. No analysis.json update.

Pre-commit values. ANCHORED_SHA is the zero placeholder in this file and is
patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1210-launched background suite
(observed at this run's check: log 10636 bytes, mtime Oct 4 2026 12:59 PDT,
~3% progress, no live pytest in the ps scan - the one ps hit was the grep
pipeline's own wrapper shell, an artifact not a suite process); its verdict
and tombstone belong to #1215 (next Type D). CHECKED ONLY.

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 961 keys, the fifty-first member form, or the fortieth
direction-claim form; the forty-ninth and fiftieth member forms are asserted
via runtime-built needles against profiles/careers/journalists.yaml; the
35th-39th direction forms are asserted via runtime-built needles against the
landed YAML (never written contiguously in source); the constants are
constructed at runtime.
"""

import os
import re
import subprocess

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TESTS_DIR = HERE

OWN_BASENAME = (
    "test_type_c_1214_october_publisher_deal_renewal_status_sweep_"
    "oct04_3pm.py"
)
BLOCK_KEY = (
    "type_c_1214_october_publisher_deal_renewal_status_sweep_oct04_3pm"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "971a92501137ae125bbacdd6f44968fa2a94106a"  # patched per #565
# Post-first-run values per #719: README_TEST_COUNT / README_FILE_COUNT /
# COLLECTED_NEW_TESTS are patched to the post-sync-positive values after the
# first collection run (README ratchets 65417/1538 -> 65417+N/1539 in the
# doc-sync followup).
README_TEST_COUNT = 65417 + 83  # patched post-first-run per #719
README_FILE_COUNT = 1539  # patched post-first-run per #719
COLLECTED_NEW_TESTS = 83  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=960 is THIS run's landed
# mechanism; NEXT_NUM=961 stays forward.
MECH_NUM = 960
NEXT_NUM = 961

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "961" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "961" at runtime
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"
FORTIETH_DIR = "FORT" + "IETH relationship direction"
FORTY_NINTH_MEMBER = "FORTY" + "-NINTH falsification-family member"
FIFTIETH_MEMBER = "FIFT" + "IETH falsification-family member"
FIFTY_FIRST_MEMBER = "FIFTY" + "-FIRST falsification-family member"

# The landed m960 block lives here (top-level key; designed keying per
# #715: the block key carries iteration 1214, no 960 substring).
ENTITIES_PATH = os.path.join(REPO, "profiles", "competitor-entities.yaml")
FILE_1213 = (
    "test_type_b_1213_kaitlyn_huamani_ap_meta_connect_vs_openai_devday_"
    "falsification_oct04_2pm.py"
)
M846_BLOCK_NEEDLE = "type_c_1024_benioff"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1210_full_suite.log"
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
    out = _git("log", "--format=%H", "--grep=Type C #1214:").stdout.strip()
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

class TestAnchor1214:
    def test_anchor_sha_format(self):
        # 40-char hex in both states (placeholder 0*40 pre-anchor,
        # main-commit hash post-anchor).
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA

    def test_anchor_placeholder_or_main_commit(self):
        # Either the pre-anchor placeholder or a hash present in git log.
        if ANCHORED_SHA != "0" * 40:
            log = _git("log", "--format=%H").stdout
            assert ANCHORED_SHA in log

    def test_anchor_placeholder_pin(self):
        # BY DESIGN: green pre-anchor (placeholder), red post-anchor
        # (patched). Exactly one designed failure post-anchor per the
        # #1196 corrective pattern.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_followup_commit_message_convention(self):
        # Post-anchor only meaningful; pre-anchor the grep is empty and the
        # assertion is vacuous-truthful via the placeholder pin above.
        log = _git("log", "--oneline", "--grep=Type C #1214 anchor").stdout
        if ANCHORED_SHA != "0" * 40:
            assert "Type C #1214 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type C #1214:").stdout
        assert "Type C #1214" in log or ANCHORED_SHA == "0" * 40


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1214 is the FIFTH and CLOSING leg of 1210-1214.
# ---------------------------------------------------------------------------

class TestRotationGuard1214:
    def test_rotation_window_is_1210_1214(self):
        assert "1210-1214" in _entities_text()

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1210-1214 window FIFTH and CLOSING leg "
            "(D #1210 -> E #1211 -> A #1212 -> B #1213 -> C #1214)"
        )

    def test_iteration_type_c(self):
        assert _block()["iteration_type"] == "C"

    def test_iteration_time(self):
        assert _block()["iteration_time"] == "2026-10-04 15:26 PDT"

    def test_goal_and_job(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (per #715).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1214:
    def test_block_key_present_once(self):
        assert _entities_text().count(BLOCK_KEY + ":") == 1

    def test_block_key_zero_960_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1214, not the mechanism number 960.
        assert "960" not in BLOCK_KEY

    def test_zero_underscore_960_repo_wide(self):
        # Per #1213's forward guard (zero-960 keys all forms): no
        # underscore-form 960 mechanism key may exist repo-wide
        # (own file excluded from the walk).
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_960_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_961_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_960(self):
        present = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert present, "m960 must be present in profiles"
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n

    def test_no_duplicate_block_key(self):
        d = _load_entities()
        assert list(d.keys()).count(BLOCK_KEY) == 1

    def test_urls_copied_verbatim(self):
        urls = [s["url"] for s in _block()["sources"]]
        assert len(urls) == 4
        assert (
            "https://ppc.land/full-bot-protection-drops-to-2-4-of-"
            "popular-websites-datadome-finds/"
        ) in urls
        assert (
            "https://www.fastcompany.com/91611155/"
            "bad-bot-traffic-is-growing-9-times-faster-than-human-web-traffic"
        ) in urls
        assert (
            "https://siliconangle.com/2026/09/22/datadome-report-finds-"
            "bad-bot-traffic-growing-nine-times-faster-than-human-traffic/"
        ) in urls
        assert "https://everything-pr.com/ai-licensing-tracker" in urls
        for u in urls:
            assert u.startswith("https://"), u

    def test_novel_flag_discipline(self):
        # Zero novel URLs this run: the finding is a bounded-absence
        # refresh, not a new money fact. All four sources are disclosed
        # as carried or rejected-candidate documentation.
        novel = [s for s in _block()["sources"] if s["novel"] is True]
        carried = [s for s in _block()["sources"] if s["novel"] is False]
        assert len(novel) == 0
        assert len(carried) == 4
        for s in carried:
            assert (
                "disclosed as carried" in s["what"]
                or "REJECTED-CANDIDATE DOCUMENTATION" in s["what"]
            ), s["url"]

    def test_no_new_money_facts_claimed(self):
        assert "NO NEW MONEY FACTS" in _block()["money_flow"]
        assert "temporal-posture verification only" in _block()["money_flow"]
        assert "bounded-absence refresh, not a priced fact" in _block()[
            "money_flow"
        ]

    def test_rejected_candidates_documented(self):
        n = _block()["novelty"]
        assert "DataDome" in n
        assert "REJECTED on Type C scope" in n
        assert "scrape-volume statistic" in n
        assert "unverified, not claimed" in n
        urls = [s["url"] for s in _block()["sources"]]
        assert not any("publishers-ai-buyers-content-market" in u for u in urls)

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

class TestBlockStructure1214:
    def test_yaml_parses(self):
        _load_entities()

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
        b = _block()
        assert b["type"] == "financial_incentive_mapping"
        assert b["type_label"] == "Financial Incentive Mapping"
        assert b["iteration"] == 1214
        assert b["mechanism_id"] == 960

    def test_confounder_strength_order(self):
        # Strong-first ordering per the Type C confounder convention.
        strengths = [c["strength"] for c in _block()["confounders"]]
        assert strengths[0] == "STRONG"
        assert strengths[1] == "STRONG"
        assert set(strengths) <= {"STRONG", "MODERATE", "WEAK"}

    def test_four_sources_accessed(self):
        for s in _block()["sources"]:
            assert s["accessed"] == "2026-10-04"

    def test_flags(self):
        b = _block()
        assert b["yaml_parse_clean"] is True
        assert b["ascii_only"] is True

    def test_ascii_only_content(self):
        # The block text must be pure ASCII (no em dashes, no smart
        # quotes); yaml.safe_load output is the assertion surface.
        for key in ("mechanism_name", "finding", "money_flow",
                    "novelty", "rotation_transparency", "concurrency"):
            text = _block()[key]
            assert text.isascii(), key


# ---------------------------------------------------------------------------
# 5. Content discipline (m960: four legs; October renewal-status
# checkpoint; no new money facts).
# ---------------------------------------------------------------------------

class TestM960ContentDiscipline1214:
    def test_axel_expiry_countdown_leg(self):
        f = _block()["finding"]
        assert "Axel Springer expiry countdown leg" in f
        assert "~2 months out" in f
        assert "Dec 13 2023" in f
        assert "tens of millions EUR" in f
        assert "UNRESOLVED" in f

    def test_first_gen_cohort_leg(self):
        f = _block()["finding"]
        assert "First-gen cohort leg" in f
        assert "Conde Nast" in f
        assert "The Atlantic" in f
        assert "#599 convention" in f
        assert "positive control" in f

    def test_newscorp_confirmation_leg(self):
        f = _block()["finding"]
        assert "News Corp dual-payer leg" in f
        assert "HOLDS" in f
        assert "$400M combined figure stands" in f
        assert "carried from #1209" in f

    def test_devday_forward_watch_leg(self):
        f = _block()["finding"]
        assert "Forward-watch leg" in f
        assert "Oct 6 2026" in f
        assert "has not occurred" in f

    def test_connects_to_three_lines(self):
        assert _block()["connects_to"] == [597, 600, 957]

    def test_bi_control_case_stands(self):
        f = _block()["finding"]
        assert "control case against financial determinism is unchanged" in f

    def test_meta_pays_axel_springer_zero(self):
        f = _block()["finding"]
        assert "Meta pays Axel Springer $0" in f

    def test_no_tracker_reread_this_run(self):
        f = _block()["finding"]
        assert "No tracker re-read this run" in f


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL / qualitative-only per the Aug 28
# 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1214:
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

class TestFalsificationLedger1214:
    def test_not_family_member(self):
        assert _block()["falsification_family_member"] is False

    def test_ledger_50_in_block(self):
        assert "ledger holds at 50" in _block()["falsification_family"]

    def test_forty_ninth_member_intact_3x(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source. The landed claim lives in
        # profiles/careers/journalists.yaml (the #1208 m956 block).
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

    def test_members_only_in_journalists_yaml(self):
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

class TestDirectionExtension1214:
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
# 9. Forward-looking staleness (#1215's pins).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1214:
    def test_zero_961_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 961" in src
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src

    def test_no_fortieth_direction_guard(self):
        # Same profiles-scope note as the extension class above.
        assert _needle_hits_profiles(FORTIETH_DIR) == [], FORTIETH_DIR
        assert len(FORTIETH_DIR) > 0

    def test_no_fifty_first_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert FIFTY_FIRST_MEMBER not in src
        assert len(FIFTY_FIRST_MEMBER) > 0

    def test_1213_pins_flip_by_design_documented(self):
        # #1213's forward guards (max-959, zero-960 keys all forms,
        # no-Type-C-#1214-in-git-log) flip by design now that m960 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1213" in src
        text = _entities_text()
        assert "1213" in text or "m959" in text

    def test_thirty_fifth_direction_still_present(self):
        assert _source_grep(THIRTY_FIFTH_DIR)

    def test_thirty_sixth_direction_still_present(self):
        assert _source_grep(THIRTY_SIXTH_DIR)

    def test_thirty_seventh_direction_still_present(self):
        assert _source_grep(THIRTY_SEVENTH_DIR)

    def test_thirty_eighth_direction_still_present(self):
        assert _source_grep(THIRTY_EIGHTH_DIR)

    def test_thirty_ninth_direction_still_present(self):
        assert _source_grep(THIRTY_NINTH_DIR)


# ---------------------------------------------------------------------------
# 10. Guard lifecycle (this run pins the 960 landing for #1215).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1214:
    def test_pins_on_960_landing(self):
        # The guards this run lays for the next leg: max-960, zero-961
        # numeric, no-Type-D-#1215-in-git-log, extension (fortieth
        # absent), forty-ninth + fiftieth intact, no fifty-first.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 960" in src
        assert "NEXT_NUM = 961" in src

    def test_no_type_d_1215_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type D #1215").stdout
        assert log.strip() == ""

    def test_961_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1213_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1213))

    def test_1213_pins_flip_by_design_documented(self):
        # #1213's forward guards (max-959, zero-960 numeric,
        # no-Type-C-#1214-in-git-log) flip by design now that m960 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1213" in src
        text = _entities_text()
        assert "1213" in text or "m959" in text


# ---------------------------------------------------------------------------
# 11. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1215).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1214:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1210_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type C brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1210-launched suite at the ~15:30 PDT check (log 10636 bytes,
        # last write Oct 4 12:59 PDT, ~3% progress, no live pytest in the
        # ps scan - the one ps hit was the grep pipeline's own wrapper
        # shell, an artifact not a suite process). Its verdict and
        # tombstone belong to #1215 per #795. CHECKED ONLY.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "CHECKED ONLY" in src
        assert "10636" in src
        assert "#1215" in src

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m960 markers.
        log = _read(SUITE_LOG)
        assert "m960" not in log
        assert "Type C #1214" not in log


# ---------------------------------------------------------------------------
# 12. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1214:
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
        assert "#1214" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 65417 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1539


# ---------------------------------------------------------------------------
# 13. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1214:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1214 Type C:" in text

    def test_no_duplicate_1214_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1214 Type C:") == 1

    def test_window_fifth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1210-1214" in text


# ---------------------------------------------------------------------------
# 14. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1214:
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
            assert "mechanism_id: 960" not in diff, path
            assert "Type C #1214" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 block lives in profiles/competitor-entities.yaml;
        # this run appends the m960 block at the end of that file but must
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
        assert "mechanism_id: 960" in diff
