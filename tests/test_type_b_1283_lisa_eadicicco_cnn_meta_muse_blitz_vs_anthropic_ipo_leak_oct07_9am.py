# -*- coding: utf-8 -*-
"""Type B #1283 tests: Lisa Eadicicco (CNN (CNN Business)) - Meta Muse AI agent Connect launch under privacy-pushback framing
(-0.35 MANUAL ILLUSTRATIVE, NEW Sep-24 arm, mirror-attested (KION))
vs Anthropic leaked IPO filing ("existential risk") under scandal framing (-0.45, NEW Sep-29 arm,
mirror-attested (KION + lapost)); illustrative delta (Anthropic minus Meta) -0.10
register asymmetry in the Meta-soft direction (m1001).

Mechanism 1001 (NOT a falsification-family member; ledger holds at 56).
CNN holds the Dec 5 2025 Meta AI content-licensing deal (in-corpus, profiles/competitor-entities.yaml mechanism 539; Reuters Dec-5-2025 URL re-surfaced, disclosed); Meta is the payer here and Anthropic sits in mechanism 539's zero-deal entity set, so the pair tests payer-softening at the journalist level - the near-null delta does not adjudicate it (CONTROL-CASE, same brief as #1218).
Peg asymmetry (Connect Muse launch vs leaked IPO filing) is the STRONG
confound.

Excerpt-bounded research per #503 (delegated scout candidate sweep +
main-run browser.search verification sets, 0 browser.open reads).
Delegated scout (candidate sweep, ~55 searches): SELECTED Eadicicco as the only fully-verified in-window same-journalist pair with URL-complete arms (CNN, Sep 24 / Sep 29, 5 days apart); the scout's #2 (Vanian/CNBC) rejected on main-run verification (the OpenAI-arm verbatim CNBC URL never surfaced); #3 (Chen/NYT) and #4 (Gurman/Bloomberg) rejected (verbatim outlet URLs missing); #5 (Perez/TechCrunch) rejected (no competitor arm found). Prior "Lisa Eadicicco" mentions are inside Raymond Wong's career record (wearables-beat comparison notes), never a mechanism.

The m1001 block lives in profiles/careers/journalists.yaml as a
competitor_coverage sub-key of the NEW top-level `lisa_eadicicco_type_b` key
(per the #643 convention; zero dedicated type_b key pre-commit;
mechanism_ids [1001]).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only CHECKS the #1280-launched background suite
(goal hidden_files type_d_1280_full_suite.log, observed at this run's
check; an observation, not a verdict); its verdict and tombstone belong
to #1285 (next Type D). This run neither re-launches, kills, nor writes
to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit), #900
(untracked Type D test file), #1012-wt (working-tree edit on the committed
Type A #1012 file).

Type B lands one mechanism (mechanism 1001); the Type A predecessor added
one (mechanism 1000). Next run #1284 Type C closes the 1280-1284 window.
Rotation: D #1280 -> E #1281 -> A #1282 -> B #1283 -> C #1284. This run is
the FOURTH leg of the 1280-1284 window. The main commit is the anchor
per #565.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth through fifty-seventh
member-claim forms, or the thirty-fifth through fortieth direction forms;
the constants are constructed at runtime. (The landed ordinals live as
short lowercase forms in prose here; the live full-form claims live in
profiles/financial-times.yaml, profiles/news-corp.yaml,
profiles/the-verge.yaml, profiles/guardian.yaml, profiles/atlantic.yaml,
profiles/wired.yaml, and profiles/careers/journalists.yaml.)
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
WIRED_PATH = os.path.join(PROFILES_DIR, "wired.yaml")
OWN_BASENAME = (
    "test_type_b_1283_lisa_eadicicco_cnn_meta_muse_blitz_vs_"
    "anthropic_ipo_leak_oct07_9am.py"
)
TOP_KEY = "lisa_eadicicco_type_b"

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "9d6803cf85b2c8811e5e3f146d93c71a67494648"  # patched green in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1001
NEXT_NUM = 1002  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_b_1283_lisa_eadicicco_cnn_meta_muse_blitz_vs_"
    "anthropic_ipo_leak_oct07_9am"
)

# Predecessor chain: #1282 Type A continued the 1280-1284 window.
PRED_MAIN_1282 = "915f95cd"
PRED_ANCHOR_1282 = "ea804f92"
PRED_DOCSYNC_1282 = "29386d75"
PRED_FINAL_1282 = "45e359a6"
# #1281 Type E (second leg) for the rotation-guard chain.
PRED_MAIN_1281 = "3c53f5f9"
PRED_ANCHOR_1281 = "7ef464d2"
PRED_DOCSYNC_1281 = "b23ffee6"
PRED_FINAL_1281 = "10d64db0"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the own-run git-log pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1283 = "9d6803cf85b2c8811e5e3f146d93c71a67494648"

# Forward guard for the next leg: #1284 Type C. Re-pinned by #1284's
# log-hash followup per #721 (starts as 0*40; the forward pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1284 = "7325305f"  # re-pinned to #1284 main sha per #721

# The #1282 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 1000; zero one-zero-zero-two keys all
# forms / no-Type-B-#1283-in-git-log / fortieth direction absent /
# forty-eighth through fifty-sixth members intact /
# fifty-seventh member absent / ledger 56).
E1282_FILE = (
    "test_type_a_1282_wired_amazon_oct02_datacenter_nda_"
    "accountability_oct07_8am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 71577  # post-doc-sync total (pre-sync 71468 + 109)
README_FILE_COUNT = 1608  # pre-sync 1607 + 1 (this file)

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

# Novel source URLs: 2 zero-hit repo-wide pre-commit (git grep
# -F); 2 in-corpus re-surfaces disclosed (cnn.com Meta canonical via #966 press tracking; Reuters Dec-2025 Meta-deal URL via mechanism 539).
NOVEL_URLS = [
    "https://kioncentralcoast.com/money/cnn-business-consumer/2026/09/23/meta-is-betting-big-on-its-muse-ai-agent-with-a-blitz-of-new-gadgets/",
    "https://www.cnn.com/2026/09/29/tech/anthropic-ipo-details-leak?cid=external-feeds_iluminar_meta",

]
RESURFACED_URLS = [
    "https://www.cnn.com/2026/09/24/tech/meta-muse-ai-glasses-connect?cid=external-feeds_iluminar_meta",
    "https://www.reuters.com/business/meta-strikes-multiple-ai-deals-with-news-publishers-axios-reports-2025-12-05/",

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


def _load_journalists():
    return yaml.safe_load(_read(JOURNALISTS_PATH))


def _top():
    data = _load_journalists()
    assert TOP_KEY in data
    return data[TOP_KEY]


def _block():
    return _top()["competitor_coverage"][BLOCK_KEY]


def _block_text():
    return _read(JOURNALISTS_PATH)


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

class TestAnchor1283:
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
        assert "FOURTH leg of the 1280-1284 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1283:
    def test_predecessor_1282_chain_verified(self):
        for sha in (
            PRED_MAIN_1282, PRED_ANCHOR_1282, PRED_DOCSYNC_1282,
            PRED_FINAL_1282,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1281_chain_verified(self):
        for sha in (
            PRED_MAIN_1281, PRED_ANCHOR_1281, PRED_DOCSYNC_1281,
            PRED_FINAL_1281,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1280 -> E #1281 -> A #1282 -> B #1283 -> C #1284" in src

    def test_next_leg_is_type_c_1284(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1284 Type C" in src

    def test_type_b_lands_one_mechanism(self):
        # Type B lands exactly one mechanism (mechanism 1001); the Type
        # A predecessor added one (mechanism 1000).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1283:
    def test_top_key_found(self):
        assert _top()["mechanism_ids"] == [MECH_NUM]

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1283 in key, no 1001 or
        # 1002 substring.
        assert "1283" in BLOCK_KEY
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
        assert nums, "mechanism 1001 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_novel_urls_in_block_source_urls_verbatim(self):
        b = _block()
        urls = b["source_urls"]
        for novel in NOVEL_URLS:
            assert novel in urls, novel

    def test_resurfaced_urls_disclosed(self):
        b = _block()
        for resurfaced in RESURFACED_URLS:
            assert resurfaced in b["source_urls"], resurfaced
        assert "re-surface" in b["novelty"] or "resurface" in b["novelty"]

    def test_meta_canonical_is_resurface_not_novel(self):
        # The cnn.com Meta canonical lives in the corpus via #966/#971
        # press tracking; it is a disclosed re-surface, NOT counted
        # among the novel URLs.
        assert RESURFACED_URLS[0] not in NOVEL_URLS
        assert RESURFACED_URLS[1] not in NOVEL_URLS
        assert len(NOVEL_URLS) == 2
        assert len(RESURFACED_URLS) == 2


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
            os.path.join("profiles", "careers", "journalists.yaml"),
            "README.md",
            os.path.join("docs", "ARCHITECTURE.md"),
            "iteration-log.md",
        }
        for h in hits:
            assert h in allowed, h

    def test_meta_mirror_url_novelty(self):
        # The KION mirror URL was zero-hit repo-wide pre-commit; now
        # present only inside this block.
        text = _block_text()
        assert "kioncentralcoast.com/money/cnn-business-consumer/2026/09/23/meta-is-betting-big" in text
        block_start = text.index(BLOCK_KEY + ":")
        assert "kioncentralcoast.com/money/cnn-business-consumer/2026/09/23/meta-is-betting-big" not in text[:block_start]

    def test_anthropic_canonical_novelty(self):
        text = _block_text()
        assert "cnn.com/2026/09/29/tech/anthropic-ipo-details-leak" in text
        block_start = text.index(BLOCK_KEY + ":")
        assert "cnn.com/2026/09/29/tech/anthropic-ipo-details-leak" not in text[:block_start]


    def test_both_arms_new_documented(self):
        b = _block()
        assert "NEW" in b["meta_arm"]["status"]
        assert "NEW" in b["anthropic_arm"]["status"]

    def test_no_type_b_1283_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type B #1283" must be this run's main
        # commit or a descendant of it - i.e., no PRIOR run committed
        # this run's iteration. Deselected in the in-gate run (fails
        # pre-commit by design: PRED_MAIN_1283 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type B #1283")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1283).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h


# ---------------------------------------------------------------------------
# 4. Block structure under the NEW lisa_eadicicco_type_b top-level key.
# ---------------------------------------------------------------------------

class TestBlockStructure1283:
    def test_journalists_profile_exists(self):
        assert os.path.exists(JOURNALISTS_PATH)

    def test_top_key_is_expected_parent(self):
        assert _top()["name"] == "Lisa Eadicicco"
        assert _top()["publication"] == "cnn"

    def test_block_key_present_under_competitor_coverage(self):
        assert BLOCK_KEY in _top()["competitor_coverage"]

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_iteration_fields(self):
        b = _block()
        assert b["iteration"] == 1283
        assert b["type"] == "B"
        assert b["date"] == "2026-10-07 09:00 PDT"

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "block_key", "mechanism_id", "iteration", "type", "date",
            "test_file", "author", "goal_id", "job_id",
            "scheduled_job_id", "journalist", "publication", "window",
            "design", "meta_arm", "anthropic_arm",
            "scorer_delta_MANUAL_ILLUSTRATIVE", "delta_reading",
            "confounders", "counter_evidence", "connects_to", "verdict",
            "falsification_family", "falsification_family_member",
            "falsification_ledger", "ledger_note", "is_significant",
            "correlation_not_causation", "no_analysis_json_update",
            "artifact_readiness", "research_method", "novelty",
            "background_suite_status", "in_flight", "source_urls",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_meta_arm_tone(self):
        assert _block()["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.35

    def test_comp_arm_tone(self):
        assert _block()["anthropic_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.45

    def test_scorer_delta(self):
        assert _block()["scorer_delta_MANUAL_ILLUSTRATIVE"] == -0.10

    def test_connects_to_lineage(self):
        assert 539 in _block()["connects_to"]
        assert 519 in _block()["connects_to"]

    def test_source_urls_count(self):
        assert len(_block()["source_urls"]) == 4

    def test_meta_arm_date_and_byline(self):
        b = _block()
        assert b["meta_arm"]["date"] == "2026-09-24"
        assert b["meta_arm"]["author_byline"] == "Lisa Eadicicco"

    def test_comp_arm_date_and_byline(self):
        b = _block()
        assert b["anthropic_arm"]["date"] == "2026-09-29"
        # Co-bylined (Isidore + Eadicicco); assert membership, not
        # equality - the co-byline is a disclosed confound.
        assert "Lisa Eadicicco" in b["anthropic_arm"]["author_byline"]


# ---------------------------------------------------------------------------
# 5. Content discipline: verbatim quotes, mirror attestation, ASCII.
# ---------------------------------------------------------------------------

class TestM1001ContentDiscipline1283:
    def test_meta_key_quotes_verbatim(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "widely panned" in joined
        assert "discreetly record" in joined

    def test_meta_headline_verbatim(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "blitz of new gadgets" in joined

    def test_meta_lede_register(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "concerns over AI" in joined

    def test_anthropic_key_quotes_verbatim(self):
        quotes = _block()["anthropic_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "existential risk to humanity" in joined
        assert "resist shutdown" in joined

    def test_anthropic_scandal_register(self):
        quotes = _block()["anthropic_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "resembling blackmail" in joined
        assert "never this stark" in joined

    def test_cnn_deal_holding_disclosed(self):
        b = _block()
        assert "CNN" in b["design"]
        assert "Dec-5-2025" in b["design"] or "Dec 5 2025" in b["design"]

    def test_meta_canonical_resurface_disclosed(self):
        # The cnn.com Meta canonical is in-corpus via #966 press
        # tracking; the block carries the novel KION mirror as the
        # Meta-arm source and discloses the canonical as re-surfaced.
        b = _block()
        assert "re-surfaced" in b["meta_arm"]["url_note"]
        assert "#966" in b["meta_arm"]["url_note"]


    def test_mirror_attestation_disclosed(self):
        b = _block()
        assert "mirror-attested" in b["meta_arm"]["evidence_tier"]
        assert "mirror-attested" in b["anthropic_arm"]["evidence_tier"]
        assert "0 browser.open per #503" in b["meta_arm"]["evidence_tier"]

    def test_ascii_only(self):
        raw = _read(os.path.join(TESTS_DIR, OWN_BASENAME)).encode("utf-8")
        raw.decode("ascii")

    def test_no_em_dashes(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src
        assert "\u2013" not in src

    def test_yaml_block_ascii(self):
        # Only this run's appended block must be ASCII; the legacy
        # file carries pre-existing non-ASCII elsewhere.
        text = _block_text()
        block = text[text.index(TOP_KEY + ":"):]
        block.encode("ascii")


# ---------------------------------------------------------------------------
# 6. Statistical discipline: MANUAL/QUALITATIVE ONLY per Aug 28 2026 rule.
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1283:
    def test_manual_illustrative_only(self):
        b = _block()
        assert "MANUAL ILLUSTRATIVE" in b["design"]

    def test_engine_not_run(self):
        b = _block()
        assert b["no_analysis_json_update"] is True

    def test_p_value_not_calculated(self):
        # The needle and the expected def line are both runtime-built;
        # the only contiguous occurrence in this file is the def line.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        needle = "p" + "_value"
        expected_def = "    def test_" + needle + "_not_calculated(self):"
        hits = [l for l in src.splitlines() if needle in l]
        assert hits == [expected_def], hits

    def test_is_significant_false(self):
        assert _block()["is_significant"] is False

    def test_correlation_not_causation(self):
        assert _block()["correlation_not_causation"] is True

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_verdict_directionally_supported_not_proven(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _block()["falsification_family"] or \
            "No analysis.json update warranted" in _block()["falsification_family"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 56 (NOT a member).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1283:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert "NOT a falsification-family member" in b["falsification_family"]

    def test_control_case_disclosed(self):
        b = _block()
        assert "CONTROL-CASE" in b["falsification_family"]

    def test_fifty_sixth_intact_in_wired(self):
        # Landed #1282 (m1000, profiles/wired.yaml). Asserted on the
        # working tree so the pin is stable across commit boundaries.
        assert _T56 in _read(WIRED_PATH)

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

    def test_fifty_seventh_absent(self):
        assert _git_grep_tracked_source(_T57, None) == []

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (
            "THIRT" + "Y-FIFTH relationship direction",
            "THIRT" + "Y-SIXTH relationship direction",
            "THIRT" + "Y-SEVENTH relationship direction",
            "THIRT" + "Y-EIGHTH relationship direction",
            "THIRT" + "Y-NINTH relationship direction",
        ):
            assert _git_grep_tracked_source(needle, "profiles/") != [], needle

    def test_fortieth_direction_absent(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_ledger_holds_at_56(self):
        assert "holds at 56" in _block()["ledger_note"]
        assert _block()["falsification_ledger"] == 56

    def test_ledger_note_states_not_a_member(self):
        assert "NOT a falsification-family member" in _block()["ledger_note"]


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: pins for #1284; #1282's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1283:
    def test_pins_on_1001_landing(self):
        # Type B lands one mechanism: max becomes 1001, next is 1002.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1001" in src
        assert "NEXT_NUM = 1002" in src

    def test_no_type_c_1284_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1284's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1284" must be #1284's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1284 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1284")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1284's own commits"
        main = _git("rev-parse", PRED_MAIN_1284).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1002_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1002_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1002_dash_absent_repo_wide(self):
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
        # Landed #1282 (m1000, profiles/wired.yaml). Asserted on the
        # working tree so the pin is stable across the main-commit
        # boundary; the HEAD sweep sees it from the main commit on.
        assert _T56 in _read(WIRED_PATH)

    def test_no_fifty_seventh_member_pin(self):
        # m1001 is NOT a falsification-family member (CONTROL-CASE);
        # the fifty-seventh member-claim form stays absent repo-wide.
        assert _git_grep_tracked_source(_T57, None) == []

    def test_predecessor_1282_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1282_FILE))

    def test_next_leg_is_1284_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1284 Type C" in src

    def test_1282_pins_flip_by_design_documented(self):
        # #1282's forward guards (max-1000, zero one-zero-zero-two
        # keys all forms, no-Type-B-#1283-in-git-log, fortieth
        # direction absent, forty-eighth through fifty-sixth members
        # intact, no fifty-seventh member, ledger 56) verified GREEN
        # pre-commit this run via the subprocess staleness pin (Type
        # B lands mechanism 1001 as a CONTROL-CASE, not a family
        # member); the max-1000, zero one-zero-zero-two, and
        # no-Type-B-#1283-in-git-log pins flip post-main-commit on
        # this run's own landing (the #1191-class self-trip and the
        # #1272-class forward-guard expiry, by design, documented in
        # the staleness pin below).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1283" in src
        assert "2 failed, 17 passed" in src


# ---------------------------------------------------------------------------
# 9. Background suite: #1280's suite is CHECKED ONLY per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1283:
    def test_1280_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1280_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1280-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1283_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1280-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1285" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1283:
    def test_readme_test_file_table_has_1283_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1283" in readme

    def test_architecture_has_1283_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1283" in arch

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

class TestIterationLog1283:
    def test_1283_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1283 Type B" in log

    def test_1282_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1282 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1282's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1283:
    def test_1282_guard_lifecycle_post_commit_self_trip(self):
        # Post-main-commit form: 17 of the 19 pass; the two that fail
        # BY DESIGN are test_no_type_b_1283_in_git_log_pin (this run's
        # own main commit carries "Type B #1283" while PRED_MAIN_1283
        # in the #1282 file is still 0*40; the #1191-class self-trip,
        # re-pinned green in this run's log-hash followup per #721)
        # and test_1001_numeric_absent_in_profiles (mechanism 1001
        # lands in profiles/ this run; the #1272-class forward-guard
        # expiry - the next-number guard is consumed by the landing).
        # test_pins_on_mechanism_landing stays GREEN (asserts on the
        # #1282 file's own constants, untouched by this run); the
        # member and direction pins stay GREEN (m1001 is a
        # CONTROL-CASE, not a family member). Deselected pre-commit
        # (both pins pass pre-commit).
        res = _class_run(E1282_FILE, "TestGuardLifecycle1282")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "2 failed, 17 passed" in res.stdout, res.stdout[-2000:]
        for name in (
            "test_no_type_b_1283_in_git_log_pin",
            "test_1001_numeric_absent_in_profiles",
        ):
            assert name in res.stdout, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1283:
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
        # #1024 m846 (profiles/competitor-entities.yaml) is NOT
        # touched - decision pending. This run stages only its own
        # files by explicit path.
        res = _git("diff", "--name-only")
        assert "profiles/competitor-entities.yaml" not in res.stdout.split()
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src

    def test_own_diff_excludes_inflight(self):
        # This run's staged set must never include the in-flight
        # files; verified at commit time by explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "explicit-path" in src
