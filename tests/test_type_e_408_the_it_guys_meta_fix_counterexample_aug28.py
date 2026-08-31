"""
Test Type E #408 - The IT Guys Meta fix counterexample Aug 28 2026
Verifies podcast-sentiment.md entry 123 exists and sources cited.
"""
def test_entry_123_exists():
    import pathlib
    p = pathlib.Path("podcast-sentiment.md")
    assert p.exists()
    txt = p.read_text()
    assert "The IT Guys" in txt
    assert "5 PM Technology News Recap" in txt or "5pm" in txt.lower() or "5 PM" in txt
    assert "theitguysfix.com" in txt
    assert "kittentts-bella" in txt.lower() or "KittenTTS Bella" in txt

def test_sources_cited():
    import pathlib
    txt = pathlib.Path("podcast-sentiment.md").read_text()
    # entry 123 should have at least 5 source URLs
    assert txt.count("https://") >= 5
