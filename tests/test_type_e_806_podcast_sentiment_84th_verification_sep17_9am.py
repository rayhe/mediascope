"""Type E #806: podcast sentiment 84th verification cycle (Sep 17 2026, 09:00 PDT).

Guilty Feminist: episode 500 stands as newest twenty-two hours after #796
(23:00 PDT Sep 16). Official-site corroboration carried from #796
(guiltyfeminist.com/new-normal/, crawled 18h at #796; ~28h elapsed by this
run); no fresh browser.open this run, snippet-bounded method per #796.
uk-podcasts.co.uk (crawled 4h) still shows 760 episodes / "Latest episode:
2026-09-16" (UNCHANGED since #801); still an UNVERIFIED single-directory
signal; no episode-501 asserted per #503/iteration-492 discipline. Listen
Notes still lags on 498 (756 episodes; Last Crawl 10 days ago).
podparadise.com (crawled 9h) observed this run (was bounded absence at
#801): 757 episodes, 499 "Where You End and I Begin with Lindsey Mendick"
(recorded 15 Aug 2026 TKE Studios Margate, released 7 Sep 2026;
art/politics, not tech) latest on that directory; pre-existing corpus key,
not new. goloudnow.com (crawled 9h) observed this run on a pre-existing
key (in corpus since #726): listing surfaces "In Conversation with Indhu
Rubasingham" (National Theatre; recorded 9 Sep 2026, released 12 Sep;
theatre, not tech) - a non-numbered special, NOT episode 501.
chortle.co.uk (crawled 22h) / edfringe.com (crawled <1h) /
stagewhispers.com.au (104d) live-show listings observed this run (were
bounded absence at #801); all pre-existing corpus keys; listings not
episodes. listennotes.com/pt/ stale mirror (710 episodes, latest 469
Feminist History; crawled 216d; pre-existing key). No episode 501 detected
anywhere this run; weekly cadence puts the next numbered release plausibly
near Sep 21. ZERO new URL keys this run: GF-set 8 keys observed, ALL
previously-logged, ALL verified in corpus pre-commit; zero Meta/wearables
content in any observed title/description (snippet-bounded).

EHE 43-day hold continues (Aug 10 -> Sep 17): 7 re-surfaces, ALL
previously-logged URL keys, ALL verified in corpus pre-commit (thetimes
52d/crawled 52d; engadget WWW-uppercase 62d/crawled 3d, same page per #676
convention; petapixel 56d/crawled 20h; latestly 49d/crawled 25d;
hyperallergic http key 64d/crawled 2h, same content; Times of India
133146816 via proxy wrapper, in corpus via #721, crawled 2d, same content;
fstoppers lenticular crawled 3d, in corpus via #465/#536). No new primary
campaign motif; last phase remains the circa Aug 10 Epstein poster; no
competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap
camera wearables in any of the 84 cycles.

Attention Sphere 84th no-match as podcast: quoted search returned this
repo's own GitHub pages (5 commit URLs + 1 blob URL with Full-URL mappings;
rejected as circular per established discipline) and the Andrew Bosworth
"Possible" iHeart episode (2025-03-26, crawled 287d; wearables-positive
Meta-CTO interview unrelated to any podcast named Attention Sphere; in
corpus). Identity strand unchanged from #596; task-spec name remains
misidentified; Tracked Sources 83->84 cycles through Sep 17 2026.

Press surfaces: 6 results observed; ALL previously-logged URL keys, ALL
verified in corpus pre-commit (livemint voice-recordings-by-default piece
crawled 334d; techcrunch Mar 2026 contractor-review lawsuit piece crawled
2d; bbc.bm host-mirror of in-corpus Reuters Dec 2025 piece crawled 281d;
livemint trends piece crawled 189d; forbesindia privacy-scandal roundup
crawled 162d; androidpolice class-action piece crawled 15d, 195 days old,
in corpus via test_android_police / #606 / #776, NOT new). Recency frontier
TIED at Sep 9 (thirty-fifth consecutive tie after #636 through #801); the
petapixel.com Sep 9 piece remains the newest date-verified in-corpus
Meta-glasses press item; no advance.

Standing rule (Aug 28 2026): tone NOT_SCORED, p_value/cohens_d
NOT_CALCULATED, is_significant False; Type E monitoring-only, no mechanism
block in profiles/. No analysis.json update warranted. 22 external URL keys
observed (8 GF + 7 EHE + 1 iHeart Boz + 6 press); ALL 22 previously-logged
verified in corpus pre-commit; ZERO new keys this run. No browser.open;
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


class TestNovelty806:
    """Iteration 806 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_806_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_806*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_806_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_806 files, no #806 in git log); this test
        # pins that no duplicate #806 main commit ever appears.
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
            if re.match(r"^[0-9a-f]{40} Type E #806: podcast sentiment", l)
        ]
        assert len(mains) == 1, mains
        anchor = TestRotationCycleGuard806.ANCHORED_SHA
        assert mains[0].startswith(anchor + " "), (anchor, mains)


class TestRotationCycleGuard806:
    """Rotation: 805-809 window, #805 (D) anchors, #806 is the E leg.

    Deselected pre-commit per the #565 followup convention (the #806 main
    commit does not exist yet); patched green in the anchor followup.
    """

    ANCHORED_SHA = "f0b2d0304a2985d2264211f028f1a6bceccee999"  # main commit this run, per #565

    EXPECTED_ORDER = [("E", "806"), ("D", "805"), ("C", "804"), ("B", "803"), ("A", "802")]
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

    def test_window_805_809_second_leg_e(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type E #806: podcast sentiment")
        assert self.ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
            "PATCH_ME_IN_FOLLOWUP_PER_565",
        ), mains
        assert mains and mains[0].startswith(self.ANCHORED_SHA + " "), mains


class TestGF84thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #806")[-1]

    def test_500_stands_newest_twenty_two_hours_after_796(self):
        section = self._section()
        assert "Episode 500 stands as newest twenty-two hours after #796" in section

    def test_official_site_corroboration_carried_from_796(self):
        section = self._section()
        assert "Official-site corroboration carried from #796" in section
        assert "guiltyfeminist.com/new-normal/" in section
        assert "crawled 18h at #796" in section
        assert "~28h elapsed by this run" in section

    def test_no_fresh_browser_open_snippet_bounded(self):
        section = self._section()
        assert "no fresh browser.open this run" in section
        assert "snippet-bounded method per #796" in section

    def test_uk_podcasts_still_760_latest_sep_16_unverified_unchanged(self):
        section = self._section()
        assert 'uk-podcasts.co.uk (crawled 4h) still shows 760 episodes / "Latest episode: 2026-09-16"' in section
        assert "UNCHANGED since #801" in section
        assert "UNVERIFIED single-directory signal" in section
        assert "no drop is asserted per #503/iteration-492 discipline" in section

    def test_listen_notes_still_498_crawled_10d(self):
        section = self._section()
        assert "Listen Notes still lags on 498 (756 episodes; Last Crawl 10 days ago)" in section

    def test_podparadise_observed_757_499_mendick_preexisting_key(self):
        section = self._section()
        assert "podparadise.com (crawled 9h) observed this run" in section
        assert "757 episodes" in section
        assert '499 "Where You End and I Begin with Lindsey Mendick"' in section
        assert "pre-existing corpus key, not new" in section

    def test_goloudnow_observed_indhu_rubasingham_special_preexisting_key(self):
        section = self._section()
        assert "goloudnow.com (crawled 9h) observed this run on a pre-existing key" in section
        assert '"In Conversation with Indhu Rubasingham"' in section
        assert "in corpus since #726" in section
        assert "non-numbered special, NOT episode 501" in section

    def test_live_show_listings_observed_preexisting_keys(self):
        section = self._section()
        assert "chortle.co.uk (crawled 22h) / edfringe.com (crawled <1h) / stagewhispers.com.au (104d) live-show listings observed this run" in section
        assert "were bounded absence at #801" in section
        assert "listings not episodes" in section

    def test_listennotes_pt_stale_mirror_preexisting_key(self):
        section = self._section()
        assert "listennotes.com/pt/ stale mirror" in section
        assert "710 episodes, latest 469 Feminist History" in section
        assert "crawled 216d" in section

    def test_no_episode_501_next_release_plausibly_near_sep_21(self):
        section = self._section()
        assert "No episode 501 detected anywhere this run" in section
        assert "weekly cadence puts the next numbered release plausibly near Sep 21" in section

    def test_triggernometry_bounded_absence(self):
        section = self._section()
        assert "The YouTube Triggernometry clip oVPri0Wr6F0 did not surface this run (bounded absence, not a claim; in corpus since #771)" in section

    def test_zero_new_url_keys_eight_keys_all_in_corpus(self):
        section = self._section()
        assert "ZERO new URL keys this run: GF-set 8 keys observed, ALL previously-logged, ALL verified in corpus pre-commit" in section

    def test_zero_meta_wearables_content(self):
        section = self._section()
        assert "All observed titles/descriptions carry ZERO Meta/wearables content (snippet-bounded)" in section


class TestEHEHold84thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #806")[-1]

    def test_forty_three_day_hold(self):
        section = self._section()
        assert "43-day hold continues (Aug 10 -> Sep 17)" in section

    def test_seven_resurfaces_all_in_corpus(self):
        section = self._section()
        assert "7 re-surfaces observed, ALL previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "(52 days, crawled 52d)" in section
        assert "(62 days, crawled 3d" in section
        assert "(56 days, crawled 20h)" in section
        assert "(49 days, crawled 25d" in section
        assert "(64 days, crawled 2h; same content)" in section
        assert "(lenticular piece re-surfaced, crawled 3d" in section

    def test_toi_piece_resurfaced_fresh_crawl_2d_same_content(self):
        section = self._section()
        assert "in corpus via #721, crawled 2d; fresh crawl, same content as #736-#801" in section
        assert "same canonical key via proxy wrapper, no new key" in section

    def test_no_new_primary_motif_84_cycles(self):
        section = self._section()
        assert "No new primary campaign motif" in section
        assert "Last campaign phase remains the circa Aug 10 Epstein poster" in section
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 84 cycles" in section


class TestAttentionSphere84thNoMatch:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #806")[-1]

    def test_eighty_fourth_no_match(self):
        section = self._section()
        assert "(eighty-fourth no-match)" in section

    def test_github_pages_rejected_circular(self):
        section = self._section()
        assert "5 commit URLs + 1 blob URL with Full-URL mappings" in section
        assert "rejected as circular per established discipline" in section

    def test_boz_possible_episode_unrelated_in_corpus(self):
        section = self._section()
        assert 'Andrew Bosworth "Possible" iHeart episode (2025-03-26, crawled 287d' in section
        assert "unrelated to any podcast named Attention Sphere; in corpus" in section

    def test_tracked_sources_83_to_84(self):
        section = self._section()
        assert "Identity strand unchanged from #596" in section
        assert "Tracked Sources 83->84 cycles through Sep 17 2026" in section


class TestPressSurfaces806:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #806")[-1]

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

    def test_frontier_tied_thirty_fifth(self):
        section = self._section()
        assert "TIED at Sep 9 (thirty-fifth consecutive tie after #636 through #801)" in section
        assert "the petapixel.com Sep 9 piece remains the newest date-verified in-corpus Meta-glasses press item" in section
        assert "no advance" in section


class TestStandingRules806:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #806")[-1]

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

    def test_url_key_accounting_22_observed_22_known_zero_new(self):
        section = self._section()
        assert "22 external URL keys observed (8 GF + 7 EHE + 1 iHeart Boz + 6 press)" in section
        assert "ALL 22 previously-logged verified in corpus pre-commit; ZERO new keys this run" in section

    def test_circular_github_urls_rejected(self):
        section = self._section()
        assert "6 github.com own-repo URLs rejected as circular per established discipline, not ingested" in section

    def test_ascii_no_em_dashes(self):
        assert "\u2014" not in self._section()
        assert "\u2013" not in self._section()

    def test_test_file_ref(self):
        section = self._section()
        assert "tests/test_type_e_806_podcast_sentiment_84th_verification_sep17_9am.py" in section


class TestDocSync806:
    def test_readme_row_806(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_row_806_in_table(self):
        doc = _read(README_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_architecture_row_806(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_806_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog806:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #806 entry sits at the end of the file, not the top.
        return "\n".join(lines[-110:])

    def test_log_entry_present(self):
        # "#806 Type E:" is the entry header; a bare "#806" would
        # false-positive on #805's rotation line ("E (#806) -> ...").
        assert "#806 Type E:" in self._tail()

    def test_log_cycle_and_hour(self):
        assert "eighty-fourth" in self._tail()
        assert "09:00 PDT" in self._tail()


class TestDateGrounding806:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_17_2026_is_thursday(self):
        assert self._weekday("2026-09-17") == "Thursday"
