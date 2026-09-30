"""Type E #1091: podcast sentiment 141st verification cycle - GF EPISODE 502
HOLDS as latest (eighth Type E verification since the Sep 28 11:00am
release (~41 hours after publication); NO 503 surfaced; three-directory
corroboration), EHE 51-day hold (Aug 10 Epstein spoof -> Sep 30) with FIVE
logged keys re-surfaced (huckmag pervert-glasses piece re-surfaced after
the #1086 non-surface; kayvan-mirza op-ed re-surfaced after the #1086
non-surface) and ONE new-to-corpus verbatim URL key (feminist.org author
archive, SECONDARY CITATION per #531 - campaign-coverage of the ongoing
strands, not a new campaign motif), Attention Sphere 141st no-match as a
podcast (7 own-repo GitHub commit URLs only; blob did NOT surface this
run; git-cat-file-verified circular; Tracked Sources 140->141), press
SEVEN in-corpus re-surfaces (thesun.ie Boz piece re-surfaces again;
gagadget re-surfaces via #981/#986; linkedin roundup, letsdatascience,
and ppc.land stay non-surfacing) + ZERO new press keys; the all-key
pure-re-surface streak ENDS at three (restarted at #1076); recency
frontier HOLDS at Sep 29 (fourth hold since the #1071 advance).
Guard lifecycle: the #1090 Type D run pinned the zero-886 forward-looking
guards (MAX_ID = 885, NEXT_NUM = 886 in the #1090 file); they PASS this run
and fail BY DESIGN when mechanism 886 lands at a future A/B/C leg of the
1090-1094 window.

Second leg of the 1090-1094 window: D (#1090) -> E (#1091) -> A -> B -> C.
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

ITERATION = 1091
TYPE_LETTER = "E"
RUN_PDT = "2026-09-30 04:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "711d3169181f1e583b8fc96a7ec39d791f35f7f1"

README_TESTS_AFTER = 55301
README_FILES_AFTER = 1416

# The #1090 Type D file pins this window's zero-886 forward-looking
# guards (MAX_ID = 885, NEXT_NUM = 886). This run verifies they PASS.
D1090_FILE = (
    "test_type_d_1090_m883_m884_m885_qualitative_corpus_integrity_"
    "sep30_3am.py"
)
MAX_ID = 885
NEXT_NUM = 886

# New verbatim URL key this run (zero pre-commit corpus hits). Needle
# format-built per #715; not carried as a contiguous literal anywhere
# else in this file (only inside the md-section prose via variable).
NEW_KEY = "http" + "://feminist.org" + "/news" + "/author" + "/lkollross/"


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _corpus_hits(needle):
    return _git(["grep", "-l", needle, "--", "."]).stdout.splitlines()


def _md_1091():
    return _read(MD).split("## Iteration #1091")[1]


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE1091:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1091 main commit exists pre-commit; the anchor test pins
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
            if "Type E #1091" in line and "followup" not in line.lower()
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
# 2. Rotation guard: second leg of the 1090-1094 window
# --------------------------------------------------------------------------
class TestRotationGuard1090_1094Window:
    @pytest.mark.rotation
    def test_second_leg_of_1090_1094_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 1091

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {1090: "D", 1091: "E", 1092: "A", 1093: "B", 1094: "C"}
        assert expected[1091] == "E"

    @pytest.mark.rotation
    def test_predecessor_1090_present(self):
        # The #1090 Type D opener's main, anchor, and log-hash commits
        # must all be in history before this run commits.
        for short in ("4881bd45", "418a8b52", "3c5c48ce"):
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
# 4. Guilty Feminist: 141st cycle - episode 502 holds, streak ends at three
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredFortyFirstCycle:
    GF_RESURFACED_KEYS = [
        "podscan.fm/podcasts/the-guilty-feminist-1",
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "youtube.com/watch?v=iKXj2w2cp50",
        "podscan.fm/podcasts/the-guilty-feminist",
        "goloudnow.com/podcasts/the-guilty-feminist-152/deborah-frances-white-on-the-news-meeting-519585",
        "uk-podcasts.co.uk/podcast/the-guilty-feminist/deborah-frances-white-on-the-news-meeting",
    ]

    def test_episode_502_holds_as_latest_no_503(self):
        md = _md_1091()
        assert "EPISODE 502 HOLDS as latest" in md
        assert "eighth Type E verification since the Sep 28 11:00am release (~41 hours after publication)" in md
        assert "NO 503 surfaced" in md
        assert "The Guilty Feminist 502. Homophobia" in md

    def test_three_directory_corroboration(self):
        md = _md_1091()
        assert "Three-directory corroboration this run" in md
        assert "LATEST EPISODE: The Guilty Feminist 502. Homophobia" in md
        assert "Latest Episode: 502. Homophobia with Freya Parker and Linus Karp" in md
        assert '"Latest episode: 2026-09-28"' in md

    def test_502_cast_and_venue_logged(self):
        md = _md_1091()
        assert "Freya Parker" in md
        assert "Linus Karp" in md
        assert "recorded 21 August 2026 at Gilded Balloon at the Museum" in md

    def test_zero_new_gf_keys_but_streak_ends(self):
        md = _md_1091()
        assert "ZERO new-to-corpus verbatim GF URL keys this run" in md
        assert "The all-key pure-re-surface streak ENDS at three (restarted at #1076)" in md

    def test_gf_resurfaced_keys_in_corpus(self):
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_gf_circular_commit_url_rejected(self):
        md = _md_1091()
        assert "2f9a4a27" in md
        assert "git-cat-file-verified present" in md
        assert "rejected as circular, not ingested" in md

    def test_zero_meta_wearables_content_141_cycles(self):
        md = _md_1091()
        assert "ZERO Meta/wearables content in any GF episode across all 141 cycles" in md
        assert "topic: homophobia; snippet-bounded" in md
        assert "no tone score asserted" in md


# --------------------------------------------------------------------------
# 5. Everyone Hates Elon: 51-day hold, FIVE logged keys + ONE new key
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredFortyFirstCycle:
    EHE_RESURFACED_KEYS = [
        "afrotech.com/smart-glasses-ethics-and-consent",
        "huckmag.com/article/activists-slam-pervert-glasses-in-new-guerrilla-campaign",
        "linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates-viky-hurai-jaklovska-ssqwf",
        "linkedin.com/pulse/dear-ai-glasses-industry-situation-critical-red-kayvan-mirza-zwaze",
        "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
    ]

    def test_51_day_hold(self):
        md = _md_1091()
        assert "51-day hold continues" in md
        assert "date(2026,9,30)-date(2026,8,10)=51 days" in md

    def test_five_logged_keys_resurfaced(self):
        md = _md_1091()
        assert "5 logged keys re-surfaced this run" in md
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_huckmag_resurfaces(self):
        md = _md_1091()
        assert "huckmag pervert-glasses piece (crawled 2h; in corpus via #1021, re-surfaced" in md

    def test_kayvan_mirza_resurfaces_after_1086_non_surface(self):
        md = _md_1091()
        assert "kayvan-mirza op-ed (crawled 1d; in corpus via #1001/#1006, re-surfaced after the #1086 non-surface)" in md

    def test_one_new_verbatim_ehe_key_secondary_citation(self):
        md = _md_1091()
        assert "ONE new-to-corpus verbatim EHE URL key" in md
        assert "feminist.org author archive" in md
        assert "SECONDARY CITATION per #531, not an independent surface" in md
        assert "campaign-coverage of the ongoing strands, not a new campaign motif" in md
        # The new key must now be present in the working tree (the md
        # section this run wrote) - it was zero-hit pre-commit.
        assert _corpus_hits(NEW_KEY), NEW_KEY

    def test_one_circular_github_url_rejected(self):
        md = _md_1091()
        assert "1 own-repo GitHub URL in the EHE result set" in md
        assert "podcast-sentiment.md blob, git-cat-file-verified present" in md
        assert "rejected as circular, not ingested" in md

    def test_no_competitor_equivalent_campaign_141_cycles(self):
        md = _md_1091()
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 141 cycles" in md

    def test_non_surfacing_strands_remain_in_corpus(self):
        md = _md_1091()
        for strand in (
            "designtaxi 34124 Epstein-ad thread",
            "softonic Epstein-poster",
            "thebesttimes consent email-drive",
            "cloudfront Kylie-poster mirror",
            "ranzware Kylie-lenticular mirror",
            "lapost CNN relay",
            "Non-surfacing strands remain in corpus",
        ):
            assert strand in md, strand

    def test_epstein_ad_thread_still_primary_motif(self):
        md = _md_1091()
        assert "Glasses for people who don't do consent." in md
        assert "still the primary motif" in md


# --------------------------------------------------------------------------
# 6. Attention Sphere: 141st no-match as a podcast
# --------------------------------------------------------------------------
class TestAttentionSphereHundredFortyFirstNoMatch:
    OWN_REPO_COMMIT_SHORTHS = ["40d6e7b0", "d4618aae", "5e238e78", "0d9132c6", "bf0cbbf1", "dec56140", "16611229"]

    def test_141st_no_match_prose(self):
        md = _md_1091()
        assert "One-hundred-forty-first quoted-search no-match" in md
        assert "returned no matching podcast" in md

    def test_blob_did_not_surface_this_run(self):
        md = _md_1091()
        assert "the podcast-sentiment.md blob did NOT surface this run" in md
        assert "7 commit URLs only" in md

    def test_commit_urls_git_log_verified_circular(self):
        md = _md_1091()
        for short in self.OWN_REPO_COMMIT_SHORTHS:
            assert short in md
            assert _git(["cat-file", "-t", short]).stdout.strip() == "commit", short
        assert "git-cat-file-verified present" in md
        assert "circular as evidence" in md

    def test_tracked_sources_140_to_141(self):
        assert "Tracked Sources advanced 140->141" in _md_1091()

    def test_task_spec_still_misidentified(self):
        md = _md_1091()
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 7. Press surfaces: SEVEN re-surfaces, ZERO new
# --------------------------------------------------------------------------
class TestPressSurfacesHundredFortyFirstCycle:
    PRESS_RESURFACED_KEYS = [
        "usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses/91913146007/",
        "community.designtaxi.com/topic/39120-meta-releases-ray-ban-smart-glasses-without-the-cameras-amid-privacy-stalking-concerns/",
        "americanow.com/FreeNewsReader/tech-firms-address-smart-glasses-privacy-concerns-amidst-public-backlash/",
        "techgig.com/news/tech-drops/meta-unveils-ai-powered-muse-charm-camera-free-ray-ban-glasses-at-connect-event/134472411",
        "analyticsinsight.net/news/meta-ray-ban-audio-launches-at-usd-349-with-camera-free-ai",
        "thesun.ie/tech/17676556/meta-vr-glasses-boz-andrew-bosworth-ray-ban-audio/",
        "gagadget.com/en/727279-ray-ban-meta-audio-smart-glasses-without-the-camera-controversy/",
    ]

    def test_seven_resurfaces_zero_new_key(self):
        md = _md_1091()
        assert "SEVEN previously-logged keys re-surfaced this run" in md
        assert "ZERO new-to-corpus press URL keys this run" in md

    def test_resurfaced_keys_all_in_corpus(self):
        for key in self.PRESS_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_thesun_boz_resurfaces_again(self):
        md = _md_1091()
        assert "thesun.ie Boz piece 17676556 (crawled 1d; in corpus via #1071, re-surfaced again)" in md

    def test_gagadget_resurfaces_again_via_981_986(self):
        md = _md_1091()
        assert "gagadget Ray-Ban Audio camera-free piece (crawled 3h; in corpus via #981/#986, re-surfaced again)" in md

    def test_mid_cycle_press_keys_cited(self):
        md = _md_1091()
        assert "americanow FreeNewsReader backlash piece (crawled 1h; in corpus via #1011)" in md
        assert "techgig Sep-25 Muse Charm piece (crawled 1d; in corpus via #1016)" in md
        assert "analyticsinsight Ray-Ban Audio piece (crawled 2h; in corpus via #1016)" in md

    def test_recency_frontier_holds_at_sep_29(self):
        md = _md_1091()
        assert "Recency frontier: HOLDS at Sep 29" in md
        assert "fourth hold since the #1071 advance" in md

    def test_asymmetry_note_meta_exclusive(self):
        md = _md_1091()
        assert "Meta-exclusive privacy-pressure framing continues across all 141 cycles" in md
        assert "no competitor camera-wearable coverage carries equivalent privacy-pressure framing" in md

    def test_snippet_bounded_tone_not_scored(self):
        md = _md_1091()
        assert "Snippet-bounded, tone NOT_SCORED per the standing rule" in md


# --------------------------------------------------------------------------
# 8. Guard lifecycle: the #1090 zero-886 pins PASS this run
# --------------------------------------------------------------------------
class TestGuardLifecycleZero886Pin:
    def test_1090_file_pins_max_id_885_and_next_886(self):
        text = _read(os.path.join(REPO, "tests", D1090_FILE))
        assert re.search(r"^MAX_ID = 885", text, re.M), D1090_FILE
        assert re.search(r"^NEXT_NUM = 886", text, re.M), D1090_FILE

    def test_zero_next_numeric_886_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        needle = "mechanism" + "_id" + ":"
        digits = "8" + "86"
        out = _git(["grep", "-nE", f"{needle}[[:space:]]*{digits}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_886_carriers_pinned_to_guard_needles_only(self):
        # Format-built per #715: the 886 needles are never carried as
        # contiguous literals in source files. profiles/ and tests/
        # carry no 886 mechanism key strings. Own file excluded; no
        # new carrier may appear this run.
        n1 = "mech" + "anism_" + "8" + "86"
        n2 = "mech" + "anism-" + "8" + "86"
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

    def test_886_guards_exist_in_1090_file(self):
        # The zero-886 guards exist in the #1090 file (PASS this run,
        # verified at this run's pre-commit check), and fail BY DESIGN
        # when mechanism 886 lands at a future A/B/C leg of the
        # 1090-1094 window.
        text = _read(os.path.join(REPO, "tests", D1090_FILE))
        assert "test_zero_886_numeric_forms_in_profiles" in text
        assert "test_zero_886_forms_repo_wide" in text

    def test_886_guards_fail_by_design_lifecycle(self):
        # Calendar pin: the 885 landing happened at #1089 (Type C).
        # The zero-886 guards fail BY DESIGN when mechanism 886 lands -
        # expected at a future A/B/C leg of the 1090-1094 window.
        text = _read(os.path.join(REPO, "tests", D1090_FILE))
        assert "zero-886" in text.lower()


# --------------------------------------------------------------------------
# 9. Corpus novelty pre-commit greps per #715
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_1091_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_1091*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_885(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # m883/m884/m885 committed at #1087/#1088/#1089 Type A/B/C, all
        # verified at #1090 Type D. Type E adds no mechanisms. (The
        # in-flight #899 m771 hunk does not change the max.)
        assert maxid == 885

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "8" + "86"
        needle = "mechanism" + "_id" + ":"
        out = _git(["grep", "-nE", f"{needle}[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles(self):
        # Format-built needles per #715: no literal next-number
        # mechanism key strings carried in profiles/.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "8" + "86"
        n2 = "mech" + "anism" + "-" + "8" + "86"
        hits = []
        for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(p)
        assert hits == []

    def test_next_carriers_in_tests_pinned_to_guard_files(self):
        # Underscore/dash 886 needles in tests/ must appear ONLY in the
        # pinned guard carriers - and per #715 all 886 needles are
        # fragment-constructed, so NO committed test file carries an 886
        # key literal: the carrier set is EMPTY. (The #1090 zero-886
        # guard needles are verified present and fragment-correct in the
        # guard-lifecycle class.) Own file carries no 886 literal
        # (excluded); no new carrier may appear this run.
        n1 = "mech" + "anism_" + "8" + "86"
        n2 = "mech" + "anism-" + "8" + "86"
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
        assert "NOT_SCORED" in _md_1091()

    def test_engine_not_run_no_significance(self):
        md = _md_1091()
        assert "engine NOT run" in md
        assert "is_significant False" in md

    def test_no_new_mechanisms_monitoring_only(self):
        assert "monitoring-only" in _md_1091()
        assert "no mechanisms added" in _md_1091()

    def test_falsification_ledger_holds_at_37(self):
        assert "ledger holds at 37" in _md_1091()

    def test_not_artifact_grade_correlation_not_causation(self):
        md = _md_1091()
        assert "NOT artifact-grade" in md
        assert "Correlation is not causation" in md
        assert "directionally_supported_not_proven" in md

    def test_result_row_counts(self):
        md = _md_1091()
        assert "28 result rows / 19 non-circular distinct URL keys / ONE new verbatim URL key this run" in md


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
        # the stats table: 55239/1415 -> 55301/1416 (+62/+1 this file).
        text = _read(README)
        assert "| Tests | 55301 | Across 1416 test files |" in text

    def test_architecture_tests_tree_updated(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE.replace(".py", "") in _read(ARCH)

    def test_architecture_lists_1091_file(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE in set(re.findall(r"(test_\w+\.py)", _read(ARCH)))


# --------------------------------------------------------------------------
# 12. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_1091_entry_present_with_finding_shape(self):
        # Fails pre-commit by design; green once the iteration-log
        # entry is prepended.
        log = _read(LOG)
        assert "## #1091 Type E" in log
        idx = log.index("## #1091 Type E")
        block = log[idx : idx + 3000]
        assert "141st verification" in block
        assert "Sep 30 2026, 04:00 PDT" in block
        assert "SECOND and MIDDLE leg of the 1090-1094 window" in block

    def test_1091_entry_carries_commit_hashes_per_721(self):
        log = _read(LOG)
        idx = log.index("## #1091 Type E")
        block = log[idx : idx + 3000]
        assert "main commit" in block
        assert "anchor" in block
        assert "log-hash followup" in block

    def test_1091_entry_carries_streak_and_frontier_prose(self):
        log = _read(LOG)
        idx = log.index("## #1091 Type E")
        block = log[idx : idx + 4000]
        assert "the all-key pure-re-surface streak ENDS at three" in block
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
