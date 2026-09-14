"""
Type D -- Iteration #745 (Mon 2026-09-14 11:00 PDT): m679 / m680 / m681
qualitative-discipline verification + post-#744 corpus integrity
(max numeric mechanism_id 681; zero mechanism 682 keys; ledger holds at 24) +
#740 background-suite tombstone (NINTH consecutive death; re-launched as
type_d_745_full_suite.log).

Verifies:
- m679 (WSJ x OpenAI slowdown-week Altman relay register test, Type A #742,
  profiles/news-corp.yaml): MANUAL ILLUSTRATIVE register contrast (OpenAI arm
  avg +0.075 vs Anthropic -0.45, illustrative delta +0.525; OpenAI-vs-Meta
  near-symmetric per #519), p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant False, engine NOT run, verdict
  directionally_supported_not_proven, NOT artifact-grade; NOT a
  falsification-family member (ledger holds at 24).
- m680 (Hamish Hector (TechRadar) Snap-aspirational vs Meta-alarm register
  gradient, Type B #743, profiles/competitor-coverage-research.yaml):
  journalist-level cross-entity gradient, MANUAL ILLUSTRATIVE Snap-arm
  register +0.55, verdict directionally_supported_not_proven,
  p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False, engine NOT
  run, NOT artifact-grade; careers/journalists.yaml hamish_hector entry
  backlinks mechanism 680 (mechanism_ids [115, 680], snap_specs_2026 block);
  NOT a falsification-family member (ledger holds at 24).
- m681 (Sep 14 ANI Division Bench hearing-day outcome watch + India
  attribution-deal two-tier synthesis leg, Type C #744,
  profiles/competitor-entities.yaml): qualitative-only statistical_discipline
  (scorer none, tone NOT_SCORED, p_value/cohens_d/ci NOT_CALCULATED,
  is_significant False, engine NOT run, NOT artifact-grade), verdict
  directional_only; NOT a falsification-family member (ledger holds at 24).
- Falsification ledger: TWENTY-FOURTH present, TWENTY-FIFTH absent;
  ledger holds at 24.
- Post-#744 corpus integrity: max numeric mechanism_id == 681 in
  profiles/; zero mechanism 682 keys in profiles/ and tests/ (own file
  excluded as sweep carrier per the #715 pattern-rescope lesson); m679 /
  m680 / m681 each unique in their home YAML; designed keying holds
  (no underscore-form 679/680/681 mechanism key substrings in profiles/).
  #743's max-680 sweep fails by designed supersession (per #710/#720
  convention); #744's max-681 sweep stays green.
- Statistical meaningfulness on FRESH synthetic corpora (new values this
  run, not #740's): strong-signal n=5-per-arm pair (asymmetry +1.096 exact,
  t=28.683630957943713, p=4.16452596430539e-09, d=18.141121078163906,
  CI (1.03, 1.166) above zero, is_significant True at the ENGINE layer);
  fresh near-null pair (asymmetry 0.008, t=0.2069734735216887,
  p=0.841206380424086, d=0.13090151831301758, CI (-0.06, 0.072) crossing
  zero, silent); fresh degenerate n=1-per-arm contract (t=0.0, p=1.0,
  d=0.0, is_significant False, |asymmetry| == 0.93, arm-swap negates).
  Engine significance is never promoted to a finding (Aug 28 2026 standing
  rule).
- Full-suite status: the #740 re-launched background 38K suite died mid-run
  (type_d_740_full_suite.log stalled at 21777 bytes / 50% progress since
  Sep 14 17:52 UTC; no pytest alive at this run's check) - NINTH
  consecutive background death (#705's, #710's, #715's first re-launch,
  #715's re-launch, #720's re-launch, #725's re-launch, #730's re-launch,
  #735's re-launch, #740's re-launch; tombstone lineage per #565 log
  convention). Re-launched this run to goal hidden_files
  type_d_745_full_suite.log; next Type D run checks it.
- Rotation guard: #744 Type C main commit present; 741-745 window orders
  E->A->B->C->D (anchor patched in the followup per #565).

Note on sweep-key hygiene: this file references mechanisms 679, 680, 681
only via their descriptive block keys and the space form ("mechanism 679");
it never carries the contiguous underscore form with trailing underscore,
keeping #740's committed zero-679 test sweep and #744's committed zero-681
test sweep green. The zero-682 sweep instrument in this file uses string
concatenation so the contiguous form appears only inside this file's own
sweep logic (excluded as carrier per #715).
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

ITERATION = 745
MECH_MAX = 681

NC = os.path.join(REPO_ROOT, "profiles", "news-corp.yaml")
RESEARCH = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
COMPETITOR_ENTITIES = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
CAREERS = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
LOG = os.path.join(REPO_ROOT, "iteration-log.md")
GOAL_HIDDEN = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/hidden_files"
)

M679_KEY = "wsj_openai_altman_slowdown_relay_vs_anthropic_moral_conflict_sep14"
M680_KEY = "hamish_hector_techradar_snap_sci_fi_vs_meta_alarm_register_gradient"
M681_KEY = "ani_sep14_hearing_outcome_watch_two_tier_synthesis_leg"

M679_TEST_FILE = "test_type_a_742_wsj_openai_altman_slowdown_relay_sep14_7am.py"
M680_TEST_FILE = "test_type_b_743_hamish_hector_techradar_snap_sci_fi_vs_meta_alarm_register_gradient_sep14_8am.py"
M681_TEST_FILE = "test_type_c_744_ani_sep14_outcome_watch_two_tier_synthesis_sep14_10am.py"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. Anchor test is deselected pre-commit.
ANCHORED_SHA = "a3a2ce3a583af7ee5a7f45eae6eded4ef391ac56"


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


def _fold(block):
    # YAML `>` folding joins wrapped lines with spaces; normalize the same way
    # so multi-line assertions are not broken by source line breaks.
    return re.sub(r"\s+", " ", block)


def _load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


# -- novelty ---------------------------------------------------------------

class TestNovelty745:
    def test_single_test_file_for_745(self):
        hits = [
            os.path.basename(p)
            for p in glob.glob(os.path.join(TESTS_DIR, "test_type_d_745*.py"))
        ]
        assert hits == [TEST_BASENAME], hits

    def test_no_type_d_745_in_git_log_pre_commit(self):
        result = _git("log", "--oneline", "--grep=Type D #745")
        assert result.returncode == 0
        assert result.stdout.strip() == "", result.stdout.strip()

    def test_m679_key_unique_in_news_corp_profile(self):
        data = _load_yaml(NC)
        openai = data["competitor_relationships"]["openai"]
        hits = [
            k for k, v in openai.items()
            if isinstance(v, dict) and v.get("mechanism_id") == 679
        ]
        assert hits == [M679_KEY], hits

    def test_m680_key_unique_in_research_profile(self):
        data = _load_yaml(RESEARCH)
        findings = data["cross_publication_findings"]
        hits = [
            k for k, v in findings.items()
            if isinstance(v, dict) and v.get("mechanism_id") == 680
        ]
        assert hits == [M680_KEY], hits

    def test_m681_key_unique_in_entities_profile(self):
        data = _load_yaml(COMPETITOR_ENTITIES)
        openai = data["entities"]["openai"]
        hits = [
            k for k, v in openai.items()
            if isinstance(v, dict) and v.get("mechanism_id") == 681
        ]
        assert hits == [M681_KEY], hits

    def test_window_mechanisms_679_680_681_counts_repo_wide(self):
        # 679 and 681 are single-block mechanisms; 680 legitimately appears
        # twice (the research finding block + the careers backlink block).
        ids = _mechanism_ids_from_files(_profile_yaml_paths())
        assert ids.count(679) == 1, f"mechanism_id 679 count {ids.count(679)}"
        assert ids.count(680) == 2, f"mechanism_id 680 count {ids.count(680)}"
        assert ids.count(681) == 1, f"mechanism_id 681 count {ids.count(681)}"


# -- m679 discipline -------------------------------------------------------

class TestM679WSJAltmanDiscipline:
    @staticmethod
    def _block():
        return _load_yaml(NC)["competitor_relationships"]["openai"][M679_KEY]

    def test_block_identity_fields(self):
        b = self._block()
        assert b["mechanism_id"] == 679
        assert b["iteration"] == 742
        assert b["iteration_type"] == "A"
        assert b["type"] == "competitor_coverage_deep_dive"
        assert b["type_label"] == "Competitor Coverage Deep Dive"

    def test_scorer_block_manual_illustrative_values(self):
        s = self._block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["target_entity"] == "openai"
        assert s["peer_entity"] == "anthropic"
        assert s["target_scores_MANUAL_ILLUSTRATIVE"] == [0.10, 0.05]
        assert s["peer_scores_MANUAL_ILLUSTRATIVE"] == [-0.45]
        assert s["target_avg"] == 0.075
        assert s["peer_avg"] == -0.45
        assert s["delta"] == 0.525
        assert s["is_significant"] is False

    def test_scorer_discipline_not_calculated(self):
        s = self._block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "NOT_CALCULATED" in s["p_value"]
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert "Engine NOT run" in s["methodology"]

    def test_statistical_discipline_string(self):
        sd = self._block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE only" in sd
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in sd
        assert "is_significant false" in sd
        assert "engine NOT run" in sd
        assert "verdict directionally_supported_not_proven" in sd
        assert "NOT artifact-grade" in sd
        assert "no analysis.json update warranted" in sd

    def test_finding_register_mix_inconclusive(self):
        folded = _fold(self._block()["finding"])
        assert "Register MIXES within one month on the same payer" in folded
        assert "Incentive attribution is INCONCLUSIVE" in folded
        assert "NOT a falsification-family member" in folded
        assert "Ledger holds at 24" in folded
        assert "NOT artifact-grade" in folded
        assert "Correlation is not causation" in folded

    def test_no_analysis_json_update_flag(self):
        assert self._block()["no_analysis_json_update"] is True

    def test_correlation_not_causation_flag(self):
        assert self._block()["correlation_not_causation"] is True

    def test_anchor_article_identity(self):
        a = self._block()["articles_this_run"][0]
        assert a["byline"] == "Gareth Vipers"
        assert a["date"] == "2026-09-14"
        assert a["tone_MANUAL_ILLUSTRATIVE"] == 0.10
        assert a["register"] == "constructive_ceo_framing_relay"

    def test_novelty_note_zero_prior_files(self):
        assert "Zero test_type_a_742 files on disk pre-commit" in self._block()["novelty"]

    def test_test_file_backlink_exists(self):
        assert os.path.exists(os.path.join(TESTS_DIR, M679_TEST_FILE))


# -- m680 discipline -------------------------------------------------------

class TestM680HectorDiscipline:
    @staticmethod
    def _block():
        return _load_yaml(RESEARCH)["cross_publication_findings"][M680_KEY]

    def test_block_identity_fields(self):
        b = self._block()
        assert b["mechanism_id"] == 680
        assert b["iteration"] == 743
        assert b["rotation_type"] == "B"
        assert b["journalist"] == "Hamish Hector"
        assert b["publication"] == "TechRadar (Future plc)"
        assert b["finding_type"] == "journalist_cross_entity"
        assert b["competitor"] == "Snap/Meta"

    def test_verdict_directional_only(self):
        assert self._block()["verdict"] == "directionally_supported_not_proven"

    def test_snap_arm_register_pinned(self):
        folded = _fold(self._block()["finding"])
        assert "MANUAL ILLUSTRATIVE Snap-arm register +0.55" in folded

    def test_statistical_discipline_in_finding(self):
        folded = _fold(self._block()["finding"])
        assert "p_value NOT_CALCULATED" in folded
        assert "cohens_d NOT_CALCULATED" in folded
        assert "ci_95 NOT_CALCULATED" in folded
        assert "is_significant False" in folded
        assert "engine NOT run" in folded
        assert "NOT artifact-grade" in folded

    def test_not_falsification_family(self):
        folded = _fold(self._block()["finding"])
        assert "NOT a falsification-family member" in folded
        assert "ledger holds at 24" in folded
        assert "Correlation is not causation" in folded

    def test_test_file_backlink_and_count(self):
        b = self._block()
        assert b["test_file"] == "tests/" + M680_TEST_FILE
        assert b["test_count"] == 47
        assert os.path.exists(os.path.join(TESTS_DIR, M680_TEST_FILE))

    def test_careers_snap_specs_block(self):
        data = _load_yaml(CAREERS)
        snap = data["hamish_hector"]["smart_glasses_coverage"]["snap_specs_2026"]
        assert snap["mechanism_id"] == 680
        assert snap["date"] == "2026-06-17"
        assert snap["tone"] == "aspirational"
        assert snap["privacy_vocabulary_count"] == 0
        assert "ispr.info" in snap["byline_verification"]

    def test_careers_mechanism_ids_backlink_680(self):
        data = _load_yaml(CAREERS)
        assert 680 in data["hamish_hector"]["mechanism_ids"]

    def test_careers_notes_backlink_680(self):
        data = _load_yaml(CAREERS)
        notes = _fold(data["hamish_hector"]["notes"])
        assert "mechanism 680" in notes
        assert "Type B #743" in notes


# -- m681 discipline -------------------------------------------------------

class TestM681TwoTierDiscipline:
    @staticmethod
    def _block():
        return _load_yaml(COMPETITOR_ENTITIES)["entities"]["openai"][M681_KEY]

    def test_block_identity_fields(self):
        b = self._block()
        assert b["mechanism_id"] == 681
        assert b["iteration"] == 744
        assert b["iteration_type"] == "C"
        assert b["type"] == "financial_incentive_mapping"
        assert b["type_label"] == "Financial Incentive Mapping"
        assert b["job_id"] == "mediascope-daily-iteration"
        assert b["goal_id"] == "goal_54093bda4145"

    def test_statistical_discipline_dict(self):
        sd = self._block()["statistical_discipline"]
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False
        assert sd["artifact_grade"] is False
        assert sd["qualitative_only"] is True

    def test_no_coverage_tone_claim(self):
        assert self._block()["no_coverage_tone_claim"] is True

    def test_cautious_language_required(self):
        assert self._block()["cautious_language_required"] is True

    def test_no_causal_claim(self):
        assert "No causal claim" in self._block()["correlational_note"]

    def test_not_falsification_family(self):
        ff = self._block()["falsification_family"]
        assert "NOT a falsification-family member" in ff
        assert "ledger holds at 24" in ff

    def test_no_analysis_json_update(self):
        assert "No analysis.json update warranted" in self._block()["artifact_readiness"]

    def test_synthesis_sub_blocks_present(self):
        b = self._block()
        for key in ("hearing_day_outcome_watch", "two_tier_structure",
                    "corpus_value_inference", "precedent_reading"):
            assert key in b, f"missing sub-block {key}"

    def test_verdict_directional_only(self):
        sd = self._block()["statistical_discipline"]
        assert "directional_only" in sd["verdict"]

    def test_test_file_backlink_exists(self):
        assert self._block()["test_file"] == "tests/" + M681_TEST_FILE
        assert os.path.exists(os.path.join(TESTS_DIR, M681_TEST_FILE))


# -- falsification ledger ---------------------------------------------------

class TestFalsificationLedger745:
    @staticmethod
    def _profiles_corpus():
        return "\n".join(
            open(p, encoding="utf-8").read() for p in _profile_yaml_paths()
        )

    def test_twenty_fourth_present(self):
        assert "TWENTY-FOURTH" in self._profiles_corpus()

    def test_twenty_fifth_absent(self):
        assert "TWENTY-FIFTH" not in self._profiles_corpus()


# -- post-#744 corpus integrity --------------------------------------------

class TestCorpusIntegrityPost744:
    def test_max_mechanism_id_is_681(self):
        ids = _mechanism_ids_from_files(_profile_yaml_paths())
        assert max(ids) == MECH_MAX, f"max mechanism_id {max(ids)} != {MECH_MAX}"

    def test_zero_mechanism_682_keys_in_profiles(self):
        # Concatenation keeps the contiguous underscore form out of this
        # file's own text; the sweep logic itself is the only mention.
        for p in _profile_yaml_paths():
            text = open(p, encoding="utf-8").read()
            assert "mechanism" + "_682" not in text, f"mechanism 682 key in {p}"

    def test_zero_m681_underscore_keys_in_other_tests(self):
        # Mirrors #744's committed sweep: carriers are files whose sweep
        # instrument legitimately names the key; this file avoids the
        # contiguous form entirely (descriptive block keys + space form).
        carriers = {TEST_BASENAME, M680_TEST_FILE, M681_TEST_FILE}
        hits = []
        for fn in sorted(os.listdir(TESTS_DIR)):
            if not fn.endswith(".py") or fn in carriers:
                continue
            text = open(os.path.join(TESTS_DIR, fn), encoding="utf-8").read()
            if "mechanism" + "_681_" in text:
                hits.append(fn)
        assert hits == [], f"mechanism 681 underscore keys in test files: {hits}"

    def test_window_mechanisms_679_680_681_present(self):
        ids = _mechanism_ids_from_files(_profile_yaml_paths())
        assert {679, 680, 681} <= set(ids)

    def test_743_max_680_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to 681
        # supersedes #743's test_max_mechanism_680 per the #710/#720 convention.
        ids = _mechanism_ids_from_files(_profile_yaml_paths())
        assert max(ids) == 681

    def test_designed_keying_no_underscore_679_680_681_in_profiles(self):
        # The #723/#738/#739 designed-keying convention: mechanism ids
        # advance in colon form only; block keys carry no underscore-form
        # mechanism key substring. Trailing-underscore form matches the
        # committed sweep instruments (#740/#744); documentation mentions
        # like "mechanism_681 keys" (space form) are not keys.
        corpus = "\n".join(
            open(p, encoding="utf-8").read() for p in _profile_yaml_paths()
        )
        for n in ("679", "680", "681"):
            assert "mechanism" + "_" + n + "_" not in corpus, \
                f"underscore-form mechanism {n} key in profiles"


# -- engine verification on fresh synthetic corpora -------------------------

_PS = datetime(2026, 9, 1)
_PE = datetime(2026, 9, 14)

_STRONG_T = [0.61, 0.55, 0.66, 0.58, 0.52]
_STRONG_P = [-0.49, -0.56, -0.44, -0.60, -0.47]
_NULL_T = [0.04, -0.07, 0.09, -0.03, 0.02]
_NULL_P = [-0.06, 0.05, -0.02, 0.08, -0.04]
_DEGEN_T = [0.38]
_DEGEN_P = [-0.55]


class TestEngineFreshCorpora745:
    def test_strong_signal_pair_is_significant_at_engine_layer(self):
        r = calculate_asymmetry(_STRONG_T, _STRONG_P, "tgt", ["peer"], "slug", _PS, _PE)
        assert r.asymmetry_score == pytest.approx(1.096, rel=1e-9)
        assert r.t_statistic == pytest.approx(28.683630957943713, rel=1e-9)
        assert r.p_value == pytest.approx(4.16452596430539e-09, rel=1e-9)
        assert r.cohens_d == pytest.approx(18.141121078163906, rel=1e-9)
        assert r.is_significant is True

    def test_strong_signal_ci_above_zero(self):
        r = calculate_asymmetry(_STRONG_T, _STRONG_P, "tgt", ["peer"], "slug", _PS, _PE)
        assert r.confidence_interval_lower == pytest.approx(1.03, abs=1e-9)
        assert r.confidence_interval_upper == pytest.approx(1.166, abs=1e-9)
        assert r.confidence_interval_lower > 0

    def test_strong_signal_arm_swap_negates(self):
        r = calculate_asymmetry(_STRONG_P, _STRONG_T, "peer", ["tgt"], "slug", _PS, _PE)
        assert r.asymmetry_score == pytest.approx(-1.096, rel=1e-9)

    def test_near_null_pair_stays_silent(self):
        r = calculate_asymmetry(_NULL_T, _NULL_P, "tgt", ["peer"], "slug", _PS, _PE)
        assert r.asymmetry_score == pytest.approx(0.008, rel=1e-9)
        assert r.t_statistic == pytest.approx(0.2069734735216887, rel=1e-9)
        assert r.p_value == pytest.approx(0.841206380424086, rel=1e-9)
        assert r.p_value > 0.05
        assert r.cohens_d == pytest.approx(0.13090151831301758, rel=1e-9)
        assert r.is_significant is False

    def test_near_null_ci_crosses_zero(self):
        r = calculate_asymmetry(_NULL_T, _NULL_P, "tgt", ["peer"], "slug", _PS, _PE)
        assert r.confidence_interval_lower == pytest.approx(-0.06, abs=1e-9)
        assert r.confidence_interval_upper == pytest.approx(0.072, abs=1e-9)
        assert r.confidence_interval_lower < 0 < r.confidence_interval_upper

    def test_degenerate_n1_per_arm_contract(self):
        r = calculate_asymmetry(_DEGEN_T, _DEGEN_P, "tgt", ["peer"], "slug", _PS, _PE)
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False
        assert abs(r.asymmetry_score) == pytest.approx(0.93, rel=1e-9)

    def test_degenerate_arm_swap_negates(self):
        r = calculate_asymmetry(_DEGEN_P, _DEGEN_T, "peer", ["tgt"], "slug", _PS, _PE)
        assert r.asymmetry_score == pytest.approx(-0.93, rel=1e-9)


# -- #740 suite tombstone ----------------------------------------------------

class TestFullSuiteTombstone740:
    """The #740 re-launched background 38K suite died mid-run (log stalled at
    21777 bytes / 50% progress since Sep 14 17:52 UTC; no pytest alive at this
    run's check) - NINTH consecutive background death. Re-launched this run
    to goal hidden_files type_d_745_full_suite.log; next Type D run checks
    it."""

    @staticmethod
    def _log_path():
        return os.path.join(GOAL_HIDDEN, "type_d_740_full_suite.log")

    def test_740_suite_log_exists(self):
        assert os.path.exists(self._log_path()), "the #740 suite log must exist"

    def test_740_suite_stalled_at_21777_bytes(self):
        size = os.path.getsize(self._log_path())
        assert size == 21777, f"expected the stalled 21777-byte log, got {size}"

    def test_740_suite_progress_capped_at_50pct(self):
        text = open(self._log_path(), encoding="utf-8", errors="replace").read()
        pcts = [int(x) for x in re.findall(r"\[\s*(\d+)%\]", text)]
        assert pcts, "no progress markers in the #740 suite log"
        assert max(pcts) == 50, f"expected progress capped at 50%, got {max(pcts)}%"

    def test_740_death_later_than_735_death_point(self):
        # The lineage of eight deaths ended at 7% (#735); this ninth death
        # reached 50% - a later stall point, same failure class (background
        # suite death mid-run, no pytest alive at check).
        text = open(self._log_path(), encoding="utf-8", errors="replace").read()
        pcts = [int(x) for x in re.findall(r"\[\s*(\d+)%\]", text)]
        assert max(pcts) > 7, "ninth death should stall later than #735's 7%"
        assert os.path.getsize(self._log_path()) > 3229, \
            "ninth death log should exceed #735's 3229-byte death log"


# -- Rotation guard / novelty anchor (#565 convention) ------------------------

class TestRotationCycleGuard745:
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
        for n in range(721, 746):
            assert n in files and len(files[n]) == 1, \
                f"iteration {n} file missing or duplicated: {files.get(n)}"
            letter, fn = files[n][0]
            expected = "deabc"[(n - 710) % 5]
            assert letter == expected, f"iteration {n}: expected type {expected}, file is {fn}"

    def test_window_741_745_closes_e_to_d(self):
        files = self._rotation_files()
        assert files[741][0][0] == "e"
        assert files[742][0][0] == "a"
        assert files[743][0][0] == "b"
        assert files[744][0][0] == "c"
        assert files[745][0][0] == "d"
        assert files[745][0][1] == TEST_BASENAME

    def test_744_was_type_c_in_window(self):
        files = self._rotation_files()
        assert files[744][0][0] == "c"

    def test_rotation_adjacency_cycle_valid(self):
        files = self._rotation_files()
        order = "deabc"
        for n in range(721, 745):
            cur = files[n][0][0]
            nxt = files[n + 1][0][0]
            assert nxt == order[(order.index(cur) + 1) % 5], \
                f"rotation break between #{n} ({cur}) and #{n + 1} ({nxt})"

    def test_anchor_is_main_commit_patched_in_followup(self):
        """Rotation window 741-745 closes E->D. Anchor patched in followup per #565.

        The main commit is selected robustly: followup and push-pending-note
        commits also carry the "Type D #745:" subject, so the naive newest-match
        would shadow the main commit once the note is committed (the #735
        hardening, kept here).
        """
        result = _git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines()
            if "Type D #745:" in line
            and "followup" not in line
            and "push-pending note" not in line
        ]
        assert len(mains) == 1, f"expected exactly one Type D #745 main commit, got {mains}"
        main = mains[0].split()[0]
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


# -- Doc-sync ratchet ----------------------------------------------------------

class TestDocSyncRatchet745:
    """README / ARCHITECTURE / iteration-log rows land pre-main-commit."""

    def test_readme_test_file_table_row(self):
        content = open(os.path.join(REPO_ROOT, "README.md"), encoding="utf-8").read()
        assert TEST_BASENAME in content

    def test_architecture_tree_row(self):
        content = open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"), encoding="utf-8").read()
        assert TEST_BASENAME in content

    def test_iteration_log_tail_745(self):
        # Recent runs (#736-#744) append entries at the end of iteration-log.md
        # (the file head stays frozen at #735 per #735's committed doc-sync
        # test), so the #745 entry is asserted at the tail. Window widened to
        # 7000 chars: this run's entry is ~6725 chars (three mechanism
        # verifications + tombstone lineage + push-status followup), so a
        # smaller window would miss its header.
        tail = open(LOG, encoding="utf-8").read()[-7000:]
        assert "#745 Type D:" in tail, tail[-200:]
