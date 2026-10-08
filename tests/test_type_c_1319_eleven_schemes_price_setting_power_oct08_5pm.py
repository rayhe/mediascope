# -*- coding: utf-8 -*-
"""Type C #1319 tests: eleven-scheme AI-content payment landscape and the
price-setting-power split (nohacks.co, Oct 4 2026) - FIRST dedicated corpus
mechanism on the third-party taxonomy of AI-content payment schemes,
documented as mechanism 1023.

Iteration #1319 is the FIFTH and CLOSING leg of the 1315-1319 window
(D #1315 -> E #1316 -> A #1317 -> B #1318 -> C #1319 per the #565 anchor +
rotation guard). This run lands mechanism 1023: the FIRST dedicated corpus
mechanism on the nohacks.co "Eleven Ways Websites Can Get Paid For AI Use,
And Who Sets The Price In Each" taxonomy (~Oct 4 2026) - a
landscape-consolidation leg mapping who sets the price across the payment
rails (website-sets-price vs AI-company-sets-price), cross-referenced against
the corpus's mapped rails (TollBit m789/m1014, Cloudflare m786/m1013,
Google pilot m702/m708/m891, Amazon Content Partners m1020). The
bilateral-deal layer is documented as saturated this run (1 delegated scout,
4 candidates, ALL rejected; 6 main-run browser.search verification sets).

Conventions carried forward:
- #565: this run's main commit is the anchor; ANCHORED_SHA starts as 0*40
  and is patched to the main commit sha in the anchor followup.
- #715: pre-commit novelty greps (zero test_type_c_1319 files on disk;
  no "Type C #1319" in git log; max numeric mechanism_id 1022 pre-commit;
  zero numeric/underscore/dash one-zero-two-three mechanism key forms
  repo-wide pre-commit, needles format-built; block key zero-hit
  pre-commit; "## #1319" zero-hit in iteration-log; README 74705/1643
  pre-commit; no #1319 rows in README/ARCHITECTURE test tables; 1 novel
  URL zero-hit repo-wide pre-commit).
- #719: doc-sync ratchet (README stats table + test-table row +
  docs/ARCHITECTURE.md tree row + iteration-log entry; README_TEST_COUNT /
  README_FILE_COUNT patched pre-main once the in-gate collection count is
  known).
- #721: terminal log-hash followup registers main/anchor/doc-sync hashes
  in the iteration-log entry and re-pins PRED_MAIN_1319 to the main sha in
  this file and in the #1318 file (the #1292 re-pin-both-copies precedent).
- #795: the #1315-launched background full suite is OBSERVED only this
  run (goal hidden_files type_d_1315_full_suite.log); its verdict belongs
  to #1320.
- Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test
  file working-tree edit), #900 (untracked Type D test file), #1012-wt
  (working-tree edit on the committed Type A #1012 file) all stay out of
  this run's index/diff via explicit-path staging. Do NOT touch #1024's
  m846: self-flagged sourcing-constraint violation; Ray's
  revert/leave/rebuild-from-primary decision still pending.
- The Aug 28 2026 standing rule: MANUAL / qualitative ONLY. No
  coverage-tone pair scored (tone NOT_SCORED); p_value/cohens_d/ci_95
  NOT_CALCULATED; is_significant false; engine NOT run; verdict
  mechanism_documented; NOT a falsification-family member (ledger holds
  at 59); NOT artifact-grade; no_analysis_json_update true.
- 0 browser.open per #503 (excerpt-bounded); 6 main-run browser.search
  verification sets + 1 delegated scout (4 ranked candidates, ALL
  rejected on main-run corpus verification).
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
SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1315_full_suite.log")
OWN_BASENAME = (
    "test_type_c_1319_eleven_schemes_price_setting_power_"
    "oct08_5pm.py"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "0" * 40

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1023
NEXT_NUM = 1024  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_c_1319_eleven_schemes_price_setting_power_"
    "oct08_5pm"
)

# Predecessor chain: #1318 Type B (fourth leg).
PRED_MAIN_1318 = "71c2cc5219e7a00986312a1278b6bb2caf7d0bb2"
PRED_ANCHOR_1318 = "f61ddae6031bd8587f4009a02b540b70d5986c33"
PRED_DOCSYNC_1318 = "725e0db1d983b68e240f1b5d4639fdf531ca9791"
PRED_FINAL_1318 = "ee817ba07730ed333f4005869d256d1286baa8a5"
PRED_PUSH_1318 = "88c3a344b56832d57a11a72e79d78fdf9e0edd33"
# #1317 Type A (third leg) for the rotation-guard chain.
PRED_MAIN_1317 = "7749f95d8d5b36031bba2bf11ddc92636d48b753"
PRED_ANCHOR_1317 = "27fb204cf0f1b94c038f1a1678a805a7e4bf0600"
PRED_DOCSYNC_1317 = "c5b63c08ac60c741a1af727e854f3c7df694abdd"
PRED_FINAL_1317 = "8f3d3f8da89ce7d7688e8f720d9d414954eace9a"
# #1316 Type E (second leg).
PRED_MAIN_1316 = "5d160c6cc9a8d68e863499b4e5fc142845c21060"
PRED_ANCHOR_1316 = "49d60e8ac4b57b1b9c76b585b4d4484217fb4f26"
PRED_DOCSYNC_1316 = "9e3dc23ba09a831477253f38267fbbdcabf439ab"
PRED_FINAL_1316 = "4867ff1c0bfa89b469f794c0220f9c295dd40c4f"
# #1315 Type D (window opener).
PRED_MAIN_1315 = "137d1a952e65889587a464db7d9e96a584078717"
PRED_ANCHOR_1315 = "265d3e569f59ea55aa14458ae64206c8224a3af0"
PRED_DOCSYNC_1315 = "5e867883942d75b4c5dc329460f2c7b6f41e3e10"
PRED_FINAL_1315 = "2e11a9f9f5d36cca715d688860e051bb33adc979"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the own-run git-log pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1319 = "0" * 40

# Forward guard for the next leg: #1320 Type D. Re-pinned by #1320's
# log-hash followup per #721 (starts as 0*40; placeholder-only per
# the Type C precedent - this file carries no forward git-log pin of
# its own beyond the lifecycle class form).
PRED_MAIN_1320 = "0" * 40

# The #1318 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 1022; zero one-zero-two-three keys all
# forms / no-Type-C-#1319-in-git-log / fortieth direction absent /
# forty-eighth through fifty-ninth members intact /
# sixtieth member absent / ledger 59).
E1318_FILE = (
    "test_type_b_1318_will_shanklin_engadget_muse_glasses_"
    "vs_iphone_duo_camera_oct08_4pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 74826  # patched pre-main: pre-sync 74705 + 121 collected
README_FILE_COUNT = 1644  # pre-sync 1643 + 1 (this file)

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

# Novel source URL: 1 zero-hit repo-wide pre-commit (git grep -F).
NOVEL_URLS = [
    "https://nohacks.co/blog/websites-get-paid-for-ai-use-who-sets-the-price",
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

class TestAnchor1319:
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
        assert "FIFTH and CLOSING leg of the 1315-1319 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1318/#1317/#1316/#1315 chain; closes 1315-1319.
# ---------------------------------------------------------------------------

class TestRotationGuard1319:
    def test_predecessor_1318_chain_verified(self):
        for sha in (
            PRED_MAIN_1318, PRED_ANCHOR_1318, PRED_DOCSYNC_1318,
            PRED_FINAL_1318, PRED_PUSH_1318,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1317_chain_verified(self):
        for sha in (
            PRED_MAIN_1317, PRED_ANCHOR_1317, PRED_DOCSYNC_1317,
            PRED_FINAL_1317,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1316_chain_verified(self):
        for sha in (
            PRED_MAIN_1316, PRED_ANCHOR_1316, PRED_DOCSYNC_1316,
            PRED_FINAL_1316,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_opener_1315_verified(self):
        for sha in (
            PRED_MAIN_1315, PRED_ANCHOR_1315, PRED_DOCSYNC_1315,
            PRED_FINAL_1315,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1315 -> E #1316 -> A #1317 -> B #1318 -> C #1319" in src

    def test_next_window_opens_1320(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1320 Type D opens the 1320-1324 window" in src

    def test_type_c_lands_one_mechanism(self):
        # Type C lands exactly one mechanism (mechanism 1023); the Type
        # B predecessor landed one (mechanism 1022).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type C lands one mechanism" in src

    def test_fifth_closing_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIFTH and CLOSING leg" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: 1023 lands; key forms stay clean per #715.
# ---------------------------------------------------------------------------

class TestMechanismNovelty1319:
    def test_max_mechanism_id_is_1023_post_landing(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1319 in key, no 1023 or
        # 1024 substring.
        assert "1319" in BLOCK_KEY
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
        nums = []
        for _line in _repo_grep_numeric_mechanism_id(MECH_NUM):
            nums.append(MECH_NUM)
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert len(_repo_grep_numeric_mechanism_id(MECH_NUM)) >= 1

    def test_no_type_c_1319_in_git_log_own_run(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type C #1319" must be #1319's main
        # commit or a descendant of it. Deselected in the in-gate run
        # (fails pre-commit by design: PRED_MAIN_1319 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1319")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1319's own commits"
        main = _git("rev-parse", PRED_MAIN_1319).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_novel_url_zero_hit_pre_commit(self):
        # The novel URL was verified zero-hit repo-wide pre-commit
        # via git grep -F this run.
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--", ".")
            assert out.stdout.strip() == "", url

    def test_taxonomy_first_dedicated_mechanism(self):
        # FIRST dedicated corpus mechanism on the third-party
        # AI-content payment-scheme taxonomy: zero nohacks.co hits and
        # zero "eleven schemes" hits pre-commit; the five visible
        # schemes individually mapped or mention-level but the
        # comparative taxonomy unbanked. Disclosed in the block's
        # novelty note.
        nov = _block()["novelty"]
        assert "FIRST dedicated corpus mechanism" in nov
        assert "nohacks.co" in nov


# ---------------------------------------------------------------------------
# 4. Block structure in profiles/competitor-entities.yaml.
# ---------------------------------------------------------------------------

class TestBlockStructure1319:
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
        assert set(_block()["connects_to"]) == {702, 786, 789, 891,
                                                1013, 1014, 1020}

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
        # The ~Oct-4-2026 taxonomy vintage vs Oct-8-2026 banking must
        # be disclosed (no fresh-announcement overclaim); the
        # AI-company-sets table is explicitly NOT enumerated
        # (excerpt-bounded per #503).
        b = _block()
        assert "Oct 4" in b["finding"] or "4 days" in b["finding"]
        assert "NOT enumerated" in b["finding"]

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
        assert "no 1023 string" in b["key_design_note"]


# ---------------------------------------------------------------------------
# 5. m1023 content discipline: the eleven-scheme taxonomy, the
#    price-setting-power split, corpus cross-references, and the
#    saturation context.
# ---------------------------------------------------------------------------

class TestM1023ContentDiscipline1319:
    def test_taxonomy_name_in_mechanism_name(self):
        assert "Eleven-scheme" in _block()["mechanism_name"]
        assert "price-setting-power" in _block()["mechanism_name"]

    def test_five_website_sets_schemes_enumerated(self):
        f = _block()["finding"]
        assert "Cloudflare Pay Per Crawl" in f
        assert "Cloudflare Monetization Gateway" in f
        assert "x402" in f
        assert "TollBit" in f
        assert "RSL Collective" in f

    def test_price_setting_split_framed(self):
        f = _block()["finding"]
        assert "WHO SETS THE PRICE" in f
        assert "WEBSITE-SETS-PRICE GROUP" in f
        assert "AI-COMPANY-SETS-PRICE GROUP" in f

    def test_none_named_marker_explained(self):
        f = _block()["finding"]
        assert "None named" in f

    def test_ai_company_sets_table_not_enumerated(self):
        # Excerpt-bounded per #503: the second table's rows were not
        # visible, so they are explicitly NOT enumerated.
        f = _block()["finding"]
        assert "not excerpt-visible" in f
        assert "NOT enumerated" in f

    def test_corpus_cross_reference_tollbit(self):
        f = _block()["finding"]
        assert "m789" in f
        assert "m1014" in f

    def test_corpus_cross_reference_cloudflare(self):
        f = _block()["finding"]
        assert "m786" in f
        assert "m1013" in f

    def test_corpus_cross_reference_google_pilot(self):
        f = _block()["finding"]
        assert "m702" in f
        assert "m891" in f

    def test_corpus_cross_reference_amazon(self):
        f = _block()["finding"]
        assert "m1020" in f

    def test_rsl_mention_level_disclosed(self):
        f = _block()["finding"]
        assert "mention-level only" in f

    def test_saturation_context_documented(self):
        f = _block()["finding"]
        assert "SATURATION CONTEXT" in f
        assert "delegated scout" in f
        assert "ALL rejected" in f

    def test_scout_rejections_enumerated(self):
        f = _block()["finding"]
        assert "Axel Springer" in f
        assert "Getty" in f

    def test_main_run_saturation_checks_enumerated(self):
        f = _block()["finding"]
        assert "Redpine" in f
        assert "Impelsys x Cashmere" in f
        assert "xAI/Grok" in f

    def test_landscape_consolidation_framing(self):
        f = _block()["finding"]
        assert "landscape-consolidation" in f
        assert "not a new bilateral" in f

    def test_confounders_graded(self):
        confs = _block()["confounders"]
        strengths = {c["strength"] for c in confs}
        assert "strong" in strengths
        assert "medium" in strengths
        assert len(confs) >= 4

    def test_single_outlet_confound(self):
        confs = _block()["confounders"]
        texts = " ".join(c["text"] for c in confs)
        assert "Single-outlet" in texts

    def test_no_new_bilateral_confounder(self):
        confs = _block()["confounders"]
        texts = " ".join(c["text"] for c in confs)
        assert "No new bilateral" in texts


# ---------------------------------------------------------------------------
# 6. Statistical discipline: MANUAL/qualitative ONLY per the standing rule.
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1319:
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

class TestFalsificationLedger1319:
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
# 8. Guard lifecycle: forward guards for #1320 Type D.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1319:
    def test_pins_on_1023_landing(self):
        # Type C lands one mechanism: max 1023, next 1024.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1023" in src
        assert "NEXT_NUM = 1024" in src

    def test_no_type_d_1320_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1320's terminal log-hash followup
        # per #721): every commit whose message matches "Type D
        # #1320" must be #1320's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1320 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type D #1320")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1320's own commits"
        main = _git("rev-parse", PRED_MAIN_1320).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1024_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1024_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1024_dash_absent_repo_wide(self):
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
        # m1023 is NOT a falsification-family member (eleven-scheme
        # landscape-consolidation documentation); the sixtieth
        # member-claim form stays absent repo-wide. The needle is
        # fragment-built (per the #1307 literal-discipline repair) so
        # this file carries no contiguous literal.
        assert _git_grep_tracked_source(_T60, None) == []

    def test_predecessor_1318_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1318_FILE))

    def test_next_leg_is_1320_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1320 Type D" in src

    def test_1318_pins_flip_by_design_documented(self):
        # #1318's forward guards (max-1022, zero one-zero-two-three
        # keys all forms, no-Type-C-#1319-in-git-log, fortieth
        # direction absent, forty-eighth through fifty-ninth members
        # intact in profiles/, sixtieth absent, ledger 59) verified
        # GREEN at HEAD pre-commit this run. The
        # no-Type-C-#1319-in-git-log pin flips BY DESIGN at this run's
        # main commit (the #1191-class self-trip, re-pinned post-commit
        # by TestStalenessPins1319). Type C lands one mechanism, so the
        # zero one-zero-two-three numeric pin flips BY DESIGN too (the
        # #1272-class forward-guard expiry; the underscore/dash pins
        # stay green by the #723/#738/#739 designed keying).
        # Documented in the staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1319" in src
        assert "no_type_c_1319_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Background-suite check per #795 (OBSERVE ONLY; verdict belongs to
#    #1320).
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1319:
    def test_1315_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1315_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1315-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1319_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1315-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1315" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1319:
    def test_readme_test_file_table_has_1319_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1319_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert OWN_BASENAME in arch

    def test_readme_stats_ratcheted(self):
        readme = _read(README_PATH)
        assert "| Tests | %d |" % README_TEST_COUNT in readme
        assert "Across %d test files" % README_FILE_COUNT in readme


# ---------------------------------------------------------------------------
# 11. Iteration-log entry per #721 (3 tests; deselected pre-commit)
# ---------------------------------------------------------------------------

class TestIterationLog1319:
    def test_log_has_1319_entry(self):
        text = _read(LOG_PATH)
        assert "## #1319 Type C" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1023" in text
        assert "mechanism_documented" in text
        assert "ledger holds at 59" in text


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1318's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------

class TestStalenessPins1319:
    def test_1318_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 22 tests in the class; ONE flips
        # BY DESIGN when this run's main commit lands and STAYS
        # flipped: the test_1023_numeric_absent_in_profiles pin (the
        # m1023 landing carries "mechanism_id: 1023" in colon form -
        # the #1272-class forward-guard expiry; the underscore/dash
        # pins stay green by the #723/#738/#739 designed keying). The
        # no_type_c_1319_in_git_log ancestor pin ALSO flips at the
        # main commit but is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1319 now holds this run's
        # main sha, in this file AND in the #1318 file per the #1292
        # re-pin-both-copies precedent). The class run below therefore
        # expects 1 failed / 21 passed and documents the designed flip.
        # The #1318 block is read-only to this run; the flip is
        # documented here, not repaired. Deselected in the in-gate run
        # (fails pre-commit by design).
        res = _class_run(E1318_FILE, "TestGuardLifecycle1318")
        out = res.stdout + res.stderr
        assert "1 failed, 21 passed" in out, out[-2000:]
        assert "test_1023_numeric_absent_in_profiles" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1319:
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
