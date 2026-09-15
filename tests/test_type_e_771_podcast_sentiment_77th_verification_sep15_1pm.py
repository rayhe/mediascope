"""Type E #771: podcast sentiment 77th verification cycle (Sep 15 2026, 13:00 PDT).

Guilty Feminist: episode 500 stands as newest ten hours after #766.
goloudnow.com (crawled 4h) corroborates; au.radio.net did not surface this
run, so goloudnow is the sole fresh directory corroboration. ZERO
Meta/AI/wearables/privacy/surveillance content in title/description
(snippet-bounded); the episode topic is the Palestinian Circus, not tech.
No first-hand page read this run; no tone score asserted.
uk-podcasts.co.uk (crawled 4h) still shows 758 episodes / "Latest episode:
2026-09-12", lagging one behind the release; still an UNVERIFIED
single-directory signal; no drop asserted per #503/iteration-492
discipline. Listen Notes (crawled 20d) still lags on 498 (756 episodes).
podscan.fm signal carried from #726: the 499 transcript was the newest
NUMBERED release; no new podscan result this run, and per #503 discipline
that bounded absence is not a claim. No episode 501 detected anywhere this
run; weekly cadence puts the next numbered release plausibly near Sep 21.
Chortle's Sun 13 Sep 2026 Kings Place live show is now past; a recorded
live performance, not an episode release. ONE new-to-corpus URL key
observed (YouTube Triggernometry clip oVPri0Wr6F0, crawled 6h), verified
new pre-commit via repo-wide git grep, NOT ingested (not a Guilty Feminist
episode; zero tech content; out-of-scope for the three tracking strands;
snippet-bounded; surfaced-not-new handling per #460/#506). 7 of the 8
GF-set URLs verified in corpus pre-commit.

EHE 39-day hold continues (Aug 10 -> Sep 15, same calendar day as #766): 7
re-surfaces, ALL previously-logged URL keys, ALL verified in corpus
pre-commit (thetimes 51d/crawled 51d; engadget WWW-uppercase 60d/crawled
17d, same page per #676 convention; petapixel 54d/crawled 21d; latestly
47d/crawled 23d; hyperallergic http key 62d/crawled 3h; fstoppers
lenticular re-surfaced crawled 1d) plus the Times of India 133146816
UK-venue-bans editorial piece re-surfaced (in corpus via #721, crawled 12h;
same content as #736-#766; same canonical key via proxy wrapper, no new
key). No new primary campaign motif; last phase remains the circa Aug 10
Epstein poster; no competitor-equivalent guerrilla campaign against
Apple/Google/Samsung/Snap camera wearables in any of the 77 cycles.

Attention Sphere 77th no-match as podcast: quoted-search top results were
this repo's own GitHub commit pages (5 commit URLs, rejected as circular
per established discipline), plus the Andrew Bosworth "Possible" iHeart
episode (2025-03-26, crawled 285d; wearables-positive Meta-CTO interview
unrelated to any podcast named Attention Sphere; in corpus). Identity
strand unchanged from #596; task-spec name remains misidentified; Tracked
Sources table 76->77 cycles through Sep 15 2026.

Press surfaces: 6 results observed; ALL previously-logged URL keys, ALL
verified in corpus pre-commit (livemint voice-recordings-by-default piece
crawled 332d; techcrunch Mar 2026 contractor-review lawsuit piece crawled
4d; bbc.bm host-mirror 279d; livemint trends piece crawled 188d; reuters
Dec 2025 take-off piece 279d/crawled 279d; forbesindia privacy-scandal
roundup crawled 160d). Recency frontier TIED at Sep 9 (twenty-eighth
consecutive tie after #636 through #766); the petapixel.com Sep 9 piece
remains the newest date-verified in-corpus Meta-glasses press item; no
advance. GF episode 500 is a podcast milestone release carrying zero
Meta/wearables content, not a Meta-glasses press item, so the frontier is
unaffected. The YouTube clip is a non-tech debate clip, not a press item,
so the frontier is unaffected.

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


class TestNovelty771:
    """Iteration 771 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_771_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_771*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_771_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_771 files, no #771 in git log); this test
        # pins that no duplicate #771 main commit ever appears.
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
            if re.match(r"^[0-9a-f]{40} Type E #771: podcast sentiment", l)
        ]
        assert len(mains) == 1, "expected exactly one #771 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard771.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestRotationCycleGuard771:
    """Rotation: 770-774 window, #770 (D) anchors, #771 is the E leg.

    Deselected pre-commit per the #565 followup convention (the #771 main
    commit does not exist yet); patched green in the anchor followup.
    """

    ANCHORED_SHA = "919eb54ab152ee32df932718df8136dccf3aa7e5"  # main commit this run, per #565

    EXPECTED_ORDER = [("E", "771"), ("D", "770"), ("C", "769"), ("B", "768"), ("A", "767")]
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

    def test_window_770_774_second_leg_e(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type E #771: podcast sentiment")
        assert self.ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains and mains[0].startswith(self.ANCHORED_SHA + " "), mains


class TestGF77thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #771")[-1]

    def test_500_stands_newest_ten_hours_after_766(self):
        section = self._section()
        assert "Episode 500 stands as newest ten hours after #766" in section

    def test_goloudnow_corroborates_crawled_4h(self):
        section = self._section()
        assert "goloudnow.com (crawled 4h)" in section
        assert "sole fresh directory corroboration" in section
        assert "au.radio.net did not surface this run" in section

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

    def test_listen_notes_still_498_crawled_20d(self):
        section = self._section()
        assert "Listen Notes (crawled 20d) still lags on 498" in section

    def test_podscan_signal_carried_from_726(self):
        section = self._section()
        assert "podscan.fm signal carried from #726" in section

    def test_no_episode_501_next_release_plausibly_near_sep_21(self):
        section = self._section()
        assert "No episode 501 detected anywhere this run" in section
        assert "weekly cadence puts the next numbered release plausibly near Sep 21" in section

    def test_chortle_live_show_now_past(self):
        section = self._section()
        assert "Chortle's Sun 13 Sep 2026 Kings Place live show is now past" in section
        assert "a recorded live performance, not an episode release" in section

    def test_youtube_clip_new_to_corpus_not_ingested_out_of_scope(self):
        section = self._section()
        assert "https://www.youtube.com/watch?v=oVPri0Wr6F0" in section
        assert "Verified new pre-commit via repo-wide git grep" in section
        assert "NOT ingested" in section
        assert "surfaced-not-new handling of #460/#506" in section

    def test_seven_of_eight_gf_urls_in_corpus_pre_commit(self):
        section = self._section()
        assert "7 of the 8 GF-set URLs verified in corpus pre-commit" in section


class TestEHE39DayHold77thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #771")[-1]

    def test_thirty_nine_day_hold_same_calendar_day(self):
        section = self._section()
        assert "39-day hold continues (Aug 10 -> Sep 15, same calendar day as #766)" in section

    def test_seven_resurfaces_all_in_corpus(self):
        section = self._section()
        assert "7 re-surfaces observed: 6 previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "(51 days, crawled 51d)" in section
        assert "(60 days, crawled 17d" in section
        assert "(54 days, crawled 21d)" in section
        assert "(47 days, crawled 23d" in section
        assert "(62 days, crawled 3h" in section
        assert "(lenticular piece re-surfaced, crawled 1d" in section

    def test_toi_piece_resurfaced_same_key_crawled_12h(self):
        section = self._section()
        assert "(in corpus via #721, crawled 12h" in section
        assert "same canonical key via proxy wrapper, no new key" in section

    def test_no_new_primary_motif_77_cycles(self):
        section = self._section()
        assert "No new primary campaign motif" in section
        assert "Last campaign phase remains the circa Aug 10 Epstein poster" in section
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 77 cycles" in section


class TestAttentionSphere77thNoMatch:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #771")[-1]

    def test_seventy_seventh_no_match(self):
        section = self._section()
        assert "(seventy-seventh no-match)" in section

    def test_github_commit_pages_rejected_circular(self):
        section = self._section()
        assert "5 commit URLs, rejected as circular per established discipline" in section

    def test_boz_possible_episode_unrelated_in_corpus(self):
        section = self._section()
        assert "Andrew Bosworth \"Possible\" iHeart episode (2025-03-26, crawled 285d" in section
        assert "unrelated to any podcast named Attention Sphere; in corpus" in section

    def test_table_attention_sphere_77_cycles(self):
        section = self._section()
        assert "Identity strand unchanged from #596" in section
        assert "Tracked Sources 76->77 cycles through Sep 15 2026" in section


class TestPressSurfaces771:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #771")[-1]

    def test_six_results_all_known_keys_in_corpus(self):
        section = self._section()
        assert "SIX results observed; ALL previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses-privacy-concerns-after-workers-reviewed-nudity-sex-and-other-footage/" in section
        assert "are-mark-zuckerbergs-meta-ai-smart-glasses-watching-you-privacy-row-fuels-online-fears-puts-spotlight-on-dpdp-act-11772781893202.html" in section
        assert "meta-ray-ban-smart-glasses-could-store-voice-recordings-by-default-what-it-means-for-users/amp-11746118684276.html" in section
        assert "https://www.forbesindia.com/article/ai-tracker/why-metas-ray-ban-smart-glasses-are-causing-a-privacy-scandal/2991937/1" in section
        assert "(Mar 2026 Swedish-newspapers contractor-review lawsuit piece, crawled 4d" in section
        assert "(voice-recordings-by-default policy piece, crawled 332d" in section

    def test_frontier_tied_twenty_eighth(self):
        section = self._section()
        assert "TIED at Sep 9 (twenty-eighth consecutive tie after #636 through #766)" in section
        assert "no advance" in section
        assert "GF episode 500 is a podcast milestone release carrying zero Meta/wearables content, not a Meta-glasses press item" in section
        assert "The YouTube clip is a non-tech debate clip, not a press item" in section


class TestStandingRules771:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #771")[-1]

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

    def test_youtube_new_key_git_grep_verified_not_ingested(self):
        section = self._section()
        assert "ONE new URL key observed" in section
        assert "verified new-to-corpus pre-commit" in section
        assert "NOT ingested" in section

    def test_no_browser_open_snippet_bounded(self):
        section = self._section()
        assert "No browser.open verification attempt this run" in section
        assert "snippet-bounded directory corroboration" in section

    def test_ascii_no_em_dashes(self):
        assert "\u2014" not in self._section()
        assert "\u2013" not in self._section()

    def test_test_file_ref(self):
        section = self._section()
        assert "tests/test_type_e_771_podcast_sentiment_77th_verification_sep15_1pm.py" in section


class TestDocSync771:
    def test_readme_row_771(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_row_771_in_table(self):
        doc = _read(README_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_architecture_row_771(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_771_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog771:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #771 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        # "#771 Type E:" is the entry header; a bare "#771" would
        # false-positive on #770's rotation line ("E (#771) -> ...").
        assert "#771 Type E:" in self._tail()

    def test_log_cycle_and_hour(self):
        assert "seventy-seventh" in self._tail()
        assert "13:00 PDT" in self._tail()


class TestDateGrounding771:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_15_2026_is_tuesday(self):
        assert self._weekday("2026-09-15") == "Tuesday"
