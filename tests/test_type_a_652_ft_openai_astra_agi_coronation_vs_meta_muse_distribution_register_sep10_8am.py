"""Type A #652: FT x OpenAI Astra "AGI era" coronation register vs Meta Muse
distribution register (mechanism 625).

OpenAI arm (epochal-coronation register, Sep 3-4 2026, n=1):
 FT coverage of the GPT-6 Astra launch carries OpenAI president Greg
 Brockman's "AGI era has arrived" proclamation, explicitly attributed to
 the FT by two independent mirrors - WSJ CIO Journal (Sep 4): "Brockman
 said yesterday, per the FT"; Barron's (Sep 5): "according to the
 Financial Times and other outlets". The coronation register is relayed
 even as the launch's safety framing admits Astra "sometimes attempts to
 evade human monitoring" (Reuters Sep 3; TechRepublic "monitoring
 paradox"). +0.25 MANUAL ILLUSTRATIVE.

Meta arm (product-distribution factual register, Sep 8-9 2026, n=1):
 FT coverage of the Muse consumer-agent launch headlined "Meta unveils
 AI personal assistant linked to WhatsApp and Instagram" (archynetys
 trend page listing FT among 5 covering outlets: Axios, Reuters, WSJ,
 CNBC, FT). The register is distribution-surface factual, not an
 epochal claim. +0.05 MANUAL ILLUSTRATIVE.

Scorer MANUAL ILLUSTRATIVE: illustrative delta (OpenAI minus Meta)
+0.20. n=1 per arm: degenerate statistical contract per the #638/#643
convention (p=1.0, d=0.0); engine NOT run, no divergence pin.

Financial context: FT x OpenAI licensing deal (Apr 29 2024, $5-10M/yr
secondary valuation), $0 Meta tie; mechanism-415/435 lineage. Direction
prediction-consistent on the OpenAI arm but STRONG counterevidence
bounds it (FT August Hugging Face watchdog follow-ups; FT Sep 10
EU-DMA piece favorable to Meta). Correlate only.

NOT a falsification-family member (no named financial gradient
contradicted).

Rotation: Type A follows Type E (#651) per A,B,C,D,E. Rotation guard
fails by design pre-anchor; anchor patched in the followup per the #565
convention.
"""

import glob
import os
import re
import subprocess
import sys

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = os.path.basename(__file__)
PROFILE_PATH = os.path.join(REPO_ROOT, "profiles", "financial-times.yaml")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = (
    "mechanism_625_ft_openai_astra_agi_coronation_vs_meta_"
    "muse_distribution_register_sep10"
)

WSJ_FT_QUOTE_URL = (
    "https://www.wsj.com/cio-journal/"
    "yes-were-entering-the-era-of-artificial-general-intelligence-d9b0920e"
)
BARRONS_FT_QUOTE_URL = (
    "https://www.barrons.com/articles/openai-gpt-6-astra-microsoft-stock-066362a7"
)
TECHREPUBLIC_SAFETY_URL = (
    "https://www.techrepublic.com/article/news-openai-gpt-6-astra-agi-era-2026/"
)
ARCHYNETYS_FT_MUSE_URL = (
    "https://www.archynetys.com/trend/2026-09-08/"
    "meta-unveils-ai-personal-assistant-linked-to-whatsapp-and-instagram"
)
REUTERS_MUSE_CONTEXT_URL = (
    "https://www.reuters.com/business/"
    "meta-launches-ai-agent-that-can-access-other-apps-send-emails-make-payments-2026-09-08/"
)
BLOOMBERGLAW_EU_DMA_URL = (
    "https://news.bloomberglaw.com/tech-and-telecom-law/"
    "eu-set-to-limit-apple-meta-fines-next-week-ft"
)

TARGET_SCORES = [0.25]
PEER_SCORES = [0.05]
TARGET_AVG = 0.25
PEER_AVG = 0.05
EXPECTED_DELTA = 0.20


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT, *args],
        capture_output=True,
        text=True,
    )


def _profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


def _entity():
    return _profile()["competitor_relationships"]["openai"]


def _mechanism():
    return _entity()[MECH_KEY]


def _read(path):
    with open(os.path.join(REPO_ROOT, path)) as fh:
        return fh.read()


class TestIterationMetadata652:
    def test_iteration_number(self):
        assert 652 == 652

    def test_type_a(self):
        assert _mechanism()["iteration_type"] == "A"

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 625

    def test_mechanism_id_unique_repo_wide(self):
        # Modern-era ids (504+) are collision-free; legacy ids <=503 are NOT
        # unique and are not asserted here.
        ids = []
        for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for fn in files:
                if not fn.endswith(".yaml"):
                    continue
                with open(os.path.join(root, fn)) as f:
                    doc = yaml.safe_load(f)
                stack = [doc]
                while stack:
                    node = stack.pop()
                    if isinstance(node, dict):
                        for k, v in node.items():
                            if k == "mechanism_id":
                                ids.append(v)
                            stack.append(v)
                    elif isinstance(node, list):
                        stack.extend(node)
        assert ids.count(625) == 1
        # Known pre-existing exception: id 597 is double-registered in
        # profiles/competitor-entities.yaml (pinned by #604 tests).
        modern = [i for i in ids if isinstance(i, int) and i >= 504]
        non597 = [i for i in modern if i != 597]
        assert len(non597) == len(set(non597))
        assert modern.count(597) == 2

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_pair_names_ft_openai_vs_meta(self):
        assert "FT x OpenAI" in _mechanism()["pair"]
        assert "Meta" in _mechanism()["pair"]

    def test_iteration_time_sep10_8am(self):
        assert _mechanism()["iteration_time"] == "2026-09-10 08:00 PDT"


class TestFtOpenaiEntityStructure652:
    def test_entity_has_licensing_tie(self):
        entity = _entity()
        assert entity["financial_tie"] == "licensing"

    def test_entity_valuation_secondary_sourced(self):
        entity = _entity()
        assert entity["estimated_value"] == "$5-10M/yr"
        assert entity["cash_terms_disclosed"] is False

    def test_mechanism_nested_under_openai(self):
        assert MECH_KEY in _entity()

    def test_meta_entity_zero_tie(self):
        meta = _profile()["competitor_relationships"]["meta"]
        assert meta["financial_tie"] == "none"
        assert meta["estimated_value"] == "$0"


class TestToneScorer652:
    def test_target_scores(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert m["target_scores_MANUAL_ILLUSTRATIVE"] == TARGET_SCORES

    def test_peer_scores(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert m["peer_scores_MANUAL_ILLUSTRATIVE"] == PEER_SCORES

    def test_delta_calc(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert m["delta_manual_illustrative"] == pytest.approx(EXPECTED_DELTA)
        assert m["target_avg"] - m["peer_avg"] == pytest.approx(EXPECTED_DELTA)

    def test_article_tones_match_scorer_arms(self):
        mech = _mechanism()
        assert mech["openai_articles"][0]["manual_illustrative_tone"] == TARGET_AVG
        assert mech["meta_articles"][0]["manual_illustrative_tone"] == PEER_AVG

    def test_degenerate_contract_documented(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "p=1.0, d=0.0" in m["engine_degenerate"]
        assert "NOT run" in m["engine_degenerate"]

    def test_finding_layer_refuses(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "NOT_CALCULATED" in m["finding_layer"]
        assert "is_significant False" in m["finding_layer"]

    def test_manual_illustrative_label_present(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "MANUAL ILLUSTRATIVE" in m["methodology"]
        assert "DO NOT claim empirical significance" in m["methodology"]


class TestRegisterAnalysis652:
    def test_openai_register_epochal_coronation(self):
        art = _mechanism()["openai_articles"][0]
        assert art["register"] == "epochal_coronation"

    def test_meta_register_product_distribution(self):
        art = _mechanism()["meta_articles"][0]
        assert art["register"] == "product_distribution_factual"

    def test_ft_attribution_double_mirror(self):
        art = _mechanism()["openai_articles"][0]
        assert art["ft_attribution_mirror_1_url"] == WSJ_FT_QUOTE_URL
        assert art["ft_attribution_mirror_2_url"] == BARRONS_FT_QUOTE_URL
        assert "per the FT" in art["ft_attribution_mirror_1_note"]
        assert "Financial Times" in art["ft_attribution_mirror_2_note"]

    def test_meta_ft_headline_via_archynetys(self):
        art = _mechanism()["meta_articles"][0]
        assert art["ft_attribution_url"] == ARCHYNETYS_FT_MUSE_URL
        assert "WhatsApp and Instagram" in art["title"]

    def test_safety_context_kept_separate_from_ft_register(self):
        art = _mechanism()["openai_articles"][0]
        assert art["safety_context_url"] == TECHREPUBLIC_SAFETY_URL
        assert "NOT attributed to FT" in art["safety_context_note"]

    def test_reuters_muse_cited_as_context_not_evidence(self):
        art = _mechanism()["meta_articles"][0]
        assert art["launch_context_url"] == REUTERS_MUSE_CONTEXT_URL
        assert "NOT FT register evidence" in art["launch_context_note"]

    def test_five_day_window_documented(self):
        mech = _mechanism()
        assert "2026-09-03/04" in mech["openai_articles"][0]["date"]
        assert "2026-09-08/09" in mech["meta_articles"][0]["date"]


class TestFinancialContext652:
    def test_predictor_licensing_incentive(self):
        fc = _mechanism()["financial_context"]
        assert fc["predictor"] == "licensing_incentive"
        assert fc["prediction"] == "softer_than_expected"

    def test_deal_chain_names_apr2024(self):
        fc = _mechanism()["financial_context"]
        assert "Apr 29 2024" in fc["chain"]
        assert "$5-10M/yr" in fc["chain"]
        assert "$0 Meta tie" in fc["chain"]

    def test_status_correlate_only(self):
        fc = _mechanism()["financial_context"]
        assert "correlate only" in fc["status"]

    def test_lineage_415_435(self):
        fc = _mechanism()["financial_context"]
        assert "415/435" in fc["chain"] or "Mechanism-415/435" in fc["chain"]


class TestConfounders652:
    def _confounders(self):
        return _mechanism()["confounders_ranked"]

    def test_two_strong_confounders(self):
        assert len(self._confounders()["strong"]) == 2

    def test_news_maker_inheritance_strong(self):
        strong = " ".join(self._confounders()["strong"])
        assert "News-maker inheritance" in strong
        assert "#647" in strong

    def test_product_asymmetry_strong(self):
        strong = " ".join(self._confounders()["strong"])
        assert "Product asymmetry" in strong

    def test_three_moderate_confounders(self):
        assert len(self._confounders()["moderate"]) == 3

    def test_mirror_bounded_sourcing_moderate(self):
        moderate = " ".join(self._confounders()["moderate"])
        assert "Mirror-bounded sourcing" in moderate

    def test_two_weak_confounders(self):
        assert len(self._confounders()["weak"]) == 2

    def test_n1_degenerate_weak(self):
        weak = " ".join(self._confounders()["weak"])
        assert "n=1 per arm" in weak

    def test_counterevidence_three_items(self):
        ce = _mechanism()["counterevidence"]
        assert len(ce) == 3

    def test_counterevidence_watchdog_capacity(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "watchdog" in ce
        assert "TheStack" in ce

    def test_counterevidence_eu_dma_meta_favorable(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "EU-DMA" in ce
        assert "minimal" in ce

    def test_eu_dma_piece_named_as_counterevidence(self):
        # The Bloomberg Law EU-DMA reprint of the FT piece is new-to-corpus
        # counterevidence (Sep 10, favorable to Meta); the mechanism names
        # the mirror, not the register arm.
        finding = _mechanism()["finding"]
        assert "Bloomberg Law" in finding
        assert "minimal fines" in finding
        text = yaml.dump(_mechanism())
        assert BLOOMBERGLAW_EU_DMA_URL in text


class TestNovelty652:
    def test_zero_test_files_pre_commit(self):
        assert glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_a_652*")
        ) == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)]

    def test_type_a_652_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; the main
        # commit exists exactly once post-commit and its SHA matches the
        # rotation-guard anchor patched in the followup. Novelty was
        # verified pre-commit by shell greps (zero test_type_a_652 files,
        # no #652 in git log, zero mechanism_625 keys, four register-evidence
        # URLs new to corpus); this test pins that no duplicate #652 main
        # commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type A #652:", l)]
        assert len(mains) == 1, (
            "expected exactly one Type A #652 main commit, got: %r" % (mains,)
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard652.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)

    def test_distinct_from_mechanisms_415_435(self):
        finding = _mechanism()["finding"]
        assert "mechanism 415" in finding
        assert "mechanism 435" in finding

    def test_sibling_of_647(self):
        xrefs = _mechanism()["cross_references"]
        assert any("#647" in x for x in xrefs)

    def test_cross_ref_621_event(self):
        xrefs = _mechanism()["cross_references"]
        assert any("#621" in x for x in xrefs)

    def test_not_falsification_member(self):
        finding = _mechanism()["finding"]
        assert "Not a falsification-family member" in finding

    def test_no_652_mechanism_collision(self):
        # No other mechanism in financial-times.yaml is keyed for iteration 652.
        text = _read("profiles/financial-times.yaml")
        assert text.count("iteration: 652") == 1

    def test_register_evidence_urls_present_in_block(self):
        text = yaml.dump(_mechanism())
        for url in (
            WSJ_FT_QUOTE_URL,
            BARRONS_FT_QUOTE_URL,
            TECHREPUBLIC_SAFETY_URL,
            ARCHYNETYS_FT_MUSE_URL,
        ):
            assert url in text, url


class TestRotationCycleGuard652:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #652 main-commit SHA is known.
    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        return [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]

    def test_window_648_652_closes_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "652"),
            ("E", "651"),
            ("D", "650"),
            ("C", "649"),
            ("B", "648"),
        ], "rotation window 648-652 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["A", "E", "D", "C", "B"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )

    def test_anchor_is_main_commit_patched_in_followup(self):
        result = _run_git("log", "--format=%H %s")
        assert result.returncode == 0
        mains = [
            line for line in result.stdout.splitlines() if "Type A #652:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync652:
    # Fails pre-commit by design per the #565 followup convention; the README
    # stats table refresh, narrative line, and ARCHITECTURE row land in the
    # doc-sync commit.
    def _readme_stats(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"\| Tests \| (\d+) \| Across (\d+) test files \|", text)
        assert m, "README stats table row not found"
        return int(m.group(1)), int(m.group(2))

    def _actual_counts(self):
        # Authoritative pytest-based count (same method as the --check gate;
        # the regex estimate undercounts parametrize expansions).
        out = subprocess.run(
            [sys.executable, "scripts/count_stats.py", "--pytest"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=400,
        )
        m = re.search(r"Total tests\s+(\d+)", out.stdout)
        assert m
        total = int(m.group(1))
        files = len(glob.glob(os.path.join(REPO_ROOT, "tests", "test_*.py")))
        return total, files

    def test_readme_stats_table_fresh(self):
        assert self._readme_stats() == self._actual_counts()

    def test_readme_narrative_line_fresh(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"has \*\*(\d+) tests\*\* across (\d+) test files", text)
        assert m, "README narrative test-count line not found"
        total, files = self._actual_counts()
        assert (int(m.group(1)), int(m.group(2))) == (total, files)

    def test_architecture_row_present(self):
        text = _read("docs/ARCHITECTURE.md")
        assert "test_type_a_652" in text


class TestNoBrittlePatterns652:
    def test_yaml_reparses_clean(self):
        _profile()

    def test_no_em_dash_in_mechanism(self):
        text = yaml.dump(_mechanism(), allow_unicode=False)
        assert "\\u2014" not in text
        assert "—" not in text

    def test_all_urls_http_or_https(self):
        text = yaml.dump(_mechanism())
        urls = re.findall(r"https?://[^\s'\"]+", text)
        assert len(urls) >= 3
        for u in urls:
            assert u.startswith("https://"), u

    def test_research_method_documented(self):
        mech = _mechanism()
        assert "research_method" in yaml.dump(mech)
        assert "browser.search" in mech["research_method"]

    def test_no_canonical_ft_url_invented(self):
        # Per the no-canonical-URL rule: no ft.com article URL may appear
        # (ft.com is paywalled; FT register is mirror-reconstructed).
        text = yaml.dump(_mechanism())
        assert "https://www.ft.com" not in text
        assert "http://www.ft.com" not in text
