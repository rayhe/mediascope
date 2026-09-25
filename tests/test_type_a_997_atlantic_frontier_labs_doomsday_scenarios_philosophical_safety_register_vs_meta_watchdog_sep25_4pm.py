"""Type A #997 (2026-09-25 16:00 PDT): The Atlantic x OpenAI/Anthropic Sep-25
doomsday-scenarios philosophical safety-discourse essay vs the carried Meta
Watchdog arms. Third leg of the 995-999 window (D #995 -> E #996 -> A #997).

NEW arm (n=1, mirror_excerpt_bounded): The Atlantic Sep 25, 2026 "Let's get
specific about these doomsday scenarios" (Ideas/Essay register per the LinkedIn
relay https://www.linkedin.com/pulse/lets-get-specific-ai-doomsday-scenarios-the-atlantic-pu7yc)
- sympathetic-exploratory safety-discourse register taking frontier-lab
builders' doomsday beliefs as a premise worth specifying, zero conduct
scrutiny of OpenAI/Anthropic, MANUAL ILLUSTRATIVE +0.00. CARRIED target arm
(m694 / Type A #772, un-rescored per #807): Epley Sep 6 "AI Is Already Changing
What It Means to Be Human" +0.05 (philosophical-anthropology register via the
SZ licensed-reprint mirror). CARRIED peer arms (m481, un-rescored per #807):
Meta Jul-24-2026 Watchdog "Why Would Meta Download So Much Porn?" -0.75 and
Meta Mar-20-2025 "The Unbelievable Scale of AI's Pirated-Books Problem" -0.55.
Bounded absence: no theatlantic.com Meta Connect 2026 coverage in the Sep-25
query sets (bounded search-index absence; theatlantic.com policy-blocked, so
stated as silence, not proof).

Target average +0.025; peer average -0.65; illustrative target-minus-peer delta
+0.675 - directionally consistent with the m481/m694 strand. The claim is a
temporal EXTENSION of m694's philosophical-register strand (Sep 6 -> Sep 25
two-item sequence) and a register-SELECTION claim, not tone magnitude: frontier
labs get the Ideas wonder register; Meta gets the Watchdog accountability
register (or bounded silence). The essay's builders are named generically in
the visible excerpt; OpenAI/Anthropic targeting is inferred from the Sep-2026
doomsday discourse context (STRONGLY confounded, listed).

Statistical discipline per the Aug 28 2026 standing rule: MANUAL ILLUSTRATIVE
scores only, p_value/cohens_d/ci NOT_CALCULATED, is_significant False, engine
NOT run at the finding layer; verdict directionally_supported_not_proven; no
analysis.json update; NOT artifact-grade; NOT falsification-family member;
ledger holds at 30.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4
(patched green in the anchor followup). Doc-sync 3 fail pre-commit per #719,
all green post-doc-sync; iteration-log newest-entry green; hash-placeholder
test fails pre-commit per the #721 convention; staged-set test fails pre-commit
by design.
38 tests, 10 classes. ASCII only, no em dashes.
"""

import re
import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
PROFILE = REPO / "profiles" / "atlantic.yaml"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"
LOG = REPO / "iteration-log.md"
THIS_FILE = Path(__file__).name

ANCHORED_SHA = "a288bc51"  # patched green in the anchor followup per #565

ITERATION = 997
MECHANISM = 829
BLOCK_KEY = (
    "type_a_997_atlantic_frontier_labs_doomsday_scenarios_philosophical_safety_register_vs_meta_watchdog_sep25_2026"
)

NEW_URLS = [
    "https://www.linkedin.com/pulse/lets-get-specific-ai-doomsday-scenarios-the-atlantic-pu7yc",
]

CARRIED_URLS = [
    "https://www.sueddeutsche.de/projekte/artikel/gesellschaft/ai-is-already-changing-what-it-means-to-be-human-e286988/?utm_campaign=sz_meta",
    "https://web.archive.org/web/20260724235323/https://www.theatlantic.com/technology/2026/07/meta-strike-3-porn-lawsuit/688023/",
]

CONNECTS_TO = [481, 694, 404, 572, 718, 825]

EXPECTED_TESTS = 38
README_TESTS_BEFORE, README_TESTS_AFTER = 51264, 51302
README_FILES_BEFORE, README_FILES_AFTER = 1321, 1322

MECH_ID_MARKER = "mechanism" + "_829"
NEXT_ID_MARKER = "mechanism" + "_830"
TOKEN_NEEDLE = "x-access" + "-token"

STAGED_SET = {
    "profiles/atlantic.yaml",
    f"tests/{THIS_FILE}",
    "README.md",
    "docs/ARCHITECTURE.md",
    "iteration-log.md",
}


def run_git(*args):
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, cwd=REPO
    )


def load_block():
    with open(PROFILE) as f:
        data = yaml.safe_load(f)
    return data["competitor_relationships"]["openai"][BLOCK_KEY]


class TestNovelty997:
    def test_single_type_a_997_test_file(self):
        files = sorted((REPO / "tests").glob("test_type_a_997*.py"))
        assert [f.name for f in files] == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type A #997" in r2.stdout

    def test_novelty_claim_present_in_block(self):
        block = load_block()
        assert "FIRST corpus mechanism on the Atlantic Sep-25 doomsday-scenarios essay" in block["novelty"]
        assert "zero underscore-form 829 mechanism key strings" in block["novelty"]


class TestRotationCycleGuard997:
    @pytest.mark.rotation
    def test_third_leg_of_995_to_999_window(self):
        text = LOG.read_text()
        assert "## #995" in text and "Type D" in text
        assert "## #996" in text and "Type E" in text
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "A"

    @pytest.mark.rotation
    def test_predecessor_996_type_e_committed(self):
        r = run_git("log", "--oneline", "--grep=#996")
        assert r.stdout.strip() != ""
        assert (REPO / "tests" / "test_type_e_996_podcast_sentiment_122nd_verification_sep25_3pm.py").exists()

    @pytest.mark.rotation
    def test_no_successor_998_type_b_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type B #998")
        assert r.stdout.strip() == ""
        assert "## #998" not in LOG.read_text()

    @pytest.mark.rotation
    def test_no_concurrent_in_flight_type_a_997_by_commit_time(self):
        r = run_git("log", "--format=%H %s", "--grep=Type A #997")
        matches = [l for l in r.stdout.splitlines() if l.strip()]
        own = run_git("log", "--format=%H", "--", f"tests/{THIS_FILE}").stdout.splitlines()
        competing = [l for l in matches if l.split()[0] not in own]
        assert competing == [], f"concurrent Type A #997 commits: {competing}"


class TestMechanism829Content:
    def test_block_key_unique_at_indent_4_under_openai(self):
        hits = [
            line
            for line in PROFILE.read_text().splitlines()
            if line == f"    {BLOCK_KEY}:"
        ]
        assert len(hits) == 1

    def test_mechanism_id_829_iteration_997_type_a(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "A"
        assert block["type"] == "Type A - Competitor Coverage Deep Dive"
        assert block["publication_pair"] == "Atlantic x OpenAI/Anthropic"
        assert block["competitor"] == "openai"

    def test_new_url_first_appearance(self):
        for url in NEW_URLS:
            assert url in yaml.safe_dump(load_block()), url
            r = run_git("grep", "-l", "-F", url, "--", "profiles/")
            assert [f for f in r.stdout.splitlines() if f] == [
                "profiles/atlantic.yaml"
            ], url

    def test_carried_urls_present_in_block(self):
        block = load_block()
        text = yaml.safe_dump(block)
        for url in CARRIED_URLS:
            assert url in text, url

    def test_connects_to_all_exist(self):
        for m in CONNECTS_TO:
            r = run_git("grep", "-l", f"mechanism_id: {m}$", "--", "profiles/")
            if r.stdout.strip() == "":
                # legacy key form (e.g. mechanism 481 predates mechanism_id)
                r = run_git(
                    "grep", "-l", f"mechanism: {m}$", "--", "profiles/"
                )
            if r.stdout.strip() == "":
                # oldest blocks carry no numeric ID field; keyed by
                # mechanism_<id>_... block name with iteration: <id>
                r = run_git(
                    "grep", "-l", f"mechanism_{m}_", "--", "profiles/"
                )
            assert r.stdout.strip() != "", m
        assert load_block()["connects_to"] == CONNECTS_TO

    def test_verdict_directionally_supported_not_proven(self):
        block = load_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["no_analysis_json_update"] is True

    def test_finding_mentions_extension_and_counterevidence(self):
        finding = load_block()["finding"]
        assert "EXTENDS m694" in finding
        assert "register SELECTION" in finding
        assert "Correlation only" in finding


class TestAsymmetryScorerMath:
    def test_delta_math(self):
        block = load_block()
        scorer = block["asymmetry_scorer_result"]
        assert abs(scorer["target_avg"] - 0.025) < 1e-9
        assert abs(scorer["meta_avg"] - (-0.65)) < 1e-9
        assert abs(scorer["delta_target_minus_meta"] - 0.675) < 1e-9
        assert (
            abs(
                (scorer["target_avg"] - scorer["meta_avg"])
                - scorer["delta_target_minus_meta"]
            )
            < 1e-9
        )

    def test_tones_manual_illustrative_only(self):
        block = load_block()
        assert "MANUAL ILLUSTRATIVE" in block["manual_illustrative_tones_note"]
        assert block["asymmetry_scorer_result"]["artifact_grade"] is False

    def test_scorer_fields_present(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert scorer["target_entity"] == "openai"
        assert scorer["reference_entity"] == "meta"
        assert scorer["publication"] == "the-atlantic"
        assert "interpretation" in scorer
        assert "limitations" in scorer


class TestStatisticalDiscipline997:
    def test_p_value_not_calculated(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False

    def test_correlation_not_causation_in_finding(self):
        finding = load_block()["finding"]
        assert "Correlation only" in finding

    def test_confounders_six_strong_first(self):
        confounders = load_block()["confounders"]
        assert len(confounders) == 6
        assert confounders[0].startswith("STRONG")
        assert confounders[1].startswith("STRONG")
        assert confounders[2].startswith("STRONG")
        assert confounders[5].startswith("WEAK")

    def test_counterevidence_and_counterargument_present(self):
        block = load_block()
        assert len(block["counterevidence"]) >= 4
        assert len(block["strongest_counterargument"]) > 100


class TestSupersessionAndCorpusPost996:
    def test_corpus_max_mechanism_id_is_829(self):
        r = run_git(
            "grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/"
        )
        ids = sorted(
            int(m.group(1))
            for m in (
                re.match(r"mechanism_id: ([0-9]+)$", line)
                for line in r.stdout.splitlines()
            )
            if m
        )
        assert ids[-1] == 829

    def test_iteration_996_max_828_sweep_superseded_by_design(self):
        r = run_git("grep", "-l", "mechanism_id: 828$", "--", "profiles/")
        assert r.stdout.strip() != ""
        r2 = run_git("grep", "-l", "mechanism_id: 829$", "--", "profiles/")
        assert r2.stdout.strip() != ""

    def test_zero_underscore_830_repo_wide(self):
        r = run_git("grep", "-l", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_numeric_830_in_profiles(self):
        r = run_git("grep", "-l", "mechanism_id: 830$", "--", "profiles/")
        assert r.stdout.strip() == ""

    def test_iteration_996_zero_underscore_829_sweep_stays_green(self):
        r = run_git("grep", "-l", MECH_ID_MARKER, "--", "profiles/", "tests/")
        assert r.stdout.strip() == ""

    def test_iteration_996_zero_numeric_829_sweep_fails_by_designed_supersession(self):
        r = run_git("grep", "-l", "mechanism_id: 829$", "--", "profiles/")
        assert r.stdout.strip() != ""

    def test_numeric_829_keys_in_exactly_the_designed_location(self):
        r = run_git("grep", "-l", "mechanism_id: 829$", "--", "profiles/")
        files = [f for f in r.stdout.splitlines() if f]
        assert files == ["profiles/atlantic.yaml"]
        r2 = run_git("grep", "-c", "mechanism_id: 829$", "--", "profiles/atlantic.yaml")
        assert r2.stdout.strip().endswith(":1")


class TestLedger997:
    def test_not_falsification_family_member(self):
        assert load_block()["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        assert load_block()["falsification_ledger"] == 30

    def test_ledger_note_present(self):
        note = load_block()["falsification_note"]
        assert "holds at 30" in note


class TestDocSync997:
    def test_readme_stats_updated(self):
        text = README.read_text()
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text
        assert f"| Tests | {README_TESTS_AFTER} | Across {README_FILES_AFTER} test files |" in text

    def test_readme_table_row_for_997(self):
        text = README.read_text()
        assert f"`tests/{THIS_FILE}`" in text
        assert text.index(f"`tests/{THIS_FILE}`") > text.index(
            "`tests/test_type_e_996_podcast_sentiment_122nd_verification_sep25_3pm.py`"
        )

    def test_architecture_tree_row_for_997(self):
        assert THIS_FILE in ARCH.read_text()


class TestIterationLog997:
    def test_newest_entry_is_997_prepended(self):
        headings = [
            line
            for line in LOG.read_text().splitlines()
            if line.startswith("## #")
        ]
        assert headings[0].startswith("## #997")

    def test_hash_placeholders_filled_post_followup(self):
        text = LOG.read_text()
        entry = text.split("## #997")[1].split("## #996")[0]
        assert re.search(r"\b[0-9a-f]{40}\b", entry) is not None


class TestPushReadiness997:
    def test_staged_set_exactly_five_paths(self):
        r = run_git("diff", "--cached", "--name-only")
        staged = {f for f in r.stdout.splitlines() if f}
        assert staged == STAGED_SET

    def test_concurrency_files_untouched_and_unstaged(self):
        r = run_git("status", "--porcelain")
        lines = r.stdout.splitlines()
        staged = {l[3:] for l in lines if l[:2] in ("M ", "A ")}
        assert "profiles/nytimes.yaml" not in staged
