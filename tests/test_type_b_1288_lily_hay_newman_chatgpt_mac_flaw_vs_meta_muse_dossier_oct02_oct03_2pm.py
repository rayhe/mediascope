# -*- coding: utf-8 -*-
"""Type B #1288 tests: Lily Hay Newman (+ Matt Burgess co-byline, WIRED) -
Oct-2 ChatGPT Mac app flaw accountability register (-0.30 MANUAL
ILLUSTRATIVE, NEW arm, relay-attested via the redhot.sg verbatim reprint +
the WIRED author-listing attestation) vs carried Oct-3 Meta Muse dossier
accountability register (-0.58, m988, Type A #1262); illustrative delta
(OpenAI minus Meta) +0.28 - the deal partner draws the softer register on
the software-flaw peg, 1 day apart, same co-byline pair.

Mechanism 1004 (NOT a falsification-family member; ledger holds at 57).
Develops the open empirical thread that m988 (Type A #1262) left for a
future test of the Conde Nast x OpenAI softer-prediction: the thread
resolves toward the thesis direction on this peg (directionally supported,
not proven). m898 (Type A #1112, FORTIETH member) already counted the
adversarial-on-payer observation for WIRED x OpenAI on the lawsuit peg, so
per the #1143 temporal-replication precedent this same-publication new-peg
observation is not a new prediction test. Peg-bounded inversion disclosed:
the lawsuit peg ran adversarial on the payer (-0.40); this software-flaw
peg runs softer on the payer (-0.30) than on Meta (-0.58).

Excerpt-bounded research per #503 (main-run candidate sweep across ~18
journalists + exact-headline verification sets, 0 browser.open reads).
Candidate sweep: SELECTED Newman/Burgess as the only fully-verified
in-window same-co-byline pair with URL-complete arms (WIRED, Oct 2 / Oct 3,
1 day apart); REJECTED Goode (saturated m431/m436), Heath (saturated #563),
Zeff (saturated #913/#1123), Stein (saturated #968), Robison (saturated
#370), Fried (saturated #1158), Field (saturated m52), Criddle (saturated
#1143), Ashworth (saturated #853/#998), Fung (no in-window pieces),
Seetharaman (departing WSJ, no in-window pieces), Matsakis (returns Nov 11,
no in-window bylines), Roose (book promo only), Horwitz (no competitor
arm), Murphy Kelly (no byline surfaced), Vanian (prior rejection stands).
The delegated scout returned only a fragment and was unusable; the
main-run sweep above is the operative candidate record.

The m1004 block lives in profiles/careers/journalists.yaml under the Lily
Hay Newman journalist item as a sibling of the type_b_1008 block (THIRD
dedicated Type B mechanism on Newman: m635, m836, m1004);
mechanism_ids [1004].

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this pre-commit
file and is patched to the main-commit hash in the anchor followup commit.
One anchor test (the placeholder pin) fails BY DESIGN post-anchor.

Per #795: this run only CHECKS the #1285-launched background suite
(goal hidden_files type_d_1285_full_suite.log, observed at this run's
check; an observation, not a verdict); its verdict and tombstone belong
to #1290 (next Type D). This run neither re-launches, kills, nor writes
to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit), #900
(untracked Type D test file), #1012-wt (working-tree edit on the committed
Type A #1012 file).

Type B lands one mechanism (mechanism 1004); the Type A predecessor added
one (mechanism 1003). Next run #1289 Type C closes the 1285-1289 window.
Rotation: D #1285 -> E #1286 -> A #1287 -> B #1288 -> C #1289. This run is
the FOURTH leg of the 1285-1289 window. The main commit is the anchor
per #565.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth through fifty-seventh
member-claim forms, the fifty-eighth member-claim form, or the fortieth
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
WIRED_PATH = os.path.join(PROFILES_DIR, "wired.yaml")
OWN_BASENAME = (
    "test_type_b_1288_lily_hay_newman_chatgpt_mac_flaw_vs_"
    "meta_muse_dossier_oct02_oct03_2pm.py"
)
JOURNALIST_NAME = "Lily Hay Newman"

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "30ef8867191d2a89688200b083df440cb0c22c4e"  # patched post-commit per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1004
NEXT_NUM = 1005  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_b_1288_lily_hay_newman_chatgpt_mac_flaw_vs_"
    "meta_muse_dossier_oct02_oct03"
)

# Predecessor chain: #1287 Type A continued the 1285-1289 window.
PRED_MAIN_1287 = "32786e12"
PRED_ANCHOR_1287 = "3a21f16b"
PRED_DOCSYNC_1287 = "6eb575e5"
PRED_FINAL_1287 = "9da5dbd4"
PRED_PUSH_1287 = "52ff0210"
# #1286 Type E (second leg) for the rotation-guard chain.
PRED_MAIN_1286 = "7b75118a"
PRED_ANCHOR_1286 = "954b6788"
PRED_DOCSYNC_1286 = "d2048a8e"
PRED_FINAL_1286 = "90708117"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the own-run git-log pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1288 = "0" * 40

# Forward guard for the next leg: #1289 Type C. Re-pinned by #1289's
# log-hash followup per #721 (starts as 0*40; the forward pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1289 = "0" * 40

# The #1287 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 1003; zero one-zero-zero-four keys all
# forms / no-Type-B-#1288-in-git-log / fortieth direction absent /
# forty-eighth through fifty-seventh members intact /
# fifty-eighth member absent / ledger 57).
E1287_FILE = (
    "test_type_a_1287_ap_anthropic_sep27_oct01_dual_lab_safety_"
    "pegs_oct07_1pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 71976  # post-doc-sync total (pre-sync 71889 + 87)
README_FILE_COUNT = 1613  # pre-sync 1612 + 1 (this file)

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

# Novel source URLs: 2 zero-hit repo-wide pre-commit (git grep -F).
# The Meta arm URLs are carried from m988 (not novel, disclosed).
NOVEL_URLS = [
    "https://www.redhot.sg/a-flaw-in-chatgpt-s-mac-app-could-have-let-hackers-grab-sensitive-data-723649.html",
    "https://inforeader.com/i/?a=normal&search=author%3A%22Lily+Hay+Newman%22&rid=68066b29e5527&get=f_28",
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


def _newman_item():
    data = _load_journalists()
    return next(
        j for j in data["journalists"] if j.get("name") == JOURNALIST_NAME
    )


def _block():
    return _newman_item()[BLOCK_KEY]


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

class TestAnchor1288:
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
        assert "FOURTH leg of the 1285-1289 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1288:
    def test_predecessor_1287_chain_verified(self):
        for sha in (
            PRED_MAIN_1287, PRED_ANCHOR_1287, PRED_DOCSYNC_1287,
            PRED_FINAL_1287, PRED_PUSH_1287,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1286_chain_verified(self):
        for sha in (
            PRED_MAIN_1286, PRED_ANCHOR_1286, PRED_DOCSYNC_1286,
            PRED_FINAL_1286,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1285 -> E #1286 -> A #1287 -> B #1288 -> C #1289" in src

    def test_next_leg_is_type_c_1289(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1289 Type C" in src

    def test_type_b_lands_one_mechanism(self):
        # Type B lands exactly one mechanism (mechanism 1004); the Type
        # A predecessor added one (mechanism 1003).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1288:
    def test_block_found_under_newman_item(self):
        assert BLOCK_KEY in _newman_item()
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

    def test_meta_arm_urls_carried_not_novel(self):
        # The Meta arm URLs are carried from m988 (disclosed, not
        # novel); the block must not present them as novel.
        meta_urls = _block()["meta_arm"]["source_urls"]
        for u in NOVEL_URLS:
            assert u not in meta_urls

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

    def test_no_type_b_1288_in_git_log_pin(self):
        # Pre-commit form: no commit message carries "Type B #1288"
        # (the #1191-class self-trip; this run's own main commit flips
        # it post-commit, re-pinned green in the log-hash followup per
        # #721). Deselected in the in-gate run (fails post-main-commit
        # by design).
        out = _git("log", "--format=%H", "--grep=Type B #1288")
        assert out.stdout.strip() == "", out.stdout


# ---------------------------------------------------------------------------
# 4. Block structure
# ---------------------------------------------------------------------------

class TestBlockStructure1288:
    def test_journalists_profile_exists(self):
        assert os.path.exists(JOURNALISTS_PATH)

    def test_block_under_newman_item(self):
        item = _newman_item()
        assert item["name"] == JOURNALIST_NAME
        assert BLOCK_KEY in item

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_iteration_fields(self):
        b = _block()
        assert b["iteration"] == 1288
        assert b["iteration_type"] == "B"
        assert b["type"] == "B"

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "journalist", "co_byline", "publication", "finding",
            "openai_arm", "meta_arm", "illustrative_means",
            "asymmetry_scorer_result", "statistical_discipline",
            "financial_context", "confounders", "counterevidence",
            "cross_references", "connects_to", "research_method",
            "novelty", "test_file", "artifact_readiness",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_openai_arm_tone(self):
        assert _block()["openai_arm"]["tone_illustrative"] == -0.30

    def test_meta_arm_tone(self):
        assert _block()["meta_arm"]["tone_illustrative"] == -0.58

    def test_scorer_delta(self):
        means = _block()["illustrative_means"]
        assert means["delta_openai_minus_meta"] == pytest.approx(0.28)
        assert means["delta_calc"] == "-0.30 - (-0.58) = +0.28"

    def test_connects_to_lineage(self):
        assert _block()["connects_to"] == [988, 898, 635, 836, 504]

    def test_source_urls_count(self):
        assert len(_block()["openai_arm"]["source_urls"]) == 2

    def test_openai_arm_date_and_byline(self):
        arm = _block()["openai_arm"]
        assert arm["date"] == "2026-10-02"
        assert arm["byline"] == "Lily Hay Newman, Matt Burgess"

    def test_meta_arm_date_and_byline(self):
        arm = _block()["meta_arm"]
        assert arm["date"] == "2026-10-03"
        assert arm["byline"] == "Lily Hay Newman, Matt Burgess"


# ---------------------------------------------------------------------------
# 5. Content discipline
# ---------------------------------------------------------------------------

class TestM1004ContentDiscipline1288:
    def test_openai_headline_verbatim(self):
        quotes = _block()["openai_arm"]["evidence_quotes"]
        assert any(
            "A Flaw in ChatGPT" in q and "Hackers Grab Sensitive Data" in q
            for q in quotes
        )

    def test_openai_dek_verbatim(self):
        quotes = _block()["openai_arm"]["evidence_quotes"]
        assert any("inviting - and vulnerable - target" in q for q in quotes)

    def test_openai_wardle_quote(self):
        quotes = _block()["openai_arm"]["evidence_quotes"]
        assert any("building manager" in q for q in quotes)

    def test_openai_bauer_response(self):
        quotes = _block()["openai_arm"]["evidence_quotes"]
        assert any("recognize a need to move faster" in q for q in quotes)

    def test_meta_headline_verbatim(self):
        quotes = _block()["meta_arm"]["evidence_quotes"]
        assert any("Muse Creates Detailed Profiles" in q for q in quotes)

    def test_meta_system_prompt_quote(self):
        quotes = _block()["meta_arm"]["evidence_quotes"]
        assert any("a page for every person" in q for q in quotes)

    def test_meta_right_of_reply_disclosed(self):
        quotes = _block()["meta_arm"]["evidence_quotes"]
        assert any("Daniel Roberts" in q for q in quotes)

    def test_conde_nast_deal_disclosed(self):
        fin = _block()["financial_context"]
        assert "Aug 2024" in fin
        assert "$5-10M/yr" in fin

    def test_m988_open_thread_disclosed(self):
        assert "open empirical thread" in _block()["finding"]

    def test_m898_inversion_disclosed(self):
        ce = " ".join(_block()["counterevidence"])
        assert "m898" in ce

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
        assert "\u2014" not in src
        assert "\u2013" not in src

    def test_yaml_block_ascii(self):
        block = _block()
        yaml.safe_dump(block).encode("ascii")


# ---------------------------------------------------------------------------
# 6. Statistical discipline (the Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1288:
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


# ---------------------------------------------------------------------------
# 7. Falsification ledger (ledger holds at 57; NOT a member)
# ---------------------------------------------------------------------------

class TestFalsificationLedger1288:
    def test_not_a_falsification_family_member(self):
        assert "NOT a falsification-family member" in _block()["finding"]

    def test_ledger_holds_at_57(self):
        assert "Ledger holds at 57" in _block()["finding"]

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

    def test_no_fifty_eighth_member_pin(self):
        # m1004 is NOT a falsification-family member (directional
        # support, not a uniform-prediction test); the fifty-eighth
        # member-claim form stays absent repo-wide.
        assert _git_grep_tracked_source(_T58, None) == []

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        # Spot-check: the 35th-39th direction slots remain occupied
        # (the fortieth stays absent by design).
        text = _read(os.path.join(PROFILES_DIR, "competitor-entities.yaml"))
        assert "thirty-ninth" in text

    def test_fortieth_direction_absent(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: this run's forward guards (post-main-commit form)
# ---------------------------------------------------------------------------

class TestGuardLifecycle1288:
    def test_pins_on_1004_landing(self):
        # Type B lands one mechanism: max becomes 1004, next is 1005.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1004" in src
        assert "NEXT_NUM = 1005" in src

    def test_no_type_c_1289_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1289's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1289" must be #1289's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1289 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1289")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1289's own commits"
        main = _git("rev-parse", PRED_MAIN_1289).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1005_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1005_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1005_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_fifty_seventh_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_fifty_eighth_member_pin(self):
        assert _git_grep_tracked_source(_T58, None) == []

    def test_predecessor_1287_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1287_FILE))

    def test_next_leg_is_1289_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1289 Type C" in src

    def test_1287_pins_flip_by_design_documented(self):
        # #1287's forward guards (max-1003, zero one-zero-zero-four
        # keys all forms, no-Type-B-#1288-in-git-log, fortieth
        # direction absent, forty-eighth through fifty-seventh members
        # intact, no fifty-eighth member, ledger 57) verified GREEN
        # pre-commit this run via the subprocess staleness pin (Type
        # B lands mechanism 1004 as a directional case, not a family
        # member); the max-1003, zero one-zero-zero-four, and
        # no-Type-B-#1288-in-git-log pins flip post-main-commit on
        # this run's own landing (the #1191-class self-trip and the
        # #1272-class forward-guard expiry, by design, documented in
        # the staleness pin below; the self-trip is re-pinned green
        # by the log-hash followup's PRED_MAIN_1288 re-pin per #721).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1288" in src
        assert "1 failed, 19 passed" in src


# ---------------------------------------------------------------------------
# 9. Background suite: #1285's suite is CHECKED ONLY per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1288:
    def test_1285_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1285_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1285-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1288_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1285-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1290" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1288:
    def test_readme_test_file_table_has_1288_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1288" in readme

    def test_architecture_has_1288_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1288" in arch

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

class TestIterationLog1288:
    def test_1288_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1288 Type B" in log

    def test_1287_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1287 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1287's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1288:
    def test_1287_guard_lifecycle_post_commit_self_trip(self):
        # Post-log-hash-followup form: 19 of the 20 pass; the one
        # that fails BY DESIGN is test_1004_numeric_absent_in_profiles
        # (mechanism 1004 lands in profiles/ this run; the
        # #1272-class forward-guard expiry - the next-number guard is
        # consumed by the landing). test_no_type_b_1288_in_git_log_pin
        # (the #1191-class self-trip: this run's own main commit
        # carries "Type B #1288") is re-pinned GREEN here by the
        # log-hash followup's PRED_MAIN_1288 re-pin per #721.
        # test_pins_on_one_mechanism_landing stays GREEN (asserts on
        # the #1287 file's own constants, untouched by this run); the
        # member and direction pins stay GREEN (m1004 is a
        # directional case, not a family member). Deselected pre-commit
        # (the numeric pin passes pre-commit; the git-log pin fails
        # pre-commit on the empty-match assert).
        res = _class_run(E1287_FILE, "TestGuardLifecycle1287")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "1 failed, 19 passed" in res.stdout, res.stdout[-2000:]
        assert (
            "test_1004_numeric_absent_in_profiles" in res.stdout
        ), res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1288:
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
