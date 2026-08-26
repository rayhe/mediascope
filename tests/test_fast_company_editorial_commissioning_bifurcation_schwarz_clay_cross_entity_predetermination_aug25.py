"""
Test: Fast Company Editorial Commissioning Bifurcation — Hunter Schwarz Design Contributor
vs Dan Clay Branding Consultant Cross-Entity Story Assignment Privacy Vocabulary Predetermination

Mechanism #309

Hypothesis: Fast Company assigns different TYPES of contributors to predetermine
coverage framing for different tech entities. Design contributors get aspirational
angles (Google/Warby Parker), external branding consultants get adversarial literary
essays (Meta). The assignment IS the framing — vocabulary outcomes are predetermined
by who is commissioned to write.

Natural experiment: Same publication (Fast Company), same product category
(camera-equipped smart glasses), same 2026 window.

Hunter Schwarz (design contributor):
- Google/Warby Parker (May 2026): aspirational product journalism, CEO quotes,
  design details, camera mentioned once in features list, ONE generic privacy
  sentence, ZERO alarm terms
- Meta/Alan Dye hire (2026): neutral/positive — "serious about designing hardware"
- Anthropic/Claude Design (Fast Company ME): aspirational — "gives vibe coders
  more control"

Dan Clay (Lippincott brand strategist, novelist, NOT tech journalist):
- Meta smart glasses (Aug 25, 2026): literary essay, 10 distinct alarm/surveillance
  terms, panopticon metaphor, Irish castle prison metaphor, "algorithm chow" coinage

Source URLs:
- Hunter Schwarz (May 2026): https://www.fastcompany.com/91544045/warby-parker-google-intelligent-eyewear
- Dan Clay (Aug 25, 2026): https://www.fastcompany.com/91594615/metas-creepy-smart-glasses-are-part-of-a-much-bigger-plan
- Schwarz author page: https://www.fastcompany.com/user/hschwarz
- Dan Clay author page: https://www.fastcompany.com/user/dan-clay
"""

import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


class TestEditorialCommissioningBifurcation:
    """Verify the editorial commissioning pattern exists in profiles."""

    def test_mechanism_309_exists(self):
        """Mechanism #309 must be documented."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        # Search all keys for mechanism 309
        found = False
        def search_dict(d):
            nonlocal found
            if isinstance(d, dict):
                if d.get('mechanism_id') == 309 or d.get('mechanism_number') == 309:
                    found = True
                    return
                for v in d.values():
                    search_dict(v)
            elif isinstance(d, list):
                for item in d:
                    search_dict(item)
        search_dict(data)
        assert found, "Mechanism #309 (Fast Company Editorial Commissioning Bifurcation) not found"

    def test_mechanism_type_is_journalist_cross_entity(self):
        """Mechanism type should be journalist_cross_entity_tracking or editorial_commissioning."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        found_type = None
        def search_dict(d):
            nonlocal found_type
            if isinstance(d, dict):
                if d.get('mechanism_id') == 309:
                    found_type = d.get('type', '')
                    return
                for v in d.values():
                    search_dict(v)
            elif isinstance(d, list):
                for item in d:
                    search_dict(item)
        search_dict(data)
        assert found_type is not None
        assert 'commissioning' in found_type or 'journalist' in found_type or 'editorial' in found_type


class TestSchwarzCrossEntityCoverage:
    """Verify Hunter Schwarz cross-entity coverage patterns."""

    def test_schwarz_google_warby_parker_aspirational(self):
        """Schwarz Google/Warby Parker article should be documented as aspirational."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        found = False
        def search_dict(d):
            nonlocal found
            if isinstance(d, dict):
                if d.get('mechanism_id') == 309:
                    finding = str(d.get('finding', ''))
                    if 'Schwarz' in finding and ('aspirational' in finding.lower() or 'design' in finding.lower()):
                        found = True
                    return
                for v in d.values():
                    search_dict(v)
            elif isinstance(d, list):
                for item in d:
                    search_dict(item)
        search_dict(data)
        assert found, "Schwarz aspirational Google/Warby Parker coverage not documented"

    def test_schwarz_privacy_analysis_zero_for_google(self):
        """Schwarz article should document zero alarm terms for Google cameras."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        found = False
        def search_dict(d):
            nonlocal found
            if isinstance(d, dict):
                if d.get('mechanism_id') == 309:
                    finding = str(d.get('finding', ''))
                    if 'zero' in finding.lower() and ('alarm' in finding.lower() or 'privacy' in finding.lower()):
                        found = True
                    return
                for v in d.values():
                    search_dict(v)
            elif isinstance(d, list):
                for item in d:
                    search_dict(item)
        search_dict(data)
        assert found, "Zero privacy alarm terms for Google not documented in mechanism 309"


class TestDanClayContributorType:
    """Verify Dan Clay contributor type analysis."""

    def test_dan_clay_not_tech_journalist(self):
        """Dan Clay should be documented as branding consultant, not tech journalist."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        found = False
        def search_dict(d):
            nonlocal found
            if isinstance(d, dict):
                if d.get('mechanism_id') == 309:
                    finding = str(d.get('finding', ''))
                    if ('Lippincott' in finding or 'branding' in finding.lower() or 'consultant' in finding.lower()):
                        found = True
                    return
                for v in d.values():
                    search_dict(v)
            elif isinstance(d, list):
                for item in d:
                    search_dict(item)
        search_dict(data)
        assert found, "Dan Clay Lippincott/branding consultant identity not documented"

    def test_dan_clay_alarm_term_count(self):
        """Dan Clay Meta article should document 10+ alarm terms."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        found = False
        def search_dict(d):
            nonlocal found
            if isinstance(d, dict):
                if d.get('mechanism_id') == 309:
                    finding = str(d.get('finding', ''))
                    if '10' in finding and ('alarm' in finding.lower() or 'surveillance' in finding.lower()):
                        found = True
                    return
                for v in d.values():
                    search_dict(v)
            elif isinstance(d, list):
                for item in d:
                    search_dict(item)
        search_dict(data)
        assert found, "Dan Clay 10 alarm terms not documented in mechanism 309"


class TestFinancialContextDocumented:
    """Verify financial context for editorial commissioning is documented."""

    def test_google_advertising_relationship_documented(self):
        """Google programmatic ad dependency should be noted."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        found = False
        def search_dict(d):
            nonlocal found
            if isinstance(d, dict):
                if d.get('mechanism_id') == 309:
                    context = str(d.get('financial_context', ''))
                    if 'Google' in context and ('advertising' in context.lower() or 'programmatic' in context.lower() or 'search' in context.lower()):
                        found = True
                    return
                for v in d.values():
                    search_dict(v)
            elif isinstance(d, list):
                for item in d:
                    search_dict(item)
        search_dict(data)
        assert found, "Google advertising relationship not in financial_context"

    def test_meta_competitor_relationship_documented(self):
        """Meta advertising competition should be noted."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        found = False
        def search_dict(d):
            nonlocal found
            if isinstance(d, dict):
                if d.get('mechanism_id') == 309:
                    context = str(d.get('financial_context', ''))
                    if 'Meta' in context and 'compet' in context.lower():
                        found = True
                    return
                for v in d.values():
                    search_dict(v)
            elif isinstance(d, list):
                for item in d:
                    search_dict(item)
        search_dict(data)
        assert found, "Meta advertising competition not in financial_context"


class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    def test_cross_references_mechanism_308(self):
        """Should cross-reference mechanism #308 (same-publication vocabulary bifurcation)."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        found = False
        def search_dict(d):
            nonlocal found
            if isinstance(d, dict):
                if d.get('mechanism_id') == 309:
                    refs = d.get('extends_mechanisms', [])
                    for ref in refs:
                        if isinstance(ref, dict) and ref.get('mechanism_id') == 308:
                            found = True
                    return
                for v in d.values():
                    search_dict(v)
            elif isinstance(d, list):
                for item in d:
                    search_dict(item)
        search_dict(data)
        assert found, "Should cross-reference mechanism #308"

    def test_cross_references_mechanism_15(self):
        """Should cross-reference mechanism #15 (Fast Company Snap vs Meta)."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        found = False
        def search_dict(d):
            nonlocal found
            if isinstance(d, dict):
                if d.get('mechanism_id') == 309:
                    refs = d.get('extends_mechanisms', [])
                    for ref in refs:
                        if isinstance(ref, dict) and ref.get('mechanism_id') == 15:
                            found = True
                    return
                for v in d.values():
                    search_dict(v)
            elif isinstance(d, list):
                for item in d:
                    search_dict(item)
        search_dict(data)
        assert found, "Should cross-reference mechanism #15"
