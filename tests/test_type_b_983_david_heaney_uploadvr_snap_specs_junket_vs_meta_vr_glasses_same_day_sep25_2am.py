"""Type B #983 (2026-09-25 02:00 PDT): David Heaney (UploadVR) - Sep-23 Snap
Specs junket-disclosed hands-on vs same-day Meta VR Glasses announcement.
FIRST dedicated corpus mechanism on Heaney (mechanism 821). Fourth leg of
the 980-984 window (D #980 -> E #981 -> A #982 -> B #983 -> C #984).

Snap arm (NEW, UploadVR, Sep 23 2026): "Snap Specs Hands-On: Minimum Viable
Consumer True AR Glasses" - opens with the junket disclosure ("For
disclosure, Snap paid for my flights and accommodation for its "launch"
event"), runs the harshest product register in the same-day pair
("optically rough," rainbow pattern, poor color uniformity, blue streaks;
tracking only "just about pass" the minimum bar) while carrying
ambition-positive market framing ("beating companies like Meta and Apple to
market") and the Nvidia agentic-AI partnership relay. Zero
camera/privacy/surveillance vocabulary in the indexed excerpt on a 4-camera
face-worn glasses product (bounded-listing absence per the iteration-492
rule). MANUAL ILLUSTRATIVE -0.10.

Meta arm (NEW, UploadVR, Sep 23 2026, same journalist, same publication,
same day, same hardware category): "Meta VR Glasses Officially Announced,
Shipping Spring 2027 For $1300" - neutral spec relay (2.4K micro-OLED, 100g,
tethered puck, Snapdragon Reality Elite), headline price-flag neutral.
MANUAL ILLUSTRATIVE 0.00.

Privacy-register control: Heaney's Meta glasses coverage habitually carries
privacy vocabulary ("Meta To Launch Smart Glasses Without Camera As Privacy
Backlash Grows", Sep 13 2026; "Meta Still Internally Debating Privacy Of
Always-On AI Glasses", Jul 8 2026; "Meta Is Improving Its Smart Glasses
Privacy LED Tampering Detection", Jul 7 2026), while the junket-funded Snap
hands-on on 4-camera glasses carries none in the indexed excerpt.

Illustrative delta (Snap minus Meta): -0.10 - 0.00 = -0.10, n=1 vs n=1,
directional only. The junket did NOT buy product softness - the Snap arm's
optical criticism is the harshest product judgment in the pair, so
disclosure-coexists-with-criticism bounds the naive incentive-softening
prediction. REPLICATES the Sep-16 launch-window challenger-optimism
direction at journalist level alongside m743 (Ashworth, WIRED), m749 (Ropek,
TechCrunch), m746 (Pero, Gizmodo) - a FOURTH journalist, same direction;
EXTENDS the m629 same-day same-journalist precedent class (Reece Rogers,
WIRED, Jul 7 2026) with a disclosed travel-junket leg. Resolves the #928
rejected-candidate note ("no corpus presence, no same-writer competitor
arm").

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
42 tests, 10 classes. ASCII only, no em dashes.
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

ITERATION = 983
MECHANISM = 821
BLOCK_KEY = (
    "type_b_983_david_heaney_uploadvr_snap_specs_junket_vs_meta_vr_glasses_"
    "same_day_sep25"
)

SNAP_URL = (
    "https://www.uploadvr.com/snap-specs-hands-on-minimum-viable-consumer-"
    "true-ar-glasses/"
)
META_URL = (
    "https://www.uploadvr.com/meta-vr-glasses-officially-announced-"
    "connect-2026/"
)

SNAP_TONE = -0.10
META_TONE = 0.00
ILLUSTRATIVE_DELTA = -0.10

CONNECTS_TO = [629, 743, 746, 269, 734, 791]

EXPECTED_TESTS = 42
README_TESTS_BEFORE, README_TESTS_AFTER = 50576, 50618
README_FILES_BEFORE, README_FILES_AFTER = 1307, 1308

MECH_ID_MARKER = "mechanism" + "_821"
NEXT_ID_MARKER = "mechanism" + "_822"
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
    return data["david_heaney"]


def load_block():
    return load_item()["competitor_coverage"][BLOCK_KEY]


class TestNovelty983:
    def test_single_type_b_983_test_file(self):
        files = sorted((REPO / "tests").glob("test_type_b_983*.py"))
        assert [f.name for f in files] == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type B #983" in r2.stdout

    def test_novelty_first_heaney_mechanism_claim(self):
        novelty = load_block()["novelty"]
        assert "FIRST dedicated corpus mechanism on David Heaney" in novelty
        assert "no same-writer competitor arm" in novelty


class TestRotationCycleGuard983:
    @pytest.mark.rotation
    def test_fourth_leg_of_980_to_984_window(self):
        text = LOG.read_text()
        assert "## #980" in text and "## #981" in text and "## #982" in text
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["type"] == "B"

    @pytest.mark.rotation
    def test_predecessor_982_type_a_committed(self):
        r = run_git("log", "--oneline", "--grep=#982")
        assert r.stdout.strip() != ""
        assert (REPO / "tests" / "test_type_a_982_wired_pinky_promises_skepticism_vs_google_xr_sep_window_noncoverage_sep25_1am.py").exists()

    @pytest.mark.rotation
    def test_no_successor_984_type_c_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type C #984")
        assert r.stdout.strip() == ""
        assert "## #984" not in LOG.read_text()

    @pytest.mark.rotation
    def test_no_duplicate_983_in_log(self):
        log = LOG.read_text()
        assert log.count("## #983 Type B:") <= 1


class TestMechanism821Content:
    def test_block_key_unique_at_indent_4(self):
        hits = [
            line
            for line in PROFILE.read_text().splitlines()
            if line == f"    {BLOCK_KEY}:"
        ]
        assert len(hits) == 1

    def test_mechanism_id_821_iteration_983_type_b(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["type"] == "B"
        assert block["goal_id"] == "goal_54093bda4145"

    def test_item_fields(self):
        item = load_item()
        assert item["name"] == "David Heaney"
        assert item["current_publication"] == "UploadVR"
        assert item["mechanism_ids"] == [MECHANISM]

    def test_two_new_urls_first_appearance_in_profiles(self):
        # Exactly 2 hits each in exactly the designed file: the block arm
        # url field plus the item-level source_urls list. Both URLs were
        # zero-hit repo-wide pre-commit (pre-commit novelty grep).
        for url in (SNAP_URL, META_URL):
            r = run_git("grep", "-c", "-F", url, "--", "profiles/")
            assert r.stdout.strip() == "profiles/careers/journalists.yaml:2", url

    def test_item_source_urls_contain_both(self):
        urls = load_item()["source_urls"]
        assert SNAP_URL in urls
        assert META_URL in urls

    def test_block_arm_urls(self):
        block = load_block()
        assert block["new_snap_arm"]["url"] == SNAP_URL
        assert block["new_meta_arm"]["url"] == META_URL

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
        assert "junket" in finding
        assert "correlation" in finding.lower()

    def test_privacy_register_control_present(self):
        control = load_block()["privacy_register_control"]
        assert "Privacy Backlash" in control["control_basis"]
        assert "4-camera" in control["contrast"]


class TestAsymmetryScorerMath:
    def test_delta_math(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert abs(scorer["snap_arm_tone"] - SNAP_TONE) < 1e-9
        assert abs(scorer["meta_arm_tone"] - META_TONE) < 1e-9
        assert abs(scorer["illustrative_delta_snap_minus_meta"] - ILLUSTRATIVE_DELTA) < 1e-9
        assert (
            abs(
                (scorer["snap_arm_tone"] - scorer["meta_arm_tone"])
                - scorer["illustrative_delta_snap_minus_meta"]
            )
            < 1e-9
        )

    def test_tones_manual_illustrative_only(self):
        block = load_block()
        assert "MANUAL ILLUSTRATIVE" in block["statistical_discipline"]
        assert block["asymmetry_scorer_result"]["artifact_grade"] is False

    def test_snap_arm_junket_disclosure_quoted(self):
        quotes = load_block()["new_snap_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "Snap paid for my flights" in joined
        assert "optical artifacts" in joined


class TestStatisticalDiscipline983:
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

    def test_four_counterevidence_items(self):
        block = load_block()
        assert len(block["counter_evidence"]) == 4
        assert "no concealment" in block["counter_evidence"][0]


class TestSupersessionAndCorpusPost982:
    def test_corpus_max_mechanism_id_is_821(self):
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
        assert ids[-1] == 821

    def test_iteration_982_zero_underscore_821_sweep_stays_green(self):
        r = run_git("grep", "-l", MECH_ID_MARKER, "--", "profiles/", "tests/")
        assert r.stdout.strip() == ""

    def test_zero_numeric_822_in_profiles(self):
        r = run_git("grep", "-l", "mechanism_id: 822$", "--", "profiles/")
        assert r.stdout.strip() == ""

    def test_numeric_821_keys_in_exactly_the_designed_location(self):
        r = run_git("grep", "-l", "mechanism_id: 821$", "--", "profiles/")
        files = [f for f in r.stdout.splitlines() if f]
        assert files == ["profiles/careers/journalists.yaml"]
        r2 = run_git("grep", "-c", "mechanism_id: 821$", "--", "profiles/careers/journalists.yaml")
        assert r2.stdout.strip().endswith(":1")

    def test_iteration_982_zero_numeric_821_sweep_fails_by_designed_supersession(self):
        r = run_git("grep", "-l", "mechanism_id: 821$", "--", "profiles/")
        assert r.stdout.strip() != ""


class TestLedger983:
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


class TestDocSync983:
    def test_readme_stats_updated(self):
        text = README.read_text()
        assert f"| Tests | {README_TESTS_AFTER} | Across {README_FILES_AFTER} test files |" in text

    def test_readme_table_row_for_983(self):
        text = README.read_text()
        assert f"`tests/{THIS_FILE}`" in text
        assert text.index(f"`tests/{THIS_FILE}`") > text.index(
            "`tests/test_type_a_982_wired_pinky_promises_skepticism_vs_google_xr_sep_window_noncoverage_sep25_1am.py`"
        )

    def test_architecture_tree_row_for_983(self):
        assert THIS_FILE in ARCH.read_text()


class TestIterationLog983:
    def test_newest_entry_is_983_prepended(self):
        headings = [
            line
            for line in LOG.read_text().splitlines()
            if line.startswith("## #")
        ]
        assert headings[0].startswith("## #983")

    def test_hash_placeholders_filled_post_followup(self):
        text = LOG.read_text()
        entry = text.split("## #983")[1].split("## #982")[0]
        assert re.search(r"\b[0-9a-f]{40}\b", entry) is not None


class TestPushReadiness983:
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

    def test_no_literal_underscore_821_in_test_file(self):
        text = (REPO / "tests" / THIS_FILE).read_text()
        assert MECH_ID_MARKER not in text

    def test_origin_remote_is_github(self):
        r = run_git("remote", "get-url", "origin")
        assert "github.com" in r.stdout
        assert "rayhe/mediascope" in r.stdout
