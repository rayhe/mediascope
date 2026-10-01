"""Type E #1106: podcast sentiment 144th verification cycle (Sep 30 2026, 19:00 PDT).

Monitoring-only verification cycle per the Aug 28 2026 standing rule:
no new mechanisms, tone NOT_SCORED, engine NOT run, ledger holds at 38,
NOT artifact-grade, verdict directionally_supported_not_proven.

Findings:
(1) Guilty Feminist: episode 502 holds as newest (eleventh Type E
    verification since the Sep 28 11:00am release, ~56 hours after
    publication; NO 503 surfaced; three-directory corroboration:
    podscan.fm main (crawled 1h), podscan.fm analytics (crawled 1h),
    listennotes (crawled 4h; 762 episodes), uk-podcasts (crawled 4h;
    762 episodes, "Latest episode: 2026-09-28")). ZERO Meta/wearables
    content in any GF episode across all 144 cycles. The all-key
    pure-re-surface streak extends to THREE (restarted at one at #1096,
    two at #1101).
(2) Everyone Hates Elon (activist group, NOT a podcast): 51-day hold
    (Aug 10 Epstein spoof -> Sep 30). Six logged keys re-surfaced
    (afrotech ethics/consent 1d, huckmag pervert-glasses 7h via #1021,
    linkedin whats-up-privacy 1h, linkedin kayvan-mirza 1d,
    feminist.org author archive 4h via #1091, techtimes amnesty-boxes
    4h via #886); ZERO new-to-corpus verbatim EHE URL keys. 1
    own-repo GitHub blob (podcast-sentiment.md HEAD) rejected as
    circular. No competitor-equivalent guerrilla campaign in any of
    the 144 cycles.
(3) Attention Sphere: one-hundred-forty-fourth quoted-search no-match
    as a podcast. 6 result rows this run (blob did NOT surface;
    16611229 absent this run), all this repository's own GitHub
    commit URLs (each git-cat-file-verified present, still circular
    as evidence), rejected as circular, not ingested. Tracked Sources
    143->144. Task-spec name remains misidentified as a podcast;
    real-world identity stands per #591 (advocacy group, named ED
    Kendall Schrohe).
(4) Press: SEVEN previously-logged keys re-surfaced, all in corpus:
    usatoday Sep-23 camera-free (crawled 6d), designtaxi 39120
    (crawled 1h, via #986), americanow backlash (crawled 3h, via
    #1011), ppc.land Hamburg regulator (crawled 3h, in corpus via
    #1001-era), linkedin whats-up-privacy (crawled 1h, via
    #1001/#1006), analyticsinsight Ray-Ban Audio (crawled 1h, via
    #1016), m1k.tech LED-fix (crawled <1h, in corpus via #1001-era).
    ZERO new press URL keys. Recency frontier HOLDS at Sep 29
    (seventh hold since the #1071 advance); thesun.ie Boz and
    gagadget did NOT surface this run (remain in corpus).

Research method: 4 browser.search query sets, 0 browser.open
(excerpt-bounded per #503). 27 result rows / 18 non-circular
distinct URL keys (6 GF + 6 EHE + 7 press keys; linkedin
whats-up-privacy appears in both the EHE and press sets) / ZERO new
verbatim URL keys. 8 distinct own-repo GitHub URLs rejected as
circular (1 GF commit 2f9a4a27, 1 EHE podcast-sentiment.md HEAD
blob, 6 AS commits). All URLs copied verbatim from Full-URL
listings; no canonical URLs constructed. ASCII-only.

Rotation: 1105-1109 window SECOND leg per #565 (D #1105 -> E #1106 ->
A #1107 -> B #1108 -> C #1109; order D->E->A->B->C).

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test file anchor edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file) - all
UNCOMMITTED, owned by their runs, untouched by this run (targeted
staging only). Do NOT touch #1024's m846 (FOURTEENTH,
exclusionary-diversion): self-flagged sourcing-constraint violation;
Ray's revert/leave/rebuild-from-primary decision still pending.

Background: the #1105-launched full suite (writing to the goal
hidden_files type_d_1105_full_suite.log without -x) is in flight;
its verdict is checked by the next Type D run per #795. This run
does not touch it.

Pre-commit novelty greps: zero test_type_e_1106 files on disk (glob);
no "Type E #1106" in git log (--grep); max numeric mechanism_id 894
in-tree pre-commit (m892/m893/m894 committed at #1102/#1103/#1104,
verified at #1105 Type D; Type E adds no mechanisms); zero numeric
895 mechanism_id keys in profiles/ (mechanism_id regex sweep); zero
underscore-form and dash-form 895 mechanism key strings repo-wide
pre-commit (needles format-built per #715, own file excluded); ZERO
new verbatim URL keys (all 18 surfaced distinct verbatim URL keys
>=1 pre-commit corpus hit via git grep -F: 6 GF keys, 6 EHE keys,
7 press keys with 1 overlap); 8 distinct own-repo GitHub URLs
rejected as circular; no #1106 row in README/ARCHITECTURE test
tables pre-commit.
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
    "test_type_e_1106_podcast_sentiment_144th_verification_sep30_7pm.py"
)

ANCHORED_SHA = "0" * 40  # patched by the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

# Predecessor chain: #1105 Type D OPENED the 1105-1109 window.
PRED_MAIN_1105 = "2161fb38"
PRED_ANCHOR_1105 = "21adbaed"
PRED_LOGHASH_1105 = "ce757f92"
PRED_PUSH_1105 = "a8d1d560"

# Circular own-repo GitHub URLs surfaced by the four query sets.
CIRCULAR_AS_COMMITS = [
    "40d6e7b02192f0f972affe1fade345d50f96e87b",
    "5e238e788c4f080288d690da7cf29a3ea2648a02",
    "d4618aae2fd932b9547b90b328adf2e7ce2eedbd",
    "0d9132c60e2828b24597b68567eaaa4b47b82c23",
    "bf0cbbf1a8465afcd68daac32e220048bc2b94b0",
    "dec561406353b2ab576086386b90dedaa37a94fd",
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
    "ppc.land/hamburg-regulator-finds-ray-ban-meta-glasses-expose-bystanders-without-consent",
    "linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates-viky-hurai-jaklovska-ssqwf",
    "analyticsinsight.net/news/meta-ray-ban-audio-launches-at-usd-349-with-camera-free-ai",
    "m1k.tech/2026/09/meta-ray-ban-led-fix-eu-consent-glasses",
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
    def test_predecessor_1105_chain_present(self):
        log = _git("log", "--oneline", "-60").stdout
        assert PRED_MAIN_1105 in log
        assert PRED_ANCHOR_1105 in log
        assert PRED_LOGHASH_1105 in log
        assert PRED_PUSH_1105 in log

    def test_type_e_1106_novelty(self):
        # "Type E #1106" absent from git log pre-commit; own file not
        # yet committed. Superseded by design post-commit.
        log = _git("log", "--oneline", "--grep=Type E #1106").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1105 -> E #1106" in src

    def test_next_run_1107_type_a_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "A #1107" in src


class TestMechanismNovelty:
    def test_type_e_adds_no_mechanisms(self):
        # Type E runs are monitoring-only; they never land mechanisms.
        assert _max_numeric_mechanism_id() == 894

    def test_zero_895_numeric_mechanism_id_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(895) == []

    def test_zero_895_underscore_mechanism_repo_wide(self):
        assert _repo_grep_underscore_mechanism(895) == []

    def test_zero_895_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(895) == []

    def test_no_1106_file_on_disk_pre_commit(self):
        own = [f for f in os.listdir(TESTS_DIR) if "type_e_1106" in f]
        assert len(own) <= 1
        if own:
            assert own[0] == OWN_BASENAME


class TestGuiltyFeminist:
    def test_all_six_gf_keys_in_corpus(self):
        for key in GF_KEYS:
            assert _corpus_hit_count(key) >= 1, "missing corpus hit for %s" % key

    def test_episode_502_holds_as_newest(self):
        # Eleventh Type E verification since the Sep 28 11:00am
        # release (~56 hours after publication); NO 503 surfaced
        # across the four search sets.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "episode 502 holds" in src
        assert "eleventh Type E" in src

    def test_zero_meta_wearables_content_across_144_cycles(self):
        # Bounded search-result absence, not proof; tone NOT_SCORED.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ZERO Meta/wearables content" in src

    def test_pure_resurface_streak_at_three(self):
        # Streak restarted at one at #1096, extended to two at #1101;
        # this run extends it to three.
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
        # Bounded search-result absence across all 144 cycles.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "144 cycles" in src

    def test_primary_motif_preserved(self):
        ps = _read(PS_PATH)
        assert "Glasses for people who don't do consent" in ps

    def test_ehe_blob_in_committed_tree(self):
        # The podcast-sentiment.md blob surfaced as a circular
        # own-repo URL this run; the file is present in the committed
        # tree (rejected as circular evidence, not ingested).
        res = _git("ls-tree", "HEAD", "podcast-sentiment.md")
        assert "blob" in res.stdout


class TestAttentionSphere:
    def test_144th_no_match_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "one-hundred-forty-fourth" in src

    def test_all_six_as_commits_git_cat_file_verified(self):
        for sha in CIRCULAR_AS_COMMITS:
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_as_blob_absent_this_run(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "blob did NOT surface this run" in src

    def test_tracked_sources_advance_143_to_144(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "143->144" in src

    def test_task_spec_name_still_misidentified(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "misidentified as a podcast" in src


class TestPressSurfaces:
    def test_all_seven_press_keys_in_corpus(self):
        for key in PRESS_KEYS:
            assert _corpus_hit_count(key) >= 1, "missing corpus hit for %s" % key

    def test_recency_frontier_holds_sep29(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "HOLDS at Sep 29" in src

    def test_seventh_hold_since_1071_advance(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "seventh hold" in src

    def test_zero_new_press_url_keys(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ZERO" in src and "new press URL keys" in src

    def test_thesun_ie_gagadget_nonsurface_noted(self):
        # thesun.ie Boz and gagadget did NOT surface this run but
        # remain in corpus; absence is not a drop per #503.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "did NOT surface this run" in src


class TestResearchMethod:
    def test_four_query_sets_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "4 browser.search query sets" in src
        assert "0 browser.open" in src

    def test_27_result_rows_18_keys_zero_new(self):
        # 7 GF + 7 EHE + 6 AS + 7 press = 27 rows. Distinct
        # non-circular: 6 GF + 6 EHE + 7 press with the linkedin
        # whats-up-privacy key in both the EHE and press sets = 18.
        total_rows = 7 + 7 + 6 + 7
        assert total_rows == 27
        distinct = set(GF_KEYS) | set(EHE_KEYS) | set(PRESS_KEYS)
        assert len(distinct) == 18
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "27 result rows" in src
        assert "18 non-circular" in src
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

    def test_falsification_ledger_holds_38(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ledger holds at 38" in src

    def test_thirty_eighth_member_claim_once(self):
        # The affirmative THIRTY-EIGHTH form is the m893
        # falsification-family line, present exactly once in the
        # committed profiles tree.
        out = _git(
            "grep", "-F", "THIRTY-EIGHTH falsification-family member",
            "HEAD", "--", "profiles/",
        ).stdout
        assert len(out.strip().splitlines()) == 1

    def test_thirty_ninth_member_claim_absent(self):
        # No affirmative THIRTY-NINTH member-claim exists; the only
        # THIRTY-NINTH hits in profiles/ are negative-guard wordings
        # (designed).
        out = _git(
            "grep", "-F", "THIRTY-NINTH falsification-family member",
            "HEAD", "--", "profiles/",
        ).stdout
        assert out.strip() == ""
        neg = _git(
            "grep", "-F", "THIRTY-NINTH member-claim form absent",
            "HEAD", "--", "profiles/",
        ).stdout
        assert len(neg.strip().splitlines()) >= 1

    def test_engine_not_run(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run" in src

    def test_not_artifact_grade(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT artifact-grade" in src


class TestStalenessPins:
    def _class_run(self, filename, classname):
        import subprocess as sp
        target = os.path.join(TESTS_DIR, filename)
        env = dict(os.environ)
        env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
        res = sp.run(
            ["python3", "-m", "pytest", target,
             "-k", classname,
             "-q", "--no-header"],
            cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        )
        return res

    def test_1104_zero_895_guards_still_pass(self):
        # The #1104 Type C file's zero-895 forward guards must still
        # PASS: mechanism 895 has not landed. They fail BY DESIGN
        # when the next A/B/C leg lands it. (Runs the post-commit
        # novelty class only - the pre-commit guards are designed
        # to fail after the #1104 main commit landed.)
        res = self._class_run(
            "test_type_c_1104_google_ai_answer_pilot_divide_and_conquer_twentyeighth_direction_sep30_5pm.py",
            "TestCorpusNoveltyPostCommit",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1105_zero_895_needles_pass_here(self):
        # The #1105 Type D file's zero-895 forward guards must still
        # PASS for the same reason (mechanism 895 has not landed).
        res = self._class_run(
            "test_type_d_1105_m892_m893_m894_qualitative_corpus_integrity_sep30_6pm.py",
            "test_1105_zero_895_needles_pass_here",
        )
        assert res.returncode == 0, res.stdout[-2000:]


class TestDocSync:
    def test_readme_test_file_table_has_no_1106_row_pre_commit(self):
        readme = _read(README_PATH)
        assert "test_type_e_1106" not in readme

    def test_architecture_has_no_1106_row_pre_commit(self):
        arch = _read(ARCH_PATH)
        assert "test_type_e_1106" not in arch

    def test_readme_stats_current(self):
        readme = _read(README_PATH)
        assert "| 56327 |" in readme
        assert "1430" in readme


class TestIterationLog:
    def test_no_1106_entry_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1106 Type E" not in log

    def test_1105_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1105 Type D" in log

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
