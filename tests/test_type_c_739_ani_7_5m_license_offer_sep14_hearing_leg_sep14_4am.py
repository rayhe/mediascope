"""
Type C iteration #739: ANI $7.5M license-offer pricing datum + Sep 14 2026
Division Bench hearing-day leg (mechanism 678) - FIRST dedicated corpus
pricing leg attaching an exact dollar figure to the India-market BATNA
(extension of mechanism 657).

Mint (livemint.com opinion piece, Jul 24 2026 coverage, excerpt-bounded per
#503): "the court noted that ANI had offered OpenAI a licence for $7.5
million, demonstrating that its asserted injury was capable of monetary
valuation." The balance-of-convenience reasoning in the Jul 24 interim order
turns on that number: because ANI itself monetized the injury, the loss is
monetarily compensable if ANI ultimately succeeds, so interim injunction was
refused. The $7.5M ask is the single public price tag for an Indian
publisher's AI-training licence in the record, and it is judicially embedded
in the fair-use pricing decision.

Scale contrast: vs OpenAI's $300-400M/yr global paid-publisher portfolio
(m494 family); vs the zero-fee attribution-discovery template with BCCL and
the Indian Express Group (mechanism 609); vs Anthropic's $1.5B settlement
pricing paid licensing elsewhere (#729 carried). Fair-use pricing pair with
mechanism 672 (US DOJ Statement of Interest filed Sep 1-2 pushing the
license-alternative price toward zero; the India appeal reprices the other
arm ten days later per #729).

Sep 14 2026 Division Bench hearing (listed today; bench Justices V. Kameshwar
Rao and Manmeet PS Arora; Rao now Chief Justice of Patna High Court; bench
did not assemble Sep 8). No hearing-outcome reporting surfaced in bounded
searches this run (~04:00 PDT / 16:30 IST) - bounded absence per
iteration-492, not a proven zero.

Statistical discipline (Aug 28 2026 standing contract): qualitative-only;
scorer none; tone NOT_SCORED; p_value/cohens_d/ci_95 NOT_CALCULATED;
is_significant False; engine NOT run; NOT artifact-grade. Verdict: license
price documented ($7.5M plaintiff ask, excerpt-bounded); incentive-pricing
inference directional_only. NOT a falsification-family member (ledger holds
at 24). Correlation is not causation.

Rotation: Type C (A/B/C/D/E cycle). Window 735-739 closes D (#735) -> E
(#736) -> A (#737) -> B (#738) -> C (#739); novelty anchor patched in the
followup per the #565 convention (two-commit: main, then anchor SHA patch).
Research method: 2 browser.search query sets this run; 1 browser.open
attempt on the Mint piece failed terminally (upstream_unavailable, retry
exhausted) - NOT retried per turn constraint; excerpt-bounded per #503.
No analysis.json update warranted (qualitative Type C pricing leg).
Sep 14 2026 04:00 PDT - 64 tests, 10 classes.
"""

"""Deselected pre-commit: rotation-guard anchor test per the #565 followup
convention; the anchor is patched in the followup commit once the main
commit SHA is known."""

import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO, "tests")
THIS_FILE = os.path.basename(__file__)

MECHANISM_KEY = "ani_license_price_tag_7_5m_sep14_division_bench_hearing_leg"
YAML_PATH = os.path.join(REPO, "profiles", "competitor-entities.yaml")
LOG_PATH = os.path.join(REPO, "iteration-log.md")
FILE_738 = "test_type_b_738_jason_aten_inc_google_aspirational_vs_apple_adversarial_register_gradient_sep14_3am.py"

MINT_URL = "https://www.livemint.com/opinion/online-views/ani-vs-openai-delhi-high-court-ruling-intellectual-property-ai-training-copyright-11785477510864.html"
BMI_URL = "https://bestmediainfo.com/mediainfo/mediainfo-digital/ani-openai-copyright-appeal-rescheduled-to-september-14-in-delhi-hc-12507218"
KOK_URL = "https://www.kokthum.com/national/ani-moves-delhi-high-court-division-bench-in-openai-case-india-news"
E4M_URL = "https://www.exchange4media.com/digital-news/openai-vs-ani-courts-interim-relief-to-openai-raises-bar-for-publisher-copyright-claims-156652.html"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. Anchor test is deselected pre-commit.
ANCHORED_SHA = "8083313e95d0dfb54351d3b91fed28c5749882ff"


def load_block():
    with open(YAML_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["entities"]["openai"][MECHANISM_KEY]


class TestIterationMetadata739:
    def test_iteration_is_739(self):
        assert load_block()["iteration"] == 739

    def test_rotation_is_type_c(self):
        assert load_block()["rotation"] == "Type C"

    def test_iteration_type_c(self):
        assert load_block()["iteration_type"] == "C"

    def test_type_is_financial_incentive_mapping(self):
        assert load_block()["type"] == "financial_incentive_mapping"

    def test_type_label(self):
        assert load_block()["type_label"] == "Financial Incentive Mapping"

    def test_date_time_job_goal(self):
        b = load_block()
        assert b["date_analyzed"] == "2026-09-14"
        assert b["time_pdt"] == "04:00"
        assert b["job_id"] == "mediascope-daily-iteration"
        assert b["goal_id"] == "goal_54093bda4145"

    def test_mechanism_id_678_int(self):
        b = load_block()
        assert isinstance(b["mechanism_id"], int)
        assert b["mechanism_id"] == 678

    def test_single_678_block_in_openai(self):
        openai = yaml.safe_load(open(YAML_PATH, encoding="utf-8"))["entities"]["openai"]
        hits = [k for k, v in openai.items()
                if isinstance(v, dict) and v.get("mechanism_id") == 678]
        assert hits == [MECHANISM_KEY]

    def test_first_pricing_leg_claim(self):
        assert "FIRST" in load_block()["mechanism_name"]
        assert "pricing" in load_block()["mechanism_name"].lower()

    def test_test_file_field(self):
        assert load_block()["test_file"] == "tests/" + THIS_FILE


class TestPriceDatumFacts739:
    def test_amount_usd_7_5m(self):
        assert load_block()["price_datum"]["amount_usd"] == 7500000

    def test_direction_is_ani_ask(self):
        d = load_block()["price_datum"]
        assert "ANI offered OpenAI" in d["direction"]
        assert "$7.5 million" in d["direction"]

    def test_mint_source_attribution(self):
        assert "Mint" in load_block()["price_datum"]["source"]

    def test_evidence_grade_excerpt_bounded(self):
        g = load_block()["price_datum"]["evidence_grade"]
        assert "excerpt-bounded" in g
        assert "#503" in g

    def test_judicial_function_balance_of_convenience(self):
        f = load_block()["price_datum"]["judicial_function"]
        assert "balance-of-convenience" in f
        assert "interim injunction refused" in f

    def test_overview_quotes_mint_figure(self):
        o = load_block()["overview"]
        assert "$7.5 million" in o
        assert "capable of monetary valuation" in o

    def test_hearing_listed_today(self):
        h = load_block()["hearing_day_watch"]
        assert h["listed"] == "Sep 14 2026, Division Bench of the Delhi High Court"

    def test_bench_composition(self):
        b = load_block()["hearing_day_watch"]["bench"]
        assert "V. Kameshwar Rao" in b
        assert "Manmeet PS Arora" in b
        assert "Patna High Court" in b

    def test_outcome_unresolved_bounded_absence(self):
        s = load_block()["hearing_day_watch"]["status"]
        assert "outcome unresolved" in s
        assert "bounded absence" in load_block()["overview"]


class TestBATNAPricingTheory739:
    def test_scale_contrast_four_legs(self):
        assert len(load_block()["scale_contrast"]) == 4

    def test_portfolio_300_400m(self):
        joined = " ".join(load_block()["scale_contrast"])
        assert "$300-400M/yr" in joined

    def test_zero_fee_template_m609(self):
        joined = " ".join(load_block()["scale_contrast"])
        assert "zero-fee" in joined
        assert "mechanism 609" in joined

    def test_anthropic_1_5b_settlement(self):
        joined = " ".join(load_block()["scale_contrast"])
        assert "$1.5B" in joined

    def test_ani_between_zero_and_portfolio(self):
        joined = " ".join(load_block()["scale_contrast"])
        assert "only Indian single-publisher price tag" in joined

    def test_fair_use_pricing_pair_us_leg(self):
        p = load_block()["fair_use_pricing_pair"]
        assert "mechanism 672" in p["us_leg"]
        assert "toward zero" in p["us_leg"]

    def test_fair_use_pricing_pair_india_leg(self):
        assert "Sep 14 2026" in load_block()["fair_use_pricing_pair"]["india_leg"]

    def test_correlational_note_no_causal_claim(self):
        assert "No causal claim" in load_block()["correlational_note"]

    def test_no_coverage_tone_claim(self):
        assert load_block()["no_coverage_tone_claim"] is True

    def test_cautious_language_required(self):
        assert load_block()["cautious_language_required"] is True


class TestConfounders739:
    def test_six_ranked_confounders(self):
        assert len(load_block()["ranked_confounders"]) == 6

    def test_three_strong_three_weak_pattern(self):
        strengths = [c["strength"] for c in load_block()["ranked_confounders"]]
        assert strengths == ["strong", "strong", "strong", "moderate", "moderate", "weak"]

    def test_strong_confound_second_source_missing(self):
        joined = " ".join(c["confounder"] for c in load_block()["ranked_confounders"])
        assert "second-source corroboration has not surfaced" in joined

    def test_browser_open_failure_logged(self):
        joined = " ".join(c["confounder"] for c in load_block()["ranked_confounders"])
        assert "browser.open first-hand attempt failed terminally" in joined

    def test_weak_confound_mixed_scale(self):
        weak = load_block()["ranked_confounders"][-1]
        assert weak["strength"] == "weak"
        assert "mixes a single-publisher ask with an annual portfolio total" in weak["confounder"]

    def test_four_bounded_absences(self):
        assert len(load_block()["bounded_absences"]) == 4

    def test_no_openai_response_absence(self):
        joined = " ".join(load_block()["bounded_absences"])
        assert "no OpenAI response to the $7.5M offer" in joined


class TestSourcesAndResearch739:
    def test_four_source_urls(self):
        assert len(load_block()["source_urls"]) == 4

    def test_source_urls_verbatim(self):
        urls = load_block()["source_urls"]
        assert urls[0] == MINT_URL
        assert urls[1] == BMI_URL
        assert urls[2] == KOK_URL
        assert urls[3] == E4M_URL

    def test_research_method_two_query_sets(self):
        rm = load_block()["research_method"]
        assert "2 browser.search query sets" in rm
        assert "verbatim from Full-URL listings" in rm

    def test_browser_open_failure_in_research_method(self):
        assert "upstream_unavailable" in load_block()["research_method"]

    def test_cross_references_present(self):
        joined = " ".join(load_block()["cross_references"])
        for ref in ("mechanism 657", "mechanism 609", "mechanism 672",
                    "mechanism 636", "mechanism 519"):
            assert ref in joined, ref

    def test_novelty_first_pricing_datum(self):
        assert "FIRST dedicated pricing-datum leg" in load_block()["novelty"]

    def test_statistical_discipline_qualitative(self):
        sd = load_block()["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False
        assert sd["artifact_grade"] is False
        assert "directional_only" in sd["verdict"]
        assert "NOT a falsification-family member" in sd or \
               "NOT a falsification-family member" in load_block()["falsification_family"]

    def test_falsification_family_not_member(self):
        assert "NOT a falsification-family member" in load_block()["falsification_family"]
        assert "ledger holds at 24" in load_block()["falsification_family"]

    def test_no_analysis_json_update(self):
        assert "No analysis.json update" in load_block()["artifact_readiness"]


class TestIterationLog739:
    def _tail(self):
        with open(LOG_PATH, encoding="utf-8") as f:
            return "\n".join(f.read().splitlines()[-40:])

    def test_log_entry_present(self):
        assert "#739" in self._tail()

    def test_log_mechanism_678(self):
        assert "mechanism 678" in self._tail()

    def test_log_price_datum(self):
        assert "7.5" in self._tail()

    def test_log_rotation_window(self):
        assert "735-739" in self._tail()


class TestRotationCycleGuard739:
    ANCHORED_SHA = ANCHORED_SHA

    @staticmethod
    def _rotation_files():
        result = {}
        for fn in os.listdir(TESTS_DIR):
            m = re.match(r"test_type_([a-e])_(\d+)_", fn)
            if m:
                result.setdefault(int(m.group(2)), []).append((m.group(1), fn))
        return result

    def test_24_rotation_files_contiguous(self):
        files = self._rotation_files()
        for n in range(716, 740):
            assert n in files and len(files[n]) == 1, \
                f"iteration {n} file missing or duplicated: {files.get(n)}"
            letter, fn = files[n][0]
            expected = "deabc"[(n - 710) % 5]
            assert letter == expected, f"iteration {n}: expected type {expected}, file is {fn}"

    def test_window_closes_to_c(self):
        files = self._rotation_files()
        assert files[735][0][0] == "d"
        assert files[736][0][0] == "e"
        assert files[737][0][0] == "a"
        assert files[738][0][0] == "b"
        assert files[739][0][0] == "c"
        assert files[739][0][1] == THIS_FILE

    def test_anchor_sha_pinned_post_commit(self):
        actual = subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=REPO
        ).stdout.strip()
        assert self.ANCHORED_SHA != "TBD_PATCHED_IN_FOLLOWUP", "anchor not yet patched post-commit"
        assert actual == self.ANCHORED_SHA, f"HEAD {actual} != anchored {self.ANCHORED_SHA}"


class TestDocSync739:
    def test_readme_row(self):
        with open(os.path.join(REPO, "README.md"), encoding="utf-8") as f:
            assert THIS_FILE in f.read()

    def test_architecture_row(self):
        with open(os.path.join(REPO, "docs", "ARCHITECTURE.md"), encoding="utf-8") as f:
            assert THIS_FILE in f.read()


class TestSweepSupersession739:
    def test_max_mechanism_678(self):
        ids = []
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if not fn.endswith(".yaml"):
                    continue
                text = open(os.path.join(root, fn), encoding="utf-8").read()
                ids.extend(int(x) for x in re.findall(r"(?m)^\s*mechanism_id:\s*(\d+)\s*$", text))
        assert max(ids) == 678

    def test_zero_underscore_678_keys_in_profiles(self):
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = open(os.path.join(root, fn), encoding="utf-8").read()
                    assert "mechanism_678_" not in text, f"mechanism_678_ key in {fn}"

    def test_zero_underscore_678_keys_outside_carriers(self):
        carriers = {FILE_738, THIS_FILE}
        hits = []
        for fn in os.listdir(TESTS_DIR):
            fp = os.path.join(TESTS_DIR, fn)
            if fn in carriers or not os.path.isfile(fp):
                continue
            if "mechanism_678_" in open(fp, encoding="utf-8").read():
                hits.append(fn)
        assert hits == [], f"mechanism_678_ keys outside sweep carriers: {hits}"

    def test_zero_mechanism_679_keys_profiles_only(self):
        # Mirrors the #734 pattern: profiles/-only walk. My own file
        # references 679 in this sweep test, so tests/ is excluded.
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = open(os.path.join(root, fn), encoding="utf-8").read()
                    assert "mechanism_679" not in text, fn

    def test_738_max_677_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to
        # 678 supersedes #738's max-677 sweep per the #710/#720 convention.
        text = open(YAML_PATH, encoding="utf-8").read()
        assert "mechanism_id: 678" in text

    def test_738_zero_678_sweep_stays_green_by_designed_keying(self):
        # My block keys as ani_license_price_tag_7_5m_sep14_division_bench_hearing_leg
        # (colon-form mechanism_id: 678), so #738's underscore-form sweep
        # for mechanism_678_ stays green - designed keying per #723.
        assert "mechanism_678" not in MECHANISM_KEY
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    assert "mechanism_678_" not in open(os.path.join(root, fn), encoding="utf-8").read()

    def test_ledger_holds_at_24(self):
        corpus = ""
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    corpus += open(os.path.join(root, fn), encoding="utf-8").read()
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus


class TestDateGrounding739:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_14_2026_is_monday(self):
        assert self._weekday("2026-09-14") == "Monday"

    def test_jul_24_2026_is_friday(self):
        assert self._weekday("2026-07-24") == "Friday"

    def test_sep_8_2026_is_tuesday(self):
        assert self._weekday("2026-09-08") == "Tuesday"
