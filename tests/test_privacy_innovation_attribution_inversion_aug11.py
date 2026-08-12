"""
Privacy Innovation Attribution Inversion — Cross-Journalist Framing of
Meta's Industry-First Camera-Disable Feature

Type B: Journalist Cross-Entity Tracking (Aug 11, 2026 22:00 PT)

Mechanism #55: Documents how Meta's July 7, 2026 industry-first privacy feature
(camera disables if LED indicator is tampered with — "No other kind of camera
has done this and we're proud to lead the industry forward") was universally
framed as reactive damage control across publications, while Samsung's similar
privacy toggle (Jul 22) was framed as a feature and Apple's privacy delay
(Jul 26) was framed as responsible leadership.

Cross-journalist evidence:
- Ben Schoon (9to5Google): "inherently a privacy nightmare" for Meta's innovation
- Chandra Steele (Android Police): "but women's safety remains an issue" qualifier
- Digital Trends: "creep's weapon" framing subordinates innovation to narrative
- PetaPixel: "listening to the criticism" reactive framing
- Kyle Barr (Gizmodo): Samsung covered neutrally, Meta praised for build quality
- WebProNews: Apple's delay framed as "privacy reckoning" vs Meta's "baggage"
- Fast Company (SA): "The Problem with MetaRayBan glasses" litany framing

The SAME privacy concern (cameras on faces) receives INVERTED framing
depending on which company implements the solution.
"""

import yaml
import os
import pytest

COMPETITOR_RESEARCH_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
)

COMPETITOR_ENTITIES_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'competitor-entities.yaml'
)


@pytest.fixture(scope='module')
def competitor_research():
    with open(COMPETITOR_RESEARCH_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def competitor_entities():
    with open(COMPETITOR_ENTITIES_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def cross_pub_findings(competitor_research):
    cpf = competitor_research.get('cross_publication_findings', {})
    assert cpf, "cross_publication_findings section must exist"
    return cpf


@pytest.fixture(scope='module')
def mechanism(cross_pub_findings):
    m = cross_pub_findings.get('privacy_innovation_attribution_inversion')
    assert m is not None, (
        "Missing privacy_innovation_attribution_inversion in cross_publication_findings"
    )
    return m


# ── Class 1: Mechanism Structure ────────────────────────────────────


class TestMechanismStructure:
    """Verify mechanism #55 has all required top-level fields."""

    def test_mechanism_exists(self, mechanism):
        assert mechanism is not None

    def test_mechanism_id(self, mechanism):
        assert mechanism.get('mechanism_id') == 55

    def test_date_added(self, mechanism):
        assert mechanism.get('date_added') == '2026-08-11'

    def test_discovery_date(self, mechanism):
        assert mechanism.get('discovery_date') == '2026-08-11'

    def test_rotation_type(self, mechanism):
        assert mechanism.get('rotation_type') == 'B'

    def test_mechanism_name(self, mechanism):
        name = mechanism.get('mechanism_name', '')
        assert 'Privacy Innovation Attribution Inversion' in name

    def test_finding_type(self, mechanism):
        assert 'cross_entity' in mechanism.get('finding_type', '')

    def test_has_finding_summary(self, mechanism):
        summary = mechanism.get('finding_summary', '')
        assert len(summary) > 200, "Finding summary should be substantive"

    def test_has_test_file(self, mechanism):
        tf = mechanism.get('test_file', '')
        assert 'test_privacy_innovation_attribution_inversion_aug11' in tf

    def test_has_journalist_field(self, mechanism):
        assert 'journalist' in mechanism or 'journalists' in mechanism

    def test_publication_is_cross_publication(self, mechanism):
        pub = mechanism.get('publication', '')
        assert 'cross' in pub.lower() or 'multiple' in pub.lower()


# ── Class 2: Three Key Events ───────────────────────────────────────


class TestThreeKeyEvents:
    """Validate all three dated events are documented."""

    def test_meta_jul7_event(self, mechanism):
        articles = mechanism.get('articles', [])
        meta_jul7 = [a for a in articles if '2026-07-07' in a.get('date', '')]
        assert len(meta_jul7) >= 1, "Must document Meta's Jul 7 camera-disable announcement"

    def test_samsung_jul22_event(self, mechanism):
        articles = mechanism.get('articles', [])
        samsung_jul22 = [a for a in articles if '2026-07-22' in a.get('date', '')]
        assert len(samsung_jul22) >= 1, "Must document Samsung's Jul 22 Galaxy Glasses event"

    def test_apple_jul26_event(self, mechanism):
        articles = mechanism.get('articles', [])
        apple_jul26 = [a for a in articles if '2026-07-26' in a.get('date', '')]
        assert len(apple_jul26) >= 1, "Must document Apple's Jul 26 privacy delay report"

    def test_chronological_order(self, mechanism):
        """Events should be documented in chronological order."""
        articles = mechanism.get('articles', [])
        dates = [a.get('date', '') for a in articles if a.get('date')]
        # At minimum, we should have dates spanning Jul 7 through Jul 26
        assert any('07-07' in d or '07-08' in d or '07-10' in d for d in dates), \
            "Must have Meta early July articles"
        assert any('07-22' in d for d in dates), "Must have Samsung Jul 22 article"
        assert any('07-26' in d for d in dates), "Must have Apple Jul 26 article"

    def test_meta_event_is_industry_first(self, mechanism):
        summary = mechanism.get('finding_summary', '')
        assert 'industry' in summary.lower() and 'first' in summary.lower(), \
            "Summary must note Meta's feature was industry-first"


# ── Class 3: Article Evidence ───────────────────────────────────────


class TestArticleEvidence:
    """Validate article entries have required fields and real source URLs."""

    def test_minimum_article_count(self, mechanism):
        articles = mechanism.get('articles', [])
        assert len(articles) >= 7, "Must have at least 7 articles documented"

    def test_all_articles_have_urls(self, mechanism):
        articles = mechanism.get('articles', [])
        for i, art in enumerate(articles):
            url = art.get('url', '') or art.get('source_url', '')
            assert url.startswith('http'), f"Article {i} missing valid URL"

    def test_all_articles_have_publication(self, mechanism):
        articles = mechanism.get('articles', [])
        for i, art in enumerate(articles):
            assert art.get('publication'), f"Article {i} missing publication"

    def test_all_articles_have_dates(self, mechanism):
        articles = mechanism.get('articles', [])
        for i, art in enumerate(articles):
            assert art.get('date'), f"Article {i} missing date"

    def test_all_articles_have_tone(self, mechanism):
        articles = mechanism.get('articles', [])
        for i, art in enumerate(articles):
            assert 'tone' in art or 'tone_score' in art or 'framing' in art, \
                f"Article {i} missing tone/framing assessment"

    def test_9to5google_article(self, mechanism):
        articles = mechanism.get('articles', [])
        g9 = [a for a in articles if '9to5' in a.get('publication', '').lower()
              or '9to5google' in a.get('url', '').lower()
              or '9to5' in a.get('url', '').lower()]
        assert len(g9) >= 1, "Must include 9to5Google (Ben Schoon) article"

    def test_android_police_article(self, mechanism):
        articles = mechanism.get('articles', [])
        ap = [a for a in articles if 'android police' in a.get('publication', '').lower()
              or 'androidpolice' in a.get('url', '').lower()]
        assert len(ap) >= 1, "Must include Android Police (Chandra Steele) article"

    def test_digital_trends_article(self, mechanism):
        articles = mechanism.get('articles', [])
        dt = [a for a in articles if 'digital trends' in a.get('publication', '').lower()
              or 'digitaltrends' in a.get('url', '').lower()]
        assert len(dt) >= 1, "Must include Digital Trends article"

    def test_petapixel_article(self, mechanism):
        articles = mechanism.get('articles', [])
        pp = [a for a in articles if 'petapixel' in a.get('publication', '').lower()
              or 'petapixel' in a.get('url', '').lower()]
        assert len(pp) >= 1, "Must include PetaPixel article"


# ── Class 4: Journalist-Level Analysis ──────────────────────────────


class TestJournalistAnalysis:
    """Validate journalist-level cross-entity tracking."""

    def test_ben_schoon_documented(self, mechanism):
        summary = mechanism.get('finding_summary', '')
        articles = mechanism.get('articles', [])
        journalists = [a.get('journalist', '') for a in articles]
        assert any('Schoon' in j for j in journalists) or 'Schoon' in summary, \
            "Ben Schoon must be documented"

    def test_chandra_steele_documented(self, mechanism):
        articles = mechanism.get('articles', [])
        journalists = [a.get('journalist', '') for a in articles]
        assert any('Steele' in j for j in journalists), \
            "Chandra Steele must be documented"

    def test_meta_coverage_adversarial(self, mechanism):
        """Meta's privacy innovation should be documented as receiving adversarial framing."""
        articles = mechanism.get('articles', [])
        meta_articles = [a for a in articles
                         if 'meta' in a.get('publication', '').lower()
                         or '2026-07-07' in a.get('date', '')
                         or '2026-07-08' in a.get('date', '')
                         or '2026-07-10' in a.get('date', '')]
        # At least some Meta-era articles should have negative/adversarial tone
        adversarial = [a for a in meta_articles
                       if a.get('tone_score', 0) < 0
                       or 'adversarial' in str(a.get('framing', '')).lower()
                       or 'reactive' in str(a.get('framing', '')).lower()
                       or 'negative' in str(a.get('tone', '')).lower()]
        assert len(adversarial) >= 1, "Meta articles should document adversarial framing"

    def test_samsung_coverage_neutral(self, mechanism):
        """Samsung's coverage should be documented as neutral/positive."""
        articles = mechanism.get('articles', [])
        samsung = [a for a in articles if '2026-07-22' in a.get('date', '')]
        for art in samsung:
            tone = art.get('tone', '') or art.get('framing', '')
            assert 'adversarial' not in str(tone).lower() or 'neutral' in str(tone).lower(), \
                "Samsung coverage should not be primarily adversarial"


# ── Class 5: Framing Inversion Pattern ──────────────────────────────


class TestFramingInversion:
    """Validate the core finding: same concern, inverted framing by company."""

    def test_inversion_documented(self, mechanism):
        summary = mechanism.get('finding_summary', '')
        assert 'inver' in summary.lower() or 'asymmetr' in summary.lower(), \
            "Summary must document framing inversion"

    def test_same_privacy_concern(self, mechanism):
        """All three events address the same privacy concern: cameras on faces."""
        summary = mechanism.get('finding_summary', '')
        assert 'camera' in summary.lower() or 'privacy' in summary.lower()

    def test_meta_framed_reactive(self, mechanism):
        """Meta's industry-first feature framed as reactive/damage control."""
        summary = mechanism.get('finding_summary', '')
        articles = mechanism.get('articles', [])
        all_text = summary + ' '.join(str(a) for a in articles)
        assert ('reactive' in all_text.lower()
                or 'damage control' in all_text.lower()
                or 'backlash' in all_text.lower()
                or 'nightmare' in all_text.lower())

    def test_apple_framed_aspirational(self, mechanism):
        """Apple's delay framed as responsible/aspirational."""
        articles = mechanism.get('articles', [])
        apple_arts = [a for a in articles if '2026-07-26' in a.get('date', '')]
        all_text = ' '.join(str(a) for a in apple_arts)
        assert ('priorit' in all_text.lower()
                or 'responsible' in all_text.lower()
                or 'reckoning' in all_text.lower()
                or 'aspir' in all_text.lower()
                or 'lead' in all_text.lower())

    def test_samsung_framed_as_feature(self, mechanism):
        """Samsung's privacy toggle framed as product feature, not damage control."""
        articles = mechanism.get('articles', [])
        samsung_arts = [a for a in articles if '2026-07-22' in a.get('date', '')]
        all_text = ' '.join(str(a) for a in samsung_arts)
        assert ('neutral' in all_text.lower()
                or 'feature' in all_text.lower()
                or 'product' in all_text.lower())


# ── Class 6: Confounding Factors ────────────────────────────────────


class TestConfoundingFactors:
    """Validate intellectual honesty: at least 5 confounding factors."""

    def test_minimum_confounding_factors(self, mechanism):
        factors = mechanism.get('confounding_factors', [])
        assert len(factors) >= 5, f"Need ≥5 confounding factors, found {len(factors)}"

    def test_cambridge_analytica_factor(self, mechanism):
        """Must acknowledge Meta's track record as a confounding factor."""
        factors = mechanism.get('confounding_factors', [])
        all_factors = ' '.join(str(f) for f in factors)
        assert ('cambridge' in all_factors.lower()
                or 'track record' in all_factors.lower()
                or 'privacy controvers' in all_factors.lower()
                or 'history' in all_factors.lower())

    def test_market_leader_scrutiny_factor(self, mechanism):
        """Must acknowledge market leader receives more scrutiny."""
        factors = mechanism.get('confounding_factors', [])
        all_factors = ' '.join(str(f) for f in factors)
        assert ('market leader' in all_factors.lower()
                or 'scrutiny' in all_factors.lower()
                or 'incumbent' in all_factors.lower()
                or 'leader' in all_factors.lower())

    def test_shipped_vs_unshipped_factor(self, mechanism):
        """Must acknowledge Meta glasses are shipped, Samsung/Apple not yet."""
        factors = mechanism.get('confounding_factors', [])
        all_factors = ' '.join(str(f) for f in factors)
        assert ('ship' in all_factors.lower()
                or 'market' in all_factors.lower()
                or 'already on' in all_factors.lower()
                or 'real-world' in all_factors.lower())

    def test_reactive_trigger_factor(self, mechanism):
        """Must acknowledge Meta's update was triggered by reported misuse."""
        factors = mechanism.get('confounding_factors', [])
        all_factors = ' '.join(str(f) for f in factors)
        assert ('triggered' in all_factors.lower()
                or 'reactive' in all_factors.lower()
                or 'misuse' in all_factors.lower()
                or 'respond' in all_factors.lower())

    def test_factors_are_substantive(self, mechanism):
        """Each factor should be a substantive explanation, not a stub."""
        factors = mechanism.get('confounding_factors', [])
        for i, factor in enumerate(factors):
            assert len(str(factor)) >= 20, f"Factor {i} too short: {factor}"


# ── Class 7: Testable Predictions ───────────────────────────────────


class TestTestablePredictions:
    """Validate forward-looking testable predictions (≥3)."""

    def test_minimum_predictions(self, mechanism):
        preds = mechanism.get('testable_predictions', [])
        assert len(preds) >= 3, f"Need ≥3 testable predictions, found {len(preds)}"

    def test_samsung_shipping_prediction(self, mechanism):
        """Should predict what happens when Samsung glasses ship."""
        preds = mechanism.get('testable_predictions', [])
        all_preds = ' '.join(str(p) for p in preds)
        assert 'samsung' in all_preds.lower(), \
            "Must predict Samsung shipping outcome"

    def test_apple_launch_prediction(self, mechanism):
        """Should predict Apple smart glasses launch framing."""
        preds = mechanism.get('testable_predictions', [])
        all_preds = ' '.join(str(p) for p in preds)
        assert 'apple' in all_preds.lower(), \
            "Must predict Apple launch framing"

    def test_predictions_are_falsifiable(self, mechanism):
        """Predictions should be specific enough to be falsifiable."""
        preds = mechanism.get('testable_predictions', [])
        for i, pred in enumerate(preds):
            pred_text = str(pred)
            assert len(pred_text) >= 30, f"Prediction {i} too short to be falsifiable"


# ── Class 8: Source URLs ────────────────────────────────────────────


class TestSourceURLs:
    """Validate all source URLs are present and well-formed."""

    def test_has_9to5google_url(self, mechanism):
        articles = mechanism.get('articles', [])
        urls = [a.get('url', '') or a.get('source_url', '') for a in articles]
        assert any('9to5google.com' in u for u in urls), "Missing 9to5Google URL"

    def test_has_androidpolice_url(self, mechanism):
        articles = mechanism.get('articles', [])
        urls = [a.get('url', '') or a.get('source_url', '') for a in articles]
        assert any('androidpolice.com' in u for u in urls), "Missing Android Police URL"

    def test_has_digitaltrends_url(self, mechanism):
        articles = mechanism.get('articles', [])
        urls = [a.get('url', '') or a.get('source_url', '') for a in articles]
        assert any('digitaltrends.com' in u for u in urls), "Missing Digital Trends URL"

    def test_has_petapixel_url(self, mechanism):
        articles = mechanism.get('articles', [])
        urls = [a.get('url', '') or a.get('source_url', '') for a in articles]
        assert any('petapixel.com' in u for u in urls), "Missing PetaPixel URL"

    def test_has_gizmodo_url(self, mechanism):
        articles = mechanism.get('articles', [])
        urls = [a.get('url', '') or a.get('source_url', '') for a in articles]
        assert any('gizmodo.com' in u for u in urls), "Missing Gizmodo Samsung URL"

    def test_has_webpronews_url(self, mechanism):
        articles = mechanism.get('articles', [])
        urls = [a.get('url', '') or a.get('source_url', '') for a in articles]
        assert any('webpronews.com' in u for u in urls), "Missing WebProNews Apple URL"

    def test_has_fastcompany_url(self, mechanism):
        articles = mechanism.get('articles', [])
        urls = [a.get('url', '') or a.get('source_url', '') for a in articles]
        assert any('fastcompany' in u for u in urls), "Missing Fast Company URL"

    def test_all_urls_are_https(self, mechanism):
        articles = mechanism.get('articles', [])
        urls = [a.get('url', '') or a.get('source_url', '') for a in articles]
        for url in urls:
            if url:
                assert url.startswith('https://'), f"URL not HTTPS: {url}"


# ── Class 9: Competitor Entity References ───────────────────────────


class TestCompetitorEntityReferences:
    """Verify competitor-entities.yaml has _ref pointers for mechanism #55."""

    def test_samsung_privacy_attribution_ref(self, competitor_entities):
        entities = competitor_entities.get('entities', {})
        samsung = entities.get('samsung', {})
        ref = samsung.get('privacy_innovation_attribution')
        assert ref is not None, \
            "Samsung in competitor-entities.yaml must have privacy_innovation_attribution section"

    def test_samsung_ref_mechanism_id(self, competitor_entities):
        entities = competitor_entities.get('entities', {})
        samsung = entities.get('samsung', {})
        ref = samsung.get('privacy_innovation_attribution', {})
        assert ref.get('mechanism_id') == 55 or ref.get('_ref_mechanism_id') == 55, \
            "Samsung privacy_innovation_attribution must reference mechanism #55"

    def test_apple_privacy_attribution_ref(self, competitor_entities):
        entities = competitor_entities.get('entities', {})
        apple = entities.get('apple', {})
        ref = apple.get('privacy_innovation_attribution')
        assert ref is not None, \
            "Apple in competitor-entities.yaml must have privacy_innovation_attribution section"

    def test_apple_ref_mechanism_id(self, competitor_entities):
        entities = competitor_entities.get('entities', {})
        apple = entities.get('apple', {})
        ref = apple.get('privacy_innovation_attribution', {})
        assert ref.get('mechanism_id') == 55 or ref.get('_ref_mechanism_id') == 55, \
            "Apple privacy_innovation_attribution must reference mechanism #55"
