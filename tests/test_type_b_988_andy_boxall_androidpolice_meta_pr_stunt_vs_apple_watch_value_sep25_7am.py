"""Type B #988 (2026-09-25 07:00 PDT): Andy Boxall (Android Police) - Sep-24
Meta Ray-Ban Audio "PR stunt" motive-attribution column vs Sep-10-2025 Apple
Watch SE 3 constructive value column. FIRST dedicated corpus mechanism on
Boxall (mechanism 824). Fourth leg of the 985-989 window (D #985 -> E #986 ->
A #987 -> B #988 -> C #989).

Meta arm (NEW, Android Police, Sep 24 2026, 11:38 AM EDT, full-text
first-hand read): "Meta's new Ray-Ban smart glasses are just a PR stunt to
dodge the camera backlash" - motive-attribution adversarial register: the
camera-free Ray-Ban Meta Audio is read as backlash-management theater
("aren't made for us to buy," "cynical, business-driven, PR response to a
social issue"); $349 attacked as "shocking" against $99-$299 earbud anchors;
the product called "hopelessly outdated"; the privacy-positive design move
treated as incriminating evidence ("You can't be a pervert with these!").
MANUAL ILLUSTRATIVE -0.55.

Apple arm (NEW, Android Police, Sep 10 2025, 2:11 PM EDT, full-text
first-hand read): "I'm struggling to find an Android watch that competes
with the Apple Watch SE 3" - constructive value register: "best value
smartwatch of the year," "genuinely good value," Apple praised for holding
the $250 price; harshness vocabulary ("hang their heads in shame") directed
at Android OEM competitors, not Apple; no motive-attribution register and no
sensor-privacy vocabulary on an always-on wrist sensor device. MANUAL
ILLUSTRATIVE +0.35.

Illustrative delta (Apple minus Meta): 0.90, n=1 vs n=1, directional only.
The salient asymmetry is register direction - price praise on Apple's $250
vs price attack on Meta's $349, plus a motive-attribution register ("PR
stunt") applied to Meta's privacy-positive hardware move with no analog in
Boxall's Apple wearables writing.

Statistical discipline per the Aug 28 2026 standing rule: MANUAL
ILLUSTRATIVE scores only, p_value/cohens_d/ci NOT_CALCULATED, is_significant
False, engine NOT run at the finding layer; verdict
directionally_supported_not_proven; no analysis.json update; NOT
artifact-grade; NOT falsification-family member; ledger holds at 30.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4
(patched green in the anchor followup). Doc-sync 3 + iteration-log 1 green
pre-commit per #719 (README/ARCH/log entry updated before the pre-commit
test pass); the hash-placeholder iteration-log test fails pre-commit per
the #721 convention and goes green in the log-hash followup.
43 tests, 10 classes (pre-commit pass: 37 green with anchor 1 + rotation 4
deselected per #565 and the hash-placeholder test failing per #721; the
staged-set push-readiness test is a PRE-COMMIT gate - it asserts the index
equals the exact five intended paths before the main commit and fails
post-commit by design once followup commits consume the staging). ASCII
only, no em dashes.
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

ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

ITERATION = 988
MECHANISM = 824
BLOCK_KEY = (
    "type_b_988_andy_boxall_androidpolice_meta_pr_stunt_vs_apple_watch_value_"
    "sep25"
)

META_URL = (
    "https://www.androidpolice.com/meta-ray-ban-audio-smart-glasses-pr-stunt-"
    "to-dodge-camera-backlash/"
)
APPLE_URL = (
    "https://www.androidpolice.com/"
    "android-smartwatch-makers-should-be-ashamed-of-themselves/"
)

META_TONE = -0.55
APPLE_TONE = 0.35
ILLUSTRATIVE_DELTA = 0.90

CONNECTS_TO = [821, 809, 818]

EXPECTED_TESTS = 43
README_TESTS_BEFORE, README_TESTS_AFTER = 50814, 50857
README_FILES_BEFORE, README_FILES_AFTER = 1312, 1313

MECH_ID_MARKER = "mechanism" + "_824"
NEXT_ID_MARKER = "mechanism" + "_825"
TOKEN_NEEDLE = "x-access" + "-token"

STAGED_SET = {
    "profiles/careers/journalists.yaml",
    f"tests/{THIS_FILE}",
    "README.md",
    "docs/ARCHITECTURE.md",
    "iteration-log.md",
}


def run_git(*args):
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, cwd=REPO
    )


def load_item():
    with open(PROFILE) as f:
        data = yaml.safe_load(f)
    return data["andy_boxall"]


def load_block():
    return load_item()["competitor_coverage"][BLOCK_KEY]


class TestNovelty988:
    def test_single_type_b_988_test_file(self):
        files = sorted((REPO / "tests").glob("test_type_b_988*.py"))
        assert [f.name for f in files] == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type B #988" in r2.stdout

    def test_novelty_first_boxall_mechanism_claim(self):
        novelty = load_block()["novelty"]
        assert "FIRST dedicated corpus mechanism on Andy Boxall" in novelty
        assert "associate editor Andy Boxall" in novelty
        assert "#976 Type E press-set" in novelty


class TestRotationCycleGuard988:
    @pytest.mark.rotation
    def test_fourth_leg_of_985_to_989_window(self):
        text = LOG.read_text()
        assert "## #985" in text and "## #986" in text and "## #987" in text
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["type"] == "B"

    @pytest.mark.rotation
    def test_predecessor_987_type_a_committed(self):
        r = run_git("log", "--oneline", "--grep=#987")
        assert r.stdout.strip() != ""
        assert (REPO / "tests" / "test_type_a_987_ft_openai_burn_realism_vs_meta_muse_charm_momentum_change_sep25_6am.py").exists()

    @pytest.mark.rotation
    def test_no_successor_989_type_c_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type C #989")
        assert r.stdout.strip() == ""
        assert "## #989" not in LOG.read_text()

    @pytest.mark.rotation
    def test_no_duplicate_988_in_log(self):
        log = LOG.read_text()
        assert log.count("## #988 Type B:") <= 1


class TestMechanism824Content:
    def test_block_key_unique_at_indent_4(self):
        hits = [
            line
            for line in PROFILE.read_text().splitlines()
            if line == f"    {BLOCK_KEY}:"
        ]
        assert len(hits) == 1

    def test_mechanism_id_824_iteration_988_type_b(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["type"] == "B"
        assert block["goal_id"] == "goal_54093bda4145"

    def test_item_fields(self):
        item = load_item()
        assert item["name"] == "Andy Boxall"
        assert item["current_publication"] == "Android Police"
        assert item["mechanism_ids"] == [MECHANISM]

    def test_two_urls_in_profiles_exactly_twice_each(self):
        # Exactly 2 hits each in the designed file: the block arm url field
        # plus the item-level source_urls list. The Meta URL's only other
        # corpus presence is the #976 Type E press-set (podcast-sentiment.md
        # and test_type_e_976.py as a crawl reference, not a Type B arm).
        for url in (META_URL, APPLE_URL):
            r = run_git("grep", "-c", "-F", url, "--", "profiles/")
            assert r.stdout.strip() == "profiles/careers/journalists.yaml:2", url

    def test_item_source_urls_contain_both(self):
        urls = load_item()["source_urls"]
        assert META_URL in urls
        assert APPLE_URL in urls

    def test_block_arm_urls(self):
        block = load_block()
        assert block["new_meta_arm"]["url"] == META_URL
        assert block["new_apple_arm"]["url"] == APPLE_URL

    def test_connects_to_all_exist(self):
        for m in CONNECTS_TO:
            r = run_git("grep", "-l", f"mechanism_id: {m}$", "--", "profiles/")
            assert r.stdout.strip() != "", m
        assert load_block()["connects_to"] == CONNECTS_TO

    def test_verdict_and_finding_mentions(self):
        block = load_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["no_analysis_json_update"] is True
        finding = block["finding"]
        assert "PR stunt" in finding
        assert "correlation" in finding.lower()

    def test_price_register_control_present(self):
        control = load_block()["price_register_control"]
        assert "shocking" in control["control_basis"]
        assert "best value smartwatch of the year" in control["control_basis"]


class TestAsymmetryScorerMath:
    def test_delta_math(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert abs(scorer["meta_arm_tone"] - META_TONE) < 1e-9
        assert abs(scorer["apple_arm_tone"] - APPLE_TONE) < 1e-9
        assert abs(scorer["illustrative_delta_apple_minus_meta"] - ILLUSTRATIVE_DELTA) < 1e-9
        assert (
            abs(
                (scorer["apple_arm_tone"] - scorer["meta_arm_tone"])
                - scorer["illustrative_delta_apple_minus_meta"]
            )
            < 1e-9
        )

    def test_tones_manual_illustrative_only(self):
        block = load_block()
        assert "MANUAL ILLUSTRATIVE" in block["statistical_discipline"]
        assert block["asymmetry_scorer_result"]["artifact_grade"] is False

    def test_meta_arm_quotes_present(self):
        quotes = load_block()["new_meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "PR stunt" in joined
        assert "aren't made for us to buy" in joined

    def test_apple_arm_quotes_present(self):
        quotes = load_block()["new_apple_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "hang their heads in shame" in joined
        assert "best value smartwatch of the year" in joined


class TestStatisticalDiscipline988:
    def test_p_value_cohens_d_ci_not_calculated(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["confidence_interval"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False

    def test_correlation_not_causation_in_finding(self):
        assert "Correlation only" in load_block()["finding"]

    def test_six_confounders_strong_first(self):
        confounders = load_block()["confounders"]
        assert len(confounders) == 6
        assert confounders[0].startswith("STRONG")
        assert confounders[1].startswith("STRONG")
        assert confounders[2].startswith("STRONG")
        assert confounders[5].startswith("WEAK")

    def test_five_counterevidence_items(self):
        block = load_block()
        assert len(block["counter_evidence"]) == 5
        assert "equal-opportunity harshness" in block["counter_evidence"][0]


class TestSupersessionAndCorpusPost987:
    def test_corpus_max_mechanism_id_is_824(self):
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
        assert ids[-1] == 824

    def test_iteration_987_zero_underscore_824_sweep_stays_green(self):
        r = run_git("grep", "-l", MECH_ID_MARKER, "--", "profiles/", "tests/")
        assert r.stdout.strip() == ""

    def test_zero_numeric_825_in_profiles(self):
        r = run_git("grep", "-l", "mechanism_id: 825$", "--", "profiles/")
        assert r.stdout.strip() == ""

    def test_numeric_824_keys_in_exactly_the_designed_location(self):
        r = run_git("grep", "-l", "mechanism_id: 824$", "--", "profiles/")
        files = [f for f in r.stdout.splitlines() if f]
        assert files == ["profiles/careers/journalists.yaml"]
        r2 = run_git("grep", "-c", "mechanism_id: 824$", "--", "profiles/careers/journalists.yaml")
        assert r2.stdout.strip().endswith(":1")

    def test_iteration_987_zero_numeric_824_sweep_fails_by_designed_supersession(self):
        r = run_git("grep", "-l", "mechanism_id: 824$", "--", "profiles/")
        assert r.stdout.strip() != ""


class TestLedger988:
    def test_not_falsification_family_member(self):
        assert load_block()["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        assert load_block()["falsification_ledger"] == 30

    def test_ledger_note_present(self):
        note = load_block()["ledger_note"]
        assert "holds at 30" in note

    def test_no_thirty_first_member_form(self):
        r = run_git("grep", "-c", "THIRTY-FIRST falsification-family member", "--", "profiles/")
        assert r.returncode == 1 or not r.stdout.strip()


class TestDocSync988:
    def test_readme_stats_updated(self):
        text = README.read_text()
        assert f"| Tests | {README_TESTS_AFTER} | Across {README_FILES_AFTER} test files |" in text

    def test_readme_table_row_for_988(self):
        text = README.read_text()
        assert f"`tests/{THIS_FILE}`" in text
        assert text.index(f"`tests/{THIS_FILE}`") > text.index(
            "`tests/test_type_a_987_ft_openai_burn_realism_vs_meta_muse_charm_momentum_change_sep25_6am.py`"
        )

    def test_architecture_tree_row_for_988(self):
        assert THIS_FILE in ARCH.read_text()


class TestIterationLog988:
    def test_newest_entry_is_988_prepended(self):
        headings = [
            line
            for line in LOG.read_text().splitlines()
            if line.startswith("## #")
        ]
        assert headings[0].startswith("## #988")

    def test_hash_placeholders_filled_post_followup(self):
        text = LOG.read_text()
        entry = text.split("## #988")[1].split("## #987")[0]
        assert re.search(r"\b[0-9a-f]{40}\b", entry) is not None


class TestPushReadiness988:
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

    def test_no_literal_underscore_824_in_test_file(self):
        text = (REPO / "tests" / THIS_FILE).read_text()
        assert MECH_ID_MARKER not in text

    def test_origin_remote_is_github(self):
        r = run_git("remote", "get-url", "origin")
        assert "github.com" in r.stdout
        assert "rayhe/mediascope" in r.stdout
