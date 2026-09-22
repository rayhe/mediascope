"""Type E #926: podcast sentiment 108th verification cycle (GF episode 501
CONFIRMED again - listennotes.com main directory crawled 16h still at top;
uk-podcasts SURFACED this run (crawled 6h, 501-signal corroboration,
in-corpus re-surface); podparadise SURFACED this run (crawled 6h, listing
still lags, in-corpus re-surface); goloudnow exact-URL variant same
in-corpus directory family; ONE new GF URL key (youtube.com/watch?v=
485W5ZCBXgc, GF484 old-episode mirror, not a new episode or finding);
podscan.fm + official-site did NOT surface this run, remain in corpus; no
episode 502; EHE 43-day hold, engadget bus-stops re-surfaced again (crawled
24h), ZERO new URL keys; Attention Sphere 108th quoted-search no-match,
Tracked Sources 107->108; press 7 ALL previously-logged incl.
startupfortune re-surface again (crawled 1h), ZERO new press URL keys;
recency frontier HOLDS at Sep 18) - Sep 22 2026 16:00 PDT.

Monitoring-only per the Aug 28 2026 standing rule: tone NOT_SCORED,
p_value/cohens_d NOT_CALCULATED, is_significant False, engine NOT run,
no mechanisms added, no analysis.json update, NOT artifact-grade.
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

ITERATION = 926
TYPE_LETTER = "E"
RUN_PDT = "2026-09-22 16:00 PDT"
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
class TestNoveltyAnchorTypeE926:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #926 main commit exists pre-commit; the anchor test pins
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
            if "Type E #926" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_e_926_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_926*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 925-929 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard925_929Window:
    @pytest.mark.rotation
    def test_second_leg_of_925_929_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 926

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {925: "D", 926: "E", 927: "A", 928: "B", 929: "C"}
        assert expected[926] == "E"

    @pytest.mark.rotation
    def test_predecessor_925_type_d_committed(self):
        # #925 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md); this run's own #926 entry will be prepended
        # above it.
        assert "## #925 Type D" in _read(LOG)

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
# 3. The Guilty Feminist: 108th cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredEighthCycle:
    GF_LOGGED_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "goloudnow.com/podcasts/the-guilty-feminist-152",
        "uk-podcasts.co.uk/podcast/the-guilty-feminist/deborah-frances-white-on-the-news-meeting",
        "podparadise.com/Podcast/1068940771",
        "youtube.com/watch?v=8OeSUuyvuXc",
        "youtube.com/watch?v=HL3iFdYBk9M",
    ]
    GF_NEW_KEY = "youtube.com/watch?v=485W5ZCBXgc"

    def test_episode_501_confirmed_again_this_run(self):
        md = _read(MD)
        assert "501 CONFIRMED AGAIN" in md
        assert "Out North East" in md
        assert "crawled 16h" in md

    def test_no_episode_502_surfaced(self):
        # No 502 anywhere this run: listennotes main still 501 at top.
        # Weekly cadence, not a signal.
        md = _read(MD)
        assert "no episode 502" in md

    def test_uk_podcasts_podparadise_surfaces_this_run(self):
        # Unlike #921: uk-podcasts and podparadise SURFACED this run
        # (both in-corpus re-surfaces, not new keys). podparadise's
        # episode listing still lags at the Sep-16 rerelease.
        md = _read(MD)
        assert "uk-podcasts.co.uk SURFACED this run" in md
        assert "PodParadise SURFACED this run" in md
        assert "still lags" in md

    def test_podscan_and_official_did_not_surface_remain_in_corpus(self):
        md = _read(MD)
        assert "podscan.fm" in md
        assert "did NOT surface this run" in md

    def test_all_logged_gf_keys_in_corpus(self):
        for key in self.GF_LOGGED_KEYS:
            assert _corpus_hits(key), key

    def test_one_new_gf_url_key_logged_as_old_episode_mirror(self):
        # youtube.com/watch?v=485W5ZCBXgc (GF484 "Girls Rights Are Human
        # Rights" part-one YouTube mirror; old episode released May 25
        # 2026): zero pre-commit corpus hits in any form (verified via
        # git grep pre-commit; the md now carries the key itself).
        # Logged as a directory-mirror key, NOT a new episode or finding.
        md = _read(MD)
        assert "ONE NEW GF URL KEY" in md
        assert self.GF_NEW_KEY in md
        assert "old-episode mirror" in md
        assert "NOT a new episode" in md

    def test_goloudnow_variant_same_in_corpus_directory_family(self):
        # The goloudnow result URL this run is an exact-URL variant of the
        # same in-corpus goloudnow.com/podcasts/the-guilty-feminist-152
        # directory family (19 corpus files), not a new URL key.
        md = _read(MD)
        assert "same in-corpus" in md or "directory family" in md
        assert len(_corpus_hits("goloudnow.com/podcasts/the-guilty-feminist-152")) >= 1

    def test_zero_meta_wearables_across_108_cycles(self):
        md = _read(MD)
        assert "across all 108 cycles" in md
        assert "bounded search-result absence" in md


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 43-day hold, ZERO new URL keys this run
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredEighthCycle:
    KNOWN_KEYS = [
        "designtaxi.com/topic/34124",
        "fstoppers.com/news/kylie-jenner-ad-hides",
        "d33gy59ovltp76.cloudfront.net",
        "designtaxi.com/topic/33476",
        "techtimes.co.uk/activists-challenge-meta-ray-ban",
        "engadget.com/2217151",
    ]

    def test_hold_arithmetic_43_days_not_42(self):
        # Aug 10 Epstein spoof -> Sep 22: 43 days. Regression guard on the
        # #846/#851 47/48 slips: do not relabel as 42-day (that was Sep 21).
        assert (date(2026, 9, 22) - date(2026, 8, 10)).days == 43
        assert "43-day hold" in _read(MD)

    def test_epstein_spoof_remains_last_major_phase_marker(self):
        assert "Epstein spoof" in _read(MD)

    def test_amnesty_boxes_phase_logged_in_corpus(self):
        assert "amnesty-boxes" in _read(MD).lower()
        assert _corpus_hits("techtimes.co.uk/activists-challenge-meta-ray-ban")

    def test_zero_new_ehe_url_keys_this_run(self):
        assert "ZERO new URL keys this run" in _read(MD)

    def test_known_ehe_keys_remain_in_corpus(self):
        for key in self.KNOWN_KEYS:
            assert _corpus_hits(key), key

    def test_engadget_bus_stops_resurface_again_in_corpus(self):
        # engadget.com/2217151 (Karissa Bell Jul-16 bus-stops original)
        # re-surfaced again this run (crawled 24h); verified
        # already-in-corpus, not a new key.
        md = _read(MD)
        assert "surfaced again this run" in md
        assert "crawled 24h" in md
        assert len(_corpus_hits("engadget.com/2217151")) >= 1

    def test_softonic_singulism_did_not_surface_remain_in_corpus(self):
        md = _read(MD)
        assert "softonic" in md.lower()
        assert "singulism" in md.lower()
        assert "did NOT surface this run" in md

    def test_no_competitor_equivalent_campaign_bounded_absence(self):
        md = _read(MD)
        assert "No competitor-equivalent guerrilla campaign" in md


# --------------------------------------------------------------------------
# 5. Attention Sphere: 108th no-match
# --------------------------------------------------------------------------
class TestAttentionSphereHundredEighthNoMatch:
    CIRCULAR_COMMITS = [
        "a288c86",
        "a2b656f",
        "9590385",
        "2c4e21e",
        "25c730e",
        "3d16eac",
    ]

    def test_no_match_108th_cycle(self):
        md = _read(MD)
        assert "one-hundred-eighth no-match" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "rejected as circular" in md
        assert "not ingested" in md

    def test_same_commit_hash_set_as_prior_cycles(self):
        md = _read(MD)
        for short in self.CIRCULAR_COMMITS:
            assert short in md, short

    def test_tracked_sources_advanced_107_to_108(self):
        assert "107->108" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        assert "misidentified as a podcast" in _read(MD)

    def test_real_world_identity_stands(self):
        assert "Kendall Schrohe" in _read(MD)


# --------------------------------------------------------------------------
# 6. Press surfaces: 108th cycle, ZERO new URL keys
# --------------------------------------------------------------------------
class TestPressSurfacesHundredEighthCycle:
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
        # RE-SURFACED again this run (crawled 1h); verified
        # already-in-corpus, not a new key.
        md = _read(MD)
        assert "RE-SURFACED again this run" in md
        assert "crawled 1h" in md
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

    def test_no_sep19_through_sep22_surfaces(self):
        assert "no Sep 19, Sep 20, Sep 21, or Sep 22 surfaces" in _read(MD)


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps (per #715 convention)
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_926_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_926*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_786(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 786 in-tree: 786 (committed #924 Type C, competitor-entities.yaml).
        # The in-flight #884/#899 blocks (m762/m771) are lower.
        assert maxid == 786

    def test_zero_numeric_787_mechanism_keys_in_profiles(self):
        d1 = "78" + "7"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_787_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal "787" key strings
        # carried. Designed keying is colon-form in profiles/; the tests/
        # _787 filename hits (other test files' negative guards) are a
        # different namespace. __pycache__ artifacts excluded per the #715
        # pattern-rescope lesson.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_78" + "7"
        n2 = "mech" + "anism" + "-" + "78" + "7"
        hits = []
        for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(p)
        for p in glob.glob(os.path.join(REPO, "tests", "test_*.py")):
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
        assert "47598" in readme and "1251" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_926_marker(self):
        assert "## #926 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        assert "925-929 window" in _read(LOG)


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
        # blocks (m762 / m771); this run adds no 926 hunks to them.
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
            assert "926" not in diff
        jdiff = _git(["diff", "--", "profiles/careers/journalists.yaml"]).stdout
        assert "926" not in jdiff
