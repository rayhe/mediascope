"""
Test Mechanism #493 (Type B #493): Geoffrey Fowler (WaPo) Company-Agnostic
Adversarial Privacy Testing - Ownership-Level Falsification

Type B: Journalist Cross-Entity Tracking - September 3, 2026, 11:00 PDT
Iteration #493 (rotation 492 A -> 493 B)

KEY FINDING: Fowler's first-person privacy-testing column ("The Secret Life
of My Data") applies an identical adversarial register to Meta, Apple,
Amazon, and Google. No puff-piece bifurcation found in the verified corpus.

OWNERSHIP-LEVEL INVERSION: The strongest possible financial tie (the
publication's owner company, Amazon, via Bezos/Nash Holdings) received two
of Fowler's hardest-hitting adversarial tests:
- Alexa (2019): Amazon kept four years of recorded home audio, including
  family conversations about medications.
- Amazon Key (Dec 2017): removed the smart lock plus camera after two
  weeks; "The biggest downsides ... it has been Amazon"; on-the-record
  "I review all tech the same" addressing Bezos ownership directly.

This inverts the naive financial-incentive prediction and joins the
falsification family (#457 Adrienne So, #471, #472, #492).

META CORPUS: two-week Facebook/Instagram cut-off experiment (2019):
Facebook tracked him across at least 95 apps, websites, and businesses;
"hired a private eye to prepare a dossier about my life."

META-GLASSES BOUNDED ABSENCE: four targeted searches this run surfaced no
Fowler byline conducting a Meta smart-glasses adversarial privacy test. The
Sep 2021 Ray-Ban Stories launch piece ("Smart Glasses Made Google Look
Dumb...") is NYT/Mike Isaac, verified via byline attribution. Per the #492
rule this absence is search-bounded, not a zero claim.

Sources (all verified this run via secondary/mirror pages; WaPo primary
is paywalled):
- https://www.macrumors.com/2021/05/05/airtags-anti-stalking-measures-not-sufficient/
- https://www.tomsguide.com/news/airtag-anti-stalking-measures-tested-and-theyre-not-good-enough
- https://9to5mac.com/2021/05/06/airtag-stalking
- https://www.publicradioeast.org/us/2019-07-31/how-tech-companies-track-your-every-move-and-put-your-data-up-for-sale
- https://www.marketplace.org/episode/2019/06/28/when-a-tech-columnist-digs-into-the-secret-life-of-his-data
- https://yro.slashdot.org/story/17/12/09/0414237/reporter-regrets-letting-amazons-delivery-people-into-his-house
- https://edition.pagesuite.com/popovers/dynamic_article_popover.aspx?artguid=bc9f63cc-eb9d-4028-9880-61de14178b88
"""

import os
import re

import pytest
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
REPO_ROOT = os.path.join(os.path.dirname(__file__), '..')


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml'), encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml'), encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_fowler_profile():
    for j in load_journalists().get('journalists', []):
        if j.get('name') == 'Geoffrey Fowler':
            return j
    return None


def get_mechanism_493():
    return load_research()['cross_publication_findings'][
        'wapo_geoffrey_fowler_company_agnostic_privacy_testing']


def get_coverage():
    return get_fowler_profile().get('competitor_coverage', {})


# ===================================================================
# Class 1: Fowler profile exists with correct career structure
# ===================================================================
class TestFowlerProfileExists:
    def test_profile_found(self):
        assert get_fowler_profile() is not None, "Geoffrey Fowler entry must exist in journalists.yaml"

    def test_multi_publication(self):
        assert get_fowler_profile().get('multi_publication') is True

    def test_wsj_tenure_ends_2017(self):
        career = get_fowler_profile().get('career', [])
        wsj = [c for c in career if c.get('publication') == 'wall-street-journal']
        assert len(wsj) == 1
        assert wsj[0].get('end') == '2017'

    def test_wapo_tenure_from_2017(self):
        career = get_fowler_profile().get('career', [])
        wapo = [c for c in career if c.get('publication') == 'washington-post']
        assert len(wapo) == 1
        assert wapo[0].get('start') == '2017'
        assert wapo[0].get('end') == 'present'
        assert 'columnist' in wapo[0].get('role', '')

    def test_source_urls_https(self):
        urls = get_fowler_profile().get('source_urls', [])
        assert len(urls) >= 5, f"expected at least 5 source URLs, got {len(urls)}"
        assert all(u.startswith('https://') for u in urls)


# ===================================================================
# Class 2: Meta corpus - Facebook tracking experiment, adversarial
# ===================================================================
class TestFowlerMetaCoverage:
    def test_experiment_present(self):
        meta = get_coverage().get('meta_facebook_tracking_experiment', {})
        assert meta.get('author_byline') == 'Geoffrey Fowler'
        assert meta.get('publication') == 'washington-post'

    def test_95_tracker_result(self):
        meta = get_coverage().get('meta_facebook_tracking_experiment', {})
        assert '95' in meta.get('result', ''), "must record the 95 apps/websites/businesses result"

    def test_adversarial_register(self):
        meta = get_coverage().get('meta_facebook_tracking_experiment', {})
        assert meta.get('adversarial_register') is True
        vocab = ' '.join(meta.get('adversarial_vocabulary', [])).lower()
        assert 'private eye' in vocab and 'dossier' in vocab

    def test_meta_source_url(self):
        meta = get_coverage().get('meta_facebook_tracking_experiment', {})
        urls = meta.get('source_urls', [])
        assert any('pagesuite.com' in u for u in urls)


# ===================================================================
# Class 3: Apple corpus - AirTag and iPhone tests, adversarial
# ===================================================================
class TestFowlerAppleCoverage:
    def test_airtag_date(self):
        airtag = get_coverage().get('apple_airtag_stalking_test', {})
        assert airtag.get('date') == '2021-05-05'

    def test_airtag_adversarial_vocabulary(self):
        airtag = get_coverage().get('apple_airtag_stalking_test', {})
        assert airtag.get('adversarial_register') is True
        vocab = ' '.join(airtag.get('adversarial_vocabulary', [])).lower()
        assert 'stalking' in vocab
        assert 'sufficient' in vocab

    def test_airtag_three_sources(self):
        airtag = get_coverage().get('apple_airtag_stalking_test', {})
        assert len(airtag.get('source_urls', [])) >= 3

    def test_iphone_overnight_trackers(self):
        iphone = get_coverage().get('apple_iphone_overnight_tracker_test', {})
        assert iphone.get('adversarial_register') is True
        assert 'housands' in iphone.get('result', ''), "must record thousands of overnight trackers"


# ===================================================================
# Class 4: Amazon corpus - ownership-level inversion
# ===================================================================
class TestFowlerAmazonOwnershipInversion:
    def test_alexa_four_year_retention(self):
        alexa = get_coverage().get('amazon_alexa_audio_retention', {})
        assert alexa.get('adversarial_register') is True
        assert 'four years' in alexa.get('result', '')
        assert 'medication' in alexa.get('result', '')

    def test_alexa_ownership_dimension(self):
        alexa = get_coverage().get('amazon_alexa_audio_retention', {})
        assert 'nash' in alexa.get('ownership_dimension', '').lower() or \
               'bezos' in alexa.get('ownership_dimension', '').lower()

    def test_amazon_key_removal(self):
        key = get_coverage().get('amazon_key_smart_lock_test', {})
        assert key.get('date') == '2017-12'
        assert key.get('adversarial_register') is True
        assert 'two weeks' in key.get('result', '')

    def test_review_all_tech_same_quote(self):
        key = get_coverage().get('amazon_key_smart_lock_test', {})
        vocab = ' '.join(key.get('adversarial_vocabulary', []))
        assert 'I review all tech the same' in vocab
        assert 'bezos' in key.get('ownership_note', '').lower()

    def test_research_entry_owner_company(self):
        entry = get_mechanism_493()
        assert 'bezos' in entry.get('publication_owner', '').lower()


# ===================================================================
# Class 5: Google corpus - Chrome tracker test, adversarial
# ===================================================================
class TestFowlerGoogleCoverage:
    def test_chrome_tracker_count(self):
        chrome = get_coverage().get('google_chrome_tracker_test', {})
        assert chrome.get('adversarial_register') is True
        assert '11,000' in chrome.get('result', '')

    def test_chrome_source(self):
        chrome = get_coverage().get('google_chrome_tracker_test', {})
        assert any('marketplace.org' in u for u in chrome.get('source_urls', []))


# ===================================================================
# Class 6: Mechanism #493 statistical discipline and registry integrity
# ===================================================================
class TestMechanism493Discipline:
    def test_mechanism_id(self):
        assert get_mechanism_493().get('mechanism_id') == 493

    def test_finding_type(self):
        assert get_mechanism_493().get('finding_type') == 'company_agnostic_adversarial_privacy_testing'

    def test_falsification_family(self):
        fam = get_mechanism_493().get('falsification_family', [])
        for member in (457, 472, 492):
            assert member in fam, f"falsification family must include #{member}"

    def test_statistical_discipline(self):
        disc = get_mechanism_493().get('statistical_discipline', {})
        assert disc.get('is_significant') is False
        assert disc.get('correlation_not_causation') is True
        assert disc.get('p_value') == 'NOT_CALCULATED'

    def test_bounded_absence_not_zero_claim(self):
        absence = get_mechanism_493().get('meta_glasses_bounded_absence', '')
        assert 'search-bounded' in absence, "absence must be labeled search-bounded per #492 rule"
        assert 'mike isaac' in absence.lower(), "must record the Isaac byline correction"

    def test_no_em_dash_in_new_yaml(self):
        emdash = chr(0x2014)
        raw = open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml'), encoding='utf-8').read()
        start = raw.index('- name: Geoffrey Fowler')
        end = raw.index('jacob_krol:')
        assert emdash not in raw[start:end]
        raw2 = open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml'), encoding='utf-8').read()
        start2 = raw2.index('wapo_geoffrey_fowler_company_agnostic_privacy_testing')
        end2 = raw2.index("methodology: 'For each profiled publication")
        assert emdash not in raw2[start2:end2]

    def test_profile_finding_block_references_493(self):
        finding = get_coverage().get('type_b_493_within_journalist_finding', {})
        assert finding.get('mechanism_id') == 493
        assert finding.get('iteration') == 493


# ===================================================================
# Class 7: Iteration log records #493 newest-first
# ===================================================================
class TestIterationLog493:
    def test_log_starts_with_493(self):
        log = open(os.path.join(REPO_ROOT, 'iteration-log.md'), encoding='utf-8').read()
        assert log.startswith('#493 Type B:'), "iteration log must start with the #493 entry (newest-first)"

    def test_log_names_fowler(self):
        log = open(os.path.join(REPO_ROOT, 'iteration-log.md'), encoding='utf-8').read(4000)
        assert 'Geoffrey Fowler' in log
        assert 'Type B' in log
