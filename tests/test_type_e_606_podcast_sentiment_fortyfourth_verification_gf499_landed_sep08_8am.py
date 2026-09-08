"""
Type E #606 - Podcast Sentiment Tracking: Forty-Fourth Verification Cycle Sep 8 08:00 PDT
Guilty Feminist 499 LANDS (forty-fourth cycle: RSS feed opened directly, PRIMARY
tier - 499 "Where You End and I Begin" with Lindsey Mendick, presented DFW,
recorded 15 Aug 2026 at TKE Studios in Margate, pubDate Mon 07 Sep 2026
11:00:00 -0000; subject is the Carl Freedman Gallery Margate exhibition on
romantic attachment / body horror / ceramics; tech-word audit finds zero
Meta/glasses/AI/wearables/privacy/surveillance vocabulary in title/description,
bounded to surfaced text; the #601 499-prediction HELD at its stated 0.85
MANUAL ILLUSTRATIVE probability; uk-podcasts.co.uk directory metadata flagged
the drop pre-confirmation, Listen Notes 2-day crawl still lagging on 498;
episode 500 watch item penciled Mon Sep 14) +
EHE 30-Day Hold (no new primary campaign motif: re-surfaces only, all in
corpus: Times spoof-Epstein 43d, feminist.org FMF piece listed updated 7d /
crawled 7h, engadget bus stops 53d crawled 4d, latestly Jul 30 fact-check 40d
crawled 16d, petapixel Jul 23 lenticular 47d crawled 14d, sifted.eu ban piece
logged #480 13d, afrotech ethics piece 53d crawled 2h; no competitor-equivalent
guerrilla campaign in forty-four cycles) +
Attention Sphere 44th No-Match AS PODCAST (quoted search top results are this
repository's own GitHub commits, rejected as circular; identity strand
unchanged from #596; Tracked Sources table miss repairs: 41->44 cycles, GF row
~495->499 episodes) +
ZERO new-to-corpus press surfaces (startupfortune #561 ND Cal amended,
letsdatascience #586 expanded lawsuit, biometricupdate Alvarez #601,
reuters HateAid, bloomberglaw #576 false-ad, androidpolice contractor strand -
all in corpus lineage) +
recency frontier TIED at Sep 7 (not advanced) +
MANUAL ILLUSTRATIVE no false significance, no em dashes, verbatim URLs as
surfaced, distinct from 601, forty-fourth verification cycle, extends #601 by
5 hours, not duplicate, iteration-log entry present and newest-first, #605
entry repositioned to newest-first order as miss repair.
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
ITERATION = 606
DATE_STR = "2026-09-08 08:00 PDT"
TEST_FILE = Path(__file__).name
CYCLE = 44

VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"

FILE_602 = "test_type_a_602_wired_anthropic_licensing_halo_september_silence_extension_sep08_4am.py"
FILE_603 = "test_type_b_603_joanna_stern_independent_phase_cross_entity_gradient_sep08_5am.py"
FILE_604 = "test_type_c_604_axel_springer_dual_ai_payer_microsoft_kkr_split_telegraph_sep08_6am.py"
FILE_605 = "test_type_d_605_scorer_consistency_603_degenerate_604_602_spotcheck_rotation_doc_sync_sep08_7am.py"

RSS_FEED = "feeds.megaphone.fm/APL9072247766"


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
        assert ITERATION == 606

    def test_cycle_number_is_forty_fourth(self):
        assert CYCLE == 44

    def test_date_string(self):
        assert DATE_STR == "2026-09-08 08:00 PDT"

    def test_goal_and_job_ids(self):
        assert GOAL_ID == "goal_54093bda4145"
        assert JOB_ID == "mediascope-daily-iteration"

    def test_file_name_convention(self):
        assert TEST_FILE.startswith("test_type_e_606_")
        assert TEST_FILE.endswith("_sep08_8am.py")

    def test_previous_main_type_was_d(self):
        subjects = self._mains()
        # Pre-commit the newest main commit is #605 D; post-commit it is
        # this run's #606 E with #605 D directly beneath. Either way, #605 D
        # must be the rotation predecessor in the top two main commits.
        assert re.search(r"Type D #605:", subjects[0]) or re.search(
            r"Type D #605:", subjects[1]
        ), f"#605 D not found in top two mains: {subjects[:2]!r}"

    def test_rotation_next_after_d_is_e(self):
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        assert (order["E"] - order["D"]) % 5 == 1

    def test_neighbor_test_files_exist(self):
        for f in (FILE_602, FILE_603, FILE_604, FILE_605):
            assert (TESTS_DIR / f).exists(), f"neighbor test file missing: {f}"

    def test_rotation_edge_recorded_in_block(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"605 D -> 606 E", block), (
            "block must record the 605 D -> 606 E rotation edge"
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


class TestGuiltyFeminist499Landed:
    def test_499_landed_asserted(self):
        block = block_for(read_doc(), ITERATION)
        assert "499 LANDS" in block

    def test_499_title_and_guest(self):
        block = block_for(read_doc(), ITERATION)
        assert "Where You End and I Begin" in block
        assert "Lindsey Mendick" in block

    def test_release_date_from_rss(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"Mon, 07 Sep 2026 11:00:00", block), (
            "block must cite the RSS pubDate Mon, 07 Sep 2026 11:00:00"
        )

    def test_recorded_at_tke_studios(self):
        block = block_for(read_doc(), ITERATION)
        assert "Recorded 15 August 2026 at TKE Studios in Margate" in block

    def test_primary_tier_rss_feed_opened(self):
        block = block_for(read_doc(), ITERATION)
        assert RSS_FEED in block
        assert re.search(r"PRIMARY", block), (
            "the run must disclose the PRIMARY evidence tier for the 499 RSS read"
        )

    def test_uk_podcasts_metadata_flag(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"uk-podcasts\.co\.uk.*latest episode.*2026-09-07", block), (
            "block must record the uk-podcasts directory metadata that flagged the drop"
        )

    def test_listen_notes_lag_noted(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"Listen Notes.{0,60}lagging on 498", block), (
            "block must note the Listen Notes 2-day crawl still listed 498"
        )

    def test_tech_word_audit_zero_keywords(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(
            r"No Meta, glasses, AI, wearables, privacy, or surveillance vocabulary",
            block,
        ), "tech-word audit must state zero tech keywords in title/description"

    def test_499_prediction_held(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"#601 prediction.*HELD.*0\.85", block), (
            "block must record the #601 499-prediction holding at 0.85"
        )

    def test_500_watch_item_penciled(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"Episode 500.*Monday Sep 14", block), (
            "episode 500 milestone watch item must be penciled for Monday Sep 14"
        )

    def test_audit_bounded_to_surfaces(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"bounded to the surfaced text|bounded to surfaced text", block), (
            "the tech-word audit must be bounded to surfaced text, not audio"
        )

    def test_forty_fourth_cycle_labeled(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"forty-fourth verification cycle", block, re.IGNORECASE), (
            "block must label this the forty-fourth verification cycle"
        )


class TestEHEHold:
    def test_thirty_day_hold(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"30-Day Hold", block)

    def test_no_new_primary_motif(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"No new primary campaign motif", block)

    def test_resurfaces_all_in_corpus(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"re-surfaces only, all in corpus", block)

    def test_seven_resurfaces_distinguished(self):
        block = block_for(read_doc(), ITERATION)
        for marker in (
            "Times Aug 26 spoof-Epstein",
            "feminist.org Feminist Majority Foundation",
            "engadget Jul 13-17 bus-stop",
            "latestly.com Jul 30 fact-check",
            "petapixel.com Jul 23 lenticular-ad",
            "sifted.eu",
            "afrotech.com ethics",
        ):
            assert marker in block, f"EHE re-surface missing: {marker}"

    def test_no_double_counting(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"No double-counting", block)

    def test_no_competitor_equivalent_44_cycles(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"forty-four verification cycles", block, re.IGNORECASE), (
            "the no-competitor-equivalent strand must now span forty-four cycles"
        )

    def test_activist_group_not_podcast(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"activist group, not a podcast", block)


class TestAttentionSphereIdentity:
    def test_44th_no_match_as_podcast(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"forty-fourth no-match", block, re.IGNORECASE)

    def test_circular_github_results_rejected(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"GitHub commits \(rejected as circular\)", block)

    def test_identity_strand_unchanged_from_596(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"identity strand unchanged from #596", block, re.IGNORECASE)

    def test_still_misidentified_in_task_spec(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"task-spec name remains misidentified as a podcast", block)

    def test_tracked_sources_41_to_44_repair(self):
        doc = read_doc()
        table = doc[: doc.index("## Iteration #606")]
        attention_row = next(
            line for line in table.splitlines() if line.startswith("| Attention Sphere |")
        )
        assert "44 verification cycles through Sep 8 2026" in attention_row, (
            "Tracked Sources table must be repaired from 41 to 44 cycles"
        )
        assert "41 verification cycles through Sep 7 2026" not in table, (
            "the stale 41-cycle wording must be gone from the Tracked Sources table"
        )

    def test_guilty_feminist_row_episode_count_repair(self):
        doc = read_doc()
        assert "499 episodes (Sep 8 2026)" in doc, (
            "GF table row must be repaired from ~495 to 499 episodes"
        )
        assert "Active, ~495 episodes" not in doc, (
            "the stale ~495 episode count must be gone"
        )


class TestNewSurfaces:
    def test_zero_new_to_corpus(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(
            r"Zero new-to-corpus press surfaces this run", block
        ), "block must state zero new-to-corpus press surfaces this run"

    def test_startupfortune_lineage(self):
        block = block_for(read_doc(), ITERATION)
        assert "startupfortune.com/meta-glasses-lawsuit-says-intimate-footage-trained-ai-via-kenyan-contractors/" in block
        assert re.search(r"In corpus via #561", block)

    def test_letsdatascience_lineage(self):
        block = block_for(read_doc(), ITERATION)
        assert "letsdatascience.com/news/meta-faces-expanded-smart-glasses-privacy-lawsuit-8bd7207f" in block
        assert re.search(r"In corpus via #586", block)

    def test_biometricupdate_lineage(self):
        block = block_for(read_doc(), ITERATION)
        assert "biometricupdate.com/202609/meta-sued-over-alleged-facial-recognition-training-for-smart-glasses" in block
        assert re.search(r"In corpus via #601", block)

    def test_reuters_bloomberglaw_androidpolice_lineage(self):
        block = block_for(read_doc(), ITERATION)
        for marker in (
            "reuters.com/legal/government/german-advocacy-group-lodges-criminal-complaint",
            "news.bloomberglaw.com/litigation/meta-faces-false-ad-suit",
            "androidpolice.com/meta-ai-glasses-privacy-concern",
        ):
            assert marker in block, f"in-corpus lineage missing: {marker}"

    def test_recency_frontier_tied_not_advanced(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"recency frontier.*TIED|TIED.*recency frontier", block, re.IGNORECASE), (
            "frontier must be stated as TIED at Sep 7, not claimed advanced"
        )

    def test_no_post_sep_7_surface(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"no surface postdates Sep 7", block, re.IGNORECASE)


class TestScoresAndDiscipline:
    def test_manual_illustrative_only(self):
        block = block_for(read_doc(), ITERATION)
        assert "MANUAL ILLUSTRATIVE" in block

    def test_no_significance_claimed(self):
        block = block_for(read_doc(), ITERATION)
        assert "p_value NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_no_tone_scores_on_episode(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"No tone scores computed on the episode", block)

    def test_no_em_dashes_in_block(self):
        block = block_for(read_doc(), ITERATION)
        assert "\u2014" not in block, "em dash found in Iteration #606 block"
        assert "\u2013" not in block, "en dash found in Iteration #606 block"

    def test_no_em_dashes_in_this_test_file(self):
        text = (TESTS_DIR / TEST_FILE).read_text(encoding="utf-8")
        assert "\u2014" not in text, "em dash found in test file"
        assert "\u2013" not in text, "en dash found in test file"


class TestSources:
    def test_rss_feed_url_verbatim(self):
        block = block_for(read_doc(), ITERATION)
        assert "https://feeds.megaphone.fm/APL9072247766" in block

    def test_uk_podcasts_urls_present(self):
        block = block_for(read_doc(), ITERATION)
        assert "https://uk-podcasts.co.uk/podcast/the-guilty-feminist" in block

    def test_listen_notes_and_chortle_present(self):
        block = block_for(read_doc(), ITERATION)
        assert "listennotes.com/podcasts/the-guilty-feminist" in block
        assert "chortle.co.uk" in block

    def test_carlfreedman_gallery_url(self):
        block = block_for(read_doc(), ITERATION)
        assert "https://carlfreedman.com/exhibition/lindsey-mendick-2026/" in block

    def test_ehe_source_urls_verbatim(self):
        block = block_for(read_doc(), ITERATION)
        for url in (
            "https://www.thetimes.com/uk/london/article/meta-ai-glasses-spoof-advert-jeffrey-epstein-slx3wttm5",
            "https://feminist.org/news/helpful-or-hurtful-the-growing-privacy-debate-over-meta-glasses/",
            "https://www.latestly.com/social-viral/fact-check/did-jeffrey-epstein-feature-on-meta-smart-glasses-billboard-ad-in-london-fact-check-finds-viral-claim-fake-7538349.html",
        ):
            assert url in block, f"EHE source URL missing: {url}"


class TestConfoundersAndLog:
    def test_strong_confounders_present(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"STRONG:", block)

    def test_keyword_audit_limited_to_show_notes(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"absence of tech vocabulary in show notes does not prove", block), (
            "the keyword-audit limit must be stated as a STRONG confounder"
        )

    def test_listing_lag_confounders_ranked(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"listing-based holds are time-bounded to this run", block)

    def test_hours_cadence_bounded(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"time-bounded to this run", block)

    def test_novelty_verification_claimed(self):
        block = block_for(read_doc(), ITERATION)
        assert re.search(r"Novelty verification:", block)

    def test_log_entry_present_newest_first(self):
        log = read_log()
        assert log.startswith("#606 Type E:"), (
            "iteration-log.md must start with the #606 entry (newest-first)"
        )

    def test_log_entry_covers_rotation_edge(self):
        log = read_log()
        head = log[:4000]
        assert re.search(r"rotation 605 D -> 606 E", head)

    def test_605_entry_repositioned(self):
        log = read_log()
        pos606 = log.find("#606 Type E:")
        pos605 = log.find("#605 Type D:")
        pos604 = log.find("#604 Type C:")
        assert pos606 != -1 and pos605 != -1 and pos604 != -1
        assert pos606 < pos605 < pos604, (
            "#606 must precede #605 which must precede #604 (newest-first)"
        )
        assert pos604 < 40000, (
            f"#604 entry should sit near the top after the miss repair, "
            f"found at char {pos604}"
        )


class TestNoBrittleSweep606:
    def test_current_cycle_label_not_stale(self):
        block = block_for(read_doc(), ITERATION)
        assert "forty-third verification cycle" not in block.lower(), (
            "block must not claim the forty-third label for this run"
        )
        assert "43rd verification cycle is new" not in block.lower(), (
            "block must not claim the 43rd cycle as this run"
        )

    def test_distinct_from_601(self):
        block = block_for(read_doc(), ITERATION)
        assert "extends #601" in block or "distinct from #601" in block

    def test_no_zero_coverage_claims(self):
        block = block_for(read_doc(), ITERATION)
        assert not re.search(r"\bzero coverage\b", block, re.IGNORECASE)

    def test_no_em_dash_in_rotation_guard_anchor_line(self):
        text = (TESTS_DIR / TEST_FILE).read_text(encoding="utf-8")
        assert "\u2014" not in text


class TestRotationCycleGuard606:
    """Rotation guard, deselected pre-commit per the #565 followup convention.

    Asserts the post-commit anchor, so it runs green only in the followup
    commit after the main commit SHA is known. Pre-commit it is deselected.
    """

    ANCHORED_COMMIT = "POST_COMMIT_ANCHOR"

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

    def test_window_602_606_closes_d_to_e(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("E", "606"),
            ("D", "605"),
            ("C", "604"),
            ("B", "603"),
            ("A", "602"),
        ], f"rotation window 602-606 wrong: {observed}"

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


class TestDocSyncRatchet606:
    def test_readme_row_for_606(self):
        readme = read_readme()
        assert re.search(r"#606", readme), "README.md missing the #606 test-table row"

    def test_arch_row_for_606(self):
        arch = read_arch()
        assert re.search(r"#606", arch), "docs/ARCHITECTURE.md missing the #606 tree row"

    def test_601_row_survives_in_readme(self):
        readme = read_readme()
        assert re.search(r"#601", readme), "README.md lost the #601 row"

    def test_601_row_survives_in_arch(self):
        arch = read_arch()
        assert re.search(r"#601", arch), "docs/ARCHITECTURE.md lost the #601 row"

    def test_iteration_log_606_entry_present(self):
        log = read_log()
        assert "#606 Type E" in log

    def test_count_stats_gate_green(self):
        out = subprocess.run(
            [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "count_stats.py"), "--check"],
            capture_output=True, text=True, timeout=600, cwd=str(REPO_ROOT))
        assert out.returncode == 0, f"count_stats --check failed:\n{out.stdout}\n{out.stderr}"
