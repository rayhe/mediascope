"""
Type E #626 - Podcast Sentiment Tracking: Forty-Eighth Verification Cycle Sep 9 05:00 PDT
Guilty Feminist 499 HOLDS (forty-eighth cycle: no new episode; uk-podcasts.co.uk
directory metadata crawled 3 hours shows "Latest episode: 2026-09-07";
au.radio.net lists 499 "Where You End and I Begin" released 07/09/2026 as
latest; Listen Notes 2-day crawl still lags on 498; podscan.fm 499 TKE Studios
Margate transcript confirms the art episode is the newest numbered release;
Chortle live-show page re-surfaced; episode 500 watch item still penciled Mon
Sep 14 on weekly-Monday cadence; no new tech-word audit since no new episode) +
EHE 30-Day Hold (no new primary campaign motif: six re-surfaces observed this
run, all in corpus: thetimes.com spoof-Epstein 44d crawled 44d, feminist.org FMF
via #470 listed updated 8d crawled 4h, petapixel.com lenticular 48d crawled 15d,
sifted.eu ban piece via #480 14d crawled 13d, engadget.com bus stops 54d crawled
5d, afrotech.com ethics piece 54d crawled 23h; hyperallergic.com lenticular
origin story in corpus but not re-surfaced in this run's top results; no double
counting, no competitor-equivalent guerrilla campaign in forty-eight cycles) +
Attention Sphere 48th No-Match AS PODCAST (quoted-search top results are this
repository's own GitHub commits, rejected as circular; creators.spotify.com and
podcasters.spotify.com Purposeful Empathy pages name "The Attention Sphere" as
Ava Smithing's non-profit organization, identity-strand confirmation, NOT a
podcast; tomorrowunveiled.com PDF absent this run, in-corpus search noise per
#587/#591/#596 precedent; identity strand unchanged from #596; task-spec still
misidentified; Tracked Sources table repaired 47->48 cycles) +
ZERO new-to-corpus press surfaces (distinct from #621's two new press surfaces
plus frontier advance and from #616's zero-new cycle): thevermilion.com Meta
Ray-Ban Display Italy piece ~Sep 2025 is a new-to-corpus URL but predates the
Sep 8 frontier, NOT a press-surface advance; in-corpus re-surfaces are the
Reuters Sep 8 Muse piece via #621, techtime.news Lumus via #621, stuff.tv Oakley
piece, thetimes.com Fear-and-loathing via #581, roadtovr.com Connect piece, and
letsdatascience expanded-lawsuit via #586; recency frontier TIED at Sep 8, not
advanced +
MANUAL ILLUSTRATIVE no false significance, no em dashes, verbatim URLs as
surfaced, extends #621 by 5 hours, forty-eighth verification cycle is new,
622-626 rotation-cycle guard closing the D->E edge (anchor patched post-commit
per #565 convention), count_stats gate - Sep 9 2026 05:00 PDT.
"""

import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DOC_PATH = REPO_ROOT / "podcast-sentiment.md"
LOG_PATH = REPO_ROOT / "iteration-log.md"
README = REPO_ROOT / "README.md"
ARCH = REPO_ROOT / "docs" / "ARCHITECTURE.md"
TESTS_DIR = REPO_ROOT / "tests"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 626
DATE_STR = "2026-09-09 05:00 PDT"
TEST_FILE = Path(__file__).name
CYCLE = 48

VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"

FILE_622 = "test_type_a_622_guardian_apple_vision_pro_vs_meta_pervert_glasses_sep09_1am.py"
FILE_623 = "test_type_b_623_kashmir_hill_surveillance_register_constancy_sep09_2am.py"
FILE_624 = "test_type_c_624_openai_india_attribution_deal_blitz_sep09_3am.py"
FILE_625 = "test_type_d_625_scorer_consistency_621_622_623_624_rotation_doc_sync_sep09_4am.py"

THEVERMILION_DISPLAY = "https://www.thevermilion.com/meta-ray-ban-display-the-glasses-that-replace-the-smartphone-and-not-only-in-italy-since-2026/article_15267/"
REUTERS_MUSE = "https://www.reuters.com/business/meta-launches-ai-agent-that-can-access-other-apps-send-emails-make-payments-2026-09-08/"


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
        assert ITERATION == 626

    def test_cycle_number_is_forty_eighth(self):
        assert CYCLE == 48

    def test_date_string(self):
        assert DATE_STR == "2026-09-09 05:00 PDT"

    def test_goal_and_job_ids(self):
        assert GOAL_ID == "goal_54093bda4145"
        assert JOB_ID == "mediascope-daily-iteration"

    def test_file_name_convention(self):
        assert TEST_FILE.startswith("test_type_e_626_")
        assert TEST_FILE.endswith("_sep09_5am.py")

    def test_previous_main_type_was_d(self):
        subjects = self._mains()
        # Pre-commit the newest main commit is #625 D; post-commit it is
        # this run's #626 E with #625 D directly beneath. Either way, #625 D
        # must be the rotation predecessor in the top two main commits.
        assert re.search(r"Type D #625:", subjects[0]) or re.search(
            r"Type D #625:", subjects[1]
        ), f"#625 D not found in top two mains: {subjects[:2]!r}"

    def test_rotation_next_after_d_is_e(self):
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        assert (order["E"] - order["D"]) % 5 == 1

    def test_neighbor_test_files_exist(self):
        for f in (FILE_622, FILE_623, FILE_624, FILE_625):
            assert (TESTS_DIR / f).exists(), f"neighbor test file missing: {f}"

    def test_rotation_edge_recorded_in_block(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"625 D -> 626 E", block), (
            "block must record the 625 D -> 626 E rotation edge"
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

    def test_forty_eighth_cycle_labeled(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"Forty-Eighth", block), (
            "block must label the forty-eighth verification cycle"
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

    def test_six_observed_resurfaces_all_in_corpus(self):
        block = block_for(read_doc(), ITERATION)
        block_lower = block.lower()
        for needle in ("thetimes.com", "feminist.org", "petapixel.com",
                       "sifted.eu", "engadget.com", "afrotech.com"):
            assert needle in block_lower, f"EHE re-surface URL missing from block: {needle}"

    def test_six_observed_distinguished(self):
        block = block_for(read_doc(), ITERATION)
        block_lower = block.lower()
        hits = sum(
            1 for needle in ("thetimes.com", "feminist.org", "petapixel.com",
                             "sifted.eu", "engadget.com", "afrotech.com")
            if needle in block_lower
        )
        assert hits == 6, f"expected 6 observed EHE re-surfaces, found {hits}"

    def test_hyperallergic_in_corpus_not_resurfaced(self):
        block = block_for(read_doc(), ITERATION)
        assert "hyperallergic.com" in block
        assert re.search(r"hyperallergic.*in corpus", block, re.IGNORECASE), (
            "block must note the hyperallergic.com lenticular origin story is in corpus"
        )

    def test_no_double_counting(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"No double counting", block), (
            "block must note no double counting of EHE re-surfaces"
        )

    def test_no_competitor_equivalent_48_cycles(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"No competitor-equivalent.*forty-eight cycles", block), (
            "block must note no competitor-equivalent campaign in forty-eight cycles"
        )

    def test_activist_group_not_podcast(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"activist.*NOT a podcast", block), (
            "block must reaffirm EHE is an activist group, not a podcast"
        )


class TestAttentionSphereIdentity:
    def test_48th_no_match_as_podcast(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"Forty-Eighth No-Match as a Podcast|48th no-match as podcast",
                         block, re.IGNORECASE), (
            "block must assert the forty-eighth Attention Sphere no-match as podcast"
        )

    def test_circular_github_results_rejected(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"own-corpus GitHub commits.*circular|rejected as circular",
                         block, re.IGNORECASE), (
            "block must note own-corpus GitHub results were rejected as circular"
        )

    def test_spotify_nonprofit_identity_confirmation(self):
        block = block_for(read_doc(), ITERATION)
        assert "creators.spotify.com" in block
        assert "podcasters.spotify.com" in block
        assert re.search(r"non-profit organization", block), (
            "block must note Spotify pages name The Attention Sphere as Ava Smithing's non-profit organization"
        )

    def test_tomorrowunveiled_absent_this_run(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"tomorrowunveiled.*did not surface this run", block), (
            "block must note the tomorrowunveiled PDF did not surface this run"
        )
        assert re.search(r"in-corpus search noise per #587/#591/#596", block), (
            "block must carry the tomorrowunveiled in-corpus-noise precedent"
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

    def test_tracked_sources_47_to_48_repair(self):
        doc = read_doc()
        table = doc[: doc.index("## Iteration #621")]
        attention_row = next(
            line for line in table.splitlines() if line.startswith("| Attention Sphere |")
        )
        assert "48 verification cycles through Sep 9 2026" in attention_row, (
            "Tracked Sources table must be repaired from 47 to 48 cycles"
        )
        assert "47 verification cycles through Sep 9 2026" not in table, (
            "the stale 47-cycle wording must be gone from the Tracked Sources table"
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
            "block must assert zero new-to-corpus press surfaces this run"
        )

    def test_recency_frontier_tied_at_sep_8(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"Recency frontier.*TIED at Sep 8", block), (
            "block must tie the recency frontier at Sep 8"
        )

    def test_frontier_not_advanced(self):
        block = block_for(read_doc(), ITERATION)
        assert "frontier ADVANCES" not in block, (
            "block must not advance the recency frontier this run"
        )

    def test_thevermilion_predates_frontier(self):
        block = block_for(read_doc(), ITERATION)
        assert THEVERMILION_DISPLAY in block

    def test_thevermilion_not_press_surface_advance(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"NOT a press-surface advance", block, re.IGNORECASE), (
            "block must deny press-surface-advance status to the pre-frontier URL"
        )

    def test_in_corpus_resurfaces(self):
        block = block_for(read_doc(), ITERATION)
        for needle in ("in corpus via #621", "in corpus via #581",
                       "in corpus via #586", "stuff.tv", "roadtovr"):
            assert needle in block, f"in-corpus lineage missing from block: {needle}"
        assert REUTERS_MUSE in block
        assert "techtime.news" in block

    def test_distinct_from_621_and_616(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"distinct from #621", block)
        assert re.search(r"distinct from #616", block)


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
        assert "https://petapixel.com/2026/07/23/kylie-jenners-meta-smart-glasses-parodied-in-guerrilla-lenticular-ad/" in block
        assert "https://www.thetimes.com/uk/london/article/meta-ai-glasses-spoof-advert-jeffrey-epstein-slx3wttm5" in block

    def test_thevermilion_url_verbatim(self):
        block = block_for(read_doc(), ITERATION)
        assert THEVERMILION_DISPLAY in block

    def test_reuters_in_corpus_via_621(self):
        block = block_for(read_doc(), ITERATION)
        assert REUTERS_MUSE in block
        assert re.search(r"in corpus via #621", block), (
            "block must note the Reuters Sep 8 piece is in corpus via #621"
        )

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
        assert re.search(r"extends #621", block), (
            "block must note it extends #621"
        )

    def test_novelty_verification_claimed(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"\*\*Novelty verification:\*\*", block), (
            "block must carry a novelty verification section"
        )
        assert re.search(r"forty-eighth verification cycle is new", block, re.IGNORECASE), (
            "block must assert the forty-eighth cycle is new"
        )

    def test_log_entry_present_newest_first(self):
        log = read_log()
        pos_626 = log.find("#626 Type E")
        assert pos_626 != -1, "iteration-log.md missing the #626 entry"
        pos_625 = log.find("#625 Type D")
        assert pos_625 != -1, "iteration-log.md missing the #625 entry"
        assert pos_626 < pos_625, "#626 entry must be newest-first above #625"

    def test_log_entry_covers_rotation_edge(self):
        log = read_log()
        pos = log.find("#626 Type E")
        section = log[pos:pos + 4000]
        assert re.search(r"625 D -> 626 E", section), (
            "log entry must cover the 625 D -> 626 E rotation edge"
        )


class TestNoBrittleSweep626:
    def test_current_cycle_label_not_stale(self):
        block = block_for(read_doc(), ITERATION)
        assert "forty-seventh" not in block.lower(), (
            "block must not claim the forty-seventh label for this run"
        )
        assert "47th cycle is new" not in block.lower(), (
            "block must not claim the 47th cycle as this run"
        )

    def test_distinct_from_621(self):
        block = block_for(read_doc(), ITERATION)
        assert "extends #621" in block or "distinct from #621" in block

    def test_no_zero_coverage_claims(self):
        block = block_for(read_doc(), ITERATION)
        assert not re.search(r"\bzero coverage\b", block, re.IGNORECASE)

    def test_no_stale_six_from_621(self):
        block = block_for(read_doc(), ITERATION)
        block_lower = block.lower()
        for needle in ("latestly.com", "fstoppers.com", "thedrum.com"):
            assert needle not in block_lower, (
                f"block must not carry the stale #621 re-surface set item: {needle}"
            )


class TestRotationCycleGuard626:
    """Rotation guard, deselected pre-commit per the #565 followup convention.

    Asserts the post-commit anchor, so it runs green only in the followup
    commit after the main commit SHA is known. Pre-commit it is deselected.
    """

    ANCHORED_COMMIT = "POST_COMMIT_ANCHOR"  # main commit of Type E #626, patched in followup per #565 convention
    EXPECTED_WINDOW_NEWEST_FIRST = [
        ("E", 626),
        ("D", 625),
        ("C", 624),
        ("B", 623),
        ("A", 622),
    ]

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "log", "-n40",
             TestRotationCycleGuard626.ANCHORED_COMMIT, "--format=%s"],
            capture_output=True, text=True, check=True)
        return [s for s in out.stdout.splitlines()
                if re.match(r"^Type [A-E] #\d+:", s)][:5]

    def test_git_commit_order_matches_rotation(self):
        subjects = self._mains()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        for i, (typ, num) in enumerate(self.EXPECTED_WINDOW_NEWEST_FIRST):
            assert f"#{num}" in subjects[i], \
                f"position {i}: expected #{num}, got {subjects[i]!r}"
            assert re.search(rf"Type {typ} #{num}:", subjects[i]), \
                f"position {i}: expected Type {typ} #{num}, got {subjects[i]!r}"

    def test_rotation_adjacency_cycle_valid(self):
        # D->E is the edge this run closes; newest-first order is E,D,C,B,A.
        # (order[a] - order[b]) % 5 == 1 steps one rotation step forward.
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append(m.group(1))
        assert observed == ["E", "D", "C", "B", "A"]
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, \
                f"rotation broken: {a} -> {b} is not a valid cycle edge"

    def test_anchor_is_post_commit(self):
        assert self.ANCHORED_COMMIT != "POST_COMMIT_ANCHOR", \
            "anchor must be patched to the main-commit hash in the followup"

    def test_closes_d_to_e_edge(self):
        types = [t for t, _ in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert types[0] == "E" and types[1] == "D"

    def test_five_window_members(self):
        assert len(self.EXPECTED_WINDOW_NEWEST_FIRST) == 5


class TestDocSyncRatchet626:
    def test_readme_row_for_626(self):
        readme = read_readme()
        assert re.search(r"#626", readme), "README.md missing the #626 test-table row"

    def test_arch_row_for_626(self):
        arch = read_arch()
        assert re.search(r"#626", arch), "docs/ARCHITECTURE.md missing the #626 tree row"

    def test_625_row_survives_in_readme(self):
        readme = read_readme()
        assert re.search(r"#625", readme), "README.md lost the #625 row"

    def test_625_row_survives_in_arch(self):
        arch = read_arch()
        assert re.search(r"#625", arch), "docs/ARCHITECTURE.md lost the #625 row"

    def test_iteration_log_626_entry_present(self):
        log = read_log()
        assert "#626 Type E" in log

    def test_count_stats_gate_green(self):
        out = subprocess.run(
            [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "count_stats.py"), "--check"],
            capture_output=True, text=True, timeout=600, cwd=str(REPO_ROOT))
        assert out.returncode == 0, f"count_stats --check failed:\n{out.stdout}\n{out.stderr}"
