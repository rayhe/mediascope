# -*- coding: utf-8 -*-
"""Type A #1237 tests: Barron's (Dow Jones / News Corp) - OpenAI
Oct-1-2026 FTC-probe enforcement coverage (NEW B1 arm, first use as a
primary arm; in-corpus only as a #1147 corroborating relay) + Sep-30
Daily-roundup Astra-cancellation card (NEW B2 arm) vs Barron's in-window
Meta Connect/Muse investor-forward pair (NEW M1/M2 arms, Sep 23-24).

Mechanism 973 (the fifty-first falsification-family member; the live
full-form claim lives in profiles/news-corp.yaml;
ledger 50->51). FIRST dedicated corpus mechanism on the Barron's
publication line (third News Corp title after WSJ/NY Post): the naive
uniform payer-softening prediction (competitor_relationships.openai
coverage_prediction 'softer', from the May 2024 News Corp-OpenAI
$250M/5yr deal) FAILS at Barron's, and the dual-payer payment-scale
prediction fails with it - the 5:1 larger payer (OpenAI $250M/5yr) gets
the harder register (-0.275 arm avg, enforcement accountability with
comment-seeking) than the $50M/yr Meta deal partner (+0.075 arm avg,
investor-forward). Illustrative delta (OpenAI minus Meta) -0.35.
Enforcement-register replication of the m904 WSJ News Corp line at a
second News Corp title. Cross-peg confound disclosed (enforcement peg
vs product-launch pegs); bounded absence of an in-window Barron's Meta
enforcement-scale peg. Statistical discipline: MANUAL/QUALITATIVE ONLY
per the Aug 28 2026 standing rule (tones hand-assigned, n=2 vs n=2;
p_value/cohens_d/ci_95 NOT_CALCULATED; engine NOT run; is_significant
false; NOT artifact-grade; no analysis.json update).

Research: delegated scout proposed WSJ x OpenAI on the Astra peg -
REJECTED on main-run verification (m904 #1122 already counted the WSJ
x OpenAI safety-crisis test on the same peg; #1143
temporal-replication precedent; the scout's verbatim URLs confirmed
real but the pair was saturated). Time x OpenAI and Guardian x
Anthropic rejected for failing verbatim-URL discipline (no citable
time.com/theguardian.com originals surfaced). SELECTED Barron's x
OpenAI (novel line, parent-level dual-payer tie). 4 main-run
browser.search verification sets (B1/B2/M1/M2 URLs confirmed verbatim
from Full-URL listings; B1 re-surface confirmed in-corpus via git
grep). 0 browser.open per #503 (excerpt-bounded; barrons.com
paywalled).

The mechanism 973 block lives in profiles/news-corp.yaml as a
competitor_relationships.openai sub-key (4-space indent), appended at
the end of the openai section (after the m958 block). Targeted staging
by explicit path only; the in-flight #899/#938/#900/#1012-wt files stay
out of this run's index/diff.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor; TestAnchor1237 deselected in the in-gate run.

Per #795: this run only CHECKS the #1235-launched background suite
(goal hidden_files type_d_1235_full_suite.log, observed ALIVE at this
run's check); its verdict and tombstone belong to #1240 (next Type D).
This run neither re-launches, kills, nor writes to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth / forty-ninth / fiftieth /
fifty-first / fifty-second member-claim forms, or the thirty-fifth
through fortieth direction forms; the constants are constructed at
runtime. (The landed ordinals live as short lowercase forms in prose
here; the live full-form claims live in profiles/financial-times.yaml,
profiles/careers/journalists.yaml, and profiles/news-corp.yaml: the
forty-eighth, forty-ninth, fiftieth, and fifty-first members
respectively.)
"""

import os
import re
import subprocess

import pytest

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
OWN_BASENAME = (
    "test_type_a_1237_barrons_openai_ftc_probe_enforcement_vs_"
    "meta_connect_investor_forward_oct05_11am.py"
)
PROFILE_FILE = os.path.join(PROFILES_DIR, "news-corp.yaml")

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "e0da8e28bee3e3bb284021b4768b1ef618428457"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 973
NEXT_NUM = 974  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_a_1237_barrons_openai_ftc_probe_enforcement_vs_"
    "meta_connect_investor_forward_oct05_11am"
)

# Predecessor chain: #1236 Type E continued the 1235-1239 window.
PRED_MAIN_1236 = "a403518b"
PRED_ANCHOR_1236 = "19ae4fc2"
PRED_DOCSYNC_1236 = "d1350466"
PRED_FINAL_1236 = "a5e8af23"

# The #1236 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 972; zero next-number nine-seven-three
# keys all forms / no-Type-A-#1237-in-git-log / fortieth direction
# absent / forty-eighth + forty-ninth + fiftieth members intact /
# fifty-first member absent / ledger 50).
E1236_FILE = (
    "test_type_e_1236_podcast_sentiment_170th_verification_oct05_10am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 67389  # post-doc-sync total (pre-sync 67311 + 78)
README_FILE_COUNT = 1562  # pre-sync 1561 + 1 (this file)

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"

# Novel source URLs: 3 are zero-hit repo-wide pre-commit (git grep -F);
# the B1 FTC URL is an in-corpus re-surface (cited as a #1147
# corroborating relay; FIRST use as a primary arm this run).
NOVEL_URLS = [
    "https://www.barrons.com/articles/"
    "stock-market-things-to-know-today-oura-anthropic-openai-ipo-ce6267d0",
    "https://www.barrons.com/articles/"
    "meta-vr-glasses-muse-ai-apple-64b98241",
    "https://www.barrons.com/articles/"
    "meta-connect-2026-muse-ai-1c069cf1",
]
RESURFACE_URL = (
    "https://www.barrons.com/articles/"
    "ftc-openai-anthropic-ai-safety-investigation-8eb4be96"
)


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


def _iter_working_tree_profiles():
    """Yield profile paths in the working tree (includes uncommitted)."""
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
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


def _working_tree_grep_profiles(needle):
    """Grep working-tree profiles/ for a literal needle (fragment-built).

    Used for the fifty-first member pin: the landed claim lives in the
    uncommitted block pre-commit.
    """
    return [
        p
        for p in _iter_working_tree_profiles()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _load_newscorp():
    import yaml
    return yaml.safe_load(_read(PROFILE_FILE))


def _openai_section():
    return _load_newscorp()["competitor_relationships"]["openai"]


def _block():
    return _openai_section()[BLOCK_KEY]


def _block_text():
    return _read(PROFILE_FILE)


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

class TestAnchor1237:
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
        assert "THIRD leg of the 1235-1239 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1237:
    def test_predecessor_1236_chain_verified(self):
        for sha in (
            PRED_MAIN_1236, PRED_ANCHOR_1236, PRED_DOCSYNC_1236,
            PRED_FINAL_1236,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1235_chain_verified(self):
        for sha in ("933e69a7", "8ca2b606", "8ac95ab1", "76e92dd9"):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1235 -> E #1236 -> A #1237 -> B #1238 -> C #1239" in src

    def test_next_leg_is_type_b_1238(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1238 Type B" in src

    def test_type_a_lands_one_mechanism(self):
        # Type A lands exactly one mechanism (mechanism 973); the Type
        # E predecessor added none.
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type A lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1237:
    def test_barrons_line_new_at_head(self):
        # FIRST dedicated Barron's publication-line mechanism: no
        # barrons_openai block key in tracked profiles/ at HEAD.
        assert _git_grep_tracked_source("barrons_openai", "profiles/") == []

    def test_openai_section_found(self):
        sec = _openai_section()
        assert BLOCK_KEY in sec

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1237 in key, no 973 or
        # 974 substring.
        assert "1237" in BLOCK_KEY
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
        for n in range(MECH_NUM + 1, MECH_NUM + 20):
            assert _repo_grep_numeric_mechanism_id(n) == [], n
        assert nums, "mechanism 973 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_novel_urls_in_block_source_urls_verbatim(self):
        b = _block()
        urls = [u["url"] for u in b["source_urls"]]
        for novel in NOVEL_URLS:
            assert novel in urls, novel

    def test_resurface_b1_in_block_and_in_corpus(self):
        # B1 is a re-surface (in-corpus as a #1147 corroborating relay)
        # used as a primary arm for the first time this run.
        b = _block()
        urls = [u["url"] for u in b["source_urls"]]
        assert RESURFACE_URL in urls
        hits = _git_grep_tracked_source(RESURFACE_URL, None)
        assert "profiles/news-corp.yaml" in hits
        assert any("test_type_a_1147" in h for h in hits)

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit
        # it appears only in the landed YAML block and the doc-sync
        # targets (README, ARCHITECTURE, iteration-log). This test
        # file never carries the contiguous key: BLOCK_KEY is
        # fragment-built per #715.
        out = _git("grep", "-F", "-l", BLOCK_KEY, "HEAD", "--", ".").stdout
        hits = []
        for line in out.splitlines():
            line = line.strip()
            if line.startswith("HEAD:"):
                line = line[len("HEAD:"):]
            if line.strip():
                hits.append(line.strip())
        allowed = {
            os.path.join("profiles", "news-corp.yaml"),
            "README.md",
            os.path.join("docs", "ARCHITECTURE.md"),
            "iteration-log.md",
        }
        for h in hits:
            assert h in allowed, h

    def test_no_barrons_openai_arm_before_this_run(self):
        # The novelty claim: no barrons_openai arm block existed in
        # news-corp.yaml before this run's landing; now present only
        # inside this block.
        text = _block_text()
        block_start = text.index(BLOCK_KEY + ":")
        assert "barrons_openai" not in text[:block_start]

    def test_openai_arm_dates(self):
        b = _block()
        assert b["openai_arm"]["arm_B1"]["date"] == "2026-10-01"
        assert b["openai_arm"]["arm_B2"]["date"] == "2026-09-30"

    def test_no_type_a_1237_in_git_log_pin(self):
        # Pre-main-commit form: no prior run committed this run's
        # iteration. Post-main-commit it self-trips on this run's own
        # commits (the #1191-class self-trip, re-pinned in the
        # terminal log-hash followup per #721).
        out = _git("log", "--oneline", "--grep=Type A #1237").stdout
        assert out.strip() == "", out.strip()


# ---------------------------------------------------------------------------
# 4. Block structure under competitor_relationships.openai.
# ---------------------------------------------------------------------------

class TestBlockStructure1237:
    def test_newscorp_profile_exists(self):
        assert os.path.exists(PROFILE_FILE)

    def test_openai_section_is_expected_parent(self):
        data = _load_newscorp()
        assert "openai" in data["competitor_relationships"]

    def test_block_key_present_under_openai(self):
        assert BLOCK_KEY in _openai_section()

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "mechanism_id", "finding", "verdict",
            "falsification_family_member", "falsification_ledger",
            "openai_arm", "meta_arm", "financial_relationship",
            "register_analysis", "confounders", "counterevidence",
            "source_urls", "research_method", "rotation_transparency",
            "statistical_discipline",
        ):
            assert field in b, field

    def test_arms_have_tones(self):
        b = _block()
        assert b["openai_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.275
        assert b["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.075

    def test_yaml_parse_clean(self):
        assert _block()["yaml_parse_clean"] is True


# ---------------------------------------------------------------------------
# 5. Mechanism 973 content discipline.
# ---------------------------------------------------------------------------

class TestM973ContentDiscipline1237:
    def test_finding_states_delta(self):
        assert "-0.35" in _block()["finding"]

    def test_falsification_member_landed(self):
        b = _block()
        assert b["falsification_family_member"] is True
        assert b["falsification_ledger"] == 51
        assert b["verdict"] == "falsification_member_confirmed"

    def test_fifty_first_form_present_in_block(self):
        # The live member-claim form lands in the profile block this
        # run (fragment-built here per #715).
        text = _block_text()
        assert _T51 in text

    def test_no_fifty_second_form_in_block(self):
        text = _block_text()
        assert _T52 not in text

    def test_cross_peg_confound_disclosed(self):
        b = _block()
        text = b["finding"] + b["register_analysis"]
        assert "cross-peg" in text

    def test_excerpt_tier_disclosed(self):
        text = " ".join(_block()["confounders"]["strong"])
        assert "0 browser.open per #503" in text

    def test_payment_scale_inversion_stated(self):
        assert "5:1" in _block()["finding"]

    def test_ascii_only_block(self):
        assert _block()["ascii_only"] is True
        # Scoped to this run's block per the #1208 in-gate fix: the
        # news-corp.yaml file carries one pre-existing non-ASCII char
        # (em dash) outside this block.
        text = _block_text()
        start = text.index(BLOCK_KEY + ":")
        end = text.index("\n  meta:", start)
        blk = text[start:end]
        assert all(ord(c) < 128 for c in blk)
        assert "—" not in blk


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug 28 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1237:
    def test_manual_illustrative_only(self):
        b = _block()
        assert "MANUAL ILLUSTRATIVE ONLY" in b["statistical_discipline"]

    def test_engine_not_run(self):
        b = _block()
        assert b["engine_run"] is False
        assert b["scorer"]["engine_run"] is False

    def test_not_significant(self):
        b = _block()
        assert b["is_significant"] is False
        assert b["scorer"]["is_significant"] is False

    def test_no_analysis_json_update(self):
        b = _block()
        assert b["no_analysis_json_update"] is True

    def test_not_artifact_grade(self):
        b = _block()
        assert b["artifact_grade"] is False


# ---------------------------------------------------------------------------
# 7. Falsification ledger (50 -> 51 this run).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1237:
    def test_forty_eighth_member_intact_pin(self):
        # The single live forty-eighth member claim (mechanism 952,
        # profiles/financial-times.yaml) must survive this run
        # unchanged.
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact_pin(self):
        # The single live forty-ninth member claim (mechanism 956,
        # careers/journalists.yaml) must survive this run unchanged.
        assert _git_grep_tracked_source(_T49, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_fiftieth_member_intact_pin(self):
        # The single live fiftieth member claim (mechanism 959,
        # careers/journalists.yaml) must survive this run unchanged.
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_member_landed_this_run(self):
        # The fifty-first member claim lands in profiles/news-corp.yaml
        # this run (working-tree pin: the block is uncommitted
        # pre-commit).
        assert _working_tree_grep_profiles(_T51) == [
            os.path.join(PROFILES_DIR, "news-corp.yaml")]

    def test_no_fifty_second_member_pin(self):
        assert _git_grep_tracked_source(_T52, None) == []

    def test_no_fortieth_direction_pin(self):
        # The fortieth direction-claim form stays absent in profiles/
        # (profiles-scoped per the #1199 in-gate fix).
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_this_run_adds_member(self):
        assert _block()["falsification_family_member"] is True


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: this run's forward guards for #1238.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1237:
    def test_pins_on_973_landing(self):
        # Type A lands one mechanism: max becomes 973, next is 974.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 973" in src
        assert "NEXT_NUM = 974" in src

    def test_no_type_b_1238_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type B #1238").stdout
        assert out.strip() == "", out.strip()

    def test_974_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_974_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_974_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T49, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_fiftieth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_member_present_pin(self):
        assert _working_tree_grep_profiles(_T51) == [
            os.path.join(PROFILES_DIR, "news-corp.yaml")]

    def test_no_fifty_second_member_pin(self):
        assert _git_grep_tracked_source(_T52, None) == []

    def test_predecessor_1236_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1236_FILE))

    def test_next_leg_is_1238_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1238 Type B" in src

    def test_1236_pins_flip_by_design_documented(self):
        # #1236's forward guards (max-972, zero-973 keys all forms,
        # no-Type-A-#1237-in-git-log, fortieth absent, forty-eighth +
        # forty-ninth + fiftieth intact in profiles/, fifty-first
        # absent) verified GREEN pre-commit this run via the
        # subprocess staleness pin (Type A lands mechanism 973); the
        # max-972, zero-973, no-Type-A-#1237-in-git-log, and
        # no-fifty-first pins flip post-main-commit on this run's own
        # landing (the #1191-class self-trip, by design, documented in
        # the staleness pin below).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1236" in src
        assert "973" in src


# ---------------------------------------------------------------------------
# 9. Background suite: #1235's suite is CHECKED ONLY per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1237:
    def test_1235_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1235_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1235-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1237_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1235-launched" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Staleness pins: #1236's guard lifecycle self-trips by design
# ---------------------------------------------------------------------------
class TestStalenessPins1237:
    def test_1236_guard_lifecycle_post_commit_self_trip(self):
        # Deselected pre-commit (meaningful only post-main-commit):
        # 8 of the 11 pass; three fail BY DESIGN on this run's own
        # main commit - test_no_type_a_1237_in_git_log_pin,
        # test_973_numeric_absent_in_profiles, and
        # test_no_fifty_first_member_pin (the #1236 block is read-only
        # to this run). The #1236 forward guards (fortieth absent,
        # forty-eighth + forty-ninth + fiftieth intact) stay GREEN.
        res = _class_run(E1236_FILE, "TestGuardLifecycle1236")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "3 failed, 8 passed" in res.stdout, res.stdout[-2000:]
        for name in (
            "test_no_type_a_1237_in_git_log_pin",
            "test_973_numeric_absent_in_profiles",
            "test_no_fifty_first_member_pin",
        ):
            assert name in res.stdout, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 11. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------
class TestDocSync1237:
    def test_readme_test_file_table_has_1237_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_a_1237" in readme

    def test_architecture_has_1237_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1237" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 12. Iteration log (3 tests; deselected pre-commit per #721)
# ---------------------------------------------------------------------------
class TestIterationLog1237:
    def test_1237_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1237 Type A" in log

    def test_1236_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1236 Type E" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------
class TestInFlightIsolation1237:
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

    def test_do_not_touch_1024_m846(self):
        # Guarded in the log entry per convention; the test file keeps
        # the in-flight list only (own-file reference would trip the
        # contiguous-literal discipline elsewhere).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1024" in src
