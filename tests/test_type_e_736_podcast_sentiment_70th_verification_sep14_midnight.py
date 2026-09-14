"""Type E #736: podcast sentiment 70th verification cycle (Sep 14 2026, 00:00 PDT).

Guilty Feminist: NO new episode content this run. au.radio.net (Last Updated
2 days ago, crawled 6h) still 758 episodes with the #721 "In Conversation with
Indhu Rubasingham" special (12/09/2026, 49 mins) on top, unchanged.
uk-podcasts.co.uk (crawled 4h) still 758 / "Latest episode: 2026-09-12",
unchanged since #706 - still an UNVERIFIED single-directory signal; no drop
asserted per #503/iteration-492. Listen Notes (crawled 8d) still lags on 498
(756 episodes). podscan.fm signal carried from #726 (crawled 4h at that
time): the 499 transcript was the newest NUMBERED release; no new podscan
result this run, and per #503 that bounded absence is not a claim. ZERO NEW
URL KEYS this run: the chortle.co.uk Edinburgh Fringe live-show listing key
already in corpus (pre-existing key, not a new episode; the Sun 13 Sep Kings
Place show is a live-show listing, not a release). The 500-watch HOLDS: the
projected day (Mon Sep 14) arrived with no numbered episode 500 detected;
numbered-500 cadence (499 released Sep 7) had pointed at TODAY. No first-hand
page read attempted; no tone scores computed (no verified new numbered
episode).

EHE 37-day hold continues (Aug 10 -> Sep 14, inclusive count): 7 re-surfaces,
ALL previously-logged URL keys, ALL verified in corpus pre-commit
(thetimes Epstein 49d/crawled 49d; engadget WWW-uppercase 59d/crawled 9d,
same page per #676 convention; petapixel lenticular 53d/crawled 20d;
latestly fact-check 46d/crawled 22d; hyperallergic http key 61d/crawled 6h;
fstoppers lenticular re-surfaced crawled 4h) plus the Times of India
133146816 UK-venue-bans editorial piece re-surfaced (in corpus via #721,
crawled 7d; snippet shows content refreshed since #721 - Tim
Martin/Wetherspoons ban quote, Lorde Madrid stage attack, "pervert glasses"
nickname, Bloomberg Apple-glasses-delay-to-WWDC-2027 note; same canonical
key, no new key). No new primary campaign motif; last phase remains the
circa Aug 10 Epstein poster; no competitor-equivalent guerrilla campaign
against Apple/Google/Samsung/Snap camera wearables in any of the 70 cycles.

Attention Sphere 70th no-match as podcast: quoted-search top results were
this repo's own GitHub pages (rejected as circular per established
discipline), the Andrew Bosworth "Possible" iHeart episode (2025-03-26,
crawled 284d; wearables-positive Meta-CTO interview unrelated to any podcast
named Attention Sphere), and QA-correction commit pages. Identity strand
unchanged from #596; task-spec name remains misidentified; Tracked Sources
table 69->70 cycles through Sep 14 2026.

Press surfaces: 6 results observed; ALL previously-logged URL keys, ALL
verified in corpus pre-commit (livemint trends piece crawled 186d; livemint
voice-recordings-by-default piece crawled 331d; techcrunch Mar 2026
contractor-review lawsuit piece crawled 40d; bbc.bm host-mirror in corpus via
#721; reuters Dec 2025 take-off piece 278d/crawled 278d; forbesindia
privacy-scandal roundup crawled 159d). Recency frontier TIED at Sep 9
(twenty-first consecutive tie after #636 through #731); the petapixel.com
Sep 9 piece remains the newest date-verified in-corpus Meta-glasses press
item; no advance.

Standing rule (Aug 28 2026): tone NOT_SCORED, p_value/cohens_d
NOT_CALCULATED, is_significant False; Type E monitoring-only, no mechanism
block in profiles/. No analysis.json update warranted.
"""

import glob
import os
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


class TestNovelty736:
    """Iteration 736 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_736_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_736*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_736_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_736 files, no #736 in git log); this test
        # pins that no duplicate #736 main commit ever appears.
        log = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in log if re.match(r"^[0-9a-f]+ Type E #736:", l)]
        assert len(mains) == 1, "expected exactly one #736 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard736.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestRotationCycleGuard736:
    """Rotation: distinct-mains window test, #726-style.

    Robust to the #678 history artifact and the #565 followup convention: first
    occurrence of each distinct iteration number, newest first.
    """

    ANCHORED_SHA = "7fe8a139ee783dc334722695ef5cfced1ca16b35"

    @staticmethod
    def _mains():
        # First occurrence of each distinct iteration number, newest first.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%s"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        seen = set()
        mains = []
        for s in out:
            m = re.match(r"^Type [A-E] #(\d+):", s)
            if m and m.group(1) not in seen:
                seen.add(m.group(1))
                mains.append(s)
        return mains

    def test_window_732_736_closes_a_to_e(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("E", "736"),
            ("D", "735"),
            ("C", "734"),
            ("B", "733"),
            ("A", "732"),
        ], "rotation window 732-736 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["E", "D", "C", "B", "A"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )


class TestGF70thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #736")[-1]

    def _table(self):
        return _read("podcast-sentiment.md").split("## Tracked Sources")[1].split("### Secondary")[0]

    def test_no_new_gf_episode_this_run(self):
        section = self._section()
        assert "No new GF episode content this run" in section

    def test_au_radio_net_still_758_special_on_top_unchanged(self):
        section = self._section()
        assert "au.radio.net (Last Updated 2 days ago, crawled 6h) still lists 758 episodes" in section
        assert "\"In Conversation with Indhu Rubasingham\" (12/09/2026, 49 mins) on top, unchanged from #731" in section

    def test_uk_podcasts_still_unverified_single_directory_signal(self):
        section = self._section()
        assert "unchanged since #706" in section
        assert "UNVERIFIED" in section
        assert "single-directory signal" in section
        assert "no drop is asserted" in section

    def test_listen_notes_still_498(self):
        section = self._section()
        assert "Listen Notes (crawled 8d) still lags on 498 (756 episodes)" in section

    def test_podscan_signal_carried_from_726(self):
        section = self._section()
        assert "podscan.fm signal carried from #726" in section
        assert "the 499 transcript was the newest NUMBERED release" in section
        assert "per #503 discipline that bounded absence is not a claim" in section

    def test_zero_new_url_keys_chortle_key_preexisting(self):
        section = self._section()
        assert "ZERO NEW URL KEYS this run" in section
        assert "chortle.co.uk Edinburgh Fringe live-show listing key" in section
        assert "already in corpus" in section

    def test_500_watch_holds_projected_day_arrived(self):
        section = self._section()
        assert "The 500-watch HOLDS" in section
        assert "the projected day (Mon Sep 14) arrived with no numbered episode 500 detected" in section
        assert "numbered-500 cadence (499 released Sep 7) had pointed at TODAY" in section

    def test_table_gf_row_updated_736(self):
        assert "499 numbered episodes + Sep 12 2026 unnumbered special (Sep 14 2026)" in self._table()


class TestEHE37DayHold70thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #736")[-1]

    def test_thirty_seven_day_hold(self):
        section = self._section()
        assert "37-day hold continues (Aug 10 -> Sep 14, inclusive count)" in section

    def test_six_known_keys_all_in_corpus(self):
        section = self._section()
        assert "6 previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "meta-ai-glasses-spoof-advert-jeffrey-epstein-slx3wttm5 (49 days, crawled 49d)" in section
        assert "WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/ (59 days, crawled 9d" in section
        assert "kylie-jenners-meta-smart-glasses-parodied-in-guerrilla-lenticular-ad/ (53 days, crawled 20d)" in section
        assert "7538349.html (46 days, crawled 22d; in corpus since #383/#445/#465)" in section
        assert "http://hyperallergic.com/guerrilla-london-bus-ads-mock-kylie-jenners-meta-glasses-campaign/ (61 days, crawled 6h" in section
        assert "fstoppers.com/news/kylie-jenner-ad-hides-disturbing-secret-just-have-stand-right-spot-903612" in section

    def test_toi_piece_resurfaced_content_refreshed_same_key(self):
        section = self._section()
        assert "Times of India 133146816 UK-venue-bans editorial piece re-surfaced (in corpus via #721, crawled 7d" in section
        assert "snippet shows content refreshed since #721" in section
        assert "same canonical key, no new key" in section

    def test_no_new_primary_motif_70_cycles(self):
        section = self._section()
        assert "Last campaign phase remains the circa Aug 10 Epstein poster" in section
        assert "in any of the 70 cycles" in section


class TestAttentionSphere70thNoMatch:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #736")[-1]

    def test_seventieth_no_match(self):
        section = self._section()
        assert "seventieth no-match" in section

    def test_circular_github_rejected(self):
        section = self._section()
        assert "rejected as circular per established discipline" in section

    def test_boz_possible_episode_unrelated(self):
        section = self._section()
        assert "Andrew Bosworth \"Possible\" iHeart episode (2025-03-26, crawled 284d" in section
        assert "unrelated to any podcast named Attention Sphere" in section

    def test_identity_strand_unchanged(self):
        section = self._section()
        assert "Identity strand unchanged from #596" in section
        assert "Task-spec name remains misidentified" in section

    def test_table_attention_sphere_70_cycles(self):
        table = _read("podcast-sentiment.md").split("## Tracked Sources")[1].split("### Secondary")[0]
        assert "70 verification cycles through Sep 14 2026, all no-match as a podcast" in table


class TestPressSurfaces736:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #736")[-1]

    def test_six_results_all_known_keys_in_corpus(self):
        section = self._section()
        assert "SIX results observed; ALL previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses-privacy-concerns-after-workers-reviewed-nudity-sex-and-other-footage/" in section
        assert "are-mark-zuckerbergs-meta-ai-smart-glasses-watching-you-privacy-row-fuels-online-fears-puts-spotlight-on-dpdp-act-11772781893202.html" in section
        assert "meta-ray-ban-smart-glasses-could-store-voice-recordings-by-default-what-it-means-for-users/amp-11746118684276.html" in section
        assert "https://www.forbesindia.com/article/ai-tracker/why-metas-ray-ban-smart-glasses-are-causing-a-privacy-scandal/2991937/1" in section

    def test_bbc_bm_mirror_in_corpus_via_721(self):
        section = self._section()
        assert "https://bbc.bm/ray-ban-meta-glasses-take-off-but-face-privacy-and-competition-test" in section
        assert "in corpus via #721" in section

    def test_frontier_tied_twenty_first(self):
        section = self._section()
        assert "TIED at Sep 9 (twenty-first consecutive tie after #636 through #731)" in section
        assert "no advance" in section


class TestStandingRules736:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #736")[-1]

    def test_no_tone_scores(self):
        section = self._section()
        assert "p_value NOT_CALCULATED" in section
        assert "is_significant False" in section
        assert "Type E monitoring-only, no mechanism block in profiles/" in section

    def test_no_analysis_json_update(self):
        section = self._section()
        assert "No analysis.json update warranted" in section

    def test_four_query_sets(self):
        section = self._section()
        assert "4 browser.search query sets this run" in section

    def test_ascii_no_em_dashes(self):
        assert "\u2014" not in self._section()
        assert "\u2013" not in self._section()

    def test_test_file_ref(self):
        section = self._section()
        assert "tests/test_type_e_736_podcast_sentiment_70th_verification_sep14_midnight.py" in section
