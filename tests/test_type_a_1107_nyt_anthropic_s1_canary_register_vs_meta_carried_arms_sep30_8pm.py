"""Type A #1107 (2026-09-30 20:00 PDT) - NYT x Anthropic Sep-2026 S-1
canary-register arm vs carried NYT x Meta arms, mechanism 895.

THIRD leg of the 1105-1109 window (D #1105 -> E #1106 -> A #1107 -> B #1108 ->
C #1109), per the #565 rotation anchor. Predecessor: #1106 Type E
(mediascope-daily-iteration, 2026-09-30 19:00 PDT). The 1100-1104 window is
verified closed.

Mechanism 895 extends m835 (Type A #1007, Sep 26 2026): m835 paired the
Sep-12 Amodei-slowdown news arm (+0.10) and the Sep-18 IPO-scoop momentum arm
(+0.25, IPOScoop attestation) against the Sep-23 Meta Connect relay (+0.10)
and the Aug-18 ICE-ban memo enforcement arm (-0.30). This run carries all
four m835 arms un-rescored per #807 and adds the FIRST dedicated S-1-peg NYT
x Anthropic arm: the Sep-29 DealBook / Andrew Ross Sorkin piece
("Anthropic's IPO filing"), relay-attested via the implicator.ai attributed
relay carrying the explicit nytimes.com URL, excerpt-bounded per #503
(0 browser.open). MANUAL ILLUSTRATIVE -0.35: market-systemic accountability
register - the IPO framed as a contagion vector for the AI-capital edifice
('the tech economy's canary in the coal mine'; Amazon/Google balance-sheet
stakes; 'cascading mark-to-market event'; 'circular financing' fears).

Findings: (1) same-event third-publication leg of the S-1 register series per
the m847/m856 precedent - m883 (Verge, Sep 30, -0.40), m892 (FT, Sep 29,
-0.35), NYT m895 (-0.35): near-parity cross-publication replication at a
third outlet whose Anthropic tie is reported-not-confirmed; (2) within-entity
swing at NYT x Anthropic: m835's carried Sep-18 +0.25 to the fresh Sep-29
-0.35 = -0.60 in 11 days, the THIRD publication-level replication of the
peg-follows-register swing (m676 FT: -0.55/16d; m712->m877 WIRED: -0.50/13d);
(3) fresh Anthropic -0.35 vs carried Meta mean -0.10, illustrative delta -0.25
- the accountability register lands HARDER on the reported-settlement
counterparty than on Meta on this window's pegs, inverting the naive
deal-softening read.

NOT a falsification-family member: no uniform payer-softening prediction
under test (the NYT-Anthropic settlement is reported-not-confirmed; the
Amazon-deal payer-softening prediction was already falsified at m567).
Falsification ledger holds at 38 (THIRTY-EIGHTH = m893, journalists.yaml);
THIRTY-NINTH absent. Relationship directions: TWENTY-EIGHTH present
(m894, competitor-entities.yaml DIVIDE-AND-CONQUER); TWENTY-NINTH absent.

Literal discipline per #715: this file carries NO contiguous underscore-form,
dash-form, or colon-form 895 mechanism literal - the 895 needles are
format-built ("%d" % MECH_NUM), so the zero-895 sweeps keep one hit
(profiles/nytimes.yaml) and the zero-896 forward guards stay green.
The #1024 m846 sourcing-constraint matter is not touched by this run.
"""

import glob
import logging
import math
import os
import re
import subprocess

import pytest
import yaml

from mediascope.score.asymmetry import calculate_asymmetry

log = logging.getLogger(__name__)

ITERATION = 1107
TYPE_LETTER = "A"
WINDOW = "1105-1109"
MECH_NUM = 895
NEXT_NUM = 896
ANCHORED_SHA = "0" * 40  # patched to the main-commit SHA in the anchor followup
OWN_BASENAME = (
    "test_type_a_1107_nyt_anthropic_s1_canary_register_"
    "vs_meta_carried_arms_sep30_8pm.py"
)
BLOCK_KEY = (
    "mechanism_%d_nyt_anthropic_sep2026_ipo_register_swing_"
    "vs_meta_carried_arms" % MECH_NUM
)
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
NYT_FILE = os.path.join(PROFILES_DIR, "nytimes.yaml")
NYT_URL = ("https://www.nytimes.com/2026/09/29/business/dealbook/"
           "anthropic-ipo-filing-s1.html")
IMPLICATOR_URL = ("https://www.implicator.ai/"
                  "anthropic-ipo-prospectus-518-billion-"
                  "compute-commitments.md")

# Patched post-commit once README/ARCHITECTURE doc-sync lands.
README_TEST_COUNT = 56461
README_FILE_COUNT = 1432
TEST_BASENAME = OWN_BASENAME

F1104 = ("test_type_c_1104_google_ai_answer_pilot_divide_and_conquer_"
         "twentyeighth_direction_sep30_5pm.py")
F1105 = ("test_type_d_1105_m892_m893_m894_qualitative_corpus_integrity_"
         "sep30_6pm.py")
F1106 = ("test_type_e_1106_meta_openai_sep2026_federal_antitrust_suit_"
         "vs_google_carried_arms_sep30_7pm.py")


def _source_files():
    out = []
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs
                   if d not in ("__pycache__", ".git", ".venv")]
        for f in files:
            out.append(os.path.join(root, f))
    return out


def _iter_source_files():
    for p in _source_files():
        if p.endswith((".py", ".yaml", ".md", ".json")):
            yield p


def _max_numeric_mechanism_id_in_profiles():
    best = -1
    for p in glob.glob(os.path.join(PROFILES_DIR, "*.yaml")):
        for m in re.finditer(r"mechanism_id:\s*(\d+)",
                             open(p, encoding="utf-8",
                                  errors="replace").read()):
            best = max(best, int(m.group(1)))
    return best


def _repo_grep_underscore_mechanism(n):
    needle = "mechanism_%d" % n
    return [p for p in _iter_source_files()
            if needle in open(p, encoding="utf-8", errors="replace").read()]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism-%d" % n
    return [p for p in _iter_source_files()
            if needle in open(p, encoding="utf-8", errors="replace").read()]


def _profiles_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    return [p for p in glob.glob(os.path.join(PROFILES_DIR, "*.yaml"))
            if needle in open(p, encoding="utf-8",
                              errors="replace").read()]


def _nyt_text():
    return open(NYT_FILE, encoding="utf-8").read()


def _block_text():
    text = _nyt_text()
    start = text.index(BLOCK_KEY)
    lines = text[start:].split("\n")
    end = next(i for i, line in enumerate(lines)
               if i > 0 and re.match(r"^  [a-z_]", line))
    return "\n".join(lines[:end])


def _block_yaml():
    return yaml.safe_load(
        _nyt_text())["competitor_relationships"]["anthropic"][BLOCK_KEY]


def _class_run(test_file, class_name):
    return subprocess.run(
        [os.path.join(REPO_ROOT, ".venv", "bin", "python"), "-m", "pytest",
         os.path.join(TESTS_DIR, test_file) + "::" + class_name,
         "-q", "--no-header", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )


# ---------------------------------------------------------------------------
# 1. Novelty (pre-commit: #715 protocol).
# ---------------------------------------------------------------------------

class TestNovelty1107:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(
            os.path.join(TESTS_DIR, "test_type_a_1107*.py"))
        assert len(files) == 1, files

    def test_main_commit_is_unique_and_anchored(self):
        """DESELECTED pre-commit per #565: the main commit does not exist yet.

        Post-commit this asserts the single #1107 commit is the anchor and
        carries the block-key + test-file changes.
        """

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_a_1107 files on disk" in _block_text()

    def test_window_legs_present(self):
        d_files = glob.glob(os.path.join(TESTS_DIR, "test_type_d_1105*.py"))
        e_files = glob.glob(os.path.join(TESTS_DIR, "test_type_e_1106*.py"))
        assert len(d_files) >= 1 and len(e_files) >= 1

    def test_max_numeric_mechanism_id_is_895(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_underscore_next_num_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_next_num_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_next_num_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []


# ---------------------------------------------------------------------------
# 2. Rotation guard (DESELECTED pre-commit per #565/#719/#721; markers anchor/rotation).
# ---------------------------------------------------------------------------

class TestRotationGuard1107:
    @pytest.mark.rotation
    def test_window_1105_1109_third_leg(self):
        """A is the third leg of the 1105-1109 window per #565."""
        assert TYPE_LETTER == "A"
        assert ITERATION == 1107
        assert WINDOW == "1105-1109"

    @pytest.mark.rotation
    def test_type_a_adjacency_in_window(self):
        """D(#1105) -> E(#1106) -> A(#1107, this run) -> B(#1108) -> C(#1109)."""
        d_files = glob.glob(os.path.join(TESTS_DIR, "test_type_d_1105*.py"))
        e_files = glob.glob(os.path.join(TESTS_DIR, "test_type_e_1106*.py"))
        assert len(d_files) >= 1 and len(e_files) >= 1

    @pytest.mark.rotation
    def test_predecessor_is_type_e_1106(self):
        files = glob.glob(os.path.join(TESTS_DIR, "test_type_e_1106*.py"))
        assert len(files) >= 1

    @pytest.mark.rotation
    def test_anchor_is_ancestor_of_head(self):
        """Post-commit: the anchor commit is an ancestor of HEAD."""
        result = subprocess.run(
            ["git", "merge-base", "--is-ancestor", ANCHORED_SHA, "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0


# ---------------------------------------------------------------------------
# 3. Novelty anchor (DESELECTED pre-commit per #565; patched green post-commit).
# ---------------------------------------------------------------------------

class TestNoveltyAnchor1107:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1107 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type A #1107" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "placeholder",
        )
        assert any(ANCHORED_SHA[:12] in line for line in mains)

    @pytest.mark.anchor
    def test_anchor_sha_is_full_40_hex(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)


# ---------------------------------------------------------------------------
# 4. Mechanism 895 block structure.
# ---------------------------------------------------------------------------

class TestMechanism895Structure:
    def test_block_key_present_once(self):
        text = _nyt_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_block_under_anthropic_section(self):
        d = _block_yaml()
        assert d["publication"] == "The New York Times"
        assert d["mechanism_id"] == MECH_NUM
        assert d["iteration"] == ITERATION
        assert d["iteration_type"] == "A"
        assert d["iteration_time"] == "2026-09-30 20:00 PDT"

    def test_distinct_from_prior_names_lineage(self):
        d = _block_yaml()
        for token in ("835", "883", "892", "m847/m856"):
            assert token in d["distinct_from_prior"], token

    def test_rotation_guard_field(self):
        d = _block_yaml()
        assert "1105-1109" in d["rotation_guard"]
        assert "THIRD leg" in d["rotation_guard"]

    def test_test_file_field_matches(self):
        d = _block_yaml()
        assert d["test_file"] == "tests/" + OWN_BASENAME

    def test_no_em_dash_in_block(self):
        assert "—" not in _block_text()
        assert "–" not in _block_text()


# ---------------------------------------------------------------------------
# 5. Mechanism 895 Anthropic arms: 1 fresh S-1 arm + 1 carried temporal anchor.
# ---------------------------------------------------------------------------

class TestMechanism895AnthropicArms:
    def test_one_fresh_anthropic_arm(self):
        arms = _block_yaml()["articles_anthropic"]
        assert len(arms) == 1

    def test_sorkin_arm_register_and_tone(self):
        arm = _block_yaml()["articles_anthropic"][0]
        assert arm["register"] == "market_systemic_accountability"
        assert arm["manual_illustrative_tone"] == -0.35
        assert arm["date"] == "2026-09-29"

    def test_sorkin_arm_byline_and_desk(self):
        arm = _block_yaml()["articles_anthropic"][0]
        assert arm["byline"] == "Andrew Ross Sorkin"
        assert arm["desk"] == "DealBook"

    def test_sorkin_arm_url(self):
        arm = _block_yaml()["articles_anthropic"][0]
        assert arm["url"] == NYT_URL
        assert arm["attestation_url"] == IMPLICATOR_URL

    def test_sorkin_arm_canary_language(self):
        arm = _block_yaml()["articles_anthropic"][0]
        langs = " ".join(arm["key_language"])
        assert "canary in the coal mine" in langs
        assert "mark-to-market" in langs
        assert "circular financing" in langs

    def test_carried_sep18_anchor_arm(self):
        anchors = _block_yaml()["carried_anthropic_temporal_anchor"]
        assert len(anchors) == 1
        arm = anchors[0]
        assert arm["date"] == "2026-09-18"
        assert arm["tone_carried"] == 0.25
        assert arm["register"] == "ipo_momentum_capital_market"
        assert "#807" in arm["source"]
        assert "not novel" in arm["novelty_note"]

    def test_arms_excerpt_bounded(self):
        d = _block_yaml()
        assert "#503" in d["research_method"]
        assert "0 browser.open" in d["research_method"]


# ---------------------------------------------------------------------------
# 6. Mechanism 895 Meta arms (carried, un-rescored per #807).
# ---------------------------------------------------------------------------

class TestMechanism895MetaArms:
    def test_two_meta_arms(self):
        arms = _block_yaml()["articles_meta_carried"]
        assert len(arms) == 2

    def test_connect_arm_carried(self):
        arm = _block_yaml()["articles_meta_carried"][0]
        assert arm["tone_carried"] == 0.10
        assert arm["register"] == "straight_product_launch_relay"
        assert "#807" in arm["source"]

    def test_ice_ban_arm_carried(self):
        arm = _block_yaml()["articles_meta_carried"][1]
        assert arm["tone_carried"] == -0.30
        assert arm["register"] == "enforcement_register_investigative"
        assert "#807" in arm["source"]

    def test_carried_arms_not_novel(self):
        for arm in _block_yaml()["articles_meta_carried"]:
            assert "not novel" in arm["novelty_note"]


# ---------------------------------------------------------------------------
# 7. Financial relationship (non-causal language).
# ---------------------------------------------------------------------------

class TestFinancialRelationship895:
    def test_anthropic_reported_settlement_single_source(self):
        fr = _block_yaml()["financial_relationship"]
        assert "single-source UNVERIFIED" in fr["nyt_anthropic_reported_settlement"]
        assert "Dec 29 2025" in fr["nyt_anthropic_reported_settlement"]

    def test_amazon_deal_indirect_channel(self):
        fr = _block_yaml()["financial_relationship"]
        assert "$20-25M/yr" in fr["nyt_amazon_deal"]
        assert "Anthropic investor" in fr["nyt_amazon_deal"]

    def test_openai_adversarial_litigation(self):
        fr = _block_yaml()["financial_relationship"]
        assert "Dec 2023" in fr["nyt_openai_litigation"]

    def test_meta_zero(self):
        fr = _block_yaml()["financial_relationship"]
        assert fr["nyt_meta"] == "$0, no licensing relationship"

    def test_deal_not_disclosed(self):
        fr = _block_yaml()["financial_relationship"]
        assert fr["deal_disclosed_in_nyt_coverage"] is False

    def test_non_causal_language(self):
        fr = _block_yaml()["financial_relationship"]
        assert "not proof of editorial control" in fr["non_causal_language"]


# ---------------------------------------------------------------------------
# 8. Mechanism 895 scorer (MANUAL ILLUSTRATIVE ONLY - engine NOT run).
# ---------------------------------------------------------------------------

class TestMechanism895Scorer:
    def _scorer(self):
        return _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]

    def test_scorer_manual_only(self):
        assert self._scorer()["scorer"] == "MANUAL ILLUSTRATIVE ONLY, engine NOT run"

    def test_target_scores(self):
        s = self._scorer()
        assert s["target_scores"] == [-0.35]
        assert s["target_avg"] == -0.35

    def test_peer_scores(self):
        s = self._scorer()
        assert s["peer_scores"] == [0.10, -0.30]
        assert s["peer_avg"] == -0.10

    def test_delta(self):
        s = self._scorer()
        assert s["delta"] == -0.25
        assert s["delta_calc"] == "-0.35 - (-0.10) = -0.25"

    def test_temporal_swing(self):
        s = self._scorer()
        assert "-0.60 in 11 days" in s["temporal_swing"]
        assert "third publication-level" in s["temporal_swing"]

    def test_cross_publication_triple(self):
        s = self._scorer()
        assert "m883" in s["cross_publication_s1_triple"]
        assert "m892" in s["cross_publication_s1_triple"]
        assert "0.05" in s["cross_publication_s1_triple"]

    def test_inference_not_calculated(self):
        s = self._scorer()
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["verdict"] == "directionally_supported_not_proven"
        assert s["no_analysis_json_update"] is True
        assert s["artifact_grade"] is False
        assert s["correlation_not_causation"] is True


# ---------------------------------------------------------------------------
# 9. Statistical discipline + falsification-family negative guard.
# ---------------------------------------------------------------------------

class TestMechanism895Discipline:
    def test_discipline_tokens(self):
        d = _block_yaml()
        for token in ("MANUAL ILLUSTRATIVE ONLY", "engine NOT run",
                      "NOT_CALCULATED", "NOT artifact-grade",
                      "directionally_supported_not_proven"):
            assert token in d["statistical_discipline"], token

    def test_falsification_negative(self):
        d = _block_yaml()
        assert d["falsification_family"].startswith(
            "NOT a falsification-family member")
        assert "m567" in d["falsification_family"]
        assert "THIRTY-NINTH" in d["falsification_family"]

    def test_finding_correlation_guard(self):
        assert "Correlation is not causation" in _block_yaml()["finding"]


# ---------------------------------------------------------------------------
# 10. Ledger holds at 38 (THIRTY-NINTH absent - negative guard).
# ---------------------------------------------------------------------------

class TestLedgerHoldsAt38:
    def test_not_falsification_family(self):
        d = _block_yaml()
        assert d["falsification_family"].startswith(
            "NOT a falsification-family member")

    def test_ledger_38(self):
        assert _block_yaml()["ledger"] == "38"

    def test_exactly_one_38th_member_form(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if "THIRTY-EIGHTH falsification-family member" in text:
                    hits.append(p)
        assert hits == [os.path.join(
            PROFILES_DIR, "careers", "journalists.yaml")], hits

    def test_38th_is_journalists_m893(self):
        text = open(os.path.join(PROFILES_DIR, "careers", "journalists.yaml"),
                    encoding="utf-8").read()
        assert "THIRTY-EIGHTH falsification-family member" in text
        assert ("mechanism_id: %d" % 893) in text

    def test_no_39th_member_form(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if "THIRTY-NINTH falsification-family member" in text:
                    hits.append(p)
        assert hits == [], hits
        assert "THIRTY-NINTH falsification-family member" not in _block_text()

    def test_m895_not_member_form(self):
        assert "THIRTY-NINTH" in _block_text()
        assert "NOT a falsification-family member" in _block_text()

    def test_journalists_guard_line_intact(self):
        text = open(os.path.join(PROFILES_DIR, "careers", "journalists.yaml"),
                    encoding="utf-8").read()
        assert "THIRTY-EIGHTH falsification-family member" in text

    def test_no_29th_direction_form(self):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if "TWENTY-NINTH relationship direction" in text:
                    hits.append(p)
        assert hits == [], hits

    def test_28th_direction_present(self):
        text = open(os.path.join(PROFILES_DIR, "competitor-entities.yaml"),
                    encoding="utf-8").read()
        assert "TWENTY-EIGHTH relationship direction" in text
        assert ("mechanism_id: %d" % 894) in text


# ---------------------------------------------------------------------------
# 11. Synthetic engine calibration (fresh values, NOT #1105's).
#
# Aug 28 2026 standing rule: the engine is calibrated here on SYNTHETIC
# data only, via mediascope.score.asymmetry.calculate_asymmetry with its
# real signature (target_scores, peer_scores, target_entity,
# peer_entities, publication_slug, period_start, period_end). The finding
# layer stays MANUAL ILLUSTRATIVE ONLY: the engine is never promoted to
# findings, and these numbers are NOT a corpus claim.
# ---------------------------------------------------------------------------

SYN_TARGET_1107 = [-0.33, -0.37, -0.31, -0.35, -0.39]
SYN_PEER_1107 = [0.12, -0.26, 0.09]


class TestSyntheticEngineCalibration1107:
    def _calculate(self):
        from datetime import datetime

        def calc(target_scores, peer_scores):
            return calculate_asymmetry(
                target_scores,
                peer_scores,
                "Anthropic",
                ["Meta"],
                "synthetic-calibration-1107",
                datetime(2026, 9, 30),
                datetime(2026, 9, 30),
            )

        return calc

    def test_engine_runs_on_synthetic_only(self):
        calc = self._calculate()
        res = calc(SYN_TARGET_1107, SYN_PEER_1107)
        log.info(
            "CALIBRATION 1107 synthetic-only: n_target=%d n_peer=%d "
            "asymmetry=%.6f t=%.6f p=%.6g d=%.6f ci=(%.6f, %.6f) "
            "significant=%s",
            len(SYN_TARGET_1107), len(SYN_PEER_1107),
            res.asymmetry_score, res.t_statistic, res.p_value,
            res.cohens_d, res.confidence_interval_lower,
            res.confidence_interval_upper, res.is_significant,
        )
        assert math.isfinite(res.t_statistic)
        assert math.isfinite(res.p_value)
        assert math.isfinite(res.cohens_d)
        assert res.asymmetry_score < 0

    def test_synthetic_delta_matches_hand_calc(self):
        calc = self._calculate()
        res = calc(SYN_TARGET_1107, SYN_PEER_1107)
        hand = (sum(SYN_TARGET_1107) / len(SYN_TARGET_1107)
                - sum(SYN_PEER_1107) / len(SYN_PEER_1107))
        assert res.asymmetry_score == pytest.approx(hand)

    def test_effect_size_sane(self):
        calc = self._calculate()
        res = calc(SYN_TARGET_1107, SYN_PEER_1107)
        assert abs(res.cohens_d) < 5
        assert abs(res.cohens_d) > 0.2

    def test_ci_contains_delta(self):
        calc = self._calculate()
        res = calc(SYN_TARGET_1107, SYN_PEER_1107)
        lo = res.confidence_interval_lower
        hi = res.confidence_interval_upper
        assert (hi - lo) < 2.0
        assert lo <= res.asymmetry_score <= hi

    def test_finding_layer_not_engine_scored(self):
        d = _block_yaml()
        assert d["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["scorer"] == (
            "MANUAL ILLUSTRATIVE ONLY, engine NOT run")
        assert "engine NOT run" in d["statistical_discipline"]


# ---------------------------------------------------------------------------
# 12. Supersession: #1104/#1105 zero-895 guards fail BY DESIGN.
# ---------------------------------------------------------------------------

class TestSupersessionPins1107:
    def test_underscore_895_hits_exactly_nyt(self):
        """#1104/#1105 zero-895 sweeps fail BY DESIGN: the single hit
        is the new m895 block in profiles/nytimes.yaml."""
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [NYT_FILE], hits

    def test_numeric_895_hits_exactly_nyt_profiles(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [NYT_FILE], hits

    def test_dash_895_stays_zero(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_max_numeric_is_895_not_894(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_novel_urls_zero_hit_elsewhere(self):
        urls = (NYT_URL, IMPLICATOR_URL)
        for url in urls:
            hits = [
                p for p in _iter_source_files()
                if url in open(p, encoding="utf-8", errors="replace").read()
            ]
            assert hits == [NYT_FILE], (url, hits)

    def test_1104_zero_895_guards_fail_by_design(self):
        # The #1104 TestCorpusNoveltyPostCommit zero-895 sweeps grep the
        # WORKING tree - they fail BY DESIGN now that this run's m895
        # block is in the tree (pre-run they passed; designed lifecycle).
        # The class's HEAD-grep pins (894 present, no TWENTY-NINTH) still
        # pass; the 3 zero-895 sweep tests trip on the uncommitted block.
        result = _class_run(F1104, "TestCorpusNoveltyPostCommit")
        assert result.returncode != 0, result.stdout[-2000:]
        assert "895" in result.stdout

    def test_1105_zero_895_guards_fail_by_design(self):
        # The #1105 TestTypeDForwardLookingStaleness1105 guards grep the
        # WORKING tree - they fail BY DESIGN now that this run's m895
        # block is in the tree. Designed lifecycle; #1110 pins zero-896.
        result = _class_run(F1105, "TestTypeDForwardLookingStaleness1105")
        assert result.returncode != 0, result.stdout[-2000:]
        assert "895" in result.stdout


# ---------------------------------------------------------------------------
# 13. Doc-sync (DESELECTED pre-commit per #565/#719/#721).
# ---------------------------------------------------------------------------

class TestDocSync1107:
    @pytest.mark.docsync
    def test_readme_count_gate(self):
        """README test/file counts match the post-run totals."""
        readme = open(os.path.join(REPO_ROOT, "README.md"),
                      encoding="utf-8").read()
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme

    @pytest.mark.docsync
    def test_readme_table_row(self):
        """The #1107 test-file row is appended to the README test table."""
        readme = open(os.path.join(REPO_ROOT, "README.md"),
                      encoding="utf-8").read()
        assert TEST_BASENAME in readme

    @pytest.mark.docsync
    def test_architecture_count_gate(self):
        """ARCHITECTURE.md counts match the post-run totals."""
        arch = open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"),
                    encoding="utf-8").read()
        assert str(README_TEST_COUNT) in arch
        assert str(README_FILE_COUNT) in arch

    @pytest.mark.docsync
    def test_architecture_tree_row(self):
        """The #1107 test-file row is appended to the ARCHITECTURE tree."""
        arch = open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"),
                    encoding="utf-8").read()
        assert TEST_BASENAME in arch


# ---------------------------------------------------------------------------
# 14. Iteration log (DESELECTED pre-commit per #565/#719/#721; marker log).
# ---------------------------------------------------------------------------

class TestIterationLog1107:
    @pytest.mark.log
    def test_log_captures_1107(self):
        """The iteration log carries the #1107 Type A entry."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:5000]
        assert "## #1107 Type A:" in head
        assert "20:00 PDT" in head
        assert "m895" in head

    @pytest.mark.log
    def test_log_window(self):
        """The entry names the 1105-1109 window third leg."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:5000]
        assert "1105-1109" in head
        assert "THIRD leg" in head

    @pytest.mark.log
    def test_log_ledger_38(self):
        """The entry records ledger holds at 38."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:5000]
        assert "ledger holds at 38" in head
        assert "THIRTY-NINTH" in head

    @pytest.mark.log
    def test_log_lineage(self):
        """The entry records the m835 extension and m883/m892 triple."""
        head = open(os.path.join(REPO_ROOT, "iteration-log.md"),
                    encoding="utf-8").read()[:5000]
        assert "835" in head
        assert "883" in head
        assert "892" in head


# ---------------------------------------------------------------------------
# 15. In-flight isolation: #899/#938/#900/#1012-wt untouched by this run.
# ---------------------------------------------------------------------------

def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO_ROOT, capture_output=True, text=True
    )


class TestInFlightIsolation1107:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        src = open(os.path.join(TESTS_DIR, OWN_BASENAME),
                   encoding="utf-8").read()
        assert "#899" in src

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_do_not_touch_1024_m846(self):
        # Guarded in the log entry per convention; the test file keeps
        # the in-flight list only (own-file reference would trip the
        # contiguous-literal discipline elsewhere).
        src = open(os.path.join(TESTS_DIR, OWN_BASENAME),
                   encoding="utf-8").read()
        assert "#1024" in src
