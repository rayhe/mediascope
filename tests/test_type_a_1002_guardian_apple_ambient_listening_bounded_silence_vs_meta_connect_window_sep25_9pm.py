"""Type A #1002 (2026-09-25 21:00 PDT): The Guardian x Apple Sep-2026
ambient-listening bounded silence vs Guardian x Meta police-memo investigation
+ Connect stigma register. Third leg of the 1000-1004 window (D #1000 ->
E #1001 -> A #1002).

NEW finding (coverage SELECTION, mechanism 832): in the Sep-2026 wearables
event window the Guardian ran TWO Meta arms - (1) a Sep-8 FOIA-driven
investigative piece, "internal documents reviewed by The Guardian," framing
Ray-Ban Meta glasses as a covert-recording security threat (NYPD
counterterrorism memo, DHS/fusion-center memos, ICE ban; MANUAL ILLUSTRATIVE
-0.75), and (2) a Sep-24 Connect piece by its own consumer-technology editor
Samuel Gibbs keeping the "perv glasses"/"spy glasses" stigma register on the
camera-free Ray-Ban Meta Audio (MANUAL ILLUSTRATIVE -0.20) - while Apple drew
bounded silence: ZERO Guardian UK authored pieces on Apple's Sep-9
always-listening Audio Intelligence (Siri Recap all-day ambient conversation
summaries; Live Rewind 15-second conversation buffer) across 6 search query
sets. Temporal replication of the m607 zero-financial-gradient control
(Sep-9 review-register gap), now on coverage SELECTION rather than review
register. The selection asymmetry (2 Meta arms vs 0 Apple arms) is the
finding; no magnitude delta is computed (Apple arm NOT_SCORED, delta
NOT_COMPUTED). Four new verbatim URL keys (enmnews Sep-8 relay, ainvest
exhibit, genztech timeline, globalcommunityweekly Gibbs relay); petapixel
Sep-9 relay carried as in-corpus corroboration.

Statistical discipline per the Aug 28 2026 standing rule: MANUAL ILLUSTRATIVE
scores only, p_value/cohens_d/ci NOT_CALCULATED, is_significant False, engine
NOT run at the finding layer; verdict directionally_supported_not_proven; no
analysis.json update; NOT artifact-grade; NOT falsification-family member;
ledger holds at 30. Excerpt-bounded per #503 (0 browser.open);
theguardian.com policy-blocked, mirror-attributed only. Correlation is not
causation. Hypothesis-generating only. ASCII-only, no em dashes.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4
(patched green in the anchor followup). Doc-sync 3 fail pre-commit per #719,
all green post-doc-sync; iteration-log newest-entry green; hash-placeholder
test fails pre-commit per the #721 convention; staged-set test fails pre-commit
by design.
41 tests, 10 classes. ASCII only, no em dashes.
"""

import re
import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
PROFILE = REPO / "profiles" / "guardian.yaml"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"
LOG = REPO / "iteration-log.md"
THIS_FILE = Path(__file__).name

ANCHORED_SHA = "1c858d9b"  # patched green in the anchor followup per #565

ITERATION = 1002
MECHANISM = 832
BLOCK_KEY = (
    "type_a_1002_guardian_apple_ambient_listening_sep2026_bounded_silence_"
    "vs_meta_police_memo_connect_stigma_register_sep25_2026"
)

NEW_URLS = [
    "https://enmnews.com/2026/09/08/police-across-us-sound-alarm-over-meta-smart-glasses-covert-recording-threat",
    "https://www.ainvest.com/news/exhibit-memos-renamed-meta-glasses-surveillance-device-2609/",
    "https://genztech.blog/p/nypd-dhs-memos-meta-ray-ban-glasses-security-threat/",
    "https://globalcommunityweekly.substack.com/p/meta-debuts-no-camera-smart-glasses",
]

CARRIED_URLS = [
    "https://petapixel.com/2026/09/09/us-police-warn-meta-smart-glasses-could-be-a-security-threat/",
    "http://richardhartley.com/2024/08/vision-pro-review-apples-cutting-edge-headset-lives-up-to-the-hype/",
    "https://www.theguardian.com/technology/2024/jan/30/apple-vision-pro-reviews-roundup-stunning-potential-with-big-trade-offs",
    "https://www.youtube.com/shorts/Cb8gV-uNBnM",
]

CONNECTS_TO = [607, 537, 826, 830, 827]

EXPECTED_TESTS = 41
README_TESTS_BEFORE, README_TESTS_AFTER = 51509, 51550
README_FILES_BEFORE, README_FILES_AFTER = 1326, 1327

MECH_ID_MARKER = "mechanism" + "_832"
NEXT_ID_MARKER = "mechanism" + "_833"
NEXT_DASH_MARKER = "mechanism" + "-833"
TOKEN_NEEDLE = "x-access" + "-token"

STAGED_SET = {
    "profiles/guardian.yaml",
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


class TestNovelty1002:
    def test_single_type_a_1002_test_file(self):
        files = sorted((REPO / "tests").glob("test_type_a_1002*.py"))
        assert [f.name for f in files] == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type A #1002" in r2.stdout

    def test_novelty_claim_present_in_block(self):
        block = load_block()
        assert "FIRST corpus mechanism on the Sep-2026 Guardian Apple ambient-listening coverage-selection asymmetry" in block["novelty"]


class TestRotationCycleGuard1002:
    @pytest.mark.rotation
    def test_third_leg_of_1000_to_1004_window(self):
        text = LOG.read_text()
        assert "## #1000" in text and "Type D" in text
        assert "## #1001" in text and "Type E" in text
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "A"

    @pytest.mark.rotation
    def test_predecessor_1001_type_e_committed(self):
        r = run_git("log", "--oneline", "--grep=#1001")
        assert r.stdout.strip() != ""
        assert (REPO / "tests" / "test_type_e_1001_podcast_sentiment_123rd_verification_sep25_8pm.py").exists()

    @pytest.mark.rotation
    def test_no_successor_1003_type_b_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type B #1003")
        assert r.stdout.strip() == ""
        assert "## #1003" not in LOG.read_text()

    @pytest.mark.rotation
    def test_no_concurrent_in_flight_type_a_1002_by_commit_time(self):
        r = run_git("log", "--format=%H %s", "--grep=Type A #1002")
        matches = [l for l in r.stdout.splitlines() if l.strip()]
        own = run_git("log", "--format=%H", "--", f"tests/{THIS_FILE}").stdout.splitlines()
        competing = [l for l in matches if l.split()[0] not in own]
        assert competing == [], f"concurrent Type A #1002 commits: {competing}"


class TestMechanism832Content:
    def test_block_key_unique_at_indent_4_under_apple(self):
        hits = [
            line
            for line in PROFILE.read_text().splitlines()
            if line == f"    {BLOCK_KEY}:"
        ]
        assert len(hits) == 1

    def test_mechanism_id_832_iteration_1002_type_a(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "A"
        assert block["type"] == "Type A - Competitor Coverage Deep Dive"
        assert block["publication_pair"] == "Guardian x Apple"
        assert block["competitor"] == "apple"

    def test_new_urls_first_appearance(self):
        for url in NEW_URLS:
            assert url in yaml.safe_dump(load_block()), url
            r = run_git("grep", "-l", "-F", url, "--", "profiles/")
            assert [f for f in r.stdout.splitlines() if f] == [
                "profiles/guardian.yaml"
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

    def test_finding_mentions_replication_and_selection(self):
        finding = load_block()["finding"]
        assert "REPLICATES m607" in finding
        assert "coverage-SELECTION" in finding
        assert "Correlation only" in finding

    def test_apple_bounded_absence_documented(self):
        absence = load_block()["apple_side_bounded_absence"]
        assert "ZERO Guardian UK authored pieces" in absence["claim"]
        assert len(absence["query_sets"]) == 5
        assert len(absence["meta_angled_corroboration_sets"]) == 3
        assert "bounded silence, not proof of non-publication" in absence["absence_bound"]


class TestAsymmetryScorerSelection1002:
    def test_meta_avg_minus_0_475(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert abs(scorer["meta_avg"] - (-0.475)) < 1e-9
        assert load_block()["manual_illustrative_tones_meta"] == [-0.75, -0.20]

    def test_target_not_scored_bounded_absence(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert scorer["target_avg"] == "NOT_SCORED_BOUNDED_ABSENCE"
        assert scorer["target_entity"] == "apple"

    def test_delta_not_computed_selection_asymmetry(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert scorer["delta_target_minus_meta"] == "NOT_COMPUTED_SELECTION_ASYMMETRY"
        assert "selection" in scorer["interpretation"].lower()

    def test_tones_manual_illustrative_only(self):
        block = load_block()
        assert "MANUAL ILLUSTRATIVE" in block["manual_illustrative_tones_note"]
        assert block["asymmetry_scorer_result"]["artifact_grade"] is False

    def test_scorer_fields_present(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert scorer["reference_entity"] == "meta"
        assert scorer["publication"] == "the-guardian"
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        assert "interpretation" in scorer
        assert "limitations" in scorer


class TestStatisticalDiscipline1002:
    def test_p_value_not_calculated(self):
        block = load_block()
        assert block["p_value"] == "NOT_CALCULATED"
        assert block["cohens_d"] == "NOT_CALCULATED"
        assert block["is_significant"] is False

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


class TestSupersessionAndCorpusPost1001:
    def test_corpus_max_mechanism_id_is_832(self):
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
        assert ids[-1] == 832

    def test_iteration_1000_max_831_sweep_superseded_by_design(self):
        r = run_git("grep", "-l", "mechanism_id: 831$", "--", "profiles/")
        assert r.stdout.strip() != ""
        r2 = run_git("grep", "-l", "mechanism_id: 832$", "--", "profiles/")
        assert r2.stdout.strip() != ""

    def test_zero_underscore_833_repo_wide(self):
        r = run_git("grep", "-l", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_dash_833_repo_wide(self):
        r = run_git("grep", "-l", NEXT_DASH_MARKER, "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_numeric_833_in_profiles(self):
        r = run_git("grep", "-l", "mechanism_id: 833$", "--", "profiles/")
        assert r.stdout.strip() == ""

    def test_iteration_1000_zero_numeric_832_sweep_fails_by_designed_supersession(self):
        r = run_git("grep", "-l", "mechanism_id: 832$", "--", "profiles/")
        assert r.stdout.strip() != ""

    def test_numeric_832_keys_in_exactly_the_designed_location(self):
        r = run_git("grep", "-l", "mechanism_id: 832$", "--", "profiles/")
        files = [f for f in r.stdout.splitlines() if f]
        assert files == ["profiles/guardian.yaml"]
        r2 = run_git("grep", "-c", "mechanism_id: 832$", "--", "profiles/guardian.yaml")
        assert r2.stdout.strip().endswith(":1")


class TestLedger1002:
    def test_not_falsification_family_member(self):
        assert load_block()["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        assert load_block()["falsification_ledger"] == 30

    def test_ledger_note_present(self):
        note = load_block()["falsification_note"]
        assert "holds at 30" in note


class TestDocSync1002:
    def test_readme_stats_updated(self):
        text = README.read_text()
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text
        assert f"| Tests | {README_TESTS_AFTER} | Across {README_FILES_AFTER} test files |" in text

    def test_readme_table_row_for_1002(self):
        text = README.read_text()
        assert f"`tests/{THIS_FILE}`" in text
        assert text.index(f"`tests/{THIS_FILE}`") > text.index(
            "`tests/test_type_e_1001_podcast_sentiment_123rd_verification_sep25_8pm.py`"
        )

    def test_architecture_tree_row_for_1002(self):
        assert THIS_FILE in ARCH.read_text()


class TestIterationLog1002:
    def test_newest_entry_is_1002_prepended(self):
        headings = [
            line
            for line in LOG.read_text().splitlines()
            if line.startswith("## #")
        ]
        assert headings[0].startswith("## #1002")

    def test_hash_placeholders_filled_post_followup(self):
        text = LOG.read_text()
        entry = text.split("## #1002")[1].split("## #1001")[0]
        assert re.search(r"\b[0-9a-f]{40}\b", entry) is not None


class TestPushReadiness1002:
    def test_staged_set_exactly_five_paths(self):
        r = run_git("diff", "--cached", "--name-only")
        staged = {f for f in r.stdout.splitlines() if f}
        assert staged == STAGED_SET

    def test_concurrency_files_untouched_and_unstaged(self):
        r = run_git("status", "--porcelain")
        lines = r.stdout.splitlines()
        staged = {l[3:] for l in lines if l[:2] in ("M ", "A ")}
        assert "profiles/nytimes.yaml" not in staged
