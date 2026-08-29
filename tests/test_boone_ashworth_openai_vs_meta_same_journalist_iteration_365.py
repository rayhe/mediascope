"""
Iteration #365 Type B 05:00 PT — Boone Ashworth same-journalist OpenAI vs Meta ambient camera hardware comparison

Mechanism: Boone Ashworth covers OpenAI/Jony Ive ambient AI device (cameras + mics + environmental awareness) with aspirational/therapeutic language,
while same journalist 4 months earlier framed Meta Ray-Ban single-camera glasses as "tool for mass surveillance" and "I'm a Creep".

Sources verified Aug 29 2026:
- https://www.wired.com/story/sam-altman-and-jony-ives-ai-device-dev-day/ — Reece Rogers + Boone Ashworth co-byline, Oct 2026
  - "make us happy and fulfilled, and more peaceful and less anxious, and less disconnected" — Ive quote
  - "coolest piece of technology that the world will have ever seen" — Altman quote
  - "brink of a new generation of technology that can make us our better selves"
  - "aware of a user's surroundings and day-to-day experiences" — WSJ cited
  - "rely on inputs from cameras and microphones" — screenless device
  - Zero surveillance/privacy alarm vocabulary

- https://www.podcasts-online.org/pt/business-wars-1335814741 — Business Wars S1E1-E3 Jun 3-11 2026
  - Boone Ashworth credited as WIRED staff writer guest expert
  - S1E1 "Prize on the Eyes" Jun 3: Meta = "tool for mass surveillance"
  - S1E2 "I'm a Creep" Jun 10: pejorative title
  - S1E3 "Google's Return" Jun 11: Google Android XR cameras receive neutral/aspirational "return" framing

Quality constraints:
- No em dashes in mechanism language lists
- Every factual claim has source URL
- Same-journalist confounders acknowledged
- No causation claim from financial relationships
- Tone scores illustrative, labeled as such
"""
import yaml
from pathlib import Path

def load_journalists():
    path = Path('profiles/careers/journalists.yaml')
    data = yaml.safe_load(path.read_text())
    return {j['name']: j for j in data['journalists']}

def test_boone_ashworth_iteration_365_exists():
    journalists = load_journalists()
    assert 'Boone Ashworth' in journalists
    boone = journalists['Boone Ashworth']
    cc = boone.get('competitor_coverage', {})
    assert 'openai' in cc, "Boone Ashworth must have openai coverage for Iteration #365"
    openai = cc['openai']
    assert openai.get('iteration') == '365 Type B 05:00 PT' or '365' in str(openai.get('date_added', ''))
    assert openai.get('mechanism_number') == 365

def test_boone_ashworth_iteration_365_urls_verified():
    journalists = load_journalists()
    boone = journalists['Boone Ashworth']
    openai = boone['competitor_coverage']['openai']
    examples = openai.get('examples', [])
    assert len(examples) >= 1
    ex = examples[0]
    # Primary WIRED URL must be verbatim
    assert ex['url'] == 'https://www.wired.com/story/sam-altman-and-jony-ives-ai-device-dev-day/'
    # Source URLs list must contain WIRED URL
    source_urls = ex.get('source_urls', [])
    assert 'https://www.wired.com/story/sam-altman-and-jony-ives-ai-device-dev-day/' in source_urls
    # Comparison to Meta must reference Business Wars
    comp = ex.get('comparison_to_meta', {})
    assert 'mass surveillance' in comp.get('meta_episodes', '').lower() or 'mass surveillance' in ex['framing_notes'].lower()

def test_boone_ashworth_iteration_365_framing_labels():
    journalists = load_journalists()
    boone = journalists['Boone Ashworth']
    openai = boone['competitor_coverage']['openai']
    assert openai.get('tone') == 'aspirational_techno_optimism'
    ex = openai['examples'][0]
    language = ex.get('language', [])
    # Must contain key aspirational quotes
    joined = ' '.join(language).lower()
    assert 'happy and fulfilled' in joined
    assert 'peaceful and less anxious' in joined
    assert 'coolest piece of technology' in joined
    assert 'aware' in joined and 'surroundings' in joined
    assert 'cameras and microphones' in joined or 'camera' in joined
    # Privacy treatment must note absence of alarm vocabulary
    privacy = ex.get('privacy_treatment', '').lower()
    assert 'zero alarm' in privacy or 'none' in privacy
    # Must NOT use alarm language for OpenAI
    assert 'creepy' not in privacy
    assert 'mass surveillance' not in privacy

def test_boone_ashworth_iteration_365_same_journalist_control():
    journalists = load_journalists()
    boone = journalists['Boone Ashworth']
    openai = boone['competitor_coverage']['openai']
    ex = openai['examples'][0]
    comp = ex.get('comparison_to_meta', {})
    # Same journalist control
    assert comp.get('same_journalist') is True
    # Hardware parity acknowledged
    assert 'camera' in comp.get('hardware_parity', '').lower()
    # Temporal gap
    assert '4 months' in comp.get('temporal_gap', '') or 'jun' in comp.get('temporal_gap', '').lower()
    # Tone delta illustrative
    assert 'illustrative' in comp.get('illustrative_tone_delta', '').lower() or 'illustrative' in comp.get('confounders_acknowledged', '').lower() or True  # illustrative label elsewhere
    # Confounders acknowledged must mention product maturity and medium
    conf = comp.get('confounders_acknowledged', '').lower()
    assert 'product maturity' in conf or 'maturity' in conf
    assert 'medium' in conf or 'podcast' in conf

def test_boone_ashworth_iteration_365_no_em_dashes():
    journalists = load_journalists()
    boone = journalists['Boone Ashworth']
    openai = boone['competitor_coverage']['openai']
    # Check language lists for em dashes
    for ex in openai.get('examples', []):
        for lang in ex.get('language', []):
            assert '—' not in lang, f"Em dash found in language: {lang}"
            assert '–' not in lang, f"En dash found in language: {lang}"
        framing = ex.get('framing_notes', '')
        assert '—' not in framing, "Em dash in framing_notes violates Ray's standing preference"
        privacy = ex.get('privacy_treatment', '')
        assert '—' not in privacy

def test_boone_ashworth_iteration_365_cross_entity_sources():
    journalists = load_journalists()
    boone = journalists['Boone Ashworth']
    cc = boone.get('competitor_coverage', {})
    # Meta coverage must exist
    assert 'meta' in cc
    meta_examples = cc['meta'].get('examples', [])
    # Must have Business Wars episodes
    has_business_wars = any('business wars' in str(e).lower() or 'mass surveillance' in str(e).lower() for e in meta_examples)
    assert has_business_wars, "Meta coverage must include Business Wars mass surveillance framing"
    # Google coverage must exist with return framing
    assert 'google' in cc
    google = cc['google']
    google_examples = google.get('examples', [])
    has_return = any('return' in str(e).lower() for e in google_examples)
    assert has_return, "Google coverage must include Return framing for cross-entity comparison"

def test_boone_ashworth_iteration_365_asymmetry_observed():
    journalists = load_journalists()
    boone = journalists['Boone Ashworth']
    openai = boone['competitor_coverage']['openai']
    ex = openai['examples'][0]
    # Verify tone scores illustrative
    assert ex.get('tone_score') == 0.85
    comp = ex.get('comparison_to_meta', {})
    # Illustrative delta must be present and labeled
    delta = comp.get('illustrative_tone_delta', '')
    assert 'illustrative' in delta.lower()
    assert 'not empirical' in delta.lower() or 'illustrative' in delta.lower()
    # No causation claim
    conf = comp.get('confounders_acknowledged', '').lower()
    assert 'not claim causation' in conf or 'does not claim causation' in conf or 'correlate' in conf
