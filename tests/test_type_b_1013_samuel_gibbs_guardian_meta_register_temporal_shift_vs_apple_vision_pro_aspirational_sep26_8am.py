"""Type B #1013 (2026-09-26 08:00 PDT): Samuel Gibbs (Guardian) Meta register
temporal shift - Sep-24 2026 Connect stigma relay vs Sep-17 2025 launch
announcement baseline vs carried Apple Vision Pro aspirational review.
Fourth leg of the 1010-1014 window (D #1010 -> E #1011 -> A #1012 -> B #1013).

JOURNALIST-ANGLE TEMPORAL-SHIFT extension of mechanism 611 (Type B #628,
Gibbs within-writer genre register) and mechanism 832 (Type A #1002,
Guardian zero-financial-gradient control). All three arm tones are CARRIED
un-rescored per #807: Meta stigma arm Sep-24 2026 "Meta debuts no-camera
smart glasses and virtual reality spectacles" (stigma paragraph
"frequently being dubbed perv glasses or spy glasses" on the camera-free
Ray-Ban Meta Audio; MANUAL ILLUSTRATIVE -0.20, from m832); Meta baseline
arm Sep-17 2025 Meta Ray-Ban Display launch announcement (neutral-positive
+0.10, from m611); Apple arm Aug-16 2024 Vision Pro hands-on review
(aspirational +0.35, from m611/#622).

Within-writer Meta register deteriorates 0.30 over 12 months (+0.10 to
-0.20) with genre held at NEWS on both Meta arms, isolating the
news-environment peg (scandal-heavy Connect 2026) from the genre confound
that dominated m611. Entity gap with the new stigma arm: Meta minus Apple
-0.55 ((-0.20) - (0.35)), widened from m611's -0.25, but the Apple side
stays review-genre so the cross-entity comparison remains genre-bounded.
Zero-financial-gradient control extended to the journalist level (Guardian
$0 Apple, $0 Meta). Verdict directionally_supported_not_proven.

Statistical discipline per the Aug 28 2026 standing rule: MANUAL
ILLUSTRATIVE scores only (all tones carried un-rescored),
p_value/cohens_d/ci NOT_CALCULATED, is_significant False, engine NOT run at
the finding layer; verdict directionally_supported_not_proven; no
analysis.json update; NOT artifact-grade; NOT falsification-family member;
ledger holds at 30.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4
(patched green in the anchor followup). Doc-sync 3 fail pre-commit per #719,
all green post-doc-sync; iteration-log newest-entry green; hash-placeholder
test fails pre-commit per the #721 convention; staged-set test fails
pre-commit by design.
41 tests, 10 classes. ASCII only, no em dashes.
"""

import os
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

ANCHORED_SHA = "a11199707577599ea5410e26f3a788d58dbc01e4"  # patched in the anchor followup per #565

ITERATION = 1013
MECHANISM = 839
BLOCK_KEY = (
    "type_b_1013_samuel_gibbs_guardian_meta_register_temporal_shift_"
    "sep2026_stigma_vs_apple_vision_pro_aspirational"
)

# All arms are CARRIED this run (per #807); no new-to-corpus arm URLs.
# The journalist-angle block itself is the novelty.
CARRIED_URLS = [
    "https://globalcommunityweekly.substack.com/p/meta-debuts-no-camera-smart-glasses",
    "https://www.richardhartley.com/2025/09/meta-announces-first-ray-ban-smart-glasses-with-in-built-augmented-reality-display/",
    "http://richardhartley.com/2024/08/vision-pro-review-apples-cutting-edge-headset-lives-up-to-the-hype/",
]

CONNECTS_TO = [611, 832, 622]

PREDECESSOR_SHAS = {
    "788bc9a8d2099253160b7303ff09a70a0a10be74",  # #1012 main
    "06287964114e13ff7de97742060d2409ecb7458d",  # #1012 anchor
    "6126457c70a3dd88f0c47fa146636d4b9f1a72f9",  # #1012 log-hash
}

EXPECTED_TESTS = 41
README_TESTS_BEFORE, README_TESTS_AFTER = 52029, 52070
README_FILES_BEFORE, README_FILES_AFTER = 1337, 1338

MECH_ID_MARKER = "mechanism" + "_839"
NEXT_ID_MARKER = "mechanism" + "_840"
NEXT_DASH_MARKER = "mechanism" + "-840"

STAGED_SET = {
    "profiles/careers/journalists.yaml",
    "tests/" + THIS_FILE,
    "README.md",
    "docs/ARCHITECTURE.md",
    "iteration-log.md",
}


def run_git(*args):
    return subprocess.run(
        ["git"] + list(args), capture_output=True, text=True, cwd=REPO
    )


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def load_block():
    with open(PROFILE, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    item = next(
        j for j in data["journalists"] if j.get("name") == "Samuel Gibbs"
    )
    return item["competitor_coverage"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty per the Aug 31 standing rule
# ---------------------------------------------------------------------------
class TestNovelty1013:
    def test_single_type_b_1013_test_file(self):
        files = sorted(
            f for f in os.listdir(os.path.join(str(REPO), "tests"))
            if f.startswith("test_type_b_1013") and f.endswith(".py")
        )
        assert files == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type B #1013" in r2.stdout

    def test_no_type_b_1013_in_git_log_precommit(self):
        r = run_git("log", "--format=%H %s", "--grep", "Type B #1013")
        own = run_git(
            "log", "--format=%H", "--", "tests/" + THIS_FILE
        ).stdout
        hits = [
            line for line in r.stdout.splitlines()
            if line.split()[0] not in own.split()
        ]
        assert hits == []


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1010-1014 window, fourth leg
# ---------------------------------------------------------------------------
class TestRotationGuard1013:
    def test_window_legs_in_iteration_log(self):
        text = _read(LOG)
        assert "## #1010 Type D" in text
        assert "## #1011 Type E" in text
        assert "## #1012 Type A" in text
        assert "1010-1014" in text

    @pytest.mark.rotation
    def test_fourth_leg_of_1010_to_1014_window(self):
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "B"
        assert "1010-1014 window" in block["rotation_transparency"]
        assert "FOURTH leg" in block["rotation_transparency"]

    @pytest.mark.rotation
    def test_predecessor_1012_type_a_committed(self):
        r = run_git("log", "--oneline", "--grep", "Type A #1012")
        assert r.stdout.strip() != ""
        assert (
            REPO
            / "tests"
            / "test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py"
        ).exists()

    @pytest.mark.rotation
    def test_no_successor_1014_type_c_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type C #1014")
        assert r.stdout.strip() == ""
        assert "## #1014" not in _read(LOG)

    @pytest.mark.rotation
    def test_no_concurrent_type_b_1013_by_commit_time(self):
        r = run_git("log", "--format=%H %s", "--grep", "Type B #1013")
        matches = [line for line in r.stdout.splitlines() if line.strip()]
        own = run_git(
            "log", "--format=%H", "--", "tests/" + THIS_FILE
        ).stdout.split()
        competing = [line for line in matches if line.split()[0] not in own]
        assert competing == []


# ---------------------------------------------------------------------------
# 3. Mechanism 839 block content
# ---------------------------------------------------------------------------
class TestMechanism839Content:
    def test_block_key_unique_at_indent_4(self):
        hits = [
            line for line in _read(PROFILE).splitlines()
            if line == "    " + BLOCK_KEY + ":"
        ]
        assert len(hits) == 1

    def test_mechanism_id_839_iteration_1013_type_b(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "B"
        assert block["type"] == "B"

    def test_journalist_and_publication(self):
        block = load_block()
        assert block["journalist"] == "Samuel Gibbs"
        assert block["publication"] == "Guardian News and Media"

    def test_publication_author_goal_job_fields(self):
        block = load_block()
        assert block["author"] == "Kit (with Ray)"
        assert block["goal_id"] == "goal_54093bda4145"
        assert block["job_id"] == "mediascope-daily-iteration"
        assert block["date_analyzed"] == "2026-09-26"
        assert block["time_pdt"] == "08:00"

    def test_key_design_note_no_numeric_substring(self):
        block = load_block()
        assert MECH_ID_MARKER not in BLOCK_KEY
        assert NEXT_ID_MARKER not in BLOCK_KEY
        assert "key_design_note" in block
        assert "mechanism" + "_839" not in block["key_design_note"]

    def test_connects_to_all_exist_in_profiles(self):
        for m in CONNECTS_TO:
            r = run_git("grep", "-l", "mechanism_id: %d$" % m, "--", "profiles/")
            assert r.stdout.strip() != "", m
        assert load_block()["connects_to"] == CONNECTS_TO

    def test_rotation_transparency_names_window_and_predecessor(self):
        rt = load_block()["rotation_transparency"]
        assert "1010-1014" in rt
        assert "#1012" in rt
        assert "788bc9a8d2099253160b7303ff09a70a0a10be74" in rt


# ---------------------------------------------------------------------------
# 4. Evidence: three carried arms (per #807)
# ---------------------------------------------------------------------------
class TestEvidence1013:
    def test_three_arms_each_with_tone(self):
        block = load_block()
        for arm_key in ("meta_arm_stigma", "meta_arm_baseline", "apple_arm"):
            arm = block[arm_key]
            assert "piece" in arm and "date" in arm
            assert "tone_illustrative" in arm

    def test_all_arm_urls_already_in_corpus(self):
        # All arms CARRIED this run; the journalist-angle block is the novelty.
        for url in CARRIED_URLS:
            r = run_git("grep", "-l", "-F", url, "--", "profiles/")
            files = [f for f in r.stdout.splitlines() if f]
            assert "profiles/careers/journalists.yaml" in files, url

    def test_arm_dates(self):
        block = load_block()
        assert block["meta_arm_stigma"]["date"] == "2026-09-24"
        assert block["meta_arm_baseline"]["date"] == "2025-09-17"
        assert block["apple_arm"]["date"] == "2024-08-16"

    def test_meta_stigma_arm_score_carried_from_832(self):
        arm = load_block()["meta_arm_stigma"]
        assert arm["tone_illustrative"] == -0.20
        assert "un-rescored" in arm["tone_status"]
        assert "mechanism 832" in arm["tone_status"]
        assert "perv glasses" in arm["evidence_quotes"][0]
        assert arm["byline"] == "Samuel Gibbs"

    def test_meta_baseline_and_apple_arms_carried(self):
        block = load_block()
        baseline = block["meta_arm_baseline"]
        assert baseline["tone_illustrative"] == 0.10
        assert "un-rescored" in baseline["tone_status"]
        assert "mechanism 611" in baseline["tone_status"]
        apple = block["apple_arm"]
        assert apple["tone_illustrative"] == 0.35
        assert "un-rescored" in apple["tone_status"]
        assert apple["byline"] == "Samuel Gibbs"


# ---------------------------------------------------------------------------
# 5. Scores: temporal shift, means and delta
# ---------------------------------------------------------------------------
class TestScores1013:
    def test_temporal_shift_and_delta(self):
        means = load_block()["illustrative_means"]
        assert abs(means["temporal_shift_meta"] - (-0.30)) < 1e-9
        assert "(-0.20) - (0.10) = -0.30" in means["temporal_shift_calc"]
        assert abs(means["delta"] - (-0.55)) < 1e-9
        assert "(-0.20) - (0.35) = -0.55" in means["delta_calc"]

    def test_delta_is_meta_minus_apple_widened_from_611(self):
        means = load_block()["illustrative_means"]
        assert "Meta minus Apple" in means["delta_calc"]
        assert "m611" in means["delta_calc"] or "-0.25" in means["delta_calc"]

    def test_no_scorer_run(self):
        sd = load_block()["statistical_discipline"]
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "MANUAL_ILLUSTRATIVE_CARRIED"

    def test_scorer_result_fields(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert abs(
            scorer["illustrative_delta_meta_minus_apple"] - (-0.55)
        ) < 1e-9
        assert abs(scorer["illustrative_temporal_shift_meta"] - (-0.30)) < 1e-9
        assert scorer["target_entity"] == "meta"
        assert scorer["reference_entity"] == "apple"
        assert scorer["artifact_grade"] is False


# ---------------------------------------------------------------------------
# 6. Statistical discipline per the Aug 28 2026 standing rule
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline1013:
    def test_manual_illustrative_only(self):
        sd = load_block()["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false_engine_not_run(self):
        sd = load_block()["statistical_discipline"]
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False

    def test_verdict_directionally_supported_not_proven(self):
        sd = load_block()["statistical_discipline"]
        assert sd["verdict"] == "directionally_supported_not_proven"

    def test_no_analysis_json_update(self):
        assert load_block()["no_analysis_json_update"] is True

    def test_cautious_language_required(self):
        block = load_block()
        assert block["cautious_language_required"] is True
        assert "Correlation only" in block["correlational_note"]


# ---------------------------------------------------------------------------
# 7. Corpus novelty sweeps (post-insert guards)
# ---------------------------------------------------------------------------
class TestCorpusNovelty1013:
    def test_max_numeric_mechanism_id_is_839(self):
        r = run_git("grep", "-h", "-o", "-P", r"mechanism_id:\s*\K[0-9]+",
                    "--", "profiles/")
        ids = sorted(
            int(m.group(1))
            for line in r.stdout.splitlines()
            for m in [re.match(r"([0-9]+)$", line)]
            if m
        )
        assert ids[-1] == MECHANISM

    def test_zero_underscore_840_repo_wide(self):
        r = run_git("grep", "-l", NEXT_ID_MARKER,
                    "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_dash_840_repo_wide(self):
        r = run_git("grep", "-l", NEXT_DASH_MARKER,
                    "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_numeric_840_in_profiles(self):
        r = run_git("grep", "-l", "mechanism_id: 840$", "--", "profiles/")
        assert r.stdout.strip() == ""


# ---------------------------------------------------------------------------
# 8. Falsification ledger
# ---------------------------------------------------------------------------
class TestLedger1013:
    def test_not_falsification_family_member(self):
        assert load_block()["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        block = load_block()
        assert block["falsification_ledger"] == 30
        assert "holds at 30" in block["falsification_note"]


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (fail pre-commit, green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSync1013:
    def test_readme_pre_run_values_still_present(self):
        # Pre-run values carried in the new test-file table row's
        # doc-sync prose (52029/1337 -> NEW), so they remain present
        # after the header counts are bumped.
        readme = _read(README)
        assert "52029" in readme and "1337" in readme

    def test_readme_table_row_for_1013(self):
        assert ("`tests/" + THIS_FILE + "`") in _read(README)

    def test_architecture_tree_row_for_1013(self):
        assert THIS_FILE.replace(".py", "") in _read(ARCH)


# ---------------------------------------------------------------------------
# 10. Push readiness
# ---------------------------------------------------------------------------
class TestPushReadiness1013:
    def test_ascii_only_no_em_dashes(self):
        # Scopes to the new test file and the m839 block only: the profile
        # carries pre-existing unicode in older sections, untouched by design.
        for text in (open(__file__, encoding="utf-8").read(),
                     yaml.safe_dump(load_block())):
            text.encode("ascii")
            assert "\u2014" not in text  # em dash via unicode escape
            assert "\u2013" not in text  # en dash via unicode escape

    def test_hash_placeholders_filled_post_followup(self):
        # Fails pre-commit per the #721 convention: this run's own main/anchor
        # SHAs are only known after the commits land, then patched into the log.
        # Predecessor (#1012) hashes are cited in Rotation transparency and do
        # not count; at least the main + anchor SHAs of #1013 must be present.
        text = _read(LOG)
        entry = text.split("## #1013")[1].split("## #1012")[0]
        own_hashes = {
            h for h in re.findall(r"\b[0-9a-f]{40}\b", entry)
            if h not in PREDECESSOR_SHAS
        }
        assert len(own_hashes) >= 2

    def test_staged_set_exactly_five_paths_and_concurrency_untouched(self):
        # Fails pre-commit by design: staging happens at commit time.
        r = run_git("diff", "--cached", "--name-only")
        staged = {f for f in r.stdout.splitlines() if f}
        assert staged == STAGED_SET
        # Concurrency: #899 (nytimes.yaml m771 hunk), #938 (anchor patch),
        # #900 (untracked test) all stay out of this run's index.
        r2 = run_git("status", "--porcelain")
        idx = {line[3:] for line in r2.stdout.splitlines()
               if line[:2] in ("M ", "A ")}
        assert "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py" not in idx
        assert "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py" not in idx
        assert "profiles/competitor-entities.yaml" not in idx
        r3 = run_git("diff", "--", "profiles/nytimes.yaml")
        assert "spur_licensing_market_exists_coalition_founder_datum_unsealed_filings_wave_sep2026" in r3.stdout
