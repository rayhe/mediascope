"""Type B #1003 (2026-09-25 22:00 PDT): James Pero (Gizmodo) Sep-2026 Snap Specs
ear-bending comedy feature - STIGMA-REGISTER ROUTING extension of mechanisms
806/791 within the same journalist. Fourth leg of the 1000-1004 window
(D #1000 -> E #1001 -> A #1002 -> B #1003).

NEW arm (n=1, full-text first-hand this run): Gizmodo "Do Snap's Beefy AR
Glasses Actually Bend Your Ears?" (James Pero; September 2026, bounded from
/2026/09/ asset paths and Snap launch-event attendance) - first-person
anatomy-humor hands-on: "do they really bend the sh*t out of your ears?",
"big, chunky, comically large", "a little bit of journalism that nobody
asked for" / "J*ear*nalism", roughly-10-person ear canvass ("everybody said
that it was a no"), one-on-one time with Snap Specs staff including Head of
Specs Studio Ben Feuerstein, engineering sympathy ("Snap has built a
standalone face computer", "miniaturization is hard", the meme as "a silly
representation of a real problem"). Verdict: "weighty but not ear-bendy".
MANUAL ILLUSTRATIVE +0.10: open bulk criticism converted into anatomy comedy,
self-deprecating field reporting, and engineering sympathy; the verdict
gently clears the product. CARRIED comparator (m806 / Type B #958,
un-rescored per #807): Sep-23 Meta Ray-Ban Audio -0.20 (camera-free product,
yet the privacy-accusation frame persists in headline/dek: "Avoid the 'Perv'
Problem", "glasshole"; the objection moves from hardware to brand).
Illustrative Snap-minus-Meta delta +0.30 (0.10 - (-0.20)), same direction as
m791 (-0.65) and the m806 Snap comparison (-0.55): Pero routes Snap's
physical conspicuousness into anatomy humor while Meta's camera-free product
keeps the sexualized public-stigma headline. Bounded by m818 (category-bound
within Meta; no journalist-global hostility claim) and by m746/m933 (the
playful-Snap register itself replicates).

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
40 tests, 10 classes. ASCII only, no em dashes.
"""

import re
import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
PROFILE = REPO / "profiles" / "careers" / "journalists.yaml"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"
LOG = REPO / "iteration-log.md"
THIS_FILE = Path(__file__).name

ANCHORED_SHA = "f17bc65d"  # patched green in the anchor followup per #565

ITERATION = 1003
MECHANISM = 833
BLOCK_KEY = (
    "type_b_1003_james_pero_gizmodo_snap_specs_earbending_comedy_vs_meta_audio_stigma_sep25"
)

NEW_URLS = [
    "https://gizmodo.com/do-snaps-beefy-ar-glasses-actually-bend-your-ears-2000812837",
]

CONNECTS_TO = [806, 791, 746, 818, 211, 269, 743]

EXPECTED_TESTS = 40
README_TESTS_BEFORE, README_TESTS_AFTER = 51550, 51590
README_FILES_BEFORE, README_FILES_AFTER = 1327, 1328

MECH_ID_MARKER = "mechanism" + "_833"
NEXT_ID_MARKER = "mechanism" + "_834"

STAGED_SET = {
    "profiles/careers/journalists.yaml",
    f"tests/{THIS_FILE}",
    "README.md",
    "docs/ARCHITECTURE.md",
    "iteration-log.md",
}

CONCURRENCY_UNTOUCHED = {
    "profiles/nytimes.yaml",
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
}


def run_git(*args):
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, cwd=REPO
    )


def load_block():
    with open(PROFILE) as f:
        data = yaml.safe_load(f)
    return data["james_pero"]["competitor_coverage"][BLOCK_KEY]


class TestNovelty1003:
    def test_single_type_b_1003_test_file(self):
        files = sorted((REPO / "tests").glob("test_type_b_1003*.py"))
        assert [f.name for f in files] == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type B #1003" in r2.stdout

    def test_novelty_claim_present_in_block(self):
        block = load_block()
        assert "FIRST dedicated corpus mechanism" in block["novelty"]
        assert "zero underscore-form 833 mechanism key strings" in block["novelty"]
        assert "NARROWED claim" in block["novelty"]


class TestRotationCycleGuard1003:
    @pytest.mark.rotation
    def test_fourth_leg_of_1000_to_1004_window(self):
        text = LOG.read_text()
        assert "## #1000" in text and "Type D" in text
        assert "## #1001" in text and "Type E" in text
        assert "## #1002" in text and "Type A" in text
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "B"

    @pytest.mark.rotation
    def test_predecessor_1002_type_a_committed(self):
        r = run_git("log", "--oneline", "--grep=#1002")
        assert r.stdout.strip() != ""
        assert (
            REPO
            / "tests"
            / "test_type_a_1002_guardian_apple_ambient_listening_bounded_silence_vs_meta_connect_window_sep25_9pm.py"
        ).exists()

    @pytest.mark.rotation
    def test_no_successor_1004_type_b_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type B #1004")
        assert r.stdout.strip() == ""
        assert "## #1004" not in LOG.read_text()

    @pytest.mark.rotation
    def test_no_concurrent_in_flight_type_b_1003_by_commit_time(self):
        r = run_git("log", "--format=%H %s", "--grep=Type B #1003")
        matches = [l for l in r.stdout.splitlines() if l.strip()]
        own = run_git("log", "--format=%H", "--", f"tests/{THIS_FILE}").stdout.splitlines()
        competing = [l for l in matches if l.split()[0] not in own]
        assert competing == [], f"concurrent Type B #1003 commits: {competing}"


class TestMechanismContent1003:
    def test_block_key_unique_at_indent_4(self):
        hits = [
            line
            for line in PROFILE.read_text().splitlines()
            if line == f"    {BLOCK_KEY}:"
        ]
        assert len(hits) == 1

    def test_mechanism_id_833_iteration_1003_type_b(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "B"
        assert block["type"] == "B"
        assert block["journalist"] == "James Pero"
        assert block["publication"] == "Gizmodo (Keleops AG)"

    def test_new_urls_first_appearance(self):
        for url in NEW_URLS:
            assert url in yaml.safe_dump(load_block()), url
            r = run_git("grep", "-l", "-F", url, "--", "profiles/")
            assert [f for f in r.stdout.splitlines() if f] == [
                "profiles/careers/journalists.yaml"
            ], url

    def test_attested_quotes_in_block(self):
        arm = load_block()["new_snap_arm"]
        assert arm["title"] == "Do Snap's Beefy AR Glasses Actually Bend Your Ears?"
        quotes = " ".join(arm["key_quotes"])
        assert "weighty but not ear-bendy" in quotes
        assert "J*ear*nalism" in quotes
        assert "Ben Feuerstein" in quotes
        assert arm["tone_score"] == 0.10

    def test_carried_meta_arm_806_unrescored(self):
        arm = load_block()["carried_meta_arm"]
        assert arm["mechanism"] == 806
        assert arm["carried_per"] == "#807 (un-rescored)"
        assert arm["tone_score"] == -0.20

    def test_connects_to_all_exist(self):
        for m in CONNECTS_TO:
            r = run_git("grep", "-l", f"mechanism_id: {m}$", "--", "profiles/")
            assert r.stdout.strip() != "", m
        assert load_block()["connects_to"] == CONNECTS_TO

    def test_verdict_directionally_supported_not_proven(self):
        block = load_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["no_analysis_json_update"] is True

    def test_finding_mentions_register_routing_and_delta(self):
        finding = load_block()["finding"]
        assert "anatomy comedy" in finding
        assert "+0.30" in finding
        assert "Correlation only" in finding


class TestAsymmetryScorerMath:
    def test_delta_math(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert abs(scorer["new_snap_arm_tone_manual_illustrative"] - 0.10) < 1e-9
        assert abs(scorer["carried_meta_audio_tone_manual_illustrative"] - (-0.20)) < 1e-9
        assert abs(scorer["illustrative_delta_snap_minus_meta"] - 0.30) < 1e-9
        assert scorer["delta_calc"] == "0.10 - (-0.20) = 0.30"
        assert (
            abs(
                (scorer["new_snap_arm_tone_manual_illustrative"]
                 - scorer["carried_meta_audio_tone_manual_illustrative"])
                - scorer["illustrative_delta_snap_minus_meta"]
            )
            < 1e-9
        )

    def test_tones_manual_illustrative_only(self):
        block = load_block()
        assert "MANUAL ILLUSTRATIVE" in block["manual_illustrative_tones_note"]
        assert block["asymmetry_scorer_result"]["artifact_grade"] is False

    def test_scorer_fields_present(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert scorer["target_entity"] == "snap"
        assert scorer["reference_entity"] == "meta"
        assert scorer["publication"] == "gizmodo"
        assert "interpretation" in scorer
        assert "limitations" in scorer
        assert scorer["statistical_contract"] == "degenerate_n1_per_arm"


class TestStatisticalDiscipline1003:
    def test_p_value_not_calculated(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False

    def test_correlation_not_causation_in_finding(self):
        finding = load_block()["finding"]
        assert "Correlation only" in finding

    def test_confounders_seven_strong_first(self):
        confounders = load_block()["confounders"]
        assert len(confounders) == 7
        assert confounders[0].startswith("[STRONG]")
        assert confounders[1].startswith("[STRONG]")
        assert confounders[2].startswith("[STRONG]")
        assert confounders[3].startswith("[MODERATE]")
        assert confounders[4].startswith("[MODERATE]")
        assert confounders[5].startswith("[WEAK]")
        assert confounders[6].startswith("[WEAK]")

    def test_counterevidence_and_counterargument_present(self):
        block = load_block()
        assert len(block["counterevidence"]) >= 4
        assert len(block["strongest_counterargument"]) > 100


class TestSupersessionAndCorpusPost1002:
    def test_corpus_max_mechanism_id_is_833(self):
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
        assert ids[-1] == 833

    def test_iteration_1002_max_832_sweep_superseded_by_design(self):
        r = run_git("grep", "-l", "mechanism_id: 832$", "--", "profiles/")
        assert r.stdout.strip() != ""
        r2 = run_git("grep", "-l", "mechanism_id: 833$", "--", "profiles/")
        assert r2.stdout.strip() != ""

    def test_zero_underscore_834_repo_wide(self):
        r = run_git("grep", "-l", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_numeric_834_in_profiles(self):
        r = run_git("grep", "-l", "mechanism_id: 834$", "--", "profiles/")
        assert r.stdout.strip() == ""

    def test_iteration_1002_zero_underscore_833_sweep_stays_green(self):
        r = run_git("grep", "-l", MECH_ID_MARKER, "--", "profiles/", "tests/")
        assert r.stdout.strip() == ""

    def test_iteration_1002_zero_numeric_833_sweep_fails_by_designed_supersession(self):
        r = run_git("grep", "-l", "mechanism_id: 833$", "--", "profiles/")
        assert r.stdout.strip() != ""

    def test_numeric_833_keys_in_exactly_the_designed_location(self):
        r = run_git("grep", "-l", "mechanism_id: 833$", "--", "profiles/")
        files = [f for f in r.stdout.splitlines() if f]
        assert files == ["profiles/careers/journalists.yaml"]
        r2 = run_git("grep", "-c", "mechanism_id: 833$", "--", "profiles/careers/journalists.yaml")
        assert r2.stdout.strip().endswith(":1")


class TestLedger1003:
    def test_not_falsification_family_member(self):
        assert load_block()["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        assert load_block()["falsification_ledger"] == 30

    def test_ledger_note_present(self):
        note = load_block()["falsification_note"]
        assert "holds at 30" in note


class TestDocSync1003:
    def test_readme_stats_updated(self):
        text = README.read_text()
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text
        assert f"| Tests | {README_TESTS_AFTER} | Across {README_FILES_AFTER} test files |" in text

    def test_readme_table_row_for_1003(self):
        text = README.read_text()
        assert f"`tests/{THIS_FILE}`" in text
        assert text.index(f"`tests/{THIS_FILE}`") > text.index(
            "`tests/test_type_a_1002_guardian_apple_ambient_listening_bounded_silence_vs_meta_connect_window_sep25_9pm.py`"
        )

    def test_architecture_tree_row_for_1003(self):
        assert THIS_FILE in ARCH.read_text()


class TestIterationLog1003:
    def _entry(self):
        text = LOG.read_text()
        return text.split("## #1003")[1].split("## #1002")[0]

    def test_newest_entry_is_1003_prepended(self):
        headings = [
            line
            for line in LOG.read_text().splitlines()
            if line.startswith("## #")
        ]
        assert headings[0].startswith("## #1003")

    def test_entry_mentions_new_mechanism_id_and_pero(self):
        entry = self._entry().lower()
        assert "mechanism 833" in entry
        assert "james pero" in entry
        assert "1000-1004" in entry

    def test_hash_placeholders_filled_post_followup(self):
        entry = self._entry()
        assert re.search(r"\b[0-9a-f]{40}\b", entry) is not None


class TestPushReadiness1003:
    def test_staged_set_exactly_five_paths(self):
        r = run_git("diff", "--cached", "--name-only")
        staged = {f for f in r.stdout.splitlines() if f}
        assert staged == STAGED_SET

    def test_concurrency_files_untouched_and_unstaged(self):
        r = run_git("status", "--porcelain")
        lines = r.stdout.splitlines()
        staged = {l[3:] for l in lines if l[:2] in ("M ", "A ")}
        for path in CONCURRENCY_UNTOUCHED:
            assert path not in staged, path
