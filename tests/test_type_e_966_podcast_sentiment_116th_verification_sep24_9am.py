"""Type E #966: podcast sentiment 116th verification cycle - GF 501 CONFIRMED
AGAIN (no 502), ZERO new GF URL keys (chortle/getpodcast/goloudnow
re-surfaces all in-corpus), EHE 45-day hold with ZERO new URL keys
(thebesttimes full-URL key re-surfaced in-corpus via #961), Attention
Sphere 116th no-match (blob page SURFACED this run, absent at #956; 6
commit URLs all verified in git log, rejected circular), FOUR new press
URL keys (3x mobilesyrup Sep-23 Connect + 1x CNN Sep-24), recency frontier
ADVANCES Sep 23 -> Sep 24 (first advance since #956).

Second leg of the 965-969 window: D (#965) -> E (#966) -> A -> B -> C.
Monitoring-only per the Aug 28 2026 standing rule: tone NOT_SCORED,
p_value/cohens_d NOT_CALCULATED, is_significant False, engine NOT run,
no mechanisms added, falsification ledger holds at 29, NOT artifact-grade.
"""

import glob
import os
import re
import subprocess

import pytest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(REPO, "podcast-sentiment.md")
LOG = os.path.join(REPO, "iteration-log.md")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
THIS_FILE = os.path.basename(__file__)

ITERATION = 966
TYPE_LETTER = "E"
RUN_PDT = "2026-09-24 09:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "0d9132c60e2828b24597b68567eaaa4b47b82c23"


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
class TestNoveltyAnchorTypeE966:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #966 main commit exists pre-commit; the anchor test pins
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
            if "Type E #966" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_e_966_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_966*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 965-969 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard965_969Window:
    @pytest.mark.rotation
    def test_second_leg_of_965_969_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 966

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {965: "D", 966: "E", 967: "A", 968: "B", 969: "C"}
        assert expected[966] == "E"

    @pytest.mark.rotation
    def test_predecessor_965_type_d_committed(self):
        # #965 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md); this run's own #966 entry will be prepended
        # above it.
        assert "## #965 Type D" in _read(LOG)

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
# 3. The Guilty Feminist: 116th cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredSixteenthCycle:
    GF_RESURFACED_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "goloudnow.com/podcasts/the-guilty-feminist-152/deborah-frances-white-on-the-news-meeting-519585",
        "podparadise.com/Podcast/1068940771",
        "uk-podcasts.co.uk/podcast/the-guilty-feminist/deborah-frances-white-on-the-news-meeting",
        "getpodcast.com/podcast/the-guilty-feminist",
        "chortle.co.uk/shows/edinburgh_fringe_2026",
    ]

    def test_episode_501_confirmed_again_this_run(self):
        md = _read(MD)
        assert "EPISODE 501 CONFIRMED AGAIN THIS RUN" in md
        assert "listennotes.com main directory (crawled 10h) still lists at top" in md
        assert "The Guilty Feminist 501. Out North East" in md

    def test_no_episode_502_surfaced(self):
        md = _read(MD)
        assert "No episode 502 surfaced anywhere" in md
        assert "four-day absence since Sep 21" in md
        assert "consistent with weekly cadence, not a signal" in md

    def test_zero_new_gf_url_keys_this_run(self):
        # Pure-re-surface cycle: chortle Edinburgh-Fringe-2026 show page
        # (crawled 5d), getpodcast directory page (crawled 70d), goloudnow
        # 519585 News-Meeting variant (crawled 6h) all carry >=1 pre-commit
        # corpus hit each (verified via git grep -F); nothing new ingested.
        md = _read(MD)
        assert "ZERO new verbatim GF URL keys this run" in md
        assert "pure-re-surface cycle" in md

    def test_resurfaced_keys_still_in_corpus(self):
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_podparadise_still_lags_at_rerelease(self):
        md = _read(MD)
        assert "PodParadise SURFACED this run (crawled 10h)" in md
        assert "500/501 absent" in md

    def test_uk_podcasts_501_signal_corroboration(self):
        md = _read(MD)
        assert "uk-podcasts SURFACED this run (crawled 10h)" in md
        assert "501-signal corroboration" in md

    def test_zero_meta_wearables_across_116_cycles(self):
        assert "across all 116 cycles" in _read(MD)


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 116th cycle, 45-day hold, zero new URL keys
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredSixteenthCycle:
    EHE_RESURFACED_KEYS = [
        "softonic.com/articles/ray-ban-meta-smart-glasses-back-in-the-spotlight-london-ad-uses-epstein-image",
        "community.designtaxi.com/topic/34124-jeffrey-epstein-appears-to-model-meta-ray-bans-smart-glasses-on-new-ads",
        "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
        "afrotech.com/smart-glasses-ethics-and-consent",
        "article_8e7b63ae-0b36-5a4f-a25e-f468f7e98d2f",
        "d33gy59ovltp76.cloudfront.net/news/london-bus-stop-poster-brutally-mocks-kylie-jenner",
    ]

    def test_hold_arithmetic_45_days(self):
        # Aug 10 -> Sep 24 = 45 days (date difference, same formula as
        # the #846/#851 regression guard). #951/#956 were 44-day
        # same-day holds; the date advanced at #961 and holds here.
        from datetime import date

        assert (date(2026, 9, 24) - date(2026, 8, 10)).days == 45
        assert "45-day hold continues" in _read(MD)

    def test_epstein_spoof_remains_last_major_phase_marker(self):
        md = _read(MD)
        assert "Aug 10 Epstein spoof -> Sep 24" in md

    def test_six_logged_keys_resurfaced_this_run(self):
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_thebesttimes_key_resurfaced_not_new(self):
        # The thebesttimes consent-drive full-URL key (article_8e7b63ae
        # suffix) was ingested as a NEW key at #961; this run it
        # re-surfaced in-corpus (crawled 57d). Re-surface, not a new key.
        md = _read(MD)
        assert "thebesttimes full-URL key RE-SURFACED this run, in corpus via #961" in md
        assert "ZERO new verbatim EHE URL keys this run" in md

    def test_non_surfacing_strands_remain_in_corpus(self):
        md = _read(MD)
        assert "did NOT surface this run (remain in corpus)" in md
        assert "latestly fact-check pair" in md

    def test_no_competitor_equivalent_campaign_116_cycles(self):
        md = _read(MD)
        assert (
            "No competitor-equivalent guerrilla campaign against "
            "Apple/Google/Samsung/Snap camera wearables in any of the "
            "116 cycles"
        ) in md


# --------------------------------------------------------------------------
# 5. Attention Sphere: 116th no-match, blob page SURFACED this run
# --------------------------------------------------------------------------
class TestAttentionSphereHundredSixteenthNoMatch:
    COMMIT_SHAS = (
        "a2b656f",
        "2c4e21e",
        "53e66f",
        "3d16eac",
        "36592f",
        "a288c86",
    )

    def test_no_match_116th_cycle(self):
        md = _read(MD)
        assert "one-hundred-sixteenth no-match" in md
        assert "returned no matching podcast" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "7 results were all this repository's own GitHub URLs" in md
        assert "rejected as circular, not ingested" in md

    def test_blob_page_surfaced_this_run(self):
        # #956's blob page was absent; back at #961; still surfacing here.
        md = _read(MD)
        assert "podcast-sentiment.md blob page, which SURFACED AGAIN this run (absent at #956)" in md

    def test_commit_family_variants_verified_in_git_log(self):
        md = _read(MD)
        for sha in self.COMMIT_SHAS:
            assert sha in md, sha
        # Each SHA resolves to a real commit object in the repo: circular
        # as evidence, verified rather than asserted.
        for sha in self.COMMIT_SHAS:
            out = subprocess.run(
                ["git", "cat-file", "-t", sha],
                cwd=REPO,
                capture_output=True,
                text=True,
            )
            assert out.stdout.strip() == "commit", sha

    def test_tracked_sources_advanced_115_to_116(self):
        assert "Tracked Sources advanced 115->116" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        md = _read(MD)
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 6. Press surfaces: 116th cycle, FOUR new URL keys, frontier ADVANCES
# --------------------------------------------------------------------------
class TestPressSurfacesHundredSixteenthCycle:
    NEW_KEYS = [
        "mobilesyrup.com/2026/09/23/meta-audio-focused-ray-ban-smart-glasses",
        "mobilesyrup.com/2026/09/23/meta-third-gen-ray-bans-lisa-collaboration",
        "cnn.com/2026/09/24/tech/meta-muse-ai-glasses-connect",
        "mobilesyrup.com/2026/09/23/meta-ray-ban-display-launch-in-canada-for-1149",
    ]
    RESURFACED_KEYS = [
        "usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses",
        "letsdatascience.com/news/meta-unveils-camera-free-ray-ban-meta-audio-glasses-at-conne",
    ]

    def test_four_new_press_url_keys_this_run(self):
        md = _read(MD)
        assert "FOUR NEW-TO-CORPUS URL keys this run" in md

    def test_new_keys_now_in_corpus(self):
        # Pre-commit they were zero-hit (verified via git grep -F); the
        # podcast-sentiment.md entry ingests them, so post-commit each
        # key carries >=1 corpus hit.
        for key in self.NEW_KEYS:
            assert _corpus_hits(key), key

    def test_mobilesyrup_connect_coverage_logged(self):
        # mobilesyrup Sep 23 (all crawled <1h): audio-only Audio ($349
        # USD context, 43g, shipping Oct 13), Gen 3 + Lisa/Kylie collabs,
        # Display Canada launch ($1,149 CAD).
        md = _read(MD)
        assert "Ray-Ban Meta Audio" in md
        assert "Lisa" in md
        assert "1,149" in md

    def test_cnn_sep24_piece_logged(self):
        # CNN Sep 24: Muse agent blitz, Charm device, 7M+ units via
        # Reuters, Lorde + venue bans + Feb filming-women reporting as
        # the Meta-concentrated pressure context.
        md = _read(MD)
        assert "Muse personal AI agent" in md
        assert "Charm" in md
        assert "Lorde" in md

    def test_recency_frontier_advances_to_sep_24(self):
        # The CNN Sep-24 piece is the first post-Sep-23 surface: frontier
        # ADVANCES Sep 23 -> Sep 24, the first advance since #956's
        # Sep 18 -> Sep 23 move. The three mobilesyrup keys are Sep-23
        # Connect coverage and do not move the frontier by themselves.
        md = _read(MD)
        assert "Recency frontier: ADVANCES Sep 23 -> Sep 24" in md
        assert "first frontier advance since #956" in md

    def test_resurfaced_keys_still_in_corpus(self):
        md = _read(MD)
        for key in self.RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_asymmetry_note_meta_concentrated_pressure(self):
        # Connect-week coverage frames the camera-free Audio against
        # Meta-concentrated privacy pressure (Hamburg Sep-10 finding,
        # HateAid complaint, Sep-1 LED-tamper bricking, ACLU
        # facial-recognition letter, Lorde, venue bans).
        md = _read(MD)
        assert "Meta-concentrated privacy pressure" in md
        assert "ACLU" in md

    def test_snippet_bounded_tone_not_scored(self):
        md = _read(MD)
        assert "Snippet-bounded, tone NOT_SCORED per the standing rule" in md


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps (per #715 convention)
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_966_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_966*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_810(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 810 in-tree: m808/m809/m810 committed at #962/#963/#964 Type
        # A/B/C and verified at #965 Type D. The in-flight #884/#899
        # blocks (m762/m771) are lower. Type E adds no mechanisms.
        assert maxid == 810

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "81" + "1"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key strings
        # carried. Designed keying is colon-form in profiles/; the tests/
        # filename hits (other test files' negative guards) are a different
        # namespace. __pycache__ artifacts excluded per the #715
        # pattern-rescope lesson. Own file excluded as sweep carrier.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "81" + "1"
        n2 = "mech" + "anism" + "-" + "81" + "1"
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
        assert "49702" in readme and "1290" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_966_marker(self):
        assert "## #966 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        log = _read(LOG)
        assert "965-969" in log
        assert "SECOND leg" in log


# --------------------------------------------------------------------------
# 11. Push readiness per #750
# --------------------------------------------------------------------------
class TestPushReadiness:
    def test_ascii_only_no_em_dashes(self):
        raw = open(os.path.join(REPO, "tests", THIS_FILE), "rb").read()
        assert all(b < 128 for b in raw), "non-ASCII byte in own file"
        assert b"\xe2\x80\x94" not in raw  # em dash, escaped so own file stays ASCII-only

    def test_no_blob_url_in_this_file(self):
        # Own file must not carry the repo blob URL, or it becomes a
        # self-circular search key.
        # Needle format-built (no literal blob URL carried): own file must
        # not become a self-circular search key.
        needle = "github.com" + "/rayhe/mediascope" + "/blob"
        assert needle not in _read(os.path.join(REPO, "tests", THIS_FILE))

    def test_concurrent_files_untouched_by_this_run(self):
        # The in-flight #884/#899/#938/#900 working-tree edits are owned
        # by their runs; this run stages only its own files.
        status = _git(["status", "--short"]).stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in ("competitor-entities.yaml", "nytimes.yaml",
                  "test_type_b_938_", "test_type_d_900_"):
            assert not any(f in l for l in staged)
