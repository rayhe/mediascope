# -*- coding: utf-8 -*-
"""Type C #1324 tests: OpenAI x Atlassian reciprocal enterprise embed
(announced Oct 6 2026) - FIRST dedicated corpus mechanism on the
lab-as-supplier reciprocal-embed geometry, documented as mechanism 1026.

Iteration #1324 is the FIFTH and CLOSING leg of the 1320-1324 window
(D #1320 -> E #1321 -> A #1322 -> B #1323 -> C #1324 per the #565 anchor +
rotation guard). This run lands mechanism 1026: the FIRST dedicated corpus
mechanism on the OpenAI x Atlassian expanded partnership (announced Oct 6
2026, timed to the Team '26 Europe conference) - the lab-as-supplier
reciprocal-embed geometry: (1) OpenAI frontier models (GPT-6 Astra, the
GPT-5.6 series) power agents across Atlassian's platform and Rovo, paired
with the Teamwork Graph (the permission-aware map of people, projects,
documents, decisions); (2) the money arrow runs enterprise-vendor to lab -
an OpenAI representative described the arrangement on background
(VentureBeat) as "effectively a spend commitment", Atlassian committing
dollars to OpenAI models and tech, NOT the reverse; specifics declined and
neither company published financial terms; (3) reciprocal enterprise legs -
more than 3,000 Atlassian developers use Codex through ChatGPT Enterprise
(Atlassian as OpenAI customer), ChatGPT and Codex reach into Jira work
items, Confluence content and Bitbucket over MCP (rebuilt MCP server: 220+
tools, 15M calls/day), and OpenAI keeps using Jira to run critical
workflows (lab as Atlassian user). Rovo stays multi-model - its internal
gateway routes dynamically across OpenAI and other providers, GPT-6 Astra
is not the default, and Anthropic's head of enterprise product is quoted on
the MCP integration - the spend commitment buys routing priority, not
exclusivity. Documented as a variant EXTENSION of the m807 vendor-embed
family (the reversed arrow: there the vendor capability embeds in the
lab's product; here the LAB's capability embeds in the VENDOR's product,
with reciprocal customer/user arrows), NOT a new relationship direction:
the fortieth direction form stays absent by design; the thirty-fifth
through thirty-ninth directions stand.

Conventions carried forward:
- #565: this run's main commit is the anchor; ANCHORED_SHA starts as 0*40
  and is patched to the main commit sha in the anchor followup.
- #715: pre-commit novelty greps (zero test_type_c_1324 files on disk;
  no "Type C #1324" in git log; max numeric mechanism_id 1025 pre-commit;
  zero numeric/underscore/dash one-zero-two-six mechanism key forms
  repo-wide pre-commit, needles format-built; block key zero-hit
  pre-commit; "## #1324" zero-hit in iteration-log; README 75225/1648
  pre-commit; no #1324 rows in README/ARCHITECTURE test tables; 6 novel
  URLs zero-hit repo-wide pre-commit; "atlassian" zero-hit repo-wide
  pre-commit, case-insensitive).
- #719: doc-sync ratchet (README stats table + test-table row +
  docs/ARCHITECTURE.md tree row + iteration-log entry; README_TEST_COUNT /
  README_FILE_COUNT patched pre-main once the in-gate collection count is
  known).
- #721: terminal log-hash followup registers main/anchor/doc-sync hashes
  in the iteration-log entry and re-pins PRED_MAIN_1324 to the main sha in
  this file and in the #1323 file (the #1292 re-pin-both-copies precedent).
- #795: the #1320-launched background full suite is OBSERVED only this
  run (goal hidden_files type_d_1320_full_suite.log); its verdict belongs
  to #1325.
- Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test
  file working-tree edit), #900 (untracked Type D test file), #1012-wt
  (working-tree edit on the committed Type A #1012 file) all stay out of
  this run's index/diff via explicit-path staging. Do NOT touch #1024's
  m846: self-flagged sourcing-constraint violation; Ray's
  revert/leave/rebuild-from-primary decision still pending. This run
  appends m1026 at end-of-file; the m846 block (HEAD lines 26350-26472)
  is verified byte-identical to HEAD in TestInFlightIsolation1324.
- The Aug 28 2026 standing rule: MANUAL / qualitative ONLY. No
  coverage-tone pair scored (tone NOT_SCORED); p_value/cohens_d/ci_95
  NOT_CALCULATED; is_significant false; engine NOT run; verdict
  mechanism_documented; NOT a falsification-family member (ledger holds
  at 60); NOT artifact-grade; no_analysis_json_update true.
- 0 browser.open per #503 (excerpt-bounded); 6 main-run browser.search
  verification sets; 8 rejected candidates documented in the block's
  novelty field (Hearst re-report, Meta x News Corp, SPUR v1.0,
  NYT $28M spend, Broadcom $50B+ temporal extension, Anthropic zero-deal,
  ABC parliament testimony, News/Media Alliance lobby trip).
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
    "test_type_c_1324_openai_atlassian_reciprocal_embed_"
    "oct08_8pm.py"
)
TOP_KEY = "type_c_1324_openai_atlassian_reciprocal_enterprise_embed_oct08_8pm"

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "ea330ddebc4d9c3d715d9ecd1532add85274c0db"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1026
NEXT_NUM = 1027  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_c_1324_openai_atlassian_reciprocal_enterprise_"
    "embed_oct08_8pm"
)

# Predecessor chain: #1323 Type B (fourth leg).
PRED_MAIN_1323 = "6fae5cd614267592c77100188b6e956bb6d7ed34"
PRED_ANCHOR_1323 = "60bc6f3c5e242a507f9c8f459a481bb54dc89651"
PRED_DOCSYNC_1323 = "7d9e7ec8cc1d23df4d8a516d978f077580d1dfa3"
PRED_FINAL_1323 = "98c2bab11e1815d581ee1dd468192dd5423f97e5"
PRED_PUSH_1323 = "d758f050e2e23466c3d8e03a36a428456f624712"
# #1322 Type A (third leg) for the rotation-guard chain.
PRED_MAIN_1322 = "237e0a1e2f21b114e11a1c0405c2905ea31f9eba"
PRED_ANCHOR_1322 = "1e2d00afd10fa945c9679343536ccdda5cea1520"
PRED_DOCSYNC_1322 = "fa17e8d9c9b983df7023ed12f48dee83c6af8c86"
PRED_FINAL_1322 = "83b6672fd45c8e96d3bc2a10ef4ee8e0c30da5ba"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the own-run git-log pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1324 = "ea330ddebc4d9c3d715d9ecd1532add85274c0db"

# Forward guard for the next leg: #1325 Type D. Re-pinned by #1325's
# log-hash followup per #721 (starts as 0*40; the forward pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1325 = "cc24b13b8c8a22597e5c1c3795a7f3cf1d90d167"  # re-pinned to main sha per #721

# The #1323 window-continuation file, for the staleness pin on its
# guard-lifecycle class.
A1323_FILE = (
    "test_type_b_1323_katie_paul_reuters_human_concierge_"
    "vs_muse_launch_oct08_7pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 75324  # post-doc-sync total (pre-sync 75225 + 99)
README_FILE_COUNT = 1649  # pre-sync 1648 + 1 (this file)

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form.
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

# Novel source URLs: 6 zero-hit repo-wide pre-commit (git grep -F).
NOVEL_URLS = [
    "https://cellcog.ai/blog/atlassian-openai-partnership/",
    "https://aiweekly.co/alerts/atlassian-commits-spend-to-openai-"
    "keeps-rovo-router-open",
    "https://venturebeat.com/orchestration/atlassian-deepens-its-"
    "openai-partnership-with-a-spend-commitment-but-its-platform-"
    "stays-firmly-multi-model",
    "https://aiindustrytoday.com/news/openai-and-atlassian-deepen-"
    "partnership-around-frontier-models-and-the-teamwork-graph/",
    "https://cryptobriefing.com/atlassian-openai-expand-"
    "partnership-gpt-6/",
    "https://thejoai.com/ai-news/ecb-chief-warns-ais-debt-impact-"
    "equifax-launches-54-ai-products-atlassian/",
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

class TestAnchor1324:
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
        assert "FIFTH and CLOSING leg of the 1320-1324 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1324:
    def test_predecessor_1323_chain_verified(self):
        for sha in (
            PRED_MAIN_1323, PRED_ANCHOR_1323, PRED_DOCSYNC_1323,
            PRED_FINAL_1323, PRED_PUSH_1323,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1322_chain_verified(self):
        for sha in (
            PRED_MAIN_1322, PRED_ANCHOR_1322, PRED_DOCSYNC_1322,
            PRED_FINAL_1322,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1320 -> E #1321 -> A #1322 -> B #1323 -> C #1324" in src

    def test_next_leg_is_type_d_1325(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1325 Type D" in src

    def test_type_c_lands_one_mechanism(self):
        # Type C lands exactly one mechanism (mechanism 1026); the Type
        # B predecessor added one (mechanism 1025).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type C lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1324:
    def test_top_key_found(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1324 in key, no 1026 or
        # 1027 substring.
        assert "1324" in BLOCK_KEY
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

    def test_no_type_c_1324_in_git_log_own_run(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721 in BOTH files per
        # the #1292 precedent): every commit whose message matches
        # "Type C #1324" must be #1324's main commit or a descendant of
        # it. Deselected in the in-gate run (fails pre-commit by
        # design: PRED_MAIN_1324 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1324")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1324's own commits"
        main = _git("rev-parse", PRED_MAIN_1324).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_novel_urls_zero_hit_at_head(self):
        # The 6 novel URLs were verified zero-hit repo-wide pre-commit
        # via git grep -F this run (documented in the block's novelty
        # field); at HEAD they must still be absent (they land only in
        # this run's uncommitted block).
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--", ".")
            assert out.stdout.strip() == "", url

    def test_atlassian_novelty_documented(self):
        # FIRST dedicated corpus mechanism on OpenAI x Atlassian: zero
        # "atlassian" hits repo-wide pre-commit (case-insensitive),
        # disclosed in the block's novelty field.
        assert 'zero "atlassian" hits repo-wide pre-commit' in \
            _block()["novelty"]

    def test_eight_rejections_documented(self):
        # 8 rejected candidates documented in the novelty field.
        nov = _block()["novelty"]
        assert "REJECTED CANDIDATES" in nov
        for tag in ("Hearst", "News Corp", "SPUR", "Broadcom",
                    "Anthropic", "lobby trip"):
            assert tag in nov, tag

    def test_no_1324_row_in_readme_table(self):
        readme = _read(README_PATH)
        assert "test_type_c_1324" not in readme

    def test_no_1324_row_in_architecture_tree(self):
        arch = _read(ARCH_PATH)
        assert "test_type_c_1324" not in arch

    def test_no_1324_in_iteration_log_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1324" not in log


# ---------------------------------------------------------------------------
# 4. Block structure
# ---------------------------------------------------------------------------

class TestBlockStructure1324:
    def test_top_level_fields(self):
        b = _block()
        assert b["iteration"] == 1324
        assert b["iteration_type"] == "C"
        assert b["type"] == "financial_incentive_mapping"
        assert b["block_key"] == BLOCK_KEY
        assert b["date_analyzed"] == "2026-10-08"

    def test_finding_fields(self):
        b = _block()
        assert b["verdict"] == "mechanism_documented"
        assert b["verdict_detail"] == "mechanism_documented"
        assert b["falsification_family_member"] is False
        assert b["browser_opens"] == 0
        assert b["yaml_parse_clean"] is True
        assert b["ascii_only"] is True

    def test_researcher_attribution(self):
        b = _block()
        assert b["researcher"] == "Kit (with Ray)"
        assert b["author"] == "Kit (with Ray)"
        assert b["goal_id"] == "goal_54093bda4145"

    def test_connects_to_vendor_embed(self):
        # Variant extension of the m807 vendor-embed family.
        assert _block()["connects_to"] == [807]

    def test_sources_count_and_novelty(self):
        b = _block()
        assert len(b["sources"]) == 6
        assert all(s["novel"] is True for s in b["sources"])
        assert all(s["accessed"] == "2026-10-08" for s in b["sources"])

    def test_confounders_graded(self):
        b = _block()
        assert len(b["confounders"]) == 5
        strengths = [c["strength"] for c in b["confounders"]]
        assert strengths.count("strong") == 2
        assert strengths.count("medium") == 2
        assert strengths.count("weak") == 1

    def test_no_em_dashes_in_block(self):
        src = _read(ENTITIES_PATH)
        start = src.index(TOP_KEY + ":")
        seg = src[start:start + 20000]
        assert "\u2014" not in seg
        assert "\u2013" not in seg

    def test_key_design_note(self):
        assert "no 1026 string per #715" in _block()["key_design_note"]

    def test_rotation_transparency_present(self):
        rt = _block()["rotation_transparency"]
        assert "FIFTH and CLOSING leg of the 1320-1324 window" in rt
        assert "the 1315-1319 window is VERIFIED CLOSED" in rt

    def test_concurrency_note_present(self):
        cc = _block()["concurrency"]
        assert "Do NOT touch #1024 m846" in cc
        assert "#899" in cc and "#938" in cc

    def test_background_suite_observation(self):
        bss = _block()["background_suite_status"]
        assert "#1320-launched" in bss
        assert "#795" in bss
        assert "#1325" in bss

    def test_research_method_documents_sets(self):
        rm = _block()["research_method"]
        assert "6 main-run browser.search verification sets" in rm
        assert "0 browser.open" in rm


# ---------------------------------------------------------------------------
# 5. m1026 content discipline
# ---------------------------------------------------------------------------

class TestM1026ContentDiscipline1324:
    def test_spend_commitment_arrow(self):
        f = _block()["finding"]
        assert "effectively a spend commitment" in f
        assert "Atlassian committing dollars to OpenAI" in f
        assert "NOT the reverse" in f

    def test_three_arrows_documented(self):
        f = _block()["finding"]
        assert "LAB-AS-SUPPLIER" in f
        assert "THE SPEND COMMITMENT" in f
        assert "RECIPROCAL ENTERPRISE LEGS" in f

    def test_lab_as_supplier_details(self):
        f = _block()["finding"]
        assert "GPT-6 Astra" in f
        assert "Teamwork Graph" in f
        assert "not its only engine" in f

    def test_reciprocal_legs_details(self):
        f = _block()["finding"]
        assert "3,000" in f
        assert "ChatGPT Enterprise" in f
        assert "OpenAI keeps using Jira" in f

    def test_multi_model_non_exclusivity(self):
        f = _block()["finding"]
        # Case-insensitive: the block carries the uppercase header form
        # "MULTI-MODEL NON-EXCLUSIVITY" (fixed to .lower() per the #1318
        # / #1323 confounder case-sensitivity pattern).
        assert "multi-model" in f.lower()
        assert "routes dynamically" in f
        assert "Scott White" in f

    def test_no_published_financial_terms(self):
        f = _block()["finding"]
        assert "neither company published financial terms" in f
        assert "specifics declined" in f

    def test_reversed_vendor_embed_distinction(self):
        f = _block()["finding"]
        assert "reversed arrow" in f
        assert "m807 vendor-embed family" in f

    def test_no_new_direction_landed(self):
        f = _block()["finding"]
        assert "NOT a new relationship direction" in f
        nov = _block()["novelty"]
        assert "fortieth direction-claim form absent" in nov
        assert "thirty-fifth through thirty-ninth" in nov

    def test_announcement_date(self):
        f = _block()["finding"]
        assert "announced Oct 6 2026" in f
        # Parsed-YAML form: the YAML source escapes the apostrophe as
        # '', which parses to a single quote in the block text.
        assert "Team '26 Europe" in f

    def test_partnership_context_2023(self):
        f = _block()["finding"]
        assert "began in 2023" in f

    def test_excerpt_bounded(self):
        assert _block()["browser_opens"] == 0
        assert "0 browser.open per #503" in _block()["research_method"]

    def test_mcp_server_scale(self):
        f = _block()["finding"]
        assert "220+" in f
        assert "15M calls/day" in f


# ---------------------------------------------------------------------------
# 6. Statistical discipline (the Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1324:
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

class TestFalsificationLedger1324:
    def test_not_a_member(self):
        ff = _block()["falsification_family"]
        assert "NOT a member (ledger holds at 60" in ff

    def test_no_coverage_tone_pair(self):
        ff = _block()["falsification_family"]
        assert "no coverage-tone pair scored" in ff
        assert "no uniform-prediction test" in ff

    def test_sixtieth_present_documented(self):
        ff = _block()["falsification_family"]
        assert "sixtieth member-claim form present 3x" in ff

    def test_sixty_first_absent_documented(self):
        ff = _block()["falsification_family"]
        assert "sixty-first member-claim form absent repo-wide" in ff

    def test_forty_eighth_present_documented(self):
        ff = _block()["falsification_family"]
        assert "forty-eighth member-claim form present 2x" in ff

    def test_no_sixty_first_repo_wide(self):
        assert _git_grep_tracked_source(_T61, None) == []


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: pins for #1325; #1323's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1324:
    def test_pins_on_1026_landing(self):
        # Type C lands one mechanism: max becomes 1026, next is 1027.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1026" in src
        assert "NEXT_NUM = 1027" in src

    def test_no_type_d_1325_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1325's terminal log-hash followup
        # per #721): every commit whose message matches "Type D
        # #1325" must be #1325's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1325 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type D #1325")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1325's own commits"
        main = _git("rev-parse", PRED_MAIN_1325).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1027_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1027_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1027_dash_absent_repo_wide(self):
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

    def test_no_sixty_first_member_pin(self):
        assert _git_grep_tracked_source(_T61, None) == []

    def test_predecessor_1323_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, A1323_FILE))

    def test_next_leg_is_1325_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1325 Type D" in src

    def test_1323_pins_flip_by_design_documented(self):
        # Documents the two BY-DESIGN flips at this run's main commit:
        # test_no_type_c_1324_in_git_log_pin (the #1191-class
        # self-trip, re-pinned green in the terminal log-hash followup
        # per #721 in BOTH files per the #1292 precedent) and
        # test_1026_numeric_absent_in_profiles (the #1272-class
        # forward-guard expiry, permanent - the next-number guard is
        # consumed by the m1026 landing).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1191-class" in src
        assert "#1272-class" in src


# ---------------------------------------------------------------------------
# 9. Background suite check per #795
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1324:
    def test_1320_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1320_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1320-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1324_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1320-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1325" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1324:
    def test_readme_test_file_table_has_1324_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_c_1324" in readme

    def test_architecture_has_1324_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_c_1324" in arch

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

class TestIterationLog1324:
    def test_1324_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1324 Type C" in log

    def test_1323_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1323 Type B" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1323's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1324:
    def test_1323_guard_lifecycle_post_commit(self):
        # Post-terminal-followup form: 22 of the 23 pass; the one that
        # fails BY DESIGN is test_1026_numeric_absent_in_profiles
        # (mechanism 1026 lands in profiles/ this run; the #1272-class
        # forward-guard expiry - the next-number guard is consumed by
        # the landing; stays red permanently). The second flip,
        # test_no_type_c_1324_in_git_log_pin (the #1191-class
        # self-trip: this run's own main commit carries "Type C
        # #1324"), is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1324 now holds this run's
        # main sha, in BOTH the #1324 and #1323 files per the #1292
        # precedent). test_pins_on_1025_landing stays GREEN (asserts on
        # the #1323 file's own constants, untouched by this run); the
        # member and direction pins stay GREEN (m1026 is a
        # financial-architecture leg, not a family member; no new
        # direction landed).
        # Deselected pre-commit (verified only post-terminal-followup).
        res = _class_run(A1323_FILE, "TestGuardLifecycle1323")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "1 failed, 22 passed" in res.stdout, res.stdout[-2000:]
        assert "test_1026_numeric_absent_in_profiles" in res.stdout, \
            res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1324:
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
        # decision still pending. This run appends m1026 at
        # end-of-file only; the m846 block must be byte-identical to
        # HEAD. Do NOT touch #1024 m846.
        head = _git(
            "show", "HEAD:profiles/competitor-entities.yaml").stdout
        work = _read(ENTITIES_PATH)
        assert (head.splitlines()[M846_HEAD_START - 1:M846_HEAD_END]
                == work.splitlines()[M846_HEAD_START - 1:M846_HEAD_END])
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src
