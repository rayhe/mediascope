"""Type C #664: Meta x Reuters multiyear AI chatbot news licensing deal (Oct 2024)
- FIRST dedicated corpus formalization of the Meta x Reuters AI content
  licensing deal (mechanism 633, next free; max numeric mechanism id
  pre-commit 632): announced Oct 25 2024 (Axios first; Reuters self-report
  Aditya Soni; Meta spokesperson confirmed); multi-year, confidential terms,
  Reuters compensated (Axios sourcing); real-time Reuters news in the Meta AI
  chatbot for US users (Facebook, Instagram, WhatsApp, Messenger) with
  summaries and links; Llama training rights UNDISCLOSED. Context: Meta's
  first news deal in years; Reuters a Meta fact-checking partner since 2020;
  Zuckerberg's Sep 2024 "publishers overestimate the value" Verge framing.
- Sep 2026 renewal-window status check: 4 bounded query sets surfaced NO
  renewal/extension/termination reporting; treated ACTIVE per the #599/#609
  convention (bounded absence per the iteration-492 rule).
- Owner-level primary-source disclosure: Thomson Reuters earnings transcripts
  disclose Reuters News generative-AI licensing revenue (Q3 2024 +10% on the
  GenAI line; Q4 2025 $5M transactional agency revenue, Feb 5 2026 call;
  2025-vs-2024 one-off decline with 2026 acceleration forecast; Q1 2026 +6%
  with $3M intercompany line; partners never named). DISAMBIGUATION: Thomson
  Reuters (the company, NYSE:TRI) is not Robert Thomson (News Corp CEO,
  mechanism 594); both held earnings calls on Feb 5 2026.
- FALSIFICATION PIN: Meta PAYS Reuters under an active multiyear deal, yet
  Reuters' Sep 8 2026 Katie Paul Muse-launch piece runs a hard accountability
  register ("despite internal concerns that the technology mismanages its
  access to sensitive personal data"; "RAISING THE STAKES FOR SAFETY";
  internal-tests mixed results). THIRTEENTH falsification-family member
  (after #662 twelfth; #632/#637 partial members only). First payer-Meta-leg
  falsification pin. Excerpt-bounded evidence tier.

Qualitative Type C mapping. tone_scores NOT_SCORED; p_value, cohens_d,
ci_95 NOT_CALCULATED (standing rule Aug 28 2026). Correlational language
only; no causal claim; no blanket coverage-tone claim beyond the single
pinned piece.

Rotation: Type C follows Type B (#663) per A,B,C,D,E. Rotation guard and
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

MECH_KEY = "mechanism_633_meta_reuters_multiyear_ai_chatbot_licensing_deal_sep2026"
FILENAME = "test_type_c_664_meta_reuters_ai_chatbot_deal_falsification_sep10_9pm.py"

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


def _meta_entity():
    with open(ENTITIES_PATH, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return data["entities"]["meta"]


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
    # Next sibling is either another mechanism (4-space) or the next entity
    # (2-space, e.g. xai: here).
    m = re.search(r"\n(?:    mechanism_\d+|  [a-z_]+):", rest)
    return rest[: m.start()] if m else rest


class TestIterationMetadata664:
    def test_mechanism_id_633(self):
        assert _mechanism()["mechanism_id"] == 633

    def test_iteration_664(self):
        assert _mechanism()["iteration"] == 664

    def test_type_c(self):
        m = _mechanism()
        assert m["rotation"] == "Type C"
        assert m["type"] == "financial_incentive_mapping"

    def test_date_time_pdt(self):
        m = _mechanism()
        assert m["date_analyzed"] == "2026-09-10"
        assert m["time_pdt"] == "21:00"

    def test_job_and_goal(self):
        m = _mechanism()
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_mechanism_name_mentions_meta_reuters(self):
        name = _mechanism()["mechanism_name"]
        assert "Meta x Reuters" in name
        assert "Oct 2024" in name

    def test_mechanism_name_mentions_falsification_member_13(self):
        assert "Member 13" in _mechanism()["mechanism_name"]

    def test_mechanism_name_no_em_dash(self):
        assert "\u2014" not in _mechanism()["mechanism_name"]


class TestMechanismPlacement633:
    def test_nested_under_entities_meta(self):
        assert MECH_KEY in _meta_entity()

    def test_sibling_mechanism_549_same_parent(self):
        meta = _meta_entity()
        assert "mechanism_549_newscorp_meta_50m_yr_deal" in meta
        assert meta["mechanism_549_newscorp_meta_50m_yr_deal"]["mechanism_id"] == 549

    def test_no_em_dash_in_block(self):
        assert "\u2014" not in _block_text(), "em dash found in mechanism block"

    def test_ascii_only_in_block(self):
        block = _block_text()
        bad = [c for c in block if ord(c) > 127]
        assert not bad, f"non-ASCII chars in block: {bad[:5]}"

    def test_key_unique_repo_wide(self):
        text = _read(ENTITIES_PATH)
        assert text.count("    " + MECH_KEY + ":") == 1


class TestDealBaseline664:
    def _dt(self):
        return _mechanism()["deal_terms"]

    def test_announcement_date_oct_25_2024(self):
        assert _mechanism()["announcement_date"] == "2024-10-25"

    def test_broke_by_axios_first_reuters_self_report(self):
        broke = _mechanism()["broke_by"]
        assert "Axios first reported" in broke
        assert "Aditya Soni" in broke
        assert "Meta spokesperson confirmed" in broke

    def test_term_multiyear(self):
        assert "multi-year" in self._dt()["term"]

    def test_value_confidential_compensated(self):
        val = self._dt()["value"]
        assert "confidential" in val
        assert "Reuters compensated" in val

    def test_scope_us_meta_ai_chatbot(self):
        assert "US users" in self._dt()["scope"]
        assert "Meta AI chatbot" in self._dt()["scope"]

    def test_surfaces_four_apps(self):
        surfaces = self._dt()["surfaces"]
        for app in ("Facebook", "Instagram", "WhatsApp", "Messenger"):
            assert app in surfaces

    def test_use_cases_summaries_and_links(self):
        uc = self._dt()["use_cases"]
        assert "summary" in uc
        assert "link" in uc

    def test_training_rights_undisclosed(self):
        tr = self._dt()["training_rights"]
        assert "UNDISCLOSED" in tr
        assert "Llama" in tr

    def test_context_first_news_deal_in_years(self):
        assert "first news deal in years" in _mechanism()["context"]["first_news_deal_in_years"]

    def test_context_fact_checking_since_2020(self):
        assert "2020" in _mechanism()["context"]["fact_checking_since_2020"]

    def test_context_zuckerberg_verge_framing(self):
        q = _mechanism()["context"]["zuckerberg_verge_quote"]
        assert "overestimate the value" in q
        assert "The Verge" in q

    def test_context_llm_pulse_timeline(self):
        assert "first news deal" in _mechanism()["context"]["llm_pulse_timeline"]


class TestStatusCheckSep2026:
    def _sc(self):
        return _mechanism()["status_check_sep2026"]

    def test_four_query_sets(self):
        assert len(self._sc()["query_sets"]) == 4

    def test_no_renewal_reporting(self):
        assert "NO renewal" in self._sc()["result"]

    def test_status_active_per_convention(self):
        assert "ACTIVE" in self._sc()["status"]
        assert "#599" in self._sc()["status"]

    def test_bounded_absence_discipline(self):
        assert "iteration-492" in self._sc()["discipline"]

    def test_llm_pulse_lists_reuters(self):
        assert "Reuters" in self._sc()["result"] or "Reuters" in _mechanism()["overview"]


class TestThomsonReutersDisclosure:
    def _td(self):
        return _mechanism()["thomson_reuters_financial_disclosure"]

    def test_q3_2024_plus_10_genai_line(self):
        q = self._td()["q3_2024"]
        assert "+10%" in q
        assert "generative AI-related licensing revenue" in q

    def test_q4_2025_call_5m(self):
        q = self._td()["q4_2025_call"]
        assert "$5 million" in q
        assert "Feb 5 2026" in q

    def test_q4_2025_motley_decline_acceleration(self):
        q = self._td()["q4_2025_motley"]
        assert "decline" in q
        assert "acceleration" in q

    def test_q1_2026_plus_6_intercompany_3m(self):
        q = self._td()["q1_2026"]
        assert "+6%" in q
        assert "$3 million" in q
        assert "intercompany" in q

    def test_partners_never_named(self):
        assert "never names" in self._td()["confidentiality"]

    def test_thomson_disambiguation(self):
        d = self._td()["disambiguation"]
        assert "Robert Thomson" in d
        assert "mechanism 594" in d
        assert "NOT Robert Thomson" in d

    def test_feb5_2026_dual_call_guard(self):
        assert "Feb 5 2026" in self._td()["disambiguation"]
        assert "TRI Q4 2025" in self._td()["disambiguation"]
        assert "News Corp Q2 FY2026" in self._td()["disambiguation"]


class TestFalsificationPinThirteen:
    def _ff(self):
        return _mechanism()["falsification_family"]

    def test_family_membership_thirteenth(self):
        assert "THIRTEENTH" in self._ff()["membership"]
        assert "#662 twelfth" in self._ff()["membership"]

    def test_prediction_softer_from_paid_counterparty(self):
        assert "SOFTER" in self._ff()["prediction"]

    def test_reuters_muse_piece_sep_8_2026(self):
        obs = self._ff()["observed"]
        assert "Sep 8 2026" in obs
        assert "Muse" in obs

    def test_katie_paul_byline(self):
        assert "Katie Paul" in self._ff()["observed"]

    def test_hard_register_quotes(self):
        obs = self._ff()["observed"]
        assert "mismanages its access to sensitive personal data" in obs
        assert "RAISING THE STAKES FOR SAFETY" in obs

    def test_illustrative_tone_minus_045_manual(self):
        t = self._ff()["illustrative_tone"]
        assert "-0.45" in t
        assert "MANUAL ILLUSTRATIVE" in t

    def test_first_payer_meta_pin(self):
        assert "Meta is the payer" in self._ff()["first_payer_meta_pin"] or \
            "Meta-as-payer" in self._ff()["first_payer_meta_pin"]

    def test_cross_outlet_nuance(self):
        nu = self._ff()["cross_outlet_nuance"]
        assert "+0.40" in nu
        assert "Bobrowsky" in nu
        assert "-0.45" in nu

    def test_excerpt_bounded_tier(self):
        assert "reuters.com not opened first-hand" in self._ff()["excerpt_bounded"]


class TestConfoundersAndCounterevidence:
    def test_five_ranked_confounders(self):
        assert len(_mechanism()["ranked_confounders"]) == 5

    def test_strong_confound_1_shah_admission(self):
        c = _mechanism()["ranked_confounders"][0]
        assert c["strength"] == "strong"
        assert "Vishal Shah" in c["confounder"]

    def test_strong_confound_2_wire_genre_n1(self):
        c = _mechanism()["ranked_confounders"][1]
        assert c["strength"] == "strong"
        assert "n=1" in c["confounder"]

    def test_strong_confound_3_payment_magnitude_unknown(self):
        c = _mechanism()["ranked_confounders"][2]
        assert c["strength"] == "strong"
        assert "undisclosed" in c["confounder"]

    def test_moderate_confound_launch_register(self):
        c = _mechanism()["ranked_confounders"][3]
        assert c["strength"] == "moderate"

    def test_weak_confound_rag_scope(self):
        c = _mechanism()["ranked_confounders"][4]
        assert c["strength"] == "weak"
        assert "RAG" in c["confounder"] or "chatbot-RAG" in c["confounder"]

    def test_three_counterevidence(self):
        assert len(_mechanism()["counterevidence"]) == 3

    def test_counterevidence_earnings_tied_to_licensing(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "+10%" in ce

    def test_counterevidence_self_report_neutral(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "neutral" in ce

    def test_counterevidence_wsj_soft_counterpart(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "News Corp" in ce
        assert "+0.40" in ce


class TestNovelty664:
    def _nv(self):
        return " ".join(_mechanism()["novelty_verification"])

    def test_first_corpus_formalization_meta_reuters(self):
        assert "FIRST corpus formalization of the Meta x Reuters AI content licensing deal" in self._nv()

    def test_zero_mechanism_633_keys_precommit(self):
        assert "Zero mechanism_633 keys repo-wide pre-commit" in self._nv()

    def test_zero_test_type_c_664_files(self):
        assert "Zero test_type_c_664 files on disk pre-commit" in self._nv()

    def test_no_664_in_git_log_precommit(self):
        assert "No Type C #664 in git log pre-commit" in self._nv()

    def test_mechanism_633_next_free_632_max(self):
        assert "mechanism_id 633 next free" in self._nv()
        assert "max numeric mechanism id pre-commit 632" in self._nv()

    def test_distinct_from_549_453_594(self):
        nv = self._nv()
        assert "mechanism 549" in nv
        assert "#453" in nv
        assert "mechanism 594" in nv

    def test_source_urls_count_13(self):
        assert len(_mechanism()["source_urls"]) == 13

    def test_key_urls_verbatim(self):
        joined = " ".join(_mechanism()["source_urls"])
        assert "https://www.reuters.com/technology/artificial-intelligence/meta-platforms-use-reuters-news-content-ai-chatbot-2024-10-25/?outputType=chromeless" in joined
        assert "https://www.reuters.com/business/meta-launches-ai-agent-that-can-access-other-apps-send-emails-make-payments-2026-09-08/" in joined
        assert "https://llmpulse.ai/blog/ai-content-licensing-deals/" in joined
        assert "https://www.marketbeat.com/earnings/reports/2026-2-5-thomson-reuters-corp-can-stock/" in joined

    def test_urls_verbatim_no_construction(self):
        for u in _mechanism()["source_urls"]:
            assert u.startswith("http"), f"non-verbatim URL form: {u}"

    def test_research_method_four_query_sets(self):
        assert "4 browser.search query sets" in _mechanism()["research_method"]


class TestRotationCycleGuard664:
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

    def test_window_660_664_closes_b_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "664"),
            ("B", "663"),
            ("A", "662"),
            ("E", "661"),
            ("D", "660"),
        ], f"rotation window 660-664 wrong: {observed}"

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
        # Post-commit anchor: the #664 main commit. Patched in the followup
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
        assert subject.startswith("Type C #664:"), (
            f"post-commit anchor broken: newest main is not #664: {subject!r}"
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
        sample = "Type C #664: Meta Reuters deal falsification"
        for p in guard_patterns:
            assert re.search(p, sample), f"guard pattern {p!r} fails on sample"


class TestDocSyncRatchet664:
    def _readme(self):
        return _read(README_PATH)

    def _arch(self):
        return _read(ARCH_PATH)

    def test_readme_has_664_row(self):
        assert re.search(r"#664", self._readme()), "README.md missing the #664 test-table row"

    def test_arch_has_664_row(self):
        assert re.search(r"#664", self._arch()), "docs/ARCHITECTURE.md missing the #664 tree row"

    def test_prior_rows_intact(self):
        readme, arch = self._readme(), self._arch()
        for n in ("659", "661", "663"):
            assert re.search(rf"#{n}", readme), f"README.md lost the #{n} row"
        for n in ("659", "660", "661", "662", "663"):
            assert re.search(rf"#{n}", arch), f"docs/ARCHITECTURE.md lost the #{n} row"

    def test_readme_row_test_count_matches(self):
        m = re.search(rf"`{re.escape(FILENAME)}`\s*\|\s*(\d+)\s*\|", self._readme())
        assert m, "README #664 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )

    def test_readme_row_says_664(self):
        line = next(
            (ln for ln in self._readme().splitlines() if FILENAME in ln),
            None,
        )
        assert line is not None, "README missing the #664 row entirely"
        assert "#664" in line, "README #664 row does not reference #664"

    def test_log_starts_with_664(self):
        assert _read(LOG_PATH).lstrip().startswith("#664 Type C:")
