"""Type A #682 (2026-09-11 16:00 PDT): FT x Anthropic AISI-refusal
accountability scoop vs FT x Meta/OpenAI launch-week registers.

First dedicated Type A mechanism on FT's Sep 9/10 2026 Anthropic
AISI-refusal accountability scoop: Anthropic refused to submit its latest
model (Claude Mythos 5.1) to the UK AI Security Institute before release,
the first UK bypass, with two AISI architects (Rishi Sunak, Matt Clifford)
now at Anthropic; the story was raised at PMQs. FT original paywalled;
register reconstructed from five attestation snippets this run (Times x2,
lse.co.uk/Alliance News, brieftea, theaiinsider), all five URLs new to
corpus.

The scoop's watchdog accountability register (MANUAL ILLUSTRATIVE -0.45)
CONTRADICTS the anthropic entity block's coverage_prediction ("softer via
Google channel", mechanism 441): the indirect Google channel did not
prevent a watchdog scoop and did not soften the register. FIFTEENTH
falsification-family member (ledger at 14 via mechanism 634, #667; #675
verified no FIFTEENTH anywhere in profiles/).

Same-window FT comparators run the other direction: FT's Sep 10 OpenAI
Astra coverage is the "AGI era" coronation (+0.25, carried from mechanism
625), FT's Meta Muse coverage is neutral product-distribution framing
(+0.05, carried from mechanism 625), and FT's Sep 10 EU-DMA piece is
favorable to Meta (via Bloomberg Law). No FT September accountability
piece surfaced on OpenAI's safety-negative week (Sep 5 wiki incident,
Coxon resignation, Altman slowdown openness) across four search query
sets: bounded search-result absence per the iteration-492 rule, not a
proven zero.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic only):
Meta [+0.05] avg 0.05 vs Anthropic [-0.45] avg -0.45. Delta (Meta minus
Anthropic) +0.50. p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, ci
NOT_CALCULATED, is_significant False, artifact_grade False. NOT
artifact-grade: n=1 scored item per arm (degenerate statistical contract
per the #638/#643 convention), Anthropic tone hand-assigned for the
mirror-attested register, Meta arm tone carried from mechanism 625, no
engine run.

Strongest counterargument: the falsification membership is at the
coverage-selection level and directional only. Mechanism 441's "softer via
Google channel" prediction was made for the fundraising/aspirational
coverage lane; an adversarial AISI-refusal safety scoop does not refute a
softening prediction scoped to fundraising framing, and the watchdog
register is driven by genuine news value (first-ever UK bypass,
revolving door, PMQs). A scope-bounded version of the prediction survives
this finding intact. Accepted as a major counterweight; claim stays
bounded, correlation-only, MANUAL ILLUSTRATIVE.

Evidence hygiene: all five attestation URLs carried verbatim from tool
output this run; no ft.com URLs constructed; FT original paywalled, not
opened; bounded search-result absence stated for FT September OpenAI
accountability coverage; no em dashes; zero repo-wide hits for all five
URLs before this run. Correlation is not causation.

Durable conventions (from #495): line-anchored (^, re.MULTILINE) heading
search in iteration-log.md; relative newest-first ordering between
neighbors, never absolute-top or fixed head slices.
"""

import glob
import os
import re
import subprocess
import sys

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO_ROOT, "profiles", "financial-times.yaml")
LOG = os.path.join(REPO_ROOT, "iteration-log.md")
TEST_BASENAME = "test_type_a_682_ft_anthropic_aisi_refusal_accountability_scoop_vs_meta_sep11_4pm.py"

MECH_KEY = "mechanism_643_ft_anthropic_aisi_refusal_accountability_scoop_vs_meta_openai_launch_week_register_sep11"

TIMES_GAMBLING_URL = "https://www.thetimes.com/uk/technology-uk/article/tech-giants-gambling-with-lives-superintelligence-gh275qr8d"
TIMES_POWERFUL_URL = "https://www.thetimes.com/business/companies-markets/article/anthropic-did-not-submit-most-powerful-ai-model-for-uk-testing-claude-g37tct2vm"
LSE_PMQs_URL = "https://www.lse.co.uk/news/uk-pm-acknowledges-ai-risks-as-anthropic-expert-warns-of-catastrophe-srkc3uncwn4t4tk.html"
BRIEFTEA_URL = "https://brieftea.com/a/anthropic-withheld-its-latest-ai-model-from-uk-testing-102LBWTnUURrip9oKjCa"
AIINSIDER_URL = "https://theaiinsider.tech/2026/09/09/anthropic-faces-scrutiny-over-account-security-and-internal-warnings-on-ai-risk/"
META_MUSE_URL = "https://www.archynetys.com/trend/2026-09-08/meta-unveils-ai-personal-assistant-linked-to-whatsapp-and-instagram"
OPENAI_ASTRA_URL = "https://www.wsj.com/cio-journal/yes-were-entering-the-era-of-artificial-general-intelligence-d9b0920e"
EU_DMA_URL = "https://news.bloomberglaw.com/tech-and-telecom-law/eu-set-to-limit-apple-meta-fines-next-week-ft"


def _load_profile():
    with open(PROFILE) as f:
        return yaml.safe_load(f)


def _mechanism():
    return _load_profile()["competitor_relationships"]["anthropic"][MECH_KEY]


def _mechanism_block_text():
    with open(PROFILE) as f:
        text = f.read()
    start = text.index(MECH_KEY)
    end = text.index("\n  x_twitter:", start)
    return text[start:end]


def _read(path):
    with open(path) as f:
        return f.read()


def _run_git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


class TestNovelty682:
    """Iteration 682 is new; nothing with this number existed pre-commit."""

    def test_single_type_a_682_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_a_682*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_a_682_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; the main
        # commit exists exactly once post-commit and its SHA matches the
        # rotation-guard anchor patched in the followup. Novelty was
        # verified pre-commit by shell greps (zero test_type_a_682 files,
        # no #682 in git log, no mechanism_id 643 in profiles, all five
        # attestation URLs new to corpus); this test pins that no duplicate
        # #682 main commit ever appears.
        out = _run_git("log", "--format=%H %s")
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^Type A #682:", line.split(" ", 1)[-1])
        ]
        assert len(mains) == 1, "expected exactly one Type A #682 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard682.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_anthropic(self):
        profile = _load_profile()
        assert MECH_KEY in profile["competitor_relationships"]["anthropic"]

    def test_mechanism_id_is_next_free(self):
        assert _mechanism()["mechanism_id"] == 643

    def test_identity_fields(self):
        m = _mechanism()
        assert m["iteration"] == 682
        assert m["iteration_type"] == "A"
        assert m["date"] == "2026-09-11"
        assert m["type"] == "Type A - Competitor Coverage Deep Dive"
        assert m["iteration_time"] == "2026-09-11 16:00 PDT"

    def test_publication_pair_and_comparators(self):
        m = _mechanism()
        assert m["publication_pair"] == "FT x Anthropic"
        assert m["competitor"] == "anthropic"
        assert m["comparison_entities"] == ["meta", "openai"]

    def test_author_kit_with_ray(self):
        assert _mechanism()["author"] == "Kit (with Ray)"

    def test_no_em_dashes_in_block(self):
        assert '\u2014' not in _mechanism_block_text()

    def test_test_file_field_matches_this_file(self):
        assert _mechanism()["test_file"].endswith(TEST_BASENAME)


class TestAttestationArms:
    def test_times_gambling_url_verbatim(self):
        urls = [a.get("attestation_url") or a.get("url") for a in _mechanism()["articles"]]
        assert TIMES_GAMBLING_URL in urls

    def test_times_gambling_ft_attribution(self):
        arts = _mechanism()["articles"]
        a = [x for x in arts if x.get("attestation_url") == TIMES_GAMBLING_URL][0]
        assert "refused to submit its latest model to the UK" in a["attestation_excerpt"]
        assert "Rishi Sunak and Matt Clifford" in a["attestation_excerpt"]
        assert a["date"] == "2026-09-09"
        assert a["manual_illustrative_tone"] == -0.45
        assert "accountability scoop" in a["register"]
        assert "first corpus appearance this run" in a["url_novelty"]

    def test_times_powerful_url_verbatim_and_attribution(self):
        urls = [a.get("url") for a in _mechanism()["articles"]]
        assert TIMES_POWERFUL_URL in urls
        arts = _mechanism()["articles"]
        a = [x for x in arts if x.get("url") == TIMES_POWERFUL_URL][0]
        assert "The story was reported by the Financial Times" in a["attestation_excerpt"]
        assert "first corpus appearance this run" in a["url_novelty"]

    def test_lse_pmqs_url_verbatim(self):
        urls = [a.get("url") for a in _mechanism()["articles"]]
        assert LSE_PMQs_URL in urls
        arts = _mechanism()["articles"]
        a = [x for x in arts if x.get("url") == LSE_PMQs_URL][0]
        assert "Financial Times reported" in a["attestation_excerpt"]
        assert "PMQs" in a["register"]

    def test_brieftea_url_verbatim(self):
        urls = [a.get("url") for a in _mechanism()["articles"]]
        assert BRIEFTEA_URL in urls

    def test_aiinsider_url_verbatim(self):
        urls = [a.get("url") for a in _mechanism()["articles"]]
        assert AIINSIDER_URL in urls
        arts = _mechanism()["articles"]
        a = [x for x in arts if x.get("url") == AIINSIDER_URL][0]
        assert "Financial Times separately reported" in a["attestation_excerpt"]

    def test_five_attestation_urls_new_to_corpus(self):
        arts = _mechanism()["articles"]
        a = [x for x in arts if x.get("attestation_url") == TIMES_GAMBLING_URL][0]
        assert "five attestation snippets" in a["evidence_grade"]
        assert "Five attestation URLs carried verbatim" in _mechanism()["research_method"]
        assert "all five URLs repo-wide-grep verified new to corpus" in _mechanism()["research_method"]

    def test_eight_articles_total(self):
        assert len(_mechanism()["articles"]) == 8


class TestMetaOpenAIComparators:
    def test_meta_muse_url_verbatim(self):
        urls = [a.get("url") for a in _mechanism()["articles"]]
        assert META_MUSE_URL in urls

    def test_meta_muse_carried_from_625(self):
        arts = _mechanism()["articles"]
        a = [x for x in arts if x.get("url") == META_MUSE_URL][0]
        assert a["manual_illustrative_tone"] == 0.05
        assert "product_distribution_factual" in a["register"]
        assert "mechanism 625" in a["evidence_grade"]

    def test_openai_astra_url_verbatim(self):
        urls = [a.get("ft_attribution_mirror_1_url") for a in _mechanism()["articles"]]
        assert OPENAI_ASTRA_URL in urls

    def test_openai_astra_coronation_carried_from_625(self):
        arts = _mechanism()["articles"]
        a = [x for x in arts if x.get("ft_attribution_mirror_1_url") == OPENAI_ASTRA_URL][0]
        assert a["manual_illustrative_tone"] == 0.25
        assert "epochal_coronation" in a["register"]

    def test_eu_dma_url_verbatim(self):
        urls = [a.get("url") for a in _mechanism()["articles"]]
        assert EU_DMA_URL in urls

    def test_openai_accountability_absence_bounded(self):
        f = _mechanism()["finding"]
        assert "bounded search-result absence" in f
        assert "iteration-492 rule" in f
        assert "not a proven zero" in f


class TestScorer:
    def test_arrays(self):
        r = _mechanism()["asymmetry_scorer_result"]
        assert r["target_entity"] == "anthropic"
        assert r["target_tones_manual_illustrative"] == [-0.45]
        assert r["peer_entities"] == ["meta"]
        assert r["peer_tones_manual_illustrative"] == [0.05]

    def test_arithmetic(self):
        r = _mechanism()["asymmetry_scorer_result"]
        assert abs(r["target_avg"] - (-0.45)) < 1e-9
        assert abs(r["peer_avg"] - 0.05) < 1e-9
        assert abs(r["delta_meta_minus_anthropic"] - 0.5) < 1e-9

    def test_manual_illustrative_guards(self):
        r = _mechanism()["asymmetry_scorer_result"]
        assert r["p_value"] == "NOT_CALCULATED"
        assert r["cohens_d"] == "NOT_CALCULATED"
        assert r["ci"] == "NOT_CALCULATED"
        assert r["is_significant"] is False
        assert r["artifact_grade"] is False

    def test_finding_layer_not_significant(self):
        assert _mechanism()["asymmetry_scorer_result"]["is_significant"] is False
        assert "is_significant false" in _mechanism()["finding"]

    def test_limitations_stated(self):
        r = _mechanism()["asymmetry_scorer_result"]
        assert "n=1" in r["limitations"]
        assert "no engine run" in r["limitations"]
        assert "degenerate statistical contract" in r["limitations"]


class TestConfoundersAndCounterargument:
    def test_confounders_present(self):
        confs = _mechanism()["confounders"]
        assert len(confs) >= 6
        blob = " ".join(confs)
        assert "news-value gap" in blob
        assert "mirror attestation" in blob
        assert "lane asymmetry" in blob
        assert "iteration-492 rule" in blob

    def test_strongest_counterargument_scope_bound(self):
        ca = _mechanism()["strongest_counterargument"]
        assert "fundraising/aspirational" in ca
        assert "scope-bounded" in ca
        assert "MANUAL ILLUSTRATIVE" in ca
        assert "correlation-only" in ca

    def test_financial_context_prediction_fails(self):
        fc = _mechanism()["financial_context"]
        assert "FAILS" in fc
        assert "$0 direct Anthropic deal" in fc
        assert "softer via Google channel" in fc

    def test_falsification_family_fifteenth(self):
        ff = _mechanism()["falsification_family"]
        assert "FIFTEENTH falsification-family member" in ff
        assert "mechanism 634" in ff
        assert "#675 verified no FIFTEENTH" in ff
        assert "Correlation is not causation" in ff

    def test_cross_references(self):
        assert _mechanism()["cross_references"] == [441, 625, 634]

    def test_novelty_distinct_from_prior(self):
        nov = _mechanism()["novelty"]
        assert "mechanism 441" in nov
        assert "mechanism 625" in nov
        assert "FIFTEENTH falsification-family member" in nov
        assert "mechanism_643" in nov


class TestIterationLog682:
    def test_log_starts_with_682(self):
        text = _read(LOG)
        assert text.startswith("#682 Type A")

    def test_log_entry_relative_order(self):
        text = _read(LOG)
        m682 = re.search(r"^#682\b", text, re.MULTILINE)
        m681 = re.search(r"^#681\b", text, re.MULTILINE)
        assert m682 is not None and m681 is not None
        assert m682.start() < m681.start()

    def test_log_entry_content(self):
        text = _read(LOG)
        start = text.index("#682 Type A")
        end = text.index("#681 Type E")
        block = text[start:end]
        assert "FT x Anthropic" in block
        assert "+0.50" in block
        assert "mechanism 643" in block
        assert "FIFTEENTH falsification-family" in block
        assert "NOT artifact-grade" in block


class TestRotationCycleGuard682:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #682 main-commit SHA is known.
    ANCHORED_SHA = "c24ee448ae5e10f20afef3f5ba9063193cdfda4c"

    @staticmethod
    def _mains():
        out = _run_git("log", "--format=%s")
        assert out.returncode == 0
        return [
            s for s in out.stdout.splitlines()
            if re.match(r"^Type [A-E] #\d+:", s)
        ]

    def test_window_678_682_closes_b_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "682"),
            ("E", "681"),
            ("D", "680"),
            ("C", "679"),
            ("B", "678"),
        ], "rotation window 678-682 wrong: %r" % (observed,)

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
            line for line in result.stdout.splitlines() if "Type A #682:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync682:
    # Fails pre-commit by design per the #565 followup convention; the README
    # stats table refresh, narrative line, test-file table row, and
    # ARCHITECTURE row land in the doc-sync commit.
    def _readme_stats(self):
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        m = re.search(r"\| Tests \| (\d+) \| Across (\d+) test files \|", text)
        assert m, "README stats table row not found"
        return int(m.group(1)), int(m.group(2))

    def _actual_counts(self):
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
        text = _read(os.path.join(REPO_ROOT, "README.md"))
        m = re.search(r"has \*\*(\d+) tests\*\* across (\d+) test files", text)
        assert m, "README narrative test-count line not found"
        total, files = self._actual_counts()
        assert (int(m.group(1)), int(m.group(2))) == (total, files)

    def test_architecture_row_present(self):
        text = _read(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md"))
        assert "test_type_a_682" in text
