"""Type B #613 (2026-09-08 16:00 PDT): Brian Heater (TechCrunch, hardware editor
until early 2025) cross-entity hands-on register constancy.

Within-journalist comparison: Heater covers Meta glasses (Ray-Ban Meta review,
Oct 17 2023, first-hand field review; Meta Orion announcement, Sep 25 2024)
and Apple (Vision Pro Day One, Feb 1 2024, launch-day setup diary), with a
comparative Snap dig inside the Orion piece. The BODY register is CONSTANT
across Meta and Apple: hands-on, design-forward, first-person, self-deprecating
humor, use-case caveats for both entities. Two BOUNDED divergences sit in
framing layers above the body: (1) headline register - snide "influencer"
social-frame for the Meta Ray-Ban review vs neutral-service "Day One" for
Apple (Meta Orion headline is neutral-technical, register-matched to Apple);
(2) price framing - Apple $3,500 justified via explicit R&D apologia vs Meta
$299 value-caveat vs Orion $10K/unit bump-citation.

The verdict is a CONSTANCY pin for the financial theory (TechCrunch carries no
in-corpus AI licensing deals with Meta or Apple, predicting a NULL gap, and
the body register matches that prediction): joins the reporter-level
falsification/alternative-driver family (#538, #548, #553, #563, #568, #578,
#583, #588, #608). Directional, not dispositive.

All tone values are MANUAL ILLUSTRATIVE per the Aug 28 2026 standing rule.
p_value / cohens_d / ci_95 are NOT_CALCULATED; is_significant is false.
correlation_not_causation. No em dashes anywhere in this file.
"""
import yaml
import pytest

ITERATION = 613
MECHANISM_ID = 602
MECHANISM_KEY = ("mechanism_602_brian_heater_techcrunch_meta_vs_apple_"
                 "hands_on_register_constancy_sep08")

ORION_URL = ("https://techcrunch.com/2024/09/25/"
             "meta-teases-orion-the-most-advanced-glasses-the-world-has-ever-seen")
RAYBAN_URL = "http://techcrunch.com/2023/10/17/ray-ban-meta-review/1200"
VISIONPRO_URL = "https://techcrunch.com/2024/01/31/apple-vision-pro-day-one/"


@pytest.fixture(scope="module")
def profiles():
    with open("profiles/careers/journalists.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def entry(profiles):
    matches = [j for j in profiles["journalists"]
               if j.get("name") == "Brian Heater"]
    assert len(matches) == 1, f"expected exactly one Brian Heater entry, got {len(matches)}"
    return matches[0]


@pytest.fixture(scope="module")
def mechanism(entry):
    assert MECHANISM_KEY in entry, f"{MECHANISM_KEY} missing from Brian Heater entry"
    return entry[MECHANISM_KEY]


@pytest.fixture(scope="module")
def scorer(mechanism):
    return mechanism["asymmetry_scorer_result_illustrative"]


class TestIterationMetadata613:
    def test_iteration_number(self, mechanism):
        assert mechanism["iteration"] == ITERATION

    def test_mechanism_id(self, mechanism):
        assert mechanism["mechanism_id"] == MECHANISM_ID

    def test_date(self, mechanism):
        assert mechanism["date"] == "2026-09-08 16:00 PDT"

    def test_hour_type_b(self, mechanism):
        assert mechanism["type"] == "B"

    def test_job_and_goal(self, mechanism):
        assert mechanism["job_id"] == "mediascope-daily-iteration"
        assert mechanism["goal"] == "goal_54093bda4145"


class TestJournalistEntry613:
    def test_entry_name(self, entry):
        assert entry["name"] == "Brian Heater"

    def test_techcrunch_career_present(self, entry):
        pubs = [c.get("publication") for c in entry["career"]]
        assert "techcrunch" in pubs

    def test_hardware_editor_role(self, entry):
        roles = [c.get("role") for c in entry["career"]]
        assert "hardware_editor" in roles

    def test_departure_date_noted(self, entry):
        career = [c for c in entry["career"] if c.get("publication") == "techcrunch"][0]
        assert career["end"] == "2025-02"
        assert "early 2025" in career["notes"]

    def test_three_source_urls_verbatim(self, entry):
        assert ORION_URL in entry["source_urls"]
        assert RAYBAN_URL in entry["source_urls"]
        assert VISIONPRO_URL in entry["source_urls"]

    def test_multi_publication_flag(self, entry):
        assert entry["multi_publication"] is True


class TestMetaArmRayBan613:
    @pytest.fixture(scope="class")
    def rayban(self, mechanism):
        return mechanism["meta_arm"]["rayban_meta_review"]

    def test_piece_date(self, rayban):
        assert "Oct 17 2023" in rayban["piece"]

    def test_source_url_verbatim(self, rayban):
        assert rayban["source_url"] == RAYBAN_URL

    def test_tone_illustrative(self, rayban):
        assert rayban["tone_illustrative"] == -0.10

    def test_design_praise_quoted(self, rayban):
        notes = rayban["framing_notes"]
        assert "genuinely impressed by the industrial design" in notes
        assert "surprisingly few concessions" in notes

    def test_headline_register_noted(self, rayban):
        assert "influencer" in rayban["framing_notes"]

    def test_price_caveat_quoted(self, rayban):
        assert "sheer novelty" in rayban["framing_notes"]

    def test_privacy_register_meta_favorable(self, rayban):
        notes = rayban["framing_notes"]
        assert "extremely necessary" in notes
        assert "privacy is paramount" in notes


class TestMetaArmOrion613:
    @pytest.fixture(scope="class")
    def orion(self, mechanism):
        return mechanism["meta_arm"]["orion"]

    def test_piece_date(self, orion):
        assert "Sep 25 2024" in orion["piece"]

    def test_source_url_verbatim(self, orion):
        assert orion["source_url"] == ORION_URL

    def test_tone_illustrative(self, orion):
        assert orion["tone_illustrative"] == 0.10

    def test_cost_skepticism_noted(self, orion):
        notes = orion["framing_notes"]
        assert "$10,000 per unit" in notes
        assert "concept phase" in notes

    def test_zuckerberg_hyperbole_line(self, orion):
        assert "hard to accuse Zuckerberg of hyperbole" in orion["framing_notes"]

    def test_snap_dig_present(self, orion):
        assert "narrow FOV" in orion["framing_notes"]


class TestAppleArmVisionPro613:
    @pytest.fixture(scope="class")
    def visionpro(self, mechanism):
        return mechanism["apple_arm"]["vision_pro_day_one"]

    def test_piece_date(self, visionpro):
        assert "Feb 1 2024" in visionpro["piece"]

    def test_source_url_verbatim(self, visionpro):
        assert visionpro["source_url"] == VISIONPRO_URL

    def test_tone_illustrative(self, visionpro):
        assert visionpro["tone_illustrative"] == 0.20

    def test_rd_apologia_quoted(self, visionpro):
        assert "millions poured into seven or eight years of R&D" in visionpro["framing_notes"]

    def test_playful_not_puffery(self, visionpro):
        notes = visionpro["framing_notes"]
        assert "talking thumb with a huffing addiction" in notes
        assert "motion-sickness" in notes or "motion sickness" in notes


class TestSnapContext613:
    @pytest.fixture(scope="class")
    def snap(self, mechanism):
        return mechanism["snap_context"]

    def test_not_scored(self, snap):
        assert snap["scoring"] == "NOT_SCORED - comparative context only, not a scored arm; the piece belongs to Meta's arm."

    def test_spectacles_dig_quoted(self, snap):
        assert "extremely large with a very narrow FOV" in snap["piece"]

    def test_source_url_is_orion(self, snap):
        assert snap["source_url"] == ORION_URL


class TestPriceFramingDivergence613:
    @pytest.fixture(scope="class")
    def pricing(self, mechanism):
        return mechanism["price_framing_divergence"]

    def test_apple_rd_apologia(self, pricing):
        assert "R&D apologia" in pricing["apple"]

    def test_meta_value_caveat(self, pricing):
        assert "value-caveat" in pricing["meta_rayban"]

    def test_orion_bump_citation(self, pricing):
        assert "bump" in pricing["meta_orion"]

    def test_bounded_note(self, pricing):
        assert "Bounded to price-sentences only" in pricing["note"]


class TestHeadlineRegisterDivergence613:
    @pytest.fixture(scope="class")
    def headlines(self, mechanism):
        return mechanism["headline_register_divergence"]

    def test_meta_rayban_headline(self, headlines):
        assert "influencer" in headlines["meta_rayban"]

    def test_apple_headline(self, headlines):
        assert "Day One" in headlines["apple"]

    def test_orion_headline_register_matched(self, headlines):
        assert "neutral-technical" in headlines["meta_orion"]
        assert "register-matched to the Apple piece" in headlines["note"]

    def test_bounded_to_rayban(self, headlines):
        assert "bounded to the Ray-Ban review" in headlines["note"]


class TestIllustrativeDelta613:
    @pytest.fixture(scope="class")
    def delta(self, mechanism):
        return mechanism["illustrative_delta"]

    def test_convention(self, delta):
        assert delta["convention"] == "Meta minus Apple"

    def test_meta_avg_arithmetic(self, delta):
        scores = delta["meta_scores"]
        assert scores == [-0.10, 0.10]
        assert round(sum(scores) / len(scores), 2) == delta["meta_avg"] == 0.0

    def test_apple_avg(self, delta):
        assert delta["apple_scores"] == [0.20]
        assert delta["apple_avg"] == 0.20

    def test_delta_arithmetic(self, delta):
        assert round(delta["meta_avg"] - delta["apple_avg"], 2) == delta["delta"] == -0.20


class TestScorerDiscipline613:
    def test_engine_t_path_degenerate(self, scorer):
        from mediascope.score.statistical import welch_t_test
        t, p = welch_t_test([-0.10, 0.10], [0.20])
        assert (t, p) == (0.0, 1.0)
        assert "n=1 apple arm" in scorer["engine"]

    def test_engine_cohens_nonzero_mirror(self, scorer):
        from mediascope.score.statistical import cohens_d
        d = cohens_d([-0.10, 0.10], [0.20])
        assert round(d, 4) == -1.4142
        assert "NOT a new pin" in scorer["engine"]
        assert "#610 taxonomy" in scorer["engine"]

    def test_p_value_not_calculated(self, scorer):
        assert scorer["p_value"] == "NOT_CALCULATED"

    def test_cohens_not_calculated(self, scorer):
        assert scorer["cohens_d"] == "NOT_CALCULATED"

    def test_ci_not_calculated(self, scorer):
        assert scorer["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self, scorer):
        assert scorer["is_significant"] is False

    def test_statistical_discipline_string(self, scorer):
        assert scorer["statistical_discipline"] == "MANUAL ILLUSTRATIVE per standing rule Aug 28 2026; correlation_not_causation."


class TestConfounders613:
    def test_four_confounders(self, mechanism):
        assert len(mechanism["confounders"]) == 4

    def test_strength_tags(self, mechanism):
        tags = [c.split("]")[0] for c in mechanism["confounders"]]
        assert tags == ["[STRONG", "[STRONG", "[MODERATE", "[WEAK"]

    def test_genre_boundary_cited(self, mechanism):
        assert "#593 genre boundary" in mechanism["confounders"][0]

    def test_timing_skew(self, mechanism):
        assert "Oct 2023" in mechanism["confounders"][1]
        assert "Feb 2024" in mechanism["confounders"][1]
        assert "Sep 2024" in mechanism["confounders"][1]

    def test_three_counterexamples(self, mechanism):
        assert len(mechanism["counterexamples"]) == 3

    def test_orion_meta_favorable_counterexample(self, mechanism):
        assert "hard to accuse Zuckerberg of hyperbole" in mechanism["counterexamples"][0]


class TestNoveltyAndCrossRefs613:
    def test_novelty_note_free_mechanism(self, mechanism):
        assert "next free profiles mechanism id" in mechanism["novelty_note"]
        assert "(max pre-commit 601" in mechanism["novelty_note"]

    def test_block_key(self, mechanism):
        assert mechanism["block_key"] == "type_b_613_brian_heater_techcrunch_meta_apple_hands_on_constancy"

    def test_test_file_value(self, mechanism):
        assert mechanism["test_file"] == ("tests/test_type_b_613_brian_heater_techcrunch_"
                                          "meta_apple_hands_on_constancy_sep08_4pm.py")

    def test_cross_refs_gurman_and_stein(self, mechanism):
        refs = " ".join(mechanism["cross_refs"])
        assert "#593" in refs
        assert "#588" in refs
        assert "#608" in refs

    def test_verdict_constancy_pin(self, mechanism):
        assert "CONSTANCY pin" in mechanism["verdict"]
        assert "Illustrative only, significant False" in mechanism["verdict"]

    def test_no_em_dashes_in_mechanism(self, mechanism):
        import json
        blob = json.dumps(mechanism)
        assert "\u2014" not in blob, "em dash found in mechanism block"

    def test_artifact_readiness_no_update(self, mechanism):
        assert mechanism["artifact_readiness"].startswith("No analysis.json update warranted")

    def test_author_attribution(self, mechanism):
        assert mechanism["author"] == "Kit (with Ray)"


class TestRotationCycleGuard613:
    """Covers the 609-613 main-commit window (B,A,E,D,C newest-first),
    closing the A->B edge. ANCHOR PATCHED POST-COMMIT per the #565 followup
    convention: the expected anchor commit id is filled in the followup run
    after the main commit is created."""
    EXPECTED_WINDOW_NEWEST_FIRST = [
        ("Type B", 613),
        ("Type A", 612),
        ("Type E", 611),
        ("Type D", 610),
        ("Type C", 609),
    ]
    # Anchor: patched in followup - see iteration-log entry for #613.
    ANCHOR_MAIN_COMMIT = "PENDING_FOLLOWUP_PATCH"

    def test_window_sequence(self):
        seq = [(t, n) for t, n in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert seq[0] == ("Type B", 613)
        assert seq[-1] == ("Type C", 609)

    def test_closes_a_to_b_edge(self):
        types = [t for t, _ in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert types[0] == "Type B" and types[1] == "Type A"

    def test_five_window_members(self):
        assert len(self.EXPECTED_WINDOW_NEWEST_FIRST) == 5

    def test_anchor_patched_post_commit(self):
        assert self.ANCHOR_MAIN_COMMIT is not None and self.ANCHOR_MAIN_COMMIT != "PENDING_FOLLOWUP_PATCH"
