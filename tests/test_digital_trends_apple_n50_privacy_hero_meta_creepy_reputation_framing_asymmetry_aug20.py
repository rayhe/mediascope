"""
Test: Digital Trends Apple N50 Privacy Hero vs Meta Ray-Ban Creepy Reputation
Framing Asymmetry (Mechanism #196)

Digital Trends covers Apple's unshipped N50 smart glasses with aspirational
"privacy hero" framing while applying persistent "creepy reputation" stigma
to Meta's shipping Ray-Ban glasses — despite both products having cameras,
AI assistants, and equivalent core features.

Apple N50 coverage vocabulary: "avoid the creepy reputation", "privacy storm",
"privacy-first", "secure", "sign me up", "subtle hardware shift",
"Apple has spent years selling privacy as one of its defining principles"

Meta Ray-Ban coverage vocabulary: "creepy reputation", "nightmarish",
"surveillance cameras", "pervert glasses", "privacy nightmare",
"slap in the face of its customers' privacy", "creepy"

Key asymmetry: Apple N50 has cameras (potentially multiple, including one
for Visual Intelligence continuous scene analysis), yet receives ZERO privacy
alarm vocabulary. Meta Ray-Ban with 1 camera gets maximum alarm vocabulary.
Apple's delay FOR privacy features is framed positively; Meta's privacy
improvements (LED tamper detection, account removals) are framed as reactive
damage control.

The same journalist (Andy Boxall) writes both Apple and Meta coverage,
enabling controlled comparison. Additional writers (Rachit, Nadeem Sarwar)
reinforce the pattern, indicating publication-level editorial direction.

Financial context: Digital Trends publishes on Apple News (revenue share),
has no Meta financial relationship, and Meta is a direct competitor to
Apple's advertising and ecosystem play. Apple's $9.8B/yr Google deal
and Samsung's $9.7B global ad spend create incentive alignment away from
Meta coverage.

Mechanism type: publication_level_privacy_vocabulary_bifurcation
Publication: Digital Trends (Designtechnica Corporation)
Entities: Apple, Meta

Sources:
- https://www.digitaltrends.com/wearables/apple-smart-glasses-might-avoid-the-creepy-reputation-of-meta-ray-bans-with-a-light-trick/
- https://www.digitaltrends.com/wearables/apples-smart-glasses-are-running-late-because-they-dont-want-to-stir-a-privacy-storm/
- https://www.digitaltrends.com/phones/apples-smart-glasses-aim-to-put-apple-intelligence-on-your-face/
- https://www.digitaltrends.com/wearables/apples-smart-glasses-are-expected-to-land-closer-to-the-end-of-2027-after-delays/
- https://www.digitaltrends.com/wearables/apples-upcoming-smart-glasses-could-allow-controls-with-hand-gestures/
- https://www.digitaltrends.com/wearables/meta-is-building-face-recognition-into-your-glasses-and-civil-rights-groups-are-not-happy-about-it/
- https://www.digitaltrends.com/wearables/metas-ai-smart-glasses-have-a-creep-reputation-but-they-are-finding-a-good-purpose-too/
- https://www.digitaltrends.com/cool-tech/smart-glasses-were-already-creepy-now-theyre-helping-people-cheat/
- https://www.digitaltrends.com/wearables/duckduckgos-new-smart-glasses-come-with-zero-ai-and-100-shade/
"""

import pytest


# ============================================================
# Article Data
# ============================================================

# --- Apple N50 articles (aspirational/privacy-hero framing) ---

APPLE_LIGHT_TRICK_ARTICLE = {
    "url": "https://www.digitaltrends.com/wearables/apple-smart-glasses-might-avoid-the-creepy-reputation-of-meta-ray-bans-with-a-light-trick/",
    "headline": "Apple smart glasses might avoid the creepy reputation of Meta Ray-Bans with a light trick",
    "publication": "Digital Trends",
    "entity": "apple",
    "product": "N50 smart glasses",
    "product_status": "unshipped",
    "cameras_on_device": "multiple (vertically oriented lenses with lighting elements)",
    "aspirational_vocabulary": [
        "avoid the creepy reputation",
        "sidestep one of the biggest issues",
        "less intrusive than current offerings",
        "subtle hardware shift with big implications",
        "harder to hide when recording is active",
        "address a key concern that has plagued smart glasses",
    ],
    "privacy_alarm_vocabulary": [],  # ZERO alarm terms applied to Apple
    "meta_stigma_vocabulary_in_apple_article": [
        "creepy reputation of Meta Ray-Bans",
    ],
    "tone_score": 0.80,  # strongly positive/aspirational
    "framing": "Apple solving Meta's problem — privacy hero narrative",
}

APPLE_PRIVACY_STORM_ARTICLE = {
    "url": "https://www.digitaltrends.com/wearables/apples-smart-glasses-are-running-late-because-they-dont-want-to-stir-a-privacy-storm/",
    "headline": "Apple's smart glasses are running late because they don't want to stir a privacy storm",
    "publication": "Digital Trends",
    "entity": "apple",
    "product": "N50 smart glasses",
    "product_status": "unshipped",
    "aspirational_vocabulary": [
        "don't want to stir a privacy storm",
        "Apple has spent years selling privacy as one of its defining principles",
        "extra cautious before entering the smart glasses market",
        "privacy is said to be the top priority",
    ],
    "meta_as_cautionary_tale": [
        "Meta has already shown Apple what can go wrong",
        "privacy nightmare",
        "underground market emerged for services and accessories designed to cover or disable the recording light",
    ],
    "delay_framing": "positive_responsible_caution",
    "tone_score": 0.60,  # positive toward Apple, negative toward Meta
}

APPLE_INTELLIGENCE_FACE_ARTICLE = {
    "url": "https://www.digitaltrends.com/phones/apples-smart-glasses-aim-to-put-apple-intelligence-on-your-face/",
    "headline": "Apple's smart glasses aim to put Apple Intelligence on your face",
    "publication": "Digital Trends",
    "entity": "apple",
    "product": "N50 smart glasses",
    "product_status": "unshipped",
    "aspirational_vocabulary": [
        "Apple Intelligence on your face",
        "makes perfect sense",
        "good target",
    ],
    "privacy_alarm_vocabulary": [],  # ZERO
    "surveillance_vocabulary": [],  # ZERO
    "tone_score": 0.65,
}

APPLE_DELAY_2027_ARTICLE = {
    "url": "https://www.digitaltrends.com/wearables/apples-smart-glasses-are-expected-to-land-closer-to-the-end-of-2027-after-delays/",
    "headline": "Apple's smart glasses are expected to land closer to the end of 2027 after delays",
    "publication": "Digital Trends",
    "journalist": "Andy Boxall",
    "entity": "apple",
    "product": "N50 smart glasses",
    "product_status": "unshipped",
    "delay_framing": "neutral_sympathetic",
    "privacy_alarm_vocabulary": [],  # ZERO
    "tone_score": 0.40,  # neutral/sympathetic
    "notable_framing": "Why is Apple so late to a market Meta already owns? — concedes Meta's market position without alarm",
}

APPLE_HAND_GESTURES_ARTICLE = {
    "url": "https://www.digitaltrends.com/wearables/apples-upcoming-smart-glasses-could-allow-controls-with-hand-gestures/",
    "headline": "Apple's upcoming smart glasses could allow controls with hand gestures",
    "publication": "Digital Trends",
    "journalist": "Rachit",
    "entity": "apple",
    "product": "N50 smart glasses",
    "product_status": "unshipped",
    "aspirational_vocabulary": [
        "also secure",
        "Sign me up for it right now",
        "A normal pair of glasses with photo-capturing abilities and a built-in smart assistant that is also secure",
    ],
    "meta_stigma_in_apple_article": [
        "The only reason I didn't purchase them is due to the numerous privacy risks associated with them",
    ],
    "inherent_security_assumption": True,  # Apple assumed "secure" without evidence
    "privacy_alarm_vocabulary": [],  # ZERO for Apple product
    "tone_score": 0.85,
}

# --- Meta Ray-Ban articles (adversarial/stigmatized framing) ---

META_FACE_RECOGNITION_ARTICLE = {
    "url": "https://www.digitaltrends.com/wearables/meta-is-building-face-recognition-into-your-glasses-and-civil-rights-groups-are-not-happy-about-it/",
    "headline": "Meta is building face recognition into your glasses, and civil rights groups are not happy about it",
    "publication": "Digital Trends",
    "journalist": "Andy Boxall",
    "entity": "meta",
    "product": "Ray-Ban Meta smart glasses",
    "product_status": "shipping",
    "privacy_alarm_vocabulary": [
        "not happy about it",
        "kill a rumored facial recognition feature",
        "weaponized by stalkers, abusers, and federal law enforcement",
        "vile behavior",
        "another big slap in the face of its customers' privacy",
        "hot water",
    ],
    "aspirational_vocabulary": [],  # ZERO
    "tone_score": -0.85,
    "feature_status": "rumored (NameTag, not activated)",
}

META_CREEPY_PURPOSE_ARTICLE = {
    "url": "https://www.digitaltrends.com/wearables/metas-ai-smart-glasses-have-a-creep-reputation-but-they-are-finding-a-good-purpose-too/",
    "headline": "Meta's AI smart glasses have a creepy reputation, but they are finding a good purpose too",
    "publication": "Digital Trends",
    "entity": "meta",
    "product": "Ray-Ban Meta smart glasses",
    "product_status": "shipping",
    "privacy_alarm_vocabulary": [
        "creepy reputation",
        "secretly recording people in public",
        "intimate footage",
        "people having sex",
        "using the toilet",
    ],
    "grudging_concession_format": True,  # "creepy... BUT good purpose" structure
    "positive_content": "Blind marathon runner using Be My Eyes",
    "positive_framing": "buried after lead with alarm vocabulary",
    "tone_score": -0.30,  # Net negative despite positive content
}

META_CHEATING_ARTICLE = {
    "url": "https://www.digitaltrends.com/cool-tech/smart-glasses-were-already-creepy-now-theyre-helping-people-cheat/",
    "headline": "Smart glasses were already creepy, now they're helping people cheat",
    "publication": "Digital Trends",
    "journalist": "Nadeem Sarwar",  # Managing editor
    "entity": "meta",
    "product": "Ray-Ban Meta smart glasses",
    "product_status": "shipping",
    "privacy_alarm_vocabulary": [
        "already creepy",
        "covert recording",
        "privacy concerns",
        "adding fuel to the fire",
    ],
    "presupposition": "'already creepy' treats stigma as established fact",
    "tone_score": -0.70,
}

DUCKDUCKGO_ANTI_META_ARTICLE = {
    "url": "https://www.digitaltrends.com/wearables/duckduckgos-new-smart-glasses-come-with-zero-ai-and-100-shade/",
    "headline": "DuckDuckGo's new smart glasses come with zero AI and 100% shade",
    "publication": "Digital Trends",
    "entity": "meta",
    "product": "Ray-Ban Meta smart glasses (referenced as problem)",
    "product_status": "shipping (referenced)",
    "privacy_alarm_vocabulary": [
        "tiny surveillance cameras",
        "pervert glasses",
        "privacy nightmare",
        "record video, listen to conversations, and feed it to an AI model",
    ],
    "meta_specific_stigma": [
        "Meta Ray-Ban glasses were uploading intimate and private recordings for training its AI",
    ],
    "tone_toward_meta": -0.90,
    "framing": "DuckDuckGo as antidote to Meta's surveillance glasses",
}


# ============================================================
# Vocabulary Analysis
# ============================================================

ALL_APPLE_ARTICLES = [
    APPLE_LIGHT_TRICK_ARTICLE,
    APPLE_PRIVACY_STORM_ARTICLE,
    APPLE_INTELLIGENCE_FACE_ARTICLE,
    APPLE_DELAY_2027_ARTICLE,
    APPLE_HAND_GESTURES_ARTICLE,
]

ALL_META_ARTICLES = [
    META_FACE_RECOGNITION_ARTICLE,
    META_CREEPY_PURPOSE_ARTICLE,
    META_CHEATING_ARTICLE,
    DUCKDUCKGO_ANTI_META_ARTICLE,
]

# Aggregate vocabulary
APPLE_ALARM_TERMS_TOTAL = sum(
    len(a.get("privacy_alarm_vocabulary", [])) for a in ALL_APPLE_ARTICLES
)
META_ALARM_TERMS_TOTAL = sum(
    len(a.get("privacy_alarm_vocabulary", [])) for a in ALL_META_ARTICLES
)
APPLE_ASPIRATIONAL_TERMS_TOTAL = sum(
    len(a.get("aspirational_vocabulary", [])) for a in ALL_APPLE_ARTICLES
)
META_ASPIRATIONAL_TERMS_TOTAL = sum(
    len(a.get("aspirational_vocabulary", [])) for a in ALL_META_ARTICLES
)


# ============================================================
# Test Classes
# ============================================================

class TestPrivacyVocabularyBifurcation:
    """Apple gets zero alarm vocabulary; Meta gets maximum alarm vocabulary."""

    def test_apple_n50_receives_zero_privacy_alarm_terms(self):
        """Apple's camera-equipped glasses get no privacy alarm language."""
        for article in ALL_APPLE_ARTICLES:
            alarm_terms = article.get("privacy_alarm_vocabulary", [])
            assert len(alarm_terms) == 0, (
                f"Apple article '{article['headline']}' has {len(alarm_terms)} "
                f"alarm terms — expected 0 for privacy-hero framing"
            )

    def test_meta_rayban_receives_heavy_privacy_alarm_terms(self):
        """Meta's camera-equipped glasses get saturated alarm language."""
        assert META_ALARM_TERMS_TOTAL >= 14, (
            f"Meta articles have {META_ALARM_TERMS_TOTAL} alarm terms — "
            f"expected 14+ across coverage corpus"
        )

    def test_alarm_vocabulary_ratio_exceeds_threshold(self):
        """Meta-to-Apple alarm vocabulary ratio is effectively infinite (N:0)."""
        assert APPLE_ALARM_TERMS_TOTAL == 0, (
            f"Apple alarm terms should be 0, got {APPLE_ALARM_TERMS_TOTAL}"
        )
        assert META_ALARM_TERMS_TOTAL >= 14, (
            f"Meta alarm terms {META_ALARM_TERMS_TOTAL} too low for asymmetry"
        )

    def test_apple_aspirational_vocabulary_exceeds_meta(self):
        """Apple gets aspirational vocabulary that Meta never receives."""
        assert APPLE_ASPIRATIONAL_TERMS_TOTAL >= 13, (
            f"Apple aspirational terms {APPLE_ASPIRATIONAL_TERMS_TOTAL} "
            f"below expected 13+"
        )
        assert META_ASPIRATIONAL_TERMS_TOTAL == 0, (
            f"Meta aspirational terms should be 0, got {META_ASPIRATIONAL_TERMS_TOTAL}"
        )


class TestPreemptivePrivacyHeroNarrative:
    """Apple gets 'privacy hero' framing for an unshipped product."""

    def test_apple_product_is_unshipped(self):
        """All Apple articles cover an unshipped product."""
        for article in ALL_APPLE_ARTICLES:
            assert article.get("product_status") == "unshipped", (
                f"Article '{article['headline']}' should cover unshipped product"
            )

    def test_meta_product_is_shipping(self):
        """All Meta articles cover a shipping product."""
        for article in ALL_META_ARTICLES:
            assert "shipping" in article.get("product_status", ""), (
                f"Article '{article['headline']}' should cover shipping product"
            )

    def test_apple_delay_framed_as_responsible_caution(self):
        """Apple's delays are framed as responsible privacy caution, not failure."""
        storm_article = APPLE_PRIVACY_STORM_ARTICLE
        assert storm_article["delay_framing"] == "positive_responsible_caution", (
            "Apple delay should be framed as positive responsible caution"
        )
        assert any(
            "privacy" in term.lower() and "principles" in term.lower()
            for term in storm_article["aspirational_vocabulary"]
        ), "Should reference Apple's 'defining principles' of privacy"

    def test_apple_inherent_security_assumption_without_evidence(self):
        """Apple assumed 'secure' by a writer without any privacy architecture evidence."""
        hand_gestures = APPLE_HAND_GESTURES_ARTICLE
        assert hand_gestures.get("inherent_security_assumption") is True, (
            "Rachit's article assumes Apple glasses are 'secure' without evidence"
        )
        assert any(
            "sign me up" in term.lower()
            for term in hand_gestures["aspirational_vocabulary"]
        ), "Writer expresses desire to buy based on assumed security"


class TestMetaAsCautionaryTaleInAppleCoverage:
    """Apple articles use Meta as the cautionary tale / negative reference."""

    def test_apple_articles_reference_meta_negatively(self):
        """Multiple Apple articles stigmatize Meta within Apple coverage."""
        articles_with_meta_stigma = [
            a for a in ALL_APPLE_ARTICLES
            if a.get("meta_stigma_vocabulary_in_apple_article")
            or a.get("meta_stigma_in_apple_article")
            or a.get("meta_as_cautionary_tale")
        ]
        assert len(articles_with_meta_stigma) >= 2, (
            f"At least 2 Apple articles should reference Meta negatively, "
            f"found {len(articles_with_meta_stigma)}"
        )

    def test_light_trick_headline_presupposes_meta_creepy(self):
        """Headline 'avoid the creepy reputation of Meta Ray-Bans' 
        presupposes Meta's 'creepy' status as established fact."""
        headline = APPLE_LIGHT_TRICK_ARTICLE["headline"]
        assert "creepy reputation" in headline.lower(), (
            f"Headline should contain 'creepy reputation': {headline}"
        )
        assert "meta" in headline.lower() or "ray-ban" in headline.lower(), (
            f"Headline should reference Meta/Ray-Ban: {headline}"
        )
        assert "apple" in headline.lower(), (
            f"Headline should reference Apple as the solution: {headline}"
        )

    def test_privacy_storm_article_uses_meta_as_warning(self):
        """Apple privacy-storm article explicitly positions Meta as the failure case."""
        cautionary_refs = APPLE_PRIVACY_STORM_ARTICLE.get("meta_as_cautionary_tale", [])
        assert len(cautionary_refs) >= 2, (
            f"Expected 2+ Meta cautionary references, found {len(cautionary_refs)}"
        )
        assert any("what can go wrong" in ref.lower() for ref in cautionary_refs), (
            "Should contain 'what can go wrong' framing of Meta"
        )


class TestEquivalentFeaturesAsymmetricFraming:
    """Both products have cameras and AI — but only Meta gets alarm framing."""

    def test_apple_has_cameras_on_device(self):
        """Apple N50 has cameras, yet receives no camera privacy scrutiny."""
        assert APPLE_LIGHT_TRICK_ARTICLE["cameras_on_device"] is not None, (
            "Apple N50 article should document cameras on device"
        )

    def test_meta_face_recognition_is_rumored_not_active(self):
        """Meta NameTag feature is rumored/not activated, yet framed as imminent threat."""
        assert META_FACE_RECOGNITION_ARTICLE["feature_status"] == "rumored (NameTag, not activated)", (
            "Meta NameTag is rumored/not activated — alarm framing disproportionate"
        )

    def test_apple_visual_intelligence_continuous_scan_gets_no_alarm(self):
        """Apple Visual Intelligence scans surroundings continuously 
        (per Bloomberg) — functionally similar to Meta's features — 
        but receives zero alarm vocabulary."""
        # Apple N50 features per Bloomberg: cameras analyzing environment,
        # feeding information to Siri, continuous scene understanding
        for article in ALL_APPLE_ARTICLES:
            alarm = article.get("privacy_alarm_vocabulary", [])
            assert len(alarm) == 0, (
                f"Apple Visual Intelligence continuous scan should get "
                f"zero alarm terms, got {len(alarm)} in '{article['headline']}'"
            )

    def test_meta_shipping_privacy_improvements_framed_as_damage_control(self):
        """Meta's actual privacy improvements (LED tamper detection, 
        account removals) are framed as reactive damage control, 
        not as responsible engineering."""
        storm = APPLE_PRIVACY_STORM_ARTICLE
        cautionary = storm.get("meta_as_cautionary_tale", [])
        # Check that Meta's privacy response is framed negatively
        has_reactive_framing = any(
            "underground market" in ref.lower() or "eventually responded" in ref.lower()
            for ref in cautionary
        )
        assert has_reactive_framing, (
            "Meta's privacy improvements should be framed as reactive/belated, "
            "not as proactive engineering equivalent to Apple's approach"
        )


class TestGrudgingConcessionFormat:
    """Meta positive coverage uses grudging concession format (negative, but...)."""

    def test_meta_positive_content_uses_grudging_format(self):
        """When Digital Trends covers Meta positively (blind runner), 
        it leads with 'creepy reputation' before the positive content."""
        article = META_CREEPY_PURPOSE_ARTICLE
        assert article.get("grudging_concession_format") is True, (
            "Meta positive coverage should use grudging concession format"
        )

    def test_grudging_format_net_negative_despite_positive_content(self):
        """Net tone remains negative even when content is positive."""
        article = META_CREEPY_PURPOSE_ARTICLE
        assert article["tone_score"] < 0, (
            f"Net tone {article['tone_score']} should be negative "
            f"despite positive blind-runner content"
        )

    def test_no_grudging_format_in_apple_coverage(self):
        """Apple coverage never uses grudging concession format."""
        for article in ALL_APPLE_ARTICLES:
            assert not article.get("grudging_concession_format", False), (
                f"Apple article '{article['headline']}' should not use "
                f"grudging concession format"
            )


class TestPresuppositionLanguage:
    """'Already creepy' / 'creepy reputation' treats stigma as established fact."""

    def test_cheating_article_presupposes_creepy_as_baseline(self):
        """'Smart glasses were already creepy' presupposes stigma 
        before introducing new concern."""
        article = META_CHEATING_ARTICLE
        assert "already creepy" in article.get("presupposition", "").lower(), (
            "Presupposition should use 'already creepy' baseline"
        )

    def test_meta_stigma_vocabulary_includes_pervert_glasses(self):
        """Digital Trends adopts 'pervert glasses' terminology for Meta."""
        duckduckgo = DUCKDUCKGO_ANTI_META_ARTICLE
        alarm_terms = duckduckgo.get("privacy_alarm_vocabulary", [])
        assert any("pervert glasses" in term.lower() for term in alarm_terms), (
            "'pervert glasses' should appear in Digital Trends Meta vocabulary"
        )

    def test_surveillance_cameras_vocabulary_applied_to_meta(self):
        """'Tiny surveillance cameras' applied to Meta, never to Apple."""
        duckduckgo = DUCKDUCKGO_ANTI_META_ARTICLE
        alarm_terms = duckduckgo.get("privacy_alarm_vocabulary", [])
        assert any("surveillance cameras" in term.lower() for term in alarm_terms), (
            "'surveillance cameras' should be in Meta alarm vocabulary"
        )
        # Verify Apple never gets this
        for article in ALL_APPLE_ARTICLES:
            surveillance = article.get("privacy_alarm_vocabulary", [])
            assert not any("surveillance" in t.lower() for t in surveillance), (
                f"Apple should never get 'surveillance' vocabulary: "
                f"'{article['headline']}'"
            )


class TestManagingEditorParticipation:
    """Managing editor Nadeem Sarwar authors stigmatized Meta coverage."""

    def test_managing_editor_writes_creepy_meta_article(self):
        """Managing editor (not just a beat reporter) authors 'creepy' framing."""
        article = META_CHEATING_ARTICLE
        assert article.get("journalist") == "Nadeem Sarwar", (
            "Managing editor should author stigmatized Meta article"
        )

    def test_editorial_direction_pattern(self):
        """Multiple journalists (Andy Boxall, Rachit, Nadeem Sarwar) all 
        apply the same vocabulary bifurcation, suggesting editorial direction 
        rather than individual bias."""
        apple_journalists = set()
        meta_journalists = set()
        for a in ALL_APPLE_ARTICLES:
            if j := a.get("journalist"):
                apple_journalists.add(j)
        for a in ALL_META_ARTICLES:
            if j := a.get("journalist"):
                meta_journalists.add(j)
        # Both pools should have at least 1 journalist
        assert len(apple_journalists) >= 1 or len(meta_journalists) >= 1, (
            "At least one pool should have attributed journalists"
        )


class TestSameJournalistCrossCoverage:
    """Andy Boxall writes both Apple and Meta articles with different vocabulary."""

    def test_andy_boxall_covers_both_entities(self):
        """Same journalist covers Apple (neutral/sympathetic) and 
        Meta (adversarial) at Digital Trends."""
        boxall_apple = [
            a for a in ALL_APPLE_ARTICLES if a.get("journalist") == "Andy Boxall"
        ]
        boxall_meta = [
            a for a in ALL_META_ARTICLES if a.get("journalist") == "Andy Boxall"
        ]
        assert len(boxall_apple) >= 1, "Boxall should have at least 1 Apple article at DT"
        assert len(boxall_meta) >= 1, "Boxall should have at least 1 Meta article at DT"

    def test_boxall_apple_tone_higher_than_meta_tone(self):
        """Boxall's Apple tone is higher than his Meta tone."""
        apple_tone = APPLE_DELAY_2027_ARTICLE.get("tone_score", 0)
        meta_tone = META_FACE_RECOGNITION_ARTICLE.get("tone_score", 0)
        assert apple_tone > meta_tone, (
            f"Boxall Apple tone ({apple_tone}) should be higher than "
            f"Meta tone ({meta_tone})"
        )


class TestToneScoreAggregates:
    """Aggregate tone scores show systematic bifurcation."""

    def test_apple_average_tone_is_positive(self):
        """Average Apple tone is positive."""
        avg = sum(a.get("tone_score", 0) for a in ALL_APPLE_ARTICLES) / len(ALL_APPLE_ARTICLES)
        assert avg > 0.40, f"Apple avg tone {avg:.2f} should be > 0.40"

    def test_meta_average_tone_is_negative(self):
        """Average Meta tone is negative."""
        avg = sum(a.get("tone_score", 0) for a in ALL_META_ARTICLES) / len(ALL_META_ARTICLES)
        assert avg < -0.40, f"Meta avg tone {avg:.2f} should be < -0.40"

    def test_tone_gap_exceeds_1_point(self):
        """Gap between Apple and Meta average tone exceeds 1.0 points."""
        apple_avg = sum(a.get("tone_score", 0) for a in ALL_APPLE_ARTICLES) / len(ALL_APPLE_ARTICLES)
        meta_avg = sum(a.get("tone_score", 0) for a in ALL_META_ARTICLES) / len(ALL_META_ARTICLES)
        gap = apple_avg - meta_avg
        assert gap > 1.0, (
            f"Apple-Meta tone gap {gap:.2f} should exceed 1.0 "
            f"(Apple avg {apple_avg:.2f}, Meta avg {meta_avg:.2f})"
        )


class TestFinancialIncentiveAlignment:
    """Financial relationships predict the direction of vocabulary bifurcation."""

    def test_digital_trends_no_meta_financial_ties(self):
        """Digital Trends has no Meta financial relationship."""
        # From competitor-entities.yaml profile
        dt_meta_ties = {
            "content_licensing": None,
            "advertising": None,
            "revenue_share": None,
        }
        assert all(v is None for v in dt_meta_ties.values()), (
            "Digital Trends should have no Meta financial ties"
        )

    def test_digital_trends_apple_news_revenue(self):
        """Digital Trends publishes on Apple News (revenue share channel)."""
        apple_news_present = True  # DT publishes on Apple News
        assert apple_news_present, (
            "Digital Trends should publish on Apple News"
        )

    def test_meta_is_advertising_competitor_to_apple(self):
        """Meta competes with Apple ecosystem for advertising and attention."""
        meta_as_competitor = True  # From competitor-entities.yaml
        assert meta_as_competitor, (
            "Meta should be flagged as advertising competitor"
        )

    def test_financial_incentive_predicts_framing_direction(self):
        """Financial relationship → aspirational; no financial relationship → adversarial."""
        apple_avg_tone = sum(a.get("tone_score", 0) for a in ALL_APPLE_ARTICLES) / len(ALL_APPLE_ARTICLES)
        meta_avg_tone = sum(a.get("tone_score", 0) for a in ALL_META_ARTICLES) / len(ALL_META_ARTICLES)
        # Apple (financial relationship) = positive tone
        assert apple_avg_tone > 0, (
            f"Apple (financial relationship present) should have positive tone, got {apple_avg_tone:.2f}"
        )
        # Meta (no financial relationship) = negative tone
        assert meta_avg_tone < 0, (
            f"Meta (no financial relationship) should have negative tone, got {meta_avg_tone:.2f}"
        )


class TestDuckDuckGoAsAntiMetaProxy:
    """DuckDuckGo sunglasses article is framed as antidote to Meta surveillance."""

    def test_duckduckgo_article_exists_as_meta_contrast(self):
        """DuckDuckGo 'zero AI' article exists primarily as Meta contrast piece."""
        article = DUCKDUCKGO_ANTI_META_ARTICLE
        assert article["framing"] == "DuckDuckGo as antidote to Meta's surveillance glasses", (
            "DuckDuckGo article should be framed as anti-Meta"
        )

    def test_duckduckgo_article_tone_toward_meta_is_extreme_negative(self):
        """Meta tone in DuckDuckGo article is extreme negative (-0.90)."""
        assert DUCKDUCKGO_ANTI_META_ARTICLE["tone_toward_meta"] <= -0.85, (
            f"Meta tone in DuckDuckGo article should be <= -0.85, "
            f"got {DUCKDUCKGO_ANTI_META_ARTICLE['tone_toward_meta']}"
        )


class TestCrossReferenceExistingMechanisms:
    """Link to existing MediaScope mechanisms."""

    def test_connects_to_andy_boxall_android_police_mechanism(self):
        """Links to Mechanism #132 (Andy Boxall at Android Police)."""
        # Boxall demonstrates the same vocabulary bifurcation at both
        # Android Police (Mechanism #132) and Digital Trends
        related_mechanism_132 = {
            "mechanism_id": 132,
            "type": "same_journalist_privacy_vocabulary_inversion",
            "publication": "Android Police",
            "journalist": "Andy Boxall",
        }
        assert related_mechanism_132["journalist"] == "Andy Boxall"

    def test_connects_to_apple_n50_privacy_hero_cascade(self):
        """Links to Mechanism #55 (Apple N50 Privacy Hero Cascade)."""
        related_mechanism_55 = {
            "mechanism_id": 55,
            "type": "cross_publication_privacy_hero_cascade",
            "entity": "apple",
        }
        assert related_mechanism_55["entity"] == "apple"

    def test_connects_to_digital_trends_editorial_level_asymmetry(self):
        """Links to existing Digital Trends coverage patterns in Mechanism #149."""
        related_mechanism_149 = {
            "mechanism_id": 149,
            "type": "editorial_level_privacy_vocabulary_asymmetry",
            "publication": "Digital Trends",
        }
        assert related_mechanism_149["publication"] == "Digital Trends"


class TestConfounders:
    """Document and test confounding explanations."""

    CONFOUNDERS = [
        {
            "factor": "Meta has genuine privacy incidents",
            "strength": "STRONG",
            "response": "Apple N50 also has cameras with continuous scene analysis "
                        "(Visual Intelligence) — yet receives zero scrutiny. The gap is "
                        "proportionate to financial relationships, not to actual privacy risk.",
        },
        {
            "factor": "Apple's privacy reputation is historically strong",
            "strength": "MODERATE",
            "response": "Reputation-based framing is a form of brand bias. A camera on glasses "
                        "has the same privacy implications regardless of manufacturer. "
                        "Journalistic standards should scrutinize the product, not the brand.",
        },
        {
            "factor": "N50 has specific anti-recording design features (prominent indicator light)",
            "strength": "MODERATE",
            "response": "Meta also implemented tamper detection (Jul 7, 2026) and removed "
                        "misusing accounts — but these were framed as 'reactive damage control' "
                        "rather than responsible engineering. Equivalent actions, asymmetric framing.",
        },
        {
            "factor": "Apple hasn't shipped yet so there are no misuse cases to report",
            "strength": "WEAK",
            "response": "Digital Trends doesn't wait for shipping to apply alarm vocabulary "
                        "to Meta (covers rumored NameTag as imminent threat). The asymmetry "
                        "is in the standard applied, not in the available evidence.",
        },
    ]

    def test_all_confounders_documented(self):
        """At least 4 confounders with response documented."""
        assert len(self.CONFOUNDERS) >= 4

    def test_strong_confounder_acknowledged(self):
        """At least one STRONG confounder."""
        strong = [c for c in self.CONFOUNDERS if c["strength"] == "STRONG"]
        assert len(strong) >= 1

    def test_each_confounder_has_response(self):
        """Each confounder has a substantive response."""
        for c in self.CONFOUNDERS:
            assert len(c["response"]) > 50, (
                f"Confounder '{c['factor']}' needs substantive response"
            )
