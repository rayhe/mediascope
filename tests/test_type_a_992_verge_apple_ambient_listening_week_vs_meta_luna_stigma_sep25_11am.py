"""Type A #992 (2026-09-25 11:00 PDT): The Verge x Apple ambient-listening
register week (Sep 9-24, 2026) vs The Verge x Meta carried Luna stigma arm.
Third leg of the 990-994 window (D #990 -> E #991 -> A #992 -> B #993 -> C #994).

Apple arm (NEW this run, n=2): (1) Sep 9, 2026 "Read the Apple document
explaining how new listening features still protect your privacy"
(https://www.theverge.com/tech/992919/apple-siri-ai-audio-intelligence-privacy)
- company-briefed privacy-defense register relaying Apple's own Siri Recap /
Live Rewind / Audio Intelligence document, MANUAL ILLUSTRATIVE +0.10;
(2) Sep 24, 2026 "Everything is spying on you and there's no opting out"
(Janus Rose, The Verge, via WeSearch) - privacy-skeptical blowback register,
MANUAL ILLUSTRATIVE -0.30.
Meta arm (CARRIED from mechanism 794 / Type B #938, un-rescored per #807):
Dominic Preston Sep 16, 2026 "Meta is reportedly ready to launch less pervy
smart glasses" (https://www.theverge.com/tech/996138/meta-luna-ray-ban-smart-glasses-camera-free-connect),
"pervert glasses" stigma vocabulary, MANUAL ILLUSTRATIVE -0.30.
Apple arm average -0.10; illustrative Apple-minus-Meta delta +0.20 - directionally
consistent with but NARROWER than m646's launch-window +0.73 (temporal BOUND on
m646 under the shared ambient-listening peg). The Sep-24 Apple-skeptical arm is
counter-evidence: The Verge's watchdog capacity is not Apple-gated (parallels
m643's FT control); the softest Apple item is a briefing-relay genre artifact.

Statistical discipline per the Aug 28 2026 standing rule: MANUAL ILLUSTRATIVE
scores only, p_value/cohens_d/ci NOT_CALCULATED, is_significant False, engine
NOT run at the finding layer; verdict directionally_supported_not_proven; no
analysis.json update; NOT artifact-grade; NOT falsification-family member;
ledger holds at 30.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4
(patched green in the anchor followup). Doc-sync 3 fail pre-commit per #719,
all green post-doc-sync; iteration-log hash-placeholder test fails pre-commit
per the #721 convention.
38 tests, 10 classes. ASCII only, no em dashes.
"""

import re
import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
PROFILE = REPO / "profiles" / "the-verge.yaml"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"
LOG = REPO / "iteration-log.md"
THIS_FILE = Path(__file__).name

ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched green in the anchor followup per #565

ITERATION = 992
MECHANISM = 826
BLOCK_KEY = (
    "type_a_992_verge_apple_ambient_listening_week_vs_meta_luna_stigma_sep25_2026"
)

NEW_URLS = [
    "https://www.theverge.com/tech/992919/apple-siri-ai-audio-intelligence-privacy",
    "https://wesearch.press/s/everything-is-spying-on-you-and-there-s-no-opting-out-657c98f3",
]

CARRIED_URLS = [
    "https://www.theverge.com/tech/996138/meta-luna-ray-ban-smart-glasses-camera-free-connect",
]

CONNECTS_TO = [646, 794, 811, 643, 628]

EXPECTED_TESTS = 38
README_TESTS_BEFORE, README_TESTS_AFTER = 51017, 51055
README_FILES_BEFORE, README_FILES_AFTER = 1316, 1317

MECH_ID_MARKER = "mechanism" + "_826"
NEXT_ID_MARKER = "mechanism" + "_827"
TOKEN_NEEDLE = "x-access" + "-token"

STAGED_SET = {
    "profiles/the-verge.yaml",
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
    return data["competitor_relationships"]["apple"][BLOCK_KEY]


class TestNovelty992:
    def test_single_type_a_992_test_file(self):
        files = sorted((REPO / "tests").glob("test_type_a_992*.py"))
        assert [f.name for f in files] == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type A #992" in r2.stdout

    def test_novelty_claim_present_in_block(self):
        block = load_block()
        assert "Two new URL keys" in block["novelty"]
        assert "first corpus appearance" in block["novelty"]


class TestRotationCycleGuard992:
    @pytest.mark.rotation
    def test_third_leg_of_990_to_994_window(self):
        text = LOG.read_text()
        assert "## #990" in text and "Type D" in text
        assert "## #991" in text and "Type E" in text
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "A"

    @pytest.mark.rotation
    def test_predecessor_991_type_e_committed(self):
        r = run_git("log", "--oneline", "--grep=#991")
        assert r.stdout.strip() != ""
        assert (REPO / "tests" / "test_type_e_991_podcast_sentiment_121st_verification_sep25_10am.py").exists()

    @pytest.mark.rotation
    def test_no_successor_993_type_b_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type B #993")
        assert r.stdout.strip() == ""
        assert "## #993" not in LOG.read_text()

    @pytest.mark.rotation
    def test_no_concurrent_in_flight_type_a_992_by_commit_time(self):
        r = run_git("log", "--oneline", "--grep=Type A #992")
        assert r.stdout.strip() == ""


class TestMechanism826Content:
    def test_block_key_unique_at_indent_4_under_apple(self):
        hits = [
            line
            for line in PROFILE.read_text().splitlines()
            if line == f"    {BLOCK_KEY}:"
        ]
        assert len(hits) == 1

    def test_mechanism_id_826_iteration_992_type_a(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "A"
        assert block["type"] == "Type A - Competitor Coverage Deep Dive"
        assert block["publication_pair"] == "Verge x Apple"
        assert block["competitor"] == "apple"

    def test_two_new_urls_first_appearance(self):
        for url in NEW_URLS:
            assert url in yaml.safe_dump(load_block()), url
            r = run_git("grep", "-l", "-F", url, "--", "profiles/")
            assert [f for f in r.stdout.splitlines() if f] == [
                "profiles/the-verge.yaml"
            ], url

    def test_carried_url_present_in_block(self):
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

    def test_finding_mentions_bound_and_counterevidence(self):
        finding = load_block()["finding"]
        assert "BOUND on the m646 finding" in finding or "temporal BOUND" in finding
        assert "watchdog capacity is not Apple-gated" in finding
        assert "Correlation only" in finding


class TestAsymmetryScorerMath:
    def test_delta_math(self):
        block = load_block()
        scorer = block["asymmetry_scorer_result"]
        assert abs(scorer["apple_avg"] - (-0.1)) < 1e-9
        assert abs(scorer["meta_avg"] - (-0.3)) < 1e-9
        assert abs(scorer["delta_apple_minus_meta"] - 0.2) < 1e-9
        assert (
            abs(
                (scorer["apple_avg"] - scorer["meta_avg"])
                - scorer["delta_apple_minus_meta"]
            )
            < 1e-9
        )

    def test_tones_manual_illustrative_only(self):
        block = load_block()
        assert "MANUAL ILLUSTRATIVE" in block["manual_illustrative_tones_note"]
        assert block["asymmetry_scorer_result"]["artifact_grade"] is False

    def test_scorer_fields_present(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert scorer["target_entity"] == "apple"
        assert scorer["reference_entity"] == "meta"
        assert scorer["publication"] == "the-verge"
        assert "interpretation" in scorer
        assert "limitations" in scorer


class TestStatisticalDiscipline992:
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


class TestSupersessionAndCorpusPost991:
    def test_corpus_max_mechanism_id_is_826(self):
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
        assert ids[-1] == 826

    def test_iteration_991_max_825_sweep_superseded_by_design(self):
        r = run_git("grep", "-l", "mechanism_id: 825$", "--", "profiles/")
        assert r.stdout.strip() != ""
        r2 = run_git("grep", "-l", "mechanism_id: 826$", "--", "profiles/")
        assert r2.stdout.strip() != ""

    def test_zero_underscore_827_repo_wide(self):
        r = run_git("grep", "-l", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_numeric_827_in_profiles(self):
        r = run_git("grep", "-l", "mechanism_id: 827$", "--", "profiles/")
        assert r.stdout.strip() == ""

    def test_iteration_991_zero_underscore_826_sweep_stays_green(self):
        r = run_git("grep", "-l", MECH_ID_MARKER, "--", "profiles/", "tests/")
        assert r.stdout.strip() == ""

    def test_iteration_991_zero_numeric_826_sweep_fails_by_designed_supersession(self):
        r = run_git("grep", "-l", "mechanism_id: 826$", "--", "profiles/")
        assert r.stdout.strip() != ""

    def test_numeric_826_keys_in_exactly_the_designed_location(self):
        r = run_git("grep", "-l", "mechanism_id: 826$", "--", "profiles/")
        files = [f for f in r.stdout.splitlines() if f]
        assert files == ["profiles/the-verge.yaml"]
        r2 = run_git("grep", "-c", "mechanism_id: 826$", "--", "profiles/the-verge.yaml")
        assert r2.stdout.strip().endswith(":1")


class TestLedger992:
    def test_not_falsification_family_member(self):
        assert load_block()["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        assert load_block()["falsification_ledger"] == 30

    def test_ledger_note_present(self):
        note = load_block()["falsification_note"]
        assert "holds at 30" in note


class TestDocSync992:
    def test_readme_stats_updated(self):
        text = README.read_text()
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text
        assert f"| Tests | {README_TESTS_AFTER} | Across {README_FILES_AFTER} test files |" in text

    def test_readme_table_row_for_992(self):
        text = README.read_text()
        assert f"`tests/{THIS_FILE}`" in text
        assert text.index(f"`tests/{THIS_FILE}`") > text.index(
            "`tests/test_type_e_991_podcast_sentiment_121st_verification_sep25_10am.py`"
        )

    def test_architecture_tree_row_for_992(self):
        assert THIS_FILE in ARCH.read_text()


class TestIterationLog992:
    def test_newest_entry_is_992_prepended(self):
        headings = [
            line
            for line in LOG.read_text().splitlines()
            if line.startswith("## #")
        ]
        assert headings[0].startswith("## #992")

    def test_hash_placeholders_filled_post_followup(self):
        text = LOG.read_text()
        entry = text.split("## #992")[1].split("## #991")[0]
        assert re.search(r"\b[0-9a-f]{40}\b", entry) is not None


class TestPushReadiness992:
    def test_staged_set_exactly_five_paths(self):
        r = run_git("diff", "--cached", "--name-only")
        staged = {f for f in r.stdout.splitlines() if f}
        assert staged == STAGED_SET

    def test_concurrency_files_untouched_and_unstaged(self):
        r = run_git("status", "--porcelain")
        lines = r.stdout.splitlines()
        staged = {l[3:] for l in lines if l[:2] in ("M ", "A ")}
        assert "profiles/nytimes.yaml" not in staged
