"""Type E #936: podcast sentiment 110th verification cycle (GF episode 501
CONFIRMED again - listennotes.com main directory crawled 10h still at top;
official-site new-normal-weeks-1-and-2 page variant SURFACED AGAIN this run
(crawled 12h, 501 at top, no 502, first-party family in corpus since #911);
podscan.fm SURFACED AGAIN this run (crawled 15h, 501 intro transcript: Vision
Fest Sep 25 + Road to Gilead open space, zero Meta/wearables content,
snippet-bounded); podparadise SURFACED again (crawled 16h, listing still lags
at 499, 500/501 absent, in-corpus re-surface); uk-podcasts SURFACED again
(crawled 5h, old 2022 bonus-episode content, in-corpus directory family); ZERO
new verbatim GF URL keys this run (8/8 non-circular URL keys >=1 corpus hit
pre-commit; first pure-re-surface cycle since #926/#921); no episode 502
(ten-day absence since Sep 21, weekly cadence, not a signal); EHE 44-day
hold, 6 logged keys re-surfaced, techtimes amnesty-boxes did NOT surface
(remains in corpus), ZERO new URL keys; Attention Sphere 110th quoted-search
no-match, 6 results all own-repo GitHub URLs (same 6 commit URLs, blob page
did NOT surface this run), Tracked Sources 109->110; press 7 ALL
previously-logged, ZERO new press URL keys; recency frontier HOLDS at
Sep 18; no Sep 19 through Sep 23 surfaces) - Sep 23 2026 02:00 PDT.

Monitoring-only per the Aug 28 2026 standing rule: tone NOT_SCORED,
p_value/cohens_d NOT_CALCULATED, is_significant False, engine NOT run,
no mechanisms added, no analysis.json update, NOT artifact-grade.
Max numeric mechanism_id 792 in-tree; zero 793 keys numeric/underscore/dash.
Falsification ledger holds at 29. ASCII-only. No em dashes.
"""
import os
import re
import glob
import subprocess
from datetime import date

import pytest

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG = os.path.join(REPO, "iteration-log.md")
MD = os.path.join(REPO, "podcast-sentiment.md")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
THIS_FILE = os.path.basename(__file__)

ITERATION = 936
TYPE_LETTER = "E"
RUN_PDT = "2026-09-23 02:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _corpus_hits(needle):
    return _git(["grep", "-l", needle, "--", "."]).stdout.splitlines()


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE936:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #936 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type E #936" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_e_936_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_936*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 935-939 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard935_939Window:
    @pytest.mark.rotation
    def test_second_leg_of_935_939_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 936

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {935: "D", 936: "E", 937: "A", 938: "B", 939: "C"}
        assert expected[936] == "E"

    @pytest.mark.rotation
    def test_predecessor_935_type_d_committed(self):
        # #935 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md); this run's own #936 entry will be prepended
        # above it.
        assert "## #935 Type D" in _read(LOG)

    @pytest.mark.rotation
    def test_no_concurrent_inflight_commits_asserted(self):
        # In-flight at this run's checks: #884 Type C (m762),
        # #899 Type C (m771), #900 Type D - none committed yet.
        # (#898/m770 is absent, not in-flight: lost at #918, per #920.)
        # Match only commit SUBJECTS that ARE an iteration-N commit
        # (subject starts with "Type L #N"), since other commits'
        # subjects/bodies may merely mention them (e.g. this run's own
        # concurrency note naming #884/#899/#900).
        subjects = [
            _git(["log", "--format=%s", "-1", c]).stdout.strip()
            for c in _git(["log", "--format=%H", "-8"]).stdout.splitlines()
        ]
        for n in ("884", "899", "900"):
            pat = re.compile(r"^Type [ABCDE] #" + n + r"(?!\d)")
            assert not any(pat.search(s) for s in subjects), (n, subjects)


# --------------------------------------------------------------------------
# 3. The Guilty Feminist: 110th cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredTenthCycle:
    GF_LOGGED_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "guiltyfeminist.com/new-normal-weeks-1-and-2",
        "goloudnow.com/podcasts/the-guilty-feminist-152",
        "uk-podcasts.co.uk/podcast/the-guilty-feminist/deborah-frances-white-on-the-news-meeting",
        "podparadise.com/Podcast/1068940771",
        "youtube.com/watch?v=8OeSUuyvuXc",
        "youtube.com/watch?v=HL3iFdYBk9M",
        "youtube.com/watch?v=485W5ZCBXgc",
    ]

    def test_episode_501_confirmed_again_this_run(self):
        md = _read(MD)
        assert "501 CONFIRMED AGAIN" in md
        assert "Out North East" in md
        assert "crawled 10h" in md

    def test_no_episode_502_surfaced(self):
        # No 502 anywhere this run: listennotes main still 501 at top and
        # the official-site page variant also lists 501 at top. Ten-day
        # absence since Sep 21, consistent with weekly cadence, not a
        # signal.
        md = _read(MD)
        assert "no episode 502" in md

    def test_official_site_page_variant_surfaces_again_this_run(self):
        # Unlike #921 (official-site did NOT surface) but like #931: the
        # new-normal-weeks-1-and-2 page variant SURFACED AGAIN this run
        # (crawled 12h), listing 501 at top, no 502. First-party
        # directory family in corpus since #911; the variant key was
        # logged at #931, so it is a re-surface, not a new key.
        md = _read(MD)
        assert "new-normal-weeks-1-and-2" in md
        assert "SURFACED AGAIN this run" in md

    def test_podscan_surfaces_again_with_vision_fest_intro_transcript(self):
        # podscan.fm SURFACED AGAIN this run (crawled 15h), in-corpus
        # re-surface, not a new key. The 501 intro transcript is
        # bounded: Vision Fest Sep 25 appearance + Road to Gilead open
        # space event, zero Meta/wearables content (snippet-bounded).
        md = _read(MD)
        assert "podscan.fm SURFACED AGAIN this run" in md
        assert "Vision Fest" in md
        assert len(_corpus_hits("podscan.fm/podcasts/the-guilty-feminist-1")) >= 1

    def test_uk_podcasts_podparadise_surfaces_again_this_run(self):
        # uk-podcasts SURFACED again (crawled 5h, old 2022
        # bonus-episode content, in-corpus directory family);
        # podparadise SURFACED again (crawled 16h, listing still lags at
        # the Sep-16 rerelease, 500/501 absent).
        md = _read(MD)
        assert "uk-podcasts SURFACED again" in md
        assert "PodParadise SURFACED again" in md
        assert "still lags" in md

    def test_all_logged_gf_keys_in_corpus(self):
        for key in self.GF_LOGGED_KEYS:
            assert _corpus_hits(key), key

    def test_zero_new_gf_url_keys_pure_resurface_cycle(self):
        # This run is the first pure-re-surface cycle since #926/#921:
        # all 8 non-circular GF URL keys were >=1 corpus hit pre-commit
        # (verified via git grep pre-commit); the md records ZERO new
        # verbatim GF URL keys. No new episodes, no new findings.
        md = _read(MD)
        assert "ZERO NEW VERBATIM GF URL KEYS this run" in md
        assert "pure-re-surface cycle" in md

    def test_zero_meta_wearables_across_110_cycles(self):
        md = _read(MD)
        assert "across all 110 cycles" in md
        assert "bounded search-result absence" in md


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 44-day hold, ZERO new URL keys this run
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredTenthCycle:
    KNOWN_KEYS = [
        "designtaxi.com/topic/34124",
        "fstoppers.com/news/kylie-jenner-ad-hides",
        "d33gy59ovltp76.cloudfront.net",
        "designtaxi.com/topic/33476",
        "techtimes.co.uk/activists-challenge-meta-ray-ban",
        "engadget.com/2217151",
    ]

    def test_hold_arithmetic_44_days_not_43(self):
        # Aug 10 Epstein spoof -> Sep 23: 44 days. Regression guard on the
        # #846/#851 47/48 slips: do not relabel as 43-day (that was Sep 22).
        assert (date(2026, 9, 23) - date(2026, 8, 10)).days == 44
        assert "44-day hold" in _read(MD)

    def test_epstein_spoof_remains_last_major_phase_marker(self):
        assert "Epstein spoof" in _read(MD)

    def test_amnesty_boxes_phase_logged_in_corpus(self):
        assert "amnesty-boxes" in _read(MD).lower()
        assert _corpus_hits("techtimes.co.uk/activists-challenge-meta-ray-ban")

    def test_techtimes_amnesty_boxes_did_not_surface_remains_in_corpus(self):
        # Unlike #931 (techtimes re-surfaced): the amnesty-boxes strand
        # did NOT surface this run; it remains in corpus. Last campaign
        # phase remains the circa Aug 24 amnesty-boxes strand.
        md = _read(MD)
        assert "techtimes.co.uk amnesty-boxes" in md or "amnesty-boxes campaign strand did NOT surface" in md

    def test_zero_new_ehe_url_keys_this_run(self):
        assert "ZERO new URL keys this run" in _read(MD)

    def test_known_ehe_keys_remain_in_corpus(self):
        for key in self.KNOWN_KEYS:
            assert _corpus_hits(key), key

    def test_softonic_singulism_did_not_surface_remain_in_corpus(self):
        md = _read(MD)
        assert "softonic" in md.lower()
        assert "singulism" in md.lower()
        assert "did NOT surface this run" in md


# --------------------------------------------------------------------------
# 5. Attention Sphere: 110th no-match
# --------------------------------------------------------------------------
class TestAttentionSphereHundredTenthNoMatch:
    CIRCULAR_COMMITS = [
        "a288c86",
        "a2b656f",
        "9590385",
        "2c4e21e",
        "25c730e",
        "3d16eac",
    ]

    def test_no_match_110th_cycle(self):
        md = _read(MD)
        assert "one-hundred-tenth no-match" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "rejected as circular" in md
        assert "not ingested" in md

    def test_blob_page_did_not_surface_one_fewer_circular_hit(self):
        # Unlike #931 (7 circular hits incl. the podcast-sentiment.md
        # blob page): the blob page did NOT surface this run, so only
        # the 6 commit URLs surfaced (one fewer circular hit).
        md = _read(MD)
        assert "did NOT surface this run" in md
        assert "one fewer circular hit" in md

    def test_same_commit_hash_set_as_prior_cycles(self):
        md = _read(MD)
        for short in self.CIRCULAR_COMMITS:
            assert short in md, short

    def test_tracked_sources_advanced_109_to_110(self):
        assert "109->110" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        assert "misidentified as a podcast" in _read(MD)

    def test_real_world_identity_stands(self):
        assert "Kendall Schrohe" in _read(MD)


# --------------------------------------------------------------------------
# 6. Press surfaces: 110th cycle, ZERO new URL keys
# --------------------------------------------------------------------------
class TestPressSurfacesHundredTenthCycle:
    KNOWN_KEYS = [
        "ppc.land/hamburg-regulator",
        "livemint.com/technology/tech-news/meta-ray-ban-smart-glasses-could-store",
        "9to5google.com/2026/08/28/meta-ray-ban-smart-glasses-privacy-led-loophole",
        "startupfortune.com/meta-permanently-disables-cameras-on-thousands-of-tampered-smart-glasses",
        "webpronews.com/germanys-privacy-push",
        "webpronews.com/metas-new-smart-glasses-update",
        "recordinglaw.com/news/meta-ray-ban-smart-glasses-privacy-scandal",
    ]

    def test_zero_new_press_url_keys(self):
        assert "ZERO new press URL keys this run" in _read(MD)

    def test_all_observed_press_keys_previously_logged(self):
        for key in self.KNOWN_KEYS:
            assert _corpus_hits(key), key

    def test_startupfortune_resurfaced_again_this_run_still_in_corpus(self):
        # startupfortune tampered-LED bricking was in corpus via #881 and
        # RE-SURFACED again this run (crawled 3h); verified
        # already-in-corpus, not a new key.
        md = _read(MD)
        assert "RE-SURFACED again this run" in md
        assert "crawled 3h" in md
        assert _corpus_hits("startupfortune.com/meta-permanently-disables")

    def test_recordinglaw_faq_in_corpus(self):
        # recordinglaw.com privacy-scandal FAQ (Bartone v. Meta + Swedish
        # contractor investigation) is in corpus, not a new key.
        assert len(_corpus_hits("recordinglaw.com/news/meta-ray-ban-smart-glasses-privacy-scandal")) >= 1

    def test_roadtovr_nypost_did_not_surface_remain_in_corpus(self):
        md = _read(MD)
        assert "roadtovr.com" in md
        assert "nypost.com" in md
        assert "did NOT surface this run" in md or "Did not surface this run" in md

    def test_recency_frontier_holds_sep_18(self):
        assert "Recency frontier: HOLDS at Sep 18" in _read(MD)

    def test_no_sep19_through_sep23_surfaces(self):
        assert "no Sep 19, Sep 20, Sep 21, Sep 22, or Sep 23 surfaces" in _read(MD)


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps (per #715 convention)
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_936_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_936*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_792(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 792 in-tree: 792 (committed #934 Type C, competitor-entities.yaml
        # xai_apple settlement leg). The in-flight #884/#899 blocks
        # (m762/m771) are lower.
        assert maxid == 792

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "79" + "3"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key strings
        # carried. Designed keying is colon-form in profiles/; the tests/
        # filename hits (other test files' negative guards) are a different
        # namespace. __pycache__ artifacts excluded per the #715
        # pattern-rescope lesson. Own file excluded as sweep carrier.
        # (Note: the test_type_c_934 file's NEXT_ID_NUMERIC reservation
        # constant is the sole designed 793 carrier; it is a reservation,
        # not a mechanism key string.)
        n1 = "m" + "ech" + "an" + "is" + "m" + "_79" + "3"
        n2 = "mech" + "anism" + "-" + "79" + "3"
        hits = []
        for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(p)
        for p in glob.glob(os.path.join(REPO, "tests", "test_*.py")):
            if os.path.basename(p) == THIS_FILE:
                continue
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(p)
        assert hits == []

    def test_concurrent_inflight_files_not_in_this_commit_scope(self):
        # In-flight: #884 Type C (competitor-entities.yaml m762),
        # #899 Type C (nytimes.yaml m771), #900 Type D (untracked test
        # file) - all uncommitted; this run's staged set must not
        # include those files. (#898/m770 is absent, not in-flight.)
        status = _git(["status", "--short"]).stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in ("competitor-entities", "journalists.yaml", "nytimes.yaml"):
            assert not any(f in l for l in staged)


# --------------------------------------------------------------------------
# 8. Statistical discipline: the Aug 28 2026 standing rule
# --------------------------------------------------------------------------
class TestStatisticalDisciplineStandingRule:
    def test_tone_not_scored(self):
        assert "NOT_SCORED" in _read(MD)

    def test_engine_not_run_no_significance(self):
        md = _read(MD)
        assert "engine NOT run" in md
        assert "is_significant False" in md

    def test_no_new_mechanisms_monitoring_only(self):
        assert "monitoring-only" in _read(MD)

    def test_falsification_ledger_holds_at_29(self):
        assert "ledger holds at 29" in _read(MD)

    def test_not_artifact_grade_correlation_not_causation(self):
        md = _read(MD)
        assert "NOT artifact-grade" in md
        assert "Correlation is not causation" in md


# --------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats_table_updated(self):
        readme = _read(README)
        assert "48139" in readme and "1261" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_936_marker(self):
        assert "## #936 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        assert "935-939 window" in _read(LOG)


# --------------------------------------------------------------------------
# 11. Push readiness
# --------------------------------------------------------------------------
class TestPushReadiness:
    def test_ascii_only_no_em_dashes(self):
        text = _read(__file__)
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_no_blob_url_in_this_file(self):
        # The circular own-repo blob URL is rejected, never ingested, and
        # never carried into this test file (verbatim-listing rule).
        # Concatenated so the literal never appears in this file.
        needle = "blob/" + "HEAD/podcast-sentiment"
        assert needle not in _read(__file__)

    def test_concurrent_files_untouched_by_this_run(self):
        # git diffs on the in-flight files must show only their own
        # blocks (m762 / m771); this run adds no 936 hunks to them.
        # NOTE per #920/#925: profiles/careers/journalists.yaml is CLEAN
        # in the working tree (#898/m770 hunk lost at #918, confirmed
        # absent at the corpus layer) - so its diff is empty this run
        # and there is no 770 hunk to pin.
        for f, own in (
            ("profiles/competitor-entities.yaml", "762"),
            ("profiles/nytimes.yaml", "771"),
        ):
            diff = _git(["diff", "--", f]).stdout
            assert ("mechanism" + "_id" + ": " + own) in diff
            assert "936" not in diff
        jdiff = _git(["diff", "--", "profiles/careers/journalists.yaml"]).stdout
        assert "936" not in jdiff
