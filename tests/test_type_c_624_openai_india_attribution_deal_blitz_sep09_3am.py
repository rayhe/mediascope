"""Type C #624: OpenAI India attribution-deal blitz (Sep 7-8 2026).

FIRST dedicated India-market mechanism in the corpus (mechanism_id 609,
next free pre-commit; max numeric mechanism_id was 608). Within 48 hours
OpenAI signed two Indian publisher groups to attribution-and-links ChatGPT
discovery partnerships:

(a) BCCL (Times Group), announced Sep 7 2026: The Times of India + The
Economic Times into ChatGPT, attributed excerpts/summaries with direct
links, no fee disclosed.

(b) Indian Express Group, announced Sep 8 2026: The Indian Express + The
Financial Express + business properties, live reporting plus archives,
seven languages (English, Hindi, Marathi, Malayalam, Tamil, Bengali,
Gujarati), attributed excerpts with source identification and direct
links, full editorial control retained, no fee disclosed. Quoted:
Nandagopal Rajan (CEO, Indian Express Digital) and Varun Shetty (VP,
Media Partnerships, OpenAI).

Deal structure: both framed as content discovery / attribution
partnerships, NOT as training-data licences. $0 disclosed fee on both
legs.

Sue-then-sign arc: ANI sued OpenAI Nov 2024 (Delhi High Court); Feb 2025
the Indian Express, NDTV, Network18, Hindustan Times and the DNPA sought
to join the suit while OpenAI's 31-page filing (Reuters) denied using
their content for training; Jul 24 2026 the Delhi HC denied ANI's interim
relief; Sep 8 2026 ANI's appeal was listed and adjourned to Sep 14 (Bar
and Bench via FourWeekMBA), the same day the Indian Express partnership
was announced. Timing coincidence on the record, not a coordination
claim.

Structural import: The Times of India is already a Google News AI pilot
publisher in the corpus (mechanism 412), so the Sep 7 OpenAI deal makes
TOI the third Google-plus-OpenAI dual-payer publisher after FT (437) and
WaPo (569). Extends the sue-one-sign-the-other sequence (#514 Guardian),
the woo-and-sue dual posture (#519 News Corp), and the pay-or-sue
bifurcation (#614 Reddit v. Anthropic) into the India market.

Qualitative Type C mapping only: tone_scores NOT_SCORED, p_value and
cohens_d NOT_CALCULATED, is_significant False, correlation not causation,
no coverage-tone claim (neither counterparty is a tracked publication).

Rotation: Type C follows Type B (#623) per A,B,C,D,E. Rotation guard
deselected pre-commit per the #565 followup convention; anchor patched in
the followup commit once the main commit SHA is known.
"""

import ast
import glob
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

MECH_KEY = "mechanism_609_openai_india_attribution_deal_blitz"
FILENAME = "test_type_c_624_openai_india_attribution_deal_blitz_sep09_3am.py"

FOURWEEK_URL = "https://fourweekmba.com/ai-openai-india-publisher-deals-attribution-strategy/"
MEDIABRIEF_URL = "https://mediabrief.com/indian-express-group-partners-with-openai/"
INDIANTELEVISION_URL = "https://indiantelevision.com/mam/indian-express-group-partners-with-openai-to-expand-discovery-of-its-journalism/"
STORYBOARD18_URL = "https://www.storyboard18.com/digital/indian-express-openai-partner-for-content-discovery-ws-l-110051.htm"
ADTRIBE_URL = "https://adtribe.world/indian-express-group-signs-openai-deal-covering-seven-languages"
TECHPORTAL_URL = "https://thetechportal.com/2025/02/13/openai-denies-allegations-of-using-indian-media-groups-content-to-train-chatgpt-report/"
LLMPULSE_URL = "https://llmpulse.ai/blog/ai-content-licensing-deals/"

EXPECTED_LANGUAGES = [
    "English", "Hindi", "Marathi", "Malayalam", "Tamil", "Bengali", "Gujarati",
]


def _entities():
    with open(ENTITIES_PATH) as f:
        return yaml.safe_load(f)


def _mechanism():
    m = _entities()["entities"]["openai"].get(MECH_KEY)
    assert m is not None, f"{MECH_KEY} missing from the openai entity"
    return m


def _deals():
    return {d["counterparty"]: d for d in _mechanism()["deals"]}


def _bccl():
    ds = _deals()
    key = next(k for k in ds if k.startswith("BCCL"))
    return ds[key]


def _express():
    ds = _deals()
    key = next(k for k in ds if "Indian Express Group" in k)
    return ds[key]


def _count_def_tests():
    path = os.path.join(TESTS_DIR, FILENAME)
    tree = ast.parse(open(path).read())
    return sum(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name.startswith("test_")
        for n in ast.walk(tree)
    )


def read_readme():
    with open(README_PATH) as f:
        return f.read()


def read_arch():
    with open(ARCH_PATH) as f:
        return f.read()


def read_log():
    with open(LOG_PATH) as f:
        return f.read()


class TestIterationMetadata624:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 624

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 609

    def test_mechanism_id_unique_repo_wide(self):
        hits = []
        for path in glob.glob(
            os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True
        ):
            hits.extend(re.findall(r"mechanism_id: 609\b", open(path).read()))
        assert len(hits) == 1, f"mechanism_id 609 appears {len(hits)} times"

    def test_iteration_type_c(self):
        assert _mechanism()["verification"]["type"] == "C"

    def test_scheduled_job_id(self):
        assert _mechanism()["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_goal_id(self):
        assert _mechanism()["goal_id"] == "goal_54093bda4145"

    def test_iteration_log_has_624_entry_newest_first(self):
        assert read_log().startswith("#624 Type C:"), (
            "iteration-log.md is not newest-first at #624"
        )

    def test_author_attribution(self):
        assert _mechanism()["author"] == "Kit (with Ray)"

    def test_date(self):
        assert _mechanism()["verification"]["date"] == "2026-09-09 03:00 PDT"

    def test_first_india_market_mechanism(self):
        dumped = yaml.safe_dump(
            _entities()["entities"]["openai"], allow_unicode=True
        ).lower()
        assert dumped.count("india_attribution_deal_blitz") >= 1


class TestDealFacts624:
    def test_two_deals(self):
        assert len(_mechanism()["deals"]) == 2

    def test_bccl_announced_sep7(self):
        assert _bccl()["announced"] == "2026-09-07"

    def test_bccl_publications(self):
        pubs = _bccl()["publications"]
        assert "The Times of India" in pubs
        assert "The Economic Times" in pubs

    def test_bccl_structure_attribution_links(self):
        s = _bccl()["structure"]
        assert "attributed" in s and "direct links" in s

    def test_bccl_terms_undisclosed(self):
        assert "undisclosed" in _bccl()["financial_terms"]

    def test_indian_express_announced_sep8(self):
        assert _express()["announced"] == "2026-09-08"

    def test_indian_express_publications(self):
        pubs = _express()["publications"]
        assert "The Indian Express" in pubs
        assert "The Financial Express" in pubs
        assert "business properties" in pubs

    def test_indian_express_seven_languages(self):
        assert _express()["languages"] == EXPECTED_LANGUAGES

    def test_indian_express_live_plus_archives(self):
        assert "archived" in _express()["content_scope"]
        assert "live" in _express()["content_scope"]

    def test_indian_express_editorial_control(self):
        ec = _express()["editorial_control"]
        assert "complete and independent editorial control" in ec
        assert "no editorial role" in ec

    def test_quotes_rajan_and_shetty(self):
        speakers = [q["speaker"] for q in _express()["quotes"]]
        assert any("Nandagopal Rajan" in s for s in speakers)
        assert any("Varun Shetty" in s for s in speakers)

    def test_zero_disclosed_fee_note(self):
        note = _mechanism()["deal_structure_note"]
        assert "Zero dollars of disclosed fee" in note
        assert "training-data licence" in note


class TestSueThenSignArc624:
    def _arc(self):
        return " ".join(_mechanism()["sue_then_sign_arc"])

    def test_ani_suit_nov2024(self):
        assert "Nov 2024" in self._arc()
        assert "Delhi High Court" in self._arc()

    def test_feb2025_join_attempt_and_denial(self):
        arc = self._arc()
        assert "Feb 2025" in arc
        assert "seek to join the suit" in arc
        assert "31-page filing" in arc
        assert "denies using" in arc

    def test_jul2026_interim_relief_denied(self):
        assert "Jul 24 2026" in self._arc()
        assert "denies" in self._arc()

    def test_sep8_appeal_adjourned_sep14(self):
        arc = self._arc()
        assert "adjourned to Sep 14" in arc
        assert "Bar and Bench" in arc

    def test_net_arc_sue_then_sign(self):
        assert "Sue-then-sign sequence" in self._arc()

    def test_timing_coincidence_disclaimed(self):
        assert "coincidence on the record" in self._arc()


class TestStructuralContrasts624:
    def _contrasts(self):
        return " ".join(_mechanism()["structural_contrasts"])

    def test_contrast_514_guardian(self):
        assert "Mechanism 514" in self._contrasts()
        assert "sue-one-sign-the-other" in self._contrasts()

    def test_contrast_519_newscorp(self):
        assert "Mechanism 519" in self._contrasts()
        assert "woo-and-sue" in self._contrasts()

    def test_contrast_614_reddit_anthropic(self):
        assert "Mechanism 614" in self._contrasts()
        assert "pay-or-sue" in self._contrasts()

    def test_contrast_412_toi_dual_payer(self):
        c = self._contrasts()
        assert "Mechanism 412" in c
        assert "third" in c
        assert "437" in c and "569" in c

    def test_contrast_iteration_609_renewal_window(self):
        assert "Iteration 609" in self._contrasts()

    def test_correlation_not_causation(self):
        sd = _mechanism()["statistical_discipline"]
        assert sd["correlation_not_causation"] is True
        assert "No causal claim" in _mechanism()["correlational_note"]

    def test_confounders_ranked(self):
        confs = _mechanism()["ranked_confounders"]
        assert len(confs) == 5
        strengths = [c["strength"] for c in confs]
        assert strengths.count("strong") == 2
        assert "weak" in strengths

    def test_no_coverage_tone_claim(self):
        assert _mechanism()["no_coverage_tone_claim"] is True


class TestRotationCycleGuard624:
    """Rotation guard, deselected pre-commit per the #565 followup convention.

    Asserts the post-commit anchor, so it runs green only in the followup
    commit after the main commit SHA is known. Pre-commit it is deselected.
    """

    def _mains(self):
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]
        assert len(mains) >= 5
        return mains

    def test_window_620_624_closes_b_to_c(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("C", "624"),
            ("B", "623"),
            ("A", "622"),
            ("E", "621"),
            ("D", "620"),
        ], f"rotation window 620-624 wrong: {observed}"

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
        # Post-commit anchor: the #624 main commit. Patched in the followup
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
        assert sha.startswith("PATCH_IN_FOLLOWUP"), f"anchor drifted: {sha}"
        assert subject.startswith("Type C #624:"), (
            f"post-commit anchor broken: newest main is not #624: {subject!r}"
        )


class TestDocSyncRatchet624:
    def test_readme_has_624_row(self):
        assert re.search(r"#624", read_readme()), "README.md missing the #624 test-table row"

    def test_arch_has_624_row(self):
        assert re.search(r"#624", read_arch()), "docs/ARCHITECTURE.md missing the #624 tree row"

    def test_prior_rows_intact(self):
        readme, arch = read_readme(), read_arch()
        for n in ("619", "620", "621", "622", "623"):
            assert re.search(rf"#{n}", readme), f"README.md lost the #{n} row"
            assert re.search(rf"#{n}", arch), f"docs/ARCHITECTURE.md lost the #{n} row"

    def test_readme_row_test_count_matches(self):
        m = re.search(rf"`{re.escape(FILENAME)}`\s*\|\s*(\d+)\s*\|", read_readme())
        assert m, "README #624 row missing or malformed"
        assert int(m.group(1)) == _count_def_tests(), (
            f"README row says {m.group(1)} but file carries {_count_def_tests()}"
        )

    def test_readme_row_says_624(self):
        line = next(
            (ln for ln in read_readme().splitlines() if FILENAME in ln),
            None,
        )
        assert line is not None, "README missing the #624 row entirely"
        assert "#624" in line, "README #624 row does not reference #624"

    def test_log_starts_with_624(self):
        assert read_log().startswith("#624 Type C:")


class TestNoBrittlePatterns624:
    def test_yaml_reparses_clean(self):
        m = _mechanism()
        assert m["mechanism_id"] == 609
        assert m["deals"][1]["languages"] == EXPECTED_LANGUAGES

    def test_no_em_dash_in_mechanism(self):
        text = yaml.safe_dump(_mechanism(), allow_unicode=True)
        assert "\u2014" not in text, "em dash leaked into the #624 mechanism"

    def test_all_urls_http_or_https(self):
        for u in _mechanism()["sources"]:
            assert u.startswith("http"), f"bad URL: {u}"

    def test_no_zero_coverage_claims(self):
        dumped = yaml.safe_dump(_mechanism(), allow_unicode=True).lower()
        assert "zero investigative" not in dumped
        assert "zero coverage" not in dumped
        assert "has written zero" not in dumped

    def test_no_engine_significance_claims(self):
        dumped = yaml.safe_dump(_mechanism(), allow_unicode=True).lower()
        assert "p_value" in dumped
        assert "significant true" not in dumped

    def test_source_urls_verbatim(self):
        sources = _mechanism()["sources"]
        for url in (
            FOURWEEK_URL,
            MEDIABRIEF_URL,
            INDIANTELEVISION_URL,
            STORYBOARD18_URL,
            ADTRIBE_URL,
            TECHPORTAL_URL,
            LLMPULSE_URL,
        ):
            assert url in sources, f"source URL missing from mechanism: {url}"

    def test_research_method_names_evidence_tiers(self):
        method = _mechanism()["research_method"]
        assert "iteration-492" in method
        assert "second-hand" in method

    def test_artifact_readiness_present(self):
        assert "analysis.json" in _mechanism()["artifact_readiness"]
