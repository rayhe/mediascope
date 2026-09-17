"""Type E #796: podcast sentiment 82nd verification cycle (Sep 16 2026, 23:00 PDT).

Guilty Feminist: episode 500 stands as newest fourteen hours after #791.
Official site guiltyfeminist.com/new-normal/ (crawled 18h) carries "Latest
episode 500. Five Hundredth Episode with Kate Cheka and the Palestinian
Circus, Published: 14 September 2026" - first-party corroboration, second
official-site confirmation in a row (#786 was the first). goloudnow.com
(crawled 8h) now lists a changed visible slate vs #786/#791: the "In
Conversation with Indhu Rubasingham" unnumbered special (first logged #721;
recorded 9 September 2026 at the National Theatre, released 12 September)
re-surfaced on top alongside the 58-min "14 September Finished" entry
matching the 500 release. ZERO Meta/AI/wearables/privacy/surveillance
content in the listed titles/descriptions (snippet-bounded); the special's
topic is theatre, not tech. podparadise.com (crawled 14h) still lists 757
episodes with newest NUMBERED release 499 (Where You End and I Begin with
Lindsey Mendick, released 7 September 2026), unchanged from #791 (still
lags the official 500 release; in corpus via #791). uk-podcasts.co.uk
(crawled 13h) still shows 758 episodes / "Latest episode: 2026-09-12",
lagging one behind the release; still an UNVERIFIED single-directory
signal; no drop asserted per #503/iteration-492 discipline. Listen Notes
(crawled 21d) still lags on 498 (756 episodes). podscan.fm signal carried
from #726: the 499 transcript was the newest NUMBERED release; no new
podscan result this run. No episode 501 detected anywhere this run; weekly
cadence puts the next numbered release plausibly near Sep 21. The chortle
edinburgh_fringe_2026 listing (crawled 12h), the edfringe.com live-show
listing (crawled 18h), and the stagewhispers.com.au live-show review
(crawled 103d) all re-surfaced; live-show listings, not episodes; all
pre-existing corpus keys. The YouTube Triggernometry clip oVPri0Wr6F0 did
not surface this run (bounded absence, not a claim; in corpus since #771).
ZERO new URL keys this run: all 8 GF-set URL keys verified in corpus
pre-commit (targeted git grep, each >=1 hit).

EHE 42-day hold continues (Aug 10 -> Sep 16): 7 re-surfaces, ALL
previously-logged URL keys, ALL verified in corpus pre-commit (thetimes
52d/crawled 52d; engadget WWW-uppercase 62d/crawled 18d, same page per
#676 convention; petapixel 56d/crawled 10h; latestly 49d/crawled 25d;
hyperallergic http key 64d/crawled 13h, same content; fstoppers lenticular
re-surfaced crawled 3d) plus the Times of India 133146816 UK-venue-bans
editorial piece re-surfaced (in corpus via #721, crawled 1d; fresh crawl,
same content as #736-#791; same canonical key via proxy wrapper, no new
key). No new primary campaign motif; last phase remains the circa Aug 10
Epstein poster; no competitor-equivalent guerrilla campaign against
Apple/Google/Samsung/Snap camera wearables in any of the 82 cycles.

Attention Sphere 82nd no-match as podcast: quoted-search top results were
this repo's own GitHub commit pages (5 commit URLs, rejected as circular
per established discipline), plus the Andrew Bosworth "Possible" iHeart
episode (2025-03-26, crawled 287d; wearables-positive Meta-CTO interview
unrelated to any podcast named Attention Sphere; in corpus). Identity strand
unchanged from #596; task-spec name remains misidentified; Tracked Sources
81->82 cycles through Sep 16 2026.

Press surfaces: 6 results observed; ALL previously-logged URL keys, ALL
verified in corpus pre-commit (livemint voice-recordings-by-default piece
crawled 334d; techcrunch Mar 2026 contractor-review lawsuit piece crawled
2d; bbc.bm host-mirror crawled 281d; livemint trends piece crawled 189d;
forbesindia privacy-scandal roundup crawled 162d; epic.org EPIC-to-FTC FRT
letter Feb 2026 crawled 56d, in corpus, NOT new). Recency frontier TIED at
Sep 9 (thirty-third consecutive tie after #636 through #791); the
petapixel.com Sep 9 piece remains the newest date-verified in-corpus
Meta-glasses press item; no advance. GF episode 500 and the Indhu
Rubasingham unnumbered special carry zero Meta/wearables content
(snippet-bounded), so the frontier is unaffected. The epic.org return is a
Feb 2026 letter, not an advance.

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


class TestNovelty796:
    """Iteration 796 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_796_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_796*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_796_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_796 files, no #796 in git log); this test
        # pins that no duplicate #796 main commit ever appears.
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
            if re.match(r"^[0-9a-f]{40} Type E #796: podcast sentiment", l)
        ]
        assert len(mains) == 1, mains
        anchor = TestRotationCycleGuard796.ANCHORED_SHA
        assert mains[0].startswith(anchor + " "), (anchor, mains)


class TestRotationCycleGuard796:
    """Rotation: 795-799 window, #795 (D) anchors, #796 is the E leg.

    Deselected pre-commit per the #565 followup convention (the #796 main
    commit does not exist yet); patched green in the anchor followup.
    """

    ANCHORED_SHA = "90bad2df4923069e3446a8eda57c7f54175df3fc"  # main commit this run, per #565

    EXPECTED_ORDER = [("E", "796"), ("D", "795"), ("C", "794"), ("B", "793"), ("A", "792")]
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

    def test_window_795_799_second_leg_e(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type E #796: podcast sentiment")
        assert self.ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
            "PATCH_ME_IN_FOLLOWUP_PER_565",
        ), mains
        assert mains and mains[0].startswith(self.ANCHORED_SHA + " "), mains


class TestGF82ndCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #796")[-1]

    def test_500_stands_newest_fourteen_hours_after_791(self):
        section = self._section()
        assert "Episode 500 stands as newest fourteen hours after #791" in section

    def test_official_site_second_confirmation_crawled_18h(self):
        section = self._section()
        assert "Official site guiltyfeminist.com/new-normal/ (crawled 18h) still carries" in section
        assert "second official-site confirmation in a row (#786 was the first)" in section

    def test_goloudnow_changed_slate_crawled_8h(self):
        section = self._section()
        assert "goloudnow.com (crawled 8h) now lists a changed visible slate vs #786/#791" in section

    def test_indhu_rubasingham_resurfaced_first_logged_721(self):
        section = self._section()
        assert "the \"In Conversation with Indhu Rubasingham\" unnumbered special (first logged #721" in section
        assert "recorded 9 September 2026 at the National Theatre, released 12 September" in section
        assert "re-surfaced on top alongside the 58-min \"14 September Finished\" entry matching the 500 release" in section

    def test_zero_meta_wearables_content_special_theatre_not_tech(self):
        section = self._section()
        assert "ZERO Meta/AI/wearables/privacy/surveillance content in the listed titles/descriptions (snippet-bounded)" in section
        assert "the special's topic is theatre, not tech" in section

    def test_podparadise_still_499_crawled_14h_unchanged(self):
        section = self._section()
        assert "podparadise.com (crawled 14h) still lists 757 episodes" in section
        assert "newest NUMBERED release 499 (Where You End and I Begin with Lindsey Mendick, released 7 September 2026), unchanged from #791" in section
        assert "still lags the official 500 release; in corpus via #791" in section

    def test_uk_podcasts_still_unverified_single_directory_signal(self):
        section = self._section()
        assert 'uk-podcasts.co.uk (crawled 13h) still shows 758 episodes / "Latest episode: 2026-09-12"' in section
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

    def test_live_show_listings_resurfaced_not_episodes(self):
        section = self._section()
        assert "The chortle.co.uk edinburgh_fringe_2026 GF show listing (crawled 12h)" in section
        assert "the edfringe.com live-show directory listing (crawled 18h)" in section
        assert "the stagewhispers.com.au live-show review (crawled 103d) all re-surfaced" in section
        assert "live-show listings, not episodes; all pre-existing corpus keys" in section

    def test_triggernometry_bounded_absence_not_ingested(self):
        section = self._section()
        assert "The YouTube Triggernometry clip oVPri0Wr6F0 did not surface this run (bounded absence, not a claim; in corpus since #771)" in section

    def test_zero_new_url_keys_eight_gf_set_in_corpus(self):
        section = self._section()
        assert "ZERO new URL keys this run: all 8 GF-set URL keys verified in corpus pre-commit (targeted git grep, each >=1 hit)" in section

    def test_no_drop_asserted_discipline(self):
        section = self._section()
        assert "no drop is asserted per #503/iteration-492 discipline" in section


class TestEHEHold82ndCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #796")[-1]

    def test_forty_two_day_hold(self):
        section = self._section()
        assert "42-day hold continues (Aug 10 -> Sep 16)" in section

    def test_seven_resurfaces_all_in_corpus(self):
        section = self._section()
        assert "7 re-surfaces observed, ALL previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "(52 days, crawled 52d)" in section
        assert "(62 days, crawled 18d" in section
        assert "(56 days, crawled 10h)" in section
        assert "(49 days, crawled 25d" in section
        assert "(64 days, crawled 13h; same content)" in section
        assert "(lenticular piece re-surfaced, crawled 3d" in section

    def test_toi_piece_resurfaced_fresh_crawl_1d_same_content(self):
        section = self._section()
        assert "(in corpus via #721, crawled 1d; fresh crawl, same content as #736-#791" in section
        assert "same canonical key via proxy wrapper, no new key" in section

    def test_no_new_primary_motif_82_cycles(self):
        section = self._section()
        assert "No new primary campaign motif" in section
        assert "Last campaign phase remains the circa Aug 10 Epstein poster" in section
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 82 cycles" in section


class TestAttentionSphere82ndNoMatch:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #796")[-1]

    def test_eighty_second_no_match(self):
        section = self._section()
        assert "(eighty-second no-match)" in section

    def test_github_commit_pages_rejected_circular(self):
        section = self._section()
        assert "5 commit URLs, rejected as circular per established discipline" in section

    def test_boz_possible_episode_unrelated_in_corpus(self):
        section = self._section()
        assert "Andrew Bosworth \"Possible\" iHeart episode (2025-03-26, crawled 287d" in section
        assert "unrelated to any podcast named Attention Sphere; in corpus" in section

    def test_tracked_sources_81_to_82(self):
        section = self._section()
        assert "Identity strand unchanged from #596" in section
        assert "Tracked Sources 81->82 cycles through Sep 16 2026" in section


class TestPressSurfaces796:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #796")[-1]

    def test_six_results_all_known_keys_in_corpus(self):
        section = self._section()
        assert "SIX results observed; ALL previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses-privacy-concerns-after-workers-reviewed-nudity-sex-and-other-footage/" in section
        assert "are-mark-zuckerbergs-meta-ai-smart-glasses-watching-you-privacy-row-fuels-online-fears-puts-spotlight-on-dpdp-act-11772781893202.html" in section
        assert "meta-ray-ban-smart-glasses-could-store-voice-recordings-by-default-what-it-means-for-users/amp-11746118684276.html" in section
        assert "https://bbc.bm/ray-ban-meta-glasses-take-off-but-face-privacy-and-competition-test" in section
        assert "(voice-recordings-by-default policy piece, crawled 334d" in section
        assert "(host-mirror of the in-corpus Reuters Dec 2025 piece, crawled 281d" in section

    def test_epic_url_in_corpus_not_new(self):
        section = self._section()
        assert "https://epic.org/wp-content/uploads/2026/02/letter-from-EPIC-to-FTC-re-Meta-FRT-glasses.pdf?_bhlid=45e2ef2bbb9d2ce438306e818f840b46fb5da476" in section
        assert "(EPIC-to-FTC letter re Meta FRT glasses, Feb 2026; crawled 56d; in corpus, NOT new)" in section

    def test_frontier_tied_thirty_third(self):
        section = self._section()
        assert "TIED at Sep 9 (thirty-third consecutive tie after #636 through #791)" in section
        assert "no advance" in section
        assert "not Meta-glasses press items, so the frontier is unaffected" in section
        assert "The epic.org return is a Feb 2026 letter, not an advance" in section


class TestStandingRules796:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #796")[-1]

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

    def test_zero_new_url_keys_all_22_in_corpus(self):
        section = self._section()
        assert "ZERO new URL keys this run; all 22 observed external URL keys verified in corpus pre-commit" in section
        assert "(8 GF-set + 7 EHE-set + 1 iHeart + 6 press-set; git grep -l each >=1 hit)" in section

    def test_five_circular_github_urls_rejected(self):
        section = self._section()
        assert "5 github.com own-repo commit URLs rejected as circular per established discipline, not ingested" in section

    def test_no_browser_open_snippet_bounded(self):
        section = self._section()
        assert "No browser.open verification attempt this run" in section
        assert "snippet-bounded directory corroboration for episode 500" in section
        assert "official site crawled 18h" in section

    def test_ascii_no_em_dashes(self):
        assert "\u2014" not in self._section()
        assert "\u2013" not in self._section()

    def test_test_file_ref(self):
        section = self._section()
        assert "tests/test_type_e_796_podcast_sentiment_82nd_verification_sep16_11pm.py" in section


class TestDocSync796:
    def test_readme_row_796(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_row_796_in_table(self):
        doc = _read(README_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_architecture_row_796(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_796_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog796:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #796 entry sits at the end of the file, not the top.
        return "\n".join(lines[-110:])

    def test_log_entry_present(self):
        # "#796 Type E:" is the entry header; a bare "#796" would
        # false-positive on #795's rotation line ("E (#796) -> ...").
        assert "#796 Type E:" in self._tail()

    def test_log_cycle_and_hour(self):
        assert "eighty-second" in self._tail()
        assert "23:00 PDT" in self._tail()


class TestDateGrounding796:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_16_2026_is_wednesday(self):
        assert self._weekday("2026-09-16") == "Wednesday"
