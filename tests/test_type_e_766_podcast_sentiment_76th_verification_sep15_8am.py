"""Type E #766: podcast sentiment 76th verification cycle (Sep 15 2026, 08:00 PDT).

Guilty Feminist: episode 500 stands as newest five hours after #761.
au.radio.net (Last Updated 15 hours ago, crawled 4h) still lists 759
episodes with episode 500 on top; goloudnow.com (crawled 10h)
corroborates. ZERO Meta/AI/wearables/privacy/surveillance content in
title/description (snippet-bounded); the episode topic is the Palestinian
Circus, not tech. No first-hand page read this run; no tone score
asserted. uk-podcasts.co.uk (crawled 4h) still shows 758 episodes /
"Latest episode: 2026-09-12", lagging one behind the release; still an
UNVERIFIED single-directory signal; no drop asserted per #503/
iteration-492 discipline. Listen Notes (crawled 20d) still lags on 498
(756 episodes). podscan.fm signal carried from #726: the 499 transcript
was the newest NUMBERED release; no new podscan result this run, and per
#503 discipline that bounded absence is not a claim. No episode 501
detected anywhere this run; weekly cadence puts the next numbered release
plausibly near Sep 21. Chortle (crawled 2d) still lists the Sun 13 Sep
2026 Kings Place live show, now past; a recorded live performance, not an
episode release. ZERO new URL keys this run: all 7 observed GF directory
URLs verified in corpus pre-commit via git grep.

EHE 39-day hold continues (Aug 10 -> Sep 15, inclusive count): 7
re-surfaces, ALL previously-logged URL keys, ALL verified in corpus
pre-commit (thetimes Epstein 50d/crawled 50d; engadget WWW-uppercase
60d/crawled 17d, same page per #676 convention; petapixel lenticular
54d/crawled 21d; latestly fact-check 47d/crawled 23d; hyperallergic http
key 62d/crawled 2h; fstoppers lenticular re-surfaced crawled 1d) plus the
Times of India 133146816 UK-venue-bans editorial piece re-surfaced (in
corpus via #721, crawled 7h; same content as
#736/#741/#746/#751/#756/#761; same canonical key via proxy wrapper, no
new key). No new primary campaign motif; last phase remains the circa Aug
10 Epstein poster; no competitor-equivalent guerrilla campaign against
Apple/Google/Samsung/Snap camera wearables in any of the 76 cycles.

Attention Sphere 76th no-match as podcast: quoted-search top results were
this repo's own GitHub commit pages (5 commit URLs, rejected as circular
per established discipline), plus the Andrew Bosworth "Possible" iHeart
episode (2025-03-26, crawled 285d; wearables-positive Meta-CTO interview
unrelated to any podcast named Attention Sphere; in corpus). Identity
strand unchanged from #596; task-spec name remains misidentified; Tracked
Sources table 75->76 cycles through Sep 15 2026.

Press surfaces: 6 results observed; ALL previously-logged URL keys, ALL
verified in corpus pre-commit (livemint voice-recordings-by-default piece
crawled 332d; techcrunch Mar 2026 contractor-review lawsuit piece crawled
42d; bbc.bm host-mirror crawled 279d; livemint trends piece crawled 187d;
reuters Dec 2025 take-off piece 279d/crawled 279d; forbesindia
privacy-scandal roundup crawled 160d). Recency frontier TIED at Sep 9
(twenty-seventh consecutive tie after #636 through #761); the
petapixel.com Sep 9 piece remains the newest date-verified in-corpus
Meta-glasses press item; no advance. GF episode 500 is a podcast
milestone release carrying zero Meta/wearables content, not a
Meta-glasses press item, so the frontier is unaffected.

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


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


class TestNovelty766:
    """Iteration 766 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_766_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_766*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_766_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_766 files, no #766 in git log); this test
        # pins that no duplicate #766 main commit ever appears.
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
            if re.match(r"^[0-9a-f]{40} Type E #766: podcast sentiment", l)
        ]
        assert len(mains) == 1, "expected exactly one #766 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard766.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestRotationCycleGuard766:
    """Rotation: distinct-mains window test, #726-style.

    Robust to the #678 history artifact and the #565 followup convention:
    first occurrence of each distinct iteration number, newest first. #766
    opens the 766-770 window, opening E->A->B->C->D.
    """

    ANCHORED_SHA = "aa8dcb5db867036f021631d436cdce1dc2d651c6"  # main commit this run, per #565

    @staticmethod
    def _mains():
        # First occurrence of each distinct iteration number, newest first.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        seen = set()
        mains = []
        for s in out:
            m = re.match(r"^Type [A-E] #(\d+):", s)
            if m and m.group(1) not in seen:
                seen.add(m.group(1))
                mains.append(s)
        return mains

    def test_window_762_766_opens_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("E", "766"),
            ("D", "765"),
            ("C", "764"),
            ("B", "763"),
            ("A", "762"),
        ], "rotation window 762-766 wrong: %r" % (observed,)

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
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )


class TestGF76thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #766")[-1]

    def _table(self):
        return _read("podcast-sentiment.md").split("## Tracked Sources")[1].split("### Secondary")[0]

    def test_500_stands_newest_five_hours_after_761(self):
        section = self._section()
        assert "Episode 500 stands as newest five hours after #761" in section

    def test_au_radio_net_759_episodes_two_directory_corroboration(self):
        section = self._section()
        assert "au.radio.net (Last Updated 15 hours ago, crawled 4h) still lists 759 episodes" in section
        assert "500. Five Hundredth Episode with Kate Cheka and the Palestinian Circus" in section
        assert "14/09/2026, 58 mins" in section
        assert "recorded 22 August 2026 at Gilded Balloon at the Museum" in section
        assert "goloudnow.com (crawled 10h) corroborates" in section

    def test_zero_meta_wearables_content_snippet_bounded(self):
        section = self._section()
        assert "Title/description carry ZERO Meta/AI/wearables/privacy/surveillance content (snippet-bounded)" in section
        assert "the episode topic is the Palestinian Circus, not tech" in section

    def test_no_first_hand_read_no_tone_score(self):
        section = self._section()
        assert "No first-hand page read this run" in section
        assert "snippet-bounded directory corroboration only" in section
        assert "no tone score asserted on the episode" in section

    def test_uk_podcasts_still_unverified_single_directory_signal(self):
        section = self._section()
        assert "uk-podcasts.co.uk (crawled 4h) still shows 758 episodes" in section
        assert "UNVERIFIED single-directory signal" in section
        assert "no drop is asserted per #503/iteration-492 discipline" in section

    def test_listen_notes_still_498_crawled_20d(self):
        section = self._section()
        assert "Listen Notes (crawled 20d) still lags on 498 (756 episodes)" in section

    def test_podscan_signal_carried_from_726(self):
        section = self._section()
        assert "podscan.fm signal carried from #726" in section
        assert "the 499 transcript was the newest NUMBERED release" in section
        assert "per #503 discipline that bounded absence is not a claim" in section

    def test_no_episode_501_next_release_plausibly_near_sep_21(self):
        section = self._section()
        assert "No episode 501 detected anywhere this run" in section
        assert "weekly cadence puts the next numbered release plausibly near Sep 21" in section

    def test_chortle_live_show_now_past(self):
        section = self._section()
        assert "Chortle (crawled 2d) still lists the Sun 13 Sep 2026 Kings Place live show" in section
        assert "now past" in section
        assert "a recorded live performance, not an episode release" in section

    def test_zero_new_url_keys_this_run(self):
        section = self._section()
        assert "ZERO new URL keys this run: all 7 observed GF directory URLs verified in corpus pre-commit via git grep" in section

    def test_table_gf_row_501_watch_8am(self):
        assert "500 numbered episodes (Sep 15 2026)" in self._table()
        assert "Numbered-episode 501 not yet indexed as of Sep 15 2026 08:00 PDT" in self._table()


class TestEHE39DayHold76thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #766")[-1]

    def test_thirty_nine_day_hold(self):
        section = self._section()
        assert "39-day hold continues (Aug 10 -> Sep 15, inclusive count)" in section

    def test_seven_resurfaces_all_in_corpus(self):
        section = self._section()
        assert "7 re-surfaces observed: 6 previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "meta-ai-glasses-spoof-advert-jeffrey-epstein-slx3wttm5 (50 days, crawled 50d)" in section
        assert "WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/ (60 days, crawled 17d" in section
        assert "kylie-jenners-meta-smart-glasses-parodied-in-guerrilla-lenticular-ad/ (54 days, crawled 21d)" in section
        assert "7538349.html (47 days, crawled 23d; in corpus since #383/#445/#465)" in section
        assert "http://hyperallergic.com/guerrilla-london-bus-ads-mock-kylie-jenners-meta-glasses-campaign/ (62 days, crawled 2h" in section
        assert "fstoppers.com/news/kylie-jenner-ad-hides-disturbing-secret-just-have-stand-right-spot-903612" in section
        assert "lenticular piece re-surfaced, crawled 1d" in section

    def test_toi_piece_resurfaced_same_key_crawled_7h(self):
        section = self._section()
        assert "Times of India 133146816 UK-venue-bans editorial piece re-surfaced (in corpus via #721, crawled 7h" in section
        assert "same canonical key via proxy wrapper, no new key" in section

    def test_no_new_primary_motif_76_cycles(self):
        section = self._section()
        assert "Last campaign phase remains the circa Aug 10 Epstein poster" in section
        assert "in any of the 76 cycles" in section


class TestAttentionSphere76thNoMatch:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #766")[-1]

    def test_seventy_sixth_no_match(self):
        section = self._section()
        assert "seventy-sixth no-match" in section

    def test_github_commit_pages_rejected_circular(self):
        section = self._section()
        assert "5 commit URLs, rejected as circular per established discipline" in section
        assert "https://github.com/rayhe/mediascope/commit/3d16eacfc03d35bad9ade4a15403fbcea2fb293c (circular, rejected)" in section
        assert "https://github.com/rayhe/mediascope/commit/2c4e21e39a3bb17e74c8afc0bd5b7ad25bda29b4 (circular, rejected)" in section

    def test_boz_possible_episode_unrelated_in_corpus(self):
        section = self._section()
        assert "Andrew Bosworth \"Possible\" iHeart episode (2025-03-26, crawled 285d" in section
        assert "unrelated to any podcast named Attention Sphere" in section
        assert "in corpus" in section

    def test_table_attention_sphere_76_cycles(self):
        table = _read("podcast-sentiment.md").split("## Tracked Sources")[1].split("### Secondary")[0]
        assert "76 verification cycles through Sep 15 2026, all no-match as a podcast" in table


class TestPressSurfaces766:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #766")[-1]

    def test_six_results_all_known_keys_in_corpus(self):
        section = self._section()
        assert "SIX results observed; ALL previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses-privacy-concerns-after-workers-reviewed-nudity-sex-and-other-footage/" in section
        assert "are-mark-zuckerbergs-meta-ai-smart-glasses-watching-you-privacy-row-fuels-online-fears-puts-spotlight-on-dpdp-act-11772781893202.html" in section
        assert "meta-ray-ban-smart-glasses-could-store-voice-recordings-by-default-what-it-means-for-users/amp-11746118684276.html" in section
        assert "https://www.forbesindia.com/article/ai-tracker/why-metas-ray-ban-smart-glasses-are-causing-a-privacy-scandal/2991937/1" in section
        assert "crawled 42d" in section
        assert "crawled 332d" in section

    def test_frontier_tied_twenty_seventh(self):
        section = self._section()
        assert "TIED at Sep 9 (twenty-seventh consecutive tie after #636 through #761)" in section
        assert "no advance" in section
        assert "GF episode 500 is a podcast milestone release carrying zero Meta/wearables content, not a Meta-glasses press item" in section


class TestStandingRules766:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #766")[-1]

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
        assert "with since=2026-09-15" in section
        assert "with since=2026-09-14" in section

    def test_zero_new_url_keys_git_grep_verified(self):
        section = self._section()
        assert "Pre-commit repo-wide git grep" in section
        assert "ZERO new URL keys this run" in section

    def test_no_browser_open_snippet_bounded(self):
        section = self._section()
        assert "No browser.open verification attempt this run" in section
        assert "snippet-bounded two-directory corroboration" in section

    def test_ascii_no_em_dashes(self):
        assert "\u2014" not in self._section()
        assert "\u2013" not in self._section()

    def test_test_file_ref(self):
        section = self._section()
        assert "tests/test_type_e_766_podcast_sentiment_76th_verification_sep15_8am.py" in section
