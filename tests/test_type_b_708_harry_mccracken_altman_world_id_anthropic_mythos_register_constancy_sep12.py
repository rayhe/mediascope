"""Type B #708: Harry McCracken (Fast Company) same-journalist cross-entity
column-register pair - temporal falsification update on the Aug 20 file-local
McCracken CEO-attribution finding (mechanism #201, iteration #209).

Finding: REGISTER CONSTANCY in the adversarial AI-strategy column register -
TWENTY-SECOND falsification-family member (journalist-attribution class).
McCracken applies CEO-personalized adversarial framing to Altman (-0.50
illustrative: "lashes it to the controversy he generates in his day job",
Altman named in the headline, "strange mini-scandal") and mission-dismissive
framing to Anthropic (-0.45 illustrative: "obsessing over AGI is folly") at
the same intensity as his Meta corpus (-0.38 illustrative: "fixated",
"ego is intertwined", anonymous critics). The journalist-level "McCracken
humanizes non-Meta CEOs" attribution from the Aug 20 CEO-attribution thesis
fails for OpenAI-adjacent and Anthropic entities in the Apr 2026 column
register - the humanization differential is Snap-specific and CEO-access-driven
(exclusive Spiegel interview), not a Meta-exclusion rule.

Arms:
- Altman arm (Apr 24 2026): "Can Sam Altman make proving you're human seem
  cool - and essential?" (Fast Company; title em dash rendered as hyphen per
  ASCII-only corpus convention)
  https://www.fastcompany.com/91531465/world-id-tools-for-humanity-proof-of-human-worldcoin
- Anthropic arm (Apr 10 2026): "Anthropic's 'Mythos' AI proves that obsessing
  over AGI is folly" (Fast Company; canonical URL not verbatim-recoverable
  this run - none constructed)
- Meta arm (carried from the Aug 20 file-local mechanism #201): 2021
  "Facebook gets in your Ray-Bans" (balanced, "Dystopia averted") + 2022
  "Why Mark Zuckerberg is fixated on creating AR's 'iPhone moment'"
  (adversarial CEO-attribution)

Evidence grade: competitor arms second-hand (excerpt-bounded) - title/date/
byline/dek plus body excerpts verbatim from search results this run (crawled
2d); full columns NOT read first-hand, per the #503 precedent, disclosed.
Meta arm carried from the Aug 20 file-local test which verified the Fast
Company source URLs.

Mechanism 659, first mechanism key on the new Harry McCracken journalist
entry in profiles/careers/journalists.yaml.
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

MECH_KEY = "mechanism_659_harry_mccracken_altman_world_id_anthropic_mythos_adversarial_register_constancy_sep12"
ALTMAN_URL = "https://www.fastcompany.com/91531465/world-id-tools-for-humanity-proof-of-human-worldcoin"

# Patched to the real main-commit SHA in the followup commit per the #565
# convention; the guard classes are deselected pre-commit.
ANCHORED_SHA = "b35d217defbb2ba9cdb24ad01b2be138f03c28c9"


def _careers():
    with open(CAREERS_PATH) as f:
        return yaml.safe_load(f)["journalists"]


def _mccracken():
    matches = [j for j in _careers() if j.get("name") == "Harry McCracken"]
    assert len(matches) == 1, "expected exactly one Harry McCracken entry"
    return matches[0]


def _mechanism():
    o = _mccracken()
    assert MECH_KEY in o, "mechanism_659 key missing on the McCracken entry"
    return o[MECH_KEY]


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args],
        capture_output=True,
        text=True,
        timeout=60,
    )


class TestHarryMcCrackenAltmanArm:
    def test_altman_column_title_and_date(self):
        m = _mechanism()
        arm = m["altman_arm"]
        assert arm["date"] == "2026-04-24"
        assert arm["title"] == "Can Sam Altman make proving you are human seem cool - and essential?"
        assert "em dash" in arm["title_note"]

    def test_altman_column_url_is_verbatim_fastcompany(self):
        m = _mechanism()
        assert m["altman_arm"]["url"] == ALTMAN_URL
        assert m["altman_arm"]["url"].startswith("https://www.fastcompany.com/91531465/")

    def test_altman_column_sole_byline_attested(self):
        m = _mechanism()
        arm = m["altman_arm"]
        assert arm["byline"] == "Harry McCracken (sole)"
        assert "BuzzSumo" in arm["byline_attribution"]
        assert "Plugged In" in arm["byline_attribution"]

    def test_altman_column_ceo_personalization_evidence(self):
        m = _mechanism()
        detail = m["altman_arm"]["register_detail"]
        # The #201 thesis treated CEO-personalized adversarial framing as
        # Meta-exclusive; the Altman column falsifies that at the journalist level.
        assert "Altman" in m["altman_arm"]["title"]
        assert "lashes it to the controversy he generates in his day job" in detail
        assert "strange mini-scandal" in detail
        assert "miscommunication" in detail
        assert "clawing back a shred of pre-AI normalcy" in detail

    def test_altman_column_tone_and_evidence_grade(self):
        m = _mechanism()
        arm = m["altman_arm"]
        assert arm["tone_illustrative"] == -0.50
        assert "second-hand" in arm["evidence_grade"]
        assert "#503" in arm["evidence_grade"]
        assert "NOT read first-hand" in arm["evidence_grade"]


class TestHarryMcCrackenAnthropicMythosArm:
    def test_mythos_column_title_and_date(self):
        m = _mechanism()
        arm = m["anthropic_arm"]
        assert arm["date"] == "2026-04-10"
        assert arm["title"] == "Anthropic's 'Mythos' AI proves that obsessing over AGI is folly"

    def test_mythos_column_mission_dismissive_framing(self):
        m = _mechanism()
        detail = m["anthropic_arm"]["register_detail"]
        assert "obsessing over AGI is folly" in detail
        assert "we can't wait for fixes" in detail

    def test_mythos_column_no_invented_url(self):
        # The canonical URL was not verbatim-recoverable; none was constructed.
        m = _mechanism()
        arm = m["anthropic_arm"]
        assert "url" not in arm, "no URL key: none was verbatim-recoverable"
        assert "No URL constructed or guessed" in arm["canonical_url_note"]
        assert arm["tone_illustrative"] == -0.45
        assert "second-hand" in arm["evidence_grade"]


class TestHarryMcCrackenMetaArmCarried:
    def test_meta_arm_carries_201_corpus(self):
        m = _mechanism()
        arm = m["meta_arm"]
        assert "mechanism #201" in arm["title"]
        assert arm["tone_illustrative"] == -0.38

    def test_meta_arm_2021_balanced_piece_evidence(self):
        m = _mechanism()
        detail = m["meta_arm"]["register_detail"]
        assert "Dystopia averted" in detail
        assert "https://www.fastcompany.com/90673958/facebook-smart-glasses-ray-ban-stories-luxottica" in detail

    def test_meta_arm_2022_ego_piece_evidence(self):
        m = _mechanism()
        detail = m["meta_arm"]["register_detail"]
        assert "ego is intertwined" in detail
        assert "fixated on creating AR's 'iPhone moment'" in detail
        assert "https://www.fastcompany.com/90741172/mark-zuckerberg-meta-ar-glasses-nazere-hypernova" in detail


class TestPairMechanism708:
    def test_delta_is_near_null_constancy(self):
        m = _mechanism()
        r = m["asymmetry_scorer_result"]
        assert r["target_avg"] == -0.475
        assert r["reference_avg"] == -0.38
        assert abs(r["delta_competitor_minus_meta"] - (-0.10)) < 1e-9
        assert abs(r["delta_competitor_minus_meta"]) < 0.15

    def test_illustrative_only_contract(self):
        m = _mechanism()
        r = m["asymmetry_scorer_result"]
        assert r["p_value"] == "NOT_CALCULATED"
        assert r["cohens_d"] == "NOT_CALCULATED"
        assert r["ci"] == "NOT_CALCULATED"
        assert r["is_significant"] is False
        assert r["statistical_contract"] == "degenerate_n1_per_arm"
        assert r["artifact_grade"] is False
        assert "MANUAL ILLUSTRATIVE" in r["method"]

    def test_register_bound_not_contradiction(self):
        m = _mechanism()
        note = m["register_bound_note"]
        assert note["contradiction"] is False
        assert "Snap-specific" in note["bound_statement"]
        assert "CEO-access-driven" in note["bound_statement"]
        assert "not a Meta-exclusion rule" in note["bound_statement"]

    def test_altman_headline_personalization_corroboration(self):
        # The Altman headline itself personalizes to "Sam Altman" - a register
        # break from any Meta-only-personalization reading.
        m = _mechanism()
        assert "Sam Altman" in m["altman_arm"]["title"]
        assert "register break" in m["verdict"]


class TestFinancialContext708:
    def test_zero_gradient_control(self):
        m = _mechanism()
        fc = m["financial_context"]
        assert fc["predictor"] == "null_tie_control"
        assert fc["prediction"] == "no_differential_prediction"
        assert "NO known AI content licensing deals" in fc["detail"]

    def test_correlation_not_causation(self):
        m = _mechanism()
        assert "Correlation, not causation" in m["financial_context"]["detail"]
        assert "No analysis.json update warranted" in m["verdict"]


class TestMechanism659Yaml:
    def test_mechanism_id_and_iteration(self):
        m = _mechanism()
        assert m["mechanism_id"] == 659
        assert m["iteration"] == 708
        assert m["type"] == "B"

    def test_first_mechanism_key_on_new_entry(self):
        o = _mccracken()
        mech_keys = [k for k in o if k.startswith("mechanism_")]
        assert mech_keys == [MECH_KEY]
        assert o["publication"] == "Fast Company"

    def test_twenty_second_falsification_family_member(self):
        m = _mechanism()
        assert "TWENTY-SECOND" in m["verdict"]
        assert "falsification-family member" in m["verdict"]
        assert "journalist-attribution class" in m["verdict"]

    def test_confounders_ranked_with_strong_first(self):
        m = _mechanism()
        confs = m["confounders"]
        strong = [c for c in confs if c.startswith("[STRONG]")]
        moderate = [c for c in confs if c.startswith("[MODERATE]")]
        weak = [c for c in confs if c.startswith("[WEAK]")]
        assert len(strong) == 3
        assert len(moderate) == 2
        assert len(weak) == 1
        assert any("TFH-is-not-OpenAI" in c for c in strong)
        assert any("second-hand bounded" in c.lower() for c in strong)
        assert any("CEO-access asymmetry" in c for c in moderate)

    def test_novelty_and_rotation(self):
        m = _mechanism()
        assert "FIRST YAML mechanism on Harry McCracken" in m["novelty"]
        assert "Rotation: 707 A -> 708 B" in m["novelty"]
        assert "#703/m656" in m["novelty"]

    def test_no_em_dash_in_mechanism_or_file(self):
        m = _mechanism()
        assert "\u2014" not in str(m), "em dash found in mechanism block"
        with open(os.path.join(TESTS_DIR, TEST_BASENAME)) as f:
            assert "\u2014" not in f.read(), "em dash found in test file"


class TestRotationCycleGuard708:
    """Deselected pre-commit; anchor patched in the followup commit."""

    ANCHORED_SHA = ANCHORED_SHA

    def test_type_b_708_file_unique(self):
        matches = glob.glob(os.path.join(TESTS_DIR, "test_type_b_708*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_b_708_main_commit_unique_and_anchored(self):
        # Runs green only post-main-commit per the #565 followup convention.
        # Deselect pre-commit; the followup patches ANCHORED_SHA to the real
        # main-commit SHA. Novelty was verified pre-commit by shell greps
        # (zero test_type_b_708 files, no #708 in git log, zero
        # mechanism_659 keys in profiles/, no McCracken journalist entry,
        # both Apr 2026 column titles new-to-corpus, #201/m201 as the
        # bounded prior for the Meta-vs-Snap CEO-attribution differential).
        import re
        out = _run_git("log", "--format=%H %s")
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type B #708:", line)
        ]
        assert len(mains) == 1, "expected exactly one Type B #708 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard708.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )
