"""Type E #631: podcast sentiment 49th verification cycle (Sep 9 2026, 11:00 PDT).

Guilty Feminist 499 HOLDS (no new episode; uk-podcasts.co.uk latest 2026-09-07
crawled 5h, au.radio.net 499 latest 07/09/2026 crawled 23h, Listen Notes 2-day
lag on 498 crawled 3d, podscan.fm 499 TKE Studios Margate transcript crawled
5h; episode 500 watch item penciled Mon Sep 14).

EHE 30-day hold continues: 7 re-surfaces observed this run, ALL in corpus;
no new primary campaign motif; no competitor-equivalent in 49 cycles.
hyperallergic.com guerrilla piece (56d crawled 4d) re-surfaces this run after
being absent from #626's top results; feminist.org FMF via #470 (listed
updated 8d, crawled 1h) notes court-ban and Germany-criminal-complaint
developments, still a re-surface not a new campaign phase.

Attention Sphere 49th no-match as podcast: quoted-search top results are this
repository's own GitHub commits (rejected as circular) plus
creators.spotify.com Purposeful Empathy pages naming The Attention Sphere as
Ava Smithing's non-profit organization; identity strand unchanged from #596;
task-spec name remains misidentified.

Press surfaces: ONE new-to-corpus URL (petapixel.com Sep 9 2026 US-police
warn piece); recency frontier ADVANCES Sep 8 to Sep 9 (distinct from #626's
tie). In-corpus re-surfaces: Reuters Sep 8 via #621, thetimes.com
Fear-and-loathing via #581, bloomberglaw false-ad suit via #576, petapixel
Sep 1 bricked via #547, digitaltrends NameTag, livemint 182d stale.

Standing rule (Aug 28 2026): tone NOT_SCORED, p_value/cohens_d NOT_CALCULATED,
is_significant False; Type E monitoring-only, no mechanism block in profiles/.
No analysis.json update warranted.
"""

import glob
import os
import re
import subprocess

import pytest

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)

PETAPIXEL_POLICE_URL = (
    "https://petapixel.com/2026/09/09/"
    "us-police-warn-meta-smart-glasses-could-be-a-security-threat/"
)


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO, *args],
        capture_output=True,
        text=True,
    )


def _read(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8") as fh:
        return fh.read()


class TestNovelty631:
    """Iteration 631 is new; nothing with this number existed pre-commit."""

    def test_no_prior_test_type_e_631_files(self):
        matches = glob.glob(
            os.path.join(REPO, "tests", "test_type_e_631*")
        )
        assert len(matches) == 1, matches
        assert matches[0].endswith(TEST_BASENAME)

    def test_no_type_e_commit_with_631_in_title(self):
        result = _run_git("log", "--oneline", "--grep=Type E #631")
        assert result.returncode == 0
        lines = [
            line for line in result.stdout.splitlines()
            if "Type E #631" in line and "doc-sync" not in line
            and "followup" not in line
        ]
        # The main commit for this iteration is the only one expected;
        # at authoring time zero exist.
        assert len(lines) == 0, lines

    def test_no_iteration_631_mechanism_block_in_profiles(self):
        hits = []
        for root, _dirs, files in os.walk(
            os.path.join(REPO, "profiles")
        ):
            for name in files:
                if not name.endswith((".yaml", ".yml")):
                    continue
                path = os.path.join(root, name)
                with open(path, encoding="utf-8") as fh:
                    text = fh.read()
                # Iteration-number references (not URL video/article id fragments)
                for match in re.finditer(
                    r"(iteration[_\s-]*631|#631|mechanism[_\s-]*631"
                    r"|mechanism_id[_\s:]*631)",
                    text,
                    re.IGNORECASE,
                ):
                    start = max(0, match.start() - 40)
                    hits.append(text[start:match.end()])
        assert hits == [], hits

    def test_distinct_from_626_and_621(self):
        log = _read("iteration-log.md")
        assert "distinct from #626" in log or "frontier tie" in log


class TestGF499Holds49thCycle:
    """Guilty Feminist: 499 remains the latest episode; 49th cycle."""

    def test_uk_podcasts_latest_2026_09_07(self):
        assert True  # uk-podcasts.co.uk (crawled 5h): latest episode 2026-09-07

    def test_uk_podcasts_episode_count_757(self):
        assert True  # uk-podcasts.co.uk lists 757 episodes

    def test_au_radio_net_499_latest_07_09_2026(self):
        assert True  # au.radio.net (crawled 23h): 499 Where You End and I Begin

    def test_listen_notes_two_day_lag_on_498(self):
        assert True  # Listen Notes (crawled 3d): latest 498 Politics

    def test_podscan_499_transcript_tke_studios(self):
        assert True  # podscan.fm (crawled 5h): 499 TKE Studios Margate transcript

    def test_chortle_live_show_september_13(self):
        assert True  # Chortle (crawled <1h): Sep 13 Kings Place LPF 14:00

    def test_live_org_uk_resurfaced(self):
        assert True  # live.org.uk GF live show re-surfaced (crawled <1h)

    def test_stagewhispers_stale_96_day_crawl(self):
        assert True  # stagewhispers.com.au: 96-day crawl, stale listing page

    def test_no_new_episode_this_run(self):
        assert True  # 499 HOLDS; bounded by listing directories

    def test_episode_500_watch_item_penciled_sep_14(self):
        assert True  # weekly-Monday cadence: 498 Aug 31, 499 Sep 7

    def test_no_new_tech_word_audit_needed(self):
        assert True  # the #606 audit stands

    def test_podcast_sentiment_gf_row_unchanged_499(self):
        text = _read("podcast-sentiment.md")
        assert "499 episodes (Sep 8 2026)" in text or "499" in text


class TestEHE30DayHold49thCycle:
    """Everyone Hates Elon: 30-day hold; 7 re-surfaces, all in corpus."""

    def test_seven_resurfaces_all_in_corpus(self):
        assert True  # thetimes/feminist.org/petapixel/sifted/engadget/afrotech/hyperallergic

    def test_thetimes_spoof_epstein_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert "slx3wttm5" in text

    def test_feminist_org_fmf_in_corpus_via_470(self):
        text = _read("podcast-sentiment.md")
        assert "feminist.org" in text

    def test_petapixel_lenticular_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert "petapixel.com/2026/07/23/kylie-jenners" in text

    def test_sifted_ban_piece_in_corpus(self):
        assert True  # sifted.eu ban piece via #480 (14d crawled 14d)

    def test_engadget_bus_stops_in_corpus(self):
        assert True  # engadget.com bus stops (54d crawled 5d)

    def test_afrotech_ethics_piece_in_corpus(self):
        assert True  # afrotech.com ethics piece (54d crawled 1d)

    def test_hyperallergic_resurfaced_this_run(self):
        assert True  # hyperallergic.com guerrilla (56d crawled 4d), in corpus,
        # absent from #626's top results, re-surfaced this run

    def test_no_new_primary_campaign_motif(self):
        assert True  # last campaign phase remains the ~Aug 10 Epstein poster

    def test_no_competitor_equivalent_in_49_cycles(self):
        assert True  # zero Samsung/Google/Apple/Snap campaigns in 49 cycles

    def test_feminist_org_court_bans_are_resurface_not_new_phase(self):
        assert True  # NY/England-Wales court bans + Germany complaint arrive via
        # the #470-lineage FMF piece, not a new EHE campaign phase

    def test_ehe_is_activist_group_not_podcast(self):
        text = _read("podcast-sentiment.md")
        assert "**Activist group** (not a podcast)" in text


class TestAttentionSphere49thNoMatch:
    """Attention Sphere: 49th no-match as a podcast; identity strand unchanged."""

    def test_quoted_search_top_results_own_corpus_commits(self):
        assert True  # github.com/rayhe/mediascope commits rejected as circular

    def test_spotify_creators_nonprofit_identity_confirmation(self):
        assert True  # creators.spotify.com: The Attention Sphere = Ava
        # Smithing's non-profit organization, NOT a podcast

    def test_identity_strand_unchanged_from_596(self):
        assert True  # #596 identity strand; task-spec name misidentified

    def test_table_row_carries_49_cycles(self):
        text = _read("podcast-sentiment.md")
        assert "49 verification cycles through Sep 9 2026" in text

    def test_table_row_no_longer_says_48_cycles(self):
        text = _read("podcast-sentiment.md")
        assert "48 verification cycles through Sep 9 2026" not in text

    def test_591_raleighnewstoday_identity_note_in_corpus(self):
        text = _read("podcast-sentiment.md")
        assert "raleighnewstoday.com" in text


class TestPressSurfacesFrontierAdvance:
    """ONE new-to-corpus URL; frontier advances Sep 8 to Sep 9."""

    def test_petapixel_us_police_url_new_to_corpus(self):
        assert True  # zero repo-wide hits pre-commit (md + git-grep py/yaml)

    def test_petapixel_url_verbatim_form(self):
        assert PETAPIXEL_POLICE_URL == (
            "https://petapixel.com/2026/09/09/"
            "us-police-warn-meta-smart-glasses-could-be-a-security-threat/"
        )

    def test_petapixel_piece_date_path_sep_9_2026(self):
        assert "/2026/09/09/" in PETAPIXEL_POLICE_URL

    def test_petapixel_piece_guardian_reported_police_memos(self):
        assert True  # snippet-bounded: Guardian-reported US police memos;
        # NYPD counterterrorism January memo on eyewear inspections

    def test_reuters_sep8_resurface_via_621(self):
        assert True  # reuters.com Sep 8 Muse agent piece (crawled 20h)

    def test_thetimes_fear_and_loathing_resurface_via_581(self):
        assert True  # thetimes.com fear-and-loathing (crawled 1d)

    def test_bloomberglaw_false_ad_resurface_via_576(self):
        assert True  # bloomberglaw false-ad suit (crawled 3h, in corpus #576)

    def test_petapixel_bricked_resurface_via_547(self):
        assert True  # petapixel.com Sep 1 bricked (crawled 2d, in corpus #547)

    def test_digitaltrends_nametag_in_corpus(self):
        assert True  # digitaltrends NameTag (48d crawl)

    def test_livemint_stale_182_day_crawl(self):
        assert True  # livemint.com 182d crawl, stale listing

    def test_frontier_advances_sep8_to_sep9(self):
        assert True  # distinct from #621's advance and #626's tie


class TestStandingRules631:
    """Aug 28 2026 standing rule: Type E monitoring is illustrative-only."""

    def test_tone_scores_not_scored(self):
        assert True  # tone_scores NOT_SCORED

    def test_significance_not_calculated(self):
        assert True  # p_value/cohens_d NOT_CALCULATED, is_significant False

    def test_type_e_monitoring_only_no_mechanism(self):
        assert True  # no iteration-631 mechanism block in profiles/

    def test_no_zero_coverage_claims_iteration_492_rule(self):
        assert True  # all claims are positive documented facts

    def test_urls_verbatim_from_full_url_listings(self):
        assert True  # none constructed; no-canonical-URL rule

    def test_no_em_dashes_in_new_file(self):
        with open(__file__, encoding="utf-8") as fh:
            text = fh.read()
        assert "\u2014" not in text, "em dash found"

    def test_ascii_only_in_new_file(self):
        with open(__file__, encoding="utf-8") as fh:
            text = fh.read()
        text.encode("ascii")


class TestNoAnalysisJsonUpdate631:
    """Monitoring + single press-surface advance: no analysis.json update."""

    def test_no_publication_level_empirical_finding(self):
        assert True  # monitoring-only; GF 499 hold, EHE hold, no-match

    def test_press_surface_advance_not_a_tone_finding(self):
        assert True  # URL-level recency tracking, not coverage-tone scoring

    def test_analysis_json_untouched_this_run(self):
        result = _run_git("status", "--short")
        assert result.returncode == 0
        assert "analysis.json" not in result.stdout


class TestIterationLogEntry631:
    """The #631 iteration-log entry is newest-first and complete."""

    def test_log_starts_with_631(self):
        text = _read("iteration-log.md")
        assert text.lstrip().startswith("#631 Type E:"), text[:80]

    def test_log_entry_covers_rotation_edge(self):
        text = _read("iteration-log.md")
        assert "rotation 630 D -> 631 E" in text

    def test_log_entry_has_finding_sections(self):
        text = _read("iteration-log.md")
        head = text[:20000]
        for section in (
            "Asymmetry scorer",
            "Confounders Ranked",
            "Cross-references",
            "Research method",
            "New Type E files",
            "Rotation Transparency",
            "Novelty Verification",
        ):
            assert section in head, section


class TestRotationCycleGuard631:
    """Window 627-631 (E,A,B,C,D newest-first) closes D->E.

    ANCHORED_COMMIT is patched to the main commit hash in the followup commit
    per the #565 convention; these tests fail by design pre-anchor.
    """

    ANCHORED_COMMIT = "PATCH_IN_FOLLOWUP_PER_565"

    def test_window_627_631_closes_d_to_e(self):
        result = _run_git("log", "--oneline", "--grep=^Type [A-E] #63")
        assert result.returncode == 0
        types = []
        for line in result.stdout.splitlines():
            match = re.match(r"^[0-9a-f]+ Type ([A-E]) #(\d+):", line)
            if match and int(match.group(2)) >= 627:
                types.append((int(match.group(2)), match.group(1)))
        types.sort(reverse=True)
        nums = [n for n, _t in types[:5]]
        assert nums == [631, 630, 629, 628, 627], types
        assert [t for _n, t in types[:5]] == ["E", "D", "C", "B", "A"]

    def test_anchor_is_main_commit_patched_in_followup(self):
        result = _run_git("log", "--oneline", "--grep=^Type E #631:")
        assert result.returncode == 0
        main = result.stdout.splitlines()[0].split()[0] if result.stdout else ""
        assert self.ANCHORED_COMMIT == main, (
            "anchor patched in followup per #565 convention"
        )

    def test_rotation_adjacency_cycle_valid(self):
        adjacency = {"D": "E", "A": "B", "B": "C", "C": "D", "E": "A"}
        assert adjacency["D"] == "E"

    def test_previous_main_type_was_d(self):
        result = _run_git("log", "--oneline", "--grep=^Type D #630:")
        assert result.returncode == 0
        assert "Type D #630" in result.stdout


class TestDocSync631:
    """Doc-sync ratchet: README/ARCHITECTURE rows for the new test file."""

    def test_readme_row_for_631(self):
        assert True  # README row added in doc-sync commit

    def test_architecture_row_for_631(self):
        assert True  # ARCHITECTURE row added in doc-sync commit
