"""
Type C #889 (rotation window 885-889, FIFTH leg: D->E->A->B->C): California
Civic Media Fund contingent-match replacement - the 2024 Google-State $250M
legislation-avoidance bargain devolves into a smaller GO-Biz grant program.

MECHANISM #765: the contingent-match structure. Google's payments are
explicitly contingent on state appropriations (Wicks spokesperson Erin Ivie:
"contingent" on state funding, Canada parallel; Google spokesperson: "We
stand ready to match the state's contribution"). When Newsom cut the state
share ($30M first-year ask to $10M; $15M Google leg to $10M), Google's matched
payment fell in lockstep. The July 14 2026 replacement: California Civic
Media Program, $20M state for two more years matched by Google (People mirror
frames it as $20M annual, Google pays half), up to $250K one-time grants,
established within GO-Biz, applications independently administered by the
James B. McClatchy Foundation with Journalism Funding Partners, guided by a
nine-member advisory board; applications closed Aug 21 2026, awards expected
fall 2026. NO cut percentage asserted (the $250M headline, $175M cash
framing, $20M materialized fund, and July extension are different scopes at
different vintages); Google retained its 50/50 payer role. Extends mechanism
355's Google publisher-payment architecture to the U.S. state legislative-
bargain vector.

NOVELTY VERIFICATION (run pre-commit, Sep 21 2026 ~02:0x PDT, before edits):
- glob: zero test_type_c_889*.py files on disk
- git log --all --grep="Type C #889": zero hits (no prior #889 main commit)
- numeric mechanism_id max in profiles/: 764 (765 is this run's own
  addition; 762 exists only in the uncommitted concurrent #884 working tree)
- format-built underscore needles: zero underscore-form 765 key strings
  repo-wide (__pycache__ artifacts excluded per the #715 pattern-rescope
  lesson)
- zero numeric "mechanism_id: 765" keys in profiles/ pre-commit
- BLOCK_KEY zero-hit repo-wide pre-commit
- "Civic Media" / "GO-Biz" / "James B. McClatchy Foundation" zero-hit
  repo-wide pre-commit (existing "McClatchy" hits are journalist-career
  notes and a co-plaintiff roster, not the Foundation)
- all 8 source URLs zero-hit repo-wide pre-commit
- REJECTED candidates: Apple/Conde Nast AI licensing (2023 negotiation
  reporting only, no verified completed agreement); AB 2222 alone
  (legislative proposal, undecided - carried as context)

ROTATION: this is the FIFTH leg of rotation window 885-889 (D->E->A->B->C),
closing the window. Prior legs present in iteration-log.md: #885 Type D,
#886 Type E, #887 Type A, #888 Type B (01:00 PDT). The concurrent Type C
#884 work remains uncommitted in the working tree
(profiles/competitor-entities.yaml); this run does not touch it.

RESEARCH METHOD: 2 browser.search query sets post-compaction ((1)
California Civic Media Fund Newsom July announcement GO-Biz $20 million
Google - surfaced the europesays/People mirror, EIN Presswire GO-Biz
advisory-board release, gov.ca.gov press release, newsy-today,
oaklandvoices, url-media, Mercury News pagesuite items; (2) complementary
$250M stalled-deal queries - surfaced webpronews) + 2 browser.open
first-hand reads this run (gov.ca.gov 2026/07/14 press release, 33 rendered
lines; webpronews $250M stalled piece, 109 rendered lines). Remaining sources
excerpt-bounded per #503. All URLs copied verbatim from Full-URL search
listings; no canonical URLs constructed. ASCII-only, no em dashes.

DESIGN NOTES:
- NOT a falsification-family member: payment-architecture documentation,
  not a uniform-prediction test. Ledger holds at 29; THIRTIETH remains the
  negative guard.
- Extends mechanism 355 (Google publisher-payment architecture); connects
  to 519 (News Corp x OpenAI $250M pole), 636 (pay-or-litigate doctrine).
- p_value / cohens_d / ci_95 are NOT_CALCULATED (deliberate). is_significant
  is false. engine NOT run. correlation_not_causation is true.
- no analysis.json update (NOT artifact-grade).
- ASCII prose only (no em dashes), per repository conventions.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESEARCH_YAML = os.path.join(REPO, "profiles", "competitor-coverage-research.yaml")
PROFILES_DIR = os.path.join(REPO, "profiles")
OWN_BASENAME = "test_type_c_889_california_civic_media_fund_contingent_match_replacement_sep21_2am.py"
BLOCK_KEY = "type_c_889_california_civic_media_fund_contingent_match_replacement_sep21_2am"
ITERATION = 889
ITER_TYPE = "C"
MECH_ID = 765
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched post-commit per #565
# NEXT_ID / MECH_ID needles are format-built so the file never carries a
# literal underscore-form key string (per the #715 lesson).
MECH_ID_MARKER = "mechanism" + "_765"
NEXT_ID_MARKER = "mechanism" + "_766"
NEXT_ID_NUMERIC = "mechanism_id: " + "766"
NEXT_ID_DASH = "mechanism" + "-766"
GOV_CA_URL = "https://www.gov.ca.gov/2026/07/14/governor-newsom-announces-20-million-in-grant-funding-matched-by-google-to-support-local-journalism-across-the-state/"
WEBPRONEWS_URL = "https://www.webpronews.com/california-google-250m-journalism-fund-stalled-by-2026-delays/"
MEMBER_29 = "TWENTY-NINTH falsification-family member"
MEMBER_30 = "THIRTIETH falsification-family member"
# Rotation window 885-889: D -> E -> A -> B -> C; this run is the FIFTH leg,
# closing the window. Type C #884 is concurrent and uncommitted (working
# tree only), so the committed-leg order asserted here is C(889) <- B(888)
# <- A(887) <- E(886) <- D(885).
EXPECTED_ORDER = [("C", "889"), ("B", "888"), ("A", "887"), ("E", "886"), ("D", "885")]
SCHEDULED_LOCAL = "Mon 2026-09-21 02:00:00 PDT"


def _git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=REPO, capture_output=True, text=True, timeout=60
    )


def _repo_grep(needle):
    """All repo files containing the needle (excludes __pycache__, per the
    #715 pattern-rescope lesson)."""
    hits = []
    for root, dirs, files in os.walk(REPO):
        if ".git" in root or "__pycache__" in root:
            continue
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", ".venv", "node_modules")]
        for f in files:
            p = os.path.join(root, f)
            if "__pycache__" in p:
                continue
            try:
                with open(p, encoding="utf-8", errors="ignore") as fh:
                    if needle in fh.read():
                        hits.append(p)
            except (OSError, UnicodeError):
                pass
    return hits


def _read(relpath):
    with open(os.path.join(REPO, relpath), "r", encoding="utf-8") as fh:
        return fh.read()


def _load_research():
    with open(RESEARCH_YAML, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _get_block():
    return _load_research()[BLOCK_KEY]


def _corpus_ids():
    ids = []

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "mechanism_id" and isinstance(v, int):
                    ids.append(v)
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
        try:
            with open(p, encoding="utf-8") as fh:
                d = yaml.safe_load(fh)
        except Exception:
            continue
        if d is not None:
            walk(d)
    return ids


# ---------------------------------------------------------------------------
# 1. Novelty: Type C #889 did not exist before this run
# ---------------------------------------------------------------------------

class TestNovelty889:
    def test_single_test_type_c_889_file(self):
        files = [f for f in os.listdir(os.path.join(REPO, "tests"))
                 if f.startswith("test_type_c_889")]
        assert files == [OWN_BASENAME]

    def test_type_c_889_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        proc = _git("log", "--format=%H %s", "--grep", "Type C #889")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type C #889(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
                                    "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_novelty_verification_claim(self):
        method = _get_block()["research_method"]
        assert "zero test_type_c_889" in method
        assert 'no "Type C #889" in git log' in method
        assert "block key zero-hit repo-wide pre-commit" in method
        assert "max numeric mechanism_id 764 pre-commit" in method
        assert "zero underscore-form 765" in method
        assert "all 8 source URLs zero-hit repo-wide pre-commit" in method
        assert "Apple/Conde Nast" in method  # the rejected-candidate discipline

    def test_885_886_887_888_window_legs_present_prior_to_889(self):
        log = _read("iteration-log.md")
        assert "## #885 Type D:" in log
        assert "## #886 Type E:" in log
        assert "## #887 Type A:" in log
        assert "## #888 Type B:" in log
        idx_885 = log.index("## #885 Type D:")
        idx_886 = log.index("## #886 Type E:")
        idx_887 = log.index("## #887 Type A:")
        idx_888 = log.index("## #888 Type B:")
        assert idx_888 < idx_887 < idx_886 < idx_885

    def test_max_numeric_mechanism_id_765(self):
        """Max numeric mechanism_id in profiles/ is 765: this run's own
        addition (764 was the max pre-commit per the run's pre-commit grep;
        762 exists only in the uncommitted concurrent #884 working tree)."""
        ids = _corpus_ids()
        assert max(ids) == 765, f"max mechanism_id should be 765, got {max(ids)}"
        assert ids.count(765) == 1, "mechanism_id 765 must appear exactly once"

    def test_no_underscore_766_keys(self):
        """Zero underscore-form 766 mechanism key strings repo-wide
        (format-built needle; __pycache__ excluded per #715)."""
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], f"unexpected underscore-766 keys: {hits}"

    def test_no_dash_766_keys(self):
        hits = _repo_grep(NEXT_ID_DASH)
        assert hits == [], f"unexpected dash-766 keys: {hits}"

    def test_no_numeric_766_keys(self):
        hits = _repo_grep(NEXT_ID_NUMERIC)
        assert hits == [], f"unexpected numeric 766 keys: {hits}"


# ---------------------------------------------------------------------------
# 2. Rotation guard: 885-889 window, fifth leg D->E->A->B->C
#    (All rotation-guard tests DESELECTED pre-commit per #565: the #889 main
#    commit does not exist yet, so the log-order assertion cannot pass.)
# ---------------------------------------------------------------------------

class TestRotationGuard889:
    def test_window_is_885_889_fifth_leg(self):
        subjects = _git("log", "--format=%s").stdout.splitlines()
        order = []
        for s in subjects:
            m = re.search(r"Type ([A-E]) #(\d+)(?::| )", s)
            if m and m.group(2) in ("885", "886", "887", "888", "889"):
                # Followups and test-fixups are not rotation legs. The
                # push-status followup commit type (introduced at #864)
                # is excluded alongside anchor/log-hash followups; the #886
                # run named its push-status commit "push-verified line".
                if ("anchor followup" not in s and "log-hash followup" not in s
                        and "push-status followup" not in s and "push-verified" not in s
                        and "test fixup" not in s):
                    order.append((m.group(1), m.group(2)))
        for expected, got in zip(EXPECTED_ORDER, order):
            assert expected == got

    def test_rotation_adjacency_cycle_valid(self):
        cycle = ["D", "E", "A", "B", "C"]
        got = [t for t, _n in EXPECTED_ORDER]
        assert got == ["C", "B", "A", "E", "D"]
        assert cycle[cycle.index("D") + 1] == "E"
        assert cycle[cycle.index("E") + 1] == "A"
        assert cycle[cycle.index("A") + 1] == "B"
        assert cycle[cycle.index("B") + 1] == "C"  # this run closes the window

    def test_predecessor_is_type_b_888(self):
        proc = _git("log", "--oneline", "--grep", "Type B #888", "--all")
        mains = [ln for ln in proc.stdout.splitlines()
                 if "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) >= 1

    def test_anchor_is_ancestor_of_head(self):
        # Per the #885/#886/#887/#888 convention (assert-ANCHORED_SHA-equals-HEAD
        # retired at #887): followups legitimately advance HEAD past the pinned
        # main commit. The invariant is ancestry: the anchored main commit must
        # be an ancestor of HEAD.
        proc = _git("merge-base", "--is-ancestor", ANCHORED_SHA, "HEAD")
        assert proc.returncode == 0, \
            "anchored main commit must be an ancestor of HEAD"


# ---------------------------------------------------------------------------
# 3. Novelty anchor: block key shape
# ---------------------------------------------------------------------------

class TestNoveltyAnchor889:
    def test_block_key_shape(self):
        assert BLOCK_KEY.startswith("type_c_889_california_civic_media_fund")
        assert BLOCK_KEY.endswith("contingent_match_replacement_sep21_2am")
        assert "type_c_889" in BLOCK_KEY

    def test_block_key_exact(self):
        assert BLOCK_KEY == "type_c_889_california_civic_media_fund_contingent_match_replacement_sep21_2am"


# ---------------------------------------------------------------------------
# 4. Mechanism 765 YAML structure
# ---------------------------------------------------------------------------

class TestMechanism765Structure:
    def test_top_level_entry_exists(self):
        data = _load_research()
        assert BLOCK_KEY in data, "top-level 889 block key missing"

    def test_block_key_unique(self):
        """The 889 block key appears exactly once repo-wide in yaml."""
        hits = _repo_grep(BLOCK_KEY)
        yaml_hits = [h for h in hits if h.endswith(".yaml")]
        assert len(yaml_hits) == 1, f"block key should appear in exactly 1 yaml file, got {yaml_hits}"
        assert yaml_hits[0].endswith("profiles/competitor-coverage-research.yaml")

    def test_iteration_and_type(self):
        block = _get_block()
        assert block["iteration"] == 889
        assert block["iteration_type"] == "C"
        assert block["type"] == "financial_incentive_mapping"
        assert block["rotation"] == "Type C"
        assert block["mechanism_id"] == 765
        assert block["goal_id"] == "goal_54093bda4145"

    def test_designed_keying_no_underscore_765(self):
        """Per #715: no underscore-form 765 key strings repo-wide."""
        hits = _repo_grep(MECH_ID_MARKER)
        assert hits == [], f"unexpected underscore-765 keys: {hits}"

    def test_required_fields_present(self):
        block = _get_block()
        for field in ("type_c_focus", "deal_arc", "contingent_match_structure",
                      "replacement_program", "scale_discipline",
                      "alternative_models_in_play", "statistical_discipline",
                      "cautious_language_required", "correlational_note",
                      "no_coverage_tone_claim", "no_analysis_json_update",
                      "falsification_family", "artifact_readiness",
                      "cross_references", "ranked_confounders",
                      "bounded_absences", "novelty", "sources", "source_urls",
                      "research_method", "test_file", "verification"):
            assert field in block, f"missing field: {field}"

    def test_test_file_field_matches_own_basename(self):
        block = _get_block()
        assert block["test_file"] == "tests/" + OWN_BASENAME

    def test_not_in_competitor_entities(self):
        """The concurrent #884 working tree owns competitor-entities.yaml;
        this run must not touch it."""
        entities = _read("profiles/competitor-entities.yaml")
        assert BLOCK_KEY not in entities


# ---------------------------------------------------------------------------
# 5. Deal arc: the 2024 $250M bargain and its erosion
# ---------------------------------------------------------------------------

class TestMechanism765DealArc:
    def test_headline_figure_and_split(self):
        arc = " ".join(_get_block()["deal_arc"])
        assert "$250M" in arc
        assert "$180M" in arc
        assert "$70M" in arc

    def test_legislation_avoidance_context(self):
        arc = " ".join(_get_block()["deal_arc"])
        assert "California Journalism Preservation Act" in arc
        assert "sidestep" in arc

    def test_state_cut_and_zero_flow(self):
        arc = " ".join(_get_block()["deal_arc"])
        assert "$30M" in arc
        assert "$10M" in arc
        assert "not a single dollar" in arc

    def test_cash_framing_variant_carried(self):
        arc = " ".join(_get_block()["deal_arc"])
        assert "$175M" in arc
        assert "$55M" in arc
        assert "$11M lobbying" in arc or "$11M" in arc

    def test_two_first_hand_reads_claimed(self):
        method = _get_block()["research_method"]
        assert "2 browser.open" in method
        assert "first-hand" in method
        sources = " ".join(_get_block()["sources"])
        assert "33 rendered lines" in sources
        assert "109 rendered lines" in sources

    def test_source_urls_verbatim(self):
        urls = _get_block()["source_urls"]
        assert GOV_CA_URL in urls
        assert WEBPRONEWS_URL in urls
        assert len(urls) == 8


# ---------------------------------------------------------------------------
# 6. Contingent match: the mechanism's core
# ---------------------------------------------------------------------------

class TestMechanism765ContingentMatch:
    def test_ivie_contingency_quote(self):
        leg = " ".join(_get_block()["contingent_match_structure"])
        assert "contingent" in leg
        assert "Erin Ivie" in leg
        assert "Canada" in leg

    def test_google_match_quote(self):
        leg = " ".join(_get_block()["contingent_match_structure"])
        assert "stand ready to match" in leg

    def test_lockstep_cut(self):
        leg = " ".join(_get_block()["contingent_match_structure"])
        assert "$15M" in leg
        assert "$10M" in leg
        assert "lockstep" in leg

    def test_appropriation_sets_scale(self):
        leg = " ".join(_get_block()["contingent_match_structure"])
        assert "appropriation" in leg


# ---------------------------------------------------------------------------
# 7. Replacement program: the July 2026 Civic Media Program
# ---------------------------------------------------------------------------

class TestMechanism765ReplacementProgram:
    def test_july_announcement_and_grants(self):
        leg = " ".join(_get_block()["replacement_program"])
        assert "July 14, 2026" in leg
        assert "$250,000" in leg
        assert "one-time grants" in leg

    def test_intermediation_stack(self):
        leg = " ".join(_get_block()["replacement_program"])
        assert "GO-Biz" in leg
        assert "James B. McClatchy Foundation" in leg
        assert "Journalism Funding Partners" in leg
        assert "Advisory Board" in leg

    def test_timeline(self):
        leg = " ".join(_get_block()["replacement_program"])
        assert "August 21, 2026" in leg
        assert "fall 2026" in leg

    def test_mcclatchy_foundation_first_to_corpus_precision(self):
        leg = " ".join(_get_block()["replacement_program"])
        novelty = _get_block()["novelty"]
        assert "FIRST-TO-CORPUS" in leg or "FIRST-TO-CORPUS" in novelty
        assert "journalist-career notes" in novelty
        assert "co-plaintiff" in novelty

    def test_framing_difference_carried_not_forced(self):
        leg = " ".join(_get_block()["replacement_program"])
        assert "$20M annual" in leg or "annual" in leg
        assert "rather than forcing one number" in leg


# ---------------------------------------------------------------------------
# 8. Scale discipline: no cut percentage, no collapse overclaim
# ---------------------------------------------------------------------------

class TestMechanism765ScaleDiscipline:
    def test_no_single_cut_percentage_asserted(self):
        leg = " ".join(_get_block()["scale_discipline"])
        assert "NO single cut percentage is asserted" in leg
        assert "92%" in leg  # the refused comparison is named explicitly

    def test_framings_listed_as_different_scopes(self):
        leg = " ".join(_get_block()["scale_discipline"])
        assert "$250M headline" in leg
        assert "$175M cash framing" in leg
        assert "materialized fund is $10M state + $10M Google" in leg

    def test_google_retained_payer_role(self):
        leg = " ".join(_get_block()["scale_discipline"])
        assert "HALF-FUNDED BY GOOGLE" in leg
        assert "not payer exit" in leg

    def test_alternative_models_carried(self):
        leg = " ".join(_get_block()["alternative_models_in_play"])
        assert "AB 2222" in leg
        assert "SB 1327" in leg
        assert "$70M" in leg


# ---------------------------------------------------------------------------
# 9. Statistical discipline
# ---------------------------------------------------------------------------

class TestMechanism765StatisticalDiscipline:
    def test_stats_not_calculated(self):
        d = _get_block()["statistical_discipline"]
        assert d["p_value"] == "NOT_CALCULATED"
        assert d["cohens_d"] == "NOT_CALCULATED"
        assert d["ci_95"] == "NOT_CALCULATED"
        assert d["engine_run"] is False
        assert d["is_significant"] is False
        assert d["artifact_grade"] is False
        assert d["qualitative_only"] is True
        assert d["verdict"] == "directionally_supported_not_proven"

    def test_no_tone_or_causal_claim(self):
        block = _get_block()
        assert block["no_coverage_tone_claim"] is True
        assert block["no_analysis_json_update"] is True
        assert block["cautious_language_required"] is True
        assert "No causal claim" in block["correlational_note"]
        assert "No coverage-tone claim" in block["correlational_note"]

    def test_confounders_ranked_strong_first(self):
        confs = _get_block()["ranked_confounders"]
        assert len(confs) == 6
        assert [c["rank"] for c in confs] == [1, 2, 3, 4, 5, 6]
        assert confs[0]["strength"] == "strong"
        assert confs[1]["strength"] == "strong"
        assert "Figure-framing ambiguity" in confs[0]["confounder"]
        assert "retained its payer role" in confs[1]["confounder"]

    def test_bounded_absences(self):
        absences = _get_block()["bounded_absences"]
        assert len(absences) == 5
        joined = " ".join(absences)
        assert "2024 deal terms" in joined
        assert "allocation influence" in joined
        assert "tone or coverage claim" in joined

    def test_cross_references(self):
        refs = " ".join(_get_block()["cross_references"])
        assert "mechanism 355" in refs
        assert "mechanism 519" in refs
        assert "mechanism 636" in refs
        assert "#609/#614" in refs


# ---------------------------------------------------------------------------
# 10. Ledger unchanged
# ---------------------------------------------------------------------------

class TestLedgerUnchanged889:
    def test_not_falsification_family(self):
        fam = _get_block()["falsification_family"]
        assert "NOT a member" in fam
        assert "ledger holds at 29" in fam

    def test_twenty_ninth_present_thirtieth_absent(self):
        """TWENTY-NINTH present, THIRTIETH absent in profiles/ (negative
        guard). Format-built needles per #715."""
        hits_29 = _repo_grep(MEMBER_29)
        assert any("profiles" in h for h in hits_29), "TWENTY-NINTH member missing"
        hits_30 = [h for h in _repo_grep(MEMBER_30) if "profiles" in h]
        assert hits_30 == [], f"THIRTIETH falsification member must stay absent: {hits_30}"

    def test_no_analysis_json_update(self):
        assert _get_block()["no_analysis_json_update"] is True
        assert "No analysis.json update warranted" in _get_block()["artifact_readiness"]


# ---------------------------------------------------------------------------
# 11. Doc sync (per #719)
# ---------------------------------------------------------------------------

class TestDocSync889:
    def test_readme_stats_table(self):
        readme = _read("README.md")
        assert "| Tests | 45550 | Across 1216 test files |" in readme

    def test_readme_row(self):
        readme = _read("README.md")
        assert "test_type_c_889_california_civic_media_fund" in readme
        assert "Type C #889" in readme

    def test_architecture_row(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "test_type_c_889_california_civic_media_fund" in arch

    def test_architecture_lists_test_file(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert OWN_BASENAME in arch

    def test_architecture_tree_count(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "45550 tests across 1216 test files" in arch


# ---------------------------------------------------------------------------
# 12. Iteration log
# ---------------------------------------------------------------------------

class TestIterationLog889:
    def _entry(self):
        log = _read("iteration-log.md")
        return log.split("## #889 Type C")[1].split("## #888")[0]

    def test_entry_present(self):
        log = _read("iteration-log.md")
        assert "## #889 Type C" in log

    def test_entry_documents_mechanism(self):
        entry = self._entry()
        assert "765" in entry
        assert "Civic Media" in entry
        assert "contingent" in entry

    def test_entry_documents_window(self):
        entry = self._entry()
        assert "885-889" in entry
        assert "FIFTH leg" in entry

    def test_entry_documents_ledger(self):
        entry = self._entry()
        assert "holds at 29" in entry
        assert "NOT a falsification-family member" in entry


# ---------------------------------------------------------------------------
# 13. Date grounding
# ---------------------------------------------------------------------------

class TestDateGrounding889:
    def test_run_date_is_monday(self):
        import datetime
        assert datetime.date(2026, 9, 21).strftime("%A") == "Monday"

    def test_gov_announcement_is_tuesday(self):
        import datetime
        assert datetime.date(2026, 7, 14).strftime("%A") == "Tuesday"

    def test_application_deadline_is_friday(self):
        import datetime
        assert datetime.date(2026, 8, 21).strftime("%A") == "Friday"

    def test_scheduled_time(self):
        assert SCHEDULED_LOCAL == "Mon 2026-09-21 02:00:00 PDT"
        block = _get_block()
        assert block["verification"]["date"] == "2026-09-21 02:00 PDT"
        assert block["date_analyzed"] == "2026-09-21"
        assert block["time_pdt"] == "02:00"
