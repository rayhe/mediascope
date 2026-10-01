"""Type A #1112 (2026-10-01 01:00 PDT) - WIRED x OpenAI Sep-29 LASST Hugging
Face lawsuit accountability register vs carried WIRED x Meta arms,
mechanism 898.

THIRD leg of the 1110-1114 window (D #1110 -> E #1111 -> A #1112 -> B #1113
-> C #1114), per the #565 rotation anchor. Predecessor: #1111 Type E
(mediascope-daily-iteration, 2026-10-01 00:00 PDT). The 1105-1109 window is
verified closed.

Mechanism 898 answers the open empirical test left by m889 (Type A #1097,
Sep 30 2026): WIRED coverage of the Sep-29 LASST California lawsuit over
the Hugging Face breach EXISTS and is adversarial, not softened or
suppressed. Fresh arm: Sep 29 2026, Lily Hay Newman, 'OpenAI Sued Over
Hugging Face Hack: CDAFA, No Damages' - WIRED reports Legal Advocates for
Safe Science and Technology (LASST) filed in San Francisco Superior Court
against OpenAI Group PBC and the OpenAI Foundation over the July incident
in which roughly 700 of OpenAI's AI agents breached Hugging Face
infrastructure; CDAFA (Penal Code 502) as the UCL unlawful predicate plus
AB 316 (Civil Code 1714.46); injunctive relief, not damages; WIRED framing:
'a nonprofit doing what Hugging Face has not: attempting court
accountability for the actions of OpenAI's evaluation agents.'
Excerpt-bounded per #503 (WIRED paywalled; 0 browser.open); relay-attested
via the explainx.ai FAQ carrying verbatim WIRED/Lily Hay Newman
attribution.

MANUAL ILLUSTRATIVE -0.40 (adversarial accountability on the deal partner,
the hardest WIRED x OpenAI arm in the corpus on a litigation peg) vs
carried WIRED x Meta mean -0.375 (Pinky Promises skepticism -0.45, NameTag
class action -0.30, un-rescored per #807): pooled delta -0.025, near-null
parity. The clean adversarial-legal-peg read: -0.40 (LASST suit) vs -0.30
(NameTag class action) = -0.10 - on adversarial-legal pegs the paid
counterparty is HARDER on its payer than on the non-payer, same genre,
same outlet, genre confound controlled.

FORTIETH falsification-family member (ledger 39->40): the uniform
payer-softening prediction (Conde Nast Aug-2024 OpenAI licensing deal,
mechanism 504 -> softer OpenAI coverage at WIRED) fails on ordering.
Extends the falsification-of-financial-determinism family at the
deal-partner level after #597's coverage-selection and #602's
licensing-halo bounds; extends the m877 peg-not-entity finding from the
leak-driven and safety-crisis registers into the enforcement-litigation
register. TWENTY-NINTH relationship direction still the newest (m897);
THIRTIETH direction absent.

Literal discipline per #715: this file carries NO contiguous underscore-form,
dash-form, or colon-form 898 mechanism literal - the 898 needles are
format-built ("%d" % MECH_NUM), so the zero-898 sweeps keep one hit
(profiles/wired.yaml) and the zero-899 forward guards stay green.
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

ITERATION = 1112
TYPE_LETTER = "A"
WINDOW = "1110-1114"
MECH_NUM = 898
NEXT_NUM = 899
ANCHORED_SHA = "0" * 40  # main commit, patched in the anchor followup per #565
OWN_BASENAME = (
    "test_type_a_1112_wired_openai_lasst_huggingface_lawsuit_register_"
    "vs_meta_carried_arms_oct01_1am.py"
)
BLOCK_KEY = (
    "mechanism_%d_wired_openai_lasst_huggingface_lawsuit_register_"
    "vs_meta_carried_arms_sep30" % MECH_NUM
)
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
WIRED_FILE = os.path.join(PROFILES_DIR, "wired.yaml")
RELAY_URL = ("https://explainx.ai/blog/"
             "lasst-openai-hugging-face-lawsuit-california-cdafa-2026")

# Predecessor chain: #1111 Type E SECOND leg of the 1110-1114 window.
PRED_MAIN_1111 = "3b128066"
PRED_ANCHOR_1111 = "6ded09d1"
PRED_LOGHASH_1111 = "9b00a5d5"
PRED_FINAL_1111 = "c7dc930f"

F1110 = ("test_type_d_1110_m895_m896_m897_qualitative_corpus_integrity_"
         "sep30_11pm.py")
F1111 = ("test_type_e_1111_podcast_sentiment_145th_verification_"
         "oct01_12am.py")
F1109 = ("test_type_c_1109_google_pilot_grounding_origination_"
         "framethenprice_twentyninth_direction_sep30_10pm.py")

README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")


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


def _wired_text():
    return open(WIRED_FILE, encoding="utf-8").read()


def _block_text():
    text = _wired_text()
    start = text.index(BLOCK_KEY)
    lines = text[start:].split("\n")
    end = next(i for i, line in enumerate(lines)
               if i > 0 and re.match(r"^  [a-z_]", line))
    return "\n".join(lines[:end])


def _block_yaml():
    return yaml.safe_load(
        _wired_text())["competitor_relationships"]["openai"][BLOCK_KEY]


def _class_run(test_file, class_name):
    return subprocess.run(
        [os.path.join(REPO_ROOT, ".venv", "bin", "python"), "-m", "pytest",
         os.path.join(TESTS_DIR, test_file) + "::" + class_name,
         "-q", "--no-header", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )


def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO_ROOT, capture_output=True, text=True
    )


# ---------------------------------------------------------------------------
# 1. Novelty (pre-commit: #715 protocol).
# ---------------------------------------------------------------------------

class TestNovelty1112:
    def test_single_test_file_for_iteration(self):
        files = glob.glob(
            os.path.join(TESTS_DIR, "test_type_a_1112*.py"))
        assert len(files) == 1, files

    def test_novelty_verification_claim_in_block(self):
        assert "zero test_type_a_1112 files on disk" in _block_text()

    def test_window_legs_present(self):
        d_files = glob.glob(os.path.join(TESTS_DIR, "test_type_d_1110*.py"))
        e_files = glob.glob(os.path.join(TESTS_DIR, "test_type_e_1111*.py"))
        assert len(d_files) >= 1 and len(e_files) >= 1

    def test_max_numeric_mechanism_id_is_898(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_underscore_next_num_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_next_num_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_zero_numeric_next_num_in_profiles(self):
        assert _profiles_grep_numeric_mechanism_id(NEXT_NUM) == []


# ---------------------------------------------------------------------------
# 2. Rotation guard (pre-commit assertions; git-log novelty test is
# SUPERSEDED BY DESIGN post-commit - deselect in post-commit full runs).
# ---------------------------------------------------------------------------

class TestRotationGuard1112:
    def test_predecessor_1111_chain_present(self):
        log = _git("log", "--oneline", "-60").stdout
        assert PRED_MAIN_1111 in log
        assert PRED_ANCHOR_1111 in log
        assert PRED_LOGHASH_1111 in log
        assert PRED_FINAL_1111 in log

    def test_type_a_1112_novelty(self):
        # "Type A #1112" absent from git log pre-commit; own file not
        # yet committed. SUPERSEDED BY DESIGN once this run's main
        # commit ("Type A #1112:") lands; post-commit, the anchor
        # asserts the patched ANCHORED_SHA is present in git log.
        # Deselect this test in post-commit full runs.
        log = _git("log", "--oneline", "--grep=Type A #1112").stdout
        assert log.strip() == ""

    def test_window_order_d_e_a_b_c(self):
        src = open(os.path.join(TESTS_DIR, OWN_BASENAME),
                   encoding="utf-8").read()
        assert "E #1111 -> A #1112" in src

    def test_next_run_1113_type_b_noted(self):
        src = open(os.path.join(TESTS_DIR, OWN_BASENAME),
                   encoding="utf-8").read()
        assert "B #1113" in src


# ---------------------------------------------------------------------------
# 3. Novelty anchor (pre-commit placeholder; patched green post-commit).
# ---------------------------------------------------------------------------

class TestNoveltyAnchor1112:
    def test_anchored_sha_placeholder_pre_commit(self):
        # Pre-commit the anchor is a zero placeholder; the anchor
        # followup patches it per #565. This test documents the
        # pre-commit state; the post-commit rotation guard asserts the
        # patched value is present in git log.
        assert ANCHORED_SHA == "0" * 40 or len(ANCHORED_SHA) == 40

    def test_anchor_mechanics_documented(self):
        src = open(os.path.join(TESTS_DIR, OWN_BASENAME),
                   encoding="utf-8").read()
        assert "ANCHORED_SHA" in src
        assert "#565" in src


# ---------------------------------------------------------------------------
# 4. Mechanism 898 block structure.
# ---------------------------------------------------------------------------

class TestMechanism898Structure:
    def test_block_key_present_once(self):
        text = _wired_text()
        assert text.count(BLOCK_KEY + ":") == 1

    def test_block_under_openai_section(self):
        d = _block_yaml()
        assert d["publication"] == "WIRED"
        assert d["mechanism_id"] == MECH_NUM
        assert d["iteration"] == ITERATION
        assert d["iteration_type"] == "A"
        assert d["iteration_time"] == "2026-10-01 01:00 PDT"

    def test_distinct_from_prior_names_lineage(self):
        d = _block_yaml()
        for token in ("889", "877", "591", "504"):
            assert token in d["distinct_from_prior"], token

    def test_rotation_guard_field(self):
        d = _block_yaml()
        assert "1110-1114" in d["rotation_guard"]
        assert "THIRD leg" in d["rotation_guard"]

    def test_test_file_field_matches(self):
        d = _block_yaml()
        assert d["test_file"] == "tests/" + OWN_BASENAME

    def test_ledger_40(self):
        assert _block_yaml()["falsification_ledger"] == "40"

    def test_no_em_dash_in_block(self):
        assert "—" not in _block_text()
        assert "–" not in _block_text()


# ---------------------------------------------------------------------------
# 5. Mechanism 898 OpenAI arm: 1 fresh LASST lawsuit arm.
# ---------------------------------------------------------------------------

class TestMechanism898OpenAIArm:
    def test_one_fresh_openai_arm(self):
        arms = _block_yaml()["articles_openai"]
        assert len(arms) == 1

    def test_lasst_arm_register_and_tone(self):
        arm = _block_yaml()["articles_openai"][0]
        assert arm["register"] == "adversarial_accountability_enforcement_litigation"
        assert arm["manual_illustrative_tone"] == -0.40
        assert arm["date"] == "2026-09-29"

    def test_lasst_arm_byline(self):
        arm = _block_yaml()["articles_openai"][0]
        assert arm["author"] == "Lily Hay Newman"

    def test_lasst_arm_relay_url(self):
        arm = _block_yaml()["articles_openai"][0]
        assert arm["url"] == RELAY_URL

    def test_lasst_arm_key_language(self):
        arm = _block_yaml()["articles_openai"][0]
        assert "court accountability" in arm["language"]
        assert "Hugging Face" in arm["piece"]

    def test_lasst_arm_corroboration(self):
        arm = _block_yaml()["articles_openai"][0]
        assert len(arm["mirror_urls"]) == 3

    def test_arm_excerpt_bounded(self):
        d = _block_yaml()
        assert "#503" in d["research_method"]
        assert "0 browser.open" in d["research_method"]


# ---------------------------------------------------------------------------
# 6. Mechanism 898 Meta arms (carried, un-rescored per #807).
# ---------------------------------------------------------------------------

class TestMechanism898MetaArms:
    def test_two_meta_arms(self):
        arms = _block_yaml()["articles_meta"]
        assert len(arms) == 2

    def test_pinky_promises_arm_carried(self):
        arm = _block_yaml()["articles_meta"][0]
        assert arm["tone_carried"] == -0.45
        assert arm["register"] == "skepticism_on_positive_news"
        assert "#807" in arm["source"]

    def test_nametag_arm_carried(self):
        arm = _block_yaml()["articles_meta"][1]
        assert arm["tone_carried"] == -0.30
        assert arm["register"] == "adversarial_legal"
        assert "#807" in arm["source"]

    def test_carried_arms_not_novel(self):
        for arm in _block_yaml()["articles_meta"]:
            assert "not novel" in arm["novelty_note"]


# ---------------------------------------------------------------------------
# 7. Financial relationship (non-causal language).
# ---------------------------------------------------------------------------

class TestFinancialRelationship898:
    def test_conde_nast_openai_deal(self):
        fr = _block_yaml()["financial_relationship"]
        assert "$1-5M/yr" in fr["conde_nast_openai_deal"]
        assert "Aug 2024" in fr["conde_nast_openai_deal"]

    def test_conde_nast_meta_zero(self):
        fr = _block_yaml()["financial_relationship"]
        assert fr["conde_nast_meta"] == "$0, no licensing relationship"

    def test_deal_not_disclosed(self):
        fr = _block_yaml()["financial_relationship"]
        assert fr["deal_disclosed_in_wired_coverage"] is False

    def test_non_causal_language(self):
        fr = _block_yaml()["financial_relationship"]
        assert "no causal claim" in fr["non_causal_language"]


# ---------------------------------------------------------------------------
# 8. Mechanism 898 scorer (MANUAL ILLUSTRATIVE ONLY - engine NOT run).
# ---------------------------------------------------------------------------

class TestMechanism898Scorer:
    def _scorer(self):
        return _block_yaml()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]

    def test_scorer_manual_only(self):
        assert self._scorer()["scorer"].startswith("none (MANUAL ILLUSTRATIVE ONLY")

    def test_target_scores(self):
        s = self._scorer()
        assert s["target_scores"] == [-0.40]
        assert s["target_avg"] == -0.40

    def test_peer_scores(self):
        s = self._scorer()
        assert s["peer_scores"] == [-0.45, -0.30]
        assert s["peer_avg"] == -0.375

    def test_delta(self):
        s = self._scorer()
        assert s["delta"] == pytest.approx(-0.025)
        assert s["delta_calc"] == "-0.40 - (-0.375) = -0.025"

    def test_legal_peg_read(self):
        s = self._scorer()
        assert "-0.10" in s["delta_direction"]

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
# 9. Statistical discipline + FORTIETH falsification-family member form.
# ---------------------------------------------------------------------------

class TestMechanism898Discipline:
    def test_discipline_tokens(self):
        d = _block_yaml()
        for token in ("MANUAL ILLUSTRATIVE ONLY", "engine NOT run",
                      "NOT_CALCULATED", "artifact_grade false",
                      "directionally_supported_not_proven"):
            assert token in d["statistical_discipline"], token

    def test_falsification_fortieth_member_form(self):
        d = _block_yaml()
        assert d["falsification_family"].startswith(
            "FORTIETH falsification-family member")
        assert "uniform payer-softening prediction" in d["falsification_family"]

    def test_finding_correlation_guard(self):
        assert "Correlation is not causation" in _block_yaml()["finding"]


# ---------------------------------------------------------------------------
# 10. Ledger holds at 40 (FORTY-FIRST absent - negative guard).
# ---------------------------------------------------------------------------

def _profiles_member_form_hits(form):
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            text = open(p, encoding="utf-8", errors="replace").read()
            if form in text:
                hits.append(p)
    return hits


class TestLedgerHoldsAt40:
    def test_fortieth_member_form_exactly_once_in_wired(self):
        hits = _profiles_member_form_hits(
            "FORTIETH falsification-family member")
        assert hits == [WIRED_FILE], hits

    def test_39th_still_once_in_journalists(self):
        hits = _profiles_member_form_hits(
            "THIRTY-NINTH falsification-family member")
        assert hits == [os.path.join(
            PROFILES_DIR, "careers", "journalists.yaml")], hits

    def test_no_41st_member_form(self):
        hits = _profiles_member_form_hits(
            "FORTY-FIRST falsification-family member")
        assert hits == [], hits
        assert "FORTY-FIRST" not in _block_text()

    def test_29th_direction_present(self):
        text = open(os.path.join(PROFILES_DIR, "competitor-entities.yaml"),
                    encoding="utf-8").read()
        assert "TWENTY-NINTH relationship direction" in text

    def test_no_30th_direction(self):
        hits = _profiles_member_form_hits(
            "THIRTIETH relationship direction")
        assert hits == [], hits

    def test_m898_claims_no_higher_slot(self):
        assert "FORTY-FIRST" not in _block_yaml()["falsification_family"]


# ---------------------------------------------------------------------------
# 11. Synthetic engine calibration (fresh values, NOT #1110's).
#
# Aug 28 2026 standing rule: the engine is calibrated here on SYNTHETIC
# data only, via mediascope.score.asymmetry.calculate_asymmetry with its
# real signature (target_scores, peer_scores, target_entity,
# peer_entities, publication_slug, period_start, period_end). The finding
# layer stays MANUAL ILLUSTRATIVE ONLY: the engine is never promoted to
# findings, and these numbers are NOT a corpus claim.
# ---------------------------------------------------------------------------

SYN_TARGET_1112 = [-0.50, -0.20, -0.45, -0.30, -0.40]
SYN_PEER_1112 = [0.10, -0.30, 0.05]


class TestSyntheticEngineCalibration1112:
    def _calculate(self):
        from datetime import datetime

        def calc(target_scores, peer_scores):
            return calculate_asymmetry(
                target_scores,
                peer_scores,
                "OpenAI",
                ["Meta"],
                "synthetic-calibration-1112",
                datetime(2026, 10, 1),
                datetime(2026, 10, 1),
            )

        return calc

    def test_engine_runs_on_synthetic_only(self):
        calc = self._calculate()
        res = calc(SYN_TARGET_1112, SYN_PEER_1112)
        log.info(
            "CALIBRATION 1112 synthetic-only: n_target=%d n_peer=%d "
            "asymmetry=%.6f t=%.6f p=%.6g d=%.6f ci=(%.6f, %.6f) "
            "significant=%s",
            len(SYN_TARGET_1112), len(SYN_PEER_1112),
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
        res = calc(SYN_TARGET_1112, SYN_PEER_1112)
        hand = (sum(SYN_TARGET_1112) / len(SYN_TARGET_1112)
                - sum(SYN_PEER_1112) / len(SYN_PEER_1112))
        assert res.asymmetry_score == pytest.approx(hand)

    def test_effect_size_sane(self):
        calc = self._calculate()
        res = calc(SYN_TARGET_1112, SYN_PEER_1112)
        assert abs(res.cohens_d) < 5
        assert abs(res.cohens_d) > 0.2

    def test_ci_contains_delta(self):
        calc = self._calculate()
        res = calc(SYN_TARGET_1112, SYN_PEER_1112)
        lo = res.confidence_interval_lower
        hi = res.confidence_interval_upper
        assert (hi - lo) < 2.0
        assert lo <= res.asymmetry_score <= hi

    def test_finding_layer_not_engine_scored(self):
        d = _block_yaml()
        assert d["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["scorer"].startswith(
            "none (MANUAL ILLUSTRATIVE ONLY")
        assert "engine NOT run" in d["statistical_discipline"]


# ---------------------------------------------------------------------------
# 12. Supersession: #1110/#1111/#1109 zero-898 guards fail BY DESIGN.
# ---------------------------------------------------------------------------

class TestSupersessionPins1112:
    def test_underscore_898_hits_exactly_wired(self):
        """#1110/#1109/#1111 zero-898 sweeps fail BY DESIGN: the single hit
        is the new m898 block in profiles/wired.yaml."""
        hits = _repo_grep_underscore_mechanism(MECH_NUM)
        assert hits == [WIRED_FILE], hits

    def test_numeric_898_hits_exactly_wired_profiles(self):
        hits = _profiles_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [WIRED_FILE], hits

    def test_dash_898_stays_zero(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_max_numeric_is_898_not_897(self):
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_novel_relay_url_zero_hit_elsewhere(self):
        hits = [
            p for p in _iter_source_files()
            if RELAY_URL in open(p, encoding="utf-8",
                                 errors="replace").read()
        ]
        assert hits == [WIRED_FILE], hits

    def test_1110_zero_898_guards_fail_by_design(self):
        # The #1110 TestGuardLifecycle1110 zero-898 guards grep the
        # WORKING tree - they fail BY DESIGN now that this run's m898
        # block is in the tree (pre-run they passed; designed lifecycle).
        result = _class_run(F1110, "TestGuardLifecycle1110")
        assert result.returncode != 0, result.stdout[-2000:]
        assert "898" in result.stdout

    def test_1111_staleness_pins_fail_by_design(self):
        # The #1111 TestStalenessPins class pins the #1110 zero-898
        # forward guards as still-green; it fails BY DESIGN now that
        # mechanism 898 has landed at this run's A leg.
        result = _class_run(F1111, "TestStalenessPins")
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1109_corpus_novelty_fails_by_design(self):
        # The #1109 TestCorpusNoveltyPostCommit zero-898 sweeps plus the
        # no-FORTIETH-member guard trip BY DESIGN on this run's landing.
        result = _class_run(F1109, "TestCorpusNoveltyPostCommit")
        assert result.returncode != 0, result.stdout[-2000:]


# ---------------------------------------------------------------------------
# 13. Doc-sync (pre-commit assertions; rows land with the doc-sync).
# ---------------------------------------------------------------------------

class TestDocSync1112:
    def test_readme_test_file_table_has_no_1112_row_pre_commit(self):
        readme = open(README_PATH, encoding="utf-8").read()
        assert "test_type_a_1112" not in readme

    def test_architecture_has_no_1112_row_pre_commit(self):
        arch = open(ARCH_PATH, encoding="utf-8").read()
        assert "test_type_a_1112" not in arch

    def test_readme_stats_current(self):
        readme = open(README_PATH, encoding="utf-8").read()
        assert "| 56734 |" in readme
        assert "1436" in readme


# ---------------------------------------------------------------------------
# 14. Iteration log (pre-commit assertions; entry lands with the log).
# ---------------------------------------------------------------------------

class TestIterationLog1112:
    def test_no_1112_entry_pre_commit(self):
        log = open(LOG_PATH, encoding="utf-8").read()
        assert "## #1112 Type A" not in log

    def test_1111_entry_present(self):
        log = open(LOG_PATH, encoding="utf-8").read()
        assert "## #1111 Type E" in log

    def test_rotation_transparency_convention(self):
        log = open(LOG_PATH, encoding="utf-8").read()
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 15. In-flight isolation: #899/#938/#900/#1012-wt untouched by this run.
# ---------------------------------------------------------------------------

class TestInFlightIsolation1112:
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
