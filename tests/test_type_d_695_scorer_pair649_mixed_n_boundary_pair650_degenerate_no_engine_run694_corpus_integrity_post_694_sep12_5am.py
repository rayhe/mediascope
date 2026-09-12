"""
Type D - Test & Verify: real-engine verification of the #692 mixed-n
(n=2 vs n=1) illustrative pair (mechanism 649: Reuters Apple Duo arms
[+0.15, -0.25] vs Meta Muse arm [-0.45], block delta (Apple minus Meta)
+0.40) - the EIGHTH degenerate-boundary pin (junk cohens_d
+1.414213562373095 computable while Welch significance degenerates:
t=0.0, p=1.0, is_significant False; smallest-magnitude positive junk-d
in the lineage, proving the contract binds the significance flag, not
effect-size arithmetic) + the #693 n=1-per-arm byline-isolated pair
(mechanism 650: Nicole Nguyen WSJ, Apple [+0.40] vs Meta [+0.15],
block delta +0.25 reproduces IEEE-cleanly at 0.25) - the FIFTEENTH
n=1-per-arm degenerate-ledger pair (first four #645; fifth/sixth #650;
seventh/eighth #655; ninth/tenth #660; eleventh/twelfth #665;
thirteenth #670; fourteenth #675) + the Type D
statistical-meaningfulness mandate (fresh strong-signal synthetic
corpus: asym +0.8, t=16.0, p=2.33e-07, d=10.1193, CI entirely positive,
engine-significant at the engine layer, never promoted to a finding;
near-null corpus p=0.3733 stays silent) + #694 no-engine-run
verification (mechanism 651 Microsoft x Nine APAC deal-leg carries
scorer none, tone_scores NOT_SCORED, qualitative_only true; Type D
read-only convention - the 651 block is untouched) + post-#694 corpus
integrity sweep (mechanism 649 present and unique in
profiles/competitor-entities.yaml under entities.apple with iteration
692, iteration_type A; mechanism 650 present and unique in
profiles/careers/journalists.yaml under the Nicole Nguyen entry with
iteration 693, type B, apple_arm tone_illustrative 0.4 and meta_arm
0.15; mechanism 651 present and unique in
profiles/competitor-entities.yaml under entities.microsoft with
iteration 694, rotation Type C; modern (504+) id era collision-free
with max == 651 and no 652 anywhere in profiles/ or tests/) +
falsification-ledger integrity (EIGHTEENTH via m649, NINETEENTH via
m650, no TWENTIETH; #609 first-gen OpenAI publisher renewal cohort
stays closed at 7/7, no EIGHTH member; divergence ratchet holds at 8,
no NINTH) + Type E 61-cycle tracked-sources integrity + cross-doc
header agreement (README.md and docs/ARCHITECTURE.md headers agree and
match the test files on disk, per the #690-reinstated guard).

Iteration #695 - Sat 2026-09-12 05:00 PDT
(scheduled job_id mediascope-daily-iteration, goal_54093bda4145, rotation 694 C -> 695 D)

Verification arc: #692 (Type A, mechanism 649) logged a MANUAL
ILLUSTRATIVE delta +0.40 on a mixed-n (n=2 vs n=1) pair with no engine
run; #693 (Type B, mechanism 650) logged a MANUAL ILLUSTRATIVE delta
+0.25 on an n=1-per-arm byline-isolated pair with no engine run; #694
(Type C, mechanism 651) logged qualitative financial mapping only with
no tone arms at all. This run verifies those decisions against the
real scorer path: the #692 pair reproduces the degenerate-boundary
contract (t=0.0, p=1.0, is_significant False) while cohens_d returns a
computable junk value (+1.4142), the #693 pair reproduces the classic
degenerate contract EXACTLY (t=0.0, p=1.0, d=0.0, |asymmetry| == 0.25),
and #694 correctly runs no engine. The finding layer stays
is_significant False per the Aug 28 2026 standing rule, so the
manual-illustrative pins STRENGTHEN the no-empirical-claim discipline:
degenerate engine inputs never become empirical findings, and a
computable effect size on degenerate arms is meaningless junk.

The Type D mandate "verify the asymmetry scoring produces
statistically meaningful results" is satisfied by the strong-signal
synthetic check: peer arm [+0.25, +0.20, +0.30, +0.15, +0.35] vs Meta
arm [-0.55, -0.45, -0.60, -0.50, -0.65] (n=5 per arm) yields asymmetry
+0.8, t=16.000000000000004, p=2.3341863207873997e-07,
d=10.119288512538814, is_significant True at the ENGINE layer, CI
(0.71, 0.8800000000000001) entirely above zero. When real signal
exists, the engine flags it; when it does not (near-null pair,
p=0.3733411674819867), it stays silent. The scorer is discriminative,
not decoration. Engine significance is never promoted to a finding.

#694 correctly runs NO engine: mechanism 651 (Microsoft x Nine
Entertainment Jul 3 2026 APAC-first Copilot grounding deal) is a
financial-incentive deal-level leg whose statistical_discipline block
carries scorer none, tone_scores NOT_SCORED, p_value NOT_CALCULATED,
cohens_d NOT_CALCULATED, ci_95 NOT_CALCULATED, is_significant false,
qualitative_only true, correlation_not_causation true,
artifact_grade false. There are no tone arms for the engine to score.
Mechanism 651's block is left untouched (Type D read-only convention).

Corpus integrity sweep: mechanism 649 (Reuters x Apple Duo launch
register vs Reuters Meta Muse register, #692) is present and unique in
profiles/competitor-entities.yaml under entities.apple with iteration
692, iteration_type A, carrying the MANUAL ILLUSTRATIVE +0.40 pin and
the verbatim Reuters URL slugs; mechanism 650 (Nicole Nguyen WSJ Apple
Duo first-impressions vs Meta WhatsApp walled-garden byline-isolated
pair, #693) is present and unique in profiles/careers/journalists.yaml
with iteration 693, type B, journalist Nicole Nguyen, publication The
Wall Street Journal, apple_arm tone_illustrative 0.4 and meta_arm
tone_illustrative 0.15; mechanism 651 (Microsoft x Nine Entertainment
APAC deal, #694) is present and unique in profiles/competitor-entities.yaml
under entities.microsoft with iteration 694, rotation Type C, and the
septuple-to-8 architecture extension. Max modern mechanism_id == 651;
mechanism_652 appears nowhere in profiles/ or tests/.

Falsification-ledger integrity: m649 holds EIGHTEENTH (ledger stood
at 17 after #689's SEVENTEENTH; #690 Type D and #691 Type E claimed no
membership), m650 holds NINETEENTH; no TWENTIETH anywhere in profiles/.
The #609 first-gen OpenAI publisher renewal cohort stays closed at 7/7
(News Corp SEVENTH; no EIGHTH member). The divergence ratchet holds at
8 (#642 still the smallest-p holder), no NINTH.

Rotation guard: window 691-695 (E, A, B, C, D newest-first), closing
the C->D edge. Rotation-guard 3 + doc-sync 4 + novelty-anchor 1
deselected pre-commit per the #565 followup convention; anchor patched
in the followup once the #695 main-commit SHA is known.

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

FILE_695 = "test_type_d_695_scorer_pair649_mixed_n_boundary_pair650_degenerate_no_engine_run694_corpus_integrity_post_694_sep12_5am.py"

# Pinned illustrative tone arms from the #692 mechanism block
# (mechanism_649_reuters_apple_duo_launch_register_vs_reuters_meta_muse_register_sep12).
# Apple arms: Duo launch news +0.15, skeptical follow-up -0.25.
# Meta arm: Muse launch piece -0.45.
TONE_APPLE_692 = [0.15, -0.25]
TONE_META_692 = [-0.45]
DELTA_649_BLOCK = 0.40  # (Apple minus Meta), block: "-0.05 - (-0.45) = 0.40"

# Pinned illustrative tone arms from the #693 mechanism block
# (mechanism_650_nicole_nguyen_apple_duo_first_impressions_vs_meta_whatsapp_walled_garden_sep12).
# Apple arm: Duo first impressions +0.40 (first-hand read).
# Meta arm: WhatsApp walled-garden +0.15 (first-hand read, reaffirmed upward from 0.1).
TONE_APPLE_693 = [0.40]
TONE_META_693 = [0.15]
DELTA_650_BLOCK = 0.25  # (Apple minus Meta)

# Engine values produced this run by direct calculate_asymmetry calls on
# the pinned arms above; constants confirmed before this test file was
# written (research-method rule).
# m649: t=0.0, p=1.0, d=1.414213562373095 (junk), asym=0.4, sig False.
# m649 arm-swap: t=0.0, p=1.0, d=-1.414213562373095, asym=-0.4.
# m650: t=0.0, p=1.0, d=0.0, asym=0.25 IEEE-clean, sig False.
EXPECTED_D_649_JUNK = 1.414213562373095

# Strong-signal synthetic corpus (fresh this run, n=5 per arm): the
# engine must flag it at the engine layer; significance here is never
# promoted to a finding (Aug 28 2026 standing rule).
STRONG_PEER = [0.25, 0.20, 0.30, 0.15, 0.35]
STRONG_META = [-0.55, -0.45, -0.60, -0.50, -0.65]
EXPECTED_STRONG = {
    "asym": 0.8,
    "t": 16.000000000000004,
    "p": 2.3341863207873997e-07,
    "d": 10.119288512538814,
}
# Near-null pair: the engine must stay silent.
NULL_TARGET = [0.04, -0.03, 0.06, -0.02, 0.01]
NULL_PEER = [-0.05, 0.02, -0.04, 0.03, -0.01]

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


# Window files 691-694 must exist and carry README/ARCHITECTURE rows.
WINDOW_FILES = {
    691: "test_type_e_691_podcast_sentiment_61st_verification_gf499_watch_sep12_1am.py",
    692: "test_type_a_692_reuters_apple_duo_launch_register_vs_meta_muse_register_sep12_2am.py",
    693: "test_type_b_693_nicole_nguyen_apple_duo_first_impressions_vs_meta_whatsapp_walled_garden_sep12_3am.py",
    694: "test_type_c_694_microsoft_nine_apac_first_copilot_deal_sep12_4am.py",
}
EXPECTED_NEWEST_FIRST = [
    (695, "D"),
    (694, "C"),
    (693, "B"),
    (692, "A"),
    (691, "E"),
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


class TestIteration695Metadata:
    def test_docstring_ids(self):
        doc = __doc__
        assert "iteration #695" in doc.lower()
        assert "2026-09-12" in doc
        assert "Type D" in doc
        assert "goal_54093bda4145" in doc
        assert "mediascope-daily-iteration" in doc

    def test_rotation_c_to_d(self):
        assert "rotation 694 C -> 695 D" in __doc__

    def test_filename_convention(self):
        assert os.path.basename(__file__) == FILE_695


class TestNovelty695:
    def test_no_type_d_695_commit_pre_commit(self):
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        assert "Type D #695:" not in out


class TestScorerMixedNBoundaryPair649:
    """The #692 Reuters pair (Apple [0.15, -0.25] n=2 vs Meta [-0.45]
    n=1) is the EIGHTH degenerate-boundary pin: Welch significance
    degenerates (t=0.0, p=1.0, is_significant False) while cohens_d
    returns a computable junk value (+1.414213562373095, the
    smallest-magnitude positive junk-d in the lineage after #667's
    +17.68 and #690/pair646's -4.10). The degenerate contract binds the
    significance flag, not effect-size arithmetic."""

    def test_t_statistic_is_zero(self):
        r = _score(TONE_APPLE_692, TONE_META_692, "reuters")
        assert r.t_statistic == 0.0

    def test_p_value_is_one(self):
        r = _score(TONE_APPLE_692, TONE_META_692, "reuters")
        assert r.p_value == 1.0

    def test_cohens_d_is_computable_junk(self):
        # The boundary refinement: d does NOT degenerate on mixed-n
        # arms (the n=1 arm contributes zero variance, so the pooled sd
        # collapses to the n=2 arm's own sd). Junk, and must be ignored
        # per the Aug 28 2026 standing rule.
        r = _score(TONE_APPLE_692, TONE_META_692, "reuters")
        assert abs(r.cohens_d - EXPECTED_D_649_JUNK) < 1e-9

    def test_asymmetry_matches_manual_illustrative_delta(self):
        r = _score(TONE_APPLE_692, TONE_META_692, "reuters")
        assert abs(r.asymmetry_score - DELTA_649_BLOCK) < 1e-9

    def test_engine_not_significant(self):
        r = _score(TONE_APPLE_692, TONE_META_692, "reuters")
        assert r.is_significant is False

    def test_arm_swap_negates_and_stays_degenerate(self):
        r = _score(TONE_META_692, TONE_APPLE_692, "reuters")
        assert abs(r.asymmetry_score + DELTA_649_BLOCK) < 1e-9
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert abs(r.cohens_d + EXPECTED_D_649_JUNK) < 1e-9
        assert r.is_significant is False


class TestScorerDegeneratePair650:
    """The #693 Nguyen pair (Apple [0.40] vs Meta [0.15], n=1 per arm)
    is the FIFTEENTH n=1-per-arm degenerate-ledger pair: the classic
    contract holds exactly - t=0.0, p=1.0, d=0.0, |asymmetry| == 0.25
    IEEE-clean (contrast #673's 0.19999999999999998), arm-swap negates
    exactly, is_significant False."""

    def test_t_statistic_is_zero(self):
        r = _score(TONE_APPLE_693, TONE_META_693, "wsj")
        assert r.t_statistic == 0.0

    def test_p_value_is_one(self):
        r = _score(TONE_APPLE_693, TONE_META_693, "wsj")
        assert r.p_value == 1.0

    def test_cohens_d_is_zero(self):
        r = _score(TONE_APPLE_693, TONE_META_693, "wsj")
        assert r.cohens_d == 0.0

    def test_asymmetry_matches_manual_illustrative_delta(self):
        r = _score(TONE_APPLE_693, TONE_META_693, "wsj")
        assert abs(r.asymmetry_score - DELTA_650_BLOCK) < 1e-9

    def test_engine_not_significant(self):
        r = _score(TONE_APPLE_693, TONE_META_693, "wsj")
        assert r.is_significant is False

    def test_arm_swap_negates_exactly(self):
        fwd = _score(TONE_APPLE_693, TONE_META_693, "wsj")
        rev = _score(TONE_META_693, TONE_APPLE_693, "wsj")
        assert abs(fwd.asymmetry_score + rev.asymmetry_score) < 1e-12
        assert rev.t_statistic == 0.0 and rev.cohens_d == 0.0
        assert rev.is_significant is False


class TestScorerStatisticalMeaningfulness695:
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

    def test_null_pair_stays_silent(self):
        r = _score(NULL_TARGET, NULL_PEER, "synthetic")
        assert r.is_significant is False

    def test_null_pair_p_value_not_small(self):
        r = _score(NULL_TARGET, NULL_PEER, "synthetic")
        assert r.p_value > 0.05


class TestNoEngineRun694:
    """#694 correctly runs NO engine: mechanism 651 is a
    financial-incentive deal-level leg with no tone arms. The block is
    verified read-only, never edited."""

    def _block(self):
        return _yaml("profiles/competitor-entities.yaml")["entities"][
            "microsoft"
        ][
            "mechanism_651_microsoft_nine_entertainment_apac_first_copilot_grounding_jul2026"
        ]

    def test_mechanism_651_iteration_694_type_c(self):
        b = self._block()
        assert b["mechanism_id"] == 651
        assert b["iteration"] == 694
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

    def test_eighth_leg_architecture_present(self):
        b = self._block()
        arch = " ".join(b["architecture_context"])
        assert "Eighth distinct Microsoft-publisher financial mechanism" in arch


class TestCorpusIntegrityPost694:
    """Post-#694 sweep: mechanisms 649/650/651 placed, max modern id 651,
    no 652 anywhere. The #690 sweep's max-648/no-649 guards fail by
    designed supersession (convention)."""

    def test_mechanism_649_in_competitor_entities_yaml(self):
        block = _yaml("profiles/competitor-entities.yaml")["entities"][
            "apple"
        ]["mechanism_649_reuters_apple_duo_launch_register_vs_reuters_meta_muse_register_sep12"]
        assert block["mechanism_id"] == 649
        assert block["iteration"] == 692
        assert block["iteration_type"] == "A"

    def test_mechanism_649_carries_pinned_tone_arms(self):
        block = _yaml("profiles/competitor-entities.yaml")["entities"][
            "apple"
        ]["mechanism_649_reuters_apple_duo_launch_register_vs_reuters_meta_muse_register_sep12"]
        scorer = block["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["target_scores_MANUAL_ILLUSTRATIVE"] == [0.15, -0.25]
        assert scorer["peer_scores_MANUAL_ILLUSTRATIVE"] == [-0.45]
        assert scorer["delta_manual_illustrative"] == 0.4

    def test_mechanism_650_in_journalists_yaml(self):
        found = []
        for j in _yaml("profiles/careers/journalists.yaml")["journalists"]:
            for key in ("mechanisms", "pair_mechanisms", "type_b_mechanisms"):
                for m in (j.get(key) or []):
                    if isinstance(m, dict) and "mechanism_650" in str(
                        list(m.keys())[0]
                    ):
                        found.append((j["name"], list(m.keys())[0]))
        # mechanism entries live in a flat list mixed with narrative
        # entries; fall back to a text search scoped to the file.
        if not found:
            txt = open(
                os.path.join(REPO_ROOT, "profiles/careers/journalists.yaml"),
                encoding="utf-8",
            ).read()
            assert "mechanism_650_nicole_nguyen" in txt
            assert txt.count("mechanism_650_nicole_nguyen") == 1

    def test_mechanism_650_journalist_and_tones(self):
        txt = open(
            os.path.join(REPO_ROOT, "profiles/careers/journalists.yaml"),
            encoding="utf-8",
        ).read()
        assert "journalist: Nicole Nguyen" in txt
        assert "tone_illustrative: 0.4" in txt
        assert "tone_illustrative: 0.15" in txt

    def test_mechanism_651_in_competitor_entities_yaml(self):
        block = _yaml("profiles/competitor-entities.yaml")["entities"][
            "microsoft"
        ][
            "mechanism_651_microsoft_nine_entertainment_apac_first_copilot_grounding_jul2026"
        ]
        assert block["mechanism_id"] == 651
        assert block["iteration"] == 694
        assert block["date_analyzed"] == "2026-09-12"

    def test_max_modern_mechanism_id_is_651(self):
        ids = [
            int(m)
            for m in re.findall(r"mechanism_(\d+)", _profiles_text())
        ]
        modern = [i for i in ids if i >= 504]
        assert max(modern) == 651

    def test_no_mechanism_652_in_profiles(self):
        assert "mechanism_652" not in _profiles_text()

    def test_no_mechanism_652_key_in_profiles(self):
        assert "mechanism_id: 652" not in _profiles_text()

    def test_no_mechanism_652_in_tests(self):
        chunks = []
        for f in glob.glob(os.path.join(TESTS_DIR, "test_*.py")):
            if f.endswith(os.path.basename(__file__)):
                continue
            with open(f, encoding="utf-8") as fh:
                chunks.append(fh.read())
        assert "mechanism_652" not in "\n".join(chunks)

    def test_journalists_yaml_parses(self):
        assert len(_yaml("profiles/careers/journalists.yaml")["journalists"]) >= 267


class TestLedgerIntegrity695:
    """Falsification ledger at 19 (EIGHTEENTH via m649 #692, NINETEENTH
    via m650 #693; #694 claimed no membership); #609 cohort 7/7;
    divergence ratchet holds at 8."""

    def test_eighteenth_pin_present(self):
        text = _profiles_text()
        assert "EIGHTEENTH falsification-family member" in text

    def test_nineteenth_pin_present(self):
        text = _profiles_text()
        assert "NINETEENTH falsification-family member" in text

    def test_no_twentieth_falsification_member(self):
        text = _profiles_text()
        assert "TWENTIETH" not in text

    def test_m694_not_falsification_member(self):
        b = _yaml("profiles/competitor-entities.yaml")["entities"][
            "microsoft"
        ][
            "mechanism_651_microsoft_nine_entertainment_apac_first_copilot_grounding_jul2026"
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


class TestTypeEPodcastSentimentIntegrity695:
    """Type E integrity: podcast-sentiment.md keeps the Attention Sphere
    61st-cycle no-match row (per #691), the Everyone Hates Elon
    activist-group (not a podcast) row, and the Guilty Feminist 499."""

    def _text(self):
        with open(os.path.join(REPO_ROOT, "podcast-sentiment.md"),
                  encoding="utf-8") as fh:
            return fh.read()

    def test_attention_sphere_61st_cycle(self):
        text = self._text()
        assert "Attention Sphere" in text
        assert "61 verification cycles" in text

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


class TestCrossDocHeaderAgreement695:
    """Durable guard for the #499 miss (reinstated #690): README.md and
    ARCHITECTURE.md headers must agree with each other and with the
    test files on disk."""

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


class TestDocSync695:
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

    def test_695_row_in_readme_table(self):
        with open(README, encoding="utf-8") as fh:
            assert FILE_695 in fh.read()

    def test_695_row_in_architecture_tree(self):
        with open(ARCH, encoding="utf-8") as fh:
            assert FILE_695 in fh.read()

    def test_iteration_log_entry_for_695(self):
        with open(LOG, encoding="utf-8") as fh:
            assert re.search(r"^#695 Type D:", fh.read(), re.MULTILINE)


class TestRotationCycleGuard695:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #695 main-commit SHA is known.
    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched in followup per #565 convention

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

    def test_window_691_695_closes_c_to_d(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("D", "695"),
            ("C", "694"),
            ("B", "693"),
            ("A", "692"),
            ("E", "691"),
        ], f"rotation window 691-695 wrong: {observed}"

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
        # Post-commit anchor: the #695 main commit. Patched in the followup
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
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #695:", l)]
        assert len(mains) == 1, f"expected one Type D #695 main: {mains}"
        sha = mains[0].split(" ", 1)[0]
        assert sha == self.ANCHORED_SHA, f"anchor not yet patched: {sha}"


class TestIteration695NoveltyAnchor:
    """Deselected pre-commit per the #565 followup convention; patched
    green post-doc-sync. Novelty was verified pre-commit by shell
    greps (zero test_type_d_695 files, no #695 in git log,
    max mechanism 651, no 652 anywhere); this test pins that no
    duplicate #695 main commit ever appears."""

    def test_type_d_695_file_unique(self):
        matches = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_d_695*.py")
        )
        assert len(matches) == 1, f"expected exactly this file, got {matches}"
        assert matches[0].endswith(FILE_695)

    def test_type_d_695_main_commit_unique_and_anchored(self):
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #695:", l)]
        assert len(mains) == 1, (
            f"expected exactly one Type D #695 main commit, got: {mains}"
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard695.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, f"main commit {sha} != guard anchor {anchor}"


class TestWindow691to694Persistence:
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


class TestYamlIntegrity695:
    @pytest.mark.parametrize(
        "path",
        [
            "profiles/competitor-entities.yaml",
            "profiles/careers/journalists.yaml",
        ],
    )
    def test_yaml_parses(self, path):
        assert _yaml(path) is not None
