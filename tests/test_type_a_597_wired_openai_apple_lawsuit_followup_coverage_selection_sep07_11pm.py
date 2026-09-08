"""Type A #597 (2026-09-07 23:00 PDT): WIRED x OpenAI Apple-lawsuit followup
coverage-selection.

WIRED published exactly 1 article on the Apple v. OpenAI hardware
trade-secrets case (Jul 10 2026, Maxwell Zeff, the accusation phase). Across
the next 59 days the case escalated through 5 more beats, all carrying
OpenAI's counter-narrative, and 3 bounded search-result sets this run surfaced
zero WIRED articles on any of them: Jul 14 OpenAI public response; Aug 3
Apple preliminary-injunction + expedited-discovery bid with OpenAI's "based on
false information and completely unnecessary" blog-post rebuttal; Aug 6 OpenAI
motion to dismiss calling the allegations "meritless"; Aug 31 Apple's new
forensic-evidence filing on Liu's MacBook; Sep 1 OpenAI's "this dispute is a
mess of Apple's own making" filing, which Reuters, WSJ, MacRumors, Bloomberg
Law, 9to5Mac, TechRepublic and Outlook Business all treated as a beat worth
covering.

The accusation gets covered; the defendant's rebuttals do not. This is the
coverage-selection form of the Condé Nast x OpenAI licensing prediction
(#504), distinct from the tone-form finding in the pre-existing
apple_v_openai_silence block (Aug 28 correction). Illustrative delta +0.5733
(OpenAI target -0.2 minus Meta peer -0.773), MANUAL ILLUSTRATIVE n.s.,
standing rule Aug 28 2026. Mechanism_id 591, the next free numeric id.

Durable conventions (from #495): line-anchored (^, re.MULTILINE) heading
search in iteration-log.md; relative newest-first ordering between neighbors,
never absolute-top or fixed head slices. Rotation-guard class deselected
pre-commit per the #565 followup convention; anchor patched in the followup.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, "profiles", "wired.yaml")
LOG = os.path.join(REPO, "iteration-log.md")

MECH_KEY = "mechanism_591_wired_openai_apple_lawsuit_followup_coverage_selection_sep07"

ZEFF_URL = "https://www.wired.com/story/apple-sues-openai-allegedly-stealing-ip-hardware/"
REUTERS_SEP1 = "https://www.reuters.com/legal/litigation/openai-says-apple-has-only-itself-blame-trade-secret-fight-2026-09-01/"
WSJ_SEP1 = "https://www.wsj.com/tech/openai-hits-back-at-apple-lawsuit-claiming-it-stole-trade-secrets-c0d34f44"
MACRUMORS_SEP1 = "https://www.macrumors.com/2026/09/01/dispute-said-to-be-mess-of-apples-own-making/"
MACRUMORS_DISMISS = "https://www.macrumors.com/2026/08/06/openai-asks-judge-to-dismiss-apple-lawsuit/"
MACRUMORS_REBUTTAL = "https://www.macrumors.com/2026/08/04/openai-posts-public-rebuttal-to-apple/"
MACRUMORS_RESPONSE = "https://www.macrumors.com/2026/07/14/openai-apple-lawsuit-response/"
BLOOMBERGLAW_EVIDENCE = "https://news.bloomberglaw.com/artificial-intelligence/apple-says-openai-is-destroying-evidence-in-trade-secrets-case"
NINE5MAC_SEP1 = "https://9to5mac.com/2026/09/01/openai-calls-trade-secret-dispute-a-mess-of-apples-own-making/"
TECHREPUBLIC_SEP1 = "https://www.techrepublic.com/article/news-apple-openai-macbook-evidence-trade-secrets/"
OUTLOOK_SEP1 = "https://www.outlookbusiness.com/corporate/openai-vs-apple-trade-secret-theft-lawsuit-proceedings-employee-exits-hardware-design-manufacturing-data"
WIXX_INJUNCTION = "https://wixx.com/2026/08/04/apple-seeks-preliminary-injunction-against-openai-in-trade-secrets-case/"
APPLEINSIDER_INJUNCTION = "https://appleinsider.com/articles/26/08/04/apple-demands-openai-injunction-discovery-testimony-now-to-prevent-more-harm"

PEER_URLS = (REUTERS_SEP1, WSJ_SEP1, MACRUMORS_SEP1, MACRUMORS_DISMISS,
             MACRUMORS_REBUTTAL, MACRUMORS_RESPONSE, BLOOMBERGLAW_EVIDENCE,
             NINE5MAC_SEP1, TECHREPUBLIC_SEP1, OUTLOOK_SEP1, WIXX_INJUNCTION,
             APPLEINSIDER_INJUNCTION)

FOLLOWUP_DATES = ("2026-07-14", "2026-08-03", "2026-08-06", "2026-08-31",
                  "2026-09-01")


def _mechanism():
    with open(PROFILE) as f:
        doc = yaml.safe_load(f)
    return doc["competitor_relationships"]["openai"][MECH_KEY]


def _mechanism_block_text():
    with open(PROFILE) as f:
        text = f.read()
    start = text.index(MECH_KEY)
    end = text.index("\n  meta:", start)
    return text[start:end]


def _segment(log_text, num):
    """Return the text of iteration #num's log entry (heading to next heading)."""
    headings = [(m.start(), m.group(1)) for m in re.finditer(r"^#(\d+) Type [A-E]:", log_text, re.M)]
    starts = [pos for pos, n in headings if n == str(num)]
    assert starts, f"#{num} heading not found"
    start = starts[0]
    later = [pos for pos, _ in headings if pos > start]
    end = min(later) if later else len(log_text)
    return log_text[start:end]


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_openai(self):
        with open(PROFILE) as f:
            doc = yaml.safe_load(f)
        assert MECH_KEY in doc["competitor_relationships"]["openai"]

    def test_identity_fields(self):
        m = _mechanism()
        assert m["mechanism_id"] == 591
        assert m["iteration"] == 597
        assert m["iteration_type"] == "A"
        assert m["date"] == "2026-09-07"
        assert m["iteration_time"] == "2026-09-07 23:00 PDT"

    def test_publication_pair_and_comparators(self):
        m = _mechanism()
        assert m["publication_pair"] == "WIRED x OpenAI"
        assert m["competitor"] == "openai"
        assert "meta" in m["comparison_entities"]
        assert "apple" in m["comparison_entities"]

    def test_openai_entity_block_predates_mechanism(self):
        with open(PROFILE) as f:
            doc = yaml.safe_load(f)
        o = doc["competitor_relationships"]["openai"]
        assert o["financial_tie"] == "licensing"
        assert o["coverage_prediction"] == "softer"

    def test_author_kit_with_ray(self):
        assert _mechanism()["author"] == "Kit (with Ray)"

    def test_financial_verdict_consistent(self):
        assert _mechanism()["financial_context"]["verdict"].startswith("CONSISTENT")

    def test_no_em_dashes_in_block(self):
        assert "\u2014" not in _mechanism_block_text()

    def test_block_is_ascii(self):
        _mechanism_block_text().encode("ascii")


class TestOpenAIArticles:
    def test_seven_article_records(self):
        assert len(_mechanism()["articles"]) == 7

    def test_scored_zeff_article(self):
        arts = _mechanism()["articles"]
        zeff = [a for a in arts if a["author"] == "Maxwell Zeff"][0]
        assert zeff["url"] == ZEFF_URL
        assert zeff["date"] == "2026-07-10"
        assert zeff["manual_illustrative_tone"] == -0.2
        assert zeff["evidence_tier"] == "in_corpus_carried_secondary"

    def test_zeff_tone_is_relay_characterized(self):
        arts = _mechanism()["articles"]
        zeff = [a for a in arts if a["author"] == "Maxwell Zeff"][0]
        assert "relay" in zeff["verification"].lower()

    def test_five_followup_beats_bounded_absence(self):
        arts = _mechanism()["articles"]
        followups = [a for a in arts if a["evidence_tier"] == "bounded_search_absence"]
        assert len(followups) == 5
        for a in followups:
            assert a["url"] is None
            assert a["manual_illustrative_tone"] is None

    def test_followup_dates_complete(self):
        arts = _mechanism()["articles"]
        dates = {a["date"] for a in arts if a["evidence_tier"] == "bounded_search_absence"}
        assert dates == set(FOLLOWUP_DATES)

    def test_followup_verification_cites_peer_urls(self):
        arts = _mechanism()["articles"]
        followups = [a for a in arts if a["evidence_tier"] == "bounded_search_absence"]
        for a in followups:
            assert "http" in a["verification"]

    def test_meta_comparator_carried_from_547(self):
        arts = _mechanism()["articles"]
        meta = [a for a in arts if a["entity"] == "meta"][0]
        assert "547" in meta["title"] or "547" in meta["verification"]
        assert "Creep" in " ".join(meta["key_phrases"])

    def test_no_zero_coverage_claim_language(self):
        for a in _mechanism()["articles"]:
            if a["evidence_tier"] == "bounded_search_absence":
                assert "bounded" in a["register"]
        finding_lower = _mechanism()["finding"].lower()
        assert "zero wired articles" in finding_lower


class TestPeerCoverageControls:
    def test_seven_outlets_on_sep1_beat(self):
        m = _mechanism()
        sep1 = [a for a in m["articles"] if a["date"] == "2026-09-01"][0]
        assert "Reuters" in " ".join(sep1["key_phrases"])
        assert REUTERS_SEP1 in sep1["verification"]
        assert WSJ_SEP1 in sep1["verification"]

    def test_peer_urls_in_source_urls(self):
        srcs = _mechanism()["source_urls"]
        for u in PEER_URLS:
            assert u in srcs, f"peer URL missing from source_urls: {u}"

    def test_wsj_rebuttal_control_in_finding(self):
        finding = _mechanism()["finding"]
        assert "WSJ" in finding
        assert "Hits Back" in finding

    def test_distinct_from_cites_predecessors(self):
        df = " ".join(_mechanism()["distinct_from"])
        assert "apple_v_openai_silence" in df
        assert "356" in df
        assert "547" in df
        assert "532" in df

    def test_cross_references_in_finding(self):
        finding = _mechanism()["finding"]
        for ref in ("504", "547", "532", "356"):
            assert ref in finding, f"missing cross-ref {ref}"


class TestAsymmetryScorerArithmetic:
    def test_delta_openai_minus_meta(self):
        sc = _mechanism()["asymmetry_scorer_result"]
        assert abs(sc["delta_openai_minus_meta"] - 0.5733) < 0.0001

    def test_delta_reproduces_logged_arrays(self):
        sc = _mechanism()["asymmetry_scorer_result"]
        openai_avg = sum(sc["openai_target_scores"]) / len(sc["openai_target_scores"])
        meta_avg = sum(sc["meta_peer_scores"]) / len(sc["meta_peer_scores"])
        assert abs(openai_avg - sc["openai_target_avg"]) < 0.0001
        assert abs(meta_avg - sc["meta_peer_avg"]) < 0.0001
        assert abs((openai_avg - meta_avg) - sc["delta_openai_minus_meta"]) < 0.0001

    def test_standing_rule_discipline(self):
        sc = _mechanism()["asymmetry_scorer_result"]
        assert sc["p_value"] == "NOT_CALCULATED"
        assert sc["cohens_d"] == "NOT_CALCULATED"
        assert sc["ci_95"] == "NOT_CALCULATED"
        assert sc["is_significant"] is False

    def test_n_thin_documented(self):
        sc = _mechanism()["asymmetry_scorer_result"]
        assert sc["openai_n"] == 1
        assert sc["meta_n"] == 3
        assert "n=1" in sc["note"]

    def test_meta_scores_match_547_baseline(self):
        sc = _mechanism()["asymmetry_scorer_result"]
        assert sc["meta_peer_scores"] == [-0.82, -0.72, -0.78]

    def test_manual_illustrative_method(self):
        sc = _mechanism()["asymmetry_scorer_result"]
        assert "MANUAL ILLUSTRATIVE" in sc["method"]


class TestStatisticalDiscipline:
    def test_discipline_block_names_bounded_absence(self):
        sd = _mechanism()["statistical_discipline"]
        assert "bounded search-result absence" in sd

    def test_discipline_not_empirical(self):
        sd = _mechanism()["statistical_discipline"]
        assert "no empirical" in sd.lower() or "NOT empirical" in sd

    def test_discipline_correlation_not_causation(self):
        sd = _mechanism()["statistical_discipline"]
        assert "Correlation is not causation" in sd


class TestConfoundersRanked:
    def test_five_confounders(self):
        assert len(_mechanism()["confounders"]) == 5

    def test_strong_confounder_first(self):
        confs = _mechanism()["confounders"]
        assert confs[0]["strength"] == "STRONG"
        assert "Litigation-news norms" in confs[0]["text"]

    def test_bounded_absence_confounder_present(self):
        texts = " ".join(c["text"] for c in _mechanism()["confounders"])
        assert "bounded search-result absences" in texts

    def test_four_counterevidence_items(self):
        assert len(_mechanism()["counter_evidence"]) == 4

    def test_counterevidence_includes_wsj_falsification_note(self):
        ce = " ".join(_mechanism()["counter_evidence"])
        assert "WSJ" in ce
        assert "mechanically suppress" in ce

    def test_counterevidence_includes_accusation_coverage(self):
        ce = " ".join(_mechanism()["counter_evidence"])
        assert "Jul 10" in ce


class TestNovelty:
    def test_novelty_block_documents_precommit_greps(self):
        nv = _mechanism()["novelty_verification"]
        assert "mechanism_591" in nv
        assert "590" in nv

    def test_research_method_names_iteration_492_rule(self):
        assert "iteration-492" in _mechanism()["research_method"]

    def test_research_method_notes_wired_block(self):
        assert "policy-blocked" in _mechanism()["research_method"]

    def test_research_method_weekday_grounding(self):
        assert "date -d" in _mechanism()["research_method"]

    def test_no_constructed_urls_in_research_method(self):
        assert "no" in _mechanism()["research_method"].lower()
        assert "constructed" in _mechanism()["research_method"]


class TestIterationLogEntry:
    def test_597_heading_present(self):
        with open(LOG) as f:
            text = f.read()
        seg = _segment(text, 597)
        assert "WIRED x OpenAI" in seg

    def test_rotation_transparency(self):
        with open(LOG) as f:
            text = f.read()
        seg = _segment(text, 597)
        assert "596 E -> 597 A" in seg

    def test_log_entry_names_mechanism(self):
        with open(LOG) as f:
            text = f.read()
        seg = _segment(text, 597)
        assert "mechanism_591" in seg

    def test_log_entry_names_delta(self):
        with open(LOG) as f:
            text = f.read()
        seg = _segment(text, 597)
        assert "0.5733" in seg


class TestNoBrittle:
    def test_all_source_urls_start_https(self):
        for u in _mechanism()["source_urls"]:
            assert u.startswith("https://"), f"non-https URL: {u}"

    def test_zeff_url_in_source_urls(self):
        assert ZEFF_URL in _mechanism()["source_urls"]

    def test_no_duplicate_article_dates_on_openai_side(self):
        dates = [a["date"] for a in _mechanism()["articles"] if a["entity"] == "openai"]
        assert len(dates) == len(set(dates))


# POST_COMMIT_ANCHOR placeholder (guard class deselected pre-commit);
# anchor patched in the followup commit per the #565 convention.
class TestRotationCycleGuard597:
    ANCHORED_COMMIT = "POST_COMMIT_ANCHOR"

    MAIN_COMMIT_PATTERN = re.compile(r"^Type [A-E] #\d+:")

    @staticmethod
    def _git_main_subjects(n=5):
        out = subprocess.run(
            ["git", "-C", str(REPO), "log", "-n40",
             TestRotationCycleGuard597.ANCHORED_COMMIT, "--format=%s"],
            capture_output=True, text=True, check=True)
        mains = [s for s in out.stdout.splitlines()
                 if TestRotationCycleGuard597.MAIN_COMMIT_PATTERN.match(s)]
        return mains[:n]

    def test_git_commit_order_matches_rotation(self):
        subjects = self._git_main_subjects()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#597", "A"),
            ("#596", "E"),
            ("#595", "D"),
            ("#594", "C"),
            ("#593", "B"),
        ]
        for i, (num, typ) in enumerate(expected):
            assert num in subjects[i], \
                f"position {i}: expected {num}, got {subjects[i]!r}"
            assert re.search(rf"Type {typ} {re.escape(num)}", subjects[i]), \
                f"position {i}: expected Type {typ} {num}, got {subjects[i]!r}"

    def test_rotation_adjacency_cycle_valid(self):
        # A->E is the edge this run closes; the full 5-window must be a
        # rotation walk in commit-newest-first order: A,E,D,C,B (the
        # rotation runs backward in newest-first order). (order[a] -
        # order[b]) % 5 == 1 steps one position backward from the newer
        # commit a to the older commit b, i.e. one rotation step forward.
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        subjects = self._git_main_subjects()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #\d+", s)
            assert m, f"could not parse type from {s!r}"
            observed.append(m.group(1))
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, \
                f"rotation edge {a}->{b} invalid in window {observed}"
