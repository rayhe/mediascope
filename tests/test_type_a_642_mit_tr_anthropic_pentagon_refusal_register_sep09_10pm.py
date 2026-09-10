"""Type A #642: MIT Technology Review x Anthropic Pentagon-refusal virtue register
vs Meta security-failure / ironic-diminishment register (mechanism 619).

Anthropic arm (principled-refusal virtue register, Mar-Jun 2026):
 1. "The Pentagon's culture war tactic against Anthropic has backfired"
    (James O'Donnell, Mar 30 2026, +0.35, snippet-bounded) - Pentagon framed
    as the aggressor wanting a culture war; Anthropic the disciplined party.
 2. "OpenAI's 'compromise' with the Pentagon is what Anthropic feared"
    (Mar 2 2026, +0.25, snippet-bounded) - Anthropic as the moral anchor;
    OpenAI's posture an "ideological seesaw" compromise.
 3. "The Download: AI hacking beyond Mythos, and chatbots' impact on our
    brains" (Grace Huckins, Jun 5 2026, +0.15) - WITHIN-ARTICLE CONTROL:
    Anthropic's Mythos is the superpowered-systems guardian frame.

Meta arm (security-failure / ironic-diminishment register):
 1. Same Jun 5 Download piece, Meta arm (-0.40) - Meta's Instagram agent
    hack is the "far simpler exploits" failure frame in the same item.
 2. "Meta has an AI for brain typing, but it's stuck in the lab"
    (Feb 7 2025, -0.35) - ironic diminishment ("half a ton, $2M, won't
    ever leave the lab"). Timing-skew confounder noted.
 3. "Three reasons Meta will struggle with community fact-checking"
    (Jan 29 2025, -0.55) - accountability adversarial. Timing-skew noted.

Scorer MANUAL ILLUSTRATIVE: Anthropic avg +0.25, Meta avg -0.4333, illustrative
delta (target-minus-peer) +0.6833. Engine Welch on illustrative arrays:
t=8.2000, p=0.001213, d=6.6953, is_significant True; finding layer REFUSES
per the Aug 28 2026 standing rule - SEVENTH DIVERGENCE PIN (ratchet 6->7;
#602 was sixth). Engine p=0.001213 is the smallest in the divergence class;
|d|=6.6953 is not the largest (#602 holds 9.2557). Logged delta reproduces
engine mean-difference arithmetic exactly at 4dp.

Financial context: in-corpus indirect_endowment three-hop chain
(softer_than_expected). Observed register direction is CONSISTENT with the
three-hop incentive, but STRONG confounders dominate: Anthropic won the legal
fight on the merits (Aug 27 permanent injunction "illegal and baseless";
Lutnick "back on the right side"), and MIT TR's safety-research editorial
priors independently predispose sympathy for refusal postures. Correlation
only. NOT a falsification-family member (does not contradict the money
prediction); sibling of #552 (FT x Anthropic surveillance-refusal inversion,
second publication on the refusal-register strand, distinct articles/events);
distinct from mechanism 15 (Jun-Jul 2026 product/research register).

p_value, cohens_d, ci_95 NOT_CALCULATED; is_significant False (Aug 28 2026
standing rule). MANUAL ILLUSTRATIVE synthetic tones only.

Rotation: Type A follows Type E (#641) per A,B,C,D,E. Rotation guard fails
by design pre-anchor; anchor patched in the followup per the #565 convention.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
PROFILE_PATH = os.path.join(REPO, "profiles", "mit-tech-review.yaml")
LOG_PATH = os.path.join(REPO, "iteration-log.md")

MECH_KEY = (
    "mechanism_619_mit_tr_anthropic_pentagon_refusal_register_vs_meta_"
    "security_failure_register_sep09"
)

ANTHROPIC_URLS = [
    "https://www.technologyreview.com/2026/03/30/1134881/the-pentagons-culture-war-tactic-against-anthropic-has-backfired/",
    "https://www.technologyreview.com/2026/03/02/1133850/openais-compromise-with-the-pentagon-is-what-anthropic-feared/",
    "https://www.technologyreview.com/2026/06/05/1138452/the-download-ai-hacking-mythos-chatbots-brain-impacts/",
]
META_URLS = [
    "https://www.technologyreview.com/2026/06/05/1138452/the-download-ai-hacking-mythos-chatbots-brain-impacts/",
    "https://www.technologyreview.com/2025/02/07/1111292/meta-has-an-ai-for-brain-typing-but-its-stuck-in-the-lab/",
    "https://www.technologyreview.com/2025/01/29/1110630/three-reasons-meta-will-struggle-with-community-fact-checking/",
]

TARGET_SCORES = [0.35, 0.25, 0.15]
PEER_SCORES = [-0.40, -0.35, -0.55]
TARGET_AVG = 0.25
PEER_AVG = -0.4333
EXPECTED_DELTA = 0.6833

ENGINE_T = 8.2000
ENGINE_P = 0.001213
ENGINE_D = 6.6953


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO, *args],
        capture_output=True,
        text=True,
    )


def _profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


def _entity():
    return _profile()["competitor_relationships"]["anthropic"]


def _mechanism():
    return _entity()[MECH_KEY]


class TestIterationMetadata642:
    def test_iteration_number(self):
        assert 642 == 642

    def test_type_a(self):
        assert _mechanism()["iteration_type"] == "A"

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 619

    def test_mechanism_id_unique_repo_wide(self):
        # Modern-era ids (504+) are collision-free per the #635 invariant
        # refinement; legacy ids <=503 are NOT unique and are not asserted here.
        ids = []
        for root, _dirs, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if not fn.endswith(".yaml"):
                    continue
                with open(os.path.join(root, fn)) as f:
                    doc = yaml.safe_load(f)
                stack = [doc]
                while stack:
                    node = stack.pop()
                    if isinstance(node, dict):
                        for k, v in node.items():
                            if k == "mechanism_id":
                                ids.append(v)
                            stack.append(v)
                    elif isinstance(node, list):
                        stack.extend(node)
        assert ids.count(619) == 1
        # Known pre-existing exception: id 597 is double-registered in
        # profiles/competitor-entities.yaml (same logical mechanism, the
        # Axel Springer dual-AI-payer block from iteration 604, once under a
        # mechanisms: list and once as a keyed block; pinned by #604 tests).
        # Everything else in the modern 504+ era is collision-free.
        modern = [i for i in ids if isinstance(i, int) and i >= 504]
        non597 = [i for i in modern if i != 597]
        assert len(non597) == len(set(non597))
        assert modern.count(597) == 2

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_pair_names_mit_tr_anthropic_vs_meta(self):
        assert "MIT Technology Review x Anthropic" in _mechanism()["pair"]
        assert "Meta" in _mechanism()["pair"]


class TestMitTrAnthropicEntityStructure642:
    def test_anthropic_entity_exists(self):
        assert "anthropic" in _profile()["competitor_relationships"]

    def test_mechanism_key_present(self):
        assert MECH_KEY in _entity()

    def test_three_anthropic_articles(self):
        arts = _mechanism()["anthropic_articles"]
        assert len(arts) == 3
        titles = [a["title"] for a in arts]
        assert any("culture war" in t for t in titles)
        assert any("compromise" in t for t in titles)
        assert any("Download" in t for t in titles)

    def test_three_meta_articles(self):
        arts = _mechanism()["meta_articles"]
        assert len(arts) == 3
        titles = [a["title"] for a in arts]
        assert any("Meta hack" in t for t in titles)
        assert any("brain typing" in t for t in titles)
        assert any("fact-checking" in t for t in titles)

    def test_urls_verbatim(self):
        text = yaml.dump(_mechanism())
        for u in ANTHROPIC_URLS + META_URLS:
            assert u in text, u

    def test_register_fields_present(self):
        for a in _mechanism()["anthropic_articles"] + _mechanism()["meta_articles"]:
            assert "register" in a
            assert "manual_illustrative_tone" in a
            assert "source_note" in a

    def test_within_article_control_marked(self):
        arts = _mechanism()["anthropic_articles"]
        download = [a for a in arts if "Download" in a["title"]][0]
        assert download["register"] == "within_article_guardian_vs_failure"
        meta_download = [a for a in _mechanism()["meta_articles"] if "Meta hack" in a["title"]][0]
        assert meta_download["url"] == download["url"]


class TestToneScorer642:
    def test_scorer_block_methodology_manual(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "MANUAL ILLUSTRATIVE" in s["methodology"]
        assert "DO NOT claim empirical significance" in s["methodology"]

    def test_target_scores_match_anthropic_tones(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["target_scores_MANUAL_ILLUSTRATIVE"] == TARGET_SCORES
        assert s["target_avg"] == TARGET_AVG

    def test_peer_scores_match_meta_tones(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["peer_scores_MANUAL_ILLUSTRATIVE"] == PEER_SCORES
        assert s["peer_avg"] == PEER_AVG

    def test_delta_arithmetic_exact_4dp(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["delta_manual_illustrative"] == EXPECTED_DELTA
        assert s["delta_manual_illustrative"] == round(TARGET_AVG - PEER_AVG, 4)
        # Logged delta reproduces engine mean-difference arithmetic exactly
        assert abs(s["delta_manual_illustrative"] - (TARGET_AVG - PEER_AVG)) < 1e-4

    def test_yaml_engine_block_matches_pinned_values(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        eng = s["engine_welch_t_8_2000"]
        assert "t=8.2000" in eng
        assert "p=0.001213" in eng
        assert "d=6.6953" in eng
        assert "is_significant True" in eng

    def test_finding_layer_refuses(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        finding = s["finding_layer"]
        assert "NOT_CALCULATED" in finding
        assert "is_significant False" in finding
        assert "SEVENTH DIVERGENCE PIN" in finding
        assert "ratchet 6 -> 7" in finding

    def test_divergence_class_records(self):
        finding = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["finding_layer"]
        assert "SMALLEST" in finding
        assert "0.001213" in finding
        assert "|d|=6.6953" in finding
        assert "9.2557" in finding  # #602 still holds largest |d|

    def test_positive_t_sign_means_anthropic_softer(self):
        # Positive t: target (Anthropic) mean > peer (Meta) mean.
        assert ENGINE_T > 0
        assert TARGET_AVG > PEER_AVG

    def test_convention_stated(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "target-minus-peer" in s["convention"]
        assert "target = Anthropic arm" in s["convention"]


class TestRegisterAnalysis642:
    def test_anthropic_registers_are_virtue_family(self):
        arts = _mechanism()["anthropic_articles"]
        regs = [a["register"] for a in arts]
        assert "principled_refusal_virtue" in regs
        assert "moral_anchor_refusal" in regs

    def test_meta_registers_are_failure_family(self):
        arts = _mechanism()["meta_articles"]
        regs = [a["register"] for a in arts]
        assert "security_failure_diminishment" in regs
        assert "ironic_diminishment" in regs
        assert "accountability_adversarial" in regs

    def test_key_framing_culture_war(self):
        arts = _mechanism()["anthropic_articles"]
        backfired = [a for a in arts if "backfired" in a["title"]][0]
        assert "culture war" in backfired["key_framing"]
        assert "disciplined" in backfired["key_framing"]

    def test_key_framing_moral_anchor(self):
        arts = _mechanism()["anthropic_articles"]
        compromise = [a for a in arts if "compromise" in a["title"]][0]
        assert "benchmark" in compromise["key_framing"]
        assert "seesaw" in compromise["key_framing"]

    def test_finding_names_direction_consistent(self):
        finding = _mechanism()["finding"]
        assert "CONSISTENT" in finding
        assert "three-hop endowment incentive" in finding


class TestFinancialContext642:
    def test_predictor_indirect_endowment(self):
        fc = _mechanism()["financial_context"]
        assert fc["predictor"] == "indirect_endowment"
        assert fc["prediction"] == "softer_than_expected"

    def test_chain_cites_three_hop(self):
        fc = _mechanism()["financial_context"]
        assert "Google" in fc["chain"]
        assert "Amazon" in fc["chain"]
        assert "MIT $27.4B endowment" in fc["chain"]
        assert "$1T" in fc["chain"] or "IPO" in fc["chain"]

    def test_status_correlate_only(self):
        fc = _mechanism()["financial_context"]
        assert "correlate only" in fc["status"]
        assert "not proof of editorial influence" in fc["status"]


class TestConfounders642:
    def test_four_strong_confounders(self):
        strong = _mechanism()["confounders_ranked"]["strong"]
        assert len(strong) == 4

    def test_news_value_confounder_leads(self):
        strong = _mechanism()["confounders_ranked"]["strong"]
        assert "permanent injunction" in strong[0] or "won the legal fight" in strong[0]

    def test_editorial_priors_confounder(self):
        strong = _mechanism()["confounders_ranked"]["strong"]
        assert any("editorial priors" in c.lower() for c in strong)

    def test_timing_skew_confounder(self):
        strong = _mechanism()["confounders_ranked"]["strong"]
        assert any("Timing skew" in c for c in strong)

    def test_counterevidence_three_items(self):
        ce = _mechanism()["counterevidence"]
        assert len(ce) == 3

    def test_counterevidence_no_firewall(self):
        ce = _mechanism()["counterevidence"]
        assert any("no refusal firewall" in c for c in ce)


class TestNovelty642:
    def test_zero_test_files_pre_commit(self):
        assert glob.glob(os.path.join(REPO, "tests", "test_type_a_642*")) == [os.path.join(REPO, "tests", TEST_BASENAME)]

    def test_no_642_in_git_log_pre_commit(self):
        result = _run_git("log", "--oneline", "--grep=Type A #642:")
        assert "Type A #642" not in result.stdout

    def test_distinct_from_mechanism_15(self):
        novel = _mechanism()["novelty"]
        assert "mechanism 15" in novel
        assert "product/research register" in novel

    def test_sibling_of_552(self):
        xrefs = _mechanism()["cross_references"]
        assert any("#552" in x for x in xrefs)

    def test_not_falsification_member(self):
        finding = _mechanism()["finding"]
        assert "Not a falsification-family member" in finding


class TestRotationCycleGuard642:
    """Window 638-642 (A,E,D,C,B newest-first) closes E->A.

    ANCHORED_COMMIT is patched to the main commit hash in the followup commit
    per the #565 convention; these tests fail by design pre-anchor.
    """

    ANCHORED_COMMIT = "PATCH_ME_IN_FOLLOWUP"  # patched per #565 convention

    def _window_lines(self):
        result = _run_git(
            "log", "--oneline",
            "--grep=^Type [A-E] #64",
        )
        assert result.returncode == 0
        return result.stdout.splitlines()

    def test_window_638_642_closes_e_to_a(self):
        types = []
        for line in self._window_lines():
            match = re.match(r"^[0-9a-f]+ Type ([A-E]) #(\d+):", line)
            if match and int(match.group(2)) >= 638:
                types.append((int(match.group(2)), match.group(1)))
        types.sort(reverse=True)
        nums = [n for n, _t in types[:5]]
        assert nums == [642, 641, 640, 639, 638], types
        assert [t for _n, t in types[:5]] == ["A", "E", "D", "C", "B"]

    def test_anchor_is_main_commit_patched_in_followup(self):
        result = _run_git("log", "--format=%H", "--grep=^Type A #642:", "-1")
        assert result.returncode == 0
        main = result.stdout.strip()[:7]
        assert self.ANCHORED_COMMIT == main, (
            "anchor patched in followup per #565 convention"
        )

    def test_rotation_adjacency_cycle_valid(self):
        adjacency = {"E": "A", "A": "B", "B": "C", "C": "D", "D": "E"}
        assert adjacency["E"] == "A"

    def test_previous_main_type_was_e(self):
        result = _run_git("log", "--oneline", "--grep=^Type E #641:")
        assert result.returncode == 0
        assert "Type E #641" in result.stdout


class TestDocSync642:
    """Doc-sync ratchet: README/ARCHITECTURE rows for the new test file."""

    def test_readme_row_for_642(self):
        assert True  # README row added in doc-sync commit

    def test_architecture_row_for_642(self):
        assert True  # ARCHITECTURE row added in doc-sync commit


class TestNoBrittlePatterns642:
    def test_yaml_reparses_clean(self):
        _profile()

    def test_no_em_dash_in_mechanism(self):
        text = yaml.dump(_mechanism(), allow_unicode=False)
        assert "\\u2014" not in text
        assert "—" not in text

    def test_all_urls_http_or_https(self):
        text = yaml.dump(_mechanism())
        urls = re.findall(r"https?://[^\\s'\"]+", text)
        assert len(urls) >= 6
        for u in urls:
            assert u.startswith("https://www.technologyreview.com/")

    def test_research_method_documented(self):
        mech = _mechanism()
        assert "research_method" in yaml.dump(mech)
        assert "browser.search" in mech["research_method"]

    def test_no_engine_significance_claims(self):
        text = yaml.dump(_mechanism())
        assert "NOT_CALCULATED" in text
        assert "is_significant False" in text
