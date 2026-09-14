"""
Type D -- Iteration #750 (Mon 2026-09-14 16:00 PDT): m682 / m683 / m684
qualitative-discipline verification + post-#749 corpus integrity
(max numeric mechanism_id 684; zero mechanism 685 keys; ledger holds at 24) +
#745 background-suite tombstone (TENTH consecutive death; re-launched as
type_d_750_full_suite.log).

Verifies:
- m682 (WSJ x OpenAI slowdown-week enterprise watchdog expose register test,
  Type A #747, profiles/news-corp.yaml): same-publication same-day register
  MIX on the licensing payer (expose -0.40 MANUAL ILLUSTRATIVE vs carried
  relay pair [+0.10, +0.05] avg +0.075, illustrative delta -0.475; same-week
  register range 0.65), p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False, engine NOT run, verdict
  directionally_supported_not_proven, NOT artifact-grade, incentive
  attribution INCONCLUSIVE; NOT a falsification-family member (ledger
  holds at 24).
- m683 (Kate Conger (NYT) X/Musk-adversarial vs AI-lab-concern register
  split, Type B #748, profiles/competitor-coverage-research.yaml):
  journalist-level cross-entity register split, verdict
  directionally_supported_not_proven, p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False, engine NOT run, NOT artifact-grade; careers
  journalists.yaml list entry (name Kate Conger) backlinks mechanism 683;
  NOT a falsification-family member (ledger holds at 24).
- m684 (Getty Images x Perplexity global multi-year visual licensing,
  Oct 31 2025, Type C #749, profiles/competitor-entities.yaml):
  qualitative-only financial-incentive leg (scorer none, tone NOT_SCORED,
  p_value/cohens_d/ci NOT_CALCULATED, is_significant False, engine NOT run,
  NOT artifact-grade), no coverage-tone claim, verdict
  directionally_supported_not_proven on the financial-relationship
  documentation; NOT a falsification-family member (ledger holds at 24).
- Falsification ledger: TWENTY-FOURTH present, TWENTY-FIFTH absent;
  ledger holds at 24.
- Post-#749 corpus integrity: max numeric mechanism_id == 684 in
  profiles/; zero mechanism 685 keys in profiles/ and tests/ (own file
  excluded as sweep carrier per the #715 pattern-rescope lesson); m682 /
  m683 / m684 each present in their home YAML; designed keying holds
  (no underscore-form 682/683/684 mechanism key substrings in profiles/).
  #749's max-684 sweep stays green (Type D adds no mechanisms); #748's
  max-683 sweep fails by designed supersession (per #710/#720 convention).
- Statistical meaningfulness on FRESH synthetic corpora (new values this
  run, not #745's): strong-signal n=5-per-arm pair (asymmetry +1.154 exact,
  t=25.45037897327402, p=6.367391986424009e-09, d=16.0962329740007,
  CI (1.076, 1.234) above zero, is_significant True at the ENGINE layer);
  fresh near-null pair (asymmetry 0.004, t=0.1581138830084189,
  p=0.878364558371825, d=0.1, CI (-0.04, 0.044) crossing zero, silent);
  fresh degenerate n=1-per-arm contract (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 0.93, arm-swap negates).
  Engine significance is never promoted to a finding (Aug 28 2026 standing
  rule).
- Full-suite status: the #745 re-launched background 39K suite died mid-run
  (type_d_745_full_suite.log stalled at 1431 bytes / 3% progress since
  Sep 14 18:53 UTC; no pytest alive at this run's check) - TENTH
  consecutive background death (#705's, #710's, #715's first re-launch,
  #715's re-launch, #720's re-launch, #725's re-launch, #730's re-launch,
  #735's re-launch, #740's re-launch, #745's re-launch; tombstone lineage
  per #565 log convention). Re-launched this run to goal hidden_files
  type_d_750_full_suite.log with --continue-on-collection-errors (the 39
  pre-existing textblob ModuleNotFoundError collection errors exit-2 the
  plain run, per #745's tombstone correction) and the not-yet-existent
  anchor deselected; next Type D run checks it.
- Rotation guard: #749 Type C main commit present; 746-750 window orders
  E->A->B->C->D (anchor patched in the followup per #565).

Keying note (differs from #745 by design): this file resolves the three
mechanism blocks through mechanism_id walks and never carries the
descriptive block keys literally, so the #747/#748/#749 committed
descriptive-key uniqueness instruments stay green (#745's literal key
references left #742's equivalent test red; this run avoids repeating
that). The contiguous underscore form for mechanism ids appears only via
string concatenation inside sweep logic (own file excluded as carrier per
#715); space and colon forms are used in prose.
"""

"""Deselected pre-commit: rotation-guard anchor test per the #565 followup
convention; the anchor is patched in the followup commit once the main
commit SHA is known."""

import os
import re
import glob
import subprocess
from datetime import datetime

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_BASENAME = os.path.basename(__file__)

from mediascope.score.asymmetry import calculate_asymmetry

ITERATION = 750
MECH_MAX = 684

NC = os.path.join(REPO_ROOT, "profiles", "news-corp.yaml")
RESEARCH = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
CAREERS = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
LOG = os.path.join(REPO_ROOT, "iteration-log.md")
GOAL_HIDDEN = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/hidden_files"
)

M682_TEST_FILE = "test_type_a_747_wsj_openai_clash_expose_slowdown_sep14_1pm.py"
M683_TEST_FILE = "test_type_b_748_kate_conger_nyt_x_adversarial_vs_ai_lab_concern_register_gawker_pipeline_sep14_2pm.py"
M684_TEST_FILE = "test_type_c_749_getty_perplexity_visual_licensing_oct2025_sep14_3pm.py"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. Anchor test is deselected pre-commit.
ANCHORED_SHA = "c89819e9c32b4d0ed7203acba7968274cad50c3e"  # main commit, patched per #565


def _git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args], capture_output=True, text=True
    )


def _profile_yaml_paths():
    out = []
    for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith(".yaml"):
                out.append(os.path.join(root, fn))
    return out


def _mechanism_ids_from_files(paths):
    ids = []
    for p in paths:
        text = open(p, encoding="utf-8").read()
        ids.extend(
            int(x)
            for x in re.findall(r"(?m)^\s*mechanism_id:\s*(\d+)\s*$", text)
        )
    return ids


def _block_by_mechanism_id(parent, mech_id):
    # Direct-children walk: resolves a mechanism block without carrying the
    # descriptive block key literally (keeps the #747/#748/#749 committed
    # descriptive-key uniqueness instruments green).
    hits = [
        (k, v) for k, v in parent.items()
        if isinstance(v, dict) and v.get("mechanism_id") == mech_id
    ]
    assert len(hits) == 1, f"mechanism {mech_id}: {len(hits)} hits"
    return hits[0][1]


def _fold(block):
    # YAML `>` folding joins wrapped lines with spaces; normalize the same way
    # so multi-line assertions are not broken by source line breaks.
    return re.sub(r"\s+", " ", str(block))


def _load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _m682_block():
    data = _load_yaml(NC)
    return _block_by_mechanism_id(data["competitor_relationships"]["openai"], 682)


def _m683_block():
    data = _load_yaml(RESEARCH)
    return _block_by_mechanism_id(data["cross_publication_findings"], 683)


def _m684_block():
    data = _load_yaml(COMPETITOR_ENTITIES)
    return _block_by_mechanism_id(data["entities"]["perplexity"], 684)


def _kate_conger_entry():
    data = _load_yaml(CAREERS)
    hits = [
        item for item in data["journalists"]
        if isinstance(item, dict) and item.get("name") == "Kate Conger"
    ]
    assert len(hits) == 1, f"Kate Conger entries: {len(hits)}"
    return hits[0]


# -- novelty ---------------------------------------------------------------

class TestNovelty750:
    def test_single_test_file_for_750(self):
        hits = [
            os.path.basename(p)
            for p in glob.glob(os.path.join(TESTS_DIR, "test_type_d_750*.py"))
        ]
        assert hits == [TEST_BASENAME], hits

    def test_no_type_d_750_in_git_log_pre_commit(self):
        result = _git("log", "--oneline", "--grep=Type D #750")
        assert result.returncode == 0
        assert result.stdout.strip() == "", result.stdout.strip()

    def test_m682_key_unique_in_news_corp_profile(self):
        data = _load_yaml(NC)
        parent = data["competitor_relationships"]["openai"]
        hits = [
            k for k, v in parent.items()
            if isinstance(v, dict) and v.get("mechanism_id") == 682
        ]
        assert len(hits) == 1, hits
        # Designed keying: the block key carries no underscore-form 682 key
        # substring (keeps the #744/#745 committed zero-682 profile sweeps
        # green).
        assert "mechanism" + "_682" not in hits[0]

    def test_m683_key_unique_in_research_profile(self):
        data = _load_yaml(RESEARCH)
        parent = data["cross_publication_findings"]
        hits = [
            k for k, v in parent.items()
            if isinstance(v, dict) and v.get("mechanism_id") == 683
        ]
        assert len(hits) == 1, hits
        assert "mechanism" + "_683" not in hits[0]

    def test_m684_key_unique_in_entities_profile(self):
        data = _load_yaml(COMPETITOR_ENTITIES)
        parent = data["entities"]["perplexity"]
        hits = [
            k for k, v in parent.items()
            if isinstance(v, dict) and v.get("mechanism_id") == 684
        ]
        assert len(hits) == 1, hits
        assert "mechanism" + "_684" not in hits[0]

    def test_window_mechanisms_682_683_684_counts_repo_wide(self):
        # All three are single-block mechanisms in singular `mechanism_id:`
        # form. (683's careers backlink uses the plural `mechanism_ids`
        # list form on the Kate Conger entry, verified separately in
        # TestM683CongerDiscipline - unlike #743's Hamish Hector entry,
        # which carries singular `mechanism_id: 680` and counted twice.)
        ids = _mechanism_ids_from_files(_profile_yaml_paths())
        assert ids.count(682) == 1, f"mechanism_id 682 count {ids.count(682)}"
        assert ids.count(683) == 1, f"mechanism_id 683 count {ids.count(683)}"
        assert ids.count(684) == 1, f"mechanism_id 684 count {ids.count(684)}"

    def test_no_descriptive_key_literals_in_this_file(self):
        # Regression guard for the #745-class breakage: #745's literal
        # descriptive-key references left #742's committed uniqueness test
        # red. This file resolves blocks by mechanism_id walk only. The
        # #747/#748/#749 test filenames legitimately embed descriptive-key
        # fragments (they are those runs' own files, referenced here only
        # as backlink-existence checks), so they are stripped before the
        # fragment scan.
        own = open(os.path.join(TESTS_DIR, TEST_BASENAME), encoding="utf-8").read()
        for fn in (M682_TEST_FILE, M683_TEST_FILE, M684_TEST_FILE):
            own = own.replace(fn, "")
        # Fragments themselves are built by concatenation so the check does
        # not trip on its own literals.
        for frag in (
            "wsj_openai_clash_" + "money_safety",
            "kate_conger_nyt_x_" + "adversarial",
            "getty_perplexity_" + "visual_licensing",
        ):
            assert frag not in own, f"descriptive key fragment in own file: {frag}"


# -- m682 discipline -------------------------------------------------------

class TestM682WSJClashExposeDiscipline:
    def test_block_identity_fields(self):
        b = _m682_block()
        assert b["mechanism_id"] == 682
        assert b["iteration"] == 747
        assert b["iteration_type"] == "A"
        assert b["type"] == "competitor_coverage_deep_dive"
        assert b["type_label"] == "Competitor Coverage Deep Dive"

    def test_scorer_block_manual_illustrative_values(self):
        s = _m682_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["target_entity"] == "openai"
        assert s["peer_arm"] == "same_publication_same_day_relay_pair"
        assert s["expose_score_MANUAL_ILLUSTRATIVE"] == -0.40
        assert s["relay_scores_MANUAL_ILLUSTRATIVE"] == [0.10, 0.05]
        assert s["relay_avg"] == 0.075
        assert s["delta"] == -0.475
        assert s["is_significant"] is False

    def test_scorer_discipline_not_calculated(self):
        s = _m682_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "NOT_CALCULATED" in s["p_value"]
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert "Engine NOT run" in s["methodology"]

    def test_tightest_temporal_register_mix_note(self):
        s = _m682_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "Tightest temporal register-mix" in s["delta_note"]
        assert "0.65" in s["register_range_note"]

    def test_statistical_discipline_string(self):
        sd = _m682_block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE only" in sd
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in sd
        assert "is_significant false" in sd
        assert "engine NOT run" in sd
        assert "verdict directionally_supported_not_proven" in sd
        assert "NOT artifact-grade" in sd
        assert "no analysis.json update warranted" in sd

    def test_finding_register_mix_inconclusive(self):
        folded = _fold(_m682_block()["finding"])
        assert "Register MIXES within 24 hours on the same payer" in folded
        assert "Incentive attribution is INCONCLUSIVE" in folded
        assert "NOT a falsification-family member" in folded
        assert "Ledger holds at 24" in folded
        assert "NOT artifact-grade" in folded
        assert "Correlation is not causation" in folded

    def test_no_analysis_json_update_flag(self):
        assert _m682_block()["no_analysis_json_update"] is True

    def test_correlation_not_causation_flag(self):
        assert _m682_block()["correlation_not_causation"] is True

    def test_anchor_article_identity(self):
        a = _m682_block()["articles_this_run"][0]
        assert a["title"] == "How the Clash Between Money and Safety Created a Monumental Crisis for AI"
        assert a["byline"] == "Robert McMillan, Amrith Ramkumar, Keach Hagey, Erin Woo"
        assert a["date"] == "2026-09-14"
        assert a["tone_MANUAL_ILLUSTRATIVE"] == -0.40
        assert a["register"] == "enterprise_watchdog_expose"

    def test_type_a_747_test_file_exists(self):
        assert os.path.exists(os.path.join(TESTS_DIR, M682_TEST_FILE))


# -- m683 discipline -------------------------------------------------------

class TestM683CongerDiscipline:
    def test_block_identity_fields(self):
        b = _m683_block()
        assert b["mechanism_id"] == 683
        assert b["iteration"] == 748
        assert b["rotation_type"] == "B"
        assert b["journalist"] == "Kate Conger"
        assert b["publication"] == "The New York Times"
        assert b["finding_type"] == "journalist_cross_entity"
        assert b["competitor"] == "X-AI-labs"

    def test_verdict_directional_only(self):
        assert _m683_block()["verdict"] == "directionally_supported_not_proven"

    def test_x_musk_arm_pinned(self):
        folded = _fold(_m683_block()["finding"])
        assert "Character Limit: How Elon Musk Destroyed Twitter" in folded

    def test_ai_lab_arm_pinned(self):
        folded = _fold(_m683_block()["finding"])
        assert "Anthropic Researchers Raise Alarm Over A.I. Acceleration" in folded

    def test_statistical_discipline_in_finding(self):
        folded = _fold(_m683_block()["finding"])
        assert "MANUAL ILLUSTRATIVE" in folded
        assert "p_value" in folded
        assert "cohens_d" in folded
        assert "is_significant" in folded
        assert "engine NOT run" in folded
        assert "NOT artifact-grade" in folded

    def test_not_falsification_family(self):
        folded = _fold(_m683_block()["finding"])
        assert "NOT a falsification-family member" in folded
        assert "ledger holds at 24" in folded
        assert "Correlation is not causation" in folded

    def test_test_file_backlink_and_count(self):
        b = _m683_block()
        assert b["test_file"] == "tests/" + M683_TEST_FILE
        assert b["test_count"] == 34
        assert os.path.exists(os.path.join(TESTS_DIR, M683_TEST_FILE))

    def test_source_urls_count(self):
        assert len(_m683_block()["source_urls"]) == 7

    def test_careers_entry_mechanism_ids_backlink_683(self):
        entry = _kate_conger_entry()
        assert 683 in entry["mechanism_ids"]

    def test_careers_notes_backlink_683(self):
        notes = _fold(_kate_conger_entry()["notes"])
        assert "mechanism 683" in notes
        assert "Type B #748" in notes


# -- m684 discipline -------------------------------------------------------

class TestM684GettyPerplexityDiscipline:
    def test_block_identity_fields(self):
        b = _m684_block()
        assert b["mechanism_id"] == 684
        assert b["iteration"] == 749
        assert b["iteration_type"] == "C"
        assert b["type"] == "financial_incentive_mapping"
        assert b["type_label"] == "Financial Incentive Mapping"

    def test_statistical_discipline_qualitative_only(self):
        sd = _fold(_m684_block()["statistical_discipline"])
        assert "Qualitative Type C mapping" in sd
        assert "p_value NOT_CALCULATED" in sd
        assert "cohens_d NOT_CALCULATED" in sd
        assert "ci_95 NOT_CALCULATED" in sd
        assert "Engine NOT run" in sd
        assert "NOT artifact-grade" in sd
        assert "directionally_supported_not_proven" in sd
        assert "no coverage-tone claim" in sd

    def test_tone_not_scored(self):
        assert _m684_block()["tone_scores"] == "NOT_SCORED"

    def test_not_falsification_family(self):
        ff = _fold(_m684_block()["falsification_family"])
        assert "NOT a falsification-family member" in ff
        assert "ledger holds at 24" in ff

    def test_no_coverage_tone_claim(self):
        assert _m684_block()["no_coverage_tone_claim"] is True

    def test_cautious_language_required(self):
        assert _m684_block()["cautious_language_required"] is True

    def test_no_causal_claim(self):
        assert "No causal claim" in _fold(_m684_block()["correlational_note"])

    def test_first_dedicated_mapping_novelty(self):
        assert "FIRST dedicated corpus mapping of Getty Images x Perplexity" in _fold(
            _m684_block()["novelty"]
        )

    def test_source_urls_count(self):
        assert len(_m684_block()["source_urls"]) == 8

    def test_verification_block(self):
        v = _m684_block()["verification"]
        assert v["iteration"] == 749
        assert v["yaml_parse_clean"] is True
        assert v["ascii_only"] is True

    def test_type_c_749_test_file_exists(self):
        assert os.path.exists(os.path.join(TESTS_DIR, M684_TEST_FILE))


# -- falsification ledger ----------------------------------------------------

class TestFalsificationLedger750:
    @staticmethod
    def _profiles_corpus():
        return "\n".join(
            open(p, encoding="utf-8").read() for p in _profile_yaml_paths()
        )

    def test_twenty_fourth_present(self):
        assert "TWENTY-FOURTH" in self._profiles_corpus()

    def test_twenty_fifth_absent(self):
        assert "TWENTY-FIFTH" not in self._profiles_corpus()


# -- post-#749 corpus integrity --------------------------------------------

class TestCorpusIntegrityPost749:
    def test_max_mechanism_id_is_684(self):
        ids = _mechanism_ids_from_files(_profile_yaml_paths())
        assert max(ids) == MECH_MAX, f"max mechanism_id {max(ids)} != {MECH_MAX}"

    def test_zero_mechanism_685_keys_in_profiles(self):
        # Concatenation keeps the contiguous underscore form out of this
        # file's own text; the sweep logic itself is the only mention.
        for p in _profile_yaml_paths():
            text = open(p, encoding="utf-8").read()
            assert "mechanism" + "_685" not in text, f"mechanism 685 key in {p}"

    def test_zero_m684_underscore_keys_in_other_tests(self):
        # No test file carries the contiguous underscore form for 684: the
        # #747/#748/#749 sweep instruments all use concatenation, and this
        # file resolves blocks by mechanism_id walk. Own file is the carrier
        # only via its concatenated sweep logic (excluded per #715).
        hits = []
        for fn in sorted(os.listdir(TESTS_DIR)):
            if not fn.endswith(".py") or fn == TEST_BASENAME:
                continue
            text = open(os.path.join(TESTS_DIR, fn), encoding="utf-8").read()
            if "mechanism" + "_684_" in text:
                hits.append(fn)
        assert hits == [], f"mechanism 684 underscore keys in test files: {hits}"

    def test_window_mechanisms_682_683_684_present(self):
        ids = _mechanism_ids_from_files(_profile_yaml_paths())
        assert {682, 683, 684} <= set(ids)

    def test_749_max_684_sweep_stays_green(self):
        # Type D adds no mechanisms: #749's test_max_mechanism_id_is_684
        # remains true post-#750 by construction.
        ids = _mechanism_ids_from_files(_profile_yaml_paths())
        assert max(ids) == 684

    def test_748_max_683_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to 684
        # supersedes #748's test_max_mechanism_id_is_683 per the #710/#720
        # convention.
        ids = _mechanism_ids_from_files(_profile_yaml_paths())
        assert max(ids) == 684

    def test_designed_keying_no_underscore_682_683_684_in_profiles(self):
        # The #723/#738/#739 designed-keying convention: mechanism ids
        # advance in colon form only; block keys carry no underscore-form
        # mechanism key substring. Trailing-underscore form matches the
        # committed sweep instruments (#747/#748/#749).
        corpus = "\n".join(
            open(p, encoding="utf-8").read() for p in _profile_yaml_paths()
        )
        for n in ("682", "683", "684"):
            assert "mechanism" + "_" + n + "_" not in corpus, \
                f"underscore-form mechanism {n} key in profiles"


# -- engine verification on fresh synthetic corpora -------------------------

_PS = datetime(2026, 9, 1)
_PE = datetime(2026, 9, 14)

_STRONG_T = [0.71, 0.63, 0.78, 0.66, 0.59]
_STRONG_P = [-0.44, -0.52, -0.39, -0.57, -0.48]
_NULL_T = [0.03, -0.05, 0.06, -0.02, 0.01]
_NULL_P = [-0.04, 0.03, -0.01, 0.05, -0.02]
_DEGEN_T = [0.42]
_DEGEN_P = [-0.51]


class TestEngineFreshCorpora750:
    def test_strong_signal_pair_is_significant_at_engine_layer(self):
        r = calculate_asymmetry(_STRONG_T, _STRONG_P, "tgt", ["peer"], "slug", _PS, _PE)
        assert r.asymmetry_score == pytest.approx(1.154, rel=1e-9)
        assert r.t_statistic == pytest.approx(25.45037897327402, rel=1e-9)
        assert r.p_value == pytest.approx(6.367391986424009e-09, rel=1e-9)
        assert r.cohens_d == pytest.approx(16.0962329740007, rel=1e-9)
        assert r.is_significant is True

    def test_strong_signal_ci_above_zero(self):
        r = calculate_asymmetry(_STRONG_T, _STRONG_P, "tgt", ["peer"], "slug", _PS, _PE)
        assert r.confidence_interval_lower == pytest.approx(1.076, abs=1e-9)
        assert r.confidence_interval_upper == pytest.approx(1.2340499999999999, abs=1e-9)
        assert r.confidence_interval_lower > 0

    def test_strong_signal_arm_swap_negates(self):
        r = calculate_asymmetry(_STRONG_P, _STRONG_T, "peer", ["tgt"], "slug", _PS, _PE)
        assert r.asymmetry_score == pytest.approx(-1.154, rel=1e-9)

    def test_near_null_pair_stays_silent(self):
        r = calculate_asymmetry(_NULL_T, _NULL_P, "tgt", ["peer"], "slug", _PS, _PE)
        assert r.asymmetry_score == pytest.approx(0.003999999999999998, rel=1e-9)
        assert r.t_statistic == pytest.approx(0.1581138830084189, rel=1e-9)
        assert r.p_value == pytest.approx(0.878364558371825, rel=1e-9)
        assert r.p_value > 0.05
        assert r.cohens_d == pytest.approx(0.09999999999999995, rel=1e-9)
        assert r.is_significant is False

    def test_near_null_ci_crosses_zero(self):
        r = calculate_asymmetry(_NULL_T, _NULL_P, "tgt", ["peer"], "slug", _PS, _PE)
        assert r.confidence_interval_lower == pytest.approx(-0.04000000000000001, abs=1e-9)
        assert r.confidence_interval_upper == pytest.approx(0.044000000000000004, abs=1e-9)
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_n1_per_arm_contract(self):
        r = calculate_asymmetry(_DEGEN_T, _DEGEN_P, "tgt", ["peer"], "slug", _PS, _PE)
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(r.asymmetry_score) == pytest.approx(0.9299999999999999, rel=1e-9)

    def test_degenerate_arm_swap_negates(self):
        r = calculate_asymmetry(_DEGEN_P, _DEGEN_T, "peer", ["tgt"], "slug", _PS, _PE)
        assert r.asymmetry_score == pytest.approx(-0.9299999999999999, rel=1e-9)


# -- #745 suite tombstone ----------------------------------------------------

class TestFullSuiteTombstone745:
    """The #745 re-launched background 39K suite died mid-run (log stalled at
    1431 bytes / 3% progress since Sep 14 18:53 UTC; no pytest alive at this
    run's check) - TENTH consecutive background death. Re-launched this run
    to goal hidden_files type_d_750_full_suite.log; next Type D run checks
    it."""

    @staticmethod
    def _log_path():
        return os.path.join(GOAL_HIDDEN, "type_d_745_full_suite.log")

    def test_745_suite_log_exists(self):
        assert os.path.exists(self._log_path()), "the #745 suite log must exist"

    def test_745_suite_stalled_at_1431_bytes(self):
        size = os.path.getsize(self._log_path())
        assert size == 1431, f"expected the stalled 1431-byte log, got {size}"

    def test_745_suite_progress_capped_at_3pct(self):
        text = open(self._log_path(), encoding="utf-8", errors="replace").read()
        pcts = [int(x) for x in re.findall(r"\[\s*(\d+)%\]", text)]
        assert pcts, "no progress markers in the #745 suite log"
        assert max(pcts) == 3, f"expected progress capped at 3%, got {max(pcts)}%"

    def test_745_death_earlier_than_740_death_point(self):
        # The lineage of nine deaths ended at 50% (#740); this tenth death
        # stalled at 3% - an earlier stall point, same failure class
        # (background suite death mid-run, no pytest alive at check).
        text = open(self._log_path(), encoding="utf-8", errors="replace").read()
        pcts = [int(x) for x in re.findall(r"\[\s*(\d+)%\]", text)]
        assert max(pcts) < 50, "tenth death should stall earlier than #740's 50%"
        assert os.path.getsize(self._log_path()) < 21777, \
            "tenth death log should be smaller than #740's 21777-byte death log"


# -- Rotation guard / novelty anchor (#565 convention) ------------------------

class TestRotationCycleGuard750:
    ANCHORED_SHA = ANCHORED_SHA

    @staticmethod
    def _rotation_files():
        result = {}
        for fn in os.listdir(TESTS_DIR):
            m = re.match(r"test_type_([a-e])_(\d+)_", fn)
            if m:
                result.setdefault(int(m.group(2)), []).append((m.group(1), fn))
        return result

    def test_25_rotation_files_contiguous(self):
        files = self._rotation_files()
        for n in range(726, 751):
            assert n in files and len(files[n]) == 1, \
                f"iteration {n} file missing or duplicated: {files.get(n)}"
            letter, fn = files[n][0]
            expected = "deabc"[(n - 710) % 5]
            assert letter == expected, f"iteration {n}: expected type {expected}, file is {fn}"

    def test_window_746_750_closes_e_to_d(self):
        files = self._rotation_files()
        assert files[746][0][0] == "e"
        assert files[747][0][0] == "a"
        assert files[748][0][0] == "b"
        assert files[749][0][0] == "c"
        assert files[750][0][0] == "d"
        assert files[750][0][1] == TEST_BASENAME

    def test_749_was_type_c_in_window(self):
        files = self._rotation_files()
        assert files[749][0][0] == "c"

    def test_rotation_adjacency_cycle_valid(self):
        files = self._rotation_files()
        order = "deabc"
        for n in range(726, 750):
            cur = files[n][0][0]
            nxt = files[n + 1][0][0]
            assert nxt == order[(order.index(cur) + 1) % 5], \
                f"rotation break between #{n} ({cur}) and #{n + 1} ({nxt})"

    def test_anchor_is_main_commit_patched_in_followup(self):
        """Rotation window 746-750 closes E->D. Anchor patched in followup per #565.

        The main commit is selected robustly: followup and push-pending-note
        commits also carry the "Type D #750:" subject, so the naive newest-match
        would shadow the main commit once the note is committed (the #735
        hardening, kept here).
        """
        result = _git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines()
            if "Type D #750:" in line
            and "followup" not in line
            and "push-pending note" not in line
        ]
        assert len(mains) == 1, f"expected exactly one Type D #750 main commit, got {mains}"
        main = mains[0].split()[0]
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


# -- Doc-sync ratchet ----------------------------------------------------------

class TestDocSyncRatchet750:
    """README / ARCHITECTURE / iteration-log rows land pre-main-commit."""

    def test_readme_test_file_table_row(self):
        content = open(os.path.join(REPO_ROOT, "README.md"), encoding="utf-8").read()
        assert TEST_BASENAME in content

    def test_architecture_tree_row(self):
        content = open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"), encoding="utf-8").read()
        assert TEST_BASENAME in content

    def test_iteration_log_tail_750(self):
        # Recent runs (#736 and later) append entries at the end of
        # iteration-log.md (the file head stays frozen at #735 per #735's
        # committed doc-sync test), so the #750 entry is asserted at the
        # tail. Window widened to 8000 chars: this run's entry is ~7625
        # chars (three mechanism verifications + keying-hygiene note +
        # tombstone lineage + push-status followups), so #745's 7000-char
        # window would miss its header.
        tail = open(LOG, encoding="utf-8").read()[-8000:]
        assert "#750 Type D:" in tail, tail[-200:]
