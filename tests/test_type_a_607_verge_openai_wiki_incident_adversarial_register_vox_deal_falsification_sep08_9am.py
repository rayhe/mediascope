"""
Type A #607 - Competitor Coverage Deep Dive: The Verge x OpenAI wiki-incident
adversarial register - Vox-deal falsification at the incident-coverage layer
- Sep 8 2026 09:00 PDT

The Verge ran an adversarial delayed-disclosure register on the OpenAI
DseWiki "wiki incident" (Sep 4-6 2026) despite the Vox Media-OpenAI content
licensing deal (May 2024, in-corpus) predicting "softer" coverage. Original
headline: "OpenAI Kept DseWiki Agent Breakout Under Wraps for Weeks During
Hugging Face Fallout" (verbatim via aiweekly.co); canonical URL carried
verbatim from webpronews ("The Verge first covered the admission"):
https://www.theverge.com/ai-artificial-intelligence/990773/openai-german-wiki-incident
theverge.com is policy-blocked for browser.open per standing rule, so
verification is second-hand and excerpt-bounded, same as #507.

MANUAL ILLUSTRATIVE, NOT empirical (standing rule Aug 28 2026).
OpenAI arm (n=1): [-0.65] vs Meta comparator arms (carried #592):
[-0.55, -0.6, -0.5], avg -0.55. Illustrative delta (OpenAI minus Meta):
-0.10 - the deal PARTNER is covered marginally MORE adversarially than the
$0-tie baseline. Engine on illustrative arms: welch_t_test returns
(0.0, 1.0) - the #603-pinned degenerate guard fires on the n=1 arm;
cohens_d computes -2.0 (rounded), the asymmetric n=1 vs n=3 variant
mirroring #593. Finding layer refuses: p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False. NOT an agreement-pole pin: the pole
requires a non-degenerate engine computation.

Falsification family moves 8 -> 9: #607 joins
#538, #563, #568, #578, #583, #588, #599, #604, #607. Second Vox-deal
falsification instance (first: #573 Nilay Patel interview-access layer);
#507 is the ad-monetization domain boundary, not a family member.
Correlation is not causation; n=1 vs n=3 is directional, not dispositive.
"""
import glob
import os
import re
import subprocess

import pytest
import yaml

from mediascope.score.statistical import welch_t_test, cohens_d

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERGE_PATH = os.path.join(REPO_ROOT, "profiles", "the-verge.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

MECH_KEY = "mechanism_598_verge_openai_wiki_incident_adversarial_register_vox_deal_falsification_sep08"
OPENAI_TONES = [-0.65]
META_TONES = [-0.55, -0.6, -0.5]  # carried from #592 same-outlet set
OPENAI_AVG = -0.65
META_AVG = -0.55
DELTA = -0.10  # openai_avg - meta_avg
VERGE_WIKI_URL = "https://www.theverge.com/ai-artificial-intelligence/990773/openai-german-wiki-incident"
VERGE_WIKI_HEADLINE = "OpenAI Kept DseWiki Agent Breakout Under Wraps for Weeks During Hugging Face Fallout"
FAMILY_NINE = "#538, #563, #568, #578, #583, #588, #599, #604, #607"


def _verge():
    with open(VERGE_PATH) as f:
        return yaml.safe_load(f)


def _mechanism():
    return _verge()["competitor_relationships"]["openai"][MECH_KEY]


def read_readme():
    with open(README_PATH) as f:
        return f.read()


def read_arch():
    with open(ARCH_PATH) as f:
        return f.read()


class TestIterationMetadata607:
    def test_mechanism_id_is_598_next_free_numeric(self):
        assert _mechanism()["mechanism_id"] == 598

    def test_iteration_number_is_607(self):
        assert _mechanism()["iteration"] == 607

    def test_iteration_type_is_a(self):
        assert _mechanism()["iteration_type"] == "A"

    def test_publication_focus_is_the_verge(self):
        assert _mechanism()["publication_focus"] == "The Verge"

    def test_entity_pair_openai_vs_meta(self):
        assert _mechanism()["entity_pair"] == "OpenAI vs Meta"

    def test_falsification_family_mentioned(self):
        assert "falsification" in _mechanism()["falsification_family"].lower()

    def test_scheduled_job_id(self):
        assert _mechanism()["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_goal_id(self):
        assert _mechanism()["goal_id"] == "goal_54093bda4145"


class TestWikiIncidentArticle607:
    def _openai_article(self):
        arts = [a for a in _mechanism()["articles"] if a["entity"] == "openai"]
        assert len(arts) == 1
        return arts[0]

    def test_exactly_one_openai_article(self):
        self._openai_article()

    def test_url_verbatim_not_constructed(self):
        assert self._openai_article()["url"] == VERGE_WIKI_URL

    def test_headline_verbatim(self):
        assert self._openai_article()["title"] == VERGE_WIKI_HEADLINE

    def test_tone_is_minus_065(self):
        assert self._openai_article()["manual_illustrative_tone"] == -0.65

    def test_register_adversarial_delayed_disclosure(self):
        assert "adversarial" in self._openai_article()["register"]

    def test_url_note_names_policy_block(self):
        assert "policy-blocked" in self._openai_article()["url_note"]

    def test_verification_is_second_hand(self):
        assert "second-hand" in self._openai_article()["verification"]

    def test_key_phrases_carry_delayed_disclosure(self):
        phrases = " ".join(self._openai_article()["key_phrases"])
        assert "under wraps for weeks" in phrases

    def test_date_in_september_2026_window(self):
        assert self._openai_article()["date"].startswith("2026-09")


class TestMetaComparatorCarried592:
    def _meta_articles(self):
        return [a for a in _mechanism()["articles"] if a["entity"] == "meta"]

    def test_three_meta_articles(self):
        assert len(self._meta_articles()) == 3

    def test_meta_tones_match_592_arms(self):
        tones = [a["manual_illustrative_tone"] for a in self._meta_articles()]
        assert tones == META_TONES

    def test_meta_avg_minus_055(self):
        tones = [a["manual_illustrative_tone"] for a in self._meta_articles()]
        assert round(sum(tones) / len(tones), 2) == META_AVG

    def test_all_carried_from_592(self):
        for a in self._meta_articles():
            assert "592" in a["carried_from"]

    def test_all_meta_tones_adversarial(self):
        for a in self._meta_articles():
            assert a["manual_illustrative_tone"] <= -0.5


class TestVoxDealFinancialTie607:
    def _openai_entity(self):
        return _verge()["competitor_relationships"]["openai"]

    def test_financial_tie_is_licensing(self):
        assert self._openai_entity()["financial_tie"] == "licensing"

    def test_coverage_prediction_softer(self):
        assert self._openai_entity()["coverage_prediction"] == "softer"

    def test_direction_receiving(self):
        assert self._openai_entity()["direction"] == "receiving"

    def test_venturebeat_source_url_present(self):
        assert "venturebeat.com" in self._openai_entity()["source_url"]

    def test_mechanism_507_preexists(self):
        ent = self._openai_entity()
        assert "mechanism_507_verge_openai_ad_monetization_register_boundary_condition" in ent

    def test_falsification_claims_softer_prediction(self):
        assert 'predicting "softer" coverage' in _mechanism()["discovery_summary"]


class TestScorerReproduction607:
    def test_delta_minus_010(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["asymmetry_score"] == DELTA

    def test_delta_reproduces_mean_difference(self):
        computed = round(OPENAI_AVG - META_AVG, 2)
        assert computed == DELTA

    def test_score_direction_openai_minus_meta(self):
        assert _mechanism()["asymmetry_scorer_result"]["score_direction"] == "openai_minus_meta"

    def test_engine_welch_degenerate_on_n1_arm(self):
        t, p = welch_t_test(OPENAI_TONES, META_TONES)
        assert (t, p) == (0.0, 1.0)

    def test_engine_cohens_d_computes_minus_two(self):
        d = cohens_d(OPENAI_TONES, META_TONES)
        assert abs(d - (-2.0)) < 1e-9

    def test_engine_matches_yaml_drift_note(self):
        note = _mechanism()["asymmetry_scorer_result"]["engine_drift_check"]
        assert "(0.0, 1.0)" in note
        assert "-2.0" in note

    def test_p_value_not_calculated(self):
        assert _mechanism()["asymmetry_scorer_result"]["p_value"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert _mechanism()["asymmetry_scorer_result"]["is_significant"] is False

    def test_method_manual_illustrative(self):
        assert _mechanism()["asymmetry_scorer_result"]["method"] == "manual_illustrative"

    def test_statistical_discipline_standing_rule(self):
        disc = _mechanism()["statistical_discipline"]
        assert "NOT_CALCULATED" in disc
        assert "correlation_not_causation" in disc

    def test_not_an_agreement_pole_pin(self):
        # The agreement pole requires a non-degenerate engine computation;
        # the degenerate guard fires on the n=1 arm, so this is a
        # degenerate-boundary agreement, not a pole pin. Agreement pole
        # stays at 11.
        t, p = welch_t_test(OPENAI_TONES, META_TONES)
        assert (t, p) == (0.0, 1.0)
        assert "NOT" in _mechanism()["finding"] and "agreement-pole pin" in _mechanism()["finding"]

    def test_divergence_ratchet_untouched(self):
        # No divergence pin here: the t-path is degenerate (0.0, 1.0) and
        # the finding layer refuses, so engine and finding agree on
        # non-significance at the degenerate boundary. Divergence ratchet
        # stays at 6; agreement pole stays at 11 (not a pole pin).
        t, p = welch_t_test(OPENAI_TONES, META_TONES)
        assert (t, p) == (0.0, 1.0)
        assert "SIXTH DIVERGENCE" not in __doc__


class TestFalsificationFamilyNine:
    def test_family_moves_8_to_9(self):
        assert "Falsification family moves 8 -> 9" in __doc__

    def test_nine_member_list(self):
        assert FAMILY_NINE in __doc__
        assert FAMILY_NINE in _mechanism()["falsification_family"]

    def test_mechanism_mentions_falsification_family(self):
        import json
        assert "falsification" in json.dumps(_mechanism()).lower()

    def test_second_vox_deal_instance_after_573(self):
        assert "#573" in __doc__
        assert "interview-access" in __doc__

    def test_507_is_boundary_not_member(self):
        assert "ad-monetization domain boundary" in __doc__

    def test_related_498_distinct(self):
        assert "#498" in _mechanism()["falsification_family"]


class TestNoBrittlePatterns607:
    def test_exactly_one_607_file(self):
        files = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_a_607_*.py")
        )
        assert len(files) == 1

    def test_no_duplicate_mechanism_598_keys(self):
        count = 0
        for root, _, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    with open(os.path.join(root, fn)) as f:
                        count += f.read().count("mechanism_598_verge_openai")
        assert count == 1, f"mechanism_598 key appears {count} times"

    def test_no_absolute_zero_coverage_claim(self):
        # iteration-492 rule: absence claims are bounded to search-result
        # sets; the mechanism must not assert absolute zero coverage.
        text = _mechanism()["research_method"]
        assert "no zero-coverage claims" in text

    def test_peer_context_has_deal_absent_outlets(self):
        peers = _mechanism()["peer_context"]
        assert any(p["financial_tie"] == "none" for p in peers)

    def test_gizmodo_peer_url_verbatim(self):
        peers = _mechanism()["peer_context"]
        giz = next(p for p in peers if p["outlet"] == "Gizmodo")
        assert giz["url"] == (
            "https://gizmodo.com/another-rogue-openai-agent-swarm-went-undisclosed-"
            "we-have-no-idea-how-many-more-are-out-there-2000807447"
        )

    def test_source_urls_all_http(self):
        for u in _mechanism()["source_urls"]:
            assert u.startswith("http"), f"non-http source URL: {u!r}"


class TestRotationCycleGuard607:
    """Rotation guard, deselected pre-commit per the #565 followup convention.

    Asserts the post-commit anchor, so it runs green only in the followup
    commit after the main commit SHA is known. Pre-commit it is deselected.
    """

    def _mains(self):
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]
        assert len(mains) >= 5
        return mains

    def test_window_603_607_closes_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "607"),
            ("E", "606"),
            ("D", "605"),
            ("C", "604"),
            ("B", "603"),
        ], f"rotation window 603-607 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["A", "E", "D", "C", "B"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_536be32(self):
        # Post-commit anchor: the #607 main commit. Patched in the followup
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
        assert sha.startswith("536be32"), f"anchor drifted: {sha}"
        assert subject.startswith("Type A #607:"), (
            f"post-commit anchor broken: newest main is not #607: {subject!r}"
        )


class TestDocSyncRatchet607:
    def test_readme_row_for_607(self):
        readme = read_readme()
        assert re.search(r"#607", readme), "README.md missing the #607 test-table row"

    def test_arch_row_for_607(self):
        arch = read_arch()
        assert re.search(r"#607", arch), "docs/ARCHITECTURE.md missing the #607 tree row"

    def test_606_row_survives_in_readme(self):
        readme = read_readme()
        assert re.search(r"#606", readme), "README.md lost the #606 row"

    def test_606_row_survives_in_arch(self):
        arch = read_arch()
        assert re.search(r"#606", arch), "docs/ARCHITECTURE.md lost the #606 row"

    def test_readme_row_carries_correct_test_count(self):
        readme = read_readme()
        m = re.search(
            r"`test_type_a_607_verge_openai_wiki_incident_adversarial_register_vox_deal_falsification_sep08_9am\.py` \| (\d+)",
            readme,
        )
        assert m, "README #607 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )


def _count_def_tests():
    import ast
    path = os.path.join(
        REPO_ROOT,
        "tests",
        "test_type_a_607_verge_openai_wiki_incident_adversarial_register_vox_deal_falsification_sep08_9am.py",
    )
    tree = ast.parse(open(path).read())
    return sum(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name.startswith("test_")
        for n in ast.walk(tree)
    )
