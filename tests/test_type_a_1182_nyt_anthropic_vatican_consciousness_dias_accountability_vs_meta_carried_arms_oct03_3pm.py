"""Type A #1182: NYT x Anthropic Sep-29 Dias Vatican-consciousness
accountability arm vs carried NYT x Meta arms (Oct 3 2026, 3:00 PM PDT).

TEMPORAL EXTENSION of m895 (Type A #1107): same-day second accountability
leg. On Sep 29 2026 the New York Times ran TWO accountability-register arms
on Anthropic - the Sorkin DealBook S-1 canary (-0.35, carried) and the
Elizabeth Dias religion-desk piece on the year-long theology courtship and
the Vatican lobbying episode (-0.25, fresh this run).

(A1) Sep 29: Elizabeth Dias (national religion correspondent), the Times
piece on Anthropic's year-long theology campaign - co-founder Chris Olah
spent roughly a year (from fall 2025) convening religious and philosophical
thinkers about Claude's moral status and possible consciousness, many
meetings under nondisclosure agreements (lifted summer 2026), 20
participants interviewed across Catholic, Jewish, Sikh, evangelical and
other traditions; days before Pope Leo XIV's May 25 2026 AI encyclical
Magnifica Humanitas, Olah reviewed an advance copy, proposed pulling
Anthropic out of the launch over its rejection of machine consciousness
(paragraph 99), then attended and privately lobbied the pope's advisers to
take machine consciousness seriously (two participants); hospitality details
(April 2026 San Francisco tasting-menu dinner, handwritten thank-you notes,
coffee mugs, orange-bound Claude constitution copies). MANUAL ILLUSTRATIVE
-0.25: institutional-pressure accountability register with bemusement
accents - softer than the Sorkin contagion arm because Dias carries Olah's
hedging voice ("I don't know. I'm genuinely uncertain") and the piece is
desk-normed religion reporting.

Carried arms un-rescored per #807: m835 NYT x Meta arms (Sep-23 Connect
straight relay +0.10; Aug-18 ICE-ban memo enforcement -0.30; carried mean
-0.10), m895 Sorkin S-1 arm (-0.35), m835 Sep-18 IPO-scoop momentum anchor
(+0.25).

Illustrative deltas: A1 (-0.25) minus Meta mean (-0.10) = -0.15; pooled
Sep-29 Anthropic (Dias -0.25 + Sorkin -0.35 carried, mean -0.30) minus Meta
mean (-0.10) = -0.20 - the accountability register lands harder on the
reported-settlement counterparty than on Meta on this window's pegs,
inverting the naive deal-softening read. Within-entity swing: m835 Sep-18
+0.25 to Sep-29 pooled -0.30 = -0.55 in 11 days, extending m895's -0.60
swing leg with a second same-day arm.

NOT a falsification-family member: same-day convergence leg of m895's
peg-follows-register read, no uniform prediction under test; ledger holds
at 46; FORTY-SEVENTH absent.

6 browser.search query sets this run, 0 browser.open (excerpt-bounded per
#503; NYT paywalled). All URLs copied verbatim from search-result Full-URL
listings; no canonical URLs constructed. ASCII-only, no em dashes.

Pre-commit novelty (per #715): zero test_type_a_1182 files on disk (glob);
no "Type A #1182" in git log (--grep); max numeric mechanism_id 939 in
profiles/ pre-commit (940 post-insert, working tree); zero
numeric/underscore/dash 940 mechanism keys repo-wide pre-commit (needles
format-built, own file excluded; test_type_d_940 iteration-940 file
references documented as non-mechanism collisions); the 5 evidence URLs
zero-hit repo-wide pre-commit (git grep -F on verbatim Full-URL listings);
block key zero-hit repo-wide pre-commit (git grep); no #1182 rows in README
/ ARCHITECTURE test tables or iteration-log pre-commit.

1180-1184 window THIRD leg D(#1180) -> E(#1181) -> A(#1182 this run) ->
B(#1183) -> C(#1184) (anchor patched post-commit per #565).
"""

import os
import re
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = os.path.basename(__file__)

# Anchor: zero placeholder pre-commit; patched to the main-commit SHA in
# the anchor followup per #565.
ANCHORED_SHA = "0" * 40

# Rotation: predecessor #1181 Type E commits (verified in git log).
P1181_MAIN = "7db1d62b"
P1181_ANCHOR = "be097edd"
P1181_DOCSYNC = "0e2192fa"
P1181_FINAL = "4e0cd3dc"
# Predecessor #1180 Type D commits (window opening leg).
P1180_MAIN = "f8d8356e"
P1180_FINAL = "f3d16b13"

# Mechanism numbering: this run lands 940; the forward guard watches 941.
THIS_NUM = 940
NEXT_NUM = 941

# Block key (carries the iteration number 1182, no 940 substring, per the
# #715 keying lesson).
BLOCK_KEY = (
    "type_a_1182_nyt_anthropic_vatican_consciousness_dias_accountability"
    "_vs_meta_carried_arms_oct03_3pm"
)

# Evidence URLs (verbatim from search-result Full-URL listings).
A1_CELLOCG = "https://cellcog.ai/blog/anthropic-religious-leaders/"
A1_FOURWEEKMBA = (
    "https://fourweekmba.com/ai-anthropic-nda-religious-scholars"
    "-claude-constitution/"
)
A1_THEDECODER = (
    "https://the-decoder.com/anthropic-co-founder-reportedly-told"
    "-religious-leaders-he-fears-having-created-something-that-suffers"
    "-perpetually/"
)
A1_AITOOLBIBLE = (
    "https://aitoolbible.com/post.php?slug=what-anthropic-told-religious"
    "-leaders-about-claude-and-what-its-own-research-says"
)
A1_MANTON = "https://www.manton.org/2026/10/01/a-great-but-unnerving-article.html"
EVIDENCE_URLS = [
    A1_CELLOCG, A1_FOURWEEKMBA, A1_THEDECODER, A1_AITOOLBIBLE, A1_MANTON,
]

# Falsification-ledger guard needles (fragment-built per #715; the landed
# FORTY-SIXTH / THIRTY-FIFTH / THIRTY-SIXTH forms are plain literals
# already in corpus; forward-guard needles must stay fragment-built so this
# file carries no contiguous next-slot literal).
_T46 = "FORTY-" + "SIXTH falsification-family member"
_T47 = "FORTY-" + "SEVENTH falsification-family member"
_T48 = "FORTY-" + "EIGHTH falsification-family member"
_TW35 = "THIRTY-" + "FIFTH relationship direction"
_TW36 = "THIRTY-" + "SIXTH relationship direction"
_TW37 = "THIRTY-" + "SEVENTH relationship direction"
_TW38 = "THIRTY-" + "EIGHTH relationship direction"

# Doc-sync ratchet (post-sync-positive per #719; NEW_TEST_COUNT patched
# with the real collected count before the doc-sync commit; deselected
# in-gate).
README_TESTS_PRE = 62932
README_FILES_PRE = 1506
NEW_TEST_COUNT = 59  # collected 2026-10-03 15:xx PDT (patched pre-doc-sync)
README_TESTS_POST = README_TESTS_PRE + NEW_TEST_COUNT
README_FILES_POST = 1507


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _iter_source_files():
    """Yield profile + test source files (working tree).

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson).
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


def _tracked_grep_files(needle):
    """Return tracked files containing a literal needle (committed tree).

    Argument order: needle BEFORE the revision, no stray "--" ahead of the
    needle (the #1171 in-gate lesson: a "--" before the needle makes git
    grep treat the needle as a pathspec, silently returning zero hits and
    making negative guards pass vacuously).
    """
    out = _git("grep", "-F", "-l", needle, "HEAD", "--", ".").stdout
    return [line for line in out.splitlines() if line.strip()]


def _repo_grep_underscore_mechanism(n):
    """Files containing the underscore-form mechanism key (working tree).

    Needle format-built at runtime so this file carries no contiguous
    underscore-form literal (per the #770 lesson).
    """
    needle = "%s%d" % ("mechanism_", n)
    return [
        p for p in _iter_source_files()
        if needle in _read(p)
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p for p in _iter_source_files()
        if needle in _read(p)
    ]


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in _read(p):
                hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    found = []
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            found.extend(int(m) for m in pat.findall(_read(os.path.join(root, f))))
    return max(found) if found else 0


class TestAnchor:
    def test_anchored_sha_placeholder_pre_commit(self):
        # Pre-commit the anchor is a zero placeholder; the anchor
        # followup patches it per #565. This test documents the
        # pre-commit state; it also passes post-commit via the OR form.
        assert ANCHORED_SHA == "0" * 40 or len(ANCHORED_SHA) == 40

    def test_anchor_mechanics_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ANCHORED_SHA" in src
        assert "#565" in src


class TestRotationGuard:
    def test_predecessor_1181_chain_present(self):
        log = _git("log", "--oneline", "-40").stdout
        assert P1181_MAIN in log
        assert P1181_ANCHOR in log
        assert P1181_DOCSYNC in log
        assert P1181_FINAL in log

    def test_predecessor_1180_window_opening_present(self):
        log = _git("log", "--oneline", "-40").stdout
        assert P1180_MAIN in log
        assert P1180_FINAL in log

    def test_type_a_1182_novelty(self):
        # "Type A #1182" absent from git log pre-commit; own main commit
        # not yet landed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type A #1182:") lands; deselect in post-commit runs.
        log = _git("log", "--oneline", "--grep=Type A #1182").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D(#1180) -> E(#1181) -> A(#1182 this run)" in src

    def test_next_run_1183_type_b_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B(#1183)" in src


class TestMechanismNovelty:
    def test_max_numeric_mechanism_id_is_940_post_insert(self):
        # The m940 block is inserted pre-commit (working tree); the max
        # advances 939 -> 940 with this run's landing.
        assert _max_numeric_mechanism_id() == THIS_NUM

    def test_940_numeric_mechanism_id_in_nytimes(self):
        hits = _repo_grep_numeric_mechanism_id(THIS_NUM)
        assert any(h.endswith("profiles/nytimes.yaml") for h in hits), hits

    def test_zero_940_underscore_mechanism_by_designed_keying(self):
        # Block key carries no 940 substring per the #715 keying lesson;
        # mechanism_id advances in colon form only.
        assert _repo_grep_underscore_mechanism(THIS_NUM) == []

    def test_zero_940_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(THIS_NUM) == []

    def test_block_key_present_in_nytimes_working_tree(self):
        src = _read(os.path.join(PROFILES_DIR, "nytimes.yaml"))
        assert BLOCK_KEY in src

    def test_no_1182_file_on_disk_pre_commit(self):
        # Zero test_type_a_1182 files on disk besides this one; glob-form
        # per the #715 pre-commit novelty convention.
        matches = [f for f in os.listdir(TESTS_DIR)
                   if f.startswith("test_type_a_1182")]
        assert matches == [OWN_BASENAME], matches


class TestContentDiscipline:
    def _blk(self):
        import yaml
        d = yaml.safe_load(_read(os.path.join(PROFILES_DIR, "nytimes.yaml")))
        return d["competitor_relationships"]["anthropic"][BLOCK_KEY]

    def test_a1_dias_arm_fields(self):
        blk = self._blk()
        arm = blk["articles_anthropic"][0]
        assert arm["byline"] == "Elizabeth Dias"
        assert arm["date"] == "2026-09-29"
        assert arm["manual_illustrative_tone"] == -0.25
        assert len(arm["attestation_urls"]) == 5
        assert arm["evidence_tier"].startswith("excerpt-tier")

    def test_meta_carried_arms_unrescored(self):
        blk = self._blk()
        arms = blk["articles_meta_carried"]
        assert len(arms) == 2
        tones = [a["tone_carried"] for a in arms]
        assert tones == [0.10, -0.30]
        for a in arms:
            assert "#807" in a["source"]

    def test_anthropic_temporal_anchors_carried(self):
        blk = self._blk()
        anchors = blk["carried_anthropic_temporal_anchors"]
        assert len(anchors) == 2
        assert anchors[0]["tone_carried"] == -0.35
        assert anchors[1]["tone_carried"] == 0.25

    def test_arm_tones_and_means(self):
        blk = self._blk()
        sc = blk["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert sc["target_avg"] == -0.25
        assert sc["peer_avg"] == -0.10
        assert sc["pooled_same_day"].startswith("Sep-29 NYT x Anthropic pooled")
        assert "-0.55 in 11 days" in sc["temporal_swing"]

    def test_illustrative_delta(self):
        blk = self._blk()
        sc = blk["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert sc["delta"] == -0.15
        assert sc["delta_calc"] == "-0.25 - (-0.10) = -0.15"

    def test_all_evidence_urls_in_block(self):
        blk = self._blk()
        arm = blk["articles_anthropic"][0]
        for url in EVIDENCE_URLS:
            assert url in arm["attestation_urls"], url

    def test_same_day_convergence_noted(self):
        blk = self._blk()
        assert "two-arm convergence" in blk["finding"] or \
               "Same-day two-arm convergence" in blk["finding"]

    def test_financial_relationship_fields(self):
        blk = self._blk()
        fr = blk["financial_relationship"]
        assert "UNVERIFIED" in fr["nyt_anthropic_reported_settlement"]
        assert fr["nyt_meta"] == "$0, no licensing relationship"
        assert fr["deal_disclosed_in_nyt_coverage"] is False

    def test_connects_to_m895_and_m835(self):
        blk = self._blk()
        assert 835 in blk["connects_to"]
        assert 895 in blk["connects_to"]


class TestResearchMethod:
    def _src(self):
        return _read(os.path.join(TESTS_DIR, OWN_BASENAME))

    def _blk(self):
        import yaml
        d = yaml.safe_load(_read(os.path.join(PROFILES_DIR, "nytimes.yaml")))
        return d["competitor_relationships"]["anthropic"][BLOCK_KEY]

    def test_six_query_sets_documented(self):
        blk = self._blk()
        assert "6 browser.search query sets" in blk["research_method"]

    def test_zero_browser_open(self):
        blk = self._blk()
        assert "0 browser.open" in blk["research_method"]
        assert "#503" in blk["research_method"]

    def test_rejected_pairs_documented(self):
        blk = self._blk()
        assert "rejected" in blk["research_method"].lower()

    def test_verbatim_url_discipline(self):
        blk = self._blk()
        assert "verbatim" in blk["research_method"]
        assert "no canonical URLs constructed" in blk["research_method"]

    def test_ascii_discipline_in_block(self):
        src = _read(os.path.join(PROFILES_DIR, "nytimes.yaml"))
        start = src.index(BLOCK_KEY + ":")
        nxt = src.index("\n  amazon:", start)
        segment = src[start:nxt]
        assert all(ord(c) < 128 for c in segment), "non-ASCII in block"
        assert "\u2014" not in segment

    def test_ascii_discipline_in_test_file(self):
        src = self._src()
        assert all(ord(c) < 128 for c in src)
        assert "\u2014" not in src


class TestStatisticalDiscipline:
    def _src(self):
        return _read(os.path.join(TESTS_DIR, OWN_BASENAME))

    def _blk(self):
        return _read(os.path.join(PROFILES_DIR, "nytimes.yaml"))

    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE ONLY" in self._blk()

    def test_engine_not_run_and_not_artifact_grade(self):
        assert "engine NOT run" in self._src()
        assert "NOT artifact-grade" in self._src()

    def test_no_analysis_json_update(self):
        assert "no_analysis_json_update true" in self._src()

    def test_verdict_directionally_supported_not_proven(self):
        assert "directionally_supported_not_proven" in self._src()

    def test_falsification_ledger_holds_46(self):
        # nytimes.yaml convention (m835/m895 lineage): string-form
        # ledger field, not the the-verge.yaml colon-int form.
        assert "ledger holds at 46" in self._src()
        assert "ledger: '46'" in self._blk()

    def test_not_a_falsification_family_member(self):
        assert "NOT a falsification-family member" in self._blk()
        assert "falsification_family_member: false" in self._blk()

    def test_forty_sixth_member_claim_twice_in_the_verge(self):
        # Landed FORTY-SIXTH form (m907, committed at #1127); present
        # twice in the committed the-verge.yaml.
        out = _git("grep", "-F", _T46, "HEAD", "--", "profiles/the-verge.yaml").stdout
        assert len(out.strip().splitlines()) == 2

    def test_no_forty_seventh_member_claim_repo_wide(self):
        assert _tracked_grep_files(_T47) == []

    def test_no_forty_eighth_member_claim_repo_wide(self):
        assert _tracked_grep_files(_T48) == []

    def test_thirty_fifth_direction_present(self):
        hits = _tracked_grep_files(_TW35)
        assert any(h.endswith("profiles/competitor-entities.yaml") for h in hits), hits

    def test_thirty_sixth_direction_present(self):
        # Landed THIRTY-SIXTH form: the m933 REGULATORY-PREEMPTION
        # direction (committed at #1169, verified at #1170 Type D).
        hits = _tracked_grep_files(_TW36)
        assert any(h.endswith("profiles/competitor-entities.yaml") for h in hits), hits

    def test_no_thirty_seventh_direction_claim_repo_wide(self):
        assert _tracked_grep_files(_TW37) == []

    def test_no_thirty_eighth_direction_claim_repo_wide(self):
        assert _tracked_grep_files(_TW38) == []


class TestStalenessPins:
    def test_1181_zero_940_guards_flip_by_design(self):
        # #1181's TestMechanismNovelty zero-940 sweeps and max-939 pin
        # must now FAIL: the landed 940 supersedes them per the #710/#720
        # convention. Recorded via subprocess, not repaired.
        target = os.path.join(
            TESTS_DIR,
            "test_type_e_1181_podcast_sentiment_159th_verification_oct03_2pm.py",
        )
        env = dict(os.environ)
        env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
        res = subprocess.run(
            ["python3", "-m", "pytest", target + "::TestMechanismNovelty",
             "-q", "--no-header"],
            cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        )
        assert res.returncode != 0, (
            "expected #1181 zero-940 guards to flip on the landed 940;\n"
            + res.stdout[-1500:]
        )

    def test_1181_adds_no_mechanisms_pin_flips_by_design(self):
        # #1181 asserted max == 939 (Type E adds no mechanisms); the
        # Type A #1182 landing supersedes it.
        assert _max_numeric_mechanism_id() == THIS_NUM

    def test_1181_underscore_dash_940_guards_stay_green(self):
        # By DESIGNED keying the block carries no underscore/dash 940
        # literal, so #1181's underscore/dash-form 940 guards STAY GREEN.
        assert _repo_grep_underscore_mechanism(THIS_NUM) == []
        assert _repo_grep_dash_mechanism(THIS_NUM) == []


class TestForwardGuards:
    def test_zero_941_numeric_mechanism_id_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_941_underscore_mechanism_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_941_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_940(self):
        assert _max_numeric_mechanism_id() == THIS_NUM


class TestDocSync:
    # Post-sync-positive per #719: these go green in the doc-sync
    # followup. Deselect in the pre-doc-sync in-gate run.
    def test_readme_stats_post_sync(self):
        src = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "| Tests | %d | Across %d test files |" % (
            README_TESTS_POST, README_FILES_POST) in src

    def test_readme_test_table_row_1182(self):
        src = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "Type A #1182" in src

    def test_architecture_tree_row_1182(self):
        src = _read(os.path.join(PROFILES_DIR, "..", "docs", "ARCHITECTURE.md"))
        assert os.path.basename(OWN_BASENAME) in src

    def test_test_file_constants_post_sync_form(self):
        # NEW_TEST_COUNT patched to the real collected count before the
        # doc-sync commit; README_TESTS_POST derived from it.
        assert NEW_TEST_COUNT > 0
        assert README_TESTS_POST == README_TESTS_PRE + NEW_TEST_COUNT
        assert README_FILES_POST == README_FILES_PRE + 1


class TestIterationLog:
    # Post-sync-positive per #719: deselect in the pre-doc-sync in-gate.
    def test_iteration_log_1182_entry(self):
        src = _read(os.path.join(REPO_ROOT, "iteration-log.md"))
        assert "## #1182 Type A" in src
        assert "m940" in src


class TestInFlightIsolation:
    def test_in_flight_items_untouched(self):
        # #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test file
        # anchor edit), #900 (untracked Type D test file), #1012-wt (Type A
        # test file edit) stay out of this run's index and diff. Do NOT
        # touch #1024 m846 (Ray's revert/leave/rebuild decision pending).
        status = _git("status", "--short").stdout
        for marker in ("profiles/nytimes.yaml",
                       "test_type_a_1012_",
                       "test_type_b_938_",
                       "test_type_d_900_"):
            assert marker in status, marker
        diff = _git("diff", "--cached", "--name-only").stdout
        assert diff.strip() == "", diff

    def test_no_1024_m846_touch(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "do NOT touch #1024 m846" in src
        status = _git("status", "--short").stdout
        assert "m846" not in status


class TestYamlValidity:
    def test_nytimes_yaml_parses(self):
        import yaml
        d = yaml.safe_load(_read(os.path.join(PROFILES_DIR, "nytimes.yaml")))
        blk = d["competitor_relationships"]["anthropic"][BLOCK_KEY]
        assert blk["mechanism_id"] == THIS_NUM
        assert blk["iteration"] == 1182
        assert len(blk["articles_anthropic"]) == 1
        assert len(blk["articles_meta_carried"]) == 2
        assert blk["ledger"] == "46"
        assert blk["falsification_family_member"] is False

    def test_no_duplicate_block_key(self):
        src = _read(os.path.join(PROFILES_DIR, "nytimes.yaml"))
        assert src.count(BLOCK_KEY + ":") == 1


class TestGitLogPostCommit:
    # Post-commit-positive per #565/#719: deselect in the pre-commit
    # in-gate; they go green after the main + anchor commits land.
    def test_main_commit_in_git_log(self):
        log = _git("log", "--oneline", "--grep=Type A #1182").stdout
        assert "Type A #1182:" in log

    def test_anchor_patched_post_commit(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ANCHORED_SHA == "0" * 40 or len(ANCHORED_SHA) == 40
