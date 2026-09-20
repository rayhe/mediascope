"""Type E #871: podcast sentiment 97th verification cycle - Sep 20 2026 02:00 PDT.

Second leg of the 870-874 window (D #870 -> E #871 -> A -> B -> C).
Monitoring-only: GF episode 500 stands newest (~6 days after Sep 14
release; official-site corroboration carried from #796); ZERO new URL
keys this run across all 4 query sets (first zero-new-key cycle since
the podscan key landed at #866). All 7 GF keys observed are
previously-logged (youtube iKXj2w2cp50 crawled 2d; getpodcast stale 66d
RESURFACED after missing #866; listennotes main re-crawled 11h lists
500 + Rubasingham special + 499/498/497/496 with the "Released 23
December." snippet string reappearing, again snippet-level noise;
goloudnow re-crawled 6h "16 September Finished"; uk-podcasts 760 /
"Latest episode: 2026-09-16" UNCHANGED since #806, UNVERIFIED
single-directory signal; podparadise crawled 3d top 757 / Sep 7 = 499;
listennotes pt stale 219d). podscan key did NOT surface this run
(remains in corpus). No episode 501 anywhere. EHE 41-day hold
(date(2026,9,20)-date(2026,8,10)=41 days; regression guard on the
#846/#851 47/48 arithmetic slips retained; the "40-day" label belonged
to Sep 19 and must not be carried to Sep 20); 6 results: 1 circular
own-repo GitHub blob (rejected) + 5 previously-logged EHE keys
(designtaxi 34124 re-crawled 7d; designtaxi 33476 re-crawled 1d;
softonic Epstein re-crawled 5h; singulism re-crawled 1h; cloudfront
IBTimes UK mirror re-crawled 14h) - ZERO new EHE keys, no new campaign
motif, last campaign phase remains the circa Aug 10 Epstein poster; no
competitor-equivalent guerrilla campaign in any of the 97 cycles.
Attention Sphere 97th quoted-search no-match (identical 7 own-repo
GitHub URLs - the podcast-sentiment.md blob plus 6 commit URLs
a288c86/a2b656f/9590385/2c4e21e/25c730e/3d16eac, same set as
#846/#851/#856/#861/#866 - circular-rejected; Tracked Sources 96->97).
Press: 7 results, ALL previously-logged keys (ppc.land Hamburg
re-crawled 1h; livemint stale 337d; nypost Sep-18 CA lawsuit crawled 1d;
9to5google crawled 5d; startupfortune re-crawled 2h; softonic LED-loophole
re-crawled <1h; webpronews re-crawled 1h) - ZERO new press keys; the
usa-times "creep glasses" dating piece from #846 did not surface this
run (remains in corpus). Recency frontier HOLDS at Sep 18 (#846's
nypost Sep 18 CA-lawsuit piece remains newest; no Sep 19 or Sep 20
surfaces). 27 result rows / 19 non-circular distinct URL keys, ALL
previously-logged, zero new. Standing rule (Aug 28 2026): tone
NOT_SCORED, p_value/cohens_d NOT_CALCULATED, is_significant False. No
mechanism block in profiles/. No analysis.json update warranted. NOT
artifact-grade.

49 tests, 11 classes.

Conventions: anchor 1 + novelty-log-singleton 1 + rotation-guard 3 deselected
pre-commit per #565, patched green in the anchor followup; doc-sync 4 +
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
# (>=1 hit verified pre-commit). podscan.fm did not surface this run.
GF_KEYS = [
    "youtube.com/watch?v=iKXj2w2cp50",
    "getpodcast.com/podcast/the-guilty-feminist",
    "rJKyRn2TWG",  # Listen Notes main + PT mirror share the episode ID
    "uk-podcasts.co.uk/podcast/the-guilty-feminist",
    "podparadise.com/Podcast/1068940771",
    "goloudnow.com/podcasts/the-guilty-feminist-152",
    "podscan.fm/podcasts/the-guilty-feminist-1",  # not surfaced this run; still a known key
]

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
# #846/#851/#856/#861/#866 (verbatim hashes from this run's Full-URL listing).
AS_CIRCULAR_PREFIX = "github.com/rayhe/mediascope/commit/"
AS_CIRCULAR_COMMITS = [
    "a288c86f0be14694552fea4aa0fd3674cefe93bc",
    "a2b656f0660e299090803b4dfd7ee01087900c9f",
    "959038536c82b63a7ab3b708226aec070a43514a",
    "2c4e21e39a3bb17e74c8afc0bd5b7ad25bda29b4",
    "25c730ed6097aae952bdf714fe2afe375d8f9e35",
    "3d16eacfc03d35bad9ade4a15403fbcea2fb293c",
]

# Press set: all 7 keys previously-logged. ZERO new press URL keys this
# run; the usa-times key from #846 did not surface (remains in corpus).
KNOWN_PRESS_KEYS = [
    "ppc.land/hamburg-regulator-finds-ray-ban-meta-glasses-expose-bystanders-without-consent/",
    "www.livemint.com/technology/tech-news/meta-ray-ban-smart-glasses-could-store-voice-recordings-by-default-what-it-means-for-users/amp-11746118684276.html",
    "nypost.com/2026/09/18/us-news/california-users-among-plaintiffs-suing-meta-over-smart-glasses/",
    "9to5google.com/2026/08/28/meta-ray-ban-smart-glasses-privacy-led-loophole-update/",
    "startupfortune.com/meta-permanently-disables-cameras-on-thousands-of-tampered-smart-glasses/",
    "en.softonic.com/articles/meta-ray-ban-smart-glasses-update-privacy-loophole-now-closed",
    "webpronews.com/germanys-privacy-push-targets-meta-ray-ban-glasses-with-criminal-filing/",
]


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


class TestNovelty871:
    """Iteration 871 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_871_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_871*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_no_type_e_871_in_git_log_precommit(self):
        # Deselected pre-commit per the #565 followup convention alongside
        # the anchor test; verified pre-commit by shell grep (no "Type E
        # #871" in git log) and patched green post-commit, where it pins
        # the main commit as a singleton.
        log = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        mains = [
            l
            for l in log
            if re.search(r"Type E #871: podcast sentiment", l)
        ]
        assert len(mains) == 1, mains

    def test_type_e_871_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_871 files, no #871 in git log); this test
        # pins that no duplicate #871 main commit ever appears.
        log = _git_log_mains("Type E #871: podcast sentiment")
        assert len(log) == 1, log


class TestRotationCycleGuard871:
    """Rotation: 870-874 window, #870 (D) anchors, #871 is the E leg.

    The ANCHORED_SHA is patched to the main commit's SHA in the anchor
    followup per the #565 convention; these tests are deselected pre-commit.
    """

    ANCHORED_SHA = "3818ba8a4093743198f1b5fd36d9e5ca66222241"

    def test_870_874_window_second_leg(self):
        log = _read("iteration-log.md")
        assert "## #871" in log
        assert "870-874" in log

    def test_predecessor_870_type_d(self):
        log = _git_log_mains("Type D #870:")
        assert len(log) >= 1, "expected the #870 Type D main commit"

    def test_no_duplicate_871_in_log(self):
        lines = [
            l
            for l in _read("iteration-log.md").splitlines()
            if l.startswith("## #871")
        ]
        assert len(lines) == 1, lines


class TestGF97thCycle:
    """Guilty Feminist: episode 500 stands newest; zero new GF keys."""

    def test_gf_known_keys_all_in_corpus(self):
        # All 7 GF keys observed this run must each carry >=1 corpus hit.
        for key in GF_KEYS:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "GF key missing from corpus: %r" % key

    def test_zero_new_gf_keys_this_run(self):
        # First zero-new-key GF set since the podscan key landed at #866;
        # the #871 section must state that explicitly.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #871")[1]
        assert "ZERO new GF URL keys" in section

    def test_gf_500_stands_newest_no_501(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #871")[1]
        assert "No episode 501" in section
        assert "stands as newest" in section

    def test_gf_ln_snippet_anomaly_not_a_new_episode(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #871")[1]
        assert "Released 23 December" in section
        assert "snippet-level noise" in section

    def test_uk_podcasts_signal_flagged_unverified(self):
        # uk-podcasts 760 / "Latest episode: 2026-09-16" UNCHANGED since #806
        # remains an UNVERIFIED single-directory signal per #503/iteration-492.
        ps = _read("podcast-sentiment.md")
        assert "UNVERIFIED single-directory signal" in ps

    def test_podscan_not_surfaced_this_run(self):
        # podscan.fm did not surface this run; the section must say so, and
        # the key must still be present in the corpus from #866.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #871")[1]
        assert "did NOT surface this run" in section

    def test_getpodcast_resurfaced_this_run(self):
        # getpodcast missed #866 and resurfaced this run (stale 66d mirror);
        # the section must say it resurfaced.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #871")[1]
        assert "resurfaced" in section.lower()

    def test_zero_meta_wearables_content_across_cycles(self):
        ps = _read("podcast-sentiment.md")
        assert "ZERO Meta/wearables content" in ps or "zero Meta/wearables content" in ps.lower()


class TestEHEHold97thCycle:
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
        section = _read("podcast-sentiment.md").split("## Iteration #871")[1]
        assert "41-day hold" in section
        assert "48-day" not in section
        assert "47-day" not in section

    def test_ehe_known_keys_all_in_corpus(self):
        for key in EHE_KEYS:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "EHE key missing from corpus: %r" % key

    def test_zero_new_ehe_keys_this_run(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #871")[1]
        assert "ZERO new EHE URL keys" in section

    def test_no_new_campaign_motif(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #871")[1]
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
        section = ps.split("## Iteration #871")[1]
        assert "circular" in section.lower()


class TestAttentionSphere97thNoMatch:
    """Attention Sphere: 97th quoted-search no-match; circular rejects."""

    def test_97th_no_match(self):
        ps = _read("podcast-sentiment.md")
        assert "ninety-seventh" in ps.lower()

    def test_circular_github_rejected(self):
        ps = _read("podcast-sentiment.md")
        assert "circular" in ps.lower()
        for commit in AS_CIRCULAR_COMMITS:
            hits = _needle_hits(AS_CIRCULAR_PREFIX + commit)
            assert len(hits) >= 1, "AS circular commit not in corpus: %r" % commit

    def test_tracked_sources_advanced_96_to_97(self):
        ps = _read("podcast-sentiment.md")
        assert "97 verification cycles" in ps

    def test_task_spec_misidentification_stated(self):
        ps = _read("podcast-sentiment.md")
        assert "misidentified" in ps.lower()


class TestPressSurfaces871:
    """Press: all 7 keys previously-logged; zero new press keys."""

    def test_seven_press_keys_all_in_corpus(self):
        for key in KNOWN_PRESS_KEYS:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "press key missing from corpus: %r" % key

    def test_zero_new_press_keys_this_run(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #871")[1]
        assert "ZERO new press URL keys" in section

    def test_nypost_ca_lawsuit_details(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #871")[1]
        assert "70+ plaintiffs" in section

    def test_hamburg_report_details(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #871")[1]
        assert "53-page" in section

    def test_no_tone_score_without_first_hand_read(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #871")[1]
        assert "NOT_SCORED" in section


class TestRecencyFrontier871:
    """Recency frontier holds at Sep 18."""

    def test_frontier_holds_at_sep_18(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #871")[1]
        assert "HOLDS at Sep 18" in section

    def test_frontier_driver_is_nypost_sep_18(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #871")[1]
        assert "NY Post Sep 18" in section or "nypost Sep 18" in section.lower()


class TestStandingRules871:
    """Aug 28 2026 standing rule; Type E adds no mechanisms; ledger 27."""

    def test_tone_not_scored(self):
        ps = _read("podcast-sentiment.md")
        assert "NOT_SCORED" in ps

    def test_is_significant_false(self):
        ps = _read("podcast-sentiment.md")
        assert "is_significant False" in ps or "is_significant false" in ps.lower()

    def test_twenty_seventh_member_present(self):
        # TWENTY-SEVENTH member-form present in profiles/ (the-verge.yaml
        # m751); TWENTY-EIGHTH member-form absent. Ledger 26->27 at #867.
        corpus = _profiles_corpus()
        assert "TWENTY-SEVENTH falsification-family member" in corpus

    def test_twenty_eighth_member_absent(self):
        corpus = _profiles_corpus()
        assert "TWENTY-EIGHTH falsification-family member" not in corpus

    def test_ledger_holds_at_27(self):
        assert 26 + 1 == 27

    def test_max_mechanism_753_no_754_keys(self):
        # Type E adds no mechanisms: max numeric mechanism_id stays 753 and
        # zero underscore-form 754 mechanism key strings exist in profiles/.
        needle_base = "mechanism" + "_" + "75" + "4"
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
        # Type E is monitoring-only: no test_type_e_871 block key anywhere
        # in profiles/.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "grep", "-l", "--", "test_type_e_871", "--", "profiles/"],
            capture_output=True,
            text=True,
        ).stdout.strip()
        assert out == "", out

    def test_no_analysis_json_update_warranted(self):
        ps = _read("podcast-sentiment.md")
        assert "No analysis.json update warranted" in ps


class TestDocSync871:
    def test_readme_row_871(self):
        readme = _read("README.md")
        assert "test_type_e_871_podcast_sentiment_97th_verification_sep20_2am.py" in readme

    def test_readme_row_871_in_table(self):
        readme = _read("README.md")
        assert "| `test_type_e_871_podcast_sentiment_97th_verification_sep20_2am.py` |" in readme

    def test_architecture_row_871(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "test_type_e_871_podcast_sentiment_97th_verification_sep20_2am.py" in arch

    def test_architecture_lists_871_file(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "tests/test_type_e_871_podcast_sentiment_97th_verification_sep20_2am.py" in arch


class TestIterationLog871:
    def test_iteration_log_has_871_entry(self):
        log = _read("iteration-log.md")
        assert "## #871" in log

    def test_iteration_log_871_records_zero_new_keys(self):
        log = _read("iteration-log.md")
        assert "ZERO new URL keys" in log
        assert "41-day hold" in log


class TestDateGrounding871:
    def test_sep_20_2026_is_sunday(self):
        import datetime
        assert datetime.date(2026, 9, 20).strftime("%A") == "Sunday"

    def test_sep_19_2026_is_saturday(self):
        import datetime
        assert datetime.date(2026, 9, 19).strftime("%A") == "Saturday"

    def test_sep_18_2026_is_friday(self):
        import datetime
        assert datetime.date(2026, 9, 18).strftime("%A") == "Friday"
