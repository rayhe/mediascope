"""Type B #998 (2026-09-25 17:00 PDT): Boone Ashworth (WIRED) Sep-23 Meta
Connect spec roundup - GENRE BOUND on mechanism 743 within the same
journalist. Fourth leg of the 995-999 window (D #995 -> E #996 -> A #997
-> B #998).

NEW arm (n=1, excerpt-tier per #503): WIRED "Meta Connect 2026: VR glasses,
camera-free Ray-Bans, Muse AI expansion, and holographic avatars" (23:42 UTC
Sep 23 2026; "Boone Ashworth - Wired" byline via the savedelete.com news
archive; independently corroborated by a verbatim deadstack.net
launch-coverage cluster attributing a WIRED/Boone Ashworth piece "Meta VR
Glasses, Ray-Ban Meta Audio, Ray-Ban Meta Gen 3: Specs, Features, Prices",
crawled ~44h before Sep 25 17:00 PDT) - neutral spec-relay register, MANUAL
ILLUSTRATIVE 0.00. The dek relays products with a neutral "unveiled" verb,
states the $1,299 VR Glasses price without judgment, mentions "camera-free
Ray-Ban Meta Audio" with ZERO privacy/surveillance/stigma vocabulary in the
surfaced excerpt, and relays product-positive descriptors ("slimmer designs",
"longer battery life", "holographic avatars", "K-Pop collaboration with
Blackpink's Lisa"). CARRIED comparator (m743 / Type B #853, un-rescored per
#807): Sep-16 Snap Specs launch arm -0.15 (price-skeptical headline/dek).
Illustrative Meta-minus-Snap delta +0.15 (0.00 - (-0.15)): the cross-entity
direction FLIPS at news-register level relative to m743's feature-register
finding (Meta subscription arm -0.48 vs Snap -0.15, gap 0.33 Meta-adversarial).
The m743 adversarial-Meta finding is genre-bounded, not refuted:
investigative/feature registers (-0.48, -0.85, -0.15) do not predict
Ashworth's launch-week news-relay register, where Meta gets the milder arm.
Cross-journalist contrast in the same Connect window: Pero (m806) frames the
camera-free Audio with the "Avoid the 'Perv' Problem" stigma headline and
Song (m827) with the "ditches the camera" stigma verb; Ashworth's WIRED relay
attaches no stigma vocabulary to the same product - Ashworth is the register
outlier of the three Connect-week Meta framers.

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
39 tests, 10 classes. ASCII only, no em dashes.
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

ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched green in the anchor followup per #565

ITERATION = 998
MECHANISM = 830
BLOCK_KEY = (
    "type_b_998_boone_ashworth_wired_meta_connect_2026_spec_roundup_genre_bound_m743"
)

NEW_URLS = [
    "https://savedelete.com/news/archive/2026/09/23/",
    "https://deadstack.net/",
]

CONNECTS_TO = [743, 442, 89, 640, 641, 818, 806, 827]

EXPECTED_TESTS = 39
README_TESTS_BEFORE, README_TESTS_AFTER = 51302, 51341
README_FILES_BEFORE, README_FILES_AFTER = 1322, 1323

MECH_ID_MARKER = "mechanism" + "_830"
NEXT_ID_MARKER = "mechanism" + "_831"

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
    item = next(
        j for j in data["journalists"] if j.get("name") == "Boone Ashworth"
    )
    return item[BLOCK_KEY]


class TestNovelty998:
    def test_single_type_b_998_test_file(self):
        files = sorted((REPO / "tests").glob("test_type_b_998*.py"))
        assert [f.name for f in files] == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type B #998" in r2.stdout

    def test_novelty_claim_present_in_block(self):
        block = load_block()
        assert "FIRST corpus evidence of Ashworth's WIRED Sep-23" in block["novelty"]
        assert "zero underscore-form 830 mechanism key strings" in block["novelty"]


class TestRotationCycleGuard998:
    @pytest.mark.rotation
    def test_fourth_leg_of_995_to_999_window(self):
        text = LOG.read_text()
        assert "## #995" in text and "Type D" in text
        assert "## #996" in text and "Type E" in text
        assert "## #997" in text and "Type A" in text
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "B"

    @pytest.mark.rotation
    def test_predecessor_997_type_a_committed(self):
        r = run_git("log", "--oneline", "--grep=#997")
        assert r.stdout.strip() != ""
        assert (
            REPO
            / "tests"
            / "test_type_a_997_atlantic_frontier_labs_doomsday_scenarios_philosophical_safety_register_vs_meta_watchdog_sep25_4pm.py"
        ).exists()

    @pytest.mark.rotation
    def test_no_successor_999_type_b_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type B #999")
        assert r.stdout.strip() == ""
        assert "## #999" not in LOG.read_text()

    @pytest.mark.rotation
    def test_no_concurrent_in_flight_type_b_998_by_commit_time(self):
        r = run_git("log", "--format=%H %s", "--grep=Type B #998")
        matches = [l for l in r.stdout.splitlines() if l.strip()]
        own = run_git("log", "--format=%H", "--", f"tests/{THIS_FILE}").stdout.splitlines()
        competing = [l for l in matches if l.split()[0] not in own]
        assert competing == [], f"concurrent Type B #998 commits: {competing}"


class TestMechanism830Content:
    def test_block_key_unique_at_indent_2(self):
        hits = [
            line
            for line in PROFILE.read_text().splitlines()
            if line == f"  {BLOCK_KEY}:"
        ]
        assert len(hits) == 1

    def test_mechanism_id_830_iteration_998_type_b(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "B"
        assert block["type"] == "B"
        assert block["journalist"] == "Boone Ashworth"
        assert block["publication"] == "WIRED (Conde Nast)"

    def test_new_urls_first_appearance(self):
        for url in NEW_URLS:
            assert url in yaml.safe_dump(load_block()), url
            r = run_git("grep", "-l", "-F", url, "--", "profiles/")
            assert [f for f in r.stdout.splitlines() if f] == [
                "profiles/careers/journalists.yaml"
            ], url

    def test_attested_titles_in_block(self):
        arm = load_block()["new_meta_arm"]
        assert "VR glasses, camera-free Ray-Bans, Muse AI expansion" in arm["title_savedelete_attested"]
        assert "Ray-Ban Meta Audio, Ray-Ban Meta Gen 3" in arm["title_deadstack_variant"]
        assert "Meta unveiled a $1,299 pair of VR glasses" in arm["dek_verbatim"]

    def test_connects_to_all_exist(self):
        for m in CONNECTS_TO:
            r = run_git("grep", "-l", f"mechanism_id: {m}$", "--", "profiles/")
            assert r.stdout.strip() != "", m
        assert load_block()["connects_to"] == CONNECTS_TO

    def test_verdict_directionally_supported_not_proven(self):
        block = load_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["no_analysis_json_update"] is True

    def test_finding_mentions_genre_bound_and_flip(self):
        finding = load_block()["finding"]
        assert "GENRE BOUND on mechanism 743" in finding
        assert "FLIPS at news-register level" in finding
        assert "Correlation only" in finding


class TestAsymmetryScorerMath:
    def test_delta_math(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert abs(scorer["new_meta_arm_tone_manual_illustrative"] - 0.0) < 1e-9
        assert abs(scorer["carried_snap_sep16_tone_manual_illustrative"] - (-0.15)) < 1e-9
        assert abs(scorer["illustrative_delta_meta_minus_snap"] - 0.15) < 1e-9
        assert scorer["delta_calc"] == "0.00 - (-0.15) = 0.15"
        assert (
            abs(
                (scorer["new_meta_arm_tone_manual_illustrative"]
                 - scorer["carried_snap_sep16_tone_manual_illustrative"])
                - scorer["illustrative_delta_meta_minus_snap"]
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
        assert scorer["reference_entity"] == "snap"
        assert scorer["publication"] == "wired"
        assert "interpretation" in scorer
        assert "limitations" in scorer
        assert scorer["statistical_contract"] == "degenerate_n1_per_arm"


class TestStatisticalDiscipline998:
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


class TestSupersessionAndCorpusPost997:
    def test_corpus_max_mechanism_id_is_830(self):
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
        assert ids[-1] == 830

    def test_iteration_997_max_829_sweep_superseded_by_design(self):
        r = run_git("grep", "-l", "mechanism_id: 829$", "--", "profiles/")
        assert r.stdout.strip() != ""
        r2 = run_git("grep", "-l", "mechanism_id: 830$", "--", "profiles/")
        assert r2.stdout.strip() != ""

    def test_zero_underscore_831_repo_wide(self):
        r = run_git("grep", "-l", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_numeric_831_in_profiles(self):
        r = run_git("grep", "-l", "mechanism_id: 831$", "--", "profiles/")
        assert r.stdout.strip() == ""

    def test_iteration_997_zero_underscore_830_sweep_stays_green(self):
        r = run_git("grep", "-l", MECH_ID_MARKER, "--", "profiles/", "tests/")
        assert r.stdout.strip() == ""

    def test_iteration_997_zero_numeric_830_sweep_fails_by_designed_supersession(self):
        r = run_git("grep", "-l", "mechanism_id: 830$", "--", "profiles/")
        assert r.stdout.strip() != ""

    def test_numeric_830_keys_in_exactly_the_designed_location(self):
        r = run_git("grep", "-l", "mechanism_id: 830$", "--", "profiles/")
        files = [f for f in r.stdout.splitlines() if f]
        assert files == ["profiles/careers/journalists.yaml"]
        r2 = run_git("grep", "-c", "mechanism_id: 830$", "--", "profiles/careers/journalists.yaml")
        assert r2.stdout.strip().endswith(":1")


class TestLedger998:
    def test_not_falsification_family_member(self):
        assert load_block()["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        assert load_block()["falsification_ledger"] == 30

    def test_ledger_note_present(self):
        note = load_block()["falsification_note"]
        assert "holds at 30" in note


class TestDocSync998:
    def test_readme_stats_updated(self):
        text = README.read_text()
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text
        assert f"| Tests | {README_TESTS_AFTER} | Across {README_FILES_AFTER} test files |" in text

    def test_readme_table_row_for_998(self):
        text = README.read_text()
        assert f"`tests/{THIS_FILE}`" in text
        assert text.index(f"`tests/{THIS_FILE}`") > text.index(
            "`tests/test_type_a_997_atlantic_frontier_labs_doomsday_scenarios_philosophical_safety_register_vs_meta_watchdog_sep25_4pm.py`"
        )

    def test_architecture_tree_row_for_998(self):
        assert THIS_FILE in ARCH.read_text()


class TestIterationLog998:
    def _entry(self):
        text = LOG.read_text()
        return text.split("## #998")[1].split("## #997")[0]

    def test_newest_entry_is_998_prepended(self):
        headings = [
            line
            for line in LOG.read_text().splitlines()
            if line.startswith("## #")
        ]
        assert headings[0].startswith("## #998")

    def test_entry_mentions_mechanism_830_and_ashworth(self):
        entry = self._entry().lower()
        assert "mechanism 830" in entry
        assert "boone ashworth" in entry
        assert "995-999" in entry

    def test_hash_placeholders_filled_post_followup(self):
        entry = self._entry()
        assert re.search(r"\b[0-9a-f]{40}\b", entry) is not None


class TestPushReadiness998:
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
