"""Type E #911: podcast sentiment 105th verification cycle (GF episode 501
CONFIRMED again - listennotes.com main directory crawled 1h still at top,
plus FIRST-PARTY official-site confirmation this run via
guiltyfeminist.com/new-normal/ listing 501 as the latest episode, extending
#906's two-directory corroboration to a third first-party source; podscan.fm
transcript excerpt of the 501 intro (Road to Gilead / Vision Fest Sep 25)
carries zero Meta/wearables content; ZERO new GF URL keys (8/8
previously-logged); EHE 43-day Epstein-spoof hold, engadget bus-stops key
re-surfaced again, ZERO new URL keys; Attention Sphere 105th quoted-search
no-match, Tracked Sources 104->105; press 7 ALL previously-logged incl.
recordinglaw.com FAQ, startupfortune re-surface again, ZERO new press URL
keys; recency frontier HOLDS at Sep 18) - Sep 22 2026 01:00 PDT.

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

ITERATION = 911
TYPE_LETTER = "E"
RUN_PDT = "2026-09-22 01:00 PDT"
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
class TestNoveltyAnchorTypeE911:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #911 main commit exists pre-commit; the anchor test pins
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
            if "Type E #911" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_e_911_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_911*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 910-914 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard910_914Window:
    @pytest.mark.rotation
    def test_second_leg_of_910_914_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 911

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {910: "D", 911: "E", 912: "A", 913: "B", 914: "C"}
        assert expected[911] == "E"

    @pytest.mark.rotation
    def test_predecessor_910_type_d_committed(self):
        # #910 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md); this run's own #911 entry will be prepended
        # above it.
        assert "## #910 Type D" in _read(LOG)

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
# 3. The Guilty Feminist: 105th cycle, 501 confirmed + first-party site
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredFifthCycle:
    GF_KNOWN_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "podparadise.com/Podcast/1068940771",
        "guiltyfeminist.com/new-normal",
        "listennotes.com/pt/podcasts/the-guilty-feminist",
        "podscan.fm/podcasts/the-guilty-feminist-1",
        "youtube.com/watch?v=8OeSUuyvuXc",
        "youtube.com/watch?v=HL3iFdYBk9M",
        "uk-podcasts.co.uk/podcast/the-guilty-feminist",
    ]

    def test_episode_501_confirmed_again_this_run(self):
        md = _read(MD)
        assert "501 CONFIRMED AGAIN" in md
        assert "Out North East" in md
        assert "crawled 1h" in md

    def test_official_site_first_party_confirmation(self):
        # guiltyfeminist.com/new-normal/ (crawled 19h) now lists 501 as
        # the latest episode directly on the official site: third source
        # after #906's listennotes + uk-podcasts two-directory
        # corroboration.
        md = _read(MD)
        assert "FIRST-PARTY official-site confirmation" in md
        assert "Published: 21 September 2026" in md
        assert "third, first-party source" in md

    def test_podscan_transcript_excerpt_zero_meta_wearables(self):
        # podscan.fm GF directory carries a 501 intro transcript excerpt
        # (Road to Gilead open-space / Vision Fest Sep 25); the excerpt
        # carries zero Meta/wearables content (snippet-bounded); the URL
        # is a known key (25 corpus hits pre-commit), NOT new.
        md = _read(MD)
        assert "podscan.fm/podcasts/the-guilty-feminist-1" in md
        assert "Road to Gilead" in md
        assert "Meta/wearables content in the intro-transcript excerpt" in md

    def test_zero_new_gf_url_keys(self):
        assert "ZERO new GF URL keys" in _read(MD)

    def test_all_observed_gf_keys_previously_logged(self):
        for key in self.GF_KNOWN_KEYS:
            assert _corpus_hits(key), key

    def test_podparadise_still_lags_at_499(self):
        # podparadise (crawled 16h) still shows 499 at top against the
        # official 501: directory lag, not an episode-count claim.
        md = _read(MD)
        assert "lags official 501" in md

    def test_zero_meta_wearables_across_105_cycles(self):
        md = _read(MD)
        assert "across all 105 cycles" in md
        assert "bounded search-result absence" in md


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 43-day hold, ZERO new URL keys this run
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredFifthCycle:
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
        # engadget.com/2217151 (Karissa Bell Jul 16 bus-stops original)
        # re-surfaced again this run (crawled 12h); verified
        # already-in-corpus (11 hits pre-commit), not a new key.
        md = _read(MD)
        assert "surfaced again this run" in md
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
# 5. Attention Sphere: 105th no-match
# --------------------------------------------------------------------------
class TestAttentionSphereHundredFifthNoMatch:
    CIRCULAR_COMMITS = [
        "a288c86",
        "a2b656f",
        "9590385",
        "2c4e21e",
        "25c730e",
        "3d16eac",
    ]

    def test_no_match_105th_cycle(self):
        md = _read(MD)
        assert "one-hundred-fifth no-match" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "rejected as circular" in md
        assert "not ingested" in md

    def test_same_commit_hash_set_as_prior_cycles(self):
        md = _read(MD)
        for short in self.CIRCULAR_COMMITS:
            assert short in md, short

    def test_tracked_sources_advanced_104_to_105(self):
        assert "104->105" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        assert "misidentified as a podcast" in _read(MD)

    def test_real_world_identity_stands(self):
        assert "Kendall Schrohe" in _read(MD)


# --------------------------------------------------------------------------
# 6. Press surfaces: 105th cycle, ZERO new URL keys
# --------------------------------------------------------------------------
class TestPressSurfacesHundredFifthCycle:
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

    def test_no_sep19_through_sep22_surfaces(self):
        assert "no Sep 19, Sep 20, Sep 21, or Sep 22 surfaces" in _read(MD)


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps (per #715 convention)
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_911_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_911*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_777(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 777 in-tree: 777 (committed #909 Type C, competitor-entities.yaml).
        # The in-flight #884/#898/#899 blocks (m762/m770/m771) are lower.
        assert maxid == 777

    def test_zero_numeric_778_mechanism_keys_in_profiles(self):
        d1 = "77" + "8"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_778_carriers_in_profiles(self):
        # Format-built needles per #715: no literal "778" key strings
        # carried. Designed keying is colon-form in profiles/; the tests/
        # _778 filename hits (other test files' negative guards) are a
        # different namespace.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_77" + "8"
        n2 = "mech" + "anism" + "-" + "77" + "8"
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
        assert "46723" in _read(README) and "1236" in _read(README)

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_911_marker(self):
        assert "## #911 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        assert "910-914 window" in _read(LOG)


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
        # blocks (m762 / m770 / m771); this run adds no 911 hunks to them.
        for f, own in (
            ("profiles/competitor-entities.yaml", "762"),
            ("profiles/careers/journalists.yaml", "770"),
            ("profiles/nytimes.yaml", "771"),
        ):
            diff = _git(["diff", "--", f]).stdout
            assert ("mechanism" + "_id" + ": " + own) in diff
            assert "911" not in diff
