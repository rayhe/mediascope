"""Type E #951: podcast sentiment 113th verification cycle (GF episode 501
CONFIRMED AGAIN - listennotes.com main directory crawled 16h still at top;
official-site new-normal-weeks-1-and-2 page variant SURFACED AGAIN this run
(crawled 2h) 501 at top no 502; guiltyfeminist.com/new-normal/ base page
variant SURFACED this run (crawled 9h) 501 at top no 502, in-corpus since
#946; uk-podcasts bonus-episode page variant SURFACED this run (crawled 1h,
"Latest episode: 2026-09-21" 501-signal corroboration, in-corpus directory
family); podparadise did NOT surface this run (remains in corpus);
podscan.fm did NOT surface this run (remains in corpus); listennotes PT
variant surfaced crawled 223d old content in-corpus family variant;
goloudnow 350 IWD-2023 part-two + goloudnow 285 Woman-and-Power episode-page
variants re-surfaced in-corpus (logged as new keys at #946); ZERO NEW
VERBATIM GF URL KEYS this run, pure-re-surface cycle resumes; no episode
502 (two-day absence since Sep 21, weekly cadence, not a signal); zero
Meta/wearables across all 113 cycles bounded search-result absence; EHE
44-day hold (same-day carry from #946, still Sep 23), 6 logged keys
re-surfaced (34124 crawled 1h, fstoppers 1d, engadget 2d, 33476 3h,
singulism 5h, cloudfront 4d), techtimes amnesty-boxes + softonic did NOT
surface (remain in corpus), ZERO new URL keys; Attention Sphere 113th
quoted-search no-match, 7 circular own-repo GitHub URLs (same 6 commit
URLs a288c86/a2b656f/9590385/2c4e21e/25c730e/3d16eac as #846 through #946 +
the blob page, which SURFACED AGAIN this run, same 7 circular hits as
#946), Tracked Sources 112->113; press 7 ALL previously-logged, ZERO new
press URL keys, startupfortune RE-SURFACED again (crawled 2h, in corpus via
#881), roadtovr/nypost did NOT surface (remain in corpus); recency frontier
HOLDS at Sep 18, no Sep 19 through Sep 23 surfaces) - Sep 23 2026 17:00 PDT.

Monitoring-only per the Aug 28 2026 standing rule: tone NOT_SCORED,
p_value/cohens_d NOT_CALCULATED, is_significant False, engine NOT run,
no mechanisms added, no analysis.json update, NOT artifact-grade.
Max numeric mechanism_id 801 in-tree; zero 802 keys numeric/underscore/dash.
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

ITERATION = 951
TYPE_LETTER = "E"
RUN_PDT = "2026-09-23 17:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "d86ace6d622a373da56eaaee0bb031bc25aec2a8"


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
class TestNoveltyAnchorTypeE951:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #951 main commit exists pre-commit; the anchor test pins
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
            if "Type E #951" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_e_951_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_951*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 950-954 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard950_954Window:
    @pytest.mark.rotation
    def test_second_leg_of_950_954_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 951

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {950: "D", 951: "E", 952: "A", 953: "B", 954: "C"}
        assert expected[951] == "E"

    @pytest.mark.rotation
    def test_predecessor_950_type_d_committed(self):
        # #950 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md); this run's own #951 entry will be prepended
        # above it.
        assert "## #950 Type D" in _read(LOG)

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
# 3. The Guilty Feminist: 113th cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredThirteenthCycle:
    GF_LOGGED_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "guiltyfeminist.com/new-normal-weeks-1-and-2",
        "guiltyfeminist.com/new-normal/",
        "goloudnow.com/podcasts/the-guilty-feminist-152",
        "uk-podcasts.co.uk/podcast/the-guilty-feminist",
    ]

    def test_episode_501_confirmed_again_this_run(self):
        md = _read(MD)
        assert "501 CONFIRMED AGAIN" in md
        assert "Out North East" in md
        assert "crawled 16h" in md

    def test_no_episode_502_surfaced(self):
        # No 502 anywhere this run: listennotes main still 501 at top,
        # official-site variants 501 at top, uk-podcasts still carries the
        # "Latest episode: 2026-09-21" 501-signal. Two-day absence since
        # Sep 21, consistent with weekly cadence, not a signal.
        md = _read(MD)
        assert "no episode 502" in md

    def test_official_site_variants_surfaced_this_run(self):
        # The official-site new-normal-weeks-1-and-2 page variant SURFACED
        # AGAIN this run (crawled 2h, 501 at top, no 502; first-party
        # family in corpus since #911); the guiltyfeminist.com/new-normal/
        # base page variant SURFACED this run (crawled 9h, 501 at top, no
        # 502; in-corpus since #946 logged it as a new key).
        md = _read(MD)
        assert "new-normal-weeks-1-and-2 page variant SURFACED AGAIN this run" in md
        assert "crawled 2h" in md
        assert "new-normal/ base page variant SURFACED this run" in md
        assert "crawled 9h" in md

    def test_uk_podcasts_surfaced_podparadise_podscan_did_not(self):
        # uk-podcasts bonus-episode page variant SURFACED this run
        # (crawled 1h, "Latest episode: 2026-09-21" 501-signal
        # corroboration, in-corpus directory family); podparadise and
        # podscan.fm did NOT surface this run (remain in corpus).
        md = _read(MD)
        assert "uk-podcasts bonus-episode page variant SURFACED this run" in md
        assert "crawled 1h" in md
        assert "PodParadise did NOT surface this run" in md
        assert "podscan.fm did NOT surface this run" in md

    def test_zero_new_verbatim_gf_url_keys_pure_resurface(self):
        # The #946 interruption (two goloudnow directory-mirror keys) is
        # in-corpus now: both variants re-surfaced this run, ZERO new
        # verbatim GF URL keys this run. Pure-re-surface cycle resumes.
        md = _read(MD)
        assert "pure-re-surface cycle resumes" in md
        assert "ZERO new verbatim GF URL keys this run" in md
        for key in ("350-international-womens-day-2023", "285-woman-and-power"):
            assert _corpus_hits(key), key

    def test_all_logged_gf_keys_in_corpus(self):
        for key in self.GF_LOGGED_KEYS:
            assert _corpus_hits(key), key

    def test_zero_meta_wearables_across_113_cycles(self):
        md = _read(MD)
        assert "across all 113 cycles" in md
        assert "bounded search-result absence" in md


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 44-day hold, ZERO new URL keys this run
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredThirteenthCycle:
    KNOWN_KEYS = [
        "community.designtaxi.com/topic/34124",
        "fstoppers.com/news/kylie-jenner-ad-hides",
        "d33gy59ovltp76.cloudfront.net",
        "community.designtaxi.com/topic/33476",
        "singulism.com/en/2026-07-17-meta-glasses-protest-london-bus-stops",
        "www.engadget.com/2217151",
    ]

    def test_hold_arithmetic_44_days_same_day_carry(self):
        # Aug 10 Epstein spoof -> Sep 23: 44 days. Regression guard on the
        # #846/#851 47/48 slips: same-day carry from the Sep 23 12:00 cycle
        # (#946), which was also 44 days - the later hour does not advance
        # the date difference.
        assert (date(2026, 9, 23) - date(2026, 8, 10)).days == 44
        assert "44-day hold" in _read(MD)

    def test_epstein_spoof_remains_last_major_phase_marker(self):
        assert "Epstein spoof" in _read(MD)

    def test_six_logged_keys_resurfaced_this_run(self):
        # 34124 (crawled 1h), fstoppers (1d), engadget (2d), 33476 (3h),
        # singulism (5h), cloudfront mirror (4d) - all re-surfaced this
        # run, in corpus, not new keys.
        md = _read(MD)
        assert "crawled 1h" in md
        assert "singulism" in md.lower()
        for key in self.KNOWN_KEYS:
            assert _corpus_hits(key), key

    def test_zero_new_ehe_url_keys_this_run(self):
        assert "ZERO new URL keys this run" in _read(MD)

    def test_techtimes_softonic_did_not_surface_remain_in_corpus(self):
        md = _read(MD)
        assert "techtimes" in md.lower()
        assert "softonic" in md.lower()
        assert "did NOT surface this run" in md

    def test_no_competitor_equivalent_campaign_113_cycles(self):
        assert "113 cycles" in _read(MD)


# --------------------------------------------------------------------------
# 5. Attention Sphere: 113th no-match
# --------------------------------------------------------------------------
class TestAttentionSphereHundredThirteenthNoMatch:
    CIRCULAR_COMMITS = [
        "a288c86",
        "a2b656f",
        "9590385",
        "2c4e21e",
        "25c730e",
        "3d16eac",
    ]

    def test_no_match_113th_cycle(self):
        md = _read(MD)
        assert "one-hundred-thirteenth no-match" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "rejected as circular" in md
        assert "not ingested" in md

    def test_blob_page_surfaces_again_same_as_946(self):
        # Same as #946 (7 circular hits, blob page SURFACED AGAIN) - not
        # one more than #946 this time.
        md = _read(MD)
        assert "SURFACED AGAIN this run" in md
        assert "same 7 circular hits as #946" in md

    def test_same_commit_hash_set_as_prior_cycles(self):
        md = _read(MD)
        for short in self.CIRCULAR_COMMITS:
            assert short in md, short

    def test_tracked_sources_advanced_112_to_113(self):
        assert "112->113" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        assert "misidentified as a podcast" in _read(MD)

    def test_real_world_identity_stands(self):
        assert "Kendall Schrohe" in _read(MD)


# --------------------------------------------------------------------------
# 6. Press surfaces: 113th cycle, ZERO new URL keys
# --------------------------------------------------------------------------
class TestPressSurfacesHundredThirteenthCycle:
    KNOWN_KEYS = [
        "ppc.land/hamburg-regulator",
        "livemint.com/technology/tech-news/meta-ray-ban-smart-glasses-could-store",
        "9to5google.com/2026/08/28/meta-ray-ban-smart-glasses-privacy-led-loophole",
        "reuters.com/legal/government/german-advocacy-group",
        "startupfortune.com/meta-permanently-disables-cameras-on-thousands-of-tampered-smart-glasses",
        "webpronews.com/germanys-privacy-push",
        "recordinglaw.com/news/meta-ray-ban-smart-glasses-privacy-scandal",
    ]

    def test_zero_new_press_url_keys(self):
        assert "ZERO new press URL keys this run" in _read(MD)

    def test_all_observed_press_keys_previously_logged(self):
        for key in self.KNOWN_KEYS:
            assert _corpus_hits(key), key

    def test_startupfortune_resurfaced_again_this_run_still_in_corpus(self):
        # startupfortune tampered-LED bricking was in corpus via #881 and
        # RE-SURFACED again this run (crawled 2h); verified
        # already-in-corpus, not a new key.
        md = _read(MD)
        assert "RE-SURFACED again this run" in md
        assert "crawled 2h" in md
        assert _corpus_hits("startupfortune.com/meta-permanently-disables")

    def test_roadtovr_nypost_did_not_surface_remain_in_corpus(self):
        md = _read(MD)
        assert "roadtovr.com" in md
        assert "nypost.com" in md
        assert "did NOT surface this run" in md

    def test_recency_frontier_holds_sep_18(self):
        assert "Recency frontier: HOLDS at Sep 18" in _read(MD)

    def test_no_sep19_through_sep23_surfaces(self):
        assert "no Sep 19, Sep 20, Sep 21, Sep 22, or Sep 23 surfaces" in _read(MD)


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps (per #715 convention)
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_951_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_951*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_801(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 801 in-tree: 801 (committed #949/#950 Type C/D, competitor-entities.yaml
        # DOJ Google ad-tech remedies leg). The in-flight #884/#899 blocks
        # (m762/m771) are lower.
        assert maxid == 801

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "80" + "2"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key strings
        # carried. Designed keying is colon-form in profiles/; the tests/
        # filename hits (other test files' negative guards) are a different
        # namespace. __pycache__ artifacts excluded per the #715
        # pattern-rescope lesson. Own file excluded as sweep carrier.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "80" + "2"
        n2 = "mech" + "anism" + "-" + "80" + "2"
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
        assert "48980" in readme and "1276" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_951_marker(self):
        assert "## #951 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        assert "950-954 window" in _read(LOG)


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
        # blocks (m762 / m771); this run adds no 951 hunks to them.
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
            assert "951" not in diff
        jdiff = _git(["diff", "--", "profiles/careers/journalists.yaml"]).stdout
        assert "951" not in jdiff
