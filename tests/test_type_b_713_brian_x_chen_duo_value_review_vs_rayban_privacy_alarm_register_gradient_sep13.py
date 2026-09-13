"""Type B #713: Brian X. Chen (NYT) same-journalist cross-entity register pair -
second-Apple-comparator extension of the #458/m484 Chen privacy-bifurcation
finding (m484 paired the Meta Ray-Ban arm with the Apple Vision Pro arm).

Finding: BOUNDED ASYMMETRY in the #663 gradient-absent family. Chen applies
the privacy-alarm register to Meta's Ray-Ban glasses (-0.50 illustrative:
LED covert-capture experiment, Gilliard private-space interview, "alarming
for privacy in private spaces") and the consumer value-review register to
Apple's iPhone Duo (+0.15 illustrative, carried from #712: price-skepticism
title, trade-off listing, mild hands-on positives). The m484 bifurcation
direction (Meta alarm, Apple non-alarm) reproduces on a second, newer Apple
comparator. Illustrative delta (Meta minus Apple) -0.65, degenerate n=1 vs
n=1 per #638/#643, MANUAL ILLUSTRATIVE only, no engine run.

Arms:
- Meta arm (Dec 2023, carried from #458/m484): "Meta's Ray-Bans Are Alarming
  for Privacy in Private Spaces, Not in Public" (NYT Tech Fix column)
  https://pxlnv.com/linklog/meta-ray-bans-privacy/ (Pixel Envy linklog quoting
  the column verbatim; nytimes.com canonical URL not verbatim-recoverable
  this run - none constructed per #503)
- Apple arm (Sep 2026, carried from #712/m661): "Why is Apple's New Foldable
  iPhone Duo $1,999?" (NYT, Brian X. Chen, photos by Jason Henry; nytimes.com
  blocked - #712 used verbatim Chen passages on a mirror plus 2 syndications)

Evidence grade: both arms second-hand (excerpt-bounded) - Meta arm via Pixel
Envy verbatim excerpts (search-result verbatim this run, crawled 13d);
Apple arm carried from #712's mirror/syndication excerpts; nytimes.com
blocked for direct fetch on both runs, per the #503 precedent, disclosed.

Financial context: ZERO-GRADIENT CONTROL. NYT x Apple: no AI content
licensing deal on record; NYT left Apple News in 2020 (carried from #712).
NYT x Meta: no AI licensing deal on record (Meta's Mar 2026 European
publisher bundle #689 covered Le Figaro/Prisa/Suddeutsche Zeitung, not NYT).
The deal theory makes no differential prediction; the observed register gap
is genre/peg/timing driven. NOT a falsification-family member; the ledger
stays at 22 after #708's TWENTY-SECOND. Correlation, not causation. No
analysis.json update warranted.

Mechanism 662, first mechanism key on the Brian X. Chen journalist entry in
profiles/careers/journalists.yaml.
"""

import glob
import os
import subprocess

import pytest
import yaml


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
TEST_BASENAME = os.path.basename(__file__)
CAREERS_PATH = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")

MECH_KEY = "mechanism_662_brian_x_chen_duo_value_review_vs_rayban_privacy_alarm_register_gradient_sep13"
PXLNV_URL = "https://pxlnv.com/linklog/meta-ray-bans-privacy/"
FB_DATA_URL = "https://www.nytimes.com/2018/04/11/technology/personaltech/i-downloaded-the-information-that-facebook-has-on-me-yikes.html"

# Patched to the real main-commit SHA in the followup commit per the #565
# convention; the guard classes are deselected pre-commit.
ANCHORED_SHA = "PATCHED_IN_FOLLOWUP_PER_565"


def _careers():
    with open(CAREERS_PATH) as f:
        return yaml.safe_load(f)["journalists"]


def _chen():
    matches = [j for j in _careers() if j.get("name") == "Brian X. Chen"]
    assert len(matches) == 1, "expected exactly one Brian X. Chen entry"
    return matches[0]


def _mechanism():
    o = _chen()
    assert MECH_KEY in o, "mechanism_662 key missing on the Chen entry"
    return o[MECH_KEY]


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args],
        capture_output=True,
        text=True,
        timeout=60,
    )


class TestBrianXChenMetaRayBanArm:
    def test_rayban_piece_title_and_date(self):
        m = _mechanism()["meta_arm"]
        assert m["title"] == "Meta's Ray-Bans Are Alarming for Privacy in Private Spaces, Not in Public"
        assert m["date"] == "2023-12"
        assert m["byline"] == "Brian X. Chen (sole)"

    def test_rayban_pxlnv_url_verbatim(self):
        m = _mechanism()["meta_arm"]
        assert m["url"] == PXLNV_URL
        assert "none constructed per #503" in m["url_note"]

    def test_rayban_led_experiment_evidence(self):
        detail = _mechanism()["meta_arm"]["register_detail"]
        assert "200 photos and videos" in detail
        assert "BART trains" in detail
        assert "no one looked at the LED light" in detail

    def test_rayban_gilliard_interview(self):
        detail = _mechanism()["meta_arm"]["register_detail"]
        assert "Chris Gilliard" in detail
        assert "private-space" in detail

    def test_rayban_privacy_alarm_framing(self):
        m = _mechanism()["meta_arm"]
        assert "privacy-alarm" in m["register"]
        assert "alarming for privacy in private spaces" in m["register_detail"]

    def test_rayban_tone_and_evidence_grade(self):
        m = _mechanism()["meta_arm"]
        assert m["tone_illustrative"] == -0.50
        assert "second-hand (excerpt-bounded)" in m["evidence_grade"]
        assert "#503" in m["evidence_grade"]


class TestBrianXChenAppleDuoArmCarried:
    def test_duo_title_carried_from_712(self):
        m = _mechanism()["apple_arm"]
        assert m["title"] == "Why is Apple's New Foldable iPhone Duo $1,999?"
        assert m["date"] == "2026-09"

    def test_duo_chen_byline_carried(self):
        m = _mechanism()["apple_arm"]
        assert "Brian X. Chen" in m["byline"]
        assert "carried from #712" in m["byline_attribution"]

    def test_duo_value_review_register(self):
        m = _mechanism()["apple_arm"]
        assert "value review" in m["register"]
        detail = m["register_detail"]
        assert "crease in the center" in detail
        assert "fingerprint sensor" in detail
        assert "extremely thin" in detail

    def test_duo_tone_carried(self):
        m = _mechanism()["apple_arm"]
        assert m["tone_illustrative"] == 0.15

    def test_duo_evidence_grade_carried_second_hand(self):
        m = _mechanism()["apple_arm"]
        assert "carried from #712/m661" in m["evidence_grade"]
        assert "second-hand (excerpt-bounded)" in m["evidence_grade"]
        assert "No URL constructed or guessed" in m["canonical_url_note"]


class TestPairMechanism713:
    def test_delta_meta_minus_apple(self):
        r = _mechanism()["asymmetry_scorer_result"]
        assert r["delta_meta_minus_apple"] == -0.65
        assert abs(r["target_avg"] - r["reference_avg"] - r["delta_meta_minus_apple"]) < 1e-9

    def test_illustrative_only_contract(self):
        r = _mechanism()["asymmetry_scorer_result"]
        assert "MANUAL ILLUSTRATIVE" in r["method"]
        assert r["p_value"] == "NOT_CALCULATED"
        assert r["cohens_d"] == "NOT_CALCULATED"
        assert r["ci"] == "NOT_CALCULATED"
        assert r["is_significant"] is False
        assert r["artifact_grade"] is False

    def test_degenerate_statistical_contract(self):
        r = _mechanism()["asymmetry_scorer_result"]
        assert r["statistical_contract"] == "degenerate_n1_per_arm"
        assert r["target_tones_manual_illustrative"] == [-0.50]
        assert r["reference_tones_manual_illustrative"] == [0.15]

    def test_extends_m484_second_comparator(self):
        m = _mechanism()
        assert "second-Apple-comparator extension" in m["pair_shape"]
        assert "#458/m484" in m["pair_shape"]
        assert "Vision Pro" in m["pair_shape"]
        assert "BOUNDED ASYMMETRY" in m["verdict"]
        assert "NOT a falsification-family member" in m["verdict"]

    def test_both_arms_positive_chen_bylines(self):
        # iteration-492 rule: no zero-coverage claims; both arms are
        # positive Chen bylines.
        m = _mechanism()
        assert "Brian X. Chen" in m["meta_arm"]["byline"]
        assert "Brian X. Chen" in m["apple_arm"]["byline"]
        assert "iteration-492" in " ".join(m["cross_references"])


class TestFinancialContext713:
    def test_zero_gradient_control(self):
        f = _mechanism()["financial_context"]
        assert f["predictor"] == "zero_gradient_control"
        assert f["prediction"] == "no_differential_prediction"

    def test_nyt_apple_no_ai_deal(self):
        detail = _mechanism()["financial_context"]["detail"]
        assert "NYT x Apple: NO known AI content licensing deal" in detail
        assert "left Apple News in 2020" in detail

    def test_nyt_meta_no_ai_deal(self):
        detail = _mechanism()["financial_context"]["detail"]
        assert "NYT x Meta: NO known AI licensing deal" in detail
        assert "#689" in detail

    def test_correlation_not_causation(self):
        f = _mechanism()["financial_context"]
        assert "Correlation, not causation" in f["detail"]
        assert "#663 family" in f["detail"]


class TestCounterevidence713:
    def test_2018_facebook_data_column_url_verbatim(self):
        ce = _mechanism()["counterevidence"]
        assert any(FB_DATA_URL in c for c in ce)
        assert any("longstanding Tech Fix mode" in c for c in ce)

    def test_chen_applies_critical_register_to_apple(self):
        ce = _mechanism()["counterevidence"]
        assert any("iPhone Air" in c and "thin-is-not-enough" in c for c in ce)

    def test_polk_breadth_not_meta_exclusion(self):
        ce = _mechanism()["counterevidence"]
        assert any("George Polk" in c and "Silicon Valley" in c for c in ce)


class TestMechanism662Yaml:
    def test_mechanism_id_and_iteration(self):
        m = _mechanism()
        assert m["mechanism_id"] == 662
        assert m["iteration"] == 713
        assert m["type"] == "B"
        assert m["journalist"] == "Brian X. Chen"
        assert m["publication"] == "The New York Times"

    def test_first_mechanism_key_on_chen_entry(self):
        o = _chen()
        mech_keys = [k for k in o if k.startswith("mechanism_")]
        assert mech_keys == [MECH_KEY]
        assert list(o.keys())[0] == MECH_KEY
        assert o["name"] == "Brian X. Chen"

    def test_bounded_asymmetry_not_falsification_member(self):
        m = _mechanism()
        assert "BOUNDED ASYMMETRY" in m["verdict"]
        assert "NOT a falsification-family member" in m["verdict"]
        assert "gradient-absent family" in m["verdict"]

    def test_ledger_stays_at_22(self):
        m = _mechanism()
        assert "the ledger stays at 22" in m["verdict"]
        assert "TWENTY-SECOND" in m["verdict"]

    def test_confounders_ranked_with_strong_first(self):
        m = _mechanism()
        confs = m["confounders"]
        strong = [c for c in confs if c.startswith("[STRONG]")]
        moderate = [c for c in confs if c.startswith("[MODERATE]")]
        weak = [c for c in confs if c.startswith("[WEAK]")]
        assert len(strong) == 3
        assert len(moderate) == 2
        assert len(weak) == 1
        assert any("Genre skew" in c for c in strong)
        assert any("News-peg asymmetry" in c for c in strong)
        assert any("Temporal gap" in c for c in strong)
        assert any("Second-hand bounded" in c for c in moderate)

    def test_novelty_and_rotation(self):
        m = _mechanism()
        assert "FIRST mechanism key on the Brian X. Chen journalist entry" in m["novelty"]
        assert "Rotation: 712 A -> 713 B" in m["novelty"]
        assert "#458/m484" in m["novelty"]
        assert "Duo-vs-Ray-Ban Chen pair was never a mechanism" in m["novelty"]

    def test_no_em_dash_in_mechanism_or_file(self):
        m = _mechanism()
        assert "\u2014" not in str(m), "em dash found in mechanism block"
        with open(os.path.join(TESTS_DIR, TEST_BASENAME)) as f:
            assert "\u2014" not in f.read(), "em dash found in test file"


class TestRotationCycleGuard713:
    """Deselected pre-commit; anchor patched in the followup commit."""

    ANCHORED_SHA = ANCHORED_SHA

    def test_type_b_713_file_unique(self):
        matches = glob.glob(os.path.join(TESTS_DIR, "test_type_b_713*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_b_713_main_commit_unique_and_anchored(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA. Novelty was verified pre-commit by shell greps
        # (zero test_type_b_713 files, no #713 in git log, zero
        # mechanism_662 keys in profiles/, zero mechanisms on the Chen
        # journalist entry, m484 as the bounded Vision-Pro-comparator prior,
        # #712 as the carried Duo-arm source).
        import re
        out = _run_git("log", "--format=%H %s")
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type B #713:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type B #713 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard713.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )
