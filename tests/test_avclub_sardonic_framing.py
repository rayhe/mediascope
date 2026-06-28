"""Tests for AV Club Meta Arena gambling framing analysis.

Validates detection of sardonic/sarcastic framing devices identified
in the AV Club's coverage of Meta's Arena prediction market app.
The article is a stress test for sarcasm detection: almost every sentence
deploys loaded language, ironic quotation, or mock-certainty sarcasm.

Added: 2026-06-27 (Type A iteration — AV Club sardonic framing deep dive)
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices


# Full article text (stripped of metadata header)
ARTICLE_TEXT = """
We live in a golden age of online gambling, as sports betting sites recruit SNL stars to voice commercials they label as "content" while sinking their hooks into long-running game shows, and the rise of "prediction markets" allows betting to move out of arenas and stadiums and into exciting realms like "Will the United States invade other countries and capture their heads of state?" (That last one is currently the subject of a high-profile court case, after a U.S. Army soldier was accused of making more than $400,000 off of "predictions" fueled by his knowledge of plans for the capture of Venezuela's Nicolás Maduro earlier this year.) All of which has led Mark Zuckerberg, the frequently sidelined wallflower of Silicon Valley's cadre of gormless tech bros, to ask, "Why not me?"

This is per reporting this week in The New York Times, which reports that Zuck has been pushing his forces at Meta hard in the production of Arena, a prediction market he hopes to launch into the same space currently addicting dopamine-seekers courtesy of sites like Kalshi and Polymarket. Admittedly, Meta's version will have one big twist: The current version of the project apparently runs off of meaningless "points," not actual cash. Which suggests that either a) Zuckerberg doesn't want to get yelled at/regulated by people who will be angry about him turning Facebook into an actual gambling site, or, b) he's banking on the fact that people are more addicted to the betting part of prediction markets than the actual "winning money" portion. What's that? You'd like to hear that last thought rephrased in some real "woof, felt that in the pit of our stomachs" corpo-speech from Facebook's executives? By all means: "We believe that prediction markets are one of the more interesting new content types. With the right containers, the social conversation is the payoff as people aim to show off how good they are at predicting things to their friends." You know, like how humans talk!

In fact, the latest reports suggest Zuckerberg has pushed his staff to try to make contacts and partnerships at both Kalshi and Polymarket, who we're sure are just thrilled at the idea of this lumbering behemoth trying to horn in on their scams. Prediction markets—which claim that they're just fun analysis tools that simply happen to resemble fuel for an unquenchable, omnidirectional gambling addiction—are facing increased scrutiny from many legislators and state governments at the moment, although the federal government itself has been very slow to say anything even remotely negative about them, a fact that presumably has absolutely nothing to do with the fact that both Kalshi and Polymarket have paid Donald Trump, Jr., to serve as a "strategic advisers" for them over the last two years.
""".strip()


def _device_types(text: str) -> list[str]:
    """Return sorted list of unique device types detected in *text*."""
    return sorted({d.device_type for d in detect_framing_devices(text)})


def _devices_of_type(text: str, dtype: str) -> list[str]:
    """Return evidence texts for all devices of *dtype* in *text*."""
    return [d.evidence_text for d in detect_framing_devices(text) if d.device_type == dtype]


class TestIronicQuotationDetection:
    """Scare quotes / distancing quotes in the AV Club article."""

    def test_content_scare_quotes(self):
        devices = _devices_of_type(ARTICLE_TEXT, "ironic_quotation")
        evidence = " ".join(devices).lower()
        assert "content" in evidence

    def test_prediction_markets_scare_quotes(self):
        devices = _devices_of_type(ARTICLE_TEXT, "ironic_quotation")
        evidence = " ".join(devices).lower()
        assert "prediction markets" in evidence

    def test_predictions_scare_quotes(self):
        devices = _devices_of_type(ARTICLE_TEXT, "ironic_quotation")
        evidence = " ".join(devices).lower()
        assert "predictions" in evidence

    def test_points_scare_quotes(self):
        devices = _devices_of_type(ARTICLE_TEXT, "ironic_quotation")
        evidence = " ".join(devices).lower()
        assert "points" in evidence

    def test_winning_money_scare_quotes(self):
        devices = _devices_of_type(ARTICLE_TEXT, "ironic_quotation")
        evidence = " ".join(devices).lower()
        assert "winning money" in evidence

    def test_strategic_advisers_scare_quotes(self):
        devices = _devices_of_type(ARTICLE_TEXT, "ironic_quotation")
        evidence = " ".join(devices).lower()
        assert "strategic advisers" in evidence

    def test_ironic_quotation_count(self):
        """Article uses at least 6 distinct scare-quoted terms."""
        devices = _devices_of_type(ARTICLE_TEXT, "ironic_quotation")
        assert len(devices) >= 6


class TestSarcasticCorrectionDetection:
    """Sarcastic/ironic commentary patterns in sardonic journalism."""

    def test_you_know_like_how(self):
        """'You know, like how humans talk!' — post-quote sarcastic aside."""
        devices = _devices_of_type(ARTICLE_TEXT, "sarcastic_correction")
        evidence = " ".join(devices).lower()
        assert "you know" in evidence

    def test_mock_certainty_thrilled(self):
        """'who we're sure are just thrilled' — mock-certainty sarcasm."""
        devices = _devices_of_type(ARTICLE_TEXT, "sarcastic_correction")
        evidence = " ".join(devices).lower()
        assert "thrilled" in evidence

    def test_ironic_denial_presumably(self):
        """'presumably has absolutely nothing to do with' — ironic denial."""
        devices = _devices_of_type(ARTICLE_TEXT, "sarcastic_correction")
        evidence = " ".join(devices).lower()
        assert "presumably" in evidence

    def test_sarcastic_correction_count(self):
        """Article deploys at least 3 sarcastic correction devices."""
        devices = _devices_of_type(ARTICLE_TEXT, "sarcastic_correction")
        assert len(devices) >= 3


class TestLoadedLanguageDetection:
    """Ad hominem and industry-as-vice loaded language."""

    def test_tech_bros(self):
        devices = _devices_of_type(ARTICLE_TEXT, "loaded_language")
        evidence = " ".join(devices).lower()
        assert "tech bro" in evidence

    def test_gormless(self):
        devices = _devices_of_type(ARTICLE_TEXT, "loaded_language")
        evidence = " ".join(devices).lower()
        assert "gormless" in evidence

    def test_wallflower(self):
        devices = _devices_of_type(ARTICLE_TEXT, "loaded_language")
        evidence = " ".join(devices).lower()
        assert "wallflower" in evidence

    def test_lumbering(self):
        devices = _devices_of_type(ARTICLE_TEXT, "loaded_language")
        evidence = " ".join(devices).lower()
        assert "lumbering" in evidence

    def test_scams(self):
        devices = _devices_of_type(ARTICLE_TEXT, "loaded_language")
        evidence = " ".join(devices).lower()
        assert "scam" in evidence

    def test_gambling_addiction(self):
        devices = _devices_of_type(ARTICLE_TEXT, "loaded_language")
        evidence = " ".join(devices).lower()
        assert "gambling addiction" in evidence

    def test_hooks_into(self):
        devices = _devices_of_type(ARTICLE_TEXT, "loaded_language")
        evidence = " ".join(devices).lower()
        assert "hooks" in evidence

    def test_loaded_language_count(self):
        """Article deploys at least 7 loaded language devices."""
        devices = _devices_of_type(ARTICLE_TEXT, "loaded_language")
        assert len(devices) >= 7


class TestOverallFramingProfile:
    """Aggregate framing profile for the article."""

    def test_total_device_count(self):
        """Sardonic article should trigger at least 14 framing devices."""
        devices = detect_framing_devices(ARTICLE_TEXT)
        assert len(devices) >= 14

    def test_device_type_diversity(self):
        """Article should trigger at least 3 distinct device types."""
        types = _device_types(ARTICLE_TEXT)
        assert len(types) >= 3

    def test_core_types_present(self):
        """All three core sardonic device types should be present."""
        types = set(_device_types(ARTICLE_TEXT))
        assert "ironic_quotation" in types
        assert "loaded_language" in types
        assert "sarcastic_correction" in types


class TestIronicDenialIsolated:
    """Isolated unit tests for new ironic denial patterns."""

    def test_presumably_nothing_to_do_with(self):
        text = "presumably has absolutely nothing to do with the payments"
        devices = _devices_of_type(text, "sarcastic_correction")
        assert len(devices) >= 1

    def test_surely_no_connection(self):
        text = "surely no connection to the lobbying"
        devices = _devices_of_type(text, "sarcastic_correction")
        assert len(devices) >= 1

    def test_obviously_entirely_unrelated(self):
        text = "this is obviously entirely unrelated to the investigation"
        devices = _devices_of_type(text, "sarcastic_correction")
        assert len(devices) >= 1


class TestMockCertaintyIsolated:
    """Isolated unit tests for mock-certainty sarcasm patterns."""

    def test_were_sure_thrilled(self):
        text = "we're sure are just thrilled"
        devices = _devices_of_type(text, "sarcastic_correction")
        assert len(devices) >= 1

    def test_im_sure_delighted(self):
        text = "I'm sure they are delighted"
        devices = _devices_of_type(text, "sarcastic_correction")
        assert len(devices) >= 1

    def test_were_sure_with_pronoun(self):
        text = "we're sure he is just thrilled about the news"
        devices = _devices_of_type(text, "sarcastic_correction")
        assert len(devices) >= 1


class TestAdHominemIsolated:
    """Isolated unit tests for ad hominem / character diminishment patterns."""

    def test_tech_bros(self):
        text = "the tech bros of Silicon Valley"
        devices = _devices_of_type(text, "loaded_language")
        assert any("tech bro" in d.lower() for d in devices)

    def test_lumbering_behemoth(self):
        text = "this lumbering behemoth trying to compete"
        devices = _devices_of_type(text, "loaded_language")
        assert any("lumbering" in d.lower() for d in devices)

    def test_megalomania(self):
        text = "critics call it megalomania"
        devices = _devices_of_type(text, "loaded_language")
        assert any("megalomania" in d.lower() for d in devices)


class TestIndustryAsViceIsolated:
    """Isolated unit tests for industry-as-vice framing patterns."""

    def test_their_scams(self):
        text = "horn in on their scams"
        devices = _devices_of_type(text, "loaded_language")
        assert any("scam" in d.lower() for d in devices)

    def test_gambling_addiction(self):
        text = "fuel for an unquenchable gambling addiction"
        devices = _devices_of_type(text, "loaded_language")
        assert any("addiction" in d.lower() for d in devices)

    def test_sinking_hooks(self):
        text = "sinking their hooks into consumers"
        devices = _devices_of_type(text, "loaded_language")
        assert any("hook" in d.lower() for d in devices)
