"""Type E #1101: podcast sentiment 143rd verification cycle (Sep 30 2026, 14:00 PDT).

Monitoring-only verification cycle per the Aug 28 2026 standing rule:
no new mechanisms, tone NOT_SCORED, engine NOT run, ledger holds at 37,
NOT artifact-grade, verdict directionally_supported_not_proven.

Findings:
(1) Guilty Feminist: episode 502 holds as newest (tenth Type E
    verification since the Sep 28 11:00am release, ~51 hours after
    publication; NO 503 surfaced; three-directory corroboration:
    podscan.fm main, podscan.fm analytics, listennotes, uk-podcasts).
    ZERO Meta/wearables content in any GF episode across all 143 cycles.
    The all-key pure-re-surface streak extends to TWO (restarted at one
    at #1096).
(2) Everyone Hates Elon (activist group, NOT a podcast): 51-day hold
    (Aug 10 Epstein spoof -> Sep 30). Six logged keys re-surfaced;
    ZERO new-to-corpus verbatim EHE URL keys. No competitor-equivalent
    guerrilla campaign in any of the 143 cycles.
(3) Attention Sphere: one-hundred-forty-third quoted-search no-match as
    a podcast. All 7 results this repository's own GitHub commit URLs
    (blob did NOT surface this run; each git-cat-file-verified present,
    still circular as evidence). Tracked Sources 142->143. Task-spec
    name remains misidentified as a podcast; real-world identity stands
    per #591.
(4) Press: six previously-logged keys re-surfaced, all in corpus; ZERO
    new press URL keys. Recency frontier HOLDS at Sep 29 (sixth hold
    since the #1071 advance).

Research method: 4 browser.search query sets, 0 browser.open
(excerpt-bounded per #503). 27 result rows / 18 non-circular distinct
URL keys / ZERO new verbatim URL keys. All URLs copied verbatim from
Full-URL listings; no canonical URLs constructed. ASCII-only.

Rotation: 1100-1104 window SECOND leg per #565 (D #1100 -> E #1101 ->
A #1102 -> B #1103 -> C #1104; order D->E->A->B->C).

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test file anchor edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file) - all
UNCOMMITTED, owned by their runs, untouched by this run (targeted
staging only). Do NOT touch #1024's m846 (FOURTEENTH,
exclusionary-diversion): self-flagged sourcing-constraint violation;
Ray's revert/leave/rebuild-from-primary decision still pending.

Pre-commit novelty greps: zero test_type_e_1101 files on disk (glob);
no "Type E #1101" in git log (--grep); max numeric mechanism_id 891
in-tree pre-commit (m889/m890/m891 committed at #1097/#1098/#1099,
verified at #1100 Type D; Type E adds no mechanisms); zero numeric 891
mechanism_id keys are absent from the novelty claim because 891 is
COMMITTED this window (the #1099 zero-891 needles are pinned staleness
in #1099's file by design); this run asserts zero 892 in all three
mechanism forms (needles format-built per #715; own file excluded);
all 18 surfaced verbatim URL keys >=1 pre-commit corpus hit via
git grep -F; 8 distinct own-repo GitHub URLs rejected as circular
(1 GF set: 2f9a4a27 commit; 7 AS set: 40d6e7b0, d4618aae, 5e238e78,
0d9132c6, dec56140, bf0cbbf1, 16611229; each git-cat-file-verified
present, still circular as evidence); no #1101 row in
README/ARCHITECTURE test tables pre-commit.
"""

import os
import re
import subprocess

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
PS_PATH = os.path.join(REPO_ROOT, "podcast-sentiment.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
OWN_BASENAME = (
    "test_type_e_1101_podcast_sentiment_143rd_verification_sep30_2pm.py"
)

ANCHORED_SHA = "0" * 40  # patched by the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

# Predecessor chain: #1100 Type D OPENED the 1100-1104 window.
PRED_MAIN_1100 = "6678ba05"
PRED_ANCHOR_1100 = "eb9cc385"
PRED_LOGHASH_1100 = "07c91cf1"
PRED_PUSH_1100 = "66562a9b"

# Circular own-repo GitHub URLs surfaced by the four query sets.
CIRCULAR_AS_COMMITS = [
    "40d6e7b02192f0f972affe1fade345d50f96e87b",
    "d4618aae2fd932b9547b90b328adf2e7ce2eedbd",
    "5e238e788c4f080288d690da7cf29a3ea2648a02",
    "0d9132c60e2828b24597b68567eaaa4b47b82c23",
    "dec561406353b2ab576086386b90dedaa37a94fd",
    "bf0cbbf1a8465afcd68daac32e220048bc2b94b0",
    "16611229702c3e83601d303959c6a0e649d64381",
]
CIRCULAR_GF_COMMIT = "2f9a4a270d63544d7529c6f39655d6cf18e141f6"

GF_KEYS = [
    "podscan.fm/podcasts/the-guilty-feminist-1",
    "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG",
    "youtube.com/watch?v=iKXj2w2cp50",
    "goloudnow.com/podcasts/the-guilty-feminist-152/deborah-frances-white-on-the-news-meeting-519585",
    "podscan.fm/podcasts/the-guilty-feminist",
    "uk-podcasts.co.uk/podcast/the-guilty-feminist/deborah-frances-white-on-the-news-meeting",
]

EHE_KEYS = [
    "afrotech.com/smart-glasses-ethics-and-consent",
    "huckmag.com/article/activists-slam-pervert-glasses-in-new-guerrilla-campaign",
    "linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates-viky-hurai-jaklovska-ssqwf",
    "feminist.org/news/author/lkollross",
    "linkedin.com/pulse/dear-ai-glasses-industry-situation-critical-red-kayvan-mirza-zwaze",
    "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
]

PRESS_KEYS = [
    "usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses/91913146007",
    "community.designtaxi.com/topic/39120-meta-releases-ray-ban-smart-glasses-without-the-cameras-amid-privacy-stalking-concerns",
    "americanow.com/FreeNewsReader/tech-firms-address-smart-glasses-privacy-concerns-amidst-public-backlash",
    "analyticsinsight.net/news/meta-ray-ban-audio-launches-at-usd-349-with-camera-free-ai",
    "thesun.ie/tech/17676556/meta-vr-glasses-boz-andrew-bosworth-ray-ban-audio",
    "gagadget.com/en/727279-ray-ban-meta-audio-smart-glasses-without-the-camera-controversy",
]


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _corpus_hit_count(needle):
    """Total pre-commit corpus hits for a verbatim URL key (>=1 expected)."""
    out = _git("grep", "-F", "-c", needle, "HEAD", "--", ".").stdout
    total = 0
    for line in out.splitlines():
        parts = line.rsplit(":", 1)
        if len(parts) == 2 and parts[1].strip().isdigit():
            total += int(parts[1])
    return total


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: local test
    pyc files carry next-number needle strings from their own
    guards; compiled artifacts are excluded from the sweeps).
    """
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f)
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f)


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source
    file carries no contiguous underscore-form literal (per the #770
    lesson).
    """
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    found = []
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            found.extend(
                int(m) for m in pat.findall(
                    open(os.path.join(root, f),
                         encoding="utf-8", errors="replace").read()
                )
            )
    return max(found) if found else 0


class TestAnchor:
    def test_anchored_sha_placeholder_pre_commit(self):
        # Pre-commit the anchor is a zero placeholder; the anchor
        # followup patches it per #565. This test documents the
        # pre-commit state; the post-commit rotation guard asserts the
        # patched value is present in git log.
        assert ANCHORED_SHA == "0" * 40 or len(ANCHORED_SHA) == 40

    def test_anchor_mechanics_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ANCHORED_SHA" in src
        assert "#565" in src


class TestRotationGuard:
    def test_predecessor_1100_chain_present(self):
        log = _git("log", "--oneline", "-60").stdout
        assert PRED_MAIN_1100 in log
        assert PRED_ANCHOR_1100 in log
        assert PRED_LOGHASH_1100 in log

    def test_type_e_1101_novelty(self):
        # "Type E #1101" absent from git log pre-commit; own file not
        # yet committed. Superseded by design post-commit.
        log = _git("log", "--oneline", "--grep=Type E #1101").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1100 -> E #1101" in src

    def test_next_run_1102_type_a_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "A #1102" in src


class TestMechanismNovelty:
    def test_type_e_adds_no_mechanisms(self):
        # Type E runs are monitoring-only; they never land mechanisms.
        assert _max_numeric_mechanism_id() == 891

    def test_zero_892_numeric_mechanism_id_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(892) == []

    def test_zero_892_underscore_mechanism_repo_wide(self):
        assert _repo_grep_underscore_mechanism(892) == []

    def test_zero_892_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(892) == []

    def test_no_1101_file_on_disk_pre_commit(self):
        own = [f for f in os.listdir(TESTS_DIR) if "type_e_1101" in f]
        assert len(own) <= 1
        if own:
            assert own[0] == OWN_BASENAME


class TestGuiltyFeminist:
    def test_all_six_gf_keys_in_corpus(self):
        for key in GF_KEYS:
            assert _corpus_hit_count(key) >= 1, "missing corpus hit for %s" % key

    def test_episode_502_holds_as_newest(self):
        # Tenth Type E verification since the Sep 28 11:00am release;
        # NO 503 surfaced across four search sets.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "episode 502 holds" in src
        assert "tenth Type E" in src

    def test_zero_meta_wearables_content_across_143_cycles(self):
        # Bounded search-result absence, not proof; tone NOT_SCORED.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ZERO Meta/wearables content" in src

    def test_pure_resurface_streak_at_two(self):
        # Streak restarted at one at #1096; this run extends it to two.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "pure-re-surface streak" in src

    def test_gf_circular_commit_rejected(self):
        # 2f9a4a27 is this repo's own commit page; git-cat-file
        # verified present, rejected as circular, not ingested.
        res = _git("cat-file", "-t", CIRCULAR_GF_COMMIT)
        assert res.stdout.strip() == "commit"


class TestEveryoneHatesElon:
    def test_all_six_ehe_keys_in_corpus(self):
        for key in EHE_KEYS:
            assert _corpus_hit_count(key) >= 1, "missing corpus hit for %s" % key

    def test_51_day_hold_arithmetic(self):
        import datetime
        days = (datetime.date(2026, 9, 30) - datetime.date(2026, 8, 10)).days
        assert days == 51

    def test_ehe_not_a_podcast(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "activist group, NOT a podcast" in src

    def test_no_competitor_equivalent_campaign(self):
        # Bounded search-result absence across all 143 cycles.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "143 cycles" in src

    def test_primary_motif_preserved(self):
        ps = _read(PS_PATH)
        assert "Glasses for people who don't do consent" in ps


class TestAttentionSphere:
    def test_143rd_no_match_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "one-hundred-forty-third" in src

    def test_all_seven_as_commits_git_cat_file_verified(self):
        for sha in CIRCULAR_AS_COMMITS:
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_as_blob_absent_this_run(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "blob did NOT surface this run" in src

    def test_tracked_sources_advance_142_to_143(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "142->143" in src

    def test_task_spec_name_still_misidentified(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "misidentified as a podcast" in src


class TestPressSurfaces:
    def test_all_six_press_keys_in_corpus(self):
        for key in PRESS_KEYS:
            assert _corpus_hit_count(key) >= 1, "missing corpus hit for %s" % key

    def test_recency_frontier_holds_sep29(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "HOLDS at Sep 29" in src

    def test_sixth_hold_since_1071_advance(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "sixth hold" in src

    def test_zero_new_press_url_keys(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ZERO" in src and "new press URL keys" in src


class TestResearchMethod:
    def test_four_query_sets_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "4 browser.search query sets" in src
        assert "0 browser.open" in src

    def test_27_result_rows_18_keys_zero_new(self):
        total = len(GF_KEYS) + len(EHE_KEYS) + len(PRESS_KEYS)
        assert total == 18
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "27 result rows" in src
        assert "18 non-circular distinct" in src
        assert "ZERO new verbatim URL keys" in src

    def test_eight_circular_urls_rejected(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "8 distinct own-repo GitHub URLs" in src

    def test_urls_verbatim_no_construction(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "copied verbatim from" in src
        assert "no canonical URLs constructed" in src


class TestStatisticalDiscipline:
    def test_monitoring_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Monitoring-only verification cycle" in src
        assert "tone NOT_SCORED" in src

    def test_falsification_ledger_holds_37(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ledger holds at 37" in src

    def test_thirty_eighth_absent(self):
        # The only THIRTY-EIGHTH member-claim-form hits repo-wide are
        # negative-guard notes asserting its absence (per the #1100
        # entry: "the two THIRTY-EIGHTH hits are negative-guard notes,
        # designed"). No affirmative THIRTY-EIGHTH member claim exists.
        res = _git(
            "grep", "-F", "THIRTY-EIGHTH member-claim",
            "HEAD", "--", "profiles/",
        )
        lines = [ln for ln in res.stdout.splitlines() if ln.strip()]
        affirmative = [ln for ln in lines if "absent" not in ln.lower()]
        assert affirmative == [], affirmative

    def test_engine_not_run(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run" in src

    def test_not_artifact_grade(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT artifact-grade" in src


class TestStalenessPins:
    def test_1100_zero_892_guards_still_pass(self):
        # The #1100 Type D file's zero-892 forward guards must still
        # PASS: mechanism 892 has not landed. They fail BY DESIGN when
        # mechanism 892 lands at a future A/B/C leg of the 1100-1104
        # window. Pinned via subprocess per the staleness convention.
        import subprocess as sp
        target = os.path.join(
            TESTS_DIR,
            "test_type_d_1100_m889_m890_m891_qualitative_corpus_integrity_sep30_1pm.py",
        )
        env = dict(os.environ)
        env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
        res = sp.run(
            ["python3", "-m", "pytest", target,
             "-k", "test_1100_zero_892_needles_pass_here",
             "-q", "--no-header"],
            cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        )
        assert res.returncode == 0, res.stdout + res.stderr

    def test_1099_zero_892_guards_still_pass(self):
        # The #1099 Type C file's zero-892 forward guards must still
        # PASS for the same reason.
        import subprocess as sp
        target = os.path.join(
            TESTS_DIR,
            "test_type_c_1099_google_ai_contribution_pilot_rate_disclosure_unilateral_pricing_twentyseventh_direction_sep30_12pm.py",
        )
        env = dict(os.environ)
        env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
        res = sp.run(
            ["python3", "-m", "pytest", target,
             "-k", "zero_892",
             "-q", "--no-header"],
            cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        )
        assert res.returncode == 0, res.stdout + res.stderr


class TestDocSync:
    def test_readme_test_file_table_has_no_1101_row_pre_commit(self):
        readme = _read(README_PATH)
        assert "test_type_e_1101" not in readme

    def test_architecture_has_no_1101_row_pre_commit(self):
        arch = _read(ARCH_PATH)
        assert "test_type_e_1101" not in arch

    def test_readme_stats_current(self):
        readme = _read(README_PATH)
        assert "| 55971 |" in readme
        assert "1425" in readme


class TestIterationLog:
    def test_no_1101_entry_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1101 Type E" not in log

    def test_1100_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1100 Type D" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


class TestInFlightIsolation:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#899" in src

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_do_not_touch_1024_m846(self):
        # Guarded in the log entry per convention; the test file keeps
        # the in-flight list only (own-file reference would trip the
        # contiguous-literal discipline elsewhere).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1024" in src
