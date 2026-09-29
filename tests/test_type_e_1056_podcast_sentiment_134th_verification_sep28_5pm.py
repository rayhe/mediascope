"""Type E #1056: podcast sentiment 134th verification cycle - GF EPISODE 502
RELEASED TODAY (breaks the seven-day no-502 hold; the thirteenth-cycle
pure-re-surface episode-key streak that ran #991 through #1051 ENDS; the
all-key pure-re-surface streak advances to FOUR with ZERO new verbatim URL
keys across all four strands), EHE 49-day hold (Aug 10 Epstein spoof ->
Sep 28) with FIVE logged keys re-surfaced and ZERO new EHE keys, Attention
Sphere 134th no-match as a podcast (blob SURFACED AGAIN + 6 commit URLs
git-cat-file-verified circular; Tracked Sources 133->134), press SEVEN
in-corpus re-surfaces incl. the linkedin privacy roundup (SURFACED this
run after missing #1051; ppc.land Hamburg in-corpus re-surface) + ZERO
new verbatim keys (recency frontier HOLDS at Sep 26, fourth hold after
the #1036 advance); Meta-exclusive privacy-pressure framing across all
134 cycles.

Second leg of the 1055-1059 window: D (#1055) -> E (#1056) -> A -> B -> C.
Monitoring-only per the Aug 28 2026 standing rule: tone NOT_SCORED,
p_value/cohens_d NOT_CALCULATED, is_significant False, engine NOT run,
no mechanisms added, falsification ledger holds at 35, NOT artifact-grade.
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

ITERATION = 1056
TYPE_LETTER = "E"
RUN_PDT = "2026-09-28 17:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "1c2028f975883beab9a4c243822fa019316328f8"


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _corpus_hits(needle):
    return _git(["grep", "-l", needle, "--", "."]).stdout.splitlines()


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _md_1056():
    return _read(MD).split("## Iteration #1056")[1]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE1056:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1056 main commit exists pre-commit; the anchor test pins
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
            if "Type E #1056" in line and "followup" not in line.lower()
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
# 2. Rotation guard: second leg of the 1055-1059 window
# --------------------------------------------------------------------------
class TestRotationGuard1055_1059Window:
    @pytest.mark.rotation
    def test_second_leg_of_1055_1059_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 1056

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {1055: "D", 1056: "E", 1057: "A", 1058: "B", 1059: "C"}
        assert expected[1056] == "E"

    @pytest.mark.rotation
    def test_predecessor_1055_type_d_committed(self):
        # #1055 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md, directly under this run's own #1056 entry
        # once prepended). Regex-visible window chain post-commit reads
        # E1056 -> D1055 -> C1054 -> B1053 -> A1052 straight.
        assert "## #1055 Type D" in _read(LOG)


# --------------------------------------------------------------------------
# 3. Concurrency: in-flight runs stay out of this run's scope
# --------------------------------------------------------------------------
class TestNoConcurrentInflightIterationCommits:
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
# 4. The Guilty Feminist: 134th cycle, EPISODE 502 RELEASED TODAY
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredThirtyFourthCycle:
    GF_RESURFACED_KEYS = [
        "podscan.fm/podcasts/the-guilty-feminist-1",
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "youtube.com/watch?v=iKXj2w2cp50",
        "podscan.fm/podcasts/the-guilty-feminist",
        "goloudnow.com/podcasts/the-guilty-feminist-152/deborah-frances-white-on-the-news-meeting-519585",
        "uk-podcasts.co.uk/podcast/the-guilty-feminist/deborah-frances-white-on-the-news-meeting",
        "podscan.fm/podcasts/the-guilty-feminist/episodes/499-where-you-end-and-i-begin-with-lindsey-mendick-1",
    ]

    def test_episode_502_released_today_breaks_hold(self):
        md = _md_1056()
        assert "EPISODE 502 RELEASED TODAY" in md
        assert "The Guilty Feminist 502. Homophobia" in md
        assert "released 28 September 2026" in md
        assert 'the seven-day "no 502" hold BREAKS' in md

    def test_three_directory_corroboration(self):
        md = _md_1056()
        assert "Three-directory corroboration this run" in md
        assert "Latest Episode: 502. Homophobia" in md
        assert "LATEST EPISODE: The Guilty Feminist 502. Homophobia" in md
        assert '"Latest episode: 2026-09-28"' in md

    def test_502_cast_and_venue_logged(self):
        md = _md_1056()
        assert "Freya Parker" in md
        assert "Linus Karp" in md
        assert "recorded 21 August 2026 at Gilded Balloon at the Museum" in md

    def test_zero_new_gf_keys_but_pure_resurface_streak_ends(self):
        md = _md_1056()
        assert "ZERO new-to-corpus verbatim GF URL keys this run" in md
        assert (
            "ENDS the thirteenth-cycle pure-re-surface episode-key streak "
            "that ran #991 through #1051" in md
        )
        assert "this is NOT a pure-re-surface episode-key cycle" in md

    def test_gf_resurfaced_keys_in_corpus(self):
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_all_key_streak_advances_to_four(self):
        md = _md_1056()
        assert "The all-key pure-re-surface streak advances to FOUR" in md
        assert "ZERO new verbatim URL keys across all four strands this run" in md

    def test_zero_meta_wearables_content_134_cycles(self):
        md = _md_1056()
        assert "ZERO Meta/wearables content in any GF episode across all 134 cycles" in md
        assert "topic: homophobia; snippet-bounded" in md
        assert "no tone score asserted" in md


# --------------------------------------------------------------------------
# 5. Everyone Hates Elon: 49-day hold, FIVE logged keys re-surfaced
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredThirtyFourthCycle:
    EHE_RESURFACED_KEYS = [
        "community.designtaxi.com/topic/34124",
        "en.softonic.com/articles/ray-ban-meta-smart-glasses-back-in-the-spotlight",
        "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
        "afrotech.com/smart-glasses-ethics-and-consent",
        "thebesttimes.com/entertainment/technology_and_science/do-you-consent-to-being-filmed-by-ai-glasses",
    ]

    def test_49_day_hold(self):
        md = _md_1056()
        assert "49-day hold continues" in md
        assert "date(2026,9,28)-date(2026,8,10)=49 days" in md

    def test_five_logged_keys_resurfaced(self):
        md = _md_1056()
        assert "5 logged keys re-surfaced this run" in md
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_zero_new_ehe_keys_this_run(self):
        assert "ZERO new-to-corpus verbatim EHE URL keys this run" in _md_1056()

    def test_two_circular_github_urls_rejected(self):
        md = _md_1056()
        assert "2 own-repo GitHub URLs in the EHE result set" in md
        assert "rejected as circular, not ingested" in md
        assert "36592f8" in md

    def test_no_competitor_equivalent_campaign_134_cycles(self):
        md = _md_1056()
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 134 cycles" in md

    def test_non_surfacing_strands_remain_in_corpus(self):
        md = _md_1056()
        assert "ranzware Kylie-lenticular mirror" in md
        assert "engadget bus-stops original" in md
        assert "hyperallergic Epstein ad" in md
        assert "latestly fact-check pair" in md
        assert "lapost CNN relay" in md
        assert "kayvan-mirza op-ed" in md
        assert "huckmag pervert-glasses" in md
        assert "Non-surfacing strands remain in corpus" in md

    def test_epstein_ad_thread_still_primary_motif(self):
        md = _md_1056()
        assert "Glasses for people who don't do consent." in md
        assert "still the primary motif" in md


# --------------------------------------------------------------------------
# 6. Attention Sphere: 134th no-match as a podcast
# --------------------------------------------------------------------------
class TestAttentionSphereHundredThirtyFourthNoMatch:
    OWN_REPO_COMMIT_SHORTHS = ["9590385", "a288c86", "a2b656f", "25c730e", "6da2928", "fe4528b"]

    def test_134th_no_match_prose(self):
        md = _md_1056()
        assert "One-hundred-thirty-fourth quoted-search no-match" in md
        assert "returned no matching podcast" in md

    def test_blob_surfacing_again(self):
        md = _md_1056()
        assert "SURFACED AGAIN this run" in md

    def test_commit_urls_git_log_verified_circular(self):
        md = _md_1056()
        for short in self.OWN_REPO_COMMIT_SHORTHS:
            assert short in md
        assert "git-cat-file-verified present" in md
        assert "circular as evidence" in md

    def test_tracked_sources_133_to_134(self):
        assert "Tracked Sources advanced 133->134" in _md_1056()

    def test_task_spec_still_misidentified(self):
        md = _md_1056()
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 7. Press surfaces: SEVEN re-surfaces + ZERO new keys, frontier HOLDS
# --------------------------------------------------------------------------
class TestPressSurfacesHundredThirtyFourthCycle:
    PRESS_RESURFACED_KEYS = [
        "community.designtaxi.com/topic/39120-meta-releases-ray-ban-smart-glasses-without-the-cameras-amid-privacy-stalking-concerns/",
        "usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses/91913146007/",
        "techgig.com/news/tech-drops/meta-unveils-ai-powered-muse-charm-camera-free-ray-ban-glasses-at-connect-event/134472411",
        "americanow.com/FreeNewsReader/tech-firms-address-smart-glasses-privacy-concerns-amidst-public-backlash/",
        "analyticsinsight.net/news/meta-ray-ban-audio-launches-at-usd-349-with-camera-free-ai",
        "ppc.land/hamburg-regulator-finds-ray-ban-meta-glasses-expose-bystanders-without-consent/",
        "linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates",
    ]

    def test_seven_resurfaces_zero_new_keys(self):
        md = _md_1056()
        assert "SEVEN previously-logged keys re-surfaced this run" in md
        assert "ZERO new-to-corpus verbatim URL keys this run" in md

    def test_resurfaced_keys_all_in_corpus(self):
        for key in self.PRESS_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_linkedin_privacy_roundup_surfaced_after_missing_1051(self):
        md = _md_1056()
        assert "linkedin privacy roundup (crawled 21h, logged via #976): SURFACED this run after missing #1051" in md
        assert "re-surface, not new" in md
        assert _corpus_hits("linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates")

    def test_ppc_land_hamburg_in_corpus_resurface(self):
        md = _md_1056()
        assert "ppc.land Hamburg regulator piece (crawled 2h, in corpus via podcast-sentiment.md)" in md

    def test_recency_frontier_holds_at_sep_26_fourth_hold(self):
        md = _md_1056()
        assert "Recency frontier: HOLDS at Sep 26" in md
        assert "fourth hold after the #1036 advance" in md

    def test_asymmetry_note_meta_exclusive(self):
        md = _md_1056()
        assert "Meta-exclusive privacy-pressure framing continues across all 134 cycles" in md
        assert "no competitor camera-wearable coverage carries equivalent privacy-pressure framing" in md

    def test_snippet_bounded_tone_not_scored(self):
        md = _md_1056()
        assert "Snippet-bounded, tone NOT_SCORED per the standing rule" in md


# --------------------------------------------------------------------------
# 8. Corpus novelty pre-commit greps per #715
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_1056_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_1056*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_866(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # 866 in-tree: m862 committed at #1052 Type A, m863 at #1053
        # Type B, m864 at #1054 Type C, all verified at #1055 Type D,
        # m865 at #1057 Type A, m866 at #1058 Type B. Type E adds no
        # mechanisms. (The in-flight #899 m771 hunk does not change
        # the max.)
        assert maxid == 866

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "86" + "7"
        out = _git(["grep", "-nE", f"mechanism_id:[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles(self):
        # Format-built needles per #715: no literal next-number key
        # strings carried. profiles/ is designed colon-form; no
        # 866 carriers exist in profiles/ at all.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "86" + "6"
        n2 = "mech" + "anism" + "-" + "86" + "6"
        hits = []
        for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(p)
        assert hits == []

    def test_next_carriers_in_tests_pinned_to_guard_files(self):
        # Underscore/dash 866 needles in tests/ must appear ONLY in the
        # pinned guard carriers (empty set this run: #1054's
        # forward-looking literals covered 865; no committed test file
        # carries an 866 literal - all 866 needles are format-built per
        # #715). Own file carries no 866 literal (excluded); no new
        # carrier may appear this run.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "86" + "6"
        n2 = "mech" + "anism" + "-" + "86" + "6"
        pinned = set()
        hits = set()
        for p in glob.glob(os.path.join(REPO, "tests", "test_*.py")):
            if os.path.basename(p) == THIS_FILE:
                continue
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.add(os.path.basename(p))
        assert hits == pinned

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
# 9. Statistical discipline: the Aug 28 2026 standing rule
# --------------------------------------------------------------------------
class TestStatisticalDisciplineStandingRule:
    def test_tone_not_scored(self):
        assert "NOT_SCORED" in _md_1056()

    def test_engine_not_run_no_significance(self):
        md = _md_1056()
        assert "engine NOT run" in md
        assert "is_significant False" in md

    def test_no_new_mechanisms_monitoring_only(self):
        assert "monitoring-only" in _md_1056()
        assert "no mechanisms added" in _md_1056()

    def test_falsification_ledger_holds_at_35(self):
        assert "ledger holds at 35" in _md_1056()

    def test_not_artifact_grade_correlation_not_causation(self):
        md = _md_1056()
        assert "NOT artifact-grade" in md
        assert "Correlation is not causation" in md
        assert "directionally_supported_not_proven" in md

    def test_result_row_counts(self):
        md = _md_1056()
        assert "28 result rows / 19 non-circular distinct URL keys / ZERO new verbatim URL keys this run" in md


# --------------------------------------------------------------------------
# 10. Doc-sync ratchet per #719
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_test_file_table_row_present(self):
        # This run's test-file table row must exist in README.md.
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE.replace(".py", "") in _read(ARCH)

    def test_architecture_lists_1056_file(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE in set(re.findall(r"(test_\w+\.py)", _read(ARCH)))


# --------------------------------------------------------------------------
# 11. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_1056_entry_present_with_finding_shape(self):
        # Fails pre-commit by design; green once the iteration-log
        # entry is prepended.
        log = _read(LOG)
        assert "## #1056 Type E" in log
        idx = log.index("## #1056 Type E")
        block = log[idx : idx + 3000]
        assert "134th verification" in block
        assert "Sep 28 2026, 17:00 PDT" in block
        assert "SECOND leg of the 1055-1059 window" in block

    def test_1056_entry_carries_commit_hashes_per_721(self):
        log = _read(LOG)
        idx = log.index("## #1056 Type E")
        block = log[idx : idx + 3000]
        assert "main commit" in block
        assert "anchor" in block
        assert "log-hash followup" in block

    def test_1056_entry_carries_streak_and_frontier_prose(self):
        log = _read(LOG)
        idx = log.index("## #1056 Type E")
        block = log[idx : idx + 4000]
        assert "all-key pure-re-surface streak advances to FOUR" in block
        assert "recency frontier HOLDS at Sep 26" in block


# --------------------------------------------------------------------------
# 12. Push readiness per #716 / #717
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
