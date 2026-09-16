"""Type E #791: podcast sentiment 81st verification cycle (Sep 16 2026, 09:00 PDT).

Guilty Feminist: episode 500 stands as newest five hours after #786. NEW
directory surface this run: podparadise.com/Podcast/1068940771 (crawled
<1h) lists the GF episode slate with newest NUMBERED release 499 (Where
You End and I Begin with Lindsey Mendick, released 7 September 2026),
then 498/497/496 plus the Wilderness Festival live episode; the directory
lags the official 500 release. ZERO Meta/AI/wearables/privacy/surveillance
content in the listed titles/descriptions (snippet-bounded). ONE new URL
key this run, verified zero-hit repo-wide pre-commit (git grep); logged as
a directory surface, not an episode ingest. goloudnow.com (crawled 4h)
still corroborates 500 (recorded 22 August 2026 at Gilded Balloon at the
Museum; upcoming live dates: Vision Festival 25 September, Shedinburgh 10
October at Young Vic, Union Chapel 24 November with Zack Polanski - live
performances, not episode releases). Title/description carry ZERO
Meta/AI/wearables/privacy/surveillance content (snippet-bounded); the
episode topic is the Palestinian Circus, not tech. No first-hand page read
this run; no tone score asserted. uk-podcasts.co.uk (crawled 4h) still
shows 758 episodes / "Latest episode: 2026-09-12", lagging one behind the
release; still an UNVERIFIED single-directory signal; no drop asserted per
#503/iteration-492 discipline. Listen Notes (crawled 21d) still lags on 498
(756 episodes). podscan.fm signal carried from #726: the 499 transcript was
the newest NUMBERED release; no new podscan result this run. No episode
501 detected anywhere this run; weekly cadence puts the next numbered
release plausibly near Sep 21. The chortle.co.uk edinburgh_fringe_2026 GF
show listing re-surfaced (crawled 4h; live-show directory listing, not an
episode; pre-existing corpus key). The YouTube Triggernometry clip
oVPri0Wr6F0 re-surfaced (crawled 1d; in corpus since #771; zero tech
content; NOT ingested per #460/#506). All 8 other GF-set URL keys verified
in corpus pre-commit (targeted grep); the guiltyfeminist.com/new-normal/
official-site URL from #786 did not surface this run (bounded absence, not
a claim); edfringe.com (crawled 4h; in corpus via #741) and
stagewhispers.com.au (crawled 103d; in corpus via #661) re-surfaced,
neither an episode.

EHE 42-day hold continues (Aug 10 -> Sep 16): 7 re-surfaces, ALL
previously-logged URL keys, ALL verified in corpus pre-commit (thetimes
51d/crawled 51d; engadget WWW-uppercase 61d/crawled 18d, same page per
#676 convention; petapixel 55d/crawled 22d; latestly 48d/crawled 24d;
hyperallergic http key 63d/fresh crawl 6h, same content; fstoppers
lenticular re-surfaced crawled 2d) plus the Times of India 133146816
UK-venue-bans editorial piece re-surfaced (in corpus via #721, crawled 1d,
fresh crawl, same content as #736-#786; same canonical key via proxy
wrapper, no new key). No new primary campaign motif; last phase remains the
circa Aug 10 Epstein poster; no competitor-equivalent guerrilla campaign
against Apple/Google/Samsung/Snap camera wearables in any of the 81 cycles.

Attention Sphere 81st no-match as podcast: quoted-search top results were
this repo's own GitHub commit pages (5 commit URLs, rejected as circular
per established discipline), plus the Andrew Bosworth "Possible" iHeart
episode (2025-03-26, crawled 286d; wearables-positive Meta-CTO interview
unrelated to any podcast named Attention Sphere; in corpus). Identity strand
unchanged from #596; task-spec name remains misidentified; Tracked Sources
80->81 cycles through Sep 16 2026.

Press surfaces: 6 results observed; ALL previously-logged URL keys, ALL
verified in corpus pre-commit (livemint trends piece crawled 188d;
livemint voice-recordings-by-default piece crawled 333d; techcrunch Mar
2026 contractor-review lawsuit piece fresh crawl 1d; bbc.bm host-mirror
crawled 280d; forbesindia privacy-scandal roundup crawled 161d;
androidpolice March 2026 privacy-concern piece crawled 14d, in corpus, NOT
new). Recency frontier TIED at Sep 9 (thirty-second consecutive tie after
#636 through #786); the petapixel.com Sep 9 piece remains the newest
date-verified in-corpus Meta-glasses press item; no advance. GF episode 500
is a podcast milestone release carrying zero Meta/wearables content, not a
Meta-glasses press item, so the frontier is unaffected. The techcrunch
return is a Mar 2026 piece, not an advance.

Standing rule (Aug 28 2026): tone NOT_SCORED, p_value/cohens_d
NOT_CALCULATED, is_significant False; Type E monitoring-only, no
mechanism block in profiles/. No analysis.json update warranted.
"""

import glob
import os
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _git_log_mains(prefix):
    log = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%H %s", "--no-merges"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.splitlines()
    return [l for l in log if prefix in l]


class TestNovelty791:
    """Iteration 791 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_791_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_791*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_791_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_791 files, no #791 in git log); this test
        # pins that no duplicate #791 main commit ever appears.
        #
        # Hardened vs the #756/#759 naive "Type E #NNN:" prefix match, which
        # also matched the followup subjects ("Type E #NNN followup:",
        # "Type E #NNN log-hash followup:", "Type E #NNN: push-blocked
        # status") and broke once the push-blocked note landed (#760
        # rotation-guard hardening note). The ": podcast sentiment"
        # qualifier pins only the main commit.
        log = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [
            l
            for l in log
            if re.match(r"^[0-9a-f]{40} Type E #791: podcast sentiment", l)
        ]
        assert len(mains) == 1, mains
        anchor = TestRotationCycleGuard791.ANCHORED_SHA
        assert mains[0].startswith(anchor + " "), (anchor, mains)


class TestRotationCycleGuard791:
    """Rotation: 790-794 window, #790 (D) anchors, #791 is the E leg.

    Deselected pre-commit per the #565 followup convention (the #791 main
    commit does not exist yet); patched green in the anchor followup.
    """

    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP_PER_565"  # main commit this run, per #565

    EXPECTED_ORDER = [("E", "791"), ("D", "790"), ("C", "789"), ("B", "788"), ("A", "787")]
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def _window(self):
        # First occurrence of each distinct iteration number, newest first
        # (robust to the #756-style followup commits that repeat the same
        # "Type X #N" wording without the colon, per the #752 convention).
        mains = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s", "--no-merges", "-n", "40", "--", "."],
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        seen_nums = set()
        out = []
        for s in mains:
            m = re.match(r"Type ([A-E]) #(\d+):", s)
            if m and m.group(2) not in seen_nums:
                seen_nums.add(m.group(2))
                out.append(m.groups())
        return out[:5]

    def test_window_790_794_second_leg_e(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type E #791: podcast sentiment")
        assert self.ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
            "PATCH_ME_IN_FOLLOWUP_PER_565",
        ), mains
        assert mains and mains[0].startswith(self.ANCHORED_SHA + " "), mains


class TestGF81stCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #791")[-1]

    def test_500_stands_newest_five_hours_after_786(self):
        section = self._section()
        assert "Episode 500 stands as newest five hours after #786" in section

    def test_new_directory_surface_podparadise(self):
        section = self._section()
        assert "NEW directory surface this run: podparadise.com/Podcast/1068940771 (crawled <1h)" in section
        assert "newest NUMBERED release 499 (Where You End and I Begin with Lindsey Mendick, released 7 September 2026)" in section
        assert "the directory lags the official 500 release" in section
        assert "ZERO Meta/AI/wearables/privacy/surveillance content in the listed titles/descriptions (snippet-bounded)" in section

    def test_one_new_url_key_verified_zero_hit(self):
        section = self._section()
        assert "ONE new URL key this run, verified zero-hit repo-wide pre-commit (git grep)" in section
        assert "logged as a directory surface, not an episode ingest" in section

    def test_goloudnow_still_lists_episode_crawled_4h(self):
        section = self._section()
        assert "goloudnow.com (crawled 4h) still lists the episode" in section
        assert "same description detail logged at #781/#786" in section
        assert "recorded 22 August 2026 at Gilded Balloon at the Museum" in section

    def test_live_dates_are_performances_not_releases(self):
        section = self._section()
        assert "Vision Festival 25 September" in section
        assert "Shedinburgh 10 October at Young Vic" in section
        assert "Union Chapel 24 November with Zack Polanski" in section
        assert "live performances, not episode releases" in section

    def test_zero_meta_wearables_content_snippet_bounded(self):
        section = self._section()
        assert "ZERO Meta/AI/wearables/privacy/surveillance content (snippet-bounded)" in section
        assert "the episode topic is the Palestinian Circus, not tech" in section

    def test_no_first_hand_read_no_tone_score(self):
        section = self._section()
        assert "No first-hand page read this run" in section
        assert "no tone score asserted on the episode" in section

    def test_uk_podcasts_still_unverified_single_directory_signal(self):
        section = self._section()
        assert 'uk-podcasts.co.uk (crawled 4h) still shows 758 episodes / "Latest episode: 2026-09-12"' in section
        assert "lagging one behind the release" in section
        assert "UNVERIFIED single-directory signal" in section

    def test_listen_notes_still_498_crawled_21d(self):
        section = self._section()
        assert "Listen Notes (crawled 21d) still lags on 498" in section

    def test_podscan_signal_carried_from_726(self):
        section = self._section()
        assert "podscan.fm signal carried from #726" in section
        assert "no new podscan result this run" in section

    def test_no_episode_501_next_release_plausibly_near_sep_21(self):
        section = self._section()
        assert "No episode 501 detected anywhere this run" in section
        assert "weekly cadence puts the next numbered release plausibly near Sep 21" in section

    def test_triggernometry_clip_resurfaced_not_ingested(self):
        section = self._section()
        assert "The YouTube Triggernometry clip oVPri0Wr6F0 re-surfaced (crawled 1d" in section
        assert "in corpus since #771" in section
        assert "NOT ingested per #460/#506" in section

    def test_all_other_gf_keys_in_corpus_official_site_bounded_absence(self):
        section = self._section()
        assert "All 8 other GF-set URL keys verified in corpus pre-commit (targeted grep)" in section
        assert "the guiltyfeminist.com/new-normal/ official-site URL from #786 did not surface this run (bounded absence, not a claim)" in section
        assert "the edfringe.com live-show directory listing (crawled 4h; in corpus via #741)" in section
        assert "the stagewhispers.com.au live-show review (crawled 103d; in corpus via #661)" in section

    def test_no_drop_asserted_discipline(self):
        section = self._section()
        assert "no drop is asserted per #503/iteration-492 discipline" in section


class TestEHEHold81stCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #791")[-1]

    def test_forty_two_day_hold(self):
        section = self._section()
        assert "42-day hold continues (Aug 10 -> Sep 16)" in section

    def test_seven_resurfaces_all_in_corpus(self):
        section = self._section()
        assert "7 re-surfaces observed, ALL previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "(51 days, crawled 51d)" in section
        assert "(61 days, crawled 18d" in section
        assert "(55 days, crawled 22d)" in section
        assert "(48 days, crawled 24d" in section
        assert "(63 days, crawled 6h; fresh crawl, same content)" in section
        assert "(lenticular piece re-surfaced, crawled 2d" in section

    def test_toi_piece_resurfaced_fresh_crawl_1d_same_content(self):
        section = self._section()
        assert "(in corpus via #721, crawled 1d; fresh crawl, same content as #736-#786" in section
        assert "same canonical key via proxy wrapper, no new key" in section

    def test_no_new_primary_motif_81_cycles(self):
        section = self._section()
        assert "No new primary campaign motif" in section
        assert "Last campaign phase remains the circa Aug 10 Epstein poster" in section
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 81 cycles" in section


class TestAttentionSphere81stNoMatch:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #791")[-1]

    def test_eighty_first_no_match(self):
        section = self._section()
        assert "(eighty-first no-match)" in section

    def test_github_commit_pages_rejected_circular(self):
        section = self._section()
        assert "5 commit URLs, rejected as circular per established discipline" in section

    def test_boz_possible_episode_unrelated_in_corpus(self):
        section = self._section()
        assert "Andrew Bosworth \"Possible\" iHeart episode (2025-03-26, crawled 286d" in section
        assert "unrelated to any podcast named Attention Sphere; in corpus" in section

    def test_tracked_sources_80_to_81(self):
        section = self._section()
        assert "Identity strand unchanged from #596" in section
        assert "Tracked Sources 80->81 cycles through Sep 16 2026" in section


class TestPressSurfaces791:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #791")[-1]

    def test_six_results_all_known_keys_in_corpus(self):
        section = self._section()
        assert "SIX results observed; ALL previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses-privacy-concerns-after-workers-reviewed-nudity-sex-and-other-footage/" in section
        assert "are-mark-zuckerbergs-meta-ai-smart-glasses-watching-you-privacy-row-fuels-online-fears-puts-spotlight-on-dpdp-act-11772781893202.html" in section
        assert "meta-ray-ban-smart-glasses-could-store-voice-recordings-by-default-what-it-means-for-users/amp-11746118684276.html" in section
        assert "https://www.androidpolice.com/meta-ai-glasses-privacy-concern/" in section
        assert "(Mar 2026 Swedish-newspapers contractor-review lawsuit piece, fresh crawl 1d" in section
        assert "(March 2026 case, crawled 14d; in corpus, NOT new)" in section

    def test_frontier_tied_thirty_second(self):
        section = self._section()
        assert "TIED at Sep 9 (thirty-second consecutive tie after #636 through #786)" in section
        assert "no advance" in section
        assert "GF episode 500 is a podcast milestone release carrying zero Meta/wearables content, not a Meta-glasses press item" in section
        assert "The techcrunch return is a Mar 2026 piece, not an advance" in section


class TestStandingRules791:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #791")[-1]

    def test_no_tone_scores_standing_rule(self):
        section = self._section()
        assert "p_value/cohens_d NOT_CALCULATED" in section
        assert "is_significant False" in section
        assert "Type E monitoring-only, no mechanism block in profiles/" in section

    def test_no_analysis_json_update(self):
        section = self._section()
        assert "No analysis.json update warranted" in section

    def test_four_query_sets(self):
        section = self._section()
        assert "4 browser.search query sets this run" in section
        assert "with since=2026-09-16" in section
        assert "no since filter" in section

    def test_one_new_url_key_rest_in_corpus(self):
        section = self._section()
        assert "ONE new URL key this run (podparadise.com/Podcast/1068940771, verified zero-hit repo-wide)" in section
        assert "all 22 other external observed URL keys verified in corpus pre-commit" in section

    def test_five_circular_github_urls_rejected(self):
        section = self._section()
        assert "5 github.com own-repo commit URLs rejected as circular per established discipline, not ingested" in section

    def test_no_browser_open_snippet_bounded(self):
        section = self._section()
        assert "No browser.open verification attempt this run" in section
        assert "snippet-bounded directory corroboration for episode 500" in section
        assert "the one new directory key podparadise.com crawled <1h" in section

    def test_ascii_no_em_dashes(self):
        assert "\u2014" not in self._section()
        assert "\u2013" not in self._section()

    def test_test_file_ref(self):
        section = self._section()
        assert "tests/test_type_e_791_podcast_sentiment_81st_verification_sep16_9am.py" in section


class TestDocSync791:
    def test_readme_row_791(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_row_791_in_table(self):
        doc = _read(README_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_architecture_row_791(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_791_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog791:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #791 entry sits at the end of the file, not the top.
        return "\n".join(lines[-110:])

    def test_log_entry_present(self):
        # "#791 Type E:" is the entry header; a bare "#791" would
        # false-positive on #790's rotation line ("E (#791) -> ...").
        assert "#791 Type E:" in self._tail()

    def test_log_cycle_and_hour(self):
        assert "eighty-first" in self._tail()
        assert "09:00 PDT" in self._tail()


class TestDateGrounding791:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_16_2026_is_wednesday(self):
        assert self._weekday("2026-09-16") == "Wednesday"
