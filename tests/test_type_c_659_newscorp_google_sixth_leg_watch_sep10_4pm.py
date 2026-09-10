"""Type C #659: News Corp x Google AI licensing talks sixth-leg watch (Sep 2026 status)
- First dedicated corpus mapping of the potential SIXTH News Corp AI-revenue leg
  (Google). Digiday first-hand read this run (~Nov 2025, zero pre-commit corpus
  hits): News Corp scoping a multi-LLM licensing portfolio strategy beyond the
  May 2024 OpenAI deal; Google began AI licensing talks with publishers in
  summer 2025; News Corp looking at closer Google Gemini work since summer 2025;
  Thomson (Times Tech Summit, Oct 21 2025) described a partnership with Google
  plus "significant" partnerships with OpenAI and Apple; Sun publisher Dominic
  Carter: deals with OpenAI "or with Google and possibly others". NO signed
  News Corp x Google AI licensing deal in 3 bounded Sep 2026 query sets; the
  Press Gazette tracker (updated ~Sep 7 2026) and LLM Pulse deal map (updated
  Sep 7 2026) both list News Corp-OpenAI only. Sixth-leg status: TALKS
  DOCUMENTED, NO SIGNED DEAL, UNRESOLVED (bounded absence per iteration-492
  rule). Operationalizes the standing watch item from mechanism 627 (#654):
  Thomson's Aug 5 2026 Q4 FY2026 "advanced discussions with several other
  companies" line.

Extends mechanism 594 (News Corp five-leg AI revenue architecture, which has
no Google leg) with the first sixth-leg watch mechanism (mechanism 630, next
free; max numeric mechanism id pre-commit 629). Qualitative Type C mapping.
tone_scores NOT_SCORED; p_value, cohens_d, ci_95 NOT_CALCULATED (standing rule
Aug 28 2026). Correlational language only; no causal claim; no coverage-tone
claim. NOT a falsification-family member.

Rotation: Type C follows Type B (#658) per A,B,C,D,E. Rotation guard and
doc-sync classes deselected pre-commit per the #565 followup convention;
anchor patched in the followup commit once the main commit SHA is known.
"""

import ast
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTITIES_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
NEWSCORP_PATH = os.path.join(REPO_ROOT, "profiles", "news-corp.yaml")

MECH_KEY = "mechanism_630_news_corp_google_ai_licensing_talks_sixth_leg_watch_sep2026"
FILENAME = "test_type_c_659_newscorp_google_sixth_leg_watch_sep10_4pm.py"

ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"


def _find_all(o, key, hits):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key:
                hits.append(v)
            _find_all(v, key, hits)
    elif isinstance(o, list):
        for v in o:
            _find_all(v, key, hits)
    return hits


def _mechanism():
    with open(ENTITIES_PATH, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    hits = _find_all(data, MECH_KEY, [])
    assert len(hits) == 1, f"{MECH_KEY} occurs {len(hits)} times (want exactly 1)"
    return hits[0]


def _count_def_tests():
    path = os.path.join(TESTS_DIR, FILENAME)
    tree = ast.parse(open(path).read())
    return sum(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name.startswith("test_")
        for n in ast.walk(tree)
    )


def _read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def _block_text():
    text = _read(ENTITIES_PATH)
    start = text.index("    " + MECH_KEY + ":")
    rest = text[start + len("    " + MECH_KEY + ":"):]
    m = re.search(r"\n    mechanism_\d", rest)
    return rest[: m.start()] if m else rest


class TestIterationMetadata659:
    def test_mechanism_id_630(self):
        assert _mechanism()["mechanism_id"] == 630

    def test_iteration_659(self):
        assert _mechanism()["iteration"] == 659

    def test_type_c(self):
        m = _mechanism()
        assert m["rotation"] == "Type C"
        assert m["type"] == "financial_incentive_mapping"

    def test_date_time_pdt(self):
        m = _mechanism()
        assert m["date_analyzed"] == "2026-09-10"
        assert m["time_pdt"] == "16:00"

    def test_job_and_goal(self):
        m = _mechanism()
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_mechanism_name_mentions_news_corp(self):
        assert "News Corp" in _mechanism()["mechanism_name"]

    def test_mechanism_name_mentions_google(self):
        assert "Google" in _mechanism()["mechanism_name"]

    def test_mechanism_name_mentions_sixth_leg(self):
        assert "Sixth-Leg" in _mechanism()["mechanism_name"]

    def test_mechanism_name_mentions_digiday(self):
        assert "Digiday" in _mechanism()["mechanism_name"]

    def test_mechanism_name_no_signed_deal_claim(self):
        assert "No Signed Deal" in _mechanism()["mechanism_name"]


class TestMechanismPlacement630:
    def test_nested_under_entities_google(self):
        with open(ENTITIES_PATH, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        assert MECH_KEY in data["entities"]["google"]

    def test_sibling_mechanisms_same_parent(self):
        with open(ENTITIES_PATH, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        parent = data["entities"]["google"]
        assert "mechanism_529_canada_c18_google_100m_meta_zero_natural_experiment" in parent

    def test_no_em_dash_in_block(self):
        assert "\u2014" not in _block_text(), "em dash found in the mechanism_630 block"

    def test_ascii_quotes_only_in_block(self):
        assert "\u2019" not in _block_text()
        assert "\u201c" not in _block_text()
        assert "\u201d" not in _block_text()


class TestGoogleTalksLeg:
    def test_talks_window_summer_2025(self):
        assert "summer 2025" in _mechanism()["google_talks_leg"]["talks_window"]

    def test_first_documented_digiday_nov_2025(self):
        first = _mechanism()["google_talks_leg"]["first_documented"]
        assert "Digiday" in first
        assert "Nov 2025" in first

    def test_talks_cover_gemini(self):
        assert "Gemini" in _mechanism()["google_talks_leg"]["what_talks_cover"]

    def test_signed_deal_none(self):
        assert "NONE" in _mechanism()["google_talks_leg"]["signed_ai_licensing_deal"]

    def test_status_unresolved(self):
        assert _mechanism()["google_talks_leg"]["status"] == "UNRESOLVED"

    def test_existing_relationship_is_product_set(self):
        rel = _mechanism()["google_talks_leg"]["existing_relationship"]
        assert "Workspace" in rel
        assert "distinct from a signed AI licensing deal" in rel

    def test_overview_states_no_signed_deal(self):
        assert "NO signed News Corp x Google AI licensing deal" in _mechanism()["overview"]


class TestThomsonMultiLLMDoctrine:
    def test_woo_and_sue(self):
        assert "woo" in _mechanism()["thomson_multi_llm_doctrine"]["woo_and_sue"]

    def test_non_exclusivity(self):
        doc = _mechanism()["thomson_multi_llm_doctrine"]["non_exclusivity"]
        assert "non-exclusive by design" in doc
        assert "Gunderson Dettmer" in doc

    def test_pay_per_usage_shift(self):
        doc = _mechanism()["thomson_multi_llm_doctrine"]["pay_per_usage_shift"]
        assert "pay-per-usage" in doc
        assert "RAG" in doc

    def test_carter_quote(self):
        quote = _mechanism()["thomson_multi_llm_doctrine"]["carter_quote"]
        assert "Dominic Carter" in quote
        assert "with Google and possibly others" in quote

    def test_brave_callout(self):
        brave = _mechanism()["thomson_multi_llm_doctrine"]["brave_callout"]
        assert "Brave" in brave
        assert "shamelessly stealing content at scale" in brave

    def test_brave_corroboration_surface_named(self):
        brave = _mechanism()["thomson_multi_llm_doctrine"]["brave_callout"]
        assert "theregister.com" in brave
        assert "Aug 6 2026" in brave


class TestFiveLegContext:
    def test_mechanism_594(self):
        assert _mechanism()["five_leg_context"]["mechanism"] == 594

    def test_legs_mention_openai_value(self):
        assert "$250M/5yr" in _mechanism()["five_leg_context"]["legs"]

    def test_legs_mention_meta_value(self):
        assert "$50M/yr" in _mechanism()["five_leg_context"]["legs"]

    def test_google_would_be_sixth_leg(self):
        sixth = _mechanism()["five_leg_context"]["google_would_be"]
        assert "sixth leg" in sixth
        assert "search-platform counterparty" in sixth


class TestPerplexitySueLeg:
    def test_suit_oct_2024(self):
        assert "Oct 2024" in _mechanism()["perplexity_sue_leg_status"]["suit"]

    def test_dismissal_bid_rejected(self):
        assert "rejected Aug 2025" in _mechanism()["perplexity_sue_leg_status"]["dismissal_bid"]

    def test_no_perplexity_deal(self):
        assert "NONE" in _mechanism()["perplexity_sue_leg_status"]["deal"]


class TestQuerySetsAndAbsence:
    def test_three_query_sets(self):
        assert len(_mechanism()["query_sets"]) == 3

    def test_query_set_1_no_new_signed_deal(self):
        result = _mechanism()["query_sets"][0]["result"]
        assert "NO new signed deal announcement" in result

    def test_query_set_1_only_resurfaces(self):
        result = _mechanism()["query_sets"][0]["result"]
        assert "May 2024 OpenAI announcement re-surfaces" in result
        assert "Mar 2026 Meta leg" in result

    def test_query_set_2_thomson_quote_reconfirmed(self):
        result = _mechanism()["query_sets"][1]["result"]
        assert "Q4 FY2026 quote re-confirmed" in result
        assert "no new signed deal" in result

    def test_query_set_2_theregister_resurface(self):
        result = _mechanism()["query_sets"][1]["result"]
        assert "theregister.com Aug 6 2026 re-surface" in result
        assert "crawled 3d" in result

    def test_query_set_3_digiday_new_to_corpus(self):
        result = _mechanism()["query_sets"][2]["result"]
        assert "NEW TO CORPUS Digiday ~Nov 2025" in result
        assert "Google talks documented" in result

    def test_query_set_3_trackers_list_openai_only(self):
        result = _mechanism()["query_sets"][2]["result"]
        assert "Press Gazette tracker" in result
        assert "LLM Pulse deal map" in result
        assert "News Corp-OpenAI only" in result

    def test_bounded_absence_discipline(self):
        sd = _mechanism()["statistical_discipline"]
        assert "iteration-492 rule" in sd
        assert "no zero-coverage claims beyond the searches actually run" in sd


class TestConfoundersAndCounterevidence:
    def test_five_confounders(self):
        assert len(_mechanism()["ranked_confounders"]) == 5

    def test_strength_profile(self):
        strengths = [c["strength"] for c in _mechanism()["ranked_confounders"]]
        assert strengths == ["strong", "strong", "moderate", "moderate", "weak"]

    def test_ranks_sequential(self):
        assert [c["rank"] for c in _mechanism()["ranked_confounders"]] == [1, 2, 3, 4, 5]

    def test_strong_confounder_talks_not_revenue(self):
        confs = _mechanism()["ranked_confounders"]
        assert "Talks are not revenue" in confs[0]["confounder"]
        assert "no tone prediction attaches" in confs[0]["confounder"]

    def test_strong_confounder_partnership_ambiguity(self):
        confs = _mechanism()["ranked_confounders"]
        assert "ambiguous" in confs[1]["confounder"]
        assert "declining comment" in confs[1]["confounder"]

    def test_moderate_confounders(self):
        confs = _mechanism()["ranked_confounders"]
        assert "anonymous" in confs[2]["confounder"]
        assert "Nov 2023" in confs[3]["confounder"]
        assert "CEO salesmanship" in confs[3]["confounder"]

    def test_counterargument_ai_overviews_grievance(self):
        ca = _mechanism()["strongest_counterargument"]
        assert "AI Overviews" in ca
        assert "traffic-cannibalization grievance" in ca

    def test_counterargument_cma_designation(self):
        ca = _mechanism()["strongest_counterargument"]
        assert "CMA" in ca
        assert "strategic-market-status" in ca

    def test_cross_references(self):
        xrefs = " ".join(_mechanism()["cross_references"])
        for token in ("Mechanism 594", "Mechanism 627", "Mechanism 519", "Mechanism 549", "Mechanism 624", "Mechanism 529", "#609", "#654"):
            assert token in xrefs, f"cross-reference {token} missing"

    def test_statistical_discipline(self):
        sd = _mechanism()["statistical_discipline"]
        assert "p_value, cohens_d, ci_95 NOT_CALCULATED" in sd
        assert "tone_scores NOT_SCORED" in sd
        assert "NOT a falsification-family member" in sd


class TestNovelty659:
    def test_first_dedicated_google_talks_mapping(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "FIRST dedicated News Corp x Google AI-licensing-talks mapping" in nv

    def test_first_corpus_record_digiday_piece(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "FIRST corpus record of the Digiday ~Nov 2025" in nv
        assert "zero pre-commit hits" in nv

    def test_zero_630_keys_precommit(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "Zero mechanism_630 keys repo-wide pre-commit" in nv
        assert "max numeric mechanism id pre-commit 629" in nv

    def test_zero_test_type_c_659_files(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "Zero test_type_c_659 files on disk pre-commit" in nv

    def test_no_659_in_git_log_precommit(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "No Type C #659 in git log pre-commit" in nv

    def test_distinct_from_prior_mechanisms(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "mechanism 594" in nv
        assert "mechanism 627" in nv
        assert "mechanism 529" in nv

    def test_not_falsification_member(self):
        nv = " ".join(_mechanism()["novelty_verification"])
        assert "NOT a falsification-family member" in nv

    def test_source_urls_count_and_key_urls(self):
        urls = _mechanism()["source_urls"]
        assert len(urls) == 7
        joined = " ".join(urls)
        assert "https://digiday.com/media/news-corp-in-talks-with-google-for-ai-licensing-deal/" in joined
        assert "https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/" in joined
        assert "https://llmpulse.ai/blog/ai-content-licensing-deals/" in joined
        assert "https://www.theregister.com/ai-and-ml/2026/08/06/news-corp-labels-some-ai-companies-crass-kleptomaniacs/5283848" in joined

    def test_urls_verbatim_no_construction(self):
        for u in _mechanism()["source_urls"]:
            assert u.startswith("http"), f"non-verbatim URL form: {u}"

    def test_research_method_first_hand_read(self):
        rm = _mechanism()["research_method"]
        assert "browser.open first-hand read" in rm
        assert "101 lines" in rm


class TestRotationCycleGuard659:
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

    def test_window_655_659_closes_b_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "659"),
            ("B", "658"),
            ("A", "657"),
            ("E", "656"),
            ("D", "655"),
        ], f"rotation window 655-659 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["C", "B", "A", "E", "D"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #659 main commit. Patched in the followup
        # per the #565 convention once the main commit SHA is known.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [
            l for l in out if re.match(r"^[0-9a-f]{40} Type [A-E] #\d+:", l)
        ]
        sha, subject = mains[0].split(" ", 1)
        assert sha.startswith(ANCHORED_SHA), f"anchor not yet patched: {sha}"
        assert subject.startswith("Type C #659:"), (
            f"post-commit anchor broken: newest main is not #659: {subject!r}"
        )

    def test_rotation_guard_regex_actually_matches(self):
        # #632 process note: a rotation guard whose regex never matches is a
        # silent no-op. Verify the guard regexes match a real main-commit
        # subject. Written as a semantic check so the test cannot defeat
        # itself by containing the literal pattern.
        src = open(os.path.join(TESTS_DIR, FILENAME)).read()
        patterns = re.findall(r're\.search\(r"([^"]+)"', src)
        guard_patterns = [p for p in patterns if p.startswith("Type (")]
        assert guard_patterns, "no rotation-guard regex found in this file"
        sample = "Type C #659: News Corp Google sixth-leg watch"
        for p in guard_patterns:
            assert re.search(p, sample), f"guard pattern {p!r} fails on sample"


class TestDocSyncRatchet659:
    def _readme(self):
        return _read(README_PATH)

    def _arch(self):
        return _read(ARCH_PATH)

    def test_readme_has_659_row(self):
        assert re.search(r"#659", self._readme()), "README.md missing the #659 test-table row"

    def test_arch_has_659_row(self):
        assert re.search(r"#659", self._arch()), "docs/ARCHITECTURE.md missing the #659 tree row"

    def test_prior_rows_intact(self):
        readme, arch = self._readme(), self._arch()
        for n in ("654", "655", "658"):
            assert re.search(rf"#{n}", readme), f"README.md lost the #{n} row"
        for n in ("654", "655", "656", "657", "658"):
            assert re.search(rf"#{n}", arch), f"docs/ARCHITECTURE.md lost the #{n} row"

    def test_readme_row_test_count_matches(self):
        m = re.search(rf"`{re.escape(FILENAME)}`\s*\|\s*(\d+)\s*\|", self._readme())
        assert m, "README #659 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )

    def test_readme_row_says_659(self):
        line = next(
            (ln for ln in self._readme().splitlines() if FILENAME in ln),
            None,
        )
        assert line is not None, "README missing the #659 row entirely"
        assert "#659" in line, "README #659 row does not reference #659"

    def test_log_starts_with_659(self):
        assert _read(LOG_PATH).lstrip().startswith("#659 Type C:")


class TestNewsCorpProfileWatchEntry659:
    @staticmethod
    def _rels():
        with open(NEWSCORP_PATH, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        return data["revenue_relationships"]

    @staticmethod
    def _google():
        rels = TestNewsCorpProfileWatchEntry659._rels()
        matches = [r for r in rels if r.get("partner") == "Google"]
        assert len(matches) == 1, (
            f"want exactly 1 Google revenue_relationships entry, got {len(matches)}"
        )
        return matches[0]

    def test_google_entry_type_is_talks_not_deal(self):
        g = self._google()
        assert g["type"] == "ai_licensing_talks_unconfirmed", (
            "Google entry must be typed as unconfirmed talks, not a signed deal"
        )

    def test_google_entry_not_verified(self):
        g = self._google()
        assert g["verified"] is False, "talks entry must not be marked verified"

    def test_google_entry_signed_null(self):
        g = self._google()
        assert g["signed"] is None, "no signed date for an unconfirmed talks entry"

    def test_google_entry_references_mechanism_630(self):
        g = self._google()
        assert "630" in g["scope"], "watch entry should point at mechanism 630"

    def test_google_entry_cites_digiday(self):
        g = self._google()
        assert g["source_url"] == (
            "https://digiday.com/media/news-corp-in-talks-with-google-for-ai-licensing-deal/"
        )

    def test_google_entry_status_unresolved(self):
        g = self._google()
        assert "UNRESOLVED" in g["scope"], "watch entry must carry the UNRESOLVED status"

    def test_five_signed_legs_untouched(self):
        rels = self._rels()
        signed = [
            r["partner"]
            for r in rels
            if r.get("verified") is True
            and r.get("type") in ("ai_licensing", "settlement_revenue")
        ]
        for p in ("OpenAI", "Meta", "Microsoft", "Anthropic", "Bloomberg"):
            assert p in signed, f"signed leg {p} disturbed by the Google watch entry"
