"""Type E #801: podcast sentiment 83rd verification cycle (Sep 17 2026, 04:00 PDT).

Guilty Feminist: episode 500 stands as newest seventeen hours after #796
(23:00 PDT Sep 16). Official-site corroboration carried from #796
(guiltyfeminist.com/new-normal/, crawled 18h at #796; ~23h elapsed by this
run); no fresh browser.open this run, snippet-bounded method per #796.
uk-podcasts.co.uk (crawled 4h) now shows 760 episodes / "Latest episode:
2026-09-16" (was 758 / 2026-09-12 at #796); still an UNVERIFIED
single-directory signal; no episode-501 asserted per #503/iteration-492
discipline. Listen Notes still lags on 498 (756 episodes; Last Crawl 10
days ago). podparadise / goloudnow / chortle / edfringe / stagewhispers not
observed this run (bounded absence; signals carried from #796). No episode
501 detected anywhere this run; weekly cadence puts the next numbered
release plausibly near Sep 21. THREE new URL keys this run, ALL GF
distribution surfaces with ZERO Meta/wearables content (snippet-bounded):
youtube.com/watch?v=DTtg_5J9Fqc (GF 479 Welsh Election Special part two,
recorded 12 April 2026 New Theatre Cardiff, released 20 April; politics,
not tech), youtube.com/watch?v=_u8jWa1dqBc (GF 473 ROAD TO GILEAD: Fascism
with Desiree Burch and Professor Roger Griffin, recorded 20 Feb 2026 Museum
of Comedy, released 9 Mar; politics, not tech), and the iHeart GF podcast
page (shown episodes 458 Annie Lennox at the V&A Nov 2025 + Emergency
Episode Gaza nurse Alaa Al-ghoul Nov 2025; not tech). GF-set: 7 URL keys
observed (4 previously-logged verified in corpus pre-commit + 3 new logged
this run).

EHE 43-day hold continues (Aug 10 -> Sep 17): 7 re-surfaces, ALL
previously-logged URL keys, ALL verified in corpus pre-commit (thetimes
52d/crawled 52d; engadget WWW-uppercase 62d/crawled 3d, same page per #676
convention; petapixel 56d/crawled 15h; latestly 49d/crawled 25d;
hyperallergic http key 64d/crawled 18h, same content; Times of India
133146816 via proxy wrapper, 37 days updated/crawled 2d, in corpus via
#721, same content; fstoppers lenticular crawled 3d, in corpus via
#465/#536). No new primary campaign motif; last phase remains the circa
Aug 10 Epstein poster; no competitor-equivalent guerrilla campaign against
Apple/Google/Samsung/Snap camera wearables in any of the 83 cycles.

Attention Sphere 83rd no-match as podcast: quoted search returned this
repo's own GitHub commit pages (5 commit URLs with Full-URL mappings, 1
mapping absent; rejected as circular per established discipline) and the
Andrew Bosworth "Possible" iHeart episode (2025-03-26, crawled 287d;
wearables-positive Meta-CTO interview unrelated to any podcast named
Attention Sphere; in corpus). Identity strand unchanged from #596;
task-spec name remains misidentified; Tracked Sources 82->83 cycles through
Sep 17 2026.

Press surfaces: 6 results observed; ALL previously-logged URL keys, ALL
verified in corpus pre-commit (livemint voice-recordings-by-default piece
crawled 334d; techcrunch Mar 2026 contractor-review lawsuit piece crawled
2d; bbc.bm host-mirror of in-corpus Reuters Dec 2025 piece crawled 281d;
livemint trends piece crawled 189d; forbesindia privacy-scandal roundup
crawled 162d; androidpolice class-action piece crawled 15d, 195 days old,
in corpus via test_android_police / #606 / #776, NOT new). Recency frontier
TIED at Sep 9 (thirty-fourth consecutive tie after #636 through #796); the
petapixel.com Sep 9 piece remains the newest date-verified in-corpus
Meta-glasses press item; no advance.

Standing rule (Aug 28 2026): tone NOT_SCORED, p_value/cohens_d
NOT_CALCULATED, is_significant False; Type E monitoring-only, no mechanism
block in profiles/. No analysis.json update warranted. 21 external URL keys
observed (7 GF + 7 EHE + 1 iHeart Boz + 6 press); 18 previously-logged
verified in corpus pre-commit, 3 new GF distribution-surface keys logged
this run. No browser.open; snippet-bounded method.
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


class TestNovelty801:
    """Iteration 801 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_801_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_801*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_801_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_801 files, no #801 in git log); this test
        # pins that no duplicate #801 main commit ever appears.
        #
        # Hardened vs the #756/#759 naive "Type E #NNN:" prefix match, which
        # also matched the followup subjects ("Type E #NNN followup:",
        # "Type E #NNN: push-blocked status") and broke once the push-blocked
        # note landed (#760 rotation-guard hardening note). The
        # ": podcast sentiment" qualifier pins only the main commit.
        log = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [
            l
            for l in log
            if re.match(r"^[0-9a-f]{40} Type E #801: podcast sentiment", l)
        ]
        assert len(mains) == 1, mains
        anchor = TestRotationCycleGuard801.ANCHORED_SHA
        assert mains[0].startswith(anchor + " "), (anchor, mains)


class TestRotationCycleGuard801:
    """Rotation: 800-804 window, #800 (D) anchors, #801 is the E leg.

    Deselected pre-commit per the #565 followup convention (the #801 main
    commit does not exist yet); patched green in the anchor followup.
    """

    ANCHORED_SHA = "45cb8ea218c9f1bade9b49ecc6c117d3ca215b36"  # main commit this run, per #565

    EXPECTED_ORDER = [("E", "801"), ("D", "800"), ("C", "799"), ("B", "798"), ("A", "797")]
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

    def test_window_800_804_second_leg_e(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type E #801: podcast sentiment")
        assert self.ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
            "PATCH_ME_IN_FOLLOWUP_PER_565",
        ), mains
        assert mains and mains[0].startswith(self.ANCHORED_SHA + " "), mains


class TestGF83rdCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #801")[-1]

    def test_500_stands_newest_seventeen_hours_after_796(self):
        section = self._section()
        assert "Episode 500 stands as newest seventeen hours after #796" in section

    def test_official_site_corroboration_carried_from_796(self):
        section = self._section()
        assert "Official-site corroboration carried from #796" in section
        assert "guiltyfeminist.com/new-normal/" in section
        assert "crawled 18h at #796" in section

    def test_no_fresh_browser_open_snippet_bounded(self):
        section = self._section()
        assert "no fresh browser.open this run" in section
        assert "snippet-bounded method per #796" in section

    def test_uk_podcasts_now_760_episodes_latest_sep_16_unverified(self):
        section = self._section()
        assert 'uk-podcasts.co.uk (crawled 4h) now shows 760 episodes / "Latest episode: 2026-09-16"' in section
        assert "was 758 / 2026-09-12 at #796" in section
        assert "UNVERIFIED single-directory signal" in section
        assert "no drop is asserted per #503/iteration-492 discipline" in section

    def test_listen_notes_still_498_crawled_10d(self):
        section = self._section()
        assert "Listen Notes still lags on 498 (756 episodes; Last Crawl 10 days ago)" in section

    def test_directory_signals_not_observed_bounded_absence(self):
        section = self._section()
        assert "podparadise.com / goloudnow.com not observed this run (bounded absence" in section
        assert "signals carried from #796" in section

    def test_no_episode_501_next_release_plausibly_near_sep_21(self):
        section = self._section()
        assert "No episode 501 detected anywhere this run" in section
        assert "weekly cadence puts the next numbered release plausibly near Sep 21" in section

    def test_live_show_listings_bounded_absence(self):
        section = self._section()
        assert "chortle.co.uk / edfringe.com / stagewhispers.com.au live-show listings not observed this run" in section
        assert "bounded absence" in section

    def test_triggernometry_bounded_absence(self):
        section = self._section()
        assert "The YouTube Triggernometry clip oVPri0Wr6F0 did not surface this run (bounded absence, not a claim; in corpus since #771)" in section

    def test_three_new_url_keys_youtube_479(self):
        section = self._section()
        assert "https://www.youtube.com/watch?v=DTtg_5J9Fqc" in section
        assert "GF 479 Welsh Election Special part two" in section
        assert "recorded 12 April 2026 New Theatre Cardiff, released 20 April" in section

    def test_three_new_url_keys_youtube_473(self):
        section = self._section()
        assert "https://www.youtube.com/watch?v=_u8jWa1dqBc" in section
        assert "GF 473 ROAD TO GILEAD: Fascism" in section
        assert "recorded 20 Feb 2026 Museum of Comedy, released 9 Mar" in section

    def test_three_new_url_keys_iheart_page(self):
        section = self._section()
        assert "https://www.iheart.com/podcast/263-the-guilty-feminist-27628788/" in section
        assert "shown episodes 458 Annie Lennox in Conversation at the V&A (Nov 2025)" in section
        assert "Emergency Episode Gaza nurse Alaa Al-ghoul (Nov 2025)" in section

    def test_new_keys_zero_meta_wearables_content(self):
        section = self._section()
        assert "ZERO Meta/wearables content (snippet-bounded)" in section

    def test_gf_set_seven_keys_four_known_three_new(self):
        section = self._section()
        assert "GF-set: 7 URL keys observed this run (4 previously-logged verified in corpus pre-commit + 3 new logged this run)" in section


class TestEHEHold83rdCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #801")[-1]

    def test_forty_three_day_hold(self):
        section = self._section()
        assert "43-day hold continues (Aug 10 -> Sep 17)" in section

    def test_seven_resurfaces_all_in_corpus(self):
        section = self._section()
        assert "7 re-surfaces observed, ALL previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "(52 days, crawled 52d)" in section
        assert "(62 days, crawled 3d" in section
        assert "(56 days, crawled 15h)" in section
        assert "(49 days, crawled 25d" in section
        assert "(64 days, crawled 18h; same content)" in section
        assert "(lenticular piece re-surfaced, crawled 3d" in section

    def test_toi_piece_resurfaced_fresh_crawl_2d_same_content(self):
        section = self._section()
        assert "in corpus via #721, crawled 2d; fresh crawl, same content as #736-#796" in section
        assert "same canonical key via proxy wrapper, no new key" in section

    def test_no_new_primary_motif_83_cycles(self):
        section = self._section()
        assert "No new primary campaign motif" in section
        assert "Last campaign phase remains the circa Aug 10 Epstein poster" in section
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 83 cycles" in section


class TestAttentionSphere83rdNoMatch:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #801")[-1]

    def test_eighty_third_no_match(self):
        section = self._section()
        assert "(eighty-third no-match)" in section

    def test_github_commit_pages_rejected_circular(self):
        section = self._section()
        assert "5 commit URLs with Full-URL mappings, 1 mapping absent" in section
        assert "rejected as circular per established discipline" in section

    def test_boz_possible_episode_unrelated_in_corpus(self):
        section = self._section()
        assert 'Andrew Bosworth "Possible" iHeart episode (2025-03-26, crawled 287d' in section
        assert "unrelated to any podcast named Attention Sphere; in corpus" in section

    def test_tracked_sources_82_to_83(self):
        section = self._section()
        assert "Identity strand unchanged from #596" in section
        assert "Tracked Sources 82->83 cycles through Sep 17 2026" in section


class TestPressSurfaces801:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #801")[-1]

    def test_six_results_all_known_keys_in_corpus(self):
        section = self._section()
        assert "SIX results observed; ALL previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses-privacy-concerns-after-workers-reviewed-nudity-sex-and-other-footage/" in section
        assert "are-mark-zuckerbergs-meta-ai-smart-glasses-watching-you-privacy-row-fuels-online-fears-puts-spotlight-on-dpdp-act-11772781893202.html" in section
        assert "meta-ray-ban-smart-glasses-could-store-voice-recordings-by-default-what-it-means-for-users/amp-11746118684276.html" in section
        assert "https://bbc.bm/ray-ban-meta-glasses-take-off-but-face-privacy-and-competition-test" in section
        assert "(voice-recordings-by-default policy piece, crawled 334d" in section
        assert "(host-mirror of the in-corpus Reuters Dec 2025 piece, crawled 281d" in section

    def test_androidpolice_in_corpus_not_new(self):
        section = self._section()
        assert "https://www.androidpolice.com/meta-ai-glasses-privacy-concern/" in section
        assert "in corpus via test_android_police / #606 / #776, NOT new" in section

    def test_frontier_tied_thirty_fourth(self):
        section = self._section()
        assert "TIED at Sep 9 (thirty-fourth consecutive tie after #636 through #796)" in section
        assert "the petapixel.com Sep 9 piece remains the newest date-verified in-corpus Meta-glasses press item" in section
        assert "no advance" in section


class TestStandingRules801:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #801")[-1]

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
        assert "with since=2026-09-17" in section
        assert "no since filter" in section

    def test_url_key_accounting_21_observed_18_known_3_new(self):
        section = self._section()
        assert "21 external URL keys observed (7 GF + 7 EHE + 1 iHeart Boz + 6 press)" in section
        assert "18 previously-logged verified in corpus pre-commit, 3 new GF distribution-surface keys logged this run" in section

    def test_circular_github_urls_rejected(self):
        section = self._section()
        assert "rejected as circular per established discipline, not ingested" in section

    def test_ascii_no_em_dashes(self):
        assert "\u2014" not in self._section()
        assert "\u2013" not in self._section()

    def test_test_file_ref(self):
        section = self._section()
        assert "tests/test_type_e_801_podcast_sentiment_83rd_verification_sep17_4am.py" in section


class TestDocSync801:
    def test_readme_row_801(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_row_801_in_table(self):
        doc = _read(README_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_architecture_row_801(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_801_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog801:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #801 entry sits at the end of the file, not the top.
        return "\n".join(lines[-110:])

    def test_log_entry_present(self):
        # "#801 Type E:" is the entry header; a bare "#801" would
        # false-positive on #800's rotation line ("E (#801) -> ...").
        assert "#801 Type E:" in self._tail()

    def test_log_cycle_and_hour(self):
        assert "eighty-third" in self._tail()
        assert "04:00 PDT" in self._tail()


class TestDateGrounding801:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_17_2026_is_thursday(self):
        assert self._weekday("2026-09-17") == "Thursday"
