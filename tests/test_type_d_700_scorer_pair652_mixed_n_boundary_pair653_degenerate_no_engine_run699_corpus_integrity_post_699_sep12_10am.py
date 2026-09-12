"""
Type D - Test & Verify: real-engine verification of the #697 mixed-n
(n=2 vs n=1) illustrative pair (mechanism 652: Gizmodo Apple Duo arms
[+0.20, +0.45] vs Meta Muse arm [-0.25], block delta (Apple minus Meta)
+0.575) - the NINTH degenerate-boundary pin (junk cohens_d
+3.252691193458 computable while Welch significance degenerates:
t=0.0, p=1.0, is_significant False; the #697 block's parenthetical
"(p=1.0, d=0.0)" is refined this run exactly as #695 refined #692's:
d does NOT degenerate on mixed-n arms, it returns computable junk) +
the #698 n=1-per-arm byline-isolated pair (mechanism 653: Raymond Wong
Gizmodo, Apple Duo hands-on [+0.45] vs Meta Ray-Ban Gen 2 review
[+0.30], block delta +0.15 reproduces at 0.15) - the SIXTEENTH
n=1-per-arm degenerate-ledger pair (first four #645; fifth/sixth #650;
seventh/eighth #655; ninth/tenth #660; eleventh/twelfth #665;
thirteenth #670; fourteenth #675; fifteenth #695) + the Type D
statistical-meaningfulness mandate (fresh strong-signal synthetic
corpus: asym +0.796, t=16.228, p=2.59748e-07, d=10.2635, CI entirely
positive, engine-significant at the engine layer, never promoted to a
finding; fresh near-null corpus p=0.3733 stays silent) + #699
no-engine-run verification (mechanism 654 Apple x Google Gemini
publisher-content bypass leg carries scorer none, tone_scores
NOT_SCORED, qualitative_only true; Type D read-only convention - the
654 block is untouched) + post-#699 corpus integrity sweep (mechanism
652 present and unique in profiles/competitor-entities.yaml under
entities.apple with iteration 697, iteration_type A, pinned arms
[0.2, 0.45]/[-0.25]; mechanism 653 present and unique in
profiles/careers/journalists.yaml under the Raymond Wong entry with
iteration 698, type B, apple_arm tone_illustrative 0.45 and meta_arm
0.30; mechanism 654 present and unique in
profiles/competitor-entities.yaml under entities.apple with iteration
699, rotation Type C; modern (504+) id era collision-free with max ==
654 and no 655 anywhere in profiles/ or tests/) +
falsification-ledger integrity (TWENTIETH via m653 #698; m652 and m654
claim no membership; #609 first-gen OpenAI publisher renewal cohort
stays closed at 7/7, no EIGHTH member; divergence ratchet holds at 8,
no NINTH) + Type E 62-cycle tracked-sources integrity + cross-doc
header agreement (README.md and docs/ARCHITECTURE.md headers agree and
match the test files on disk, per the #690-reinstated guard).

Iteration #700 - Sat 2026-09-12 10:00 PDT
(scheduled job_id mediascope-daily-iteration, goal_54093bda4145, rotation 699 C -> 700 D)

Verification arc: #697 (Type A, mechanism 652) logged a MANUAL
ILLUSTRATIVE delta +0.575 on a mixed-n (n=2 vs n=1) pair with no engine
run; #698 (Type B, mechanism 653) logged a MANUAL ILLUSTRATIVE delta
+0.15 on an n=1-per-arm byline-isolated review-register pair with no
engine run; #699 (Type C, mechanism 654) logged qualitative financial
mapping only with no tone arms at all. This run verifies those
decisions against the real scorer path: the #697 pair reproduces the
degenerate-boundary contract (t=0.0, p=1.0, is_significant False) while
cohens_d returns a computable junk value (+3.252691193458), the #698
pair reproduces the classic degenerate contract EXACTLY (t=0.0, p=1.0,
d=0.0, |asymmetry| == 0.15), and #699 correctly runs no engine. The
finding layer stays is_significant False per the Aug 28 2026 standing
rule, so the manual-illustrative pins STRENGTHEN the no-empirical-claim
discipline: degenerate engine inputs never become empirical findings,
and a computable effect size on degenerate arms is meaningless junk.

The Type D mandate "verify the asymmetry scoring produces
statistically meaningful results" is satisfied by the strong-signal
synthetic check: peer arm [+0.32, +0.21, +0.27, +0.19, +0.36] vs Meta
arm [-0.51, -0.47, -0.63, -0.43, -0.59] (n=5 per arm) yields asymmetry
+0.796, t=16.228009610758, p=2.59748e-07, d=10.263494452219,
is_significant True at the ENGINE layer, CI (0.714, 0.882) entirely
above zero. When real signal exists, the engine flags it; when it does
not (fresh near-null pair, p=0.373341167482), it stays silent. The
scorer is discriminative, not decoration. Engine significance is never
promoted to a finding.

#699 correctly runs NO engine: mechanism 654 (Apple x Google Gemini
multi-year AI deal publisher-content bypass leg, confirmed Jan 12
2026) is a financial-incentive deal-level leg whose
statistical_discipline block carries scorer none, tone_scores
NOT_SCORED, p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, ci_95
NOT_CALCULATED, is_significant false, qualitative_only true,
correlation_not_causation true, artifact_grade false. There are no
tone arms for the engine to score. Mechanism 654's block is left
untouched (Type D read-only convention).

Corpus integrity sweep: mechanism 652 (Gizmodo Apple Duo launch
register vs Gizmodo Meta Muse experiment, #697) is present and unique
in profiles/competitor-entities.yaml under entities.apple with
iteration 697, iteration_type A, carrying the MANUAL ILLUSTRATIVE
+0.575 pin and the three verbatim Gizmodo URL slugs; mechanism 653
(Raymond Wong Gizmodo Duo hands-on vs Ray-Ban Gen 2 review register
constancy, #698) is present and unique in
profiles/careers/journalists.yaml with iteration 698, type B,
journalist Raymond Wong, publication Gizmodo, apple_arm
tone_illustrative 0.45 and meta_arm tone_illustrative 0.30;
mechanism 654 (Apple x Google Gemini publisher-content bypass leg,
#699) is present and unique in profiles/competitor-entities.yaml
under entities.apple with iteration 699, rotation Type C, scorer none.
Max modern mechanism_id == 654; mechanism_655 appears nowhere in
profiles/ or tests/.

Falsification-ledger integrity: m653 holds TWENTIETH (ledger at 20
after #698); m652 and m654 claim no membership; no TWENTY-FIRST
anywhere in profiles/. The #609 first-gen OpenAI publisher renewal
cohort stays closed at 7/7 (News Corp SEVENTH; no EIGHTH member). The
divergence ratchet holds at 8 (#642 still the smallest-p holder), no
NINTH.

Rotation guard: window 696-700 (E, A, B, C, D newest-first), closing
the C->D edge. Rotation-guard 3 + doc-sync 4 + cross-doc 2 +
novelty-anchor 2 deselected pre-commit per the #565 followup
convention; anchors patched in the followup once the #700 main-commit
SHA is known.

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

from mediascope.score.asymmetry import calculate_asymmetry

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(REPO_ROOT, "iteration-log.md")
README = os.path.join(REPO_ROOT, "README.md")
ARCH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
SCRIPTS = os.path.join(REPO_ROOT, "scripts")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")

FILE_700 = "test_type_d_700_scorer_pair652_mixed_n_boundary_pair653_degenerate_no_engine_run699_corpus_integrity_post_699_sep12_10am.py"

# Pinned illustrative tone arms from the #697 mechanism block
# (mechanism_652_gizmodo_apple_duo_launch_register_vs_gizmodo_meta_muse_experiment_sep12).
# Apple arms: Duo launch news +0.20, Duo hands-on (Ray Wong) +0.45.
# Meta arm: Muse experiment -0.25.
TONE_APPLE_697 = [0.2, 0.45]
TONE_META_697 = [-0.25]
DELTA_652_BLOCK = 0.575  # (Apple minus Meta), block: "0.325 - (-0.25) = 0.575"

# Pinned illustrative tone arms from the #698 mechanism block
# (mechanism_653_raymond_wong_duo_hands_on_vs_ray_ban_gen2_review_register_constancy_sep12).
# Apple arm: Duo hands-on +0.45 (carried from #697 hand score).
# Meta arm: Ray-Ban Meta Gen 2 review +0.30 (hand-scored this run).
TONE_APPLE_698 = [0.45]
TONE_META_698 = [0.30]
DELTA_653_BLOCK = 0.15  # (Apple minus Meta)

# Engine values produced this run by direct calculate_asymmetry calls on
# the pinned arms above; constants confirmed before this test file was
# written (research-method rule).
# m652: t=0.0, p=1.0, d=3.252691193458 (junk), asym=0.575, sig False.
# m652 arm-swap: t=0.0, p=1.0, d=-3.252691193458, asym=-0.575.
# m653: t=0.0, p=1.0, d=0.0, asym=0.15, sig False.
EXPECTED_D_652_JUNK = 3.252691193458

# Strong-signal synthetic corpus (fresh this run, n=5 per arm): the
# engine must flag it at the engine layer; significance here is never
# promoted to a finding (Aug 28 2026 standing rule).
STRONG_PEER = [0.32, 0.21, 0.27, 0.19, 0.36]
STRONG_META = [-0.51, -0.47, -0.63, -0.43, -0.59]
EXPECTED_STRONG = {
    "asym": 0.796,
    "t": 16.228009610758,
    "p": 2.59748e-07,
    "d": 10.263494452219,
    "ci_lo": 0.714,
    "ci_hi": 0.882,
}
# Near-null pair (fresh this run): the engine must stay silent.
# Coincidence noted: the p-value matches #695's fresh near-null p to
# 12 decimal places (0.373341167482) through the Welch t-distribution
# mapping, not through arm identity - the arms differ.
NULL_TARGET = [0.05, -0.04, 0.02, -0.01, 0.03]
NULL_PEER = [-0.02, 0.04, -0.06, 0.01, -0.03]
EXPECTED_NULL = {
    "t": 0.943242218284,
    "p": 0.373341167482,
    "d": 0.596558759001,
}

_PERIOD = dict(
    period_start=datetime(2026, 9, 8), period_end=datetime(2026, 9, 11)
)


def _score(target, peer, publication):
    return calculate_asymmetry(
        list(target),
        list(peer),
        target_entity="target",
        peer_entities=["peer"],
        publication_slug=publication,
        **_PERIOD,
    )


# Window files 696-699 must exist and carry README/ARCHITECTURE rows.
WINDOW_FILES = {
    696: "test_type_e_696_podcast_sentiment_62nd_verification_gf499_watch_sep12_6am.py",
    697: "test_type_a_697_gizmodo_apple_duo_launch_register_vs_meta_muse_experiment_sep12_7am.py",
    698: "test_type_b_698_raymond_wong_duo_hands_on_vs_ray_ban_gen2_review_register_constancy_sep12_8am.py",
    699: "test_type_c_699_apple_google_gemini_bypass_leg_sep12_9am.py",
}
EXPECTED_NEWEST_FIRST = [
    (700, "D"),
    (699, "C"),
    (698, "B"),
    (697, "A"),
    (696, "E"),
]

_HEADING_RE = re.compile(r"^#(\d+) Type ([A-E]):", re.MULTILINE)
_COUNT_HEADER_RE = re.compile(r"(\d+) tests\*{0,2} across (\d+) test files")


def _headings():
    """iteration number -> (log position, hour type) for real headings."""
    found = {}
    with open(LOG, encoding="utf-8") as fh:
        text = fh.read()
    for m in _HEADING_RE.finditer(text):
        found.setdefault(int(m.group(1)), (m.start(), m.group(2)))
    return found


def _count_header(doc_text):
    m = _COUNT_HEADER_RE.search(doc_text)
    assert m, "missing 'N tests across M test files' header"
    return int(m.group(1)), int(m.group(2))


def _yaml(path):
    with open(os.path.join(REPO_ROOT, path), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _profiles_text():
    chunks = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for f in files:
            if not f.endswith((".yaml", ".yml")):
                continue
            with open(os.path.join(root, f), encoding="utf-8") as fh:
                chunks.append(fh.read())
    return "\n".join(chunks)


class TestIteration700Metadata:
    def test_docstring_ids(self):
        doc = __doc__
        assert "iteration #700" in doc.lower()
        assert "2026-09-12" in doc
        assert "Type D" in doc
        assert "goal_54093bda4145" in doc
        assert "mediascope-daily-iteration" in doc

    def test_rotation_c_to_d(self):
        assert "rotation 699 C -> 700 D" in __doc__

    def test_filename_convention(self):
        assert os.path.basename(__file__) == FILE_700

class TestScorerMixedNBoundaryPair652:
    """The #697 Gizmodo pair (Apple [0.20, 0.45] n=2 vs Meta [-0.25]
    n=1) is the NINTH degenerate-boundary pin: Welch significance
    degenerates (t=0.0, p=1.0, is_significant False) while cohens_d
    returns a computable junk value (+3.252691193458). This run also
    refines the #697 block's parenthetical "(p=1.0, d=0.0)": exactly as
    #695 refined #692's, d does NOT degenerate on mixed-n arms (the
    n=1 arm contributes zero variance, so the pooled sd collapses to
    the n=2 arm's own sd). Junk, and must be ignored per the Aug 28
    2026 standing rule."""

    def test_t_statistic_is_zero(self):
        r = _score(TONE_APPLE_697, TONE_META_697, "gizmodo")
        assert r.t_statistic == 0.0

    def test_p_value_is_one(self):
        r = _score(TONE_APPLE_697, TONE_META_697, "gizmodo")
        assert r.p_value == 1.0

    def test_cohens_d_is_computable_junk(self):
        # The boundary refinement: d does NOT degenerate on mixed-n
        # arms. Junk, and must be ignored per the Aug 28 2026 standing
        # rule.
        r = _score(TONE_APPLE_697, TONE_META_697, "gizmodo")
        assert abs(r.cohens_d - EXPECTED_D_652_JUNK) < 1e-9

    def test_asymmetry_matches_manual_illustrative_delta(self):
        r = _score(TONE_APPLE_697, TONE_META_697, "gizmodo")
        assert abs(r.asymmetry_score - DELTA_652_BLOCK) < 1e-9

    def test_engine_not_significant(self):
        r = _score(TONE_APPLE_697, TONE_META_697, "gizmodo")
        assert r.is_significant is False

    def test_arm_swap_negates_and_stays_degenerate(self):
        r = _score(TONE_META_697, TONE_APPLE_697, "gizmodo")
        assert abs(r.asymmetry_score + DELTA_652_BLOCK) < 1e-9
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert abs(r.cohens_d + EXPECTED_D_652_JUNK) < 1e-9
        assert r.is_significant is False


class TestScorerDegeneratePair653:
    """The #698 Wong pair (Apple [0.45] vs Meta [0.30], n=1 per arm) is
    the SIXTEENTH n=1-per-arm degenerate-ledger pair: the classic
    contract holds exactly - t=0.0, p=1.0, d=0.0, |asymmetry| == 0.15,
    arm-swap negates exactly, is_significant False."""

    def test_t_statistic_is_zero(self):
        r = _score(TONE_APPLE_698, TONE_META_698, "gizmodo")
        assert r.t_statistic == 0.0

    def test_p_value_is_one(self):
        r = _score(TONE_APPLE_698, TONE_META_698, "gizmodo")
        assert r.p_value == 1.0

    def test_cohens_d_is_zero(self):
        r = _score(TONE_APPLE_698, TONE_META_698, "gizmodo")
        assert r.cohens_d == 0.0

    def test_asymmetry_matches_manual_illustrative_delta(self):
        r = _score(TONE_APPLE_698, TONE_META_698, "gizmodo")
        assert abs(r.asymmetry_score - DELTA_653_BLOCK) < 1e-9

    def test_engine_not_significant(self):
        r = _score(TONE_APPLE_698, TONE_META_698, "gizmodo")
        assert r.is_significant is False

    def test_arm_swap_negates_exactly(self):
        fwd = _score(TONE_APPLE_698, TONE_META_698, "gizmodo")
        rev = _score(TONE_META_698, TONE_APPLE_698, "gizmodo")
        assert abs(fwd.asymmetry_score + rev.asymmetry_score) < 1e-12
        assert rev.t_statistic == 0.0 and rev.cohens_d == 0.0
        assert rev.is_significant is False


class TestScorerStatisticalMeaningfulness700:
    """The Type D mandate: the engine must flag real signal (strong
    synthetic, engine layer) and stay silent on noise (near-null)."""

    def test_strong_signal_asymmetry(self):
        r = _score(STRONG_PEER, STRONG_META, "synthetic")
        assert abs(r.asymmetry_score - EXPECTED_STRONG["asym"]) < 1e-9

    def test_strong_signal_t_statistic(self):
        r = _score(STRONG_PEER, STRONG_META, "synthetic")
        assert abs(r.t_statistic - EXPECTED_STRONG["t"]) < 1e-9

    def test_strong_signal_p_value(self):
        r = _score(STRONG_PEER, STRONG_META, "synthetic")
        assert abs(r.p_value - EXPECTED_STRONG["p"]) < 1e-12

    def test_strong_signal_is_significant_at_engine_layer(self):
        r = _score(STRONG_PEER, STRONG_META, "synthetic")
        assert r.is_significant is True

    def test_strong_signal_large_effect(self):
        r = _score(STRONG_PEER, STRONG_META, "synthetic")
        assert abs(r.cohens_d - EXPECTED_STRONG["d"]) < 1e-9

    def test_strong_signal_ci_excludes_zero(self):
        r = _score(STRONG_PEER, STRONG_META, "synthetic")
        assert r.confidence_interval_lower > 0
        assert abs(r.confidence_interval_lower - EXPECTED_STRONG["ci_lo"]) < 1e-9
        assert abs(r.confidence_interval_upper - EXPECTED_STRONG["ci_hi"]) < 1e-9

    def test_null_pair_stays_silent(self):
        r = _score(NULL_TARGET, NULL_PEER, "synthetic")
        assert r.is_significant is False

    def test_null_pair_p_value_not_small(self):
        r = _score(NULL_TARGET, NULL_PEER, "synthetic")
        assert r.p_value > 0.05
        assert abs(r.p_value - EXPECTED_NULL["p"]) < 1e-9
        assert abs(r.t_statistic - EXPECTED_NULL["t"]) < 1e-9
        assert abs(r.cohens_d - EXPECTED_NULL["d"]) < 1e-9


class TestNoEngineRun699:
    """#699 correctly runs NO engine: mechanism 654 is a
    financial-incentive deal-level leg with no tone arms. The block is
    verified read-only, never edited."""

    def _block(self):
        return _yaml("profiles/competitor-entities.yaml")["entities"][
            "apple"
        ][
            "mechanism_654_apple_google_gemini_publisher_content_bypass_leg_sep2026"
        ]

    def test_mechanism_654_iteration_699_type_c(self):
        b = self._block()
        assert b["mechanism_id"] == 654
        assert b["iteration"] == 699
        assert b["rotation"] == "Type C"

    def test_no_tone_claim_pinned(self):
        b = self._block()
        sd = b["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["qualitative_only"] is True
        assert sd["scorer"] == "none"

    def test_p_and_d_not_calculated(self):
        b = self._block()
        sd = b["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False

    def test_falsification_family_not_member(self):
        b = self._block()
        assert "NOT a member" in b["falsification_family"]["membership"]

    def test_bypass_leg_identity(self):
        b = self._block()
        key = "mechanism_654_apple_google_gemini_publisher_content_bypass_leg_sep2026"
        assert b["mechanism_id"] == 654
        assert "gemini" in key and "bypass" in key

class TestCorpusIntegrityPost699:
    """Post-#699 sweep: mechanisms 652/653/654 placed, max modern id 654,
    no 655 anywhere. The #695 sweep's max-651/no-652 guards fail by
    designed supersession (convention)."""

    def test_mechanism_652_in_competitor_entities_yaml(self):
        block = _yaml("profiles/competitor-entities.yaml")["entities"][
            "apple"
        ][
            "mechanism_652_gizmodo_apple_duo_launch_register_vs_gizmodo_meta_muse_experiment_sep12"
        ]
        assert block["mechanism_id"] == 652
        assert block["iteration"] == 697
        assert block["iteration_type"] == "A"

    def test_mechanism_652_carries_pinned_tone_arms(self):
        block = _yaml("profiles/competitor-entities.yaml")["entities"][
            "apple"
        ][
            "mechanism_652_gizmodo_apple_duo_launch_register_vs_gizmodo_meta_muse_experiment_sep12"
        ]
        scorer = block["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["target_scores_MANUAL_ILLUSTRATIVE"] == [0.2, 0.45]
        assert scorer["peer_scores_MANUAL_ILLUSTRATIVE"] == [-0.25]
        assert scorer["delta_manual_illustrative"] == 0.575

    def test_mechanism_653_in_journalists_yaml(self):
        txt = open(
            os.path.join(REPO_ROOT, "profiles/careers/journalists.yaml"),
            encoding="utf-8",
        ).read()
        key = "mechanism_653_raymond_wong_duo_hands_on_vs_ray_ban_gen2_review_register_constancy_sep12"
        assert key in txt
        assert txt.count(key) == 1

    def test_mechanism_653_journalist_and_tones(self):
        txt = open(
            os.path.join(REPO_ROOT, "profiles/careers/journalists.yaml"),
            encoding="utf-8",
        ).read()
        assert "Raymond Wong" in txt
        assert "tone_illustrative: 0.45" in txt
        assert "tone_illustrative: 0.3" in txt
        assert "TWENTIETH falsification-family member" in txt

    def test_mechanism_654_in_competitor_entities_yaml(self):
        block = _yaml("profiles/competitor-entities.yaml")["entities"][
            "apple"
        ][
            "mechanism_654_apple_google_gemini_publisher_content_bypass_leg_sep2026"
        ]
        assert block["mechanism_id"] == 654
        assert block["iteration"] == 699
        assert block["date_analyzed"] == "2026-09-12"

    def test_max_modern_mechanism_id_is_654(self):
        ids = [
            int(m)
            for m in re.findall(r"mechanism_(\d+)", _profiles_text())
        ]
        modern = [i for i in ids if i >= 504]
        assert max(modern) == 654

    def test_no_mechanism_655_in_profiles(self):
        assert "mechanism_655" not in _profiles_text()

    def test_no_mechanism_655_key_in_profiles(self):
        assert "mechanism_id: 655" not in _profiles_text()

    def test_no_mechanism_655_in_tests(self):
        chunks = []
        for f in glob.glob(os.path.join(TESTS_DIR, "test_*.py")):
            if f.endswith(os.path.basename(__file__)):
                continue
            with open(f, encoding="utf-8") as fh:
                chunks.append(fh.read())
        assert "mechanism_655" not in "\n".join(chunks)

    def test_journalists_yaml_parses(self):
        assert len(_yaml("profiles/careers/journalists.yaml")["journalists"]) >= 267


class TestLedgerIntegrity700:
    """Falsification ledger at 20 (TWENTIETH via m653 #698; m652 and m654
    claim no membership; no TWENTY-FIRST); #609 cohort 7/7; divergence
    ratchet holds at 8."""

    def test_twentieth_pin_present(self):
        text = _profiles_text()
        assert "TWENTIETH falsification-family member" in text

    def test_no_twenty_first_falsification_member(self):
        text = _profiles_text()
        assert "TWENTY-FIRST" not in text

    def test_m652_not_falsification_member(self):
        b = _yaml("profiles/competitor-entities.yaml")["entities"][
            "apple"
        ][
            "mechanism_652_gizmodo_apple_duo_launch_register_vs_gizmodo_meta_muse_experiment_sep12"
        ]
        assert "NOT a falsification-family member" in b[
            "falsification_family"
        ]["membership"]

    def test_m654_not_falsification_member(self):
        b = _yaml("profiles/competitor-entities.yaml")["entities"][
            "apple"
        ][
            "mechanism_654_apple_google_gemini_publisher_content_bypass_leg_sep2026"
        ]
        assert "NOT a member" in b["falsification_family"]["membership"]

    def test_no_eighth_renewal_cohort_member(self):
        text = _profiles_text()
        assert "EIGHTH member of the #609" not in text
        assert "eighth member of the #609" not in text

    def test_seventh_cohort_member_still_newscorp(self):
        text = _profiles_text()
        assert (
            "SEVENTH member of the #609 first-gen OpenAI publisher "
            "renewal cohort"
        ) in text

    def test_no_ninth_divergence_pin(self):
        text = _profiles_text()
        assert text.count("EIGHTH DIVERGENCE PIN") == 1
        assert "NINTH" not in text


class TestTypeEPodcastSentimentIntegrity700:
    """Type E integrity: podcast-sentiment.md keeps the Attention Sphere
    62nd-cycle no-match row (per #696), the Everyone Hates Elon
    activist-group (not a podcast) row, and the Guilty Feminist 499."""

    def _text(self):
        with open(os.path.join(REPO_ROOT, "podcast-sentiment.md"),
                  encoding="utf-8") as fh:
            return fh.read()

    def test_attention_sphere_62nd_cycle(self):
        text = self._text()
        assert "Attention Sphere" in text
        assert "62 verification cycles" in text

    def test_everyone_hates_elon_not_podcast(self):
        text = self._text()
        assert "Everyone Hates Elon" in text
        assert "not a podcast" in text.lower()

    def test_guilty_feminist_present(self):
        text = self._text()
        assert "Guilty Feminist" in text

    def test_guilty_feminist_499(self):
        text = self._text()
        assert "499" in text

class TestCrossDocHeaderAgreement700:
    """Durable guard for the #499 miss (reinstated #690): README.md and
    ARCHITECTURE.md headers must agree with each other and with the
    test files on disk. Deselected pre-commit per the #565 followup
    convention; doc-sync lands in the followup."""

    def test_headers_agree(self):
        with open(README, encoding="utf-8") as fh:
            readme_tests, readme_files = _count_header(fh.read())
        with open(ARCH, encoding="utf-8") as fh:
            arch_tests, arch_files = _count_header(fh.read())
        assert (readme_tests, readme_files) == (arch_tests, arch_files), (
            f"README header {(readme_tests, readme_files)} != "
            f"ARCHITECTURE header {(arch_tests, arch_files)}"
        )

    def test_header_file_count_matches_disk(self):
        with open(ARCH, encoding="utf-8") as fh:
            _, arch_files = _count_header(fh.read())
        on_disk = len(glob.glob(os.path.join(TESTS_DIR, "test_*.py")))
        assert arch_files == on_disk, (
            f"ARCHITECTURE header claims {arch_files} test files, "
            f"but {on_disk} exist on disk"
        )


class TestDocSync700:
    # Deselected pre-commit per the #565 followup convention; README
    # stats, ARCHITECTURE rows, and the iteration-log entry land in the
    # followup commit. Patched green post-doc-sync.

    def test_count_stats_check_passes(self):
        """scripts/count_stats.py --check is the canonical README sync gate."""
        result = subprocess.run(
            [sys.executable, os.path.join(SCRIPTS, "count_stats.py"),
             "--check", "--pytest"],
            capture_output=True,
            text=True,
            timeout=300,
            cwd=REPO_ROOT,
        )
        assert result.returncode == 0, (
            f"count_stats.py --check failed:\n{result.stdout}\n{result.stderr}"
        )

    def test_700_row_in_readme_table(self):
        with open(README, encoding="utf-8") as fh:
            assert FILE_700 in fh.read()

    def test_700_row_in_architecture_tree(self):
        with open(ARCH, encoding="utf-8") as fh:
            assert FILE_700 in fh.read()

    def test_iteration_log_entry_for_700(self):
        with open(LOG, encoding="utf-8") as fh:
            assert re.search(r"^#700 Type D:", fh.read(), re.MULTILINE)


class TestRotationCycleGuard700:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #700 main-commit SHA is known.
    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

    @staticmethod
    def _mains():
        # First occurrence of each distinct iteration number, newest first.
        # Distinct-iteration dedup (per the #679 guard convention): followup
        # SHA-fix commits re-titled "Type [A-E] #NNN: ..." match the filter,
        # so raw subjects[:5] can show one iteration twice; the intent is
        # the distinct iteration mains in order.
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=REPO_ROOT,
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

    def test_window_696_700_closes_c_to_d(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("D", "700"),
            ("C", "699"),
            ("B", "698"),
            ("A", "697"),
            ("E", "696"),
        ], f"rotation window 696-700 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            observed.append(m.group(1))
        assert observed == ["D", "C", "B", "A", "E"]
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #700 main commit. Patched in the followup
        # per the #565 convention once the main commit SHA is known.
        assert self.ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP", \
            "anchor not patched"
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #700:", l)]
        assert len(mains) == 1, f"expected one Type D #700 main: {mains}"
        sha = mains[0].split(" ", 1)[0]
        assert sha == self.ANCHORED_SHA, f"anchor not yet patched: {sha}"


class TestIteration700NoveltyAnchor:
    """Deselected pre-commit per the #565 followup convention; patched
    green post-doc-sync. Novelty was verified pre-commit by shell
    greps (zero test_type_d_700 files, no #700 in git log,
    max mechanism 654, no 655 anywhere); this test pins that no
    duplicate #700 main commit ever appears."""

    def test_type_d_700_file_unique(self):
        matches = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_d_700*.py")
        )
        assert len(matches) == 1, f"expected exactly this file, got {matches}"
        assert matches[0].endswith(FILE_700)

    def test_type_d_700_main_commit_unique_and_anchored(self):
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #700:", l)]
        assert len(mains) == 1, (
            f"expected exactly one Type D #700 main commit, got: {mains}"
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard700.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, f"main commit {sha} != guard anchor {anchor}"


class TestWindow696to699Persistence:
    def test_window_test_files_exist(self):
        for num, fname in WINDOW_FILES.items():
            assert os.path.exists(os.path.join(TESTS_DIR, fname)), \
                f"#{num} file missing: {fname}"

    @pytest.mark.parametrize("fname", list(WINDOW_FILES.values()))
    def test_readme_rows_present(self, fname):
        with open(README, encoding="utf-8") as fh:
            assert fname in fh.read()

    @pytest.mark.parametrize("fname", list(WINDOW_FILES.values()))
    def test_architecture_rows_present(self, fname):
        with open(ARCH, encoding="utf-8") as fh:
            assert fname in fh.read()


class TestYamlIntegrity700:
    @pytest.mark.parametrize(
        "path",
        [
            "profiles/competitor-entities.yaml",
            "profiles/careers/journalists.yaml",
        ],
    )
    def test_yaml_parses(self, path):
        assert _yaml(path) is not None
