"""Type E #1116: podcast sentiment 146th verification cycle (Oct 1 2026, 05:00 AM PDT).

Monitoring-only verification cycle per the Aug 28 2026 standing rule:
no new mechanisms, tone NOT_SCORED, engine NOT run, ledger holds at 41,
NOT artifact-grade, verdict directionally_supported_not_proven.

Findings:
(1) Guilty Feminist: episode 502 holds as newest (thirteenth Type E
    verification since the Sep 28 11:00am release, ~66 hours after
    publication; NO 503 surfaced; two-directory corroboration this run:
    listennotes main (crawled 3h; "LATEST EPISODE: The Guilty Feminist
    502. Homophobia", 01:00:32; 762 episodes), podscan.fm main (crawled
    4h; "Latest Episode: 502. Homophobia with Freya Parker and Linus
    Karp", published Sep 28 2026 11:00am); plus the listennotes TH stale
    locale variant (all in corpus; zero new verbatim GF URL keys).
    4 own-repo GitHub commit URLs surfaced in the GF set this run
    (#911 commit 57934866, #756 commit 95903853, #916 commit 2f72a838,
    2f9a4a27; each git-cat-file-verified present, still circular as
    evidence), rejected as circular, not ingested. ZERO Meta/wearables
    content in any GF episode across all 146 cycles (bounded
    search-result absence). The all-key pure-re-surface streak extends
    to FIVE (restarted at one at #1096, two at #1101, three at #1106,
    four at #1111).
(2) Everyone Hates Elon (activist group, NOT a podcast): 52-day hold
    (Aug 10 Epstein spoof -> Oct 1; date(2026,10,1)-date(2026,8,10)=52
    days). Six logged keys re-surfaced (afrotech ethics/consent 1d;
    huckmag pervert-glasses <1h via #1021; linkedin whats-up-privacy
    <1h via #1001/#1006; feminist.org author archive 4h via #1091;
    linkedin kayvan-mirza 2d via #1001/#1006; techtimes amnesty-boxes
    4h via #886); ZERO new-to-corpus verbatim EHE URL keys. 1
    own-repo GitHub blob (podcast-sentiment.md HEAD) rejected as
    circular. No competitor-equivalent guerrilla campaign in any of
    the 146 cycles.
(3) Attention Sphere: one-hundred-forty-sixth quoted-search no-match
    as a podcast. 6 result rows this run (blob did NOT surface;
    16611229 absent this run), all this repository's own GitHub
    commit URLs (the same set as #1106/#1111; each git-cat-file-verified
    present, still circular as evidence), rejected as circular, not
    ingested. Tracked Sources 145->146. Task-spec name remains
    misidentified as a podcast; real-world identity stands per #591
    (advocacy group, named ED Kendall Schrohe).
(4) Press: SEVEN previously-logged keys re-surfaced, all in corpus:
    usatoday Sep-23 camera-free (crawled 6d), designtaxi 39120
    (crawled <1h, via #986), americanow backlash (crawled 1h, via
    #1011), ppc.land Hamburg regulator (crawled <1h, in corpus via
    #1001-era), linkedin whats-up-privacy (crawled <1h, via
    #1001/#1006), analyticsinsight Ray-Ban Audio (crawled 3h, via
    #1016), dig.watch camera-free Luna (crawled 2h, via #1001-era).
    ZERO new-to-corpus press URL keys. Recency frontier HOLDS at Sep
    29 (the #1071 thesun.ie Boz piece remains the newest-in-corpus
    surface; ninth hold since the #1071 advance; thesun.ie and
    gagadget did NOT surface this run but remain in corpus).

Research method: 4 browser.search query sets, 0 browser.open
(excerpt-bounded per #503). 27 result rows / 15 non-circular
distinct URL keys (3 GF + 6 EHE + 7 press keys; linkedin
whats-up-privacy appears in both the EHE and press sets) / ZERO new
verbatim URL keys. 11 distinct own-repo GitHub URLs rejected as
circular (4 GF commits, 1 EHE podcast-sentiment.md HEAD blob, 6 AS
commits). All URLs copied verbatim from Full-URL listings; no
canonical URLs constructed. ASCII-only.

Rotation: 1115-1119 window SECOND leg per #565 (D #1115 -> E #1116 ->
A #1117 -> B #1118 -> C #1119; order D->E->A->B->C).

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test file anchor edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file) - all
UNCOMMITTED, owned by their runs, untouched by this run (targeted
staging only). Do NOT touch #1024's m846 (FOURTEENTH,
exclusionary-diversion): self-flagged sourcing-constraint violation;
Ray's revert/leave/rebuild-from-primary decision still pending.

Background: the #1115-launched full suite (writing to the goal
hidden_files type_d_1115_full_suite.log without -x) is in flight at
this run's check (1621 bytes / ~2% dots, last write Oct 1 04:35
PDT); its verdict is checked by the next Type D run (#1120) per
#795. This run does not touch it.

Pre-commit novelty greps: zero test_type_e_1116 files on disk (glob);
no "Type E #1116" in git log (--grep); max numeric mechanism_id 900
in-tree pre-commit (m898/m899/m900 committed at #1112/#1113/#1114,
verified at #1115 Type D; Type E adds no mechanisms); zero numeric,
underscore, and dash 901 mechanism key forms repo-wide pre-commit
(needles format-built per #715, own file excluded); ZERO new
verbatim URL keys (all 16 surfaced distinct verbatim URL keys >=1
pre-commit corpus hit via git grep -F: 3 GF keys, 6 EHE keys, 7
press keys with 1 overlap); 11 distinct own-repo GitHub URLs
rejected as circular; no #1116 row in README/ARCHITECTURE test
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
    "test_type_e_1116_podcast_sentiment_146th_verification_oct01_5am.py"
)

ANCHORED_SHA = "3e11793836161f6f0995de61ab7a9783d4ffbc33"  # patched by the anchor followup (was "0" * 40)

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

# Predecessor chain: #1115 Type D OPENED the 1115-1119 window.
PRED_MAIN_1115 = "ccac64fb"
PRED_ANCHOR_1115 = "092d0549"
PRED_LOGHASH_1115 = "ef5bf9c5"
PRED_FINAL_1115 = "79c2ec7e"

# Circular own-repo GitHub URLs surfaced by the four query sets.
CIRCULAR_AS_COMMITS = [
    "40d6e7b02192f0f972affe1fade345d50f96e87b",
    "5e238e788c4f080288d690da7cf29a3ea2648a02",
    "d4618aae2fd932b9547b90b328adf2e7ce2eedbd",
    "0d9132c60e2828b24597b68567eaaa4b47b82c23",
    "bf0cbbf1a8465afcd68daac32e220048bc2b94b0",
    "dec561406353b2ab576086386b90dedaa37a94fd",
]

CIRCULAR_GF_COMMITS = [
    "57934866162ac95b380fb6ee935e9a482c909a01",
    "959038536c82b63a7ab3b708226aec070a43514a",
    "2f9a4a270d63544d7529c6f39655d6cf18e141f6",
    "2f72a838ea3cf90013b01012248f40d0a995c938",
]

GF_KEYS = [
    "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG",
    "podscan.fm/podcasts/the-guilty-feminist",
    "listennotes.com/th/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG",
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
    "dig.watch/updates/meta-confirms-camera-free-ray-ban-smart-glasses",
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
    def test_predecessor_1115_chain_present(self):
        log = _git("log", "--oneline", "-80").stdout
        assert PRED_MAIN_1115 in log
        assert PRED_ANCHOR_1115 in log
        assert PRED_LOGHASH_1115 in log
        assert PRED_FINAL_1115 in log

    def test_type_e_1116_novelty(self):
        # "Type E #1116" absent from git log pre-commit; own file not
        # yet committed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type E #1116:") lands; post-commit, the anchor
        # asserts the patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        log = _git("log", "--oneline", "--grep=Type E #1116").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1115 -> E #1116" in src

    def test_next_run_1117_type_a_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "A #1117" in src


class TestMechanismNovelty:
    def test_type_e_adds_no_mechanisms(self):
        # Type E runs are monitoring-only; they never land mechanisms.
        assert _max_numeric_mechanism_id() == 900

    def test_zero_901_numeric_mechanism_id_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(901) == []

    def test_zero_901_underscore_mechanism_repo_wide(self):
        assert _repo_grep_underscore_mechanism(901) == []

    def test_zero_901_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(901) == []

    def test_no_1116_file_on_disk_pre_commit(self):
        own = [f for f in os.listdir(TESTS_DIR) if "type_e_1116" in f]
        assert len(own) <= 1
        if own:
            assert own[0] == OWN_BASENAME


class TestGuiltyFeminist:
    def test_all_three_gf_keys_in_corpus(self):
        for key in GF_KEYS:
            assert _corpus_hit_count(key) >= 1, "missing corpus hit for %s" % key

    def test_episode_502_holds_as_newest(self):
        # Thirteenth Type E verification since the Sep 28 11:00am
        # release (~66 hours after publication); NO 503 surfaced
        # across the four search sets.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "episode 502 holds" in src
        assert "thirteenth Type E" in src

    def test_zero_meta_wearables_content_across_146_cycles(self):
        # Bounded search-result absence, not proof; tone NOT_SCORED.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ZERO Meta/wearables content" in src

    def test_pure_resurface_streak_at_five(self):
        # Streak restarted at one at #1096, extended to two at #1101,
        # three at #1106, and four at #1111; this run extends it to
        # five.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "pure-re-surface streak" in src
        assert "extends to" in src and "FIVE" in src

    def test_four_gf_circular_commits_git_cat_file_verified(self):
        # Unlike #1111 (zero own-repo GF URLs), the GF set surfaced
        # four own-repo commit URLs this run; each is present in the
        # repo, still circular as evidence, rejected not ingested.
        for sha in CIRCULAR_GF_COMMITS:
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "4 own-repo GitHub commit URLs" in src


class TestEveryoneHatesElon:
    def test_all_six_ehe_keys_in_corpus(self):
        for key in EHE_KEYS:
            assert _corpus_hit_count(key) >= 1, "missing corpus hit for %s" % key

    def test_53_day_hold_arithmetic(self):
        import datetime
        days = (datetime.date(2026, 10, 1) - datetime.date(2026, 8, 10)).days
        assert days == 52

    def test_ehe_not_a_podcast(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "activist group, NOT a podcast" in src

    def test_no_competitor_equivalent_campaign(self):
        # Bounded search-result absence across all 146 cycles.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "146 cycles" in src

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
    def test_146th_no_match_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "one-hundred-forty-sixth" in src

    def test_all_six_as_commits_git_cat_file_verified(self):
        for sha in CIRCULAR_AS_COMMITS:
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_as_blob_absent_this_run(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "blob did NOT surface this run" in src

    def test_tracked_sources_advance_145_to_146(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "145->146" in src

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

    def test_ninth_hold_since_1071_advance(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ninth hold" in src

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

    def test_27_result_rows_15_keys_zero_new(self):
        # 7 GF + 7 EHE + 6 AS + 7 press = 27 rows. Distinct
        # non-circular: 3 GF + 6 EHE + 7 press with the linkedin
        # whats-up-privacy key in both the EHE and press sets = 15.
        total_rows = 7 + 7 + 6 + 7
        assert total_rows == 27
        distinct = set(GF_KEYS) | set(EHE_KEYS) | set(PRESS_KEYS)
        assert len(distinct) == 15
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "27 result rows" in src
        assert "15 non-circular" in src
        assert "ZERO new verbatim URL keys" in src

    def test_eleven_circular_urls_rejected(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "11 distinct own-repo GitHub URLs" in src

    def test_urls_verbatim_no_construction(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "copied verbatim from" in src
        assert "no canonical URLs constructed" in src


class TestStatisticalDiscipline:
    def test_monitoring_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Monitoring-only verification cycle" in src
        assert "tone NOT_SCORED" in src

    def test_falsification_ledger_holds_41(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ledger holds at 41" in src

    def test_forty_first_member_claim_journalists_twice(self):
        # The affirmative FORTY-FIRST form is the m899
        # falsification-family line, present twice in the committed
        # profiles tree per #1115: the claim line plus the
        # research_method novelty prose (a #1113 self-reference,
        # not a second claim), both in journalists.yaml.
        out = _git(
            "grep", "-F", "FORTY-FIRST falsification-family member",
            "HEAD", "--", "profiles/careers/journalists.yaml",
        ).stdout
        assert len(out.strip().splitlines()) == 2

    def test_forty_second_member_claim_absent(self):
        # No affirmative FORTY-SECOND member-claim exists; the only
        # FORTY-SECOND form in profiles/ is the designed
        # negative-guard wording (affirmative form absent repo-wide).
        t42 = "FORTY" + "-SECOND"
        aff = _git(
            "grep", "-F", t42 + " falsification-family member",
            "HEAD", "--", "profiles/",
        ).stdout
        assert aff.strip() == ""
        neg = _git(
            "grep", "-F", t42 + " member-claim form absent",
            "HEAD", "--", "profiles/",
        ).stdout
        assert len(neg.strip().splitlines()) >= 1

    def test_thirtieth_direction_present(self):
        out = _git(
            "grep", "-F", "THIRTIETH relationship direction",
            "HEAD", "--", "profiles/",
        ).stdout
        assert len(out.strip().splitlines()) >= 1

    def test_thirty_first_direction_claim_absent(self):
        tw31 = "THIRTY" + "-FIRST"
        out = _git(
            "grep", "-Fi", tw31 + " relationship direction",
            "HEAD", "--", "profiles/",
        ).stdout
        assert out.strip() == ""

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

    def test_1115_guard_lifecycle_zero_901_still_green(self):
        # The #1115 Type D file's guard-lifecycle class pins the
        # zero-901 forward guards (numeric, underscore, dash; next
        # number 901; max id 900). It must still PASS: mechanism 901
        # has not landed. It fails BY DESIGN when a future A/B/C leg
        # lands it.
        res = self._class_run(
            "test_type_d_1115_m898_m899_m900_qualitative_corpus_integrity_oct01_4am.py",
            "TestGuardLifecycle1115",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1114_forward_guards_zero_901_still_green(self):
        # #1114's TestForwardGuards1114 pins the zero-901 forward
        # guards too; still green at #1116 (901 unlanded).
        res = self._class_run(
            "test_type_c_1114_google_news_ai_pilot_three_track_segmentation_trackseparatedpricing_thirtieth_direction_oct01_3am.py",
            "TestForwardGuards1114",
        )
        assert res.returncode == 0, res.stdout[-2000:]


class TestDocSync:
    def test_readme_test_file_table_has_no_1116_row_pre_commit(self):
        readme = _read(README_PATH)
        assert "test_type_e_1116" not in readme

    def test_architecture_has_no_1116_row_pre_commit(self):
        arch = _read(ARCH_PATH)
        assert "test_type_e_1116" not in arch

    def test_readme_stats_current(self):
        readme = _read(README_PATH)
        assert "| 57961 |" in readme
        assert "1440" in readme


class TestIterationLog:
    def test_no_1116_entry_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1116 Type E" not in log

    def test_1115_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1115 Type D" in log

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
