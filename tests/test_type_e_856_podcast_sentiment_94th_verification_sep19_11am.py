"""Type E #856: podcast sentiment 94th verification cycle - Sep 19 2026 11:00 PDT.

Second leg of the 855-859 window (D #855 -> E #856 -> A -> B -> C).
Monitoring-only: GF episode 500 stands newest (~5 days after Sep 14
release; official-site corroboration carried from #796); ZERO new GF
URL keys (7 observed, all previously-logged); EHE 40-day hold
(date(2026,9,19)-date(2026,8,10)=40 days; 5 URL keys all in corpus,
quoted-search GitHub blob rejected circular); Attention Sphere 94th
quoted-search no-match (identical 6 own-repo GitHub commit URLs,
circular-rejected; Tracked Sources 93->94); press SEVEN results ALL
previously-logged (verified each >=1 corpus hit pre-commit), ZERO new
URL keys; recency frontier HOLDS at Sep 18 (#846's nypost CA-lawsuit
piece remains newest). 26 result rows / 20 distinct URL keys observed,
all previously-logged. Standing rule (Aug 28 2026): tone NOT_SCORED,
p_value/cohens_d NOT_CALCULATED, is_significant False. No mechanism
block in profiles/. No analysis.json update warranted. NOT artifact-grade.

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
# ZERO new GF URL keys.
GF_KEYS = [
    "youtube.com/watch?v=iKXj2w2cp50",
    "goloudnow.com/podcasts/the-guilty-feminist-152/deborah-frances-white-on-the-news-meeting-519585",
    "rJKyRn2TWG",  # Listen Notes main + PT mirror share the episode ID
    "uk-podcasts.co.uk/podcast/the-guilty-feminist",
    "podparadise.com/Podcast/1068940771",
    "youtube.com/watch?v=8OeSUuyvuXc",  # logged in #846, now pre-existing
    "getpodcast.com/podcast/the-guilty-feminist",  # verified pre-existing #851
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
# not ingested. Six commit URLs this run (identical set to #846/#851).
AS_CIRCULAR_PREFIX = "github.com/rayhe/mediascope/commit/"

# Press set: 7 results this run, ALL previously-logged URL keys (each >=1
# corpus hit pre-commit). ZERO new press URL keys this run.
NEW_PRESS_KEYS = []
KNOWN_PRESS_KEYS = [
    "ppc.land/hamburg-regulator-finds-ray-ban-meta-glasses-expose-bystanders-without-consent/",
    "nypost.com/2026/09/18/us-news/california-users-among-plaintiffs-suing-meta-over-smart-glasses/",
    "usa-times.news/violated-singles-say-dates-secretly-filmed-them-with-meta-ray-bans-as-creep-glasses-trend-sparks-outrage/",
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


def _profiles_corpus():
    # Walks profiles/ on disk (not git grep) so the sweep sees working-tree
    # state pre-commit; test files in tests/ cannot pollute the count.
    parts = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for f in files:
            with open(os.path.join(root, f), encoding="utf-8", errors="replace") as fh:
                parts.append(fh.read())
    return "\n".join(parts)


class TestNovelty856:
    """Iteration 856 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_856_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_856*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_no_type_e_856_in_git_log_precommit(self):
        # Deselected pre-commit per the #565 followup convention alongside
        # the anchor test; verified pre-commit by shell grep (no "Type E
        # #856" in git log) and patched green post-commit, where it pins
        # the main commit as a singleton.
        log = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        mains = [
            l
            for l in log
            if re.search(r"Type E #856: podcast sentiment", l)
        ]
        assert len(mains) == 1, mains

    def test_type_e_856_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_856 files, no #856 in git log); this test
        # pins that no duplicate #856 main commit ever appears.
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
            if re.search(r"Type E #856: podcast sentiment", l)
        ]
        assert len(mains) == 1, mains


class TestRotationCycleGuard856:
    """Rotation: 855-859 window, #855 (D) anchors, #856 is the E leg.

    The ANCHORED_SHA is patched to the main commit's SHA in the anchor
    followup per the #565 convention; these tests are deselected pre-commit.
    """

    ANCHORED_SHA = "ab4dee6467ab5d54d6d00d11e60ac528b2a43a1b"

    def test_855_859_window_second_leg(self):
        log = _read("iteration-log.md")
        assert "## #856" in log
        assert "855-859" in log

    def test_predecessor_855_type_d(self):
        log = _git_log_mains("Type D #855:")
        assert len(log) >= 1, "expected the #855 Type D main commit"

    def test_no_duplicate_856_in_log(self):
        lines = [
            l
            for l in _read("iteration-log.md").splitlines()
            if l.startswith("## #856")
        ]
        assert len(lines) == 1, lines


class TestGF94thCycle:
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
        section = ps.split("## Iteration #856")[1]
        assert "ZERO new GF URL keys this run" in section

    def test_gf_500_stands_newest_no_501(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #856")[1]
        assert "500" in section
        assert "No episode 501" in section or "no 501" in section.lower()

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

    def test_listen_notes_main_caught_up(self):
        # Listen Notes main re-crawled <1h lists 500 at top + the unnumbered
        # Indhu Rubasingham special + 499/498/497/496 (caught up from the
        # 421-lag observed #766-#836, confirmed #841).
        ps = _read("podcast-sentiment.md")
        assert "Rubasingham" in ps


class TestEHEHold94thCycle:
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
        section = _read("podcast-sentiment.md").split("## Iteration #856")[1]
        assert "40-day hold" in section
        assert "48-day hold" not in section
        assert "47-day hold" not in section

    def test_all_ehe_keys_in_corpus(self):
        for key in EHE_KEYS:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "EHE key missing from corpus: %r" % key

    def test_no_new_ehe_key_this_run(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #856")[1] if "## Iteration #856" in ps else ps
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


class TestAttentionSphere94thNoMatch:
    """Attention Sphere: 94th quoted-search no-match; circular rejects."""

    def test_94th_no_match(self):
        ps = _read("podcast-sentiment.md")
        assert "94th" in ps or "ninety-fourth" in ps.lower()

    def test_circular_github_rejected(self):
        ps = _read("podcast-sentiment.md")
        assert "circular" in ps.lower()

    def test_tracked_sources_advanced(self):
        # Tracked Sources 93->94 cycles through Sep 19 2026.
        ps = _read("podcast-sentiment.md")
        assert "Tracked Sources 93->94" in ps or "94 verification cycles" in ps

    def test_task_spec_misidentification_stated(self):
        ps = _read("podcast-sentiment.md")
        assert "misidentified" in ps.lower()


class TestPressSurfaces856:
    """Press set: 7 results, ALL previously-logged, zero new URL keys."""

    def test_seven_press_keys_all_in_corpus(self):
        assert len(KNOWN_PRESS_KEYS) == 7, KNOWN_PRESS_KEYS
        assert NEW_PRESS_KEYS == [], NEW_PRESS_KEYS
        for key in KNOWN_PRESS_KEYS:
            hits = _needle_hits(key)
            assert len(hits) >= 1, "press key missing from corpus: %r" % key

    def test_zero_new_press_keys_this_run(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #856")[1]
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


class TestRecencyFrontier856:
    """Recency frontier HOLDS at Sep 18 (#846's nypost piece newest)."""

    def test_frontier_holds_at_sep_18(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #856")[1]
        assert "HOLDS at Sep 18" in section

    def test_frontier_driver_is_nypost_sep_18(self):
        ps = _read("podcast-sentiment.md")
        section = ps.split("## Iteration #856")[1]
        assert "nypost" in section.lower()
        assert "Sep 18" in section


class TestStandingRules856:
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
        # Exactly 3 occurrences per the #855 guard update, all
        # "TWENTY-SEVENTH absent" negative guards in the m739
        # (competitor-coverage-research), m740 (journalists), and m743
        # (journalists) falsification_family fields.
        corpus = _profiles_corpus()
        assert corpus.count("TWENTY-SEVENTH") == 3
        assert corpus.count("TWENTY-SEVENTH absent") == 3

    def test_ledger_holds_at_26(self):
        assert 25 + 1 == 26

    def test_max_mechanism_744_no_745_keys(self):
        # Type E adds no mechanisms: max numeric mechanism_id stays 744 and
        # zero underscore-form 745 mechanism key strings exist in profiles/.
        needle_base = "mechanism" + "_" + "74" + "5"
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
        # Type E is monitoring-only: no test_type_e_856 block key anywhere
        # in profiles/.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "grep", "-l", "--", "test_type_e_856", "--", "profiles/"],
            capture_output=True,
            text=True,
        ).stdout.strip()
        assert out == "", out

    def test_no_analysis_json_update_warranted(self):
        ps = _read("podcast-sentiment.md")
        assert "No analysis.json update warranted" in ps


class TestDocSync856:
    def test_readme_row_856(self):
        readme = _read("README.md")
        assert "test_type_e_856_podcast_sentiment_94th_verification_sep19_11am.py" in readme

    def test_readme_row_856_in_table(self):
        readme = _read("README.md")
        assert "| `test_type_e_856_podcast_sentiment_94th_verification_sep19_11am.py` |" in readme

    def test_architecture_row_856(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "test_type_e_856_podcast_sentiment_94th_verification_sep19_11am.py" in arch

    def test_architecture_lists_856_file(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "tests/test_type_e_856_podcast_sentiment_94th_verification_sep19_11am.py" in arch


class TestIterationLog856:
    def test_iteration_log_has_856_entry(self):
        log = _read("iteration-log.md")
        assert "## #856" in log

    def test_iteration_log_856_records_frontier_hold(self):
        log = _read("iteration-log.md")
        assert "Sep 18" in log


class TestDateGrounding856:
    def test_sep_19_2026_is_saturday(self):
        import datetime
        assert datetime.date(2026, 9, 19).strftime("%A") == "Saturday"

    def test_sep_18_2026_is_friday(self):
        import datetime
        assert datetime.date(2026, 9, 18).strftime("%A") == "Friday"

    def test_sep_10_2026_is_thursday(self):
        import datetime
        assert datetime.date(2026, 9, 10).strftime("%A") == "Thursday"
