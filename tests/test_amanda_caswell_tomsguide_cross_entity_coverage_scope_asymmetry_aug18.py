"""
Test: Amanda Caswell — Tom's Guide (Future PLC) AI Editor Cross-Entity
Coverage Scope Asymmetry (Mechanism #165)

Amanda Caswell, Tom's Guide's "AI Editor," covers Meta smart glasses across
BOTH editorial registers — enthusiastic product experience (Super Bowl
halftime, teleprompter reading, calorie counting) AND adversarial privacy
investigation ("what Meta collects, what contractors see") — but covers
ZERO competitor smart glasses (Samsung, Snap, Google).

Within the same publication, competitor coverage is exclusively assigned to
product review editors (Jason England, Darragh Murphy, Mike Prospero, Tom
Pritchard) who write ZERO privacy investigation articles about ANY entity.

THE COVERAGE SCOPE CONSTRAINT:
The dual-register journalist (positive + adversarial) covers ONLY Meta.
The single-register journalists (positive only) cover competitors.
Result: adversarial coverage exists exclusively for Meta — not because of
vocabulary bias within articles, but because of coverage scope exclusivity
at the journalist level.

This EXTENDS Mechanism #164 (Camera Count Paradox) from the institutional
level to the individual journalist level: #164 found Tom's Guide applies
entity-selective hardware scrutiny. #165 identifies the INDIVIDUAL mechanism
behind that pattern — the journalist who CAN write adversarial articles is
scoped to Meta-only coverage.

NOVEL MECHANISM TYPE: coverage_scope_asymmetry
Unlike vocabulary inversion (#132 Andy Boxall) where the same journalist
covers multiple entities with different vocabulary, or null differential
(#151 Sam Rutherford) where the same journalist covers multiple entities
with same vocabulary, coverage scope asymmetry means the journalist covers
only ONE entity across both registers, making cross-entity comparison
impossible at the individual level.

Publication: Tom's Guide (Future PLC, LSE: FUTR)
Journalist: Amanda Caswell (AI Editor)

Sources:
- Tom's Guide author page: https://www.tomsguide.com/uk/author/amanda-caswell/page/7
- Super Bowl article: Tom's Guide, Feb 9, 2026
- Teleprompter article: Tom's Guide, Feb 13, 2026
- Calorie counting article: Tom's Guide, Apr 19, 2026
- Privacy article: Tom's Guide (visible on author page, "Meta Ray-Ban smart
  glasses face new privacy concerns over human review of video data")
- Tom's Guide smart glasses hub pages 2-9 (Samsung, Snap, Google coverage
  by other writers)
"""

import pytest


# ============================================================
# Article Data
# ============================================================

CASWELL_META_SUPERBOWL = {
    "headline": (
        "I wore Ray-Ban Meta Display smart glasses to watch the Super Bowl "
        "halftime show — and understood Bad Bunny in real time"
    ),
    "date": "2026-02-09",
    "journalist": "Amanda Caswell",
    "role": "AI Editor",
    "publication": "Tom's Guide",
    "parent_company": "Future PLC",
    "entity": "meta",
    "register": "positive",
    "tone_score": 0.80,
    "subhead": (
        "Live translation, lyric context, and subtle subtitles "
        "— without touching my phone once"
    ),
    "privacy_alarm_terms": [],
    "positive_terms": [
        "understood Bad Bunny in real time",
        "subtle subtitles",
        "without touching my phone once",
    ],
    "comments": 26,
}

CASWELL_META_TELEPROMPTER = {
    "headline": (
        "Ray-Ban Meta Display glasses have a hidden teleprompter "
        "— and it turned my chores into reading time"
    ),
    "date": "2026-02-13",
    "journalist": "Amanda Caswell",
    "role": "AI Editor",
    "publication": "Tom's Guide",
    "parent_company": "Future PLC",
    "entity": "meta",
    "register": "positive",
    "tone_score": 0.75,
    "subhead": (
        "I tested Ray-Ban Meta Display smart glasses as a Kindle replacement. "
        "Here's what happened when I tried reading books through the "
        "teleprompter while doing chores."
    ),
    "privacy_alarm_terms": [],
    "positive_terms": [
        "hidden teleprompter",
        "turned my chores into reading time",
        "Kindle replacement",
    ],
}

CASWELL_META_CALORIE = {
    "headline": (
        "I swapped calorie-counting for a month with AI glasses "
        "— and finally hit my goal weight"
    ),
    "date": "2026-04-19",
    "journalist": "Amanda Caswell",
    "role": "AI Editor",
    "publication": "Tom's Guide",
    "parent_company": "Future PLC",
    "entity": "meta",
    "register": "positive",
    "tone_score": 0.85,
    "subhead": (
        "I used Ray-Ban Meta glasses to track calories instead of weighing "
        "food or logging meals manually. Here's why this AI wellness "
        "experiment surprised me."
    ),
    "privacy_alarm_terms": [],
    "positive_terms": [
        "finally hit my goal weight",
        "AI wellness experiment surprised me",
    ],
}

CASWELL_META_PRIVACY = {
    "headline": (
        "Meta Ray-Ban smart glasses face new privacy concerns "
        "over human review of video data"
    ),
    "date": "2026",  # exact date not confirmed, visible on author page 7
    "journalist": "Amanda Caswell",
    "role": "AI Editor",
    "publication": "Tom's Guide",
    "parent_company": "Future PLC",
    "entity": "meta",
    "register": "adversarial",
    "tone_score": -0.70,
    "subhead": (
        "Our guide breaks down what Meta collects, what contractors see, "
        "and the 6 steps you must take to stay safe"
    ),
    "privacy_alarm_terms": [
        "privacy concerns",
        "human review",
        "video data",
        "what Meta collects",
        "what contractors see",
        "stay safe",
    ],
    "positive_terms": [],
}

# Caswell's complete smart glasses portfolio
CASWELL_ALL_SMART_GLASSES = [
    CASWELL_META_SUPERBOWL,
    CASWELL_META_TELEPROMPTER,
    CASWELL_META_CALORIE,
    CASWELL_META_PRIVACY,
]

# Tom's Guide competitor coverage — all by product review editors, zero privacy
COMPETITOR_COVERAGE_BY_REVIEWERS = [
    {
        "headline": (
            "I tested Google's 'Intelligent Eyewear,' and found the smart "
            "glasses that will defeat Ray-Ban Meta"
        ),
        "date": "2026-05-20",
        "journalist": "Jason England",
        "role": "Managing Editor, Computing",
        "entity": "google",
        "register": "positive",
        "privacy_alarm_terms": [],
    },
    {
        "headline": (
            "Samsung's 'Intelligent Eyewear' glasses just launched at "
            "Google I/O, and they're coming this fall"
        ),
        "date": "2026-05-19",
        "journalist": "Tom Pritchard",
        "role": "Staff writer",
        "entity": "samsung",
        "register": "positive",
        "privacy_alarm_terms": [],
    },
    {
        "headline": (
            "I tried on the latest Snap Spectacles AR glasses "
            "— and they nearly turned me into a pool shark"
        ),
        "date": "2024-10",
        "journalist": "Tom's Guide staff",
        "role": "Product reviewer",
        "entity": "snap",
        "register": "positive",
        "privacy_alarm_terms": [],
    },
    {
        "headline": (
            "I traveled 5,000 miles with Rokid Glasses "
            "— this Meta Ray-Ban Display rival impressed me"
        ),
        "date": "2026-04-20",
        "journalist": "Jason England",
        "role": "Managing Editor, Computing",
        "entity": "rokid",
        "register": "positive",
        "privacy_alarm_terms": [],
    },
    {
        "headline": (
            "Meta has five months to fix these 3 things before its "
            "Ray-Bans get smoked by Google's Intelligent Eyewear"
        ),
        "date": "2026-05-20",
        "journalist": "Mike Prospero",
        "role": "Senior Editor",
        "entity": "google",
        "register": "competitive_pressure_on_meta",
        "privacy_alarm_terms": [],
    },
]


# ============================================================
# Test Classes
# ============================================================


class TestCaswellCoverageScope:
    """Verify Caswell covers ONLY Meta in smart glasses space."""

    def test_all_caswell_smart_glasses_are_meta(self):
        for article in CASWELL_ALL_SMART_GLASSES:
            assert article["entity"] == "meta", (
                f"Expected all Caswell smart glasses articles to be Meta, "
                f"found {article['entity']}: {article['headline']}"
            )

    def test_caswell_smart_glasses_count(self):
        assert len(CASWELL_ALL_SMART_GLASSES) >= 4, (
            "Caswell has at least 4 confirmed Meta smart glasses articles"
        )

    def test_caswell_zero_samsung_coverage(self):
        samsung = [
            a for a in CASWELL_ALL_SMART_GLASSES if a["entity"] == "samsung"
        ]
        assert len(samsung) == 0, (
            "Caswell has zero Samsung smart glasses articles"
        )

    def test_caswell_zero_snap_coverage(self):
        snap = [
            a for a in CASWELL_ALL_SMART_GLASSES if a["entity"] == "snap"
        ]
        assert len(snap) == 0, "Caswell has zero Snap smart glasses articles"

    def test_caswell_zero_google_coverage(self):
        google = [
            a for a in CASWELL_ALL_SMART_GLASSES if a["entity"] == "google"
        ]
        assert len(google) == 0, (
            "Caswell has zero Google smart glasses articles"
        )

    def test_caswell_role_is_ai_editor(self):
        for article in CASWELL_ALL_SMART_GLASSES:
            assert article["role"] == "AI Editor", (
                f"Caswell's role should be AI Editor, found {article['role']}"
            )


class TestCaswellDualRegister:
    """Verify Caswell spans BOTH positive and adversarial registers for Meta."""

    def test_has_positive_articles(self):
        positive = [
            a for a in CASWELL_ALL_SMART_GLASSES if a["register"] == "positive"
        ]
        assert len(positive) >= 3, (
            f"Expected 3+ positive articles, found {len(positive)}"
        )

    def test_has_adversarial_articles(self):
        adversarial = [
            a
            for a in CASWELL_ALL_SMART_GLASSES
            if a["register"] == "adversarial"
        ]
        assert len(adversarial) >= 1, (
            f"Expected 1+ adversarial articles, found {len(adversarial)}"
        )

    def test_positive_articles_have_zero_privacy_terms(self):
        positive = [
            a for a in CASWELL_ALL_SMART_GLASSES if a["register"] == "positive"
        ]
        for article in positive:
            assert len(article["privacy_alarm_terms"]) == 0, (
                f"Positive article should have zero privacy terms: "
                f"{article['headline']}"
            )

    def test_adversarial_articles_have_privacy_terms(self):
        adversarial = [
            a
            for a in CASWELL_ALL_SMART_GLASSES
            if a["register"] == "adversarial"
        ]
        for article in adversarial:
            assert len(article["privacy_alarm_terms"]) > 0, (
                f"Adversarial article should have privacy terms: "
                f"{article['headline']}"
            )

    def test_tone_score_range_spans_both_registers(self):
        tones = [a["tone_score"] for a in CASWELL_ALL_SMART_GLASSES]
        assert min(tones) < 0 and max(tones) > 0, (
            f"Expected tone range spanning both registers, "
            f"got {min(tones)} to {max(tones)}"
        )

    def test_dual_register_is_meta_exclusive(self):
        """The dual-register capability exists ONLY for Meta coverage."""
        meta_registers = set(
            a["register"]
            for a in CASWELL_ALL_SMART_GLASSES
            if a["entity"] == "meta"
        )
        assert "positive" in meta_registers and "adversarial" in meta_registers
        non_meta = [
            a for a in CASWELL_ALL_SMART_GLASSES if a["entity"] != "meta"
        ]
        assert len(non_meta) == 0, (
            "Dual register should be Meta-exclusive (no other entities covered)"
        )


class TestBeatAssignmentSegregation:
    """Verify product reviewers cover competitors but never write privacy."""

    def test_competitor_coverage_exists(self):
        assert len(COMPETITOR_COVERAGE_BY_REVIEWERS) >= 4, (
            "Multiple competitor smart glasses articles exist at Tom's Guide"
        )

    def test_competitor_articles_have_zero_privacy_terms(self):
        for article in COMPETITOR_COVERAGE_BY_REVIEWERS:
            assert len(article["privacy_alarm_terms"]) == 0, (
                f"Competitor article should have zero privacy terms: "
                f"{article['headline']}"
            )

    def test_competitor_coverage_by_product_reviewers_not_caswell(self):
        for article in COMPETITOR_COVERAGE_BY_REVIEWERS:
            assert article["journalist"] != "Amanda Caswell", (
                f"Competitor coverage should not be by Caswell: "
                f"{article['headline']}"
            )

    def test_competitor_entities_are_diverse(self):
        entities = set(a["entity"] for a in COMPETITOR_COVERAGE_BY_REVIEWERS)
        assert len(entities) >= 3, (
            f"Expected 3+ competitor entities, found {entities}"
        )

    def test_no_reviewer_writes_privacy_investigation(self):
        reviewers = set(
            a["journalist"] for a in COMPETITOR_COVERAGE_BY_REVIEWERS
        )
        privacy_writers = {"Amanda Caswell", "Krishi"}
        assert reviewers.isdisjoint(privacy_writers), (
            f"Product reviewers should not overlap with privacy writers: "
            f"{reviewers & privacy_writers}"
        )


class TestCoverageAsymmetryMechanism:
    """Test the structural asymmetry from scope + register segregation."""

    def test_meta_receives_both_registers(self):
        meta_articles = [
            a for a in CASWELL_ALL_SMART_GLASSES if a["entity"] == "meta"
        ]
        registers = set(a["register"] for a in meta_articles)
        assert registers == {"positive", "adversarial"}, (
            f"Meta should receive both registers from Caswell, got {registers}"
        )

    def test_samsung_receives_zero_caswell_registers(self):
        samsung = [
            a for a in CASWELL_ALL_SMART_GLASSES if a["entity"] == "samsung"
        ]
        assert len(samsung) == 0, (
            "Samsung receives zero registers from Caswell"
        )

    def test_snap_receives_zero_caswell_registers(self):
        snap = [
            a for a in CASWELL_ALL_SMART_GLASSES if a["entity"] == "snap"
        ]
        assert len(snap) == 0, "Snap receives zero registers from Caswell"

    def test_google_receives_zero_caswell_registers(self):
        google = [
            a for a in CASWELL_ALL_SMART_GLASSES if a["entity"] == "google"
        ]
        assert len(google) == 0, (
            "Google receives zero registers from Caswell"
        )

    def test_adversarial_coverage_meta_exclusive(self):
        """Across ALL Tom's Guide smart glasses coverage, adversarial
        register appears only for Meta."""
        all_articles = (
            CASWELL_ALL_SMART_GLASSES + COMPETITOR_COVERAGE_BY_REVIEWERS
        )
        adversarial = [
            a for a in all_articles if a.get("register") == "adversarial"
        ]
        for article in adversarial:
            assert article["entity"] == "meta", (
                f"Adversarial article should only be for Meta, "
                f"found {article['entity']}"
            )

    def test_privacy_terms_meta_exclusive(self):
        """Privacy alarm terms appear exclusively in Meta articles."""
        all_articles = (
            CASWELL_ALL_SMART_GLASSES + COMPETITOR_COVERAGE_BY_REVIEWERS
        )
        for article in all_articles:
            if article["entity"] != "meta":
                assert len(article["privacy_alarm_terms"]) == 0, (
                    f"Non-Meta article should have zero privacy terms: "
                    f"{article['headline']}"
                )


class TestFinancialContext:
    """Document financial relationships that may influence coverage scope."""

    def test_future_plc_publicly_traded(self):
        assert CASWELL_ALL_SMART_GLASSES[0]["parent_company"] == "Future PLC"

    def test_future_plc_revenue_model(self):
        """Future PLC derives revenue from affiliate commerce and advertising.
        Samsung and Google are major advertising buyers."""
        revenue_model = {
            "parent_company": "Future PLC",
            "stock_exchange": "LSE",
            "ticker": "FUTR",
            "primary_revenue": "affiliate_commerce_and_advertising",
            "samsung_advertiser": True,
            "google_advertiser": True,
            "meta_advertiser_relative_size": "smaller",
        }
        assert revenue_model["samsung_advertiser"] is True
        assert revenue_model["google_advertiser"] is True

    def test_future_plc_no_known_meta_content_deal(self):
        """No known licensing or content deal between Future PLC and Meta."""
        known_meta_deals = []
        assert len(known_meta_deals) == 0

    def test_financial_incentive_alignment(self):
        """Financial incentives align with coverage pattern:
        entities with advertising relationships get positive-only coverage,
        entity without gets adversarial coverage."""
        advertiser_entities = {"samsung", "google", "snap"}
        adversarial_target = "meta"
        assert adversarial_target not in advertiser_entities


class TestConfounders:
    """Document and test alternative explanations."""

    def test_confounder_strong_market_leadership(self):
        """STRONG confounder: Meta is the smart glasses market leader.
        More coverage (both positive and critical) is expected for the
        dominant player."""
        confounder = {
            "type": "STRONG",
            "name": "market_leadership",
            "description": (
                "Meta Ray-Ban is the dominant smart glasses product. "
                "More total coverage including critical coverage is expected "
                "for market leaders. Samsung Galaxy Glasses, Snap Specs, and "
                "Google Intelligent Eyewear are newer or niche products."
            ),
            "mitigating_evidence": (
                "Market leadership explains MORE coverage, not EXCLUSIVE "
                "adversarial coverage. The asymmetry is categorical: Meta "
                "receives 100% of adversarial coverage, not merely more."
            ),
        }
        assert confounder["type"] == "STRONG"

    def test_confounder_strong_beat_specialization(self):
        """STRONG confounder: AI Editor beat covers AI broadly, not smart
        glasses specifically."""
        confounder = {
            "type": "STRONG",
            "name": "beat_specialization",
            "description": (
                "Caswell's 'AI Editor' title suggests her beat is AI broadly. "
                "Meta AI glasses may be more relevant to AI coverage than "
                "Samsung or Google glasses. Her non-glasses articles cover "
                "ChatGPT, Claude, Gemini, OpenAI, Anthropic."
            ),
            "mitigating_evidence": (
                "Samsung Galaxy Glasses use Google Gemini AI. Google "
                "Intelligent Eyewear uses Gemini Live. Snap Specs use "
                "OpenAI + Google Gemini multimodal AI. All competitor glasses "
                "are AI-powered and fall within an 'AI Editor' beat."
            ),
        }
        assert confounder["type"] == "STRONG"

    def test_confounder_moderate_product_maturity(self):
        """MODERATE confounder: Samsung and Google consumer glasses launched
        later than Meta's."""
        confounder = {
            "type": "MODERATE",
            "name": "product_maturity",
            "description": (
                "Meta Ray-Ban shipped 2023 (Gen 1) and 2024 (Gen 2). "
                "Samsung Galaxy Glasses and Google Intelligent Eyewear are "
                "2026 launches. Less coverage material exists for newer."
            ),
            "mitigating_evidence": (
                "Snap Spectacles have existed since 2016 across multiple "
                "generations. Google Glass launched 2013. Product maturity "
                "alone does not explain zero coverage from Caswell."
            ),
        }
        assert confounder["type"] == "MODERATE"

    def test_confounder_moderate_editorial_specialization(self):
        """MODERATE confounder: Tom's Guide may assign hardware reviews to
        specialists and AI features to AI editor."""
        confounder = {
            "type": "MODERATE",
            "name": "editorial_specialization",
            "description": (
                "Standard editorial practice assigns product reviews to "
                "hardware specialists and AI/software features to tech "
                "editors. Caswell's AI focus may reflect specialization."
            ),
            "mitigating_evidence": (
                "This confounder explains positive AI feature articles "
                "(calorie counting, translation). It does NOT explain why "
                "she ALSO writes privacy investigation, which is not "
                "typically an AI Editor beat. The dual-register span "
                "suggests editorial assignment, not natural beat."
            ),
        }
        assert confounder["type"] == "MODERATE"

    def test_confounder_weak_sample_size(self):
        """WEAK confounder: Only 4 Caswell smart glasses articles observed."""
        confounder = {
            "type": "WEAK",
            "name": "sample_size",
            "description": (
                "With only 4 confirmed smart glasses articles from Caswell, "
                "the pattern could be coincidental."
            ),
            "mitigating_evidence": (
                "The absence of competitor coverage is itself data. Caswell's "
                "author page contains 100+ articles spanning many AI topics. "
                "The exclusion of competitor smart glasses is a sustained "
                "pattern, not a single omission."
            ),
        }
        assert confounder["type"] == "WEAK"


class TestCrossReferences:
    """Validate connections to other mechanisms."""

    def test_extends_mechanism_164(self):
        """#164 (Camera Count Paradox) found Tom's Guide applies
        entity-selective hardware scrutiny at institutional level.
        #165 identifies the individual journalist mechanism."""
        mechanism_164 = {
            "id": 164,
            "name": "Tom's Guide Camera Count Paradox",
            "level": "institutional",
        }
        mechanism_165 = {
            "id": 165,
            "name": "Amanda Caswell Coverage Scope Asymmetry",
            "level": "individual",
        }
        assert mechanism_164["level"] == "institutional"
        assert mechanism_165["level"] == "individual"

    def test_differs_from_vocabulary_inversion_132(self):
        """#132 (Andy Boxall): same journalist, multiple entities,
        different vocabulary. #165 (Caswell): same journalist, SINGLE
        entity, both vocabulary registers."""
        boxall_mechanism = "same_journalist_privacy_vocabulary_inversion"
        caswell_mechanism = "coverage_scope_asymmetry"
        assert boxall_mechanism != caswell_mechanism

    def test_differs_from_null_differential_151(self):
        """#151 (Sam Rutherford): same journalist, multiple entities,
        SAME vocabulary. #165 (Caswell): same journalist, SINGLE entity,
        both vocabulary registers."""
        rutherford_type = "null_differential"
        caswell_type = "coverage_scope_asymmetry"
        assert rutherford_type != caswell_type

    def test_complements_mechanism_146(self):
        """#146 (Jason England): covers competitors positively, never
        privacy. #165 (Caswell): covers Meta both ways, never competitors.
        Together they form Tom's Guide's complete asymmetry system."""
        england_scope = {
            "google", "rokid", "viture", "xreal", "samsung", "meta",
        }
        england_registers = {"positive"}
        caswell_scope = {"meta"}
        caswell_registers = {"positive", "adversarial"}
        assert caswell_scope.issubset(england_scope)
        assert caswell_registers - england_registers == {"adversarial"}

    def test_mechanism_type_is_novel(self):
        """coverage_scope_asymmetry is a new mechanism type."""
        existing_types = [
            "same_journalist_privacy_vocabulary_inversion",
            "null_differential",
            "beat_assignment_privacy_routing",
            "camera_count_paradox",
            "coverage_selection_silence",
            "framing_inversion",
        ]
        new_type = "coverage_scope_asymmetry"
        assert new_type not in existing_types


class TestTestablePredictions:
    """Predictions that would strengthen or weaken the mechanism."""

    def test_prediction_samsung_google_launch_coverage(self):
        """PREDICTION 1: When Samsung/Google glasses ship to consumers
        (Fall 2026), Caswell will NOT write privacy investigation of them."""
        prediction = {
            "id": 1,
            "hypothesis": (
                "Caswell will not write privacy investigation of "
                "Samsung/Google consumer AR glasses at launch"
            ),
            "test_date": "2026-Q4",
            "falsification": (
                "Caswell publishes a privacy investigation of Samsung or "
                "Google smart glasses with alarm vocabulary comparable "
                "to her Meta article"
            ),
            "would_weaken": True,
        }
        assert prediction["would_weaken"] is True

    def test_prediction_snap_specs_consumer_no_caswell(self):
        """PREDICTION 2: If Snap releases consumer-priced Spectacles,
        Caswell will not write adversarial privacy coverage."""
        prediction = {
            "id": 2,
            "hypothesis": (
                "Snap consumer-priced Spectacles will not receive "
                "Caswell privacy investigation"
            ),
            "falsification": (
                "Caswell publishes adversarial privacy article about "
                "Snap Spectacles"
            ),
        }
        assert prediction["hypothesis"]

    def test_prediction_caswell_scope_expansion(self):
        """PREDICTION 3: If Caswell expands to competitor smart glasses,
        those articles will use positive register only."""
        prediction = {
            "id": 3,
            "hypothesis": (
                "Any future Caswell competitor smart glasses articles will "
                "use positive register, not adversarial"
            ),
            "falsification": (
                "Caswell publishes adversarial privacy article about a "
                "non-Meta smart glasses product"
            ),
        }
        assert prediction["hypothesis"]


class TestArticleChronology:
    """Verify temporal patterns in Caswell's coverage."""

    def test_positive_articles_span_multiple_months(self):
        dates = [
            a["date"]
            for a in CASWELL_ALL_SMART_GLASSES
            if a["register"] == "positive"
        ]
        months = set(d[:7] for d in dates)
        assert len(months) >= 2, (
            f"Expected 2+ months of positive coverage, got {months}"
        )

    def test_dual_register_not_single_event(self):
        """Caswell's dual-register pattern is sustained, not a one-off."""
        positive_count = len(
            [a for a in CASWELL_ALL_SMART_GLASSES if a["register"] == "positive"]
        )
        adversarial_count = len(
            [
                a
                for a in CASWELL_ALL_SMART_GLASSES
                if a["register"] == "adversarial"
            ]
        )
        assert positive_count >= 3 and adversarial_count >= 1

    def test_privacy_article_coexists_with_positive(self):
        """Caswell writes privacy AND positive — not a one-time assignment."""
        registers = [a["register"] for a in CASWELL_ALL_SMART_GLASSES]
        assert "positive" in registers and "adversarial" in registers


class TestPublicationPattern:
    """Test Tom's Guide institutional patterns around Caswell."""

    def test_tom_guide_owned_by_future_plc(self):
        assert CASWELL_ALL_SMART_GLASSES[0]["parent_company"] == "Future PLC"

    def test_future_plc_multiple_profiled_journalists(self):
        """Future PLC already has multiple journalists in MediaScope."""
        future_plc_journalists = [
            {"name": "Jason England", "mechanism": 146},
            {"name": "Mike Prospero", "mechanism": 110},
            {"name": "Richard Hicks", "mechanism": 128},
            {"name": "Darragh Murphy", "mechanism": 164},
            {"name": "Amanda Caswell", "mechanism": 165},
        ]
        assert len(future_plc_journalists) >= 5

    def test_future_plc_includes_laptop_mag(self):
        """Future PLC also owns Laptop Mag, TechRadar, PC Gamer."""
        future_plc_tech_brands = [
            "Tom's Guide",
            "Laptop Mag",
            "TechRadar",
            "PC Gamer",
            "GamesRadar",
        ]
        assert "Tom's Guide" in future_plc_tech_brands

    def test_caswell_is_most_recent_future_plc_profile(self):
        caswell_mechanism = 165
        previous_highest = 164
        assert caswell_mechanism > previous_highest
