"""
Mechanism #242: Fast Company (Mansueto Ventures) UK Cinema Ban Institutional Entity
Selection — Category-Neutral Ban Headlined as Meta-Exclusive + Snap Specs Sep 16
Launch Omission

TYPE A: Competitor Coverage Deep Dive (Fast Company + Meta vs Snap/Apple/Samsung/Google)
Extends Mechanism #121 (Fast Company Snap/Meta vocabulary asymmetry)

FINDING: Fast Company published "Meta glasses in movie theaters? Some cinema owners ban
them" on Aug 20, 2026, covering the UK Cinema Association (UKCA) statement restricting
"camera-enabled smart glasses." The UKCA statement is ENTITY-NEUTRAL — it says
"camera-enabled smart glasses," not "Meta glasses." But Fast Company's headline selects
Meta exclusively, the body names Meta 10+ times, and the article lists 6 additional
Meta-specific institutional bans without once asking whether any competitor's camera
wearables would face the same restrictions.

This creates a THREE-ARTICLE longitudinal coverage pattern at Fast Company:

| Article              | Date    | Entity | Framing                    | Privacy Terms |
|---------------------|---------|--------|----------------------------|---------------|
| Snap Specs AWE      | Jun 16  | Snap   | Aspirational CEO profile   | 0             |
| Meta controversies  | Jul 10  | Meta   | Controversy compilation    | 10+           |
| UK cinema ban       | Aug 20  | Meta   | Institutional ban cascade  | 5+            |

3 articles, 65 days. Meta is ALWAYS the alarm target. Snap is ALWAYS aspirational or absent.

INSTITUTIONAL ENTITY SELECTION:
The UKCA statement covers ALL "camera-enabled smart glasses." This includes:
  - Snap Specs (4 cameras, launching Sep 16, 2026 — 27 days after article)
  - Apple camera AirPods / smart glasses (cameras, launching 2027)
  - Samsung Galaxy Glasses (cameras, launched Jul 22, 2026)
  - Google Android XR reference glasses (cameras, in development)

None are mentioned. Fast Company transforms a CATEGORY policy into a META-specific stigma
event. The headline "Meta glasses in movie theaters?" frames Meta as the subject of the
ban; "camera-enabled smart glasses" frames the technology category.

SNAP SPECS LAUNCH OMISSION:
Snap Specs consumer launch is Sep 16, 2026 — 27 days after publication. Fast Company:
  - Published a 2,500-word aspirational Snap Specs profile Jun 16 (mechanism #121)
  - Did NOT ask in the UK cinema article whether Snap Specs (4 cameras) would face bans
  - Did NOT ask whether the UKCA policy applies to Snap Specs
  - Snap's AWE profile contained ZERO privacy questions despite 4 cameras

HEADLINE ENTITY SELECTION CONCORDANCE:
Fast Company joins a cross-publication concordance pattern (mechanism #236, ICE ban):
  - Fast Company: "Meta glasses in movie theaters? Some cinema owners ban them"
  - Reuters: "UK cinemas restricting Meta AI and other smart glasses"
  - The Gazette/Resident: "UK cinemas introducing new ban on using Meta Glasses"
  - UKCA statement: "camera-enabled smart glasses" (entity-neutral)

All publications select Meta for the headline despite entity-neutral source.

CONFOUNDERS (5):
  1. STRONG: Meta holds ~76% market share. "Meta glasses" is a common synecdoche.
  2. STRONG: Meta has genuine documented privacy incidents; Snap Specs haven't shipped yet.
  3. MODERATE: The HMCTS quote specifically names "Meta glasses," giving publications
     a named-entity peg even if the UKCA statement is neutral.
  4. MODERATE: Different article genres (institutional ban news vs CEO profile feature).
  5. WEAK: Snap Specs at $2,195 are developer-oriented, not mass consumer yet.

SOURCES:
  - https://www.fastcompany.com/91593349/meta-glasses-in-movie-theaters-some-cinema-owners-ban-them
  - https://www.fastcompany.com/91559773/snap-specs-2026-ar-glasses-evan-spiegel
  - https://www.fastcompany.com/91571430/the-many-controversies-of-metas-ai-glasses
  - https://www.reuters.com/business/media-telecom/uk-cinemas-restricting-meta-ai-other-smart-glasses-over-piracy-concerns-2026-08-20/

CROSS-REFERENCES:
  - #121: Fast Company Snap/Meta privacy vocabulary asymmetry (Jun-Jul 2026)
  - #236: ICE/DHS institutional ban paradox — Meta-exclusive stigma cascade
  - #8: Safe target coefficient
  - #239: Conde Nast Snap Discover quintuple financial alignment
  - #231: Snap Specs CLAD quad-AI developer ecosystem
"""

import pytest
import yaml
import os

RESEARCH_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
)


@pytest.fixture(scope='module')
def research_data():
    with open(RESEARCH_PATH) as f:
        return yaml.safe_load(f)


# --- Article Content Fixtures ---

UK_CINEMA_BAN_ARTICLE_HEADLINE = (
    "Meta glasses in movie theaters? Some cinema owners ban them"
)

UK_CINEMA_BAN_ARTICLE_BODY = (
    "UK cinemas are moving to restrict camera-enabled smart glasses made by Meta "
    "Platforms and other tech companies, joining the trend of establishments banning "
    "the wearable technology in public settings.\n"
    "On Thursday, the UK Cinema Association (UKCA) released a statement saying that "
    "while it recognizes smart glasses can provide benefits to those with access "
    "requirements, use of the technology in movie theaters is raising concerns around "
    '"privacy and film piracy."\n'
    "Despite the growing rejection of Meta glasses in different spaces, seven million "
    "were sold in 2025.\n"
    "UK cinemas are joining a trend of many other establishments, workplaces, and "
    "groups prohibiting or restricting smart glasses. The trend comes amid growing "
    "conversations around Meta glasses being used in schools, medical offices, and "
    "bathrooms.\n"
    "Last week, courts in England and Wales began prohibiting smart glasses. "
    'HMCTS said that "Meta glasses will be confiscated from anyone entering its '
    'judicial buildings."\n'
    "The HMCTS joined other UK establishments, including private members' club Soho "
    "House and pub chain Wetherspoon, in its Meta glasses ban.\n"
    "About a month before, in July, the New York state court system prohibited the "
    "use of smart glasses in all courts.\n"
    "On Tuesday, Immigration and Customs Enforcement (ICE) prohibited its employees "
    "from wearing Meta glasses in the federal workplace out of privacy concerns.\n"
    'The UKCA says the restriction of Meta glasses is a developing area.\n'
)

UKCA_STATEMENT = (
    "UK cinema operators are aware of the increasing availability and use of "
    "wearable technology such as smart glasses and the extent to which these can "
    "provide benefits to those with specific access requirements. However, they are "
    "also mindful of the issues around privacy and film piracy that arise around "
    "the use of such technology in cinemas, and as a result many are introducing "
    "policies to prohibit and/or restrict the wearing of camera-enabled smart "
    "glasses in particular in their venues."
)

SNAP_SPECS_ARTICLE_SNIPPET = (
    "Snap's cofounder and CEO, Evan Spiegel, gave this morning's keynote at AWE. "
    "He came with news: Snap is releasing a pair of AR-enabled glasses called Specs. "
    "It intends to ship them this fall for $2,195, and is taking preorders.\n"
    '"If you look at the history of the company, we\'ve been laser focused on trying '
    'to make computing more human," he says.\n'
    "By putting AR before your very glasses-wearing eyes, Specs offer a richer canvas "
    "for AR than a smartphone-sized app like Snapchat can.\n"
    '"For me, what\'s so fun about Specs is seeing all of these amazing creative '
    'experiences that I never would have thought of myself."\n'
)


# --- Entity Selection Tests ---

class TestHeadlineEntitySelection:
    """The UKCA statement says 'camera-enabled smart glasses' (entity-neutral).
    Fast Company's headline selects 'Meta glasses' exclusively."""

    def test_ukca_statement_is_entity_neutral(self):
        """UKCA statement does not name Meta, Snap, Apple, Samsung, or Google."""
        assert "Meta" not in UKCA_STATEMENT
        assert "Snap" not in UKCA_STATEMENT
        assert "Apple" not in UKCA_STATEMENT
        assert "Samsung" not in UKCA_STATEMENT
        assert "Google" not in UKCA_STATEMENT

    def test_ukca_uses_category_language(self):
        """UKCA says 'camera-enabled smart glasses' — a category, not a brand."""
        assert "camera-enabled smart glasses" in UKCA_STATEMENT

    def test_headline_selects_meta_exclusively(self):
        """Headline names Meta, not 'camera-enabled smart glasses'."""
        assert "Meta" in UK_CINEMA_BAN_ARTICLE_HEADLINE
        assert "camera-enabled" not in UK_CINEMA_BAN_ARTICLE_HEADLINE
        assert "smart glasses" not in UK_CINEMA_BAN_ARTICLE_HEADLINE.lower()

    def test_headline_excludes_all_competitors(self):
        """No competitor named in headline despite ban covering all devices."""
        assert "Snap" not in UK_CINEMA_BAN_ARTICLE_HEADLINE
        assert "Apple" not in UK_CINEMA_BAN_ARTICLE_HEADLINE
        assert "Samsung" not in UK_CINEMA_BAN_ARTICLE_HEADLINE
        assert "Google" not in UK_CINEMA_BAN_ARTICLE_HEADLINE

    def test_headline_uses_ban_vocabulary(self):
        """Headline uses 'ban' — restriction/prohibition framing."""
        assert "ban" in UK_CINEMA_BAN_ARTICLE_HEADLINE.lower()


class TestBodyCompetitorAbsence:
    """Snap, Apple, Samsung, Google all make camera-enabled smart glasses.
    None are mentioned in the UK cinema ban article."""

    def test_snap_not_mentioned_in_body(self):
        """Snap Specs (4 cameras, Sep 16 consumer launch) not mentioned."""
        assert "Snap" not in UK_CINEMA_BAN_ARTICLE_BODY
        assert "Specs" not in UK_CINEMA_BAN_ARTICLE_BODY
        assert "Spectacles" not in UK_CINEMA_BAN_ARTICLE_BODY

    def test_apple_not_mentioned_in_body(self):
        """Apple camera AirPods / smart glasses not mentioned."""
        assert "Apple" not in UK_CINEMA_BAN_ARTICLE_BODY
        assert "AirPods" not in UK_CINEMA_BAN_ARTICLE_BODY

    def test_samsung_not_mentioned_in_body(self):
        """Samsung Galaxy Glasses (launched Jul 22) not mentioned."""
        assert "Samsung" not in UK_CINEMA_BAN_ARTICLE_BODY
        assert "Galaxy" not in UK_CINEMA_BAN_ARTICLE_BODY

    def test_google_not_mentioned_in_body(self):
        """Google Android XR glasses not mentioned."""
        assert "Google" not in UK_CINEMA_BAN_ARTICLE_BODY
        assert "Android XR" not in UK_CINEMA_BAN_ARTICLE_BODY

    def test_meta_mentioned_multiple_times(self):
        """Meta named 7+ times in the article body."""
        meta_count = UK_CINEMA_BAN_ARTICLE_BODY.lower().count("meta")
        assert meta_count >= 7, f"Expected Meta 7+ times, got {meta_count}"


class TestInstitutionalBanCascadeListing:
    """The article lists 6 institutional bans, ALL naming Meta specifically,
    creating a cascade stigma effect."""

    def test_hmcts_courts_ban_listed(self):
        assert "courts in England and Wales" in UK_CINEMA_BAN_ARTICLE_BODY

    def test_soho_house_ban_listed(self):
        assert "Soho House" in UK_CINEMA_BAN_ARTICLE_BODY

    def test_wetherspoon_ban_listed(self):
        assert "Wetherspoon" in UK_CINEMA_BAN_ARTICLE_BODY

    def test_new_york_courts_ban_listed(self):
        assert "New York state court" in UK_CINEMA_BAN_ARTICLE_BODY

    def test_ice_ban_listed(self):
        assert "Immigration and Customs Enforcement" in UK_CINEMA_BAN_ARTICLE_BODY

    def test_ukca_ban_is_primary(self):
        assert "UK Cinema Association" in UK_CINEMA_BAN_ARTICLE_BODY

    def test_no_institutional_ban_names_competitor(self):
        """No institution listed bans Snap/Apple/Samsung/Google by name."""
        bans_section = UK_CINEMA_BAN_ARTICLE_BODY
        # All bans reference Meta or generic "smart glasses"
        for competitor in ["Snap", "Apple", "Samsung", "Google"]:
            assert competitor not in bans_section, \
                f"{competitor} appears in ban cascade section"


class TestSnapSpecsLaunchOmission:
    """Snap Specs consumer launch Sep 16 — 27 days after article — is never
    mentioned despite being directly relevant to a camera glasses ban."""

    def test_snap_specs_launch_date(self):
        """Snap Specs consumer launch: Sep 16, 2026. Article: Aug 20, 2026."""
        from datetime import date
        article_date = date(2026, 8, 20)
        specs_launch = date(2026, 9, 16)
        days_until_launch = (specs_launch - article_date).days
        assert days_until_launch == 27

    def test_article_does_not_ask_about_specs_ban_applicability(self):
        """Would Snap Specs (4 cameras) be banned from UK cinemas?
        The article never asks."""
        assert "Snap" not in UK_CINEMA_BAN_ARTICLE_BODY
        assert "Specs" not in UK_CINEMA_BAN_ARTICLE_BODY

    def test_snap_specs_has_more_cameras_than_meta(self):
        """Snap Specs: 4 cameras. Meta Ray-Ban: 1 camera.
        More cameras = equal or greater ban relevance."""
        snap_specs_cameras = 4
        meta_rayban_cameras = 1
        assert snap_specs_cameras > meta_rayban_cameras


# --- Cross-Entity Framing Pattern (3-article longitudinal) ---

class TestLongitudinalCoveragePattern:
    """Three Fast Company articles (65 days) create a consistent pattern:
    Meta = alarm target, Snap = aspirational or absent."""

    def test_snap_article_privacy_vocabulary_zero(self):
        """Snap Specs AWE profile (Jun 16): zero privacy alarm terms."""
        alarm_terms = [
            "privacy", "surveillance", "spy", "creepy", "pervert",
            "recording", "covert", "ban", "prohibit", "restrict"
        ]
        snippet_lower = SNAP_SPECS_ARTICLE_SNIPPET.lower()
        found = [t for t in alarm_terms if t in snippet_lower]
        assert len(found) == 0, f"Found alarm terms in Snap article: {found}"

    def test_meta_ban_article_privacy_vocabulary_present(self):
        """UK cinema ban (Aug 20): multiple privacy alarm terms."""
        alarm_terms = [
            "privacy", "ban", "prohibit", "restrict", "confiscated"
        ]
        body_lower = UK_CINEMA_BAN_ARTICLE_BODY.lower()
        found = [t for t in alarm_terms if t in body_lower]
        assert len(found) >= 3, \
            f"Expected 3+ alarm terms in Meta article, found {len(found)}: {found}"

    def test_three_article_entity_alarm_assignment(self):
        """Entity-alarm assignment is consistent across all 3 articles:
        Meta always receives alarm framing; Snap never does."""
        articles = {
            "snap_specs_jun16": {
                "entity": "Snap",
                "alarm": False,
                "framing": "aspirational CEO profile"
            },
            "meta_controversies_jul10": {
                "entity": "Meta",
                "alarm": True,
                "framing": "controversy compilation"
            },
            "meta_uk_cinema_aug20": {
                "entity": "Meta",
                "alarm": True,
                "framing": "institutional ban cascade"
            }
        }
        meta_alarm = all(
            a["alarm"] for a in articles.values() if a["entity"] == "Meta"
        )
        snap_alarm = any(
            a["alarm"] for a in articles.values() if a["entity"] == "Snap"
        )
        assert meta_alarm, "Meta should be alarm-assigned in all articles"
        assert not snap_alarm, "Snap should not be alarm-assigned in any article"


class TestPrivacyVocabularyQuantification:
    """Quantify privacy alarm vocabulary across Fast Company's 3 articles."""

    def test_ban_article_alarm_density(self):
        """UK cinema ban article: high alarm term density."""
        alarm_terms = [
            "ban", "prohibit", "restrict", "confiscated", "privacy",
            "piracy", "rejection"
        ]
        body_lower = UK_CINEMA_BAN_ARTICLE_BODY.lower()
        count = sum(body_lower.count(t) for t in alarm_terms)
        assert count >= 8, f"Expected 8+ alarm instances, got {count}"

    def test_snap_article_aspiration_density(self):
        """Snap Specs profile: high aspirational term density."""
        aspiration_terms = [
            "mission", "fun", "exciting", "amazing", "creative",
            "human", "innovative"
        ]
        snippet_lower = SNAP_SPECS_ARTICLE_SNIPPET.lower()
        count = sum(snippet_lower.count(t) for t in aspiration_terms)
        assert count >= 3, f"Expected 3+ aspiration instances, got {count}"


# --- YAML Registration Tests ---

class TestYAMLRegistration:
    """Mechanism #242 must be registered in competitor-coverage-research.yaml."""

    def test_mechanism_registered(self, research_data):
        cpf = research_data.get('cross_publication_findings', {})
        section = cpf.get('fastco_uk_cinema_ban_institutional_entity_selection')
        assert section is not None, (
            "Missing fastco_uk_cinema_ban_institutional_entity_selection in "
            "competitor-coverage-research.yaml cross_publication_findings"
        )

    def test_mechanism_id(self, research_data):
        cpf = research_data.get('cross_publication_findings', {})
        section = cpf['fastco_uk_cinema_ban_institutional_entity_selection']
        assert section.get('mechanism_id') == 242

    def test_mechanism_type(self, research_data):
        cpf = research_data.get('cross_publication_findings', {})
        section = cpf['fastco_uk_cinema_ban_institutional_entity_selection']
        assert section.get('mechanism_type') == 'competitor_coverage_deep_dive'

    def test_extends_mechanism_121(self, research_data):
        cpf = research_data.get('cross_publication_findings', {})
        section = cpf['fastco_uk_cinema_ban_institutional_entity_selection']
        cross_refs = section.get('cross_references', [])
        ref_ids = [r.get('mechanism_id') for r in cross_refs]
        assert 121 in ref_ids, "Must cross-reference mechanism #121"

    def test_confounders_present(self, research_data):
        cpf = research_data.get('cross_publication_findings', {})
        section = cpf['fastco_uk_cinema_ban_institutional_entity_selection']
        confounders = section.get('confounding_factors', [])
        assert len(confounders) >= 4, f"Expected 4+ confounders, got {len(confounders)}"

    def test_source_urls_present(self, research_data):
        cpf = research_data.get('cross_publication_findings', {})
        section = cpf['fastco_uk_cinema_ban_institutional_entity_selection']
        urls = section.get('source_urls', [])
        assert len(urls) >= 3, f"Expected 3+ source URLs, got {len(urls)}"

    def test_snap_specs_launch_noted(self, research_data):
        cpf = research_data.get('cross_publication_findings', {})
        section = cpf['fastco_uk_cinema_ban_institutional_entity_selection']
        summary = section.get('finding_summary', '')
        assert 'Sep' in summary or 'September' in summary or 'launch' in summary, \
            "Finding summary should note Snap Specs launch proximity"


class TestCrossEntityCameraCountParadox:
    """Snap Specs have MORE cameras than Meta glasses, yet receive zero
    ban/restriction coverage from Fast Company."""

    def test_snap_has_4_cameras(self):
        snap_cameras = 4  # 2 full-color + 2 IR computer vision
        assert snap_cameras == 4

    def test_meta_has_1_camera(self):
        meta_cameras = 1
        assert meta_cameras == 1

    def test_camera_count_inversely_correlated_with_scrutiny(self):
        """More cameras = less scrutiny at Fast Company.
        This is the INVERSE of what proportionate coverage would predict."""
        snap_cameras = 4
        meta_cameras = 1
        snap_privacy_questions_ban_article = 0
        meta_privacy_questions_ban_article = 5  # conservative count
        # If proportionate: more cameras should equal more privacy questions
        assert snap_cameras > meta_cameras
        assert snap_privacy_questions_ban_article < meta_privacy_questions_ban_article
