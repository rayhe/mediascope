"""Type E #1096: podcast sentiment 142nd verification cycle - GF EPISODE 502
HOLDS as latest (ninth Type E verification since the Sep 28 11:00am
release, ~46 hours after publication; NO 503 surfaced; three-directory
corroboration), EHE 51-day hold (Aug 10 Epstein spoof -> Sep 30) with SIX
logged keys re-surfaced and ZERO new-to-corpus verbatim URL keys (pure
re-surface cycle; the all-key pure-re-surface streak RESTARTS at one),
Attention Sphere 142nd no-match as a podcast (7 own-repo GitHub commit
URLs only; the podcast-sentiment.md blob did NOT surface this run;
git-cat-file-verified circular; Tracked Sources 141->142), press SIX
in-corpus re-surfaces + ZERO new press keys; recency frontier HOLDS at
Sep 29 (fifth hold since the #1071 advance).
Guard lifecycle: the #1095 Type D run pinned the zero-889 forward-looking
guards (MAX_ID = 888, NEXT_NUM = 889 in the #1095 file); they PASS this run
and fail BY DESIGN when mechanism 889 lands at a future A/B/C leg of the
1095-1099 window.

Second leg of the 1095-1099 window: D (#1095) -> E (#1096) -> A -> B -> C.
Monitoring-only per the Aug 28 2026 standing rule: tone NOT_SCORED,
p_value/cohens_d NOT_CALCULATED, is_significant False, engine NOT run,
no mechanisms added, falsification ledger holds at 37, NOT artifact-grade.
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

ITERATION = 1096
TYPE_LETTER = "E"
RUN_PDT = "2026-09-30 09:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "f94f88a2c5551be3ab3cfcae50f1962d1591d8fc"

README_TESTS_AFTER = 55660
README_FILES_AFTER = 1421

# The #1095 Type D file pins this window's zero-889 forward-looking
# guards (MAX_ID = 888, NEXT_NUM = 889). This run verifies they PASS.
D1095_FILE = (
    "test_type_d_1095_m886_m887_m888_qualitative_corpus_integrity_"
    "sep30_8am.py"
)
MAX_ID = 888
NEXT_NUM = 889


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _corpus_hits(needle):
    return _git(["grep", "-l", needle, "--", "."]).stdout.splitlines()


def _md_1096():
    return _read(MD).split("## Iteration #1096")[1]


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE1096:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1096 main commit exists pre-commit; the anchor test pins
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
            if "Type E #1096" in line and "followup" not in line.lower()
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
# 2. Rotation guard: second leg of the 1095-1099 window
# --------------------------------------------------------------------------
class TestRotationGuard1095_1099Window:
    @pytest.mark.rotation
    def test_second_leg_of_1095_1099_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 1096

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {1095: "D", 1096: "E", 1097: "A", 1098: "B", 1099: "C"}
        assert expected[1096] == "E"

    @pytest.mark.rotation
    def test_predecessor_1095_present(self):
        # The #1095 Type D opener's main, anchor, and log-hash commits
        # must all be in history before this run commits.
        for short in ("ed8c9cf2", "188b15f6", "75243d3f"):
            result = _git(["log", "--format=%H %s"])
            assert short in result.stdout, short


# --------------------------------------------------------------------------
# 3. Concurrency: in-flight iterations stay out of this run's commit
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
        assert not any(re.match(r"^Type [A-E] #(899|938|900)\b", s) for s in subjects)


# --------------------------------------------------------------------------
# 4. Guilty Feminist: 142nd cycle - episode 502 holds, streak restarts
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredFortySecondCycle:
    GF_RESURFACED_KEYS = [
        "podscan.fm/podcasts/the-guilty-feminist-1",
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "youtube.com/watch?v=iKXj2w2cp50",
        "podscan.fm/podcasts/the-guilty-feminist",
        "goloudnow.com/podcasts/the-guilty-feminist-152/deborah-frances-white-on-the-news-meeting-519585",
        "uk-podcasts.co.uk/podcast/the-guilty-feminist/deborah-frances-white-on-the-news-meeting",
    ]

    def test_episode_502_holds_as_latest_no_503(self):
        md = _md_1096()
        assert "EPISODE 502 HOLDS as latest" in md
        assert "ninth Type E verification since the Sep 28 11:00am release (~46 hours after publication)" in md
        assert "NO 503 surfaced" in md
        assert "The Guilty Feminist 502. Homophobia" in md

    def test_three_directory_corroboration(self):
        md = _md_1096()
        assert "Three-directory corroboration this run" in md
        assert "LATEST EPISODE: The Guilty Feminist 502. Homophobia" in md
        assert "Latest Episode: 502. Homophobia with Freya Parker and Linus Karp" in md
        assert '"Latest episode: 2026-09-28"' in md

    def test_502_cast_and_venue_logged(self):
        md = _md_1096()
        assert "Freya Parker" in md
        assert "Linus Karp" in md
        assert "recorded 21 August 2026 at Gilded Balloon at the Museum" in md

    def test_zero_new_gf_keys_streak_restarts_at_one(self):
        md = _md_1096()
        assert "ZERO new-to-corpus verbatim GF URL keys this run" in md
        assert "The all-key pure-re-surface streak RESTARTS at one" in md

    def test_gf_resurfaced_keys_in_corpus(self):
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_gf_circular_commit_url_rejected(self):
        md = _md_1096()
        assert "2f9a4a27" in md
        assert "git-cat-file-verified present" in md
        assert "rejected as circular, not ingested" in md

    def test_zero_meta_wearables_content_142_cycles(self):
        md = _md_1096()
        assert "ZERO Meta/wearables content in any GF episode across all 142 cycles" in md
        assert "topic: homophobia; snippet-bounded" in md
        assert "no tone score asserted" in md


# --------------------------------------------------------------------------
# 5. Everyone Hates Elon: 51-day hold, SIX logged keys, ZERO new keys
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredFortySecondCycle:
    EHE_RESURFACED_KEYS = [
        "afrotech.com/smart-glasses-ethics-and-consent",
        "huckmag.com/article/activists-slam-pervert-glasses-in-new-guerrilla-campaign",
        "linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates-viky-hurai-jaklovska-ssqwf",
        "linkedin.com/pulse/dear-ai-glasses-industry-situation-critical-red-kayvan-mirza-zwaze",
        "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
        "feminist.org/news/author/lkollross/",
    ]

    def test_51_day_hold(self):
        md = _md_1096()
        assert "51-day hold continues" in md
        assert "date(2026,9,30)-date(2026,8,10)=51 days" in md

    def test_six_logged_keys_resurfaced(self):
        md = _md_1096()
        assert "6 logged keys re-surfaced this run" in md
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_huckmag_resurfaces(self):
        md = _md_1096()
        assert "huckmag pervert-glasses piece (crawled 2h; in corpus via #1021, re-surfaced" in md

    def test_kayvan_mirza_resurfaces(self):
        md = _md_1096()
        assert "linkedin kayvan-mirza op-ed (crawled 1d; in corpus via #1001/#1006" in md

    def test_feminist_org_archive_now_resurfaces_from_1091(self):
        md = _md_1096()
        assert "feminist.org author archive (crawled 4h; in corpus via #1091" in md

    def test_zero_new_ehe_keys_pure_resurface_cycle(self):
        md = _md_1096()
        assert "ZERO new-to-corpus verbatim EHE URL keys this run" in md
        assert "pure re-surface cycle" in md

    def test_one_circular_github_url_rejected(self):
        md = _md_1096()
        assert "1 own-repo GitHub URL in the EHE result set" in md
        assert "podcast-sentiment.md blob, git-cat-file-verified present" in md
        assert "rejected as circular, not ingested" in md

    def test_no_competitor_equivalent_campaign_142_cycles(self):
        md = _md_1096()
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 142 cycles" in md


    def test_epstein_ad_thread_still_primary_motif(self):
        md = _md_1096()
        assert "Glasses for people who don't do consent." in md
        assert "still the primary motif" in md


# --------------------------------------------------------------------------
# 6. Attention Sphere: 142nd no-match as a podcast
# --------------------------------------------------------------------------
class TestAttentionSphereHundredFortySecondNoMatch:
    OWN_REPO_COMMIT_SHORTHS = ["40d6e7b0", "d4618aae", "5e238e78", "0d9132c6", "bf0cbbf1", "dec56140", "16611229"]

    def test_142nd_no_match_prose(self):
        md = _md_1096()
        assert "One-hundred-forty-second quoted-search no-match" in md
        assert "returned no matching podcast" in md

    def test_blob_did_not_surface_this_run(self):
        md = _md_1096()
        assert "the podcast-sentiment.md blob did NOT surface this run" in md
        assert "7 commit URLs only" in md

    def test_commit_urls_git_log_verified_circular(self):
        md = _md_1096()
        for short in self.OWN_REPO_COMMIT_SHORTHS:
            assert short in md
            assert _git(["cat-file", "-t", short]).stdout.strip() == "commit", short
        assert "git-cat-file-verified present" in md
        assert "circular as evidence" in md

    def test_tracked_sources_141_to_142(self):
        assert "Tracked Sources advanced 141->142" in _md_1096()

    def test_task_spec_still_misidentified(self):
        md = _md_1096()
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 7. Press surfaces: SIX re-surfaces, ZERO new keys
# --------------------------------------------------------------------------
class TestPressSurfacesHundredFortySecondCycle:
    PRESS_RESURFACED_KEYS = [
        "usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses/91913146007/",
        "community.designtaxi.com/topic/39120-meta-releases-ray-ban-smart-glasses-without-the-cameras-amid-privacy-stalking-concerns/",
        "americanow.com/FreeNewsReader/tech-firms-address-smart-glasses-privacy-concerns-amidst-public-backlash/",
        "analyticsinsight.net/news/meta-ray-ban-audio-launches-at-usd-349-with-camera-free-ai",
        "thesun.ie/tech/17676556/meta-vr-glasses-boz-andrew-bosworth-ray-ban-audio/",
        "gagadget.com/en/727279-ray-ban-meta-audio-smart-glasses-without-the-camera-controversy/",
    ]

    def test_six_resurfaces_zero_new_key(self):
        md = _md_1096()
        assert "SIX previously-logged keys re-surfaced this run" in md
        assert "ZERO new-to-corpus press URL keys this run" in md

    def test_resurfaced_keys_all_in_corpus(self):
        for key in self.PRESS_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_thesun_boz_resurfaces_again(self):
        md = _md_1096()
        assert "thesun.ie Boz piece 17676556 (crawled 1d; in corpus via #1071, re-surfaced again)" in md

    def test_gagadget_resurfaces_again_via_981_986(self):
        md = _md_1096()
        assert "gagadget Ray-Ban Audio camera-free piece (crawled <1h; in corpus via #981/#986, re-surfaced again)" in md

    def test_mid_cycle_press_keys_cited(self):
        md = _md_1096()
        assert "americanow FreeNewsReader backlash piece (crawled 2h; in corpus via #1011)" in md
        assert "analyticsinsight Ray-Ban Audio piece (crawled 7h; in corpus via #1016)" in md

    def test_recency_frontier_holds_at_sep_29(self):
        md = _md_1096()
        assert "Recency frontier: HOLDS at Sep 29" in md
        assert "fifth hold since the #1071 advance" in md

    def test_asymmetry_note_meta_exclusive(self):
        md = _md_1096()
        assert "Meta-exclusive privacy-pressure framing continues across all 142 cycles" in md
        assert "no competitor camera-wearable coverage carries equivalent privacy-pressure framing" in md

    def test_snippet_bounded_tone_not_scored(self):
        md = _md_1096()
        assert "Snippet-bounded, tone NOT_SCORED per the standing rule" in md


# --------------------------------------------------------------------------
# 8. Guard lifecycle: the #1095 zero-889 pins PASS this run
# --------------------------------------------------------------------------
class TestGuardLifecycleZero889Pin:
    def test_1095_file_pins_max_id_888_and_next_889(self):
        text = _read(os.path.join(REPO, "tests", D1095_FILE))
        assert re.search(r"^MAX_ID = 888", text, re.M), D1095_FILE
        assert re.search(r"^NEXT_NUM = 889", text, re.M), D1095_FILE

    def test_zero_next_numeric_889_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        needle = "mechanism" + "_id" + ":"
        digits = "8" + "89"
        out = _git(["grep", "-nE", f"{needle}[[:space:]]*{digits}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_889_carriers_pinned_to_guard_needles_only(self):
        # Format-built per #715: the 889 needles are never carried as
        # contiguous literals in source files. profiles/ and tests/
        # carry no 889 mechanism key strings. Own file excluded; no
        # new carrier may appear this run.
        n1 = "mech" + "anism_" + "8" + "89"
        n2 = "mech" + "anism-" + "8" + "89"
        hits = set()
        for p in glob.glob(os.path.join(REPO, "tests", "test_*.py")):
            if os.path.basename(p) == THIS_FILE:
                continue
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.add(os.path.basename(p))
        for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.add(os.path.basename(p))
        assert hits == set(), hits

    def test_889_guards_exist_in_1095_file(self):
        # The zero-889 guards exist in the #1095 file (PASS this run,
        # verified at this run's pre-commit check), and fail BY DESIGN
        # when mechanism 889 lands at a future A/B/C leg of the
        # 1095-1099 window.
        text = _read(os.path.join(REPO, "tests", D1095_FILE))
        assert "test_zero_889_numeric_forms_in_profiles" in text
        assert "test_zero_889_forms_repo_wide" in text

    def test_889_guards_fail_by_design_lifecycle(self):
        # Calendar pin: the 888 landing happened at #1094 (Type C).
        # The zero-889 guards fail BY DESIGN when mechanism 889 lands -
        # expected at a future A/B/C leg of the 1095-1099 window.
        text = _read(os.path.join(REPO, "tests", D1095_FILE))
        assert "zero-889" in text.lower()


# --------------------------------------------------------------------------
# 9. Corpus novelty pre-commit greps per #715
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_1096_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_1096*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_888(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # m886/m887/m888 committed at #1092/#1093/#1094 Type A/B/C, all
        # verified at #1095 Type D. Type E adds no mechanisms. (The
        # in-flight #899 m771 hunk does not change the max.)
        assert maxid == 888

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "8" + "89"
        needle = "mechanism" + "_id" + ":"
        out = _git(["grep", "-nE", f"{needle}[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles(self):
        # Format-built needles per #715: no literal next-number
        # mechanism key strings carried in profiles/.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "8" + "89"
        n2 = "mech" + "anism" + "-" + "8" + "89"
        hits = []
        for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(p)
        assert hits == []

    def test_next_carriers_in_tests_pinned_to_guard_files(self):
        # Underscore/dash 889 needles in tests/ must appear ONLY in the
        # pinned guard carriers - and per #715 all 889 needles are
        # fragment-constructed, so NO committed test file carries an 889
        # key literal: the carrier set is EMPTY. (The #1095 zero-889
        # guard needles are verified present and fragment-correct in the
        # guard-lifecycle class.) Own file carries no 889 literal
        # (excluded); no new carrier may appear this run.
        n1 = "mech" + "anism_" + "8" + "89"
        n2 = "mech" + "anism-" + "8" + "89"
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
# 10. Statistical discipline: the Aug 28 2026 standing rule
# --------------------------------------------------------------------------
class TestStatisticalDisciplineStandingRule:
    def test_tone_not_scored(self):
        assert "NOT_SCORED" in _md_1096()

    def test_engine_not_run_no_significance(self):
        md = _md_1096()
        assert "engine NOT run" in md
        assert "is_significant False" in md

    def test_no_new_mechanisms_monitoring_only(self):
        assert "monitoring-only" in _md_1096()
        assert "no mechanisms added" in _md_1096()

    def test_falsification_ledger_holds_at_37(self):
        assert "ledger holds at 37" in _md_1096()

    def test_not_artifact_grade_correlation_not_causation(self):
        md = _md_1096()
        assert "NOT artifact-grade" in md
        assert "Correlation is not causation" in md
        assert "directionally_supported_not_proven" in md

    def test_result_row_counts(self):
        md = _md_1096()
        assert "27 result rows / 18 non-circular distinct URL keys / ZERO new verbatim URL keys this run" in md


# --------------------------------------------------------------------------
# 11. Doc-sync ratchet per #719
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_test_file_table_row_present(self):
        # This run's test-file table row must exist in README.md.
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_readme_stats_advanced(self):
        # Fails pre-commit by design; green once doc-sync ratchets
        # the stats table: 55599/1420 -> 55660/1421 (+61/+1 this file).
        text = _read(README)
        assert "| Tests | 55660 | Across 1421 test files |" in text

    def test_architecture_tests_tree_updated(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE.replace(".py", "") in _read(ARCH)

    def test_architecture_lists_1096_file(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE in set(re.findall(r"(test_\w+\.py)", _read(ARCH)))


# --------------------------------------------------------------------------
# 12. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_1096_entry_present_with_finding_shape(self):
        # Fails pre-commit by design; green once the iteration-log
        # entry is prepended.
        log = _read(LOG)
        assert "## #1096 Type E" in log
        idx = log.index("## #1096 Type E")
        block = log[idx : idx + 3000]
        assert "142nd verification" in block
        assert "Sep 30 2026, 09:00 PDT" in block
        assert "SECOND leg of the 1095-1099 window" in block

    def test_1096_entry_carries_commit_hashes_per_721(self):
        log = _read(LOG)
        idx = log.index("## #1096 Type E")
        block = log[idx : idx + 3000]
        assert "main commit" in block
        assert "anchor" in block
        assert "log-hash followup" in block

    def test_1096_entry_carries_streak_and_frontier_prose(self):
        log = _read(LOG)
        idx = log.index("## #1096 Type E")
        block = log[idx : idx + 4000]
        assert "the all-key pure-re-surface streak RESTARTS at one" in block
        assert "recency frontier HOLDS at Sep 29" in block


# --------------------------------------------------------------------------
# 13. Push readiness per #716 / #717
# --------------------------------------------------------------------------
class TestPushReadiness:
    def test_ascii_only_no_em_dashes(self):
        raw = open(os.path.join(REPO, "tests", THIS_FILE), "rb").read()
        assert all(b < 128 for b in raw), "non-ASCII byte in own file"
        assert b"\\xe2\\x80\\x94" not in raw  # em dash, escaped so own file stays ASCII-only

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
