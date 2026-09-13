"""Type E #721: podcast sentiment 67th verification cycle (Sep 13 2026, 09:00 PDT).

Guilty Feminist: NEW EPISODE this run - "In Conversation with Indhu Rubasingham"
(12/09/2026, 49 mins; recorded 9 Sep 2026 at the National Theatre, released 12 Sep),
first new GF episode content in corpus since 499 (Sep 7). UNNUMBERED special (title
lacks the "NNN. Title" convention of the numbered sequence; theatre topic, zero
Meta/AI/wearables/privacy/surveillance in title/description). ie.radio.net (Last
Updated 1 day ago, crawled 4h) lists 758 episodes with this special on top. No
direct episode URL was returned; listing key http://ie.radio.net/podcast/the-guilty-feminist
is already in corpus, so the episode is new content on a logged listing key.
uk-podcasts.co.uk still 758 / "Latest episode: 2026-09-12" (crawled 4h), unchanged
since #706 - still an UNVERIFIED single-directory signal; the Sep 12 date on the new
special corroborates the directory was pointing at THIS special, not a numbered 500;
no drop asserted per #503/iteration-492 discipline. au.radio.net (crawled 4d) still
757 / 499 latest (stale); Listen Notes (crawled 7d) still lags on 498; podscan.fm
(crawled 4h) still shows 499 as newest NUMBERED release. The 500-watch HOLDS: the
penciled Sep 12 item was an unnumbered special, so numbered-500 still points at
Mon Sep 14. Chortle Sep 13 Kings Place LPF 14:00 live show TODAY (crawled 7h) is a
live show, concluded 14:00 BST (06:00 PDT), not episode 500. No first-hand page read
attempted; no tone scores computed (no verified new numbered episode).

EHE 35-day hold continues: 6 previously-logged URL keys, ALL verified in corpus
pre-commit (thetimes Epstein 48d/crawled 48d; engadget WWW-uppercase 58d/crawled 9d,
same page per #676 convention; petapixel lenticular 52d/crawled 19d; latestly
fact-check 45d/crawled 21d; hyperallergic http key 60d/crawled 8d; fstoppers
lenticular re-surfaced crawled 6d). sifted.eu did NOT surface this run. ONE NEW URL
KEY this run: Times of India UK-venue-bans piece
(metas-spy-glasses-face-resistance-in-uk-banned-by-restaurants-pubs-and-theatres-across-the-country/articleshow/133146816;
~33 days old, crawled 6d; surfaced via appwritefunc proxy wrapper; canonical URL
logged verbatim; distinct from the logged toi-plus piece 133054023; zero corpus hits
pre-commit). It is a new-to-corpus editorial press surface mentioning the EHE
campaign (Wetherspoons bans, "pervert glasses", Lorde onstage attack, EHE bus-stop
ads, Meta LED defense, US courtroom bans, Bloomberg/Apple delay). No new primary
campaign motif; last phase remains the circa Aug 10 Epstein poster; no
competitor-equivalent guerrilla campaign in any of the 67 cycles.

Attention Sphere 67th no-match as podcast: quoted-search top results were this
repo's own GitHub pages (rejected as circular per established discipline), the
Andrew Bosworth "Possible" iHeart episode (2025-03-26, crawled 283d; wearables-positive
Meta-CTO interview unrelated to any podcast named Attention Sphere), and
QA-correction commit pages. Identity strand unchanged from #596; task-spec name
remains misidentified; Tracked Sources table 66->67 cycles through Sep 13 2026.

Press surfaces: 6 results observed; 4 previously-logged URL keys verified in corpus
pre-commit (techcrunch Mar 2026 contractor-review lawsuit piece crawled 40d; livemint
trends piece crawled 185d; livemint voice-recordings-by-default piece crawled 330d;
reuters Dec 2025 take-off piece 277d). One additional new URL key that is NOT a new
editorial surface: bbc.bm host-mirror of the in-corpus Reuters Dec 2025 piece (zero
corpus hits pre-commit, logged verbatim, same editorial content). Recency frontier
TIED at Sep 9 (eighteenth consecutive tie after #636 through #716); the petapixel.com
Sep 9 piece remains the newest date-verified in-corpus Meta-glasses press item (the
Times of India piece is ~33 days old, no advance).

Standing rule (Aug 28 2026): tone NOT_SCORED, p_value/cohens_d NOT_CALCULATED,
is_significant False; Type E monitoring-only, no mechanism block in profiles/. No
analysis.json update warranted.
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


class TestNovelty721:
    """Iteration 721 is new; nothing with this number existed pre-commit."""

    def test_single_type_e_721_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_e_721*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_e_721_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_e_721 files, no #721 in git log); this test
        # pins that no duplicate #721 main commit ever appears.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--format=%H %s"],
            capture_output=True,
            text=True,
        )
        mains = [
            line for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type E #721:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type E #721 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        anchor = TestRotationCycleGuard721.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)


class TestRotationCycleGuard721:
    """Rotation: distinct-mains window test, #716-style.

    Robust to the #678 history artifact and the #565 followup convention: first
    occurrence of each distinct iteration number, newest first.
    """

    ANCHORED_SHA = "669e21472354982898003d56a4bc40a8781a569b"

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

    def test_window_717_721_closes_d_to_e(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("E", "721"),
            ("D", "720"),
            ("C", "719"),
            ("B", "718"),
            ("A", "717"),
        ], "rotation window 717-721 wrong: %r" % (observed,)

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


class TestGF67thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #721")[-1]

    def _table(self):
        return _read("podcast-sentiment.md").split("## Tracked Sources")[1].split("### Secondary")[0]

    def test_new_indhu_rubasingham_special_logged(self):
        section = self._section()
        assert "In Conversation with Indhu Rubasingham" in section
        assert "12/09/2026" in section
        assert "49 mins" in section
        assert "recorded 9 September 2026 at the National Theatre" in section
        assert "released 12 September" in section

    def test_special_is_unnumbered_not_500(self):
        section = self._section()
        assert "UNNUMBERED special" in section
        assert 'lacks the "NNN. Title" convention' in section

    def test_special_has_no_meta_wearables_content(self):
        section = self._section()
        assert "zero Meta/AI/wearables/privacy/surveillance in the title or description" in section

    def test_ie_radio_net_lists_758_with_special_on_top(self):
        section = self._section()
        assert "ie.radio.net (Last Updated 1 day ago, crawled 4h) now lists 758 episodes" in section

    def test_no_direct_episode_url_returned_listing_key_already_in_corpus(self):
        section = self._section()
        assert "No direct episode URL was returned" in section
        assert "http://ie.radio.net/podcast/the-guilty-feminist is already in corpus" in section

    def test_uk_podcasts_flip_still_unverified_single_directory_signal(self):
        section = self._section()
        assert "unchanged since #706" in section
        assert "UNVERIFIED" in section
        assert "single-directory signal" in section
        assert "no drop is asserted" in section

    def test_au_radio_net_stale_757_499(self):
        section = self._section()
        assert "au.radio.net (crawled 4d) still lists 757 episodes with 499 latest (stale)" in section

    def test_listen_notes_still_498(self):
        section = self._section()
        assert "Listen Notes (crawled 7d) still lags on 498" in section

    def test_podscan_499_newest_numbered(self):
        section = self._section()
        assert "podscan.fm (crawled 4h) still shows the 499 transcript as the newest NUMBERED release" in section

    def test_500_watch_holds_penciled_mon_sep_14(self):
        section = self._section()
        assert "The 500-watch HOLDS" in section
        assert "still points at Mon Sep 14" in section

    def test_chortle_live_show_today_concluded(self):
        section = self._section()
        assert "Chortle Sep 13 Kings Place LPF 14:00 live show TODAY (crawled 7h this run)" in section
        assert "concluded 14:00 BST (06:00 PDT)" in section

    def test_table_gf_row_updated(self):
        assert "499 numbered episodes + Sep 12 2026 unnumbered special (Sep 13 2026)" in self._table()

    def test_table_gf_row_notes_new_special(self):
        assert '"In Conversation with Indhu Rubasingham" special (theatre topic, zero Meta/wearables content)' in self._table()


class TestEHE35DayHold67thCycle:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #721")[-1]

    def test_six_known_keys_all_in_corpus(self):
        section = self._section()
        assert "6 previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "meta-ai-glasses-spoof-advert-jeffrey-epstein-slx3wttm5 (48 days, crawled 48d)" in section
        assert "WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/ (58 days, crawled 9d" in section
        assert "kylie-jenners-meta-smart-glasses-parodied-in-guerrilla-lenticular-ad/ (52 days, crawled 19d)" in section
        assert "7538349.html (45 days, crawled 21d; in corpus since #383/#445/#465)" in section
        assert "http://hyperallergic.com/guerrilla-london-bus-ads-mock-kylie-jenners-meta-glasses-campaign/ (60 days, crawled 8d" in section
        assert "fstoppers.com/news/kylie-jenner-ad-hides-disturbing-secret-just-have-stand-right-spot-903612" in section

    def test_sifted_absent_this_run(self):
        section = self._section()
        assert "sifted.eu did NOT surface this run" in section

    def test_new_times_of_india_url_key_logged_verbatim(self):
        section = self._section()
        assert "https://timesofindia.indiatimes.com/technology/tech-news/metas-spy-glasses-face-resistance-in-uk-banned-by-restaurants-pubs-and-theatres-across-the-country/articleshow/133146816.cms" in section
        assert "distinct from the logged toi-plus \"i-spy-with-my-smart-glasses\" piece 133054023" in section
        assert "zero corpus hits pre-commit" in section

    def test_new_key_is_editorial_surface_mentioning_ehe(self):
        section = self._section()
        assert "new-to-corpus editorial press surface mentioning the EHE campaign" in section
        assert "Wetherspoons" in section

    def test_no_new_primary_motif_67_cycles(self):
        section = self._section()
        assert "Last campaign phase remains the circa Aug 10 Epstein poster" in section
        assert "in any of the 67 cycles" in section


class TestAttentionSphere67thNoMatch:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #721")[-1]

    def test_sixty_seventh_no_match(self):
        section = self._section()
        assert "sixty-seventh no-match" in section

    def test_circular_github_rejected(self):
        section = self._section()
        assert "rejected as circular per established discipline" in section

    def test_boz_possible_episode_unrelated(self):
        section = self._section()
        assert "Andrew Bosworth \"Possible\" iHeart episode (2025-03-26, crawled 283d" in section
        assert "unrelated to any podcast named Attention Sphere" in section

    def test_identity_strand_unchanged(self):
        section = self._section()
        assert "Identity strand unchanged from #596" in section
        assert "Task-spec name remains misidentified" in section

    def test_table_attention_sphere_67_cycles(self):
        table = _read("podcast-sentiment.md").split("## Tracked Sources")[1].split("### Secondary")[0]
        assert "67 verification cycles through Sep 13 2026, all no-match as a podcast" in table


class TestPressSurfaces721:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #721")[-1]

    def test_four_known_keys_in_corpus(self):
        section = self._section()
        assert "4 previously-logged URL keys, ALL verified in corpus pre-commit" in section
        assert "techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses-privacy-concerns-after-workers-reviewed-nudity-sex-and-other-footage/" in section
        assert "are-mark-zuckerbergs-meta-ai-smart-glasses-watching-you-privacy-row-fuels-online-fears-puts-spotlight-on-dpdp-act-11772781893202.html" in section
        assert "meta-ray-ban-smart-glasses-could-store-voice-recordings-by-default-what-it-means-for-users/amp-11746118684276.html" in section

    def test_bbc_bm_mirror_new_key_not_new_surface(self):
        section = self._section()
        assert "https://www.bbc.bm/ray-ban-meta-glasses-take-off-but-face-privacy-and-competition-test" in section
        assert "host-mirror of the in-corpus Reuters Dec 2025 piece" in section
        assert "not a new editorial surface" in section

    def test_frontier_tied_eighteenth(self):
        section = self._section()
        assert "TIED at Sep 9 (eighteenth consecutive tie after #636 through #716)" in section
        assert "no advance" in section

    def test_roadtovr_v26_in_corpus(self):
        section = self._section()
        assert "https://roadtovr.com/meta-ray-ban-glasses-privacy-led-camera-update/" in section


class TestStandingRules721:
    def _section(self):
        return _read("podcast-sentiment.md").split("## Iteration #721")[-1]

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
        assert "tests/test_type_e_721_podcast_sentiment_67th_verification_sep13_9am.py" in section
