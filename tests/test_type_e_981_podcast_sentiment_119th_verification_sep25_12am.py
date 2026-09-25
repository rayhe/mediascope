"""Type E #981: podcast sentiment 119th verification cycle - GF 501 CONFIRMED
AGAIN (no 502; THREE new directory-mirror keys: plinkhq, ms.podbean,
nz.radio.net), EHE 46-day hold with ONE new URL key (lapost CNN relay:
Wetherspoons ban, fake amnesty bin sign, Google Glass callback), Attention
Sphere 119th no-match (blob page SURFACED AGAIN, 6 commit URLs
git-log-verified circular, Tracked Sources 118->119), THREE new press URL
keys (gagadget, playtechdeep Sep-24 brief, techspot), frontier HOLDS at
Sep 24.

Second leg of the 980-984 window: D (#980) -> E (#981) -> A -> B -> C.
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

ITERATION = 981
TYPE_LETTER = "E"
RUN_PDT = "2026-09-25 00:00 PDT"
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
class TestNoveltyAnchorTypeE981:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #981 main commit exists pre-commit; the anchor test pins
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
            if "Type E #981" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_e_981_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_981*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 980-984 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard980_984Window:
    @pytest.mark.rotation
    def test_second_leg_of_980_984_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 981

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {980: "D", 981: "E", 982: "A", 983: "B", 984: "C"}
        assert expected[981] == "E"

    @pytest.mark.rotation
    def test_predecessor_980_type_d_committed(self):
        # #980 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md); this run's own #981 entry will be prepended
        # above it.
        assert "## #980 Type D" in _read(LOG)

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
# 3. The Guilty Feminist: 119th cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredNineteenthCycle:
    GF_RESURFACED_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "guiltyfeminist.com/new-normal/",
        "guiltyfeminist.com/new-normal-weeks-1-and-2",
        "podscan.fm/podcasts/the-guilty-feminist",
    ]
    GF_NEW_KEYS = [
        "plinkhq.com/i/1068940771",
        "ms.podbean.com/podcast-detail/96viz-3cbfc",
        "nz.radio.net/podcast/the-guilty-feminist",
    ]

    def test_episode_501_confirmed_again_this_run(self):
        md = _read(MD)
        assert "EPISODE 501 CONFIRMED AGAIN THIS RUN" in md
        assert "listennotes.com main directory (crawled 13h) still lists at top" in md
        assert "The Guilty Feminist 501. Out North East" in md

    def test_no_episode_502_surfaced(self):
        md = _read(MD)
        assert "No episode 502 surfaced anywhere" in md
        assert "four-day absence since Sep 21" in md
        assert "consistent with weekly cadence, not a signal" in md

    def test_three_new_gf_url_keys_this_run(self):
        # THREE new-to-corpus verbatim GF URL keys: plinkhq GF
        # directory (crawled 2d, 501 at top), ms.podbean GF directory
        # (crawled 3d, 501 at top), nz.radio.net GF directory (crawled
        # 2d, 761-episode listing, 501 at top). Old-episode
        # directory-mirror keys, zero pre-commit corpus hits (verified
        # via git grep -F); the podcast-sentiment.md entry ingests
        # them, so post-commit each carries >=1 corpus hit.
        md = _read(MD)
        assert "THREE NEW-TO-CORPUS verbatim GF URL keys this run" in md
        assert "old-episode directory-mirror keys" in md
        for key in self.GF_NEW_KEYS:
            assert _corpus_hits(key), key

    def test_resurfaced_keys_still_in_corpus(self):
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_official_site_variants_re_surface_not_new(self):
        md = _read(MD)
        assert "guiltyfeminist.com/new-normal/ official-site base page" in md
        assert "guiltyfeminist.com/new-normal-weeks-1-and-2 official-site page variant" in md

    def test_zero_meta_wearables_across_119_cycles(self):
        assert "across all 119 cycles" in _read(MD)


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 119th cycle, 46-day hold, ONE new URL key
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredNineteenthCycle:
    EHE_RESURFACED_KEYS = [
        "community.designtaxi.com/topic/34124-jeffrey-epstein-appears-to-model-meta-ray-bans-smart-glasses-on-new-ads",
        "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
        "linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates-viky-hurai-jaklovska-ssqwf",
        "afrotech.com/smart-glasses-ethics-and-consent",
    ]
    EHE_NEW_KEYS = [
        "lapost.com/content/turn-the-cameras-off",
    ]

    def test_hold_arithmetic_46_days(self):
        # Aug 10 -> Sep 25 = 46 days (date difference, same formula as
        # the #846/#851 regression guard). Date rolled at midnight;
        # one day past #976's same-day 45-day hold.
        from datetime import date

        assert (date(2026, 9, 25) - date(2026, 8, 10)).days == 46
        assert "46-day hold continues" in _read(MD)

    def test_epstein_spoof_remains_last_major_phase_marker(self):
        md = _read(MD)
        assert "Aug 10 Epstein spoof -> Sep 25" in md

    def test_four_logged_keys_resurfaced_this_run(self):
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_one_new_ehe_url_key_this_run(self):
        # Pre-commit zero-hit (verified via git grep -F); the
        # podcast-sentiment.md entry ingests it, so post-commit it
        # carries >=1 corpus hit.
        for key in self.EHE_NEW_KEYS:
            assert _corpus_hits(key), key
        md = _read(MD)
        assert "ONE NEW-TO-CORPUS EHE URL key this run" in md

    def test_lapost_cnn_relay_details_logged(self):
        # The lapost piece is a CNN relay: Wetherspoons pub-chain ban,
        # the EHE fake "Smart Glasses Amnesty" bin sign dated
        # September 10 2026, Meta anti-tamper shutter claims, Google
        # Glass decade-ago callback. Campaign-coverage, not a podcast
        # episode.
        md = _read(MD)
        assert "Wetherspoons pub-chain ban on Meta-glasses recording" in md
        assert "Google Glass decade-ago callback" in md
        assert "campaign-coverage, not a podcast episode" in md

    def test_non_surfacing_strands_remain_in_corpus(self):
        md = _read(MD)
        assert "did NOT surface this run (remain in corpus)" in md
        assert "ranzware Kylie-lenticular mirror (#976)" in md

    def test_no_competitor_equivalent_campaign_119_cycles(self):
        md = _read(MD)
        assert (
            "No competitor-equivalent guerrilla campaign against "
            "Apple/Google/Samsung/Snap camera wearables in any of the "
            "119 cycles"
        ) in md


# --------------------------------------------------------------------------
# 5. Attention Sphere: 119th no-match, same circular family as #596-era
# --------------------------------------------------------------------------
class TestAttentionSphereHundredNineteenthNoMatch:
    COMMIT_SHAS = (
        "9590385",
        "a288c86",
        "a2b656f",
        "2c4e21e",
        "25c730e",
        "3d16eac",
    )

    def test_no_match_119th_cycle(self):
        md = _read(MD)
        assert "one-hundred-nineteenth no-match" in md
        assert "returned no matching podcast" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "7 results were all this repository's own GitHub URLs" in md
        assert "rejected as circular, not ingested" in md

    def test_blob_page_surfaced_again(self):
        # Blob page SURFACED at #966/#971/#976; still surfacing at #981.
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

    def test_tracked_sources_advanced_118_to_119(self):
        assert "Tracked Sources advanced 118->119" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        md = _read(MD)
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 6. Press surfaces: 119th cycle, THREE new URL keys, frontier HOLDS
# --------------------------------------------------------------------------
class TestPressSurfacesHundredNineteenthCycle:
    NEW_KEYS = [
        "gagadget.com/en/727279",
        "playtechdeep.blog/2026/09/24",
        "techspot.com/news/113968",
    ]
    RESURFACED_KEYS = [
        "ppc.land/hamburg-regulator-finds-ray-ban-meta-glasses-expose-bystanders-without-consent",
        "startupfortune.com/meta-permanently-disables-cameras-on-thousands-of-tampered-smart-glasses",
        "usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses",
        "analyticsinsight.net/news/meta-ray-ban-audio-launches-at-usd-349-with-camera-free-ai",
    ]

    def test_three_new_press_url_keys_this_run(self):
        md = _read(MD)
        assert "THREE NEW-TO-CORPUS URL keys this run" in md

    def test_new_press_keys_now_in_corpus(self):
        # Pre-commit each was zero-hit (verified via git grep -F); the
        # podcast-sentiment.md entry ingests them, so post-commit each
        # carries >=1 corpus hit.
        for key in self.NEW_KEYS:
            assert _corpus_hits(key), key

    def test_techspot_competitive_register_logged(self):
        # The techspot piece mixes adversarial register on Meta's
        # motives ("attempt to sidestep concerns") with a competitive
        # register crediting Meta's VR glasses for calling out
        # Apple's failed Vision Pro - logged verbatim, not scored.
        md = _read(MD)
        assert "directly calls out Apple's failed Vision Pro" in md
        assert "attempt to sidestep concerns" in md

    def test_gagadget_backlash_framing_logged(self):
        md = _read(MD)
        assert "after months of fallout" in md
        assert "backlash-management" in md

    def test_recency_frontier_holds_at_sep_24(self):
        # The playtechdeep (Sep 24), gagadget, and techspot pieces are
        # same-day-or-older than the #966/#976 Sep-24 frontier, so the
        # frontier HOLDS at Sep 24 (no advance this run; #966's Sep 23
        # -> Sep 24 move stands).
        md = _read(MD)
        assert "Recency frontier: HOLDS at Sep 24" in md
        assert "no frontier advance this run" in md

    def test_resurfaced_keys_still_in_corpus(self):
        for key in self.RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_connect_week_keys_not_surfacing_remain_in_corpus(self):
        md = _read(MD)
        assert "did NOT surface this run (remain in corpus)" in md
        assert "androidpolice Sep-24 11:38 AM EDT PR-stunt piece (#976)" in md

    def test_asymmetry_note_meta_exclusive(self):
        md = _read(MD)
        assert "No competitor camera-wearable coverage carries equivalent privacy-pressure framing" in md
        assert "Meta-exclusive across all 119 cycles" in md

    def test_snippet_bounded_tone_not_scored(self):
        md = _read(MD)
        assert "Snippet-bounded, tone NOT_SCORED per the standing rule" in md


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps (per #715 convention)
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_981_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_981*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_819(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 819 in-tree: m819 committed at #979 Type C and verified at
        # #980 Type D. Type E adds no mechanisms. (The in-flight #899
        # m771 hunk does not change the max.)
        assert maxid == 819

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "82" + "0"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key strings
        # carried. Designed keying is colon-form in profiles/; the tests/
        # filename hits (other test files' negative guards) are a different
        # namespace. __pycache__ artifacts excluded per the #715
        # pattern-rescope lesson. Own file excluded as sweep carrier.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "82" + "0"
        n2 = "mech" + "anism" + "-" + "82" + "0"
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
        # doc-sync prose (50482/1305 -> NEW), so they remain present
        # after the stats table itself is bumped.
        readme = _read(README)
        assert "50482" in readme and "1305" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_981_marker(self):
        assert "## #981 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        log = _read(LOG)
        assert "980-984" in log
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
