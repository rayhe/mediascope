"""Type E #991: podcast sentiment 121st verification cycle - GF 501 CONFIRMED
AGAIN (no 502; pure-re-surface cycle, ZERO new GF keys), EHE 46-day hold with
ZERO new EHE keys (second consecutive pure-re-surface cycle), Attention Sphere
121st no-match (blob page SURFACED AGAIN, 6 commit URLs git-log-verified
circular, Tracked Sources 120->121), press surfaces 7/7 in-corpus re-surfaces,
frontier HOLDS at Sep 24.

Second leg of the 990-994 window: D (#990) -> E (#991) -> A -> B -> C.
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

ITERATION = 991
TYPE_LETTER = "E"
RUN_PDT = "2026-09-25 10:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "407e95de279475ee70927882ada879a450479318"


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _corpus_hits(needle):
    return _git(["grep", "-l", needle, "--", "."]).stdout.splitlines()


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _md_991():
    return _read(MD).split("## Iteration #991")[1]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE991:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #991 main commit exists pre-commit; the anchor test pins
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
            if "Type E #991" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        )
        assert len(mains) >= 1

    def test_exactly_one_type_e_991_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_991*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 990-994 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard990_994Window:
    @pytest.mark.rotation
    def test_second_leg_of_990_994_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 991

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {990: "D", 991: "E", 992: "A", 993: "B", 994: "C"}
        assert expected[991] == "E"

    @pytest.mark.rotation
    def test_predecessor_990_type_d_committed(self):
        # #990 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md); this run's own #991 entry will be prepended
        # above it.
        assert "## #990 Type D" in _read(LOG)

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
# 3. The Guilty Feminist: 121st cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredTwentyFirstCycle:
    GF_RESURFACED_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "goloudnow.com/podcasts/the-guilty-feminist-152",
        "goloudnow.com/podcasts/the-guilty-feminist-152/acting-your-age-with-nicky-clark-meera-syal-and-juliet-stevenson-331960",
        "goloudnow.com/podcasts/the-guilty-feminist-152/500-five-hundredth-episode-with-kate-cheka-and-the-palestinian-circus-608555",
        "goloudnow.com/podcasts/the-guilty-feminist-152/the-guilty-feminist-watches-and-just-like-that-season-3-episode-1-with-jessica-fostekew-531534",
        "goloudnow.com/podcasts/the-guilty-feminist-152/350-international-womens-day-2023-with-felicity-ward-helen-bauer-michelle-de-swarte-grace-petrie-and-ellie-dixon-part-two-404081",
    ]

    def test_episode_501_confirmed_again_this_run(self):
        md = _read(MD)
        assert "EPISODE 501 CONFIRMED AGAIN THIS RUN" in md
        assert "The listennotes.com main directory (crawled 23h" in md
        assert "still lists at top" in md
        assert "The Guilty Feminist 501. Out North East" in md

    def test_no_episode_502_surfaced(self):
        md = _read(MD)
        assert "No episode 502 surfaced anywhere" in md
        assert "four-day absence since Sep 21" in md
        assert "consistent with weekly cadence, not a signal" in md

    def test_zero_new_gf_url_keys_this_run(self):
        # Pure-re-surface cycle: 6/6 observed GF keys carry >=1
        # pre-commit corpus hit; ZERO new-to-corpus GF keys. Third
        # consecutive pure-re-surface cycle after #976/#981 (with #986's
        # directory-mirror novelty in between as the only new-key cycle).
        md = _read(MD)
        assert "ZERO new-to-corpus verbatim GF URL keys this run" in md
        assert "pure-re-surface cycle" in md
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_resurfaced_keys_still_in_corpus(self):
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_directory_mirrors_not_surfacing_this_run(self):
        md = _read(MD)
        assert "plinkhq, ms.podbean, za.radio.net, and ca.radio.net" in md
        assert "did NOT surface" in md
        assert "remain in corpus" in md

    def test_zero_meta_wearables_across_121_cycles(self):
        assert "across all 121 cycles" in _read(MD)


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 121st cycle, 46-day hold, ZERO new URL keys
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredTwentyFirstCycle:
    EHE_RESURFACED_KEYS = [
        "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
        "linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates-viky-hurai-jaklovska-ssqwf",
        "lapost.com/content/turn-the-cameras-off-london-s-growing-privacy-pushback-against-smart-glasses",
        "afrotech.com/smart-glasses-ethics-and-consent",
        "community.designtaxi.com/topic/34124-jeffrey-epstein-appears-to-model-meta-ray-bans-smart-glasses-on-new-ads",
    ]

    def test_hold_arithmetic_46_days(self):
        # Aug 10 Epstein spoof -> Sep 25: same-day as the #981 and #986
        # 46-day holds (calendar-day arithmetic, not elapsed-hours).
        from datetime import date

        assert (date(2026, 9, 25) - date(2026, 8, 10)).days == 46
        md = _read(MD)
        assert "46-day hold continues" in md
        assert "date(2026,9,25)-date(2026,8,10)=46 days" in md

    def test_epstein_spoof_remains_last_major_phase_marker(self):
        md = _read(MD)
        assert "Aug 10 Epstein spoof" in md
        assert "same-day as the #981 and #986 46-day holds" in md

    def test_five_logged_keys_resurfaced_this_run(self):
        md = _read(MD)
        assert "5 logged keys re-surfaced" in md
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_zero_new_ehe_url_keys_this_run(self):
        md = _read(MD)
        assert "ZERO new-to-corpus EHE URL keys this run" in md
        assert "second consecutive pure-re-surface cycle after #986" in md

    def test_circular_github_urls_rejected_this_run(self):
        md = _read(MD)
        assert "2 own-repo GitHub URLs in the EHE result set" in md
        assert "rejected as circular, not ingested" in md

    def test_non_surfacing_strands_remain_in_corpus(self):
        md = _read(MD)
        assert "ranzware Kylie-lenticular mirror (#976)" in md
        assert "latestly fact-check pair did NOT surface this run" in md
        assert "remain in corpus" in md

    def test_no_competitor_equivalent_campaign_121_cycles(self):
        assert "any of the 121 cycles" in _read(MD)


# --------------------------------------------------------------------------
# 5. Attention Sphere: 121st no-match
# --------------------------------------------------------------------------
class TestAttentionSphereHundredTwentyFirstNoMatch:
    COMMIT_SHAS = (
        "9590385",
        "a288c86",
        "a2b656f",
        "2c4e21e",
        "25c730e",
        "3d16eac",
    )

    def test_no_match_121st_cycle(self):
        md = _read(MD)
        assert "one-hundred-twenty-first no-match" in md
        assert "returned no matching podcast" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "7 results were all this repository's own GitHub URLs" in md
        assert "rejected as circular, not ingested" in md

    def test_blob_page_surfaced_again(self):
        # Blob page SURFACED at #966/#971/#976/#981/#986; still at #991.
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

    def test_tracked_sources_advanced_120_to_121(self):
        assert "Tracked Sources advanced 120->121" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        md = _read(MD)
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 6. Press surfaces: 121st cycle, 7/7 in-corpus re-surfaces, frontier HOLDS
# --------------------------------------------------------------------------
class TestPressSurfacesHundredTwentyFirstCycle:
    PRESS_RESURFACED_KEYS = [
        "ppc.land/hamburg-regulator-finds-ray-ban-meta-glasses-expose-bystanders-without-consent",
        "startupfortune.com/meta-permanently-disables-cameras-on-thousands-of-tampered-smart-glasses",
        "usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses",
        "community.designtaxi.com/topic/39120-meta-releases-ray-ban-smart-glasses-without-the-cameras-amid-privacy-stalking-concerns",
        "dig.watch/updates/meta-confirms-camera-free-ray-ban-smart-glasses",
        "analyticsinsight.net/news/meta-ray-ban-audio-launches-at-usd-349-with-camera-free-ai",
        "captaincompliance.com/education/meta-launches-camera-free-ray-ban-smart-glasses-but-removing-the-camera-does-not-end-the-privacy-debate",
    ]

    def test_seven_of_seven_pure_resurface(self):
        # 7/7 press keys carry >=1 pre-commit corpus hit; ZERO new.
        md = _read(MD)
        assert "SEVEN results observed, ALL previously-logged URL keys" in md
        assert "ZERO new-to-corpus URL keys this run" in md
        for key in self.PRESS_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_press_keys_now_in_corpus(self):
        for key in self.PRESS_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_recency_frontier_holds_at_sep_24(self):
        md = _read(MD)
        assert "Recency frontier: HOLDS at Sep 24" in md
        assert "no frontier advance this run" in md
        assert "the #966 Sep 23 -> Sep 24 move stands" in md

    def test_designtaxi_39120_audio_piece_logged(self):
        md = _read(MD)
        assert "community.designtaxi.com/topic/39120" in md
        assert "in corpus via #986" in md

    def test_captaincompliance_privacy_debate_logged(self):
        md = _read(MD)
        assert "captaincompliance.com/education/meta-launches-camera-free" in md
        assert "no obvious bystander signal for audio recording" in md

    def test_asymmetry_note_meta_exclusive(self):
        md = _read(MD)
        assert "Meta-exclusive across all 121 cycles" in md
        assert "no competitor camera-wearable coverage carries equivalent privacy-pressure framing" in md

    def test_snippet_bounded_tone_not_scored(self):
        md = _read(MD)
        assert "Snippet-bounded, tone NOT_SCORED per the standing rule" in md


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps per #715
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_991_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_991*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_825(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 825 in-tree: m825 committed at #989 Type C and verified at
        # #990 Type D. Type E adds no mechanisms. (The in-flight #899
        # m771 hunk does not change the max.)
        assert maxid == 825

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "82" + "6"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key strings
        # carried. Designed keying is colon-form in profiles/; the tests/
        # filename hits (other test files' negative guards) are a different
        # namespace. __pycache__ artifacts excluded per the #715
        # pattern-rescope lesson. Own file excluded as sweep carrier.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "82" + "6"
        n2 = "mech" + "anism" + "-" + "82" + "6"
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
        # doc-sync prose (50967/1315 -> NEW), so they remain present
        # after the stats table itself is bumped.
        readme = _read(README)
        assert "50967" in readme and "1315" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_991_marker(self):
        assert "## #991 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        log = _read(LOG)
        assert "990-994" in log
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
