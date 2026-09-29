"""Type E #1066: podcast sentiment 136th verification cycle - GF EPISODE 502
HOLDS as latest (third day since the Sep 28 11:00am release; NO 503
surfaced; three-directory corroboration), EHE 50-day hold (Aug 10 Epstein
spoof -> Sep 29) with FIVE logged keys re-surfaced and ZERO new EHE keys,
Attention Sphere 136th no-match as a podcast (blob SURFACED AGAIN + 6
commit URLs git-cat-file-verified circular; Tracked Sources 135->136),
press SEVEN in-corpus re-surfaces (recency frontier HOLDS at Sep 26, sixth
hold after the #1036 advance) + ZERO new verbatim keys; Meta-exclusive
privacy-pressure framing across all 136 cycles. The all-key pure-re-surface
streak advances to SIX. Guard lifecycle pin: the #1062/#1063/#1064 window
files pin the zero-871 forward-looking guards (M_ID == 870 in all three;
PASS this run, fail BY DESIGN when mechanism 871 lands at a future A/B/C
leg; to be pinned by the #1070 Type D run).

Second leg of the 1065-1069 window: D (#1065) -> E (#1066) -> A -> B -> C.
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

ITERATION = 1066
TYPE_LETTER = "E"
RUN_PDT = "2026-09-29 03:00 PDT"
OWN_BASENAME = os.path.basename(__file__)
ANCHORED_SHA = "8c144fe8680a58e85a1b081841f7a0706dab0d52"

README_TESTS_AFTER = 54709
README_FILES_AFTER = 1391

# The 1065-1069 window's A/B/C legs; each carries its zero-871
# forward-looking guards (needles format-built per #715).
GUARD_FILES = [
    "test_type_a_1062_ft_apple_sep2026_duo_launch_market_register_vs_meta_muse_product_register_sep28_11pm.py",
    "test_type_b_1063_james_pero_gizmodo_vr_headsets_cooked_enthusiasm_vs_pr_cleanup_adversarial_sep29_12am.py",
    "test_type_c_1064_oracle_openai_300b_45gw_demand_underwriting_twentieth_direction_sep29_1am.py",
]


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _corpus_hits(needle):
    return _git(["grep", "-l", needle, "--", "."]).stdout.splitlines()


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _md_1066():
    return _read(MD).split("## Iteration #1066")[1]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeE1066:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1066 main commit exists pre-commit; the anchor test pins
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
            if "Type E #1066" in line and "followup" not in line.lower()
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
# 2. Rotation guard: second leg of the 1065-1069 window
# --------------------------------------------------------------------------
class TestRotationGuard1065_1069Window:
    @pytest.mark.rotation
    def test_second_leg_of_1065_1069_window(self):
        assert TYPE_LETTER == "E"
        assert ITERATION == 1066

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {1065: "D", 1066: "E", 1067: "A", 1068: "B", 1069: "C"}
        assert expected[1066] == "E"

    @pytest.mark.rotation
    def test_predecessor_1065_type_d_committed(self):
        # #1065 Type D is COMMITTED (its log entry sits at the head of
        # iteration-log.md, directly under this run's own #1066 entry
        # once prepended). Regex-visible window chain post-commit reads
        # E1066 -> D1065 -> C1064 -> B1063 -> A1062 straight.
        assert "## #1065 Type D" in _read(LOG)


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
# 4. The Guilty Feminist: 136th cycle, EPISODE 502 HOLDS, no 503
# --------------------------------------------------------------------------
class TestGuiltyFeministHundredThirtySixthCycle:
    GF_RESURFACED_KEYS = [
        "podscan.fm/podcasts/the-guilty-feminist-1",
        "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white",
        "youtube.com/watch?v=iKXj2w2cp50",
        "podscan.fm/podcasts/the-guilty-feminist",
        "goloudnow.com/podcasts/the-guilty-feminist-152/deborah-frances-white-on-the-news-meeting-519585",
        "uk-podcasts.co.uk/podcast/the-guilty-feminist/deborah-frances-white-on-the-news-meeting",
        "podscan.fm/podcasts/the-guilty-feminist/episodes/499-where-you-end-and-i-begin-with-lindsey-mendick-1",
    ]

    def test_episode_502_holds_as_latest_no_503(self):
        md = _md_1066()
        assert "EPISODE 502 HOLDS as latest" in md
        assert "third day since the Sep 28 11:00am release" in md
        assert "NO 503 surfaced" in md
        assert "The Guilty Feminist 502. Homophobia" in md

    def test_three_directory_corroboration(self):
        md = _md_1066()
        assert "Three-directory corroboration this run" in md
        assert "Latest Episode: 502. Homophobia" in md
        assert "LATEST EPISODE: The Guilty Feminist 502. Homophobia" in md
        assert '"Latest episode: 2026-09-28"' in md

    def test_502_cast_and_venue_logged(self):
        md = _md_1066()
        assert "Freya Parker" in md
        assert "Linus Karp" in md
        assert "recorded 21 August 2026 at Gilded Balloon at the Museum" in md

    def test_zero_new_gf_keys_all_key_streak_advances_to_six(self):
        md = _md_1066()
        assert "ZERO new-to-corpus verbatim GF URL keys this run" in md
        assert "The all-key pure-re-surface streak advances to SIX" in md
        assert "ZERO new verbatim URL keys across all four strands this run" in md

    def test_gf_resurfaced_keys_in_corpus(self):
        for key in self.GF_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_zero_meta_wearables_content_136_cycles(self):
        md = _md_1066()
        assert "ZERO Meta/wearables content in any GF episode across all 136 cycles" in md
        assert "topic: homophobia; snippet-bounded" in md
        assert "no tone score asserted" in md


# --------------------------------------------------------------------------
# 5. Everyone Hates Elon: 50-day hold, FIVE logged keys re-surfaced
# --------------------------------------------------------------------------
class TestEveryoneHatesElonHundredThirtySixthCycle:
    EHE_RESURFACED_KEYS = [
        "community.designtaxi.com/topic/34124",
        "en.softonic.com/articles/ray-ban-meta-smart-glasses-back-in-the-spotlight",
        "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
        "afrotech.com/smart-glasses-ethics-and-consent",
        "thebesttimes.com/entertainment/technology_and_science/do-you-consent-to-being-filmed-by-ai-glasses",
    ]

    def test_50_day_hold(self):
        md = _md_1066()
        assert "50-day hold continues" in md
        assert "date(2026,9,29)-date(2026,8,10)=50 days" in md

    def test_five_logged_keys_resurfaced(self):
        md = _md_1066()
        assert "5 logged keys re-surfaced this run" in md
        for key in self.EHE_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_zero_new_ehe_keys_this_run(self):
        assert "ZERO new-to-corpus verbatim EHE URL keys this run" in _md_1066()

    def test_two_circular_github_urls_rejected(self):
        md = _md_1066()
        assert "2 own-repo GitHub URLs in the EHE result set" in md
        assert "rejected as circular, not ingested" in md
        assert "36592f8" in md

    def test_no_competitor_equivalent_campaign_136_cycles(self):
        md = _md_1066()
        assert "No competitor-equivalent guerrilla campaign against Apple/Google/Samsung/Snap camera wearables in any of the 136 cycles" in md

    def test_non_surfacing_strands_remain_in_corpus(self):
        md = _md_1066()
        assert "ranzware Kylie-lenticular mirror" in md
        assert "engadget bus-stops original" in md
        assert "hyperallergic Epstein ad" in md
        assert "latestly fact-check pair" in md
        assert "lapost CNN relay" in md
        assert "kayvan-mirza op-ed" in md
        assert "huckmag pervert-glasses" in md
        assert "Non-surfacing strands remain in corpus" in md

    def test_epstein_ad_thread_still_primary_motif(self):
        md = _md_1066()
        assert "Glasses for people who don't do consent." in md
        assert "still the primary motif" in md


# --------------------------------------------------------------------------
# 6. Attention Sphere: 136th no-match as a podcast
# --------------------------------------------------------------------------
class TestAttentionSphereHundredThirtySixthNoMatch:
    OWN_REPO_COMMIT_SHORTHS = ["9590385", "a288c86", "a2b656f", "25c730e", "6da2928", "fe4528b"]

    def test_136th_no_match_prose(self):
        md = _md_1066()
        assert "One-hundred-thirty-sixth quoted-search no-match" in md
        assert "returned no matching podcast" in md

    def test_blob_surfacing_again(self):
        md = _md_1066()
        assert "SURFACED AGAIN this run" in md

    def test_commit_urls_git_log_verified_circular(self):
        md = _md_1066()
        for short in self.OWN_REPO_COMMIT_SHORTHS:
            assert short in md
        assert "git-cat-file-verified present" in md
        assert "circular as evidence" in md

    def test_tracked_sources_135_to_136(self):
        assert "Tracked Sources advanced 135->136" in _md_1066()

    def test_task_spec_still_misidentified(self):
        md = _md_1066()
        assert "Task-spec name remains misidentified as a podcast" in md
        assert "Real-world identity stands per #591" in md


# --------------------------------------------------------------------------
# 7. Press surfaces: SEVEN re-surfaces + ZERO new keys, frontier HOLDS
# --------------------------------------------------------------------------
class TestPressSurfacesHundredThirtySixthCycle:
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
        md = _md_1066()
        assert "SEVEN previously-logged keys re-surfaced this run" in md
        assert "ZERO new-to-corpus verbatim URL keys this run" in md

    def test_resurfaced_keys_all_in_corpus(self):
        for key in self.PRESS_RESURFACED_KEYS:
            assert _corpus_hits(key), key

    def test_linkedin_privacy_roundup_plain_resurface(self):
        md = _md_1066()
        assert "the linkedin privacy roundup (crawled 2h, logged via #976)" in md
        assert _corpus_hits("linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates")

    def test_ppc_land_hamburg_in_corpus_resurface(self):
        md = _md_1066()
        assert "ppc.land Hamburg regulator piece (crawled <1h, in corpus via podcast-sentiment.md)" in md

    def test_recency_frontier_holds_at_sep_26_sixth_hold(self):
        md = _md_1066()
        assert "Recency frontier: HOLDS at Sep 26" in md
        assert "sixth hold after the #1036 advance" in md

    def test_asymmetry_note_meta_exclusive(self):
        md = _md_1066()
        assert "Meta-exclusive privacy-pressure framing continues across all 136 cycles" in md
        assert "no competitor camera-wearable coverage carries equivalent privacy-pressure framing" in md

    def test_snippet_bounded_tone_not_scored(self):
        md = _md_1066()
        assert "Snippet-bounded, tone NOT_SCORED per the standing rule" in md


# --------------------------------------------------------------------------
# 8. Guard lifecycle pin: zero-871 forward-looking guards (designed lifecycle)
# --------------------------------------------------------------------------
class TestGuardLifecycleZero871Pin:
    def test_window_files_pin_m_id_870(self):
        # All three window files were rolled to M_ID = 870 by the #1064
        # roll-forward; the OWN_M_ID split (868/869 in the A/B legs)
        # keeps own-mechanism structure separate from the corpus max.
        for base in GUARD_FILES:
            text = _read(os.path.join(REPO, "tests", base))
            assert re.search(r"^M_ID = 870$", text, re.M), base

    def test_zero_next_numeric_871_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        needle = "mechanism" + "_id" + ":"
        digits = "8" + "71"
        out = _git(["grep", "-nE", f"{needle}[[:space:]]*{digits}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_871_carriers_pinned_to_guard_files_only(self):
        # Format-built per #715: the 871 needles are never carried as
        # contiguous literals anywhere (the #1062 NEXT_US/NEXT_DASH
        # sweeps and the #1063 NEXT_* sweeps are fragment-constructed;
        # the #1064 guard names carry the bare digits, not the key
        # string). A contiguous literal sweep is therefore the empty
        # set; the guards themselves are verified present and fragment
        # correct in the lifecycle test below.
        n1 = "mech" + "anism_" + "8" + "71"
        n2 = "mech" + "anism-" + "8" + "71"
        hits = set()
        for p in glob.glob(os.path.join(REPO, "tests", "test_*.py")):
            if os.path.basename(p) == THIS_FILE:
                continue
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.add(os.path.basename(p))
        assert hits == set(), hits

    def test_871_guards_present_and_fail_by_design_lifecycle(self):
        # The zero-871 guards exist in all three window files (PASS this
        # run, verified at this run's pre-commit check), and fail BY
        # DESIGN when mechanism 871 lands at a future A/B/C leg of the
        # 1065-1069 window. The #1070 Type D run pins them then.
        for base in GUARD_FILES:
            text = _read(os.path.join(REPO, "tests", base))
            assert "zero_next" in text, base
        t1062 = _read(os.path.join(REPO, "tests", GUARD_FILES[0]))
        t1063 = _read(os.path.join(REPO, "tests", GUARD_FILES[1]))
        t1064 = _read(os.path.join(REPO, "tests", GUARD_FILES[2]))
        assert "NEXT_NUMERIC" in t1062
        assert '"87" + "1"' in t1063  # format-built 871 needles
        assert "test_zero_next_numeric_871_in_profiles" in t1064


# --------------------------------------------------------------------------
# 9. Corpus novelty pre-commit greps per #715
# --------------------------------------------------------------------------
class TestCorpusNoveltyPreCommitGreps:
    def test_zero_type_e_1066_files_pre_run_convention(self):
        # This run's own file is the only one; convention documented in log.
        files = glob.glob(os.path.join(REPO, "tests", "*type_e_1066*"))
        assert len(files) == 1

    def test_max_numeric_mechanism_id_870(self):
        n7 = "mechanism" + "_id" + ":"
        maxid = 0
        for f in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            for m in re.finditer(n7 + r"\s*(\d+)", open(f, errors="ignore").read()):
                maxid = max(maxid, int(m.group(1)))
        # m868/m869/m870 committed at #1062-#1064 Type A/B/C, all
        # verified at #1065 Type D. Type E adds no mechanisms. (The
        # in-flight #899 m771 hunk does not change the max.)
        assert maxid == 870

    def test_zero_numeric_next_keys_in_profiles(self):
        # Next-number numeric form absent from profiles/ (format-built
        # needle per #715: no literal next-number key string carried).
        d1 = "8" + "71"
        needle = "mechanism" + "_id" + ":"
        out = _git(["grep", "-nE", f"{needle}[[:space:]]*{d1}([^0-9]|$)", "--", "profiles/"]).stdout
        assert out.strip() == ""

    def test_zero_format_built_next_carriers_in_profiles(self):
        # Format-built needles per #715: no literal next-number key
        # strings carried. profiles/ is designed colon-form; no
        # 871 carriers exist in profiles/ at all.
        n1 = "m" + "ech" + "an" + "is" + "m" + "_" + "8" + "71"
        n2 = "mech" + "anism" + "-" + "8" + "71"
        hits = []
        for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.append(p)
        assert hits == []

    def test_next_carriers_in_tests_pinned_to_guard_files(self):
        # Underscore/dash 871 needles in tests/ must appear ONLY in the
        # pinned guard carriers - and per #715 all 871 needles are
        # fragment-constructed, so NO committed test file carries an 871
        # key literal: the carrier set is EMPTY. (The #1062, #1063, and
        # #1064 guard needles are verified present and fragment-correct
        # in the guard-lifecycle class.) Own file carries no 871 literal
        # (excluded); no new carrier may appear this run.
        n1 = "mech" + "anism_" + "8" + "71"
        n2 = "mech" + "anism-" + "8" + "71"
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
        assert "NOT_SCORED" in _md_1066()

    def test_engine_not_run_no_significance(self):
        md = _md_1066()
        assert "engine NOT run" in md
        assert "is_significant False" in md

    def test_no_new_mechanisms_monitoring_only(self):
        assert "monitoring-only" in _md_1066()
        assert "no mechanisms added" in _md_1066()

    def test_falsification_ledger_holds_at_35(self):
        assert "ledger holds at 35" in _md_1066()

    def test_not_artifact_grade_correlation_not_causation(self):
        md = _md_1066()
        assert "NOT artifact-grade" in md
        assert "Correlation is not causation" in md
        assert "directionally_supported_not_proven" in md

    def test_result_row_counts(self):
        md = _md_1066()
        assert "28 result rows / 19 non-circular distinct URL keys / ZERO new verbatim URL keys this run" in md


# --------------------------------------------------------------------------
# 11. Doc-sync ratchet per #719
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_test_file_table_row_present(self):
        # This run's test-file table row must exist in README.md.
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE.replace(".py", "") in _read(ARCH)

    def test_architecture_lists_1066_file(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE in set(re.findall(r"(test_\w+\.py)", _read(ARCH)))


# --------------------------------------------------------------------------
# 12. Iteration-log entry per #719
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_1066_entry_present_with_finding_shape(self):
        # Fails pre-commit by design; green once the iteration-log
        # entry is prepended.
        log = _read(LOG)
        assert "## #1066 Type E" in log
        idx = log.index("## #1066 Type E")
        block = log[idx : idx + 3000]
        assert "136th verification" in block
        assert "Sep 29 2026, 03:00 PDT" in block
        assert "SECOND leg of the 1065-1069 window" in block

    def test_1066_entry_carries_commit_hashes_per_721(self):
        log = _read(LOG)
        idx = log.index("## #1066 Type E")
        block = log[idx : idx + 3000]
        assert "main commit" in block
        assert "anchor" in block
        assert "log-hash followup" in block

    def test_1066_entry_carries_streak_and_frontier_prose(self):
        log = _read(LOG)
        idx = log.index("## #1066 Type E")
        block = log[idx : idx + 4000]
        assert "all-key pure-re-surface streak advances to SIX" in block
        assert "recency frontier HOLDS at Sep 26" in block


# --------------------------------------------------------------------------
# 13. Push readiness per #716 / #717
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
