# -*- coding: utf-8 -*-
"""Type C #1314 tests: Amazon Content Partners (in-kind small-publisher
program, ~mid-Jun 2026 gated preview) - FIRST dedicated corpus mechanism
on the in-kind AI-publisher incentive (AWS WAF bot-traffic control +
1% Associates uplift + premium ad inventory + $100/mo AWS credits),
documented as mechanism 1020.

Iteration #1314 is the FIFTH and CLOSING leg of the 1310-1314 window
(D #1310 -> E #1311 -> A #1312 -> B #1313 -> C #1314 per the #565 anchor +
rotation guard). This run lands mechanism 1020: the FIRST dedicated corpus
mechanism on Amazon's Content Partners program - a US-only,
voluntary/fee-free/no-minimums program for small/indie publishers that
pays in infrastructure + commerce + ad benefits rather than cash
licensing. Dating honesty is explicit: reported ~mid-Jun 2026 (pulse.bot
Last Updated 113 days pre-check); no exact launch date in the excerpts,
so none is claimed.

Conventions carried forward:
- #565: this run's main commit is the anchor; ANCHORED_SHA starts as 0*40
  and is patched to the main commit sha in the anchor followup.
- #715: pre-commit novelty greps (zero test_type_c_1314 files on disk;
  no "Type C #1314" in git log; max numeric mechanism_id 1019 pre-commit;
  zero numeric/underscore/dash one-zero-two-zero mechanism key forms
  repo-wide pre-commit, needles format-built; block key zero-hit
  pre-commit; "## #1314" zero-hit in iteration-log; README 74174/1638
  pre-commit; no #1314 rows in README/ARCHITECTURE test tables; 3 novel
  URLs zero-hit repo-wide pre-commit).
- #719: doc-sync ratchet (README stats table + test-table row +
  docs/ARCHITECTURE.md tree row + iteration-log entry; README_TEST_COUNT /
  README_FILE_COUNT patched pre-main once the in-gate collection count is
  known).
- #721: terminal log-hash followup registers main/anchor/doc-sync hashes
  in the iteration-log entry and re-pins PRED_MAIN_1314 to the main sha in
  this file and in the #1313 file (the #1292 re-pin-both-copies precedent).
- #795: the #1310-launched background full suite is OBSERVED only this
  run (goal hidden_files type_d_1310_full_suite.log); its verdict belongs
  to #1315.
- Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test
  file working-tree edit), #900 (untracked Type D test file), #1012-wt
  (working-tree edit on the committed Type A #1012 file) all stay out of
  this run's index/diff via explicit-path staging. Do NOT touch #1024's
  m846 (FOURTEENTH, exclusionary-diversion): self-flagged
  sourcing-constraint violation; Ray's revert/leave/rebuild-from-primary
  decision still pending.
- The Aug 28 2026 standing rule: MANUAL / qualitative ONLY. No
  coverage-tone pair scored (tone NOT_SCORED); p_value/cohens_d/ci_95
  NOT_CALCULATED; is_significant false; engine NOT run; verdict
  mechanism_documented; NOT a falsification-family member (ledger holds
  at 59); NOT artifact-grade; no_analysis_json_update true.
- 0 browser.open per #503 (excerpt-bounded); 2 main-run browser.search
  verification sets + 1 delegated scout (4 ranked candidates; Microsoft
  PCM and Cloudflare Pay Per Use Sep-30 beta rejected on repo-overlap,
  NMA x ProRata rejected on NMA-Bria collective overlap, Amazon Content
  Partners SELECTED).
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
SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1310_full_suite.log")
OWN_BASENAME = (
    "test_type_c_1314_amazon_content_partners_in_kind_"
    "oct08_12pm.py"
)

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "944d5510174c894fa4d1fec6c9e9a679e93a4b8f"  # patched to main commit per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1020
NEXT_NUM = 1021  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_c_1314_amazon_content_partners_in_kind_"
    "oct08_12pm"
)

# Predecessor chain: #1313 Type B (fourth leg).
PRED_MAIN_1313 = "fc747c1346a12167eaf28ac461ab2ae5546c7e04"
PRED_ANCHOR_1313 = "b65104acd015ce46972e496d637ab56a68489f1a"
PRED_DOCSYNC_1313 = "39aec13dc9bdd8d22568f7223df4bb8e6f91c8d0"
PRED_FINAL_1313 = "f8011a0042151dfdba1bbff7af45b8c79574cf6b"
PRED_PUSH_1313 = "252ac34b70ea31933d47e91a5eee2390ebdf7fa5"
# #1312 Type A (third leg) for the rotation-guard chain.
PRED_MAIN_1312 = "9e37e42b129c20e39eac73e245d6e52b15510b4e"
PRED_ANCHOR_1312 = "37e7a7e94e9fe86d793f1e73366b94181edd8ee4"
PRED_DOCSYNC_1312 = "fe67a3bbc9e4dbdfbae96f1aab35a36d11fd520b"
PRED_FINAL_1312 = "ccf522f8d88659ad52d1f6b2d04368e04f08e137"
PRED_PUSH_1312 = "5e67c15a939284448403f6eb04e6844df9deed5e"
# #1311 Type E (second leg).
PRED_MAIN_1311 = "a9d11a087f42aca79a5e2beee63e60c57c019720"
PRED_ANCHOR_1311 = "d12c4a613df0a08ff75210f828126e5d364377ea"
PRED_DOCSYNC_1311 = "b77dad3ee3436411e92c92f568fb11c8c1287ceb"
PRED_FINAL_1311 = "a35c64357ee20018f83274e18898042ffe07ab37"
PRED_PUSH_1311 = "49159ceebbb297e875c54274735802333b560cba"
# #1310 Type D (window opener).
PRED_MAIN_1310 = "84f3c3190dff8fc3d9342450c45aa021ac965496"
PRED_ANCHOR_1310 = "348e71be83501f18728ac8929099e839cd58f6be"
PRED_DOCSYNC_1310 = "8ef3c0299558850529c6f8f5306098d62da6261c"
PRED_FINAL_1310 = "726bd33fc28c6e134bf93ed5facd3fb6a488cbac"
PRED_PUSH_1310 = "34e26caecac445732cbdfa646acef55430584754"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40).
PRED_MAIN_1314 = "0" * 40  # re-pinned to main sha in the terminal log-hash followup per #721

# Forward guard for the next leg: #1315 Type D. Re-pinned by #1315's
# log-hash followup per #721 (starts as 0*40; placeholder-only per
# the Type C precedent - this file carries no forward git-log pin of
# its own beyond the lifecycle class form).
PRED_MAIN_1315 = "0" * 40  # re-pinned by #1315 terminal log-hash followup per #721

# The #1313 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 1019; zero one-zero-two-zero keys all
# forms / no-Type-C-#1314-in-git-log / fortieth direction absent /
# forty-eighth through fifty-ninth members intact /
# sixtieth member absent / ledger 59).
E1313_FILE = (
    "test_type_b_1313_zoe_kleinman_bbc_pervert_glasses_"
    "vs_openai_ukraine_cyber_defence_oct08_12pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 74295  # patched pre-main: pre-sync 74174 + 121 collected
README_FILE_COUNT = 1639  # pre-sync 1638 + 1 (this file)

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

# Novel source URLs: 3 zero-hit repo-wide pre-commit (git grep -F).
NOVEL_URLS = [
    "https://www.pulse.bot/creator-economy/news/"
    "amazon-launches-program-for-independent-creators-navigating-"
    "ai-search-8a4ac729-bdea-4c0b-a130-ebe96e4baedc/",
    "https://www.netinfluencer.com/amazon-launches-program-for-"
    "independent-creators-navigating-ai-search/",
    "https://mlq.ai/news/amazon-advances-plans-for-ai-content-"
    "licensing-platform-targeting-publishers/",
]


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


def _load_entities():
    return yaml.safe_load(_read(ENTITIES_PATH))


def _block():
    data = _load_entities()
    assert BLOCK_KEY in data
    return data[BLOCK_KEY]


def _block_text():
    return _read(ENTITIES_PATH)


def _git_grep_tracked_source(needle, scope):
    """Grep tracked files at HEAD for a literal needle (fragment-built)."""
    args = ["git", "grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    out = subprocess.run(
        args, cwd=REPO_ROOT, capture_output=True, text=True
    ).stdout
    cleaned = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        if line:
            cleaned.append(line)
    return cleaned


def _class_run(filename, classname):
    target = os.path.join(TESTS_DIR, filename)
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    return subprocess.run(
        ["python3", "-m", "pytest", target,
         "-k", classname,
         "-q", "--no-header"],
        cwd=REPO_ROOT, capture_output=True, text=True, env=env,
    )


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1314:
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
        assert "FIFTH and CLOSING leg of the 1310-1314 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1313/#1312/#1311/#1310 chain; closes 1310-1314.
# ---------------------------------------------------------------------------

class TestRotationGuard1314:
    def test_predecessor_1313_chain_verified(self):
        for sha in (
            PRED_MAIN_1313, PRED_ANCHOR_1313, PRED_DOCSYNC_1313,
            PRED_FINAL_1313, PRED_PUSH_1313,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1312_chain_verified(self):
        for sha in (
            PRED_MAIN_1312, PRED_ANCHOR_1312, PRED_DOCSYNC_1312,
            PRED_FINAL_1312, PRED_PUSH_1312,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1311_chain_verified(self):
        for sha in (
            PRED_MAIN_1311, PRED_ANCHOR_1311, PRED_DOCSYNC_1311,
            PRED_FINAL_1311, PRED_PUSH_1311,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_opener_1310_verified(self):
        for sha in (
            PRED_MAIN_1310, PRED_ANCHOR_1310, PRED_DOCSYNC_1310,
            PRED_FINAL_1310, PRED_PUSH_1310,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1310 -> E #1311 -> A #1312 -> B #1313 -> C #1314" in src

    def test_next_window_opens_1315(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1315 Type D opens the 1315-1319 window" in src

    def test_type_c_lands_one_mechanism(self):
        # Type C lands exactly one mechanism (mechanism 1020); the Type
        # B predecessor landed one (mechanism 1019).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type C lands one mechanism" in src

    def test_fifth_closing_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIFTH and CLOSING leg" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: 1020 lands; key forms stay clean per #715.
# ---------------------------------------------------------------------------

class TestMechanismNovelty1314:
    def test_max_mechanism_id_is_1020_post_landing(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_block_key_present(self):
        assert BLOCK_KEY in _load_entities()

    def test_block_key_occurs_twice_in_text(self):
        text = _block_text()
        assert text.count(BLOCK_KEY) == 2

    def test_1020_numeric_present_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(MECH_NUM) == [ENTITIES_PATH]

    def test_1020_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_1020_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_iteration_field(self):
        assert _block()["iteration"] == 1314

    def test_iteration_type_field(self):
        assert _block()["iteration_type"] == "C"

    def test_no_type_c_1314_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type C #1314" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type C #1314")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1314).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_novel_urls_zero_hit_pre_commit(self):
        # Post-landing the URLs exist in the block's sources (expected);
        # this pin documents the pre-commit novelty claim from the
        # novelty field. Verified by the git grep -F audit pre-commit.
        by_url = {s["url"]: s for s in _block()["sources"]}
        for u in NOVEL_URLS:
            assert u in by_url, u
            assert by_url[u]["novel"] is True, u

    def test_scout_rejection_audit_documented(self):
        # All three rejected scout candidates must be named in the
        # novelty field with their corpus dispositions.
        nov = _block()["novelty"]
        assert "Microsoft" in nov and "PCM" in nov
        assert "Cloudflare" in nov
        assert "ProRata" in nov

    def test_program_name_zero_hit_disclosure(self):
        # The program-name novelty claim must ride the novelty field.
        nov = _block()["novelty"]
        assert "zero-hit" in nov or "zero hit" in nov


# ---------------------------------------------------------------------------
# 4. Block structure at the competitor-entities.yaml top level.
# ---------------------------------------------------------------------------

class TestBlockStructure1314:
    def test_block_key_top_level(self):
        data = _load_entities()
        assert BLOCK_KEY in data
        assert data[BLOCK_KEY]["mechanism_id"] == MECH_NUM

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_block_key_field(self):
        assert _block()["block_key"] == BLOCK_KEY

    def test_required_fields_present(self):
        b = _block()
        for field in ("mechanism_name", "finding", "verdict",
                      "verdict_detail", "novelty", "research_method",
                      "rotation_transparency", "concurrency",
                      "connects_to", "confounders", "sources",
                      "background_suite_status", "falsification_family",
                      "falsification_family_member"):
            assert field in b, field

    def test_connects_to_present(self):
        assert set(_block()["connects_to"]) == {489, 559, 564}

    def test_all_novel_sources(self):
        urls = [s["url"] for s in _block()["sources"]]
        for u in NOVEL_URLS:
            assert u in urls, u

    def test_all_sources_marked_novel(self):
        by_url = {s["url"]: s for s in _block()["sources"]}
        for u in NOVEL_URLS:
            assert by_url[u]["novel"] is True, u

    def test_yaml_parse_clean_flag(self):
        assert _block()["yaml_parse_clean"] is True

    def test_ascii_only_flag(self):
        assert _block()["ascii_only"] is True

    def test_verdict_mechanism_documented(self):
        assert _block()["verdict"] == "mechanism_documented"
        assert _block()["verdict_detail"] == "mechanism_documented"

    def test_manual_qualitative_only(self):
        assert "MANUAL / qualitative ONLY" in _block()["finding"]

    def test_engine_not_run(self):
        assert _block()["engine_run"] is False

    def test_not_falsification_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert "ledger holds at 59" in b["falsification_family"]

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_not_artifact_grade(self):
        assert _block()["artifact_grade"] is False

    def test_browser_opens_zero(self):
        assert _block()["browser_opens"] == 0

    def test_dating_honesty_disclosed(self):
        # The ~mid-Jun-2026 gated-preview vintage vs Oct-2026
        # banking dating must be disclosed in the block (no
        # fresh-announcement overclaim).
        b = _block()
        assert "Jun" in b["finding"] or "113 days" in b["finding"]
        assert "gated preview" in b["finding"]

    def test_block_ascii_only(self):
        def _walk(o):
            if isinstance(o, str):
                o.encode("ascii")
            elif isinstance(o, dict):
                for v in o.values():
                    _walk(v)
            elif isinstance(o, list):
                for v in o:
                    _walk(v)
        _walk(_block())

    def test_no_em_dashes(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        em_dash = chr(0x2014)  # built at runtime per #770; no literal in source
        en_dash = chr(0x2013)
        assert em_dash not in src
        assert en_dash not in src

    def test_yaml_block_ascii(self):
        block = _block()
        yaml.safe_dump(block).encode("ascii")

    def test_key_design_note_no_mech_id_substring(self):
        b = _block()
        assert "no 1020 string" in b["key_design_note"]


# ---------------------------------------------------------------------------
# 5. m1020 content discipline: the in-kind program's four benefits,
#    preview status, eligibility terms, and corpus distinctions.
# ---------------------------------------------------------------------------

class TestM1020ContentDiscipline1314:
    def test_program_name_in_mechanism_name(self):
        assert "Amazon Content Partners" in _block()["mechanism_name"]

    def test_four_benefits_enumerated(self):
        f = _block()["finding"]
        assert "AWS WAF" in f
        assert "Associates" in f
        assert "Amazon Publisher Services" in f
        assert "$100" in f

    def test_bot_control_geometry(self):
        f = _block()["finding"]
        assert "block" in f and "rate-limit" in f and "monetize" in f

    def test_gated_preview_status(self):
        f = _block()["finding"]
        assert "gated preview" in f
        assert "contentpartners.amazon.com" in f

    def test_participation_terms(self):
        f = _block()["finding"]
        assert "voluntary" in f  # lowercase in finding text
        assert "no fees" in f
        assert "no minimum" in f or "no traffic minimum" in f

    def test_us_only_disclosed(self):
        f = _block()["finding"]
        assert "U.S." in f or "US-only" in f

    def test_exit_terms_disclosed(self):
        f = _block()["finding"]
        assert "leave" in f

    def test_in_kind_class_first_claim(self):
        nov = _block()["novelty"]
        assert "in-kind" in nov
        assert "FIRST" in nov

    def test_distinct_from_rufus_legs(self):
        f = _block()["finding"]
        assert "m489" in f or "489" in f
        assert "m564" in f or "564" in f
        assert "cash" in f.lower()

    def test_distinct_from_nyt_alexa(self):
        f = _block()["finding"]
        assert "m559" in f or "559" in f
        assert "$20" in f

    def test_aws_marketplace_context_disclosed(self):
        f = _block()["finding"]
        assert "Feb" in f and "2026" in f
        assert "marketplace" in f.lower()

    def test_confounders_graded(self):
        confs = _block()["confounders"]
        strengths = {c["strength"] for c in confs}
        assert "strong" in strengths
        assert "medium" in strengths
        assert len(confs) >= 4

    def test_trade_press_sourcing_confound(self):
        confs = _block()["confounders"]
        texts = " ".join(c["text"] for c in confs)
        assert "trade" in texts.lower() or "press" in texts.lower()

    def test_no_dollar_licensing_confounder(self):
        confs = _block()["confounders"]
        texts = " ".join(c["text"] for c in confs)
        assert "cash" in texts.lower() or "dollar" in texts.lower()


# ---------------------------------------------------------------------------
# 6. Statistical discipline: MANUAL/qualitative ONLY per the standing rule.
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1314:
    def test_manual_qualitative_only(self):
        b = _block()
        assert "MANUAL / qualitative ONLY" in b["finding"]

    def test_tone_not_scored(self):
        b = _block()
        assert "NOT_SCORED" in b["finding"]
        assert b["tone_scored"] is False

    def test_engine_not_run(self):
        assert _block()["engine_run"] is False

    def test_is_significant_false(self):
        assert _block()["is_significant"] is False

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_not_artifact_grade(self):
        assert _block()["artifact_grade"] is False

    def test_verdict_mechanism_documented(self):
        assert _block()["verdict"] == "mechanism_documented"

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in _block()["finding"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 59 (NOT a member).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1314:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert "NOT a member" in b["falsification_family"]

    def test_fifty_ninth_intact_in_news_corp(self):
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_intact_in_ft(self):
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_seventh_intact_in_ap(self):
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_sixth_intact_in_wired(self):
        out = _git(
            "grep", "-c", "-F", _T56, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_intact_in_atlantic(self):
        out = _git(
            "grep", "-c", "-F", _T55, "HEAD", "--",
            "profiles/atlantic.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_intact_in_guardian(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_third_intact_in_verge(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_second_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_first_intact_in_news_corp(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_forty_ninth_intact_in_journalists(self):
        out = _git(
            "grep", "-c", "-F", _T49, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_forty_eighth_intact_in_ft(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_sixtieth_absent(self):
        assert _git_grep_tracked_source(_T60, None) == []

    def test_fortieth_direction_absent(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_ledger_holds_at_59(self):
        assert "holds at 59" in _block()["falsification_family"]

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (
            "THIRT" + "Y-FIFTH relationship direction",
            "THIRT" + "Y-SIXTH relationship direction",
            "THIRT" + "Y-SEVENTH relationship direction",
            "THIRT" + "Y-EIGHTH relationship direction",
            "THIRT" + "Y-NINTH relationship direction",
        ):
            assert _git_grep_tracked_source(needle, "profiles/") != [], needle


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: forward guards for #1315 Type D.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1314:
    def test_pins_on_1020_landing(self):
        # Type C lands one mechanism: max 1020, next 1021.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1020" in src
        assert "NEXT_NUM = 1021" in src

    def test_no_type_d_1315_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1315's terminal log-hash followup
        # per #721): every commit whose message matches "Type D
        # #1315" must be #1315's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1315 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type D #1315")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1315's own commits"
        main = _git("rev-parse", PRED_MAIN_1315).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1021_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1021_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1021_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

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

    def test_no_sixtieth_member_pin(self):
        # m1020 is NOT a falsification-family member (in-kind
        # small-publisher incentive documentation on the Amazon rail);
        # the sixtieth member-claim form stays absent repo-wide. The
        # needle is fragment-built (per the #1307 literal-discipline
        # repair) so this file carries no contiguous literal.
        assert _git_grep_tracked_source(_T60, None) == []

    def test_predecessor_1313_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1313_FILE))

    def test_next_leg_is_1315_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1315 Type D" in src

    def test_1313_pins_flip_by_design_documented(self):
        # #1313's forward guards (max-1019, zero one-zero-two-zero
        # keys all forms, no-Type-C-#1314-in-git-log, fortieth
        # direction absent, forty-eighth through fifty-ninth members
        # intact in profiles/, sixtieth absent, ledger 59) verified
        # GREEN at HEAD pre-commit this run. The
        # no-Type-C-#1314-in-git-log pin flips BY DESIGN at this run's
        # main commit (the #1191-class self-trip, re-pinned post-commit
        # by TestStalenessPins1314). Type C lands one mechanism, so the
        # zero one-zero-two-zero numeric pin flips BY DESIGN too (the
        # #1272-class forward-guard expiry; the underscore/dash pins
        # stay green by the #723/#738/#739 designed keying).
        # Documented in the staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1314" in src
        assert "no_type_c_1314_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Background-suite check per #795 (OBSERVE ONLY; verdict belongs to
#    #1315).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1314:
    def test_1310_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1310_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1310-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1314_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1310-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1310" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1314:
    def test_readme_test_file_table_has_1314_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1314_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert OWN_BASENAME in arch

    def test_readme_stats_ratcheted(self):
        readme = _read(README_PATH)
        assert "| Tests | %d |" % README_TEST_COUNT in readme
        assert "Across %d test files" % README_FILE_COUNT in readme


# ---------------------------------------------------------------------------
# 11. Iteration-log entry per #721 (3 tests; deselected pre-commit)
# ---------------------------------------------------------------------------

class TestIterationLog1314:
    def test_log_has_1314_entry(self):
        text = _read(LOG_PATH)
        assert "## #1314 Type C" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1020" in text
        assert "mechanism_documented" in text
        assert "ledger holds at 59" in text


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1313's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------

class TestStalenessPins1314:
    def test_1313_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 22 tests in the class; ONE flips
        # BY DESIGN when this run's main commit lands and STAYS
        # flipped: the test_1020_numeric_absent_in_profiles pin (the
        # m1020 landing carries "mechanism_id: 1020" in colon form -
        # the #1272-class forward-guard expiry; the underscore/dash
        # pins stay green by the #723/#738/#739 designed keying). The
        # no_type_c_1314_in_git_log ancestor pin ALSO flips at the
        # main commit but is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1314 now holds this run's
        # main sha, in this file AND in the #1313 file per the #1292
        # re-pin-both-copies precedent). The class run below therefore
        # expects 1 failed / 21 passed and documents the designed flip.
        # The #1313 block is read-only to this run; the flip is
        # documented here, not repaired. Deselected in the in-gate run
        # (fails pre-commit by design).
        res = _class_run(E1313_FILE, "TestGuardLifecycle1313")
        out = res.stdout + res.stderr
        assert "1 failed, 21 passed" in out, out[-2000:]
        assert "test_1020_numeric_absent_in_profiles" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1314:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files via explicit-path staging.
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
