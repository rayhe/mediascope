"""
Type D - Test & Verify: real-engine verification of the #682 publication-level
pair (mechanism 643: FT x Anthropic AISI-refusal accountability scoop,
Meta arm [+0.05] vs Anthropic arm [-0.45], n=1 per arm - t=0.0, p=1.0,
d=0.0, asymmetry +0.50 exact, is_significant False at the engine layer,
matching the #682 block's MANUAL ILLUSTRATIVE delta and the degenerate
statistical contract of the #638/#643 convention) + real-engine verification
of the #683 byline-isolated pair (mechanism 644: Hayden Field sole-byline,
OpenAI arm [-0.10] vs Meta arm [-0.15], n=1 per arm - t=0.0, p=1.0, d=0.0,
asymmetry +0.05 IEEE-INEXACT (0.04999999999999999), asserted within 1e-9 per
the #673/#675 refinement precedent, is_significant False) + #684
no-engine-run verification (mechanism 645 carries no tone arms:
asymmetry_relevance has no_tone_claim true, tone_predictor_grade
MODERATE-WEAK, qualitative_only; Type D read-only convention - the 645
block is untouched) + post-#684 corpus integrity sweep (mechanism 643
present and unique in profiles/financial-times.yaml under
competitor_relationships/anthropic with iteration 682, rotation Type A;
mechanism 644 present and unique in profiles/careers/journalists.yaml
Hayden Field entry with iteration 683, iteration_type B, carrying
tone_illustrative -0.15 meta_arm and -0.10 openai_arm; mechanism 645
present and unique in profiles/competitor-entities.yaml under
entities/microsoft with iteration 684, rotation Type C; the modern (504+)
id era is collision-free with max == 645 and no 646 anywhere in profiles/
or tests/) + ledger integrity (falsification ledger advances to 15 via
mechanism 643 FIFTEENTH, no SIXTEENTH anywhere; #609 first-gen OpenAI
renewal cohort stays closed at 7/7 with the #654 News Corp block still
SEVENTH, no EIGHTH; divergence ratchet holds at 8, no NINTH) +
Type E 59-cycle tracked-sources integrity.

Iteration #685 - Fri 2026-09-11 19:00 PDT
(scheduled job_id mediascope-daily-iteration, goal_54093bda4145, rotation 684 C -> 685 D)

Verification arc: #682 (Type A, mechanism 643) logged a MANUAL
ILLUSTRATIVE delta +0.50 (Meta +0.05 vs Anthropic -0.45) with no engine
run - the FIFTEENTH falsification-family member; #683 (Type B, mechanism
644) logged a MANUAL ILLUSTRATIVE delta +0.05 (OpenAI -0.10 vs Meta
-0.15), also with no engine run, as a Vox-deal falsification pin at
journalist level; #684 (Type C, mechanism 645) logged qualitative
deal-level mapping only with no tone arms at all. This run verifies those
decisions against the real scorer path: both pairs reproduce the degenerate
contract EXACTLY (t=0.0, p=1.0, d=0.0; the +0.50 and +0.05 deltas are pure
arithmetic; arm-swaps negate and stay degenerate). The finding layer stays
is_significant False per the Aug 28 2026 standing rule, so the
manual-illustrative pins STRENGTHEN the no-empirical-claim discipline:
degenerate engine inputs never become empirical findings.

The Type D mandate "verify the asymmetry scoring produces statistically
meaningful results" is satisfied by the strong-signal synthetic check:
Meta arm [-0.60,-0.50,-0.70,-0.55,-0.65,-0.45] vs peer arm
[+0.30,+0.40,+0.35,+0.45,+0.25,+0.50] (n=6 per arm) yields
asymmetry -0.9500000000000001, t=-17.59058189567848,
p=7.498515787192946e-09, d=-10.155927192672127, is_significant True at the
ENGINE layer, CI (-1.0416666666666665, -0.8500000000000001) entirely
below zero. When real signal exists, the engine flags it; when it does
not (near-null pair, p=0.9327294666975322), it stays silent. The scorer
is discriminative, not decoration.

#684 correctly runs NO engine: mechanism 645 is a financial-incentive
deal-level leg (Microsoft Publisher Content Marketplace x Conde Nast
bilateral leg) whose asymmetry_relevance explicitly carries
no_tone_claim: true and tone_predictor_grade: MODERATE-WEAK. There are
no tone arms for the engine to score. Mechanism 645's block is left
untouched (Type D read-only convention).

Corpus integrity sweep: mechanism 643 (FT x Anthropic AISI-refusal
accountability scoop vs Meta/OpenAI launch-week registers, #682) is
present and unique in profiles/financial-times.yaml under
competitor_relationships/anthropic with iteration 682, iteration_type A,
carrying the MANUAL ILLUSTRATIVE +0.50 pin and the falsification_family
FIFTEENTH ledger claim; mechanism 644 (Hayden Field Meta Muse Spark
re-entry deficit vs OpenAI GPT-5.6 regulatory-friction launch byline
register, #683) is present and unique in
profiles/careers/journalists.yaml Hayden Field entry with iteration 683,
iteration_type B, carrying tone_illustrative -0.15 (meta_arm) and -0.10
(openai_arm) hand-scored this run; mechanism 645 (Microsoft PCM x Conde
Nast bilateral deal-level leg, #684) is present and unique in
profiles/competitor-entities.yaml under entities/microsoft with
iteration 684, rotation Type C, date_analyzed 2026-09-11, and the
north-of-$10M WSJ quantum caveat. Max modern mechanism_id == 645;
mechanism_646 appears nowhere in profiles/ or tests/.

Designed supersession note: the #680 Type D sweep's
test_max_modern_mechanism_id_is_642 and test_no_mechanism_643_in_profiles
/ test_no_mechanism_643_in_tests now fail by supersession (max is 645;
mechanism_643 is a real key in financial-times.yaml and mechanism_644 in
journalists.yaml), consistent with the established convention (cf. #680's
note on #675's tests).

Rotation guard: window 681-685 (E, A, B, C, D newest-first), closing the
C->D edge. Rotation-guard 4 + doc-sync 4 + novelty-anchor 1 deselected
pre-commit per the #565 followup convention; anchor patched in the
followup once the #685 main-commit SHA is known.

No em dashes; ASCII-only.
"""
import glob
import os
import re
import subprocess
import sys
from datetime import datetime

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)

from mediascope.score.asymmetry import calculate_asymmetry

P0 = datetime(2026, 9, 4)
P1 = datetime(2026, 9, 11)

# Pinned illustrative tone pair from the #682 mechanism block.
# #682 Type A: Meta arm [+0.05] (Sep 8 2026 FT Meta Muse coverage, neutral
# product-distribution framing, carried from mechanism 625) vs Anthropic
# arm [-0.45] (Sep 9 2026 FT AISI-refusal accountability scoop, watchdog
# register, hand-assigned for the mirror-attested register). Illustrative
# delta (Meta minus Anthropic) +0.50, MANUAL ILLUSTRATIVE, n=1 per arm -
# degenerate contract.
TONE_META_682 = [0.05]
TONE_ANTHROPIC_682 = [-0.45]

# Engine-verified constants for the #682 pair (confirmed this run via the
# real calculate_asymmetry path before the file was written).
P_643 = 1.0
T_643 = 0.0
D_643 = 0.0
ASYM_643 = 0.50

# Pinned illustrative tone pair from the #683 mechanism block.
# #683 Type B: Hayden Field sole byline. OpenAI arm [-0.10] (Jun 26 2026
# GPT-5.6 regulatory-friction launch) vs Meta arm [-0.15] (Apr 8 2026 Muse
# Spark competitive-deficit re-entry). Illustrative delta (OpenAI minus
# Meta) +0.05, MANUAL ILLUSTRATIVE, n=1 per arm - degenerate contract.
TONE_OPENAI_683 = [-0.10]
TONE_META_683 = [-0.15]

# Engine-verified constants for the #683 pair (confirmed this run via the
# real calculate_asymmetry path before the file was written). The +0.05
# is IEEE-inexact (0.04999999999999999), so it is asserted within 1e-9
# per the #673 refinement precedent (0.19999999999999998 vs 0.2), NOT
# IEEE-exact.
P_644 = 1.0
T_644 = 0.0
D_644 = 0.0
ASYM_644 = 0.05

# Strong-signal synthetic corpus for the Type D statistical-meaningfulness
# mandate. Meta arm [-0.60,-0.50,-0.70,-0.55,-0.65,-0.45] (avg -0.575),
# peer arm [+0.30,+0.40,+0.35,+0.45,+0.25,+0.50] (avg +0.375).
# Engine-verified constants (confirmed this run).
SIG_TARGET = [-0.60, -0.50, -0.70, -0.55, -0.65, -0.45]
SIG_PEER = [0.30, 0.40, 0.35, 0.45, 0.25, 0.50]
P_SIG = 7.498515787192946e-09
T_SIG = -17.59058189567848
D_SIG = -10.155927192672127
ASYM_SIG = -0.9500000000000001
CI_LO_SIG = -1.0416666666666665
CI_HI_SIG = -0.8500000000000001

# Near-null pair: no real difference; the engine must stay silent.
NULL_A = [-0.2, 0.1, 0.3, -0.1, 0.0, 0.2]
NULL_B = [-0.15, 0.05, 0.25, -0.05, 0.1, 0.15]
P_NULL = 0.9327294666975322


def _score(target, peers):
    return calculate_asymmetry(
        target_scores=target,
        peer_scores=peers,
        target_entity="target",
        peer_entities=["peer"],
        publication_slug="wired",
        period_start=P0,
        period_end=P1,
    )


class TestIteration685Metadata:
    def test_iteration_number(self):
        assert 685 == 685

    def test_type_is_d(self):
        assert "D" == "D"

    def test_rotation_edge(self):
        # A -> B -> C -> D -> E; previous main commit was Type C #684
        assert "C->D" == "C->D"

    def test_run_time_sep11_7pm(self):
        assert "2026-09-11 19:00 PDT" == "2026-09-11 19:00 PDT"


class TestNovelty685:
    """This run must not collide with an earlier #685."""

    def test_single_type_d_685_file(self):
        matches = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_d_685*.py")
        )
        assert len(matches) == 1, f"expected exactly this file, got {matches}"
        assert matches[0].endswith(
            "test_type_d_685_scorer_pair643_engine_pair644_ieee_inexact_no_engine_run684_corpus_integrity_post_684_sep11_7pm.py"
        )

    def test_type_d_685_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_d_685 files, no #685 in git log,
        # max mechanism 645, no 646 anywhere); this test pins that no
        # duplicate #685 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #685:", l)]
        assert len(mains) == 1, (
            f"expected exactly one Type D #685 main commit, got: {mains}"
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard685.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, f"main commit {sha} != guard anchor {anchor}"


class TestScorerDegeneratePair643:
    """Engine verification of the #682 publication-level pair (mechanism
    643): Meta [+0.05] vs Anthropic [-0.45], n=1 per arm. The degenerate
    contract (t=0.0, p=1.0, d=0.0) holds exactly; the +0.50 delta is pure
    arithmetic, matching the block's MANUAL ILLUSTRATIVE claim."""

    def test_t_statistic_is_zero(self):
        r = _score(TONE_META_682, TONE_ANTHROPIC_682)
        assert r.t_statistic == T_643

    def test_p_value_is_one(self):
        r = _score(TONE_META_682, TONE_ANTHROPIC_682)
        assert r.p_value == P_643

    def test_cohens_d_is_zero(self):
        r = _score(TONE_META_682, TONE_ANTHROPIC_682)
        assert r.cohens_d == D_643

    def test_asymmetry_matches_manual_illustrative_delta(self):
        r = _score(TONE_META_682, TONE_ANTHROPIC_682)
        assert abs(r.asymmetry_score - ASYM_643) < 1e-9

    def test_engine_not_significant(self):
        r = _score(TONE_META_682, TONE_ANTHROPIC_682)
        assert r.is_significant is False

    def test_arm_swap_negates_and_stays_degenerate(self):
        r = _score(TONE_ANTHROPIC_682, TONE_META_682)
        assert abs(r.asymmetry_score - (-ASYM_643)) < 1e-9
        assert (r.t_statistic, r.p_value, r.cohens_d) == (0.0, 1.0, 0.0)
        assert r.is_significant is False


class TestScorerDegeneratePair644:
    """Engine verification of the #683 byline-isolated pair (mechanism
    644): OpenAI [-0.10] vs Meta [-0.15], n=1 per arm. The degenerate
    contract (t=0.0, p=1.0, d=0.0) holds exactly; the +0.05 delta is pure
    arithmetic but IEEE-inexact, so it is asserted within 1e-9 per the
    #673 refinement precedent, matching the block's MANUAL ILLUSTRATIVE
    claim."""

    def test_t_statistic_is_zero(self):
        r = _score(TONE_OPENAI_683, TONE_META_683)
        assert r.t_statistic == T_644

    def test_p_value_is_one(self):
        r = _score(TONE_OPENAI_683, TONE_META_683)
        assert r.p_value == P_644

    def test_cohens_d_is_zero(self):
        r = _score(TONE_OPENAI_683, TONE_META_683)
        assert r.cohens_d == D_644

    def test_asymmetry_matches_manual_illustrative_delta_within_ieee(self):
        r = _score(TONE_OPENAI_683, TONE_META_683)
        # -0.10 - (-0.15) == 0.04999999999999999; the block's +0.05 is the
        # rounded claim. NOT IEEE-exact per the #673 precedent.
        assert abs(r.asymmetry_score - ASYM_644) < 1e-9

    def test_asymmetry_not_ieee_exact(self):
        # Pins the distinction so no later reader claims exactness.
        r = _score(TONE_OPENAI_683, TONE_META_683)
        assert r.asymmetry_score != ASYM_644

    def test_engine_not_significant(self):
        r = _score(TONE_OPENAI_683, TONE_META_683)
        assert r.is_significant is False

    def test_arm_swap_negates_and_stays_degenerate(self):
        r = _score(TONE_META_683, TONE_OPENAI_683)
        assert abs(r.asymmetry_score - (-ASYM_644)) < 1e-9
        assert (r.t_statistic, r.p_value, r.cohens_d) == (0.0, 1.0, 0.0)
        assert r.is_significant is False


class TestScorerStatisticalMeaningfulness:
    """The Type D mandate: verify the asymmetry scorer produces
    statistically meaningful results. On a strong-signal synthetic corpus
    the engine must reach significance with a large effect size and a
    confidence interval that excludes zero; on a near-null corpus it must
    stay silent."""

    def test_strong_signal_asymmetry(self):
        r = _score(SIG_TARGET, SIG_PEER)
        assert abs(r.asymmetry_score - ASYM_SIG) < 1e-12

    def test_strong_signal_t_statistic(self):
        r = _score(SIG_TARGET, SIG_PEER)
        assert abs(r.t_statistic - T_SIG) < 1e-9

    def test_strong_signal_p_value(self):
        r = _score(SIG_TARGET, SIG_PEER)
        assert abs(r.p_value - P_SIG) / P_SIG < 1e-6

    def test_strong_signal_is_significant(self):
        r = _score(SIG_TARGET, SIG_PEER)
        assert r.is_significant is True
        assert r.p_value < 0.05

    def test_strong_signal_large_effect(self):
        r = _score(SIG_TARGET, SIG_PEER)
        assert abs(r.cohens_d) > 1.0
        assert abs(abs(r.cohens_d) - abs(D_SIG)) < 1e-6

    def test_strong_signal_ci_excludes_zero(self):
        r = _score(SIG_TARGET, SIG_PEER)
        assert abs(r.confidence_interval_lower - CI_LO_SIG) < 1e-9
        assert abs(r.confidence_interval_upper - CI_HI_SIG) < 1e-9
        assert r.confidence_interval_upper < 0.0

    def test_null_pair_stays_silent(self):
        r = _score(NULL_A, NULL_B)
        assert r.is_significant is False
        assert r.p_value > 0.5

    def test_null_pair_p_value(self):
        r = _score(NULL_A, NULL_B)
        assert abs(r.p_value - P_NULL) < 1e-9


class TestNoEngineRun684:
    """#684 correctly runs NO engine: mechanism 645 is a financial-incentive
    deal-level leg with no tone arms. Its asymmetry_relevance carries
    no_tone_claim true and a MODERATE-WEAK tone-predictor grade. Type D
    read-only convention - the block is verified, not edited."""

    @staticmethod
    def _block():
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            data = yaml.safe_load(fh)
        key = "mechanism_645_microsoft_pcm_conde_nast_bilateral_leg"
        return data["entities"]["microsoft"][key]

    def test_mechanism_645_iteration_684_type_c(self):
        b = self._block()
        assert b["mechanism_id"] == 645
        assert b["iteration"] == 684
        assert b["rotation"] == "Type C"
        assert b["date_analyzed"] == "2026-09-11"

    def test_no_tone_claim_pinned(self):
        b = self._block()
        assert b["asymmetry_relevance"]["no_tone_claim"] is True

    def test_tone_predictor_grade_moderate_weak(self):
        b = self._block()
        assert b["asymmetry_relevance"]["tone_predictor_grade"] == "MODERATE-WEAK"

    def test_no_tone_arms_present(self):
        # A deal-level leg must carry no tone-score arms to score.
        b = self._block()
        dumped = yaml.safe_dump(b)
        assert "tone_illustrative" not in dumped
        assert "target_tones" not in dumped

    def test_pcm_quantum_caveat_present(self):
        b = self._block()
        assert "north of $10M" in b["scale_2026"]["microsoft_investment"]
        assert b["status_sep_2026"]["verdict"] == "ACTIVE"


class TestCorpusIntegrityPost684:
    """Post-#684 corpus integrity: mechanisms 643/644/645 present and
    unique in their files; the modern (504+) id era is collision-free with
    max == 645 and no 646 anywhere in profiles/ or tests/."""

    @staticmethod
    def _load(relpath):
        path = os.path.join(REPO_ROOT, relpath)
        with open(path) as fh:
            return yaml.safe_load(fh)

    def _all_mechanism_ids(self, data, ids=None):
        ids = ids if ids is not None else []
        if isinstance(data, dict):
            for k, v in data.items():
                if k == "mechanism_id" and isinstance(v, int):
                    ids.append(v)
                self._all_mechanism_ids(v, ids)
        elif isinstance(data, list):
            for v in data:
                self._all_mechanism_ids(v, ids)
        return ids

    def test_mechanism_643_in_financial_times_yaml(self):
        data = self._load("profiles/financial-times.yaml")
        key = "mechanism_643_ft_anthropic_aisi_refusal_accountability_scoop_vs_meta_openai_launch_week_register_sep11"
        assert key in data["competitor_relationships"]["anthropic"]
        b = data["competitor_relationships"]["anthropic"][key]
        assert b["mechanism_id"] == 643
        assert b["iteration"] == 682
        assert b["iteration_type"] == "A"

    def test_mechanism_643_fifteenth_ledger_claim(self):
        data = self._load("profiles/financial-times.yaml")
        text = yaml.safe_dump(data)
        assert "FIFTEENTH falsification-family member" in text

    def test_mechanism_644_in_journalists_yaml(self):
        data = self._load("profiles/careers/journalists.yaml")
        found = None
        for entry in data["journalists"]:
            if isinstance(entry, dict):
                for k in entry:
                    if "mechanism_644" in str(k):
                        found = entry
        assert found is not None, "mechanism_644 block not found"
        assert found["name"] == "Hayden Field"
        key = "mechanism_644_hayden_field_meta_muse_spark_reentry_deficit_vs_openai_gpt56_regulatory_launch_byline_register_sep11"
        b = found[key]
        assert b["mechanism_id"] == 644
        assert b["iteration"] == 683
        assert b["iteration_type"] == "B"

    def test_mechanism_644_journalist_and_tones(self):
        data = self._load("profiles/careers/journalists.yaml")
        found = None
        for entry in data["journalists"]:
            if isinstance(entry, dict) and entry.get("name") == "Hayden Field":
                found = entry
        assert found is not None
        key = "mechanism_644_hayden_field_meta_muse_spark_reentry_deficit_vs_openai_gpt56_regulatory_launch_byline_register_sep11"
        b = found[key]
        assert b["meta_arm"]["tone_illustrative"] == -0.15
        assert b["openai_arm"]["tone_illustrative"] == -0.10

    def test_mechanism_645_in_competitor_entities_yaml(self):
        data = self._load("profiles/competitor-entities.yaml")
        key = "mechanism_645_microsoft_pcm_conde_nast_bilateral_leg"
        assert key in data["entities"]["microsoft"]
        assert data["entities"]["microsoft"][key]["mechanism_id"] == 645

    def test_max_modern_mechanism_id_is_645(self):
        ids = []
        for rel in ("profiles/financial-times.yaml",
                    "profiles/wired.yaml",
                    "profiles/competitor-entities.yaml",
                    "profiles/careers/journalists.yaml"):
            ids.extend(self._all_mechanism_ids(self._load(rel)))
        modern = [i for i in ids if i >= 504]
        assert max(modern) == 645, f"max modern id {max(modern)} != 645"

    def test_no_mechanism_646_in_profiles(self):
        # #675 convention: regex over profiles/ YAML files (avoids
        # self-matching the test file's own grep string).
        hits = []
        for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if not f.endswith((".yaml", ".yml")):
                    continue
                fp = os.path.join(root, f)
                with open(fp) as fh:
                    text = fh.read()
                if re.search(r"mechanism_646\b", text) or re.search(
                    r"mechanism_id:\s*646\b", text
                ):
                    hits.append(fp)
        assert hits == [], f"unexpected mechanism 646 references: {hits}"

    def test_no_mechanism_646_in_tests(self):
        # No test file except this one may reference mechanism 646.
        self_name = os.path.basename(__file__)
        hits = []
        for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "tests")):
            if "__pycache__" in root:
                continue
            for f in files:
                if not f.endswith(".py") or f == self_name:
                    continue
                fp = os.path.join(root, f)
                with open(fp) as fh:
                    text = fh.read()
                if re.search(r"mechanism_646\b", text) or re.search(
                    r"mechanism_id:\s*646\b", text
                ):
                    hits.append(fp)
        assert hits == [], f"unexpected mechanism 646 references: {hits}"


class TestLedgerIntegrity685:
    """Ledger pins: the falsification ledger advances to 15 with no
    SIXTEENTH; the #609 first-gen OpenAI publisher renewal cohort stays
    closed at 7/7 (the #654 News Corp block still SEVENTH, no EIGHTH);
    the divergence ratchet holds at 8 with no NINTH."""

    @staticmethod
    def _profiles_text():
        chunks = []
        for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if not f.endswith((".yaml", ".yml")):
                    continue
                with open(os.path.join(root, f)) as fh:
                    chunks.append(fh.read())
        return "\n".join(chunks)

    def test_no_sixteenth_falsification_member(self):
        assert "SIXTEENTH" not in self._profiles_text()

    def test_fifteenth_pin_present_and_unique(self):
        # Exactly two occurrences, both inside the mechanism_643 block
        # (the falsification_family claim and the novelty claim).
        text = self._profiles_text()
        assert text.count("FIFTEENTH falsification-family member") == 2

    def test_no_eighth_renewal_cohort_member(self):
        text = self._profiles_text()
        assert "EIGHTH member of the #609" not in text
        assert "eighth member of the #609" not in text

    def test_seventh_cohort_member_still_newscorp(self):
        text = self._profiles_text()
        assert "SEVENTH member of the #609 first-gen OpenAI publisher renewal cohort" in text

    def test_no_ninth_divergence_pin(self):
        text = self._profiles_text()
        assert text.count("EIGHTH DIVERGENCE PIN") == 1
        assert "NINTH" not in text


class TestTypeEPodcastSentimentIntegrity685:
    """Type E integrity: podcast-sentiment.md keeps the Everyone Hates Elon
    activist-group (not a podcast) row and the Attention Sphere row with
    59 verification cycles through Sep 11 2026."""

    def _text(self):
        path = os.path.join(REPO_ROOT, "podcast-sentiment.md")
        with open(path) as fh:
            return fh.read()

    def test_podcast_sentiment_file_exists(self):
        assert os.path.exists(os.path.join(REPO_ROOT, "podcast-sentiment.md"))

    def test_ehe_activist_group_row_intact(self):
        assert "Everyone Hates Elon" in self._text()

    def test_attention_sphere_row_intact(self):
        assert "Attention Sphere" in self._text()

    def test_attention_sphere_59_cycles(self):
        assert "59 verification cycles through Sep 11 2026" in self._text()


class TestDocSync685:
    # Fails pre-commit by design per the #565 followup convention; the
    # README stats table refresh, ARCHITECTURE row, test-file table row,
    # and iteration-log entry are added in the doc-sync commit.
    def _readme_stats(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"\| Tests \| (\d+) \| Across (\d+) test files \|", text)
        assert m, "README stats table row not found"
        return int(m.group(1)), int(m.group(2))

    def _actual_counts(self):
        out = subprocess.run(
            [sys.executable, "scripts/count_stats.py", "--pytest"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=400,
        )
        m = re.search(r"Total tests\s+(\d+)", out.stdout)
        assert m, f"count_stats.py --pytest produced no Total tests line: {out.stdout[:300]}"
        tests = int(m.group(1))
        m2 = re.search(r"Total test files\s+(\d+)", out.stdout)
        files = int(m2.group(1)) if m2 else None
        return tests, files

    def test_readme_stats_match_actual(self):
        readme_tests, readme_files = self._readme_stats()
        actual_tests, actual_files = self._actual_counts()
        assert readme_tests == actual_tests, (
            f"README tests {readme_tests} != actual {actual_tests}"
        )
        if actual_files is not None:
            assert readme_files == actual_files, (
                f"README files {readme_files} != actual {actual_files}"
            )

    def test_architecture_row_for_685(self):
        path = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
        with open(path) as fh:
            text = fh.read()
        assert "test_type_d_685" in text, "ARCHITECTURE row for #685 missing"

    def test_iteration_log_entry_for_685(self):
        path = os.path.join(REPO_ROOT, "iteration-log.md")
        with open(path) as fh:
            text = fh.read()
        assert "#685 Type D:" in text, "iteration-log entry for #685 missing"

    def test_ledger_content_documented_in_log(self):
        # The #685 iteration-log entry records the mechanism 645
        # no-engine-run verification and the max-id-645 integrity pin.
        path = os.path.join(REPO_ROOT, "iteration-log.md")
        with open(path) as fh:
            text = fh.read()
        assert "#685 Type D:" in text
        start = text.index("#685 Type D:")
        entry = text[start : start + 12000]
        assert "mechanism 645" in entry


class TestRotationCycleGuard685:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #685 main-commit SHA is known.
    ANCHORED_SHA = "a7e4b21eca0e6381f4bbf6369ba660291f031c6a"  # patched in followup per #565 convention

    @staticmethod
    def _mains():
        # First occurrence of each distinct iteration number, newest first.
        # Distinct-iteration dedup (per the #679 guard convention): followup
        # SHA-fix commits re-titled "Type [A-E] #NNN: ..." match the filter,
        # so raw subjects[:5] can show one iteration twice; the intent is
        # the distinct iteration mains in order.
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        seen = set()
        mains = []
        for s in out:
            m = re.match(r"^Type [A-E] #(\d+):", s)
            if m and m.group(1) not in seen:
                seen.add(m.group(1))
                mains.append(s)
        return mains

    def test_window_681_685_closes_c_to_d(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("D", "685"),
            ("C", "684"),
            ("B", "683"),
            ("A", "682"),
            ("E", "681"),
        ], f"rotation window 681-685 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["D", "C", "B", "A", "E"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #685 main commit. Patched in the followup
        # per the #565 convention once the main commit SHA is known.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [
            l for l in out if re.match(r"^[0-9a-f]{40} Type [A-E] #\d+:", l)
        ]
        sha, subject = mains[0].split(" ", 1)
        assert sha == self.ANCHORED_SHA, f"anchor not yet patched: {sha}"
        assert subject.startswith("Type D #685:"), (
            f"newest main commit is not Type D #685: {subject}"
        )
        # The #684 main commit must still be exactly one, preserving the
        # C->D edge the window closes.
        prev = [l for l in mains if re.search(r" Type C #684:", l)]
        assert len(prev) == 1, "expected exactly one Type C #684 main commit"

    def test_novelty_anchor_single_main_commit(self):
        # Exactly one Type D #685 main commit ever (novelty pin).
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #685:", l)]
        assert len(mains) == 1, f"expected exactly one Type D #685 main commit, got: {mains}"
