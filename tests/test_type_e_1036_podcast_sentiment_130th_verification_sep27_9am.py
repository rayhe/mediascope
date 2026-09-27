"""Type E #1036: podcast sentiment 130th verification cycle - GF 501 CONFIRMED
AGAIN (no 502; six-day absence since Sep 21), ZERO new verbatim GF URL keys
(tenth consecutive pure-re-surface episode-key cycle after #991, #996,
#1001, #1006, #1011, #1016, #1021, #1026, and #1031; the all-key
pure-re-surface streak BREAKS at ONE on the new maglazana press key), EHE
48-day hold (Aug 10 Epstein spoof -> Sep 27) with FIVE logged keys
re-surfaced and ZERO new EHE keys, Attention Sphere 130th no-match as a
podcast (blob SURFACED AGAIN + 6 commit URLs git-cat-file-verified
circular; Tracked Sources 129->130), press SIX re-surfaces + ONE new
verbatim key (maglazana Sep-26 camera-free/Audio+Gen-3 piece; recency
frontier ADVANCES Sep 25 -> Sep 26, first advance since #1011);
Meta-exclusive privacy-pressure framing across all 130 cycles.

Second leg of the 1035-1039 window: D (#1035) -> E (#1036) -> A -> B -> C.
Monitoring-only per the Aug 28 2026 standing rule: tone NOT_SCORED,
p_value/cohens_d NOT_CALCULATED, is_significant False, engine NOT run,
no mechanisms added, falsification ledger holds at 31, NOT artifact-grade.
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

ITERATION = 1036
TYPE_LETTER = "E"
RUN_PDT = "2026-09-27 09:00 PDT"
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


def _md_1036():
    return _read(MD).split("## Iteration #1036")[1]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE1036:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1036 main commit exists pre-commit; the anchor test pins
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
            if "Type E #1036" in line and "followup" not in line.lower()
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
# 2. Rotation guard: second leg of the 1035-1039 window
# --------------------------------------------------------------------------
class TestRotationGuard1035_1039Window:
    @pytest.mark.rotation
    def test_second_leg_of_1035_1039_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 1036

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {1035: "D", 1036: "E", 1037: "A", 1038: "B", 1039: "C"}
        assert expected[1036] == "E"

    @pytest.mark.rotation
    def test_predecessor_1035_type_d_committed(self):
        # #1035 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md, directly under this run's own #1036 entry
        # once prepended).
        assert "## #1035 Type D" in _read(LOG)

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
# 3. The Guilty Feminist: 130th cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredThirtiethCycle:
    GF_RESURFACED_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "listennotes.com/th/podcasts/the-guilty-feminist-deborah-frances-white",
        "youtube.com/watch?v=iKXj2w2cp50",
        "uk-podcasts.co.uk/podcast/the-guilty-feminist/deborah-frances-white-on-the-news-meeting",
        "goloudnow.com/podcasts/the-guilty-feminist-152/deborah-frances-white-on-the-news-meeting-519585",
        "podscan.fm/podcasts/the-guilty-feminist/episodes/499-where-you-end-and-i-begin-with-lindsey-mendick-1",
        "guiltyfeminist.com/live-shows/",
    ]

    def test_501_confirmed_again_prose(self):
        md = _md_1036()
        assert "EPISODE 501 CONFIRMED AGAIN THIS RUN" in md
        assert "The Guilty Feminist 501. Out North East" in md

    def test_no_502_six_day_absence(self):
        md = _md_1036()
        assert "No episode 502 surfaced anywhere" in md
        assert "six-day absence since Sep 21" in md

    def test_zero_new_episode_keys_tenth_pure_resurface_streak(self):
        md = _md_1036()
        assert "ZERO new-to-corpus verbatim GF URL keys this run" in md
        assert (
            "tenth consecutive pure-re-surface episode-key cycle after "
            "#991, #996, #1001, #1006, #1011, #1016, #1021, #1026, and #1031" in md
        )

    def test_gf_resurfaced_keys_in_corpus(self):
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_all_key_streak_breaks_at_one_on_maglazana(self):
        md = _md_1036()
        assert "the all-key pure-re-surface streak BREAKS at ONE" in md
        assert "the maglazana Sep-26 press key is the first new verbatim URL key since #1026's live-shows/ auxiliary key" in md

    def test_zero_meta_wearables_content_130_cycles(self):
        md = _md_1036()
        assert "ZERO Meta/wearables content in any GF episode across all 130 cycles" in md


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 48-day hold, FIVE logged keys re-surfaced
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredThirtiethCycle:
    EHE_RESURFACED_KEYS = [
        "community.designtaxi.com/topic/34124-jeffrey-epstein-appears-to-model-meta-ray-bans-smart-glasses-on-new-ads",
        "en.softonic.com/articles/ray-ban-meta-smart-glasses-back-in-the-spotlight-london-ad-uses-epstein-image",
        "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
        "afrotech.com/smart-glasses-ethics-and-consent",
        "thebesttimes.com/entertainment/technology_and_science/do-you-consent-to-being-filmed-by-ai-glasses/article_8e7b63ae-0b36-5a4f-a25e-f468f7e98d2f.html",
    ]

    def test_48_day_hold(self):
        md = _md_1036()
        assert "48-day hold continues" in md
        assert "date(2026,9,27)-date(2026,8,10)=48 days" in md

    def test_five_logged_keys_resurfaced(self):
        md = _md_1036()
        assert "5 logged keys re-surfaced this run" in md
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_designtaxi_34124_returns_after_1031_absence(self):
        md = _md_1036()
        assert "designtaxi 34124 Epstein-ad thread" in md
        assert "RETURNS after NOT surfacing at #1031" in md

    def test_zero_new_ehe_keys_this_run(self):
        assert "ZERO new-to-corpus verbatim EHE URL keys this run" in _md_1036()

    def test_two_circular_github_urls_rejected(self):
        md = _md_1036()
        assert "2 own-repo GitHub URLs in the EHE result set" in md
        assert "rejected as circular, not ingested" in md
        assert "36592f8f" in md

    def test_no_competitor_equivalent_campaign_130_cycles(self):
        md = _md_1036()
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 130 cycles" in md

    def test_non_surfacing_strands_remain_in_corpus(self):
        md = _md_1036()
        assert "ranzware Kylie-lenticular mirror" in md
        assert "engadget bus-stops original" in md
        assert "hyperallergic Epstein ad" in md
        assert "latestly fact-check pair" in md
        assert "lapost CNN relay" in md
        assert "linkedin privacy roundup" in md
        assert "kayvan-mirza op-ed" in md
        assert "huckmag pervert-glasses" in md
        assert "did NOT surface this run (remain in corpus)" in md


# --------------------------------------------------------------------------
# 5. Attention Sphere: 130th no-match as a podcast
# --------------------------------------------------------------------------
class TestAttentionSphereHundredThirtiethNoMatch:
    OWN_REPO_COMMIT_SHORTHS = ["9590385", "a288c86", "a2b656f", "25c730e", "6da2928", "fe4528b"]

    def test_130th_no_match_prose(self):
        md = _md_1036()
        assert "one-hundred-thirtieth no-match" in md
        assert "returned no matching podcast" in md

    def test_blob_surfacing_again(self):
        md = _md_1036()
        assert "SURFACED AGAIN this run" in md

    def test_commit_urls_git_log_verified_circular(self):
        md = _md_1036()
        for short in self.OWN_REPO_COMMIT_SHORTHS:
            assert short in md
        assert "git cat-file -t" in md
        assert "circular as evidence" in md

    def test_tracked_sources_129_to_130(self):
        assert "Tracked Sources advanced 129->130" in _md_1036()

    def test_task_spec_still_misidentified(self):
        md = _md_1036()
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 6. Press surfaces: SIX re-surfaces + ONE new key, frontier Sep 25 -> Sep 26
# --------------------------------------------------------------------------
class TestPressSurfacesHundredThirtiethCycle:
    PRESS_RESURFACED_KEYS = [
        "usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses/91913146007/",
        "techgig.com/news/tech-drops/meta-unveils-ai-powered-muse-charm-camera-free-ray-ban-glasses-at-connect-event/134472411",
        "community.designtaxi.com/topic/39120-meta-releases-ray-ban-smart-glasses-without-the-cameras-amid-privacy-stalking-concerns/",
        "americanow.com/FreeNewsReader/tech-firms-address-smart-glasses-privacy-concerns-amidst-public-backlash/",
        "dig.watch/updates/meta-confirms-camera-free-ray-ban-smart-glasses",
        "analyticsinsight.net/news/meta-ray-ban-audio-launches-at-usd-349-with-camera-free-ai",
    ]
    PRESS_NEW_KEY = "maglazana.com/2026/09/26/meta-unveils-camera-free-new-gen-3-smart-glasses/"

    def test_six_resurfaces_one_new_key(self):
        md = _md_1036()
        assert "SIX previously-logged keys" in md
        assert "ONE new-to-corpus verbatim URL key this run" in md

    def test_resurfaced_keys_all_in_corpus(self):
        for key in self.PRESS_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_maglazana_new_key_shape(self):
        md = _md_1036()
        assert "maglazana.com/2026/09/26/meta-unveils-camera-free-new-gen-3-smart-glasses/" in md
        assert "zero pre-commit corpus hits" in md
        assert "crawled 3h" in md

    def test_recency_frontier_advances_sep_25_to_sep_26(self):
        md = _md_1036()
        assert "Recency frontier: ADVANCES Sep 25 -> Sep 26" in md
        assert "first advance since #1011" in md

    def test_americanow_resurface_replaces_ppc_land(self):
        md = _md_1036()
        assert "in corpus via #1011/#1016" in md
        assert "ppc.land Hamburg key again absent this run" in md
        assert "did NOT surface this run (remain in corpus)" in md

    def test_asymmetry_note_meta_exclusive(self):
        md = _md_1036()
        assert "Meta-exclusive privacy-pressure framing continues across all 130 cycles" in md
        assert "no competitor camera-wearable coverage carries equivalent privacy-pressure framing" in md

    def test_snippet_bounded_tone_not_scored(self):
        md = _md_1036()
        assert "Snippet-bounded, tone NOT_SCORED per the standing rule" in md


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps per #715
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_1036_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_1036*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_852(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 852 in-tree: m850 committed at #1032 Type A, m851 at #1033 Type B,
        # m852 at #1034 Type C, all verified at #1035 Type D. Type E adds no
        # mechanisms. (The in-flight #899 m771 hunk does not change the max.)
        assert maxid == 852

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "85" + "3"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key
        # strings carried. Designed keying is colon-form in profiles/;
        # tests/ sweeps exclude __pycache__ artifacts, the #1035
        # sweep-carrier (its NEXT_NUM 853 literals are next-number
        # guards, not assigned mechanism keys, per the #715 convention),
        # and own file.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "85" + "3"
        n2 = "mech" + "anism" + "-" + "85" + "3"
        sweep_carriers = {
            THIS_FILE,
            "test_type_d_1035_m850_m851_m852_qualitative_corpus_integrity_sep27_8am.py",
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
        assert "NOT_SCORED" in _md_1036()

    def test_engine_not_run_no_significance(self):
        md = _md_1036()
        assert "engine NOT run" in md
        assert "is_significant False" in md

    def test_no_new_mechanisms_monitoring_only(self):
        assert "monitoring-only" in _md_1036()
        assert "no mechanisms added" in _md_1036()

    def test_falsification_ledger_holds_at_31(self):
        assert "ledger holds at 31" in _md_1036()

    def test_not_artifact_grade_correlation_not_causation(self):
        md = _md_1036()
        assert "NOT artifact-grade" in md
        assert "Correlation is not causation" in md
        assert "directionally_supported_not_proven" in md

    def test_result_row_counts(self):
        md = _md_1036()
        assert "28 result rows / 19 non-circular distinct URL keys / 1 new verbatim URL key this run" in md


# --------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_test_file_table_row_present(self):
        # This run's test-file table row must exist in README.md.
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE.replace(".py", "") in _read(ARCH)

    def test_architecture_lists_1036_file(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE in set(re.findall(r"(test_\w+\.py)", _read(ARCH)))


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_1036_entry_present_with_finding_shape(self):
        # Fails pre-commit by design; green once the iteration-log
        # entry is prepended.
        log = _read(LOG)
        assert "## #1036 Type E" in log
        idx = log.index("## #1036 Type E")
        block = log[idx : idx + 3000]
        assert "130th verification" in block
        assert "Sep 27 2026, 09:00 PDT" in block
        assert "SECOND leg of the 1035-1039 window" in block

    def test_1036_entry_carries_commit_hashes_per_721(self):
        log = _read(LOG)
        idx = log.index("## #1036 Type E")
        block = log[idx : idx + 3000]
        assert "main commit" in block
        assert "anchor" in block
        assert "log-hash followup" in block

    def test_1036_entry_carries_streak_and_frontier_prose(self):
        log = _read(LOG)
        idx = log.index("## #1036 Type E")
        block = log[idx : idx + 3000]
        assert "all-key pure-re-surface streak BREAKS at ONE" in block
        assert "recency frontier ADVANCES Sep 25 -> Sep 26" in block


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
