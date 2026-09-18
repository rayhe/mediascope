"""Type E #816: podcast sentiment 86th verification cycle (Sep 17 2026, 19:00 PDT).

Guilty Feminist: episode 500 stands as newest thirty-two hours after #796
(23:00 PDT Sep 16). Official-site corroboration carried from #796
(guiltyfeminist.com/new-normal/, crawled 18h at #796; ~38h elapsed by this
run); no fresh browser.open this run, snippet-bounded method per #796.
uk-podcasts.co.uk (crawled 14h) still shows 760 episodes / "Latest episode:
2026-09-16" (UNCHANGED since #806); still an UNVERIFIED single-directory
signal; no episode-501 asserted per #503/iteration-492 discipline. Listen
Notes re-crawled 6h ago (was 1h at #811): 760 episodes, still lags on
the 421 American Election RERELEASED listing as latest episode; stale.
listennotes.com/nl/ locale mirror (Last Crawl 224d; pre-existing corpus
key): 707 episodes, latest 467 Woof (recorded 20 Jan 2026 via Riverside,
released 26 Jan); another stale locale mirror, not an episode. iHeart GF
directory page observed (crawled 297d; pre-existing key): shown slate 458
Annie Lennox (Nov 2025) + Emergency Episode Gaza nurse Alaa Al-ghoul
(Nov 2025); stale. NEW URL key this run: the episode-500 YouTube upload
(iKXj2w2cp50, recorded 22 Aug 2026 at Gilded Balloon at the Museum,
released 14 Sep, crawled 16h) - same episode as the in-corpus official-site
listing, YouTube distribution only, verified 0 hits repo-wide pre-commit.
Other YouTube clips: 491 Dame Tracey Emin (crawled 66d), 479 Welsh Election
part two (crawled 148d), both pre-existing; 473 ROAD TO GILEAD bounded
absence this run. No episode 501 detected anywhere; weekly cadence puts the
next numbered release plausibly near Sep 21. Triggernometry clip
oVPri0Wr6F0 bounded absence this run (in corpus since #771). GF-set 7 keys:
6 previously-logged + 1 NEW (the 500 YouTube upload); zero Meta/wearables
content in any observed title/description (snippet-bounded).

EHE 45-day hold continues (Aug 10 -> Sep 17): 7 re-surfaces, ALL
previously-logged URL keys, ALL verified in corpus pre-commit (thetimes
53d/crawled 53d; engadget WWW-uppercase 63d/crawled 3d, same page per #676
convention; petapixel 57d/crawled 1d; latestly 50d/crawled 26d;
hyperallergic http key 65d/crawled 1h, same content; Times of India
133146816 via proxy wrapper, in corpus via #721, crawled 2d, same content;
fstoppers lenticular crawled 4h, in corpus via #465/#536). No new primary
campaign motif; last phase remains the circa Aug 10 Epstein poster; no
competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap
camera wearables in any of the 86 cycles.

Attention Sphere 86th no-match as podcast: quoted search returned this
repo's own GitHub pages (4 commit URLs with Full-URL mappings; rejected as
circular per established discipline) and the Andrew Bosworth "Possible"
iHeart episode (2025-03-26, crawled 287d; wearables-positive Meta-CTO
interview unrelated to any podcast named Attention Sphere; in corpus).
Identity strand unchanged from #596; task-spec name remains misidentified;
Tracked Sources 85->86 cycles through Sep 17 2026.

Press surfaces: 6 results observed; ALL previously-logged URL keys, ALL
verified in corpus pre-commit (livemint voice-recordings-by-default piece
crawled 335d; techcrunch Mar 2026 contractor-review lawsuit piece crawled
2d; bbc.bm host-mirror of in-corpus Reuters Dec 2025 piece crawled 282d;
livemint trends piece crawled 190d; forbesindia privacy-scandal roundup
crawled 163d; androidpolice class-action piece crawled 16d, 196 days old,
in corpus via test_android_police / #606 / #776, NOT new). Recency frontier
TIED at Sep 9 (thirty-seventh consecutive tie after #636 through #811);
the petapixel.com Sep 9 piece remains the newest date-verified in-corpus
Meta-glasses press item; no advance.

Standing rule (Aug 28 2026): tone NOT_SCORED, p_value/cohens_d
NOT_CALCULATED, is_significant False; Type E monitoring-only, no mechanism
block in profiles/. No analysis.json update warranted. 21 external URL keys
observed (7 GF + 7 EHE + 1 iHeart Boz + 6 press); 20 previously-logged
verified in corpus pre-commit; 1 NEW key (episode-500 YouTube distribution
URL, same episode content). No browser.open; snippet-bounded method.
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


class TestNovelty816:
    """Iteration 816 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_816_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_816*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_816_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_816 files, no #816 in git log); this test
        # pins that no duplicate #816 main commit ever appears.
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
            if re.match(r"^[0-9a-f]{40} Type E #816: podcast sentiment", l)
        ]
        assert len(mains) == 1, mains
        anchor = TestRotationCycleGuard816.ANCHORED_SHA
        assert mains[0].startswith(anchor + " "), (anchor, mains)


class TestRotationCycleGuard816:
    """Rotation: 815-819 window, #815 (D) anchors, #816 is the E leg.

    Deselected pre-commit per the #565 followup convention (the #816 main
    commit does not exist yet); patched green in the anchor followup.
    """

    ANCHORED_SHA = "5ddcf156f62ad7ab978ca82aa6902c88ba61579b"  # main commit this run, per #565

    EXPECTED_ORDER = [("E", "816"), ("D", "815"), ("C", "814"), ("B", "813"), ("A", "812")]
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

    def test_window_815_819_second_leg_e(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type E #816: podcast sentiment")
        assert self.ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
            "PATCH_ME_IN_FOLLOWUP_PER_565",
        ), mains
        assert mains and mains[0].startswith(self.ANCHORED_SHA + " "), mains


class TestGF86thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #816")[-1]

    def test_500_stands_newest_thirty_two_hours_after_796(self):
        section = self._section()
        assert "Episode 500 stands as newest thirty-two hours after #796" in section

    def test_official_site_corroboration_carried_from_796(self):
        section = self._section()
        assert "Official-site corroboration carried from #796" in section
        assert "guiltyfeminist.com/new-normal/" in section
        assert "crawled 18h at #796" in section
        assert "~38h elapsed by this run" in section

    def test_no_fresh_browser_open_snippet_bounded(self):
        section = self._section()
        assert "no fresh browser.open this run" in section
        assert "snippet-bounded method per #796" in section

    def test_uk_podcasts_still_760_latest_sep_16_unverified_unchanged(self):
        section = self._section()
        assert 'uk-podcasts.co.uk (crawled 14h) still shows 760 episodes / "Latest episode: 2026-09-16"' in section
        assert "UNCHANGED since #806" in section
        assert "UNVERIFIED single-directory signal" in section
        assert "no drop is asserted per #503/iteration-492 discipline" in section

    def test_listen_notes_recrawled_6h_still_lags_421(self):
        section = self._section()
        assert "Listen Notes re-crawled 6h ago (was 1h at #811)" in section
        assert "760 episodes, still lags on the 421 American Election RERELEASED listing as latest episode" in section

    def test_nl_locale_mirror_surfaced_stale_preexisting_key(self):
        section = self._section()
        assert "listennotes.com/nl/ locale mirror surfaced this run (Last Crawl 224d; pre-existing corpus key)" in section
        assert "707 episodes, latest 467 Woof" in section
        assert "another stale locale mirror, not an episode" in section

    def test_iheart_gf_directory_page_stale_preexisting_key(self):
        section = self._section()
        assert "iHeart GF directory page observed this run (crawled 297d; pre-existing key)" in section
        assert "458 Annie Lennox in Conversation at the V&A (Nov 2025)" in section
        assert "Emergency Episode Gaza nurse Alaa Al-ghoul (Nov 2025)" in section

    def test_new_key_500_youtube_upload_verified_zero_hits_precommit(self):
        section = self._section()
        assert "NEW URL key this run: the episode-500 YouTube upload" in section
        assert "same episode as the in-corpus official-site listing, YouTube distribution only" in section
        assert "verified 0 hits repo-wide pre-commit" in section
        assert "https://www.youtube.com/watch?v=iKXj2w2cp50" in section

    def test_other_youtube_clips_observed_473_bounded_absence(self):
        section = self._section()
        assert "491 Dame Tracey Emin in Conversation (crawled 66d), 479 Welsh Election Special part two (crawled 148d)" in section
        assert "both pre-existing corpus keys; clips not episodes" in section
        assert "473 ROAD TO GILEAD (crawled 143d) bounded absence this run (in corpus; did not surface in the GF query set)" in section

    def test_no_episode_501_next_release_plausibly_near_sep_21(self):
        section = self._section()
        assert "No episode 501 detected anywhere this run" in section
        assert "weekly cadence puts the next numbered release plausibly near Sep 21" in section

    def test_triggernometry_bounded_absence(self):
        section = self._section()
        assert "The YouTube Triggernometry clip oVPri0Wr6F0 did not surface this run (bounded absence, not a claim; in corpus since #771)" in section

    def test_gf_set_accounting_seven_keys_six_known_one_new(self):
        section = self._section()
        assert "GF-set: 7 keys observed, 6 previously-logged + 1 NEW (the 500 YouTube upload)" in section
        assert "the 6 known verified in corpus pre-commit" in section

    def test_zero_meta_wearables_content(self):
        section = self._section()
        assert "All observed titles/descriptions carry ZERO Meta/wearables content (snippet-bounded)" in section


class TestEHEHold86thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #816")[-1]

    def test_forty_five_day_hold(self):
        section = self._section()
        assert "45-day hold continues (Aug 10 -> Sep 17)" in section

    def test_seven_resurfaces_all_in_corpus(self):
        section = self._section()
        assert "7 re-surfaces observed, ALL previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "(53 days, crawled 53d)" in section
        assert "(63 days, crawled 3d" in section
        assert "(57 days, crawled 1d)" in section
        assert "(50 days, crawled 26d" in section
        assert "(65 days, crawled 1h; same content)" in section
        assert "(lenticular piece re-surfaced, crawled 4h" in section

    def test_toi_piece_resurfaced_fresh_crawl_2d_same_content(self):
        section = self._section()
        assert "in corpus via #721, crawled 2d; same content as #736-#811" in section
        assert "same canonical key via proxy wrapper, no new key" in section

    def test_no_new_primary_motif_86_cycles(self):
        section = self._section()
        assert "No new primary campaign motif" in section
        assert "Last campaign phase remains the circa Aug 10 Epstein poster" in section
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 86 cycles" in section


class TestAttentionSphere86thNoMatch:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #816")[-1]

    def test_eighty_sixth_no_match(self):
        section = self._section()
        assert "(eighty-sixth no-match)" in section

    def test_github_pages_rejected_circular(self):
        section = self._section()
        assert "4 commit URLs with Full-URL mappings" in section
        assert "rejected as circular per established discipline" in section

    def test_boz_possible_episode_unrelated_in_corpus(self):
        section = self._section()
        assert 'Andrew Bosworth "Possible" iHeart episode (2025-03-26, crawled 287d' in section
        assert "unrelated to any podcast named Attention Sphere; in corpus" in section

    def test_tracked_sources_85_to_86(self):
        section = self._section()
        assert "Identity strand unchanged from #596" in section
        assert "Tracked Sources 85->86 cycles through Sep 17 2026" in section


class TestPressSurfaces816:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #816")[-1]

    def test_six_results_all_known_keys_in_corpus(self):
        section = self._section()
        assert "SIX results observed; ALL previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses-privacy-concerns-after-workers-reviewed-nudity-sex-and-other-footage/" in section
        assert "are-mark-zuckerbergs-meta-ai-smart-glasses-watching-you-privacy-row-fuels-online-fears-puts-spotlight-on-dpdp-act-11772781893202.html" in section
        assert "meta-ray-ban-smart-glasses-could-store-voice-recordings-by-default-what-it-means-for-users/amp-11746118684276.html" in section
        assert "https://bbc.bm/ray-ban-meta-glasses-take-off-but-face-privacy-and-competition-test" in section
        assert "(voice-recordings-by-default policy piece, crawled 335d" in section
        assert "(host-mirror of the in-corpus Reuters Dec 2025 piece, crawled 282d" in section

    def test_androidpolice_in_corpus_not_new(self):
        section = self._section()
        assert "https://www.androidpolice.com/meta-ai-glasses-privacy-concern/" in section
        assert "in corpus via test_android_police / #606 / #776, NOT new" in section

    def test_frontier_tied_thirty_seventh(self):
        section = self._section()
        assert "TIED at Sep 9 (thirty-seventh consecutive tie after #636 through #811)" in section
        assert "the petapixel.com Sep 9 piece remains the newest date-verified in-corpus Meta-glasses press item" in section
        assert "no advance" in section


class TestStandingRules816:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #816")[-1]

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

    def test_url_key_accounting_21_observed_20_known_1_new(self):
        section = self._section()
        assert "21 external URL keys observed (7 GF + 7 EHE + 1 iHeart Boz + 6 press)" in section
        assert "20 previously-logged verified in corpus pre-commit (each >=1 hit); 1 NEW key (the episode-500 YouTube upload" in section

    def test_circular_github_urls_rejected(self):
        section = self._section()
        assert "4 github.com own-repo URLs rejected as circular per established discipline, not ingested" in section

    def test_ascii_no_em_dashes(self):
        assert "\u2014" not in self._section()
        assert "\u2013" not in self._section()

    def test_test_file_ref(self):
        section = self._section()
        assert "tests/test_type_e_816_podcast_sentiment_86th_verification_sep17_7pm.py" in section


class TestDocSync816:
    def test_readme_row_816(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_readme_row_816_in_table(self):
        doc = _read(README_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))

    def test_architecture_row_816(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_816_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog816:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #816 entry sits at the end of the file, not the top.
        return "\n".join(lines[-120:])

    def test_log_entry_present(self):
        # "#816 Type E:" is the entry header; a bare "#816" would
        # false-positive on #815's rotation line ("E (#816) -> ...").
        assert "#816 Type E:" in self._tail()

    def test_log_cycle_and_hour(self):
        assert "eighty-sixth" in self._tail()
        assert "19:00 PDT" in self._tail()


class TestDateGrounding816:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_17_2026_is_thursday(self):
        assert self._weekday("2026-09-17") == "Thursday"
