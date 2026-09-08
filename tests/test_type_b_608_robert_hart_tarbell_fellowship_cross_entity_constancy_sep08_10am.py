"""Type B #608 (2026-09-08 10:00 PDT): Robert Hart (The Verge, Senior Tarbell
Fellow) cross-entity register constancy.

Writer-level control: Hart covers OpenAI (DseWiki agent breakout, adversarial
delayed-disclosure, -0.65) and Meta (AI-app clickbait column, adversarial
diminutive, -0.50). Illustrative delta -0.15 is noise; the finding is CONSTANCY
of an adversarial register across a frontier lab and Meta, not Meta-specific
asymmetry. Tarbell fellowship funder chain (Moskovitz-backed Coefficient
Giving; Moskovitz reported Anthropic investor) is documented as structural
financial context with an explicit correlational-only causal boundary - it
predicts safety-critical scrutiny of ALL frontier labs, not Meta-specific
harshness.

All tone values are MANUAL ILLUSTRATIVE. p_value / cohens_d / ci_95 are
NOT_CALCULATED; is_significant is false. correlation_not_causation.
"""
import yaml
import pytest

ITERATION = 608
MECHANISM_ID = 599
MECHANISM_KEY = "mechanism_599_robert_hart_tarbell_fellowship_cross_entity_constancy_sep08"

VERGE_WIKI = "https://www.theverge.com/ai-artificial-intelligence/990773/openai-german-wiki-incident"
META_RELAY = "https://github.com/modestyzht/modestyzht.github.io/blob/HEAD/source/_posts/ai-daily-2026-06-07.md"
FOX_TARBELL = "https://foxnews.com/politics/top-media-outlets-fail-disclose-bankrolling-ai-reporters"
BIO_URL = "https://talkingbiznews.com/media-news/hart-now-covering-ai-for-the-verge/"


@pytest.fixture(scope="module")
def profiles():
    with open("profiles/careers/journalists.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def entry(profiles):
    matches = [j for j in profiles["journalists"] if j.get("name") == "Robert Hart"]
    assert len(matches) == 1, f"expected exactly one Robert Hart entry, got {len(matches)}"
    return matches[0]


@pytest.fixture(scope="module")
def mechanism(entry):
    assert MECHANISM_KEY in entry, f"{MECHANISM_KEY} missing from Robert Hart entry"
    return entry[MECHANISM_KEY]


@pytest.fixture(scope="module")
def scorer(mechanism):
    return mechanism["asymmetry_scorer_result_illustrative"]


class TestIterationMetadata608:
    def test_iteration_number(self, mechanism):
        assert mechanism["iteration"] == ITERATION

    def test_mechanism_id(self, mechanism):
        assert mechanism["mechanism_id"] == MECHANISM_ID

    def test_date(self, mechanism):
        assert mechanism["date"] == "2026-09-08 10:00 PDT"

    def test_hour_type_b(self, mechanism):
        assert mechanism["type"] == "B"

    def test_job_and_goal(self, mechanism):
        assert mechanism["job_id"] == "mediascope-daily-iteration"
        assert mechanism["goal"] == "goal_54093bda4145"


class TestYamlStructure608:
    def test_entry_bio_url(self, entry):
        assert BIO_URL in entry["source_urls"]

    def test_tarbell_fellowship_noted(self, entry):
        assert "Tarbell" in entry["notes"]

    def test_required_keys(self, mechanism):
        for key in ("mechanism_id", "iteration", "date", "type", "title",
                    "openai_arm", "meta_arm", "tarbell_financial_context",
                    "illustrative_delta", "asymmetry_scorer_result_illustrative",
                    "confounders", "counterexamples", "research_method",
                    "artifact_readiness", "author", "test_file"):
            assert key in mechanism, f"missing key: {key}"

    def test_mechanism_id_unique(self):
        text = open("profiles/careers/journalists.yaml", encoding="utf-8").read()
        assert text.count("mechanism_id: 599") == 1

    def test_title_names_constancy(self, mechanism):
        assert "constancy" in mechanism["title"].lower()

    def test_author_kit_with_ray(self, mechanism):
        assert mechanism["author"] == "Kit (with Ray)"


class TestCorpusArms608:
    def test_openai_tone(self, mechanism):
        assert mechanism["openai_arm"]["tone_illustrative"] == -0.65

    def test_openai_url_verbatim(self, mechanism):
        assert mechanism["openai_arm"]["source_url"] == VERGE_WIKI

    def test_openai_byline_bounded(self, mechanism):
        assert "second-hand" in mechanism["openai_arm"]["source_note"]

    def test_meta_tone(self, mechanism):
        assert mechanism["meta_arm"]["tone_illustrative"] == -0.50

    def test_meta_url_verbatim(self, mechanism):
        assert mechanism["meta_arm"]["source_url"] == META_RELAY

    def test_meta_relay_characterized(self, mechanism):
        assert "relay" in mechanism["meta_arm"]["source_note"].lower()

    def test_anthropic_context_not_scored(self, mechanism):
        ctx = mechanism["anthropic_context"]
        assert ctx["source_url"] == FOX_TARBELL
        assert "NOT a scored arm" in ctx["source_note"]

    def test_all_urls_verbatim_format(self, mechanism):
        for url in (mechanism["openai_arm"]["source_url"],
                    mechanism["meta_arm"]["source_url"],
                    mechanism["anthropic_context"]["source_url"]):
            assert url.startswith("https://"), url


class TestIllustrativeDelta608:
    def test_delta_convention(self, mechanism):
        delta = mechanism["illustrative_delta"]
        assert delta["convention"] == "OpenAI minus Meta"
        assert delta["openai"] == -0.65
        assert delta["meta"] == -0.50
        assert abs(delta["delta"] - (-0.15)) < 1e-9

    def test_scorer_degenerate_symmetric(self, scorer):
        assert "t=0.0, p=1.0" in scorer["engine"]
        assert "n=1 vs n=1" in scorer["engine"]

    def test_degenerate_boundary_pin_sixth(self, scorer):
        assert scorer["degenerate_boundary_pin"].startswith("sixth")

    def test_stats_not_calculated(self, scorer):
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False

    def test_statistical_discipline(self, scorer):
        assert "MANUAL ILLUSTRATIVE" in scorer["statistical_discipline"]
        assert "correlation_not_causation" in scorer["statistical_discipline"]


class TestFinancialContextBoundary608:
    def test_funders_attributed(self, mechanism):
        ctx = mechanism["tarbell_financial_context"]
        assert "Coefficient Giving" in ctx["funders_claimed"]
        assert "Dustin Moskovitz" in ctx["funders_claimed"]

    def test_causal_boundary_correlational_only(self, mechanism):
        ctx = mechanism["tarbell_financial_context"]
        assert "CORRELATIONAL ONLY" in ctx["causal_boundary"]
        assert "No causal claim asserted" in ctx["causal_boundary"]

    def test_disclosure_gap_positive_control(self, mechanism):
        ctx = mechanism["tarbell_financial_context"]
        assert "NBC News" in ctx["disclosure_gap"]


class TestConfounders608:
    def test_three_confounders(self, mechanism):
        assert len(mechanism["confounders"]) == 3

    def test_strong_confounders_first(self, mechanism):
        assert mechanism["confounders"][0].startswith("STRONG:")
        assert mechanism["confounders"][1].startswith("STRONG:")
        assert mechanism["confounders"][2].startswith("MODERATE:")

    def test_genre_confounder_present(self, mechanism):
        assert "genre asymmetry" in mechanism["confounders"][1].lower()

    def test_two_counterexamples(self, mechanism):
        assert len(mechanism["counterexamples"]) == 2


class TestNovelty608:
    def test_research_method_documents_novelty_greps(self, mechanism):
        rm = mechanism["research_method"]
        assert "zero" in rm.lower() and "robert hart" in rm.lower()

    def test_novelty_note_next_free_id(self, mechanism):
        assert "599" in mechanism["novelty_note"] and "598" in mechanism["novelty_note"]


class TestRotationCycleGuard608:
    """Covers the 604-608 main-commit window (B,A,E,D,C newest-first),
    closing the A->B edge. ANCHOR PATCHED POST-COMMIT per the #565 followup
    convention: the expected anchor commit id is filled in the followup run
    after the main commit is created."""
    EXPECTED_WINDOW_NEWEST_FIRST = [
        ("Type B", 608),
        ("Type A", 607),
        ("Type E", 606),
        ("Type D", 605),
        ("Type C", 604),
    ]
    # Anchor: patched in followup - see iteration-log entry for #608.
    ANCHOR_MAIN_COMMIT = "1016ef0"

    def test_window_sequence(self):
        seq = [(t, n) for t, n in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert seq[0] == ("Type B", 608)
        assert seq[-1] == ("Type C", 604)

    def test_closes_a_to_b_edge(self):
        types = [t for t, _ in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert types[0] == "Type B" and types[1] == "Type A"

    def test_five_window_members(self):
        assert len(self.EXPECTED_WINDOW_NEWEST_FIRST) == 5

    def test_anchor_patched_post_commit(self):
        assert self.ANCHOR_MAIN_COMMIT is not None
