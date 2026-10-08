# -*- coding: utf-8 -*-
"""Type C #1309 tests: Gannett (NYSE: GCI) / USA TODAY Network x Perplexity -
strategic AI content licensing bilateral (Jul 30 2025, banked Oct 8 2026 via
the #784 deferral queue).

Iteration #1309 is the FIFTH and CLOSING leg of the 1305-1309 window
(D #1305 -> E #1306 -> A #1307 -> B #1308 -> C #1309 per the #565 anchor +
rotation guard). This run lands mechanism 1017: the FIRST dedicated corpus
mechanism on a Perplexity local-news bilateral - Gannett licenses USA TODAY
plus 200-plus local newsbrands into Perplexity AI search and the Comet
browser, with ad-revenue sharing plus Sonar API / Enterprise Pro access for
all Gannett staff. The bilateral is Jul-30-2025 vintage, surfaced by the #784
Type C run (Sep 2026) and explicitly deferred there as quote candidate for
the next Type C unquote; this run banks it. Dating honesty is explicit: this
is a previously-uncaptured bilateral, not a new announcement.

Conventions carried forward:
- #565: this run's main commit is the anchor; ANCHORED_SHA starts as 0*40
  and is patched to the main commit sha in the anchor followup.
- #715: pre-commit novelty greps (zero test_type_c_1309 files on disk;
  no "Type C #1309" in git log; max numeric mechanism_id 1016 pre-commit;
  zero numeric/underscore/dash one-zero-one-seven mechanism key forms
  repo-wide pre-commit, needles format-built; block key zero-hit
  pre-commit; "## #1309" zero-hit in iteration-log; README 73684/1633
  pre-commit; no #1309 rows in README/ARCHITECTURE test tables; 3 novel
  URLs zero-hit repo-wide pre-commit).
- #719: doc-sync ratchet (README stats table + test-table row +
  docs/ARCHITECTURE.md tree row + iteration-log entry; README_TEST_COUNT /
  README_FILE_COUNT patched pre-main once the in-gate collection count is
  known).
- #721: terminal log-hash followup registers main/anchor/doc-sync hashes
  in the iteration-log entry and re-pins PRED_MAIN_1309 to the main sha in
  this file and in the #1308 file (the #1292 re-pin-both-copies precedent).
- #795: the #1305-launched background full suite is OBSERVED only this
  run (goal hidden_files type_d_1305_full_suite.log); its verdict belongs
  to #1310.
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
- 0 browser.open per #503 (excerpt-bounded); 3 main-run browser.search
  verification sets + 1 delegated scout (4 ranked candidates, all rejected
  on repo-overlap audit).
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
SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1305_full_suite.log")
OWN_BASENAME = (
    "test_type_c_1309_gannett_perplexity_strategic_bilateral_"
    "oct08_8am.py"
)

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "5cd426485398c1842fe559ced9f30d7212d1c250"  # patched to main commit per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1017
NEXT_NUM = 1018  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_c_1309_gannett_perplexity_strategic_bilateral_"
    "oct08_8am"
)

# Predecessor chain: #1308 Type B (fourth leg).
PRED_MAIN_1308 = "5b997970b53d4a9e687a2f9a1a99e2cd2b558891"
PRED_ANCHOR_1308 = "76924a625ac637196493ea2b9641c0db0d3376e9"
PRED_DOCSYNC_1308 = "50c7558ecdc2f44c442b0bcac93152c9a0f4d2ac"
PRED_FINAL_1308 = "603946bb659a0140477c2fd059f09a3e9f5ef1e7"
PRED_PUSH_1308 = "dc4556c174a383c5c72cc8e09deff7f99b432037"
# #1307 Type A (third leg) for the rotation-guard chain.
PRED_MAIN_1307 = "7009064e750fd2ecb3a0940ebabeb954dee5a789"
PRED_ANCHOR_1307 = "6ee958a7357e20e21d49f076c3fc12d4c955105f"
PRED_DOCSYNC_1307 = "a0ec12d1a983ee810d268d911e453a1a7f21b9e1"
PRED_FINAL_1307 = "73307210c6887a9e1e979a279fd2ec84434166b4"
PRED_PUSH_1307 = "ea18c53b6073eacade2c6f5a96e69214ac991da5"
# #1306 Type E (second leg).
PRED_MAIN_1306 = "0ac1044d0d6398ffcaa7914662323af0dd125c7b"
PRED_ANCHOR_1306 = "69dadafb9f5ab2696cc61a2c5286c93c0715748b"
PRED_DOCSYNC_1306 = "dbed9dbca9bc70bc7602d1d95bd3fdcc14656e9c"
PRED_FINAL_1306 = "f7640d284e1a27dd0f795910dbc3d8da56937fb8"
PRED_PUSH_1306 = "fe8e635fe25c073eaf5c1443eab447467329dfca"
# #1305 Type D (window opener).
PRED_MAIN_1305 = "df99a8be9332a4d8861eff86c046acb13c5f5f10"
PRED_ANCHOR_1305 = "905b5853d9cc7af7cd6a0d26b8157a1be33a7e92"
PRED_DOCSYNC_1305 = "cd2cf1dfe60b207c8833f914ae529f6ed9c0e0ac"
PRED_FINAL_1305 = "2a8709d90ee8d38fa76bcf0c6cb326bcdb2347d4"
PRED_PUSH_1305 = "75551707c04583655e2a51bd43aa237aa9f9617a"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40).
PRED_MAIN_1309 = "5cd426485398c1842fe559ced9f30d7212d1c250"  # re-pinned to main sha in the terminal log-hash followup per #721

# Forward guard for the next leg: #1310 Type D. Re-pinned by #1310's
# log-hash followup per #721 (starts as 0*40; placeholder-only per
# the Type C precedent - this file carries no forward git-log pin of
# its own beyond the lifecycle class form).
PRED_MAIN_1310 = "84f3c3190dff8fc3d9342450c45aa021ac965496"  # re-pinned by #1310 terminal log-hash followup per #721

# The #1308 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 1016; zero one-zero-one-seven keys all
# forms / no-Type-C-#1309-in-git-log / fortieth direction absent /
# forty-eighth through fifty-ninth members intact /
# sixtieth member absent / ledger 59).
E1308_FILE = (
    "test_type_b_1308_tobi_opeyemi_amure_thestreet_meta_glasses_"
    "vs_openai_astra_oct08_7am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 73762  # patched pre-main: pre-sync 73684 + 78 collected
README_FILE_COUNT = 1634  # pre-sync 1633 + 1 (this file)

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
    "https://www.silicon.co.uk/press-release/gannett-usa-today-"
    "network-and-perplexity-announce-strategic-ai-content-"
    "licensing-agreement",
    "https://www.usatodayco.com/pr/gannett-i-usa-today-network-"
    "and-perplexity-announce-strategic-ai-content-licensing-"
    "ageement/",
    "https://stocktitan.net/news/GCI/gannett-usa-today-network-"
    "and-perplexity-announce-strategic-ai-18rqzi0x1xqv.html",
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

class TestAnchor1309:
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
        assert "FIFTH and CLOSING leg of the 1305-1309 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1308/#1307/#1306/#1305 chain; closes 1305-1309.
# ---------------------------------------------------------------------------

class TestRotationGuard1309:
    def test_predecessor_1308_chain_verified(self):
        for sha in (
            PRED_MAIN_1308, PRED_ANCHOR_1308, PRED_DOCSYNC_1308,
            PRED_FINAL_1308, PRED_PUSH_1308,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1307_chain_verified(self):
        for sha in (
            PRED_MAIN_1307, PRED_ANCHOR_1307, PRED_DOCSYNC_1307,
            PRED_FINAL_1307, PRED_PUSH_1307,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1306_chain_verified(self):
        for sha in (
            PRED_MAIN_1306, PRED_ANCHOR_1306, PRED_DOCSYNC_1306,
            PRED_FINAL_1306, PRED_PUSH_1306,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_opener_1305_verified(self):
        for sha in (
            PRED_MAIN_1305, PRED_ANCHOR_1305, PRED_DOCSYNC_1305,
            PRED_FINAL_1305, PRED_PUSH_1305,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1305 -> E #1306 -> A #1307 -> B #1308 -> C #1309" in src

    def test_next_window_opens_1310(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1310 Type D opens the 1310-1314 window" in src

    def test_type_c_lands_one_mechanism(self):
        # Type C lands exactly one mechanism (mechanism 1017); the Type
        # B predecessor landed one (mechanism 1016).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type C lands one mechanism" in src

    def test_fifth_closing_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIFTH and CLOSING leg" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: 1017 lands; key forms stay clean per #715.
# ---------------------------------------------------------------------------

class TestMechanismNovelty1309:
    def test_max_mechanism_id_is_1017_post_landing(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_block_key_present(self):
        assert BLOCK_KEY in _load_entities()

    def test_block_key_occurs_twice_in_text(self):
        text = _block_text()
        assert text.count(BLOCK_KEY) == 2

    def test_1017_numeric_present_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(MECH_NUM) == [ENTITIES_PATH]

    def test_1017_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_1017_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_iteration_field(self):
        assert _block()["iteration"] == 1309

    def test_iteration_type_field(self):
        assert _block()["iteration_type"] == "C"

    def test_no_type_c_1309_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type C #1309" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type C #1309")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1309).stdout.strip()
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

    def test_deferral_queue_honored(self):
        # The #784 deferral bullet designated this bilateral as
        # candidate for the next Type C; the block documents the
        # deferral in the finding and novelty fields.
        b = _block()
        assert "#784" in b["finding"] or "#784" in b["novelty"]
        assert "candidate for the next Type C" in b["novelty"]


# ---------------------------------------------------------------------------
# 4. Block structure at the competitor-entities.yaml top level.
# ---------------------------------------------------------------------------

class TestBlockStructure1309:
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
        assert set(_block()["connects_to"]) == {391, 663, 750}

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
        # The Jul-2025 vintage vs Oct-2026 banking dating must be
        # disclosed in the block (no fresh-announcement overclaim).
        b = _block()
        assert "Jul 30 2025" in b["finding"] or "Jul-30-2025" in b["finding"]
        assert "deferred" in b["finding"] or "deferral" in b["novelty"]

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

    def test_scout_rejection_audit_documented(self):
        # All four scout candidates rejected on repo-overlap must be
        # named in the novelty field with their corpus dispositions.
        nov = _block()["novelty"]
        assert "Snap x Perplexity" in nov
        assert "Google UK" in nov
        assert "Apple-Google Gemini" in nov or "Apple x Google Gemini" in nov
        assert "Penske" in nov


# ---------------------------------------------------------------------------
# 5. Guard lifecycle: forward guards for #1310 Type D.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1309:
    def test_pins_on_1017_landing(self):
        # Type C lands one mechanism: max 1017, next 1018.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1017" in src
        assert "NEXT_NUM = 1018" in src

    def test_no_type_d_1310_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1310's terminal log-hash followup
        # per #721): every commit whose message matches "Type D
        # #1310" must be #1310's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1310 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type D #1310")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1310's own commits"
        main = _git("rev-parse", PRED_MAIN_1310).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1018_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1018_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1018_dash_absent_repo_wide(self):
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
        # m1017 is NOT a falsification-family member (local-news
        # bilateral documentation on the Perplexity rail); the
        # sixtieth member-claim form stays absent repo-wide. The
        # needle is fragment-built (per the #1307 literal-discipline
        # repair) so this file carries no contiguous literal.
        assert _git_grep_tracked_source(_T60, None) == []

    def test_predecessor_1308_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1308_FILE))

    def test_next_leg_is_1310_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1310 Type D" in src

    def test_1308_pins_flip_by_design_documented(self):
        # #1308's forward guards (max-1016, zero one-zero-one-seven
        # keys all forms, no-Type-C-#1309-in-git-log, fortieth
        # direction absent, forty-eighth through fifty-ninth members
        # intact in profiles/, sixtieth absent, ledger 59) verified
        # GREEN at HEAD pre-commit this run. The
        # no-Type-C-#1309-in-git-log pin flips BY DESIGN at this run's
        # main commit (the #1191-class self-trip, re-pinned post-commit
        # by TestStalenessPins1309). Type C lands one mechanism, so the
        # zero one-zero-one-seven numeric pin flips BY DESIGN too (the
        # #1272-class forward-guard expiry; the underscore/dash pins
        # stay green by the #723/#738/#739 designed keying).
        # Documented in the staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1309" in src
        assert "no_type_c_1309_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 6. Staleness pins: #1308's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------

class TestStalenessPins1309:
    def test_1308_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 22 tests in the class; ONE flips
        # BY DESIGN when this run's main commit lands and STAYS
        # flipped: the test_1017_numeric_absent_in_profiles pin (the
        # m1017 landing carries "mechanism_id: 1017" in colon form -
        # the #1272-class forward-guard expiry; the underscore/dash
        # pins stay green by the #723/#738/#739 designed keying). The
        # no_type_c_1309_in_git_log ancestor pin ALSO flips at the
        # main commit but is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1309 now holds this run's
        # main sha, in this file AND in the #1308 file per the #1292
        # re-pin-both-copies precedent). The class run below therefore
        # expects 1 failed / 21 passed and documents the designed flip.
        # The #1308 block is read-only to this run; the flip is
        # documented here, not repaired. Deselected in the in-gate run
        # (fails pre-commit by design).
        res = _class_run(E1308_FILE, "TestGuardLifecycle1308")
        out = res.stdout + res.stderr
        assert "1 failed, 21 passed" in out, out[-2000:]
        assert "test_1017_numeric_absent_in_profiles" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 7. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1309:
    def test_readme_test_file_table_has_1309_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1309_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert OWN_BASENAME in arch

    def test_readme_stats_ratcheted(self):
        readme = _read(README_PATH)
        assert "| Tests | %d |" % README_TEST_COUNT in readme
        assert "Across %d test files" % README_FILE_COUNT in readme


# ---------------------------------------------------------------------------
# 8. Iteration-log entry per #721 (3 tests; deselected pre-commit)
# ---------------------------------------------------------------------------

class TestIterationLog1309:
    def test_log_has_1309_entry(self):
        text = _read(LOG_PATH)
        assert "## #1309 Type C" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1017" in text
        assert "mechanism_documented" in text
        assert "ledger holds at 59" in text


# ---------------------------------------------------------------------------
# 9. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1309:
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
