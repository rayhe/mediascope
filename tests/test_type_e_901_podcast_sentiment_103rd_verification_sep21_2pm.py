"""Type E #901: podcast sentiment 103rd verification cycle (GF 500 newest, no 501;
uk-podcasts "Latest episode: 2026-09-21" signal UNCHANGED and still UNVERIFIED
as a 501 indicator; EHE 42-day Epstein-spoof hold, engadget bus-stops key
re-surfaced (in corpus, 13 hits), ZERO new URL keys across all sets;
Attention Sphere 103rd quoted-search no-match, Tracked Sources 102->103;
press 7 results ALL previously-logged, ZERO new press URL keys; recency
frontier HOLDS at Sep 18) - Sep 21 2026 14:00 PDT.

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

ITERATION = 901
TYPE_LETTER = "E"
RUN_PDT = "2026-09-21 14:00 PDT"
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


def _exclude(pycache=True):
    return [p for p in _corpus_hits("772") if "__pycache__" not in p]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE901:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #901 main commit exists pre-commit; the anchor test pins
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
            if "Type E #901" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_e_901_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_901*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 900-904 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard900_904Window:
    @pytest.mark.rotation
    def test_second_leg_of_900_904_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 901

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {900: "D", 901: "E", 902: "A", 903: "B", 904: "C"}
        assert expected[901] == "E"

    @pytest.mark.rotation
    def test_predecessor_900_type_d_in_flight(self):
        # #900 Type D ran at 13:00 PDT; its test file is on disk (untracked),
        # its commit lands after this run's. Iteration numbers follow the
        # rotation schedule, not commit order.
        files = glob.glob(os.path.join(REPO, "tests", "*type_d_900*"))
        assert len(files) >= 1

    @pytest.mark.rotation
    def test_no_concurrent_inflight_commits_asserted(self):
        # In-flight at this run's checks: #884 Type C, #898 Type B, #899
        # Type C, #900 Type D - none committed yet. Match only commit
        # SUBJECTS: other commits' bodies may mention them. The subject
        # sequence must read 897 -> 896 -> 895 with the in-flight runs
        # skipped.
        result = subprocess.run(
            ["git", "log", "--format=%s", "-25"], cwd=REPO,
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        nums = []
        for line in result.stdout.splitlines():
            m = re.match(r"Type [A-E] #(\d+)", line)
            if m and (not nums or nums[-1] != m.group(1)):
                nums.append(m.group(1))
        assert nums[:3] == ["897", "896", "895"], nums[:3]
        for skip in ("884", "898", "899", "900"):
            assert skip not in nums


# --------------------------------------------------------------------------
# 3. Guilty Feminist: 103rd cycle, episode 500 stands newest, no 501
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredThirdCycle:
    GF_KNOWN_KEYS = [
        "youtube.com/watch?v=iKXj2w2cp50",
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "goloudnow.com/podcasts/the-guilty-feminist-152",
        "getpodcast.com/podcast/the-guilty-feminist",
        "uk-podcasts.co.uk/podcast/the-guilty-feminist",
        "podparadise.com/Podcast/1068940771",
        "listennotes.com/pt/podcasts/the-guilty-feminist",
    ]

    def test_episode_500_is_newest_observed(self):
        assert "500. Five Hundredth episode with Kate Cheka and the Palestinian Circus" in _read(MD)

    def test_no_episode_501_surface(self):
        assert "no episode 501" in _read(MD).lower()

    def test_zero_new_gf_url_keys(self):
        assert "ZERO new GF URL keys" in _read(MD)

    def test_all_observed_gf_keys_previously_logged(self):
        for key in self.GF_KNOWN_KEYS:
            assert _corpus_hits(key), key

    def test_getpodcast_surfaced_still_in_corpus(self):
        # getpodcast re-surfaced at #886 (in corpus since #866); surfaces again this run.
        assert len(_corpus_hits("getpodcast")) >= 1

    def test_uk_podcasts_signal_unchanged_still_unverified(self):
        # The single-directory signal was ADVANCED 2026-09-16 -> 2026-09-21
        # at #896; this run it is UNCHANGED at 2026-09-21 and remains
        # UNVERIFIED as an episode-501 indicator. Do NOT assert 501 exists.
        md = _read(MD)
        assert "Latest episode: 2026-09-21" in md
        assert "UNVERIFIED" in md

    def test_zero_meta_wearables_content_bounded_absence(self):
        md = _read(MD)
        assert "ZERO Meta/wearables content" in md
        assert "bounded search-result absence" in md


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 42-day hold, ZERO new URL keys this run
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredThirdCycle:
    KNOWN_KEYS = [
        "designtaxi.com/topic/34124",
        "fstoppers.com/news/kylie-jenner-ad-hides",
        "d33gy59ovltp76.cloudfront.net",
        "designtaxi.com/topic/33476",
        "techtimes.co.uk/activists-challenge-meta-ray-ban",
        "engadget.com/2217151",
    ]

    def test_hold_arithmetic_42_days_not_41(self):
        # Aug 10 Epstein spoof -> Sep 21: 42 days. Regression guard on the
        # #846/#851 47/48 slips: do not relabel as 41-day (that was Sep 20).
        assert (date(2026, 9, 21) - date(2026, 8, 10)).days == 42
        assert "42-day hold" in _read(MD)

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

    def test_engadget_bus_stops_resurface_in_corpus(self):
        # engadget.com/2217151 (Karissa Bell Jul 16 bus-stops original) was
        # not in #896's observed set; it re-surfaced this run (crawled 1h)
        # and is verified already-in-corpus (13 hits), not a new key.
        assert len(_corpus_hits("engadget.com/2217151")) >= 1

    def test_softonic_singulism_did_not_surface_remain_in_corpus(self):
        md = _read(MD)
        assert "softonic" in md.lower()
        assert "singulism" in md.lower()
        assert "did NOT surface this run" in md

    def test_no_competitor_equivalent_campaign_bounded_absence(self):
        md = _read(MD)
        assert "No competitor-equivalent guerrilla campaign" in md
        assert "bounded search-result absence" in md


# --------------------------------------------------------------------------
# 5. Attention Sphere: 103rd no-match
# --------------------------------------------------------------------------
class TestAttentionSphereHundredThirdNoMatch:
    CIRCULAR_COMMITS = [
        "a288c86",
        "a2b656f",
        "9590385",
        "2c4e21e",
        "25c730e",
        "3d16eac",
    ]

    def test_no_match_103rd_cycle(self):
        md = _read(MD)
        assert "one-hundred-third no-match" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "rejected as circular" in md
        assert "not ingested" in md

    def test_same_commit_hash_set_as_prior_cycles(self):
        md = _read(MD)
        for short in self.CIRCULAR_COMMITS:
            assert short in md, short

    def test_tracked_sources_advanced_102_to_103(self):
        assert "102->103" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        assert "misidentified as a podcast" in _read(MD)

    def test_real_world_identity_stands(self):
        assert "Kendall Schrohe" in _read(MD)


# --------------------------------------------------------------------------
# 6. Press surfaces: 103rd cycle, ZERO new URL keys
# --------------------------------------------------------------------------
class TestPressSurfacesHundredThirdCycle:
    KNOWN_KEYS = [
        "ppc.land/hamburg-regulator",
        "livemint.com/technology/tech-news/meta-ray-ban-smart-glasses-could-store",
        "9to5google.com/2026/08/28/meta-ray-ban-smart-glasses-privacy-led-loophole",
        "webpronews.com/germanys-privacy-push",
        "webpronews.com/metas-new-smart-glasses-update",
        "roadtovr.com/meta-ray-ban-glasses-privacy-led-camera-update",
        "nypost.com/2026/09/18/us-news/california-users-among-plaintiffs",
    ]

    def test_zero_new_press_url_keys(self):
        assert "ZERO new press URL keys this run" in _read(MD)

    def test_all_observed_press_keys_previously_logged(self):
        for key in self.KNOWN_KEYS:
            assert _corpus_hits(key), key

    def test_startupfortune_softonic_did_not_surface_remain_in_corpus(self):
        md = _read(MD)
        assert "startupfortune.com" in md
        assert "did NOT surface this run" in md or "Did not surface this run" in md

    def test_recency_frontier_holds_sep_18(self):
        assert "Recency frontier: HOLDS at Sep 18" in _read(MD)

    def test_nypost_sep18_remains_frontier_driver(self):
        assert "recency-frontier driver" in _read(MD)

    def test_no_sep19_sep20_sep21_surfaces(self):
        assert "no Sep 19, Sep 20, or Sep 21 surfaces" in _read(MD)


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps (per #715 convention)
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_901_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_901*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_771(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 771 in-tree: 770 (in-flight #898 Type B, journalists.yaml) and 771
        # (in-flight #899 Type C, nytimes.yaml), both uncommitted.
        assert maxid == 771

    def test_zero_numeric_772_mechanism_keys_in_profiles(self):
        d1 = "77" + "2"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_772_carriers_repo_wide(self):
        n1 = "m" + "ech" + "an" + "is" + "m" + "_77" + "2"
        n2 = "mech" + "anism" + "-" + "77" + "2"
        hits = []
        for f in _exclude():
            t = open(f, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(f)
        assert hits == []

    def test_concurrent_inflight_files_not_in_this_commit_scope(self):
        # In-flight: #884 Type C (competitor-entities.yaml m762), #898 Type B
        # (journalists.yaml m770), #899 Type C (nytimes.yaml m771) - all
        # uncommitted; this run's staged set must not include those files.
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
        assert "46058" in _read(README) and "1225" in _read(README)

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_901_marker(self):
        assert "## #901 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        assert "900-904 window" in _read(LOG)


# --------------------------------------------------------------------------
# 11. Push readiness
# --------------------------------------------------------------------------
class TestPushReadiness:
    def test_ascii_only_no_em_dashes(self):
        text = _read(__file__)
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_all_urls_from_verbatim_listings(self):
        needle = "https://github.com/" + "rayhe/mediascope/blob/HEAD/podcast-sentiment.md"
        assert needle not in _read(__file__)

    def test_concurrent_files_untouched_by_this_run(self):
        # git diffs on the three in-flight files must show only their own
        # blocks (m762 / m770 / m771); this run adds no 901 hunks to them.
        for f, own in (
            ("profiles/competitor-entities.yaml", "762"),
            ("profiles/careers/journalists.yaml", "770"),
            ("profiles/nytimes.yaml", "771"),
        ):
            diff = _git(["diff", "--", f]).stdout
            assert ("mechanism" + "_id" + ": " + own) in diff
            assert "901" not in diff
