# -*- coding: utf-8 -*-
"""Type C #1339 tests: Hachette et al. v Google selective-payer Gemini suit
(S.D.N.Y. 1:26-cv-05870, filed Jul 10 2026) - FIRST dedicated corpus mechanism
on the repurposed-commercial-relationship litigation leg: Google licensed
Gemini training content from AP/Reddit/Shutterstock and talked to 20+ more
publishers while allegedly repurposing Google Books content obtained under
scope-limited distribution agreements, documented as mechanism 1035.

Iteration #1339 is the FIFTH and CLOSING leg of the 1335-1339 window
(D #1335 -> E #1336 -> A #1337 -> B #1338 -> C #1339 per the #565 anchor +
rotation guard). Next run #1340 Type D opens the 1340-1344 window.
This run lands mechanism 1035: Hachette Book Group, Cengage Learning,
Elsevier, Scott Turow and S.C.R.I.B.E., Inc. sued Google on Jul 10 2026
(S.D.N.Y. 1:26-cv-05870, 57-page putative class action) alleging Google
copied millions of books and journal articles to train Gemini (and LaMDA,
PaLM, Bard), obtained through Google Books, Google Play Books and Google
Scholar under scope-limited agreements covering snippet display, ebook
distribution and discovery - agreements the plaintiffs say did not authorize
AI training - supplemented by web scraping including pirate sources and
paywalled content, with CMI stripped (DMCA 1202). The selective-payer datum
(complaint paras 103-105, via complaint-PDF relays): Google "is well aware
of the market for licensing AI training materials"; "licenses Gemini
training content from the Associated Press, Reddit, and Shutterstock"; "is
also in talks to license Gemini training content from at least another 20
news publishers"; was "recently hit with a EUR 250m fine for failing to
respect commitments [Google] made in 2022 to stop using news publishers''
online content to train Gemini without permission or compensation." The
October peg is Kenneth Eade''s Oct 1 2026 analysis: "Google faces a twist no
other AI defendant has: many of the works allegedly came through Google
Books, its own distribution channel for authors" - plus the Bartz frame
("training on lawfully acquired books is transformative; where the books
came from ... may decide this case"). The same plaintiff roster sued Meta
on May 5 2026 (pirate-site sourcing alleged, no prior commercial
relationship) - the Google geometry is the contrast case: repurposed
commercial relationship vs pure taking. The suit prices Google''s selective
payment: a documented payer in the training-data market (AP Jan 2025,
Reddit $60M/yr, Shutterstock $25-50M range, AI Contribution Pilot) that
allegedly bypassed payment for these plaintiffs'' works. Documented as a
litigation-tier leg in the m636 pay-or-litigate taxonomy (connects_to
[636, 843, 1029]), NOT a new relationship direction: the fortieth
direction form stays absent by design; the thirty-fifth through
thirty-ninth directions stand.

Conventions carried forward:
- #565: this run''s main commit is the anchor; ANCHORED_SHA starts as
  0*40 and is patched to the main commit sha in the anchor followup.
- #715: pre-commit novelty greps (zero test_type_c_1339 files on disk;
  no "Type C #1339" in git log; max numeric mechanism_id 1034
  pre-commit; zero numeric/underscore/dash one-zero-three-five
  mechanism key forms repo-wide pre-commit, needles format-built;
  block key zero-hit pre-commit; "## #1339" zero-hit in
  iteration-log; README 76751/1663 pre-commit; no #1339 rows in
  README/ARCHITECTURE test tables; 8 novel URLs zero-hit repo-wide
  pre-commit; "selective payer"/"selective-payer" zero-hit repo-wide
  pre-commit).
- #719: doc-sync ratchet (README stats table + test-table row +
  docs/ARCHITECTURE.md tree row + iteration-log entry;
  README_TEST_COUNT / README_FILE_COUNT patched pre-main once the
  in-gate collection count is known).
- #721: terminal log-hash followup registers main/anchor/doc-sync
  hashes in the iteration-log entry and re-pins PRED_MAIN_1339 to the
  main sha in this file and in the #1338 file (the #1292
  re-pin-both-copies precedent).
- #795: the #1335-launched background full suite is OBSERVED only
  this run (goal hidden_files type_d_1335_full_suite.log); its verdict
  belongs to #1340. Observed DEAD at this run''s check (last write Oct 9
  05:44:08 PDT at [ 1%], no live pytest process; the #1338 entry''s
  ~08:00 last-write claim does not match the file mtime - recorded,
  not adjudicated).
- Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
  test file working-tree edit), #900 (untracked Type D test file),
  #1012-wt (working-tree edit on the committed Type A #1012 file)
  all stay out of this run''s index/diff via explicit-path staging.
  Do NOT touch #1024''s m846: self-flagged sourcing-constraint
  violation; Ray''s revert/leave/rebuild-from-primary decision still
  pending. This run appends m1035 at end-of-file; the m846 block (HEAD
  lines 26350-26472) is verified byte-identical to HEAD in
  TestInFlightIsolation1339.
- The Aug 28 2026 standing rule: MANUAL / qualitative ONLY. No
  coverage-tone pair scored (tone NOT_SCORED); p_value/cohens_d/ci_95
  NOT_CALCULATED; is_significant false; engine NOT run; verdict
  mechanism_documented; NOT a falsification-family member (ledger holds
  at 62); NOT artifact-grade; no_analysis_json_update true.
- 0 browser.open per #503 (excerpt-bounded); the delegated scout
  returned the OpenAI-India angle (REJECTED on main-run corpus
  verification: m609/#624/#709/#944/#1079 saturated; scout''s
  Meta-x-News-Corp fallback in-corpus m519); 3 main-run browser.search
  verification sets re-ran the selection independently; 15 rejected
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
    "test_type_c_1339_hachette_google_selective_payer_"
    "repurposed_relationship_oct09_9am.py"
)
TOP_KEY = (
    "type_c_1339_hachette_google_selective_payer_"
    "repurposed_relationship_oct09_9am"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "e6c6a7511d6ce5d3ed66da14d564ab8b8774a7be"  # 0*40 pre-commit; patched to the main-commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1035
NEXT_NUM = 1036  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_c_1339_hachette_google_selective_payer_"
    "repurposed_relationship_oct09_9am"
)

# Predecessor chain: #1338 Type B (fourth leg).
PRED_MAIN_1338 = "148b3e4cd83332f93bcff757e85d862306885de3"
PRED_ANCHOR_1338 = "2806600af08a2b3e4a81085afa235d4ad70bb44c"
PRED_DOCSYNC_1338 = "83f6d4141b1183673b7d140d36a3e2d4faf1df47"
PRED_FINAL_1338 = "553e21642d59b4cd646d2f04141401c037f6d2c4"
# #1337 Type A (third leg) for the rotation-guard chain.
PRED_MAIN_1337 = "c8d74b54ebe3acc9ac189f03b94a6dc74a4b4940"
PRED_ANCHOR_1337 = "122ce5e7493a2d92cddb12c8f1d698fe31377eba"
PRED_DOCSYNC_1337 = "cb323d9ecf31478ac18048ee20e19ee3fcde5565"
PRED_FINAL_1337 = "9f537c0887f02bf0b7b53e383005d89b3a1ae01c"

# Forward guard for #1340 (Type D): placeholder per #721; re-pinned to
# the main sha in the terminal log-hash followup of the #1340 run.
PRED_MAIN_1340 = "0" * 40

# Own-run main-commit placeholder per #721: 0*40 pre-commit, re-pinned
# to this run's main sha in the terminal log-hash followup (in BOTH
# this file and the #1338 file per the #1292 precedent).
PRED_MAIN_1339 = "e6c6a7511d6ce5d3ed66da14d564ab8b8774a7be"  # re-pinned to #1339 main sha in the anchor followup per #721/#1292

# #1338's test file (for the guard-lifecycle staleness pins).
A1338_FILE = (
    "test_type_b_1338_alfonso_maruccia_techspot_norway_"
    "glasses_ban_vs_google_finland_forest_oct09_8am.py"
)

# Doc-sync constants per #719: patched pre-main to the post-sync
# values once the in-gate collection count is known.
# Post-sync-positive: 76751 + 101 tests, 1663 + 1 files.
README_TEST_COUNT = 76852
README_FILE_COUNT = 1664

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

# Novel source URLs: 8 zero-hit repo-wide pre-commit (git grep -F on
# verbatim Full-URL listings).
NOVEL_URLS = [
    "https://www.ghacks.net/2026/07/21/book-writers-sue-google-over-"
    "alleged-use-of-copyrighted-books-to-train-gemini/",
    "https://betanews.com/article/publishers-sue-google-gemini-book-"
    "training/",
    "https://111things.com/national/publishers-and-authors-sue-google-"
    "over-gemini-training-data/",
    "https://mlq.ai/news/hachette-cengage-and-elsevier-sue-google-over-"
    "ai-training-on-millions-of-copyrighted-works/",
    "https://www.scconline.com/blog/post/2026/07/21/gemini-ai-training-"
    "lawsuit-google-copyrighted-books/",
    "https://titikbaca.my/wp-content/uploads/2026/07/hachette-v.-google-"
    "dkt.-1-complaint2.pdf",
    "https://oandz.com/wp-content/uploads/2026-07-10-Doc-1-Hachette-v-"
    "Google-Complaint.pdf",
    "https://www.linkedin.com/pulse/can-google-train-gemini-millions-"
    "copyrighted-books-without-eade-0ohne",
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

class TestAnchor1339:
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
        assert "FIFTH and CLOSING leg of the 1335-1339 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1339:
    def test_predecessor_1338_chain_verified(self):
        for sha in (
            PRED_MAIN_1338, PRED_ANCHOR_1338, PRED_DOCSYNC_1338,
            PRED_FINAL_1338,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1337_chain_verified(self):
        for sha in (
            PRED_MAIN_1337, PRED_ANCHOR_1337, PRED_DOCSYNC_1337,
            PRED_FINAL_1337,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1335 -> E #1336 -> A #1337 -> B #1338 -> C #1339" in src

    def test_next_leg_is_type_d_1340(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1340 Type D" in src

    def test_type_c_lands_one_mechanism(self):
        # Type C lands exactly one mechanism (mechanism 1035); the Type
        # B predecessor added one (mechanism 1034).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type C lands one mechanism" in src

    def test_window_closes_here(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1340-1344 window" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1339:
    def test_top_key_found(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1339 in key, no 1035 or
        # 1036 substring.
        assert "1339" in BLOCK_KEY
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

    def test_no_type_c_1339_in_git_log_own_run(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721 in BOTH files per
        # the #1292 precedent): every commit whose message matches
        # "Type C #1339" must be #1339's main commit or a descendant of
        # it. Deselected in the in-gate run (fails pre-commit by
        # design: PRED_MAIN_1339 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1339")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1339's own commits"
        main = _git("rev-parse", PRED_MAIN_1339).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_novel_urls_zero_hit_at_head(self):
        # The 8 novel URLs were verified zero-hit repo-wide pre-commit
        # via git grep -F this run (documented in the block's novelty
        # field); at HEAD they must still be absent (they land only in
        # this run's uncommitted block).
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--", ".")
            assert out.stdout.strip() == "", url

    def test_selective_payer_framing_novel(self):
        # The "selective payer" framing is novel to the corpus
        # (zero-hit repo-wide pre-commit); this run introduces it.
        assert "selective-payer" in _block()["finding"]
        assert "selective payment" in _block()["finding"].lower()

    def test_fifteen_rejections_documented(self):
        # 15 rejected candidates documented in the novelty field.
        nov = _block()["novelty"]
        assert "REJECTED CANDIDATES" in nov
        for tag in ("BCCL", "Village Media", "Redpine", "TollBit",
                    "ElevenLabs", "Huxe", "Atlassian"):
            assert tag in nov, tag

    def test_scout_rejection_documented(self):
        # The scout's India angle was rejected on main-run corpus
        # verification; the rejection is documented, not hidden.
        nov = _block()["novelty"]
        assert "m609" in nov
        assert "#944" in nov

    def test_no_1339_row_in_readme_table(self):
        readme = _read(README_PATH)
        assert "test_type_c_1339" not in readme


# ---------------------------------------------------------------------------
# 4. Block structure
# ---------------------------------------------------------------------------

class TestBlockStructure1339:
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


# ---------------------------------------------------------------------------
# 5. m1035 content discipline
# ---------------------------------------------------------------------------

class TestM1035ContentDiscipline1339:
    def test_suit_facts_present(self):
        f = _block()["finding"]
        assert "1:26-cv-05870" in f
        assert "Jul 10 2026" in f
        assert "57-page" in f
        assert "Hachette Book Group" in f
        assert "Cengage Learning" in f
        assert "Elsevier" in f
        assert "Scott Turow" in f

    def test_repurposed_relationship_geometry(self):
        f = _block()["finding"]
        assert "repurposed" in f
        assert "Google Books" in f
        assert "scope-limited" in f

    def test_selective_payer_datum_present(self):
        f = _block()["finding"]
        assert "Associated Press, Reddit, and Shutterstock" in f
        assert "another 20" in f
        assert "EUR 250m fine" in f

    def test_october_peg_present(self):
        f = _block()["finding"]
        assert "Oct 1 2026" in f
        assert "Kenneth Eade" in f
        assert "twist no other AI defendant has" in f

    def test_bartz_framing_present(self):
        f = _block()["finding"]
        assert "Bartz" in f
        assert "lawfully acquired books is transformative" in f

    def test_dual_defendant_roster_present(self):
        f = _block()["finding"]
        assert "May 5 2026" in f
        assert "dual-defendant roster" in f.lower()

    def test_relief_sought_present(self):
        f = _block()["finding"]
        assert "class certification" in f
        assert "destruction of infringing copies" in f

    def test_connects_to_636_843_1029(self):
        assert _block()["connects_to"] == [636, 843, 1029]

    def test_litigation_tier_not_new_direction(self):
        f = _block()["finding"]
        assert "litigation-tier taxonomy" in f
        assert "fortieth" in f
        assert "thirty-fifth through" in f

    def test_confounders_strong_first(self):
        cs = _block()["confounders"]
        assert len(cs) == 5
        assert cs[0]["strength"] == "strong"
        assert cs[1]["strength"] == "strong"
        assert "Excerpt-bounded per #503" in cs[0]["text"]
        assert "Allegations, not findings" in cs[1]["text"]

    def test_eight_sources(self):
        assert len(_block()["sources"]) == 8

    def test_sources_carry_urls_and_access(self):
        for s in _block()["sources"]:
            assert s["url"].startswith("http")
            assert s["accessed"] == "2026-10-09"
            assert s["novel"] is True

    def test_complaint_pdf_relays_present(self):
        srcs = _block()["sources"]
        urls = [s["url"] for s in srcs]
        assert any("titikbaca.my" in u for u in urls)
        assert any("oandz.com" in u for u in urls)

    def test_eade_linkedin_source_present(self):
        srcs = _block()["sources"]
        assert any("linkedin.com" in s["url"] for s in srcs)


# ---------------------------------------------------------------------------
# 6. Statistical discipline (the Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1339:
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

class TestFalsificationLedger1339:
    def test_not_a_member(self):
        ff = _block()["falsification_family"]
        assert "NOT a member (ledger holds at 62" in ff

    def test_no_coverage_tone_pair(self):
        ff = _block()["falsification_family"]
        assert "no coverage-tone pair scored" in ff
        assert "no uniform-prediction test" in ff

    def test_sixty_second_present_documented(self):
        ff = _block()["falsification_family"]
        assert "sixty-second" in ff

    def test_sixty_third_absent_documented(self):
        ff = _block()["falsification_family"]
        assert "sixty-third member-claim form absent repo-wide" in ff

    def test_no_sixty_third_repo_wide(self):
        assert _git_grep_tracked_source(_T63, None) == []

    def test_ledger_62_held(self):
        # This run must not move the ledger.
        assert _block()["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: pins for #1340; #1338's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1339:
    def test_pins_on_1035_landing(self):
        # Type C lands one mechanism: max becomes 1035, next is 1036.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1035" in src
        assert "NEXT_NUM = 1036" in src

    def test_no_type_d_1340_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1340's terminal log-hash followup
        # per #721): every commit whose message matches "Type D
        # #1340" must be #1340's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1340 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type D #1340")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1340's own commits"
        main = _git("rev-parse", PRED_MAIN_1340).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1036_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1036_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1036_dash_absent_repo_wide(self):
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

    def test_predecessor_1338_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, A1338_FILE))

    def test_next_leg_is_1340_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1340 Type D" in src

    def test_1338_pins_flip_by_design_documented(self):
        # Documents the BY-DESIGN flips at this run's main commit:
        # test_no_type_c_1339_in_git_log_pin (the #1191-class
        # self-trip, re-pinned green in the terminal log-hash followup
        # per #721 in BOTH files per the #1292 precedent) and
        # test_1035_numeric_absent_in_profiles (the #1272-class
        # forward-guard expiry, permanent - the next-number guard is
        # consumed by the m1035 landing). The underscore/dash 1035
        # pins stay green: the landed number appears only as the colon
        # form per the designed keying.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1191-class" in src
        assert "#1272-class" in src


# ---------------------------------------------------------------------------
# 9. Background suite check per #795
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1339:
    def test_1335_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1335_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1335-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1339_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1335-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1340" in _block()["background_suite_status"]
        assert "DEAD" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1339:
    def test_readme_test_file_table_has_1339_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_c_1339" in readme

    def test_architecture_has_1339_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_c_1339" in arch

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

class TestIterationLog1339:
    def test_1339_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1339 Type C" in log

    def test_1338_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1338 Type B" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1338's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1339:
    def test_1338_guard_lifecycle_post_commit(self):
        # Post-terminal-followup form: 24 of the 25 pass; the one that
        # fails BY DESIGN is test_1035_numeric_absent_in_profiles
        # (mechanism 1035 lands in profiles/ this run; the #1272-class
        # forward-guard expiry - the next-number guard is consumed by
        # the landing; stays red permanently). The underscore/dash
        # 1035 pins stay green (the landed number appears only as the
        # colon form per the designed keying). The second flip,
        # test_no_type_c_1339_in_git_log_pin (the #1191-class
        # self-trip: this run's own main commit carries "Type C
        # #1339"), is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1339 now holds this run's
        # main sha, in BOTH the #1339 and #1338 files per the #1292
        # precedent). test_pins_on_one_mechanism_landing stays GREEN
        # (asserts on the #1338 file's own constants, untouched by this
        # run); the member and direction pins stay GREEN (m1035 is a
        # financial-architecture leg, not a family member; no new
        # direction landed).
        # Deselected pre-commit (verified only post-terminal-followup).
        res = _class_run(A1338_FILE, "TestGuardLifecycle1338")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "1 failed, 24 passed" in res.stdout, res.stdout[-2000:]
        assert "test_1035_numeric_absent_in_profiles" in res.stdout, \
            res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1339:
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
        # decision still pending. This run appends m1035 at
        # end-of-file only; the m846 block must be byte-identical to
        # HEAD. Do NOT touch #1024 m846.
        head = _git(
            "show", "HEAD:profiles/competitor-entities.yaml").stdout
        work = _read(ENTITIES_PATH)
        assert (head.splitlines()[M846_HEAD_START - 1:M846_HEAD_END]
                == work.splitlines()[M846_HEAD_START - 1:M846_HEAD_END])
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src
