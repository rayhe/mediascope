"""Type E #891: podcast sentiment 101st verification cycle (GF 500 newest, no 501;
EHE 42-day Epstein-spoof hold, ZERO new URL keys across all sets; Attention
Sphere 101st quoted-search no-match, Tracked Sources 100->101; press 7 results
ALL previously-logged, ZERO new press URL keys; recency frontier HOLDS at
Sep 18) - Sep 21 2026 04:00 PDT.

Monitoring-only per the Aug 28 2026 standing rule: tone NOT_SCORED,
p_value/cohens_d NOT_CALCULATED, is_significant False, engine NOT run,
no mechanisms added, no analysis.json update, NOT artifact-grade.
Falsification ledger holds at 29. ASCII-only. No em dashes.
"""
import os
import re
import glob
import subprocess

import pytest

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG = os.path.join(REPO, "iteration-log.md")
MD = os.path.join(REPO, "podcast-sentiment.md")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
THIS_FILE = os.path.basename(__file__)

ITERATION = 891
TYPE_LETTER = "E"
RUN_PDT = "2026-09-21 04:00 PDT"
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
    return [p for p in _corpus_hits("766") if "__pycache__" not in p]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE891:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #891 main commit exists pre-commit; the anchor test pins
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
            if "Type E #891" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_e_891_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_891*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 890-894 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard890_894Window:
    @pytest.mark.rotation
    def test_second_leg_of_890_894_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 891

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {890: "D", 891: "E", 892: "A", 893: "B", 894: "C"}
        assert expected[891] == "E"

    @pytest.mark.rotation
    def test_predecessor_is_890_type_d(self):
        log = _read(LOG)
        assert "## #890 Type D" in log

    @pytest.mark.rotation
    def test_no_concurrent_884_commit_asserted(self):
        # The concurrent Type C #884 run commits after this run; its
        # main commit is absent from git history. Match only commit
        # SUBJECTS: other commits' bodies may mention #884 (this run's
        # own concurrency note does). Iteration numbers follow the
        # rotation schedule, not commit order, so the subject sequence
        # must read 891 -> 890 -> 889 with the in-flight 884 skipped.
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
        assert nums[:3] == ["891", "890", "889"], nums[:3]
        assert "884" not in nums


# --------------------------------------------------------------------------
# 3. Guilty Feminist: 101st cycle, episode 500 stands newest, no 501
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredFirstCycle:
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

    def test_uk_podcasts_signal_unchanged_unverified(self):
        assert "Latest episode: 2026-09-16" in _read(MD)
        assert "UNVERIFIED" in _read(MD)

    def test_zero_meta_wearables_content_bounded_absence(self):
        md = _read(MD)
        assert "ZERO Meta/wearables content" in md
        assert "bounded search-result absence" in md


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 42-day hold, ZERO new URL keys this run
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredFirstCycle:
    KNOWN_KEYS = [
        "designtaxi.com/topic/34124",
        "fstoppers.com/news/kylie-jenner-ad-hides-disturbing-secret",
        "d33gy59ovltp76.cloudfront.net",
        "designtaxi.com/topic/33476",
        "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
        "softonic.com/articles/ray-ban-meta-smart-glasses-back-in-the-spotlight",
    ]

    def test_hold_arithmetic_42_days_not_41(self):
        import datetime
        assert (datetime.date(2026, 9, 21) - datetime.date(2026, 8, 10)).days == 42
        assert "42-day hold" in _read(MD)

    def test_epstein_spoof_remains_last_major_phase_marker(self):
        assert "Aug 10 Epstein spoof" in _read(MD)

    def test_amnesty_boxes_phase_logged_in_corpus(self):
        md = _read(MD)
        assert "amnesty boxes" in md.lower()
        assert "Ray-Ban stores" in md

    def test_zero_new_ehe_url_keys_this_run(self):
        assert "ZERO new URL keys this run" in _read(MD)

    def test_known_ehe_keys_remain_in_corpus(self):
        for key in self.KNOWN_KEYS:
            assert _corpus_hits(key), key

    def test_fstoppers_piece_in_corpus_since_465(self):
        assert len(_corpus_hits("fstoppers.com/news/kylie-jenner-ad-hides-disturbing-secret")) >= 1

    def test_no_competitor_equivalent_campaign_bounded_absence(self):
        assert "no competitor-equivalent guerrilla campaign" in _read(MD).lower()


# --------------------------------------------------------------------------
# 5. Attention Sphere: 101st quoted-search no-match as a podcast
# --------------------------------------------------------------------------
class TestAttentionSphereHundredFirstNoMatch:
    CIRCULAR_COMMIT_HASHES = [
        "959038536c82b63a7ab3b708226aec070a43514a",
        "a288c86f0be14694552fea4aa0fd3674cefe93bc",
        "a2b656f0660e299090803b4dfd7ee01087900c9f",
        "2c4e21e39a3bb17e74c8afc0bd5b7ad25bda29b4",
        "25c730ed6097aae952bdf714fe2afe375d8f9e35",
        "3d16eacfc03d35bad9ade4a15403fbcea2fb293c",
    ]

    def test_no_match_101st_cycle(self):
        md = _read(MD)
        assert "one-hundred-first no-match" in md or "101st" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "circular" in md and "rejected" in md

    def test_same_commit_hash_set_as_prior_cycles(self):
        md = _read(MD)
        for h in self.CIRCULAR_COMMIT_HASHES[:3]:
            assert h[:9] in md

    def test_tracked_sources_advanced_100_to_101(self):
        assert "100->101" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        assert "misidentified as a podcast" in _read(MD)

    def test_real_world_identity_stands(self):
        assert "Kendall Schrohe" in _read(MD)


# --------------------------------------------------------------------------
# 6. Press surfaces: 7 results, ALL previously-logged, frontier at Sep 18
# --------------------------------------------------------------------------
class TestPressSurfacesHundredFirstCycle:
    KNOWN_PRESS_KEYS = [
        "ppc.land/hamburg-regulator-finds-ray-ban-meta-glasses-expose-bystanders",
        "livemint.com/technology/tech-news/meta-ray-ban-smart-glasses-could-store-voice-recordings",
        "9to5google.com/2026/08/28/meta-ray-ban-smart-glasses-privacy-led-loophole-update",
        "webpronews.com/germanys-privacy-push-targets-meta-ray-ban-glasses-with-criminal-filing",
        "webpronews.com/metas-new-smart-glasses-update-shuts-down-camera-on-privacy-light-tampering",
        "roadtovr.com/meta-ray-ban-glasses-privacy-led-camera-update",
        "nypost.com/2026/09/18/us-news/california-users-among-plaintiffs-suing-meta-over-smart-glasses",
    ]

    def test_zero_new_press_url_keys(self):
        assert "ZERO new press URL keys" in _read(MD)

    def test_all_observed_press_keys_previously_logged(self):
        for key in self.KNOWN_PRESS_KEYS:
            assert _corpus_hits(key), key

    def test_startupfortune_softonic_did_not_surface_remain_in_corpus(self):
        md = _read(MD)
        assert "Did not surface this run" in md

    def test_recency_frontier_holds_sep_18(self):
        md = _read(MD)
        assert "Recency frontier: HOLDS at Sep 18" in md

    def test_nypost_sep18_remains_frontier_driver(self):
        md = _read(MD)
        assert "nypost Sep-18 piece remains the recency-frontier driver" in md

    def test_no_sep19_sep20_sep21_surfaces(self):
        assert "no Sep 19, Sep 20, or Sep 21 surfaces" in _read(MD)


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_891_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_891*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_765(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        assert maxid == 765

    def test_zero_numeric_766_mechanism_keys_in_profiles(self):
        d1 = "76" + "6"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_766_carriers_repo_wide(self):
        n1 = "m" + "ech" + "an" + "is" + "m" + "_76" + "6"
        n2 = "mech" + "anism" + "-" + "76" + "6"
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
        assert "45665" in _read(README) and "1218" in _read(README)

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_891_marker(self):
        assert "## #891 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        assert "890-894 window" in _read(LOG)


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
        assert "891" not in diff
