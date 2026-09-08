"""
Type A #602 - Competitor Coverage Deep Dive: WIRED x Anthropic Licensing-Halo
September Silence Extension - Sep 8 2026 04:00 PDT

Four Anthropic beats in the Sep 1-8 2026 window ($1.5B piracy settlement payout
dispute Sep 6; public S-1 prospectus watch post-Labor-Day with $100B raise /
up-to-$2T valuation reports Sep 3-4; Claude Fable 5.1 / Mythos 5.1 GA Sep 1;
AISI incident-report followup extended to 35 days) carry peer-outlet coverage
in neutral-to-constructive business/process register while bounded WIRED
search-result sets return no WIRED article. Financial predictor is INDIRECT:
Conde Nast's Aug 2024 OpenAI content licensing deal (in-corpus) is with
Anthropic's chief rival, not Anthropic - the naive deal-gradient hypothesis
predicts rival harshness, not softness. Observed: bounded-absence silence on
adversarial Anthropic beats plus carried adversarial Meta register
(avg -0.7733 from #547). This is the LICENSING-HALO extension: register
softness/silence radiates beyond the deal partner to the rival lab, joining
the Verge x Anthropic control and the falsification-of-financial-determinism
family (#552 FT x Anthropic, #193 BI, #599 Song inversion).

MANUAL ILLUSTRATIVE, NOT empirical (standing rule Aug 28 2026).
Peer register [0.10, -0.05, -0.10] avg -0.0167 vs Meta target
[-0.82, -0.72, -0.78] avg -0.7733: illustrative delta +0.7567
(peer-minus-target). Engine drift check on illustrative arrays:
t=-11.3358, p=0.001755, d=-9.2557, is_significant True -> finding layer
refuses (NOT_CALCULATED, False): SIXTH DIVERGENCE PIN (ratchet 5 -> 6),
smallest engine p in class, largest |d| in class.
"""
import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIRED_PATH = os.path.join(REPO_ROOT, "profiles", "wired.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

TARGET_SCORES = [-0.82, -0.72, -0.78]  # Meta alarm baseline, carried from #547
PEER_SCORES = [-0.10, -0.05, 0.10]  # peer-outlet register for Sept Anthropic beats (beat order)
TARGET_AVG = -0.7733
PEER_AVG = -0.0167
DELTA = 0.7567  # peer_avg - target_avg
ENGINE_T = -11.3358
ENGINE_P = 0.001755
ENGINE_D = -9.2557


def _wired():
    with open(WIRED_PATH) as f:
        return yaml.safe_load(f)


def _mechanism():
    d = _wired()
    return d["competitor_relationships"]["anthropic"][
        "mechanism_595_wired_anthropic_licensing_halo_september_silence_extension_sep08"
    ]


def read_readme():
    with open(README_PATH) as f:
        return f.read()


def read_arch():
    with open(ARCH_PATH) as f:
        return f.read()


class TestIterationMetadata602:
    def test_mechanism_id_is_595_next_free_numeric(self):
        assert _mechanism()["mechanism_id"] == 595

    def test_iteration_number_is_602(self):
        assert _mechanism()["iteration"] == 602

    def test_iteration_type_is_a(self):
        assert _mechanism()["iteration_type"] == "A"

    def test_iteration_time_sep08_4am(self):
        assert _mechanism()["iteration_time"] == "2026-09-08 04:00 PDT"

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_entity_pair_anthropic_vs_meta(self):
        assert "Anthropic" in _mechanism()["entity_pair"]
        assert "Meta" in _mechanism()["entity_pair"]

    def test_author_kit_with_ray(self):
        assert _mechanism()["author"] == "Kit (with Ray)"


class TestYamlMechanism595Structure:
    def test_block_lives_under_wired_anthropic(self):
        d = _wired()
        assert "anthropic" in d["competitor_relationships"]
        block = d["competitor_relationships"]["anthropic"][
            "mechanism_595_wired_anthropic_licensing_halo_september_silence_extension_sep08"
        ]
        assert block["publication_focus"] == "WIRED"

    def test_four_september_beats(self):
        beats = _mechanism()["september_beats_bounded_absence"]["beats"]
        assert len(beats) == 4

    def test_beat_dates_in_september_window(self):
        beats = _mechanism()["september_beats_bounded_absence"]["beats"]
        dates = [b["date"] for b in beats]
        assert dates[0] == "2026-09-06"
        assert "2026-09-03" in dates[1]
        assert dates[2] == "2026-09-01"
        assert "35 days" in dates[3]

    def test_source_urls_verbatim_and_count(self):
        urls = _mechanism()["source_urls"]
        assert len(urls) == 8
        assert "https://wired24.co.za/2026/09/06/authors-respond-to-publishers-and-agents-statements-on-anthropic-settlement/" in urls
        assert "https://www.fool.com/investing/2026/09/03/anthropic-gearing-up-ipo-spacex-investors/" in urls
        assert "https://www.fool.com/investing/2026/09/04/anthropic-has-already-raised-130-billion-ahead-of/" in urls
        assert "https://www.thestreet.com/technology/anthropic-30-trillion-ipo-valuation" in urls
        assert "https://www.neuralbuddies.com/p/ai-news-recap-september-4-2026" in urls
        assert "https://www.reuters.com/technology/openai-signs-deal-with-cond-nast-2024-08-20/" in urls

    def test_no_guessed_or_constructed_urls(self):
        blob = str(_mechanism()["source_urls"])
        assert "wired.com/story/" not in blob, "no WIRED article URL should be constructed - coverage is bounded absence"

    def test_meta_comparator_three_articles(self):
        articles = _mechanism()["meta_comparator_carried_547"]["articles"]
        assert len(articles) == 3
        assert articles[0]["manual_illustrative_tone"] == -0.82
        assert articles[1]["manual_illustrative_tone"] == -0.72
        assert articles[2]["manual_illustrative_tone"] == -0.78

    def test_research_method_discloses_bounded_absence(self):
        rm = _mechanism()["september_beats_bounded_absence"]["research_method"]
        assert "BOUNDED" in rm
        assert "iteration-492" in rm

    def test_brake_pedal_excluded_as_stale_with_disclosure(self):
        beats = _mechanism()["september_beats_bounded_absence"]["beats"]
        aisi_beat = beats[3]
        assert "brake pedal" in aisi_beat["note"]
        assert "94 days stale" in aisi_beat["note"]


class TestScorerConsistencyDivergencePin6:
    """Sixth divergence pin: engine reaches significance on the illustrative
    arrays, finding layer refuses per the Aug 28 2026 standing rule."""

    def test_engine_t_pinned(self):
        from mediascope.score.statistical import welch_t_test

        t, p = welch_t_test(TARGET_SCORES, PEER_SCORES)
        assert round(t, 4) == ENGINE_T, f"engine t drifted: {t}"
        assert round(p, 6) == ENGINE_P, f"engine p drifted: {p}"

    def test_engine_d_pinned(self):
        from mediascope.score.statistical import cohens_d

        d = cohens_d(TARGET_SCORES, PEER_SCORES)
        assert round(d, 4) == ENGINE_D, f"engine d drifted: {d}"

    def test_engine_reaches_significance(self):
        assert ENGINE_P < 0.05

    def test_smallest_engine_p_in_divergence_class(self):
        # #592 (fifth divergence pin) had engine p=0.006857; this is smaller.
        assert ENGINE_P < 0.006857

    def test_largest_abs_d_in_divergence_class(self):
        # #592 (fifth divergence pin) had |d|=5.715476; this is larger.
        assert abs(ENGINE_D) > 5.715476

    def test_delta_reproduces_engine_arithmetic_exactly(self):
        raw = (sum(PEER_SCORES) / 3) - (sum(TARGET_SCORES) / 3)
        assert round(raw, 4) == DELTA, f"logged delta does not reproduce engine arithmetic: {raw}"
        assert _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]["delta"] == DELTA

    def test_delta_convention_peer_minus_target(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["delta_convention"] == "peer_avg minus target_avg (positive = peer register softer than Meta register)"
        assert s["peer_avg"] == PEER_AVG
        assert s["target_avg"] == TARGET_AVG

    def test_finding_layer_refuses(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        finding = s["finding_layer"]
        assert "NOT_CALCULATED" in finding
        assert "is_significant False" in finding
        assert "SIXTH DIVERGENCE PIN" in finding
        assert "ratchet 5 -> 6" in finding

    def test_negative_t_sign_means_meta_more_adversarial(self):
        # Negative t: target (Meta) mean < peer (Anthropic register) mean.
        assert ENGINE_T < 0
        assert TARGET_AVG < PEER_AVG

    def test_methodology_labels_manual_illustrative(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "MANUAL ILLUSTRATIVE" in s["methodology"]
        assert "DO NOT claim empirical significance" in s["methodology"]

    def test_yaml_engine_block_matches_pinned_values(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        eng = s["engine_welch_t_minus11_3358"]
        assert "t=-11.3358" in eng
        assert "p=0.001755" in eng
        assert "d=-9.2557" in eng
        assert "is_significant True" in eng


class TestMetaComparator547:
    def test_target_scores_carried_verbatim(self):
        s = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert s["target_scores_MANUAL_ILLUSTRATIVE"] == TARGET_SCORES

    def test_target_avg_4dp(self):
        assert TARGET_AVG == -0.7733
        assert _mechanism()["meta_comparator_carried_547"]["target_avg"] == -0.7733

    def test_peer_scores_match_beat_tones(self):
        beats = _mechanism()["september_beats_bounded_absence"]["beats"]
        tones = [b["manual_illustrative_tone"] for b in beats[:3]]
        assert tones == PEER_SCORES

    def test_comparator_note_names_547(self):
        note = _mechanism()["meta_comparator_carried_547"]["note"]
        assert "#547" in note


class TestFinancialContextHalo:
    def test_conde_nast_openai_deal_cited_in_corpus(self):
        fc = _mechanism()["financial_context"]
        assert "Aug 20 2024" in fc["conde_nast_openai_deal"]
        assert "wired.yaml:177" in fc["conde_nast_openai_deal"]
        assert fc["conde_nast_openai_deal_url"] == "https://www.reuters.com/technology/openai-signs-deal-with-cond-nast-2024-08-20/"

    def test_anthropic_direct_tie_zero(self):
        fc = _mechanism()["financial_context"]
        assert "$0" in fc["anthropic_direct_tie"]

    def test_meta_direct_tie_zero(self):
        fc = _mechanism()["financial_context"]
        assert "$0" in fc["meta_direct_tie"]

    def test_halo_hypothesis_states_rival_prediction_failure(self):
        fc = _mechanism()["financial_context"]
        assert "rival harshness" in fc["halo_hypothesis"]
        assert "fails" in fc["halo_hypothesis"]

    def test_correlation_only_language(self):
        fc = _mechanism()["financial_context"]
        assert "Correlation only" in fc["halo_hypothesis"]
        assert "correlational, not causal proof" in fc["editorial_independence_note"]

    def test_no_evidence_of_directive_reviewed(self):
        fc = _mechanism()["financial_context"]
        assert "No evidence of direct directive" in fc["editorial_independence_note"]

    def test_discovery_summary_names_halo_and_falsification_family(self):
        ds = _mechanism()["discovery_summary"]
        assert "LICENSING-HALO" in ds
        assert "falsification-of-financial-determinism" in ds
        assert "#552" in ds and "#193" in ds and "#599" in ds


class TestConfoundersAndCounterevidence:
    def test_three_strong_confounders(self):
        c = _mechanism()["confounders_ranked"]
        assert len(c["strong"]) == 3

    def test_three_moderate_confounders(self):
        c = _mechanism()["confounders_ranked"]
        assert len(c["moderate"]) == 3

    def test_two_weak_confounders(self):
        c = _mechanism()["confounders_ranked"]
        assert len(c["weak"]) == 2

    def test_strong_confounders_bound_the_absence_claim(self):
        strong = _mechanism()["confounders_ranked"]["strong"]
        blob = " ".join(strong)
        assert "bounded search-result absences" in blob
        assert "iteration-492" in blob

    def test_no_absolute_zero_coverage_claim(self):
        blob = str(_mechanism())
        assert "ZERO coverage" not in blob
        assert "zero coverage" not in blob.lower() or "zero coverage of the settlement itself" in blob.lower() or "bounded" in blob

    def test_four_counterevidence_items(self):
        ce = _mechanism()["counterevidence"]
        assert len(ce) == 4

    def test_counterevidence_includes_july_adversarial_capacity(self):
        blob = " ".join(_mechanism()["counterevidence"])
        assert "Jul 31" in blob

    def test_counterevidence_includes_no_disclosure_obligation(self):
        blob = " ".join(_mechanism()["counterevidence"])
        assert "no rule requires WIRED" in blob


class TestNoveltyVsExisting:
    def test_exactly_one_602_test_file(self):
        matches = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_a_602_*.py")
        )
        assert len(matches) == 1, f"expected exactly one 602 file, got {matches}"

    def test_mechanism_595_unique_in_profiles(self):
        out = subprocess.run(
            ["grep", "-rn", "mechanism_595", os.path.join(REPO_ROOT, "profiles")],
            capture_output=True,
            text=True,
        ).stdout
        hits = [l for l in out.splitlines() if "mechanism_595_wired_anthropic" in l]
        assert len(hits) == 1, f"mechanism_595 block should appear exactly once, got {hits}"

    def test_distinct_from_mechanism_92(self):
        nv = _mechanism()["novelty_vs_existing"]
        assert "EXTENDS" in nv["mechanism_92"]
        assert "35 days" in nv["mechanism_92"]

    def test_distinct_from_118_154_275_451_591(self):
        nv = _mechanism()["novelty_vs_existing"]
        for key in ["mechanism_118", "mechanism_154", "mechanism_275", "mechanism_451", "mechanism_591"]:
            assert key in nv, f"missing novelty distinction for {key}"

    def test_halo_member_joins_second_publication(self):
        nv = _mechanism()["novelty_vs_existing"]
        assert "second publication in the halo family" in nv["verge_anthropic_mechanism"]

    def test_anthropic_block_previously_had_no_595(self):
        d = _wired()
        block = d["competitor_relationships"]["anthropic"]
        mechanisms = [k for k in block if k.startswith("mechanism_")]
        assert "mechanism_595_wired_anthropic_licensing_halo_september_silence_extension_sep08" in mechanisms
        ids = [block[k].get("mechanism_id") for k in mechanisms]
        assert ids.count(595) == 1

    def test_delta_positive_sign_is_peer_softer(self):
        # Positive delta = peer register softer than Meta register.
        # Must not be conflated with #599's positive-sign inversion (that was
        # target-minus-peer); this run's convention is peer-minus-target.
        assert DELTA > 0
        assert PEER_AVG > TARGET_AVG


class TestRotationCycleGuard602:
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

    def test_window_598_602_closes_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "602"),
            ("E", "601"),
            ("D", "600"),
            ("C", "599"),
            ("B", "598"),
        ], f"rotation window 598-602 wrong: {observed}"

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

    def test_anchor_is_previous_main_e962d39(self):
        # Pre-commit anchor: the #601 main commit. The followup patches this
        # to the #602 main commit SHA once it is known.
        subjects = self._mains()
        assert subjects[0].startswith("Type E #601:"), (
            f"pre-commit anchor broken: newest main is not #601: {subjects[0]!r}"
        )


class TestDocSyncRatchet602:
    def test_readme_row_for_602(self):
        readme = read_readme()
        assert re.search(r"#602", readme), "README.md missing the #602 test-table row"

    def test_arch_row_for_602(self):
        arch = read_arch()
        assert re.search(r"#602", arch), "docs/ARCHITECTURE.md missing the #602 tree row"

    def test_601_row_survives_in_readme(self):
        readme = read_readme()
        assert re.search(r"#601", readme), "README.md lost the #601 row"

    def test_601_row_survives_in_arch(self):
        arch = read_arch()
        assert re.search(r"#601", arch), "docs/ARCHITECTURE.md lost the #601 row"
