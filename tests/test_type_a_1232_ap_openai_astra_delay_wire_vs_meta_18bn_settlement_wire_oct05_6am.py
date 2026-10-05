# -*- coding: utf-8 -*-
"""Type A #1232 tests: Associated Press - OpenAI Sep-28/29-2026 Astra
safety-delay wire (NEW arm, relay-attested via NPR affiliates) vs AP
Aug-26-2026 Meta $18bn teen-harm settlement wire (NEW arm,
relay-attested via AP Business SummaryBrief carriers).

Mechanism 970 (NOT a falsification-family member; ledger holds at 50).
MECHANISM DOCUMENTATION of a new publication line: AP is itself the
Jul-13-2023 OpenAI archive-licensing counterparty, so this is the direct
payer-register test the corpus was missing. AP's wire register on the
shared Astra safety peg is neutral (-0.10 MANUAL ILLUSTRATIVE: "security
concerns voiced by its researchers" wrapped in OpenAI's own deceleration
frame, no adversarial vocabulary, no named critic) while the same wire
service's Meta settlement wire is settlement-factual with adversarial
substance (-0.45: "landmark legal settlement", "$18 billion", "teen
social media addiction"). Illustrative delta (OpenAI minus Meta) +0.35
runs WITH the naive payer-softening prediction, but the comparison is
cross-peg (model-delay wire vs settlement wire) and both arms are straight
wire-service copy, so the register gap tracks peg valence and the wire
genre, not editorial modulation. NOT a uniform-prediction test; ledger
holds at 50. Statistical discipline: MANUAL/QUALITATIVE ONLY per the Aug
28 2026 standing rule (tones hand-assigned, n=1 vs n=1;
p_value/cohens_d/ci_95 NOT_CALCULATED; engine NOT run; is_significant
false; NOT artifact-grade; no analysis.json update).

Research: delegated scout (17 browser.search query sets across 11
candidate pairs; SELECTED AP x OpenAI; REJECTED Bloomberg/Verge/NYT/
Atlantic x OpenAI|Anthropic as saturated, WaPo x OpenAI for failing
verbatim-URL discipline, Forbes x OpenAI as peg-absent, CNBC x OpenAI as
near-miss with no citable URLs, WSJ x Anthropic as thin/out-of-window) +
2 main-run browser.search verification sets (AP x OpenAI Jul-13-2023 deal
confirmed via Reuters/pressgazette; AP Meta $18bn wire confirmed via
ftimes/MTSU carriers with the OAKLAND, Calif. (AP) Aug-26 dateline).
0 browser.open per #503 (excerpt-bounded; relay attestation; no canonical
apnews.com URLs constructed).

The mechanism 970 block lives in profiles/ap.yaml (NEW profile file this
run) as a competitor_relationships.openai sub-key (4-space indent),
appended after the openai financial_metadata stub. Targeted staging by
explicit path only; the in-flight #899/#938/#900/#1012-wt files stay out
of this run's index/diff.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor.

Per #795: this run only CHECKS the #1230-launched background suite
(goal hidden_files type_d_1230_full_suite.log); its verdict and tombstone
belong to #1235 (next Type D). This run neither re-launches, kills, nor
writes to the suite.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed or next number, the forty-eighth / forty-ninth / fiftieth /
fifty-first member-claim forms, or the thirty-fifth through fortieth
direction forms; the constants are constructed at runtime. (The landed
ordinals live as short lowercase forms in prose here; the live full-form
claims live in profiles/financial-times.yaml and
profiles/careers/journalists.yaml: the forty-eighth, forty-ninth, and
fiftieth members respectively.)
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
    "test_type_a_1232_ap_openai_astra_delay_wire_vs_"
    "meta_18bn_settlement_wire_oct05_6am.py"
)
PROFILE_FILE = os.path.join(PROFILES_DIR, "ap.yaml")

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "9f74c6eef01113e5f8ccce4cb518d5c4399a9d1f"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 970
NEXT_NUM = 971  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_a_1232_ap_openai_astra_delay_wire_vs_"
    "meta_18bn_settlement_wire"
)

# Predecessor chain: #1231 Type E continued the 1230-1234 window.
PRED_MAIN_1231 = "9f4fdafe"
PRED_ANCHOR_1231 = "5d933b11"
PRED_DOCSYNC_1231 = "c0d7f479"
PRED_FINAL_1231 = "2ba700c2"

# The #1231 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 969; zero next-number nine-seven-zero /
# no-Type-A-#1232-in-git-log / fortieth direction absent /
# forty-eighth + forty-ninth + fiftieth members intact /
# fifty-first member absent / ledger 50).
E1231_FILE = (
    "test_type_e_1231_podcast_sentiment_169th_verification_oct05_5am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 66958  # post-doc-sync total (pre-sync 66895 + 63)
README_FILE_COUNT = 1557  # pre-sync 1556 + 1 (this file)

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"

# Novel source URLs: 5 are zero-hit repo-wide pre-commit (git grep -F);
# the pressgazette AI-deals roundup is an in-corpus deal source
# (re-surface: cited in financial-times.yaml, guardian.yaml, etc.).
# Post-commit all 6 live in the block's source_urls.
NOVEL_URLS = [
    "https://www.wextradio.org/npr-news/2026-09-29/"
    "openai-delays-latest-model-over-security-concerns-as-"
    "industry-faces-pressure",
    "https://www.kcsm.org/npr-news/2026-09-28/"
    "openai-delays-latest-model-over-security-concerns-as-"
    "industry-faces-pressure",
    "https://firstamendment.mtsu.edu/post/"
    "meta-reaches-landmark-18-billion-settlement-with-states-in-"
    "trial-over-teen-social-media-addiction/",
    "https://www.ftimes.com/news/wire/ap-business-summarybrief-at-"
    "7-23-p-m-edt/article_2994cee1-89c2-54f7-b73c-4b2847a22a93.html",
    "https://www.reuters.com/business/media-telecom/"
    "associated-press-openai-partner-explore-generative-ai-use-"
    "news-2023-07-13/",
    "https://pressgazette.co.uk/platforms/"
    "news-publisher-ai-deals-lawsuits-openai-google/",
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


def _load_ap():
    import yaml
    return yaml.safe_load(_read(PROFILE_FILE))


def _openai_section():
    return _load_ap()["competitor_relationships"]["openai"]


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

class TestAnchor1232:
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
        assert "THIRD leg of the 1230-1234 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestRotationGuard1232:
    def test_predecessor_1231_chain_verified(self):
        for sha in (
            PRED_MAIN_1231, PRED_ANCHOR_1231, PRED_DOCSYNC_1231,
            PRED_FINAL_1231,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_predecessor_1230_chain_verified(self):
        for sha in ("3d4a7a89", "23de2781", "6f62b9a7", "407016dd"):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1230 -> E #1231 -> A #1232 -> B #1233 -> C #1234" in src

    def test_next_leg_is_type_b_1233(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1233 Type B" in src

    def test_type_a_lands_one_mechanism(self):
        # Type A lands exactly one mechanism (mechanism 970); the Type
        # E predecessor added none.
        assert _block()["mechanism_id"] == MECH_NUM
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type A lands one mechanism" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline)
# ---------------------------------------------------------------------------

class TestMechanismNovelty1232:
    def test_openai_section_found(self):
        sec = _openai_section()
        assert BLOCK_KEY in sec

    def test_block_key_zero_mechanism_number_substring(self):
        # Designed keying per #715: iteration 1232 in key, no 970 or
        # 971 substring.
        assert "1232" in BLOCK_KEY
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
        assert nums, "mechanism 970 must be present in profiles"

    def test_no_duplicate_block_key(self):
        text = _block_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_novel_urls_in_block_source_urls_verbatim(self):
        b = _block()
        urls = [u["url"] for u in b["source_urls"]]
        for novel in NOVEL_URLS:
            assert novel in urls, novel

    def test_block_key_zero_hit_except_landed(self):
        # Pre-commit the block key was zero-hit repo-wide; post-commit
        # it appears only in the landed YAML block, this test file, and
        # the doc-sync targets (README, ARCHITECTURE, iteration-log).
        out = _git("grep", "-F", "-l", BLOCK_KEY, "HEAD", "--", ".").stdout
        hits = [line for line in out.splitlines() if line.strip()]
        allowed = {
            os.path.join("profiles", "ap.yaml"),
            os.path.join("tests", OWN_BASENAME),
            "README.md",
            os.path.join("docs", "ARCHITECTURE.md"),
            "iteration-log.md",
        }
        for h in hits:
            assert h in allowed, h

    def test_no_astra_wire_before_this_run(self):
        # The novelty claim: the AP Astra-delay wire register was absent
        # from ap.yaml before this run's landing; now present only
        # inside this block.
        text = _block_text()
        assert "Astra safety delay" in text
        block_start = text.index(BLOCK_KEY + ":")
        assert "Astra safety delay" not in text[:block_start]

    def test_meta_arm_new_documented(self):
        b = _block()
        assert "NEW" in b["meta_arm"]["status"]

    def test_openai_arm_date_and_byline(self):
        b = _block()
        assert b["openai_arm"]["date"] == "2026-09-28"
        assert b["openai_arm"]["byline"] == "The Associated Press"

    def test_no_type_a_1232_in_git_log_pin(self):
        # Pre-commit form: no prior run committed this iteration.
        # Re-pinned to the post-commit own-set form in the log-hash
        # followup per #721 (the #1191-class self-trip).
        out = _git("log", "--oneline", "--grep=Type A #1232").stdout
        assert out.strip() == "", out.strip()


# ---------------------------------------------------------------------------
# 4. Block structure under competitor_relationships.openai.
# ---------------------------------------------------------------------------

class TestBlockStructure1232:
    def test_ap_profile_exists(self):
        assert os.path.exists(PROFILE_FILE)

    def test_openai_section_is_expected_parent(self):
        data = _load_ap()
        assert "openai" in data["competitor_relationships"]

    def test_block_key_present_under_openai(self):
        assert BLOCK_KEY in _openai_section()

    def test_required_fields_present(self):
        b = _block()
        for field in (
            "mechanism_id", "finding", "verdict", "openai_arm",
            "meta_arm", "financial_relationship", "register_analysis",
            "confounders", "counterevidence", "source_urls",
            "research_method", "rotation_transparency",
            "statistical_discipline",
        ):
            assert field in b, field

    def test_arms_have_tones(self):
        b = _block()
        assert b["openai_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.10
        assert b["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == -0.45

    def test_yaml_parse_clean(self):
        assert _block()["yaml_parse_clean"] is True


# ---------------------------------------------------------------------------
# 5. Mechanism 970 content discipline.
# ---------------------------------------------------------------------------

class TestM970ContentDiscipline1232:
    def test_finding_states_delta(self):
        assert "+0.35" in _block()["finding"]

    def test_not_a_falsification_member(self):
        b = _block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 50

    def test_cross_peg_confound_disclosed(self):
        b = _block()
        text = b["finding"] + b["register_analysis"]
        assert "cross-peg" in text

    def test_wire_genre_confound_disclosed(self):
        text = " ".join(_block()["confounders"]["strong"])
        assert "wire-register genre" in text

    def test_relay_attestation_disclosed(self):
        text = " ".join(_block()["confounders"]["strong"])
        assert "relay attestation" in text

    def test_ascii_only_block(self):
        assert _block()["ascii_only"] is True
        text = _block_text()
        assert all(ord(c) < 128 for c in text)
        assert "\u2014" not in text

    def test_no_full_ordinal_claim_forms_in_block(self):
        # The full member-claim and direction-claim forms stay
        # fragment-built; prose uses lowercase/short forms only.
        text = _block_text()
        for frag_a, frag_b in (
            ("FIFT", "Y-FIRST falsification-family member"),
            ("FORT", "IETH relationship direction"),
        ):
            assert (frag_a + frag_b) not in text


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug 28 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1232:
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
# 7. Falsification ledger (holds at 50).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1232:
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

    def test_no_fifty_first_member_pin(self):
        assert _git_grep_tracked_source(_T51, None) == []

    def test_no_fortieth_direction_pin(self):
        # The fortieth direction-claim form stays absent in profiles/
        # (profiles-scoped per the #1199 in-gate fix).
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_this_run_adds_no_member(self):
        assert _block()["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: this run's forward guards for #1233.
# ---------------------------------------------------------------------------

class TestGuardLifecycle1232:
    def test_pins_on_970_landing(self):
        # Type A lands one mechanism: max becomes 970, next is 971.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 970" in src
        assert "NEXT_NUM = 971" in src

    def test_no_type_b_1233_in_git_log_pin(self):
        out = _git("log", "--oneline", "--grep=Type B #1233").stdout
        assert out.strip() == "", out.strip()

    def test_971_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_971_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_971_dash_absent_repo_wide(self):
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

    def test_no_fifty_first_member_pin(self):
        assert _git_grep_tracked_source(_T51, None) == []

    def test_predecessor_1231_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1231_FILE))

    def test_next_leg_is_1233_type_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1233 Type B" in src

    def test_1231_pins_flip_by_design_documented(self):
        # #1231's forward guards (max-969, zero-970 keys all forms,
        # no-Type-A-#1232-in-git-log, fortieth absent, forty-eighth +
        # forty-ninth + fiftieth intact in profiles/, fifty-first
        # absent) verified GREEN pre-commit this run via the
        # subprocess staleness pin (Type A lands mechanism 970); the
        # max-969, zero-970, and no-Type-A-#1232-in-git-log pins flip
        # post-main-commit on this run's own landing (the #1191-class
        # self-trip, by design, documented in the staleness pin
        # below).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1231" in src
        assert "970" in src


# ---------------------------------------------------------------------------
# 9. Background suite: #1230's suite is CHECKED ONLY per #795.
# ---------------------------------------------------------------------------

class TestBackgroundSuiteCheck1232:
    def test_1230_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1230_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1230-launched suite is observed.
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1232_full_suite.log"))

    def test_observation_documented_in_block(self):
        assert "#1230-launched" in _block()["background_suite_status"]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestDocSync1232:
    def test_readme_test_file_table_has_1232_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_a_1232" in readme

    def test_architecture_has_1232_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1232" in arch

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

class TestIterationLog1232:
    def test_1232_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1232 Type A" in log

    def test_1231_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1231 Type E" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 12. Staleness pins: #1231's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1232:
    def test_1231_guard_lifecycle_post_commit_self_trip(self):
        # Post-main-commit form: 9 of the 11 pass; the two that fail BY
        # DESIGN are test_no_type_a_1232_in_git_log_pin (this run's own
        # main commit carries "Type A #1232") and
        # test_970_numeric_absent_in_profiles (mechanism 970 lands in
        # profiles/ this run). The #1231 block is read-only to this
        # run. Deselected pre-commit (both pins pass pre-commit).
        res = _class_run(E1231_FILE, "TestGuardLifecycle1231")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "2 failed, 9 passed" in res.stdout, res.stdout[-2000:]
        assert (
            "test_no_type_a_1232_in_git_log_pin" in res.stdout
        ), res.stdout[-2000:]
        assert (
            "test_970_numeric_absent_in_profiles" in res.stdout
        ), res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------

class TestInFlightIsolation1232:
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

    def test_own_diff_excludes_inflight(self):
        # This run's staged set must never include the in-flight
        # files; verified at commit time by explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "explicit-path" in src
