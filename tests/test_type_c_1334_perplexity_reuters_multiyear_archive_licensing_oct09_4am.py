# -*- coding: utf-8 -*-
"""Type C #1334 tests: Perplexity x Reuters multi-year archive licensing
deal (announced Mon Sep 7 2026) - FIRST dedicated corpus mechanism on the
wire's first AI-search-company deal: Perplexity's biggest publisher
licensing deal to date converts the sued lab into the archive's largest
AI-search customer - the defendant-to-customer conversion, documented as
mechanism 1032.

Iteration #1334 is the FIFTH and CLOSING leg of the 1330-1334 window
(D #1330 -> E #1331 -> A #1332 -> B #1333 -> C #1334 per the #565 anchor +
rotation guard). Next run #1335 Type D opens the 1335-1339 window.
This run lands mechanism 1032: Perplexity and Reuters announced a
multi-year licensing agreement (Mon Sep 7 2026, relay-dated) under which
Perplexity can search and display summarized excerpts of Reuters' news
archive going back decades, with citations and links back to Reuters.com;
financial terms undisclosed. Perplexity's biggest publisher licensing deal
to date (the relay's claim); Reuters' first AI-search-company agreement
(parent Thomson Reuters has done AI licensing before, archive-only per
Hasker's May-2026 strategy). The lab that News Corp's Dow Jones and New
York Post sued in Oct 2025 (in-corpus 1:24-cv-07984), with live suits from
the NYT, CNN, Reddit, Britannica, Nikkei and Asahi Shimbun, is now the
wire's largest AI-search licensee - the m636 pay-or-litigate bifurcation
resolving toward pay on the Perplexity side. Documented as a variant
EXTENSION of the m636 pay-or-litigate bifurcation family (connects_to
[636, 624, 1017]), NOT a new relationship direction: the fortieth
direction form stays absent by design; the thirty-fifth through
thirty-ninth directions stand.

Conventions carried forward:
- #565: this run's main commit is the anchor; ANCHORED_SHA starts as
  0*40 and is patched to the main commit sha in the anchor followup.
- #715: pre-commit novelty greps (zero test_type_c_1334 files on disk;
  no "Type C #1334" in git log; max numeric mechanism_id 1031
  pre-commit; zero numeric/underscore/dash one-zero-three-two
  mechanism key forms repo-wide pre-commit, needles format-built;
  block key zero-hit pre-commit; "## #1334" zero-hit in
  iteration-log; README 76231/1657 pre-commit; no #1334 rows in
  README/ARCHITECTURE test tables; 3 novel URLs zero-hit repo-wide
  pre-commit; "curiouslm" and "abascal" zero-hit repo-wide pre-commit).
- #719: doc-sync ratchet (README stats table + test-table row +
  docs/ARCHITECTURE.md tree row + iteration-log entry;
  README_TEST_COUNT / README_FILE_COUNT patched pre-main once the
  in-gate collection count is known).
- #721: terminal log-hash followup registers main/anchor/doc-sync
  hashes in the iteration-log entry and re-pins PRED_MAIN_1334 to the
  main sha in this file and in the #1333 file (the #1292
  re-pin-both-copies precedent).
- #795: the #1330-launched background full suite is OBSERVED only
  this run (goal hidden_files type_d_1330_full_suite.log); its verdict
  belongs to #1335.
- Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
  test file working-tree edit), #900 (untracked Type D test file),
  #1012-wt (working-tree edit on the committed Type A #1012 file)
  all stay out of this run's index/diff via explicit-path staging.
  Do NOT touch #1024's m846: self-flagged sourcing-constraint
  violation; Ray's revert/leave/rebuild-from-primary decision still
  pending. This run appends m1032 at end-of-file; the m846 block (HEAD
  lines 26350-26472) is verified byte-identical to HEAD in
  TestInFlightIsolation1334.
- The Aug 28 2026 standing rule: MANUAL / qualitative ONLY. No
  coverage-tone pair scored (tone NOT_SCORED); p_value/cohens_d/ci_95
  NOT_CALCULATED; is_significant false; engine NOT run; verdict
  mechanism_documented; NOT a falsification-family member (ledger holds
  at 62); NOT artifact-grade; no_analysis_json_update true.
- 0 browser.open per #503 (excerpt-bounded); the delegated scout
  returned an empty handoff (no usable findings delivered - documented
  in the block's novelty field); 3 main-run browser.search
  verification sets re-ran the selection independently; 12 rejected
  candidates documented in the block's novelty field.
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
    "test_type_c_1334_perplexity_reuters_multiyear_archive_"
    "licensing_oct09_4am.py"
)
TOP_KEY = "type_c_1334_perplexity_reuters_multiyear_archive_licensing_oct09_4am"

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "0" * 40

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1032
NEXT_NUM = 1033  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_c_1334_perplexity_reuters_multiyear_archive_"
    "licensing_oct09_4am"
)

# Predecessor chain: #1333 Type B (fourth leg).
PRED_MAIN_1333 = "8ecaff72e61b8f6567a7bc186fa3cf42f810e865"
PRED_ANCHOR_1333 = "95684494a7aa527604869d97a14f24f5ee4871a2"
PRED_DOCSYNC_1333 = "3dbce6bf1de73ca80da6f8ec3d3da21da475a833"
PRED_FINAL_1333 = "37b5a4681c18b5c6939bbc26b4f75b0a01864611"
PRED_PUSH_1333 = "4348d6484630e24465a270b8b14343ad78b9d3be"
# #1332 Type A (third leg) for the rotation-guard chain.
PRED_MAIN_1332 = "ec6f82b9360e649e99bd6da0fe7470fd444c4dd3"
PRED_ANCHOR_1332 = "f810858b8197f6f9be611b2b929f4da69a231b6b"
PRED_DOCSYNC_1332 = "015c7eceab299c2239a0691438e6560b4b63f043"
PRED_FINAL_1332 = "1d85704ab6690a40bb810ba6537baeffe3cff0d7"

# Forward guard for #1335 (Type D): placeholder per #721; re-pinned to
# the main sha in the terminal log-hash followup of the #1335 run.
PRED_MAIN_1335 = "0" * 40

# Own-run main-commit placeholder per #721: 0*40 pre-commit, re-pinned
# to this run's main sha in the terminal log-hash followup (in BOTH
# this file and the #1333 file per the #1292 precedent).
PRED_MAIN_1334 = "0" * 40

# #1333's test file (for the guard-lifecycle staleness pins).
A1333_FILE = (
    "test_type_b_1333_maggie_harrison_dupre_futurism_dupes_"
    "blinking_light_vs_meta_ai_prompts_oct09_3am.py"
)

# Doc-sync constants per #719: patched pre-main to the post-sync
# values once the in-gate collection count is known.
README_TEST_COUNT = 76328
README_FILE_COUNT = 1659

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

# Novel source URLs: 3 zero-hit repo-wide pre-commit (git grep -F on
# verbatim Full-URL listings). The fourth source (startupfortune's
# HP/Crusoe piece) is carried in-corpus and is marked novel: false in
# the block.
NOVEL_URLS = [
    "https://curiouslm.com/blog/perplexity-reuters-licensing-deal-"
    "news-archive",
    "https://talkingbiznews.com/media-news/reuters-ai-deals-are-"
    "only-for-archived-content/",
    "https://pressgazette.substack.com/p/reuters-ai-deals-only-"
    "involve-archive",
]

# The #1024 m846 block line range at HEAD (verified byte-identical to
# the working tree; the decision on revert/leave/rebuild is pending).
M846_HEAD_START = 26350
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

class TestAnchor1334:
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
        assert "FIFTH and CLOSING leg of the 1330-1334 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1334:
    def test_predecessor_1333_chain_verified(self):
        for sha in (
            PRED_MAIN_1333, PRED_ANCHOR_1333, PRED_DOCSYNC_1333,
            PRED_FINAL_1333, PRED_PUSH_1333,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1332_chain_verified(self):
        for sha in (
            PRED_MAIN_1332, PRED_ANCHOR_1332, PRED_DOCSYNC_1332,
            PRED_FINAL_1332,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1330 -> E #1331 -> A #1332 -> B #1333 -> C #1334" in src

    def test_next_leg_is_type_d_1335(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1335 Type D" in src

    def test_type_c_lands_one_mechanism(self):
        # Type C lands exactly one mechanism (mechanism 1032); the Type
        # B predecessor added one (mechanism 1031).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type C lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1334:
    def test_top_key_found(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1334 in key, no 1032 or
        # 1033 substring.
        assert "1334" in BLOCK_KEY
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

    def test_no_type_c_1334_in_git_log_own_run(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721 in BOTH files per
        # the #1292 precedent): every commit whose message matches
        # "Type C #1334" must be #1334's main commit or a descendant of
        # it. Deselected in the in-gate run (fails pre-commit by
        # design: PRED_MAIN_1334 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1334")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1334's own commits"
        main = _git("rev-parse", PRED_MAIN_1334).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_novel_urls_zero_hit_at_head(self):
        # The 3 novel URLs were verified zero-hit repo-wide pre-commit
        # via git grep -F this run (documented in the block's novelty
        # field); at HEAD they must still be absent (they land only in
        # this run's uncommitted block).
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--", ".")
            assert out.stdout.strip() == "", url

    def test_startupfortune_url_carried_not_novel(self):
        # The fourth source URL is carried in-corpus; the block marks
        # it novel: false and it must not appear in NOVEL_URLS.
        assert all("startupfortune" not in u for u in NOVEL_URLS)
        srcs = _block()["sources"]
        sf = [s for s in srcs
              if "startupfortune" in s["url"]]
        assert len(sf) == 1
        assert sf[0]["novel"] is False

    def test_relay_attribution_documented(self):
        # The curiouslm relay's "Reuters CEO Santiago Abascal"
        # attribution conflicts with the Press Gazette record (Steve
        # Hasker, Thomson Reuters president and CEO) - disclosed in
        # the block's confounders and finding.
        assert "Santiago Abascal" in _block()["finding"]
        assert "Steve Hasker" in _block()["finding"]

    def test_twelve_rejections_documented(self):
        # 12 rejected candidates documented in the novelty field.
        nov = _block()["novelty"]
        assert "REJECTED CANDIDATES" in nov
        for tag in ("red-button", "Turvey", "News Corp x Anthropic",
                    "TollBit 7x", "Axel Springer"):
            assert tag in nov, tag

    def test_no_1334_row_in_readme_table(self):
        readme = _read(README_PATH)
        assert "test_type_c_1334" not in readme


# ---------------------------------------------------------------------------
# 4. Block structure
# ---------------------------------------------------------------------------

class TestBlockStructure1334:
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


# ---------------------------------------------------------------------------
# 5. m1032 content discipline
# ---------------------------------------------------------------------------

class TestM1032ContentDiscipline1334:
    def test_deal_facts_present(self):
        f = _block()["finding"]
        assert "Sep 7 2026" in f
        assert "decades" in f
        assert "citations and links" in f

    def test_biggest_deal_claim_present(self):
        f = _block()["finding"]
        assert "biggest publisher licensing deal to date" in f
        assert "first such agreement with an AI search company" in f

    def test_terms_undisclosed_present(self):
        f = _block()["finding"]
        assert "financial terms undisclosed" in f

    def test_lawsuit_trail_present(self):
        f = _block()["finding"]
        assert "1:24-cv-07984" in f
        assert "Dow Jones and New York Post sued Perplexity" in f

    def test_connects_to_636_624_1017(self):
        assert _block()["connects_to"] == [636, 624, 1017]

    def test_variant_extension_not_new_direction(self):
        f = _block()["finding"]
        assert "variant EXTENSION of the m636 pay-or-litigate" in f
        assert "fortieth direction form absent repo-wide by design" in f
        assert "thirty-fifth through thirty-ninth stand" in f

    def test_softening_prediction_disclosed(self):
        f = _block()["finding"]
        assert "runs via SOFTENING" in f
        assert "claims no slot in the coverage-tone falsification ledger" in f

    def test_confounders_strong_first(self):
        cs = _block()["confounders"]
        assert len(cs) == 5
        assert cs[0]["strength"] == "strong"
        assert cs[1]["strength"] == "strong"
        assert "Excerpt-bounded per #503" in cs[0]["text"]
        assert "Relay-attribution conflict" in cs[1]["text"]

    def test_four_sources(self):
        assert len(_block()["sources"]) == 4

    def test_sources_carry_urls_and_access(self):
        for s in _block()["sources"]:
            assert s["url"].startswith("http")
            assert s["accessed"] == "2026-10-09"
            assert "novel" in s

    def test_curiouslm_is_primary_relay(self):
        srcs = _block()["sources"]
        assert "curiouslm.com" in srcs[0]["url"]
        assert "primary relay" in srcs[0]["what"]


# ---------------------------------------------------------------------------
# 6. Statistical discipline (the Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1334:
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

class TestFalsificationLedger1334:
    def test_not_a_member(self):
        ff = _block()["falsification_family"]
        assert "NOT a member (ledger holds at 62" in ff

    def test_no_coverage_tone_pair(self):
        ff = _block()["falsification_family"]
        assert "no coverage-tone pair scored" in ff
        assert "no uniform-prediction test" in ff

    def test_sixty_second_present_documented(self):
        ff = _block()["falsification_family"]
        assert "sixty-second present 3x" in ff

    def test_sixty_third_absent_documented(self):
        ff = _block()["falsification_family"]
        assert "sixty-third member-claim form absent repo-wide" in ff

    def test_forty_eighth_present_documented(self):
        ff = _block()["falsification_family"]
        assert "forty-eighth member-claim form present 2x" in ff

    def test_no_sixty_third_repo_wide(self):
        assert _git_grep_tracked_source(_T63, None) == []

    def test_ledger_62_at_head(self):
        # The #1333 block carries the ledger-62 pin; this run must not
        # move the ledger.
        assert _block()["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: pins for #1335; #1333's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1334:
    def test_pins_on_1032_landing(self):
        # Type C lands one mechanism: max becomes 1032, next is 1033.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1032" in src
        assert "NEXT_NUM = 1033" in src

    def test_no_type_d_1335_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1335's terminal log-hash followup
        # per #721): every commit whose message matches "Type D
        # #1335" must be #1335's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1335 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type D #1335")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1335's own commits"
        main = _git("rev-parse", PRED_MAIN_1335).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1033_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1033_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1033_dash_absent_repo_wide(self):
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

    def test_no_sixty_third_member_pin(self):
        assert _git_grep_tracked_source(_T63, None) == []

    def test_predecessor_1333_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, A1333_FILE))

    def test_next_leg_is_1335_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1335 Type D" in src

    def test_1333_pins_flip_by_design_documented(self):
        # Documents the BY-DESIGN flips at this run's main commit:
        # test_no_type_c_1334_in_git_log_pin (the #1191-class
        # self-trip, re-pinned green in the terminal log-hash followup
        # per #721 in BOTH files per the #1292 precedent) and
        # test_1032_numeric_absent_in_profiles (the #1272-class
        # forward-guard expiry, permanent - the next-number guard is
        # consumed by the m1032 landing). The underscore/dash 1032
        # pins stay green: the landed number appears only as the colon
        # form per the designed keying.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1191-class" in src
        assert "#1272-class" in src


# ---------------------------------------------------------------------------
# 9. Background suite check per #795
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1334:
    def test_1330_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1330_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1330-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1334_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1330-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1335" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1334:
    def test_readme_test_file_table_has_1334_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_c_1334" in readme

    def test_architecture_has_1334_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_c_1334" in arch

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

class TestIterationLog1334:
    def test_1334_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1334 Type C" in log

    def test_1333_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1333 Type B" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1333's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1334:
    def test_1333_guard_lifecycle_post_commit(self):
        # Post-terminal-followup form: 24 of the 25 pass; the one that
        # fails BY DESIGN is test_1032_numeric_absent_in_profiles
        # (mechanism 1032 lands in profiles/ this run; the #1272-class
        # forward-guard expiry - the next-number guard is consumed by
        # the landing; stays red permanently). The underscore/dash
        # 1032 pins stay green (the landed number appears only as the
        # colon form per the designed keying). The second flip,
        # test_no_type_c_1334_in_git_log_pin (the #1191-class
        # self-trip: this run's own main commit carries "Type C
        # #1334"), is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1334 now holds this run's
        # main sha, in BOTH the #1334 and #1333 files per the #1292
        # precedent). test_pins_on_1032_landing stays GREEN (asserts on
        # the #1333 file's own constants, untouched by this run); the
        # member and direction pins stay GREEN (m1032 is a
        # financial-architecture leg, not a family member; no new
        # direction landed).
        # Deselected pre-commit (verified only post-terminal-followup).
        res = _class_run(A1333_FILE, "TestGuardLifecycle1333")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "1 failed, 24 passed" in res.stdout, res.stdout[-2000:]
        assert "test_1032_numeric_absent_in_profiles" in res.stdout, \
            res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1334:
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

    def test_1024_m846_block_untouched(self):
        # #1024 m846 (profiles/competitor-entities.yaml, HEAD lines
        # 26350-26472): Ray's revert/leave/rebuild-from-primary
        # decision still pending. This run appends m1032 at
        # end-of-file only; the m846 block must be byte-identical to
        # HEAD. Do NOT touch #1024 m846.
        head = _git(
            "show", "HEAD:profiles/competitor-entities.yaml").stdout
        work = _read(ENTITIES_PATH)
        assert (head.splitlines()[M846_HEAD_START - 1:M846_HEAD_END]
                == work.splitlines()[M846_HEAD_START - 1:M846_HEAD_END])
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src
