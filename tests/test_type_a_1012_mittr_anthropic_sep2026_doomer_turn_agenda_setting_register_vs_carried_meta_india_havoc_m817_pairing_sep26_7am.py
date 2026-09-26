"""Type A #1012 (2026-09-26 07:00 PDT): MIT Technology Review x Anthropic Sep-14
doomer-turn agenda-setting register vs carried MIT TR x Meta Sep-23 India havoc
investigation. Third leg of the 1010-1014 window (D #1010 -> E #1011 -> A #1012).

NEW finding (register selection, mechanism 838, EXTENDING mechanism 817's MIT TR
register-inversion strand to the Anthropic axis): in the Sep 14-23 2026 window MIT
Technology Review gave the Anthropic-led AI-slowdown consensus event the analytic
agenda-setting register while its Meta coverage stayed in the accountability
register. Anthropic arm (NEW this run): Will Douglas Heaven's Sep 14 2026 piece
"The AI industry has taken a doomer turn. What now?" (technologyreview.com/
2026/09/14/1144048, excerpt-attested this run, 0 browser.open per #503): Dario
Amodei's slowdown essay is the catalyst peg; the lab convergence (Amodei, Altman,
Hassabis, Musk) is framed as the industry's meaningful event of the week; MANUAL
ILLUSTRATIVE +0.10. Meta arm (CARRIED from mechanism 817, un-rescored per #807):
the Sep 23 2026 "Smart glasses are already causing havoc in India" investigation
(technologyreview.com/2026/09/23/1144953, full-text browser.open verified at #977),
havoc/accountability register; MANUAL ILLUSTRATIVE -0.60. Illustrative delta
(Anthropic minus Meta) +0.70 on a degenerate n=1 vs n=1 pair, NOT significant.
This is a register-selection finding, NOT a uniform-softness finding: the Sep-14
piece embeds its own IPO-optics demystification thesis and turns the skeptical
optic on OpenAI ("shelved a faulty product") as well.

Statistical discipline per the Aug 28 2026 standing rule: MANUAL ILLUSTRATIVE
scores only, p_value/cohens_d/ci NOT_CALCULATED, is_significant False, engine NOT
run at the finding layer; verdict directionally_supported_not_proven; no
analysis.json update; NOT artifact-grade; NOT falsification-family member; ledger
holds at 30. Excerpt-bounded per #503 (0 browser.open). Correlation is not
causation. Hypothesis-generating only. ASCII-only, no em dashes.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4
(patched green in the anchor followup). Doc-sync 3 fail pre-commit per #719, all
green post-doc-sync; iteration-log 2 fail pre-commit; hash-placeholder test fails
pre-commit per the #721 convention; staged-set test fails pre-commit by design.
46 tests, 11 classes. ASCII only, no em dashes.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, "profiles", "mit-tech-review.yaml")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
LOG = os.path.join(REPO, "iteration-log.md")
THIS_FILE = os.path.basename(__file__)

ANCHORED_SHA = "788bc9a8d2099253160b7303ff09a70a0a10be74"  # patched in the anchor followup per #565

ITERATION = 1012
MECHANISM = 838
BLOCK_KEY = (
    "type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_"
    "vs_carried_meta_india_havoc_m817_pairing_sep26_7am"
)

NEW_URLS = [
    "https://www.technologyreview.com/2026/09/14/1144048/"
    "the-ai-industry-has-taken-a-doomer-turn-what-now/",
]

CONNECTS_TO = [817, 15, 619, 685, 790]

EXPECTED_TESTS = 46
README_TESTS_BEFORE, README_TESTS_AFTER = 51983, 52029
README_FILES_BEFORE, README_FILES_AFTER = 1336, 1337

MECH_ID_MARKER = "mechanism" + "_838"
NEXT_ID_MARKER = "mechanism" + "_839"
NEXT_DASH_MARKER = "mechanism" + "-839"
NEXT_NUMERIC = "mechanism_id: " + "839"

STAGED_SET = {
    "profiles/mit-tech-review.yaml",
    "tests/" + THIS_FILE,
    "README.md",
    "docs/ARCHITECTURE.md",
    "iteration-log.md",
}

# Predecessor (#1011) SHAs, excluded from the own-hash set in the #721 test.
PREDECESSOR_HASHES = {
    "d9288ceb07ce1e4d6943193535a52dfe4ebe11bf",  # #1011 main
    "5542710e8d98af1dca44951ef861651f16abd806",  # #1011 anchor
    "8f2b19c4081f66b2b23f54e2ee4b9b90cd3ce9ea",  # #1011 log-hash
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
    return data["competitor_relationships"]["anthropic"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty per the Aug 31 standing rule
# ---------------------------------------------------------------------------
class TestNovelty1012:
    def test_single_type_a_1012_test_file(self):
        files = sorted(
            f for f in os.listdir(os.path.join(REPO, "tests"))
            if f.startswith("test_type_a_1012") and f.endswith(".py")
        )
        assert files == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type A #1012" in r2.stdout

    def test_no_type_a_1012_in_git_log_precommit(self):
        r = run_git("log", "--format=%H %s", "--grep", "Type A #1012")
        own = run_git("log", "--format=%H", "--", "tests/" + THIS_FILE).stdout
        hits = [
            line for line in r.stdout.splitlines()
            if line.split()[0] not in own.split()
        ]
        assert hits == []

    def test_block_key_zero_hit_precommit(self):
        # Post-commit: the block key lives in exactly two committed files.
        r = run_git("grep", "-l", "-F", BLOCK_KEY, "--", "profiles/")
        assert r.stdout.splitlines() == ["profiles/mit-tech-review.yaml"]
        r2 = run_git("grep", "-l", "-F", BLOCK_KEY, "--", "tests/")
        assert r2.stdout.splitlines() == ["tests/" + THIS_FILE]


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1010-1014 window, third leg
# ---------------------------------------------------------------------------
class TestRotationGuard1010_1014Window:
    def test_window_legs_in_iteration_log(self):
        text = _read(LOG)
        assert "## #1010 Type D" in text
        assert "## #1011 Type E" in text
        assert "1010-1014" in text

    @pytest.mark.rotation
    def test_third_leg_of_1010_to_1014_window(self):
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "A"
        assert "1010-1014 window third leg" in block["rotation_transparency"]

    @pytest.mark.rotation
    def test_predecessor_1011_type_e_committed(self):
        r = run_git("log", "--oneline", "--grep", "Type E #1011")
        assert r.stdout.strip() != ""

    @pytest.mark.rotation
    def test_no_successor_1013_type_b_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type B #1013")
        assert r.stdout.strip() == ""
        assert "## #1013" not in _read(LOG)

    @pytest.mark.rotation
    def test_no_concurrent_type_a_1012_by_commit_time(self):
        r = run_git("log", "--format=%H %s", "--grep", "Type A #1012")
        matches = [line for line in r.stdout.splitlines() if line.strip()]
        own = run_git(
            "log", "--format=%H", "--", "tests/" + THIS_FILE
        ).stdout.split()
        competing = [line for line in matches if line.split()[0] not in own]
        assert competing == []


# ---------------------------------------------------------------------------
# 3. Mechanism 838 block content
# ---------------------------------------------------------------------------
class TestMechanism838Content:
    def test_block_key_unique_at_indent_4_under_anthropic(self):
        hits = [
            line for line in _read(PROFILE).splitlines()
            if line == "    " + BLOCK_KEY + ":"
        ]
        assert len(hits) == 1

    def test_mechanism_id_838_iteration_1012_type_a(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "A"
        assert block["type"] == "competitor_coverage_deep_dive"

    def test_publication_author_goal_job_fields(self):
        block = load_block()
        assert block["publication"] == "MIT Technology Review"
        assert block["publication_pair"] == "MIT TR x Anthropic"
        assert block["author"] == "Kit (with Ray)"
        assert block["goal_id"] == "goal_54093bda4145"
        assert block["scheduled_job_id"] == "mediascope-daily-iteration"
        assert block["date_analyzed"] == "2026-09-26"
        assert block["time_pdt"] == "07:00"

    def test_key_design_note_no_838_underscore_key(self):
        block = load_block()
        assert MECH_ID_MARKER not in BLOCK_KEY
        assert "key_design_note" in block

    def test_connects_to_all_exist_in_profiles(self):
        for m in CONNECTS_TO:
            r = run_git("grep", "-l", "mechanism_id: %d$" % m, "--", "profiles/")
            assert r.stdout.strip() != "", m
        assert load_block()["connects_to"] == CONNECTS_TO

    def test_rotation_transparency_names_window(self):
        rt = load_block()["rotation_transparency"]
        assert "1010-1014" in rt
        assert "#1010" in rt and "#1011" in rt


# ---------------------------------------------------------------------------
# 4. Evidence: one NEW arm, one CARRIED arm, verbatim URLs
# ---------------------------------------------------------------------------
class TestEvidence1012:
    def test_two_arms_with_tone_and_register(self):
        block = load_block()
        for arm_key in ("anthropic_arm", "meta_arm"):
            arm = block[arm_key]
            assert "title" in arm and "url" in arm
            assert "tone_manual_illustrative" in arm
            assert "register" in arm

    def test_new_url_first_appearance(self):
        for url in NEW_URLS:
            assert url in yaml.safe_dump(load_block()), url
            r = run_git("grep", "-l", "-F", url, "--", "profiles/")
            assert [f for f in r.stdout.splitlines() if f] == [
                "profiles/mit-tech-review.yaml"
            ], url

    def test_arm_dates(self):
        block = load_block()
        assert "2026-09-14" in block["anthropic_arm"]["date"]
        assert "2026-09-23" in block["meta_arm"]["date"]

    def test_anthropic_arm_score(self):
        arm = load_block()["anthropic_arm"]
        assert arm["tone_manual_illustrative"] == 0.10
        assert "excerpt-bounded" in arm["attestation"]
        assert "novelty_in_corpus" in arm

    def test_meta_arm_score_carried(self):
        arm = load_block()["meta_arm"]
        assert arm["tone_manual_illustrative"] == -0.60
        assert arm["carried_from"] == 817
        assert "NOT re-fetched" in arm["attestation"]


# ---------------------------------------------------------------------------
# 5. Scores: illustrative delta arithmetic
# ---------------------------------------------------------------------------
class TestScores1012:
    def test_delta_arithmetic(self):
        block = load_block()
        anth = block["anthropic_arm"]["tone_manual_illustrative"]
        meta = block["meta_arm"]["tone_manual_illustrative"]
        assert round(anth - meta, 2) == 0.70
        assert block["illustrative_delta"] == 0.70

    def test_delta_direction_string(self):
        assert load_block()["delta_direction"] == "Anthropic minus Meta"

    def test_finding_layer_manual_illustrative(self):
        assert load_block()["finding_layer"] == "MANUAL ILLUSTRATIVE"

    def test_register_selection_not_uniform_softness(self):
        finding = load_block()["finding"]
        assert "register-selection finding" in finding
        assert "NOT a uniform-softness finding" in finding
        assert "shelved a faulty product" in finding


# ---------------------------------------------------------------------------
# 6. Statistical discipline per the Aug 28 2026 standing rule
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline1012:
    def test_manual_illustrative_only(self):
        sd = load_block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in sd

    def test_p_value_cohens_d_ci_not_calculated(self):
        sd = load_block()["statistical_discipline"]
        assert "p_value NOT_CALCULATED" in sd
        assert "cohens_d NOT_CALCULATED" in sd
        assert "confidence interval NOT_CALCULATED" in sd

    def test_is_significant_false_engine_not_run(self):
        sd = load_block()["statistical_discipline"]
        assert "is_significant False" in sd
        assert "engine NOT run" in sd

    def test_verdict_and_no_analysis_json(self):
        block = load_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["no_analysis_json_update"] is True

    def test_not_falsification_family_ledger_30(self):
        block = load_block()
        assert block["falsification_family_member"] is False
        assert block["falsification_ledger"] == 30


# ---------------------------------------------------------------------------
# 7. Corpus novelty: max id and zero next-number forms (committed tree)
# ---------------------------------------------------------------------------
class TestCorpusNovelty1012:
    def test_max_numeric_mechanism_id_is_838(self):
        r = run_git("grep", "-h", "-o", "-P", r"mechanism_id:\s*\K[0-9]+",
                    "--", "profiles/")
        ids = sorted(
            int(line) for line in r.stdout.splitlines() if line.isdigit()
        )
        assert ids[-1] == MECHANISM

    def test_zero_underscore_839_repo_wide(self):
        r = run_git("grep", "-l", NEXT_ID_MARKER,
                    "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_dash_839_repo_wide(self):
        r = run_git("grep", "-l", NEXT_DASH_MARKER,
                    "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_numeric_839_in_profiles(self):
        r = run_git("grep", "-l", NEXT_NUMERIC, "--", "profiles/")
        assert r.stdout.strip() == ""


# ---------------------------------------------------------------------------
# 8. Doc-sync ratchet per #719 (fail pre-commit, green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSync1012:
    def test_readme_pre_run_values_still_present(self):
        # Pre-run values carried in the new test-file table row's
        # doc-sync prose (51983/1336 -> NEW), so they remain present
        # after README's header stats row is bumped.
        readme = _read(README)
        assert "51983" in readme and "1336" in readme

    def test_readme_table_row_for_1012(self):
        assert ("`tests/" + THIS_FILE + "`") in _read(README)

    def test_architecture_tree_row_for_1012(self):
        assert THIS_FILE.replace(".py", "") in _read(ARCH)


# ---------------------------------------------------------------------------
# 9. Iteration-log entry per #719 (fail pre-commit, green post-entry)
# ---------------------------------------------------------------------------
class TestIterationLog1012:
    def test_newest_entry_is_1012_prepended(self):
        headings = [
            line for line in _read(LOG).splitlines()
            if line.startswith("## #")
        ]
        assert headings[0].startswith("## #1012")

    def test_log_entry_names_third_leg(self):
        text = _read(LOG)
        entry = text.split("## #1012")[1].split("## #1011")[0]
        assert "Type A" in entry
        assert "THIRD leg" in entry


# ---------------------------------------------------------------------------
# 10. Confounders, counter-evidence, financial context
# ---------------------------------------------------------------------------
class TestConfounders1012:
    def test_confounders_ranked_strong_first(self):
        conf = load_block()["confounders"]
        assert list(conf.keys()) == ["strong", "moderate", "weak"]
        assert len(conf["strong"]) >= 3

    def test_excerpt_bounded_is_strong_confounder(self):
        strong = load_block()["confounders"]["strong"]
        assert any("0 browser.open" in c for c in strong)

    def test_counterevidence_four_points(self):
        ce = load_block()["counterevidence"]
        assert len(ce) == 4

    def test_financial_two_sided_nexus(self):
        fc = load_block()["financial_context"]
        assert "two-sided" in fc["nexus_shape"]
        assert "cooperative-conflict" in fc["nexus_shape"]
        assert "prediction_status" in fc


# ---------------------------------------------------------------------------
# 11. Push readiness
# ---------------------------------------------------------------------------
class TestPushReadiness1012:
    def test_ascii_only_no_em_dashes(self):
        # Scopes to the new test file and the m838 block only: the profile
        # carries pre-existing unicode in older sections, untouched by design.
        for text in (open(__file__, encoding="utf-8").read(),
                     yaml.safe_dump(load_block())):
            text.encode("ascii")
            assert "\u2014" not in text  # em dash via unicode escape
            assert "\u2013" not in text  # en dash via unicode escape

    def test_hash_placeholders_filled_post_followup(self):
        # Fails pre-commit per the #721 convention: this run's own main/anchor
        # SHAs are only known after the commits land, then patched into the log.
        # Predecessor (#1011) hashes are excluded; at least the main + anchor
        # SHAs of #1012 must be present.
        text = _read(LOG)
        entry = text.split("## #1012")[1].split("## #1011")[0]
        own_hashes = {
            h for h in re.findall(r"\b[0-9a-f]{40}\b", entry)
            if h not in PREDECESSOR_HASHES
        }
        assert len(own_hashes) >= 2

    def test_staged_set_exactly_five_paths(self):
        # Fails pre-commit by design: staging happens at commit time.
        r = run_git("diff", "--cached", "--name-only")
        staged = {f for f in r.stdout.splitlines() if f}
        assert staged == STAGED_SET

    def test_concurrency_in_flight_unstaged(self):
        # #899 (nytimes.yaml m771 hunk), #938 (anchor patch), #900 (untracked
        # test) stay out of the index.
        r = run_git("status", "--porcelain")
        staged = {line[3:] for line in r.stdout.splitlines()
                  if line[:2] in ("M ", "A ")}
        assert "profiles/nytimes.yaml" not in staged
        assert "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py" not in staged
        assert "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py" not in staged
        # The #899 m771 hunk inside nytimes.yaml must remain UNSTAGED in the
        # worktree (this run stages its own m838 hunk from a different file).
        r2 = run_git("diff", "--", "profiles/nytimes.yaml")
        assert "spur_licensing_market_exists_coalition_founder_datum_unsealed_filings_wave_sep2026" in r2.stdout
