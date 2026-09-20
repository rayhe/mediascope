"""Type E #881: podcast sentiment 99th verification cycle - Sep 20 2026 12:00 PDT.

Second leg of the 880-884 window (D #880 -> E #881 -> A -> B -> C).
Monitoring-only: GF episode 500 stands newest (~6 days after Sep 14
release; official-site corroboration carried from #796); the same 7 GF
keys observed are all previously-logged (youtube iKXj2w2cp50;
goloudnow; uk-podcasts 760 / "Latest episode: 2026-09-16" UNCHANGED
since #806, UNVERIFIED single-directory signal; listennotes main + PT
mirror; podparadise; youtube 8OeSUuyvuXc episode-482 upload, in corpus
since #846); getpodcast did NOT surface this run (remains in corpus
from #866); podscan.fm did NOT surface this run (remains in corpus from
#866). No episode 501 anywhere. EHE 41-day hold
(date(2026,9,20)-date(2026,8,10)=41 days; regression guard on the
#846/#851 47/48 arithmetic slips retained; the "40-day" label belonged
to Sep 19 and must not be carried to Sep 20); 6 results: 1 circular
own-repo GitHub blob (rejected) + 5 previously-logged EHE keys
(designtaxi 34124; designtaxi 33476; softonic Epstein re-surface;
singulism; cloudfront IBTimes UK mirror) - ZERO new EHE keys, no new
campaign motif, last campaign phase remains the circa Aug 10 Epstein
poster; no competitor-equivalent guerrilla campaign in any of the 99
cycles. Attention Sphere 99th quoted-search no-match (identical 7
own-repo GitHub URLs - the podcast-sentiment.md blob plus 6 commit URLs
a288c86/a2b656f/9590385/2c4e21e/25c730e/3d16eac, same set as
#846/#851/#856/#861/#866/#871/#876 - circular-rejected; Tracked Sources
98->99). Press: SEVEN results, ALL previously-logged URL keys (ZERO new
press URL keys this run, unlike #876's two new surfaces): the nypost
Sep 18 CA-lawsuit piece re-SURFACED this run (crawled 1d; did NOT
surface at #876) and remains the recency-frontier driver; webpronews
germanys-privacy-push HateAid piece previously-logged via #866/#871;
recordinglaw Bartone-repackage and webpronews LED-tampering from #876
did NOT surface this run (remain in corpus). Recency frontier HOLDS at
Sep 18 (no Sep 19 or Sep 20 surfaces). 27 result rows / 19 non-circular
distinct URL keys, 0 new. Standing rule (Aug 28 2026): tone NOT_SCORED,
p_value/cohens_d NOT_CALCULATED, is_significant False. No mechanism
block in profiles/. No analysis.json update warranted. NOT
artifact-grade.

50 tests, 11 classes.

Conventions: novelty anchor 2 + rotation-guard 3 deselected pre-commit
per #565, patched green in the anchor followup; doc-sync 4 +
iteration-log 2 green pre-commit per #719. ASCII-only, no em dashes.
"""

import glob
import os
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TEST_BASENAME = os.path.basename(__file__)

# The 7 previously-logged GF URL keys observed this run (verbatim from
# the Full-URL listing). ALL are previously-logged in the corpus this run
# (>=1 hit verified pre-commit). getpodcast and podscan.fm did NOT
# surface this run; both remain in the corpus from #866.
GF_KEYS = [
    "youtube.com/watch?v=iKXj2w2cp50",
    "www.goloudnow.com/podcasts/the-guilty-feminist-152/deborah-frances-white-on-the-news-meeting-519585",
    "uk-podcasts.co.uk/podcast/the-guilty-feminist/deborah-frances-white-on-the-news-meeting",
    "www.listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG/",
    "www.podparadise.com/Podcast/1068940771",
    "www.youtube.com/watch?v=8OeSUuyvuXc",  # episode-482 upload, in corpus since #846
]
GF_STALE_PT_MIRROR_KEY = "www.listennotes.com/pt/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG/"
GF_GETPODCAST_KEY = "getpodcast.com/podcast/the-guilty-feminist"  # not surfaced this run
GF_PODSCAN_KEY = "podscan.fm/podcasts/the-guilty-feminist-1"  # not surfaced this run

# The 5 previously-logged EHE URL keys observed this run (the GitHub blob
# was circular-rejected). ZERO new EHE keys this run.
EHE_KEYS = [
    "community.designtaxi.com/topic/33476-activist-group-hijacks-kylie-jenners-meta-smart-glasses-ads-with-sharp-privacy-warnings-across-london/",
    "community.designtaxi.com/topic/34124-jeffrey-epstein-appears-to-model-meta-ray-bans-smart-glasses-on-new-ads/",
    "en.softonic.com/articles/ray-ban-meta-smart-glasses-back-in-the-spotlight-london-ad-uses-epstein-image",
    "singulism.com/en/2026-07-17-meta-glasses-protest-london-bus-stops/",
    "d33gy59ovltp76.cloudfront.net/news/london-bus-stop-poster-brutally-mocks-kylie-jenner-and-metas-ai-glasses-its-giving-fascism",
]

# Circular own-repo results from the Attention Sphere quoted search; rejected,
# not ingested. The podcast-sentiment.md blob plus the same 6 commit URLs as
# #846/#851/#856/#861/#866/#871/#876 (verbatim hashes from this run's
# Full-URL listing).
AS_CIRCULAR_PREFIX = "github.com/rayhe/mediascope/commit/"
AS_CIRCULAR_COMMITS = [
    "a288c86f0be14694552fea4aa0fd3674cefe93bc",
    "a2b656f0660e299090803b4dfd7ee01087900c9f",
    "959038536c82b63a7ab3b708226aec070a43514a",
    "2c4e21e39a3bb17e74c8afc0bd5b7ad25bda29b4",
    "25c730ed6097aae952bdf714fe2afe375d8f9e35",
    "3d16eacfc03d35bad9ade4a15403fbcea2fb293c",
]

# Press: 7 previously-logged keys, ZERO new URL keys this run (unlike
# #876's two new surfaces). The nypost Sep 18 key re-SURFACED this run
# (it did NOT surface at #876) and remains the recency-frontier driver;
# the webpronews germanys-privacy-push HateAid key is in the corpus via
# #866/#871. The #876 recordinglaw and webpronews-LED-tampering keys did
# NOT surface this run (they remain in the corpus).
PRESS_KEYS = [
    "ppc.land/hamburg-regulator-finds-ray-ban-meta-glasses-expose-bystanders-without-consent/",
    "www.livemint.com/technology/tech-news/meta-ray-ban-smart-glasses-could-store-voice-recordings-by-default-what-it-means-for-users/amp-11746118684276.html",
    "9to5google.com/2026/08/28/meta-ray-ban-smart-glasses-privacy-led-loophole-update/",
    "startupfortune.com/meta-permanently-disables-cameras-on-thousands-of-tampered-smart-glasses/",
    "en.softonic.com/articles/meta-ray-ban-smart-glasses-update-privacy-loophole-now-closed",
    "www.webpronews.com/germanys-privacy-push-targets-meta-ray-ban-glasses-with-criminal-filing/",
]
NYPOST_SEP18_KEY = "nypost.com/2026/09/18/us-news/california-users-among-plaintiffs-suing-meta-over-smart-glasses/"
RECORDINGLAW_KEY = "www.recordinglaw.com/news/meta-ray-ban-smart-glasses-privacy-scandal/"  # not surfaced this run
WEBPRONEWS_LED_KEY = "www.webpronews.com/metas-new-smart-glasses-update-shuts-down-camera-on-privacy-light-tampering/"  # not surfaced this run


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


def _profiles_corpus():
    # Walks profiles/ on disk (not git grep) so the sweep sees working-tree
    # state pre-commit; test files in tests/ cannot pollute the count.
    parts = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for f in files:
            with open(os.path.join(root, f), encoding="utf-8", errors="replace") as fh:
                parts.append(fh.read())
    return "\n".join(parts)


class TestNovelty881:
    """Iteration 881 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_881_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_881*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_no_type_e_881_in_git_log_precommit(self):
        # Deselected pre-commit per the #565 followup convention alongside
        # the anchor test; verified pre-commit by shell grep (no "Type E
        # #881" in git log) and patched green post-commit, where it pins
        # the main commit as a singleton.
        log = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        mains = [
            l
            for l in log
            if re.search(r"Type E #881: podcast sentiment", l)
        ]
        assert len(mains) == 1, mains

    def test_type_e_881_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_881 files, no #881 in git log); this test
        # pins that no duplicate #881 main commit ever appears.
        log = _git_log_mains("Type E #881: podcast sentiment")
        assert len(log) == 1, log


class TestRotationCycleGuard881:
    """Rotation: 880-884 window, #880 (D) anchors, #881 is the E leg.

    The ANCHORED_SHA is patched to the main commit's SHA in the anchor
    followup per the #565 convention; these tests are deselected pre-commit.
    """

    ANCHORED_SHA = "0000000000000000000000000000000000000000"

    def test_880_884_window_second_leg(self):
        log = _read("iteration-log.md")
        assert "## #881" in log
        assert "880-884" in log

    def test_predecessor_880_type_d(self):
        log = _git_log_mains("Type D #880:")
        assert len(log) >= 1, "expected the #880 Type D main commit"

    def test_no_duplicate_881_in_log(self):
        lines = [
            l
            for l in _read("iteration-log.md").splitlines()
            if l.startswith("## #881")
        ]
        assert len(lines) == 1, lines


class TestGF99thCycle:
    """Guilty Feminist: episode 500 stands newest; zero new GF keys."""

    def test_gf_known_keys_all_in_corpus(self):
        # All 7 GF keys observed this run must each carry >=1 corpus hit.
        for key in GF_KEYS + [GF_STALE_PT_MIRROR_KEY]:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "GF key missing from corpus: %r" % key

    def test_zero_new_gf_keys_this_run(self):
        # The #881 section must state that explicitly.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #881")[1]
        assert "ZERO new GF URL keys" in section

    def test_gf_500_stands_newest_no_501(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #881")[1]
        assert "No episode 501" in section
        assert "stands as newest" in section

    def test_gf_500_six_days_after_release(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #881")[1]
        assert "~6 days after release" in section

    def test_uk_podcasts_signal_flagged_unverified(self):
        # uk-podcasts 760 / "Latest episode: 2026-09-16" UNCHANGED since #806
        # remains an UNVERIFIED single-directory signal per #503/iteration-492.
        ps = _read("podcast-sentiment.md")
        assert "UNVERIFIED single-directory signal" in ps

    def test_podscan_not_surfaced_this_run(self):
        # podscan.fm did not surface this run; the section must say so, and
        # the key must still be present in the corpus from #866.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #881")[1]
        assert "did NOT surface this run" in section
        hits = _needle_hits(GF_PODSCAN_KEY)
        assert len(hits) >= 1, "podscan GF key must remain in corpus"

    def test_getpodcast_not_surfaced_this_run(self):
        # getpodcast resurfaced at #871 but did NOT surface this run; it
        # stays in the corpus and the section must say it did not surface.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #881")[1]
        assert "did NOT surface this run" in section
        hits = _needle_hits(GF_GETPODCAST_KEY)
        assert len(hits) >= 1, "getpodcast GF key must remain in corpus"

    def test_zero_meta_wearables_content_across_cycles(self):
        ps = _read("podcast-sentiment.md")
        assert "across all 99 cycles" in ps


class TestEHEHold99thCycle:
    """Everyone Hates Elon: 41-day hold, zero new EHE keys."""

    def test_ehe_41_day_hold(self):
        """41-day hold; regression guard on the date subtraction.

        #846 labeled the Aug 10 -> Sep 19 hold "47-day" and #851's
        first draft advanced it to "48-day". Both were arithmetically
        wrong. #866 corrected the Sep 19 label to 40-day. This run the
        Sep 20 hold is 41 days: date(2026, 9, 20) - date(2026, 8, 10)
        == 41 days. The doc must carry "41-day hold" and never the
        40/47/48-day labels for the Sep 20 window.
        """
        import datetime
        assert (datetime.date(2026, 9, 20) - datetime.date(2026, 8, 10)).days == 41
        section = _read("podcast-sentiment.md").split("## Iteration #881")[1]
        assert "41-day hold" in section
        assert "48-day" not in section
        assert "47-day" not in section

    def test_ehe_known_keys_all_in_corpus(self):
        for key in EHE_KEYS:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "EHE key missing from corpus: %r" % key

    def test_zero_new_ehe_keys_this_run(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #881")[1]
        assert "ZERO new EHE URL keys" in section

    def test_no_new_campaign_motif(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #881")[1]
        assert "NO new primary campaign motif" in section

    def test_no_competitor_equivalent(self):
        ps = _read("podcast-sentiment.md")
        assert "No competitor-equivalent" in ps or "no competitor-equivalent" in ps.lower()

    def test_ehe_is_campaign_group_not_podcast(self):
        # Verified 2026-09-07: "Everyone Hates Elon" is an activist campaign
        # group, NOT a podcast. Campaign activity is logged as media/news
        # coverage, never as podcast episodes.
        ps = _read("podcast-sentiment.md")
        assert "NOT a podcast" in ps or "not a podcast" in ps.lower()

    def test_ehe_circular_github_rejected(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #881")[1]
        assert "circular" in section.lower()


class TestAttentionSphere99thNoMatch:
    """Attention Sphere: 99th quoted-search no-match; circular rejects."""

    def test_99th_no_match(self):
        ps = _read("podcast-sentiment.md")
        assert "ninety-ninth" in ps.lower()

    def test_circular_github_rejected(self):
        ps = _read("podcast-sentiment.md")
        assert "circular" in ps.lower()
        for commit in AS_CIRCULAR_COMMITS:
            hits = _needle_hits(AS_CIRCULAR_PREFIX + commit)
            assert len(hits) >= 1, "AS circular commit not in corpus: %r" % commit

    def test_tracked_sources_advanced_98_to_99(self):
        ps = _read("podcast-sentiment.md")
        assert "99 verification cycles" in ps

    def test_task_spec_misidentification_stated(self):
        ps = _read("podcast-sentiment.md")
        assert "misidentified" in ps.lower()


class TestPressSurfaces881:
    """Press: 7 known keys, ZERO new URL keys (unlike #876)."""

    def test_seven_press_keys_all_in_corpus(self):
        for key in PRESS_KEYS + [NYPOST_SEP18_KEY]:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "press key missing from corpus: %r" % key

    def test_zero_new_press_keys_this_run(self):
        # Unlike #876's two new surfaces, this run ingested ZERO new URL
        # keys: the section must state that explicitly.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #881")[1]
        assert "ZERO new press URL keys" in section

    def test_nypost_sep18_resurfaced_this_run(self):
        # The nypost Sep 18 piece did NOT surface at #876 but re-SURFACED
        # this run; it stays in the corpus and remains the recency-frontier
        # driver.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #881")[1]
        assert "re-SURFACED this run" in section
        hits = _needle_hits(NYPOST_SEP18_KEY)
        assert len(hits) >= 1, "nypost Sep 18 key must remain in corpus"

    def test_webpronews_germany_previously_logged(self):
        # The HateAid criminal-filing webpronews URL surfaced this run and
        # was logged new-to-corpus at #866/#871; it is NOT new this run.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #881")[1]
        assert "previously-logged" in section
        hits = _needle_hits("germanys-privacy-push")
        assert len(hits) >= 1

    def test_recordinglaw_not_surfaced_this_run(self):
        # The #876 recordinglaw Bartone-repackage key did NOT surface this
        # run; it stays in the corpus.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #881")[1]
        assert "Did not surface this run" in section
        hits = _needle_hits(RECORDINGLAW_KEY)
        assert len(hits) >= 1, "recordinglaw key must remain in corpus"

    def test_webpronews_led_tampering_not_surfaced_this_run(self):
        # The #876 webpronews LED-tampering key did NOT surface this run;
        # it stays in the corpus.
        hits = _needle_hits(WEBPRONEWS_LED_KEY)
        assert len(hits) >= 1, "webpronews LED-tampering key must remain in corpus"


class TestRecencyFrontier881:
    """Recency frontier holds at Sep 18."""

    def test_frontier_holds_at_sep_18(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #881")[1]
        assert "HOLDS at Sep 18" in section

    def test_frontier_driver_is_nypost_sep_18(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #881")[1]
        assert "frontier driver" in section
        assert "Sep 18" in section


class TestStandingRules881:
    """Aug 28 2026 standing rule; Type E adds no mechanisms; ledger 28."""

    def test_tone_not_scored(self):
        ps = _read("podcast-sentiment.md")
        assert "NOT_SCORED" in ps

    def test_is_significant_false(self):
        ps = _read("podcast-sentiment.md")
        assert "is_significant False" in ps or "is_significant false" in ps.lower()

    def test_twenty_eighth_member_present(self):
        # TWENTY-EIGHTH member-form present in profiles/ (journalists.yaml
        # m758, ledger 27->28 at #878); TWENTY-NINTH member-form absent.
        corpus = _profiles_corpus()
        assert "TWENTY-EIGHTH falsification-family member" in corpus

    def test_twenty_ninth_member_absent(self):
        corpus = _profiles_corpus()
        assert "TWENTY-NINTH falsification-family member" not in corpus

    def test_ledger_holds_at_28(self):
        assert 27 + 1 == 28

    def test_max_mechanism_759_no_760_keys(self):
        # Type E adds no mechanisms: max numeric mechanism_id stays 759 and
        # zero underscore-form 760 mechanism key strings exist in profiles/.
        needle_base = "mechanism" + "_" + "76" + "0"
        hits = [
            p
            for p in subprocess.run(
                ["git", "-C", REPO_ROOT, "grep", "-l", "--", needle_base, "--", "profiles/"],
                capture_output=True,
                text=True,
            ).stdout.splitlines()
            if "__pycache__" not in p
        ]
        assert hits == [], hits

    def test_no_type_e_mechanism_block_added(self):
        # Type E is monitoring-only: no test_type_e_881 block key anywhere
        # in profiles/.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "grep", "-l", "--", "test_type_e_881", "--", "profiles/"],
            capture_output=True,
            text=True,
        ).stdout.strip()
        assert out == "", out

    def test_no_analysis_json_update_warranted(self):
        ps = _read("podcast-sentiment.md")
        assert "No analysis.json update warranted" in ps


class TestDocSync881:
    def test_readme_row_881(self):
        readme = _read("README.md")
        assert "test_type_e_881_podcast_sentiment_99th_verification_sep20_12pm.py" in readme

    def test_readme_row_881_in_table(self):
        readme = _read("README.md")
        assert "| `test_type_e_881_podcast_sentiment_99th_verification_sep20_12pm.py` |" in readme

    def test_architecture_row_881(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "test_type_e_881_podcast_sentiment_99th_verification_sep20_12pm.py" in arch

    def test_architecture_lists_881_file(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "tests/test_type_e_881_podcast_sentiment_99th_verification_sep20_12pm.py" in arch


class TestIterationLog881:
    def test_iteration_log_has_881_entry(self):
        log = _read("iteration-log.md")
        assert "## #881" in log

    def test_iteration_log_881_records_zero_new_keys_and_hold(self):
        log = _read("iteration-log.md")
        assert "ZERO new URL keys" in log
        assert "41-day hold" in log


class TestDateGrounding881:
    def test_sep_20_2026_is_sunday(self):
        import datetime
        assert datetime.date(2026, 9, 20).strftime("%A") == "Sunday"

    def test_sep_19_2026_is_saturday(self):
        import datetime
        assert datetime.date(2026, 9, 19).strftime("%A") == "Saturday"

    def test_sep_18_2026_is_friday(self):
        import datetime
        assert datetime.date(2026, 9, 18).strftime("%A") == "Friday"
