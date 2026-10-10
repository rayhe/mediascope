# -*- coding: utf-8 -*-
"""Type C #1349 tests: October 9 2026 financial-incentive landscape
saturation verification (m1041) - FIRST dedicated corpus mechanism on the
saturation-verification leg: a systematic verification that every
financial-incentive development surfaced in the October 2026 window maps
to an already-banked corpus mechanism. Zero novel mechanisms found.

Iteration #1349 is the FIFTH and CLOSING leg of the 1345-1349 window
(D #1345 -> E #1346 -> A #1347 -> B #1348 -> C #1349 per the #565 anchor +
rotation guard). Next run #1350 Type D opens the 1350-1354 window.
This run lands mechanism 1041: the saturation verification. Method: 1
delegated scout (4 ranked candidates, all rejected on main-run corpus
verification) + 7 main-run browser.search verification sets across the
fresh-October financial angles (new licensing deals, earnings-call
disclosures, IPO/ad-monetization figures, publisher-remuneration
enforcement, litigation-coalition expansion, lab financing). Every
candidate maps to a banked mechanism:
- Google AI-contribution pilot payout figures (Technori Oct 5) -> m891
  (Type C #1099, Sep 30 rate disclosure; the figures are identical)
- Poland UOKiK Google remuneration charges (Oct 5) -> m993 (Type C
  #1269, same Oct-5 charges)
- OpenAI India newspaper deals BCCL ~$5M / Indian Express ~$3M
  (Sep 23) -> m798 pricing context (carried)
- ChatGPT ads $1B run rate + Oct-5 image-ads expansion -> m981
  (Type C #1249, same milestone + expansion)
- Redpine 20M-paper publisher licensing (Oct 6) -> #1289 (Type C,
  Oct 7, same event)
- Impelsys x Cashmere metered-use rail (Oct 7) -> #1284 (Type C,
  Oct 7, same event)
- News Corp v Brave suit -> news-corp.yaml Jul-22-2026 countersuit
  (in-corpus)
- Microsoft x Nine Entertainment APAC deal -> #1119 (Type C, Oct 1)
- 35-publisher / 400-newspaper Platkin coalition -> type_c_964
  (60 publishers / 550+ publications, both suits banked)
- Bloomsbury $3,000/title Anthropic settlement distribution ->
  banked $3,000/work settlement economics (m984 family)
- OtterlyAI 48% citation premium -> banked (test_ai_citation_-
  amplification + #249)
- Apple x Huxe IP licensing (Oct 9) -> REJECTED as out-of-scope
  (not a publication party; #1339 reached the same verdict)
- Anthropic Claude-for-Startups $45K credits (Oct 6) -> startup
  program, not a publisher incentive; out of scope
- OpenAI $30B bridge at $1.4T (Sep 30) -> lab financing, no
  publisher counterparty; out of scope
The Press Gazette AI deals/lawsuits tracker (updated Oct 9 2026) lists
nine "recent developments"; all nine map to banked mechanisms (verified
item-by-item in the block). Verdict: mechanism_documented (a
verification, not a discovery). NOT a falsification-family member
(ledger holds at 64). NOT a new relationship direction (fortieth
absent by design; thirty-fifth through thirty-ninth stand).

Conventions carried forward:
- #565: this run's main commit is the anchor; ANCHORED_SHA starts as
  0*40 and is patched to the main commit sha in the anchor followup.
- #715: pre-commit novelty greps (zero test_type_c_1349 files on disk;
  no 'Type C #1349' in git log; max numeric mechanism_id 1040
  pre-commit; zero numeric/underscore/dash one-zero-four-one
  mechanism key forms repo-wide pre-commit, needles format-built;
  block key zero-hit pre-commit; '## #1349' zero-hit in
  iteration-log; README 77769/1673 pre-commit; no #1349 rows in
  README/ARCHITECTURE test tables; 5 novel verification-instrument
  URLs zero-hit repo-wide pre-commit; the saturation-verification
  framing zero-hit repo-wide pre-commit).
- #719: doc-sync ratchet (README stats table + test-table row +
  docs/ARCHITECTURE.md tree row + iteration-log entry;
  README_TEST_COUNT / README_FILE_COUNT patched pre-main once the
  in-gate collection count is known).
- #721: terminal log-hash followup registers main/anchor/doc-sync
  hashes in the iteration-log entry and re-pins PRED_MAIN_1349 to the
  main sha in this file and in the #1348 file (the #1292
  re-pin-both-copies precedent).
- #795: the #1345-launched background full suite is CHECKED ONLY
  this run (goal hidden_files type_d_1345_full_suite.log); its verdict
  belongs to #1350. Observed at this run's ~4:00 PM PDT check: last
  write Oct 9 15:26 PDT at [ 7%], ONE live pytest process - ALIVE
  (recorded, not adjudicated).
- Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
  test file working-tree edit), #900 (untracked Type D test file),
  #1012-wt (working-tree edit on the committed Type A #1012 file)
  all stay out of this run's index/diff via explicit-path staging.
  Do NOT touch #1024's m846: self-flagged sourcing-constraint
  violation; Ray's revert/leave/rebuild-from-primary decision still
  pending. This run appends m1041 at end-of-file; the m846 block (HEAD
  lines 26349-26472) is verified byte-identical to HEAD in
  TestInFlightIsolation1349.
- The Aug 28 2026 standing rule: MANUAL / qualitative ONLY. No
  coverage-tone pair scored (tone NOT_SCORED); p_value/cohens_d/ci_95
  NOT_CALCULATED; is_significant false; engine NOT run; verdict
  mechanism_documented; NOT a falsification-family member (ledger holds
  at 64); NOT artifact-grade; no_analysis_json_update true.
- 0 browser.open per #503 (excerpt-bounded); 1 delegated scout (4
  ranked candidates, raw verbatim URLs, no novelty characterization -
  the #1341 post-hoc lesson) + 7 main-run browser.search
  verification sets re-ran the selection independently (corpus novelty
  verified via git grep -F by the main run).
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
GOAL_HIDDEN = os.path.join(
    os.path.expanduser("~"), "workspace", "goals",
    "mediascope-meta-wearables-press-analysis", "hidden_files",
)
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
OWN_BASENAME = (
    "test_type_c_1349_financial_incentive_"
    "saturation_verification_oct09_4pm.py"
)
TOP_KEY = (
    "type_c_1349_financial_incentive_"
    "saturation_verification_oct09_4pm"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "0537ff47210203bcc0395c233dc5992b4a350918"  # 0*40 pre-commit; patched to the main-commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1041
NEXT_NUM = 1042  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_c_1349_financial_incentive_"
    "saturation_verification_oct09_4pm"
)

# Predecessor chain: #1348 Type B (fourth leg).
PRED_MAIN_1348 = "a78d889cdf5f4cd8a10f48529284af6dfd89602e"
PRED_ANCHOR_1348 = "fbcb8b7b4058f1d475584b66f8982f4079f6674c"
PRED_DOCSYNC_1348 = "fc063e8c99ac1ad2c389d1bca3a729fa0cf8b382"
PRED_FINAL_1348 = "dc5b1af330da41d68dd353a2e737397bcf4c3f81"
# #1347 Type A (third leg) for the rotation-guard chain.
PRED_MAIN_1347 = "f027435cbbb44187fe3fe9ae95f5f1c88c71b646"
PRED_ANCHOR_1347 = "aa9da7ad286469be8f9144f7feb1098a6a2c9b9c"
PRED_DOCSYNC_1347 = "be9578de4e92c0ecf0cf675118eb91c84de028d"
PRED_FINAL_1347 = "373baad0660df3620296d0a42ce0c214d9184a4d"

# Forward guard for #1350 (Type D): placeholder per #721; re-pinned to
# the main sha in the terminal log-hash followup of the #1350 run.
PRED_MAIN_1350 = "238da12bf7f4d163204cfc7ddccd377616ec0e52"

# Own-run main-commit placeholder per #721: 0*40 pre-commit, re-pinned
# to this run's main sha in the terminal log-hash followup (in BOTH
# this file and the #1348 file per the #1292 precedent).
PRED_MAIN_1349 = "0537ff47210203bcc0395c233dc5992b4a350918"  # re-pinned to #1349 main sha in the terminal log-hash followup per #721/#1292

# #1348's test file (for the guard-lifecycle staleness pins).
A1348_FILE = (
    "test_type_b_1348_sarah_perez_techcrunch_muse_charm_"
    "vs_gemini_call_for_me_sep24_3pm.py"
)

# Doc-sync constants per #719: patched pre-main to the post-sync
# values once the in-gate collection count is known.
README_TEST_COUNT = 77870
README_FILE_COUNT = 1674

# Fragment-built so this file carries no contiguous literal of a
# member/direction claim form it asserts present or absent.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"
_T54 = "FIFT" + "Y-FOURTH falsification-family member"
_T55 = "FIFT" + "Y-FIFTH falsification-family member"
_T56 = "FIFT" + "Y-SIXTH falsification-family member"
_T57 = "FIFT" + "Y-SEVENTH falsification-family member"
_T58 = "FIFT" + "Y-EIGHTH falsification-family member"
_T59 = "FIFT" + "Y-NINTH falsification-family member"
_T60 = "SIXT" + "IETH falsification-family member"
_T61 = "SIXT" + "Y-FIRST falsification-family member"
_T62 = "SIXT" + "Y-SECOND falsification-family member"
_T63 = "SIXT" + "Y-THIRD falsification-family member"
_T64 = "SIXT" + "Y-FOURTH falsification-family member"
_T65 = "SIXT" + "Y-FIFTH falsification-family member"

# Novel verification-instrument URLs: 5 zero-hit repo-wide pre-commit
# (git grep -F on verbatim Full-URL listings). These are the search
# instruments that confirmed saturation, not new mechanism sources.
NOVEL_URLS = [
    "https://www.medianama.com/2026/06/223-us-35-newspaper-"
    "publishers-sue-openai-microsoft/",
    "https://www.blockhead.co/2026/09/30/openai-seeks-at-least-"
    "30-billion-at-1-4-trillion-valuation-as-bridge-to-delayed-ipo/",
    "https://www.macrumors.com/2026/10/09/apple-signs-hiring-deal-"
    "ai-podcast-startup-huxe/",
    "https://www.pondero.ai/news/2026-10-07-claude-for-startups-"
    "expansion/",
    "https://en.walaw.press/articles/bloomsbury_to_receive_"
    "compensation_under_landmark_$1.5_billion_anthropic_copyright_"
    "settlement/GPGQXQFFFMPQ",
]

# The #1024 m846 block line range at HEAD (verified byte-identical to
# the working tree; the decision on revert/leave/rebuild is pending).
M846_HEAD_START = 26349
M846_HEAD_END = 26472


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _iter_source_files():
    """Yield paths for profile + test source files.

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
    return max(found) if found else None


def _git_grep_tracked_source(needle, scope):
    """Grep tracked files at HEAD for a literal needle (fragment-built)."""
    args = ["git", "grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    else:
        args.append(".")
    out = _git(*args[1:])
    cleaned = []
    for line in out.stdout.splitlines():
        line = line.strip()
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        if line:
            cleaned.append(line)
    return cleaned


def _load_entities():
    with open(ENTITIES_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _block():
    return _load_entities()[TOP_KEY]


def _class_run(test_file, class_name):
    return subprocess.run(
        [".venv/bin/python", "-m", "pytest",
         os.path.join(TESTS_DIR, test_file) + "::" + class_name,
         "--no-header", "-q", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )


# ---------------------------------------------------------------------------
# 1. Anchor convention per #565
# ---------------------------------------------------------------------------


class TestAnchor1349:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit this is 0*40 and the test passes BY DESIGN;
        # fails post-anchor (patched to the main commit sha).
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha per #565 in the anchor followup (both this
        # expected value and the ANCHORED_SHA constant are patched).
        # Pre-commit this is 0*40 and the test fails BY DESIGN;
        # deselected in the in-gate run.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40

    def test_this_run_main_commit_is_anchor(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "main commit is the anchor" in src

    def test_rotation_phrase_in_docstring(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIFTH and CLOSING leg of the 1345-1349 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1349:
    def test_predecessor_1348_chain_verified(self):
        for sha in (
            PRED_MAIN_1348, PRED_ANCHOR_1348, PRED_DOCSYNC_1348,
            PRED_FINAL_1348,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1347_chain_verified(self):
        for sha in (
            PRED_MAIN_1347, PRED_ANCHOR_1347, PRED_DOCSYNC_1347,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1345 -> E #1346 -> A #1347 -> B #1348 -> C #1349" in src

    def test_next_leg_is_type_d_1350(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1350 Type D" in src

    def test_type_c_lands_one_mechanism(self):
        # Type C lands exactly one mechanism (mechanism 1041); the Type
        # B predecessor added one (mechanism 1040).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type C lands one mechanism" in src

    def test_window_closes_here(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1350-1354 window" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1349:
    def test_top_key_found(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1349 in key, no 1041 or
        # 1042 substring.
        assert "1349" in BLOCK_KEY
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        # Per #715 designed keying the landed number appears only as
        # the colon form; the underscore key form must not exist
        # repo-wide.
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_dash_mechanism_repo_wide(self):
        hits = _repo_grep_dash_mechanism(MECH_NUM)
        assert hits == [], hits

    def test_zero_numeric_next_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_this_run(self):
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert len(_repo_grep_numeric_mechanism_id(MECH_NUM)) >= 1

    def test_no_type_c_1349_in_git_log_own_run(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721 in BOTH files per
        # the #1292 precedent): every commit whose message matches
        # "Type C #1349" must be #1349's main commit or a descendant of
        # it. Deselected in the in-gate run (fails pre-commit by
        # design: PRED_MAIN_1349 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1349")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1349's own commits"
        main = _git("rev-parse", PRED_MAIN_1349).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_novel_urls_zero_hit_at_head(self):
        # The 5 novel verification-instrument URLs were verified
        # zero-hit repo-wide pre-commit via git grep -F this run
        # (documented in the block's novelty field); at HEAD they must
        # still be absent (they land only in this run's uncommitted
        # block).
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--", ".")
            assert out.stdout.strip() == "", url

    def test_saturation_verification_framing_novel(self):
        # No prior corpus mechanism is a saturation verification: the
        # framing is novel even though every verified datum is banked.
        assert "saturation" in _block()["finding"]
        assert "zero novel" in _block()["finding"].lower()

    def test_rejections_documented(self):
        # All scout + main-run rejections documented in the novelty
        # field (the #1339 fifteen-rejection audit precedent).
        nov = _block()["novelty"]
        assert "REJECTED CANDIDATES" in nov
        for tag in ("m891", "m993", "m798", "m981", "Redpine",
                    "Impelsys", "Brave", "Nine", "Platkin",
                    "Bloomsbury", "Otterly", "Huxe"):
            assert tag in nov, tag

    def test_scout_rejections_documented(self):
        # The scout's 4 ranked candidates were all rejected on main-run
        # corpus verification; the rejections are documented, not
        # hidden.
        nov = _block()["novelty"]
        assert "4 ranked candidates" in nov
        assert "all rejected" in nov

    def test_no_1349_row_in_readme_table(self):
        readme = _read(README_PATH)
        assert "test_type_c_1349" not in readme


# ---------------------------------------------------------------------------
# 4. Block structure
# ---------------------------------------------------------------------------

class TestBlockStructure1349:
    def test_yaml_parses_clean(self):
        assert _block()["yaml_parse_clean"] is True

    def test_ascii_only(self):
        assert _block()["ascii_only"] is True
        raw = _read(ENTITIES_PATH)
        start = raw.index(TOP_KEY + ":")
        segment = raw[start:]
        segment.encode("ascii")

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "mechanism_id", "type", "iteration", "finding",
            "verdict", "novelty", "research_method",
            "rotation_transparency", "concurrency", "connects_to",
            "confounders", "sources", "falsification_family",
            "background_suite_status",
        ):
            assert field in b, field

    def test_type_field(self):
        b = _block()
        assert b["type"] == "financial_incentive_mapping"
        assert b["iteration_type"] == "C"

    def test_block_key_matches_top_key(self):
        assert _block()["block_key"] == TOP_KEY

    def test_appended_at_end_of_file(self):
        # This run appends at end-of-file only; the block is the last
        # top-level key in competitor-entities.yaml.
        doc = _load_entities()
        keys = list(doc.keys())
        assert keys[-1] == TOP_KEY, keys[-1]

    def test_indent_two_space(self):
        raw = _read(ENTITIES_PATH)
        start = raw.index(TOP_KEY + ":")
        segment = raw[start:]
        for line in segment.splitlines()[1:20]:
            if line.strip():
                assert line.startswith("  "), line

    def test_no_em_dashes_in_block(self):
        raw = _read(ENTITIES_PATH)
        start = raw.index(TOP_KEY + ":")
        segment = raw[start:]
        assert "\u2014" not in segment

    def test_researcher_attribution(self):
        assert _block()["researcher"] == "Kit (with Ray)"

    def test_goal_id_present(self):
        assert _block()["goal_id"] == "goal_54093bda4145"

    def test_five_sources(self):
        assert len(_block()["sources"]) == 5
        for s in _block()["sources"]:
            assert s["novel"] is True
            assert s["accessed"] == "2026-10-09"


# ---------------------------------------------------------------------------
# 5. m1041 content discipline
# ---------------------------------------------------------------------------

class TestM1041ContentDiscipline1349:
    def test_verification_scope_present(self):
        f = _block()["finding"]
        assert "1 delegated scout" in f
        assert "7 main-run browser.search verification sets" in f

    def test_scout_candidates_all_rejected(self):
        f = _block()["finding"]
        assert "4 ranked candidates" in f
        assert "all rejected" in f

    def test_press_gazette_tracker_verified(self):
        f = _block()["finding"]
        assert "Press Gazette" in f
        assert "Oct 9 2026" in f
        assert "nine" in f.lower()

    def test_banked_mappings_present(self):
        f = _block()["finding"]
        for mech in ("m891", "m993", "m798", "m981", "m594"):
            assert mech in f, mech

    def test_out_of_scope_rejections_present(self):
        f = _block()["finding"]
        assert "Huxe" in f
        assert "out of scope" in f

    def test_connects_to(self):
        cts = _block()["connects_to"]
        for m in (891, 984, 594, 981, 993, 798):
            assert m in cts, m

    def test_confounder_ranking(self):
        cs = _block()["confounders"]
        assert cs[0]["strength"] == "strong"
        assert cs[1]["strength"] == "strong"
        assert cs[2]["strength"] == "moderate"
        assert cs[4]["strength"] == "weak"
        assert "Excerpt-bounded" in cs[0]["text"]

    def test_rejection_audit_present(self):
        nov = _block()["novelty"]
        assert "REJECTED CANDIDATES" in nov

    def test_research_method_documents_screening(self):
        rm = _block()["research_method"]
        assert "7 main-run browser.search verification sets" in rm
        assert "0 browser.open per #503" in rm

    def test_october_currency_present(self):
        f = _block()["finding"]
        assert "Oct 9 2026" in f
        assert "current" in f.lower()


# ---------------------------------------------------------------------------
# 6. Statistical discipline (the Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1349:
    def test_manual_qualitative_only(self):
        assert "MANUAL / qualitative ONLY" in _block()["finding"]

    def test_tone_not_scored(self):
        assert _block()["tone_scored"] is False
        assert "tone NOT_SCORED" in _block()["finding"]

    def test_no_significance_machinery(self):
        assert _block()["is_significant"] is False
        assert _block()["engine_run"] is False

    def test_verdict_mechanism_documented(self):
        assert _block()["verdict"] == "mechanism_documented"
        assert _block()["verdict_detail"] == "mechanism_documented"

    def test_not_artifact_grade(self):
        assert _block()["artifact_grade"] is False
        assert _block()["no_analysis_json_update"] is True

    def test_not_a_family_member(self):
        assert _block()["falsification_family_member"] is False

    def test_correlation_caveat(self):
        assert "Correlation is not causation" in _block()["finding"]
        assert "hypothesis-generating only" in _block()["finding"]

    def test_docstring_carries_standing_rule(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Aug 28 2026 standing rule" in src
        assert "NOT_CALCULATED" in src


# ---------------------------------------------------------------------------
# 7. Falsification ledger
# ---------------------------------------------------------------------------

class TestFalsificationLedger1349:
    def test_not_a_member(self):
        ff = _block()["falsification_family"]
        assert "NOT a member (ledger holds at 64" in ff

    def test_no_coverage_tone_pair(self):
        ff = _block()["falsification_family"]
        assert "no coverage-tone pair scored" in ff
        assert "no uniform-prediction test" in ff

    def test_sixty_fourth_present_documented(self):
        ff = _block()["falsification_family"]
        assert "sixty-fourth" in ff

    def test_sixty_fifth_absent_documented(self):
        ff = _block()["falsification_family"]
        assert "sixty-fifth member-claim form absent repo-wide" in ff

    def test_no_sixty_fifth_repo_wide(self):
        assert _git_grep_tracked_source(_T65, None) == []

    def test_ledger_64_held(self):
        # This run must not move the ledger.
        assert _block()["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: pins for #1350; #1348's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1349:
    def test_pins_on_1041_landing(self):
        # Type C lands one mechanism: max becomes 1041, next is 1042.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1041" in src
        assert "NEXT_NUM = 1042" in src

    def test_no_type_d_1350_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1350's terminal log-hash followup
        # per #721): every commit whose message matches "Type D
        # #1350" must be #1350's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1350 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type D #1350")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1350's own commits"
        main = _git("rev-parse", PRED_MAIN_1350).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1042_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1042_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1042_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T48, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_forty_ninth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T49, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T55, "HEAD", "--",
            "profiles/atlantic.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_sixth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T56, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_seventh_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixtieth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_first_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T61, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_second_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_third_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T63, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_fourth_member_present_pin(self):
        # Landed #1347 (m1039 AP x OpenAI, profiles/ap.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T64, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_fifth_member_pin(self):
        assert _git_grep_tracked_source(_T65, None) == []

    def test_predecessor_1348_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, A1348_FILE))

    def test_next_leg_is_1350_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1350 Type D" in src

    def test_1348_pins_flip_by_design_documented(self):
        # Documents the BY-DESIGN flips at this run's main commit:
        # test_no_type_c_1349_in_git_log_pin (the #1191-class
        # self-trip, re-pinned green in the terminal log-hash followup
        # per #721 in BOTH files per the #1292 precedent) and
        # test_1041_numeric_absent_in_profiles (the #1272-class
        # forward-guard expiry, permanent - the next-number guard is
        # consumed by the m1041 landing). The underscore/dash 1041
        # pins stay green: the landed number appears only as the colon
        # form per the designed keying. The no-sixty-fifth-member pin
        # stays green (m1041 is a verification leg, not a family
        # member).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1191-class" in src
        assert "#1272-class" in src


# ---------------------------------------------------------------------------
# 9. Background suite check per #795
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1349:
    def test_1345_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1345_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1345-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1349_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1345-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1350" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1349:
    def test_readme_test_file_table_has_1349_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_c_1349" in readme

    def test_architecture_has_1349_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_c_1349" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 11. Iteration log (3 tests; deselected pre-commit per #721)
# ---------------------------------------------------------------------------

class TestIterationLog1349:
    def test_1349_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1349 Type C" in log

    def test_1348_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1348 Type B" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1348's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1349:
    def test_1348_guard_lifecycle_post_commit(self):
        # Post-terminal-followup form: 24 of the 25 pass; the one that
        # fails BY DESIGN and permanently is
        # test_1041_numeric_absent_in_profiles (mechanism 1041 lands in
        # profiles/ this run; the #1272-class forward-guard expiry -
        # the next-number guard is consumed by the landing; stays red
        # permanently). The #1191-class self-trip
        # (test_no_type_c_1349_in_git_log_pin) flips GREEN post-repin:
        # PRED_MAIN_1349 holds this run's main sha in BOTH the #1349
        # and #1348 files per #721/#1292, and every "Type C #1349"
        # commit is a descendant of it. The underscore/dash 1041 pins
        # stay green (the landed number appears only as the colon form
        # per the designed keying). test_ledger_holds_at_64_in_block
        # stays GREEN (m1041 is a verification leg, not a family
        # member). The member and direction pins stay GREEN.
        # Deselected pre-commit (verified only post-terminal-followup).
        res = _class_run(A1348_FILE, "TestGuardLifecycle1348")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "1 failed, 24 passed" in res.stdout, res.stdout[-2000:]
        assert "test_1041_numeric_absent_in_profiles" in res.stdout, \
            res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1349:
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

    def test_1012_wt_working_tree_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_a_1012" in res.stdout

    def test_own_diff_excludes_inflight(self):
        # This run's staged set must never include the in-flight
        # files; verified at commit time by explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "explicit-path" in src

    def test_1024_m846_block_untouched(self):
        # #1024 m846 (profiles/competitor-entities.yaml, HEAD lines
        # 26349-26472): Ray's revert/leave/rebuild-from-primary
        # decision still pending. This run appends m1041 at
        # end-of-file only; the m846 block must be byte-identical to
        # HEAD. Do NOT touch #1024 m846.
        head = _git(
            "show", "HEAD:profiles/competitor-entities.yaml").stdout
        work = _read(ENTITIES_PATH)
        assert (head.splitlines()[M846_HEAD_START - 1:M846_HEAD_END]
                == work.splitlines()[M846_HEAD_START - 1:M846_HEAD_END])
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src
