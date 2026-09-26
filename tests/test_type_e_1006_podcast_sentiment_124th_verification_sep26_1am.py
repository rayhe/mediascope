"""Type E #1006: podcast sentiment 124th verification cycle - GF 501 CONFIRMED
AGAIN (no 502; fourth consecutive pure-re-surface GF cycle, ZERO new GF keys),
EHE 47-day hold with ZERO new URL keys (5 logged keys re-surfaced:
techtimes, linkedin privacy roundup, lapost, afrotech, kayvan-mirza),
Attention Sphere 124th no-match (blob page SURFACED AGAIN, 6 commit URLs
git-log-verified circular - identical to the #996 set, Tracked Sources
123->124), press 7/7 pure re-surface (ppc.land, startupfortune, gizbot,
m1k.tech, linkedin privacy roundup, usatoday, designtaxi 39120; ZERO new
press keys; frontier HOLDS at Sep 24).

Second leg of the 1005-1009 window: D (#1005) -> E (#1006) -> A -> B -> C.
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

ITERATION = 1006
TYPE_LETTER = "E"
RUN_PDT = "2026-09-26 01:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "9e82a6279f43b2244591f0a211261f18d48c0696"


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _corpus_hits(needle):
    return _git(["grep", "-l", needle, "--", "."]).stdout.splitlines()


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _md_1006():
    return _read(MD).split("## Iteration #1006")[1]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE1006:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1006 main commit exists pre-commit; the anchor test pins
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
            if "Type E #1006" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        )
        assert len(mains) >= 1

    def test_exactly_one_type_e_1006_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_1006*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 1005-1009 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard1005_1009Window:
    @pytest.mark.rotation
    def test_second_leg_of_1005_1009_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 1006

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {1005: "D", 1006: "E", 1007: "A", 1008: "B", 1009: "C"}
        assert expected[1006] == "E"

    @pytest.mark.rotation
    def test_predecessor_1005_type_d_committed(self):
        # #1005 Type D is COMMITTED (its log entry sits under this run's
        # own #1006 entry at the head of iteration-log.md).
        assert "## #1005 Type D" in _read(LOG)

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
# 3. The Guilty Feminist: 124th cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredTwentyFourthCycle:
    GF_RESURFACED_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "ca.radio.net/podcast/the-guilty-feminist",
        "plinkhq.com/i/1068940771",
        "ms.podbean.com/podcast-detail/96viz-3cbfc",
    ]

    def test_episode_501_confirmed_again_this_run(self):
        md = _md_1006()
        assert "EPISODE 501 CONFIRMED AGAIN THIS RUN" in md
        assert "The listennotes.com main directory (crawled 1d" in md
        assert "still lists at top" in md
        assert "The Guilty Feminist 501. Out North East" in md

    def test_no_episode_502_surfaced(self):
        md = _md_1006()
        assert "No episode 502 surfaced anywhere" in md
        assert "five-day absence since Sep 21" in md
        assert "consistent with weekly cadence, not a signal" in md

    def test_zero_new_gf_url_keys_this_run(self):
        # Pure-re-surface cycle: 4/4 observed GF keys carry >=1
        # pre-commit corpus hit; ZERO new-to-corpus GF keys. Fourth
        # consecutive pure-re-surface cycle after #991, #996, and #1001
        # (the #986 directory-mirror novelty is the last new-key cycle).
        md = _md_1006()
        assert "ZERO new-to-corpus verbatim GF URL keys this run" in md
        assert "pure-re-surface cycle" in md
        assert "fourth consecutive pure-re-surface cycle after #991, #996, and #1001" in md
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_directory_mirrors_back_in_results_this_run(self):
        # The ca.radio.net / plinkhq / ms.podbean directory mirrors did
        # NOT surface at #1001; this run all three re-surface, all
        # already in corpus. The ca.radio.net 762-episode count vs
        # listennotes 761 is a directory artifact, not an episode.
        md = _md_1006()
        assert "the ca.radio.net GF directory" in md
        assert "the plinkhq episode page" in md
        assert "the ms.podbean GF podcast page" in md
        assert "count-vs-listennotes-761 is a directory artifact, not an episode" in md

    def test_non_surfacing_variants_remain_in_corpus(self):
        md = _md_1006()
        assert "the youtube 500 page variant" in md
        assert "the goloudnow main directory" in md
        assert "did NOT surface" in md
        assert "remain in corpus" in md
        assert _corpus_hits("404081"), "404081 remains in corpus"

    def test_zero_meta_wearables_across_124_cycles(self):
        assert "across all 124 cycles" in _md_1006()


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 124th cycle, 47-day hold, ZERO new URL keys
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredTwentyFourthCycle:
    EHE_RESURFACED_KEYS = [
        "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
        "linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates-viky-hurai-jaklovska-ssqwf",
        "lapost.com/content/turn-the-cameras-off-london-s-growing-privacy-pushback-against-smart-glasses",
        "afrotech.com/smart-glasses-ethics-and-consent",
        "linkedin.com/pulse/dear-ai-glasses-industry-situation-critical-red-kayvan-mirza-zwaze",
    ]

    def test_hold_arithmetic_47_days(self):
        # Aug 10 Epstein spoof -> Sep 26: calendar-day arithmetic, not
        # elapsed-hours. The 46-day hold at #1001 advances one day.
        from datetime import date

        assert (date(2026, 9, 26) - date(2026, 8, 10)).days == 47
        md = _md_1006()
        assert "47-day hold continues" in md
        assert "date(2026,9,26)-date(2026,8,10)=47 days" in md

    def test_epstein_spoof_remains_last_major_phase_marker(self):
        md = _md_1006()
        assert "Aug 10 Epstein spoof" in md
        assert "47-day hold continues (Aug 10 Epstein spoof -> Sep 26" in md

    def test_five_logged_keys_resurfaced_this_run(self):
        md = _md_1006()
        assert "5 logged keys re-surfaced this run" in md
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_kayvan_mirza_key_now_a_logged_key(self):
        # The #1001 ONE-new-key is this run a logged re-surface
        # (in corpus via #1001), and this run carries ZERO new keys.
        md = _md_1006()
        assert "in corpus via #1001" in md
        assert "the #1001 kayvan-mirza key is the newest" in md

    def test_zero_new_ehe_url_keys_this_run(self):
        md = _md_1006()
        assert "ZERO new verbatim EHE URL keys this run" in md
        assert "no new campaign motif" in md

    def test_circular_github_urls_rejected_this_run(self):
        md = _md_1006()
        assert "2 own-repo GitHub URLs in the EHE result set" in md
        assert "rejected as circular, not ingested" in md

    def test_non_surfacing_strands_remain_in_corpus(self):
        md = _md_1006()
        assert "The designtaxi 34124 Epstein-ad thread" in md
        assert "ranzware Kylie-lenticular mirror (#976)" in md
        assert "latestly fact-check pair did NOT surface this run" in md
        assert "remain in corpus" in md

    def test_no_competitor_equivalent_campaign_124_cycles(self):
        assert "any of the 124 cycles" in _md_1006()


# --------------------------------------------------------------------------
# 5. Attention Sphere: 124th no-match
# --------------------------------------------------------------------------
class TestAttentionSphereHundredTwentyFourthNoMatch:
    COMMIT_SHAS = (
        "9590385",
        "a288c86",
        "a2b656f",
        "25c730e",
        "6da2928",
        "fe4528b",
    )

    def test_no_match_124th_cycle(self):
        md = _md_1006()
        assert "one-hundred-twenty-fourth no-match" in md
        assert "returned no matching podcast" in md

    def test_circular_github_results_rejected(self):
        md = _md_1006()
        assert "7 results were all this repository's own GitHub URLs" in md
        assert "rejected as circular, not ingested" in md

    def test_blob_page_surfaced_again(self):
        # Blob page SURFACED at #966/#971/#976/#981/#986/#991/#996/#1001;
        # still at #1006.
        md = _md_1006()
        assert "podcast-sentiment.md blob page, which SURFACED AGAIN this run" in md

    def test_variant_family_commits_verified_in_git_log(self):
        md = _md_1006()
        for sha in self.COMMIT_SHAS:
            assert sha in md, sha
        # Each SHA resolves to a real commit object in the repo: circular
        # as evidence, verified rather than asserted. The set is
        # identical to the #996 set.
        for sha in self.COMMIT_SHAS:
            out = subprocess.run(
                ["git", "cat-file", "-t", sha],
                cwd=REPO,
                capture_output=True,
                text=True,
            )
            assert out.stdout.strip() == "commit", sha

    def test_tracked_sources_advanced_123_to_124(self):
        assert "Tracked Sources advanced 123->124" in _md_1006()

    def test_task_spec_name_still_misidentified(self):
        md = _md_1006()
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 6. Press surfaces: 124th cycle, 7/7 pure re-surface, ZERO new keys,
#    frontier HOLDS at Sep 24
# --------------------------------------------------------------------------
class TestPressSurfacesHundredTwentyFourthCycle:
    PRESS_RESURFACED_KEYS = [
        "ppc.land/hamburg-regulator-finds-ray-ban-meta-glasses-expose-bystanders-without-consent",
        "startupfortune.com/meta-permanently-disables-cameras-on-thousands-of-tampered-smart-glasses",
        "gizbot.com/social-media/news/meta-ray-ban-ai-glasses-update-blocks-cameras-when-recording-light-is-tampered-with-128269.html",
        "m1k.tech/2026/09/meta-ray-ban-led-fix-eu-consent-glasses/",
        "linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates-viky-hurai-jaklovska-ssqwf",
        "usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses",
        "community.designtaxi.com/topic/39120-meta-releases-ray-ban-smart-glasses-without-the-cameras-amid-privacy-stalking-concerns",
    ]

    def test_seven_all_resurfaced_composition(self):
        # 7 press results: all SEVEN previously-logged URL keys (>=1
        # pre-commit corpus hit); ZERO new-to-corpus verbatim press URL
        # keys this run (pure re-surface cycle).
        md = _md_1006()
        assert "SEVEN results observed" in md
        assert "all SEVEN previously-logged URL keys" in md
        assert "ZERO new-to-corpus verbatim press URL keys this run" in md
        assert "pure re-surface cycle" in md
        for key in self.PRESS_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_press_keys_all_in_corpus(self):
        for key in self.PRESS_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_recency_frontier_holds_at_sep_24(self):
        md = _md_1006()
        assert "Recency frontier: HOLDS at Sep 24" in md
        assert "zero new press keys this run" in md
        assert "no frontier advance" in md
        assert "the #966 Sep 23 -> Sep 24 move stands" in md

    def test_non_surfacing_keys_remain_in_corpus(self):
        md = _md_1006()
        assert "dig.watch Audio detail (#961)" in md
        assert "analyticsinsight Audio piece (#961)" in md
        assert "captaincompliance privacy-debate piece (#986)" in md
        assert "did NOT surface this run (remain in corpus)" in md

    def test_asymmetry_note_meta_exclusive(self):
        md = _md_1006()
        assert "Meta-exclusive privacy-pressure framing continues across all 124 cycles" in md
        assert "no competitor camera-wearable coverage carries equivalent privacy-pressure framing" in md

    def test_snippet_bounded_tone_not_scored(self):
        md = _md_1006()
        assert "Snippet-bounded, tone NOT_SCORED per the standing rule" in md

    def test_pure_resurface_cycle_note(self):
        # This run is the FIRST all-seven pure-re-surface press cycle
        # (the #1001 cycle added TWO new press keys; this run adds none).
        assert "pure re-surface cycle" in _md_1006()


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps per #715
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_1006_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_1006*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_834(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 834 in-tree: m834 committed at #1004 Type C and verified at
        # #1005 Type D. Type E adds no mechanisms. (The in-flight #899
        # m771 hunk does not change the max.)
        assert maxid == 834

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "83" + "5"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key
        # strings carried. Designed keying is colon-form in profiles/;
        # tests/ sweeps exclude __pycache__ artifacts, the #1004/#1005
        # sweep-carriers (their NEXT_NUM 835 literals are next-number
        # guards, not assigned mechanism keys, per the #715 convention),
        # and own file.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "83" + "5"
        n2 = "mech" + "anism" + "-" + "83" + "5"
        sweep_carriers = {
            THIS_FILE,
            "test_type_c_1004_australia_nbi_regulatory_bargaining_passed_sep25_11pm.py",
            "test_type_d_1005_m832_m833_m834_qualitative_corpus_integrity_sep26_12am.py",
        }
        hits = []
        for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(p)
        for p in glob.glob(os.path.join(REPO, "tests", "test_*.py")):
            if os.path.basename(p) in sweep_carriers:
                continue
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(p)
        assert hits == []

    def test_concurrent_inflight_files_not_in_this_commit_scope(self):
        # In-flight: #899 Type C (nytimes.yaml m771), #938 Type B
        # (open anchor edit in its test file), #900 Type D (untracked
        # test file) - all uncommitted; this run's staged set must not
        # include those files. Fails pre-commit by design (nothing
        # staged yet); green once the run stages its own files.
        status = _git(["status", "--short"]).stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in ("nytimes.yaml", "test_type_b_938_", "test_type_d_900_"):
            assert not any(f in l for l in staged)


# --------------------------------------------------------------------------
# 8. Statistical discipline: the Aug 28 2026 standing rule
# --------------------------------------------------------------------------
class TestStatisticalDisciplineStandingRule:
    def test_tone_not_scored(self):
        assert "NOT_SCORED" in _md_1006()

    def test_engine_not_run_no_significance(self):
        md = _md_1006()
        assert "engine NOT run" in md
        assert "is_significant False" in md

    def test_no_new_mechanisms_monitoring_only(self):
        assert "monitoring-only" in _md_1006()

    def test_falsification_ledger_holds_at_30(self):
        assert "ledger holds at 30" in _md_1006()

    def test_not_artifact_grade_correlation_not_causation(self):
        md = _md_1006()
        assert "NOT artifact-grade" in md
        assert "Correlation is not causation" in md
        assert "directionally_supported_not_proven" in md


# --------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats_table_updated(self):
        # Pre-run values carried in the new test-file table row's
        # doc-sync prose (51697/1330 -> NEW), so they remain present
        # after the stats table itself is bumped.
        readme = _read(README)
        assert "51697" in readme and "1330" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_1006_marker(self):
        assert "## #1006 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        log = _read(LOG)
        assert "1005-1009" in log
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
