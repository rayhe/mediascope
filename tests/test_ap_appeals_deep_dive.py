"""Type A deep-dive tests for AP 'Meta appeals verdict' article.

Discovered in MediaScope Type A iteration 2026-07-12 22:00 PT.
Tests framing gaps fixed this iteration:
  - loaded_language: "hook" (base infinitive verb, was only catching "hooked")
  - loaded_language: "legal woes" (editorial dramatization)
  - loaded_language: "shielded from" (legal-protection-as-hiding metaphor)

Article: "Meta appeals verdict in social media addiction lawsuit"
Publication: AP (syndicated via The Hindu Business Line)
Published: July 11, 2026
"""

import pytest

from mediascope.analyze.framing import detect_framing_devices


# ----- Excerpts targeting specific patterns ----- #

HOOK_INFINITIVE = (
    "Meta, the parent company of Instagram and Facebook, has appealed "
    "the verdict of a landmark social media addiction lawsuit in Los Angeles, "
    "challenging the jury's determination that the company designed its "
    "platforms to hook young users without concern for their well-being."
)

LEGAL_WOES = (
    "The verdict in this case came during a time of legal woes for Meta. "
    "A jury in New Mexico returned a verdict finding that Meta's platforms "
    "harm children's mental health and safety just one day before the "
    "California jury reached its decision."
)

SHIELDED_FROM = (
    "Tech companies like Meta and YouTube are shielded from legal "
    "responsibility for content posted by third parties, based on "
    "Section 230 of the 1996 Communications Decency Act."
)

FULL_ARTICLE = (
    "Meta, the parent company of Instagram and Facebook, has appealed "
    "the verdict of a landmark social media addiction lawsuit in Los Angeles, "
    "challenging the jury's determination that the company designed its "
    "platforms to hook young users without concern for their well-being. "
    "Lawyers representing Meta filed a notice of appeal Tuesday in Los "
    "Angeles County Superior Court. The lawyers will provide their arguments "
    "related to the appeal in subsequent court filings. "
    "The case centred on a 20-year-old woman who said she became addicted "
    "to social media as a child and that it worsened her mental health "
    "struggles. The jury found that negligence by both Meta and Google-owned "
    "YouTube, which was also a defendant in the case, was a substantial "
    "factor in causing harm to the young woman, identified in court only "
    "by her initials, KGM, and her first name, Kaley. "
    'The jury awarded her $3 million in damages and recommended an '
    'additional $3 million in punitive damages. Her lead attorney, Mark '
    'Lanier, said in a statement Friday that the legal team is expecting '
    'the appellate court to "continue the careful application of the law '
    'to this case, affirming the verdict of the trial court." '
    "A notice of appeal starts what can be a lengthy process. A Meta "
    "spokesperson provided a statement Friday that they also gave when "
    "the jury returned the verdict in March, saying that teen mental health "
    'is "profoundly complex and cannot be linked to a single app." '
    "Meta and Google had each filed post-trial motions for judgment "
    "notwithstanding the verdict — a routinely filed motion by defence "
    "lawyers asking a judge to toss out the jury's verdict — and for a "
    "new trial. The trial judge, Carolyn B. Kuhl, denied those motions "
    "in early June. "
    "Tech companies like Meta and YouTube are shielded from legal "
    "responsibility for content posted by third parties, based on "
    "Section 230 of the 1996 Communications Decency Act. To get around "
    "those protections, the plaintiffs focused on the design features of "
    'the platforms like "infinite scroll," or the endless nature of feeds '
    "on the platforms, and autoplay functions. "
    "Questions about encroaching into content-related territory were the "
    "subject of many objections from the defendants throughout the "
    "five-week trial. "
    "The verdict in this case came during a time of legal woes for Meta. "
    "A jury in New Mexico returned a verdict finding that Meta's platforms "
    "harm children's mental health and safety just one day before the "
    "California jury reached its decision. The New Mexico jury, siding "
    "with state prosecutors who brought the case, landed on a penalty of "
    "$375 million. Meta has said the company disagrees with the verdict "
    "and will also appeal in that case. "
    '"We will continue to defend ourselves vigorously, and we remain '
    'confident in our record of protecting teens online," a Meta '
    "spokesperson said in a statement at the time of the verdicts and "
    "again on Friday. "
    "Kaley's case was a first-of-its-kind lawsuit, and the verdict could "
    "influence the outcome of thousands of similar lawsuits accusing "
    "social media companies of deliberately causing harm. TikTok and "
    "Snapchat parent company Snap Inc. were also initially named as "
    "defendants in the case, but each settled for undisclosed sums "
    "before the trial began."
)


# ---- Tests for Fix 1: "hook" base infinitive ---- #


class TestHookInfinitive:
    """Ensure bare infinitive 'hook' is detected as loaded_language."""

    def test_hook_infinitive_detected(self):
        devices = detect_framing_devices(HOOK_INFINITIVE)
        types_evidence = [(d.device_type, d.evidence_text) for d in devices]
        assert any(
            dt == "loaded_language" and "hook" in ev.lower()
            for dt, ev in types_evidence
        ), f"Expected loaded_language 'hook' but got: {types_evidence}"

    def test_hook_conjugations(self):
        """All verb forms should fire loaded_language."""
        for form in ["hook", "hooks", "hooked", "hooking"]:
            text = f"The platform was designed to {form} teenagers."
            devices = detect_framing_devices(text)
            ll = [d for d in devices if d.device_type == "loaded_language"]
            assert ll, f"loaded_language not detected for '{form}'"


# ---- Tests for Fix 2: "legal woes" editorialization ---- #


class TestLegalWoes:
    """'Legal woes' and variants should trigger loaded_language."""

    def test_legal_woes_detected(self):
        devices = detect_framing_devices(LEGAL_WOES)
        types_evidence = [(d.device_type, d.evidence_text) for d in devices]
        assert any(
            dt == "loaded_language" and "woes" in ev.lower()
            for dt, ev in types_evidence
        ), f"Expected loaded_language 'woes' but got: {types_evidence}"

    @pytest.mark.parametrize(
        "modifier",
        ["legal", "financial", "regulatory", "mounting", "growing"],
    )
    def test_woes_with_modifiers(self, modifier):
        text = f"The company faces {modifier} woes after the ruling."
        devices = detect_framing_devices(text)
        ll = [d for d in devices if d.device_type == "loaded_language"
              and "woes" in d.evidence_text.lower()]
        assert ll, f"loaded_language not detected for '{modifier} woes'"


# ---- Tests for Fix 3: "shielded from" metaphor ---- #


class TestShieldedFrom:
    """'Shielded from' legal-protection-as-hiding should fire loaded_language."""

    def test_shielded_from_detected(self):
        devices = detect_framing_devices(SHIELDED_FROM)
        types_evidence = [(d.device_type, d.evidence_text) for d in devices]
        assert any(
            dt == "loaded_language" and "shielded" in ev.lower()
            for dt, ev in types_evidence
        ), f"Expected loaded_language 'shielded from' but got: {types_evidence}"

    @pytest.mark.parametrize("prep", ["from", "against", "by"])
    def test_shielded_prepositions(self, prep):
        text = f"Companies are shielded {prep} lawsuits under the statute."
        devices = detect_framing_devices(text)
        ll = [d for d in devices if d.device_type == "loaded_language"
              and "shielded" in d.evidence_text.lower()]
        assert ll, f"loaded_language not detected for 'shielded {prep}'"


# ---- Full-article integration test ---- #


class TestFullArticleIntegration:
    """Verify all expected devices fire on the complete article."""

    def test_minimum_device_count(self):
        devices = detect_framing_devices(FULL_ARTICLE)
        assert len(devices) >= 12, (
            f"Expected ≥12 devices, got {len(devices)}: "
            f"{[(d.device_type, d.evidence_text[:40]) for d in devices]}"
        )

    def test_all_three_fixes_present(self):
        devices = detect_framing_devices(FULL_ARTICLE)
        types_evidence = [(d.device_type, d.evidence_text.lower()) for d in devices]

        assert any(
            dt == "loaded_language" and ev == "hook"
            for dt, ev in types_evidence
        ), "Fix 1 (hook infinitive) not firing on full article"

        assert any(
            dt == "loaded_language" and "woes" in ev
            for dt, ev in types_evidence
        ), "Fix 2 (legal woes) not firing on full article"

        assert any(
            dt == "loaded_language" and "shielded" in ev
            for dt, ev in types_evidence
        ), "Fix 3 (shielded from) not firing on full article"

    def test_landmark_still_detected(self):
        devices = detect_framing_devices(FULL_ARTICLE)
        assert any(
            d.device_type == "loaded_language" and "landmark" in d.evidence_text.lower()
            for d in devices
        )

    def test_kicker_framing_detected(self):
        devices = detect_framing_devices(FULL_ARTICLE)
        assert any(d.device_type == "kicker_framing" for d in devices)

    def test_trend_bundling_detected(self):
        devices = detect_framing_devices(FULL_ARTICLE)
        assert any(d.device_type == "trend_bundling" for d in devices)
