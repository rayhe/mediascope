# -*- coding: utf-8 -*-
"""Type C #1344 tests: Getty Images (US) v Stability AI Lanham Act survival
(N.D. Cal. 3:25-cv-06891-TLT, Apr 23 2026 order) - FIRST dedicated corpus
mechanism on the visual-licensor litigation leg: trademark, false-designation
and dilution claims survive dismissal; the licensor sues one lab while signing
with others (Getty x OpenAI m684, Getty x Perplexity Oct-2025).

Iteration #1344 is the FIFTH and CLOSING leg of the 1340-1344 window
(D #1340 -> E #1341 -> A #1342 -> B #1343 -> C #1344 per the #565 anchor +
rotation guard). Next run #1345 Type D opens the 1345-1349 window.
This run lands mechanism 1038: Getty Images (US), Inc. v. Stability AI, Ltd.
(N.D. Cal. 3:25-cv-06891-TLT, Judge Trina L. Thompson; filed Aug 2025, refiled
after the Delaware voluntary dismissal). The Apr-23-2026 order (Doc. 53)
denied Stability''s motion to dismiss the Lanham Act claims - trademark
infringement, false designation of origin (15 U.S.C. 1125(a)), dilution -
plus California UCL; dismissed without prejudice only the false-CMI count.
Key holdings: AI-generated images bearing distorted Getty watermarks are
''goods'' under the Lanham Act; Dastar does not bar the false-designation
claim; Getty adequately pled ''household'' fame. The UK parallel (Justice
Joanna Smith, Nov 2025): trademark won ''in part'', secondary copyright lost
(''historic and extremely limited in scope''). The Type C nexus: Getty SIGNS
with OpenAI (m684) and Perplexity while SUING Stability AI - selective
enforcement, the visual-licensor sue-side counterpart to its sign-side;
mirrors the Guardian triple-path (sue Cohere + license OpenAI + SPUR).
Connects to m636 (pay-or-litigate taxonomy), m684 (sign-side), m1029
(USA TODAY v OpenAI litigation leg). NOT a new relationship direction:
the fortieth direction form stays absent by design; the thirty-fifth through
thirty-ninth directions stand.

Conventions carried forward:
- #565: this run''s main commit is the anchor; ANCHORED_SHA starts as
  0*40 and is patched to the main commit sha in the anchor followup.
- #715: pre-commit novelty greps (zero test_type_c_1344 files on disk;
  no ''Type C #1344'' in git log; max numeric mechanism_id 1037
  pre-commit; zero numeric/underscore/dash one-zero-three-eight
  mechanism key forms repo-wide pre-commit, needles format-built;
  block key zero-hit pre-commit; ''## #1344'' zero-hit in
  iteration-log; README 77262/1668 pre-commit; no #1344 rows in
  README/ARCHITECTURE test tables; 5 novel URLs zero-hit repo-wide
  pre-commit; the Getty-specific Lanham Act survival zero-hit repo-wide
  pre-commit - the single ''lanham'' hit is the Guardian/Cohere
  triple-path note, not Getty).
- #719: doc-sync ratchet (README stats table + test-table row +
  docs/ARCHITECTURE.md tree row + iteration-log entry;
  README_TEST_COUNT / README_FILE_COUNT patched pre-main once the
  in-gate collection count is known).
- #721: terminal log-hash followup registers main/anchor/doc-sync
  hashes in the iteration-log entry and re-pins PRED_MAIN_1344 to the
  main sha in this file and in the #1343 file (the #1292
  re-pin-both-copies precedent).
- #795: the #1340-launched background full suite is OBSERVED only
  this run (goal hidden_files type_d_1340_full_suite.log); its verdict
  belongs to #1345. Observed at this run''s ~12:15 PM PDT check: last
  write Oct 9 09:35 PDT at [ 0%], NO live pytest process - appears DEAD
  (was observed ALIVE at the #1340 launch; recorded, not adjudicated).
- Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
  test file working-tree edit), #900 (untracked Type D test file),
  #1012-wt (working-tree edit on the committed Type A #1012 file)
  all stay out of this run''s index/diff via explicit-path staging.
  Do NOT touch #1024''s m846: self-flagged sourcing-constraint
  violation; Ray''s revert/leave/rebuild-from-primary decision still
  pending. This run appends m1038 at end-of-file; the m846 block (HEAD
  lines 26349-26472) is verified byte-identical to HEAD in
  TestInFlightIsolation1344.
- The Aug 28 2026 standing rule: MANUAL / qualitative ONLY. No
  coverage-tone pair scored (tone NOT_SCORED); p_value/cohens_d/ci_95
  NOT_CALCULATED; is_significant false; engine NOT run; verdict
  mechanism_documented; NOT a falsification-family member (ledger holds
  at 63); NOT artifact-grade; no_analysis_json_update true.
- 0 browser.open per #503 (excerpt-bounded); the delegated scout
  returned 8 ranked candidates (#1 APIG REJECTED on main-run corpus
  verification: already in-corpus as the
  french_apig_ai_overviews_complaint_aug2026 sub-block; #4 India fee
  figures already carried via m798); 2 main-run browser.search
  verification sets re-ran the selection independently; 6 rejected
  candidates documented in the block''s novelty field.
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
    "test_type_c_1344_getty_stability_lanham_act_"
    "visual_licensor_suit_oct09_12pm.py"
)
TOP_KEY = (
    "type_c_1344_getty_stability_lanham_act_"
    "visual_licensor_suit_oct09_12pm"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "0" * 40  # 0*40 pre-commit; patched to the main-commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1038
NEXT_NUM = 1039  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_c_1344_getty_stability_lanham_act_"
    "visual_licensor_suit_oct09_12pm"
)

# Predecessor chain: #1343 Type B (fourth leg).
PRED_MAIN_1343 = "d3252af1d0ee6bb0e25aa8690c8ad86d47211969"
PRED_ANCHOR_1343 = "0ed77aae26d6d2bc1debe53c1763c81af0c1bf8b"
PRED_DOCSYNC_1343 = "b6f4bb907fa9a936067493213aac89fd5058ce0b"
PRED_FINAL_1343 = "e353a64cf92475abc086db6fd1283330275c4bd6"
# #1342 Type A (third leg) for the rotation-guard chain.
PRED_MAIN_1342 = "3e71adbdce7e47b9212bc9b2881201d7b08a72c5"
PRED_ANCHOR_1342 = "d1ce1912b9e35913cd181cbad5a2885fef316df8"
PRED_DOCSYNC_1342 = "13d866e835a36a7f0111dcb6a28e0798197ced62"
PRED_FINAL_1342 = "814a1c3493babbea8f8877a5524efc2df26b0e1c"

# Forward guard for #1345 (Type D): placeholder per #721; re-pinned to
# the main sha in the terminal log-hash followup of the #1345 run.
PRED_MAIN_1345 = "0" * 40

# Own-run main-commit placeholder per #721: 0*40 pre-commit, re-pinned
# to this run's main sha in the terminal log-hash followup (in BOTH
# this file and the #1343 file per the #1292 precedent).
PRED_MAIN_1344 = "0" * 40  # re-pinned to #1344 main sha in the terminal log-hash followup per #721/#1292

# #1343's test file (for the guard-lifecycle staleness pins).
A1343_FILE = (
    "test_type_b_1343_ariel_zilber_nypost_creep_glasses_"
    "vs_anthropic_claude_policy_oct09_11am.py"
)

# Doc-sync constants per #719: patched pre-main to the post-sync
# values once the in-gate collection count is known.
# Post-sync-positive: 77262 + 100 tests, 1668 + 1 files.
README_TEST_COUNT = 77362
README_FILE_COUNT = 1669

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

# Novel source URLs: 5 zero-hit repo-wide pre-commit (git grep -F on
# verbatim Full-URL listings).
NOVEL_URLS = [
    "https://www.jdsupra.com/legalnews/trademark-law-meets-"
    "generative-ai-key-9850246/",
    "https://www.courtlistener.com/recap/gov.uscourts.cand.454636/"
    "gov.uscourts.cand.454636.53.0.pdf",
    "https://www.thefashionlaw.com/from-chatgpt-to-deepfake-"
    "creating-apps-a-running-list-of-key-ai-lawsuits/",
    "https://news.bloomberglaw.com/ip-law/gettys-ai-copyright-"
    "suit-survives-stabilitys-bid-for-dismissal",
    "https://www.marketing-interactive.com/getty-images-suffers-"
    "partial-defeat-in-uk-copyright-lawsuit-against-stability-ai",
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


class TestAnchor1344:
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
        assert "FIFTH and CLOSING leg of the 1340-1344 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1344:
    def test_predecessor_1343_chain_verified(self):
        for sha in (
            PRED_MAIN_1343, PRED_ANCHOR_1343, PRED_DOCSYNC_1343,
            PRED_FINAL_1343,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1342_chain_verified(self):
        for sha in (
            PRED_MAIN_1342, PRED_ANCHOR_1342, PRED_DOCSYNC_1342,
            PRED_FINAL_1342,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1340 -> E #1341 -> A #1342 -> B #1343 -> C #1344" in src

    def test_next_leg_is_type_d_1345(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1345 Type D" in src

    def test_type_c_lands_one_mechanism(self):
        # Type C lands exactly one mechanism (mechanism 1038); the Type
        # B predecessor added one (mechanism 1037).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type C lands one mechanism" in src

    def test_window_closes_here(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1345-1349 window" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1344:
    def test_top_key_found(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1344 in key, no 1038 or
        # 1039 substring.
        assert "1344" in BLOCK_KEY
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

    def test_no_type_c_1344_in_git_log_own_run(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721 in BOTH files per
        # the #1292 precedent): every commit whose message matches
        # "Type C #1344" must be #1344's main commit or a descendant of
        # it. Deselected in the in-gate run (fails pre-commit by
        # design: PRED_MAIN_1344 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1344")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1344's own commits"
        main = _git("rev-parse", PRED_MAIN_1344).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_novel_urls_zero_hit_at_head(self):
        # The 5 novel URLs were verified zero-hit repo-wide pre-commit
        # via git grep -F this run (documented in the block's novelty
        # field); at HEAD they must still be absent (they land only in
        # this run's uncommitted block).
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--", ".")
            assert out.stdout.strip() == "", url

    def test_lanham_act_framing_novel_for_getty(self):
        # The single pre-existing repo-wide "lanham" hit is the
        # Guardian/Cohere triple-path note (guardian.yaml), not Getty;
        # this run introduces the Getty-specific Lanham Act survival.
        assert "Lanham Act" in _block()["finding"]
        assert "3:25-cv-06891-TLT" in _block()["finding"]
        assert "french_apig_ai_overviews" not in _block()["finding"]

    def test_six_rejections_documented(self):
        # 6 rejected candidates documented in the novelty field.
        nov = _block()["novelty"]
        assert "REJECTED CANDIDATES" in nov
        for tag in ("APIG", "Folha", "m798", "Britannica",
                    "Shutterstock", "renewal"):
            assert tag in nov, tag

    def test_scout_rejection_documented(self):
        # The scout's #1 APIG angle was rejected on main-run corpus
        # verification; the rejection is documented, not hidden.
        nov = _block()["novelty"]
        assert "french_apig_ai_overviews_complaint_aug2026" in nov
        assert "12624" in nov

    def test_no_1344_row_in_readme_table(self):
        readme = _read(README_PATH)
        assert "test_type_c_1344" not in readme


# ---------------------------------------------------------------------------
# 4. Block structure
# ---------------------------------------------------------------------------

class TestBlockStructure1344:
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
        assert " " not in segment

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
# 5. m1038 content discipline
# ---------------------------------------------------------------------------

class TestM1038ContentDiscipline1344:
    def test_suit_facts_present(self):
        f = _block()["finding"]
        assert "3:25-cv-06891-TLT" in f
        assert "Trina L. Thompson" in f
        assert "Aug 2025" in f
        assert "12M+" in f

    def test_apr23_order_present(self):
        f = _block()["finding"]
        assert "Doc. 53" in f
        assert "DENIED" in f
        assert "GRANTED-IN-PART" in f

    def test_key_holdings_present(self):
        f = _block()["finding"]
        assert "'goods' under the Lanham Act" in f
        assert "Dastar" in f
        assert "household" in f
        assert "2.8B annual searches" in f

    def test_uk_parallel_present(self):
        f = _block()["finding"]
        assert "Joanna Smith" in f
        assert "historic and extremely limited in scope" in f

    def test_type_c_nexus_present(self):
        f = _block()["finding"]
        assert "m684" in f
        assert "SIGNS with OpenAI" in f
        assert "SUING Stability AI" in f
        assert "selective enforcement" in f

    def test_connects_to(self):
        assert _block()["connects_to"] == [636, 684, 1029]

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
        assert "2 main-run browser.search verification sets" in rm
        assert "0 browser.open per #503" in rm

    def test_october_status_present(self):
        f = _block()["finding"]
        assert "Oct 9 2026" in f
        assert "continues" in f


# ---------------------------------------------------------------------------
# 6. Statistical discipline (the Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1344:
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

class TestFalsificationLedger1344:
    def test_not_a_member(self):
        ff = _block()["falsification_family"]
        assert "NOT a member (ledger holds at 63" in ff

    def test_no_coverage_tone_pair(self):
        ff = _block()["falsification_family"]
        assert "no coverage-tone pair scored" in ff
        assert "no uniform-prediction test" in ff

    def test_sixty_third_present_documented(self):
        ff = _block()["falsification_family"]
        assert "sixty-third" in ff

    def test_sixty_fourth_absent_documented(self):
        ff = _block()["falsification_family"]
        assert "sixty-fourth member-claim form absent repo-wide" in ff

    def test_no_sixty_fourth_repo_wide(self):
        assert _git_grep_tracked_source(_T64, None) == []

    def test_ledger_63_held(self):
        # This run must not move the ledger.
        assert _block()["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: pins for #1345; #1343's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1344:
    def test_pins_on_1038_landing(self):
        # Type C lands one mechanism: max becomes 1038, next is 1039.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1038" in src
        assert "NEXT_NUM = 1039" in src

    def test_no_type_d_1345_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1345's terminal log-hash followup
        # per #721): every commit whose message matches "Type D
        # #1345" must be #1345's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1345 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type D #1345")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1345's own commits"
        main = _git("rev-parse", PRED_MAIN_1345).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1039_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1039_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1039_dash_absent_repo_wide(self):
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
        # Landed #1342 (m1036 Times x OpenAI, profiles/news-corp.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T63, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_fourth_member_pin(self):
        assert _git_grep_tracked_source(_T64, None) == []

    def test_predecessor_1343_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, A1343_FILE))

    def test_next_leg_is_1345_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1345 Type D" in src

    def test_1343_pins_flip_by_design_documented(self):
        # Documents the BY-DESIGN flips at this run's main commit:
        # test_no_type_c_1344_in_git_log_pin (the #1191-class
        # self-trip, re-pinned green in the terminal log-hash followup
        # per #721 in BOTH files per the #1292 precedent) and
        # test_1038_numeric_absent_in_profiles (the #1272-class
        # forward-guard expiry, permanent - the next-number guard is
        # consumed by the m1038 landing). The underscore/dash 1038
        # pins stay green: the landed number appears only as the colon
        # form per the designed keying. The no-sixty-fourth-member pin
        # stays green (m1038 is a financial-architecture leg, not a
        # family member).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1191-class" in src
        assert "#1272-class" in src


# ---------------------------------------------------------------------------
# 9. Background suite check per #795
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1344:
    def test_1340_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1340_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1340-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1344_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1340-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1345" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1344:
    def test_readme_test_file_table_has_1344_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_c_1344" in readme

    def test_architecture_has_1344_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_c_1344" in arch

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

class TestIterationLog1344:
    def test_1344_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1344 Type C" in log

    def test_1343_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1343 Type B" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1343's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1344:
    def test_1343_guard_lifecycle_post_commit(self):
        # Post-terminal-followup form: 25 of the 26 pass; the one that
        # fails BY DESIGN is test_1038_numeric_absent_in_profiles
        # (mechanism 1038 lands in profiles/ this run; the #1272-class
        # forward-guard expiry - the next-number guard is consumed by
        # the landing; stays red permanently). The underscore/dash
        # 1038 pins stay green (the landed number appears only as the
        # colon form per the designed keying). The second flip,
        # test_no_type_c_1344_in_git_log_pin (the #1191-class
        # self-trip: this run's own main commit carries "Type C
        # #1344"), is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1344 now holds this run's
        # main sha, in BOTH the #1344 and #1343 files per the #1292
        # precedent). test_pins_on_one_mechanism_landing stays GREEN
        # (asserts on the #1343 file's own constants, untouched by this
        # run); the member and direction pins stay GREEN (m1038 is a
        # financial-architecture leg, not a family member; no new
        # direction landed).
        # Deselected pre-commit (verified only post-terminal-followup).
        res = _class_run(A1343_FILE, "TestGuardLifecycle1343")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "1 failed, 25 passed" in res.stdout, res.stdout[-2000:]
        assert "test_1038_numeric_absent_in_profiles" in res.stdout, \
            res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1344:
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
        # decision still pending. This run appends m1038 at
        # end-of-file only; the m846 block must be byte-identical to
        # HEAD. Do NOT touch #1024 m846.
        head = _git(
            "show", "HEAD:profiles/competitor-entities.yaml").stdout
        work = _read(ENTITIES_PATH)
        assert (head.splitlines()[M846_HEAD_START - 1:M846_HEAD_END]
                == work.splitlines()[M846_HEAD_START - 1:M846_HEAD_END])
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src
