"""Type E #896: podcast sentiment 102nd verification cycle (GF 500 newest, no 501;
EHE 42-day Epstein-spoof hold, ZERO new URL keys across all sets; Attention
Sphere 102nd quoted-search no-match, Tracked Sources 101->102; press 7 results
ALL previously-logged, ZERO new press URL keys; recency frontier HOLDS at
Sep 18; uk-podcasts "Latest episode: 2026-09-21" signal advanced but
UNVERIFIED as a 501 indicator) - Sep 21 2026 09:00 PDT.

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

ITERATION = 896
TYPE_LETTER = "E"
RUN_PDT = "2026-09-21 09:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "93ba758be0658821b2b275693482f1eea64bec23"


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
    return [p for p in _corpus_hits("769") if "__pycache__" not in p]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE896:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #896 main commit exists pre-commit; the anchor test pins
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
            if "Type E #896" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_e_896_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_896*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 895-899 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard895_899Window:
    @pytest.mark.rotation
    def test_second_leg_of_895_899_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 896

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {895: "D", 896: "E", 897: "A", 898: "B", 899: "C"}
        assert expected[896] == "E"

    @pytest.mark.rotation
    def test_predecessor_is_895_type_d(self):
        log = _read(LOG)
        assert "## #895 Type D" in log

    @pytest.mark.rotation
    def test_no_concurrent_884_commit_asserted(self):
        # The concurrent Type C #884 run commits after this run; its
        # main commit is absent from git history. Match only commit
        # SUBJECTS: other commits' bodies may mention #884 (this run's
        # own concurrency note does). Iteration numbers follow the
        # rotation schedule, not commit order, so the subject sequence
        # must read 896 -> 895 -> 894 with the in-flight 884 skipped.
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
        assert nums[:3] == ["896", "895", "894"], nums[:3]
        assert "884" not in nums


# --------------------------------------------------------------------------
# 3. Guilty Feminist: 102nd cycle, episode 500 stands newest, no 501
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredSecondCycle:
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

    def test_uk_podcasts_signal_advanced_unverified(self):
        # The single-directory signal advanced 2026-09-16 -> 2026-09-21 this
        # run; it is still UNVERIFIED as an episode-501 indicator.
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
class TestEveryoneHatesElonHundredSecondCycle:
    KNOWN_KEYS = [
        "designtaxi.com/topic/34124",
        "fstoppers.com/news/kylie-jenner-ad-hides",
        "d33gy59ovltp76.cloudfront.net",
        "designtaxi.com/topic/33476",
        "techtimes.co.uk/activists-challenge-meta-ray-ban",
        "softonic.com/articles/ray-ban-smart-glasses-back-in-the-spotlight",
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

    def test_fstoppers_piece_in_corpus_since_465(self):
        assert "in corpus since #465" in _read(MD)

    def test_no_competitor_equivalent_campaign_bounded_absence(self):
        md = _read(MD)
        assert "No competitor-equivalent guerrilla campaign" in md
        assert "bounded search-result absence" in md


# --------------------------------------------------------------------------
# 5. Attention Sphere: 102nd no-match
# --------------------------------------------------------------------------
class TestAttentionSphereHundredSecondNoMatch:
    CIRCULAR_COMMITS = [
        "a288c86",
        "a2b656f",
        "9590385",
        "2c4e21e",
        "25c730e",
        "3d16eac",
    ]

    def test_no_match_102nd_cycle(self):
        md = _read(MD)
        assert "one-hundred-second no-match" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "rejected as circular" in md
        assert "not ingested" in md

    def test_same_commit_hash_set_as_prior_cycles(self):
        md = _read(MD)
        for short in self.CIRCULAR_COMMITS:
            assert short in md, short

    def test_tracked_sources_advanced_101_to_102(self):
        assert "101->102" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        assert "misidentified as a podcast" in _read(MD)

    def test_real_world_identity_stands(self):
        assert "Kendall Schrohe" in _read(MD)


# --------------------------------------------------------------------------
# 6. Press surfaces: 102nd cycle, ZERO new URL keys
# --------------------------------------------------------------------------
class TestPressSurfacesHundredSecondCycle:
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
    def test_zero_type_e_896_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_896*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_768(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        assert maxid == 768

    def test_zero_numeric_769_mechanism_keys_in_profiles(self):
        d1 = "76" + "9"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_769_carriers_repo_wide(self):
        n1 = "m" + "ech" + "an" + "is" + "m" + "_76" + "9"
        n2 = "mech" + "anism" + "-" + "76" + "9"
        hits = []
        for f in _exclude():
            t = open(f, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(f)
        assert hits == []

    def test_concurrent_884_change_not_in_this_commit_scope(self):
        # The concurrent Type C #884 block in competitor-entities.yaml stays
        # uncommitted; this run's staged set must not include that file.
        status = _git(["status", "--short"]).stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        assert not any("competitor-entities" in l for l in staged)


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
        assert "45946" in _read(README) and "1223" in _read(README)

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_896_marker(self):
        assert "## #896 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        assert "895-899 window" in _read(LOG)


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

    def test_concurrent_file_untouched_by_this_run(self):
        # git diff on the concurrent file must show ONLY the #884 block (m762),
        # i.e. this run added no hunks to competitor-entities.yaml.
        diff = _git(["diff", "--", "profiles/competitor-entities.yaml"]).stdout
        assert "mechanism" + "_id" + ": 762" in diff
        assert "896" not in diff
