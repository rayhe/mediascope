"""
Type D - Test & Verify: real-engine verification of the #687 publication-level
pair (mechanism 646: The Verge Apple iPhone Duo launch register vs Meta Muse
launch register, Meta arm [-0.35] vs Apple arm [+0.25, +0.50], n=1 vs n=2 -
asymmetry -0.725, block rounds to -0.73 exact; t=0.0, p=1.0 degenerate
significance contract, is_significant False at the engine layer, arm-swap
negates to +0.725 and stays degenerate) + real-engine verification of the
#688 byline-isolated pair (mechanism 647: Adam Satariano sole-byline, Meta
[-0.50] vs TikTok [-0.50], n=1 per arm - asymmetry 0.0 EXACT, t=0.0, p=1.0,
d=0.0, is_significant False, matching the #688 block's delta 0.00) + #689
no-engine-run verification (mechanism 648 is a Type C deal-level leg: the
falsification_family SEVENTEENTH pin carries illustrative_tone -0.55 MANUAL
ILLUSTRATIVE on a degenerate n=1 pin, no tone arms for the engine to score;
Type D read-only convention - the 648 block is untouched) + post-#689
corpus integrity sweep (mechanism 646 present and unique in
profiles/the-verge.yaml under competitor_relationships/apple with iteration
687, iteration_type A; mechanism 647 present and unique in
profiles/careers/journalists.yaml under the Adam Satariano entry with
iteration 688, type B, carrying tone_illustrative -0.50 on both arms;
mechanism 648 present and unique in profiles/competitor-entities.yaml under
entities/meta with iteration 689, rotation Type C; max modern mechanism_id
== 648 and no 649 anywhere in profiles/ or tests/) + ledger integrity
(falsification ledger advances to 17 via mechanism 647 SIXTEENTH and
mechanism 648 El Pais SEVENTEENTH, FIFTEENTH still on mechanism 643, no
EIGHTEENTH anywhere; #609 first-gen OpenAI publisher renewal cohort stays
closed at 7/7 with the #654 News Corp block still SEVENTH, no EIGHTH;
divergence ratchet holds at 8, no NINTH) + Type E 60-cycle tracked-sources
integrity.

Iteration #690 - Sat 2026-09-12 00:00 PDT
(scheduled job_id mediascope-daily-iteration, goal_54093bda4145, rotation 689 C -> 690 D)
goal_54093bda4145 mediascope-daily-iteration iteration 690 Type D 2026-09-12 00:00 PDT

Verification arc: #687 (Type A, mechanism 646) logged a MANUAL ILLUSTRATIVE
delta -0.73 (Meta -0.35 vs Apple +0.375) with no engine run - the second
publication on the launch-genre boundary-condition family (#662 WSJ first),
NOT a falsification-family member (both arms $0-deal at The Verge); #688
(Type B, mechanism 647) logged a MANUAL ILLUSTRATIVE delta 0.00 (Meta -0.50
vs TikTok -0.50) with no engine run - the SIXTEENTH falsification-family
member (Satariano register constancy, NYT $0-deal with Meta/TikTok/X);
#689 (Type C, mechanism 648) logged qualitative deal-level mapping only
with no tone arms at all - the SEVENTEENTH falsification-family member (El
Pais toxic-spills pin, second Meta-payer pin). This run verifies those
decisions against the real scorer path: pair 646 reproduces the degenerate
significance contract EXACTLY (t=0.0, p=1.0, is_significant False; the
-0.73 delta is pure arithmetic, 0.375 - 0.35 rounded); pair 647 reproduces
the contract EXACTLY (t=0.0, p=1.0, d=0.0, asymmetry 0.0 exact). One
refinement vs #682/#683: Cohen's d does NOT degenerate on pair 646
(d=-4.1012193308819755, nonzero pooled sd from the n=2 arm) even though
the Welch significance machinery does (t=0.0, p=1.0) - the degenerate
contract binds the significance flag, not the effect-size arithmetic. The
bootstrap CI (-0.85, -0.6) also excludes zero while is_significant stays
False: CI and t-test are different machinery; the Aug 28 standing rule
binds the finding layer to is_significant, which remains False on every
degenerate input. Manual-illustrative pins STRENGTHEN the no-empirical-
claim discipline: degenerate engine inputs never become findings.

The Type D mandate "verify the asymmetry scoring produces statistically
meaningful results" is satisfied by the strong-signal synthetic check:
Meta arm [-0.60,-0.50,-0.70,-0.55,-0.65,-0.45] vs peer arm
[+0.30,+0.40,+0.35,+0.45,+0.25,+0.50] (n=6 per arm) yields
asymmetry -0.9500000000000001, t=-17.59058189567848,
p=7.498515787192946e-09, d=-10.155927192672127, is_significant True at the
ENGINE layer, CI (-1.0416666666666665, -0.8500000000000001) entirely
below zero. When real signal exists, the engine flags it; when it does
not (near-null pair, p=0.9431203973446252), it stays silent. The scorer
is discriminative, not decoration.

#689 correctly runs NO engine: mechanism 648 is a financial-incentive
deal-level leg (Meta x European publishers AI news licensing bundle,
Le Figaro / Prisa / Suddeutsche Zeitung March 2026) whose
falsification_family pin is a degenerate n=1 illustrative pin. There are
no tone arms for the engine to score. Mechanism 648's block is left
untouched (Type D read-only convention).

Corpus integrity sweep: mechanism 646 (The Verge Apple Duo vs Meta Muse
launch register, #687) is present and unique in profiles/the-verge.yaml
under competitor_relationships/apple with iteration 687, iteration_type A,
carrying the MANUAL ILLUSTRATIVE -0.73 pin; mechanism 647 (Satariano DSA
addictive-design register constancy, #688) is present and unique in
profiles/careers/journalists.yaml under the Adam Satariano entry with
iteration 688, type B, carrying tone_illustrative -0.50 on meta_arm and
tiktok_arm; mechanism 648 (Meta x European publishers bundle, #689) is
present and unique in profiles/competitor-entities.yaml under
entities/meta with iteration 689, rotation Type C, mechanism_id 648. Max
modern mechanism_id == 648; mechanism_649 appears nowhere in profiles/
or tests/.

Designed supersession note: the #685 Type D sweep's
test_no_mechanism_646_in_profiles / test_no_mechanism_646_in_tests and
test_max_modern_mechanism_id_is_645 now fail by supersession (max is 648;
mechanism_646 is a real key in the-verge.yaml, mechanism_647 in
journalists.yaml, mechanism_648 in competitor-entities.yaml), consistent
with the established convention (cf. #685's note on #680's tests).

Rotation guard: window 686-690 (E, A, B, C, D newest-first), closing the
C->D edge. Rotation-guard 4 + doc-sync 4 deselected pre-commit per the
#565 followup convention; anchor patched in the followup once the #690
main-commit SHA is known. Doc-sync deselects: count_stats --check (README
stats refresh lands in followup), the #690 README/ARCHITECTURE rows, and
the cross-doc header-agreement test (README header goes stale until the
followup stats refresh; the ARCHITECTURE header is re-synced in the main
commit).

ARCHITECTURE.md stale-header repair (docs only, no test logic touched):
the tests/ tree header read "29236 tests across 879 test files" since #551
(Sep 5), while README.md carries 36297/1017 and 1018 test files exist on
disk. Root cause: count_stats.py --check only gates README.md, and the
#500 cross-doc header-agreement guard regressed out of later Type D files
(#685 has no TestCrossDocHeaderAgreement class), so README-only sync
tooling let ARCHITECTURE.md drift for seven days. This run re-syncs the
ARCHITECTURE.md tests/ tree header to the authoritative count_stats
numbers (after this file and its doc rows landed) and reinstates the
cross-doc agreement guard in TestCrossDocHeaderAgreement690.

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

FILE_690 = "test_type_d_690_scorer_pair646_engine_pair647_exact_no_engine_run689_corpus_integrity_post_689_sep12_12am.py"

# Pinned illustrative tone arms from the #687 mechanism block.
# Meta Muse launch register (Hart, mirror-attested): [-0.35]
# Apple iPhone Duo launch register (Lawler 0.25, staffers 0.50): [+0.25, +0.50]
TONE_META_687 = [-0.35]
TONE_APPLE_687 = [0.25, 0.50]
DELTA_646_BLOCK = -0.73  # block rounds -0.725 to -0.73

# Pinned illustrative tone arms from the #688 mechanism block.
# Satariano sole-byline, both arms hand-scored -0.50.
TONE_META_688 = [-0.50]
TONE_TIKTOK_688 = [-0.50]
DELTA_647_BLOCK = 0.0

# Strong-signal synthetic corpus (standing since #675): the engine must
# flag it at the engine layer; significance here is never promoted to a
# finding (Aug 28 2026 standing rule).
STRONG_META = [-0.60, -0.50, -0.70, -0.55, -0.65, -0.45]
STRONG_PEER = [0.30, 0.40, 0.35, 0.45, 0.25, 0.50]
# Near-null pair: the engine must stay silent.
NULL_META = [-0.05, 0.10, -0.12, 0.03, 0.08]
NULL_PEER = [0.02, -0.09, 0.11, -0.04, 0.06]

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


# Window files 686-689 must exist and carry README/ARCHITECTURE rows.
WINDOW_FILES = {
    686: "test_type_e_686_podcast_sentiment_60th_verification_gf499_holds_sep11_8pm.py",
    687: "test_type_a_687_verge_apple_duo_launch_vs_meta_muse_launch_register_sep11_9pm.py",
    688: "test_type_b_688_adam_sat_meta_dsa_addictive_design_vs_tiktok_dsa_byline_register_sep11_10pm.py",
    689: "test_type_c_689_meta_european_publishers_bundle_sep11_11pm.py",
}
EXPECTED_NEWEST_FIRST = [
    (690, "D"),
    (689, "C"),
    (688, "B"),
    (687, "A"),
    (686, "E"),
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


class TestIteration690Metadata:
    def test_docstring_ids(self):
        doc = __doc__
        assert "iteration 690" in doc
        assert "2026-09-12" in doc
        assert "Type D" in doc
        assert "goal_54093bda4145" in doc
        assert "mediascope-daily-iteration" in doc

    def test_rotation_c_to_d(self):
        assert "rotation 689 C -> 690 D" in __doc__

    def test_filename_convention(self):
        assert os.path.basename(__file__) == FILE_690


class TestScorerPair646:
    """Engine verification of the #687 publication-level pair (mechanism
    646): Meta [-0.35] vs Apple [+0.25, +0.50], n=1 vs n=2. The -0.725
    delta is pure arithmetic (block rounds to -0.73); the Welch
    significance machinery degenerates (t=0.0, p=1.0, is_significant
    False) while Cohen's d stays arithmetically nonzero - the degenerate
    contract binds significance, not effect-size arithmetic."""

    def test_asymmetry_delta_reproduces(self):
        # #673-style rounding-stage refinement: the engine scores raw arms
        # (-0.35) - (0.375) = -0.725, while the #687 block's -0.73 is
        # computed from the ROUNDED apple arm average 0.38 recorded in the
        # block ((-0.35) - (0.38) = -0.73). Both are pure arithmetic at
        # different rounding stages; the block's note ("delta = -0.35 -
        # 0.375 = -0.725 rounded to -0.73") documents its stage. Pin both.
        r = _score(TONE_META_687, TONE_APPLE_687, "the-verge")
        assert r.asymmetry_score == pytest.approx(-0.725)
        raw_delta = TONE_META_687[0] - sum(TONE_APPLE_687) / len(TONE_APPLE_687)
        assert r.asymmetry_score == pytest.approx(raw_delta)
        block_delta = TONE_META_687[0] - 0.38  # block's rounded arm average
        assert block_delta == pytest.approx(-0.73)
        assert DELTA_646_BLOCK == -0.73

    def test_t_statistic_is_zero(self):
        r = _score(TONE_META_687, TONE_APPLE_687, "the-verge")
        assert r.t_statistic == 0.0

    def test_p_value_is_one(self):
        r = _score(TONE_META_687, TONE_APPLE_687, "the-verge")
        assert r.p_value == 1.0

    def test_cohens_d_not_degenerate(self):
        # #682/#683 refinement: with one arm at n>=2 the pooled sd is
        # nonzero, so Cohen's d does NOT degenerate even though the Welch
        # significance machinery does. Pinned exactly.
        r = _score(TONE_META_687, TONE_APPLE_687, "the-verge")
        assert r.cohens_d == pytest.approx(-4.1012193308819755)

    def test_engine_not_significant(self):
        r = _score(TONE_META_687, TONE_APPLE_687, "the-verge")
        assert r.is_significant is False

    def test_bootstrap_ci_excludes_zero_but_flag_stays_false(self):
        # CI and t-test are different machinery: the bootstrap CI on this
        # degenerate pair excludes zero while is_significant stays False.
        # Per the Aug 28 standing rule the finding layer follows the flag,
        # so this is documented as machinery nuance, not a finding.
        r = _score(TONE_META_687, TONE_APPLE_687, "the-verge")
        assert r.confidence_interval_lower == pytest.approx(-0.85)
        assert r.confidence_interval_upper == pytest.approx(-0.6)
        assert r.confidence_interval_upper < 0.0
        assert r.is_significant is False

    def test_arm_swap_negates_and_stays_degenerate(self):
        r = _score(TONE_APPLE_687, TONE_META_687, "the-verge")
        assert r.asymmetry_score == pytest.approx(0.725)
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.is_significant is False


class TestScorerPair647:
    """Engine verification of the #688 byline-isolated pair (mechanism
    647): Meta [-0.50] vs TikTok [-0.50], n=1 per arm. Asymmetry 0.0 EXACT;
    full degenerate contract (t=0.0, p=1.0, d=0.0); block delta 0.00
    reproduces."""

    def test_asymmetry_delta_zero_exact(self):
        r = _score(TONE_META_688, TONE_TIKTOK_688, "nytimes")
        assert r.asymmetry_score == 0.0

    def test_t_statistic_is_zero(self):
        r = _score(TONE_META_688, TONE_TIKTOK_688, "nytimes")
        assert r.t_statistic == 0.0

    def test_p_value_is_one(self):
        r = _score(TONE_META_688, TONE_TIKTOK_688, "nytimes")
        assert r.p_value == 1.0

    def test_cohens_d_is_zero(self):
        r = _score(TONE_META_688, TONE_TIKTOK_688, "nytimes")
        assert r.cohens_d == 0.0

    def test_engine_not_significant(self):
        r = _score(TONE_META_688, TONE_TIKTOK_688, "nytimes")
        assert r.is_significant is False

    def test_arm_swap_stays_zero_degenerate(self):
        r = _score(TONE_TIKTOK_688, TONE_META_688, "nytimes")
        assert r.asymmetry_score == 0.0
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.is_significant is False


class TestNoEngineRun689:
    """#689 (mechanism 648) correctly runs NO engine: the block is a Type C
    deal-level leg whose falsification_family pin is a degenerate n=1
    illustrative pin. There are no tone arms for the engine to score.
    Type D read-only convention: the 648 block is untouched."""

    def _block(self):
        data = _yaml("profiles/competitor-entities.yaml")
        key = "mechanism_648_meta_european_publishers_bundle_mar2026"
        assert key in data["entities"]["meta"], "mechanism 648 missing"
        return data["entities"]["meta"][key]

    def test_mechanism_id_and_iteration(self):
        b = self._block()
        assert b["mechanism_id"] == 648
        assert b["iteration"] == 689
        assert b["rotation"] == "Type C"

    def test_no_tone_arms(self):
        b = self._block()
        for arm_key in ("meta_arm", "apple_arm", "tiktok_arm", "peer_arm",
                        "target_tones", "target_tones_manual_illustrative"):
            assert arm_key not in b, f"unexpected tone arm key: {arm_key}"
        raw = yaml.safe_dump(b)
        assert "tone_illustrative" not in raw or "illustrative_tone" in raw

    def test_seventeenth_pin_present(self):
        raw = yaml.safe_dump(self._block())
        assert "SEVENTEENTH falsification-family member" in raw

    def test_single_illustrative_pin_not_arms(self):
        b = self._block()
        fals = b["falsification_family"]
        assert "-0.55" in str(fals.get("illustrative_tone", ""))
        assert "n=1" in str(fals.get("excerpt_bounded", "")) or \
            "degenerate n=1 pin" in yaml.safe_dump(fals)

    def test_no_asymmetry_engine_claim(self):
        raw = yaml.safe_dump(self._block())
        assert "asymmetry_scorer" not in raw


class TestStatisticalMeaningfulness690:
    """The standing mandate: the engine flags real signal and stays silent
    on near-null. Engine-layer significance is never promoted to a finding
    per the Aug 28 2026 rule."""

    def test_strong_signal_engine_significant(self):
        r = _score(STRONG_META, STRONG_PEER, "synthetic")
        assert r.asymmetry_score == pytest.approx(-0.9500000000000001)
        assert r.t_statistic == pytest.approx(-17.59058189567848)
        assert r.p_value == pytest.approx(7.498515787192946e-09)
        assert r.cohens_d == pytest.approx(-10.155927192672127)
        assert r.is_significant is True
        assert r.confidence_interval_lower == pytest.approx(-1.0416666666666665)
        assert r.confidence_interval_upper == pytest.approx(-0.8500000000000001)
        assert r.confidence_interval_upper < 0.0

    def test_near_null_stays_silent(self):
        r = _score(NULL_META, NULL_PEER, "synthetic")
        assert r.p_value == pytest.approx(0.9431203973446252)
        assert r.is_significant is False


class TestCorpusIntegrityPost689:
    """Mechanisms 646/647/648 are present, unique, and correctly pinned;
    the modern (504+) id era is collision-free with max == 648."""

    def _mechanism_ids(self):
        ids = []

        def walk(node):
            if isinstance(node, dict):
                for k, v in node.items():
                    if k == "mechanism_id" and isinstance(v, int):
                        ids.append(v)
                    walk(v)
            elif isinstance(node, list):
                for v in node:
                    walk(v)

        for path in (
            "profiles/the-verge.yaml",
            "profiles/careers/journalists.yaml",
            "profiles/competitor-entities.yaml",
        ):
            walk(_yaml(path))
        return ids

    def test_mechanism_646_in_the_verge_yaml(self):
        data = _yaml("profiles/the-verge.yaml")
        key = ("mechanism_646_verge_apple_duo_launch_register_"
               "vs_meta_muse_launch_register_sep11")
        apple = data["competitor_relationships"]["apple"]
        assert key in apple
        b = apple[key]
        assert b["mechanism_id"] == 646
        assert b["iteration"] == 687
        assert b["iteration_type"] == "A"
        assert "-0.73" in str(yaml.safe_dump(b)) or \
            b["asymmetry_scorer"]["delta_meta_minus_apple"] == -0.73

    def test_mechanism_646_tone_arms_match_engine_inputs(self):
        data = _yaml("profiles/the-verge.yaml")
        key = ("mechanism_646_verge_apple_duo_launch_register_"
               "vs_meta_muse_launch_register_sep11")
        b = data["competitor_relationships"]["apple"][key]
        apple_tones = [i["tone_illustrative"]
                       for i in b["apple_arm"]["items"] if "tone_illustrative" in i]
        meta_tones = [i["tone_illustrative"]
                      for i in b["meta_arm"]["items"] if "tone_illustrative" in i]
        assert sorted(apple_tones) == sorted(TONE_APPLE_687)
        assert meta_tones == TONE_META_687

    def test_mechanism_647_in_journalists_yaml(self):
        data = _yaml("profiles/careers/journalists.yaml")
        key = ("mechanism_647_adam_sat_meta_dsa_addictive_design_"
               "vs_tiktok_dsa_byline_register_sep11")
        entries = [j for j in data["journalists"]
                   if isinstance(j, dict) and j.get("name") == "Adam Satariano"]
        assert len(entries) == 1
        b = entries[0][key]
        assert b["mechanism_id"] == 647
        assert b["iteration"] == 688
        assert b["type"] == "B"
        assert b["meta_arm"]["tone_illustrative"] == TONE_META_688[0]
        assert b["tiktok_arm"]["tone_illustrative"] == TONE_TIKTOK_688[0]
        assert b["asymmetry_scorer_result"]["delta_meta_minus_tiktok"] == 0.0

    def test_mechanism_648_in_competitor_entities_yaml(self):
        data = _yaml("profiles/competitor-entities.yaml")
        key = "mechanism_648_meta_european_publishers_bundle_mar2026"
        assert key in data["entities"]["meta"]
        b = data["entities"]["meta"][key]
        assert b["mechanism_id"] == 648
        assert b["iteration"] == 689

    def test_max_modern_mechanism_id_is_648(self):
        ids = self._mechanism_ids()
        modern = [i for i in ids if i >= 504]
        assert max(modern) == 648, f"max modern id wrong: {max(modern)}"

    def test_no_mechanism_649_in_profiles(self):
        text = _profiles_text()
        assert not re.search(r"mechanism_id:\s*649\b", text)

    def test_no_mechanism_649_key_in_profiles(self):
        text = _profiles_text()
        assert "mechanism_649" not in text

    def test_no_mechanism_649_in_tests(self):
        hits = []
        for root, _dirs, files in os.walk(TESTS_DIR):
            for f in files:
                if not f.endswith(".py"):
                    continue
                fp = os.path.join(root, f)
                with open(fp, encoding="utf-8") as fh:
                    text = fh.read()
                if re.search(r"mechanism_649\b", text) and fp != __file__:
                    hits.append(fp)
        assert hits == [], f"unexpected mechanism 649 references: {hits}"


class TestLedgerIntegrity690:
    """Ledger pins: the falsification ledger advances to 17 via mechanism
    647 SIXTEENTH (#688) and mechanism 648 El Pais SEVENTEENTH (#689);
    FIFTEENTH stays on mechanism 643; no EIGHTEENTH. The #609 first-gen
    OpenAI publisher renewal cohort stays closed at 7/7 (News Corp SEVENTH);
    the divergence ratchet holds at 8, no NINTH."""

    def test_sixteenth_pin_present(self):
        text = _profiles_text()
        assert "SIXTEENTH falsification-family member" in text

    def test_seventeenth_pin_present(self):
        text = _profiles_text()
        assert "SEVENTEENTH falsification-family member" in text

    def test_fifteenth_pin_still_present(self):
        text = _profiles_text()
        assert "FIFTEENTH falsification-family member" in text

    def test_no_eighteenth_falsification_member(self):
        text = _profiles_text()
        assert "EIGHTEENTH" not in text

    def test_646_is_not_falsification_member(self):
        block = _yaml("profiles/the-verge.yaml")["competitor_relationships"][
            "apple"
        ]["mechanism_646_verge_apple_duo_launch_register_"
            "vs_meta_muse_launch_register_sep11"]
        assert block["falsification_family_member"] is False
        assert block["falsification_note"].startswith(
            "NOT a falsification-family member"
        )

    def test_no_eighth_renewal_cohort_member(self):
        text = _profiles_text()
        assert "EIGHTH member of the #609" not in text
        assert "eighth member of the #609" not in text

    def test_seventh_cohort_member_still_newscorp(self):
        text = _profiles_text()
        assert ("SEVENTH member of the #609 first-gen OpenAI publisher "
                "renewal cohort") in text

    def test_no_ninth_divergence_pin(self):
        text = _profiles_text()
        assert text.count("EIGHTH DIVERGENCE PIN") == 1
        assert "NINTH" not in text


class TestTypeEPodcastSentimentIntegrity690:
    """Type E integrity: podcast-sentiment.md keeps the Everyone Hates Elon
    activist-group (not a podcast) row and the Attention Sphere row with
    60 verification cycles through Sep 11 2026 (per #686)."""

    def _text(self):
        with open(os.path.join(REPO_ROOT, "podcast-sentiment.md"),
                  encoding="utf-8") as fh:
            return fh.read()

    def test_attention_sphere_60th_cycle(self):
        text = self._text()
        assert "Attention Sphere" in text
        assert "60" in text

    def test_everyone_hates_elon_not_podcast(self):
        text = self._text()
        assert "Everyone Hates Elon" in text
        assert "not a podcast" in text.lower() or "NOT a podcast" in text

    def test_guilty_feminist_present(self):
        text = self._text()
        assert "Guilty Feminist" in text


class TestRotationCycleGuard690:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #690 main-commit SHA is known.
    ANCHORED_SHA = "5623665f26c9a5211dc9ab3395c59075a7731216"  # patched in followup per #565 convention

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

    def test_window_686_690_closes_c_to_d(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("D", "690"),
            ("C", "689"),
            ("B", "688"),
            ("A", "687"),
            ("E", "686"),
        ], f"rotation window 686-690 wrong: {observed}"

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
        # Post-commit anchor: the #690 main commit. Patched in the followup
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
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #690:", l)]
        assert len(mains) == 1, f"expected one Type D #690 main: {mains}"
        sha = mains[0].split(" ", 1)[0]
        assert sha == self.ANCHORED_SHA, f"anchor not yet patched: {sha}"


class TestIteration690NoveltyAnchor:
    """Deselected pre-commit per the #565 followup convention; patched
    green post-doc-sync. Novelty was verified pre-commit by shell
    greps (zero test_type_d_690 files, no #690 in git log,
    max mechanism 648, no 649 anywhere); this test pins that no
    duplicate #690 main commit ever appears."""

    def test_type_d_690_file_unique(self):
        matches = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_d_690*.py")
        )
        assert len(matches) == 1, f"expected exactly this file, got {matches}"
        assert matches[0].endswith(FILE_690)

    def test_type_d_690_main_commit_unique_and_anchored(self):
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #690:", l)]
        assert len(mains) == 1, (
            f"expected exactly one Type D #690 main commit, got: {mains}"
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard690.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, f"main commit {sha} != guard anchor {anchor}"


class TestWindow686to689Persistence:
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


class TestCrossDocHeaderAgreement690:
    """Durable guard for the #499 miss: README-only sync tooling left the
    ARCHITECTURE.md tests/ tree header stale. Both docs' headers must agree
    with each other and with the files on disk."""

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


class TestDocSync690:
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

    def test_690_row_in_readme_table(self):
        with open(README, encoding="utf-8") as fh:
            assert FILE_690 in fh.read()

    def test_690_row_in_architecture_tree(self):
        with open(ARCH, encoding="utf-8") as fh:
            assert FILE_690 in fh.read()


class TestYamlIntegrity690:
    @pytest.mark.parametrize(
        "path",
        [
            "profiles/competitor-entities.yaml",
            "profiles/competitor-coverage-research.yaml",
            "profiles/the-verge.yaml",
            "profiles/careers/journalists.yaml",
        ],
    )
    def test_yaml_parses(self, path):
        assert _yaml(path) is not None
