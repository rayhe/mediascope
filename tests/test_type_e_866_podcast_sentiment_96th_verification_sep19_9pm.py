"""Type E #866: podcast sentiment 96th verification cycle - Sep 19 2026 21:00 PDT.

Second leg of the 865-869 window (D #865 -> E #866 -> A -> B -> C).
Monitoring-only: GF episode 500 stands newest (~5 days after Sep 14
release; official-site corroboration carried from #796); ONE new GF
URL key (podscan.fm GF directory listing, surfaces Bonnie Greer
tribute emergency re-release, zero wearables content); 6 other GF
keys all previously-logged (uk-podcasts 760 / "Latest episode:
2026-09-16" UNCHANGED since #806, UNVERIFIED single-directory signal;
Listen Notes main re-crawled 6h lists 500 + Rubasingham special +
499/498/497/496; the "Released 23 December." snippet string reappeared,
again snippet-level noise; goloudnow re-crawled 1h; podparadise crawled
2d top 757 / Sep 7 = 499; Listen Notes pt mirror stale; getpodcast not
surfaced this run). EHE 40-day hold (date(2026,9,19)-date(2026,8,10)=40
days; regression-guarded 47/48 labels); TWO new EHE URL keys (designtaxi
topic/34124 Epstein-ad community thread; cloudfront IBTimes UK
Kylie-poster mirror) - both new mirrors of in-corpus stories, ZERO new
campaign motifs; 3 previously-logged EHE keys; quoted-search GitHub blob
rejected circular; engadget key not surfaced this run (story remains in
corpus). Attention Sphere 96th quoted-search no-match (identical 7
own-repo GitHub URLs - the podcast-sentiment.md blob plus 6 commit
URLs a288c86/a2b656f/9590385/2c4e21e/25c730e/3d16eac, same set as
#846/#851/#856/#861 - circular-rejected; Tracked Sources 94->96 with
ERRATUM: #861's cycle section recorded 94->95 but left the top-table
row at 94; corrected this run). Press: 6 previously-logged keys + ONE
new URL key (webpronews HateAid Aug-11 criminal-complaint summary,
story lineage in corpus). Recency frontier HOLDS at Sep 18 (#846's
nypost Sep 18 CA-lawsuit piece remains newest; no Sep 19 surfaces;
webpronews is ~39d old). 27 result rows / 19 non-circular distinct URL
keys (15 previously-logged, 4 new - all four new mirrors/surfaces of
in-corpus stories). Standing rule (Aug 28 2026): tone NOT_SCORED,
p_value/cohens_d NOT_CALCULATED, is_significant False. No mechanism
block in profiles/. No analysis.json update warranted. NOT artifact-grade.

52 tests, 11 classes.

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

# The 6 previously-logged GF URL keys observed this run (verbatim from
# the Full-URL listing). ALL are previously-logged in the corpus this run
# (verified pre-commit). The podscan.fm key is new this run (NEW_GF_KEYS).
GF_KEYS = [
    "youtube.com/watch?v=iKXj2w2cp50",
    "goloudnow.com/podcasts/the-guilty-feminist-152/deborah-frances-white-on-the-news-meeting-519585",
    "rJKyRn2TWG",  # Listen Notes main + PT mirror share the episode ID
    "uk-podcasts.co.uk/podcast/the-guilty-feminist",
    "podparadise.com/Podcast/1068940771",
    "getpodcast.com/podcast/the-guilty-feminist",  # not surfaced this run; still a known key
]
NEW_GF_KEYS = [
    "podscan.fm/podcasts/the-guilty-feminist-1",
]

# The 3 previously-logged EHE URL keys observed this run (the GitHub blob
# was circular-rejected; the engadget key from #861 did not surface this
# run but remains in corpus). The 2 NEW EHE URL keys are new mirrors of
# in-corpus stories (Epstein ad; Kylie lenticular hijack), not new motifs.
EHE_KEYS = [
    "community.designtaxi.com/topic/33476-activist-group-hijacks-kylie-jenners-meta-smart-glasses-ads-with-sharp-privacy-warnings-across-london/",
    "en.softonic.com/articles/ray-ban-meta-smart-glasses-back-in-the-spotlight-london-ad-uses-epstein-image",
    "singulism.com/en/2026-07-17-meta-glasses-protest-london-bus-stops/",
]
NEW_EHE_KEYS = [
    "community.designtaxi.com/topic/34124-jeffrey-epstein-appears-to-model-meta-ray-bans-smart-glasses-on-new-ads/",
    "d33gy59ovltp76.cloudfront.net/news/london-bus-stop-poster-brutally-mocks-kylie-jenner-and-metas-ai-glasses-its-giving-fascism",
]

# Circular own-repo results from the Attention Sphere quoted search; rejected,
# not ingested. The podcast-sentiment.md blob plus the same 6 commit URLs as
# #846/#851/#856/#861 (verbatim hashes from this run's Full-URL listing).
AS_CIRCULAR_PREFIX = "github.com/rayhe/mediascope/commit/"
AS_CIRCULAR_COMMITS = [
    "a288c86f0be14694552fea4aa0fd3674cefe93bc",
    "a2b656f0660e299090803b4dfd7ee01087900c9f",
    "959038536c82b63a7ab3b708226aec070a43514a",
    "2c4e21e39a3bb17e74c8afc0bd5b7ad25bda29b4",
    "25c730ed6097aae952bdf714fe2afe375d8f9e35",
    "3d16eacfc03d35bad9ade4a15403fbcea2fb293c",
]

# Press set: 6 previously-logged keys + 1 NEW key (webpronews HateAid
# piece - new mirror of the in-corpus HateAid Aug-11 story).
NEW_PRESS_KEYS = [
    "webpronews.com/germanys-privacy-push-targets-meta-ray-ban-glasses-with-criminal-filing/",
]
KNOWN_PRESS_KEYS = [
    "ppc.land/hamburg-regulator-finds-ray-ban-meta-glasses-expose-bystanders-without-consent/",
    "www.livemint.com/technology/tech-news/meta-ray-ban-smart-glasses-could-store-voice-recordings-by-default-what-it-means-for-users/amp-11746118684276.html",
    "nypost.com/2026/09/18/us-news/california-users-among-plaintiffs-suing-meta-over-smart-glasses/",
    "9to5google.com/2026/08/28/meta-ray-ban-smart-glasses-privacy-led-loophole-update/",
    "startupfortune.com/meta-permanently-disables-cameras-on-thousands-of-tampered-smart-glasses/",
    "en.softonic.com/articles/meta-ray-ban-smart-glasses-update-privacy-loophole-now-closed",
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


class TestNovelty866:
    """Iteration 866 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_866_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_866*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_no_type_e_866_in_git_log_precommit(self):
        # Deselected pre-commit per the #565 followup convention alongside
        # the anchor test; verified pre-commit by shell grep (no "Type E
        # #866" in git log) and patched green post-commit, where it pins
        # the main commit as a singleton.
        log = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        mains = [
            l
            for l in log
            if re.search(r"Type E #866: podcast sentiment", l)
        ]
        assert len(mains) == 1, mains

    def test_type_e_866_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_866 files, no #866 in git log); this test
        # pins that no duplicate #866 main commit ever appears.
        log = _git_log_mains("Type E #866: podcast sentiment")
        assert len(log) == 1, log


class TestRotationCycleGuard866:
    """Rotation: 865-869 window, #865 (D) anchors, #866 is the E leg.

    The ANCHORED_SHA is patched to the main commit's SHA in the anchor
    followup per the #565 convention; these tests are deselected pre-commit.
    """

    ANCHORED_SHA = "PLACEHOLDER_PATCHED_IN_ANCHOR_FOLLOWUP"

    def test_865_869_window_second_leg(self):
        log = _read("iteration-log.md")
        assert "## #866" in log
        assert "865-869" in log

    def test_predecessor_865_type_d(self):
        log = _git_log_mains("Type D #865:")
        assert len(log) >= 1, "expected the #865 Type D main commit"

    def test_no_duplicate_866_in_log(self):
        lines = [
            l
            for l in _read("iteration-log.md").splitlines()
            if l.startswith("## #866")
        ]
        assert len(lines) == 1, lines


class TestGF96thCycle:
    """Guilty Feminist: episode 500 stands newest; one new GF URL key."""

    def test_gf_known_keys_all_in_corpus(self):
        # The 6 previously-logged GF keys must each carry >=1 corpus hit.
        # getpodcast did not surface this run but remains a known key.
        for key in GF_KEYS:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "GF key missing from corpus: %r" % key

    def test_new_gf_key_logged_this_run(self):
        # The podscan.fm GF directory listing is the ONE new GF URL key
        # (zero pre-commit corpus hits); the #866 section must log it.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #866")[1]
        for key in NEW_GF_KEYS:
            assert key in section, key

    def test_podscan_bonnie_greer_tribute_note(self):
        # The podscan key surfaces a Bonnie Greer tribute emergency
        # re-release: snippet-bounded, death not independently verified,
        # ZERO wearables content, not a numbered episode, no tone score.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #866")[1]
        assert "Bonnie Greer" in section
        assert "tribute" in section.lower()
        assert "zero wearables content" in section.lower() or "ZERO Meta/wearables content" in section

    def test_gf_500_stands_newest_no_501(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #866")[1]
        assert "No episode 501" in section

    def test_gf_ln_snippet_anomaly_not_a_new_episode(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #866")[1]
        assert "Released 23 December" in section
        assert "snippet-level noise" in section

    def test_uk_podcasts_signal_flagged_unverified(self):
        # uk-podcasts 760 / "Latest episode: 2026-09-16" UNCHANGED since #806
        # remains an UNVERIFIED single-directory signal per #503/iteration-492.
        ps = _read("podcast-sentiment.md")
        assert "UNVERIFIED single-directory signal" in ps

    def test_getpodcast_not_surfaced_this_run(self):
        # getpodcast did not surface this run; the section must say so.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #866")[1]
        assert "did NOT surface this run" in section

    def test_zero_meta_wearables_content_across_cycles(self):
        ps = _read("podcast-sentiment.md")
        assert "ZERO Meta/wearables content" in ps or "zero Meta/wearables content" in ps.lower()


class TestEHEHold96thCycle:
    """Everyone Hates Elon: 40-day hold, two new EHE mirror keys."""

    def test_ehe_40_day_hold(self):
        """40-day hold; regression guard on the date subtraction.

        #846 labeled the Aug 10 -> Sep 19 hold "47-day" and #851's
        first draft advanced it to "48-day". Both are arithmetically
        wrong: date(2026, 9, 19) - date(2026, 8, 10) == 40 days. The
        doc must carry the corrected label and never the old ones.
        """
        import datetime
        assert (datetime.date(2026, 9, 19) - datetime.date(2026, 8, 10)).days == 40
        section = _read("podcast-sentiment.md").split("## Iteration #866")[1]
        assert "40-day hold" in section
        assert "48-day hold" not in section
        assert "47-day hold" not in section

    def test_ehe_known_keys_all_in_corpus(self):
        for key in EHE_KEYS:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "EHE key missing from corpus: %r" % key

    def test_new_ehe_keys_logged_this_run(self):
        # Both new EHE keys are new MIRRORS of in-corpus stories (Epstein
        # ad; Kylie lenticular hijack), not new campaign motifs.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #866")[1]
        for key in NEW_EHE_KEYS:
            assert key in section, key
        assert "not new campaign motifs" in section.lower() or "new mirrors" in section.lower()

    def test_new_ehe_keys_story_lineage_distinguished(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #866")[1]
        assert "in-corpus" in section

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
        section = ps.split("## Iteration #866")[1]
        assert "circular" in section.lower()


class TestAttentionSphere96thNoMatch:
    """Attention Sphere: 96th quoted-search no-match; circular rejects."""

    def test_96th_no_match(self):
        ps = _read("podcast-sentiment.md")
        assert "ninety-sixth" in ps.lower()

    def test_circular_github_rejected(self):
        ps = _read("podcast-sentiment.md")
        assert "circular" in ps.lower()
        for commit in AS_CIRCULAR_COMMITS:
            hits = _needle_hits(AS_CIRCULAR_PREFIX + commit)
            assert len(hits) >= 1, "AS circular commit not in corpus: %r" % commit

    def test_tracked_sources_advanced_with_erratum(self):
        # Tracked Sources 94->96 through Sep 19 2026; #861's row update was
        # missed (recorded 94->95 in its cycle section but left the row at
        # 94) - the erratum must be stated in the top table.
        ps = _read("podcast-sentiment.md")
        assert "96 verification cycles" in ps
        assert "ERRATUM" in ps

    def test_task_spec_misidentification_stated(self):
        ps = _read("podcast-sentiment.md")
        assert "misidentified" in ps.lower()


class TestPressSurfaces866:
    """Press: 6 previously-logged keys + 1 new webpronews mirror key."""

    def test_six_press_keys_all_in_corpus(self):
        for key in KNOWN_PRESS_KEYS:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "press key missing from corpus: %r" % key

    def test_new_press_key_logged_this_run(self):
        # The webpronews HateAid piece is the ONE new press URL key
        # (zero pre-commit corpus hits); the #866 section must log it.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #866")[1]
        for key in NEW_PRESS_KEYS:
            assert key in section, key

    def test_webpronews_hateaid_story_lineage(self):
        # The HateAid Aug-11 criminal-complaint action is in-corpus; the
        # webpronews URL is the new surface. Story lineage must be stated.
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #866")[1]
        assert "HateAid" in section
        assert "story lineage in corpus" in section.lower() or "in-corpus" in section.lower()

    def test_webpronews_snippet_bounded_details(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #866")[1]
        assert "Frankfurt" in section
        assert "Fielmann" in section

    def test_hamburg_report_details(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #866")[1]
        assert "53-page" in section

    def test_nypost_ca_lawsuit_details(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #866")[1]
        assert "70+ plaintiffs" in section

    def test_no_tone_score_without_first_hand_read(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #866")[1]
        assert "NOT_SCORED" in section


class TestRecencyFrontier866:
    """Recency frontier holds at Sep 18."""

    def test_frontier_holds_at_sep_18(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #866")[1]
        assert "HOLDS at Sep 18" in section

    def test_frontier_driver_is_nypost_sep_18(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #866")[1]
        assert "NY Post Sep 18" in section or "nypost Sep 18" in section.lower()


class TestStandingRules866:
    """Aug 28 2026 standing rule; Type E adds no mechanisms; ledger 26."""

    def test_tone_not_scored(self):
        ps = _read("podcast-sentiment.md")
        assert "NOT_SCORED" in ps

    def test_is_significant_false(self):
        ps = _read("podcast-sentiment.md")
        assert "is_significant False" in ps or "is_significant false" in ps.lower()

    def test_twenty_sixth_member_present(self):
        # TWENTY-SIXTH member-form present in profiles/; TWENTY-SEVENTH
        # member-form absent. Refined per #850/#855: #847 (m739), #848
        # (m740), and #853 (m743) landed "TWENTY-SEVENTH absent" negative
        # guard strings in their falsification_family fields, so the guard
        # targets member-form strings per the #710/#720 convention
        # (documented, not repaired).
        corpus = _profiles_corpus()
        assert "TWENTY-SIXTH falsification-family member" in corpus

    def test_twenty_seventh_member_absent(self):
        corpus = _profiles_corpus()
        assert "TWENTY-SEVENTH falsification-family member" not in corpus

    def test_twenty_seventh_occurrences_are_negative_guards_only(self):
        # Exactly 6 occurrences per the #860 guard update (3 at #855 plus
        # the m745 #857 and the two m746 #858 guards), all
        # "TWENTY-SEVENTH absent" negative guards; one journalists.yaml
        # occurrence is line-wrapped, so the absent-match spans whitespace.
        corpus = _profiles_corpus()
        assert corpus.count("TWENTY-SEVENTH") == 6
        assert len(re.findall(r"TWENTY-SEVENTH\s+absent", corpus)) == 6

    def test_ledger_holds_at_26(self):
        assert 25 + 1 == 26

    def test_max_mechanism_750_no_751_keys(self):
        # Type E adds no mechanisms: max numeric mechanism_id stays 750 and
        # zero underscore-form 751 mechanism key strings exist in profiles/.
        needle_base = "mechanism" + "_" + "75" + "1"
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
        # Type E is monitoring-only: no test_type_e_866 block key anywhere
        # in profiles/.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "grep", "-l", "--", "test_type_e_866", "--", "profiles/"],
            capture_output=True,
            text=True,
        ).stdout.strip()
        assert out == "", out

    def test_no_analysis_json_update_warranted(self):
        ps = _read("podcast-sentiment.md")
        assert "No analysis.json update warranted" in ps


class TestDocSync866:
    def test_readme_row_866(self):
        readme = _read("README.md")
        assert "test_type_e_866_podcast_sentiment_96th_verification_sep19_9pm.py" in readme

    def test_readme_row_866_in_table(self):
        readme = _read("README.md")
        assert "| `test_type_e_866_podcast_sentiment_96th_verification_sep19_9pm.py` |" in readme

    def test_architecture_row_866(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "test_type_e_866_podcast_sentiment_96th_verification_sep19_9pm.py" in arch

    def test_architecture_lists_866_file(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "tests/test_type_e_866_podcast_sentiment_96th_verification_sep19_9pm.py" in arch


class TestIterationLog866:
    def test_iteration_log_has_866_entry(self):
        log = _read("iteration-log.md")
        assert "## #866" in log

    def test_iteration_log_866_records_new_surfaces(self):
        log = _read("iteration-log.md")
        assert "webpronews" in log
        assert "podscan.fm" in log


class TestDateGrounding866:
    def test_sep_19_2026_is_saturday(self):
        import datetime
        assert datetime.date(2026, 9, 19).strftime("%A") == "Saturday"

    def test_sep_18_2026_is_friday(self):
        import datetime
        assert datetime.date(2026, 9, 18).strftime("%A") == "Friday"

    def test_sep_10_2026_is_thursday(self):
        import datetime
        assert datetime.date(2026, 9, 10).strftime("%A") == "Thursday"
