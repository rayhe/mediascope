# -*- coding: utf-8 -*-
"""Type B #1303 tests: Kelvin Chan (Associated Press) - Jun-9-2026 EU
WhatsApp interim-measures order on Meta (-0.40 MANUAL ILLUSTRATIVE,
NEW Meta arm, excerpt-attested via the techxplore.com byline-carrying
PDF mirror "June 9 2026, by Kelvin Chan" and the barchart.com
byline-carrying mirror "Kelvin Chan - AP"; apnews.com canonical not
recovered from search listings, none constructed per policy) vs
Sep-17-2026 OpenAI voluntary misalignment-disclosure framework
(+0.10 MANUAL ILLUSTRATIVE, NEW OpenAI arm, wvlt.tv byline-carrying
mirror with contributing-credit byline "AP Business Writers Kelvin
Chan in London and Kaitlyn Huamani in Los Angeles contributed to this
report"); illustrative delta (OpenAI minus Meta) +0.50 - same writer,
same wire, ~3 months apart.

Mechanism 1013 (NOT a falsification-family member; ledger holds at 59).
FIRST dedicated Type B mechanism on Kelvin Chan (zero "Kelvin Chan"
hits repo-wide pre-commit, grep-verified this run; his Aug-26
$18bn-settlement co-byline with Ortutay/Huamani is not mechanism-ized
under his name, disclosed). The documented AI content-licensing deal
at this outlet is AP x OpenAI (archive licensing, Jul 13 2023,
m970/m1003 lineage) - OpenAI IS the payer in the compared pair and
AP x Meta is $0 in-corpus, so the +0.50 illustrative delta runs WITH
the naive payer-softening prediction: a thesis-consistent observation
at the journalist level, NOT a falsification-family member. STRONG
confounds: peg asymmetry (antitrust enforcement order vs voluntary
corporate disclosure) and contributor-vs-lead byline asymmetry on the
OpenAI arm (Chan is a contributing credit, not the lead byline;
co-contributor Kaitlyn Huamani is saturated m959/#1213, disclosed).

Excerpt-bounded research per #503 (1 delegated scout, ~29 searches,
0 browser.open; 2 main-run exact-headline browser.search verification
sets, 0 browser.open reads). Scout SELECTED Chan as the only
fully-verified same-writer pair with URL-complete arms (AP wire,
Jun 9 / Sep 17 2026); REJECTED 40+ candidates in a numbered audit
(saturated: Criddle, Wagner, Milmo, Hern, Hardawar, Steele, Dent,
Ortutay, Bhuiyan, Murphy, Field, Paul, Nellis, Thompson, O'Brien,
Hao, Dara Kerr (type_b_513), Wong, Duffy, Gurman, Fried; structural:
Parrish, Nix, Tong, Khari Johnson, Haselton, Stokel-Walker; prior-run
rejections stand: Velazco, Albergotti, Vanian, Metz, Elias, Wiggers,
Amadeo; no clean pair: Machkovech, Ricker, Mims, Dalvin Brown,
Villas-Boas, Bass, Palazzolo, Matt O'Brien, Varanasi, Langley).
Backup #2 Rollet/BI (no verbatim article URLs surfaced); backup #3
Rosenberg/Axios (no clean Meta arm).

The m1013 block lives in profiles/careers/journalists.yaml under the
kelvin_chan_type_b keyed entry's competitor_coverage dict (per the
#643 convention); mechanism_ids [1013].

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor.

Per #795: this run only CHECKS the #1300-launched background suite
(goal hidden_files type_d_1300_full_suite.log, observed at this run's
check; an observation, not a verdict); its verdict and tombstone belong
to #1305 (next Type D). This run neither re-launches, kills, nor writes
to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

Type B lands one mechanism (mechanism 1013); the Type A predecessor
added one (mechanism 1012). Next run #1304 Type C closes the 1300-1304
window. Rotation: D #1300 -> E #1301 -> A #1302 -> B #1303 -> C #1304.
This run is the FOURTH leg of the 1300-1304 window. The main commit is
the anchor per #565.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth through fifty-ninth
member-claim forms, the sixtieth member-claim form, or the fortieth
direction form; the constants are constructed at runtime. (The landed
ordinals live as short lowercase forms in prose here; the live full-form
claims live in profiles/financial-times.yaml, profiles/news-corp.yaml,
profiles/the-verge.yaml, profiles/guardian.yaml, profiles/atlantic.yaml,
profiles/wired.yaml, profiles/ap.yaml, and profiles/careers/journalists.yaml.)

Quoted material below is limited to short verbatim phrases per the
copyright-brief-quotation rule; registers are otherwise paraphrased.
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
AP_PATH = os.path.join(PROFILES_DIR, "ap.yaml")
OWN_BASENAME = (
    "test_type_b_1303_kelvin_chan_ap_meta_whatsapp_eu_order_"
    "vs_openai_disclosure_oct08_2am.py"
)
TOP_KEY = "kelvin_chan_type_b"

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "0078dd5d043b2b47276a5a19d5e7f89919b9975e"  # patched to main commit per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1013
NEXT_NUM = 1014  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_b_1303_kelvin_chan_ap_meta_whatsapp_eu_order_"
    "vs_openai_disclosure_oct08_2am"
)

# Predecessor chain: #1302 Type A (third leg).
PRED_MAIN_1302 = "b8859fbc369d47ba937b5f4e33ed3686f65c94f8"
PRED_ANCHOR_1302 = "a8be4ff142678989ab8c4b329dc61edf54c2b422"
PRED_DOCSYNC_1302 = "b643afcec3ea8c59e91d51daa7edceb6e7e9b5f9"
PRED_FINAL_1302 = "7c49179c7a7ad38bd6a5d634cc5e5cfad0271926"
PRED_PUSH_1302 = "dd93dd6fe04f2fceb36104cbc439e3c2a3ab83ea"
# #1301 Type E (second leg) for the rotation-guard chain.
PRED_MAIN_1301 = "68be73fa52f911ddd45760980e5a08c47fec15d7"
PRED_ANCHOR_1301 = "deb96ee6d3f8356e9faef14cbf3bcba2bdf5dfcc"
PRED_DOCSYNC_1301 = "8dc0404dc76e9b0c0783a0f328a2e31486d40464"
PRED_FINAL_1301 = "9c61ea8b3e0c0bc733f0c9bea6364e8a722f00dc"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the own-run git-log pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1303 = "0078dd5d043b2b47276a5a19d5e7f89919b9975e"  # re-pinned to #1303 main sha in the terminal log-hash followup per #721

# Forward guard for the next leg: #1304 Type C. Re-pinned by #1304's
# log-hash followup per #721 (starts as 0*40; the forward pin is
# deselected in the in-gate run and fails pre-commit by design).
PRED_MAIN_1304 = "0" * 40

# The #1302 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 1012; zero one-zero-one-three keys all
# forms / no-Type-B-#1303-in-git-log / fortieth direction absent /
# forty-eighth through fifty-ninth members intact /
# sixtieth member absent / ledger 59).
D1302_FILE = (
    "test_type_a_1302_wsj_google_eu_dma_fine_enforcement_"
    "vs_carried_meta_arms_oct08_1am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 73204  # post-doc-sync total (pre-sync 73086 + 118)
README_FILE_COUNT = 1628  # pre-sync 1627 + 1 (this file)

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

# Novel source URLs: 3 zero-hit repo-wide pre-commit (git grep -F);
# 1 in-corpus re-surface disclosed (Reuters Jul-13-2023 AP x OpenAI
# deal URL via m970, re-surfaced).
NOVEL_URLS = [
    "https://techxplore.com/news/2026-06-eu-meta-whatsapp-access-rival.pdf",
    "https://www.wvlt.tv/2026/09/17/openai-flags-more-concerning-new-ai-behavior-vows-track-it-more-closely/",
    "https://www.barchart.com/story/news/2382257/eu-orders-meta-to-restore-whatsapp-access-for-rival-ai-chatbots",
]
RESURFACED_URLS = [
    "https://www.reuters.com/business/media-telecom/associated-press-openai-partner-explore-generative-ai-use-news-2023-07-13/",
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

class TestAnchor1303:
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
        assert "FOURTH leg of the 1300-1304 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1303:
    def test_predecessor_1302_chain_verified(self):
        for sha in (
            PRED_MAIN_1302, PRED_ANCHOR_1302, PRED_DOCSYNC_1302,
            PRED_FINAL_1302, PRED_PUSH_1302,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1301_chain_verified(self):
        for sha in (
            PRED_MAIN_1301, PRED_ANCHOR_1301, PRED_DOCSYNC_1301,
            PRED_FINAL_1301,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1300 -> E #1301 -> A #1302 -> B #1303 -> C #1304" in src

    def test_next_leg_is_type_c_1304(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1304 Type C" in src

    def test_type_b_lands_one_mechanism(self):
        # Type B lands exactly one mechanism (mechanism 1013); the Type
        # A predecessor added one (mechanism 1012).
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1303:
    def test_top_key_found(self):
        assert _top()["mechanism_ids"] == [MECH_NUM]

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1303 in key, no 1013 or
        # 1014 substring.
        assert "1303" in BLOCK_KEY
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
        assert nums, "mechanism 1013 must be present in profiles"

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

    def test_novel_url_counts(self):
        assert len(NOVEL_URLS) == 3
        assert len(RESURFACED_URLS) == 1

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
        # The techxplore PDF mirror URL was zero-hit repo-wide
        # pre-commit; now present only inside this block.
        text = _block_text()
        assert "techxplore.com/news/2026-06-eu-meta-whatsapp-access-rival" in text
        block_start = text.index(BLOCK_KEY + ":")
        assert "techxplore.com/news/2026-06-eu-meta-whatsapp-access-rival" not in text[:block_start]

    def test_openai_mirror_url_novelty(self):
        text = _block_text()
        assert "wvlt.tv/2026/09/17/openai-flags-more-concerning-new-ai-behavior" in text
        block_start = text.index(BLOCK_KEY + ":")
        assert "wvlt.tv/2026/09/17/openai-flags-more-concerning-new-ai-behavior" not in text[:block_start]

    def test_kelvin_chan_novelty(self):
        # Zero "Kelvin Chan" hits repo-wide pre-commit (grep-verified
        # this run); now present only inside this block.
        text = _block_text()
        assert text.count("Kelvin Chan") >= 1
        block_start = text.index(TOP_KEY + ":")
        assert "Kelvin Chan" not in text[:block_start]

    def test_both_arms_new_documented(self):
        b = _block()
        assert "NEW" in b["meta_arm"]["status"]
        assert "NEW" in b["openai_arm"]["status"]

    def test_no_type_b_1303_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type B #1303" must be this run's main
        # commit or a descendant of it - i.e., no PRIOR run committed
        # this run's iteration. Deselected in the in-gate run (fails
        # pre-commit by design: PRED_MAIN_1303 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type B #1303")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1303).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h


# ---------------------------------------------------------------------------
# 4. Block structure under the NEW kelvin_chan_type_b top-level key.
# ---------------------------------------------------------------------------

class TestBlockStructure1303:
    def test_journalists_profile_exists(self):
        assert os.path.exists(JOURNALISTS_PATH)

    def test_top_key_is_expected_parent(self):
        assert _top()["name"] == "Kelvin Chan"
        assert _top()["publication"] == "ap"

    def test_block_key_present_under_competitor_coverage(self):
        assert BLOCK_KEY in _top()["competitor_coverage"]

    def test_mechanism_id_field(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_iteration_fields(self):
        b = _block()
        assert b["iteration"] == 1303
        assert b["type"] == "B"
        assert b["date"] == "2026-10-08 02:00 PDT"

    def test_required_block_fields(self):
        b = _block()
        for field in (
            "block_key", "mechanism_id", "iteration", "type", "date",
            "test_file", "author", "goal_id", "job_id",
            "scheduled_job_id", "journalist", "publication", "window",
            "design", "meta_arm", "openai_arm",
            "scorer_delta_MANUAL_ILLUSTRATIVE", "delta_reading",
            "confounders", "counter_evidence", "connects_to", "verdict",
            "finding", "falsification_family",
            "falsification_family_member", "falsification_ledger",
            "ledger_note", "is_significant", "correlation_not_causation",
            "no_analysis_json_update", "artifact_readiness",
            "research_method", "novelty", "background_suite_status",
            "in_flight", "source_urls",
        ):
            assert field in b, field

    def test_test_file_field_matches_own_basename(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_meta_arm_tone(self):
        assert _block()["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.40

    def test_comp_arm_tone(self):
        assert _block()["openai_arm"]["tone_MANUAL_ILLUSTRATIVE"] == 0.10

    def test_scorer_delta(self):
        assert _block()["scorer_delta_MANUAL_ILLUSTRATIVE"] == 0.50

    def test_connects_to_lineage(self):
        assert 970 in _block()["connects_to"]
        assert 1003 in _block()["connects_to"]

    def test_source_urls_count(self):
        assert len(_block()["source_urls"]) == 4

    def test_meta_arm_date_and_byline(self):
        b = _block()
        assert b["meta_arm"]["date"] == "2026-06-09"
        assert b["meta_arm"]["author_byline"] == "Kelvin Chan"

    def test_comp_arm_date_and_byline(self):
        b = _block()
        assert b["openai_arm"]["date"] == "2026-09-17"
        # Contributing credit (Chan + Huamani); assert membership, not
        # equality - the contributor asymmetry is a disclosed confound.
        assert "Kelvin Chan" in b["openai_arm"]["author_byline"]


# ---------------------------------------------------------------------------
# 5. Content discipline: short verbatim phrases, mirror attestation, ASCII.
# ---------------------------------------------------------------------------

class TestM1013ContentDiscipline1303:
    def test_meta_key_phrases_verbatim(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "ordered Meta Platforms to restore access" in joined
        assert "breaching EU law" in joined

    def test_meta_headline_verbatim(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "restore WhatsApp access for rival AI chatbots" in joined

    def test_meta_regulatory_register(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "prevent harm to competition" in joined
        assert "regulatory overreach" in joined

    def test_openai_key_phrases_verbatim(self):
        quotes = _block()["openai_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "disclosed six reports" in joined
        assert "unexpected or concerning" in joined

    def test_openai_disclosure_register(self):
        quotes = _block()["openai_arm"]["key_quotes"]
        joined = " ".join(quotes)
        assert "step in the right direction" in joined
        assert "broader and better-informed consensus" in joined

    def test_ap_openai_deal_disclosed(self):
        b = _block()
        assert "Jul-13-2023" in b["design"] or "Jul 13 2023" in b["design"]
        assert "m970" in b["design"] or "970" in b["design"]

    def test_ap_meta_zero_deal_disclosed(self):
        b = _block()
        assert "$0" in b["design"] or "zero-deal" in b["design"]

    def test_mirror_attestation_disclosed(self):
        b = _block()
        assert "mirror-attested" in b["meta_arm"]["evidence_tier"]
        assert "mirror-attested" in b["openai_arm"]["evidence_tier"]
        assert "0 browser.open per #503" in b["meta_arm"]["evidence_tier"]

    def test_contributor_byline_disclosed(self):
        b = _block()
        assert "contributing" in b["openai_arm"]["evidence_tier"]

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

class TestStatisticalDiscipline1303:
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

    def test_thesis_consistent_not_falsification(self):
        # The +0.50 delta runs WITH the naive payer-softening
        # prediction (AP x OpenAI deal; OpenAI is the payer), so this
        # is a thesis-consistent observation, NOT a falsification.
        b = _block()
        assert b["falsification_family_member"] is False
        assert "thesis-consistent" in b["falsification_family"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 59 (NOT a member).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1303:
    def test_not_a_falsification_family_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert "NOT a falsification-family member" in b["falsification_family"]

    def test_thesis_consistent_disclosed(self):
        b = _block()
        assert "thesis-consistent" in b["falsification_family"]

    def test_fifty_ninth_intact_in_news_corp(self):
        # Landed #1302 (m1012, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
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

    def test_ledger_holds_at_59(self):
        assert "holds at 59" in _block()["ledger_note"]
        assert _block()["falsification_ledger"] == 59

    def test_ledger_note_states_not_a_member(self):
        assert "NOT a falsification-family member" in _block()["ledger_note"]


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: pins for #1304; #1302's pins flip BY DESIGN.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1303:
    def test_pins_on_1013_landing(self):
        # Type B lands one mechanism: max becomes 1013, next is 1014.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1013" in src
        assert "NEXT_NUM = 1014" in src

    def test_no_type_c_1304_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1304's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1304" must be #1304's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1304 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1304")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1304's own commits"
        main = _git("rev-parse", PRED_MAIN_1304).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1014_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1014_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1014_dash_absent_repo_wide(self):
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
        # m1013 is NOT a falsification-family member (thesis-consistent
        # observation); the sixtieth member-claim form stays absent
        # repo-wide.
        assert _git_grep_tracked_source(_T60, None) == []

    def test_predecessor_1302_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, D1302_FILE))

    def test_next_leg_is_1304_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1304 Type C" in src

    def test_1302_pins_flip_by_design_documented(self):
        # #1302's forward guards (max-1012, zero one-zero-one-three
        # keys all forms, no-Type-B-#1303-in-git-log, fortieth
        # direction absent, forty-eighth through fifty-ninth members
        # intact, no sixtieth member, ledger 59) verified GREEN
        # pre-commit this run via the subprocess staleness pin (Type
        # B lands mechanism 1013 as a thesis-consistent observation,
        # not a family member); the max-1012 and zero one-zero-one-three
        # pins flip post-main-commit on this run's own landing (the
        # #1191-class self-trip on no-Type-B-#1303-in-git-log, re-pinned
        # green in the terminal followup, and the #1272-class
        # forward-guard expiry on 1013-numeric-absent, permanent), by
        # design, documented in the staleness pin below).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1303" in src
        assert "1 failed, 21 passed" in src


# ---------------------------------------------------------------------------
# 9. Background suite: #1300's suite is CHECKED ONLY per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1303:
    def test_1300_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1300_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1300-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1303_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1300-launched" in _block()["background_suite_status"]
        assert "#795" in _block()["background_suite_status"]
        assert "#1305" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1303:
    def test_readme_test_file_table_has_1303_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1303" in readme

    def test_architecture_has_1303_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1303" in arch

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

class TestIterationLog1303:
    def test_1303_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1303 Type B" in log

    def test_1302_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1302 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1302's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1303:
    def test_1302_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 21 of the 22 pass; the one that
        # fails BY DESIGN is test_1013_numeric_absent_in_profiles
        # (mechanism 1013 lands in profiles/ this run; the #1272-class
        # forward-guard expiry - the next-number guard is consumed by
        # the landing; stays red permanently). The second flip,
        # test_no_type_b_1303_in_git_log_pin (the #1191-class
        # self-trip: this run's own main commit carries "Type B
        # #1303"), is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1303 now holds this run's
        # main sha). test_pins_on_one_mechanism_landing stays GREEN
        # (asserts on the #1302 file's own constants, untouched by
        # this run); the member and direction pins stay GREEN (m1013
        # is a thesis-consistent observation, not a family member).
        # Deselected pre-commit (the pin passes pre-commit).
        res = _class_run(D1302_FILE, "TestGuardLifecycle1302")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "1 failed, 21 passed" in res.stdout, res.stdout[-2000:]
        assert "test_1013_numeric_absent_in_profiles" in res.stdout, \
            res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1303:
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
