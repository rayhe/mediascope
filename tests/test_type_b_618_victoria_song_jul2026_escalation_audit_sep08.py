"""Type B #618 (2026-09-08 21:00 PDT): Victoria Song (The Verge, senior reviewer,
wearables beat) Jul 2026 escalation audit - register-conditioned asymmetry.

Within-writer comparison across two registers:
(a) the privacy-editorial register - the Jul 2026 Meta trilogy, three items in
20 days (Jul 7 LED-tamper origin story, Jul 20 "pervert glasses" editorial,
Jul 27 "holds all the cards" backlash narrative);
(b) the product-news register - Apple Siri-AI Watch item Jul 13 2026 (same
two-week window), Samsung Galaxy XR hands-on Oct 2025, Google Android XR
JARVIS comparison Dec 2024, plus Meta-positive product arms Sep 2025 and
Feb 2024.

Verdict: REGISTER-CONDITIONED ASYMMETRY. The trilogy is real within-writer
adversarial escalation on Meta in the privacy-editorial register (illustrative
delta -0.90 vs the same-window Apple product-news arm), and it postdates the
data-integrity correction's fair-journalist verdict. The escalation does NOT
overturn that verdict - it bounds it: the adversarial register is confined to
the privacy-editorial lane while the product-review lane stays
balanced-to-positive on Meta itself; each trilogy item has a genuine
adversarial news peg; no equivalent adversarial news peg existed for
Samsung/Google glasses, so the missing counterfactual is untestable.

Model update: mechanism #75's bifurcation thesis is refined into a
register-conditioned model - the same journalist is fair in product register
and adversarial in privacy register, and the privacy register activates on
real events. EXTENDS #75; REFINES the Song data-integrity correction; BOUNDS
the falsification family (#538, #548, #553, #563, #568, #578, #583, #588,
#608, #613). NOT a falsification-family member; NOT a pure asymmetry pin.

All tone values are MANUAL ILLUSTRATIVE per the Aug 28 2026 standing rule.
p_value / cohens_d / ci_95 are NOT_CALCULATED; is_significant is false.
correlation_not_causation. No em dashes anywhere in this file.
"""
import re

import pytest
import yaml

ITERATION = 618
MECHANISM_ID = 605
BLOCK_KEY = "type_b_618_victoria_song_jul2026_escalation_audit"

BUZZSUMO_PROFILE = "https://buzzsumo.com/journalist/victoria-song-16465716/"
MUCKRACK_ARTICLES = "https://muckrack.com/victoria-song/articles"
AIVANET_MIRROR = ("https://www.aivanet.com/2026/07/"
                  "with-smart-glasses-meta-holds-all-the-cards-but-fails-to-play-them-well/")
SAMSUNG_MIRROR = ("https://worldofsoftware.org/samsung-galaxy-xr-hands-on-"
                  "its-like-a-cheaper-apple-vision-pro-and-launches-today/")
SAMSUNG_YOUTUBE = "https://www.youtube.com/watch?v=qq7YVwl11vY"
WIKIPEDIA_ANDROID_XR = "https://en.wikipedia.org/wiki/Android_XR"


@pytest.fixture(scope="module")
def profiles():
    with open("profiles/careers/journalists.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def entry(profiles):
    matches = [j for j in profiles["journalists"]
               if j.get("name") == "Victoria Song"]
    assert len(matches) == 1, f"expected exactly one Victoria Song entry, got {len(matches)}"
    return matches[0]


@pytest.fixture(scope="module")
def mechanism(entry):
    cc = entry.get("competitor_coverage", {})
    assert BLOCK_KEY in cc, f"{BLOCK_KEY} missing from Victoria Song competitor_coverage"
    return cc[BLOCK_KEY]


@pytest.fixture(scope="module")
def trilogy(mechanism):
    return mechanism["meta_trilogy_jul2026"]


@pytest.fixture(scope="module")
def arms(mechanism):
    return {a["entity"]: a for a in mechanism["competitor_arms"]}


@pytest.fixture(scope="module")
def scorer(mechanism):
    return mechanism["asymmetry_scorer_result_illustrative"]


class TestIterationMetadata618:
    def test_iteration_number(self, mechanism):
        assert mechanism["iteration"] == ITERATION

    def test_mechanism_id(self, mechanism):
        assert mechanism["mechanism_id"] == MECHANISM_ID

    def test_date(self, mechanism):
        assert mechanism["date"] == "2026-09-08 21:00 PDT"

    def test_hour_type_b(self, mechanism):
        assert mechanism["type"] == "B"

    def test_job_and_goal(self, mechanism):
        assert mechanism["job_id"] == "mediascope-daily-iteration"
        assert mechanism["goal_id"] == "goal_54093bda4145"


class TestJournalistEntry618:
    def test_entry_name(self, entry):
        assert entry["name"] == "Victoria Song"

    def test_wearables_beat_noted(self, entry):
        assert "wearables" in entry["notes"].lower()

    def test_verge_senior_reviewer(self, entry):
        assert "The Verge" in entry["notes"]

    def test_single_entry_no_duplicates(self, profiles):
        matches = [j for j in profiles["journalists"]
                   if j.get("name") == "Victoria Song"]
        assert len(matches) == 1


class TestMetaTrilogyJul2026:
    def test_three_items(self, trilogy):
        assert len(trilogy) == 3

    def test_jul7_led_tamper(self, trilogy):
        item = trilogy[0]
        assert item["date"] == "2026-07-07"
        assert item["author"] == "Victoria Song"
        assert item["manual_illustrative_tone"] == -0.55
        assert "privacy light" in item["title"]

    def test_jul20_pervert_glasses(self, trilogy):
        item = trilogy[1]
        assert item["date"] == "2026-07-20"
        assert item["manual_illustrative_tone"] == -0.6
        assert "pervert glasses" in item["title"]
        assert "Del Vecchio" in item["note"]

    def test_jul27_holds_all_cards(self, trilogy):
        item = trilogy[2]
        assert item["date"] == "2026-07-27"
        assert item["manual_illustrative_tone"] == -0.5
        assert "holds all the cards" in item["title"]
        assert "mass surveillance predator glasses" in item["note"]

    def test_trilogy_avg(self, trilogy):
        tones = [t["manual_illustrative_tone"] for t in trilogy]
        assert sum(tones) / len(tones) == pytest.approx(-0.55)


class TestAppleArmJul13:
    def test_apple_arm_present(self, arms):
        assert "apple" in arms

    def test_same_window(self, arms):
        assert arms["apple"]["date"] == "2026-07-13"

    def test_aspirational_tone(self, arms):
        assert arms["apple"]["manual_illustrative_tone"] == 0.35

    def test_title_bounded_listing(self, arms):
        assert "wrist computer" in arms["apple"]["title"]
        assert arms["apple"]["evidence_tier"] == "title_listing_buzzsumo_this_run"


class TestSamsungArmOct2025:
    def test_samsung_arm_present(self, arms):
        assert "samsung" in arms

    def test_hands_on_register(self, arms):
        assert arms["samsung"]["register"] == "hands_on_product_forward"

    def test_mirror_url_verbatim(self, arms):
        assert SAMSUNG_MIRROR in arms["samsung"]["note"]

    def test_zero_privacy_vocabulary(self, arms):
        assert "Zero privacy vocabulary" in arms["samsung"]["note"]


class TestGoogleArmDec2024:
    def test_google_arm_present(self, arms):
        assert "google" in arms

    def test_jarvis_comparison(self, arms):
        assert "J.A.R.V.I.S." in arms["google"]["note"]

    def test_timing_skew_recorded(self, arms):
        assert "19 months" in arms["google"]["note"]


class TestMetaPositiveArms:
    def test_meta_positive_arm_present(self, arms):
        assert "meta_positive" in arms

    def test_display_praise(self, arms):
        assert arms["meta_positive"]["manual_illustrative_tone"] == 0.3

    def test_better_than_apple_arm(self, arms):
        assert "BETTER than Apple" in arms["meta_positive"]["note"]

    def test_coexistence_is_evidence(self, arms):
        assert "core evidence for the register-conditioned model" in arms["meta_positive"]["note"]


class TestIllustrativeDelta618:
    def test_delta_convention(self, scorer):
        assert scorer["correlation_not_causation"] is True

    def test_meta_avg(self, scorer):
        assert scorer["meta_trilogy_avg"] == pytest.approx(-0.55)

    def test_apple_arm(self, scorer):
        assert scorer["apple_jul13_arm"] == 0.35

    def test_delta_arithmetic(self, scorer):
        assert scorer["delta_meta_minus_apple_jul2026_window"] == pytest.approx(-0.90)

    def test_register_gradient_framing(self, scorer):
        assert "REGISTER gradient" in scorer["note"]


class TestScorerDiscipline618:
    def test_p_value_not_calculated(self, scorer):
        assert scorer["p_value"] == "NOT_CALCULATED"

    def test_cohens_not_calculated(self, scorer):
        assert scorer["cohens_d"] == "NOT_CALCULATED"

    def test_ci_not_calculated(self, scorer):
        assert scorer["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self, scorer):
        assert scorer["is_significant"] is False

    def test_manual_illustrative_only(self, scorer):
        assert "MANUAL ILLUSTRATIVE ONLY" in scorer["note"]

    def test_no_engine_t_claims(self, scorer):
        for key in ("engine_t", "engine_welch_t", "t_stat"):
            assert key not in scorer


class TestConfounders618:
    def test_five_confounders(self, mechanism):
        assert len(mechanism["confounders_ranked"]) == 5

    def test_strength_tags(self, mechanism):
        strengths = [c["strength"] for c in mechanism["confounders_ranked"]]
        assert strengths == ["STRONG", "STRONG", "MODERATE", "MODERATE", "WEAK"]

    def test_genre_skew_strong(self, mechanism):
        first = mechanism["confounders_ranked"][0]["text"]
        assert "Genre skew" in first

    def test_news_peg_skew_strong(self, mechanism):
        second = mechanism["confounders_ranked"][1]["text"]
        assert "News-peg skew" in second
        assert "EHE guerrilla campaign" in second

    def test_missing_counterfactual_untestable(self, mechanism):
        assert "untestable" in mechanism["verdict"]


class TestRegisterConditionedVerdict618:
    def test_verdict_label(self, mechanism):
        assert mechanism["verdict"].startswith("REGISTER-CONDITIONED ASYMMETRY")

    def test_extends_75(self, mechanism):
        assert "EXTENDS #75" in mechanism["verdict"]

    def test_refines_correction(self, mechanism):
        assert "REFINES the Song data-integrity correction" in mechanism["verdict"]

    def test_bounds_falsification_family(self, mechanism):
        assert "BOUNDS the falsification family" in mechanism["verdict"]

    def test_not_falsification_member(self, mechanism):
        assert "NOT a falsification-family member" in mechanism["verdict"]

    def test_not_pure_asymmetry_pin(self, mechanism):
        assert "NOT a pure asymmetry pin" in mechanism["verdict"]


class TestNoveltyAndCrossRefs618:
    def test_block_key(self, mechanism):
        assert mechanism["block_key"] == BLOCK_KEY

    def test_novelty_free_mechanism(self, mechanism):
        assert "next free profiles mechanism id" in mechanism["novelty"]
        assert "max pre-commit 604" in mechanism["novelty"]

    def test_distinct_from_75_and_599(self, mechanism):
        assert "Distinct from mechanism #75" in mechanism["novelty"]
        assert "#599 Type C pin" in mechanism["novelty"]

    def test_cross_refs_include_buzzsumo_muckrack(self, mechanism):
        refs = " ".join(mechanism["cross_refs"])
        assert BUZZSUMO_PROFILE in refs
        assert MUCKRACK_ARTICLES in refs

    def test_no_em_dashes_in_mechanism(self, mechanism):
        text = str(mechanism)
        assert "\u2014" not in text, "em dash found in mechanism YAML"

    def test_artifact_readiness_no_update(self, mechanism):
        assert mechanism["artifact_readiness"].startswith("No analysis.json update warranted")

    def test_author_attribution(self, mechanism):
        assert mechanism["author"] == "Kit (with Ray)"


class TestRotationCycleGuard618:
    """Covers the 614-618 main-commit window (B,A,E,D,C newest-first),
    closing the A->B edge. ANCHOR PATCHED POST-COMMIT per the #565 followup
    convention: the expected anchor commit id is filled in the followup run
    after the main commit is created."""
    EXPECTED_WINDOW_NEWEST_FIRST = [
        ("Type B", 618),
        ("Type A", 617),
        ("Type E", 616),
        ("Type D", 615),
        ("Type C", 614),
    ]
    # Anchor: patched in followup - see iteration-log entry for #618.
    ANCHOR_MAIN_COMMIT = "PENDING_FOLLOWUP_PATCH"

    def test_window_sequence(self):
        seq = [(t, n) for t, n in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert seq[0] == ("Type B", 618)
        assert seq[-1] == ("Type C", 614)

    def test_closes_a_to_b_edge(self):
        types = [t for t, _ in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert types[0] == "Type B" and types[1] == "Type A"

    def test_five_window_members(self):
        assert len(self.EXPECTED_WINDOW_NEWEST_FIRST) == 5

    def test_anchor_patched_post_commit(self):
        assert self.ANCHOR_MAIN_COMMIT is not None and self.ANCHOR_MAIN_COMMIT != "PENDING_FOLLOWUP_PATCH"


def test_no_em_dashes_in_test_file():
    import pathlib
    text = pathlib.Path(__file__).read_text(encoding="utf-8")
    assert "\u2014" not in text, "em dash found in test file"
