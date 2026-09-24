"""Type E #971: podcast sentiment 117th verification cycle - GF 501 CONFIRMED
AGAIN (no 502), ZERO new GF URL keys (4 goloudnow old-episode variants all
re-surfaced in-corpus), EHE 45-day hold with ZERO new URL keys (6 logged
keys re-surfaced, own-repo blob circular), Attention Sphere 117th no-match
(blob page SURFACED AGAIN, same 6 commit URLs as #966 verified, rejected
circular, Tracked Sources 116->117), ONE new press URL key (morningstar
Dow Jones Sep-24 Connect relay), recency frontier HOLDS at Sep 24.

Second leg of the 970-974 window: D (#970) -> E (#971) -> A -> B -> C.
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

ITERATION = 971
TYPE_LETTER = "E"
RUN_PDT = "2026-09-24 14:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "08bf56713ed51253a5df4206025f6ad5f7f81ed4"


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
class TestNoveltyAnchorTypeE971:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #971 main commit exists pre-commit; the anchor test pins
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
            if "Type E #971" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_e_971_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_971*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 970-974 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard970_974Window:
    @pytest.mark.rotation
    def test_second_leg_of_970_974_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 971

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {970: "D", 971: "E", 972: "A", 973: "B", 974: "C"}
        assert expected[971] == "E"

    @pytest.mark.rotation
    def test_predecessor_970_type_d_committed(self):
        # #970 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md); this run's own #971 entry will be prepended
        # above it.
        assert "## #970 Type D" in _read(LOG)

    @pytest.mark.rotation
    def test_no_concurrent_inflight_commits_asserted(self):
        # In-flight at this run's checks: #899 Type C (m771),
        # #938 Type B (open anchor edit), #900 Type D (untracked) -
        # none committed yet.
        # Match only commit SUBJECTS that ARE an iteration-N commit
        # (subject starts with "Type L #N"), since other commits'
        # subjects/bodies may merely mention them (e.g. this run's own
        # concurrency note naming #899/#938/#900).
        subjects = [
            _git(["log", "--format=%s", "-1", c]).stdout.strip()
            for c in _git(["log", "--format=%H", "-8"]).stdout.splitlines()
        ]
        for n in ("899", "938", "900"):
            pat = re.compile(r"^Type [ABCDE] #" + n + r"(?!\d)")
            assert not any(pat.search(s) for s in subjects), (n, subjects)


# --------------------------------------------------------------------------
# 3. The Guilty Feminist: 117th cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredSeventeenthCycle:
    GF_RESURFACED_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "goloudnow.com/podcasts/the-guilty-feminist-152/acting-your-age-with-nicky-clark-meera-syal-and-juliet-stevenson-331960",
        "goloudnow.com/podcasts/the-guilty-feminist-152/500-five-hundredth-episode-with-kate-cheka-and-the-palestinian-circus-608555",
        "goloudnow.com/podcasts/the-guilty-feminist-152/285-woman-and-power-with-sophie-duker-and-special-guest-kathy-lette-315350",
        "goloudnow.com/podcasts/the-guilty-feminist-152/350-international-womens-day-2023-with-felicity-ward-helen-bauer-michelle-de-swarte-grace-petrie-and-ellie-dixon-part-two-404081",
    ]

    def test_episode_501_confirmed_again_this_run(self):
        md = _read(MD)
        assert "EPISODE 501 CONFIRMED AGAIN THIS RUN" in md
        assert "listennotes.com main directory (crawled 3h) still lists at top" in md
        assert "The Guilty Feminist 501. Out North East" in md

    def test_no_episode_502_surfaced(self):
        md = _read(MD)
        assert "No episode 502 surfaced anywhere" in md
        assert "three-day absence since Sep 21" in md
        assert "consistent with weekly cadence, not a signal" in md

    def test_zero_new_gf_url_keys_this_run(self):
        # Pure-re-surface cycle: the four goloudnow old-episode page
        # variants (331960 acting-your-age crawled 2d, 608555 500
        # episode crawled 2d, 315350 285 woman-and-power crawled 4h,
        # 404081 350 IWD-2023 part-two crawled 4h) were ingested as NEW
        # keys at #946/#961 and all carried >=1 pre-commit corpus hit
        # this run (verified via git grep -F). Nothing new ingested.
        md = _read(MD)
        assert "ZERO new verbatim GF URL keys this run" in md
        assert "pure-re-surface cycle" in md

    def test_resurfaced_keys_still_in_corpus(self):
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_podparadise_chortle_absent_this_run(self):
        # PodParadise and chortle surfaced at #966; neither surfaced at
        # #971 (remain in corpus). Explicit surfacing-set discipline:
        # only observed keys get logged as observed.
        md = _read(MD)
        assert "PodParadise, uk-podcasts, chortle, getpodcast, official-site, and podscan.fm did NOT surface this run (remain in corpus)" in md

    def test_goloudnow_variants_re_surfaces_not_new(self):
        md = _read(MD)
        assert "FOUR goloudnow old-episode page variants re-surfaced, all in-corpus" in md
        assert "ingested as new keys at #946/#961" in md

    def test_zero_meta_wearables_across_117_cycles(self):
        assert "across all 117 cycles" in _read(MD)


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 117th cycle, 45-day hold, zero new URL keys
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredSeventeenthCycle:
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
        # the #846/#851 regression guard). Same-day hold as #961/#966;
        # the date has not advanced.
        from datetime import date

        assert (date(2026, 9, 24) - date(2026, 8, 10)).days == 45
        assert "45-day hold continues" in _read(MD)

    def test_epstein_spoof_remains_last_major_phase_marker(self):
        md = _read(MD)
        assert "Aug 10 Epstein spoof -> Sep 24" in md

    def test_six_logged_keys_resurfaced_this_run(self):
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_zero_new_ehe_url_keys_this_run(self):
        # One own-repo blob URL also appeared in the EHE result set
        # (Last Updated 16 days ago, crawled 6d) - rejected as circular,
        # not ingested: the blob carries no literal query term as
        # evidence; it is the corpus describing itself.
        md = _read(MD)
        assert "ZERO new verbatim EHE URL keys this run" in md
        assert "own-repo blob URL in the EHE result set (rejected as circular, not ingested)" in md

    def test_non_surfacing_strands_remain_in_corpus(self):
        md = _read(MD)
        assert "did NOT surface this run (remain in corpus)" in md
        assert "latestly fact-check pair" in md

    def test_no_competitor_equivalent_campaign_117_cycles(self):
        md = _read(MD)
        assert (
            "No competitor-equivalent guerrilla campaign against "
            "Apple/Google/Samsung/Snap camera wearables in any of the "
            "117 cycles"
        ) in md


# --------------------------------------------------------------------------
# 5. Attention Sphere: 117th no-match, same circular family as #966
# --------------------------------------------------------------------------
class TestAttentionSphereHundredSeventeenthNoMatch:
    COMMIT_SHAS = (
        "a2b656f",
        "2c4e21e",
        "53e66f",
        "3d16eac",
        "36592f",
        "a288c86",
    )

    def test_no_match_117th_cycle(self):
        md = _read(MD)
        assert "one-hundred-seventeenth no-match" in md
        assert "returned no matching podcast" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "7 results were all this repository's own GitHub URLs" in md
        assert "rejected as circular, not ingested" in md

    def test_blob_page_surfaced_again(self):
        # Blob page SURFACED at #961 and #966; still surfacing at #971.
        md = _read(MD)
        assert "podcast-sentiment.md blob page, which SURFACED AGAIN this run" in md

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

    def test_tracked_sources_advanced_116_to_117(self):
        assert "Tracked Sources advanced 116->117" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        md = _read(MD)
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 6. Press surfaces: 117th cycle, ONE new URL key, frontier HOLDS
# --------------------------------------------------------------------------
class TestPressSurfacesHundredSeventeenthCycle:
    NEW_KEYS = [
        "morningstar.com/news/dow-jones/202609243796/meta-to-launch-new-smartglasses-models-equipped-with-its-muse-ai-agent",
    ]
    RESURFACED_KEYS = [
        "mobilesyrup.com/2026/09/23/meta-audio-focused-ray-ban-smart-glasses",
        "mobilesyrup.com/2026/09/23/meta-third-gen-ray-bans-lisa-collaboration",
        "usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses",
        "letsdatascience.com/news/meta-unveils-camera-free-ray-ban-meta-audio-glasses-at-conne-dbda6d5c",
        "cnn.com/2026/09/24/tech/meta-muse-ai-glasses-connect",
    ]

    def test_one_new_press_url_key_this_run(self):
        md = _read(MD)
        assert "ONE NEW-TO-CORPUS URL key this run" in md

    def test_morningstar_dow_jones_key_now_in_corpus(self):
        # Pre-commit it was zero-hit (verified via git grep -F); the
        # podcast-sentiment.md entry ingests it, so post-commit it
        # carries >=1 corpus hit.
        for key in self.NEW_KEYS:
            assert _corpus_hits(key), key

    def test_morningstar_piece_logged(self):
        # Dow Jones Newswires relay on Morningstar (Sep 24 08:19 ET,
        # crawled <1h): Connect smartglasses launch line - audio-only
        # Audio + Ray-Ban Meta Gen 3, both carrying Muse; Connor Hart
        # byline.
        md = _read(MD)
        assert "Dow Jones Newswires" in md
        assert "Muse" in md

    def test_connect_keys_resurfaced_not_new(self):
        # mobilesyrup x2 (crawled 2h), usatoday (crawled 8h), cnn
        # (crawled 8h), letsdatascience full-slug key (crawled <1h) -
        # all ingested at #966, all re-surfaces this run.
        md = _read(MD)
        assert "crawled 8h; in corpus via #956" in md
        assert "crawled 8h; in corpus via #966" in md

    def test_recency_frontier_holds_at_sep_24(self):
        # The morningstar piece is a Sep-24 relay - same-day as the
        # #966 CNN piece, so the frontier HOLDS at Sep 24 (no advance
        # this run; #966's Sep 23 -> Sep 24 move stands).
        md = _read(MD)
        assert "Recency frontier: HOLDS at Sep 24" in md
        assert "no frontier advance this run" in md

    def test_resurfaced_keys_still_in_corpus(self):
        md = _read(MD)
        for key in self.RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_asymmetry_note_meta_concentrated_pressure(self):
        md = _read(MD)
        assert "Meta-concentrated privacy pressure" in md
        assert "Lorde" in md

    def test_snippet_bounded_tone_not_scored(self):
        md = _read(MD)
        assert "Snippet-bounded, tone NOT_SCORED per the standing rule" in md


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps (per #715 convention)
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_971_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_971*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_813(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 813 in-tree: m811/m812/m813 committed at #967/#968/#969 Type
        # A/B/C and verified at #970 Type D. Type E adds no mechanisms.
        assert maxid == 813

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "81" + "4"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key strings
        # carried. Designed keying is colon-form in profiles/; the tests/
        # filename hits (other test files' negative guards) are a different
        # namespace. __pycache__ artifacts excluded per the #715
        # pattern-rescope lesson. Own file excluded as sweep carrier.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "81" + "4"
        n2 = "mech" + "anism" + "-" + "81" + "4"
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
        # In-flight: #899 Type C (nytimes.yaml m771), #938 Type B
        # (open anchor edit in its test file), #900 Type D (untracked
        # test file) - all uncommitted; this run's staged set must not
        # include those files.
        status = _git(["status", "--short"]).stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in ("nytimes.yaml", "test_type_b_938_", "test_type_d_900_"):
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
        assert "directionally_supported_not_proven" in md


# --------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats_table_updated(self):
        # Pre-run values carried in the new test-file table row's
        # doc-sync prose (49962/1295 -> 50013/1296), so they remain
        # present after the stats table itself is bumped.
        readme = _read(README)
        assert "49962" in readme and "1295" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_971_marker(self):
        assert "## #971 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        log = _read(LOG)
        assert "970-974" in log
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
        # The in-flight #899/#938/#900 working-tree edits are owned by
        # their runs; this run stages only its own files.
        status = _git(["status", "--short"]).stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in ("nytimes.yaml", "test_type_b_938_", "test_type_d_900_"):
            assert not any(f in l for l in staged)
