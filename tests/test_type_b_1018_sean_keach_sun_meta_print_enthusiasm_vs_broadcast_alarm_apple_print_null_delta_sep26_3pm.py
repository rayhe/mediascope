"""Type B #1018 (2026-09-26 15:00 PDT): Sean Keach (The Sun / News Corp)
cross-medium register control - print hands-on enthusiasm for BOTH Meta and
Apple (NULL cross-entity delta) vs broadcast alarm on Meta (TalkTV, carried
from the #182 Type E News Corp financial-paradox entry). Fourth leg of the
1015-1019 window (D #1015 -> E #1016 -> A #1017 -> B #1018).

CROSS-MEDIUM NULL-DELTA CONTROL. Resolves the #978/#983 Keach rejections
("no within-journalist competitor pair in corpus scope") with newly surfaced
Keach Apple arms (2024 Vision Pro daily-wear review + Jul-2024 Tim Cook
Vision Pro interview).

PRIMARY PAIR (genre-matched hands-on reviews): Keach's Sep-2026 Meta VR
Glasses hands-on ("I COULDN'T believe my eyes. How has Meta managed this?",
"it's thrilling to see the kind of breakthrough gadget like the Meta VR
Glasses that genuinely shock me") at MANUAL ILLUSTRATIVE +0.40 vs his 2024
Apple Vision Pro review ("I've been wearing hi-tech headset every day -
there are three places I'm obsessed with using it"; in-mirror credit
"Credit: Sean Keach / The Sun") at MANUAL ILLUSTRATIVE +0.35. Illustrative
delta (Meta minus Apple) +0.05, NOT significant: the same writer applies the
same enthusiastic review register to both entities, genre held constant.

SUPPORTING PAIR (exec interviews, genre-matched): Keach's Sep-2026 Boz
interview ("The Sun's Sean Keach talked to Boz about Meta's latest gadgets")
vs his Jul-2024 Tim Cook Vision Pro interview (9to5mac relay, "Sean Keach
writes:"), both symmetric company-leader messaging relays.

WITHIN-WRITER MEDIUM SPLIT (carried arm): the same Keach's TalkTV broadcast
segment on Meta glasses (~Jul 9 2026, "They Can SEE EVERYTHING!", sentiment
-7/10 in the #182 Type E entry, carried at -0.70) is alarm-register on the
SAME entity his print register treats enthusiastically: illustrative medium
split (broadcast minus print) -1.10, isolating MEDIUM/GENRE as the register
driver. The #182 News Corp financial paradox carries forward: News Corp
receives Meta content partnership revenue (Active; litigation partner AND
content partner) yet Keach alarms on Meta on broadcast TV, and News Corp
takes OpenAI $250M/5yr licensing while OpenAI's companion device gets neutral
coverage - money predicts neither the print enthusiasm (Apple $0, equally
soft) nor the broadcast alarm (Meta revenue-positive, still alarmed).

Statistical discipline per the Aug 28 2026 standing rule: MANUAL
ILLUSTRATIVE scores only (four of five arms NEW this run, hand-assigned; the
broadcast arm tone CARRIED un-rescored from #182 per #807),
p_value/cohens_d/ci NOT_CALCULATED, is_significant False, engine NOT run at
the finding layer; verdict directionally_supported_not_proven; no
analysis.json update; NOT artifact-grade; NOT falsification-family member;
ledger holds at 30.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4
(patched green in the anchor followup). Doc-sync 3 fail pre-commit per #719,
all green post-doc-sync; iteration-log newest-entry green; hash-placeholder
test fails pre-commit per the #721 convention; staged-set test fails
pre-commit by design.
42 tests, 10 classes. ASCII only, no em dashes.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
PROFILE = REPO / "profiles" / "careers" / "journalists.yaml"
PODCAST = REPO / "podcast-sentiment.md"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"
LOG = REPO / "iteration-log.md"
THIS_FILE = Path(__file__).name

ANCHORED_SHA = "97df5870a4fc675eeb7ef97e55efbe0634ff5097"  # patched in the anchor followup per #565

ITERATION = 1018
MECHANISM = 842
BLOCK_KEY = (
    "type_b_1018_sean_keach_sun_cross_medium_register_meta_print_"
    "enthusiasm_vs_broadcast_alarm_apple_print_null_delta"
)

# Five arms: four NEW this run, one CARRIED from the #182 Type E entry.
NEW_URLS = [
    "https://www.thesun.co.uk/tech/40467585/meta-vr-glasses-virtual-reality-specs-features-price-review/",
    "https://www.thescottishsun.co.uk/tech/16866229/meta-vr-glasses-boz-andrew-bosworth-ray-ban-audio/",
    "https://newstextarea.com/deutsch/apple-vision-pro-review-ive-been-wearing-hi-tech-headset-every-day-there-are-three-places-im-obsessed-with-using-it",
    "https://9to5mac.com/2024/07/11/tim-cook-explains-what-he-thinks-vision-pro-is-good-for/",
    "https://thesuntech.substack.com/p/my-big-surprise-wearing-the-apple",
    "https://www.thesun.co.uk/tech/38801942/apple-smart-glasses-iphone-face-release-headset-meta-features/",
]
# The TalkTV broadcast arm is CARRIED from the #182 Type E corpus entry.
CARRIED_BROADCAST_URL = "https://www.youtube.com/watch?v=LspLdcz9uqQ"

CONNECTS_TO = [181, 818, 839]

PREDECESSOR_SHAS = {
    "97df5870a4fc675eeb7ef97e55efbe0634ff5097",  # #1017 main
    "3d8c8155fc81536924591a84ebe8eb682ab4dca2",  # #1017 anchor
    "306853614780b784dd83403a636864fd9971e1c2",  # #1017 log-hash
}

EXPECTED_TESTS = 42
README_TESTS_BEFORE, README_TESTS_AFTER = 52278, 52320
README_FILES_BEFORE, README_FILES_AFTER = 1342, 1343

MECH_ID_MARKER = "mechanism" + "_842"
NEXT_ID_MARKER = "mechanism" + "_843"
NEXT_DASH_MARKER = "mechanism" + "-843"

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
        j for j in data["journalists"] if j.get("name") == "Sean Keach"
    )
    return item["competitor_coverage"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty per the Aug 31 standing rule
# ---------------------------------------------------------------------------
class TestNovelty1018:
    def test_single_type_b_1018_test_file(self):
        files = sorted(
            f for f in os.listdir(os.path.join(str(REPO), "tests"))
            if f.startswith("test_type_b_1018") and f.endswith(".py")
        )
        assert files == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type B #1018" in r2.stdout

    def test_no_type_b_1018_in_git_log_precommit(self):
        r = run_git("log", "--format=%H %s", "--grep", "Type B #1018")
        own = run_git(
            "log", "--format=%H", "--", "tests/" + THIS_FILE
        ).stdout
        hits = [
            line for line in r.stdout.splitlines()
            if line.split()[0] not in own.split()
        ]
        assert hits == []


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1015-1019 window, fourth leg
# ---------------------------------------------------------------------------
class TestRotationGuard1018:
    def test_window_legs_in_iteration_log(self):
        text = _read(LOG)
        assert "## #1015 Type D" in text
        assert "## #1016 Type E" in text
        assert "## #1017 Type A" in text
        assert "1015-1019" in text

    @pytest.mark.rotation
    def test_fourth_leg_of_1015_to_1019_window(self):
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "B"
        assert "1015-1019 window" in block["rotation_transparency"]
        assert "FOURTH leg" in block["rotation_transparency"]

    @pytest.mark.rotation
    def test_predecessor_1017_type_a_committed(self):
        r = run_git("log", "--oneline", "--grep", "Type A #1017")
        assert r.stdout.strip() != ""
        assert (
            REPO
            / "tests"
            / "test_type_a_1017_verge_microsoft_sep2026_copyright_defense_headline_register_vs_meta_connect_backlash_framing_pcm_licensing_gradient_sep26_2pm.py"
        ).exists()

    @pytest.mark.rotation
    def test_no_successor_1019_type_c_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type C #1019")
        assert r.stdout.strip() == ""
        assert "## #1019" not in _read(LOG)

    @pytest.mark.rotation
    def test_no_concurrent_type_b_1018_by_commit_time(self):
        r = run_git("log", "--format=%H %s", "--grep", "Type B #1018")
        matches = [line for line in r.stdout.splitlines() if line.strip()]
        own = run_git(
            "log", "--format=%H", "--", "tests/" + THIS_FILE
        ).stdout.split()
        competing = [line for line in matches if line.split()[0] not in own]
        assert competing == []


# ---------------------------------------------------------------------------
# 3. Mechanism 842 block content
# ---------------------------------------------------------------------------
class TestMechanism842Content:
    def test_block_key_unique_at_indent_4(self):
        hits = [
            line for line in _read(PROFILE).splitlines()
            if line == "    " + BLOCK_KEY + ":"
        ]
        assert len(hits) == 1

    def test_mechanism_id_842_iteration_1018_type_b(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "B"
        assert block["type"] == "B"

    def test_journalist_and_publication(self):
        block = load_block()
        assert block["journalist"] == "Sean Keach"
        assert block["publication"] == "The Sun (News Corp)"

    def test_publication_author_goal_job_fields(self):
        block = load_block()
        assert block["author"] == "Kit (with Ray)"
        assert block["goal_id"] == "goal_54093bda4145"
        assert block["job_id"] == "mediascope-daily-iteration"
        assert block["date_analyzed"] == "2026-09-26"
        assert block["time_pdt"] == "15:00"

    def test_key_design_note_no_numeric_substring(self):
        block = load_block()
        assert MECH_ID_MARKER not in BLOCK_KEY
        assert NEXT_ID_MARKER not in BLOCK_KEY
        assert "key_design_note" in block
        assert "mechanism" + "_842" not in block["key_design_note"]

    def test_connects_to_all_exist_in_profiles(self):
        for m in CONNECTS_TO:
            r = run_git("grep", "-l", "mechanism_id: %d$" % m, "--", "profiles/")
            assert r.stdout.strip() != "", m
        assert load_block()["connects_to"] == CONNECTS_TO

    def test_rotation_transparency_names_window_and_predecessor(self):
        rt = load_block()["rotation_transparency"]
        assert "1015-1019" in rt
        assert "#1017" in rt
        assert "97df5870a4fc675eeb7ef97e55efbe0634ff5097" in rt


# ---------------------------------------------------------------------------
# 4. Evidence: four NEW arms + one CARRIED broadcast arm (per #807)
# ---------------------------------------------------------------------------
class TestEvidence1018:
    def test_five_arms_each_with_tone(self):
        block = load_block()
        for arm_key in (
            "meta_arm_print",
            "meta_arm_supporting",
            "meta_arm_broadcast",
            "apple_arm_print",
            "apple_arm_supporting",
        ):
            arm = block[arm_key]
            assert "piece" in arm and "date" in arm
            assert "tone_illustrative" in arm

    def test_new_arm_urls_in_corpus_post_insert(self):
        # The journalist-angle block is the novelty; the four NEW arm URLs
        # land in profiles/careers/journalists.yaml with this run.
        for url in NEW_URLS:
            r = run_git(
                "grep", "-l", "-F", url, "--", "profiles/careers/journalists.yaml"
            )
            assert r.stdout.strip() != "", url

    def test_broadcast_arm_carried_from_182_entry(self):
        # The TalkTV segment URL is already corpus-recorded in
        # podcast-sentiment.md (Iteration #182 Type E); the novelty is the
        # journalist-angle mechanism-ization, not the URL.
        assert CARRIED_BROADCAST_URL in _read(PODCAST)

    def test_arm_dates(self):
        block = load_block()
        assert block["meta_arm_print"]["date"] == "2026-09-24"
        assert block["meta_arm_broadcast"]["date"] == "2026-07-09"
        assert block["apple_arm_supporting"]["date"] == "2024-07-11"

    def test_meta_print_arm_score_new_and_quotes(self):
        arm = load_block()["meta_arm_print"]
        assert arm["tone_illustrative"] == 0.40
        assert "NEW this run" in arm["tone_status"]
        assert "I COULDN" in arm["evidence_quotes"][1]
        assert "genuinely shock me" in arm["evidence_quotes"][2]
        assert arm["byline"] == "Sean Keach"

    def test_broadcast_arm_score_carried_from_182(self):
        arm = load_block()["meta_arm_broadcast"]
        assert arm["tone_illustrative"] == -0.70
        assert "un-rescored" in arm["tone_status"]
        assert "#182" in arm["tone_status"]
        assert "SEE EVERYTHING" in arm["evidence_quotes"][0]


# ---------------------------------------------------------------------------
# 5. Scores: null cross-entity delta and the medium split
# ---------------------------------------------------------------------------
class TestScores1018:
    def test_null_delta_and_medium_split(self):
        means = load_block()["illustrative_means"]
        assert abs(means["delta"] - 0.05) < 1e-9
        assert "(0.40) - (0.35) = +0.05" in means["delta_calc"]
        assert abs(means["medium_split"] - (-1.10)) < 1e-9
        assert "(-0.70) - (0.40) = -1.10" in means["medium_split_calc"]

    def test_delta_is_meta_minus_apple_null(self):
        means = load_block()["illustrative_means"]
        assert "Meta print minus Apple print" in means["delta_calc"]
        assert "NULL cross-entity delta" in means["delta_calc"]

    def test_no_scorer_run(self):
        sd = load_block()["statistical_discipline"]
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "MANUAL_ILLUSTRATIVE_NEW"

    def test_scorer_result_fields(self):
        scorer = load_block()["asymmetry_scorer_result"]
        assert abs(
            scorer["illustrative_delta_meta_minus_apple"] - 0.05
        ) < 1e-9
        assert abs(
            scorer["illustrative_medium_split_broadcast_minus_print"] - (-1.10)
        ) < 1e-9
        assert scorer["target_entity"] == "meta"
        assert scorer["reference_entity"] == "apple"
        assert scorer["artifact_grade"] is False


# ---------------------------------------------------------------------------
# 6. Statistical discipline per the Aug 28 2026 standing rule
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline1018:
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
class TestCorpusNovelty1018:
    def test_max_numeric_mechanism_id_is_842(self):
        r = run_git("grep", "-h", "-o", "-P", r"mechanism_id:\s*\K[0-9]+",
                    "--", "profiles/")
        ids = sorted(
            int(m.group(1))
            for line in r.stdout.splitlines()
            for m in [re.match(r"([0-9]+)$", line)]
            if m
        )
        assert ids[-1] == MECHANISM

    def test_zero_underscore_843_repo_wide(self):
        r = run_git("grep", "-l", NEXT_ID_MARKER,
                    "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_dash_843_repo_wide(self):
        r = run_git("grep", "-l", NEXT_DASH_MARKER,
                    "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_numeric_843_in_profiles(self):
        r = run_git("grep", "-l", "mechanism_id: 843$", "--", "profiles/")
        assert r.stdout.strip() == ""


# ---------------------------------------------------------------------------
# 8. Falsification ledger
# ---------------------------------------------------------------------------
class TestLedger1018:
    def test_not_falsification_family_member(self):
        assert load_block()["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        block = load_block()
        assert block["falsification_ledger"] == 30
        assert "holds at 30" in block["falsification_note"]


# ---------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719 (fail pre-commit, green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSync1018:
    def test_readme_pre_run_values_still_present(self):
        # Pre-run values carried in the new test-file table row's
        # doc-sync prose (52278/1342 -> NEW), so they remain present
        # after the header counts are bumped.
        readme = _read(README)
        assert "52278" in readme and "1342" in readme

    def test_readme_table_row_for_1018(self):
        assert ("`tests/" + THIS_FILE + "`") in _read(README)

    def test_architecture_tree_row_for_1018(self):
        assert THIS_FILE.replace(".py", "") in _read(ARCH)


# ---------------------------------------------------------------------------
# 10. Push readiness
# ---------------------------------------------------------------------------
class TestPushReadiness1018:
    def test_ascii_only_no_em_dashes(self):
        # Scopes to the new test file and the m842 block only: the profile
        # carries pre-existing unicode in older sections, untouched by design.
        for text in (open(__file__, encoding="utf-8").read(),
                     yaml.safe_dump(load_block())):
            text.encode("ascii")
            assert "\u2014" not in text  # em dash via unicode escape
            assert "\u2013" not in text  # en dash via unicode escape

    def test_hash_placeholders_filled_post_followup(self):
        # Fails pre-commit per the #721 convention: this run's own main/anchor
        # SHAs are only known after the commits land, then patched into the log.
        # Predecessor (#1017) hashes are cited in Rotation transparency and do
        # not count; at least the main + anchor SHAs of #1018 must be present.
        text = _read(LOG)
        entry = text.split("## #1018")[1].split("## #1017")[0]
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
        # Concurrency: #899 (nytimes.yaml m771 hunk), #938 (Type B test file
        # anchor edit), #900 (untracked test), #1012 working-tree block-key
        # fix all stay out of this run's index.
        r2 = run_git("status", "--porcelain")
        idx = {line[3:] for line in r2.stdout.splitlines()
               if line[:2] in ("M ", "A ")}
        assert "profiles/nytimes.yaml" not in idx
        assert "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py" not in idx
        assert "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py" not in idx
        assert "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py" not in idx
        r3 = run_git("diff", "--", "profiles/nytimes.yaml")
        assert "spur_licensing_market_exists_coalition_founder_datum_unsealed_filings_wave_sep2026" in r3.stdout
