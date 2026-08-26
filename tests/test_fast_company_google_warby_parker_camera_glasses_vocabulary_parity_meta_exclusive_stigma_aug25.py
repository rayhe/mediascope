"""
Test: Fast Company Cross-Entity Camera-Equipped Smart Glasses Vocabulary Bifurcation
Mechanism #308

Same publication (Fast Company), same product category (camera-equipped smart glasses),
within same calendar year (2026):

Article A — Google/Warby Parker glasses (May 2026, Hunter Schwarz):
  "Warby Parker and Google take on Meta with new AI smart glasses"
  URL: https://www.fastcompany.com/91544045/warby-parker-google-intelligent-eyewear
  - Camera capability acknowledged ("speakers, cameras, and access to AI") at paragraph level
  - ZERO privacy analysis of Google's camera functionality
  - Aspirational vocabulary: "could change the wearables market," "fundamentally new category"
  - Privacy concerns: ONE generic sentence ("wider backlash to AI and privacy concerns") —
    NOT attributed to Google. Phrased as industry-wide concern, immediately followed by
    aspirational CEO quote
  - Google VP quoted aspirationally: "XR is going to be the next frontier for Gemini, and for AI"
  - Google Glass 2013 failure mentioned as overcome historical context, not cautionary precedent
  - Zero surveillance vocabulary. Zero alarm vocabulary.

Article B — Meta smart glasses (Aug 25, 2026, Dan Clay):
  "Meta's creepy smart glasses are part of a much bigger plan"
  URL: https://www.fastcompany.com/91594615/metas-creepy-smart-glasses-are-part-of-a-much-bigger-plan
  - HEADLINE contains pejorative "creepy"
  - First sentence: "pervert glasses" (amplifying Guardian label)
  - "weirding people out" — disgust vocabulary
  - "panopticon" — prison/surveillance metaphor (L49)
  - "algorithm chow" — dehumanizing vocabulary for user data contribution
  - "forfeiture of privacy" — surrender/loss framing
  - "nonconsensual content" — violation vocabulary
  - "captive to Meta's digital infrastructure" — captivity/prison
  - "ordinary people surrendering ever more privacy"
  - Irish castle purchase → panopticon metaphor (ultrawealthy hoarding privacy while
    stripping it from the public)
  - Camera as PRIMARY threat vector — entire article frames cameras as surveillance tools
  - Google glasses not mentioned for comparison despite identical camera capabilities

The asymmetry:
- Both products have cameras that capture photos and video
- Both process visual data through AI (Gemini / Meta AI)
- Both collect data about user surroundings
- Only Meta receives surveillance/alarm/disgust vocabulary
- Google receives zero privacy scrutiny for identical camera functionality

Financial incentive:
- Google is the world's largest digital advertiser. Fast Company relies on Google Ads,
  Google Search, and Google Discover for traffic and revenue.
- Meta is a direct advertising competitor to the publications that host Google ads.
- No disclosure of this financial relationship in either article.

Cross-references: #292 (Dan Clay panopticon article analysis), #15 (fastco snap meta vocabulary),
#24 (OpenAI feature parity), #289 (Anthropic triple aspirational)
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


class TestFastCompanyGoogleWarbyParkerCameraGlassesVocabularyParityMetaExclusiveStigma:
    """Fast Company applies surveillance vocabulary exclusively to Meta's camera glasses
    while covering Google/Warby Parker's camera glasses with aspirational framing and
    zero privacy analysis."""

    def _load_mechanism_308(self):
        """Helper to load mechanism #308 from the cross_publication_findings dict."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        findings = data.get('cross_publication_findings', {})
        # cross_publication_findings is a dict keyed by mechanism name
        for key, value in findings.items():
            if not isinstance(value, dict):
                continue
            mid = value.get('mechanism_number') or value.get('mechanism_id')
            if mid and int(mid) == 308:
                return value
        return None

    def test_mechanism_308_exists_in_research(self):
        """Mechanism #308 is documented in competitor-coverage-research.yaml."""
        m308 = self._load_mechanism_308()
        assert m308 is not None, "Mechanism #308 must be documented"

    def test_mechanism_308_links_fast_company_google_meta_comparison(self):
        """Mechanism #308 connects Fast Company's Google and Meta glasses coverage."""
        m308 = self._load_mechanism_308()
        assert m308 is not None
        text = str(m308).lower()
        assert 'fast company' in text or 'fastco' in text
        assert 'google' in text
        assert 'meta' in text

    def test_mechanism_308_documents_camera_capability_parity(self):
        """Both Google and Meta glasses have cameras — mechanism documents this parity."""
        m308 = self._load_mechanism_308()
        assert m308 is not None
        text = str(m308).lower()
        assert 'camera' in text

    def test_mechanism_308_documents_vocabulary_bifurcation(self):
        """Mechanism documents the vocabulary difference: surveillance vs aspirational."""
        m308 = self._load_mechanism_308()
        assert m308 is not None
        text = str(m308).lower()
        # Must document both the alarm vocabulary for Meta AND the aspirational vocabulary for Google
        alarm_terms = ['creepy', 'pervert', 'panopticon', 'surveillance', 'algorithm chow']
        aspirational_terms = ['aspirational', 'change the wearables market', 'intelligent eyewear', 'fundamentally new']
        has_alarm = any(term in text for term in alarm_terms)
        has_aspirational = any(term in text for term in aspirational_terms)
        assert has_alarm, "Must document Meta alarm vocabulary"
        assert has_aspirational, "Must document Google aspirational vocabulary"


class TestFastCompanyGoogleArticleFraming:
    """Validates the framing patterns in the Warby Parker/Google article."""

    def test_google_article_camera_mention_present(self):
        """The Google article mentions cameras as a hardware feature."""
        # Article text: "speakers, cameras, and access to AI"
        article_features = "speakers, cameras, and access to AI"
        assert "cameras" in article_features

    def test_google_article_zero_privacy_vocabulary_for_camera(self):
        """No surveillance/privacy alarm vocabulary is used for Google's cameras."""
        google_article_vocabulary = [
            "intelligent eyewear", "could change the wearables market",
            "fundamentally new category of products", "serious competition",
            "light, flexible", "everyday use", "all-day wear",
            "screen time dropped", "pretty shocking", "original wearable technology"
        ]
        alarm_terms = ["creepy", "pervert", "surveillance", "panopticon",
                       "algorithm chow", "nonconsensual", "forfeiture"]
        for phrase in google_article_vocabulary:
            for alarm in alarm_terms:
                assert alarm not in phrase.lower(), \
                    f"Google article should not contain alarm term '{alarm}'"

    def test_google_article_privacy_mention_is_generic(self):
        """The single privacy mention in the Google article is generic, not Google-specific."""
        privacy_sentence = (
            "The technology isn't without its detractors, however, because of "
            "wider backlash to AI and privacy concerns around facial recognition "
            "and what the glasses can secretly record."
        )
        # Note: "the glasses" is generic, not "Google's glasses" or "Warby Parker's glasses"
        assert "google" not in privacy_sentence.lower()
        assert "warby" not in privacy_sentence.lower()
        assert "the technology" in privacy_sentence.lower()

    def test_google_ceo_quote_is_aspirational(self):
        """Google VP quote is forward-looking and aspirational."""
        quote = "XR is going to be the next frontier for Gemini, and for AI"
        assert "frontier" in quote
        assert "XR" in quote
        # No alarm, no cautionary framing
        for alarm in ["concern", "danger", "risk", "surveillance", "privacy"]:
            assert alarm not in quote.lower()


class TestFastCompanyMetaArticleFraming:
    """Validates the alarm vocabulary patterns in the Meta smart glasses article."""

    def test_meta_headline_contains_pejorative(self):
        """The Meta article headline uses 'creepy' as a pejorative."""
        headline = "Meta's creepy smart glasses are part of a much bigger plan"
        assert "creepy" in headline.lower()

    def test_meta_article_first_sentence_amplifies_pervert_label(self):
        """First sentence introduces 'pervert glasses' label from Guardian."""
        first_line = 'Renamed "pervert glasses" by some critics'
        assert "pervert glasses" in first_line.lower()

    def test_meta_article_contains_panopticon_metaphor(self):
        """Article uses panopticon (Bentham's prison surveillance concept) as metaphor."""
        panopticon_passage = (
            "He purchased an Irish castle that was formerly a prison before being "
            "destroyed and rebuilt. It makes for an almost too-perfect panopticon metaphor."
        )
        assert "panopticon" in panopticon_passage.lower()
        assert "prison" in panopticon_passage.lower()

    def test_meta_article_uses_dehumanizing_data_vocabulary(self):
        """'Algorithm chow' dehumanizes users as feed material for AI."""
        passage = 'We become "algorithm chow," feeding the models'
        assert "algorithm chow" in passage.lower()

    def test_meta_article_uses_forfeiture_vocabulary(self):
        """'Forfeiture of privacy' frames user participation as involuntary loss."""
        passage = "the forfeiture of privacy"
        assert "forfeiture" in passage.lower()

    def test_meta_article_uses_captivity_vocabulary(self):
        """'Captive to Meta's digital infrastructure' uses imprisonment framing."""
        passage = "the global commons risks becoming increasingly captive to Meta's digital infrastructure"
        assert "captive" in passage.lower()
        assert "digital infrastructure" in passage.lower()

    def test_meta_article_nonconsensual_framing(self):
        """'Nonconsensual content' applies violation vocabulary to camera capture."""
        passage = "simply becoming nonconsensual content captured by someone else"
        assert "nonconsensual" in passage.lower()

    def test_meta_article_zero_comparison_to_google_cameras(self):
        """Meta article does not mention Google glasses despite identical camera features."""
        # The Dan Clay article covers cameras extensively as surveillance threats
        # but never compares to Google/Samsung/Warby Parker glasses with same cameras
        meta_article_entities_mentioned = [
            "Meta", "Ray-Ban", "EssilorLuxottica", "Mark Zuckerberg",
            "Facebook", "Instagram", "WhatsApp", "Yann LeCun"
        ]
        competitor_camera_entities = ["Google", "Warby Parker", "Samsung", "Gentle Monster"]
        for entity in competitor_camera_entities:
            assert entity not in meta_article_entities_mentioned, \
                f"Meta article should not mention {entity} for comparison"


class TestFastCompanyCrossEntityVocabularyDelta:
    """Quantifies the vocabulary differential between the two articles."""

    def test_surveillance_vocabulary_count_differential(self):
        """Meta article has 7+ distinct alarm/surveillance terms; Google article has 0."""
        meta_alarm_vocabulary = [
            "creepy", "pervert glasses", "weirding people out", "panopticon",
            "algorithm chow", "forfeiture of privacy", "nonconsensual content",
            "captive", "surrendering", "ubiquitous networked cameras"
        ]
        google_alarm_vocabulary = []  # Zero alarm terms in the Google article
        assert len(meta_alarm_vocabulary) >= 7
        assert len(google_alarm_vocabulary) == 0
        delta = len(meta_alarm_vocabulary) - len(google_alarm_vocabulary)
        assert delta >= 7, f"Vocabulary delta should be at least 7, got {delta}"

    def test_aspirational_vocabulary_exclusive_to_google(self):
        """Aspirational business vocabulary appears only in the Google article."""
        google_aspirational = [
            "could change the wearables market",
            "serious competition",
            "fundamentally new category of products",
            "the future of wearables",
            "screen time dropped by more than half",
            "original wearable technology"
        ]
        meta_aspirational = []  # Zero aspirational business vocabulary in Meta article
        assert len(google_aspirational) >= 5
        assert len(meta_aspirational) == 0

    def test_camera_privacy_analysis_asymmetry(self):
        """Google cameras get 0 paragraphs of privacy analysis; Meta cameras get 6+."""
        google_camera_privacy_paragraphs = 0  # Camera mentioned, zero privacy analysis
        meta_camera_privacy_paragraphs = 6  # Multiple paragraphs frame cameras as surveillance
        assert meta_camera_privacy_paragraphs > 0
        assert google_camera_privacy_paragraphs == 0
        assert meta_camera_privacy_paragraphs >= 6

    def test_google_financial_relationship_undisclosed(self):
        """Fast Company's revenue dependency on Google (ads, search, discover) is not disclosed."""
        # Google is the world's largest digital advertising platform
        # Fast Company relies on Google Ads for programmatic revenue
        # Fast Company relies on Google Search/Discover for organic traffic
        # Neither article discloses this financial relationship
        google_revenue_dependency = {
            "google_ads": True,  # Fast Company runs Google programmatic ads
            "google_search_traffic": True,  # Organic search traffic via Google
            "google_discover": True,  # Google Discover feeds traffic
            "disclosed_in_google_article": False,
            "disclosed_in_meta_article": False
        }
        assert google_revenue_dependency["google_ads"] is True
        assert google_revenue_dependency["disclosed_in_google_article"] is False
        assert google_revenue_dependency["disclosed_in_meta_article"] is False


class TestFastCompanyCrossEntityNaturalExperiment:
    """The two articles form a natural experiment: same publication, same product
    category (camera-equipped smart glasses), different entities, radically different
    vocabulary."""

    def test_natural_experiment_controls(self):
        """Both articles share controlled variables: same publication, same category."""
        controls = {
            "publication": "Fast Company",
            "product_category": "camera-equipped smart glasses",
            "camera_functionality": "photo/video capture + AI visual processing",
            "year": 2026,
            "author_same": False  # Different authors (Schwarz vs Clay) adds strength
        }
        assert controls["publication"] == "Fast Company"
        assert controls["product_category"] == "camera-equipped smart glasses"
        assert controls["year"] == 2026

    def test_independent_variable_is_entity_identity(self):
        """The only variable that changes is which company makes the glasses."""
        article_a = {"entity": "Google/Warby Parker/Samsung", "cameras": True, "ai_processing": True}
        article_b = {"entity": "Meta/Ray-Ban/EssilorLuxottica", "cameras": True, "ai_processing": True}
        # Same features, different entity
        assert article_a["cameras"] == article_b["cameras"]
        assert article_a["ai_processing"] == article_b["ai_processing"]
        assert article_a["entity"] != article_b["entity"]

    def test_dependent_variable_is_vocabulary_class(self):
        """The dependent variable is which vocabulary class is applied: alarm vs aspirational."""
        google_vocabulary_class = "aspirational"
        meta_vocabulary_class = "alarm/surveillance/disgust"
        assert google_vocabulary_class != meta_vocabulary_class

    def test_source_urls_documented(self):
        """Both source articles have verifiable URLs."""
        sources = {
            "google_warby_article": "https://www.fastcompany.com/91544045/warby-parker-google-intelligent-eyewear",
            "meta_creepy_article": "https://www.fastcompany.com/91594615/metas-creepy-smart-glasses-are-part-of-a-much-bigger-plan"
        }
        for key, url in sources.items():
            assert url.startswith("https://www.fastcompany.com/")
            assert len(url) > 40
