"""Type A #657: The Verge x Snap Specs Sep-2026 shipping-phase event register
vs Meta LED-tamper surveillance-alarm register (mechanism 628).

First dedicated Type A mechanism under the-verge.yaml
competitor_relationships.snap (zero prior snap entity key in that block;
both register-evidence URLs new-to-corpus per repo-wide grep this run).
Shipping-phase extension of the Aug 9 2026 Verge x Snap Specs deep dive
(commit 17b7cf4), which pinned the Meta LED-tamper tone at -0.2.

Snap arm (event-forward product register, Sep 2026 pre-ship, n=1):
 The Verge's Specs launch-event piece (973155) ahead of the Sep 16 event
 / fall shipping window carries an event-forward product register: demos,
 developers, demand, price. No surveillance language in the surfaced
 characterization. +0.2 MANUAL ILLUSTRATIVE. Evidence tier
 excerpt_bounded: theverge.com returned a policy block for browser.open
 this run (single attempt, not retried), so existence/topic are verified
 via the Glass Almanac Sep-2026 citation of the verbatim Verge URL; the
 register is inferred from topic/title-class, not a first-hand read.

Meta arm (surveillance-alarm register, Jul 7 2026, n=1):
 Victoria Song's "Meta's glasses will turn off the camera if you tamper
 with the privacy light", surfaced via the thetechstreetnow.com reprint
 (which states "Copyright of this story solely belongs to
 theverge.com"). The canonical Verge URL is unattested and is NOT
 invented per the no-canonical-URL rule. -0.2 MANUAL ILLUSTRATIVE,
 carried from the Aug 9 block.

Scorer MANUAL ILLUSTRATIVE: illustrative delta (Snap minus Meta) +0.40.
n=1 per arm: degenerate statistical contract (p=1.0, d=0.0); engine NOT
run, no divergence pin. No empirical significance claimed or computed.

Financial context: aligned-incentive (indirect). Snap Specs ship with
OpenAI API integration and Google Gemini integration (both Meta AI
competitors); OpenAI x Vox Media/PMC licensing deal (May 29 2024)
treated ACTIVE per #599; Google = programmatic ad dependence; Meta $0
(PMC sold ALL Meta shares Q2 2025, mechanism #112). SECOND-ORDER claim:
no direct Snap-to-Vox-Media payment is on record (the documented Snap
publisher payment, $58M Discover revenue-share 2016 + $2-4M/yr flat
fees, ran to Conde Nast, mechanism 239). Correlate only.

Strong counterevidence bounds it to register-specific, not
valence-general: Vergecast "Snap's Specs look good on nobody" (The
Verge IS willing to be negative about Snap on product grounds);
TechCrunch Aug 3 2026 hard questions on Specs preorder numbers (by a
competitor publication, not The Verge); mechanism #75 Song bifurcated
mode (writer-lane, not publisher-incentive).

NOT a falsification-family member (no named financial gradient
contradicted).

Rotation: Type A follows Type E (#656) per A,B,C,D,E. Rotation guard
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
PROFILE_PATH = os.path.join(REPO_ROOT, "profiles", "the-verge.yaml")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = (
    "mechanism_628_verge_snap_sep_specs_event_vs_meta_"
    "led_tamper_alarm_sep10"
)

VERGE_SNAP_EVENT_URL = (
    "https://www.theverge.com/tech/973155/"
    "snap-is-hosting-a-specs-launch-event-in-september"
)
SNAP_ATTRIBUTION_URL = (
    "https://glassalmanac.com/they-want-to-try-specs-ignites-debate-as-"
    "snap-posts-19-revenue-lift-in-2026/"
)
VERGE_META_LED_TAMPER_REPRINT_URL = (
    "https://thetechstreetnow.com/metas-glasses-will-turn-off-the-camera-"
    "if-you-tamper-with-the-privacy-light/"
)
TECHCRUNCH_SNAP_SIDESTEP_URL = (
    "https://techcrunch.com/2026/08/03/"
    "snap-ceo-sidesteps-specs-pre-order-questions-on-q2-earnings-call/"
)

TARGET_SCORES = [0.2]
PEER_SCORES = [-0.2]
TARGET_AVG = 0.2
PEER_AVG = -0.2
EXPECTED_DELTA = 0.40


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
    return _profile()["competitor_relationships"]["snap"]


def _mechanism():
    return _entity()[MECH_KEY]


def _read(path):
    with open(os.path.join(REPO_ROOT, path)) as fh:
        return fh.read()


class TestIterationMetadata657:
    def test_iteration_number(self):
        assert 657 == 657

    def test_type_a(self):
        assert _mechanism()["iteration_type"] == "A"

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 628

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
        assert ids.count(628) == 1
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

    def test_pair_names_verge_snap_vs_meta(self):
        assert "The Verge x Snap" in _mechanism()["pair"]
        assert "Meta" in _mechanism()["pair"]

    def test_iteration_time_sep10_2pm(self):
        assert _mechanism()["iteration_time"] == "2026-09-10 14:00 PDT"


class TestSnapEntityStructure657:
    def test_entity_has_indirect_tie(self):
        entity = _entity()
        assert entity["financial_tie"] == "indirect"

    def test_no_direct_verge_snap_deal_on_record(self):
        entity = _entity()
        text = yaml.dump(entity)
        assert "No direct content licensing or advertising deal" in text
        assert "NOT Vox Media" in text

    def test_entity_value_names_openai_google_channels(self):
        entity = _entity()
        assert "OpenAI" in entity["estimated_value"]
        assert "Google" in entity["estimated_value"]

    def test_coverage_prediction_softer(self):
        assert _entity()["coverage_prediction"] == "softer"

    def test_mechanism_nested_under_snap(self):
        assert MECH_KEY in _entity()

    def test_meta_entity_zero_tie(self):
        meta = _profile()["competitor_relationships"]["meta"]
        assert meta["financial_tie"] == "none"
        assert meta["estimated_value"] == "$0"


class TestToneScorer657:
    def test_target_scores(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert m["target_scores_MANUAL_ILLUSTRATIVE"] == TARGET_SCORES

    def test_peer_scores(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert m["peer_scores_MANUAL_ILLUSTRATIVE"] == PEER_SCORES

    def test_delta_calc(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert m["delta_manual_illustrative"] == pytest.approx(EXPECTED_DELTA)
        assert m["target_avg"] - m["peer_avg"] == pytest.approx(EXPECTED_DELTA)

    def test_article_tones_match_scorer_arms(self):
        mech = _mechanism()
        assert mech["snap_articles"][0]["manual_illustrative_tone"] == TARGET_AVG
        assert mech["meta_articles"][0]["manual_illustrative_tone"] == PEER_AVG

    def test_degenerate_contract_documented(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "p=1.0, d=0.0" in m["engine_degenerate"]
        assert "NOT run" in m["engine_degenerate"]

    def test_finding_layer_refuses(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "NOT_CALCULATED" in m["finding_layer"]
        assert "is_significant False" in m["finding_layer"]

    def test_manual_illustrative_label_present(self):
        m = _mechanism()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "MANUAL ILLUSTRATIVE" in m["methodology"]
        assert "DO NOT claim empirical significance" in m["methodology"]


class TestRegisterAnalysis657:
    def test_snap_register_event_forward_product(self):
        art = _mechanism()["snap_articles"][0]
        assert art["register"] == "event_forward_product"

    def test_meta_register_surveillance_alarm(self):
        art = _mechanism()["meta_articles"][0]
        assert art["register"] == "surveillance_alarm"

    def test_snap_event_url_verbatim(self):
        art = _mechanism()["snap_articles"][0]
        assert art["url"] == VERGE_SNAP_EVENT_URL

    def test_snap_evidence_tier_excerpt_bounded(self):
        art = _mechanism()["snap_articles"][0]
        assert art["evidence_tier"] == "excerpt_bounded"
        assert "browser policy" in art["framing"]

    def test_snap_attribution_url_present(self):
        art = _mechanism()["snap_articles"][0]
        assert art["source_attribution_url"] == SNAP_ATTRIBUTION_URL

    def test_meta_evidence_tier_mirror_bounded(self):
        art = _mechanism()["meta_articles"][0]
        assert art["evidence_tier"] == "mirror_bounded"
        assert art["url"] == VERGE_META_LED_TAMPER_REPRINT_URL
        assert "thetechstreetnow.com" in art["url"]

    def test_meta_byline_song_jul7(self):
        art = _mechanism()["meta_articles"][0]
        assert art["byline"] == "Victoria Song"
        assert art["date"] == "2026-07-07"

    def test_meta_canonical_url_not_invented(self):
        art = _mechanism()["meta_articles"][0]
        assert "unattested" in art["canonical_url_note"]
        assert "not invented" in art["canonical_url_note"]

    def test_snap_window_sep2026_pre_ship(self):
        art = _mechanism()["snap_articles"][0]
        assert "2026-09" in art["date"]
        assert "Sep 16" in art["framing"] or "Sep-16" in art["framing"] or "Sep 16" in art["date"]

    def test_register_evidence_urls_in_block(self):
        text = yaml.dump(_mechanism())
        for url in (
            VERGE_SNAP_EVENT_URL,
            SNAP_ATTRIBUTION_URL,
            VERGE_META_LED_TAMPER_REPRINT_URL,
        ):
            assert url in text, url


class TestFinancialContext657:
    def test_predictor_aligned_incentive_indirect(self):
        fc = _mechanism()["financial_context"]
        assert fc["predictor"] == "aligned_incentive (indirect)"
        assert fc["prediction"] == "softer_than_expected"

    def test_deal_chain_names_openai_google_meta(self):
        fc = _mechanism()["financial_context"]
        assert "OpenAI" in fc["chain"]
        assert "Google" in fc["chain"]
        assert "May 29 2024" in fc["chain"]
        assert "$0" in fc["chain"]

    def test_status_correlate_only_second_order(self):
        fc = _mechanism()["financial_context"]
        assert "correlate only" in fc["status"]
        assert "SECOND-ORDER" in fc["status"]

    def test_no_direct_deal_claim(self):
        fc = _mechanism()["financial_context"]
        assert "DO NOT claim a direct Verge-Snap deal" in fc["status"]

    def test_conde_nast_boundary_named(self):
        fc = _mechanism()["financial_context"]
        assert "Conde Nast" in fc["status"]


class TestConfounders657:
    def _confounders(self):
        return _mechanism()["confounders_ranked"]

    def test_three_strong_confounders(self):
        assert len(self._confounders()["strong"]) == 3

    def test_excerpt_bounded_strong(self):
        strong = " ".join(self._confounders()["strong"])
        assert "Excerpt-bounded Verge register" in strong

    def test_genre_phase_skew_strong(self):
        strong = " ".join(self._confounders()["strong"])
        assert "Genre/phase skew" in strong

    def test_time_window_skew_strong(self):
        strong = " ".join(self._confounders()["strong"])
        assert "Time-window skew" in strong

    def test_three_moderate_confounders(self):
        assert len(self._confounders()["moderate"]) == 3

    def test_mirror_bounded_moderate(self):
        moderate = " ".join(self._confounders()["moderate"])
        assert "Mirror-bounded Meta evidence" in moderate

    def test_scale_asymmetry_moderate(self):
        moderate = " ".join(self._confounders()["moderate"])
        assert "Scale asymmetry" in moderate

    def test_byline_asymmetry_moderate(self):
        moderate = " ".join(self._confounders()["moderate"])
        assert "Byline asymmetry" in moderate

    def test_two_weak_confounders(self):
        assert len(self._confounders()["weak"]) == 2

    def test_n1_degenerate_weak(self):
        weak = " ".join(self._confounders()["weak"])
        assert "n=1 per arm" in weak

    def test_counterevidence_three_items(self):
        ce = _mechanism()["counterevidence"]
        assert len(ce) == 3

    def test_counterevidence_vergecast_negative_on_snap(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "Vergecast" in ce
        assert "look good on nobody" in ce

    def test_counterevidence_techcrunch_hard_questions(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "TechCrunch" in ce
        assert "sidesteps" in ce
        text = yaml.dump(_mechanism())
        assert TECHCRUNCH_SNAP_SIDESTEP_URL in text

    def test_counterevidence_song_bifurcated_mode(self):
        ce = " ".join(_mechanism()["counterevidence"])
        assert "#75" in ce
        assert "bifurcated" in ce


class TestNovelty657:
    def test_zero_test_files_pre_commit(self):
        assert glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_a_657*")
        ) == [os.path.join(REPO_ROOT, "tests", TEST_BASENAME)]

    def test_type_a_657_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; the main
        # commit exists exactly once post-commit and its SHA matches the
        # rotation-guard anchor patched in the followup. Novelty was
        # verified pre-commit by shell greps (zero test_type_a_657 files,
        # no Type A #657 in git log, zero mechanism_628 keys, both
        # register-evidence URLs new to corpus); this test pins that no
        # duplicate #657 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type A #657:", l)]
        assert len(mains) == 1, (
            "expected exactly one Type A #657 main commit, got: %r" % (mains,)
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard657.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, "main commit %s != guard anchor %s" % (sha, anchor)

    def test_distinct_from_aug9_deep_dive(self):
        xrefs = _mechanism()["cross_references"]
        assert any("17b7cf4" in x for x in xrefs)
        finding = _mechanism()["finding"]
        assert "Shipping-phase extension" in finding

    def test_sibling_of_653(self):
        xrefs = _mechanism()["cross_references"]
        assert any("#653" in x for x in xrefs)

    def test_not_falsification_member(self):
        finding = _mechanism()["finding"]
        assert "Not a falsification-family member" in finding

    def test_no_657_mechanism_collision(self):
        # No other mechanism in the-verge.yaml is keyed for iteration 657.
        text = _read("profiles/the-verge.yaml")
        assert text.count("iteration: 657") == 1


class TestRotationCycleGuard657:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #657 main-commit SHA is known.
    ANCHORED_SHA = "6b4703c2edda415491aef1b83ecc6a4d5c97aa12"  # patched in followup per #565 convention

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

    def test_window_653_657_closes_e_to_a(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("A", "657"),
            ("E", "656"),
            ("D", "655"),
            ("C", "654"),
            ("B", "653"),
        ], "rotation window 653-657 wrong: %r" % (observed,)

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
            line for line in result.stdout.splitlines() if "Type A #657:" in line
        ]
        main = mains[0].split()[0] if mains else ""
        assert self.ANCHORED_SHA == main, (
            "anchor patched in followup per #565 convention"
        )


class TestDocSync657:
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
        assert "test_type_a_657" in text

    def test_iteration_log_entry_657(self):
        text = _read("iteration-log.md")
        assert "#657" in text or "657" in text


class TestNoBrittlePatterns657:
    def test_yaml_reparses_clean(self):
        _profile()

    def test_no_em_dash_in_mechanism(self):
        text = yaml.dump(_mechanism(), allow_unicode=False)
        assert "\\u2014" not in text
        assert "—" not in text

    def test_all_urls_http_or_https(self):
        text = yaml.dump(_mechanism())
        urls = re.findall(r"https?://[^\s'\"]+", text)
        assert len(urls) >= 3
        for u in urls:
            assert u.startswith("https://"), u

    def test_research_method_documented(self):
        mech = _mechanism()
        assert "research_method" in yaml.dump(mech)
        assert "browser.search" in mech["research_method"]

    def test_no_verge_canonical_url_invented_for_meta_reprint(self):
        # Per the no-canonical-URL rule: the Meta arm must not carry an
        # invented theverge.com article URL; the reprint URL is the only
        # https URL on the Meta arm.
        art = _mechanism()["meta_articles"][0]
        text = yaml.dump(art)
        assert art["url"] == VERGE_META_LED_TAMPER_REPRINT_URL
        urls = re.findall(r"https?://[^\s'\"]+", text)
        assert urls == [VERGE_META_LED_TAMPER_REPRINT_URL], urls

    def test_snap_verge_url_is_verbatim_search_surface(self):
        # The Snap arm's theverge.com URL is verbatim from the browser.search
        # Full-URL listing (Glass Almanac citing it), not constructed.
        art = _mechanism()["snap_articles"][0]
        assert art["url"] == VERGE_SNAP_EVENT_URL
        assert art["evidence_tier"] == "excerpt_bounded"
