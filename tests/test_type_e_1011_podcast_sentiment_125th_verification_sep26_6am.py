"""Type E #1011: podcast sentiment 125th verification cycle - GF 501 CONFIRMED
AGAIN (no 502; fifth consecutive pure-re-surface GF cycle, ZERO new GF keys),
EHE 47-day hold with ZERO new URL keys (3 logged keys re-surfaced:
lapost CNN relay, cnn.com Sep-22 original, linkedin privacy roundup),
Attention Sphere 125th no-match (blob page SURFACED AGAIN, 6 commit URLs
git-cat-file-verified circular; Tracked Sources 124->125), press FOUR
NEW-to-corpus URL keys (usatoday Sep-25 Dan Levy 91938905007, americanow
FreeNewsReader, thesun Boz 40496059, medianama 223-meta-ray-ban-audio) +
THREE re-surfaces (gizbot, m1k.tech, dig.watch camera-free); recency
frontier ADVANCES Sep 24 -> Sep 25 (first advance since #966).

Second leg of the 1010-1014 window: D (#1010) -> E (#1011) -> A -> B -> C.
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

ITERATION = 1011
TYPE_LETTER = "E"
RUN_PDT = "2026-09-26 06:00 PDT"
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


def _md_1011():
    return _read(MD).split("## Iteration #1011")[1]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE1011:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1011 main commit exists pre-commit; the anchor test pins
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
            if "Type E #1011" in line and "followup" not in line.lower()
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
# 2. Rotation guard: second leg of the 1010-1014 window
# --------------------------------------------------------------------------
class TestRotationGuard1010_1014Window:
    @pytest.mark.rotation
    def test_second_leg_of_1010_1014_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 1011

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {1010: "D", 1011: "E", 1012: "A", 1013: "B", 1014: "C"}
        assert expected[1011] == "E"

    @pytest.mark.rotation
    def test_predecessor_1010_type_d_committed(self):
        # #1010 Type D is COMMITTED (its log entry sits under this run's
        # own #1011 entry at the head of iteration-log.md).
        assert "## #1010 Type D" in _read(LOG)

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
# 3. The Guilty Feminist: 125th cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredTwentyFifthCycle:
    GF_RESURFACED_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "ca.radio.net/podcast/the-guilty-feminist",
        "plinkhq.com/i/1068940771",
        "ms.podbean.com/podcast-detail/96viz-3cbfc",
    ]

    def test_501_confirmed_again_prose(self):
        md = _md_1011()
        assert "EPISODE 501 CONFIRMED AGAIN THIS RUN" in md
        assert "The Guilty Feminist 501. Out North East" in md

    def test_no_502_six_day_absence(self):
        md = _md_1011()
        assert "No episode 502 surfaced anywhere" in md
        assert "six-day absence since Sep 21" in md

    def test_zero_new_gf_keys_fifth_consecutive_pure_resurface(self):
        md = _md_1011()
        assert "ZERO new-to-corpus verbatim GF URL keys this run" in md
        assert "fifth consecutive pure-re-surface cycle after #991, #996, #1001, and #1006" in md

    def test_gf_resurfaced_keys_in_corpus(self):
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_zero_meta_wearables_content_125_cycles(self):
        md = _md_1011()
        assert "ZERO Meta/wearables content in any GF episode across all 125 cycles" in md


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 47-day hold, zero new keys
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredTwentyFifthCycle:
    EHE_RESURFACED_KEYS = [
        "lapost.com/content/turn-the-cameras-off-london-s-growing-privacy-pushback-against-smart-glasses",
        "cnn.com/2026/09/22/tech/london-privacy-pushback-meta-smart-glasses",
        "linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates-viky-hurai-jaklovska-ssqwf",
    ]

    def test_47_day_hold_same_day(self):
        md = _md_1011()
        assert "47-day hold continues" in md
        assert "date(2026,9,26)-date(2026,8,10)=47 days" in md
        assert "same-day hold" in md

    def test_three_logged_keys_resurfaced(self):
        md = _md_1011()
        assert "3 logged keys re-surfaced this run" in md
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_zero_new_ehe_keys(self):
        md = _md_1011()
        assert "ZERO new verbatim EHE URL keys this run" in md
        assert "no new campaign motif" in md

    def test_four_circular_github_urls_rejected(self):
        md = _md_1011()
        assert "4 own-repo GitHub URLs in the EHE result set" in md
        assert "rejected as circular, not ingested" in md

    def test_no_competitor_equivalent_campaign_125_cycles(self):
        md = _md_1011()
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 125 cycles" in md

    def test_non_surfacing_strands_remain_in_corpus(self):
        md = _md_1011()
        assert "techtimes amnesty-boxes strand" in md
        assert "afrotech ethics/consent piece" in md
        assert "kayvan-mirza linkedin op-ed" in md
        assert "did NOT surface this run (remain in corpus)" in md


# --------------------------------------------------------------------------
# 5. Attention Sphere: 125th no-match as a podcast
# --------------------------------------------------------------------------
class TestAttentionSphereHundredTwentyFifthNoMatch:
    OWN_REPO_COMMIT_SHORTHS = ["9590385", "a288c86", "6da2928", "97a5a5e", "3d16eac", "a2b656f"]

    def test_125th_no_match_prose(self):
        md = _md_1011()
        assert "one-hundred-twenty-fifth no-match" in md
        assert "returned no matching podcast" in md

    def test_blob_surfacing_again(self):
        md = _md_1011()
        assert "SURFACED AGAIN this run" in md

    def test_commit_urls_git_log_verified_circular(self):
        md = _md_1011()
        for short in self.OWN_REPO_COMMIT_SHORTHS:
            assert short in md
        assert "git cat-file -t" in md
        assert "circular as evidence" in md

    def test_tracked_sources_124_to_125(self):
        assert "Tracked Sources advanced 124->125" in _md_1011()

    def test_task_spec_still_misidentified(self):
        md = _md_1011()
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 6. Press surfaces: 4 new + 3 re-surfaces, frontier advances Sep 24 -> Sep 25
# --------------------------------------------------------------------------
class TestPressSurfacesHundredTwentyFifthCycle:
    PRESS_NEW_KEYS = [
        "usatoday.com/story/entertainment/tv-streaming/2026/09/25/dan-levy-slams-smart-glasses-cameras/91938905007/",
        "americanow.com/FreeNewsReader/tech-firms-address-smart-glasses-privacy-concerns-amidst-public-backlash/",
        "thesun.co.uk/tech/40496059/meta-vr-glasses-boz-andrew-bosworth-ray-ban-audio/",
        "medianama.com/2026/09/223-meta-ray-ban-audio-glasses-privacy/",
    ]
    PRESS_RESURFACED_KEYS = [
        "gizbot.com/social-media/news/meta-ray-ban-ai-glasses-update-blocks-cameras-when-recording-light-is-tampered-with-128269.html",
        "m1k.tech/2026/09/meta-ray-ban-led-fix-eu-consent-glasses/",
        "dig.watch/updates/meta-confirms-camera-free-ray-ban-smart-glasses",
    ]

    def test_four_new_to_corpus_keys_composition(self):
        md = _md_1011()
        assert "FOUR new-to-corpus verbatim URL keys" in md
        assert "THREE previously-logged URL keys" in md

    def test_new_keys_in_corpus_post_ingest(self):
        # After this run's md ingestion, the new keys are corpus-known.
        for key in self.PRESS_NEW_KEYS:
            assert _corpus_hits(key), key

    def test_resurfaced_keys_all_in_corpus(self):
        for key in self.PRESS_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_recency_frontier_advances_sep_24_to_sep_25(self):
        md = _md_1011()
        assert "Recency frontier: ADVANCES Sep 24 -> Sep 25" in md
        assert "first advance since #966" in md

    def test_non_surfacing_keys_remain_in_corpus(self):
        md = _md_1011()
        assert "ppc.land Hamburg piece" in md
        assert "startupfortune LED-tamper bricking piece" in md
        assert "designtaxi 39120 camera-free piece" in md
        assert "captaincompliance privacy-debate piece (#986)" in md
        assert "did NOT surface this run (remain in corpus)" in md

    def test_asymmetry_note_meta_exclusive(self):
        md = _md_1011()
        assert "Meta-exclusive privacy-pressure framing continues across all 125 cycles" in md
        assert "no competitor camera-wearable coverage carries equivalent privacy-pressure framing" in md

    def test_snippet_bounded_tone_not_scored(self):
        md = _md_1011()
        assert "Snippet-bounded, tone NOT_SCORED per the standing rule" in md


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps per #715
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_1011_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_1011*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_837(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 837 in-tree: m837 committed at #1009 Type C and verified at
        # #1010 Type D. Type E adds no mechanisms. (The in-flight #899
        # m771 hunk does not change the max.)
        assert maxid == 837

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "83" + "8"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key
        # strings carried. Designed keying is colon-form in profiles/;
        # tests/ sweeps exclude __pycache__ artifacts, the #1009/#1010
        # sweep-carriers (their NEXT_NUM 838 literals are next-number
        # guards, not assigned mechanism keys, per the #715 convention),
        # and own file.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "83" + "8"
        n2 = "mech" + "anism" + "-" + "83" + "8"
        sweep_carriers = {
            THIS_FILE,
            "test_type_c_1009_akamai_anthropic_116b_warrant_demand_for_equity_sep26_4am.py",
            "test_type_d_1010_m835_m836_m837_qualitative_corpus_integrity_sep26_5am.py",
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
        assert "NOT_SCORED" in _md_1011()

    def test_engine_not_run_no_significance(self):
        md = _md_1011()
        assert "engine NOT run" in md
        assert "is_significant False" in md

    def test_no_new_mechanisms_monitoring_only(self):
        assert "monitoring-only" in _md_1011()

    def test_falsification_ledger_holds_at_30(self):
        assert "ledger holds at 30" in _md_1011()

    def test_not_artifact_grade_correlation_not_causation(self):
        md = _md_1011()
        assert "NOT artifact-grade" in md
        assert "Correlation is not causation" in md
        assert "directionally_supported_not_proven" in md

    def test_result_row_counts(self):
        md = _md_1011()
        assert "25 result rows / 14 non-circular distinct URL keys / 4 new verbatim URL keys this run" in md


# --------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats_table_updated(self):
        # Pre-run values carried in the new test-file table row's
        # doc-sync prose (51935/1335 -> NEW), so they remain present
        # after the stats table itself is bumped.
        readme = _read(README)
        assert "51935" in readme and "1335" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_1011_entry_present_with_finding_shape(self):
        log = _read(LOG)
        assert "## #1011 Type E" in log
        idx = log.index("## #1011 Type E")
        block = log[idx : idx + 3000]
        assert "125th verification" in block
        assert "Sep 26 2026, 06:00 PDT" in block
        assert "SECOND leg of the 1010-1014 window" in block

    def test_1011_entry_carries_commit_hashes_per_721(self):
        log = _read(LOG)
        idx = log.index("## #1011 Type E")
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
        # The in-flight #899/#938/#900 working-tree edits are owned by
        # their runs; this run stages only its own files.
        status = _git(["status", "--short"]).stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in ("nytimes.yaml", "test_type_b_938_", "test_type_d_900_"):
            assert not any(f in l for l in staged)
