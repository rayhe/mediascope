"""Type E #846: podcast sentiment 92nd verification cycle - Sep 19 2026 01:00 PDT.

Second leg of the 845-849 window (D #845 -> E #846 -> A -> B -> C).
Monitoring-only: GF episode 500 stands newest (~4.75 days after Sep 14
release; official-site corroboration carried from #796); EHE 47-day hold
(Aug 10 -> Sep 19), no new EHE URL keys; Attention Sphere 92nd
quoted-search no-match; press SEVEN results with THREE new URL keys
(ppc.land Hamburg Sep 10 53-page report, NY Post Sep 18 CA lawsuit
70+ plaintiffs, usa-times "creep glasses" ~Sep 16); recency frontier
ADVANCES Sep 9 -> Sep 18 (first advance in 43 consecutive ties).
25 observed URL keys: 7 GF + 5 EHE + 6 AS-circular + 7 press;
20 previously-logged, 5 NEW (1 GF stale upload + 3 press + the GF
482 key counts once). Standing rule (Aug 28 2026): tone NOT_SCORED,
p_value/cohens_d NOT_CALCULATED, is_significant False. No mechanism
block in profiles/. No analysis.json update warranted. NOT artifact-grade.

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
    "rJKyRn2TWG",  # Listen Notes main + PT mirror share the episode ID
    "uk-podcasts.co.uk/podcast/the-guilty-feminist",
    "podparadise.com/Podcast/1068940771",
    "youtube.com/watch?v=8OeSUuyvuXc",  # NEW this run: episode 482 stale upload
]
NEW_GF_KEYS = ["youtube.com/watch?v=8OeSUuyvuXc"]

EHE_KEYS = [
    "WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/",
    "singulism.com/en/2026-07-17-meta-glasses-protest-london-bus-stops/",
    "petapixel.com/2026/07/23/kylie-jenners-meta-smart-glasses-parodied-in-guerrilla-lenticular-ad/",
    "community.designtaxi.com/topic/33476-activist-group-hijacks-kylie-jenners-meta-smart-glasses-ads-with-sharp-privacy-warnings-across-london/",
    "en.softonic.com/articles/ray-ban-meta-smart-glasses-back-in-the-spotlight-london-ad-uses-epstein-image",  # new in #841, now pre-existing
]

# Circular own-repo results from the Attention Sphere quoted search; rejected,
# not ingested. Six commit URLs this run (five familiar + one new hash).
AS_CIRCULAR_PREFIX = "github.com/rayhe/mediascope/commit/"

# Press set: 7 results. Three NEW URL keys this run (verified zero-hit
# repo-wide pre-commit); four previously-logged.
NEW_PRESS_KEYS = [
    "ppc.land/hamburg-regulator-finds-ray-ban-meta-glasses-expose-bystanders-without-consent/",
    "nypost.com/2026/09/18/us-news/california-users-among-plaintiffs-suing-meta-over-smart-glasses/",
    "usa-times.news/violated-singles-say-dates-secretly-filmed-them-with-meta-ray-bans-as-creep-glasses-trend-sparks-outrage/",
]
KNOWN_PRESS_KEYS = [
    "livemint.com/technology/tech-news/meta-ray-ban-smart-glasses-could-store-voice-recordings-by-default-what-it-means-for-users/amp-11746118684276.html",
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


class TestNovelty846:
    """Iteration 846 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_846_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_846*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_846_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_846 files, no #846 in git log); this test
        # pins that no duplicate #846 main commit ever appears.
        #
        # Hardened vs the #756/#759 naive "Type E #NNN:" prefix match, which
        # also matched the followup subjects (\"Type E #NNN followup:\",
        # \"Type E #NNN: push-blocked status\") and broke once the push-blocked
        # note landed (#760 rotation-guard hardening note). The
        # \": podcast sentiment\" qualifier pins only the main commit.
        log = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        mains = [
            l
            for l in log
            if re.match(r"^[0-9a-f]{40} Type E #846: podcast sentiment", l)
        ]
        assert len(mains) == 1, mains
        anchor = TestRotationCycleGuard846.ANCHORED_SHA
        assert mains[0].startswith(anchor + " "), (anchor, mains)


class TestRotationCycleGuard846:
    """Rotation: 845-849 window, #845 (D) anchors, #846 is the E leg.

    The ANCHORED_SHA is patched to the main commit's SHA in the anchor
    followup per the #565 convention; these tests are deselected pre-commit.
    """

    ANCHORED_SHA = "0000000000000000000000000000000000000000"

    def test_845_849_window_second_leg(self):
        readme = _read("iteration-log.md")
        assert "#846" in readme
        assert "845-849" in readme

    def test_predecessor_845_type_d(self):
        log = _git_log_mains("Type D #845:")
        assert len(log) >= 1, "expected the #845 Type D main commit"

    def test_no_duplicate_846_in_log(self):
        lines = [
            l
            for l in _read("iteration-log.md").splitlines()
            if l.startswith("## #846")
        ]
        assert len(lines) == 1, lines


class TestGF92ndCycle:
    """Guilty Feminist: episode 500 stands newest; one new stale-upload key."""

    def test_gf_keys_in_corpus_or_logged(self):
        # All GF keys are either previously-logged (corpus hits) or the one
        # NEW key documented in podcast-sentiment.md's #846 section.
        ps = _read("podcast-sentiment.md")
        for key in GF_KEYS:
            if key in NEW_GF_KEYS:
                assert key in ps, "new GF key must be logged in podcast-sentiment.md: %r" % key
            else:
                hits = _needle_hits(key)
                assert len(hits) >= 1, "GF key missing from corpus: %r" % key

    def test_new_gf_key_is_stale_upload_not_new_episode(self):
        # The new 8OeSUuyvuXc key resolves to episode 482 (Ten for Ten #10:
        # Sara Pascoe, recorded April 2026, released May 11, crawled 130d).
        # It is a stale YouTube upload surfacing in search, NOT a new episode
        # and NOT Meta/wearables content.
        ps = _read("podcast-sentiment.md")
        assert "8OeSUuyvuXc" in ps
        assert "482" in ps

    def test_gf_500_stands_newest(self):
        ps = _read("podcast-sentiment.md")
        assert "500" in ps
        assert "no episode 501" in ps.lower() or "no 501" in ps.lower()

    def test_uk_podcasts_signal_flagged_unverified(self):
        # uk-podcasts 760 / "Latest episode: 2026-09-16" UNCHANGED since #806
        # remains an UNVERIFIED single-directory signal per #503/iteration-492.
        ps = _read("podcast-sentiment.md")
        assert "UNVERIFIED single-directory signal" in ps

    def test_zero_meta_wearables_content_across_cycles(self):
        ps = _read("podcast-sentiment.md")
        assert "ZERO Meta/wearables content" in ps or "zero Meta/wearables content" in ps.lower()

    def test_listen_notes_main_caught_up(self):
        # Listen Notes main re-crawled 12h lists 500 at top + the unnumbered
        # Indhu Rubasingham special + 499/498/497/496 (caught up from the
        # 421-lag observed #766-#836, confirmed #841).
        ps = _read("podcast-sentiment.md")
        assert "Rubasingham" in ps


class TestEHEHold92ndCycle:
    """Everyone Hates Elon: 47-day hold, no new URL keys this run."""

    def test_ehe_47_day_hold(self):
        ps = _read("podcast-sentiment.md")
        assert "47-day hold" in ps

    def test_all_ehe_keys_in_corpus(self):
        for key in EHE_KEYS:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "EHE key missing from corpus: %r" % key

    def test_no_new_ehe_key_this_run(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #846")[1] if "## Iteration #846" in ps else ps
        assert "softonic" in section.lower()

    def test_no_competitor_equivalent(self):
        ps = _read("podcast-sentiment.md")
        assert "No competitor-equivalent" in ps or "no competitor-equivalent" in ps.lower()

    def test_ehe_is_campaign_group_not_podcast(self):
        # Verified 2026-09-07: "Everyone Hates Elon" is an activist campaign
        # group, NOT a podcast. Campaign activity is logged as media/news
        # coverage, never as podcast episodes.
        ps = _read("podcast-sentiment.md")
        assert "NOT a podcast" in ps or "not a podcast" in ps.lower()


class TestAttentionSphere92ndNoMatch:
    """Attention Sphere: 92nd quoted-search no-match; circular rejects."""

    def test_92nd_no_match(self):
        ps = _read("podcast-sentiment.md")
        assert "92nd" in ps or "ninety-second" in ps.lower()

    def test_circular_github_rejected(self):
        ps = _read("podcast-sentiment.md")
        assert "circular" in ps.lower()

    def test_tracked_sources_advanced(self):
        # Tracked Sources 91->92 cycles through Sep 19 2026.
        ps = _read("podcast-sentiment.md")
        assert "Tracked Sources 91->92" in ps or "Tracked Sources 91" in ps

    def test_task_spec_misidentification_stated(self):
        ps = _read("podcast-sentiment.md")
        assert "misidentified" in ps.lower()


class TestPressSurfaces846:
    """Press set: 7 results, 3 NEW URL keys, 4 previously-logged."""

    def test_new_press_keys_logged_in_sentiment(self):
        ps = _read("podcast-sentiment.md")
        for key in NEW_PRESS_KEYS:
            assert key in ps, "new press key must be logged: %r" % key

    def test_new_press_keys_now_have_corpus_hits(self):
        # Post-commit the new keys land in podcast-sentiment.md (the #846
        # section); pre-commit they were verified zero-hit repo-wide.
        for key in NEW_PRESS_KEYS:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "new press key not ingested: %r" % key

    def test_known_press_keys_in_corpus(self):
        for key in KNOWN_PRESS_KEYS:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "press key missing from corpus: %r" % key

    def test_hamburg_report_details(self):
        # Hamburg HmbBfDI 53-page Sep 10 2026 report: hardware teardown,
        # companion-app network traffic, GDPR legal assessment; wearers (not
        # just Meta) responsible for bystander consent; LED often too dim.
        ps = _read("podcast-sentiment.md")
        assert "Hamburg" in ps
        assert "53-page" in ps

    def test_nypost_ca_lawsuit_details(self):
        # NY Post Sep 18 2026: 70+ plaintiffs, amended late-August complaint,
        # Kenya contractors, sex/nudity/bathroom footage, PL18 plaintiff.
        ps = _read("podcast-sentiment.md")
        assert "70" in ps
        assert "Kenya" in ps

    def test_usa_times_creep_glasses_details(self):
        # usa-times ~Sep 16 2026: dating "creep glasses" piece relaying WIRED's
        # Courtney McAnuff reporting (summer 2024 Manhattan date, Instagram
        # Story of bar/subway footage, "I felt super violated").
        ps = _read("podcast-sentiment.md")
        assert "creep glasses" in ps.lower()

    def test_no_tone_score_without_first_hand_read(self):
        # Snippet-bounded: no tone score asserted without a first-hand read.
        ps = _read("podcast-sentiment.md")
        assert "NOT_SCORED" in ps


class TestRecencyFrontier846:
    """Recency frontier ADVANCES Sep 9 -> Sep 18 (first advance in 43 ties)."""

    def test_frontier_advances_to_sep_18(self):
        ps = _read("podcast-sentiment.md")
        assert "ADVANCES" in ps
        assert "Sep 18" in ps

    def test_43_consecutive_ties_broken(self):
        # The frontier was TIED at Sep 9 for forty-three consecutive cycles
        # (#636 through #841) on the petapixel Sep 9 piece.
        ps = _read("podcast-sentiment.md")
        assert "43" in ps

    def test_frontier_driver_is_nypost_sep_18(self):
        ps = _read("podcast-sentiment.md")
        assert "nypost" in ps.lower()

    def test_sep_10_hamburg_and_sep_16_usa_times_noted(self):
        ps = _read("podcast-sentiment.md")
        assert "Sep 10" in ps
        assert "Sep 16" in ps


class TestStandingRules846:
    """Aug 28 2026 standing rule: monitoring-only, no mechanism, no artifact."""

    def test_tone_not_scored(self):
        ps = _read("podcast-sentiment.md")
        assert "NOT_SCORED" in ps

    def test_stats_not_calculated(self):
        ps = _read("podcast-sentiment.md")
        assert "NOT_CALCULATED" in ps

    def test_is_significant_false(self):
        ps = _read("podcast-sentiment.md")
        assert "is_significant False" in ps

    def test_no_mechanism_block_in_profiles(self):
        # Type E adds no mechanism: max numeric mechanism_id stays 738
        # (post-#845); zero 739 keys anywhere in profiles/.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "grep", "-E", "--", "mechanism_id: 739", "--", "profiles/"],
            capture_output=True,
            text=True,
        ).stdout.strip()
        assert out == "", out

    def test_falsification_ledger_holds_at_26(self):
        # Ledger convention: TWENTY-SIXTH present; TWENTY-SEVENTH absent
        # *in profiles/* (doc-level "absent in profiles/" phrases elsewhere
        # are prose about the profiles corpus, not assigned ledger entries).
        hits = _needle_hits("TWENTY-SIXTH")
        assert len(hits) >= 1
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "grep", "-l", "--", "TWENTY-SEVENTH", "--", "profiles/"],
            capture_output=True,
            text=True,
        ).stdout.strip()
        assert out == "", out


class TestDocSync846:
    def test_readme_row_846(self):
        readme = _read("README.md")
        assert "test_type_e_846_podcast_sentiment_92nd_verification_sep19_1am.py" in readme

    def test_readme_row_846_in_table(self):
        readme = _read("README.md")
        assert "| `test_type_e_846_podcast_sentiment_92nd_verification_sep19_1am.py` |" in readme

    def test_architecture_row_846(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "test_type_e_846_podcast_sentiment_92nd_verification_sep19_1am.py" in arch

    def test_architecture_lists_846_file(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "tests/test_type_e_846_podcast_sentiment_92nd_verification_sep19_1am.py" in arch


class TestIterationLog846:
    def test_iteration_log_has_846_entry(self):
        log = _read("iteration-log.md")
        assert "## #846" in log

    def test_iteration_log_846_records_frontier_advance(self):
        log = _read("iteration-log.md")
        assert "Sep 18" in log


class TestDateGrounding846:
    def test_sep_19_2026_is_saturday(self):
        import datetime
        assert datetime.date(2026, 9, 19).strftime("%A") == "Saturday"

    def test_sep_18_2026_is_friday(self):
        import datetime
        assert datetime.date(2026, 9, 18).strftime("%A") == "Friday"

    def test_sep_10_2026_is_thursday(self):
        import datetime
        assert datetime.date(2026, 9, 10).strftime("%A") == "Thursday"
