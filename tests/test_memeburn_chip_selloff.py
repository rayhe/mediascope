"""Regression tests for Memeburn Meta Cloud chip selloff article (Jul 7 2026).

Type A deep dive — tests entity coverage gaps (Oracle, Samsung, SK Hynix,
Semiconductor Equipment, Storage/Memory) and new Meta/OpenAI aliases added
in this iteration, plus the Benchmark homograph fix and new loaded_language
patterns (super bubble, mega bubble).
"""

import pytest

from mediascope.analyze.entities import detect_entities
from mediascope.analyze.framing import detect_framing_devices


# ── Entity detection: new clusters ──────────────────────────────────────


class TestOracleCluster:
    def test_oracle_detected(self):
        mentions = detect_entities("Oracle is one of the five largest hyperscalers.")
        assert any(m.cluster == "Oracle" for m in mentions)

    def test_oracle_cloud(self):
        mentions = detect_entities("Oracle Cloud gained share amid the selloff.")
        assert any(m.cluster == "Oracle" and m.canonical_name == "Oracle Cloud" for m in mentions)

    def test_larry_ellison(self):
        mentions = detect_entities("Larry Ellison said Oracle would expand AI capacity.")
        assert any(m.cluster == "Oracle" and m.canonical_name == "Larry Ellison" for m in mentions)


class TestSamsungCluster:
    def test_samsung_detected(self):
        mentions = detect_entities("Samsung dropped 7% on the news.")
        assert any(m.cluster == "Samsung" for m in mentions)

    def test_samsung_electronics(self):
        mentions = detect_entities("Samsung Electronics reported weaker guidance.")
        assert any(m.cluster == "Samsung" for m in mentions)


class TestSKHynixCluster:
    def test_sk_hynix_detected(self):
        mentions = detect_entities("SK Hynix fell 9% as memory stocks declined.")
        assert any(m.cluster == "SK Hynix" for m in mentions)

    def test_hynix_standalone(self):
        mentions = detect_entities("Hynix supplies HBM chips to Nvidia.")
        assert any(m.cluster == "SK Hynix" for m in mentions)


class TestSemiconductorEquipmentCluster:
    def test_kla_detected(self):
        mentions = detect_entities("KLA dropped 12% in the selloff.")
        assert any(m.cluster == "Semiconductor Equipment" and m.canonical_name == "KLA" for m in mentions)

    def test_lam_research(self):
        mentions = detect_entities("Lam Research fell 10% on Meta Compute fears.")
        assert any(m.cluster == "Semiconductor Equipment" and m.canonical_name == "Lam Research" for m in mentions)

    def test_applied_materials(self):
        mentions = detect_entities("Applied Materials saw its worst day in months.")
        assert any(m.cluster == "Semiconductor Equipment" and m.canonical_name == "Applied Materials" for m in mentions)

    def test_asml(self):
        mentions = detect_entities("ASML warned of potential order cancellations.")
        assert any(m.cluster == "Semiconductor Equipment" for m in mentions)


class TestStorageMemoryCluster:
    def test_sandisk_detected(self):
        mentions = detect_entities("SanDisk plunged 14% amid overcapacity fears.")
        assert any(m.cluster == "Storage/Memory" and m.canonical_name == "SanDisk" for m in mentions)

    def test_western_digital(self):
        mentions = detect_entities("Western Digital shares fell sharply.")
        assert any(m.cluster == "Storage/Memory" for m in mentions)


# ── Entity detection: new aliases for existing clusters ─────────────────


class TestMetaComputeAliases:
    def test_meta_compute(self):
        mentions = detect_entities("Meta Compute represents a new cloud play.")
        assert any(m.cluster == "Meta" and m.canonical_name == "Meta Compute" for m in mentions)

    def test_santosh_janardhan(self):
        mentions = detect_entities("Santosh Janardhan leads Meta's infrastructure.")
        assert any(m.cluster == "Meta" and m.canonical_name == "Santosh Janardhan" for m in mentions)

    def test_daniel_gross_meta(self):
        mentions = detect_entities("Daniel Gross runs Superintelligence Labs.")
        assert any(m.cluster == "Meta" and m.canonical_name == "Daniel Gross" for m in mentions)


class TestOpenAIJalapeno:
    def test_jalapeno_chip(self):
        mentions = detect_entities("OpenAI's custom chip, codenamed Jalapeño, aims to reduce reliance on Nvidia.")
        assert any(m.cluster == "OpenAI" and "Jalapeño" in m.canonical_name for m in mentions)


class TestFinancialServicesNewAliases:
    def test_bernstein(self):
        mentions = detect_entities("Bernstein analysts downgraded the sector.")
        assert any(m.cluster == "Financial Services" and m.canonical_name == "Bernstein" for m in mentions)

    def test_deloitte(self):
        mentions = detect_entities("Deloitte projected semiconductor sales of $1 trillion.")
        assert any(m.cluster == "Financial Services" and m.canonical_name == "Deloitte" for m in mentions)


# ── Benchmark homograph fix ─────────────────────────────────────────────


class TestBenchmarkHomograph:
    def test_benchmark_common_noun_not_matched(self):
        """'benchmark' as a common noun should NOT match VC/Tech Investors."""
        mentions = detect_entities("a benchmark tracking 30 major chipmakers fell 8%")
        assert not any(m.cluster == "VC/Tech Investors" and "Benchmark" in m.canonical_name for m in mentions), \
            "Common-noun 'benchmark' should not match VC firm Benchmark"

    def test_benchmark_vc_firm_matched(self):
        """'Benchmark' followed by VC context words should still match."""
        mentions = detect_entities("Benchmark led the Series A round.")
        assert any(m.cluster == "VC/Tech Investors" for m in mentions)

    def test_benchmark_capital(self):
        mentions = detect_entities("Benchmark Capital invested $50M.")
        assert any(m.cluster == "VC/Tech Investors" for m in mentions)


# ── Loaded language: financial crash terms ──────────────────────────────


class TestSuperBubbleFraming:
    def test_super_bubble(self):
        devices = detect_framing_devices("This is a super bubble waiting to pop.")
        assert any(d.device_type == "loaded_language" for d in devices)

    def test_mega_bubble(self):
        devices = detect_framing_devices("The AI mega bubble is unprecedented.")
        assert any(d.device_type == "loaded_language" for d in devices)

    def test_house_of_cards(self):
        devices = detect_framing_devices("The entire capex thesis is a house of cards.")
        assert any(d.device_type == "loaded_language" for d in devices)

    def test_bubble_burst(self):
        devices = detect_framing_devices("Analysts warn the bubble burst is imminent.")
        assert any(d.device_type == "loaded_language" for d in devices)
