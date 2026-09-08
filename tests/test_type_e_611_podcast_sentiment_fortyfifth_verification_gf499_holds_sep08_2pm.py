"""
Type E #611 - Podcast Sentiment Tracking: Forty-Fifth Verification Cycle Sep 8 14:00 PDT
Guilty Feminist 499 HOLDS (forty-fifth cycle: no new episode; uk-podcasts.co.uk
directory metadata crawled less than 1 hour shows "Latest episode: 2026-09-07";
au.radio.net lists 499 "Where You End and I Begin" released 07/09/2026 as
latest; Listen Notes 2-day crawl still lags on 498; podscan.fm 499 transcript
confirms the TKE Studios Margate art episode; episode 500 watch item still
penciled Mon Sep 14 on weekly-Monday cadence) +
EHE 30-Day Hold (no new primary campaign motif: re-surfaces only, all in
corpus: Times spoof-Epstein 44d, feminist.org FMF via #470 listed updated 7d /
crawled 1h, engadget bus stops 53d crawled 4d, latestly.com Jul 30 fact-check
40d crawled 16d, petapixel Jul 23 lenticular 47d crawled 14d, sifted.eu ban
piece via #480 13d, afrotech ethics piece 53d crawled 8h; no double counting,
no competitor-equivalent guerrilla campaign in forty-five cycles) +
Attention Sphere 45th No-Match AS PODCAST (quoted-search top results are this
repository's own GitHub commits, rejected as circular; identity strand
unchanged from #596; task-spec still misidentified; Tracked Sources table
repaired 44->45 cycles) +
ZERO new-to-corpus press surfaces with ONE new-to-corpus primary-document URL
(pdfserver.amlaw.com/legalradar/pm-63515270_complaint.pdf, the March ND Cal
false-ad complaint filing Case 4:26-cv-02015-HSG underlying the #576
Bloomberg Law strand - new URL, known lineage, NOT a press surface per the
#606 carlfreedman precedent) +
recency frontier TIED at Sep 7 (not advanced) +
MANUAL ILLUSTRATIVE no false significance, no em dashes, verbatim URLs as
surfaced, distinct from 606, forty-fifth verification cycle, extends #606 by
6 hours, not duplicate, iteration-log entry present and newest-first.
"""

import re
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent
DOC_PATH = REPO_ROOT / "podcast-sentiment.md"
LOG_PATH = REPO_ROOT / "iteration-log.md"
README = REPO_ROOT / "README.md"
ARCH = REPO_ROOT / "docs" / "ARCHITECTURE.md"
TESTS_DIR = REPO_ROOT / "tests"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 611
DATE_STR = "2026-09-08 14:00 PDT"
TEST_FILE = Path(__file__).name
CYCLE = 45

VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"

FILE_607 = "test_type_a_607_verge_openai_wiki_incident_adversarial_register_vox_deal_falsification_sep08_9am.py"
FILE_608 = "test_type_b_608_robert_hart_tarbell_fellowship_cross_entity_constancy_sep08_10am.py"
FILE_609 = "test_type_c_609_first_gen_openai_publisher_deal_renewal_window_sep08_11am.py"
FILE_610 = "test_type_d_610_scorer_consistency_607_608_degenerate_609_boundary_rotation_doc_sync_sep08_1pm.py"

AMLAW_PDF = "https://pdfserver.amlaw.com/legalradar/pm-63515270_complaint.pdf"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def read_log():
    return LOG_PATH.read_text(encoding="utf-8")


def read_readme():
    return README.read_text(encoding="utf-8")


def read_arch():
    return ARCH.read_text(encoding="utf-8")


def block_for(doc, iteration):
    m = re.search(
        r"## Iteration #%d\b.*?(?=^## Iteration #|\Z)" % iteration,
        doc,
        re.DOTALL | re.MULTILINE,
    )
    assert m, "Iteration #%d block not found in podcast-sentiment.md" % iteration
    return m.group(0)


class TestIterationNumberAndRotation:
    def test_iteration_number(self):
        assert ITERATION == 611

    def test_cycle_number_is_forty_fifth(self):
        assert CYCLE == 45

    def test_date_string(self):
        assert DATE_STR == "2026-09-08 14:00 PDT"

    def test_goal_and_job_ids(self):
        assert GOAL_ID == "goal_54093bda4145"
        assert JOB_ID == "mediascope-daily-iteration"

    def test_file_name_convention(self):
        assert TEST_FILE.startswith("test_type_e_611_")
        assert TEST_FILE.endswith("_sep08_2pm.py")

    def test_previous_main_type_was_d(self):
        subjects = self._mains()
        # Pre-commit the newest main commit is #610 D; post-commit it is
        # this run's #611 E with #610 D directly beneath. Either way, #610 D
        # must be the rotation predecessor in the top two main commits.
        assert re.search(r"Type D #610:", subjects[0]) or re.search(
            r"Type D #610:", subjects[1]
        ), f"#610 D not found in top two mains: {subjects[:2]!r}"

    def test_rotation_next_after_d_is_e(self):
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        assert (order["E"] - order["D"]) % 5 == 1

    def test_neighbor_test_files_exist(self):
        for f in (FILE_607, FILE_608, FILE_609, FILE_610):
            assert (TESTS_DIR / f).exists(), f"neighbor test file missing: {f}"

    def test_rotation_edge_recorded_in_block(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"610 D -> 611 E", block), (
            "block must record the 610 D -> 611 E rotation edge"
        )

    def _mains(self):
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
        )
        return [
            s
            for s in out.stdout.splitlines()
            if re.match(r"^Type [A-E] #\d+:", s)
        ]


class TestGuiltyFeminist499Holds:
    def test_499_holds_asserted(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"499\s+HOLDS|499 still latest", block), (
            "block must assert GF 499 holds as latest"
        )

    def test_uk_podcasts_latest_2026_09_07(self):
        block = block_for(read_doc(), ITERATION)
        assert "Latest episode: 2026-09-07" in block

    def test_au_radio_net_499_latest(self):
        block = block_for(read_doc(), ITERATION)
        assert "au.radio.net" in block
        assert re.search(r"499.*Where You End and I Begin.*latest", block), (
            "block must note au.radio.net lists 499 as latest"
        )

    def test_listen_notes_lag_noted(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"Listen Notes.*498", block), (
            "block must note Listen Notes still lags on 498"
        )

    def test_500_watch_item_penciled_sep_14(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"episode 500.*Sep 14|Sep 14.*episode 500", block, re.IGNORECASE), (
            "block must pencil the episode 500 watch item for Sep 14"
        )

    def test_no_new_episode_this_run(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"No new episode", block), (
            "block must state no new episode dropped this run"
        )

    def test_forty_fifth_cycle_labeled(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"Forty-Fifth", block), (
            "block must label the forty-fifth verification cycle"
        )


class TestEHEHold:
    def test_thirty_day_hold(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"30-Day Hold|thirty-day hold", block, re.IGNORECASE), (
            "block must note the EHE 30-day hold continues"
        )

    def test_no_new_primary_motif(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"No new primary campaign motif", block)

    def test_resurfaces_all_in_corpus(self):
        block = block_for(read_doc(), ITERATION)
        block_lower = block.lower()
        for needle in ("thetimes.com", "feminist.org", "engadget.com",
                       "latestly.com", "petapixel.com", "sifted.eu",
                       "afrotech.com"):
            assert needle in block_lower, f"EHE re-surface URL missing from block: {needle}"

    def test_seven_resurfaces_distinguished(self):
        block = block_for(read_doc(), ITERATION)
        block_lower = block.lower()
        hits = sum(
            1 for needle in ("thetimes.com", "feminist.org", "engadget.com",
                             "latestly.com", "petapixel.com", "sifted.eu",
                             "afrotech.com")
            if needle in block_lower
        )
        assert hits == 7, f"expected 7 EHE re-surfaces, found {hits}"

    def test_no_double_counting(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"No double counting", block), (
            "block must note no double counting of EHE re-surfaces"
        )

    def test_no_competitor_equivalent_45_cycles(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"No competitor-equivalent.*forty-five cycles", block), (
            "block must note no competitor-equivalent campaign in forty-five cycles"
        )

    def test_activist_group_not_podcast(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"activist.*NOT a podcast", block), (
            "block must reaffirm EHE is an activist group, not a podcast"
        )


class TestAttentionSphereIdentity:
    def test_45th_no_match_as_podcast(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"Forty-Fifth No-Match as a Podcast|45th no-match as podcast",
                         block, re.IGNORECASE), (
            "block must assert the forty-fifth Attention Sphere no-match as podcast"
        )

    def test_circular_github_results_rejected(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"own-corpus GitHub commits.*circular|rejected as circular",
                         block, re.IGNORECASE), (
            "block must note own-corpus GitHub results were rejected as circular"
        )

    def test_identity_strand_unchanged_from_596(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"Identity strand unchanged from #596", block), (
            "block must note the identity strand is unchanged from #596"
        )

    def test_still_misidentified_in_task_spec(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"task-spec.*misidentified|misidentified.*task-spec",
                         block, re.IGNORECASE), (
            "block must note the task-spec name remains misidentified as a podcast"
        )

    def test_tracked_sources_44_to_45_repair(self):
        doc = read_doc()
        table = doc[: doc.index("## Iteration #611")]
        attention_row = next(
            line for line in table.splitlines() if line.startswith("| Attention Sphere |")
        )
        assert "45 verification cycles through Sep 8 2026" in attention_row, (
            "Tracked Sources table must be repaired from 44 to 45 cycles"
        )
        assert "44 verification cycles through Sep 8 2026" not in table, (
            "the stale 44-cycle wording must be gone from the Tracked Sources table"
        )

    def test_guilty_feminist_row_unchanged(self):
        doc = read_doc()
        assert re.search(r"The Guilty Feminist \| \*\*Podcast\*\*.*499 episodes", doc), (
            "GF row must still show 499 episodes"
        )


class TestNewSurfaces:
    def test_zero_new_press_surfaces(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"ZERO new-to-corpus press surfaces", block), (
            "block must assert zero new-to-corpus press surfaces"
        )

    def test_amlaw_pdf_new_url_known_lineage(self):
        block = block_for(read_doc(), ITERATION)
        assert AMLAW_PDF in block, (
            "block must include the new-to-corpus amlaw complaint PDF URL"
        )
        assert re.search(r"new-to-corpus primary-document URL", block), (
            "block must label the PDF as a new-to-corpus primary-document URL"
        )

    def test_amlaw_pdf_not_a_press_surface(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"NOT a press surface|not a press surface", block, re.IGNORECASE), (
            "block must deny the PDF press-surface status"
        )

    def test_amlaw_pdf_case_number(self):
        block = block_for(read_doc(), ITERATION)
        assert "4:26-cv-02015-HSG" in block, (
            "block must cite the complaint case number"
        )

    def test_amlaw_pdf_resolves_to_576_strand(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"#576", block), (
            "block must tie the PDF to the in-corpus #576 Bloomberg Law strand"
        )

    def test_lineage_surfaces_all_in_corpus(self):
        block = block_for(read_doc(), ITERATION)
        for needle in ("startupfortune.com", "letsdatascience.com",
                       "biometricupdate.com", "reuters.com",
                       "bloomberglaw.com", "androidpolice.com"):
            assert needle in block, f"lineage URL missing from block: {needle}"

    def test_recency_frontier_tied_not_advanced(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"Recency frontier.*TIED at Sep 7", block), (
            "block must tie the recency frontier at Sep 7, not advance it"
        )

    def test_no_post_sep_7_surface(self):
        block = block_for(read_doc(), ITERATION)
        assert not re.search(r"postdates? Sep 7|newer than Sep 7", block, re.IGNORECASE), (
            "block must not claim any surface postdates Sep 7"
        )


class TestScoresAndDiscipline:
    def test_manual_illustrative_only(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"MANUAL ILLUSTRATIVE", block), (
            "block must carry the MANUAL ILLUSTRATIVE discipline label"
        )

    def test_no_significance_claimed(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"p_value NOT_CALCULATED", block), (
            "block must show p_value NOT_CALCULATED"
        )
        assert re.search(r"is_significant False", block), (
            "block must show is_significant False"
        )

    def test_no_tone_scores_on_episode(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"No tone scores|no tone scores", block, re.IGNORECASE), (
            "block must state no tone scores were computed this run"
        )

    def test_no_em_dashes_in_block(self):
        block = block_for(read_doc(), ITERATION)
        assert "\u2014" not in block, "block contains an em dash"

    def test_no_em_dashes_in_this_test_file(self):
        text = (TESTS_DIR / TEST_FILE).read_text(encoding="utf-8")
        assert "\u2014" not in text, "test file contains an em dash"


class TestSources:
    def test_amlaw_url_verbatim(self):
        block = block_for(read_doc(), ITERATION)
        assert "https://pdfserver.amlaw.com/legalradar/pm-63515270_complaint.pdf" in block

    def test_gf_directory_urls_present(self):
        block = block_for(read_doc(), ITERATION)
        for needle in ("uk-podcasts.co.uk", "au.radio.net",
                       "listennotes.com", "podscan.fm"):
            assert needle in block, f"GF directory URL missing: {needle}"

    def test_chortle_and_live_org_present(self):
        block = block_for(read_doc(), ITERATION)
        assert "chortle.co.uk" in block
        assert "live.org.uk" in block

    def test_ehe_source_urls_verbatim(self):
        block = block_for(read_doc(), ITERATION)
        assert "https://WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/" in block
        assert "https://www.thetimes.com/uk/london/article/meta-ai-glasses-spoof-advert-jeffrey-epstein-slx3wttm5" in block

    def test_attention_sphere_identity_url_present(self):
        block = block_for(read_doc(), ITERATION)
        assert "raleighnewstoday.com" in block

    def test_no_constructed_urls(self):
        block = block_for(read_doc(), ITERATION)
        for line in block.splitlines():
            for m in re.finditer(r"https?://\S+", line):
                url = m.group(0).rstrip(")")
                assert "search-results://" not in url, (
                    f"constructed search-results URL leaked into block: {url}"
                )


class TestConfoundersAndLog:
    def test_strong_confounders_present(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"- STRONG:", block), "block must rank STRONG confounders"

    def test_listing_lag_confounders_ranked(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"listing.*lag|lag.*listing", block, re.IGNORECASE), (
            "block must document listing-lag confounders"
        )

    def test_hours_cadence_bounded(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"extends #606", block), (
            "block must note it extends #606"
        )

    def test_novelty_verification_claimed(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"\*\*Novelty verification:\*\*", block), (
            "block must carry a novelty verification section"
        )
        assert re.search(r"forty-fifth verification cycle is new", block, re.IGNORECASE), (
            "block must assert the forty-fifth cycle is new"
        )

    def test_log_entry_present_newest_first(self):
        log = read_log()
        pos_611 = log.find("#611 Type E")
        assert pos_611 != -1, "iteration-log.md missing the #611 entry"
        pos_610 = log.find("#610 Type D")
        assert pos_610 != -1, "iteration-log.md missing the #610 entry"
        assert pos_611 < pos_610, "#611 entry must be newest-first above #610"

    def test_log_entry_covers_rotation_edge(self):
        log = read_log()
        pos = log.find("#611 Type E")
        section = log[pos:pos + 4000]
        assert re.search(r"610 D -> 611 E", section), (
            "log entry must cover the 610 D -> 611 E rotation edge"
        )


class TestNoBrittleSweep611:
    def test_current_cycle_label_not_stale(self):
        block = block_for(read_doc(), ITERATION)
        assert "forty-fourth verification cycle" not in block.lower(), (
            "block must not claim the forty-fourth label for this run"
        )
        assert "44th verification cycle is new" not in block.lower(), (
            "block must not claim the 44th cycle as this run"
        )

    def test_distinct_from_606(self):
        block = block_for(read_doc(), ITERATION)
        assert "extends #606" in block or "distinct from #606" in block

    def test_no_zero_coverage_claims(self):
        block = block_for(read_doc(), ITERATION)
        assert not re.search(r"\bzero coverage\b", block, re.IGNORECASE)

    def test_no_em_dash_in_rotation_guard_anchor_line(self):
        text = (TESTS_DIR / TEST_FILE).read_text(encoding="utf-8")
        assert "\u2014" not in text


class TestRotationCycleGuard611:
    """Rotation guard, deselected pre-commit per the #565 followup convention.

    Asserts the post-commit anchor, so it runs green only in the followup
    commit after the main commit SHA is known. Pre-commit it is deselected.
    """

    ANCHORED_COMMIT = "PATCH_IN_FOLLOWUP"

    def _mains(self):
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]
        assert len(mains) >= 5
        return mains

    def test_window_607_611_closes_d_to_e(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("E", "611"),
            ("D", "610"),
            ("C", "609"),
            ("B", "608"),
            ("A", "607"),
        ], f"rotation window 607-611 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["E", "D", "C", "B", "A"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )


class TestDocSyncRatchet611:
    def test_readme_row_for_611(self):
        readme = read_readme()
        assert re.search(r"#611", readme), "README.md missing the #611 test-table row"

    def test_arch_row_for_611(self):
        arch = read_arch()
        assert re.search(r"#611", arch), "docs/ARCHITECTURE.md missing the #611 tree row"

    def test_606_row_survives_in_readme(self):
        readme = read_readme()
        assert re.search(r"#606", readme), "README.md lost the #606 row"

    def test_606_row_survives_in_arch(self):
        arch = read_arch()
        assert re.search(r"#606", arch), "docs/ARCHITECTURE.md lost the #606 row"

    def test_iteration_log_611_entry_present(self):
        log = read_log()
        assert "#611 Type E" in log

    def test_count_stats_gate_green(self):
        out = subprocess.run(
            [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "count_stats.py"), "--check"],
            capture_output=True, text=True, timeout=600, cwd=str(REPO_ROOT))
        assert out.returncode == 0, f"count_stats --check failed:\n{out.stdout}\n{out.stderr}"
