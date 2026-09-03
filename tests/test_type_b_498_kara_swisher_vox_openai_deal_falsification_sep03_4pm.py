"""
Test Mechanism #498 (Type B #498): Kara Swisher (Vox Media) vs the #494
Vox-OpenAI Deal Prediction - Deal-Partner Falsification

Type B: Journalist Cross-Entity Tracking - September 3, 2026, 16:00 PDT
Iteration #498 (rotation 497 A -> 498 B)

KEY FINDING: Kara Swisher applies a uniformly adversarial register to Meta,
OpenAI, and Apple. The naive prediction from mechanism #494 (Vox Media x
OpenAI strategic content and product partnership, May 29 2024) says Swisher -
whose "On with Kara Swisher" runs on the Vox Media Podcast Network - should
treat OpenAI more softly than Meta. The verified corpus falsifies it, and the
strongest evidence POST-DATES the deal:

- Jul 5 2024 (5 weeks post-deal): pressed OpenAI CTO Mira Murati on the
  Scarlett Johansson voice-theft controversy and profit-over-safety
  accusations, in a live on-stage interview.
- Sep 25 2025 (16 months post-deal): full episode platforming the parents
  suing OpenAI and Sam Altman PERSONALLY over the ChatGPT teen-suicide case
  ("Did ChatGPT Encourage a Teen Suicide? The Parents Suing OpenAI Say Yes").

META CORPUS (same adversarial register, no softening gradient toward the
deal partner):
- Zuckerberg "the most dangerous person in the tech world" (Burn Book,
  requoted Jan 2025)
- Facebook et al "digital arms dealers" (NYT column, 2018)
- "why the public is paying for Mark Zuckerberg's education" (NYT Opinion)

APPLE CALIBRATION: Apr 5 2021 Sway interview pressed Tim Cook on Epic
antitrust ("What's wrong with Epic... going their own way?"), sideloading,
and Parler - adversarial register toward a company with no Vox financial tie
in either direction.

This joins the falsification family (#457 Adrienne So, #471, #472, #492
Verge Samsung correction, #493 Fowler): star-franchise interviewers whose
brand IS adversarial access journalism do not modulate tone for the
employer's deal partners. Boundary condition on the financial-incentive
theory, not a universal rule.

Sources (all verified this run via search-result excerpts and mirror pages):
Meta:
- https://www.out.com/media/mark-zuckerberg-kara-swisher-criticism-reactions?xrs=RebelMouse_fb&ts=1737136481
- https://www.publicradioeast.org/us/2018-08-07/silicon-valley-cant-outrun-its-controversies-so-what-should-it-do
- https://www.nytco.com/press/kara-swisher-is-departing-times-opinion/
OpenAI:
- https://www.beckershospitalreview.com/disruptors/what-openais-fight-says-about-boards/
- https://www.thewrap.com/openai-employees-call-board-resign-sam-altman/
- https://www.podchaser.com/podcasts/on-with-kara-swisher-4865725/episodes/openai-ceo-sam-altman-on-gpt-4-167533271
- https://podfollow.com/pivot/episode/62ed6c2612259e2bb41c35c7ed77abf18932586d/view
- https://www.iheart.com/podcast/1319-on-with-kara-swisher-101646907/episode/did-chatgpt-encourage-a-teen-suicide-296670345/
- https://www.podchaser.com/podcasts/on-with-kara-swisher-4865725/episodes/how-did-kara-scoop-openai-and-more-on-burn-book-with-sam-altman/9b71b327-0e23-498e-a573-5e23d790bb43?_language=en
Apple:
- https://www.macstories.net/news/kara-swisher-interviews-apple-ceo-cook-for-sway/
- https://www.macrumors.com/2021/04/05/tim-cook-sideloading-apps-would-break-the-iphone/
- https://github.com/extratone/bilge/blob/HEAD/documentation/Tim%20Cook%20Interview%202021%20Transcript%20-%20Kara%20Swisher.md
Show-network attribution (Vox Media Podcast Network):
- https://canadian-podcasts.com/podcast/on-with-kara-swisher/sam-altman-openai-and-the-future-of-artificial-gen
Deal facts: mechanism #494 in profiles/competitor-entities.yaml (entities.openai),
verified Sep 3 2026 12:00 PDT from the voxmedia.com May 29 2024 announcement.
"""

import os
import re

import pytest
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
REPO_ROOT = os.path.join(os.path.dirname(__file__), '..')

VOX_OPENAI_DEAL_DATE = '2024-05-29'


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml'), encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml'), encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_swisher_profile():
    for j in load_journalists().get('journalists', []):
        if j.get('name') == 'Kara Swisher':
            return j
    return None


def get_mechanism_498():
    return load_research()['cross_publication_findings'][
        'vox_kara_swisher_openai_deal_partner_falsification']


def get_coverage():
    return get_swisher_profile().get('competitor_coverage', {})


# ===================================================================
# Class 1: Swisher profile exists with Vox Media tenure
# ===================================================================
class TestSwisherProfileExists:
    def test_profile_found(self):
        assert get_swisher_profile() is not None, "Kara Swisher entry must exist in journalists.yaml"

    def test_multi_publication(self):
        assert get_swisher_profile().get('multi_publication') is True

    def test_vox_media_tenure_from_2022(self):
        career = get_swisher_profile().get('career', [])
        vox = [c for c in career if c.get('publication') == 'vox-media']
        assert len(vox) == 1
        assert vox[0].get('start') == '2022-09'
        assert vox[0].get('end') in (None, 'present'), "vox-media is the current tenure"

    def test_five_outlet_arc(self):
        pubs = {c.get('publication') for c in get_swisher_profile().get('career', [])}
        for expected in ('washington-post', 'wsj', 'nytimes', 'vox-media'):
            assert expected in pubs, f"expected {expected} in career arc"

    def test_source_urls_https(self):
        urls = get_swisher_profile().get('source_urls', [])
        assert len(urls) >= 1
        assert all(u.startswith('https://') for u in urls)


# ===================================================================
# Class 2: Meta corpus - uniformly adversarial, no softening
# ===================================================================
class TestSwisherMetaCorpus:
    def test_dangerous_person_item(self):
        meta = get_coverage().get('meta_zuckerberg_most_dangerous', {})
        assert meta.get('adversarial_register') is True
        assert 'dangerous' in meta.get('adversarial_vocabulary', '').lower()

    def test_digital_arms_dealers_item(self):
        meta = get_coverage().get('meta_digital_arms_dealers', {})
        assert meta.get('adversarial_register') is True
        assert meta.get('date') == '2018-08-07'

    def test_zuckerberg_education_item(self):
        meta = get_coverage().get('meta_zuckerberg_education_column', {})
        assert meta.get('adversarial_register') is True
        assert 'education' in meta.get('adversarial_vocabulary', '').lower()

    def test_three_meta_items_all_adversarial(self):
        keys = ('meta_zuckerberg_most_dangerous', 'meta_digital_arms_dealers',
                'meta_zuckerberg_education_column')
        for k in keys:
            assert get_coverage().get(k, {}).get('adversarial_register') is True, k

    def test_meta_source_urls(self):
        urls = get_coverage().get('meta_zuckerberg_most_dangerous', {}).get('source_urls', [])
        assert any('out.com' in u for u in urls)


# ===================================================================
# Class 3: OpenAI POST-DEAL corpus - the falsification core
# ===================================================================
class TestSwisherOpenAIPostDealCorpus:
    def test_murati_interview_post_deal(self):
        murati = get_coverage().get('openai_murati_scarjo_interview', {})
        assert murati.get('date') == '2024-07-05'
        assert murati.get('date') > VOX_OPENAI_DEAL_DATE, "Murati interview must post-date the Vox-OpenAI deal"
        assert murati.get('post_deal') is True

    def test_murati_adversarial_vocabulary(self):
        murati = get_coverage().get('openai_murati_scarjo_interview', {})
        assert murati.get('adversarial_register') is True
        vocab = murati.get('adversarial_vocabulary', '').lower()
        assert 'scarlett johansson' in vocab or 'scarjo' in vocab
        assert 'profit over safety' in vocab

    def test_raine_episode_post_deal(self):
        raine = get_coverage().get('openai_raine_teen_suicide_episode', {})
        assert raine.get('date') == '2025-09-25'
        assert raine.get('date') > VOX_OPENAI_DEAL_DATE
        assert raine.get('post_deal') is True

    def test_raine_targets_altman_personally(self):
        raine = get_coverage().get('openai_raine_teen_suicide_episode', {})
        assert raine.get('adversarial_register') is True
        assert raine.get('targets_altman_personally') is True
        assert 'suing' in raine.get('result', '').lower()

    def test_raine_source_url(self):
        raine = get_coverage().get('openai_raine_teen_suicide_episode', {})
        assert any('iheart.com' in u for u in raine.get('source_urls', []))

    def test_two_post_deal_adversarial_items(self):
        post_deal = [k for k, v in get_coverage().items()
                     if isinstance(v, dict) and v.get('post_deal') is True
                     and v.get('adversarial_register') is True]
        assert len(post_deal) >= 2, f"expected >=2 post-deal adversarial OpenAI items, got {post_deal}"


# ===================================================================
# Class 4: OpenAI PRE-DEAL corpus - adversarial before any deal too
# ===================================================================
class TestSwisherOpenAIPreDealCorpus:
    def test_board_blip_criticism(self):
        blip = get_coverage().get('openai_board_blip_criticism', {})
        assert blip.get('date') == '2023-11-21'
        assert blip.get('date') < VOX_OPENAI_DEAL_DATE
        assert blip.get('adversarial_register') is True
        vocab = blip.get('adversarial_vocabulary', '').lower()
        assert 'stupid' in vocab or 'bad board' in vocab

    def test_broke_employee_letter_scoop(self):
        blip = get_coverage().get('openai_board_blip_criticism', {})
        assert '505' in blip.get('result', ''), "must record breaking the 505/700 employee letter"

    def test_gpt4_interview_pressed(self):
        gpt4 = get_coverage().get('openai_altman_gpt4_interview', {})
        assert gpt4.get('adversarial_register') is True
        vocab = gpt4.get('adversarial_vocabulary', '').lower()
        assert 'hallucination' in vocab
        assert '230' in vocab or 'section 230' in vocab


# ===================================================================
# Class 5: Apple calibration - adversarial with no financial tie either way
# ===================================================================
class TestSwisherAppleCalibration:
    def test_cook_sway_interview_date(self):
        cook = get_coverage().get('apple_cook_sway_antitrust_interview', {})
        assert cook.get('date') == '2021-04-05'

    def test_cook_antitrust_pressing(self):
        cook = get_coverage().get('apple_cook_sway_antitrust_interview', {})
        assert cook.get('adversarial_register') is True
        vocab = cook.get('adversarial_vocabulary', '').lower()
        assert 'epic' in vocab
        assert 'sideload' in vocab

    def test_cook_transcript_source(self):
        cook = get_coverage().get('apple_cook_sway_antitrust_interview', {})
        assert any('github.com' in u for u in cook.get('source_urls', []))


# ===================================================================
# Class 6: Mechanism #498 statistical discipline and registry integrity
# ===================================================================
class TestMechanism498Discipline:
    def test_mechanism_id(self):
        assert get_mechanism_498().get('mechanism_id') == 498

    def test_finding_type(self):
        assert get_mechanism_498().get('finding_type') == 'deal_partner_falsification'

    def test_deal_reference(self):
        entry = get_mechanism_498()
        assert entry.get('deal_mechanism_id') == 494
        assert entry.get('deal_date') == VOX_OPENAI_DEAL_DATE

    def test_falsification_family(self):
        fam = get_mechanism_498().get('falsification_family', [])
        for member in (457, 492, 493):
            assert member in fam, f"falsification family must include #{member}"

    def test_statistical_discipline(self):
        disc = get_mechanism_498().get('statistical_discipline', {})
        assert disc.get('is_significant') is False
        assert disc.get('correlation_not_causation') is True
        assert disc.get('p_value') == 'NOT_CALCULATED'

    def test_no_em_dash_in_new_yaml(self):
        emdash = chr(0x2014)
        raw = open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml'), encoding='utf-8').read()
        start = raw.index('name: Kara Swisher')
        end = raw.index('- awards:', start)
        assert emdash not in raw[start:end]
        raw2 = open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml'), encoding='utf-8').read()
        start2 = raw2.index('vox_kara_swisher_openai_deal_partner_falsification')
        end2 = raw2.index("\nmethodology:", start2)
        assert emdash not in raw2[start2:end2]

    def test_profile_finding_block_references_498(self):
        finding = get_coverage().get('type_b_498_within_journalist_finding', {})
        assert finding.get('mechanism_id') == 498
        assert finding.get('iteration') == 498


# ===================================================================
# Class 7: Iteration log records #498 newest-first
# ===================================================================
def _heading_pos(marker):
    # Line-anchored search (per the #495 fix): plain str.index() can match
    # quoted mentions of a heading literal inside newer entries' prose.
    log = open(os.path.join(REPO_ROOT, 'iteration-log.md'), encoding='utf-8').read()
    m = re.search(r'^' + re.escape(marker), log, re.MULTILINE)
    assert m, "heading not found: %s" % marker
    return m.start(), log


class TestIterationLog498:
    def test_log_orders_498_newest_first(self):
        i498, _ = _heading_pos('#498 Type B:')
        i497, _ = _heading_pos('#497 Type A:')
        i496, _ = _heading_pos('#496 Type E:')
        assert i498 < i497 < i496, "iteration log must keep #498 > #497 > #496 newest-first order"

    def test_log_names_swisher(self):
        i498, log = _heading_pos('#498 Type B:')
        i497, _ = _heading_pos('#497 Type A:')
        seg = log[i498:i497]
        assert 'Kara Swisher' in seg
        assert 'Type B' in seg
