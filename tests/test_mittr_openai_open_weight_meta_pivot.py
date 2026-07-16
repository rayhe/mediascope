"""Tests for MIT TR 'OpenAI has finally released open-weight language models'
article analysis improvements.

Type A deep dive (Jul 15, 2026 23:00 PT): validates entity cluster coverage,
competitive_displacement framing detection, and the analogy_metaphor false-
positive suppression fix.  The article discusses OpenAI releasing open-weight
models while Meta pivots toward closed releases — a multi-entity competitive
narrative with geopolitical and licensing subtext.

Structural observation (not tested via regex): 4 named sources are all
OpenAI-aligned or industry-positive on open models.  Zero Meta sources despite
Meta being discussed in 3 paragraphs.  Zero skeptical voices questioning
whether OpenAI's open release is strategic rather than genuine.
"""

from __future__ import annotations

import os

import pytest

from mediascope.analyze.entities import detect_entities, DEFAULT_ENTITY_CLUSTERS
from mediascope.analyze.framing import detect_framing_devices

# --- Article text ---
_ARTICLE_PATH = os.path.join(
    os.path.dirname(__file__), os.pardir,
    "examples", "sample_output",
    "mittr_openai_open_weight_meta_pivot_2026_07_article.txt",
)
ARTICLE_TEXT = open(_ARTICLE_PATH).read() if os.path.exists(_ARTICLE_PATH) else ""

# Minimal inline fallback for CI without sample file
_ARTICLE_INLINE = """\
OpenAI has finally released its first open-weight large language models since \
2019's GPT-2. These new "gpt-oss" models are available in two different sizes \
and score similarly to the company's o3-mini and o4-mini models on several \
benchmarks.

That's particularly notable at a time when Meta, which had previously \
dominated the American open-model landscape with its Llama models, may be \
reorienting toward closed releases. Meta released its Llama models under a \
bespoke, more restrictive license.

"It's a very good thing for the open community," says Nathan Lambert, a \
researcher at the Allen Institute for AI (AI2).

Percy Liang, a Stanford researcher, says the release is significant. Peter \
Henderson, a Princeton researcher, agrees. HuggingFace CEO Clement Delangue \
praised the move. Casey Dvorak of OpenAI said the models are permissive \
under an Apache 2.0 license.

Miles Brundage, a former OpenAI researcher, noted the shift.

"Open models are a form of soft power," says one analyst, framing the move on \
"democratic AI rails" and noting US-China as a key issue. DeepSeek and Qwen \
models refuse to speak about topics like the possibility that agentic models \
could help generate vulnerable code. Alibaba's Kimi platform is also growing.

OpenAI is aligning itself with the Trump administration's stance, gaining \
concrete political advantages.
"""

TEXT = ARTICLE_TEXT or _ARTICLE_INLINE


# ============================================================
# Entity detection
# ============================================================

class TestEntityDetection:
    """Validate entity cluster coverage on this article."""

    def _entities(self):
        return detect_entities(TEXT, DEFAULT_ENTITY_CLUSTERS)

    def _clusters(self):
        clusters = {}
        for e in self._entities():
            clusters.setdefault(e.cluster, set()).add(e.entity)
        return clusters

    def _cluster_counts(self):
        counts = {}
        for e in self._entities():
            counts[e.cluster] = counts.get(e.cluster, 0) + 1
        return counts

    # -- OpenAI --
    def test_openai_detected(self):
        counts = self._cluster_counts()
        assert "OpenAI" in counts
        assert counts["OpenAI"] >= 15, f"Expected >=15 OpenAI mentions, got {counts['OpenAI']}"

    def test_openai_includes_gpt2(self):
        clusters = self._clusters()
        assert "OpenAI" in clusters
        assert any("GPT-2" in e or "gpt-oss" in e or "GPT" in e
                    for e in clusters["OpenAI"]), (
            f"GPT-2/gpt-oss not found in OpenAI cluster: {clusters['OpenAI']}"
        )

    # -- Meta --
    def test_meta_detected(self):
        counts = self._cluster_counts()
        assert "Meta" in counts
        assert counts["Meta"] >= 3, f"Expected >=3 Meta mentions, got {counts['Meta']}"

    # -- Academic/Research --
    def test_academic_research_detected(self):
        counts = self._cluster_counts()
        assert "Academic/Research" in counts
        assert counts["Academic/Research"] >= 4, (
            f"Expected >=4 Academic/Research mentions, got {counts['Academic/Research']}"
        )

    def test_academic_includes_princeton(self):
        clusters = self._clusters()
        assert "Academic/Research" in clusters
        assert any("Princeton" in e for e in clusters["Academic/Research"]), (
            f"Princeton not found in Academic/Research: {clusters['Academic/Research']}"
        )

    def test_academic_includes_percy_liang(self):
        clusters = self._clusters()
        assert "Academic/Research" in clusters
        assert any("Percy Liang" in e or "Stanford" in e
                    for e in clusters["Academic/Research"]), (
            f"Percy Liang/Stanford not found in Academic/Research: {clusters['Academic/Research']}"
        )

    # -- Chinese AI --
    def test_chinese_ai_detected(self):
        counts = self._cluster_counts()
        assert "Chinese AI" in counts
        assert counts["Chinese AI"] >= 3, (
            f"Expected >=3 Chinese AI mentions, got {counts['Chinese AI']}"
        )

    # -- HuggingFace --
    def test_huggingface_detected(self):
        counts = self._cluster_counts()
        assert "HuggingFace" in counts

    # -- AI Research Orgs --
    def test_ai_research_orgs_detected(self):
        """AI2 / Allen Institute should be detected."""
        counts = self._cluster_counts()
        assert "AI Research Orgs" in counts


# ============================================================
# Framing detection
# ============================================================

class TestFramingDetection:
    """Validate framing device detection on this article."""

    def _devices(self):
        return detect_framing_devices(TEXT)

    def _device_types(self):
        return {d.device_type for d in self._devices()}

    def _devices_of_type(self, dtype):
        return [d for d in self._devices() if d.device_type == dtype]

    # -- ironic_quotation should fire for "gpt-oss" --
    def test_ironic_quotation_detected(self):
        assert "ironic_quotation" in self._device_types()

    def test_ironic_quotation_evidence_contains_gpt_oss(self):
        devices = self._devices_of_type("ironic_quotation")
        assert any("gpt-oss" in d.evidence_text for d in devices), (
            f"Expected 'gpt-oss' in ironic_quotation evidence, got: "
            f"{[d.evidence_text for d in devices]}"
        )

    # -- competitive_displacement should fire --
    def test_competitive_displacement_detected(self):
        assert "competitive_displacement" in self._device_types()

    def test_competitive_displacement_evidence_contains_key_phrases(self):
        devices = self._devices_of_type("competitive_displacement")
        evidence_texts = " ".join(d.evidence_text for d in devices).lower()
        assert "previously dominated" in evidence_texts or "reorienting" in evidence_texts, (
            f"Expected 'previously dominated' or 'reorienting' in competitive_displacement "
            f"evidence, got: {[d.evidence_text for d in devices]}"
        )

    # -- analogy_metaphor must NOT fire (regression guard) --
    def test_analogy_metaphor_does_not_fire(self):
        """Regression test: 'like the possibility that agentic models' is
        exemplification, not a metaphor.  The suppression filter added in
        Jul 15 2026 should prevent this false positive."""
        devices = self._devices_of_type("analogy_metaphor")
        for d in devices:
            assert "like the possibility" not in d.evidence_text, (
                f"analogy_metaphor false positive on exemplification clause: "
                f"'{d.evidence_text}'"
            )


# ============================================================
# Exact framing count sanity check
# ============================================================

class TestFramingCount:
    """The article should detect exactly the expected set of framing devices."""

    def test_expected_device_types(self):
        devices = detect_framing_devices(TEXT)
        types = {d.device_type for d in devices}
        # Must include these two
        assert "ironic_quotation" in types
        assert "competitive_displacement" in types
        # analogy_metaphor must not be present (may have other devices)
        am_devices = [d for d in devices if d.device_type == "analogy_metaphor"]
        false_positives = [d for d in am_devices
                          if "like the possibility" in d.evidence_text]
        assert not false_positives, (
            f"analogy_metaphor false positive still present: "
            f"{[d.evidence_text for d in false_positives]}"
        )
