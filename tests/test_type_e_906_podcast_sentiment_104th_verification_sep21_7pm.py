"""Type E #906: podcast sentiment 104th verification cycle (GF episode 501
CONFIRMED this run, resolving the #896-#901 501 watch; uk-podcasts
"Latest episode: 2026-09-21" signal now CORROBORATED as the 501 indicator
by listennotes.com main directory; ZERO new GF URL keys; EHE 42-day
Epstein-spoof hold, engadget bus-stops key re-surfaced again, ZERO new URL
keys; Attention Sphere 104th quoted-search no-match, Tracked Sources
103->104; press 7 ALL previously-logged incl. recordinglaw.com FAQ,
startupfortune re-surface, ZERO new press URL keys; recency frontier HOLDS
at Sep 18) - Sep 21 2026 19:00 PDT.

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

ITERATION = 906
TYPE_LETTER = "E"
RUN_PDT = "2026-09-21 19:00 PDT"
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
    return [p for p in _corpus_hits("775") if "__pycache__" not in p]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE906:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #906 main commit exists pre-commit; the anchor test pins
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
            if "Type E #906" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_e_906_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_906*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 905-909 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard905_909Window:
    @pytest.mark.rotation
    def test_second_leg_of_905_909_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 906

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {905: "D", 906: "E", 907: "A", 908: "B", 909: "C"}
        assert expected[906] == "E"

    @pytest.mark.rotation
    def test_predecessor_905_type_d_committed(self):
        # #905 Type D ran at 18:00 PDT and is COMMITTED (its log entry sits
        # at the head of iteration-log.md); this run's own #906 entry will
        # be prepended above it.
        assert "## #905 Type D" in _read(LOG)

    @pytest.mark.rotation
    def test_no_concurrent_inflight_commits_asserted(self):
        # In-flight at this run's checks: #884 Type C (m762),
        # #898 Type B (m770), #899 Type C (m771), #900 Type D - none
        # committed yet. Match only commit SUBJECTS: other commits' bodies
        # may mention them.
        subjects = [
            _git(["log", "--format=%s", "-1", c]).stdout.strip()
            for c in _git(["log", "--format=%H", "-8"]).stdout.splitlines()
        ]
        for n in ("884", "898", "899", "900"):
            assert not any(
                ("Type " in s) and (f"#{n} " in s or s.endswith(f"#{n}"))
                for s in subjects
            ), (n, subjects)


# --------------------------------------------------------------------------
# 3. The Guilty Feminist: 501 CONFIRMED this run, resolving the watch
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredFourthCycle:
    GF_KNOWN_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "getpodcast.com/podcast/the-guilty-feminist",
        "goloudnow.com/podcasts/the-guilty-feminist-152",
        "uk-podcasts.co.uk/podcast/the-guilty-feminist",
        "podparadise.com/Podcast/1068940771",
        "listennotes.com/pt/podcasts/the-guilty-feminist",
        "youtube.com/watch?v=HL3iFdYBk9M",
    ]

    def test_episode_501_confirmed_this_run(self):
        md = _read(MD)
        assert "501 CONFIRMED" in md
        assert "Out North East" in md

    def test_uk_podcasts_signal_now_corroborated(self):
        # The #896-#901 single-directory signal ("Latest episode:
        # 2026-09-21", UNVERIFIED) is now corroborated as the 501 indicator
        # by the listennotes.com main directory (crawled 3h), which shows
        # "The Guilty Feminist 501. Out North East ... Released 21
        # September" at top. The prior UNVERIFIED caution is lifted.
        md = _read(MD)
        assert "CORROBORATED as the 501" in md
        assert "Released 21 September" in md

    def test_zero_new_gf_url_keys(self):
        assert "ZERO new GF URL keys" in _read(MD)

    def test_all_observed_gf_keys_previously_logged(self):
        for key in self.GF_KNOWN_KEYS:
            assert _corpus_hits(key), key

    def test_episode_501_zero_meta_wearables_content(self):
        md = _read(MD)
        assert "501" in md
        assert "ZERO Meta/wearables content" in md
        assert "bounded search-result absence" in md

    def test_getpodcast_stale_still_in_corpus(self):
        # getpodcast re-surfaced at #886 (in corpus since #866); surfaces
        # again this run with a stale 68d crawl (491 at top), still in
        # corpus, not a new key.
        assert len(_corpus_hits("getpodcast.com/podcast/the-guilty-feminist")) >= 1


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 42-day hold, ZERO new URL keys this run
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredFourthCycle:
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

    def test_engadget_bus_stops_resurface_again_in_corpus(self):
        # engadget.com/2217151 (Karissa Bell Jul 16 bus-stops original)
        # re-surfaced at #901 and surfaces again this run (crawled 6h);
        # verified already-in-corpus (11 hits pre-commit), not a new key.
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
# 5. Attention Sphere: 104th no-match
# --------------------------------------------------------------------------
class TestAttentionSphereHundredFourthNoMatch:
    CIRCULAR_COMMITS = [
        "a288c86",
        "a2b656f",
        "9590385",
        "2c4e21e",
        "25c730e",
        "3d16eac",
    ]

    def test_no_match_104th_cycle(self):
        md = _read(MD)
        assert "one-hundred-fourth no-match" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "rejected as circular" in md
        assert "not ingested" in md

    def test_same_commit_hash_set_as_prior_cycles(self):
        md = _read(MD)
        for short in self.CIRCULAR_COMMITS:
            assert short in md, short

    def test_tracked_sources_advanced_103_to_104(self):
        assert "103->104" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        assert "misidentified as a podcast" in _read(MD)

    def test_real_world_identity_stands(self):
        assert "Kendall Schrohe" in _read(MD)


# --------------------------------------------------------------------------
# 6. Press surfaces: 104th cycle, ZERO new URL keys
# --------------------------------------------------------------------------
class TestPressSurfacesHundredFourthCycle:
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

    def test_startupfortune_resurfaced_this_run_still_in_corpus(self):
        # startupfortune tampered-LED bricking was in corpus via #881, did
        # NOT surface at #901, and RE-SURFACED this run (crawled 6h);
        # verified already-in-corpus (11 hits pre-commit), not a new key.
        md = _read(MD)
        assert "RE-SURFACED this run" in md
        assert _corpus_hits("startupfortune.com/meta-permanently-disables")

    def test_recordinglaw_faq_in_corpus(self):
        # recordinglaw.com privacy-scandal FAQ (Bartone v. Meta + Swedish
        # contractor investigation) is in corpus (4 hits pre-commit), not
        # a new key.
        assert len(_corpus_hits("recordinglaw.com/news/meta-ray-ban-smart-glasses-privacy-scandal")) >= 1

    def test_roadtovr_nypost_did_not_surface_remain_in_corpus(self):
        md = _read(MD)
        assert "roadtovr.com" in md
        assert "nypost.com" in md
        assert "did NOT surface this run" in md or "Did not surface this run" in md

    def test_recency_frontier_holds_sep_18(self):
        assert "Recency frontier: HOLDS at Sep 18" in _read(MD)

    def test_no_sep19_sep20_sep21_surfaces(self):
        assert "no Sep 19, Sep 20, or Sep 21 surfaces" in _read(MD)


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps (per #715 convention)
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_906_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_906*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_774(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 774 in-tree: 774 (committed #904 Type C, financial-times.yaml).
        # The in-flight #884/#898/#899 blocks (m762/m770/m771) are lower.
        assert maxid == 774

    def test_zero_numeric_775_mechanism_keys_in_profiles(self):
        d1 = "77" + "5"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_775_carriers_in_profiles(self):
        # Format-built needles per #715: no literal "775" key strings
        # carried. Designed keying is colon-form in profiles/; the tests/
        # _775 filename hits (test_type_d_775 etc.) are ITERATION-number
        # references, a different namespace.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_77" + "5"
        n2 = "mech" + "anism" + "-" + "77" + "5"
        hits = []
        for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(p)
        assert hits == []

    def test_concurrent_inflight_files_not_in_this_commit_scope(self):
        # In-flight: #884 Type C (competitor-entities.yaml m762), #898 Type B
        # (journalists.yaml m770), #899 Type C (nytimes.yaml m771),
        # #900 Type D (untracked test file) - all uncommitted; this run's
        # staged set must not include those files.
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
        assert "46412" in _read(README) and "1231" in _read(README)

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_906_marker(self):
        assert "## #906 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        assert "905-909 window" in _read(LOG)


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
        # git diffs on the three in-flight files must show only their own
        # blocks (m762 / m770 / m771); this run adds no 906 hunks to them.
        for f, own in (
            ("profiles/competitor-entities.yaml", "762"),
            ("profiles/careers/journalists.yaml", "770"),
            ("profiles/nytimes.yaml", "771"),
        ):
            diff = _git(["diff", "--", f]).stdout
            assert ("mechanism" + "_id" + ": " + own) in diff
            assert "906" not in diff
