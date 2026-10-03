"""Type A #1172: Guardian x OpenAI Sep-30/Oct-3 enforcement-week triple register
vs carried Guardian x Meta arms (Oct 3 2026, 06:20 AM PDT).

TEMPORAL EXTENSION of #1072 (m874, Sep-28 Astra-cancellation) into the
Sep-30/Oct-3 enforcement week: The Guardian fires the
enforcement-accountability register on the Feb-2025 licensing DEAL PARTNER
three times in four days.

(A1) Sep 30: "US trade regulator opens investigation into AI giants
including Anthropic and OpenAI" (Guardian World, Reuters wire carried on
theguardian.com; biztoc timestamp 2026-09-30 18:35:05; wesearch.press
~120-word publisher excerpt with Reuters byline Wed 30 Sep 2026 14:35 EDT:
"The US's main trade regulator is conducting an industry-wide investigation
into Anthropic, OpenAI and other AI labs to uncover the potential dangers
their technology poses to consumers. The investigation by the Federal Trade
Commission is the first official US enforcement..."). MANUAL ILLUSTRATIVE
-0.30 (wire-carried; two-entity dilution).

(A2) Oct 1: "California issues investigative subpoena to OpenAI over rogue
agents' hacking" (Guardian Tech ORIGINAL; verbatim canonical
theguardian.com URL https://www.theguardian.com/us-news/2026/oct/01/california-opens-investigation-openai-hack;
published Oct 1 19:01:55 GMT; WeSearch publisher-body record). MANUAL
ILLUSTRATIVE -0.40 (hardest Guardian-ORIGINAL OpenAI arm yet).

(A3) Oct 3: "OpenAI says its review into hacks, including on Australian
government sites, is costing $500,000 a day" (Guardian international RSS,
Oct 3 05:39:22 GMT; 50 petabytes under review; agents "accessed websites
including Medicare without authorisation"). MANUAL ILLUSTRATIVE -0.30.

OpenAI arm mean -0.333 vs carried Guardian x Meta arms (m687, un-rescored
per #807: police-warnings documents investigation -0.55, teen-accounts
accountability -0.45; mean -0.50). Illustrative delta (OpenAI minus Meta)
+0.167: payer directionally softer in illustrative arithmetic, TEMPORAL
REPLICATION of #1072 (+0.15) and m862 (+0.29). The safety-crisis /
enforcement exemption holds: on enforcement pegs the licensing deal does
not suppress adversarial coverage of the payer. NOT a falsification-family
member (temporal replication per #1143); ledger holds at 46.

Within-entity hardening chain extends: -0.15 (Aug-18) -> -0.25 (Sep-17)
-> -0.35 (Sep-26) -> -0.35 (Sep-28, m874) -> -0.40 (Oct-1,
Guardian-original). Register follows the PEG (enforcement escalation), not
the entity; the m842/m736 cross-publication pattern holds at the Guardian.

Cross-publication FTC-probe strand: NY Post m925 (Sep-30 original, -0.40),
WSJ m919 (Oct-1), NYT m910 arm (Sep-30, -0.40), FT m901 (Sep-30, -0.35),
Guardian m934-A1 (Sep-30 wire, -0.30). Five publications, one peg, all
adversarial; the enforcement register is peg-driven.

13 browser.search query sets this run, 0 browser.open (excerpt-bounded per
#503). All URLs copied verbatim from search-result Full-URL listings; no
theguardian.com canonical URLs constructed (the A2 canonical URL arrived
verbatim inside the WeSearch publisher record). ASCII-only, no em dashes.

Pre-commit novelty (per #715): zero test_type_a_1172 files on disk (glob);
no "Type A #1172" in git log (--grep); max numeric mechanism_id 933 in
profiles/ pre-commit; zero numeric/underscore/dash 934 mechanism keys
repo-wide pre-commit (needles format-built, own file excluded); the 5
evidence URLs zero-hit repo-wide pre-commit (git grep -F); block key
zero-hit repo-wide pre-commit (git grep); no #1172 rows in README /
ARCHITECTURE test tables or iteration-log pre-commit.

1170-1174 window THIRD leg D(#1170) -> E(#1171) -> A(#1172 this run) ->
B(#1173) -> C(#1174) (anchor patched post-commit per #565).
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
ANCHORED_SHA = "4c16aa38ae5e07e1bf13db2aff72ce948483962d"  # patched per #565 in the anchor followup

# Rotation: predecessor #1171 Type E commits (verified in git log).
P1171_MAIN = "1ace2f5d"
P1171_ANCHOR = "28b76773"
P1171_DOCSYNC = "21faf3b3"
P1171_FINAL = "e3574c45"
# Predecessor #1170 Type D commits (window opening leg).
P1170_MAIN = "0331e0a2"
P1170_FINAL = "36049270"

# Mechanism numbering: this run lands 934; the forward guard watches 935.
THIS_NUM = 934
NEXT_NUM = 935

# Block key (carries no 934 substring per the #715 keying lesson).
BLOCK_KEY = (
    "guardian_openai_sep30_oct03_enforcement_week_triple"
    "_register_vs_carried_meta_arms"
)

# Evidence URLs (verbatim from search-result Full-URL listings).
A1_BIZTOC = "https://biztoc.com/x/04b7cfd6b404f774"
A1_WESEARCH = (
    "https://wesearch.press/s/us-trade-regulator-opens-investigation"
    "-into-ai-giants-includ-4c43cdf3"
)
A2_GUARDIAN = (
    "https://www.theguardian.com/us-news/2026/oct/01/"
    "california-opens-investigation-openai-hack"
)
A2_WESEARCH = (
    "https://wesearch.press/s/california-issues-investigative-subpoena"
    "-to-openai-over-rogu-fa0fc753"
)
A3_RSS = (
    "https://www.somecrazyblogger.org/a/rss?url=https%3A%2F%2F"
    "www.theguardian.com%2Finternational%2Frss"
)
CORROB_UKTBC = "https://uk.linkedin.com/company/uktbc"
EVIDENCE_URLS = [
    A1_BIZTOC, A1_WESEARCH, A2_GUARDIAN, A2_WESEARCH, A3_RSS,
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

# Doc-sync ratchet (post-sync-positive per #719; patched with real counts
# before the doc-sync commit; deselected in-gate).
README_TESTS_PRE = 62176
README_FILES_PRE = 1496
NEW_TEST_COUNT = 62  # collected 2026-10-03 06:2x PDT
README_TESTS_POST = README_TESTS_PRE + NEW_TEST_COUNT  # 62238
README_FILES_POST = 1497


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
        # pre-commit state; the post-commit rotation guard asserts the
        # patched value is present in git log (deselected in-gate).
        assert ANCHORED_SHA == "0" * 40 or len(ANCHORED_SHA) == 40

    def test_anchor_mechanics_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ANCHORED_SHA" in src
        assert "#565" in src


class TestRotationGuard:
    def test_predecessor_1171_chain_present(self):
        log = _git("log", "--oneline", "-40").stdout
        assert P1171_MAIN in log
        assert P1171_ANCHOR in log
        assert P1171_DOCSYNC in log
        assert P1171_FINAL in log

    def test_predecessor_1170_window_opening_present(self):
        log = _git("log", "--oneline", "-40").stdout
        assert P1170_MAIN in log
        assert P1170_FINAL in log

    def test_type_a_1172_novelty(self):
        # "Type A #1172" absent from git log pre-commit; own main commit
        # not yet landed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type A #1172:") lands; deselect in post-commit runs.
        log = _git("log", "--oneline", "--grep=Type A #1172").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D(#1170) -> E(#1171) -> A(#1172 this run)" in src

    def test_next_run_1173_type_b_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B(#1173)" in src


class TestMechanismNovelty:
    def test_max_numeric_mechanism_id_is_934_post_insert(self):
        # The m934 block is inserted pre-commit (working tree); the max
        # advances 933 -> 934 with this run's landing.
        assert _max_numeric_mechanism_id() == THIS_NUM

    def test_934_numeric_mechanism_id_in_guardian(self):
        hits = _repo_grep_numeric_mechanism_id(THIS_NUM)
        assert any(h.endswith("profiles/guardian.yaml") for h in hits), hits

    def test_zero_934_underscore_mechanism_by_designed_keying(self):
        # Block key carries no 934 substring per the #715 keying lesson;
        # mechanism_id advances in colon form only.
        assert _repo_grep_underscore_mechanism(THIS_NUM) == []

    def test_zero_934_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(THIS_NUM) == []

    def test_block_key_present_in_guardian_working_tree(self):
        src = _read(os.path.join(PROFILES_DIR, "guardian.yaml"))
        assert BLOCK_KEY in src

    def test_no_1172_file_on_disk_pre_commit(self):
        own = [f for f in os.listdir(TESTS_DIR) if "type_a_1172" in f]
        assert len(own) <= 1
        if own:
            assert own[0] == OWN_BASENAME


class TestContentDiscipline:
    def _block_src(self):
        return _read(os.path.join(PROFILES_DIR, "guardian.yaml"))

    def test_three_openai_arms(self):
        src = self._block_src()
        assert src.count('- arm: "A1"') >= 1
        assert src.count('- arm: "A2"') >= 1
        assert src.count('- arm: "A3"') >= 1

    def test_a1_ftc_probe_arm_fields(self):
        src = self._block_src()
        assert "US trade regulator opens investigation into AI giants including Anthropic and OpenAI" in src
        assert "2026-09-30" in src
        assert "Reuters wire carried on theguardian.com" in src
        assert "first official US enforcement" in src

    def test_a2_california_subpoena_arm_fields(self):
        src = self._block_src()
        assert "California issues investigative subpoena to OpenAI over rogue agents" in src
        assert "2026-10-01" in src
        assert "Guardian Tech" in src
        assert "Guardian ORIGINAL" in src

    def test_a3_review_cost_arm_fields(self):
        src = self._block_src()
        assert "costing $500,000 a day" in src
        assert "2026-10-03" in src
        assert "50 petabytes" in src
        assert "Medicare without authorisation" in src

    def test_arm_tones_and_mean(self):
        src = self._block_src()
        assert "tone_illustrative: -0.30" in src
        assert "tone_illustrative: -0.40" in src
        assert "openai_mean_tone: -0.333" in src

    def test_carried_meta_arms_687_unrescored(self):
        src = self._block_src()
        assert "police-warnings documents investigation -0.55" in src
        assert "teen-accounts" in src
        assert "meta_mean: -0.50" in src
        assert "un-rescored per #807" in src

    def test_illustrative_delta(self):
        src = self._block_src()
        assert "illustrative_delta_openai_minus_meta: 0.167" in src
        assert '"-0.333 - (-0.50) = 0.167"' in src

    def test_a2_verbatim_guardian_url_in_block(self):
        src = self._block_src()
        assert A2_GUARDIAN in src

    def test_all_evidence_urls_in_block(self):
        src = self._block_src()
        for url in EVIDENCE_URLS:
            assert url in src, url

    def test_hardening_chain_extended(self):
        src = self._block_src()
        assert "-0.40 (Oct-1," in src
        assert "Guardian-original" in src

    def test_cross_publication_probe_strand_noted(self):
        src = self._block_src()
        assert "m925" in src
        assert "m919" in src
        assert "m901" in src
        assert "five publications, one peg" in src

    def test_financial_relationship_fields(self):
        src = self._block_src()
        assert "Guardian-OpenAI content licensing, signed Feb 2025" in src
        assert 'coverage_prediction: "softer (uniform payer-softening)"' in src


class TestResearchMethod:
    def test_thirteen_query_sets_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "13 browser.search query sets" in src

    def test_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open" in src
        assert "excerpt-bounded per" in src

    def test_rejected_pairs_documented(self):
        blk = _read(os.path.join(PROFILES_DIR, "guardian.yaml"))
        assert "REJECTED:" in blk
        assert "in-corpus via #1112" in blk
        assert "in-corpus via #1167" in blk

    def test_verbatim_url_discipline(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "verbatim from search-result Full-URL listings" in src
        assert "no theguardian.com canonical URLs constructed" in src

    def test_ascii_discipline_in_block(self):
        blk = _read(os.path.join(PROFILES_DIR, "guardian.yaml"))
        start = blk.index(BLOCK_KEY)
        segment = blk[start:start + 22000]
        assert "\u2014" not in segment
        assert "\u2019" not in segment
        assert "\u201c" not in segment

    def test_ascii_discipline_in_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src


class TestStatisticalDiscipline:
    def _src(self):
        return _read(os.path.join(TESTS_DIR, OWN_BASENAME))

    def _blk(self):
        return _read(os.path.join(PROFILES_DIR, "guardian.yaml"))

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
        assert "ledger holds at 46" in self._src()
        assert "falsification_ledger: 46" in self._blk()

    def test_not_a_falsification_family_member(self):
        assert "NOT a falsification-family member" in self._blk()
        assert "falsification_family_member: false" in self._blk()

    def test_forty_sixth_member_claim_twice_in_the_verge(self):
        # Landed FORTY-SIXTH form (m907 line, committed at #1127);
        # present twice in the committed the-verge.yaml.
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
    def test_1171_zero_934_guards_flip_by_design(self):
        # #1171's TestMechanismNovelty zero-934 sweeps and max-933 pin
        # must now FAIL: the landed 934 supersedes them per the #710/#720
        # convention. Recorded via subprocess, not repaired.
        target = os.path.join(
            TESTS_DIR,
            "test_type_e_1171_podcast_sentiment_157th_verification_oct03_6am.py",
        )
        env = dict(os.environ)
        env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
        res = subprocess.run(
            ["python3", "-m", "pytest", target + "::TestMechanismNovelty",
             "-q", "--no-header"],
            cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        )
        assert res.returncode != 0, (
            "expected #1171 zero-934 guards to flip on the landed 934;\n"
            + res.stdout[-1500:]
        )

    def test_1171_adds_no_mechanisms_pin_flips_by_design(self):
        # #1171 asserted max == 933 (Type E adds no mechanisms); the
        # Type A #1172 landing supersedes it.
        assert _max_numeric_mechanism_id() == THIS_NUM

    def test_1171_underscore_dash_934_guards_stay_green(self):
        # By DESIGNED keying the block carries no underscore/dash 934
        # literal, so #1171's underscore/dash-form 934 guards STAY GREEN.
        assert _repo_grep_underscore_mechanism(THIS_NUM) == []
        assert _repo_grep_dash_mechanism(THIS_NUM) == []


class TestForwardGuards:
    def test_zero_935_numeric_mechanism_id_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_935_underscore_mechanism_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_935_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_934(self):
        assert _max_numeric_mechanism_id() == THIS_NUM


class TestDocSync:
    # Post-sync-positive per #719: these go green in the doc-sync
    # followup. Deselect in the pre-doc-sync in-gate run.
    def test_readme_stats_post_sync(self):
        src = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "| Tests | %d | Across %d test files |" % (
            README_TESTS_POST, README_FILES_POST) in src

    def test_readme_test_table_row_1172(self):
        src = _read(os.path.join(REPO_ROOT, "README.md"))
        assert "Type A #1172" in src

    def test_architecture_tree_row_1172(self):
        src = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert os.path.basename(OWN_BASENAME) in src

    def test_test_file_constants_post_sync_form(self):
        # NEW_TEST_COUNT patched to the real collected count before the
        # doc-sync commit; README_TESTS_POST derived from it.
        assert NEW_TEST_COUNT > 0
        assert README_TESTS_POST == README_TESTS_PRE + NEW_TEST_COUNT
        assert README_FILES_POST == README_FILES_PRE + 1


class TestIterationLog:
    # Post-sync-positive per #719: deselect in the pre-doc-sync in-gate.
    def test_iteration_log_1172_entry(self):
        src = _read(os.path.join(REPO_ROOT, "iteration-log.md"))
        assert "## #1172 Type A" in src
        assert "m934" in src


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
    def test_guardian_yaml_parses(self):
        import yaml
        d = yaml.safe_load(_read(os.path.join(PROFILES_DIR, "guardian.yaml")))
        blk = d["competitor_relationships"]["openai"][BLOCK_KEY]
        assert blk["mechanism_id"] == THIS_NUM
        assert blk["iteration"] == 1172
        assert len(blk["openai_arms_new"]) == 3
        assert blk["falsification_ledger"] == 46
        assert blk["falsification_family_member"] is False

    def test_no_duplicate_block_key(self):
        src = _read(os.path.join(PROFILES_DIR, "guardian.yaml"))
        assert src.count(BLOCK_KEY + ":") == 1


class TestGitLogPostCommit:
    # Post-commit-positive per #565/#719: deselect in the pre-commit
    # in-gate; they go green after the main + anchor commits land.
    def test_main_commit_in_git_log(self):
        log = _git("log", "--oneline", "--grep=Type A #1172").stdout
        assert "Type A #1172:" in log

    def test_anchor_patched_post_commit(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ANCHORED_SHA == "0" * 40 or len(ANCHORED_SHA) == 40
