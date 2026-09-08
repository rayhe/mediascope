"""
Type C #599: Vox Media AI-revenue architecture (Sep 2026 status verification) +
writer-level behavioral pin (Victoria Song).

FINANCIAL MAP (verified Sep 2026):
  Leg 1: Vox Media-OpenAI content licensing + product partnership (May 29, 2024,
         multiyear, terms undisclosed). Bounded Sep 2026 searches surfaced NO
         termination/cancellation/renegotiation news -> treated as still ACTIVE.
         Post-PMC-acquisition transfer to PMX remains UNRESOLVED (disclosed, not claimed).
  Leg 2: Google programmatic ad-revenue dependence of Vox/PMC properties (in-corpus).
  Leg 3: Meta pays $0 in AI licensing (in-corpus).

BEHAVIORAL PIN: Victoria Song (The Verge senior reviewer, wearables beat) scored
Google's first-gen Pixel Watch (-0.35 illustrative) harsher than Meta's first-gen
Ray-Ban Display glasses (-0.10 illustrative): illustrative delta +0.13 n.s.,
writer-level falsification of the deal-gradient prediction. The incentive map is
verified at the financial layer; its behavioral reach is bounded by writer-level
register constancy.

Statistical discipline (standing rule, Aug 28 2026): illustrative hand-scores
only; p_value deliberately NOT_CALCULATED; is_significant False; no empirical
significance claims.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_FILE_NAME = "test_type_c_599_vox_media_ai_revenue_architecture_sep08.py"

META_TONES = [-0.1, 0.0, 0.1]
GOOGLE_TONES = [-0.35, 0.1]

META_URLS = [
    "https://thehotjem.com/meta-ray-ban-display-glasses-a-new-frontier-of-smart-wearables/",
    "https://www.wazupnaija.com/counting-renaissance-butts-in-rome-with-the-meta-ray-ban-display/",
    "https://www.Uploadvr.com/meta-ray-ban-display-hands-on-meta-neural-band/",
]
GOOGLE_URLS = [
    "https://www.androidauthority.com/google-pixel-watch-buyers-guide-3221637/",
    "https://hardware.slashdot.org/story/25/08/20/2113247/googles-pixel-watch-4-has-a-big-focus-on-ai?sdsrc=nextbtmprev",
]


def load_yaml(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as f:
        return yaml.safe_load(f)


def song_block():
    doc = load_yaml("profiles/careers/journalists.yaml")
    for j in doc["journalists"]:
        name = j.get("name", "")
        if "Victoria Song" in name or "Song" in name:
            cc = j.get("competitor_coverage") or {}
            key = "type_c_599_victoria_song_vox_financial_stack_behavioral_pin"
            if key in cc:
                return cc[key]
    raise AssertionError("Victoria Song #599 block not found in journalists.yaml")


def verge_openai_leg():
    doc = load_yaml("profiles/the-verge.yaml")
    for rel in doc.get("revenue_relationships", []):
        if rel.get("partner") == "OpenAI" and rel.get("relationship_type") == "licensing":
            return rel
    raise AssertionError("Vox Media-OpenAI licensing leg not found in the-verge.yaml")


class TestYamlAndEntry:
    def test_journalists_yaml_parses(self):
        doc = load_yaml("profiles/careers/journalists.yaml")
        assert isinstance(doc.get("journalists"), list)

    def test_the_verge_yaml_parses(self):
        doc = load_yaml("profiles/the-verge.yaml")
        assert isinstance(doc.get("revenue_relationships"), list)

    def test_song_block_present(self):
        block = song_block()
        assert block["iteration"] == 599
        assert block["type"] == "C"
        assert block["mechanism_id"] == 593
        assert block["date"] == "2026-09-08"

    def test_song_corpus_shape(self):
        block = song_block()
        assert len(block["meta_corpus"]) == 3
        assert len(block["google_corpus"]) == 2
        for item in block["meta_corpus"] + block["google_corpus"]:
            assert item.get("source_url", "").startswith("http")
            assert "tone" in item
            assert "Evidence tier" in item.get("notes", "")

    def test_verge_openai_leg_has_sep2026_verification(self):
        leg = verge_openai_leg()
        desc = leg.get("description", "")
        assert "#599" in desc
        assert "ACTIVE" in desc
        assert "UNRESOLVED" in desc

    def test_verge_openai_leg_core_facts(self):
        leg = verge_openai_leg()
        desc = leg.get("description", "")
        assert "May 29, 2024" in desc
        assert leg.get("date_established") == "2024-05-29"
        assert leg.get("estimated_value") == "undisclosed (multi-year)"
        assert len(leg.get("source_urls", [])) >= 2


class TestFinancialArchitecture:
    def test_leg1_openai_licensing_active(self):
        leg = verge_openai_leg()
        desc = leg.get("description", "")
        assert "Vox Media signed a content licensing and product partnership with OpenAI" in desc
        assert "NO termination, cancellation, or renegotiation" in desc

    def test_leg1_terms_undisclosed(self):
        leg = verge_openai_leg()
        assert "undisclosed" in leg.get("estimated_value", "")

    def test_leg1_union_friction_recorded(self):
        leg = verge_openai_leg()
        desc = leg.get("description", "")
        assert "Vox Media Union" in desc or "WGAE" in desc

    def test_leg2_google_ad_revenue_in_corpus(self):
        raw = open(os.path.join(REPO_ROOT, "profiles/the-verge.yaml"),
                   encoding="utf-8").read()
        assert "depends on Google programmatic ad revenue" in raw

    def test_leg3_meta_zero_licensing_in_corpus(self):
        raw = open(os.path.join(REPO_ROOT, "profiles/the-verge.yaml"),
                   encoding="utf-8").read()
        assert "Meta pays The Verge's parent $0 for AI content" in raw

    def test_three_legs_all_present(self):
        # The incentive stack is exactly these three legs; no fourth leg invented.
        leg = verge_openai_leg()
        raw = open(os.path.join(REPO_ROOT, "profiles/the-verge.yaml"),
                   encoding="utf-8").read()
        assert leg is not None
        assert "depends on Google programmatic ad revenue" in raw
        assert "Meta pays The Verge's parent $0 for AI content" in raw

    def test_deal_conflict_significance_recorded(self):
        leg = verge_openai_leg()
        desc = leg.get("description", "")
        assert "CONFLICT SIGNIFICANCE" in desc
        assert "OpenAI is Meta's direct competitor" in desc

    def test_no_deal_value_invented(self):
        # Terms were never disclosed; the corpus must not claim a dollar figure.
        leg = verge_openai_leg()
        desc = leg.get("description", "")
        assert "$" not in desc.replace("$0", "").replace("AI licensing", ""), \
            "no dollar figure may be attached to the OpenAI licensing leg"


class TestStatusVerification:
    def test_bounded_searches_documented(self):
        block = song_block()
        method = block.get("research_method", "")
        assert "Vox Media OpenAI content licensing deal status 2026" in method
        assert "Vox Media PMC acquisition completed OpenAI licensing deal" in method

    def test_bounded_absence_discipline(self):
        # iteration-492 rule: bounded absence is a documented search outcome, not a fact.
        block = song_block()
        assert "bounded-absence" in block.get("research_method", "")
        leg = verge_openai_leg()
        assert "bounded Sep 2026 searches" in leg.get("description", "")

    def test_pmx_transfer_disclosed_not_claimed(self):
        leg = verge_openai_leg()
        desc = leg.get("description", "")
        assert "UNRESOLVED" in desc
        assert "disclosed, not claimed" in desc

    def test_verdict_bounds_not_refutes(self):
        block = song_block()
        verdict = block.get("verdict", "")
        assert "BOUNDED" in verdict
        assert "real money" in verdict
        assert "bounded by writer-level constancy" in verdict


class TestBehavioralPin:
    def test_meta_tones_match_block(self):
        block = song_block()
        tones = [item["tone"] for item in block["meta_corpus"]]
        assert tones == META_TONES

    def test_google_tones_match_block(self):
        block = song_block()
        tones = [item["tone"] for item in block["google_corpus"]]
        assert tones == GOOGLE_TONES

    def test_source_urls_verbatim(self):
        block = song_block()
        meta_urls = [item["source_url"] for item in block["meta_corpus"]]
        google_urls = [item["source_url"] for item in block["google_corpus"]]
        assert meta_urls == META_URLS
        assert google_urls == GOOGLE_URLS

    def test_delta_arithmetic(self):
        block = song_block()
        res = block["asymmetry_scorer_result_illustrative"]
        target_avg = round(sum(META_TONES) / len(META_TONES), 4)
        peer_avg = round(sum(GOOGLE_TONES) / len(GOOGLE_TONES), 4)
        assert abs(target_avg - 0.0) < 1e-9
        assert abs(peer_avg - (-0.125)) < 1e-9
        assert abs((target_avg - peer_avg) - 0.125) < 1e-9
        assert res["delta"] == 0.13
        assert res["target_avg"] == 0.0
        assert res["peer_avg"] == -0.125

    def test_delta_sign_opposite_money_prediction(self):
        # Deal gradient predicts softer Google (negative delta: Meta - Google < 0).
        # Observed delta is positive: Song scored Google's first-gen watch harsher.
        block = song_block()
        res = block["asymmetry_scorer_result_illustrative"]
        assert res["delta"] > 0
        assert "OPPOSITE sign" in res["delta_direction"]

    def test_privacy_frame_tracks_camera_not_company(self):
        block = song_block()
        verdict = block.get("verdict", "")
        assert "tracks the camera, not the corporate payer" in verdict


class TestStatisticalDiscipline:
    def test_p_value_not_calculated(self):
        block = song_block()
        res = block["asymmetry_scorer_result_illustrative"]
        assert res["p_value"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        block = song_block()
        res = block["asymmetry_scorer_result_illustrative"]
        assert res["is_significant"] is False

    def test_correlation_not_causation(self):
        block = song_block()
        res = block["asymmetry_scorer_result_illustrative"]
        assert res["correlation_not_causation"] is True

    def test_methodology_discloses_manual_illustrative(self):
        block = song_block()
        res = block["asymmetry_scorer_result_illustrative"]
        assert "MANUAL ILLUSTRATIVE" in res["methodology"]
        assert "NOT an empirical measurement" in res["methodology"]

    def test_no_false_significance_language(self):
        raw = open(os.path.join(REPO_ROOT, "profiles/careers/journalists.yaml"),
                   encoding="utf-8").read()
        start = raw.find("type_c_599_victoria_song_vox_financial_stack_behavioral_pin")
        seg = raw[start:start + 20000]
        assert "statistically significant" not in seg.lower()


class TestConfoundersCounterevidence:
    def test_confounders_graded(self):
        block = song_block()
        confs = block.get("confounders", [])
        assert len(confs) >= 4
        assert any(c.startswith("[STRONG]") for c in confs)
        assert any(c.startswith("[MODERATE]") for c in confs)
        assert any(c.startswith("[WEAK]") for c in confs)

    def test_counterevidence_present(self):
        block = song_block()
        ce = block.get("counterevidence", [])
        assert len(ce) >= 3

    def test_counterevidence_names_scope_limit(self):
        # The falsification is register-scoped: her broader Meta narrative register
        # is privacy-adversarial. A blanket Meta-favorable reading would be wrong.
        block = song_block()
        joined = " ".join(block.get("counterevidence", []))
        assert "privacy-adversarial" in joined
        assert "register-scoped" in joined


class TestNoveltyAndRotation:
    def test_exactly_one_599_test_file(self):
        files = glob.glob(os.path.join(os.path.dirname(__file__),
                                       "test_type_c_599*.py"))
        assert len(files) == 1 and os.path.basename(files[0]) == TEST_FILE_NAME, \
            f"Exactly one 599 test file must exist, got {files}"

    def test_no_type_c_599_commit_yet(self):
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "--grep=#599", "--format=%H"],
            capture_output=True, text=True, check=True)
        assert out.stdout.strip() == "", \
            f"#599 already committed: {out.stdout.strip()}"

    def test_mechanism_593_zero_precommit_hits(self):
        # mechanism_593 is created by this run; the only hits allowed are in
        # this run's own files (the test file itself + journalists.yaml block).
        # git grep exits 1 on no matches, so check the output, not the code.
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "grep", "-l", "mechanism_593", "HEAD", "--",
             "profiles", "tests", "docs", "README.md"],
            capture_output=True, text=True)
        assert out.stdout.strip() == "", \
            f"mechanism_593 already in committed tree: {out.stdout.strip()}"

    def test_rotation_type_and_number(self):
        block = song_block()
        assert block["type"] == "C"
        assert block["iteration"] == 599


class TestRotationCycleGuard599:
    # POST_COMMIT_ANCHOR placeholder; patched to the main-commit short hash
    # in the followup commit per the #565 convention.
    ANCHORED_COMMIT = "PENDING"

    # MAIN_COMMIT_PATTERN: only main-iteration commits anchor the rotation.
    # Followup ("Type C #599 followup: ...") and doc-sync commits interleave
    # between mains since the #572/#573/#574 convention change; the naive
    # newest-5 filter broke on them. The colon immediately after the iteration
    # number distinguishes mains.
    MAIN_COMMIT_PATTERN = re.compile(r"^Type [A-E] #\d+:")

    @staticmethod
    def _git_main_subjects(n=5):
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "log", "-n40",
             TestRotationCycleGuard599.ANCHORED_COMMIT, "--format=%s"],
            capture_output=True, text=True, check=True)
        mains = [s for s in out.stdout.splitlines()
                 if TestRotationCycleGuard599.MAIN_COMMIT_PATTERN.match(s)]
        return mains[:n]

    def test_git_commit_order_matches_rotation(self):
        subjects = self._git_main_subjects()
        assert len(subjects) >= 5, f"fewer than 5 main commits: {subjects}"
        expected = [
            ("#599", "C"),
            ("#598", "B"),
            ("#597", "A"),
            ("#596", "E"),
            ("#595", "D"),
        ]
        for i, (num, typ) in enumerate(expected):
            assert num in subjects[i], \
                f"position {i}: expected {num}, got {subjects[i]!r}"
            assert re.search(rf"Type {typ} {re.escape(num)}", subjects[i]), \
                f"position {i}: expected Type {typ} {num}, got {subjects[i]!r}"

    def test_rotation_adjacency_cycle_valid(self):
        # C->B is the edge this run closes; the full 5-window must be a
        # rotation walk in commit-newest-first order: C,B,A,E,D (the rotation
        # runs backward in newest-first order). (order[a] - order[b]) % 5 == 1
        # steps one position backward from the newer commit a to the older
        # commit b, i.e. one rotation step forward.
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        subjects = self._git_main_subjects()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append(m.group(1))
        assert observed == ["C", "B", "A", "E", "D"]
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, \
                f"rotation broken: {a} -> {b} is not a valid cycle edge"

    def test_no_duplicate_iteration_numbers_in_window(self):
        subjects = self._git_main_subjects()
        nums = [re.search(r"#(\d+):", s).group(1) for s in subjects[:5]]
        assert len(nums) == len(set(nums)), \
            f"duplicate iteration numbers in window: {nums}"
