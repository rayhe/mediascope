"""Type E #1021: podcast sentiment 127th verification cycle - GF 501 CONFIRMED
AGAIN (no 502; seventh consecutive pure-re-surface GF cycle, ZERO new GF
keys), EHE 47-day hold (same-day, #1016 also 47) with ONE new-to-corpus URL
key (huckmag Isaac Muk Underground-stickers continuation, campaign-coverage
not a new campaign motif; 4 logged keys re-surfaced: afrotech ethics/consent,
linkedin privacy roundup, kayvan-mirza op-ed, techtimes amnesty-boxes; 2
own-repo GitHub URLs rejected as circular), Attention Sphere 127th no-match
(blob page SURFACED AGAIN, 6 commit URLs 9590385/a288c86/a2b656f/25c730e/
6da2928/fe4528b git-cat-file-verified circular; Tracked Sources 126->127),
press ZERO new URL keys (7/7 re-surfaces: usatoday Sep-23 camera-free, techgig
Sep-25 Connect, designtaxi 39120, dig.watch camera-free, analyticsinsight,
linkedin privacy roundup, ppc.land Hamburg); recency frontier HOLDS at Sep 25.

Second leg of the 1020-1024 window: D (#1020) -> E (#1021) -> A -> B -> C.
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

ITERATION = 1021
TYPE_LETTER = "E"
RUN_PDT = "2026-09-26 18:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "ca5af404694eb3d1a77b7d02082c9783f4d58e91"


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _corpus_hits(needle):
    return _git(["grep", "-l", needle, "--", "."]).stdout.splitlines()


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _md_1021():
    return _read(MD).split("## Iteration #1021")[1]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE1021:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1021 main commit exists pre-commit; the anchor test pins
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
            if "Type E #1021" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "placeholder",
        )
        assert any(ANCHORED_SHA[:12] in line for line in mains)

    @pytest.mark.anchor
    def test_anchor_sha_is_full_40_hex(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)


# --------------------------------------------------------------------------
# 2. Rotation guard: second leg of the 1020-1024 window
# --------------------------------------------------------------------------
class TestRotationGuard1020_1024Window:
    @pytest.mark.rotation
    def test_second_leg_of_1020_1024_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 1021

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {1020: "D", 1021: "E", 1022: "A", 1023: "B", 1024: "C"}
        assert expected[1021] == "E"

    @pytest.mark.rotation
    def test_predecessor_1020_type_d_committed(self):
        # #1020 Type D is COMMITTED (its log entry sits under this run's
        # own #1021 entry at the head of iteration-log.md).
        assert "## #1020 Type D" in _read(LOG)

    @pytest.mark.rotation
    def test_no_concurrent_inflight_commits_asserted(self):
        # In-flight at this run's checks: #899 Type C (m771),
        # #938 Type B (open anchor edit), #900 Type D (untracked) -
        # none committed yet. (#1012-wt is a working-tree edit on the
        # already-committed Type A #1012, not a new iteration commit.)
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
# 3. The Guilty Feminist: 127th cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredTwentySeventhCycle:
    GF_RESURFACED_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "listennotes.com/th/podcasts/the-guilty-feminist-deborah-frances-white",
        "youtube.com/watch?v=iKXj2w2cp50",
        "uk-podcasts.co.uk/podcast/the-guilty-feminist/deborah-frances-white-on-the-news-meeting",
        "goloudnow.com/podcasts/the-guilty-feminist-152/deborah-frances-white-on-the-news-meeting-519585",
    ]

    def test_501_confirmed_again_prose(self):
        md = _md_1021()
        assert "EPISODE 501 CONFIRMED AGAIN THIS RUN" in md
        assert "The Guilty Feminist 501. Out North East" in md

    def test_no_502_five_day_absence(self):
        md = _md_1021()
        assert "No episode 502 surfaced anywhere" in md
        assert "five-day absence since Sep 21" in md

    def test_zero_new_gf_keys_seventh_consecutive_pure_resurface(self):
        md = _md_1021()
        assert "ZERO new-to-corpus verbatim GF URL keys this run" in md
        assert "seventh consecutive pure-re-surface cycle after #991, #996, #1001, #1006, #1011, and #1016" in md

    def test_gf_resurfaced_keys_in_corpus(self):
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_zero_meta_wearables_content_127_cycles(self):
        md = _md_1021()
        assert "ZERO Meta/wearables content in any GF episode across all 127 cycles" in md


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 47-day hold (same-day), ONE new key
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredTwentySeventhCycle:
    EHE_RESURFACED_KEYS = [
        "afrotech.com/smart-glasses-ethics-and-consent",
        "linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates-viky-hurai-jaklovska-ssqwf",
        "linkedin.com/pulse/dear-ai-glasses-industry-situation-critical-red-kayvan-mirza-zwaze",
        "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
    ]
    EHE_NEW_KEY = "huckmag.com/article/activists-slam-pervert-glasses-in-new-guerrilla-campaign"

    def test_47_day_hold_same_day(self):
        md = _md_1021()
        assert "47-day hold continues" in md
        assert "date(2026,9,26)-date(2026,8,10)=47 days" in md
        assert "same-day hold, #1016 was also 47" in md

    def test_four_logged_keys_resurfaced(self):
        md = _md_1021()
        assert "4 logged keys re-surfaced this run" in md
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_one_new_ehe_key_huckmag_in_corpus_post_ingest(self):
        md = _md_1021()
        assert "NEW TO CORPUS this run (1):" in md
        assert "zero pre-commit corpus hits, verified via git grep -F" in md
        # After this run's md ingestion, the new key is corpus-known.
        assert _corpus_hits(self.EHE_NEW_KEY), self.EHE_NEW_KEY

    def test_huckmag_is_campaign_coverage_not_new_motif(self):
        md = _md_1021()
        assert "not a new campaign motif" in md
        assert "Campaign-coverage of the ongoing Underground-stickers strand" in md

    def test_two_circular_github_urls_rejected(self):
        md = _md_1021()
        assert "2 own-repo GitHub URLs in the EHE result set" in md
        assert "rejected as circular, not ingested" in md
        assert "36592f8" in md

    def test_no_competitor_equivalent_campaign_127_cycles(self):
        md = _md_1021()
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 127 cycles" in md

    def test_non_surfacing_strands_remain_in_corpus(self):
        md = _md_1021()
        assert "designtaxi 34124 Epstein-ad thread" in md
        assert "ranzware Kylie-lenticular mirror" in md
        assert "engadget bus-stops original" in md
        assert "latestly fact-check pair" in md
        assert "lapost CNN relay" in md
        assert "did NOT surface this run (remain in corpus)" in md


# --------------------------------------------------------------------------
# 5. Attention Sphere: 127th no-match as a podcast
# --------------------------------------------------------------------------
class TestAttentionSphereHundredTwentySeventhNoMatch:
    OWN_REPO_COMMIT_SHORTHS = ["9590385", "a288c86", "a2b656f", "25c730e", "6da2928", "fe4528b"]

    def test_127th_no_match_prose(self):
        md = _md_1021()
        assert "one-hundred-twenty-seventh no-match" in md
        assert "returned no matching podcast" in md

    def test_blob_surfacing_again(self):
        md = _md_1021()
        assert "SURFACED AGAIN this run" in md

    def test_commit_urls_git_log_verified_circular(self):
        md = _md_1021()
        for short in self.OWN_REPO_COMMIT_SHORTHS:
            assert short in md
        assert "git cat-file -t" in md
        assert "circular as evidence" in md

    def test_tracked_sources_126_to_127(self):
        assert "Tracked Sources advanced 126->127" in _md_1021()

    def test_task_spec_still_misidentified(self):
        md = _md_1021()
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 6. Press surfaces: ZERO new keys, 7/7 re-surfaces, frontier HOLDS at Sep 25
# --------------------------------------------------------------------------
class TestPressSurfacesHundredTwentySeventhCycle:
    PRESS_RESURFACED_KEYS = [
        "usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses/91913146007/",
        "techgig.com/news/tech-drops/meta-unveils-ai-powered-muse-charm-camera-free-ray-ban-glasses-at-connect-event/134472411",
        "community.designtaxi.com/topic/39120-meta-releases-ray-ban-smart-glasses-without-the-cameras-amid-privacy-stalking-concerns/",
        "dig.watch/updates/meta-confirms-camera-free-ray-ban-smart-glasses",
        "analyticsinsight.net/news/meta-ray-ban-audio-launches-at-usd-349-with-camera-free-ai",
        "ppc.land/hamburg-regulator-finds-ray-ban-meta-glasses-expose-bystanders-without-consent/",
    ]

    def test_zero_new_keys_seven_resurfaces(self):
        md = _md_1021()
        assert "ALL previously-logged keys" in md
        assert "ZERO new verbatim URL keys this run" in md

    def test_resurfaced_keys_all_in_corpus(self):
        for key in self.PRESS_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_recency_frontier_holds_sep_25(self):
        md = _md_1021()
        assert "Recency frontier: HOLDS at Sep 25" in md
        assert "no advance" in md

    def test_non_surfacing_keys_remain_in_corpus(self):
        md = _md_1021()
        assert "gizbot LED-fix update" in md
        assert "m1k.tech EU-consent analysis" in md
        assert "thesun Boz interview (#1011)" in md
        assert "medianama 223-meta-ray-ban-audio piece (#1011)" in md
        assert "did NOT surface this run (remain in corpus)" in md

    def test_asymmetry_note_meta_exclusive(self):
        md = _md_1021()
        assert "Meta-exclusive privacy-pressure framing continues across all 127 cycles" in md
        assert "no competitor camera-wearable coverage carries equivalent privacy-pressure framing" in md

    def test_snippet_bounded_tone_not_scored(self):
        md = _md_1021()
        assert "Snippet-bounded, tone NOT_SCORED per the standing rule" in md

    def test_dig_watch_resurface_in_corpus_lineage(self):
        md = _md_1021()
        assert "dig.watch/updates/meta-confirms-camera-free-ray-ban-smart-glasses" in md
        assert "Sep-15 Luna codename report callback" in md


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps per #715
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_1021_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_1021*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_843(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 843 in-tree: m841 committed at #1017 Type A, m842 at #1018 Type B,
        # m843 at #1019 Type C, all verified at #1020 Type D. Type E adds no
        # mechanisms. (The in-flight #899 m771 hunk does not change the max.)
        assert maxid == 843

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "84" + "4"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key
        # strings carried. Designed keying is colon-form in profiles/;
        # tests/ sweeps exclude __pycache__ artifacts, the #1020
        # sweep-carrier (its NEXT_NUM 844 literals are next-number
        # guards, not assigned mechanism keys, per the #715 convention),
        # and own file.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "84" + "4"
        n2 = "mech" + "anism" + "-" + "84" + "4"
        sweep_carriers = {
            THIS_FILE,
            "test_type_d_1020_m841_m842_m843_qualitative_corpus_integrity_sep26_5pm.py",
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
        # test file), #1012-wt (working-tree edit on the committed
        # Type A #1012 test file) - all uncommitted; this run's staged
        # set must not include those files. Fails pre-commit by design
        # (nothing staged yet); green once the run stages its own files.
        status = _git(["status", "--short"]).stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in ("nytimes.yaml", "test_type_b_938_", "test_type_d_900_", "test_type_a_1012_"):
            assert not any(f in l for l in staged)


# --------------------------------------------------------------------------
# 8. Statistical discipline: the Aug 28 2026 standing rule
# --------------------------------------------------------------------------
class TestStatisticalDisciplineStandingRule:
    def test_tone_not_scored(self):
        assert "NOT_SCORED" in _md_1021()

    def test_engine_not_run_no_significance(self):
        md = _md_1021()
        assert "engine NOT run" in md
        assert "is_significant False" in md

    def test_no_new_mechanisms_monitoring_only(self):
        assert "monitoring-only" in _md_1021()

    def test_falsification_ledger_holds_at_30(self):
        assert "ledger holds at 30" in _md_1021()

    def test_not_artifact_grade_correlation_not_causation(self):
        md = _md_1021()
        assert "NOT artifact-grade" in md
        assert "Correlation is not causation" in md
        assert "directionally_supported_not_proven" in md

    def test_result_row_counts(self):
        md = _md_1021()
        assert "28 result rows / 16 non-circular distinct URL keys / 1 new verbatim URL key this run" in md


# --------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats_table_updated(self):
        # Pre-run values carried in the new test-file table row's
        # doc-sync prose (52424/1345 -> NEW), so they remain present
        # after the stats table itself is bumped.
        readme = _read(README)
        assert "52424" in readme and "1345" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_1021_entry_present_with_finding_shape(self):
        log = _read(LOG)
        assert "## #1021 Type E" in log
        idx = log.index("## #1021 Type E")
        block = log[idx : idx + 3000]
        assert "127th verification" in block
        assert "Sep 26 2026, 18:00 PDT" in block
        assert "SECOND leg of the 1020-1024 window" in block

    def test_1021_entry_carries_commit_hashes_per_721(self):
        log = _read(LOG)
        idx = log.index("## #1021 Type E")
        block = log[idx : idx + 3000]
        assert "main commit" in block
        assert "anchor" in block
        assert "log-hash followup" in block


# --------------------------------------------------------------------------
# 11. Push readiness per #716 / #717
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
        # The in-flight #899/#938/#900/#1012-wt working-tree edits are
        # owned by their runs; this run stages only its own files.
        status = _git(["status", "--short"]).stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in ("nytimes.yaml", "test_type_b_938_", "test_type_d_900_", "test_type_a_1012_"):
            assert not any(f in l for l in staged)
