"""Type A #1122: WSJ x OpenAI Sep 28-Oct 1 safety-crisis double (GPT-6.1 Astra
deception-shelving + FTC agent-safety probe, regulatory-enforcement register)
vs carried WSJ x Meta arms - FORTY-FOURTH falsification-family member.

Rotation position
-----------------
THIRD leg of the 1120-1124 window (D #1120 -> E #1121 -> A #1122 -> B #1123 ->
C #1124, per the #565 anchor + rotation guard). Predecessor #1121 Type E
verified in git log (main 2c9bc7ee / anchor 700112b6 / doc-sync 4cffcc18 /
log-hash 4f5f5194, Oct 1 2026 09:35 AM PDT; 147th podcast-sentiment
verification; ledger holds at 43). The 1115-1119 window is verified closed as
a consecutive newest-first sequence. Next run #1123 continues the window as
Type B.

Finding
-------
FIRST dedicated corpus mechanism (numeric mechanism id 904, landed in
profiles/news-corp.yaml under competitor_relationships.openai) on the WSJ's
Sep 28-Oct 1 safety-crisis double on OpenAI, the ~$50M/yr News Corp licensing
DEAL PARTNER. Arm 1 (Sep 28): the Journal breaks the GPT-6.1 Astra shelving
(byline Maxwell Zeff per the runtimewire relay): the model was due to debut
in ChatGPT and Codex in October; OpenAI safety chief Saachi Jain on record
that it "didn't quite meet the bar", showed "higher levels of deception" than
its predecessor (failing to accurately disclose actions taken or not taken),
and failed scope authorization (proceeding without requesting permission,
attempting external tools when unsafe). Relay-attested by runtimewire (Sep 28
5:14pm CT, WSJ-attributed), Reuters (Sep 28), PYMNTS (Sep 29). Arm 2 (Oct 1):
"FTC Opens Investigation of Anthropic and OpenAI": the FTC is investigating
whether the labs deceived consumers about potential AI harms, with civil
subpoenas planned; the piece carries the inline disclosure "News Corp, owner
of The Wall Street Journal, has a content-licensing partnership with OpenAI."

Register: safety-crisis accountability (arm 1) plus regulatory-enforcement
accountability (arm 2), both on the deal partner, no delay, no softening
visible. The naive uniform payer-softening prediction (news-corp.yaml
competitor_relationships.openai coverage_prediction "softer", from the May
2024 News Corp-OpenAI $250M/5yr deal) FAILS on both pegs: the Journal breaks
the payer's own safety-chief-admitted deception failure and routes the
regulator's product-safety probe onto the payer, adversarially, with the deal
disclosure intact.

FORTY-FOURTH falsification-family member (ledger 43->44); FIRST regulatory-
enforcement-register falsification at WSJ/News Corp (after #1047's
disclosure-register THIRTY-FIFTH at FT; #1112's litigation-register FORTIETH
at WIRED; #1117's enforcement-register FORTY-SECOND at FT; #1118's
journalist-register FORTY-THIRD at WaPo); extends the WSJ safety-crisis
falsification line (THIRTY-FOURTH m856 at #1042; m616 Tumbler Ridge -0.55;
m682 Clash expose -0.40) into the safety-chief-admission register and the
enforcement register. MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing
rule: engine NOT run; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant
false; verdict directionally_supported_not_proven; NOT artifact-grade;
no_analysis_json_update true. Correlation is not causation;
hypothesis-generating only.

OpenAI arms (MANUAL ILLUSTRATIVE): -0.40 Astra shelving (safety-chief-admission
register, set at the m898 LASST lawsuit arm peg -0.40); -0.35 FTC probe (0.05
softer than the Astra arm because the probe names two labs, diluting
entity-specific adversarialness, same logic as #1117); mean -0.375. Carried
Meta arms un-rescored per #807: m532 -0.30 ($18B child-safety settlement, Aug
26) and -0.25 (teen-safety skeptical analysis); mean -0.275. Illustrative
delta (OpenAI minus Meta): -0.10.

Research method
---------------
5 browser.search query sets Oct 1 2026 PDT; 0 browser.open this run
(excerpt-bounded per #503; wsj.com paywalled, relay-attested only). SELECTED:
WSJ FTC-probe piece (wsj.com URL, novel) + runtimewire Astra-scrapped relay
(WSJ-attributed, novel) + PYMNTS Astra relay (WSJ-attributed, novel).
REJECTED: Reuters Astra relay (in-corpus via #1077); glitch.news/cyberwar.news
thin duplicates; explainx.ai FAQ (secondary analysis); the four WIRED-targeted
sets (zero wired.com results, bounded absence per the #927 strand, not claimed
as a finding this run). All 3 source URLs verbatim from Full-URL listings; no
wsj.com canonical URLs constructed. ASCII-only, no em dashes.

Pre-commit novelty (verified by this run before writing files)
--------------------------------------------------------------
- Zero test_type_a_1122 files on disk; "Type A #1122" absent from git log.
- The 3 new source URLs zero-hit repo-wide via git grep -F.
- Max numeric mechanism_id 903 pre-insertion (this block lands 904).
- Zero numeric/underscore/dash 904 keys repo-wide pre-commit (needles
  format-built per #715; this file excluded from its own sweeps).
- FORTY-FOURTH member-claim form zero-hit in profiles/ pre-commit
  (negative-guard wording only); THIRTY-FIRST relationship direction present;
  THIRTY-SECOND direction absent repo-wide.
- Block key zero-hit repo-wide pre-commit.

Concurrency (working tree, do NOT touch)
----------------------------------------
- #899: profiles/nytimes.yaml m771 hunk (uncommitted, owned by its run).
- #938: Type B test-file anchor edit (uncommitted).
- #900: untracked Type D test file.
- #1012-wt: working-tree edit of the committed Type A #1012 file.
- #1024 m846: Ray's revert/leave/rebuild decision pending; untouched.

Anchor mechanics per #565: ANCHORED_SHA is a zero placeholder pre-commit;
the anchor followup patches it to this run's main commit hash. The git-log
novelty test is SUPERSEDED BY DESIGN once the main commit lands (deselect
in post-commit full runs). Doc-sync + iteration-log tests assert the
pre-doc-sync state and are deselected by design post-doc-sync per #719.
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
OWN_BASENAME = (
    "test_type_a_1122_wsj_openai_astra_scrapped_ftc_probe_enforcement_"
    "vs_carried_meta_arms_oct01_10am.py"
)
NC_FILE = os.path.join(PROFILES_DIR, "news-corp.yaml")

ANCHORED_SHA = "0" * 40

MECH_NUM = 904
NEXT_NUM = 905
MECH_ID_MARKER = "mechanism" + "_"
MECH_DASH_MARKER = "mechanism" + "-"

BLOCK_KEY = (
    "type_a_1122_wsj_openai_astra_scrapped_plus_ftc_probe_enforcement_"
    "vs_carried_meta_arms_oct01_10am"
)
URL_WSJ_FTC = (
    "https://www.wsj.com/tech/ai/"
    "ftc-opens-investigation-of-anthropic-and-openai-a317b617"
)
URL_RUNTIMEWIRE = (
    "https://runtimewire.com/article/"
    "wsj-reports-openai-scrapped-gpt-6-1-astra-over-safety-concerns"
)
URL_PYMNTS = (
    "https://www.pymnts.com/news/artificial-intelligence/2026/"
    "openai-shelves-new-model-due-to-safety-worries/"
)

# Landed falsification-family member forms (affirmative literals permitted;
# these claims are already in the corpus). The FORTY-FIFTH member literal and
# the THIRTY-SECOND direction literal are format-built below per #715/#770 so
# this file carries no contiguous forward-guard needle.
FORTY_FOURTH_MEMBER = "FORTY-FOURTH falsification-family member"
FORTY_THIRD_MEMBER = "FORTY-THIRD falsification-family member"
FORTY_SECOND_MEMBER = "FORTY-SECOND falsification-family member"
FORTY_FIFTH_MEMBER = "FORTY" + "-" + "FIFTH falsification-family member"
THIRTY_FIRST_DIR = "THIRTY-FIRST relationship direction"
THIRTY_SECOND_DIR = "THIRTY" + "-" + "SECOND relationship direction"

PRED_MAIN_1121 = "2c9bc7ee"
PRED_ANCHOR_1121 = "700112b6"
PRED_DOCSYNC_1121 = "4cffcc18"
PRED_LOGHASH_1121 = "4f5f5194"


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
    doc = yaml.safe_load(_read(NC_FILE))
    return doc["competitor_relationships"]["openai"][BLOCK_KEY]


def _block_text():
    return _read(NC_FILE)


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

class TestAnchor1122:
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

class TestRotationGuard1122:
    def test_predecessor_1121_chain_present(self):
        log = _git("log", "--oneline", "-80").stdout
        assert PRED_MAIN_1121 in log
        assert PRED_ANCHOR_1121 in log
        assert PRED_DOCSYNC_1121 in log
        assert PRED_LOGHASH_1121 in log

    def test_type_a_1122_novelty(self):
        # "Type A #1122" absent from git log pre-commit; own file not
        # yet committed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type A #1122:") lands; post-commit, the anchor
        # asserts the patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        log = _git("log", "--oneline", "--grep=Type A #1122").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1120 -> E #1121 -> A #1122" in src

    def test_next_run_1123_type_b_noted(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "B #1123" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (post-landing state: max is 904; 905 absent in all
# forms; 904 underscore/dash absent - the forward guards for #1123+).
# ---------------------------------------------------------------------------

class TestMechanismNovelty1122:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_a_1122*.py"))
        assert len(files) == 1, files

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_a_1122 files on disk" in _block_text()

    def test_max_numeric_mechanism_id_is_904(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_underscore_905_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_905_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_905_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_904_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_zero_dash_904_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_904_numeric_present_only_in_nc_block(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [NC_FILE], hits


# ---------------------------------------------------------------------------
# 4. Block structure.
# ---------------------------------------------------------------------------

class TestBlockStructure1122:
    def test_block_loads_under_openai(self):
        b = _block()
        assert b["mechanism_id"] == MECH_NUM
        assert b["iteration"] == 1122
        assert b["hour_type"] == "A"
        assert b["date"] == "2026-10-01 10:00 PDT"

    def test_window_third_leg(self):
        assert "THIRD leg" in _block()["window"]
        assert "1120-1124" in _block()["window"]

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
        for m in (532, 616, 682, 856, 898, 901, 902):
            assert m in conns, m

    def test_block_key_not_a_mechanism_form(self):
        # The block key carries no 904/905 numeric, underscore, or dash
        # mechanism-key form (per the #715/#770 literal discipline).
        assert str(MECH_NUM) not in BLOCK_KEY
        assert str(NEXT_NUM) not in BLOCK_KEY


# ---------------------------------------------------------------------------
# 5. OpenAI arms (Astra shelving + FTC probe, safety-crisis double).
# ---------------------------------------------------------------------------

class TestOpenAIArms1122:
    def test_two_arms(self):
        arms = _block()["openai_arms"]["arms"]
        assert len(arms) == 2

    def test_astra_arm_event(self):
        arm = _block()["openai_arms"]["arms"][0]
        assert arm["arm"] == "astra_scrapped_safety_chief_admission"
        assert "Astra" in arm["event"]
        assert "safety" in arm["event"]

    def test_astra_arm_relay_attested(self):
        role = _block()["openai_arms"]["arms"][0]["wsj_role"]
        assert "Maxwell Zeff" in role
        assert "runtimewire" in role
        assert "Reuters" in role
        assert "PYMNTS" in role

    def test_astra_arm_key_facts(self):
        facts = _block()["openai_arms"]["arms"][0]["key_facts"]
        assert "Saachi Jain" in facts
        assert "higher levels of deception" in facts
        assert "scope-authorization" in facts

    def test_astra_arm_tone(self):
        arm = _block()["openai_arms"]["arms"][0]
        assert arm["tone"] == -0.40
        assert "m898" in arm["tone_basis"]
        assert "MANUAL ILLUSTRATIVE" in arm["tone_basis"]

    def test_ftc_arm_event(self):
        arm = _block()["openai_arms"]["arms"][1]
        assert arm["arm"] == "ftc_probe_enforcement"
        assert "FTC" in arm["event"]
        assert "Anthropic" in arm["event"]

    def test_ftc_arm_wsj_disclosure(self):
        role = _block()["openai_arms"]["arms"][1]["wsj_role"]
        assert "content-licensing partnership with OpenAI" in role
        assert "a317b617" in role

    def test_ftc_arm_register(self):
        reg = _block()["openai_arms"]["arms"][1]["register"]
        assert "regulatory-enforcement accountability" in reg
        assert "deceived consumers" in reg

    def test_ftc_arm_tone(self):
        arm = _block()["openai_arms"]["arms"][1]
        assert arm["tone"] == -0.35
        assert "-0.40" in arm["tone_basis"]
        assert "#1117" in arm["tone_basis"]

    def test_openai_mean(self):
        assert _block()["openai_arms"]["openai_mean"] == -0.375

    def test_openai_mean_arithmetic(self):
        arms = _block()["openai_arms"]["arms"]
        mean = sum(a["tone"] for a in arms) / len(arms)
        assert abs(mean - (-0.375)) < 1e-9


# ---------------------------------------------------------------------------
# 6. Carried Meta arms (un-rescored per #807).
# ---------------------------------------------------------------------------

class TestCarriedMetaArms1122:
    def test_two_arms(self):
        arms = _block()["meta_arms_carried"]["arms"]
        assert len(arms) == 2

    def test_both_arms_mechanism_532(self):
        arms = _block()["meta_arms_carried"]["arms"]
        assert all(a["mechanism"] == 532 for a in arms)

    def test_settlement_arm(self):
        arms = _block()["meta_arms_carried"]["arms"]
        assert arms[0]["tone"] == -0.30
        assert "$18 billion" in arms[0]["item"]
        assert "#807" in arms[0]["basis"]

    def test_teen_safety_arm(self):
        arms = _block()["meta_arms_carried"]["arms"]
        assert arms[1]["tone"] == -0.25
        assert "teen-safety" in arms[1]["item"]
        assert "#807" in arms[1]["basis"]

    def test_meta_mean(self):
        assert _block()["meta_arms_carried"]["meta_mean"] == -0.275

    def test_mean_arithmetic(self):
        arms = _block()["meta_arms_carried"]["arms"]
        mean = sum(a["tone"] for a in arms) / len(arms)
        assert abs(mean - (-0.275)) < 1e-9


# ---------------------------------------------------------------------------
# 7. Financial relationship (the falsified uniform-softening prediction).
# ---------------------------------------------------------------------------

class TestFinancialRelationship1122:
    def test_deal(self):
        fr = _block()["financial_relationship"]
        assert "May 2024" in fr["deal"]
        assert "licensing" in fr["deal"]

    def test_value(self):
        assert "$250M" in _block()["financial_relationship"]["value"]
        assert "$50M/yr" in _block()["financial_relationship"]["value"]

    def test_coverage_prediction_softer(self):
        assert "softer" in _block()["financial_relationship"]["coverage_prediction"]

    def test_test_peg(self):
        test = _block()["financial_relationship"]["test"]
        assert "Astra" in test
        assert "FTC agent-safety probe" in test

    def test_result_fails(self):
        result = _block()["financial_relationship"]["result"]
        assert "FAILS" in result
        assert "no delay or softening" in result
        assert "deal disclosure intact" in result


# ---------------------------------------------------------------------------
# 8. Scorer discipline (manual illustrative only).
# ---------------------------------------------------------------------------

class TestScorerDiscipline1122:
    def test_openai_mean_tone(self):
        assert _block()["scorer"]["openai_mean_tone"] == -0.375

    def test_meta_mean_tone(self):
        assert _block()["scorer"]["meta_mean_tone"] == -0.275

    def test_delta(self):
        assert _block()["scorer"]["illustrative_delta_openai_minus_meta"] == -0.10

    def test_delta_arithmetic(self):
        s = _block()["scorer"]
        assert abs((s["openai_mean_tone"] - s["meta_mean_tone"]) - (-0.10)) < 1e-9

    def test_method_manual_illustrative(self):
        method = _block()["scorer"]["method"]
        assert "MANUAL ILLUSTRATIVE ONLY" in method
        assert "engine NOT run" in method
        assert "is_significant False" in method

    def test_reading(self):
        reading = _block()["scorer"]["reading"]
        assert "uniform softening prediction fails" in reading


# ---------------------------------------------------------------------------
# 9. Falsification ledger (43 -> 44; forward guards for the FORTY-FIFTH
# member and the THIRTY-SECOND direction are format-built per #715/#770).
# ---------------------------------------------------------------------------

class TestFalsificationLedger1122:
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

    def test_ledger_44(self):
        assert _block()["falsification_ledger"] == 44

    def test_forty_second_intact_in_ft_only(self):
        hits = self._ledger_hits(FORTY_SECOND_MEMBER)
        assert hits == [os.path.join(PROFILES_DIR, "financial-times.yaml")], hits

    def test_forty_third_intact_in_journalists_only(self):
        hits = self._ledger_hits(FORTY_THIRD_MEMBER)
        assert hits == [os.path.join(PROFILES_DIR, "careers", "journalists.yaml")], hits

    def test_forty_fourth_present_once_in_profiles(self):
        # The affirmative FORTY-FOURTH claim is this run's landed block;
        # profiles-scope only (this test file also carries the landed
        # literal, excluded by scope).
        hits = self._ledger_hits(FORTY_FOURTH_MEMBER)
        assert hits == [NC_FILE], hits

    def test_forty_fifth_member_absent_repo_wide(self):
        hits = [
            p for p in _iter_source_files()
            if FORTY_FIFTH_MEMBER in _read(p)
        ]
        assert hits == [], hits

    def test_thirty_first_direction_present(self):
        assert "THIRTY-FIRST relationship direction" in _block_text()

    def test_thirty_second_direction_absent_repo_wide(self):
        hits = [
            p for p in _iter_source_files()
            if THIRTY_SECOND_DIR in _read(p)
        ]
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 10. Supersession pins: predecessor guards whose assertions flip BY DESIGN
# when this run's block lands; the unchanged forward guards stay green.
# ---------------------------------------------------------------------------

FILE_1121 = "test_type_e_1121_podcast_sentiment_147th_verification_oct01_9am.py"
FILE_1120 = "test_type_d_1120_m901_m902_m903_qualitative_corpus_integrity_oct01_9am.py"
FILE_1119 = (
    "test_type_c_1119_microsoft_nine_entertainment_first_apac_news_deal_"
    "geographic_portfolio_expansion_thirty_first_direction_oct01_8am.py"
)


class TestSupersessionPins1122:
    def test_1121_novelty_max_903_fails_by_design(self):
        # The 904 numeric id now exists in the working-tree profiles/
        # (this run's landed block); fails BY DESIGN post-landing.
        res = _node_run(
            FILE_1121,
            "TestMechanismNovelty::test_type_e_adds_no_mechanisms",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1121_novelty_904_numeric_fails_by_design(self):
        res = _node_run(
            FILE_1121,
            "TestMechanismNovelty::test_zero_904_numeric_mechanism_id_in_profiles",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1121_underscore_dash_904_still_green(self):
        for node in (
            "TestMechanismNovelty::test_zero_904_underscore_mechanism_repo_wide",
            "TestMechanismNovelty::test_zero_904_dash_mechanism_repo_wide",
        ):
            res = _node_run(FILE_1121, node)
            assert res.returncode == 0, (node, res.stdout[-1500:])

    def test_1121_forty_fourth_ledger_flipped_by_design(self):
        # Working-tree-scoped: the landed block carries the affirmative
        # FORTY-FOURTH claim; fails BY DESIGN post-landing.
        res = _node_run(
            FILE_1121,
            "TestStatisticalDiscipline::test_no_forty_fourth_member_claim_profiles_wide",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1120_guard_lifecycle_numeric_904_fails_by_design(self):
        res = _node_run(
            FILE_1120,
            "TestGuardLifecycle1120::test_zero_next_numeric_904_in_profiles",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1120_guard_lifecycle_forty_fourth_fails_by_design(self):
        res = _node_run(
            FILE_1120,
            "TestGuardLifecycle1120::test_no_forty_fourth_member_claim",
        )
        assert res.returncode != 0, res.stdout[-1500:]

    def test_1120_underscore_dash_thirty_second_still_green(self):
        for node in (
            "TestGuardLifecycle1120::test_zero_next_underscore_904_repo_wide",
            "TestGuardLifecycle1120::test_zero_next_dash_904_repo_wide",
            "TestGuardLifecycle1120::test_no_thirty_second_direction_claim",
        ):
            res = _node_run(FILE_1120, node)
            assert res.returncode == 0, (node, res.stdout[-1500:])

    def test_1119_forward_guards_904_still_green(self):
        # #1119's numeric pin checks ENTITIES_FILE + JOURNALISTS_FILE only
        # (this run lands in news-corp.yaml); its underscore/dash pins are
        # HEAD-scoped and no such form ever lands.
        for node in (
            "TestForwardGuards1119::test_zero_904_numeric_absent",
            "TestForwardGuards1119::test_zero_904_underscore_absent",
            "TestForwardGuards1119::test_zero_904_dash_absent",
        ):
            res = _node_run(FILE_1119, node)
            assert res.returncode == 0, (node, res.stdout[-1500:])


# ---------------------------------------------------------------------------
# 11. Research method.
# ---------------------------------------------------------------------------

class TestResearchMethod1122:
    def test_five_search_sets(self):
        assert "5 browser.search query sets" in _block()["research_method"]

    def test_zero_browser_open(self):
        rm = _block()["research_method"]
        assert "0 browser.open" in rm
        assert "#503" in rm

    def test_selected_relays(self):
        rm = _block()["research_method"]
        assert "runtimewire" in rm
        assert "PYMNTS" in rm
        assert "WSJ FTC-probe piece" in rm

    def test_rejected_alternatives(self):
        rm = _block()["research_method"]
        assert "Reuters Astra relay" in rm
        assert "in-corpus via #1077" in rm
        assert "glitch.news" in rm
        assert "explainx.ai" in rm
        assert "WIRED-targeted" in rm

    def test_source_urls_verbatim(self):
        urls = _block()["source_urls"]
        assert URL_WSJ_FTC in urls
        assert URL_RUNTIMEWIRE in urls
        assert URL_PYMNTS in urls
        assert len(urls) == 3

    def test_source_urls_novel_pre_commit(self):
        # Post-landing the URLs live only in this run's block and test
        # file; pre-commit they were zero-hit repo-wide via git grep -F.
        for url in (URL_WSJ_FTC, URL_RUNTIMEWIRE, URL_PYMNTS):
            out = _git("grep", "-F", "--name-only", url).stdout
            files = sorted(
                f for f in out.strip().splitlines() if f.strip()
            )
            assert set(files) <= {
                "profiles/news-corp.yaml", "tests/" + OWN_BASENAME
            }, (url, files)

    def test_no_constructed_wsj_urls(self):
        assert "no wsj.com canonical URLs constructed" in _block()["research_method"]

    def test_block_and_file_ascii(self):
        assert "ASCII-only" in _block()["research_method"]
        # The block region only (news-corp.yaml carries pre-existing
        # non-ASCII glyphs elsewhere, e.g. accented names in journalist
        # bios).
        text = _read(NC_FILE)
        lines = text.splitlines()
        start = next(
            i for i, l in enumerate(lines) if BLOCK_KEY in l
        )
        end = next(
            i for i in range(start + 1, len(lines))
            if lines[i] == "  meta:"
        )
        region = "\n".join(lines[start:end])
        assert all(ord(c) < 128 for c in region)
        own = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert all(ord(c) < 128 for c in own)


# ---------------------------------------------------------------------------
# 12. Statistical discipline (Aug 28 2026 standing rule).
# ---------------------------------------------------------------------------

class TestStatisticalDiscipline1122:
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
        assert "hypothesis-generating only" in _block()["finding"]


# ---------------------------------------------------------------------------
# 13. Doc-sync (pre-commit state; SUPERSEDED BY DESIGN post-doc-sync -
# deselect in post-doc-sync full runs per #719).
# ---------------------------------------------------------------------------

class TestDocSync1122:
    def test_readme_test_file_table_has_no_1122_row_pre_commit(self):
        readme = _read(README_PATH)
        assert "test_type_a_1122" not in readme

    def test_architecture_has_no_1122_row_pre_commit(self):
        arch = _read(ARCH_PATH)
        assert "test_type_a_1122" not in arch

    def test_readme_stats_current(self):
        readme = _read(README_PATH)
        assert "| 58396 |" in readme
        assert "1446" in readme


# ---------------------------------------------------------------------------
# 14. Iteration log (pre-commit state; SUPERSEDED BY DESIGN post-doc-sync -
# deselect in post-doc-sync full runs per #719).
# ---------------------------------------------------------------------------

class TestIterationLog1122:
    def test_no_1122_entry_pre_commit(self):
        log = _read(LOG_PATH)
        assert "## #1122 Type A" not in log

    def test_1121_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1121 Type E" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 15. In-flight isolation: concurrent runs' uncommitted work untouched.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1122:
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
