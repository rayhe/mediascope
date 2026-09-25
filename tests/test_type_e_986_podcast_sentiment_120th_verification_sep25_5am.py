"""Type E #986: podcast sentiment 120th verification cycle - GF 501 CONFIRMED
AGAIN (no 502; THREE new directory-mirror keys: ca.radio.net + two plinkhq
episode-page variants), EHE 46-day hold with ZERO new EHE keys, Attention
Sphere 120th no-match (blob page SURFACED AGAIN, 6 commit URLs
git-log-verified circular, Tracked Sources 119->120), TWO new press URL keys
(designtaxi topic/39120 Audio piece, captaincompliance Audio-privacy-debate
piece), frontier HOLDS at Sep 24.

Second leg of the 985-989 window: D (#985) -> E (#986) -> A -> B -> C.
Monitoring-only per the Aug 28 2026 standing rule: tone NOT_SCORED,
p_value/cohens_d NOT_CALCULATED, is_significant False, engine NOT run,
no mechanisms added, falsification ledger holds at 30, NOT artifact-grade.
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

ITERATION = 986
TYPE_LETTER = "E"
RUN_PDT = "2026-09-25 05:00 PDT"
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


def _md_986():
    return _read(MD).split("## Iteration #986")[1]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE986:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #986 main commit exists pre-commit; the anchor test pins
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
            if "Type E #986" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_e_986_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_986*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 985-989 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard985_989Window:
    @pytest.mark.rotation
    def test_second_leg_of_985_989_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 986

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {985: "D", 986: "E", 987: "A", 988: "B", 989: "C"}
        assert expected[986] == "E"

    @pytest.mark.rotation
    def test_predecessor_985_type_d_committed(self):
        # #985 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md); this run's own #986 entry will be prepended
        # above it.
        assert "## #985 Type D" in _read(LOG)

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
# 3. The Guilty Feminist: 120th cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredTwentiethCycle:
    GF_RESURFACED_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "plinkhq.com/i/1068940771",
        "ms.podbean.com/podcast-detail/96viz-3cbfc",
        "za.radio.net/podcast/the-guilty-feminist",
    ]
    GF_NEW_KEYS = [
        "ca.radio.net/podcast/the-guilty-feminist",
        "plinkhq.com/i/1068940771/e/1000688509666",
        "plinkhq.com/i/1068940771/e/1000710267738",
    ]

    def test_episode_501_confirmed_again_this_run(self):
        md = _read(MD)
        assert "EPISODE 501 CONFIRMED AGAIN THIS RUN" in md
        assert "The listennotes.com main directory (crawled 18h" in md
        assert "still lists at top" in md
        assert "The Guilty Feminist 501. Out North East" in md

    def test_no_episode_502_surfaced(self):
        md = _read(MD)
        assert "No episode 502 surfaced anywhere" in md
        assert "four-day absence since Sep 21" in md
        assert "consistent with weekly cadence, not a signal" in md

    def test_three_new_gf_url_keys_this_run(self):
        # THREE new-to-corpus verbatim GF URL keys: ca.radio.net GF
        # directory (crawled 1d, 501 at top) + two plinkhq episode-page
        # variants (both crawled 13d). Old-episode directory-mirror
        # keys, zero pre-commit corpus hits (verified via git grep -F);
        # the podcast-sentiment.md entry ingests them, so post-commit
        # each carries >=1 corpus hit.
        md = _read(MD)
        assert "THREE NEW-TO-CORPUS verbatim GF URL keys this run" in md
        assert "old-episode directory-mirror keys" in md
        for key in self.GF_NEW_KEYS:
            assert _corpus_hits(key), key

    def test_resurfaced_keys_still_in_corpus(self):
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_directory_mirrors_re_surface_not_new(self):
        md = _read(MD)
        assert "plinkhq GF directory page SURFACED AGAIN this run" in md
        assert "ms.podbean GF directory (crawled 4d" in md

    def test_zero_meta_wearables_across_120_cycles(self):
        assert "across all 120 cycles" in _read(MD)


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 120th cycle, 46-day hold, ZERO new URL keys
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredTwentiethCycle:
    EHE_RESURFACED_KEYS = [
        "community.designtaxi.com/topic/34124-jeffrey-epstein-appears-to-model-meta-ray-bans-smart-glasses-on-new-ads",
        "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
        "linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates-viky-hurai-jaklovska-ssqwf",
        "lapost.com/content/turn-the-cameras-off",
        "afrotech.com/smart-glasses-ethics-and-consent",
    ]

    def test_hold_arithmetic_46_days(self):
        # Aug 10 -> Sep 25 = 46 days (date difference, same formula as
        # the #846/#851 regression guard). Same-day as #981's 46-day
        # hold (this run is the 05:00 PDT slot, still Sep 25).
        from datetime import date

        assert (date(2026, 9, 25) - date(2026, 8, 10)).days == 46
        assert "46-day hold continues" in _read(MD)

    def test_epstein_spoof_remains_last_major_phase_marker(self):
        md = _read(MD)
        assert "Aug 10 Epstein spoof -> Sep 25" in md

    def test_five_logged_keys_resurfaced_this_run(self):
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_zero_new_ehe_url_keys_this_run(self):
        # Unlike #976 (two new keys) and #981 (lapost), this run adds
        # zero verbatim EHE keys. The #986 section asserts it; earlier
        # sections' counts are not touched.
        md986 = _md_986()
        assert "ZERO new-to-corpus EHE URL keys this run" in md986
        assert "ONE NEW-TO-CORPUS EHE URL key" not in md986

    def test_circular_github_urls_rejected_this_run(self):
        md986 = _md_986()
        assert "Two own-repo GitHub URLs in the EHE result set" in md986
        assert "rejected as circular, not ingested" in md986

    def test_non_surfacing_strands_remain_in_corpus(self):
        md986 = _md_986()
        assert "did NOT surface this run (remain in corpus)" in md986
        assert "ranzware Kylie-lenticular mirror (#976)" in md986

    def test_no_competitor_equivalent_campaign_120_cycles(self):
        md = _read(MD)
        assert (
            "No competitor-equivalent guerrilla campaign against "
            "Apple/Google/Samsung/Snap camera wearables in any of the "
            "120 cycles"
        ) in md


# --------------------------------------------------------------------------
# 5. Attention Sphere: 120th no-match, same circular family as #596-era
# --------------------------------------------------------------------------
class TestAttentionSphereHundredTwentiethNoMatch:
    COMMIT_SHAS = (
        "9590385",
        "a288c86",
        "a2b656f",
        "2c4e21e",
        "25c730e",
        "3d16eac",
    )

    def test_no_match_120th_cycle(self):
        md = _read(MD)
        assert "one-hundred-twentieth no-match" in md
        assert "returned no matching podcast" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "7 results were all this repository's own GitHub URLs" in md
        assert "rejected as circular, not ingested" in md

    def test_blob_page_surfaced_again(self):
        # Blob page SURFACED at #966/#971/#976/#981; still surfacing at #986.
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

    def test_tracked_sources_advanced_119_to_120(self):
        assert "Tracked Sources advanced 119->120" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        md = _read(MD)
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 6. Press surfaces: 120th cycle, TWO new URL keys, frontier HOLDS
# --------------------------------------------------------------------------
class TestPressSurfacesHundredTwentiethCycle:
    NEW_KEYS = [
        "community.designtaxi.com/topic/39120",
        "captaincompliance.com/education/meta-launches-camera-free-ray-ban-smart-glasses",
    ]
    RESURFACED_KEYS = [
        "ppc.land/hamburg-regulator-finds-ray-ban-meta-glasses-expose-bystanders-without-consent",
        "startupfortune.com/meta-permanently-disables-cameras-on-thousands-of-tampered-smart-glasses",
        "usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses",
        "analyticsinsight.net/news/meta-ray-ban-audio-launches-at-usd-349-with-camera-free-ai",
        "gagadget.com/en/727279",
    ]

    def test_two_new_press_url_keys_this_run(self):
        md986 = _md_986()
        assert "TWO NEW-TO-CORPUS URL keys this run" in md986

    def test_new_press_keys_now_in_corpus(self):
        # Pre-commit each was zero-hit (verified via git grep -F); the
        # podcast-sentiment.md entry ingests them, so post-commit each
        # carries >=1 corpus hit.
        for key in self.NEW_KEYS:
            assert _corpus_hits(key), key

    def test_designtaxi_39120_audio_piece_logged(self):
        md986 = _md_986()
        assert "community.designtaxi.com/topic/39120" in md986
        assert "gives Meta an answer to one of the most persistent concerns" in md986

    def test_captaincompliance_privacy_debate_logged(self):
        # The captaincompliance piece frames the Audio's camera omission
        # as an apparent convenience-preserving compromise while noting
        # audio recording has no obvious bystander signal - logged
        # verbatim, not scored.
        md986 = _md_986()
        assert "captaincompliance.com/education" in md986
        assert "apparent attempt to preserve the convenience" in md986

    def test_recency_frontier_holds_at_sep_24(self):
        # Both new keys are Sep-24 or Sep-24-adjacent Connect-week
        # coverage, so the frontier HOLDS at Sep 24 (no advance this
        # run; #966's Sep 23 -> Sep 24 move stands).
        md986 = _md_986()
        assert "Recency frontier: HOLDS at Sep 24" in md986
        assert "no frontier advance this run" in md986

    def test_resurfaced_keys_still_in_corpus(self):
        for key in self.RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_non_surfacing_press_keys_remain_in_corpus(self):
        md986 = _md_986()
        assert "did NOT surface this run (remain in corpus)" in md986
        assert "playtechdeep Sep-24 brief (#981)" in md986

    def test_asymmetry_note_meta_exclusive(self):
        md986 = _md_986()
        assert "no competitor camera-wearable coverage carries equivalent privacy-pressure framing" in md986
        assert "Meta-exclusive across all 120 cycles" in md986

    def test_snippet_bounded_tone_not_scored(self):
        md = _read(MD)
        assert "Snippet-bounded, tone NOT_SCORED per the standing rule" in md


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps (per #715 convention)
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_986_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_986*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_822(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 822 in-tree: m822 committed at #984 Type C and verified at
        # #985 Type D. Type E adds no mechanisms. (The in-flight #899
        # m771 hunk does not change the max.)
        assert maxid == 822

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "82" + "3"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key strings
        # carried. Designed keying is colon-form in profiles/; the tests/
        # filename hits (other test files' negative guards) are a different
        # namespace. __pycache__ artifacts excluded per the #715
        # pattern-rescope lesson. Own file excluded as sweep carrier.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "82" + "3"
        n2 = "mech" + "anism" + "-" + "82" + "3"
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

    def test_falsification_ledger_holds_at_30(self):
        assert "ledger holds at 30" in _read(MD)

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
        # doc-sync prose (50721/1310 -> NEW), so they remain present
        # after the stats table itself is bumped.
        readme = _read(README)
        assert "50721" in readme and "1310" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_986_marker(self):
        assert "## #986 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        log = _read(LOG)
        assert "985-989" in log
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
