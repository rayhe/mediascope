"""
Test Mechanism #85 follow-up (Type B #488): Chris Welch Within-Journalist
Meta vs Samsung Privacy Vocabulary Contrast

Type B: Journalist Cross-Entity Tracking — September 3, 2026

KEY FINDING: Mechanism #85 established that adversarial smart-glasses privacy
framing did not travel with Chris Welch from The Verge to Bloomberg, using a
between-person comparison (Welch's neutral Samsung coverage vs his former Verge
colleagues' adversarial Meta coverage). Type B #488 tightens this to a
WITHIN-JOURNALIST comparison in Welch's own byline, and corrects the journalist
profile in the process.

Correction: profiles/careers/journalists.yaml previously recorded Welch's
Verge-era Meta-glasses adversarial piece count as 0 ("product reviewer, NOT
privacy investigator"). That was wrong. On May 1 2025, writing for The Verge,
Welch authored "Meta tightens privacy policy around Ray-Ban glasses to boost AI
training," covering the April 29 2025 Ray-Ban Meta privacy policy update (Hey
Meta default-on, voice-recording cloud-storage opt-out removed, 1-year
retention). His own copy used adversarial privacy vocabulary:

- "giving Meta AI a more frequent view of the world"
- "Meta will frequently be analyzing whatever's captured by the built-in camera"
- "Meta is taking after Amazon by no longer allowing Ray-Ban Meta owners to opt out"
- "The motivation behind these changes is clear: Meta wants to continue providing
  its AI models with heaps of data on which to train and improve subsequent results"

Fourteen months later at Bloomberg (Jul 22 2026), Welch covered Samsung Galaxy
Glasses at Galaxy Unpacked: camera-equipped glasses whose Gemini AI analyzes the
wearer's camera feed in real time (structurally equivalent or greater AI-camera
data collection surface than the Ray-Ban Meta policy he criticized). His
Bloomberg framing was neutral-positive with privacy as a product attribute and
zero adversarial vocabulary (Techmeme lead story).

The adversarial privacy register appears in Welch's Verge output and is absent
from his Bloomberg output for structurally similar hardware. This weakens
mechanism #85's MODERATE confounder ("Welch was a product reviewer, not a
privacy investigator; he may not have written adversarial privacy pieces even if
he stayed at The Verge") because he demonstrably did write one. New MODERATE
confounder recorded: genre asymmetry (privacy-policy rollback vs product launch).

Sources:
- Techmeme citation (byline/date/headline): https://www.techmeme.com/250501/p23
- Full-text mirror of the Verge piece: https://old.thelemmy.club/comment/18411988?source
- Security Now #1024 transcript (verbatim quotes): http://www.grc.com/sn/sn-1024.htm
- TechCrunch follow-up citing "according to The Verge":
  https://techcrunch.com/2025/04/30/if-you-own-ray-ban-meta-glasses-you-should-double-check-your-privacy-settings/
- Samsung Galaxy Glasses (Gemini real-time camera analysis):
  https://www.macrumors.com/2026/05/13/samsung-ai-smart-glasses-july/
"""

import os
import pytest
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')) as f:
        return yaml.safe_load(f)


def get_welch_profile(data):
    for j in data.get('journalists', []):
        if j.get('name') == 'Chris Welch':
            return j
    return None


def get_welch_mechanism(research):
    cpf = research.get('cross_publication_findings', {})
    return cpf.get('bloomberg_chris_welch_career_migration', {})


def get_verge_era(profile):
    return profile.get('competitor_coverage', {}).get('meta_glasses', {}).get('verge_era', {})


# ===================================================================
# Test Class 1: Verge-Era Adversarial Piece Corrected in Profile
# ===================================================================
class TestVergeEraCorrection:
    """The journalists.yaml profile must reflect the corrected adversarial count."""

    def test_adversarial_count_corrected(self):
        profile = get_welch_profile(load_journalists())
        verge_era = get_verge_era(profile)
        assert verge_era.get('adversarial_pieces') == 1, \
            f"Verge-era adversarial_pieces must be corrected to 1, got {verge_era.get('adversarial_pieces')}"

    def test_flagship_piece_title(self):
        verge_era = get_verge_era(get_welch_profile(load_journalists()))
        piece = verge_era.get('flagship_piece', {})
        assert 'privacy policy' in piece.get('title', '').lower(), \
            "Flagship piece must be the Ray-Ban Meta privacy policy article"

    def test_flagship_piece_date(self):
        verge_era = get_verge_era(get_welch_profile(load_journalists()))
        piece = verge_era.get('flagship_piece', {})
        assert piece.get('date') == '2025-05-01', \
            f"Piece date must be 2025-05-01, got {piece.get('date')}"

    def test_flagship_piece_byline(self):
        verge_era = get_verge_era(get_welch_profile(load_journalists()))
        piece = verge_era.get('flagship_piece', {})
        assert piece.get('author_byline') == 'Chris Welch', \
            "Byline must be Chris Welch himself (within-journalist design)"
        assert piece.get('publication') == 'the-verge', \
            "Publication must be the-verge (pre-migration)"

    def test_flagship_piece_subject(self):
        """Subject must be the April 29 2025 policy update specifics."""
        verge_era = get_verge_era(get_welch_profile(load_journalists()))
        piece = verge_era.get('flagship_piece', {})
        subject = piece.get('subject', '').lower()
        assert 'hey meta' in subject and 'opt-out' in subject.replace('_', '-'), \
            f"Subject must name the Hey Meta default-on and opt-out removal, got: {subject}"

    def test_adversarial_vocabulary_documented(self):
        verge_era = get_verge_era(get_welch_profile(load_journalists()))
        piece = verge_era.get('flagship_piece', {})
        vocab = piece.get('adversarial_vocabulary', [])
        assert len(vocab) >= 4, \
            f"Must document >=4 adversarial vocabulary markers, got {len(vocab)}"

    def test_heaps_of_data_quote_present(self):
        """The single most adversarial line must be captured verbatim."""
        verge_era = get_verge_era(get_welch_profile(load_journalists()))
        vocab_text = ' '.join(verge_era.get('flagship_piece', {}).get('adversarial_vocabulary', [])).lower()
        assert 'heaps of data' in vocab_text, \
            "Must capture the 'heaps of data' motive-attribution line"

    def test_taking_after_amazon_quote_present(self):
        verge_era = get_verge_era(get_welch_profile(load_journalists()))
        vocab_text = ' '.join(verge_era.get('flagship_piece', {}).get('adversarial_vocabulary', [])).lower()
        assert 'taking after amazon' in vocab_text, \
            "Must capture the 'taking after Amazon' peer-shaming line"

    def test_source_urls_present(self):
        verge_era = get_verge_era(get_welch_profile(load_journalists()))
        urls = verge_era.get('flagship_piece', {}).get('source_urls', [])
        assert len(urls) >= 3, \
            f"Must cite >=3 sources for the piece, got {len(urls)}"
        assert any('techmeme.com/250501' in u for u in urls), \
            "Must include the Techmeme byline/date citation"

    def test_correction_note_present(self):
        verge_era = get_verge_era(get_welch_profile(load_journalists()))
        assert 'correction' in verge_era.get('note', '').lower(), \
            "Verge-era note must acknowledge the Sep 3 2026 correction"


# ===================================================================
# Test Class 2: Within-Journalist Follow-Up Block in Profile
# ===================================================================
class TestWithinJournalistFollowup:
    """The type_b_488 follow-up block must document the within-person contrast."""

    def test_followup_block_exists(self):
        profile = get_welch_profile(load_journalists())
        followup = profile.get('competitor_coverage', {}).get('type_b_488_within_journalist_followup')
        assert followup, "type_b_488_within_journalist_followup must exist"

    def test_followup_date(self):
        profile = get_welch_profile(load_journalists())
        followup = profile['competitor_coverage']['type_b_488_within_journalist_followup']
        assert followup.get('date') == '2026-09-03', \
            f"Follow-up date must be 2026-09-03, got {followup.get('date')}"

    def test_followup_names_both_registers(self):
        """Finding must name the Verge adversarial register and Bloomberg neutral one."""
        profile = get_welch_profile(load_journalists())
        finding = profile['competitor_coverage']['type_b_488_within_journalist_followup'].get('finding', '').lower()
        assert 'heaps of data' in finding, "Must cite the Verge adversarial marker"
        assert 'samsung' in finding and 'bloomberg' in finding, \
            "Must name the Bloomberg Samsung comparison"

    def test_followup_notes_gemini_realtime(self):
        """Structural equivalence argument needs the Gemini real-time analysis fact."""
        profile = get_welch_profile(load_journalists())
        finding = profile['competitor_coverage']['type_b_488_within_journalist_followup'].get('finding', '').lower()
        assert 'gemini' in finding and 'real time' in finding, \
            "Must note Samsung's Gemini real-time camera-feed analysis"

    def test_confounder_update_weakens_reviewer_defense(self):
        profile = get_welch_profile(load_journalists())
        update = profile['competitor_coverage']['type_b_488_within_journalist_followup'].get('confounder_update', '').lower()
        assert 'product reviewer' in update or 'privacy investigator' in update, \
            "Must address the product-reviewer confounder"
        assert 'weaken' in update, "Must state the confounder is weakened"

    def test_genre_confounder_added(self):
        profile = get_welch_profile(load_journalists())
        followup = profile['competitor_coverage']['type_b_488_within_journalist_followup']
        confounders = followup.get('new_confounders', [])
        assert any('genre' in c.get('factor', '').lower() for c in confounders), \
            "Must add the genre-asymmetry confounder (rollback vs launch)"


# ===================================================================
# Test Class 3: Mechanism #85 Follow-Up in Competitor Research
# ===================================================================
class TestMechanism85Followup:
    """The #85 mechanism entry must carry the within-journalist follow-up."""

    def test_followup_key_exists(self):
        mechanism = get_welch_mechanism(load_competitor_research())
        assert mechanism.get('within_journalist_followup'), \
            "within_journalist_followup must exist on mechanism #85"

    def test_followup_iteration_number(self):
        followup = get_welch_mechanism(load_competitor_research())['within_journalist_followup']
        assert followup.get('type_b_iteration') == 488, \
            f"Must record Type B iteration 488, got {followup.get('type_b_iteration')}"

    def test_followup_references_this_test_file(self):
        followup = get_welch_mechanism(load_competitor_research())['within_journalist_followup']
        expected = 'tests/test_chris_welch_within_journalist_meta_vs_samsung_privacy_sep03.py'
        assert followup.get('test_file') == expected, \
            f"Must reference this test file, got {followup.get('test_file')}"

    def test_followup_documents_correction(self):
        followup = get_welch_mechanism(load_competitor_research())['within_journalist_followup']
        assert 'adversarial_pieces' in followup.get('corrects', ''), \
            "Must document the adversarial_pieces 0->1 profile correction"

    def test_followup_source_urls(self):
        followup = get_welch_mechanism(load_competitor_research())['within_journalist_followup']
        urls = followup.get('verge_piece_source_urls', [])
        assert len(urls) >= 3, f"Must cite >=3 sources, got {len(urls)}"
        assert any('techmeme.com/250501' in u for u in urls), \
            "Must include the Techmeme citation"

    def test_mechanism_id_still_85(self):
        """Follow-up must not create a new mechanism ID (no number collision)."""
        mechanism = get_welch_mechanism(load_competitor_research())
        assert mechanism.get('mechanism_id') == 85, \
            "Mechanism ID must remain 85; this is a follow-up, not a new mechanism"


# ===================================================================
# Test Class 4: Cross-Entity Symmetry of the Comparison
# ===================================================================
class TestComparisonSymmetry:
    """The comparison must hold structurally similar hardware on both sides."""

    def test_meta_side_is_camera_glasses(self):
        verge_era = get_verge_era(get_welch_profile(load_journalists()))
        subject = verge_era.get('flagship_piece', {}).get('subject', '').lower()
        assert 'ray-ban' in subject or 'glasses' in verge_era.get('flagship_piece', {}).get('title', '').lower(), \
            "Meta side must be the Ray-Ban Meta camera glasses"

    def test_samsung_side_is_camera_glasses(self):
        profile = get_welch_profile(load_journalists())
        finding = profile['competitor_coverage']['type_b_488_within_journalist_followup'].get('finding', '').lower()
        assert 'camera-equipped' in finding or 'camera' in finding, \
            "Samsung side must be camera-equipped glasses (structural match)"

    def test_same_journalist_both_sides(self):
        """Both sides must be Welch's own byline, not colleagues'."""
        profile = get_welch_profile(load_journalists())
        verge_byline = get_verge_era(profile).get('flagship_piece', {}).get('author_byline')
        assert verge_byline == 'Chris Welch' == profile.get('name'), \
            "Both sides of the contrast must be Welch's own byline"
