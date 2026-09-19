"""Type E #841: podcast sentiment 91st verification cycle - Sep 18 2026 20:00 PDT.

Second leg of the 840-844 window (D #840 -> E #841 -> A -> B -> C).
Monitoring-only: GF episode 500 stands newest (45h after #796); EHE 46-day
hold; Attention Sphere 91st quoted-search no-match; frontier TIED at Sep 9
(42nd consecutive tie). 18 observed URL keys: 16 previously-logged, 2 NEW
(getpodcast GF directory surface; softonic Epstein-poster re-surface).
Standing rule (Aug 28 2026): tone NOT_SCORED, p_value/cohens_d
NOT_CALCULATED, is_significant False. No mechanism block in profiles/.
No analysis.json update warranted. NOT artifact-grade.

Conventions: anchor 1 + rotation-guard 3 deselected pre-commit per #565,
patched green in the anchor followup; doc-sync 4 + iteration-log 2 green
pre-commit per #719. ASCII-only, no em dashes.
"""

import glob
import os
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TEST_BASENAME = os.path.basename(__file__)

# Exact URL keys observed this run (verbatim from the Full-URL listings).
GF_KEYS = [
    "youtube.com/watch?v=iKXj2w2cp50",
    "goloudnow.com/podcasts/the-guilty-feminist-152/deborah-frances-white-on-the-news-meeting-519585",
    "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG/",
    "getpodcast.com/podcast/the-guilty-feminist",  # NEW this run
    "uk-podcasts.co.uk/podcast/the-guilty-feminist/deborah-frances-white-on-the-news-meeting",
    "podparadise.com/Podcast/1068940771",
    "listennotes.com/pt/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG/",
]
NEW_GF_KEYS = ["getpodcast.com/podcast/the-guilty-feminist"]

EHE_KEYS = [
    "WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/",
    "singulism.com/en/2026-07-17-meta-glasses-protest-london-bus-stops/",
    "petapixel.com/2026/07/23/kylie-jenners-meta-smart-glasses-parodied-in-guerrilla-lenticular-ad/",
    "community.designtaxi.com/topic/33476-activist-group-hijacks-kylie-jenners-meta-smart-glasses-ads-with-sharp-privacy-warnings-across-london/",
    "en.softonic.com/articles/ray-ban-meta-smart-glasses-back-in-the-spotlight-london-ad-uses-epstein-image",  # NEW this run
]
NEW_EHE_KEYS = ["en.softonic.com/articles/ray-ban-meta-smart-glasses-back-in-the-spotlight-london-ad-uses-epstein-image"]

PRESS_KEYS = [
    "livemint.com/news/trends/are-mark-zuckerbergs-meta-ai-smart-glasses-watching-you-privacy-row-fuels-online-fears-puts-spotlight-on-dpdp-act-11772781893202.html",
    "livemint.com/technology/tech-news/meta-ray-ban-smart-glasses-could-store-voice-recordings-by-default-what-it-means-for-users/amp-11746118684276.html",
    "bbc.bm/ray-ban-meta-glasses-take-off-but-face-privacy-and-competition-test",
    "techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses-privacy-concerns-after-workers-reviewed-nudity-sex-and-other-footage/",
    "forbesindia.com/article/ai-tracker/why-metas-ray-ban-smart-glasses-are-causing-a-privacy-scandal/2991937/1",
]
# Reuters canonical param-variant (not a new surface per the ?share=twitter precedent).
REUTERS_PARAM_VARIANT = "ray-ban-meta-glasses-take-off-face-privacy-competition-test-2025-12-09/?testcode=t10t1QDsH"


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


def _needle_hits(needle):
    # Per the #715 pattern-rescope lesson: needles are format-built here so
    # no literal mechanism-key strings are carried in the test file; hits in
    # __pycache__ artifacts are excluded as instruments.
    out = subprocess.run(
        ["git", "-C", REPO_ROOT, "grep", "-l", "--", needle, "--", "."],
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    return [p for p in out if "__pycache__" not in p]


class TestNovelty841:
    """Iteration 841 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_841_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_841*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_841_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_841 files, no #841 in git log); this test
        # pins that no duplicate #841 main commit ever appears.
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
            if re.match(r"^[0-9a-f]{40} Type E #841: podcast sentiment", l)
        ]
        assert len(mains) == 1, mains
        anchor = TestRotationCycleGuard841.ANCHORED_SHA
        assert mains[0].startswith(anchor + " "), (anchor, mains)


class TestRotationCycleGuard841:
    """Rotation: 840-844 window, #840 (D) anchors, #841 is the E leg.

    Deselected pre-commit per the #565 followup convention (the #841 main
    commit does not exist yet); patched green in the anchor followup.
    """

    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP_PER_565"  # main commit this run, per #565

    EXPECTED_ORDER = [("E", "841"), ("D", "840"), ("C", "839"), ("B", "838"), ("A", "837")]
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

    def test_window_840_844_second_leg_e(self):
        assert self._window() == self.EXPECTED_ORDER

    def test_rotation_adjacency_cycle_valid(self):
        window = self._window()
        for (t1, _), (t2, _) in zip(window, window[1:]):
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_anchor_sha_matches_head(self):
        mains = _git_log_mains("Type E #841: podcast sentiment")
        assert self.ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
            "PATCH_ME_IN_FOLLOWUP_PER_565",
        ), mains
        assert mains and mains[0].startswith(self.ANCHORED_SHA + " "), mains


class TestGF91stCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #841")[-1]

    def test_500_stands_newest_forty_five_hours_after_796(self):
        section = self._section()
        assert "Episode 500 stands as newest forty-five hours after #796" in section
        assert "(23:00 PDT Sep 16)" in section

    def test_official_site_corroboration_carried_from_796(self):
        section = self._section()
        assert "Official-site corroboration carried from #796" in section
        assert "guiltyfeminist.com/new-normal/" in section

    def test_no_fresh_browser_open_snippet_bounded(self):
        section = self._section()
        assert "no fresh browser.open this run, snippet-bounded method per #796" in section

    def test_uk_podcasts_still_760_latest_sep_16_unverified_unchanged(self):
        section = self._section()
        assert 'still shows 760 episodes / "Latest episode: 2026-09-16"' in section
        assert "UNVERIFIED single-directory signal" in section

    def test_listen_notes_recrawled_7h_caught_up_from_421_lag(self):
        section = self._section()
        assert "re-crawled 7h ago (was 2h at #836)" in section
        assert "now lists The Guilty Feminist 500 at top" in section
        assert "caught up from the 421-lag" in section

    def test_locale_mirrors_stale_preexisting_keys(self):
        section = self._section()
        assert "listennotes.com/nl/" in section
        assert "listennotes.com/pt/" in section

    def test_goloudnow_observed_preexisting_key(self):
        section = self._section()
        assert "deborah-frances-white-on-the-news-meeting-519585" in section
        assert "pre-existing key since #726" in section

    def test_podparadise_still_lags_official_500(self):
        section = self._section()
        assert "top listed 757 / Sep 7, 2026 = 499" in section
        assert "lags official 500" in section

    def test_getpodcast_new_url_key(self):
        section = self._section()
        assert "getpodcast.com/podcast/the-guilty-feminist" in section
        assert "NEW URL KEY" in section

    def test_no_episode_501_next_release_plausibly_near_sep_21(self):
        section = self._section()
        assert "No episode 501 detected anywhere this run" in section
        assert "plausibly near Sep 21" in section

    def test_triggernometry_bounded_absence(self):
        section = self._section()
        assert "Triggernometry clip oVPri0Wr6F0 did not surface this run" in section

    def test_gf_set_accounting_seven_keys_six_known_one_new_zero_meta_content(self):
        section = self._section()
        assert "GF-set: 7 keys observed, 6 previously-logged + 1 new (getpodcast)" in section
        assert "ZERO Meta/wearables content (snippet-bounded)" in section
        for key in GF_KEYS:
            assert key in section, key


class TestEHEHold91stCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #841")[-1]

    def test_forty_six_day_hold_continues(self):
        section = self._section()
        assert "46-day hold continues (Aug 10 -> Sep 18)" in section

    def test_five_keys_four_known_one_new(self):
        section = self._section()
        assert "5 URL keys observed, 4 previously-logged + 1 NEW URL KEY" in section
        for key in EHE_KEYS:
            assert key in section, key

    def test_softonic_new_key_resurface_not_new_motif(self):
        section = self._section()
        assert NEW_EHE_KEYS[0] in section
        assert "NOT a new campaign motif" in section

    def test_no_competitor_equivalent_campaign(self):
        section = self._section()
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 91 cycles." in section


class TestAttentionSphere91stNoMatch:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #841")[-1]

    def test_ninety_first_no_match(self):
        section = self._section()
        assert "ninety-first no-match" in section

    def test_five_github_commit_urls_rejected_circular(self):
        section = self._section()
        assert "(circular, rejected)" in section
        for sha in ("a288c86f0be14694552fea4aa0fd3674cefe93bc",
                    "a2b656f0660e299090803b4dfd7ee01087900c9f",
                    "959038536c82b63a7ab3b708226aec070a43514a",
                    "2c4e21e39a3bb17e74c8afc0bd5b7ad25bda29b4",
                    "25c730ed6097aae952bdf714fe2afe375d8f9e35"):
            assert sha in section, sha

    def test_boz_possible_bounded_absence_this_run(self):
        section = self._section()
        assert '"Possible" iHeart episode (2025-03-26, unrelated wearables-positive Meta-CTO interview; in corpus) did NOT surface this run' in section

    def test_tracked_sources_90_to_91(self):
        section = self._section()
        assert "Tracked Sources 90->91 cycles through Sep 18 2026." in section


class TestPressSurfaces841:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #841")[-1]

    def test_six_results_five_known_plus_param_variant(self):
        section = self._section()
        assert "SIX results observed; 5 previously-logged URL keys + 1 param-variant" in section
        for key in PRESS_KEYS:
            assert key in section, key

    def test_reuters_param_variant_not_new(self):
        section = self._section()
        assert REUTERS_PARAM_VARIANT in section
        assert "param-variant of the logged base key, not a new surface" in section

    def test_frontier_tied_forty_second(self):
        section = self._section()
        assert "TIED at Sep 9 (forty-second consecutive tie after #636 through #836)" in section
        assert "no advance" in section


class TestStandingRules841:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #841")[-1]

    def test_no_tone_scores_standing_rule(self):
        section = self._section()
        assert "tone NOT_SCORED" in section
        assert "p_value/cohens_d NOT_CALCULATED" in section
        assert "is_significant False" in section
        assert "Aug 28 2026" in section

    def test_no_mechanism_added(self):
        section = self._section()
        assert "max numeric mechanism_id 735 (Type E adds none)" in section

    def test_no_analysis_json_update(self):
        section = self._section()
        assert "No analysis.json update warranted" in section

    def test_four_query_sets(self):
        section = self._section()
        assert "4 browser.search query sets this run" in section

    def test_url_key_accounting_18_observed_16_known_2_new(self):
        section = self._section()
        assert "18 external URL keys observed (7 GF + 5 EHE + 6 press)" in section
        assert "16 previously-logged" in section
        assert "2 NEW" in section

    def test_circular_github_urls_rejected(self):
        section = self._section()
        assert "6 github.com own-repo URLs rejected as circular per established discipline, not ingested" in section

    def test_ascii_no_em_dashes(self):
        section = self._section()
        for bad in ("\u2014", "\u2013", "\u201c", "\u201d", "\u2018", "\u2019"):
            assert bad not in section, bad

    def test_test_file_ref(self):
        section = self._section()
        assert "tests/test_type_e_841_podcast_sentiment_91st_verification_sep18_8pm.py" in section


class TestDocSync841:
    def test_readme_row_841(self):
        readme = _read("README.md")
        assert "test_type_e_841_podcast_sentiment_91st_verification_sep18_8pm.py" in readme

    def test_readme_row_841_in_table(self):
        readme = _read("README.md")
        assert "| `test_type_e_841_podcast_sentiment_91st_verification_sep18_8pm.py` |" in readme

    def test_architecture_row_841(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "test_type_e_841_podcast_sentiment_91st_verification_sep18_8pm.py" in arch

    def test_architecture_lists_841_file(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "tests/test_type_e_841_podcast_sentiment_91st_verification_sep18_8pm.py" in arch


class TestIterationLog841:
    def test_log_entry_present(self):
        log = _read("iteration-log.md")
        assert "Type E #841" in log
        assert "podcast sentiment 91st verification" in log

    def test_log_cycle_and_hour(self):
        log = _read("iteration-log.md")
        assert "Sep 18 2026, 20:00 PDT" in log
        assert "840-844 window" in log


class TestDateGrounding841:
    def test_sep_18_2026_is_friday(self):
        import datetime
        assert datetime.date(2026, 9, 18).strftime("%A") == "Friday"
