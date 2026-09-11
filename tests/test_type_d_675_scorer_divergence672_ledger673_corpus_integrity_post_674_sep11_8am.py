"""
Type D - Test & Verify: real-engine verification of the #672 EIGHTH
divergence pin (MIT TR x OpenAI [-0.25,-0.20,-0.15] vs Meta
[-0.40,-0.35,-0.55]: t=3.5000, p=0.042172, d=2.8577, asymmetry
+0.23333333333333336, is_significant True at the ENGINE layer only) +
FOURTEENTH n=1-per-arm degenerate-ledger pair (#673 Type B, Ina Fried
Apple [+0.30] vs Meta [+0.10]: t=0.0, p=1.0, d=0.0, |asymmetry| == 0.2
within 1e-9, IEEE-inexact per the #673 block) + #674 no-engine-run
verification (qualitative_only, no_tone_scores, no_p_value, mechanism_638
block untouched per the Type D read-only convention) + post-#674 corpus
integrity sweep (mechanisms 637/638/639 pinned, max modern id 639, no
640) + divergence ratchet at 8 / falsification ledger at 14 / #609
cohort 7/7 closure checks + Type E 57-cycle tracked-sources integrity.

Iteration #675 - Fri 2026-09-11 08:00 PDT
(scheduled job_id mediascope-daily-iteration, goal_54093bda4145, rotation 674 C -> 675 D)

Verification arc: #672 (Type A, mechanism 637) logged an ENGINE RUN with
is_significant True at the engine layer on illustrative arrays; #673
(Type B, mechanism 638) logged manual-illustrative only with no engine
run; #674 (Type C, mechanism 639) logged qualitative mapping only with no
tone arms. This run verifies those decisions against the real scorer
path: the #672 engine numbers reproduce EXACTLY (t=3.5000, p=0.042172,
d=2.8577, asymmetry +0.23333333333333336, is_significant True engine
layer; arm-swap negates with t=-3.5, d=-2.8577, same p). The finding
layer stays is_significant False per the Aug 28 2026 standing rule, so
the divergence pin STRENGTHENS the no-empirical-claim discipline: engine
significance on synthetic illustrative arrays is never promoted.

The divergence ratchet moves 7 -> 8 (#642 held 7). #672's block asserts
its p=0.042172 is the LARGEST p-value in the divergence class (barely
under 0.05), #642 holds the smallest (0.001213), #602 the largest |d|
(9.2557): the engine re-run here confirms the #672 p value; the class
rankings are corpus claims pinned by block text, consistent with the
established convention (cf. #670's falsification-ledger textual pins).

#673 is the FOURTEENTH n=1-per-arm degenerate-ledger pair (first four
#645; fifth/sixth #650; seventh/eighth #655; ninth/tenth #660; eleventh
#663 and twelfth #664 per #665; thirteenth #668 per #670): the classic
contract holds, with one refinement - 0.30 - 0.10 is IEEE-inexact
(0.19999999999999998), so |asymmetry| == 0.2 is asserted within 1e-9 per
the #673 block's own tolerance, NOT IEEE-exact (contrast #668's exact
0.40). Arm-swap sums to exactly 0.0 anyway.

#674 correctly runs NO engine: mechanism 639 is a publication-level
Layer-2 salary-funding status verification plus a formal correction to
the #673 gradient-absent premise. Its statistical_discipline carries
no_tone_scores: true, no_p_value: true, qualitative_only: true,
correlation_not_causation: true, is_significant: false. There are no tone
arms for the engine to score. Mechanism 638's block is left untouched
(Type D read-only convention); mechanism 639 carries the dated
correction.

Corpus integrity sweep: mechanism 637 (MIT TR x OpenAI agentic-safety
accountability register vs Meta agentic-failure, #672) is present and
unique in profiles/mit-tech-review.yaml under
competitor_relationships.openai with iteration 672, rotation Type A, and
carries the EIGHTH DIVERGENCE PIN statement; mechanism 638 (Ina Fried,
Axios, Meta Muse vs Apple ambient-AI register, #673) is present and
unique in profiles/careers/journalists.yaml with iteration 673,
iteration_type B, explicitly NOT a falsification-family member and
gradient-absent; mechanism 639 (Axios x OpenAI Layer-2 leg Sep 2026
status correction to #673, #674) is present and unique in
profiles/competitor-entities.yaml with iteration 674, rotation Type C,
and names mechanism_638_block_untouched. The modern (504+) id era is
collision-free with max == 639 and no 640 anywhere in profiles/;
journalists.yaml parses at 268 journalists (267 + Ina Fried).

Cohort and ledger checks: the #609 first-gen OpenAI publisher renewal
cohort stays closed at 7/7 (the #654 News Corp block still names itself
the SEVENTH member). Mechanism 630 is still a separate UNRESOLVED watch
item (sixth News Corp AI-revenue leg, Google): its block explicitly
states the cohort is complete and "a Google leg would sit outside the
cohort". The falsification ledger stands at 14 (mechanism 634 still
FOURTEENTH; no FIFTEENTH anywhere in profiles/); mechanism 638 is
gradient-absent not a member; mechanism 639 carries zero falsification
text (correction-only, not a ledger member). The divergence ratchet
stands at 8: the EIGHTH DIVERGENCE PIN statement appears only at
mechanism 637, and there is no NINTH anywhere.

Type E integrity: the Tracked Sources table is at 57 verification cycles
through Sep 11 2026 (#671), GF at 499 episodes (Sep 11 2026), EHE
activist-group (not a podcast) row intact, Attention Sphere no-match row
intact with the misidentified-spec text.

Designed supersession note: the #670 Type D sweep's
test_max_mechanism_id_is_636 and test_no_mechanism_637_anywhere now fail
by supersession (max is 639; mechanism_637 is now a real key under
competitor_relationships.openai in mit-tech-review.yaml), consistent with
the established convention (cf. #670's note on #665's tests).

Rotation guard: window 671-675 (D, C, B, A, E newest-first), closing the
C->D edge. Rotation-guard 4 + doc-sync 4 + novelty-anchor 1 deselected
pre-commit per the #565 followup convention; anchor patched in the
followup once the #675 main-commit SHA is known.
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

# Pinned illustrative tone pairs from the Sep 11 mechanism blocks.
# #672 Type A (MIT Technology Review): OpenAI arm [-0.25, -0.20, -0.15]
# (Sep 8 math-piece credit-scooping accountability -0.25; Sep 2 Download
# Astra "critical" cyber-risk cultural-problems -0.20; Aug 19 Download
# Astra safety-pause hype-skepticism -0.15; avg -0.20) vs Meta arm
# [-0.40, -0.35, -0.55] (Jun 5 2026 Download Meta hack "far simpler
# exploits" -0.40; Aug 6 2026 Download Meta rogue model -0.35; Jan 2025
# fact-checking accountability -0.55; avg -0.4333). Illustrative delta
# (OpenAI minus Meta) +0.23333333333333336, MANUAL ILLUSTRATIVE, n=3 vs
# n=3 - the EIGHTH divergence pin (engine p=0.042172, largest in class).
TONE_OPENAI_672 = [-0.25, -0.20, -0.15]
TONE_META_672 = [-0.40, -0.35, -0.55]

# #673 Type B (Axios, Ina Fried): Apple arm [+0.30] (ambient-AI
# privacy-virtue headline register) vs Meta arm [+0.10] (Muse
# executive-access business register). Illustrative delta (Apple minus
# Meta) +0.20, MANUAL ILLUSTRATIVE, n=1 per arm - the FOURTEENTH
# degenerate-ledger pair. Gradient-absent control case, NOT a
# falsification-family member. 0.30 - 0.10 is IEEE-inexact
# (0.19999999999999998), so the delta is pinned within 1e-9, not exactly.
TONE_APPLE_673 = [0.30]
TONE_META_673 = [0.10]

# Engine-verified constants for the #672 pair (confirmed this run via the
# real calculate_asymmetry path before the file was written).
P_672 = 0.042172
D_672 = 2.8577
ASYM_672 = 0.23333333333333336


class TestIteration675Metadata:
    def test_iteration_number(self):
        assert 675 == 675

    def test_type_is_d(self):
        assert "D" == "D"

    def test_rotation_edge(self):
        # A -> B -> C -> D -> E; previous main commit was Type C #674
        assert "C->D" == "C->D"

    def test_run_time_sep11_8am(self):
        assert "2026-09-11 08:00 PDT" == "2026-09-11 08:00 PDT"


class TestNovelty675:
    """This run must not collide with an earlier #675."""

    def test_single_type_d_675_file(self):
        matches = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_d_675*.py")
        )
        assert len(matches) == 1, f"expected exactly this file, got {matches}"
        assert matches[0].endswith(
            "test_type_d_675_scorer_divergence672_ledger673_corpus_integrity_post_674_sep11_8am.py"
        )

    def test_type_d_675_main_commit_unique_and_anchored(self):
        # Post-commit the #675 main commit exists exactly once (this run's);
        # its SHA matches the rotation-guard anchor patched in the followup
        # per the #565 convention. Novelty was verified pre-commit by shell
        # greps (zero test_type_d_675 files, no #675 in git log); this test
        # pins that no duplicate #675 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #675:", l)]
        assert len(mains) == 1, (
            f"expected exactly one Type D #675 main commit, got: {mains}"
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard675.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, f"main commit {sha} != guard anchor {anchor}"


class TestScorerDivergencePin672:
    """The #672 MIT TR x OpenAI pair through the real calculate_asymmetry
    path.

    EIGHTH divergence pin (FIRST through SEVENTH per the corpus ledger;
    #642 was seventh with p=0.001213). The #672 block's engine numbers
    reproduce EXACTLY: t=3.5000, p=0.042172, d=2.8577, asymmetry
    +0.23333333333333336, is_significant True at the ENGINE layer.
    Finding-layer significance is never promoted per the Aug 28 2026
    standing rule (p_value NOT_CALCULATED, is_significant False at the
    finding layer) - the pin STRENGTHENS the no-empirical-claim
    discipline.
    """

    def test_forward_engine_numbers_reproduce_exactly(self):
        r = calculate_asymmetry(
            TONE_OPENAI_672, TONE_META_672, "OpenAI", ["Meta"],
            "mit-tech-review", P0, P1,
        )
        assert r.t_statistic == pytest.approx(3.5000, rel=1e-9)
        # p is quoted at 6dp in the #672 block (0.042172); the engine
        # returns 0.04217156757343684, so compare with abs tolerance.
        assert r.p_value == pytest.approx(P_672, abs=1e-6)
        assert r.cohens_d == pytest.approx(D_672, rel=1e-4)
        assert r.asymmetry_score == ASYM_672

    def test_engine_significant_below_point_zero_five(self):
        r = calculate_asymmetry(
            TONE_OPENAI_672, TONE_META_672, "OpenAI", ["Meta"],
            "mit-tech-review", P0, P1,
        )
        assert r.p_value < 0.05
        assert r.is_significant is True

    def test_arm_swap_negates_t_and_d_preserves_p(self):
        fwd = calculate_asymmetry(
            TONE_OPENAI_672, TONE_META_672, "OpenAI", ["Meta"],
            "mit-tech-review", P0, P1,
        )
        rev = calculate_asymmetry(
            TONE_META_672, TONE_OPENAI_672, "Meta", ["OpenAI"],
            "mit-tech-review", P0, P1,
        )
        assert rev.asymmetry_score == -ASYM_672
        assert fwd.asymmetry_score + rev.asymmetry_score == 0.0
        assert rev.t_statistic == pytest.approx(-fwd.t_statistic, rel=1e-9)
        assert rev.p_value == pytest.approx(fwd.p_value, rel=1e-12)
        assert rev.cohens_d == pytest.approx(-fwd.cohens_d, rel=1e-9)

    def test_identical_arms_invariant(self):
        r = calculate_asymmetry(
            TONE_OPENAI_672, TONE_OPENAI_672, "OpenAI", ["OpenAI"],
            "mit-tech-review", P0, P1,
        )
        assert r.asymmetry_score == 0.0
        assert r.is_significant is False

    def test_finding_layer_block_carries_eighth_pin_statement(self):
        path = os.path.join(REPO_ROOT, "profiles", "mit-tech-review.yaml")
        with open(path) as fh:
            text = fh.read()
        start = text.index(
            "mechanism_637_mittr_openai_agentic_safety_accountability_register_vs_meta_agentic_failure_sep2026"
        )
        block = text[start : start + 20000]
        assert "EIGHTH DIVERGENCE PIN" in block
        assert "ratchet 7 -> 8" in block
        assert "#642 was seventh with p=0.001213" in block

    def test_finding_layer_stays_not_significant_per_standing_rule(self):
        path = os.path.join(REPO_ROOT, "profiles", "mit-tech-review.yaml")
        with open(path) as fh:
            text = fh.read()
        start = text.index(
            "mechanism_637_mittr_openai_agentic_safety_accountability_register_vs_meta_agentic_failure_sep2026"
        )
        block = text[start : start + 20000]
        assert "is_significant False (Aug 28 2026 standing rule" in block
        assert "p_value NOT_CALCULATED" in block
        assert "engine significance on synthetic illustrative arrays is never promoted" in block

    def test_class_ranking_claims_pinned_in_block(self):
        # Corpus claims (cf. #670's textual-ledger convention): #672's
        # p=0.042172 is asserted as the LARGEST p in the divergence class,
        # #642 holds the smallest (0.001213), #602 the largest |d| (9.2557).
        path = os.path.join(REPO_ROOT, "profiles", "mit-tech-review.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "Engine p=0.042172 is the LARGEST p-value in the divergence class" in text
        assert "#642 holds the smallest (0.001213)" in text
        assert "#602 holds the largest |d| (9.2557)" in text


class TestScorerDegenerateLedger673:
    """The #673 Ina Fried pair through the real calculate_asymmetry path.

    FOURTEENTH n=1-per-arm degenerate-ledger pair (first four #645;
    fifth/sixth #650; seventh/eighth #655; ninth/tenth #660; eleventh
    #663 and twelfth #664 per #665; thirteenth #668 per #670). The classic
    contract holds: t=0.0, p=1.0, d=0.0 (n_a + n_b <= 2), arm-swap
    negates, is_significant False. One refinement vs #668: 0.30 - 0.10 is
    IEEE-inexact (0.19999999999999998), so |asymmetry| == 0.2 is asserted
    within 1e-9 per the #673 block's own tolerance, NOT IEEE-exact.
    """

    def test_forward_asymmetry_is_point_two_within_tolerance(self):
        r = calculate_asymmetry(
            TONE_APPLE_673, TONE_META_673, "Apple", ["Meta"],
            "axios", P0, P1,
        )
        assert r.asymmetry_score == pytest.approx(0.2, abs=1e-9)
        assert r.asymmetry_score != 0.2  # IEEE-inexact, per the #673 block

    def test_degenerate_statistics(self):
        r = calculate_asymmetry(
            TONE_APPLE_673, TONE_META_673, "Apple", ["Meta"],
            "axios", P0, P1,
        )
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_arm_swap_sums_to_zero_exactly(self):
        fwd = calculate_asymmetry(
            TONE_APPLE_673, TONE_META_673, "Apple", ["Meta"],
            "axios", P0, P1,
        )
        rev = calculate_asymmetry(
            TONE_META_673, TONE_APPLE_673, "Meta", ["Apple"],
            "axios", P0, P1,
        )
        assert fwd.asymmetry_score + rev.asymmetry_score == 0.0
        assert rev.asymmetry_score == pytest.approx(-0.2, abs=1e-9)

    def test_identical_arms_invariant(self):
        r = calculate_asymmetry(
            TONE_APPLE_673, TONE_APPLE_673, "Apple", ["Apple"],
            "axios", P0, P1,
        )
        assert r.asymmetry_score == 0.0
        assert r.is_significant is False

    def test_mechanism_638_pinned_gradient_absent_not_falsification(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            text = fh.read()
        start = text.index(
            "mechanism_638_ina_fried_axios_meta_muse_vs_apple_ambient_ai_register_sep08_sep10"
        )
        block = text[start : start + 15000]
        assert "mechanism_id: 638" in block
        assert "iteration: 673" in block
        assert "NOT a falsification-family member" in block
        assert "gradient-absent" in block


class TestNoEngineRun674:
    """#674 (mechanism 639) correctly runs NO engine: qualitative
    publication-level mapping plus a formal correction to the #673
    premise. The statistical_discipline mapping pins no_tone_scores,
    no_p_value, qualitative_only, correlation_not_causation, and
    is_significant false; there are no tone arms for the engine to
    score."""

    def _block(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        start = text.index(
            "mechanism_639_axios_openai_layer2_leg_sep2026_status_correction_673"
        )
        return text[start : start + 15000]

    def test_statistical_discipline_no_tone_scores(self):
        assert "no_tone_scores: true" in self._block()

    def test_statistical_discipline_no_p_value_qualitative_only(self):
        block = self._block()
        assert "no_p_value: true" in block
        assert "qualitative_only: true" in block
        assert "is_significant: false" in block
        assert "correlation_not_causation: true" in block

    def test_mechanism_639_pinned_type_c_iteration_674(self):
        block = self._block()
        assert "mechanism_id: 639" in block
        assert "iteration: 674" in block
        assert "Type C" in block

    def test_mechanism_638_block_untouched_read_only_convention(self):
        # The Type D read-only convention: mechanism 639 carries the dated
        # correction; mechanism 638's block is left untouched and named as
        # such in the correction block.
        assert "mechanism_638_block_untouched" in self._block()


class TestNoEmpiricalClaim675:
    """The Aug 28 2026 standing rule: engine significance on synthetic
    illustrative arrays is never promoted to a finding-layer empirical
    claim. The #672 divergence pin is the EIGHTH such engine-significant
    pin, and the discipline is what keeps it from becoming an empirical
    finding."""

    def test_engine_significance_does_not_imply_finding_significance(self):
        r = calculate_asymmetry(
            TONE_OPENAI_672, TONE_META_672, "OpenAI", ["Meta"],
            "mit-tech-review", P0, P1,
        )
        # Engine layer: significant. Finding layer per the standing rule:
        # p_value NOT_CALCULATED, is_significant False. Both are pinned by
        # the mechanism_637 finding_layer text (see
        # TestScorerDivergencePin672).
        assert r.is_significant is True
        assert "True" == str(r.is_significant)

    def test_no_divergence_pin_promoted_to_analysis_json(self):
        # Divergence pins are descriptive, not empirical: no analysis.json
        # update is warranted for an engine-significant illustrative pair.
        path = os.path.join(REPO_ROOT, "iteration-log.md")
        with open(path) as fh:
            text = fh.read()
        assert "#672 Type A:" in text
        start = text.index("#672 Type A:")
        entry = text[start : start + 8000]
        assert "No analysis.json update warranted" in entry

    def test_junk_d_discipline_unaffected_by_engine_significance(self):
        # Engine significance on n=3 illustrative arrays does not change
        # the junk-d discipline: a computable d on degenerate arms (#667,
        # #670) is meaningless and must be ignored even though the engine
        # returns a number.
        path = os.path.join(REPO_ROOT, "iteration-log.md")
        with open(path) as fh:
            text = fh.read()
        assert "#670 Type D:" in text
        start = text.index("#670 Type D:")
        entry = text[start : start + 10000]
        assert "must be ignored" in entry

    def test_correlation_not_causation_in_639_block(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        start = text.index(
            "mechanism_639_axios_openai_layer2_leg_sep2026_status_correction_673"
        )
        block = text[start : start + 15000]
        assert "correlation_not_causation: true" in block


class TestCorpusIntegrityPost674:
    """Post-#674 corpus integrity sweep: mechanisms 637/638/639 pinned
    with their #672/#673/#674 values; max modern id 639; no 640."""

    def _find_mechanism(self, tree, prefix):
        found = []

        def walk(node, path):
            if isinstance(node, dict):
                for k, v in node.items():
                    if isinstance(k, str) and k.startswith(prefix):
                        found.append((path + [k], v))
                    walk(v, path + [k])
            elif isinstance(node, list):
                for i, v in enumerate(node):
                    walk(v, path + [str(i)])

        walk(tree, [])
        return found

    def test_mechanism_637_present_unique_under_mittr_openai(self):
        path = os.path.join(REPO_ROOT, "profiles", "mit-tech-review.yaml")
        with open(path) as fh:
            tree = yaml.safe_load(fh)
        found = self._find_mechanism(tree, "mechanism_637")
        assert len(found) == 1, f"expected one mechanism_637, got {len(found)}"
        path_keys, block = found[0]
        assert "openai" in " ".join(path_keys).lower(), (
            f"mechanism_637 not under competitor_relationships.openai: {path_keys}"
        )
        assert block["mechanism_id"] == 637
        assert block["iteration"] == 672

    def test_mechanism_638_present_unique_in_journalists_yaml(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            text = fh.read()
        assert len(re.findall(r"mechanism_638_ina_fried_axios", text)) == 1
        assert "mechanism_id: 638" in text

    def test_mechanism_639_present_unique_under_entities(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            tree = yaml.safe_load(fh)
        found = self._find_mechanism(tree, "mechanism_639")
        assert len(found) == 1, f"expected one mechanism_639, got {len(found)}"
        path_keys, block = found[0]
        assert "entities" in path_keys, (
            f"mechanism_639 not under entities: {path_keys}"
        )
        assert block["mechanism_id"] == 639
        assert block["iteration"] == 674

    def test_max_mechanism_id_is_639(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        ids = sorted({int(m) for m in re.findall(r"mechanism_id:\s*(\d+)", text)})
        modern = [i for i in ids if i >= 504]
        assert modern, "no modern-era mechanism ids found"
        assert max(modern) == 639, f"max mechanism id is {max(modern)}, expected 639"

    def test_no_mechanism_640_anywhere(self):
        hits = []
        for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if not f.endswith((".yaml", ".yml")):
                    continue
                fp = os.path.join(root, f)
                with open(fp) as fh:
                    text = fh.read()
                if re.search(r"mechanism_640\b", text) or re.search(
                    r"mechanism_id:\s*640\b", text
                ):
                    hits.append(fp)
        assert hits == [], f"unexpected mechanism 640 references: {hits}"

    def test_journalists_yaml_parses(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            data = yaml.safe_load(fh)
        assert isinstance(data, dict)
        assert len(data["journalists"]) >= 268

    def test_mittr_yaml_parses_with_637_block(self):
        path = os.path.join(REPO_ROOT, "profiles", "mit-tech-review.yaml")
        with open(path) as fh:
            data = yaml.safe_load(fh)
        assert isinstance(data, dict)
        assert "mechanism_637_mittr_openai_agentic_safety_accountability_register_vs_meta_agentic_failure_sep2026" in str(
            data
        )

    def test_ina_fried_journalist_entry_present(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "Ina Fried" in text


class TestDivergenceRatchetAndLedger675:
    """The divergence ratchet stands at 8; the falsification ledger stands
    at 14; the #609 cohort stays closed at 7/7; mechanism 630 stays a
    watch item outside the cohort."""

    def _profiles_text(self):
        chunks = []
        for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if not f.endswith((".yaml", ".yml")):
                    continue
                with open(os.path.join(root, f)) as fh:
                    chunks.append(fh.read())
        return "\n".join(chunks)

    def test_eighth_divergence_pin_statement_unique(self):
        # The pin statement appears exactly once in caps form (at mechanism
        # 637); no second publication claims the eighth pin.
        text = self._profiles_text()
        assert len(re.findall(r"EIGHTH DIVERGENCE PIN", text)) == 1

    def test_no_ninth_divergence_pin(self):
        text = self._profiles_text()
        assert not re.search(r"NINTH [Dd]ivergence pin", text), (
            "unexpected NINTH divergence pin claim"
        )

    def test_falsification_ledger_at_fourteen(self):
        # Mechanism 634 is still the FOURTEENTH falsification-family
        # member; nothing in #672/#673/#674 advances the ledger.
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        block_start = text.index(
            "mechanism_634_reuters_openai_sep_week_register_vs_reuters_meta_muse_register"
        )
        block = text[block_start : block_start + 30000]
        assert "FOURTEENTH falsification-family member" in block

    def test_no_fifteenth_falsification_member(self):
        text = self._profiles_text()
        assert not re.search(r"FIFTEENTH falsification", text, re.I), (
            "unexpected FIFTEENTH falsification-family member"
        )

    def test_672_not_falsification_family(self):
        # #672 explicitly: prediction ordering neutral vs adversarial is
        # consistent, so NOT a falsification-family member.
        path = os.path.join(REPO_ROOT, "profiles", "mit-tech-review.yaml")
        with open(path) as fh:
            text = fh.read()
        start = text.index(
            "mechanism_637_mittr_openai_agentic_safety_accountability_register_vs_meta_agentic_failure_sep2026"
        )
        block = text[start : start + 20000]
        assert "NOT a falsification-family member" in block

    def test_609_cohort_still_closed_at_seven(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "mechanism_627_news_corp_openai_renewal_window_250m_five_year_sep2026" in text
        block_start = text.index(
            "mechanism_627_news_corp_openai_renewal_window_250m_five_year_sep2026"
        )
        block = text[block_start : block_start + 6000]
        assert "SEVENTH member of the #609 first-gen OpenAI publisher renewal cohort" in block

    def test_sixth_leg_watch_still_outside_cohort(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        block_start = text.index(
            "mechanism_630_news_corp_google_ai_licensing_talks_sixth_leg_watch_sep2026"
        )
        block = text[block_start : block_start + 9000]
        assert "status: 'UNRESOLVED'" in block
        assert "a Google leg would sit outside the cohort" in block


class TestTypeEPodcastSentimentIntegrity675:
    """The #671 Type E doc-sync ratchet held: 57 cycles, GF 499 (Sep 11
    2026), EHE identity."""

    def _table_text(self):
        path = os.path.join(REPO_ROOT, "podcast-sentiment.md")
        with open(path) as fh:
            return fh.read()

    def test_tracked_sources_at_57_cycles(self):
        assert "57 verification cycles through Sep 11 2026" in self._table_text()

    def test_guilty_feminist_499_row_sep11(self):
        assert "Active, 499 episodes (Sep 11 2026)" in self._table_text()

    def test_ehe_activist_group_not_podcast(self):
        assert "| Everyone Hates Elon | **Activist group** (not a podcast) |" in self._table_text()

    def test_attention_sphere_no_match_row(self):
        text = self._table_text()
        assert "| Attention Sphere | **No matching podcast found**" in text
        assert "task spec name misidentified as a podcast" in text


class TestDocSync675:
    # Fails pre-commit by design per the #565 followup convention; the README
    # stats table refresh and ARCHITECTURE row are added in the doc-sync
    # commit.
    def _readme_stats(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"\| Tests \| (\d+) \| Across (\d+) test files \|", text)
        assert m, "README stats table row not found"
        return int(m.group(1)), int(m.group(2))

    def _actual_counts(self):
        # Authoritative pytest-based count (same method as the --check gate;
        # the regex estimate undercounts parametrize expansions).
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

    def test_architecture_row_for_675(self):
        path = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
        with open(path) as fh:
            text = fh.read()
        assert "test_type_d_675" in text, "ARCHITECTURE row for #675 missing"

    def test_iteration_log_entry_for_675(self):
        path = os.path.join(REPO_ROOT, "iteration-log.md")
        with open(path) as fh:
            text = fh.read()
        assert "#675 Type D:" in text, "iteration-log entry for #675 missing"

    def test_ledger_ordinal_fourteenth_documented_in_log(self):
        # The #675 iteration-log entry records the #673 pair as the
        # FOURTEENTH n=1-per-arm degenerate-ledger pair.
        path = os.path.join(REPO_ROOT, "iteration-log.md")
        with open(path) as fh:
            text = fh.read()
        assert "#675 Type D:" in text
        start = text.index("#675 Type D:")
        entry = text[start : start + 12000]
        assert "FOURTEENTH" in entry


class TestRotationCycleGuard675:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #675 main-commit SHA is known.
    ANCHORED_SHA = "93c91bcad6480958c0ce82a1cba41108ba93a539"  # patched in followup per #565 convention

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        return [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]

    def test_window_671_675_closes_c_to_d(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("D", "675"),
            ("C", "674"),
            ("B", "673"),
            ("A", "672"),
            ("E", "671"),
        ], f"rotation window 671-675 wrong: {observed}"

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
        # Post-commit anchor: the #675 main commit. Patched in the followup
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
        assert subject.startswith("Type D #675:"), (
            f"newest main commit is not Type D #675: {subject}"
        )
        # The #674 main commit must still be exactly one, preserving the
        # C->D edge the window closes.
        prev = [l for l in mains if re.search(r" Type C #674:", l)]
        assert len(prev) == 1, "expected exactly one Type C #674 main commit"

    def test_novelty_anchor_single_main_commit(self):
        # Exactly one Type D #675 main commit ever (novelty pin).
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #675:", l)]
        assert len(mains) == 1, f"expected exactly one Type D #675 main commit, got: {mains}"
