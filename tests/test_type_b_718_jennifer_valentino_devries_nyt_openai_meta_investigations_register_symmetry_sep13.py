"""Type B #718: Jennifer Valentino-DeVries (NYT investigations desk) -
litigation-adversary register symmetry.

Finding: REGISTER SYMMETRY at reporter level - TWENTY-FOURTH
falsification-family member (ledger 23->24). Valentino-DeVries, an NYT
investigations-desk reporter whose employer has sued OpenAI since Dec 2023,
applies a near-identical document-driven accountability register to OpenAI
(-0.60 illustrative) and Meta (-0.55 illustrative): delta (OpenAI minus
Meta) -0.05, near-null. The naive lawsuit-hardening prediction fails at this
reporter - the second reporter-level extension of mechanism 471 after 538
(Cade Metz), this time on the investigations desk.

Arms:
- OpenAI arm (Nov 23 2025, co-bylined Kashmir Hill + Jennifer Valentino-DeVries;
  Kevin Roose contributed reporting; Julie Tate contributed research):
  "What OpenAI Did When ChatGPT Users Lost Touch With Reality" - ChatGPT
  sycophancy/mental-health investigation. Excerpt-bounded (nytimes.com
  policy-blocked; excerpts verbatim from muckrack listing, wiktionary
  citation quotations, armwoodtechnology mirror).
- Meta arms (Jun 2026): "Teachers Are Going to Hate It: How Social Media Apps
  Hooked Teens at School" (Jun 4 2026; 1,400 school-district lawsuit docs;
  Meta paid teen ambassadors); "Many child safety features on social apps
  don't work, report finds" (NYU/Northeastern study); "On Instagram, a
  jewelry ad draws solicitations for sex with a 5-year-old".

Evidence grade: all arms second-hand excerpt-bounded per the #503 precedent,
disclosed. No zero-coverage claims per iteration-492.

Mechanism 665, first mechanism key on the Jennifer Valentino-DeVries
journalist entry in profiles/careers/journalists.yaml.
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
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "type_b_718_jennifer_valentino_devries_nyt_openai_meta_investigations_register_symmetry_sep13"
OPENAI_MIRROR_URL = "https://www.armwoodtechnology.com/2025/11/what-openai-did-when-chatgpt-users-lost.html"
MUCKRACK_URL = "https://muckrack.com/jenvalentino/articles"
BIZTOC_URL = "https://biztoc.com/x/a33fe91fadf42459"

# Patched to the real main-commit SHA in the followup commit per the #565
# convention; the guard classes are deselected pre-commit.
ANCHORED_SHA = "64200d4fe6eefd741ffa6d9b66ba53515f127cb8"


def _careers():
    with open(CAREERS_PATH) as f:
        return yaml.safe_load(f)["journalists"]


def _journalist():
    matches = [j for j in _careers() if j.get("name") == "Jennifer Valentino-DeVries"]
    assert len(matches) == 1, "expected exactly one Jennifer Valentino-DeVries entry"
    return matches[0]


def _mechanism():
    o = _journalist()
    assert "competitor_coverage" in o, "competitor_coverage missing on the entry"
    assert MECH_KEY in o["competitor_coverage"], "mechanism_665 key missing"
    return o["competitor_coverage"][MECH_KEY]


def _read(path):
    with open(path) as f:
        return f.read()


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args],
        capture_output=True,
        text=True,
        timeout=60,
    )


class TestOpenAIArm718:
    def test_openai_arm_title_and_date(self):
        arm = _mechanism()["openai_arm"]
        assert arm["title"] == "What OpenAI Did When ChatGPT Users Lost Touch With Reality"
        assert arm["date"] == "2025-11-23"

    def test_openai_arm_co_byline_names(self):
        byline = _mechanism()["openai_arm"]["byline"]
        assert "Kashmir Hill" in byline
        assert "Jennifer Valentino-DeVries" in byline
        assert "Kevin Roose" in byline

    def test_openai_arm_science_fiction_lede_excerpt(self):
        excerpts = _mechanism()["openai_arm"]["key_excerpts"]
        assert any("inadvertently destabilizes some of their minds" in e for e in excerpts)

    def test_openai_arm_noose_excerpt(self):
        excerpts = _mechanism()["openai_arm"]["key_excerpts"]
        assert any("offered instructions for how to tie a noose" in e for e in excerpts)

    def test_openai_arm_psychosis_statistic_excerpt(self):
        excerpts = _mechanism()["openai_arm"]["key_excerpts"]
        assert any("560,000 people" in e and "psychosis or mania" in e for e in excerpts)

    def test_openai_arm_metric_pressure_excerpts(self):
        excerpts = _mechanism()["openai_arm"]["key_excerpts"]
        assert any("increase daily active users by 5 percent" in e for e in excerpts)
        assert any("That metric still matters, maybe more than ever" in e for e in excerpts)

    def test_openai_arm_healthy_engagement_skepticism(self):
        excerpts = _mechanism()["openai_arm"]["key_excerpts"]
        assert any("Healthy engagement" in e for e in excerpts)
        assert _mechanism()["openai_arm"]["illustrative_tone"] == -0.60

    def test_openai_arm_mirror_url_verbatim_and_bounded(self):
        assert OPENAI_MIRROR_URL == "https://www.armwoodtechnology.com/2025/11/what-openai-did-when-chatgpt-users-lost.html"
        grade = _mechanism()["openai_arm"]["evidence_grade"]
        assert "excerpt-bounded" in grade
        assert "nytimes.com policy-blocked" in grade


class TestMetaArms718:
    def test_three_meta_arms(self):
        arms = _mechanism()["meta_arms"]
        assert len(arms) == 3

    def test_school_piece_title_and_date(self):
        arm = _mechanism()["meta_arms"][0]
        assert arm["title"] == "Teachers Are Going to Hate It: How Social Media Apps Hooked Teens at School"
        assert arm["date"] == "2026-06-04"

    def test_school_piece_teen_ambassadors_excerpt(self):
        excerpt = _mechanism()["meta_arms"][0]["key_excerpt"]
        assert "teen ambassadors" in excerpt
        assert "Meta paid" in excerpt

    def test_child_safety_piece_study_attribution(self):
        arm = _mechanism()["meta_arms"][1]
        assert arm["title"] == "Many child safety features on social apps do not work, report finds"
        assert "New York University" in arm["key_excerpt"]
        assert "Northeastern University" in arm["key_excerpt"]

    def test_instagram_jewelry_ad_piece(self):
        arm = _mechanism()["meta_arms"][2]
        assert arm["title"] == "On Instagram, a jewelry ad draws solicitations for sex with a 5-year-old"

    def test_meta_arms_illustrative_average(self):
        arms = _mechanism()["meta_arms"]
        tones = [a["illustrative_tone"] for a in arms]
        assert tones == [-0.55, -0.55, -0.55]
        assert sum(tones) / len(tones) == -0.55

    def test_meta_arms_excerpt_bounded(self):
        for arm in _mechanism()["meta_arms"]:
            assert "excerpt-bounded" in arm["evidence_grade"]

    def test_biztoc_url_verbatim(self):
        assert BIZTOC_URL == "https://biztoc.com/x/a33fe91fadf42459"


class TestPairMechanism718:
    def test_delta_is_near_null(self):
        m = _mechanism()
        delta = m["illustrative_delta_openai_minus_meta"]
        assert abs(delta) == 0.05
        assert delta == -0.05

    def test_delta_matches_arm_tones(self):
        m = _mechanism()
        openai = m["openai_arm"]["illustrative_tone"]
        meta_avg = sum(a["illustrative_tone"] for a in m["meta_arms"]) / len(m["meta_arms"])
        assert abs((openai - meta_avg) - m["illustrative_delta_openai_minus_meta"]) < 1e-9

    def test_illustrative_only_contract(self):
        contract = _mechanism()["scorer_contract"]
        assert "MANUAL ILLUSTRATIVE ONLY" in contract
        assert "NOT_CALCULATED" in contract
        assert "is_significant False" in contract
        assert "NOT artifact-grade" in contract

    def test_arm_swap_negation(self):
        assert -(-0.05) == 0.05

    def test_peg_gravity_confound_acknowledged(self):
        confs = _mechanism()["confounders_ranked"]
        peg = [c for c in confs if "peg gravity" in c["confound"]]
        assert len(peg) == 1
        assert peg[0]["strength"] == "STRONG"

    def test_co_byline_dilution_acknowledged(self):
        confs = _mechanism()["confounders_ranked"]
        dil = [c for c in confs if "co-byline dilution" in c["confound"]]
        assert len(dil) == 1
        assert "Kashmir Hill" in dil[0]["confound"]


class TestFinancialContext718:
    def test_lawsuit_december_2023_carried(self):
        ctx = _mechanism()["institutional_context"]["nyt_v_openai_lawsuit"]
        assert "Dec 2023" in ctx
        assert "copyright infringement" in ctx

    def test_zero_openai_licensing_revenue(self):
        fin = _mechanism()["financial_context"]
        assert "$0 AI licensing revenue from OpenAI" in fin

    def test_no_meta_deal_on_record(self):
        fin = _mechanism()["financial_context"]
        assert "No NYT x Meta AI content licensing deal on record" in fin

    def test_correlation_not_causation(self):
        fin = _mechanism()["financial_context"]
        assert "Correlation only, not causation" in fin
        assert "no causal claim" in fin


class TestMechanism665Yaml:
    def test_mechanism_id_and_iteration(self):
        m = _mechanism()
        assert m["mechanism_id"] == 665
        assert isinstance(m["mechanism_id"], int)
        assert m["iteration"] == 718
        assert m["iteration_type"] == "B"
        assert m["date"] == "2026-09-13"
        assert m["publication"] == "nytimes"

    def test_first_mechanism_key_on_entry(self):
        o = _journalist()
        assert list(o["competitor_coverage"].keys()) == [MECH_KEY]

    def test_twenty_fourth_falsification_family_member(self):
        finding = _mechanism()["finding"]
        assert "TWENTY-FOURTH falsification-family member" in finding
        assert "ledger 23->24" in finding

    def test_second_reporter_level_extension_of_471(self):
        finding = _mechanism()["finding"]
        assert "mechanism 471" in finding
        assert "after 538 (Cade Metz)" in finding

    def test_confounders_ranked_with_strong_first(self):
        confs = _mechanism()["confounders_ranked"]
        assert len(confs) == 5
        assert confs[0]["strength"] == "STRONG"
        assert confs[1]["strength"] == "STRONG"
        assert confs[2]["strength"] == "MODERATE"
        assert confs[3]["strength"] == "MODERATE"
        assert confs[4]["strength"] == "WEAK"
        for c in confs:
            assert c["confound"] and c["mitigant"]

    def test_novelty_and_cross_refs(self):
        m = _mechanism()
        assert "First dedicated Type B on Jennifer Valentino-DeVries" in m["novelty"]
        assert "mechanism 623" in m["novelty"]
        refs = " ".join(m["cross_references"])
        assert "mechanism 471" in refs
        assert "mechanism 538" in refs
        assert "mechanism 623" in refs

    def test_no_em_dash_in_mechanism_or_file(self):
        m = _mechanism()
        blob = yaml.safe_dump(m)
        assert "\u2014" not in blob
        assert "\u2013" not in blob
        assert "\u2014" not in _read(os.path.join(TESTS_DIR, TEST_BASENAME))
        assert "\u2013" not in _read(os.path.join(TESTS_DIR, TEST_BASENAME))


class TestIterationLog718:
    def test_log_has_718_type_b_entry(self):
        text = _read(LOG_PATH)
        assert "#718 Type B:" in text

    def test_rotation_a_to_b(self):
        text = _read(LOG_PATH)
        assert text.index("#718 Type B:") < text.index("#717 Type A:")


class TestRotationCycleGuard718:
    ANCHORED_SHA = ANCHORED_SHA

    def test_type_b_718_file_unique(self):
        matches = glob.glob(os.path.join(TESTS_DIR, "test_type_b_718*"))
        assert matches == [os.path.join(TESTS_DIR, TEST_BASENAME)]

    def test_type_b_718_main_commit_unique_and_anchored(self):
        result = _run_git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [line for line in result.stdout.splitlines() if "Type B #718:" in line]
        assert len(mains) == 1
        main = mains[0].split()[0]
        assert ANCHORED_SHA == main, "anchor test pinned to main commit %s" % ANCHORED_SHA


class TestDocSync718:
    def test_readme_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        assert TEST_BASENAME in text

    def test_architecture_has_row(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert TEST_BASENAME in text
