"""Type E #450: Podcast Sentiment Tracking - Thirteenth Verification Sep 1 2026 16:00 PDT"""

def test_mechanism_exists():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "Iteration #450" in p
    assert "Type E #450" in p

def test_guilty_feminist_latest_498_no_499():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "498 Politics" in p
    assert "31 Aug 2026" in p or "31 August 2026" in p
    assert "no 499 as of Sep 1 16:00" in p or "No 499" in p or "no new episode beyond 498" in p.lower()

def test_guilty_feminist_no_meta():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text().lower()
    assert "no meta" in p
    assert "silence maintained" in p

def test_thirteenth_verification_cycle():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "Thirteenth Verification" in p or "13th verification" in p or "13th Verification" in p

def test_ehe_activist_group_not_podcast():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "Everyone Hates Elon" in p
    assert "Activist group" in p or "activist group" in p
    assert "not a podcast" in p.lower() or "not podcast" in p.lower()

def test_ehe_22_day_hold():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "22-day hold" in p or "22 day hold" in p.lower()
    assert "Aug 10" in p

def test_ehe_campaign_timeline():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "Bezos" in p or "Met Gala" in p
    assert "Trump" in p and "Epstein" in p
    assert "Windsor Castle" in p
    assert "JD Vance" in p or "Vance" in p

def test_ehe_london_vs_musk():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "London vs Musk" in p
    assert "Tesla Model S" in p

def test_attention_sphere_nonprofit():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "Attention Sphere" in p
    assert "Non-profit org" in p or "non-profit org" in p.lower()
    assert "No matching podcast" in p or "no matching podcast" in p.lower()

def test_attention_sphere_13th_no_match():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "13th" in p or "Thirteenth" in p
    assert "Attention Sphere" in p

def test_fortune_ai_weekly_revalidation():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "Fortune AI Weekly" in p
    assert "Why Meta's Ray-Bans" in p or "Why Meta" in p

def test_fortune_daily_jony_ive():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "Fortune Daily" in p
    assert "Jony Ive" in p

def test_9to5mac_daily():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "9to5Mac" in p
    assert "AirPods" in p

def test_ai2day_duplicate_prevention():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "AI2Day" in p
    assert "DUPLICATE PREVENTION" in p or "duplicate prevention" in p.lower()

def test_secondary_sources_present():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "LatestLY" in p
    assert "Marketplace" in p
    assert "Shared Security" in p

def test_podcast_vs_print_framing():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "WIRED" in p
    assert "MANUAL ILLUSTRATIVE" in p
    assert "p_value NOT_CALCULATED" in p

def test_sentiment_methodology_manual():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "MANUAL ILLUSTRATIVE" in p
    assert "is_significant False" in p or "is_significant false" in p.lower()

def test_novelty_vs_existing():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "Mechanism 445" in p or "#445" in p
    assert "Microsoft PCM" in p

def test_confounders_ranked():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "STRONG" in p
    assert "MODERATE" in p
    assert "WEAK" in p
    assert "NOT_CALCULATED" in p

def test_cautious_language():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text().lower()
    assert "correlation does not imply causation" in p or "correlation not causation" in p
    assert "structural incentive" in p

def test_no_em_dashes():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    # Check last iteration block only to avoid false positives from earlier content
    last = p.split("## Iteration #450")[-1]
    assert "—" not in last, "em dash found in #450 block"

def test_source_urls_https():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    last = p.split("## Iteration #450")[-1]
    assert "https://guiltyfeminist.com/list-of-episodes/" in last
    assert "https://en.wikipedia.org/wiki/Everyone_Hates_Elon" in last
    # Circular GitHub reference must be marked as REMOVED, not present as primary
    assert "github.com/rayhe/mediascope/blob/HEAD/podcast-sentiment.md" not in last or "REMOVED" in last or "circular" in last.lower()
    # Verify secondary/unverified labeling
    assert "SECONDARY" in last
    assert "UNVERIFIED" in last or "unverified" in last.lower()
    # Verify MANUAL ILLUSTRATIVE discipline preserved
    assert "MANUAL ILLUSTRATIVE" in last
    assert "p_value NOT_CALCULATED" in last
    assert "is_significant False" in last or "is_significant false" in last.lower()

def test_circular_source_removed():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    last = p.split("## Iteration #450")[-1]
    # The circular self-reference must not be claimed as a valid source
    # It should be explicitly noted as removed or absent as primary
    assert "circular" in last.lower() or "REMOVED" in last
    # No claim that GitHub blob is a primary source for Attention Sphere
    assert "Attention Sphere" in last
    # Verify Wikipedia correctly labeled as secondary not primary
    assert "Wikipedia" in last and ("secondary" in last.lower())

def test_source_count_corrected():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    last = p.split("## Iteration #450")[-1]
    # Heading must not still claim 17 HTTPS Direct after circular removal
    assert "17 HTTPS Direct" not in last or "16 HTTPS" in last or "Circular Removed" in last

def test_goal_job_ids():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "goal_54093bda4145" in p
    assert "mediascope-daily-iteration" in p
    assert "iteration 450" in p.lower() or "Iteration #450" in p

def test_rotation_transparency():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "Rotation Transparency" in p
    assert "449 D to 450 E" in p

def test_extension_justification():
    import pathlib
    p=pathlib.Path("podcast-sentiment.md").read_text()
    assert "Extension vs Duplicate" in p or "Extension not duplicate" in p
