"""
Type E #521 - Podcast Sentiment Tracking: Twenty-Seventh Verification Cycle Sep 4 16:00 PDT
Guilty Feminist 498 Hold No 499 as of 16:00 (zeno.fm opened this run, 27th cycle) +
EHE 25-Day Hold, Hyperallergic Arts-Press Corpus First-Hand Verified
(previously-known outlet per repo grep - NOT a new vertical, seven-vertical count stands;
self-correction recorded; both pieces opened first-hand this run with verbatim quotes) +
Attention Sphere 27th No-Match (nonprofit identification stays secondary-only)
"""
import re
from pathlib import Path

DOC_PATH = Path(__file__).parent.parent / "podcast-sentiment.md"
LOG_PATH = Path(__file__).parent.parent / "iteration-log.md"
GOAL_ID = "goal_54093bda4145"
JOB_ID = "mediascope-daily-iteration"
ITERATION = 521
DATE_STR = "2026-09-04 16:00 PDT"


def read_doc():
    return DOC_PATH.read_text(encoding="utf-8")


def get_521_block():
    text = read_doc()
    # Durable rule (fixed #495): anchor iteration headings to line start,
    # never match with unanchored substring search.
    m = re.search(r"^## Iteration #521", text, re.MULTILINE)
    assert m, "Iteration #521 block not found in podcast-sentiment.md"
    rest = text[m.end():]
    nxt = re.search(r"^## Iteration #", rest, re.MULTILINE)
    block = text[m.start():(m.end() + nxt.start() if nxt else len(text))]
    return block


class TestIterationNumberAndRotation:
    def test_iteration_number_present(self):
        block = get_521_block()
        assert "521" in block
        assert "Type E" in block

    def test_date_present(self):
        block = get_521_block()
        assert DATE_STR in block

    def test_rotation_d_to_e(self):
        block = get_521_block()
        assert "520" in block
        assert "D" in block and "E" in block

    def test_goal_and_job_ids(self):
        text = read_doc()
        assert GOAL_ID in text
        assert JOB_ID in text

    def test_twenty_seventh_cycle_label(self):
        block = get_521_block()
        lower = block.lower()
        assert "twenty-seventh" in lower

    def test_extends_516(self):
        block = get_521_block()
        assert "#516" in block
        lower = block.lower()
        assert "6 hours" in block or "6-hour" in lower

    def test_distinct_from_516(self):
        block = get_521_block()
        assert "516" in block
        lower = block.lower()
        assert "distinct from" in lower or "extends #516" in lower


class TestGuiltyFeministHold:
    def test_498_latest(self):
        block = get_521_block()
        assert "498" in block
        assert "Politics" in block
        assert "31 Aug 2026" in block

    def test_no_499_bounded(self):
        block = get_521_block()
        assert "No 499" in block
        lower = block.lower()
        assert "bounded absence" in lower

    def test_official_source_opened_this_run(self):
        block = get_521_block()
        assert "https://zeno.fm/podcast/the-guilty-feminist/" in block
        assert "opened this run" in block

    def test_cadence_note(self):
        block = get_521_block()
        assert "Sep 7" in block
        assert "weekly" in block.lower()

    def test_extension_not_duplicate(self):
        block = get_521_block()
        lower = block.lower()
        assert "extension not duplicate" in lower
        assert "fresh primary open" in lower


class TestEveryoneHatesElon:
    def test_25_day_hold(self):
        block = get_521_block()
        assert "25 days" in block
        assert "Aug 10" in block

    def test_activist_not_podcast_discipline(self):
        block = get_521_block()
        lower = block.lower()
        assert "activist group, not a podcast" in lower

    def test_hyperallergic_not_a_new_vertical_self_correction(self):
        block = get_521_block()
        assert "Hyperallergic" in block
        lower = block.lower()
        assert "self-correction" in lower
        assert "not a new vertical" in lower

    def test_seven_vertical_count_stands(self):
        block = get_521_block()
        lower = block.lower()
        assert "seven-vertical count stands" in lower

    def test_hyperallergic_opened_first_hand_this_run(self):
        block = get_521_block()
        assert "https://hyperallergic.com/jeffrey-epstein-dons-meta-ai-glasses-in-damning-guerrilla-ad/" in block
        assert "opened first-hand this run" in block

    def test_hyperallergic_byline_and_date(self):
        block = get_521_block()
        assert "Rhea Nayyar" in block
        assert "2026-08-10" in block

    def test_epstein_intake_photo_quote(self):
        block = get_521_block()
        assert "sex offender registry intake photo of Jeffrey Epstein" in block
        assert "Glasses for people who don't do consent" in block

    def test_sandwich_board_rayban_flagship_quote(self):
        block = get_521_block()
        assert "sandwich board" in block
        assert "Ray-Ban's flagship store" in block

    def test_pervert_glasses_instagram_quote(self):
        block = get_521_block()
        assert "pervert glasses" in block
        assert "Instagram" in block

    def test_page_tags(self):
        block = get_521_block()
        assert "Protest Art" in block

    def test_not_a_new_campaign_discipline(self):
        block = get_521_block()
        lower = block.lower()
        assert "not a new vertical" in lower
        assert "primary-campaign hold stands" in lower

    def test_kylie_second_piece_https_opened_repo_grounded(self):
        block = get_521_block()
        assert "https://hyperallergic.com/guerrilla-london-bus-ads-mock-kylie-jenners-meta-glasses-campaign/" in block
        assert "Kylie" in block
        lower = block.lower()
        assert "repo-grounded" in lower

    def test_kylie_spokesperson_quotes(self):
        block = get_521_block()
        assert "track us in the real world too" in block
        assert "that's abuse" in block

    def test_kylie_corroborating_details(self):
        block = get_521_block()
        assert "Harvard" in block
        assert "LED" in block

    def test_instagram_corroboration_bounded(self):
        block = get_521_block()
        lower = block.lower()
        assert "second-hand corroboration" in lower
        assert "bounded" in lower
        assert "not opened first-hand" in lower

    def test_provenance_guard(self):
        block = get_521_block()
        assert "latestly.com" in block
        lower = block.lower()
        assert "spoof activism" in lower

    def test_email_drive_standing(self):
        block = get_521_block()
        assert "9,000" in block
        assert "muckrack.com" in block

    def test_no_competitor_equivalent_bounded(self):
        block = get_521_block()
        lower = block.lower()
        assert "twenty-seven" in lower
        assert "bounded search-result absence" in lower

    def test_known_corpus_only(self):
        block = get_521_block()
        lower = block.lower()
        assert "no new primary campaign motif" in lower


class TestNewPressItems:
    def test_webpronews_snippet_bounded(self):
        block = get_521_block()
        assert "webpronews.com" in block
        assert "Sam Altman Rejects Smart Glasses" in block
        lower = block.lower()
        assert "snippet-bounded" in lower

    def test_webpronews_competitor_context_noted(self):
        block = get_521_block()
        lower = block.lower()
        assert "samsung" in lower or "gentle monster" in lower
        assert "snap" in lower

    def test_glassalmanac_snippet_bounded(self):
        block = get_521_block()
        assert "glassalmanac.com" in block
        assert "HateAid" in block
        assert "Josephine Ballon" in block
        lower = block.lower()
        assert "snippet-bounded" in lower

    def test_glassalmanac_criminal_complaint_detail(self):
        block = get_521_block()
        assert "Aug 12 2026" in block
        assert "criminal complaint" in block.lower()


class TestAttentionSphere:
    def test_27th_no_match(self):
        block = get_521_block()
        lower = block.lower()
        assert "twenty-seventh" in lower
        assert "no-match" in lower or "no matching podcast" in lower

    def test_circular_rejection(self):
        block = get_521_block()
        lower = block.lower()
        assert "circular" in lower
        assert "not cited as evidence" in lower

    def test_purposeful_empathy_secondary_corroboration(self):
        block = get_521_block()
        lower = block.lower()
        assert "purposeful empathy" in lower
        assert "secondary corroboration" in lower

    def test_bounded_claim(self):
        block = get_521_block()
        lower = block.lower()
        assert "bounded search-result absence" in lower

    def test_nonprofit_identification_stays_secondary(self):
        block = get_521_block()
        lower = block.lower()
        assert "secondary-only" in lower
        assert "left to their own devices" in lower


class TestStatisticalHygiene:
    def test_manual_illustrative_label(self):
        block = get_521_block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci NOT_CALCULATED" in block
        assert "is_significant False" in block

    def test_ehe_illustrative_score(self):
        block = get_521_block()
        assert "-8/10" in block

    def test_hyperallergic_not_scored_as_asymmetry_evidence(self):
        block = get_521_block()
        lower = block.lower()
        assert "not scored as asymmetry evidence" in lower

    def test_correlation_not_causation(self):
        block = get_521_block()
        lower = block.lower()
        assert "correlation" in lower
        assert "causation" in lower

    def test_no_em_dashes(self):
        block = get_521_block()
        assert "\u2014" not in block, "Em dash found in #521 block"

    def test_https_only(self):
        block = get_521_block()
        urls = re.findall(r'https?://[^\s)\"]+', block)
        assert urls, "Expected URLs in #521 block"
        for u in urls:
            assert u.startswith("https://"), f"Non-HTTPS URL found: {u}"

    def test_no_false_significance(self):
        block = get_521_block()
        lower = block.lower()
        assert "no claim of empirical significance" in lower or "do not claim empirical" in lower

    def test_confounders_ranked(self):
        block = get_521_block()
        lower = block.lower()
        assert "strong" in lower
        assert "moderate" in lower
        assert "weak" in lower


class TestNoveltyAndDuplicatePrevention:
    def test_no_microsoft_pcm_novelty_claim(self):
        block = get_521_block()
        lower = block.lower()
        # The only permitted PCM mention is the explicit no-novelty-claim guard
        assert lower.count("pcm") <= 1
        assert "no microsoft pcm novelty claim" in lower


class TestIterationLog:
    def test_iteration_log_521_exists(self):
        log_text = LOG_PATH.read_text(encoding="utf-8")
        assert "#521" in log_text
        assert "Type E" in log_text
        assert "2026-09-04 16:00 PDT" in log_text

    def test_log_newest_first_relative(self):
        # Durable rule (fixed #495): relative newest-first ordering between
        # neighboring entries, never absolute-top assertions.
        log_text = LOG_PATH.read_text(encoding="utf-8")
        idx_521 = log_text.find("#521 Type E")
        idx_520 = log_text.find("#520 Type D")
        assert idx_521 != -1 and idx_520 != -1
        assert idx_521 < idx_520, "#521 entry must precede #520 (newest-first)"
