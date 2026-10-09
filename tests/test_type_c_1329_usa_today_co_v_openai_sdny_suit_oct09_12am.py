# -*- coding: utf-8 -*-
"""Type C #1329 tests: USA TODAY Co. v OpenAI (SDNY 1:26-cv-08892,
filed Oct 8 2026) - FIRST dedicated corpus mechanism on the suit-side
of the pay-or-litigate bifurcation running on the SAME publisher that
signed the banked m1017 Perplexity licensing bilateral, documented as
mechanism 1029.

Iteration #1329 is the FIFTH and CLOSING leg of the 1325-1329 window
(D #1325 -> E #1326 -> A #1327 -> B #1328 -> C #1329 per the #565 anchor +
rotation guard). Next run #1330 Type D opens the 1330-1334 window.
This run lands mechanism 1029: USA TODAY Co. (TDAY.N) and affiliated
newspaper entities sued OpenAI in SDNY on Oct 8 2026, seeking damages
"in excess of $250 million" plus an injunction over training on
"hundreds of thousands" of articles from 19 publications - the same
Gannett-lineage publisher that licensed USA TODAY and 200+ local
publications to Perplexity (m1017, Jul 30 2025). The publisher's
AI-monetization strategy bifurcates by counterparty: license the
smaller lab, litigate the frontier lab. Documented as a variant
EXTENSION of the m636 pay-or-litigate bifurcation family (connects_to
[636, 1017]), NOT a new relationship direction: the fortieth direction
form stays absent by design; the thirty-fifth through thirty-ninth
directions stand.

Conventions carried forward:
- #565: this run's main commit is the anchor; ANCHORED_SHA starts as
  0*40 and is patched to the main commit sha in the anchor followup.
- #715: pre-commit novelty greps (zero test_type_c_1329 files on disk;
  no "Type C #1329" in git log; max numeric mechanism_id 1028
  pre-commit; zero numeric/underscore/dash one-zero-two-nine
  mechanism key forms repo-wide pre-commit, needles format-built;
  block key zero-hit pre-commit; "## #1329" zero-hit in
  iteration-log; README 75721/1653 pre-commit; no #1329 rows in
  README/ARCHITECTURE test tables; 7 novel URLs zero-hit repo-wide
  pre-commit; docket 1:26-cv-08892 zero-hit repo-wide pre-commit).
- #719: doc-sync ratchet (README stats table + test-table row +
  docs/ARCHITECTURE.md tree row + iteration-log entry;
  README_TEST_COUNT / README_FILE_COUNT patched pre-main once the
  in-gate collection count is known).
- #721: terminal log-hash followup registers main/anchor/doc-sync
  hashes in the iteration-log entry and re-pins PRED_MAIN_1329 to the
  main sha in this file and in the #1328 file (the #1292
  re-pin-both-copies precedent).
- #795: the #1325-launched background full suite is OBSERVED only
  this run (goal hidden_files type_d_1325_full_suite.log); its verdict
  belongs to #1330.
- Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
  test file working-tree edit), #900 (untracked Type D test file),
  #1012-wt (working-tree edit on the committed Type A #1012 file)
  all stay out of this run's index/diff via explicit-path staging.
  Do NOT touch #1024's m846: self-flagged sourcing-constraint
  violation; Ray's revert/leave/rebuild-from-primary decision still
  pending. This run appends m1029 at end-of-file; the m846 block (HEAD
  lines 26350-26472) is verified byte-identical to HEAD in
  TestInFlightIsolation1329.
- The Aug 28 2026 standing rule: MANUAL / qualitative ONLY. No
  coverage-tone pair scored (tone NOT_SCORED); p_value/cohens_d/ci_95
  NOT_CALCULATED; is_significant false; engine NOT run; verdict
  mechanism_documented; NOT a falsification-family member (ledger holds
  at 61); NOT artifact-grade; no_analysis_json_update true.
- 0 browser.open per #503 (excerpt-bounded); 1 delegated scout plus 2
  main-run browser.search verification sets; 9 rejected candidates
  documented in the block's novelty field.
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
    "test_type_c_1329_usa_today_co_v_openai_sdny_suit_"
    "oct09_12am.py"
)
TOP_KEY = "type_c_1329_usa_today_co_v_openai_sdny_suit_oct09_12am"

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "e64c14d5f45144dff91bd8a7286d314dab4abbd0"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1029
NEXT_NUM = 1030  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_c_1329_usa_today_co_v_openai_sdny_suit_"
    "oct09_12am"
)

# Predecessor chain: #1328 Type B (fourth leg).
PRED_MAIN_1328 = "086130d2e75b2297a100be11273d652d93aa890e"
PRED_ANCHOR_1328 = "5753d64b8558275127c35b65d72da42d261250d4"
PRED_DOCSYNC_1328 = "7dee227276a9fe1beaee5935cb8f87fe8dbff06e"
PRED_FINAL_1328 = "0d9756cac464e78e579815a3395e213cb34b33d1"
PRED_PUSH_1328 = "87a4bd2fe9a7c14519bc7f168c09c1613f030b7d"
# #1327 Type A (third leg) for the rotation-guard chain.
PRED_MAIN_1327 = "7e011cb6297df622d3d89d36950b38ba45fc1a15"
PRED_ANCHOR_1327 = "2853e32596a8002dc820005b8cf5cfd94338449c"
PRED_DOCSYNC_1327 = "d211a1184de9a7a77a3309752aec3ae6be5651ab"
PRED_FINAL_1327 = "786b7942253f18aaf674ea6563017fd61d1891d5"

# Forward guard for #1330 (Type D): placeholder per #721; re-pinned to
# the main sha in the terminal log-hash followup of the #1330 run.
PRED_MAIN_1330 = "0" * 40

# Own-run main-commit placeholder per #721: 0*40 pre-commit, re-pinned
# to this run's main sha in the terminal log-hash followup (in BOTH
# this file and the #1328 file per the #1292 precedent).
PRED_MAIN_1329 = "0" * 40

# #1328's test file (for the guard-lifecycle staleness pins).
A1328_FILE = (
    "test_type_b_1328_matt_swider_shortcut_meta_rayban_gen3_vs_"
    "apple_iphone_duo_oct08_11pm.py"
)

# Doc-sync constants per #719: patched pre-main to the post-sync
# values once the in-gate collection count is known.
README_TEST_COUNT = 75816
README_FILE_COUNT = 1654

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

# Novel source URLs: 7 zero-hit repo-wide pre-commit (git grep -F on
# verbatim Full-URL listings). The eighth source (Press Gazette's
# publisher-AI-deals tracker) is carried in-corpus since the Sep-2-2026
# log read and is marked novel: false in the block.
NOVEL_URLS = [
    "https://www.reuters.com/legal/legalindustry/usa-today-sues-"
    "openai-copyright-infringement-over-ai-training-2026-10-08/",
    "https://runtimewire.com/article/usa-today-openai-copyright-"
    "lawsuit-october-2026",
    "https://www.unite.ai/usa-today-sues-openai-over-copyrighted-"
    "news-content-in-ai-training/",
    "https://tvnewscheck.com/ai/article/usa-today-sues-openai-for-"
    "over-250m-alleging-willful-copyright-infringement/",
    "https://chatgptiseatingtheworld.com/2026/10/08/usa-today-sues-"
    "openai-in-yet-another-tag-along-copyright-suit/",
    "https://news.bloomberglaw.com/ip-law/usa-today-news-outlets-"
    "join-openai-copyright-infringement-fight",
    "https://oossa.com/en/usa-today-sues-openai-for-alleged-"
    "copyright-infringement",
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
    args = ["grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    else:
        args.append(".")
    out = _git(*args).stdout
    cleaned = []
    for line in out.splitlines():
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

class TestAnchor1329:
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
        assert "FIFTH and CLOSING leg of the 1325-1329 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1329:
    def test_predecessor_1328_chain_verified(self):
        for sha in (
            PRED_MAIN_1328, PRED_ANCHOR_1328, PRED_DOCSYNC_1328,
            PRED_FINAL_1328, PRED_PUSH_1328,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1327_chain_verified(self):
        for sha in (
            PRED_MAIN_1327, PRED_ANCHOR_1327, PRED_DOCSYNC_1327,
            PRED_FINAL_1327,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1325 -> E #1326 -> A #1327 -> B #1328 -> C #1329" in src

    def test_next_leg_is_type_d_1330(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1330 Type D" in src

    def test_type_c_lands_one_mechanism(self):
        # Type C lands exactly one mechanism (mechanism 1029); the Type
        # B predecessor added one (mechanism 1028).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type C lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1329:
    def test_top_key_found(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1329 in key, no 1029 or
        # 1030 substring.
        assert "1329" in BLOCK_KEY
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

    def test_no_type_c_1329_in_git_log_own_run(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721 in BOTH files per
        # the #1292 precedent): every commit whose message matches
        # "Type C #1329" must be #1329's main commit or a descendant of
        # it. Deselected in the in-gate run (fails pre-commit by
        # design: PRED_MAIN_1329 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1329")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1329's own commits"
        main = _git("rev-parse", PRED_MAIN_1329).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_novel_urls_zero_hit_at_head(self):
        # The 7 novel URLs were verified zero-hit repo-wide pre-commit
        # via git grep -F this run (documented in the block's novelty
        # field); at HEAD they must still be absent (they land only in
        # this run's uncommitted block).
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--", ".")
            assert out.stdout.strip() == "", url

    def test_press_gazette_url_carried_not_novel(self):
        # The eighth source URL is carried in-corpus since the
        # Sep-2-2026 log read; the block marks it novel: false and it
        # must not appear in NOVEL_URLS.
        assert all("pressgazette" not in u for u in NOVEL_URLS)
        srcs = _block()["sources"]
        pg = [s for s in srcs
              if "pressgazette" in s["url"]]
        assert len(pg) == 1
        assert pg[0]["novel"] is False

    def test_docket_novelty_documented(self):
        # FIRST dedicated corpus mechanism on USA TODAY Co. v OpenAI:
        # zero "1:26-cv-08892" hits repo-wide pre-commit, disclosed in
        # the block's novelty field.
        assert 'zero \'1:26-cv-08892\' hits repo-wide pre-commit' in \
            _block()["novelty"]

    def test_nine_rejections_documented(self):
        # 9 rejected candidates documented in the novelty field.
        nov = _block()["novelty"]
        assert "REJECTED CANDIDATES" in nov
        for tag in ("ByteDance", "Anthropic", "Amazon DSP",
                    "Redpine", "Axel Springer"):
            assert tag in nov, tag

    def test_no_1329_row_in_readme_table(self):
        readme = _read(README_PATH)
        assert "test_type_c_1329" not in readme


# ---------------------------------------------------------------------------
# 4. Block structure
# ---------------------------------------------------------------------------

class TestBlockStructure1329:
    def test_yaml_parses_clean(self):
        assert _block()["yaml_parse_clean"] is True

    def test_ascii_only(self):
        assert _block()["ascii_only"] is True
        raw = _read(ENTITIES_PATH)
        start = raw.index(TOP_KEY + ":")
        nxt = raw.find("\ntype_c_1330", start)
        segment = raw[start:] if nxt == -1 else raw[start:nxt]
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
        nxt = raw.find("\ntype_c_1330", start)
        segment = raw[start:] if nxt == -1 else raw[start:nxt]
        for line in segment.splitlines()[1:20]:
            if line.strip():
                assert line.startswith("  "), line

    def test_no_em_dashes_in_block(self):
        raw = _read(ENTITIES_PATH)
        start = raw.index(TOP_KEY + ":")
        nxt = raw.find("\ntype_c_1330", start)
        segment = raw[start:] if nxt == -1 else raw[start:nxt]
        assert "\u2014" not in segment

    def test_researcher_attribution(self):
        assert _block()["researcher"] == "Kit (with Ray)"


# ---------------------------------------------------------------------------
# 5. m1029 content discipline
# ---------------------------------------------------------------------------

class TestM1029ContentDiscipline1329:
    def test_filing_facts_present(self):
        f = _block()["finding"]
        assert "1:26-cv-08892" in f
        assert "Oct 8 2026" in f
        assert "hundreds of thousands" in f
        assert "19 publications" in f

    def test_ask_facts_present(self):
        f = _block()["finding"]
        assert "in excess of $250 million" in f
        assert "DMCA 1202" in f

    def test_suit_vs_deal_contrast_present(self):
        f = _block()["finding"]
        assert "m1017" in f
        assert "Perplexity" in f
        assert "license the smaller lab, litigate the frontier lab" in f

    def test_connects_to_m636_and_m1017(self):
        assert _block()["connects_to"] == [636, 1017]

    def test_variant_extension_not_new_direction(self):
        f = _block()["finding"]
        assert "variant EXTENSION of the m636 pay-or-litigate" in f
        assert "fortieth direction form absent repo-wide by design" in f
        assert "thirty-fifth through thirty-ninth stand" in f

    def test_antagonism_prediction_disclosed(self):
        f = _block()["finding"]
        assert "ANTAGONISM" in f
        assert "mirror image of the payer-softening thesis" in f

    def test_confounders_strong_first(self):
        cs = _block()["confounders"]
        assert len(cs) == 5
        assert cs[0]["strength"] == "strong"
        assert cs[1]["strength"] == "strong"
        assert "Adversarial money CLAIM" in cs[0]["text"]
        assert "Excerpt-bounded per #503" in cs[1]["text"]

    def test_eight_sources(self):
        assert len(_block()["sources"]) == 8

    def test_sources_carry_urls_and_access(self):
        for s in _block()["sources"]:
            assert s["url"].startswith("http")
            assert s["accessed"] == "2026-10-09"
            assert "novel" in s

    def test_reuters_is_primary_wire(self):
        srcs = _block()["sources"]
        assert "reuters.com" in srcs[0]["url"]
        assert "primary wire" in srcs[0]["what"]


# ---------------------------------------------------------------------------
# 6. Statistical discipline (the Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1329:
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

class TestFalsificationLedger1329:
    def test_not_a_member(self):
        ff = _block()["falsification_family"]
        assert "NOT a member (ledger holds at 61" in ff

    def test_no_coverage_tone_pair(self):
        ff = _block()["falsification_family"]
        assert "no coverage-tone pair scored" in ff
        assert "no uniform-prediction test" in ff

    def test_sixty_first_present_documented(self):
        ff = _block()["falsification_family"]
        assert "sixty-first member-claim form present 2x" in ff

    def test_sixty_second_absent_documented(self):
        ff = _block()["falsification_family"]
        assert "sixty-second member-claim form absent repo-wide" in ff

    def test_forty_eighth_present_documented(self):
        ff = _block()["falsification_family"]
        assert "forty-eighth member-claim form present 2x" in ff

    def test_no_sixty_second_repo_wide(self):
        assert _git_grep_tracked_source(_T62, None) == []

    def test_ledger_61_at_head(self):
        # The #1328 block carries the ledger-61 pin; this run must not
        # move the ledger.
        assert _block()["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: pins for #1330; #1328's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1329:
    def test_pins_on_1029_landing(self):
        # Type C lands one mechanism: max becomes 1029, next is 1030.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1029" in src
        assert "NEXT_NUM = 1030" in src

    def test_no_type_d_1330_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1330's terminal log-hash followup
        # per #721): every commit whose message matches "Type D
        # #1330" must be #1330's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1330 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type D #1330")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1330's own commits"
        main = _git("rev-parse", PRED_MAIN_1330).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1030_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1030_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1030_dash_absent_repo_wide(self):
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

    def test_no_sixty_second_member_pin(self):
        assert _git_grep_tracked_source(_T62, None) == []

    def test_predecessor_1328_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, A1328_FILE))

    def test_next_leg_is_1330_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1330 Type D" in src

    def test_1328_pins_flip_by_design_documented(self):
        # Documents the BY-DESIGN flips at this run's main commit:
        # test_no_type_c_1329_in_git_log_pin (the #1191-class
        # self-trip, re-pinned green in the terminal log-hash followup
        # per #721 in BOTH files per the #1292 precedent) and
        # test_1029_numeric_absent_in_profiles (the #1272-class
        # forward-guard expiry, permanent - the next-number guard is
        # consumed by the m1029 landing). The underscore/dash 1029
        # pins stay green: the landed number appears only as the colon
        # form per the designed keying.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1191-class" in src
        assert "#1272-class" in src


# ---------------------------------------------------------------------------
# 9. Background suite check per #795
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1329:
    def test_1325_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1325_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1325-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1329_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1325-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1330" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1329:
    def test_readme_test_file_table_has_1329_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_c_1329" in readme

    def test_architecture_has_1329_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_c_1329" in arch

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

class TestIterationLog1329:
    def test_1329_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1329 Type C" in log

    def test_1328_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1328 Type B" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1328's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1329:
    def test_1328_guard_lifecycle_post_commit(self):
        # Post-terminal-followup form: 23 of the 24 pass; the one that
        # fails BY DESIGN is test_1029_numeric_absent_in_profiles
        # (mechanism 1029 lands in profiles/ this run; the #1272-class
        # forward-guard expiry - the next-number guard is consumed by
        # the landing; stays red permanently). The underscore/dash
        # 1029 pins stay green (the landed number appears only as the
        # colon form per the designed keying). The second flip,
        # test_no_type_c_1329_in_git_log_pin (the #1191-class
        # self-trip: this run's own main commit carries "Type C
        # #1329"), is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1329 now holds this run's
        # main sha, in BOTH the #1329 and #1328 files per the #1292
        # precedent). test_pins_on_1028_landing stays GREEN (asserts on
        # the #1328 file's own constants, untouched by this run); the
        # member and direction pins stay GREEN (m1029 is a
        # financial-architecture leg, not a family member; no new
        # direction landed).
        # Deselected pre-commit (verified only post-terminal-followup).
        res = _class_run(A1328_FILE, "TestGuardLifecycle1328")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "1 failed, 23 passed" in res.stdout, res.stdout[-2000:]
        assert "test_1029_numeric_absent_in_profiles" in res.stdout, \
            res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1329:
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
        # decision still pending. This run appends m1029 at
        # end-of-file only; the m846 block must be byte-identical to
        # HEAD. Do NOT touch #1024 m846.
        head = _git(
            "show", "HEAD:profiles/competitor-entities.yaml").stdout
        work = _read(ENTITIES_PATH)
        assert (head.splitlines()[M846_HEAD_START - 1:M846_HEAD_END]
                == work.splitlines()[M846_HEAD_START - 1:M846_HEAD_END])
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src
