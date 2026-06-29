"""Tests for denial_contradiction detection of combative denial keywords.

Verifies that 'fundamentally flawed', 'flawed', and 'misunderstanding'
are caught by the denial_contradiction framing device detector, and
that 'replicated' works as an evidence-counter keyword.

Added in: 2026-06-29 Type A deep dive (Engadget child safety article)
"""

from mediascope.analyze.framing import detect_framing_devices


def test_fundamentally_flawed_denial_with_replication():
    """'fundamentally flawed' denial near evidence of replication."""
    text = (
        'Meta called the report "fundamentally flawed and demonstrates '
        'a basic misunderstanding of how our tools work." However, the '
        "New York Times reported that it was able to replicate the "
        "study's findings independently."
    )
    devices = detect_framing_devices(text)
    types = {d.device_type for d in devices}
    assert "denial_contradiction" in types, (
        f"Expected denial_contradiction for 'fundamentally flawed' "
        f"denial near replication evidence; got {types}"
    )


def test_flawed_study_denial_near_confirmation():
    """'flawed' denial near evidence confirmation."""
    text = (
        'The company dismissed the study as "flawed" and said it '
        '"misrepresents our safety features." But researchers at two '
        "universities confirmed the results using independent testing."
    )
    devices = detect_framing_devices(text)
    types = {d.device_type for d in devices}
    assert "denial_contradiction" in types, (
        f"Expected denial_contradiction for 'flawed' denial near "
        f"confirmation; got {types}"
    )


def test_misunderstanding_denial_near_evidence():
    """'misunderstanding' denial near evidence markers."""
    text = (
        'A spokesperson called the findings "a misunderstanding of our '
        'tools" and said the authors "fail to provide examples." Yet the '
        "investigation found that three of the five features tested were "
        "completely non-functional."
    )
    devices = detect_framing_devices(text)
    types = {d.device_type for d in devices}
    assert "denial_contradiction" in types, (
        f"Expected denial_contradiction for 'misunderstanding' denial "
        f"near evidence; got {types}"
    )


def test_replicated_as_evidence_counter():
    """'replicated' should work as evidence counter-keyword."""
    text = (
        '"There is no evidence that our features are broken," the '
        "company said. An independent team replicated the exact same "
        "failures using fresh test accounts."
    )
    devices = detect_framing_devices(text)
    types = {d.device_type for d in devices}
    assert "denial_contradiction" in types, (
        f"Expected denial_contradiction with 'replicated' as evidence "
        f"counter; got {types}"
    )


def test_verified_as_evidence_counter():
    """'verified' should work as evidence counter-keyword."""
    text = (
        '"The claims are baseless," a spokesperson insisted. '
        "Researchers at three universities verified the methodology "
        "and confirmed identical results."
    )
    devices = detect_framing_devices(text)
    types = {d.device_type for d in devices}
    assert "denial_contradiction" in types, (
        f"Expected denial_contradiction with 'verified' as evidence "
        f"counter; got {types}"
    )


def test_fundamentally_flawed_in_evidence_first_pattern():
    """Evidence-first order: findings → then 'fundamentally flawed' denial."""
    text = (
        "The study found that 66% of Instagram's safety features failed "
        "to function as described. Meta's head of safety dismissed the "
        'report as "fundamentally flawed" and said the researchers had '
        '"a basic misunderstanding" of the platform\'s architecture.'
    )
    devices = detect_framing_devices(text)
    types = {d.device_type for d in devices}
    assert "denial_contradiction" in types, (
        f"Expected denial_contradiction in evidence-first pattern with "
        f"'fundamentally flawed'; got {types}"
    )
