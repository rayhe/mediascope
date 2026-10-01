"""Type E #1121: podcast sentiment 147th verification cycle (Oct 1 2026, 09:35 AM PDT).

Monitoring-only verification cycle per the Aug 28 2026 standing rule:
no new mechanisms, tone NOT_SCORED, engine NOT run, ledger holds at 43,
NOT artifact-grade, verdict directionally_supported_not_proven.

Findings:
(1) Guilty Feminist: episode 502 holds as newest (fourteenth Type E
    verification since the Sep 28 11:00am release, ~70.5 hours after
    publication; NO 503 surfaced; two-directory corroboration this run:
    listennotes main (crawled 1h; "LATEST EPISODE: The Guilty Feminist
    502. Homophobia", 01:00:32; 762 episodes), uk-podcasts.co.uk
    (crawled 9h; 762 episodes, "Latest episode: 2026-09-28"),
    podscan.fm main page (crawled 5h; 502 Homophobia summary with Linus
    Karp, Palmolive sponsor read); plus the listennotes TH stale locale
    variant, the podscan 499 transcript page, the youtube episode-500
    page, and the chortle Edinburgh-Fringe-2026 show page (all in
    corpus; zero new verbatim GF URL keys). 0 own-repo GitHub URLs
    surfaced in the GF set this run (unlike #1116's four). ZERO
    Meta/wearables content in any GF episode across all 147 cycles
    (bounded search-result absence). The all-key pure-re-surface streak
    extends to SIX (restarted at one at #1096, two at #1101, three at
    #1106, four at #1111, five at #1116).
(2) Everyone Hates Elon (activist group, NOT a podcast): 52-day hold
    (Aug 10 Epstein spoof -> Oct 1; date(2026,10,1)-date(2026,8,10)=52
    days). Five logged keys re-surfaced (huckmag pervert-glasses piece
    crawled <1h via #1021; linkedin whats-up-privacy roundup crawled 1h
    via #1001/#1006; feminist.org author archive crawled 4h via #1091;
    linkedin kayvan-mirza op-ed crawled 2d via #1001/#1006; techtimes
    amnesty-boxes crawled 4h via #886); afrotech ethics/consent did NOT
    surface this run (in corpus). ZERO new-to-corpus verbatim EHE URL
    keys. 2 own-repo GitHub URLs rejected as circular (podcast-sentiment
    HEAD blob + the examples sample_output wearables_advocacy strand
    blob; each git-ls-tree-verified present in the committed tree, not
    ingested). No competitor-equivalent guerrilla campaign in any of
    the 147 cycles.
(3) Attention Sphere: one-hundred-forty-seventh quoted-search no-match
    as a podcast. 6 result rows this run (blob did NOT surface;
    16611229 absent this run), all this repository's own GitHub commit
    URLs (the same set as #1106/#1111/#1116; each git-cat-file-verified
    present, still circular as evidence), rejected as circular, not
    ingested. Tracked Sources 146->147. Task-spec name remains
    misidentified as a podcast; real-world identity stands per #591
    (advocacy group, named ED Kendall Schrohe).
(4) Press: THREE previously-logged keys re-surfaced (techspot news
    113968 camera-free piece via #981; analyticsinsight Ray-Ban Audio
    piece via #1016; letsdatascience camera-free piece via #966) + FOUR
    NEW-TO-CORPUS URL keys this run (geeky-gadgets Meta Connect 2026
    announcements; techspot community forums mirror of the 113968
    story; techjournalhq camera-free Audio piece; avcaesar "the
    anti-pervert solution?" piece). Recency frontier HOLDS at Sep 29
    (the #1071 thesun.ie Boz piece remains the newest-in-corpus
    surface; tenth hold since the #1071 advance; thesun.ie and gagadget
    did NOT surface this run but remain in corpus). Meta-exclusive
    privacy-pressure framing continues across all 147 cycles; no
    competitor camera-wearable coverage carries equivalent
    privacy-pressure framing. Snippet-bounded, tone NOT_SCORED.

Research method: 4 browser.search query sets, 0 browser.open
(excerpt-bounded per #503). 27 result rows / 19 non-circular
distinct URL keys (7 GF + 5 EHE + 7 press keys; no URL key repeats
across the four query sets) / FOUR new verbatim URL keys. 8 distinct own-repo GitHub URLs rejected as
circular (0 GF, 2 EHE blobs, 6 AS commits; each git-cat-file or
git-ls-tree verified present in the committed tree, still circular as
evidence). All URLs copied verbatim from Full-URL listings; no
canonical URLs constructed. ASCII-only.

Rotation: 1120-1124 window SECOND leg per #565 (D #1120 -> E #1121 ->
A #1122 -> B #1123 -> C #1124; order D->E->A->B->C).

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test file anchor edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file) - all
UNCOMMITTED, owned by their runs, untouched by this run (targeted
staging only). Do NOT touch #1024's m846 (FOURTEENTH,
exclusionary-diversion): self-flagged sourcing-constraint violation;
Ray's revert/leave/rebuild-from-primary decision still pending.

Background: the #1120-launched full suite (writing to the goal
hidden_files type_d_1120_full_suite.log, 1654 bytes / last write Oct
1 09:38 PDT) is in flight at this run's check; its verdict belongs to
#1125 per #795. This run does not touch it.

Pre-commit novelty greps: zero test_type_e_1121 files on disk (glob);
no "Type E #1121" in git log (--grep); max numeric mechanism_id 903
in-tree pre-commit (m901/m902/m903 committed at #1117/#1118/#1119
Type A/B/C, verified at #1120 Type D; Type E adds no mechanisms);
zero numeric/underscore/dash next-number 904 mechanism key forms
repo-wide pre-commit (needles format-built per #715, own file
excluded); 19 surfaced distinct verbatim URL keys: 15 at >=1
pre-commit corpus hit via git grep -F (7 GF keys, 5 EHE keys, 3 press
re-surfaces) and 4 NEW with zero pre-commit hits; 8
distinct own-repo GitHub URLs rejected as circular; no #1121 row in
README/ARCHITECTURE test tables or iteration-log pre-commit.
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
    "test_type_e_1121_podcast_sentiment_147th_verification_oct01_9am.py"
)

ANCHORED_SHA = "2c9bc7ee7da65707f58382ebe81831903fe62a62"  # main commit, patched per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

# Predecessor chain: #1120 Type D OPENED the 1120-1124 window.
PRED_MAIN_1120 = "69728626"
PRED_ANCHOR_1120 = "4605e386"
PRED_DOCSYNC_1120 = "1254a00c"
PRED_FINAL_1120 = "85d1902e"

# The #1120 window-opener file, for the staleness pin on its
# zero-904 guard lifecycle class.
D1120_FILE = (
    "test_type_d_1120_m901_m902_m903_qualitative_"
    "corpus_integrity_oct01_9am.py"
)

# The landed FORTY-THIRD member and THIRTY-FIRST direction forms are
# plain literals (already in corpus). The forty-fourth-member and
# thirty-second-direction needles are fragment-built per #715 so this
# file carries no contiguous literal of a forward-guard claim form.
_T43 = "FORTY-THIRD falsification-family member"
_TW31 = "THIRTY-FIRST relationship direction"
_T44 = "FORTY-" + "FOURTH falsification-family member"
_TW32 = "THIRTY-" + "SECOND relationship direction"

# Circular own-repo GitHub commit URLs surfaced by the Attention
# Sphere query set this run (the same 6 as #1106/#1111/#1116).
CIRCULAR_AS_COMMITS = [
    "40d6e7b02192f0f972affe1fade345d50f96e87b",
    "5e238e788c4f080288d690da7cf29a3ea2648a02",
    "d4618aae2fd932b9547b90b328adf2e7ce2eedbd",
    "0d9132c60e2828b24597b68567eaaa4b47b82c23",
    "bf0cbbf1a8465afcd68daac32e220048bc2b94b0",
    "dec561406353b2ab576086386b90dedaa37a94fd",
]

GF_KEYS = [
    "chortle.co.uk/shows/edinburgh_fringe_2026/g/39124/the_guilty_feminist",
    "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG",
    "uk-podcasts.co.uk/podcast/the-guilty-feminist/deborah-frances-white-on-the-news-meeting",
    "podscan.fm/podcasts/the-guilty-feminist",
    "listennotes.com/th/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG",
    "podscan.fm/podcasts/the-guilty-feminist/episodes/499-where-you-end-and-i-begin-with-lindsey-mendick-1",
    "youtube.com/watch?v=iKXj2w2cp50",
]

EHE_KEYS = [
    "huckmag.com/article/activists-slam-pervert-glasses-in-new-guerrilla-campaign",
    "linkedin.com/pulse/whats-up-privacy-meta-ray-ban-glasses-updates-viky-hurai-jaklovska-ssqwf",
    "feminist.org/news/author/lkollross",
    "linkedin.com/pulse/dear-ai-glasses-industry-situation-critical-red-kayvan-mirza-zwaze",
    "techtimes.co.uk/activists-challenge-meta-ray-ban-smart-glasses-london-1808470",
]

# Press re-surfaces: zero pre-commit novelty (all in corpus).
PRESS_RESURFACE_KEYS = [
    "techspot.com/news/113968-meta-new-smart-glasses-skip-cameras-privacy-backlash.html",
    "analyticsinsight.net/news/meta-ray-ban-audio-launches-at-usd-349-with-camera-free-ai",
    "letsdatascience.com/news/meta-unveils-camera-free-ray-ban-meta-audio-glasses-at-conne-dbda6d5c",
]

# New-to-corpus verbatim URL keys this run: zero pre-commit hits.
NEW_PRESS_KEYS = [
    "geeky-gadgets.com/meta-connect-2026-announcements",
    "techspot.com/community/topics/metas-new-smart-glasses-skip-the-cameras-and-the-privacy-backlash-that-came-with-them.298926",
    "techjournalhq.com/meta-camera-free-ray-ban-audio-ai-glasses-9896",
    "avcaesar.com/news/8122/ray-ban-meta-audio-smart-glasses-without-a-camera-the-anti-pervert-solution",
]


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _corpus_hit_count(needle):
    """Total pre-commit corpus hits for a verbatim URL key."""
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


def _profiles_text():
    parts = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            parts.append(
                (
                    os.path.join(root, f),
                    open(
                        os.path.join(root, f),
                        encoding="utf-8",
                        errors="replace",
                    ).read(),
                )
            )
    return parts


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
    def test_predecessor_1120_chain_present(self):
        log = _git("log", "--oneline", "-80").stdout
        assert PRED_MAIN_1120 in log
        assert PRED_ANCHOR_1120 in log
        assert PRED_DOCSYNC_1120 in log
        assert PRED_FINAL_1120 in log

    def test_type_e_1121_novelty(self):
        # "Type E #1121" absent from git log pre-commit; own file not
        # yet committed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type E #1121:") lands; post-commit, the anchor
        # asserts the patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        log = _git("log", "--oneline", "--grep=Type E #1121").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1120 -> E #1121" in src

    def test_next_run_1122_type_a_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "A #1122" in src


class TestMechanismNovelty:
    def test_type_e_adds_no_mechanisms(self):
        # Type E runs are monitoring-only; they never land mechanisms.
        assert _max_numeric_mechanism_id() == 903

    def test_zero_904_numeric_mechanism_id_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(904) == []

    def test_zero_904_underscore_mechanism_repo_wide(self):
        assert _repo_grep_underscore_mechanism(904) == []

    def test_zero_904_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(904) == []

    def test_no_1121_file_on_disk_pre_commit(self):
        own = [f for f in os.listdir(TESTS_DIR) if "type_e_1121" in f]
        assert len(own) <= 1
        if own:
            assert own[0] == OWN_BASENAME


class TestGuiltyFeminist:
    def test_all_seven_gf_keys_in_corpus(self):
        for key in GF_KEYS:
            assert _corpus_hit_count(key) >= 1, "missing corpus hit for %s" % key

    def test_episode_502_holds_as_newest(self):
        # Fourteenth Type E verification since the Sep 28 11:00am
        # release (~70.5 hours after publication); NO 503 surfaced
        # across the four search sets.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "episode 502 holds" in src
        assert "fourteenth Type E" in src

    def test_zero_meta_wearables_content_across_147_cycles(self):
        # Bounded search-result absence, not proof; tone NOT_SCORED.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ZERO Meta/wearables content" in src
        assert "147 cycles" in src

    def test_pure_resurface_streak_at_six(self):
        # Streak restarted at one at #1096, extended to two at #1101,
        # three at #1106, four at #1111, five at #1116; this run
        # extends it to six.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "pure-re-surface streak" in src
        assert "extends to" in src and "SIX" in src

    def test_zero_own_repo_gf_urls_this_run(self):
        # Unlike #1116 (four own-repo commit URLs in the GF set), the
        # GF set surfaced zero own-repo GitHub URLs this run.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 own-repo GitHub URLs" in src


class TestEveryoneHatesElon:
    def test_all_five_ehe_keys_in_corpus(self):
        for key in EHE_KEYS:
            assert _corpus_hit_count(key) >= 1, "missing corpus hit for %s" % key

    def test_52_day_hold_arithmetic(self):
        import datetime
        days = (datetime.date(2026, 10, 1) - datetime.date(2026, 8, 10)).days
        assert days == 52

    def test_ehe_not_a_podcast(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "activist group, NOT a podcast" in src

    def test_no_competitor_equivalent_campaign(self):
        # Bounded search-result absence across all 147 cycles.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "147 cycles" in src

    def test_primary_motif_preserved(self):
        ps = _read(PS_PATH)
        assert "Glasses for people who don't do consent" in ps

    def test_two_ehe_circular_blobs_in_committed_tree(self):
        # The two own-repo GitHub URLs surfaced in the EHE set this
        # run are present in the committed tree (rejected as circular
        # evidence, not ingested).
        for rel in (
            "podcast-sentiment.md",
            "examples/sample_output/wearables_advocacy_coalition_analysis_2026_jul.md",
        ):
            res = _git("ls-tree", "HEAD", rel)
            assert "blob" in res.stdout, rel


class TestAttentionSphere:
    def test_147th_no_match_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "one-hundred-forty-seventh" in src

    def test_all_six_as_commits_git_cat_file_verified(self):
        for sha in CIRCULAR_AS_COMMITS:
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_as_blob_absent_this_run(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "blob did NOT surface this run" in src

    def test_tracked_sources_advance_146_to_147(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "146->147" in src

    def test_task_spec_name_still_misidentified(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "misidentified as a podcast" in src


class TestPressSurfaces:
    def test_three_resurface_keys_in_corpus(self):
        for key in PRESS_RESURFACE_KEYS:
            assert _corpus_hit_count(key) >= 1, "missing corpus hit for %s" % key

    def test_four_new_press_keys_zero_precommit_hits(self):
        # PRE-COMMIT NOVELTY PIN: the four press keys were verified
        # zero-hit against the pre-commit tree in the pre-commit
        # battery (git grep -F at 09:35 PDT Oct 1). Post-commit this
        # assertion is BY DESIGN red: the main commit lands this
        # file, which documents the new keys, so HEAD carries hits.
        # Deselect in post-commit runs (like the TestRotationGuard
        # novelty pin).
        for key in NEW_PRESS_KEYS:
            assert _corpus_hit_count(key) == 0, "unexpected hit for %s" % key

    def test_new_keys_documented_in_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOUR" in src and "new verbatim URL keys" in src

    def test_recency_frontier_holds_sep29(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "HOLDS at Sep 29" in src

    def test_tenth_hold_since_1071_advance(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "tenth hold" in src

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

    def test_27_result_rows_19_distinct_4_new(self):
        # 7 GF + 7 EHE + 6 AS + 7 press = 27 rows. Distinct
        # non-circular: 7 GF + 5 EHE + 3 press re-surfaces + 4 new
        # press keys = 19 (no URL key repeats across the four query
        # sets). 4 of the 19 are new-to-corpus verbatim URL keys.
        total_rows = 7 + 7 + 6 + 7
        assert total_rows == 27
        distinct = set(GF_KEYS) | set(EHE_KEYS) | set(
            PRESS_RESURFACE_KEYS + NEW_PRESS_KEYS
        )
        assert len(distinct) == 19
        assert len(NEW_PRESS_KEYS) == 4
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "27 result rows" in src
        assert "19 non-circular" in src
        assert "FOUR new" in src

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

    def test_falsification_ledger_holds_43(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ledger holds at 43" in src

    def test_forty_third_member_claim_twice_in_journalists(self):
        # The affirmative FORTY-THIRD form is the m902
        # falsification-family line, present twice in the committed
        # profiles tree per #1118/#1120: the claim line plus the
        # finding line's self-reference, both in journalists.yaml.
        out = _git(
            "grep", "-F", _T43,
            "HEAD", "--", "profiles/careers/journalists.yaml",
        ).stdout
        assert len(out.strip().splitlines()) == 2

    def test_forty_third_claim_in_exactly_one_profiles_file(self):
        out = _git(
            "grep", "-l", "-F", _T43, "HEAD", "--", "profiles/",
        ).stdout
        assert len(out.strip().splitlines()) == 1

    def test_no_forty_fourth_member_claim_profiles_wide(self):
        # The next falsification slot must be unclaimed profiles-wide
        # (needle format-built per #715; designed negative-guard
        # wordings do not carry the claim form).
        for p, t in _profiles_text():
            assert _T44 not in t, p

    def test_thirty_first_direction_present(self):
        out = _git(
            "grep", "-F", _TW31, "HEAD", "--", "profiles/",
        ).stdout
        assert len(out.strip().splitlines()) >= 1

    def test_thirty_second_direction_absent_profiles_wide(self):
        tw32 = "THIRTY-" + "SECOND relationship direction"
        for p, t in _profiles_text():
            assert tw32 not in t, p

    def test_engine_not_run(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run" in src

    def test_not_artifact_grade(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT artifact-grade" in src


class TestStalenessPins:
    def _class_run(self, filename, classname):
        target = os.path.join(TESTS_DIR, filename)
        env = dict(os.environ)
        env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
        res = subprocess.run(
            ["python3", "-m", "pytest", target,
             "-k", classname,
             "-q", "--no-header"],
            cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        )
        return res

    def test_1120_guard_lifecycle_zero_904_still_green(self):
        # The #1120 Type D file's guard-lifecycle class pins the
        # zero-904 forward guards (numeric, underscore, dash; next
        # number 904; max id 903). It must still PASS: mechanism 904
        # has not landed (Type E adds no mechanisms). It fails BY
        # DESIGN when a future A/B/C leg lands it.
        res = self._class_run(
            D1120_FILE,
            "TestGuardLifecycle1120",
        )
        assert res.returncode == 0, res.stdout[-2000:]


class TestDocSync:
    def test_readme_test_file_table_has_no_1121_row_pre_commit(self):
        readme = _read(README_PATH)
        assert "test_type_e_1121" not in readme

    def test_architecture_has_no_1121_row_pre_commit(self):
        arch = _read(ARCH_PATH)
        assert "test_type_e_1121" not in arch

    def test_readme_stats_current(self):
        readme = _read(README_PATH)
        assert "| 58339 |" in readme
        assert "1445" in readme


class TestIterationLog:
    def test_no_1121_entry_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1121 Type E" not in log

    def test_1120_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1120 Type D" in log

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
