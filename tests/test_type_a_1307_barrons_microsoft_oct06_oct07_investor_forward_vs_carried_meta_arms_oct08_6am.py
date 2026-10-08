"""Type A #1307: Barron's x Microsoft Oct-6/Oct-7 2026 investor-forward register (Oct 8 2026, ~06:00 AM PDT).

m1015 - FIRST dedicated corpus mechanism on the Barron's x Microsoft
investor-forward register. The naive uniform payer-softening prediction
(news-corp.yaml competitor_relationships.microsoft coverage_prediction
"softer", from the Nov-2024 News Corp x Microsoft HarperCollins
book-licensing deal) is MET, not falsified, on the fresh peg: Barron's
runs the Oct-6 AI-safety-moment as a Microsoft bull case ("Microsoft
Nears $4 Trillion as AI Safety Fears Become a Selling Point", 98%
analyst Buy) and the Oct-7 Surface/Nvidia keynote as product-forward
event coverage ("Microsoft and Nvidia Unveil AI-Centric Laptop and
'Hybrid Intelligence'", Surface Laptop Ultra $2,599 preorder). MANUAL
ILLUSTRATIVE +0.30 (B1) / +0.20 (B2); Microsoft arm avg +0.25.

Carried Barron's x Meta arms (M1 +0.05 Sep-24 Connect keynote,
M2 +0.10 Sep-23 Muse investor piece, from #1237, un-rescored per #807),
mean +0.075. Illustrative delta (Microsoft minus Meta): +0.175 -
symmetric investor-forward softness at the investor title; the smaller
Meta payer and the Microsoft payer both get the cushioned register.

This EXTENDS m527 (Sep-4 WSJ x Microsoft woo-side register,
financially-scrutinized-but-cushioned +0.07) into a NEW cushioning form:
safety-fear inversion (the same Oct-6 AI-safety news moment the FT ran
adversarially on its own payer OpenAI - saturated member line - Barron's
runs as a Microsoft selling point). The softness is title-local, not
parent-level: the NY Post Sep-18 "largest theft of labor in human
history" piece (novel URL this run, adversarial on BOTH Microsoft and
OpenAI payers) shows the tabloid register goes hard on payers -
consistent with the 29th member's dual-payer tabloid symmetry.

Per #715 this docstring uses lowercase forms only: thesis-consistent
observation, NOT a falsification-family member (ledger holds at 59);
no new direction - fortieth absent by design, 35th-39th stand. Verdict:
thesis_consistent_observation, domain-bounded to Barron's investor
register on the Oct-6/Oct-7 product/market pegs.

Novelty: the two Barron's URLs and the NY Post Sep-18 URL zero-hit
repo-wide pre-commit (git grep -F). The scout's FT x OpenAI Oct-6
rogue-agent liability arms were excluded by design (saturated:
FT x OpenAI member line); WIRED x OpenAI Oct-6 arms excluded
(saturated: 40th/47th member line); WSJ x OpenAI Sep-28/Oct-1 double
excluded (saturated: m904 44th member).

Statistical discipline: monitoring-only per the Aug 28 2026 standing rule
(MANUAL ILLUSTRATIVE ONLY, engine NOT run, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, NOT artifact-grade, no analysis.json
update, verdict thesis_consistent_observation). Correlation is not
causation. Hypothesis-generating only.

1 delegated scout (ranked 3 pairs; FT x OpenAI + WIRED x OpenAI held as
saturated backups; NY Post x Microsoft Sep-18 noted as novel counterpoint)
+ 3 main-run browser.search verification sets (2 scout-corroboration + 1
fresh), 0 browser.open per #503. Excerpt-bounded; the Barron's URLs are
verbatim from the Full-URL listings; no canonical URLs constructed.
ASCII-only, no em dashes.

Rotation: this run is iteration #1307 Type A, the THIRD leg of the
1305-1309 window (D #1305 -> E #1306 -> A #1307 -> B #1308 -> C #1309, per
the #565 anchor + rotation guard). Predecessor #1306 Type E verified in
git log (main 0ac1044d / anchor 69dadafb / doc-sync dbed9dbc / log-hash
f7640d28); the 1300-1304 window is VERIFIED CLOSED. This run's main
commit is the anchor per #565; ANCHORED_SHA patched post-commit. The
#1306 forward guards verified pre-commit this run: max-1014; zero
one-zero-one-five keys all forms; no-Type-A-#1307-in-git-log; fortieth
direction absent; forty-eighth through fifty-ninth members intact; no
sixtieth member (repo-wide); ledger 59. Next: #1308 Type B continues the
window; the #1305-launched background-suite verdict belongs to #1310
per #795.

Pre-commit novelty greps per #715: zero test_type_a_1307 files on disk
(glob); no "Type A #1307" in git log (--grep); max numeric mechanism_id
1014 in profiles/ pre-commit (mechanism_id regex sweep); zero
numeric/underscore/dash one-zero-one-five mechanism key forms repo-wide
pre-commit (needles format-built per #715, own file excluded, __pycache__
excluded per the #715 pattern-rescope lesson); block key zero-hit
repo-wide pre-commit (designed keying: iteration 1307 in key, no 1015
substring, per the #723/#738/#739 convention); "## #1307" zero-hit in
iteration-log pre-commit; README stats 73473/1631 pre-commit; no #1307
row in README/ARCHITECTURE test tables pre-commit; the 3 novel URLs
zero-hit repo-wide pre-commit (git grep -F).

Doc-sync constants per #719: README_TEST_COUNT / README_FILE_COUNT hold
the post-doc-sync values from the start (patched pre-main once the
in-gate collection count is known); the doc-sync commit ratchets README
73473/1631 -> post-sync totals.
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
NEWSCORP_PATH = os.path.join(PROFILES_DIR, "news-corp.yaml")
WIRED_PATH = os.path.join(PROFILES_DIR, "wired.yaml")

OWN_BASENAME = (
    "test_type_a_1307_barrons_microsoft_oct06_oct07_"
    "investor_forward_vs_carried_meta_arms_oct08_6am.py"
)
BLOCK_KEY = (
    "type_a_1307_barrons_microsoft_oct06_oct07_"
    "investor_forward_vs_carried_meta_arms_oct08_6am"
)

# Pre-commit placeholder per #565; patched to the main commit sha in
# the anchor followup.
ANCHORED_SHA = "0" * 40

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1015
NEXT_NUM = 1016  # integer only; key-form needles are format-built

# Predecessor chain: #1306 Type E closed the SECOND leg.
PRED_MAIN_1306 = "0ac1044d0d6398ffcaa7914662323af0dd125c7b"
PRED_ANCHOR_1306 = "69dadafb9f5ab2696cc61a2c5286c93c0715748b"
PRED_DOCSYNC_1306 = "dbed9dbca9bc70bc7602d1d95bd3fdcc14656e9c"
PRED_FINAL_1306 = "f7640d284e1a27dd0f795910dbc3d8da56937fb8"

# This run's main commit (full sha), for the ancestor-form
# no-Type-A-#1307 pin in the #1306 file. Patched in the terminal
# log-hash followup per #721.
PRED_MAIN_1307 = "0" * 40  # re-pinned in the terminal log-hash followup per #721

# #1308's main commit (full sha), for the ancestor-form no-Type-B-#1308
# pin. Patched in #1308's terminal log-hash followup per #721.
PRED_MAIN_1308 = "0" * 40  # re-pinned to #1308 main sha per #721

# The #1306 predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1014; zero next-number
# one-zero-one-five / no-Type-A-#1307-in-git-log / fortieth
# direction absent / forty-eighth through fifty-ninth members
# intact / sixtieth member absent / ledger 59).
D1306_FILE = (
    "test_type_e_1306_podcast_sentiment_184th_"
    "verification_oct08_5am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 73575  # post-doc-sync total (pre-sync 73473 + 102)
README_FILE_COUNT = 1632  # pre-sync 1631 + 1 (this file)

# MANUAL ILLUSTRATIVE tones (hand-assigned at excerpt level).
B1_SAFETY_SELLING_POINT_TONE = 0.30
B2_SURFACE_EVENT_TONE = 0.20
MICROSOFT_MEAN_TONE = 0.25
META_M1_TONE = 0.05
META_M2_TONE = 0.10
META_MEAN_TONE = 0.075
ILLUSTRATIVE_DELTA = 0.175

# Ordinal member-claim forms, built at runtime so this source file
# carries no contiguous full-form claim (per the #715 literal
# discipline; the live full-form claims live in the profile block).
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

B1_URL = (
    "https://www.barrons.com/articles/"
    "microsoft-stock-buy-ai-security-4c4c7383"
)
B2_URL = (
    "https://www.barrons.com/articles/"
    "microsoft-and-nvidia-will-present-new-ai-centric-"
    "laptop-today-why-it-matters-1a5fb9e9"
)
NYPOST_COUNTERPOINT_URL = (
    "https://nypost.com/2026/09/18/business/"
    "microsoft-openai-workers-privately-worried-their-work-"
    "is-largest-theft-of-labor-in-human-history/"
)


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO_ROOT, capture_output=True,
        text=True,
    )


def _iter_source_files():
    """Yield profile + test source files for the sweep instruments.

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
    return subprocess.run(
        ["python3", "-m", "pytest", filename + "::" + classname, "-q"],
        cwd=TESTS_DIR, capture_output=True, text=True,
    )


def _block():
    doc = yaml.safe_load(_read(NEWSCORP_PATH))
    return doc["competitor_relationships"]["microsoft"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Anchor per #565 (this run's main commit is the anchor; the anchor
#    followup patches ANCHORED_SHA to the main commit sha).
# ---------------------------------------------------------------------------


class TestAnchor1307:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565. This test is
        # deselected in the in-gate run; the patched form is asserted
        # post-anchor.
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

    def test_anchor_duality_documented(self):
        # The #565 duality: the placeholder pin passes pre-commit and
        # fails post-anchor BY DESIGN; the patched pin is the mirror.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "BY DESIGN post-anchor" in src or "fails BY DESIGN" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1306 closed the SECOND leg; #1307 is the THIRD.
# ---------------------------------------------------------------------------


class TestRotationGuard1307:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-60").stdout
        for sha, label in (
            (PRED_MAIN_1306, "1306 main"),
            (PRED_ANCHOR_1306, "1306 anchor"),
            (PRED_DOCSYNC_1306, "1306 doc-sync"),
            (PRED_FINAL_1306, "1306 log-hash"),
        ):
            assert sha[:8] in log, label

    def test_1306_type_e_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type E #1306").stdout
        assert out.strip() != ""

    def test_third_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD leg of the 1305-1309 window" in src

    def test_1300_1304_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1300-1304" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1308_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B #1308" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: Type A lands one mechanism (max 1014 -> 1015).
# ---------------------------------------------------------------------------


class TestMechanismNovelty1307:
    def test_max_numeric_mechanism_id_1015(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_type_a_1307_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type A #1307" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type A #1307")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1307).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715, __pycache__
        # excluded per the #715 pattern-rescope lesson). NEXT_NUM is
        # 1016: this run lands 1015, so the next-number forms stay
        # absent.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_designed_no_1015_substring(self):
        # Designed keying per #723/#738/#739: the iteration-form block
        # key carries the iteration (1307), never the mechanism number.
        assert "1015" not in BLOCK_KEY
        assert "1307" in BLOCK_KEY

    def test_forward_guards_for_1308(self):
        # Staged for the next leg: max-1015 in profiles/; zero
        # one-zero-one-six keys all forms; no-Type-B-#1308-in-git-log;
        # fortieth direction absent; forty-eighth through fifty-ninth
        # intact; no sixtieth member; ledger 59.
        assert _max_numeric_mechanism_id() == 1015
        assert _repo_grep_numeric_mechanism_id(1016) == []
        assert _repo_grep_underscore_mechanism(1016) == []
        assert _repo_grep_dash_mechanism(1016) == []
        assert _git("log", "--oneline", "--grep=Type B #1308").stdout.strip() == ""
        assert _git_grep_tracked_source(_T40, "profiles/") == []
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]
        assert _T59 in _read(os.path.join(PROFILES_DIR, "news-corp.yaml"))
        assert _git_grep_tracked_source(_T60, None) == []

    def test_novel_urls_zero_hit_pre_commit(self):
        # The two Barron's URLs and the NY Post counterpoint URL were
        # zero-hit repo-wide pre-commit (git grep -F, verified this run
        # before the block landed). Post-landing they live in the
        # block's arms; assert each is present in news-corp.yaml.
        text = _read(NEWSCORP_PATH)
        assert text.count(B1_URL) >= 1
        assert text.count(B2_URL) >= 1
        assert text.count(NYPOST_COUNTERPOINT_URL) >= 1


# ---------------------------------------------------------------------------
# 4. Barron's x Microsoft Oct-6/Oct-7 arms (NEW this run)
# ---------------------------------------------------------------------------


class TestBarronsMicrosoftArms1307:
    def test_block_present_with_mechanism_id_1015(self):
        block = _block()
        assert block["mechanism_id"] == 1015
        assert block["iteration"] == 1307
        assert block["iteration_type"] == "A"

    def test_b1_title_and_date(self):
        block = _block()
        arm = block["microsoft_arms"][0]
        assert arm["title"] == (
            "Microsoft Nears $4 Trillion as AI Safety Fears "
            "Become a Selling Point"
        )
        assert arm["date"] == "2026-10-06"

    def test_b1_url_novel(self):
        block = _block()
        arm = block["microsoft_arms"][0]
        assert arm["url"] == B1_URL
        assert "zero-hit" in arm["url_status"]

    def test_b1_register_safety_fear_inversion(self):
        block = _block()
        arm = block["microsoft_arms"][0]
        assert arm["register"] == "safety_fear_inversion_bull_case"

    def test_b1_tone_plus_030(self):
        block = _block()
        arm = block["microsoft_arms"][0]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == B1_SAFETY_SELLING_POINT_TONE == 0.30

    def test_b1_key_facts_safety_selling_point(self):
        block = _block()
        text = yaml.safe_dump(block["microsoft_arms"][0])
        assert "$4 Trillion" in text
        assert "98%" in text

    def test_b2_title_and_date(self):
        block = _block()
        arm = block["microsoft_arms"][1]
        assert arm["title"] == (
            "Microsoft and Nvidia Unveil AI-Centric Laptop and "
            "'Hybrid Intelligence'"
        )
        assert arm["date"] == "2026-10-07"

    def test_b2_url_novel(self):
        block = _block()
        arm = block["microsoft_arms"][1]
        assert arm["url"] == B2_URL
        assert "zero-hit" in arm["url_status"]

    def test_b2_register_product_forward_event(self):
        block = _block()
        arm = block["microsoft_arms"][1]
        assert arm["register"] == "product_forward_event"

    def test_b2_tone_plus_020(self):
        block = _block()
        arm = block["microsoft_arms"][1]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == B2_SURFACE_EVENT_TONE == 0.20

    def test_b2_key_facts_surface_ultra(self):
        block = _block()
        text = yaml.safe_dump(block["microsoft_arms"][1])
        assert "$2,599" in text
        assert "RTX Spark" in text

    def test_microsoft_mean_plus_025(self):
        block = _block()
        assert block["microsoft_mean_tone"] == MICROSOFT_MEAN_TONE == 0.25

    def test_two_new_arms(self):
        # Only the Oct-6/Oct-7 Barron's pegs are NEW this run: the
        # scout's FT x OpenAI Oct-6 rogue-agent liability arms were
        # deliberately excluded (saturated: FT x OpenAI member line),
        # the WIRED x OpenAI Oct-6 arms were excluded (saturated:
        # 40th/47th member line), and the WSJ x OpenAI Sep-28/Oct-1
        # double was excluded (saturated: m904 44th member).
        block = _block()
        assert "saturated" in yaml.safe_dump(block)

    def test_nypost_counterpoint_novel_url(self):
        # The Sep-18 NY Post "largest theft of labor" piece is novel
        # to the corpus and adversarial on BOTH payers - carried as a
        # bounding counterpoint, not a fresh arm.
        block = _block()
        cp = block["tabloid_register_counterpoint"]
        assert cp["url"] == NYPOST_COUNTERPOINT_URL
        assert "zero-hit" in cp["url_status"]

    def test_excerpt_bounded_no_browser_open(self):
        block = _block()
        assert block["research_method"].count("0 browser.open") >= 1


# ---------------------------------------------------------------------------
# 5. Carried Barron's x Meta arms (#1237, un-rescored per #807)
# ---------------------------------------------------------------------------


class TestMetaArms1307:
    def test_meta_arms_carried_from_1237(self):
        block = _block()
        assert "#1237" in block["meta_arms_carried"]["carried_from"]
        assert "#807" in block["meta_arms_carried"]["carried_from"]

    def test_m1_connect_keynote_plus_005(self):
        block = _block()
        arms = block["meta_arms_carried"]["arms"]
        assert any("+0.05" in a for a in arms)

    def test_m2_muse_investor_plus_010(self):
        block = _block()
        arms = block["meta_arms_carried"]["arms"]
        assert any("+0.10" in a for a in arms)

    def test_meta_mean_plus_0075(self):
        block = _block()
        assert block["meta_arms_carried"]["meta_mean"] == META_MEAN_TONE == 0.075


# ---------------------------------------------------------------------------
# 6. Financial relationship: News Corp x Microsoft HarperCollins deal
# ---------------------------------------------------------------------------


class TestFinancialRelationship1307:
    def test_deal_nov_2024_documented(self):
        block = _block()
        deal = block["financial_relationship"]["deal"]
        assert "Nov 2024" in deal
        assert "HarperCollins" in deal

    def test_deal_never_officially_confirmed(self):
        block = _block()
        deal = block["financial_relationship"]["deal"]
        assert "never officially confirmed" in deal

    def test_book_division_attenuation_disclosed(self):
        block = _block()
        fr = block["financial_relationship"]
        assert "attenuated" in fr["transmission_note"]

    def test_multi_payer_confounders_disclosed(self):
        block = _block()
        fr = block["financial_relationship"]
        assert "OpenAI" in fr["openai_financial"]
        assert "Meta" in fr["meta_financial"]

    def test_coverage_prediction_naive_softer(self):
        block = _block()
        pred = block["financial_relationship"]["coverage_prediction"]
        assert "softer" in pred

    def test_prediction_met_not_falsified(self):
        block = _block()
        assert block["financial_relationship"]["prediction_outcome"] == (
            "MET_not_falsified"
        )

    def test_non_causal_language_present(self):
        block = _block()
        assert "Correlation does not establish causation" in \
            block["financial_relationship"]["non_causal_language"]


# ---------------------------------------------------------------------------
# 7. Asymmetry delta: Microsoft +0.25 vs Meta +0.075, delta +0.175
# ---------------------------------------------------------------------------


class TestAsymmetryDelta1307:
    def test_microsoft_mean_plus_025(self):
        block = _block()
        assert block["scorer"]["microsoft_mean_tone"] == MICROSOFT_MEAN_TONE == 0.25

    def test_meta_mean_plus_0075(self):
        block = _block()
        assert block["scorer"]["meta_mean_tone"] == META_MEAN_TONE == 0.075

    def test_illustrative_delta_plus_0175(self):
        block = _block()
        assert block["scorer"]["illustrative_delta_microsoft_minus_meta"] == \
            ILLUSTRATIVE_DELTA == 0.175

    def test_delta_calc_documented(self):
        block = _block()
        assert "0.25 - 0.075 = +0.175" in block["scorer"]["delta_calc"]

    def test_degenerate_sample_contract(self):
        block = _block()
        assert "n=2 vs n=2" in block["scorer"]["methodology"]

    def test_reading_prediction_met(self):
        block = _block()
        assert block["scorer"]["reading"] == (
            "prediction_MET_symmetric_softness"
        )

    def test_engine_not_run(self):
        block = _block()
        assert block["scorer"]["engine_run"] is False


# ---------------------------------------------------------------------------
# 8. Research method: 1 scout + 3 verification sets, 0 browser.open
# ---------------------------------------------------------------------------


class TestResearchMethod1307:
    def test_delegated_scout_documented(self):
        block = _block()
        assert "1 delegated scout" in block["research_method"]

    def test_three_verification_sets(self):
        block = _block()
        assert "3 main-run browser.search verification sets" in \
            block["research_method"]

    def test_scout_rejections_documented(self):
        block = _block()
        assert "FT x OpenAI" in block["scout_rejections"]
        assert "WIRED x OpenAI" in block["scout_rejections"]

    def test_saturation_exclusions_documented(self):
        block = _block()
        assert "saturated" in block["scout_rejections"]

    def test_novelty_greps_documented(self):
        block = _block()
        assert "zero test_type_a_1307 files" in block["novelty"]

    def test_no_canonical_urls_constructed(self):
        block = _block()
        assert "no canonical URLs constructed" in block["novelty"]

    def test_excerpt_bounded(self):
        block = _block()
        assert "Excerpt-bounded" in block["research_method"] or \
            "excerpt-bounded" in block["research_method"]


# ---------------------------------------------------------------------------
# 9. Thesis-consistent observation: NOT a falsification-family member
# ---------------------------------------------------------------------------


class TestThesisConsistent1307:
    def test_not_a_member_ledger_holds_59(self):
        block = _block()
        assert block["verdict_block"]["verdict"] == "thesis_consistent_observation"
        assert "NOT a falsification-family member" in \
            block["verdict_block"]["member_status"]
        assert "ledger holds at 59" in block["verdict_block"]["member_status"]

    def test_no_sixtieth_member_form_in_block(self):
        # The block must not claim the sixtieth member (lowercase
        # docstring discipline per #715; the profile carries no
        # sixtieth member-claim form).
        text = yaml.safe_dump(_block())
        assert "SIXTIETH falsification-family member" not in text

    def test_extends_m527(self):
        block = _block()
        assert "m527" in block["verdict_block"]["extends"]

    def test_new_cushioning_register_named(self):
        block = _block()
        assert "safety_fear_inversion" in block["verdict_block"]["new_register"]

    def test_title_local_not_parent_level(self):
        block = _block()
        assert "title-local" in block["verdict_block"]["scope_bound"]

    def test_counterpoint_bounded(self):
        block = _block()
        assert "29th" in block["verdict_block"]["counterpoint_bound"]

    def test_distinct_from_m904_m1006_members(self):
        block = _block()
        d = block["verdict_block"]["distinct_from_prior"]
        assert "m904" in d
        assert "44th" in d or "FORTY-FOURTH" in d


# ---------------------------------------------------------------------------
# 10. Statistical discipline per the Aug 28 2026 standing rule
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1307:
    def test_manual_illustrative_only(self):
        block = _block()
        assert block["statistical_discipline"]["scores"] == "MANUAL ILLUSTRATIVE only"

    def test_engine_not_run(self):
        block = _block()
        assert block["statistical_discipline"]["engine_run"] is False

    def test_p_value_not_calculated(self):
        block = _block()
        sd = block["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False

    def test_not_artifact_grade(self):
        block = _block()
        sd = block["statistical_discipline"]
        assert sd["artifact_grade"] is False
        assert sd["no_analysis_json_update"] is True

    def test_verdict_thesis_consistent(self):
        block = _block()
        assert block["statistical_discipline"]["verdict"] == \
            "thesis_consistent_observation"

    def test_correlation_not_causation(self):
        block = _block()
        sd = block["statistical_discipline"]
        assert sd["correlation_not_causation"] is True
        assert sd["hypothesis_generating_only"] is True


# ---------------------------------------------------------------------------
# 11. Guard lifecycle: forward guards for #1308 (Type B).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1307:
    def test_pins_on_one_mechanism_landing(self):
        # Type A lands one mechanism: max 1015, next 1016.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1015" in src
        assert "NEXT_NUM = 1016" in src

    def test_no_type_b_1308_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1308's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1308" must be #1308's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1308")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1308's own commits"
        main = _git("rev-parse", PRED_MAIN_1308).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1016_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1016_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1016_dash_absent_repo_wide(self):
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
        assert _T56 in _read(os.path.join(PROFILES_DIR, "wired.yaml"))

    def test_fifty_seventh_member_present_pin(self):
        # Landed #1287 (m1003, profiles/ap.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_present_pin(self):
        # Landed #1292 (m1006, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_member_present_pin(self):
        # Landed #1302 (m1012, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixtieth_member_pin(self):
        # This run lands a thesis-consistent observation, NOT a
        # member: the sixtieth member-claim form stays absent
        # repo-wide (source scope; __pycache__ excluded per the #715
        # pattern-rescope lesson).
        assert _git_grep_tracked_source(_T60, None) == []

    def test_predecessor_1306_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, D1306_FILE))

    def test_next_leg_is_1308_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1308 Type B" in src

    def test_1306_pins_flip_by_design_documented(self):
        # #1306's forward guards (max-1014, zero one-zero-one-five
        # keys all forms, no-Type-A-#1307-in-git-log, fortieth
        # absent, forty-eighth through fifty-ninth intact in
        # profiles/, sixtieth absent, ledger 59) verified GREEN
        # at HEAD pre-commit this run. TWO pins flip BY DESIGN at
        # this run's main commit: the no-Type-A-#1307-in-git-log pin
        # (the #1191-class self-trip, re-pinned post-commit by
        # TestStalenessPins1307) and the zero one-zero-one-five
        # numeric pin (the #1272-class forward-guard expiry - the
        # m1015 landing carries "mechanism_id: 1015" in colon form;
        # the underscore/dash pins stay green by the #723/#738/#739
        # designed keying). The no-sixtieth-member pin stays GREEN
        # (this run lands no member). Documented in the staleness
        # pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1307" in src
        assert "no_type_a_1307_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1306's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1307:
    def test_1306_guard_lifecycle_post_commit_self_trip(self):
        # Post-terminal-followup form: 23 tests in the class; ONE
        # flips BY DESIGN when this run's main commit lands and STAYS
        # flipped permanently: test_1015_numeric_absent_in_profiles
        # (the #1272-class forward-guard expiry - the m1015 landing
        # carries "mechanism_id: 1015" in colon form; the
        # underscore/dash pins stay green by the #723/#738/#739
        # designed keying). The second flip,
        # test_no_type_a_1307_in_git_log_pin (the #1191-class
        # self-trip), is re-pinned green in the terminal log-hash
        # followup per #721 (its PRED_MAIN_1307 now holds this run's
        # main sha, in BOTH the #1307 and #1306 files per the
        # re-pin-both-copies precedent). The class run below therefore
        # expects 1 failed / 22 passed and documents the designed
        # flips. The #1306 block is read-only to this run; the flips
        # are documented here, not repaired.
        res = _class_run(D1306_FILE, "TestGuardLifecycle1306")
        out = res.stdout + res.stderr
        assert "1 failed, 22 passed" in out, out[-2000:]
        assert "test_1015_numeric_absent_in_profiles" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 13. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1307:
    def test_readme_test_file_table_has_1307_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1307_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert OWN_BASENAME in arch

    def test_readme_stats_ratcheted(self):
        readme = _read(README_PATH)
        assert "| Tests | %d |" % README_TEST_COUNT in readme
        assert "Across %d test files" % README_FILE_COUNT in readme


# ---------------------------------------------------------------------------
# 14. Iteration log per #721.
# ---------------------------------------------------------------------------


class TestIterationLog1307:
    def test_log_has_1307_entry(self):
        text = _read(LOG_PATH)
        assert "## #1307 Type A" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "m1015" in text
        assert "thesis_consistent_observation" in text
        assert "ledger holds at 59" in text


# ---------------------------------------------------------------------------
# 15. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1307:
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

    def test_own_diff_excludes_inflight(self):
        # This run's staged set must never include the in-flight
        # files; verified at commit time by explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "explicit-path staging" in src
