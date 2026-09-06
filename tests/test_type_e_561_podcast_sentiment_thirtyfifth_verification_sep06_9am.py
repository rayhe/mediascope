"""
Type E #561 - Podcast Sentiment Tracking: Thirty-Fifth Verification Cycle Sep 6 09:00 PDT
Guilty Feminist 498 Hold No 499 as of 09:00 (search-result secondary, 10h crawl, 35th cycle,
cadence note 499 near Sep 7, Chortle LPF Sep 13) +
EHE 28-Day Hold with Times/Engadget/feminist.org/Hyperallergic-x2
re-surfaces verified already-in-corpus via pre-commit grep, circular GitHub rejected, NOT new campaigns +
Attention Sphere 35th No-Match (circular GitHub pages rejected, Spotify Creators 3h-fresh
reconfirms nonprofit) +
ONE new press surface this cycle (Startup Fortune Kenyan-contractors amended-complaint
re-report ~Sep 5, newest in-corpus surface superseding #531 Jezebel; older returns in-corpus)
"""
import re
from pathlib import Path

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 561
DATE_STR = "2026-09-06 09:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_561_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #561", text, re.MULTILINE)
    assert m, "Iteration #561 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_561_block()
        assert "561" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_561_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_561_block()
        lower = block.lower()
        assert "555 d -> 556 e" not in lower  # previous cycle's rotation, not this one
        assert "560 d -> 561 e" in lower

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_thirtyfifth_cycle_label(self):
        block = get_561_block()
        lower = block.lower()
        assert "thirty-fifth" in lower

    def test_distinct_from_556(self):
        block = get_561_block()
        lower = block.lower()
        assert "thirty-fifth" in lower
        assert "556" in block  # references prior cycle by number, not as self


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_561_block()
        assert "498" in block
        lower = block.lower()
        assert "latest episode" in lower or "498 hold" in lower

    def test_no_499_bounded(self):
        block = get_561_block()
        assert "499" in block
        lower = block.lower()
        assert "bounded" in lower

    def test_secondary_only_disclosed(self):
        block = get_561_block()
        lower = block.lower()
        assert "secondary-only" in lower

    def test_listennotes_secondary_10h_crawl(self):
        block = get_561_block()
        assert "ListenNotes" in block or "listennotes" in block.lower()
        assert "10 hours" in block

    def test_cadence_note_sep7(self):
        block = get_561_block()
        assert "Sep 7" in block
        lower = block.lower()
        assert "cadence" in lower

    def test_chortle_lpf_sep13(self):
        block = get_561_block()
        assert "Chortle" in block
        assert "Sep 13" in block

    def test_zero_meta_wearables_thirtyfive_cycles(self):
        block = get_561_block()
        lower = block.lower()
        assert "thirty-five verification cycles" in lower or "thirty-five cycles" in lower

    def test_extension_not_duplicate(self):
        block = get_561_block()
        lower = block.lower()
        assert "extension not duplicate" in lower or "5-hour extension" in lower


class TestEHEHold:
    def test_28_day_hold(self):
        block = get_561_block()
        lower = block.lower()
        assert "28-day" in lower or "28 days" in lower

    def test_activist_not_podcast(self):
        block = get_561_block()
        lower = block.lower()
        assert "activist group, not a podcast" in lower

    def test_query_window_since_aug10(self):
        block = get_561_block()
        assert "2026-08-10" in block

    def test_times_epstein_resurface(self):
        block = get_561_block()
        assert "thetimes.com" in block
        lower = block.lower()
        assert "in corpus" in lower

    def test_engadget_resurface(self):
        block = get_561_block()
        assert "ENGADGET" in block or "engadget" in block.lower()

    def test_feminist_org_resurface(self):
        block = get_561_block()
        assert "feminist.org" in block
        assert "29 hits" in block

    def test_hyperallergic_two_resurfaces(self):
        block = get_561_block()
        lower = block.lower()
        assert "hyperallergic" in lower
        assert "5 files" in lower

    def test_circular_github_rejected(self):
        block = get_561_block()
        lower = block.lower()
        assert "circular" in lower
        assert "rejected" in lower

    def test_no_new_primary_motif(self):
        block = get_561_block()
        lower = block.lower()
        assert "no new primary campaign motif" in lower

    def test_no_competitor_equivalent(self):
        block = get_561_block()
        lower = block.lower()
        assert "no competitor-equivalent" in lower
        assert "thirty-five verification cycles" in lower or "thirty-five cycles" in lower

    def test_no_double_counting(self):
        block = get_561_block()
        lower = block.lower()
        assert "re-surfaces" in lower or "re-surfaced" in lower


class TestAttentionSphereNoMatch:
    def test_35th_no_match(self):
        block = get_561_block()
        lower = block.lower()
        assert "thirty-fifth no-match" in lower

    def test_circular_github_rejected(self):
        block = get_561_block()
        lower = block.lower()
        assert "circular" in lower

    def test_spotify_creators_nonprofit_reconfirmation(self):
        block = get_561_block()
        assert "creators.spotify.com" in block
        lower = block.lower()
        assert "non-profit organization" in lower

    def test_attentionstudio_named(self):
        block = get_561_block()
        assert "theattentionstudio.com" in block

    def test_misidentified_status_unchanged(self):
        block = get_561_block()
        lower = block.lower()
        assert "misidentified" in lower

    def test_bounded_absence_claim(self):
        block = get_561_block()
        lower = block.lower()
        assert "bounded" in lower


class TestNewPressSurface:
    def test_startupfortune_new_surface(self):
        block = get_561_block()
        assert "startupfortune.com/meta-glasses-lawsuit-says-intimate-footage-trained-ai-via-kenyan-contractors" in block

    def test_new_surface_section_heading(self):
        block = get_561_block()
        assert "ONE New" in block

    def test_amended_complaint_aug31(self):
        block = get_561_block()
        lower = block.lower()
        assert "amended complaint" in lower
        assert "august 31" in lower

    def test_bystander_class_expansion(self):
        block = get_561_block()
        lower = block.lower()
        assert "bystanders" in lower or "bystander" in lower

    def test_kenyan_contractors(self):
        block = get_561_block()
        lower = block.lower()
        assert "kenyan contractors" in lower

    def test_clarkson_quote(self):
        block = get_561_block()
        assert "feeding the beast" in block

    def test_novelty_zero_hits_disclosed(self):
        block = get_561_block()
        lower = block.lower()
        assert "zero hits" in lower

    def test_extension_not_new_claim_class(self):
        block = get_561_block()
        lower = block.lower()
        assert "not a new claim class" in lower

    def test_supersedes_531_jezebel(self):
        block = get_561_block()
        assert "#531 Jezebel" in block
        lower = block.lower()
        assert "newest" in lower

    def test_older_returns_listed(self):
        block = get_561_block()
        lower = block.lower()
        assert "reuters.com" in lower
        assert "techcrunch.com" in lower

    def test_trade_blog_venue_qualified(self):
        block = get_561_block()
        lower = block.lower()
        assert "niche trade-blog" in lower or "trade-blog" in lower


class TestScoresAndDiscipline:
    def test_not_calculated_scores(self):
        block = get_561_block()
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_ehe_illustrative_minus8(self):
        block = get_561_block()
        assert "-8/10" in block
        assert "MANUAL ILLUSTRATIVE" in block

    def test_no_empirical_significance_claim(self):
        block = get_561_block()
        lower = block.lower()
        assert "do not claim empirical significance" in lower or "no claim of empirical significance" in lower

    def test_correlation_not_causation(self):
        block = get_561_block()
        lower = block.lower()
        assert "correlation not causation" in lower

    def test_no_em_dashes(self):
        block = get_561_block()
        assert "—" not in block


class TestSources:
    def test_listennotes_url(self):
        block = get_561_block()
        assert "https://www.listennotes.com/podcasts/the-guilty-feminist-deborah-frances-white--rJKyRn2TWG/" in block

    def test_chortle_url(self):
        block = get_561_block()
        assert "https://www.chortle.co.uk/shows/edinburgh_fringe_2026/g/39124/the_guilty_feminist" in block

    def test_new_startupfortune_url(self):
        block = get_561_block()
        assert "https://startupfortune.com/meta-glasses-lawsuit-says-intimate-footage-trained-ai-via-kenyan-contractors/" in block

    def test_ehe_urls_present(self):
        block = get_561_block()
        assert "thetimes.com/uk/london/article/meta-ai-glasses-spoof-advert-jeffrey-epstein" in block
        assert "WWW.ENGADGET.COM/2217151/activist-group-takes-over-london-bus-stops-with-fake-meta-glasses-ads/" in block

    def test_feminist_org_url(self):
        block = get_561_block()
        assert "https://feminist.org/news/helpful-or-hurtful-the-growing-privacy-debate-over-meta-glasses/" in block

    def test_hyperallergic_http_listing_verbatim(self):
        block = get_561_block()
        assert "http://hyperallergic.com/guerrilla-london-bus-ads-mock-kylie-jenners-meta-glasses-campaign/" in block

    def test_spotify_creators_url(self):
        block = get_561_block()
        assert "https://creators.spotify.com/pod/profile/anita-nowak/" in block

    def test_older_press_urls_present(self):
        block = get_561_block()
        assert "reuters.com/sustainability/boards-policy-regulation/ray-ban-meta-glasses-take-off" in block
        assert "techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses" in block


class TestConfounders:
    def test_strong_confounders_present(self):
        block = get_561_block()
        lower = block.lower()
        assert "strong" in lower
        assert "snippet-bounded" in lower

    def test_secondary_only_weakness(self):
        block = get_561_block()
        lower = block.lower()
        assert "secondary-only" in lower

    def test_cadence_confounder(self):
        block = get_561_block()
        lower = block.lower()
        assert "five-hour cadence" in lower or "5-hour cadence" in lower

    def test_new_surface_confounder(self):
        block = get_561_block()
        lower = block.lower()
        assert "tier-1 outlet" in lower or "tier-1" in lower

    def test_iteration_log_entry_present(self):
        text = LOG_PATH.read_text(encoding="utf-8")
        assert "561" in text[:5000], "iteration-log.md entry for #561 must be near the top (newest-first)"
