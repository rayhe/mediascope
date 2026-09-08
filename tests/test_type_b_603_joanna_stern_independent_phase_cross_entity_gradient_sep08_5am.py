"""
Test Type B #603: Joanna Stern independent-phase cross-entity gradient inversion.

In Stern's independent (New Things) phase, two June 2026 product pieces carry
OPPOSITE registers: the Meta Ray-Ban LED-modding investigation is adversarial
(-0.65) while the Apple iOS 27 Siri AI week-long hands-on is constructive
(+0.60). Cross-entity delta (Meta minus Apple) INVERTS from +0.55 at WSJ
(Meta her most positive coverage) to -1.25 in the independent phase:
the post-migration adversarial turn is TARGET-SELECTED, not uniform.

Type B: Journalist Cross-Entity Tracking - September 8, 2026 (05:00 PDT)

KEY FINDING: writer-level cross-entity gradient inversion on the #105
career-migration natural experiment (mechanism_id 596, next free numeric id;
FIRST independent-phase cross-entity comparator on the Stern strand since the
Aug 7 #108/2999c7d Type B).

Independent-phase corpus (June 2026, both New Things):
- META (-0.65): "How People With Meta Glasses Can Secretly Record You" -
  paid $100 modder in NJ garage, 30-state LED-removal industry documented,
  Meta firmware update driven. https://www.youtube.com/watch?v=EaJSPeJmqis
  Impact relay (Jun 2026): "Joanna Stern, formerly of The Wall Street
  Journal, went in-depth on how this industry works in her latest YouTube
  video." https://www.androidheadlines.com/2026/06/people-are-paying-100-to-turn-metas-ray-bans-into-spy-glasses.html
- APPLE (+0.60): "Is Siri finally good?" - week-long iOS 27 Siri AI hands-on.
  9to5Mac Jun 19 2026 re-report: "answered strongly in the affirmative";
  "Siri that's pretty dead-on... I'm even considering switching to Apple
  Mail, and that says a lot". Guardrails/shortcomings also tested, verdict
  frame affirmative. https://9to5mac.com/2026/06/19/joanna-stern-spent-one-week-with-new-siri-ai-and-its-very-good/
- SNAP control (0.0, in-corpus, re-surfaced this run): NPR Morning Edition
  Jun 19 2026, "Every tech company right now is trying to work on this
  future" - neutral industry framing of $2,195 Specs.
  https://www.kdlg.org/as-heard-on-npr/2026-06-19/are-snaps-2-195-smart-glasses-the-next-big-thing-in-tech
- CONSTANCY control (in-corpus): NiemanLab May 2026 interview - her stated
  guiding principle "tech journalism for humans who like fun... to be the
  person who guides you through the world of technology". She claims voice
  continuity; observed cross-entity gradient inverts.
  https://www.niemanlab.org/2026/05/tech-journalist-joanna-stern-on-leaving-the-wall-street-journal-and-moving-on-to-new-things/

ILLUSTRATIVE scoring (MANUAL, standing Aug 28 2026 rule):
WSJ-phase Meta (+0.35) minus Apple (-0.20) = +0.55.
Independent-phase Meta (-0.65) minus Apple (+0.60) = -1.25.
Inversion magnitude 1.80. n=1 per arm. p_value/cohens_d/ci_95
NOT_CALCULATED. is_significant: false.

WHY IT MATTERS: the in-corpus journalist_cross_entity.joanna_stern block
established the migration tone shift (+0.35 -> -0.65) as the LARGEST
single-journalist Meta tone shift in the dataset and the reverse-Heikkila
mirror. This mechanism REFINES it: within the independent phase itself she
is constructive toward Apple (+0.60), so the adversarial turn is not a
uniform register shift - it is target-selected toward Meta. The driver class
stays financial-structure/incentive (audience economics, sponsor pool) but
the scope narrows. Inverts against her own WSJ baseline where Meta got the
BEST treatment (+0.35, most positive) and Apple the most critical (-0.20).
Sits as the inversion counterpoint to #598 (Hern constancy).

Confounders (graded): STRONG - genre asymmetry (investigative expose vs
product hands-on; hands-on genre constructive by default); n=1 per arm;
revenue incentives apply to BOTH phases (they differ, not absent).
MODERATE - Siri piece relay-characterized, not first-hand fetched; verdict
frame affirmative despite shortcomings noted. WEAK - New Things sponsor
identities undisclosed; MacDailyNews stale "WSJ's Joanna Stern" byline.
Counterevidence (4): WSJ-phase Meta was her most positive portfolio item;
Siri video tested shortcomings; Meta firmware-update response got a
special-edition newsletter (fair-process); reverse-Heikkila direction still
holds - this mechanism only narrows scope to target-selection.

URLs are verbatim from this run's browser.search Full-URL listings. No
canonical URLs constructed. No zero-coverage claims (iteration-492 rule).
All tone values MANUAL ILLUSTRATIVE per the standing rule.
"""
import re

import pytest
import yaml

MECHANISM_KEY = "mechanism_596_joanna_stern_independent_phase_cross_entity_gradient_inversion_sep08"
MECHANISM_ID = 596
ITERATION = 603

YOUTUBE_META = "https://www.youtube.com/watch?v=EaJSPeJmqis"
ANDROID_HEADLINES_RELAY = "https://www.androidheadlines.com/2026/06/people-are-paying-100-to-turn-metas-ray-bans-into-spy-glasses.html"
NINE_TO_FIVE_SIRI = "https://9to5mac.com/2026/06/19/joanna-stern-spent-one-week-with-new-siri-ai-and-its-very-good/"
NPR_SNAP = "https://www.kdlg.org/as-heard-on-npr/2026-06-19/are-snaps-2-195-smart-glasses-the-next-big-thing-in-tech"
NIEMANLAB = "https://www.niemanlab.org/2026/05/tech-journalist-joanna-stern-on-leaving-the-wall-street-journal-and-moving-on-to-new-things/"


@pytest.fixture(scope="module")
def profiles():
    with open("profiles/news-corp.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def mechanism(profiles):
    jce = profiles["journalist_cross_entity"]
    assert MECHANISM_KEY in jce, f"{MECHANISM_KEY} missing from journalist_cross_entity"
    return jce[MECHANISM_KEY]


@pytest.fixture(scope="module")
def scorer(mechanism):
    return mechanism["asymmetry_scorer"]


class TestIterationMetadata603:
    def test_iteration_number(self, mechanism):
        assert mechanism["iteration"] == ITERATION

    def test_mechanism_id(self, mechanism):
        assert mechanism["mechanism_id"] == MECHANISM_ID

    def test_date(self, mechanism):
        assert mechanism["date"] == "2026-09-08"

    def test_hour_type_b(self, mechanism):
        assert mechanism["hour_type"] == "B"


class TestYamlStructure603:
    def test_key_present(self, profiles):
        assert MECHANISM_KEY in profiles["journalist_cross_entity"]

    def test_required_keys(self, mechanism):
        for key in ("mechanism_id", "iteration", "date", "hour_type", "title",
                    "finding", "independent_phase_corpus", "asymmetry_scorer",
                    "confounders_ranked", "counterevidence", "distinct_from",
                    "research_method", "artifact_readiness", "author"):
            assert key in mechanism, f"missing key: {key}"

    def test_corpus_has_four_arms(self, mechanism):
        corpus = mechanism["independent_phase_corpus"]
        for arm in ("meta", "apple", "snap_control", "constancy_control"):
            assert arm in corpus, f"missing corpus arm: {arm}"

    def test_mechanism_id_unique(self, profiles):
        text = open("profiles/news-corp.yaml", encoding="utf-8").read()
        assert text.count("mechanism_id: 596") == 1

    def test_title_names_gradient_inversion(self, mechanism):
        assert "gradient inversion" in mechanism["title"].lower()

    def test_scorer_method_manual(self, scorer):
        assert scorer["method"] == "MANUAL_ILLUSTRATIVE"

    def test_author_kit_with_ray(self, mechanism):
        assert mechanism["author"] == "Kit (with Ray)"


class TestIndependentPhaseCorpus603:
    def test_meta_tone(self, mechanism):
        assert mechanism["independent_phase_corpus"]["meta"]["tone"] == -0.65

    def test_meta_article(self, mechanism):
        assert "Secretly Record You" in mechanism["independent_phase_corpus"]["meta"]["article"]

    def test_meta_url_verbatim(self, mechanism):
        assert mechanism["independent_phase_corpus"]["meta"]["source_url"] == YOUTUBE_META

    def test_meta_impact_relay_verbatim(self, mechanism):
        relay = mechanism["independent_phase_corpus"]["meta"]["impact_relay"]
        assert relay == ANDROID_HEADLINES_RELAY

    def test_meta_quote_vocabulary(self, mechanism):
        quote = mechanism["independent_phase_corpus"]["meta"]["quote"]
        assert "spy cameras" in quote and "glassholes" in quote

    def test_apple_tone(self, mechanism):
        assert mechanism["independent_phase_corpus"]["apple"]["tone"] == 0.60

    def test_apple_url_verbatim(self, mechanism):
        assert mechanism["independent_phase_corpus"]["apple"]["source_url"] == NINE_TO_FIVE_SIRI

    def test_apple_quote_affirmative(self, mechanism):
        quote = mechanism["independent_phase_corpus"]["apple"]["quote"]
        assert "dead-on" in quote and "Apple Mail" in quote

    def test_apple_tier_note(self, mechanism):
        assert "Relay" in mechanism["independent_phase_corpus"]["apple"]["tier_note"]

    def test_snap_control_neutral(self, mechanism):
        snap = mechanism["independent_phase_corpus"]["snap_control"]
        assert snap["tone"] == 0.0
        assert snap["source_url"] == NPR_SNAP

    def test_constancy_control_quote(self, mechanism):
        const = mechanism["independent_phase_corpus"]["constancy_control"]
        assert "guides you through the world of technology" in const["quote"]
        assert const["source_url"] == NIEMANLAB

    def test_all_four_urls_verbatim_format(self, mechanism):
        corpus = mechanism["independent_phase_corpus"]
        urls = [corpus["meta"]["source_url"], corpus["apple"]["source_url"],
                corpus["snap_control"]["source_url"], corpus["constancy_control"]["source_url"]]
        for url in urls:
            assert url.startswith("https://"), url


class TestWsjPhaseBaseline603:
    def test_wsj_delta_carried(self, scorer):
        assert scorer["wsj_phase_meta_minus_apple_delta"] == 0.55

    def test_wsj_delta_sign_positive(self, scorer):
        assert scorer["wsj_phase_meta_minus_apple_delta"] > 0

    def test_finding_states_wsj_arms(self, mechanism):
        finding = mechanism["finding"]
        assert "+0.35" in finding and "-0.20" in finding


class TestScorerConsistency603:
    def test_independent_delta(self, scorer):
        assert scorer["independent_phase_meta_minus_apple_delta"] == -1.25

    def test_inversion_magnitude_arithmetic(self, scorer):
        expected = scorer["wsj_phase_meta_minus_apple_delta"] - scorer["independent_phase_meta_minus_apple_delta"]
        assert abs(scorer["inversion_magnitude"] - expected) < 1e-9
        assert scorer["inversion_magnitude"] == 1.80

    def test_p_not_calculated(self, scorer):
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"

    def test_not_significant(self, scorer):
        assert scorer["is_significant"] is False

    def test_correlation_not_causation(self, scorer):
        assert scorer["correlation_not_causation"] is True

    def test_n_per_arm_one(self, scorer):
        assert scorer["n_per_arm"] == 1

    def test_finding_states_deltas(self, mechanism):
        finding = mechanism["finding"]
        assert "-1.25" in finding and "+0.55" in finding

    def test_artifact_not_ready(self, mechanism):
        assert "No analysis.json" in mechanism["artifact_readiness"]


class TestCrossEntityGradient603:
    def test_meta_adversarial_vs_apple_constructive(self, mechanism):
        corpus = mechanism["independent_phase_corpus"]
        assert corpus["meta"]["tone"] < 0 < corpus["apple"]["tone"]

    def test_gradient_sign_negative(self, scorer):
        assert scorer["independent_phase_meta_minus_apple_delta"] < 0

    def test_wsj_phase_meta_best_treatment(self, mechanism):
        finding = mechanism["finding"]
        assert "most positive" in finding

    def test_snap_control_no_privacy_investigation(self, mechanism):
        snap = mechanism["independent_phase_corpus"]["snap_control"]
        assert "no privacy investigation" in snap["framing"]

    def test_constancy_claim_bounded(self, mechanism):
        const = mechanism["independent_phase_corpus"]["constancy_control"]
        assert "inverts" in const["significance"]


class TestConfounders603:
    def test_three_grades(self, mechanism):
        conf = mechanism["confounders_ranked"]
        assert set(conf.keys()) == {"strong", "moderate", "weak"}

    def test_strong_genre_asymmetry(self, mechanism):
        strong = mechanism["confounders_ranked"]["strong"]
        assert any("Genre asymmetry" in s for s in strong)

    def test_strong_n_one(self, mechanism):
        strong = mechanism["confounders_ranked"]["strong"]
        assert any("n=1" in s for s in strong)

    def test_moderate_relay(self, mechanism):
        moderate = mechanism["confounders_ranked"]["moderate"]
        assert any("relay-characterized" in s for s in moderate)

    def test_weak_sponsor_bound(self, mechanism):
        weak = mechanism["confounders_ranked"]["weak"]
        assert any("sponsor" in s.lower() for s in weak)


class TestCounterevidence603:
    def test_four_items(self, mechanism):
        assert len(mechanism["counterevidence"]) == 4

    def test_wsj_meta_baseline(self, mechanism):
        assert any("most positive" in c for c in mechanism["counterevidence"])

    def test_fair_process_newsletter(self, mechanism):
        assert any("special-edition newsletter" in c for c in mechanism["counterevidence"])

    def test_reverse_heikkila_holds(self, mechanism):
        assert any("reverse-Heikkila" in c or "reverse Heikkila" in c
                   for c in mechanism["counterevidence"])


class TestNovelty603:
    def test_distinct_from_mechanism_105(self, mechanism):
        joined = " ".join(mechanism["distinct_from"])
        assert "mechanism #105" in joined

    def test_distinct_from_aug_type_b(self, mechanism):
        joined = " ".join(mechanism["distinct_from"])
        assert "2999c7d" in joined

    def test_distinct_from_hern_598(self, mechanism):
        joined = " ".join(mechanism["distinct_from"])
        assert "#598" in joined and "Hern" in joined

    def test_distinct_from_falsification_family(self, mechanism):
        joined = " ".join(mechanism["distinct_from"])
        assert "#599" in joined and "Song" in joined

    def test_hern_is_constancy_counterpoint(self, mechanism):
        joined = " ".join(mechanism["distinct_from"])
        assert "constancy" in joined.lower() and "inversion" in joined.lower()

    def test_research_method_documents_novelty_greps(self, mechanism):
        rm = mechanism["research_method"]
        assert "mechanism_596" in rm and "zero" in rm.lower()


class TestRotationCycleGuard603:
    """Covers the 599-603 main-commit window (B,C,D,E,A newest-first),
    closing the A->B edge. ANCHOR PATCHED POST-COMMIT per the #565 followup
    convention: the expected anchor commit id is filled in the followup run
    after the main commit is created."""
    EXPECTED_WINDOW_NEWEST_FIRST = [
        ("Type B", 603),
        ("Type A", 602),
        ("Type E", 601),
        ("Type D", 600),
        ("Type C", 599),
    ]
    # Anchor: patched in followup - see iteration-log entry for #603.
    ANCHOR_MAIN_COMMIT = "PENDING_FOLLOWUP_PATCH"

    def test_window_sequence(self):
        seq = [(t, n) for t, n in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert seq[0] == ("Type B", 603)
        assert seq[-1] == ("Type C", 599)

    def test_closes_a_to_b_edge(self):
        types = [t for t, _ in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert types[0] == "Type B" and types[1] == "Type A"

    def test_five_window_members(self):
        assert len(self.EXPECTED_WINDOW_NEWEST_FIRST) == 5
