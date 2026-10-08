# -*- coding: utf-8 -*-
"""Type B #1293 tests: Sarah Perez (TechCrunch) - Sep-30 Muse
privacy-dispute accountability register (-0.35 MANUAL ILLUSTRATIVE, NEW
Meta arm, excerpt-attested via the TechCrunch author-listing mirror)
vs Oct-1 ChatGPT shopping-features launch relay (+0.05 MANUAL
ILLUSTRATIVE, NEW OpenAI arm, excerpt-attested via the WeSearch
verbatim mirror); illustrative delta (OpenAI minus Meta) +0.40 - same
writer, same outlet, 1 day apart.

Mechanism 1007 (NOT a falsification-family member; ledger holds at 58).
THIRD dedicated Type B mechanism on Sarah Perez (first: m617, Type B
#638; second: m698, Type B #778). Replicates m698's writer-level
asymmetry direction (Meta -0.45 vs OpenAI +0.45 there; Meta -0.35 vs
OpenAI +0.05 here) at a no-deal outlet: TechCrunch/Yahoo holds no
OpenAI content-licensing deal per m698's finding, so the asymmetry
persists without a financial gradient - the writer-register pattern
bounds the deal explanation rather than confirming it. Per the #1143
temporal-replication precedent this same-writer same-pair-class
observation is not a new prediction test.

Excerpt-bounded research per #503 (main-run candidate sweep across ~20
journalists + exact-headline verification sets, 0 browser.open reads).
Candidate sweep: SELECTED Perez as the only fully-verified in-window
same-writer pair with URL-complete arms (TechCrunch, Sep 30 / Oct 1, 1
day apart); REJECTED Song (saturated m593/m827), Ashworth (saturated
m853/m998), Field (saturated type_b_1178), Eadicicco (saturated #1283),
Newman/Burgess (saturated m1004/#1288), Lawler (saturated #1243),
Preston (in-flight #938), O'Brien (saturated m854/#1038), Roth
(saturated m782/m860/m953 - the Dots pair is #1203), Huamani
(saturated m959/#1213), Chokkattu (saturated m411), Sato (saturated
m215), Bordelon (Meta arms stale Apr 2026), Ortutay (no clean
competitor arm), Grantham-Philips (no clean competitor arm), Wagner
(no in-window bylines), Paul (no fresh OpenAI arm), Robertson (no
byline surfaced), Ji (no pair surfaced), Warren (Microsoft beat, no
Meta arm).

The m1007 block lives in profiles/careers/journalists.yaml under the
Sarah Perez journalist item's competitor_coverage dict as a sibling of
the type_b_638 (m617) and type_b_778 (m698) blocks; mechanism_ids
[617, 698, 1007].

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor.

Per #795: this run only CHECKS the #1290-launched background suite
(goal hidden_files type_d_1290_full_suite.log, observed at this run's
check; an observation, not a verdict); its verdict and tombstone belong
to #1295 (next Type D). This run neither re-launches, kills, nor writes
to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

Type B lands one mechanism (mechanism 1007); the Type A predecessor
added one (mechanism 1006). Next run #1294 Type C closes the 1290-1294
window. Rotation: D #1290 -> E #1291 -> A #1292 -> B #1293 -> C #1294.
This run is the FOURTH leg of the 1290-1294 window. The main commit is
the anchor per #565.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth through fifty-eighth
member-claim forms, the fifty-ninth member-claim form, or the fortieth
direction form; the constants are constructed at runtime. (The landed
ordinals live as short lowercase forms in prose here; the live full-form
claims live in profiles/financial-times.yaml, profiles/news-corp.yaml,
profiles/the-verge.yaml, profiles/guardian.yaml, profiles/atlantic.yaml,
profiles/wired.yaml, profiles/ap.yaml, and profiles/careers/journalists.yaml.)
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
JOURNALISTS_PATH = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
OWN_BASENAME = (
    "test_type_b_1293_sarah_perez_techcrunch_muse_privacy_dispute_vs_"
    "chatgpt_shopping_sep30_oct01_6pm.py"
)
JOURNALIST_NAME = "Sarah Perez"

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "5e8b08a4229694d4bb932c67727caa7842b3e4df"  # patched to main commit per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1007
NEXT_NUM = 1008  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_b_1293_sarah_perez_techcrunch_muse_privacy_dispute_vs_"
    "chatgpt_shopping_sep30_oct01"
)

# Predecessor chain: #1292 Type A continued the 1290-1294 window.
PRED_MAIN_1292 = "ddb5921f"
PRED_ANCHOR_1292 = "4420f305"
PRED_DOCSYNC_1292 = "db89a93c"
PRED_FINAL_1292 = "434fb01b"
PRED_PUSH_1292 = "7c563e89"
# #1291 Type E (second leg) for the rotation-guard chain.
PRED_MAIN_1291 = "4f33ce6a"
PRED_ANCHOR_1291 = "17773f8a"
PRED_DOCSYNC_1291 = "041cda51"
PRED_FINAL_1291 = "939e19d6"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the own-run git-log pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1293 = "5e8b08a4229694d4bb932c67727caa7842b3e4df"  # re-pinned in the terminal log-hash followup per #721

# Forward guard for the next leg: #1294 Type C. Re-pinned by #1294's
# log-hash followup per #721 (starts as 0*40; the forward pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1294 = "0" * 40

# The #1292 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 1006; zero one-zero-zero-seven keys all
# forms / no-Type-B-#1293-in-git-log / fortieth direction absent /
# forty-eighth through fifty-eighth members intact /
# fifty-ninth member absent / ledger 58).
E1292_FILE = (
    "test_type_a_1292_ft_google_oct04_oct07_regulatory_accountability_"
    "register_oct07_5pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 72322  # post-doc-sync value per #719 (55 collected)
README_FILE_COUNT = 1618  # post-doc-sync value per #719 (+1 file)

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

# Novel source URLs: 1 zero-hit repo-wide pre-commit (git grep -F).
# The Meta arm is attested via the TechCrunch author-listing mirror
# (inforeader, headline + byline + date; canonical techcrunch.com URL
# not recovered from search listings, none constructed per policy) -
# the listing URL is attestation, not a novel source URL.
NOVEL_URLS = [
    "https://wesearch.press/s/openai-launches-two-chatgpt-shopping-features-a-virtual-try-66d70d78",
]


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _perez_item():
    data = _load_journalists()
    return next(
        j for j in data["journalists"] if j.get("name") == JOURNALIST_NAME
    )


def _block():
    return _perez_item()["competitor_coverage"][BLOCK_KEY]


def _block_text():
    return _read(JOURNALISTS_PATH)


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

class TestAnchor1293:
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
        assert "FOURTH leg of the 1290-1294 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1293:
    def test_predecessor_1292_chain_verified(self):
        for sha in (
            PRED_MAIN_1292, PRED_ANCHOR_1292, PRED_DOCSYNC_1292,
            PRED_FINAL_1292, PRED_PUSH_1292,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1291_chain_verified(self):
        for sha in (
            PRED_MAIN_1291, PRED_ANCHOR_1291, PRED_DOCSYNC_1291,
            PRED_FINAL_1291,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1290 -> E #1291 -> A #1292 -> B #1293 -> C #1294" in src

    def test_next_leg_is_type_c_1294(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1294 Type C" in src

    def test_type_b_lands_one_mechanism(self):
        # Type B lands exactly one mechanism (mechanism 1007); the Type
        # A predecessor added one (mechanism 1006).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1293:
    def test_block_found_under_perez_item(self):
        assert BLOCK_KEY in _perez_item()["competitor_coverage"]
        assert _block()["mechanism_id"] == MECH_NUM

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #723/#738/#739: the iteration-form block
        # key carries no numeric/underscore/dash mechanism-id
        # substring.
        assert str(MECH_NUM) not in BLOCK_KEY

    def test_zero_underscore_mechanism_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_mechanism_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_zero_numeric_next_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_this_run(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_novel_urls_in_block_source_urls_verbatim(self):
        urls = _block()["openai_arm"]["source_urls"]
        for u in NOVEL_URLS:
            assert u in urls, u

    def test_meta_arm_attestation_not_novel_url(self):
        # The Meta arm is attested via the author-listing mirror
        # (attestation, not a novel source URL); the block must not
        # present the listing as a novel source.
        assert "source_urls" not in _block()["meta_arm"]
        assert "byline_attribution_urls" in _block()["meta_arm"]

    def test_block_key_zero_hit_except_landed(self):
        # The block key exists only in the landed profile block and in
        # this test file (which is excluded from the sweep carrier per
        # #715); no other source file carries it.
        hits = []
        for p in _iter_source_files():
            if BLOCK_KEY in open(p, encoding="utf-8",
                                 errors="replace").read():
                hits.append(p)
        assert hits == [JOURNALISTS_PATH], hits

    def test_no_type_b_1293_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type B #1293" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1293")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1293).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h


# ---------------------------------------------------------------------------
# 4. Block structure
# ---------------------------------------------------------------------------

class TestBlockStructure1293:
    def test_journalists_profile_exists(self):
        assert os.path.exists(JOURNALISTS_PATH)

    def test_block_under_perez_competitor_coverage(self):
        item = _perez_item()
        assert item["name"] == JOURNALIST_NAME
        assert BLOCK_KEY in item["competitor_coverage"]

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_iteration_fields(self):
        b = _block()
        assert b["iteration"] == 1293
        assert b["iteration_type"] == "B"
        assert b["type"] == "B"

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "journalist", "publication", "finding",
            "meta_arm", "openai_arm", "illustrative_means",
            "asymmetry_scorer_result", "statistical_discipline",
            "financial_context", "confounders", "counterevidence",
            "cross_references", "connects_to", "research_method",
            "novelty", "test_file", "artifact_readiness",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_meta_arm_tone(self):
        assert _block()["meta_arm"]["tone_score"] == -0.35

    def test_openai_arm_tone(self):
        assert _block()["openai_arm"]["tone_score"] == 0.05

    def test_scorer_delta(self):
        means = _block()["illustrative_means"]
        assert means["delta_openai_minus_meta"] == pytest.approx(0.40)
        assert means["delta_calc"] == "0.05 - (-0.35) = +0.40"

    def test_connects_to_lineage(self):
        assert _block()["connects_to"] == [698, 617, 860, 782, 953]

    def test_source_urls_count(self):
        assert len(_block()["openai_arm"]["source_urls"]) == 1

    def test_openai_arm_date_and_byline(self):
        arm = _block()["openai_arm"]
        assert arm["date"] == "2026-10-01"
        assert arm["author_byline"] == "Sarah Perez"

    def test_meta_arm_date_and_byline(self):
        arm = _block()["meta_arm"]
        assert arm["date"] == "2026-09-30"
        assert arm["author_byline"] == "Sarah Perez"

    def test_third_perez_mechanism(self):
        cc = _perez_item()["competitor_coverage"]
        assert len(cc) == 3


# ---------------------------------------------------------------------------
# 5. Content discipline
# ---------------------------------------------------------------------------

class TestM1007ContentDiscipline1293:
    def test_meta_headline_verbatim(self):
        assert "private messages without permission" in (
            _block()["meta_arm"]["title"])

    def test_meta_aten_claim_quote(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        assert any("Aten" in q and "private texts" in q for q in quotes)

    def test_meta_stone_rebuttal_quote(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        assert any("Andy Stone" in q for q in quotes)

    def test_meta_singleton_rebuttal_quote(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        assert any("David Singleton" in q for q in quotes)

    def test_openai_headline_verbatim(self):
        title = _block()["openai_arm"]["title"]
        assert "virtual try-on" in title and "Favorites" in title

    def test_m698_replication_disclosed(self):
        assert "m698" in _block()["finding"]

    def test_no_deal_context_disclosed(self):
        fin = _block()["financial_context"]
        assert "no OpenAI content-licensing deal" in fin

    def test_ascii_only(self):
        # Block-scoped (the file carries pre-existing non-ASCII in
        # other records; this block must be clean).
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


# ---------------------------------------------------------------------------
# 6. Statistical discipline (the Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1293:
    def test_manual_illustrative_only(self):
        sd = _block()["statistical_discipline"]
        assert sd["manual_illustrative_only"] is True

    def test_engine_not_run(self):
        sd = _block()["statistical_discipline"]
        assert sd["engine_run"] is False

    def test_p_value_not_calculated(self):
        sd = _block()["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        sd = _block()["statistical_discipline"]
        assert sd["cohens_d"] == "NOT_CALCULATED"

    def test_ci_95_not_calculated(self):
        sd = _block()["statistical_discipline"]
        assert sd["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        sd = _block()["statistical_discipline"]
        assert sd["is_significant"] is False

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in _block()["finding"]

    def test_no_analysis_json_update(self):
        sd = _block()["statistical_discipline"]
        assert sd["analysis_json_update"] is False

    def test_verdict_directionally_supported_not_proven(self):
        assert (
            _block()["asymmetry_scorer_result"]["verdict"]
            == "directionally_supported_not_proven"
        )

    def test_not_artifact_grade(self):
        sd = _block()["statistical_discipline"]
        assert sd["artifact_grade"] is False
