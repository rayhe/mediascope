"""Type E #821: podcast sentiment 87th verification cycle (Sep 18 2026, 00:00 PDT).

Guilty Feminist: episode 500 stands as newest twenty-five hours after #796
(23:00 PDT Sep 16). Official-site corroboration carried from #796
(guiltyfeminist.com/new-normal/, crawled 18h at #796; ~43h elapsed by this
run); no fresh browser.open this run, snippet-bounded method per #796.
uk-podcasts.co.uk (crawled 4h) still shows 760 episodes / "Latest episode:
2026-09-16" (UNCHANGED since #806); still an UNVERIFIED single-directory
signal; no episode-501 asserted and no drop asserted per #503/iteration-492
discipline. Listen Notes re-crawled 4h ago (was 6h at #816): 760 episodes,
still lags on the 421 American Election RERELEASED listing as latest
episode; stale. listennotes.com/nl/ locale mirror (Last Crawl 225d;
pre-existing corpus key): 707 episodes, latest 467 Woof (recorded 20 Jan
2026 via Riverside, released 26 Jan); another stale locale mirror, not an
episode. iHeart GF directory page bounded absence this run (pre-existing
corpus key; did not surface in the GF query set). YouTube clips observed:
500 upload (crawled 21h; pre-existing key since #816; same episode as the
in-corpus official-site listing, YouTube distribution only), 491 Dame
Tracey Emin (crawled 66d, pre-existing), 473 ROAD TO GILEAD (crawled 143d,
pre-existing; re-surfaced after #816 bounded absence); 479 Welsh Election
part two bounded absence this run (pre-existing key; in corpus). Chortle
Edinburgh Fringe 2026 live-show listing re-surfaced (crawled 1h;
pre-existing corpus key; NOT an episode; upcoming date Sat 10 Oct 2026 at
Young Vic). No episode 501 detected anywhere this run; weekly cadence puts
the next numbered release plausibly near Sep 21. Triggernometry clip
oVPri0Wr6F0 bounded absence this run (in corpus since #771). GF-set 7 keys:
ALL previously-logged, ALL verified in corpus pre-commit (each >=1 hit);
0 NEW keys; zero Meta/wearables content in any observed title/description
(snippet-bounded).

EHE 45-day hold continues (Aug 10 -> Sep 18): 6 re-surfaces observed, ALL
previously-logged URL keys, ALL verified in corpus pre-commit (thetimes
53d/crawled 53d; engadget WWW-uppercase 63d/crawled 4d, same page per #676
convention; petapixel 57d/crawled 1d; latestly fact-check path 50d/crawled
3h; latestly social-viral path 50d/crawled 26d, in corpus since
#383/#445/#465; hyperallergic http key 65d/crawled 6h, same content).
Times of India 133146816 (in corpus via #721) and the fstoppers lenticular
piece (in corpus via #465/#536) bounded absences this run, not claims. No
new primary campaign motif; last phase remains the circa Aug 10 Epstein
poster; no competitor-equivalent guerrilla campaign against
Apple/Google/Samsung/Snap camera wearables in any of the 87 cycles.

Attention Sphere 87th no-match as podcast: quoted search returned this
repo's own GitHub pages (6 GitHub repo URLs with Full-URL mappings;
rejected as circular per established discipline, not ingested) and the
Andrew Bosworth "Possible" iHeart episode (2025-03-26, crawled 288d;
wearables-positive Meta-CTO interview unrelated to any podcast named
Attention Sphere; in corpus). Identity strand unchanged from #596;
task-spec name remains misidentified; Tracked Sources 86->87 cycles
through Sep 18 2026.

Press surfaces: 6 results observed; ALL previously-logged URL keys, ALL
verified in corpus pre-commit (livemint trends piece crawled 190d;
livemint voice-recordings-by-default policy piece crawled 335d; bbc.bm
host-mirror of in-corpus Reuters Dec 2025 piece crawled 282d; techcrunch
Mar 2026 contractor-review lawsuit piece crawled 3d, in corpus via
profiles/wired.yaml + profiles/competitor-coverage-research.yaml;
forbesindia privacy-scandal roundup crawled 163d; androidpolice class-action
piece crawled 16d, 197 days old, in corpus via test_android_police /
#606 / #776, NOT new). Recency frontier TIED at Sep 9 (thirty-eighth
consecutive tie after #636 through #816); the petapixel.com Sep 9 piece
remains the newest date-verified in-corpus Meta-glasses press item; no
advance.

Standing rule (Aug 28 2026): tone NOT_SCORED, p_value/cohens_d
NOT_CALCULATED, is_significant False; Type E monitoring-only, no mechanism
block in profiles/. No analysis.json update warranted. 20 external URL keys
observed (7 GF + 6 EHE + 1 iHeart Boz + 6 press); ALL previously-logged,
verified in corpus pre-commit (each >=1 hit); 0 NEW keys; no tone score
asserted without a first-hand read. 6 github.com own-repo URLs rejected as
circular per established discipline, not ingested. No browser.open;
snippet-bounded method.
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


class TestNovelty821:
    """Iteration 821 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_821_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_821*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_821_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_821 files, no #821 in git log); this test
        # pins that no duplicate #821 main commit ever appears.
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
        ).stdout.splitlines()
        mains = [
            l
            for l in log
            if re.match(r"^[0-9a-f]{40} Type E #821: podcast sentiment", l)
        ]
        assert len(mains) == 1, mains
        anchor = TestRotationCycleGuard821.ANCHORED_SHA
        assert mains[0].startswith(anchor + " "), (anchor, mains)


class TestRotationCycleGuard821:
    """Rotation: 820-824 window, #820 (D) anchors, #821 is the E leg.

    Deselected pre-commit per the #565 followup convention (the #821 main
    commit does not exist yet); patched green in the anchor followup.
    """

    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP_PER_565"  # main commit this run, per #565

    EXPECTED_ORDER = [("E", "821"), ("D", "820"), ("C", "819"), ("B", "818"), ("A", "817")]
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

    def test_window_820_824_second_leg_e(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type E #821: podcast sentiment")
        assert self.ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
            "PATCH_ME_IN_FOLLOWUP_PER_565",
        ), mains
        assert mains and mains[0].startswith(self.ANCHORED_SHA + " "), mains


class TestGF87thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #821")[-1]

    def test_500_stands_newest_twenty_five_hours_after_796(self):
        section = self._section()
        assert "Episode 500 stands as newest twenty-five hours after #796" in section
        assert "(23:00 PDT Sep 16)" in section

    def test_official_site_corroboration_carried_from_796(self):
        section = self._section()
        assert "Official-site corroboration carried from #796" in section
        assert "guiltyfeminist.com/new-normal/" in section
        assert "crawled 18h at #796" in section
        assert "~43h elapsed by this run" in section

    def test_no_fresh_browser_open_snippet_bounded(self):
        section = self._section()
        assert "no fresh browser.open this run" in section
        assert "snippet-bounded method per #796" in section

    def test_uk_podcasts_still_760_latest_sep_16_unverified_unchanged(self):
        section = self._section()
        assert 'uk-podcasts.co.uk (crawled 4h) still shows 760 episodes / "Latest episode: 2026-09-16"' in section
        assert "UNCHANGED since #806" in section
        assert "UNVERIFIED single-directory signal" in section
        assert "no drop is asserted per #503/iteration-492 discipline" in section

    def test_listen_notes_recrawled_4h_still_lags_421(self):
        section = self._section()
        assert "Listen Notes re-crawled 4h ago (was 6h at #816)" in section
        assert "760 episodes, still lags on the 421 American Election RERELEASED listing as latest episode" in section

    def test_nl_locale_mirror_surfaced_stale_preexisting_key(self):
        section = self._section()
        assert "listennotes.com/nl/ locale mirror (Last Crawl 225d; pre-existing corpus key)" in section
        assert "707 episodes, latest 467 Woof" in section
        assert "another stale locale mirror, not an episode" in section

    def test_iheart_gf_directory_page_bounded_absence(self):
        section = self._section()
        assert "iHeart GF directory page bounded absence this run (pre-existing corpus key" in section
        assert "did not surface in the GF query set" in section

    def test_youtube_clips_500_491_473_observed_479_bounded_absence(self):
        section = self._section()
        assert "the episode-500 upload (crawled 21h; pre-existing key since #816" in section
        assert "491 Dame Tracey Emin in Conversation (crawled 66d; pre-existing key)" in section
        assert "473 ROAD TO GILEAD (crawled 143d; pre-existing key; re-surfaced after #816 bounded absence)" in section
        assert "479 Welsh Election part two bounded absence this run (pre-existing key; in corpus)" in section

    def test_chortle_live_show_listing_resurfaced_preexisting_not_episode(self):
        section = self._section()
        assert "Chortle Edinburgh Fringe 2026 live-show listing re-surfaced (crawled 1h; pre-existing corpus key" in section
        assert "NOT an episode; upcoming date Sat 10 Oct 2026 at Young Vic" in section
        assert "https://www.chortle.co.uk/shows/edinburgh_fringe_2026/g/39124/the_guilty_feminist" in section

    def test_no_episode_501_next_release_plausibly_near_sep_21(self):
        section = self._section()
        assert "No episode 501 detected anywhere this run" in section
        assert "weekly cadence puts the next numbered release plausibly near Sep 21" in section

    def test_triggernometry_bounded_absence(self):
        section = self._section()
        assert "The YouTube Triggernometry clip oVPri0Wr6F0 did not surface this run (bounded absence, not a claim; in corpus since #771)" in section

    def test_gf_set_accounting_seven_keys_all_known_zero_new(self):
        section = self._section()
        assert "GF-set: 7 keys observed, ALL previously-logged, ALL verified in corpus pre-commit (each >=1 hit); 0 NEW keys" in section

    def test_zero_meta_wearables_content(self):
        section = self._section()
        assert "All observed titles/descriptions carry ZERO Meta/wearables content (snippet-bounded)" in section


class TestEHEHold87thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #821")[-1]

    def test_forty_five_day_hold(self):
        section = self._section()
        assert "45-day hold continues (Aug 10 -> Sep 18)" in section

    def test_six_resurfaces_all_in_corpus(self):
        section = self._section()
        assert "6 re-surfaces observed, ALL previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "(53 days, crawled 53d)" in section
        assert "(63 days, crawled 4d" in section
        assert "(57 days, crawled 1d)" in section
        assert "(50 days, crawled 3h)" in section
        assert "(50 days, crawled 26d" in section
        assert "(65 days, crawled 6h; same content)" in section

    def test_toi_fstoppers_bounded_absences(self):
        section = self._section()
        assert "the Times of India 133146816 via proxy wrapper (in corpus via #721)" in section
        assert "the fstoppers.com lenticular piece (in corpus via #465/#536)" in section

    def test_no_new_primary_motif_87_cycles(self):
        section = self._section()
        assert "No new primary campaign motif" in section
        assert "Last campaign phase remains the circa Aug 10 Epstein poster" in section
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 87 cycles" in section


class TestAttentionSphere87thNoMatch:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #821")[-1]

    def test_eighty_seventh_no_match(self):
        section = self._section()
        assert "(eighty-seventh no-match)" in section

    def test_github_pages_rejected_circular(self):
        section = self._section()
        assert "6 GitHub repo URLs with Full-URL mappings" in section
        assert "rejected as circular per established discipline, not ingested" in section

    def test_boz_possible_episode_unrelated_in_corpus(self):
        section = self._section()
        assert 'Andrew Bosworth "Possible" iHeart episode (2025-03-26, crawled 288d' in section
        assert "unrelated to any podcast named Attention Sphere; in corpus" in section

    def test_tracked_sources_86_to_87(self):
        section = self._section()
        assert "Identity strand unchanged from #596" in section
        assert "Tracked Sources 86->87 cycles through Sep 18 2026" in section


class TestPressSurfaces821:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #821")[-1]

    def test_six_results_all_known_keys_in_corpus(self):
        section = self._section()
        assert "SIX results observed; ALL previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses-privacy-concerns-after-workers-reviewed-nudity-sex-and-other-footage/" in section
        assert "are-mark-zuckerbergs-meta-ai-smart-glasses-watching-you-privacy-row-fuels-online-fears-puts-spotlight-on-dpdp-act-11772781893202.html" in section
        assert "meta-ray-ban-smart-glasses-could-store-voice-recordings-by-default-what-it-means-for-users/amp-11746118684276.html" in section
        assert "https://bbc.bm/ray-ban-meta-glasses-take-off-but-face-privacy-and-competition-test" in section
        assert "(trends piece, crawled 190d" in section
        assert "(host-mirror of the in-corpus Reuters Dec 2025 piece, crawled 282d" in section

    def test_androidpolice_in_corpus_not_new(self):
        section = self._section()
        assert "https://www.androidpolice.com/meta-ai-glasses-privacy-concern/" in section
        assert "in corpus via test_android_police / #606 / #776, NOT new" in section

    def test_frontier_tied_thirty_eighth(self):
        section = self._section()
        assert "TIED at Sep 9 (thirty-eighth consecutive tie after #636 through #816)" in section
        assert "the petapixel.com Sep 9 piece remains the newest date-verified in-corpus Meta-glasses press item" in section
        assert "no advance" in section


class TestStandingRules821:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #821")[-1]

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

    def test_url_key_accounting_20_observed_20_known_0_new(self):
        section = self._section()
        assert "20 external URL keys observed (7 GF + 6 EHE + 1 iHeart Boz + 6 press)" in section
        assert "ALL previously-logged, verified in corpus pre-commit (each >=1 hit); 0 NEW keys" in section

    def test_circular_github_urls_rejected(self):
        section = self._section()
        assert "6 github.com own-repo URLs rejected as circular per established discipline, not ingested" in section

    def test_ascii_no_em_dashes(self):
        assert "\u2014" not in self._section()
        assert "\u2013" not in self._section()

    def test_test_file_ref(self):
        section = self._section()
        assert "tests/test_type_e_821_podcast_sentiment_87th_verification_sep18_12am.py" in section


class TestDocSync821:
    def test_readme_row_821(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_row_821_in_table(self):
        doc = _read(README_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_architecture_row_821(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_821_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog821:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #821 entry sits at the end of the file, not the top.
        return "\n".join(lines[-120:])

    def test_log_entry_present(self):
        # "#821 Type E:" is the entry header; a bare "#821" would
        # false-positive on #820's rotation line ("A (#821) -> ..." style).
        assert "#821 Type E:" in self._tail()

    def test_log_cycle_and_hour(self):
        assert "eighty-seventh" in self._tail()
        assert "00:00 PDT" in self._tail()


class TestDateGrounding821:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_18_2026_is_friday(self):
        assert self._weekday("2026-09-18") == "Friday"
