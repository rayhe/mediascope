"""Type B #1008 (2026-09-26 03:00 PDT): Lily Hay Newman (WIRED) Sep-23 Meta
Connect "Pinky Promises" co-byline vs Sep-9 Apple Watch Audio Intelligence -
PEG-MATCHED replication of mechanism 635. Fourth leg of the 1005-1009 window
(D #1005 -> E #1006 -> A #1007 -> B #1008).

NEW arm (excerpt/mirror-tier per #503): WIRED "Meta Pinky Promises Its Smart
Glasses Will Be Private Soon" (co-byline attested "Boone Ashworth, Lily Hay
Newman Sep 23, 2026, 7:30 pm" via the technewstube verbatim WIRED mirror;
dek "The company is bringing its Private Processing encryption service to
its much-maligned smart glasses"). The piece is already corpus-recorded at
m814/m820 as Ashworth-attributed; NEW this run is the Newman CO-BYLINE
attestation via the new-to-corpus technewstube mirror URL. CARRIED Apple arm
(un-rescored per #807, from m635): WIRED "Apple Doesn't Want You to Worry
About the New Apple Watch's Listening Features" (solo Newman, Sep 9 2026
3:14 pm; dek with the skeptical caveat "But the protections cannot change
the facts of what the tools do"). Both arms are company privacy-assurance
announcements on microphone/surveillance-adjacent wearables; carried
illustrative tones Meta -0.45 (m820) vs Apple +0.10 (m635); illustrative
delta (Meta minus Apple) -0.55. The m635 trust-deficit finding EXTENDS to a
privacy-pledge peg-matched pair, weakening the news-peg confound.

Statistical discipline per the Aug 28 2026 standing rule: MANUAL ILLUSTRATIVE
scores only (both tones carried un-rescored), p_value/cohens_d/ci
NOT_CALCULATED, is_significant False, engine NOT run at the finding layer;
verdict directionally_supported_not_proven; no analysis.json update; NOT
artifact-grade; NOT falsification-family member; ledger holds at 30.

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

ANCHORED_SHA = "e9ffd2ec4cb8435aa29413f8dc65082d9cea8edc"  # patched in the anchor followup per #565

ITERATION = 1008
MECHANISM = 836
BLOCK_KEY = (
    "type_b_1008_lily_hay_newman_meta_connect_pinky_promises_vs_"
    "apple_watch_audio_intelligence_reassurance_sep26"
)

NEW_URLS = [
    "https://technewstube.com/wired/1870105/meta-pinky-promises-smart-glasses-private/",
]

CONNECTS_TO = [635, 814, 820]

EXPECTED_TESTS = 41
README_TESTS_BEFORE, README_TESTS_AFTER = 51789, 51830
README_FILES_BEFORE, README_FILES_AFTER = 1332, 1333

MECH_ID_MARKER = "mechanism" + "_836"
NEXT_ID_MARKER = "mechanism" + "_837"
NEXT_DASH_MARKER = "mechanism" + "-837"

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
        j for j in data["journalists"] if j.get("name") == "Lily Hay Newman"
    )
    return item[BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty per the Aug 31 standing rule
# ---------------------------------------------------------------------------
class TestNovelty1008:
    def test_single_type_b_1008_test_file(self):
        files = sorted(
            f for f in os.listdir(os.path.join(str(REPO), "tests"))
            if f.startswith("test_type_b_1008") and f.endswith(".py")
        )
        assert files == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type B #1008" in r2.stdout

    def test_no_type_b_1008_in_git_log_precommit(self):
        r = run_git("log", "--format=%H %s", "--grep", "Type B #1008")
        own = run_git(
            "log", "--format=%H", "--", "tests/" + THIS_FILE
        ).stdout
        hits = [
            line for line in r.stdout.splitlines()
            if line.split()[0] not in own.split()
        ]
        assert hits == []


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1005-1009 window, fourth leg
# ---------------------------------------------------------------------------
class TestRotationGuard1008:
    def test_window_legs_in_iteration_log(self):
        text = _read(LOG)
        assert "## #1005 Type D" in text
        assert "## #1006 Type E" in text
        assert "## #1007 Type A" in text
        assert "1005-1009" in text

    @pytest.mark.rotation
    def test_fourth_leg_of_1005_to_1009_window(self):
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "B"
        assert "1005-1009 window" in block["rotation_transparency"]
        assert "FOURTH leg" in block["rotation_transparency"]

    @pytest.mark.rotation
    def test_predecessor_1007_type_a_committed(self):
        r = run_git("log", "--oneline", "--grep", "Type A #1007")
        assert r.stdout.strip() != ""
        assert (
            REPO
            / "tests"
            / "test_type_a_1007_nyt_anthropic_sep2026_ipo_scoop_momentum_vs_meta_connect_relay_ice_enforcement_sep26_2am.py"
        ).exists()

    @pytest.mark.rotation
    def test_no_successor_1009_type_c_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type C #1009")
        assert r.stdout.strip() == ""
        assert "## #1009" not in _read(LOG)

    @pytest.mark.rotation
    def test_no_concurrent_type_b_1008_by_commit_time(self):
        r = run_git("log", "--format=%H %s", "--grep", "Type B #1008")
        matches = [line for line in r.stdout.splitlines() if line.strip()]
        own = run_git(
            "log", "--format=%H", "--", "tests/" + THIS_FILE
        ).stdout.split()
        competing = [line for line in matches if line.split()[0] not in own]
        assert competing == []


# ---------------------------------------------------------------------------
# 3. Mechanism 836 block content
# ---------------------------------------------------------------------------
class TestMechanism836Content:
    def test_block_key_unique_at_indent_2(self):
        hits = [
            line for line in _read(PROFILE).splitlines()
            if line == "  " + BLOCK_KEY + ":"
        ]
        assert len(hits) == 1

    def test_mechanism_id_836_iteration_1008_type_b(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "B"
        assert block["type"] == "B"

    def test_journalist_and_publication(self):
        block = load_block()
        assert block["journalist"] == "Lily Hay Newman"
        assert block["publication"] == "WIRED (Conde Nast)"

    def test_publication_author_goal_job_fields(self):
        block = load_block()
        assert block["author"] == "Kit (with Ray)"
        assert block["goal_id"] == "goal_54093bda4145"
        assert block["job_id"] == "mediascope-daily-iteration"
        assert block["date_analyzed"] == "2026-09-26"
        assert block["time_pdt"] == "03:00"

    def test_key_design_note_no_numeric_substring(self):
        block = load_block()
        assert MECH_ID_MARKER not in BLOCK_KEY
        assert NEXT_ID_MARKER not in BLOCK_KEY
        assert "key_design_note" in block
        assert "mechanism" + "_836" not in block["key_design_note"]

    def test_connects_to_all_exist_in_profiles(self):
        for m in CONNECTS_TO:
            r = run_git("grep", "-l", "mechanism_id: %d$" % m, "--", "profiles/")
            assert r.stdout.strip() != "", m
        assert load_block()["connects_to"] == CONNECTS_TO

    def test_rotation_transparency_names_window_and_predecessor(self):
        rt = load_block()["rotation_transparency"]
        assert "1005-1009" in rt
        assert "#1007" in rt
        assert "a0d351d30e8d3ad359c79fd4c0187cb67bfc11b7" in rt


# ---------------------------------------------------------------------------
# 4. Evidence: new Meta arm + carried Apple arm
# ---------------------------------------------------------------------------
class TestEvidence1008:
    def test_two_arms_each_with_tone(self):
        block = load_block()
        for arm_key in ("meta_arm", "apple_arm"):
            arm = block[arm_key]
            assert "piece" in arm and "date" in arm
            assert "tone_illustrative" in arm

    def test_new_url_first_appearance(self):
        for url in NEW_URLS:
            assert url in yaml.safe_dump(load_block()), url
            r = run_git("grep", "-l", "-F", url, "--", "profiles/")
            assert [f for f in r.stdout.splitlines() if f] == [
                "profiles/careers/journalists.yaml"
            ], url

    def test_arm_dates(self):
        block = load_block()
        assert block["meta_arm"]["date"] == "2026-09-23"
        assert block["apple_arm"]["date"] == "2026-09-09"

    def test_meta_arm_score_carried_unrescored(self):
        arm = load_block()["meta_arm"]
        assert arm["tone_illustrative"] == -0.45
        assert "un-rescored" in arm["tone_status"]
        assert "mechanism 820" in arm["tone_status"]
        assert "much-maligned" in arm["byline_attestation"]
        assert "Boone Ashworth, Lily Hay Newman" in arm["byline"]

    def test_apple_arm_score_carried_unrescored(self):
        arm = load_block()["apple_arm"]
        assert arm["tone_illustrative"] == 0.10
        assert "un-rescored" in arm["tone_status"]
        assert "mechanism 635" in arm["tone_status"]
        assert arm["byline"] == "Lily Hay Newman"


# ---------------------------------------------------------------------------
# 5. Scores: illustrative means and delta
# ---------------------------------------------------------------------------
class TestScores1008:
    def test_means_and_delta(self):
        means = load_block()["illustrative_means"]
        assert abs(means["meta_mean"] - (-0.45)) < 1e-9
        assert abs(means["apple_mean"] - 0.10) < 1e-9
        assert abs(means["delta"] - (-0.55)) < 1e-9
        assert "(-0.45) - (0.10) = -0.55" in means["delta_calc"]

    def test_delta_is_meta_minus_apple(self):
        means = load_block()["illustrative_means"]
        assert "Meta minus Apple" in means["delta_calc"]

    def test_no_scorer_run(self):
        sd = load_block()["statistical_discipline"]
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "MANUAL_ILLUSTRATIVE_CARRIED"

    def test_scorer_result_fields(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert abs(
            scorer["illustrative_delta_meta_minus_apple"] - (-0.55)
        ) < 1e-9
        assert scorer["target_entity"] == "meta"
        assert scorer["reference_entity"] == "apple"
        assert scorer["artifact_grade"] is False


# ---------------------------------------------------------------------------
# 6. Statistical discipline per the Aug 28 2026 standing rule
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline1008:
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
class TestCorpusNovelty1008:
    def test_max_numeric_mechanism_id_is_836(self):
        r = run_git("grep", "-h", "-o", "-P", r"mechanism_id:\s*\K[0-9]+",
                    "--", "profiles/")
        ids = sorted(
            int(m.group(1))
            for line in r.stdout.splitlines()
            for m in [re.match(r"([0-9]+)$", line)]
            if m
        )
        assert ids[-1] == MECHANISM

    def test_zero_underscore_837_repo_wide(self):
        r = run_git("grep", "-l", NEXT_ID_MARKER,
                    "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_dash_837_repo_wide(self):
        r = run_git("grep", "-l", NEXT_DASH_MARKER,
                    "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_numeric_837_in_profiles(self):
        r = run_git("grep", "-l", "mechanism_id: 837$", "--", "profiles/")
        assert r.stdout.strip() == ""


# ---------------------------------------------------------------------------
# 8. Falsification ledger
# ---------------------------------------------------------------------------
class TestLedger1008:
    def test_not_falsification_family_member(self):
        assert load_block()["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        block = load_block()
        assert block["falsification_ledger"] == 30
        assert "holds at 30" in block["falsification_note"]


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (fail pre-commit, green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSync1008:
    def test_readme_pre_run_values_still_present(self):
        # Pre-run values carried in the new test-file table row's
        # doc-sync prose (51789/1332 -> NEW), so they remain present
        # after ARCHITECTURE's tree row is bumped.
        readme = _read(README)
        assert "51789" in readme and "1332" in readme

    def test_readme_table_row_for_1008(self):
        assert ("`tests/" + THIS_FILE + "`") in _read(README)

    def test_architecture_tree_row_for_1008(self):
        assert THIS_FILE.replace(".py", "") in _read(ARCH)


# ---------------------------------------------------------------------------
# 10. Push readiness
# ---------------------------------------------------------------------------
class TestPushReadiness1008:
    def test_ascii_only_no_em_dashes(self):
        # Scopes to the new test file and the m836 block only: the profile
        # carries pre-existing unicode in older sections, untouched by design.
        for text in (open(__file__, encoding="utf-8").read(),
                     yaml.safe_dump(load_block())):
            text.encode("ascii")
            assert "\u2014" not in text  # em dash via unicode escape
            assert "\u2013" not in text  # en dash via unicode escape

    def test_hash_placeholders_filled_post_followup(self):
        # Fails pre-commit per the #721 convention: this run's own main/anchor
        # SHAs are only known after the commits land, then patched into the log.
        # Predecessor (#1007) hashes are cited in Rotation transparency and do
        # not count; at least the main + anchor SHAs of #1008 must be present.
        text = _read(LOG)
        entry = text.split("## #1008")[1].split("## #1007")[0]
        own_hashes = {
            h for h in re.findall(r"\b[0-9a-f]{40}\b", entry)
            if h != "a0d351d30e8d3ad359c79fd4c0187cb67bfc11b7"
        }
        assert len(own_hashes) >= 2

    def test_staged_set_exactly_five_paths_and_concurrency_untouched(self):
        # Fails pre-commit by design: staging happens at commit time.
        r = run_git("diff", "--cached", "--name-only")
        staged = {f for f in r.stdout.splitlines() if f}
        assert staged == STAGED_SET
        # Concurrency: #899 (nytimes.yaml m771 hunk), #938 (anchor patch),
        # #900 (untracked test), #884 (competitor-entities.yaml m762) all stay
        # out of this run's index.
        r2 = run_git("status", "--porcelain")
        idx = {line[3:] for line in r2.stdout.splitlines()
               if line[:2] in ("M ", "A ")}
        assert "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py" not in idx
        assert "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py" not in idx
        assert "profiles/competitor-entities.yaml" not in idx
        r3 = run_git("diff", "--", "profiles/nytimes.yaml")
        assert "spur_licensing_market_exists_coalition_founder_datum_unsealed_filings_wave_sep2026" in r3.stdout
