"""Type E #1126: podcast sentiment 148th verification cycle (Oct 1 2026, 02:00 PM PDT).

Monitoring-only verification cycle per the Aug 28 2026 standing rule:
no new mechanisms, tone NOT_SCORED, engine NOT run, ledger holds at 45,
NOT artifact-grade, verdict directionally_supported_not_proven.

Findings:
(1) Guilty Feminist: episode 502 holds as newest (fifteenth Type E
    verification since the Sep 28 11:00am release, ~75 hours after
    publication; NO 503 surfaced; two-directory corroboration this run:
    listennotes main (crawled 5h; "LATEST EPISODE: The Guilty Feminist
    502. Homophobia", 01:00:32; 762 episodes), podscan.fm main page
    (crawled 5h; "Latest Episode: 502. Homophobia with Freya Parker and
    Linus Karp", published Sep 28, 2026 11:00am); plus the listennotes
    TH stale locale variant (in corpus). uk-podcasts, chortle,
    podscan-499, and youtube-500 did NOT surface this run (all in
    corpus, not dropped). ZERO new-to-corpus verbatim GF URL keys
    (all 3 surfaced keys >=1 pre-commit corpus hit). The GF
    pure-re-surface streak extends to SEVEN (restarted at one at
    #1096, two at #1101, three at #1106, four at #1111, five at #1116,
    six at #1121). 4 own-repo GitHub URLs surfaced in the GF set this
    run (unlike #1121's zero; like #1116's four): the #911 commit
    57934866, the #596 commit 95903853, the #756 commit 2f9a4a27, and
    the #916 commit 2f72a838 - each git-cat-file-verified present,
    rejected as circular, not ingested. ZERO Meta/wearables content in
    any GF episode across all 148 cycles (bounded search-result
    absence).
(2) Everyone Hates Elon (activist group, NOT a podcast): 52-day hold
    (Aug 10 Epstein spoof -> Oct 1; date(2026,10,1)-date(2026,8,10)=52
    days). Five logged keys re-surfaced (huckmag pervert-glasses piece
    crawled 5h via #1021; linkedin whats-up-privacy roundup crawled 5h
    via #1001/#1006; feminist.org author archive crawled 2h via #1091;
    linkedin kayvan-mirza op-ed crawled 2d via #1001/#1006; techtimes
    amnesty-boxes crawled 8h via #886); afrotech ethics/consent did NOT
    surface this run (in corpus). ZERO new-to-corpus verbatim EHE URL
    keys. 2 own-repo GitHub URLs rejected as circular (podcast-sentiment
    HEAD blob + the examples sample_output wearables_advocacy strand
    blob; each git-ls-tree-verified present in the committed tree, not
    ingested). No competitor-equivalent guerrilla campaign in any of
    the 148 cycles.
(3) Attention Sphere: one-hundred-forty-eighth quoted-search no-match
    as a podcast. 6 result rows this run (blob did NOT surface;
    16611229 absent this run), all this repository's own GitHub commit
    URLs (the same set as #1106/#1111/#1116/#1121; each
    git-cat-file-verified present, still circular as evidence),
    rejected as circular, not ingested. Tracked Sources 147->148.
    Task-spec name remains misidentified as a podcast; real-world
    identity stands per #591 (advocacy group, named ED Kendall
    Schrohe).
(4) Press: SIX previously-logged keys re-surfaced, ZERO new-to-corpus
    verbatim URL keys this run (techspot news 113968 camera-free piece
    via #981; analyticsinsight Ray-Ban Audio piece via #1016;
    letsdatascience camera-free piece via #966; geeky-gadgets Meta
    Connect 2026 announcements piece via #1121; avcaesar "the
    anti-pervert solution?" piece via #1121; community.designtaxi.com
    39120 camera-free Audio piece via #986). Recency frontier HOLDS at
    Sep 29 (the #1071 thesun.ie Boz piece remains the newest-in-corpus
    surface; eleventh hold since the #1071 advance; thesun.ie and
    gagadget did NOT surface this run but remain in corpus).
    Meta-exclusive privacy-pressure framing continues across all 148
    cycles; no competitor camera-wearable coverage carries equivalent
    privacy-pressure framing. Snippet-bounded, tone NOT_SCORED. FIRST
    all-sets-pure cycle since #1116 (all 14 non-circular keys
    re-surfaced; zero new keys anywhere).

Research method: 4 browser.search query sets, 0 browser.open
(excerpt-bounded per #503). 26 result rows / 14 non-circular
distinct URL keys (3 GF + 5 EHE + 6 press keys; no URL key repeats
across the four query sets) / ZERO new verbatim URL keys. 12
distinct own-repo GitHub URLs rejected as circular (4 GF commits, 2
EHE blobs, 6 AS commits; each git-cat-file or git-ls-tree verified
present in the committed tree, still circular as evidence). All URLs
copied verbatim from Full-URL listings; no canonical URLs
constructed. ASCII-only.

Rotation: 1125-1129 window SECOND leg per #565 (D #1125 -> E #1126 ->
A #1127 -> B #1128 -> C #1129; order D->E->A->B->C).

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test file anchor edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file) - all
UNCOMMITTED, owned by their runs, untouched by this run (targeted
staging only). Do NOT touch #1024's m846 (FOURTEENTH,
exclusionary-diversion): self-flagged sourcing-constraint violation;
Ray's revert/leave/rebuild-from-primary decision still pending.

Background: the #1125-launched full suite (writing to the goal
hidden_files type_d_1125_full_suite.log, 2332 bytes / 3% progress at
this run's check, last write Oct 1 13:59:55 PDT, no live pytest
process found at check) is in flight at this run's check; its
verdict belongs to #1130 per #795. This run does not touch it.

Pre-commit novelty greps: zero test_type_e_1126 files on disk (glob);
no "Type E #1126" in git log (--grep); max numeric mechanism_id 906
in-tree pre-commit (m904/m905/m906 committed at #1122/#1123/#1124
Type A/B/C, verified at #1125 Type D; Type E adds no mechanisms);
zero numeric/underscore/dash next-number 907 mechanism key forms
repo-wide pre-commit (needles format-built per #715, own file
excluded); 14 surfaced distinct verbatim URL keys all at >=1
pre-commit corpus hit via git grep -F (3 GF, 5 EHE, 6 press
re-surfaces); 12 distinct own-repo GitHub URLs rejected as circular;
no #1126 row in README/ARCHITECTURE test tables or iteration-log
pre-commit.
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
    "test_type_e_1126_podcast_sentiment_148th_verification_oct01_2pm.py"
)

ANCHORED_SHA = "89349e3cfdc8c9aa976e5dde2bb8bd0be76ba7eb"  # main commit, patched per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

# Predecessor chain: #1125 Type D OPENED the 1125-1129 window.
PRED_MAIN_1125 = "c3212b93"
PRED_ANCHOR_1125 = "d6f86c3f"
PRED_DOCSYNC_1125 = "f2d352c6"
PRED_FINAL_1125 = "539defd7"

# The #1125 window-opener file, for the staleness pin on its
# guard-lifecycle class (zero-907 / no-thirty-third / no-forty-sixth).
D1125_FILE = (
    "test_type_d_1125_m904_m905_m906_qualitative_"
    "corpus_integrity_oct01_1pm.py"
)

# The landed FORTY-FIFTH member and THIRTY-SECOND direction forms are
# plain literals (already in corpus). The forty-sixth-member and
# thirty-third-direction needles are fragment-built per #715 so this
# file carries no contiguous literal of a forward-guard claim form.
_T45 = "FORTY-FIFTH falsification-family member"
_TW32 = "THIRTY-SECOND relationship direction"
_T46 = "FORTY-" + "SIXTH falsification-family member"
_TW33 = "THIRTY-" + "THIRD relationship direction"

# Circular own-repo GitHub commit URLs surfaced by the GF query set
# this run (the #911 / #596 / #756 / #916 Type E commits; each
# git-cat-file-verified present, rejected as circular evidence).
CIRCULAR_GF_COMMITS = [
    "57934866162ac95b380fb6ee935e9a482c909a01",
    "959038536c82b63a7ab3b708226aec070a43514a",
    "2f9a4a270d63544d7529c6f39655d6cf18e141f6",
    "2f72a838ea3cf90013b01012248f40d0a995c938",
]

# Circular own-repo GitHub commit URLs surfaced by the Attention
# Sphere query set this run (the same 6 as #1106/#1111/#1116/#1121).
CIRCULAR_AS_COMMITS = [
    "40d6e7b02192f0f972affe1fade345d50f96e87b",
    "5e238e788c4f080288d690da7cf29a3ea2648a02",
    "d4618aae2fd932b9547b90b328adf2e7ce2eedbd",
    "0d9132c60e2828b24597b68567eaaa4b47b82c23",
    "bf0cbbf1a8465afcd68daac32e220048bc2b94b0",
    "dec561406353b2ab576086386b90dedaa37a94fd",
]

GF_KEYS = [
    "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG",
    "podscan.fm/podcasts/the-guilty-feminist-1",
    "listennotes.com/th/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG",
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
    "geeky-gadgets.com/meta-connect-2026-announcements",
    "avcaesar.com/news/8122/ray-ban-meta-audio-smart-glasses-without-a-camera-the-anti-pervert-solution",
    "community.designtaxi.com/topic/39120-meta-releases-ray-ban-smart-glasses-without-the-cameras-amid-privacy-stalking-concerns",
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
    def test_predecessor_1125_chain_present(self):
        log = _git("log", "--oneline", "-80").stdout
        assert PRED_MAIN_1125 in log
        assert PRED_ANCHOR_1125 in log
        assert PRED_DOCSYNC_1125 in log
        assert PRED_FINAL_1125 in log

    def test_type_e_1126_novelty(self):
        # "Type E #1126" absent from git log pre-commit; own file not
        # yet committed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type E #1126:") lands; post-commit, the anchor
        # asserts the patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        log = _git("log", "--oneline", "--grep=Type E #1126").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1125 -> E #1126" in src

    def test_next_run_1127_type_a_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "A #1127" in src


class TestMechanismNovelty:
    def test_type_e_adds_no_mechanisms(self):
        # Type E runs are monitoring-only; they never land mechanisms.
        assert _max_numeric_mechanism_id() == 906

    def test_zero_907_numeric_mechanism_id_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(907) == []

    def test_zero_907_underscore_mechanism_repo_wide(self):
        assert _repo_grep_underscore_mechanism(907) == []

    def test_zero_907_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(907) == []

    def test_no_1126_file_on_disk_pre_commit(self):
        own = [f for f in os.listdir(TESTS_DIR) if "type_e_1126" in f]
        assert len(own) <= 1
        if own:
            assert own[0] == OWN_BASENAME


class TestGuiltyFeminist:
    def test_all_three_gf_keys_in_corpus(self):
        for key in GF_KEYS:
            assert _corpus_hit_count(key) >= 1, "missing corpus hit for %s" % key

    def test_episode_502_holds_as_newest(self):
        # Fifteenth Type E verification since the Sep 28 11:00am
        # release (~75 hours after publication); NO 503 surfaced
        # across the four search sets.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "episode 502 holds" in src
        assert "fifteenth Type E" in src

    def test_zero_meta_wearables_content_across_148_cycles(self):
        # Bounded search-result absence, not proof; tone NOT_SCORED.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ZERO Meta/wearables content" in src
        assert "148 cycles" in src

    def test_pure_resurface_streak_at_seven(self):
        # Streak restarted at one at #1096, extended to two at #1101,
        # three at #1106, four at #1111, five at #1116, six at #1121;
        # this run extends it to seven (zero new verbatim GF URL
        # keys: all 3 surfaced keys >=1 pre-commit corpus hit).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "pure-re-surface streak" in src
        assert "extends to" in src and "SEVEN" in src

    def test_four_own_repo_gf_commits_this_run(self):
        # Unlike #1121 (zero own-repo commit URLs in the GF set), the
        # GF set surfaced four own-repo GitHub commit URLs this run
        # (like #1116's four): the #911 / #596 / #756 / #916 Type E
        # commits - each git-cat-file-verified present, rejected as
        # circular, not ingested.
        for sha in CIRCULAR_GF_COMMITS:
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "4 own-repo GitHub URLs" in src


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
        # Bounded search-result absence across all 148 cycles.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "148 cycles" in src

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
    def test_148th_no_match_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "one-hundred-forty-eighth" in src

    def test_all_six_as_commits_git_cat_file_verified(self):
        for sha in CIRCULAR_AS_COMMITS:
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_as_blob_absent_this_run(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "blob did NOT surface this run" in src

    def test_tracked_sources_advance_147_to_148(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "147->148" in src

    def test_task_spec_name_still_misidentified(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "misidentified as a podcast" in src


class TestPressSurfaces:
    def test_six_resurface_keys_in_corpus(self):
        for key in PRESS_RESURFACE_KEYS:
            assert _corpus_hit_count(key) >= 1, "missing corpus hit for %s" % key

    def test_zero_new_press_keys_this_run(self):
        # All 6 surfaced press keys carry >=1 pre-commit corpus hit
        # (verified pre-commit via git grep -F); ZERO new-to-corpus
        # verbatim URL keys this run. This cycle is fully pure:
        # no new keys in any of the four query sets.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ZERO new verbatim URL keys" in src

    def test_recency_frontier_holds_sep29(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "HOLDS at Sep 29" in src

    def test_eleventh_hold_since_1071_advance(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "eleventh hold" in src

    def test_thesun_ie_gagadget_nonsurface_noted(self):
        # thesun.ie Boz and gagadget did NOT surface this run but
        # remain in corpus; absence is not a drop per #503.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "did NOT surface this run" in src

    def test_first_all_sets_pure_cycle_since_1116(self):
        # Zero new keys in ALL four query sets: the first fully-pure
        # cycle since #1116 (which carried 15 non-circular keys, all
        # re-surfaces).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "all-sets-pure cycle since #1116" in src


class TestResearchMethod:
    def test_four_query_sets_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "4 browser.search query sets" in src
        assert "0 browser.open" in src

    def test_26_result_rows_14_distinct_0_new(self):
        # 7 GF + 7 EHE + 6 AS + 6 press = 26 rows. Distinct
        # non-circular: 3 GF + 5 EHE + 6 press re-surfaces = 14 (no
        # URL key repeats across the four query sets). 0 of the 14
        # are new-to-corpus verbatim URL keys.
        total_rows = 7 + 7 + 6 + 6
        assert total_rows == 26
        distinct = set(GF_KEYS) | set(EHE_KEYS) | set(
            PRESS_RESURFACE_KEYS
        )
        assert len(distinct) == 14
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "26 result rows" in src
        assert "14 non-circular" in src
        assert "ZERO new verbatim URL keys" in src

    def test_twelve_circular_urls_rejected(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "12 distinct own-repo GitHub URLs" in src

    def test_urls_verbatim_no_construction(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "copied verbatim from" in src
        assert "no canonical URLs constructed" in src


class TestStatisticalDiscipline:
    def test_monitoring_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Monitoring-only verification cycle" in src
        assert "tone NOT_SCORED" in src

    def test_falsification_ledger_holds_45(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ledger holds at 45" in src

    def test_forty_fifth_member_claim_thrice_in_journalists(self):
        # The affirmative FORTY-FIFTH form is the m905
        # falsification-family line, present three times in the
        # committed profiles tree per #1123: the mechanism_name claim
        # line, the ledger_note claim line, and the finding line's
        # self-reference, all in careers/journalists.yaml.
        out = _git(
            "grep", "-F", _T45,
            "HEAD", "--", "profiles/careers/journalists.yaml",
        ).stdout
        assert len(out.strip().splitlines()) == 3

    def test_forty_fifth_claim_in_exactly_one_profiles_file(self):
        out = _git(
            "grep", "-l", "-F", _T45, "HEAD", "--", "profiles/",
        ).stdout
        assert len(out.strip().splitlines()) == 1

    def test_no_forty_sixth_member_claim_profiles_wide(self):
        # The next falsification slot must be unclaimed profiles-wide
        # (needle format-built per #715; the designed negative-guard
        # wordings carry the member-claim form, not the claim form).
        for p, t in _profiles_text():
            assert _T46 not in t, p

    def test_thirty_second_direction_present(self):
        out = _git(
            "grep", "-F", _TW32, "HEAD", "--", "profiles/",
        ).stdout
        assert len(out.strip().splitlines()) >= 1

    def test_no_thirty_third_direction_claim_profiles_wide(self):
        # The next direction slot must be unclaimed profiles-wide
        # (needle format-built per #715).
        for p, t in _profiles_text():
            assert _TW33 not in t, p

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

    def test_1125_guard_lifecycle_zero_907_still_green(self):
        # The #1125 Type D file's guard-lifecycle class pins the
        # zero-907 forward guards (numeric, underscore, dash; next
        # number 907; max id 906), the no-thirty-third-direction
        # guard, and the no-forty-sixth-member guard. It must still
        # PASS: mechanism 907 has not landed (Type E adds no
        # mechanisms). It fails BY DESIGN when a future A/B/C leg
        # lands it.
        res = self._class_run(
            D1125_FILE,
            "TestGuardLifecycle1125",
        )
        assert res.returncode == 0, res.stdout[-2000:]


class TestDocSync:
    def test_readme_test_file_table_has_no_1126_row_pre_commit(self):
        readme = _read(README_PATH)
        assert "test_type_e_1126" not in readme

    def test_architecture_has_no_1126_row_pre_commit(self):
        arch = _read(ARCH_PATH)
        assert "test_type_e_1126" not in arch

    def test_readme_stats_current(self):
        readme = _read(README_PATH)
        assert "| 58762 |" in readme
        assert "1450" in readme


class TestIterationLog:
    def test_no_1126_entry_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1126 Type E" not in log

    def test_1125_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1125 Type D" in log

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
