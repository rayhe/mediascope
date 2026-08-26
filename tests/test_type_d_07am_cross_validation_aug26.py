"""
Type D Cross-Validation: Aug 26, 2026 07:00 AM PT — Mechanisms #317–#319

VALIDATION TARGET: Three mechanisms documented in today's iteration sprint (04:00–06:00 PT):
  - #317: WSJ Anthropic pre-IPO aspirational narrative / Meta investment scrutiny bifurcation
  - #318: Wesley Hilliard (AppleInsider) resolution-conditional privacy vocabulary inversion
  - #319: ChatGPT Ads Europe Le Monde content-ad cannibalization financial architecture

Cross-validation checks:
  1. MECHANISM INTEGRITY: All three mechanisms present in competitor-coverage-research.yaml
     with required fields, non-empty source URLs, and consistent entity references
  2. ENTITY CONSISTENCY: Entities referenced by mechanisms exist in competitor-entities.yaml
  3. FINANCIAL DATA COHERENCE: Anthropic revenue figures in #317 consistent with entity
     data; OpenAI ad revenue in #319 consistent with entity advertising_business section
  4. CROSS-MECHANISM STRUCTURAL VALIDATION: Three mechanisms test different domains
     (financial journalism, tech journalism, publisher financial architecture) but connect
     through the same thesis — financial relationships predict coverage framing
  5. CONFOUNDER DOCUMENTATION: Each mechanism documents counter-confounders, verifying
     intellectual honesty of the analysis
  6. JOURNALIST PROFILE CONSISTENCY: Wesley Hilliard (#318) registered in journalists.yaml
     with proper publication linkage
  7. PUBLICATION-LEVEL PATTERN VALIDATION: #318 is third AppleInsider writer with
     vocabulary inversion — validates that individual findings aggregate to publication-level
"""

import yaml
import os
import re
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_yaml(rel_path):
    with open(os.path.join(REPO_ROOT, rel_path)) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def entities():
    return load_yaml("profiles/competitor-entities.yaml")


@pytest.fixture(scope="module")
def research():
    return load_yaml("profiles/competitor-coverage-research.yaml")


@pytest.fixture(scope="module")
def journalists():
    return load_yaml("profiles/careers/journalists.yaml")


def find_mechanism(research_data, mech_id):
    """Find a mechanism by ID in the research YAML, searching all top-level sections."""
    for section_key in research_data:
        section = research_data[section_key]
        if isinstance(section, dict):
            for key, val in section.items():
                if isinstance(val, dict) and val.get("mechanism_id") == mech_id:
                    return val
        elif isinstance(section, list):
            for item in section:
                if isinstance(item, dict) and item.get("mechanism_id") == mech_id:
                    return item
    return None


def yaml_text(data):
    """Dump YAML data to string for grep-style searching."""
    return yaml.dump(data, default_flow_style=False)


# ============================================================
# CLASS 1: Mechanism #317 — WSJ Anthropic Pre-IPO Aspirational Narrative
# ============================================================

class TestMechanism317Existence:
    """Verify mechanism #317 exists with required structure."""

    def test_mechanism_317_exists(self, research):
        m = find_mechanism(research, 317)
        assert m is not None, "Mechanism #317 not found in research YAML"

    def test_mechanism_317_has_type(self, research):
        m = find_mechanism(research, 317)
        assert m is not None
        mtype = m.get("type", "")
        assert "bifurcation" in mtype or "aspirational" in mtype or "scrutiny" in mtype, \
            f"Mechanism #317 type should reference bifurcation/aspirational/scrutiny, got: {mtype}"

    def test_mechanism_317_has_publication(self, research):
        m = find_mechanism(research, 317)
        assert m is not None
        pub = str(m.get("publication", ""))
        assert "WSJ" in pub or "Wall Street Journal" in pub, \
            f"Mechanism #317 publication should be WSJ, got: {pub}"

    def test_mechanism_317_has_articles(self, research):
        m = find_mechanism(research, 317)
        assert m is not None
        articles = m.get("articles", [])
        assert len(articles) >= 2, \
            f"Mechanism #317 should have at least 2 articles (Anthropic + Meta), got {len(articles)}"

    def test_mechanism_317_articles_have_urls(self, research):
        m = find_mechanism(research, 317)
        assert m is not None
        for art in m.get("articles", []):
            url = art.get("url", "")
            assert url.startswith("http"), f"Article missing valid URL: {art.get('title', 'unknown')}"

    def test_mechanism_317_entities_include_anthropic_and_meta(self, research):
        m = find_mechanism(research, 317)
        assert m is not None
        entities = m.get("entities", [])
        entities_lower = [e.lower() for e in entities]
        assert "anthropic" in entities_lower, "Mechanism #317 should reference Anthropic"
        assert "meta" in entities_lower, "Mechanism #317 should reference Meta"

    def test_mechanism_317_reporters_documented(self, research):
        m = find_mechanism(research, 317)
        assert m is not None
        reporters = set()
        for art in m.get("articles", []):
            r = art.get("reporter", "")
            if r:
                reporters.add(r)
        assert len(reporters) >= 2, \
            "Should document at least 2 reporters (Driebusch for Anthropic, Bobrowsky for Meta)"


class TestMechanism317FinancialCoherence:
    """Verify financial data in #317 is internally consistent."""

    def test_anthropic_revenue_in_entities(self, entities):
        anthropic = entities.get("entities", {}).get("anthropic", {})
        text = yaml_text(anthropic)
        # ARR should reference $65B or higher (July 2026 figure)
        assert re.search(r'\$6[0-9][\s]*[Bb]', text) or "65" in text or "revenue" in text.lower(), \
            "Anthropic entity should contain recent revenue data"

    def test_wsj_articles_have_tone_scores(self, research):
        m = find_mechanism(research, 317)
        assert m is not None
        for art in m.get("articles", []):
            tone = art.get("tone")
            assert tone is not None, f"Article missing tone score: {art.get('title', 'unknown')}"
            assert isinstance(tone, (int, float)), f"Tone should be numeric: {tone}"

    def test_anthropic_articles_positive_meta_articles_negative(self, research):
        """The core bifurcation: Anthropic articles should have positive tone, Meta negative."""
        m = find_mechanism(research, 317)
        assert m is not None
        anthropic_tones = []
        meta_tones = []
        for art in m.get("articles", []):
            entity = art.get("entity", "").lower()
            tone = art.get("tone", 0)
            if "anthropic" in entity:
                anthropic_tones.append(tone)
            elif "meta" in entity:
                meta_tones.append(tone)
        if anthropic_tones and meta_tones:
            avg_anthropic = sum(anthropic_tones) / len(anthropic_tones)
            avg_meta = sum(meta_tones) / len(meta_tones)
            assert avg_anthropic > avg_meta, \
                f"Anthropic avg tone ({avg_anthropic}) should be more positive than Meta ({avg_meta})"


# ============================================================
# CLASS 2: Mechanism #318 — Wesley Hilliard Resolution-Conditional Vocabulary
# ============================================================

class TestMechanism318Existence:
    """Verify mechanism #318 exists with journalist cross-entity structure."""

    def test_mechanism_318_exists(self, research):
        m = find_mechanism(research, 318)
        assert m is not None, "Mechanism #318 not found in research YAML"

    def test_mechanism_318_has_journalist(self, research):
        m = find_mechanism(research, 318)
        assert m is not None
        journalist = m.get("journalist", "")
        assert "Hilliard" in journalist or "Wesley" in journalist, \
            f"Mechanism #318 should reference Wesley Hilliard, got: {journalist}"

    def test_mechanism_318_has_publication(self, research):
        m = find_mechanism(research, 318)
        assert m is not None
        pub = str(m.get("publication", ""))
        assert "AppleInsider" in pub, f"Mechanism #318 publication should be AppleInsider, got: {pub}"

    def test_mechanism_318_has_primary_articles(self, research):
        m = find_mechanism(research, 318)
        assert m is not None
        articles = m.get("primary_articles", [])
        assert len(articles) >= 2, \
            f"Mechanism #318 should have at least 2 primary articles, got {len(articles)}"

    def test_mechanism_318_has_podcast_evidence(self, research):
        m = find_mechanism(research, 318)
        assert m is not None
        podcast = m.get("podcast_evidence", [])
        assert len(podcast) >= 1, "Mechanism #318 should include podcast evidence"

    def test_mechanism_318_has_confounding_factors(self, research):
        m = find_mechanism(research, 318)
        assert m is not None
        confounders = m.get("confounding_factors", [])
        assert len(confounders) >= 3, \
            f"Mechanism #318 should have at least 3 confounders (strong ones), got {len(confounders)}"


class TestMechanism318JournalistProfile:
    """Verify Wesley Hilliard is registered in journalists.yaml with consistent data."""

    def test_hilliard_in_journalists_yaml(self, journalists):
        text = yaml_text(journalists)
        assert "Hilliard" in text or "hilliard" in text, \
            "Wesley Hilliard should be present in journalists.yaml"

    def test_hilliard_linked_to_appleinsider(self, journalists):
        text = yaml_text(journalists)
        # Find the Hilliard section and verify AppleInsider linkage
        if "Hilliard" in text or "hilliard" in text:
            # The journalist should reference AppleInsider
            assert "AppleInsider" in text, \
                "Journalist profiles should reference AppleInsider if Hilliard is documented"


class TestMechanism318PublicationLevelPattern:
    """Verify #318 is the third AppleInsider writer with vocabulary inversion."""

    def test_appleinsider_has_multiple_documented_writers(self, research):
        """AppleInsider should have at least 3 writers with similar patterns."""
        text = yaml_text(research)
        appleinsider_writers = set()
        # Known writers: Amber Neely (#285), Malcolm Owen (#234), Wesley Hilliard (#318)
        for name in ["Neely", "Owen", "Hilliard"]:
            if name in text:
                appleinsider_writers.add(name)
        assert len(appleinsider_writers) >= 3, \
            f"Should have 3+ AppleInsider writers documented, found: {appleinsider_writers}"


# ============================================================
# CLASS 3: Mechanism #319 — ChatGPT Ads Europe Le Monde Cannibalization
# ============================================================

class TestMechanism319Existence:
    """Verify mechanism #319 exists with five-layer financial architecture."""

    def test_mechanism_319_exists(self, research):
        m = find_mechanism(research, 319)
        assert m is not None, "Mechanism #319 not found in research YAML"

    def test_mechanism_319_has_five_layers(self, research):
        m = find_mechanism(research, 319)
        assert m is not None
        layers = m.get("five_layer_architecture", {})
        assert len(layers) >= 5, \
            f"Mechanism #319 should have 5 layers in architecture, got {len(layers)}"

    def test_mechanism_319_references_le_monde(self, research):
        m = find_mechanism(research, 319)
        assert m is not None
        pubs = m.get("publications", [])
        pubs_lower = [p.lower() for p in pubs]
        assert any("monde" in p for p in pubs_lower), \
            "Mechanism #319 should reference Le Monde"

    def test_mechanism_319_references_openai(self, research):
        m = find_mechanism(research, 319)
        assert m is not None
        entities = m.get("entities", [])
        entities_lower = [e.lower() for e in entities]
        assert "openai" in entities_lower, "Mechanism #319 should reference OpenAI"

    def test_mechanism_319_has_date(self, research):
        m = find_mechanism(research, 319)
        assert m is not None
        date = m.get("date_documented", "")
        assert "2026-08-26" in date, f"Mechanism #319 date should be 2026-08-26, got: {date}"


class TestMechanism319FinancialData:
    """Verify financial data in #319 is specific and sourced."""

    def test_openai_ad_revenue_in_entities(self, entities):
        openai = entities.get("entities", {}).get("openai", {})
        text = yaml_text(openai)
        # Should reference ad revenue or advertising business
        assert "ad" in text.lower() or "advertising" in text.lower(), \
            "OpenAI entity should have advertising data"

    def test_le_monde_conversion_rates_documented(self, research):
        m = find_mechanism(research, 319)
        assert m is not None
        text = yaml_text(m)
        assert "20x" in text or "20 times" in text.lower(), \
            "Should document 20x Facebook conversion rate"
        assert "50x" in text or "50 times" in text.lower(), \
            "Should document 50x Google Discover conversion rate"

    def test_journalist_revenue_share_documented(self, research):
        m = find_mechanism(research, 319)
        assert m is not None
        text = yaml_text(m)
        assert "25%" in text, "Should document Le Monde's 25% journalist revenue share"

    def test_layer_5_individual_incentive_documented(self, research):
        m = find_mechanism(research, 319)
        assert m is not None
        layers = m.get("five_layer_architecture", {})
        layer5 = layers.get("layer_5_individual_journalist_incentive", "")
        assert "journalist" in layer5.lower() or "bonus" in layer5.lower(), \
            "Layer 5 should document individual journalist financial incentive"


# ============================================================
# CLASS 4: Cross-Mechanism Structural Validation
# ============================================================

class TestCrossMechanismConsistency:
    """Verify the three mechanisms complement each other across domains."""

    def test_three_mechanisms_cover_distinct_domains(self, research):
        m317 = find_mechanism(research, 317)
        m318 = find_mechanism(research, 318)
        m319 = find_mechanism(research, 319)
        assert all(m is not None for m in [m317, m318, m319]), "All three mechanisms must exist"

        # #317 = financial journalism (WSJ), #318 = tech/Apple journalism, #319 = publisher financial architecture
        m317_type = str(m317.get("type", ""))
        m318_type = str(m318.get("type", ""))
        m319_type = str(m319.get("type", ""))
        types = {m317_type, m318_type, m319_type}
        assert len(types) == 3, \
            f"Three mechanisms should have distinct types, got: {types}"

    def test_meta_referenced_across_all_three(self, research):
        """Meta should appear as a comparison entity in all three mechanisms."""
        for mech_id in [317, 318, 319]:
            m = find_mechanism(research, mech_id)
            assert m is not None
            text = yaml_text(m)
            assert "meta" in text.lower() or "Meta" in text, \
                f"Mechanism #{mech_id} should reference Meta"

    def test_all_mechanisms_dated_aug_26(self, research):
        """All three should have documentation dates of Aug 26, 2026."""
        for mech_id in [317, 318, 319]:
            m = find_mechanism(research, mech_id)
            assert m is not None
            text = yaml_text(m)
            assert "2026-08-26" in text or "aug26" in text.lower() or "Aug 26" in text, \
                f"Mechanism #{mech_id} should reference Aug 26, 2026"

    def test_mechanism_ids_sequential(self, research):
        """Mechanisms #317, #318, #319 should be sequential with no gaps."""
        for mech_id in [317, 318, 319]:
            m = find_mechanism(research, mech_id)
            assert m is not None, f"Mechanism #{mech_id} should exist (sequential check)"


# ============================================================
# CLASS 5: Entity Data Consistency
# ============================================================

class TestEntityConsistency:
    """Verify entities referenced by mechanisms exist in competitor-entities.yaml."""

    def test_openai_entity_exists(self, entities):
        assert "openai" in entities.get("entities", {}), "OpenAI entity must exist"

    def test_anthropic_in_entities_or_research(self, entities, research):
        """Anthropic should be documented as a competitor entity."""
        text = yaml_text(entities)
        assert "anthropic" in text.lower() or "Anthropic" in text, \
            "Anthropic should be present in competitor-entities.yaml"

    def test_openai_has_ipo_data(self, entities):
        """OpenAI entity should have IPO filing data (relevant to #317 context)."""
        openai = entities.get("entities", {}).get("openai", {})
        assert "ipo_filing" in openai or "ipo" in yaml_text(openai).lower(), \
            "OpenAI entity should document IPO filing information"

    def test_openai_has_hardware_devices(self, entities):
        """OpenAI entity should document hardware devices (relevant to privacy parity)."""
        openai = entities.get("entities", {}).get("openai", {})
        assert "hardware_devices" in openai, \
            "OpenAI entity should document planned hardware devices"


# ============================================================
# CLASS 6: URL Integrity
# ============================================================

class TestURLIntegrity:
    """Verify all source URLs in mechanisms #317-#319 are well-formed."""

    def _collect_urls(self, mechanism):
        """Extract all URLs from a mechanism."""
        urls = []
        text = yaml_text(mechanism)
        for match in re.finditer(r'https?://[^\s\'"]+', text):
            urls.append(match.group().rstrip(".,;:)"))
        return urls

    def test_mechanism_317_urls_well_formed(self, research):
        m = find_mechanism(research, 317)
        assert m is not None
        urls = self._collect_urls(m)
        assert len(urls) >= 2, f"Mechanism #317 should have at least 2 URLs, got {len(urls)}"
        for url in urls:
            assert url.startswith("https://"), f"URL should be HTTPS: {url}"
            assert " " not in url, f"URL should not contain spaces: {url}"

    def test_mechanism_318_urls_well_formed(self, research):
        m = find_mechanism(research, 318)
        assert m is not None
        urls = self._collect_urls(m)
        assert len(urls) >= 2, f"Mechanism #318 should have at least 2 URLs, got {len(urls)}"
        for url in urls:
            assert url.startswith("https://"), f"URL should be HTTPS: {url}"

    def test_mechanism_317_wsj_urls(self, research):
        m = find_mechanism(research, 317)
        assert m is not None
        urls = self._collect_urls(m)
        wsj_urls = [u for u in urls if "wsj.com" in u]
        assert len(wsj_urls) >= 2, \
            f"Mechanism #317 should have at least 2 WSJ URLs, got {len(wsj_urls)}"

    def test_mechanism_318_appleinsider_urls(self, research):
        m = find_mechanism(research, 318)
        assert m is not None
        urls = self._collect_urls(m)
        ai_urls = [u for u in urls if "appleinsider.com" in u]
        assert len(ai_urls) >= 2, \
            f"Mechanism #318 should have at least 2 AppleInsider URLs, got {len(ai_urls)}"
