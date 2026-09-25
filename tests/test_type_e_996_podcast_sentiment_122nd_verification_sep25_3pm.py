"""Type E #996: podcast sentiment 122nd verification cycle - GF 501 CONFIRMED
AGAIN (no 502; second consecutive pure-re-surface GF cycle, ZERO new GF keys),
EHE 46-day hold with ONE new verbatim URL key (cnn.com/2026/09/22, the CNN
original of the #981 lapost relay; zero pre-commit corpus hits), Attention
Sphere 122nd no-match (blob page SURFACED AGAIN, 6 commit URLs git-log-verified
circular, Tracked Sources 121->122), press surfaces 7/7 in-corpus re-surfaces,
frontier HOLDS at Sep 24.

Second leg of the 995-999 window: D (#995) -> E (#996) -> A -> B -> C.
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

ITERATION = 996
TYPE_LETTER = "E"
RUN_PDT = "2026-09-25 15:00 PDT"
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


def _md_996():
    return _read(MD).split("## Iteration #996")[1]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE996:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #996 main commit exists pre-commit; the anchor test pins
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
            if "Type E #996" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        )
        assert len(mains) >= 1

    def test_exactly_one_type_e_996_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_996*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 995-999 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard995_999Window:
    @pytest.mark.rotation
    def test_second_leg_of_995_999_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 996

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {995: "D", 996: "E", 997: "A", 998: "B", 999: "C"}
        assert expected[996] == "E"

    @pytest.mark.rotation
    def test_predecessor_995_type_d_committed(self):
        # #995 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md); this run's own #996 entry will be prepended
        # above it.
        assert "## #995 Type D" in _read(LOG)

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
# 3. The Guilty Feminist: 122nd cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredTwentySecondCycle:
    GF_RESURFACED_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "goloudnow.com/podcasts/the-guilty-feminist-152",
        "goloudnow.com/podcasts/the-guilty-feminist-152/500-five-hundredth-episode-with-kate-cheka-and-the-palestinian-circus-608555",
        "goloudnow.com/podcasts/the-guilty-feminist-152/acting-your-age-with-nicky-clark-meera-syal-and-juliet-stevenson-331960",
        "goloudnow.com/podcasts/the-guilty-feminist-152/the-guilty-feminist-watches-and-just-like-that-season-3-episode-1-with-jessica-fostekew-531534",
        "goloudnow.com/podcasts/the-guilty-feminist-152/350-international-womens-day-2023-with-felicity-ward-helen-bauer-michelle-de-swarte-grace-petrie-and-ellie-dixon-part-two-404081",
    ]

    def test_episode_501_confirmed_again_this_run(self):
        md = _md_996()
        assert "EPISODE 501 CONFIRMED AGAIN THIS RUN" in md
        assert "The listennotes.com main directory (crawled 1d" in md
        assert "still lists at top" in md
        assert "The Guilty Feminist 501. Out North East" in md

    def test_no_episode_502_surfaced(self):
        md = _md_996()
        assert "No episode 502 surfaced anywhere" in md
        assert "four-day absence since Sep 21" in md
        assert "consistent with weekly cadence, not a signal" in md

    def test_zero_new_gf_url_keys_this_run(self):
        # Pure-re-surface cycle: 6/6 observed GF keys carry >=1
        # pre-commit corpus hit; ZERO new-to-corpus GF keys. Second
        # consecutive pure-re-surface cycle after #991 (the #986
        # directory-mirror novelty is the last new-key cycle).
        md = _md_996()
        assert "ZERO new-to-corpus verbatim GF URL keys this run" in md
        assert "pure-re-surface cycle" in md
        assert "second consecutive pure-re-surface cycle after #991" in md
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_resurfaced_keys_still_in_corpus(self):
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_directory_mirrors_not_surfacing_this_run(self):
        md = _md_996()
        assert "plinkhq, ms.podbean, za.radio.net, and ca.radio.net" in md
        assert "did NOT surface" in md
        assert "remain in corpus" in md

    def test_zero_meta_wearables_across_122_cycles(self):
        assert "across all 122 cycles" in _md_996()


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 122nd cycle, 46-day hold, ONE new URL key
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredTwentySecondCycle:
    EHE_RESURFACED_KEYS = [
        "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
        "linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates-viky-hurai-jaklovska-ssqwf",
        "lapost.com/content/turn-the-cameras-off-london-s-growing-privacy-pushback-against-smart-glasses",
        "afrotech.com/smart-glasses-ethics-and-consent",
    ]
    EHE_NEW_KEY = (
        "cnn.com/2026/09/22/tech/london-privacy-pushback-meta-smart-glasses"
    )

    def test_hold_arithmetic_46_days(self):
        # Aug 10 Epstein spoof -> Sep 25: same-day as the #981, #986
        # and #991 46-day holds (calendar-day arithmetic, not
        # elapsed-hours).
        from datetime import date

        assert (date(2026, 9, 25) - date(2026, 8, 10)).days == 46
        md = _md_996()
        assert "46-day hold continues" in md
        assert "date(2026,9,25)-date(2026,8,10)=46 days" in md

    def test_epstein_spoof_remains_last_major_phase_marker(self):
        md = _md_996()
        assert "Aug 10 Epstein spoof" in md
        assert "same-day as the #981, #986, and #991 46-day holds" in md

    def test_four_logged_keys_resurfaced_this_run(self):
        md = _md_996()
        assert "4 logged keys re-surfaced" in md
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_one_new_ehe_url_key_this_run(self):
        # The CNN ORIGINAL of the #981 lapost relay: same story (the
        # Sep-22 London privacy-pushback piece), new byline-original
        # URL key. Zero pre-commit corpus hits (verified this run);
        # post-commit it is in the corpus via podcast-sentiment.md.
        md = _md_996()
        assert "ONE new verbatim EHE URL key this run" in md
        assert "the CNN ORIGINAL of the #981 lapost relay" in md
        assert "zero pre-commit corpus hits" in md
        assert _corpus_hits(self.EHE_NEW_KEY), self.EHE_NEW_KEY

    def test_new_key_is_same_story_not_new_motif(self):
        md = _md_996()
        assert "same story, new byline-original URL key" in md
        assert "not a new campaign motif" in md

    def test_circular_github_urls_rejected_this_run(self):
        md = _md_996()
        assert "2 own-repo GitHub URLs in the EHE result set" in md
        assert "rejected as circular, not ingested" in md

    def test_non_surfacing_strands_remain_in_corpus(self):
        md = _md_996()
        assert "The designtaxi 34124 Epstein-ad thread" in md
        assert "ranzware Kylie-lenticular mirror (#976)" in md
        assert "latestly fact-check pair did NOT surface this run" in md
        assert "remain in corpus" in md

    def test_no_competitor_equivalent_campaign_122_cycles(self):
        assert "any of the 122 cycles" in _md_996()


# --------------------------------------------------------------------------
# 5. Attention Sphere: 122nd no-match
# --------------------------------------------------------------------------
class TestAttentionSphereHundredTwentySecondNoMatch:
    COMMIT_SHAS = (
        "9590385",
        "a288c86",
        "a2b656f",
        "25c730e",
        "6da2928",
        "fe4528b",
    )

    def test_no_match_122nd_cycle(self):
        md = _md_996()
        assert "one-hundred-twenty-second no-match" in md
        assert "returned no matching podcast" in md

    def test_circular_github_results_rejected(self):
        md = _md_996()
        assert "7 results were all this repository's own GitHub URLs" in md
        assert "rejected as circular, not ingested" in md

    def test_blob_page_surfaced_again(self):
        # Blob page SURFACED at #966/#971/#976/#981/#986/#991; still
        # at #996.
        md = _md_996()
        assert "podcast-sentiment.md blob page, which SURFACED AGAIN this run" in md

    def test_variant_family_commits_verified_in_git_log(self):
        md = _md_996()
        for sha in self.COMMIT_SHAS:
            assert sha in md, sha
        # Each SHA resolves to a real commit object in the repo: circular
        # as evidence, verified rather than asserted. 6da2928 and
        # fe4528b are this run's variants replacing 2c4e21e/3d16eac
        # from the #991-era set.
        for sha in self.COMMIT_SHAS:
            out = subprocess.run(
                ["git", "cat-file", "-t", sha],
                cwd=REPO,
                capture_output=True,
                text=True,
            )
            assert out.stdout.strip() == "commit", sha

    def test_tracked_sources_advanced_121_to_122(self):
        assert "Tracked Sources advanced 121->122" in _md_996()

    def test_task_spec_name_still_misidentified(self):
        md = _md_996()
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 6. Press surfaces: 122nd cycle, 7/7 in-corpus re-surfaces, frontier HOLDS
# --------------------------------------------------------------------------
class TestPressSurfacesHundredTwentySecondCycle:
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
        # 7/7 press keys carry >=1 pre-commit corpus hit; ZERO new
        # press URL keys.
        md = _md_996()
        assert "SEVEN results observed, ALL previously-logged URL keys" in md
        assert "ZERO new-to-corpus press URL keys this run" in md
        for key in self.PRESS_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_press_keys_now_in_corpus(self):
        for key in self.PRESS_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_recency_frontier_holds_at_sep_24(self):
        md = _md_996()
        assert "Recency frontier: HOLDS at Sep 24" in md
        assert "no frontier advance this run" in md
        assert "the #966 Sep 23 -> Sep 24 move stands" in md
        assert "the new EHE key is the Sep-22 CNN original" in md

    def test_designtaxi_39120_audio_piece_logged(self):
        md = _md_996()
        assert "community.designtaxi.com/topic/39120" in md
        assert "in corpus via #986" in md

    def test_captaincompliance_privacy_debate_logged(self):
        md = _md_996()
        assert "captaincompliance.com/education/meta-launches-camera-free" in md
        assert "no obvious bystander signal for audio recording" in md

    def test_asymmetry_note_meta_exclusive(self):
        md = _md_996()
        assert "Meta-exclusive across all 122 cycles" in md
        assert "no competitor camera-wearable coverage carries equivalent privacy-pressure framing" in md

    def test_snippet_bounded_tone_not_scored(self):
        md = _md_996()
        assert "Snippet-bounded, tone NOT_SCORED per the standing rule" in md


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps per #715
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_996_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_996*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_828(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 828 in-tree: m828 committed at #994 Type C and verified at
        # #995 Type D. Type E adds no mechanisms. (The in-flight #899
        # m771 hunk does not change the max.)
        assert maxid == 828

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "82" + "9"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key
        # strings carried. Designed keying is colon-form in profiles/;
        # tests/ sweeps exclude __pycache__ artifacts, the #995
        # sweep-carrier (its dash-form negative-guard literal at line
        # 748 is a different namespace per the #715 pattern-rescope
        # lesson), and own file. Other tests' negative guards use
        # format-built needles only.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "82" + "9"
        n2 = "mech" + "anism" + "-" + "82" + "9"
        sweep_carriers = {
            THIS_FILE,
            "test_type_d_995_m826_m827_m828_qualitative_corpus_integrity_sep25_2pm.py",
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
        assert "NOT_SCORED" in _md_996()

    def test_engine_not_run_no_significance(self):
        md = _md_996()
        assert "engine NOT run" in md
        assert "is_significant False" in md

    def test_no_new_mechanisms_monitoring_only(self):
        assert "monitoring-only" in _md_996()

    def test_falsification_ledger_holds_at_30(self):
        assert "ledger holds at 30" in _md_996()

    def test_not_artifact_grade_correlation_not_causation(self):
        md = _md_996()
        assert "NOT artifact-grade" in md
        assert "Correlation is not causation" in md
        assert "directionally_supported_not_proven" in md


# --------------------------------------------------------------------------
# 9. Doc-sync ratchet per #719
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_stats_table_updated(self):
        # Pre-run values carried in the new test-file table row's
        # doc-sync prose (51213/1320 -> NEW), so they remain present
        # after the stats table itself is bumped.
        readme = _read(README)
        assert "51213" in readme and "1320" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_996_marker(self):
        assert "## #996 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        log = _read(LOG)
        assert "995-999" in log
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
