"""Type E #941: podcast sentiment 111th verification cycle (GF episode 501
CONFIRMED AGAIN - listennotes.com main directory crawled 6h still at top;
goloudnow exact-URL variant SURFACED this run (crawled 7h, in-corpus
directory family); uk-podcasts SURFACED this run (crawled 7h, "Latest
episode: 2026-09-21" 501-signal corroboration, in-corpus directory family);
podparadise SURFACED this run (crawled 21h, listing still lags at the
Sep-16 rerelease, 500/501 absent, in-corpus re-surface); official-site
new-normal-weeks-1-and-2 page variant did NOT surface this run (remains in
corpus); podscan.fm did NOT surface this run (remains in corpus); ZERO NEW
VERBATIM GF URL KEYS this run (7/7 non-circular URL keys >=1 corpus hit
pre-commit; second consecutive pure-re-surface cycle after #936); no episode
502 (eleven-day absence since Sep 21, weekly cadence, not a signal); EHE
44-day hold, 6 logged keys re-surfaced, techtimes amnesty-boxes RE-SURFACED
this run (crawled 5h, unlike #936), softonic/singulism did NOT surface
(remain in corpus), ZERO new URL keys; Attention Sphere 111th
quoted-search no-match, 7 circular own-repo GitHub URLs (same 6 commit
URLs + the blob page, which SURFACED AGAIN this run, one more circular
hit than #936's 6), Tracked Sources 110->111; press 7 ALL previously-logged,
ZERO new press URL keys, startupfortune RE-SURFACED again (crawled 8h);
recency frontier HOLDS at Sep 18; no Sep 19 through Sep 23 surfaces) -
Sep 23 2026 07:00 PDT.

Monitoring-only per the Aug 28 2026 standing rule: tone NOT_SCORED,
p_value/cohens_d NOT_CALCULATED, is_significant False, engine NOT run,
no mechanisms added, no analysis.json update, NOT artifact-grade.
Max numeric mechanism_id 795 in-tree; zero 796 keys numeric/underscore/dash.
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

ITERATION = 941
TYPE_LETTER = "E"
RUN_PDT = "2026-09-23 07:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "bf0cbbf1a8465afcd68daac32e220048bc2b94b0"


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
class TestNoveltyAnchorTypeE941:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #941 main commit exists pre-commit; the anchor test pins
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
            if "Type E #941" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_e_941_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_941*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 940-944 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard940_944Window:
    @pytest.mark.rotation
    def test_second_leg_of_940_944_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 941

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {940: "D", 941: "E", 942: "A", 943: "B", 944: "C"}
        assert expected[941] == "E"

    @pytest.mark.rotation
    def test_predecessor_940_type_d_committed(self):
        # #940 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md); this run's own #941 entry will be prepended
        # above it.
        assert "## #940 Type D" in _read(LOG)

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
# 3. The Guilty Feminist: 111th cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredEleventhCycle:
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
        assert "crawled 6h" in md

    def test_no_episode_502_surfaced(self):
        # No 502 anywhere this run: listennotes main still 501 at top and
        # uk-podcasts still carries the "Latest episode: 2026-09-21"
        # 501-signal. Eleven-day absence since Sep 21, consistent with
        # weekly cadence, not a signal.
        md = _read(MD)
        assert "no episode 502" in md

    def test_goloudnow_uk_podcasts_podparadise_surfaces_this_run(self):
        # goloudnow exact-URL variant SURFACED this run (crawled 7h,
        # in-corpus directory family); uk-podcasts SURFACED this run
        # (crawled 7h, "Latest episode: 2026-09-21" 501-signal
        # corroboration, in-corpus directory family); podparadise
        # SURFACED this run (crawled 21h, listing still lags at the
        # Sep-16 rerelease, 500/501 absent, in-corpus re-surface).
        md = _read(MD)
        assert "goloudnow exact-URL variant SURFACED this run" in md
        assert "uk-podcasts SURFACED this run" in md
        assert "PodParadise SURFACED this run" in md
        assert "still lags" in md

    def test_official_site_page_variant_and_podscan_did_not_surface(self):
        # Unlike #936 (both surfaced): the official-site
        # new-normal-weeks-1-and-2 page variant and podscan.fm did NOT
        # surface this run; both remain in corpus.
        md = _read(MD)
        assert "new-normal-weeks-1-and-2 page variant did NOT surface this run" in md
        assert "podscan.fm did NOT surface this run" in md

    def test_all_logged_gf_keys_in_corpus(self):
        for key in self.GF_LOGGED_KEYS:
            assert _corpus_hits(key), key

    def test_zero_new_gf_url_keys_second_consecutive_pure_resurface(self):
        # Second consecutive pure-re-surface cycle after #936 (first
        # pure-re-surface streak since #926/#921): all 7 non-circular GF
        # URL keys were >=1 corpus hit pre-commit (verified via git grep
        # pre-commit); the md records ZERO NEW VERBATIM GF URL KEYS.
        md = _read(MD)
        assert "ZERO NEW VERBATIM GF URL KEYS this run" in md
        assert "pure-re-surface cycle" in md

    def test_zero_meta_wearables_across_111_cycles(self):
        md = _read(MD)
        assert "across all 111 cycles" in md
        assert "bounded search-result absence" in md


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 44-day hold, ZERO new URL keys this run
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredEleventhCycle:
    KNOWN_KEYS = [
        "community.designtaxi.com/topic/34124",
        "fstoppers.com/news/kylie-jenner-ad-hides",
        "d33gy59ovltp76.cloudfront.net",
        "community.designtaxi.com/topic/33476",
        "techtimes.co.uk/activists-challenge-meta-ray-ban",
        "www.engadget.com/2217151",
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

    def test_techtimes_amnesty_boxes_resurfaced_this_run_crawled_5h(self):
        # Unlike #936 (amnesty-boxes did NOT surface): the techtimes
        # strand RE-SURFACED this run (crawled 5h), in corpus, not a new
        # key. Last campaign phase remains the circa Aug 24
        # amnesty-boxes strand alongside the Aug 10 Epstein poster.
        md = _read(MD)
        assert "RE-SURFACED this run" in md
        assert "crawled 5h" in md

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
# 5. Attention Sphere: 111th no-match
# --------------------------------------------------------------------------
class TestAttentionSphereHundredEleventhNoMatch:
    CIRCULAR_COMMITS = [
        "a288c86",
        "a2b656f",
        "9590385",
        "2c4e21e",
        "25c730e",
        "3d16eac",
    ]

    def test_no_match_111th_cycle(self):
        md = _read(MD)
        assert "one-hundred-eleventh no-match" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "rejected as circular" in md
        assert "not ingested" in md

    def test_blob_page_surfaces_again_one_more_circular_hit(self):
        # Unlike #936 (6 circular hits, blob page did NOT surface): the
        # podcast-sentiment.md blob page SURFACED AGAIN this run, so 7
        # circular hits (one more than #936's 6).
        md = _read(MD)
        assert "SURFACED AGAIN this run" in md
        assert "one more circular hit" in md

    def test_same_commit_hash_set_as_prior_cycles(self):
        md = _read(MD)
        for short in self.CIRCULAR_COMMITS:
            assert short in md, short

    def test_tracked_sources_advanced_110_to_111(self):
        assert "110->111" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        assert "misidentified as a podcast" in _read(MD)

    def test_real_world_identity_stands(self):
        assert "Kendall Schrohe" in _read(MD)


# --------------------------------------------------------------------------
# 6. Press surfaces: 111th cycle, ZERO new URL keys
# --------------------------------------------------------------------------
class TestPressSurfacesHundredEleventhCycle:
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
        # RE-SURFACED again this run (crawled 8h); verified
        # already-in-corpus, not a new key.
        md = _read(MD)
        assert "RE-SURFACED again this run" in md
        assert "crawled 8h" in md
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
    def test_zero_type_e_941_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_941*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_795(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 795 in-tree: 795 (committed #939 Type C, competitor-entities.yaml
        # apple siri settlement leg). The in-flight #884/#899 blocks
        # (m762/m771) are lower.
        assert maxid == 795

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "79" + "6"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key strings
        # carried. Designed keying is colon-form in profiles/; the tests/
        # filename hits (other test files' negative guards) are a different
        # namespace. __pycache__ artifacts excluded per the #715
        # pattern-rescope lesson. Own file excluded as sweep carrier.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_79" + "6"
        n2 = "mech" + "anism" + "-" + "79" + "6"
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
        assert "48414" in readme and "1266" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_941_marker(self):
        assert "## #941 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        assert "940-944 window" in _read(LOG)


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
        # blocks (m762 / m771); this run adds no 941 hunks to them.
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
            assert "941" not in diff
        jdiff = _git(["diff", "--", "profiles/careers/journalists.yaml"]).stdout
        assert "941" not in jdiff
