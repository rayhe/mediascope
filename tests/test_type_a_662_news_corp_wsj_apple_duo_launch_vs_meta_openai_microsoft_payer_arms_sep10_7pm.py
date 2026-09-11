"""Type A #662: News Corp (WSJ) x Apple Duo launch-event celebration register
vs Meta/OpenAI/Microsoft licensing-payer comparator arms (mechanism 631).

FIRST dedicated Type A mechanism under news-corp.yaml
competitor_relationships.apple. The Apple arm is NEW evidence this run:
the WSJ's Sep 9 2026 foldable-iPhone-Duo launch piece ("Apple Debuts New
Foldable iPhone Duo, New CEO and New (Higher) Prices", URL verbatim from
the browser.search Full-URLs listing) carries a launch-celebration register
moderated by a consumer-harm price thread ("most consequential product
event in years", "most significant Apple device in a decade", "Ternus may
spark a new wave of innovation", against "the bad news for consumers was
that Apple increased iPhone prices... to protect its profit margins").
+0.45 MANUAL ILLUSTRATIVE, excerpt_bounded: browser.open to wsj.com was
blocked by policy this run (terminal per developer instruction, not a
paywall claim), so no first-hand WSJ read and no byline attestation.

Comparator arms carried from #632/#637 with evidence tiers intact:
Meta +0.35 avg (Bobrowsky Sep 8 +0.40 aspirational launch feature,
first-hand; Mizuho Market Talk roundup Sep 9 +0.30, snippet-bounded);
OpenAI -0.225 avg (Tumbler Ridge liability watchdog -0.55, first-hand;
copyright news +0.10, snippet-bounded); Microsoft -0.35 avg
(reporting-structure straight report 0.00 Sep 2, first-hand; Heard
black-box analysis -0.70 Sep 3, first-hand).

Scorer MANUAL ILLUSTRATIVE: illustrative delta (Apple minus Meta) +0.10;
four-arm ledger apple +0.45 > meta +0.35 > openai -0.225 > microsoft -0.35.
n=1 vs n=2 arms: degenerate statistical contract (p=1.0, d=0.0); engine NOT
run, no divergence pin. No empirical significance claimed or computed.

Financial context: predictor licensing_payer_softer predicts payers get
softer coverage than zero-deal entities. OpenAI $50M/yr (May 22 2024
$250M/5yr, ACTIVE per #654), Meta up to $50M/yr Dow Jones news leg
(#549), Microsoft HarperCollins book leg (#524); Apple $0 AI-licensing on
record (bounded absence per #659; Thomson Oct 21 2025
partnerships-with-OpenAI/Apple quote ambiguous). Status CONTRADICTED on
the matched-launch-genre boundary: the $0 entity gets the softest register.
TWELFTH falsification-family member (after #625's eleventh; #632 and #637
partial members only). STRONG genre/event confounds bound the claim.
Correlation only, not causation.

Counterevidence preserved: the Apple price thread itself, the mechanism-206
WSJ Apple camera-AirPods selection-silence precedent, and the documented
reality of the licensing deals (falsification is genre-bounded).

Rotation: Type A follows Type E (#661) per A,B,C,D,E. Rotation guard
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
PROFILE_PATH = os.path.join(REPO_ROOT, "profiles", "news-corp.yaml")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "wsj_apple_duo_launch_register_vs_payer_arms_sep10"

WSJ_APPLE_DUO_URL = (
    "https://www.wsj.com/tech/"
    "apple-to-debut-new-foldable-iphone-new-ceo-and-new-prices-b2485b9f"
)
REUTERS_LAUNCH_URL = (
    "https://www.reuters.com/business/retail-consumer/"
    "apple-expected-unveil-first-folding-phone-with-new-ceo-ternus-"
    "command-2026-09-09/"
)
REUTERS_1999_URL = (
    "https://www.reuters.com/business/retail-consumer/"
    "apples-foldable-iphone-poses-1999-question-who-is-it-2026-09-10/"
)
REUTERS_PREVIEW_URL = (
    "https://www.reuters.com/technology/"
    "apple-sets-sept-9-date-next-iphone-launch-event-2026-08-26/"
)
WSJ_META_MUSE_URL = (
    "https://www.wsj.com/tech/ai/"
    "meta-launches-a-personal-ai-agent-designed-to-be-easy-to-use-3eb5cfac"
)
WSJ_META_ROUNDUP_URL = (
    "https://www.wsj.com/business/"
    "tech-media-telecom-roundup-market-talk-1307ac74"
)
WSJ_MSFT_REPORTING_URL = (
    "https://www.wsj.com/tech/ai/"
    "microsoft-to-change-reporting-structure-to-reflect-effects-of-ai-59dce66d"
)

TARGET_SCORES = [0.45]
META_PEER_SCORES = [0.40, 0.30]
OPENAI_PEER_SCORES = [-0.55, 0.10]
MICROSOFT_PEER_SCORES = [0.00, -0.70]
TARGET_AVG = 0.45
META_AVG = 0.35
OPENAI_AVG = -0.225
MICROSOFT_AVG = -0.35
EXPECTED_DELTA = 0.10


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
    return _profile()["competitor_relationships"]["apple"]


def _mechanism():
    return _entity()[MECH_KEY]


def _read(path):
    with open(os.path.join(REPO_ROOT, path)) as fh:
        return fh.read()


class TestIterationMetadata662:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 662

    def test_type_a(self):
        assert _mechanism()["iteration_type"] == "A"

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 631

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
        assert ids.count(631) == 1
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

    def test_pair_names_apple_vs_payer_arms(self):
        assert "Apple" in _mechanism()["pair"]
        assert "Meta" in _mechanism()["pair"]

    def test_iteration_time_sep10_7pm(self):
        assert _mechanism()["iteration_time"] == "2026-09-10 19:00 PDT"

    def test_author_kit_with_ray(self):
        assert _mechanism()["author"] == "Kit (with Ray)"


class TestAppleEntityStructure662:
    def test_entity_financial_tie_distribution(self):
        entity = _entity()
        assert entity["financial_tie"] == "distribution"

    def test_entity_value_undisclosed(self):
        entity = _entity()
        assert entity["estimated_value"] == "undisclosed"
        assert entity["direction"] == "receiving"

    def test_entity_description_apple_news_plus(self):
        entity = _entity()
        assert "Apple News+" in entity["description"]

    def test_entity_coverage_prediction_neutral(self):
        assert _entity()["coverage_prediction"] == "neutral"

    def test_mechanism_nested_under_apple(self):
        assert MECH_KEY in _entity()
        assert _mechanism()["mechanism_id"] == 631

    def test_sibling_mechanism_206_intact(self):
        cam = _entity()["camera_wearables_coverage_selection_silence"]
        assert cam["mechanism_id"] == 206


class TestToneScorer662:
    def test_target_scores(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert m["target_scores_MANUAL_ILLUSTRATIVE"] == TARGET_SCORES

    def test_meta_peer_scores(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert m["meta_peer_scores_MANUAL_ILLUSTRATIVE"] == META_PEER_SCORES

    def test_openai_peer_scores(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert m["openai_peer_scores_MANUAL_ILLUSTRATIVE"] == OPENAI_PEER_SCORES

    def test_microsoft_peer_scores(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert m["microsoft_peer_scores_MANUAL_ILLUSTRATIVE"] == MICROSOFT_PEER_SCORES

    def test_delta_calc(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert m["delta_manual_illustrative"] == pytest.approx(EXPECTED_DELTA)
        assert m["target_avg"] - m["meta_peer_avg"] == pytest.approx(EXPECTED_DELTA)

    def test_four_arm_ledger_ordering(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        avgs = {
            "apple": m["target_avg"],
            "meta": m["meta_peer_avg"],
            "openai": m["openai_peer_avg"],
            "microsoft": m["microsoft_peer_avg"],
        }
        assert avgs == {
            "apple": pytest.approx(0.45),
            "meta": pytest.approx(0.35),
            "openai": pytest.approx(-0.225),
            "microsoft": pytest.approx(-0.35),
        }
        ordered = sorted(avgs, key=avgs.get, reverse=True)
        assert ordered == ["apple", "meta", "openai", "microsoft"]
        assert "apple +0.45 > meta +0.35 > openai -0.225 > microsoft -0.35" in m[
            "four_arm_ledger"
        ]

    def test_article_tones_match_scorer_arms(self):
        mech = _mechanism()
        assert mech["apple_article"]["manual_illustrative_tone"] == TARGET_AVG
        meta_tones = [
            a["manual_illustrative_tone"]
            for a in mech["meta_comparator_arm"]["articles"]
        ]
        assert meta_tones == META_PEER_SCORES
        assert mech["meta_comparator_arm"]["avg_tone_manual_illustrative"] == pytest.approx(
            META_AVG
        )

    def test_degenerate_contract_documented(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "p=1.0, d=0.0" in m["engine_degenerate"]
        assert "NOT run" in m["engine_degenerate"]

    def test_finding_layer_refuses(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "NOT_CALCULATED" in m["finding_layer"]
        assert "is_significant False" in m["finding_layer"]
        assert m["is_significant"] is False
        assert m["p_value"].startswith("NOT_CALCULATED")

    def test_manual_illustrative_label_present(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "MANUAL ILLUSTRATIVE" in m["methodology"]
        assert "DO NOT claim empirical significance" in m["methodology"]

class TestRegisterAnalysis662:
    def test_apple_register_launch_celebration(self):
        art = _mechanism()["apple_article"]
        assert art["register"] == "launch_celebration_with_price_scrutiny"

    def test_apple_url_verbatim(self):
        art = _mechanism()["apple_article"]
        assert art["url"] == WSJ_APPLE_DUO_URL

    def test_apple_evidence_tier_excerpt_bounded(self):
        art = _mechanism()["apple_article"]
        assert art["evidence_tier"] == "excerpt_bounded"
        assert "BLOCKED BY POLICY" in _mechanism()["research_method"]

    def test_apple_byline_unattested(self):
        art = _mechanism()["apple_article"]
        assert "unattested" in art["byline"]

    def test_apple_price_thread_quoted(self):
        art = _mechanism()["apple_article"]
        joined = " ".join(art["price_thread_quotes"])
        assert "New (Higher) Prices" in joined
        assert "bad news for consumers" in joined
        assert "protect its profit margins" in joined

    def test_apple_framing_celebration_quotes(self):
        framing = _mechanism()["apple_article"]["framing"]
        assert "most consequential product event in years" in framing
        assert "most significant Apple device in a decade" in framing
        assert "spark a new wave of innovation" in framing

    def test_apple_corrorborating_reuters_urls(self):
        urls = _mechanism()["apple_article"]["corroborating_event_urls"]
        assert REUTERS_LAUNCH_URL in urls
        assert REUTERS_1999_URL in urls
        assert REUTERS_PREVIEW_URL in urls

    def test_apple_canonical_url_not_invented(self):
        art = _mechanism()["apple_article"]
        assert "not constructed" in art["canonical_url_note"]
        assert "Full-URLs listing" in art["canonical_url_note"]

    def test_meta_arm_carried_from_632(self):
        arm = _mechanism()["meta_comparator_arm"]
        assert arm["carried_from"] == "#632 / mechanism 613"
        assert arm["articles"][0]["byline"] == "Meghan Bobrowsky"
        assert arm["articles"][0]["url"] == WSJ_META_MUSE_URL
        assert arm["articles"][1]["url"] == WSJ_META_ROUNDUP_URL

    def test_openai_arm_carried_from_637(self):
        arm = _mechanism()["openai_comparator_arm"]
        assert arm["carried_from"] == "#637 / mechanism 616"
        assert arm["articles"][0]["register"] == "adversarial_liability_watchdog"
        assert arm["avg_tone_manual_illustrative"] == pytest.approx(OPENAI_AVG)

    def test_microsoft_arm_carried_from_632(self):
        arm = _mechanism()["microsoft_comparator_arm"]
        assert arm["carried_from"] == "#632 / mechanism 613"
        assert arm["articles"][0]["url"] == WSJ_MSFT_REPORTING_URL
        assert arm["avg_tone_manual_illustrative"] == pytest.approx(MICROSOFT_AVG)

    def test_all_register_urls_https(self):
        text = yaml.dump(_mechanism())
        urls = re.findall(r"https?://[^\s'\"]+", text)
        assert len(urls) >= 7
        for u in urls:
            assert u.startswith("https://"), u


class TestFinancialContext662:
    def test_predictor_licensing_payer_softer(self):
        fc = _mechanism()["financial_context"]
        assert fc["predictor"] == "licensing_payer_softer"
        assert "payers covered softer than zero-deal entities" in fc["prediction"]

    def test_chain_names_all_four_legs(self):
        chain = _mechanism()["financial_context"]["chain"]
        assert "$50M/yr" in chain
        assert "May 22 2024" in chain
        assert "up to $50M/yr" in chain
        assert "HarperCollins" in chain
        assert "$0 AI-licensing" in chain

    def test_chain_apple_bounded_absence(self):
        chain = _mechanism()["financial_context"]["chain"]
        assert "bounded absence per #659" in chain
        assert "ambiguous" in chain

    def test_status_contradicted_on_genre_boundary(self):
        status = _mechanism()["financial_context"]["status"]
        assert "CONTRADICTED" in status
        assert "matched-launch-genre boundary" in status
        assert "carried as context, not as gradient tests" in status

    def test_correlate_only(self):
        fc = _mechanism()["financial_context"]
        assert fc["correlate_only"] is True
        assert _mechanism()["correlation_not_causation"] is True

    def test_do_not_claim_guardrail(self):
        fc = _mechanism()["financial_context"]
        assert "DO NOT claim" in fc["do_not_claim"]

    def test_apple_news_plus_orthogonal(self):
        chain = _mechanism()["financial_context"]["chain"]
        assert "Apple News+" in chain
        assert "orthogonal" in chain


class TestConfounders662:
    def _confounders(self):
        return _mechanism()["confounders_ranked"]

    def test_three_strong_confounders(self):
        assert len(self._confounders()["strong"]) == 3

    def test_launch_genre_skew_strong(self):
        strong = " ".join(self._confounders()["strong"])
        assert "Launch-genre celebration skew" in strong

    def test_excerpt_bounded_strong(self):
        strong = " ".join(self._confounders()["strong"])
        assert "Excerpt-bounded Apple register" in strong

    def test_event_innovation_skew_strong(self):
        strong = " ".join(self._confounders()["strong"])
        assert "Event/innovation skew" in strong

    def test_three_moderate_confounders(self):
        assert len(self._confounders()["moderate"]) == 3

    def test_time_window_skew_moderate(self):
        moderate = " ".join(self._confounders()["moderate"])
        assert "Time-window skew" in moderate

    def test_evidence_tier_asymmetry_moderate(self):
        moderate = " ".join(self._confounders()["moderate"])
        assert "Evidence-tier asymmetry" in moderate

    def test_price_scrutiny_moderate(self):
        moderate = " ".join(self._confounders()["moderate"])
        assert "Price-scrutiny thread" in moderate

    def test_two_weak_confounders(self):
        assert len(self._confounders()["weak"]) == 2

    def test_n1_degenerate_weak(self):
        weak = " ".join(self._confounders()["weak"])
        assert "degenerate statistical contract" in weak

    def test_counterevidence_three_items(self):
        ce = _mechanism()["counterevidence"]
        assert len(ce) == 3

    def test_counterevidence_price_thread(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "bad news for consumers" in ce

    def test_counterevidence_mechanism_206_silence(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "mechanism 206" in ce
        assert "selection-silence" in ce

    def test_counterevidence_deals_real(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "genre-bounded" in ce

    def test_strongest_counterargument_genre(self):
        sca = _mechanism()["strongest_counterargument"]
        assert "genre confound" in sca
        assert "excerpt-bounded" in sca


class TestNovelty662:
    def test_zero_test_files_pre_commit(self):
        assert glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_a_662*")
        ) == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)]

    def test_type_a_662_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; the main
        # commit exists exactly once post-commit and its SHA matches the
        # rotation-guard anchor patched in the followup. Novelty was
        # verified pre-commit by shell greps (zero test_type_a_662 files,
        # no Type A #662 in git log, zero mechanism_631 keys, the WSJ Duo
        # URL new to corpus); this test pins that no duplicate #662 main
        # commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type A #662:", l)]
        assert len(mains) == 1, (
            "expected exactly one Type A #662 main commit, got: %r" % (mains,)
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard662.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)

    def test_distinct_from_apple_silence_mechanisms(self):
        xrefs = _mechanism()["cross_references"]
        assert any("mechanism 206" in x for x in xrefs)
        ce = " ".join(_mechanism()["counterevidence"])
        assert "mechanism 206" in ce
        assert "selection-silence" in ce

    def test_twelfth_falsification_family_member(self):
        finding = _mechanism()["finding"]
        assert "TWELFTH falsification-family member" in finding
        assert "after #625's eleventh" in finding
        assert "#632/#637 partial" in finding

    def test_sibling_arms_of_632_637(self):
        xrefs = _mechanism()["cross_references"]
        assert any("#632" in x for x in xrefs)
        assert any("#637" in x for x in xrefs)

    def test_no_662_mechanism_collision(self):
        # No other mechanism in news-corp.yaml is keyed for iteration 662.
        text = _read("profiles/news-corp.yaml")
        assert text.count("iteration: 662") == 1


class TestRotationCycleGuard662:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #662 main-commit SHA is known.
    ANCHORED_SHA = "9da82dce04f6cc477124fb640ff69a920453bdfb"  # patched in followup per #565 convention

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

    def test_window_658_662_closes_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "662"),
            ("E", "661"),
            ("D", "660"),
            ("C", "659"),
            ("B", "658"),
        ], "rotation window 658-662 wrong: %r" % (observed,)

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
            line for line in result.stdout.splitlines() if "Type A #662:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync662:
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
        assert "test_type_a_662" in text

    def test_iteration_log_entry_662(self):
        text = _read("iteration-log.md")
        assert "#662" in text


class TestNoBrittlePatterns662:
    def test_yaml_reparses_clean(self):
        _profile()

    def test_no_em_dash_in_mechanism(self):
        text = yaml.dump(_mechanism(), allow_unicode=False)
        assert "\\u2014" not in text
        assert "\u2014" not in text

    def test_no_em_dash_in_test_file(self):
        with open(os.path.join(REPO_ROOT, "tests", TEST_BASENAME)) as fh:
            assert "\u2014" not in fh.read()

    def test_all_urls_http_or_https(self):
        text = yaml.dump(_mechanism())
        urls = re.findall(r"https?://[^\s'\"]+", text)
        assert len(urls) >= 7
        for u in urls:
            assert u.startswith("https://"), u

    def test_research_method_documented(self):
        mech = _mechanism()
        assert "research_method" in yaml.dump(mech)
        assert "browser.search" in mech["research_method"]

    def test_no_wishlist_urls_invented(self):
        # Per the no-canonical-URL rule: the Apple arm carries only the
        # verbatim search-surfaced WSJ URL plus corroborating Reuters URLs;
        # the Meta/Microsoft comparator URLs are carried from #632 verbatim.
        text = yaml.dump(_mechanism())
        assert WSJ_APPLE_DUO_URL in text
        assert WSJ_META_MUSE_URL in text
        assert WSJ_MSFT_REPORTING_URL in text
