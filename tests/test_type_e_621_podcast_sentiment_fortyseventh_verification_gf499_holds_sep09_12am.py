"""
Type E #621 - Podcast Sentiment Tracking: Forty-Seventh Verification Cycle Sep 9 00:00 PDT
Guilty Feminist 499 HOLDS (forty-seventh cycle: no new episode; uk-podcasts.co.uk
directory metadata crawled 6 hours shows "Latest episode: 2026-09-07";
au.radio.net lists 499 "Where You End and I Begin" released 07/09/2026 as
latest; Listen Notes 2-day crawl still lags on 498; podscan.fm 499 TKE Studios
Margate transcript confirms the art episode is the newest numbered release;
Chortle live-show page re-surfaced; episode 500 watch item still penciled Mon
Sep 14 on weekly-Monday cadence; no new tech-word audit since no new episode) +
EHE 30-Day Hold (no new primary campaign motif: six re-surfaces observed this
run, all in corpus: latestly.com Jul 30 fact-check 41d crawled 17d, engadget
bus stops 54d crawled 4d, fstoppers.com lenticular crawled 2d, feminist.org FMF
via #470 listed updated 8d crawled 3h, petapixel Jul 23 lenticular 48d crawled
15d, thedrum.com Mark Palmer opinion 26d crawled less than 1h; three prior-cycle
lineage items carried in corpus: thetimes.com spoof-Epstein 45d, sifted.eu ban
piece via #480, afrotech ethics piece; no double counting, no
competitor-equivalent guerrilla campaign in forty-seven cycles) +
Attention Sphere 47th No-Match AS PODCAST (quoted-search top results are this
repository's own GitHub commits, rejected as circular; creators.spotify.com and
podcasters.spotify.com Purposeful Empathy pages name "The Attention Sphere" as
Ava Smithing's non-profit organization, identity-strand confirmation, NOT a
podcast; tomorrowunveiled.com PDF absent this run, in-corpus search noise per
#587/#591/#596 precedent; identity strand unchanged from #596; task-spec still
misidentified; Tracked Sources table repaired 46->47 cycles) +
TWO new-to-corpus press surfaces postdating the Sep 7 frontier (Reuters Sep 8
Meta Muse/Hatch AI-agent piece with the glasses-hook "soon"; USA Today Sep 8
best-tech roundup with a Meta Glasses blurb, usatoday.com a NEW domain to the
corpus) + recency frontier ADVANCES Sep 7 to Sep 8 (distinct from #611's single
new primary-document URL and #616's zero-new cycle) + two new-to-corpus URLs
predating the frontier (techtime.news Lumus Sep 2, eagle1063.iheart.com
camera-tampering Sep 2) NOT press-surface advances + in-corpus re-surfaces
(thetimes.com Fear-and-loathing field test via #581, letsdatascience
expanded-lawsuit via #586, amlaw PDF via #611) +
MANUAL ILLUSTRATIVE no false significance, no em dashes, verbatim URLs as
surfaced, extends #616 by 5 hours, forty-seventh verification cycle is new,
617-621 rotation-cycle guard closing the D->E edge (anchor patched post-commit
per #565 convention), count_stats gate - Sep 9 2026 00:00 PDT.
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
ITERATION = 621
DATE_STR = "2026-09-09 00:00 PDT"
TEST_FILE = Path(__file__).name
CYCLE = 47

VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"

FILE_617 = "test_type_a_617_verge_samsung_launch_cycle_register_sep08_8pm.py"
FILE_618 = "test_type_b_618_victoria_song_jul2026_escalation_audit_sep08.py"
FILE_619 = "test_type_c_619_apple_siri_ai_negotiation_silence_status_check_sep08_10pm.py"
FILE_620 = "test_type_d_620_scorer_consistency_617_618_619_monitoring_boundary_rotation_doc_sync_sep08_11pm.py"

AMLAW_PDF = "https://pdfserver.amlaw.com/legalradar/pm-63515270_complaint.pdf"
REUTERS_MUSE = "https://www.reuters.com/business/meta-launches-ai-agent-that-can-access-other-apps-send-emails-make-payments-2026-09-08/"
USA_TODAY = "https://www.usatoday.com/story/shopping/tech/2026/09/08/best-tech-products-2026/91584576007/"
TECHTIME_LUMUS = "https://techtime.news/2026/09/02/lumus-2/"
EAGLE_TAMPER = "https://eagle1063.iheart.com/content/2026-09-02-meta-disables-cameras-on-thousands-of-ai-glasses-after-tampering/"


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
        assert ITERATION == 621

    def test_cycle_number_is_forty_seventh(self):
        assert CYCLE == 47

    def test_date_string(self):
        assert DATE_STR == "2026-09-09 00:00 PDT"

    def test_goal_and_job_ids(self):
        assert GOAL_ID == "goal_54093bda4145"
        assert JOB_ID == "mediascope-daily-iteration"

    def test_file_name_convention(self):
        assert TEST_FILE.startswith("test_type_e_621_")
        assert TEST_FILE.endswith("_sep09_12am.py")

    def test_previous_main_type_was_d(self):
        subjects = self._mains()
        # Pre-commit the newest main commit is #620 D; post-commit it is
        # this run's #621 E with #620 D directly beneath. Either way, #620 D
        # must be the rotation predecessor in the top two main commits.
        assert re.search(r"Type D #620:", subjects[0]) or re.search(
            r"Type D #620:", subjects[1]
        ), f"#620 D not found in top two mains: {subjects[:2]!r}"

    def test_rotation_next_after_d_is_e(self):
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        assert (order["E"] - order["D"]) % 5 == 1

    def test_neighbor_test_files_exist(self):
        for f in (FILE_617, FILE_618, FILE_619, FILE_620):
            assert (TESTS_DIR / f).exists(), f"neighbor test file missing: {f}"

    def test_rotation_edge_recorded_in_block(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"620 D -> 621 E", block), (
            "block must record the 620 D -> 621 E rotation edge"
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

    def test_forty_seventh_cycle_labeled(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"Forty-Seventh", block), (
            "block must label the forty-seventh verification cycle"
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
        for needle in ("latestly.com", "engadget.com", "fstoppers.com",
                       "feminist.org", "petapixel.com", "thedrum.com"):
            assert needle in block_lower, f"EHE re-surface URL missing from block: {needle}"

    def test_six_observed_distinguished(self):
        block = block_for(read_doc(), ITERATION)
        block_lower = block.lower()
        hits = sum(
            1 for needle in ("latestly.com", "engadget.com", "fstoppers.com",
                             "feminist.org", "petapixel.com", "thedrum.com")
            if needle in block_lower
        )
        assert hits == 6, f"expected 6 observed EHE re-surfaces, found {hits}"

    def test_three_prior_lineage_carried_in_corpus(self):
        block = block_for(read_doc(), ITERATION)
        for needle in ("thetimes.com spoof-Epstein", "sifted.eu", "afrotech"):
            assert needle in block, f"carried lineage missing from block: {needle}"

    def test_no_double_counting(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"No double counting", block), (
            "block must note no double counting of EHE re-surfaces"
        )

    def test_no_competitor_equivalent_47_cycles(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"No competitor-equivalent.*forty-seven cycles", block), (
            "block must note no competitor-equivalent campaign in forty-seven cycles"
        )

    def test_activist_group_not_podcast(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"activist.*NOT a podcast", block), (
            "block must reaffirm EHE is an activist group, not a podcast"
        )


class TestAttentionSphereIdentity:
    def test_47th_no_match_as_podcast(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"Forty-Seventh No-Match as a Podcast|47th no-match as podcast",
                         block, re.IGNORECASE), (
            "block must assert the forty-seventh Attention Sphere no-match as podcast"
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

    def test_tracked_sources_46_to_47_repair(self):
        doc = read_doc()
        table = doc[: doc.index("## Iteration #611")]
        attention_row = next(
            line for line in table.splitlines() if line.startswith("| Attention Sphere |")
        )
        assert "47 verification cycles through Sep 9 2026" in attention_row, (
            "Tracked Sources table must be repaired from 46 to 47 cycles"
        )
        assert "46 verification cycles through Sep 8 2026" not in table, (
            "the stale 46-cycle wording must be gone from the Tracked Sources table"
        )

    def test_guilty_feminist_row_unchanged(self):
        doc = read_doc()
        assert re.search(r"The Guilty Feminist \| \*\*Podcast\*\*.*499 episodes", doc), (
            "GF row must still show 499 episodes"
        )


class TestNewSurfaces:
    def test_two_new_press_surfaces(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"TWO new-to-corpus press surfaces", block), (
            "block must assert two new-to-corpus press surfaces"
        )
        assert REUTERS_MUSE in block
        assert USA_TODAY in block

    def test_reuters_muse_verbatim(self):
        block = block_for(read_doc(), ITERATION)
        assert REUTERS_MUSE in block
        assert re.search(r"Meta Muse|Muse/Hatch", block), (
            "block must name the Reuters piece as the Meta Muse/Hatch agent story"
        )

    def test_usa_today_new_domain_to_corpus(self):
        block = block_for(read_doc(), ITERATION)
        assert USA_TODAY in block
        assert re.search(r"usatoday\.com.*NEW domain to the corpus", block), (
            "block must note usatoday.com is a new domain to the corpus"
        )

    def test_recency_frontier_advances_sep_7_to_sep_8(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"Recency frontier.*ADVANCES Sep 7 to Sep 8", block), (
            "block must advance the recency frontier from Sep 7 to Sep 8"
        )

    def test_frontier_not_tied(self):
        block = block_for(read_doc(), ITERATION)
        assert "frontier TIED" not in block, (
            "block must not tie the recency frontier this run"
        )

    def test_techtime_predates_frontier(self):
        block = block_for(read_doc(), ITERATION)
        assert TECHTIME_LUMUS in block
        assert re.search(r"NOT a press-surface advance", block, re.IGNORECASE), (
            "block must deny press-surface-advance status to the pre-frontier URLs"
        )

    def test_eagle1063_predates_frontier(self):
        block = block_for(read_doc(), ITERATION)
        assert EAGLE_TAMPER in block

    def test_in_corpus_resurfaces(self):
        block = block_for(read_doc(), ITERATION)
        for needle in ("in corpus via #581", "in corpus via #586", "in corpus via #611"):
            assert needle in block, f"in-corpus lineage missing from block: {needle}"
        assert AMLAW_PDF in block
        assert re.search(r"NOT a press surface", block, re.IGNORECASE), (
            "block must deny the amlaw PDF press-surface status"
        )

    def test_distinct_from_611_and_616(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"distinct from #611", block)
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
    def test_reuters_url_verbatim(self):
        block = block_for(read_doc(), ITERATION)
        assert "https://www.reuters.com/business/meta-launches-ai-agent-that-can-access-other-apps-send-emails-make-payments-2026-09-08/" in block

    def test_usa_today_url_verbatim(self):
        block = block_for(read_doc(), ITERATION)
        assert "https://www.usatoday.com/story/shopping/tech/2026/09/08/best-tech-products-2026/91584576007/" in block

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
        assert "https://fstoppers.com/news/kylie-jenner-ad-hides-disturbing-secret-just-have-stand-right-spot-903612" in block
        assert "https://www.thedrum.com/opinion/mark-palmer-is-the-glasses-partnership-with-meta-making-ray-ban-lose-its-cool" in block

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
        assert re.search(r"extends #616", block), (
            "block must note it extends #616"
        )

    def test_novelty_verification_claimed(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"\*\*Novelty verification:\*\*", block), (
            "block must carry a novelty verification section"
        )
        assert re.search(r"forty-seventh verification cycle is new", block, re.IGNORECASE), (
            "block must assert the forty-seventh cycle is new"
        )

    def test_log_entry_present_newest_first(self):
        log = read_log()
        pos_621 = log.find("#621 Type E")
        assert pos_621 != -1, "iteration-log.md missing the #621 entry"
        pos_620 = log.find("#620 Type D")
        assert pos_620 != -1, "iteration-log.md missing the #620 entry"
        assert pos_621 < pos_620, "#621 entry must be newest-first above #620"

    def test_log_entry_covers_rotation_edge(self):
        log = read_log()
        pos = log.find("#621 Type E")
        section = log[pos:pos + 4000]
        assert re.search(r"620 D -> 621 E", section), (
            "log entry must cover the 620 D -> 621 E rotation edge"
        )


class TestNoBrittleSweep621:
    def test_current_cycle_label_not_stale(self):
        block = block_for(read_doc(), ITERATION)
        assert "forty-sixth" not in block.lower(), (
            "block must not claim the forty-sixth label for this run"
        )
        assert "46th verification cycle is new" not in block.lower(), (
            "block must not claim the 46th cycle as this run"
        )

    def test_distinct_from_616(self):
        block = block_for(read_doc(), ITERATION)
        assert "extends #616" in block or "distinct from #616" in block

    def test_no_zero_coverage_claims(self):
        block = block_for(read_doc(), ITERATION)
        assert not re.search(r"\bzero coverage\b", block, re.IGNORECASE)

    def test_no_seven_resurface_drift(self):
        block = block_for(read_doc(), ITERATION)
        assert not re.search(r"7 re-surfaces", block), (
            "block must not carry the stale 7-re-surface count from #616"
        )


class TestRotationCycleGuard621:
    """Rotation guard, deselected pre-commit per the #565 followup convention.

    Asserts the post-commit anchor, so it runs green only in the followup
    commit after the main commit SHA is known. Pre-commit it is deselected.
    """

    ANCHORED_COMMIT = "34e3227"  # main commit of Type E #621, patched in followup per #565 convention
    EXPECTED_WINDOW_NEWEST_FIRST = [
        ("E", 621),
        ("D", 620),
        ("C", 619),
        ("B", 618),
        ("A", 617),
    ]

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "log", "-n40",
             TestRotationCycleGuard621.ANCHORED_COMMIT, "--format=%s"],
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


class TestDocSyncRatchet621:
    def test_readme_row_for_621(self):
        readme = read_readme()
        assert re.search(r"#621", readme), "README.md missing the #621 test-table row"

    def test_arch_row_for_621(self):
        arch = read_arch()
        assert re.search(r"#621", arch), "docs/ARCHITECTURE.md missing the #621 tree row"

    def test_620_row_survives_in_readme(self):
        readme = read_readme()
        assert re.search(r"#620", readme), "README.md lost the #620 row"

    def test_620_row_survives_in_arch(self):
        arch = read_arch()
        assert re.search(r"#620", arch), "docs/ARCHITECTURE.md lost the #620 row"

    def test_iteration_log_621_entry_present(self):
        log = read_log()
        assert "#621 Type E" in log

    def test_count_stats_gate_green(self):
        out = subprocess.run(
            [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "count_stats.py"), "--check"],
            capture_output=True, text=True, timeout=600, cwd=str(REPO_ROOT))
        assert out.returncode == 0, f"count_stats --check failed:\n{out.stdout}\n{out.stderr}"
