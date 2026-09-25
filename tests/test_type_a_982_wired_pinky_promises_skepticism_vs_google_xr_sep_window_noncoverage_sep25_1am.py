"""Type A #982 (2026-09-25 01:00 PDT): WIRED Sep-23 Pinky-Promises privacy
skepticism vs Google XR Sep-window non-coverage - Connect-week Meta alarm
cluster against continued Google camera-glasses silence. Third leg of the
980-984 window (D #980 -> E #981 -> A #982 -> B #983 -> C #984).

Meta arm (carried from mechanism #814, in-corpus mirror attestation): WIRED
Sep 23, 2026 "Meta Pinky Promises Its Smart Glasses Will Be Private Soon"
(Boone Ashworth) - skeptical register on Meta's privacy-POSITIVE Connect
announcement, headline frames the Private Processing pledge as a dubious
"pinky promise", no firm timeline - MANUAL ILLUSTRATIVE -0.45. Google arm
(new evidence this run): WIRED published zero Google XR camera-glasses pieces
in the same window despite fresh peer-covered news pegs - Snapdragon Summit
Sep 23 2026 (Google confirms Gemini eyewear from Gentle Monster and Warby
Parker will run on Snapdragon AR1, the-gadgeteer.com), Samsung Unpacked Jul
2026 Android XR details (camera, ~9hr battery, fall launch, thurrott.com),
Warby Parker partnership confirmation (chainstoreage.com), I/O 2026 audio
glasses (digitaltrends.com) - 4 new URLs. Positive control (carried from
mechanism #640): WIRED's May 19, 2026 hands-on Android XR piece proves WIRED
covers Google XR glasses enthusiastically (+0.15) when it chooses to, so the
Sep-window absence is a selection signal, not a beat gap. Silence documented
in mechanism #547 (Sep 5) extends 20 days to Sep 25, spanning WIRED's heaviest
Meta-wearables coverage week.

Illustrative delta (Meta minus Google): -0.45 - 0.15 = -0.60, n=1 vs carried
baseline, NOT significant. EXTENDS m547 (silence strand) and m640 (register
inversion); distinct from m814 (Snap comparator, WIRED x Snap section).
Connects [547, 640, 431, 814, 452, 612].

Statistical discipline per the Aug 28 2026 standing rule: MANUAL ILLUSTRATIVE
scores only, p_value/cohens_d/ci NOT_CALCULATED, is_significant False, engine
NOT run at the finding layer; verdict directionally_supported_not_proven; no
analysis.json update; NOT artifact-grade; NOT falsification-family member;
ledger holds at 30.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4
(patched green in the anchor followup). Doc-sync 3 + iteration-log 2 fail
pre-commit per #719, all green post-doc-sync.
42 tests, 10 classes. ASCII only, no em dashes.
"""

import re
import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
PROFILE = REPO / "profiles" / "wired.yaml"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"
LOG = REPO / "iteration-log.md"
THIS_FILE = Path(__file__).name

ANCHORED_SHA = "123b54a88a90b924157e203c9d0fb768dedeecaa"

ITERATION = 982
MECHANISM = 820
BLOCK_KEY = (
    "wired_sep23_pinky_promises_privacy_skepticism_vs_google_xr_"
    "sep_window_noncoverage_sep25_2026"
)

NEW_URLS = [
    "https://the-gadgeteer.com/2026/09/23/snapdragon-summit-2026-qualcomm-puts-ai-agents-on-smart-glasses/",
    "https://www.thurrott.com/hardware/339507/samsung-details-upcoming-smart-glasses-developed-with-gentle-monster-and-warby-parker",
    "https://chainstoreage.com/warby-parker-partners-google-samsung-new-smart-glasses",
    "https://www.digitaltrends.com/home-theater/google-shows-off-android-audio-glasses-designed-by-gentle-monster-and-warby-parker/",
]

CARRIED_URLS = [
    "https://www.aob-news.com/2026/09/23/meta-pinky-promises-its-smart-glasses-will-be-private-soon/",
    "https://www.wired.com/story/hands-on-with-all-of-google-new-upcoming-android-xr-smart-glasses/",
]

CONNECTS_TO = [547, 640, 431, 814, 452, 612]

EXPECTED_TESTS = 42
README_TESTS_BEFORE, README_TESTS_AFTER = 50534, 50576
README_FILES_BEFORE, README_FILES_AFTER = 1306, 1307

MECH_ID_MARKER = "mechanism" + "_820"
NEXT_ID_MARKER = "mechanism" + "_821"
TOKEN_NEEDLE = "x-access" + "-token"

STAGED_SET = {
    "profiles/wired.yaml",
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
    return data["competitor_relationships"]["google"][BLOCK_KEY]


class TestNovelty982:
    def test_single_type_a_982_test_file(self):
        files = sorted((REPO / "tests").glob("test_type_a_982*.py"))
        assert [f.name for f in files] == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type A #982" in r2.stdout

    def test_novelty_claim_present_in_block(self):
        novelty = load_block()["novelty"]
        assert "Pinky Promises" in novelty
        assert "20 days" in novelty
        assert "4 new URLs" in novelty


class TestRotationCycleGuard982:
    @pytest.mark.rotation
    def test_third_leg_of_980_to_984_window(self):
        text = LOG.read_text()
        assert "## #980" in text and "Type D" in text
        assert "## #981" in text and "Type E" in text
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "A"

    @pytest.mark.rotation
    def test_predecessor_981_type_e_committed(self):
        r = run_git("log", "--oneline", "--grep=#981")
        assert r.stdout.strip() != ""
        assert (REPO / "tests" / "test_type_e_981_podcast_sentiment_119th_verification_sep25_12am.py").exists()

    @pytest.mark.rotation
    def test_no_successor_983_type_b_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type B #983")
        assert r.stdout.strip() == ""
        assert "## #983" not in LOG.read_text()

    @pytest.mark.rotation
    def test_no_concurrent_in_flight_type_a_982_by_commit_time(self):
        r = run_git("log", "--oneline", "--grep=Type A #982")
        assert r.stdout.strip() == ""


class TestMechanism820Content:
    def test_block_key_unique_at_indent_4_under_google(self):
        hits = [
            line
            for line in PROFILE.read_text().splitlines()
            if line == f"    {BLOCK_KEY}:"
        ]
        assert len(hits) == 1

    def test_mechanism_id_820_iteration_982_type_a(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "A"
        assert block["type"] == "Type A - Competitor Coverage Deep Dive"
        assert block["goal_id"] == "goal_54093bda4145"

    def test_four_new_urls_first_appearance(self):
        for url in NEW_URLS:
            assert url in PROFILE.read_text()
            r = run_git("grep", "-c", "-F", url, "--", "profiles/")
            assert r.stdout.strip().endswith(":1"), url

    def test_carried_urls_present_in_block(self):
        text = PROFILE.read_text()
        for url in CARRIED_URLS:
            assert url in text

    def test_connects_to_all_exist(self):
        for m in CONNECTS_TO:
            r = run_git("grep", "-l", f"mechanism_id: {m}$", "--", "profiles/")
            assert r.stdout.strip() != "", m
        assert load_block()["connects_to"] == CONNECTS_TO

    def test_verdict_directionally_supported_not_proven(self):
        block = load_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["no_analysis_json_update"] is True

    def test_finding_mentions_pinky_promises_and_snapdragon(self):
        finding = load_block()["finding"]
        assert "Pinky Promises" in finding
        assert "Snapdragon Summit" in finding
        assert "correlation" in finding.lower()

    def test_positive_control_may19_hands_on_cited(self):
        finding = load_block()["finding"]
        assert "May 19, 2026" in finding
        assert "positive control" in finding.lower()


class TestAsymmetryScorerMath:
    def test_delta_math(self):
        block = load_block()
        scorer = block["asymmetry_scorer_result"]
        assert abs(scorer["target_avg"] - (-0.45)) < 1e-9
        assert abs(scorer["reference_avg"] - 0.15) < 1e-9
        assert abs(scorer["delta_meta_minus_google"] - (-0.6)) < 1e-9
        assert (
            abs(
                (scorer["target_avg"] - scorer["reference_avg"])
                - scorer["delta_meta_minus_google"]
            )
            < 1e-9
        )

    def test_tones_manual_illustrative_only(self):
        block = load_block()
        assert "MANUAL ILLUSTRATIVE" in block["manual_illustrative_tones_note"]
        assert block["asymmetry_scorer_result"]["artifact_grade"] is False

    def test_scorer_fields_present(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert scorer["target_entity"] == "meta"
        assert scorer["reference_entity"] == "google"
        assert scorer["publication"] == "wired"
        assert "interpretation" in scorer
        assert "limitations" in scorer


class TestStatisticalDiscipline982:
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


class TestSupersessionAndCorpusPost981:
    def test_corpus_max_mechanism_id_is_820(self):
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
        assert ids[-1] == 820

    def test_iteration_981_max_819_sweep_superseded_by_design(self):
        r = run_git("grep", "-l", "mechanism_id: 819$", "--", "profiles/")
        assert r.stdout.strip() != ""
        r2 = run_git("grep", "-l", "mechanism_id: 820$", "--", "profiles/")
        assert r2.stdout.strip() != ""

    def test_zero_underscore_821_repo_wide(self):
        r = run_git("grep", "-l", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_numeric_821_in_profiles(self):
        r = run_git("grep", "-l", "mechanism_id: 821$", "--", "profiles/")
        assert r.stdout.strip() == ""

    def test_iteration_981_zero_underscore_820_sweep_stays_green(self):
        r = run_git("grep", "-l", MECH_ID_MARKER, "--", "profiles/", "tests/")
        assert r.stdout.strip() == ""

    def test_iteration_981_zero_numeric_820_sweep_fails_by_designed_supersession(self):
        r = run_git("grep", "-l", "mechanism_id: 820$", "--", "profiles/")
        assert r.stdout.strip() != ""

    def test_numeric_820_keys_in_exactly_the_designed_location(self):
        r = run_git("grep", "-l", "mechanism_id: 820$", "--", "profiles/")
        files = [f for f in r.stdout.splitlines() if f]
        assert files == ["profiles/wired.yaml"]
        r2 = run_git("grep", "-c", "mechanism_id: 820$", "--", "profiles/wired.yaml")
        assert r2.stdout.strip().endswith(":1")


class TestLedger982:
    def test_not_falsification_family_member(self):
        assert load_block()["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        assert load_block()["falsification_ledger"] == 30

    def test_ledger_note_present(self):
        note = load_block()["ledger_note"]
        assert "holds at 30" in note


class TestDocSync982:
    def test_readme_stats_updated(self):
        text = README.read_text()
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text
        assert f"| Tests | {README_TESTS_AFTER} | Across {README_FILES_AFTER} test files |" in text

    def test_readme_table_row_for_982(self):
        text = README.read_text()
        assert f"`tests/{THIS_FILE}`" in text
        assert text.index(f"`tests/{THIS_FILE}`") > text.index(
            "`tests/test_type_e_981_podcast_sentiment_119th_verification_sep25_12am.py`"
        )

    def test_architecture_tree_row_for_982(self):
        assert THIS_FILE in ARCH.read_text()


class TestIterationLog982:
    def test_newest_entry_is_982_prepended(self):
        headings = [
            line
            for line in LOG.read_text().splitlines()
            if line.startswith("## #")
        ]
        assert headings[0].startswith("## #982")

    def test_hash_placeholders_filled_post_followup(self):
        text = LOG.read_text()
        entry = text.split("## #982")[1].split("## #981")[0]
        assert re.search(r"\b[0-9a-f]{40}\b", entry) is not None


class TestPushReadiness982:
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

    def test_no_literal_underscore_820_in_test_file(self):
        text = (REPO / "tests" / THIS_FILE).read_text()
        assert MECH_ID_MARKER not in text

    def test_origin_remote_is_github_ssh_form(self):
        r = run_git("remote", "get-url", "origin")
        assert "github.com" in r.stdout
        assert "rayhe/mediascope" in r.stdout
