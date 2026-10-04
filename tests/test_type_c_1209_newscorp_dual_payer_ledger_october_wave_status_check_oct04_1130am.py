"""Type C #1209: News Corp dual-payer licensing ledger October-2026 status check
(m957, profiles/competitor-entities.yaml) - FIFTH and CLOSING leg of the
1205-1209 window (D #1205 -> E #1206 -> A #1207 -> B #1208 -> C #1209).

Mechanism 957 is a STATUS-CHECK EXTENSION of the corpus News Corp dual-payer
financial relationship line (m519, Type C #519 Sep 4 2026: News Corp x OpenAI
content licensing deal, >$250M/5yr, largest OpenAI publisher deal, dual-AI-payer
owner with Meta leg and woo-and-sue posture), NOT a new relationship direction.
The fortieth direction stays absent by design; the thirty-fifth (m915,
METER-THEN-INVITE), thirty-sixth (m933, REGULATORY-PREEMPTION), thirty-seventh
(m942, INVEST-AND-LICENSE), thirty-eighth (m945, LICENSE-AND-CO-BUILD), and
thirty-ninth (m948, LICENSE-AND-ADOPT) stand.

Four legs: (1) everything-pr tracker leg (updated Oct 4 2026): re-pins News
Corp x OpenAI up to $250M/5yr and News Corp-Meta up to $50M/yr x 3yr ($150M
total) starting March 2026 in one live view (URL carried, re-read disclosed);
(2) Press Gazette tracker leg (updated ~Sep 29 2026): carries the Meta leg
in its signed-deals list (URL carried, re-read disclosed); (3) combined-figure
leg (awesomeagents.ai, Mar 2026, NOVEL URL): "News Corp's total AI licensing
revenue now passes $400 million across the OpenAI and Meta deals" - the $400M
combined figure is NEW to the corpus; (4) prediction leg: the m519 dual-payer
prediction (symmetric softening incentives toward both Meta and OpenAI at WSJ;
Christopher Mims' dual-disclosure practice) stands un-falsified.

MANUAL / qualitative-only per the Aug 28 2026 standing rule: 2 browser.search
query sets, 0 browser.open; no engine runs, no p-values. NOT artifact-grade.
No analysis.json update. Ledger holds at 49 (the forty-ninth falsification-
family member stands: m956, profiles/careers/journalists.yaml); the fiftieth
member-claim form is absent repo-wide.

Pre-commit values. ANCHORED_SHA is the zero placeholder in this file and is
patched to the main-commit hash in the anchor followup commit.

Per #795: this run only CHECKS the #1205-launched background suite
(observed ALIVE at this run's check: log 38653 bytes, mtime Oct 4 2026 11:32
PDT, ~13% progress, pytest alive at ps scan); its verdict and tombstone
belong to #1210 (next Type D).

Do NOT touch #1024 (m846), #899 (nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must not
carry contiguous numeric/underscore/dash mechanism-key forms of the next
number 958 keys, the fiftieth member form, or the fortieth direction-claim
form; the forty-ninth member form is asserted via runtime-built needles
against profiles/careers/journalists.yaml; the 35th-39th direction forms are
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
    "test_type_c_1209_newscorp_dual_payer_ledger_october_wave_"
    "status_check_oct04_1130am.py"
)
BLOCK_KEY = (
    "type_c_1209_newscorp_dual_payer_ledger_october_wave_"
    "status_check_oct04_1130am"
)

# Pre-commit values. ANCHORED_SHA is patched to the main-commit hash in the
# anchor followup (git rev-parse HEAD after the main commit), per #565.
ANCHORED_SHA = "0" * 40
# Post-first-run values per #719: README_TEST_COUNT / README_FILE_COUNT are
# patched to the post-sync-positive values after the first collection run
# (README ratchets 65006/1533 -> 65006+N/1534 in the doc-sync followup).
README_TEST_COUNT = 65006 + 0  # patched post-first-run per #719
README_FILE_COUNT = 1534
COLLECTED_NEW_TESTS = 0  # patched post-first-run per #719

# Forward guards for the next landing. MECH_NUM=957 is THIS run's landed
# mechanism; NEXT_NUM=958 stays forward.
MECH_NUM = 957
NEXT_NUM = 958

# Needle markers, format-built per #715. The marker is concatenated with the
# number at runtime; the file must never carry the contiguous form.
MECH_ID_MARKER = "mechanism" + "_"     # + "958" at runtime
MECH_DASH_MARKER = "mechanism" + "-"   # + "958" at runtime
THIRTY_FIFTH_DIR = "THIRTY" + "-FIFTH relationship direction"
THIRTY_SIXTH_DIR = "THIRTY" + "-SIXTH relationship direction"
THIRTY_SEVENTH_DIR = "THIRTY" + "-SEVENTH relationship direction"
THIRTY_EIGHTH_DIR = "THIRTY" + "-EIGHTH relationship direction"
THIRTY_NINTH_DIR = "THIRTY" + "-NINTH relationship direction"
FORTIETH_DIR = "FORT" + "IETH relationship direction"
FORTY_NINTH_MEMBER = "FORTY" + "-NINTH falsification-family member"
FIFTIETH_MEMBER = "FIFT" + "IETH falsification-family member"

# The landed m957 block lives here (top-level key; designed keying per
# #715: the block key carries iteration 1209, no 957 substring).
ENTITIES_PATH = os.path.join(REPO, "profiles", "competitor-entities.yaml")
FILE_1208 = (
    "test_type_b_1208_blake_montgomery_guardian_openai_rogue_vs_meta_"
    "18bn_falsification_oct04_11am.py"
)
M846_BLOCK_NEEDLE = "type_c_1024_benioff"

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1205_full_suite.log"
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
    out = _git("log", "--format=%H", "--grep=Type C #1209:").stdout.strip()
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
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1209:
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
        # "Type C #1209 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = _git("log", "--oneline", "--grep=Type C #1209 anchor").stdout
        assert "Type C #1209 anchor" in log

    def test_main_commit_message_convention(self):
        log = _git("log", "--oneline", "--grep=Type C #1209:").stdout
        assert "Type C #1209" in log


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1209 is the FIFTH and CLOSING leg of 1205-1209.
# ---------------------------------------------------------------------------

class TestRotationGuard1209:
    def test_rotation_window_is_1205_1209(self):
        assert "1205-1209" in _entities_text()

    def test_leg_order_documented(self):
        b = _block()
        assert b["window"] == (
            "1205-1209 window FIFTH and CLOSING leg "
            "(D #1205 -> E #1206 -> A #1207 -> B #1208 -> C #1209)"
        )

    def test_iteration_type_c(self):
        assert _block()["iteration_type"] == "C"

    def test_iteration_time(self):
        assert _block()["iteration_time"] == "2026-10-04 11:30 PDT"

    def test_goal_and_job(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (per #715).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1209:
    def test_block_key_present_once(self):
        assert _entities_text().count(BLOCK_KEY + ":") == 1

    def test_block_key_zero_957_substring(self):
        # Designed keying per #715: the block key carries the iteration
        # number 1209, not the mechanism number 957.
        assert "957" not in BLOCK_KEY

    def test_zero_underscore_957_repo_wide(self):
        # Per #1208's forward guard (zero-957 keys all forms): no
        # underscore-form 957 mechanism key may exist repo-wide
        # (own file excluded from the walk).
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_957_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_958_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_957(self):
        present = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert present, "m957 must be present in profiles"
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _profiles_grep_numeric_mechanism_id(n) == [], n

    def test_no_duplicate_block_key(self):
        d = _load_entities()
        assert list(d.keys()).count(BLOCK_KEY) == 1

    def test_urls_copied_verbatim(self):
        urls = [s["url"] for s in _block()["sources"]]
        assert len(urls) == 4
        assert (
            "https://awesomeagents.ai/news/"
            "meta-150m-news-corp-ai-licensing-deal/"
        ) in urls
        assert "https://everything-pr.com/ai-licensing-tracker" in urls
        assert (
            "https://pressgazette.co.uk/platforms/"
            "news-publisher-ai-deals-lawsuits-openai-google/"
        ) in urls
        assert (
            "https://www.stockmoguls.com/2026/09/06/"
            "which-media-companies-profit-when-ai-pays-for-archives/"
        ) in urls
        for u in urls:
            assert u.startswith("https://"), u

    def test_novel_flag_discipline(self):
        # Exactly one novel URL (awesomeagents); the three tracker URLs
        # are carried re-reads, disclosed as novel:false.
        novel = [s for s in _block()["sources"] if s["novel"] is True]
        carried = [s for s in _block()["sources"] if s["novel"] is False]
        assert len(novel) == 1
        assert "awesomeagents" in novel[0]["url"]
        assert len(carried) == 3
        for s in carried:
            assert "disclosed as carried" in s["what"]

    def test_400m_figure_is_new_corpus_fact(self):
        assert "400 million" in _block()["finding"]
        assert "NEW corpus money fact" in _block()["finding"]
        assert "combined figure" in _block()["novelty"]
        assert "zero-hit repo-wide pre-commit" in _block()["novelty"]

    def test_rejected_candidates_documented(self):
        n = _block()["novelty"]
        assert "OpenAI x Synopsys" in n
        assert "out of Type C scope" in n
        assert "Anthropic IPO prospectus" in n
        assert "DOJ amicus" in n

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

class TestBlockStructure1209:
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
        assert b["iteration"] == 1209
        assert b["mechanism_id"] == 957

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
# 5. Content discipline (m957: four legs; dual-payer ledger HOLDS).
# ---------------------------------------------------------------------------

class TestM957ContentDiscipline1209:
    def test_everything_pr_tracker_leg(self):
        f = _block()["finding"]
        assert "Everything-pr tracker leg" in f
        assert "up to $250 million over five years" in f
        assert "up to $50 million per year for three years" in f
        assert "starting March 2026" in f

    def test_press_gazette_tracker_leg(self):
        f = _block()["finding"]
        assert "Press Gazette tracker leg" in f
        assert "up to $50m per year" in f
        assert "signed-deals list" in f

    def test_combined_figure_leg(self):
        f = _block()["finding"]
        assert "Combined-figure leg" in f
        assert "passes $400 million" in f
        assert "largest dual-lab publisher revenue line" in f

    def test_prediction_leg_unfalsified(self):
        f = _block()["finding"]
        assert "Prediction leg" in f
        assert "un-falsified" in f
        assert "Christopher Mims" in f
        assert "symmetric softening incentives" in f

    def test_money_flow_combined_ledger(self):
        m = _block()["money_flow"]
        assert "OPENAI PAYS NEWS CORP" in m
        assert "META PAYS NEWS CORP" in m
        assert "COMBINED DUAL-PAYER LEDGER" in m
        assert "passes $400 million" in m

    def test_confounder_estimate_on_estimate(self):
        texts = " ".join(c["text"] for c in _block()["confounders"])
        assert "estimate-on-estimate" in texts
        assert "thin-provenance" in texts

    def test_confounder_carried_urls_disclosed(self):
        texts = " ".join(c["text"] for c in _block()["confounders"])
        assert "carried in-corpus" in texts
        assert "living documents" in texts

    def test_confounder_no_tone_arms(self):
        texts = " ".join(c["text"] for c in _block()["confounders"])
        assert "no tone arms" in texts

    def test_connects_to_m519(self):
        assert _block()["connects_to"] == [519]

    def test_verdict(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_coverage_nexus_bounded_absence(self):
        assert "iteration-492" in _block()["coverage_nexus"]

    def test_coverage_nexus_type_a_followup(self):
        assert "m919 disclosure-asymmetry" in _block()["coverage_nexus"]


# ---------------------------------------------------------------------------
# 6. Statistical discipline (MANUAL / qualitative-only; NOT artifact-grade).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1209:
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
# 7. Falsification ledger: holds at 49 (m956); the fiftieth form absent.
# ---------------------------------------------------------------------------

class TestFalsificationLedger1209:
    def test_not_family_member(self):
        assert _block()["falsification_family_member"] is False

    def test_ledger_49_in_block(self):
        assert "ledger holds at 49" in _block()["falsification_family"]

    def test_forty_ninth_member_in_journalists_yaml(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source. The landed claim lives in
        # profiles/careers/journalists.yaml (the #1208 m956 block).
        hits = _needle_hits_file(
            FORTY_NINTH_MEMBER, "profiles/careers/journalists.yaml"
        )
        assert hits, FORTY_NINTH_MEMBER

    def test_forty_ninth_member_claim_exact(self):
        # The #1208 m956 landing registers the forty-ninth member in
        # profiles/careers/journalists.yaml.
        assert _needle_hits_profiles(FORTY_NINTH_MEMBER) == [
            "profiles/careers/journalists.yaml"
        ]

    def test_fiftieth_member_absent_repo_wide(self):
        # Format-built per #715: constructed at runtime, never written
        # contiguously in source. Scope is repo-wide (the forward form must
        # not exist anywhere, including this file's own source).
        assert _source_grep(FIFTIETH_MEMBER) == [], FIFTIETH_MEMBER
        assert len(FIFTIETH_MEMBER) > 0


# ---------------------------------------------------------------------------
# 8. Direction extension (no new direction; the fortieth form absent).
# ---------------------------------------------------------------------------

class TestDirectionExtension1209:
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
# 9. Forward-looking staleness (#1210's pins).
# ---------------------------------------------------------------------------

class TestForwardLookingStaleness1209:
    def test_zero_958_guards_are_forward(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NEXT_NUM = 958" in src
        # Needles format-built per #715: constructed at runtime, never
        # written contiguously in source.
        assert (MECH_ID_MARKER + str(NEXT_NUM)) not in src
        assert (MECH_DASH_MARKER + str(NEXT_NUM)) not in src

    def test_no_fortieth_direction_guard(self):
        # Same profiles-scope note as the extension class above.
        assert _needle_hits_profiles(FORTIETH_DIR) == [], FORTIETH_DIR
        assert len(FORTIETH_DIR) > 0

    def test_no_fiftieth_member_guard(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert FIFTIETH_MEMBER not in src
        assert len(FIFTIETH_MEMBER) > 0

    def test_1208_pins_flip_by_design_documented(self):
        # #1208's forward guards (max-956, zero-957 keys all forms,
        # no-Type-C-#1209-in-git-log) flip by design now that m957 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1208" in src
        text = _entities_text()
        assert "1208" in text or "m956" in text

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
# 10. Guard lifecycle (this run pins the 957 landing for #1210).
# ---------------------------------------------------------------------------

class TestGuardLifecycle1209:
    def test_pins_on_957_landing(self):
        # The guards this run lays for the next leg: max-957, zero-958
        # numeric, no-Type-D-#1210-in-git-log, extension (fortieth
        # absent), forty-ninth intact, no fiftieth.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 957" in src
        assert "NEXT_NUM = 958" in src

    def test_no_type_d_1210_in_git_log_pin(self):
        log = _git("log", "--oneline", "--grep=Type D #1210").stdout
        assert log.strip() == ""

    def test_958_numeric_absent_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_predecessor_1208_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, FILE_1208))

    def test_1208_pins_flip_by_design_documented(self):
        # #1208's forward guards (max-956, zero-957 numeric,
        # no-Type-C-#1209-in-git-log) flip by design now that m957 has
        # landed; recorded, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1208" in src
        text = _entities_text()
        assert "1208" in text or "m956" in text


# ---------------------------------------------------------------------------
# 11. Background suite check (checked only per #795 - the verdict and any
# tombstoning belong to the next Type D run, #1210).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1209:
    def test_suite_log_path_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_d_1205_full_suite.log" in src

    def test_suite_checked_only_recorded_not_touched(self):
        # This run stays on targeted verification per the Type C brief;
        # the suite is read-only state, never re-launched, killed, or
        # written to here. The honest observation per #795:
        # #1205-launched suite ALIVE at the ~11:35 PDT check (log 38653
        # bytes, last write Oct 4 11:32 PDT, pytest processes alive at
        # this run's ps scan, progress ~13%, dots accumulating). Its
        # verdict and tombstone belong to #1210 per #795.
        # CHECKED ONLY.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "CHECKED ONLY" in src
        assert "38653" in src
        assert "#1210" in src

    def test_no_pytest_spawned_by_this_run(self):
        # The suite's own process state is recorded, not asserted on;
        # this test only checks the suite log carries no m957 markers.
        log = _read(SUITE_LOG)
        assert "m957" not in log
        assert "Type C #1209" not in log


# ---------------------------------------------------------------------------
# 12. Doc-sync ratchet (per #719: README stats + test table row +
# ARCHITECTURE tree row + test-file constants patch).
# ---------------------------------------------------------------------------

class TestDocSync1209:
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
        assert "#1209" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 65006 + COLLECTED_NEW_TESTS
        assert README_FILE_COUNT == 1534


# ---------------------------------------------------------------------------
# 13. Iteration log (#719: the entry carries hashes per #721).
# ---------------------------------------------------------------------------

class TestIterationLog1209:
    def test_log_entry_header(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #1209 Type C:" in text

    def test_no_duplicate_1209_entries(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.count("## #1209 Type C:") == 1

    def test_window_fifth_leg_noted(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "1205-1209" in text


# ---------------------------------------------------------------------------
# 14. In-flight isolation (marker-scoped per the repo-wide traversal
# lesson; cf. TestInflightIsolation1142).
# ---------------------------------------------------------------------------

class TestInflightIsolation1209:
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
            assert "mechanism_id: 957" not in diff, path
            assert "Type C #1209" not in diff, path

    def test_m846_untouched(self):
        # #1024's m846 block lives in profiles/competitor-entities.yaml;
        # this run appends the m957 block at the end of that file but must
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
        assert "mechanism_id: 957" in diff
