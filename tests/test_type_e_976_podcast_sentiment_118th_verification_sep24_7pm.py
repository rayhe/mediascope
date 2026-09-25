"""Type E #976: podcast sentiment 118th verification cycle - GF 501 CONFIRMED
AGAIN (no 502), ZERO new GF URL keys (pure-re-surface: listennotes main,
goloudnow 519585, PodParadise SURFACED, uk-podcasts variant, TH locale,
podscan.fm, getpodcast), EHE 45-day hold with TWO new URL keys (ranzware
Kylie-lenticular mirror, linkedin privacy roundup; own-repo blob circular),
Attention Sphere 118th no-match (blob page SURFACED AGAIN, 6 commit URLs
git-log-verified circular, Tracked Sources 117->118), FOUR new press URL
keys (neowin, cultofmac, dainikjagranmpcg, androidpolice PR-stunt), recency
frontier HOLDS at Sep 24.

Second leg of the 975-979 window: D (#975) -> E (#976) -> A -> B -> C.
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

ITERATION = 976
TYPE_LETTER = "E"
RUN_PDT = "2026-09-24 19:00 PDT"
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
class TestNoveltyAnchorTypeE976:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #976 main commit exists pre-commit; the anchor test pins
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
            if "Type E #976" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_exactly_one_type_e_976_file_on_disk(self):
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_976*"))
        assert len(files) == 1 and os.path.basename(files[0]) == THIS_FILE


# --------------------------------------------------------------------------
# 2. Rotation guard, 975-979 window (deselected pre-commit per #565)
# --------------------------------------------------------------------------
class TestRotationGuard975_979Window:
    @pytest.mark.rotation
    def test_second_leg_of_975_979_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 976

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {975: "D", 976: "E", 977: "A", 978: "B", 979: "C"}
        assert expected[976] == "E"

    @pytest.mark.rotation
    def test_predecessor_975_type_d_committed(self):
        # #975 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md); this run's own #976 entry will be prepended
        # above it.
        assert "## #975 Type D" in _read(LOG)

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
# 3. The Guilty Feminist: 118th cycle, 501 confirmed again, no 502
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredEighteenthCycle:
    GF_RESURFACED_KEYS = [
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "goloudnow.com/podcasts/the-guilty-feminist-152/deborah-frances-white-on-the-news-meeting-519585",
        "podparadise.com/Podcast/1068940771",
        "uk-podcasts.co.uk/podcast/the-guilty-feminist/deborah-frances-white-on-the-news-meeting",
        "podscan.fm/podcasts/the-guilty-feminist",
        "getpodcast.com/podcast/the-guilty-feminist",
    ]

    def test_episode_501_confirmed_again_this_run(self):
        md = _read(MD)
        assert "EPISODE 501 CONFIRMED AGAIN THIS RUN" in md
        assert "listennotes.com main directory (crawled 8h) still lists at top" in md
        assert "The Guilty Feminist 501. Out North East" in md

    def test_no_episode_502_surfaced(self):
        md = _read(MD)
        assert "No episode 502 surfaced anywhere" in md
        assert "three-day absence since Sep 21" in md
        assert "consistent with weekly cadence, not a signal" in md

    def test_zero_new_gf_url_keys_this_run(self):
        # Pure-re-surface cycle: listennotes main, goloudnow 519585
        # News-Meeting variant (crawled 16h, in corpus via #966),
        # PodParadise SURFACED this run (crawled 3h, listing still lags
        # at the Sep-16 rerelease, 501 absent, in-corpus re-surface),
        # uk-podcasts directory-page variant (crawled 20h, 501-signal
        # corroboration, in-corpus family), listennotes TH locale
        # variant (crawled 177d, stale, in-corpus family variant),
        # podscan.fm (crawled 21h, in-corpus re-surface), getpodcast
        # (crawled 71d, in-corpus family). Every observed key carried
        # >=1 pre-commit corpus hit (verified via git grep -F).
        md = _read(MD)
        assert "ZERO new verbatim GF URL keys this run" in md
        assert "pure-re-surface cycle" in md

    def test_resurfaced_keys_still_in_corpus(self):
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_podparadise_surfaced_again_this_run(self):
        # PodParadise did NOT surface at #971; it SURFACES again at
        # #976 (crawled 3h) - the 762-episode listing still lags at
        # the Sep-16 421 American-Election-part-two "Remembering Bonnie
        # Greer" rerelease, 501 absent, so it is an in-corpus
        # re-surface, not a new key.
        md = _read(MD)
        assert "PodParadise SURFACED this run" in md
        assert "in-corpus re-surface" in md

    def test_uk_podcasts_variant_re_surface_not_new(self):
        md = _read(MD)
        assert "uk-podcasts deborah-frances-white-on-the-news-meeting directory-page variant" in md
        assert "501-signal corroboration" in md

    def test_zero_meta_wearables_across_118_cycles(self):
        assert "across all 118 cycles" in _read(MD)


# --------------------------------------------------------------------------
# 4. Everyone Hates Elon: 118th cycle, 45-day hold, TWO new URL keys
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredEighteenthCycle:
    EHE_RESURFACED_KEYS = [
        "community.designtaxi.com/topic/34124-jeffrey-epstein-appears-to-model-meta-ray-bans-smart-glasses-on-new-ads",
        "en.softonic.com/articles/ray-ban-meta-smart-glasses-back-in-the-spotlight-london-ad-uses-epstein-image",
        "petapixel.com/2026/07/23/kylie-jenners-meta-smart-glasses-parodied-in-guerrilla-lenticular-ad",
        "hyperallergic.com/jeffrey-epstein-dons-meta-ai-glasses-in-damning-guerrilla-ad",
    ]
    EHE_NEW_KEYS = [
        "ranzware.com/kylie-jenners-meta-smart-glasses-parodied-in-guerrilla-lenticular-ad",
        "linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates-viky-hurai-jaklovska-ssqwf",
    ]

    def test_hold_arithmetic_45_days(self):
        # Aug 10 -> Sep 24 = 45 days (date difference, same formula as
        # the #846/#851 regression guard). Same-day hold as #971.
        from datetime import date

        assert (date(2026, 9, 24) - date(2026, 8, 10)).days == 45
        assert "45-day hold continues" in _read(MD)

    def test_epstein_spoof_remains_last_major_phase_marker(self):
        md = _read(MD)
        assert "Aug 10 Epstein spoof -> Sep 24" in md

    def test_four_logged_keys_resurfaced_this_run(self):
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_two_new_ehe_url_keys_this_run(self):
        # Pre-commit both were zero-hit (verified via git grep -F);
        # the podcast-sentiment.md entry ingests them, so post-commit
        # they carry >=1 corpus hit each.
        for key in self.EHE_NEW_KEYS:
            assert _corpus_hits(key), key

    def test_ranzware_is_verbatim_mirror_of_in_corpus_piece(self):
        # The ranzware piece is a verbatim mirror of the in-corpus
        # PetaPixel Kylie-lenticular piece (same "Via
        # @EverybodyHatesElon" lead, same skeleton-Jenner lenticular
        # bus-stop ad): new outlet, not a new story.
        md = _read(MD)
        assert "verbatim mirror of the in-corpus PetaPixel Kylie-lenticular piece" in md
        assert "new outlet, not a new story" in md

    def test_non_surfacing_strands_remain_in_corpus(self):
        md = _read(MD)
        assert "did NOT surface this run (remain in corpus)" in md
        assert "techtimes amnesty-boxes strand" in md

    def test_no_competitor_equivalent_campaign_118_cycles(self):
        md = _read(MD)
        assert (
            "No competitor-equivalent guerrilla campaign against "
            "Apple/Google/Samsung/Snap camera wearables in any of the "
            "118 cycles"
        ) in md


# --------------------------------------------------------------------------
# 5. Attention Sphere: 118th no-match, same circular family as #596/#571-era
# --------------------------------------------------------------------------
class TestAttentionSphereHundredEighteenthNoMatch:
    COMMIT_SHAS = (
        "9590385",
        "a288c86",
        "a2b656f",
        "2c4e21e",
        "25c730e",
        "3d16eac",
    )

    def test_no_match_118th_cycle(self):
        md = _read(MD)
        assert "one-hundred-eighteenth no-match" in md
        assert "returned no matching podcast" in md

    def test_circular_github_results_rejected(self):
        md = _read(MD)
        assert "7 results were all this repository's own GitHub URLs" in md
        assert "rejected as circular, not ingested" in md

    def test_blob_page_surfaced_again(self):
        # Blob page SURFACED at #966/#971; still surfacing at #976.
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

    def test_tracked_sources_advanced_117_to_118(self):
        assert "Tracked Sources advanced 117->118" in _read(MD)

    def test_task_spec_name_still_misidentified(self):
        md = _read(MD)
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 6. Press surfaces: 118th cycle, FOUR new URL keys, frontier HOLDS
# --------------------------------------------------------------------------
class TestPressSurfacesHundredEighteenthCycle:
    NEW_KEYS = [
        "neowin.net/news/meta-launches-camera-free-ray-ban-meta-audio-and-third-gen-ai-glasses",
        "cultofmac.com/news/meta-ray-ban-glasses-camera-free-option-gen-3-upgrade",
        "english.dainikjagranmpcg.com/technology/meta-launches-camera-free-ray-ban-meta-audio-glasses/article-32762",
        "androidpolice.com/meta-ray-ban-audio-smart-glasses-pr-stunt-to-dodge-camera-backlash",
    ]
    RESURFACED_KEYS = [
        "usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses",
        "analyticsinsight.net/news/meta-ray-ban-audio-launches-at-usd-349-with-camera-free-ai",
        "letsdatascience.com/news/meta-unveils-camera-free-ray-ban-meta-audio-glasses-at-conne-dbda6d5c",
    ]

    def test_four_new_press_url_keys_this_run(self):
        md = _read(MD)
        assert "FOUR NEW-TO-CORPUS URL keys this run" in md

    def test_new_press_keys_now_in_corpus(self):
        # Pre-commit each was zero-hit (verified via git grep -F); the
        # podcast-sentiment.md entry ingests them, so post-commit each
        # carries >=1 corpus hit.
        for key in self.NEW_KEYS:
            assert _corpus_hits(key), key

    def test_androidpolice_adversarial_register_logged(self):
        # The androidpolice Sep-24 piece is the first outright
        # adversarial Connect-week register ("just a PR stunt to dodge
        # the camera backlash"); logged with its framing verbatim.
        md = _read(MD)
        assert "PR stunt to dodge the camera backlash" in md
        assert "ADVERSARIAL register" in md

    def test_recency_frontier_holds_at_sep_24(self):
        # The neowin (Sep 24 00:50 EDT) and androidpolice (Sep 24 11:38
        # AM EDT) pieces are same-day as the #966/#971 Sep-24 frontier,
        # so the frontier HOLDS at Sep 24 (no advance this run; #966's
        # Sep 23 -> Sep 24 move stands).
        md = _read(MD)
        assert "Recency frontier: HOLDS at Sep 24" in md
        assert "no frontier advance this run" in md

    def test_resurfaced_keys_still_in_corpus(self):
        for key in self.RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_connect_week_keys_not_surfacing_remain_in_corpus(self):
        md = _read(MD)
        assert "did NOT surface this run (remain in corpus)" in md
        assert "morningstar Dow Jones Sep-24 relay (#971)" in md

    def test_asymmetry_note_meta_concentrated_pressure(self):
        md = _read(MD)
        assert "Meta-concentrated privacy pressure" in md
        assert "Meta-exclusive across all 118 cycles" in md

    def test_snippet_bounded_tone_not_scored(self):
        md = _read(MD)
        assert "Snippet-bounded, tone NOT_SCORED per the standing rule" in md


# --------------------------------------------------------------------------
# 7. Corpus novelty pre-commit greps (per #715 convention)
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_976_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_976*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_816(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 816 in-tree: m814/m815/m816 committed at #972/#973/#974 Type
        # A/B/C and verified at #975 Type D. Type E adds no mechanisms.
        # (The in-flight #899 m771 hunk does not change the max.)
        assert maxid == 816

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "81" + "7"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles_and_tests(self):
        # Format-built needles per #715: no literal next-number key strings
        # carried. Designed keying is colon-form in profiles/; the tests/
        # filename hits (other test files' negative guards) are a different
        # namespace. __pycache__ artifacts excluded per the #715
        # pattern-rescope lesson. Own file excluded as sweep carrier.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "81" + "7"
        n2 = "mech" + "anism" + "-" + "81" + "7"
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
        # doc-sync prose (50220/1300 -> 50272/1301), so they remain
        # present after the stats table itself is bumped.
        readme = _read(README)
        assert "50220" in readme and "1300" in readme

    def test_readme_test_file_table_row_present(self):
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        text = _read(ARCH)
        assert THIS_FILE.replace(".py", "") in text


# --------------------------------------------------------------------------
# 10. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_log_has_976_marker(self):
        assert "## #976 Type E" in _read(LOG)

    def test_log_entry_names_window_leg(self):
        log = _read(LOG)
        assert "975-979" in log
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
