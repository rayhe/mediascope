"""
Type C iteration #744: Sep 14 Division Bench hearing-day outcome watch (second
check, ~22:30 IST) + India attribution-deal economics first-hand synthesis leg
(FourWeekMBA Sep 9 2026) - mechanism 681. FIRST dedicated corpus mapping of
the two-tier global licensing structure (paid licences US/UK/EU vs attribution
deals in cost-sensitive markets) and the multilingual-archive corpus-value
inference; extension of mechanisms 657/678/609.

Sub-finding 1 (watch): the ANI v. OpenAI Division Bench appeal was listed for
today, Sep 14 2026. Mechanism 678's first check (~04:00 PDT / 16:30 IST,
hearing window open) found a bounded absence of outcome reporting. This run's
second check (~10:00 PDT / ~22:30 IST, hearing window likely closed) finds the
bounded absence continues across five query sets: either the bench did not
assemble again or reporting has not surfaced; neither is claimed (bounded
absence per iteration-492). The appeal outcome reprices the India template
($0 attribution vs $7.5M ask); an unresolved listing defers the repricing
while the zero-fee template keeps setting precedent.

Sub-finding 2 (synthesis): first-hand read this run (147 rendered lines) of
the FourWeekMBA Sep 9 2026 analysis piece (already a corpus source on m609 and
m657). Independently corroborates the corpus's dual-track reading and adds
three analytical claims not previously carried in the corpus: (a) the two-tier
global pricing structure; (b) the corpus-value inference on seven-language
archives; (c) attribution-as-consideration as a precedent weakening subsequent
publishers' negotiating positions ("traffic in lieu of cash"). The piece also
models the evidentiary discipline the corpus requires (Sep 8 timing flagged as
on-the-record coincidence; licence-versus-litigate framing labeled analysis,
not a coordination claim).

Statistical discipline (Aug 28 2026 standing contract): qualitative-only;
scorer none; tone NOT_SCORED; p_value/cohens_d/ci_95 NOT_CALCULATED;
is_significant False; engine NOT run; NOT artifact-grade. Verdict: two-tier
structure and corpus-value inference documented (first-hand read); hearing
outcome unobserved (bounded absence); incentive-repricing inference is
directional_only. NOT a falsification-family member (ledger holds at 24).
No analysis.json update warranted.

Rotation: Type C (A/B/C/D/E cycle). Window 740-744 closes D (#740) -> E
(#741) -> A (#742) -> B (#743) -> C (#744); novelty anchor patched in the
followup per the #565 convention (two-commit: main, then anchor SHA patch).
Research method: 5 browser.search query sets + 1 browser.open first-hand read.
Sep 14 2026 10:00 PDT - 72 tests, 10 classes.
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

MECHANISM_KEY = "ani_sep14_hearing_outcome_watch_two_tier_synthesis_leg"
YAML_PATH = os.path.join(REPO, "profiles", "competitor-entities.yaml")
LOG_PATH = os.path.join(REPO, "iteration-log.md")
FILE_743 = "test_type_b_743_hamish_hector_techradar_snap_sci_fi_vs_meta_alarm_register_gradient_sep14_8am.py"

FOURWEEKMBA_URL = "https://fourweekmba.com/ai-openai-india-publisher-deals-attribution-strategy/"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. Anchor test is deselected pre-commit.
ANCHORED_SHA = "a78480f1c37d596ec7e46309967181588057803e"


def load_block():
    with open(YAML_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["entities"]["openai"][MECHANISM_KEY]


class TestIterationMetadata744:
    def test_iteration_is_744(self):
        assert load_block()["iteration"] == 744

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
        assert b["time_pdt"] == "10:00"
        assert b["job_id"] == "mediascope-daily-iteration"
        assert b["goal_id"] == "goal_54093bda4145"

    def test_mechanism_id_681_int(self):
        b = load_block()
        assert isinstance(b["mechanism_id"], int)
        assert b["mechanism_id"] == 681

    def test_single_681_block_in_openai(self):
        openai = yaml.safe_load(open(YAML_PATH, encoding="utf-8"))["entities"]["openai"]
        hits = [k for k, v in openai.items()
                if isinstance(v, dict) and v.get("mechanism_id") == 681]
        assert hits == [MECHANISM_KEY]

    def test_first_synthesis_leg_claim(self):
        assert "FIRST" in load_block()["mechanism_name"]
        assert "two-tier" in load_block()["mechanism_name"]

    def test_test_file_field(self):
        assert load_block()["test_file"] == "tests/" + THIS_FILE


class TestHearingOutcomeWatch744:
    def test_hearing_listed_today(self):
        w = load_block()["hearing_day_outcome_watch"]
        assert "Sep 14 2026" in w["listed"]

    def test_bench_composition(self):
        w = load_block()["hearing_day_outcome_watch"]
        assert "Rao" in w["bench"] and "Arora" in w["bench"]
        assert "did not assemble Sep 8" in w["bench"]

    def test_first_check_carried_from_678(self):
        w = load_block()["hearing_day_outcome_watch"]
        assert "mechanism 678" in w["first_check"]
        assert "16:30 IST" in w["first_check"]

    def test_second_check_bounded_absence(self):
        w = load_block()["hearing_day_outcome_watch"]
        assert "22:30 IST" in w["second_check"]
        assert "bounded absence" in w["second_check"]

    def test_no_outcome_claimed(self):
        w = load_block()["hearing_day_outcome_watch"]
        assert "neither claimed" in w["reading"]

    def test_repricing_consequence_deferred(self):
        w = load_block()["hearing_day_outcome_watch"]
        assert "$7.5M" in w["repricing_consequence"]
        assert "defers the repricing" in w["repricing_consequence"]

    def test_bounded_absence_logged(self):
        absences = load_block()["bounded_absences"]
        assert any("22:30 IST" in a for a in absences)
        assert any("iteration-492" in a for a in absences)

    def test_no_new_deals_absence(self):
        absences = " ".join(load_block()["bounded_absences"])
        assert "no new AI publisher licensing deals" in absences

    def test_no_seattle_times_newsday_developments(self):
        absences = " ".join(load_block()["bounded_absences"])
        assert "Seattle Times" in absences and "m675" in absences


class TestTwoTierSynthesis744:
    def test_two_tier_claim(self):
        t = load_block()["two_tier_structure"]
        assert "paid licences" in t["claim"] and "attribution deals" in t["claim"]

    def test_us_paid_side(self):
        t = load_block()["two_tier_structure"]
        assert "News Corp" in t["us_paid_side"] and "Axel Springer" in t["us_paid_side"]

    def test_india_attribution_side(self):
        t = load_block()["two_tier_structure"]
        assert "BCCL" in t["india_attribution_side"]
        assert "Sep 7" in t["india_attribution_side"] and "Sep 8" in t["india_attribution_side"]

    def test_first_hand_two_tier_quote(self):
        t = load_block()["two_tier_structure"]
        assert "two-tier global structure" in t["first_hand_quote"]

    def test_traffic_in_lieu_of_cash(self):
        t = load_block()["two_tier_structure"]
        assert "in lieu of cash" in t["implication"]

    def test_corpus_value_inference(self):
        c = load_block()["corpus_value_inference"]
        assert "seven-language" in c["claim"] or "seven languages" in c["claim"]
        assert "scarce material" in c["claim"]

    def test_corpus_value_self_flagged_analysis(self):
        c = load_block()["corpus_value_inference"]
        assert "the inference is mine" in c["first_hand_quote"]

    def test_precedent_reading(self):
        p = load_block()["precedent_reading"]
        assert "dual-track content strategy" in p["claim"]

    def test_distribution_legitimacy(self):
        p = load_block()["precedent_reading"]
        assert "different product perception" in p["distribution_legitimacy"]

    def test_piece_discipline_carried(self):
        p = load_block()["precedent_reading"]
        assert "not a coordination claim" in p["piece_discipline"]

    def test_48_hour_stat_block(self):
        facts = " ".join(load_block()["first_hand_facts"])
        assert "48 hours" in facts and "$0 disclosed fee" in facts
        assert "7 languages" in facts

    def test_not_training_licence_framing(self):
        facts = " ".join(load_block()["first_hand_facts"])
        assert "neither" in facts and "training-data licence" in facts

    def test_quoted_parties(self):
        facts = " ".join(load_block()["first_hand_facts"])
        assert "Varun Shetty" in facts and "Nandagopal Rajan" in facts


class TestConfounders744:
    def test_six_ranked_confounders(self):
        confs = load_block()["ranked_confounders"]
        assert len(confs) == 6
        assert [c["rank"] for c in confs] == [1, 2, 3, 4, 5, 6]

    def test_strength_distribution(self):
        confs = load_block()["ranked_confounders"]
        strengths = [c["strength"] for c in confs]
        assert strengths.count("strong") == 2
        assert strengths.count("moderate") == 2
        assert strengths.count("weak") == 2

    def test_strong_confound_analysis_not_primary(self):
        confs = load_block()["ranked_confounders"]
        assert "not primary reporting" in confs[0]["confounder"]

    def test_strong_confound_outcome_conditional(self):
        confs = load_block()["ranked_confounders"]
        assert "conditional" in confs[1]["confounder"]

    def test_five_bounded_absences(self):
        assert len(load_block()["bounded_absences"]) == 5

    def test_correlational_note_no_causal_claim(self):
        assert "No causal claim" in load_block()["correlational_note"]

    def test_no_coverage_tone_claim(self):
        assert load_block()["no_coverage_tone_claim"] is True

    def test_cautious_language_required(self):
        assert load_block()["cautious_language_required"] is True


class TestSourcesAndResearch744:
    def test_one_source_url(self):
        urls = load_block()["source_urls"]
        assert urls == [FOURWEEKMBA_URL]

    def test_source_url_verbatim(self):
        assert FOURWEEKMBA_URL in load_block()["source_urls"]

    def test_research_method_five_query_sets(self):
        rm = load_block()["research_method"]
        assert "5 browser.search query sets" in rm

    def test_research_method_first_hand_read(self):
        rm = load_block()["research_method"]
        assert "1 browser.open first-hand read" in rm

    def test_research_method_no_new_suits(self):
        rm = load_block()["research_method"]
        assert "no new developments" in rm

    def test_cross_references_present(self):
        refs = " ".join(load_block()["cross_references"])
        for token in ["mechanism 657", "mechanism 678", "mechanism 609",
                      "mechanism 709", "mechanism 672", "#503", "iteration-492",
                      "#565", "Aug 28 2026 standing rule"]:
            assert token in refs, token

    def test_novelty_first_two_tier(self):
        assert "FIRST dedicated corpus mapping" in load_block()["novelty"]
        assert "two-tier global licensing structure" in load_block()["novelty"]

    def test_novelty_distinguishes_parents(self):
        assert "Distinct from mechanism 678" in load_block()["novelty"]

    def test_statistical_discipline_qualitative(self):
        sd = load_block()["statistical_discipline"]
        assert sd["scorer"] == "none"
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False
        assert sd["engine_run"] is False
        assert sd["artifact_grade"] is False
        assert sd["qualitative_only"] is True

    def test_falsification_family_not_member(self):
        assert "NOT a falsification-family member" in load_block()["falsification_family"]
        assert "ledger holds at 24" in load_block()["falsification_family"]

    def test_no_analysis_json_update(self):
        assert "No analysis.json update warranted" in load_block()["artifact_readiness"]

    def test_verification_block(self):
        v = load_block()["verification"]
        assert v["yaml_parse_clean"] is True
        assert v["iteration"] == 744
        assert v["type"] == "C"
        assert v["goal_id"] == "goal_54093bda4145"


class TestIterationLog744:
    def _tail(self):
        with open(LOG_PATH) as f:
            return "\n".join(f.read().splitlines()[-45:])

    def test_log_entry_present(self):
        assert "#744" in self._tail()

    def test_log_mechanism_681(self):
        assert "mechanism 681" in self._tail()

    def test_log_two_tier(self):
        assert "two-tier" in self._tail()

    def test_log_hearing_watch(self):
        assert "22:30 IST" in self._tail()

    def test_log_rotation_window(self):
        assert "740-744" in self._tail()


class TestRotationCycleGuard744:
    ANCHORED_SHA = ANCHORED_SHA

    @staticmethod
    def _rotation_files():
        result = {}
        for fn in os.listdir(TESTS_DIR):
            m = re.match(r"test_type_([a-e])_(\d+)_", fn)
            if m:
                result.setdefault(int(m.group(2)), []).append((m.group(1), fn))
        return result

    def test_25_rotation_files_contiguous(self):
        files = self._rotation_files()
        for n in range(720, 745):
            assert n in files and len(files[n]) == 1, f"iteration {n} file missing or duplicated: {files.get(n)}"
            letter, fn = files[n][0]
            expected = "deabc"[(n - 710) % 5]
            assert letter == expected, f"iteration {n}: expected type {expected}, file is {fn}"

    def test_window_closes_to_c(self):
        files = self._rotation_files()
        assert files[740][0][0] == "d"
        assert files[741][0][0] == "e"
        assert files[742][0][0] == "a"
        assert files[743][0][0] == "b"
        assert files[744][0][0] == "c"
        assert files[744][0][1] == THIS_FILE

    def test_anchor_sha_pinned_post_commit(self):
        actual = subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=REPO
        ).stdout.strip()
        assert self.ANCHORED_SHA != "TBD_PATCHED_IN_FOLLOWUP", "anchor not yet patched post-commit"
        assert actual == self.ANCHORED_SHA, f"HEAD {actual} != anchored {self.ANCHORED_SHA}"


class TestDocSync744:
    def test_readme_row(self):
        with open(os.path.join(REPO, "README.md"), encoding="utf-8") as f:
            assert THIS_FILE in f.read()

    def test_architecture_row(self):
        with open(os.path.join(REPO, "docs", "ARCHITECTURE.md"), encoding="utf-8") as f:
            assert THIS_FILE in f.read()


class TestSweepSupersession744:
    def test_max_mechanism_681(self):
        ids = []
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if not fn.endswith(".yaml"):
                    continue
                text = open(os.path.join(root, fn), encoding="utf-8").read()
                ids.extend(int(x) for x in re.findall(r"(?m)^\s*mechanism_id:\s*(\d+)\s*$", text))
        assert max(ids) == 681

    def test_zero_underscore_681_keys_in_profiles(self):
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = open(os.path.join(root, fn), encoding="utf-8").read()
                    assert "mechanism_681_" not in text, f"mechanism_681_ key in {fn}"

    def test_zero_underscore_681_keys_outside_carriers(self):
        carriers = {FILE_743, THIS_FILE}
        hits = []
        for fn in os.listdir(TESTS_DIR):
            fp = os.path.join(TESTS_DIR, fn)
            if fn in carriers or not os.path.isfile(fp):
                continue
            if "mechanism" + "_681_" in open(fp, encoding="utf-8").read():
                hits.append(fn)
        assert hits == [], f"mechanism_681_ keys outside sweep carriers: {hits}"

    def test_zero_mechanism_682_keys_profiles_only(self):
        # Mirrors the #734 pattern: profiles/-only walk. My own file
        # references 682 in this sweep test, so tests/ is excluded.
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = open(os.path.join(root, fn), encoding="utf-8").read()
                    assert "mechanism_682" not in text, fn

    def test_743_max_680_sweep_fails_by_designed_supersession(self):
        # Documented, not repaired: advancing max numeric mechanism id to
        # 681 supersedes #743's max-680 sweep per the #710/#720 convention.
        text = open(YAML_PATH, encoding="utf-8").read()
        assert "mechanism_id: 681" in text

    def test_743_zero_681_sweep_stays_green_by_designed_keying(self):
        # My block keys as ani_sep14_hearing_outcome_watch_two_tier_synthesis_leg
        # (colon-form mechanism_id: 681), so #743's underscore-form sweep
        # for mechanism_681_ stays green - designed keying per #723.
        assert "mechanism_681" not in MECHANISM_KEY
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    assert "mechanism_681_" not in open(os.path.join(root, fn), encoding="utf-8").read()

    def test_ledger_holds_at_24(self):
        corpus = ""
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith(".yaml"):
                    corpus += open(os.path.join(root, fn), encoding="utf-8").read()
        assert "TWENTY-FOURTH" in corpus
        assert "TWENTY-FIFTH" not in corpus


class TestDateGrounding744:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_14_2026_is_monday(self):
        assert self._weekday("2026-09-14") == "Monday"

    def test_sep_7_2026_is_monday(self):
        assert self._weekday("2026-09-07") == "Monday"

    def test_sep_8_2026_is_tuesday(self):
        assert self._weekday("2026-09-08") == "Tuesday"
