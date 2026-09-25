"""Type B #993: Victoria Song (The Verge) Sep-23 Ray-Ban Audio stigma frame + Sep-24
Vergecast business-model-attribution vs Snap "broken illusion" product-skepticism
(mechanism 827 in profiles/careers/journalists.yaml).

Temporal extension of mechanism 75: Song's privacy/data-harvesting register fires
on Meta in Connect week while her Snap-side register in the same segment stays
product/market-skeptical with zero data-harvesting vocabulary. Illustrative
Meta-minus-Snap delta -0.15 NARROWS m75's gap: temporal BOUND, not replication.

Evidence tiers: Sep-23 piece = feed-attestation excerpt (TechNewsTube theverge
proxy, byline + date + title + partial body); Sep-24 segment = scraper relay
(finance.biggo.com relay of the Vergecast segment, attribution shared with
co-host per relay text). No canonical theverge.com URLs constructed this run.

MANUAL ILLUSTRATIVE ONLY. n=1 vs n=1. p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant False. Engine not run. verdict directionally_supported_not_proven.
Not artifact-grade. NOT falsification-family member. Ledger holds at 30.

Doc-sync (this run, venv python): README stats 51055/1317 -> 51098/1318 (+43/+1).
"""

import re
import subprocess

import pytest
import yaml

ITERATION = 993
TYPE_LETTER = "B"
MECH_ID = 827
EXPECTED_TESTS = 43
THIS_FILE = "tests/test_type_b_993_victoria_song_verge_rayban_audio_stigma_vs_snap_broken_illusion_sep25_noon.py"
BLOCK_KEY = "type_b_993_victoria_song_verge_rayban_audio_stigma_vs_snap_broken_illusion_sep25"
PREDECESSOR_FILE = "tests/test_type_a_992_verge_apple_ambient_listening_week_vs_meta_luna_stigma_sep25_11am.py"
README_TESTS_BEFORE = 51055
README_TESTS_AFTER = 51098
README_FILES_BEFORE = 1317
README_FILES_AFTER = 1318
CONNECTS_TO = [75, 722, 764, 773, 818, 824]
META_TONE = -0.35
SNAP_TONE = -0.20
DELTA_EXPECTED = -0.15
NEW_URL_TNT = "https://technewstube.com/theverge/1870121/meta-ditches-camera-newest-smart-glasses/"
NEW_URL_BIGGO = "https://finance.biggo.com/news/d71bedffa3fb45e3"
ANCHORED_SHA = "1a512b73"
CONCURRENCY_UNSTAGED = [
    "profiles/nytimes.yaml",
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
]
CONCURRENCY_UNTRACKED = [
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
]
EXPECTED_STAGED = sorted([
    "profiles/careers/journalists.yaml",
    THIS_FILE,
    "README.md",
    "docs/ARCHITECTURE.md",
    "iteration-log.md",
])


def run_git(*args):
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, cwd="."
    )


def load_journalists():
    with open("profiles/careers/journalists.yaml") as f:
        return yaml.safe_load(f)


def mechanism_block():
    item = load_journalists()["victoria_song"]
    return item["competitor_coverage"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# Novelty and anchor
# ---------------------------------------------------------------------------


class TestNovelty993:
    def test_single_type_b_993_test_file(self):
        p = run_git("ls-files", "tests/test_type_b_993*")
        assert p.stdout.strip().splitlines() == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert re.fullmatch(r"[0-9a-f]{8}", ANCHORED_SHA), (
            "ANCHORED_SHA must be patched to the main-commit short SHA in the "
            "anchor followup per the #716 pattern; placeholder expected pre-commit"
        )

    def test_first_dedicated_type_b_mechanism_on_song_under_top_level_item(self):
        text = open("profiles/careers/journalists.yaml").read()
        assert text.count("\nvictoria_song:") == 1
        block = mechanism_block()
        assert block["mechanism_id"] == MECH_ID
        assert block["iteration"] == ITERATION
        assert block["type"] == TYPE_LETTER
        # mechanism 75 predates the sequence numbering; 593 is Type C
        assert "mechanism 75 predates the sequence numbering" in block["novelty"]
        assert "mechanism 593 is Type C" in block["novelty"]


# ---------------------------------------------------------------------------
# Rotation-cycle guards (deselected post-commit: successor invalidates them)
# ---------------------------------------------------------------------------


@pytest.mark.rotation_cycle
class TestRotationCycleGuard993:
    def test_fourth_leg_of_990_to_994_window(self):
        log = open("iteration-log.md").read()
        assert "## #993" in log and "## #992" in log

    def test_predecessor_992_type_a_committed(self):
        p = run_git("log", "--oneline", "--grep=Type A #992")
        assert "Type A #992" in p.stdout

    def test_no_successor_994_type_c_commit_yet(self):
        p = run_git("log", "--oneline", "--grep=Type C #994")
        assert p.stdout.strip() == ""

    def test_no_duplicate_993_in_log(self):
        log = open("iteration-log.md").read()
        assert log.count("## #993 Type B") == 1


# ---------------------------------------------------------------------------
# Mechanism 827 content
# ---------------------------------------------------------------------------


class TestMechanism827Content:
    def test_block_key_unique_at_indent_4(self):
        text = open("profiles/careers/journalists.yaml").read()
        assert text.count("    " + BLOCK_KEY + ":") == 1

    def test_mechanism_id_iteration_type(self):
        block = mechanism_block()
        assert block["mechanism_id"] == MECH_ID
        assert block["iteration"] == ITERATION
        assert block["type"] == TYPE_LETTER
        assert block["date"] == "2026-09-25"
        assert block["goal_id"] == "goal_54093bda4145"

    def test_item_fields(self):
        item = load_journalists()["victoria_song"]
        assert item["name"] == "Victoria Song"
        assert item["current_publication"] == "The Verge"
        assert item["mechanism_ids"] == [MECH_ID]
        assert "smart glasses" in item["beats"]

    def test_item_source_urls_contain_both(self):
        item = load_journalists()["victoria_song"]
        assert NEW_URL_TNT in item["source_urls"]
        assert NEW_URL_BIGGO in item["source_urls"]

    def test_block_arm_urls_exact(self):
        block = mechanism_block()
        assert block["meta_corpus"][0]["source_url"] == NEW_URL_TNT
        assert block["meta_corpus"][1]["source_url"] == NEW_URL_BIGGO
        assert block["competitor_corpus"][0]["source_url"] == NEW_URL_BIGGO

    def test_new_urls_appear_designed_times_in_profiles(self):
        p1 = run_git("grep", "-F", "-o", NEW_URL_TNT, "--", "profiles/")
        p2 = run_git("grep", "-F", "-o", NEW_URL_BIGGO, "--", "profiles/")
        assert p1.stdout.count(NEW_URL_TNT) == 2, "TNT URL: block arm + item source_urls"
        assert p2.stdout.count(NEW_URL_BIGGO) == 3, "BIGGO URL: two block arms + item source_urls"

    def test_connects_to_all_exist_in_corpus(self):
        p = run_git("grep", "-h", "mechanism_id:", "--", "profiles/")
        for mid in CONNECTS_TO:
            assert f"mechanism_id: {mid}" in p.stdout

    def test_finding_verdict_mentions_temporal_bound(self):
        evidence = "\n".join(mechanism_block()["observed_evidence"])
        assert "NARROWS" in evidence
        assert "temporal BOUND" in evidence
        assert "directionally_supported_not_proven" in mechanism_block()["verdict"]

    def test_register_selectivity_present(self):
        evidence = "\n".join(mechanism_block()["observed_evidence"])
        notes = mechanism_block()["competitor_corpus"][0]["notes"]
        assert "zero data-harvesting vocabulary on Snap" in evidence
        assert "privacy register stays on Meta" in notes


# ---------------------------------------------------------------------------
# Asymmetry scorer math (manual illustrative)
# ---------------------------------------------------------------------------


class TestAsymmetryScorerMath993:
    def test_delta_math(self):
        computed = round(META_TONE - SNAP_TONE, 2)
        assert computed == DELTA_EXPECTED, f"{META_TONE}-{SNAP_TONE} != {DELTA_EXPECTED}"
        assert mechanism_block()["scoring"]["illustrative_delta_meta_minus_snap"] == DELTA_EXPECTED

    def test_tones_manual_illustrative_only(self):
        scoring = mechanism_block()["scoring"]
        assert scoring["manual_illustrative"] is True
        assert scoring["meta_arm_tone"] == META_TONE
        assert scoring["snap_arm_tone"] == SNAP_TONE
        for key in ("p_value", "cohens_d", "confidence_interval_95"):
            assert scoring[key] == "NOT_CALCULATED"
        assert scoring["is_significant"] is False

    def test_meta_arm_quotes_present(self):
        text = open("profiles/careers/journalists.yaml").read()
        assert "pervert glasses" in text
        assert "Hoover Up Your Data" in text

    def test_snap_arm_quotes_present(self):
        text = open("profiles/careers/journalists.yaml").read()
        assert "broken illusion" in text
        assert "$2,195" in text


# ---------------------------------------------------------------------------
# Statistical discipline
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline993:
    def test_no_significance_claimed(self):
        sd = mechanism_block()["statistical_discipline"]
        assert "is_significant False" in sd
        assert "not evidence of bias" in sd

    def test_correlation_not_causation(self):
        note = mechanism_block()["correlational_note"]
        assert "correlational observations" in note
        assert "No causal claim" in note

    def test_six_confounders_strong_first(self):
        confounders = mechanism_block()["confounders"]
        assert len(confounders) == 6
        strengths = [c["strength"] for c in confounders]
        assert strengths[:3] == ["STRONG", "STRONG", "STRONG"]
        assert strengths.count("STRONG") == 3

    def test_five_counterevidence_items(self):
        counter = mechanism_block()["counterevidence"]
        assert len(counter) == 5
        joined = "\n".join(counter)
        assert "not adversarial" in joined
        assert "broken illusion" in joined


# ---------------------------------------------------------------------------
# Supersession and corpus state post-#992
# ---------------------------------------------------------------------------


class TestSupersessionAndCorpusPost992:
    def test_corpus_max_mechanism_id_is_827(self):
        p = run_git("grep", "-oh", "mechanism_id: [0-9][0-9]*", "--", "profiles/")
        ids = [int(x.split(":")[1]) for x in p.stdout.strip().splitlines()]
        assert max(ids) == MECH_ID

    def test_zero_underscore_827_keys_in_profiles_and_tests(self):
        needle = "mechanism" + "_827"
        p = run_git("grep", "-l", needle, "--", "profiles/", "tests/")
        assert p.stdout.strip() == ""

    def test_zero_numeric_828_keys_in_profiles(self):
        p = run_git("grep", "-l", "mechanism_id: 828", "--", "profiles/")
        assert p.stdout.strip() == ""

    def test_numeric_827_in_designed_location_only(self):
        p = run_git("grep", "-l", "mechanism_id: 827", "--", "profiles/")
        assert p.stdout.strip().splitlines() == ["profiles/careers/journalists.yaml"]

    def test_numeric_826_still_present_predecessor(self):
        p = run_git("grep", "-l", "mechanism_id: 826", "--", "profiles/")
        assert p.stdout.strip() != ""


# ---------------------------------------------------------------------------
# Falsification ledger
# ---------------------------------------------------------------------------


class TestLedger993:
    def test_not_falsification_family(self):
        block = mechanism_block()
        assert block["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        block = mechanism_block()
        assert block["falsification_ledger"] == 30

    def test_ledger_note_holds(self):
        note = mechanism_block()["ledger_note"]
        assert "Ledger holds at 30" in note

    def test_no_thirty_first_member_form(self):
        p = run_git("grep", "-l", "THIRTY-FIRST falsification-family member", "--", "profiles/")
        assert p.stdout.strip() == ""


# ---------------------------------------------------------------------------
# Doc-sync
# ---------------------------------------------------------------------------


class TestDocSync993:
    def test_readme_stats_updated(self):
        text = open("README.md").read()
        assert f"| Tests | {README_TESTS_AFTER} | Across {README_FILES_AFTER} test files |" in text
        assert f"| Tests | {README_TESTS_BEFORE} |" not in text

    def test_readme_table_row_present_after_992(self):
        text = open("README.md").read()
        assert THIS_FILE in text
        assert text.index(THIS_FILE) < text.index(PREDECESSOR_FILE), (
            "README test-file table is newest-first: #993 row must precede #992"
        )

    def test_architecture_tree_row_present_after_992(self):
        text = open("docs/ARCHITECTURE.md").read()
        assert THIS_FILE in text
        assert text.index(THIS_FILE) < text.index(PREDECESSOR_FILE)


# ---------------------------------------------------------------------------
# Iteration log
# ---------------------------------------------------------------------------


class TestIterationLog993:
    def test_log_newest_entry_is_993(self):
        log = open("iteration-log.md").read()
        assert log.startswith("## #993 Type B"), "iteration-log.md must be prepended newest-first"

    def test_log_hash_placeholders_filled_post_commit(self):
        log = open("iteration-log.md").read()
        entry = log.split("## #993 Type B")[1].split("\n## #")[0]
        assert "<SHA_MAIN>" not in entry, "main commit hash must be patched in log-hash followup"
        assert "<SHA_ANCHOR>" not in entry, "anchor hash must be patched in log-hash followup"
        assert "<SHA_LOGHASH>" not in entry, "log-hash followup hash must be patched"
        assert "<DATE>" not in entry, "date placeholder must be filled"


# ---------------------------------------------------------------------------
# Push readiness
# ---------------------------------------------------------------------------


class TestPushReadiness993:
    def test_staged_set_is_exactly_five_paths(self):
        p = run_git("diff", "--cached", "--name-only")
        staged = sorted(p.stdout.strip().splitlines())
        assert staged == EXPECTED_STAGED, f"unexpected staged set: {staged}"

    def test_concurrency_files_untouched_and_unstaged(self):
        p = run_git("diff", "--cached", "--name-only")
        staged = p.stdout.strip().splitlines()
        for path in CONCURRENCY_UNSTAGED + CONCURRENCY_UNTRACKED:
            assert path not in staged
        for path in CONCURRENCY_UNSTAGED:
            p2 = run_git("diff", "--name-only")
            assert path in p2.stdout.strip().splitlines()
        p3 = run_git("status", "--porcelain")
        for path in CONCURRENCY_UNTRACKED:
            assert f"?? {path}" in p3.stdout

    def test_no_credentials_in_staged_diff(self):
        p = run_git("diff", "--cached")
        added = "\n".join(
            line[1:] for line in p.stdout.splitlines()
            if line.startswith("+") and not line.startswith("+++")
        ).lower()
        frags = ("to" + "ken", "pass" + "word", "sec" + "ret",
                 "api" + "_key", "api" + "key")
        for frag in frags:
            assert frag not in added, f"credential-like fragment {frag!r} in staged diff"

    def test_no_literal_underscore_827_in_test_file(self):
        text = open(THIS_FILE).read()
        assert "mechanism" + "_827" not in text

    def test_origin_remote_is_github_https(self):
        p = run_git("remote", "get-url", "origin")
        assert p.stdout.strip() == "https://github.com/rayhe/mediascope-asymmetry.git"
