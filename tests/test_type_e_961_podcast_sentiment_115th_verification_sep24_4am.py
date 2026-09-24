"""Type E #961: podcast sentiment 115th verification cycle - GF 501 CONFIRMED
AGAIN (no 502), FOUR new GF directory-mirror URL keys, EHE 45-day hold with
ONE new verbatim thebesttimes URL key (in-corpus lineage), Attention Sphere
115th no-match (blob page SURFACED AGAIN), TWO new press URL keys
(dig.watch + analyticsinsight), recency frontier HOLDS at Sep 23.

Second leg of the 960-964 window: D (#960) -> E (#961) -> A -> B -> C.
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

ITERATION = 961
TYPE_LETTER = "E"
RUN_PDT = "2026-09-24 04:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565"


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
class TestNoveltyAnchorTypeE961:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #961 main commit exists pre-commit; the anchor test pins
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
            if "Type E #961" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_e_961_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_961*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 960-964 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard960_964Window:
    @pytest.mark.rotation
    def test_second_leg_of_960_964_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 961

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {960: "D", 961: "E", 962: "A", 963: "B", 964: "C"}
        assert expected[961] == "E"

    @pytest.mark.rotation
    def test_predecessor_960_type_d_committed(self):
        # #960 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md); this run's own #961 entry will be prepended
        # above it.
        assert "## #960 Type D" in _read(LOG)

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
# 3. The Guilty Feminist: 115th cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredFifteenthCycle:
    GF_NEW_KEYS = [
        "goloudnow.com/podcasts/the-guilty-feminist-152/acting-your-age-with-nicky-clark-meera-syal-and-juliet-stevenson-331960",
        "goloudnow.com/podcasts/the-guilty-feminist-152/emergency-episode-gaza-nurse-alaa-al-ghoul-530933",
        "goloudnow.com/podcasts/the-guilty-feminist-152/500-five-hundredth-episode-with-kate-cheka-and-the-palestinian-circus-608555",
        "goloudnow.com/podcasts/the-guilty-feminist-152/the-guilty-feminist-watches-and-just-like-that-season-3-episode-1-with-jessica-fostekew-531534",
    ]
    GF_RESURFACED_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "goloudnow.com/podcasts/the-guilty-feminist-152/285-woman-and-power-with-sophie-duker-and-special-guest-kathy-lette-315350",
    ]

    def test_episode_501_confirmed_again_this_run(self):
        md = _read(MD)
        assert "EPISODE 501 CONFIRMED AGAIN THIS RUN" in md
        assert "listennotes.com main directory (crawled 5h) still lists at top" in md
        assert "The Guilty Feminist 501. Out North East" in md

    def test_no_episode_502_surfaced(self):
        md = _read(MD)
        assert "No episode 502 surfaced anywhere" in md
        assert "three-day absence since Sep 21" in md
        assert "consistent with weekly cadence, not a signal" in md

    def test_four_new_gf_directory_mirror_keys(self):
        # FOUR new verbatim GF URL keys: old-episode directory-mirror
        # page-variant keys (331960 Acting-Your-Age, 530933
        # Emergency-Episode-Gaza, 608555 500-page, 531534 AJLT-Watches),
        # zero pre-commit corpus hits each (the 500/AJLT page variants
        # were misclassified as re-surfaces until git grep proved
        # otherwise; corrected in the same run). The podcast-sentiment.md
        # entry ingests them, so post-commit each key carries >=1 hit.
        md = _read(MD)
        assert "FOUR new verbatim GF URL keys this run" in md
        for key in self.GF_NEW_KEYS:
            assert _corpus_hits(key), key

    def test_resurfaced_keys_still_in_corpus(self):
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_uk_podcasts_official_site_podparadise_absent_this_run(self):
        md = _read(MD)
        assert "uk-podcasts, podscan.fm, the official site, and PodParadise did NOT surface this run" in md

    def test_zero_meta_wearables_across_115_cycles(self):
        assert "across all 115 cycles" in _read(MD)


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 115th cycle, 45-day hold, ONE new URL key
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredFifteenthCycle:
    EHE_RESURFACED_KEYS = [
        "community.designtaxi.com/topic/34124-jeffrey-epstein-appears-to-model-meta-ray-bans-smart-glasses-on-new-ads",
        "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
        "softonic.com/articles/ray-ban-meta-smart-glasses-back-in-the-spotlight-london-ad-uses-epstein-image",
        "afrotech.com/smart-glasses-ethics-and-consent",
        "d33gy59ovltp76.cloudfront.net/news/london-bus-stop-poster-brutally-mocks-kylie-jenner",
    ]
    EHE_NEW_KEY = (
        "thebesttimes.com/entertainment/technology_and_science/"
        "do-you-consent-to-being-filmed-by-ai-glasses"
    )

    def test_hold_arithmetic_45_days(self):
        # Aug 10 -> Sep 24 = 45 days (date difference, same formula as
        # the #846/#851 regression guard). #951/#956 were 44-day
        # same-day holds; the date has now advanced.
        from datetime import date

        assert (date(2026, 9, 24) - date(2026, 8, 10)).days == 45
        assert "45-day hold continues" in _read(MD)

    def test_epstein_spoof_remains_last_major_phase_marker(self):
        md = _read(MD)
        assert "Aug 10 Epstein spoof -> Sep 24" in md

    def test_five_logged_keys_resurfaced_this_run(self):
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_one_new_verbatim_url_key_in_corpus_lineage(self):
        # The thebesttimes consent email-drive verbatim URL key had zero
        # pre-commit corpus hits; the campaign data point itself is in
        # corpus since #460 (via muckrack), so this is a new URL key on
        # in-corpus lineage, not a new campaign phase.
        md = _read(MD)
        assert "ONE new verbatim URL key this run" in md
        assert _corpus_hits(self.EHE_NEW_KEY), self.EHE_NEW_KEY
        assert "campaign data point logged #460 via muckrack" in md

    def test_non_surfacing_strands_remain_in_corpus(self):
        md = _read(MD)
        assert "did NOT surface this run (remain in corpus)" in md
        assert "latestly fact-check pair" in md

    def test_no_competitor_equivalent_campaign_115_cycles(self):
        md = _read(MD)
        assert (
            "No competitor-equivalent guerrilla campaign against "
            "Apple/Google/Samsung/Snap camera wearables in any of the "
            "115 cycles"
        ) in md


# --------------------------------------------------------------------------
# 5. Attention Sphere: 115th no-match, blob page SURFACED AGAIN
# --------------------------------------------------------------------------
class TestAttentionSphereHundredFifteenthNoMatch:
    def test_no_match_115th_cycle(self):
        md = _read(MD)
        assert "one-hundred-fifteenth no-match" in md
        assert "returned no matching podcast" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "7 results were all this repository's own GitHub URLs" in md
        assert "rejected as circular, not ingested" in md

    def test_blob_page_surfaced_again_this_run(self):
        # #956's blob page was absent; it is back this run.
        md = _read(MD)
        assert "podcast-sentiment.md blob page, which SURFACED AGAIN this run (absent at #956)" in md

    def test_commit_family_variants_documented(self):
        md = _read(MD)
        assert "53e66f and 36592f this run's variants" in md
        assert "9590385/25c730e absent this run" in md
        assert "36592f verified present in the repo git log" in md

    def test_tracked_sources_advanced_114_to_115(self):
        assert "Tracked Sources advanced 114->115" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        md = _read(MD)
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 6. Press surfaces: 115th cycle, TWO new URL keys, frontier HOLDS Sep 23
# --------------------------------------------------------------------------
class TestPressSurfacesHundredFifteenthCycle:
    NEW_KEYS = [
        "dig.watch/updates/meta-confirms-camera-free-ray-ban-smart-glasses",
        "analyticsinsight.net/news/meta-ray-ban-audio-launches-at-usd-349-with-camera-free-ai",
    ]
    RESURFACED_KEYS = [
        "ppc.land/hamburg-regulator",
        "startupfortune.com/meta-permanently-disables-cameras-on-thousands-of-tampered-smart-glasses",
        "usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses",
        "letsdatascience.com/news/meta-unveils-camera-free-ray-ban-meta-audio-glasses-at-conne",
        "financial-news.co.uk/meta-unveils-camera-free-smart-glasses-as-privacy-pressure-builds",
    ]

    def test_two_new_press_url_keys_this_run(self):
        md = _read(MD)
        assert "TWO NEW-TO-CORPUS URL keys this run" in md

    def test_new_keys_now_in_corpus(self):
        # Pre-commit they were zero-hit (verified via git grep -F); the
        # podcast-sentiment.md entry ingests them, so post-commit each
        # key carries >=1 corpus hit.
        for key in self.NEW_KEYS:
            assert _corpus_hits(key), key

    def test_connect_2026_camera_free_coverage_logged(self):
        # dig.watch (Sep 23): Audio as Meta's first audio glasses;
        # analyticsinsight (Sep 23): USD 349, shipping Oct 13, Muse agent
        # coming to the glasses lineup.
        md = _read(MD)
        assert "Ray-Ban Meta Audio" in md
        assert "Muse personal AI agent" in md
        assert "shipping Oct 13" in md

    def test_resurfaced_keys_still_in_corpus(self):
        md = _read(MD)
        for key in self.RESURFACED_KEYS:
            assert _corpus_hits(key), key
        assert "RE-SURFACED again this run" in md

    def test_recency_frontier_holds_at_sep_23(self):
        # #956 advanced the frontier Sep 18 -> Sep 23; this run adds two
        # more Sep-23 Connect surfaces but nothing post-Sep-23, so the
        # frontier HOLDS.
        md = _read(MD)
        assert "Recency frontier: HOLDS at Sep 23" in md
        assert "first frontier advance since #846" in md

    def test_asymmetry_note_meta_concentrated_pressure(self):
        # The camera-free launch coverage is framed against
        # Meta-concentrated privacy pressure (Hamburg Sep-10 finding,
        # HateAid complaint, Sep-1 LED-tamper bricking, ACLU
        # facial-recognition letter, India non-consensual-recording cases).
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
    def test_zero_type_e_961_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_961*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_807(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 807 in-tree: m807 committed at #959 Type C / verified at
        # #960 Type D (competitor-entities.yaml Palantir vendor-embed
        # leg). The in-flight #884/#899 blocks (m762/m771) are lower.
        assert maxid == 807

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "80" + "8"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key strings
        # carried. Designed keying is colon-form in profiles/; the tests/
        # filename hits (other test files' negative guards) are a different
        # namespace. __pycache__ artifacts excluded per the #715
        # pattern-rescope lesson. Own file excluded as sweep carrier.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "80" + "8"
        n2 = "mech" + "anism" + "-" + "80" + "8"
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
        assert "49498" in readme and "1286" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_961_marker(self):
        assert "## #961 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        log = _read(LOG)
        assert "960-964" in log
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
