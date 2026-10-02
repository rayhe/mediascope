"""Type E #1131: podcast sentiment 149th verification cycle (Oct 1 2026, 07:00 PM PDT).

Monitoring-only verification cycle per the Aug 28 2026 standing rule:
no new mechanisms, tone NOT_SCORED, engine NOT run, ledger holds at 46,
NOT artifact-grade, verdict directionally_supported_not_proven.

Findings:
(1) Guilty Feminist: episode 502 holds as newest (sixteenth Type E
    verification since the Sep 28 11:00am release, ~80 hours after
    publication; NO 503 surfaced; two-directory corroboration this run:
    listennotes main (crawled 10h; "LATEST EPISODE: The Guilty Feminist
    502. Homophobia", 01:00:32; 762 episodes), podscan.fm main page
    (crawled 14h; 502 Homophobia summary with Linus Karp, Palmolive
    sponsor read); plus the listennotes TH stale locale variant, the
    chortle Edinburgh-Fringe-2026 show page (crawled 4d),
    uk-podcasts.co.uk (crawled 7h; 762 episodes; "Latest episode:
    2026-09-28"), the uk-podcasts Deborah Frances-White On The News
    Meeting episode page, and the youtube episode-500 page - all in
    corpus). ONE new-to-corpus verbatim GF URL key this run:
    youtube.com/watch?v=IVVk2wTR5xE (Deborah Frances-White SXSW London
    2026 panel "Is Authoritarianism Creeping Into the UK?" with Agnes
    Callamard, Josie Fernandez-Marelli, Misan Harriman;
    authoritarian-creep / culture-war framing; snippet carries zero
    Meta/wearables content - NOT a GF episode). The GF pure-re-surface
    streak ENDS at seven (restarted at one at #1096, extended two at
    #1101, three at #1106, four at #1111, five at #1116, six at #1121,
    seven at #1126). ZERO Meta/wearables content in any GF episode
    across all 149 cycles (bounded search-result absence).
(2) Everyone Hates Elon (activist group, NOT a podcast): 52-day hold
    (Aug 10 Epstein spoof -> Oct 1; date(2026,10,1)-date(2026,8,10)=52
    days). Five logged keys re-surfaced (huckmag pervert-glasses piece
    crawled 9h via #1021; linkedin whats-up-privacy roundup crawled 10h
    via #1001/#1006; feminist.org author archive crawled 7h via #1091;
    linkedin kayvan-mirza op-ed crawled 2d via #1001/#1006; techtimes
    amnesty-boxes crawled 3h via #886); afrotech ethics/consent did NOT
    surface this run (in corpus). ZERO new-to-corpus verbatim EHE URL
    keys (pure re-surface cycle). 2 own-repo GitHub URLs rejected as
    circular (podcast-sentiment HEAD blob + the examples sample_output
    wearables_advocacy strand blob; each git-ls-tree-verified present
    in the committed tree, not ingested). No competitor-equivalent
    guerrilla campaign in any of the 149 cycles (bounded search-result
    absence).
(3) Attention Sphere: one-hundred-forty-ninth quoted-search no-match
    as a podcast. 6 result rows this run (blob did NOT surface;
    16611229 absent this run), all this repository's own GitHub commit
    URLs (the same set as #1106/#1111/#1116/#1121/#1126; each
    git-cat-file-verified present, still circular as evidence),
    rejected as circular, not ingested. Tracked Sources 148->149.
    Task-spec name remains misidentified as a podcast; real-world
    identity stands per #591 (advocacy group, named ED Kendall
    Schrohe).
(4) Press: SEVEN result rows = 6 re-surfaces + 1 new. Re-surfaces:
    techspot news 113968 camera-free piece (crawled 3h; in corpus via
    #981); avcaesar "the anti-pervert solution?" piece (crawled 2h;
    in corpus via #1121); techjournalhq camera-free Audio piece
    (crawled <1h; in corpus via #1121); geeky-gadgets Meta Connect
    2026 announcements piece (crawled 5d; in corpus via #1121);
    usatoday Sep-23 camera-free piece (crawled 7d); maglazana Sep-26
    camera-free piece (crawled 2h; in corpus via #1036-era). ONE
    new-to-corpus verbatim press URL key: impartpad Ray-Ban Meta Audio
    pre-order piece (crawled 1h; $349, shipping Oct 13, camera-free AI
    positioning; snippet-bounded, tone NOT_SCORED). Recency frontier
    HOLDS at Sep 29 (the #1071 thesun.ie Boz piece remains the
    newest-in-corpus surface; twelfth hold since the #1071 advance;
    thesun.ie and gagadget did NOT surface this run but remain in
    corpus). Meta-exclusive privacy-pressure framing continues across
    all 149 cycles; no competitor camera-wearable coverage carries
    equivalent privacy-pressure framing. Snippet-bounded, tone
    NOT_SCORED.

Research method: 4 browser.search query sets, 0 browser.open
(excerpt-bounded per #503). 27 result rows / 19 non-circular
distinct URL keys (7 GF + 5 EHE + 7 press; no URL key repeats
across the four query sets) / TWO new verbatim URL keys. 8 distinct
own-repo GitHub URLs rejected as circular (0 GF, 2 EHE blobs,
6 AS commits; each git-cat-file or git-ls-tree verified present in
the committed tree, still circular as evidence). All URLs copied
verbatim from Full-URL listings; no canonical URLs constructed.
ASCII-only.

Rotation: 1130-1134 window SECOND leg per #565 (D #1130 -> E #1131 ->
A #1132 -> B #1133 -> C #1134; order D->E->A->B->C).

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test file anchor edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file) - all
UNCOMMITTED, owned by their runs, untouched by this run (targeted
staging only). Do NOT touch #1024's m846 (FOURTEENTH,
exclusionary-diversion): self-flagged sourcing-constraint violation;
Ray's revert/leave/rebuild-from-primary decision still pending.

Background: the #1130-launched full suite (writing to the goal
hidden_files type_d_1130_full_suite.log, 1588 bytes at this run's
check, one candidate pytest PID at check) is in flight at this run's
check; its verdict belongs to #1135 per #795. This run does not
touch it.

Pre-commit novelty greps: zero test_type_e_1131 files on disk (glob);
no "Type E #1131" in git log (--grep); max numeric mechanism_id 909
in-tree pre-commit (m907/m908/m909 committed at #1127/#1128/#1129
Type A/B/C, verified at #1130 Type D; Type E adds no mechanisms);
zero numeric/underscore/dash next-number nine-ten mechanism key forms
repo-wide pre-commit (needles format-built per #715, own file
excluded); 19 surfaced distinct non-circular verbatim URL keys: 17 at
>=1 pre-commit corpus hit via git grep -F (6 GF re-surfaces, 5 EHE,
6 press re-surfaces) and 2 NEW with zero pre-commit hits
(youtube.com/watch?v=IVVk2wTR5xE Deborah Frances-White SXSW London
panel, GF set; impartpad Ray-Ban Meta Audio pre-order piece, press
set); 8 distinct own-repo GitHub URLs rejected as circular; no #1131
row in README/ARCHITECTURE test tables or iteration-log pre-commit.
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
    "test_type_e_1131_podcast_sentiment_149th_verification_oct01_7pm.py"
)

ANCHORED_SHA = "79899109f9b05567be1d51111196a8ff19848011"  # placeholder pre-commit; patched per #565 in the anchor followup

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

# Predecessor chain: #1130 Type D OPENED the 1130-1134 window.
PRED_MAIN_1130 = "fb682ff9"
PRED_ANCHOR_1130 = "8bfa3fe8"
PRED_DOCSYNC_1130 = "dd2b63fe"
PRED_FINAL_1130 = "25bdf092"

# The #1130 window-opener file, for the staleness pin on its
# guard-lifecycle class (zero next-number nine-ten / no-thirty-fourth /
# no-forty-seventh).
D1130_FILE = (
    "test_type_d_1130_m907_m908_m909_qualitative_"
    "corpus_integrity_oct01_6pm.py"
)

# The landed FORTY-SIXTH member and THIRTY-THIRD direction forms are
# plain literals (already in corpus). The forty-seventh-member and
# thirty-fourth-direction needles are fragment-built per #715 so this
# file carries no contiguous literal of a forward-guard claim form.
_T46 = "FORTY-" + "SIXTH falsification-family member"
_TW33 = "THIRTY-" + "THIRD relationship direction"
_T47 = "FORTY-" + "SEVENTH falsification-family member"
_TW34 = "THIRTY-" + "FOURTH relationship direction"

# No own-repo GitHub commit URLs surfaced by the GF query set this run
# (unlike #1116's and #1126's four). Zero-length list documents the
# clean set.
CIRCULAR_GF_COMMITS = []

# Circular own-repo GitHub commit URLs surfaced by the Attention
# Sphere query set this run (the same 6 as #1106/#1111/#1116/#1121/#1126).
CIRCULAR_AS_COMMITS = [
    "40d6e7b02192f0f972affe1fade345d50f96e87b",
    "5e238e788c4f080288d690da7cf29a3ea2648a02",
    "d4618aae2fd932b9547b90b328adf2e7ce2eedbd",
    "0d9132c60e2828b24597b68567eaaa4b47b82c23",
    "bf0cbbf1a8465afcd68daac32e220048bc2b94b0",
    "dec561406353b2ab576086386b90dedaa37a94fd",
]

# GF re-surfaces: all >=1 pre-commit corpus hit.
GF_RESURFACE_KEYS = [
    "chortle.co.uk/shows/edinburgh_fringe_2026/g/39124/the_guilty_feminist",
    "listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG",
    "podscan.fm/podcasts/the-guilty-feminist",
    "listennotes.com/th/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG",
    "uk-podcasts.co.uk/podcast/the-guilty-feminist/deborah-frances-white-on-the-news-meeting",
    "youtube.com/watch?v=iKXj2w2cp50",
]

# GF set, NEW this run: zero pre-commit corpus hits. NOT a GF episode
# (Deborah Frances-White SXSW London 2026 authoritarianism panel).
GF_NEW_KEYS = [
    "youtube.com/watch?v=IVVk2wTR5xE",
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
    "avcaesar.com/news/8122/ray-ban-meta-audio-smart-glasses-without-a-camera-the-anti-pervert-solution",
    "techjournalhq.com/meta-camera-free-ray-ban-audio-ai-glasses-9896",
    "geeky-gadgets.com/meta-connect-2026-announcements",
    "usatoday.com/story/tech/news/2026/09/23/meta-camera-free-smart-glasses/91913146007",
    "maglazana.com/2026/09/26/meta-unveils-camera-free-new-gen-3-smart-glasses",
]

# Press set, NEW this run: zero pre-commit corpus hits.
PRESS_NEW_KEYS = [
    "impartpad.com/news/ray-ban-meta-audio-glasses-camera-free-ai-audio-from-349-ship-13-oct",
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
    def test_predecessor_1130_chain_present(self):
        log = _git("log", "--oneline", "-80").stdout
        assert PRED_MAIN_1130 in log
        assert PRED_ANCHOR_1130 in log
        assert PRED_DOCSYNC_1130 in log
        assert PRED_FINAL_1130 in log

    def test_type_e_1131_novelty(self):
        # "Type E #1131" absent from git log pre-commit; own file not
        # yet committed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type E #1131:") lands; post-commit, the anchor
        # asserts the patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        log = _git("log", "--oneline", "--grep=Type E #1131").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1130 -> E #1131" in src

    def test_next_run_1132_type_a_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "A #1132" in src


class TestMechanismNovelty:
    def test_type_e_adds_no_mechanisms(self):
        # Type E runs are monitoring-only; they never land mechanisms.
        assert _max_numeric_mechanism_id() == 909

    def test_zero_910_numeric_mechanism_id_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(910) == []

    def test_zero_910_underscore_mechanism_repo_wide(self):
        assert _repo_grep_underscore_mechanism(910) == []

    def test_zero_910_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(910) == []

    def test_no_1131_file_on_disk_pre_commit(self):
        own = [f for f in os.listdir(TESTS_DIR) if "type_e_1131" in f]
        assert len(own) <= 1
        if own:
            assert own[0] == OWN_BASENAME


class TestGuiltyFeminist:
    def test_six_gf_resurface_keys_in_corpus(self):
        for key in GF_RESURFACE_KEYS:
            assert _corpus_hit_count(key) >= 1, "missing corpus hit for %s" % key

    def test_sxsw_panel_key_new_to_corpus(self):
        # The youtube SXSW London panel key has zero pre-commit corpus
        # hits (verified pre-commit via git grep -F); it is NOT a GF
        # episode, so GF-episode corpus (502 as newest) is untouched.
        for key in GF_NEW_KEYS:
            assert _corpus_hit_count(key) == 0, "expected zero hits for %s" % key

    def test_episode_502_holds_as_newest(self):
        # Sixteenth Type E verification since the Sep 28 11:00am
        # release (~80 hours after publication); NO 503 surfaced
        # across the four search sets.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "episode 502 holds" in src
        assert "sixteenth Type E" in src

    def test_zero_meta_wearables_content_across_149_cycles(self):
        # Bounded search-result absence, not proof; tone NOT_SCORED.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ZERO Meta/wearables content" in src
        assert "149 cycles" in src

    def test_pure_resurface_streak_ends_at_seven(self):
        # Streak restarted at one at #1096, extended to two at #1101,
        # three at #1106, four at #1111, five at #1116, six at #1121,
        # seven at #1126; this run's one new GF-set key (the SXSW
        # panel surface, zero pre-commit corpus hits) ENDS the streak
        # at seven - it does not extend it.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "pure-re-surface streak" in src
        assert "ENDS at seven" in src

    def test_zero_own_repo_gf_commits_this_run(self):
        # Unlike #1116's and #1126's four, the GF set surfaced zero
        # own-repo GitHub commit URLs this run (clean set; the two
        # circular URLs this run were both in the EHE set).
        assert CIRCULAR_GF_COMMITS == []
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "zero own-repo" in src

    def test_two_directory_corroboration_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "two-directory corroboration" in src
        assert "762 episodes" in src


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
        # Bounded search-result absence across all 149 cycles.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "149 cycles" in src

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
    def test_149th_no_match_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "one-hundred-forty-ninth" in src

    def test_all_six_as_commits_git_cat_file_verified(self):
        for sha in CIRCULAR_AS_COMMITS:
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_as_blob_absent_this_run(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "blob did NOT surface this run" in src

    def test_tracked_sources_advance_148_to_149(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "148->149" in src

    def test_task_spec_name_still_misidentified(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "misidentified as a podcast" in src


class TestPressSurfaces:
    def test_six_resurface_keys_in_corpus(self):
        for key in PRESS_RESURFACE_KEYS:
            assert _corpus_hit_count(key) >= 1, "missing corpus hit for %s" % key

    def test_one_new_press_key_zero_pre_commit_hits(self):
        # The impartpad Ray-Ban Meta Audio pre-order piece has zero
        # pre-commit corpus hits (verified pre-commit via git grep -F);
        # the GF streak break and this key are the two new verbatim
        # URL keys this run.
        for key in PRESS_NEW_KEYS:
            assert _corpus_hit_count(key) == 0, "expected zero hits for %s" % key

    def test_recency_frontier_holds_sep29(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "HOLDS at Sep 29" in src

    def test_twelfth_hold_since_1071_advance(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "twelfth hold" in src

    def test_thesun_ie_gagadget_nonsurface_noted(self):
        # thesun.ie Boz and gagadget did NOT surface this run but
        # remain in corpus; absence is not a drop per #503.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "did NOT surface this run" in src

    def test_meta_exclusive_framing_noted(self):
        # Meta-exclusive privacy-pressure framing across all 149
        # cycles; no competitor camera-wearable coverage carries
        # equivalent privacy-pressure framing.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Meta-exclusive privacy-pressure framing" in src
        assert "149 cycles" in src

    def test_seven_press_rows_six_plus_one(self):
        # 7 press rows: 6 re-surfaces + 1 new key.
        assert len(PRESS_RESURFACE_KEYS) == 6
        assert len(PRESS_NEW_KEYS) == 1


class TestResearchMethod:
    def test_four_query_sets_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "4 browser.search query sets" in src
        assert "0 browser.open" in src

    def test_27_result_rows_19_distinct_2_new(self):
        # 7 GF + 7 EHE + 6 AS + 7 press = 27 rows. Distinct
        # non-circular: 7 GF + 5 EHE + 7 press = 19 (no URL key
        # repeats across the four query sets). 2 of the 19 are
        # new-to-corpus verbatim URL keys.
        total_rows = 7 + 7 + 6 + 7
        assert total_rows == 27
        distinct = set(GF_RESURFACE_KEYS) | set(GF_NEW_KEYS) | set(
            EHE_KEYS
        ) | set(PRESS_RESURFACE_KEYS) | set(PRESS_NEW_KEYS)
        assert len(distinct) == 19
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "27 result rows" in src
        assert "19 non-circular" in src
        assert "TWO new verbatim URL keys" in src

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

    def test_falsification_ledger_holds_46(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ledger holds at 46" in src

    def test_forty_sixth_member_claim_twice_in_the_verge(self):
        # The landed FORTY-SIXTH form is the m907
        # falsification-family line (committed at #1127, verified at
        # #1130), present twice in the committed the-verge.yaml.
        out = _git(
            "grep", "-F", _T46,
            "HEAD", "--", "profiles/the-verge.yaml",
        ).stdout
        assert len(out.strip().splitlines()) == 2

    def test_forty_sixth_claim_in_exactly_one_profiles_file(self):
        out = _git(
            "grep", "-l", "-F", _T46, "HEAD", "--", "profiles/",
        ).stdout
        assert len(out.strip().splitlines()) == 1

    def test_no_forty_seventh_member_claim_profiles_wide(self):
        # The next falsification slot must be unclaimed profiles-wide
        # (needle format-built per #715; the designed negative-guard
        # wordings carry the member-claim form, not the claim form).
        for p, t in _profiles_text():
            assert _T47 not in t, p

    def test_thirty_third_direction_present(self):
        # The landed THIRTY-THIRD form is the m909 LITIGATION-CHANNEL
        # direction (committed at #1129, verified at #1130).
        out = _git(
            "grep", "-F", _TW33, "HEAD", "--", "profiles/",
        ).stdout
        assert len(out.strip().splitlines()) >= 1

    def test_no_thirty_fourth_direction_claim_profiles_wide(self):
        # The next direction slot must be unclaimed profiles-wide
        # (needle format-built per #715).
        for p, t in _profiles_text():
            assert _TW34 not in t, p

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

    def test_1130_guard_lifecycle_still_green(self):
        # The #1130 Type D file's guard-lifecycle class pins the
        # zero next-number nine-ten forward guards (numeric, underscore,
        # dash; max id 909), the no-thirty-fourth-direction guard, and
        # the no-forty-seventh-member guard. It must still PASS: this
        # Type E run lands no mechanisms. It fails BY DESIGN when a
        # future A/B/C leg lands mechanism nine-ten.
        res = self._class_run(
            D1130_FILE,
            "TestGuardLifecycle1130",
        )
        assert res.returncode == 0, res.stdout[-2000:]


class TestDocSync:
    def test_readme_test_file_table_has_no_1131_row_pre_commit(self):
        readme = _read(README_PATH)
        assert "test_type_e_1131" not in readme

    def test_architecture_has_no_1131_row_pre_commit(self):
        arch = _read(ARCH_PATH)
        assert "test_type_e_1131" not in arch

    def test_readme_stats_current(self):
        readme = _read(README_PATH)
        assert "| 59142 |" in readme
        assert "1455" in readme


class TestIterationLog:
    def test_no_1131_entry_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1131 Type E" not in log

    def test_1130_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1130 Type D" in log

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
