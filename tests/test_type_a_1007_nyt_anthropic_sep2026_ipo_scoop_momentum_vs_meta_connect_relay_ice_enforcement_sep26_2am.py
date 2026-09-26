"""Type A #1007 (2026-09-26 02:00 PDT): NYT x Anthropic Sep-2026 IPO-scoop momentum
register vs NYT x Meta Connect-relay + Aug ICE-ban enforcement register. Third leg
of the 1005-1009 window (D #1005 -> E #1006 -> A #1007).

NEW finding (coverage register selection, mechanism 835): in the Sep 12-23 2026
window the New York Times ran two Anthropic arms in the constructive band - a Sep 12
news piece on Dario Amodei's slowdown essay (15minutenews attestation of the NYT
original, reception consensus-framed; MANUAL ILLUSTRATIVE +0.10) and a Sep 18 IPO
scoop (IPOScoop attestation quoting the NYT original verbatim: November debut, $100B+
annualized revenue, $2T valuation; MANUAL ILLUSTRATIVE +0.25) - against two Meta arms
split across registers: the Sep 23 Connect straight relay ("Meta Unveils 3 Smart
Glasses With Built-In A.I.", killbait attestation, not-clickbait/factual; MANUAL
ILLUSTRATIVE +0.10) and the Aug 18 memo-sourced ICE-ban investigative piece (original
NYT URL recovered verbatim via the glassesbegone repo sourceUrl field; enforcement
register; MANUAL ILLUSTRATIVE -0.30). Anthropic mean +0.175, Meta mean -0.10,
illustrative delta (Anthropic minus Meta) +0.275. The register SELECTION is the
asymmetry; incentive read is incentive-CONSISTENT with the reported (single-source
unverified) NYT-Anthropic settlement tie but attribution is INCONCLUSIVE. Temporal
extension of the m685 slowdown family into the IPO peg; FIRST corpus
mechanism-ization of the NYT's own Aug-18 ICE-ban investigative piece.

Statistical discipline per the Aug 28 2026 standing rule: MANUAL ILLUSTRATIVE scores
only, p_value/cohens_d/ci NOT_CALCULATED, is_significant False, engine NOT run at
the finding layer; verdict directionally_supported_not_proven; no analysis.json
update; NOT artifact-grade; NOT falsification-family member; ledger holds at 30.
Excerpt-bounded per #503 (0 browser.open). Correlation is not causation.
Hypothesis-generating only. ASCII-only, no em dashes.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4 (patched
green in the anchor followup). Doc-sync 3 fail pre-commit per #719, all green
post-doc-sync; iteration-log 2 fail pre-commit; hash-placeholder test fails
pre-commit per the #721 convention; staged-set test fails pre-commit by design.
41 tests, 10 classes. ASCII only, no em dashes.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, "profiles", "nytimes.yaml")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
LOG = os.path.join(REPO, "iteration-log.md")
THIS_FILE = os.path.basename(__file__)

ANCHORED_SHA = "a0d351d30e8d3ad359c79fd4c0187cb67bfc11b7"  # patched in the anchor followup per #565

ITERATION = 1007
MECHANISM = 835
BLOCK_KEY = (
    "type_a_1007_nyt_anthropic_sep2026_ipo_scoop_momentum_register_vs_meta_"
    "connect_relay_ice_enforcement_sep26_2026"
)

NEW_URLS = [
    "https://www.15minutenews.com/article/2026/09/12/282850031/anthropic-ceo-dario-amodei-calls-for-ai-slowdown/",
    "https://www.iposcoop.com/the-ipo-buzz-anthropic-ipo-may-come-in-november-the-nyt-reports/",
    "https://en.killbait.com/meta-announces-three-new-ai-powered-smart-glasses-at-connect-2026-conference.html",
    "https://www.nytimes.com/2026/08/18/technology/ice-meta-smart-glasses.html",
]

CONNECTS_TO = [685, 822, 832, 790]

EXPECTED_TESTS = 41
README_TESTS_BEFORE, README_TESTS_AFTER = 51748, 51789
README_FILES_BEFORE, README_FILES_AFTER = 1331, 1332

MECH_ID_MARKER = "mechanism" + "_835"
NEXT_ID_MARKER = "mechanism" + "_836"
NEXT_DASH_MARKER = "mechanism" + "-836"

STAGED_SET = {
    "profiles/nytimes.yaml",
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
    return data["competitor_relationships"]["anthropic"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty per the Aug 31 standing rule
# ---------------------------------------------------------------------------
class TestNovelty1007:
    def test_single_type_a_1007_test_file(self):
        files = sorted(
            f for f in os.listdir(os.path.join(REPO, "tests"))
            if f.startswith("test_type_a_1007") and f.endswith(".py")
        )
        assert files == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type A #1007" in r2.stdout

    def test_no_type_a_1007_in_git_log_precommit(self):
        r = run_git("log", "--format=%H %s", "--grep", "Type A #1007")
        own = run_git("log", "--format=%H", "--", "tests/" + THIS_FILE).stdout
        hits = [
            line for line in r.stdout.splitlines()
            if line.split()[0] not in own.split()
        ]
        assert hits == []


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1005-1009 window, third leg
# ---------------------------------------------------------------------------
class TestRotationGuard1005_1009Window:
    def test_window_legs_in_iteration_log(self):
        text = _read(LOG)
        assert "## #1005 Type D" in text
        assert "## #1006 Type E" in text
        assert "1005-1009" in text

    @pytest.mark.rotation
    def test_third_leg_of_1005_to_1009_window(self):
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "A"
        assert "1005-1009 window third leg" in block["rotation_transparency"]

    @pytest.mark.rotation
    def test_predecessor_1006_type_e_committed(self):
        r = run_git("log", "--oneline", "--grep", "Type E #1006")
        assert r.stdout.strip() != ""

    @pytest.mark.rotation
    def test_no_successor_1008_type_b_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type B #1008")
        assert r.stdout.strip() == ""
        assert "## #1008" not in _read(LOG)

    @pytest.mark.rotation
    def test_no_concurrent_type_a_1007_by_commit_time(self):
        r = run_git("log", "--format=%H %s", "--grep", "Type A #1007")
        matches = [line for line in r.stdout.splitlines() if line.strip()]
        own = run_git(
            "log", "--format=%H", "--", "tests/" + THIS_FILE
        ).stdout.split()
        competing = [line for line in matches if line.split()[0] not in own]
        assert competing == []


# ---------------------------------------------------------------------------
# 3. Mechanism 835 block content
# ---------------------------------------------------------------------------
class TestMechanism835Content:
    def test_block_key_unique_at_indent_4_under_anthropic(self):
        hits = [
            line for line in _read(PROFILE).splitlines()
            if line == "    " + BLOCK_KEY + ":"
        ]
        assert len(hits) == 1

    def test_mechanism_id_835_iteration_1007_type_a(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "A"
        assert block["type"] == "competitor_coverage_deep_dive"

    def test_publication_author_goal_job_fields(self):
        block = load_block()
        assert block["publication"] == "The New York Times"
        assert block["author"] == "Kit (with Ray)"
        assert block["goal_id"] == "goal_54093bda4145"
        assert block["job_id"] == "mediascope-daily-iteration"
        assert block["date_analyzed"] == "2026-09-26"
        assert block["time_pdt"] == "02:00"

    def test_key_design_note_no_835_underscore_key(self):
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
        assert "1005-1009" in rt
        assert "#1005" in rt and "#1006" in rt


# ---------------------------------------------------------------------------
# 4. Evidence: four arms, verbatim URLs
# ---------------------------------------------------------------------------
class TestEvidence1007:
    def test_four_arms_each_with_tone(self):
        arms = load_block()["articles_this_run"]
        assert len(arms) == 4
        for arm in arms:
            assert "title" in arm and "url" in arm
            assert "tone_manual_illustrative" in arm

    def test_new_urls_first_appearance(self):
        for url in NEW_URLS:
            assert url in yaml.safe_dump(load_block()), url
            r = run_git("grep", "-l", "-F", url, "--", "profiles/")
            assert [f for f in r.stdout.splitlines() if f] == [
                "profiles/nytimes.yaml"
            ], url

    def test_arm_dates(self):
        arms = load_block()["articles_this_run"]
        dates = [arm["date"] for arm in arms]
        assert any("2026-09-12" in d for d in dates)
        assert any("2026-09-18" in d for d in dates)
        assert any("2026-09-23" in d for d in dates)
        assert any("2026-08-18" in d for d in dates)

    def test_anthropic_arm_scores(self):
        arms = load_block()["articles_this_run"]
        ipo = [a for a in arms if "IPO" in a["title"]][0]
        slow = [a for a in arms if "Slowdown" in a["title"]][0]
        assert ipo["tone_manual_illustrative"] == 0.25
        assert slow["tone_manual_illustrative"] == 0.10

    def test_meta_arm_scores(self):
        arms = load_block()["articles_this_run"]
        relay = [a for a in arms if "3 Smart Glasses" in a["title"]][0]
        ice = [a for a in arms if "ICE" in a["title"]][0]
        assert relay["tone_manual_illustrative"] == 0.10
        assert ice["tone_manual_illustrative"] == -0.30


# ---------------------------------------------------------------------------
# 5. Scores: means and illustrative delta
# ---------------------------------------------------------------------------
class TestScores1007:
    def test_means_and_delta(self):
        means = load_block()["illustrative_means"]
        assert abs(means["anthropic_mean"] - 0.175) < 1e-9
        assert abs(means["meta_mean"] - (-0.10)) < 1e-9
        assert abs(means["delta"] - 0.275) < 1e-9
        assert "(+0.175) - (-0.10) = +0.275" in means["delta_calc"]

    def test_delta_is_anthropic_minus_meta(self):
        means = load_block()["illustrative_means"]
        assert "Anthropic minus Meta" in means["delta_calc"]

    def test_no_scorer_run(self):
        sd = load_block()["statistical_discipline"]
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "MANUAL_ILLUSTRATIVE"

    def test_iposcoop_arm_novelty_note(self):
        arms = load_block()["articles_this_run"]
        ipo = [a for a in arms if "IPO" in a["title"]][0]
        assert "zero hits repo-wide pre-commit" in ipo["url_status"]
        assert "iposcoop.com" in ipo["url"]

    def test_winbuzzer_rejection_documented(self):
        block = load_block()
        text = yaml.safe_dump(block)
        assert "rejected as already in-corpus via m784" in text


# ---------------------------------------------------------------------------
# 6. Statistical discipline per the Aug 28 2026 standing rule
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline1007:
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
        assert block["correlational_note"]


# ---------------------------------------------------------------------------
# 7. Corpus novelty sweeps (post-insert guards)
# ---------------------------------------------------------------------------
class TestCorpusNovelty1007:
    def test_max_numeric_mechanism_id_is_835(self):
        r = run_git("grep", "-h", "-o", "-P", r"mechanism_id:\s*\K[0-9]+",
                    "--", "profiles/")
        ids = sorted(
            int(m.group(1))
            for line in r.stdout.splitlines()
            for m in [re.match(r"([0-9]+)$", line)]
            if m
        )
        assert ids[-1] == MECHANISM

    def test_zero_underscore_836_repo_wide(self):
        r = run_git("grep", "-l", NEXT_ID_MARKER,
                    "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_dash_836_repo_wide(self):
        r = run_git("grep", "-l", NEXT_DASH_MARKER,
                    "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""


# ---------------------------------------------------------------------------
# 8. Doc-sync ratchet per #719 (fail pre-commit, green post-doc-sync)
# ---------------------------------------------------------------------------
class TestDocSync1007:
    def test_readme_pre_run_values_still_present(self):
        # Pre-run values carried in the new test-file table row's
        # doc-sync prose (51748/1331 -> NEW), so they remain present
        # after ARCHITECTURE's tree row is bumped.
        readme = _read(README)
        assert "51748" in readme and "1331" in readme

    def test_readme_table_row_for_1007(self):
        assert ("`tests/" + THIS_FILE + "`") in _read(README)

    def test_architecture_tree_row_for_1007(self):
        assert THIS_FILE.replace(".py", "") in _read(ARCH)


# ---------------------------------------------------------------------------
# 9. Iteration-log entry per #719 (fail pre-commit, green post-entry)
# ---------------------------------------------------------------------------
class TestIterationLog1007:
    def test_newest_entry_is_1007_prepended(self):
        headings = [
            line for line in _read(LOG).splitlines()
            if line.startswith("## #")
        ]
        assert headings[0].startswith("## #1007")

    def test_log_entry_names_third_leg(self):
        text = _read(LOG)
        entry = text.split("## #1007")[1].split("## #1006")[0]
        assert "Type A" in entry
        assert "THIRD leg" in entry


# ---------------------------------------------------------------------------
# 10. Push readiness
# ---------------------------------------------------------------------------
class TestPushReadiness1007:
    def test_ascii_only_no_em_dashes(self):
        # Scopes to the new test file and the m835 block only: the profile
        # carries pre-existing unicode in older sections, untouched by design.
        for text in (open(__file__, encoding="utf-8").read(),
                     yaml.safe_dump(load_block())):
            text.encode("ascii")
            assert "\u2014" not in text  # em dash via unicode escape
            assert "\u2013" not in text  # en dash via unicode escape

    def test_hash_placeholders_filled_post_followup(self):
        # Fails pre-commit per the #721 convention: this run's own main/anchor
        # SHAs are only known after the commits land, then patched into the log.
        # Predecessor (#1006) hashes are cited in Rotation transparency and do
        # not count; at least the main + anchor SHAs of #1007 must be present.
        text = _read(LOG)
        entry = text.split("## #1007")[1].split("## #1006")[0]
        own_hashes = {
            h for h in re.findall(r"\b[0-9a-f]{40}\b", entry)
            if h not in ("9e82a6279f43b2244591f0a211261f18d48c0696",
                         "1cae3521ed7881a2f0a642ca259d3eca2e524f0b")
        }
        assert len(own_hashes) >= 2

    def test_staged_set_exactly_five_paths(self):
        # Fails pre-commit by design: staging happens at commit time.
        r = run_git("diff", "--cached", "--name-only")
        staged = {f for f in r.stdout.splitlines() if f}
        assert staged == STAGED_SET

    def test_concurrency_in_flight_unstaged(self):
        # #884 (competitor-entities.yaml m762), #899 (nytimes.yaml m771 hunk),
        # #938 (anchor patch), #900 (untracked test) stay out of the index.
        r = run_git("status", "--porcelain")
        staged = {line[3:] for line in r.stdout.splitlines()
                  if line[:2] in ("M ", "A ")}
        assert "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py" not in staged
        assert "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py" not in staged
        assert "profiles/competitor-entities.yaml" not in staged
        # The #899 m771 hunk inside nytimes.yaml must remain UNSTAGED even
        # though this run stages its own m835 hunk from the same file.
        r2 = run_git("diff", "--", "profiles/nytimes.yaml")
        assert "spur_licensing_market_exists_coalition_founder_datum_unsealed_filings_wave_sep2026" in r2.stdout
