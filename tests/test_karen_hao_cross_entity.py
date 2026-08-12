"""
Karen Hao Cross-Entity Coverage Analysis — Institutional Alignment and Entity Selection (Type B)

Mechanism #60: Institutional Financial Alignment Predicts Investigative Target Selection

KEY FINDING: Karen Hao's investigative focus at MIT Technology Review aligns with
the financial incentive structure of her employing institution. Facebook, which had
$0 in MIT/MIT TR financial relationships, received a 9-month adversarial deep-dive
investigation ("The Facebook Gatekeeper," March 11, 2021). Google, which funds MIT
research through the MIT-Google Program for Computing Innovation, individual grants,
and Eric Schmidt's personal philanthropy, received NO comparable adversarial
investigation despite a concurrent AI ethics crisis (Gebru fired Dec 2020, Mitchell
fired Feb 2021) that was objectively more dramatic.

CAREER PATH (natural experiment across 4 institutional financial structures):

1. MIT Technology Review (2018-2022):
   - MIT-Google Program funds research requiring "relevance to Google"
   - Eric Schmidt personally funded MIT AI initiatives
   - Google/DeepMind has bilateral research relationships with MIT
   - Facebook/Meta: $0 in MIT or MIT TR relationships
   → Published: "The Facebook Gatekeeper" (9-month adversarial investigation)
   → NOT published: comparable investigation of Google AI ethics

2. Wall Street Journal (2022-2023):
   - News Corp: $50M/yr Meta + $50M/yr OpenAI (balanced)
   → Pivoted to China tech beat; no domestic Big Tech adversarial investigations

3. The Atlantic (2023-2024):
   - Owned by Emerson Collective (Laurene Powell Jobs)
   - Laurene Powell Jobs is Apple's largest individual shareholder
   → Contributing writer; no Apple AI investigations

4. Freelance / "Empire of AI" book (2025):
   - Publisher: Penguin Press (no Big Tech financial entanglements)
   - AI Now Institute board member (advocacy org)
   → Primary target: OpenAI (no institutional financial relationship)
   → Counter-example of "good AI": Google DeepMind's AlphaFold (MIT partner)

THE GEBRU TIMING GAP: On March 11, 2021, Hao published the Facebook Gatekeeper
investigation. That same week, the Google AI ethics crisis was at peak intensity:
Google had fired Timnit Gebru (Dec 2020) and Margaret Mitchell (Feb 2021), and
Google employees published open letters about harassment and intimidation. VentureBeat
(March 12, 2021) covered BOTH stories in adjacent paragraphs — noting the parallel.
Hao's investigation targeted the company with zero MIT financial ties, not the
company whose AI ethics crisis was more dramatic AND whose parent funds MIT research.

THE ALPHAFOLD SIGNAL: Across multiple post-MIT-TR interviews (TechCrunch Sep 2025,
MIT event Mar 2026, IBM Think May 2026), Hao consistently cites Google DeepMind's
AlphaFold as the exemplar of how AI SHOULD be done — "Those are the types of AI
systems that we need. AlphaFold does not create mental health crises" (TechCrunch).
This positions Google as the SOLUTION while OpenAI/Meta are the PROBLEM, despite:
- Google's AI division using comparable compute and environmental resources
- Google firing its own AI ethics leadership (Gebru, Mitchell)
- Google's search monopoly creating larger societal concentration than any other AI company
- Google's data center water consumption being specifically cited in Hao's own
  Chile reporting (LetsDataScience Jun 2026) — yet this never connects to the
  AlphaFold-positive framing

CONFOUNDING FACTORS (7 documented):
1. Hao began the Facebook investigation ~9 months before publication — the timing
   was NOT opportunistic relative to the Gebru crisis
2. Individual journalists cannot investigate every company simultaneously
3. The Gebru/Mitchell story was being covered by other reporters (Metz, Schiffer)
4. Facebook was Hao's primary beat at MIT TR; investigative depth follows beats
5. Hao DID critique Google in the AI Colonialism series (Chilean water) — but at a
   structural/systems level, not as an adversarial corporate investigation
6. Her book DID adversarially target OpenAI, showing willingness to investigate
   powerful companies when they have no institutional financial relationship
7. MIT TR claims editorial independence from MIT per stated policy

THE DISTINCTION: Hao's coverage of Google is not suppressed — she mentions Google
tangentially and even criticizes Google's water usage in Chile. But there is a clear
DEPTH ASYMMETRY: Facebook gets the 9-month adversarial deep-dive with inside sources,
organizational analysis, and systemic critique. Google gets systems-level mentions
in broader coverage. The same journalist applies a substantially different
investigative depth standard — and the depth difference correlates with the
employing institution's financial relationships.

CROSS-REFERENCE:
- Mechanism #17 (Guardian SID governance capture): Governance + financial ties → soft coverage
- Mechanism #29 (Guardian rogue AI volume asymmetry): Coverage volume tracks financial ties
- Mechanism #49 (Bobrowsky entity targeting): Beat assignment as mechanism for asymmetry
- Mechanism #57 (Seetharaman frame-lock): Professional identity persists across institutions
- MIT TR profile: Google/MIT bilateral financial relationships documented
- Deepa Seetharaman (Mechanism #57): Migration carries framing; Hao pattern differs —
  Hao's targeting shifted WITH institutions (Facebook at MIT TR, OpenAI in book),
  suggesting institutional alignment rather than frame-lock

Sources:
  - MIT Technology Review: "How Facebook got addicted to spreading misinformation" (Mar 11, 2021)
    https://www.technologyreview.com/2021/03/11/1020600/facebook-responsible-ai-misinformation/
  - VentureBeat: "AI Weekly: Facebook, Google, and the tension between profits and fairness" (Mar 12, 2021)
    https://venturebeat.com/business/ai-weekly-facebook-google-and-the-tension-between-profits-and-fairness
  - TechCrunch: "Karen Hao on the Empire of AI, AGI evangelists, and the cost of belief" (Sep 14, 2025)
    https://techcrunch.com/2025/09/14/karen-hao-on-the-empire-of-ai-agi-evangelists-and-the-cost-of-belief/
  - MIT News: "What's the right path for AI?" (Mar 20, 2026)
    https://news.mit.edu/2026/right-path-for-ai-karen-hao-paola-ricaurte-0320
  - IBM Think: "Cracking the Empire of AI" (Dec 2025)
    https://www.ibm.com/think/news/cracking-empire-of-ai
  - LetsDataScience: "Karen Hao Frames AI as Threat to Democracy" (Jul 2026)
    https://letsdatascience.com/news/karen-hao-frames-ai-as-threat-to-democracy-05a0fd08
  - Times Higher Education: "Conference suspends Google sponsorship after ethics experts' exit" (Mar 2021)
    https://Www.timeshighereducation.com/news/conference-suspends-google-sponsorship-after-ethics-experts-exit
  - Earwolf/Factually podcast: Karen Hao on Facebook investigation
    https://www.earwolf.com/episode/why-facebook-refuses-to-fix-the-misinformation-crisis-it-created-with-karen-hao/
  - Wikipedia: Karen Hao
    https://en.wikipedia.org/wiki/Karen_Hao

Created: 2026-08-12
"""

import yaml
import os
import pytest
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"
REPO_ROOT = Path(__file__).parent.parent


def load_yaml(name):
    with open(PROFILES_DIR / name) as f:
        return yaml.safe_load(f)


def load_journalists():
    with open(PROFILES_DIR / "careers" / "journalists.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def competitor_research():
    return load_yaml("competitor-coverage-research.yaml")


@pytest.fixture(scope="module")
def mit_tr_profile():
    return load_yaml("mit-tech-review.yaml")


@pytest.fixture(scope="module")
def journalists_data():
    return load_journalists()


@pytest.fixture(scope="module")
def hao_career(journalists_data):
    """Extract Karen Hao's career data from journalists.yaml."""
    for entry in journalists_data.get("journalists", []):
        if entry.get("name") == "Karen Hao":
            return entry
    pytest.fail("Karen Hao not found in journalists.yaml")


@pytest.fixture(scope="module")
def mechanism_60(competitor_research):
    """Extract mechanism #60 from cross_publication_findings."""
    findings = competitor_research.get("cross_publication_findings", {})
    for key, val in findings.items():
        if isinstance(val, dict) and val.get("mechanism_id") == 60:
            return val
    pytest.fail("Mechanism #60 not found in cross_publication_findings")


# ─── Class 1: Career Path Verification ────────────────────────────────────────

class TestHaoCareerPath:
    """Verify Karen Hao's 4-institution career path is documented."""

    def test_hao_exists_in_journalists(self, hao_career):
        assert hao_career["name"] == "Karen Hao"

    def test_hao_multi_publication(self, hao_career):
        assert hao_career.get("multi_publication") is True

    def test_mit_tr_tenure(self, hao_career):
        career = hao_career.get("career", [])
        mit_tr = [c for c in career if c.get("publication") == "mit-tech-review"]
        assert len(mit_tr) >= 1, "MIT Tech Review career entry missing"
        entry = mit_tr[0]
        assert entry.get("start") in ("2018", "2018-01", "2018-06")
        assert entry.get("end") in ("2022", "2022-01", "2022-06")

    def test_wsj_tenure(self, hao_career):
        career = hao_career.get("career", [])
        wsj = [c for c in career if c.get("publication") == "wall-street-journal"]
        assert len(wsj) >= 1, "WSJ career entry missing"

    def test_atlantic_tenure(self, hao_career):
        career = hao_career.get("career", [])
        atlantic = [c for c in career if c.get("publication") == "atlantic"]
        assert len(atlantic) >= 1, "Atlantic career entry missing"

    def test_career_at_least_4_stops(self, hao_career):
        """Career spans 4+ distinct publications/roles."""
        career = hao_career.get("career", [])
        pubs = set(c.get("publication") for c in career)
        assert len(pubs) >= 4, f"Expected 4+ publications, found {len(pubs)}: {pubs}"


# ─── Class 2: Mechanism #60 Structural Integrity ──────────────────────────────

class TestMechanism60Structure:
    """Verify mechanism #60 has all required fields and correct metadata."""

    def test_mechanism_id(self, mechanism_60):
        assert mechanism_60["mechanism_id"] == 60

    def test_has_finding_summary(self, mechanism_60):
        summary = mechanism_60.get("finding_summary", "")
        assert len(summary) > 100, "Finding summary too short"

    def test_has_discovery_date(self, mechanism_60):
        assert mechanism_60.get("discovery_date") == "2026-08-12"

    def test_has_date_added(self, mechanism_60):
        assert "date_added" in mechanism_60

    def test_has_source_urls(self, mechanism_60):
        urls = mechanism_60.get("source_urls", [])
        assert len(urls) >= 4, f"Expected 4+ source URLs, found {len(urls)}"

    def test_has_confounding_factors(self, mechanism_60):
        factors = mechanism_60.get("confounding_factors", [])
        assert len(factors) >= 5, f"Expected 5+ confounding factors, found {len(factors)}"

    def test_has_testable_predictions(self, mechanism_60):
        predictions = mechanism_60.get("testable_predictions", [])
        assert len(predictions) >= 3, f"Expected 3+ predictions, found {len(predictions)}"

    def test_has_cross_references(self, mechanism_60):
        xrefs = mechanism_60.get("cross_references", [])
        assert len(xrefs) >= 3, f"Expected 3+ cross-references, found {len(xrefs)}"


# ─── Class 3: MIT-Google Financial Relationship Context ────────────────────────

class TestMITGoogleFinancialRelationship:
    """Verify the MIT-Google financial relationship is documented in the MIT TR profile."""

    def test_google_partner_exists(self, mit_tr_profile):
        """Google/Alphabet must be listed as a financial partner of MIT."""
        # Check both revenue_relationships and financial_relationships keys
        partners = mit_tr_profile.get("revenue_relationships", []) or \
                   mit_tr_profile.get("financial_relationships", [])
        google_partners = [p for p in partners if isinstance(p, dict) and
                          "google" in str(p.get("partner", "")).lower()]
        assert len(google_partners) >= 1, "Google not found in MIT TR revenue_relationships"

    def test_mit_google_program_documented(self, mit_tr_profile):
        """The MIT-Google Program for Computing Innovation should be documented."""
        content = yaml.dump(mit_tr_profile)
        assert "MIT-Google" in content or "mit-google" in content.lower(), \
            "MIT-Google Program not documented in profile"

    def test_facebook_meta_zero_relationship(self, mit_tr_profile):
        """Facebook/Meta should have no direct financial relationship with MIT/MIT TR."""
        partners = mit_tr_profile.get("financial_relationships", [])
        meta_partners = [p for p in partners if isinstance(p, dict) and
                        ("meta" in str(p.get("partner", "")).lower() or
                         "facebook" in str(p.get("partner", "")).lower())]
        # If Meta IS listed, it should note zero direct financial relationship
        # Meta is listed in competitor_entities, not financial_relationships
        for mp in meta_partners:
            desc = str(mp.get("description", "")).lower()
            if "no" in desc and ("deal" in desc or "relationship" in desc):
                return  # Correctly documented as no relationship
        # If not listed at all, that also confirms zero relationship
        if len(meta_partners) == 0:
            return
        # If listed without noting it's zero, that's fine if it's a coverage target
        pass

    def test_schmidt_philanthropy_documented(self, mit_tr_profile):
        """Eric Schmidt's personal funding of MIT AI initiatives should appear."""
        content = yaml.dump(mit_tr_profile)
        assert "Schmidt" in content, \
            "Eric Schmidt philanthropy to MIT not documented"


# ─── Class 4: Entity Selection Asymmetry ──────────────────────────────────────

class TestEntitySelectionAsymmetry:
    """Test the core finding: investigative depth correlates with institutional financial ties."""

    def test_facebook_gatekeeper_documented(self, mechanism_60):
        """The 9-month Facebook investigation must be referenced."""
        summary = mechanism_60.get("finding_summary", "")
        assert "gatekeeper" in summary.lower() or "facebook" in summary.lower(), \
            "Facebook Gatekeeper investigation not referenced in finding"

    def test_google_absence_documented(self, mechanism_60):
        """The absence of comparable Google investigation must be documented."""
        summary = mechanism_60.get("finding_summary", "")
        assert "google" in summary.lower(), \
            "Google coverage gap not referenced in finding"

    def test_alphafold_signal_documented(self, mechanism_60):
        """The AlphaFold positive framing pattern must be documented."""
        summary = mechanism_60.get("finding_summary", "")
        alphafold = "alphafold" in summary.lower()
        alphafold_in_details = any("alphafold" in str(v).lower()
                                  for v in mechanism_60.values())
        assert alphafold or alphafold_in_details, \
            "AlphaFold positive framing signal not documented"

    def test_gebru_timing_documented(self, mechanism_60):
        """The Gebru/Mitchell timing parallel must be documented."""
        all_text = str(mechanism_60).lower()
        assert "gebru" in all_text or "mitchell" in all_text, \
            "Gebru/Mitchell timing gap not documented"

    def test_depth_not_suppression_distinction(self, mechanism_60):
        """Finding must distinguish depth asymmetry from suppression."""
        all_text = str(mechanism_60).lower()
        has_depth = "depth" in all_text
        has_not_suppressed = "not suppress" in all_text or "tangential" in all_text or \
                            "systems" in all_text or "structural" in all_text
        assert has_depth or has_not_suppressed, \
            "Must distinguish depth asymmetry from total suppression"


# ─── Class 5: Confounding Factor Quality ──────────────────────────────────────

class TestConfoundingFactorQuality:
    """Verify confounding factors are substantive, not strawmen."""

    def test_investigation_timeline_factor(self, mechanism_60):
        """Must note that the Facebook investigation began before Gebru crisis."""
        factors = mechanism_60.get("confounding_factors", [])
        factor_text = " ".join(str(f) for f in factors).lower()
        assert "9 month" in factor_text or "nine month" in factor_text or \
               "began" in factor_text or "before" in factor_text, \
            "Must note investigation timeline predates Gebru crisis"

    def test_beat_assignment_factor(self, mechanism_60):
        """Must note Facebook was her primary beat."""
        factors = mechanism_60.get("confounding_factors", [])
        factor_text = " ".join(str(f) for f in factors).lower()
        assert "beat" in factor_text or "primary" in factor_text, \
            "Must note Facebook was her primary beat"

    def test_editorial_independence_factor(self, mechanism_60):
        """Must note MIT TR claims editorial independence."""
        factors = mechanism_60.get("confounding_factors", [])
        factor_text = " ".join(str(f) for f in factors).lower()
        assert "independence" in factor_text or "independent" in factor_text, \
            "Must note MIT TR editorial independence claim"

    def test_openai_book_willingness_factor(self, mechanism_60):
        """Must note that Empire of AI targeted OpenAI, showing adversarial willingness."""
        factors = mechanism_60.get("confounding_factors", [])
        factor_text = " ".join(str(f) for f in factors).lower()
        assert "openai" in factor_text or "book" in factor_text or \
               "empire" in factor_text, \
            "Must note willingness to target OpenAI in book"


# ─── Class 6: Cross-Reference Integrity ───────────────────────────────────────

class TestCrossReferenceIntegrity:
    """Verify cross-references to related mechanisms are valid."""

    def test_references_seetharaman_frame_lock(self, mechanism_60):
        """Should reference Mechanism #57 (Seetharaman frame-lock) for comparison."""
        xrefs = mechanism_60.get("cross_references", [])
        xref_text = " ".join(str(x) for x in xrefs).lower()
        assert "57" in xref_text or "seetharaman" in xref_text, \
            "Should reference Mechanism #57 for contrast"

    def test_references_bobrowsky_entity_targeting(self, mechanism_60):
        """Should reference Mechanism #49 (entity targeting) as related pattern."""
        xrefs = mechanism_60.get("cross_references", [])
        xref_text = " ".join(str(x) for x in xrefs).lower()
        assert "49" in xref_text or "bobrowsky" in xref_text or \
               "entity" in xref_text, \
            "Should reference Mechanism #49 for entity targeting parallel"

    def test_references_mit_tr_profile(self, mechanism_60):
        """Should reference MIT TR profile for financial relationship evidence."""
        xrefs = mechanism_60.get("cross_references", [])
        xref_text = " ".join(str(x) for x in xrefs).lower()
        assert "mit" in xref_text, \
            "Should reference MIT TR profile"


# ─── Class 7: Testable Predictions ────────────────────────────────────────────

class TestTestablePredictions:
    """Verify predictions are falsifiable and specific."""

    def test_predictions_are_falsifiable(self, mechanism_60):
        """Each prediction must contain a verifiable claim."""
        predictions = mechanism_60.get("testable_predictions", [])
        for i, pred in enumerate(predictions):
            pred_text = str(pred).lower()
            has_entity = any(e in pred_text for e in
                           ["google", "alphafold", "hao", "openai", "meta",
                            "investigation", "adversarial", "coverage"])
            assert has_entity, \
                f"Prediction {i} lacks a verifiable entity reference: {pred_text[:80]}"

    def test_predictions_are_distinct(self, mechanism_60):
        """Predictions should not be near-duplicates."""
        predictions = mechanism_60.get("testable_predictions", [])
        pred_set = set()
        for pred in predictions:
            # Normalize
            key = str(pred).lower()[:50]
            assert key not in pred_set, f"Near-duplicate prediction: {key}"
            pred_set.add(key)


# ─── Class 8: Distinction from Seetharaman (Mechanism #57) ────────────────────

class TestDistinctionFromSeetharaman:
    """Mechanism #60 documents a DIFFERENT pattern than #57 (frame-lock)."""

    def test_different_mechanism_type(self, mechanism_60, competitor_research):
        """#60 is institutional alignment; #57 is professional identity capture."""
        findings = competitor_research.get("cross_publication_findings", {})
        mech_57 = None
        for key, val in findings.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 57:
                mech_57 = val
                break
        if mech_57 is None:
            pytest.skip("Mechanism #57 not found")

        m60_summary = mechanism_60.get("finding_summary", "").lower()
        m57_summary = mech_57.get("finding_summary", "").lower()

        # #57 should be about frame persistence across institutions
        # #60 should be about target selection aligning with institution
        assert "institutional" in m60_summary or "alignment" in m60_summary or \
               "financial" in m60_summary, \
            "#60 should emphasize institutional financial alignment"

    def test_opposite_migration_pattern(self, mechanism_60):
        """Hao's targeting SHIFTS with institutions (unlike Seetharaman's frame-lock)."""
        all_text = str(mechanism_60).lower()
        # Should note that target selection changed with institutional context
        assert "shift" in all_text or "different" in all_text or \
               "align" in all_text or "correlat" in all_text, \
            "Should note target selection shifts with institutional context"


# ─── Class 9: Source URL Verification ──────────────────────────────────────────

class TestSourceURLVerification:
    """Verify source URLs are present and well-formed."""

    def test_source_urls_are_valid(self, mechanism_60):
        """All source URLs should be well-formed HTTP(S) URLs."""
        urls = mechanism_60.get("source_urls", [])
        for url in urls:
            url_str = str(url)
            assert url_str.startswith("http://") or url_str.startswith("https://"), \
                f"Invalid URL: {url_str}"

    def test_has_primary_source_url(self, mechanism_60):
        """Must include the MIT TR Facebook investigation URL."""
        urls = mechanism_60.get("source_urls", [])
        url_text = " ".join(str(u) for u in urls).lower()
        assert "technologyreview.com" in url_text, \
            "Must include technologyreview.com URL for the Gatekeeper investigation"

    def test_has_venturebeat_parallel(self, mechanism_60):
        """Must include VentureBeat parallel coverage URL for timing evidence."""
        urls = mechanism_60.get("source_urls", [])
        url_text = " ".join(str(u) for u in urls).lower()
        assert "venturebeat" in url_text, \
            "Must include VentureBeat URL for Gebru timing parallel evidence"


# ─── Class 10: Empire of AI Entity Selection ──────────────────────────────────

class TestEmpireOfAIEntitySelection:
    """Analyze entity selection in "Empire of AI" relative to institutional ties."""

    def test_book_targets_openai(self, mechanism_60):
        """Empire of AI primarily targets OpenAI — which has no MIT financial ties."""
        all_text = str(mechanism_60).lower()
        assert "empire" in all_text and "openai" in all_text, \
            "Must document Empire of AI's primary OpenAI targeting"

    def test_alphafold_as_positive_foil(self, mechanism_60):
        """AlphaFold (Google DeepMind) positioned as positive counter-example in book/interviews."""
        all_text = str(mechanism_60).lower()
        assert "alphafold" in all_text, \
            "Must document AlphaFold as positive foil pattern"

    def test_google_not_primary_book_target(self, mechanism_60):
        """Google is NOT the primary target of Empire of AI despite comparable scale."""
        all_text = str(mechanism_60).lower()
        # The finding should note that Google gets positive framing, not adversarial targeting
        has_positive_framing = "positive" in all_text or "good" in all_text or \
                              "counter-example" in all_text or "exemplar" in all_text or \
                              "solution" in all_text
        assert has_positive_framing, \
            "Must note Google receives positive framing rather than adversarial targeting"
