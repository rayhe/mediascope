"""Type C #1004: Australia News Bargaining Incentive (enacted Aug 20 2026) - State-Compelled Deal-or-Levy Regulatory Bargaining - TWELFTH relationship direction.

FIFTH and CLOSING leg of the 1000-1004 window (D->E->A->B->C per #565).

Mechanism 834 in profiles/competitor-entities.yaml (top-level block):
the FIRST dedicated corpus mechanism on the ENACTED Australian News Media
Bargaining Bill 2026 + News Journalism Payments Bill 2026 (Senate passage
Aug 20 2026). The corpus's earlier NBI record described the April 2026
draft-stage 2.25% terms; this block adds the final-law record and explicitly
supersedes the draft-stage description without overwriting history.

Direction: REGULATORY-BARGAINING - state-compelled deal-making where the
state legislates the payer's menu (the twelfth relationship direction per the
m807 enumeration: 1 sue-then-sign m624; 2 pay-or-litigate bifurcation m636;
3 grant-then-sue m675; 4 license-over-authors m699; 5 pool-and-license m720;
6 infrastructure-capture m738; 7 publisher-as-feed-operator m741;
8 vendor-embed m807; 9 litigation-pooling m810; 10 publisher-traffic-gate
m828; 11 commerce-conversion licensing m831; 12 regulatory-bargaining m834).

Statistical contract: tone NOT_SCORED (qualitative financial-incentive
mapping), no tone statistics, engine NOT run, is_significant False,
no causal claim, verdict directionally_supported_not_proven, no
analysis.json update, NOT artifact-grade, NOT falsification-family member,
ledger holds at 30.

Evidence: 8 source URLs (Reuters x2, Meta about.fb.com, ibtimes.sg, NPR
mirror wcbe.org, mi-3, CBAA, wdsm710 draft recap), 0 browser.open
(excerpt-bounded per #503). Rate is BOUNDED but UNRESOLVED between
secondary sources: Reuters reports 2.5%, mi-3 reports 2.75%. The block
claims the deal-or-levy STRUCTURE, not the exact rate.

Run contract: main commit keeps ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP";
anchor followup patches it; log-hash followup fills iteration-log hashes;
push-status finalizer closes the run. Pre-commit, run:
    .venv/bin/python -m pytest tests/<this file> -m "not anchor and not rotation" -q
The anchor test, rotation-guard class, staged-set test, and hash-placeholder
test fail pre-commit by design (anchor patched post-commit; rotation guard
checks committed predecessors; staging happens right before the commit;
hashes filled by the log-hash followup).
"""
from pathlib import Path
import re
import subprocess

import pytest
import yaml

ITERATION = 1004
ITERATION_TYPE = "C"
MECHANISM = 834
BLOCK_KEY = (
    "type_c_1004_australia_news_bargaining_incentive_regulatory_bargaining_sep25_11pm"
)
THIS_FILE = (
    "test_type_c_1004_australia_nbi_regulatory_bargaining_passed_sep25_11pm.py"
)
REPO = Path(__file__).resolve().parent.parent
PROFILE = REPO / "profiles" / "competitor-entities.yaml"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"
LOG = REPO / "iteration-log.md"

ANCHORED_SHA = "c8f9fc97"

NEW_URLS = [
    "https://www.reuters.com/legal/litigation/australia-passes-law-levy-tech-giants-that-fail-pay-local-news-2026-08-20/",
    "https://www.reuters.com/business/australia-make-tech-companies-pay-more-outlets-content-under-reworked-media-law-2026-08-12/",
    "https://about.fb.com/news/2026/06/metas-response-to-australias-proposed-news-bargaining-incentive/",
    "https://www.ibtimes.sg/australia-targets-big-tech-new-levy-news-payments-google-meta-tiktok-could-pay-millions-92549",
    "https://www.wcbe.org/2026-08-21/big-tech-companies-will-have-to-pay-to-publish-australian-news-content-under-new-laws",
    "http://www.mi-3.com.au/21-08-2026/news-media-bargaining-incentive-clears-parliament-275-charge-be-levvied-big-tech",
    "https://www.cbaa.org.au/news/cbaa-comms/2026/08/21/news-bargaining-incentive-marks-a-new-chapter-for-",
    "https://wdsm710.com/2026/04/27/australia-to-charge-big-tech-companies-2-levy-unless-they-strike-local-news-deals/",
]
CONNECTS_TO = [594, 331, 549, 735, 355, 807]

README_TESTS_BEFORE = 51590
README_FILES_BEFORE = 1328
README_TESTS_AFTER = 51642
README_FILES_AFTER = 1329

STAGED_SET = {
    "profiles/competitor-entities.yaml",
    f"tests/{THIS_FILE}",
    "iteration-log.md",
    "README.md",
    "docs/ARCHITECTURE.md",
}
CONCURRENCY_UNTOUCHED = {
    "profiles/nytimes.yaml",
    "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
    "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py",
}

MECH_ID_MARKER = "mechanism" + "_834"
MECH_DASH_MARKER = "mechanism" + "-834"
NEXT_ID_MARKER = "mechanism" + "_835"
MECH_NUM = f"mechanism_id: {MECHANISM}$"


def run_git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO, capture_output=True, text=True, check=False
    )


def load_block():
    with open(PROFILE) as fh:
        doc = yaml.safe_load(fh)
    return doc[BLOCK_KEY]


class TestNovelty1004:
    def test_single_test_type_c_1004_file(self):
        files = sorted((REPO / "tests").glob("test_type_c_1004*.py"))
        assert [f.name for f in files] == [THIS_FILE]

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP"
        r = run_git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit"
        r2 = run_git("log", "--format=%s", "-1", ANCHORED_SHA)
        assert "Type C #1004" in r2.stdout

    def test_novelty_claim_present_in_block(self):
        block = load_block()
        assert "FIRST dedicated corpus mechanism" in block["novelty"]
        assert "zero underscore-form 834 mechanism key strings" in block["novelty"]
        assert "TWELFTH relationship direction" in block["novelty"]

    def test_no_literal_underscore_or_dash_834_keys(self):
        r = run_git("grep", "-l", MECH_ID_MARKER, "--", "profiles/", "tests/", "docs/", "iteration-log.md")
        assert r.stdout.strip() == ""
        r2 = run_git("grep", "-l", MECH_DASH_MARKER, "--", "profiles/", "tests/", "docs/", "iteration-log.md")
        assert r2.stdout.strip() == ""


class TestRotationCycleGuard1004:
    @pytest.mark.rotation
    def test_fifth_leg_of_1000_to_1004_window(self):
        text = LOG.read_text()
        assert "## #1000" in text and "Type D" in text
        assert "## #1001" in text and "Type E" in text
        assert "## #1002" in text and "Type A" in text
        assert "## #1003" in text and "Type B" in text
        block = load_block()
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "C"

    @pytest.mark.rotation
    def test_predecessor_1003_type_b_committed(self):
        r = run_git("log", "--oneline", "--grep=#1003")
        assert r.stdout.strip() != ""
        assert (
            REPO
            / "tests"
            / "test_type_b_1003_james_pero_gizmodo_snap_earbending_comedy_vs_meta_audio_stigma_sep25_10pm.py"
        ).exists()

    @pytest.mark.rotation
    def test_no_successor_1004_type_c_commit_yet(self):
        r = run_git("log", "--oneline", "--grep", "Type C #1004")
        assert r.stdout.strip() == ""
        assert "## #1004" not in LOG.read_text()

    @pytest.mark.rotation
    def test_no_concurrent_in_flight_type_c_1004_by_commit_time(self):
        r = run_git("log", "--format=%H %s", "--grep=Type C #1004")
        matches = [l for l in r.stdout.splitlines() if l.strip()]
        own = run_git("log", "--format=%H", "--", f"tests/{THIS_FILE}").stdout.splitlines()
        competing = [l for l in matches if l.split()[0] not in own]
        assert competing == [], f"concurrent Type C #1004 commits: {competing}"


class TestMechanism834Content:
    def test_block_key_unique_at_zero_indent(self):
        hits = [
            line
            for line in PROFILE.read_text().splitlines()
            if line == f"{BLOCK_KEY}:"
        ]
        assert len(hits) == 1

    def test_mechanism_id_834_iteration_1004_type_c(self):
        block = load_block()
        assert block["mechanism_id"] == MECHANISM
        assert block["iteration"] == ITERATION
        assert block["iteration_type"] == "C"
        assert block["type"] == "financial_incentive_mapping"
        assert block["type_label"] == "Financial Incentive Mapping"

    def test_new_urls_first_appearance(self):
        for url in NEW_URLS:
            assert url in yaml.safe_dump(load_block()), url
            r = run_git("grep", "-l", "-F", url, "--", "profiles/")
            assert [f for f in r.stdout.splitlines() if f] == [
                "profiles/competitor-entities.yaml"
            ], url

    def test_connects_to_all_exist(self):
        for m in CONNECTS_TO:
            r = run_git("grep", "-l", f"mechanism_id: {m}$", "--", "profiles/")
            assert r.stdout.strip() != "", m
        assert load_block()["connects_to"] == CONNECTS_TO

    def test_passage_facts_structure(self):
        facts = load_block()["passage_facts"]
        assert facts["passed"] == "2026-08-20"
        assert "8 publisher groups" in facts["offset_path"]
        assert "150%" in facts["offset_path"] and "200%" in facts["offset_path"]
        assert "25%" in facts["offset_path"]
        assert "A$250M" in facts["threshold"]
        assert "5%" in facts["levy_path"]
        assert "Australian Associated Press" in facts["levy_path"]

    def test_rate_uncertainty_bounded_not_settled(self):
        rate = load_block()["rate_uncertainty"]
        assert "2.5%" in rate["reuters_reports"]
        assert "2.75%" in rate["mi3_reports"]
        assert "not the exact" in rate["claim_boundary"]
        finding = load_block()["finding"]
        assert "2.5%-reported/2.75%-reported" in finding

    def test_draft_record_superseded_not_overwritten(self):
        sup = load_block()["draft_record_supersession"]
        assert "2.25%" in sup["note"]
        assert "supersedes" in sup["note"]
        assert "not overwritten" in sup["note"] or "retained as history" in sup["note"]
        assert "consciously separated" in sup["note"]

    def test_verdict_directionally_supported_not_proven(self):
        block = load_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["no_analysis_json_update"] is True

    def test_finding_mentions_regulatory_bargaining_and_batna(self):
        finding = load_block()["finding"]
        assert "regulatory-bargaining" in finding
        assert "TWELFTH" in finding
        assert "BATNA" in finding
        assert "Correlation only" in finding


class TestRegulatoryBargainingDirection:
    def test_twelfth_direction_named(self):
        tax = load_block()["relationship_direction_taxonomy"]
        assert tax.startswith("TWELFTH relationship direction")

    def test_enumeration_lists_all_twelve(self):
        tax = load_block()["relationship_direction_taxonomy"]
        for token in ["m624", "m636", "m675", "m699", "m720", "m738", "m741",
                      "m807", "m810", "m828", "m831"]:
            assert token in tax, token
        assert "TWELFTH" in tax
        assert "REGULATORY-BARGAINING" in tax

    def test_taxonomy_tension_carried(self):
        tax = load_block()["relationship_direction_taxonomy"]
        assert "m737" in tax
        assert "termination-leverage" in tax
        assert "Not resolved this run" in tax

    def test_ai_exclusion_asymmetry(self):
        facts = load_block()["passage_facts"]
        assert "consciously separated" in facts["ai_exclusion"]
        tax = load_block()["relationship_direction_taxonomy"]
        assert "LLM-only AI services are exempt" in tax

    def test_loophole_closure_encoded(self):
        lc = load_block()["loophole_closure"]
        assert "2024" in lc["meta_2024_walkaway"]
        assert "closed that loophole" in lc["closure"]

    def test_meta_position_quoted(self):
        meta = load_block()["meta_position"]
        assert "tax on innovation dressed up as media policy" in meta["quotes"]["tax_on_innovation"]
        assert "discriminatory" in meta["quotes"]["discriminatory"]
        assert "vehemently opposed" in meta["quotes"]["opposed"]
        assert "free-trade agreement" in meta["fta_objection"]

    def test_strongest_counterargument_present(self):
        block = load_block()
        assert len(block["strongest_counterargument"]) > 100
        assert "compelled bilateral market" in block["strongest_counterargument"]


class TestSourceCorroboration1004:
    def test_eight_sources_present(self):
        assert len(load_block()["sources"]) == len(NEW_URLS)
        assert load_block()["sources"] == NEW_URLS

    def test_reuters_passage_url_present(self):
        assert NEW_URLS[0] in yaml.safe_dump(load_block())

    def test_reuters_intro_url_present(self):
        assert NEW_URLS[1] in yaml.safe_dump(load_block())

    def test_meta_about_fb_url_present(self):
        assert NEW_URLS[2] in yaml.safe_dump(load_block())


class TestStatisticalDiscipline1004:
    def test_tone_scores_not_scored(self):
        assert load_block()["tone_scores"] == "NOT_SCORED"

    def test_no_tone_statistics_calculated(self):
        block = load_block()
        assert block["engine_run"] is False
        assert "p_value" not in block
        assert "cohens_d" not in block

    def test_excerpt_bounded_no_browser_open(self):
        assert load_block()["excerpt_bounded"] is True
        assert load_block()["verification"]["browser_opens"] == 0

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

    def test_counterevidence_four_plus(self):
        block = load_block()
        assert len(block["counterevidence"]) >= 4
        assert "AI labs to pay" in block["counterevidence"][0]


class TestSupersessionAndCorpusPost1003:
    def test_corpus_max_mechanism_id_is_834(self):
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
        assert ids[-1] == 834

    def test_iteration_1003_max_833_sweep_superseded_by_design(self):
        r = run_git("grep", "-l", "mechanism_id: 833$", "--", "profiles/")
        assert r.stdout.strip() != ""
        r2 = run_git("grep", "-l", "mechanism_id: 834$", "--", "profiles/")
        assert r2.stdout.strip() != ""

    def test_zero_underscore_835_repo_wide(self):
        r = run_git("grep", "-l", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert r.stdout.strip() == ""

    def test_zero_numeric_835_in_profiles(self):
        r = run_git("grep", "-l", "mechanism_id: 835$", "--", "profiles/")
        assert r.stdout.strip() == ""

    def test_iteration_1003_zero_underscore_834_sweep_stays_green(self):
        r = run_git("grep", "-l", MECH_ID_MARKER, "--", "profiles/", "tests/")
        assert r.stdout.strip() == ""

    def test_iteration_1003_zero_numeric_834_sweep_fails_by_designed_supersession(self):
        r = run_git("grep", "-l", "mechanism_id: 834$", "--", "profiles/")
        assert r.stdout.strip() != ""

    def test_numeric_834_keys_in_exactly_the_designed_location(self):
        r = run_git("grep", "-l", "mechanism_id: 834$", "--", "profiles/")
        files = [f for f in r.stdout.splitlines() if f]
        assert files == ["profiles/competitor-entities.yaml"]
        r2 = run_git("grep", "-c", "mechanism_id: 834$", "--", "profiles/competitor-entities.yaml")
        assert r2.stdout.strip().endswith(":1")


class TestLedger1004:
    def test_not_falsification_family_member(self):
        assert load_block()["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        assert load_block()["falsification_ledger"] == 30

    def test_ledger_note_present(self):
        note = load_block()["falsification_note"]
        assert "holds at 30" in note


class TestDocSync1004:
    def test_readme_stats_updated(self):
        text = README.read_text()
        assert str(README_TESTS_AFTER) in text
        assert str(README_FILES_AFTER) in text
        assert f"| Tests | {README_TESTS_AFTER} | Across {README_FILES_AFTER} test files |" in text

    def test_readme_table_row_for_1004(self):
        text = README.read_text()
        assert f"`tests/{THIS_FILE}`" in text
        assert text.index(f"`tests/{THIS_FILE}`") > text.index(
            "`tests/test_type_b_1003_james_pero_gizmodo_snap_earbending_comedy_vs_meta_audio_stigma_sep25_10pm.py`"
        )

    def test_architecture_tree_row_for_1004(self):
        assert THIS_FILE in ARCH.read_text()


class TestIterationLog1004:
    def _entry(self):
        text = LOG.read_text()
        return text.split("## #1004")[1].split("## #1003")[0]

    def test_newest_entry_is_1004_prepended(self):
        headings = [
            line
            for line in LOG.read_text().splitlines()
            if line.startswith("## #")
        ]
        assert headings[0].startswith("## #1004")

    def test_entry_mentions_new_mechanism_and_window_close(self):
        entry = self._entry().lower()
        assert "mechanism 834" in entry
        assert "1000-1004" in entry
        assert "d->e->a->b->c" in entry

    def test_entry_mentions_nbi_passage(self):
        entry = self._entry().lower()
        assert "bargaining incentive" in entry or "nbi" in entry
        assert "august 20" in entry or "aug 20" in entry

    def test_hash_placeholders_filled_post_followup(self):
        entry = self._entry()
        assert re.search(r"\b[0-9a-f]{40}\b", entry) is not None


class TestPushReadiness1004:
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
