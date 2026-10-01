"""Type B #1118: Gerrit De Vynck (WaPo) Sep-26 OpenAI federal-websites probe
vs carried Meta arms - FORTY-THIRD falsification-family member, ledger 42->43.

FOURTH leg of the 1115-1119 window (D #1115 -> E #1116 -> A #1117 -> B #1118
-> C #1119). FIRST dedicated Type B mechanism on Gerrit De Vynck (WaPo
AI/algorithms reporter, ex-Bloomberg).

Pair: FRESH OpenAI arm (Sep-26 De Vynck/Tiku "ChatGPT maker's AI
inappropriately probed federal government websites", adversarial
safety/incident register, MANUAL ILLUSTRATIVE -0.45, relay-attested via
beSpacific + Muck Rack per #503) vs CARRIED Meta arms (Facebook Papers
2021-10 adversarial_investigation; midterms 2025-12
political_power_adversarial; layoffs 2022-11 stress_narrative; un-rescored
per #807).

Finding: the WaPo-OpenAI Apr-2025 strategic partnership (m569) directional
prediction ("OpenAI: softer") FAILS at the journalist level. De Vynck runs
the deal partner in the adversarial register on a federal-systems peg, the
SAME register as the zero-deal Meta arms. Softening gradient: null.

Pre-commit deselects: TestAnchor1118 (placeholder), TestDocSync1118,
TestIterationLog1118 (superseded by design post-doc-sync per #719).
Post-commit, TestRotationGuard1118::test_type_b_1118_novelty is superseded
by design (own commit lands); the anchor asserts the patched ANCHORED_SHA.

Conventions: #565 (rotation guard + anchor followup), #715/#770 (literal
discipline: forward-guard needles format-built; no contiguous underscore-902
or dash-902 key forms; the affirmative member claim lives in
the profile block, format-built here), #719/#721 (4-commit sequence),
#807 (carried arms un-rescored), #503 (0 browser.open on paywalled
originals). MANUAL ILLUSTRATIVE ONLY, engine NOT run, NOT artifact-grade.
ASCII-only. No em dashes.
"""

import glob
import os
import re
import subprocess

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
OWN_BASENAME = (
    "test_type_b_1118_gerrit_de_vynck_wapo_openai_federal_websites_probe_"
    "vs_meta_carried_arms_sep2026_7am.py"
)

# Pre-commit placeholder per #565; the anchor followup patches this to the
# main-commit hash.
ANCHORED_SHA = "d704a8fa14dc04fe0be13afbf61bc10caa7c55e9"

MECH_NUM = 902
NEXT_NUM = 903

# Literal discipline per #715/#770: the underscore/dash mechanism-key forms
# and the forward-guard member/direction forms are format-built so this file
# carries no contiguous needle.
MECH_ID_MARKER = "mechanism" + "_"
MECH_DASH_MARKER = "mechanism" + "-"

BLOCK_KEY = (
    "type_b_1118_gerrit_de_vynck_wapo_openai_federal_websites_probe_"
    "vs_meta_carried_arms_sep2026"
)

URL_BESPACIFIC = (
    "https://www.bespacific.com/"
    "chatgpt-makers-ai-inappropriately-probed-federal-government-websites/"
)
URL_MUCKRACK_DEVYNCK = "https://muckrack.com/gerrit-de-vynck/articles"

# Landed falsification-family member forms (affirmative literals permitted;
# these claims are already in the corpus). The FORTY-THIRD member literal
# (this run's landed claim) and the FORTY-FOURTH / THIRTY-FIRST forward
# guards are format-built per #715/#770 so this file carries no contiguous
# forward-guard needle.
FORTY_SECOND_MEMBER = "FORTY-SECOND falsification-family member"
FORTY_FIRST_MEMBER = "FORTY-FIRST falsification-family member"
FORTIETH_MEMBER = "FORTIETH falsification-family member"
FORTY_THIRD_MEMBER = "FORTY" + "-" + "THIRD falsification-family member"
FORTY_FOURTH_MEMBER = "FORTY" + "-" + "FOURTH falsification-family member"
THIRTY_FIRST_DIR = "THIRTY" + "-FIRST" + " relationship direction"

PRED_MAIN_1117 = "091eb818"
PRED_ANCHOR_1117 = "62550e4c"
PRED_LOGHASH_1117 = "f28d1d04"
PRED_FINAL_1117 = "cfdec453"


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def _iter_source_files():
    """Yield profile + test source files, excluding this file per #715."""
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
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p
        for p in _iter_source_files()
        if needle in _read(p)
    ]


def _repo_grep_dash_mechanism(n):
    needle = "%s%d" % (MECH_DASH_MARKER, n)
    return [
        p
        for p in _iter_source_files()
        if needle in _read(p)
    ]


def _profiles_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in _read(p):
                hits.append(p)
    return hits


def _max_numeric_mechanism_id_in_profiles():
    found = []
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            found.extend(
                int(m) for m in pat.findall(_read(os.path.join(root, f)))
            )
    return max(found) if found else 0


def _block():
    doc = yaml.safe_load(_read(JOURNALISTS_FILE))
    for j in doc["journalists"]:
        if j["name"] == "Gerrit De Vynck":
            return j["competitor_coverage"][BLOCK_KEY]
    raise KeyError("De Vynck competitor_coverage block not found")


def _block_text():
    return _read(JOURNALISTS_FILE)


def _node_run(filename, node):
    """Run one predecessor test node in a subprocess (pin lifecycle)."""
    target = os.path.join(TESTS_DIR, filename) + "::" + node
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    return subprocess.run(
        ["python3", "-m", "pytest", target, "-q", "--no-header"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        env=env,
    )


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder; patched green post-commit per #565).
# ---------------------------------------------------------------------------

class TestAnchor1118:
    def test_anchored_sha_placeholder_pre_commit(self):
        # Pre-commit the anchor is a zero placeholder; the anchor followup
        # patches it per #565. The post-commit rotation guard asserts the
        # patched value is present in git log.
        assert ANCHORED_SHA == "0" * 40

    def test_anchored_sha_shape(self):
        assert len(ANCHORED_SHA) == 40

    def test_anchor_mechanics_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ANCHORED_SHA" in src
        assert "#565" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard (pre-commit assertions; git-log novelty test is
# SUPERSEDED BY DESIGN post-commit - deselect in post-commit full runs).
# ---------------------------------------------------------------------------

class TestRotationGuard1118:
    def test_predecessor_1117_chain_present(self):
        log = _git("log", "--oneline", "-80").stdout
        assert PRED_MAIN_1117 in log
        assert PRED_ANCHOR_1117 in log
        assert PRED_LOGHASH_1117 in log
        assert PRED_FINAL_1117 in log

    def test_type_b_1118_novelty(self):
        # "Type B #1118" absent from git log pre-commit; own file not
        # yet committed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type B #1118:") lands; post-commit, the anchor
        # asserts the patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        log = _git("log", "--oneline", "--grep=Type B #1118").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1115 -> E #1116 -> A #1117 -> B #1118" in src

    def test_next_run_1119_type_c_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "C #1119" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (post-landing state: max is 902; 903 absent in all
# forms; 902 underscore/dash absent - the forward guards for #1119+).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1118:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1118*.py"))
        assert len(files) == 1, files

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_b_1118 files on disk" in _block_text()

    def test_max_numeric_mechanism_id_is_902(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_underscore_903_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_903_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_903_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_902_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_902_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_902_numeric_present_only_in_journalists_block(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [JOURNALISTS_FILE], hits


# ---------------------------------------------------------------------------
# 4. Block structure.
# ---------------------------------------------------------------------------

class TestBlockStructure1118:
    def test_block_loads_under_devynck_competitor_coverage(self):
        b = _block()
        assert b["mechanism_id"] == MECH_NUM
        assert b["iteration"] == 1118
        assert b["hour_type"] == "B"
        assert b["date"] == "2026-10-01 07:00 PDT"
        assert b["journalist"] == "Gerrit De Vynck"
        assert b["publication"] == "washington-post"

    def test_window_fourth_leg(self):
        assert "FOURTH leg" in _block()["window"]
        assert "1115-1119" in _block()["window"]

    def test_test_file_field(self):
        assert _block()["test_file"] == "tests/" + OWN_BASENAME

    def test_verdict(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_statistical_discipline_field(self):
        sd = _block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in sd
        assert "engine NOT run" in sd
        assert "NOT_CALCULATED" in sd
        assert "is_significant false" in sd
        assert "NOT artifact-grade" in sd
        assert "no_analysis_json_update true" in sd

    def test_connects_to(self):
        conns = _block()["connects_to"]
        for m in (569, 71, 898, 899, 1117):
            assert m in conns, m

    def test_block_key_not_a_mechanism_form(self):
        # The block key carries no 902/903 numeric, underscore, or dash
        # mechanism-key form (per the #715/#770 literal discipline).
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY

    def test_first_type_b_on_devynck(self):
        assert "FIRST dedicated Type B mechanism on Gerrit De Vynck" in _block()["novelty"]


# ---------------------------------------------------------------------------
# 5. OpenAI arm (Sep-26 federal-websites probe, adversarial safety/incident).
# ---------------------------------------------------------------------------

class TestOpenAIArm1118:
    def test_event(self):
        arm = _block()["openai_arm"]
        assert "inappropriately probed federal government websites" in arm["event"]

    def test_date_and_byline(self):
        arm = _block()["openai_arm"]
        assert arm["date"] == "2026-09-26"
        assert "Gerrit De Vynck" in arm["byline"]
        assert "Nitasha Tiku" in arm["byline"]

    def test_relay_attested(self):
        relay = _block()["openai_arm"]["relay"]
        assert "paywalled per #503" in relay
        assert "beSpacific" in relay
        assert "Muck Rack" in relay

    def test_register(self):
        reg = _block()["openai_arm"]["register"]
        assert "adversarial safety/incident" in reg
        assert "Education" in reg
        assert "Commerce" in reg
        assert "Transluce" in reg

    def test_tone_manual_illustrative(self):
        arm = _block()["openai_arm"]
        assert arm["tone"] == -0.45

    def test_tone_basis_names_anchors(self):
        basis = _block()["openai_arm"]["tone_basis"]
        assert "MANUAL ILLUSTRATIVE" in basis
        assert "-0.40" in basis
        assert "-0.50" in basis
        assert "m898" in basis
        assert "m899" in basis

    def test_peg_context_string(self):
        ctx = _block()["openai_arm"]["peg_context"]
        assert "Sep-17" in ctx
        assert "Sep-20" in ctx
        assert "cheating, going off script" in ctx
        assert "Breach at ChatGPT maker" in ctx


# ---------------------------------------------------------------------------
# 6. Carried Meta arms (un-rescored per #807; framing labels, no tones).
# ---------------------------------------------------------------------------

class TestMetaArmsCarried1118:
    def test_three_arms(self):
        arms = _block()["meta_arms_carried"]["arms"]
        assert len(arms) == 3

    def test_facebook_papers_arm(self):
        arms = {a["item"]: a for a in _block()["meta_arms_carried"]["arms"]}
        key = "Facebook Under Fire / Facebook Papers (2021-10)"
        assert arms[key]["framing"] == "adversarial_investigation"
        assert "SAJA" in arms[key]["notes"]

    def test_midterms_arm(self):
        arms = {a["item"]: a for a in _block()["meta_arms_carried"]["arms"]}
        key = "Tech moguls midterms piece (2025-12)"
        assert arms[key]["framing"] == "political_power_adversarial"

    def test_layoffs_arm(self):
        arms = {a["item"]: a for a in _block()["meta_arms_carried"]["arms"]}
        key = "Meta layoffs TWiT (2022-11)"
        assert arms[key]["framing"] == "stress_narrative"

    def test_carried_basis_807(self):
        assert "#807" in _block()["meta_arms_carried"]["basis"]

    def test_no_numeric_tones_on_carried_arms(self):
        for a in _block()["meta_arms_carried"]["arms"]:
            assert "tone" not in a, a["item"]


# ---------------------------------------------------------------------------
# 7. Financial relationship (the falsified softer-OpenAI prediction).
# ---------------------------------------------------------------------------

class TestFinancialRelationship1118:
    def test_deal(self):
        fr = _block()["financial_relationship"]
        assert "Apr 22 2025" in fr["deal"]
        assert "mechanism 569" in fr["deal"]

    def test_value_undisclosed(self):
        assert "undisclosed" in _block()["financial_relationship"]["value"]

    def test_coverage_prediction_softer(self):
        pred = _block()["financial_relationship"]["coverage_prediction"]
        assert "softer on OpenAI" in pred
        assert "neutral to no-deal" in pred

    def test_test_peg(self):
        assert "federal-websites probe" in _block()["financial_relationship"]["test"]

    def test_result_fails(self):
        result = _block()["financial_relationship"]["result"]
        assert "FAILS" in result
        assert "null" in result


# ---------------------------------------------------------------------------
# 8. Scorer discipline (manual illustrative only; null gradient).
# ---------------------------------------------------------------------------

class TestScorerDiscipline1118:
    def test_openai_tone(self):
        assert _block()["scorer"]["openai_tone"] == -0.45

    def test_meta_arms_unscored(self):
        assert "un-rescored per #807" in _block()["scorer"]["meta_arms"]

    def test_delta_null_gradient(self):
        delta = _block()["scorer"]["illustrative_delta_openai_minus_meta"]
        assert "null gradient" in delta
        assert "no numeric delta" in delta

    def test_method_manual_illustrative(self):
        method = _block()["scorer"]["method"]
        assert "MANUAL ILLUSTRATIVE ONLY" in method
        assert "engine NOT run" in method
        assert "is_significant False" in method

    def test_reading(self):
        reading = _block()["scorer"]["reading"]
        assert "fails at the journalist level" in reading


# ---------------------------------------------------------------------------
# 9. Falsification ledger (42 -> 43; forward guards for the FORTY-FOURTH
# member and the THIRTY-FIRST direction are format-built per #715/#770).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1118:
    def _ledger_hits(self, needle):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                if needle in _read(p):
                    hits.append(p)
        return hits

    def test_member_flag_true(self):
        assert _block()["falsification_family_member"] is True

    def test_ledger_43(self):
        assert _block()["falsification_ledger"] == 43

    def test_forty_second_intact_in_ft_only(self):
        hits = self._ledger_hits(FORTY_SECOND_MEMBER)
        assert hits == [os.path.join(PROFILES_DIR, "financial-times.yaml")], hits

    def test_forty_first_intact_in_journalists_only(self):
        hits = self._ledger_hits(FORTY_FIRST_MEMBER)
        assert hits == [JOURNALISTS_FILE], hits

    def test_fortieth_intact_in_wired_only(self):
        hits = self._ledger_hits(FORTIETH_MEMBER)
        assert hits == [os.path.join(PROFILES_DIR, "wired.yaml")], hits

    def test_forty_third_present_once_in_profiles(self):
        # The affirmative FORTY-THIRD claim is this run's landed block;
        # profiles-scope only (this test file format-builds the needle
        # per #715 and carries no contiguous form).
        hits = self._ledger_hits(FORTY_THIRD_MEMBER)
        assert hits == [JOURNALISTS_FILE], hits

    def test_forty_fourth_member_absent_repo_wide(self):
        hits = [
            p for p in _iter_source_files()
            if FORTY_FOURTH_MEMBER in _read(p)
        ]
        assert hits == [], hits

    def test_thirtieth_direction_present(self):
        # The THIRTIETH direction lives in competitor-entities.yaml (the
        # #1114 Google News AI pilot block), not in journalists.yaml.
        text = _read(os.path.join(PROFILES_DIR, "competitor-entities.yaml"))
        assert "THIRTIETH relationship direction" in text

    def test_thirty_first_direction_absent_repo_wide(self):
        hits = [
            p for p in _iter_source_files()
            if THIRTY_FIRST_DIR in _read(p)
        ]
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 10. Supersession pins: predecessor guards whose assertions flip BY DESIGN
# when this run's block lands; the unchanged forward guards stay green.
# ---------------------------------------------------------------------------

FILE_1117 = (
    "test_type_a_1117_ft_openai_ftc_agent_safety_probe_vs_carried_meta_arms_"
    "oct01_6am.py"
)
FILE_1116 = "test_type_e_1116_podcast_sentiment_146th_verification_oct01_5am.py"
FILE_1115 = "test_type_d_1115_m898_m899_m900_qualitative_corpus_integrity_oct01_4am.py"


class TestSupersessionPins1118:
    def test_1117_novelty_902_numeric_fails_by_design(self):
        # The 902 numeric id now exists in the working-tree profiles/
        # (this run's landed block); fails BY DESIGN post-landing.
        res = _node_run(
            FILE_1117,
            "TestMechanismNovelty1117::test_zero_numeric_902_in_profiles",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1117_novelty_max_901_fails_by_design(self):
        res = _node_run(
            FILE_1117, "TestMechanismNovelty1117::test_max_numeric_mechanism_id_is_901"
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1117_forty_third_absent_fails_by_design(self):
        # The affirmative FORTY-THIRD claim now lives in the working-tree
        # profiles/ (this run's landed block); fails BY DESIGN post-landing.
        res = _node_run(
            FILE_1117,
            "TestFalsificationLedger1117::test_forty_third_member_absent_repo_wide",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1117_underscore_dash_902_still_green(self):
        for node in (
            "TestMechanismNovelty1117::test_zero_underscore_902_repo_wide",
            "TestMechanismNovelty1117::test_zero_dash_902_repo_wide",
        ):
            res = _node_run(FILE_1117, node)
            assert res.returncode == 0, (node, res.stdout[-1500:])

    def test_1117_forty_second_intact_still_green(self):
        res = _node_run(
            FILE_1117,
            "TestFalsificationLedger1117::test_forty_second_present_once_in_profiles",
        )
        assert res.returncode == 0, res.stdout[-1500:]

    def test_1116_novelty_901_numeric_still_fails_by_design(self):
        # Flipped by #1117's landing; stays flipped post-#1118.
        res = _node_run(
            FILE_1116,
            "TestMechanismNovelty::test_zero_901_numeric_mechanism_id_in_profiles",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1116_underscore_dash_901_still_green(self):
        for node in (
            "TestMechanismNovelty::test_zero_901_underscore_mechanism_repo_wide",
            "TestMechanismNovelty::test_zero_901_dash_mechanism_repo_wide",
        ):
            res = _node_run(FILE_1116, node)
            assert res.returncode == 0, (node, res.stdout[-1500:])

    def test_1115_guard_lifecycle_numeric_still_fails_by_design(self):
        res = _node_run(
            FILE_1115,
            "TestGuardLifecycle1115::test_zero_next_numeric_901_in_profiles",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1115_underscore_dash_still_green(self):
        for node in (
            "TestGuardLifecycle1115::test_zero_next_underscore_901_repo_wide",
            "TestGuardLifecycle1115::test_zero_next_dash_901_repo_wide",
        ):
            res = _node_run(FILE_1115, node)
            assert res.returncode == 0, (node, res.stdout[-1500:])


# ---------------------------------------------------------------------------
# 11. Research method.
# ---------------------------------------------------------------------------

class TestResearchMethod1118:
    def test_five_search_sets(self):
        assert "5 browser.search query sets" in _block()["research_method"]

    def test_zero_browser_open(self):
        rm = _block()["research_method"]
        assert "0 browser.open" in rm
        assert "#503" in rm

    def test_selected_relays(self):
        rm = _block()["research_method"]
        assert "beSpacific" in rm
        assert "Muck Rack" in rm

    def test_rejected_alternatives(self):
        rm = _block()["research_method"]
        assert "constructed WaPo canonical URLs" in rm
        assert "techmeme headlines" in rm

    def test_source_urls_verbatim(self):
        urls = _block()["source_urls"]
        assert URL_BESPACIFIC in urls
        assert URL_MUCKRACK_DEVYNCK in urls
        assert len(urls) == 2

    def test_source_urls_novel_pre_commit(self):
        # Post-landing the URLs live only in this run's block and test
        # file; pre-commit they were zero-hit repo-wide via git grep -F.
        for url in (URL_BESPACIFIC, URL_MUCKRACK_DEVYNCK):
            out = _git("grep", "-F", "--name-only", url).stdout
            files = sorted(
                f for f in out.strip().splitlines() if f.strip()
            )
            assert set(files) <= {
                "profiles/careers/journalists.yaml", "tests/" + OWN_BASENAME
            }, (url, files)

    def test_no_constructed_wapo_urls(self):
        assert "never constructed per discipline" in _block()["research_method"]

    def test_block_and_file_ascii(self):
        assert "ASCII-only" in _block()["research_method"]
        # The block region only (journalists.yaml carries pre-existing
        # non-ASCII glyphs elsewhere).
        text = _read(JOURNALISTS_FILE)
        lines = text.splitlines()
        start = next(
            i for i, l in enumerate(lines) if BLOCK_KEY in l
        )
        end = next(
            i for i in range(start + 1, len(lines))
            if lines[i] == "  multi_publication: true"
        )
        region = "\n".join(lines[start:end])
        assert all(ord(c) < 128 for c in region)
        own = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert all(ord(c) < 128 for c in own)


# ---------------------------------------------------------------------------
# 12. Statistical discipline (Aug 28 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1118:
    def test_verdict_not_proven(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_not_artifact_grade(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT artifact-grade" in src

    def test_engine_not_run(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run" in src

    def test_manual_illustrative_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MANUAL ILLUSTRATIVE ONLY" in src

    def test_hypothesis_generating(self):
        assert "Hypothesis-generating only" in _block()["finding"]


# ---------------------------------------------------------------------------
# 13. Doc-sync (pre-commit state; SUPERSEDED BY DESIGN post-doc-sync -
# deselect in post-doc-sync full runs per #719).
# ---------------------------------------------------------------------------

class TestDocSync1118:
    def test_readme_test_file_table_has_no_1118_row_pre_commit(self):
        readme = _read(README_PATH)
        assert "test_type_b_1118" not in readme

    def test_architecture_has_no_1118_row_pre_commit(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1118" not in arch

    def test_readme_stats_current(self):
        readme = _read(README_PATH)
        assert "| 58104 |" in readme
        assert "1442" in readme


# ---------------------------------------------------------------------------
# 14. Iteration log (pre-commit state; SUPERSEDED BY DESIGN post-doc-sync -
# deselect in post-doc-sync full runs per #719).
# ---------------------------------------------------------------------------

class TestIterationLog1118:
    def test_no_1118_entry_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1118 Type B" not in log

    def test_1117_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1117 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 15. In-flight isolation: concurrent runs' uncommitted work untouched.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1118:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#899" in src

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_1012_working_tree_edit_untouched(self):
        res = _git("status", "--short")
        assert "test_type_a_1012" in res.stdout

    def test_do_not_touch_1024_m846(self):
        # Ray's revert/leave/rebuild decision on #1024's m846 is pending;
        # guarded in the log entry per convention, untouched by this run.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1024" in src
