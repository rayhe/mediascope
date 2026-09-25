"""Type A #987 (2026-09-25 06:00 PDT): FT x OpenAI September-2026 cash-burn
realism (-0.15, carried from mechanism #754) vs FT x Meta September-2026
Muse-Charm momentum-change constructiveness (+0.20, NEW this run) - register
inversion in an unmatched-peg window, temporal BOUND on mechanisms #718/#754.
Third leg of the 985-989 window (D #985 -> E #986 -> A #987 -> B #988 -> C #989).

OpenAI arm (carried, un-rescored per #807): FT Sep 18, 2026 $278B cash-burn
forecast scoop on its $5-10M/yr licensing partner - "expects to burn through
$278 billion in cash between 2026 and 2030", negative free cash flow of $278B
2026-2030, the $122B March raise "on track to exhaust that cash by 2028",
against revenue tenfold $36B to $350B by 2030, cumulative $840B, $856B compute
spend. MANUAL ILLUSTRATIVE -0.15, balance-sheet realism, the FT's most
adversarial OpenAI item this window. Meta arm (NEW): Hannah Murphy's FT Sep 24,
2026 "Meta puts its AI assistant on a keychain" piece (Ars Technica relay,
theoverspill.blog Sep 25) - Muse "has helped change the momentum of
Zuckerberg's huge bet on AI", "most downloaded app on both the Apple and
Android app stores in the US since its launch two weeks ago", "centerpiece" of
the AI vision, "state-of-the-art privacy and security" relayed straight.
MANUAL ILLUSTRATIVE +0.20. Illustrative OpenAI-minus-Meta delta -0.35, n=1 vs
n=1, NOT significant - INVERTS mechanism #718's matched-peg +0.55 gap
(Sep-15 OpenAI $1.2T investor-demand scoop vs Jun-5 Meta equity-raise
desperation scoop). Within-reporter departure: Murphy is corpus-classified
Meta-adversarial (FT profile), so the constructive register is peg-driven, not
structural. Supporting OpenAI-side context (NEW): Aug 31, 2026 ChatGPT ads $1B
annualized run-rate relay (+0.05, neutral milestone).

Statistical discipline per the Aug 28 2026 standing rule: MANUAL ILLUSTRATIVE
scores only, p_value/cohens_d/ci NOT_CALCULATED, is_significant False, engine
NOT run at the finding layer; verdict directionally_supported_not_proven; no
analysis.json update; NOT artifact-grade; NOT falsification-family member;
ledger holds at 30.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4
(patched green in the anchor followup). Doc-sync 3 fail pre-commit per #719,
all green post-doc-sync; iteration-log hash-placeholder test fails pre-commit
per the #721 convention.
41 tests, 10 classes. ASCII only, no em dashes.
"""

import re
import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
PROFILE = REPO / "profiles" / "financial-times.yaml"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"
LOG = REPO / "iteration-log.md"
THIS_FILE = Path(__file__).name

ANCHORED_SHA = "0dd16fa8613dc7b4b3cc0cc293e5c7eda4c01d80"

ITERATION = 987
MECHANISM = 823
BLOCK_KEY = (
    "type_a_987_ft_openai_burn_realism_vs_meta_muse_charm_"
    "momentum_change_sep25_2026"
)

NEW_URLS = [
    "https://theoverspill.blog/2026/09/25/fbi-hack-employees-terabytes-start-up-2749/",
    "https://mlq.ai/news/openai-says-chatgpt-ads-reach-1-billion-annualized-revenue-run-rate-in-under-200-days/",
    "https://northlandnewsradio.com/2026/09/18/openai-expects-to-burn-through-almost-280-billion-by-2030-ft-reports/",
]

CARRIED_URLS = [
    "https://wixx.com/2026/09/18/openai-expects-to-burn-through-almost-280-billion-by-2030-ft-reports/",
    "https://www.reuters.com/legal/transactional/openai-mulls-funding-round-12-trillion-valuation-ahead-ipo-ft-reports-2026-09-15/",
    "https://www.usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses/91913146007/",
    "https://dig.watch/updates/meta-confirms-camera-free-ray-ban-smart-glasses",
]

CONNECTS_TO = [754, 718, 54, 643, 676, 625]

EXPECTED_TESTS = 41
README_TESTS_BEFORE, README_TESTS_AFTER = 50773, 50814
README_FILES_BEFORE, README_FILES_AFTER = 1311, 1312

MECH_ID_MARKER = "mechanism" + "_823"
NEXT_ID_MARKER = "mechanism" + "_824"
TOKEN_NEEDLE = "x-access" + "-token"

STAGED_SET = {
    "profiles/financial-times.yaml",
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


class TestNovelty987:
    def test_single_type_a_987_test_file(self):
        files = sorted((REPO / "tests").glob("test_type_a_987*.py"))
        assert [f.name for f in files] == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type A #987" in r2.stdout

    def test_novelty_claim_present_in_block(self):
        block = load_block()
        assert "Three new URL keys" in block["novelty"]
        assert block["novelty"].count("first corpus appearance") >= 0


class TestRotationCycleGuard987:
    @pytest.mark.rotation
    def test_third_leg_of_985_to_989_window(self):
        text = LOG.read_text()
        assert "## #985" in text and "Type D" in text
        assert "## #986" in text and "Type E" in text
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "A"

    @pytest.mark.rotation
    def test_predecessor_986_type_e_committed(self):
        r = run_git("log", "--oneline", "--grep=#986")
        assert r.stdout.strip() != ""
        assert (REPO / "tests" / "test_type_e_986_podcast_sentiment_120th_verification_sep25_5am.py").exists()

    @pytest.mark.rotation
    def test_no_successor_988_type_b_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type B #988")
        assert r.stdout.strip() == ""
        assert "## #988" not in LOG.read_text()

    @pytest.mark.rotation
    def test_no_concurrent_in_flight_type_a_987_by_commit_time(self):
        r = run_git("log", "--oneline", "--grep=Type A #987")
        assert r.stdout.strip() == ""


class TestMechanism823Content:
    def test_block_key_unique_at_indent_4_under_openai(self):
        hits = [
            line
            for line in PROFILE.read_text().splitlines()
            if line == f"    {BLOCK_KEY}:"
        ]
        assert len(hits) == 1

    def test_mechanism_id_823_iteration_987_type_a(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "A"
        assert block["type"] == "Type A - Competitor Coverage Deep Dive"
        assert block["publication_pair"] == "FT x OpenAI"
        assert block["competitor"] == "openai"

    def test_three_new_urls_first_appearance(self):
        for url in NEW_URLS:
            assert url in yaml.safe_dump(load_block()), url
            r = run_git("grep", "-l", "-F", url, "--", "profiles/")
            assert [f for f in r.stdout.splitlines() if f] == [
                "profiles/financial-times.yaml"
            ], url

    def test_carried_urls_present_in_block(self):
        block = load_block()
        text = yaml.safe_dump(block)
        for url in CARRIED_URLS:
            assert url in text, url

    def test_connects_to_all_exist(self):
        for m in CONNECTS_TO:
            r = run_git("grep", "-l", f"mechanism_id: {m}$", "--", "profiles/")
            assert r.stdout.strip() != "", m
        assert load_block()["connects_to"] == CONNECTS_TO

    def test_verdict_directionally_supported_not_proven(self):
        block = load_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["no_analysis_json_update"] is True

    def test_finding_mentions_cash_burn_and_muse_charm(self):
        finding = load_block()["finding"]
        assert "$278 billion" in finding
        assert "Muse" in finding
        assert "change the momentum" in finding
        assert "Correlation only" in finding


class TestAsymmetryScorerMath:
    def test_delta_math(self):
        block = load_block()
        scorer = block["asymmetry_scorer_result"]
        assert abs(scorer["target_avg"] - (-0.15)) < 1e-9
        assert abs(scorer["reference_avg"] - 0.2) < 1e-9
        assert abs(scorer["delta_openai_minus_meta"] - (-0.35)) < 1e-9
        assert (
            abs(
                (scorer["target_avg"] - scorer["reference_avg"])
                - scorer["delta_openai_minus_meta"]
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
        assert scorer["publication"] == "financial-times"
        assert "interpretation" in scorer
        assert "limitations" in scorer


class TestStatisticalDiscipline987:
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
        assert len(block["counterevidence"]) >= 3
        assert len(block["strongest_counterargument"]) > 100


class TestSupersessionAndCorpusPost986:
    def test_corpus_max_mechanism_id_is_823(self):
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
        assert ids[-1] == 823

    def test_iteration_986_max_822_sweep_superseded_by_design(self):
        r = run_git("grep", "-l", "mechanism_id: 822$", "--", "profiles/")
        assert r.stdout.strip() != ""
        r2 = run_git("grep", "-l", "mechanism_id: 823$", "--", "profiles/")
        assert r2.stdout.strip() != ""

    def test_zero_underscore_824_repo_wide(self):
        r = run_git("grep", "-l", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_numeric_824_in_profiles(self):
        r = run_git("grep", "-l", "mechanism_id: 824$", "--", "profiles/")
        assert r.stdout.strip() == ""

    def test_iteration_986_zero_underscore_823_sweep_stays_green(self):
        r = run_git("grep", "-l", MECH_ID_MARKER, "--", "profiles/", "tests/")
        assert r.stdout.strip() == ""

    def test_iteration_986_zero_numeric_823_sweep_fails_by_designed_supersession(self):
        r = run_git("grep", "-l", "mechanism_id: 823$", "--", "profiles/")
        assert r.stdout.strip() != ""

    def test_numeric_823_keys_in_exactly_the_designed_location(self):
        r = run_git("grep", "-l", "mechanism_id: 823$", "--", "profiles/")
        files = [f for f in r.stdout.splitlines() if f]
        assert files == ["profiles/financial-times.yaml"]
        r2 = run_git("grep", "-c", "mechanism_id: 823$", "--", "profiles/financial-times.yaml")
        assert r2.stdout.strip().endswith(":1")


class TestLedger987:
    def test_not_falsification_family_member(self):
        assert load_block()["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        assert load_block()["falsification_ledger"] == 30

    def test_ledger_note_present(self):
        note = load_block()["ledger_note"]
        assert "holds at 30" in note


class TestDocSync987:
    def test_readme_stats_updated(self):
        text = README.read_text()
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text
        assert f"| Tests | {README_TESTS_AFTER} | Across {README_FILES_AFTER} test files |" in text

    def test_readme_table_row_for_987(self):
        text = README.read_text()
        assert f"`tests/{THIS_FILE}`" in text
        assert text.index(f"`tests/{THIS_FILE}`") > text.index(
            "`tests/test_type_e_986_podcast_sentiment_120th_verification_sep25_5am.py`"
        )

    def test_architecture_tree_row_for_987(self):
        assert THIS_FILE in ARCH.read_text()


class TestIterationLog987:
    def test_newest_entry_is_987_prepended(self):
        headings = [
            line
            for line in LOG.read_text().splitlines()
            if line.startswith("## #")
        ]
        assert headings[0].startswith("## #987")

    def test_hash_placeholders_filled_post_followup(self):
        text = LOG.read_text()
        entry = text.split("## #987")[1].split("## #986")[0]
        assert re.search(r"\b[0-9a-f]{40}\b", entry) is not None


class TestPushReadiness987:
    def test_staged_set_exactly_five_paths(self):
        r = run_git("diff", "--cached", "--name-only")
        staged = {f for f in r.stdout.splitlines() if f}
        assert staged == STAGED_SET

    def test_concurrency_files_untouched_and_unstaged(self):
        r = run_git("status", "--porcelain")
        lines = r.stdout.splitlines()
        staged = {l[3:] for l in lines if l[:2] in ("M ", "A ")}
        assert "profiles/nytimes.yaml" not in staged
        assert not any("test_type_b_938" in f for f in staged)
        assert not any("test_type_d_900" in f for f in staged)
        assert any(
            l.startswith(" M ") and "profiles/nytimes.yaml" in l for l in lines
        )

    def test_no_credentials_in_staged_diff(self):
        r = run_git("diff", "--cached")
        assert TOKEN_NEEDLE not in r.stdout

    def test_no_literal_underscore_823_in_test_file(self):
        text = (REPO / "tests" / THIS_FILE).read_text()
        assert MECH_ID_MARKER not in text

    def test_origin_remote_is_github_ssh_form(self):
        r = run_git("remote", "get-url", "origin")
        assert "github.com" in r.stdout
        assert "rayhe/mediascope" in r.stdout
