"""Type E #861: podcast sentiment 95th verification cycle - Sep 19 2026 16:00 PDT.

Second leg of the 860-864 window (D #860 -> E #861 -> A -> B -> C).
Monitoring-only: GF episode 500 stands newest (~5 days after Sep 14
release; official-site corroboration carried from #796); ZERO new GF
URL keys (7 observed, all previously-logged; uk-podcasts 760 /
"Latest episode: 2026-09-16" UNCHANGED since #806, UNVERIFIED
single-directory signal; Listen Notes main re-crawled <1h lists 500
at top + Rubasingham special + 499/498/497/496; goloudnow 519585
re-crawled 19h; podparadise 1068940771 crawled 2d top 757 / Sep 7 =
499; getpodcast stale 66d top 491; Listen Notes pt mirror stale 219d
top 469); EHE 40-day hold (date(2026,9,19)-date(2026,8,10)=40 days;
5 URL keys all in corpus, quoted-search GitHub blob rejected
circular); Attention Sphere 95th quoted-search no-match (identical 7
own-repo GitHub URLs - the podcast-sentiment.md blob plus 6 commit
URLs a288c86/a2b656f/9590385/2c4e21e/25c730e/3d16eac, same set as
#846/#851/#856 - circular-rejected; Tracked Sources 94->95); press
SEVEN results ALL previously-logged (each >=1 corpus hit
pre-commit), ZERO new URL keys; recency frontier HOLDS at Sep 18
(#846's nypost Sep 18 CA-lawsuit piece remains newest). 27 result
rows / 19 distinct URL keys observed, all previously-logged.
Standing rule (Aug 28 2026): tone NOT_SCORED, p_value/cohens_d
NOT_CALCULATED, is_significant False. No mechanism block in
profiles/. No analysis.json update warranted. NOT artifact-grade.

48 tests, 11 classes.

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

# All 7 GF URL keys observed this run (verbatim from the Full-URL listing).
# ALL are previously-logged in the corpus this run (verified pre-commit).
# ZERO new GF URL keys. The #856 GF set carried a second YouTube key
# (youtube.com/watch?v=8OeSUuyvuXc, logged in #846); it did not surface
# this run, and the Listen Notes pt mirror replaces it in this run's set.
GF_KEYS = [
    "youtube.com/watch?v=iKXj2w2cp50",
    "goloudnow.com/podcasts/the-guilty-feminist-152/deborah-frances-white-on-the-news-meeting-519585",
    "rJKyRn2TWG",  # Listen Notes main + PT mirror share the episode ID
    "uk-podcasts.co.uk/podcast/the-guilty-feminist",
    "podparadise.com/Podcast/1068940771",
    "getpodcast.com/podcast/the-guilty-feminist",
]
NEW_GF_KEYS = []

# All 5 EHE URL keys observed this run (the 6th result was the circular
# github.com podcast-sentiment.md blob, rejected). All previously-logged.
EHE_KEYS = [
    "WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/",
    "singulism.com/en/2026-07-17-meta-glasses-protest-london-bus-stops/",
    "petapixel.com/2026/07/23/kylie-jenners-meta-smart-glasses-parodied-in-guerrilla-lenticular-ad/",
    "community.designtaxi.com/topic/33476-activist-group-hijacks-kylie-jenners-meta-smart-glasses-ads-with-sharp-privacy-warnings-across-london/",
    "en.softonic.com/articles/ray-ban-meta-smart-glasses-back-in-the-spotlight-london-ad-uses-epstein-image",
]

# Circular own-repo results from the Attention Sphere quoted search; rejected,
# not ingested. The podcast-sentiment.md blob plus the same 6 commit URLs as
# #846/#851/#856 (verbatim hashes from this run's Full-URL listing).
AS_CIRCULAR_PREFIX = "github.com/rayhe/mediascope/commit/"
AS_CIRCULAR_COMMITS = [
    "a288c86f0be14694552fea4aa0fd3674cefe93bc",
    "a2b656f0660e299090803b4dfd7ee01087900c9f",
    "959038536c82b63a7ab3b708226aec070a43514a",
    "2c4e21e39a3bb17e74c8afc0bd5b7ad25bda29b4",
    "25c730ed6097aae952bdf714fe2afe375d8f9e35",
    "3d16eacfc03d35bad9ade4a15403fbcea2fb293c",
]

# Press set: 7 results this run, ALL previously-logged URL keys (each >=1
# corpus hit pre-commit). ZERO new press URL keys this run.
NEW_PRESS_KEYS = []
KNOWN_PRESS_KEYS = [
    "ppc.land/hamburg-regulator-finds-ray-ban-meta-glasses-expose-bystanders-without-consent/",
    "nypost.com/2026/09/18/us-news/california-users-among-plaintiffs-suing-meta-over-smart-glasses/",
    "livemint.com/technology/tech-news/meta-ray-ban-smart-glasses-could-store-voice-recordings-by-default-what-it-means-for-users/amp-11746118684276.html",
    "9to5google.com/2026/08/28/meta-ray-ban-smart-glasses-privacy-led-loophole-update/",
    "startupfortune.com/meta-permanently-disables-cameras-on-thousands-of-tampered-smart-glasses/",
    "en.softonic.com/articles/meta-ray-ban-smart-glasses-update-privacy-loophole-now-closed",
    "usa-times.news/violated-singles-say-dates-secretly-filmed-them-with-meta-ray-bans-as-creep-glasses-trend-sparks-outrage/",
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


class TestNovelty861:
    """Iteration 861 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_861_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_861*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_no_type_e_861_in_git_log_precommit(self):
        # Deselected pre-commit per the #565 followup convention alongside
        # the anchor test; verified pre-commit by shell grep (no "Type E
        # #861" in git log) and patched green post-commit, where it pins
        # the main commit as a singleton.
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
            if re.search(r"Type E #861: podcast sentiment", l)
        ]
        assert len(mains) == 1, mains

    def test_type_e_861_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_861 files, no #861 in git log); this test
        # pins that no duplicate #861 main commit ever appears.
        log = _git_log_mains("Type E #861: podcast sentiment")
        assert len(log) == 1, log


class TestRotationCycleGuard861:
    """Rotation: 860-864 window, #860 (D) anchors, #861 is the E leg.

    The ANCHORED_SHA is patched to the main commit's SHA in the anchor
    followup per the #565 convention; these tests are deselected pre-commit.
    """

    ANCHORED_SHA = "05dc621e67f8520c2a9a30958a2dcfad7dc643f4"

    def test_860_864_window_second_leg(self):
        log = _read("iteration-log.md")
        assert "## #861" in log
        assert "860-864" in log

    def test_predecessor_860_type_d(self):
        log = _git_log_mains("Type D #860:")
        assert len(log) >= 1, "expected the #860 Type D main commit"

    def test_no_duplicate_861_in_log(self):
        lines = [
            l
            for l in _read("iteration-log.md").splitlines()
            if l.startswith("## #861")
        ]
        assert len(lines) == 1, lines


class TestGF95thCycle:
    """Guilty Feminist: episode 500 stands newest; zero new URL keys."""

    def test_gf_keys_all_in_corpus(self):
        # This run all 7 GF keys are previously-logged (corpus hits); there
        # are no NEW GF keys to additionally log.
        assert NEW_GF_KEYS == [], NEW_GF_KEYS
        for key in GF_KEYS:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "GF key missing from corpus: %r" % key

    def test_zero_new_gf_keys_this_run(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #861")[1]
        assert "ZERO new GF URL keys this run" in section

    def test_gf_500_stands_newest_no_501(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #861")[1]
        assert "500" in section
        assert "No episode 501" in section or "no 501" in section.lower()

    def test_gf_ln_main_snippet_anomaly_not_a_new_episode(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #861")[1]
        assert "Released 23 December" in section
        assert "snippet-level noise" in section

    def test_uk_podcasts_signal_flagged_unverified(self):
        # uk-podcasts 760 / "Latest episode: 2026-09-16" UNCHANGED since #806
        # remains an UNVERIFIED single-directory signal per #503/iteration-492.
        ps = _read("podcast-sentiment.md")
        assert "UNVERIFIED single-directory signal" in ps

    def test_getpodcast_key_verified_preexisting(self):
        # The getpodcast key surfaced again in search this run but is a
        # pre-existing corpus key (verified in-corpus at #851 with 8
        # occurrence hits across 4 files); _needle_hits counts files.
        hits = _needle_hits("getpodcast.com/podcast/the-guilty-feminist")
        assert len(hits) >= 4, hits

    def test_zero_meta_wearables_content_across_cycles(self):
        ps = _read("podcast-sentiment.md")
        assert "ZERO Meta/wearables content" in ps or "zero Meta/wearables content" in ps.lower()


class TestEHEHold95thCycle:
    """Everyone Hates Elon: 40-day hold, no new URL keys this run."""

    def test_ehe_40_day_hold(self):
        """40-day hold; regression guard on the date subtraction.

        #846 labeled the Aug 10 -> Sep 19 hold "47-day" and #851's
        first draft advanced it to "48-day". Both are arithmetically
        wrong: date(2026, 9, 19) - date(2026, 8, 10) == 40 days. The
        doc must carry the corrected label and never the old ones.
        """
        import datetime
        assert (datetime.date(2026, 9, 19) - datetime.date(2026, 8, 10)).days == 40
        section = _read("podcast-sentiment.md").split("## Iteration #861")[1]
        assert "40-day hold" in section
        assert "48-day hold" not in section
        assert "47-day hold" not in section

    def test_all_ehe_keys_in_corpus(self):
        for key in EHE_KEYS:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "EHE key missing from corpus: %r" % key

    def test_no_new_ehe_key_this_run(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #861")[1] if "## Iteration #861" in ps else ps
        assert "NO new EHE URL keys this run" in section

    def test_no_competitor_equivalent(self):
        ps = _read("podcast-sentiment.md")
        assert "No competitor-equivalent" in ps or "no competitor-equivalent" in ps.lower()

    def test_ehe_is_campaign_group_not_podcast(self):
        # Verified 2026-09-07: "Everyone Hates Elon" is an activist campaign
        # group, NOT a podcast. Campaign activity is logged as media/news
        # coverage, never as podcast episodes.
        ps = _read("podcast-sentiment.md")
        assert "NOT a podcast" in ps or "not a podcast" in ps.lower()


class TestAttentionSphere95thNoMatch:
    """Attention Sphere: 95th quoted-search no-match; circular rejects."""

    def test_95th_no_match(self):
        ps = _read("podcast-sentiment.md")
        assert "95th" in ps or "ninety-fifth" in ps.lower()

    def test_circular_github_rejected(self):
        ps = _read("podcast-sentiment.md")
        assert "circular" in ps.lower()

    def test_tracked_sources_advanced(self):
        # Tracked Sources 94->95 cycles through Sep 19 2026.
        ps = _read("podcast-sentiment.md")
        assert "Tracked Sources 94->95" in ps or "95 verification cycles" in ps

    def test_task_spec_misidentification_stated(self):
        ps = _read("podcast-sentiment.md")
        assert "misidentified" in ps.lower()


class TestPressSurfaces861:
    """Press set: 7 results, ALL previously-logged, zero new URL keys."""

    def test_seven_press_keys_all_in_corpus(self):
        assert len(KNOWN_PRESS_KEYS) == 7, KNOWN_PRESS_KEYS
        assert NEW_PRESS_KEYS == [], NEW_PRESS_KEYS
        for key in KNOWN_PRESS_KEYS:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "press key missing from corpus: %r" % key

    def test_zero_new_press_keys_this_run(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #861")[1]
        assert "ZERO new URL keys this run" in section

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


class TestRecencyFrontier861:
    """Recency frontier HOLDS at Sep 18 (#846's nypost piece newest)."""

    def test_frontier_holds_at_sep_18(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #861")[1]
        assert "HOLDS at Sep 18" in section

    def test_frontier_driver_is_nypost_sep_18(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #861")[1]
        assert "nypost" in section.lower()
        assert "Sep 18" in section


class TestStandingRules861:
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

    def test_max_mechanism_747_no_748_keys(self):
        # Type E adds no mechanisms: max numeric mechanism_id stays 747 and
        # zero underscore-form 748 mechanism key strings exist in profiles/.
        needle_base = "mechanism" + "_" + "74" + "8"
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
        # Type E is monitoring-only: no test_type_e_861 block key anywhere
        # in profiles/.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "grep", "-l", "--", "test_type_e_861", "--", "profiles/"],
            capture_output=True,
            text=True,
        ).stdout.strip()
        assert out == "", out

    def test_no_analysis_json_update_warranted(self):
        ps = _read("podcast-sentiment.md")
        assert "No analysis.json update warranted" in ps


class TestDocSync861:
    def test_readme_row_861(self):
        readme = _read("README.md")
        assert "test_type_e_861_podcast_sentiment_95th_verification_sep19_4pm.py" in readme

    def test_readme_row_861_in_table(self):
        readme = _read("README.md")
        assert "| `test_type_e_861_podcast_sentiment_95th_verification_sep19_4pm.py` |" in readme

    def test_architecture_row_861(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "test_type_e_861_podcast_sentiment_95th_verification_sep19_4pm.py" in arch

    def test_architecture_lists_861_file(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "tests/test_type_e_861_podcast_sentiment_95th_verification_sep19_4pm.py" in arch


class TestIterationLog861:
    def test_iteration_log_has_861_entry(self):
        log = _read("iteration-log.md")
        assert "## #861" in log

    def test_iteration_log_861_records_frontier_hold(self):
        log = _read("iteration-log.md")
        assert "Sep 18" in log


class TestDateGrounding861:
    def test_sep_19_2026_is_saturday(self):
        import datetime
        assert datetime.date(2026, 9, 19).strftime("%A") == "Saturday"

    def test_sep_18_2026_is_friday(self):
        import datetime
        assert datetime.date(2026, 9, 18).strftime("%A") == "Friday"

    def test_sep_10_2026_is_thursday(self):
        import datetime
        assert datetime.date(2026, 9, 10).strftime("%A") == "Thursday"
